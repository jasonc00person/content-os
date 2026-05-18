#!/usr/bin/env bash
# splice.sh — cuts + concatenates clips per cuts.json
# usage: splice.sh <job_dir>
# reads:  /tmp/video-editor/<job-name>/cuts.json
# writes: video-editor/projects/<job-name>/outputs/<job-name>.mp4

set -euo pipefail

JOB_DIR="${1:?usage: splice.sh <job_dir>}"
JOB_DIR="$(cd "$JOB_DIR" && pwd)"
JOB_NAME="$(basename "$JOB_DIR")"
WORK="/tmp/video-editor/$JOB_NAME"
MEDIA_DIR="$JOB_DIR"
[ -d "$JOB_DIR/raw" ] && MEDIA_DIR="$JOB_DIR/raw"
OUT="$JOB_DIR/outputs"
CUTS="$WORK/cuts.json"
mkdir -p "$WORK/segments" "$OUT"

[ -f "$CUTS" ] || { echo "missing $CUTS" >&2; exit 1; }

# cuts.json schema:
# { "segments": [ { "clip": "clip-01.mov", "start": 1.2, "end": 4.8 }, ... ] }

# Extract each segment to a .ts intermediate. Use accurate output seeking so
# WhisperX word-level timestamps stay authoritative.
rm -f "$WORK/segments"/*.ts "$WORK/concat.txt" 2>/dev/null || true

python3 - "$MEDIA_DIR" "$CUTS" "$WORK" <<'PY' > "$WORK/segments.tsv"
import json, os, sys
media_dir, cuts_path, work = sys.argv[1:]
with open(cuts_path) as f:
    cuts = json.load(f)
for i, seg in enumerate(cuts["segments"]):
    clip_path = seg["clip"] if os.path.isabs(seg["clip"]) else os.path.join(media_dir, seg["clip"])
    start = float(seg["start"])
    end = float(seg["end"])
    if end <= start:
        raise SystemExit(f"segment {i} has end <= start: {seg}")
    if not os.path.exists(clip_path):
        raise SystemExit(f"clip not found for segment {i}: {clip_path}")
    print(f"{i}\t{clip_path}\t{start:.3f}\t{end - start:.3f}")
PY

while IFS=$'\t' read -r i clip start duration; do
  seg_file="$WORK/segments/seg-$(printf '%04d' "$i").ts"
  # -ss after -i = accurate seek; re-encode each segment to keep A/V sync clean.
  # NOTE: pure -c copy on arbitrary cut points often desyncs; small encode is worth it
  ffmpeg -nostdin -hide_banner -loglevel error -y \
    -i "$clip" -ss "$start" -t "$duration" \
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
