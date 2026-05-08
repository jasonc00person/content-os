---
name: yt-competitor-research
description: "Scans YouTube competitors serially via Chrome — orchestrator opens a fresh tab and hands the ID to a Sonnet scraper that loops every channel in that single tab, picks the top 3 long-form videos by views per channel from the most recent grid load, then visits only those 3 to capture title + description + likes + date. The orchestrator then sorts all 3 × N videos by views and writes the report directly. Triggers: youtube competitor research, yt research, what's working on youtube, youtube outliers, research yt competitors, youtube niche research."
---

# YT Competitor Research — Top 3 Long-Form Videos by Views Per Channel

The orchestrator opens a fresh Chrome tab and hands the tab ID to a Sonnet scraper. The scraper works through every competitor in sequence using that single tab. For each channel, navigate to the `/videos` grid (most-recent sorted), identify the top 3 videos by view count, and visit only those 3 to capture title + description + likes + date. The scraper closes the tab when done. The orchestrator takes the returned JSON, sorts the pooled 3 × N videos by views high-to-low across all channels, tags topic + CTA, and writes the report directly — no second subagent needed.

## How to Trigger
- "research my yt competitors" / "run yt content research"
- "what's working on youtube in my niche"
- "find yt outliers on @handle, @handle, @handle"

## Prerequisites

- **Claude in Chrome extension** installed and connected (https://claude.ai/chrome). The skill drives a real Chrome window via the `mcp__claude-in-chrome__*` tools.
- **A `competitor-list.md` file** in the project root with a `## YouTube` section listing channels via `youtube.com/@handle` URLs. The orchestrator extracts handles from that section. If the section is missing or empty, the user must name handles inline.
- **macOS launch command**: the skill uses `open -a "Google Chrome"` to launch Chrome if the extension isn't connected. On Linux/Windows, swap that for the OS-appropriate launcher.
- **A `research/` directory** at the project root. The skill creates it if missing.

## Inputs

### Competitor handles
Default: read `competitor-list.md`, find the `## YouTube` section, and extract every `@handle` from `youtube.com/@handle` URLs in that section.
Override: user can name specific handles ("research @creator_one, @creator_two, @creator_three").

---

## Architecture

```
Orchestrator (opens tab, assigns ID) → Sonnet scraper (uses assigned tab, closes it) → Orchestrator (writes report) → research/YT-Competitor-Research_YYYY-MM-DD.md
```

**Why this design:**
- **Orchestrator owns tab creation, scraper owns teardown.** Splitting lifecycle keeps the orchestrator's view of Chrome state authoritative (it can clear stale tabs cleanly before handing off) and gives the scraper a single tab handle to operate against without having to negotiate tab-group state itself.
- **One tab, foreground.** Serial avoids Chrome's background-tab throttling. Slower than parallel but bulletproof.
- **No scrolling.** YouTube's `/videos` grid renders ~30 tiles on initial load with the default sort being most-recent. View counts are visible on every grid tile, so we can pre-filter to top 3 without visiting any video pages.
- **No window resize.** Default size loads enough tiles. Larger window loads more, smaller loads similar; either way we have ≥3 without scrolling.
- **Top 3 by views, not by recency.** Every grid load is bounded to recent uploads anyway (~30 most recent), so view-sort surfaces the strongest of those without arbitrarily cutting fresh content. Cuts video visits from N×many → 3 per channel.

---

## Scraper Agent Brief

Spawn with `subagent_type: general-purpose`, `model: sonnet`. Substitute `{HANDLES_JSON}` (e.g. `["creator_one","creator_two","creator_three"]`) and `{TAB_ID}` (the tab ID the orchestrator already opened):

```
You are scraping YouTube competitor videos for content research. The orchestrator has already opened a fresh Chrome tab for you. Use that tab end-to-end, then close it before returning.

HANDLES: {HANDLES_JSON}
TAB_ID: {TAB_ID}

STEP 0 — Load Chrome tools.
Call ToolSearch with query: select:mcp__claude-in-chrome__navigate,mcp__claude-in-chrome__javascript_tool,mcp__claude-in-chrome__browser_batch,mcp__claude-in-chrome__tabs_context_mcp,mcp__claude-in-chrome__tabs_close_mcp

DO NOT create a new tab. The orchestrator already created one for you (TAB_ID above). DO NOT force-focus Chrome — no `osascript activate`, no `wmctrl -a`, nothing that yanks Chrome to the foreground.

Optionally call `tabs_context_mcp` once to confirm the tab is present, but do not create or close anything yet.

STEP 1 (per handle) — Navigate to the videos grid and grab the top 3 video URLs by views.
DO NOT scroll. DO NOT resize the window. The default browser size already loads enough tiles.

Use ONE browser_batch with 3 actions:
  1. navigate → https://www.youtube.com/@{HANDLE}/videos
  2. javascript_tool → wait 7s for hydration: `new Promise(r => setTimeout(() => r('w'), 7000))`
  3. javascript_tool → extract URLs sorted by views. YouTube has stripped most stable IDs from `/videos` tiles (no `#video-title-link`, no `#metadata-line`, no `#video-title`). Use innerText parsing on the tile, and prefer the watch-link's innerText for the title (its `aria-label` includes a trailing duration like "27 minutes"):

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
      const tiles = [...document.querySelectorAll('ytd-rich-item-renderer')];
      const videos = tiles.map(tile => {
        const watchLinks = [...tile.querySelectorAll('a[href*="/watch?v="]')];
        if (!watchLinks.length) return null;
        // Two links per tile (thumbnail + title); the longer-text one is the title link.
        const titleLink = watchLinks.reduce((best, a) => (a.innerText.trim().length > (best?.innerText.trim().length || 0) ? a : best), null);
        const url = new URL(titleLink.getAttribute('href'), location.origin).href.split('&')[0];
        const innerTitle = titleLink.innerText.trim();
        const ariaTitle = (titleLink.getAttribute('aria-label') || '').replace(/\s+\d+\s+(seconds?|minutes?|hours?)(?:,\s*\d+\s+(?:seconds?|minutes?|hours?))*\s*$/i, '').trim();
        const title = innerTitle || ariaTitle;
        const text = tile.innerText;
        const viewsMatch = text.match(/([\d.,]+\s*[KMB]?)\s+views?/i);
        const ageMatch = text.match(/(\d+\s+(?:second|minute|hour|day|week|month|year)s?\s+ago)/i);
        const viewsText = viewsMatch ? viewsMatch[1].trim() : '';
        const age = ageMatch ? ageMatch[1] : '';
        return { url, viewsText, age, views: parseViews(viewsText), title };
      }).filter(v => v && v.url);
      const top3 = [...videos].sort((a,b) => (b.views||0) - (a.views||0)).slice(0,3);
      return { videoCount: videos.length, top3 };
    })()

If `videoCount === 0`, the page didn't fully hydrate — almost always because the MCP tab is hidden/backgrounded. STOP IMMEDIATELY. Do not retry, do not move to the next handle. Close your tab and return a JSON object like `{"error": "hydration_failed", "handle": "<handle>"}` so the orchestrator can prompt the user to make the tab visible.

If `videoCount` is 1 or 2, the channel just has very few uploads — that's fine, take what's there and continue.

STEP 2 (after ALL handles' grids are scraped) — Pool all top-3 URLs from every handle, sort globally by views high-to-low, then visit each one to extract title / description / likes / date.

Visiting in global view-sorted order (not per-handle order) is intentional: highest-viewed videos first means if anything errors out partway, we still have the best content captured.

Use ONE browser_batch chaining 3 actions per video (navigate → wait 3s → extract). Total = 3 × N × 3 actions in one batch.

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

STEP 3 — Build per-handle result objects.
Combine each handle's top-3 metadata results with their views/age from STEP 1, sorted by views (highest first within the handle).

STEP 4 — Close your tab.
Call `tabs_close_mcp` on TAB_ID. Do this BEFORE returning so the user's browser is clean by the time control hands back to the orchestrator. Don't enumerate the group or close other tabs — just yours. The MCP tab group can linger; that's fine.

STEP 5 — Return the combined JSON block (no other prose). Return:

{
  "handles": [
    {
      "handle": "creator_one",
      "videos": [
        {
          "url": "https://www.youtube.com/watch?v=...",
          "title": "<full title>",
          "views": 178000,
          "viewsText": "178K views",
          "age": "2 weeks ago",
          "likes": "6.3K",
          "date": "2026-04-20",
          "description": "<full description, may include line breaks>"
        }
        // up to 3 entries per handle, sorted by views (highest first)
      ]
    },
    {
      "handle": "creator_two",
      "error": "<short reason if applicable>"
    }
  ]
}
```

---

## Report Format (you, the orchestrator, write this directly)

Take the scraper's combined JSON and write the report yourself. The pool is up to 3 × N videos (already pre-filtered to each channel's best by views from the recent grid). Sort them globally by view count high-to-low — every scraped video makes it into the report, no editorial cuts.

For each video, add:
  - **Topic tag** — Education / Journey / Hot take / Lifestyle / Behind-the-scenes / Build-in-public / Story / Tutorial
  - **CTA type** — Comment-bait / Subscribe-bait / Watch-next / Link-in-desc / DM / None
  - **Why it worked** — one line on hook archetype, format mechanic, topic angle, or engagement trigger

Add a **Pattern paragraph** at the top — 2-3 sentences on what repeats across the pool: dominant themes, hook archetypes, format mechanics, title patterns, etc. If a channel had a scrape error, omit it from the body but call it out in the Pattern line.

Write to: `<project_root>/research/YT-Competitor-Research_<DATE>.md` (computed in step 2)

Format EXACTLY:

```
# YT Competitor Research — Top Long-Form Videos

**Generated:** YYYY-MM-DD | **Channels scraped:** N | **Videos in report:** M (top 3 by views per channel)

> **Pattern:** <2-3 sentences on what's repeating across the pool — dominant themes, hook archetypes, title patterns, format mechanics. Be specific.>

---

### 1. [<TITLE>](<URL>) — @handle

`<views> views · <likes> likes` · <like%> like rate · posted <date>

**Topic:** <tag> · **CTA:** <type>

**Why it worked:** <one line>

> <full description, blockquoted. Preserve line breaks. Don't truncate.>

---

### 2. [<TITLE>](<URL>) — @handle

[same structure, repeat for every video in the pool, ordered by views high-to-low]
```

RULES:
- Format view counts human-readable (1.1M, 296K, 47.3K). Likes same.
- Like rate: likes ÷ views × 100, rounded to 1 decimal (e.g. "1.8%"). If likes is null, write "n/a like rate".
- Date: prefer the ISO date from `meta[itemprop="datePublished"]`. If only relative age available, use that.
- TITLE is the full og:title. Trim emojis only if they break the markdown link.
- Strict view-sort across the whole pool — no editorial reordering.
- No closing wrap-up. The list IS the report.

---

## Main Skill Flow (what YOU do, the orchestrator)

1. **Resolve handles.** Read `competitor-list.md` from the project root. Find the `## YouTube` section and extract every `@handle` from `youtube.com/@handle` URLs in that section (or use handles the user named inline). If the section is missing/empty and no inline handles, ask the user.
2. **Compute the output path.** Today's date in `YYYY-MM-DD` → `<project_root>/research/YT-Competitor-Research_<DATE>.md`. Create `research/` if missing. If a file already exists at that path (e.g. you ran the skill earlier today), `rm` it now so step 5 can do a clean Write.
3. **Open the Chrome tab.** Load Chrome tab tools via `ToolSearch` with query `select:mcp__claude-in-chrome__tabs_context_mcp,mcp__claude-in-chrome__tabs_create_mcp`. Then:
   - Call `tabs_context_mcp`. If it returns "No MCP tab groups found" AND Chrome isn't running (`pgrep -x "Google Chrome"` via Bash), launch Chrome (`open -a "Google Chrome"` on macOS), wait ~2s, then call `tabs_context_mcp` with `createIfEmpty: true`. If Chrome is already running but the group is empty, call `tabs_context_mcp` with `createIfEmpty: true`. If the group already exists, call `tabs_create_mcp` to add a fresh tab.
   - Capture the new tab's ID. This is `{TAB_ID}` for step 4.
   - If `tabs_context_mcp` returns "Browser extension is not connected" (or anything similar), STOP and ask the user to verify the Claude in Chrome extension is connected at https://claude.ai/chrome and that the MCP tab is visible on their screen — YouTube's grid won't hydrate reliably if the tab is hidden behind another window or in a backgrounded space. Wait for the user to confirm before retrying. Don't force-focus Chrome yourself; the user has to do this.
4. Spawn the scraper subagent (`subagent_type: general-purpose`, `model: sonnet`) with the brief above. Inject `{HANDLES_JSON}` and `{TAB_ID}`. The scraper uses the assigned tab, scrapes, then closes it before returning.
5. **Write the report yourself** using the format above and the scraper's returned JSON. One Write call to the path from step 2.
6. Report the file path back to the user.

---

## Rules of Thumb
- Single tab, single agent — no parallelism.
- **Don't force-focus Chrome.** No `osascript activate`, no `wmctrl -a`, nothing that yanks Chrome to the foreground. If the user has Chrome open behind something, leave it. Only launch Chrome when it's not already running.
- Hydration failure (grid returns 0 videos) means the MCP tab is hidden/backgrounded. Stop immediately — don't retry, don't skip to the next handle. The orchestrator asks the user to make the tab visible, then re-runs.
- 1-2 videos on a channel is legit (small/new channel) — take what's there and continue.
- NO scrolling. NO window resize. The default loads what we need.
- Lifecycle ownership: orchestrator opens the tab and assigns the ID; scraper uses that tab and closes it in STEP 4; orchestrator writes the report from the returned JSON.
- If the scraper returns a hydration error, the orchestrator stops, tells the user "the YT tab couldn't load — make sure the Claude in Chrome MCP tab is visible on your screen (not behind another window, not in a backgrounded space)" and waits for the user to confirm before retrying.
- Create `research/` if missing.
- Report contains every video scraped (up to 3 × N). No padding, no editorial cuts.
