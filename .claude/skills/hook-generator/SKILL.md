---
name: hook-generator
description: "Crafts proven, scroll-stopping video hooks from real performance data. Short-form (reels/TikTok/Shorts): a 404-hook bank of top-performing reels ranked by views — Claude diagnoses which of the 8 hook structures fit, pulls the highest-performing frameworks, and writes a spread of spoken hooks in Jason's voice, each anchored to a real framework with view-count proof. Long-form (YouTube): the hook IS the title, so it writes title options instead — retrieved from title-corpus/titles.json (every title on Jason's channel + all tracked competitors, scored by breakout = views ÷ that channel's median), matched by archetype and keyword, each option citing the real title it's modeled on. Triggers: write a hook, write me a hook, hook for this video, hook for my video, generate hooks, give me hooks, hook ideas, viral hook, scroll stopper, opening line, hook generator, need a hook, what's a good hook for, title options, youtube title, write a title, title ideas, title for this video, what should I call this video, better title, retitle."
---

# Hook Generator — proven hooks from real viral data

Jason brings a video idea (a topic, a rough concept, or a full script he already
wrote). Claude turns it into a set of **spoken hooks** — the first 3–5 seconds the
host says on camera — each one built on a framework that already went viral, in
the creator's own voice (`voice-dna.md`), tied to the positioning in `backbone/messaging.md`.

The edge is the data. Two banks, one per format:

- **Short-form → `404-kallaway-hooks.csv`**: 404 spoken hooks from top-performing
  reels, tagged with structure, framework, source, and **view count**.
- **Long-form → `title-corpus/titles.json`**: every title on Jason's own channel
  plus every tracked YouTube competitor (~2.7K titles), each scored by
  **breakout** = views ÷ that channel's median, so a small channel's outlier
  ranks above a big channel's average day.

We don't invent hook shapes from vibes — we pull the proven ones and pour Jason's
idea into them. **First decide the format** (Step 0), because the two banks don't
transfer: a line that stops a thumb on Instagram is not a line that wins a click
against eleven other thumbnails on the YouTube home feed.

## The Flow

```
0. FORMAT   — short-form (spoken hook) or YouTube long-form (title)? Decides the bank.
1. GATHER   — take Jason's idea / script / topic. Distill the core payoff.
2. DIAGNOSE — short: pick 3–4 hook structures (reference/structures.md).
              long:  pick 3–4 title archetypes (find_titles.py --list).
3. PULL     — short: find_hooks.py → proven frameworks + view proof.
              long:  find_titles.py → proven titles + breakout proof (own winners first).
4. WRITE    — short: 6–8 spoken hooks.  long: 5–6 titles. Creator's voice either way.
5. DELIVER  — options with the proof behind each; recommend one.
```

## Step 0 — Decide the format

Ask nothing; read it off the request. "Reel", "short", "TikTok", "hook for my
video" with a 30–90s idea, or a beat sheet marked short-form → **short-form**, run
Steps 1–5 as written. "YouTube video", "long-form", "title", "what should I call
it", or a Notion beat sheet in the long-form format → **long-form**, run Steps 1–5
but with the **Long-form** substitutions in each step. Never write a spoken hook
for a long-form video or a title for a reel.

## Step 1 — Gather the idea

Take whatever Jason gives you:
- **A full script / beat sheet** → the hook is the opening line; read the whole
  thing so the hook matches the payoff the video actually delivers.
- **A rough concept** (e.g. "a video about the one habit that doubled my output") →
  that's enough; pull the core transformation.
- **Just a topic** (e.g. "systems that save time") → make a reasonable read of the
  angle through the niche on the CLAUDE.md Creator Profile "Niche" line, state it
  in one line, and generate. Don't interrogate Jason — he'll redirect if it's off.

Find the **core** before writing: what's the payoff, the surprise, the enemy, or
the number? A hook is a promise the rest of the video keeps — you can't write the
promise until you know the payoff.

## Step 2 — Diagnose the structures

Read [reference/structures.md](reference/structures.md) and pick the **3–4
structures** that best fit this idea. The 8: Educational/Tutorial, Secret Reveal,
Contrarian/Negative, Raw Shock, Question, Experimentation, Fortuneteller,
Comparison. Quick map:

- Showing a system / how-to → **Educational**, **Secret Reveal**
- Hot take / picking a fight → **Contrarian**, **Question**
- A result that sounds fake → **Raw Shock**, **Comparison**, **Experimentation**
- Belief shift / story → **Fortuneteller**, **Secret Reveal**

Aim for a *spread* of distinct angles, not four flavors of one line.

**Long-form:** archetypes replace structures. Run
`python3 .claude/skills/hook-generator/scripts/find_titles.py --list` and read the
table (archetype, count, median breakout, how many hit ≥3x, best example). Pick
3–4 that fit the idea. The tags are regex heuristics on the title text
(`experiment` = "I taught/let/made/replaced…", `news-shock`, `cost`, `warning`,
`versus`, `course`, `listicle`, `how-to`, `outcome`, `question`); the numbers next
to them are real. Prefer archetypes with a high **≥3x** count over a high median
alone: outliers are what you're modeling, not the typical case.

## Step 3 — Pull the proven frameworks

The bank is the source of truth. Query it — never eyeball the raw CSV. Run from
the repo root (`python` on Windows):

```bash
python3 .claude/skills/hook-generator/scripts/find_hooks.py --list                          # the 8 + counts
python3 .claude/skills/hook-generator/scripts/find_hooks.py --structure "secret" --top 15   # top in one structure
python3 .claude/skills/hook-generator/scripts/find_hooks.py --structure all --top 3         # a spread across all 8
python3 .claude/skills/hook-generator/scripts/find_hooks.py --keyword ai --top 20           # topic-anchored search
python3 .claude/skills/hook-generator/scripts/find_hooks.py --structure question --keyword money
```

Pull frameworks for the structures you picked in Step 2. If the idea has a strong
topical anchor (a word from your niche: money, build, content, ai...), add
`--keyword` to surface hooks from adjacent topics — their *shape* transfers even
when the subject doesn't. Results are pre-ranked by performance (rank 1 ≈ 9.5M avg
views), so the top of each list is the strongest proof.

**Long-form:** same idea, other bank. Three pulls, in this order:

```bash
python3 .claude/skills/hook-generator/scripts/find_titles.py --own --top 10                      # 1. Jason's own winners — his audience's CTR, outranks everything
python3 .claude/skills/hook-generator/scripts/find_titles.py --keyword "motion,animation" --top 15   # 2. topic-adjacent titles across the corpus (comma = OR)
python3 .claude/skills/hook-generator/scripts/find_titles.py --archetype experiment --top 10      # 3. one call per archetype picked in Step 2 (or --archetype all --top 20 for a spread)
```

Extras: `--days 120` (what's breaking out lately; news-shock titles rot in weeks),
`--handle nateherk` (one competitor), `--pattern "^I (taught|let)"` (regex),
`--min-breakout 3` (outliers only). Every row prints `[breakout] views  month
archetype @handle` (★ = own channel) so the proof travels with the title. Never
open `titles.json` directly; it's 800KB.

## Step 4 — Write the hooks

For each hook: take a proven **framework** (the `[X]/[Y]` template) and pour
Jason's idea into it. **Keep the framework's shape and rhythm** — that's the part
that's proven — and swap in Jason's specifics.

Voice and positioning come from the repo, never from this file:

- **Voice = `voice-dna.md`** (fallback: the Voice/Tone one-liner in the CLAUDE.md
  Creator Profile). Positioning and any real number = `backbone/messaging.md`
  (its proof bank). Never invent a register, a slang set, or a stat.
- **Own winners.** If `knowledge/winning-hooks.md` exists, read it: it holds hook
  shapes that already worked for this creator and outranks a generic bank row of
  the same shape.
- **Spoken, not written.** This is a line Jason *says* in the first 3 seconds, not
  a caption. Sounds like a FaceTime with a friend. (Short-form = spoken hook. If
  the idea is YouTube long-form, frame it as a **title** paired with the thumbnail
  instead; never substitute one for the other.)
- **Make them feel behind or surprised in 3 seconds.** Name the enemy the offer
  removes (see `backbone/offer.md`), drop a real number from the proof bank, or
  open a curiosity loop.
- **Don't jam the CTA into the hook.** The hook earns the watch; the offer ask
  (`backbone/offer.md`) comes later in the script. Don't drop a CTA by accident.

**Long-form titles, in addition:**
- **Model the shape, swap the subject.** "I taught Claude how to use Premiere Pro
  and it's INSANE." (32x, own) → "I Taught Claude to Make Vox-Style Motion
  Graphics". Keep the verb, the tension, the length; change the noun.
- **Own winners beat corpus winners.** A 30x on Jason's channel is his audience
  clicking. A 30x on a competitor is proof the topic works in the niche. Cite which.
- **Comment data is an archetype source too.** If `yt-comment-mining` surfaced a
  recurring objection ("looks like AI slop"), a title that answers it is a
  `warning`/`news-shock` play with proof nobody else can copy. Say so in the proof line.
- **Under ~60 characters, thumbnail does the other half.** Don't stuff the title
  with what the thumb will show. Parenthetical qualifiers ("(No WSL)", "(Full
  Setup)") are the one exception; the corpus shows them working on Jason's channel.
- **No numbers Jason doesn't have.** A "$3,000" title needs a real $3,000 in the
  script. `backbone/messaging.md` is the only source for a stat.

## Step 5 — Deliver

Present **6–8 hooks** in chat, grouped/labeled by structure so Jason sees distinct
angles. For each, show the line + the framework it's built on + the source's view
count (that's the trust signal — he asked for *proven* hooks). Format (the lines
below are illustrative; write your own from your niche):

```
**Option 1 — Secret Reveal**
"Nobody fumbled a bag harder than people still doing [the manual thing] by hand in 2026."
↳ framework: "Nobody [X failed action] harder than [Y example]" · 17.7M views (@frankmichaelsmith)

**Option 2 — Question**
"Is there any way for a one-person team to [the outcome]? Watch."
↳ framework: "Is there any way for [X] to [Y achieve goal]?" · 1.59M views (@codiesanchez)
```

If a hook is built on one of your own past winners instead of a bank row, cite it
as `↳ from your own winners (knowledge/winning-hooks.md)`.

**Long-form:** present **5–6 titles**, labeled by archetype, each with the corpus
title it's modeled on and that title's breakout + views + handle:

```
**Option 2 — experiment**
"I Taught Claude to Make Vox-Style Motion Graphics"
↳ modeled on: "I taught Claude how to use Premiere Pro and it's INSANE." · 32.2x · 58K · @jasoncooperson ★
```

Recommend one and say why in a line (own-channel proof > competitor proof >
archetype median). The chosen title becomes the working title in Notion via
`scriptwriter`.

End with a one-line **recommendation** (which to lead with and why). Then it's
Jason's pick — the chosen hook hands off to scripting.

## Rules

- **Data first, vibes second.** Every hook traces to a framework in the bank (or a
  hook from your own winners in `knowledge/winning-hooks.md`, when that file
  exists). Don't invent hook shapes from memory.
- **Query, don't read.** Use `find_hooks.py` / `find_titles.py` to slice the banks.
  Never dump the 171KB CSV or the 800KB `titles.json` into context.
- **Right bank for the format.** Reels never get titles from `titles.json`;
  YouTube long-form never gets spoken hooks from the CSV. Step 0 decides, once.
- **Stale corpus, say so.** `find_titles.py` prints the build date. If it's older
  than ~90 days, mention it and suggest `python3 title-corpus/build.py` (30s);
  don't run it mid-session unless asked.
- **Spoken line, not caption.** The artifact is what Jason says out loud (or, for
  YT long-form, the title). Never substitute a text overlay or caption.
- **Spread the angles.** 3–4 structures, distinct hooks — variety to pick from.
- **Voice is non-negotiable.** If a hook reads like LinkedIn, rewrite it. Pull from
  `voice-dna.md`, not a generic "viral" register.
- **The hook is a promise.** It must match the payoff the video actually delivers —
  no bait the script can't cash.

## Files

| Path | What it is |
|------|------------|
| `404-kallaway-hooks.csv` | The proven-hook bank — 404 hooks, ranked by views. Source of truth. Query via the script; don't read raw. |
| `scripts/find_hooks.py` | Slices the bank by structure / keyword, returns top frameworks + proof. |
| `scripts/find_titles.py` | Long-form: slices `title-corpus/titles.json` by archetype / keyword / handle / age, ranked by breakout. `--list` for the archetype table. |
| `../../../title-corpus/titles.json` | The long-form bank (repo root). Built by `title-corpus/build.py` from yt-dlp flat playlists: own channel + every `## YouTube` handle in `competitor-list.md`, newest 400 each, breakout-scored per channel. Rebuild quarterly or when a batch of winners lands. |
| `reference/structures.md` | The 8 structures explained — trigger, best-for, your angle, top proof. Read this to pick structures. |
