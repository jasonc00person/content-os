#!/usr/bin/env bash
# yt-download: download any yt-dlp URL as a Premiere-compatible MP4 (H.264 video + AAC audio).
# Usage: yt-download.sh <url> [output_dir] [max_height]
#   output_dir  default: ~/Downloads
#   max_height  default: 1080 (YouTube only serves H.264 up to 1080p; anything higher is VP9/AV1 and gets re-encoded)
# Prints the absolute path of the finished file on stdout.
set -euo pipefail

URL="${1:?usage: yt-download.sh <url> [output_dir] [max_height]}"
OUT_DIR="${2:-$HOME/Downloads}"
MAX_H="${3:-1080}"
mkdir -p "$OUT_DIR"

for bin in yt-dlp ffmpeg ffprobe; do
  command -v "$bin" >/dev/null || { echo "[error] $bin not installed (brew install $bin)" >&2; exit 1; }
done

# Prefer H.264 (avc1) + AAC (mp4a) streams so most downloads need no re-encode.
# Fall back to best-available so the download never fails on codec choice; the gate below fixes the codec.
# The cap is a sort, not a [height<=N] filter: yt-dlp's `res` is the SMALLER dimension, so a vertical
# 1080x1920 Short counts as 1080 (a height filter capped Shorts at 480x854).
FMT="bv*[vcodec^=avc1]+ba[acodec^=mp4a]/bv*[vcodec^=avc1]+ba/bv*+ba/b"
# Above 1080 there is no avc1 on YouTube, so the avc1 preference would silently hand back 1080p.
# Take the best stream at the requested size and let the gate below re-encode it.
[ "$MAX_H" -gt 1080 ] && FMT="bv*+ba/b"

FILE="$(yt-dlp -f "$FMT" -S "res:${MAX_H}" --merge-output-format mp4 --no-playlist \
  -o "${OUT_DIR}/%(title)s.%(ext)s" --print after_move:filepath --no-simulate "$URL" | tail -n 1)"
[ -f "$FILE" ] || { echo "[error] download failed" >&2; exit 1; }

VCODEC="$(ffprobe -v error -select_streams v:0 -show_entries stream=codec_name -of csv=p=0 "$FILE")"
ACODEC="$(ffprobe -v error -select_streams a:0 -show_entries stream=codec_name -of csv=p=0 "$FILE" || true)"

if [ "$VCODEC" = "h264" ] && { [ "$ACODEC" = "aac" ] || [ -z "$ACODEC" ]; }; then
  echo "[ok] $VCODEC/${ACODEC:-none}, no re-encode needed" >&2
else
  echo "[fix] $VCODEC/${ACODEC:-none} is not Premiere-safe, re-encoding to H.264/AAC" >&2
  TMP="${FILE%.*}.h264.tmp.mp4"
  ffmpeg -y -hide_banner -loglevel error -i "$FILE" \
    -c:v libx264 -preset veryfast -crf 18 -pix_fmt yuv420p \
    -c:a aac -b:a 192k -movflags +faststart "$TMP"
  mv -f "$TMP" "$FILE"
fi

echo "$FILE"
