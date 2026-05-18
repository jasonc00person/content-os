# It’s Broken… The Claude Code Vs Codex Debate Is Finally Over

- **Source:** https://www.youtube.com/watch?v=8ImlAQOyVTs
- **Uploader:** AI LABS
- **Uploaded:** 2026-05-02
- **Duration:** 15:52
- **Method:** YouTube captions (no transcription needed)

## Transcript

For a long time, everyone's go-to model for coding was Claude. Not only because it performed well, but because there weren't other options on the same tier. Then GPT models stepped up and closed the gap, especially with the release of GPT 5.5, which brought it down to almost none. To compare the two, we needed to put them in the environments designed best for them, which means their own CLIs. So, we're putting Opus 4.7 and GPT 5.5 to the test to see how they perform against each other. We'll test them across nine categories to find out which one actually comes out on top, and by the end, you'll know which one earns the spot in your workflows. Usability is where Claude code starts breaking down for us. We've been using it for most of our tasks, coding and non-coding, but it was only good until the 2.1.0 update. After that, things started going downhill for Claude code. The UI is the most frustrating part because it has the biggest impact on the experience. The terminal glitches, rendering breaks, and a lot of what used to feel polished now feels off. It used to be one of the best TUIs, but only until it started being vibe coded. It now feels more broken with multiple bugs like rendering issues, cache leaks, about which not only us were complaining. The bigger problem is that they removed the dangerously skip permissions mode and replaced it with auto mode by default. We used to run bypass permission mode for most of our tasks with hooks set up for whichever files we didn't want Claude to touch. Now it asks for permissions on even that mode. When we gave Claude a prompt to create a skills, shifted to another Claude session to do something else, and only later found that the skill creation was blocked by permission prompt for writing to the dot Claude folder the entire time. We came back expecting the skills to be created, and it was just sitting there waiting. Codex handles this better because it's Yolo mode doesn't ask for any permissions the way Claude code's auto mode does. The CLI is built on Rust, so the UI is much smoother than Claude code's React-based setup, and even after a long session, nothing breaks. Personality configuration is another spot where Codex pulls ahead. We can set the personality to a more direct and concise language. This is because GPT 5.5 is significantly more sycophantic and is agreeable with every prompt than Opus 4.7 is. This is why changing the personality in Codex prevents that default behavior in the model. To make Opus 4.7 direct, we have to rely on instructions in Claude.md, while Codex does that with just a setting change. Pre-installed skills are another difference. Codex ships with many that Claude Code doesn't have, including the agent browser skill. That matters for anyone building apps, because in Codex we don't need to explicitly connect MCPs for browser verification. It does that automatically after implementing any feature. It also has a built-in skill creator, so when we want a new skill, it generates a complete one with the right structure and reference files. In Claude, we need to install the skill creator separately to get a properly structured skill. Otherwise, it just writes an MD file. Now, there are still two things Claude Code does better. Codex doesn't offer rewinding, which is a feature we use the most, so not having it is a real downside. Claude Code also lets us view its thinking by ex- panding it with control plus O, which Codex doesn't do well. Viewing the reasoning is helpful because we can correct the approach mid-task instead of waiting for the implementation to finish and then redoing it. So, looking at how Claude Code's user experience degrades with each new update, Codex gets a point for usability. On cost, [snorts] Claude Code is the more expensive tool by a wide margin. Not in terms of actual prices, but by usability per same price. Claude Code is not available on the free tier at all and is only available starting from the Pro and Max plans. The plans have nearly identical pricing. The Pro plan is basically unusable for any good scale application because it hits its limits on just a few tasks. We can't even properly use Opus 4.7 for any meaningful task on Pro. The limits run out very quickly even on the Max plan that we use. Codex is in a better position from the start. It's available even on the free plan with limited usage. Both use a similar 5-hour window mechanism, so to see which one gets more work done, we ran them on tasks of the same scale. Claude Code already has a context command that visualizes how many tokens a session has used, but Codex doesn't have a built-in equivalent, so we had to find a workaround for the comparison. Both tools store their sessions as JSON files, just organized differently. So, we built a small tool that reads them and counts the tokens used in each session. On the same app and a similar level of debugging, Opus 4.7 burned through 173,000 tokens, while GPT 5.5 used only 82,000. This is because GPT 5.5 gets work done in fewer tokens and far fewer retries. So, Codex lasted significantly longer and turned out to be far more cost-efficient for the same work. But before we move forwards, let's have a word by our sponsor, Stream. You're building an app and your users need to talk, Stream and connect. You try handling that yourself, 3 months later, you're still debugging instead of shipping. Stream skips all of that. Stream gives you everything out of the box from in-app chat and video calling to activity feeds and AI moderation, so you're shipping features, not building infrastructure from scratch. We're talking WhatsApp-style messaging, Zoom-style video calls, and Instagram-style feeds all built in. What really stands out is Stream's new launch, Vision Agents. You can build intelligent AI agents that see, hear, and act on live video and audio, all in Python with just a few lines of code. Everything runs on a global edge network for low latency everywhere. From startups to scaling apps, leading platforms across social, fitness, and community rely on Stream to power over a billion end users. If you're a developer building the next big app, Stream scales with you from day one. Start for free at getstream.io. Links in the pinned comment. The real test for the two models is on how they build products. As we said before, GPT 5.5 is faster and consumes fewer tokens, so it ships working apps quicker. Opus 4.7 spends more tokens on thinking, plans deeper, and iterates on all aspects of the app at the same time. Planning was the first thing we wanted to test. We've been using Claude Code's planning mode for a long time. It It most things, has some flaws, but is still quite usable. So, we wanted to see how GPT-5.5 performs at planning because OpenAI claims it does better at planning tasks and executing them. We enabled plan mode and opened it in a folder that already contained a back-end for an app, an API built using FastAPI, and asked it to build the front-end for it. It explored the project thoroughly and asked a few questions, but the questions were fairly simple. It could have gone deeper into how we wanted the front-end to look because for front-end work, that matters. The plan it produced was very simple. It included a summary of the main flow, the key changes, the pages to add, and how to test them. The one thing it did well was clearly separating its assumptions, so we knew exactly what it was taking for granted. We told it to proceed and it finished in about 8 minutes. The same task on Claude Code took 24 minutes, but Opus 4.7's plan was much more in-depth, considered more aspects of the application, and even pulled in Shadcn UI to improve the user experience. So, Opus 4.7 does better in terms of planning. Next, [snorts] we wanted to test both on a greenfield app. We gave them the same prompt, that is to create a monorepo with a Python Flask back-end and a Next.js front-end along with the full pipeline and key requirements for how the app should work. Claude Code switched into planning mode by itself because of its harness design. Codex did not switch into planning mode and instead started implementing directly. It finished much faster than Claude Code, which took around 16 minutes because of the planning step. GPT-5.5's version of the app had a much simpler UI and mainly focused on making sure the app worked. It didn't work properly at the start, so we debugged it iteratively. One thing we noticed was that the interview prompts were hardcoded because we hadn't provided any API key. The prompt specified using the Gemini API as a back-end, but since no key was available, it implemented a fallback so the app wouldn't crash completely. Codex had actually used local follow-up questions without any explicit prompting. We liked this because fallback mechanisms like these are useful in production since they prevent crashes. After a few iterations and adding the API key, the app's flow worked properly even though the UI was still simple. So, GPT-5.5 looked at the edge cases and implemented mechanisms to fill in the gaps. Opus 4.7 on the other hand, asked us to give it the API key before it started implementation and built the entire app around that. So, Opus 4.7, unlike GPT-5.5, didn't prepare for fallbacks and just needed everything available up front. Due to this, when the API wasn't actually there, the app had no fallback and just gave an error. Claude Code does focus on user experience and functionality together, so its implementation looked more realistic. This is Opus 4.7's UI strength showing up, which we covered in our previous video where we said Opus 4.7 is way better at handling the UI, but its implementation also had issues. When we asked it to debug, it didn't directly inspect the implementation like Codex did. Instead, it started asking us questions about what might be causing the problem and relied on our testing. It added debug points like indicators in the UI and console logs and asked us to check states and report back. After a back and forth, it eventually fixed the issue and the interview feature worked. We preferred how Codex used the agent browser to debug on its own. So, in terms of autonomous working, Codex's implementation was better and in terms of user experience, Claude Code did a way better job. We also wanted to test how both handle the init command. Claude Code's init runs without expanding the prompt inline. It creates a simple Claude.md file that's around 90 lines and includes architecture, app flow, front end and back end structure, and all required commands to run the app. A lot of that information is redundant and doesn't really benefit the agent, which is why it isn't always necessary to keep all of it. Codex's setup was more refined. It included commit guidelines, pull request guidelines, and security instructions properly while keeping the project structure section brief instead of overloading it with detail. Neither was perfect, but Codex handled agents.md was perfect, but Codex handled agents.md better. better. &gt;&gt; Now, we also wanted to test how both perform on code review. We gave the same prompt for a reliability review to both Codex and Claude code, asking them to document the review in separate files while working on the same code base. Once both had generated their reports, we opened a new session and asked Claude to output the diff between the two files comparing the findings. Claude's review was much more detailed. It organized every finding by priority and included components, the exact code snippets behind the issues. Codex's report mentioned line numbers but did not include the actual code snippets. Both reports were thorough, sharing several findings while each caught a few the other missed. Claude code also reported security issues like a leaked API key and a vulnerability. The task was a reliability review though, and those issues were outside the scope. Claude code reported every extra problem it ran into along the way, while Codex stayed strictly on reliability. So, Codex's report was more aligned with the original request, while Claude code's was broader but less focused on the specific task. If we had to describe both in terms of building, GPT 5.5 feels more like a back-end engineer focused on getting the application's functionality delivered correctly first, while Opus 4.7 feels more like a full-stack engineer trying to balance both functionality and user experience. On [snorts] context management, Codex performed much better than Claude code. Claude code has in-session context editing, which removes tool calls and reasoning steps that no longer matter from the conversation. It clears redundant information from the session to avoid bloat. The compaction isn't perfect, but at least it doesn't keep unnecessary parts in the context while compacting. Codex doesn't edit their context. It compacts the entire conversation just as it took place. The one thing it does better is preserving the last 20,000 tokens in memory and not compacting that portion at all. That helps prevent performance degradation in Codex after compaction, so that the conversation can flow smoothly from the next prompt onward. We tested its performance and Codex performed better after compaction than Claude code did. So, even though Claude code follows a more detailed, multi-step compaction process, Codex's preserved tail keeps the agent more useful in practice. Memory works differently between the two. Cloud Code's harness is mostly stateless across sessions, meaning each session starts without any context from the previous one. It now has a memory feature that can store persistent preferences or instructions. So, if we tell it to avoid doing something a certain way, it stores that and applies it again later within the same project. That helps when working repeatedly in a single project, but the memory is project-scoped. So, switching projects loses that stored behavior. Codex takes the opposite route. It consolidates information from multiple sessions over time and builds a global memory across interactions. So, it can retain patterns beyond a single project. That can help consistency across different tasks. So, in short, Cloud Code keeps memory more contained within a project, while Codex takes a more cross-session, cross-project approach, which changes how each of them adapts over time. Since Cloud Code has been around for longer and is being developed constantly to improve developer experience, it has more to offer compared to Codex. Cloud Code has a hook system, which lets us run our own scripts at specific points in the agent's life cycle, like before or after a tool runs, among other points for things like blocking unsafe commands, running formatters, and more. We can also run sub-agents in a dedicated work tree, so their performance doesn't affect each other. We can control the effort level for the models, and we can even use keywords like ultra think to push reasoning to its maximum on a specific task. None of that has an equivalent in Codex right now. The ecosystem is the other clear win for Cloud Code. We can run sessions through the Cloud desktop app and delegate tasks from the mobile app. Across Cloud Code, the desktop app, web app, and browser extensions, the surface is much wider than Codex, which mainly consists of a web app and a desktop app that was only recently released and didn't feel as strong at the time we tested it. Sessions also move between environments more easily on Cloud Code, which makes it more convenient to work across different interfaces. Codex also has many interesting features. In the cloud, it has an attempt flag that runs the same task n times. It produces several implementations and selects the best one. Claude Code can do something similar, but only through configurations and instructions, not as a flag. The other Codex-only feature, which sets it apart from the rest, is its integration with OpenAI's image models. It can use them directly in the CLI to generate images for the websites it's working on. Claude relies mostly on SVG-based generation for visuals, which doesn't even compete on quality because it doesn't have any image model yet. If we're building a UI that needs real imagery, Codex is the only one of the two that does it without even being explicitly told to. Also, if you are enjoying our content, consider pressing the hype button because it helps us create more content like this and reach out to more people. Both [snorts] use sub-agents, even though the concept was introduced by Claude first. Since it came first in Claude Code, its integration is more mature because it has been agent-centric and focused on the coding experience for way longer than OpenAI. It supports agents that can be orchestrated through remote sessions, while Codex mainly supports multi-agent workflows inside the terminal environment. The biggest difference is how each invokes sub-agents. Claude Code can spawn agents without explicit invocation, while Codex only creates an agent if we explicitly ask for one in the prompt. When Codex spawns agents, it names them and pass them a proper prompt as well. In coding performance, the two are fairly similar, but the design choices behind them are different. Claude Code sub-agents use an explicit allow list, meaning the parent agent defines exactly which tools the sub-agent can access, while Codex sub-agents inherit tool access from the parent by default. Claude Code also gives every sub-agent a completely fresh context window. A sub-agent doesn't have access to the conversation history and only sees the prompt from the parent, plus the system prompt and any global rules because Claude focuses on context isolation. Codex CLI does the opposite. It forks the full history into the sub-agent session with the parent's prompt layered on top. Codex agents retain more context about what's already been discussed, which does help improve their performance. In practice, Claude code strict isolation hurt our research sub-agents. When we used them, the results weren't good enough because they only saw the immediate prompt and didn't have any prior context. Codex agents get the whole history, can iterate more effectively, and perform better on tasks where continuity matters. That brings us to the end of this video. If you'd like to support the channel and help us keep making videos like this, you can do so by using the Super Thanks button below. As always, thank you for watching and I'll see you in the next one.

## Timestamped

`[00:02]` For a long time, everyone's go-to model
`[00:02]` for coding was Claude. Not only because
`[00:03]` it performed well, but because there
`[00:05]` weren't other options on the same tier.
`[00:07]` Then GPT models stepped up and closed
`[00:09]` the gap, especially with the release of
`[00:11]` GPT 5.5, which brought it down to almost
`[00:13]` none. To compare the two, we needed to
`[00:15]` put them in the environments designed
`[00:17]` best for them, which means their own
`[00:18]` CLIs. So, we're putting Opus 4.7 and GPT
`[00:22]` 5.5 to the test to see how they perform
`[00:24]` against each other. We'll test them
`[00:26]` across nine categories to find out which
`[00:28]` one actually comes out on top, and by
`[00:30]` the end, you'll know which one earns the
`[00:31]` spot in your workflows. Usability is
`[00:34]` where Claude code starts breaking down
`[00:36]` for us. We've been using it for most of
`[00:38]` our tasks, coding and non-coding, but it
`[00:40]` was only good until the 2.1.0 update.
`[00:43]` After that, things started going
`[00:44]` downhill for Claude code. The UI is the
`[00:46]` most frustrating part because it has the
`[00:48]` biggest impact on the experience. The
`[00:50]` terminal glitches, rendering breaks, and
`[00:52]` a lot of what used to feel polished now
`[00:54]` feels off. It used to be one of the best
`[00:56]` TUIs, but only until it started being
`[00:58]` vibe coded. It now feels more broken
`[01:00]` with multiple bugs like rendering
`[01:02]` issues, cache leaks, about which not
`[01:04]` only us were complaining. The bigger
`[01:06]` problem is that they removed the
`[01:07]` dangerously skip permissions mode and
`[01:09]` replaced it with auto mode by default.
`[01:11]` We used to run bypass permission mode
`[01:13]` for most of our tasks with hooks set up
`[01:15]` for whichever files we didn't want
`[01:16]` Claude to touch. Now it asks for
`[01:18]` permissions on even that mode. When we
`[01:20]` gave Claude a prompt to create a skills,
`[01:22]` shifted to another Claude session to do
`[01:24]` something else, and only later found
`[01:26]` that the skill creation was blocked by
`[01:28]` permission prompt for writing to the dot
`[01:30]` Claude folder the entire time. We came
`[01:32]` back expecting the skills to be created,
`[01:34]` and it was just sitting there waiting.
`[01:36]` Codex handles this better because it's
`[01:37]` Yolo mode doesn't ask for any
`[01:39]` permissions the way Claude code's auto
`[01:41]` mode does. The CLI is built on Rust, so
`[01:43]` the UI is much smoother than Claude
`[01:45]` code's React-based setup, and even after
`[01:47]` a long session, nothing breaks.
`[01:49]` Personality configuration is another
`[01:51]` spot where Codex pulls ahead. We can set
`[01:53]` the personality to a more direct and
`[01:55]` concise language. This is because GPT
`[01:57]` 5.5 is significantly more sycophantic
`[02:00]` and is agreeable with every prompt than
`[02:02]` Opus 4.7 is. This is why changing the
`[02:05]` personality in Codex prevents that
`[02:07]` default behavior in the model. To make
`[02:08]` Opus 4.7 direct, we have to rely on
`[02:11]` instructions in Claude.md, while Codex
`[02:13]` does that with just a setting change.
`[02:15]` Pre-installed skills are another
`[02:17]` difference. Codex ships with many that
`[02:19]` Claude Code doesn't have, including the
`[02:21]` agent browser skill. That matters for
`[02:23]` anyone building apps, because in Codex
`[02:25]` we don't need to explicitly connect MCPs
`[02:27]` for browser verification. It does that
`[02:29]` automatically after implementing any
`[02:31]` feature. It also has a built-in skill
`[02:32]` creator, so when we want a new skill, it
`[02:34]` generates a complete one with the right
`[02:36]` structure and reference files. In
`[02:38]` Claude, we need to install the skill
`[02:40]` creator separately to get a properly
`[02:41]` structured skill. Otherwise, it just
`[02:43]` writes an MD file. Now, there are still
`[02:45]` two things Claude Code does better.
`[02:47]` Codex doesn't offer rewinding, which is
`[02:49]` a feature we use the most, so not having
`[02:51]` it is a real downside. Claude Code also
`[02:53]` lets us view its thinking by ex- panding
`[02:55]` it with control plus O, which Codex
`[02:57]` doesn't do well. Viewing the reasoning
`[02:59]` is helpful because we can correct the
`[03:00]` approach mid-task instead of waiting for
`[03:02]` the implementation to finish and then
`[03:04]` redoing it. So, looking at how Claude
`[03:06]` Code's user experience degrades with
`[03:08]` each new update, Codex gets a point for
`[03:10]` usability. On cost, [snorts] Claude Code
`[03:12]` is the more expensive tool by a wide
`[03:14]` margin. Not in terms of actual prices,
`[03:16]` but by usability per same price. Claude
`[03:19]` Code is not available on the free tier
`[03:21]` at all and is only available starting
`[03:23]` from the Pro and Max plans. The plans
`[03:24]` have nearly identical pricing. The Pro
`[03:26]` plan is basically unusable for any good
`[03:28]` scale application because it hits its
`[03:30]` limits on just a few tasks. We can't
`[03:32]` even properly use Opus 4.7 for any
`[03:35]` meaningful task on Pro. The limits run
`[03:37]` out very quickly even on the Max plan
`[03:38]` that we use. Codex is in a better
`[03:40]` position from the start. It's available
`[03:42]` even on the free plan with limited
`[03:44]` usage. Both use a similar 5-hour window
`[03:46]` mechanism, so to see which one gets more
`[03:48]` work done, we ran them on tasks of the
`[03:50]` same scale. Claude Code already has a
`[03:52]` context command that visualizes how many
`[03:54]` tokens a session has used, but Codex
`[03:56]` doesn't have a built-in equivalent, so
`[03:58]` we had to find a workaround for the
`[03:59]` comparison. Both tools store their
`[04:01]` sessions as JSON files, just organized
`[04:04]` differently. So, we built a small tool
`[04:05]` that reads them and counts the tokens
`[04:07]` used in each session. On the same app
`[04:09]` and a similar level of debugging, Opus
`[04:11]` 4.7 burned through 173,000
`[04:14]` tokens, while GPT 5.5 used only 82,000.
`[04:18]` This is because GPT 5.5 gets work done
`[04:21]` in fewer tokens and far fewer retries.
`[04:23]` So, Codex lasted significantly longer
`[04:25]` and turned out to be far more
`[04:26]` cost-efficient for the same work. But
`[04:28]` before we move forwards, let's have a
`[04:30]` word by our sponsor, Stream. You're
`[04:32]` building an app and your users need to
`[04:33]` talk, Stream and connect. You try
`[04:35]` handling that yourself, 3 months later,
`[04:37]` you're still debugging instead of
`[04:38]` shipping. Stream skips all of that.
`[04:40]` Stream gives you everything out of the
`[04:42]` box from in-app chat and video calling
`[04:44]` to activity feeds and AI moderation, so
`[04:46]` you're shipping features, not building
`[04:48]` infrastructure from scratch. We're
`[04:49]` talking WhatsApp-style messaging,
`[04:51]` Zoom-style video calls, and
`[04:52]` Instagram-style feeds all built in. What
`[04:55]` really stands out is Stream's new
`[04:56]` launch, Vision Agents. You can build
`[04:58]` intelligent AI agents that see, hear,
`[05:00]` and act on live video and audio, all in
`[05:03]` Python with just a few lines of code.
`[05:05]` Everything runs on a global edge network
`[05:07]` for low latency everywhere. From
`[05:08]` startups to scaling apps, leading
`[05:10]` platforms across social, fitness, and
`[05:12]` community rely on Stream to power over a
`[05:14]` billion end users. If you're a developer
`[05:16]` building the next big app, Stream scales
`[05:19]` with you from day one. Start for free at
`[05:21]` getstream.io. Links in the pinned
`[05:23]` comment. The real test for the two
`[05:25]` models is on how they build products. As
`[05:27]` we said before, GPT 5.5 is faster and
`[05:30]` consumes fewer tokens, so it ships
`[05:32]` working apps quicker. Opus 4.7 spends
`[05:34]` more tokens on thinking, plans deeper,
`[05:36]` and iterates on all aspects of the app
`[05:38]` at the same time. Planning was the first
`[05:40]` thing we wanted to test. We've been
`[05:42]` using Claude Code's planning mode for a
`[05:44]` long time. It It most things, has some
`[05:46]` flaws, but is still quite usable. So, we
`[05:48]` wanted to see how GPT-5.5 performs at
`[05:51]` planning because OpenAI claims it does
`[05:53]` better at planning tasks and executing
`[05:55]` them. We enabled plan mode and opened it
`[05:57]` in a folder that already contained a
`[05:59]` back-end for an app, an API built using
`[06:01]` FastAPI, and asked it to build the
`[06:03]` front-end for it. It explored the
`[06:05]` project thoroughly and asked a few
`[06:06]` questions, but the questions were fairly
`[06:08]` simple. It could have gone deeper into
`[06:10]` how we wanted the front-end to look
`[06:12]` because for front-end work, that
`[06:13]` matters. The plan it produced was very
`[06:15]` simple. It included a summary of the
`[06:17]` main flow, the key changes, the pages to
`[06:19]` add, and how to test them. The one thing
`[06:21]` it did well was clearly separating its
`[06:23]` assumptions, so we knew exactly what it
`[06:25]` was taking for granted. We told it to
`[06:26]` proceed and it finished in about 8
`[06:28]` minutes. The same task on Claude Code
`[06:30]` took 24 minutes, but Opus 4.7's plan was
`[06:33]` much more in-depth, considered more
`[06:34]` aspects of the application, and even
`[06:36]` pulled in Shadcn UI to improve the user
`[06:38]` experience. So, Opus 4.7 does better in
`[06:41]` terms of planning. Next, [snorts] we
`[06:43]` wanted to test both on a greenfield app.
`[06:45]` We gave them the same prompt, that is to
`[06:47]` create a monorepo with a Python Flask
`[06:49]` back-end and a Next.js front-end along
`[06:52]` with the full pipeline and key
`[06:53]` requirements for how the app should
`[06:55]` work. Claude Code switched into planning
`[06:57]` mode by itself because of its harness
`[06:59]` design. Codex did not switch into
`[07:01]` planning mode and instead started
`[07:02]` implementing directly. It finished much
`[07:04]` faster than Claude Code, which took
`[07:06]` around 16 minutes because of the
`[07:07]` planning step. GPT-5.5's
`[07:10]` version of the app had a much simpler UI
`[07:12]` and mainly focused on making sure the
`[07:14]` app worked. It didn't work properly at
`[07:15]` the start, so we debugged it
`[07:17]` iteratively. One thing we noticed was
`[07:18]` that the interview prompts were
`[07:20]` hardcoded because we hadn't provided any
`[07:22]` API key. The prompt specified using the
`[07:24]` Gemini API as a back-end, but since no
`[07:26]` key was available, it implemented a
`[07:28]` fallback so the app wouldn't crash
`[07:30]` completely. Codex had actually used
`[07:31]` local follow-up questions without any
`[07:33]` explicit prompting. We liked this
`[07:35]` because fallback mechanisms like these
`[07:37]` are useful in production since they
`[07:39]` prevent crashes. After a few iterations
`[07:41]` and adding the API key, the app's flow
`[07:43]` worked properly even though the UI was
`[07:45]` still simple. So, GPT-5.5
`[07:47]` looked at the edge cases and implemented
`[07:49]` mechanisms to fill in the gaps. Opus 4.7
`[07:52]` on the other hand, asked us to give it
`[07:54]` the API key before it started
`[07:56]` implementation and built the entire app
`[07:58]` around that. So, Opus 4.7, unlike
`[08:00]` GPT-5.5, didn't prepare for fallbacks
`[08:03]` and just needed everything available up
`[08:05]` front. Due to this, when the API wasn't
`[08:07]` actually there, the app had no fallback
`[08:09]` and just gave an error. Claude Code does
`[08:11]` focus on user experience and
`[08:12]` functionality together, so its
`[08:14]` implementation looked more realistic.
`[08:16]` This is Opus 4.7's UI strength showing
`[08:19]` up, which we covered in our previous
`[08:20]` video where we said Opus 4.7 is way
`[08:23]` better at handling the UI, but its
`[08:24]` implementation also had issues. When we
`[08:26]` asked it to debug, it didn't directly
`[08:28]` inspect the implementation like Codex
`[08:30]` did. Instead, it started asking us
`[08:32]` questions about what might be causing
`[08:34]` the problem and relied on our testing.
`[08:36]` It added debug points like indicators in
`[08:38]` the UI and console logs and asked us to
`[08:40]` check states and report back. After a
`[08:42]` back and forth, it eventually fixed the
`[08:44]` issue and the interview feature worked.
`[08:45]` We preferred how Codex used the agent
`[08:47]` browser to debug on its own. So, in
`[08:49]` terms of autonomous working, Codex's
`[08:51]` implementation was better and in terms
`[08:53]` of user experience, Claude Code did a
`[08:55]` way better job. We also wanted to test
`[08:57]` how both handle the init command. Claude
`[08:59]` Code's init runs without expanding the
`[09:01]` prompt inline. It creates a simple
`[09:03]` Claude.md file that's around 90 lines
`[09:06]` and includes architecture, app flow,
`[09:08]` front end and back end structure, and
`[09:10]` all required commands to run the app. A
`[09:12]` lot of that information is redundant and
`[09:13]` doesn't really benefit the agent, which
`[09:15]` is why it isn't always necessary to keep
`[09:17]` all of it. Codex's setup was more
`[09:19]` refined. It included commit guidelines,
`[09:21]` pull request guidelines, and security
`[09:23]` instructions properly while keeping the
`[09:25]` project structure section brief instead
`[09:27]` of overloading it with detail. Neither
`[09:29]` was perfect, but Codex handled agents.md
`[09:31]` was perfect, but Codex handled agents.md better.
`[09:32]` better.
`[09:32]` &gt;&gt; Now, we also wanted to test how both
`[09:34]` perform on code review. We gave the same
`[09:36]` prompt for a reliability review to both
`[09:38]` Codex and Claude code, asking them to
`[09:40]` document the review in separate files
`[09:42]` while working on the same code base.
`[09:44]` Once both had generated their reports,
`[09:46]` we opened a new session and asked Claude
`[09:48]` to output the diff between the two files
`[09:50]` comparing the findings. Claude's review
`[09:52]` was much more detailed. It organized
`[09:53]` every finding by priority and included
`[09:55]` components, the exact code snippets
`[09:57]` behind the issues. Codex's report
`[09:59]` mentioned line numbers but did not
`[10:01]` include the actual code snippets. Both
`[10:03]` reports were thorough, sharing several
`[10:05]` findings while each caught a few the
`[10:07]` other missed. Claude code also reported
`[10:09]` security issues like a leaked API key
`[10:11]` and a vulnerability. The task was a
`[10:13]` reliability review though, and those
`[10:15]` issues were outside the scope. Claude
`[10:17]` code reported every extra problem it ran
`[10:19]` into along the way, while Codex stayed
`[10:21]` strictly on reliability. So, Codex's
`[10:23]` report was more aligned with the
`[10:24]` original request, while Claude code's
`[10:26]` was broader but less focused on the
`[10:27]` specific task. If we had to describe
`[10:29]` both in terms of building, GPT 5.5 feels
`[10:33]` more like a back-end engineer focused on
`[10:35]` getting the application's functionality
`[10:37]` delivered correctly first, while Opus
`[10:39]` 4.7 feels more like a full-stack
`[10:41]` engineer trying to balance both
`[10:42]` functionality and user experience. On
`[10:45]` [snorts] context management, Codex
`[10:46]` performed much better than Claude code.
`[10:48]` Claude code has in-session context
`[10:50]` editing, which removes tool calls and
`[10:52]` reasoning steps that no longer matter
`[10:54]` from the conversation. It clears
`[10:55]` redundant information from the session
`[10:57]` to avoid bloat. The compaction isn't
`[10:59]` perfect, but at least it doesn't keep
`[11:01]` unnecessary parts in the context while
`[11:03]` compacting. Codex doesn't edit their
`[11:04]` context. It compacts the entire
`[11:06]` conversation just as it took place. The
`[11:08]` one thing it does better is preserving
`[11:10]` the last 20,000 tokens in memory and not
`[11:12]` compacting that portion at all. That
`[11:14]` helps prevent performance degradation in
`[11:16]` Codex after compaction, so that the
`[11:18]` conversation can flow smoothly from the
`[11:20]` next prompt onward. We tested its
`[11:21]` performance and Codex performed better
`[11:23]` after compaction than Claude code did.
`[11:25]` So, even though Claude code follows a
`[11:27]` more detailed, multi-step compaction
`[11:29]` process, Codex's preserved tail keeps
`[11:31]` the agent more useful in practice.
`[11:33]` Memory works differently between the
`[11:34]` two. Cloud Code's harness is mostly
`[11:36]` stateless across sessions, meaning each
`[11:38]` session starts without any context from
`[11:40]` the previous one. It now has a memory
`[11:42]` feature that can store persistent
`[11:44]` preferences or instructions. So, if we
`[11:46]` tell it to avoid doing something a
`[11:47]` certain way, it stores that and applies
`[11:49]` it again later within the same project.
`[11:51]` That helps when working repeatedly in a
`[11:53]` single project, but the memory is
`[11:55]` project-scoped. So, switching projects
`[11:57]` loses that stored behavior. Codex takes
`[11:59]` the opposite route. It consolidates
`[12:01]` information from multiple sessions over
`[12:03]` time and builds a global memory across
`[12:05]` interactions. So, it can retain patterns
`[12:07]` beyond a single project. That can help
`[12:08]` consistency across different tasks. So,
`[12:11]` in short, Cloud Code keeps memory more
`[12:13]` contained within a project, while Codex
`[12:15]` takes a more cross-session,
`[12:16]` cross-project approach, which changes
`[12:18]` how each of them adapts over time. Since
`[12:20]` Cloud Code has been around for longer
`[12:22]` and is being developed constantly to
`[12:24]` improve developer experience, it has
`[12:25]` more to offer compared to Codex. Cloud
`[12:27]` Code has a hook system, which lets us
`[12:29]` run our own scripts at specific points
`[12:31]` in the agent's life cycle, like before
`[12:33]` or after a tool runs, among other points
`[12:36]` for things like blocking unsafe
`[12:37]` commands, running formatters, and more.
`[12:39]` We can also run sub-agents in a
`[12:41]` dedicated work tree, so their
`[12:42]` performance doesn't affect each other.
`[12:44]` We can control the effort level for the
`[12:45]` models, and we can even use keywords
`[12:47]` like ultra think to push reasoning to
`[12:49]` its maximum on a specific task. None of
`[12:52]` that has an equivalent in Codex right
`[12:53]` now. The ecosystem is the other clear
`[12:55]` win for Cloud Code. We can run sessions
`[12:57]` through the Cloud desktop app and
`[12:59]` delegate tasks from the mobile app.
`[13:01]` Across Cloud Code, the desktop app, web
`[13:03]` app, and browser extensions, the surface
`[13:05]` is much wider than Codex, which mainly
`[13:08]` consists of a web app and a desktop app
`[13:10]` that was only recently released and
`[13:12]` didn't feel as strong at the time we
`[13:13]` tested it. Sessions also move between
`[13:15]` environments more easily on Cloud Code,
`[13:17]` which makes it more convenient to work
`[13:19]` across different interfaces. Codex also
`[13:21]` has many interesting features. In the
`[13:22]` cloud, it has an attempt flag that runs
`[13:24]` the same task n times. It produces
`[13:27]` several implementations and selects the
`[13:29]` best one. Claude Code can do something
`[13:30]` similar, but only through configurations
`[13:32]` and instructions, not as a flag. The
`[13:34]` other Codex-only feature, which sets it
`[13:36]` apart from the rest, is its integration
`[13:38]` with OpenAI's image models. It can use
`[13:40]` them directly in the CLI to generate
`[13:42]` images for the websites it's working on.
`[13:44]` Claude relies mostly on SVG-based
`[13:46]` generation for visuals, which doesn't
`[13:48]` even compete on quality because it
`[13:50]` doesn't have any image model yet. If
`[13:52]` we're building a UI that needs real
`[13:53]` imagery, Codex is the only one of the
`[13:55]` two that does it without even being
`[13:57]` explicitly told to. Also, if you are
`[13:59]` enjoying our content, consider pressing
`[14:01]` the hype button because it helps us
`[14:03]` create more content like this and reach
`[14:05]` out to more people. Both [snorts] use
`[14:07]` sub-agents, even though the concept was
`[14:09]` introduced by Claude first. Since it
`[14:10]` came first in Claude Code, its
`[14:12]` integration is more mature because it
`[14:14]` has been agent-centric and focused on
`[14:16]` the coding experience for way longer
`[14:18]` than OpenAI. It supports agents that can
`[14:20]` be orchestrated through remote sessions,
`[14:22]` while Codex mainly supports multi-agent
`[14:24]` workflows inside the terminal
`[14:26]` environment. The biggest difference is
`[14:27]` how each invokes sub-agents. Claude Code
`[14:30]` can spawn agents without explicit
`[14:32]` invocation, while Codex only creates an
`[14:34]` agent if we explicitly ask for one in
`[14:37]` the prompt. When Codex spawns agents, it
`[14:39]` names them and pass them a proper prompt
`[14:41]` as well. In coding performance, the two
`[14:43]` are fairly similar, but the design
`[14:44]` choices behind them are different.
`[14:46]` Claude Code sub-agents use an explicit
`[14:48]` allow list, meaning the parent agent
`[14:50]` defines exactly which tools the
`[14:51]` sub-agent can access, while Codex
`[14:53]` sub-agents inherit tool access from the
`[14:55]` parent by default. Claude Code also
`[14:57]` gives every sub-agent a completely fresh
`[15:00]` context window. A sub-agent doesn't have
`[15:02]` access to the conversation history and
`[15:04]` only sees the prompt from the parent,
`[15:05]` plus the system prompt and any global
`[15:07]` rules because Claude focuses on context
`[15:10]` isolation. Codex CLI does the opposite.
`[15:12]` It forks the full history into the
`[15:14]` sub-agent session with the parent's
`[15:16]` prompt layered on top. Codex agents
`[15:18]` retain more context about what's already
`[15:20]` been discussed, which does help improve
`[15:22]` their performance. In practice, Claude
`[15:23]` code strict isolation hurt our research
`[15:26]` sub-agents. When we used them, the
`[15:27]` results weren't good enough because they
`[15:29]` only saw the immediate prompt and didn't
`[15:31]` have any prior context. Codex agents get
`[15:34]` the whole history, can iterate more
`[15:36]` effectively, and perform better on tasks
`[15:38]` where continuity matters. That brings us
`[15:40]` to the end of this video. If you'd like
`[15:41]` to support the channel and help us keep
`[15:43]` making videos like this, you can do so
`[15:45]` by using the Super Thanks button below.
`[15:47]` As always, thank you for watching and
`[15:49]` I'll see you in the next one.
