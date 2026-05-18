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
  "model_default": "seedance_2_0",
  "duration_default": 5,
  "aspect_ratio_default": "9:16",
  "moments": [
    {
      "id": "m1",
      "t_start": 4.2,
      "t_end": 6.8,
      "prompt": "Cinematic close-up of hands typing on a sleek MacBook, golden hour light streaming through window, shallow depth of field, soft bokeh, anamorphic lens, slow push-in",
      "covers_line": "for free in five minutes"
    },
    {
      "id": "m2",
      "t_start": 12.0,
      "t_end": 14.5,
      "model": "kling3_0",
      "start_image": "/path/to/reference.jpg",
      "prompt": "subtle product reveal, camera slowly pulls back, ambient motion",
      "covers_line": "the moment everything clicks"
    }
  ]
}
```

`t_start`/`t_end` are timestamps **on the final video** (post rough-cut/reframe). `covers_line` is a comment for readability.

**Defaults** (top-level, overrideable per moment):
- `model_default` — `seedance_2_0` (SOTA all-purpose video). Use `kling3_0` for the cleanest image-to-video.
- `duration_default` — `5` seconds. Seedance 2.0 supports 4–15s.
- `aspect_ratio_default` — `9:16`. Render still crops to 1080×1920 as a safety net.

**Per-moment overrides:**
- `model` — swap models for a single moment (e.g. `kling3_0` for image-to-video).
- `duration` — different clip length for this moment.
- `aspect_ratio` — different framing.
- `start_image` — local image path for **image-to-video**. The clip begins from this frame and the prompt describes the motion away from it. Pair with `kling3_0` for the cleanest transition or `seedance_2_0` for more dramatic motion.

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

## CLI Setup

Auth is browser-based via the `higgsfield` CLI — no API key, no `.env` entry.

```bash
# One-time install
curl -fsSL https://raw.githubusercontent.com/higgsfield-ai/cli/main/install.sh | sh

# One-time login (opens browser, ~5s)
higgsfield auth login
```

`generate.py` checks both before submitting. If the CLI is missing or the session is expired, it bails with the exact command you need to run.

## CLI Quirks (read before editing the scripts)

The upstream Higgsfield cookbook (`higgsfield-ai/skills` repo) shows flags and patterns the installed CLI (`v0.1.40`) does **not** actually support. The skill works around these — don't undo the workarounds by trusting the public docs.

- **No `--output-dir`.** Cookbook shows `higgsfield generate create … --output-dir ./dir`. Reality: `Error: Unknown params: output-dir`. `generate.py` instead runs with `--json --wait`, walks the response for any `.mp4` URL, and downloads it with urllib into `/tmp/video-editor/<job>/broll/<id>.mp4`. Keep that download path; don't reach for `--output-dir` again.
- **`duration` must be integer** for `seedance_2_0` (schema-enforced — `5.0` is rejected). `generate.py` casts before passing. If you add a new video model, check its schema before assuming floats work.
- **`higgsfield generate create --help` is misleading** — it shows only `-h, --help` and global flags. Model-specific params pass through dynamically. Truth source: `higgsfield model get <job_set_type>` (e.g. `seedance_2_0`, `kling3_0`). Always check that before adding/changing a model param.
- **`render.sh` uses a portable `while read` loop**, not `mapfile -t`. macOS ships bash 3.2, which has no `mapfile`. Don't "modernize" it.
- **Auth check is `higgsfield account status`**, not `higgsfield auth status` (which doesn't exist).

## Cost Math (Higgsfield)

- ~$0.50–1.00 per 5-second clip
- A typical reel uses 3–6 moments → **$1.50–6 per reel**
- The skill prints an estimate before submitting:
  ```
  [broll] Submitting 4 moments × 5s each ≈ $2-4 total. Continue? [y/N]
  ```

## Gotchas

- **Generation time** — 60–120s per clip, run in parallel via the CLI's `--wait`. A 4-moment manifest takes ~2-3 min wall time.
- **Clip duration must cover the window** — request 5s, use windows ≤5s. If you want a longer cover, split into two adjacent moments with different prompts. Seedance 2.0 supports up to 15s.
- **Aspect ratio is requested but render still crops** — manifest defaults to `--aspect_ratio 9:16` at submit, and the render scales to 1080×1920 (crop center) as a safety net. For tightest framing, also use 9:16 motion prompts ("vertical composition", "portrait framing").
- **Audio is dropped from generated clips** — only the original video's audio plays. Generated audio is usually generic music or noise; you don't want it.
- **Failed generations** — if Higgsfield fails on a moment, the script reports it and leaves a gap. Re-run with just that moment's id to retry: `generate.py broll.json --only m3`.
- **Manifest review is mandatory** — never auto-approve. The prompts ARE the creative work; if Claude got one wrong, fix it before paying for it.
- **Image-to-video model choice** — for `start_image` moments, `kling3_0` is the cleanest transition; `seedance_2_0` gives more dramatic motion. Default is `seedance_2_0`; swap per moment via the `model` field.

## What This Skill Does NOT Do

- Generate audio/music for the B-roll (irrelevant — voice plays underneath)
- Decide when to use B-roll vs let the talking head breathe — that's Claude's editorial call in the proposal step
- Train Soul Characters or run Marketing Studio ad workflows — that's the broader `higgsfield-generate` / `higgsfield-soul-id` surface; this skill is purposely scoped to inline cinematic cutaways for a single edited reel
