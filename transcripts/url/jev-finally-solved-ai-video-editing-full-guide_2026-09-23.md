# JEV Finally Solved AI Video Editing (Full guide)

- **Source:** https://www.youtube.com/watch?v=ZlICPWwgmmg
- **Uploader:** Albert Olgaard
- **Uploaded:** 2026-09-20
- **Duration:** 6:00
- **Detected language:** en (p=1.00)
- **Model:** small.en

## Transcript

What the actual f**k? Yesterday, I posted this video right here. And if you go to it, can you see something wrong about it? It's getting really good views. It said 1 of 10. But guess what? Nothing in this entire YouTube video is made by a human. All the zoom-ins, all the captions, the tracking on my face. It's even highlighting things on the screen and blurring sensitive information in the video. In this video, no one ever opened a video editor. No human was involved at all. And guess what? This video you're watching now, also 100% edited by AI. Using this exact skill. And I'm not using Remotion and I'm not using Hyperframes that gives it that very generic AI look. And if we go to the comments, no one has any idea. Instead, it's actually just simple Python and it works both inside of Cloud or Codex. But AI editing is usually really slow and it makes mistakes. But that's why we can use the new Jeff model. Because it's really fast and really good at taking quick decisions. And in this video, you're getting the skill that one-shots video editing. If you don't know me, my name is Albert and I am by no means the smartest. I didn't even go to university. However, I've still managed to build a multi-seven figure business and consult a billion dollar companies only because I am decently good at using AI. And now we are making AI education free for absolutely everyone. So if you haven't already, make sure to subscribe. Okay, I'm not going to bore you with exactly how it works. But here's a quick overview of how Cloud can do this. First, AI transcribes my voice and we need to use a very specific API for this. This is generally just the only thing that I've tried that works. And for determining the transcript, this is where our AI calls upon the new Jeff model to speed things up a lot. And then after the AI has the transcript of the video, it can then plan out every single scene in the video when we should show screen share, when we should show my face. It basically makes decisions based on the transcript. It then builds out all the scenes, it cleans my screen share, it blurs sensitive information like API keys. And this part is what takes a while to do because it's going through the entire video frame by frame. But that's also the reason so I can launch it every single video. It then runs a feedback loop where it checks every single change that it makes to ensure that it hasn't missed anything. And then first, it spits out the video section by section so I can check that everything is like it's supposed to be. And at the end, it renders the entire thing and gives me the entire YouTube video. All right, the first thing we need to do is to grab the skill. It's inside of our completely free community. You can join in the description. Again, completely free to join forever. Go inside of classroom and then inside of cloud skills. And then inside of this folder, you can download all of my cloud skills. For this, I'll recommend that you set the model to Opus and you then set it to Ultracode. This is what I found the best. If I use Fable, I run into my Fable limits way too quickly. So Opus Ultracode works really well for this. And then you want to insert the raw video that you've recorded, insert that into cloud. And then you take your screen share and insert that as well. I'll show you what screen recalling tool I'm using later in this video. And then we just say, please use the Albert editing skill to edit this entire video. If you have any ideas to things you want to add like in the intro, et cetera, then you can mention it. For example, show the viral exposed about the new model launch. Do this in the intro. I want the video slow paced, not too many animations only in the intro. If you have any ideas or anything you want to make sure that it does correctly, then you mention it in this prompt right here. So for example, later in the video, when I explain something, I can say that around midway through the video when I'm explaining things, please show clean animations of what I'm talking about just to visualize things. By the way, the dictation tool I'm using right here is CodeType. It's actually a tool that I built myself and you can see it is pretty fast. I thought it was crazy that tools like Whisper Flow charges like 20 bucks a month while training on our data. So I actually built my own dictation tool. It's $9 a month. Or if you hop on yearly, then it's $7 a month. You can check it out. There's a link in the description. And then that's all we need to do. All the instructions are already inside of the skill and the Albert editing skill. You might have to write Albert YouTube editing skill because I have multiple skills. Then we hit enter and now Claude will start working on this video. This process can take a while because of the way that I've built this skill where I basically wanted to one-shot it every single time and I wanted to make no mistakes and take a little longer than usual. Editing an entire video depending on how long it is can take anywhere from like three hours to five hours. Some of my longer videos even take like 10 hours to edit. But the great thing about it is that I just have this running in the background and I can work on all my other stuff while it's editing. When it's done, then it spits out all of these videos right here. And I'll just go through them and I'll check that it has actually done the things that I wanted it to do. And if there's anything I want to change, I can just tell it in natural language and it's going to go in and fix that thing. So you can see it has split up this YouTube video in a couple of different sections. A couple of tips to get this clean cursor for the screen share if that's the kind of videos that you're creating. I use a software that's called Screen Studio. Again, not sponsored. That's just what I'm using. Something I've heard which I don't know is true is that these platforms, they can sometimes flag content if it's yielded by code. So to make sure that doesn't hurt performance or flag anything inside of the platforms, I put it inside of just like CapCut or any video editor really. I then export the file which basically just rewrites the metadata just to be 100% sure that it doesn't hurt any performance. Running this is definitely not cheap. You can see I've hit my 100% fable usage this week and it resets in 10 hours and I'm on the 20x floor plan. But I'm also creating videos. I created what like three videos this week using Opus and using fable as well. You could also try with a cheaper model. You're probably not going to get as good results but you can probably get like 80% of the way there if you use something like Deepsea 4.1 Flash. It might also be faster. And that is how you end up with a YouTube video like this that is 100% edited by AI. Just like this video that you're watching right now, also edited with this exact approach. And here's the crazy thing. I also made an editing skill for my Instagram Reels and you can see they're getting really good views. 75k, 87k, 113,000 views. And look at how they look as well. This is also 100% edited by AI and I think it looks so dope and it saves me so much time. If you want a YouTube video like this one that I just created but for Instagram Reels, then make sure to like the video and subscribe so you don't miss that one. Again, the skill we have used in this video, you can find it inside of our free community. I'll leave a link in the description. Thank you so much for watching. Albert.

## Timestamped

`[00:00]` What the actual f**k?
`[00:01]` Yesterday, I posted this video right here.
`[00:03]` And if you go to it, can you see something wrong about it?
`[00:06]` It's getting really good views.
`[00:07]` It said 1 of 10.
`[00:08]` But guess what?
`[00:09]` Nothing in this entire YouTube video is made by a human.
`[00:13]` All the zoom-ins, all the captions, the tracking on my face.
`[00:16]` It's even highlighting things on the screen
`[00:19]` and blurring sensitive information in the video.
`[00:22]` In this video, no one ever opened a video editor.
`[00:25]` No human was involved at all.
`[00:27]` And guess what?
`[00:28]` This video you're watching now, also 100% edited by AI.
`[00:32]` Using this exact skill.
`[00:34]` And I'm not using Remotion and I'm not using Hyperframes
`[00:37]` that gives it that very generic AI look.
`[00:39]` And if we go to the comments, no one has any idea.
`[00:42]` Instead, it's actually just simple Python
`[00:44]` and it works both inside of Cloud or Codex.
`[00:46]` But AI editing is usually really slow and it makes mistakes.
`[00:50]` But that's why we can use the new Jeff model.
`[00:52]` Because it's really fast and really good at taking quick decisions.
`[00:55]` And in this video, you're getting the skill
`[00:57]` that one-shots video editing.
`[00:58]` If you don't know me, my name is Albert
`[01:00]` and I am by no means the smartest.
`[01:02]` I didn't even go to university.
`[01:03]` However, I've still managed to build a multi-seven figure business
`[01:06]` and consult a billion dollar companies
`[01:08]` only because I am decently good at using AI.
`[01:11]` And now we are making AI education free for absolutely everyone.
`[01:14]` So if you haven't already, make sure to subscribe.
`[01:16]` Okay, I'm not going to bore you with exactly how it works.
`[01:19]` But here's a quick overview of how Cloud can do this.
`[01:21]` First, AI transcribes my voice
`[01:23]` and we need to use a very specific API for this.
`[01:25]` This is generally just the only thing that I've tried that works.
`[01:28]` And for determining the transcript,
`[01:29]` this is where our AI calls upon the new Jeff model
`[01:32]` to speed things up a lot.
`[01:34]` And then after the AI has the transcript of the video,
`[01:36]` it can then plan out every single scene in the video
`[01:38]` when we should show screen share, when we should show my face.
`[01:41]` It basically makes decisions based on the transcript.
`[01:44]` It then builds out all the scenes, it cleans my screen share,
`[01:47]` it blurs sensitive information like API keys.
`[01:50]` And this part is what takes a while to do
`[01:52]` because it's going through the entire video frame by frame.
`[01:55]` But that's also the reason
`[01:56]` so I can launch it every single video.
`[01:57]` It then runs a feedback loop
`[01:59]` where it checks every single change that it makes
`[02:01]` to ensure that it hasn't missed anything.
`[02:03]` And then first, it spits out the video section by section
`[02:05]` so I can check that everything is like it's supposed to be.
`[02:08]` And at the end, it renders the entire thing
`[02:09]` and gives me the entire YouTube video.
`[02:11]` All right, the first thing we need to do
`[02:12]` is to grab the skill.
`[02:13]` It's inside of our completely free community.
`[02:15]` You can join in the description.
`[02:16]` Again, completely free to join forever.
`[02:18]` Go inside of classroom and then inside of cloud skills.
`[02:21]` And then inside of this folder,
`[02:22]` you can download all of my cloud skills.
`[02:24]` For this, I'll recommend that you set the model to Opus
`[02:27]` and you then set it to Ultracode.
`[02:29]` This is what I found the best.
`[02:30]` If I use Fable, I run into my Fable limits way too quickly.
`[02:33]` So Opus Ultracode works really well for this.
`[02:36]` And then you want to insert the raw video
`[02:37]` that you've recorded, insert that into cloud.
`[02:39]` And then you take your screen share
`[02:41]` and insert that as well.
`[02:41]` I'll show you what screen recalling tool
`[02:43]` I'm using later in this video.
`[02:44]` And then we just say,
`[02:45]` please use the Albert editing skill
`[02:48]` to edit this entire video.
`[02:50]` If you have any ideas to things you want to add
`[02:52]` like in the intro, et cetera,
`[02:54]` then you can mention it.
`[02:55]` For example, show the viral exposed
`[02:58]` about the new model launch.
`[02:59]` Do this in the intro.
`[03:01]` I want the video slow paced,
`[03:03]` not too many animations only in the intro.
`[03:06]` If you have any ideas
`[03:07]` or anything you want to make sure that it does correctly,
`[03:09]` then you mention it in this prompt right here.
`[03:11]` So for example, later in the video,
`[03:12]` when I explain something,
`[03:13]` I can say that around midway through the video
`[03:15]` when I'm explaining things,
`[03:16]` please show clean animations
`[03:18]` of what I'm talking about just to visualize things.
`[03:20]` By the way, the dictation tool I'm using right here
`[03:21]` is CodeType.
`[03:22]` It's actually a tool that I built myself
`[03:24]` and you can see it is pretty fast.
`[03:26]` I thought it was crazy
`[03:27]` that tools like Whisper Flow charges like 20 bucks a month
`[03:30]` while training on our data.
`[03:31]` So I actually built my own dictation tool.
`[03:33]` It's $9 a month.
`[03:34]` Or if you hop on yearly,
`[03:35]` then it's $7 a month.
`[03:36]` You can check it out.
`[03:37]` There's a link in the description.
`[03:38]` And then that's all we need to do.
`[03:39]` All the instructions
`[03:40]` are already inside of the skill
`[03:42]` and the Albert editing skill.
`[03:43]` You might have to write Albert YouTube editing skill
`[03:45]` because I have multiple skills.
`[03:47]` Then we hit enter
`[03:47]` and now Claude will start working on this video.
`[03:50]` This process can take a while
`[03:52]` because of the way that I've built this skill
`[03:54]` where I basically wanted to one-shot it every single time
`[03:56]` and I wanted to make no mistakes
`[03:58]` and take a little longer than usual.
`[03:59]` Editing an entire video
`[04:00]` depending on how long it is
`[04:02]` can take anywhere from like three hours to five hours.
`[04:05]` Some of my longer videos
`[04:06]` even take like 10 hours to edit.
`[04:07]` But the great thing about it
`[04:08]` is that I just have this running in the background
`[04:10]` and I can work on all my other stuff
`[04:12]` while it's editing.
`[04:13]` When it's done,
`[04:14]` then it spits out all of these videos right here.
`[04:16]` And I'll just go through them
`[04:17]` and I'll check that it has actually done
`[04:18]` the things that I wanted it to do.
`[04:20]` And if there's anything I want to change,
`[04:21]` I can just tell it in natural language
`[04:23]` and it's going to go in and fix that thing.
`[04:25]` So you can see it has split up this YouTube video
`[04:26]` in a couple of different sections.
`[04:28]` A couple of tips to get this clean cursor
`[04:30]` for the screen share
`[04:31]` if that's the kind of videos that you're creating.
`[04:33]` I use a software that's called Screen Studio.
`[04:35]` Again, not sponsored.
`[04:36]` That's just what I'm using.
`[04:37]` Something I've heard
`[04:38]` which I don't know is true
`[04:39]` is that these platforms,
`[04:40]` they can sometimes flag content if it's yielded by code.
`[04:44]` So to make sure that doesn't hurt performance
`[04:46]` or flag anything inside of the platforms,
`[04:48]` I put it inside of just like CapCut
`[04:50]` or any video editor really.
`[04:51]` I then export the file
`[04:53]` which basically just rewrites the metadata
`[04:54]` just to be 100% sure
`[04:56]` that it doesn't hurt any performance.
`[04:57]` Running this is definitely not cheap.
`[04:59]` You can see I've hit my 100% fable usage this week
`[05:02]` and it resets in 10 hours
`[05:03]` and I'm on the 20x floor plan.
`[05:05]` But I'm also creating videos.
`[05:06]` I created what like three videos this week
`[05:09]` using Opus and using fable as well.
`[05:11]` You could also try with a cheaper model.
`[05:13]` You're probably not going to get as good results
`[05:14]` but you can probably get like 80% of the way there
`[05:17]` if you use something like Deepsea 4.1 Flash.
`[05:19]` It might also be faster.
`[05:21]` And that is how you end up with a YouTube video like this
`[05:23]` that is 100% edited by AI.
`[05:26]` Just like this video that you're watching right now,
`[05:28]` also edited with this exact approach.
`[05:30]` And here's the crazy thing.
`[05:31]` I also made an editing skill for my Instagram Reels
`[05:34]` and you can see they're getting really good views.
`[05:36]` 75k, 87k, 113,000 views.
`[05:39]` And look at how they look as well.
`[05:40]` This is also 100% edited by AI
`[05:44]` and I think it looks so dope
`[05:45]` and it saves me so much time.
`[05:47]` If you want a YouTube video like this one
`[05:48]` that I just created
`[05:49]` but for Instagram Reels,
`[05:50]` then make sure to like the video and subscribe
`[05:51]` so you don't miss that one.
`[05:53]` Again, the skill we have used in this video,
`[05:54]` you can find it inside of our free community.
`[05:56]` I'll leave a link in the description.
`[05:57]` Thank you so much for watching.
`[05:59]` Albert.
