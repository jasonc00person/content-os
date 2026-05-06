---
name: competitor-research
description: "Scans Instagram competitors serially via Chrome — one Sonnet agent loops through every account in a single tab, picks the top 3 reels by views per handle (excluding pinned), then visits only those 3 to capture caption + engagement + date. A second Sonnet agent ranks all 3 × N reels by views and writes the report. Triggers: content research, competitor research, what's trending, niche research, research competitors, find outliers, trending content, what's working in my niche."
---

# Competitor Research — Top 3 by Views Per Handle

One Sonnet agent works through every competitor in sequence using a single Chrome tab. For each account, navigate to the reels grid, filter pinned posts via aria-label, identify the top 3 non-pinned reels by view count, and visit only those 3 to capture caption + engagement + date. A second Sonnet agent takes the pooled 3 × N reels, sorts them by views high-to-low across all accounts, and formats the report.

## How to Trigger
- "research competitors" / "run content research"
- "what's trending in my niche"
- "find outliers on @handle, @handle, @handle"

## Prerequisites

- **Claude in Chrome extension** installed and connected (https://claude.ai/chrome). The skill drives a real Chrome window via the `mcp__claude-in-chrome__*` tools.
- **A `competitor-list.md` file** in the project root listing IG handles to scrape (any format that lists `@handle` or `instagram.com/handle/`). The orchestrator just needs to extract handles from it. If the file is missing, the user must name handles inline.
- **macOS launch command**: the skill uses `open -a "Google Chrome"` to launch Chrome if the extension isn't connected. On Linux/Windows, swap that for the OS-appropriate launcher.
- **A `research/` directory** at the project root. The skill creates it if missing.

## Inputs

### Competitor handles
Default: read `competitor-list.md` and use every account listed.
Override: user can name specific handles ("research creator_one, creator_two, creator_three").

---

## Architecture

```
Sonnet scraper (one tab, serial loop) → Sonnet synthesizer → research/Competitor-Research_YYYY-MM-DD.md
```

**Why this design:**
- **One tab, foreground.** Serial avoids Chrome's background-tab throttling and IG's anti-bot quirks (intersection observers don't fire on hidden tabs, IG soft-blocks parallel sessions). Slower than parallel but bulletproof.
- **No scrolling.** IG's reels grid renders ~12 thumbnails on initial load — typically 3 pinned + 9 non-pinned. View counts are visible on every grid thumbnail, so we can pre-filter to top 3 without visiting any reel pages.
- **No window resize.** Default size loads enough thumbnails. Larger window loads more, smaller loads the same; either way we have ≥3 non-pinned without scrolling.
- **Top 3 by views, not by recency.** Every grid load is bounded to recent posts anyway (~9 most recent non-pinned), so view-sort surfaces the strongest of those without arbitrarily cutting fresh content. Cuts reel visits from 7 → 3 per handle (~57% faster than a "newest 7" approach).
- **Sonnet end-to-end.** Both scraping and synthesis are mechanical (navigate → extract for the first; sort + format + light tagging for the second). With every reel making it into the report and view-sort doing the ranking, there's no editorial picking left for a larger model to add value on.

---

## Scraper Agent Brief

Spawn with `subagent_type: general-purpose`, `model: sonnet`. Substitute `{TAB_ID}` and `{HANDLES_JSON}` (e.g. `["creator_one","creator_two","creator_three"]`) and `{OUTPUT_PATH}` (the absolute path the synthesizer should write to — see Main Skill Flow):

```
You are scraping Instagram competitor reels for content research. You have ONE tab and a list of handles. Loop through every handle serially in that tab. Return one combined JSON.

ASSIGNED TAB: {TAB_ID}
HANDLES: {HANDLES_JSON}

STEP 0 — Load Chrome tools.
Call ToolSearch with query: select:mcp__claude-in-chrome__navigate,mcp__claude-in-chrome__javascript_tool,mcp__claude-in-chrome__browser_batch,mcp__claude-in-chrome__tabs_close_mcp

STEP 1 (per handle) — Navigate to the reels grid and grab the top 3 non-pinned URLs by views.
DO NOT scroll. DO NOT resize the window. The default browser size already loads enough thumbnails.

Use ONE browser_batch with 3 actions:
  1. navigate → https://www.instagram.com/{HANDLE}/reels/
  2. javascript_tool → wait 8s for hydration: `new Promise(r => setTimeout(() => r('w'), 8000))`
  3. javascript_tool → extract URLs sorted by views:

    (() => {
      const parseViews = s => {
        const m = s.match(/(\d+(?:\.\d+)?)([KMB])/i);
        return m ? parseFloat(m[1]) * ({K:1e3, M:1e6, B:1e9}[m[2].toUpperCase()]) : (parseInt(s.replace(/,/g,''), 10) || null);
      };
      const all = [...document.querySelectorAll('a[href*="/reel/"]')];
      const isPinned = a => !!a.querySelector('svg[aria-label="Pinned post icon"]');
      const nonPinned = all.filter(a => !isPinned(a)).map(a => ({ url: a.href, views: parseViews(a.innerText.trim()) }));
      const top3 = [...nonPinned].sort((a,b) => (b.views||0) - (a.views||0)).slice(0,3);
      return { nonPinnedCount: nonPinned.length, top3 };
    })()

If `nonPinnedCount < 3`, the page didn't fully hydrate. Re-navigate, wait 8s, retry once. If still <3, record an error for this handle and move to the next.

CRITICAL: the pinned detection uses `svg[aria-label="Pinned post icon"]`. Do NOT use any innerText regex like `/Nx/` — that prefix only appears when a reel is hovered or in interactive state, so it's unreliable. The aria-label is the only stable signal.

STEP 2 (after ALL handles' grids are scraped) — Pool all 3 × N URLs from every handle, sort globally by views high-to-low, then visit each one to extract caption / likes / comments / date.

Visiting in global view-sorted order (not per-handle order) is intentional: highest-viewed reels first means if anything errors out partway, we still have the best content captured.

Use ONE browser_batch chaining 3 actions per reel (navigate → wait 2.5s → extract). Total = 3 × N × 3 actions in one batch.

For each reel:
  1. navigate → reel URL
  2. javascript_tool → wait: `new Promise(r => setTimeout(() => r('w'), 2500))`
  3. javascript_tool → extract:

    (() => {
      const t = document.querySelector('meta[property="og:title"]')?.content || '';
      const d = document.querySelector('meta[property="og:description"]')?.content || '';
      const c = t.match(/: "([\s\S]*)"$/);
      return {
        caption: c ? c[1] : t,
        likes: d.match(/([\d.,]+[KMB]?)\s+likes?/i)?.[1] || null,
        comments: d.match(/([\d.,]+[KMB]?)\s+comments?/i)?.[1] || null,
        date: d.match(/on\s+([A-Z][a-z]+\s+\d{1,2},\s+\d{4})/)?.[1] || null
      };
    })()

STEP 3 — Build per-handle result objects.
Combine each handle's 3 metadata results with their views from STEP 1, sorted by views (highest first within the handle).

STEP 4 — Close the assigned tab via `tabs_close_mcp` with `tabId: {TAB_ID}`. Do this BEFORE returning the JSON — your job owns the browser lifecycle for this run.

After the tab is closed, RETURN ONE combined JSON block (no other prose):

{
  "handles": [
    {
      "handle": "creator_one",
      "reels": [
        {
          "url": "https://www.instagram.com/creator_one/reel/.../",
          "views": 178000,
          "likes": "6,338",
          "comments": "94",
          "date": "April 20, 2026",
          "caption": "<full caption>",
          "hook": "<first line of caption, trimmed, max 120 chars>"
        }
        // 3 entries per handle, sorted by views (highest first)
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

## Synthesizer Brief

Spawn with `subagent_type: general-purpose`, `model: sonnet`. Substitute `{OUTPUT_PATH}` (the absolute path computed by the orchestrator, e.g. `<project_root>/research/Competitor-Research_YYYY-MM-DD.md`):

```
You are formatting a competitor research report from a multi-account pool of top-performing reels.

DATA — top 3 reels by views per competitor (raw scrape):

<paste the scraper's combined JSON here>

YOUR JOB:
The pool is 3 × N reels (already pre-filtered to each handle's best by views). Sort them globally by view count high-to-low and write the report. No editorial picking — every scraped reel makes it into the report.

For each reel, add:
  - **Topic tag** — Education / Journey / Hot take / Lifestyle / Behind-the-scenes / Build-in-public / Story / Tutorial
  - **CTA type** — Comment-bait / Follow-bait / Save-bait / DM / None
  - **Why it worked** — one line on hook archetype, format mechanic, topic angle, or engagement trigger
  - **Pattern paragraph** at the top — 2-3 sentences on what repeats across the pool: dominant themes, hook archetypes, format mechanics, comment-keyword games, etc.

If a handle had a scrape error, omit it from the body but call it out in the Pattern line.

OUTPUT — write to: {OUTPUT_PATH}

Format EXACTLY:

# Competitor Research — Top Reels

**Generated:** YYYY-MM-DD | **Accounts scraped:** N | **Reels in report:** M (top 3 by views per handle)

> **Pattern:** <2-3 sentences on what's repeating across the pool — dominant themes, hook archetypes, format mechanics, comment-keyword games. Be specific.>

---

### 1. [<HOOK — first line of caption>](<URL>) — @handle

`<views> views · <likes> likes · <comments> comments` · <like%> like rate · <comment%> comment rate · posted <date>

**Topic:** <tag> · **CTA:** <type>

**Why it worked:** <one line>

> <full caption, blockquoted. Preserve line breaks. Don't truncate.>

---

### 2. [<HOOK>](<URL>) — @handle

[same structure, repeat for every reel in the pool, ordered by views high-to-low]

---

RULES:
- Format view counts human-readable (1.1M, 296K, 47.3K). Likes/comments same.
- Engagement rates: likes ÷ views × 100, rounded to 1 decimal (e.g. "1.8%"). Comments same.
- HOOK is the first line of the caption. Trim emojis only if they break the markdown link.
- Strict view-sort across the whole pool — no editorial reordering.
- No closing wrap-up. The list IS the report.

After saving, return the file path.
```

---

## Main Skill Flow (what YOU do, the orchestrator)

1. **Resolve handles.** Read `competitor-list.md` from the project root and extract every handle listed (or use handles the user named inline). If both are missing, ask the user.
2. **Compute the output path.** Today's date in `YYYY-MM-DD` → `<project_root>/research/Competitor-Research_<DATE>.md`. Create `research/` if missing.
3. **Allocate exactly ONE tab:**
   - Load `tabs_context_mcp`, `tabs_create_mcp`, `tabs_close_mcp` via ToolSearch.
   - Call `tabs_context_mcp`. If extension isn't connected, launch Chrome (`open -a "Google Chrome"` on macOS; OS equivalent elsewhere), then call `tabs_context_mcp` with `createIfEmpty: true`.
   - Claim one tab. Close any other MCP tabs so the final state is exactly 1 tab.
4. Spawn the scraper subagent (`subagent_type: general-purpose`, `model: sonnet`) with the brief above. Inject `{TAB_ID}` and `{HANDLES_JSON}`. The scraper closes its own tab as its final step before returning the JSON.
5. When the scraper returns, spawn the synthesizer subagent (`subagent_type: general-purpose`, `model: sonnet`) with the JSON + brief above. Inject `{OUTPUT_PATH}` from step 2. The synthesizer never touches the browser.
6. Report the file path back to the user.

---

## Rules of Thumb
- Single tab, single agent — no parallelism. Foreground render is the whole point.
- **Keep the Chrome tab visible.** IG throttles hidden tabs and grids fail to hydrate. If a grid returns empty, check the tab isn't backgrounded before assuming a real failure.
- NO scrolling. NO window resize. The default loads what we need.
- Pinned detection is `svg[aria-label="Pinned post icon"]` — never the innerText regex.
- Scraper closes its own tab before returning. Synthesizer never sees the browser.
- If the scraper errors out on one handle, it should record the error and continue. Synthesizer works with what made it through.
- Create `research/` if missing.
- Report contains every reel scraped (3 × N). No padding, no editorial cuts.
