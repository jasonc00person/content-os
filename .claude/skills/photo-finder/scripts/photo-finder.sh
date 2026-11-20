#!/usr/bin/env bash
# photo-finder.sh — builds the persistent venv once, then runs photo_finder.py with the given args.
#   bash .claude/skills/photo-finder/scripts/photo-finder.sh find [--since YYYY-MM-DD] [--look "..."] [--refs DIR]
#   bash .claude/skills/photo-finder/scripts/photo-finder.sh export photos/runs/<stamp> 3,7,12 [--downloads]
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"

[ "$(uname)" = "Darwin" ] || { echo "[photo-finder] macOS only (reads the Photos library)" >&2; exit 1; }

# Persistent venv: built once, reused every run. The sentinel is written only after a
# successful install, so an interrupted build self-heals on the next run.
VENV="${CONTENT_OS_PHOTO_VENV:-$HOME/.cache/content-os/photo-finder-venv}"
if [ ! -e "$VENV/.deps-ok" ]; then
  echo "[photo-finder] first-run: building venv at $VENV (torch + SigLIP, a few minutes)" >&2
  rm -rf "$VENV"
  uv venv "$VENV" --python 3.12 >&2
  uv pip install --python "$VENV/bin/python" "osxphotos>=0.77.2" torch torchvision transformers \
    sentencepiece protobuf pillow numpy "aesthetic-predictor-v2-5==2024.12.18.1" >&2
  touch "$VENV/.deps-ok"
fi

exec "$VENV/bin/python" "$HERE/photo_finder.py" "$@"
