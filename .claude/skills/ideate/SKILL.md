---
name: ideate
description: "Runs a timed 1-hour ideation block. Picks platform + goal, sets a Mac alarm, probes the business backbone for fresh angles, scans Notion saved Ideas (including IG/YT links the user dropped), then runs competitor research if still dry — outputs N packaged ideas straight into Notion as new Idea pages, ready for the scriptwriter skill. Triggers: /ideate, ideate, ideation, ideation block, brainstorm ideas, come up with ideas, batch ideas, fill the pipeline, content ideation, need ideas."
---

# Ideate — Timed Ideation Block

A focused 1-hour ideation session that ends with a fixed number of ideas packaged and ready for the scriptwriter skill. Designed to fight blank-page paralysis: backbone probe first (original angles from Jason's own positioning), then Notion saved Ideas (stuff he already flagged as worth making), then competitor research as the fallback.

## How to Trigger
- **"/ideate"** — start a new ideation block
- **"ideate for IG"** / **"ideate for YT"** — skip platform question, set goal next
- **"ideate 5 reels"** / **"ideate 1 YouTube video"** — skip both questions, start the timer

---

## The Flow

```
Step 0 → Platform + Goal       (~2 min)
Step 1 → Set 1hr timer         (~1 min)
Step 2 → Backbone probe        (~10–15 min)  ← original angles first
Step 3 → Notion saved Ideas    (~10–15 min)  ← stuff Jason already flagged
Step 4 → Competitor research   (~20–25 min)  ← only if still short
Step 5 → Package + drop into Notion as Ideas
```

If Jason hits the goal early (e.g., backbone probe alone produces 5 strong reel angles), **skip remaining steps and go straight to Step 5**. The timer is a budget, not a quota.

---

## Step 0 — Platform + Goal

Ask two questions if not provided in the trigger phrase:

1. **Platform:** YouTube long-form / Instagram short-form (default if unclear: IG short-form — Jason's primary motion)
2. **Goal:** How many ideas, packaged and ready, by the end of the hour
   - Default for short-form: **5 reels**
   - Default for long-form: **1 YouTube video** (long-form ideas need more depth, fewer needed)
   - Jason can override

Output one line confirming:
> **Block plan:** [N] [platform] ideas in 60 min. Starting timer now.

---

## Step 1 — Set the Timer

Run a single Bash command (background mode) that fires a Mac notification with sound at the 60-minute mark:

```bash
START_TS=$(date +%s) && (sleep 3600 && osascript -e 'display notification "Ideation block — time to package what you have." with title "/ideate" sound name "Glass"') &
```

Then **save the start timestamp** in conversation context (just remember the value of `START_TS`). Use it at each step transition to print:

```
[XX min in — YY min left]
```

Example:
```
[15 min in — 45 min left] Step 2 done. 3 angles flagged. Moving to Notion saved Ideas.
```

Print a checkpoint at the start of each remaining step (2, 3, 4, 5). Don't spam — once per step transition is enough.

**If Jason wants to stop early** (hits goal, or wants to bail): kill the background sleep with the job ID, or just `pkill -f 'sleep 3600'` and confirm.

---

## Step 2 — Backbone Probe (~10–15 min)

Read all four backbone files in parallel:
- `backbone/vision.md` — mission, MRR ladder, backstory
- `backbone/icp.md` — Standard + Premium ICPs, USP, competitor breakdown
- `backbone/offer.md` — pricing, deliverables, urgency
- `backbone/messaging.md` — 5 belief shifts, headlines, proof bank

Then **probe** — generate angles by asking these questions against the backbone:

1. **Belief shift angles:** Each of the 5 belief shifts in `messaging.md` is a content angle. Which ones haven't been hit recently? (Cross-check with `analytics/` if available.)
2. **Proof bank angles:** Any specific result, client win, or personal milestone in the backbone that hasn't been turned into content? (e.g., Albert 200→5–10K views, Ayden $2K→$10K, Poppy 700K viral, $7,410 MRR.)
3. **Anti-LARP / contrarian angles:** What's the niche getting wrong that Jason's positioning corrects? (Anti-gatekeep, anti-$5–50K courses, anti-corporate.)
4. **ICP pain → dream outcome bridges:** What's a current ICP pain (Standard or Inner Circle) that maps directly to one of the offer's deliverables?
5. **Urgency / timeliness angles:** May 17 price flip from $75 → $97. The pivot itself (May 3 from high-ticket to Skool). Any deadline or change creates urgency content.

**Output a numbered list of raw angle seeds** (no full hooks yet — just the angle):

```
BACKBONE PROBE — [N] angles found

1. [Angle] — [which belief shift / proof point / pain it ties to]
2. [Angle] — [...]
...
```

Then ask Jason: **"Any of these feel right? Mark the ones you'd film."**

Mark the ones he picks. They survive into Step 5.

---

## Step 3 — Notion Saved Ideas (~10–15 min)

Pull all pages from the Notion content DB with Status = `Idea`. The DB ID is `21bf6585-5e6b-81df-b692-e0321083dffa` (same as the notion-content-pipeline skill).

For each Idea page, look for **reference links Jason has already saved** — he sometimes saves a tweet, reel, or YouTube video URL in the title or in the page body as a "this is the kind of thing I want to make" reference.

### How to find the links:
1. Use `mcp__notion__API-post-search` with `filter: {"property": "object", "value": "page"}` and paginate.
2. Filter to pages with `parent.database_id = 21bf6585-5e6b-81df-b692-e0321083dffa` AND `properties.Status.status.name = "Idea"`.
3. For each Idea page:
   - Check the **title** for URLs (regex: `instagram\.com|youtube\.com|youtu\.be|tiktok\.com|x\.com|twitter\.com`)
   - Pull block children with `mcp__notion__API-get-block-children` and check for:
     - `bookmark` blocks (they have a `url` field)
     - `embed` blocks
     - `paragraph` / `rich_text` blocks containing URLs
     - `link_preview` blocks

### What to do with them:
- **Filter to platform-relevant links.** If the block is for IG short-form, surface IG/TikTok/Shorts links and skip long-form YT.
- **Group:** Ideas with reference links go on top — those are pre-loaded angles. Ideas without links get listed underneath.
- **For each Idea with a link:** if it's an IG reel or YouTube video, optionally pull the transcript using the **transcribe-url skill** (only if Jason wants to dig in — ask first, don't auto-burn tokens).

**Output:**

```
NOTION SAVED IDEAS — [X] with refs, [Y] without

With reference links:
  1. "[Title]" → [URL] ([platform])
  2. "[Title]" → [URL] ([platform])

Without links (just titles):
  - [Title]
  - [Title]

Want to pull the transcript on any of these to dig into the angle?
```

---

## Step 4 — Competitor Research (only if still short)

**Skip this step if Jason already has enough angles from Steps 2 + 3 to hit the goal.** Don't burn the second half of the hour scraping if backbone + Notion already filled the slate.

If still short, run the appropriate research skill:
- **IG short-form** → invoke the `ig-competitor-research` skill
- **YouTube long-form** → invoke the `yt-competitor-research` skill

Then mine the resulting report for outliers — top-performing reels/videos that map to a Jason angle. Each outlier becomes a candidate idea.

**Output:**

```
COMPETITOR PULL — [N] outlier-driven angles

1. [Angle] — modeled on [competitor] [URL] ([X] views)
2. [Angle] — modeled on [competitor] [URL] ([X] views)
...
```

---

## Step 5 — Package + Drop Into Notion

This is the whole point of the skill. Take the angles that survived (backbone picks + Notion-link picks + competitor picks) and turn them into **packaged ideas ready for the scriptwriter skill**.

### Package format (per idea):

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
IDEA #[N] — [Working Title]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Platform: [IG short-form / YT long-form]
Funnel: TOF / MOF / BOF
Angle: [one-line core insight or claim]
Hook seed: [rough hook direction — not the final 3 hooks, just the seed]
Belief shift / pain: [which one from messaging.md]
Proof anchor: [specific result, client, or system referenced]
Reference: [URL if from Notion-saved or competitor, else "original"]
```

### Drop into Notion:

For each packaged idea, **create a new page** in the Notion content DB using `mcp__notion__API-post-page`:

```
parent: { "database_id": "21bf6585-5e6b-81df-b692-e0321083dffa" }
properties: {
  "Title": { "title": [{ "text": { "content": "[Working Title]" } }] },
  "Status": { "status": { "name": "Idea" } },
  "Format": { "select": { "name": "Short-form" or "Long-form" } }
}
children: [
  // paragraph block with the full package details so scriptwriter can read it later
]
```

The package details (angle, hook seed, belief shift, proof anchor, reference URL) go in the **page body** as paragraph blocks so the scriptwriter skill can pull them on the next call.

### Final output:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
/IDEATE COMPLETE — [N]/[goal] ideas packaged
Time: [XX min] of 60 min
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Dropped into Notion as Ideas:
  1. [Title] — [TOF/MOF/BOF]
  2. [Title] — [TOF/MOF/BOF]
  ...

Next: /scriptwriter to turn any of these into scripts.
```

If under goal: be honest. Don't pad with weak ideas to hit the number.

---

## Important Notes

- **The timer is a budget, not a quota.** Stop early if the goal is hit. Don't run out the clock probing for marginal angles.
- **Don't auto-pull transcripts** from every saved Notion link — ask first. Token-heavy if there are 10+ saved Ideas.
- **Backbone probe is the highest-leverage step.** Original angles from Jason's own positioning beat outlier-mimicking every time. Only fall back to competitor research if backbone + Notion are dry.
- **One question per step transition, max.** Don't ping Jason every minute — let him think. The checkpoint print is enough.
- **Default platform if Jason is mid-flow and doesn't specify:** IG short-form. That's his primary motion right now.
- **Kill the timer if Jason bails:** `pkill -f 'sleep 3600'` cleanly. Don't leave background sleeps orphaned.

---

## What This Skill Does NOT Do

- Write the actual scripts (use scriptwriter skill — `/ideate` only packages the ideas, scriptwriter turns them into hooks/teleprompter)
- Generate hooks (3-hook variations come from scriptwriter, not here — Step 5 produces a "hook seed" only)
- Replace the analytics review (if Jason wants data-driven angle selection, use `ig-analytics` first, then feed findings into Step 2)
- Auto-run competitor research before backbone — backbone is always first, competitor is the fallback
