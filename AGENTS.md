# AGENTS.md

This workspace is a content operating system. Claude Code is the original runner, but Codex and other agent harnesses should use the same project conventions.

## Canonical Skill Registry

Project skills live in `.claude/skills/`.

Do not move, rename, or duplicate these folders for Codex. Treat `.claude/skills/<skill-name>/SKILL.md` as the source of truth for each workflow, and use any scripts/assets inside that skill folder.

Current skills:

- `research-ig-competitors`
- `research-yt-competitors`
- `research-yt-search`
- `ideate`
- `scriptwriter`
- `transcribe-url`
- `rough-cut`
- `audio-polish`
- `reframe`
- `broll`
- `captions`
- `thumbnail`
- `post-content`

## How Codex-Style Agents Should Use Skills

When the user names a skill, uses a trigger phrase from a skill description, or asks for a pipeline step listed in `CLAUDE.md`:

1. Open the matching `.claude/skills/<skill-name>/SKILL.md`.
2. Follow that file's workflow and folder contract.
3. Load only the supporting files needed for the task.
4. Prefer scripts inside the skill's `scripts/` folder over reimplementing the workflow.
5. Keep generated intermediates in the locations defined by the skill.

If a skill needs secrets, APIs, paid generation, network access, or long-running commands, use the active harness's permission flow before executing.

## Primary Pipeline

Use `CLAUDE.md` as the high-level map of the content system. The main pipeline is:

1. Research: `research-ig-competitors`, `research-yt-competitors`, `research-yt-search`
2. Ideation: `ideate`
3. Scripting: `scriptwriter`
4. Filming: Jason
5. Rough Cut: `rough-cut`
6. Audio Polish: `audio-polish`
7. Reframe: `reframe`
8. B-Roll: `broll`
9. Captions: `captions`
10. Thumbnail: `thumbnail` (YouTube optional)
11. Posting: `post-content`

## Runner-Specific Notes

- Claude Code may auto-discover `.claude/skills` and uses `.claude/settings.json` for permissions.
- Codex may not auto-discover `.claude/skills`; this file is the bridge. Read the relevant `SKILL.md` manually when needed.
- Model names such as GPT-5.5 or Claude are not the skill system. The harness supplies files, tools, permissions, and any native skill discovery.

## Editing Rules

- Keep skill documentation and scripts together inside `.claude/skills/<skill-name>/`.
- Do not add a parallel `.codex/skills` tree unless the user explicitly asks for a native Codex packaging experiment.
- If a workflow changes, update the matching `SKILL.md`, scripts, and any references in `CLAUDE.md` or this file.
- Do not delete research reports, transcripts, or video-editor outputs unless the user explicitly asks.

## Imported Claude Cowork project instructions
