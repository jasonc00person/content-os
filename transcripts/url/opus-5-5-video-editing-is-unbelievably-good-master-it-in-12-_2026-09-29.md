# Opus 5.5 Video Editing is Unbelievably Good (master it in 12 mins)

- **Source:** https://www.youtube.com/watch?v=YKFpSe28mlg
- **Uploader:** Jay E | RoboNuggets
- **Uploaded:** 2026-09-29
- **Duration:** 12:54
- **Detected language:** en (p=1.00)
- **Model:** small.en

## Transcript

Opus 5.5 for video editing and motion graphics has gotten pretty unbelievable lately. And so these examples that you'll see are all created with Opus, and all I did is to give it access to my workspace, no generative AI video model was used, and I just sent a simple prompt like this where I asked it to make a dynamic motion graphics video that showcases its capabilities. This is another similar example, but where I pushed it to use more 3D elements. And in fact, some of the videos I launched recently, like this one that already has 300,000 views, it was also edited using Opus 5.5. So Opus 5.5 just came out and Antropic just published an official comprehensive guide on how to prompt it. You can keep one agents.md as your single instructions file now instead of keeping a claw.md and an agents.md in sync. One of the best things you can do is to ask for them in the SVG format. That stands for Scalable Vector Graphics, so that it scales to any size without going blurry. You can open the file and change a color by hand, and you can even have Claude animate these icons. So with SVGs, every graphic that you get back from Claude is editable and animatable. So clearly, I've been testing this model heavily for automated videos, and in my view, these are all a major step up versus what we had previously. So today, I'll teach you how to best use this capability of 5.5 so that by the end of it, you can also level up your video and motion graphics skills using AI. I know exactly how I make videos like these that get hundreds of thousands of views, even if they are AI edited. And if you're new, my name is Jay. I spent over a decade working with brands you probably know. I've been in AI since my masters in data science, and now I'm leading our AI business in one of the largest AI communities globally. Let's dive into it. So before we go into the different levels by which you can use Opus's capability for video editing, I actually want to give you context of what really happens under the hood when you send a simple prompt like this to 5.5. Because as I mentioned earlier, this whole video that it created for us, it didn't really use any generative AI video model for it. All of the movements, all of the text, and basically everything you see here, those are all created using code. And in fact, in this demo interface, you can clearly see I can select these individual elements which are all just images in my workspace. And all they are really is Claude pointing to this particular photo in this case, and using some code, in this case, JavaScript in order to place them in this exact position, in this exact timestamp. And everything that you see here, including the movements, the motion graphics, that is all using Opus 5.5's taste. And if you're curious exactly what tools it used to achieve that video, I also just asked Opus to illustrate that here in Excalidraw. And you can see that with that one-shot prompt that we sent it, it just used its native knowledge of HTML, CSS, JavaScript, and a couple of other libraries like 3JS and FFmpeg in order to achieve that look. Which again, you don't even need to understand all of this, although in my view, it's at least good to be aware of them. But because of how powerful these models have become, you can pretty much just rely on 5.5 to create you create showreels like that using a single prompt. I did want to call out though, that for this particular test, we did not use hyperframes or remotion, which are these popular open source libraries for video editing using Claude, which just illustrates for you how good natively Opus 5.5 has become, because even without these plugins, it's able to create videos like that. And by the way, if you want to learn how to build and sell AI systems that businesses actually pay for, then that's pretty much all we do over at the Robonuggets community, where not only do you get access to the Claude Living Masterclass, which we update every week and takes you from zero to mastery with the latest on AI, but you also get access to our Agents as a Service course, which walks you through how to actually get paid for all these AI skills that you are learning. You also get to be part of a genuinely great community of AI builders. In fact, you can see just some of the recent wins our members are getting from the program right here. So if you want to start earning from AI, then check that just in the pinned comment below. Now back to the video. But if you're serious about producing video using AI and using Claude, you need to understand that there's still levels to this skill still, because that example that we went through, that's the most basic level. That's level one, where you send a single prompt and you get a good result. Now, in my view, I think this level is still useful, at least for you to try out, because number one, it gives you a sense of the capability of these models. So if you have a prompt like that, that pushes the ceiling of what a certain model can do, then when a new model gets released, you can just repeat that same prompt to test how good things are now. I also think that one-shot prompts that provide showcase reels like that are quite good in terms of building up a portfolio for you, because if you're a video editor and you're just looking for show reels to showcase your work, then this is a great and easy way for you to get that almost immediately. Because remember, and this is a good time to bring up this chart again, if you're watching this video and you know how to use Claude code, amongst the whole population of people, you are probably here in the red cell. So you're in a very small fraction of people who actually know how good these models have become when it comes to video editing at least. But for a huge portion of people and the customers that you may be serving, this type of capability and motion graphics is actually something that you would expect a top professional agency to be able to produce. And so bottom line is, if you want to create production-level videos using Claude, you probably won't get there with one-shot, but there's clearly still benefits to doing this. And so to make it easy for you to copy those prompts and for you to test it, I just made this nine-page PDF, which you can just send to Claude and pick out all of the starter prompts that I will mention in this video, including those one-shot prompts that I used in order to create those demo reels. And you can just grab this PDF for free down below in the description. Now, like I said, level one, it's useful, but you probably won't get to the end result that you want for production-level quality videos. And so the way that you do that is to move towards level two, which is taking you from one-shot prompting to actually storyboarding your videos. Now, the great thing about this is you don't actually have to sketch it yourself, even though you can do that. You can actually have Claude storyboard your videos for you. So why is storyboarding even important in the first place? Well, usually for most beginners, if they send, let's say, a prompt and they already have an idea of the video that they want, depending on the complexity of this final video, it's more often the case that this prompt that you start with isn't really detailed enough to give you that final result in one shot. And so what ends up happening is that your AI model, Claude in this case, will actually veer away towards the wrong direction and produce for you a final video that has all of the animations and has all of the tokens already spent and burnt, but producing the wrong result, which is very far away from what you want. And so the reason why storyboards are important is that if you ask the AI model to create them first before going all out on this wrong result that it's about to make, if you're able to preview what it's about to do at less cost and at much faster turnaround times, because this is just a storyboard anyway, then you can steer this model towards the right direction to give you the video that you want. Now, I'll just show you the interface that I use and which we're developing as part of the toolkit for our community. But at its core, to do storyboarding effectively, you just need two things. You need to be able to tell Claude that you would want first a storyboard or a set of images of the animations that it's about to do, as well as a description of what actually happens in this particular scene. And so you can see here when I ask it to create a storyboard for me for the Rubrik app, it already created all the HTML elements for me, but without the animations yet. But instead, what it created for me are these screenshots, as well as the descriptions of the animations that it's about to do. So it's saying here that the camera whips to the first panel, it then continues across the panels and so on and so forth. And so at this point, it hasn't rendered the video yet, but you get a clear sense of what it's about to do. Now, the second element when it comes to storyboarding is a way for you to give feedback to it. Now, obviously, you can just open up your chat window and give feedback that way. But I just think with a lot of video and design work, it is much more effective if you can give feedback in the context of the visuals that you're seeing. And so in this interface, let's say I want this to be less text heavy. I can just click on this particular frame. It will add a comment here. And I can just give that feedback for this particular frame. And the great thing about this is when this comment is posted to Claude, it will also give the exact timestamp and even the exact point that I made the comment on in this particular frame. So it's much more directed and in my view is much more effective as well in terms of steering your agent towards what you want. And so what I usually do is I just run through this whole storyboard that it created for us. I give all of my comments and when I'm done with that, I just copy all of these comments and then just paste all of those comments to Claude. Either ask for another storyboard or just go directly to the video depending on how close Claude is already to the video that I actually want. Now, let's take this one level up because if you want to be really good at steering your AI agent, in this case, Opus 5.5, integrating videos that are really stunning, then you want to get to level three where you're actually directing it based on the video that it already created. Because if we go back to our illustration earlier, if you gave feedback on the storyboard and you asked Opus 5.5 for the video that you want, I often find that that takes you around let's say 80 to 90% there in terms of the final polished quality output that you actually really want. And so if you get really good at directing AI to create the final video output for you, then you have reached level three. And at the very core of it, directing really is just giving feedback to the final video and similar to the previous level. You can always do this by speaking to Claude via the chat window, giving your feedback there via natural language. But often what I find is when it comes to reviewing video, it's much easier again if you actually have an interface on an operating system yourself of how you can give feedback to AI. Just to show you one example for my work. This is again another beta version of the toolkit that we're developing for our community. So it's not yet the final look of this piece of software. But this rubric editor basically lets you play the video, give comments on each of these frames. And more importantly, you can also give feedback on the audio that it used, which isn't really something that you will hear during the storyboard process, right? So I'm not sure if you can hear it. You can pretty much hear the sound effects that it used and give comments there. So let's say after viewing the video, we decided that this particular frame or scene is no longer important. Then we can just say to remove this scene and you can see this comment comes with a timestamp where I placed this feedback and it knows exactly what graphic I am referring to. And so similar to storyboarding, you can actually just make a lot of comments on this reel, copy all of those comments and then just send it back to Claude. And just to give you an example from an actual video. So that Opus 5.5 tips video, which the one that has already 300,000 plus views. This is actually the rubric editor where I work with Opus 5.5 to produce that final video. So essentially the difference with this one is that if you can see here, since this is coming from a raw footage, I asked Claude to identify the specific takes that I want to keep in this video and I made a separate lesson on this if you want to learn how to do that. And then if I play this, which right now it's at 2X speed, which is a much faster way for me to just review its animations in there. You can see that when I reviewed this, I just made this comment for this animation where I just said to focus on the title of the page and I gave the link to that Claude platform documentation there, which is why it came back with this animation. And then I just did that across all clips because at least for this video, I did want it to pass my own review and I wanted to match the level of quality that I am envisioning. The great thing with Opus is that I'm finding that I need to give less and less comments just because of how good it one shots these animations. Like it really gets the stuff that I want to be shown. And sometimes when I'm directing this particular video, I just need to provide minor corrections here and there and then I copy all of the comments for all of the clips and I send it back to Claude, wait for it to update this rubric editor and then ask it to render the final video when it's done. And so there you go. That is in my view, how you maximize the capability of Opus 5.5 when it comes to automated video editing. As you can see, there's still a lot of human review involved, which I think is how it should be anyway, because in a world where everyone can pretty much one shot show reels like what you saw in this video, then the real differentiator that you would have in terms of creating videos would be your own taste plus also the operating system by which you work and give feedback to your AI models. Now, to be clear, even if you are storyboarding and even if you are directing on your own, I still think that the lead time to create quality videos have shrunk so much that you can pretty much have just one person do an entire motion graphics video entirely on their own plus Opus 5.5. And as I mentioned, if you need starter prompts for everything that I showed in this video, you can just grab this PDF and send it to your agent. Hopefully that was useful. As always, thank you for watching until the end and consider tapping subscribe below if it is because that helps me a lot to put out more educational stuff like this. I'll see you all next time. Cheers.

## Timestamped

`[00:00]` Opus 5.5 for video editing and motion graphics has gotten pretty unbelievable lately.
`[00:04]` And so these examples that you'll see are all created with Opus,
`[00:07]` and all I did is to give it access to my workspace,
`[00:10]` no generative AI video model was used,
`[00:12]` and I just sent a simple prompt like this
`[00:14]` where I asked it to make a dynamic motion graphics video
`[00:17]` that showcases its capabilities.
`[00:34]` This is another similar example,
`[00:36]` but where I pushed it to use more 3D elements.
`[00:53]` And in fact, some of the videos I launched recently,
`[00:55]` like this one that already has 300,000 views,
`[00:58]` it was also edited using Opus 5.5.
`[01:00]` So Opus 5.5 just came out and Antropic just published
`[01:04]` an official comprehensive guide on how to prompt it.
`[01:06]` You can keep one agents.md as your single instructions file now
`[01:10]` instead of keeping a claw.md and an agents.md in sync.
`[01:14]` One of the best things you can do is to ask for them in the SVG format.
`[01:18]` That stands for Scalable Vector Graphics,
`[01:20]` so that it scales to any size without going blurry.
`[01:23]` You can open the file and change a color by hand,
`[01:26]` and you can even have Claude animate these icons.
`[01:28]` So with SVGs, every graphic that you get back from Claude
`[01:32]` is editable and animatable.
`[01:34]` So clearly, I've been testing this model heavily
`[01:36]` for automated videos, and in my view,
`[01:38]` these are all a major step up versus what we had previously.
`[01:41]` So today, I'll teach you how to best use this capability of 5.5
`[01:44]` so that by the end of it,
`[01:45]` you can also level up your video and motion graphics skills using AI.
`[01:49]` I know exactly how I make videos like these
`[01:51]` that get hundreds of thousands of views,
`[01:52]` even if they are AI edited.
`[01:54]` And if you're new, my name is Jay.
`[01:56]` I spent over a decade working with brands you probably know.
`[01:58]` I've been in AI since my masters in data science,
`[02:01]` and now I'm leading our AI business
`[02:02]` in one of the largest AI communities globally.
`[02:05]` Let's dive into it.
`[02:06]` So before we go into the different levels
`[02:08]` by which you can use Opus's capability for video editing,
`[02:11]` I actually want to give you context
`[02:12]` of what really happens under the hood
`[02:14]` when you send a simple prompt like this to 5.5.
`[02:17]` Because as I mentioned earlier,
`[02:18]` this whole video that it created for us,
`[02:20]` it didn't really use any generative AI video model for it.
`[02:23]` All of the movements, all of the text,
`[02:25]` and basically everything you see here,
`[02:26]` those are all created using code.
`[02:28]` And in fact, in this demo interface,
`[02:30]` you can clearly see I can select these individual elements
`[02:32]` which are all just images in my workspace.
`[02:34]` And all they are really is Claude pointing
`[02:36]` to this particular photo in this case,
`[02:38]` and using some code, in this case,
`[02:39]` JavaScript in order to place them in this exact position,
`[02:43]` in this exact timestamp.
`[02:44]` And everything that you see here,
`[02:46]` including the movements, the motion graphics,
`[02:48]` that is all using Opus 5.5's taste.
`[02:50]` And if you're curious exactly what tools
`[02:52]` it used to achieve that video,
`[02:54]` I also just asked Opus to illustrate that here in Excalidraw.
`[02:58]` And you can see that with that one-shot prompt
`[02:59]` that we sent it,
`[03:00]` it just used its native knowledge of HTML, CSS, JavaScript,
`[03:04]` and a couple of other libraries like 3JS and FFmpeg
`[03:08]` in order to achieve that look.
`[03:09]` Which again, you don't even need to understand all of this,
`[03:12]` although in my view, it's at least good to be aware of them.
`[03:14]` But because of how powerful these models have become,
`[03:16]` you can pretty much just rely on 5.5
`[03:18]` to create you create showreels like that
`[03:20]` using a single prompt.
`[03:22]` I did want to call out though,
`[03:23]` that for this particular test,
`[03:24]` we did not use hyperframes or remotion,
`[03:27]` which are these popular open source libraries
`[03:29]` for video editing using Claude,
`[03:30]` which just illustrates for you
`[03:32]` how good natively Opus 5.5 has become,
`[03:34]` because even without these plugins,
`[03:36]` it's able to create videos like that.
`[03:38]` And by the way, if you want to learn
`[03:39]` how to build and sell AI systems
`[03:40]` that businesses actually pay for,
`[03:42]` then that's pretty much all we do
`[03:44]` over at the Robonuggets community,
`[03:45]` where not only do you get access
`[03:46]` to the Claude Living Masterclass,
`[03:48]` which we update every week
`[03:49]` and takes you from zero to mastery
`[03:51]` with the latest on AI,
`[03:52]` but you also get access to our Agents as a Service course,
`[03:55]` which walks you through how to actually get paid
`[03:57]` for all these AI skills that you are learning.
`[03:59]` You also get to be part
`[04:00]` of a genuinely great community of AI builders.
`[04:03]` In fact, you can see just some of the recent wins
`[04:05]` our members are getting from the program right here.
`[04:07]` So if you want to start earning from AI,
`[04:08]` then check that just in the pinned comment below.
`[04:10]` Now back to the video.
`[04:11]` But if you're serious about producing video
`[04:13]` using AI and using Claude,
`[04:15]` you need to understand that there's still levels
`[04:17]` to this skill still,
`[04:18]` because that example that we went through,
`[04:20]` that's the most basic level.
`[04:21]` That's level one, where you send a single prompt
`[04:24]` and you get a good result.
`[04:25]` Now, in my view, I think this level is still useful,
`[04:28]` at least for you to try out,
`[04:29]` because number one, it gives you a sense
`[04:30]` of the capability of these models.
`[04:32]` So if you have a prompt like that,
`[04:33]` that pushes the ceiling of what a certain model can do,
`[04:36]` then when a new model gets released,
`[04:37]` you can just repeat that same prompt
`[04:39]` to test how good things are now.
`[04:41]` I also think that one-shot prompts
`[04:43]` that provide showcase reels like that
`[04:45]` are quite good in terms of building up a portfolio for you,
`[04:48]` because if you're a video editor
`[04:49]` and you're just looking for show reels
`[04:51]` to showcase your work,
`[04:52]` then this is a great and easy way
`[04:54]` for you to get that almost immediately.
`[04:56]` Because remember, and this is a good time
`[04:58]` to bring up this chart again,
`[05:00]` if you're watching this video
`[05:01]` and you know how to use Claude code,
`[05:03]` amongst the whole population of people,
`[05:04]` you are probably here in the red cell.
`[05:07]` So you're in a very small fraction of people
`[05:09]` who actually know how good these models have become
`[05:11]` when it comes to video editing at least.
`[05:13]` But for a huge portion of people
`[05:15]` and the customers that you may be serving,
`[05:16]` this type of capability and motion graphics
`[05:19]` is actually something that you would expect
`[05:21]` a top professional agency to be able to produce.
`[05:24]` And so bottom line is,
`[05:25]` if you want to create production-level videos using Claude,
`[05:28]` you probably won't get there with one-shot,
`[05:30]` but there's clearly still benefits to doing this.
`[05:32]` And so to make it easy for you to copy those prompts
`[05:35]` and for you to test it,
`[05:36]` I just made this nine-page PDF,
`[05:38]` which you can just send to Claude
`[05:39]` and pick out all of the starter prompts
`[05:41]` that I will mention in this video,
`[05:42]` including those one-shot prompts
`[05:43]` that I used in order to create those demo reels.
`[05:46]` And you can just grab this PDF for free
`[05:48]` down below in the description.
`[05:49]` Now, like I said, level one, it's useful,
`[05:51]` but you probably won't get to the end result
`[05:54]` that you want for production-level quality videos.
`[05:56]` And so the way that you do that
`[05:58]` is to move towards level two,
`[06:00]` which is taking you from one-shot prompting
`[06:02]` to actually storyboarding your videos.
`[06:04]` Now, the great thing about this
`[06:05]` is you don't actually have to sketch it yourself,
`[06:08]` even though you can do that.
`[06:09]` You can actually have Claude storyboard your videos
`[06:12]` for you.
`[06:12]` So why is storyboarding even important
`[06:14]` in the first place?
`[06:15]` Well, usually for most beginners,
`[06:17]` if they send, let's say, a prompt
`[06:19]` and they already have an idea
`[06:20]` of the video that they want,
`[06:21]` depending on the complexity of this final video,
`[06:24]` it's more often the case
`[06:25]` that this prompt that you start with
`[06:27]` isn't really detailed enough
`[06:28]` to give you that final result in one shot.
`[06:30]` And so what ends up happening
`[06:31]` is that your AI model, Claude in this case,
`[06:34]` will actually veer away towards the wrong direction
`[06:37]` and produce for you a final video
`[06:39]` that has all of the animations
`[06:41]` and has all of the tokens already spent and burnt,
`[06:43]` but producing the wrong result,
`[06:45]` which is very far away from what you want.
`[06:47]` And so the reason why storyboards are important
`[06:49]` is that if you ask the AI model
`[06:51]` to create them first before going all out
`[06:53]` on this wrong result that it's about to make,
`[06:54]` if you're able to preview what it's about to do
`[06:56]` at less cost and at much faster turnaround times,
`[06:59]` because this is just a storyboard anyway,
`[07:01]` then you can steer this model
`[07:02]` towards the right direction
`[07:04]` to give you the video that you want.
`[07:05]` Now, I'll just show you the interface that I use
`[07:07]` and which we're developing
`[07:08]` as part of the toolkit for our community.
`[07:10]` But at its core, to do storyboarding effectively,
`[07:13]` you just need two things.
`[07:14]` You need to be able to tell Claude
`[07:15]` that you would want first a storyboard
`[07:17]` or a set of images of the animations
`[07:19]` that it's about to do,
`[07:20]` as well as a description of what actually happens
`[07:23]` in this particular scene.
`[07:24]` And so you can see here
`[07:25]` when I ask it to create a storyboard for me
`[07:27]` for the Rubrik app,
`[07:28]` it already created all the HTML elements for me,
`[07:31]` but without the animations yet.
`[07:32]` But instead, what it created for me
`[07:33]` are these screenshots,
`[07:35]` as well as the descriptions of the animations
`[07:37]` that it's about to do.
`[07:38]` So it's saying here
`[07:39]` that the camera whips to the first panel,
`[07:41]` it then continues across the panels
`[07:43]` and so on and so forth.
`[07:44]` And so at this point,
`[07:44]` it hasn't rendered the video yet,
`[07:46]` but you get a clear sense
`[07:47]` of what it's about to do.
`[07:49]` Now, the second element
`[07:50]` when it comes to storyboarding
`[07:51]` is a way for you
`[07:52]` to give feedback to it.
`[07:53]` Now, obviously, you can just open up
`[07:54]` your chat window
`[07:55]` and give feedback that way.
`[07:57]` But I just think
`[07:58]` with a lot of video and design work,
`[07:59]` it is much more effective
`[08:00]` if you can give feedback
`[08:02]` in the context of the visuals
`[08:03]` that you're seeing.
`[08:04]` And so in this interface,
`[08:05]` let's say I want this
`[08:06]` to be less text heavy.
`[08:07]` I can just click
`[08:08]` on this particular frame.
`[08:09]` It will add a comment here.
`[08:11]` And I can just give that feedback
`[08:12]` for this particular frame.
`[08:14]` And the great thing about this
`[08:15]` is when this comment
`[08:16]` is posted to Claude,
`[08:17]` it will also give
`[08:18]` the exact timestamp
`[08:19]` and even the exact point
`[08:20]` that I made the comment on
`[08:21]` in this particular frame.
`[08:23]` So it's much more directed
`[08:24]` and in my view
`[08:24]` is much more effective as well
`[08:26]` in terms of steering your agent
`[08:27]` towards what you want.
`[08:28]` And so what I usually do
`[08:29]` is I just run through
`[08:30]` this whole storyboard
`[08:31]` that it created for us.
`[08:32]` I give all of my comments
`[08:34]` and when I'm done with that,
`[08:35]` I just copy all of these comments
`[08:36]` and then just paste
`[08:37]` all of those comments to Claude.
`[08:38]` Either ask for another storyboard
`[08:40]` or just go directly to the video
`[08:42]` depending on how close Claude
`[08:44]` is already to the video
`[08:45]` that I actually want.
`[08:46]` Now, let's take this one level up
`[08:48]` because if you want to be really good
`[08:50]` at steering your AI agent,
`[08:51]` in this case, Opus 5.5,
`[08:53]` integrating videos
`[08:54]` that are really stunning,
`[08:55]` then you want to get to level three
`[08:57]` where you're actually directing it
`[08:58]` based on the video
`[08:59]` that it already created.
`[09:00]` Because if we go back
`[09:01]` to our illustration earlier,
`[09:03]` if you gave feedback
`[09:03]` on the storyboard
`[09:04]` and you asked Opus 5.5
`[09:06]` for the video that you want,
`[09:07]` I often find that that takes you
`[09:08]` around let's say 80 to 90% there
`[09:10]` in terms of the final polished
`[09:12]` quality output
`[09:13]` that you actually really want.
`[09:14]` And so if you get really good
`[09:15]` at directing AI
`[09:16]` to create the final video output for you,
`[09:18]` then you have reached level three.
`[09:20]` And at the very core of it,
`[09:21]` directing really is just giving feedback
`[09:23]` to the final video
`[09:24]` and similar to the previous level.
`[09:26]` You can always do this
`[09:27]` by speaking to Claude
`[09:28]` via the chat window,
`[09:29]` giving your feedback there
`[09:30]` via natural language.
`[09:31]` But often what I find is
`[09:32]` when it comes to reviewing video,
`[09:34]` it's much easier again
`[09:35]` if you actually have
`[09:36]` an interface on an operating system
`[09:38]` yourself of how you can give feedback
`[09:40]` to AI.
`[09:40]` Just to show you one example
`[09:42]` for my work.
`[09:42]` This is again another beta version
`[09:44]` of the toolkit
`[09:45]` that we're developing
`[09:46]` for our community.
`[09:46]` So it's not yet the final look
`[09:48]` of this piece of software.
`[09:49]` But this rubric editor
`[09:51]` basically lets you play the video,
`[09:53]` give comments on each of these frames.
`[09:55]` And more importantly,
`[09:56]` you can also give feedback
`[09:57]` on the audio that it used,
`[09:58]` which isn't really something
`[09:59]` that you will hear
`[10:00]` during the storyboard process, right?
`[10:01]` So I'm not sure
`[10:02]` if you can hear it.
`[10:03]` You can pretty much hear
`[10:04]` the sound effects
`[10:05]` that it used
`[10:05]` and give comments there.
`[10:06]` So let's say after viewing the video,
`[10:08]` we decided that this particular frame
`[10:10]` or scene is no longer important.
`[10:12]` Then we can just say
`[10:12]` to remove this scene
`[10:14]` and you can see this comment
`[10:15]` comes with a timestamp
`[10:16]` where I placed this feedback
`[10:17]` and it knows exactly
`[10:18]` what graphic I am referring to.
`[10:20]` And so similar to storyboarding,
`[10:22]` you can actually just make
`[10:23]` a lot of comments on this reel,
`[10:24]` copy all of those comments
`[10:26]` and then just send it back to Claude.
`[10:27]` And just to give you an example
`[10:28]` from an actual video.
`[10:30]` So that Opus 5.5 tips video,
`[10:32]` which the one that has
`[10:33]` already 300,000 plus views.
`[10:35]` This is actually the rubric editor
`[10:37]` where I work with Opus 5.5
`[10:38]` to produce that final video.
`[10:40]` So essentially the difference
`[10:41]` with this one is that
`[10:42]` if you can see here,
`[10:43]` since this is coming
`[10:44]` from a raw footage,
`[10:45]` I asked Claude to identify
`[10:47]` the specific takes
`[10:48]` that I want to keep in this video
`[10:49]` and I made a separate lesson on this
`[10:51]` if you want to learn
`[10:52]` how to do that.
`[10:53]` And then if I play this,
`[10:54]` which right now it's at 2X speed,
`[10:58]` which is a much faster way
`[11:00]` for me to just review
`[11:01]` its animations in there.
`[11:02]` You can see that when I reviewed this,
`[11:04]` I just made this comment
`[11:05]` for this animation
`[11:05]` where I just said to focus
`[11:07]` on the title of the page
`[11:08]` and I gave the link
`[11:09]` to that Claude platform documentation there,
`[11:11]` which is why it came back
`[11:12]` with this animation.
`[11:13]` And then I just did that
`[11:14]` across all clips
`[11:15]` because at least for this video,
`[11:17]` I did want it to pass my own review
`[11:20]` and I wanted to match
`[11:21]` the level of quality
`[11:22]` that I am envisioning.
`[11:23]` The great thing with Opus
`[11:24]` is that I'm finding
`[11:25]` that I need to give
`[11:26]` less and less comments
`[11:27]` just because of how good
`[11:28]` it one shots these animations.
`[11:30]` Like it really gets the stuff
`[11:31]` that I want to be shown.
`[11:32]` And sometimes when I'm directing
`[11:34]` this particular video,
`[11:35]` I just need to provide
`[11:36]` minor corrections here and there
`[11:37]` and then I copy all of the comments
`[11:39]` for all of the clips
`[11:40]` and I send it back to Claude,
`[11:41]` wait for it to update
`[11:42]` this rubric editor
`[11:43]` and then ask it to render
`[11:44]` the final video when it's done.
`[11:46]` And so there you go.
`[11:46]` That is in my view,
`[11:47]` how you maximize
`[11:48]` the capability of Opus 5.5
`[11:50]` when it comes
`[11:51]` to automated video editing.
`[11:52]` As you can see,
`[11:53]` there's still a lot
`[11:54]` of human review involved,
`[11:55]` which I think is how
`[11:56]` it should be anyway,
`[11:57]` because in a world
`[11:58]` where everyone can pretty much
`[11:59]` one shot show reels
`[12:00]` like what you saw in this video,
`[12:02]` then the real differentiator
`[12:03]` that you would have in terms
`[12:04]` of creating videos
`[12:06]` would be your own taste
`[12:07]` plus also the operating system
`[12:09]` by which you work
`[12:10]` and give feedback
`[12:11]` to your AI models.
`[12:12]` Now, to be clear,
`[12:13]` even if you are storyboarding
`[12:14]` and even if you are directing
`[12:16]` on your own,
`[12:16]` I still think that the lead time
`[12:18]` to create quality videos
`[12:20]` have shrunk so much
`[12:21]` that you can pretty much
`[12:22]` have just one person
`[12:23]` do an entire motion graphics video
`[12:25]` entirely on their own
`[12:26]` plus Opus 5.5.
`[12:28]` And as I mentioned,
`[12:28]` if you need starter prompts
`[12:29]` for everything that I showed
`[12:31]` in this video,
`[12:31]` you can just grab this PDF
`[12:33]` and send it to your agent.
`[12:34]` Hopefully that was useful.
`[12:36]` As always, thank you
`[12:36]` for watching until the end
`[12:37]` and consider tapping
`[12:38]` subscribe below if it is
`[12:39]` because that helps me a lot
`[12:40]` to put out more
`[12:41]` educational stuff like this.
`[12:42]` I'll see you all next time.
`[12:43]` Cheers.
