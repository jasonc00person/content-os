---
name: scriptwriter
description: "Turns a source video URL (or fresh topic / ramble / Notion Idea) into a beats-only script written straight into the Notion content pipeline. Default flow: transcribe the source, run it through the backbone to find the user's unique creative twist, then write a visually intuitive beat sheet into a new Notion page — using the source's own structural shape as the section headings (not a fixed HOOK/VALUE/CTA template). Not word-for-word — the user fills in their own expertise on camera. Triggers: write a script, script this, scriptwriter, twist this video, rewrite this reel, script out idea X, turn this ramble into a script, batch scripts."
---

# Scriptwriter — Beats Into Notion

Produces **scannable beat sheets**, not teleprompter text. Each script lands as a Notion page in the content pipeline, with properties set and a body the user can read on a phone between takes — every bullet is a full readable sentence describing what happens in that beat.

The default play: take a video that already worked for someone else, **steal the format**, then build a **completely new concept** inside that proven structural shell. The twist is a new idea wearing a winning outfit — not the source video re-spun in the user's voice.

---

## ⚠️ The Core Principle — Format vs Concept

This is the whole game. Read it twice.

**FORMAT (copy this — it's the proven viral mechanism):**
- Hook type and mechanism — **what counts as "the hook" depends on the format:**
  - **Short-form (IG Reels / TikTok / YT Shorts):** the hook is whatever the host SAYS in the first 3-5 seconds. The on-screen title overlay and caption are decoration; the spoken opener is what stops the scroll.
  - **Long-form (YouTube):** the hook is the **title** (paired with the thumbnail). Title is what earns the click, and no click means no view. The spoken cold-open matters for retention, but the title's grammatical/rhetorical pattern is what we copy as the hook.
  - In both cases: pull the verbatim hook artifact (spoken line for short-form, title string for long-form) and treat *its* grammatical/rhetorical pattern as the format to keep.
- Structural shape (list, demo, story, build-in-public, before/after, rant, walkthrough)
- Pacing and beat timing (when the payoff lands, how long the value section runs)
- CTA pattern (comment-keyword, DM, link in bio)
- Visual/shot grammar (proof shot opener, screen recording, talking head, B-roll style)

**CONCEPT (must be net-new — this is where the user actually says something):**
- The topic / claim / argument / insight
- The specific examples, numbers, frameworks, names
- The proof anchors and stories
- The angle on the niche
- The belief shift being reinforced

If we copy both, it's AI slop — the source diluted and rewritten. If we copy neither, we lose the structural reason it worked. The job is **proven format + original concept**. Always.

A successful TWIST passes this test: *"If the source creator saw the user's video, they'd recognize the format but not the idea."* If they'd recognize the idea, restart the concept step.

---

## Modes

| Mode | Trigger | Source |
|------|---------|--------|
| **TWIST** *(primary)* | URL provided ("twist this", "rewrite this reel", URL pasted) | Source video → transcribe → twist via backbone |
| **FRESH** | Topic only ("write a script about X") | Backbone + voice DNA, no source |
| **RAMBLE** | Voice dump / stream of consciousness | Extract core idea → structure |
| **PIPELINE** | "script out [Idea]" / "script idea #3" | Existing Notion page in `Idea` status |

Detect the mode before doing anything. If ambiguous, ask one question and proceed.

---

## TWIST Flow (the main flow)

### 1. Ask upfront: "Do you already have a twist?"

Before transcribing or doing any decomposition work, ask the user one question:

> *"Got a twist/concept already, or want me to read the video + backbone and propose one?"*

Two branches from here:

- **User has a twist** → capture it verbatim. Skip step 4's candidate generation entirely (their concept is the concept). Run steps 2 → 3 → 5 → 6 with their concept locked in.
- **User wants you to propose** → run the full flow (steps 2 → 3 → 4 → 5 → 6) and surface ONE proposed twist at step 4. Confirm it before writing to Notion.

Skip this question when the user clearly stated their twist in the same message they supplied the URL — including `/ideate` handoffs where the twist appears in the `USER PICK` field. Parse the message for any "except / but / instead / make it about / with [X]" clause that names a fresh angle. If found, treat it as a user-supplied twist and skip the question.

### 2. Spawn a Sonnet subagent — transcribe + decompose (NEVER read the full transcript directly)

Bundle transcription and format decomposition into a single subagent call. The orchestrator must NOT load the full transcript into its own context. The subagent returns only a tight FORMAT skeleton.

**Why this is non-negotiable:** the whole point of TWIST is "throw away concept, keep format." The full transcript is exactly the stuff we need to discard — loading it wastes tokens and risks concept contamination (orchestrator drifting toward source-flavored beats during writeup). A 30-min long-form transcript can run 40K+ tokens, none of which the orchestrator needs.

**The subagent's job:**
1. Run `transcribe-url` on the URL (or read the cached transcript at the supplied `TRANSCRIPT` path if `/ideate` handoff already produced one).
2. Decompose the transcript into a structured FORMAT skeleton.
3. Return ONLY that skeleton + a one-line "source concept signature" (so the orchestrator can do an overlap check on the user's twist without ever seeing the source's specifics).

**Spawn it as:** `Agent` tool with `subagent_type: general-purpose` and `model: sonnet`. Prompt template:

```
You are doing format decomposition for the scriptwriter skill. Read the source transcript and return ONLY the format skeleton — no concept details.

Source URL: <URL>
Cached transcript path (skip transcribe if provided): <PATH or "none — transcribe first">

If no cached path: run `bash .claude/skills/transcribe-url/scripts/transcribe-url.sh "<URL>"` first, then read the resulting file (with offset/limit if it's large).

Return EXACTLY this structure (~400 words total):

## SOURCE CONCEPT SIGNATURE
<one phrase — what the source is actually ABOUT at the topic level. The orchestrator uses this for overlap-check only. Keep it generic enough that it doesn't contaminate, e.g. "small-business consulting transformation" not "HVAC duct cleaning pricing">

## HOOK ARTIFACT (verbatim — pulled from the right place per format)
For SHORT-FORM (IG Reels / TikTok / YT Shorts): quote the literal first 3-5 seconds of SPOKEN audio (what the host says, NOT the title overlay or caption).
For LONG-FORM (YouTube): quote the literal video TITLE string (NOT the spoken cold-open).
"<the verbatim hook artifact, in quotes>"

## HOOK STRUCTURAL PATTERN
<one sentence describing the grammatical/rhetorical mechanism — e.g. "I used to [embarrassing past belief], and it [got me result]" or "How I [achieved outcome] in [timeframe] using [method]" — strip the actual concept words and just name the SHAPE>

## HOOK MECHANISM
<one line — type of hook (confession / contrarian / curiosity gap / proof drop / list promise / dream outcome / etc.) + what it promises the viewer>

## STRUCTURAL SHAPE
<one phrase — e.g. "consultation deep-dive with time-later payoff", "list video", "before/after">

## BEAT LIST (in order)
For each beat:
- BEAT NAME IN CAPS — rough timestamp range — one-sentence intent (no concept details)

Aim for the actual count of beats observed. No forced 5-act mold.

## PACING NOTES
- Where the hook payoff lands
- How long the value section runs
- How often the host breaks to camera for meta-commentary
- CTA placement pattern (single, repeated, woven)

## CTA PATTERN
<one paragraph — soft/hard, keyword/link, give-first vs direct sale, frequency, exact placement>

## VISUAL / SHOT GRAMMAR
- Main shot type
- Signature visual moves (overlays, before/after reveals, physical proof devices, etc.)

## SIGNATURE PSYCH MOVE
<one sentence — the specific psychological mechanism doing the heavy lifting>

HARD RULES:
- **THE HOOK ARTIFACT DEPENDS ON THE FORMAT.** Short-form (IG Reels / TikTok / YT Shorts) → the spoken first 3-5 seconds. Long-form (YouTube) → the video title. Never substitute one for the other. On short-form the title overlay/caption is decoration; on long-form the spoken cold-open is retention, not the hook.
- NO source-specific topics, names, niches, dollar amounts, examples, or arguments anywhere except the SOURCE CONCEPT SIGNATURE line and the HOOK ARTIFACT quote.
- Beat names describe structural function only ("DIAGNOSE BOTTLENECK" yes, "DIAGNOSE HVAC PRICING" no).
- ~400 words total. Terse. No editorializing, no improvement suggestions, no "why it works" essays.
- Return only the structured output. No preamble.
```

The subagent's return is the only artifact the orchestrator works from for the rest of the flow. Treat it as the canonical decomposition — don't second-guess by re-reading the transcript.

### 3. Load backbone (selectively)
Always: `voice-dna.md` + `backbone/icp.md` + `backbone/messaging.md`.
Add only if relevant: `backbone/offer.md` (pricing/offer angles), `backbone/vision.md` (mission-driven content).

### 4. Lock the concept (skip candidate generation if user already named a twist in step 1)

**If the user supplied a twist in step 1:** their concept IS the concept. Skip the rest of this step's candidate generation — go straight to the source-creator test (rule 3 below) to make sure their idea isn't accidentally close to the source. Compare the user's twist against the subagent's `SOURCE CONCEPT SIGNATURE` line. If there's overlap, surface that and ask them to sharpen it. Otherwise lock and move on.

**If the user wanted you to propose:** This is where most AI script tools fail — they re-spin the source's concept in a new voice and call it a twist. That is slop. Don't do it.

Take the FORMAT skeleton returned by the step-2 subagent, hold it fixed, and **invent a fresh concept** that fits inside it. The concept must be something the user can credibly say that doesn't overlap with the subagent's `SOURCE CONCEPT SIGNATURE`.

Surface ONE proposed twist (no menus, no ladders). It must:
1. **Fit the kept format perfectly** (same hook mechanism, same structural shape, same payoff timing, same CTA pattern). If a concept doesn't fit the format, drop it — find one that does.
2. **Be anchored to something only the user has** — pull from the user's backbone:
   - Specific proof from the user's proof bank (`backbone/messaging.md` — follower counts, MRR, member wins, named viral hits)
   - A user-specific system, methodology, or tool stack named in their backbone or `voice-dna.md`
   - One of the **belief shifts** in `messaging.md` (if structured that way — count and content vary per user)
   - The user's backstory beats (origin, prior path, distinctive credentials)
3. **Pass the source-creator test:** if the original creator saw the user's video, they'd nod at the format but not recognize the idea. Concretely: the user's concept must sit in a different topic-space than the subagent's `SOURCE CONCEPT SIGNATURE`. If they overlap, kill it and try again.

State it in one sentence and wait for the user to confirm or refine:
*"Format kept: [hook mech + structural shape from source]. New concept: [the user's fresh idea] — anchored to [proof/system/belief]."*

User confirms or refines → lock concept. User wants a different angle → propose a second one (still just one, not a list). Don't write to Notion until the concept is locked.

### 5. Structure the beats — using the source's actual shape
Take the structural beats from the step-2 subagent's `BEAT LIST` and use them as the section headings, in the same order, at roughly the same pacing. **Do not flatten the source into a generic HOOK/BUILDUP/VALUE/PAYOFF/CTA template.** A build-in-public deep-dive has different beats than a rant, a list video, a before/after, or a day-in-the-life — and forcing them all into the same five-act mold strips out the structural reason the source worked.

Beats describe *what happens in this section*, not the words the user says. One example anchor line per beat is fine when the line is structurally load-bearing (e.g., the CTA keyword) — otherwise leave room for them to riff.

### 6. Write to Notion
Create a new page in the content database. Properties + beat-sheet body — exact spec below. The source URL goes in the **Source URL** property, and for YouTube long-form sources the thumbnail gets embedded as the first body block (see Notion Output Spec).

---

## FRESH / RAMBLE / PIPELINE (shorter)

When there's no source video, you don't get a free format model — you have to pick one. Push back on the user before generating beats from thin air:

- **FRESH** — best path is to reframe as TWIST: ask the user for a reference video that has the format/shape they want. If they refuse or genuinely have no model in mind, pick the natural beat shape for the content type (a list video has N item-beats; a rant has setup → rant → payoff; a demo has hook → setup → steps → result → CTA) and proceed. Never invent a 5-beat HOOK/BUILDUP/VALUE/PAYOFF/CTA shell on autopilot.
- **RAMBLE** — extract the core insight + emotion + ICP pain from the dump. Confirm in one line: *"Heard you saying: [insight] — going [TOF/BOF]. What viral video should I model the format off?"* If they have one, switch to TWIST. If not, pick the natural beat shape for the content type as in FRESH.
- **PIPELINE** — find the existing `Idea` page in Notion (use search, fuzzy-match title). Same rule: if the Idea page links a reference URL, treat it as TWIST. Otherwise pick the natural beat shape from the content type. **Update** that page (don't create new): set status to `Scripted`, write beats into the page body. Append, don't overwrite, if the page already has notes.

### Ideate batch payloads (no special mode — same flow as a normal call)

When invoked from `/ideate`, the args come in this shape:

```
URL: <source URL — or "none" for original-idea path>
FORMAT: Short-form | Long-form
USER PICK: <user's verbatim pick message from ideate's Step 5 prompt>
[MODE: original]   ← only present for the rare original-idea path
```

Treat this as a normal invocation — no bypass logic, no special-case branches:
- `URL` present + no `MODE: original` → TWIST mode. Step 1 still runs; if `USER PICK` already names a twist (look for "except / but / instead / make it about / with [X]"), skip the question and lock the user's twist as the concept.
- `MODE: original` (or `URL: none`) → RAMBLE mode. Use `USER PICK` as the ramble.

That's it. The handoff is just a tidier version of "user pasted a URL and said something about it" — no exotic flow needed.

---

## Beats — Derived From the Source, Not Templated

There is no fixed beat list. Beat names + count + order come from the step-2 subagent's `BEAT LIST` decomposition. Some examples of what real source-derived beat sets look like:

- **Build-in-public deep-dive:** Cold Open Claim → Proof Reel → Architecture Reveal → Live Walkthrough (N steps) → Before/After Recap → CTA
- **Contrarian rant:** Bold Claim → "Here's why everyone's wrong" → Receipt / Proof → Reframe → Action Step → CTA
- **List/listicle:** Hook + List Promise → Item 1 → Item 2 → … → Item N → CTA
- **Before/After transformation:** Setup ("here's where I started") → The Trigger → The Process → The Result → How to Replicate → CTA
- **Day-in-the-life:** Cold Open / Identity Hint → Morning beat → Work beat → Money beat → Wrap → Soft CTA
- **Demo/tutorial:** Hook + Outcome Promise → Setup → Step 1 → Step 2 → … → Result → CTA

These are illustrations, not menus to pick from. **Mirror what the actual source does.** If the source has a "Proof Reel" before the architecture reveal, the script has a "Proof Reel" before the architecture reveal. If the source has 4 walkthrough steps, the script has 4 walkthrough beats — don't collapse them into a single "Value" block.

### Per-beat structure (applies to every beat, whatever it's called)
- **Heading:** the beat name in CAPS (e.g. `PROOF REEL`, `ARCHITECTURE REVEAL`, `STEP 2 — DECOMPOSE`). Add a rough timestamp range in parens.
- **Intent line:** what mental purpose this beat serves — one short sentence, max ~12 words.
- **Direction bullets:** 2–6 bullets on what gets covered in this section.
- **Anchor (only when load-bearing):** specific number, system name, exact CTA keyword, or quote that has to land verbatim.
- **Visual cue (only when relevant):** italic-gray paragraph naming the shot or B-roll.

---

## ✂️ Readability Rule (THIS IS A HARD CONSTRAINT)

Each bullet is a **full readable sentence** that describes what happens in that beat — direction with enough context to actually use, not cryptic shorthand. The user reads this on his phone between takes, so the sheet has to flow like real script direction. Fragment-style bullets (`→ / + / = / vs` shorthand, sub-10-word headlines) were tried and failed — too cryptic to scan and act on in the moment.

### Hard rules
- **Every bullet is one complete sentence.** It should make sense read aloud. No `→`, `+`, `=`, `vs` shorthand inside bullets — save those for callout anchors, beat headings, and metadata.
- **Target ~15–25 words per bullet.** Long enough to convey both the WHAT and roughly the HOW. If a single beat naturally needs 30+ words, split it into two bullets.
- **Direction, not verbiage.** Describe what happens in this beat — what the host does, what the guest covers, what the section is for. The user says his own words on camera; you're not writing teleprompter text.
- **Quote ONLY load-bearing lines** (CTA keyword, an exact hook phrase that has to land verbatim, a specific number). Everything else stays as direction.
- **Cut meta-commentary.** No "this is what makes the video worth watching," "this earns the rest of the video," "this is the moment that justifies the hook." The user knows why the beats are there.
- **No filler adverbs.** Cut "literally," "actually," "specifically," "really," "very," "quite."

### Before/after — what wrong looks like

❌ Fragment soup (the old failure mode — too cryptic to scan as direction):
> Receipt drop: <viral-hit number> + last 60 days of reels
> Differentiator: format kept, concept new, no slop
> ID beat: <follower count, MRR, origin>. Anti-guru tone

✅ Full-sentence direction (what we want):
> Open straight to camera and drop the receipt cold — name the specific viral-hit view count and the fact that every reel in the last 60 days came through this same agent.
> Land the differentiator: this thing refuses to rewrite the source, it keeps the format and writes a completely new concept, which is why it doesn't read like AI slop.
> Quick identity beat with the follower count, MRR, and origin — anti-guru tone, in and out, no flex.

A scannable script direction beats cryptic shorthand every time. The user needs to read the bullet and know what to actually do in that beat, without having to decode it.

### Two beats that are almost always present (under different names)
- **Some kind of opening hook** — the section that earns the rest of the video. Whether it's a cold-open claim, a bold question, a proof shot, or a list promise depends on the source.
- **Some kind of CTA** — even soft CTAs (just "subscribe" or "link in bio") are beats. The CTA keyword, when one exists, is the only line that's load-bearing verbatim.

Everything else is dictated by the source.

---

## Notion Output Spec

Schema reference: `notion-pipeline.md`. Don't duplicate property shapes here — load that file for the exact write payloads.

### ⚠️ MCP gotcha — `children` takes raw objects, not stringified JSON

The `mcp__notion__API-post-page` tool's JSON schema declares `children: { items: { type: "string" } }`. **It is wrong.** The Notion API rejects strings with `body.children[0] should be an object, instead was "..."`. Pass each block as a raw JSON object in the array — same as the underlying Notion REST API expects. Do this on the first call; don't waste a round trip discovering it again.

### Property writes
| Property | Value |
|----------|-------|
| **Title** | The script title — punchy, ~6–10 words, hook-flavored. Not the source video's title. |
| **Status** | `Scripted` (TWIST/FRESH/RAMBLE create new in this status; PIPELINE flips Idea → this) |
| **Format** | `Short-form` by default. `Long-form` only if user says YouTube long-form. |
| **Type** | **Leave blank.** Jason tags this himself after reviewing the script. Never write to this field. |
| **Source URL** | TWIST mode: the source video URL goes here (including `/ideate` batch handoffs that supply a URL). Leave blank for FRESH / RAMBLE / `MODE: original`. |
| **Raw Footage** | Leave blank. This is for Jason's own raw clips later — `post-content` and `rough-cut` fill it. |

#### Page icon — always set on create

Every new page gets a single emoji icon that represents the **hook concept** — set it on the initial `API-post-page` call via the top-level `icon` field (`{"type": "emoji", "emoji": "📦"}`). Never skip; the Kanban reads icons at a glance.

Pick the emoji from what the video is actually about, not the funnel tag or format. Examples:
- Repos / tools list → 📦 · 🧰
- Money / revenue / MRR → 💰 · 💸
- Contrarian / hot take / rant → 🔥 · 🎯
- Build-in-public / system reveal → 🛠️ · ⚙️
- Numbered countdown / list → 🔟 · 📋
- Case study / member win → 🏆 · 📈
- Belief shift / reframe → 🧠 · 💡
- AI / Claude / agent angle → 🤖
- Algorithm / virality / hooks → 🎣 · 📊
- Anti-guru / call-out → 🚫 · 👀

If nothing obvious fits, pick the closest match — never default to a generic 📝 or skip the field. One emoji only.

### YouTube thumbnail (long-form sources only)

For YouTube long-form sources (Format = `Long-form`, source on `youtube.com` / `youtu.be`), embed the thumbnail as the very first body block. The title + thumbnail are the conversion levers for YT, so having the original visible in the script page makes recreation faster.

Extract the video ID from the URL:
- `youtube.com/watch?v=VIDEO_ID` → `VIDEO_ID`
- `youtu.be/VIDEO_ID` → `VIDEO_ID`
- `youtube.com/shorts/VIDEO_ID` → `VIDEO_ID` (but Shorts is short-form — skip)

Use the standard CDN URL: `https://i.ytimg.com/vi/<VIDEO_ID>/maxresdefault.jpg` (fall back to `hqdefault.jpg` if maxres 404s — rare). Embed as a Notion `image` block with `type: external`.

Skip the thumbnail block for IG / TikTok / X / Vimeo sources — they don't have stable, public thumbnail CDNs we can rely on.

### Body blocks (the beat sheet)

Two fixed framing callouts at the top, two fixed sections at the bottom (final CTA-keyword callout if applicable + Notes for the user). Everything in between is **N beats derived from the source**, each rendered with the same per-beat shape.

```
[image — external] https://i.ytimg.com/vi/<VIDEO_ID>/maxresdefault.jpg     ← only for YouTube long-form TWIST sources

[callout 💡] Format kept: <source's structural shape — name the actual beats in order>. New concept: <fresh idea> — anchored to <proof/system/belief>.
[callout 🎬] Source (format model only — concept is original): <URL>     ← only for TWIST mode

[divider]

── repeat for each beat from the step-2 subagent's BEAT LIST, in source order ──

[heading_2] <BEAT NAME IN CAPS> (<rough timestamp range>)
[paragraph] <intent — one sentence on what this beat does>
[bulleted_list] direction points
[callout 📌] Anchor: <only if beat has a load-bearing line/number/quote>     ← optional
[paragraph (italic, gray)] Visual: <shot cue>     ← optional

[divider between beats]

── after the final beat ──

[callout 🎯] Keyword: <EXACT CTA KEYWORD>     ← only if a keyword CTA is part of the format

[divider]

[heading_3] Notes for the user
[bulleted_list] Belief shift reinforced · Proof anchor · Delivery tip · Anything format-specific the user should watch for
```

### After the page is written
Reply in chat with:
- One-line confirmation: `Created "<title>" → <Notion URL>`
- Two-sentence angle summary (the twist + why it lands for the user specifically).
- Nothing else. No re-printing the beats — they live in Notion now.

---

## Voice Lock (still enforced)

The beats themselves don't need the user's exact voice (they supply that on camera) — but any anchor lines, hooks, or CTA wording you DO write must pass voice lock against `voice-dna.md`.

### Banned phrases (auto-rewrite if they slip in)
"In today's video" / "Don't forget to like and subscribe" / "It's important to note" / "Leverage" / "Harness the power of" / "Game-changing" / "At the end of the day" / "In conclusion" / "Follow for more value" / corporate hedging.

### Voice markers
Pull voice markers (slang, openers, closers, characteristic phrasings) from `voice-dna.md`. Use them sparingly in anchor lines only.

### Persona test
If a written line could come from any other creator in the niche, anchor it to a user-specific proof, system, or belief shift — or cut it.

---

## Quality Gates (silent — fix or flag, don't lecture)

1. **Anti-slop check (TWIST only — the most important gate).** The orchestrator does NOT have the source transcript (subagent kept it). Instead: scan your written beats and confirm none of them topic-overlap with the subagent's `SOURCE CONCEPT SIGNATURE`. If anything looks suspiciously close (or you're not sure), send the suspect beats back to the same subagent via `SendMessage` and ask: "Do any of these overlap with concept content from the source?" If yes, throw out the concept and re-do step 4 — keep the format, build a *different* idea.
2. **Format actually kept.** TWIST mode: does the new concept fit the same hook mechanism, structural shape, pacing, and CTA pattern as the source? If we drifted off the format, the structural reason it worked is gone — re-anchor.
3. **Anchored to the user.** At least one proof / system / belief-shift reference somewhere in the beats. If a generic creator could have written this, it's not anchored.
4. **Hook opens a loop.** If the payoff is guessable from the hook alone, rewrite the hook.
5. **Beats are scannable.** A reader scrolling on a phone in 5 seconds can see the script's shape (whatever the source's shape is) and know what each section does. Headings in CAPS, dividers between beats, intent line under each heading.
6. **Readability check.** Every bullet is a full readable sentence (~15–25 words). No `→ / + / = / vs` shorthand inside bullets. No meta-commentary. No quoted spoken lines unless load-bearing. If a bullet sprawls past ~30 words or covers two separate ideas, split it.
7. **CTA is give-first.** No begging. Comment-for-resource or DM-keyword preferred.

---

## Context Loading Rules

**Always:** `voice-dna.md`, `backbone/icp.md`, `backbone/messaging.md`, `notion-pipeline.md`.

**On request only:** `backbone/offer.md`, `backbone/vision.md`, anything in `viral-knowledge/`, research reports, performance data, full transcripts of the user's own past content.

The methodology lives in the source video itself — that's the whole point of TWIST. The backbone supplies *the user's* layer (audience, voice, beliefs); the source supplies the structural model. We don't need a generic "how to write viral scripts" overlay sitting on top of both.

Never read the entire `viral-knowledge/` folder per call. Never read `transcripts/` wholesale.

---

## What This Skill Does NOT Do

- Write word-for-word teleprompter text. (Beats only — the user riffs on camera.)
- Generate hashtags or full captions.
- Schedule or post content (use `post-content`).
- Research trends from scratch (use `research-ig-competitors` / `research-yt-competitors` / `research-yt-search` first, then feed findings here).
- Transcribe (use `transcribe-url`).
- Ask 10 clarifying questions before starting — make a call and go.
