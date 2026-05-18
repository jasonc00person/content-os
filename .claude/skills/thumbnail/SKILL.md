---
name: thumbnail
description: "YouTube thumbnail generator via Higgsfield Nano Banana Pro. Claude reads the video's hook/title (Notion page or raw string), proposes thumbnail concepts with cinematic prompts anchored to Jason's face-ref photo library, you approve the manifest, then submits in parallel and downloads 16:9 PNGs ready for text overlay. Optional per-concept extra_refs let you bake in logos, products, or other brand assets. Triggers: make a thumbnail, yt thumbnail, generate thumbnail, youtube thumbnail, design a thumbnail."
---

# Thumbnail — YouTube Thumbnails via Nano Banana Pro

Generates branded YT thumbnails anchored to a small library of real photos of Jason at `assets/face-refs/`. Claude reads the video's hook, proposes concepts (composition, expression, lighting, single visual metaphor), then `nano_banana_2` (Nano Banana Pro) renders 16:9 variants. Optional `extra_refs` per concept bake in logos / products / scene refs alongside the face anchors. No generated text on the image — title overlay happens in Photoshop/Figma after.

## Anchor Library (live)

| Source | Purpose |
|---|---|
| `assets/face-refs/*.{png,jpg,jpeg,webp}` | Real and AI-generated photos of Jason, varied angles + expressions + lighting. Always passed as `--image <path>` on every generation. |
| `assets/logos/*.png` | Brand marks (Claude, Codex, etc.) — referenced per-concept via `extra_refs`. |

The CLI auto-uploads local paths every run. No upload-id cache to manage. Adding a new file to `assets/face-refs/` takes effect on the next generation automatically.

**Why this approach beats Soul V2:** Soul-trained fine-tunes drift, leak training-image artifacts (UI screenshots, gibberish text), and lock you into the Soul-aware model lineup. `nano_banana_2` with multi-photo `input_images` gives photoreal output, locks identity from 3+ angles simultaneously, and unlocks the SOTA image models. Trade-off: $2/image vs $0.12 for Soul V2 — but Soul V2 results were unusable so this is the actual price.

**Proven settings (codex-vs-claude-code test, 2026-05-17):** 6 face-refs + 2 logo extra_refs + `nano_banana_2` at `16:9 / 2k` produced clean photoreal output, recognizable logos, locked identity, zero hallucinated text. The orange Anthropic brand vs the purple-blue Codex brand creates a natural warm/cool color split — leverage it in prompts.

## When to Use

- Long-form YT videos before posting (`post-content` doesn't generate the thumbnail).
- Standalone — not part of the rough-cut → captions pipeline (that's reels).
- Re-roll freely; cost is ~$6/concept set of 3 variants.

## The Flow

```
1. Claude reads input: a Notion page name/ID OR a raw title string
2. Claude writes /tmp/thumbnails/<slug>/thumb.json — concepts + prompts + (optional) extra_refs
3. You review the manifest, edit prompts, drop concepts
4. Run generate.py → uploads new face-refs/logos, submits in parallel, downloads
5. Pick the winner → add title type in Photoshop/Figma → upload to YT
```

**Manifest review is the safety gate.** No money spent until you say go.

## Manifest Schema

```json
{
  "topic": "Codex vs. Claude Code",
  "slug": "codex-vs-claude-code",
  "model": "nano_banana_2",
  "aspect_ratio": "16:9",
  "quality": "2k",
  "variants_per_concept": 3,
  "concepts": [
    {
      "id": "c1",
      "name": "split-verdict",
      "prompt": "...",
      "extra_refs": [
        "assets/logos/claude-icon-color.png",
        "assets/logos/codex-icon-color.png"
      ]
    },
    {
      "id": "c2",
      "name": "shock-vs",
      "prompt": "...",
      "model": "seedream_v4_5",
      "quality": "high"
    }
  ]
}
```

**Defaults** (overrideable per concept):
- `model` — `nano_banana_2`
- `aspect_ratio` — `16:9`
- `quality` — `2k` for nano_banana_2 (no extra cost), `high` for seedream_v4_5
- `variants_per_concept` — `3`

**`extra_refs`** — paths relative to project root or absolute. Appended to the auto-loaded face-refs on every variant of that concept. Use for logos, product shots, color palette refs, or scene references.

**Per-model quality flag** (auto-handled by script):
| Model | CLI flag | Valid values |
|---|---|---|
| `nano_banana_2` | `--resolution` | `1k`, `2k`, `4k` |
| `seedream_v4_5` | `--quality` | `basic`, `high` |

`text2image_soul_v2` is **not supported** by this skill — it uses a different schema (`medias` + `custom_reference_id`, not `input_images`) and Soul-fine-tune drift produced unusable results. Pin to `nano_banana_2` unless you specifically need seedream's cinematic flair.

## Prompt Style Guide

Thumbnail prompts ≠ B-roll prompts. Different rules:

| Element | Thumbnail | B-roll |
|---|---|---|
| Subject | "This person" — face fidelity from input_images | Concrete scene |
| Expression | **Critical** — wide-eye, half-smirk, raised brow, mouth-open shock. Locked into prompt. | Often abstract / no face |
| Composition | Rule-of-thirds. Call out negative space for title overlay. | Cinematic motion focus |
| Background | One legible visual metaphor (lightning, smoke, dust, glow, color split) | Environmental texture |
| Color | High contrast, 2-color story (cool/warm split, teal/orange, blue/red) | Mood-driven, varied |
| Lens / lighting | "35mm shallow DOF", "key light from camera-left", "neon practicals" | Same toolkit |
| **Forbidden** | "text on screen", "title overlay", "subtitles", "ChatGPT chat UI", "terminal interface", any text-bearing UI element. Nano Banana Pro will hallucinate gibberish letters wherever you imply text. Use abstract physical metaphors instead. | n/a |

✅ **Good prompt:**
"Photoreal portrait of this person mid-shocked-laugh, eyes wide, mouth open, hands raised palms-up. Background bisected vertically — left half deep electric-blue lightning column, right half warm amber dust storm. Hard-edge color split behind silhouette. Studio key from above, 50mm shallow DOF, photoreal cinematic. Negative space lower-third for title overlay."

❌ **Bad prompt:**
"Claude Code vs ChatGPT thumbnail showing him looking at a terminal screen with code and a chat window"

Why bad: names a screen + terminal + chat window = model renders gibberish text on all three.

## Usage

```bash
# After Claude writes /tmp/thumbnails/<slug>/thumb.json and you've reviewed it:
python3 .claude/skills/thumbnail/scripts/generate.py /tmp/thumbnails/<slug>/thumb.json

# Re-roll one concept:
python3 .claude/skills/thumbnail/scripts/generate.py /tmp/thumbnails/<slug>/thumb.json --only c1

# Dry-run:
python3 .claude/skills/thumbnail/scripts/generate.py /tmp/thumbnails/<slug>/thumb.json --dry-run
```

Output: `video-editor/outputs/thumbnails/<slug>/<concept_id>_v<n>.png`.

## CLI Quirks (read before editing)

**Authoritative upstream docs** (canonical source — read these before guessing):
- [`higgsfield-ai/skills/higgsfield-generate/references/media-inputs.md`](https://github.com/higgsfield-ai/skills/blob/main/higgsfield-generate/references/media-inputs.md) — per-model media roles, single-vs-multi-image models, schema mismatch error meanings
- [`higgsfield-ai/skills/higgsfield-generate/references/prompt-engineering.md`](https://github.com/higgsfield-ai/skills/blob/main/higgsfield-generate/references/prompt-engineering.md) — prompt length caps, image-to-image vs image-to-video framing, ip-detect / nsfw rejection avoidance
- [`higgsfield-ai/skills/higgsfield-generate/references/model-catalog.md`](https://github.com/higgsfield-ai/skills/blob/main/higgsfield-generate/references/model-catalog.md) — full model list with use-case mapping

Same playbook as `broll`. Notes on the installed CLI `v0.1.40`:

- **No `--output-dir`.** Script runs with `--json --wait`, walks the response for `status: completed` + `result_url`, downloads via urllib.
- **`--image` is the canonical face-anchor flag** — repeat it once per reference: `--image ./a.png --image ./b.png --image <upload_id>`. The CLI auto-uploads local paths (no manual `higgsfield upload create` needed). The `--input_images` JSON-array shape works too but is more brittle and required for advanced types (`image_job`, `nano_banana_2_job` etc. — unused here).
- **Quality flag differs per model** — `nano_banana_2` uses `--resolution`, `seedream_v4_5` uses `--quality`. Script maps via `MODEL_CONFIG`.
- **Multi-image ref cap is per-model** — Nano Banana Pro accepts ~8 images per upstream docs. 6 face-refs + 2 logos = inside the headroom.
- **Result extraction is strict** — only matches nodes with `status: completed` + `result_url`. No regex fallback (would grab echoed `--image` upload URLs).
- **Model schema source of truth:** `higgsfield model get <model>` — NOT `generate create --help` (only shows global flags).
- **Auth check is `higgsfield account status`**, not `auth status` (which is a help menu).

## Cost Math (Higgsfield)

| Model | Cost / image | Notes |
|---|---|---|
| `nano_banana_2` (Pro) | **2 credits (~$2)** | Default. Best identity from input_images. No cost difference 1k/2k/4k. |
| `seedream_v4_5` | 1 credit (~$1) | Cinematic flair, slight identity drift |

Typical run:
- 2 concepts × 3 variants × nano_banana_2 = 6 images × $2 = **$12**
- 1 concept × 3 variants × nano_banana_2 = **$6**

Script prints estimate before submit:
```
[thumb] 2 concept(s) × 3 variant(s) = 6 images ≈ $12.00 total. Continue? [y/N]
```

## Gotchas

- **Generation time** — 30–60s per image, parallel via `--wait`. 6-image batch ≈ 1–2 min wall.
- **Identity fidelity scales with refs** — 6 face-refs > 2 > 1. Add a new pose to `assets/face-refs/` and the next run picks it up automatically (mtime cache invalidates).
- **Logos in extra_refs** — Nano Banana Pro respects brand-mark composition well but doesn't always render them at the size you wrote. If a logo comes out tiny, say "large prominent logo" explicitly in the prompt.
- **Negative space is a request, not a guarantee** — verify on output before paying for type-overlay work.
- **Failed generations** — script reports per-concept failures. Re-run with `--only c2` to retry.
- **Manifest review is mandatory** — never auto-approve. Prompts are the creative work.
- **No text in image** — title type goes on in Photoshop/Figma after. The model will hallucinate gibberish if asked for words.

## What This Skill Does NOT Do

- Render title type on the thumbnail (Photoshop/Figma after)
- Pull Notion script content automatically (Claude does that before writing the manifest)
- Upload to YouTube (`post-content` handles posting)
- Generate Reels covers / IG carousel covers (different aspect, different rules — out of scope)
- Train Soul IDs or run Marketing Studio workflows (broader Higgsfield surface — this skill is just thumbnails)
