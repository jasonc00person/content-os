---
name: audio-polish
description: "Cleans the audio on a video file. FFmpeg afftdn denoise + loudnorm to -14 LUFS (broadcast/social standard). Optional music bed with sidechain duck. Pure audio pass — never re-encodes video. Triggers: polish the audio, clean audio, normalize audio, audio-polish, add music bed."
---

# Audio Polish — Voice Clean + Loudness Standard

Cleans the audio track on a video file. Denoises, normalizes loudness, optionally lays a music bed under the voice with sidechain ducking so the music gets quiet when you talk and loud when you're silent.

**Never re-encodes video** — uses `-c:v copy` so the visual quality is byte-identical to the input.

## When to Use

- Right after `rough-cut`, before reframe/broll/captions.
- Standalone on any existing reel that sounds quiet, peaky, or noisy.

## Folder Contract

```
video-editor/
├── inbox/
│   └── <job>/
│       └── music/                ← OPTIONAL — drop one .mp3 here to enable a music bed
│           └── bed.mp3
└── outputs/
    ├── <job>.mp4                 ← input (rough-cut output)
    └── <job>__polished.mp4       ← output (audio cleaned)
```

If `inbox/<job>/music/*.mp3` exists, it gets auto-detected and used as the bed. Otherwise voice-only polish.

## The Chain

1. **afftdn=nr=12** — FFT denoise on the voice. 12dB noise reduction is the sweet spot (more = artifacts, less = audible hiss).
2. **loudnorm=I=-14:TP=-1:LRA=11** — normalize to -14 LUFS (Spotify/TikTok/IG/YT spec), peak -1dBTP, loudness range 11.
3. *(optional)* **sidechaincompress** on music keyed to voice — ducks music ~8dB when voice is active, releases over 400ms.
4. **amix** voice + ducked music.

Everything is one FFmpeg pass. Re-encoded audio (AAC 192k), copied video. Fast.

## Usage

```bash
# Default: detect job folder's music dir, write <input>__polished.mp4 next to input
bash .claude/skills/audio-polish/scripts/polish.sh video-editor/outputs/<job>.mp4

# Explicit output path
bash .claude/skills/audio-polish/scripts/polish.sh video-editor/outputs/<job>.mp4 /tmp/out.mp4

# Force a specific music file (overrides auto-detect)
bash .claude/skills/audio-polish/scripts/polish.sh video-editor/outputs/<job>.mp4 --music ~/music/lofi.mp3

# Skip music bed even if one exists in inbox
bash .claude/skills/audio-polish/scripts/polish.sh video-editor/outputs/<job>.mp4 --no-music
```

## Defaults Worth Knowing

| Param | Value | Why |
|---|---|---|
| Target loudness | **-14 LUFS** | Spotify/IG/TikTok/YT spec. Louder = platforms attenuate. Quieter = sounds weak. |
| True peak | **-1 dBTP** | Prevents inter-sample clipping after platform re-encode. |
| LRA | **11** | Typical for spoken word. Music alone wants 7. |
| Denoise | **12 dB** | Tuned for indoor talking-head with HVAC/room tone. Bump higher for noisier rooms. |
| Music bed level | **-22 dB** | Quiet enough to hide under voice, loud enough to be felt between lines. |
| Duck depth | **~8 dB** | Music drops noticeably when voice fires, doesn't disappear. |

Edit `polish.sh` if any of these feel off for a specific reel.

## Pipeline

`rough-cut` → **audio-polish** → `reframe` → `broll` → `captions` → `post-content`

Audio polish runs early so every downstream skill works on the clean audio.

## Gotchas

- **MP3 music bed**: stereo, any sample rate. Loops automatically if shorter than the video.
- **No music dir** = pure voice clean, which is the most common case. Don't force a music bed if the reel doesn't need one.
- **Loudnorm is single-pass dynamic** — fast and good enough for short reels. Two-pass linear is ~10% more accurate but doubles runtime. Not worth it here.
- **Don't run twice** — the second loudnorm pass will over-compress an already-normalized track.
