---
name: yt-download
description: "Downloads any video URL (YouTube, Instagram, TikTok, anything yt-dlp supports) as a Premiere-compatible MP4: H.264 video + AAC audio, always. Prefers native H.264 streams so most pulls need no re-encode, and re-encodes with ffmpeg whenever the source is AV1/VP9/Opus (the codecs Premiere rejects). Triggers: download this video, download this youtube video, grab this video, save this video, pull this video, get me this clip, yt-download, download for premiere."
---

# yt-download — Premiere-safe video downloads

Every video downloaded for editing goes through this script. Never call bare `yt-dlp` for a download that will be dragged into Premiere: YouTube's default "best" stream is AV1 or VP9, which Premiere imports as unsupported.

## Run It

```bash
bash .claude/skills/yt-download/scripts/yt-download.sh "<url>" [output_dir] [max_height]
```

- `output_dir` defaults to `~/Downloads`. Pass a `video-editor` job folder when the clip is b-roll for a cut.
- `max_height` defaults to `1080` and caps the video's SHORT side, so it means the same thing for both orientations: landscape lands at 1920x1080, a vertical Short/reel at 1080x1920. Never pass `1920` to "fix" a vertical. YouTube only serves H.264 up to 1080p; asking for 4K (`2160`) downloads VP9/AV1 and triggers a full re-encode, so only pass it when 4K is explicitly requested.
- The script prints the absolute path of the finished file. Report that path and the resolution/duration back.

## What it does

1. `yt-dlp` with a format selector that prefers `avc1` video + `mp4a` audio, falling back to best-available so the download never fails on codec choice. The size cap is `-S "res:<max_height>"` (yt-dlp's `res` = the smaller dimension), not a `[height<=N]` filter. Above 1080 the `avc1` preference is dropped, since it would otherwise win and hand back 1080p.
2. `ffprobe` gate: if the merged file isn't `h264` + `aac`, `ffmpeg` re-encodes it (libx264, crf 18, yuv420p, AAC 192k, faststart) in place.
3. Output is always `<title>.mp4`, Premiere-ready.

## Gotchas

- The `[ok]`/`[fix]` line on stderr tells you whether a re-encode happened. Re-encodes run at roughly 5-10x realtime on this machine; a 20-minute video takes a few minutes. Say so up front for long sources.
- Always ffprobe the result and report the real resolution. A vertical that comes back at 480x854 means the cap regressed to a height filter (hit 2026-09-17).
- Playlists are ignored (`--no-playlist`); one URL = one file.
- Instagram/TikTok sources are already H.264 almost always, so they pass the gate untouched.
- Need a transcript instead of the file? That's `transcribe-url`, not this skill.
