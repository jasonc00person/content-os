---
# Every Claude Code Memory System Compared (So You Don't Have To)
**Channel:** Simon Scrapes  ·  **Published:** 2026-04-23  ·  **Duration:** 41:21  ·  **Views:** 126,351
**URL:** https://www.youtube.com/watch?v=UHVFcUzAGlM
---

## Summary
A practical tour of every major memory system for Claude Code, organized into six escalating "levels" that build on top of each other rather than competing. The creator frames the whole space around one question — when you give Claude Code a task, how does it pull the right context at the right time? — and breaks each option down by where memory lives (storage/file structure) and how Claude retrieves it. He demos the native `CLAUDE.md` + auto `memory.md` (level 1), John Connolly's hook-based structured memory built on Pavel Hryn's concept (level 2), the OpenClaude-derived semantic MemSearch plugin (level 3), verbatim local RAG via Mem Palace (level 4), Karpathy's LLM Wiki / Recall knowledge graphs (level 5), and cross-tool Postgres brains like Open Brain and Mem0 (level 6). His own recommendation: most people should stop at level 2; he personally runs up to level 3 in his Agentic OS.

## Key Points
- Every memory system answers the same question (right context at the right time); they differ only on storage location and retrieval mechanism.
- **Level 1 — Native (free, already on):** `CLAUDE.md` is always loaded; keep it under ~200 lines and reference external files for big context to avoid "context rot." `memory.md` auto-memory quietly indexes per-project notes. Anthropic is reportedly building an always-on consolidation daemon ("Kairos," found in a leaked source).
- **Level 2 — Structured + hooks (John Connolly / Pavel Hryn):** A prompt added to `CLAUDE.md` builds a `.claude/memory` structure (general/domain/tools files), a SessionStart hook auto-injects the `memory.md` index, and a "reorganize memory" command de-dupes and consolidates. The creator says most people should stop here.
- **Level 3 — Semantic search (MemSearch by Zilliz):** Ports OpenClaude's markdown-first three-layer design (long-term `memory.md`, daily notes, "dreaming" promotion) into Claude Code; chunks docs into vectors and uses a UserPromptSubmit hook to inject the top 3 semantic matches automatically. Two-line install. Claude Mem is a similar-but-heavier MCP-based alternative he considers overkill.
- **Level 4 — Verbatim local recall (Mem Palace):** A free, local RAG that stores conversations word-for-word, indexed in a dense symbolic "AAAK" language using a memory-palace metaphor (wings/rooms/closets/drawers) over SQLite + Chroma. Hooks fire on session-end/pre-compaction; downside is it's not human-readable markdown.
- **Level 5 — Knowledge graphs (Karpathy's LLM Wiki / Recall / LightRAG):** For building an interconnected "second brain" from articles, videos, podcasts — `raw/` (Claude reads) + `wiki/` (Claude owns), all markdown, visualized in Obsidian. Recall is the done-for-you hosted version; LightRAG is enterprise overkill. He thinks these are for research, not operational memory.
- **Level 6 — Cross-tool memory (Open Brain by Nate Jones / Mem0):** A Postgres brain (on Supabase) with a single `thoughts` table that every AI tool — Claude Code, ChatGPT, Cursor, Claude Desktop — queries via MCP. Most future-proof and portable (~10–30p/month), but hardest to set up (~30–45 min) and adds latency. Mem0 is the production-ready, well-funded alternative but stores data on their servers.
- **How to choose:** Just starting → level 1. Been using Claude Code a while → level 2 and stop. Losing old decisions across months → level 3 (MemSearch) or level 4 (Mem Palace). Want cross-tool/owned data → level 6 (Open Brain or Mem0).
- Levels 1–3 stack cleanly together; the creator runs up to level 3 in his own Agentic Operating System.

## Full Transcript

Right now, if you search for the best Claude Code memory system, you get absolutely buried. Mem0, Karpathy's Obsidian Wiki, OpenClaude, Hermes, Mem Palace, LightRAG, Claude Mem. It's getting ridiculous to keep up with it. But after spending hours researching it, these aren't competing tools. They're different ways of handling memory depending on your use case. And the reason I went deep on this is because I've been building out my own agentic operating system — basically a business brain that runs across everything I do. So I needed to figure out what actually works, what scales, and what just adds complexity to my existing setup.

In this video, I'll walk through six levels of memory that build on top of each other, all the way to systems that work across every single AI tool that you use. By the end, you'll know exactly which one makes sense for your use case and which ones you can completely ignore. But before we go through the levels, one thing I want you to know now — because it'll make the rest of the video easier to follow — is that every memory system is answering exactly the same question: when you give Claude Code a task, how does it pull the right context at the right time? So the difference between each level is just two things. First, where your memory lives — the storage mechanism and what the file structure looks like, whether it's markdown or stored as vectors. And second, how Claude actually gets hold of that data — the retrieval stage. Some stuff gets copied into Claude's context automatically, some sits in a database and gets searched exactly when it's needed, some lives on your laptop, some lives on the cloud.

### Level 1 — Native Claude Code memory

You can think of level one as the native stuff that ships inside Claude Code. Most of you have already heard of the `claude.md` file, some of you have heard of `memory.md`, but very few people are actually using both together properly. Let's do `claude.md` first. It's effectively a plain markdown file inside your project folder where you store your rules, stuff about your brand, things about how you work with clients, coding style — and it's always loaded into every single session you pull up inside the terminal. Think of it like a note that sits at the start of the context, almost like a system prompt you're giving to Claude.

You can have this at the Claude project folder level to pass to all of your Claude instances. You can have it slightly lower at the root folder level if you have multiple projects within the same folder, or you can have it at the individual project level for specific project instructions. The lower down the folder structure you go, it still inherits the parent `CLAUDE.md`, but for any conflicting rules it will always take the local `CLAUDE.md` as gospel.

Here's the thing most people get wrong — stuffing too much into the `CLAUDE.md`: your full brand guide, your tone-of-voice document, your complete client list. Think about it: every single time Claude starts a session, it's going to burn through that context window reading all of that. It's important context, but only when you load it in at the right time. This is exactly the problem we're trying to solve, called context rot — the inability for LLMs to recall 100% of the information we've loaded in as we increase the amount of context loaded in the first place. As a general rule of thumb, keep your `CLAUDE.md` under 200 lines. If you've got more context, like a brand voice document, put that in a separate external file referenced from the `CLAUDE.md` so it only gets pulled in at the right time.

The second built-in memory system already running on your machine is called auto memory, and it forms a `memory.md` file. Jump into an existing project folder and type `/memory`, hit enter, and you'll see a few things: imported memory if you're using a separate system, plus project and user memory (your `CLAUDE.md` files at different levels). Open up the auto-memory folder and you'll see that on a per-project basis there's a memory structure with a `memory.md` file. Inside that file is an index of lots of different memories that Claude Code can reference and open up. It hasn't dumped a huge amount of memories in there — on a project basis it's got specific project-level feedback, and on a more general scale a bunch of feedback for specific things, kept as separate documents. It's following exactly what we talked about: don't dump more than 200 lines in a single file. Always reference a separate file and treat `memory.md` (or `CLAUDE.md`) as an index that points to another file.

For example, we've got a file that's feedback on project structure — "level two or three projects go up under project/briefs" — kept as `feedback-project-structure.md`, loaded only when Claude understands we're looking at project structures. If I go to an empty folder, there's no `memory.md` or `CLAUDE.md` inside it; running `/memory` and opening the auto-memory folder shows no memory consolidation, because it's done on a per-project basis. You don't have to create that `memory.md` file — it's quietly taking notes on your tasks and feedback in the background and creating those files as an index.

So `CLAUDE.md` and `memory.md` are what Claude has today, and it's clear Anthropic wants to own this problem themselves. When the Claude Code source accidentally leaked a couple of weeks back, people found references to a system called Kairos — an unreleased, always-on daemon that watches your project continuously, decides what's worth remembering, and consolidates old notes while you sleep. It's not in any public build yet, but Anthropic is clearly working to solve this context-rot problem and improve the native memory system. Level one's setup is already done for you, it's free, you just need to use it properly. If you keep repeating information to Claude that you think it should already know — that's where level two comes in.

### Level 2 — Structured memory + hooks (John Connolly / Pavel Hryn)

Level two improves the reliability of feeding those memory files in at the right time, and improves the built-in structure inside Claude. I found an article by a guy called John Connolly who took a concept by Pavel Hryn, a huge name in tech, who wrote (on the 18th of Feb) "how to give Claude Code memory — paste this into your project's `CLAUDE.md`." Bearing in mind this was before Claude's auto-memory feature was announced, what it now does is build on that structure, and when combined with John's work, gives us the ability to inject memory automatically at the start of every single session.

Basically we add a big prompt to the `CLAUDE.md` all about how to manage memory and the rules for managing it. A structured memory system rooted at `.claude/memory`: a `memory.md`, a `general.md` storing cross-project facts, preferences and environment setups, plus domain-specific knowledge as `domain/topic` markdown files (one file per topic), and the same for tools — individual files like `slack.md` with specific tool config, workarounds, and edge cases. We add this to our `CLAUDE.md`, go into plan mode, and get it to set up a memory structure for our project that we can then automatically inject into every session.

This works using a Claude Code SessionStart hook, so that when you open a new terminal — or even spin off sub-agents — it automatically loads the `memory.md` index into session files. A hook is just a little script that says: at specific moments, like session start, inject this context into Claude. We're not loading the full context, just the `memory.md` index. The second exciting thing is the potential for sharing this between teammates: sync those domain files so that if somebody's working on a different project, they can save memory files into a shared folder the whole team can access.

To set it up, go to the link in the description, copy the whole markdown section for part one, and add it to `CLAUDE.md`. It creates a global memory directory structure, updates the `CLAUDE.md`, and initializes project `memory.md` files. When I say "reorganize memory," it reads all the memory files, removes duplicates and outdated entries, merges entries that belong together, splits files that cover too many topics, resorts entries by date, and updates the `memory.md` index. But first we just copy this into a prompt — we're not putting it directly in `CLAUDE.md`. Open a new terminal in an existing or empty project (I've got my AgenticOS demo project here), switch to plan mode (shift+tab twice), and paste the entire prompt. It plans out a structure for our memory files and what to add to `CLAUDE.md` based on what already exists.

Once Claude has built the plan for part one, we switch into plan mode again and run "reorganize memory" to tidy up the memory files. Right now it's exploring the memory system state before coming back with a plan. It comes back: "structured persistent memory management system — setting up a global structured memory system for Claude Code so that knowledge persists across sessions and projects." Currently our root `CLAUDE.md` exists but is empty, Claude memory doesn't exist, and only one of our 28 projects has a `memory/memory.md`. It's checked all the way up the parent tree. It's going to create a global memory directory with general, tools, and domain; update our `CLAUDE.md` with all five sections (memory management, global memory, repo memory, auto-init which auto-creates `memory.md` on session start). We click "yes, and bypass permissions" and let it execute.

It's now built the global memory structure. Command-click into any of these files and you can see linking rules between global and project memories, plus `general.md`, the tools, and the domains — cross-project conventions in `general.md`, and a project `memory.md` per project. For all 28 projects it's created or consolidated a specific `memory.md`. Now we run "reorganize memory" in plan mode (not bypass) and it comes up with a plan to fill these `memory.md` and `CLAUDE.md` files with the relevant folder structure.

Whilst that runs, step two is introducing the hook. This hook injects your project memory and the global `memory.md` index before the first tool call of every session — so when you spin up a sub-agent, it throws in that index. We copy the file; in summary it creates the `settings.json` hook saying that on PreToolUse, run the `pre-tool-memory.sh` file (the script that loads in the memory files), and it updates `CLAUDE.md` so that instead of reading `.claude/memory/memory.md` at session start, it auto-injects it via the hook — not relying on Claude reading it and taking action. After five days of usage for John specifically, the number of memory files increased significantly (up 90%) with significantly more lines, but `memory.md` and `general.md` barely grew because they're just index files pointing to the correct tools, domains, and files.

I've asked it to reorganize the memory and this is brilliant. It's looked through my AgenticOS folder and found 11 or 12 empty memory files — empty template, empty template, two empty sessions — and says we just need to delete those; what's the point loading them in? Phase two trims the empty sessions; phase three resolves stale open threads (reading the specific threads in our daily memories to find what happened after those actions); then it adds cross-references between projects, updates `general.md` with all the projects we've worked on, updates the `memory.md` indexes, and runs a verification phase. We click "yes, and bypass permissions." All verifications pass: it deleted 13 files, trimmed six sessions, finished nine open threads, added 10 cross-references, added three patterns to `general.md`, kept 12 daily files with meaningful content, and cleared the empty memory directories inside the clients' folders.

Now we run the second prompt in plan mode and execute the plan to add to `settings.json` so it injects this every time we start a new session. It registers the hook in `settings.json` and updates our global memory and `CLAUDE.md`, so everything executes automatically when a session starts. For a lot of you, this will be enough. But the moment you run this for more than a few weeks, your files get messy and the keyword search that works for a small number of files stops working as you scale. That's where level three comes in.

(Quick aside — YouTube tells me 97% of you watching haven't subscribed; hit subscribe if you've made it this far.)

Only add to level two if two things are true: one, you've been using Claude Code for more than a month and your memory files have grown past a handful; and two, if you've ever typed a question where the answer is somewhere in your notes but Claude couldn't find it.

### Level 3 — Semantic search (MemSearch by Zilliz)

At level two, Claude loads memory more reliably, but as you scale across months and multiple clients, the structure stops scaling — you end up with a giant `general.md` that can't be read efficiently, and because it summarizes key topics rather than taking words verbatim, the keyword search falls apart. Level three solves both. The template comes from an AI agent you're probably familiar with called OpenClaude. The OpenClaude file structure isn't from Claude Code, but the memory design is genuinely powerful and clean — three layers. First, a `memory.md` of long-term durable facts (preferences, decisions, facts about your business), loaded at the start of every session. Second, daily note files — one file per date, a running log of what happened, what got decided, what got shipped, what didn't work; today's and yesterday's load automatically, older ones stay "on the desk" but don't load into context. Third, an optional process called dreaming — a background process that reads your daily notes, scores them, and promotes the ones that keep coming up into long-term `memory.md`, while stale stuff gets forgotten so it doesn't blow your context.

This brings us to a framework called MemSearch, which is a plugin that ports OpenClaude's framework over to Claude Code. It's built by Zilliz, the team behind one of the most popular open-source vector databases, so they know about searching by semantics and meaning. They've extracted OpenClaude's memory architecture into a standalone library that plugs into Claude Code with a two-line install. It keeps all the OpenClaude benefits — markdown-first philosophy (everything readable and portable), the same chunking strategy, the same `memory.md` + daily-notes file structure — but works inside Claude Code. It chunks your documents into semantic vectors so searching understands the meaning behind your questions and your stored content rather than keyword matching. And it applies hooks: it auto-injects the top matches into every prompt via a UserPromptSubmit hook, feeding the top three semantic matches from your memory files directly into context. You don't have to remember to ask Claude to search.

To install, take the two lines: open a new folder, open Claude Code, run `/plugin marketplace add zilliztech memsearch` — it finds and clones the repository, and we add it to our local folder only. Then `plugin install memsearch`, installed for this repo only. It spins up a `settings.local.json` with `memsearch` plugins set to true. Run `/reloadplugins`, control-C twice, and reopen Claude Code. To verify, have a few conversations, then check your memory files with `ls .memsearch/memoryfiles` — you should see today's date inside a memory file. Or use the built-in skill it installs, `memory recall` ("search and recall relevant memories from past sessions via MemSearch"), which you can run as a slash command. We've got no daily memory files yet — it starts from this point. It's using the UserPromptSubmit hook, searching the MemSearch files now. This is super similar to what we use in our own Agentic OS for daily log files plus a long-term memory file that we semantically push into context at the right time.

There's another alternative worth knowing about — but in my opinion not suitable for us — called Claude Mem. It's a Claude Code plugin that automatically captures everything Claude does during a coding session, compresses it with AI, and injects relevant context back into future sessions. Sounds almost the same, super popular, similar goal, but a different philosophy: it uses MCP tools and a three-tier storage model (summaries, timeline, observations). It has more out-of-the-box features than MemSearch — a little dashboard to search memories, team collaboration, cost tracking, privacy labels — but it's a bit overkill for what we need. If you want that management layer, Claude Mem gives you that. But it's MCP-based, which means Claude has to actively decide to call the search tool rather than injecting from a local database like MemSearch. The other major difference: Claude Mem stores everything in the background, whereas MemSearch keeps everything in plain markdown so you can go back and read it.

### Level 4 — Verbatim local recall (Mem Palace)

Level four is where we get serious with word-for-word conversation recall, using a framework called Mem Palace. You only need this level if you catch yourself thinking, "I know we discussed this a few weeks ago, but I can't remember exactly what was decided." Where level three finds your notes and a summary of them, level four finds the exact words used when you made a decision. The best part: it's all stored locally. Compared to the other levels, this is a proper RAG system. It's free, and right now it's got the highest benchmark score of any memory system ever published, apparently. Because it stores words verbatim, nothing gets summarized, so theoretically nothing gets lost.

The content stays verbatim always. The index above it is written in "AAAK," a dense symbolic dialect an LLM can scan at a glance — effectively a different language — with pointers to locations of specific data. You're searching an index that points to a specific area or "drawer" inside a second database, so it retrieves information straight away. Their example: "My son's name is Noah. He turns 6 on September the 12th. He loves dinosaurs." The pointer gets indexed as "Noah, son, age 6, date of birth," storing that in drawer 007 inside wing 42, room 11. When you semantically search, it uses this memory palace — an ancient memory method storing things in wings, rooms, closets, and drawers. A wing represents people/projects/topics; rooms could be day-sessions or threads; closets could be topics, threads, or bundles; and inside is the verbatim text. A series of nested pointers takes it to the exact place. Because it's stored in that symbolic AAAK index, the model can scan thousands of drawers in a single pass, super quickly — 2 weeks later you can ask a question and it retrieves in 42 milliseconds from the exact drawer, and can pull the verbatim text.

It uses two separate databases: a SQL database tracking entities and relationships, and a Chroma vector database storing every conversation as searchable chunks. Like previous levels, it uses background hooks to silently store and index — filing happens on session end and on pre-compaction (it fires the hook before compacting). To install, it's one command — install it, initialize it, and it creates a palace structure (wings, rooms, drawers) in a `.mem-palace` folder, registers all the hooks in your `settings.json`, and starts working. You can even retrospectively mine previous sessions using a "mine" function. At this level, Claude can literally search every conversation you've ever had in plain English, word for word. One downside: it's not verbatim in markdown, so it's not directly readable, but you can retrieve quickly. Even now, everything's still locked to your local machine. So what about the research you did in ChatGPT three or four months ago? The brainstorming on your phone? That's where levels five and six come in — they're totally different, because they're not about remembering conversations anymore, but about having conversations across multiple tools and reliably storing research that connects all your information.

### Level 5 — Knowledge graphs (Karpathy's LLM Wiki / Recall / LightRAG)

Level five is totally different — Mem Palace is the pinnacle of remembering word-for-word conversations; level five is about building a knowledge base of interconnected information. Add level five if you regularly consume information you want to keep and connect over time: articles, videos, podcasts, client notes — anywhere you read a lot and lose track of what you learned. It's less about one-off projects and more about building a second brain on topics you care about. Skip it if you consume content casually and don't need to come back to it.

The most popular library is Andrej Karpathy's GitHub repo / markdown file about LLM Wikis, which got huge coverage. It's a pattern for using Claude to build a living wiki about any topic. You create two folders: a `raw` folder where you drop source documents (articles, reports, podcast transcripts, YouTube transcripts, PDFs) that Claude reads from but never writes to; and a `wiki` folder that Claude owns completely — it writes every file, maintains the structure, and updates cross-references, and you never write to the wiki yourself. It's all plain markdown — no external or vector database. All you need are those files, Obsidian, and an AI. Inside Obsidian (free), once you compile your resources you get a knowledge graph of how they interconnect.

I'm not going to do a dedicated video on this, because I don't think it's super relevant for how we want to synthesize information. Donnelly summarized it well in his article: it's best when you have a "save for later" folder — a pile of bookmarked Slack threads, YouTube videos, and client notes you never go back to — that you want to see the interlinking relationships between. Effectively a Wikipedia on a specific subject. Good for deep research on interconnected topics, but I can't see the directly applicable use cases for retrieving this inside a system like the Business OS or Agent OS. If you disagree, tell me in the comments. I can see opening wikis for specific key topic areas you're researching and having them visualized, but for building out business projects I'm not sure it's the best memory system, apart from deep research on a topic.

A few people surfaced a similar alternative called Recall, which has been blowing up. Recall is a hosted service — basically Karpathy's wiki done for you. Install a browser extension, save articles, podcasts, PDFs, and Recall summarizes, tags, and auto-builds the knowledge graph without the setup headache. It gives you its own AI chat interface so you can chat to your saved content, works on your phone, and has MCP access so you can connect it to Claude Code. In some ways it's better than LLM Wiki because there's zero setup — no Obsidian to download, just a login, and all the work is done for you. Why I think it's not as good as Karpathy's pattern for most people: first, ownership — you don't own the data; Recall lets you export to markdown, but while it's live it's on their servers, so you're renting not owning. Second, Recall is built for content consumption, not operational memory — great for "I watched 40 YouTube videos on Claude Code; which talked about memory and what did they say?" but not for "what did we decide about client X's landing page and conversion rates back in March?" Third, it's off-the-shelf software, so there's a pricing implication. My take: if you're non-technical and mainly want to organize articles, videos, and podcasts, Recall is great; if you want maximum control and to build out that Wikipedia, LLM Wiki beats it.

There's also a heavyweight knowledge-graph alternative called LightRAG — an enterprise-grade knowledge graph designed for heavier entity extraction, dual-level retrieval, the full research-grade thing. But it's overkill for 99% of business owners; you don't need that setup headache or massive background database. You're better off going back to level four, or for a visual knowledge base installing Karpathy's pattern or using Recall. To be clear, both of these are for building knowledge bases, not operational memory, so they probably wouldn't be used in many of our own use cases apart from research.

### Level 6 — Cross-tool memory (Open Brain by Nate Jones / Mem0)

Up to this point, everything lives inside Claude Code. But some of you don't just use Code — you might use ChatGPT on your phone, or Cursor — and when you use multiple AI tools, none of them know anything about each other. Level six is a method called Open Brain by Nate Jones, who has brilliant knowledge in this space. The intent is to let you switch between AI tools constantly (ChatGPT on your phone, Claude Code at your desk). It's the only system today where all your different AI tools can see the same memory automatically in real time. Arguably it's the most future-proof and portable, because your memory lives in a Postgres database that you own — so when the next big AI tool drops in six months, you just connect it to your existing Postgres brain, no migration needed. If you're still living mostly inside Code on one machine, it's probably worth skipping.

It's an infrastructure layer for your thinking: one database, one chat channel, and any AI you use can plug into it — super powerful if you work across apps. You're not tied to any SaaS, and it's cheap to run, less than a dollar a month. It runs on a Postgres database hosted on Supabase. Inside is basically one table called `thoughts`, where every row is a single memory — a chunk of text, an embedding vector for search, some tags, and a timestamp. It uses built-in extensions that handle the semantic search. We have an MCP server running from Claude Code that connects to Supabase's edge functions, which act as a front door for every AI tool that wants to read from the database.

If that sounds complicated, that's one downside — it does have an AI-assisted setup, but it takes significantly longer to set up and understand than the others. There's a full setup guide (linked below), a video walkthrough from Nate himself, and companion prompts to migrate your memories from existing Claude Code memory systems into Open Brain. For retrieval, Claude Code, ChatGPT, Claude Desktop, and Cursor can all query the same brain. I'm not going to set this up live as it's probably overkill for most people, but Nate's guide is written for non-technical people and takes about 30 to 45 minutes. There's a live community — check the GitHub and join if you want help with setup. If you want your memory portable and not tied to Claude Code, this is probably the right solution.

There's an alternative I'll quickly mention called Mem0 — another cross-tool memory layer. It's well-funded, well-marketed, and widely used, "used by 100,000 developers" from large companies. If you want something more production-ready, check out mem0.ai — its setup gets you started in less than a minute, and you get a universal self-improving AI memory layer for your LLM applications, completely cross-tool. If you're shipping an AI product, this might be a sensible choice. The downside: your data lives on their servers permanently, whereas with Open Brain you own the Supabase project, can export the whole Postgres database whenever you want, and control access. In terms of level six, Open Brain (not Mem0) is probably the most complex to set up, and it's the only one that introduces a significant monthly cost — though Open Brain is more like 10–30p per month on Supabase's free tier. The other downside versus other levels: it's not locally held data, so we query an external database every time, which adds some latency. But that might be the compromise you'll make if you want every AI tool to share the same memory.

### Which one should you pick?

If you're literally just starting, don't worry about these memory systems — turn on level one by using your `CLAUDE.md` and `memory.md` files the right way. Ten minutes, massive improvement over Claude's built-in memory. If you've been using Claude Code for a little bit, go to level two, install John's hook, and honestly most of you should stop right there. If you've built up significant context and you're losing old decisions across months of work, go to level three (install MemSearch) or level four (verbatim word-for-word retrieval from Mem Palace). Levels five and six are a different realm for specific use cases: level five (Karpathy's LLM Wiki) is best for deep research on a specific topic and referencing relationships between subtopics; level six is for something you own, still relatively cheap, that plugs into any external AI tool — Open Brain or Mem0.

The best part: a lot of these stack together. You can run levels one, two, and three together with no issues — the folder structure is fairly similar and you can ask Claude Code to integrate them. As for what I'm personally implementing: I'm running up to level three inside the Agentic Operating System, following those OpenClaude conventions but adding the semantic search capability and the hooks that inject certain context at certain times, which improves search and recall inside the business operating system. If you want to see exactly how to build out your own Agentic Operating System, watch the next video. Thanks for watching — see you in the next one.

## Timestamped Transcript

**[0:00] Intro — the memory-system overload**
Right now, if you search for the best Claude Code memory system, you get absolutely buried — Mem0, Karpathy's Obsidian Wiki, OpenClaude, Hermes, Mem Palace, LightRAG, Claude Mem. These aren't competing tools; they're different ways of handling memory depending on your use case. I've been building my own agentic operating system — a business brain across everything I do — so I needed to figure out what works, what scales, and what just adds complexity. This video walks through six levels of memory that build on each other.

**[0:45] The core question + the two variables**
Every memory system answers the same question: when you give Claude Code a task, how does it pull the right context at the right time? Each level differs on just two things — where your memory lives (storage / file structure, markdown vs. vectors) and how Claude retrieves it. Some context gets copied in automatically, some sits in a database and gets searched when needed, some lives locally, some in the cloud.

**[1:31] Level 1 — CLAUDE.md basics**
Level one is the native stuff shipping inside Claude Code. `claude.md` is a plain markdown file with your rules, brand, client workflow, and coding style, always loaded into every session like a system prompt. You can place it at the project-folder level, the root level, or the individual project level.

**[2:18] CLAUDE.md inheritance + the over-stuffing mistake**
Lower folders inherit the parent `CLAUDE.md` but local rules win on conflict. The big mistake is stuffing too much in — full brand guide, tone-of-voice doc, complete client list — because Claude burns context reading all of it every session.

**[3:04] Context rot + the 200-line rule + auto memory.md**
Context rot is the LLM's inability to recall 100% of loaded information as context grows. Keep `CLAUDE.md` under 200 lines and reference external files for big context. The second built-in system is auto memory (`memory.md`) — type `/memory` to see imported, project, and user memory.

**[3:50] How auto memory indexes per project**
Inside the auto-memory folder, `memory.md` is an index pointing to separate feedback files — project-level feedback plus general feedback — rather than one giant dump.

**[4:36] Treat memory.md as an index + empty-folder demo**
Always reference separate files and treat `memory.md` / `CLAUDE.md` as an index (e.g. `feedback-project-structure.md` loads only when relevant). An empty folder has no memory files until Claude quietly creates them.

**[5:22] The leaked "Kairos" daemon**
Auto memory takes notes in the background. The leaked Claude Code source referenced "Kairos" — an unreleased always-on daemon that watches your project, decides what to remember, and consolidates notes while you sleep. Anthropic is clearly working to solve context rot natively.

**[6:08] Level 1 wrap + intro to Level 2 (John Connolly / Pavel Hryn)**
Level one is free and already set up. If you keep repeating things Claude should know, move to level two — based on John Connolly's article building on Pavel Hryn's "how to give Claude Code memory."

**[6:53] The structured memory prompt**
Add a big memory-management prompt to `CLAUDE.md`: a structure rooted at `.claude/memory` with `memory.md`, `general.md` (cross-project facts), domain files (`domain/topic`, one per topic), and tool files (e.g. `slack.md`).

**[7:39] SessionStart hook + team sharing**
A SessionStart hook auto-loads the `memory.md` index when you open a terminal or spin off sub-agents. Bonus: sync domain files into a shared folder so teammates share memory.

**[8:26] Setup begins — copy part one into a prompt**
Copy the part-one markdown from the description; it creates a global memory directory, updates `CLAUDE.md`, initializes project `memory.md` files, and defines "reorganize memory" (dedupe, merge, split, resort, reindex). Paste it into plan mode in a project.

**[9:11] What "reorganize memory" does + running the plan**
"Reorganize memory" reads all files, removes duplicates/outdated entries, merges related entries, splits over-broad files, resorts by date, updates the index. Switch to plan mode, paste, and let it plan the structure.

**[9:59] Claude explores + returns a plan**
In the AgenticOS demo, Claude explores the memory state and returns a plan: root `CLAUDE.md` empty, Claude memory missing, only 1 of 28 projects has `memory/memory.md`. It will build the global directory and update `CLAUDE.md` with five sections.

**[10:44] Executing the build**
Click "yes, and bypass permissions." It builds the global memory structure with linking rules between global and project memories, `general.md`, tools, and domains.

**[11:31] Per-project memory files created**
For all 28 projects it creates/consolidates a `memory.md`. Now run "reorganize memory" in plan mode to fill the files with the relevant folder structure.

**[12:17] Step two — introducing the hook**
The PreToolUse/SessionStart hook injects project memory + the global `memory.md` index before the first tool call, so sub-agents get the index. The `settings.json` hook runs `pre-tool-memory.sh`.

**[13:02] Hook auto-injects instead of relying on Claude reading**
`CLAUDE.md` is updated so memory is auto-injected via the hook rather than Claude reading it. After 5 days, John's memory files grew ~90% but `memory.md`/`general.md` barely grew (they're just indexes).

**[13:48] Reorganize finds empties + stale threads**
Reorganize found ~11–12 empty memory files to delete, trims empty sessions (phase 2), resolves stale open threads (phase 3) by reading what happened after actions.

**[14:34] Cross-references + verification**
It adds cross-references between projects, updates `general.md`, updates the `memory.md` indexes, and runs verification.

**[15:20] Verification results**
All passed: deleted 13 files, trimmed 6 sessions, finished 9 open threads, added 10 cross-references, added 3 patterns to `general.md`, kept 12 meaningful daily files, cleared empty client directories.

**[16:06] Register the second hook + when Level 2 breaks down**
Run the second prompt to register the hook in `settings.json`. For many this is enough — but after a few weeks files get messy and keyword search stops scaling. That's level three.

**[16:52] Subscribe ask + when to use Level 2**
(97% of viewers aren't subscribed — hit subscribe.) Only add level two if you've used Claude Code >1 month with growing files, and you've had answers in your notes that Claude couldn't find.

**[17:38] Level 2's scaling problem + Level 3 / OpenClaude**
At scale, `general.md` gets too big and keyword search fails. Level three's template comes from OpenClaude — a clean three-layer design.

**[18:23] OpenClaude's three layers + "dreaming"**
Layer 1: long-term `memory.md` (durable facts). Layer 2: daily notes (running log; today/yesterday auto-load). Layer 3: optional "dreaming" — a background process that scores daily notes and promotes recurring ones to long-term memory while forgetting stale stuff.

**[19:09] MemSearch by Zilliz**
MemSearch is a plugin porting OpenClaude into Claude Code, built by Zilliz (vector-database team). Two-line install, markdown-first, same chunking and file structure.

**[19:54] Semantic vectors + UserPromptSubmit hook**
It chunks documents into semantic vectors so search understands meaning, and uses a UserPromptSubmit hook to auto-inject the top three semantic matches into every prompt.

**[20:40] Installing MemSearch**
`/plugin marketplace add zilliztech memsearch`, add to local folder, `plugin install memsearch` for this repo only — spins up `settings.local.json`.

**[21:25] Reload + verify**
Run `/reloadplugins`, control-C twice, reopen Claude Code. Verify with `ls .memsearch/memoryfiles` or the `memory recall` skill.

**[22:12] MemSearch in action + Claude Mem intro**
It uses the UserPromptSubmit hook to search MemSearch files — similar to the creator's own Agentic OS. Alternative: Claude Mem, an MCP-based plugin with a three-tier storage model.

**[22:59] Claude Mem vs. MemSearch**
Claude Mem has more features (dashboard, team collaboration, cost tracking, privacy labels) but is overkill and MCP-based (Claude must decide to call the search tool). It stores everything in the background; MemSearch keeps readable markdown.

**[23:45] Level 4 — Mem Palace intro**
Level four is verbatim, word-for-word recall via Mem Palace — stored locally, free, highest published benchmark score, nothing summarized so nothing lost.

**[24:30] The AAAK index + the Noah example**
Content stays verbatim; the index is written in "AAAK," a dense symbolic dialect with pointers to "drawers." Example: "Noah, son, age 6, date of birth."

**[25:15] The memory-palace metaphor**
Pointer maps to drawer 007, wing 42, room 11. Wings = people/projects/topics; rooms = day-sessions/threads; closets = topics/bundles; inside = verbatim text.

**[26:01] Symbolic scanning speed + dual databases**
The AAAK index lets the model scan thousands of drawers in one pass — retrieval in 42ms two weeks later. It uses a SQL database (entities/relationships) + Chroma (conversation chunks).

**[26:47] Background hooks + install**
Filing happens silently via hooks on session-end and pre-compaction. One-command install creates `.mem-palace` (wings/rooms/drawers), registers hooks in `settings.json`.

**[27:32] Mining old sessions + downside**
A "mine" function retrospectively indexes past sessions. Downside: not verbatim markdown, so not directly readable. Everything's still local — what about ChatGPT or phone brainstorms?

**[28:17] Bridge to Levels 5 & 6**
Levels five and six are different — not about remembering conversations but having conversations across tools and storing connected research.

**[29:04] Level 5 — knowledge bases**
Level five builds a knowledge base of interconnected information (articles, videos, podcasts, client notes) — a second brain. Skip it if you consume casually.

**[29:51] Karpathy's LLM Wiki structure**
Karpathy's LLM Wiki: a `raw` folder Claude reads from (never writes), a `wiki` folder Claude owns completely, all plain markdown, visualized in Obsidian's knowledge graph.

**[30:36] Obsidian + the creator's skepticism**
All you need is the files, Obsidian (free), and an AI. The creator isn't doing a dedicated video — not super relevant for synthesizing info his way.

**[31:21] Best use case + business doubts**
Donnelly: best for a "save for later" pile of bookmarks you want to interlink — a Wikipedia on a subject. The creator doesn't see direct business-OS retrieval use beyond deep research.

**[32:07] Recall — the done-for-you LLM Wiki**
Recall is a hosted version of Karpathy's wiki — browser extension, save articles/podcasts/PDFs, auto-tags and builds the graph, AI chat interface, phone support, MCP access.

**[32:53] Why Recall falls short**
Zero setup but: you don't own the data (lives on their servers), it's built for content consumption not operational memory, and there's a pricing implication.

**[33:39] Recall verdict + LightRAG**
Verdict: Recall for non-technical content organizing; LLM Wiki for maximum control. LightRAG is an enterprise knowledge graph — overkill for 99% of business owners.

**[34:26] Knowledge bases ≠ operational memory + bridge to Level 6**
Both are for knowledge bases, not operational memory. Up to now everything lives inside Code — but you might also use ChatGPT or Cursor, and they don't know about each other.

**[35:12] Level 6 — Open Brain by Nate Jones**
Open Brain lets every AI tool see the same memory in real time, stored in a Postgres database you own — most future-proof and portable, no migration when new tools drop. Skip if you're single-machine in Code.

**[35:57] Open Brain architecture**
One database, one chat channel, ~<$1/month on Supabase Postgres. One `thoughts` table: text chunk + embedding vector + tags + timestamp. An MCP server connects Claude Code to Supabase edge functions.

**[36:44] Setup difficulty + migration prompts**
Downside: AI-assisted setup takes longer to set up and understand. Full guide, Nate's video walkthrough, and companion prompts migrate existing memories. Claude Code, ChatGPT, Claude Desktop, and Cursor all query the same brain.

**[37:29] Open Brain wrap + Mem0 intro**
The creator won't set it up live (~30–45 min for non-technical users); there's a live GitHub community. Alternative: Mem0, a well-funded cross-tool memory layer used by 100,000 developers.

**[38:16] Mem0 vs. Open Brain**
Mem0 starts in under a minute, production-ready, cross-tool — but data lives on their servers permanently. Open Brain: you own the Supabase project and can export the Postgres database.

**[39:01] Level 6 trade-offs**
Open Brain is the most complex and the only one with meaningful monthly cost (10–30p on Supabase free tier). Downside: not local, so external queries add latency — the compromise for shared cross-tool memory.

**[39:47] Which to pick**
Just starting → level one (10 min). Been using Code a while → level two and stop. Losing old decisions → level three (MemSearch) or level four (Mem Palace).

**[40:34] Stacking + the creator's own setup + outro**
Levels five (Karpathy's LLM Wiki for research) and six (Open Brain / Mem0 for owned cross-tool memory) are for specific cases. Levels 1–3 stack cleanly. The creator runs up to level three in his Agentic OS — OpenClaude conventions plus semantic search and hooks. Watch the next video for building your own Agentic Operating System.
