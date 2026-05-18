# Karpathy's Obsidian RAG + Claude Code = CHEAT CODE

- **Source:** https://www.youtube.com/watch?v=OSZdFnQmgRw
- **Uploader:** Chase AI
- **Uploaded:** 2026-04-04
- **Duration:** 13:57
- **Method:** YouTube captions (no transcription needed)

## Transcript

Andrei Karpathy just gave us the keys to his personal Obsidian rag system. And I put rag in air quotes because this Obsidian power knowledge base has no vector database, no embeddings, and no complicated retrieval process. Yet, it solves the exact same problem that these more complicated rag structures claim to do. Which is allow our large language model to handle large amounts of documents and answer questions and gather accurate information about them. And the best part about this Obsidian powered system is that it is very lightweight, it's essentially free, and it is the perfect middle ground for a solo operator or a small team. So, today I'm going to show you how Karpathy's Obsidian knowledge system works, how to set it up yourself, and how it differs between traditional rag systems, so you know if this is the right option for you. So, the process by which we are going to create this Obsidian powered knowledge system was laid out yesterday in a pretty comprehensive Twitter post by Andrei Karpathy. Now, the big takeaway from this post is that we are able to create large language model knowledge bases that essentially act in the same way as something like light rag or rag anything or any other graph rag system with Obsidian. And we're able to do so in a rather simple manner by just having a clever structure to our file system and how we actually ingest data. And the end result is that I am able to ingest a pretty significant amount of data and documents into my Obsidian vault and use Claude code to ask questions about it, to figure out connections between different things. AAA, the exact same thing you would do with a traditional rag system, but with none of the overhead and a way simpler setup. And as Andrei lays out, the setup looks something like this. First, we have data ingestion. We are bringing in articles, we're bringing in papers, we're bringing in repos from the internet or from wherever, and we're bringing it into a raw directory inside of our Obsidian vault. This is essentially the staging area before it gets turned into a wiki. We as the human being in this interaction are able to see all of this happening via Obsidian. Obsidian for all intents and purposes is our front end. Here is where I can see where all the documents are laid out. Here's where I can read all of the wikis. So it isn't sort of abstracted away in a black box like it isn't a rag system. It's kind of hard even in a graph rag setup like like rag to actually go inside of here and really see everything. I mean I can but as cool as this looks this isn't, you know, very efficient. And from there you just do a Q&amp;A via something like Claude code. And like Andre laid out here, he expected that he would have to reach out for something like rag but a large language model has been pretty good about auto maintaining index files and brief summary of all the documents it reads. And this is something we are going to be able to do too with a pretty simple Claude.md file which I will be giving you. And you will be able to find that Claude.md as well as a written guide that comes with a bunch of prompts inside of my free Chase AI community. There will be a link to that in the description of this video. And speaking of Chase AI, and you knew this was coming, quick plug for my Claude code masterclass. Just released this a couple weeks ago and it is the number one place to go from zero to AI dev especially if you do not come from a technical background. You can find a link to this in the pinned comment. So make sure to check this out if you're serious about learning this tool. Now before we jump into the specifics of how to set up this Obsidian system for yourself, let's go over the actual file structure because this is important to understand how data is coming into our vault and then getting turned into wikis. So the Obsidian vault is where everything lives. As you'll see if you've never used it before, when you download Obsidian you are going to designate a specific folder as the vault. In my case it is quite literally called the vault. That's where everything in Obsidian lives. As a subfolder of the vault we are going to have the raw folder. The raw folder is where all of our research gets dumped, anything we want to manually include in these wikis gets put. This is essentially the staging folder. So, this is where all the raw data is going to be held. This can be markdown files, this can be PDFs, and I'm going to show you how to use the Obsidian Clipper to essentially turn any webpage into a markdown file like it's sent to the raw folder automatically. We will have another sub-folder that is the wiki folder. So, what the large language model is going to do, what Claude Code will do for us, is on demand or you could have it even be a skill or have it be automated, is we are going to point it at the raw folder and say, "Hey, I want you to create a wiki about whatever subject you've been gathering information about." From there, it will then create a wiki about that. So, you can see we have three different wikis here, one for AI agents, one for RAG systems, and one for content creation. Now, in in between the wiki folder and these sub-wiki folders is the master index markdown. This is essentially just a list of all of the different wikis that have been created. Because the idea is when you, this is you, when you talk to Claude Code, all right, that's Claude Code over there, and say, "Hey, I want to learn more about AI agents. Can you ask I you know, I want to ask questions about my wiki." Well, what is it going to do? Well, it's going to go to the vault because you're probably already in there. It's then going to go to the wiki folder. It's going to go to the master index folder and say, "Hey, what wikis have we created?" Oh, he wants to know about RAG systems. Okay, it goes down to RAG, and the wiki folders themselves have index files which break down all the additional content. So, what Obsidian gives us and what this file structure gives us is a very clear path to find information even if we have a ton of it floating around. And this helps Claude Code because it's not going to have a ton of issues finding the data. We're not going to run a million tool calls to see what's in our file structure, but it also helps you because it's very clear where to go. For example, over here on the left is my Obsidian folder. I'm in the Obsidian UI and we'll go through the download here in a second. But if I want to see a wiki, what do I do? I just go to wiki. I have a master index which lays down everything in there. Right now, it's just three things, but if there were 3,000, it still wouldn't be too difficult. And then from there, you know, I can click on it. It takes me to the index of that specific wiki and then I can look at different stuff inside of I can look at different stuff inside of there. there. It's that simple and it's that simple for AI 2, which is why we're able to use essentially just a markdown file structure to somewhat mimic a rag system. So while that theory is cool, now let's go into how to actually set this up for yourself. First and foremost, you're going to need to download Obsidian. You're just going to head to obsidian.md, hit download now, go through the wizard. It's completely free and you're going to designate some folder as the vault. Just create one, call it the vault. Makes it easy for me and I'll probably work for you. After we create the vault, we now need to set up this file structure inside of it. The easiest way to do that is with Claude Code. Simply open up Claude Code in the vault, so that's the directory I'm in and you're going to give it a prompt telling it to create this file structure. Now luckily for you, I already created the prompt, so you can just copy this thing and paste it into Claude Code. Now if you're like me and you've already been using Obsidian for a bit, you probably have a bunch of folders already in there. So maybe you don't want to call it raw, maybe you want to call it something else. The whole point of it is you just need to designate some folder is, like I said, sort of the holding area or the staging area for where all this information's going to get dumped until it gets turned into a wiki. So adjust as needed. Now the next thing we want to do is create a Claude.md file. Personal assistant type projects, things like this that are very markdown heavy, Claude.md's are perfect for. And this Claude.md file is breaking down the knowledge base rules as well as how to essentially traverse it. So again, that we aren't wasting tokens when we ask questions. Again, I have this entire Claude.md template prompt you can use. This Claude.md file is also telling Claude how to structure these markdown files, so it's very easy to traverse files with this wikilinks format. Now let's talk about how we can bring things into this raw folder, how we can get data into our system in the first place. Well, super easy way to do this is with the Obsidian web clipper. So I will put a link to this in the school, or you can go to school, or you can go to obsidian.md/clipper. obsidian.md/clipper. And this is just a Chrome extension, which makes it super easy to turn a web which makes it super easy to turn a web page page into data, into a markdown file. Now the one issue with this web clipper is it's going to struggle with images. It's just not even going to bring them in, it'll have them as a link. But I want to be able to see the images from these documents I ingest inside of Obsidian. So what do we do? Well, we are going to use an Obsidian community skill or Obsidian community plugin to help with this. So one of the cool things about Obsidian is the community plugins, there's thousands of them. So if you're inside of Obsidian, I'm inside the desktop app right now. If I come down here and I hit this little gear, I'm going to go to community plugins. I'm going to go to browse, and then you're going to search for local images plus. You're going to download it, install it, and turn it on. Make sure it's enabled. You can confirm it's enabled by heading to your community plugins tab and seeing this little tab turned on. Now, if we use the Obsidian web clipper, and I can see that over here as an extension, you can see what happens. It immediately pulls everything, and if I hit add to Obsidian, I can see this entire article including the images. Now there is one thing we need to set up inside of the web clipper, and that's making sure it actually pulls it into the raw folder automatically. I don't want to have to manually do that. You're just going to head to the options on your web clipper. I just right clicked it, and then over here on the left, where it says default, I created my own new template, but you can stick on the default if you want. Where it says location and note location right here, you're want to you go want to change that from want to you go want to change that from clippings clippings to raw. And that will make sure when you use the web clipper, it automatically goes into the raw folder. So now, with the Obsidian web clipper extension and the images community plugin, we can now turn any web page on the internet into a markdown file that will be used for our wiki. But that is just one data funnel, and that's a manual one. We can have Claude Code do a bunch of heavy lifting, too. So let's say I was trying to create a wiki about Claude Code skills. So I told Claude Code, let's create a wiki about Claude Code skills. I already included some info in the raw folder, what we pulled in via the web clipper. Go conduct your own research and bring in the relevant raw MD files to generate that wiki. So what is it going to do? It's going to go on the internet, use its standard web search, and it's going to create its own wiki about Claude Code to create its own wiki about Claude Code skills. skills. So what you see is that this raw folder, this whole raw pipeline, that's more for you. That's for when you manually want to put in some information. Now, you can have Claude Code do that as well, but Claude Code is also smart enough to essentially take the research, figure out what's relevant itself, and just create the wiki directly. This raw folder is really for you, the human being, to have some level of organization. And here's what Claude Code came back with. So it created the Claude Code skills wiki. We see here in the master index that it's referenced here. If I click on it, this then brings us to the index of Claude Code skills, and right now it has four articles. So here's the skills overview article. You can see it links to websites, and it also links to different articles within our Obsidian vault. So if I click on skill ecosystem, here's more stuff. If I click on top skills, right so on and so forth. There's a very clear pathway from one article to another and how these things relate. Which means when you ask Cloud Code questions about these articles and these subjects, it's easy and cheap for it to answer questions about them. Which then brings us to the obvious question, do we need rag at all? You know, we look at something like this light rag setup, you watch my last few videos with light rag and rag anything, and seeing how simple the setup with the Obsidian, you're probably like, well, why would I ever even bother with these more complicated setups at all? And the truth is, if you're a solo dev, a solo operator, or a small team that isn't dealing with thousands of documents, the answer probably is Obsidian makes more sense for you. It's lightweight and you really don't need rag. These large language models, these harnesses like Cloud Code, are good enough for your use case. And we can sit here and get in the weeds about the differences between the Obsidian rag and true rag, but the truth is the big thing is scale, right? Are we trying to scale to millions of documents or are we not? Because at a certain scale, it's going to be cheaper and faster to use a proper rag system, no matter how good Cloud Code is at navigating this MD file document network you've created. But this isn't a question you necessarily need to have the exact answer to right away. Why wouldn't you just start with something like Obsidian? And if it's clear your scale goes well beyond the bounds of what this thing can handle, then just move into rag. I think people get really caught up in like answering this question when it's like, just try it out. Just experiment. It's not costing you anything to use some sort of rag system, rag system like some sort of rag system, rag system like Obsidian. Obsidian. And if it doesn't work, it doesn't work. Fine, then go to use light rag instead. People want to sit here, as they inevitably will in the comments, and like argue this back and forth. Just try it. I think the answer will be pretty clear to a certain point when you need to move to a true rag system. But the nice thing with this is is again, most people don't need a real rag system. They just don't. Right? Even if they're in a small business team situation. So, having a proper, you know, orchestrated system like the Obsidian knowledge base, I think is a huge boon to the majority of people. So, I hope this breakdown was useful to you. Definitely check out Andre's post about this. He goes into a fair amount of detail. Make sure to check out the free Chase AI School. There's a link to that in the description that has all the prompts and a written breakdown of how to actually do this if you got confused at any part. And as always, take a look at Chase AI Plus if you want to get your hands on that masterclass. Besides that, let me know what you thought, and I'll see you around.

## Timestamped

`[00:02]` Andrei Karpathy just gave us the keys to
`[00:02]` his personal Obsidian rag system.
`[00:05]` And I put rag in air quotes because this
`[00:08]` Obsidian power knowledge base has no
`[00:10]` vector database, no embeddings, and no
`[00:12]` complicated retrieval process. Yet, it
`[00:15]` solves the exact same problem that these
`[00:18]` more complicated rag structures claim to
`[00:20]` do. Which is allow our large language
`[00:23]` model to handle large amounts of
`[00:25]` documents and answer questions and
`[00:27]` gather accurate information about them.
`[00:30]` And the best part about this Obsidian
`[00:32]` powered system is that it is very
`[00:33]` lightweight, it's essentially free, and
`[00:36]` it is the perfect middle ground for a
`[00:38]` solo operator or a small team. So, today
`[00:41]` I'm going to show you how Karpathy's
`[00:43]` Obsidian knowledge system works, how to
`[00:45]` set it up yourself, and how it differs
`[00:47]` between traditional rag systems, so you
`[00:50]` know if this is the right option for
`[00:51]` you. So, the process by which we are
`[00:53]` going to create this Obsidian powered
`[00:55]` knowledge system was laid out yesterday
`[00:58]` in a pretty comprehensive Twitter post
`[01:00]` by Andrei Karpathy. Now, the big
`[01:02]` takeaway from this post is that we are
`[01:04]` able to create large language model
`[01:06]` knowledge bases that essentially act in
`[01:09]` the same way as something like light rag
`[01:11]` or rag anything or any other graph rag
`[01:14]` system with
`[01:16]` Obsidian. And we're able to do so in a
`[01:18]` rather simple manner by just having a
`[01:20]` clever structure to our file system and
`[01:23]` how we actually ingest data. And the end
`[01:26]` result is that I am able to ingest a
`[01:28]` pretty significant amount of data and
`[01:31]` documents into my Obsidian vault and use
`[01:34]` Claude code to ask questions about it,
`[01:36]` to figure out connections between
`[01:37]` different things. AAA, the exact same
`[01:40]` thing you would do with a traditional
`[01:42]` rag system, but with none of the
`[01:44]` overhead and a way simpler setup. And as
`[01:46]` Andrei lays out, the setup looks
`[01:48]` something like this. First, we have data
`[01:50]` ingestion. We are bringing in articles,
`[01:52]` we're bringing in papers, we're bringing
`[01:54]` in repos from the internet or from
`[01:56]` wherever, and we're bringing it into a
`[01:58]` raw directory inside of our Obsidian
`[02:01]` vault. This is essentially the staging
`[02:03]` area before it gets turned into a wiki.
`[02:05]` We as the human being in this
`[02:06]` interaction are able to see all of this
`[02:08]` happening via Obsidian. Obsidian for all
`[02:11]` intents and purposes is our front end.
`[02:13]` Here is where I can see where all the
`[02:14]` documents are laid out. Here's where I
`[02:16]` can read all of the wikis. So it isn't
`[02:18]` sort of abstracted away in a black box
`[02:20]` like it isn't a rag system. It's kind of
`[02:22]` hard even in a graph rag setup like like
`[02:25]` rag to actually go inside of here and
`[02:27]` really see everything. I mean I can but
`[02:30]` as cool as this looks this isn't, you
`[02:32]` know, very efficient. And from there you
`[02:34]` just do a Q&amp;A via something like Claude
`[02:36]` code. And like Andre laid out here, he
`[02:39]` expected that he would have to reach out
`[02:40]` for something like rag but a large
`[02:42]` language model has been pretty good
`[02:43]` about auto maintaining index files and
`[02:45]` brief summary of all the documents it
`[02:46]` reads. And this is something we are
`[02:48]` going to be able to do too with a pretty
`[02:50]` simple Claude.md file which I will be
`[02:52]` giving you. And you will be able to find
`[02:54]` that Claude.md as well as a written
`[02:55]` guide that comes with a bunch of prompts
`[02:57]` inside of my free Chase AI community.
`[03:00]` There will be a link to that in the
`[03:01]` description of this video. And speaking
`[03:03]` of Chase AI, and you knew this was
`[03:05]` coming, quick plug for my Claude code
`[03:07]` masterclass. Just released this a couple
`[03:09]` weeks ago and it is the number one place
`[03:10]` to go from zero to AI dev especially if
`[03:12]` you do not come from a technical
`[03:14]` background. You can find a link to this
`[03:16]` in the pinned comment. So make sure to
`[03:18]` check this out if you're serious about
`[03:21]` learning this tool. Now before we jump
`[03:23]` into the specifics of how to set up this
`[03:25]` Obsidian system for yourself, let's go
`[03:28]` over the actual file structure because
`[03:30]` this is important to understand how data
`[03:32]` is coming into our vault and then
`[03:35]` getting turned into wikis. So the
`[03:36]` Obsidian vault is where everything
`[03:38]` lives. As you'll see if you've never
`[03:40]` used it before, when you download
`[03:41]` Obsidian you are going to designate a
`[03:43]` specific folder as the vault. In my case
`[03:46]` it is quite literally called the vault.
`[03:48]` That's where everything in Obsidian
`[03:49]` lives. As a subfolder of the vault we
`[03:52]` are going to have the raw folder. The
`[03:54]` raw folder is where all of our research
`[03:57]` gets dumped, anything we want to
`[03:59]` manually include in these wikis gets
`[04:00]` put. This is essentially the staging
`[04:02]` folder. So, this is where all the raw
`[04:04]` data is going to be held. This can be
`[04:05]` markdown files, this can be PDFs, and
`[04:07]` I'm going to show you how to use the
`[04:09]` Obsidian Clipper to essentially turn any
`[04:11]` webpage into a markdown file like it's
`[04:14]` sent to the raw folder automatically. We
`[04:16]` will have another sub-folder that is the
`[04:18]` wiki folder. So, what the large language
`[04:20]` model is going to do, what Claude Code
`[04:22]` will do for us, is on demand or you
`[04:24]` could have it even be a skill or have it
`[04:26]` be automated, is we are going to point
`[04:28]` it at the raw folder and say, "Hey, I
`[04:30]` want you to create a wiki about whatever
`[04:32]` subject you've been gathering
`[04:33]` information about." From there, it will
`[04:36]` then create a wiki about that. So, you
`[04:38]` can see we have three different wikis
`[04:40]` here, one for AI agents, one for RAG
`[04:42]` systems, and one for content creation.
`[04:45]` Now, in in between the wiki folder and
`[04:48]` these sub-wiki folders is the master
`[04:51]` index markdown. This is essentially just
`[04:54]` a list of all of the different wikis
`[04:56]` that have been created. Because the idea
`[04:58]` is when you, this is you,
`[05:02]` when you talk to Claude Code, all right,
`[05:04]` that's Claude Code over there,
`[05:05]` and say, "Hey, I want to learn more
`[05:07]` about AI agents. Can you ask I you know,
`[05:10]` I want to ask questions about my wiki."
`[05:12]` Well, what is it going to do? Well, it's
`[05:13]` going to go to the vault because you're
`[05:15]` probably already in there. It's then
`[05:17]` going to go to the wiki folder. It's
`[05:18]` going to go to the master index folder
`[05:21]` and say, "Hey, what wikis have we
`[05:23]` created?" Oh, he wants to know about
`[05:25]` RAG systems. Okay, it goes down to RAG,
`[05:28]` and the wiki folders themselves have
`[05:30]` index files which break down all the
`[05:32]` additional content. So, what Obsidian
`[05:34]` gives us and what this file structure
`[05:36]` gives us is a very clear path to find
`[05:38]` information even if we have a ton of it
`[05:40]` floating around. And this helps Claude
`[05:42]` Code because it's not going to have a
`[05:44]` ton of issues finding the data. We're
`[05:46]` not going to run a million tool calls to
`[05:48]` see what's in our file structure, but it
`[05:50]` also helps you because it's very clear
`[05:51]` where to go. For example, over here on
`[05:54]` the left is my Obsidian folder. I'm in
`[05:56]` the Obsidian UI and we'll go through the
`[05:58]` download here in a second. But if I want
`[05:59]` to see a wiki, what do I do? I just go
`[06:01]` to wiki.
`[06:03]` I have a master index which lays down
`[06:05]` everything in there. Right now, it's
`[06:06]` just three things, but if there were
`[06:07]` 3,000, it still wouldn't be too
`[06:09]` difficult. And then from there, you
`[06:11]` know, I can click on it. It takes me to
`[06:14]` the index of that specific wiki and then
`[06:16]` I can look at different stuff inside of
`[06:17]` I can look at different stuff inside of there.
`[06:18]` there.
`[06:18]` It's that simple and it's that simple
`[06:20]` for AI 2, which is why we're able to use
`[06:22]` essentially just a markdown file
`[06:23]` structure to somewhat mimic a rag
`[06:26]` system. So while that theory is cool,
`[06:28]` now let's go into how to actually set
`[06:30]` this up for yourself. First and
`[06:31]` foremost, you're going to need to
`[06:32]` download Obsidian. You're just going to
`[06:34]` head to obsidian.md,
`[06:36]` hit download now, go through the wizard.
`[06:38]` It's completely free and you're going to
`[06:40]` designate some folder as the vault. Just
`[06:43]` create one, call it the vault. Makes it
`[06:45]` easy for me and I'll probably work for
`[06:47]` you. After we create the vault, we now
`[06:49]` need to set up this file structure
`[06:51]` inside of it. The easiest way to do that
`[06:53]` is with Claude Code. Simply open up
`[06:55]` Claude Code in the vault, so that's the
`[06:58]` directory I'm in and you're going to
`[06:59]` give it a prompt telling it to create
`[07:02]` this file structure. Now luckily for
`[07:03]` you, I already created the prompt, so
`[07:05]` you can just copy this thing and paste
`[07:07]` it into Claude Code. Now if you're like
`[07:08]` me and you've already been using
`[07:10]` Obsidian for a bit,
`[07:11]` you probably have a bunch of folders
`[07:13]` already in there. So maybe you don't
`[07:15]` want to call it raw, maybe you want to
`[07:17]` call it something else. The whole point
`[07:19]` of it is you just need to designate some
`[07:20]` folder is, like I said, sort of the
`[07:22]` holding area or the staging area for
`[07:24]` where all this information's going to
`[07:25]` get dumped until it gets turned into a
`[07:27]` wiki. So adjust as needed. Now the next
`[07:28]` thing we want to do is create a
`[07:29]` Claude.md file. Personal assistant type
`[07:32]` projects, things like this that are very
`[07:33]` markdown heavy, Claude.md's are perfect
`[07:36]` for. And this Claude.md file is breaking
`[07:39]` down the knowledge base rules as well as
`[07:41]` how to essentially traverse it. So
`[07:43]` again, that we aren't wasting tokens
`[07:44]` when we ask questions. Again, I have
`[07:47]` this entire Claude.md template prompt
`[07:50]` you can use. This Claude.md file is also
`[07:52]` telling Claude how to structure these
`[07:54]` markdown files, so it's very easy to
`[07:56]` traverse files with this wikilinks
`[07:59]` format. Now let's talk about how we can
`[08:01]` bring things into this raw folder, how
`[08:03]` we can get data into our system in the
`[08:05]` first place. Well, super easy way to do
`[08:07]` this is with the Obsidian web clipper.
`[08:10]` So I will put a link to this in the
`[08:12]` school, or you can go to
`[08:13]` school, or you can go to obsidian.md/clipper.
`[08:16]` obsidian.md/clipper.
`[08:16]` And this is just a Chrome extension,
`[08:18]` which makes it super easy to turn a web
`[08:20]` which makes it super easy to turn a web page
`[08:21]` page
`[08:21]` into data, into a markdown file. Now the
`[08:23]` one issue with this web clipper is it's
`[08:25]` going to struggle with images. It's just
`[08:26]` not even going to bring them in, it'll
`[08:27]` have them as a link. But I want to be
`[08:29]` able to see the images from these
`[08:30]` documents I ingest inside of Obsidian.
`[08:33]` So what do we do? Well, we are going to
`[08:35]` use an Obsidian community skill or
`[08:37]` Obsidian community plugin to help with
`[08:38]` this. So one of the cool things about
`[08:40]` Obsidian is the community plugins,
`[08:42]` there's thousands of them. So if you're
`[08:44]` inside of Obsidian, I'm inside the
`[08:46]` desktop app right now. If I come down
`[08:48]` here and I hit this little gear,
`[08:50]` I'm going to go to community plugins.
`[08:52]` I'm going to go to browse, and then
`[08:54]` you're going to search for local images
`[08:56]` plus. You're going to download it,
`[08:58]` install it, and turn it on. Make sure
`[09:00]` it's enabled. You can confirm it's
`[09:02]` enabled by heading to your community
`[09:04]` plugins tab and seeing this little
`[09:06]` tab turned on. Now, if we use the
`[09:09]` Obsidian web clipper, and I can see that
`[09:11]` over here as an extension,
`[09:13]` you can see what happens. It immediately
`[09:15]` pulls everything, and if I hit add to
`[09:18]` Obsidian, I can see this entire article
`[09:20]` including the images. Now there is one
`[09:22]` thing we need to set up inside of the
`[09:24]` web clipper, and that's making sure it
`[09:25]` actually pulls it into the raw folder
`[09:28]` automatically. I don't want to have to
`[09:29]` manually do that. You're just going to
`[09:31]` head to the options on your web clipper.
`[09:34]` I just right clicked it, and then over
`[09:35]` here on the left, where it says default,
`[09:38]` I created my own new template, but you
`[09:39]` can stick on the default if you want.
`[09:42]` Where it says location
`[09:46]` and note location right here, you're
`[09:48]` want to you go want to change that from
`[09:49]` want to you go want to change that from clippings
`[09:51]` clippings
`[09:51]` to raw. And that will make sure when you
`[09:53]` use the web clipper, it automatically
`[09:55]` goes into the raw folder. So now, with
`[09:57]` the Obsidian web clipper extension and
`[09:59]` the images community plugin, we can now
`[10:01]` turn any web page on the internet into a
`[10:05]` markdown file that will be used for our
`[10:07]` wiki. But that is just one data funnel,
`[10:09]` and that's a manual one. We can have
`[10:11]` Claude Code do a bunch of heavy lifting,
`[10:13]` too. So let's say I was trying to create
`[10:15]` a wiki about Claude Code skills. So I
`[10:17]` told Claude Code, let's create a wiki
`[10:19]` about Claude Code skills. I already
`[10:21]` included some info in the raw folder,
`[10:22]` what we pulled in via the web clipper.
`[10:25]` Go conduct your own research and bring
`[10:26]` in the relevant raw MD files to generate
`[10:28]` that wiki. So what is it going to do?
`[10:30]` It's going to go on the internet, use
`[10:31]` its standard web search, and it's going
`[10:33]` to create its own wiki about Claude Code
`[10:36]` to create its own wiki about Claude Code skills.
`[10:37]` skills.
`[10:37]` So what you see is that this raw folder,
`[10:40]` this whole raw pipeline, that's more for
`[10:41]` you. That's for when you manually want
`[10:43]` to put in some information. Now, you can
`[10:44]` have Claude Code do that as well, but
`[10:46]` Claude Code is also smart enough to
`[10:48]` essentially take the research, figure
`[10:51]` out what's relevant itself, and just
`[10:52]` create the wiki directly. This raw
`[10:54]` folder is really for you, the human
`[10:55]` being, to have some level of
`[10:56]` organization. And here's what Claude
`[10:58]` Code came back with. So it created the
`[11:01]` Claude Code skills wiki. We see here in
`[11:03]` the master index that it's referenced
`[11:05]` here. If I click on it,
`[11:07]` this then brings us to the index of
`[11:09]` Claude Code skills, and right now it has
`[11:11]` four articles. So here's the skills
`[11:13]` overview article. You can see it links
`[11:16]` to websites, and it also links to
`[11:18]` different articles within our Obsidian
`[11:20]` vault. So if I click on skill ecosystem,
`[11:23]` here's more stuff. If I click on top
`[11:25]` skills, right so on and so forth.
`[11:27]` There's a very clear pathway from one
`[11:29]` article to another and how these things
`[11:31]` relate. Which means when you ask Cloud
`[11:32]` Code questions about these articles and
`[11:34]` these subjects, it's easy and cheap for
`[11:38]` it to answer questions about them. Which
`[11:39]` then brings us to the obvious question,
`[11:41]` do we need rag at all? You know, we look
`[11:43]` at something like this light rag setup,
`[11:45]` you watch my last few videos with light
`[11:47]` rag and rag anything, and seeing how
`[11:49]` simple the setup with the Obsidian,
`[11:51]` you're probably like, well, why would I
`[11:52]` ever even bother with these more
`[11:54]` complicated setups at all? And the truth
`[11:56]` is, if you're a solo dev, a solo
`[11:59]` operator, or a small team that isn't
`[12:01]` dealing with thousands of documents, the
`[12:04]` answer probably is Obsidian makes more
`[12:07]` sense for you. It's lightweight and you
`[12:09]` really don't need rag. These large
`[12:11]` language models, these harnesses like
`[12:13]` Cloud Code, are good enough
`[12:15]` for your use case. And we can sit here
`[12:17]` and get in the weeds about the
`[12:18]` differences between the Obsidian rag and
`[12:20]` true rag, but the truth is the big thing
`[12:23]` is scale, right? Are we trying to scale
`[12:25]` to millions of documents or are we not?
`[12:27]` Because at a certain scale, it's going
`[12:29]` to be cheaper and faster to use a proper
`[12:32]` rag system,
`[12:33]` no matter how good Cloud Code is at
`[12:35]` navigating this MD file document network
`[12:39]` you've created. But this isn't a
`[12:40]` question you necessarily need to have
`[12:42]` the exact answer to right away. Why
`[12:44]` wouldn't you just start with something
`[12:46]` like Obsidian? And if it's clear your
`[12:48]` scale goes well beyond the bounds of
`[12:50]` what this thing can handle, then just
`[12:52]` move into rag.
`[12:53]` I think people get really caught up in
`[12:54]` like answering this question when it's
`[12:56]` like, just try it out. Just experiment.
`[12:58]` It's not costing you anything to use
`[13:00]` some sort of rag system, rag system like
`[13:02]` some sort of rag system, rag system like Obsidian.
`[13:03]` Obsidian.
`[13:03]` And if it doesn't work, it doesn't work.
`[13:04]` Fine, then go to use light rag instead.
`[13:06]` People want to sit here, as they
`[13:07]` inevitably will in the comments, and
`[13:09]` like argue this back and forth. Just try
`[13:11]` it. I think the answer will be pretty
`[13:12]` clear to a certain point when you need
`[13:14]` to move to a true rag system. But the
`[13:16]` nice thing with this is
`[13:18]` is again,
`[13:19]` most people don't need a real rag
`[13:20]` system. They just don't. Right? Even if
`[13:22]` they're in a small business team
`[13:24]` situation. So, having a proper, you
`[13:27]` know, orchestrated system like the
`[13:28]` Obsidian knowledge base, I think is a
`[13:30]` huge boon to the majority of people. So,
`[13:33]` I hope this breakdown was useful to you.
`[13:34]` Definitely check out Andre's post about
`[13:37]` this. He goes into a fair amount of
`[13:38]` detail. Make sure to check out the free
`[13:40]` Chase AI School. There's a link to that
`[13:42]` in the description that has all the
`[13:43]` prompts and a written breakdown of how
`[13:46]` to actually do this if you got confused
`[13:47]` at any part. And as always, take a look
`[13:50]` at Chase AI Plus if you want to get your
`[13:51]` hands on that masterclass. Besides that,
`[13:54]` let me know what you thought, and I'll
`[13:56]` see you around.
