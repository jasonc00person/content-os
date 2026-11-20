# How I Fully Automated My Video Editing (Claude Code)

- **Source:** https://www.youtube.com/watch?v=G0EH0xdy2-E
- **Uploader:** Brendan Jowett
- **Uploaded:** 2026-04-11
- **Duration:** 11:52
- **Method:** YouTube captions (no transcription needed)

## Transcript

This video was edited entirely by AI. The cuts, the transitions, the text overlays, all of it. I recorded the footage, handed it off to Claude Code, and it handled the rest. I used to spend anywhere from 3 to 6 hours editing a single video, or I'd pay an editor a few hundred dollars to do it for me. Now, the entire process runs through a workflow that Claude Code manages. I simply describe how I want the video structured, and it takes care of the entire edit from raw footage through to a finished export. There's no manual scrubbing through clips, looking for bad takes. There's no repeating the same edits I've already done on the last 10 videos. And once you've set this workflow up, it stays consistent across every single video. You're not rebuilding the edit from scratch every time. Because Claude already knows how your videos should look, it applies the same style automatically. This means that every video can come out with the same level of quality without the hours of work. So, in this video, I'm going to walk you through the full setup, showing you every tool involved, and show you how to build this exact workflow on your own computer. All right. So, I've just recently recorded a brand new video, and I'm just going to go ahead and start to edit this video, and just walk you through step-by-step what my process is from taking raw footage all the way to a fully edited video ready to publish. So, the first step in this process, once I've filmed a video, is to head over to this tool right here, which is called Descript. So, Descript is the one tool outside of Claude Code that I am going to be using here. And this is just what I use to very quickly edit all of the cuts in the video. And the easiest way to explain it is that editing on Descript is kind of like just editing a Word document. I'm not actually going to be manually cutting anything myself. And the reason that I'm not doing this directly through Claude Code is that I have found that, no matter how good my prompt is, there is still little things here and there that I do need to update and change when it comes to repeated sentences or some stuff getting cut out. It's definitely not perfect. I mean, it does a pretty good job of getting the majority of it done, but I do like to verify everything that I'm saying on the video to make sure that it's accurate. And so, that's why I do still use their interface here. So, I've just attached the MP4 to the video that I just recently filmed. And once I've done that, what I have, if I click browse more templates, I go up to all templates, and I click into created by me. I've essentially created my own template right here, which is just for cutting the YouTube video. So, all this really does is that it removes any duplicate sentences and just keeps the correct one. So, it just really fixes up the entire video. I'll usually just hit use template. And once I've done that, it'll start to load into the editor. Now, my video is going to start to get processed. Obviously, Descript is a cloud editing application, so you have to upload the video in order for it to get access to it. Then, all the processing and everything just happens in Descript. And if I just click into this right here, you can see the prompt template that I'm using is incredibly basic. It's not the most advanced prompt ever. I could probably work on this, to be honest. If you're interested in scaling your own AI voice agency and becoming a better AI developer, we've just released our AI Launchpad School Community. Inside, you're going to get access to a complete A to Z course on how to build AI voice agents alongside an A to Z course on how to use N8N to build AI workflows and agents. We've also partnered with BookedIN, which is a voice and chat AI client dashboard software, which you'll get as a bonus within the community. We've got over $3 million in software discounts for some of the top AI and business tools, including N8N, Make, Stripe, Webflow, Lovable, and so much more. I guarantee you will make your money back in the first day using these discounts. Alongside all this, I've hired the top voice AI and automation developers to work in the community to provide unlimited technical support. So, if you ever have a question or problem you need solving, we'd love to help you out. I'll have the community linked in the description. But, it just says, "Please remove all repeating sentences." Usually, the last repeated sentence is the correct one after all the mistakes. So far, I've found this does a pretty good job of getting rid of all of the junk where I've repeated a sentence multiple times trying to get a good take. So, this should really help to just cut all of that out. It works pretty quickly. Obviously, the most amount of time spent is just waiting for the video to get uploaded, especially if you're filming it in high quality, as this is a 3 GB file. All right. So, the video has uploaded. The transcription has uploaded as well. A prompt has already been applied to the script as well. You can see some cuts have already been made. So, this on the left-hand side is all of the script. So, we can scroll through this and have a look through the entire script of the video. So, that's pretty much what we're looking at right top. If we click at certain parts of the video, it is going to jump to that part of the video where where it is myself and it's saying that particular word, for example. So, that's how Descript works. This is the video editor. But, obviously, we don't want to spend too much time in here. We want to get out of this as quickly as possible. What we can do is just read through this entire script, make sure that it's exactly what it should be. And what we can do if we want to remove stuff is just select a section and hit the delete button, and it will literally just delete that part of the video. Or, if we want to add stuff, we can copy parts of the video to duplicate it for whatever reason. Uh but, that is how Descript works. Now, what I'll usually do is I'll jump over to the AI tools on the right-hand side. I'll then go down to shorten word gaps. I'll click into this, and I will get it to find all gaps that are more than 0.2 seconds. Find them all, and then just shorten them back down to 0.2 seconds. I don't want a big gap between multiple different takes. So, I just want to shorten down, and that's a way that we can do that. So, now that that is done, this video should be much more edited. You can see it's been cut down to 12 minutes from what I think it was about 20 minutes or something. We can see there's lots of cuts that have been made. And so, all I need to do is just watch this video, review it, and make sure that it is good to go. If anything needs changing, I can either delete certain elements, or I can delete parts of the script, or add sections back in. And that is pretty much it. All right. So, I just quickly went through and edited the entire video. I just watched the video, cut out anything that it needed to be cut out, and added anything back in that needed to be added back in. And now, it's good to go. I obviously made sure to clean up all of the gaps to be under 0.2 seconds, which is what I usually like to keep it at. And now, it's ready to go. So, this video is fully cut, um and this is pretty much ready to be edited. Now, one thing that I do do before jumping into the editing stage is I do like to add some music myself. This tool is just Epidemic Sound. I like to use this because the music doesn't get copyrighted. So, this is just why I use this tool. But, you can use anything, obviously. I just come here, download it, and add it into Descript. All right. So, I've added the music to the video now. I have now started the export process. It's now exporting locally to my computer, and I'll jump into Claude Code right now. All right. So, my video is now exported, and I'm jumping over to my Claude Code right now. So, this is the Claude desktop app. I'm not currently in Visual Studio Code for one reason, and I'll tell you about that in just a minute. But, this is where I've been doing all of my video editing. So, this is like the legitimate folder that I've done a bunch of other videos in, and I can scroll up and down. I can showcase a lot of the messages that I've sent through to add to this one folder to build the ultimate video editor for me. But, I think the best way for me to explain exactly what kind of setup that I'm looking at here in this Claude is just to ask Claude exactly what is set up here so that you can read through and have a look at exactly what's included. But, ultimately, the most important thing that we have included here is a tool called Remotion. Remotion allows us to essentially through code do video editing with graphics and text and elements and whatever. We can pretty much prompt a video or prompt a series of graphics into existence and have them fully edited onto our video. Remotion also comes with a timeline, which you'll see in just a minute. But, I can scroll through here, and you can see exactly what we're looking at in terms of rendering animations, creating animations, animating them, putting them on a timeline, cutting them, putting them on the actual video, understanding our video contextually, and just doing all of the edits. This is a pretty epic tool and a big part of this system and how we're able to do this. You can even see they've got support for Claude Code right here. It's a big use case for them, prompt a video. So, you can go to their website if you want to learn more about how to connect to this. It's incredibly easy. Just go to your Claude Code and tell it to set up Remotion for you. It will figure everything out, so you don't once again have to be technical to figure out how to do um all of the install commands. You don't honestly have to do any of them. Just tell it to install Remotion for you, and it's going to do that. So, I've just asked it, "Can you quickly break down how you were able to edit the videos so I can explain how you work to somebody else?" I'll just wait for this and read through it. So, here is the entire process, the stack. Number one, Remotion, obviously. That's a big part of this and how we're able to create these videos with animations, and that's a big part of what we do. Then, there's this tool right here, FFmpeg. That's just for extracting audio from the video files. So, when I upload the video, it needs to extract the audio, and then it uses the OpenAI Whisper API to transcribe that audio into a transcript with timestamps so that I can actually use that and give that to Remotion to create all of the graphics and animations that are relevant to the video, and also come up at the right parts of the video. And this is the process right here. So, it transcribes the video that we provide it with. It maps all of the graphics from the transcriptions to where it should be in the video. Then, it builds the video using, obviously, all React and TypeScript is what Remotion is using to do all of the graphics and animations. Then, number four, preview in Remotion Studio. So, I'll show you this in just a minute. But, we essentially get a timeline to be able to view the entire video. And then, lastly, very easily, we can render the video, have the video locally on our computer that we can then upload to YouTube or whatever. So, hopefully, pretty straightforward once you understand exactly how this works. For anything, if you have any questions, just ask Claude Code if you have a question. But, for the most part, installing all of this stuff is incredibly easy. And if you want access to this entire breakdown sheet right here, I will have this for a completely free download in my free school community. So, if you want to just take this and upload it to your own Claude to be able to do this yourself, you can do that as well. All right. So, now, all that I've done is I've just said, "Here is a new long-form video. Can you please edit this?" And this right here is all of the steps that it went through. It gave me all of the steps that it was going to edit and create graphics for. I said, "Looks good." And then, it went through and created all of the graphics for all of those different components. And then, at the bottom, you can see here, "Studio is running at this address right here, ready for preview." And one of the really cool things about the Claude desktop app is that they actually have a preview. And so, we can actually click into this and preview it right on the right-hand side of the actual Claude desktop app, which is pretty cool. So, I can, as you can see here, look at the Remotion editor. So, this is still Remotion. This is a part of their application in which we're able to look through the entire video that was just edited for us. And so, just scrolling down a bit on the timeline right here, if I just scroll down, you can see all of these blue elements and all of these blue boxes right here are all individual graphics that it's decided to that it's decided to create and put throughout the video. And so, if I wanted to, I can start to play this video and you can see the animations. I'll play it in 2x speed so you can see the graphics a bit so you can see the graphics a bit quicker. So, there you go. There's a series of animations that were fully created by Remotion itself. It's got a lot of text-based animations, but also some graphics here as well. So, you've got a comparison chart based on the content that it was talking about as well. I can continue to scroll through here and you can just see some of the animations throughout it that it has created. You can see here there's a list. There's obviously some things that need to be updated. Maybe we want to shrink this text to make it fit a bit nicer. We can scroll through here and just see all of the graphics that this has been able to edit for us. And this has done literally the entire video. I don't have to do it anything manually. I could publish this right away if I wanted to and I could just scroll through and have a look at everything in the video. So, that is pretty much it. That is my entire AI video editing process. Obviously, what I could do here is come through and ask it to change things and update things. And Claude obviously right now has access to this, so it's going to be able to make all those changes for me. And you can obviously get these graphics to be in a much more unique style. I have done a little bit of work in order to get my graphics and the editing style to be a little bit different from the basic Remotion edits. This is pretty much it for using AI and Claude Code to edit your videos. This is a video that I would be more than happy to now publish. I'll probably do a couple of checks over it to make sure it's all good to go. But, I can now go ahead and render this video and upload it to YouTube and it's all good to go. This is just one example of how I'm using Claude Code to automate all of my work. I'm doing a lot of videos on Claude Code at the moment. I'd recommend checking out this video right here. YouTube is recommending for you specifically to watch this video. So, I definitely recommend checking it out right now. I'll keep it on the screen for a couple more seconds here so you got some time to click on. I'm sure it's a great video. Make sure to click on

## Timestamped

`[00:02]` This video was edited entirely by AI.
`[00:02]` The cuts, the transitions, the text
`[00:04]` overlays, all of it. I recorded the
`[00:06]` footage, handed it off to Claude Code,
`[00:08]` and it handled the rest. I used to spend
`[00:10]` anywhere from 3 to 6 hours editing a
`[00:13]` single video, or I'd pay an editor a few
`[00:15]` hundred dollars to do it for me. Now,
`[00:17]` the entire process runs through a
`[00:19]` workflow that Claude Code manages. I
`[00:21]` simply describe how I want the video
`[00:23]` structured, and it takes care of the
`[00:24]` entire edit from raw footage through to
`[00:27]` a finished export. There's no manual
`[00:29]` scrubbing through clips, looking for bad
`[00:31]` takes. There's no repeating the same
`[00:33]` edits I've already done on the last 10
`[00:35]` videos. And once you've set this
`[00:36]` workflow up, it stays consistent across
`[00:39]` every single video. You're not
`[00:40]` rebuilding the edit from scratch every
`[00:41]` time. Because Claude already knows how
`[00:43]` your videos should look, it applies the
`[00:45]` same style automatically. This means
`[00:48]` that every video can come out with the
`[00:49]` same level of quality without the hours
`[00:51]` of work. So, in this video, I'm going to
`[00:53]` walk you through the full setup, showing
`[00:55]` you every tool involved, and show you
`[00:57]` how to build this exact workflow on your
`[00:59]` own computer. All right. So, I've just
`[01:01]` recently recorded a brand new video, and
`[01:03]` I'm just going to go ahead and start to
`[01:05]` edit this video, and just walk you
`[01:06]` through step-by-step what my process is
`[01:09]` from taking raw footage all the way to a
`[01:11]` fully edited video ready to publish. So,
`[01:14]` the first step in this process, once
`[01:15]` I've filmed a video, is to head over to
`[01:18]` this tool right here, which is called
`[01:20]` Descript. So, Descript is the one tool
`[01:23]` outside of Claude Code that I am going
`[01:24]` to be using here. And this is just what
`[01:26]` I use to very quickly edit all of the
`[01:28]` cuts in the video. And the easiest way
`[01:29]` to explain it is that editing on
`[01:31]` Descript is kind of like just editing a
`[01:33]` Word document. I'm not actually going to
`[01:35]` be manually cutting anything myself. And
`[01:37]` the reason that I'm not doing this
`[01:38]` directly through Claude Code is that I
`[01:40]` have found that, no matter how good my
`[01:42]` prompt is, there is still little things
`[01:44]` here and there that I do need to update
`[01:46]` and change when it comes to repeated
`[01:47]` sentences or some stuff getting cut out.
`[01:50]` It's definitely not perfect. I mean, it
`[01:51]` does a pretty good job of getting the
`[01:52]` majority of it done, but I do like to
`[01:54]` verify everything that I'm saying on the
`[01:56]` video to make sure that it's accurate.
`[01:58]` And so, that's why I do still use their
`[02:00]` interface here. So, I've just attached
`[02:02]` the MP4 to the video that I just
`[02:04]` recently filmed. And once I've done
`[02:06]` that, what I have, if I click browse
`[02:08]` more templates, I go up to all
`[02:09]` templates, and I click into created by
`[02:11]` me. I've essentially created my own
`[02:14]` template right here, which is just for
`[02:16]` cutting the YouTube video. So, all this
`[02:17]` really does is that it removes any
`[02:19]` duplicate sentences and just keeps the
`[02:21]` correct one. So, it just really fixes up
`[02:23]` the entire video. I'll usually just hit
`[02:25]` use template. And once I've done that,
`[02:27]` it'll start to load into the editor.
`[02:29]` Now, my video is going to start to get
`[02:31]` processed. Obviously, Descript is a
`[02:33]` cloud editing application, so you have
`[02:35]` to upload the video in order for it to
`[02:36]` get access to it. Then, all the
`[02:37]` processing and everything just happens
`[02:39]` in Descript. And if I just click into
`[02:40]` this right here, you can see the prompt
`[02:42]` template that I'm using is incredibly
`[02:44]` basic. It's not the most advanced prompt
`[02:45]` ever. I could probably work on this, to
`[02:47]` be honest. If you're interested in
`[02:48]` scaling your own AI voice agency and
`[02:50]` becoming a better AI developer, we've
`[02:53]` just released our AI Launchpad School
`[02:54]` Community. Inside, you're going to get
`[02:56]` access to a complete A to Z course on
`[02:58]` how to build AI voice agents alongside
`[03:01]` an A to Z course on how to use N8N to
`[03:03]` build AI workflows and agents. We've
`[03:05]` also partnered with BookedIN, which is a
`[03:07]` voice and chat AI client dashboard
`[03:09]` software, which you'll get as a bonus
`[03:11]` within the community. We've got over $3
`[03:13]` million in software discounts for some
`[03:15]` of the top AI and business tools,
`[03:17]` including N8N, Make, Stripe, Webflow,
`[03:20]` Lovable, and so much more. I guarantee
`[03:22]` you will make your money back in the
`[03:24]` first day using these discounts.
`[03:25]` Alongside all this, I've hired the top
`[03:28]` voice AI and automation developers to
`[03:30]` work in the community to provide
`[03:31]` unlimited technical support. So, if you
`[03:33]` ever have a question or problem you need
`[03:35]` solving, we'd love to help you out. I'll
`[03:37]` have the community linked in the
`[03:38]` description. But, it just says, "Please
`[03:39]` remove all repeating sentences."
`[03:41]` Usually, the last repeated sentence is
`[03:43]` the correct one after all the mistakes.
`[03:45]` So far, I've found this does a pretty
`[03:46]` good job of getting rid of all of the
`[03:48]` junk where I've repeated a sentence
`[03:50]` multiple times trying to get a good
`[03:51]` take. So, this should really help to
`[03:53]` just cut all of that out. It works
`[03:55]` pretty quickly. Obviously, the most
`[03:56]` amount of time spent is just waiting for
`[03:58]` the video to get uploaded, especially if
`[04:00]` you're filming it in high quality, as
`[04:02]` this is a 3 GB file. All right. So, the
`[04:04]` video has uploaded. The transcription
`[04:06]` has uploaded as well. A prompt has
`[04:07]` already been applied to the script as
`[04:09]` well. You can see some cuts have already
`[04:10]` been made. So, this on the left-hand
`[04:12]` side is all of the script. So, we can
`[04:13]` scroll through this and have a look
`[04:14]` through the entire script of the video.
`[04:16]` So, that's pretty much what we're
`[04:17]` looking at right top. If we click at
`[04:19]` certain parts of the video, it is going
`[04:21]` to jump to that part of the video where
`[04:23]` where it is myself and it's saying that
`[04:24]` particular word, for example. So, that's
`[04:27]` how Descript works. This is the video
`[04:29]` editor. But, obviously, we don't want to
`[04:31]` spend too much time in here. We want to
`[04:32]` get out of this as quickly as possible.
`[04:34]` What we can do is just read through this
`[04:35]` entire script, make sure that it's
`[04:37]` exactly what it should be. And what we
`[04:38]` can do if we want to remove stuff is
`[04:40]` just select a section and hit the delete
`[04:42]` button, and it will literally just
`[04:43]` delete that part of the video. Or, if we
`[04:45]` want to add stuff, we can copy parts of
`[04:46]` the video to duplicate it for whatever
`[04:48]` reason. Uh but, that is how Descript
`[04:50]` works. Now, what I'll usually do is I'll
`[04:51]` jump over to the AI tools on the
`[04:53]` right-hand side. I'll then go down to
`[04:54]` shorten word gaps. I'll click into this,
`[04:56]` and I will get it to find all gaps that
`[04:59]` are more than 0.2 seconds. Find them
`[05:01]` all, and then just shorten them back
`[05:02]` down to 0.2 seconds. I don't want a big
`[05:05]` gap between multiple different takes.
`[05:07]` So, I just want to shorten down, and
`[05:08]` that's a way that we can do that. So,
`[05:09]` now that that is done, this video should
`[05:11]` be much more edited. You can see it's
`[05:12]` been cut down to 12 minutes from what I
`[05:14]` think it was about 20 minutes or
`[05:15]` something. We can see there's lots of
`[05:16]` cuts that have been made. And so, all I
`[05:18]` need to do is just watch this video,
`[05:19]` review it, and make sure that it is good
`[05:21]` to go. If anything needs changing, I can
`[05:23]` either delete certain elements, or I can
`[05:25]` delete parts of the script, or add
`[05:27]` sections back in. And that is pretty
`[05:29]` much it. All right. So, I just quickly
`[05:30]` went through and edited the entire
`[05:32]` video. I just watched the video, cut out
`[05:34]` anything that it needed to be cut out,
`[05:35]` and added anything back in that needed
`[05:37]` to be added back in. And now, it's good
`[05:38]` to go. I obviously made sure to clean up
`[05:40]` all of the gaps to be under 0.2 seconds,
`[05:42]` which is what I usually like to keep it
`[05:44]` at. And now, it's ready to go. So, this
`[05:45]` video is fully cut, um and this is
`[05:47]` pretty much ready to be edited. Now, one
`[05:49]` thing that I do do before jumping into
`[05:51]` the editing stage is I do like to add
`[05:52]` some music myself. This tool is just
`[05:54]` Epidemic Sound. I like to use this
`[05:56]` because the music doesn't get
`[05:57]` copyrighted. So, this is just why I use
`[05:59]` this tool. But, you can use anything,
`[06:00]` obviously. I just come here, download
`[06:02]` it, and add it into Descript. All right.
`[06:04]` So, I've added the music to the video
`[06:05]` now. I have now started the export
`[06:07]` process. It's now exporting locally to
`[06:09]` my computer, and I'll jump into Claude
`[06:11]` Code right now. All right. So, my video
`[06:13]` is now exported, and I'm jumping over to
`[06:15]` my Claude Code right now. So, this is
`[06:18]` the Claude desktop app. I'm not
`[06:19]` currently in Visual Studio Code for one
`[06:21]` reason, and I'll tell you about that in
`[06:23]` just a minute. But, this is where I've
`[06:24]` been doing all of my video editing. So,
`[06:26]` this is like the legitimate folder that
`[06:27]` I've done a bunch of other videos in,
`[06:29]` and I can scroll up and down. I can
`[06:31]` showcase a lot of the messages that I've
`[06:32]` sent through to add to this one folder
`[06:34]` to build the ultimate video editor for
`[06:36]` me. But, I think the best way for me to
`[06:37]` explain exactly what kind of setup that
`[06:39]` I'm looking at here in this Claude is
`[06:41]` just to ask Claude exactly what is set
`[06:43]` up here so that you can read through and
`[06:44]` have a look at exactly what's included.
`[06:46]` But, ultimately, the most important
`[06:48]` thing that we have included here is a
`[06:50]` tool called Remotion. Remotion allows us
`[06:52]` to essentially through code do video
`[06:54]` editing with graphics and text and
`[06:56]` elements and whatever. We can pretty
`[06:58]` much prompt a video or prompt a series
`[07:00]` of graphics into existence and have them
`[07:02]` fully edited onto our video. Remotion
`[07:04]` also comes with a timeline, which you'll
`[07:05]` see in just a minute. But, I can scroll
`[07:07]` through here, and you can see exactly
`[07:08]` what we're looking at in terms of
`[07:10]` rendering animations, creating
`[07:11]` animations, animating them, putting them
`[07:13]` on a timeline, cutting them, putting
`[07:14]` them on the actual video, understanding
`[07:16]` our video contextually, and just doing
`[07:18]` all of the edits. This is a pretty epic
`[07:20]` tool and a big part of this system and
`[07:22]` how we're able to do this. You can even
`[07:23]` see they've got support for Claude Code
`[07:24]` right here. It's a big use case for
`[07:26]` them, prompt a video. So, you can go to
`[07:28]` their website if you want to learn more
`[07:29]` about how to connect to this. It's
`[07:30]` incredibly easy. Just go to your Claude
`[07:32]` Code and tell it to set up Remotion for
`[07:34]` you. It will figure everything out, so
`[07:35]` you don't once again have to be
`[07:36]` technical to figure out how to do um all
`[07:39]` of the install commands. You don't
`[07:40]` honestly have to do any of them. Just
`[07:41]` tell it to install Remotion for you, and
`[07:43]` it's going to do that. So, I've just
`[07:45]` asked it, "Can you quickly break down
`[07:46]` how you were able to edit the videos so
`[07:48]` I can explain how you work to somebody
`[07:49]` else?" I'll just wait for this and read
`[07:51]` through it. So, here is the entire
`[07:53]` process, the stack. Number one,
`[07:54]` Remotion, obviously. That's a big part
`[07:56]` of this and how we're able to create
`[07:57]` these videos with animations, and that's
`[07:59]` a big part of what we do. Then, there's
`[08:00]` this tool right here, FFmpeg. That's
`[08:03]` just for extracting audio from the video
`[08:04]` files. So, when I upload the video, it
`[08:06]` needs to extract the audio, and then it
`[08:08]` uses the OpenAI Whisper API to
`[08:10]` transcribe that audio into a transcript
`[08:13]` with timestamps so that I can actually
`[08:15]` use that and give that to Remotion to
`[08:17]` create all of the graphics and
`[08:18]` animations that are relevant to the
`[08:19]` video, and also come up at the right
`[08:21]` parts of the video. And this is the
`[08:23]` process right here. So, it transcribes
`[08:25]` the video that we provide it with. It
`[08:27]` maps all of the graphics from the
`[08:28]` transcriptions to where it should be in
`[08:30]` the video. Then, it builds the video
`[08:32]` using, obviously, all React and
`[08:33]` TypeScript is what Remotion is using to
`[08:35]` do all of the graphics and animations.
`[08:37]` Then, number four, preview in Remotion
`[08:39]` Studio. So, I'll show you this in just a
`[08:40]` minute. But, we essentially get a
`[08:41]` timeline to be able to view the entire
`[08:43]` video. And then, lastly, very easily, we
`[08:45]` can render the video, have the video
`[08:47]` locally on our computer that we can then
`[08:49]` upload to YouTube or whatever. So,
`[08:51]` hopefully, pretty straightforward once
`[08:52]` you understand exactly how this works.
`[08:54]` For anything, if you have any questions,
`[08:55]` just ask Claude Code if you have a
`[08:56]` question. But, for the most part,
`[08:57]` installing all of this stuff is
`[08:58]` incredibly easy. And if you want access
`[09:00]` to this entire breakdown sheet right
`[09:02]` here, I will have this for a completely
`[09:04]` free download in my free school
`[09:05]` community. So, if you want to just take
`[09:06]` this and upload it to your own Claude to
`[09:08]` be able to do this yourself, you can do
`[09:10]` that as well. All right. So, now, all
`[09:11]` that I've done is I've just said, "Here
`[09:13]` is a new long-form video. Can you please
`[09:15]` edit this?" And this right here is all
`[09:17]` of the steps that it went through. It
`[09:18]` gave me all of the steps that it was
`[09:19]` going to edit and create graphics for. I
`[09:21]` said, "Looks good." And then, it went
`[09:23]` through and created all of the graphics
`[09:24]` for all of those different components.
`[09:26]` And then, at the bottom, you can see
`[09:27]` here, "Studio is running at this address
`[09:29]` right here, ready for preview." And one
`[09:31]` of the really cool things about the
`[09:32]` Claude desktop app is that they actually
`[09:34]` have a preview. And so, we can actually
`[09:37]` click into this and preview it right on
`[09:39]` the right-hand side of the actual Claude
`[09:41]` desktop app, which is pretty cool. So, I
`[09:43]` can, as you can see here, look at the
`[09:45]` Remotion editor. So, this is still
`[09:47]` Remotion. This is a part of their
`[09:48]` application in which we're able to look
`[09:50]` through the entire video that was just
`[09:52]` edited for us. And so, just scrolling
`[09:54]` down a bit on the timeline right here,
`[09:56]` if I just scroll down, you can see all
`[09:58]` of these blue elements and all of these
`[10:00]` blue boxes right here are all individual
`[10:02]` graphics that it's decided to that it's
`[10:04]` decided to create and put throughout the
`[10:06]` video. And so, if I wanted to, I can
`[10:08]` start to play this video and you can see
`[10:10]` the animations. I'll play it in 2x speed
`[10:11]` so you can see the graphics a bit
`[10:12]` so you can see the graphics a bit quicker.
`[10:26]` So, there you go. There's a series of
`[10:26]` animations that were fully created by
`[10:28]` Remotion itself. It's got a lot of
`[10:30]` text-based animations, but also some
`[10:31]` graphics here as well. So, you've got a
`[10:33]` comparison chart based on the content
`[10:35]` that it was talking about as well. I can
`[10:36]` continue to scroll through here and you
`[10:37]` can just see some of the animations
`[10:39]` throughout it that it has created. You
`[10:41]` can see here there's a list. There's
`[10:42]` obviously some things that need to be
`[10:43]` updated. Maybe we want to shrink this
`[10:44]` text to make it fit a bit nicer. We can
`[10:46]` scroll through here and just see all of
`[10:48]` the graphics that this has been able to
`[10:50]` edit for us. And this has done literally
`[10:52]` the entire video. I don't have to do it
`[10:54]` anything manually. I could publish this
`[10:55]` right away if I wanted to and I could
`[10:56]` just scroll through and have a look at
`[10:58]` everything in the video. So, that is
`[11:00]` pretty much it. That is my entire AI
`[11:02]` video editing process. Obviously, what I
`[11:04]` could do here is come through and ask it
`[11:05]` to change things and update things. And
`[11:07]` Claude obviously right now has access to
`[11:09]` this, so it's going to be able to make
`[11:10]` all those changes for me. And you can
`[11:11]` obviously get these graphics to be in a
`[11:12]` much more unique style. I have done a
`[11:14]` little bit of work in order to get my
`[11:16]` graphics and the editing style to be a
`[11:17]` little bit different from the basic
`[11:19]` Remotion edits. This is pretty much it
`[11:21]` for using AI and Claude Code to edit
`[11:23]` your videos. This is a video that I
`[11:24]` would be more than happy to now publish.
`[11:26]` I'll probably do a couple of checks over
`[11:28]` it to make sure it's all good to go.
`[11:29]` But, I can now go ahead and render this
`[11:31]` video and upload it to YouTube and it's
`[11:33]` all good to go. This is just one example
`[11:35]` of how I'm using Claude Code to automate
`[11:36]` all of my work. I'm doing a lot of
`[11:38]` videos on Claude Code at the moment. I'd
`[11:40]` recommend checking out this video right
`[11:41]` here. YouTube is recommending for you
`[11:43]` specifically to watch this video. So, I
`[11:45]` definitely recommend checking it out
`[11:46]` right now. I'll keep it on the screen
`[11:48]` for a couple more seconds here so you
`[11:49]` got some time to click on. I'm sure it's
`[11:50]` a great video. Make sure to click on
