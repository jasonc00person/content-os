---
name: post-content
description: "Post or schedule content to Instagram, YouTube, and TikTok via Buffer API. Can transcribe videos and generate captions automatically. Handles video upload, caption, scheduling, and multi-platform distribution. LinkedIn and Facebook can be added by connecting them in Buffer. Triggers: post this, schedule this, publish reel, post to instagram, post to all platforms, schedule reel, queue this video, post content, transcribe and post."
---

# Post Content — Multi-Platform Publisher

Transcribe a video, generate a caption, upload it, and post/schedule across all connected platforms via Buffer's API.

## How to Trigger
- **"post this video to all platforms"** + file path
- **"schedule this reel for tomorrow"** + file path
- **"post to instagram"** + file path + caption
- **"queue this video"** + file path
- **"transcribe and post this"** + file path (auto-generates caption from video content)

## Prerequisites
- Buffer API key in `.env` as `BUFFER_API_KEY`
- Platforms connected in Buffer dashboard (`publish.buffer.com/settings/channels`)
- Python `whisper` package installed for transcription (`pip install openai-whisper`)

## Platform Config

**Organization ID:** `69d6fa971fcceb5bb1fab20a`

**Channel IDs** (run "refresh channels" to update):
- Instagram: `69d6fab1031bfa423ce3e0d5`
- TikTok: `69df3f5b031bfa423c063c33`
- YouTube: `69df3f6a031bfa423c063c68`

*To add more platforms, connect them in Buffer (`publish.buffer.com/settings/channels`) then run the refresh channels query below.*

**Refresh channels query:**
```bash
export BUFFER_API_KEY=$(grep BUFFER_API_KEY /Users/jasoncooperson/Projects/content-os/.env | cut -d= -f2) && curl -s -X POST https://api.buffer.com \
  -H "Authorization: Bearer $BUFFER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "query { channels(input: { organizationId: \"69d6fa971fcceb5bb1fab20a\" }) { id name service type } }"}' | python3 -m json.tool
```
After connecting new platforms, run this and update the Channel IDs section above.

---

## Execution Steps

### Step 1 — Parse the Request

Determine from the user's message:
- **Video file path** — absolute path to the video file
- **Caption** — user-provided, or "transcribe and generate" if not provided
- **Platforms** — which platforms to post to (default: all connected)
- **Schedule** — post now, add to queue, or schedule for specific time
- **Content type** — short-form (Reel/Short/TikTok) or long-form (YouTube only)
- **CTA** — does the user want a specific call-to-action? (e.g., "comment POPPY")

### Step 2 — Transcribe Video (if no caption provided)

If the user doesn't provide a caption, transcribe the video first:

```bash
python3 -c "
import whisper
model = whisper.load_model('base')
result = model.transcribe('/path/to/video.mp4')
print(result['text'])
"
```

Then generate a caption based on the transcript:
- Read `backbone.md` for Jason's current positioning and voice
- The caption should sound like Jason — casual, direct, no-BS
- **CTA FIRST** — if there's a keyword CTA (e.g., "comment POPPY"), it MUST be the very first line of the caption. Viewers see the first 1-2 lines before "...more"
- Structure: CTA → hook/summary → bullet points or breakdown → closing CTA repeat
- Ask the user to confirm the caption before posting (unless they say "just post it")

### Step 3 — Upload Video to Temporary Host

Videos must be at a publicly accessible URL for Buffer.

**Use Litterbox (catbox temporary hosting) — supports up to 1GB, 72hr expiry:**
```bash
curl -s -F "reqtype=fileupload" -F "time=72h" -F "fileToUpload=@/path/to/video.mp4" https://litterbox.catbox.moe/resources/internals/api.php
```
Returns a direct URL like: `https://litter.catbox.moe/abc123.mp4`

**Then verify the URL returns correct headers:**
```bash
curl -sI https://litter.catbox.moe/abc123.mp4 | head -3
```
Must show `content-length` > 0. If content-length is 0, the upload failed — try again.

**IMPORTANT — Host selection (learned from testing):**
- **tmpfiles.org** — only works for files under ~100MB. Expires in ~60 min. Use ONLY for small files.
- **Litterbox (litterbox.catbox.moe)** — works for files up to 1GB. Expires in 72hrs. **USE THIS AS DEFAULT.**
- **catbox.moe (permanent)** — returns `content-length: 0` in headers. **DO NOT USE** — Buffer rejects it.
- Buffer requires the video URL to return a valid `content-length` header. Always verify after upload.

### Step 4 — Post to Each Platform

**CRITICAL: Use the JSON file method for API calls.** Do NOT try to inline GraphQL mutations with shell escaping — captions with quotes, emojis, and newlines WILL break. Instead:

1. Use Python to write a properly escaped JSON payload to a temp file
2. Use `curl -d @/tmp/payload.json` to send it

**The proven method:**

```bash
export BUFFER_API_KEY=$(grep BUFFER_API_KEY /Users/jasoncooperson/Projects/content-os/.env | cut -d= -f2)

python3 -c "
import json

caption = '''YOUR CAPTION HERE'''
video_url = 'https://litter.catbox.moe/abc123.mp4'

query = 'mutation CreatePost(\$input: CreatePostInput!) { createPost(input: \$input) { ... on PostActionSuccess { post { id text dueAt } } ... on MutationError { message } } }'

# Instagram
ig = {'query': query, 'variables': {'input': {
    'text': caption,
    'channelId': '69d6fab1031bfa423ce3e0d5',
    'schedulingType': 'automatic',
    'mode': 'shareNow',
    'metadata': {'instagram': {'type': 'reel', 'shouldShareToFeed': True}},
    'assets': {'videos': [{'url': video_url}]}
}}}
with open('/tmp/buffer_ig.json', 'w') as f: json.dump(ig, f)

# TikTok
tt = {'query': query, 'variables': {'input': {
    'text': caption,
    'channelId': '69df3f5b031bfa423c063c33',
    'schedulingType': 'automatic',
    'mode': 'shareNow',
    'assets': {'videos': [{'url': video_url}]}
}}}
with open('/tmp/buffer_tt.json', 'w') as f: json.dump(tt, f)

# YouTube
yt = {'query': query, 'variables': {'input': {
    'text': caption,
    'channelId': '69df3f6a031bfa423c063c68',
    'schedulingType': 'automatic',
    'mode': 'shareNow',
    'metadata': {'youtube': {
        'title': 'YOUR TITLE HERE',
        'privacy': 'public',
        'madeForKids': False,
        'notifySubscribers': True,
        'categoryId': '22'
    }},
    'assets': {'videos': [{'url': video_url}]}
}}}
with open('/tmp/buffer_yt.json', 'w') as f: json.dump(yt, f)
"

# Post to each platform
echo '=== INSTAGRAM ==='
curl -s -X POST https://api.buffer.com \
  -H "Authorization: Bearer $BUFFER_API_KEY" \
  -H "Content-Type: application/json" \
  -d @/tmp/buffer_ig.json | python3 -m json.tool

echo '=== TIKTOK ==='
curl -s -X POST https://api.buffer.com \
  -H "Authorization: Bearer $BUFFER_API_KEY" \
  -H "Content-Type: application/json" \
  -d @/tmp/buffer_tt.json | python3 -m json.tool

echo '=== YOUTUBE ==='
curl -s -X POST https://api.buffer.com \
  -H "Authorization: Bearer $BUFFER_API_KEY" \
  -H "Content-Type: application/json" \
  -d @/tmp/buffer_yt.json | python3 -m json.tool
```

#### Platform-Specific Requirements

| Platform | Required Metadata | Notes |
|----------|------------------|-------|
| Instagram | `type: reel`, `shouldShareToFeed: true` | Min 3 seconds |
| TikTok | None | Video URL must stay live until published |
| YouTube | `title`, `privacy`, `madeForKids`, `notifySubscribers`, `categoryId` | categoryId `"22"` = People & Blogs |
| LinkedIn | None | More professional tone |
| Facebook | None | Casual tone OK |

#### YouTube Category IDs
- `"22"` — People & Blogs (default for creator content)
- `"28"` — Science & Technology (for AI/tech content)
- `"26"` — How-to & Style (for tutorials)
- `"24"` — Entertainment

### Scheduling Modes

| Mode | When to use | `mode` value | `dueAt` required? |
|------|------------|-------------|-------------------|
| Post now | "post this" (default) | `shareNow` | No |
| Add to queue | "queue this" | `addToQueue` | No |
| Next in queue | "post this next" | `shareNext` | No |
| Specific time | "schedule for April 20 at 3pm" | `customScheduled` | Yes (ISO 8601 UTC) |

For `customScheduled`, convert user's time to UTC ISO 8601 format: `2026-04-20T19:00:00.000Z`
Jason is in **Central Time (CT)** — UTC-5 (CDT) or UTC-6 (CST).

### Step 5 — Confirm

Report results for each platform:
```
Posted to:
  Instagram Reel — queued (next slot: [time])
  TikTok — queued (next slot: [time])
  YouTube Short — queued (next slot: [time])

Caption: [first 2 lines...]
Video: [filename]
```

If any platform fails, report the error and still post to the others.

---

## Caption Writing Guidelines

When generating captions from transcripts:

1. **CTA FIRST** — if there's a keyword CTA, it's ALWAYS line 1. This is what appears before "...more" in the feed.
2. **Hook line** — after the CTA, a 1-line hook that makes people want to read more
3. **Body** — key points from the video. Use arrows (→) or line breaks, not numbered lists
4. **Closing CTA** — repeat the keyword CTA at the bottom with 👇
5. **Voice** — casual, direct, uses emojis sparingly. Sounds like a text from a friend, not a press release.
6. **Length** — IG max 2,200 chars, TikTok max 2,200 chars, LinkedIn max 3,000 chars
7. **YouTube** — needs a separate `title` field (max 100 chars). Keep it short and curiosity-driven.

---

## Common Commands

**"post this reel"** — Upload video, post to all platforms as short-form, add to queue
**"transcribe and post"** — Transcribe video, generate caption, confirm, then post
**"schedule for tomorrow at 10am"** — Upload video, schedule across all platforms
**"post to IG only"** — Upload video, post only to Instagram
**"post long-form to YouTube"** — Upload video, post as full YouTube video (not Short)

---

## Lessons Learned (from testing)

### What broke and how to avoid it

1. **Shell escaping hell** — NEVER try to inline captions with quotes/emojis into a curl command or raw GraphQL string. Captions contain double quotes, single quotes, emojis, and newlines — shell escaping WILL fail. **Always use the Python → JSON file → `curl -d @file.json` method.**

2. **Python urllib gets blocked by Cloudflare** — Buffer's API blocks Python's default urllib user agent. **Always use curl** for the actual API calls, not Python urllib/requests.

3. **tmpfiles.org has a ~100MB limit** — Real video files are often 50-200MB. **Use Litterbox (litterbox.catbox.moe) as the default host** — supports up to 1GB.

4. **catbox.moe returns content-length: 0** — Buffer rejects URLs with zero content-length. **Never use catbox.moe (permanent)**, only use Litterbox (temporary).

5. **YouTube requires `categoryId`** — The `youtube` metadata object requires a `categoryId` string field or the API returns a validation error. Default to `"22"` (People & Blogs).

6. **Instagram requires `shouldShareToFeed: true`** — Without this boolean the API returns a validation error.

7. **Instagram reels must be at least 3 seconds** — Buffer will reject shorter videos.

8. **Load API key with grep, not source** — Use `export BUFFER_API_KEY=$(grep BUFFER_API_KEY /path/.env | cut -d= -f2)` instead of `source .env` which doesn't always propagate to subshells properly.

9. **Always verify the upload URL** — After uploading to any host, `curl -sI <url> | head -3` to confirm `content-length` > 0 before passing to Buffer.
