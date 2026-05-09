---
name: ideate
description: "Runs a timed ideation block that ships beat sheets, not just ideas. Starts a visual countdown timer, asks platform + goal count, pulls research (auto-runs the matching research skill if no report exists), then runs a per-pair loop where the user picks a winning video to recreate and names a twist. If the user blanks on a twist, ideate reads the backbone and proposes one. Each locked pair (source URL + twist) goes to the scriptwriter skill, which transcribes the source, keeps the format, swaps in the new concept, and drops a beat sheet into Notion as `Scripted`. Rare path: user has an original idea instead — ramble it (voice-to-text fine) and scriptwriter packages it fresh. Triggers: /ideate, ideate, ideation, ideation block, brainstorm ideas, come up with ideas, batch ideas, fill the pipeline, content ideation, need ideas, batch scripts."
---

# Ideate — Timed Batch Scriptwriter

A focused ideation block that produces **N beat sheets in Notion as `Scripted`** by the end of the timer. Default flow is **format-first**: pull research, user picks a winning video to recreate, user names a twist (or ideate proposes one from backbone if they blank), pair gets handed off to `scriptwriter`. Rare path: user has an original idea instead — they ramble, scriptwriter packages it fresh.

Ideate is the batch wrapper; scriptwriter is the engine.

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
Step 5 → Per-pair loop: pick video → name twist     (~3–5 min/pair)
Step 6 → Hand off each pair to scriptwriter         (~5 min/pair)
Step 7 → Stop timer + report duration
```

The timer is a budget, not a quota. If the goal is hit early, finalize immediately — don't wait out the clock.

**Step 5 and Step 6 can interleave.** As soon as a pair locks in Step 5, fire its handoff and start the next pair while scriptwriter runs. (Sequential handoffs only — see Step 6 sequencing rule.)

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
Read the selected report files in parallel. **Do NOT load the backbone yet** — it only loads in Step 5 if the user blanks on a twist.

---

## Step 5 — Per-Pair Loop (~3–5 min/pair)

This is the core. Pull all videos from the loaded reports into one ranked table, **sorted by views descending**, **top 10 cap**. Show it once at the start of the loop.

### The format table

```
| # | Views | Title | Channel |
|---|-------|-------|---------|
| 1 | 1.5M  | [exact title](https://source-url) | @creator |
| 2 | 256K  | [exact title](https://source-url) | @creator |
| 3 | 249K  | [exact title](https://source-url) | @creator |
| ... (up to 10)
```

### The default loop (format-first — repeat N times until pairs locked == goal count)

Each round, ask:

> **Pair [X/N]** — which video # are we recreating? *(Or if you've got an original idea instead, just ramble it — voice-to-text fine.)*

**Default branch (format-first):**
1. User picks `format #3` from the table.
2. **Transcribe the source first.** Invoke `transcribe-url` (or call its bash entrypoint directly: `bash .claude/skills/transcribe-url/scripts/transcribe-url.sh "<URL>"`) and read the resulting markdown file from `transcripts/url/`. **Captions lie about what made the video work** — the spoken content reveals the real hook mechanism, beat count, and pacing. Save the transcript path; you'll pass it to scriptwriter in Step 6 so it doesn't re-transcribe.
3. **Post a 3-line format breakdown** of the actual transcript: hook mechanism (one line), structural beats in order (one line), the psych trick that did the heavy lifting (one line). Keep it terse. This grounds the twist conversation in reality, not caption guesses.
4. Prompt: *"What's the twist? How are we making it our own?"*
5. **If the user names a twist** → lock pair → fire Step 6 handoff (or queue it).
6. **If the user blanks** ("got nothing", "you tell me", "I'm stuck") → load backbone:
   - Read `backbone/icp.md` and `backbone/messaging.md` (default).
   - If the source video is offer/pricing-related, also read `backbone/offer.md`. If mission/strategy-leaning, also read `backbone/vision.md`.
   - Propose **one** twist in plain English: a fresh original concept the user can speak from, dressed in the source's winning format (use the actual transcript-derived beats, not the caption). One sentence, no ladders or alternatives — pick the strongest angle and commit.
   - User accepts → lock pair. User refines → use their refinement, lock pair.

**Escape hatch (original idea — rare):**
1. User has a concept that isn't a recreation. Capture it verbatim — voice-to-text rambles welcome.
2. No source URL, no transcribe step. Format type comes from the platform (Short-form for IG/TT, Long-form for YT).
3. Lock the pair → fire Step 6 handoff in `original` mode (no URL, scriptwriter writes fresh from the ramble).

### Rules
- **Top 10 only.** Sort by views, top 10 — never more.
- **Always hyperlink the title** to the source URL using `[title](url)` form.
- **Don't pre-filter for "on-brand."** The user knows their voice.
- **Default is recreation.** Original ideas are the rare path, not the lead.
- **Don't pitch a twist unless the user blanks.** Wait for them to ask or clearly say they're stuck. Don't volunteer alternatives, don't list options — give them the floor first.
- **When you do propose a twist, propose ONE.** No ladders, no "or you could do X." Pick the strongest angle from backbone, state it, ship it.
- **Many-to-many is fine.** Same source can be reused with different twists; same twist can be paired with multiple sources.
- **One round of clarification max** per pair before locking.

### Track each pair
For each locked pair, capture:
- **Source URL** — from the picked format row (or `null` for original-idea path)
- **Transcript path** — path to the markdown file written by `transcribe-url` (or `null` for original-idea path)
- **Concept/twist** — verbatim from user (or your backbone-derived proposal if they blanked)
- **Format type** — Short-form for IG/TT, Long-form for YT

When `pairs locked == goal count`, exit the loop. Move to Step 6 (or finalize if you've been firing handoffs inline).

---

## Step 6 — Hand Off Each Pair To Scriptwriter

For each locked pair, invoke the `scriptwriter` skill via the `Skill` tool in **IDEATE-HANDOFF** mode. Scriptwriter does all the heavy lifting — transcribe the source via `transcribe-url`, decompose format vs concept, run the anti-slop check, write the beat sheet, and create a new Notion page in `Scripted` status.

### Handoff payload (per pair)

**Recreation pair (default):**
```
IDEATE HANDOFF
URL: <source URL from the format pick>
TRANSCRIPT: <path to the markdown file from transcribe-url, e.g. transcripts/url/video-by-creator_2026-05-08.md>
CONCEPT: <user's twist — verbatim, or backbone-derived if user blanked>
FORMAT: Short-form | Long-form
```

**Original-idea pair (rare):**
```
IDEATE HANDOFF
URL: none
CONCEPT: <user's ramble — verbatim>
FORMAT: Short-form | Long-form
MODE: original
```

Scriptwriter recognizes the `IDEATE HANDOFF` header. For recreation pairs, it reads the supplied `TRANSCRIPT` path directly (skips re-transcription — ideate already did that in Step 5) and decomposes format vs concept. For `MODE: original`, it skips transcription and writes a fresh beat sheet directly from the ramble. Both paths still run the source-creator test and anti-slop check.

### Sequencing
Run handoffs **sequentially**, not in parallel. Scriptwriter writes to Notion and uses the Chrome tab via transcribe-url; parallel calls would race. After each pair completes, capture the resulting Notion URL.

You can fire each handoff inline as soon as a pair locks in Step 5 — but still one at a time. If a handoff is mid-flight when the next pair locks, queue it and fire when the previous finishes.

### Step transition print
Print elapsed/remaining once before the loop starts and once after it finishes. Don't spam between pairs.

---

## Step 7 — Stop Timer + Report Duration

When all pairs are scripted (or the user calls it), compute the session duration and stop the timer.

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
  1. <Notion URL> — <concept> × format from <source URL>
  2. <Notion URL> — <concept> × format from <source URL>
  ...

Next: open Notion → Scripted column → film.
```

If under goal: be honest. Don't pad with weak pairs.

---

## Important Notes

- **Default = format-first recreation.** User picks a winning video → names a twist → handoff. Don't ask "concept-first or format-first?" — just lead with the table.
- **Original ideas are the escape hatch, not the default.** Mention it once in the loop prompt, then move on.
- **Backbone loads ONLY if the user blanks on a twist.** Otherwise the user owns the concept. When you do propose, propose ONE twist — no menus.
- **Ideate transcribes at pick-time so the twist is grounded in the actual video, not the caption.** Captions usually misrepresent what made a video work. The transcript is what surfaces the real hook mechanism + beat structure — both for the user and (when proposing) for ideate. Then hand the transcript path forward so scriptwriter doesn't re-pull it.
- **Scriptwriter is still the engine.** Don't duplicate decompose / beat-sheet / Notion-write logic here. Hand off in Step 6 and trust it.
- **The timer is a budget, not a quota.** Fire handoffs inline as pairs lock; don't wait until all N are paired.
- **Top 10 cap, hyperlinked titles, every time.** No exceptions in Step 5.
- **Auto-run research only if no matching report exists.** Don't re-run if a recent report exists — just use it.
- **Always run the cleanup block** when ending the session. Don't leave the http server or Chrome tab orphaned.
- **Always report session duration** in the final output.

---

## What This Skill Does NOT Do

- **Transcribe, decompose, or write beats.** That's scriptwriter's job. Hand off in Step 6.
- **Brainstorm twists upfront.** Let the user name the twist first. Only propose one (from backbone) if they explicitly blank.
- **Ask "concept-first or format-first?"** Default is format-first. Just show the table.
- **Drop pages in `Idea` status.** Pairs go straight to `Scripted` via scriptwriter.
- **Filter for "on-brand."** The user picks. They know their voice.
- **Pad to hit the goal.** Honest count > vanity count.
