---
name: captions
description: "Burns word-grouped captions onto a final video. Re-transcribes via WhisperX, Claude picks emphasis words from voice-dna, then generates a libass .ass with word-by-word reveal and burns via ffmpeg-full's ass filter. Three style presets: clean (default — minimal Helvetica), punch (viral yellow pop), mono (technical monospace). Triggers: add captions, caption this, burn captions, captions, subtitles."
---

# Captions — Word-Grouped Burn-In, Three Styles

Final-step skill in the pipeline. Re-transcribes the post-edited audio (so word timestamps match the cuts), groups words into 3–5-word visible lines snapped to natural pauses + sentence breaks, and burns them in via libass. Each word **fades in at its own start timestamp** (word-by-word reveal). How emphasis renders depends on the style preset.

**libass requirement:** the stock Homebrew `ffmpeg` formula is built without libass. The skill auto-detects `ffmpeg-full` (Homebrew's full-feature variant, installed at `/opt/homebrew/opt/ffmpeg-full/bin/ffmpeg`) and uses it. Other pipeline skills keep using regular `ffmpeg`. If `ffmpeg-full` is missing, install with:
```
brew install ffmpeg-full
```

## When to Use

- Last in the pipeline. Runs after `broll` so captions sit on top of B-roll overlays.
- Standalone on any video that has clear speech.

## Why Re-Transcribe?

Rough-cut's `words.json` is timestamped against the **raw clips**, before cuts were applied. The final video has different timestamps because segments were stitched in a new order. So we transcribe the final video to get aligned timestamps. WhisperX on a 60s reel = ~30s wall time, model is already warm.

## The Flow

```
1. Re-transcribe the final video:
   bash .claude/skills/rough-cut/scripts/transcribe.sh /tmp/captions-<job>
   (after first copying the final mp4 into /tmp/captions-<job>/clip.mp4)

2. Claude reads /tmp/video-editor/captions-<job>/words.json + voice-dna.md
   and writes /tmp/video-editor/captions-<job>/emphasis.json with words to pop:
   {"emphasis": ["delete", "paying", "claude", "five minutes"]}

3. Burn:
   bash .claude/skills/captions/scripts/burn.sh <input.mp4> <words.json> [emphasis.json]
```

## Style Defaults (Submagic-ish)

Pass `--style <name>` to `burn.sh`. Default is **clean**.

### clean (default)
Minimal, white-only, bold-weight emphasis. Documentary / thought-leader feel.

| | |
|---|---|
| Font | Helvetica Neue, 68pt |
| Color | White only — emphasis = bold weight, not color |
| Outline | 2px thin black + soft drop shadow |
| Position | marginV 580 (safe zone above IG/TikTok UI) |
| Word reveal | 80ms fade per word (elegant pacing) |
| Emphasis pop | None |
| Line tail | +250ms after last word |

### punch
Viral Submagic-style. Maximum attention.

| | |
|---|---|
| Font | Arial Black, 84pt (88pt emphasis) |
| Color | White / **yellow** (#FFFF00) emphasis |
| Outline | 5px chunky black |
| Position | marginV 620 (safe zone above IG/TikTok UI) |
| Word reveal | 60ms fade per word |
| Emphasis pop | Scale 100% → 118% → 100% over 200ms |
| Line tail | +200ms |

### mono
Technical / dev / "AI guy" coded.

| | |
|---|---|
| Font | Menlo (monospace), 54pt |
| Color | White only — emphasis = bold |
| Outline | 3px black, minimal shadow |
| Position | marginV 580 (safe zone above IG/TikTok UI) |
| Words per line | 4 (mono is wider) |
| Word reveal | 50ms fade (snappy) |
| Emphasis pop | None |
| Line tail | +150ms |

Edit / add styles in the `STYLES` dict at the top of `build_ass.py`.

## Line Grouping Rules

A new caption line starts when ANY of these hits:

1. **Sentence boundary** — previous word ended in `.`, `?`, `!`
2. **Natural pause** — gap to next word > 0.5s
3. **Length cap** — current line already has 5 words

This gives the rhythm short-form viewers expect — no 9-word run-ons, no orphan trailing words.

## Emphasis Selection

Without an emphasis.json, falls back to: **longest content word per line** (skipping common stopwords). Decent baseline, beatable by Claude reading voice-dna.

The Claude flow:
1. Read `voice-dna.md` for the speaker's signature emphasis patterns
2. Read the transcript
3. Pick 1–2 words per line that carry the most weight (verbs > nouns > modifiers)
4. Write `emphasis.json`: `{"emphasis": ["word1", "phrase two", ...]}`

Words are matched case-insensitively. Multi-word phrases get treated as one emphasis block.

## Usage

```bash
# Default — clean style with Claude-curated emphasis
bash .claude/skills/captions/scripts/burn.sh \
  video-editor/projects/<job>/outputs/<job>__broll.mp4 \
  /tmp/video-editor/captions-<job>/words.json \
  /tmp/video-editor/captions-<job>/emphasis.json

# Pick a different style
bash .claude/skills/captions/scripts/burn.sh ... --style punch
bash .claude/skills/captions/scripts/burn.sh ... --style mono

# No emphasis JSON — falls back to longest-content-word heuristic per line
bash .claude/skills/captions/scripts/burn.sh \
  video-editor/projects/<job>/outputs/<job>__broll.mp4 \
  /tmp/video-editor/captions-<job>/words.json
```

Default output: `<input_dir>/<input_stem>__final.mp4`.

## Pipeline

`rough-cut` → `audio-polish` → `reframe` → `broll` → **captions** → `post-content`

## Gotchas

- **Word timestamps must match the input video** — don't reuse rough-cut's words.json directly. Re-transcribe.
- **Apostrophe/contraction quirks** — WhisperX outputs words with attached punctuation ("it's", "right,"). Emphasis matching strips punctuation before comparing.
- **Font rendering** — Arial Black is the macOS default. libass uses fontconfig to find it; if Arial Black is missing, libass picks a fallback and logs a warning. Bundle a TTF in the skill folder for a Linux build later.
- **Burn-in is destructive** — captions are baked into the video, can't be turned off later. For platforms that want soft captions (YouTube), keep the `.ass` file the build emits and upload it as a separate subtitle track.
- **Long lines wider than 1080px** — libass auto-wraps at the line width set by MarginL/MarginR. A 5-word line with a long emphasis word can wrap to two visual rows; that looks fine in practice. If a single word is wider than 1080−2·marginL it'll still overflow; tighten MAX_WORDS_PER_LINE or the font size if it bites.
- **`ffmpeg-full` is keg-only** — it doesn't replace your regular `ffmpeg`. The other skills (rough-cut, audio-polish, reframe, broll) keep using the stock build. Only captions reaches for the full one.
