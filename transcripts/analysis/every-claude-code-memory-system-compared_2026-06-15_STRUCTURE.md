# Script Structure: "Every Claude Code Memory System Compared (So You Don't Have To)"

**Channel:** Simon Scrapes · **Duration:** 41:21 · **Views:** 126,351
**Format:** Long-form YouTube explainer/comparison (escalating "levels" tier-list structure)
**URL:** https://www.youtube.com/watch?v=UHVFcUzAGlM

---

## Beat-by-Beat Structural Map

### 1. Cold-Open Hook — Overwhelm + "So You Don't Have To" [0:00 – 0:45]
**Function:** Stop the scroll by naming the viewer's pain (information overload) and positioning the creator as the filter who already did the work. Establishes the payoff up front.
**Content:** Rapid-fire list of competing tool names (Mem0, Karpathy's Wiki, OpenClaude, Hermes, Mem Palace, LightRAG, Claude Mem) to dramatize the chaos, then the reframe: these aren't competing tools, they're different use cases. Drops the personal credibility anchor — he's building his own "agentic operating system" — to justify why he went deep.

### 2. Promise + Roadmap [0:45 (overlaps) – 0:45]
**Function:** Set expectations and give the viewer a reason to stay to the end ("by the end you'll know exactly which one makes sense"). Plants the six-level map as a retention spine.
**Content:** Promises a walk through six levels that build on each other, all the way to cross-tool systems. Tells viewer they'll know which to use and which to ignore.

### 3. Unifying Mental Model — The One Question + Two Variables [0:45 – 1:31]
**Function:** Hand the viewer a single lens to filter everything that follows. This is the "decoder ring" beat — it makes the rest of the video feel simple and reduces cognitive load (a retention tactic).
**Content:** Every memory system answers the same question: how does Claude pull the right context at the right time? The only differences are (1) where memory lives (storage/file structure) and (2) how Claude retrieves it. All six levels get scored against these two axes.

### 4. Body — Level 1: Native Claude Code Memory [1:31 – 6:08]
**Function:** Deliver the easy, free win first to build trust and momentum (low barrier, instant value). Teach the foundational concept (context rot) that justifies every later level.
**Content:** `CLAUDE.md` as always-loaded system prompt; folder-level inheritance + local-wins-on-conflict. The over-stuffing mistake → introduces "context rot" → the 200-line rule + reference external files. Then the lesser-known `memory.md` auto-memory (the `/memory` command, per-project indexing). Closes with the leaked "Kairos" daemon as proof Anthropic is investing here (insider credibility + intrigue).
**Sub-beats:** CLAUDE.md basics [1:31], inheritance + over-stuffing [2:18], context rot + 200-line rule + auto memory [3:04], how it indexes [3:50], index demo [4:36], Kairos leak [5:22].

### 5. Transition (Pain Bridge) → Level 2 [6:08 – 6:53]
**Function:** Escalation logic — names the symptom that signals you've outgrown the current level. Each transition in this video is a "if you feel X, you need the next level" trigger.
**Content:** "If you keep repeating info Claude should already know, that's level two." Credits the source (John Connolly building on Pavel Hryn) — sourcing as credibility.

### 6. Body — Level 2: Structured Memory + Hooks [6:53 – 16:06]
**Function:** The "most people stop here" centerpiece — the longest, most hands-on demo section. Delivers the deepest practical value and a literal copy-paste recipe. This is the value core of the video.
**Content:** The `.claude/memory` structure (memory.md, general.md, domain/, tools/). SessionStart hook that auto-injects the index + team-sharing bonus. Then a full live build: copy the prompt → plan mode → Claude explores (1 of 28 projects has memory) → execute build → per-project files → introduce the PreToolUse hook → "reorganize memory" cleanup (deletes empties, resolves stale threads, adds cross-refs) → verification results (13 deleted, 9 threads finished, etc.) → register the hook.
**Sub-beats:** structured prompt [6:53], SessionStart hook + sharing [7:39], copy part one [8:26], what reorganize does [9:11], Claude explores [9:59], execute [10:44], per-project files [11:31], the hook [12:17], auto-inject [13:02], finds empties/stale [13:48], cross-refs + verify [14:34], verification results [15:20], register hook + breakdown point [16:06].

### 7. Mid-Roll CTA — Subscribe Ask [16:52 – 17:38]
**Function:** Engagement CTA placed at a natural emotional peak — right after delivering the biggest value chunk (Level 2) and just before the next escalation, so it interrupts the least. Uses a social-proof stat as the ask.
**Content:** "YouTube tells me 97% of you haven't subscribed — hit subscribe if you've made it this far." Immediately followed by a qualifying gate: only go past level two if (a) >1 month of use with grown files, and (b) you've had answers buried where Claude couldn't find them.

### 8. Transition (Scaling-Failure Bridge) → Level 3 [17:38 – 18:23]
**Function:** Escalation via the failure mode of the previous level — keyword search and a bloated general.md stop scaling.
**Content:** Names the breakdown (giant general.md, keyword search fails because it summarizes not verbatim). Introduces Level 3's lineage (OpenClaude's clean three-layer design).

### 9. Body — Level 3: Semantic Search (MemSearch) [18:23 – 23:45]
**Function:** Raise the sophistication ceiling while keeping it accessible (two-line install). Doubles as the creator's "this is what I personally use" beat — peak personal endorsement.
**Content:** OpenClaude's three layers (long-term memory.md, daily notes, "dreaming" promotion). MemSearch by Zilliz ports it in: semantic vectors + UserPromptSubmit hook auto-injecting top-3 matches. Two-line install + verify steps. Notes this mirrors his own Agentic OS. Then the contrast/alternative — Claude Mem (MCP-based, more features but overkill).
**Sub-beats:** OpenClaude three layers [18:23], MemSearch intro [19:09], vectors + hook [19:54], install [20:40], reload/verify [21:25], in action + Claude Mem [22:12], Claude Mem vs MemSearch [22:59].

### 10. Body — Level 4: Verbatim Local Recall (Mem Palace) [23:45 – 28:17]
**Function:** Escalate to "serious" power-user territory; introduce a memorable visual metaphor (memory palace) to make an abstract RAG system sticky and re-explainable.
**Content:** Word-for-word local recall — highest published benchmark, nothing summarized. The AAAK symbolic index + the "Noah" example. The wings/rooms/closets/drawers metaphor. Dual databases (SQL + Chroma), background hooks on session-end/pre-compaction, one-command install, the "mine" function. Downside: not human-readable markdown. Ends with a bridge — "everything's still local, what about ChatGPT or your phone?"
**Sub-beats:** intro [23:45], AAAK + Noah [24:30], palace metaphor [25:15], scanning speed + dual DBs [26:01], hooks + install [26:47], mining + downside [27:32].

### 11. Pivot Bridge — Reframe to a Different Problem Class [28:17 – 29:04]
**Function:** Signposts that the video is changing categories (operational memory → knowledge/cross-tool). Resets viewer expectations so Levels 5–6 don't feel like "just more of the same."
**Content:** Levels 5 and 6 aren't about remembering conversations — they're about having conversations across tools and storing connected research.

### 12. Body — Level 5: Knowledge Graphs (Karpathy's LLM Wiki / Recall / LightRAG) [29:04 – 34:26]
**Function:** Deliver value while honestly down-ranking it ("I don't think this is for most of you") — the contrarian-honesty beat that builds trust by NOT hyping everything.
**Content:** Build a connected second brain from articles/videos/podcasts. Karpathy's LLM Wiki: raw/ (Claude reads) + wiki/ (Claude owns), all markdown, visualized in Obsidian. Creator's skepticism for business use. Recall as the done-for-you hosted version + why it falls short (no data ownership, built for consumption not ops, pricing). LightRAG = enterprise overkill.
**Sub-beats:** knowledge bases [29:04], LLM Wiki structure [29:51], Obsidian + skepticism [30:36], use case + doubts [31:21], Recall [32:07], Recall shortfalls [32:53], verdict + LightRAG [33:39].

### 13. Transition Bridge → Level 6 [34:26 – 35:12]
**Function:** Re-anchors to the "everything's been inside Claude Code so far" framing and names the gap (multiple tools don't know about each other).
**Content:** Knowledge bases ≠ operational memory; but you might also use ChatGPT or Cursor, and none share memory.

### 14. Body — Level 6: Cross-Tool Memory (Open Brain / Mem0) [35:12 – 39:47]
**Function:** Cap the escalation ladder with the most "future-proof / advanced" option — gives the video a sense of completeness. Deliberately NOT demoed (manages scope, sets up follow-up content).
**Content:** Open Brain (Nate Jones) — Postgres brain on Supabase, one `thoughts` table, MCP server fronting edge functions so every tool queries the same brain. Owned + portable + cheap (10–30p/mo) but hardest to set up (~30–45 min) + latency. Mem0 as the funded production alternative (under a minute, but data on their servers). Trade-off summary.
**Sub-beats:** Open Brain intro [35:12], architecture [35:57], setup difficulty [36:44], wrap + Mem0 [37:29], Mem0 vs Open Brain [38:16], trade-offs [39:01].

### 15. Payoff — Decision Matrix / "Which Should You Pick?" [39:47 – 40:34]
**Function:** Cash the opening promise. Collapses 40 minutes into a scannable decision tree — the single most shareable/rewatchable moment.
**Content:** Just starting → L1 (10 min). Been using a while → L2 and stop. Losing old decisions → L3 (MemSearch) or L4 (Mem Palace). L5 = deep research; L6 = owned cross-tool (Open Brain / Mem0).

### 16. Resolution + Outro + Next-Video CTA [40:34 – 41:21]
**Function:** Reduce decision paralysis (they stack), restate personal endorsement (credibility close), and hand off to the next video (watch-time chaining CTA).
**Content:** Levels 1–3 stack cleanly. The creator personally runs up to Level 3 in his Agentic OS (OpenClaude conventions + semantic search + hooks). "Watch the next video to build your own Agentic Operating System. See you in the next one."

---

## Script Skeleton (Reusable Template)

> A "tier-list / escalating levels" explainer for any crowded tool/method category.

1. **Cold-Open Hook — Overwhelm:** Rapid-fire list of [N competing options] → "these aren't competing, they're [different use cases]." Drop a one-line personal-stakes credential ("I needed this for [real project], so I went deep").
2. **Promise + Roadmap:** "I'll walk through [N levels] that build on each other. By the end you'll know exactly which one fits you and which to ignore."
3. **Unifying Mental Model:** "Every option answers the same question: [core question]. They only differ on [variable A] and [variable B]." (This lens is reused to score every level.)
4. **Level 1 (the free/easy win):** Teach the foundation + the one key concept ([failure mode, e.g. context rot]) that justifies everything later. End on an intrigue hook (insider/leak/upcoming).
5. **Pain-Bridge Transition:** "If you feel [symptom], you've outgrown this — that's Level 2." Credit the source.
6. **Level 2 (the centerpiece — "most people stop here"):** Longest, most hands-on. Full copy-paste recipe + live demo with concrete numbers from the build.
7. **Mid-Roll CTA:** Subscribe ask placed right after the biggest value chunk, using a social-proof stat. Follow with a qualifying gate ("only continue if A and B are true").
8. **Levels 3 → N:** Each level = (a) failure mode of the previous level → (b) the new mechanism → (c) install/how-to → (d) an alternative tool with honest pros/cons. Insert a sticky metaphor for the most abstract level.
9. **Pivot Bridge:** When the category changes, explicitly reset expectations ("these next ones solve a different problem").
10. **Honest down-rank:** At least one level you tell people to skip — builds trust by not hyping everything.
11. **Payoff — Decision Matrix:** "If [situation] → [level]." A scannable decision tree that cashes the opening promise.
12. **Resolution + Outro:** "They stack. Personally I run [your stack]. Watch [next video] to go deeper. See you next one."

---

## Structural Notes

1. **The hook is a "filter promise," not a question.** It opens on the viewer's overwhelm (a wall of tool names) and immediately positions the creator as the one who pre-digested it — the title's "(So You Don't Have To)" is the entire value prop, delivered in the first 45 seconds. No slow ramp.

2. **A single mental model (the "one question + two variables") is the retention backbone.** Established at [0:45] and silently reused to score all six levels. It lets a 41-minute video feel navigable because the viewer always knows what axis is being evaluated. This is the highest-leverage structural choice in the script.

3. **Transitions are pain-triggered escalators, not topic switches.** Every level boundary is "if you experience [specific failure of the previous level], you need the next one." This converts a flat comparison into a felt progression and keeps the viewer self-diagnosing — they stay watching to find their own tier.

4. **The CTA is single-placed at the value peak, not the start or end.** The only subscribe ask lands at [16:52], immediately after the meatiest, most useful section (Level 2's full build) and before the next escalation — maximum goodwill, minimum interruption. The end CTA is purely watch-time chaining ("watch the next video"), not a hard ask.

5. **Front-loaded value, complexity back-loaded, payoff saved for last.** The free/easy win (L1) and the "most people stop here" recipe (L2) come early; the advanced/expensive options (L5–L6) are explicitly framed as skippable and aren't even demoed. The decision matrix at [39:47] is deliberately held to the end so the promise pays off exactly when watch-time is hardest to retain — giving committed viewers their reward.

6. **Trust is built by down-ranking, not just hyping.** Telling viewers to skip Level 5 for business use, calling Claude Mem and LightRAG "overkill," and saying "most of you should stop at Level 2" all signal the creator is optimizing for the viewer's outcome, not tool affiliate hype — which makes the personal endorsement (his own Level-3 Agentic OS) land harder.
