#!/usr/bin/env bash
# reframe.sh — landscape → 9:16 with face tracking
# usage: reframe.sh <input.mp4> [output.mp4] [--center]
#
# Default output: <input_dir>/<input_stem>__9x16.mp4
# --center: skip face tracking, dumb horizontal center crop

set -euo pipefail

INPUT="${1:?usage: reframe.sh <input.mp4> [output.mp4] [--center]}"
[ -f "$INPUT" ] || { echo "input not found: $INPUT" >&2; exit 1; }
INPUT="$(cd "$(dirname "$INPUT")" && pwd)/$(basename "$INPUT")"
shift

OUTPUT=""
CENTER=0
while [ $# -gt 0 ]; do
  case "$1" in
    --center) CENTER=1; shift ;;
    -*) echo "unknown flag: $1" >&2; exit 1 ;;
    *)
      if [ -z "$OUTPUT" ]; then OUTPUT="$1"; shift
      else echo "unexpected arg: $1" >&2; exit 1
      fi
      ;;
  esac
done

INPUT_DIR="$(dirname "$INPUT")"
INPUT_STEM="$(basename "${INPUT%.*}")"
[ -z "$OUTPUT" ] && OUTPUT="$INPUT_DIR/${INPUT_STEM}__9x16.mp4"

# Probe source dimensions
SRC_W=$(ffprobe -v error -select_streams v:0 -show_entries stream=width -of csv=p=0 "$INPUT")
SRC_H=$(ffprobe -v error -select_streams v:0 -show_entries stream=height -of csv=p=0 "$INPUT")

# Auto-skip if already vertical
if [ "$SRC_H" -ge "$SRC_W" ]; then
  echo "[reframe] source $SRC_W x $SRC_H is already vertical — copying unchanged" >&2
  cp "$INPUT" "$OUTPUT"
  echo "[reframe] wrote $OUTPUT" >&2
  exit 0
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CMD_FILE="/tmp/reframe-$$-$(basename "${INPUT%.*}").txt"
trap 'rm -f "$CMD_FILE"' EXIT

if [ "$CENTER" -eq 1 ]; then
  CROP_H="$SRC_H"
  CROP_W=$(( SRC_H * 9 / 16 ))
  [ "$CROP_W" -gt "$SRC_W" ] && CROP_W="$SRC_W"
  CROP_X=$(( (SRC_W - CROP_W) / 2 ))
  echo "[reframe] center crop $CROP_W x $CROP_H @ x=$CROP_X" >&2
  ffmpeg -hide_banner -loglevel error -y \
    -i "$INPUT" \
    -vf "crop=${CROP_W}:${CROP_H}:${CROP_X}:0,scale=1080:1920" \
    -c:v h264_videotoolbox -b:v 8M \
    -c:a copy -movflags +faststart \
    "$OUTPUT"
  echo "[reframe] wrote $OUTPUT" >&2
  exit 0
fi

# Face-tracked crop trajectory
export UV_PROJECT_ENVIRONMENT="${UV_PROJECT_ENVIRONMENT:-$HOME/.cache/video-editor-venv}"
PY_OUT="$(uv run --quiet --python 3.11 \
  --with "mediapipe" --with "opencv-python" --with "numpy" \
  python "$SCRIPT_DIR/reframe.py" "$INPUT" "$CMD_FILE")"
while IFS='=' read -r key value; do
  case "$key" in
    CROP_W|CROP_H|SRC_W|SRC_H)
      [[ "$value" =~ ^[0-9]+$ ]] || { echo "invalid $key from reframe.py: $value" >&2; exit 1; }
      printf -v "$key" '%s' "$value"
      ;;
    "") ;;
    *) echo "unexpected output from reframe.py: $key=$value" >&2; exit 1 ;;
  esac
done <<< "$PY_OUT"

ffmpeg -hide_banner -loglevel error -y \
  -i "$INPUT" \
  -filter_complex "[0:v]sendcmd=f=${CMD_FILE},crop=${CROP_W}:${CROP_H},scale=1080:1920[vout]" \
  -map "[vout]" -map 0:a? \
  -c:v h264_videotoolbox -b:v 8M \
  -c:a copy -movflags +faststart \
  "$OUTPUT"

echo "[reframe] wrote $OUTPUT" >&2
