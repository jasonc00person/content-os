#!/usr/bin/env bash
# transcribe.sh — runs faster-whisper on every clip in a job folder
# usage: transcribe.sh <job_dir>
# job_dir should contain clip files (.mov .mp4 .mkv .m4v)
# output: <job_dir>/working/words.json

set -euo pipefail

JOB_DIR="${1:?usage: transcribe.sh <job_dir>}"
JOB_DIR="$(cd "$JOB_DIR" && pwd)"
JOB_NAME="$(basename "$JOB_DIR")"
WORK="/tmp/video-editor/$JOB_NAME"
mkdir -p "$WORK"

shopt -s nullglob nocaseglob
CLIPS=("$JOB_DIR"/*.mov "$JOB_DIR"/*.mp4 "$JOB_DIR"/*.mkv "$JOB_DIR"/*.m4v)
shopt -u nocaseglob
if [ ${#CLIPS[@]} -eq 0 ]; then
  echo "no clips found in $JOB_DIR" >&2
  exit 1
fi

# ensure faster-whisper is available via uv (auto-installs on first run, cached after)
export UV_PROJECT_ENVIRONMENT="${UV_PROJECT_ENVIRONMENT:-$HOME/.cache/video-editor-venv}"

uv run --quiet \
  --python 3.11 \
  --with "faster-whisper" \
  --with "requests" \
  --with "onnxruntime" \
  python - "$WORK/words.json" "${CLIPS[@]}" <<'PY'
import json, os, sys
from faster_whisper import WhisperModel

out_path = sys.argv[1]
clip_paths = sys.argv[2:]

# large-v3 on CPU with int8 is the quality/speed sweet spot on M-series
model = WhisperModel("large-v3", device="auto", compute_type="int8")

result = {"clips": []}
for path in clip_paths:
    name = os.path.basename(path)
    print(f"[transcribe] {name}", file=sys.stderr)
    segments, info = model.transcribe(
        path,
        word_timestamps=True,
        vad_filter=True,
        vad_parameters=dict(min_silence_duration_ms=300),
        language="en",
    )
    words = []
    for seg in segments:
        if not seg.words:
            continue
        for w in seg.words:
            words.append({
                "w": w.word.strip(),
                "start": round(w.start, 3),
                "end": round(w.end, 3),
                "prob": round(w.probability, 3),
            })
    result["clips"].append({
        "clip": name,
        "path": path,
        "duration": round(info.duration, 3),
        "words": words,
    })

with open(out_path, "w") as f:
    json.dump(result, f, indent=2)
print(f"[transcribe] wrote {out_path}", file=sys.stderr)
PY
