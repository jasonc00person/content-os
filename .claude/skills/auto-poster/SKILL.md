---
name: auto-poster
description: "Post or schedule a provided video directly through Zernio. Input is a local video path or public video URL. If no caption is provided, transcribe the video with faster-whisper (tiny.en by default) and generate a caption from that transcript. No Notion lookup or browser download. Triggers: post this video, post /path/to/video.mp4, schedule this video, queue this video, publish reel, post to instagram, post to zernio."
---

# Auto Poster

Take the video Jason gives you and post it through Zernio.

This skill does one job with one optional prep step:

`provided video -> optional faster-whisper caption -> Zernio`

Zernio posting should feel like:

```js
await fetch("https://zernio.com/api/v1/posts", {
  method: "POST",
  headers: { Authorization: `Bearer ${ZERNIO_API_KEY}` },
  body: JSON.stringify({
    content: "Caption goes here",
    platforms: [{ platform: "instagram", accountId: "..." }],
    mediaItems: [{ type: "video", url: "https://example.com/demo.mp4" }],
    publishNow: true
  })
});
```

Zernio's public examples sometimes show the shorthand shape `text`, `platforms`, and `mediaUrls`. The helper script uses the documented OpenAPI shape: `content`, `mediaItems`, and platform targets with account IDs.

## What This Skill Does Not Do

- Does not search Notion.
- Does not download from Frame.io or Google Drive.
- Does not update pipeline status inside the script. The script never touches Notion. After every successful run except `draft`, the session (not the script) resolves the video's Notion page (by the job/file, never a shared keyword) and flips it to `Posted` in the same turn. `Post Date` = the day it goes live: today for `shareNow`, the `scheduled_local` date for `customScheduled`, the queue slot's date for `addToQueue`. A scheduled post counts as posted the moment Zernio accepts it; if a later `--status` shows it failed, flip the page back to `Ready`.
- Does not run the full content production chain.

If the user wants those steps, use the relevant upstream skill first, then come back here with the final video file.

## Inputs

Required:

- Local video path, e.g. `/Users/jason/.../final.mp4`
- Or a public direct video URL, e.g. `https://.../video.mp4`

Optional:

- Caption text or caption file.
- If no caption is provided, generate one from a faster-whisper transcript.
- Platforms: default = every account with an ID in `.env`; name platforms (`--platforms instagram,youtube`) to narrow.
- Mode: default `shareNow`.
- Schedule time for `customScheduled`.
- YouTube title. Default is the filename or caption first line.
- YouTube visibility (`--yt-visibility public|private|unlisted`). Omitted = Zernio's default, public. A long-form upload goes up `private` so Jason can finish it in Studio. Zernio's presigned upload caps files at 5 GB, so re-encode a bigger export before posting (4K at 40 Mbps is plenty for YouTube).

## Prerequisites

`.env` (in the skill directory) must contain:

The key list below is the template (`.env.example` in the skill folder is a copyable version) — fill in the real values (README.md documents each key). The script defaults to the skill-directory `.env` regardless of cwd; pass `--env-file` only to override. Values in the `.env` win over any `ZERNIO_*` already exported in the shell.

```bash
ZERNIO_API_KEY=
# only the ones you have connected; every key present is a default posting target
ZERNIO_ACCOUNT_INSTAGRAM=
ZERNIO_ACCOUNT_TIKTOK=
ZERNIO_ACCOUNT_YOUTUBE=
ZERNIO_ACCOUNT_LINKEDIN=
ZERNIO_ACCOUNT_FACEBOOK=
ZERNIO_ACCOUNT_THREADS=
```

Aliases also work (same six platforms):

```bash
ZERNIO_ACCOUNT_ID_INSTAGRAM=
ZERNIO_ACCOUNT_ID_TIKTOK=
ZERNIO_ACCOUNT_ID_YOUTUBE=
```

Optional:

```bash
ZERNIO_API_URL=https://zernio.com/api/v1
ZERNIO_PROFILE_ID=
ZERNIO_QUEUE_ID=
ZERNIO_TIMEZONE=America/New_York
```

`ZERNIO_PROFILE_ID` is required only for `addToQueue`. `ZERNIO_TIMEZONE` (an IANA zone, `America/New_York` is just an example) is required only for `customScheduled`; `--timezone` overrides it per call, and `shareNow` ignores it.

System tools used by the helpers: `python3`, `ffmpeg`, `curl`, `uv` (builds the shared faster-whisper venv on first use). Nothing else to install: no compiler toolchain.

To fill (or refresh) the `ZERNIO_ACCOUNT_*` ids, run the one hardened command for it, from the repo root, once `ZERNIO_API_KEY` is in the `.env`:

```bash
python3 .claude/skills/auto-poster/scripts/post_to_zernio.py --list-accounts
```

It calls `GET /accounts` with the key from the skill `.env`, prints one paste-ready `ZERNIO_ACCOUNT_<PLATFORM>=<id>    # platform: display name` line per connected account, never prints the key, and exits 0. Paste the lines you want as default targets into `.claude/skills/auto-poster/.env`. Don't improvise a curl for this.

## Fast Path

Use the helper script. Command paths below are written from the repo root (Bash cwd resets there each turn; on Windows use `python` in place of `python3`):

```bash
python3 .claude/skills/auto-poster/scripts/post_to_zernio.py \
  "/absolute/path/to/video.mp4" \
  --caption-file "$CAPTION_FILE" \
  --mode shareNow
```

Where `$CAPTION_FILE` is a path you created in this session — not a hardcoded shared path. See "Temp files" below. No `--platforms` means every account in `.env`.

For a public video URL:

```bash
python3 .claude/skills/auto-poster/scripts/post_to_zernio.py \
  "https://example.com/video.mp4" \
  --caption "Caption goes here" \
  --platforms instagram,tiktok \
  --mode addToQueue
```

If Jason did not provide a caption, run the transcriber and capture the path it prints to stdout:

```bash
TRANSCRIPT_FILE=$(.claude/skills/auto-poster/scripts/transcribe_for_caption.sh "/absolute/path/to/video.mp4")
```

Then read `$TRANSCRIPT_FILE`, write a caption to a path you control, and pass that to `--caption-file`.

For a scheduled post:

```bash
python3 .claude/skills/auto-poster/scripts/post_to_zernio.py \
  "/absolute/path/to/video.mp4" \
  --caption-file "$CAPTION_FILE" \
  --mode customScheduled \
  --due-at "2026-05-18T12:00:00" \
  --timezone "America/New_York"
```

`--timezone` is any IANA zone (the value above is an example); omit it when `ZERNIO_TIMEZONE` is set in the `.env`. The script refuses to schedule with neither.

Before anything uploads, the script also refuses a `--due-at` that resolves to the past (Zernio publishes a past time IMMEDIATELY instead of rejecting it) or more than 6 days out (Zernio deletes an upload after 7 days if its post hasn't published, so the video would be gone at publish time; for a date further out, run it again closer to the day). The output's `scheduled_local` (e.g. `Fri 2026-09-25 11:30 CDT`) is the time it will actually go out: read that back to Jason, not the time you typed.

For a draft:

```bash
python3 .claude/skills/auto-poster/scripts/post_to_zernio.py \
  "/absolute/path/to/video.mp4" \
  --caption-file "$CAPTION_FILE" \
  --mode draft
```

To see the exact payload with zero network calls (no upload, no verify, no post), add `--dry-run`; the local path stands in for the media URL.

## Transcription (faster-whisper)

`scripts/transcribe_for_caption.sh` uses the one transcription engine every skill in this repo shares: faster-whisper in the persistent venv at `~/.cache/content-os/whisper-venv` (built by `uv` on first use or by `./setup.sh`; `CONTENT_OS_WHISPER_VENV` overrides the location). Model defaults to `tiny.en` (fast, plenty for a caption); override with `AUTO_POSTER_WHISPER_MODEL=base.en` (or `small.en`) for more accuracy at a few seconds more per run.

- The script ffmpeg-extracts 16 kHz mono audio first so whisper processes a few MB instead of hundreds.
- First run on a machine builds the venv (about 200 MB) and downloads the model; every run after that reuses the cache and a 90-second reel transcribes in a few seconds (on the GPU when the machine has one).
- The venv is sentinel-gated on `.deps-ok`, so an interrupted first build rebuilds cleanly next run.

## Temp files (security)

Do not write transcripts, captions, or downloaded media to predictable shared paths like `/tmp/auto-poster-caption.txt`. Anyone with write access to `/tmp` on the host can pre-seed those files and inject content into a post.

Instead:

- Let `transcribe_for_caption.sh` choose its own output path (it creates the transcript file with `mktemp`, mode 600, owned by you, and prints that path on stdout) and read whatever path it prints.
- When you need to write a caption, use a session-scoped path you create — e.g. the agent's outputs directory or `"$(mktemp -t auto-poster-caption.XXXXXXXX)"`.
- Before reading any file you didn't just create, verify it's owned by the current user (`stat -f %Su "$f"` on macOS, `stat -c '%U' "$f"` on Linux) and was modified after the session started. If either check fails, refuse and ask the user.

## Execution Rules

1. If the user did not provide a video path or URL, ask for the video.
2. If Jason provided a caption, use it.
3. If Jason did not provide a caption, run `transcribe_for_caption.sh`, generate a caption from the transcript, and save it to a session-scoped file you created.
4. If the video is a local file, run `post_to_zernio.py` with that path. The script uploads it through Zernio's presigned media upload flow.
5. If the video is already a public URL, pass it directly as the media URL.
6. Default to every account in `.env` unless Jason names platforms.
7. For YouTube, set `--yt-title` if Jason provides one. Otherwise use the filename or first caption line.
8. **YouTube is short-form only by default.** YouTube has no Shorts flag: it classifies a Short purely from the file (vertical or square, AND 3 min or under; a phone clip's rotation flag counts, so a landscape-stored clip that plays vertical is a Short). Anything else uploads as a LONG-FORM video on the channel. The helper ffprobes the file and drops YouTube (with a warning) unless it will land as a Short. Never pass `--yt-long-form` on your own; only when Jason explicitly says the upload IS the long-form video. If he wants a horizontal clip on Shorts, pad it to 9:16 with black bars first (see gotchas).
8. Report Zernio post IDs, statuses, platform URLs, and errors. The script marks nothing outside Zernio; the session then flips the video's Notion page to `Posted` + `Post Date`, scheduled posts included (see "What This Skill Does Not Do").
9. **Exit codes.** `0` = created, no platform failed. `2` = the post EXISTS but a platform failed (or a schedule landed at a different time than asked): report the failure, never re-run the same command; retry only the failed platform(s) with `--platforms` (TikTok at capacity: `--platforms tiktok --tiktok-draft`). `1` = nothing was created (a gate refused, or the API errored before create).
10. **Did it go out?** `--status <post_id>` fetches one post (exit 2 + the reason if any platform failed); `--status` alone lists everything scheduled or in flight plus any failures from the last 14 days. Use it whenever Jason asks whether a scheduled post went out, and after any scheduled time has passed in a session.

## Caption Rules

Generate the caption from the transcript, not from a generic template.

- If the transcript includes a real comment/DM CTA Jason said on camera, put that CTA on line 1 and repeat it at the end.
- If there is no spoken CTA, do not manufacture one. Use the strongest hook/take from the transcript and keep it casual.
- Captions carry no link by default (document, don't manufacture). The one exception: if Jason's spoken CTA names the community (exactly as named in `backbone/offer.md`), mirror that CTA in the caption. Never add a link or offer line the video didn't say.
- Keep it direct, conversational, and short enough for IG/TikTok.
- Use line breaks. Avoid numbered lists unless the video itself is clearly a numbered list.
- Threads only accepts captions of 500 characters or less. If the caption runs longer, write a trimmed under-500 version and pass it as `--threads-caption` in the same call (it goes to Threads as `customContent`; one post, one record). The script refuses a long caption on Threads without it, and refuses anything over Instagram/TikTok's 2,200 or LinkedIn's 3,000.

## Supported Modes

- `shareNow`: sends `publishNow: true`.
- `addToQueue`: sends `queuedFromProfile`, using `ZERNIO_PROFILE_ID`.
- `customScheduled`: sends `scheduledFor` and `timezone`.
- `draft`: sends `isDraft: true`.

For `customScheduled`, `--due-at` is required, and so is a timezone (`--timezone` or `ZERNIO_TIMEZONE` in the `.env`).

## Platform Metadata

The script sends:

- Caption as top-level `content`.
- Video as `mediaItems: [{ type: "video", url }]`.
- Platforms as `{ platform, accountId }` targets from `.env`.
- YouTube title as top-level `title` when posting to YouTube.

## Notes

- Zernio API base URL is `https://zernio.com/api/v1`.
- Zernio uses bearer auth with `ZERNIO_API_KEY`.
- Local files are uploaded via `POST /v1/media/presign`, then `PUT` to the returned upload URL, then posted with the returned `publicUrl`.
- Zernio also has a shorthand examples style using `text`, platform names, and `mediaUrls`; use the helper unless Jason explicitly asks for the raw shorthand payload.

## Known platform gotchas

Hard-won from real runs. Check these before a post, not after it hangs.

- **A horizontal clip on YouTube is a long-form upload, not a Short** (hit 2026-09-08: a 16:9 teaser went up as a real video on the channel and had to be deleted). YouTube decides by the file alone: vertical + 3 min or under = Short. The helper gates this automatically. To put a horizontal clip on Shorts, pad it onto a 9:16 canvas (plain black bars, shot untouched; Jason's call 2026-09-08, no blur), then post that file:
  ```bash
  ffmpeg -i in.mp4 -vf "scale=1080:-2,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:black" -c:v libx264 -crf 20 -maxrate 12M -bufsize 24M -c:a aac -b:a 160k -movflags +faststart out-9x16.mp4
  ```
- **Swapping or pulling a live post.** `DELETE /posts/{id}` only works on drafts/scheduled. For a published post use `POST /posts/{id}/unpublish` with `{"platform":"youtube"}` (also threads/facebook/linkedin/twitter; NOT Instagram or TikTok, delete those in-app). YouTube deletion is permanent; the Zernio record flips to cancelled. Then post the replacement as a new post. Retitling a live YouTube upload without a repost goes through `POST /posts/{id}/update-metadata`. Verified 2026-09-08.
- **TikTok "direct posting is at capacity"** = Zernio's shared TikTok app hit TikTok's rolling 24h cap on distinct direct-posting accounts. Not the video, not the account. Retry in a few hours, or pass `--tiktok-draft` to deliver via Creator Inbox (`tiktokSettings.draft: true`; it is NOT in the profile Drafts folder: it arrives under Inbox tab → System notifications as a "video is ready to share" notification, tap it to open the editor and post; TikTok allows 5 pending drafts per 24h). Direct-post failed 3× in one afternoon on 2026-09-08, so after two failures go straight to the draft. Zernio does NOT retry a capacity failure, so a scheduled post that hits it just loses TikTok. **Permanent fix: reconnect TikTok.** Accounts connected before Zernio moved TikTok to the Business app stay on the capped developer lane until reconnected; Business-lane accounts never hit the cap. Jason's was reconnected 2026-09-24 (`metadata.laneMigratedAt`), so this should not recur for him. The dashboard has no reconnect button (New Connection refuses a second TikTok on the profile, and Disconnect risks the history): `GET /v1/connect/tiktok?profileId=<profile>` returns an `authUrl`; open it, stay on the same @handle, accept every permission. Same-account reconnect keeps the account id and all history, so `.env` needs no change.

- **Threads captions over 500 characters fail** ("Param text must be at most 500 characters long", 3 posts in May-June went out without Threads). The script now refuses them; pass `--threads-caption` (see Caption Rules).
- **4K or over 300 MB hangs Instagram.** Zernio compresses before TikTok but hands the raw file straight to Instagram's Graph API; a 612 MB 4K export sat at `awaiting-finalize` for 20+ minutes with no error. Meta's API takes Reels up to 300 MB. The video-editor's Reels export (1080x1920, CBR 14, sized under 300 MB) is built for exactly this, so post it as is: a 163 MB one published to Instagram in seconds (2026-10-30). The script refuses Instagram sources over 300 MB or with a short side over 1080 and prints this command: re-encode so the short side is 1080 (works for vertical and horizontal; the old `scale=-2:1080` squashed a vertical to 608x1080), framing untouched, then post the re-encode:
  ```bash
  ffmpeg -i in.mp4 -vf "scale='if(gt(iw,ih),-2,1080)':'if(gt(iw,ih),1080,-2)'" -c:v libx264 -crf 20 -maxrate 12M -bufsize 24M -c:a aac -b:a 160k -movflags +faststart out-1080p.mp4
  ```
- **A stuck Instagram post leaves a live container open.** Never re-post the same video while an earlier record is still stuck: delete the old post record in Zernio first, or it double-posts once the container finalizes.
- **Zernio account IDs go stale after any OAuth reconnect.** The error reads "accounts do not belong to this user". Refresh with `python3 .claude/skills/auto-poster/scripts/post_to_zernio.py --list-accounts` and update the `ZERNIO_ACCOUNT_*` values in the skill `.env` (`.claude/skills/auto-poster/.env` from the repo root; the script reads only that file).

## Resilience (built into the helper)

The helper is hardened against the failure modes that bit us in real runs. You normally don't need to do anything — just know how it behaves:

- **Media reachability check reads the HTTP status code, not a substring of the header dump.** A `Content-Length` like `102040443` contains "404" and used to false-positive the old check. It now retries a few times (uploads can 404 briefly while they propagate) and is a *soft warning* for media we uploaded ourselves (the `PUT` runs with `curl --fail`, so a rejected upload aborts before the post, and Zernio reads the object server-side) — it only hard-fails for a user-supplied URL.
- **A timed-out create never duplicates.** `POST /posts` can succeed server-side even when the client call times out. The helper uses one stable `x-request-id` per logical post and, on any network/timeout error, *reconciles* against `GET /posts` (matching the exact caption, recent posts only) before deciding anything. If the post already landed it reports `source: recovered-after-timeout`; only if nothing is found does it retry, reusing the same request id. So never re-run the script by hand after a timeout — let it reconcile.
- **A re-run never duplicates either.** An interrupted run can still post, and a re-run re-uploads the file under a new media URL, which slips past Zernio's own 24h duplicate check (double-posted 2026-06-29). Before uploading, the script looks for the same caption in the last 24h and refuses if it is already live or queued on any target platform, naming the post id. Failed or cancelled platforms don't count, so retrying just those goes through. To replace a scheduled post, `DELETE /posts/{id}` it first.
- **A partial publish is reported, not hidden.** Zernio answers `207` with the post plus an `error` when some platforms fail inline; the helper reports the post and each platform's `errorMessage` (earlier versions printed `"error": null` for every failure) and exits 2.
- **Create timeout is 240s** (fan-out to all connected platforms takes a while), vs. the old 120s that gave up too early.
- **`source` in the output** tells you whether the post was `created` or `recovered`.

Flags for edge cases:

- `--wait-seconds N` — `shareNow` only: poll the created post by id until every platform reaches a terminal state (published/failed/cancelled), up to N seconds. Good for an accurate final report. Ignored for scheduled/queued/draft posts, which never reach a terminal state.
- `--dry-run`: print the payload and exit with zero network calls (no upload, no verify, no post).
- `--skip-verify` — skip the media reachability check entirely.
- `--max-retries N` — safe create retries (default 1); each is reconcile-guarded so it can't duplicate.
- `--status [POST_ID]`: see Execution Rules step 10.
- `--threads-caption TEXT`: the under-500-character Threads version (Caption Rules).
- `--ig-collaborators a,b`: invite up to 3 Instagram usernames as collaborators on the Reel (a sponsor's handle). The invite goes out at publish and stays pending until they accept; a rejected username is dropped without failing the post (read `droppedCollaborators` on the post).

Regression tests: `python3 .claude/skills/auto-poster/tests/test_post_to_zernio.py` runs every gate and failure path against a local mock Zernio (no real account touched, about 10s). Run it after any change to the script.
