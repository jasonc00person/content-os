---
name: research-ig-competitors
description: "Scans Instagram competitors serially via Chrome — orchestrator opens a fresh tab and hands the ID to a Sonnet scraper that loops every account in that single tab, picks the top 3 reels by views per handle (excluding pinned), then visits only those 3 to capture caption + engagement + date. The orchestrator then sorts all 3 × N reels by views and writes the report directly. Triggers: content research, competitor research, what's trending, niche research, research competitors, find outliers, trending content, what's working in my niche."
---

# IG Competitor Research — Top 3 by Views Per Handle

## Codex / Local Runner

Prefer the local headed Playwright runner when available:

```bash
npm run research:ig
```

It opens a visible logged-out Chrome session, reads public Reels grid DOM for view counts, skips pinned posts, visits the top 3 Reels per handle, and writes `research/IG-Competitor-Research_YYYY-MM-DD.md`.

Do not ask the user to log into Instagram. The workflow is designed to run against public logged-out pages. By default it uses an ephemeral browser session and does not preserve cookies or create `.cache/ig-research-chrome`.

Useful flags:

```bash
npm run research:ig -- nick_saraev minolee.mp4 chase.h.ai
npm run research:ig -- --all
npm run research:ig -- --handles 5 --top 3 --scan 12
npm run research:ig -- --profile-dir /tmp/ig-research-debug
```

Use `--profile-dir` only for debugging a browser run. It is not required for login/session reuse.

Use the Claude-in-Chrome MCP flow below only when specifically running in Claude Code with those MCP tools connected.

The orchestrator opens a fresh Chrome tab and hands the tab ID to a Sonnet scraper. The scraper works through every competitor in sequence using that single tab. For each account, navigate to the reels grid, filter pinned posts via aria-label, identify the top 3 non-pinned reels by view count, and visit only those 3 to capture caption + engagement + date. The scraper closes the tab when done. The orchestrator takes the returned JSON, sorts the pooled 3 × N reels by views high-to-low across all accounts, tags topic + CTA, and writes the report directly — no second subagent needed.

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
Default: read `competitor-list.md`, find the `## Instagram` section, extract handles from `instagram.com/handle/` URLs, and use the **first 3 listed** (top of the list = highest priority). Don't ask — just take the top 3.
Override: user can name specific handles inline ("research creator_one, creator_two, creator_three") or say "all" to scrape every account listed.

---

## Architecture

```
Orchestrator (opens tab, assigns ID) → Sonnet scraper (uses assigned tab, closes it) → Orchestrator (writes report) → research/IG-Competitor-Research_YYYY-MM-DD.md
```

**Why this design:**
- **Orchestrator owns tab creation, scraper owns teardown.** Splitting lifecycle keeps the orchestrator's view of Chrome state authoritative (it can clear stale tabs cleanly before handing off) and gives the scraper a single tab handle to operate against without having to negotiate tab-group state itself.
- **One tab, foreground.** Serial avoids Chrome's background-tab throttling and IG's anti-bot quirks (intersection observers don't fire on hidden tabs, IG soft-blocks parallel sessions). Slower than parallel but bulletproof.
- **No scrolling.** IG's reels grid renders ~12 thumbnails on initial load — typically 3 pinned + 9 non-pinned. View counts are visible on every grid thumbnail, so we can pre-filter to top 3 without visiting any reel pages.
- **No window resize.** Default size loads enough thumbnails. Larger window loads more, smaller loads the same; either way we have ≥3 non-pinned without scrolling.
- **Top 3 by views, not by recency.** Every grid load is bounded to recent posts anyway (~9 most recent non-pinned), so view-sort surfaces the strongest of those without arbitrarily cutting fresh content. Cuts reel visits from 7 → 3 per handle (~57% faster than a "newest 7" approach).

---

## Scraper Agent Brief

> **🚨 MANDATORY: pass `model: "sonnet"` on the Agent call.** Without it the scraper inherits the orchestrator's model (often Opus) and burns ~10× the budget for no quality gain. The scrape is a long, mechanical browser loop — Sonnet handles it fine.

Spawn with `subagent_type: general-purpose`, `model: "sonnet"`. Substitute `{HANDLES_JSON}` (e.g. `["creator_one","creator_two","creator_three"]`) and `{TAB_ID}` (the tab ID the orchestrator already opened):

```
You are scraping Instagram competitor reels for content research. The orchestrator has already opened a fresh Chrome tab for you. Use that tab end-to-end, then close it before returning.

HANDLES: {HANDLES_JSON}
TAB_ID: {TAB_ID}

STEP 0 — Load Chrome tools.
Call ToolSearch with query: select:mcp__claude-in-chrome__navigate,mcp__claude-in-chrome__javascript_tool,mcp__claude-in-chrome__browser_batch,mcp__claude-in-chrome__tabs_context_mcp,mcp__claude-in-chrome__tabs_close_mcp

DO NOT create a new tab. The orchestrator already created one for you (TAB_ID above). DO NOT force-focus Chrome — no `osascript activate`, no `wmctrl -a`, nothing that yanks Chrome to the foreground.

Optionally call `tabs_context_mcp` once to confirm the tab is present, but do not create or close anything yet.

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

If `nonPinnedCount < 3`, the page didn't fully hydrate — almost always because the MCP tab is hidden/backgrounded. STOP IMMEDIATELY. Do not retry, do not move to the next handle. Close your tab and return a JSON object like `{"error": "hydration_failed", "handle": "<handle>"}` so the orchestrator can prompt the user to make the tab visible.

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

STEP 4 — Close your tab.
Call `tabs_close_mcp` on TAB_ID. Do this BEFORE returning so the user's browser is clean by the time control hands back to the orchestrator. Don't enumerate the group or close other tabs — just yours. The MCP tab group can linger; that's fine.

STEP 5 — Return the combined JSON block (no other prose). Return:

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

## Report Format (you, the orchestrator, write this directly)

Take the scraper's combined JSON and write the report yourself. The pool is 3 × N reels (already pre-filtered to each handle's best by views). Sort them globally by view count high-to-low — every scraped reel makes it into the report, no editorial cuts.

For each reel, add:
  - **Topic tag** — Education / Journey / Hot take / Lifestyle / Behind-the-scenes / Build-in-public / Story / Tutorial
  - **CTA type** — Comment-bait / Follow-bait / Save-bait / DM / None
  - **Why it worked** — one line on hook archetype, format mechanic, topic angle, or engagement trigger

Add a **Pattern paragraph** at the top — 2-3 sentences on what repeats across the pool: dominant themes, hook archetypes, format mechanics, comment-keyword games, etc. If a handle had a scrape error, omit it from the body but call it out in the Pattern line.

Write to: `<project_root>/research/IG-Competitor-Research_<DATE>.md` (computed in step 2)

Format EXACTLY:

```
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
```

RULES:
- Format view counts human-readable (1.1M, 296K, 47.3K). Likes/comments same.
- Engagement rates: likes ÷ views × 100, rounded to 1 decimal (e.g. "1.8%"). Comments same.
- HOOK is the first line of the caption. Trim emojis only if they break the markdown link.
- Strict view-sort across the whole pool — no editorial reordering.
- No closing wrap-up. The list IS the report.

---

## Main Skill Flow (what YOU do, the orchestrator)

1. **Resolve handles.** Read `competitor-list.md` from the project root, find the `## Instagram` section, extract handles from `instagram.com/handle/` URLs, and **default to the first 3** (top of the list = highest priority — don't ask). If the user named specific handles inline, use those. If the user explicitly said "all", use every handle in the section. If the section is missing/empty and no inline handles, ask the user.
2. **Compute the output path.** Today's date in `YYYY-MM-DD` → `<project_root>/research/IG-Competitor-Research_<DATE>.md`. Create `research/` if missing. Don't inspect or clean up prior reports — every run just writes a new report. A same-day rerun will overwrite that day's file via Write; that's fine.
3. **Open the Chrome tab.** Load Chrome tab tools via `ToolSearch` with query `select:mcp__claude-in-chrome__tabs_context_mcp,mcp__claude-in-chrome__tabs_create_mcp`. Then:
   - Call `tabs_context_mcp`. If it returns "No MCP tab groups found" AND Chrome isn't running (`pgrep -x "Google Chrome"` via Bash), launch Chrome (`open -a "Google Chrome"` on macOS), wait ~2s, then call `tabs_context_mcp` with `createIfEmpty: true`. If Chrome is already running but the group is empty, call `tabs_context_mcp` with `createIfEmpty: true`. If the group already exists, call `tabs_create_mcp` to add a fresh tab.
   - Capture the new tab's ID. This is `{TAB_ID}` for step 4.
   - If `tabs_context_mcp` returns "Browser extension is not connected" (or anything similar), STOP and ask the user to verify the Claude in Chrome extension is connected at https://claude.ai/chrome and that the MCP tab is visible on their screen — IG won't hydrate reliably if the tab is hidden behind another window or in a backgrounded space. Wait for the user to confirm before retrying. Don't force-focus Chrome yourself; the user has to do this.
4. Spawn the scraper subagent with the brief above. Inject `{HANDLES_JSON}` and `{TAB_ID}`. The scraper uses the assigned tab, scrapes, then closes it before returning.
   - **🚨 MANDATORY Agent call params:** `subagent_type: "general-purpose"` AND `model: "sonnet"`. The `model` param is NOT optional — omitting it inherits the orchestrator's model (often Opus) and burns ~10× the budget. Sonnet handles the scrape fine; this is a mechanical browser loop, not a reasoning task.
5. **Write the report yourself** using the format above and the scraper's returned JSON. One Write call to the path from step 2.
6. Report the file path back to the user.

---

## Rules of Thumb
- Single tab, single agent — no parallelism.
- **Don't force-focus Chrome.** No `osascript activate`, no `wmctrl -a`, nothing that yanks Chrome to the foreground. If the user has Chrome open behind something, leave it. Only launch Chrome when it's not already running.
- Hydration failure (grid returns <3 non-pinned reels) means the MCP tab is hidden/backgrounded. Stop immediately — don't retry, don't skip to the next handle. The orchestrator asks the user to make the tab visible, then re-runs.
- NO scrolling. NO window resize. The default loads what we need.
- Pinned detection is `svg[aria-label="Pinned post icon"]` — never the innerText regex.
- Lifecycle ownership: orchestrator opens the tab and assigns the ID; scraper uses that tab and closes it in STEP 4; orchestrator writes the report from the returned JSON.
- If the scraper returns a hydration error, the orchestrator stops, tells the user "the IG tab couldn't load — make sure the Claude in Chrome MCP tab is visible on your screen (not behind another window, not in a backgrounded space)" and waits for the user to confirm before retrying.
- Create `research/` if missing.
- Report contains every reel scraped (3 × N). No padding, no editorial cuts.
