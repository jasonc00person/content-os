#!/usr/bin/env bash
# splice.sh — cuts + concatenates clips per cuts.json, single final re-encode
# usage: splice.sh <job_dir>
# reads:  /tmp/video-editor/<job-name>/cuts.json
# writes: video-editor/outputs/<job-name>.mp4

set -euo pipefail

JOB_DIR="${1:?usage: splice.sh <job_dir>}"
JOB_DIR="$(cd "$JOB_DIR" && pwd)"
JOB_NAME="$(basename "$JOB_DIR")"
WORK="/tmp/video-editor/$JOB_NAME"
# video-editor root is two levels up from job dir (inbox/<job>)
VIDEO_ROOT="$(cd "$JOB_DIR/../.." && pwd)"
OUT="$VIDEO_ROOT/outputs"
CUTS="$WORK/cuts.json"
mkdir -p "$WORK/segments" "$OUT"

[ -f "$CUTS" ] || { echo "missing $CUTS" >&2; exit 1; }

# Snap cut boundaries to silence if snap_silence.py exists and snapped file missing
SNAP_SCRIPT="$(dirname "$0")/snap_silence.py"
SNAPPED="$WORK/cuts_snapped.json"
if [ -f "$SNAP_SCRIPT" ]; then
  echo "[splice] snapping to silence..." >&2
  python3 "$SNAP_SCRIPT" "$JOB_DIR"
  [ -f "$SNAPPED" ] && CUTS="$SNAPPED"
fi

# cuts.json schema:
# { "segments": [ { "clip": "clip-01.mov", "start": 1.2, "end": 4.8 }, ... ] }

# extract each segment to a .ts intermediate (stream copy — instant, no quality loss)
rm -f "$WORK/segments"/*.ts "$WORK/concat.txt" 2>/dev/null || true

idx=0
python3 - "$JOB_DIR" "$CUTS" "$WORK" <<'PY' > "$WORK/segments.tsv"
import json, os, sys
job_dir, cuts_path, work = sys.argv[1:]
with open(cuts_path) as f:
    cuts = json.load(f)
for i, seg in enumerate(cuts["segments"]):
    clip_path = os.path.join(job_dir, seg["clip"])
    print(f"{i}\t{clip_path}\t{seg['start']}\t{seg['end']}")
PY

while IFS=$'\t' read -r i clip start end; do
  seg_file="$WORK/segments/seg-$(printf '%04d' "$i").ts"
  # -ss before -i = fast seek; re-encode here once to keep A/V sync clean on cuts
  # NOTE: pure -c copy on arbitrary cut points often desyncs; small encode is worth it
  ffmpeg -nostdin -hide_banner -loglevel error -y \
    -ss "$start" -to "$end" -i "$clip" \
    -c:v h264_videotoolbox -b:v 8M \
    -c:a aac -b:a 192k -ar 48000 -ac 2 \
    -avoid_negative_ts make_zero \
    -f mpegts "$seg_file"
  echo "file '$seg_file'" >> "$WORK/concat.txt"
done < "$WORK/segments.tsv"

# concat all segments (stream copy — fast)
ffmpeg -nostdin -hide_banner -loglevel error -y \
  -f concat -safe 0 -i "$WORK/concat.txt" \
  -c copy \
  -bsf:a aac_adtstoasc \
  "$WORK/concat.mp4"

# final normalize pass — loudness to -14 LUFS, strip any mpeg-ts oddness
ffmpeg -nostdin -hide_banner -loglevel error -y \
  -i "$WORK/concat.mp4" \
  -c:v copy \
  -af "loudnorm=I=-14:TP=-1.5:LRA=11" \
  -movflags +faststart \
  "$OUT/${JOB_NAME}.mp4"

echo "[splice] wrote $OUT/${JOB_NAME}.mp4" >&2
ffprobe -hide_banner -loglevel error -show_entries format=duration -of default=nw=1:nk=1 "$OUT/${JOB_NAME}.mp4"
