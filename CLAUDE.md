# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Workspace Is

This is Jason Cooperson's content creation workspace for Instagram and YouTube. It contains reference materials, transcripts, analytics, and Claude skill files used to generate high-converting scripts. This is NOT a code repository -- it's a content system powered by AI.

## Creator Profile

- **Niche**: Content coaching for established creators/operators who want to scale their personal brand and organic revenue
- **ICP**: Established $10-40k/mo creators (traders, Amazon FBA, ads agencies, etc.) — good at what they do, but stuck in 200-view jail, no organic revenue, over-reliant on ads, inconsistent with content, no clear brand direction
- **Core Offer**: **Creator Accelerator** -- $6,000 / 3-month cohort. Locked in on this ONE offer for the next 18 months. No flip-flopping.
- **Outcome (guaranteed)**: +$10k/mo organic revenue OR 10k followers in 90 days, or money back. +$12k CC money-back guarantee with stipulations.
- **Unique Mechanism**: AI content scraping/research method that produces weekly DFY viral content ideas. Best price-to-value in the content coaching space.
- **Deliverables**: 1-1 onboarding call, 3x/week group calls, DFY weekly content ideas, DFY editor placement. Month 1 = warmup + viral momentum, Month 2 = launch sequence ($$$), Month 3 = scaling + fulfillment systems.
- **Scarcity**: Only 10 spots per cohort (real scarcity — Jason wants to be hands-on with each client).
- **Who Jason does NOT serve**: Complete beginners, anyone under $10k/mo, anyone giving dispute-risk vibes.
- **Proof**: 173k IG followers, 9k YouTube subs, ~$15-20k/mo. Client wins: Albert, Ayden. Worked with notable creators (Alex Eubank, Prasad, Cole, Cynthia, Seth Capehart).
- **Voice/Tone**: Casual, direct, no-BS, uses slang ("yo what up guys"), energetic, conversational. Speaks from lived experience (college dropout, started from $0). Anti-corporate, pro-shortcut, pro-AI.
- **Full business context**: See `CA Backbone Apr 26 2026.md` in project root

## Folder Structure

| Folder | What's In It |
|--------|-------------|
| `.claude/skills/` | Claude skill files -- scriptwriter, ig-analytics, notion-content-pipeline, competitor-research, post-content, video-editor. |
| `video-editor/` | Video editing workspace. Drop raw clips in `inbox/<job-name>/`, final MP4s land in `outputs/<job-name>.mp4`. Intermediates (transcript, cuts) live in `/tmp/video-editor/<job>/`. |
| `CA Backbone Apr 26 2026.md` | Business backbone -- vision, ICP, Creator Accelerator offer, proof, niche, backstory. READ THIS FIRST for any content or strategy work. |
| `voice-dna.md` | Jason's speech patterns, openers, closers, slang, energy -- extracted from top 10 reels. READ THIS before writing any script. |
| `competitor-list.md` | Competitor accounts to study (Jun Yuh, Ava, Mino Lee, SooWei Goh). |
| `viral-knowledge/` | Scripting methodology, viral frameworks, psychology tricks, hook analysis, Instagram/YouTube playbooks. |
| `research/` | Competitor research reports. |
| `analytics/` | IG performance reports and reel metrics. |
| `final-scripts/` | Generated script batches and sponsored content (e.g., Higgsfield). |
| `transcripts/` | Raw transcripts -- Jason's YouTube content and sales call recordings. |

## How the Scripting System Works

1. **Skill files** (`.claude/skills/`) are the core engines. Each has a `SKILL.md` with system prompts, templates, and methodology:
   - `ig-analytics` -- 30-day Instagram performance reports
   - `notion-content-pipeline` -- Notion content database management
   - `competitor-research` -- Competitor scraping, outlier detection, trend analysis, content ideas
   - `scriptwriter` -- Write IG Reel/YT scripts in Jason's voice with viral frameworks (fresh, ramble, batch, rewrite modes)
   - `post-content` -- Post/schedule videos to IG, YouTube, TikTok, LinkedIn, Facebook via Buffer API
   - `video-editor` -- Rough-cuts short-form reels from raw clips. Transcribes with faster-whisper, word-aware silence snap, FFmpeg splice. No captions/B-roll -- just tight rough cuts.
2. Scripts require **context** to be effective. Always read `CA Backbone Apr 26 2026.md` first -- it has the ICP, Creator Accelerator offer, backstory, and proof. Then layer in transcripts, call recordings, or performance data as needed.
3. Script structure: **Hook (0-3s) -> Content/Value -> CTA**
4. Three content categories: **TOF** (broad reach, new eyeballs), **MOF** (nurture, build trust, show expertise), **BOF** (convert, CTA, sell the offer)
5. Check `data/Reel Performance Data` before writing new batches -- let the numbers inform angles and formats.

## Content Principles

- Value delivery falls into 3 categories: Documentation, Opening Someone's Eyes, Education
- Hooks must be scroll-stopping (dream outcomes, contrarian takes, curiosity gaps, pain points)
- Every piece of content ties back to the offer funnel: content -> DMs -> call booking
- Scripts must sound like Jason wrote them -- paraphrased and personalized, never robotic
- Conversion scripts should reference ICP pain points (stuck in 200-view jail, no organic revenue, ad-cost reliant, no editor, burnt out on content, no brand direction, no content strategy)
- Don't manufacture content -- document what's already happening. Authenticity outperforms.

## Integrations

**Apify MCP** is configured for Instagram research. Three actors available:

| Actor | Use Case |
|-------|----------|
| `apify/instagram-reel-scraper` | Pull reel data (captions, transcripts, hashtags, views, likes, duration, comments). **Primary tool** for analyzing viral content in the niche. |
| `apify/instagram-profile-scraper` | Pull profile info (bio, follower count, post count, latest posts). Use for competitor analysis. |
| `apify/instagram-scraper` | General-purpose scraper for posts, profiles, hashtags, places. Use when the other two don't cover the need. |

All three are free, official Apify actors with 99%+ success rates.
