#!/usr/bin/env bash
# polish.sh — audio cleanup on a video file
# usage: polish.sh <input.mp4> [output.mp4] [--music <path.mp3>|--no-music]
#
# Default output:  <input_dir>/<input_stem>__polished.mp4
# Default music:   inbox/<job>/music/*.mp3 if present (job inferred from input filename stem)

set -euo pipefail

INPUT="${1:?usage: polish.sh <input.mp4> [output.mp4] [--music <path>|--no-music]}"
if [ ! -f "$INPUT" ]; then
  echo "input not found: $INPUT" >&2; exit 1
fi
INPUT="$(cd "$(dirname "$INPUT")" && pwd)/$(basename "$INPUT")"
shift

OUTPUT=""
MUSIC=""
NO_MUSIC=0
while [ $# -gt 0 ]; do
  case "$1" in
    --music)
      [ -n "${2:-}" ] || { echo "--music requires a file path" >&2; exit 1; }
      MUSIC="$2"
      shift 2
      ;;
    --no-music) NO_MUSIC=1; shift ;;
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
[ -z "$OUTPUT" ] && OUTPUT="$INPUT_DIR/${INPUT_STEM}__polished.mp4"

# auto-detect music bed in inbox/<job>/music/*.mp3 (only if no flags set)
if [ -z "$MUSIC" ] && [ "$NO_MUSIC" -eq 0 ]; then
  # Walk up from input dir to find a sibling `inbox` and a job dir matching INPUT_STEM
  REPO_ROOT="$INPUT_DIR"
  while [ "$REPO_ROOT" != "/" ] && [ ! -d "$REPO_ROOT/inbox" ]; do
    REPO_ROOT="$(dirname "$REPO_ROOT")"
  done
  CANDIDATE_DIR="$REPO_ROOT/inbox/$INPUT_STEM/music"
  if [ -d "$CANDIDATE_DIR" ]; then
    FOUND="$(ls "$CANDIDATE_DIR"/*.mp3 2>/dev/null | head -n1 || true)"
    [ -n "$FOUND" ] && MUSIC="$FOUND"
  fi
fi

VOICE_CHAIN="afftdn=nr=12,loudnorm=I=-14:TP=-1:LRA=11"

if [ -n "$MUSIC" ]; then
  [ -f "$MUSIC" ] || { echo "music file not found: $MUSIC" >&2; exit 1; }
  echo "[polish] voice + music bed: $MUSIC" >&2
  ffmpeg -hide_banner -loglevel error -y \
    -i "$INPUT" \
    -stream_loop -1 -i "$MUSIC" \
    -filter_complex "[0:a]${VOICE_CHAIN}[voice];[1:a]volume=-22dB[music];[music][voice]sidechaincompress=threshold=0.04:ratio=8:attack=20:release=400:makeup=2[ducked];[voice][ducked]amix=inputs=2:duration=first:dropout_transition=0[aout]" \
    -map 0:v -map "[aout]" \
    -c:v copy -c:a aac -b:a 192k -ar 48000 \
    -movflags +faststart \
    "$OUTPUT"
else
  echo "[polish] voice only" >&2
  ffmpeg -hide_banner -loglevel error -y \
    -i "$INPUT" \
    -af "$VOICE_CHAIN" \
    -c:v copy -c:a aac -b:a 192k -ar 48000 \
    -movflags +faststart \
    "$OUTPUT"
fi

echo "[polish] wrote $OUTPUT" >&2
