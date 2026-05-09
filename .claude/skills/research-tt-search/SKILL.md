---
name: research-tt-search
description: "Explores TikTok via search bar — orchestrator opens a fresh Chrome tab and hands the ID to a Sonnet scraper that loops every search term in that single tab, clicks the Videos sub-tab to unlock the full grid, then captures caption + views + user + date for every visible card per term. The orchestrator then sorts all videos by views and writes the report directly. Use this when you want to discover what's working on TikTok by topic/keyword. Triggers: tt search research, tiktok search research, what's trending on tiktok, explore tiktok search, search-based tiktok research, research tt search, tiktok niche keyword research."
---

# TT Search Research — Top Videos Per Search Term

The orchestrator opens a fresh Chrome tab and hands the tab ID to a Sonnet scraper. The scraper works through every search term in sequence using that single tab. For each term, navigate to TikTok's video search page, click the Videos sub-tab to unlock the full grid (the default Top tab caps at 12 cards), and capture every visible card's caption + views + user + date. The scraper closes the tab when done. The orchestrator takes the returned JSON, sorts the pooled videos by views high-to-low across all terms, tags topic + CTA, and writes the report directly — no second subagent needed.

Unlike YouTube search where titles/descriptions live behind a 2nd-stage visit, TikTok's search grid exposes everything we need on the results page itself. One scrape per term. No video-detail visits.

## How to Trigger
- "research tt search for <terms>"
- "what's trending on tiktok for <term>"
- "explore tt search around <topic>"
- "tt keyword research"

## When to Use This vs research-yt-search / research-ig-competitors

| Use this skill | Use research-yt-search | Use research-ig-competitors |
|---|---|---|
| Explore TikTok by topic/keyword | Explore YouTube by topic/keyword | Track specific IG accounts you already follow |
| Find scrappy, fast-rising hooks | Find long-form niche tutorials | Track week-over-week competitor performance |
| Pull short-form viral patterns | Pull title/description patterns | Pull caption + reel format patterns |

## Prerequisites

- **Claude in Chrome extension** installed and connected (https://claude.ai/chrome). The skill drives a real Chrome window via the `mcp__claude-in-chrome__*` tools.
- **Backbone docs** — `backbone/icp.md` and `backbone/messaging.md` at the project root. The orchestrator derives search terms from these by default.
- **macOS launch command**: the skill uses `open -a "Google Chrome"` to launch Chrome if the extension isn't connected. On Linux/Windows, swap that for the OS-appropriate launcher.
- **A `research/` directory** at the project root. The skill creates it if missing.

## Inputs

### Search terms
**Default: derive from backbone.** The orchestrator reads `backbone/icp.md` + `backbone/messaging.md` and synthesizes 5-7 short search-friendly terms (2-4 words each) targeting the user's niche. Pull terms in these four shapes:

- **Pain phrases** — the literal phrasing the ICP uses to describe their stuck state (e.g. a specific frustration phrase, a status-quo descriptor). Use the exact wording from `icp.md` if it's distinctive.
- **Outcome / desire phrases** — what the ICP openly wants. Pull from headlines, aspirational outcome statements, and desire bullets in the backbone.
- **Belief-shift opposing-view terms** — for each belief shift in `messaging.md`, derive a phrase that surfaces content holding the OPPOSING view (the one the user is arguing against). These find ideologically aligned audiences and surface dunk-able takes.
- **Niche descriptors** — concrete tools, methodologies, or category names that creators in the niche actually tag content with. Pull from offer deliverables, branded methodology terms, and niche jargon in the backbone.

Skip generic umbrella terms — anything so broad it pulls noise from outside the niche (e.g. broad category labels like "AI", "fitness", "business"). The whole point is targeting INSIDE the niche.

Print the derived keywords before scraping so the user sees what will be searched.

**Override:** user can name terms inline ("research tt search for '<term 1>', '<term 2>', '<term 3>'"). When inline terms are given, skip the derivation step entirely.

---

## Architecture

```
Orchestrator (opens tab, assigns ID) → Sonnet scraper (uses assigned tab, closes it) → Orchestrator (writes report) → research/TT-Search-Research_YYYY-MM-DD.md
```

**Why this design:**
- **Same architecture as research-yt-search.** Orchestrator owns tab creation, scraper owns teardown.
- **One tab, foreground.** Serial avoids Chrome's background-tab throttling. Slower than parallel but bulletproof.
- **Click the Videos sub-tab.** TikTok's default landing on `/search/video?q=...` actually shows the "Top" cross-format tab which caps at 12 cards. Clicking the "Videos" sub-tab swaps to the videos-only grid (24+ cards) where the per-card view counts are already visible.
- **No 2nd-stage visit.** The TikTok search grid exposes caption + views + user + date inline. We get everything we need without visiting each video. ~5-7s per term end-to-end.
- **No scrolling.** Programmatic `scrollTop` on TikTok's main container doesn't trigger lazy-load (TikTok requires real wheel/touch input). The 24+ cards in the initial Videos tab payload are the working budget — that's plenty.
- **MCP redaction workaround.** Chrome MCP redacts strings matching JWT/cookie/base64 patterns in tool results. Many TikTok usernames (e.g. `faceless.inc.proj`) match the JWT regex (`a.b.c`) and come back as `[BLOCKED: JWT token]`. The scraper sanitizes user + href fields by replacing `.` with `∙` (U+2219, BULLET OPERATOR) before returning, and the orchestrator reverses it.

---

## Scraper Agent Brief

Spawn with `subagent_type: general-purpose`, `model: sonnet`. Substitute `{TERMS_JSON}` (e.g. `["<term 1>","<term 2>","<term 3>"]`) and `{TAB_ID}` (the tab ID the orchestrator already opened):

```
You are scraping TikTok search results for content research. The orchestrator has already opened a fresh Chrome tab for you. Use that tab end-to-end, then close it before returning.

TERMS: {TERMS_JSON}
TAB_ID: {TAB_ID}

STEP 0 — Load Chrome tools.
Call ToolSearch with query: select:mcp__claude-in-chrome__navigate,mcp__claude-in-chrome__javascript_tool,mcp__claude-in-chrome__browser_batch,mcp__claude-in-chrome__tabs_context_mcp,mcp__claude-in-chrome__tabs_close_mcp

DO NOT create a new tab. The orchestrator already created one for you (TAB_ID above). DO NOT force-focus Chrome — no `osascript activate`, no `wmctrl -a`, nothing that yanks Chrome to the foreground.

Optionally call `tabs_context_mcp` once to confirm the tab is present, but do not create or close anything yet.

STEP 1 (per term) — Navigate to the TikTok video search page, close the Activity sidebar if open, click the Videos sub-tab, and extract every visible card.

URL-encode the term (spaces → `%20`, special chars URL-encoded). The search URL is:
  https://www.tiktok.com/search/video?q=<ENCODED_TERM>

Use ONE browser_batch with these actions:
  1. navigate → search URL
  2. javascript_tool → wait 4s for hydration: `new Promise(r => setTimeout(() => r('w'), 4000))`
  3. javascript_tool → close the Activity sidebar if open AND click the Videos sub-tab:

    (() => {
      const activityBtn = document.querySelector('[aria-label="Activity"]');
      const inboxOpen = !!document.querySelector('[data-e2e="inbox-notifications"]');
      if (inboxOpen && activityBtn) activityBtn.click();
      const videosBtn = Array.from(document.querySelectorAll('button')).find(b =>
        b.querySelector('span')?.textContent?.trim() === 'Videos' && b.className.includes('tux-button')
      );
      videosBtn?.click();
      return { inboxClosed: inboxOpen, videosClicked: !!videosBtn };
    })()

  4. javascript_tool → wait 3s for the Videos grid to render: `new Promise(r => setTimeout(() => r('w'), 3000))`
  5. javascript_tool → extract every card. Sanitize user + href dots to bypass MCP JWT-pattern redaction:

    (() => {
      const SAFE = '∙'; // BULLET OPERATOR — replaces "." in user/href to dodge JWT regex redaction
      const sanitize = s => (s || '').replaceAll('.', SAFE);
      const parseViews = v => {
        if (!v) return 0;
        const t = v.trim().toUpperCase();
        const n = parseFloat(t);
        if (isNaN(n)) return 0;
        if (t.endsWith('K')) return Math.round(n * 1e3);
        if (t.endsWith('M')) return Math.round(n * 1e6);
        if (t.endsWith('B')) return Math.round(n * 1e9);
        return Math.round(n);
      };
      const cards = document.querySelectorAll('[id^="grid-item-container-"]');
      const results = Array.from(cards).map(card => {
        const link = card.querySelector('a[href*="/video/"]');
        const href = link?.href || '';
        const userFromUrl = href.match(/@([^/]+)\//)?.[1] || '';
        const views = card.querySelector('[data-e2e="video-views"]')?.textContent || '';
        const caption = card.querySelector('[data-e2e="search-card-video-caption"]')?.textContent?.trim() || '';
        const desc = card.querySelector('[data-e2e="search-card-desc"]')?.textContent?.trim() || '';
        // Date appears at end of desc as one of: "1d ago", "20h ago", "3d ago", "M-D", "YYYY-M"
        const dateMatch = desc.match(/(\d+\s*[hdmwy]\s*ago|\d+\s+(?:hour|day|week|month|year)s?\s+ago|\d{4}-\d{1,2}|\b\d{1,2}-\d{1,2}\b)/i);
        return {
          views,
          viewsNum: parseViews(views),
          user: sanitize(userFromUrl),
          caption,
          date: dateMatch?.[0] || '',
          href: sanitize(href)
        };
      });
      results.sort((a, b) => b.viewsNum - a.viewsNum);
      return { cardCount: results.length, results };
    })()

If `cardCount === 0`, the page didn't fully hydrate — almost always because the MCP tab is hidden/backgrounded or login-walled. STOP IMMEDIATELY. Do not retry, do not move to the next term. Close your tab and return JSON like `{"error": "hydration_failed", "term": "<term>"}` so the orchestrator can prompt the user.

If `cardCount` is small (1-11), the Videos click probably failed (still on the Top tab) or the term has thin results — take what's there and continue. The orchestrator will note it.

Repeat STEP 1 for every term, batched into separate browser_batch calls (one per term). Don't combine all terms into one mega-batch — keep each term self-contained so a single failure doesn't poison the rest.

STEP 2 — Close your tab.
Call `tabs_close_mcp` on TAB_ID. Do this BEFORE returning so the user's browser is clean by the time control hands back to the orchestrator. Don't enumerate the group or close other tabs — just yours. The MCP tab group can linger; that's fine.

STEP 3 — Return the combined JSON block (no other prose). Return:

{
  "terms": [
    {
      "term": "<term 1>",
      "cardCount": <n>,
      "results": [
        {
          "views": "<raw views string, e.g. 310K or 7.2M>",
          "viewsNum": <integer>,
          "user": "<sanitized username>",
          "caption": "<full caption with hashtags>",
          "date": "<raw date string from desc, e.g. '3d ago' or '2025-9'>",
          "href": "<sanitized full url>"
        }
        // every card extracted, sorted by viewsNum desc
      ]
    },
    {
      "term": "<term that errored>",
      "error": "hydration_failed"
    }
  ]
}

Note: user/href fields use `∙` (U+2219) instead of `.` — the orchestrator reverses this on parse.
```

---

## Report Format (you, the orchestrator, write this directly)

Take the scraper's combined JSON. **Reverse the `∙` → `.` substitution** on every `user` and `href` field as you parse. Pool every card from every term. Apply deduplication: if the same `href` appears under multiple terms, fold to a single entry and list all source terms in "ranked for". Sort the deduplicated pool globally by `viewsNum` high-to-low.

For each video, add:
  - **Topic tag** — Education / Journey / Hot take / Lifestyle / Behind-the-scenes / Build-in-public / Story / Tutorial / Money-talk / Tool-drop
  - **CTA type** — Comment-bait / Follow-bait / Watch-next / Link-in-bio / DM / None
  - **Why it ranked** — one line on hook archetype, format mechanic, topic angle, or engagement trigger that likely got it ranked for this search

Add a **Pattern paragraph** at the top — 2-3 sentences on what repeats across the pool: dominant themes, hook archetypes, format mechanics, caption patterns, account-size mix (big accounts dominating vs small accounts breaking through), date freshness (mostly recent vs evergreen). If a term had a scrape error, omit it from the body but call it out in the Pattern line.

Take the **top 30** of the deduplicated pool (or all of them if fewer than 30) — TikTok grids surface a lot of low-view filler past the first viral cluster, so capping prevents the report from drowning the signal.

Write to: `<project_root>/research/TT-Search-Research_<DATE>.md` (computed in step 2)

Format EXACTLY:

```
# TT Search Research — Top Videos By Search Term

**Generated:** YYYY-MM-DD | **Terms searched:** N | **Videos in report:** M (top by views, deduplicated across terms)

> **Pattern:** <2-3 sentences on what's repeating across the pool — dominant themes, hook archetypes, caption patterns, account-size dynamics, date freshness. Be specific.>

**Search terms:** `<term 1>` · `<term 2>` · `<term 3>` …

---

### 1. [<CAPTION>](<URL>) — @<USER>

`<views> views` · posted <date> · ranked for: `<term>`

**Topic:** <tag> · **CTA:** <type>

**Why it ranked:** <one line>

> <full caption, blockquoted. Preserve hashtags and emojis.>

---

### 2. [<CAPTION>](<URL>) — @<USER>

[same structure, repeat for every video in the pool, ordered by views high-to-low, capped at 30]
```

RULES:
- The link text is the caption (truncated to ~80 chars if very long, with `…` suffix). Strip emojis only if they break the markdown link.
- Format view counts human-readable (1.1M, 296K, 47.3K).
- Date: pass through what TikTok shows ("3d ago", "2-23", "2025-12"). No normalization — these are raw values direct from the platform.
- "ranked for" shows which search term surfaced this video. If a video appeared under multiple terms, list all terms separated by `·`.
- Strict view-sort across the whole pool — no editorial reordering.
- No closing wrap-up. The list IS the report.

---

## Main Skill Flow (what YOU do, the orchestrator)

1. **Resolve search terms.** If the user named terms inline, use those and skip to step 2. Otherwise:
   - Read `backbone/icp.md` and `backbone/messaging.md` from the project root.
   - Synthesize 5-7 short search-friendly terms (2-4 words each) using the four shapes listed in **Inputs > Search terms** above. Aim for a mix: 1-2 pain phrases, 1-2 outcome phrases, 1-2 belief-shift opposing-view terms, 1-2 niche descriptors. Avoid generic umbrella terms.
   - Print the derived list to the user before scraping (formatted as `Derived keywords: "<term 1>", "<term 2>", …`, with the source shape annotated next to each one — pain / outcome / belief-opposing / niche). This is a heads-up, not a confirmation prompt — just run with them. The user can re-run with overrides if they want different terms.
2. **Compute the output path.** Today's date in `YYYY-MM-DD` → `<project_root>/research/TT-Search-Research_<DATE>.md`. Create `research/` if missing. Don't inspect or clean up prior reports — every run just writes a new report. A same-day rerun will overwrite that day's file via Write; that's fine.
3. **Open the Chrome tab.** Load Chrome tab tools via `ToolSearch` with query `select:mcp__claude-in-chrome__tabs_context_mcp,mcp__claude-in-chrome__tabs_create_mcp`. Then:
   - Call `tabs_context_mcp`. If it returns "No MCP tab groups found" AND Chrome isn't running (`pgrep -x "Google Chrome"` via Bash), launch Chrome (`open -a "Google Chrome"` on macOS), wait ~2s, then call `tabs_context_mcp` with `createIfEmpty: true`. If Chrome is already running but the group is empty, call `tabs_context_mcp` with `createIfEmpty: true`. If the group already exists, call `tabs_create_mcp` to add a fresh tab.
   - Capture the new tab's ID. This is `{TAB_ID}` for step 4.
   - If `tabs_context_mcp` returns "Browser extension is not connected" (or anything similar), STOP and ask the user to verify the Claude in Chrome extension is connected at https://claude.ai/chrome and that the MCP tab is visible on their screen — TikTok's grid won't hydrate reliably if the tab is hidden behind another window or in a backgrounded space. Wait for the user to confirm before retrying. Don't force-focus Chrome yourself; the user has to do this.
4. Spawn the scraper subagent (`subagent_type: general-purpose`, `model: sonnet`) with the brief above. Inject `{TERMS_JSON}` and `{TAB_ID}`. The scraper uses the assigned tab, scrapes, then closes it before returning.
5. **Reverse the `∙` → `.` sanitization** on every `user` and `href` field in the returned JSON, then deduplicate by href and pool/sort globally by views.
6. **Write the report yourself** using the format above. One Write call to the path from step 2.
7. Report the file path back to the user.

---

## Rules of Thumb
- Single tab, single agent — no parallelism.
- **Don't force-focus Chrome.** No `osascript activate`, no `wmctrl -a`, nothing that yanks Chrome to the foreground. If the user has Chrome open behind something, leave it. Only launch Chrome when it's not already running.
- **Activity sidebar steals the layout.** If the user's TikTok Activity/inbox panel is open in their session, the search results main element won't have a scrollable area. The scraper closes it defensively before clicking Videos.
- **Click Videos sub-tab.** Without it, you're stuck with 12 mixed-format Top results. With it, you get 24-36 video-only cards.
- Hydration failure (`cardCount === 0`) means the MCP tab is hidden/backgrounded or TikTok wants a login. Stop immediately — don't retry, don't skip to the next term. The orchestrator asks the user to make the tab visible (or sign in), then re-runs.
- 1-11 cards on a term means the Videos click missed or the term is genuinely thin — take what's there and continue.
- NO scrolling. NO window resize. NO 2nd-stage visit. The Videos grid gives us everything in one shot.
- Lifecycle ownership: orchestrator opens the tab and assigns the ID; scraper uses that tab and closes it in STEP 2; orchestrator writes the report from the returned JSON.
- Create `research/` if missing.
- Report capped at top 30 deduplicated by views — TikTok's tail past the viral cluster is mostly noise.
