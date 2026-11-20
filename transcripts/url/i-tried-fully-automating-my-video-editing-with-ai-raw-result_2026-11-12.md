# I Tried Fully Automating My Video Editing With AI (RAW RESULTS)

- **Source:** https://www.youtube.com/watch?v=C0jOKDJtK9s
- **Uploader:** Ali Abdaal
- **Uploaded:** 2026-10-26
- **Duration:** 46:33
- **Detected language:** en (p=1.00)
- **Model:** small.en

## Transcript

Oh my god, Opus 5.5 is incredible at making launch videos. Look at this one shot. How far can I go trying this sort of AI editing compared to our human video editor, who is very good? If this works, I will be absolutely amazed. That is really good. Oh no, oh no. I'm worried for video editors. We've got amazing video editors on my team. So every time a new AI model comes out, my Twitter feed fills up with people saying that this one can now edit videos. And I've been seeing that with basically every model released for the last few months, and so I was a little bit skeptical. Now for context, I edited my own videos for about three years back when I was working as a doctor for somewhere between 10 and 40 hours a week. And so I kind of know what a good edit feels like, but I'd never actually sat down and properly tried editing with AI. But then a public holiday came around and the team mostly had the day off and we needed a launch video for Creator Grade, one of our platforms. Path, one of our editors was already doing it the normal way. And so I decided to challenge myself for the day. Could I, as someone who's never tried AI video editing, learn how to use AI for video editing and make a video that comes as close as possible to a world-class human editor. And to be honest, if AI could get me like 80% of the way there, I would be delighted. This video is a little bit experimental. Usually I tell you about stuff that I already know, but in this video, I'm taking something that I don't have any idea about. And so if you want, you can watch the process of how I'm sort of learning it and figuring it out. And hopefully there'll be something that you can take away from this to apply to your own workflows for learning things or for applying AI. This is going to be a super long video, so there'll be timestamps down below, feel free to skip around if you like. But now before touching anything, I try to work out what video editing actually is because that's how we're going to figure out how to break it down using AI. What is video editing at its core? Okay. So if we think of when you've already got some footage compared to when you don't, when you've already got some footage, what is video editing? Well, firstly, you import the footage and then you need to basically cut out all the mistakes to get a clean A cut. Then once you've got a clean A cut, you then add in B roll. It would be like the screen recordings and the screenshots and stuff. Then the hard part, the bit that takes ages is animating the B roll so that you've got like zoom ins and zoom outs instead of just showing a screenshot, which would be boring. These launch videos often go in and out, and then there's motions and transitions and fade ins and movements and swipes and pans and all those things. So that takes a human video editor ages to do. Once you've done that, then it's like background music and sound design. So the background music, you know, we've got a particular vibe, but then sound effects like risers and swipes and swishes and all that kind of stuff. That is ultimately what video editing comes down to. And then obviously the taste factor is telling a good story and deciding what to cut out, deciding what to keep in. I feel like once we break it down into all those things these days, surely the AI should be pretty good at all that stuff. To be honest, I would be very amazed if it manages to just even get the A cut right immediately, right? Because when I as a human am editing a video, if there is a pause or there's a retake, you have to know where to cut and splice the footage together so that it doesn't sound weird. You know, we had a whole lesson in my course where I taught people how to use Final Cut Pro. There was a lot of time spent on just like nailing the A cut, because if you can nail the A cut, then everything becomes smoother further down the line. But if the A cut sucks, then everything else will kind of feel a bit disjointed. The stuff I've seen on Twitter is like super, super, super polished. They're like, oh my God, Opus 5.5 is incredible at making launch videos. Look at this one shot. And I'm like, there's no way that was actually one shot. Surely you had to go back and forth quite a lot and do a lot of tinkering to get that particular result. So I'm going to be very interested to see what does the one shot look like where I'm just, I'm not really driving it. I'm just like giving it copied and pasted stuff from Grok into Claude Code and then Claude Code into Claude Code, just like raw dog and just see what it does. And then when I've dabbled with AI stuff just for anything in the past, getting it to like 80% good enough happens with one shot. But then polishing that final 20% takes frickin ages. And the bulk of the time is spent in polishing it. So it feels good and looks good and has taste applied to it rather than just the one shot version. All right, so phase one of this project is I want to start by getting a lay of the land. What options do we even have for AI video editing? So I'm just going to use Grok because I don't need a VPN for it. I'm trying to figure out how to do AI video editing. I've got some footage. I need to turn into a launch video for Creator Grid, that form that helps it just learn, grow and monetize. I want to see if I can use AI video editing to make a alternative edit, ideally the whole thing. But also we could do a 30 to 60 second faceless launch creator type thing using motion graphics and stuff. Or we could do it like talking head with screen shots, like a YouTube video, some combo of all of the above. Help me figure this out. Three different pipelines. So one option is the DaVinci thing with an API. OK, D script for the cut and then resolve for grade graphics and finish. OK, option three, this is the remotion hyper frames lane, faceless brand launch trailers. Cool. Not entirely sure what any of this means just yet, but I think we have a reasonable lay of land. All right, so quick translation because there was a lot of jargon over there. There are basically two ways AI can make you a video right now. The first one is to edit the footage that you've actually filmed. For that, I used DaVinci Resolve, which is a proper professional video editor that recently started letting AI control it directly. But then the second is to not edit footage at all. You instead get the AI to write the video as code and it generates every single frame. That's what tools called hyper frames and remotion do. And it's how a lot of those launch videos that you might have seen on YouTube and Twitter are being made. I didn't know which approach would work. And so I decided to try both of them at the same time. Oh, what a vibe right as of literally right now. Path, one of our human video editors, has actually just sent me the first draft of this video that he was manually editing. So I don't want to watch it right now, but that could be interesting to compare. How far can I go with trying this sort of AI editing stuff for the first time compared to our human video editor, who is very good? OK, also, I've got a role filmed already. How do we get started? OK, firstly, Hagen hyper frames, core skills. Experiment B, a roll cut resolve. MCP needs DaVinci Resolve Studio 21.1, 295. All right, guess I'm paying $295 for DaVinci Resolve Studio. We are buying DaVinci Resolve Studio. All righty, it worked. We have just bought DaVinci Resolve Studio for about $300. And it is an 8.5 gigabyte file. So it is downloading. All right. Now I need to Claude plug and marketplace Hagen hyper frames. Install Hagen hyper frames. Let's open up Claude code. So what I want to do is let's go local. Let's make a new folder creator grid launch video or something. And let's open 5.5. OK, I'm trying to use hyper frames to make a launch video for a creator grid. I've already had some a roll that we don't necessarily need to use it. Here are some preferred notes from Grock. Let's see what Claude does. OK, we are installing hyper frame skills into the project. All right. So I've already got that footage. Let's chuck it into the project folder. Oh, and by the way, I've added in the existing video into the project folder FYI. Ah, OK, Claude Khododoski. FFmpeg isn't installed. Yes, by all means, please do. Yes, install FFmpeg. Happy for you to install it globally on this machine. Pablo, our co-founder, has put together this Claude artifact with product views we can use. I want to see what a pure faceless, just music. No voice video looks like. But also, I want to see what it looks like with just my voice as a voiceover and also what it looks like with both my voice and face, because I think my face and voice carries trust to some degree. Let's do a pipeline test first. It's doing stuff. Installing FFmpeg and Whisper CPP. I know what both of those things mean, so I don't need to ask. But if I didn't, I would totally ask. The screenshots are good. Real UI at 4K, setting up Hyperframes project and running the 10 second pipeline test. Great. It's just doing stuff. Oh, quick note from the sponsor of this video, which is Whisperflow. Now, on a good day, I can type at about 156 words per minute. But even with that insane typing speed, I can still speak faster than I can type. And so Whisperflow is a wonderful tool for turning your voice into text in pretty much any app you might be using. So, for example, I'm going to try this right now in Slack. Hey, Angus, we've got three things for Austin. Firstly, can we book the flights by Friday? I don't know, Thursday, actually. And make sure everyone's landing the evening before. Second, can you please send everyone the agenda with the planning sessions in the morning and the afternoons left free? And then thirdly, can we sort out a group dinner place for the first night, ideally somewhere that we can all fit in one table? Cool. Thank you so much. OK, so that took me under 30 seconds. And if you look at what's come out, it's turned my spiel into a very nice numbered list that makes it very easy for the person to see what I'm talking about. I made a mistake on saying Friday, no wait Thursday. And it took that into account. Now, people always say that, yeah, but my phone's got built in dictation, to which I would say, have you seen how bad the built in dictation on your phone is? Let's just try it out. Hey, Teemu, are you around for a call on Saturday? No, wait, Sunday. And can you send me the name of that book that you mentioned? So, yeah, it doesn't know how to spell my brother's name. It doesn't clock the mistake. And now if we try exactly the same thing in WhisperFlow. Hey, Teemu, are you around for a call on Saturday? No, wait, Sunday. And can you send me the name of that book you mentioned? Great. And it even knows that this is exactly how I spell my brother's nickname, his name is Teemu, and I call him Teem, and it knows exactly how to spell it. And it's automatically taken the error into account and removed it from the text, which is awesome. In my case, I've currently written 167,630 words on WhisperFlow so far, which is a fun little stat to see. Anyway, WhisperFlow is free to use, and if you wanna use it absolutely loads, then you can get WhisperFlow Pro that gives you unlimited words, and you can get a month of WhisperFlow Pro completely free by checking out the link in the video description. And when they ask you how you heard about them, please do write YouTube and put my name in the how did you hear about us box, because then they're more likely to sponsor more of our videos, which is awesome. So thank you, WhisperFlow, for sponsoring this video, and let's get back to it. Okay, awesome. Have we downloaded DaVinci Resolve yet? Yes, we have. Let's install this. I've literally never worked with DaVinci Resolve, but how hard can it be? Okay, classic. You look at a video editor and it looks intimidating AF. What do I do here? Help. AI? Set up AI assistance. All right, let's do that. DaVinci has been added to these. Please restart. Oh, wow, okay, cool. It's already done. So Cloud Desktop. Extension installer opened. DaVinci Resolve Studio. Extension. Okay then, install. Let's go. Oh, that was quick. Let's see, what's Cloud Code saying? No, still doing stuff. It's using some tokens. 3% obsession limit. All right, we've got plenty of headroom here. So what the hell do I do next on DaVinci? I mean, in theory, it should be connected to Cloud Code, right? So I could just, do you see the DaVinci Resolve connection? MCP, I think. Let's see what happens. Yes, wow. We're about half an hour in. So far, we've managed to buy and download DaVinci Resolve Studio and Cloud Code is cooking away on trying to do the hyperframes method. By the way, can you write me a brief? I can put in another Cloud Code chat within this project to test out DaVinci Resolve MCP for building this video as an alternative method. Nice. All right, well, Cloud Code is basically telling me what to copy and paste into Cloud Code. Boom. I love a good old copy paste from AI into itself. Oh, wow, okay. Cool. Storyboards are written, no animation code yet in your bands, gradients, glow-ins, fade-in, blah, blah, blah. Film A, music and text, 30 seconds. This is its own edit. With no voice, the type and the product shots have to tell the whole story. Okay, yep. Film B, your voice, 45 seconds with a 70 second extended cut, build it once, render it twice, voice only, and then with your face added. Film A silent has three options. Okay, let's look at that. Oh, okay, it's fun. All right, let's just ask these. One, demo data. Two, yes, we can show client logos. Three, that's okay. Four, is there a logo file? Get logo from creator-grid.io. Yes, static, no animation. Still render to prove the setup works, please. Pick an A option and the B length. Okay, so B length, 45 seconds, feels good. And A, you do two things, we do everything else. All right, creator marketing with other Ks. Nice, I quite like that. That's pretty good. A one option I like. Let's go. Hey, this is so good. Okay, now let's see what Resolve's doing. Creating work folders, find whisper models, probe source view live output, Resolve scripting API. All right, it's just doing stuff. I guess maybe I won't even need to use. It's not visibly doing anything, but I guess it's doing stuff in Cloud Code with the DaVinci Resolve connector. If this works, I will be absolutely amazed. There's no way it's gonna work first time. There's just no way. But this is quite cool. It's such a vibe, isn't it? Oh, open and split view. Oh, wow. This is really cool. So at this point, we've got stuff happening basically side by side. So on this side of the screen, we've got the DaVinci Resolve method of trying to do AI video editing. On this side of the screen, we have the code hyperframes method of doing AI video editing. And I'm just sort of sitting back and waiting for it to do stuff, which feels pretty good. Yeah, this iMacs fans are starting to get pretty, you know, this is hot. Everything's hot. If this really works, I might just upgrade to an M5 Mac Studio. Oh, wow, look at that. That is actually not bad. Creator marketing without the chaos. That actually looks pretty fricking solid. That looks pretty good. I mean, as anyone can generate a still these days, but that's, you know, remains to be seen how good this is for video editing. Let's see what happens next. All right, both storyboards are sketched. No animation code has been written yet. Okay, cool. Let's look at these storyboards. This is actually remarkably good. Creator marketing without the chaos. I don't like this font, but I think this is our font. Is that our font? Okay, I might have to redesign the creative grid branding if we do use that font. I'll get to the style later. Pick your creators, prove the content. We handle the sourcing, negotiating, time briefing, reviewing, invoicing, paying, tracking, everything else. Nice. Okay, so far I'm quite impressed by this storyboard. I wonder if I should use storyboards more when doing stuff. What's happening on DaVinci side? Okay, it's still doing stuff. Okay, so DaVinci has been cooking for 20 minutes and this just seems to be running into a bunch of issues. I probably should have done this one at a time, but you know what, let's just see. Let's just see what it's gonna do. One shot. You know, one of the things with working with AI is figuring out what to do while it's thinking. I could try and do a third thing. Why not? And by the way, I want to try using remotion as a third experiment running concurrently with hyperframes and resolve. Write a brief that I can give to a new cloud code instance within this project for this. So we've got hyperframes number one, we've got resolve is method number two, and we've got remotion, which is method number three. So we now have hyperframes over here, resolve in the middle and then remotion over here. Okay, all three drafts are rendered. We have MP4 files. All right, let's see, what does this look like? And is it any good? Eh, okay, well, that's pretty bad as a faceless version. Let's try DraftV2 voice no face. Let's see what happens. If you're a brand trying to grow with creator marketing, you probably know that it is a total nightmare. If that resonates, I would love to tell you about Creator Grid, where we will literally run your creator campaigns for you end to end. You don't pay anything upfront. There is no retainer, there's no subscription, and you only pay for results, entrepreneur and creator. If we haven't met, hello, man. What the hell? It's Ali, I'm a doctor turned entrepreneur and creator with about eight million. Creator Grid is our attempt to basically give you the level of service. Oh no, oh no, it didn't, it screwed up the A-cut. Just the basic A-cut, it just doesn't get it. I knew it, I knew it, the pauses, the pauses, the pauses are bad. It's not doing the A-cut properly. And now what if we have my face in it as well? What does that look like? If you're a brand trying to grow with creator marketing, you probably know that it is a total nightmare. If that resonates, I would love to tell you about Creator Grid, where we will literally run your creator campaigns for you end to end. You don't pay anything upfront. There is no retainer, there's no subscription, and you only pay for results, entrepreneur and creator. If we haven't met, hello, my name is Ali. Oh, this isn't bad. But this would have been magical a few years ago. Whoa, you could just do that with just getting a robot to operate DaVinci Resolve, but I had way higher hopes of the V1. Okay, hopefully Hyperframes does a better job with this. So I think what I may have to do is I might have to actually manually decide what to keep in in terms of what I've said, or maybe even record a separate video that's explicitly word for word, scripted 45 seconds long, because this one was more like five minutes long and it's just tried to figure out which bits to, this is frustrating, I do not like this. Let's grab something from Epidemic Sound. I wanna find a track that people wouldn't recognize. Oh, beautiful, right. Okay, so we're using Vivaldi's Spring as the background music for the Hyperframes one. Okay, still, we've got Hyperframes doing stuff, we've got Resolve doing stuff, and now we've got Remotion that's been doing stuff for the last 23 minutes. Also, one thing that I didn't really do is I could have, like I've been seeing stuff on Twitter recently about that where people have come up with these like elaborate prompts for Hyperframes. So maybe I could have just copy pasted one of those just to see what that would do, but we're not gonna get ahead of ourselves. We're just gonna try and focus on the simple stuff. We have a silent draft of the Hyperframes video. Shall we see what this looks like? Okay, it's not bad. The classical music makes it kind of funny. It's a little bit janky. It's the equivalent of if I were like 15 years old and learning video editing for the first time and deciding to use Vivaldi's Spring as the background music. It's impressive as a V1, but of course we need refinements to make it actually good. Okay, I'm gonna go for lunch. We're gonna come back, and my prediction is that I will be disappointed with the one-shot results of this, and then we will start the actual work of doing anything with AI, which is polishing. All righty, ladies and gentlemen, we are back after our lunch break, and it is time to see what is happening. So we're gonna start with the Hyperframes one. So we saw the silent one a little bit earlier. Let's try voice and no face. If you're a brand trying to grow with creator marketing, you probably know that it is a total nightmare. I would love to tell you about Creator Grid, where we will literally run your creator campaigns for you end-to-end. All you have to do is basically two things. So firstly, you decide which creators you wanna work with, so we'll source them for you. You just sort of approve or reject them. We will give you a bunch of content, and you just decide to approve it or not. Everything else is handled by us, so the sourcing of creators, negotiating, reviewing the content initially, and then invoicing and paying the creators, tracking all the views, lines, all of that annoying stuff, we take off with your plate. Oh, wow, okay. That's like remarkably impressive. That's way better than the DaVinci Resolve one. That's really well done. Let's see what this looks like with my face as well. If you're a brand trying to grow with creator marketing, you probably know that it is a total nightmare. I would love to tell you about Creator Grid, where we will literally run your creator campaigns for you end-to-end. All you have to do is basically two things. So firstly, you decide which creators you wanna work with, so we'll source them for you, and you just sort of approve or reject them. We will give you a bunch of content, and you just decide to approve it or not. Everything else is handled by us, so the sourcing of creators, negotiating, reviewing the content initially, and then invoicing and paying the creators, tracking all the views, lines, all of that annoying stuff, we take off with your plate. Wow, okay. That is very good. I mean, obviously, it could do with a lot of work, but that is remarkably impressive. I did not think it would be that good. Let's see how Remotion does it. Whoa! Remotion has literally given me a video editor interface. What the hell? I didn't realize I could do that. That's cool. Okay, let's see what this version looks like. If you're a brand trying to grow with creator marketing, you probably know that it is a total nightmare. If that resonates, I would love to tell- Hang on, let's try the voice face one. If you're a brand trying to grow with creator marketing, you probably know that it is a total nightmare. If that resonates, I would love to tell you about Creator Grid, where we will literally run your creator campaigns for you end to end. You don't pay anything up front. There is no retainer, there's no subscription, and you only pay for results. Oh, oh, okay. We need a bit of quality control on this one. I don't know why it's bugging out. Like, it looks- Pains for brands like Notion, Whisper Flow, Todoist, Superhuman, Victor, and a bunch of others. I see what they're trying to do, but this is just like super, super, super buggy. Like, what the hell is it doing? How the hell did you create a video editor within the browser itself? I didn't build that. The browser is Remotion Studio, which comes free with Remotion. It's a small local web app. Interesting. Okay, so Remotion Studio is probably the most, like, similar to a video editing experience, but, like, it was a bit buggy. Just not as good as the one that Hyperframes made. But Hyperframes doesn't have, like, the video editing interface. It's purely the code. And the one in DaVinci Resolve just was not very good at all. So at this point, I would rate Hyperframes as being, like, probably a seven out of 10. DaVinci Resolve, I would rate it being probably a three out of 10. And Remotion was super buggy, so I'd probably give it a two out of 10 right now. But it does have the right idea. It does have the right idea. Here is the problem, I think. We think about, like, the two versions of the video. If we imagine a role is what being said that needs to be a cut, so we go for a raw A-roll. What this kind of needs is a script. To raw A-roll, then you get the A-cut, and then you get the add-in effects. What I was trying to get Resolve to do is basically take 10 gigabytes worth of A-roll footage and hope that it would, A, magically be able to 45 seconds of that to turn into a cut, but then also to actually be able to edit an A-cut using J-cuts and L-cuts to the level that I would like. Now, that is probably a little bit unfair, and it's a little bit beyond what Opus 5.5 can do at this stage. Maybe one day you'll be able to just give it a bunch of footage and say, edit this for me, but today is not that day. So we are going to have to, at least on the Resolve front, drill down and start doing things a little bit manually, by which I mean kind of breaking things down a little bit more step by step. Maybe that's the way to think about AI editing with Resolve. Prove the concept first for 30 seconds. You know, and okay, this was dumb of me to not realize beforehand. In fairness, it's always good to just one-shot and see what happened, because then you see the holes in your prompting. Because if we were hiring a human video editor and I were testing out a brand new video editor, the way we do that is we give them 10 minutes of footage and we ask them to just give us the first 60 seconds as an edit because it gives us a feel for how are they doing. It would be unfair to ask a human video editor to say, hey, of these 10 minutes, pick the best 45 seconds and turn it into a cohesive story. And then let's see the editing because it would be a lot for a human video editor who's good at video editing, but maybe not good at scripting. Maybe actually the thing that I recorded is not suitable to be spliced into a 45-second chunk. Yeah, I don't wanna be one of those people that tries to one-shot something, gets a slightly s*** once and then thinks AI sucks. Like, I knew it. I knew it was using too much data. I knew the data centers were evil, et cetera, et cetera. It's like, no, I'm sure that there's definitely a way to do this. I just need to be a little bit more sophisticated with the process and make it happen. So my learning here, learning number one is, treat the AI like a human and give it the task that you would give to a human with the same level of instruction. Okay, I'm actually gonna switch out of Claude and go back into Grok. You know what, let me just do a Swiss workflow. So I think what's happening here is that we actually have two different work streams. One is a pure faceless launch video with like text and music and stuff. And so that is one that doesn't need the original footage, but then the second one is editing original footage. Those are actually two very different things. Editing original footage involves bringing in the footage, sorting out the A-cut, and then doing the B-roll and the animations and stuff. Whereas the pure faceless is just about doing really good animations. Now, I think what we can actually do, aha, is a hybrid of the two, hybrid. Because for example, if we figure out a system of nailing the editing of actual footage, like making the A-cut really good, and then separately we had an absolutely sick way of generating insanely high quality motion video that shows the screenshots of the app with all the relevant zooms and pans and all those things. Those are more similar to the ones that people post on Twitter. We can then combine the best of both worlds to create a talking head explainer video that also has all of the bells and whistles that like a purely animated launch video would have. Yes, treat them as two factories, and then a third step that only composites. Stream one, A-cut of real footage. Stream two, motion plates. Hyper frames when product screenshots, zooms, pans, connector type music hits, build each plate as it's own three to eight second composition against real UI. Drop hyper frames MP4 into the V3's B-roll talking head stays in V1. Okay, yeah, nice. Why are you calling them motion plates? Is that like industry terminology for this sort of thing? Oh, it's just a post-production word for a finished piece of motion graphics that you drop into a timeline. A plate is a self-contained visual layer. Oh, I had no idea. In old film work, it was a painted photograph background you composite piece people against. In this workflow, it's a short already rendered movie, three to eight seconds of zoom pans type in product UI that does not need to be built inside Resolve. Ah, most should just mean it's animated. You're not asking Resolve to animate the dashboard, you're asking to place a clip that already has the animation in it. That's clever. One thing I find when learning about AI stuff, or when trying to do AI stuff, is that I learn terminology that's actually used in the industry. So for example, the other day, I was doing some thumbnails for a thing, and I learned what a contact sheet is, which is basically like a series of thumbnails for a storyboard or something like that to explore different concept directions. And then because I then had that terminology, I was able to use that terminology in future prompts. I've never heard the phrase motion plate before, but this is exactly what I want. I want the a-cut of the video, the a-roll of me talking, and then I want really high quality motion plates to appear over the top based on what I'm saying in the video. Learning number two, learn the words that the professionals use. Because as soon as I knew it was called a motion plate, I could then ask the AI for exactly what I wanted. All right, this is exciting. I now have more of a mental model of what I'm trying to actually do here. Okay, so I'm gonna start with what I want is I'll give you a roll, a cut, I cleaned up a cut of the video of me talking. Ultimately, what I want is really nice motion plates that I can add to the a-cut using something like Resolve. All right, hyperframes can do this. Only the motion graphic shows with no blocks around it. PNG sequences with transparency, 4K output, amazing frame rate match to your footage. One of plate's project with each plate as its own file. That's just to do exactly the same one for remotion and see. Okay, I think I can basically get rid of worrying about Resolve, DaVinci Resolve for now, because I know that I don't need that for this stage of the process. I'm now realizing that I just need to create the motion plates, because then the script, the a-roll, the a-cut, that's like the easy part. I could always do it manually if I really wanted to, I could chuck it into Premiere and use Firecut if I really wanted to. The a-cut is the easy part, the hard part is what I now know is called the motion plates, which is cool. Ah, it's rendering a contact sheet, let's see. Okay, that's quite good, that's quite good. You pick the creators, that is all pretty good. Wow, I like this. The only thing I don't like about it is the sort of solid colors. Okay, I like this. I just don't like the solid colors of the backgrounds of the vertical video thumbnails. I want them to look more like actual UGC. So let's use real slash AI gen photorealistic images. Oh wow, that's pretty good. So it's using Canva to generate casual UGC style images to replace this stuff that looks a little bit fake. I mean, it all looks a bit fake, but I think that would sell the vision a little bit better. Learning number three, get the AI to show you the plan before it builds anything. If you have a storyboard or a contact sheet, that takes seconds to go through and fix stuff. But if you get it to one-shot the render all the way at the end, then like you have to spend a lot more time fixing stuff. All right, so Remotion has actually done a bunch of stuff. Let's see what it looks like. Inbox triage in 60 seconds, you approve the content. Yep, you pick the creators. Okay, that's really good. Your campaigns run end to end. That is remarkably good. Well done, Remotion. That's solid, look at that. Wow. Okay, I mean, we can definitely make a nicer graph, but this is really solid. Okay, I now like Remotion again. Let me just give it the same prompts as I did with this one. All right, this point is 3.45 PM. I have a couple of calls in about an hour, and so I wanna make as much progress as I possibly can in the next hour. I think we're getting there. Like the motion plates are actually getting surprisingly good. So I just need a properly scripted 45-second video, which I can then just record now. Get, I don't know, one of these tools to get the A-cut of it. Once I have a clean A-cut that I'm happy with, I can then overlay all of these different motion plates that we're creating, whether it's from Remotion or Hyperlapse. Okay, so at this point, I'm very happy with the images of what this stuff looks like. I think it's done a really solid job. This is the Hyperframes method. Let's see what it does when it animates it. All right, updated real, new views chart. Let's see what this looks like via Remotion. Nice, nice. Okay, well done, Remotion. Now at this point, the thing I'd finally clocked was that my original video was about five minutes long, and I'd basically been asking the AI to dig out a 45-second launch video out of five minutes of me talking, which is a job that I would never give to a human editor either. And so learning number four is that if you want a short video, film a short script. So I got Claude to write me a very tight script based on what it said in the original, and then I filmed it again. Let's get Claude to create the script for me because it knows exactly what I said previously and it's been doing all this stuff. In this project, we should have the transcript of the VSL I filmed for Creator Grid. Write me the V1 of the script. Okay, this is actually a very solid script. Let's now film the thing. If you're a brand doing creator marketing, you will know that it's a total nightmare. Okay, so we have just filmed the video, so now we need to export a clean A-cut of this video. How do I most expediently export a clean A-cut? You know what? Let's download Firecut for Resolve. I think Firecut for Resolve, somewhat ironically, is actually the tool that I'm gonna use for this. Firecut for DaVinci Resolve. I've never actually used Firecut myself. Our video editors use it, and we built it as an initial tool to use in-house for our team. Okay, so now I wanna do the first cut. Boom. Can I just generate the first cut? Let's see what happens. Nice. Okay, if you're a creator and you're paying a little bit, either you're paying agency, yep. I'm a total noob to Resolve, having literally never used it before in my life, but let's see. Let's see what happens. How do I zoom in and out? Okay, yeah, fine. If you're a brand doing creator marketing, you will know that it's a total nightmare. Either you pay an agency, a massive retainer, and wait, either you pay, ah. So Firecut has given me a very rough first cut, but it hasn't quite made it. You know what? Maybe this is just a case of me actually just doing this manually. How do I do cuts? On this thing. Command T. Laid tool. Boom. Ah, it's not a magnetic timeline, for goodness sake. Haven't done this sort of shit in absolutely ages, but this literally used to be my bread and butter in final cut. Produced every two years of my life. By us, our team, and our platform. So at this point, we have just exported a clean A cut. I probably could have done it with AI, but I didn't have the time to figure it out, so I don't know how long it'll take me. So now what I want is I want the transcription. So I'm gonna use this tool, Whisper Transcription, for that. Okay, we finally have a clean cut that I've just edited. This is the transcript. I want you to generate all the motion plates for this new transcript. Boom. And let's just do the same thing over here. So the A cut is done. In Resolve using fire cut and using a bit of manual editing. Now for the B roll. Motion plates are being done by hyper frames and by remotion. Sick. Then, background music. And I think then maybe the final thing might be to add in some sound design, actually, like plops and whooshes and stuff. Conveniently, epidemic sound has a bunch of that stuff in it. They've got swooshes, ambience, water, vehicles, whoosh. Can I just give the AI access to epidemic sound? Because that would be handy if it could find API keys. I love it when there's API keys. So I don't wanna do this, try and do this one shot. We're gonna see what it does with just the motion plates and then we'll add the background music and the sound effects. But I've got it ready so that we can save some time. Bonjour. Good. You are on the camera. Okay, now that we've actually done this, while we're waiting, we can actually check out path, what path said. Let's see. If you're a brand trying to grow with creator marks. That's really good. Oh, he gets it. Right. Marketing, you probably know that it is a total nightmare. Either you pay an agency, a massive retainer, and then you wait a few months to years for the content that may or may not be usable, or you and your team is trying to like manually reach out to creators and then you're doing the outreach, the negotiation, the invoicing, the review, all of that kind of stuff yourself in-house, which you just don't have the time for. If that resonates, I would love to tell you about Creator Grid, where we will literally run your creator campaigns for you end to end. You don't pay anything upfront. There is no retainer, there's no subscription, and you only pay... Oh, that's good. That's good. That's good. Before results. That means if you're looking for creators for UGC or content for ads, you only pay for the stuff that you approve, or if you launch an organic CPM campaign, you only pay for the view. I mean, yeah, he's definitely using AI systems as well, but like, obviously it's totally fine. You said creators actually get you. If we haven't met, hello, my name is Ali. I'm a doctor turned entrepreneur and creator with about eight million followers across socials, and I've been on the creator side of brand deals for the last decade. But the reason me and my team are building Creator Grid is that for the last two or three years, we've been trying to do creator marketing ourselves for our own software products, and realizing how much of a nightmare it is, which is why we built Creator Grid for ourselves. But then as we started speaking to other brands, everyone started saying to us, oh my goodness, I need this. And so we turned it into a product that now, lots of big brands around the world are actually using. Nice, not pretty good. Using for their creator marketing. And so in the next few minutes, I wanna show you exactly how it works and why I think it is a better way for you to do your creator marketing, rather than working with an expensive agency or trying to do it in-house. Creator Grid is our attempt to basically give you the level of service that a dumb, before you agency would. Just way faster, way cheaper, and with a lot less bandwidth from your team. Nice, that's pretty similar team. The Creator Grid platform is kind of like having a teammate who lives in your Slack. So you tell them what you're trying to achieve, and then we will literally run the campaign for you end to end. A bit like how simple it is to run meta ads. You set the objectives, so whether you want content for ads or for you to see. Bloody hell, that's good. See, or whether you want an organic CPM campaign, and we'll handle every aspect of the delivery. All you have to do is basically two things. So firstly, you decide which creators you wanna work with. Okay, so I mean, he's going a little bit more like real life, rather than like the fake Harry Potter stuff that I was using. So we'll source them for you, and you just sort of approve or reject them. And secondly, as you wanna approve content. I like the sound design. Content manually, we will give you a bunch of content, and you just decided to approve it or not. Everything else is handled by us. So the sourcing of creator is negotiating, reviewing the content initially, and then invoicing and paying the creators, tracking all the views, making sure the content is in line with your brand guidelines. All of that annoying stuff, we take off with your plane. Oh, that's really good. Man, Parth is sick of this. Let's see if we can come close to his level of quality. Yeah, mate, this Mac is absolutely heating up like a barbecue. Ooh, yeah. Actually, hard to hold onto it. This means that I can campaign to the wife that I need a fully decked out M5 Mac Studio, right? Which costs about 20,000 USD. But it's worth it. It's my boy math, because it will make the AI editing a little bit faster. Even though I don't really do editing myself, I'm just doing this for the vibes, right? Is that okay? Can I get an M5 Mac Studio, please? We can do it later. Nice. Very good. Very good. All right. So remotion is rendering all its things. Hyper frames is rendering all its things. Ba da da, boom, boom, boom, boom. Compositing all plates over the cut into a review MP4. That's what we like to see. Okay. I think we are done. Your first cut with all nine plates dropped in at the time codes for review only. Let's see what happens. So this is hyper frames. If you're a brand doing creator marketing, you will know that it's a total nightmare. Either you pay loads of money to an agency and wait ages for content, or your own team gets stuck doing everything. Finding the creators, DMing them, negotiating with them, doing the invoices, writing briefs, contracts, like all of that stuff. Creator Brit started as our in-house tool for dealing with all this faff, but then loads of brands told us they love the idea. And so we spun it out. Now we run your creator campaigns end to end, whether it's UGC for ads or whether you want organic views on content. Okay. This is not bad. I wish it did more picture in picture. Okay. Not bad, but I don't like the full screen nature of the graphics. I want always turn picture, but done in a nice way. Okay. Let's see what Remotion has done. If you're a brand doing creator marketing, you will know that it's a total nightmare. Either you pay loads of money to an agency and wait ages for content, or your own team gets stuck doing everything. Finding the creators, DMing them, negotiating with them, doing the invoices, writing briefs, contracts, all of that stuff. Creator Grid started as our in-house tool for dealing with all this faff, but then loads of brands told us they love the idea. And so we spun it out. Now we run your creator campaigns end to end, whether it's UGC for ads or whether you want organic views on content. Okay. So at this point, we have got V1 of the renders from Hyperframes and from Remotion. Both are pretty good. I would say they're like 85% there. There's a bit of polish that they could all do with. The Remotion one looks a little bit more AI sloppy with the gradients and stuff. So maybe we can just stop it from doing that. And there were a couple of bugs, like if you like random frames and like flash frames and things in the Remotion one, but the Hyperframes one looked pretty good. Okay. So I'm getting both Hyperframe and Remotion to both do the picture in picture thing that sort of looks like a loom video. All right. While this is still rendering, let's do a wee wee, about nine minutes until my next call. So maybe while I'm on the call, we'll get it to keep just cooking in the background for the sound effects and the background music. Let's see if the new Remotion version is good. If you're a brand doing creator marketing, you will know that it's a total nightmare. Either you pay loads of money to an agency and wait ages for content, or your own team gets stuck doing everything. Finding the creators, DMing them, negotiating themselves, getting invoices, writing briefs, contracts, like all of that stuff. Okay, I like the Remotion one. I think we are 90% there now. So I'm just getting it to tweak the very first line and add a bit more juice to the motion graphics initially. And now I have got a call, which I'm gonna take on my laptop so I can keep this stuff running in the background without dying. At this point, I was on a call with Pablo, my co-founder on creator grade, and he actually sent over a brand new logo. Now, when it comes to normal video editing, doing a rebrand when you're 90% done with a video is a total pain in the neck because it often means going back and redoing every single graphic by hand. But because these videos were basically code, my theory was I could just give Claude the new logo and I could ask it to update the entire design system based on that logo. And so let's see how it does. So this is the new kind of logo for creator grid. This is the new creator grid logo. Can you update the styles, et cetera, of the video to match, including the relevant colors and vibe. Boom, and boom. Cool. All right, it is officially 7.05 p.m. I need to head home for family dinner and then baby bedtime with the baby girl. But I think Izzy is still here on some onboarding calls for her new Dream 21 community. And so until then, we're gonna see if we can wait for these draft renders to finish and then we'll see how good a job this does at just like re-skinning the videos based on the new logo. Yeah, it's having to like re-render all of the motion plates. Learning number five, when your video is basically code, changing your mind is super cheap. Imagine how sick it would be if I had a fully decked out Mac Studio that was able to run local AI models and I could just dump footage onto it and overnight it would edit the footage into what is at least a rough cut. And so then our editors just get the rough cut that they can then finalize. That would be absolutely freaking bananas. But for now, I feel like this is a good final test of today's learning project to learn how to do AI video editing in a day. And here we go. Boss battle. If you're a brand doing creator marketing, you will know that it's a total nightmare. Either you pay loads of money to an agency and wait ages for content, or your own team gets stuck doing everything. Finding the creators, DMing them, negotiating with them, doing the invoices, writing briefs, contracts, like all of that stuff. Creator Grid started as our in-house tool for dealing with all this faff, but then loads of brands told us they loved the idea and so we spun it out. Now we run your creator campaigns end to end, whether it's UGC for ads or whether you want organic views and content. You just have to do two things. Firstly, you just approve the creators that you wanna work with, that we give to you. And secondly, you approve the content that they produce. Everything else is handled by us, our team and our platform. There's no retainer, there's no subscription, and you only pay for the content you approve or the organic views that that content gets. We're currently working with a bunch of big brands and we have over 10,000 creators on the platform just waiting to work with you. If you'd like to try creator marketing without the chaos, please do get in touch, tell us what you're after and we will just send you creators that might be a good fit. It costs you absolutely nothing to find out. Nice, that is really good. Background music is a little bit egregious. A few of the sound effects are a little bit like, and there's a couple of flash frames where I got things a little bit wrong, but like, holy moly, this is like 97% there. Okay, now this was hyper frames. Let's check out ReMotion. If you're a brand doing creator marketing, you will know that it's a total nightmare. Either you pay loads of money to an agency and wait ages for content, or your own team gets stuck doing everything. Finding the creators, DMing them, negotiating with them, doing the invoices, writing briefs, contracts, like all of that stuff. CreatorBrit started as our in-house tool for dealing with all this faff, but then loads of brands told us they loved the idea and so we spun it out. Now we run your creator campaigns end to end, whether it's UGC for ads or whether you want organic views on content. You just have to do two things. Firstly, you just approve the creators that you wanna work with that we give to you, and secondly, you approve the content that they produce. Everything else is handled by us, our team and our platform. There's no retainer, there's no subscription, and you only pay for the content you approve or the organic views that that content gets. We're currently working with a bunch of big brands and we have over 10,000 creators on the platform just waiting to work with you. So if you'd like to try creator marketing without the chaos, please do get in touch, tell us what you're after, and we will just send you creators that might be a good fit. It costs you absolutely nothing to find out. Wow, that is also not bad. That is also pretty solid. This AI editing thing, holy moly. Do you wanna check out what I've been cooking all day? Yes, it's filming. Yeah, it's filming. Oh, wow. Well, these are cute. Wait, these look quite smooth. My music. Luna not good. Was this one-shotted? No, of course not. Okay. It was about 20-shotted. I was gonna say, this is really good. This is very good. So if we scroll, this is how much back and forth it was. Okay. So it's not a huge amount. Not too bad. And if we look at the amount of words of, I'm mostly just giving it minor prompts here and there. Yeah, and it's mostly just sort of. And it's mostly just like doing stuff. Doing stuff. Video editors are cooked. Except our guys, of course. Yeah. Our guys are great. Except our guys. Yeah. Our guys are using this a lot. I sort of popped at it. I popped at it, but it was also very good. Yeah. Nice. It was better than this stuff. I think human plus AI is the sweet spot right now. Yeah. Now I said at the start of the day that I would be happy with the AI getting to 80% as good as our human editors. By the end of the day, I reckon we got it to about 97%, especially on the motion graphics front. It took about six hours from start to finish and it didn't cost anything on top of my Claude subscription. And now that I've done this once, I've firstly got all of the code that Claude generated and so it'd be easier to do it again. But more importantly, I have more of a mental model for exactly how AI video editing works. I feel like I've unlocked a part of my brain that's now able to think of more ways to use this miraculous technology for loads of other things in the business. Just gonna be really fun. And what's flabbergasting is that this is the worst it is ever gonna be. It only gets better from here. If you've gotten to this point in the video and you enjoyed it, you might like to check out my video right over here where I talk about tips for using AI to learn anything super fast. That'll be right over there. Thank you so much for watching and I'll see ya.

## Timestamped

`[00:00]` Oh my god, Opus 5.5 is incredible at making launch videos.
`[00:02]` Look at this one shot.
`[00:03]` How far can I go trying this sort of AI editing compared to our human video
`[00:08]` editor, who is very good?
`[00:09]` If this works, I will be absolutely amazed.
`[00:12]` That is really good.
`[00:13]` Oh no, oh no.
`[00:15]` I'm worried for video editors.
`[00:17]` We've got amazing video editors on my team.
`[00:20]` So every time a new AI model comes out, my Twitter feed fills up with people
`[00:24]` saying that this one can now edit videos.
`[00:26]` And I've been seeing that with basically every model released for the last few
`[00:29]` months, and so I was a little bit skeptical.
`[00:31]` Now for context, I edited my own videos for about three years back when I was
`[00:34]` working as a doctor for somewhere between 10 and 40 hours a week.
`[00:37]` And so I kind of know what a good edit feels like, but I'd never actually sat
`[00:40]` down and properly tried editing with AI.
`[00:43]` But then a public holiday came around and the team mostly had the day off and we
`[00:46]` needed a launch video for Creator Grade, one of our platforms.
`[00:48]` Path, one of our editors was already doing it the normal way.
`[00:51]` And so I decided to challenge myself for the day.
`[00:53]` Could I, as someone who's never tried AI video editing, learn how to use AI
`[00:56]` for video editing and make a video that comes as close as possible to a
`[01:00]` world-class human editor.
`[01:01]` And to be honest, if AI could get me like 80% of the way there,
`[01:04]` I would be delighted.
`[01:05]` This video is a little bit experimental.
`[01:07]` Usually I tell you about stuff that I already know, but in this video,
`[01:10]` I'm taking something that I don't have any idea about.
`[01:12]` And so if you want, you can watch the process of how I'm sort of
`[01:15]` learning it and figuring it out.
`[01:16]` And hopefully there'll be something that you can take away from this
`[01:19]` to apply to your own workflows for learning things or for applying AI.
`[01:22]` This is going to be a super long video, so there'll be timestamps
`[01:24]` down below, feel free to skip around if you like.
`[01:26]` But now before touching anything, I try to work out what video editing
`[01:30]` actually is because that's how we're going to figure out how to break
`[01:33]` it down using AI.
`[01:34]` What is video editing at its core?
`[01:36]` Okay.
`[01:36]` So if we think of when you've already got some footage compared to when you don't,
`[01:39]` when you've already got some footage, what is video editing?
`[01:41]` Well, firstly, you import the footage and then you need to basically
`[01:44]` cut out all the mistakes to get a clean A cut.
`[01:47]` Then once you've got a clean A cut, you then add in B roll.
`[01:51]` It would be like the screen recordings and the screenshots and stuff.
`[01:54]` Then the hard part, the bit that takes ages is animating the B roll so that
`[01:59]` you've got like zoom ins and zoom outs instead of just showing a screenshot,
`[02:02]` which would be boring.
`[02:03]` These launch videos often go in and out, and then there's motions and
`[02:05]` transitions and fade ins and movements and swipes and pans and all those things.
`[02:08]` So that takes a human video editor ages to do.
`[02:11]` Once you've done that, then it's like background music and sound design.
`[02:15]` So the background music, you know, we've got a particular vibe, but then sound
`[02:18]` effects like risers and swipes and swishes and all that kind of stuff.
`[02:22]` That is ultimately what video editing comes down to.
`[02:24]` And then obviously the taste factor is telling a good story and deciding
`[02:28]` what to cut out, deciding what to keep in.
`[02:30]` I feel like once we break it down into all those things these days, surely the
`[02:33]` AI should be pretty good at all that stuff.
`[02:35]` To be honest, I would be very amazed if it manages to just even get
`[02:38]` the A cut right immediately, right?
`[02:40]` Because when I as a human am editing a video, if there is a pause or there's
`[02:44]` a retake, you have to know where to cut and splice the footage together
`[02:48]` so that it doesn't sound weird.
`[02:49]` You know, we had a whole lesson in my course where I taught people
`[02:52]` how to use Final Cut Pro.
`[02:53]` There was a lot of time spent on just like nailing the A cut, because if
`[02:56]` you can nail the A cut, then everything becomes smoother further down the line.
`[02:59]` But if the A cut sucks, then everything else will kind of feel a bit disjointed.
`[03:03]` The stuff I've seen on Twitter is like super, super, super polished.
`[03:05]` They're like, oh my God, Opus 5.5 is incredible at making launch videos.
`[03:09]` Look at this one shot.
`[03:09]` And I'm like, there's no way that was actually one shot.
`[03:11]` Surely you had to go back and forth quite a lot and do a lot of
`[03:14]` tinkering to get that particular result.
`[03:15]` So I'm going to be very interested to see what does the one shot look like
`[03:19]` where I'm just, I'm not really driving it.
`[03:20]` I'm just like giving it copied and pasted stuff from Grok into Claude
`[03:23]` Code and then Claude Code into Claude Code, just like raw dog
`[03:25]` and just see what it does.
`[03:26]` And then when I've dabbled with AI stuff just for anything in the past,
`[03:29]` getting it to like 80% good enough happens with one shot.
`[03:32]` But then polishing that final 20% takes frickin ages.
`[03:35]` And the bulk of the time is spent in polishing it.
`[03:39]` So it feels good and looks good and has taste applied to it
`[03:43]` rather than just the one shot version.
`[03:48]` All right, so phase one of this project is I want to start
`[03:51]` by getting a lay of the land.
`[03:52]` What options do we even have for AI video editing?
`[03:54]` So I'm just going to use Grok because I don't need a VPN for it.
`[03:58]` I'm trying to figure out how to do AI video editing.
`[04:02]` I've got some footage.
`[04:04]` I need to turn into a launch video for Creator Grid,
`[04:09]` that form that helps it just learn, grow and monetize.
`[04:13]` I want to see if I can use AI video editing to make a
`[04:19]` alternative edit, ideally the whole thing.
`[04:22]` But also we could do a 30 to 60 second faceless launch
`[04:27]` creator type thing using motion graphics and stuff.
`[04:32]` Or we could do it like talking head with screen shots,
`[04:37]` like a YouTube video, some combo of all of the above.
`[04:42]` Help me figure this out.
`[04:43]` Three different pipelines.
`[04:45]` So one option is the DaVinci thing with an API.
`[04:49]` OK, D script for the cut and then resolve for grade graphics and finish.
`[04:53]` OK, option three, this is the remotion hyper frames lane, faceless brand launch
`[04:57]` trailers. Cool.
`[04:58]` Not entirely sure what any of this means just yet,
`[05:01]` but I think we have a reasonable lay of land.
`[05:04]` All right, so quick
`[05:05]` translation because there was a lot of jargon over there.
`[05:07]` There are basically two ways AI can make you a video right now.
`[05:10]` The first one is to edit the footage that you've actually filmed.
`[05:13]` For that, I used DaVinci Resolve,
`[05:14]` which is a proper professional video editor that recently started letting
`[05:18]` AI control it directly.
`[05:19]` But then the second is to not edit footage at all.
`[05:21]` You instead get the AI to write the video as code
`[05:24]` and it generates every single frame.
`[05:26]` That's what tools called hyper frames and remotion do.
`[05:28]` And it's how a lot of those launch videos that you might have seen
`[05:31]` on YouTube and Twitter are being made.
`[05:32]` I didn't know which approach would work.
`[05:34]` And so I decided to try both of them at the same time.
`[05:36]` Oh, what a vibe right as of literally right now.
`[05:39]` Path, one of our human video editors, has actually just sent me the first draft
`[05:43]` of this video that he was manually editing.
`[05:46]` So I don't want to watch it right now,
`[05:48]` but that could be interesting to compare.
`[05:50]` How far can I go with trying this sort of AI editing stuff
`[05:54]` for the first time compared to our human video editor, who is very good?
`[05:59]` OK, also, I've got a role filmed already.
`[06:03]` How do we get started?
`[06:04]` OK, firstly, Hagen hyper frames, core skills.
`[06:07]` Experiment B, a roll cut resolve.
`[06:09]` MCP needs DaVinci Resolve Studio 21.1, 295.
`[06:13]` All right, guess I'm paying $295 for DaVinci Resolve Studio.
`[06:16]` We are buying DaVinci Resolve Studio.
`[06:18]` All righty, it worked.
`[06:19]` We have just bought DaVinci Resolve Studio for about $300.
`[06:22]` And it is an 8.5 gigabyte file.
`[06:25]` So it is downloading.
`[06:26]` All right. Now I need to Claude plug and marketplace Hagen hyper frames.
`[06:29]` Install Hagen hyper frames.
`[06:31]` Let's open up Claude code.
`[06:33]` So what I want to do is let's go local.
`[06:36]` Let's make a new folder creator grid
`[06:41]` launch video or something.
`[06:43]` And let's open 5.5.
`[06:46]` OK, I'm trying to use hyper frames to make a launch video for a creator grid.
`[06:51]` I've already had some a roll that we don't necessarily need to use it.
`[06:57]` Here are some preferred notes from Grock.
`[07:00]` Let's see what Claude does.
`[07:02]` OK, we are installing hyper frame skills into the project.
`[07:05]` All right.
`[07:06]` So I've already got that footage.
`[07:08]` Let's chuck it into the project folder.
`[07:10]` Oh, and by the way, I've added in the existing video into the project folder FYI.
`[07:16]` Ah, OK, Claude Khododoski.
`[07:17]` FFmpeg isn't installed.
`[07:19]` Yes, by all means, please do.
`[07:20]` Yes, install FFmpeg.
`[07:22]` Happy for you to install it globally on this machine.
`[07:26]` Pablo, our co-founder, has put together this Claude artifact with product views
`[07:33]` we can use.
`[07:34]` I want to see what a pure faceless, just music.
`[07:38]` No voice video looks like.
`[07:41]` But also, I want to see what it looks like with just my voice as a voiceover
`[07:47]` and also what it looks like with both my voice and face,
`[07:51]` because I think my face and voice carries trust to some degree.
`[07:55]` Let's do a pipeline test first.
`[07:59]` It's doing stuff.
`[08:00]` Installing FFmpeg and Whisper CPP.
`[08:03]` I know what both of those things mean, so I don't need to ask.
`[08:06]` But if I didn't, I would totally ask.
`[08:07]` The screenshots are good.
`[08:08]` Real UI at 4K, setting up Hyperframes project and running the 10 second pipeline test.
`[08:12]` Great. It's just doing stuff.
`[08:14]` Oh, quick note from the sponsor of this video, which is Whisperflow.
`[08:17]` Now, on a good day, I can type at about 156 words per minute.
`[08:20]` But even with that insane typing speed, I can still speak faster than I can type.
`[08:23]` And so Whisperflow is a wonderful tool for turning your voice into text
`[08:26]` in pretty much any app you might be using.
`[08:28]` So, for example, I'm going to try this right now in Slack.
`[08:30]` Hey, Angus, we've got three things for Austin.
`[08:32]` Firstly, can we book the flights by Friday?
`[08:33]` I don't know, Thursday, actually.
`[08:35]` And make sure everyone's landing the evening before.
`[08:37]` Second, can you please send everyone the agenda with the planning sessions
`[08:41]` in the morning and the afternoons left free?
`[08:42]` And then thirdly, can we sort out a group dinner place for the first night,
`[08:44]` ideally somewhere that we can all fit in one table?
`[08:46]` Cool. Thank you so much.
`[08:48]` OK, so that took me under 30 seconds.
`[08:50]` And if you look at what's come out, it's turned my spiel
`[08:51]` into a very nice numbered list that makes it very easy
`[08:54]` for the person to see what I'm talking about.
`[08:55]` I made a mistake on saying Friday, no wait Thursday.
`[08:57]` And it took that into account.
`[08:59]` Now, people always say that, yeah, but my phone's got built in dictation,
`[09:01]` to which I would say, have you seen how bad the built in dictation
`[09:04]` on your phone is? Let's just try it out.
`[09:05]` Hey, Teemu, are you around for a call on Saturday?
`[09:08]` No, wait, Sunday.
`[09:09]` And can you send me the name of that book that you mentioned?
`[09:10]` So, yeah, it doesn't know how to spell my brother's name.
`[09:13]` It doesn't clock the mistake.
`[09:14]` And now if we try exactly the same thing in WhisperFlow.
`[09:17]` Hey, Teemu, are you around for a call on Saturday?
`[09:19]` No, wait, Sunday.
`[09:20]` And can you send me the name of that book you mentioned?
`[09:22]` Great. And it even knows that this is exactly how I spell
`[09:24]` my brother's nickname, his name is Teemu,
`[09:26]` and I call him Teem, and it knows exactly how to spell it.
`[09:28]` And it's automatically taken the error into account
`[09:30]` and removed it from the text, which is awesome.
`[09:31]` In my case, I've currently written 167,630 words
`[09:36]` on WhisperFlow so far, which is a fun little stat to see.
`[09:39]` Anyway, WhisperFlow is free to use,
`[09:41]` and if you wanna use it absolutely loads,
`[09:42]` then you can get WhisperFlow Pro
`[09:43]` that gives you unlimited words,
`[09:45]` and you can get a month of WhisperFlow Pro completely free
`[09:47]` by checking out the link in the video description.
`[09:48]` And when they ask you how you heard about them,
`[09:50]` please do write YouTube and put my name in the
`[09:52]` how did you hear about us box,
`[09:53]` because then they're more likely
`[09:54]` to sponsor more of our videos, which is awesome.
`[09:56]` So thank you, WhisperFlow, for sponsoring this video,
`[09:57]` and let's get back to it.
`[09:58]` Okay, awesome.
`[09:59]` Have we downloaded DaVinci Resolve yet?
`[10:01]` Yes, we have.
`[10:02]` Let's install this.
`[10:04]` I've literally never worked with DaVinci Resolve,
`[10:06]` but how hard can it be?
`[10:08]` Okay, classic.
`[10:10]` You look at a video editor and it looks intimidating AF.
`[10:13]` What do I do here?
`[10:14]` Help.
`[10:16]` AI?
`[10:17]` Set up AI assistance.
`[10:18]` All right, let's do that.
`[10:18]` DaVinci has been added to these.
`[10:20]` Please restart.
`[10:21]` Oh, wow, okay, cool.
`[10:22]` It's already done.
`[10:22]` So Cloud Desktop.
`[10:23]` Extension installer opened.
`[10:25]` DaVinci Resolve Studio.
`[10:26]` Extension.
`[10:27]` Okay then, install.
`[10:29]` Let's go.
`[10:30]` Oh, that was quick.
`[10:31]` Let's see, what's Cloud Code saying?
`[10:33]` No, still doing stuff.
`[10:35]` It's using some tokens.
`[10:36]` 3% obsession limit.
`[10:37]` All right, we've got plenty of headroom here.
`[10:39]` So what the hell do I do next on DaVinci?
`[10:42]` I mean, in theory,
`[10:43]` it should be connected to Cloud Code, right?
`[10:45]` So I could just,
`[10:46]` do you see the DaVinci Resolve connection?
`[10:50]` MCP, I think.
`[10:52]` Let's see what happens.
`[10:53]` Yes, wow.
`[10:54]` We're about half an hour in.
`[10:55]` So far, we've managed to buy and download
`[10:58]` DaVinci Resolve Studio
`[10:59]` and Cloud Code is cooking away
`[11:01]` on trying to do the hyperframes method.
`[11:04]` By the way, can you write me a brief?
`[11:08]` I can put in another Cloud Code chat within this project
`[11:12]` to test out DaVinci Resolve MCP
`[11:15]` for building this video as an alternative method.
`[11:20]` Nice.
`[11:21]` All right, well,
`[11:22]` Cloud Code is basically telling me
`[11:23]` what to copy and paste into Cloud Code.
`[11:25]` Boom.
`[11:27]` I love a good old copy paste from AI into itself.
`[11:32]` Oh, wow, okay.
`[11:34]` Cool.
`[11:35]` Storyboards are written,
`[11:36]` no animation code yet in your bands,
`[11:38]` gradients, glow-ins, fade-in, blah, blah, blah.
`[11:40]` Film A, music and text, 30 seconds.
`[11:41]` This is its own edit.
`[11:43]` With no voice,
`[11:44]` the type and the product shots
`[11:45]` have to tell the whole story.
`[11:46]` Okay, yep.
`[11:47]` Film B, your voice,
`[11:48]` 45 seconds with a 70 second extended cut,
`[11:50]` build it once, render it twice, voice only,
`[11:51]` and then with your face added.
`[11:53]` Film A silent has three options.
`[11:55]` Okay, let's look at that.
`[11:57]` Oh, okay, it's fun.
`[12:00]` All right, let's just ask these.
`[12:02]` One, demo data.
`[12:04]` Two, yes, we can show client logos.
`[12:07]` Three, that's okay.
`[12:09]` Four, is there a logo file?
`[12:11]` Get logo from creator-grid.io.
`[12:14]` Yes, static, no animation.
`[12:16]` Still render to prove the setup works, please.
`[12:19]` Pick an A option and the B length.
`[12:21]` Okay, so B length, 45 seconds, feels good.
`[12:25]` And A, you do two things, we do everything else.
`[12:28]` All right, creator marketing with other Ks.
`[12:30]` Nice, I quite like that.
`[12:31]` That's pretty good.
`[12:32]` A one option I like.
`[12:34]` Let's go.
`[12:35]` Hey, this is so good.
`[12:36]` Okay, now let's see what Resolve's doing.
`[12:38]` Creating work folders, find whisper models,
`[12:41]` probe source view live output, Resolve scripting API.
`[12:44]` All right, it's just doing stuff.
`[12:45]` I guess maybe I won't even need to use.
`[12:47]` It's not visibly doing anything,
`[12:48]` but I guess it's doing stuff in Cloud Code
`[12:50]` with the DaVinci Resolve connector.
`[12:52]` If this works, I will be absolutely amazed.
`[12:54]` There's no way it's gonna work first time.
`[12:56]` There's just no way.
`[12:57]` But this is quite cool.
`[12:59]` It's such a vibe, isn't it?
`[13:00]` Oh, open and split view.
`[13:01]` Oh, wow.
`[13:03]` This is really cool.
`[13:05]` So at this point, we've got stuff happening
`[13:07]` basically side by side.
`[13:08]` So on this side of the screen,
`[13:09]` we've got the DaVinci Resolve method
`[13:12]` of trying to do AI video editing.
`[13:14]` On this side of the screen,
`[13:15]` we have the code hyperframes method
`[13:18]` of doing AI video editing.
`[13:21]` And I'm just sort of sitting back
`[13:22]` and waiting for it to do stuff, which feels pretty good.
`[13:27]` Yeah, this iMacs fans are starting to get pretty,
`[13:31]` you know, this is hot.
`[13:32]` Everything's hot.
`[13:33]` If this really works,
`[13:34]` I might just upgrade to an M5 Mac Studio.
`[13:36]` Oh, wow, look at that.
`[13:37]` That is actually not bad.
`[13:38]` Creator marketing without the chaos.
`[13:39]` That actually looks pretty fricking solid.
`[13:41]` That looks pretty good.
`[13:42]` I mean, as anyone can generate a still these days,
`[13:44]` but that's, you know,
`[13:45]` remains to be seen how good this is for video editing.
`[13:47]` Let's see what happens next.
`[13:48]` All right, both storyboards are sketched.
`[13:51]` No animation code has been written yet.
`[13:52]` Okay, cool.
`[13:53]` Let's look at these storyboards.
`[13:54]` This is actually remarkably good.
`[13:56]` Creator marketing without the chaos.
`[13:57]` I don't like this font, but I think this is our font.
`[13:59]` Is that our font?
`[14:00]` Okay, I might have to redesign the creative grid branding
`[14:03]` if we do use that font.
`[14:04]` I'll get to the style later.
`[14:05]` Pick your creators, prove the content.
`[14:07]` We handle the sourcing, negotiating, time briefing,
`[14:09]` reviewing, invoicing, paying, tracking, everything else.
`[14:11]` Nice.
`[14:12]` Okay, so far I'm quite impressed by this storyboard.
`[14:16]` I wonder if I should use storyboards more
`[14:17]` when doing stuff.
`[14:18]` What's happening on DaVinci side?
`[14:19]` Okay, it's still doing stuff.
`[14:20]` Okay, so DaVinci has been cooking for 20 minutes
`[14:23]` and this just seems to be running into a bunch of issues.
`[14:26]` I probably should have done this one at a time,
`[14:28]` but you know what, let's just see.
`[14:30]` Let's just see what it's gonna do.
`[14:31]` One shot.
`[14:32]` You know, one of the things with working with AI
`[14:34]` is figuring out what to do while it's thinking.
`[14:36]` I could try and do a third thing.
`[14:38]` Why not?
`[14:39]` And by the way, I want to try using remotion
`[14:41]` as a third experiment running concurrently
`[14:45]` with hyperframes and resolve.
`[14:47]` Write a brief that I can give to a new cloud code instance
`[14:52]` within this project for this.
`[14:54]` So we've got hyperframes number one,
`[14:56]` we've got resolve is method number two,
`[14:59]` and we've got remotion, which is method number three.
`[15:03]` So we now have hyperframes over here,
`[15:05]` resolve in the middle and then remotion over here.
`[15:12]` Okay, all three drafts are rendered.
`[15:16]` We have MP4 files.
`[15:17]` All right, let's see, what does this look like?
`[15:20]` And is it any good?
`[15:36]` Eh, okay, well, that's pretty bad as a faceless version.
`[15:40]` Let's try DraftV2 voice no face.
`[15:42]` Let's see what happens.
`[15:43]` If you're a brand trying to grow with creator marketing,
`[15:46]` you probably know that it is a total nightmare.
`[15:48]` If that resonates, I would love to tell you
`[15:50]` about Creator Grid, where we will literally run
`[15:52]` your creator campaigns for you end to end.
`[15:55]` You don't pay anything upfront.
`[15:57]` There is no retainer, there's no subscription,
`[15:58]` and you only pay for results, entrepreneur and creator.
`[16:02]` If we haven't met, hello, man.
`[16:04]` What the hell?
`[16:05]` It's Ali, I'm a doctor turned entrepreneur
`[16:07]` and creator with about eight million.
`[16:09]` Creator Grid is our attempt to basically give you
`[16:11]` the level of service.
`[16:12]` Oh no, oh no, it didn't, it screwed up the A-cut.
`[16:16]` Just the basic A-cut, it just doesn't get it.
`[16:18]` I knew it, I knew it, the pauses, the pauses,
`[16:22]` the pauses are bad.
`[16:23]` It's not doing the A-cut properly.
`[16:25]` And now what if we have my face in it as well?
`[16:27]` What does that look like?
`[16:27]` If you're a brand trying to grow with creator marketing,
`[16:30]` you probably know that it is a total nightmare.
`[16:33]` If that resonates, I would love to tell you
`[16:34]` about Creator Grid, where we will literally run
`[16:36]` your creator campaigns for you end to end.
`[16:41]` You don't pay anything upfront.
`[16:42]` There is no retainer, there's no subscription,
`[16:44]` and you only pay for results, entrepreneur and creator.
`[16:48]` If we haven't met, hello, my name is Ali.
`[16:49]` Oh, this isn't bad.
`[16:53]` But this would have been magical a few years ago.
`[16:56]` Whoa, you could just do that with just getting a robot
`[16:59]` to operate DaVinci Resolve,
`[17:00]` but I had way higher hopes of the V1.
`[17:04]` Okay, hopefully Hyperframes does a better job with this.
`[17:06]` So I think what I may have to do is I might have
`[17:09]` to actually manually decide what to keep in
`[17:12]` in terms of what I've said,
`[17:13]` or maybe even record a separate video
`[17:15]` that's explicitly word for word,
`[17:17]` scripted 45 seconds long,
`[17:19]` because this one was more like five minutes long
`[17:20]` and it's just tried to figure out which bits to,
`[17:23]` this is frustrating, I do not like this.
`[17:26]` Let's grab something from Epidemic Sound.
`[17:28]` I wanna find a track that people wouldn't recognize.
`[17:39]` Oh, beautiful, right.
`[17:41]` Okay, so we're using Vivaldi's Spring
`[17:43]` as the background music for the Hyperframes one.
`[17:46]` Okay, still, we've got Hyperframes doing stuff,
`[17:48]` we've got Resolve doing stuff,
`[17:49]` and now we've got Remotion that's been doing stuff
`[17:51]` for the last 23 minutes.
`[17:52]` Also, one thing that I didn't really do is I could have,
`[17:55]` like I've been seeing stuff on Twitter recently
`[17:57]` about that where people have come up
`[17:59]` with these like elaborate prompts for Hyperframes.
`[18:02]` So maybe I could have just copy pasted one of those
`[18:03]` just to see what that would do,
`[18:04]` but we're not gonna get ahead of ourselves.
`[18:06]` We're just gonna try and focus on the simple stuff.
`[18:09]` We have a silent draft of the Hyperframes video.
`[18:13]` Shall we see what this looks like?
`[18:45]` Okay, it's not bad.
`[18:48]` The classical music makes it kind of funny.
`[18:51]` It's a little bit janky.
`[18:53]` It's the equivalent of if I were like 15 years old
`[18:56]` and learning video editing for the first time
`[18:58]` and deciding to use Vivaldi's Spring
`[19:02]` as the background music.
`[19:04]` It's impressive as a V1,
`[19:06]` but of course we need refinements to make it actually good.
`[19:09]` Okay, I'm gonna go for lunch.
`[19:10]` We're gonna come back,
`[19:11]` and my prediction is that I will be disappointed
`[19:13]` with the one-shot results of this,
`[19:16]` and then we will start the actual work
`[19:18]` of doing anything with AI, which is polishing.
`[19:23]` All righty, ladies and gentlemen,
`[19:25]` we are back after our lunch break,
`[19:27]` and it is time to see what is happening.
`[19:31]` So we're gonna start with the Hyperframes one.
`[19:35]` So we saw the silent one a little bit earlier.
`[19:37]` Let's try voice and no face.
`[19:40]` If you're a brand trying to grow with creator marketing,
`[19:42]` you probably know that it is a total nightmare.
`[19:45]` I would love to tell you about Creator Grid,
`[19:47]` where we will literally run your creator campaigns
`[19:49]` for you end-to-end.
`[19:50]` All you have to do is basically two things.
`[19:52]` So firstly, you decide which creators you wanna work with,
`[19:54]` so we'll source them for you.
`[19:55]` You just sort of approve or reject them.
`[19:57]` We will give you a bunch of content,
`[19:58]` and you just decide to approve it or not.
`[20:00]` Everything else is handled by us,
`[20:02]` so the sourcing of creators,
`[20:03]` negotiating, reviewing the content initially,
`[20:04]` and then invoicing and paying the creators,
`[20:07]` tracking all the views, lines, all of that annoying stuff,
`[20:09]` we take off with your plate.
`[20:11]` Oh, wow, okay.
`[20:12]` That's like remarkably impressive.
`[20:14]` That's way better than the DaVinci Resolve one.
`[20:17]` That's really well done.
`[20:19]` Let's see what this looks like with my face as well.
`[20:21]` If you're a brand trying to grow with creator marketing,
`[20:23]` you probably know that it is a total nightmare.
`[20:25]` I would love to tell you about Creator Grid,
`[20:27]` where we will literally run your creator campaigns
`[20:30]` for you end-to-end.
`[20:31]` All you have to do is basically two things.
`[20:33]` So firstly, you decide which creators you wanna work with,
`[20:35]` so we'll source them for you,
`[20:36]` and you just sort of approve or reject them.
`[20:38]` We will give you a bunch of content,
`[20:39]` and you just decide to approve it or not.
`[20:41]` Everything else is handled by us,
`[20:43]` so the sourcing of creators, negotiating,
`[20:44]` reviewing the content initially,
`[20:45]` and then invoicing and paying the creators,
`[20:48]` tracking all the views, lines, all of that annoying stuff,
`[20:50]` we take off with your plate.
`[20:52]` Wow, okay.
`[20:53]` That is very good.
`[20:56]` I mean, obviously, it could do with a lot of work,
`[20:58]` but that is remarkably impressive.
`[21:00]` I did not think it would be that good.
`[21:02]` Let's see how Remotion does it.
`[21:05]` Whoa!
`[21:06]` Remotion has literally given me a video editor interface.
`[21:10]` What the hell?
`[21:11]` I didn't realize I could do that.
`[21:12]` That's cool.
`[21:13]` Okay, let's see what this version looks like.
`[21:15]` If you're a brand trying to grow with creator marketing,
`[21:17]` you probably know that it is a total nightmare.
`[21:20]` If that resonates, I would love to tell-
`[21:22]` Hang on, let's try the voice face one.
`[21:23]` If you're a brand trying to grow with creator marketing,
`[21:26]` you probably know that it is a total nightmare.
`[21:29]` If that resonates, I would love to tell you
`[21:31]` about Creator Grid,
`[21:32]` where we will literally run your creator campaigns
`[21:34]` for you end to end.
`[21:36]` You don't pay anything up front.
`[21:37]` There is no retainer, there's no subscription,
`[21:39]` and you only pay for results.
`[21:43]` Oh, oh, okay.
`[21:46]` We need a bit of quality control on this one.
`[21:48]` I don't know why it's bugging out.
`[21:49]` Like, it looks-
`[21:50]` Pains for brands like Notion, Whisper Flow,
`[21:52]` Todoist, Superhuman, Victor, and a bunch of others.
`[21:55]` I see what they're trying to do,
`[21:56]` but this is just like super, super, super buggy.
`[21:58]` Like, what the hell is it doing?
`[21:59]` How the hell did you create a video editor
`[22:03]` within the browser itself?
`[22:05]` I didn't build that.
`[22:05]` The browser is Remotion Studio,
`[22:07]` which comes free with Remotion.
`[22:09]` It's a small local web app.
`[22:10]` Interesting.
`[22:11]` Okay, so Remotion Studio is probably the most, like,
`[22:14]` similar to a video editing experience,
`[22:15]` but, like, it was a bit buggy.
`[22:17]` Just not as good as the one that Hyperframes made.
`[22:21]` But Hyperframes doesn't have, like,
`[22:22]` the video editing interface.
`[22:25]` It's purely the code.
`[22:26]` And the one in DaVinci Resolve
`[22:28]` just was not very good at all.
`[22:29]` So at this point, I would rate Hyperframes
`[22:31]` as being, like, probably a seven out of 10.
`[22:32]` DaVinci Resolve, I would rate it
`[22:33]` being probably a three out of 10.
`[22:35]` And Remotion was super buggy,
`[22:37]` so I'd probably give it a two out of 10 right now.
`[22:39]` But it does have the right idea.
`[22:40]` It does have the right idea.
`[22:42]` Here is the problem, I think.
`[22:45]` We think about, like, the two versions of the video.
`[22:47]` If we imagine a role is what being said
`[22:51]` that needs to be a cut,
`[22:53]` so we go for a raw A-roll.
`[22:55]` What this kind of needs is a script.
`[22:58]` To raw A-roll, then you get the A-cut,
`[23:01]` and then you get the add-in effects.
`[23:05]` What I was trying to get Resolve to do
`[23:07]` is basically take 10 gigabytes worth of A-roll footage
`[23:11]` and hope that it would, A,
`[23:12]` magically be able to 45 seconds of that to turn into a cut,
`[23:16]` but then also to actually be able to edit an A-cut
`[23:19]` using J-cuts and L-cuts to the level that I would like.
`[23:22]` Now, that is probably a little bit unfair,
`[23:23]` and it's a little bit beyond
`[23:24]` what Opus 5.5 can do at this stage.
`[23:27]` Maybe one day you'll be able to just
`[23:29]` give it a bunch of footage and say,
`[23:30]` edit this for me, but today is not that day.
`[23:32]` So we are going to have to,
`[23:34]` at least on the Resolve front,
`[23:36]` drill down and start doing things a little bit manually,
`[23:39]` by which I mean kind of breaking things down
`[23:41]` a little bit more step by step.
`[23:42]` Maybe that's the way to think about
`[23:44]` AI editing with Resolve.
`[23:46]` Prove the concept first for 30 seconds.
`[23:51]` You know, and okay,
`[23:51]` this was dumb of me to not realize beforehand.
`[23:53]` In fairness, it's always good to just one-shot
`[23:54]` and see what happened,
`[23:55]` because then you see the holes in your prompting.
`[23:57]` Because if we were hiring a human video editor
`[23:59]` and I were testing out a brand new video editor,
`[24:01]` the way we do that is we give them 10 minutes of footage
`[24:04]` and we ask them to just give us
`[24:05]` the first 60 seconds as an edit
`[24:07]` because it gives us a feel for how are they doing.
`[24:11]` It would be unfair to ask a human video editor
`[24:13]` to say, hey, of these 10 minutes,
`[24:14]` pick the best 45 seconds
`[24:16]` and turn it into a cohesive story.
`[24:18]` And then let's see the editing
`[24:19]` because it would be a lot for a human video editor
`[24:21]` who's good at video editing,
`[24:22]` but maybe not good at scripting.
`[24:23]` Maybe actually the thing that I recorded
`[24:25]` is not suitable to be spliced into a 45-second chunk.
`[24:27]` Yeah, I don't wanna be one of those people
`[24:29]` that tries to one-shot something,
`[24:31]` gets a slightly s*** once and then thinks AI sucks.
`[24:33]` Like, I knew it.
`[24:34]` I knew it was using too much data.
`[24:36]` I knew the data centers were evil, et cetera, et cetera.
`[24:38]` It's like, no, I'm sure that there's definitely
`[24:40]` a way to do this.
`[24:41]` I just need to be a little bit more sophisticated
`[24:42]` with the process and make it happen.
`[24:45]` So my learning here, learning number one is,
`[24:48]` treat the AI like a human and give it the task
`[24:52]` that you would give to a human
`[24:53]` with the same level of instruction.
`[24:55]` Okay, I'm actually gonna switch out of Claude
`[24:57]` and go back into Grok.
`[24:59]` You know what, let me just do a Swiss workflow.
`[25:00]` So I think what's happening here
`[25:02]` is that we actually have two different work streams.
`[25:03]` One is a pure faceless launch video
`[25:06]` with like text and music and stuff.
`[25:07]` And so that is one that doesn't need the original footage,
`[25:10]` but then the second one is editing original footage.
`[25:13]` Those are actually two very different things.
`[25:14]` Editing original footage involves bringing in the footage,
`[25:17]` sorting out the A-cut,
`[25:18]` and then doing the B-roll and the animations and stuff.
`[25:21]` Whereas the pure faceless
`[25:22]` is just about doing really good animations.
`[25:24]` Now, I think what we can actually do,
`[25:26]` aha, is a hybrid of the two, hybrid.
`[25:29]` Because for example, if we figure out a system
`[25:32]` of nailing the editing of actual footage,
`[25:35]` like making the A-cut really good,
`[25:37]` and then separately we had an absolutely sick way
`[25:40]` of generating insanely high quality motion video
`[25:44]` that shows the screenshots of the app
`[25:46]` with all the relevant zooms and pans and all those things.
`[25:48]` Those are more similar to the ones
`[25:50]` that people post on Twitter.
`[25:51]` We can then combine the best of both worlds
`[25:54]` to create a talking head explainer video
`[25:56]` that also has all of the bells and whistles
`[25:59]` that like a purely animated launch video would have.
`[26:02]` Yes, treat them as two factories,
`[26:04]` and then a third step that only composites.
`[26:06]` Stream one, A-cut of real footage.
`[26:08]` Stream two, motion plates.
`[26:09]` Hyper frames when product screenshots, zooms, pans,
`[26:11]` connector type music hits, build each plate
`[26:14]` as it's own three to eight second composition
`[26:15]` against real UI.
`[26:16]` Drop hyper frames MP4 into the V3's B-roll
`[26:18]` talking head stays in V1.
`[26:20]` Okay, yeah, nice.
`[26:21]` Why are you calling them motion plates?
`[26:23]` Is that like industry terminology for this sort of thing?
`[26:25]` Oh, it's just a post-production word
`[26:26]` for a finished piece of motion graphics
`[26:28]` that you drop into a timeline.
`[26:29]` A plate is a self-contained visual layer.
`[26:32]` Oh, I had no idea.
`[26:32]` In old film work, it was a painted photograph background
`[26:35]` you composite piece people against.
`[26:36]` In this workflow, it's a short already rendered movie,
`[26:38]` three to eight seconds of zoom pans type in product UI
`[26:40]` that does not need to be built inside Resolve.
`[26:42]` Ah, most should just mean it's animated.
`[26:44]` You're not asking Resolve to animate the dashboard,
`[26:46]` you're asking to place a clip
`[26:47]` that already has the animation in it.
`[26:49]` That's clever.
`[26:50]` One thing I find when learning about AI stuff,
`[26:52]` or when trying to do AI stuff,
`[26:53]` is that I learn terminology
`[26:56]` that's actually used in the industry.
`[26:58]` So for example, the other day,
`[26:59]` I was doing some thumbnails for a thing,
`[27:01]` and I learned what a contact sheet is,
`[27:02]` which is basically like a series of thumbnails
`[27:05]` for a storyboard or something like that
`[27:06]` to explore different concept directions.
`[27:08]` And then because I then had that terminology,
`[27:09]` I was able to use that terminology in future prompts.
`[27:12]` I've never heard the phrase motion plate before,
`[27:13]` but this is exactly what I want.
`[27:15]` I want the a-cut of the video, the a-roll of me talking,
`[27:19]` and then I want really high quality motion plates
`[27:22]` to appear over the top
`[27:23]` based on what I'm saying in the video.
`[27:24]` Learning number two,
`[27:25]` learn the words that the professionals use.
`[27:27]` Because as soon as I knew it was called a motion plate,
`[27:29]` I could then ask the AI for exactly what I wanted.
`[27:32]` All right, this is exciting.
`[27:33]` I now have more of a mental model
`[27:35]` of what I'm trying to actually do here.
`[27:39]` Okay, so I'm gonna start with what I want is
`[27:43]` I'll give you a roll, a cut,
`[27:47]` I cleaned up a cut of the video of me talking.
`[27:51]` Ultimately, what I want is really nice motion plates
`[27:55]` that I can add to the a-cut using something like Resolve.
`[28:01]` All right, hyperframes can do this.
`[28:03]` Only the motion graphic shows
`[28:04]` with no blocks around it.
`[28:06]` PNG sequences with transparency, 4K output,
`[28:09]` amazing frame rate match to your footage.
`[28:11]` One of plate's project with each plate as its own file.
`[28:14]` That's just to do exactly the same one
`[28:19]` for remotion and see.
`[28:21]` Okay, I think I can basically get rid of
`[28:24]` worrying about Resolve, DaVinci Resolve for now,
`[28:27]` because I know that I don't need that
`[28:28]` for this stage of the process.
`[28:30]` I'm now realizing that I just need
`[28:32]` to create the motion plates,
`[28:34]` because then the script, the a-roll, the a-cut,
`[28:36]` that's like the easy part.
`[28:37]` I could always do it manually if I really wanted to,
`[28:38]` I could chuck it into Premiere and use Firecut
`[28:40]` if I really wanted to.
`[28:41]` The a-cut is the easy part, the hard part
`[28:43]` is what I now know is called the motion plates,
`[28:45]` which is cool.
`[28:45]` Ah, it's rendering a contact sheet, let's see.
`[28:47]` Okay, that's quite good, that's quite good.
`[28:49]` You pick the creators, that is all pretty good.
`[28:51]` Wow, I like this.
`[28:52]` The only thing I don't like about it
`[28:53]` is the sort of solid colors.
`[28:56]` Okay, I like this.
`[28:57]` I just don't like the solid colors
`[28:59]` of the backgrounds of the vertical video thumbnails.
`[29:03]` I want them to look more like actual UGC.
`[29:07]` So let's use real slash AI gen photorealistic images.
`[29:12]` Oh wow, that's pretty good.
`[29:14]` So it's using Canva to generate casual UGC style images
`[29:18]` to replace this stuff that looks a little bit fake.
`[29:22]` I mean, it all looks a bit fake,
`[29:23]` but I think that would sell the vision a little bit better.
`[29:26]` Learning number three, get the AI to show you the plan
`[29:28]` before it builds anything.
`[29:29]` If you have a storyboard or a contact sheet,
`[29:31]` that takes seconds to go through and fix stuff.
`[29:34]` But if you get it to one-shot the render
`[29:36]` all the way at the end,
`[29:36]` then like you have to spend a lot more time fixing stuff.
`[29:38]` All right, so Remotion has actually done a bunch of stuff.
`[29:41]` Let's see what it looks like.
`[29:43]` Inbox triage in 60 seconds, you approve the content.
`[29:48]` Yep, you pick the creators.
`[29:56]` Okay, that's really good.
`[30:00]` Your campaigns run end to end.
`[30:03]` That is remarkably good.
`[30:05]` Well done, Remotion.
`[30:07]` That's solid, look at that.
`[30:11]` Wow.
`[30:15]` Okay, I mean, we can definitely make a nicer graph,
`[30:18]` but this is really solid.
`[30:19]` Okay, I now like Remotion again.
`[30:21]` Let me just give it the same prompts
`[30:23]` as I did with this one.
`[30:25]` All right, this point is 3.45 PM.
`[30:27]` I have a couple of calls in about an hour,
`[30:28]` and so I wanna make as much progress
`[30:30]` as I possibly can in the next hour.
`[30:31]` I think we're getting there.
`[30:32]` Like the motion plates
`[30:33]` are actually getting surprisingly good.
`[30:35]` So I just need a properly scripted 45-second video,
`[30:40]` which I can then just record now.
`[30:42]` Get, I don't know, one of these tools
`[30:44]` to get the A-cut of it.
`[30:45]` Once I have a clean A-cut that I'm happy with,
`[30:47]` I can then overlay all of these different motion plates
`[30:50]` that we're creating,
`[30:50]` whether it's from Remotion or Hyperlapse.
`[30:52]` Okay, so at this point,
`[30:53]` I'm very happy with the images
`[30:57]` of what this stuff looks like.
`[30:58]` I think it's done a really solid job.
`[31:00]` This is the Hyperframes method.
`[31:02]` Let's see what it does when it animates it.
`[31:06]` All right, updated real, new views chart.
`[31:09]` Let's see what this looks like via Remotion.
`[31:17]` Nice, nice.
`[31:28]` Okay, well done, Remotion.
`[31:30]` Now at this point, the thing I'd finally clocked
`[31:31]` was that my original video was about five minutes long,
`[31:34]` and I'd basically been asking the AI
`[31:35]` to dig out a 45-second launch video
`[31:38]` out of five minutes of me talking,
`[31:39]` which is a job that I would never give
`[31:40]` to a human editor either.
`[31:42]` And so learning number four is that
`[31:43]` if you want a short video, film a short script.
`[31:45]` So I got Claude to write me a very tight script
`[31:47]` based on what it said in the original,
`[31:48]` and then I filmed it again.
`[31:50]` Let's get Claude to create the script for me
`[31:51]` because it knows exactly what I said previously
`[31:53]` and it's been doing all this stuff.
`[31:54]` In this project, we should have the transcript
`[31:57]` of the VSL I filmed for Creator Grid.
`[32:00]` Write me the V1 of the script.
`[32:03]` Okay, this is actually a very solid script.
`[32:06]` Let's now film the thing.
`[32:07]` If you're a brand doing creator marketing,
`[32:08]` you will know that it's a total nightmare.
`[32:10]` Okay, so we have just filmed the video,
`[32:13]` so now we need to export a clean A-cut of this video.
`[32:17]` How do I most expediently export a clean A-cut?
`[32:22]` You know what?
`[32:23]` Let's download Firecut for Resolve.
`[32:25]` I think Firecut for Resolve, somewhat ironically,
`[32:28]` is actually the tool that I'm gonna use for this.
`[32:30]` Firecut for DaVinci Resolve.
`[32:32]` I've never actually used Firecut myself.
`[32:34]` Our video editors use it,
`[32:35]` and we built it as an initial tool
`[32:36]` to use in-house for our team.
`[32:38]` Okay, so now I wanna do the first cut.
`[32:41]` Boom.
`[32:42]` Can I just generate the first cut?
`[32:43]` Let's see what happens.
`[32:44]` Nice.
`[32:45]` Okay, if you're a creator
`[32:46]` and you're paying a little bit,
`[32:47]` either you're paying agency, yep.
`[32:48]` I'm a total noob to Resolve,
`[32:50]` having literally never used it before in my life,
`[32:51]` but let's see.
`[32:53]` Let's see what happens.
`[32:54]` How do I zoom in and out?
`[32:56]` Okay, yeah, fine.
`[32:57]` If you're a brand doing creator marketing,
`[32:58]` you will know that it's a total nightmare.
`[33:00]` Either you pay an agency, a massive retainer,
`[33:02]` and wait, either you pay, ah.
`[33:04]` So Firecut has given me a very rough first cut,
`[33:06]` but it hasn't quite made it.
`[33:09]` You know what?
`[33:10]` Maybe this is just a case of me
`[33:12]` actually just doing this manually.
`[33:14]` How do I do cuts?
`[33:16]` On this thing.
`[33:17]` Command T.
`[33:18]` Laid tool.
`[33:19]` Boom.
`[33:20]` Ah, it's not a magnetic timeline, for goodness sake.
`[33:22]` Haven't done this sort of shit in absolutely ages,
`[33:25]` but this literally used to be my bread and butter
`[33:27]` in final cut.
`[33:28]` Produced every two years of my life.
`[33:30]` By us, our team, and our platform.
`[33:31]` So at this point, we have just exported a clean A cut.
`[33:34]` I probably could have done it with AI,
`[33:35]` but I didn't have the time to figure it out,
`[33:37]` so I don't know how long it'll take me.
`[33:38]` So now what I want is I want the transcription.
`[33:41]` So I'm gonna use this tool,
`[33:42]` Whisper Transcription, for that.
`[33:43]` Okay, we finally have a clean cut that I've just edited.
`[33:48]` This is the transcript.
`[33:50]` I want you to generate all the motion plates
`[33:53]` for this new transcript.
`[33:55]` Boom.
`[33:56]` And let's just do the same thing over here.
`[33:57]` So the A cut is done.
`[33:58]` In Resolve using fire cut
`[34:00]` and using a bit of manual editing.
`[34:01]` Now for the B roll.
`[34:02]` Motion plates are being done by hyper frames
`[34:04]` and by remotion.
`[34:06]` Sick.
`[34:06]` Then, background music.
`[34:08]` And I think then maybe the final thing might be
`[34:11]` to add in some sound design, actually,
`[34:15]` like plops and whooshes and stuff.
`[34:17]` Conveniently, epidemic sound has a bunch of that stuff in it.
`[34:20]` They've got swooshes, ambience, water, vehicles, whoosh.
`[34:22]` Can I just give the AI access to epidemic sound?
`[34:27]` Because that would be handy if it could find API keys.
`[34:31]` I love it when there's API keys.
`[34:33]` So I don't wanna do this, try and do this one shot.
`[34:37]` We're gonna see what it does with just the motion plates
`[34:39]` and then we'll add the background music
`[34:41]` and the sound effects.
`[34:42]` But I've got it ready so that we can save some time.
`[34:44]` Bonjour.
`[34:47]` Good.
`[34:48]` You are on the camera.
`[34:50]` Okay, now that we've actually done this,
`[34:51]` while we're waiting, we can actually check out path,
`[34:53]` what path said.
`[34:54]` Let's see.
`[34:55]` If you're a brand trying to grow with creator marks.
`[34:57]` That's really good.
`[35:00]` Oh, he gets it.
`[35:03]` Right.
`[35:04]` Marketing, you probably know that it is a total nightmare.
`[35:06]` Either you pay an agency, a massive retainer,
`[35:08]` and then you wait a few months to years
`[35:10]` for the content that may or may not be usable,
`[35:12]` or you and your team is trying to like manually reach out
`[35:14]` to creators and then you're doing the outreach,
`[35:16]` the negotiation, the invoicing, the review,
`[35:17]` all of that kind of stuff yourself in-house,
`[35:19]` which you just don't have the time for.
`[35:20]` If that resonates, I would love to tell you
`[35:22]` about Creator Grid, where we will literally run
`[35:24]` your creator campaigns for you end to end.
`[35:26]` You don't pay anything upfront.
`[35:27]` There is no retainer, there's no subscription,
`[35:29]` and you only pay...
`[35:31]` Oh, that's good.
`[35:32]` That's good.
`[35:34]` That's good.
`[35:35]` Before results.
`[35:36]` That means if you're looking for creators
`[35:37]` for UGC or content for ads,
`[35:39]` you only pay for the stuff that you approve,
`[35:40]` or if you launch an organic CPM campaign,
`[35:42]` you only pay for the view.
`[35:44]` I mean, yeah, he's definitely using AI systems as well,
`[35:46]` but like, obviously it's totally fine.
`[35:47]` You said creators actually get you.
`[35:48]` If we haven't met, hello, my name is Ali.
`[35:49]` I'm a doctor turned entrepreneur and creator
`[35:51]` with about eight million followers across socials,
`[35:53]` and I've been on the creator side of brand deals
`[35:55]` for the last decade.
`[35:56]` But the reason me and my team are building Creator Grid
`[35:57]` is that for the last two or three years,
`[35:59]` we've been trying to do creator marketing ourselves
`[36:01]` for our own software products,
`[36:02]` and realizing how much of a nightmare it is,
`[36:03]` which is why we built Creator Grid for ourselves.
`[36:05]` But then as we started speaking to other brands,
`[36:07]` everyone started saying to us,
`[36:08]` oh my goodness, I need this.
`[36:09]` And so we turned it into a product that now,
`[36:11]` lots of big brands around the world are actually using.
`[36:13]` Nice, not pretty good.
`[36:14]` Using for their creator marketing.
`[36:15]` And so in the next few minutes,
`[36:16]` I wanna show you exactly how it works
`[36:17]` and why I think it is a better way for you
`[36:19]` to do your creator marketing,
`[36:21]` rather than working with an expensive agency
`[36:22]` or trying to do it in-house.
`[36:24]` Creator Grid is our attempt to basically give you
`[36:25]` the level of service that a dumb,
`[36:28]` before you agency would.
`[36:29]` Just way faster, way cheaper,
`[36:30]` and with a lot less bandwidth from your team.
`[36:32]` Nice, that's pretty similar team.
`[36:33]` The Creator Grid platform is kind of like
`[36:35]` having a teammate who lives in your Slack.
`[36:36]` So you tell them what you're trying to achieve,
`[36:37]` and then we will literally run the campaign
`[36:39]` for you end to end.
`[36:40]` A bit like how simple it is to run meta ads.
`[36:41]` You set the objectives,
`[36:42]` so whether you want content for ads
`[36:44]` or for you to see.
`[36:45]` Bloody hell, that's good.
`[36:45]` See, or whether you want an organic CPM campaign,
`[36:48]` and we'll handle every aspect of the delivery.
`[36:50]` All you have to do is basically two things.
`[36:51]` So firstly, you decide which creators
`[36:53]` you wanna work with.
`[36:54]` Okay, so I mean, he's going a little bit more
`[36:56]` like real life,
`[36:57]` rather than like the fake Harry Potter stuff
`[36:58]` that I was using.
`[36:59]` So we'll source them for you,
`[37:00]` and you just sort of approve or reject them.
`[37:01]` And secondly,
`[37:02]` as you wanna approve content.
`[37:03]` I like the sound design.
`[37:04]` Content manually,
`[37:05]` we will give you a bunch of content,
`[37:06]` and you just decided to approve it or not.
`[37:08]` Everything else is handled by us.
`[37:09]` So the sourcing of creator is negotiating,
`[37:11]` reviewing the content initially,
`[37:12]` and then invoicing and paying the creators,
`[37:14]` tracking all the views,
`[37:15]` making sure the content is in line
`[37:16]` with your brand guidelines.
`[37:17]` All of that annoying stuff,
`[37:18]` we take off with your plane.
`[37:19]` Oh, that's really good.
`[37:20]` Man, Parth is sick of this.
`[37:21]` Let's see if we can come close
`[37:22]` to his level of quality.
`[37:24]` Yeah, mate, this Mac is absolutely heating up
`[37:27]` like a barbecue.
`[37:29]` Ooh, yeah.
`[37:31]` Actually, hard to hold onto it.
`[37:34]` This means that I can campaign to the wife
`[37:36]` that I need a fully decked out M5 Mac Studio, right?
`[37:40]` Which costs about 20,000 USD.
`[37:42]` But it's worth it.
`[37:43]` It's my boy math,
`[37:43]` because it will make the AI editing a little bit faster.
`[37:46]` Even though I don't really do editing myself,
`[37:47]` I'm just doing this for the vibes, right?
`[37:49]` Is that okay?
`[37:49]` Can I get an M5 Mac Studio, please?
`[37:51]` We can do it later.
`[37:51]` Nice.
`[37:52]` Very good.
`[37:53]` Very good.
`[37:55]` All right.
`[37:56]` So remotion is rendering all its things.
`[37:58]` Hyper frames is rendering all its things.
`[37:59]` Ba da da, boom, boom, boom, boom.
`[38:02]` Compositing all plates over the cut into a review MP4.
`[38:05]` That's what we like to see.
`[38:06]` Okay.
`[38:07]` I think we are done.
`[38:09]` Your first cut with all nine plates dropped
`[38:11]` in at the time codes for review only.
`[38:13]` Let's see what happens.
`[38:14]` So this is hyper frames.
`[38:16]` If you're a brand doing creator marketing,
`[38:18]` you will know that it's a total nightmare.
`[38:19]` Either you pay loads of money to an agency
`[38:21]` and wait ages for content,
`[38:21]` or your own team gets stuck doing everything.
`[38:23]` Finding the creators,
`[38:24]` DMing them, negotiating with them,
`[38:25]` doing the invoices,
`[38:26]` writing briefs, contracts,
`[38:27]` like all of that stuff.
`[38:28]` Creator Brit started as our in-house tool
`[38:30]` for dealing with all this faff,
`[38:31]` but then loads of brands told us they love the idea.
`[38:33]` And so we spun it out.
`[38:34]` Now we run your creator campaigns end to end,
`[38:36]` whether it's UGC for ads
`[38:37]` or whether you want organic views on content.
`[38:39]` Okay.
`[38:40]` This is not bad.
`[38:41]` I wish it did more picture in picture.
`[38:43]` Okay.
`[38:44]` Not bad,
`[38:45]` but I don't like the full screen nature of the graphics.
`[38:49]` I want always turn picture,
`[38:52]` but done in a nice way.
`[38:55]` Okay.
`[38:56]` Let's see what Remotion has done.
`[38:59]` If you're a brand doing creator marketing,
`[39:00]` you will know that it's a total nightmare.
`[39:01]` Either you pay loads of money to an agency
`[39:03]` and wait ages for content,
`[39:04]` or your own team gets stuck doing everything.
`[39:06]` Finding the creators,
`[39:07]` DMing them, negotiating with them,
`[39:08]` doing the invoices,
`[39:09]` writing briefs, contracts,
`[39:10]` all of that stuff.
`[39:11]` Creator Grid started as our in-house tool
`[39:13]` for dealing with all this faff,
`[39:14]` but then loads of brands told us they love the idea.
`[39:15]` And so we spun it out.
`[39:16]` Now we run your creator campaigns end to end,
`[39:18]` whether it's UGC for ads
`[39:20]` or whether you want organic views on content.
`[39:22]` Okay.
`[39:23]` So at this point,
`[39:23]` we have got V1 of the renders from Hyperframes
`[39:26]` and from Remotion.
`[39:27]` Both are pretty good.
`[39:29]` I would say they're like 85% there.
`[39:31]` There's a bit of polish that they could all do with.
`[39:34]` The Remotion one looks a little bit more AI sloppy
`[39:36]` with the gradients and stuff.
`[39:37]` So maybe we can just stop it from doing that.
`[39:39]` And there were a couple of bugs,
`[39:40]` like if you like random frames
`[39:42]` and like flash frames and things in the Remotion one,
`[39:44]` but the Hyperframes one looked pretty good.
`[39:46]` Okay.
`[39:46]` So I'm getting both Hyperframe and Remotion
`[39:48]` to both do the picture in picture thing
`[39:50]` that sort of looks like a loom video.
`[39:51]` All right.
`[39:52]` While this is still rendering,
`[39:53]` let's do a wee wee,
`[39:54]` about nine minutes until my next call.
`[39:57]` So maybe while I'm on the call,
`[39:59]` we'll get it to keep just cooking in the background
`[40:01]` for the sound effects and the background music.
`[40:03]` Let's see if the new Remotion version is good.
`[40:06]` If you're a brand doing creator marketing,
`[40:08]` you will know that it's a total nightmare.
`[40:09]` Either you pay loads of money to an agency
`[40:11]` and wait ages for content,
`[40:12]` or your own team gets stuck doing everything.
`[40:14]` Finding the creators, DMing them,
`[40:15]` negotiating themselves,
`[40:16]` getting invoices, writing briefs, contracts,
`[40:17]` like all of that stuff.
`[40:18]` Okay, I like the Remotion one.
`[40:20]` I think we are 90% there now.
`[40:22]` So I'm just getting it to tweak the very first line
`[40:25]` and add a bit more juice to the motion graphics initially.
`[40:29]` And now I have got a call,
`[40:31]` which I'm gonna take on my laptop
`[40:32]` so I can keep this stuff running in the background
`[40:34]` without dying.
`[40:35]` At this point, I was on a call with Pablo,
`[40:36]` my co-founder on creator grade,
`[40:38]` and he actually sent over a brand new logo.
`[40:39]` Now, when it comes to normal video editing,
`[40:41]` doing a rebrand when you're 90% done with a video
`[40:44]` is a total pain in the neck
`[40:45]` because it often means going back
`[40:46]` and redoing every single graphic by hand.
`[40:48]` But because these videos were basically code,
`[40:50]` my theory was I could just give Claude the new logo
`[40:53]` and I could ask it to update the entire design system
`[40:56]` based on that logo.
`[40:57]` And so let's see how it does.
`[40:58]` So this is the new kind of logo for creator grid.
`[41:03]` This is the new creator grid logo.
`[41:05]` Can you update the styles, et cetera,
`[41:08]` of the video to match,
`[41:10]` including the relevant colors and vibe.
`[41:15]` Boom, and boom.
`[41:17]` Cool.
`[41:17]` All right, it is officially 7.05 p.m.
`[41:20]` I need to head home for family dinner
`[41:23]` and then baby bedtime with the baby girl.
`[41:26]` But I think Izzy is still here on some onboarding calls
`[41:30]` for her new Dream 21 community.
`[41:33]` And so until then,
`[41:34]` we're gonna see if we can wait
`[41:36]` for these draft renders to finish
`[41:37]` and then we'll see how good a job this does
`[41:39]` at just like re-skinning the videos based on the new logo.
`[41:44]` Yeah, it's having to like re-render
`[41:46]` all of the motion plates.
`[41:47]` Learning number five,
`[41:48]` when your video is basically code,
`[41:50]` changing your mind is super cheap.
`[41:51]` Imagine how sick it would be
`[41:52]` if I had a fully decked out Mac Studio
`[41:54]` that was able to run local AI models
`[41:56]` and I could just dump footage onto it
`[41:58]` and overnight it would edit the footage
`[42:01]` into what is at least a rough cut.
`[42:03]` And so then our editors just get the rough cut
`[42:05]` that they can then finalize.
`[42:06]` That would be absolutely freaking bananas.
`[42:08]` But for now, I feel like this is a good final test
`[42:11]` of today's learning project
`[42:13]` to learn how to do AI video editing in a day.
`[42:15]` And here we go.
`[42:18]` Boss battle.
`[42:20]` If you're a brand doing creator marketing,
`[42:22]` you will know that it's a total nightmare.
`[42:23]` Either you pay loads of money to an agency
`[42:24]` and wait ages for content,
`[42:25]` or your own team gets stuck doing everything.
`[42:27]` Finding the creators, DMing them,
`[42:29]` negotiating with them, doing the invoices,
`[42:30]` writing briefs, contracts, like all of that stuff.
`[42:32]` Creator Grid started as our in-house tool
`[42:34]` for dealing with all this faff,
`[42:35]` but then loads of brands told us they loved the idea
`[42:37]` and so we spun it out.
`[42:38]` Now we run your creator campaigns end to end,
`[42:40]` whether it's UGC for ads
`[42:41]` or whether you want organic views and content.
`[42:43]` You just have to do two things.
`[42:44]` Firstly, you just approve the creators
`[42:46]` that you wanna work with, that we give to you.
`[42:47]` And secondly, you approve the content that they produce.
`[42:49]` Everything else is handled by us,
`[42:51]` our team and our platform.
`[42:51]` There's no retainer, there's no subscription,
`[42:53]` and you only pay for the content you approve
`[42:55]` or the organic views that that content gets.
`[42:57]` We're currently working with a bunch of big brands
`[42:59]` and we have over 10,000 creators on the platform
`[43:01]` just waiting to work with you.
`[43:02]` If you'd like to try creator marketing without the chaos,
`[43:04]` please do get in touch, tell us what you're after
`[43:06]` and we will just send you creators
`[43:07]` that might be a good fit.
`[43:08]` It costs you absolutely nothing to find out.
`[43:10]` Nice, that is really good.
`[43:14]` Background music is a little bit egregious.
`[43:16]` A few of the sound effects are a little bit like,
`[43:17]` and there's a couple of flash frames
`[43:19]` where I got things a little bit wrong,
`[43:20]` but like, holy moly, this is like 97% there.
`[43:25]` Okay, now this was hyper frames.
`[43:27]` Let's check out ReMotion.
`[43:29]` If you're a brand doing creator marketing,
`[43:31]` you will know that it's a total nightmare.
`[43:32]` Either you pay loads of money to an agency
`[43:34]` and wait ages for content,
`[43:35]` or your own team gets stuck doing everything.
`[43:37]` Finding the creators, DMing them,
`[43:38]` negotiating with them, doing the invoices,
`[43:40]` writing briefs, contracts, like all of that stuff.
`[43:42]` CreatorBrit started as our in-house tool
`[43:44]` for dealing with all this faff,
`[43:44]` but then loads of brands told us they loved the idea
`[43:46]` and so we spun it out.
`[43:47]` Now we run your creator campaigns end to end,
`[43:49]` whether it's UGC for ads
`[43:51]` or whether you want organic views on content.
`[43:53]` You just have to do two things.
`[43:54]` Firstly, you just approve the creators
`[43:55]` that you wanna work with that we give to you,
`[43:56]` and secondly, you approve the content that they produce.
`[43:59]` Everything else is handled by us,
`[44:00]` our team and our platform.
`[44:02]` There's no retainer, there's no subscription,
`[44:03]` and you only pay for the content you approve
`[44:05]` or the organic views that that content gets.
`[44:07]` We're currently working with a bunch of big brands
`[44:08]` and we have over 10,000 creators on the platform
`[44:10]` just waiting to work with you.
`[44:11]` So if you'd like to try creator marketing
`[44:13]` without the chaos, please do get in touch,
`[44:15]` tell us what you're after,
`[44:16]` and we will just send you creators
`[44:17]` that might be a good fit.
`[44:18]` It costs you absolutely nothing to find out.
`[44:20]` Wow, that is also not bad.
`[44:22]` That is also pretty solid.
`[44:24]` This AI editing thing, holy moly.
`[44:26]` Do you wanna check out what I've been cooking all day?
`[44:28]` Yes, it's filming.
`[44:30]` Yeah, it's filming.
`[44:32]` Oh, wow.
`[44:32]` Well, these are cute.
`[44:40]` Wait, these look quite smooth.
`[44:47]` My music.
`[44:53]` Luna not good.
`[45:02]` Was this one-shotted?
`[45:02]` No, of course not.
`[45:03]` Okay.
`[45:04]` It was about 20-shotted.
`[45:05]` I was gonna say, this is really good.
`[45:08]` This is very good.
`[45:09]` So if we scroll, this is how much back and forth it was.
`[45:12]` Okay.
`[45:13]` So it's not a huge amount.
`[45:14]` Not too bad.
`[45:15]` And if we look at the amount of words of,
`[45:17]` I'm mostly just giving it minor prompts here and there.
`[45:19]` Yeah, and it's mostly just sort of.
`[45:20]` And it's mostly just like doing stuff.
`[45:22]` Doing stuff.
`[45:22]` Video editors are cooked.
`[45:24]` Except our guys, of course.
`[45:25]` Yeah.
`[45:26]` Our guys are great.
`[45:27]` Except our guys.
`[45:27]` Yeah.
`[45:28]` Our guys are using this a lot.
`[45:29]` I sort of popped at it.
`[45:31]` I popped at it, but it was also very good.
`[45:32]` Yeah.
`[45:33]` Nice.
`[45:34]` It was better than this stuff.
`[45:34]` I think human plus AI is the sweet spot right now.
`[45:38]` Yeah.
`[45:40]` Now I said at the start of the day
`[45:41]` that I would be happy with the AI
`[45:43]` getting to 80% as good as our human editors.
`[45:45]` By the end of the day,
`[45:46]` I reckon we got it to about 97%,
`[45:48]` especially on the motion graphics front.
`[45:50]` It took about six hours from start to finish
`[45:52]` and it didn't cost anything
`[45:53]` on top of my Claude subscription.
`[45:54]` And now that I've done this once,
`[45:55]` I've firstly got all of the code that Claude generated
`[45:58]` and so it'd be easier to do it again.
`[45:59]` But more importantly,
`[46:00]` I have more of a mental model
`[46:01]` for exactly how AI video editing works.
`[46:04]` I feel like I've unlocked a part of my brain
`[46:07]` that's now able to think of more ways
`[46:09]` to use this miraculous technology
`[46:12]` for loads of other things in the business.
`[46:14]` Just gonna be really fun.
`[46:16]` And what's flabbergasting is that
`[46:18]` this is the worst it is ever gonna be.
`[46:22]` It only gets better from here.
`[46:23]` If you've gotten to this point in the video
`[46:24]` and you enjoyed it,
`[46:25]` you might like to check out my video right over here
`[46:26]` where I talk about tips for using AI
`[46:29]` to learn anything super fast.
`[46:31]` That'll be right over there.
`[46:31]` Thank you so much for watching
`[46:32]` and I'll see ya.
