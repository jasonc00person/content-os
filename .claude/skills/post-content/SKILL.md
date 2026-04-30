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
- `uv` installed (transcription auto-installs `faster-whisper` into a cached venv on first run — no manual pip step)

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

### Step 1.5 — Resolve the file path (DON'T SKIP)

User-pasted paths frequently have **curly apostrophes/quotes** (`'`, `'`, `"`, `"`) where the real file uses straight ones, or vice versa. Filenames also include spaces, em-dashes, and emoji that the chat client may rewrite. **Never trust the pasted path verbatim — always verify with `ls` first.**

```bash
ls -lh "/full/pasted/path.mp4" 2>/dev/null || \
  ls -lh "$(dirname '/full/pasted/path.mp4')" | grep -iE "keyword1|keyword2"
```

If the direct `ls` fails, run the directory listing and grep for distinctive words from the filename (e.g. `starting.over`, `v1`). Then **copy the actual filename character-for-character** from the `ls` output — never retype it. The cleanest move is to assign it to a shell variable up front so every later command uses the same exact string:

```bash
VIDEO="/Users/jasoncooperson/Downloads/Every post feels like a you’re starting over from scratch v1.mp4"
ls -lh "$VIDEO"  # confirm before continuing
```

Note the byte size — if it's >100MB, you must use Litterbox in Step 3 (tmpfiles.org will reject it).

### Step 2 — Transcribe Video (if no caption provided)

Use `faster-whisper` via `uv` — same setup the `video-editor` skill uses. `uv` auto-installs the package into a cached venv on first run, so no `pip install` is required. **Run this in the background** alongside the upload in Step 3 — together they take 1-3 min on a 5-min clip and there's no reason to wait sequentially.

```bash
export UV_PROJECT_ENVIRONMENT="$HOME/.cache/video-editor-venv"
uv run --quiet --python 3.11 --with "faster-whisper" --with "onnxruntime" python - <<'PY'
from faster_whisper import WhisperModel
model = WhisperModel("large-v3", device="auto", compute_type="int8")
segments, info = model.transcribe("$VIDEO", vad_filter=True, language="en")
print(" ".join(seg.text.strip() for seg in segments))
PY
```

**Important:** the heredoc is single-quoted (`<<'PY'`), so `$VIDEO` won't expand inside it. Either substitute the path into the script before running, or pass it via `sys.argv`:

```bash
uv run --quiet --python 3.11 --with "faster-whisper" --with "onnxruntime" python - "$VIDEO" <<'PY'
import sys
from faster_whisper import WhisperModel
model = WhisperModel("large-v3", device="auto", compute_type="int8")
segments, info = model.transcribe(sys.argv[1], vad_filter=True, language="en")
print(" ".join(seg.text.strip() for seg in segments))
PY
```

Run it with `run_in_background: true` and poll/notify on the output file. Don't use stock `openai-whisper` — it isn't installed on this machine and `pip install` is slow + brittle.

Then generate a caption based on the transcript:
- Read `CA Backbone Apr 26 2026.md` and `voice-dna.md` for Jason's current positioning, ICP, and voice patterns
- The caption should sound like Jason — casual, direct, no-BS
- **CTA FIRST** — if there's a keyword CTA (e.g., "comment POPPY"), it MUST be the very first line of the caption. Viewers see the first 1-2 lines before "...more"
- Structure: CTA → hook/summary → bullet points or breakdown → closing CTA repeat
- Default: just post it. Only ask for caption confirmation if the user said "draft a caption first" or similar — Jason's standing preference is execute, then report.

### Step 3 — Upload Video to Temporary Host

Videos must be at a publicly accessible URL for Buffer. **Run this in the background in parallel with Step 2 (transcription)** — the upload of a 300MB+ file takes 30-90s and there's no reason to block on it sequentially.

**Use Litterbox (catbox temporary hosting) — supports up to 1GB, 72hr expiry:**
```bash
curl -s -F "reqtype=fileupload" -F "time=72h" -F "fileToUpload=@$VIDEO" https://litterbox.catbox.moe/resources/internals/api.php
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

Every post requires **both** `schedulingType` and `mode`. The two fields are NOT interchangeable — `schedulingType` is always `"automatic"` for these flows, and `mode` carries the actual share strategy.

| Use case | User says | `schedulingType` | `mode` | `dueAt`? |
|----------|-----------|------------------|--------|----------|
| Post now | "post this" (default) | `automatic` | `shareNow` | — |
| Add to queue | "queue this" | `automatic` | `addToQueue` | — |
| Next in queue | "post this next" | `automatic` | `shareNext` | — |
| Specific time | "schedule for April 20 at 3pm" / "tomorrow at noon" | `automatic` | `customScheduled` | Yes — ISO 8601 UTC |

For `customScheduled`, convert user's time to UTC ISO 8601 format: `2026-04-20T19:00:00.000Z`. Jason is in **Central Time (CT)** — UTC-5 (CDT) or UTC-6 (CST). For a vague "tomorrow" with no time specified, default to **noon CT (17:00 UTC during CDT, 18:00 UTC during CST)** — that's a solid mid-day post slot.

### Step 5 — Update Notion Pipeline

After at least one platform post succeeds, find the matching row in the Notion Content Database and mark it **Posted**. Buffer is the source of truth for actual publish state — Notion's job ends the moment we've handed the post off, so a successful Buffer response = Posted in Notion regardless of whether it goes live now or next week. This eliminates the entire "Scheduled" sync problem.

**Database ID:** `21bf6585-5e6b-81df-b692-e0321083dffa` (same as `notion-content-pipeline` skill)

**Post Date — always derive from Buffer's response:**
- The Buffer `createPost` mutation returns `post.dueAt` (ISO 8601 UTC) on success — this is the actual publish time Buffer has assigned, whether `shareNow`, queued, or scheduled.
- Pass the full ISO 8601 timestamp directly into Notion's `Post Date.start` so the entry includes both date AND time. Convert to Central Time offset for readability: `2026-04-30T15:00:00-05:00` (CDT) or `-06:00` (CST).
- Notion's date property accepts the full ISO 8601 string with time + offset and renders date + time in the UI.
- If `dueAt` is missing for any reason, fall back to the current local timestamp (`date +"%Y-%m-%dT%H:%M:%S%z"` then reformat to use a colon in the offset).

**Matching logic:**
1. Derive a search string from the video filename — strip extension and version/final suffixes (`v1`, `_v2`, `-final`, `(1)`). Also use any title Jason referenced in the request.
2. Call `mcp__notion__API-post-search` with the search string as `query`, `filter: {"property": "object", "value": "page"}`, `page_size: 50`.
3. Filter results to pages where `parent.database_id` = `21bf6585-5e6b-81df-b692-e0321083dffa`.
4. **One match** → patch it (see below).
5. **Multiple matches** → list the candidate titles to Jason and ask which one. Don't guess.
6. **No match** → report `Notion: no matching pipeline row found — skipped` and continue. Don't auto-create. The weekly reconciliation pass (future) will catch ad-hoc posts.

**Patch the page** with `mcp__notion__API-patch-page`:
```json
{
  "page_id": "[matched page ID]",
  "properties": {
    "Status": { "status": { "name": "Posted" } },
    "Post Date": { "date": { "start": "2026-04-30T15:00:00-05:00" } }
  }
}
```

If the Notion update fails for any reason, **don't fail the whole flow** — the post already went out. Report the Notion error in Step 6 and move on.

### Step 6 — Confirm

Report results for each platform plus the Notion update:
```
Posted to:
  Instagram Reel — queued (next slot: [time])
  TikTok — queued (next slot: [time])
  YouTube Short — queued (next slot: [time])

Notion: "[matched title]" → Posted (2026-04-30)

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

10. **Curly quotes/apostrophes in filenames break paths** — When the user pastes a filename like `you're starting over.mp4`, the chat client may render the apostrophe as the curly Unicode form (`'`, U+2019) while the actual file on disk uses the straight ASCII form (`'`, U+0027), or vice versa. **Always `ls` the path first.** If it fails, `ls` the parent directory and grep for distinctive keywords, then copy the real filename from the output into a `$VIDEO` shell variable so every subsequent command uses the same byte sequence. Do not retype filenames.

11. **`openai-whisper` is not installed; use `faster-whisper` via `uv`** — The previous version of this skill referenced `pip install openai-whisper`. That package is not installed on this machine and pip is slow/brittle. The `video-editor` skill's pattern (`uv run --with "faster-whisper" --with "onnxruntime"`) auto-installs into a cached venv and works on the first run. Reuse that pattern.

12. **Run upload + transcription in parallel as background tasks** — Both take 30s-3min on a typical 100-400MB clip. Kick them off with `run_in_background: true`, do other prep work in the meantime, and post once both complete. Sequential = 2x wall-clock for no reason.

13. **Parallel tool-call cancellation cascades** — When two Bash calls go out in the same response and the first one fails, the harness cancels the second mid-flight. If a step has any chance of failing (path probe, network call), do it alone first; only parallelize after you've confirmed the inputs are good.

14. **Don't ask "should I post this?" after Jason said "go ahead"** — Jason's standing preference is execute, then report. Confirm captions only when he explicitly asks for a draft first.

15. **`schedulingType` vs `mode` — don't confuse them** — `schedulingType` is always `"automatic"`. `mode` is the share strategy (`shareNow`, `addToQueue`, `shareNext`, `customScheduled`). Putting `customScheduled` in `schedulingType` will return `Value "customScheduled" does not exist in "SchedulingType" enum.` and `Field "mode" of required type "ShareMode!" was not provided.` Always set both fields.

16. **"Video URL validation timed out after 10 seconds" is transient** — Buffer occasionally times out probing a freshly-uploaded URL even when the URL is fully reachable. Re-verify with `curl -sI <url>` to confirm `content-length` is still set, then retry the *same* JSON payload (the Python prep step doesn't need to rerun — `/tmp/buffer_*.json` are still on disk). One retry is almost always enough.
