# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Workspace Is

This is Jason Cooperson's content creation workspace for Instagram and YouTube. It contains reference materials, transcripts, analytics, and Claude skill files used to generate high-converting scripts. This is NOT a code repository -- it's a content system powered by AI.

## Creator Profile

- **Niche**: AI systems implementation for established business owners + content coaching for beginners
- **Tier 1 Audience**: Business owners doing $10-40k/mo who need AI systems to scale without hiring
- **Tier 1 Offer**: AI Systems Implementation -- $6-8K 1-on-1 done-with-you Claude Code builds (setter bots, content pipelines, dashboards, CRM automation)
- **Tier 2 Audience**: Beginners who want to start a coaching business using Instagram
- **Tier 2 Offer**: "The Instagram Accelerator" -- $4,000 90-day cohort (feeder into Tier 1)
- **Proof**: 173k IG followers, 9k YouTube subs, ~$10k/mo MRR, production-grade AI systems built with Claude Code, worked with notable creators (Alex Eubank, Hoku Arnold, Prasad, Cole, etc.)
- **Voice/Tone**: Casual, direct, no-BS, uses slang ("yo what up guys"), energetic, conversational. Speaks from lived experience (college dropout, started from $0). Anti-corporate, pro-shortcut, pro-AI.
- **Full business context**: See `backbone.md` in project root

## Folder Structure

| Folder | What's In It |
|--------|-------------|
| `.claude/skills/` | Claude skill files -- scriptwriter, ig-analytics, notion-content-pipeline, competitor-research, web-research, post-content. |
| `backbone.md` | Business backbone -- ICP, offers (Tier 1 AI systems + Tier 2 coaching), proof, niche, backstory. READ THIS FIRST for any content or strategy work. |
| `voice-dna.md` | Jason's speech patterns, openers, closers, slang, energy -- extracted from top 10 reels. READ THIS before writing any script. |
| `competitor-list.md` | Competitor accounts to study (Jun Yuh, Ava, Mino Lee, SooWei Goh). |
| `viral-knowledge/` | Scripting methodology, viral frameworks, psychology tricks, hook analysis, Instagram/YouTube playbooks. |
| `research/` | Competitor research reports and web research trend reports. |
| `analytics/` | IG performance reports and reel metrics. |
| `final-scripts/` | Generated script batches and sponsored content (e.g., Higgsfield). |
| `transcripts/` | Raw transcripts -- Jason's YouTube content and sales call recordings. |

## How the Scripting System Works

1. **Skill files** (`.claude/skills/`) are the core engines. Each has a `SKILL.md` with system prompts, templates, and methodology:
   - `ig-analytics` -- 30-day Instagram performance reports
   - `notion-content-pipeline` -- Notion content database management
   - `competitor-research` -- Competitor scraping, outlier detection, trend analysis, content ideas
   - `web-research` -- Parallel web research across 6 domains, trending news, viral hook generation
   - `scriptwriter` -- Write IG Reel/YT scripts in Jason's voice with viral frameworks (fresh, ramble, batch, rewrite modes)
   - `post-content` -- Post/schedule videos to IG, YouTube, TikTok, LinkedIn, Facebook via Buffer API
2. Scripts require **context** to be effective. Always read `backbone.md` first -- it has the ICP (Tier 1 + Tier 2), offers, backstory, and proof. Then layer in transcripts, call recordings, or performance data as needed.
3. Script structure: **Hook (0-3s) -> Content/Value -> CTA**
4. Three content categories: **TOF** (broad reach, new eyeballs), **MOF** (nurture, build trust, show expertise), **BOF** (convert, CTA, sell the offer)
5. Check `data/Reel Performance Data` before writing new batches -- let the numbers inform angles and formats.

## Content Principles

- Value delivery falls into 3 categories: Documentation, Opening Someone's Eyes, Education
- Hooks must be scroll-stopping (dream outcomes, contrarian takes, curiosity gaps, pain points)
- Every piece of content ties back to the offer funnel: content -> DMs -> call booking
- Scripts must sound like Jason wrote them -- paraphrased and personalized, never robotic
- Conversion scripts should reference audience pain points (stuck under $5k/mo, don't know what to sell, overwhelmed, been burned by scammy courses)
- Don't manufacture content -- document what's already happening. Authenticity outperforms.

## Integrations

**Apify MCP** is configured for Instagram research. Three actors available:

| Actor | Use Case |
|-------|----------|
| `apify/instagram-reel-scraper` | Pull reel data (captions, transcripts, hashtags, views, likes, duration, comments). **Primary tool** for analyzing viral content in the niche. |
| `apify/instagram-profile-scraper` | Pull profile info (bio, follower count, post count, latest posts). Use for competitor analysis. |
| `apify/instagram-scraper` | General-purpose scraper for posts, profiles, hashtags, places. Use when the other two don't cover the need. |

All three are free, official Apify actors with 99%+ success rates.
