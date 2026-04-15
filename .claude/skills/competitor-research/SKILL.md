---
name: competitor-research
description: "Scrapes competitors' Instagram reels and carousels from the past 2 weeks, finds outlier posts (2-3x+ their average), reverse-engineers why they worked, and generates content ideas tagged TOF/MOF/BOF. Triggers: content research, competitor research, what's trending, niche research, research competitors, find outliers, trending content, what's working in my niche."
---

# Content Research — Competitor Outlier Analysis

Scrape competitors' recent Instagram content (reels + carousels), find outlier posts that massively overperformed, reverse-engineer why they worked, and generate content ideas for Jason's page.

## How to Trigger
- **"run content research"** or **"research competitors"**
- **"what's trending in my niche"**
- **"find outliers"**

## Inputs

### Competitor List
Read `competitor-list.md` in the project root for the current list of handles to scrape. Each entry has the username, follower count, and notes.

### Timeframe
Default: **past 2 weeks** (14 days). User can override (e.g., "research last 30 days").

---

## Execution Steps

### Step 1 — Scrape Each Competitor

Use a TWO-SCRAPER approach to get complete data:

**For reels:** Use `mcp__apify__apify--instagram-reel-scraper` (dedicated reel scraper):
- `username`: `["{username}"]`
- `resultsLimit`: `50`
- `onlyPostsNewerThan`: 14 days ago from today (format: `YYYY-MM-DD`)
- `skipPinnedPosts`: `true` (avoids old pinned posts polluting the data)

**For carousels/images:** Use `mcp__apify__apify--instagram-scraper` (general scraper):
- `directUrls`: `["https://www.instagram.com/{username}/"]`
- `resultsType`: `posts`
- `resultsLimit`: `50`
- `onlyPostsNewerThan`: 14 days ago from today

Then **ALWAYS** pull the full dataset with `mcp__apify__get-actor-output` before doing any analysis:
- `fields`: `url,caption,timestamp,likesCount,commentsCount,videoPlayCount,videoViewCount,type,displayUrl`
- `limit`: `100`

Run each competitor as a separate scrape call.

**CRITICAL RULES:**
1. **NEVER analyze from the scraper preview.** The initial scraper response only shows a partial preview (often 1-3 items). Always call `get-actor-output` with the `datasetId` to get ALL items with ALL fields before doing any analysis. The preview often omits fields like `videoPlayCount`.
2. The general scraper often returns pinned posts from months/years ago and may miss recent posts. Always use the **dedicated reel scraper as the PRIMARY data source** — it's more reliable and supports `skipPinnedPosts`.
3. **Don't trust post count numbers from old profile scrapes** — accounts may post much more frequently than stale metadata suggests. When in doubt, scrape without a date filter and filter client-side.

### Step 2 — Calculate Baselines & Find Outliers

For each competitor:
1. **Calculate their baseline** — median plays (for reels) or median likes (for carousels/images) across all scraped posts
2. **Flag outliers** — any post with **2x+ their median** is a mild outlier, **3x+** is a strong outlier
3. Sort outliers by performance multiplier (strongest first)

**Outlier formula:**
- Reels: `videoPlayCount / median_plays` → must be ≥ 2.0x (play counts are available from `get-actor-output` — make sure you're pulling the full dataset, not relying on the scraper preview)
- Carousels/Images (no play counts): `likesCount / median_likes` → must be ≥ 2.0x
- Also flag anything with unusually high comments relative to their average (2x+ comment ratio = high engagement signal, often indicates keyword CTA posts)

### Step 3 — Reverse-Engineer Each Outlier

For every outlier post, analyze and document:

1. **Hook** — What was the first line/visual? Categorize:
   - Dream outcome ("I made $X in Y days")
   - Contrarian take ("Stop doing X")
   - Curiosity gap ("Nobody talks about this")
   - Pain point ("If you're stuck at X...")
   - Pattern interrupt (unexpected visual/statement)
   - Social proof ("How my client went from X to Y")

2. **Format** — What type of content?
   - Talking head
   - B-roll with voiceover
   - Screen recording/tutorial
   - Text overlay / kinetic text
   - Carousel (slides)
   - Lifestyle / vlog clip
   - Meme / trending audio

3. **Topic/Angle** — What's the core subject and what angle did they take?

4. **CTA** — Did they have a call to action? What kind?
   - Comment keyword
   - DM prompt
   - Link in bio
   - Follow CTA
   - No CTA (pure value/reach play)

5. **Why it worked** — 1-2 sentences on the psychology. What made this outperform? Was it the hook, the topic, the format, the timing, or a combo?

### Step 4 — Identify Trends

Look across ALL outliers from ALL competitors and identify:
- **Topic clusters** — Are multiple competitors going viral on the same topics?
- **Format trends** — Is a specific format (carousel, talking head, etc.) overrepresented in outliers?
- **Hook patterns** — What hook styles are dominating?
- **CTA patterns** — What engagement mechanics are working?

### Step 5 — Generate Content Ideas

Based on the outliers and trends, generate **10-15 content ideas** for Jason's page. Each idea should include:
- **Title/concept** — One-line description
- **Hook** — The opening line or visual
- **Angle** — How Jason would spin this for his audience (coaching beginners, IG growth, AI-powered systems)
- **Format** — Recommended format
- **Funnel tag** — TOF, MOF, or BOF:
  - **TOF** = Maximum reach. Broad appeal, trending topics, hot takes, lifestyle. Goal: new eyeballs.
  - **MOF** = Nurture. Show expertise, behind-the-scenes, client wins, process breakdowns. Goal: build trust.
  - **BOF** = Convert. Direct CTA, offer mention, pain point + solution, DM prompts. Goal: book calls.
- **Inspired by** — Which outlier(s) inspired this idea

Ideas should sound like Jason — casual, direct, no-BS. Reference his specific proof points (173k followers, AI systems, coaching results) where relevant.

Aim for a mix: ~5 TOF, ~5 MOF, ~5 BOF.

### Step 6 — Write the Report

Save to `research/Competitor-Research_YYYY-MM-DD.md` with this structure:

```markdown
# Competitor Research Report

**Period:** [start date] – [end date] | **Generated:** [today] | **Competitors:** [count]

---

## Executive Summary

[3-5 bullet points: what's trending, biggest outliers, key takeaways]

---

## Competitor Breakdown

### [@username] — [follower count]

**Baseline:** [median plays/likes] | **Posts scraped:** [count] | **Outliers found:** [count]

#### Outliers

| Post | Plays/Likes | Multiple | Hook Type | Format | CTA |
|------|------------|----------|-----------|--------|-----|
| [topic] | 50K | 3.2x | Dream outcome | Talking head | Comment "FREE" |

**[Topic]** ([multiplier]x, [plays/likes])
- **Hook:** "[first line]"
- **Format:** [format type]
- **Topic/Angle:** [description]
- **CTA:** [CTA type and details]
- **Why it worked:** [1-2 sentences]
- **URL:** [link]

[Repeat for each outlier]

[Repeat for each competitor]

---

## Trend Analysis

### Topic Clusters
[What topics are multiple competitors going viral on?]

### Format Trends
[Which formats are overrepresented in outliers?]

### Hook Patterns
[What hook styles are dominating?]

### CTA Patterns
[What engagement mechanics are working?]

---

## Content Ideas for @jasoncooperson

| # | Concept | Hook | Format | Funnel | Inspired By |
|---|---------|------|--------|--------|-------------|
| 1 | [title] | [hook] | [format] | TOF | @competitor post |

### Idea Details

**1. [Concept]** — [Funnel Tag]
- **Hook:** "[opening line]"
- **Angle:** [how Jason spins this]
- **Format:** [recommended format]
- **Inspired by:** [@competitor — "post title" (Xx outlier)]

[Repeat for each idea]

---

*Data sourced via Apify Instagram Scraper. Report generated by Claude.*
```

---

## Important Notes
- Use TWO-SCRAPER approach: dedicated reel scraper as PRIMARY (with `skipPinnedPosts`), general scraper for carousels
- Median is better than mean for baselines — one viral post shouldn't skew the average
- If a competitor has < 5 posts in the window, note it but still analyze what's there
- Don't manufacture trends — if there's no clear pattern, say so
- Ideas must sound like Jason, not like a marketing textbook
- Keep the report scannable — tables for quick overview, detail sections for deep dives
- Create the `research/` directory if it doesn't exist
