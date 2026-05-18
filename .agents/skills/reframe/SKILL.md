---
name: reframe
description: "Auto-reframes a 16:9 (or other landscape) video to 9:16 vertical for Reels/Shorts/TikTok. MediaPipe face tracking + EMA-smoothed crop window, FFmpeg crop+scale to 1080x1920. Auto-skips if the input is already vertical. Triggers: reframe to vertical, make this 9:16, vertical crop, reframe."
---

# Reframe — 16:9 → 9:16 with Face Tracking

Tracks the face across the video, smooths the trajectory so the crop doesn't twitch, and exports a 1080×1920 vertical version. Multi-person fallback: largest face wins.

## When to Use

- After `audio-polish`, before `broll` and `captions`.
- Standalone on any landscape video you want vertical.

## How It Works

1. **Detect face per frame** with MediaPipe Face Detector (model_selection=1, full-range up to 5m).
2. **Track face center X** (vertical doesn't need tracking — we keep full source height).
3. **EMA smooth** the X trajectory with α=0.15. Removes jitter from detector noise + tiny head movements.
4. **Build a sendcmd file** with one `crop x` command every 5 frames (0.17s precision at 30fps — finer than human eye can track).
5. **FFmpeg** chains `sendcmd → crop → scale=1080:1920`. h264_videotoolbox hardware encode.

If no face is detected in a frame, holds the previous position (or center on frame 0).

## Folder Contract

```
video-editor/outputs/
├── <job>__polished.mp4     ← input (audio-polished from previous step)
└── <job>__9x16.mp4         ← output (vertical)
```

## Usage

```bash
# Default output: <input_dir>/<input_stem>__9x16.mp4
bash .Codex/skills/reframe/scripts/reframe.sh video-editor/outputs/<job>__polished.mp4

# Explicit output
bash .Codex/skills/reframe/scripts/reframe.sh in.mp4 /tmp/out.mp4

# Skip face tracking, just center-crop (faster, dumb)
bash .Codex/skills/reframe/scripts/reframe.sh in.mp4 --center
```

## Auto-Skip

If the input is already vertical (height ≥ width), the script copies the file to the output path unchanged and exits in <1s. Lets you pipeline-blind every clip without checking.

## Pipeline

`rough-cut` → `audio-polish` → **reframe** → `broll` → `captions` → `post-content`

## Tuning Notes

| Param | Default | Effect |
|---|---|---|
| `EMA_ALPHA` | 0.15 | Lower = smoother (laggy), higher = snappier (twitchy). 0.15 is the talking-head sweet spot. |
| `SAMPLE_EVERY_N_FRAMES` | 5 | How often crop position updates. 5 @ 30fps = 6 updates/sec. Higher = faster compute but visible step. |
| `MIN_CONFIDENCE` | 0.5 | MediaPipe detection threshold. Lower if face gets lost in low light. |

All three live as constants at the top of `reframe.py`.

## Gotchas

- **Two faces, similar size** — picks the largest by bbox area. Can flicker between people. Future enhancement: persistence by IoU.
- **Quick pans / cuts** — the EMA causes a brief lag (~5 frames) after a cut. Bump α to 0.25 if it's noticeable.
- **No face visible at start** — first frame falls back to horizontal center, then locks onto the face once detected.
- **Source must have square pixels** — 99% of phone/camera footage. If your source is anamorphic (rare), pre-de-squeeze with `setsar=1`.
