---
name: web-research
description: "Parallel web research across AI, creator economy, and online business trends. Spawns 6 research agents + 1 synthesizer to find trending news and generate viral hook ideas. Triggers: web research, trending news, what's happening in AI, trend research, news research, viral research, what's trending online, niche trends."
---

# Web Research — Viral Trend Scanner

Spawns 6 parallel research agents across different domains, then a synthesizer agent combines all findings into trending news + viral hook ideas for Jason's content. Output is a research report in `research/`.

## How to Trigger
- **"run web research"** or **"trend research"**
- **"what's happening in AI right now"**
- **"find trending news for content"**

## Target Audience Context
Before running, read `backbone.md` for current positioning:
- **Tier 1:** $10-40k/mo business owners who need AI systems to scale
- **Tier 2:** Beginners starting coaching businesses via Instagram
- Content should primarily attract Tier 1 (sophisticated biz owners) but TOF content can cast wider

---

## Architecture

### Phase 1 — Parallel Research (6 Agents)

Spawn 6 Agent subagents in a SINGLE message so they run in parallel. Each agent uses `WebSearch` and `WebFetch` to research its domain. Each agent should return a structured summary of the top 5-10 most noteworthy items from the past 7 days.

**CRITICAL RULES FOR RESEARCH AGENTS:**
- Every research agent prompt MUST include: "DO NOT write any files. DO NOT create reports. Return your findings as plain text only. You are a research agent — your ONLY job is to search the web and return what you found."
- Research agents must NOT generate hooks, ideas, or recommendations — they only gather raw news.
- If a research agent gets blocked (permission denied) or fails, re-run ONLY that agent. Do not restart the others.
- After ALL 6 agents return, YOU (the main agent) collect their text outputs and pass them to the synthesizer. The synthesizer is the ONLY agent that writes the final report file.

**Agent 1: AI Tools & Announcements**
- Search for: new AI tool launches, major updates (Claude, ChatGPT, Gemini, open source models), AI funding rounds, AI product shutdowns, AI drama/controversy
- Search queries: "AI news this week", "new AI tools 2026", "Claude update", "ChatGPT update", "AI startup funding", "AI controversy"
- Focus on: What's NEW (launched this week), what's CHANGING (updates/pivots), what's DYING (shutdowns/failures)

**Agent 2: Creator Economy News**
- Search for: platform algorithm changes, creator fund updates, new monetization features, big creator moves/drama, creator economy market data
- Search queries: "creator economy news", "Instagram algorithm update 2026", "TikTok update", "YouTube creator news", "content creator earnings"
- Focus on: Platform changes that affect creators, notable creator milestones or pivots, new tools/features for creators

**Agent 3: Online Business & Coaching Trends**
- Search for: coaching industry trends, online course market changes, high-ticket sales strategies, business model shifts, notable coach/consultant wins or failures
- Search queries: "online coaching trends 2026", "high ticket coaching", "online business news", "coaching industry", "digital products trends"
- Focus on: What business models are working NOW, who's scaling and how, what's falling out of favor

**Agent 4: AI in Business (Implementation Stories)**
- Search for: businesses using AI to scale, AI automation case studies, Claude Code / AI coding stories, AI replacing teams, AI ROI stories
- Search queries: "AI business automation", "Claude Code business", "AI replacing employees", "AI implementation case study", "small business AI"
- Focus on: REAL implementation stories (not hype pieces). Who built what with AI, what results did they get, what tools did they use. This is Jason's Tier 1 offer lane.

**Agent 5: Social Media Platform Updates**
- Search for: Instagram new features, TikTok news, YouTube updates, algorithm changes, policy changes, emerging platforms
- Search queries: "Instagram update April 2026", "TikTok ban update", "YouTube new features", "social media algorithm changes", "Threads update"
- Focus on: Changes that directly affect content strategy — new features to leverage, algorithm shifts to adapt to, policy changes to watch

**Agent 6: Money & Entrepreneurship Culture**
- Search for: viral money stories, entrepreneurship trends, side hustle news, economic news affecting small business, "make money online" trends
- Search queries: "entrepreneur news this week", "side hustle trends 2026", "make money online", "small business trends", "freelancer economy"
- Focus on: Stories that Jason's audience (biz owners doing $10-40k/mo) would care about. Economic shifts, tax changes, funding trends, viral success/failure stories.

### Agent Output Format

Each agent should return its findings as a structured list:

```
DOMAIN: [domain name]
DATE RANGE: [dates searched]

ITEM 1:
- Headline: [what happened]
- Source: [where you found it]
- Date: [when]
- Why it matters: [1-2 sentences on relevance to Jason's audience]
- Virality potential: [High/Medium/Low] — [why]

ITEM 2:
...
```

### Phase 2 — Synthesis (1 Agent)

After all 6 research agents return their text outputs, spawn ONE synthesizer agent. Pass it ALL 6 research outputs in a single prompt. The synthesizer is the ONLY agent that writes the report file — no other agent should touch the filesystem.

Pass it ALL the research findings plus this context:

**Synthesizer prompt context:**
- Jason's audience: Tier 1 = $10-40k/mo biz owners needing AI systems, Tier 2 = beginners starting coaching biz
- Jason's positioning: AI systems implementation expert, Claude Code power user, built setter bots / content pipelines / analytics dashboards
- Content style: Casual, direct, no-BS, pro-AI, anti-corporate, speaks from lived experience
- Content categories: TOF (reach), MOF (nurture/trust), BOF (convert/sell)

**Synthesizer tasks:**
1. **Filter** — Remove anything irrelevant to Jason's audience or positioning. Keep only items that a $10-40k/mo business owner scrolling Instagram would stop for.

2. **Rank** — Order remaining items by virality potential. Consider:
   - Is it NEW (breaking this week)?
   - Is it CONTROVERSIAL (will spark debate)?
   - Does it AFFECT the audience directly?
   - Can Jason add a UNIQUE TAKE based on his experience?

3. **Generate hooks** — For the top 10-15 trending items, create viral hook ideas:
   - **Headline/concept** — one line
   - **Hook** — the opening line (first 1-3 seconds)
   - **Jason's angle** — how he'd spin this given his expertise and positioning
   - **Format** — recommended format (talking head, screen recording, reaction, etc.)
   - **Funnel tag** — TOF, MOF, or BOF
   - **News source** — what triggered this idea
   - **Urgency** — how time-sensitive is this? (post today / post this week / evergreen angle)

4. **Identify macro trends** — What 2-3 bigger themes are emerging across multiple domains? These become content SERIES, not just one-off posts.

### Phase 3 — Write Report

Save to `research/Web-Research_YYYY-MM-DD.md` with this structure:

```markdown
# Web Research Report

**Generated:** [today] | **Research window:** Past 7 days | **Domains scanned:** 6

---

## Top Trends This Week

[3-5 bullet summary of the biggest things happening]

---

## Trending News by Domain

### AI Tools & Announcements
[Top items with headlines, sources, and relevance notes]

### Creator Economy
[...]

### Online Business & Coaching
[...]

### AI in Business (Implementation)
[...]

### Social Media Platforms
[...]

### Money & Entrepreneurship
[...]

---

## Macro Trends

### [Trend 1 Name]
[What's happening across multiple domains, why it matters, content series potential]

### [Trend 2 Name]
[...]

---

## Viral Hook Ideas

| # | Concept | Hook | Format | Funnel | Urgency |
|---|---------|------|--------|--------|---------|
| 1 | ... | ... | ... | TOF | Post today |

### Hook Details

**1. [Concept]** — [Funnel Tag] — [Urgency]
- **Hook:** "[opening line]"
- **Jason's angle:** [how to spin it]
- **Format:** [recommended format]
- **News source:** [what triggered this]

[Repeat for each hook]

---

*Research generated by 6 parallel agents + synthesizer. Data from web search.*
```

---

## Important Notes

### Agent Discipline (learned from first run)
- **Research agents must NEVER write files.** Their ONLY job is to search the web and return text. Every research agent prompt must include explicit instructions: "DO NOT write any files. Return findings as plain text only."
- **Research agents must NEVER generate hooks or ideas.** Raw news only. The synthesizer handles all analysis and idea generation.
- **The synthesizer is the ONLY agent that writes the report file.** One agent, one file, one clean write. No partial reports from research agents.
- **If one agent fails or gets blocked, re-run ONLY that agent.** Don't restart all 6. The other 5 results are still valid.

### Execution
- Spawn all 6 research agents in a SINGLE message for parallel execution
- Each research agent should use WebSearch (not WebFetch) as primary tool — only WebFetch specific URLs if needed for detail
- Time-sensitive content should be flagged with urgency level (some news is only viral for 24-48 hours)
- Don't manufacture trends — if a domain has nothing noteworthy, say "quiet week" and move on

### Output Quality
- Hooks must sound like Jason — casual, direct, confident. Not like a news anchor.
- Prioritize items where Jason has a UNIQUE ANGLE based on his actual experience building AI systems
- The report should be scannable — tables for overview, details for depth
- Aim for 15 hook ideas: ~5 TOF, ~5 MOF, ~5 BOF
