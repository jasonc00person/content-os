# ig-feed-research: setup

Scans the logged-in Instagram home feed (reels, carousels, and image posts together) in your real Chrome profile for on-niche content ideas, and tailors the algorithm while it does it with every button Instagram web offers: off-niche posts get three-dots → "Not interested" (plus "Don't suggest posts from X" for categorically wrong accounts), on-niche keeps get Saved, and on-niche accounts you follow get added to Favorites. Harvest and tailoring are one loop on one surface. Trigger it with "ig feed research", "scan my instagram feed", "tailor my instagram feed", or "what's my ig pushing".

## Install

Drop this folder into a skills directory:
- `<project>/.claude/skills/ig-feed-research/` for one project, or
- `~/.claude/skills/ig-feed-research/` to use it everywhere.

## Prerequisites

**1. Claude-in-Chrome MCP** connected to your real Chrome profile, logged into Instagram. Works from the terminal or the desktop app.

**2. Instagram UI language set to English.** `scripts/feed-tools.js` matches English strings ('Suggested for you', 'Follow', 'Ad', 'More options', 'Not interested', "Don't suggest posts from", 'Add to favorites', 'Save'); any other locale misclassifies every row and returns `no-entry` on every action.

**3. Nothing else to install.** No Apify, no yt-dlp, no Python. `scripts/feed-tools.js` is pasted into the page by the skill itself. The VidIQ Chrome extension is optional: if you have it, its "Filters" sidebar button shows an outlier score per reel, which the skill uses as a bonus check.

**4. Your niche.** If you haven't applied your brand kit yet, the first run asks for your niche in one line, saves it to `CLAUDE.md` and `brand-kit.md`, and carries on; it never asks again. The full brand kit makes the filter sharper. The niche filter (what gets kept vs "Not interested") is derived at run time from your Creator Profile in `CLAUDE.md` (the Niche line), `backbone/offer.md`, `backbone/icp.md`, and `competitor-list.md`; the skill asks for it while the Niche line still holds a placeholder.

## Output

Fills `assets/report-template.html` and writes `research/IG-Feed-Research_YYYY-MM-DD_HHMMSS.html` (dark card grid: outliers, strong picks, carousel steals, borderline, tailoring log), then opens it in your default browser (macOS `open`, Linux `xdg-open`, Windows Git Bash `start "" <file>`). Prior reports are never deleted. Cards are text-only with linked usernames; IG media URLs are signed and expire, so no thumbnails.

## Gotchas

- Instagram action-blocks bots: read, dismiss, save, favorite only (never like, follow, comment), one action at a time, caps of about 40 dismissals, 20 saves and 5 favorites per session, max 2 sessions a day. Stop on any "Try again later" toast.
- On the web, "Not interested" exists only in the home feed: on suggested posts of any kind and on reels from accounts you follow. The Reels tab, Explore, and followed carousels/images have none, and ads are never touched.
- The skill never clicks "Snooze all suggested posts": it would empty the feed the research reads.
- Instagram's "Your algorithm" topic list and "Reset suggested content" are phone-app only. Set your topics there once by hand; the browser loop can't reach them.
- Every navigation wipes the injected helpers; re-paste `scripts/feed-tools.js` after any reload.
