# transcribe-url — setup

Pulls a transcript from any public video URL and saves it as a markdown file with metadata, plain transcript, and timestamped segments. Works with YouTube, Instagram Reels, TikTok, X/Twitter, Vimeo, Facebook, LinkedIn, and anything else yt-dlp handles. Trigger it with phrases like "transcribe this link \<url\>", "transcribe this reel", "what does this video say", "pull transcript from \<url\>", or "get the transcript of this video".

## Install

Drop this folder into a skills directory:
- `<project>/.claude/skills/transcribe-url/` — for one project, or
- `~/.claude/skills/transcribe-url/` — to use it everywhere.

## Prerequisites

**1. System tools:** `yt-dlp`, `uv`, `python`, `ffmpeg` (macOS / Linux / Windows via Git Bash). `./setup.sh` at the repo root installs them and `./check-setup.sh` reports what is missing. On macOS, for example:

```
brew install yt-dlp uv python3 ffmpeg
```

- `yt-dlp` — downloads video metadata and audio.
- `uv` — builds the Python venv on first run (whisper fallback path only).
- `python` — used inline for caption parsing (YouTube fast path); the script probes `python3` then `python`, so the Windows install name works too. Whisper runs on a uv-managed Python 3.11 venv, not system python.
- `ffmpeg` — used by yt-dlp for some sites' downloads. The script keeps the native audio stream (no mp3 re-encode), so most runs never touch it.

**First-run note (whisper fallback only).** YouTube URLs with auto-generated captions skip whisper entirely and finish in about 2 seconds. For everything else, the script downloads the audio stream and transcribes it with faster-whisper's batched pipeline on the fastest hardware it finds (NVIDIA GPU, then Apple Silicon GPU, then CPU; AMD and Intel graphics use the CPU; an NVIDIA machine downloads its GPU libraries once, about 1.2 GB): about 15 seconds for a 20-minute reel on Apple Silicon, under a minute on most CPUs. The first time that path runs, it builds a Python venv at `~/.cache/content-os/whisper-venv` — expect roughly 700 MB of one-time downloads (packages + the `small.en` model weights) and a few minutes to complete. Subsequent runs reuse the venv and finish without any install step. If the first build gets interrupted, the script detects the half-built venv via a `.deps-ok` sentinel file and rebuilds cleanly on the next run.

## Output

Writes `transcripts/url/<title-slug>_<YYYY-MM-DD>.md`. The output directory is the second argument to the script and defaults to `transcripts/url/` relative to your working directory (run from the repo root, or pass an absolute path); the script prints the absolute path of the file it wrote, and Claude will display it after the run completes. Pulling the same title twice on one day writes `..._2.md`, `..._3.md` instead of overwriting.

Each file contains video metadata (source URL, uploader, upload date, duration), a full plain-text transcript block, and a timestamped version with `[MM:SS]` markers. YouTube caption files also note the method used; whisper-transcribed files include the detected language and model name.

The default whisper model is `small.en`. For better accuracy on names, heavy accents or music-heavy audio, set `WHISPER_MODEL=large-v3` (about 2.5x slower, 3 GB one-time download). `WHISPER_DEVICE=cpu` forces the CPU if the GPU path ever misbehaves.
