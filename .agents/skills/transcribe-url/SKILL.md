---
name: transcribe-url
description: "Download and transcribe any video from a social/web URL using yt-dlp and faster-whisper locally. Outputs a markdown file with metadata plus plain and timestamped transcript. Triggers: transcribe this link, transcribe this url, transcribe this reel, pull transcript from, what does this video say, get the transcript of this video, transcribe-url."
---

# Transcribe URL — yt-dlp + faster-whisper

Pulls audio from any public video URL and transcribes it locally. Zero API cost, runs on the user's local machine. Built for fast research lookups — "what's this competitor reel actually saying?"

## How to Trigger

- **"transcribe this link <url>"** → grab + transcribe + show the transcript
- **"transcribe <url>"** → same
- **"what's this reel saying <url>"** → same, but lead the reply with the gist
- Any social media URL works: YouTube, Instagram Reels/posts, TikTok, X/Twitter, Vimeo, Facebook, LinkedIn, etc.

## The Pipeline (one script, no orchestration)

```bash
bash .Codex/skills/transcribe-url/scripts/transcribe-url.sh "<url>"
```

Optional second arg: output directory (defaults to `transcripts/url/`).

The script picks one of two paths automatically:

**Fast path (YouTube only):** Pulls YouTube's auto-generated captions via `yt-dlp --write-auto-sub --skip-download`. No audio download, no whisper. Finishes in ~2s regardless of video length.

**Fallback (everything else, or YouTube without captions):**
1. Downloads audio only via `yt-dlp -x --audio-format mp3`
2. Transcribes with faster-whisper `small.en` (override with `WHISPER_MODEL=medium.en` env var)
3. Writes `transcripts/url/<slug>_<date>.md`

Returns the output path on stdout.

## Run It

YouTube URLs finish in ~2s — always synchronous. For non-YouTube short reels (<3 min), still synchronous (~10-30s). For long non-YouTube videos (10+ min), run in background.

After it completes:
1. Read the output file
2. Show the user the transcript inline (or summarize if it's long)
3. Mention the saved path in case they want to reference it later

## Output Shape

```markdown
# <video title>

- **Source:** <canonical URL>
- **Uploader:** <handle>
- **Uploaded:** YYYY-MM-DD
- **Duration:** M:SS
- **Detected language:** en (p=0.99)   # whisper path only
- **Model:** small.en                   # whisper path only
- **Method:** YouTube captions ...      # fast path only

## Transcript

<full plain text, one block>

## Timestamped

`[00:00]` first segment
`[00:04]` second segment
...
```

## Model Choice

(Only relevant for the whisper fallback. The YouTube fast path doesn't run whisper.)

- **`small.en`** (default) — ~5-10x realtime on M-series, good enough for most spoken content. Quick research lookups, competitor reels, captioned content.
- **`medium.en`** — better with mumbling, music-heavy backgrounds, accents. Override: `WHISPER_MODEL=medium.en bash .../transcribe-url.sh <url>`
- **`large-v3`** — best quality, slowest. Use only when small/medium got it wrong. The `rough-cut` skill uses this because cuts depend on word-level precision.

First run downloads the model (~250MB for small, ~1.5GB for medium, ~3GB for large) and caches it under `~/.cache/`. Subsequent runs are instant.

## Gotchas

- **YouTube without auto-captions** — extremely rare (YouTube auto-generates for almost everything), but if no `.vtt` is published we fall back to whisper automatically. No action needed.
- **Login-walled content** (private IG, restricted YouTube, TikTok login walls) — yt-dlp will error out. If it fails, try with browser cookies: edit the script to add `--cookies-from-browser chrome`. Don't do this by default — it's slower and unnecessary for public content.
- **Music-heavy or no-speech videos** — Whisper may hallucinate lyrics. If the transcript looks like nonsense, that's why. Note it in the report rather than passing the garbage along.
- **Title is used for the filename slug** — exotic Unicode titles get stripped to `transcript_<date>.md`. That's fine.
- **Don't re-transcribe** — if the same URL was already saved (search `transcripts/url/` first), just read the existing file. Whisper isn't deterministic enough that re-running adds value.
- **Language** — script lets faster-whisper auto-detect language. The `small.en` model is English-only; if the user needs another language, switch to `small` (no `.en`) via the env var.

## Handoff

This skill produces transcripts. It does NOT summarize, pull viral hooks, or write scripts. After transcribing:
- For script ideas → invoke `scriptwriter` with the transcript as raw input
- For competitor analysis at scale → use `research-ig-competitors` instead (handles many accounts at once)
- For raw clips already on disk → use `rough-cut` (different pipeline, word-level precision)
