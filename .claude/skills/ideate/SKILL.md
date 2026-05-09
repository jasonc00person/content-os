---
name: ideate
description: "Runs a timed ideation block that ships beat sheets, not just ideas. Starts a visual countdown timer, asks platform + goal count, pulls research (auto-runs the matching research skill if no report exists), then runs a per-pair pick loop where the user picks a winning video to recreate. Each pick gets handed to the scriptwriter skill, which owns the twist conversation, transcription, format decomposition, and the Notion write. Original-idea path: ramble it (voice-to-text fine) and scriptwriter packages it fresh. Triggers: /ideate, ideate, ideation, ideation block, brainstorm ideas, come up with ideas, batch ideas, fill the pipeline, content ideation, need ideas, batch scripts."
---

# Ideate — Timed Batch Wrapper

A focused ideation block that produces **N beat sheets in Notion as `Scripted`** by the end of the timer. Default flow: pull research, user picks a winning video to recreate, hand the URL to `scriptwriter`. Rare path: user has an original idea instead — they ramble, scriptwriter packages it fresh.

Ideate is the **timed batch wrapper**. Scriptwriter does all the per-video work — twist-asking, transcription, decomposition, beat sheet, Notion write. If ideate finds itself transcribing, reading backbone files, or asking for a twist, it's reaching into scriptwriter's lane.

## How to Trigger
- **"/ideate"** — start a new ideation block
- **"ideate for IG"** / **"ideate for YT"** — skip platform question, set goal next
- **"ideate 5 reels"** / **"ideate 1 YouTube video"** — skip both questions, start the timer

---

## The Flow

```
Step 1 → Start timer                                (~30s)
Step 2 → Ask platform                               (~30s)
Step 3 → Ask goal count                             (~30s)
Step 4 → Pull research (or run research skill)      (~3–5 min)
Step 5 → Per-pair pick loop                         (~30s/pair)
Step 6 → Hand off each pick to scriptwriter         (~5 min/pair, scriptwriter handles)
Step 7 → Stop timer + report duration
```

The timer is a budget, not a quota. If the goal is hit early, finalize immediately — don't wait out the clock.

**Step 5 and Step 6 can interleave.** As soon as the user picks, fire its handoff and start the next pick while scriptwriter runs. (Sequential handoffs only — see Step 6 sequencing rule.)

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
- Red flash + "TIME" at zero (silent — no sound, no browser notification)

### Step transitions
At each step transition (Step 4 → 5 → 6), print elapsed/remaining via:
```
python3 -c "import json,time,sys; r=json.load(open(sys.argv[1])); e=int(time.time())-r['start']; print(f'[{e//60} min in — {(1800-e)//60} min left]')" "$SKILL_DIR/.runtime.json"
```
Print once per transition. Don't spam.

### Stopping early
If the user bails or hits the goal early, run the cleanup block from Step 7 (kills server via `stop.py` + closes Chrome tab + reports session duration).

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

## Step 4 — Pull Research (always runs)

The default flow is recreating winning videos with a fresh twist, so research always loads. The `research/` folder holds prior outputs from the research skills.

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
Read the selected report files in parallel. **Do NOT load backbone files, transcribe anything, or decompose formats** — those are scriptwriter's responsibilities. Ideate stops at "user can see the table."

---

## Step 5 — Per-Pair Pick Loop (~30s/pair)

This is a thin loop: show the table, get the pick, fire the handoff. **No transcription, no format breakdown, no twist conversation here** — all of that lives in scriptwriter.

Pull all videos from the loaded reports into one ranked table, **sorted by views descending**, **top 10 cap**. Show it once at the start of the loop.

### The format table

```
| # | Views | Title | Channel |
|---|-------|-------|---------|
| 1 | 1.5M  | [exact title](https://source-url) | @creator |
| 2 | 256K  | [exact title](https://source-url) | @creator |
| 3 | 249K  | [exact title](https://source-url) | @creator |
| ... (up to 10)
```

### Loop (repeat N times until picks made == goal count)

Each round, ask:

> **Pair [X/N]** — which video # are we recreating? *(Or if you've got an original idea instead, just ramble it — voice-to-text fine.)*

Two paths:

**A. Recreation pick (default):**
1. User picks `#3` (may or may not name a twist alongside — doesn't matter to ideate either way).
2. Resolve the URL from the ranked table row.
3. Fire Step 6 handoff immediately, forwarding the user's verbatim pick message so scriptwriter can detect any inline twist.

**B. Original-idea ramble (rare):**
1. User has a concept that isn't a recreation. Capture it verbatim.
2. No URL to resolve.
3. Fire Step 6 handoff with `MODE: original` and the verbatim ramble.

### Rules
- **Top 10 only.** Sort by views, top 10 — never more.
- **Always hyperlink the title** to the source URL using `[title](url)` form.
- **Don't pre-filter for "on-brand."** The user knows their voice.
- **Don't transcribe, decompose, or ask for the twist.** Scriptwriter owns those. Pass the URL + the user's verbatim pick message and let it work.
- **Don't load backbone files.** Scriptwriter loads them itself. Ideate stays out of concept-level work entirely.
- **Many-to-many is fine.** Same source URL can be picked by multiple pairs (different twists) — no dedup.

### Track each pair
For each handoff fired, capture:
- Source URL (or `null` for original-idea path)
- The user's verbatim pick message
- Format type (Short-form for IG/TT, Long-form for YT)
- Notion URL once scriptwriter returns

When `picks made == goal count`, exit the loop. Move to Step 7 (or finalize if you've been firing handoffs inline).

---

## Step 6 — Hand Off Each Pick To Scriptwriter

For each pick, invoke the `scriptwriter` skill via the `Skill` tool with the minimal payload below. **Scriptwriter does everything else** — asks for the twist (or detects it inline from USER PICK), transcribes via subagent, decomposes format, writes the beat sheet, creates the Notion page in `Scripted` status.

### Handoff payload

**Recreation pair (default):**
```
URL: <source URL from the picked row>
FORMAT: Short-form | Long-form
USER PICK: <user's verbatim pick message — may contain a twist, may not>
```

**Original-idea pair (rare):**
```
URL: none
FORMAT: Short-form | Long-form
USER PICK: <user's verbatim ramble>
MODE: original
```

That's the entire payload. No CONCEPT field, no TRANSCRIPT field. Scriptwriter is responsible for everything downstream.

### Sequencing
Run handoffs **sequentially**, not in parallel. Scriptwriter writes to Notion and uses the Chrome tab via transcribe-url; parallel calls would race. After each pair completes, capture the resulting Notion URL.

You can fire each handoff inline as soon as the user picks — but still one at a time. If a handoff is mid-flight when the next pick lands, queue it and fire when the previous finishes.

### Step transition print
Print elapsed/remaining once before the loop starts and once after it finishes. Don't spam between picks.

---

## Step 7 — Stop Timer + Report Duration

When all picks are scripted (or the user calls it), compute the session duration and stop the timer.

### Compute duration
```
python3 -c "import json,time,sys; r=json.load(open(sys.argv[1])); e=int(time.time())-r['start']; print(f'{e//60} min {e%60} sec')" "$SKILL_DIR/.runtime.json"
```

### Cleanup (always run, even on early bail) — cross-platform
```
python3 "$SKILL_DIR/stop.py"
```
(Use `python` on Windows.) `stop.py` kills the server process and removes `.runtime.json`. Then close the timer tab via `mcp__claude-in-chrome__tabs_close_mcp` with the tab ID you saved at Step 1.

### Final output
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
/IDEATE COMPLETE — [N]/[goal] beat sheets shipped
Session: [XX min YY sec]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Dropped into Notion as Scripted:
  1. <Notion URL> — from <source URL>
  2. <Notion URL> — from <source URL>
  ...

Next: open Notion → Scripted column → film.
```

If under goal: be honest. Don't pad with weak picks.

---

## Important Notes

- **Default = format-first recreation.** User picks a winning video → handoff. The twist conversation happens in scriptwriter, not here.
- **Original ideas are the escape hatch, not the default.** Mention it once in the loop prompt, then move on.
- **Ideate does not transcribe, decompose, ask for twists, or load backbone files.** Every per-video concern lives in scriptwriter. If you're reaching for `transcribe-url` or `Read backbone/`, stop — you're in scriptwriter's lane.
- **Scriptwriter is the engine.** Ideate is a thin batch wrapper around it.
- **The timer is a budget, not a quota.** Fire handoffs inline as picks land; don't wait until all N are picked.
- **Top 10 cap, hyperlinked titles, every time.** No exceptions in Step 5.
- **Auto-run research only if no matching report exists.** Don't re-run if a recent report exists — just use it.
- **Always run the cleanup block** when ending the session. Don't leave the http server or Chrome tab orphaned.
- **Always report session duration** in the final output.

---

## What This Skill Does NOT Do

- **Transcribe, decompose, or write beats.** That's scriptwriter's job. Hand off in Step 6.
- **Ask for the twist or propose one.** Scriptwriter Step 1 owns the twist conversation.
- **Load backbone files.** Scriptwriter loads them as it needs them.
- **Ask "concept-first or format-first?"** Default is format-first. Just show the table.
- **Drop pages in `Idea` status.** Pairs go straight to `Scripted` via scriptwriter.
- **Filter for "on-brand."** The user picks. They know their voice.
- **Pad to hit the goal.** Honest count > vanity count.
