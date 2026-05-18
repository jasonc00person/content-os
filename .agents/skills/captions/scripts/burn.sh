#!/usr/bin/env bash
# burn.sh — burn captions onto a video from words.json (+ optional emphasis.json)
# usage: burn.sh <input.mp4> <words.json> [emphasis.json] [output.mp4]
#                [--style <name>] [--fixed] [--chin-gap <px>]
#
# Default output: <input_dir>/<input_stem>__final.mp4
# Default style:  clean  (minimal Helvetica Neue, white-only, bold emphasis)
# Other styles:   punch (viral yellow pop), mono (technical monospace) — see build_ass.py
#
# Default positioning: face-tracked. The skill runs track_face.py on the input
# and places each caption line a fixed gap below the speaker's chin. Pass
# --fixed to use the style preset's static marginV instead (or for clips
# with no visible face, e.g. pure B-roll segments).
#
# Uses libass via ffmpeg-full's `ass` filter. The stock Homebrew ffmpeg formula
# is built without libass; ffmpeg-full (keg-only) provides it without disturbing
# the system ffmpeg. Other skills (rough-cut, audio-polish, reframe, broll) still
# use the regular ffmpeg.

set -euo pipefail

STYLE="clean"
FIXED=0
CHIN_GAP=80
POSITIONAL=()
while [ $# -gt 0 ]; do
  case "$1" in
    --style)
      [ -n "${2:-}" ] || { echo "--style requires a value: punch, clean, or mono" >&2; exit 1; }
      STYLE="$2"
      shift 2
      ;;
    --style=*) STYLE="${1#--style=}"; shift ;;
    --fixed) FIXED=1; shift ;;
    --chin-gap)
      [ -n "${2:-}" ] || { echo "--chin-gap requires a pixel value" >&2; exit 1; }
      CHIN_GAP="$2"; shift 2
      ;;
    --chin-gap=*) CHIN_GAP="${1#--chin-gap=}"; shift ;;
    *) POSITIONAL+=("$1"); shift ;;
  esac
done
set -- "${POSITIONAL[@]}"

INPUT="${1:?usage: burn.sh <input.mp4> <words.json> [emphasis.json] [output.mp4] [--style punch|clean|mono]}"
WORDS="${2:?need words.json}"
EMPHASIS=""
OUTPUT=""

[ -f "$INPUT" ] || { echo "input not found: $INPUT" >&2; exit 1; }
[ -f "$WORDS" ] || { echo "words.json not found: $WORDS" >&2; exit 1; }
INPUT="$(cd "$(dirname "$INPUT")" && pwd)/$(basename "$INPUT")"
WORDS="$(cd "$(dirname "$WORDS")" && pwd)/$(basename "$WORDS")"

if [ "${3:-}" != "" ]; then
  case "$3" in
    *.json)
      EMPHASIS="$(cd "$(dirname "$3")" && pwd)/$(basename "$3")"
      OUTPUT="${4:-}"
      ;;
    *) OUTPUT="$3" ;;
  esac
fi

INPUT_DIR="$(dirname "$INPUT")"
INPUT_STEM="$(basename "${INPUT%.*}")"
[ -z "$OUTPUT" ] && OUTPUT="$INPUT_DIR/${INPUT_STEM}__final.mp4"

# Locate an ffmpeg binary that has libass compiled in
FFMPEG=""
for candidate in \
  "/opt/homebrew/opt/ffmpeg-full/bin/ffmpeg" \
  "/usr/local/opt/ffmpeg-full/bin/ffmpeg" \
  "$(command -v ffmpeg-full || true)" \
  "$(command -v ffmpeg)"
do
  [ -z "$candidate" ] && continue
  if [ -x "$candidate" ] && "$candidate" -hide_banner -h filter=ass 2>/dev/null | grep -q "^Filter ass"; then
    FFMPEG="$candidate"
    break
  fi
done
if [ -z "$FFMPEG" ]; then
  echo "no ffmpeg with libass found. Run: brew install ffmpeg-full" >&2
  exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
STAMP="$$-$(date +%s)"
ASS_FILE="/tmp/captions-${STAMP}.ass"
FACE_TRACK="/tmp/captions-${STAMP}-face.json"
trap 'rm -f "$ASS_FILE" "$FACE_TRACK"' EXIT

FACE_FLAG=()
if [ "$FIXED" -eq 0 ]; then
  export UV_PROJECT_ENVIRONMENT="${UV_PROJECT_ENVIRONMENT:-$HOME/.cache/video-editor-venv}"
  if uv run --quiet --python 3.11 \
       --with "mediapipe" --with "opencv-python" --with "numpy" \
       python "$SCRIPT_DIR/track_face.py" "$INPUT" "$FACE_TRACK" 2>&1 | sed 's/^/[track_face] /' >&2
  then
    FACE_FLAG=(--face-track "$FACE_TRACK" --chin-gap "$CHIN_GAP")
  else
    echo "[captions] face tracking failed; falling back to style's static marginV" >&2
  fi
fi

python3 "$SCRIPT_DIR/build_ass.py" "$WORDS" "$ASS_FILE" ${EMPHASIS:+"$EMPHASIS"} --style "$STYLE" ${FACE_FLAG[@]+"${FACE_FLAG[@]}"}

# The ass filter needs colons in the path escaped. Anywhere a literal colon
# could appear (rare on macOS but possible) -> \\:.
ASS_ESC="${ASS_FILE//:/\\:}"

"$FFMPEG" -hide_banner -loglevel error -y \
  -i "$INPUT" \
  -vf "ass=${ASS_ESC}" \
  -c:v h264_videotoolbox -b:v 8M \
  -c:a copy -movflags +faststart \
  "$OUTPUT"

POS_MODE="face-tracked"
[ "$FIXED" -eq 1 ] && POS_MODE="fixed"
echo "[captions] wrote $OUTPUT (style=$STYLE, pos=$POS_MODE)" >&2
