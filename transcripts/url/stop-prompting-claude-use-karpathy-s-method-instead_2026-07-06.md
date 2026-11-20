# Stop Prompting Claude. Use Karpathy's Method Instead.

- **Source:** https://www.youtube.com/watch?v=7zZy1QTvokM
- **Uploader:** Austin Marchese
- **Uploaded:** 2026-06-09
- **Duration:** 13:18
- **Method:** YouTube captions (no transcription needed)

## Transcript

I just listened to Andrej Karpathy speak at AISN 2026, and I learned something that I wasn't expecting. Almost everyone is prompting Claude wrong. So, I decided to dig deeper and see exactly how Karpathy, the former head of AI at Tesla, uses AI in 2026. And it turns out that Karpathy's method for building 10 times faster can be broken down into three simple layers. So, in today's video, I'll be breaking down each layer so that anybody can apply them. And then I'll show you the one thing that Karpathy said to focus on in the age of AI. So, layer one is the spec. AI models are incredibly smart, but they're still missing something. To showcase their current limitation, Karpathy explained a simple question AI will get wrong. &gt;&gt; I want to go to a car wash to wash my car, and it's 50 m away. Should I drive or should I walk? And state-of-the-art models today will tell you to walk because it's so close. &gt;&gt; At first, I actually didn't believe this, so I went to Claude, Gemini, Grok, and ChatGPT, asked them the same question, and they all gave me the same answer. And it reveals the whole foundation of this video. AI is brilliant at what can be measured, but for context-driven things like needing a car for a car wash, it has no signal to act on. So, how do you bridge this gap between your understanding and your contextual information and AI's computational power? That's where the spec comes in. And a spec is how you deliver your understanding to Claude in a format it can use. A term you may have heard is Claude's plan mode, which essentially can be used to help you create a plan before building anything. But Karpathy thinks that this is too But Karpathy thinks that this is too high-level. high-level. &gt;&gt; I actually don't even like the plan mode. I I would I mean, obviously it's very useful, but I think there's something more general here where you have to work with your agent to design a spec that is very agent to design a spec that is very detailed. detailed. &gt;&gt; Now, Karpathy isn't telling you that plan mode is bad. What he's actually saying is you have to go deeper, work with these AI tools to design the actual spec. So, how do you create a spec that Claude can successfully use to build what you're trying to build? The first step is you have to uncover your goal. If you just say, "Create a end-of-month report," that's a task, but the actual goal is a conclusion you're trying to draw, the decision the report drives. And what the goal actually is is something AI will literally never be able to decide. So, to help you do this, we'll tell Claude to interview me to identify the goal of this project. This is the way to get the information out of you and into the spec. Now, step two is be agile with how you work. There are two methods of completing any task. The first is waterfall, and the other is agile. Waterfall is you take a big task and you complete the entire thing, and then you show the final product. Agile on the other hand is you break that same task into small buckets, and you show the result throughout the entire process to make sure you're going in the right direction. And people are extremely susceptible to using AI agents in a waterfall manner because they want to give them everything to do at once. The better move is agile specking. You want to have a tight scope, a clear checkpoint, you want to review the output, adjust it, and then repeat. To help with this, we'll tell Claude to bias towards smaller and more compartmentalized specs. Step three is you want to be precise and use your brain. The more precise you are, the less AI has to assume. And every assumption that AI makes is a chance for it to drift from the final product you actually want. And when you have AI create a spec for you, you have to use your brain to think critically about what that spec actually says. So, to help you use your brain, you can say "Make me verify key decisions explicitly to ensure nothing is missed." And when you put these three pieces together, we have a final prompt we can use in Claude to help create a tightly scoped, to help create a tightly scoped, well-thought-out well-thought-out aligns with our actual goal. This is a process that I call modern engineering, which every successful person has to become. Now, layer two is the verifier. Layer two sits on top of the spec. This is the verification process. One of the most frustrating things about AI is reviewing and verifying the output. And unlike a human, it can't grasp non-measurable things. So, how can we help AI verify its own outputs? Well, first you need to understand the mental model behind this. And Karpathy explains it as animals versus ghosts. Here's him getting asked a question about this in a recent interview. And if it sounds confusing, don't worry, I will simplify it after. &gt;&gt; And the idea is that we're not building animals, we are summoning ghosts. Why does that framing matter? And what does it actually change about how you build and deploy and evaluate or even trust and deploy and evaluate or even trust them? them? &gt;&gt; Yeah, I think the reason I wrote about this is because I'm trying to wrap my head around what these things are, right? Because if you have a good model of what they are or are not, then you're going to be more competent at uh using them. I think it's just um coming to terms with the fact that these things are not, you know, animal intelligences. Like if you yell at them, they're not going to work better or worse or doesn't have any impact. Um and uh it's all just kind of like these statistical simulation circuits. It's more just being suspicious of it and um figuring it out over time. &gt;&gt; Now, that's some gigabrain stuff, but let me simplify it. People, me and you, are used to interacting with people, which Karpathy is calling animals. These animals are driven by different motivators and emotions, which help produce the final product and output within a team setting. And if you say to a person, become an expert at SEO marketing in the next 14 days or you're fired, they're going to figure it out. That's because they have these intrinsic motivations. But AI is not that. Karpathy describes it as a ghost, but in my eyes that's a little too confusing, so throw it out the window. Instead, think of it like a robot librarian. If you ask it that same SEO question, the librarian will only suggest resources and answers based on the books in its library. If it doesn't have a book, it can't help you. And part of the challenge here is that the librarian doesn't know when it's missing a specific book. So, it may just confidently make something up. And that's what's happening when AI nails math and fumbles things with context. It's brilliant because the library has the clear answers. But if it doesn't, then it's confidently wrong or uncertain. Which means interacting with it like it's an animal, i.e. a human, doesn't help, right? Yelling at it, pleading, just saying, "Make this better." doesn't necessarily work. Really, the only lever you have, which most people don't even think to use, is the verification lever. Because by optimizing this, it makes it so that you're playing within the actual rules that the AI follows. So, how do you help AI verify the output so it's up to the standard you want? Well, there are three places to focus on. First, you want to set the evaluation criteria up front. Before Claude touches a single thing, whether that's technical or non-technical tasks, define what good looks like with precision. For example, a vague way to evaluate an output is, "Make this report look good." Whereas, a precise way would say, "The report must have three sections, each ends with a recommendation." And if you're making the connection, this is very similar to what we covered in layer one. The more precise you are up front, the less room Claude will have to make mistakes. To help enforce this, we'll add this to our verification Claude prompt. Outline the evaluation criteria you will use to ensure a high-quality final product. Be precise. The second step is use a second AI model as the critic. Think of this like a second robot librarian from a different library. You use that librarian to grade the output of the first librarian. This other librarian has a whole different set of books, and that may give them insight into why this first librarian is right or wrong. Now, a tactical way to do this, if you use Claude code, you can install the Codex plugin, which will allow you to directly ask Codex questions within your Claude code session. So, you could say something like, "If this turns into a complex build, run the final output by Codex to ensure both systems agree." And step three is pull external signal where possible. The question here is, how can you bring in additional context that will help you verify an output? Here are two concrete examples. Let's say you're deploying an app and you're not sure if it's successfully deployed. What you can do instead is connect your Claude session with your system where it's deployed, so it can verify that it has been deployed successfully. We are making a connection to pull external data to enhance our verification layer. And now, if it says that the deployment was successful, we know for certainty that it actually was. In a non-technical example, let's say you're working on a monthly report. You could bring in your historical reports to use as reference for the exact format that the final output should be in, pulling in data and empowering the verification process. Now, bringing in this concept with the first two points, combining this third point with the first two points, here is a prompt that you can run in Claude, which will help ensure that you are adding a proper evaluation layer where it makes sense. I can't stress how important this is. The creator of Claude code, Boris Cherney, said it best. If Claude has a feedback loop, it will two to three x quality of the final result. So, layer one and layer two are about creating specs and evaluating the output. The third layer, however, is where we build a foundation that can't be replicated. But, before we get to that, if this is your first video of mine, welcome to the channel. If it's your second or more, here is our anti-slop agreement. The visuals, the testing, the hours of research that went into this video, this is entirely built for humans, not for AI clunkers. So, all that I ask is that you subscribe as part of this agreement because it helps it reach more people so that I can keep making videos like this. Also, every couple of weeks, I give away a Claude Max subscription, so comment below with whatever you're building to enter. Layer three, the environment. So, layer one and layer two need somewhere to live, and that's layer three, which is the environment that you build in. Think of this layer as a workshop. The spec is a blueprint pinned to the wall, the verifier is the quality check station by the door, and then the environment is the workshop itself. You need to create the proper tooling and the proper system so that the whole thing can function at a high level. Now, the problem here is that most people use the workshop from scratch every time they use AI. And no, if you have a single chat with your entire conversation history, that is not what I'm talking about. So, how do you create a proper workspace that improves over time? First is you need to set up a proper Claude MD file. Every time you prompt Claude, your Claude.md file gets injected automatically. It's essentially the first thing that Claude reads to help determine how it should operate. For example, you can add to your Claude MD before building anything multi-step, include a verification plan. Now, verification is forced into every build, not something that you have to remember to say. This is just one of the ways that you can improve this Claude MD, and here's actually mine on the screen, and I'm going to call out a couple of sections. The first is I outline how this repo works. So, think of my repo as my workspace. It gives high-level to the details around it. I then tell it the custom skills and how they're routed, how to use them. I then outline the architecture of the training data or knowledge architecture so that the AI knows where to look for certain information. And then I have key working rules that it should follow no matter what. Make this your environment. It's your world, and AI is living in it. It should not feel like the other way around. The second step is you need to build your LLM knowledge base. Karpathy went viral for this concept on Twitter that he calls his LLM knowledge base. And this is essentially creating a folder system on your machine that you're able to ingest your own training data in a way that makes it really easy for Claude to understand where information is. This is so important because your data is your moat. And this begins the process of building out your own intellectual data property. And step three is you have to start building out your skill set. A general rule of thumb that I have is if you plan on doing something repeatedly, create a custom skill for that. Think of this like a handbook to complete a specific task. And the more you use these skills, the better they'll become. I have a saying that I tell my team, the best way to find a leak in a hose is to run water through it. And it's the same with skills. The more you use them, the more you'll realize where you need to fix them and where they're really good. Keep running water through it and your system's going to compound over time. Step four is create rules for what the AI can and can't work on. Depending on the cost of getting something wrong, you need to establish different AI guardrails. So, here's how to think of this, right? So, take the Claude.md file that I mentioned earlier. You could add a line that says, "Don't make up information," but that's a guide, not necessarily a hard rule. So, at the end of the day, AI can still ignore it. So, if you have things that are critical not to get wrong, then you need to introduce rule-based guardrails to ensure that the AI can't bypass them. To help you visualize this, imagine you have a folder called "Important, Don't Edit." You could have a rule in Claude MD that says, "Don't touch anything in the /important, don't edit folder." And that might get you 80% of the way there, but it's essentially a request, not a rule. Claude can still touch those files. So, instead, you add a pre-tool use hook before Claude uses the write or edit tool, and it checks to see the file that it's trying to edit. Now, Claude literally can't make the edit, and it's enforced at the tool level, not the prompt level. And as a result of this, this is now a concrete rule that the agent can't bypass. So, with this in mind, bucket things into three groups. The first is always do. This is things that AI should run on autopilot. The second is ask first. So, this is anything that you want to double-check. And then the third is never do. These are lines that can't be crossed that are absolutely critical not to get wrong. Here's a prompt that brings all of these four points that I mentioned to help audit your system and create an optimized environment for Claude to interact with. That's the Karpathy method end-to-end, the spec, the verifier, and the environment. But there's a question that needs to be answered. What's the one thing that Karpathy thinks we should focus on in the age of AI? Here's him getting asked this in an interview. &gt;&gt; What still remains worth learning deeply when intelligence gets cheap as we move into the next eight era of AI? &gt;&gt; You can outsource your thinking, but you can't outsource your understanding. And the thing with everything we covered here is that the three layers are centered around your understanding of the bigger picture. You need to understand your goals and what's needed to direct AI to start working for you. Now, if you like this video, you will love this one where I do a deep dive into four Claude projects that you need to build today using these three layers. I'll see you over there. Peace.

## Timestamped

`[00:01]` I just listened to Andrej Karpathy speak
`[00:01]` at AISN 2026, and I learned something
`[00:04]` that I wasn't expecting. Almost everyone
`[00:06]` is prompting Claude wrong. So, I decided
`[00:08]` to dig deeper and see exactly how
`[00:09]` Karpathy, the former head of AI at
`[00:11]` Tesla, uses AI in 2026. And it turns out
`[00:14]` that Karpathy's method for building 10
`[00:16]` times faster can be broken down into
`[00:18]` three simple layers. So, in today's
`[00:20]` video, I'll be breaking down each layer
`[00:22]` so that anybody can apply them. And then
`[00:23]` I'll show you the one thing that
`[00:25]` Karpathy said to focus on in the age of
`[00:27]` AI. So, layer one is the spec. AI models
`[00:29]` are incredibly smart, but they're still
`[00:31]` missing something. To showcase their
`[00:33]` current limitation, Karpathy explained a
`[00:35]` simple question AI will get wrong.
`[00:37]` &gt;&gt; I want to go to a car wash to wash my
`[00:39]` car, and it's 50 m away. Should I drive
`[00:42]` or should I walk? And state-of-the-art
`[00:45]` models today will tell you to walk
`[00:46]` because it's so close.
`[00:48]` &gt;&gt; At first, I actually didn't believe
`[00:49]` this, so I went to Claude, Gemini, Grok,
`[00:51]` and ChatGPT, asked them the same
`[00:52]` question, and they all gave me the same
`[00:54]` answer. And it reveals the whole
`[00:55]` foundation of this video. AI is
`[00:57]` brilliant at what can be measured, but
`[01:00]` for context-driven things like needing a
`[01:02]` car for a car wash, it has no signal to
`[01:05]` act on. So, how do you bridge this gap
`[01:07]` between your understanding and your
`[01:08]` contextual information and AI's
`[01:10]` computational power? That's where the
`[01:11]` spec comes in. And a spec is how you
`[01:13]` deliver your understanding to Claude in
`[01:15]` a format it can use. A term you may have
`[01:17]` heard is Claude's plan mode, which
`[01:19]` essentially can be used to help you
`[01:20]` create a plan before building anything.
`[01:22]` But Karpathy thinks that this is too
`[01:25]` But Karpathy thinks that this is too high-level.
`[01:25]` high-level.
`[01:25]` &gt;&gt; I actually don't even like the plan
`[01:27]` mode. I I would
`[01:28]` I mean, obviously it's very useful, but
`[01:30]` I think there's something more general
`[01:31]` here where you have to work with your
`[01:32]` agent to design a spec that is very
`[01:34]` agent to design a spec that is very detailed.
`[01:34]` detailed.
`[01:34]` &gt;&gt; Now, Karpathy isn't telling you that
`[01:36]` plan mode is bad. What he's actually
`[01:38]` saying is you have to go deeper, work
`[01:40]` with these AI tools to design the actual
`[01:42]` spec. So, how do you create a spec that
`[01:44]` Claude can successfully use to build
`[01:46]` what you're trying to build? The first
`[01:48]` step is you have to uncover your goal.
`[01:50]` If you just say, "Create a end-of-month
`[01:52]` report," that's a task, but the actual
`[01:54]` goal is a conclusion you're trying to
`[01:56]` draw, the decision the report drives.
`[01:59]` And what the goal actually is is
`[02:00]` something AI will literally never be
`[02:02]` able to decide. So, to help you do this,
`[02:04]` we'll tell Claude to interview me to
`[02:07]` identify the goal of this project. This
`[02:09]` is the way to get the information out of
`[02:11]` you and into the spec. Now, step two is
`[02:13]` be agile with how you work. There are
`[02:15]` two methods of completing any task. The
`[02:17]` first is waterfall, and the other is
`[02:19]` agile. Waterfall is you take a big task
`[02:22]` and you complete the entire thing, and
`[02:24]` then you show the final product. Agile
`[02:26]` on the other hand is you break that same
`[02:27]` task into small buckets, and you show
`[02:30]` the result throughout the entire process
`[02:32]` to make sure you're going in the right
`[02:33]` direction. And people are extremely
`[02:35]` susceptible to using AI agents in a
`[02:37]` waterfall manner because they want to
`[02:38]` give them everything to do at once. The
`[02:41]` better move is agile specking. You want
`[02:43]` to have a tight scope, a clear
`[02:45]` checkpoint, you want to review the
`[02:46]` output, adjust it, and then repeat. To
`[02:48]` help with this, we'll tell Claude to
`[02:50]` bias towards smaller and more
`[02:51]` compartmentalized specs. Step three is
`[02:54]` you want to be precise and use your
`[02:55]` brain. The more precise you are, the
`[02:57]` less AI has to assume. And every
`[02:59]` assumption that AI makes is a chance for
`[03:01]` it to drift from the final product you
`[03:03]` actually want. And when you have AI
`[03:05]` create a spec for you, you have to use
`[03:07]` your brain to think critically about
`[03:09]` what that spec actually says. So, to
`[03:12]` help you use your brain, you can say
`[03:13]` "Make me verify key decisions explicitly
`[03:16]` to ensure nothing is missed." And when
`[03:18]` you put these three pieces together, we
`[03:20]` have a final prompt we can use in Claude
`[03:22]` to help create a tightly scoped,
`[03:24]` to help create a tightly scoped, well-thought-out
`[03:25]` well-thought-out
`[03:26]` aligns with our actual goal. This is a
`[03:27]` process that I call modern engineering,
`[03:29]` which every successful person has to
`[03:31]` become. Now, layer two is the verifier.
`[03:34]` Layer two sits on top of the spec. This
`[03:36]` is the verification process. One of the
`[03:38]` most frustrating things about AI is
`[03:40]` reviewing and verifying the output. And
`[03:42]` unlike a human, it can't grasp
`[03:44]` non-measurable things. So, how can we
`[03:47]` help AI verify its own outputs? Well,
`[03:49]` first you need to understand the mental
`[03:50]` model behind this. And Karpathy explains
`[03:53]` it as animals versus ghosts. Here's him
`[03:55]` getting asked a question about this in a
`[03:57]` recent interview. And if it sounds
`[03:59]` confusing, don't worry, I will simplify
`[04:00]` it after.
`[04:01]` &gt;&gt; And the idea is that we're not building
`[04:03]` animals, we are summoning ghosts. Why
`[04:05]` does that framing matter? And what does
`[04:07]` it actually change about how you build
`[04:09]` and deploy and evaluate or even trust
`[04:12]` and deploy and evaluate or even trust them?
`[04:12]` them?
`[04:12]` &gt;&gt; Yeah, I think the reason I wrote about
`[04:14]` this is because I'm trying to wrap my
`[04:15]` head around what these things are,
`[04:16]` right? Because if you have a good model
`[04:18]` of what they are or are not, then you're
`[04:19]` going to be more competent at uh using
`[04:21]` them. I think it's just um
`[04:23]` coming to terms with the fact that these
`[04:24]` things are not, you know, animal
`[04:26]` intelligences. Like if you yell at them,
`[04:27]` they're not going to work better or
`[04:29]` worse or doesn't have any impact. Um
`[04:32]` and uh
`[04:33]` it's all just kind of like these
`[04:34]` statistical simulation circuits. It's
`[04:36]` more just being suspicious of it and um
`[04:38]` figuring it out over time.
`[04:39]` &gt;&gt; Now, that's some gigabrain stuff, but
`[04:41]` let me simplify it. People, me and you,
`[04:43]` are used to interacting with people,
`[04:45]` which Karpathy is calling animals. These
`[04:48]` animals are driven by different
`[04:49]` motivators and emotions, which help
`[04:51]` produce the final product and output
`[04:53]` within a team setting. And if you say to
`[04:55]` a person, become an expert at SEO
`[04:57]` marketing in the next 14 days or you're
`[04:59]` fired, they're going to figure it out.
`[05:01]` That's because they have these intrinsic
`[05:03]` motivations. But AI is not that.
`[05:05]` Karpathy describes it as a ghost, but in
`[05:07]` my eyes that's a little too confusing,
`[05:09]` so throw it out the window. Instead,
`[05:10]` think of it like a robot librarian. If
`[05:12]` you ask it that same SEO question, the
`[05:14]` librarian will only suggest resources
`[05:17]` and answers based on the books in its
`[05:19]` library. If it doesn't have a book, it
`[05:21]` can't help you. And part of the
`[05:22]` challenge here is that the librarian
`[05:24]` doesn't know when it's missing a
`[05:26]` specific book. So, it may just
`[05:28]` confidently make something up. And
`[05:29]` that's what's happening when AI nails
`[05:31]` math and fumbles things with context.
`[05:33]` It's brilliant because the library has
`[05:35]` the clear answers. But if it doesn't,
`[05:37]` then it's confidently wrong or
`[05:40]` uncertain. Which means interacting with
`[05:42]` it like it's an animal, i.e. a human,
`[05:44]` doesn't help, right? Yelling at it,
`[05:46]` pleading, just saying, "Make this
`[05:47]` better." doesn't necessarily work.
`[05:49]` Really, the only lever you have, which
`[05:50]` most people don't even think to use, is
`[05:53]` the verification lever. Because by
`[05:55]` optimizing this, it makes it so that
`[05:56]` you're playing within the actual rules
`[05:58]` that the AI follows. So, how do you help
`[06:00]` AI verify the output so it's up to the
`[06:02]` standard you want? Well, there are three
`[06:04]` places to focus on. First, you want to
`[06:06]` set the evaluation criteria up front.
`[06:08]` Before Claude touches a single thing,
`[06:10]` whether that's technical or
`[06:11]` non-technical tasks, define what good
`[06:13]` looks like with precision. For example,
`[06:16]` a vague way to evaluate an output is,
`[06:17]` "Make this report look good." Whereas, a
`[06:20]` precise way would say, "The report must
`[06:22]` have three sections, each ends with a
`[06:24]` recommendation." And if you're making
`[06:25]` the connection, this is very similar to
`[06:27]` what we covered in layer one. The more
`[06:29]` precise you are up front, the less room
`[06:30]` Claude will have to make mistakes. To
`[06:32]` help enforce this, we'll add this to our
`[06:34]` verification Claude prompt. Outline the
`[06:37]` evaluation criteria you will use to
`[06:38]` ensure a high-quality final product. Be
`[06:40]` precise. The second step is use a second
`[06:43]` AI model as the critic. Think of this
`[06:45]` like a second robot librarian from a
`[06:47]` different library. You use that
`[06:49]` librarian to grade the output of the
`[06:51]` first librarian. This other librarian
`[06:53]` has a whole different set of books, and
`[06:55]` that may give them insight into why this
`[06:57]` first librarian is right or wrong. Now,
`[06:59]` a tactical way to do this, if you use
`[07:01]` Claude code, you can install the Codex
`[07:03]` plugin, which will allow you to directly
`[07:05]` ask Codex questions within your Claude
`[07:07]` code session. So, you could say
`[07:09]` something like, "If this turns into a
`[07:10]` complex build, run the final output by
`[07:13]` Codex to ensure both systems agree." And
`[07:15]` step three is pull external signal where
`[07:18]` possible. The question here is, how can
`[07:19]` you bring in additional context that
`[07:21]` will help you verify an output? Here are
`[07:23]` two concrete examples. Let's say you're
`[07:25]` deploying an app and you're not sure if
`[07:26]` it's successfully deployed. What you can
`[07:28]` do instead is connect your Claude
`[07:29]` session with your system where it's
`[07:31]` deployed, so it can verify that it has
`[07:33]` been deployed successfully. We are
`[07:35]` making a connection to pull external
`[07:36]` data to enhance our verification layer.
`[07:40]` And now, if it says that the deployment
`[07:41]` was successful, we know for certainty
`[07:43]` that it actually was. In a non-technical
`[07:45]` example, let's say you're working on a
`[07:47]` monthly report. You could bring in your
`[07:48]` historical reports to use as reference
`[07:50]` for the exact format that the final
`[07:52]` output should be in, pulling in data and
`[07:54]` empowering the verification process.
`[07:56]` Now, bringing in this concept with the
`[07:57]` first two points, combining this third
`[07:59]` point with the first two points, here is
`[08:01]` a prompt that you can run in Claude,
`[08:03]` which will help ensure that you are
`[08:04]` adding a proper evaluation layer where
`[08:06]` it makes sense. I can't stress how
`[08:07]` important this is. The creator of Claude
`[08:09]` code, Boris Cherney, said it best. If
`[08:11]` Claude has a feedback loop, it will two
`[08:13]` to three x quality of the final result.
`[08:15]` So, layer one and layer two are about
`[08:16]` creating specs and evaluating the
`[08:18]` output. The third layer, however, is
`[08:20]` where we build a foundation that can't
`[08:21]` be replicated. But, before we get to
`[08:23]` that, if this is your first video of
`[08:25]` mine, welcome to the channel. If it's
`[08:26]` your second or more, here is our
`[08:28]` anti-slop agreement. The visuals, the
`[08:30]` testing, the hours of research that went
`[08:32]` into this video, this is entirely built
`[08:34]` for humans, not for AI clunkers. So, all
`[08:37]` that I ask is that you subscribe as part
`[08:38]` of this agreement because it helps it
`[08:39]` reach more people so that I can keep
`[08:41]` making videos like this. Also, every
`[08:43]` couple of weeks, I give away a Claude
`[08:44]` Max subscription, so comment below with
`[08:46]` whatever you're building to enter. Layer
`[08:48]` three, the environment. So, layer one
`[08:50]` and layer two need somewhere to live,
`[08:51]` and that's layer three, which is the
`[08:53]` environment that you build in. Think of
`[08:54]` this layer as a workshop. The spec is a
`[08:56]` blueprint pinned to the wall, the
`[08:58]` verifier is the quality check station by
`[09:00]` the door, and then the environment is
`[09:02]` the workshop itself. You need to create
`[09:04]` the proper tooling and the proper system
`[09:06]` so that the whole thing can function at
`[09:07]` a high level. Now, the problem here is
`[09:09]` that most people use the workshop from
`[09:10]` scratch every time they use AI. And no,
`[09:12]` if you have a single chat with your
`[09:14]` entire conversation history, that is not
`[09:16]` what I'm talking about. So, how do you
`[09:17]` create a proper workspace that improves
`[09:20]` over time? First is you need to set up a
`[09:22]` proper Claude MD file. Every time you
`[09:24]` prompt Claude, your Claude.md file gets
`[09:26]` injected automatically. It's essentially
`[09:28]` the first thing that Claude reads to
`[09:30]` help determine how it should operate.
`[09:31]` For example, you can add to your Claude
`[09:33]` MD before building anything multi-step,
`[09:35]` include a verification plan. Now,
`[09:37]` verification is forced into every build,
`[09:39]` not something that you have to remember
`[09:41]` to say. This is just one of the ways
`[09:42]` that you can improve this Claude MD, and
`[09:44]` here's actually mine on the screen, and
`[09:46]` I'm going to call out a couple of
`[09:47]` sections. The first is I outline how
`[09:49]` this repo works. So, think of my repo as
`[09:51]` my workspace. It gives high-level to the
`[09:53]` details around it. I then tell it the
`[09:55]` custom skills and how they're routed,
`[09:57]` how to use them. I then outline the
`[09:59]` architecture of the training data or
`[10:01]` knowledge architecture so that the AI
`[10:03]` knows where to look for certain
`[10:04]` information. And then I have key working
`[10:06]` rules that it should follow no matter
`[10:08]` what. Make this your environment. It's
`[10:10]` your world, and AI is living in it. It
`[10:12]` should not feel like the other way
`[10:13]` around. The second step is you need to
`[10:15]` build your LLM knowledge base. Karpathy
`[10:17]` went viral for this concept on Twitter
`[10:19]` that he calls his LLM knowledge base.
`[10:21]` And this is essentially creating a
`[10:22]` folder system on your machine that
`[10:24]` you're able to ingest your own training
`[10:26]` data in a way that makes it really easy
`[10:28]` for Claude to understand where
`[10:30]` information is. This is so important
`[10:32]` because your data is your moat. And this
`[10:35]` begins the process of building out your
`[10:37]` own intellectual data property. And step
`[10:40]` three is you have to start building out
`[10:42]` your skill set. A general rule of thumb
`[10:43]` that I have is if you plan on doing
`[10:45]` something repeatedly, create a custom
`[10:47]` skill for that. Think of this like a
`[10:49]` handbook to complete a specific task.
`[10:50]` And the more you use these skills, the
`[10:52]` better they'll become. I have a saying
`[10:53]` that I tell my team, the best way to
`[10:55]` find a leak in a hose is to run water
`[10:57]` through it. And it's the same with
`[10:58]` skills. The more you use them, the more
`[11:00]` you'll realize where you need to fix
`[11:01]` them and where they're really good. Keep
`[11:03]` running water through it and your
`[11:05]` system's going to compound over time.
`[11:07]` Step four is create rules for what the
`[11:09]` AI can and can't work on. Depending on
`[11:11]` the cost of getting something wrong, you
`[11:13]` need to establish different AI
`[11:14]` guardrails. So, here's how to think of
`[11:16]` this, right? So, take the Claude.md file
`[11:18]` that I mentioned earlier. You could add
`[11:20]` a line that says, "Don't make up
`[11:21]` information," but that's a guide, not
`[11:23]` necessarily a hard rule. So, at the end
`[11:25]` of the day, AI can still ignore it. So,
`[11:27]` if you have things that are critical not
`[11:29]` to get wrong, then you need to introduce
`[11:31]` rule-based guardrails to ensure that the
`[11:34]` AI can't bypass them. To help you
`[11:36]` visualize this, imagine you have a
`[11:37]` folder called "Important, Don't Edit."
`[11:40]` You could have a rule in Claude MD that
`[11:41]` says, "Don't touch anything in the
`[11:43]` /important, don't edit folder." And that
`[11:45]` might get you 80% of the way there, but
`[11:48]` it's essentially a request, not a rule.
`[11:51]` Claude can still touch those files. So,
`[11:53]` instead, you add a pre-tool use hook
`[11:56]` before Claude uses the write or edit
`[11:58]` tool, and it checks to see the file that
`[12:00]` it's trying to edit. Now, Claude
`[12:02]` literally can't make the edit, and it's
`[12:04]` enforced at the tool level, not the
`[12:06]` prompt level. And as a result of this,
`[12:08]` this is now a concrete rule that the
`[12:10]` agent can't bypass. So, with this in
`[12:12]` mind, bucket things into three groups.
`[12:14]` The first is always do. This is things
`[12:16]` that AI should run on autopilot. The
`[12:18]` second is ask first. So, this is
`[12:20]` anything that you want to double-check.
`[12:22]` And then the third is never do. These
`[12:24]` are lines that can't be crossed that are
`[12:26]` absolutely critical not to get wrong.
`[12:28]` Here's a prompt that brings all of these
`[12:30]` four points that I mentioned to help
`[12:32]` audit your system and create an
`[12:33]` optimized environment for Claude to
`[12:35]` interact with. That's the Karpathy
`[12:36]` method end-to-end, the spec, the
`[12:38]` verifier, and the environment. But
`[12:40]` there's a question that needs to be
`[12:41]` answered. What's the one thing that
`[12:42]` Karpathy thinks we should focus on in
`[12:44]` the age of AI? Here's him getting asked
`[12:46]` this in an interview.
`[12:47]` &gt;&gt; What still remains worth learning deeply
`[12:50]` when intelligence gets cheap as we move
`[12:53]` into the next eight era of AI?
`[12:55]` &gt;&gt; You can outsource your thinking, but you
`[12:57]` can't outsource your understanding. And
`[12:58]` the thing with everything we covered
`[12:59]` here is that the three layers are
`[13:01]` centered around your understanding of
`[13:03]` the bigger picture. You need to
`[13:04]` understand your goals and what's needed
`[13:06]` to direct AI to start working for you.
`[13:08]` Now, if you like this video, you will
`[13:09]` love this one where I do a deep dive
`[13:11]` into four Claude projects that you need
`[13:13]` to build today using these three layers.
`[13:16]` I'll see you over there. Peace.
