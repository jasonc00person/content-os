# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Workspace Is

This is Jason Cooperson's content creation workspace for Instagram and YouTube. It contains reference materials, transcripts, analytics, and Claude skill files used to generate high-converting scripts. This is NOT a code repository -- it's a content system powered by AI.

## Creator Profile

- **Niche**: AI content systems + creator economy education. Anti-LARP, anti-gatekeep — quality online education that doesn't cost $5–50K.
- **Voice/Tone**: Casual, direct, no-BS, uses slang ("yo what up guys"), energetic, conversational. Speaks from lived experience (college dropout, started from $0). Anti-corporate, pro-shortcut, pro-AI.
- **Proof**: 173k IG · 9k YT · 173 paying Skool members · $7,410 MRR. Poppy video (~700K views, fully AI-scripted). Member wins: Albert (200 → 5–10K views in 7 weeks, 4× community growth), Ayden ($2K → $10K/mo). Worked with: Alex Eubank, Prasad, Cole, Cynthia, Seth Capehart.

### One Offer, Two Tiers (Skool — Creator Accelerator)

As of the May 3 2026 pivot: **one motion, one offer, no flip-flopping.** The old high-ticket plays (CA $6K cohort, DFY $10–15K install) are dead. Skool is the main thing now.

**TIER 1 — Standard ($75/mo until May 17 → $97/mo)** *(MAIN MONEY MAKER)*
- ICP: Anyone trying to make more, better, or more viral content — beginners through $20–100K/mo operators
- Aspirational outcome: First viral video + 10x views (NOT a guarantee)
- Deliverables: Plug n' play AI content system, 2× weekly content review calls w/ Jason, onboarding + custom AI research, all automation templates + resources, 2026 content course
- Urgency: $75 grandfathered for life until May 17, then $97/mo (the price flip IS the launch trigger)

**TIER 2 — Inner Circle ($4K/yr)** *(upsell, capacity-limited)*
- ICP: $10–40K/mo creators with PMF, stuck in 200-view jail
- Outcome: 10x views in 90 days, guaranteed (or we work for free until)
- Deliverables: 1-1 onboarding, 2× weekly Inner Circle calls, 3-month INSTALL → MONETIZE → SCALE roadmap, DFY editor placement
- Scarcity: 5 new clients/month max

**Full backbone:** `backbone/{vision,icp,offer,messaging}.md` — read these for any content/strategy work.

**Who Inner Circle does NOT serve**: Complete beginners, anyone under ~$10K/mo, dispute-risk vibes. Standard is open to beginners.

## Folder Structure

| Folder | What's In It |
|--------|-------------|
| `.claude/skills/` | Claude skill files -- scriptwriter, ig-analytics, research-ig-competitors, research-yt-competitors, research-yt-search, research-tt-search, post-content, video-editor, ideate. |
| `backbone/` | **Locked offer backbone — load these on demand for content/strategy work.** `vision.md` (mission, MRR ladder, backstory), `icp.md` (Standard + Premium ICPs, competitor breakdown, USP), `offer.md` (offer stack, pricing, deliverables), `messaging.md` (headlines, 5 belief shifts, proof bank, anti-LARP positioning). |
| `video-editor/` | Video editing workspace. Drop raw clips in `inbox/<job-name>/`, final MP4s land in `outputs/<job-name>.mp4`. Intermediates (transcript, cuts) live in `/tmp/video-editor/<job>/`. |
| `voice-dna.md` | Jason's speech patterns, openers, closers, slang, energy -- extracted from top 10 reels. READ THIS before writing any script. |
| `notion-pipeline.md` | Live schema for the Notion content database (DB ID, properties, status flow, write shapes). Skills that read/write the pipeline load this for IDs and shapes. |
| `competitor-list.md` | Competitor accounts to study (Jun Yuh, Ava, Mino Lee, SooWei Goh). |
| `viral-knowledge/` | Scripting methodology, viral frameworks, psychology tricks, hook analysis, Instagram/YouTube playbooks. |
| `research/` | Competitor research reports. |
| `analytics/` | IG performance reports and reel metrics. |
| `final-scripts/` | Generated script batches and sponsored content (e.g., Higgsfield). |
| `transcripts/` | Raw transcripts -- Jason's YouTube content and sales call recordings. |

## How the Scripting System Works

1. **Skill files** (`.claude/skills/`) are the core engines. Each has a `SKILL.md` with system prompts, templates, and methodology:
   - `ig-analytics` -- 30-day Instagram performance reports
   - `research-ig-competitors` -- IG competitor scraping, outlier detection, trend analysis
   - `research-yt-competitors` -- YouTube competitor scraping (long-form), top-3 by views per channel
   - `research-yt-search` -- YouTube keyword/niche exploration via search bar, top-5 by views per search term
   - `research-tt-search` -- TikTok keyword/niche exploration via search bar, every visible card per term, deduplicated and pooled
   - `scriptwriter` -- Write IG Reel/YT scripts in Jason's voice with viral frameworks (fresh, ramble, batch, rewrite modes)
   - `post-content` -- Post/schedule videos to IG, YouTube, TikTok, LinkedIn, Facebook via Buffer API
   - `video-editor` -- Rough-cuts short-form reels from raw clips. Transcribes with faster-whisper, word-aware silence snap, FFmpeg splice. No captions/B-roll -- just tight rough cuts.
   - `ideate` -- 30-min timed ideation block. Picks platform + goal, opens a self-hosted visual countdown timer in Chrome, probes backbone for original angles, scans Notion saved Ideas, falls back to competitor research, drops N packaged ideas into Notion ready for scriptwriter.
2. Scripts require **context** to be effective. Load the relevant backbone files on demand:
   - **Default for any script:** `backbone/icp.md` + `backbone/messaging.md` (audience + how we talk about it)
   - **Pricing / offer mechanics:** `backbone/offer.md`
   - **Strategic / mission-driven content:** `backbone/vision.md`
   - Layer in transcripts, call recordings, or performance data as needed.
3. Script structure: **Hook (0-3s) -> Content/Value -> CTA**
4. Three content categories: **TOF** (broad reach, new eyeballs), **MOF** (nurture, build trust, show expertise), **BOF** (convert, CTA, sell the offer)
5. Check `analytics/` reports before writing new batches -- let the numbers inform angles and formats.

## Content Principles

- Value delivery falls into 3 categories: Documentation, Opening Someone's Eyes, Education
- Hooks must be scroll-stopping (dream outcomes, contrarian takes, curiosity gaps, pain points)
- Every piece of content ties back to the offer funnel: content → Skool join (Standard) or DM / Inner Circle apply (Premium)
- Scripts must sound like Jason wrote them -- paraphrased and personalized, never robotic
- Every piece should reinforce at least one of the 5 belief shifts in `backbone/messaging.md`
- Don't manufacture content -- document what's already happening. Authenticity outperforms.

## Research

**All competitor/niche research runs through the research skills in `.claude/skills/`.** No exceptions — no Apify, no third-party scrapers, no ad-hoc API calls.

| Skill | Use For |
|-------|---------|
| `research-ig-competitors` | Instagram — scrape named handles, top 3 reels each by views |
| `research-yt-competitors` | YouTube — scrape named channels, top 3 long-form each by views |
| `research-yt-search` | YouTube — keyword/niche exploration via search bar |
| `research-tt-search` | TikTok — keyword/niche exploration via search bar |

If a request needs research data, invoke the matching skill. Reports land in `research/` as `*-Research_YYYY-MM-DD.md` and are never deleted.
