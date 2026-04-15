---
name: ig-analytics
description: "Pulls the last 30 days of Instagram Reels data via Apify and generates a full performance report. Triggers: run ig analytics, pull my IG report, instagram analytics, IG report, how are my reels doing, reel performance, instagram stats."
---

# Instagram 30-Day Analytics Report

Pulls the last 30 days of Instagram Reels data via Apify and generates a full performance report saved to `analytics/`.

## How to Trigger
Just say: **"run ig analytics"** or **"pull my IG report"**

## Execution Steps

### Step 1 — Scrape Reels (Single API Call)
Use the `mcp__apify__apify--instagram-reel-scraper` tool with:
- `username`: `["jasoncooperson"]`
- `onlyPostsNewerThan`: 30 days ago from today (format: `YYYY-MM-DD`)
- `resultsLimit`: `100`

### Step 2 — Pull Full Data with Play Counts
Use `mcp__apify__get-actor-output` with the returned `datasetId`:
- `fields`: `url,caption,timestamp,likesCount,commentsCount,videoPlayCount,videoViewCount`
- `limit`: `100`

### Step 3 — Filter & Analyze
- **Filter out** any reels with timestamps before the 30-day cutoff (the scraper sometimes returns extras)
- Sort and rank by `videoPlayCount` (this is the plays/views metric — NOT `videoViewCount`)
- Categorize each reel as: **Conversion** (has CTA keyword/DM prompt), **Lifestyle** (personal/day-in-life), or **Motivational** (mindset/grind)

### Step 4 — Generate Report
Write a markdown report to `analytics/30-Day-Instagram-Report_YYYY-MM-DD.md` with these sections:

1. **Overview** — Total reels, avg posts/week, total plays, total likes, total comments, averages per reel
2. **Posting Consistency** — Week-by-week breakdown, longest gap, consistency grade (A/B/C/D/F based on gaps and frequency)
3. **Top 5 Reels by Plays** — Table with date, topic, plays, likes, comments, URL
4. **Top 5 Reels by Likes** — Same format
5. **Top 5 Reels by Comments** — Same format
6. **All Reels (Chronological)** — Full table with plays, likes, comments, type
7. **Key Insights** — What's working, what needs attention, 3-4 actionable recommendations

### Consistency Grading Scale
- **A** = 5+ posts/week avg, no gaps > 3 days
- **B** = 4+ posts/week avg, no gaps > 5 days
- **C** = 2-3 posts/week avg OR any gap > 7 days
- **D** = 1-2 posts/week avg OR any gap > 10 days
- **F** = < 1 post/week avg

## Important Notes
- `videoPlayCount` = plays (the primary reach metric). Always use this, NOT `videoViewCount`.
- Keep it to exactly 2 Apify calls: one scrape, one data pull. No extra calls.
- Insights should reference specific posts and numbers — no generic advice.
- Report filename always includes today's date for easy archiving.
- The report should sound like a sharp analyst, not a corporate deck. Direct, data-backed, actionable.
