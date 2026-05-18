#!/usr/bin/env bash
# render.sh — overlay broll clips onto a base video. Audio of base video is preserved.
# usage: render.sh <broll_resolved.json> <base_video.mp4> [output.mp4]
#
# Default output: <base_dir>/<base_stem>__broll.mp4
#
# Reads moments[] from broll_resolved.json; each needs t_start, t_end, path (local mp4).
# Moments without "path" (failed generations) are skipped.

set -euo pipefail

MANIFEST="${1:?usage: render.sh <broll_resolved.json> <base_video.mp4> [output.mp4]}"
BASE="${2:?need base video}"
OUTPUT="${3:-}"

[ -f "$MANIFEST" ] || { echo "manifest not found: $MANIFEST" >&2; exit 1; }
[ -f "$BASE" ] || { echo "base video not found: $BASE" >&2; exit 1; }

BASE="$(cd "$(dirname "$BASE")" && pwd)/$(basename "$BASE")"
BASE_DIR="$(dirname "$BASE")"
BASE_STEM="$(basename "${BASE%.*}")"
[ -z "$OUTPUT" ] && OUTPUT="$BASE_DIR/${BASE_STEM}__broll.mp4"

FILTER_FILE="$(mktemp /tmp/broll-filter.XXXXXX.txt)"
INPUTS_FILE="$(mktemp /tmp/broll-inputs.XXXXXX.sh)"
MAP_FILE="$(mktemp /tmp/broll-map.XXXXXX.txt)"
trap 'rm -f "$FILTER_FILE" "$INPUTS_FILE" "$MAP_FILE"' EXIT

python3 - "$MANIFEST" "$BASE" "$FILTER_FILE" "$INPUTS_FILE" "$MAP_FILE" <<'PY'
import json, sys
manifest_path, base, filter_path, inputs_path, map_path = sys.argv[1:6]
manifest = json.loads(open(manifest_path).read())

inputs = ["-i", base]
filter_parts = []
prev = "0:v"
overlay_idx = 0

for m in manifest.get("moments") or []:
    path = m.get("path")
    if not path:
        continue
    t0 = float(m["t_start"])
    t1 = float(m["t_end"])
    overlay_idx += 1
    in_idx = overlay_idx
    inputs.extend(["-i", path])
    filter_parts.append(
        f"[{in_idx}:v]scale=1080:1920:force_original_aspect_ratio=increase,"
        f"crop=1080:1920,setpts=PTS-STARTPTS+{t0}/TB[b{in_idx}]"
    )
    filter_parts.append(
        f"[{prev}][b{in_idx}]overlay=enable='between(t,{t0},{t1})':"
        f"eof_action=pass[v{in_idx}]"
    )
    prev = f"v{in_idx}"

with open(filter_path, "w") as f:
    f.write(";\n".join(filter_parts))
with open(inputs_path, "w") as f:
    f.write(json.dumps(inputs))
with open(map_path, "w") as f:
    f.write(f"[{prev}]" if filter_parts else "0:v")
PY

if [ ! -s "$FILTER_FILE" ]; then
  echo "[broll] no resolved moments — copying base video unchanged" >&2
  cp "$BASE" "$OUTPUT"
  echo "[broll] wrote $OUTPUT" >&2
  exit 0
fi

MAP_V="$(cat "$MAP_FILE")"
INPUTS=()
while IFS= read -r line; do
  INPUTS+=("$line")
done < <(python3 - "$INPUTS_FILE" <<'PY'
import json, sys
for arg in json.loads(open(sys.argv[1]).read()):
    print(arg)
PY
)

ffmpeg -hide_banner -loglevel error -y "${INPUTS[@]}" \
  -filter_complex_script "$FILTER_FILE" \
  -map "$MAP_V" -map 0:a? \
  -c:v h264_videotoolbox -b:v 8M \
  -c:a copy -movflags +faststart \
  "$OUTPUT"

echo "[broll] wrote $OUTPUT" >&2
