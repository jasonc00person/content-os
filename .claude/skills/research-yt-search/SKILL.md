---
name: research-yt-search
description: "Explores YouTube via search bar — orchestrator opens a fresh Chrome tab and hands the ID to a Sonnet scraper that loops every search term in that single tab, picks the top 5 long-form videos by views per term from the search results page, then visits only those 5 to capture title + description + likes + date. The orchestrator then sorts all 5 × N videos by views and writes the report directly. Use this when you want to discover what's working in a niche by topic/keyword rather than by tracked competitor channel. Triggers: yt search research, youtube search research, what's trending for the keyword, explore youtube search, search-based youtube research, research yt search, youtube niche keyword research."
---

# YT Search Research — Top 5 Videos Per Search Term

The orchestrator opens a fresh Chrome tab and hands the tab ID to a Sonnet scraper. The scraper works through every search term in sequence using that single tab. For each term, navigate to YouTube search filtered to long-form videos, identify the top 5 results by view count from the visible grid, and visit only those 5 to capture title + description + likes + date. The scraper closes the tab when done. The orchestrator takes the returned JSON, sorts the pooled 5 × N videos by views high-to-low across all terms, tags topic + CTA, and writes the report directly — no second subagent needed.

## How to Trigger
- "research yt search for <terms>"
- "what's trending on youtube for <term>"
- "explore yt search around <topic>"
- "yt keyword research"

## When to Use This vs research-yt-competitors

| Use this skill | Use research-yt-competitors |
|---|---|
| You want to explore a topic/niche by keyword | You want to track specific channels you already know |
| You're looking for fresh creators you don't follow | You want week-over-week tracking of known competitors |
| You want to see how the algorithm ranks a topic | You want each channel's recent best regardless of topic |

## Prerequisites

- **Claude in Chrome extension** installed and connected (https://claude.ai/chrome). The skill drives a real Chrome window via the `mcp__claude-in-chrome__*` tools.
- **Search terms** — either supplied inline by the user, or read from `competitor-list.md`'s `## YouTube Search Terms` section. Each line in that section that starts with `- ` is treated as one search term (everything after the dash, trimmed).
- **macOS launch command**: the skill uses `open -a "Google Chrome"` to launch Chrome if the extension isn't connected. On Linux/Windows, swap that for the OS-appropriate launcher.
- **A `research/` directory** at the project root. The skill creates it if missing.

## Inputs

### Search terms
Default: read `competitor-list.md`, find the `## YouTube Search Terms` section, and extract every line starting with `- `. Each line is one term.
Override: user can name terms inline ("research yt search for 'ai automation', 'n8n agent', 'claude code agents'").

If the section is missing/empty AND no inline terms, ask the user.

---

## Architecture

```
Orchestrator (opens tab, assigns ID) → Sonnet scraper (uses assigned tab, closes it) → Orchestrator (writes report) → research/YT-Search-Research_YYYY-MM-DD.md
```

**Why this design:**
- **Same architecture as research-yt-competitors.** Orchestrator owns tab creation, scraper owns teardown. Splitting lifecycle keeps the orchestrator's view of Chrome state authoritative and gives the scraper a single tab handle to operate against.
- **One tab, foreground.** Serial avoids Chrome's background-tab throttling. Slower than parallel but bulletproof.
- **Search URL filtered to video type.** The `&sp=EgIQAQ%253D%253D` parameter filters out shorts, channels, and playlists — leaving only long-form video results. This is one of YouTube's most stable sp codes.
- **No scrolling.** Search results render ~20 tiles on initial load. View counts are visible on every tile, so we pre-filter to top 5 without extra interaction.
- **Top 5 by views per term** (vs top 3 per channel for competitor research). Search results pool is more diverse — wider net per term gives better signal.

---

## Scraper Agent Brief

Spawn with `subagent_type: general-purpose`, `model: sonnet`. Substitute `{TERMS_JSON}` (e.g. `["ai automation","n8n agent","claude code agents"]`) and `{TAB_ID}` (the tab ID the orchestrator already opened):

```
You are scraping YouTube search results for content research. The orchestrator has already opened a fresh Chrome tab for you. Use that tab end-to-end, then close it before returning.

TERMS: {TERMS_JSON}
TAB_ID: {TAB_ID}

STEP 0 — Load Chrome tools.
Call ToolSearch with query: select:mcp__claude-in-chrome__navigate,mcp__claude-in-chrome__javascript_tool,mcp__claude-in-chrome__browser_batch,mcp__claude-in-chrome__tabs_context_mcp,mcp__claude-in-chrome__tabs_close_mcp

DO NOT create a new tab. The orchestrator already created one for you (TAB_ID above). DO NOT force-focus Chrome — no `osascript activate`, no `wmctrl -a`, nothing that yanks Chrome to the foreground.

Optionally call `tabs_context_mcp` once to confirm the tab is present, but do not create or close anything yet.

STEP 1 (per term) — Navigate to the YouTube search results page filtered to videos and grab the top 5 video URLs by views.
DO NOT scroll. DO NOT resize the window. The default browser size already loads enough tiles.

URL-encode the term (spaces → `+`, special chars URL-encoded). The search URL is:
  https://www.youtube.com/results?search_query=<ENCODED_TERM>&sp=EgIQAQ%253D%253D

Use ONE browser_batch with 3 actions:
  1. navigate → search URL
  2. javascript_tool → wait 7s for hydration: `new Promise(r => setTimeout(() => r('w'), 7000))`
  3. javascript_tool → extract URLs sorted by views. YouTube search results use `ytd-video-renderer` tiles. Use innerText parsing for resilience (selectors change; innerText is stable):

    (() => {
      const parseViews = s => {
        if (!s) return null;
        if (/no views/i.test(s)) return 0;
        const m = s.match(/([\d.,]+)\s*([KMB])?/i);
        if (!m) return null;
        const num = parseFloat(m[1].replace(/,/g, ''));
        const mult = ({K:1e3, M:1e6, B:1e9}[(m[2]||'').toUpperCase()]) || 1;
        return Math.round(num * mult);
      };
      const tiles = [...document.querySelectorAll('ytd-video-renderer')];
      const videos = tiles.map(tile => {
        const watchLinks = [...tile.querySelectorAll('a[href*="/watch?v="]')];
        if (!watchLinks.length) return null;
        // Two links per tile (thumbnail + title); the longer-text one is the title link.
        const titleLink = watchLinks.reduce((best, a) => (a.innerText.trim().length > (best?.innerText.trim().length || 0) ? a : best), null);
        const url = new URL(titleLink.getAttribute('href'), location.origin).href.split('&')[0];
        const innerTitle = titleLink.innerText.trim();
        const ariaTitle = (titleLink.getAttribute('aria-label') || '').replace(/\s+\d+\s+(seconds?|minutes?|hours?)(?:,\s*\d+\s+(?:seconds?|minutes?|hours?))*\s*$/i, '').trim();
        const title = innerTitle || ariaTitle;
        const channelEl = tile.querySelector('ytd-channel-name a, .ytd-channel-name a, #channel-name a');
        const channel = channelEl?.innerText.trim() || '';
        const channelHref = channelEl?.getAttribute('href') || '';
        const text = tile.innerText;
        const viewsMatch = text.match(/([\d.,]+\s*[KMB]?)\s+views?/i);
        const ageMatch = text.match(/(\d+\s+(?:second|minute|hour|day|week|month|year)s?\s+ago)/i);
        const viewsText = viewsMatch ? viewsMatch[1].trim() : '';
        const age = ageMatch ? ageMatch[1] : '';
        return { url, viewsText, age, views: parseViews(viewsText), title, channel, channelHref };
      }).filter(v => v && v.url);
      const top5 = [...videos].sort((a,b) => (b.views||0) - (a.views||0)).slice(0,5);
      return { videoCount: videos.length, top5 };
    })()

If `videoCount === 0`, the page didn't fully hydrate — almost always because the MCP tab is hidden/backgrounded. STOP IMMEDIATELY. Do not retry, do not move to the next term. Close your tab and return a JSON object like `{"error": "hydration_failed", "term": "<term>"}` so the orchestrator can prompt the user to make the tab visible.

If `videoCount` is 1-4, the term just has few results — that's fine, take what's there and continue.

STEP 2 (after ALL terms' search pages are scraped) — Pool all top-5 URLs from every term, sort globally by views high-to-low, then visit each one to extract title / description / likes / date.

Visiting in global view-sorted order (not per-term order) is intentional: highest-viewed videos first means if anything errors out partway, we still have the best content captured.

Use ONE browser_batch chaining 3 actions per video (navigate → wait 3s → extract). Total = 3 × N × 5 actions in one batch (or fewer if some terms returned <5).

For each video:
  1. navigate → video URL
  2. javascript_tool → wait: `new Promise(r => setTimeout(() => r('w'), 3000))`
  3. javascript_tool → extract:

    (() => {
      const meta = sel => document.querySelector(sel)?.content || null;
      const title = meta('meta[property="og:title"]') || meta('meta[name="title"]') || '';
      // CRITICAL: og:description is truncated to ~160 chars AND collapses newlines into one line.
      // Use ytInitialPlayerResponse.videoDetails.shortDescription — full text with \n preserved.
      // Strip URLs to [LINK] before returning — Chrome MCP's redactor blocks tool results
      // containing URL/cookie patterns ("[BLOCKED: Cookie/query string data]"), which would
      // wipe the entire description. URL targets are noise for content research anyway.
      const rawDesc = window.ytInitialPlayerResponse?.videoDetails?.shortDescription || '';
      const description = rawDesc.replace(/https?:\/\/\S+/g, '[LINK]');
      const date = meta('meta[itemprop="datePublished"]') || meta('meta[itemprop="uploadDate"]') || null;
      const viewCount = meta('meta[itemprop="interactionCount"]') || null;
      // Likes from the like button aria-label, e.g. "like this video along with 12,345 other people"
      const likeBtn = document.querySelector('like-button-view-model button, ytd-segmented-like-dislike-button-renderer button[aria-label*="like" i], button[aria-label*="like this" i]');
      const likeAria = likeBtn?.getAttribute('aria-label') || '';
      const likeMatch = likeAria.match(/([\d.,]+[KMB]?)/i);
      const likes = likeMatch ? likeMatch[1] : null;
      return { title, description, date, viewCount, likes };
    })()

STEP 3 — Build per-term result objects.
Combine each term's top-5 metadata results with their views/age/channel from STEP 1, sorted by views (highest first within the term).

STEP 4 — Close your tab.
Call `tabs_close_mcp` on TAB_ID. Do this BEFORE returning so the user's browser is clean by the time control hands back to the orchestrator. Don't enumerate the group or close other tabs — just yours. The MCP tab group can linger; that's fine.

STEP 5 — Return the combined JSON block (no other prose). Return:

{
  "terms": [
    {
      "term": "ai automation",
      "videos": [
        {
          "url": "https://www.youtube.com/watch?v=...",
          "title": "<full title>",
          "channel": "<channel name>",
          "channelHref": "/@handle",
          "views": 1780000,
          "viewsText": "1.7M views",
          "age": "3 months ago",
          "likes": "63K",
          "date": "2026-02-04",
          "description": "<full description, may include line breaks>"
        }
        // up to 5 entries per term, sorted by views (highest first)
      ]
    },
    {
      "term": "n8n agent",
      "error": "<short reason if applicable>"
    }
  ]
}
```

---

## Report Format (you, the orchestrator, write this directly)

Take the scraper's combined JSON and write the report yourself. The pool is up to 5 × N videos (already pre-filtered to each term's best by views from the search results page). Sort them globally by view count high-to-low — every scraped video makes it into the report, no editorial cuts.

For each video, add:
  - **Topic tag** — Education / Journey / Hot take / Lifestyle / Behind-the-scenes / Build-in-public / Story / Tutorial
  - **CTA type** — Comment-bait / Subscribe-bait / Watch-next / Link-in-desc / DM / None
  - **Why it ranked** — one line on hook archetype, format mechanic, topic angle, or engagement trigger that likely got it ranked for this search

Add a **Pattern paragraph** at the top — 2-3 sentences on what repeats across the pool: dominant themes, hook archetypes, format mechanics, title patterns, channel size mix (big channels dominating vs small channels breaking through), etc. If a term had a scrape error, omit it from the body but call it out in the Pattern line.

Write to: `<project_root>/research/YT-Search-Research_<DATE>.md` (computed in step 2)

Format EXACTLY:

```
# YT Search Research — Top Videos By Search Term

**Generated:** YYYY-MM-DD | **Terms searched:** N | **Videos in report:** M (top 5 by views per term)

> **Pattern:** <2-3 sentences on what's repeating across the pool — dominant themes, hook archetypes, title patterns, format mechanics, channel-size dynamics. Be specific.>

**Search terms:** `<term 1>` · `<term 2>` · `<term 3>` …

---

### 1. [<TITLE>](<URL>) — <CHANNEL>

`<views> views · <likes> likes` · <like%> like rate · posted <date> · ranked for: `<term>`

**Topic:** <tag> · **CTA:** <type>

**Why it ranked:** <one line>

> <full description, blockquoted. Preserve line breaks. Don't truncate.>

---

### 2. [<TITLE>](<URL>) — <CHANNEL>

[same structure, repeat for every video in the pool, ordered by views high-to-low]
```

RULES:
- Format view counts human-readable (1.1M, 296K, 47.3K). Likes same.
- Like rate: likes ÷ views × 100, rounded to 1 decimal (e.g. "1.8%"). If likes is null, write "n/a like rate".
- Date: prefer the ISO date from `meta[itemprop="datePublished"]`. If only relative age available, use that.
- TITLE is the full og:title. Trim emojis only if they break the markdown link.
- "ranked for" shows which search term surfaced this video. If a video appeared in multiple terms' top-5s (deduplication), list all the terms separated by `·`.
- Strict view-sort across the whole pool — no editorial reordering.
- No closing wrap-up. The list IS the report.

**Deduplication:** If the same video URL shows up in multiple terms' top-5 results, include it once in the report (using its highest-views entry) and list all the terms that surfaced it in the "ranked for" line.

---

## Main Skill Flow (what YOU do, the orchestrator)

1. **Resolve search terms.** If the user named terms inline, use those. Otherwise read `competitor-list.md` from the project root, find the `## YouTube Search Terms` section, and extract every line starting with `- ` (term = everything after the dash, trimmed). If the section is missing/empty and no inline terms, ask the user.
2. **Compute the output path.** Today's date in `YYYY-MM-DD` → `<project_root>/research/YT-Search-Research_<DATE>.md`. Create `research/` if missing. Don't inspect or clean up prior reports — every run just writes a new report. A same-day rerun will overwrite that day's file via Write; that's fine.
3. **Open the Chrome tab.** Load Chrome tab tools via `ToolSearch` with query `select:mcp__claude-in-chrome__tabs_context_mcp,mcp__claude-in-chrome__tabs_create_mcp`. Then:
   - Call `tabs_context_mcp`. If it returns "No MCP tab groups found" AND Chrome isn't running (`pgrep -x "Google Chrome"` via Bash), launch Chrome (`open -a "Google Chrome"` on macOS), wait ~2s, then call `tabs_context_mcp` with `createIfEmpty: true`. If Chrome is already running but the group is empty, call `tabs_context_mcp` with `createIfEmpty: true`. If the group already exists, call `tabs_create_mcp` to add a fresh tab.
   - Capture the new tab's ID. This is `{TAB_ID}` for step 4.
   - If `tabs_context_mcp` returns "Browser extension is not connected" (or anything similar), STOP and ask the user to verify the Claude in Chrome extension is connected at https://claude.ai/chrome and that the MCP tab is visible on their screen — YouTube's grid won't hydrate reliably if the tab is hidden behind another window or in a backgrounded space. Wait for the user to confirm before retrying. Don't force-focus Chrome yourself; the user has to do this.
4. Spawn the scraper subagent (`subagent_type: general-purpose`, `model: sonnet`) with the brief above. Inject `{TERMS_JSON}` and `{TAB_ID}`. The scraper uses the assigned tab, scrapes, then closes it before returning.
5. **Write the report yourself** using the format above and the scraper's returned JSON. One Write call to the path from step 2. Apply deduplication: if a URL appears in multiple terms' top-5 lists, fold them into a single entry with all source terms listed in "ranked for".
6. Report the file path back to the user.

---

## Rules of Thumb
- Single tab, single agent — no parallelism.
- **Don't force-focus Chrome.** No `osascript activate`, no `wmctrl -a`, nothing that yanks Chrome to the foreground. If the user has Chrome open behind something, leave it. Only launch Chrome when it's not already running.
- Hydration failure (search returns 0 videos) means the MCP tab is hidden/backgrounded. Stop immediately — don't retry, don't skip to the next term. The orchestrator asks the user to make the tab visible, then re-runs.
- 1-4 search results is rare for a real term but legit — take what's there and continue.
- NO scrolling. NO window resize. The default loads what we need (~20 search result tiles).
- The `&sp=EgIQAQ%253D%253D` filter excludes shorts, channels, and playlists — leaves long-form videos only. If you need shorts research, use a different filter or a separate skill.
- Lifecycle ownership: orchestrator opens the tab and assigns the ID; scraper uses that tab and closes it in STEP 4; orchestrator writes the report from the returned JSON.
- If the scraper returns a hydration error, the orchestrator stops, tells the user "the YT tab couldn't load — make sure the Claude in Chrome MCP tab is visible on your screen (not behind another window, not in a backgrounded space)" and waits for the user to confirm before retrying.
- Create `research/` if missing.
- Report contains every unique video scraped (up to 5 × N, minus duplicates). No padding, no editorial cuts.
