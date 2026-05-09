---
name: scriptwriter
description: "Turns a source video URL (or fresh topic / ramble / Notion Idea) into a beats-only script written straight into the Notion content pipeline. Default flow: transcribe the source, run it through the backbone to find the user's unique creative twist, then write a visually intuitive beat sheet into a new Notion page — using the source's own structural shape as the section headings (not a fixed HOOK/VALUE/CTA template). Not word-for-word — the user fills in their own expertise on camera. Triggers: write a script, script this, scriptwriter, twist this video, rewrite this reel, script out idea X, turn this ramble into a script, batch scripts."
---

# Scriptwriter — Beats Into Notion

Produces **terse beat sheets**, not teleprompter text. Each script lands as a Notion page in the content pipeline, with properties set and a body the user can scan on a phone between takes — fragments, not paragraphs.

The default play: take a video that already worked for someone else, **steal the format**, then build a **completely new concept** inside that proven structural shell. The twist is a new idea wearing a winning outfit — not the source video re-spun in the user's voice.

---

## ⚠️ The Core Principle — Format vs Concept

This is the whole game. Read it twice.

**FORMAT (copy this — it's the proven viral mechanism):**
- Hook type and mechanism (dream outcome, contrarian, curiosity gap, day-in-the-life intro, etc.)
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

### 1. Transcribe the source
- If the user gave a URL, invoke the `transcribe-url` skill. Wait for the markdown file.
- Read the transcript file from `transcripts/url/`.

### 2. Decompose the source — separate FORMAT from CONCEPT

Two columns, written silently before going further:

**KEEP (the format — this is the model):**
- Hook mechanism (dream outcome / contrarian / curiosity gap / pain point / authority hijack)
- Structural shape (day-in-the-life, list, before/after, build-in-public, rant, demo, story)
- **The actual structural beats the source uses, in order** — name them as the source's creator would (e.g. "Cold Open Claim → Proof Reel → Architecture Reveal → 4-Step Walkthrough → Free File Giveaway"). These become the headings in the Notion beat sheet. There is no fixed beat template — different formats have different beats.
- Pacing — where does each beat start/end, how long is the proof section, when does payoff drop
- The *specific* psych trick that did the heavy lifting (proof shot, mind-read, scarcity, identity assignment, etc.)
- CTA pattern

**THROW AWAY (the concept — this we replace entirely):**
- The topic / niche / claim
- All examples, numbers, names, stories
- The argument and the conclusion

The first column is the scaffold we'll build on. The second column is what we burn before step 4 — none of it survives into the twist.

### 3. Load backbone (selectively)
Always: `voice-dna.md` + `backbone/icp.md` + `backbone/messaging.md`.
Add only if relevant: `backbone/offer.md` (pricing/offer angles), `backbone/vision.md` (mission-driven content).

### 4. Build a NEW concept inside the kept format

This is where most AI script tools fail — they re-spin the source's concept in a new voice and call it a twist. That is slop. Don't do it.

Instead: take the FORMAT column from step 2, hold it fixed, and **invent a fresh concept** that fits inside it. The concept must be something the user can credibly say that **didn't appear anywhere in the source transcript**.

Generate 2–3 candidate concepts. Each must:
1. **Fit the kept format perfectly** (same hook mechanism, same structural shape, same payoff timing, same CTA pattern). If a concept doesn't fit the format, drop it — find one that does.
2. **Be anchored to something only the user has** — pull from the user's backbone:
   - Specific proof from the user's proof bank (`backbone/messaging.md` — follower counts, MRR, member wins, named viral hits)
   - A user-specific system, methodology, or tool stack named in their backbone or `voice-dna.md`
   - One of the **belief shifts** in `messaging.md` (if structured that way — count and content vary per user)
   - The user's backstory beats (origin, prior path, distinctive credentials)
3. **Pass the source-creator test:** if the original creator saw the user's video, they'd nod at the format but not recognize the idea. If they'd recognize the idea, the concept is too close — kill it and try again.

Pick the strongest. State it in one sentence:
*"Format kept: [hook mech + structural shape from source]. New concept: [the user's fresh idea] — anchored to [proof/system/belief]."*

### 5. Structure the beats — using the source's actual shape
Take the structural beats you identified in step 2 and use them as the section headings, in the same order, at roughly the same pacing. **Do not flatten the source into a generic HOOK/BUILDUP/VALUE/PAYOFF/CTA template.** A build-in-public deep-dive has different beats than a rant, a list video, a before/after, or a day-in-the-life — and forcing them all into the same five-act mold strips out the structural reason the source worked.

Beats describe *what happens in this section*, not the words the user says. One example anchor line per beat is fine when the line is structurally load-bearing (e.g., the CTA keyword) — otherwise leave room for them to riff.

### 6. Write to Notion
Create a new page in the content database. Properties + beat-sheet body — exact spec below.

---

## FRESH / RAMBLE / PIPELINE (shorter)

When there's no source video, you don't get a free format model — you have to pick one. Push back on the user before generating beats from thin air:

- **FRESH** — best path is to reframe as TWIST: ask the user for a reference video that has the format/shape they want. If they refuse or genuinely have no model in mind, pick the natural beat shape for the content type (a list video has N item-beats; a rant has setup → rant → payoff; a demo has hook → setup → steps → result → CTA) and proceed. Never invent a 5-beat HOOK/BUILDUP/VALUE/PAYOFF/CTA shell on autopilot.
- **RAMBLE** — extract the core insight + emotion + ICP pain from the dump. Confirm in one line: *"Heard you saying: [insight] — going [TOF/BOF]. What viral video should I model the format off?"* If they have one, switch to TWIST. If not, pick the natural beat shape for the content type as in FRESH.
- **PIPELINE** — find the existing `Idea` page in Notion (use search, fuzzy-match title). Same rule: if the Idea page links a reference URL, treat it as TWIST. Otherwise pick the natural beat shape from the content type. **Update** that page (don't create new): set status to `Scripted`, write beats into the page body. Append, don't overwrite, if the page already has notes.

- **IDEATE HANDOFF** — when invoked from `/ideate` with a pre-supplied concept, run the standard TWIST flow but **skip step 1's transcribe call** (ideate already transcribed in its Step 5 — read the supplied `TRANSCRIPT` path directly) and **skip step 4's candidate generation** (the concept comes in pre-formed — use it directly). Still run the source-creator test (step 4 rule 3) and anti-slop check (Quality Gate 1) — those are non-negotiable. Drop into Notion as a brand-new page in `Scripted` status (not `Idea`). Handoff payload looks like:
  ```
  URL: <source video URL — used as format model>
  TRANSCRIPT: <path to existing transcript markdown — read this instead of re-transcribing>
  CONCEPT: <fresh idea from /ideate Step 5 — the user's creative raw material>
  FORMAT: Short-form | Long-form
  ```
  If `TRANSCRIPT` is missing or the file isn't readable, fall back to step 1 (transcribe the URL). If `MODE: original` is set, skip both transcribe and decompose — write a fresh beat sheet directly from the concept ramble.

---

## Beats — Derived From the Source, Not Templated

There is no fixed beat list. Beat names + count + order come from step 2's decomposition of the source. Some examples of what real source-derived beat sets look like:

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

## ✂️ Conciseness Rule (THIS IS A HARD CONSTRAINT)

Every line on the beat sheet must be readable in **under 2 seconds at a glance**. The user is going to read this on a phone between takes — long sentences kill the format.

### Hard rules
- **Bullets are fragments, not sentences.** No subjects/verbs unless they're load-bearing. Use `→`, `+`, `vs`, `=`, abbreviations.
- **Max ~10 words per bullet.** If you need more, split into two bullets.
- **One thought per bullet.** No em-dash sub-clauses, no parenthetical add-ons, no "this is the moment that…" commentary.
- **Don't write the spoken line.** Direction, not verbiage. The user will say the words on camera, not read them off the page.
- **Quote ONLY load-bearing lines** (CTA keyword, an exact hook phrase that has to land verbatim, a specific number). Everything else is direction, not script.
- **Cut meta-commentary entirely.** No "this is what makes the video worth watching," "this earns the rest of the video," "this is the moment that justifies the hook." The user knows why the beats are there.
- **No filler adverbs/adjectives.** Cut "literally," "actually," "specifically," "really," "very," "quite."

### Before/after — what wrong looks like

❌ Verbose (what Claude defaults to):
> Drop the receipt immediately: "One script it wrote pulled 700K+ views. Every reel I've shipped in the last 60 days runs through this agent."
> Name the differentiator (this is what makes the video worth watching): "It refuses to rewrite the source. It steals the FORMAT, then writes a completely new CONCEPT in my voice. No AI slop."
> Brief identity beat — quick, not a flex: <follower count, MRR, origin>. Anti-guru tone. Then: "Let's get into it."

✅ Tight (what we want):
> Receipt drop: <viral-hit number> + last 60 days of reels
> Differentiator: format kept, concept new, no slop
> ID beat: <follower count, MRR, origin>. Anti-guru tone

Five seconds to read instead of forty-five. Same information.

### Two beats that are almost always present (under different names)
- **Some kind of opening hook** — the section that earns the rest of the video. Whether it's a cold-open claim, a bold question, a proof shot, or a list promise depends on the source.
- **Some kind of CTA** — even soft CTAs (just "subscribe" or "link in bio") are beats. The CTA keyword, when one exists, is the only line that's load-bearing verbatim.

Everything else is dictated by the source.

---

## Notion Output Spec

Schema reference: `notion-pipeline.md`. Don't duplicate property shapes here — load that file for the exact write payloads.

### Property writes
| Property | Value |
|----------|-------|
| **Title** | The script title — punchy, ~6–10 words, hook-flavored. Not the source video's title. |
| **Status** | `Scripted` (TWIST/FRESH/RAMBLE/IDEATE-HANDOFF create new in this status; PIPELINE flips Idea → this) |
| **Format** | `Short-form` by default. `Long-form` only if user says YouTube long-form. |
| **Type** | Multi-select. Always include exactly one funnel tag (`TOF` / `MOF` / `BOF`). Optionally add `Viral` or `Conversion` when the angle clearly fits. |
| **Raw Footage** | If TWIST: the source URL goes here so it's findable later. |

### Body blocks (the beat sheet)

Two fixed framing callouts at the top, two fixed sections at the bottom (final CTA-keyword callout if applicable + Notes for the user). Everything in between is **N beats derived from the source**, each rendered with the same per-beat shape.

```
[callout 💡] Format kept: <source's structural shape — name the actual beats in order>. New concept: <fresh idea> — anchored to <proof/system/belief>.
[callout 🎬] Source (format model only — concept is original): <URL>     ← only for TWIST mode

[divider]

── repeat for each beat from step 2, in source order ──

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

1. **Anti-slop check (TWIST only — the most important gate).** Open the source transcript and scan: do any of the source's specific topics, claims, examples, numbers, names, or framings appear in the new beats? If yes, this is regurgitation. Throw out the concept and re-do step 4 — keep the format, build a *different* idea.
2. **Format actually kept.** TWIST mode: does the new concept fit the same hook mechanism, structural shape, pacing, and CTA pattern as the source? If we drifted off the format, the structural reason it worked is gone — re-anchor.
3. **Anchored to the user.** At least one proof / system / belief-shift reference somewhere in the beats. If a generic creator could have written this, it's not anchored.
4. **Hook opens a loop.** If the payoff is guessable from the hook alone, rewrite the hook.
5. **Beats are scannable.** A reader scrolling on a phone in 5 seconds can see the script's shape (whatever the source's shape is) and know what each section does. Headings in CAPS, dividers between beats, intent line under each heading.
6. **Conciseness check.** Every bullet readable in <2s. No bullet over ~10 words. Fragments, not sentences. No meta-commentary. No quoted spoken lines unless load-bearing. If a bullet has an em-dash with a sub-clause hanging off it, split or cut.
7. **CTA is give-first.** No begging. Comment-for-resource or DM-keyword preferred.
8. **Type tag matches the angle.** TOF for cold-reach hooks, BOF when there's offer mention or qualified ICP filter.

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
