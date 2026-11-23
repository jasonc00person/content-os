---
name: transcribe-url
description: "Transcribe any video URL (YouTube, Instagram reel, TikTok, X, anything yt-dlp handles) to a markdown transcript, locally and free. YouTube pulls captions in ~2s; everything else downloads the audio and runs faster-whisper on the fastest hardware the machine has (~15s for a 20-min reel on Apple Silicon). Triggers: transcribe this link, transcribe this url, transcribe this reel, summarize this reel, what's this reel saying, what does this video say, pull transcript from, get the transcript of this video, transcribe-url."
---

# Transcribe URL

1. **Dedupe:** `grep -rl "<video id>" transcripts/url/ transcripts/local/`. A hit means read that file; don't re-run.
2. **Run** from the repo root, synchronously (it's fast):
   ```bash
   bash .claude/skills/transcribe-url/scripts/transcribe-url.sh "<url>"
   ```
   It prints the path it wrote: `transcripts/url/<title-slug>_<YYYY-MM-DD>.md` (`_2`, `_3` when the name is taken; never overwrites). Optional arg 2 = output dir.
3. **Read the file** and give the user what they asked for: the transcript if short, a summary if long or asked for. Mention the saved path.

## Knobs (env vars, all optional)

- `WHISPER_MODEL=large-v3`: better names, accents, music beds. About 2.5x slower (25s vs 10s per 20 min on an Apple GPU) and a 3 GB one-time download. Default `small.en`; `small` for non-English.
- `YTDLP_COOKIES_BROWSER=chrome`: login-walled posts only.
- `WHISPER_DEVICE=cpu|mps|cuda`: override the auto pick. Left alone it takes the fastest lane the machine has (NVIDIA GPU, then Apple GPU, then CPU) and drops a lane on any failure. AMD and Intel graphics have no lane; they run on the CPU.
- `WHISPER_VERBATIM=1`: keep every filler word ("like", "you know"). The fast mode drops about a third of them; this is about 3x slower. Only when the exact wording matters.

## Gotchas

- Whisper invents words on music-only or no-speech clips. If it reads as nonsense, say so instead of passing it on.
- Expect Whisper misspellings of names and slang (`milliner` = millionaire). Fix them in a summary; flag them when quoting.
- The first Whisper run on a new machine builds `~/.cache/content-os/whisper-venv` and downloads the model (~700 MB, a few minutes). Every run after is instant.

## Handoff

Scripts from a transcript go to `scriptwriter`. Many accounts at once is `ig-competitor-research`. Files already on disk: `voice-corpus-builder/scripts/transcribe-file.sh`.
