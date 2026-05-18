---
name: ideate
description: "Runs an ideation block that ships beat sheets, not just ideas. Asks platform + goal count, pulls research (auto-runs the matching research skill if no report exists), then runs a per-pair pick loop where the user picks a winning video to recreate. Each pick gets handed to the scriptwriter skill, which owns the twist conversation, transcription, format decomposition, and the Notion write. Original-idea path: ramble it (voice-to-text fine) and scriptwriter packages it fresh. Triggers: /ideate, ideate, ideation, ideation block, brainstorm ideas, come up with ideas, batch ideas, fill the pipeline, content ideation, need ideas, batch scripts."
---

# Ideate — Batch Wrapper

A focused ideation block that produces **N beat sheets in Notion as `Scripted`** by the end of the session. Default flow: pull research, user picks a winning video to recreate, hand the URL to `scriptwriter`. Rare path: user has an original idea instead — they ramble, scriptwriter packages it fresh.

Ideate is the **batch wrapper**. Scriptwriter does all the per-video work — twist-asking, transcription, decomposition, beat sheet, Notion write. If ideate finds itself transcribing, reading backbone files, or asking for a twist, it's reaching into scriptwriter's lane.

## How to Trigger
- **"/ideate"** — start a new ideation block
- **"ideate for IG"** / **"ideate for YT"** — skip platform question, set goal next
- **"ideate 5 reels"** / **"ideate 1 YouTube video"** — skip both questions, jump straight to research

---

## The Flow

```
Step 1 → Stamp start time                        (~1s)
Step 2 → Ask platform                            (~30s)
Step 3 → Ask goal count                          (~30s)
Step 4 → Load knowledge + pull research          (~3–5 min)
Step 5 → Per-pair pick loop                      (~30s/pair)
Step 6 → Hand off each pick to scriptwriter      (~5 min/pair, scriptwriter handles)
Step 7 → Report session duration
```

If the goal is hit early, finalize immediately — don't pad with weak picks.

**Step 5 and Step 6 can interleave.** As soon as the user picks, fire its handoff and start the next pick while scriptwriter runs. (Sequential handoffs only — see Step 6 sequencing rule.)

---

## Step 1 — Stamp Start Time

Single bash command. No server, no Chrome tab, no countdown UI — just record when the session began so Step 7 can report duration.

```bash
date +%s > /tmp/ideate-start
```

Done. Move on.

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
> **Block plan:** [N] [platform] ideas.

---

## Step 4 — Load Knowledge + Pull Research (always runs)

Read these first when they exist:

1. `knowledge/index.md`
2. `knowledge/current-content-opportunities.md`
3. `knowledge/competitor-patterns.md`
4. `knowledge/winning-hooks.md`

This is the fast compiled layer. Use it to understand the current lane before opening raw reports. If the knowledge files are stale or missing important recent research, read the relevant `research/` report directly and mention that `knowledge-compile` should be run after the session.

The default flow is recreating winning videos with a fresh twist, so research always loads. The `research/` folder holds prior outputs from the research skills.

### Filter by platform
- **IG short-form** → `IG-Competitor-Research_*.md` (also `TT-Search-Research_*.md` if present — short-form trends overlap)
- **YouTube long-form** → `YT-Competitor-Research_*.md`, `YT-Search-Research_*.md`
- **TikTok** → `TT-Search-Research_*.md` if present; otherwise use `IG-Competitor-Research_*.md` as the closest short-form proxy

Sort matching reports by date (newest first via filename `_YYYY-MM-DD`) and pick the **2 most recent**. If only one exists, use that.

### If no matching report exists
Run the appropriate research skill before proceeding. Match platform → skill:
- **IG** → `research-ig-competitors`
- **YouTube** → `research-yt-competitors` (default — uses `competitor-list.md`, no extra input needed)
- **TikTok** → no dedicated TikTok research skill exists yet. Use the newest IG short-form report as a proxy, or ask whether to run `research-ig-competitors` first.

Tell the user one line: *"No [platform] research on file. Running `/research-[skill]` now — give it ~3–5 min."* Then invoke the matching skill. When it finishes, re-scan the `research/` folder and continue.

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

---

## Step 7 — Report Session Duration

When all picks are scripted (or the user calls it), compute the session duration from the start stamp.

```bash
echo "$(( ($(date +%s) - $(cat /tmp/ideate-start)) / 60 )) min $(( ($(date +%s) - $(cat /tmp/ideate-start)) % 60 )) sec"
rm -f /tmp/ideate-start
```

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
- **Fire handoffs inline as picks land.** Don't wait until all N are picked.
- **Top 10 cap, hyperlinked titles, every time.** No exceptions in Step 5.
- **Auto-run research only if no matching report exists.** Don't re-run if a recent report exists — just use it.
- **Always report session duration** in the final output.

---

## What This Skill Does NOT Do

- **Run a visual countdown timer.** No HTML page, no http server, no Chrome tab — just a start stamp + final duration line.
- **Transcribe, decompose, or write beats.** That's scriptwriter's job. Hand off in Step 6.
- **Ask for the twist or propose one.** Scriptwriter Step 1 owns the twist conversation.
- **Load backbone files.** Scriptwriter loads them as it needs them.
- **Ask "concept-first or format-first?"** Default is format-first. Just show the table.
- **Drop pages in `Idea` status.** Pairs go straight to `Scripted` via scriptwriter.
- **Filter for "on-brand."** The user picks. They know their voice.
- **Pad to hit the goal.** Honest count > vanity count.
