---
name: carousel-generator
description: "Instagram carousel generator for trend/news/post-to-carousel content. Use when Jason asks to make carousels, carousel posts, slide posts, IG carousel, turn news into a carousel, turn a competitor post into a carousel, or create an aesthetic educational/news breakdown. Fetches current sources when needed, creates a sharp Jason-voice angle, writes a slide manifest, renders polished 4:5 PNG slides locally, and saves a caption/notes package."
---

# Carousel Generator

Turns current news, trend reports, URLs, screenshots, transcripts, or rough ideas into Instagram carousel posts.

Default output:
- `carousel/outputs/<slug>/slide-01.png` through `slide-N.png`
- `carousel/outputs/<slug>/contact-sheet.png`
- `carousel/outputs/<slug>/caption.md`
- `/tmp/carousels/<slug>/carousel.json` manifest

## Core Rule

Carousels are not blog posts split into slides. Each slide gets one job:
1. Stop the scroll.
2. Make the reader curious.
3. Deliver one clean idea.
4. Create a reason to swipe.
5. Land on a CTA tied to Skool or Inner Circle.

## When User Provides a Topic Only

If the request needs current information, browse first. Use recent primary or reputable sources and capture URLs/dates in the manifest. Do not invent facts, numbers, names, pricing, or launch details.

Good sources:
- Company blogs/docs/press releases
- Official platform announcements
- Reputable tech/business publications
- Existing project research files in `research/`

For Instagram competitor/trend inputs, prefer existing reports from `research/` or run `research-ig-competitors` if the user is asking for competitor-derived ideas. Do not create an ad-hoc scraper.

## When User Provides a Post/URL

1. Resolve the content:
   - Article/news URL: read it and extract the useful claims.
   - YouTube/TikTok/Reel URL: use `transcribe-url` if a transcript is needed.
   - Screenshot/image: visually inspect and extract the hook, format, claim, and design cues.
2. Do not clone the post. Repackage the idea with Jason's opinion, creator-economy angle, and offer context.
3. Keep source URLs in the manifest and caption notes.

## Carousel Shapes

Pick one:

- **Trend Breakdown:** "X happened. Here's what creators should do."
- **Contrarian Take:** "Everyone is reading this wrong."
- **Playbook:** "Steal this workflow."
- **Warning:** "This is the trap."
- **Before/After:** "Old way vs new way."
- **Receipt Stack:** multiple source screenshots/claims leading to one conclusion.

Default length: 7 slides. Use 5 for simple takes, 9-10 for dense playbooks.

## Slide Formula

1. Cover: big hook, short subhead, trend/news label.
2. Context: what happened, in plain English.
3. Stakes: why creators/business owners should care.
4. Reframe: Jason's take or counterintuitive truth.
5. Playbook: what to do now.
6. Example: concrete application.
7. CTA: save/share/comment/Skool/DM depending on funnel.

## Voice Rules

Use Jason's voice: direct, casual, no-BS, anti-gatekeep, pro-shortcut, practical.

Avoid:
- Corporate report language.
- Fake urgency.
- "In today's fast-paced world."
- Dense paragraphs.
- Tiny footnotes as the only proof.

Strong carousel lines:
- "The tool is not the moat. The workflow is."
- "This is bad news if your content depends on being first."
- "Creators who wait for permission lose to creators who build systems."
- "Here's the move."

## Design Rules

Default format is Instagram portrait `4:5` at `1080x1350`.

Design direction:
- Editorial, premium, high contrast.
- Big type, sparse copy, strong hierarchy.
- 1-2 accent colors max.
- Use receipts, pills, counters, quote blocks, and simple charts when helpful.
- Never put more than ~45 words on a slide.
- Keep all critical text inside safe margins.

Do not rely on image models to render text. If custom background art is needed, generate it text-free, then render type locally.

## Manifest Workflow

1. Create `/tmp/carousels/<slug>/carousel.json`.
2. Include sources, slide copy, theme, and caption.
3. Render with:

```bash
python3 .claude/skills/carousel-generator/scripts/render_carousel.py /tmp/carousels/<slug>/carousel.json
```

4. Inspect the contact sheet. If text is crowded, shorten the slide copy and rerender.
5. Final output goes in `carousel/outputs/<slug>/`.

## Manifest Schema

```json
{
  "slug": "ai-agent-browser-war",
  "topic": "AI agents moving into browsers",
  "format": "4:5",
  "theme": "signal",
  "sources": [
    {
      "title": "Source title",
      "url": "https://example.com",
      "date": "2026-05-18",
      "note": "What claim this supports"
    }
  ],
  "slides": [
    {
      "type": "cover",
      "kicker": "TREND WATCH",
      "headline": "AI agents are moving into the browser",
      "subhead": "The boring-sounding shift that changes how creators build systems."
    },
    {
      "type": "point",
      "eyebrow": "01",
      "headline": "The browser is becoming the workspace",
      "body": "Your tabs, docs, DMs, calendar, and dashboards are where the actual business happens."
    },
    {
      "type": "cta",
      "headline": "Save this before you rebuild your workflow",
      "body": "Comment SYSTEM and I'll send the creator workflow map."
    }
  ],
  "caption": {
    "hook": "The next AI shift is not another chatbot.",
    "body": "Short caption body here.",
    "cta": "Comment SYSTEM if you want the workflow map."
  }
}
```

## Slide Types

Supported by the renderer:
- `cover`: kicker, headline, subhead
- `point`: eyebrow, headline, body
- `quote`: quote, attribution
- `compare`: headline, left_label, left, right_label, right
- `steps`: headline, steps array
- `stat`: eyebrow, stat, headline, body
- `cta`: headline, body

If a slide needs a layout the renderer does not support, use the closest type and keep the manifest simple.

## Caption Output

Write `caption.md` with:
- Caption text
- Sources/receipts
- Suggested alt text
- Posting notes

CTA defaults:
- TOF/news/trend: "Save this" or "Comment SYSTEM"
- MOF/workflow: Skool invite
- Premium/operator pain: DM "INNER CIRCLE"

## Quality Check

Before calling it done:
- Render completed with no errors.
- Contact sheet exists.
- Every slide is readable at phone size.
- Source claims are backed by URLs when current/news-based.
- CTA exists and ties back to the offer.
