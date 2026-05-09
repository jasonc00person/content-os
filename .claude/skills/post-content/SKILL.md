---
name: post-content
description: "Find a video in Notion (Ready To Post), download it from Frame.io/Drive via Chrome, transcribe + caption, post or schedule across Instagram/TikTok/YouTube via Buffer API, verify it actually published, and auto-retry once on async platform failures. Triggers: post this, post [keyword], schedule this, publish reel, post to instagram, post to all platforms, queue this video, transcribe and post, check failed posts."
---

# Post Content — Multi-Platform Publisher

Resolve a target video from Notion → download from Frame.io/Drive → upload to Buffer → verify it actually went live → auto-retry once on platform errors.

## How to Trigger
- **"post this"** — pick the Ready To Post row in Notion (1 row → just post; 2+ → ask which)
- **"post [keyword]"** — search Notion for a row matching the keyword, prefer Ready To Post status
- **"schedule [keyword] for [time]"** — same lookup, scheduled mode
- **"post [/abs/path/to.mp4]"** — legacy: skip Notion lookup, post the local file directly
- **"transcribe and post [keyword]"** — full lookup → download → transcribe → caption → post
- **"check failed posts"** — Step 0 only: scan Buffer for errored posts in the last 14 days

## Prerequisites
- Buffer API key in `.env` as `BUFFER_API_KEY`
- Notion MCP connected (`mcp__notion__*`)
- Chrome MCP available (`mcp__claude-in-chrome__*`) for Frame.io/Drive downloads
- `ffprobe` (ships with FFmpeg)
- `uv` for transcription (auto-installs `faster-whisper` on first run)

## Notion Content DB Schema (verified 2026-05-06)

**Database ID:** `<the user's Notion content database ID — configure in .env as NOTION_CONTENT_DB_ID or check backbone/ for the project's DB ID>`

| Property | Type | Purpose |
|----------|------|---------|
| Title | title | Video name (matched against user keyword) |
| Status | status | Idea, Scripting/Filming, To Edit, Editing, To Review, **Ready To Post**, Posted, Archived |
| Format | select | Short-form, Long-form |
| Type | multi_select | TOF, MOF, BOF, Brainrot, Viral |
| Post Date | date | Publish timestamp |
| Raw Footage | url | Editor input |
| **Edited Video** | url | Editor output (Frame.io / Drive) — **download source for this skill** |
| IG Link | url | Live IG URL after posting (manual fill-in for now) |

*The `Edited Video` field was previously called `Frame Link` — renamed 2026-05-06. If you see `Frame Link` in another skill, it's stale.*

## Buffer Platform Config

**Organization ID:** `<the user's Buffer organization ID — configure in .env as BUFFER_ORG_ID>`

**Channel IDs** (run "refresh channels" to update — IDs are user-specific):
- Instagram: `<configure in .env as BUFFER_CHANNEL_INSTAGRAM>`
- TikTok: `<configure in .env as BUFFER_CHANNEL_TIKTOK>`
- YouTube: `<configure in .env as BUFFER_CHANNEL_YOUTUBE>`

**Refresh channels query** (run after connecting new platforms to discover your org ID and channel IDs):
```bash
export BUFFER_API_KEY=$(grep BUFFER_API_KEY .env | cut -d= -f2) && \
export BUFFER_ORG_ID=$(grep BUFFER_ORG_ID .env | cut -d= -f2) && \
curl -s -X POST https://api.buffer.com \
  -H "Authorization: Bearer $BUFFER_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"query\": \"query { channels(input: { organizationId: \\\"$BUFFER_ORG_ID\\\" }) { id name service type } }\"}" | python3 -m json.tool
```

---

## Execution Steps

### Step 0 — Scan for stale failures (DON'T SKIP)

Before doing any new work, check Buffer for posts in `error` state from the last 14 days. **Instagram and TikTok both fail asynchronously** — `createPost` returns success the moment Buffer accepts the queue, but the actual platform ingestion can fail minutes later. Without this scan, errored posts sit silently and you only find out by checking the IG/TikTok app.

```bash
export BUFFER_API_KEY=$(grep BUFFER_API_KEY .env | cut -d= -f2)
export BUFFER_ORG_ID=$(grep BUFFER_ORG_ID .env | cut -d= -f2)
curl -s -X POST https://api.buffer.com \
  -H "Authorization: Bearer $BUFFER_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"query\": \"query { posts(input: { organizationId: \\\"$BUFFER_ORG_ID\\\", filter: { status: [error] } }, first: 20) { edges { node { id text status dueAt channelService error { message rawError } } } } }\"}" | python3 -m json.tool
```

If errored posts come back from the last ~14 days:
- Surface them with platform, dueAt, and error message (truncate `text` to ~80 chars)
- Offer to retry (see Retry Flow in Step 6)
- Don't auto-retry stale failures (>3 days old) — the Litterbox URL is dead and the source video may need re-pulling from Notion

If the user invoked the skill with **"check failed posts"** as the only request, run this and stop. Otherwise continue.

### Step 1 — Resolve target video from Notion

Find the Notion row corresponding to the video the user wants to post.

**A. Parse the user's message** for a keyword/title (everything meaningful after "post" / "schedule" / "publish"). If the message contains a literal absolute file path that exists on disk (e.g., `/Users/.../foo.mp4`), **skip to Step 3** — treat as legacy direct-post.

**B. Query Notion** with `mcp__notion__API-post-search`:
```json
{
  "query": "<keyword or empty>",
  "filter": {"property": "object", "value": "page"},
  "page_size": 100
}
```

**C. Filter** results to pages where `parent.database_id` matches the user's Notion content database ID (see "Notion Content DB Schema" above).

**D. Apply status priority:**
1. **First pass:** filter to `Status = Ready To Post`. If matches, use these.
2. **Fallback (only if user gave a keyword and Ready To Post returned nothing):** search across all statuses. Surface the broader matches with their statuses so the user knows what's going on.

**E. Selection:**
- **0 matches** → report "no Ready To Post rows found" (or "no matches for `<keyword>` in any status") and stop. Don't guess, don't fall back to local files.
- **1 match** → use it.
- **2+ matches** → list candidates: `Title · Status · Edited Video host (frame.io / drive / etc.)` and ask the user which one. Don't auto-pick.

**F. Extract and hold:**
- `page_id` (for Notion patch in Step 7)
- `Title` (for the YouTube title default and Notion fallback search)
- `Edited Video` URL (for Step 2 download)
- `Format` (Short-form vs Long-form — drives YouTube short vs long handling)

If the matched row has a blank `Edited Video` field, stop and tell the user — the editor hasn't dropped a link yet.

### Step 2 — Download the edited video

The `Edited Video` URL is **dynamic** — branch on host. **Default expectation: public Frame.io share.** Always snapshot `~/Downloads` before triggering the download so we can identify the new file.

```bash
mkdir -p ~/Downloads
ls -1At ~/Downloads > /tmp/dl_before.txt
```

#### A. Frame.io (default — public share or logged-in)

URLs: `https://f.io/<id>`, `https://app.frame.io/presentations/<id>`, `https://frame.io/share/<id>`, `https://frame.io/reviews/...`, or share-redirected `https://next.frame.io/share/<id>/view/<asset-id>`.

**Use element refs from `find` — NEVER click by pixel coordinate.** The Frame.io Download dropdown lists Original first and proxies below; rows are ~25px tall and the menu shifts position based on viewport. Pixel-coordinate clicks land on the Original row constantly. This was confirmed by repeatedly downloading a 700MB Original when targeting the 100MB proxy.

The exact sequence that works:

1. `mcp__claude-in-chrome__tabs_context_mcp` with `createIfEmpty: true` — never reuse stale tab IDs.
2. `mcp__claude-in-chrome__navigate` to the share URL. `https://f.io/<id>` redirects to `https://next.frame.io/share/<id>/view/<asset-id>` — let it.
3. Wait ~6s for the player UI to render (`computer` action `wait`).
4. **Open the Download menu via element ref:**
   ```
   find: query="Download button at top right of page", tabId=<tab>
   computer: action="left_click", ref="<returned ref_id>"
   ```
5. **Pick the proxy via element ref:**
   ```
   find: query="MP4 H264 1080×1920 proxy menu item", tabId=<tab>
   computer: action="left_click", ref="<returned ref_id>"
   ```
   The match returns a menuitem like `"Proxy h264_1080_best"` — that's the right one (~100MB, full-HD H.264, ingests cleanly on IG/TikTok/YouTube). The Original is 500MB–2GB ProRes/high-bitrate and risks Litterbox 504s + Buffer rejection.
6. Close the tab — download continues in the background.

**Edge case: bare `https://next.frame.io/share/<id>/` (no `/view/<asset-id>`)** — that's the asset-list page, not a player. The Download Asset button there only offers Original. Click into the asset thumbnail first to land on `/view/<asset-id>`, where the proxy menu appears.

**Don't fall back to pixel coordinates if `find` doesn't match.** Re-read the page (`read_page` filter=interactive) to confirm the menu is open, then re-run `find` with a slightly different query. Pixel clicks waste tokens on huge re-encodes.

#### B. Google Drive (anyone-with-link)

URL: `https://drive.google.com/file/d/<FILE_ID>/view`.

```bash
FILE_ID="<extracted from URL>"
curl -sL -o "$HOME/Downloads/notion-edit.mp4" "https://drive.google.com/uc?export=download&id=$FILE_ID"
```

For files >100MB, Drive injects a virus-scan confirmation. If `file ~/Downloads/notion-edit.mp4` reports HTML instead of MP4, fall back to the Chrome flow (open the URL, click Download).

#### C. Google Drive (private — your account only)

Use the Google Drive MCP since the user's account is connected:
1. `mcp__claude_ai_Google_Drive__search_files` to confirm the file ID
2. `mcp__claude_ai_Google_Drive__download_file_content` returns base64 for binary files. Decode and write to `~/Downloads/<safe-title>.mp4`.

#### D. Direct media URL (.mp4 / .mov)

```bash
curl -sL -o "$HOME/Downloads/<safe-title>.mp4" "<URL>"
```

#### Verify the download landed

Poll for a new file in `~/Downloads`, then confirm size and format:

```bash
for i in $(seq 1 60); do
  ls -1At ~/Downloads > /tmp/dl_after.txt
  NEW=$(comm -23 <(sort /tmp/dl_after.txt) <(sort /tmp/dl_before.txt) | head -5)
  CANDIDATE=$(echo "$NEW" | grep -iE '\.(mp4|mov|m4v)$' | head -1)
  if [ -n "$CANDIDATE" ]; then
    SIZE_NOW=$(stat -f %z "$HOME/Downloads/$CANDIDATE" 2>/dev/null || echo 0)
    sleep 3
    SIZE_LATER=$(stat -f %z "$HOME/Downloads/$CANDIDATE" 2>/dev/null || echo 0)
    if [ "$SIZE_NOW" -gt 0 ] && [ "$SIZE_NOW" = "$SIZE_LATER" ]; then
      VIDEO="$HOME/Downloads/$CANDIDATE"
      echo "Downloaded: $VIDEO ($(du -h "$VIDEO" | cut -f1))"
      break
    fi
  fi
  sleep 2
done
[ -z "$VIDEO" ] && { echo "Download did not complete within 2 minutes"; exit 1; }
file "$VIDEO" | grep -qi 'iso media\|quicktime' || { echo "Downloaded file is not video: $(file "$VIDEO")"; exit 1; }
```

If the download fails (no new file, 0 bytes, wrong format) report and stop. Don't proceed to upload a broken file.

### Step 3 — Pre-flight video validation (DON'T SKIP for IG-bound posts)

Run `ffprobe` against the downloaded file. Catches format issues that Instagram and YouTube Shorts will reject async. Skip ONLY if posting exclusively to TikTok.

**Set `PLATFORMS` env var before running** so YouTube Shorts gets its vertical check (otherwise we burn 4 min on Litterbox + Buffer round-trip before YT rejects).

```bash
export PLATFORMS="${PLATFORMS:-instagram,tiktok,youtube}"  # whatever you'll post to
ffprobe -v error -show_streams -show_format -of json "$VIDEO" > /tmp/video_probe.json 2>&1
python3 - <<'PY'
import json, os, sys
with open('/tmp/video_probe.json') as f:
    p = json.load(f)
platforms = os.environ.get('PLATFORMS', 'instagram,tiktok,youtube').split(',')
v = next((s for s in p['streams'] if s['codec_type'] == 'video'), None)
a = next((s for s in p['streams'] if s['codec_type'] == 'audio'), None)
errors = []
if not v:
    errors.append('No video stream')
else:
    if v.get('codec_name') not in ('h264', 'hevc'):
        errors.append(f"Codec is {v.get('codec_name')} — IG prefers h264 (hevc sometimes works)")
    w, h = int(v.get('width', 0)), int(v.get('height', 0))
    ratio = w / h if h > 0 else 0
    if 'instagram' in platforms and not (0.5 <= ratio <= 1.91):
        errors.append(f"Aspect ratio {w}x{h} ({ratio:.3f}) outside IG accepted range 0.5–1.91")
    if 'youtube' in platforms and ratio > 1.0:
        errors.append(f"Aspect ratio {w}x{h} ({ratio:.3f}) is landscape — YouTube Shorts requires vertical (≤1.0, ideally 9:16 = 0.5625). Re-export 9:16 OR drop 'youtube' from PLATFORMS to post as a regular long-form video.")
    fps_str = v.get('avg_frame_rate', '0/1')
    try:
        n, d = (int(x) for x in fps_str.split('/'))
        fps = n / d if d else 0
    except Exception:
        fps = 0
    if not (23 <= fps <= 60):
        errors.append(f"Frame rate {fps:.1f}fps outside IG 23–60 range")
if not a:
    errors.append('No audio stream — IG silently rejects video-only Reels')
dur = float(p['format'].get('duration', 0))
if dur < 3:
    errors.append(f"Duration {dur:.1f}s under 3s minimum")
if dur > 900:
    errors.append(f"Duration {dur:.1f}s over 15min Reels maximum")
if errors:
    print('VALIDATION FAILED:')
    for e in errors:
        print('  -', e)
    sys.exit(1)
print(f'OK: {v["codec_name"]} {v["width"]}x{v["height"]} @ {fps:.0f}fps, {dur:.0f}s, audio={a["codec_name"]}, platforms={",".join(platforms)}')
PY
```

If validation fails, stop and report. Either re-export the video, drop the offending platform from `PLATFORMS`, or have the user explicitly confirm an override.

### Step 4 — Transcribe video (if no caption provided)

Use `faster-whisper` via `uv` — same setup the `rough-cut` skill uses. **Run in the background** alongside the upload in Step 5 — they take 1-3 min on a typical clip and there's no reason to wait sequentially.

```bash
export UV_PROJECT_ENVIRONMENT="$HOME/.cache/video-editor-venv"
uv run --quiet --python 3.11 --with "faster-whisper" --with "onnxruntime" python - "$VIDEO" <<'PY'
import sys
from faster_whisper import WhisperModel
model = WhisperModel("large-v3", device="auto", compute_type="int8")
segments, info = model.transcribe(sys.argv[1], vad_filter=True, language="en")
print(" ".join(seg.text.strip() for seg in segments))
PY
```

Run with `run_in_background: true` and poll for the output. Don't use stock `openai-whisper` — not installed, pip is brittle.

Then generate a caption from the transcript:
- Read `backbone/icp.md` + `backbone/messaging.md` for current positioning, ICP, voice patterns. Layer in `voice-dna.md` for sentence-level rhythm.
- Caption sounds like the creator — casual, direct, no-BS (read `voice-dna.md` if present in the project for sentence-level rhythm)
- **CTA rule (drives EVERYTHING about the caption shape):** scan the transcript for an explicit comment/DM CTA the creator actually said on camera (e.g. "comment SYSTEM", "DM me CLAUDE", "drop AGREE in the comments").
  - **CTA present in transcript →** line 1 of the caption MUST be that exact CTA, matched to what they said ("Comment SYSTEM and I'll send you the framework 👇"). Closing line repeats the keyword with 👇. This is the conversion play — don't soften it.
  - **NO CTA in transcript (hot take, contrarian opinion, mindset post, raw thought) →** keep the caption chill and laid back. No forced/manufactured DM keyword. Lead with the hook or a punchy restatement of the take. Optional engagement bait at the end ("agree?", "thoughts?", just an emoji) — but only if it feels natural. Don't fake a funnel CTA on content that wasn't built for one.
- Structure (when there's a CTA): CTA → hook → bullets/breakdown (use `→` not numbered lists) → closing CTA repeat with 👇
- Structure (when there's no CTA): hook → take/breakdown → optional soft engagement line
- Default: just post it. Only ask for caption confirmation if user explicitly said "draft a caption first."

### Step 5 — Upload Video to Litterbox

Buffer needs a publicly accessible URL. **Run in background, parallel with Step 4 (transcription).**

```bash
curl -s -F "reqtype=fileupload" -F "time=72h" -F "fileToUpload=@$VIDEO" https://litterbox.catbox.moe/resources/internals/api.php
```
Returns a direct URL like `https://litter.catbox.moe/abc123.mp4`.

Verify after upload:
```bash
curl -sI https://litter.catbox.moe/abc123.mp4 | head -5
```
Must show `content-length` > 0. If 0, retry the upload.

**Host selection (learned from testing):**
- **Litterbox** — up to 1GB, 72hr expiry. **DEFAULT.**
- **tmpfiles.org** — under 100MB only, ~60min expiry. Don't bother.
- **catbox.moe (permanent)** — returns `content-length: 0`. **NEVER USE** — Buffer rejects it.

### Step 6 — Post + Verify + Auto-Retry

Posts to each platform AND (for `shareNow`) verifies the post actually went live. Buffer's `createPost` returns success the moment a post is queued, but Instagram and TikTok ingestion happens async — they fail silently from Buffer's perspective. The script below covers post → poll → auto-retry once on error.

**Why curl from Python:** Buffer's API blocks Python's default `urllib`/`requests` user agent via Cloudflare. We `subprocess.run(['curl', ...])` from Python to get proper JSON handling without shell escaping issues AND a Cloudflare-safe transport.

```bash
export BUFFER_API_KEY=$(grep BUFFER_API_KEY .env | cut -d= -f2)
export BUFFER_CHANNEL_INSTAGRAM=$(grep BUFFER_CHANNEL_INSTAGRAM .env | cut -d= -f2)
export BUFFER_CHANNEL_TIKTOK=$(grep BUFFER_CHANNEL_TIKTOK .env | cut -d= -f2)
export BUFFER_CHANNEL_YOUTUBE=$(grep BUFFER_CHANNEL_YOUTUBE .env | cut -d= -f2)
export VIDEO_URL="https://litter.catbox.moe/abc123.mp4"
export VIDEO_PATH="$VIDEO"   # for re-upload on retry if Litterbox URL expired
export YT_TITLE="<curiosity-driven title — default to Notion Title>"
export MODE="shareNow"        # shareNow | addToQueue | shareNext | customScheduled
# export DUE_AT="2026-05-07T17:00:00.000Z"  # only set when MODE=customScheduled
# export PLATFORMS="instagram,tiktok,youtube"  # default = all three
export CAPTION_FILE=/tmp/buffer_caption.txt
cat > "$CAPTION_FILE" <<'CAP'
PASTE THE CAPTION HERE — multiline, emojis, quotes all OK
CAP

python3 - <<'PY'
import json, subprocess, time, os, sys

API_KEY    = os.environ['BUFFER_API_KEY']
VIDEO_URL  = os.environ['VIDEO_URL']
VIDEO_PATH = os.environ.get('VIDEO_PATH', '')
YT_TITLE   = os.environ.get('YT_TITLE', '')
MODE       = os.environ['MODE']
DUE_AT     = os.environ.get('DUE_AT')
CAPTION    = open(os.environ['CAPTION_FILE']).read().strip()
PLATFORMS  = os.environ.get('PLATFORMS', 'instagram,tiktok,youtube').split(',')

CHANNELS = {
    # Channel IDs are user-specific — populate from .env or the Buffer Config section above
    'instagram': {'id': os.environ['BUFFER_CHANNEL_INSTAGRAM'],
                  'meta': {'instagram': {'type': 'reel', 'shouldShareToFeed': True}}},
    'tiktok':    {'id': os.environ['BUFFER_CHANNEL_TIKTOK'],
                  'meta': None},
    'youtube':   {'id': os.environ['BUFFER_CHANNEL_YOUTUBE'],
                  'meta': {'youtube': {'title': YT_TITLE, 'privacy': 'public',
                                       'madeForKids': False, 'notifySubscribers': True,
                                       'categoryId': '22'}}},
}

CREATE = ('mutation ($input: CreatePostInput!) { createPost(input: $input) { '
          '... on PostActionSuccess { post { id status dueAt } } '
          '... on MutationError { message } } }')
EDIT   = ('mutation ($input: EditPostInput!) { editPost(input: $input) { '
          '... on PostActionSuccess { post { id status dueAt } } '
          '... on MutationError { message } } }')
POLL   = '{ post(input: { id: "%s" }) { id status channelService error { message rawError } } }'

def gql(query, variables=None):
    payload = {'query': query}
    if variables: payload['variables'] = variables
    r = subprocess.run(
        ['curl', '-sS', '-X', 'POST', 'https://api.buffer.com',
         '-H', f'Authorization: Bearer {API_KEY}',
         '-H', 'Content-Type: application/json',
         '-d', json.dumps(payload)],
        capture_output=True, text=True, timeout=60,
    )
    try:
        return json.loads(r.stdout)
    except json.JSONDecodeError:
        return {'errors': [{'message': f'non-JSON response: {r.stdout[:300]}'}]}

def reupload(path):
    r = subprocess.run(
        ['curl', '-sS', '-F', 'reqtype=fileupload', '-F', 'time=72h',
         '-F', f'fileToUpload=@{path}',
         'https://litterbox.catbox.moe/resources/internals/api.php'],
        capture_output=True, text=True, timeout=300,
    )
    return r.stdout.strip()

def url_is_live(url):
    r = subprocess.run(['curl', '-sI', url], capture_output=True, text=True, timeout=15)
    for line in r.stdout.splitlines():
        if line.lower().startswith('content-length:'):
            try: return int(line.split(':')[1].strip()) > 0
            except: return False
    return False

def build_input(channel, mode, video_url):
    inp = {
        'text': CAPTION,
        'channelId': channel['id'],
        'schedulingType': 'automatic',
        'mode': mode,
        'assets': {'videos': [{'url': video_url}]},
    }
    if channel['meta']: inp['metadata'] = channel['meta']
    if mode == 'customScheduled' and DUE_AT: inp['dueAt'] = DUE_AT
    return inp

def poll_until_done(pid, timeout_s=240, interval=20):
    start = time.time()
    last = None
    while time.time() - start < timeout_s:
        d = gql(POLL % pid)
        last = (d.get('data') or {}).get('post')
        if not last: return None
        if last['status'] in ('sent', 'error'): return last
        time.sleep(interval)
    return last

def post_one(name, create_attempts=3):
    channel = CHANNELS[name]
    cp, res = {}, {}
    for attempt in range(1, create_attempts + 1):
        res = gql(CREATE, {'input': build_input(channel, MODE, VIDEO_URL)})
        cp = (res.get('data') or {}).get('createPost') or {}
        msg = cp.get('message', '')
        if msg and 'timed out' in msg.lower():
            time.sleep(5)
            continue
        break
    if 'message' in cp:
        return {'platform': name, 'phase': 'create', 'status': 'error', 'error': cp['message'], 'create_attempts': attempt}
    if 'errors' in res:
        return {'platform': name, 'phase': 'create', 'status': 'error', 'error': res['errors'], 'create_attempts': attempt}
    pid = (cp.get('post') or {}).get('id')
    due = (cp.get('post') or {}).get('dueAt')
    out = {'platform': name, 'post_id': pid, 'due_at': due, 'phase': 'create', 'status': 'queued', 'create_attempts': attempt}
    if MODE != 'shareNow':
        return out
    final = poll_until_done(pid)
    if not final:
        out['status'] = 'unknown'
        return out
    out['status'] = final['status']
    out['error'] = final.get('error')
    if final['status'] == 'error':
        url = VIDEO_URL
        if not url_is_live(url):
            if not VIDEO_PATH or not os.path.exists(VIDEO_PATH):
                out['retry'] = {'status': 'skipped', 'reason': 'URL expired and VIDEO_PATH missing'}
                return out
            url = reupload(VIDEO_PATH)
            if not url.startswith('http'):
                out['retry'] = {'status': 'skipped', 'reason': f're-upload failed: {url[:200]}'}
                return out
        edit_input = build_input(channel, 'shareNow', url)
        edit_input['id'] = pid
        edit_input.pop('channelId', None)
        res = gql(EDIT, {'input': edit_input})
        ep = (res.get('data') or {}).get('editPost') or {}
        if 'message' in ep:
            out['retry'] = {'status': 'error', 'phase': 'edit', 'error': ep['message']}
            return out
        retry_final = poll_until_done(pid)
        out['retry'] = {'status': retry_final['status'] if retry_final else 'unknown',
                        'error': retry_final.get('error') if retry_final else None,
                        'video_url_used': url}
    return out

results = [post_one(p) for p in PLATFORMS]
print(json.dumps(results, indent=2))
PY
```

**Read the JSON output to determine final state per platform:**
- `status: queued` and `MODE != shareNow` — scheduled successfully; verification deferred to Step 0 next session
- `status: sent` — published live
- `status: error` with no `retry` key — `MODE != shareNow`, can't auto-retry inline
- `status: error` with `retry.status: sent` — failed, retried, succeeded
- `status: error` with `retry.status: error` — failed twice; surface to the user and stop (don't mark Posted in Notion)

#### Platform-Specific Requirements

| Platform | Required Metadata | Notes |
|----------|------------------|-------|
| Instagram | `type: reel`, `shouldShareToFeed: true` | Min 3s, 9:16 ideal, h264+AAC, must have audio |
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

Every post requires **both** `schedulingType` and `mode`. They are NOT interchangeable — `schedulingType` is always `"automatic"` for these flows; `mode` carries the actual share strategy.

| Use case | User says | `schedulingType` | `mode` | `dueAt`? |
|----------|-----------|------------------|--------|----------|
| Post now | "post this" (default) | `automatic` | `shareNow` | — |
| Add to queue | "queue this" | `automatic` | `addToQueue` | — |
| Next in queue | "post this next" | `automatic` | `shareNext` | — |
| Specific time | "schedule for April 20 at 3pm" / "tomorrow at noon" | `automatic` | `customScheduled` | Yes — ISO 8601 UTC |

For `customScheduled`, convert to UTC ISO 8601: `2026-04-20T19:00:00.000Z`. Confirm the user's timezone from CLAUDE.md or ask if unknown. For vague "tomorrow" with no time, default to **noon local time** (convert to UTC accordingly).

### Step 7 — Update Notion Pipeline

We already have `page_id` from Step 1 — no second search needed. Patch the row to **Posted** with `Post Date` derived from Buffer's `dueAt`.

**Patch only if Step 6's final state was `sent` (shareNow) or `queued` (other modes).** If the post errored after retry, leave the row alone so the failure stays visible for triage.

```json
{
  "page_id": "<from Step 1>",
  "properties": {
    "Status": { "status": { "name": "Posted" } },
    "Post Date": { "date": { "start": "<ISO 8601 with local timezone offset>" } }
  }
}
```

**Post Date derivation:**
- Use `post.dueAt` from Step 6's response (ISO 8601 UTC)
- Convert to local timezone offset for readability (e.g. `2026-04-30T15:00:00-05:00`)
- Notion's date property accepts the full ISO string and renders date + time in the UI
- If `dueAt` is missing for any reason, fall back to `date +"%Y-%m-%dT%H:%M:%S%z"` and reformat the offset with a colon

If the Notion update fails, **don't fail the whole flow** — the post already went out. Report and continue.

*(Legacy direct-post mode where the user pasted a file path: skip Step 7 entirely. There's no Notion row to update.)*

### Step 8 — Confirm

Report results for each platform plus the Notion update:
```
Posted "[Notion Title]"
  Instagram Reel — sent ✅
  TikTok — error → retry sent ✅
  YouTube Short — queued (next slot: [time])

Notion: page → Posted (2026-04-30 12:00 CT)

Caption: [first 2 lines...]
Source video: [filename] (downloaded from frame.io)
```

If any platform fails twice (initial + retry), surface both errors and skip the Notion update.

---

## Caption Writing Guidelines

When generating captions from transcripts:

1. **CTA FIRST** — keyword CTAs are ALWAYS line 1. Shows before "...more" in feed.
2. **Hook line** — 1-line hook after CTA that makes people read on
3. **Body** — key points. Arrows (→) or line breaks, never numbered lists
4. **Closing CTA** — repeat the keyword with 👇
5. **Voice** — casual, direct, emojis sparingly. Sounds like a text from a friend
6. **Length** — IG/TikTok max 2,200 chars; LinkedIn max 3,000 chars
7. **YouTube** — separate `title` field (max 100 chars). Curiosity-driven, short.

---

## Common Commands

**"post this"** — Find Ready To Post in Notion, download from Edited Video link, post to all platforms with verify+retry
**"post [keyword]"** — Notion search for keyword (Ready To Post first), then full flow
**"transcribe and post [keyword]"** — Same as above + auto-generate caption from transcript
**"schedule [keyword] for tomorrow at 10am"** — Same lookup, customScheduled mode
**"post [keyword] to IG only"** — Same lookup, restrict to Instagram
**"post /Users/.../foo.mp4"** — Legacy: skip Notion lookup, post local file directly (no Notion update)
**"check failed posts"** — Step 0 only; scan Buffer for errored posts in last 14 days

---

## Lessons Learned (from testing)

### What broke and how to avoid it

1. **Shell escaping hell** — NEVER inline captions with quotes/emojis into a curl/GraphQL string. Captions contain double quotes, single quotes, emojis, newlines — shell escaping WILL fail. Always use `subprocess.run(['curl', ..., '-d', json.dumps(payload)])` from Python (Step 6) or write JSON to a temp file and `curl -d @file.json`.

2. **Python urllib/requests gets blocked by Cloudflare** — Buffer's API blocks default UA. Always shell out to `curl` for the actual API calls, even from inside Python.

3. **tmpfiles.org has a ~100MB limit** — Real videos are 50-400MB. Use Litterbox as default.

4. **catbox.moe (permanent) returns content-length: 0** — Buffer rejects URLs with zero content-length. Never use catbox.moe permanent, only Litterbox temporary.

5. **YouTube requires `categoryId`** — `youtube` metadata needs a `categoryId` string or validation error. Default `"22"`.

6. **Instagram requires `shouldShareToFeed: true`** — Without this boolean the API returns a validation error.

7. **Instagram reels must be at least 3 seconds** — Buffer rejects shorter.

8. **Load API key with grep, not `source`** — Use `export BUFFER_API_KEY=$(grep BUFFER_API_KEY /path/.env | cut -d= -f2)`. `source .env` doesn't always propagate to subshells.

9. **Always verify the upload URL** — After Litterbox upload, `curl -sI <url> | head -3` to confirm `content-length` > 0 before passing to Buffer.

10. **Curly quotes in filenames break paths** — Chat clients render `'` as `'` (U+2019) but the file uses straight `'` (U+0027). Always `ls` first; if it fails, `ls` the parent dir, grep for distinctive keywords, and copy the real filename into a `$VIDEO` shell variable. Don't retype filenames.

11. **`openai-whisper` is not installed; use `faster-whisper` via `uv`** — The `rough-cut` skill's `uv run --with "faster-whisper" --with "onnxruntime"` pattern auto-installs into a cached venv. Reuse it.

12. **Run upload + transcription in parallel as background tasks** — Both take 30s-3min on 100-400MB clips. Kick them off with `run_in_background: true`. Sequential = 2x wall-clock for no reason.

13. **Parallel tool-call cancellation cascades** — When two Bash calls go out together and the first fails, the harness cancels the second mid-flight. Risky steps (path probe, network call) should run alone first; parallelize only after confirming inputs.

14. **Don't ask "should I post this?" after the user said go** — the standing preference is execute, then report. Confirm captions only when explicitly asked for a draft first.

15. **`schedulingType` vs `mode` — don't confuse them** — `schedulingType` is always `"automatic"`. `mode` is the share strategy (`shareNow`, `addToQueue`, `shareNext`, `customScheduled`). Putting `customScheduled` in `schedulingType` returns `Value "customScheduled" does not exist in "SchedulingType" enum.` and `Field "mode" of required type "ShareMode!" was not provided.` Always set both.

16. **"Video URL validation timed out after 10 seconds" is transient** — Buffer occasionally times out probing a freshly-uploaded URL even when reachable. Re-verify with `curl -sI <url>` and retry the *same* JSON payload. One retry usually wins.

17. **Instagram fails async after Buffer accepts** — Buffer's `createPost` returns success the moment a post is queued, but Instagram's media container creation happens later (during scheduled publish or shortly after `shareNow`). When IG rejects the media — even with vague errors like `Failed to create media container for instagram: Unable to get media container status from Instagram: ERROR: ERROR` — Buffer flips the post status to `error`. **Without polling, the failure is invisible.** Confirmed case: 4/30/2026 noon CT scheduled IG Reel failed silently while TikTok+YouTube versions of the same payload published fine. Step 6's poll + auto-retry catches this; Step 0's stale-failure scan catches anything that slipped through.

18. **TikTok "stuck in processing" is also async** — Same failure class as #17. Error message: "Uh-oh. It looks like this post is stuck processing. Retrying the post should work." Confirmed case: 4/29/2026. Auto-retry handles it cleanly.

19. **`editPost` doesn't accept `channelId`** — When retrying via EditPostInput, drop `channelId`. Pass `id` instead. Re-set `mode: shareNow` and `schedulingType: automatic` even though the original post has them — EditPostInput requires both as non-null.

20. **Litterbox URLs expire in 72h** — For inline `shareNow` retries (within ~5 min), URL is still alive. For Step 0 stale failures (>3 days), URL is dead and source must be re-pulled from Notion + re-uploaded. Step 6's retry function does `url_is_live()` first and re-uploads from `VIDEO_PATH` if needed; for Step 0 retries, ask the user before re-pulling old videos.

21. **Notion DB schema drifts — re-fetch when in doubt** — `Frame Link` was renamed to `Edited Video` on 2026-05-06; statuses like `Ready To Post` get added; `Type` went from select to multi_select. Before relying on a property name in this skill, run `mcp__notion__API-retrieve-a-database` with the user's content DB ID (see "Notion Content DB Schema" above) if you suspect drift.

22. **Chrome MCP downloads land in ~/Downloads, not a tool-returned path** — When clicking a Download button via Chrome MCP, the file flows through Chrome's normal download pipeline. There's no MCP response with the path. Snapshot `~/Downloads` before, poll for the new file after, and confirm size is stable across 3s before treating download as complete.

23. **Frame.io download menu — always pick the top "Proxy" option, never "Original"** — Originals are typically 500MB–2GB ProRes/high-bitrate. Top proxy (`MP4 H264 1920x1080`) is full-HD H.264 ~100MB, already encoded for streaming, and ingests cleanly on every platform. Confirmed: 113MB H.264 proxy uploaded + ingested in <90s; Original would have been ~600MB and risked Litterbox/Buffer rejection.

24. **YouTube Shorts requires vertical (≤1.0 aspect ratio)** — IG and TikTok happily accept 16:9 widescreen, but YouTube Shorts hard-rejects with `"Video must be vertical (portrait orientation)"` during the `create` mutation. Don't discover this after upload — gate it in Step 3 pre-flight when `youtube` is in `PLATFORMS`. Either re-export 9:16 or drop YouTube from the platform list and post as long-form instead.

25. **Buffer's "URL validation timed out" can fire on `create`, not just on the post-create poll** — Lesson #16 noted the timeout exists; what wasn't obvious was that it returns as a `MutationError` from `createPost` itself (no `post_id` ever issued) on top of the post-poll path. The original Step 6 retry only handled the post-poll case. Step 6's `post_one` now retries `create` up to 3× with 5s backoff specifically when the message contains "timed out" — confirmed wins on attempt 2 every time so far. Don't widen the retry trigger; other create errors are usually real (validation, aspect, codec).

26. **Caption shape is dictated by the transcript, not by template** — If the on-camera audio has an explicit comment/DM CTA ("comment SYSTEM", "DM me CLAUDE"), the caption MUST mirror that exact CTA on line 1 — that's the conversion play. If the audio has no CTA (hot take, contrarian opinion, raw thought), forcing a manufactured DM keyword feels off and reads inauthentic. For those, keep the caption chill: lead with the hook, optional soft engagement bait at the end ("agree?", emoji), no fake funnel.
