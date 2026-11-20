# Your AI is LYING to you. Build an LLM Council Instead 🏛️ 🧠

- **Source:** https://www.youtube.com/watch?v=92rma4chrIE
- **Uploader:** Jason Cooperson
- **Uploaded:** 2026-06-02
- **Duration:** 17:11
- **Method:** YouTube captions (no transcription needed)

## Transcript

In this video, I'm going to show you exactly how to set up an LLM council so that you can get better answers from your AI when you're asking it very important questions. This has to do with like strategic questions about your business or your personal life that require a very thorough amount of reasoning, right? Um and so our goal here is to set up this LLM council so that we can get an unbiased and thorough answer from our LLM rather than just having it give us an answer straightaway without it consulting, you know, any other advisers or anything. And so for example, if you're if you're trying to ask a question like, you know, should I pivot my business to scale low ticket or high ticket, you know, that's like a very high-level important uh strategic question. And sometimes you want to consult AI on it, right? And so I'm going to show you how to get an unbiased answer because the problem is that recently Stanford did a study where they basically concluded that AI is more likely to agree with you even when you have like a stupid idea, right? It's 49% more likely to just agree with whatever you're saying. So for example, if I ask it this question of like should I pivot my business to scale low ticket, well, it already knows a little bit about me. It already knows that I'm, you know, have preferences in a certain direction. And so it's basically just going to agree with me, right? It's It's just going to say, "Hey, you should just keep doing your thing. Like keep doing your low ticket thing, right?" That's the problem that we're trying to solve, okay? How do we solve this problem? We basically are using a concept called stochastic consensus. A stochastic consensus is a process where we have a bunch of individuals basically argue and debate against each other to give you a final consensus, right? Multiple AI agents are spawned in with different configurations. And they're each independent and they're going to each do their independent perspective on it and then argue against each other, debate each other to finally give you an an answer. And this consistently outperforms when you just ask it the question straight up, right? So, that's exactly what we're going to be setting up today so that you can ask your AI questions like, you know, should I pivot my business this direction or should I text her back or like should I do this or whatever, right? And so, let's get straight into it, okay? let's get straight into it, okay? So, So, um basically, it here's how it's going to work, okay? These are the different agents that we're spawning in. The first is a contrarian, the second is a first principles agent, the third is an expansionist, we have an outsider, we have an executor, and then we have a final chairman who makes the final call, okay? Each of these agents have their own separate prompts and kind of their own perspective and biases to kind of evaluate all angles of the question, all evaluate all angles of the question, all right? right? So, I'm going to give you everything that you need for free, okay? For free. I'm going to give you all the files I wrote I already wrote all the code. I already uh delved into the the GitHub repo by Karpathy. This was actually created by Andrej Karpathy who is like AI goat. Uh he was a founder and OpenAI. He works at Anthropic now and he was the one who created this LLM council in the first place. All right? So, this is basically what that is based off of is his GitHub repo. So, the first thing to do is going to be to go down below this video and download the skill files, okay? So, if you go down below this video, whether it's on YouTube or if you're watching it in Notion, there should be a Google Drive folder just like this, okay? So, click on this Google Drive folder. It's going to bring you here. Or for you, it might look like this, okay? So, what you're going to do is just click download all. And then just give it a second, that's going to download. Okay, it just zipped up the file and then we can download so we can save and then we can click here to open it up in our downloads folder. We can see it's right here. We can double click this and it's going to extract the file and here we have all the skill files ready to go. And inside we have this folder. It's called LLM Council and inside of that we have all the scripts and we have the actual code, the skill MD file that I created for you guys. Okay. [snorts] So, we want to take this folder and we want to basically move it to the right place. Okay, so I'm going to open up a new finder window. So, we have one over here and one over here. Okay? And the next thing you need to do is open up your Claude desktop app or whatever LLM you're using. If you're using ChatGPT or Codex, that's fine. We're just going to go into Claude, okay? And we are going to go into a new chat. Let's actually go into code, okay? We got to use Claude code for this, otherwise it's not going to work. And what I want you to do is say something like this. Hey, can you give me the file path to where our global skills are installed? Just give me the file path uh so I can navigate there. Okay? So, we're going to say something like that. Shouldn't take long. Okay, boom. It just gave us the file path. So, it's right here. We're going to copy this file path right here. It's users, your name, .claud skills. We're going to copy that. We're going to go back to finder. And the one that you just downloaded is over here. We're going to open up this new window and we're going to do command shift G. Command shift G and we're going to paste that in. And we hit enter. Boom. Okay, so now this is going to be where our skill files live, okay? For you it's probably empty. And for me, I already have this downloaded, so obviously it's already right here. I'm just going to delete that, okay? What you want to do is just drag this file that you just downloaded from me, just drag it over here. Boom. There it is. Okay? So, now we can X out this file and then let's just quit Claude and then we'll reopen the app. we'll reopen the app. Claude. We reopen the app. Boom. And now if we do {slash} LLM Council, we can see we do have the skill available to us now. It's as simple as that. Okay? Now, here's how the skill works by default. Okay, so if I ask it a question like LLM Council, you know, should I um focus on scaling the low ticket or should I pivot to high ticket? Uh my goal is to make, you know, uh $50,000 a month as fast as possible. Uh which route should I go? The school is already at $8,000 MRR and the high ticket I'm doing AI agency services. I want to know which one that I should focus or scale more uh so that I can hit 50k a month as fast as possible. So, we can ask it a question like that and by default, it's it's going to run the skill, right? You'll see it run. We'll go back to that. But by default, it's going to run all these sub agents like this all on Opus 4.8. Okay? Opus 4.8 is the model that we're running on Claude. And it's going to run this using a Claude Council. So, it's going to spawn five agents. And as you can see to spawn five agents. And as you can see here, here, uh it'll do that in a second, but all of these agents are going to run on the Claude Opus 4.8 model, which is pretty good, right? We can see Okay, boom. It's spawning in all the agents. We have the pragmatist, we have the red teamer. We have one more here. Let's see what this one is. But you you click into the each of these and we can see each of them is with their own prompt, right? Their own prompt and this is exactly how we do that um stochastic debate, right? We're having each of them spawn in and basically argue against each other. We see we have uh 1 2 3 4. It's spawning in all the sub agents, right? One of them already finished. Okay? So, that's by default. And you don't need to plug in any other things. Like by default, it's just going to work. They're all going to run on a Claude model. However, the original design of this was meant to run on different models so that we could avoid the vulnerabilities of running just one model, right? Because Claude usually responds in a certain way, ChatGPT usually responds in a certain way, Gemini also usually responds in a certain way. Gemini might be better at some things, Claude might be better at some things. And so, if you click down below, uh you can view the original repo. Okay, this is the link to the original repo built by Karpathy himself. And the original design was built for different models so that we could spawn out these different agents with different models. So, if you want to run the advanced version that's going to give you the best, highest quality, like ultimate answer, where all the different models debate each other, I'm going to show you how to do that right now. All right, so the first thing to do is create a project. So, I'm going to go into this projects folder that I have on my computer. It doesn't matter. You can just go documents or honestly wherever you want to store this, okay? It do- it doesn't matter. You can even put it on your desktop. But just go somewhere and we're going to create a new folder. We're going to call this LLM We're going to call this LLM Council Council uh folder. Call it that. And then, we're just going to click inside of this just going to click inside of this folder. folder. And actually, we don't need to do that. We can do start a new session. And we're going to go here and click open folder. And then, we're going to go to projects and we're going to click that LLM Council folder. Okay? We're going to click open. And then, you're going to want to say something like this. Create a .env file in this folder uh for the LLM Council skill so that I can put my OpenRouter API key into the .env my OpenRouter API key into the .env file. file. Okay? So, we're just going to say something like that. It's going to create the .env file for us, okay? And what we're going to do next is go to a site called next is go to a site called openrouter.ai. openrouter.ai. Openrouter.ai basically allows you to run multiple LLMs on all these different models. So, if we click explore models here, we basically have access to all of these different models. Okay, this is how we are going to actually access all these different models without having to, you know, open up all the different apps, right? So, you're just going to go You're just going to want to go to personal, and then you're going to want to go to profile. Okay? And then click API keys, and then click new key. And we're going to call this LM Council test we're going to call this LM Council test key. key. And then credit You can leave that blank. Let's click create. Now, it's going to give you the key. You can copy the key, and we're going to go back to Claude. And it said, "Boom, done. .env created." And we can see here it is right here. So, now we just simply just paste the key in there. Obviously, I'm going to delete this key because I just showed it. Um so, this is going to be deleted right after this video. It's very important that you keep your keys secret, right? Because if someone gets a hold of your key, like if someone got this key, they could run up my bill and, you know, run up my charge it like just charge my card uh using OpenRouter, right? So, this is going to be deleted immediately after that. Uh after this video. But, I'm going to click save. Okay, so I click save, and we should be good to go now. I'm going to say, "Hey, I just added the OpenRouter API key in my environment file. Can you uh make sure that it's there?" Okay? We'll say that. All right. So, it did verify that it is indeed there, and it said, "You're good to run the cross-vendor mode whenever you want. So now we can say {slash} LLM you want. So now we can say {slash} LLM council council run the cross vendor mode. And I want you to answer this question. Should I keep scaling my low ticket or should I pivot and focus more on high ticket AI agency stuff? My low ticket is an $8,000 a month recurring school membership where I basically give all the AI sauce for business owners who want to scale their content, their ads, their business operations with AI so they can save time, save money, and get more done. Now right now it's at $8,000 MRR. Basically I just need more to post more and get more traffic if I want to scale that up, but I want to know what's the fastest path to $50,000 a month. I want you to answer this question for me and use cross vendor mode. Okay, boom. So now if we run that prompt, now it's going to do the actual workflow that is faithful to what workflow that is faithful to what Karpathy Karpathy you know had imagined in the first place. You can see now it's running cross vendor council via open router. If we click this well, let's wait. Okay, so look, check this out guys. It ran the cross vendor council and we can see this was the response from GPT 5.5, this was the response from Gemini 3.1 Pro, this was Opus, this was Grok, and we have another one GPT 5.5 is the reviewer, reviewer, reviewer. So we basically used a bunch of these different models, right? To actually different models, right? To actually um um just get a much more thorough response by you know having all these different models answer for us instead of just Claude. And so we can see that we actually got a different response based on the different methods. So in the one where we just ran Opus, we can see you know we had the generalist, the first principles, all these guys. We can view the transcript of each of these agents, okay? So, it had all these different agents that spawned in. It had the reviewer agents, but all of these were running on the same model. It's all running on Opus. And basically, uh this one where we just ran Claude, it said, "Scale the school. Don't pivot to high ticket, but don't kill it either. Demote it down to a cash bridge and a lead source." Um blah blah blah blah. Pull the pricing lever. Raise your school price. Make sure in your number one KPI. But if we do look at the the actual council that like run with ran with different models, we can see it was more on the side of high ticket, right? Um so, you get different responses. I would say probably this is the most thorough response because we actually called all these different models, okay? So, this is basically the best way to actually answer questions and solve problems with AI in the most thorough way possible. Now, it is going to charge you, right? Because Open Router, you're paying API prices, okay? So, if you go here, and if we look at our our our test key, we could see that it it literally cost 20 cents for that answer. Now, just to get that one answer, it cost 20 cents, okay? So, most of the time, honestly, I think just having the Claude council is good enough. It's just like if you want to be extra extra thorough what when deciding things or doing stuff, you can you do have the option to run the faithful uh workflow, which is what Karpathy designed, where we have all the different models, not just Claude. And so, that's basically the whole entire setup, guys. I gave you the skill and everything and all the files that you need for free. Now, if you guys want uh a little bit more in-depth help, okay? If you're a business owner, you want to scale with AI, you want to work faster, work smarter, uh and save money, and save time, uh I do run obviously I run my school group, okay? You can join it right here. If you click the link down in the description or down below this video, you can actually join my school group. And inside of here, I will walk you through uh installing these skills and getting all these files and actually getting you up to speed with AI so that you can work faster and better and more efficient, okay? We do a bunch of stuff in here. I do content reviews for all the members and I respond with a full loom I will respond to every single member with like a full loom breakdown. So whether you're having content problems or you're having AI problems or you want technical support, I will respond fast as in this community personally, okay? You can see in the classroom, we have start here module, we have a Claude code for dummies. So if it's like if you're just getting into AI, have all this material on that and I actually built this entire content OS viral content OS system with all my skills, all my templates and you can get everything in here so that you can just download and plug and play these systems without having to, you know, go through the effort of building all this stuff yourself. I also do weekly group calls. I'm about to have one in literally 13 minutes. I'm about to get on with the community and problem solve with you guys hands-on. So if you're a business owner and you want to take a little shortcut and just get the information, get all the stuff plug and play, I would definitely recommend joining my school definitely recommend joining my school community. community. And if you're a more advanced business owner, if you're a business owner doing over $10,000 a month and you want me to DFY implement some custom solutions and custom, you know, AI solutions for your business, I actually have that available here as well. So you can just book in, speak with me, we'll talk about the scope of your project and I will actually done for you build all the systems for you. So we got something in we got something for everyone in here. Would highly recommend joining a community of people. This is the best fastest way to like actually get ahead on this AI stuff and just plug and play these systems so you're good to go. Hopefully I'll see you in there. Hopefully you enjoyed the free value. Let me know. I'll see you guys in the next one. Peace.

## Timestamped

`[00:01]` In this video, I'm going to show you
`[00:02]` exactly how to set up an LLM council so
`[00:04]` that you can get better answers from
`[00:06]` your AI when you're asking it very
`[00:08]` important questions. This has to do with
`[00:11]` like strategic questions about your
`[00:13]` business or your personal life that
`[00:15]` require a very thorough amount of
`[00:17]` reasoning, right? Um and so our goal
`[00:20]` here is to set up this LLM council so
`[00:22]` that we can get an unbiased and thorough
`[00:24]` answer from our LLM rather than just
`[00:28]` having it give us an answer straightaway
`[00:30]` without it consulting, you know, any
`[00:32]` other advisers or anything. And so for
`[00:34]` example, if you're if you're trying to
`[00:35]` ask a question like, you know, should I
`[00:36]` pivot my business to scale low ticket or
`[00:38]` high ticket, you know, that's like a
`[00:40]` very high-level important uh strategic
`[00:43]` question. And sometimes you want to
`[00:45]` consult AI on it, right? And so I'm
`[00:47]` going to show you how to get an unbiased
`[00:48]` answer because the problem is that
`[00:51]` recently Stanford did a study where they
`[00:54]` basically concluded that AI is more
`[00:56]` likely to agree with you even when you
`[00:59]` have like a stupid idea, right? It's 49%
`[01:02]` more likely to just agree with whatever
`[01:04]` you're saying. So for example, if I ask
`[01:06]` it this question of like should I pivot
`[01:08]` my business to scale low ticket, well,
`[01:10]` it already knows a little bit about me.
`[01:11]` It already knows that I'm, you know,
`[01:13]` have preferences in a certain direction.
`[01:15]` And so it's basically just going to
`[01:17]` agree with me, right? It's It's just
`[01:19]` going to say, "Hey, you should just keep
`[01:20]` doing your thing. Like keep doing your
`[01:21]` low ticket thing, right?" That's the
`[01:23]` problem that we're trying to solve,
`[01:24]` okay? How do we solve this problem? We
`[01:27]` basically are using a concept called
`[01:29]` stochastic consensus. A stochastic
`[01:32]` consensus is a process where we have a
`[01:34]` bunch of individuals
`[01:36]` basically argue and debate against each
`[01:39]` other to give you a final consensus,
`[01:42]` right? Multiple AI agents are spawned in
`[01:45]` with different configurations.
`[01:47]` And they're each independent and they're
`[01:48]` going to each do their independent
`[01:51]` perspective on it and then argue against
`[01:53]` each other, debate each other to finally
`[01:56]` give you an an answer. And this
`[01:58]` consistently outperforms when you just
`[02:00]` ask it the question straight up, right?
`[02:03]` So, that's exactly what we're going to
`[02:05]` be setting up today so that you can ask
`[02:07]` your AI questions like, you know, should
`[02:09]` I pivot my business this direction or
`[02:11]` should I text her back or like should I
`[02:12]` do this or whatever, right? And so,
`[02:15]` let's get straight into it, okay?
`[02:17]` let's get straight into it, okay? So,
`[02:18]` So,
`[02:18]` um basically, it here's how it's going
`[02:21]` to work, okay? These are the different
`[02:22]` agents that we're spawning in. The first
`[02:24]` is a contrarian, the second is a first
`[02:26]` principles agent, the third is an
`[02:28]` expansionist, we have an outsider, we
`[02:30]` have an executor,
`[02:32]` and then we have a final chairman who
`[02:33]` makes the final call, okay? Each of
`[02:36]` these agents have their own separate
`[02:39]` prompts and kind of their own
`[02:40]` perspective and biases to kind of
`[02:43]` evaluate all angles of the question, all
`[02:47]` evaluate all angles of the question, all right?
`[02:48]` right?
`[02:48]` So, I'm going to give you everything
`[02:50]` that you need for free, okay? For free.
`[02:53]` I'm going to give you all the files I
`[02:54]` wrote I already wrote all the code. I
`[02:55]` already uh delved into the the GitHub
`[02:58]` repo by Karpathy. This was actually
`[03:00]` created by Andrej Karpathy who is like
`[03:02]` AI goat. Uh he was a founder and OpenAI.
`[03:05]` He works at Anthropic now and he was the
`[03:07]` one who created this LLM council in the
`[03:09]` first place.
`[03:10]` All right? So, this is basically what
`[03:12]` that is based off of is his GitHub repo.
`[03:15]` So, the first thing to do is going to be
`[03:16]` to go down below this video and download
`[03:19]` the skill files, okay? So, if you go
`[03:21]` down below this video, whether it's on
`[03:23]` YouTube or if you're watching it in
`[03:24]` Notion, there should be a Google Drive
`[03:26]` folder just like this, okay? So, click
`[03:28]` on this Google Drive folder. It's going
`[03:30]` to bring you here. Or for you, it might
`[03:32]` look like this, okay?
`[03:34]` So, what you're going to do is just
`[03:35]` click download all. And then just give
`[03:37]` it a second, that's going to download.
`[03:40]` Okay, it just zipped up the file and
`[03:42]` then we can download so we can save and
`[03:44]` then we can click here to open it up in
`[03:46]` our downloads folder. We can see it's
`[03:47]` right here. We can double click this and
`[03:49]` it's going to extract the file and here
`[03:51]` we have all the skill files ready to go.
`[03:53]` And inside we have this folder. It's
`[03:55]` called LLM Council and inside of that we
`[03:57]` have all the scripts and we have the
`[03:59]` actual code, the skill MD file that I
`[04:01]` created for you guys. Okay. [snorts] So,
`[04:04]` we want to take this folder and we want
`[04:06]` to basically move it to the right place.
`[04:08]` Okay, so I'm going to open up a new
`[04:11]` finder window. So, we have one over here
`[04:13]` and one over here. Okay? And the next
`[04:16]` thing you need to do is open up your
`[04:19]` Claude desktop app or whatever LLM
`[04:21]` you're using. If you're using ChatGPT or
`[04:23]` Codex, that's fine. We're just going to
`[04:25]` go into Claude, okay?
`[04:27]` And we are going to go into a new chat.
`[04:30]` Let's actually go into code, okay? We
`[04:31]` got to use Claude code for this,
`[04:33]` otherwise it's not going to work. And
`[04:34]` what I want you to do is say something
`[04:36]` like this.
`[04:37]` Hey, can you give me the file path to
`[04:39]` where our global skills are installed?
`[04:41]` Just give me the file path uh so I can
`[04:42]` navigate there.
`[04:45]` Okay? So, we're going to say something
`[04:46]` like that. Shouldn't take long.
`[04:49]` Okay, boom. It just gave us the file
`[04:50]` path. So, it's right here. We're going
`[04:52]` to copy this file path right here. It's
`[04:55]` users, your name, .claud skills. We're
`[04:57]` going to copy that. We're going to go
`[04:59]` back to finder. And
`[05:02]` the one that you just downloaded is over
`[05:03]` here. We're going to open up this new
`[05:05]` window and we're going to do command
`[05:07]` shift G. Command shift G and we're going
`[05:09]` to paste that in. And we hit enter.
`[05:12]` Boom. Okay, so now this is going to be
`[05:15]` where our skill files live, okay? For
`[05:17]` you it's probably empty. And for me, I
`[05:19]` already have this downloaded, so
`[05:21]` obviously it's already right here. I'm
`[05:22]` just going to delete that, okay? What
`[05:25]` you want to do is just drag this file
`[05:27]` that you just downloaded from me, just
`[05:29]` drag it over here. Boom. There it is.
`[05:32]` Okay? So, now we can X out this file and
`[05:35]` then let's just quit Claude and then
`[05:37]` we'll reopen the app.
`[05:40]` we'll reopen the app. Claude.
`[05:46]` We reopen the app.
`[05:46]` Boom. And now if we do {slash} LLM
`[05:49]` Council, we can see we do have the skill
`[05:52]` available to us now. It's as simple as
`[05:54]` that. Okay?
`[05:57]` Now, here's how the skill works by
`[05:59]` default. Okay, so if I ask it a question
`[06:02]` like LLM Council, you know, should I
`[06:06]` um focus
`[06:09]` on scaling the low ticket or should I
`[06:10]` pivot to high ticket? Uh my goal is to
`[06:13]` make, you know, uh $50,000 a month as
`[06:15]` fast as possible. Uh
`[06:17]` which route should I go? The school is
`[06:20]` already at $8,000 MRR and the high
`[06:23]` ticket I'm doing AI agency services. I
`[06:24]` want to know which one that I should
`[06:26]` focus or scale more uh so that I can hit
`[06:29]` 50k a month as fast as possible.
`[06:31]` So, we can ask it a question like that
`[06:33]` and by default, it's it's going to run
`[06:37]` the skill, right? You'll see it run.
`[06:38]` We'll go back to that. But by default,
`[06:40]` it's going to run all these sub agents
`[06:42]` like this
`[06:43]` all on Opus 4.8. Okay? Opus 4.8 is the
`[06:47]` model that we're running on Claude.
`[06:50]` And it's going to run this
`[06:52]` using a Claude Council. So, it's going
`[06:54]` to spawn five agents. And as you can see
`[06:57]` to spawn five agents. And as you can see here,
`[06:58]` here,
`[06:58]` uh it'll do that in a second, but all of
`[07:00]` these agents are going to run on the
`[07:02]` Claude Opus 4.8 model, which is pretty
`[07:05]` good, right? We can see
`[07:07]` Okay, boom. It's spawning in all the
`[07:08]` agents. We have the pragmatist, we have
`[07:10]` the red teamer.
`[07:11]` We have
`[07:13]` one more here. Let's see what this one
`[07:15]` is. But you you click into the each of
`[07:17]` these and we can see
`[07:19]` each of them is with their own prompt,
`[07:22]` right? Their own prompt and this is
`[07:24]` exactly how we do that um stochastic
`[07:28]` debate, right? We're having each of them
`[07:29]` spawn in and basically argue against
`[07:31]` each other.
`[07:32]` We see we have uh 1 2 3 4. It's spawning
`[07:36]` in all the sub agents, right? One of
`[07:37]` them already finished. Okay? So, that's
`[07:39]` by default. And you don't need to plug
`[07:42]` in any other things. Like by default,
`[07:44]` it's just going to work. They're all
`[07:45]` going to run on a Claude model. However,
`[07:48]` the original design of this was meant to
`[07:54]` run on different models so that we could
`[07:56]` avoid the vulnerabilities of running
`[07:59]` just one model, right? Because Claude
`[08:02]` usually responds in a certain way,
`[08:03]` ChatGPT usually responds in a certain
`[08:05]` way, Gemini
`[08:07]` also usually responds in a certain way.
`[08:09]` Gemini might be better at some things,
`[08:11]` Claude might be better at some things.
`[08:13]` And so, if you click down below, uh you
`[08:16]` can view the original repo. Okay, this
`[08:18]` is the link to the original repo built
`[08:20]` by Karpathy himself.
`[08:22]` And the original design was built for
`[08:26]` different models so that we could spawn
`[08:28]` out these different agents with
`[08:29]` different models. So, if you want to run
`[08:31]` the advanced version that's going to
`[08:33]` give you the best, highest quality, like
`[08:35]` ultimate answer,
`[08:37]` where all the different models debate
`[08:38]` each other, I'm going to show you how to
`[08:40]` do that right now.
`[08:43]` All right, so the first thing to do is
`[08:44]` create a project. So, I'm going to go
`[08:47]` into this projects folder that I have on
`[08:49]` my computer. It doesn't matter. You can
`[08:50]` just go documents or honestly wherever
`[08:52]` you want to store this, okay? It do- it
`[08:54]` doesn't matter. You can even put it on
`[08:55]` your desktop. But just go somewhere and
`[08:57]` we're going to create a new folder.
`[08:58]` We're going to call this LLM
`[09:01]` We're going to call this LLM Council
`[09:03]` Council
`[09:03]` uh folder. Call it that. And then, we're
`[09:06]` just going to click inside of this
`[09:07]` just going to click inside of this folder.
`[09:08]` folder.
`[09:08]` And actually, we don't need to do that.
`[09:10]` We can do start a new session. And we're
`[09:12]` going to go here and click open folder.
`[09:15]` And then, we're going to go to projects
`[09:16]` and we're going to click that LLM
`[09:18]` Council folder. Okay? We're going to
`[09:20]` click open. And then, you're going to
`[09:22]` want to say something like this.
`[09:24]` Create a .env file in this folder uh for
`[09:30]` the LLM Council skill so that I can put
`[09:32]` my OpenRouter API key into the .env
`[09:36]` my OpenRouter API key into the .env file.
`[09:38]` file.
`[09:38]` Okay? So,
`[09:41]` we're just going to say something like
`[09:42]` that. It's going to create the .env file
`[09:43]` for us, okay? And what we're going to do
`[09:46]` next is go to a site called
`[09:48]` next is go to a site called openrouter.ai.
`[09:50]` openrouter.ai.
`[09:50]` Openrouter.ai basically allows you to
`[09:54]` run multiple LLMs on all these different
`[09:56]` models. So, if we click explore models
`[09:58]` here, we basically have access to all of
`[10:00]` these different models. Okay, this is
`[10:03]` how we are going to actually access all
`[10:05]` these different models without having
`[10:06]` to, you know, open up all the different
`[10:09]` apps, right? So, you're just going to go
`[10:11]` You're just going to want to go to
`[10:12]` personal, and then you're going to want
`[10:14]` to go to profile. Okay? And then click
`[10:18]` API keys, and then click new key. And
`[10:22]` we're going to call this LM Council test
`[10:25]` we're going to call this LM Council test key.
`[10:26]` key.
`[10:26]` And then credit You can leave that
`[10:28]` blank. Let's click create. Now, it's
`[10:31]` going to give you the key. You can copy
`[10:33]` the key, and we're going to go back to
`[10:35]` Claude. And it said, "Boom, done. .env
`[10:37]` created." And we can see here it is
`[10:40]` right here. So, now we just simply just
`[10:43]` paste the key in there. Obviously, I'm
`[10:45]` going to delete this key because I just
`[10:47]` showed it. Um so, this is going to be
`[10:49]` deleted right after this video. It's
`[10:51]` very important that you keep your keys
`[10:52]` secret, right? Because if someone gets a
`[10:54]` hold of your key, like if someone got
`[10:55]` this key, they could run up my bill and,
`[10:58]` you know, run up my charge it like just
`[11:01]` charge my card uh using OpenRouter,
`[11:03]` right? So, this is going to be deleted
`[11:05]` immediately after that. Uh after this
`[11:07]` video. But, I'm going to click save.
`[11:10]` Okay, so I click save, and we should be
`[11:12]` good to go now. I'm going to say,
`[11:14]` "Hey, I just added the OpenRouter API
`[11:16]` key in my environment file. Can you uh
`[11:19]` make sure that it's there?"
`[11:26]` Okay? We'll say that.
`[11:26]` All right. So, it did verify that it is
`[11:27]` indeed there, and it said, "You're good
`[11:30]` to run the cross-vendor mode whenever
`[11:31]` you want. So now we can say {slash} LLM
`[11:36]` you want. So now we can say {slash} LLM council
`[11:37]` council
`[11:37]` run the cross vendor mode.
`[11:41]` And I want you to answer this question.
`[11:43]` Should I keep scaling my low ticket or
`[11:46]` should I pivot and focus more on high
`[11:48]` ticket AI agency stuff? My low ticket is
`[11:50]` an $8,000 a month recurring school
`[11:52]` membership where I basically give all
`[11:55]` the AI sauce for business owners who
`[11:57]` want to scale their content, their ads,
`[11:58]` their business operations with AI so
`[12:00]` they can save time, save money, and get
`[12:02]` more done. Now right now it's at $8,000
`[12:05]` MRR. Basically I just need more to post
`[12:07]` more and get more traffic if I want to
`[12:08]` scale that up, but I want to know what's
`[12:10]` the fastest path to $50,000 a month. I
`[12:13]` want you to answer this question for me
`[12:14]` and use cross vendor mode.
`[12:17]` Okay, boom. So now if we run that
`[12:19]` prompt, now it's going to do the actual
`[12:23]` workflow that is faithful to what
`[12:26]` workflow that is faithful to what Karpathy
`[12:27]` Karpathy
`[12:27]` you know had imagined in the first
`[12:29]` place. You can see now it's running
`[12:31]` cross vendor council via open router. If
`[12:33]` we click this
`[12:35]` well, let's wait.
`[12:37]` Okay, so look, check this out guys.
`[12:39]` It ran the cross vendor council and we
`[12:41]` can see this was the response from GPT
`[12:44]` 5.5, this was the response from Gemini
`[12:46]` 3.1 Pro, this was Opus, this was Grok,
`[12:50]` and we have another one GPT 5.5 is the
`[12:53]` reviewer, reviewer, reviewer. So we
`[12:55]` basically used a bunch of these
`[12:58]` different models, right? To actually
`[13:02]` different models, right? To actually um
`[13:04]` um
`[13:04]` just get a much more thorough response
`[13:07]` by you know
`[13:09]` having all these different models answer
`[13:10]` for us instead of just Claude.
`[13:17]` And so we can see that we actually got a
`[13:17]` different response based on the
`[13:19]` different methods. So in the one where
`[13:21]` we just ran Opus, we can see you know we
`[13:23]` had the generalist, the first
`[13:24]` principles, all these guys. We can view
`[13:26]` the transcript of each of these agents,
`[13:28]` okay? So, it had all these different
`[13:30]` agents that spawned in. It had the
`[13:31]` reviewer agents, but all of these were
`[13:33]` running on the same model. It's all
`[13:35]` running on Opus. And basically,
`[13:37]` uh this one where we just ran Claude, it
`[13:40]` said, "Scale the school. Don't pivot to
`[13:42]` high ticket, but don't kill it either.
`[13:44]` Demote it down to a cash bridge and a
`[13:45]` lead source." Um blah blah blah blah.
`[13:48]` Pull the pricing lever. Raise your
`[13:50]` school price. Make sure in your number
`[13:51]` one KPI.
`[13:53]` But if we do look at the the actual
`[13:55]` council that like run with ran with
`[13:57]` different models, we can see it was more
`[13:59]` on the side of high ticket, right? Um
`[14:02]` so, you get different responses. I would
`[14:03]` say probably this is the most thorough
`[14:05]` response because we actually called all
`[14:08]` these different models, okay? So, this
`[14:11]` is basically the best way to actually
`[14:14]` answer questions and solve problems with
`[14:16]` AI in the most thorough way possible.
`[14:19]` Now, it is going to charge you, right?
`[14:21]` Because Open Router, you're paying API
`[14:23]` prices, okay? So, if you go here, and if
`[14:26]` we look at our our our test key, we
`[14:27]` could see that it it literally cost 20
`[14:29]` cents for that answer. Now, just to get
`[14:33]` that one answer, it cost 20 cents, okay?
`[14:35]` So, most of the time, honestly, I think
`[14:37]` just having the Claude council is good
`[14:39]` enough. It's just like if you want to be
`[14:41]` extra extra thorough what when deciding
`[14:44]` things or doing stuff, you can you do
`[14:46]` have the option to run the faithful uh
`[14:48]` workflow, which is what Karpathy
`[14:49]` designed, where we have all the
`[14:50]` different models, not just Claude.
`[14:53]` And so, that's basically the whole
`[14:54]` entire setup, guys. I gave you the skill
`[14:57]` and everything and all the files that
`[14:58]` you need for free. Now, if you guys want
`[15:02]` uh a little bit more in-depth help,
`[15:04]` okay? If you're a business owner, you
`[15:05]` want to scale with AI, you want to work
`[15:07]` faster, work smarter, uh and save money,
`[15:10]` and save time, uh I do run obviously I
`[15:13]` run my school group, okay? You can join
`[15:15]` it right here. If you click the link
`[15:16]` down in the description or down below
`[15:18]` this video, you can actually join my
`[15:19]` school group. And inside of here, I will
`[15:21]` walk you through uh installing these
`[15:24]` skills and getting all these files and
`[15:26]` actually getting you up to speed with AI
`[15:28]` so that you can work faster and better
`[15:30]` and more efficient, okay? We do a bunch
`[15:32]` of stuff in here. I do content reviews
`[15:34]` for all the members and I respond with a
`[15:36]` full loom I will respond to every single
`[15:39]` member with like a full loom breakdown.
`[15:42]` So whether you're having content
`[15:43]` problems or you're having AI problems or
`[15:45]` you want technical support, I will
`[15:47]` respond fast as in this community
`[15:50]` personally, okay? You can see in the
`[15:51]` classroom, we have start here module, we
`[15:53]` have a Claude code for dummies. So if
`[15:55]` it's like if you're just getting into
`[15:57]` AI, have all this material on that and I
`[15:59]` actually built this entire content OS
`[16:01]` viral content OS system with all my
`[16:03]` skills, all my templates and you can get
`[16:05]` everything in here so that you can just
`[16:07]` download and plug and play these systems
`[16:09]` without having to, you know, go through
`[16:11]` the effort of building all this stuff
`[16:13]` yourself. I also do weekly group calls.
`[16:16]` I'm about to have one in literally 13
`[16:18]` minutes. I'm about to get on with the
`[16:20]` community and problem solve with you
`[16:21]` guys hands-on. So if you're a business
`[16:23]` owner and you want to take a little
`[16:25]` shortcut and just get the information,
`[16:26]` get all the stuff plug and play, I would
`[16:28]` definitely recommend joining my school
`[16:30]` definitely recommend joining my school community.
`[16:32]` community.
`[16:32]` And if you're a more advanced business
`[16:34]` owner, if you're a business owner doing
`[16:35]` over $10,000 a month and you want me to
`[16:38]` DFY implement some custom solutions and
`[16:40]` custom, you know, AI solutions for your
`[16:42]` business, I actually have that available
`[16:44]` here as well. So you can just book in,
`[16:46]` speak with me, we'll talk about the
`[16:47]` scope of your project and I will
`[16:49]` actually done for you build all the
`[16:51]` systems for you. So we got something in
`[16:54]` we got something for everyone in here.
`[16:55]` Would highly recommend joining a
`[16:56]` community of people. This is the best
`[16:58]` fastest way to like actually get ahead
`[17:00]` on this AI stuff and just plug and play
`[17:02]` these systems so you're good to go.
`[17:04]` Hopefully I'll see you in there.
`[17:05]` Hopefully you enjoyed the free value.
`[17:07]` Let me know. I'll see you guys in the
`[17:08]` next one. Peace.
