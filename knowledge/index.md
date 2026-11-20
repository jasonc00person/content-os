---
status: compiled
last_updated: 2026-08-17
sources:
  - CLAUDE.md
  - backbone/vision.md
  - backbone/offer.md
  - backbone/icp.md
  - backbone/messaging.md
  - voice-dna.md
  - voice-corpus/index.md
  - research/
  - transcripts/url/
  - transcripts/analysis/
  - descriptions/
---

# Knowledge Index

Repo-native compiled memory. Fast navigation layer for strategy, ideation, scripting, and research synthesis. Not a source of truth: verify anything that matters against the linked source files.

Compiled 2026-08-17 against: `backbone/` (vision 2026-08-03; offer, ICP, messaging 2026-07-13), research through 2026-07-27, transcripts through 2026-07-18, shipped descriptions through 2026-08-07, `voice-dna.md` (2026-06-10, 42-entry corpus).

## Pages

- [Positioning](creator-ai-positioning.md): the current lane (leverage AI to build a viral brand and scale a business with content), the one offer (the Skool community, name/price per `backbone/offer.md`), ICP, funnel, belief shifts. Filename is fixed for `scriptwriter`.
- [Current Content Opportunities](current-content-opportunities.md): what the latest research says to make next, and what to avoid.
- [Winning Hooks](winning-hooks.md): Jason's proven openers plus the market hook shapes winning now, all proof-linked.
- [Competitor Patterns](competitor-patterns.md): what tracked handles and the algorithm are rewarding, and long-form structure lessons.
- [Reusable Script Formats](reusable-script-formats.md): the corpus-tagged formats and borrowed long-form spines for beat sheets.

## How to use

Ideation: read this file, then `current-content-opportunities.md`, then only the raw report you need (`research/`, newest first; extract text, never open a raw HTML report).

Scripting (`scriptwriter`): read `creator-ai-positioning.md`, `winning-hooks.md`, `reusable-script-formats.md`, then `voice-dna.md` and 2 to 3 few-shots via `find_voice.py`.

Hooks (`hook-generator`): `winning-hooks.md` for Jason's shapes; the 8-structure taxonomy stays in the skill's own `reference/structures.md`.

## Source rules

- `backbone/`, `voice-dna.md`, `voice-corpus/`, `research/`, `transcripts/`, `descriptions/` stay authoritative. Prices, member counts, follower counts, and MRR live only in `backbone/`; knowledge pages point there instead of repeating them.
- Never invent proof, numbers, dates, or competitor stats here without a source path.
- Retired offers (the old high-ticket install, older membership tiers, apply / DM-to-call CTAs) do not appear in these pages except to say never pitch them.
- When a source changes, run `knowledge-compile` and bump `last_updated` on the touched pages and this index.
