#!/usr/bin/env bash
# transcribe.sh — runs WhisperX (large-v3 + wav2vec2 forced alignment) on every clip in a job folder
# usage: transcribe.sh <job_dir> [--diarize]
# output: /tmp/video-editor/<job-name>/words.json
#
# --diarize adds speaker labels per word (requires HUGGINGFACE_TOKEN in env;
# pyannote/speaker-diarization-3.1 must be accepted on Hugging Face).

set -euo pipefail

JOB_DIR="${1:?usage: transcribe.sh <job_dir> [--diarize]}"
JOB_DIR="$(cd "$JOB_DIR" && pwd)"
JOB_NAME="$(basename "$JOB_DIR")"
WORK="/tmp/video-editor/$JOB_NAME"
mkdir -p "$WORK"

DIARIZE=0
shift
while [ $# -gt 0 ]; do
  case "$1" in
    --diarize) DIARIZE=1 ;;
    *) echo "unknown flag: $1" >&2; exit 1 ;;
  esac
  shift
done

shopt -s nullglob nocaseglob
CLIPS=("$JOB_DIR"/*.mov "$JOB_DIR"/*.mp4 "$JOB_DIR"/*.mkv "$JOB_DIR"/*.m4v)
shopt -u nocaseglob
if [ ${#CLIPS[@]} -eq 0 ]; then
  echo "no clips found in $JOB_DIR" >&2
  exit 1
fi

export UV_PROJECT_ENVIRONMENT="${UV_PROJECT_ENVIRONMENT:-$HOME/.cache/video-editor-venv}"

uv run --quiet \
  --python 3.11 \
  --with "whisperx" \
  python - "$WORK/words.json" "$DIARIZE" "${CLIPS[@]}" <<'PY'
import json, os, sys
import whisperx

out_path = sys.argv[1]
diarize_flag = sys.argv[2] == "1"
clip_paths = sys.argv[3:]

# CPU + int8 is the reliable path on M-series. MPS support in whisperx/torch is
# still spotty for some ops; CPU is slower but never silently wrong.
device = "cpu"
compute_type = "int8"
batch_size = 8

print(f"[transcribe] loading whisperx large-v3 ({device}, {compute_type})", file=sys.stderr)
asr_model = whisperx.load_model("large-v3", device, compute_type=compute_type, language="en")

print("[transcribe] loading wav2vec2 alignment model", file=sys.stderr)
align_model, align_metadata = whisperx.load_align_model(language_code="en", device=device)

diarize_model = None
if diarize_flag:
    hf_token = os.environ.get("HUGGINGFACE_TOKEN", "").strip()
    if not hf_token:
        print("[transcribe] --diarize requires HUGGINGFACE_TOKEN in env", file=sys.stderr)
        sys.exit(1)
    print("[transcribe] loading pyannote diarization pipeline", file=sys.stderr)
    diarize_model = whisperx.DiarizationPipeline(use_auth_token=hf_token, device=device)

result = {"clips": []}
for path in clip_paths:
    name = os.path.basename(path)
    print(f"[transcribe] {name}", file=sys.stderr)
    audio = whisperx.load_audio(path)
    duration = len(audio) / 16000.0

    transcribe_result = asr_model.transcribe(audio, batch_size=batch_size, language="en")
    aligned = whisperx.align(
        transcribe_result["segments"],
        align_model,
        align_metadata,
        audio,
        device,
        return_char_alignments=False,
    )

    if diarize_model is not None:
        diarize_segments = diarize_model(audio)
        aligned = whisperx.assign_word_speakers(diarize_segments, aligned)

    words = []
    for seg in aligned.get("segments", []):
        for w in seg.get("words", []):
            # wav2vec2 sometimes can't align unspeakable tokens (numerals, punctuation).
            # Skip words missing timestamps so cuts.json builders don't crash.
            if "start" not in w or "end" not in w:
                continue
            entry = {
                "w": str(w.get("word", "")).strip(),
                "start": round(float(w["start"]), 3),
                "end": round(float(w["end"]), 3),
                "prob": round(float(w.get("score", 1.0)), 3),
            }
            if "speaker" in w:
                entry["speaker"] = w["speaker"]
            words.append(entry)

    result["clips"].append({
        "clip": name,
        "path": path,
        "duration": round(duration, 3),
        "words": words,
    })

with open(out_path, "w") as f:
    json.dump(result, f, indent=2)
print(f"[transcribe] wrote {out_path}", file=sys.stderr)
PY
