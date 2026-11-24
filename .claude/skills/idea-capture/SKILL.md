---
name: idea-capture
description: "Turns a video link (YouTube, Instagram reel, TikTok, any yt-dlp URL) into a fully formatted Idea page in the Notion content DB: page title = the video's title for long-form, the spoken hook for short-form, page icon = the Instagram logo (short-form) or YouTube logo (long-form), properties filled (Status Idea, Format from duration, Source URL), thumbnail as cover + inline image, and a toggle-heading body with the hook, chapter-by-chapter script structure, why it works, a twist for Jason, and the full transcript. Triggers: add this idea to notion, capture this idea, save this to notion, idea capture, add this video as an idea, notion idea from this link, log this idea."
---

# Idea Capture — link → formatted Notion Idea page

One link in, one finished `Idea` page out. No questions, no confirmation gates. Jason pastes a URL (optionally with a note), the skill pulls metadata + transcript, breaks the script down, and writes the page.

## Step 1 — Metadata (yt-dlp, one call)

```bash
yt-dlp --dump-json --skip-download "<url>" 2>/dev/null \
  | jq '{title, channel, uploader, view_count, like_count, duration, upload_date, thumbnail, description}'
```

- **Format** = `Long-form` if `duration` > 180s, else `Short-form`. Instagram reels come back with `duration: null`: read the `Duration:` line in the transcript file's header (Step 2) instead.
- **Title** (the Notion page title) depends on Format:
  - **Long-form** = `title` verbatim. Never rewrite it.
  - **Short-form** = the spoken hook, set after Step 2. IG and TikTok titles come back as "Video by <handle>", which tells Jason nothing. Take the transcript's opening sentence word for word, through its first full stop. Fix only caption garble of proper nouns and slash-codes ("/identitylog" → "/identitylock", checked against the caption). If the sentence runs past ~120 characters, stop at the end of the clause that carries the promise. A reel with no speech (music plus on-screen text) uses the on-screen hook from the first frame. Never "Video by ...", never a paraphrase.
- **Chapters**: parse `^\d+:\d+ ` lines out of `description` if present. They become the spine of the script-structure breakdown. No chapters → you segment the transcript yourself into 5-9 beats.
- **Thumbnail**: use `thumbnail` as-is for YouTube (`maxresdefault.jpg`). For IG/TikTok the yt-dlp thumbnail URL is short-lived; still use it (Notion caches external covers on first render).

## Step 2 — Transcript (reuse `transcribe-url`, never re-implement)

```bash
grep -rl "<video id or url>" transcripts/url/ || bash .claude/skills/transcribe-url/scripts/transcribe-url.sh "<url>"
```

Read the plain `## Transcript` section only (stop at `## Timestamped`). For long-form, read it in 4K-char chunks via `cut -c` rather than one giant dump.

## Step 3 — Dedupe in Notion

```bash
~/.local/bin/ntn datasources query 21bf6585-5e6b-81c2-b536-000b0adc0835 \
  --filter '{"property":"Source URL","url":{"contains":"<video id>"}}' --json \
  | jq -r '.results[] | [.id, .properties.Status.status.name, .properties.Title.title[0].plain_text] | @tsv'
```

A hit means the idea already exists: say so with the link and stop. Don't create a duplicate.

## Step 4 — Create the page (MCP `notion-create-pages`, one call)

Parent: `{"type":"data_source_id","data_source_id":"21bf6585-5e6b-81c2-b536-000b0adc0835"}` (schema in `notion-pipeline.md`).

Properties: `Title` (per Step 1: video title for long-form, spoken hook for short-form), `Status: Idea`, `Format`, `Source URL`. **Leave `Type` blank**, Jason tags funnel placement himself. `cover: <thumbnail url>`.

`icon` follows Format: `:instagram_icon:` for Short-form, `:youtube:` for Long-form (the workspace's own custom emojis, the same ones the older pages use). If the workspace has no custom emoji by that name (the create errors, or the read-back shows a different icon), pass the logo PNG instead: `https://cdn-icons-png.flaticon.com/512/2111/2111463.png` (Instagram) or `https://cdn-icons-png.flaticon.com/512/1384/1384060.png` (YouTube).

Body, in this exact order (Notion-flavored markdown; toggle headings are `## Text {toggle="true"}` with tab-indented children; quotes use `<br>` for line breaks, never raw newlines):

1. **Callout**, written as the XML tag with a tab-indented child line (attribute-list syntax on a quote does NOT make a callout, it renders as literal text):
   ```
   <callout icon="🎬" color="blue_bg">
   	[Channel](url) · views · duration · uploaded date · captured today<br>One-sentence description of what the video is.
   </callout>
   ```
2. **Thumbnail image** `![Thumbnail: "<title>"](<thumbnail url>)` so it's visible in the body, not just the cover.
3. `## 🪝 Hook (0:00 to m:ss) {toggle="true"}`: the verbatim opening line(s) as a quote, then bullets naming the hook structure (proof-first / curiosity gap / bold claim / contrarian / list promise), the stakes line, any credibility pre-empt, and the roadmap promise.
4. `## 🧱 Script Structure {toggle="true"}`: numbered list, one item per chapter/beat, `**Name (m:ss)**` then 1-2 full sentences on what happens and what the beat is doing rhetorically (pain setup, tool reveal, proof, objection handling, loop/CTA).
5. `## 🔥 Why It Works {toggle="true"}`: 4-5 bullets, each a mechanism, not a compliment ("pain before tool", "the demo is the video", "honesty chapter buys belief").
6. `## 🎯 Twist for Jason {toggle="true"}`: our version (tie to what Jason already runs; check `knowledge/` and the project memory), the differentiated angle, the 4-5 beats to steal, 2-3 rough title directions (say to run `hook-generator` for the real ones), and the single CTA (the Skool, AI Leverage Lab; never a price, never DM/apply).
7. `## 📜 Full Transcript {toggle="true"}`: the local file path in inline code, then the transcript as ONE quote block, paragraphs joined with `<br><br>`. Lightly clean caption garble of proper nouns only (e.g. "Chachib" → "ChatGPT"); don't rewrite sentences. For videos over ~4K words, condense to a faithful paragraph-per-beat abridgement and say so in the first line.

Voice for sections 3-6: Jason's. Direct, short sentences, no em dashes, no fluff. The page is for scanning on a phone between takes.

## Step 5 — Report

One line: the page link + title + Format. Nothing else. The Notion status is already `Idea`; nothing to flip.

## Gotchas

- `notion-create-pages` with `cover` wants a raw https URL, not `{{...}}` wrapped.
- Read the page back after the create (`notion-fetch`). The MCP has stored `## Heading {toggle="true"}` as literal text before; if the stored markdown shows `\{toggle`, rewrite the body with `ntn api /v1/pages/<id>/markdown -X PATCH ... </dev/null`, which makes real toggles.
- Toggle-heading children MUST be tab-indented or they render outside the toggle.
- A `>` quote breaks into separate blocks on every raw newline; use `<br>`.
- Special chars outside code spans need escaping (`\[`, `\*`, `\$` in prose). Inside code blocks, don't escape.
- Never write `Type`. Never hardcode the Skool price in the twist section.
