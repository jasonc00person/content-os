# CLAUDE.md

Jason Cooperson's content workspace for Instagram and YouTube. Not a code repo — a content system where Claude IS the application. Each step of the pipeline runs through a skill in `.claude/skills/`.

## Creator Profile

- **Niche:** AI content systems + creator economy education. Anti-LARP, anti-gatekeep — quality online education that doesn't cost $5–50K.
- **Voice/Tone:** Casual, direct, no-BS, slang-heavy, energetic. College-dropout, started from $0. Anti-corporate, pro-shortcut, pro-AI.
- **Proof:** 173k IG · 9k YT · 173 paying Skool members · $7,410 MRR. Poppy video (~700K views, fully AI-scripted). Member wins: Albert (200 → 5–10K views in 7 weeks), Ayden ($2K → $10K/mo).

### Offer (Skool — Creator Accelerator)

One motion, one offer (May 3 2026 pivot). No more $6K cohorts or $10–15K DFY installs.

- **Standard ($75/mo until May 17 → $97/mo)** — main money maker. Plug-n-play AI content system, 2× weekly review calls, custom AI research, 2026 course. Open to anyone trying to make better/more viral content.
- **Inner Circle ($4K/yr)** — capacity-limited upsell (5/mo). For $10–40K/mo creators stuck in 200-view jail. 10x views in 90 days, guaranteed. Does NOT serve beginners or anyone under ~$10K/mo.

Full backbone: `backbone/{vision,icp,offer,messaging}.md` — load on demand.

## Content Pipeline

The whole system is one linear flow. Each step has a dedicated skill (or is Jason's job):

| Step | Skill | What It Does |
|------|-------|--------------|
| 1. Research | `research-ig-competitors`, `research-yt-competitors`, `research-yt-search` | Scrape competitors / niche searches, output ranked report to `research/` |
| 2. Ideation | `ideate` | Pulls research, runs pick-loop with Jason, hands picks to scriptwriter |
| 3. Scripting | `scriptwriter` | Owns the twist conversation, transcription, and Notion write. All scripting expertise lives here. |
| 4. Filming | _(Jason)_ | Records on camera from the beat sheet |
| 5. Rough Cut | `rough-cut` | Transcribes raw clips (WhisperX), kills filler/dead air, stitches tight rough cut inside `video-editor/projects/<job>/outputs/` |
| 6. Audio Polish | `audio-polish` | FFmpeg denoise + loudnorm to -14 LUFS. Optional music bed with sidechain duck. |
| 7. Reframe | `reframe` | 16:9 → 9:16 with MediaPipe face tracking. Auto-skips if already vertical. |
| 8. B-Roll | `broll` | Generative cinematic inserts via Higgsfield. Claude proposes prompts, you approve, skill submits + overlays. |
| 9. Captions | `captions` | Word-grouped burn-in with style presets. libass/ffmpeg-full renders and burns captions. |
| 10. Thumbnail | `thumbnail` | Generates YouTube thumbnail concepts via Higgsfield Nano Banana Pro and optional title overlays. |
| 11. Carousel | `carousel-generator` | Turns trends/news/posts into polished Instagram carousel PNGs + caption package. |
| 12. Posting | `post-content` | Posts/schedules a provided video directly through Buffer |

Helper: `transcribe-url` — pulls a transcript from any video URL when needed (not part of the main pipeline).
Helper: `carousel-generator` — can also run standalone for trend/news carousels outside the video pipeline.

## Folder Structure

| Folder | What's In It |
|--------|--------------|
| `.claude/skills/` | The pipeline skills above |
| `backbone/` | Locked offer backbone — `vision.md`, `icp.md`, `offer.md`, `messaging.md`. Load on demand. |
| `viral-knowledge/` | Scripting methodology, viral frameworks, hook analysis, IG/YT playbooks. Used by `scriptwriter`. |
| `voice-dna.md` | Jason's speech patterns, openers, closers, slang. Used by `scriptwriter`. |
| `notion-pipeline.md` | Live schema for the Notion content database (DB ID, properties, status flow). Skills load this for IDs/shapes. |
| `competitor-list.md` | Tracked competitor handles/channels. |
| `knowledge/` | Compiled repo memory. Start here for strategy, ideation, scripting, and research synthesis before opening long raw sources. Derived from `research/`, `transcripts/`, `backbone/`, `viral-knowledge/`, and skill learnings. |
| `research/` | Research reports. `*-Research_YYYY-MM-DD.md`. Never deleted. |
| `transcripts/` | Raw transcripts (Jason's content, sales calls, URL transcripts in `transcripts/url/`). |
| `video-editor/` | Video workspace. One folder per content piece in `projects/<job>/`; raw clips in `raw/`, audio/music in `audio/`, source assets in `assets/`, B-roll in `broll/`, thumbnails in `thumbnails/`, finals in `outputs/`. Intermediates stay in `/tmp/video-editor/<job>/`. |
| `carousel/outputs/` | Rendered Instagram carousel slides, contact sheets, and captions. |

## Rules

- **Research is research-skills only.** No Apify, no third-party scrapers, no ad-hoc API calls. If a request needs research data, invoke the matching `research-*` skill.
- **Use `knowledge/` first for synthesis.** It is the fast compiled layer for strategy/ideation/script context. Verify important claims against source files; do not treat `knowledge/` as authoritative.
- **Refresh compiled memory when signal changes.** After high-signal research/transcripts or major positioning changes, run `knowledge-compile` to update only the affected `knowledge/` pages.
- **Scripting expertise lives in `scriptwriter`.** Don't write scripts inline in chat or improvise hook/structure rules from memory — invoke the skill.
- **Every piece of content ties back to the offer funnel** — Skool join (Standard) or DM / Inner Circle apply (Premium). The skills handle this; just don't drop CTAs by accident.
- **Document, don't manufacture.** Authenticity outperforms.
