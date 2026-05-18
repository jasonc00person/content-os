---
name: knowledge-compile
description: "Refreshes the repo-native compiled knowledge layer in knowledge/. Reads new research reports, transcripts, backbone docs, viral-knowledge, and skill learnings, then updates short source-linked markdown pages used by ideate and scriptwriter. Triggers: update knowledge, compile knowledge, refresh repo memory, update the wiki, Karpathy layer, knowledge layer."
---

# Knowledge Compile

Maintains the repo's lightweight Karpathy-style knowledge layer without Obsidian.

The goal is not to create another vault. The goal is to stop re-reading 100k+ words of scattered transcripts, reports, and playbooks every time Jason asks for strategy, ideas, or scripts.

## Folder Contract

```
knowledge/
├── index.md
├── current-content-opportunities.md
├── winning-hooks.md
├── competitor-patterns.md
├── creator-ai-positioning.md
└── reusable-script-formats.md
```

## Source Hierarchy

Authoritative sources:

1. `backbone/`
2. `voice-dna.md`
3. `viral-knowledge/`
4. `research/`
5. `transcripts/`
6. `.claude/skills/`

Compiled outputs:

- `knowledge/`

Never treat `knowledge/` as the source of truth. It is a fast navigation and synthesis layer.

## When To Run

- After a new research report lands.
- After transcribing a high-signal competitor/video.
- After a major offer, positioning, or pipeline change.
- Before a big ideation block if the latest research is not reflected in `knowledge/`.

## Refresh Workflow

1. Read `knowledge/index.md`.
2. Check newest files in `research/`, `transcripts/url/`, `backbone/`, `viral-knowledge/`, and `.claude/skills/`.
3. Compare the latest source dates against each knowledge page's `last_updated`.
4. Update only pages affected by new signal.
5. Keep each page short. It should be faster to read than the raw source.
6. Include local source paths in frontmatter and inline where useful.
7. Do not add claims, numbers, or dates without a source path.

## Page Roles

- `current-content-opportunities.md`: latest actionable content angles.
- `winning-hooks.md`: reusable hook mechanics.
- `competitor-patterns.md`: what competitors are doing that keeps working.
- `creator-ai-positioning.md`: Jason's market lane, offer, voice, and belief shifts.
- `reusable-script-formats.md`: script shapes that should feed `scriptwriter`.

## Usage Rules For Other Skills

`ideate` should read `knowledge/index.md` and `knowledge/current-content-opportunities.md` before opening raw reports.

`scriptwriter` should read `knowledge/creator-ai-positioning.md`, `knowledge/winning-hooks.md`, and `knowledge/reusable-script-formats.md` before opening full transcripts or long playbooks.

Research skills should continue writing raw reports to `research/`. They should not write directly into `knowledge/` unless explicitly running this skill afterward.
