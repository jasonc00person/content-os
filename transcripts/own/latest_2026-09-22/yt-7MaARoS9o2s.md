---
id: yt-7MaARoS9o2s
platform: youtube
url: https://www.youtube.com/watch?v=7MaARoS9o2s
views: 57879
likes: 807
date: 2026-09-08
duration_s: 817
caption: "Claude edited this entire video in ONE SHOT"
era: current
format: build-in-public
hook_type: title
spoken_hook: "Claude edited this entire video in ONE SHOT"
---

# Claude edited this entire video in ONE SHOT — 57,879 views

This video was edited by Claude in one shot.
That's right.
I didn't have to sit there and babysit or keep prompting back [music] and forth to get the
edit right.
One prompt, one go.
I'll even have Claude put up the prompt right here so you can see the one [music] single
prompt that triggered this entire edit.
Now, look.
There have been a lot of videos out there on the internet about Claude video editor.
I even built my own months ago and I've been iterating upon it ever since.
And after receiving a ton of feedback from my customers, my audience, and my community, I
noticed one huge problem with all of these Claude video editors.
They all lack autonomy.
Here is the harsh reality that a lot of these AI gurus aren't telling you about.
Claude by itself lacks the creativity, the taste, and [music] workflow instructions to be
able to do an entire edit end-to-end and have it come out like actually postable.
Like, it can do the edit, but you still have to sit there and prompt it and give it
direction for possibly a couple hours, which kind of defeats the purpose of having an AI
video editor in the first place.
Because what we really want is to be able to give Claude raw footage, tell it to do the
entire edit, no further instructions, and come back two or three hours later to a fully
finished postable edit.
And so, in today's video, that is what I will be attempting to build.
Something that I genuinely have never seen before on the internet [music] from anyone else,
or at least not of this high quality.
So, by the time you're watching this, it's already been built, and [music] whatever you're
watching right now is the direct result of Claude.
One prompt, no further work, no further tune-ups, no Like, I didn't touch it.
I even recorded the entire process start to finish.
So, for you skeptics out there, you can literally watch that entire video of Claude doing
this entire edit with just one prompt.
That'll be linked in the description.
Just so you know that I'm not lying.
I am going to walk you through exactly how I built this and exactly how you can build a
system like this for yourself, so you can fully automate your video editing and have AI edit
your videos for you in your sleep and have it come out actually good.
Let's get into it.
All right, guys.
So, everything from here on out is not part of the one-shot edit.
I just want to make that clear.
Claude did in fact edit the rest of this video and everything that you're watching right
now.
But, uh you know, obviously I had to record the intro first and do that in one shot.
It probably could have one-shotted the whole video, but anyways.
So, basically, it's a Claude code project with a bunch of files, right?
You see all these files, assets, docs, packaging, presets, blah blah blah.
This is all the code and all the files that Claude needs to be able to then control Premiere
Pro, DaVinci Resolve, and ultimately, you know, make a video edit all on its own.
Now, the problem is that Fable 5.1, the latest greatest frontier model, still lacks the
creativity, taste, and workflow knowledge to be able to produce postable end-to-end edits.
And so, the plan on how I'm actually going to do this video and build this one-shot uh video
editor is basically to build one big presets folder.
And that means everything like color grading, adding text animation, zoom ins, outs, pop-in
animations, rise and animations, light and dark preset backgrounds, rules and protocols for
how to create graphics, when to create graphics, SFX rules and presets.
Every single animation needs to be like a preset that I custom built and custom tuned so
that it actually comes out looking good.
Otherwise, it would just come out, you know, looking like AI generic slop.
Instead of relying on the AI to know how to edit, which it doesn't, we're going to use the
my human creativity and editing genius to craft a a style and then basically lock it in so
that it doesn't have to think about how to do the zoom ins or the pop ins or the rise ins.
So, here is a map of the system architecture of what the entire thing I built actually looks
like.
So, basically we have our raw footage, we do the intake, we do the rough cut.
We're using Whisper X for the rough cut.
We also have sub agents in a a recursive loop workflow in the rough cut where we kind of
loop over to make sure that the rough cut is like actually good before we move on.
And then we have audio polish.
We are going to do the color grade.
We have three steps within the graphics skill, right?
There's actually a graphics plan skill, a graphics build skill, and then a edit review skill
where we kind of loop back and forth to get rid of all those defects and all those errors
before it even comes time for us to review it, right?
And then what we have is SFX.
So, I'm going to build or I already built a specific workflow and plan for which uh sound
effects to use at which points.
Then we can do a music bed.
So, then it's up to you to review.
Here's where you would do the further refinements, right?
And then it can render.
I built a YouTube default preset.
So, anytime I put a horizontal video in, it's going to just use the default YouTube preset,
right?
This makes it easy for the community members to like build their own presets if they want a
different editing style.
We can see we have the presets folder and we have the lanes folder and the lanes has all of
everything about how to work the different apps, right?
So, right now we have CapCut, Premiere, and Resolve.
I would say Premiere and Resolve are like the two best functioning ones.
CapCut is like So, now I'm going to show you guys the demo clip of the live run uh where it
took like a full I think almost like 2 and 1/2 hours of Claude editing the intro that you
just watched end to end.
All right, guys.
This is the moment of truth.
I have been working on this video editor project for about a week and a half now.
I've been tweaking it and I think it's good enough to get a one-shot edit going.
So, I am just going to take whatever I it gives me and post it and show you guys what it can
do completely on its own.
So, I'm going to start it off with one prompt.
We are going to get the raw footage, which I believe is this right here.
So, it's the raw footage of the intro and then for the background music, we're going to be
using this right here.
So, I am going to do that and then copy the paths there.
Hey, I want you to edit this video fully end to end.
I have given you the background music that I want there, the home we're finally landing
music, so use that as the background music.
And edit this video end to end.
The only real request that I have is for when I when I say, "Oh, like there have been a lot
of videos about Claude, a video editor out there.
I want you to pull real YouTube thumbnails uh from the YouTube and use that as like the
graphic to visually show when I'm talking about like, "Oh, there's a lot of other videos out
there about Claude video editor." So, go ahead and start on this edit.
Don't stop until you're finished.
Boom.
Okay, guys.
Okay, so I'm going to keep recording this entire process.
Premiere is not even up, so it should be able to open up Premiere on its own.
So, I'm going to leave this.
It's probably going to take about 2 hours, but we'll leave this and we'll see how it does
how it gets done.
I will come back probably when it's done.
Okay, peace.
>> Okay, guys.
I just got back from the store and I think it should be done now.
I don't know what this was, but um cool.
>> [music] >> Yo, let's go.
Okay, it did it.
It did it.
It did it.
I think it worked.
Okay, total 2 hours 42 minutes.
It only used up 740k of the context window, so So, I think that's going to conclude it for
this video.
I really just recorded this for proof, just so that you know, like it really was a one shot.
Now, guys, if you want to build a system like this for yourself, um by the time you're
watching this, the build is already done.
It's published in my school.
And here we have a super thriving community of members who are all using the Claude video
editor, all building on it, and helping out each other in our content creation journey.
And I also host group calls twice a week.
So, you can come talk to me live and I will actually help you one-on-one if you have any
questions, problems, issues with AI or leveraging it to get out content faster.
Guys, if you want to do this for free, if you don't want to pay for my school, that's
totally fine.
You can try building this from scratch for yourself.
I will publish this Claude artifact down at the link in the description below, so you can
copy this, put that into Claude, see if it can, you know, build this entire thing from that.
You can also check out my other videos, like this one right here.
This is the one that I would suggest checking out if you want to build it on your own,
because I give you some prompts and I kind of walk through, you know, more in-depth how I
built it from start to finish.
You can also paste the transcript of this YouTube video into Claude and kind of build it
that way.
Well, guys, after multiple long days and weeks of working and grinding, we finally did it.
We got it to do a full, pretty good edit all in one shot.
Now, obviously, it definitely could have been better if I did some further refining, even
through prompting.
Normally, I would do that, but for the purpose of this video, I wanted to leave it just raw,
what came from Claude, so you can see how good it is.
Claude and AI integrating into video editing is coming.
There's no avoiding it.
For me, as a content creator, you know, video editing is one of the hardest, longest things
to do in the entire process.
And And so, if this is going to solve that pain point, and I can further have control and
tweak it if I want to, I mean, that's a huge, huge value add.
I'm just trying Honestly, I'm just trying my best to make cool that really helps people.
I I'm not trying to put anyone out of job or do anything like that.
I think if you are a video editor, you know, you should use this to speed up your workflow,
keep your job, get paid the same amount, but work less, because Claude can do, I would say,
80% of the work for you now.
If you are a content creator who wants to just say, just give your raw footage to Claude and
be like, "Yo, edit this video." And then come back 3 hours later to a fully edited video
that's like ready to post, then I would say like this is for you.
I think a lot of the AI gurus out there are talking about, "Oh, like Oh, here's how AI can
save you time, save you money, or like replace this part of your workflow." But rarely ever
do you see some piece of like actually economically valuable time-saving automation.
And I think that Claude video editor is one of those rare gems where it's like, "Damn, this
actually is fully replacing an entire position and department in my business." Before I had
to hire an editor, or I had to spend, you know, 6 to 8 hours editing a full YouTube video.
And now, I literally can just say, "Edit the video." Walk like overnight, or walk away, go
to the gym, do whatever you need to do for 3 hours, you come back and it's done.
You know, I'mma do one one plug now.
So, if you guys want the entire package completely built out, all done for you, all of these
files and everything already works, already built.
Look, you can either spend hours upon hours and maybe even weeks trying to build this on
your own by watching my videos and taking the transcripts and prompting back and forth, or
you can just get the files that already work straight out of the box that I already took the
time to build over months, and you can just download these.
And then you can do whatever you want with the files.
You own it.
So, if you want to do that, you can join my school community down below.
I'm not trying to sell you a SaaS, like get you hooked on a subscription or whatever, or
sell you some shitty SaaS about like some AI plugin for a Premiere Pro.
Nah, like you just get the files.
It's all of my work that I've been working on for the past months, and it will be able to
edit full YouTube videos end to end, just like the ones I showed you.
Fair warning, it can it only is really good at like talking head educational videos, right?
If you're doing vlogs or visual-based content, it's going to be harder.
And if you're doing vertical content, like for Instagram or TikTok, I haven't built a preset
out for that yet, but I probably will.
If you're doing YouTube videos and they're talking head, they're educational, I definitely
think this is going to be of great value to you.
Even if you're doing like vlog content or visual-based content, I'm sure that we're going to
me and the community are going to cook up like something for that soon.
If you're a content creator, you want to speed up and use AI not only for the video editing,
but you want to let like learn how to implement AI into your workflow so you can actually
save real time and money like I have been with this AI video editor, you can join the
community.
If you go to the classroom, go to Cloud Video Editor, you can download the folder.
It's all right there once you join, and there's a full setup guide and everything as well.
You also get all of my other automations, too.
There's a whole Cloud Code for Dummies course, so even if you're a beginner, I promise like
we got you sorted.
We got the Content OS automations, we got Cloud Finance.
We got a ton of stuff in here, guys.
So, join at the first link down in the description.
I hope to see you in there.
I hope you guys found this video valuable.
I'll see you in the next one.
Peace.
