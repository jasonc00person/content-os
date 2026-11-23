#!/usr/bin/env bash
# transcribe-url.sh — get a transcript for any video URL
# usage: transcribe-url.sh <url> [output_dir]
#
# YouTube: pull the captions (no audio, no whisper, ~2s).
# Everything else (or YouTube with no captions / a 429): ONE yt-dlp call grabs the
# native audio stream + metadata (no mp3 re-encode), then fw_fast.py (beside this
# script) transcribes it on the fastest lane this machine has: NVIDIA GPU > Apple GPU > CPU.
# Benchmarked 2026-11-22 on a 20-min reel, M5 Ultra: 157s -> ~13s end to end.

set -euo pipefail

URL="${1:?usage: transcribe-url.sh <url> [output_dir]}"
OUTPUT_DIR="${2:-transcripts/url}"
MODEL="${WHISPER_MODEL:-small.en}"
# optional: YTDLP_COOKIES_BROWSER=chrome (or firefox, safari, ...) for login-walled URLs.
COOKIES_BROWSER="${YTDLP_COOKIES_BROWSER:-}"

# system python for the caption parser. Windows installs ship `python`, not `python3`.
PY=python3; python3 -c '' >/dev/null 2>&1 || { PY=python; python -c '' >/dev/null 2>&1 || { echo "[error] python not found; run ./setup.sh from the project root" >&2; exit 1; }; }

HERE="$(cd "$(dirname "$0")" && pwd)"
WORK="$(mktemp -d "${TMPDIR:-/tmp}/transcribe-url-XXXXXX")"
OUT_FILE=""
# drop the temp dir, and an output file we reserved but never filled (failed run)
trap 'rm -rf "$WORK"; [ -n "$OUT_FILE" ] && [ ! -s "$OUT_FILE" ] && rm -f "$OUT_FILE"; true' EXIT
START=$SECONDS

is_youtube=0
case "$URL" in *youtube.com*|*youtu.be*) is_youtube=1 ;; esac

YTDLP_BASE=(--no-playlist --quiet --no-warnings)
[ -n "$COOKIES_BROWSER" ] && YTDLP_BASE+=(--cookies-from-browser "$COOKIES_BROWSER")
META_ARGS=(
  --print-to-file "%(title)s" "$WORK/title.txt"
  --print-to-file "%(uploader)s" "$WORK/uploader.txt"
  --print-to-file "%(webpage_url)s" "$WORK/url.txt"
  --print-to-file "%(duration)s" "$WORK/duration.txt"
  --print-to-file "%(upload_date)s" "$WORK/upload_date.txt"
)

echo "[fetch] $URL" >&2
VTT_FILE=""
if [ "$is_youtube" = 1 ]; then
  yt-dlp "${YTDLP_BASE[@]}" "${META_ARGS[@]}" --skip-download \
    --write-subs --write-auto-sub --sub-lang en --sub-format vtt -o "$WORK/sub.%(ext)s" "$URL" >&2 \
    || echo "[warn] caption pull failed (rate limit?); falling back to audio + whisper" >&2
  VTT_FILE="$(find "$WORK" -maxdepth 1 -name 'sub*.vtt' | head -n1)"
fi

if [ -z "$VTT_FILE" ]; then
  rm -f "$WORK"/*.txt   # --print-to-file appends; start the metadata clean
  # native audio stream, no -x/--audio-format: whisper decodes m4a/webm/opus directly
  yt-dlp "${YTDLP_BASE[@]}" "${META_ARGS[@]}" -f "ba/b" -N 4 \
    -o "$WORK/audio.%(ext)s" "$URL" >&2
  AUDIO="$(find "$WORK" -maxdepth 1 -name 'audio.*' ! -name '*.part' | head -n1)"
  [ -n "$AUDIO" ] || { echo "[error] audio download failed" >&2; exit 1; }
fi

TITLE="$(cat "$WORK/title.txt" 2>/dev/null || echo untitled)"
UPLOADER="$(cat "$WORK/uploader.txt" 2>/dev/null || echo unknown)"
DURATION="$(cat "$WORK/duration.txt" 2>/dev/null || echo NA)"
UPLOAD_DATE="$(cat "$WORK/upload_date.txt" 2>/dev/null || echo "")"
CANONICAL_URL="$(cat "$WORK/url.txt" 2>/dev/null || echo "$URL")"

SLUG="$(printf '%s' "$TITLE" | tr '[:upper:]' '[:lower:]' | tr -c 'a-z0-9' '-' \
  | sed -E 's/-+/-/g; s/^-//; s/-$//' | cut -c1-60)"
[ -z "$SLUG" ] && SLUG="transcript"
TODAY="$(date +%Y-%m-%d)"
mkdir -p "$OUTPUT_DIR"
OUTPUT_DIR="$(cd "$OUTPUT_DIR" && pwd)"
[ -w "$OUTPUT_DIR" ] || { echo "[error] can't write to $OUTPUT_DIR" >&2; exit 1; }
# reserve the filename atomically (noclobber): parallel runs from the same uploader
# used to race to one name and silently overwrite each other
set -C
OUT_FILE="$OUTPUT_DIR/${SLUG}_${TODAY}.md"; n=2
until { : > "$OUT_FILE"; } 2>/dev/null; do OUT_FILE="$OUTPUT_DIR/${SLUG}_${TODAY}_${n}.md"; n=$((n + 1)); done
set +C

# ---- fast path: YouTube captions ----
if [ -n "$VTT_FILE" ]; then
  "$PY" - "$VTT_FILE" "$OUT_FILE" "$TITLE" "$UPLOADER" "$CANONICAL_URL" "$DURATION" "$UPLOAD_DATE" <<'PY'
import re, sys

vtt_path, out_file, title, uploader, url, duration, upload_date = sys.argv[1:]
raw = open(vtt_path, encoding="utf-8").read()

ts_re = re.compile(r'(?:(\d+):)?(\d+):(\d+(?:\.\d+)?)\s+-->')
cues = []
for block in re.split(r'\n\s*\n', raw):
    lines = [l for l in block.splitlines() if l.strip()]
    ts_line = next((l for l in lines if ts_re.search(l)), None)
    if not ts_line:
        continue
    m = ts_re.search(ts_line)
    start = int(m.group(1) or 0) * 3600 + int(m.group(2)) * 60 + float(m.group(3))
    body = [l for l in lines if l != ts_line and not l.startswith(('WEBVTT', 'Kind:', 'Language:'))]
    # rolling auto-captions: the line carrying word timestamps is the new text
    active = next((l for l in body if re.search(r'<\d+:\d+:[\d.]+>', l) or '<c>' in l), None)
    if active is None and body:
        active = ' '.join(body)
    clean = re.sub(r'<[^>]+>', '', active or '').strip()
    if clean and (not cues or cues[-1][1] != clean):
        cues.append((start, clean))

def fmt_date(d):
    return f"{d[:4]}-{d[4:6]}-{d[6:8]}" if len(d) == 8 and d.isdigit() else "unknown"
def fmt_dur(d):
    try:
        d = float(d); return f"{int(d // 60)}:{int(d % 60):02d}"
    except ValueError:
        return "unknown"

plain = " ".join(t for _, t in cues) or "(no captions)"
timed = "\n".join(f"`[{int(s//60):02d}:{int(s%60):02d}]` {t}" for s, t in cues) or "(no captions)"
open(out_file, "w", encoding="utf-8").write(f"""# {title}

- **Source:** {url}
- **Uploader:** {uploader}
- **Uploaded:** {fmt_date(upload_date)}
- **Duration:** {fmt_dur(duration)}
- **Method:** YouTube captions (no transcription needed)

## Transcript

{plain}

## Timestamped

{timed}
""")
PY
  echo "[captions] wrote $OUT_FILE in $((SECONDS - START))s" >&2
  echo "$OUT_FILE"
  exit 0
fi

# ---- fallback: faster-whisper on the downloaded audio ----
# Persistent venv shared by every transcribing skill: built once, reused every run.
VENV="${CONTENT_OS_WHISPER_VENV:-$HOME/.cache/content-os/whisper-venv}"
PYBIN="$VENV/bin/python"
[ -e "$PYBIN" ] || PYBIN="$VENV/Scripts/python.exe"   # Windows venv layout
# sentinel written only after a successful install, so a half-built venv self-heals
if [ ! -e "$VENV/.deps-ok" ]; then
  echo "[transcribe] first-run: building faster-whisper venv at $VENV" >&2
  rm -rf "$VENV"
  uv venv "$VENV" --python 3.11 >&2
  PYBIN="$VENV/bin/python"; [ -e "$PYBIN" ] || PYBIN="$VENV/Scripts/python.exe"
  uv pip install --python "$PYBIN" faster-whisper onnxruntime >&2
  touch "$VENV/.deps-ok"
fi

HF_HUB_DISABLE_TELEMETRY=1 HF_HUB_DISABLE_PROGRESS_BARS=1 \
"$PYBIN" - "$HERE" "$AUDIO" "$OUT_FILE" "$TITLE" "$UPLOADER" "$CANONICAL_URL" "$DURATION" "$UPLOAD_DATE" "$MODEL" <<'PY'
import sys
sys.path.insert(0, sys.argv[1]); sys.dont_write_bytecode = True  # no __pycache__ beside the scripts
import fw_fast  # picks the fastest lane on this machine: NVIDIA GPU > Apple GPU > CPU

audio, out_file, title, uploader, url, duration, upload_date, model_name = sys.argv[2:]
segs, info, device = fw_fast.transcribe(audio, model_name)
segments = [(s["start"], s["text"]) for s in segs]
plain = " ".join(t for _, t in segments) or "(no speech detected)"
timed = "\n".join(f"`[{int(s//60):02d}:{int(s%60):02d}]` {t}" for s, t in segments) or "(no speech detected)"

d = upload_date
upload_date = f"{d[:4]}-{d[4:6]}-{d[6:8]}" if len(d) == 8 and d.isdigit() else "unknown"
try:
    secs = float(duration)
except ValueError:
    secs = info["duration"]  # IG and others often omit duration in metadata
dur_str = f"{int(secs // 60)}:{int(secs % 60):02d}"

open(out_file, "w", encoding="utf-8").write(f"""# {title}

- **Source:** {url}
- **Uploader:** {uploader}
- **Uploaded:** {upload_date}
- **Duration:** {dur_str}
- **Detected language:** {info['language']} (p={info['language_probability']:.2f})
- **Model:** {model_name} ({device})

## Transcript

{plain}

## Timestamped

{timed}
""")
PY

echo "[transcribe] wrote $OUT_FILE in $((SECONDS - START))s" >&2
echo "$OUT_FILE"
