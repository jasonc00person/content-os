#!/usr/bin/env bash
# transcribe-file.sh — plain-text transcript of a local media file (video or audio).
# usage: transcribe-file.sh <media-file> <out.txt>
#
# Same persistent faster-whisper venv the other transcription skills use
# (~/.cache/content-os/whisper-venv, built once, sentinel-gated). Prints nothing
# on stdout; the transcript lands in <out.txt>, one paragraph.
set -euo pipefail

for t in ffmpeg uv; do
  command -v "$t" >/dev/null 2>&1 || { echo "[error] $t is not installed — run ./setup.sh (or ./check-setup.sh) from the project root" >&2; exit 1; }
done

MEDIA="${1:?usage: transcribe-file.sh <media-file> <out.txt>}"
OUT="${2:?usage: transcribe-file.sh <media-file> <out.txt>}"
MODEL="${WHISPER_MODEL:-small.en}"
[ -s "$MEDIA" ] || { echo "[error] media file missing or empty: $MEDIA" >&2; exit 1; }

WORK="$(mktemp -d "${TMPDIR:-/tmp}/vcb-XXXXXX")"
trap 'rm -rf "$WORK"' EXIT

# 16 kHz mono wav — smallest input whisper is happy with
ffmpeg -nostdin -loglevel error -y -i "$MEDIA" -vn -ac 1 -ar 16000 "$WORK/audio.wav"

VENV="${CONTENT_OS_WHISPER_VENV:-$HOME/.cache/content-os/whisper-venv}"
PYBIN="$VENV/bin/python"
[ -e "$PYBIN" ] || PYBIN="$VENV/Scripts/python.exe"   # Windows venv layout
# sentinel written only after a successful install — a half-built venv (install
# interrupted once) self-heals on the next run instead of wedging forever
if [ ! -e "$VENV/.deps-ok" ]; then
  echo "[transcribe] first-run: building faster-whisper venv at $VENV" >&2
  rm -rf "$VENV"
  uv venv "$VENV" --python 3.11 >&2
  PYBIN="$VENV/bin/python"; [ -e "$PYBIN" ] || PYBIN="$VENV/Scripts/python.exe"
  uv pip install --python "$PYBIN" faster-whisper onnxruntime >&2
  touch "$VENV/.deps-ok"
fi

echo "[transcribe] model=$MODEL file=$(basename "$MEDIA")" >&2
"$PYBIN" - "$(cd "$(dirname "$0")" && pwd)" "$WORK/audio.wav" "$OUT" "$MODEL" <<'PY'
import sys
sys.path.insert(0, sys.argv[1]); sys.dont_write_bytecode = True  # no __pycache__ beside the scripts
import fw_fast  # picks the fastest lane on this machine: NVIDIA GPU > Apple GPU > CPU

audio, out_file, model_name = sys.argv[2:]
# verbatim: the corpus is imitated word for word, and the fast batched mode drops filler words
segments, _info, _device = fw_fast.transcribe(audio, model_name, verbatim=True)
lines = [seg["text"] for seg in segments]
with open(out_file, "w", encoding="utf-8") as f:
    f.write(" ".join(lines).strip() + "\n")
print(f"[transcribe] {len(lines)} segments -> {out_file}", file=sys.stderr)
PY
