---
name: ig-feed-research
description: "Scans the logged-in Instagram HOME feed (instagram.com — reels, carousels, and image posts together) in the real Chrome profile (Claude-in-Chrome MCP) for on-niche content ideas AND tailors the algorithm with every button the web gives you: three dots → 'Not interested' on off-niche posts (suggested posts of any kind + followed reels), 'Don't suggest posts from X' for categorically wrong accounts, Save on every on-niche keep, and 'Add to favorites' on on-niche followed accounts. Harvest and tailoring are ONE loop on ONE surface. Outputs a visual HTML report to research/. Use this for algorithm-driven discovery — what Instagram itself is pushing right now — vs tracked handles (ig-competitor-research). Triggers: ig feed research, instagram feed research, scan my instagram feed, tailor my instagram, clean up my instagram feed, what's my ig pushing, instagram feed ideas, ig feed."
---

# IG Home-Feed Research — Ideas + Tailoring in One Loop

Scroll the real logged-in Instagram **home feed** (`instagram.com`), classify every post against the niche, and push the algorithm both ways while you read: **Save** what's on-niche, **Not interested** what isn't. Same thesis as `yt-feed-research`: the tailoring isn't cleanup, it's the research engine. Every signal teaches the suggestion engine, and the feed compounds into a daily idea source.

Why the home feed: it's the only surface on IG web with "Not interested", and it carries **carousels and image posts too** (a whole content lane the reels tab hides). The Reels tab and Explore have no dismiss at all on web (see the surface map), so they're never part of the loop.

## How to Trigger
- "scan my instagram feed for ideas"
- "ig feed research"
- "tailor my instagram feed"
- "what's my ig pushing right now"

## When to Use This vs ig-competitor-research

| ig-feed-research | ig-competitor-research |
|---|---|
| What the algorithm pushes at Jason right now | Tracked handles' weekly best |
| Real Chrome, logged-in home feed | Apify scraper, no browser |
| Discovers unknown accounts breaking out | Fixed competitor list |
| Side effect: permanently improves the feed | No side effects |

## Prerequisites

- **Claude-in-Chrome MCP** connected to the real Chrome profile (must be logged into Instagram). Works from the terminal and the desktop app (verified from desktop 2026-11-02); if the tab runs hidden, see the hidden-tab gotcha.
- **Instagram UI language must be English.** `feed-tools.js` matches English strings ('Suggested for you', 'Follow', 'Ad', 'More options', 'Not interested', "Don't suggest posts from", 'Add to favorites', 'Save'); any other locale misclassifies every row and returns `no-entry` on every action.
- Nothing else: no Apify, no yt-dlp. The signals are likes, comments, and judgment.
- **Optional: the VidIQ Chrome extension.** Not required, and most users won't have it. When it's installed it adds a **"Filters"** button to IG's left sidebar that opens a VidIQ "Discovery" panel: the reels from your feed in a grid with plays and an outlier score each (presets Recent / Engagement darlings / Breakout reels free, the rest paid). Use it as a bonus outlier check on reel keeps; the loop never depends on it.

## What the Web Gives You (surface map, verified live 2026-11-02)

| Surface | Negative signal | Positive signal |
|---|---|---|
| Home feed, SUGGESTED post (reel, carousel, image) | Not interested → then "Don't suggest posts from X" | Save, Like, Follow |
| Home feed, FOLLOWED reel | Not interested (no account tier) | Save, Add to favorites |
| Home feed, FOLLOWED carousel / image | none | Save, Add to favorites |
| Reels tab viewer (`/reels/`) | none (menu = Report / Go to post / Share / Copy link / Embed / About this account) | Save, Like |
| Explore (`/explore/`) | none (tiles open in the same Reels viewer) | Save, Like |
| Settings → Content preferences | only "Sensitive content" on web | — |

App-only (not on web): the phone's "Your algorithm" topic list (add/remove topics for Reels, Explore and Feed), "Reset suggested content", and keyword "Not interested" filters. Those are one-time manual taps on the phone, worth doing once by hand; this skill can't reach them. The phone itself (iPhone Mirroring) is an optional deeper lane, Mac-only, outside this skill.

## Hard Safety Rules (IG action-blocks bots — YouTube doesn't care, Instagram does)

- **Read, dismiss, save, favorite. Nothing else.** Never like, follow, unfollow, comment, share, or repost from this loop.
- **Never click "Snooze all suggested posts in feed for 30 days"** (it shows on every hidden-post card). It empties the suggested lane, which is the research surface.
- **One action per `javascript_tool` call**, with the waits baked into the helpers. Never fire actions in batches.
- **Caps per session:** about 40 dismissals, 20 saves, 5 favorites. Max 2 sessions a day. Tailoring compounds across sessions anyway.
- If any **"Try again later" / "We limit how often..."** toast appears: stop all actions immediately, finish the pass read-only, flag it in the report.

## Inputs

- **Idea target** — default **20** saved ideas; user can override inline ("get me 30").
- **Niche filter** — the classification question is: *is this on-niche, or is the format directly replicable for the brand?* If neither → dismiss. The KEEP/DISMISS test is **derived at run time from the repo's context files, never hardcoded here.** Before the first `__feed()` call, read these and build the filter:
  1. `CLAUDE.md` Creator Profile → the **Niche** line. This one-liner defines "on-niche". If that line still holds a `<<` placeholder (brand kit not applied yet), don't stop: ask the user ONE message before anything else, "Quick one before I scan: what's your niche, and who's it for? One line is plenty (e.g. 'meal-prep coaching for busy parents'). If you sell something, name it too." Write the answer as the Niche line in `CLAUDE.md` AND into `brand-kit.md` section 2's Niche field (so applying the brand kit later keeps it), say where you saved it, then continue. This happens once: the next run finds the line filled. Never guess a niche to skip the question.
  2. `backbone/offer.md` (skip it, and `icp.md`, while they still hold `<<` placeholders; the Niche answer is enough) → what is sold (anything that could seed content promoting that offer is KEEP) and, when present, its "What is NOT sold" list (content whose only angle is a NOT-sold thing is DISMISS).
  3. `backbone/icp.md` → who is served and who is not (content that speaks to the ICP's problems is KEEP; content aimed at the not-served segments is DISMISS).
  4. `competitor-list.md` → every IG handle listed there is **always KEEP** when it shows up in the feed.
  5. `knowledge/*.md` when present → recent research signal on what is working in the niche.
  From that, state the filter in one line each before scanning: **KEEP** = topics matching 1–5, plus any standout carousel/image format the brand could replicate for the carousel lane; **DISMISS** = the categorical off-niche buckets you infer from the above (topics no one in the ICP would ask about, formats the brand cannot film or reproduce); **NEUTRAL** = on-niche but weak or ambiguous. Print the derived KEEP/DISMISS one-liner in the report's `{{FEED_STATE}}` fieldnote (the template has no separate slot for it) so the user can veto it. Example only: a creator whose Niche line says "AI leverage for creators" would KEEP AI builds and tool drops and DISMISS fitness, cars, and real estate.

<!-- niche-list:start (owner's concrete KEEP/DISMISS lists; the packager removes this block for clients) -->
Owner's concrete lists (recalibrated 2026-11-02 against `backbone/icp.md` of 2026-09-24 and Jason's 2026-10-01 IG target: Nick Saraev-style AI reels; if they drift, the Niche line wins). KEEP: AI news and tool drops with a use angle ("someone on GitHub just built...", new model or feature, quick AI tips, comment-keyword CTA reels), AI video editing (Claude/Claude Code driving Premiere, DaVinci, CapCut; captions, B-roll, silence cuts), Claude Code / Claude skills for non-technical creators and operators, AI content-production systems (research, scripting, hooks, thumbnails, posting), AI image/video gen used for content (Higgsfield, Veo, Nano Banana), competitor posts (IG handles in `competitor-list.md`), and standout carousel/image formats worth stealing for the carousel lane. NEUTRAL (never dismiss, never save): non-AI content strategy and growth, generic agent/n8n builds, off-lane posts from tracked competitors. DISMISS: AI money proof and side hustles ("$X/mo with AI", AI agency get-rich, faceless "hundreds a day" volume and AI-slop channel pitches), AI-girl / AI-influencer monetization (fake AI models, Fanvue/OnlyFans-style personas, even when the tutorial uses Claude), generic business/offer advice with no AI (the Hormozi genre), business history and news pages, money-guru challenge content, day-trading/crypto/forex, luxury-lifestyle flexing (watches, cars, mansions), motivational-guru edits, memes/skits, fitness, vlogs, filmmaking, real estate, general news, gadget reviews.
<!-- niche-list:end -->

## The Loop

```
read CLAUDE.md Niche line (still a << placeholder → ask once, save, go on) + backbone/offer.md + backbone/icp.md + competitor-list.md → derive KEEP/DISMISS (Inputs)
  → navigate instagram.com → inject scripts/feed-tools.js → __feed() → classify every row
  → KEEP: add to idea list (reels AND carousels AND posts) + __save(user)
      · followed on-niche account, not yet fav → __favorite(user)
  → DISMISS: __feedDismiss(user,'post')   (SUGGESTED any kind, or followed REEL)
      · SUGGESTED + categorically wrong account → __feedDismiss(user,'account')
      · followed carousel/image off-niche → no button exists; flag repeat offenders
  → NEUTRAL / AD: no action
  → __more() → __feed() → classify only rows not seen yet → repeat
  → until idea target hit or feed stalls → fill assets/report-template.html → research/ → open it
```

### Step 1 — Open the home feed
`tabs_context_mcp {createIfEmpty:true}`, navigate to `https://www.instagram.com/`, wait ~4s. If a login wall renders, stop and tell the user.

### Step 2 — Inject helpers + extract
Paste the **entire** `scripts/feed-tools.js` into one `javascript_tool` call (re-inject after every navigation — page loads wipe `window.*`). `__feed()` returns one row per article currently in the DOM: `user | SUGGESTED/followed/AD | reel/carousel/post | L<likes> C<comments> | fav,saved flags | caption`. **The feed virtualizes**: old articles leave the DOM as you scroll, so there are no stable indexes. Keep a seen-set keyed by `user + first caption words` in your own notes and classify only new rows. All actions take the username (or `"user|caption words"` when one account has two posts loaded) and find the post at call time.

A scan pass is `__more()` → `__feed()` → classify the new rows. Batch 2–3 `[__more, __feed]` pairs per `browser_batch` call when no actions are pending. Tool results truncate around 1.5KB, so when a pass returns many rows, read them in slices (`window.__rows.slice(0,6).join('\n')`).

**Safety-filter trap** (same as YT): never return raw hrefs, query strings, innerHTML, or `key=value`-shaped strings from `javascript_tool` — the harness blocks the whole result (`[BLOCKED: Cookie/query string data]`). Cleaned text only; the helpers already enforce this.

### Step 3 — Classify every row
The test: **on-niche, or replicable for the brand?** (the KEEP/DISMISS filter derived in Inputs)
- **KEEP** → idea list: username, kind (reel/carousel/post), likes, comments, hook/caption line, one-line concept, remix angle. Then `__save(user)`: saves are the strongest positive signal the web exposes. Carousels are first-class keeps — they feed the `carousel-generator` lane directly. If the account is followed and the row has no `fav` flag, also `__favorite(user)` (cap 5 a session; favorites lift that account in the home feed).
- **DISMISS** → `__feedDismiss(user,'post')` on a `SUGGESTED` row (any kind) or a followed reel. Use `(user,'account')` when a `SUGGESTED` account will never be on-niche (its whole catalog sits in one DISMISS bucket): it clicks "Don't suggest posts from <user>" on the hidden-post card and IG confirms "We won't suggest posts from X". An Undo stays on the card for Jason.
- **Followed carousels/images off-niche**: IG gives no "Not interested" there (menu = Unfollow / Add to favorites only). The helper returns `no-entry` harmlessly; flag repeat offenders in the report instead. Unfollowing is Jason's call, never the loop's.
- **AD rows**: no action, ever. Every helper refuses them with `user:ad`.
- **NEUTRAL** (in-niche but weak, ambiguous): no action. Don't punish the algorithm for almost-right guesses, and don't boost them either.

Return codes for every helper: `user:ok`, `user:ok-account` (account block landed too), `user:already` (already saved / favorited), `user:no-item` (post not in the DOM: scroll back up a step and retry once, or let it go), `user:ad` (refused), `user:no-btn` (no control found), `user:no-entry` (menu had no matching entry).

Outlier judgment: likes/comments vs how recognizable the account is. Big engagement from an unknown account = the signal; flag `small sample` when it rides on a tiny account. With VidIQ installed, cross-check reel keeps in its Discovery panel (outlier score); without it, judgment is the whole score.

### Step 4 — Advance and repeat
`__more()` then `__feed()`; classify only the new rows. One action per `javascript_tool` call. Expect 20 keeps across a few hundred scanned posts on an untuned feed — and don't grind past ~60–80 articles to force the target; report what you have and note that tailoring compounds across sessions.

**Pagination stall:** the home feed can stop serving articles (stuck at the same handful even at page bottom), and after a dismissal it sometimes re-renders back near the top. That's IG throttling or re-ranking, not a bug. Reload once and re-inject; if it persists, end the session early rather than hammering it, and say so in the report.

### Step 5 — Report
Fill **`assets/report-template.html`** (this skill's folder); do NOT design from scratch. The template is the locked preset (same editorial dark "Algorithm Field Report" as `yt-feed-research`, text-only cards with linked usernames, kind tags reel/carousel/post, likes/comments badges). The HTML comment at the top documents every `{{PLACEHOLDER}}` and the card partial to duplicate. Write the filled file to `research/IG-Feed-Research_YYYY-MM-DD_HHMMSS.html` (timestamped so a second same-day session never overwrites the first) and open it in the default browser (macOS `open`, Linux `xdg-open`, Windows Git Bash `start "" <file>`). Never delete prior reports. Sections, in order (the summary strip is the header stat row + feed-state note):
1. **Summary strip** — posts scanned, ideas saved (by kind: reels/carousels/posts), dismissals applied (post vs account level), saves and favorites applied, the derived KEEP/DISMISS one-liner used this session (inside `{{FEED_STATE}}`), feed-state before/after one-liner, any rate-limit flag.
2. **🚀 Top outliers** — biggest engagement-vs-account-size keeps, one-line remix-angle note each.
3. **📈 Strong picks** — the rest of the keeps, badges only.
4. **🎠 Carousel steals** — carousel/image formats worth cloning via `carousel-generator`.
5. **🤔 Borderline** — logged but not counted toward the target.
6. **🧹 Tailoring log** — every dismissal (username + concept + post/account level) and every save/favorite, so Jason can veto via IG's Undo or the Saved tab, plus flagged followed accounts.

Cards: linked username (`instagram.com/<user>/`), hook/caption excerpt, likes/comments badges, kind tag. **No inline thumbnails** — IG media URLs are signed, expire, and trip the safety filter. For visuals/transcripts of the winners, hand the usernames to `ig-competitor-research` or `transcribe-url`.

## Gotchas (don't rediscover)

- **The page scrolls on `<body>` now (2026-11 layout), not `documentElement`.** Setting `documentElement.scrollTop` silently does nothing and the feed sits at 5 articles. `__more()` picks whichever element actually overflows.
- **Suggested detection:** some suggested posts drop the "Suggested for you" line and only show a bare `Follow` button in the header; `__feed` counts either as `SUGGESTED`.
- **Counts:** reels show likes/comments as bare numbers next to the action buttons, not "N likes"; `__feed` reads the sibling after each button. `?` = hidden count.
- **Menus are NOT `role="dialog"`** — entries are found by scanning visible childless text leaves outside `<article>`. The hidden-post card ("Post hidden" / "Don't suggest posts from X" / Snooze / Undo) also renders outside the article now, so the account-tier click matches the exact username.
- **JS clicks work for menus, Save, and dialog entries** (no cold-start trap on IG, unlike YT). Close a stuck menu with a real `computer` Escape; the JS-dispatched one is unreliable.
- Dialog text uses curly apostrophes ("Don't suggest…") that `clean()` strips — helpers match with `don.?t` regexes; preserve that when editing.
- Ads show `Ad` (or `Sponsored`) plus "See details"/"Learn more" in the header lines — never act on them (opens ad-preference dialogs). `__feed` flags them `AD` and every helper refuses them.
- **The "1x" on every reel is a playback-speed control**, not an outlier multiplier. VidIQ's scores live only in its Discovery panel and on `/<user>/reels/` tiles.
- If Claude-in-Chrome errors "not connected", retry once — transient drops mid-session are normal and the in-flight page JS still completed. A CDP 45s timeout usually means a loop in one call ran too long: keep `__more` loops to about 8 steps per call.
- **Hidden-tab run (2026-10-01):** when Chrome runs the MCP tab hidden (`document.hidden` true), `__more()` scrolls but the lazy loader never fires. Jump the scroller to the bottom, then send one real `computer` wheel scroll (5 ticks); that loads the next batch. The Reels viewer froze the renderer outright in a hidden tab, so don't use it.
- **Best outlier source = `instagram.com/<user>/reels/` tiles** (VidIQ users only): each tile's `innerText` carries views plus the VidIQ multiplier (e.g. `423K 4.1x`), so one page load ranks an account's recent reels. Then open `/p/<id>/` per pick to read the caption and click the single `svg[aria-label="Save"]`.
- Positive tailoring works fast: saving 20 outliers + favoriting 5 accounts flipped the home feed's top 9 to 7 on-niche posts in one session (2026-10-01).
- First run of any variant is a calibration run: verify extraction on a few articles before the first action, patch `feed-tools.js` against the live DOM, and log fixes here.
