---
name: post-content
description: "Post or schedule a provided video directly through Buffer. Input is a local video path or public video URL. If no caption is provided, transcribe the video with faster-whisper and generate a caption from that transcript. No Notion lookup or browser download. Triggers: post this video, post /path/to/video.mp4, schedule this video, queue this video, publish reel, post to instagram, post to buffer."
---

# Post Content

Take the video Jason gives you and post it through Buffer.

This skill does one job with one optional prep step:

`provided video -> optional faster-whisper caption -> Buffer`

## What This Skill Does Not Do

- Does not search Notion.
- Does not download from Frame.io or Google Drive.
- Does not update pipeline status.
- Does not run the full content production chain.

If the user wants those steps, use the relevant upstream skill first, then come back here with the final video file.

## Inputs

Required:

- Local video path, e.g. `/Users/jason/.../final.mp4`
- Or a public direct video URL, e.g. `https://.../video.mp4`

Optional:

- Caption text or caption file.
- If no caption is provided, generate one from a faster-whisper transcript.
- Platforms: default `instagram,tiktok,youtube`.
- Mode: default `shareNow`.
- Schedule time for `customScheduled`.
- YouTube title. Default is the filename or caption first line.

## Prerequisites

`.env` must contain:

```bash
BUFFER_API_KEY=
BUFFER_CHANNEL_INSTAGRAM=
BUFFER_CHANNEL_TIKTOK=
BUFFER_CHANNEL_YOUTUBE=
```

Optional:

```bash
BUFFER_ORG_ID=
```

## Fast Path

Use the helper script:

```bash
python3 .claude/skills/post-content/scripts/post_to_buffer.py \
  "/absolute/path/to/video.mp4" \
  --caption-file "/tmp/caption.txt" \
  --platforms instagram,tiktok,youtube \
  --mode shareNow
```

For a public video URL:

```bash
python3 .claude/skills/post-content/scripts/post_to_buffer.py \
  "https://example.com/video.mp4" \
  --caption "Caption goes here" \
  --platforms instagram,tiktok \
  --mode addToQueue
```

If Jason did not provide a caption:

```bash
.claude/skills/post-content/scripts/transcribe_for_caption.sh \
  "/absolute/path/to/video.mp4" \
  "/tmp/post-content-transcript.txt"
```

Then write the caption from `/tmp/post-content-transcript.txt` to `/tmp/post-content-caption.txt` and pass it with `--caption-file`.

For a scheduled post:

```bash
python3 .claude/skills/post-content/scripts/post_to_buffer.py \
  "/absolute/path/to/video.mp4" \
  --caption-file "/tmp/caption.txt" \
  --mode customScheduled \
  --due-at "2026-05-18T17:00:00.000Z"
```

Convert local times to UTC ISO before passing `--due-at`. Jason is usually America/Chicago unless the current project context says otherwise.

## Execution Rules

1. If the user did not provide a video path or URL, ask for the video.
2. If Jason provided a caption, use it.
3. If Jason did not provide a caption, run `transcribe_for_caption.sh`, generate a caption from the transcript, and save it to a temp file.
4. If the video is a local file, run `post_to_buffer.py` with that path. The script uploads it to Litterbox first because Buffer requires a public URL.
5. If the video is already a public URL, pass it directly. The transcription helper can temporarily download direct media URLs for faster-whisper.
6. Default to all configured platforms unless Jason names specific platforms.
7. For YouTube, set `--yt-title` if Jason provides one. Otherwise use the filename or first caption line.
8. Report Buffer post IDs, statuses, and errors. Do not mark any outside system as posted.

## Caption Rules

Generate the caption from the transcript, not from a generic template.

- If the transcript includes a real comment/DM CTA Jason said on camera, put that CTA on line 1 and repeat it at the end.
- If there is no spoken CTA, do not manufacture one. Use the strongest hook/take from the transcript and keep it casual.
- Keep it direct, conversational, and short enough for IG/TikTok.
- Use line breaks. Avoid numbered lists unless the video itself is clearly a numbered list.

## Supported Modes

- `shareNow`
- `addToQueue`
- `shareNext`
- `customScheduled`

For `customScheduled`, `--due-at` is required.

## Platform Metadata

The script sends:

- Instagram: Reel, share to feed.
- TikTok: standard video post.
- YouTube: public video, not made for kids, category `22` People & Blogs.

## Notes

- Buffer's GraphQL API is called through `curl` from Python because direct Python HTTP clients can hit Cloudflare issues.
- Local files are uploaded to Litterbox for a temporary public URL. This is intentionally simple and fast.
- If Buffer returns an async platform error later, rerun the same command with the same video and caption.
