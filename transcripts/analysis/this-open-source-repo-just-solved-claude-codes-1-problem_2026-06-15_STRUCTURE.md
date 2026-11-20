# Script Structure: "This Open Source Repo Just Solved Claude Code's #1 Problem"

**Channel:** Chase AI · **Duration:** 13:24 · **Views:** 235,472
**Format:** Long-form YouTube tool breakdown / tutorial (explain → install → demo → wrap)
**Tool covered:** Graphiti (called "Graphify"/"Graphy" in transcript)

---

## Beat-by-Beat Structural Map

### 1. Hook / Big Claim — [0:00 – 0:24]
**Function:** Stop the scroll with a bold, specific outcome claim tied to a pain everyone in the audience feels (Claude Code's memory problem). Front-load the payoff before any setup.
**Content:** "Graphify just solved Claude Code's memory problem." Turns any repo into a knowledge graph → more accurate answers at a fraction of the token cost. Names the three magic levers up front: traverses the codebase, maps connections, discerns the *why*.

### 2. Promise + Sweeteners — [0:24 – 0:34]
**Function:** Lower resistance and stack reasons to keep watching. "Free + open source" kills the "what's the catch" objection; the promise frames the rest of the video as a deliverable.
**Content:** Best part — it's open source and completely free. "Today I'm going to show you how to get this working yourself AND what's going on under the hood."

### 3. Credibility / Social Proof — [0:34 – 0:49]
**Function:** Borrow authority from GitHub stars and reassure the viewer this isn't a niche toy. Establishes scope of what gets ingested.
**Content:** Came out a couple months ago, ~60K stars. Works with any AI coding assistant (Claude Code is just today's example). Maps code, docs, PDFs, images, videos into a queryable graph.

### 4. The "Why You Care" — Core Mental Model — [0:49 – 1:34]
**Function:** Deliver the conceptual payoff early using a dead-simple analogy so a non-technical viewer instantly "gets it." This is the retention anchor — the one idea they'll remember.
**Content:** Graph = a pre-mapped path of how A→B→C connect and *why*. Contrasts with grepping = "just doing Control+F." Graph gives Claude Code a map; grep doesn't. Therefore: fewer tokens, more accurate answers.

### 5. Curiosity Spike / Skeptic Handling — [1:34 – 1:50]
**Function:** Pre-empt the hype-skeptic, build trust by *undercutting* an inflated claim, and tee up the demo as proof. Plants a curiosity loop ("how big are the savings really?") that the demo will close.
**Content:** Some claim up to 70x savings — host says that's high, real number is lower but still significant. "You'll see when we demo it."

### 6. Transition into Mechanism — [1:50 – 2:00]
**Function:** Explicit signpost from "why" to "how." Also seeds the comparison question (RAG?) that becomes a later section.
**Content:** "That's the why you should care. Now let's talk about how it actually works." Raises: is this the same as graph RAG?

### 7. Body — How It Works (3-Pass Build) — [2:00 – 3:11]
**Function:** Deliver the core educational value as a clean, numbered list (3 passes) — easy to follow, screenshot-able, establishes the host actually understands the tool.
**Content:** Pass 1 = deterministic tree-sitter code parse (free, local, no LLM — classes, functions, imports, call graphs, comments). Pass 2 = faster-whisper transcribes audio/video. Pass 3 = LLM semantic analysis of docs/papers/images (the RAG-like pass, no true embeddings).

### 8. Body — Output Anatomy (Nodes/Edges/Communities) — [3:11 – 3:50]
**Function:** Define the vocabulary on screen so the later graph visualization lands. Re-anchors back to the "it's a map for Claude Code" payoff so the viewer never loses the point.
**Content:** Build produces nodes (circles/entities), edges (connections), communities (clusters). Reminder: we care because it's a *map* that lets Claude Code answer faster.

### 9. Anticipated-Objection Block (Q&A device) — [3:50 – 5:18]
**Function:** Mind-read the audience's two biggest questions and answer them, which raises perceived completeness and keeps the technical viewer from bouncing. Doubles as a buying-guide ("when do I use this vs. that").
**Content:** Q1 — "What if there's no code, just markdown?" → Yes, can export to an Obsidian vault (teased for the end). Q2 — "How is this different from graph RAG (LightRAG / RAG-Anything / Microsoft GraphRAG)?" → No embeddings; best for structured codebases. RAG wins for huge unstructured document sets (e.g., policy docs). The line is murky — pass 3 makes it "RAG-light."

### 10. Mid-Roll Sponsor (self-promo) — [5:18 – 5:48]
**Function:** Monetization break, placed *after* the conceptual payoff but *before* the hands-on demo — so it sits at a natural seam where curiosity ("does it actually work?") pulls the viewer through the ad.
**Content:** "A quick word from today's sponsor — me." Pitches the Claude Code Masterclass inside Chase AI Plus (weekly updates, Codex + Claude OS masterclasses). Link in pinned comment.

### 11. Install Walkthrough — [5:48 – 6:30]
**Function:** Remove friction / "it's easy" reassurance. Converts the abstract tool into something the viewer believes they can actually set up in minutes.
**Content:** Easiest path: copy the Graphify GitHub link, paste into Claude Code, say "install Graphify for me." Manual steps exist if preferred. Platform-agnostic.

### 12. Commands Overview (with a relief valve) — [6:30 – 7:38]
**Function:** Show depth/power ("there's a lot here") without overwhelming — then immediately defuse the overwhelm so the viewer doesn't feel they must memorize anything.
**Content:** Many commands — you won't remember them, and you don't have to: install ships a "Graphify skill" that teaches Claude Code which command to run from natural language. Key ones: `/graphify .` (build), `graphify query`/`explain` (force graph use), `graphify claude install` (always-on hook), Obsidian flag.

### 13. Demo Setup — [7:38 – 8:05]
**Function:** Establish the test subject and stakes so the upcoming numbers feel credible (real, "relatively large" codebase, not a toy).
**Content:** Pointing Claude Code at Open Design ("Claude Design but open sourced"). Cloned locally, run `/graphify .` on the whole folder.

### 14. Demo — Build Results — [8:05 – 8:40]
**Function:** Deliver concrete proof-of-work numbers; the specificity sells legitimacy. Introduces extra outputs (god nodes, surprising connections, suggested questions) as bonus value.
**Content:** ~6 min run: 203 files → 1,907 nodes, 3,447 edges, 109 communities, ~120K output tokens. Lists "god nodes" (most prominent), surprising connections, suggested questions.

### 15. Demo — Graph Visualization — [8:40 – 9:20]
**Function:** Visual payoff (the "wow" shot promised in the hook) — *then* deliberately deflates it to redirect attention to the real value. Stops the viewer from fixating on eye-candy over utility.
**Content:** Brings up the graph: communities/clusters, nodes (dots), edges (lines); click a node → type, community, source, neighbors. "As cool as this looks, the real value is that we've handed Claude Code a *map*."

### 16. Payoff — Head-to-Head Token Test (Proof) — [9:20 – 11:00]
**Function:** This is the climax — it closes the curiosity loop opened in beat 5 (the "70x?" question) with a controlled A/B test. Same question, two tabs, real token counts. Proof beats claims.
**Content:** Question: "Trace how a design request flows from the web app to a coding agent and back." Tab A = use Graphify (skill loads, `graphify query`). Tab B = no Graphify → Claude spawns 2 explore agents, burns 100K tokens immediately. Same correct answer both ways. Tally: ~200K tokens (grep) vs. ~80K (graph) ≈ 40% of the cost. Caveat noted: once grep has crawled, follow-up questions get cheaper.

### 17. Resolution — The "Memory" Payoff — [11:00 – 11:20]
**Function:** Tie the demo result back to the hook's exact promise ("solved the memory problem") — closing the macro loop opened at 0:00.
**Content:** Because the graph is built, you can query it cheaply again and again — that's the persistent "memory" piece.

### 18. Objection Handling — "Living Repo" — [11:20 – 12:10]
**Function:** Kill the strongest remaining doubt (does it go stale?) before the viewer can raise it. Reinforces the "free" value prop with the AST-only, no-API-cost rebuild.
**Content:** `graphify hook install` → auto-rebuilds after each commit, AST-only, no API cost, deterministic. Works in team/parallel-dev setups. Result: a persistent yet living map.

### 19. Future Tease + Positioning — [12:10 – 12:47]
**Function:** Open a forward loop to the next video (Obsidian) and place the tool on a mental spectrum so the viewer files it correctly. Drives the channel's content series.
**Content:** Obsidian flag → works on non-code repos too (full walkthrough in a future video). Positions Graphify between Obsidian and a true RAG system — a "middle-ground" memory tool.

### 20. Philosophical Wrap + CTA + Outro — [12:47 – 13:24]
**Function:** Zoom out to a reassuring takeaway ("more tools = better choices"), then stack the calls to action and tease the next touchpoint to keep the relationship going.
**Content:** More options = pick the right tool for the job; don't force Obsidian or a giant RAG build. CTAs: comment your thoughts; check Chase AI Plus / Claude Code Masterclass; free Obsidian + Claude Code webinar next week (link below). "I'll see you around."

---

## Script Skeleton (reusable template)

A fill-in-the-blank outline for a "tool breakdown" long-form video:

1. **Hook / Big Claim** — "[TOOL] just solved [WIDELY-FELT PAIN]." State the headline outcome in one sentence, name the 2-3 mechanisms that make it work.
2. **Promise + Sweetener** — "Best part: it's [free/cheap/easy]. Today I'll show you how to set it up AND what's happening under the hood."
3. **Credibility** — borrow proof (stars / users / funding / who's using it) + define scope of what it handles.
4. **Core Mental Model** — explain the ONE idea with a dead-simple analogy ("it's like [familiar thing] vs. [bad old way]"). This is your retention anchor.
5. **Curiosity Spike** — name an inflated claim about the tool, undercut it slightly ("real number is lower but still big"), promise the demo will prove it. (Opens a loop.)
6. **Signpost transition** — "That's the why. Now here's how it works."
7. **Mechanism (numbered)** — break the how into 3-ish clean numbered steps/passes.
8. **Vocabulary / Output anatomy** — define the terms the viewer will see in the demo; re-anchor to the core payoff.
9. **Anticipated Objections (Q&A)** — voice the audience's top 1-2 questions, answer each, include a "when to use this vs. alternatives" buying guide.
10. **Mid-roll sponsor** — placed at the seam right before the hands-on demo (curiosity pulls them through the ad).
11. **Install / Setup** — "easiest path is X; manual path exists." Sell "it's easy."
12. **Commands / Features overview + relief valve** — show depth, then reassure they don't have to memorize it.
13. **Demo setup** — name a real, non-trivial test subject; state the stakes.
14. **Demo results** — concrete numbers/proof-of-work.
15. **Visual payoff → redirect** — show the cool artifact, then point back to the actual value.
16. **Climax: head-to-head proof** — controlled A/B (with vs. without), real metrics, close the curiosity loop from step 5.
17. **Resolution** — tie the result back to the exact words of the hook.
18. **Objection handling** — kill the strongest remaining doubt (does it scale / go stale / cost money?).
19. **Future tease + positioning** — open a loop to the next video; place the tool on a mental spectrum.
20. **Wrap + stacked CTA + outro** — zoom-out takeaway, then comment CTA + product CTA + next-touchpoint CTA.

---

## Structural Notes

- **The hook front-loads the entire payoff, then the body re-earns it.** The very first sentence states the outcome ("solved the memory problem") and names the mechanisms. The whole video is structured as a loop that opens at 0:00 and is explicitly closed at 11:00 ("that's the memory piece") and again in the wrap — nothing is held back as a mystery, the tension is "does it actually deliver?" not "what is it?"

- **Two nested curiosity loops drive retention to the demo.** The macro loop (does it solve the memory problem?) spans the whole video. A tight micro loop is planted at 1:34 ("people claim 70x — I'm skeptical, you'll see") and isn't resolved until the token test at ~10:18. That single skeptical line is what makes a viewer sit through 8 minutes of mechanism to reach the proof.

- **Sponsor placement is surgical.** The ad sits at 5:18 — exactly between the conceptual half ("here's what it is and how it works") and the hands-on half ("now let's actually run it"). The viewer has just been told a demo is coming, so the unresolved "does it work?" tension carries them through the ad instead of bouncing.

- **Proof is shown, not asserted — and the host's credibility comes from under-claiming.** Rather than repeating the "70x" hype, he runs a real A/B test and lands on a modest ~40%-of-cost (≈2.5x) result, even adding the honest caveat that grep gets cheaper on follow-ups. Undercutting the hype is the trust move that makes the rest of the video believable.

- **Anticipated-objection blocks do the heavy lifting.** Two full sections (RAG-vs-Graphify at 3:50, living-repo at 11:20) exist purely to answer questions before the viewer asks them. This is what makes a 13-minute explainer feel "complete" rather than salesy, and it's where the comparison/buying-guide value lives.

- **CTAs are layered and back-loaded, never interrupting the value.** The only mid-video ask is the single sponsor break. Everything else — comment, masterclass, next-video tease, webinar signup — is stacked into the final 35 seconds, plus a forward-loop tease (Obsidian video) that converts this video's audience into the next video's audience.
