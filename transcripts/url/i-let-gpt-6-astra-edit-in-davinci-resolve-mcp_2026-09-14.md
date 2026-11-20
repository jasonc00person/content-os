# I Let GPT-6 Astra Edit In DaVinci Resolve MCP

- **Source:** https://www.youtube.com/watch?v=V7CtHz8JFWA
- **Uploader:** Creator Magic
- **Uploaded:** 2026-09-08
- **Duration:** 24:14
- **Method:** YouTube captions (no transcription needed)

## Transcript

now. Look at this. This is happening in real time. Hands off. This is really impressive. This is the best bit of the video. Oh, my goodness me, I am not Editing. I'm an editor of like decades and now AI is doing it for me. even. Look at this. This is insane. It's actually gone ahead and put audio dipping on the audio track. Look at that. To make the edit nice and silky smooth. we've hit AGI here, guys. Okay, here's the deal. I'm Mike here, and I'm wearing headphones today. My background is in audio editing and video production. So when GPT Astra came on the scene and basically said it's AGI for video editing, I got really interested. Then I looked at posts like this post from Higgsfield saying that everything is being edited on an infinite Autonomous canvas with GPT-6 Astra. Then I went along and I actually noticed that Blackmagic just announced DaVinci Resolve 21.1 introducing. Look at this, AI Assistant integration. So that really got my attention. And then I got a message From Brent at OpenAI who says this may make things easier. He's pointed to the first party MCP server, that just landed in DaVinci Resolve. yes, I'm going to install DaVinci Resolve Studio 21.1 and test out the MCP server and see if it truly is the Linux of video editing that I'm looking for. Let's dive in. Quick caveat here because yeah, Linux of video editing. Well that isn't DaVinci Resolve because DaVinci Resolve is not free and open source Diffusion HQ actually Diffusion Studio, that's what I've been using up until now to make most of my edits with AI agents. But hey, maybe blackmagic have made it super easy. All right, let's fire up DaVinci Resolve 21.1. What's new? Look at this, look at this. AI Assistant Control. This is so exciting. Citing ask Claude or ChatGPT to organize media, create edits and batch render. This is what interests me here and this is what we'll be testing out in this video. Right, so I'm going to create a brand new project and I'm going to call this one openclaw to mcp. Okay, and this will be one of the recent videos I actually published on my channel. Started from scratch right here. All right, that said, I've just dragged the clips in, changed the frame rate and we're ready to go. Now I'm not going to do anything. I'm going to see what my AI agent can do from scratch. All right, so we've got Codex up here and we're in the video editing project. It's a project I've created specifically for this purpose. Now one thing I want to make absolutely clear that the videos I've just dragged in are a, raw recording of my face and my screen share for 75 minutes. All the silences, all, all the mistakes, all the problems. If Astra from OpenAI truly is AGI for video editing, I want to experience it without any guidance from me, just going to open the file and show you. It's me clapping to sync there 75 minutes of me going through recording and also looking at things like confused like that because things go wrong. It's all there, all the mistakes and everything. So first of all I'm just going to ask GPT-6 Astra. Okay, I've got DaVinci Resolve running 21.1. They say that it can integrate with AI agents via MCP. Are you able to find that functionality and hook it up so that we can control DaVinci resolve not with the cursor, but with the MCP server. I'm going to get Astra on the case with that and see if it can hook this up itself. Controlling a video editor by the cursor, is not what I want to do. And the reason for it is that controlling by cursor is pretty slow and janky, whereas MCP is like a first party thing. So it's checking the support right now in my local setup and connecting. Okay, it's found it. Your Resolve 21.1 installation includes Blackmagic's native Resolve MCP. This is awesome. Checking the live connection and registering with Codex. Okay, you see, it's as easy as that I've got the ChatGPT app, or the Codex app if you like, installed on my Mac. I asked chat GPT-6 Astra to do the connection for me and it's done it look at this. MCP handshake succeeded. Resolve reports it's running and reachable. So everything is connected up to Codex. This is awesome. Lets give it a go. And I've just moved it over to the right so that my face is not blocking. ChatGPT Connected tested. Okay, excellent. Without cursor control. It's all registered. This is fantastic. To load it into Codex's tool menu, go to Settings MCP servers and restart. Okay, so I'll do that. Okay, so can you see my open DaVinci Resolve session? Are you able to insert both the program and the screen share onto separate video tracks and perform a rough edit for me using only the DaVinci Resolve MCP please. Now that's quite a complex first initial prompt. You'll see I'm using GPT-6 Astra High and it says I'll inspect the open project. So hopefully it's going to see this open Claw two MCP project and edit through Resolve's mcp. I'm very specific here. I don't want it to take over the computer. I don't want computer use. I want this all done via the MCP link to see how good it is. okay. Hands off. At the moment it's thinking things through. It's made a change to a file in the project. We'll see what comes back. Now it seems to be running a lot of scripting here. A lot of Python is getting created. Resolve MCP client Python. I can access the session in both recordings. 75 minutes long. This is correct. 4K 60 frames per second. This is good. Screen recording at 5K. Yes, excellent. Preserving sync. Oh, wow. Okay. Transcription. Initializing. I did not do that. So clearly the MCP is doing something. Resolve has kicked into action over here. This is great. And yes, so that was the first step, getting the transcription what any good AI agent would do before editing. We're in a good place. now this is going to take some time, but the best thing is it's included in my DaVinci Resolve Studio subscription. So all of this is done at, nearly 10 times speed for free. And we see while this is going on, ChatGPT is still thinking here. Resolve is returning the media correctly, but transcription timed out. Oh dear. This is the first error. It didn't time out. It's still going. But ChatGPT over here is getting impatient. It's really interesting because the workflow that I've built that I use now to agentically edit videos uses AssemblyAI transcription that will transcribe 75 minutes in like 20 seconds. So it's kind of painful sitting here watching Resolve take nearly six minutes to transcribe the same video. at this point, B roll of a monkey grinding away typing on a computer transcribing a video would look absolutely epic on screen. Oh, nearly. Yes. Okay, we're transcribed. This is good. let's go back over here to ChatGPT. Hey, the transcription just finished. Can Oh, wow. Okay, hands off. This is happening now. This is my program, my screen, share my program audio, all here in the. Yes, this is. This is kind of what I want to see. This is amazing. Okay, it hasn't actually done anything yet, but it definitely switched the scene here. Now I want it to edit. Okay, what have we got here? The two video tracks are now in place. Transcript shows retakes and long waits so I can make useful content based cuts. Resolve couldn't confirm waveform alignment. Both files are the same recording which I'm using. Wow. Okay, things are happening. Things are actually happening now. I'm not touching resolve. This is interesting. And I can see it's viewed an image. Yes. It's actually watching screenshots of my video as it edits, which is a great sign. Come on, GPT-6 Astra, make your first edit. Wow. Okay, so it's skipping around the video. Look at this. Here is my speech. You can see long gaps as I pause to change scenes or do something different. You'll see there's a lot of retakes here as well. I'm hoping that GPT-6 Astra can see all of this and control it through the resolve. MCP it says I'm keeping your existing program composition as the main picture. Clean screen share cutaways as well to help with readability, removing failed takes, production asides and long waits, and adding markers for the two Clawcast inserts that need your narration. All right, this is great. It has fully picked up context of exactly what I'm trying to do in the video. This is a great start. but just for your information, the video you're Watching is obviously edited, but I've been sitting here for 20 minutes and I still haven't seen a single splice in my timeline. This is not fast. Okay, what's happening here? Okay, everything is gone apart from one single clip here. That's interesting. What are you doing? It looks like it's building a timeline plan. And we can actually see that over here. It's made this new timeline called Rough Cut, All right, comes to 22 minutes, down from 75 minutes. This is pretty cool. I caught a one frame difference in Resolve's trim handling and I'm correcting it before applying cuts across tracks. Okay. So Now, what is really cool is I already completed this video and published it on my channel. And when I edited it with my current agentic process, it made a video that's about 22 minutes in duration. So this is a really good sign. Okay, what's happening here? It's blotted out the screen share. It's focusing on my face now. Look at this. This is happening in real time. Hands off. This is really impressive. This is the best bit of the video. Oh, my goodness me, yes. Maybe we've hit AGI here, guys. So it did a load of stuff, it stopped and now it's continuing again. This is insane. This is stuff that would take me hours post creating a video. It's literally being done in minutes here. Now what I can see is it's doing a few minutes at a time. So it did the first three minutes, it paused, then it did another three minutes, it's pausing. So it's like maybe it's QA ing. I can't tell if it's doing quality assurance right now. It's running a load of Python files that seem to be controlling the Resolve MCP client, which is pretty awesome. I had absolutely no idea that this was possible. Now I'd love to zoom in and see what's going on here. It does seem to be cutting my video quite well, which is good. Wow. More edits are happening here in front of my very eyes. I am not Editing. I'm an editor of like decades and now AI is doing it for me. The thing that used to be the most painful thing for any content creator is getting solved by AI now. And that is huge. And we can actually see now the whole timeline is here in place. We're at 21 minutes and 59 seconds. So that's pretty good. It's actually placing some markers on now all the way through. Look at these markers that are placed on. This is really interesting. I do want to know what kind of markers it's placing on the timeline. Rough cut review. That's the intro. Very nice indeed. We've got another one. Chapter marker Manage, hosting and plans. Okay, so it's like chapter markering here. Choose an AI model. So it's basically placing chapters in blue, then here orange. What have we got? Original source includes setup token. Wow. It's actually telling me here about setup tokens that I should probably take off camera. I love this. Now look at this. The 2159 rough cut is saved. All 96 sections have matching source times and linked video and audio. 10 clean screen share cutaways as well. So it's making decisions on when to use my screen share for readability. This is really, really cool. It's QA ing again, viewing more images like so, and even more images. I'm pretty impressed. Okay, I can tell you this has taken exactly half an hour. So that's the real time. Even though you're watching the edited, final polished cut of me here on YouTube. 30 minutes to get to the rough cut where GPT-6 Astra says it's done. All The full length source timeline is preserved. Markers, flag, missing Clawcast inserts and everything else needed. Okay, the moment of truth. let's play it back and check those edits. Let's dive in. Okay, I'm going to use this open claw. Little bit slow, but you know what? I would accept that edit. That would pass. I wouldn't need to retrim that. It's even. Look at this. This is insane. It's actually gone ahead and put audio dipping on the audio track. Look at that. To make the edit nice and silky smooth. I'm not even going to touch that. I could as an OCD video editor, but I won't. Let's check the next edit here. The first time. Well, if you're not. That is perfect. That is 100% perfect. All right, let's look at this edit now. Since on Hostinger one click deploy is yes. Oh my goodness. Guys, we're an AGI for video editing and audio editing. May I say, as someone who's taught audio editing for like nearly two decades on YouTube, that's done. If you want to see my other channel, that's an archive of how we humans Used to do that stuff. Couple more edits to see where we're at what you want either way when you choose a plan. Nice. So it chose to use my screen share there for readability and then cut back to me with picture in picture at this point. Now this is interesting. As I look along this timeline there's quite a, a big pause here. So I'm concerned by this KVM2 here you can type in. Okay, that is a little bit of silence there. That would be a little bit too long. So that's at this particular timestamp here. So I might go back to chat GPT-6 Astra and see if it can make that one edit for me. I'll just say there is a long silence at 1:20:11. Please fix only this and we'll see if GPT-6 Astra can make just that one little edit there and tighten this bit up. It's actually inspecting right now. Keeping tracks aligned. Of course, that's what we want. you can see there's a two second pause between you and type in my coupon code. So it's going to shorten that. Now again hands off. And there we go. It's done I think. Fantastic. Let's see if we can play back that section and listen again. Here we go. You can type in my. Yeah, that's acceptable. That's okay. Now full disclosure there. That took nearly two minutes for Codex to do using the DaVinci Resolve MCP. Two minutes to make a two second trim is not acceptable. It did remove 1.67 seconds and kept all other tracks aligned which is great. That's good but it's not perfect. If I hit command Z here, look, we get the trims back. Everything can be undone with the command Z. of course what took two minutes here can easily be done by doing shift delete. That took like one second. So in some cases yes. Getting the rough cut and doing the high level edits. Brilliant. Making fine grained changes and QA kind of things that Human in the loop would catch. You probably still want to be doing that as a human, unless you've got loads of coffee and you just want to go off and drink it while the agent makes its small little edits. So this is fun and it's a great thing that can save me a lot of time, but can it do the polish? Okay, now you've done the rough cut, I'm happy with it. I wonder if you can insert an overlay at the start of the video, introducing me as Mike Russell from Creator Magic. Now I'm just doing one simple thing and it's got no house guide on how I do my overlays. So it's going to make it all up. But I'm wondering if. Look, it says it can do this with Resolve's MCP if it could do this. Obviously if I was making a full video I'd put loads more overlays and B rolls and cutaways. But this is just one test. Let's roll back to the start and zoom in here and watch it happen in real time. Okay, it says I'm making a 5 second lower third with soft fade white name text and small teal accent. It will sit on an overlay track. Nice. Okay, look at that. It made it. It has taken nearly three minutes of working here, but it did make it a nice lower third here that I assume it's going to insert on the the timeline. Okay, there we go. Yes. It's done. Look at that. Wow, that's amazing. Let's rewind and play back. OpenClaw 2.0 is here with 16,000 pull requests. Yeah. About half of everything in the project. Okay, nice. Fade in, fade out for the lower third. That is done. It's just wrapping Up. It's doing QA here. Again, looking at the image to check and it says yes, I've added the five second lower third. Mike Russell creator Magic Till Accent. Obviously no style guide here. I did not give it any style guide but the fact it's gone ahead and done that is pretty insane. So I'm pretty happy that pretty much anything related to video editing can now be done in DaVinci resolve. Definitely we can get the rough cut, we can get lower thirds and overlays. I'm sure we could probably get B roll in there as. I'm really happy with this rough cut. It's basically ready to go to YouTube. There are only a couple more things I'd like you to do. First of all, I'd like you to color grade the video like a boss. You're the world class expert in it, so do it for me. And then I'd like you to make sure the loudness is absolutely correct for upload to YouTube. Ensure those two things and then tell me if it's ready to render and if you're able to render it yourself, let me know. Don't render yet, but just tell me if you can. Now this is the one thing that no one tells you when they're playing with video editing. First of all, video editing takes a lot of tokens. My context is now compacting. And the other thing is, well, all those slick demos you see on x and other YouTubers doing that are edited tightly and full disclaimer. I'm editing this video with AI by the way. and they show you that it happens in seconds or minutes, which it really doesn't. I've been sitting here the best part of an hour running this DaVinci Resolve MCP via Codex using GPT-6 Astra. Can it do all this stuff? Yes. Can it do it fast? It's getting better all the time, let's say. But you know, right now I've been sitting here for three minutes watching context automatically compacting. Okay, after four minutes we've done the compaction. Now let's get into action. Okay, it's already working like a pro. Keeping the grade restrained so skin looks better without distorting software interface. I Love your thinking GPT-6 Astra. Let's see what it does. So at the moment you'll see my face and the background pretty washed out. I'm hoping that it makes some changes. It's also checking Resolve's YouTube loudness controls against the whole program. Okay, what I notice is a lot of Python files getting created here, so it doesn't seem fully like it's doing everything via the mcp. A lot of stuff is Codex writing code and analyzing stuff before getting back to Resolve via the mcp. We've got images here of me. That's qa. Okay, again through the MCP client making some changes here and we can see. Yes, render settings are being locked in over here on the left with a preset it has created. Creator Magic YouTube 4K review. Now I didn't create that preset. It seems that Codex is doing that for me. it's backed up the approved edit. It's lifting the tone slightly to stop my excess orange skin and keep the purple studio lighting very nice. Audio analysis is running across the program. Cut some fades. No video render started yet. Okay, audio is already in good shape. We're at 14.69 LUFS with a 1.04 decibels true peak which I can confirm is absolutely correct. So this is really, really good. Just so you know, on color grade and audio, it's been working over 12 minutes now and it's still not quite done. Okay, look at this. The grade is applied. Opening title looks clean. Checking the saved export settings now. Okay, this is looking really good. One thing I will say is I don't see much change in terms of color grade here. It looks pretty much like what we started with, but hopefully the audio will be better. And so you know, this last step is chewing time 15 minutes and we're still not done. Oh, here we go. We're done. That's it. Just as I said that the grade is applied and saved. Brighter, more natural skin tones. Do I can't see much difference. But maybe it did make a difference. Audio is correct, technically. Ready to render. Obviously missing the inserts, which is fine. I can render it through Resolve's mcp. So let's try this render, it. And this is the final step now, the final piece in the pudding. And I can tell you as I type that command in, we're bang on an hour. So let's see. I'll render the graded timeline using the Prepared 4K YouTube preset, then check the Xbox exported file. Hopefully rendering should be pretty quick. And then we can guarantee we can work end to end in DaVinci resolve using only an AI agent. And there we go. Yeah, it's going into the render and it has indeed popped something into the render queue here. This is amazing. This is actually happening in real time. Right now it's rendering my video. So that guarantees the whole process can be automated end to end using your coding agent of choice, in my case, GPT-6 Astra on high mode along with the DaVinci Resolve MCP that was just released today in version 21.1. This is pretty insane. The 4K render is running and I'm saving it as OpenClaw 2 point zero Creator Magic MP4 in your video editing folder. Okay, this is very nice stuff and we are definitely pretty much there with video editing. Yes, it can be done and automated by AI is working in DaVinci Resolve. Great. Well, yes, because I don't need to know the software, I don't need to touch a button. This can all be automated by AI. Now, I'm an Adobe user and a premier user for years and years and yes, Adobe, I would like to see you do the same thing. Not have a proprietary lockdown AI assistant that lives in and is controlled by Adobe inside Premiere. I want to be able to choose Codex or my Claude subscription to edit my videos. I want to bring in skills to make lower thirds and overlays. I want to bring in other skills to make AI B roll. And until someone completely automates that, I'm not calling AI. Video editing done yet. Now let me explain to you a little bit about my video editing process. I am looking for the Linux of video editing. I don't want to be locked in or locked down. I want complete freedom and sovereignty over the kind of edits that I do. And up until a long time and still to this day, even the video right now that you're watching, it's edited in a buzz channel and I'm automating that using Claude code on Fable 5.1. It does the edits and then previously I was eyeballing them by pulling a timeline into DaVinci resolve. I would love to do the same thing in Premiere, but it doesn't support timeline imports that my agent can make, which is a bit of a bummer. for the eyeball, I'm not even sure if I need to use DaVinci Resolve or Premiere. Maybe I can just use another open app that there's lots of them out there. ChatCut is a big one and it's gaining in popularity. I've been messing around with Diffusion Studio, which seems to cut out the bloat that Resolve and Premiere suffer with. So the jury is still out on how this process will look. But in my opinion, the absolute meat, the brains, lie in how you automate this with your AI agent, the skills you create and how you tell your agent to edit. That's where the mote is. It's not about doing the edit or what software you use to QA or eyeball. That's basically solved and we could just use a simple video editor in the browser to check that stuff out. We don't need these big editing programs anymore. Blackmagic and DaVinci Resolve have certainly laid down the gauntlet here by making a Resolve MCP available. have been recording this RAW video for about an hour. I'm about to hand this ProRes that's recorded on my Mac Studio off to my AI agents that will edit and publish the video that you're watching right now. Let me know your thoughts. Has this been solved in your opinion, would you use this workflow? What do you want to see? What are the missing pieces? What did I not mention that I should have? Let me know in the comments down below. I'm thoroughly engaged in this topic right now. I want to see this succeed and I want video editing, overlays, aib, roll, all of that. I want it solved for creators so that literally my job is to come up with the ideas in collaboration with AI. Hit record in my studio, stop the recording and that's where I finish as a content creator. When I hit stop on the recording button, my AI agents in an ideal world should take over, publish and have it ready for you to watch on YouTube. Hopefully that's coming soon. Thank you so much for watching and YouTube is showing a video on your screen right now that's been determined by the algorithm to be absolutely perfect for you. So you should probably pay attention and you should watch it next. Thanks.

## Timestamped

`[00:00]` now.
`[00:00]` Look at this. This is happening in real time.
`[00:02]` Hands off.
`[00:03]` This is really impressive.
`[00:04]` This is the best bit of the video.
`[00:06]` Oh, my goodness me, I am not Editing.
`[00:08]` I'm an editor of like decades and now AI is doing it for me.
`[00:14]` even.
`[00:15]` Look at this. This is insane.
`[00:16]` It's actually gone ahead and put audio dipping on the audio track.
`[00:20]` Look at that.
`[00:21]` To make the edit nice and silky smooth.
`[00:23]` we've hit AGI here, guys.
`[00:25]` Okay, here's the deal.
`[00:26]` I'm Mike here, and I'm wearing headphones today.
`[00:29]` My background is in audio editing and video production.
`[00:32]` So when GPT Astra came on the scene and basically said it's AGI for video editing,
`[00:38]` I got really interested.
`[00:40]` Then I looked at posts like this post from Higgsfield saying that everything
`[00:44]` is being edited on an infinite Autonomous canvas with GPT-6 Astra.
`[00:49]` Then I went along and I actually noticed that Blackmagic just announced DaVinci
`[00:54]` Resolve 21.1 introducing.
`[00:57]` Look at this, AI Assistant integration.
`[01:00]` So that really got my attention.
`[01:03]` And then I got a message From Brent
`[01:05]` at OpenAI who says this may make things easier.
`[01:08]` He's pointed to the first party MCP
`[01:10]` server, that just landed in DaVinci Resolve.
`[01:13]` yes, I'm going to install DaVinci Resolve Studio 21.1 and test out the MCP server
`[01:19]` and see if it truly is the Linux of video editing that I'm looking for.
`[01:24]` Let's dive in.
`[01:25]` Quick caveat here because yeah, Linux of video editing.
`[01:28]` Well that isn't DaVinci Resolve because DaVinci Resolve is not free and open
`[01:32]` source Diffusion HQ actually Diffusion Studio, that's what I've been using up
`[01:37]` until now to make most of my edits with AI agents.
`[01:41]` But hey, maybe blackmagic have made it super easy.
`[01:44]` All right, let's fire up DaVinci Resolve 21.1.
`[01:48]` What's new?
`[01:49]` Look at this, look at this.
`[01:50]` AI Assistant Control.
`[01:52]` This is so exciting.
`[01:53]` Citing ask Claude or ChatGPT to organize media, create edits and batch render.
`[01:58]` This is what interests me here and this is what we'll be testing out in this
`[02:03]` video.
`[02:04]` Right, so I'm going to create a brand new project and I'm going to call this
`[02:06]` one openclaw to mcp.
`[02:10]` Okay, and this will be one of the recent videos I actually published on my channel.
`[02:13]` Started from scratch right here.
`[02:16]` All right, that said, I've just dragged the clips in, changed the frame rate
`[02:19]` and we're ready to go.
`[02:20]` Now I'm not going to do anything.
`[02:22]` I'm going to see what my AI agent can do from scratch.
`[02:25]` All right, so we've got Codex up here and we're in the video editing project.
`[02:28]` It's a project I've created specifically for this purpose.
`[02:32]` Now one thing I want to make absolutely clear that the videos I've just dragged
`[02:36]` in are a, raw recording of my face and my screen share for 75 minutes.
`[02:41]` All the silences, all, all the mistakes, all the problems.
`[02:45]` If Astra from OpenAI truly is AGI for video editing, I want to experience it
`[02:51]` without any guidance from me, just going to open the file and show you.
`[02:54]` It's me clapping to sync there 75 minutes of me going through recording and also
`[02:59]` looking at things like confused like that because things go wrong.
`[03:03]` It's all there, all the mistakes and everything.
`[03:06]` So first of all I'm just going to ask GPT-6 Astra.
`[03:09]` Okay, I've got DaVinci Resolve running 21.1.
`[03:13]` They say that it can integrate with AI agents via MCP.
`[03:17]` Are you able to find that functionality and hook it up so that we can control
`[03:21]` DaVinci resolve not with the cursor, but with the MCP server.
`[03:26]` I'm going to get Astra on the case with
`[03:27]` that and see if it can hook this up itself.
`[03:30]` Controlling a video editor by the cursor, is not what I want to do.
`[03:33]` And the reason for it is that controlling by cursor is pretty slow and janky,
`[03:39]` whereas MCP is like a first party thing.
`[03:41]` So it's checking the support right now in my local setup and connecting.
`[03:45]` Okay, it's found it.
`[03:46]` Your Resolve 21.1 installation includes Blackmagic's native Resolve MCP.
`[03:52]` This is awesome.
`[03:53]` Checking the live connection and registering with Codex.
`[03:55]` Okay, you see, it's as easy as that I've got the ChatGPT app, or the Codex app
`[04:00]` if you like, installed on my Mac.
`[04:02]` I asked chat GPT-6 Astra to do the connection for me and it's done it look at
`[04:08]` this.
`[04:09]` MCP handshake succeeded.
`[04:10]` Resolve reports it's running and reachable.
`[04:12]` So everything is connected up to Codex.
`[04:14]` This is awesome.
`[04:15]` Lets give it a go.
`[04:17]` And I've just moved it over to the right so that my face is not blocking.
`[04:20]` ChatGPT Connected tested.
`[04:23]` Okay, excellent.
`[04:24]` Without cursor control.
`[04:25]` It's all registered.
`[04:26]` This is fantastic.
`[04:28]` To load it into Codex's tool menu, go to Settings MCP servers and restart.
`[04:33]` Okay, so I'll do that.
`[04:34]` Okay, so can you see my open DaVinci Resolve session?
`[04:38]` Are you able to insert both the program and the screen share onto separate video
`[04:43]` tracks and perform a rough edit for me using only the DaVinci Resolve MCP please.
`[04:49]` Now that's quite a complex first initial prompt.
`[04:52]` You'll see I'm using GPT-6 Astra High and it says I'll inspect the open project.
`[04:57]` So hopefully it's going to see this open Claw two MCP project and edit through
`[05:01]` Resolve's mcp.
`[05:03]` I'm very specific here.
`[05:04]` I don't want it to take over the computer.
`[05:06]` I don't want computer use.
`[05:07]` I want this all done via the MCP link to see how good it is.
`[05:13]` okay.
`[05:13]` Hands off. At the moment it's thinking things through.
`[05:15]` It's made a change to a file in the project.
`[05:18]` We'll see what comes back.
`[05:19]` Now it seems to be running a lot of scripting here.
`[05:21]` A lot of Python is getting created.
`[05:24]` Resolve MCP client Python.
`[05:26]` I can access the session in both recordings.
`[05:28]` 75 minutes long.
`[05:29]` This is correct.
`[05:29]` 4K 60 frames per second.
`[05:31]` This is good.
`[05:32]` Screen recording at 5K.
`[05:33]` Yes, excellent.
`[05:35]` Preserving sync.
`[05:36]` Oh, wow.
`[05:37]` Okay.
`[05:38]` Transcription.
`[05:39]` Initializing.
`[05:40]` I did not do that.
`[05:41]` So clearly the MCP is doing something.
`[05:44]` Resolve has kicked into action over here.
`[05:46]` This is great.
`[05:47]` And yes, so that was the first step, getting the transcription what any good
`[05:51]` AI agent would do before editing.
`[05:53]` We're in a good place.
`[05:55]` now this is going to take some time, but the best thing is it's included in my
`[05:58]` DaVinci Resolve Studio subscription.
`[06:00]` So all of this is done at, nearly 10 times speed for free.
`[06:04]` And we see while this is going on, ChatGPT is still thinking here.
`[06:07]` Resolve is returning the media correctly, but transcription timed out.
`[06:11]` Oh dear.
`[06:12]` This is the first error.
`[06:13]` It didn't time out.
`[06:14]` It's still going.
`[06:15]` But ChatGPT over here is getting impatient.
`[06:17]` It's really interesting because the workflow that I've built that I use now to
`[06:21]` agentically edit videos uses AssemblyAI transcription that will transcribe 75
`[06:27]` minutes in like 20 seconds.
`[06:29]` So it's kind of painful sitting here watching Resolve take nearly six minutes
`[06:34]` to transcribe the same video.
`[06:36]` at this point, B roll of a monkey grinding away typing on a computer transcribing
`[06:41]` a video would look absolutely epic on screen.
`[06:44]` Oh, nearly.
`[06:45]` Yes.
`[06:46]` Okay, we're transcribed.
`[06:47]` This is good.
`[06:48]` let's go back over here to ChatGPT.
`[06:51]` Hey, the transcription just finished.
`[06:53]` Can Oh, wow.
`[06:54]` Okay, hands off.
`[06:54]` This is happening now.
`[06:56]` This is my program, my screen, share my program audio, all here in the.
`[07:01]` Yes, this is.
`[07:02]` This is kind of what I want to see.
`[07:04]` This is amazing.
`[07:05]` Okay, it hasn't actually done anything yet, but it definitely switched the scene
`[07:10]` here.
`[07:11]` Now I want it to edit.
`[07:12]` Okay, what have we got here?
`[07:13]` The two video tracks are now in place.
`[07:15]` Transcript shows retakes and long waits so I can make useful content based cuts.
`[07:20]` Resolve couldn't confirm waveform alignment.
`[07:23]` Both files are the same recording which I'm using.
`[07:25]` Wow.
`[07:26]` Okay, things are happening.
`[07:27]` Things are actually happening now.
`[07:29]` I'm not touching resolve.
`[07:30]` This is interesting.
`[07:31]` And I can see it's viewed an image.
`[07:33]` Yes.
`[07:33]` It's actually watching screenshots of my video as it edits, which is a great
`[07:37]` sign.
`[07:38]` Come on, GPT-6 Astra, make your first edit.
`[07:40]` Wow.
`[07:41]` Okay, so it's skipping around the video.
`[07:43]` Look at this.
`[07:44]` Here is my speech.
`[07:44]` You can see long gaps as I pause to change scenes or do something different.
`[07:49]` You'll see there's a lot of retakes here as well.
`[07:52]` I'm hoping that GPT-6 Astra can see all of this and control it through the resolve.
`[07:56]` MCP it says I'm keeping your existing program composition as the main picture.
`[08:01]` Clean screen share cutaways as well to help with readability, removing failed
`[08:05]` takes, production asides and long waits, and adding markers for the two Clawcast
`[08:09]` inserts that need your narration.
`[08:12]` All right, this is great.
`[08:13]` It has fully picked up context of exactly what I'm trying to do in the video.
`[08:17]` This is a great start.
`[08:18]` but just for your information, the video you're Watching is obviously edited,
`[08:22]` but I've been sitting here for 20 minutes and I still haven't seen a single splice
`[08:27]` in my timeline.
`[08:28]` This is not fast.
`[08:30]` Okay, what's happening here?
`[08:32]` Okay, everything is gone apart from one single clip here.
`[08:36]` That's interesting.
`[08:37]` What are you doing?
`[08:39]` It looks like it's building a timeline plan.
`[08:42]` And we can actually see that over here.
`[08:43]` It's made this new timeline called Rough Cut, All right, comes to 22 minutes,
`[08:48]` down from 75 minutes.
`[08:49]` This is pretty cool.
`[08:51]` I caught a one frame difference in Resolve's trim handling and I'm correcting
`[08:54]` it before applying cuts across tracks.
`[08:56]` Okay.
`[08:57]` So Now, what is really cool is I already completed this video and published it
`[09:01]` on my channel.
`[09:02]` And when I edited it with my current agentic process, it made a video that's
`[09:05]` about 22 minutes in duration.
`[09:07]` So this is a really good sign.
`[09:09]` Okay, what's happening here?
`[09:10]` It's blotted out the screen share.
`[09:12]` It's focusing on my face now.
`[09:13]` Look at this.
`[09:14]` This is happening in real time.
`[09:15]` Hands off.
`[09:16]` This is really impressive.
`[09:18]` This is the best bit of the video.
`[09:19]` Oh, my goodness me, yes.
`[09:21]` Maybe we've hit AGI here, guys.
`[09:24]` So it did a load of stuff, it stopped and now it's continuing again.
`[09:27]` This is insane.
`[09:28]` This is stuff that would take me hours post creating a video.
`[09:31]` It's literally being done in minutes here.
`[09:34]` Now what I can see is it's doing a few minutes at a time.
`[09:37]` So it did the first three minutes, it paused, then it did another three minutes,
`[09:40]` it's pausing.
`[09:41]` So it's like maybe it's QA ing.
`[09:43]` I can't tell if it's doing quality assurance right now.
`[09:46]` It's running a load of Python files that seem to be controlling the Resolve MCP
`[09:50]` client, which is pretty awesome.
`[09:52]` I had absolutely no idea that this was possible.
`[09:56]` Now I'd love to zoom in and see what's going on here.
`[09:59]` It does seem to be cutting my video quite well, which is good.
`[10:02]` Wow.
`[10:03]` More edits are happening here in front of my very eyes.
`[10:05]` I am not Editing.
`[10:06]` I'm an editor of like decades and now AI is doing it for me.
`[10:11]` The thing that used to be the most painful thing for any content creator is getting
`[10:15]` solved by AI now.
`[10:17]` And that is huge.
`[10:19]` And we can actually see now the whole timeline is here in place.
`[10:22]` We're at 21 minutes and 59 seconds.
`[10:25]` So that's pretty good.
`[10:26]` It's actually placing some markers on now all the way through.
`[10:29]` Look at these markers that are placed on.
`[10:31]` This is really interesting.
`[10:32]` I do want to know what kind of markers it's placing on the timeline.
`[10:36]` Rough cut review.
`[10:37]` That's the intro.
`[10:38]` Very nice indeed.
`[10:39]` We've got another one.
`[10:40]` Chapter marker Manage, hosting and plans.
`[10:42]` Okay, so it's like chapter markering here.
`[10:45]` Choose an AI model.
`[10:47]` So it's basically placing chapters in blue, then here orange.
`[10:50]` What have we got?
`[10:51]` Original source includes setup token.
`[10:53]` Wow.
`[10:54]` It's actually telling me here about setup tokens that I should probably take
`[10:57]` off camera.
`[10:59]` I love this.
`[11:01]` Now look at this.
`[11:01]` The 2159 rough cut is saved.
`[11:03]` All 96 sections have matching source times and linked video and audio.
`[11:07]` 10 clean screen share cutaways as well.
`[11:10]` So it's making decisions on when to use my screen share for readability.
`[11:14]` This is really, really cool.
`[11:16]` It's QA ing again, viewing more images like so, and even more images.
`[11:21]` I'm pretty impressed.
`[11:22]` Okay, I can tell you this has taken exactly half an hour.
`[11:26]` So that's the real time.
`[11:27]` Even though you're watching the edited, final polished cut of me here on YouTube.
`[11:31]` 30 minutes to get to the rough cut where GPT-6 Astra says it's done.
`[11:35]` All The full length source timeline is preserved.
`[11:38]` Markers, flag, missing Clawcast inserts and everything else needed.
`[11:42]` Okay, the moment of truth.
`[11:45]` let's play it back and check those edits.
`[11:47]` Let's dive in.
`[11:48]` Okay, I'm going to use this open claw.
`[11:51]` Little bit slow, but you know what?
`[11:52]` I would accept that edit.
`[11:54]` That would pass.
`[11:54]` I wouldn't need to retrim that.
`[11:56]` It's even.
`[11:57]` Look at this.
`[11:58]` This is insane.
`[11:58]` It's actually gone ahead and put audio dipping on the audio track.
`[12:02]` Look at that.
`[12:03]` To make the edit nice and silky smooth.
`[12:06]` I'm not even going to touch that.
`[12:07]` I could as an OCD video editor, but I won't.
`[12:10]` Let's check the next edit here.
`[12:12]` The first time.
`[12:13]` Well, if you're not.
`[12:14]` That is perfect.
`[12:15]` That is 100% perfect.
`[12:18]` All right, let's look at this edit now.
`[12:20]` Since on Hostinger one click deploy is yes.
`[12:23]` Oh my goodness.
`[12:24]` Guys, we're an AGI for video editing and audio editing.
`[12:28]` May I say, as someone who's taught audio editing for like nearly two decades
`[12:32]` on YouTube, that's done.
`[12:34]` If you want to see my other channel, that's an archive of how we humans Used
`[12:38]` to do that stuff.
`[12:40]` Couple more edits to see where we're at what you want either way when you choose
`[12:44]` a plan.
`[12:44]` Nice.
`[12:45]` So it chose to use my screen share there for readability and then cut back to
`[12:49]` me with picture in picture at this point.
`[12:51]` Now this is interesting.
`[12:53]` As I look along this timeline there's quite a, a big pause here.
`[12:56]` So I'm concerned by this KVM2 here you can type in.
`[13:00]` Okay, that is a little bit of silence there.
`[13:03]` That would be a little bit too long.
`[13:05]` So that's at this particular timestamp here.
`[13:09]` So I might go back to chat GPT-6 Astra and see if it can make that one edit for
`[13:14]` me.
`[13:15]` I'll just say there is a long silence at 1:20:11.
`[13:17]` Please fix only this and we'll see if GPT-6 Astra can make just that one little
`[13:22]` edit there and tighten this bit up.
`[13:25]` It's actually inspecting right now.
`[13:26]` Keeping tracks aligned.
`[13:28]` Of course, that's what we want.
`[13:30]` you can see there's a two second pause between you and type in my coupon code.
`[13:34]` So it's going to shorten that.
`[13:35]` Now again hands off.
`[13:37]` And there we go.
`[13:38]` It's done I think.
`[13:40]` Fantastic.
`[13:41]` Let's see if we can play back that section and listen again.
`[13:44]` Here we go.
`[13:45]` You can type in my.
`[13:46]` Yeah, that's acceptable.
`[13:47]` That's okay.
`[13:48]` Now full disclosure there.
`[13:50]` That took nearly two minutes for Codex to do using the DaVinci Resolve MCP.
`[13:55]` Two minutes to make a two second trim is not acceptable.
`[13:59]` It did remove 1.67 seconds and kept all other tracks aligned which is great.
`[14:04]` That's good but it's not perfect.
`[14:06]` If I hit command Z here, look, we get the trims back.
`[14:09]` Everything can be undone with the command Z.
`[14:12]` of course what took two minutes here can easily be done by doing shift delete.
`[14:17]` That took like one second.
`[14:19]` So in some cases yes.
`[14:20]` Getting the rough cut and doing the high level edits.
`[14:23]` Brilliant.
`[14:24]` Making fine grained changes and QA kind of things that Human in the loop would
`[14:28]` catch.
`[14:29]` You probably still want to be doing that as a human, unless you've got loads
`[14:33]` of coffee and you just want to go off and drink it while the agent makes its
`[14:36]` small little edits.
`[14:37]` So this is fun and it's a great thing that can save me a lot of time, but can
`[14:41]` it do the polish?
`[14:43]` Okay, now you've done the rough cut, I'm happy with it.
`[14:47]` I wonder if you can insert an overlay at the start of the video, introducing
`[14:52]` me as Mike Russell from Creator Magic.
`[14:55]` Now I'm just doing one simple thing and it's got no house guide on how I do my
`[14:58]` overlays.
`[14:59]` So it's going to make it all up.
`[15:00]` But I'm wondering if.
`[15:02]` Look, it says it can do this with Resolve's MCP if it could do this.
`[15:06]` Obviously if I was making a full video I'd put loads more overlays and B rolls
`[15:10]` and cutaways.
`[15:11]` But this is just one test.
`[15:13]` Let's roll back to the start and zoom in here and watch it happen in real time.
`[15:17]` Okay, it says I'm making a 5 second lower third with soft fade white name text
`[15:21]` and small teal accent.
`[15:22]` It will sit on an overlay track.
`[15:24]` Nice.
`[15:25]` Okay, look at that.
`[15:26]` It made it.
`[15:27]` It has taken nearly three minutes of working here, but it did make it a nice
`[15:31]` lower third here that I assume it's going to insert on the the timeline.
`[15:35]` Okay, there we go.
`[15:36]` Yes.
`[15:37]` It's done. Look at that.
`[15:38]` Wow, that's amazing.
`[15:39]` Let's rewind and play back.
`[15:40]` OpenClaw 2.0 is here with 16,000 pull requests.
`[15:44]` Yeah.
`[15:45]` About half of everything in the project.
`[15:46]` Okay, nice.
`[15:47]` Fade in, fade out for the lower third.
`[15:49]` That is done.
`[15:50]` It's just wrapping Up.
`[15:51]` It's doing QA here.
`[15:52]` Again, looking at the image to check and it says yes, I've added the five second
`[15:56]` lower third.
`[15:57]` Mike Russell creator Magic Till Accent.
`[15:59]` Obviously no style guide here.
`[16:01]` I did not give it any style guide but the fact it's gone ahead and done that
`[16:04]` is pretty insane.
`[16:06]` So I'm pretty happy that pretty much anything related to video editing can now
`[16:10]` be done in DaVinci resolve.
`[16:12]` Definitely we can get the rough cut, we can get lower thirds and overlays.
`[16:15]` I'm sure we could probably get B roll in there as.
`[16:18]` I'm really happy with this rough cut.
`[16:20]` It's basically ready to go to YouTube.
`[16:22]` There are only a couple more things I'd like you to do.
`[16:24]` First of all, I'd like you to color grade the video like a boss.
`[16:27]` You're the world class expert in it, so do it for me.
`[16:29]` And then I'd like you to make sure the loudness is absolutely correct for upload
`[16:34]` to YouTube.
`[16:35]` Ensure those two things and then tell me if it's ready to render and if you're
`[16:39]` able to render it yourself, let me know.
`[16:42]` Don't render yet, but just tell me if you can.
`[16:44]` Now this is the one thing that no one tells you when they're playing with video
`[16:47]` editing.
`[16:48]` First of all, video editing takes a lot of tokens.
`[16:51]` My context is now compacting.
`[16:53]` And the other thing is, well, all those
`[16:55]` slick demos you see on x and other YouTubers
`[16:58]` doing that are edited tightly and full disclaimer.
`[17:01]` I'm editing this video with AI by the way.
`[17:05]` and they show you that it happens
`[17:06]` in seconds or minutes, which it really doesn't.
`[17:09]` I've been sitting here the best part of an hour running this DaVinci Resolve
`[17:13]` MCP
`[17:14]` via Codex using GPT-6 Astra.
`[17:17]` Can it do all this stuff?
`[17:18]` Yes.
`[17:19]` Can it do it fast?
`[17:21]` It's getting better all the time, let's say.
`[17:23]` But you know, right now I've been sitting here for three minutes watching context
`[17:27]` automatically compacting.
`[17:29]` Okay, after four minutes we've done the compaction.
`[17:32]` Now let's get into action.
`[17:34]` Okay, it's already working like a pro.
`[17:35]` Keeping the grade restrained so skin looks better without distorting software
`[17:39]` interface.
`[17:40]` I Love your thinking GPT-6 Astra.
`[17:42]` Let's see what it does.
`[17:43]` So at the moment you'll see my face and the background pretty washed out.
`[17:47]` I'm hoping that it makes some changes.
`[17:49]` It's also checking Resolve's YouTube
`[17:51]` loudness controls against the whole program.
`[17:53]` Okay, what I notice is a lot of Python files getting created here, so it doesn't
`[17:57]` seem fully like it's doing everything via the mcp.
`[18:00]` A lot of stuff is Codex writing code and analyzing stuff before getting back
`[18:05]` to Resolve via the mcp.
`[18:07]` We've got images here of me.
`[18:08]` That's qa.
`[18:10]` Okay, again through the MCP client making some changes here and we can see.
`[18:14]` Yes, render settings are being locked in over here on the left with a preset
`[18:18]` it has created.
`[18:19]` Creator Magic YouTube 4K review.
`[18:21]` Now I didn't create that preset.
`[18:24]` It seems that Codex is doing that for me.
`[18:26]` it's backed up the approved edit.
`[18:27]` It's lifting the tone slightly to stop my excess orange skin
`[18:33]` and keep the purple studio lighting very nice.
`[18:35]` Audio analysis is running across the program.
`[18:38]` Cut some fades.
`[18:39]` No video render started yet.
`[18:41]` Okay, audio is already in good shape.
`[18:43]` We're at 14.69 LUFS with a 1.04 decibels true peak which I can confirm is
`[18:49]` absolutely correct.
`[18:50]` So this is really, really good.
`[18:52]` Just so you know, on color grade and audio, it's been working over 12 minutes
`[18:56]` now and it's still not quite done.
`[18:58]` Okay, look at this.
`[18:59]` The grade is applied.
`[19:00]` Opening title looks clean.
`[19:02]` Checking the saved export settings now.
`[19:04]` Okay, this is looking really good.
`[19:06]` One thing I will say is I don't see much change in terms of color grade here.
`[19:11]` It looks pretty much like what we started with, but hopefully the audio will
`[19:15]` be better.
`[19:16]` And so you know, this last step is chewing time 15 minutes and we're still not
`[19:21]` done.
`[19:22]` Oh, here we go.
`[19:22]` We're done.
`[19:23]` That's it.
`[19:24]` Just as I said that the grade is applied and saved.
`[19:27]` Brighter, more natural skin tones.
`[19:29]` Do I can't see much difference.
`[19:30]` But maybe it did make a difference.
`[19:32]` Audio is correct, technically.
`[19:34]` Ready to render.
`[19:35]` Obviously missing the inserts, which is fine.
`[19:38]` I can render it through Resolve's mcp.
`[19:40]` So let's try this render, it.
`[19:43]` And this is the final step now, the final piece in the pudding.
`[19:47]` And I can tell you as I type that command in, we're bang on an hour.
`[19:50]` So let's see.
`[19:51]` I'll render the graded timeline using the Prepared 4K YouTube preset, then check
`[19:56]` the Xbox exported file.
`[19:57]` Hopefully rendering should be pretty quick.
`[19:59]` And then we can guarantee we can work end to end in DaVinci resolve using only
`[20:05]` an AI agent.
`[20:06]` And there we go.
`[20:07]` Yeah, it's going into the render and it has indeed popped something into the
`[20:10]` render queue here.
`[20:11]` This is amazing.
`[20:12]` This is actually happening in real time.
`[20:14]` Right now it's rendering my video.
`[20:16]` So that guarantees the whole process can be automated end to end using your
`[20:22]` coding agent of choice, in my case, GPT-6 Astra on high mode along with the DaVinci
`[20:28]` Resolve MCP that was just released today in version 21.1.
`[20:33]` This is pretty insane.
`[20:34]` The 4K render is running and I'm saving it as OpenClaw 2 point zero Creator Magic
`[20:39]` MP4 in your video editing folder.
`[20:42]` Okay, this is very nice stuff and we are definitely pretty much there with video
`[20:47]` editing.
`[20:48]` Yes, it can be done and automated by AI is working in DaVinci Resolve.
`[20:52]` Great.
`[20:53]` Well, yes, because I don't need to know the software, I don't need to touch a
`[20:56]` button.
`[20:57]` This can all be automated by AI.
`[20:59]` Now, I'm an Adobe user and a premier user for years and years and yes, Adobe,
`[21:04]` I would like to see you do the same thing.
`[21:06]` Not have a proprietary lockdown AI assistant that lives in and is controlled
`[21:11]` by Adobe inside Premiere.
`[21:13]` I want to be able to choose Codex or my Claude subscription to edit my videos.
`[21:18]` I want to bring in skills to make lower thirds and overlays.
`[21:21]` I want to bring in other skills to make AI B roll.
`[21:24]` And until someone completely automates that, I'm not calling AI.
`[21:28]` Video editing done yet.
`[21:30]` Now let me explain to you a little bit about my video editing process.
`[21:34]` I am looking for the Linux of video editing.
`[21:37]` I don't want to be locked in or locked down.
`[21:39]` I want complete freedom and sovereignty over the kind of edits that I do.
`[21:45]` And up until a long time and still to this day, even the video right now that
`[21:49]` you're watching, it's edited in a buzz channel and I'm automating that using
`[21:54]` Claude code on Fable 5.1.
`[21:56]` It does the edits and then previously I was eyeballing them by pulling a timeline
`[22:01]` into DaVinci resolve.
`[22:02]` I would love to do the same thing in Premiere, but it doesn't support timeline
`[22:06]` imports that my agent can make, which is a bit of a bummer.
`[22:10]` for the eyeball, I'm not even sure if I need to use DaVinci Resolve or Premiere.
`[22:14]` Maybe I can just use another open app that there's lots of them out there.
`[22:18]` ChatCut is a big one and it's gaining in popularity.
`[22:21]` I've been messing around with Diffusion Studio, which seems to cut out the bloat
`[22:26]` that Resolve and Premiere suffer with.
`[22:28]` So the jury is still out on how this process will look.
`[22:31]` But in my opinion, the absolute meat, the brains, lie in how you automate this
`[22:37]` with your AI agent, the skills you create and how you tell your agent to edit.
`[22:42]` That's where the mote is.
`[22:43]` It's not about doing the edit or what software you use to QA or eyeball.
`[22:48]` That's basically solved and we could just use a simple video editor in the browser
`[22:54]` to check that stuff out.
`[22:55]` We don't need these big editing programs anymore.
`[22:58]` Blackmagic and DaVinci Resolve have certainly laid down the gauntlet here by
`[23:02]` making a Resolve MCP available.
`[23:05]` have been recording this RAW video for about an hour.
`[23:08]` I'm about to hand this ProRes that's recorded
`[23:10]` on my Mac Studio off to my AI agents
`[23:13]` that will edit and publish the video that you're watching right now.
`[23:16]` Let me know your thoughts.
`[23:17]` Has this been solved in your opinion, would you use this workflow?
`[23:21]` What do you want to see?
`[23:22]` What are the missing pieces?
`[23:24]` What did I not mention that I should have?
`[23:26]` Let me know in the comments down below.
`[23:28]` I'm thoroughly engaged in this topic right now.
`[23:31]` I want to see this succeed and I want video editing, overlays, aib, roll, all
`[23:36]` of that.
`[23:37]` I want it solved for creators so that literally my job is to come up with the
`[23:41]` ideas in collaboration with AI.
`[23:43]` Hit record in my studio, stop the recording
`[23:47]` and that's where I finish as a content
`[23:49]` creator.
`[23:50]` When I hit stop on the recording button, my AI agents in an ideal world should
`[23:55]` take over, publish and have it ready for you to watch on YouTube.
`[23:59]` Hopefully that's coming soon.
`[24:00]` Thank you so much for watching and YouTube is showing a video on your screen
`[24:04]` right now that's been determined by the algorithm to be absolutely perfect for
`[24:08]` you.
`[24:09]` So you should probably pay attention and you should watch it next.
`[24:12]` Thanks.
