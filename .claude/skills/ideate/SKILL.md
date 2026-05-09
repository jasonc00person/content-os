---
name: ideate
description: "Runs a timed ideation block. Starts a visual countdown timer, asks platform + goal count, gives the user a chance to flex original ideas first, then falls back to the research folder (running the matching research skill if no report exists for the platform) and lists the top 10 hyperlinked videos for inspiration. Drops each idea — original or research-modeled — into Notion as an Idea page so the scriptwriter skill can pick it up. Triggers: /ideate, ideate, ideation, ideation block, brainstorm ideas, come up with ideas, batch ideas, fill the pipeline, content ideation, need ideas."
---

# Ideate — Timed Ideation Block

A focused ideation session that ends with N ideas dropped into Notion, ready for the scriptwriter skill. The flow gives the user a chance to flex original ideas first, then falls back to inspiration from the `research/` folder. **The scriptwriter skill handles the actual creative twist on the next call — `/ideate` just captures and packages.**

## How to Trigger
- **"/ideate"** — start a new ideation block
- **"ideate for IG"** / **"ideate for YT"** — skip platform question, set goal next
- **"ideate 5 reels"** / **"ideate 1 YouTube video"** — skip both questions, start the timer

---

## The Flow

```
Step 1 → Start timer                         (~30s)
Step 2 → Ask platform                        (~30s)
Step 3 → Ask goal count                      (~30s)
Step 4 → Original ideas first                (open-ended)   ← user flexes creative muscle
Step 5 → Pull research (or run research)     (~3–5 min)     ← only if more ideas needed
Step 6 → User picks from top 10              (~5–10 min)
Step 7 → Package + drop into Notion as Ideas
```

If the goal is hit early (e.g. user dumps all N original ideas), **skip remaining steps and go straight to Step 7**. The timer is a budget, not a quota.

---

## Step 1 — Start the Timer

Spin up the timer FIRST, before the platform/goal questions. Keep momentum.

The timer is a self-contained HTML page (`timer.html`) served by a tiny Python HTTP server (`server.py`) and opened in a Chrome tab. **Fully portable across macOS, Linux, and Windows** — only requirements are Python 3.7+ and Chrome.

### Files in this skill folder
- `timer.html` — the visible countdown page (HTML + CSS + JS, no deps)
- `server.py` — starts http server on a free port, writes `pid + port + start_ts` to `.runtime.json`
- `stop.py` — reads `.runtime.json`, kills the server, removes the file
- `.runtime.json` — runtime state (gitignored; only exists while a block is active)

### Spin up the server (cross-platform)
The skill base directory is in the slash-command prompt — call it `$SKILL_DIR`. Pick the right launcher for the OS:

**macOS / Linux:**
```bash
SKILL_DIR="<base dir>"
(python3 "$SKILL_DIR/server.py" >/dev/null 2>&1) &
disown
sleep 1
```

**Windows (PowerShell):**
```powershell
$SkillDir = "<base dir>"
Start-Process -FilePath python -ArgumentList "$SkillDir\server.py" -WindowStyle Hidden
Start-Sleep -Seconds 1
```

**Windows (cmd):**
```cmd
start /B python "%SKILL_DIR%\server.py" >NUL 2>&1
timeout /T 1 /NOBREAK >NUL
```

### Read the runtime port
After ~1s, read `$SKILL_DIR/.runtime.json` to get the port the server claimed (it tries 8765 first, falls back to 8766–8799 if busy):
```
python3 -c "import json,sys; print(json.load(open(sys.argv[1]))['port'])" "$SKILL_DIR/.runtime.json"
```
(Use `python` instead of `python3` on Windows.)

### Open the timer tab in Chrome
1. `mcp__claude-in-chrome__tabs_context_mcp` with `createIfEmpty: true`
2. `mcp__claude-in-chrome__tabs_create_mcp` — fresh tab (or reuse the empty tab from context)
3. `mcp__claude-in-chrome__navigate` to `http://localhost:<port>/timer.html?s=1800` (use `?s=<seconds>` for testing — e.g. `?s=30`)
4. Remember the tab ID in conversation context for cleanup at Step 7

The HTML handles everything end-to-end:
- Big responsive countdown (16vw font)
- Live tab title: `HH:MM:SS · Ideation` (visible from tab bar even when in background)
- Red flash + "TIME" + audio beep + browser notification at zero

**Important:** Chrome blocks audio until the user clicks the page once. When the tab opens, tell the user: *"Click the timer page once to unlock the alarm sound."*

### Step transitions
At each step transition (Step 5 → 6 → 7), print elapsed/remaining via:
```
python3 -c "import json,time,sys; r=json.load(open(sys.argv[1])); e=int(time.time())-r['start']; print(f'[{e//60} min in — {(1800-e)//60} min left]')" "$SKILL_DIR/.runtime.json"
```
Print once per transition. Don't spam.

### Stopping early
If the user bails or hits the goal early, run the cleanup block from Step 7 (kills server via `stop.py` + closes Chrome tab).

---

## Step 2 — Ask Platform

Use `AskUserQuestion`:
1. **Platform:** Instagram short-form / YouTube long-form / TikTok

Skip if specified in the trigger phrase.

---

## Step 3 — Ask Goal Count

Use `AskUserQuestion`:
1. **Goal:** How many ideas, packaged and ready, by the end of the block
   - Default for short-form: **5 reels**
   - Default for long-form: **1 YouTube video**
   - Common alternates: 3, 5, 10

Skip if specified in the trigger phrase.

Output one line confirming:
> **Block plan:** [N] [platform] ideas in 30 min.

---

## Step 4 — Original Ideas First (creative muscle flex)

Before pulling any research, give the user the floor. They know their voice + audience better than any report. Tell them:

> Got any original ideas you want to flex first? Drop them now — caption / title / rough concept, one per line. When you're tapped out, say so and we'll pull the top 10 from research for inspiration.

For each original idea the user gives, capture:
- **Caption / title** — what they said, verbatim or lightly cleaned
- **Format** — derived from platform (Short-form for IG/TT, Long-form for YT)
- **Source URL** — none (original idea)

Track the running count: `[X / N original]`. If the user hits the goal entirely with original ideas, **skip Steps 5–6** and go straight to Step 7.

If the user has fewer originals than the goal, ask whether to top up from research or stop here. If they say top up, continue to Step 5.

### Rules
- **Don't pitch ideas yourself.** Don't volunteer angles. The user is flexing — let them.
- **Don't filter or critique.** If they give you a weak idea, capture it and move on. Their pipeline.
- **Don't load the backbone.** Same reason as the rest of the skill — scriptwriter handles brand fit.

---

## Step 5 — Pull Research (only if needed)

Only runs if the user has fewer original ideas than the goal count. The `research/` folder holds prior outputs from the research skills.

### Filter by platform
- **IG short-form** → `IG-Competitor-Research_*.md` (also `TT-Search-Research_*.md` if present — short-form trends overlap)
- **YouTube long-form** → `YT-Competitor-Research_*.md`, `YT-Search-Research_*.md`
- **TikTok** → `TT-Search-Research_*.md` (also `IG-Competitor-Research_*.md` if present)

Sort matching reports by date (newest first via filename `_YYYY-MM-DD`) and pick the **2 most recent**. If only one exists, use that.

### If no matching report exists
Run the appropriate research skill before proceeding. Match platform → skill:
- **IG** → `research-ig-competitors`
- **YouTube** → `research-yt-competitors` (default — uses `competitor-list.md`, no extra input needed)
- **TikTok** → `research-tt-search` (needs search terms — ask the user for 4–6 keywords first)

Tell the user one line: *"No [platform] research on file. Running `/research-[skill]` now — give it ~3–5 min."* Then invoke the skill via `Skill` tool. When it finishes, re-scan the `research/` folder and continue.

### Read the reports
Read the selected report files in parallel. **Do NOT load the backbone** — we're surfacing what works, not filtering for on-brand.

---

## Step 6 — User Picks From Top 10 (~5–10 min)

Pull videos from the loaded reports into one ranked table, **sorted by views descending**, and **show only the top 10**. Don't dump the full pool — 10 is the cap, every time.

### Table format

```
| # | Views | Title | Channel |
|---|-------|-------|---------|
| 1 | 1.5M  | [exact title](https://source-url) | @creator |
| 2 | 256K  | [exact title](https://source-url) | @creator |
| 3 | 249K  | [exact title](https://source-url) | @creator |
| ... (up to 10)
```

Below the table:
> Pick [remaining count] (or just give me the numbers).

### Rules
- **Top 10 only.** Sort by views, present the top 10 — never more.
- **Always hyperlink the title** to the source URL using markdown `[title](url)` form. Never plain text titles in the table.
- **Don't pre-filter for "on-brand."** The user knows their voice.
- **Don't pitch angles or twists.** Don't say "your version of this could be...". The shape IS the shape — scriptwriter handles the twist.
- **Don't ask which "concept" or "pattern."** Just videos. User picks by number.
- **One round of clarification max** if the user wants to discuss a pick. Otherwise: pick → package → ship.

### Track research-modeled picks
For each picked video, capture:
- **Caption / title** — the source video's title, verbatim
- **Format** — Short-form for IG/TT, Long-form for YT
- **Source URL** — the source video's URL

When the total (originals + picks) hits the goal, move to Step 7.

---

## Step 7 — Package + Drop Into Notion

For each idea collected (whether original or research-modeled), create a new page in the Notion content DB using `mcp__notion__API-post-page`. DB ID and property names come from `notion-pipeline.md` — load it before writing.

### Page shape
```
parent: { "database_id": "<from notion-pipeline.md>" }
properties: {
  "Title":  { "title":  [{ "text": { "content": "[caption / title]" } }] },
  "Status": { "status": { "name": "Idea" } },
  "Format": { "select": { "name": "Short-form" or "Long-form" } }
}
children: [
  // ONE paragraph block containing the source URL as a hyperlink, OR
  // no children at all if it's an original idea (no source link)
]
```

### Body content
- **Research-modeled idea:** ONE paragraph block. The block contains a single text run with the source URL as the visible text AND as the link target — i.e. `{ "type": "text", "text": { "content": "<URL>", "link": { "url": "<URL>" } } }`. That's it. No "why it worked", no view counts, no funnel-stage labels.
- **Original idea:** No children at all. Empty body.

That's the whole package: caption title, format, source link (if any). Scriptwriter pulls full context when it runs.

### Final output
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
/IDEATE COMPLETE — [N]/[goal] ideas packaged
Time: [XX min] of 30 min
Originals: [X] · Research-modeled: [Y]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Dropped into Notion as Ideas:
  1. [caption / title] — [original / modeling URL]
  2. [caption / title] — [original / modeling URL]
  ...

Next: /scriptwriter to turn any of these into scripts.
```

If under goal: be honest. Don't pad with weak picks to hit the number.

### Cleanup (always run, even on early bail) — cross-platform
```
python3 "$SKILL_DIR/stop.py"
```
(Use `python` on Windows.) `stop.py` kills the server process and removes `.runtime.json`. Then close the timer tab via `mcp__claude-in-chrome__tabs_close_mcp` with the tab ID you saved at Step 1.

---

## Important Notes

- **Originals before research, every time.** Step 4 always runs before Step 5. The user gets a shot at their own ideas before being shown other people's.
- **The timer is a budget, not a quota.** Stop early if the goal is hit. Don't run out the clock.
- **Top 10 cap, hyperlinked titles, every time.** No exceptions in Step 6.
- **Auto-run research only if no matching report exists.** Don't re-run if a report from this week already exists — just use it. Match platform → research skill in Step 5.
- **Don't load the backbone.** Not needed here — scriptwriter handles brand fit.
- **Always run the Step 7 cleanup block** when ending the session. Don't leave the http server or Chrome tab orphaned.

---

## What This Skill Does NOT Do

- **Brainstorm twists, angles, or original takes for the user.** Step 4 captures what THEY say. Don't pitch.
- **Write titles, thumbnails, or hooks.** Scriptwriter's job.
- **Filter for "on-brand."** The user picks. They know their voice.
- **Pad to hit the goal.** Honest count > vanity count.
- **Write the actual scripts.** Use the scriptwriter skill.
