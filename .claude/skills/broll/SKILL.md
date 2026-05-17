---
name: broll
description: "Generative B-roll inserts via Higgsfield. Claude reads the cut transcript + intent and proposes B-roll moments with cinematic prompts, you approve, the skill submits to Higgsfield, downloads, and overlays the clips on your video while keeping the voice audio. Triggers: add b-roll, broll, generate broll, insert b-roll, cinematic cutaways."
---

# B-Roll — Generative Cinematic Inserts via Higgsfield

The differentiator. Instead of keyword-matched stock footage, Claude reads your script's beats and writes **intentional generation prompts** that match what you're actually saying. You approve the manifest before spending money, then Higgsfield generates 5-second cinematic clips that overlay on your video at the right beats. Voiceover continues underneath.

## When to Use

- After `reframe`, before `captions`. The captions get burned on top of the B-roll overlays.
- Reels where a few well-placed cutaways would amplify the message (most of them).
- Skip when the talking head IS the moment (rants, big emotional beats, direct-to-camera challenges).

## The Flow

```
1. Claude reads /tmp/video-editor/<job>/cuts.json + inbox/<job>/intent.md
2. Claude writes /tmp/video-editor/<job>/broll.json — proposed moments + prompts
3. You review the manifest, edit prompts, drop moments
4. Run generate.py → submits to Higgsfield in parallel, polls, downloads
5. Run render.sh → overlays clips on the video
```

**The manifest review is the safety gate.** No money spent until you say go.

## Manifest Schema

```json
{
  "video": "video-editor/outputs/<job>__9x16.mp4",
  "duration_default": 5,
  "moments": [
    {
      "id": "m1",
      "t_start": 4.2,
      "t_end": 6.8,
      "prompt": "Cinematic close-up of hands typing on a sleek MacBook, golden hour light streaming through window, shallow depth of field, soft bokeh, anamorphic lens, slow push-in",
      "covers_line": "for free in five minutes"
    }
  ]
}
```

`t_start`/`t_end` are timestamps **on the final video** (post rough-cut/reframe). `covers_line` is just a comment to make the manifest readable. `duration_default` is the Higgsfield gen length (default 5s — leaves slack at the trim ends).

## Prompt Style Guide

Higgsfield's strength is cinematic motion. Write prompts like a DOP, not a stock keyword search:

✅ **Good:** "Cinematic over-the-shoulder of someone scrolling a glowing iPhone in dim bedroom, neon city lights through window, shallow DOF, slow handheld drift"

❌ **Bad:** "person on phone at night"

| Element | Why |
|---|---|
| Subject + action | Concrete physical thing happening, not a concept |
| Lighting | "Golden hour", "neon", "soft window light", "harsh practical" |
| Lens | "Anamorphic", "85mm portrait", "wide environmental", "macro" |
| Motion | "Slow push-in", "static lockoff", "handheld drift", "orbit" |
| Mood beat | Optional but helps: "isolated", "intimate", "urgent" |

Default to slow/subtle motion. Hectic generative motion fights the voiceover.

## Usage

```bash
# Step 1: Generate the clips from the manifest (run after manifest approval)
python3 .claude/skills/broll/scripts/generate.py /tmp/video-editor/<job>/broll.json

# Step 2: Overlay onto the video
bash .claude/skills/broll/scripts/render.sh /tmp/video-editor/<job>/broll_resolved.json video-editor/outputs/<job>__9x16.mp4
```

Default output: `<input_dir>/<input_stem>__broll.mp4`.

## Pipeline

`rough-cut` → `audio-polish` → `reframe` → **broll** → `captions` → `post-content`

## API Setup

Add to `.env`:
```
HIGGSFIELD_API_KEY=hgs_xxxxxxxxxxxx
```

Get a key at [cloud.higgsfield.ai](https://cloud.higgsfield.ai/). The skill reads it via:
```bash
export HIGGSFIELD_API_KEY=$(grep HIGGSFIELD_API_KEY /path/to/.env | cut -d= -f2)
```

## Cost Math (Higgsfield)

- ~$0.50–1.00 per 5-second clip
- A typical reel uses 3–6 moments → **$1.50–6 per reel**
- The skill prints an estimate before submitting:
  ```
  [broll] Submitting 4 moments × 5s each ≈ $2-4 total. Continue? [y/N]
  ```

## Gotchas

- **Generation time** — 60–120s per clip, run in parallel. A 4-moment manifest takes ~2-3 min wall time.
- **Clip duration must cover the window** — request 5s, use windows ≤5s. If you want a longer cover, split into two adjacent moments with different prompts.
- **Overlay scaling** — Higgsfield returns 720p or 1080p clips. The render scales to 1080×1920 vertical (crop center). For full visual control, use 9:16 motion prompts ("vertical composition", "portrait framing").
- **Audio is dropped from generated clips** — only the original video's audio plays. Generated audio is usually generic music or noise; you don't want it.
- **Failed generations** — if Higgsfield fails on a moment, the script reports it and leaves a gap. Re-run with just that moment's id to retry: `generate.py broll.json --only m3`.
- **Manifest review is mandatory** — never auto-approve. The prompts ARE the creative work; if Claude got one wrong, fix it before paying for it.

## What This Skill Does NOT Do

- Generate audio/music for the B-roll (irrelevant — voice plays underneath)
- Generate from reference images (text-to-video only for now; image-to-video is a future add)
- Decide when to use B-roll vs let the talking head breathe — that's Claude's editorial call in the proposal step
