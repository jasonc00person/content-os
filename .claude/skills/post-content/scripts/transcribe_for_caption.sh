#!/usr/bin/env bash
# Transcribe one provided video with faster-whisper for post captions.
# Usage: transcribe_for_caption.sh <local-video-path-or-direct-url> [output.txt]

set -euo pipefail

VIDEO="${1:?usage: transcribe_for_caption.sh <local-video-path-or-direct-url> [output.txt]}"
OUT="${2:-/tmp/post-content-transcript.txt}"
WORK="$(mktemp -d /tmp/post-content-transcribe.XXXXXX)"
INPUT="$VIDEO"

cleanup() {
  rm -rf "$WORK"
}
trap cleanup EXIT

case "$VIDEO" in
  http://*|https://*)
    INPUT="$WORK/video.mp4"
    curl -L --fail --silent --show-error "$VIDEO" -o "$INPUT"
    ;;
esac

if [ ! -f "$INPUT" ]; then
  echo "video not found: $INPUT" >&2
  exit 1
fi

export UV_PROJECT_ENVIRONMENT="${UV_PROJECT_ENVIRONMENT:-$HOME/.cache/video-editor-venv}"

uv run --quiet \
  --python 3.11 \
  --with "faster-whisper" \
  --with "onnxruntime" \
  python - "$INPUT" "$OUT" <<'PY'
import sys
from pathlib import Path
from faster_whisper import WhisperModel

video_path = sys.argv[1]
out_path = Path(sys.argv[2])

model = WhisperModel("large-v3", device="auto", compute_type="int8")
segments, info = model.transcribe(video_path, vad_filter=True, language="en")
text = " ".join(segment.text.strip() for segment in segments if segment.text.strip())

out_path.parent.mkdir(parents=True, exist_ok=True)
out_path.write_text(text.strip() + "\n")
print(str(out_path))
PY
