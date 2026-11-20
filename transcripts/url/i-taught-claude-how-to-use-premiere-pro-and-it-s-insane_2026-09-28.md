# I taught Claude how to use Premiere Pro and it's INSANE.

- **Source:** https://www.youtube.com/watch?v=Ohyo6-VO1jY
- **Uploader:** Jason Cooperson
- **Uploaded:** 2026-07-24
- **Duration:** 20:58
- **Detected language:** en (p=1.00)
- **Model:** small.en

## Transcript

What you're watching right now, every cut, every transition, and every graphic was done by Claude within Premiere Pro. Claude opened up Premiere Pro, cut together all of the footage, generated all of the graphics, and actually edited this entire video. And I'll let you be the judge of how well it did. But honestly guys, I think that this is just the beginning. I think that this is the future of where video editing is headed. I believe that you don't need to know how to do keyframes. You don't need to know what an adjustment layer is anymore. You don't need to know any of the technical aspects of things because that is being essentially replaced by AI. And now we can just focus on the creative aspects of creating content. And again, guys, I just want to remind you that everything you've seen so far has been edited using the exact system that I'm about to show you in this video right now. So without further ado, let's get into the tutorial. All right, guys. So before we get into the nitty gritty of the video, I'm going to quickly go over an overview of this entire project. Now, if you want to skip this part, you totally can. You can skip to the demo or you can skip to the tutorial section if you just want to get it straight into it. Okay, so basically what this project is that I've been working on and how I actually edited the intro that you just saw was with this project folder. It's pretty much just a Claude project that lives on my computer. So it's a folder of files. You can see all these files and that is how it's able to edit videos. I had to custom build a lot of this stuff. You can see this is what it looks like on my computer and this is what it looks like when you're in a Claude chat. Now, it's really built upon two core engines here. We have Hyperframes and we have the Premiere Pro MCP. So Hyperframes is how it's actually able to generate the motion graphics. And then the Premiere Pro MCP is how we connect up the Claude app to our Premiere Pro. Basically how I edited the intro of this video is I'm just prompting. I'm literally just talking in a Claude chat. I'm like, hey, create a visual of this. For example, I want to have a movie director on the left-hand side. Claude has like a cape and he's flying and there's lights on him, right? You describe literally whatever it is that you want and Claude will use Hyperframes to build out the actual motion graphic and then use the Premiere Pro MCP to put it actually inside Premiere. Now, there's a couple of other tools and installations you need. Whisper X is the transcription tool that we're using to transcribe videos so that we can know how to cut them and where to cut them. So both of these free open source repos will be linked down in the description below. Now, let me explain how Hyperframes works. So you're like, ah, how does it generate these motion graphics, right? Are you generating the video or are you actually building the actual motion graphics, right? And what it's actually doing is actually building the motion graphics and you can think of it like this, you know, Claude is really good at building websites, right? We already know that it's really good at web design and coding. But a lot of the times where you're just using HTML, which is a coding language, a website building coding language to create, you know, things like websites. And so if I click here and if I go to this website, you can see it's animated, right? All of these animations and everything here. When I scroll, it gets larger, blah, blah, blah. These things fade in, they dissolve in, there's all these animations right here. And so that is how Claude is actually creating these motion graphics for me. It's just kind of building an HTML website that does that and has that animation. And then it's screen recording the website. So then capture that animation, turn it into a video and then, you know, put it in your Premiere Pro timeline or whichever editing software you're using. Now MCPs, how do we give Claude control over Premiere Pro? This is also pretty easy. It's pretty much just that GitHub repo that I mentioned before that has all the code and all the tools necessary. And it basically serves as this little connector right here. So you can, you know, plug Claude into Premiere. And now you can say things like, oh, Hey, like apply a transform effect and then like do all these key frames. And I'm like, damn, that actually looks good. Let's make it slightly less intense, right? So it's going to actually go into Premiere and put all the key frames in there. I would like to also mention that this also works with DaVinci Resolve Studio, okay? It has to be the paid studio version and it also works with Final Cut Pro. However, there has not been a CapCut one published yet. So to sum it up, really, this whole system is pretty much just a folder of files on your computer and it can generate motion graphics. It can control Premiere Pro or whatever other editing apps you need. And my specific folder has a bunch of prebuilt prompts, presets, and tools that are already coded in there. And it's a lot of the work is already done. It's already a full fully built out system so that you don't need to do all that work. You can think of it like an app except Claude is the app. So with all of that out of the way, I want to talk about now the two different ways that you can go about building this for yourself. Now, if you want, you can just get the paid version. It's inside my school community. Like I mentioned, I already built out all of this for you and it comes plug and play, you know, works right out of the box. And you also get the support of being inside my school community. So I have group calls, I can help you make it work. That'll be the first link in the description. So if you don't want to pay for it, that's totally fine. I'm going to show you how to build this for free right now in this video. You can definitely use the YouTube transcript. So take the transcript of this video, use that kind of like plug it into Claude, it'll help you build this as we go. Next, I'm going to do a live demo so you can actually see it in action and what that looks like. And then after that, we will get into the tutorial, the step by step of how you can build this. I'll see you there. All right, guys, so now I'm going to do a live demo of the Claude video editor in action so you guys can see it actually run. So basically what we're going to do is do a rough cut for the overview section of this video, which is the section that you just watched. So what I'm going to do is go and find her and select my raw footage. I think the raw footage is about like nine minutes long. So we're going to command option C to copy the file path, I'm going to paste in the file path so it knows where to find it. Or you can simply say, Hey, find the footage in my downloads folder. And then I'm going to give off a prompt, something like this, hey, I need you to do a rough cut for this raw footage. It's part of the Claude premiere project. Just put it in the timeline right after the intro section. And I also want you to cut it pretty hard. So I really want you to cut out everything that's not like absolutely essential. So cut it as much as you can only really keep the essential parts and just throw it in the premiere timeline. Go now. Okay, boom. So that's literally all I needed to say. And now I'm just going to let it run and come back when it's done. My guess is it'll probably take about 10 minutes. All right, guys. So that just finished and it took about 15 minutes. I think it spent a little bit of extra time, like verifying a couple of things. It did a pretty good rough cut. So it took it from a 10 minute long clip to a four minute long total thing. And it also applied some amplify and hard limiter preset thing that I have. So it already took care of the audio too, which is very, very nice. And that's pretty much the rough cut done. Now I don't need to really touch it at all. I can of course verify though, and make any extra changes that I want to hear if I want to drag some clips or adjust some things here, which is super, super nice in terms of flexibility. Okay, now I'm going to show you a quick demo of how we generate graphics. So as an example, I'm going to be trying to recreate this little graphic here of Mars Earth, we can open up Claude. And what we're going to do here is say, hey, I need you to create a graphic. So for the background, it's going to be like a off white, a little warmer grid background and it needs to be like grungy and pay and textured. And it needs to also be animated too. So maybe we can have like two different frames that it kind of goes back and forth between to give it the animated look. So that's for the background. So for the animation, we're going to have Mars, the planet pop, it's going to rise up to the center. And then the text is going to appear above it that says Mars. And then it's immediately going to slide to the left. And then earth is going to slide in, like slide in from the right. And then the text is going to pop, pop above it that says earth. And both of those need to be like actual images of the actual planets. I mean, I guess I can give you the PNGs, but I don't know. Just see if you can go and find those yourself. If not, it's fine. I'll give them to you. But immediately after that, earth is going to slide out to the right again, and then Mars is going to come back to center, get a little bit bigger. And under it, we're going to show, I think it's negative 153 degrees Celsius. And it needs to be in like a digital alarm clock font. I mean, obviously I could keep going, but I think for now, just for the purpose of this demo, I'm just going to show that one more thing is I'm going to say also there should be a slight shadow behind each planet object, of course. And obviously, you know, everything should be textured as much as you can with half tone or grunge, definitely for the background, it should be paper feel. And then for the frame rate, we'll go with eight FPS. So that's super important because that gives it that sort of feel and style and look to it. And one more thing I want to say here is, and so when you're done with this, just throw it in the graphics demo sequence so that I can view it. Okay, boom. So we're going to send off that prompt. I'm going to see how it does. And we'll see how long it takes. I'm going to start a timer. So I'm going to come back when this is done. Okay, boom. That just finished up. And it took a total of about 16 minutes and 45 seconds. And let's check it out. Mind you, I haven't done anything to it. I haven't watched it even yet. I just want to see just straight up how it looks out right out of the gate. Boom. Pretty cool, right? Pretty good, I'd say. I mean, if I want to tweak it further, I can. I would say that's already pretty good to go. So one more little extra cherry on top is that I'll put this adjustment layer over on top of it that I already have. So I can just copy and paste that in. I'm going to move this over on top like that. Okay, honestly, I think the grain is a little bit too much. So I'm going to tone that down to maybe just 30%. Yeah, bump that contrast up, tone down the exposure. Okay, again, let's just re-render everything. Alright. Dude, that's pretty good. I don't know, man. That's pretty good. Yeah, I mean, if I want to make any extra little changes to it, I totally can. I can, essentially, if I want to change anything, I can just prompt whatever changes I need. And it will do it pretty perfectly, but I'd say, honestly, this is good to go right off the bat. Like, there's really not much changes I would want to make, besides maybe making the minus 153 degrees Celsius like a little bit smaller. But honestly, I mean, it's pretty much a perfect copy. Like, the YouTube viewer isn't going to notice the small little extra details. This is already good as is, right? It gets the job done. It even pulled the pictures of Earth and Mars, which is pretty damn cool, right? And it cut them out perfectly. This looks amazing. This is pretty much first try. So that's how you do the graphics. And that was basically just the entire process that I used to craft the entire intro of this YouTube video. I just literally just prompted it and told it what I wanted it to do, and it was able to build it for me. And honestly, guys, this would have taken like hours and hours. I don't even know how to do this on my own. A, it does it autonomously. So I can literally just scroll my phone or do literally or work on whatever else I want to work on while this is going. B, it does it way faster than if I were to do it myself. I would have had to go into After Effects, do all the keyframes and all that. I don't even know how to do that, right? So I would say this is a massive, massive time save and effort save to get really high quality looking graphics. So that's how you create graphics. And that's what I did to make the entire intro of this YouTube video. So guys, if you want, you can join my school first link down in the description below and go to the classroom, go here and just download the project folder. And inside of that project folder, I have everything already pre built out for you. So if you look in here, it's going to have all the skills like these. It's going to have all the hyper frame stuff already installed. It's going to have the Premiere Pro MCP already installed and all of the graphics presets and everything and all the knowledge and time that I took to build out this entire system is already all going to be in there pretty much ready to go right out of the box. Not only do you get the files and everything pre built, but you also get all of the other assets, projects, workflows, automations that I have inside my school community, everything to do from content creation to even just the basics of cloud code and learning how to do that to finance. And there's group calls twice a week. So if you run into any issues, you can come talk to me in person, I'll help you solve it or I'll help you get it installed. And you can post in the community if you run into any issues. And I respond to these every single day with a full loom video. But anyways, guys, with that shameless plug out of the way, let me get into the free way to do this. So let's actually go through the tutorial of building this for free. Okay, so the first step is to go in finder, go wherever you keep all of your cloud projects, create a new folder, I'm going to name this video, editor, demo, build, okay. And just make sure you have that new folder, and then go here and Claude click open folder, we are going to go in our projects, and we are going to open that new blank folder that we just created. And now what I would do is take the transcript of this YouTube video, and literally just paste in the transcript, and then enter a few lines. So paste the transcript of this YouTube video, right? The one that you're watching right now, because then it'll it just has everything about how to build this and then just say, help me, no, not even help me, build all of this, do not stop until you're done. Go now, make sure bypass permissions is on. And then just let that run, that's probably going to get the scaffolding. Maybe like 60% of the way there, that's pretty much what I would do to build this yourself from there, you just kind of have to prompt back and forth until you get it doing what you need. Obviously, you can copy and paste both of the links to the GitHub repos and paste them in here. Or if you're on, for example, DaVinci resolve, you can search for the DaVinci resolve MCP and copy and paste this one. Or if you're on Final Cut Pro, you can do the same Final Cut Pro MCP, and then copy and paste this one in there to get it working with your specific application, whatever you have. But honestly, guys, to build it yourself for free, that's really, that's really all there is to it. I mean, if you just paste in the transcript of this YouTube video, Claude will pretty much have all the knowledge it needs to build out this entire thing. It just will be missing all of the signature editing style and presets and common gotchas and all of the infrastructure that I spent time weeks crafting custom building. And it obviously will take it'll probably take you I'd say two to five hours to get it working like fully, fully well. So again, guys, if you just want something that works right out of the box, join my school community first link down in the description, okay, now I'm just going to give you some final notes and thoughts about this whole project. So let's zoom out on a larger picture, grand grand scheme of things, what does this really mean for video editors and content creators? Well, if you're a video editor, then I definitely think that you should be using AI to power up your workflow, because this is going to help you work faster and better, right? If you're a content creator, and you're looking to quote unquote, replace a video editor, I think this will definitely help. Here's the biggest concept that I want to stress about this entire project Claude video editor does not replace creativity. Okay, the only reason that the intro of this video that you watched was so good was because I came up with the ideas of what to do for the graphics, right? I prompted it and said, Hey, let's do a flying arrow that like flies around it, then it hits this, and then there's like an image of this, right? That takes creativity. If you say, all right, Claude, edit this video for me, make it good. It's just not going to do it that well, right? I had to go and actually research, okay, you know, eight frames per second, half tone, grunge texture, paper animations, paper, rip animations, Vox style, putting grain overlay, you know, all these creative things that add to the style of the video. And so what this project really means for video editors and content creators is that it's replacing the execution, the one plus one technical aspects of video editing, right? No longer do you need to know how to do keyframes or know how to apply effects or do the technical things of coding or building the actual motion graphics and stuff like that, because that's the code part of it, right? So it can do anything that you want it to do, but you have to actually have the creativity to come up with the ideas. What this means is that we as content creators and video editors, we are no longer limited by technical knowledge, right? Now if I want to create a motion graphic, I can create literally whatever motion graphic I want in any style that I want all that the only limiting factor now is my creativity and my ability to prompt well, and actually, here's a really good comparison, okay? It's like software engineers. So people that know how to code and know how to build websites and apps are much better at vibe coding than people who don't, because they actually know the ins and outs and the high level creative aspects of building an app, right? A software engineer who is very skilled is going to be able to prompt AI and build a better app than someone who doesn't. It's the same way that if you are a content creator already or a really good video editor already, you're probably going to be able to use this project a lot more effectively than someone who doesn't, because you already have the skills and the creativity and the knowledge of how to video edit. This is just cutting the time and effort that it takes to, like I said before, bring your ideas to life. Now, can you use it to outsource and replace your own creativity? Sure. If you're not a very creative person, then I guess you could just be like, hey, Claude, edit this video for me. It'll do an okay job. It'll do some graphics that are kind of basic, kind of like meh. The worst thing to do, guys, and I see people get frustrated with this a lot. They're like, well, it didn't do a good job. No, you are lazy and you didn't come up with any ideas and you're trying to outsource creativity to the AI, which is the worst thing that AI is good for. AI is good at the technical one plus one busy work stuff. That's what it should be used for, not creativity. Your ideas are the highest leverage that you have left. All the AI is doing is giving you the power to, if you have an idea, boom, it's done. So that's how you should look at this project. It's not replacing your creativity. It's replacing the busy work of actually taking your idea and bringing it to life on the screen. That's my final thoughts and how you should look at this and how you should look at AI in general. I'm going to plug my school one more time. Would love to see you in here. If you're a content creator or a video editor, you don't want to get replaced by AI and you want to learn about this stuff and you want to learn how to leverage it to create more content, create better content, scale your business, then definitely join the school community. There's also a classroom. There's Claude code for dummies. So if you're just getting started with AI or Claude, then this will have you covered. I have an entire content system. I have a finance system. I have the video editor along with a bunch of extra miscellaneous stuff. And like I said, there's group calls twice a week. I'm literally about a hop on one right after this video in like two hours and speak live to all the community members. And honestly, guys, not that many people joined. So you can get one on one time with me. If you join the community, I will help you and coach you one on one or just give you whatever my two cents on whatever you're working on. Right? So we'd love to see you in here. That's going to conclude this video. I hope you guys got value out of it. I will see you in the next one. Peace.

## Timestamped

`[00:00]` What you're watching right now, every cut, every transition, and every graphic was done
`[00:06]` by Claude within Premiere Pro.
`[00:09]` Claude opened up Premiere Pro, cut together all of the footage, generated all of the graphics,
`[00:15]` and actually edited this entire video.
`[00:18]` And I'll let you be the judge of how well it did.
`[00:20]` But honestly guys, I think that this is just the beginning.
`[00:23]` I think that this is the future of where video editing is headed.
`[00:28]` I believe that you don't need to know how to do keyframes.
`[00:30]` You don't need to know what an adjustment layer is anymore.
`[00:32]` You don't need to know any of the technical aspects of things because that is being essentially
`[00:37]` replaced by AI.
`[00:38]` And now we can just focus on the creative aspects of creating content.
`[00:42]` And again, guys, I just want to remind you that everything you've seen so far has been
`[00:46]` edited using the exact system that I'm about to show you in this video right now.
`[00:50]` So without further ado, let's get into the tutorial.
`[00:53]` All right, guys.
`[00:54]` So before we get into the nitty gritty of the video, I'm going to quickly go over an
`[00:59]` overview of this entire project.
`[01:01]` Now, if you want to skip this part, you totally can.
`[01:04]` You can skip to the demo or you can skip to the tutorial section if you just want to
`[01:06]` get it straight into it.
`[01:08]` Okay, so basically what this project is that I've been working on and how I actually
`[01:12]` edited the intro that you just saw was with this project folder.
`[01:16]` It's pretty much just a Claude project that lives on my computer.
`[01:19]` So it's a folder of files.
`[01:22]` You can see all these files and that is how it's able to edit videos.
`[01:25]` I had to custom build a lot of this stuff.
`[01:27]` You can see this is what it looks like on my computer and this is what it looks like
`[01:29]` when you're in a Claude chat.
`[01:31]` Now, it's really built upon two core engines here.
`[01:33]` We have Hyperframes and we have the Premiere Pro MCP.
`[01:38]` So Hyperframes is how it's actually able to generate the motion graphics.
`[01:42]` And then the Premiere Pro MCP is how we connect up the Claude app to our Premiere
`[01:47]` Pro.
`[01:48]` Basically how I edited the intro of this video is I'm just prompting.
`[01:50]` I'm literally just talking in a Claude chat.
`[01:52]` I'm like, hey, create a visual of this.
`[01:54]` For example, I want to have a movie director on the left-hand side.
`[01:57]` Claude has like a cape and he's flying and there's lights on him, right?
`[02:00]` You describe literally whatever it is that you want and Claude will use Hyperframes
`[02:04]` to build out the actual motion graphic and then use the Premiere Pro MCP to put it actually
`[02:10]` inside Premiere.
`[02:11]` Now, there's a couple of other tools and installations you need.
`[02:14]` Whisper X is the transcription tool that we're using to transcribe videos so that
`[02:18]` we can know how to cut them and where to cut them.
`[02:21]` So both of these free open source repos will be linked down in the description below.
`[02:26]` Now, let me explain how Hyperframes works.
`[02:28]` So you're like, ah, how does it generate these motion graphics, right?
`[02:31]` Are you generating the video or are you actually building the actual motion graphics, right?
`[02:36]` And what it's actually doing is actually building the motion graphics and you can think of
`[02:40]` it like this, you know, Claude is really good at building websites, right?
`[02:43]` We already know that it's really good at web design and coding.
`[02:47]` But a lot of the times where you're just using HTML, which is a coding language, a website
`[02:51]` building coding language to create, you know, things like websites.
`[02:56]` And so if I click here and if I go to this website, you can see it's animated, right?
`[03:00]` All of these animations and everything here.
`[03:02]` When I scroll, it gets larger, blah, blah, blah.
`[03:04]` These things fade in, they dissolve in, there's all these animations right here.
`[03:08]` And so that is how Claude is actually creating these motion graphics for me.
`[03:12]` It's just kind of building an HTML website that does that and has that animation.
`[03:17]` And then it's screen recording the website.
`[03:19]` So then capture that animation, turn it into a video and then, you know, put it in your
`[03:24]` Premiere Pro timeline or whichever editing software you're using.
`[03:27]` Now MCPs, how do we give Claude control over Premiere Pro?
`[03:31]` This is also pretty easy.
`[03:32]` It's pretty much just that GitHub repo that I mentioned before that has all the code
`[03:37]` and all the tools necessary.
`[03:38]` And it basically serves as this little connector right here.
`[03:41]` So you can, you know, plug Claude into Premiere.
`[03:44]` And now you can say things like, oh, Hey, like apply a transform effect and then like
`[03:49]` do all these key frames.
`[03:51]` And I'm like, damn, that actually looks good.
`[03:52]` Let's make it slightly less intense, right?
`[03:54]` So it's going to actually go into Premiere and put all the key frames in there.
`[03:57]` I would like to also mention that this also works with DaVinci Resolve Studio, okay?
`[04:02]` It has to be the paid studio version and it also works with Final Cut Pro.
`[04:06]` However, there has not been a CapCut one published yet.
`[04:09]` So to sum it up, really, this whole system is pretty much just a folder of files on your
`[04:15]` computer and it can generate motion graphics.
`[04:18]` It can control Premiere Pro or whatever other editing apps you need.
`[04:22]` And my specific folder has a bunch of prebuilt prompts, presets, and tools that are already
`[04:27]` coded in there.
`[04:28]` And it's a lot of the work is already done.
`[04:30]` It's already a full fully built out system so that you don't need to do all that work.
`[04:34]` You can think of it like an app except Claude is the app.
`[04:38]` So with all of that out of the way, I want to talk about now the two different ways that
`[04:41]` you can go about building this for yourself.
`[04:43]` Now, if you want, you can just get the paid version.
`[04:46]` It's inside my school community.
`[04:47]` Like I mentioned, I already built out all of this for you and it comes plug and play,
`[04:52]` you know, works right out of the box.
`[04:54]` And you also get the support of being inside my school community.
`[04:57]` So I have group calls, I can help you make it work.
`[05:00]` That'll be the first link in the description.
`[05:01]` So if you don't want to pay for it, that's totally fine.
`[05:04]` I'm going to show you how to build this for free right now in this video.
`[05:08]` You can definitely use the YouTube transcript.
`[05:10]` So take the transcript of this video, use that kind of like plug it into Claude, it'll help
`[05:14]` you build this as we go.
`[05:16]` Next, I'm going to do a live demo so you can actually see it in action and what that
`[05:19]` looks like.
`[05:20]` And then after that, we will get into the tutorial, the step by step of how you can
`[05:23]` build this.
`[05:24]` I'll see you there.
`[05:25]` All right, guys, so now I'm going to do a live demo of the Claude video editor in
`[05:29]` action so you guys can see it actually run.
`[05:33]` So basically what we're going to do is do a rough cut for the overview section of this
`[05:37]` video, which is the section that you just watched.
`[05:39]` So what I'm going to do is go and find her and select my raw footage.
`[05:44]` I think the raw footage is about like nine minutes long.
`[05:47]` So we're going to command option C to copy the file path, I'm going to paste in the
`[05:52]` file path so it knows where to find it.
`[05:54]` Or you can simply say, Hey, find the footage in my downloads folder.
`[05:57]` And then I'm going to give off a prompt, something like this, hey, I need you to do
`[06:02]` a rough cut for this raw footage.
`[06:06]` It's part of the Claude premiere project.
`[06:08]` Just put it in the timeline right after the intro section.
`[06:11]` And I also want you to cut it pretty hard.
`[06:15]` So I really want you to cut out everything that's not like absolutely essential.
`[06:20]` So cut it as much as you can only really keep the essential parts and just throw it
`[06:25]` in the premiere timeline.
`[06:27]` Go now.
`[06:28]` Okay, boom.
`[06:29]` So that's literally all I needed to say.
`[06:31]` And now I'm just going to let it run and come back when it's done.
`[06:35]` My guess is it'll probably take about 10 minutes.
`[06:38]` All right, guys.
`[06:49]` So that just finished and it took about 15 minutes.
`[06:53]` I think it spent a little bit of extra time, like verifying a couple of things.
`[06:56]` It did a pretty good rough cut.
`[06:58]` So it took it from a 10 minute long clip to a four minute long total thing.
`[07:02]` And it also applied some amplify and hard limiter preset thing that I have.
`[07:09]` So it already took care of the audio too, which is very, very nice.
`[07:12]` And that's pretty much the rough cut done.
`[07:14]` Now I don't need to really touch it at all.
`[07:15]` I can of course verify though, and make any extra changes that I want to hear if I want
`[07:19]` to drag some clips or adjust some things here, which is super, super nice in terms
`[07:23]` of flexibility.
`[07:24]` Okay, now I'm going to show you a quick demo of how we generate graphics.
`[07:28]` So as an example, I'm going to be trying to recreate this little graphic here of
`[07:33]` Mars Earth, we can open up Claude.
`[07:37]` And what we're going to do here is say, hey, I need you to create a graphic.
`[07:41]` So for the background, it's going to be like a off white, a little warmer grid
`[07:47]` background and it needs to be like grungy and pay and textured.
`[07:52]` And it needs to also be animated too.
`[07:55]` So maybe we can have like two different frames that it kind of goes back and
`[07:58]` forth between to give it the animated look.
`[08:01]` So that's for the background.
`[08:02]` So for the animation, we're going to have Mars, the planet pop, it's going
`[08:09]` to rise up to the center.
`[08:11]` And then the text is going to appear above it that says Mars.
`[08:15]` And then it's immediately going to slide to the left.
`[08:17]` And then earth is going to slide in, like slide in from the right.
`[08:20]` And then the text is going to pop, pop above it that says earth.
`[08:23]` And both of those need to be like actual images of the actual planets.
`[08:27]` I mean, I guess I can give you the PNGs, but I don't know.
`[08:30]` Just see if you can go and find those yourself.
`[08:32]` If not, it's fine.
`[08:33]` I'll give them to you.
`[08:34]` But immediately after that, earth is going to slide out to the right
`[08:37]` again, and then Mars is going to come back to center, get a little bit bigger.
`[08:42]` And under it, we're going to show, I think it's negative 153 degrees Celsius.
`[08:49]` And it needs to be in like a digital alarm clock font.
`[08:53]` I mean, obviously I could keep going, but I think for now, just for the purpose of
`[08:57]` this demo, I'm just going to show that one more thing is I'm going to say also there
`[09:02]` should be a slight shadow behind each planet object, of course.
`[09:08]` And obviously, you know, everything should be textured as much as you can with half tone
`[09:13]` or grunge, definitely for the background, it should be paper feel.
`[09:17]` And then for the frame rate, we'll go with eight FPS.
`[09:20]` So that's super important because that gives it that sort of feel and style and look to
`[09:23]` it.
`[09:24]` And one more thing I want to say here is, and so when you're done with this, just throw
`[09:27]` it in the graphics demo sequence so that I can view it.
`[09:32]` Okay, boom.
`[09:33]` So we're going to send off that prompt.
`[09:34]` I'm going to see how it does.
`[09:36]` And we'll see how long it takes.
`[09:37]` I'm going to start a timer.
`[09:38]` So I'm going to come back when this is done.
`[09:40]` Okay, boom.
`[09:41]` That just finished up.
`[09:42]` And it took a total of about 16 minutes and 45 seconds.
`[09:48]` And let's check it out.
`[09:49]` Mind you, I haven't done anything to it.
`[09:51]` I haven't watched it even yet.
`[09:52]` I just want to see just straight up how it looks out right out of the gate.
`[10:05]` Boom.
`[10:06]` Pretty cool, right?
`[10:07]` Pretty good, I'd say.
`[10:08]` I mean, if I want to tweak it further, I can.
`[10:10]` I would say that's already pretty good to go.
`[10:12]` So one more little extra cherry on top is that I'll put this adjustment layer over
`[10:18]` on top of it that I already have.
`[10:20]` So I can just copy and paste that in.
`[10:22]` I'm going to move this over on top like that.
`[10:25]` Okay, honestly, I think the grain is a little bit too much.
`[10:28]` So I'm going to tone that down to maybe just 30%.
`[10:32]` Yeah, bump that contrast up, tone down the exposure.
`[10:36]` Okay, again, let's just re-render everything.
`[10:38]` Alright.
`[10:44]` Dude, that's pretty good.
`[10:46]` I don't know, man.
`[10:47]` That's pretty good.
`[10:48]` Yeah, I mean, if I want to make any extra little changes to it, I totally can.
`[10:52]` I can, essentially, if I want to change anything, I can just prompt whatever changes I need.
`[10:57]` And it will do it pretty perfectly, but I'd say, honestly, this is good to go right
`[11:02]` off the bat.
`[11:03]` Like, there's really not much changes I would want to make, besides maybe making
`[11:06]` the minus 153 degrees Celsius like a little bit smaller.
`[11:11]` But honestly, I mean, it's pretty much a perfect copy.
`[11:14]` Like, the YouTube viewer isn't going to notice the small little extra details.
`[11:20]` This is already good as is, right?
`[11:22]` It gets the job done.
`[11:23]` It even pulled the pictures of Earth and Mars, which is pretty damn cool, right?
`[11:27]` And it cut them out perfectly.
`[11:29]` This looks amazing.
`[11:30]` This is pretty much first try.
`[11:31]` So that's how you do the graphics.
`[11:33]` And that was basically just the entire process that I used to craft the entire intro of
`[11:39]` this YouTube video.
`[11:40]` I just literally just prompted it and told it what I wanted it to do, and it was able
`[11:44]` to build it for me.
`[11:45]` And honestly, guys, this would have taken like hours and hours.
`[11:48]` I don't even know how to do this on my own.
`[11:50]` A, it does it autonomously.
`[11:51]` So I can literally just scroll my phone or do literally or work on whatever else I want
`[11:55]` to work on while this is going.
`[11:57]` B, it does it way faster than if I were to do it myself.
`[12:00]` I would have had to go into After Effects, do all the keyframes and all that.
`[12:03]` I don't even know how to do that, right?
`[12:05]` So I would say this is a massive, massive time save and effort save to get really high
`[12:11]` quality looking graphics.
`[12:13]` So that's how you create graphics.
`[12:16]` And that's what I did to make the entire intro of this YouTube video.
`[12:19]` So guys, if you want, you can join my school first link down in the description below and
`[12:24]` go to the classroom, go here and just download the project folder.
`[12:29]` And inside of that project folder, I have everything already pre built out for you.
`[12:34]` So if you look in here, it's going to have all the skills like these.
`[12:38]` It's going to have all the hyper frame stuff already installed.
`[12:41]` It's going to have the Premiere Pro MCP already installed and all of the graphics presets
`[12:46]` and everything and all the knowledge and time that I took to build out this entire system
`[12:50]` is already all going to be in there pretty much ready to go right out of the box.
`[12:55]` Not only do you get the files and everything pre built, but you also get all of the
`[12:58]` other assets, projects, workflows, automations that I have inside my school community,
`[13:02]` everything to do from content creation to even just the basics of cloud code and learning
`[13:05]` how to do that to finance.
`[13:08]` And there's group calls twice a week.
`[13:09]` So if you run into any issues, you can come talk to me in person, I'll help you solve
`[13:12]` it or I'll help you get it installed.
`[13:14]` And you can post in the community if you run into any issues.
`[13:17]` And I respond to these every single day with a full loom video.
`[13:20]` But anyways, guys, with that shameless plug out of the way, let me get into the free
`[13:25]` way to do this.
`[13:26]` So let's actually go through the tutorial of building this for free.
`[13:29]` Okay, so the first step is to go in finder, go wherever you keep all of your cloud projects,
`[13:35]` create a new folder, I'm going to name this video, editor, demo, build, okay.
`[13:43]` And just make sure you have that new folder, and then go here and Claude click open folder,
`[13:48]` we are going to go in our projects, and we are going to open that new blank folder that
`[13:51]` we just created.
`[13:52]` And now what I would do is take the transcript of this YouTube video, and literally just paste
`[13:58]` in the transcript, and then enter a few lines.
`[14:01]` So paste the transcript of this YouTube video, right?
`[14:06]` The one that you're watching right now, because then it'll it just has everything about how
`[14:10]` to build this and then just say, help me, no, not even help me, build all of this,
`[14:17]` do not stop until you're done.
`[14:21]` Go now, make sure bypass permissions is on.
`[14:24]` And then just let that run, that's probably going to get the scaffolding.
`[14:28]` Maybe like 60% of the way there, that's pretty much what I would do to build this yourself
`[14:33]` from there, you just kind of have to prompt back and forth until you get it doing what
`[14:37]` you need.
`[14:38]` Obviously, you can copy and paste both of the links to the GitHub repos and paste them
`[14:43]` in here.
`[14:44]` Or if you're on, for example, DaVinci resolve, you can search for the DaVinci resolve MCP
`[14:52]` and copy and paste this one.
`[14:54]` Or if you're on Final Cut Pro, you can do the same Final Cut Pro MCP, and then copy
`[14:59]` and paste this one in there to get it working with your specific application, whatever you
`[15:04]` have.
`[15:05]` But honestly, guys, to build it yourself for free, that's really, that's really all there
`[15:09]` is to it.
`[15:10]` I mean, if you just paste in the transcript of this YouTube video, Claude will pretty much
`[15:14]` have all the knowledge it needs to build out this entire thing.
`[15:17]` It just will be missing all of the signature editing style and presets and common gotchas
`[15:23]` and all of the infrastructure that I spent time weeks crafting custom building.
`[15:28]` And it obviously will take it'll probably take you I'd say two to five hours to get
`[15:33]` it working like fully, fully well.
`[15:35]` So again, guys, if you just want something that works right out of the box, join my school
`[15:39]` community first link down in the description, okay, now I'm just going to give you some
`[15:42]` final notes and thoughts about this whole project.
`[15:44]` So let's zoom out on a larger picture, grand grand scheme of things, what does this
`[15:49]` really mean for video editors and content creators?
`[15:53]` Well, if you're a video editor, then I definitely think that you should be using AI to power
`[15:57]` up your workflow, because this is going to help you work faster and better, right?
`[16:03]` If you're a content creator, and you're looking to quote unquote, replace a video editor,
`[16:08]` I think this will definitely help.
`[16:11]` Here's the biggest concept that I want to stress about this entire project Claude video
`[16:15]` editor does not replace creativity.
`[16:19]` Okay, the only reason that the intro of this video that you watched was so good was because
`[16:25]` I came up with the ideas of what to do for the graphics, right?
`[16:30]` I prompted it and said, Hey, let's do a flying arrow that like flies around it, then it
`[16:35]` hits this, and then there's like an image of this, right?
`[16:38]` That takes creativity.
`[16:40]` If you say, all right, Claude, edit this video for me, make it good.
`[16:45]` It's just not going to do it that well, right?
`[16:48]` I had to go and actually research, okay, you know, eight frames per second, half tone, grunge
`[16:54]` texture, paper animations, paper, rip animations, Vox style, putting grain overlay, you know,
`[17:01]` all these creative things that add to the style of the video.
`[17:04]` And so what this project really means for video editors and content creators is that it's
`[17:08]` replacing the execution, the one plus one technical aspects of video editing, right?
`[17:15]` No longer do you need to know how to do keyframes or know how to apply effects or do the technical
`[17:21]` things of coding or building the actual motion graphics and stuff like that, because that's
`[17:26]` the code part of it, right?
`[17:28]` So it can do anything that you want it to do, but you have to actually have the creativity
`[17:35]` to come up with the ideas.
`[17:37]` What this means is that we as content creators and video editors, we are no longer limited
`[17:43]` by technical knowledge, right?
`[17:47]` Now if I want to create a motion graphic, I can create literally whatever motion graphic
`[17:52]` I want in any style that I want all that the only limiting factor now is my creativity
`[17:59]` and my ability to prompt well, and actually, here's a really good comparison, okay?
`[18:05]` It's like software engineers.
`[18:07]` So people that know how to code and know how to build websites and apps are much better
`[18:15]` at vibe coding than people who don't, because they actually know the ins and outs and the
`[18:22]` high level creative aspects of building an app, right?
`[18:26]` A software engineer who is very skilled is going to be able to prompt AI and build a
`[18:32]` better app than someone who doesn't.
`[18:35]` It's the same way that if you are a content creator already or a really good video editor
`[18:40]` already, you're probably going to be able to use this project a lot more effectively
`[18:45]` than someone who doesn't, because you already have the skills and the creativity and the
`[18:49]` knowledge of how to video edit.
`[18:52]` This is just cutting the time and effort that it takes to, like I said before, bring
`[18:56]` your ideas to life.
`[18:58]` Now, can you use it to outsource and replace your own creativity?
`[19:02]` Sure.
`[19:03]` If you're not a very creative person, then I guess you could just be like, hey, Claude,
`[19:07]` edit this video for me.
`[19:08]` It'll do an okay job.
`[19:10]` It'll do some graphics that are kind of basic, kind of like meh.
`[19:14]` The worst thing to do, guys, and I see people get frustrated with this a lot.
`[19:18]` They're like, well, it didn't do a good job.
`[19:22]` No, you are lazy and you didn't come up with any ideas and you're trying to outsource
`[19:28]` creativity to the AI, which is the worst thing that AI is good for.
`[19:33]` AI is good at the technical one plus one busy work stuff.
`[19:36]` That's what it should be used for, not creativity.
`[19:39]` Your ideas are the highest leverage that you have left.
`[19:42]` All the AI is doing is giving you the power to, if you have an idea, boom, it's done.
`[19:48]` So that's how you should look at this project.
`[19:50]` It's not replacing your creativity.
`[19:52]` It's replacing the busy work of actually taking your idea and bringing it to life
`[19:59]` on the screen.
`[20:00]` That's my final thoughts and how you should look at this and how you should look at AI
`[20:04]` in general.
`[20:05]` I'm going to plug my school one more time.
`[20:07]` Would love to see you in here.
`[20:08]` If you're a content creator or a video editor, you don't want to get replaced by AI and
`[20:12]` you want to learn about this stuff and you want to learn how to leverage it to create
`[20:14]` more content, create better content, scale your business, then definitely join the school
`[20:18]` community.
`[20:19]` There's also a classroom.
`[20:20]` There's Claude code for dummies.
`[20:21]` So if you're just getting started with AI or Claude, then this will have you covered.
`[20:25]` I have an entire content system.
`[20:27]` I have a finance system.
`[20:28]` I have the video editor along with a bunch of extra miscellaneous stuff.
`[20:31]` And like I said, there's group calls twice a week.
`[20:33]` I'm literally about a hop on one right after this video in like two hours and speak live
`[20:39]` to all the community members.
`[20:40]` And honestly, guys, not that many people joined.
`[20:42]` So you can get one on one time with me.
`[20:44]` If you join the community, I will help you and coach you one on one or just give
`[20:48]` you whatever my two cents on whatever you're working on.
`[20:51]` Right?
`[20:52]` So we'd love to see you in here.
`[20:53]` That's going to conclude this video.
`[20:54]` I hope you guys got value out of it.
`[20:55]` I will see you in the next one.
`[20:57]` Peace.
