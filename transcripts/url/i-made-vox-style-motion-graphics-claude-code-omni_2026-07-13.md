# I Made Vox-Style Motion Graphics Using Only Claude Code & Omni

- **URL:** https://www.youtube.com/watch?v=dqtfk8iINXI
- **Channel:** Matt Penny | Applied AI
- **Duration:** 12:57
- **Uploaded:** 2026-07-10
- **Pulled:** 2026-07-13 (yt-dlp auto-captions)

## Transcript (plain)

I just one-shotted this with AI. >> This ship has been at war for 260 years, and she's still in commission. Meet HMS Victory, 104 guns, 27 mi of rigging, 820 men crammed. >> So, today I'm going to show you how I created this Vox style video using GPT Image 2 and Google Omni. And I'm going to show you how you can create it, too. So, let's get into it. Okay. Okay, so the first thing we need to do in order to create a Vox style video is to define what a Vox style video is. We need to give uh Claude a load of information about what this actually means. Now, there are different ways that you can do this. The way that I did it was that I used Ampify to go and find a bunch of YouTube videos that talk about Vox's editing style and video production. I said perhaps 10 of them, then put them in a notebook, LM notebook, and then from that give me a comprehensive breakdown of what the editing style is. I found this is one of the best ways to do research. You could alternatively just go and take screenshots and ask it to like analyze it. But I used this method instead. So it created me a notebook that looked a little bit like this. You can see it pulled some sources and it created a notebook. And then I asked it to create me a comprehensive style prompt and an animation prompt because we're going to be doing two things here. We're going to be creating images and we're going to be prompting animations. We're going to be doing both of those things. And it went ahead and it made that style prompt and that animation prompt. Now, these prompts are part of the video production pipeline that I've created as well as a bunch of skills which basically fix problems that I came up against whilst building it. If you want access to this entire pipeline, so like the skills, the prompts, everything like that, then there's a link down below where you can download that absolutely for free. But here are my files. You can see I've got a folder called Vox video. And if I open that up, I've got a load of different information in there. And this is the main one here, the Vox sequential scene workflow. And if I open this up, you can see it basically gives the instructions of this entire video which I'm showing you. Now, what this allows you to do is create the video in one shot. You simply say create a video by X and it will create it. However, what I'm going to show you in this video is step by step. I'm going to show you the different steps so that if you want to create this yourself, then you can. Or if you want to be able to, you know, uh reverse engineer what I created. So, maybe you can like take parts of what I've done and apply it to your own project, then you can do that. Um, and also it provides a better result because you can check it at every step along the way rather than just saying, "Hey, create this and letting it do everything." But that is an option. So, let's hop into Claude and let's actually get started creating it. I'm going to use Fable 5. I'm within this folder. That's the same folder as linked down below. And I want to create a video about the HMS Victory. I'm a proud Brit. So, let's create it about that fine bit of British history. And I'm going to say, I want to create a Vox style video all about the HMS Victory. Please, can you create me a 30-cond script broken up into three chunks of 10 seconds or less? uh just give me the script for now. Okay. So um as I said it can do everything but I want to check in this pass through. So it's going to tell me what the script is going to be and then I can edit it because the script is what is going to guide everything. Okay. So here we are. Here are the three sections. They seem okay. They seem a little bit long and I need a little bit more punch. So I'm just going to say can we cut down the size of each one of these? You can rewrite it completely if you need to. Um, and also the first section, can we start it with like something a little bit more punchy, please? Always say pleased to AI. You never know when the AI overlords are going to come and uh they're going to remember who said please and who didn't. So, [laughter] let's see what we get after that. Okay, this ship has been at war for 260 years and still in commission. Meet HMS Victory. Yeah. Okay, that is much much better. Good. Okay, so now the next step is we were going to create the first image. Now let me talk about the tools that we're using here and the models. Um we're creating the first image so that we can feed that image into the video model which will produce the video. The image model that we're using is um OpenAI's image GPT image 2 which at the moment is the best image model out there. It's not that expensive either. And then we're using Google's Omni um as the video model. Now to create these images and videos I am connecting to Kai AI. I'm not connecting directly to OpenAI's API and to Google's API. Instead, I'm just doing it through one API. It just makes it easier as um you don't have to deal with a load of API keys and a load of, you know, making sure everything's got credits. Kai is good, equally good like foul and other things like that. In order to set this up, all that I did was to ask Claude to look over Kai's documentation and set up the API routes for Google Omni and for GPT2. Okay, so now we're back in Claude and I simply going to say, "Okay, that looks good. Please can you create me just the image um of the first scene? Okay. And we'll send that off. Now, if you are running this workflow, let me give you one little tip. Fable 5 is good and the claude models are good. They are incredibly slow. So, if you actually want to produce something quickly and like time is important, then don't use claude. Use something like codeex or use something like cursor or like the grock models. However, we are going to keep using claude. It is pretty good. Okay. So, I had to reset my EMV variable. But I've got that image. Let's have a look at it. So, here it is. That is pretty good. Now, part of what the prompt says is in the first image of the first video, don't put any overlays of any text or anything because we need to add that in later. Good. So, now I'm going to say now that I'm happy with that, if you are not happy with that, then you can obviously request any changes. It is far cheaper and quicker to request changes to images like this than it is to request changes to videos. So, if you've got changes to make, make it here. Cool. So, I'm going to say that looks good. Now, can you tell me the prompt that you're going to use to create the first video from this image? So, again, you can just run this through all the way without being involved, but because this is kind of like a little bit of a walk through and showing you how it works, I'm doing it step by step. Okay, so here we go. It's giving us the prompt for this first video and we can look it over just to make sure that we like um what it's going to show us. So, um let's see. As the narration says, at war for 260 years, a large stamp appears with 260 years. Yep. Still in commission. rack focus gently on the ship. The ship sharpens and lifts slightly in contrast with the sea. Okay. Yeah, that looks fine. I'm going to say great. Go ahead and create this first video clip for me and then show it to me. Don't create more videos after this. Okay. So, again, we're just doing this first video and then we're going to go on from that and create the the second videos. And essentially, I haven't said before, this 30 second long clip is going to be three separate videos which we're going to stitch together. Now, while that generates, if you are interested in creating content with AI for your business, for your marketing, whatever it may be, then inside the applied AI mastermind, I've got some assets which can be very useful. There's a full course all about AI content fundamentals, covering everything from image creation to um hyperframes. And actually, I give you my own software which I have built bespokely to edit my own videos, but essentially from creating videos, creating images, there's also a full course about hyperframes and how to use AI to edit videos for you. And this is just a small selection of what is included within the applied AI mastermind. You can see that what is inside is a selection of full-length courses on things from Claude and AI vibe coding, Hermes, AI marketing to how to generate leads, NAT, which is still a very important tool. But most importantly, there is the AI applied to business module, which is how to see the opportunities within your business or a client's business where you can actually use AI and apply it to a business so that the business can move forward. Whether that's in terms of sales and increasing topline or cutting costs and essentially improving the bottom line, we are seeing some great results inside the mastermind for some of our members. And there is a 14-day money back guarantee. So, you can join and if you don't like what you see, if it's not for you, absolutely fine. Just request your money back and there is zero risk. And also, we're about to increase the prices. So, if you want to join and potentially save a load of money, lock in your price, then you can join with the link down below in the description, and I'd love to see you inside. Anyway, let's get back to it. Okay, so this first scene is generated. Let's have a little look at it. >> This ship has been at war for 260 years, and she's still in commission. Meet HMS Victory. >> Okay, there we go. So, um, let's close that. And now what we're going to do within this process is that it's going to read, uh, in order to create the next video. So, we've got three videos stitched together. We will do um in order to create the first frame for the next video, we're going to take this last frame here. We're going to have AI look at it because what AI is going to do is it's going to look at this and then it's going to plan on the next things that should happen from this frame here. Because I've tried it before where you just ask it to create all the prompts without seeing what's happening. And because it can't see what's happening, it creates prompts which don't really make a lot of sense. So, what in fact we're going to do is feed it this last image here. It's going to use ffmpeg to strip it. It's going to analyze it. Um, and then it's then going to take this and be able to plan on the next steps. So, I'm going to say, great, use ffmpeg to do your process and look at the last frame of that video that we created. And then using that, please plan out the next video for us. Don't actually create it. Just tell me the prompt. Now, whilst we're waiting for this, I will mention that in the description below, I've got a list of free AI resources. If you're looking to help AI uh improve your business or clients businesses, then those might just help you, and they're free. So, go ahead, check them out. Great. Okay, so here is the second prompt. So, it's got some text in it. It's going to keep this text exactly the same, but it's going to render on some more text as well. Uh, no hard cuts. Um, the narration is going to say 104 guns while rough pencil circles are drawn around two or three gunports on the ship's hull. Okay, cool. Yeah, I'm not going to read through all of that. I'm just going to assume the fable has done a good job. And actually, I'm going to say that looks good. I want you to go ahead and just uh finish the entire process for me. So, create this second video and then um take the last frame of that and create the third video from that. And then go ahead and stitch all three of those videos together. I want you to just give me the finished video. So here we're going to use that automation process which is built into this sort of like skill or project that I've built where we can just say okay just go ahead and do it. And I've given it some detail here about what it should do. Um but that's only just to make sure it stays on track. I have described before what it needs to do. So it should it should know if I just say complete it that it just needs to complete it and do duh in order to get it working. So, it's going to take probably like 5 minutes for it to create um that image to create that video. Then strip the image, analyze the image, create the prompt, create the other video, stitch them all together. So, let's come back when that's done. Let's see how it fares. Okay, so it's come back all of those three scenes stitched together into one video. It's put them all together with FFmpeg. Let's have a little look and see what it looks like. >> This ship has been at war for 260 years, and she's still in commission. Meet HMS Victory 4 guns, 27 mi of rigging, 820 men crammed inside a floating fortress. Trafalgar 1805 Nelson's flagship shattered two fleets and he died on her deck victorious. >> There you go. Pretty good. There are definitely some things we could change and we could improve, but you know, it's pretty staggering what we can now create for, you know, about a dollar. Just a little over a dollar is what that costed. So, that's the entire process. The entire process is creating a script using the Vox style guide which we created via pulling it from a load of YouTube videos. Um, first creating the first image and then turning that first image into a video. And then we take the last frame of that video and use it as the first frame for the next video. And we do that for however many bits of video you want to create. I've just done three here, but you can do as many as you like. Then once all of those video files are created, in fact, let me show you all of those video files. So here we can see if we go in here we've got uh scene one, scene two, and scene three. And we've got their raw files as well. And simply they just stitched together using ffmpeg which is just how you manipulate video files or image files as well. Um and stitched it together into one video. Now we have gone through this step by step. But you can simply say create me a video about the Napoleonic War or whatever it is you want to create a video about. walk away for 10 minutes and come back and it will create you a video 30 seconds long or 3 minutes long or 30 minutes long, however long you want. So, there we go. I hope you have found this useful. If you do want kind like the file that I used and the skill that I used, the project that I used to create this with all the prompts and all the star guides and everything like that, then I'll leave that down below in the description. All you need to do is add your own API key for Kai or FAL or whichever one you want to use. is about applying AI to your business, creating content with AI or generally improving your business with AI with PRM strategies, then do check out the applied AI mastermind which will be linked down below in the description. Found this video interesting? Then please do give it a like, subscribe if you want to see more videos like this and I would highly recommend going and watching this video next. I think you'll find it very interesting. in the next video.

## Transcript (timestamped)

[00:00] I just one-shotted this with AI.
[00:02] >> This ship has been at war for 260 years,
[00:06] and she's still in commission. Meet HMS
[00:09] Victory, 104 guns,
[00:12] 27 mi of rigging, 820 men crammed.
[00:16] >> So, today I'm going to show you how I
[00:17] created this Vox style video using GPT
[00:19] Image 2 and Google Omni. And I'm going
[00:22] to show you how you can create it, too.
[00:24] So, let's get into it. Okay. Okay, so
[00:26] the first thing we need to do in order
[00:27] to create a Vox style video is to define
[00:30] what a Vox style video is. We need to
[00:32] give uh Claude a load of information
[00:34] about what this actually means. Now,
[00:36] there are different ways that you can do
[00:37] this. The way that I did it was that I
[00:40] used Ampify to go and find a bunch of
[00:43] YouTube videos that talk about Vox's
[00:45] editing style and video production. I
[00:47] said perhaps 10 of them, then put them
[00:49] in a notebook, LM notebook, and then
[00:51] from that give me a comprehensive
[00:52] breakdown of what the editing style is.
[00:54] I found this is one of the best ways to
[00:56] do research. You could alternatively
[00:58] just go and take screenshots and ask it
[01:00] to like analyze it. But I used this
[01:02] method instead. So it created me a
[01:05] notebook that looked a little bit like
[01:06] this. You can see it pulled some sources
[01:08] and it created a notebook. And then I
[01:09] asked it to create me a comprehensive
[01:11] style prompt and an animation prompt
[01:13] because we're going to be doing two
[01:14] things here. We're going to be creating
[01:15] images and we're going to be prompting
[01:17] animations. We're going to be doing both
[01:19] of those things. And it went ahead and
[01:21] it made that style prompt and that
[01:23] animation prompt. Now, these prompts are
[01:25] part of the video production pipeline
[01:27] that I've created as well as a bunch of
[01:28] skills which basically fix problems that
[01:30] I came up against whilst building it. If
[01:32] you want access to this entire pipeline,
[01:34] so like the skills, the prompts,
[01:35] everything like that, then there's a
[01:36] link down below where you can download
[01:37] that absolutely for free. But here are
[01:39] my files. You can see I've got a folder
[01:41] called Vox video. And if I open that up,
[01:42] I've got a load of different information
[01:44] in there. And this is the main one here,
[01:45] the Vox sequential scene workflow. And
[01:48] if I open this up, you can see it
[01:50] basically gives the instructions of this
[01:52] entire video which I'm showing you. Now,
[01:53] what this allows you to do is create the
[01:55] video in one shot. You simply say create
[01:58] a video by X and it will create it.
[01:59] However, what I'm going to show you in
[02:00] this video is step by step. I'm going to
[02:02] show you the different steps so that if
[02:03] you want to create this yourself, then
[02:05] you can. Or if you want to be able to,
[02:06] you know, uh reverse engineer what I
[02:08] created. So, maybe you can like take
[02:09] parts of what I've done and apply it to
[02:11] your own project, then you can do that.
[02:13] Um, and also it provides a better result
[02:15] because you can check it at every step
[02:16] along the way rather than just saying,
[02:17] "Hey, create this and letting it do
[02:19] everything." But that is an option. So,
[02:22] let's hop into Claude and let's actually
[02:23] get started creating it. I'm going to
[02:25] use Fable 5. I'm within this folder.
[02:28] That's the same folder as linked down
[02:29] below. And I want to create a video
[02:31] about the HMS Victory. I'm a proud Brit.
[02:34] So, let's create it about that fine bit
[02:35] of British history. And I'm going to
[02:37] say, I want to create a Vox style video
[02:39] all about the HMS Victory. Please, can
[02:42] you create me a 30-cond script broken up
[02:45] into three chunks of 10 seconds or less?
[02:48] uh just give me the script for now.
[02:52] Okay. So um as I said it can do
[02:54] everything but I want to check in this
[02:56] pass through. So it's going to tell me
[02:57] what the script is going to be and then
[02:59] I can edit it because the script is what
[03:00] is going to guide everything. Okay. So
[03:02] here we are. Here are the three
[03:04] sections. They seem okay. They seem a
[03:06] little bit long and I need a little bit
[03:08] more punch. So I'm just going to say can
[03:12] we cut down the size of each one of
[03:13] these? You can rewrite it completely if
[03:16] you need to. Um, and also the first
[03:18] section, can we start it with like
[03:19] something a little bit more punchy,
[03:21] please?
[03:22] Always say pleased to AI. You never know
[03:24] when the AI overlords are going to come
[03:26] and uh they're going to remember who
[03:27] said please and who didn't. So,
[03:28] [laughter]
[03:29] let's see what we get after that. Okay,
[03:32] this ship has been at war for 260 years
[03:34] and still in commission. Meet HMS
[03:36] Victory. Yeah. Okay, that is much much
[03:38] better. Good. Okay, so now the next step
[03:40] is we were going to create the first
[03:43] image. Now let me talk about the tools
[03:44] that we're using here and the models. Um
[03:47] we're creating the first image so that
[03:49] we can feed that image into the video
[03:50] model which will produce the video. The
[03:52] image model that we're using is um
[03:54] OpenAI's image GPT image 2 which at the
[03:57] moment is the best image model out
[03:59] there. It's not that expensive either.
[04:01] And then we're using Google's Omni um as
[04:04] the video model. Now to create these
[04:05] images and videos I am connecting to Kai
[04:08] AI. I'm not connecting directly to
[04:10] OpenAI's API and to Google's API.
[04:12] Instead, I'm just doing it through one
[04:14] API. It just makes it easier as um you
[04:16] don't have to deal with a load of API
[04:17] keys and a load of, you know, making
[04:19] sure everything's got credits. Kai is
[04:20] good, equally good like foul and other
[04:23] things like that. In order to set this
[04:24] up, all that I did was to ask Claude to
[04:26] look over Kai's documentation and set up
[04:28] the API routes for Google Omni and for
[04:31] GPT2. Okay, so now we're back in Claude
[04:33] and I simply going to say, "Okay, that
[04:35] looks good. Please can you create me
[04:37] just the image um of the first scene?
[04:42] Okay. And we'll send that off. Now, if
[04:44] you are running this workflow, let me
[04:45] give you one little tip. Fable 5 is good
[04:47] and the claude models are good. They are
[04:49] incredibly slow. So, if you actually
[04:51] want to produce something quickly and
[04:52] like time is important, then don't use
[04:55] claude. Use something like codeex or use
[04:57] something like cursor or like the grock
[04:59] models. However, we are going to keep
[05:00] using claude. It is pretty good. Okay.
[05:02] So, I had to reset my EMV variable. But
[05:04] I've got that image. Let's have a look
[05:05] at it. So, here it is. That is pretty
[05:08] good. Now, part of what the prompt says
[05:10] is in the first image of the first
[05:12] video, don't put any overlays of any
[05:15] text or anything because we need to add
[05:16] that in later. Good. So, now I'm going
[05:19] to say now that I'm happy with that, if
[05:20] you are not happy with that, then you
[05:22] can obviously request any changes. It is
[05:23] far cheaper and quicker to request
[05:26] changes to images like this than it is
[05:28] to request changes to videos. So, if
[05:30] you've got changes to make, make it
[05:31] here. Cool. So, I'm going to say that
[05:33] looks good. Now, can you tell me the
[05:35] prompt that you're going to use to
[05:36] create the first video from this image?
[05:39] So, again, you can just run this through
[05:40] all the way without being involved, but
[05:42] because this is kind of like a little
[05:43] bit of a walk through and showing you
[05:44] how it works, I'm doing it step by step.
[05:46] Okay, so here we go. It's giving us the
[05:48] prompt for this first video and we can
[05:49] look it over just to make sure that we
[05:51] like um what it's going to show us. So,
[05:54] um let's see. As the narration says, at
[05:57] war for 260 years, a large stamp appears
[05:59] with 260 years. Yep. Still in
[06:01] commission. rack focus gently on the
[06:03] ship. The ship sharpens and lifts
[06:05] slightly in contrast with the sea. Okay.
[06:07] Yeah, that looks fine. I'm going to say
[06:09] great. Go ahead and create this first
[06:12] video clip for me and then show it to
[06:15] me. Don't create more videos after this.
[06:17] Okay. So, again, we're just doing this
[06:19] first video and then we're going to go
[06:20] on from that and create the the second
[06:21] videos. And essentially, I haven't said
[06:23] before, this 30 second long clip is
[06:24] going to be three separate videos which
[06:26] we're going to stitch together. Now,
[06:28] while that generates, if you are
[06:29] interested in creating content with AI
[06:32] for your business, for your marketing,
[06:33] whatever it may be, then inside the
[06:35] applied AI mastermind, I've got some
[06:36] assets which can be very useful. There's
[06:38] a full course all about AI content
[06:40] fundamentals, covering everything from
[06:42] image creation to um hyperframes. And
[06:45] actually, I give you my own software
[06:46] which I have built bespokely to edit my
[06:49] own videos, but essentially from
[06:50] creating videos, creating images,
[06:52] there's also a full course about
[06:53] hyperframes and how to use AI to edit
[06:55] videos for you. And this is just a small
[06:57] selection of what is included within the
[06:59] applied AI mastermind. You can see that
[07:01] what is inside is a selection of
[07:03] full-length courses on things from
[07:05] Claude and AI vibe coding, Hermes, AI
[07:08] marketing to how to generate leads, NAT,
[07:10] which is still a very important tool.
[07:12] But most importantly, there is the AI
[07:14] applied to business module, which is how
[07:16] to see the opportunities within your
[07:18] business or a client's business where
[07:19] you can actually use AI and apply it to
[07:22] a business so that the business can move
[07:24] forward. Whether that's in terms of
[07:26] sales and increasing topline or cutting
[07:28] costs and essentially improving the
[07:30] bottom line, we are seeing some great
[07:32] results inside the mastermind for some
[07:34] of our members. And there is a 14-day
[07:36] money back guarantee. So, you can join
[07:38] and if you don't like what you see, if
[07:40] it's not for you, absolutely fine. Just
[07:42] request your money back and there is
[07:44] zero risk. And also, we're about to
[07:46] increase the prices. So, if you want to
[07:48] join and potentially save a load of
[07:50] money, lock in your price, then you can
[07:52] join with the link down below in the
[07:54] description, and I'd love to see you
[07:55] inside. Anyway, let's get back to it.
[07:57] Okay, so this first scene is generated.
[07:58] Let's have a little look at it.
[08:00] >> This ship has been at war for 260 years,
[08:04] and she's still in commission. Meet HMS
[08:07] Victory.
[08:08] >> Okay, there we go. So, um, let's close
[08:11] that. And now what we're going to do
[08:12] within this process is that it's going
[08:14] to read, uh, in order to create the next
[08:16] video. So, we've got three videos
[08:17] stitched together. We will do um in
[08:20] order to create the first frame for the
[08:22] next video, we're going to take this
[08:24] last frame here. We're going to have AI
[08:25] look at it because what AI is going to
[08:27] do is it's going to look at this and
[08:28] then it's going to plan on the next
[08:30] things that should happen from this
[08:32] frame here. Because I've tried it before
[08:34] where you just ask it to create all the
[08:36] prompts without seeing what's happening.
[08:38] And because it can't see what's
[08:39] happening, it creates prompts which
[08:41] don't really make a lot of sense. So,
[08:43] what in fact we're going to do is feed
[08:44] it this last image here. It's going to
[08:47] use ffmpeg to strip it. It's going to
[08:49] analyze it. Um, and then it's then going
[08:51] to take this and be able to plan on the
[08:53] next steps. So, I'm going to say, great,
[08:56] use ffmpeg to do your process and look
[08:58] at the last frame of that video that we
[09:00] created. And then using that, please
[09:02] plan out the next video for us. Don't
[09:04] actually create it. Just tell me the
[09:06] prompt. Now, whilst we're waiting for
[09:07] this, I will mention that in the
[09:08] description below, I've got a list of
[09:10] free AI resources. If you're looking to
[09:12] help AI uh improve your business or
[09:14] clients businesses, then those might
[09:16] just help you, and they're free. So, go
[09:17] ahead, check them out. Great. Okay, so
[09:19] here is the second prompt. So, it's got
[09:22] some text in it. It's going to keep this
[09:24] text exactly the same, but it's going to
[09:26] render on some more text as well. Uh, no
[09:28] hard cuts. Um, the narration is going to
[09:31] say 104 guns while rough pencil circles
[09:34] are drawn around two or three gunports
[09:36] on the ship's hull. Okay, cool. Yeah,
[09:39] I'm not going to read through all of
[09:39] that. I'm just going to assume the fable
[09:41] has done a good job. And actually, I'm
[09:43] going to say that looks good. I want you
[09:45] to go ahead and just uh finish the
[09:46] entire process for me. So, create this
[09:48] second video and then um take the last
[09:51] frame of that and create the third video
[09:54] from that. And then go ahead and stitch
[09:56] all three of those videos together. I
[09:58] want you to just give me the finished
[10:00] video. So here we're going to use that
[10:02] automation process which is built into
[10:04] this sort of like skill or project that
[10:05] I've built where we can just say okay
[10:07] just go ahead and do it. And I've given
[10:09] it some detail here about what it should
[10:11] do. Um but that's only just to make sure
[10:13] it stays on track. I have described
[10:15] before what it needs to do. So it should
[10:16] it should know if I just say complete it
[10:19] that it just needs to complete it and do
[10:21] duh in order to get it working. So, it's
[10:23] going to take probably like 5 minutes
[10:26] for it to create um that image to create
[10:28] that video. Then strip the image,
[10:30] analyze the image, create the prompt,
[10:31] create the other video, stitch them all
[10:33] together. So, let's come back when
[10:34] that's done. Let's see how it fares.
[10:36] Okay, so it's come back all of those
[10:38] three scenes stitched together into one
[10:40] video. It's put them all together with
[10:41] FFmpeg. Let's have a little look and see
[10:42] what it looks like.
[10:44] >> This ship has been at war for 260 years,
[10:47] and she's still in commission. Meet HMS
[10:51] Victory
[10:52] 4 guns,
[10:54] 27 mi of rigging, 820 men crammed inside
[10:58] a floating fortress. Trafalgar 1805
[11:02] Nelson's flagship shattered two fleets
[11:05] and he died on her deck victorious.
[11:07] >> There you go. Pretty good. There are
[11:08] definitely some things we could change
[11:10] and we could improve, but you know, it's
[11:13] pretty staggering what we can now create
[11:15] for, you know, about a dollar. Just a
[11:17] little over a dollar is what that
[11:18] costed. So, that's the entire process.
[11:20] The entire process is creating a script
[11:22] using the Vox style guide which we
[11:24] created via pulling it from a load of
[11:26] YouTube videos. Um, first creating the
[11:29] first image and then turning that first
[11:31] image into a video. And then we take the
[11:33] last frame of that video and use it as
[11:35] the first frame for the next video. And
[11:37] we do that for however many bits of
[11:38] video you want to create. I've just done
[11:39] three here, but you can do as many as
[11:41] you like. Then once all of those video
[11:44] files are created, in fact, let me show
[11:45] you all of those video files. So here we
[11:48] can see if we go in here we've got uh
[11:50] scene one, scene two, and scene three.
[11:52] And we've got their raw files as well.
[11:54] And simply they just stitched together
[11:55] using ffmpeg which is just how you
[11:57] manipulate video files or image files as
[12:00] well. Um and stitched it together into
[12:02] one video. Now we have gone through this
[12:04] step by step. But you can simply say
[12:06] create me a video about the Napoleonic
[12:08] War or whatever it is you want to create
[12:10] a video about. walk away for 10 minutes
[12:12] and come back and it will create you a
[12:13] video 30 seconds long or 3 minutes long
[12:16] or 30 minutes long, however long you
[12:18] want. So, there we go. I hope you have
[12:19] found this useful. If you do want kind
[12:21] like the file that I used and the skill
[12:23] that I used, the project that I used to
[12:24] create this with all the prompts and all
[12:26] the star guides and everything like
[12:27] that, then I'll leave that down below in
[12:29] the description. All you need to do is
[12:30] add your own API key for Kai or FAL or
[12:34] whichever one you want to use. is about
[12:35] applying AI to your business, creating
[12:37] content with AI or generally improving
[12:39] your business with AI with PRM
[12:41] strategies, then do check out the
[12:42] applied AI mastermind which will be
[12:43] linked down below in the description.
[12:45] Found this video interesting? Then
[12:47] please do give it a like, subscribe if
[12:49] you want to see more videos like this
[12:51] and I would highly recommend going and
[12:52] watching this video next. I think you'll
[12:55] find it very interesting. in the next
[12:56] video.
