# I Fully Automated My Video Editing Using Claude Code (Full Walkthrough)

- **Source:** https://www.youtube.com/watch?v=HzXD4GVqXwM
- **Uploader:** Christian Peverelli
- **Uploaded:** 2026-10-04
- **Duration:** 16:58
- **Detected language:** en (p=1.00)
- **Model:** small.en

## Transcript

Everything you're seeing in this video was edited by my Claude Code system while I was asleep. Every cut, every sound, every animation, like this one, or this one, or this one, was made without touching a timeline and no, I don't know how to code. So today I'm going to pull the curtain and show you exactly how I built this expert editor step by step. The tools, how to set them up, how I taught it my style, the exact cost, and how I'm saving thousands of dollars a month. Let's go. Okay, so making a video like this one used to take a small team. And to be clear, I still have one job to hit record and also to provide feedback. But in my system, every other job goes to a different tool. So I'm going to break these down for you one by one. Now the first one is the editor. That's the person who sits in front of the timeline for hours. They watch every clip, they pick the ones they like, cut out the ones that they don't, decides where every zoom goes and also figures out the graphics and animations that they want and where. Now in my system, Claude code is the tool that does all of that. Think of this role like the project manager of the entire video. Now I personally use the desktop version of Claude, it works perfectly there. And Claude code can work locally, which means that it actually uses my computer for me. It can access the files, it uses other programs. And finally, it's able to put the output inside of a folder on my computer. Now that's actually important because Claude actually is the coordinator of all the other tools here. There's one catch here, Claude can't actually hear my videos. So how does it know what I said and where I messed up to be able to cut the whole thing together? Now that's the second job that we have in this list. It is the job of the transcriber. Now this is the person who listens to all the footage, transforms that, types it out into text and puts timestamps on these. And the tool that does that is called Parakeet. It's a completely free tool and it was built by NVIDIA, which is the leading manufacturer of chips. No, not Doritos or Lays. I mean like the chips, right? For AI. Mmm, chips. Get back to it. So Parakeet does the transcription and then Claude is able to actually read the timestamps and exactly what is being said and is able to then use that for the next step of the process. This is how we're able to identify and chop up the footage so that we have the right takes. Job three is actually the animator. This is the person who builds every single title, every logo that pops in, any motion graphics. And in the old world, this was done with After Effects. You literally had to use one tool just to do these things. And this is exactly where Hyperframes comes in, tool number three. Now this again is a free tool developed by HeyGen, which is the video platform. Claude writes each animation like a tiny website and then Hyperframe turns that into a 4K video. So now the animations can look sharp even on a large TV. It all runs on my own computer so it actually costs me nothing. However, in videos, sometimes I'll say things like open AI just announced, blah, blah, blah. And when I say that, I actually need the fourth person, which is the researcher. Someone who goes out and is able to find a screenshot of that announcement or a post on X or a research paper that proves the point that I'm actually illustrating and turns that into what we call B-roll. Things that you show on top of the video that are basically outside footage. And the thing that does that is something we all actually have already on our laptops, which is a browser. So in my case, I use Google Chrome and then Claude is able to actually use the browser to go out there and do that research. And in the background, Claude, my researcher is able to grab screenshots or record video scrolling down a website. And then it can do things like highlight lines or actually zoom into specific sections of those pages. And the great thing is that it only shows you exact facts. So it's really taking the original X post or the actual webpage. So I can just say what happens and the proof shows up on screen. Now, the fifth job is the screen editor. Now, this is mainly because I love making simple tutorials, teaching people how to use AI tools, how to make money with them. But I use screen sharing a lot. And that's why I used a tool called TELA. TELA records my face and my screen at the same time. And because TELA has a connector called an MCP, I can connect it directly into Claude code and it's able to do all the things it does inside of the software. The cuts, the zooms, the layout, the formatting, yada, yada, everything that you can do inside the software, you're able to do via Claude code. So I literally only just have to record through it and it does the rest. But up until now, we've just been talking about the visuals of this video. Every great video team has what we call a sound designer. This is a person who decides what music goes on each clip, what sound effects go in when specific things happen and make sure that these are also on brand. Because you probably don't want music styles that make you want to sleep when you're teaching a tutorial, for example. So for this, I have a sound base called Epidemic Sound. It is something I pay for, we'll talk about pricing at the end. And I'm also able to connect it to Claude and it's going to be able to go out, search for sounds. And the cool thing is that I can train it on what I like. Usually, I like having the hook be a little bit suspenseful and then I go into some kind of upbeat music that's kind of like low-fi hip-hop and have it very, very low. And so yeah, sound effects also have their own rules. I'll talk about how I set up all of this right after. And now the seventh member of the team is actually the finisher. This is the person who joins all the pieces together and looks to see if there's no mistakes. This tool is called FFmpeg. It's free and it's been cutting videos for more than 20 years. In fact, it's under the hood of pretty much every editing software that exists today. So Claude uses it and it's responsible for cutting out any black screens, checked that there's nothing off with audio sync before I ever get to even see the video. So those are the seven tools or jobs that have to be done. But none of those actually know what my video is supposed to look like. That's probably the most important thing and it's called the skill. A skill is simply just a file of instructions that Claude reads before it does the job. And it's pretty much my editing style broken down into specifics. The colors, the fonts, the animations, the sounds, with a bunch of details that are basically my preferences. Mine is called youtube-edit and it's about 1,400 lines. But the great thing is that Claude Code actually built this whole thing for me. So pretty much Claude runs all of the tools and then I tell Claude what good looks like. Now I'm not technical and you probably aren't either. So I'm going to show you exactly how to set this up. It's super easy. Okay, so the first step to set this up is to download Claude. Now you can go to Anthropic's website and you can download the desktop app. That's what I recommend. That's what I use. And once you've properly installed that, it's going to ask you to create an account. You're going to have to use either Google or your username and password to do that. And if it is the first time you download Claude in general, it will try to set you up. I do recommend you go through that. I have a full other video on how to get set up properly. You don't actually need that here. Now for this, you do need to have a paid plan. I would upgrade to the $20 plan. No need to go for higher than that at this point. Now when you hit the main interface, it's going to look something like this. It might look a little different just because things change constantly. But basically, if you click on new, you're going to be able to start a new session inside of Claude. Now up here on the left, we have Claude, which is the normal version, which is chat and co-work. And right here we have Claude code. So for this, you want to be on Claude code. And then there are a couple of setup steps you need to do before. We actually move forward. First off, you want to make sure that you are on local, meaning that it's using your computer to do this. Next up, you need to actually determine the folder in which you are going to be working. For this, you can just click on this. As you see, I'm already connected to my Claude code folder, but you can basically click on this one and you can add a completely new folder. You can create one here and then you attach it. After that, you want to turn the permissions on auto so that it can run without you having to say yes, no to thousands of things. And then you're going to want to switch the model to one of the latest models, just because the setup is an important step. After that, it will be able to run on a cheaper model. And finally, you do want to come down here to the left and you want to go inside of settings. You need to go to Claude code. And here you can copy the exact settings that I have here, or you can just decide to basically turn on one very important thing for us to be able to browse the internet, which is to turn that on and that's done right here. When you're done, you can pretty much close this and you can go back to the main menu, click on you. Then Claude code is actually going to be very good at setting this up itself. So in this case, I'll give it a prompt like this. Could you please create a video editing system for me? I'd like to use Hyperframes, FFmpeg, TELA and Epidemic Sounds for this system. Run me through how to set it up step by step. So one route is simply to get it to guide you through the process. Now, the other way to do this, Claude should be able to download and install everything that it needs and it can. It will ask you to actually connect a couple of these tools as well. You come here to the left and you go into customize and you go into connectors. And then you can pretty much select the tool. So in this case, I'll go and look for TELA, which is my screen recording device. As you can see, I've already attached this. If not, you can just click on the plus button right there. And for Epidemic Sounds, it's the same thing. Look for Epidemic Sounds. There you go. It is the music and sound effects and you can go ahead and turn this on. It'll ask you to log in in a separate browser. Once you've done that, you'll see this check mark. Now, all the other things it needs, it'll download itself. But if it doesn't find hyperframes for any reason, you can simply Google hyperframes. You'll find the link to the repo, but you can also find hyperframes inside of the connectors too. Now, once you've connected all those things, you want to make sure that it saves them as a skill on your computer. And once that has actually saved inside that one chat or thread, you want to open a new thread and give it a first test. Now, as you can see, setting these things up is pretty straightforward. What takes time is to basically fine-tune the look and feel. And if you'd like to just download my skill and use that, you can feel free to do so inside my free community. Link is below. But now let's jump into how I actually taught it my style. Well, at first, I pretty much gave it notes on every single thing I made. And I started with small clips, usually just the hook of a video. And when it gave me a first edit, I would basically give it very specific time-stamped feedback on the work it had done. And then 10 days in, I actually took one of the hooks and started just implementing sound. I had to try a bunch of different sound effects on one hook. And I had to go through about eight to 10 different sounds until I found something that really worked for what I enjoyed. Because what it had made was a little too busy for my liking. So this was mainly used for sound effects, right? When something pops up, you could have a little pop. When something's clicked on, you can have the little clicking sound. And as it started making decisions on how to use the different sounds I gave it access to, I basically told it, okay, let's reduce the sound of that. Okay, I think that I don't like this sound at all. Just take it completely out. And slowly but surely, it was learning exactly what I liked. Now, here's the absolute key to all of this. When you actually give it feedback and after that, you tell it to save what it's learned to the actual skill itself. That way, when you create a new edit, you'll constantly be improving your editing system. Then I created a new session where I had this updated skill and I basically put another hook. This time, I loved that it had gone out and grabbed a specific logo and used the sound effect to show it, but I wanted it to be shown slightly larger. I also didn't really like the color palette it was using for some sections or some animations, so I decided to switch it up a little bit. And the more videos I made and provided feedback on the better it got. And today, my skill has 36 different rules that it has to abide to. Then I started discovering really cool new animations and I started deciding which ones would make sense for the content that I actually made. And so slowly, I started adding more of these. Every time I used them, I would fine tune them. And the awesome thing is that every note that I gave it, the next time, it never made that same mistake again, meaning that I basically was getting exactly the output that I was looking for. All right, my friends, enough talking. Let me actually show you this in action. Okay, so we're back inside plot code now and since I've already created the skill or a first version of it, I can pretty much run it at any time. I'll come here. I'm going to basically add a raw file. So here, I have a hook that I recorded earlier today for this specific video. I'm going to go ahead and open this one. Then I'm going to tell it this. Please use my YouTube editing skill to edit this hook for my YouTube video. I can also choose to add any additional things I'd like if there are specific things I'd like it to do inside the hook. So in this case, when I say things like zoom, you can actually show a zoom. When I talk about a sound effect, you can make a sound effect. And then when I talk about the different animations, you can basically showcase three of the most impressive animations, either that I've already done in the past or that you really like from the library that we have inside the skill. So those are just instructions that I'm giving it because I know the hook I recorded and I'd like to actually show the editing skill inside the hook as well. But you could give it pretty much any instructions. At this point, I'm going to pretty much just press enter and let's see what Claude actually does. Running the skill, YouTube edits as I said, so it finds the skill and it just starts running it. Probing the clip and listing, okay. Now just to be clear, this is a completely unedited thing. So basically, I make lots of mistakes. I stop in the middle of the hook and look at my notes. It is basically cutting it up. So it's copying the clip, transcribing it using Parakeet, which is the tool that we talked about earlier now. That will install automatically in the setup as we talked about. Now because this process will take anywhere from 10 to maybe 20 minutes, I'll show you the V1 of the hook. Everything you're seeing in this video was edited by my Claude Code system while I was asleep. Every cut, every sound, every animation like this one or this one or this one was made without touching a timeline and no, I don't know how to code. Boom, so as you see, there's a couple things I would change from this, but it's pretty much spot on. It basically says that it cut down two minutes and 46 of raw footage into 31 seconds, which is absolutely great. And there are some little edits, right? That I wanna make. So basically what I'll say are things like this. Edit number one will be something like, could you please add some suspense sound throughout this? I'd like for you to pick a track and add it to this hook. I usually like to go through the entire clip and basically give it timestamps like, oh, I saw the second 22, you did this. I'd like for it to be like that. It could be anything from the look to sound to kind of the overall feel or the way it's cutting things. And again, at the end of all this, I can basically tell it, hey, could you please make this a little bit better? And of course, at the end of this, what's cool is I can just say, hey, can you learn from what we just did and add it to the skill? So that was a one shot. What you see at the beginning of this video is the actual final product. And before I used to do this by sections, now I do this, I just dump the entire footage inside. And if I've also recorded inside of Tella, I'm gonna tell it, hey, here are the names of the files because since it has direct access, I don't need to upload the actual documents because yes, there is a human in the loop and it's me and I actually love it. And after shooting this right now, I fed this entire raw footage to Claude Code and tomorrow I'm gonna wake up and see exactly what you've seen on screen. Tomorrow morning, I get to just watch it, give a couple notes and get the final version. So I'm the director, Claude's the editor and I didn't have to edit any, which is great because I actually don't know how to edit at all. So at this point, everyone asked me about the cost. So let's break it down to the dollar. First off, I'm on Claude. I'm on the max plan. It cost me $200 a month. Now that's a flat fee, but I actually use this for all of my work, not just my video editing. So what I did is that I got Claude to actually measure the number of tokens that it used and I have a certain limit of tokens per month. Now my last video after calculations cost me $24 to build and that's at most. Now the great thing is that Hyperframes is completely for free. So is Parakeet, so nothing to pay for there. For Tella, I'm on the annual plan. It cost me $13 per month, which is roughly $2 per video. Epidemic Sounds, which is where I get all of my sound effects and the music as well, cost me $9.99. Again, I'm on the annual plan. So let's add an extra dollar to that. So all in, I'm pretty much paying $27 per video. Now the reality is that for YouTube editors, a good editor costs anywhere between $250 and $1,000 plus per video, meaning that I'm saving hundreds of dollars per video. But the huge benefit for me is actually the speed of execution. I'm now able to plan, shoot, edit, and release a video same day. Whereas before it took me anywhere between three and seven days depending on which editor I was working with. And the revisions usually went back, forth, back, forth. And because of human error, I actually oftentimes had to repeat things that I was seeing that hadn't been changed from one video to the next. Now because I don't want you to suffer through all the same things I did, I'm gonna be giving you this skill for free inside of my free community. It's called We Are No Code. You can find the link below. Now if you wanna both see the editing skill in action for a full video and also get a full breakdown of what was announced for OpenAI Dev Day, you can check out this video right here. Hope you enjoyed this video. I'll see you guys in the next one. Let's go.

## Timestamped

`[00:00]` Everything you're seeing in this video was edited by my Claude Code system while I was asleep.
`[00:05]` Every cut, every sound, every animation, like this one, or this one, or this one,
`[00:15]` was made without touching a timeline and no, I don't know how to code.
`[00:18]` So today I'm going to pull the curtain and show you exactly how I built this expert editor
`[00:23]` step by step. The tools, how to set them up, how I taught it my style,
`[00:27]` the exact cost, and how I'm saving thousands of dollars a month. Let's go.
`[00:31]` Okay, so making a video like this one used to take a small team.
`[00:34]` And to be clear, I still have one job to hit record and also to provide feedback.
`[00:39]` But in my system, every other job goes to a different tool.
`[00:42]` So I'm going to break these down for you one by one.
`[00:44]` Now the first one is the editor. That's the person who sits in front of the timeline for hours.
`[00:49]` They watch every clip, they pick the ones they like, cut out the ones that they don't,
`[00:53]` decides where every zoom goes and also figures out the graphics and animations that they want
`[00:58]` and where. Now in my system, Claude code is the tool that does all of that.
`[01:02]` Think of this role like the project manager of the entire video.
`[01:05]` Now I personally use the desktop version of Claude, it works perfectly there.
`[01:10]` And Claude code can work locally, which means that it actually uses my computer for me.
`[01:15]` It can access the files, it uses other programs. And finally,
`[01:18]` it's able to put the output inside of a folder on my computer.
`[01:21]` Now that's actually important because Claude actually is the coordinator of all the other tools here.
`[01:26]` There's one catch here, Claude can't actually hear my videos.
`[01:30]` So how does it know what I said and where I messed up to be able to cut the whole thing together?
`[01:34]` Now that's the second job that we have in this list. It is the job of the transcriber.
`[01:38]` Now this is the person who listens to all the footage,
`[01:40]` transforms that, types it out into text and puts timestamps on these.
`[01:45]` And the tool that does that is called Parakeet.
`[01:47]` It's a completely free tool and it was built by NVIDIA, which is the leading manufacturer of chips.
`[01:52]` No, not Doritos or Lays. I mean like the chips, right? For AI.
`[01:56]` Mmm, chips.
`[01:57]` Get back to it.
`[01:58]` So Parakeet does the transcription and then Claude is able to actually read the timestamps
`[02:03]` and exactly what is being said and is able to then use that for the next step of the process.
`[02:07]` This is how we're able to identify and chop up the footage so that we have the right takes.
`[02:11]` Job three is actually the animator.
`[02:13]` This is the person who builds every single title,
`[02:16]` every logo that pops in, any motion graphics.
`[02:19]` And in the old world, this was done with After Effects.
`[02:22]` You literally had to use one tool just to do these things.
`[02:25]` And this is exactly where Hyperframes comes in, tool number three.
`[02:28]` Now this again is a free tool developed by HeyGen, which is the video platform.
`[02:33]` Claude writes each animation like a tiny website
`[02:36]` and then Hyperframe turns that into a 4K video.
`[02:40]` So now the animations can look sharp even on a large TV.
`[02:43]` It all runs on my own computer so it actually costs me nothing.
`[02:45]` However, in videos, sometimes I'll say things like open AI just announced, blah, blah, blah.
`[02:50]` And when I say that, I actually need the fourth person, which is the researcher.
`[02:55]` Someone who goes out and is able to find a screenshot of that announcement
`[02:59]` or a post on X or a research paper that proves the point that I'm actually illustrating
`[03:04]` and turns that into what we call B-roll.
`[03:06]` Things that you show on top of the video that are basically outside footage.
`[03:09]` And the thing that does that is something we all actually have already on our laptops,
`[03:13]` which is a browser.
`[03:14]` So in my case, I use Google Chrome and then Claude is able to actually use the browser
`[03:19]` to go out there and do that research.
`[03:21]` And in the background, Claude, my researcher is able to grab screenshots
`[03:25]` or record video scrolling down a website.
`[03:27]` And then it can do things like highlight lines
`[03:29]` or actually zoom into specific sections of those pages.
`[03:33]` And the great thing is that it only shows you exact facts.
`[03:35]` So it's really taking the original X post or the actual webpage.
`[03:40]` So I can just say what happens and the proof shows up on screen.
`[03:43]` Now, the fifth job is the screen editor.
`[03:45]` Now, this is mainly because I love making simple tutorials,
`[03:48]` teaching people how to use AI tools, how to make money with them.
`[03:51]` But I use screen sharing a lot.
`[03:53]` And that's why I used a tool called TELA.
`[03:55]` TELA records my face and my screen at the same time.
`[03:58]` And because TELA has a connector called an MCP,
`[04:01]` I can connect it directly into Claude code
`[04:03]` and it's able to do all the things it does inside of the software.
`[04:07]` The cuts, the zooms, the layout, the formatting, yada, yada,
`[04:10]` everything that you can do inside the software,
`[04:12]` you're able to do via Claude code.
`[04:14]` So I literally only just have to record through it and it does the rest.
`[04:18]` But up until now, we've just been talking about the visuals of this video.
`[04:21]` Every great video team has what we call a sound designer.
`[04:24]` This is a person who decides what music goes on each clip,
`[04:27]` what sound effects go in when specific things happen
`[04:31]` and make sure that these are also on brand.
`[04:33]` Because you probably don't want music styles that make you want to sleep
`[04:36]` when you're teaching a tutorial, for example.
`[04:38]` So for this, I have a sound base called Epidemic Sound.
`[04:41]` It is something I pay for, we'll talk about pricing at the end.
`[04:44]` And I'm also able to connect it to Claude
`[04:46]` and it's going to be able to go out, search for sounds.
`[04:48]` And the cool thing is that I can train it on what I like.
`[04:50]` Usually, I like having the hook be a little bit suspenseful
`[04:53]` and then I go into some kind of upbeat music
`[04:55]` that's kind of like low-fi hip-hop and have it very, very low.
`[04:59]` And so yeah, sound effects also have their own rules.
`[05:01]` I'll talk about how I set up all of this right after.
`[05:03]` And now the seventh member of the team is actually the finisher.
`[05:06]` This is the person who joins all the pieces together
`[05:08]` and looks to see if there's no mistakes.
`[05:10]` This tool is called FFmpeg.
`[05:12]` It's free and it's been cutting videos for more than 20 years.
`[05:16]` In fact, it's under the hood of pretty much every editing software that exists today.
`[05:19]` So Claude uses it and it's responsible for cutting out any black screens,
`[05:23]` checked that there's nothing off with audio sync
`[05:25]` before I ever get to even see the video.
`[05:28]` So those are the seven tools or jobs that have to be done.
`[05:30]` But none of those actually know what my video is supposed to look like.
`[05:33]` That's probably the most important thing and it's called the skill.
`[05:37]` A skill is simply just a file of instructions
`[05:40]` that Claude reads before it does the job.
`[05:42]` And it's pretty much my editing style broken down into specifics.
`[05:46]` The colors, the fonts, the animations, the sounds,
`[05:49]` with a bunch of details that are basically my preferences.
`[05:52]` Mine is called youtube-edit and it's about 1,400 lines.
`[05:55]` But the great thing is that Claude Code actually built this whole thing for me.
`[05:59]` So pretty much Claude runs all of the tools
`[06:01]` and then I tell Claude what good looks like.
`[06:03]` Now I'm not technical and you probably aren't either.
`[06:05]` So I'm going to show you exactly how to set this up.
`[06:07]` It's super easy.
`[06:08]` Okay, so the first step to set this up is to download Claude.
`[06:11]` Now you can go to Anthropic's website and you can download the desktop app.
`[06:15]` That's what I recommend.
`[06:16]` That's what I use.
`[06:17]` And once you've properly installed that,
`[06:19]` it's going to ask you to create an account.
`[06:20]` You're going to have to use either Google
`[06:22]` or your username and password to do that.
`[06:24]` And if it is the first time you download Claude in general,
`[06:27]` it will try to set you up.
`[06:29]` I do recommend you go through that.
`[06:30]` I have a full other video on how to get set up properly.
`[06:33]` You don't actually need that here.
`[06:35]` Now for this, you do need to have a paid plan.
`[06:37]` I would upgrade to the $20 plan.
`[06:39]` No need to go for higher than that at this point.
`[06:41]` Now when you hit the main interface,
`[06:43]` it's going to look something like this.
`[06:44]` It might look a little different just because things change constantly.
`[06:47]` But basically, if you click on new,
`[06:49]` you're going to be able to start a new session inside of Claude.
`[06:53]` Now up here on the left, we have Claude,
`[06:55]` which is the normal version, which is chat and co-work.
`[06:58]` And right here we have Claude code.
`[07:00]` So for this, you want to be on Claude code.
`[07:02]` And then there are a couple of setup steps you need to do before.
`[07:04]` We actually move forward.
`[07:06]` First off, you want to make sure that you are on local,
`[07:09]` meaning that it's using your computer to do this.
`[07:11]` Next up, you need to actually determine the folder
`[07:13]` in which you are going to be working.
`[07:15]` For this, you can just click on this.
`[07:17]` As you see, I'm already connected to my Claude code folder,
`[07:20]` but you can basically click on this one
`[07:22]` and you can add a completely new folder.
`[07:24]` You can create one here and then you attach it.
`[07:27]` After that, you want to turn the permissions on auto
`[07:29]` so that it can run without you having to say yes, no to thousands of things.
`[07:33]` And then you're going to want to switch the model
`[07:35]` to one of the latest models,
`[07:37]` just because the setup is an important step.
`[07:39]` After that, it will be able to run on a cheaper model.
`[07:41]` And finally, you do want to come down here to the left
`[07:43]` and you want to go inside of settings.
`[07:45]` You need to go to Claude code.
`[07:48]` And here you can copy the exact settings that I have here,
`[07:51]` or you can just decide to basically turn on
`[07:54]` one very important thing for us to be able to browse the internet,
`[07:57]` which is to turn that on and that's done right here.
`[08:01]` When you're done, you can pretty much close this
`[08:03]` and you can go back to the main menu, click on you.
`[08:06]` Then Claude code is actually going to be very good
`[08:08]` at setting this up itself.
`[08:10]` So in this case, I'll give it a prompt like this.
`[08:13]` Could you please create a video editing system for me?
`[08:16]` I'd like to use Hyperframes, FFmpeg,
`[08:19]` TELA and Epidemic Sounds for this system.
`[08:22]` Run me through how to set it up step by step.
`[08:26]` So one route is simply to get it to guide you through the process.
`[08:28]` Now, the other way to do this,
`[08:30]` Claude should be able to download and install
`[08:31]` everything that it needs and it can.
`[08:33]` It will ask you to actually connect a couple of these tools as well.
`[08:37]` You come here to the left and you go into customize
`[08:40]` and you go into connectors.
`[08:42]` And then you can pretty much select the tool.
`[08:44]` So in this case, I'll go and look for TELA,
`[08:46]` which is my screen recording device.
`[08:48]` As you can see, I've already attached this.
`[08:50]` If not, you can just click on the plus button right there.
`[08:53]` And for Epidemic Sounds, it's the same thing.
`[08:55]` Look for Epidemic Sounds.
`[08:57]` There you go.
`[08:57]` It is the music and sound effects
`[08:59]` and you can go ahead and turn this on.
`[09:01]` It'll ask you to log in in a separate browser.
`[09:02]` Once you've done that, you'll see this check mark.
`[09:04]` Now, all the other things it needs, it'll download itself.
`[09:07]` But if it doesn't find hyperframes for any reason,
`[09:10]` you can simply Google hyperframes.
`[09:12]` You'll find the link to the repo,
`[09:14]` but you can also find hyperframes inside of the connectors too.
`[09:17]` Now, once you've connected all those things,
`[09:18]` you want to make sure that it saves them as a skill on your computer.
`[09:22]` And once that has actually saved inside that one chat or thread,
`[09:26]` you want to open a new thread and give it a first test.
`[09:28]` Now, as you can see, setting these things up
`[09:30]` is pretty straightforward.
`[09:31]` What takes time is to basically fine-tune the look and feel.
`[09:34]` And if you'd like to just download my skill and use that,
`[09:37]` you can feel free to do so inside my free community.
`[09:39]` Link is below.
`[09:40]` But now let's jump into how I actually taught it my style.
`[09:43]` Well, at first, I pretty much gave it notes
`[09:45]` on every single thing I made.
`[09:47]` And I started with small clips,
`[09:49]` usually just the hook of a video.
`[09:50]` And when it gave me a first edit,
`[09:52]` I would basically give it very specific
`[09:54]` time-stamped feedback on the work it had done.
`[09:57]` And then 10 days in, I actually took one of the hooks
`[09:59]` and started just implementing sound.
`[10:01]` I had to try a bunch of different sound effects on one hook.
`[10:04]` And I had to go through about eight to 10 different sounds
`[10:07]` until I found something that really worked for what I enjoyed.
`[10:10]` Because what it had made was a little too busy for my liking.
`[10:13]` So this was mainly used for sound effects, right?
`[10:15]` When something pops up, you could have a little pop.
`[10:17]` When something's clicked on,
`[10:18]` you can have the little clicking sound.
`[10:20]` And as it started making decisions
`[10:21]` on how to use the different sounds I gave it access to,
`[10:24]` I basically told it, okay, let's reduce the sound of that.
`[10:27]` Okay, I think that I don't like this sound at all.
`[10:30]` Just take it completely out.
`[10:31]` And slowly but surely, it was learning exactly what I liked.
`[10:34]` Now, here's the absolute key to all of this.
`[10:36]` When you actually give it feedback and after that,
`[10:39]` you tell it to save what it's learned
`[10:41]` to the actual skill itself.
`[10:43]` That way, when you create a new edit,
`[10:45]` you'll constantly be improving your editing system.
`[10:47]` Then I created a new session where I had this updated skill
`[10:50]` and I basically put another hook.
`[10:52]` This time, I loved that it had gone out
`[10:54]` and grabbed a specific logo
`[10:55]` and used the sound effect to show it,
`[10:57]` but I wanted it to be shown slightly larger.
`[11:00]` I also didn't really like the color palette
`[11:02]` it was using for some sections or some animations,
`[11:04]` so I decided to switch it up a little bit.
`[11:06]` And the more videos I made
`[11:08]` and provided feedback on the better it got.
`[11:10]` And today, my skill has 36 different rules
`[11:12]` that it has to abide to.
`[11:13]` Then I started discovering really cool new animations
`[11:16]` and I started deciding which ones would make sense
`[11:18]` for the content that I actually made.
`[11:20]` And so slowly, I started adding more of these.
`[11:23]` Every time I used them, I would fine tune them.
`[11:25]` And the awesome thing is that every note that I gave it,
`[11:28]` the next time, it never made that same mistake again,
`[11:30]` meaning that I basically was getting
`[11:32]` exactly the output that I was looking for.
`[11:34]` All right, my friends, enough talking.
`[11:36]` Let me actually show you this in action.
`[11:38]` Okay, so we're back inside plot code now
`[11:40]` and since I've already created the skill
`[11:42]` or a first version of it,
`[11:43]` I can pretty much run it at any time.
`[11:45]` I'll come here.
`[11:46]` I'm going to basically add a raw file.
`[11:48]` So here, I have a hook that I recorded earlier today
`[11:53]` for this specific video.
`[11:55]` I'm going to go ahead and open this one.
`[11:57]` Then I'm going to tell it this.
`[11:59]` Please use my YouTube editing skill
`[12:02]` to edit this hook for my YouTube video.
`[12:05]` I can also choose to add any additional things I'd like
`[12:07]` if there are specific things I'd like it to do inside the hook.
`[12:10]` So in this case, when I say things like zoom,
`[12:13]` you can actually show a zoom.
`[12:15]` When I talk about a sound effect,
`[12:18]` you can make a sound effect.
`[12:20]` And then when I talk about the different animations,
`[12:22]` you can basically showcase
`[12:24]` three of the most impressive animations,
`[12:26]` either that I've already done in the past
`[12:28]` or that you really like from the library
`[12:30]` that we have inside the skill.
`[12:32]` So those are just instructions that I'm giving it
`[12:33]` because I know the hook I recorded
`[12:35]` and I'd like to actually show the editing skill
`[12:38]` inside the hook as well.
`[12:39]` But you could give it pretty much any instructions.
`[12:41]` At this point, I'm going to pretty much just press enter
`[12:44]` and let's see what Claude actually does.
`[12:46]` Running the skill, YouTube edits as I said,
`[12:48]` so it finds the skill and it just starts running it.
`[12:51]` Probing the clip and listing, okay.
`[12:54]` Now just to be clear, this is a completely unedited thing.
`[12:58]` So basically, I make lots of mistakes.
`[12:59]` I stop in the middle of the hook and look at my notes.
`[13:03]` It is basically cutting it up.
`[13:04]` So it's copying the clip, transcribing it using Parakeet,
`[13:08]` which is the tool that we talked about earlier now.
`[13:10]` That will install automatically in the setup
`[13:12]` as we talked about.
`[13:13]` Now because this process will take anywhere
`[13:15]` from 10 to maybe 20 minutes,
`[13:17]` I'll show you the V1 of the hook.
`[13:19]` Everything you're seeing in this video
`[13:20]` was edited by my Claude Code system while I was asleep.
`[13:24]` Every cut, every sound, every animation like this one
`[13:29]` or this one or this one
`[13:34]` was made without touching a timeline
`[13:36]` and no, I don't know how to code.
`[13:38]` Boom, so as you see, there's a couple things
`[13:39]` I would change from this, but it's pretty much spot on.
`[13:42]` It basically says that it cut down two minutes
`[13:45]` and 46 of raw footage into 31 seconds,
`[13:48]` which is absolutely great.
`[13:49]` And there are some little edits, right?
`[13:51]` That I wanna make.
`[13:52]` So basically what I'll say are things like this.
`[13:55]` Edit number one will be something like,
`[13:57]` could you please add some suspense sound throughout this?
`[14:01]` I'd like for you to pick a track and add it to this hook.
`[14:05]` I usually like to go through the entire clip
`[14:07]` and basically give it timestamps like,
`[14:09]` oh, I saw the second 22, you did this.
`[14:12]` I'd like for it to be like that.
`[14:14]` It could be anything from the look to sound
`[14:16]` to kind of the overall feel
`[14:18]` or the way it's cutting things.
`[14:20]` And again, at the end of all this,
`[14:22]` I can basically tell it,
`[14:23]` hey, could you please make this a little bit better?
`[14:26]` And of course, at the end of this,
`[14:27]` what's cool is I can just say,
`[14:29]` hey, can you learn from what we just did
`[14:30]` and add it to the skill?
`[14:32]` So that was a one shot.
`[14:33]` What you see at the beginning of this video
`[14:34]` is the actual final product.
`[14:36]` And before I used to do this by sections,
`[14:37]` now I do this, I just dump the entire footage inside.
`[14:40]` And if I've also recorded inside of Tella,
`[14:44]` I'm gonna tell it, hey, here are the names of the files
`[14:47]` because since it has direct access,
`[14:48]` I don't need to upload the actual documents
`[14:51]` because yes, there is a human in the loop
`[14:52]` and it's me and I actually love it.
`[14:54]` And after shooting this right now,
`[14:55]` I fed this entire raw footage to Claude Code
`[14:58]` and tomorrow I'm gonna wake up
`[14:59]` and see exactly what you've seen on screen.
`[15:01]` Tomorrow morning, I get to just watch it,
`[15:03]` give a couple notes and get the final version.
`[15:05]` So I'm the director, Claude's the editor
`[15:08]` and I didn't have to edit any,
`[15:09]` which is great because I actually don't know
`[15:10]` how to edit at all.
`[15:11]` So at this point, everyone asked me about the cost.
`[15:13]` So let's break it down to the dollar.
`[15:15]` First off, I'm on Claude.
`[15:16]` I'm on the max plan.
`[15:17]` It cost me $200 a month.
`[15:19]` Now that's a flat fee,
`[15:20]` but I actually use this for all of my work,
`[15:22]` not just my video editing.
`[15:23]` So what I did is that I got Claude
`[15:25]` to actually measure the number of tokens that it used
`[15:27]` and I have a certain limit of tokens per month.
`[15:30]` Now my last video after calculations
`[15:32]` cost me $24 to build and that's at most.
`[15:35]` Now the great thing is that Hyperframes
`[15:37]` is completely for free.
`[15:38]` So is Parakeet, so nothing to pay for there.
`[15:40]` For Tella, I'm on the annual plan.
`[15:42]` It cost me $13 per month,
`[15:43]` which is roughly $2 per video.
`[15:46]` Epidemic Sounds, which is where I get
`[15:48]` all of my sound effects and the music as well,
`[15:50]` cost me $9.99.
`[15:52]` Again, I'm on the annual plan.
`[15:54]` So let's add an extra dollar to that.
`[15:56]` So all in, I'm pretty much paying $27 per video.
`[15:59]` Now the reality is that for YouTube editors,
`[16:01]` a good editor costs anywhere between $250
`[16:04]` and $1,000 plus per video,
`[16:07]` meaning that I'm saving hundreds of dollars per video.
`[16:10]` But the huge benefit for me
`[16:11]` is actually the speed of execution.
`[16:13]` I'm now able to plan, shoot, edit,
`[16:16]` and release a video same day.
`[16:18]` Whereas before it took me anywhere
`[16:20]` between three and seven days
`[16:22]` depending on which editor I was working with.
`[16:24]` And the revisions usually went back, forth, back, forth.
`[16:27]` And because of human error,
`[16:29]` I actually oftentimes had to repeat things
`[16:31]` that I was seeing that hadn't been changed
`[16:33]` from one video to the next.
`[16:34]` Now because I don't want you to suffer
`[16:35]` through all the same things I did,
`[16:37]` I'm gonna be giving you this skill
`[16:39]` for free inside of my free community.
`[16:41]` It's called We Are No Code.
`[16:42]` You can find the link below.
`[16:44]` Now if you wanna both see the editing skill
`[16:45]` in action for a full video
`[16:47]` and also get a full breakdown
`[16:49]` of what was announced for OpenAI Dev Day,
`[16:51]` you can check out this video right here.
`[16:53]` Hope you enjoyed this video.
`[16:55]` I'll see you guys in the next one.
`[16:56]` Let's go.
