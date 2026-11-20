# Stop Prompting Claude. Start Loop Engineering.

- **Source:** https://www.youtube.com/watch?v=YAS4ojuhbW4
- **Uploader:** Austin Marchese
- **Uploaded:** 2026-06-19
- **Duration:** 12:15
- **Method:** YouTube captions (no transcription needed)

## Transcript

Boris Cherny, the creator of Claude code, just said something that should change how you use AI forever. He said, "I don't prompt Claude anymore. My job is to write loops." Then I found a tweet from Peter Steinberg, the creator of Open Claude, saying the exact same thing. You shouldn't be prompting coding agents anymore. You should be designing loops that prompt your agents. There's endless AI hype out there, but when two people who literally build the tools that we're using tell you to stop prompting and start building loops, I listen. So, I went deep on loop engineering and realized something. It's actually really simple. Most people just overcomplicate it. So, in this video, I'm breaking loop engineering down into three parts. Part one, what a loop actually is and when to use them. Part two, the four things every successful loop needs. And part three, the most important part, how you will build your first loop today, even if you have no technical experience. So, part one, what actually is a loop and how does it compare to a normal prompt? Unlike a normal prompt, which runs once and then stops, a loop is a prompt that runs over and over again until a specific task or goal is complete. Listen to how Boris thinks about his day-to-day now. &gt;&gt; Now, what's actually leveled up, I think again, to the next level of abstraction, where I don't prompt Claude anymore. I have loops that are running. They're the ones that are prompting Claude and kind of figuring out what to do. My job is to write loops. &gt;&gt; So, it's clear. Instead of prompting Claude 100 times to complete a task, you should now be thinking about how to create loops to accomplish clear goals. This sounds great, but when should you actually use it? Well, there's a four-condition test that I run when determining if I should create a loop or not. The first condition is, does the task repeat? For any one-time task, just use a prompt. Second is, is there a clear definition of done? When I was the COO of a $25 million tech startup, whatever task we were doing, we wanted to have a clear definition of how we would quantify if the task was done. And a lot like humans doing tasks, the most successful loops have a clear definition of done and a way to verify the results. Now, this is an art and not necessarily a science, and we'll cover that in a bit. Three is, can you afford to be wasteful? So, loops will automatically prompt itself until a task is complete. So, it can use a lot of tokens. Now, there's ways to limit this, which we will cover, but if you're always running into token limit issues, you want to be a bit more strategic using this. And four is, does the loop have all the necessary tools to complete a task? For example, if you're making a website, does it have the ability to check that the website is live and accessible to anyone? These tools will be used in the verification and the implementation process. If the answer is yes to all four of these conditions, you now have a candidate for building a loop. Here is a prompt to audit your workspace and rank your loop candidates using this four condition test. The prompt's on screen, and you know what loops are, and you conceptually understand when to use them. But, how do you build a loop that actually works? Part two is the four building blocks for successful loops. The first block is the trigger. This is what starts your loop. Every loop needs a trigger. This is the thing that kicks it off. And there are a lot of ways to set this up, but these are the three simplest ways. The first is actually {slash} loop. If you type {slash} loop into Claude, it will let you automatically run something at a set interval. For example, {slash} loop every six hours, check today's weather and notify me if I need to change my plans based on my calendar. This is nice because it's very simple, but it's running on your local machine. So, if you close your laptop, it'll just stop. The second is {slash} schedule. This lets you run something automatically in the cloud at any time or day in whatever cadence you want. So, you can run the prompt that I had just mentioned for the loops, but instead have it run at 8:00 a.m. every day, and it'll run remotely instead of on your machine. And the third is custom loop orchestration skills. It's a mouthful, but this is actually how I run all of my loops. I create a single loop orchestration skill that I run that kicks off the entire loop. It has all of the settings configured about what the goal is, how to complete the loop, how to verify it. In that same weather example I mentioned, I would have a single skill that would be {slash} check weather loop, and I would just type that into my terminal, and I would hit enter. Here's a prompt to help you create that custom loop orchestration skill. Block one is a trigger, and the next block is about actually doing the work. And I know we're going through these concepts pretty quickly, so I put together a free 5-day email series where I walk through a lot of the concepts we cover in this video. That's linked below and based on over 6,000 people that have gone through it, I'm highly confident that you're going to love it. But, if you don't, you can unsubscribe at any time. Block two is the execution skills. I have extensive videos on my channel about Claude skills, but in short, it is a save set of instructions that allows Claude to run the same thing every single time. Simply put, it's like a prompt that you have saved that you can easily rerun instead of having to type it. In the first block, we created a {slash} check weather loop and orchestration skill that runs the whole loop. Execution skills are different. These are the things that actually do the task. Each one is a single specialized job the orchestration calls. Of the four building blocks I'm going to cover, this is the most important. In my eyes, the rule is simple. You don't build a loop without battle-tested skills behind it. The reason for this is these skills know exactly how you want to get a task done. Back to the check weather loop. Say you didn't have a {slash} analyze workout skill, AI would just say, "It's raining, cancel your run." But, if I had a {slash} analyze workout skill that documented that I actually love running in the rain, the response would be entirely different. And this is why I use skill-driven loop development. Any loop I create has to have existing skills that I've already battle-tested. Here's a prompt to identify which skills make sense for your workspace. This will look at the current skills that you've already established and suggest loops based on those skills. This strategy is so important and it comes into play in the next block. Block number three is the goal and the verification. Every loop needs two things tied together. A goal, what you want done, and a verification, the rule that confirms you completed the goal. These go together, right? You can't have a goal unless you're able to verify the goal was complete. So, here's how you can do this for both technical and non-technical tasks. The technical example is a lot more straightforward. The goal could be launch a website to this domain and make sure it loads in under 2 seconds. To verify, AI could hit that specific domain, make sure it can see the content that it expects, calculate the load time, and then make sure that the {slash} engineer review skill approves all the changes. AI will then know exactly what's needed and then can verify the results and repeat in a loop until it's complete. So that's for technical tasks, but what about for non-technical things? Well, this is where it becomes a bit of an art, not a science. You need to bridge the abstract to verifiable. Look at the end of the technical example that I just mentioned. The slash engineer review skill has to approve the changes. How does a loop actually know if code is good or not? Well, AI is very good at writing code, so it could just say approved or not approved. The skill engineer review is set up to bridge the abstract if code is good to something verifiable, approved or not approved. And we used it in a technical example, but this is actually the key to creating loops for non-technical tasks. You have to figure out a way to verify the final result, even if it's not quantifiable. So for example, let's say you have a slash draft emails loop. The goal could be for any unread email draft response. The verification could be make sure all emails that don't have a response have a draft, and that draft has been verified by the slash email review skill, the slash writing voice skill, and the slash fact checker skill. You've now established key things you want to verify that are inherently abstract, but you've created a bridge to make them verifiable. And yes, quantifiable tasks are easier, no question. But if you choose the right non-technical task that you already have skills for, those can easily become quantifiable. And this is exactly why skill-driven loop development matters so much because once you have a skill, you can actually convert it to include a verification element. And this verification element could be at the end of the output from that skill, you could say approved or not approved, or a score from 1 to 10, etc. Here is a prompt that I've run in the past to help me convert a normal skill to a skill that can help with verification. And one pro tip here with the goals and the verification and all of this, if you can have different AI analyze the output, you'll be able to get a less biased opinion. One easy way you can do this in Claude is you could use the Codex plugin or you can have Claude spin up sub agents to analyze the work. Here's a prompt to enforce separate agent verification within your loop orchestration skills. Block four, the output and the memory. The output is obvious, right? A loop produces something, a document, updates code base, live site, Telegram messages, whatever you want the loop to produce. The non-obvious thing here that most people miss is the memory. Every loop starts from scratch unless you record what happened. And no memory means that there's no improvement and you'll end up wasting tokens because you keep hitting the same issues over and over again. Adadi Asmani has one line that sticks with me. The agent forgets, the repo doesn't. And from Anthropic docs, they say, "Provide a place to write notes, as simple as a markdown file." And so you really don't need to overthink this thing, but you need to document what the results of the loop are. Just use this prompt, which will update any of your loop orchestration skills, to write any lessons learned and run history in a specific document. Here you can see the prompt. It'll create an output and memory files. Now we know the four key building blocks, a trigger, execution skills, goals and verification, and output and memory. And before we apply this to build our first loop end-to-end, if this is your first video of mine, welcome the channel. But if this is your second or more, here is our anti-slop agreement. The visuals, the testing, the hours of research that went into this, this is entirely built for humans like you, not for AI robot scrapers. So all I ask is you subscribe as part of this agreement to help this content reach more people so I can keep doing these videos. Also, every video I give away a Claude Max subscription. So comment below with what you're building to enter. This video's winner is the goat, Bob Dobbs, who's working on a home management app. All right, that's enough of that. Let's go to part three, build your first loop today. The key here is you need to start small and follow skill-driven loop development. Ask yourself, what is the smallest thing you've already done and proved works that you can create a loop for. Once you've identified that, use the four condition test that I mentioned earlier, which again, quickly you can see on screen. And if it passes all that, it's time to create a loop. So if you already have an idea, here is a prompt to build out a loop with all of the concepts that I've mentioned in this video. Baked into that is everything that I've covered. Now, if you have no idea what to build, here is a prompt that leans on skill-driven loop development to identify candidates from your past session history. For either of these prompts and for any prompt that I covered in this or previous videos, screenshot it and then just send it into Claude and that's essentially the same as writing the prompt. And the best part of what this will create, which is a skill, is you don't have to think about using /loop or /goal to establish goals. You just get the loop orchestration skill that abstracts all of this complexity away from you. You just type that into Claude, hit enter, and then monitor the results. When you do this, one of my favorite features is that you'll notice both of these prompts have one important guardrail. I call it loop training mode. So, the first couple times you use a new loop, you want to make sure the loop pauses at every step until you approve the process. The reason for this is you want to verify that it's actually doing what you want it to be doing and it's not just burning through all of your tokens. When you have this loop training mode set up, the output could look something like this. Quick check before I burn the tokens. Then it waits for your approval and continues on the process. After you've done this and you know that the loop is doing what you want it to do, you can just turn testing mode off by running this prompt. And this is really important because you're going to get a deeper understanding of the process and ultimately these tokens aren't free, so this will save you money and it will save you time because you'll know the output is what you want. Now, before you go crazy with all these loops, I have one rule of thumb. If a goal is less quantifiable, then you need to break down loops into much smaller goals where the output is at key checkpoints in the process. Think of AI like an intern. If you just said, "Plan a corporate party," it could do anything, but you would probably want to have key checkpoints at what date to pick, where the venue is, and the theme of the party. And as somebody who throws an annual Christmas party, that's the party of the year in New York City, I I know how to throw a party, it needs a theme. But anyway, those decisions shape the entire party. It's the same with loops. What are the key moments where if the loop picks the wrong direction, the rest of the loop is entirely shot? Those are your human verification checkpoints. Ultimately, the more of these key verification checkpoints that you don't actually verify, the more the AI can go off course. So, be very mindful of that, specifically for non-measurable tasks. With all that, my favorite thing about loop engineering is the problem-solving muscle it'll force you to flex. So, go pick something small and build a loop orchestration skill for it. Now, if you like this video, you will love this video where I do a deep dive on the only Claude skills you need to 10x your output. The topics I cover there will help your loops go from good to great. I'll see you in the next one. Peace.

## Timestamped

`[00:01]` Boris Cherny, the creator of Claude
`[00:01]` code, just said something that should
`[00:03]` change how you use AI forever. He said,
`[00:05]` "I don't prompt Claude anymore. My job
`[00:06]` is to write loops." Then I found a tweet
`[00:08]` from Peter Steinberg, the creator of
`[00:09]` Open Claude, saying the exact same
`[00:11]` thing. You shouldn't be prompting coding
`[00:13]` agents anymore. You should be designing
`[00:15]` loops that prompt your agents. There's
`[00:16]` endless AI hype out there, but when two
`[00:18]` people who literally build the tools
`[00:19]` that we're using tell you to stop
`[00:21]` prompting and start building loops, I
`[00:23]` listen. So, I went deep on loop
`[00:25]` engineering and realized something. It's
`[00:26]` actually really simple. Most
`[00:28]` people just overcomplicate it. So, in
`[00:30]` this video, I'm breaking loop
`[00:31]` engineering down into three parts. Part
`[00:33]` one, what a loop actually is and when to
`[00:35]` use them. Part two, the four things
`[00:38]` every successful loop needs. And part
`[00:40]` three, the most important part, how you
`[00:42]` will build your first loop today, even
`[00:44]` if you have no technical experience. So,
`[00:46]` part one, what actually is a loop and
`[00:48]` how does it compare to a normal prompt?
`[00:49]` Unlike a normal prompt, which runs once
`[00:51]` and then stops, a loop is a prompt that
`[00:54]` runs over and over again until a
`[00:56]` specific task or goal is complete.
`[00:58]` Listen to how Boris thinks about his
`[00:59]` day-to-day now.
`[01:00]` &gt;&gt; Now, what's actually leveled up, I think
`[01:02]` again, to the next level of abstraction,
`[01:03]` where I don't prompt Claude anymore. I
`[01:06]` have loops that are running. They're the
`[01:07]` ones that are prompting Claude and kind
`[01:09]` of figuring out what to do. My job is to
`[01:11]` write loops.
`[01:11]` &gt;&gt; So, it's clear. Instead of prompting
`[01:13]` Claude 100 times to complete a task, you
`[01:15]` should now be thinking about how to
`[01:16]` create loops to accomplish clear goals.
`[01:18]` This sounds great, but when should you
`[01:19]` actually use it? Well, there's a
`[01:20]` four-condition test that I run when
`[01:22]` determining if I should create a loop or
`[01:24]` not. The first condition is, does the
`[01:26]` task repeat? For any one-time task, just
`[01:28]` use a prompt. Second is, is there a
`[01:29]` clear definition of done? When I was the
`[01:31]` COO of a $25 million tech startup,
`[01:33]` whatever task we were doing, we wanted
`[01:35]` to have a clear definition of how we
`[01:37]` would quantify if the task was done. And
`[01:39]` a lot like humans doing tasks, the most
`[01:41]` successful loops have a clear definition
`[01:43]` of done and a way to verify the results.
`[01:46]` Now, this is an art and not necessarily
`[01:47]` a science, and we'll cover that in a
`[01:49]` bit. Three is, can you afford to be
`[01:51]` wasteful? So, loops will automatically
`[01:53]` prompt itself until a task is complete.
`[01:55]` So, it can use a lot of tokens. Now,
`[01:57]` there's ways to limit this, which we
`[01:58]` will cover, but if you're always running
`[02:00]` into token limit issues, you want to be
`[02:02]` a bit more strategic using this. And
`[02:04]` four is, does the loop have all the
`[02:05]` necessary tools to complete a task? For
`[02:08]` example, if you're making a website,
`[02:09]` does it have the ability to check that
`[02:11]` the website is live and accessible to
`[02:13]` anyone? These tools will be used in the
`[02:14]` verification and the implementation
`[02:16]` process. If the answer is yes to all
`[02:18]` four of these conditions, you now have a
`[02:20]` candidate for building a loop. Here is a
`[02:21]` prompt to audit your workspace and rank
`[02:24]` your loop candidates using this four
`[02:26]` condition test. The prompt's on screen,
`[02:28]` and you know what loops are, and you
`[02:29]` conceptually understand when to use
`[02:31]` them. But, how do you build a loop that
`[02:33]` actually works? Part two is the four
`[02:35]` building blocks for successful loops.
`[02:37]` The first block is the trigger. This is
`[02:39]` what starts your loop. Every loop needs
`[02:41]` a trigger. This is the thing that kicks
`[02:43]` it off. And there are a lot of ways to
`[02:44]` set this up, but these are the three
`[02:45]` simplest ways. The first is actually
`[02:47]` {slash} loop. If you type {slash} loop
`[02:49]` into Claude, it will let you
`[02:50]` automatically run something at a set
`[02:52]` interval. For example, {slash} loop
`[02:54]` every six hours, check today's weather
`[02:56]` and notify me if I need to change my
`[02:58]` plans based on my calendar. This is nice
`[03:00]` because it's very simple, but it's
`[03:01]` running on your local machine. So, if
`[03:02]` you close your laptop, it'll just stop.
`[03:04]` The second is {slash} schedule. This
`[03:05]` lets you run something automatically in
`[03:07]` the cloud at any time or day in whatever
`[03:10]` cadence you want. So, you can run the
`[03:11]` prompt that I had just mentioned for the
`[03:13]` loops, but instead have it run at 8:00
`[03:14]` a.m. every day, and it'll run remotely
`[03:16]` instead of on your machine. And the
`[03:17]` third is custom loop orchestration
`[03:19]` skills. It's a mouthful, but this is
`[03:21]` actually how I run all of my loops. I
`[03:23]` create a single loop orchestration skill
`[03:25]` that I run that kicks off the entire
`[03:27]` loop. It has all of the settings
`[03:28]` configured about what the goal is, how
`[03:30]` to complete the loop, how to verify it.
`[03:32]` In that same weather example I
`[03:33]` mentioned, I would have a single skill
`[03:35]` that would be {slash} check weather
`[03:37]` loop, and I would just type that into my
`[03:39]` terminal, and I would hit enter. Here's
`[03:40]` a prompt to help you create that custom
`[03:42]` loop orchestration skill. Block one is a
`[03:44]` trigger, and the next block is about
`[03:46]` actually doing the work. And I know
`[03:47]` we're going through these concepts
`[03:48]` pretty quickly, so I put together a free
`[03:50]` 5-day email series where I walk through
`[03:52]` a lot of the concepts we cover in this
`[03:53]` video. That's linked below and based on
`[03:55]` over 6,000 people that have gone through
`[03:57]` it, I'm highly confident that you're
`[03:58]` going to love it. But, if you don't, you
`[04:00]` can unsubscribe at any time. Block two
`[04:02]` is the execution skills. I have
`[04:03]` extensive videos on my channel about
`[04:05]` Claude skills, but in short, it is a
`[04:07]` save set of instructions that allows
`[04:09]` Claude to run the same thing every
`[04:11]` single time. Simply put, it's like a
`[04:12]` prompt that you have saved that you can
`[04:14]` easily rerun instead of having to type
`[04:16]` it. In the first block, we created a
`[04:17]` {slash} check weather loop and
`[04:19]` orchestration skill that runs the whole
`[04:21]` loop. Execution skills are different.
`[04:23]` These are the things that actually do
`[04:24]` the task. Each one is a single
`[04:26]` specialized job the orchestration calls.
`[04:29]` Of the four building blocks I'm going to
`[04:30]` cover, this is the most important. In my
`[04:32]` eyes, the rule is simple. You don't
`[04:34]` build a loop without battle-tested
`[04:36]` skills behind it. The reason for this is
`[04:38]` these skills know exactly how you want
`[04:40]` to get a task done. Back to the check
`[04:42]` weather loop. Say you didn't have a
`[04:44]` {slash} analyze workout skill, AI would
`[04:46]` just say, "It's raining, cancel your
`[04:48]` run." But, if I had a {slash} analyze
`[04:50]` workout skill that documented that I
`[04:51]` actually love running in the rain, the
`[04:53]` response would be entirely different.
`[04:55]` And this is why I use skill-driven loop
`[04:57]` development. Any loop I create has to
`[04:59]` have existing skills that I've already
`[05:01]` battle-tested. Here's a prompt to
`[05:03]` identify which skills make sense for
`[05:05]` your workspace. This will look at the
`[05:06]` current skills that you've already
`[05:08]` established and suggest loops based on
`[05:10]` those skills. This strategy is so
`[05:12]` important and it comes into play in the
`[05:14]` next block. Block number three is the
`[05:15]` goal and the verification. Every loop
`[05:17]` needs two things tied together. A goal,
`[05:20]` what you want done, and a verification,
`[05:22]` the rule that confirms you completed the
`[05:24]` goal. These go together, right? You
`[05:25]` can't have a goal unless you're able to
`[05:27]` verify the goal was complete. So, here's
`[05:28]` how you can do this for both technical
`[05:30]` and non-technical tasks. The technical
`[05:32]` example is a lot more straightforward.
`[05:34]` The goal could be launch a website to
`[05:36]` this domain and make sure it loads in
`[05:37]` under 2 seconds. To verify, AI could hit
`[05:39]` that specific domain, make sure it can
`[05:41]` see the content that it expects,
`[05:43]` calculate the load time, and then make
`[05:45]` sure that the {slash} engineer review
`[05:47]` skill approves all the changes. AI will
`[05:50]` then know exactly what's needed and then
`[05:52]` can verify the results and repeat in a
`[05:54]` loop until it's complete. So that's for
`[05:56]` technical tasks, but what about for
`[05:57]` non-technical things? Well, this is
`[05:59]` where it becomes a bit of an art, not a
`[06:00]` science. You need to bridge the abstract
`[06:03]` to verifiable. Look at the end of the
`[06:05]` technical example that I just mentioned.
`[06:07]` The slash engineer review skill has to
`[06:09]` approve the changes. How does a loop
`[06:11]` actually know if code is good or not?
`[06:13]` Well, AI is very good at writing code,
`[06:15]` so it could just say approved or not
`[06:17]` approved. The skill engineer review is
`[06:20]` set up to bridge the abstract if code is
`[06:23]` good to something verifiable, approved
`[06:25]` or not approved. And we used it in a
`[06:27]` technical example, but this is actually
`[06:28]` the key to creating loops for
`[06:30]` non-technical tasks. You have to figure
`[06:32]` out a way to verify the final result,
`[06:34]` even if it's not quantifiable. So for
`[06:36]` example, let's say you have a slash
`[06:37]` draft emails loop. The goal could be for
`[06:40]` any unread email draft response. The
`[06:42]` verification could be make sure all
`[06:44]` emails that don't have a response have a
`[06:46]` draft, and that draft has been verified
`[06:48]` by the slash email review skill, the
`[06:50]` slash writing voice skill, and the slash
`[06:53]` fact checker skill. You've now
`[06:54]` established key things you want to
`[06:56]` verify that are inherently abstract, but
`[06:58]` you've created a bridge to make them
`[07:00]` verifiable. And yes, quantifiable tasks
`[07:02]` are easier, no question. But if you
`[07:03]` choose the right non-technical task that
`[07:05]` you already have skills for, those can
`[07:08]` easily become quantifiable. And this is
`[07:10]` exactly why skill-driven loop
`[07:11]` development matters so much because once
`[07:13]` you have a skill, you can actually
`[07:15]` convert it to include a verification
`[07:18]` element. And this verification element
`[07:19]` could be at the end of the output from
`[07:21]` that skill, you could say approved or
`[07:23]` not approved, or a score from 1 to 10,
`[07:26]` etc. Here is a prompt that I've run in
`[07:28]` the past to help me convert a normal
`[07:30]` skill to a skill that can help with
`[07:31]` verification. And one pro tip here with
`[07:33]` the goals and the verification and all
`[07:35]` of this, if you can have different AI
`[07:37]` analyze the output, you'll be able to
`[07:38]` get a less biased opinion. One easy way
`[07:41]` you can do this in Claude is you could
`[07:43]` use the Codex plugin or you can have
`[07:44]` Claude spin up sub agents to analyze the
`[07:46]` work. Here's a prompt to enforce
`[07:48]` separate agent verification within your
`[07:50]` loop orchestration skills. Block four,
`[07:52]` the output and the memory. The output is
`[07:54]` obvious, right? A loop produces
`[07:55]` something, a document, updates code
`[07:57]` base, live site, Telegram messages,
`[08:00]` whatever you want the loop to produce.
`[08:01]` The non-obvious thing here that most
`[08:03]` people miss is the memory. Every loop
`[08:05]` starts from scratch unless you record
`[08:06]` what happened. And no memory means that
`[08:08]` there's no improvement and you'll end up
`[08:10]` wasting tokens because you keep hitting
`[08:11]` the same issues over and over again.
`[08:13]` Adadi Asmani has one line that sticks
`[08:15]` with me. The agent forgets, the repo
`[08:17]` doesn't. And from Anthropic docs, they
`[08:19]` say, "Provide a place to write notes, as
`[08:21]` simple as a markdown file." And so you
`[08:23]` really don't need to overthink this
`[08:24]` thing, but you need to document what the
`[08:26]` results of the loop are. Just use this
`[08:28]` prompt, which will update any of your
`[08:30]` loop orchestration skills, to write any
`[08:32]` lessons learned and run history in a
`[08:34]` specific document. Here you can see the
`[08:36]` prompt. It'll create an output and
`[08:37]` memory files. Now we know the four key
`[08:40]` building blocks, a trigger, execution
`[08:41]` skills, goals and verification, and
`[08:43]` output and memory. And before we apply
`[08:45]` this to build our first loop end-to-end,
`[08:47]` if this is your first video of mine,
`[08:49]` welcome the channel. But if this is your
`[08:50]` second or more, here is our anti-slop
`[08:52]` agreement. The visuals, the testing, the
`[08:54]` hours of research that went into this,
`[08:55]` this is entirely built for humans like
`[08:57]` you, not for AI robot scrapers. So all I
`[09:00]` ask is you subscribe as part of this
`[09:01]` agreement to help this content reach
`[09:03]` more people so I can keep doing these
`[09:05]` videos. Also, every video I give away a
`[09:06]` Claude Max subscription. So comment
`[09:08]` below with what you're building to
`[09:09]` enter. This video's winner is the goat,
`[09:12]` Bob Dobbs, who's working on a home
`[09:14]` management app. All right, that's enough
`[09:16]` of that. Let's go to part three, build
`[09:18]` your first loop today. The key here is
`[09:19]` you need to start small and follow
`[09:21]` skill-driven loop development. Ask
`[09:22]` yourself, what is the smallest thing
`[09:24]` you've already done and proved works
`[09:26]` that you can create a loop for. Once
`[09:27]` you've identified that, use the four
`[09:29]` condition test that I mentioned earlier,
`[09:31]` which again, quickly you can see on
`[09:32]` screen. And if it passes all that, it's
`[09:34]` time to create a loop. So if you already
`[09:36]` have an idea, here is a prompt to build
`[09:38]` out a loop with all of the concepts that
`[09:40]` I've mentioned in this video. Baked into
`[09:42]` that is everything that I've covered.
`[09:43]` Now, if you have no idea what to build,
`[09:45]` here is a prompt that leans on
`[09:47]` skill-driven loop development to
`[09:49]` identify candidates from your past
`[09:51]` session history. For either of these
`[09:53]` prompts and for any prompt that I
`[09:54]` covered in this or previous videos,
`[09:56]` screenshot it and then just send it into
`[09:58]` Claude and that's essentially the same
`[09:59]` as writing the prompt. And the best part
`[10:01]` of what this will create, which is a
`[10:02]` skill, is you don't have to think about
`[10:04]` using /loop or /goal to establish goals.
`[10:07]` You just get the loop orchestration
`[10:08]` skill that abstracts all of this
`[10:10]` complexity away from you. You just type
`[10:12]` that into Claude, hit enter, and then
`[10:13]` monitor the results. When you do this,
`[10:15]` one of my favorite features is that
`[10:17]` you'll notice both of these prompts have
`[10:19]` one important guardrail. I call it loop
`[10:21]` training mode. So, the first couple
`[10:22]` times you use a new loop, you want to
`[10:24]` make sure the loop pauses at every step
`[10:27]` until you approve the process. The
`[10:28]` reason for this is you want to verify
`[10:30]` that it's actually doing what you want
`[10:32]` it to be doing and it's not just burning
`[10:34]` through all of your tokens. When you
`[10:36]` have this loop training mode set up, the
`[10:38]` output could look something like this.
`[10:39]` Quick check before I burn the tokens.
`[10:41]` Then it waits for your approval and
`[10:42]` continues on the process. After you've
`[10:44]` done this and you know that the loop is
`[10:46]` doing what you want it to do, you can
`[10:48]` just turn testing mode off by running
`[10:50]` this prompt. And this is really
`[10:51]` important because you're going to get a
`[10:52]` deeper understanding of the process and
`[10:54]` ultimately these tokens aren't free, so
`[10:56]` this will save you money and it will
`[10:58]` save you time because you'll know the
`[10:59]` output is what you want. Now, before you
`[11:01]` go crazy with all these loops, I have
`[11:03]` one rule of thumb. If a goal is less
`[11:05]` quantifiable, then you need to break
`[11:07]` down loops into much smaller goals where
`[11:10]` the output is at key checkpoints in the
`[11:12]` process. Think of AI like an intern. If
`[11:14]` you just said, "Plan a corporate party,"
`[11:16]` it could do anything, but you would
`[11:18]` probably want to have key checkpoints at
`[11:21]` what date to pick, where the venue is,
`[11:23]` and the theme of the party. And as
`[11:25]` somebody who throws an annual Christmas
`[11:26]` party, that's the party of the year in
`[11:28]` New York City, I I know how to throw a
`[11:29]` party, it needs a theme. But anyway,
`[11:31]` those decisions shape the entire party.
`[11:33]` It's the same with loops. What are the
`[11:35]` key moments where if the loop picks the
`[11:37]` wrong direction, the rest of the loop is
`[11:39]` entirely shot? Those are your human
`[11:42]` verification checkpoints. Ultimately,
`[11:44]` the more of these key verification
`[11:46]` checkpoints that you don't actually
`[11:48]` verify, the more the AI can go off
`[11:50]` course. So, be very mindful of that,
`[11:52]` specifically for non-measurable tasks.
`[11:54]` With all that, my favorite thing about
`[11:56]` loop engineering is the problem-solving
`[11:58]` muscle it'll force you to flex. So, go
`[12:00]` pick something small and build a loop
`[12:02]` orchestration skill for it. Now, if you
`[12:04]` like this video, you will love this
`[12:05]` video where I do a deep dive on the only
`[12:07]` Claude skills you need to 10x your
`[12:09]` output. The topics I cover there will
`[12:11]` help your loops go from good to great.
`[12:13]` I'll see you in the next one. Peace.
