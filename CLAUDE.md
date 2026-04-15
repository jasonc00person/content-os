# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Workspace Is

This is Jason Cooperson's content creation workspace for Instagram and YouTube. It contains reference materials, transcripts, analytics, and Claude skill files used to generate high-converting scripts. This is NOT a code repository -- it's a content system powered by AI.

## Creator Profile

- **Niche**: Helping beginners start coaching businesses using Instagram
- **Audience**: People who want to monetize a skill via Instagram, escape 9-5, hit first $10k/mo
- **Offer**: "The Instagram Accelerator" -- $4,000 90-day cohort program (20 spots)
- **Proof**: 173k IG followers, 9k YouTube subs, ~$10k/mo MRR, worked with notable creators (Alex Eubank, Hoku Arnold, Prasad, Cole, etc.)
- **Voice/Tone**: Casual, direct, no-BS, uses slang ("yo what up guys"), energetic, conversational. Speaks from lived experience (college dropout, started from $0). Anti-corporate, pro-shortcut, pro-AI.

## Folder Structure

| Folder | What's In It |
|--------|-------------|
| `skills/` | Claude `.skill` files -- the engines that generate scripts. IG reel writer, YT scriptwriter, YT ideator. |
| `reference/` | Strategy docs and training material -- Backbone Worksheet (ICP/offer), Instagram Deep Dive, YouTube Playbook, viral scripting methodology. |
| `transcripts/` | Raw transcripts -- Jason's YouTube content and sales call recordings. Mine these for content ideas and audience pain points. |
| `scripts/` | Generated script batches -- output from the skill files. |
| `data/` | Performance analytics -- reel metrics, what's working and what's not. |
| `partnerships/` | Sponsored/collab content and invoices (e.g., Higgsfield). |

## How the Scripting System Works

1. **Skill files** (`skills/`) are the core engines. Each is a compressed Claude skill archive containing system prompts, templates, hook libraries, and methodology:
   - `ig-reel-script-writer.skill` -- Instagram Reel scripts
   - `yt-scriptwriter.skill` -- YouTube video scripts
   - `yt-ideator.skill` -- YouTube video idea generation
2. Scripts require **context** to be effective. Always read the Backbone Worksheet (`reference/Jason Cooperson Backbone Worksheet - Updated by Claude.txt`) first -- it has the ICP, offer, backstory, and proof. Then layer in transcripts, call recordings, or performance data as needed.
3. Script structure: **Hook (0-3s) -> Content/Value -> CTA**
4. Two script categories: **viral/broad** (reach-optimized) and **conversion** (offer-optimized)
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
