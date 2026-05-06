#!/usr/bin/env bash
# transcribe-url.sh — download a video from any URL and transcribe with faster-whisper
# usage: transcribe-url.sh <url> [output_dir]
#
# downloads audio-only via yt-dlp, transcribes with faster-whisper small.en,
# writes a markdown transcript with metadata + timestamped lines.

set -euo pipefail

URL="${1:?usage: transcribe-url.sh <url> [output_dir]}"
OUTPUT_DIR="${2:-transcripts/url}"
MODEL="${WHISPER_MODEL:-small.en}"

WORK="$(mktemp -d /tmp/transcribe-url-XXXXXX)"
trap 'rm -rf "$WORK"' EXIT

echo "[download] $URL" >&2

# pull metadata + audio in one shot. -x extracts audio, mp3 is most compatible.
# --print-to-file gives us the metadata fields without parsing yt-dlp output.
yt-dlp \
  -x --audio-format mp3 \
  --no-playlist \
  --quiet --no-warnings --progress \
  -o "$WORK/audio.%(ext)s" \
  --print-to-file "%(title)s" "$WORK/title.txt" \
  --print-to-file "%(uploader)s" "$WORK/uploader.txt" \
  --print-to-file "%(webpage_url)s" "$WORK/url.txt" \
  --print-to-file "%(duration)s" "$WORK/duration.txt" \
  --print-to-file "%(upload_date)s" "$WORK/upload_date.txt" \
  "$URL" >&2

AUDIO="$WORK/audio.mp3"
[ -f "$AUDIO" ] || { echo "[error] audio download failed" >&2; exit 1; }

TITLE="$(cat "$WORK/title.txt" 2>/dev/null || echo untitled)"
UPLOADER="$(cat "$WORK/uploader.txt" 2>/dev/null || echo unknown)"
DURATION="$(cat "$WORK/duration.txt" 2>/dev/null || echo 0)"
UPLOAD_DATE="$(cat "$WORK/upload_date.txt" 2>/dev/null || echo "")"
CANONICAL_URL="$(cat "$WORK/url.txt" 2>/dev/null || echo "$URL")"

# build slug from title for the filename
SLUG="$(printf '%s' "$TITLE" \
  | tr '[:upper:]' '[:lower:]' \
  | tr -c 'a-z0-9' '-' \
  | sed -E 's/-+/-/g; s/^-//; s/-$//' \
  | cut -c1-60)"
[ -z "$SLUG" ] && SLUG="transcript"

TODAY="$(date +%Y-%m-%d)"
mkdir -p "$OUTPUT_DIR"
OUT_FILE="$OUTPUT_DIR/${SLUG}_${TODAY}.md"

# faster-whisper auto-installs into a cached venv (first run ~30s, then instant)
export UV_PROJECT_ENVIRONMENT="${UV_PROJECT_ENVIRONMENT:-$HOME/.cache/transcribe-url-venv}"

echo "[transcribe] model=$MODEL audio=$AUDIO" >&2

uv run --quiet \
  --python 3.11 \
  --with "faster-whisper" \
  --with "onnxruntime" \
  python - "$AUDIO" "$OUT_FILE" "$TITLE" "$UPLOADER" "$CANONICAL_URL" "$DURATION" "$UPLOAD_DATE" "$MODEL" <<'PY'
import sys
from faster_whisper import WhisperModel

audio, out_file, title, uploader, url, duration, upload_date, model_name = sys.argv[1:]

model = WhisperModel(model_name, device="auto", compute_type="int8")
segments, info = model.transcribe(
    audio,
    vad_filter=True,
    vad_parameters=dict(min_silence_duration_ms=500),
)
# segments is a generator — iterate once, keep what we need
plain_lines = []
timed_lines = []
for seg in segments:
    text = seg.text.strip()
    if not text:
        continue
    plain_lines.append(text)
    mm = int(seg.start // 60)
    ss = int(seg.start % 60)
    timed_lines.append(f"`[{mm:02d}:{ss:02d}]` {text}")

plain = " ".join(plain_lines).strip() or "(no speech detected)"

# format upload_date YYYYMMDD -> YYYY-MM-DD
if upload_date and len(upload_date) == 8 and upload_date.isdigit():
    upload_date = f"{upload_date[:4]}-{upload_date[4:6]}-{upload_date[6:8]}"
elif not upload_date or upload_date == "NA":
    upload_date = "unknown"

try:
    d = float(duration)
    dur_str = f"{int(d // 60)}:{int(d % 60):02d}"
except (ValueError, TypeError):
    dur_str = "unknown"

md = f"""# {title}

- **Source:** {url}
- **Uploader:** {uploader}
- **Uploaded:** {upload_date}
- **Duration:** {dur_str}
- **Detected language:** {info.language} (p={info.language_probability:.2f})
- **Model:** {model_name}

## Transcript

{plain}

## Timestamped

{chr(10).join(timed_lines) if timed_lines else "(no speech detected)"}
"""

with open(out_file, "w") as f:
    f.write(md)

print(f"[transcribe] wrote {out_file}", file=sys.stderr)
PY

# print the final path on stdout so callers can capture it
echo "$OUT_FILE"
