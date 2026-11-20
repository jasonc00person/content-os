---
id: yt-fSJh8etPngU
platform: youtube
url: https://www.youtube.com/watch?v=fSJh8etPngU
views: 95911
likes: 2353
date: 2026-08-07
duration_s: 1142
caption: "I Let Claude Edit My Entire Video in DaVinci Resolve (Full Setup)"
era: current
format: tutorial-walkthrough
hook_type: title
spoken_hook: "I Let Claude Edit My Entire Video in DaVinci Resolve (Full Setup)"
---

# I Let Claude Edit My Entire Video in DaVinci Resolve (Full Setup) — 95,911 views

Behold, Claude can now take full control over DaVinci Resolve and do edits completely done
for you.
This is big news for the unemployed as we now have more time to scroll Instagram reels while
Claude does all of our work for us.
No, but seriously guys, this is an actually insanely powerful workflow that I'm about to
show you and I promise it's going to save you a ton of hours when it comes to manual editing
labor and it's going to allow you to edit much higher quality videos.
So, whether you're a content creator or a video editor, buckle up, strap in because I'm
about to put you on game for completely free.
By the end of this video, I promise you're going to have a fully functioning, working AI
video editing assistant that can do rough cuts, advanced motion graphics, title cards, color
grading, exporting, and more.
So, without further ado, let's get into the video.
All right, guys.
So, I'm going to cover everything that you need to set this up and get started.
So, there are a couple prerequisites.
Let's go over them right now.
So, obviously the first thing you that you're going to need is Claude code.
You can do the $20 a month plan.
I think Sonnet 5 will work, but you might run into limits.
I would recommend being on the $100 a month plan so that you can use Opus 5 freely and not
have to run into any limits.
So, get on a Claude code plan.
That's the first thing that we're going to need.
Now, the next thing is going to be obviously DaVinci Resolve.
I think the free version should work.
If you want to try it out with the free version, you can.
I haven't tested it, but I'm pretty sure it will work with the MCP.
But, if you clicked on this video, probably means you already have DaVinci Resolve Studio
anyways.
And if you don't have Studio and you want to try this out, it's only $30 a month.
You can actually sort of get a license from their Blackmagic Cloud website.
If you do decide that you like DaVinci Resolve Studio and you decide you're going to be
using it for more than 10 months, then, you know, it'd be cheaper to go with the $295
lifetime.
But, if you just want to try out DaVinci Resolve Studio, again, $30 a month.
So, that's all the paid stuff.
Now, here's what we're going to be using for free because it's already, you know, just open
source out on the internet.
So, the first thing that we need is the HyperFrames GitHub repo.
This is the engine that allows Claude to create motion graphics.
Next thing we're going to need is the DaVinci Resolve MCP.
Again, this is a free open source repo on GitHub that allows Claude to connect to DaVinci
Resolve and actually control it.
third thing is we're just going to need, again, some more free open source tools like
Whisper X, a bunch of CLI tools like Homebrew, FFmpeg, UV, Node, Python.
This is just basic coding stuff that Claude needs to be able to run, uh, you know, this
entire video editing system.
So, lucky for you guys, I have created a completely free prompt that I'm going to give you
guys link in the description.
If you just go down in the description and click that free prompt and have that in hand
ready to go, then that covers all of this open source free stuff.
So, you don't need to worry about it.
It'll install everything for you or just walk you through installing it.
So, the free prompt will be linked in the description as well as probably a link to where
you can go to get that $30 month license to try out DaVinci Resolve Studio.
Now, if you're someone who values your time and you don't want to spend the time and hours
and work to set all this stuff up with all the blah blah blah and you want a folder of files
that is already like set and ready to go with all of these skills and all of these assets,
docs, packaging, presets, workflows, and all this stuff, this is all included in my school
community and that'll be the first link down in the description below.
If you join my school, you can skip the tutorial and just go straight into use cases and get
started right away.
And I also host group calls twice a week so I can hop on live and you can speak to me.
I will help you out with your problem.
So, you can join the school if you want to skip all this busy work.
But, for those of you that are doing this for free, just have this free prompt that's linked
in the description.
Have that ready to go and we're going to move into the setup now.
I'll see you there.
All right, guys.
Let's get into the free setup guide.
So, the first thing that we want to do is open up Finder.
If you're on Windows, that's going to be your File Explorer.
You just want to open up your files right here.
I already have a projects folder set up, but if you want to set up a projects folder to
house all of your Claude code projects, then what you can do is click view, and then you can
click this thing right here that says show path bar, and that's going to show you the path
back to your user folder.
And in here, you can click to create a new folder and call it projects.
Then you can take that projects folder and drag it to your sidebar, so it's easily
accessible.
I already have this set up, and as you can see, I have a lot of Claude code projects already
made.
So, now that we're in here, we're going to click to create a new folder.
We're going to call this Claude Resolve Editor.
Something like that is fine.
Once you have that folder created, then we're going to go back into Claude code, and we're
going to click this little folder thing right here.
We're going to click open folder, and find that folder that you just created.
Click that, click open.
Now we are in the correct project folder.
Now we can take this free prompt.
Just command A, command C, copy everything, go back to Claude code, paste in that free
prompt, hit enter, and then we're ready to go.
So, it's going to install all the CLI tools, it's going to install the MCP.
It already has both the links to the uh DaVinci Resolve MCP and the Hyperframes MCP, so
that's all taken care of.
It'll install all of that like pretty much automatically.
The one thing that you might need, if you've if you're new to Claude code, you'll probably
need to install Homebrew, which that might require you entering some commands in a terminal,
and entering your password.
You just want to make sure that Homebrew's installed.
Ask If you get confused, just ask chat.
Be like, "Yo, I don't know what to do.
Explain this to me like I'm a 12-year-old.
Just walk me through this so that I can get this done and everything set up.
Once it gets done though, you open up DaVinci Resolve, you test the connection and it's
ready to go.
Then you're pretty much good to go.
You just might need to chat back and forth and get some things installed like Homebrew,
etc., etc.
And this is going to give you the basic functionality.
Now, if you join my school community and you downloaded the folder from right here in this
tab in the classroom section, then you should be good to go already.
It like it comes with a lot of the basically everything's already built out.
So, you know, you're pretty much good to go there.
But yeah, give this a couple things, install Homebrew, get everything installed.
Once it's ready, you're ready to move on to the next section.
All right, guys.
For the first use case, we're going to be doing a rough cut.
Now, I am actually building the video that you're watching right now.
So, I'm going to build the rough cut of the intro that you just watched in this YouTube
video.
So, let's start.
I'm in the video editor project folder.
I'm on Opus 5, which is fine.
I think Sonic will work fine, too.
But anyways, let's get on with the prompting.
Yo, what up?
I just recorded the intro to a new YouTube video in my downloads folder.
So, I want you to do the rough cut and set it up in DaVinci Resolve, create a new project
for it with the name and everything, and also check Notion for the correct page.
It's the one about Claude and DaVinci Resolve.
That's the new YouTube video project that we're working on.
And let me know when you're done.
I'm sending off that prompt.
And now I'm going to time how long this takes.
Time starting now.
Done.
There we go.
Pause timer, and that took exactly 5 minutes and 41 seconds.
And as you can see, it built the entire rough cut in DaVinci Resolve for us.
Pretty good and pretty straightforward.
So, let's move on to the next use case, shall we?
All right, guys.
Let's move on to use case number two, which is motion graphics.
So, I have this rough cut of my YouTube intro right here, and we're going to put some motion
graphics on top.
So, I'm going to open a new chat, and for this, I'm using Opus 5 on high, and I'm just going
to prompt something like this.
Hey, so for the current YouTube intro that I have open on my DaVinci Resolve timeline, I
want you to do a graphics pass.
So, first, like plan like, you know, read the whole script of the intro or see what's on the
timeline, and then plan out what we should do for the graphics.
Think really, really hard about it to create like actually good graphics that are really on
point.
And then what I want you to do is create them, create all of them, put them on the timeline,
and then and then after that, I want you to do a second pass over each of the graphics
elements.
So, for each of them, I want you to go one by one through them and like adjust them and
refine them so that they're absolutely dialed in.
They're placed correctly, nothing is off, right?
None of the everything all the effects are working correctly.
I need them absolutely dialed in, and I want you to take your time with each of the graphics
one by one after you do the initial pass.
So, go ahead and do that now.
Take as much time as you need.
Okay, guys.
So, I'm going to send off that voice prompt right now, and I'm going to start a timer and
come back when this is done.
All right, guys.
I'm back, and that took a full 1 hour and 38 minutes.
Almost 1 hour and 48 minutes.
But, I think it's because I was like, "Yo, like take as much time as you need and dial it
in." And it did do a very impressive job.
Like it really went to town, and I'll actually play the clip for you right now.
Behold, Claude can now take full control over DaVinci Resolve and do edits completely done
for you.
This is big news for the unemployed as we now have more time to scroll Instagram reels while
Claude does all of our work for us.
No, but seriously, guys, this is an actually insanely powerful workflow that I'm about to
show you, and I promise it's going to save you a ton of hours when it comes to manual
editing labor, and it's going to allow you to edit much higher quality videos.
So, whether you're a content creator or a video editor, buckle up, strap in, because I'm
about to put you on game for completely free.
By the end of this video, I promise you're going to have a fully functioning, working AI
video editing assistant that can do rough cuts, advanced motion graphics, title cards, color
grading, exporting, and more.
Okay, guys, so that was very, very impressive.
Like, obviously, it did a really good job, especially for just being fully autonomous.
Like, I didn't even give it any directions, and it was able to come up with some really
amazing graphics.
It's not even on Fable, it was on Opus.
So, pretty amazing.
And if you want like super intense like crazy motion graphics like that, then definitely you
could leave it overnight, you know, or something like that, especially if you have a longer
thing you're trying to edit.
So, that's useful.
It wasn't exactly what I was actually looking for, and that reminds me, this is a good piece
of knowledge for you to know is that you got to be very specific about what you want, right?
The AI is like a genie.
Like, if you leave one little detail out, like, you got to be careful what you wish for,
right?
So, um you just have to be very, very, very specific about what you prompt.
So, I'm going to actually try and really do this right now.
Actually, for the first two clips, you can leave like we don't need any graphics for that,
cuz I'm going to do that manually.
I'll probably get some stock footage and do some like very light like meme editing for the
first two uh clips.
So, everything else is pretty much good.
I do actually like the full frame like full frame with the background and everything for the
very last C2 graphic.
All that we really need to change here is Look, let's just change the style to the more like
um modern UI style.
We can keep it 12 frames per second to get that like um posterized time effect, but I
definitely do want a more like modern uh like glow like uh tech, you know, like UI look.
Maybe like a dark blue color palette.
And we can use our dark blue grid background that we already have.
So, everything else you can basically just like restyle.
Um you can get rid of the the graphics on the first two clips, which is like what you spent
the most time on.
We actually don't need that at all.
Just kind of like restyle everything else.
Everything else looks fine.
And then when I say like oh, for free like definitely that should be like the free should be
like glowing green or something, you know?
And then your own personal AI video editor, that doesn't need to be a full frame.
Like that can just be like a graphic that comes up.
It's like the cloud mascot.
Maybe he's glowing and like controlling a timeline or something.
But that doesn't need me to to be a full frame.
It should be overlay that comes over me.
Try again.
And look, I want this to be like 30 minutes max, okay?
The last one took like a whole hour and 40 minutes.
I just want this to be like 30 minutes.
Get it done.
Put it on the timeline so I can review it.
Go ahead and do that now.
All right, guys.
So, we're going to send off that prompt.
Send that off.
And again, I'm going to time this.
And this is going to be a little bit more accurate of a timer for like how long it takes to
do the graphics.
It really depends on what you want.
If you want to take more time and spend longer on it, you totally can and just leave it like
overnight or something like that.
But um if you're like working on it like this, then you definitely want like faster
iterations.
And so, this should be fine.
So, we're going to time it.
I'll see you in a bit.
All right.
So, that just got done.
And the timer I lost the timer.
So, I'm going to have to check the time from when it started.
Okay, I like that a lot better.
And so, this is looking good, actually.
Really, all we need to do is just kind of move move this stuff around, so we could just move
this over here.
Kind of make it smaller, move it over here, etc., etc.
That's no biggie.
But, yeah, I think this is a lot better, so much faster, and this should show you how good
it is at creating graphics autonomously.
So, yeah, I'd say that we'll call this demo done.
All right, let's move on to the final use case.
>> [music] >> All right, guys.
So, for the final use case here, we're going to have the AI help us out with some color
grading.
So, I have this intro of the video right here, and I want to color grade it.
So, what I'm going to do is go into Claude and hop into a new chat.
Make sure that I'm in the video editor.
I'm in the correct folder.
And I'm going to voice prompt.
Yo, what's up?
I want to color grade the intro of my DaVinci Resolve project that I'm working on right now.
And I already have a LUT that I want you to use, so I'm going to give that to you right now.
The AI can actually build and color grade using LUTs that it builds itself, but it's really
not that good at it since, you know, AI doesn't really have vision like that.
So, let's just give it a preset LUT.
And for this, I'm going to go in my finder, and I'm going to search for The one that I
typically like to use is London.
So, I have this London Rec.
709.cube.
I'm just going to copy this copy the the file path, and then I'm just going to paste that
in.
So, go ahead and color grade the intro of this video.
Toss on that LUT, please.
Thank you.
Yeah, that's all I really need to say.
What it's going to do now is it's going to group together all of the intro clips and color
grade them for me.
Let's see how it does.
Honestly, this is something that you could probably just do manually anyways.
I mean, it doesn't really take that much time, but I just want to show you guys the
capabilities of what this can do.
You know, maybe if you toss on this prompt at the end of another big string of things that
you're doing, you just want to have it do it autonomously.
That might be useful.
So, I'll come back when it's done.
So, that just got finished and it that really only took like 2 minutes.
2 minutes, very quick.
So, it did a good job.
Kind of it even like rendered everything and checked for us to make sure before it Oh, it
gave us a comparison.
Cool.
If we go to the color view, it's you can see it grouped all of the clips together, which is
awesome.
So, now we have all of our intro clips grouped.
Okay, very cool.
So, it applied the LUT here and I want to tone it down to 75%.
So, I'm just going to go key and then I can go key output gain and go 0.75 and that like
tones down the intensity of the LUT LUT.
Okay, so one very important thing to note here, guys, is that it can do the grouping of the
clips for you and it can apply a LUT to the clips all by itself, but it cannot add further
nodes and effects.
So, for example, if you wanted to add some glow, you're going to have to drag that in
yourself and do the, you know, blah blah blah.
Unfortunately, the MCP currently is not capable of adding in more nodes and effects.
It can do that infusion, you know, for effects like that, but uh in terms of color, it
unfortunately cannot.
I don't know why it can add nodes and do things in fusion, but not in color.
Kind of silly, in my opinion.
I feel like they should give it that capability.
Anyways, so next we're going to be doing some manual hand tweaking and adjusting to add some
more effects on top of this color grade.
Boom, that's so tough.
Okay, so before, after, before, after.
Nice.
But as you can see, uh it helps to speed up our color grading process.
So, very cool.
And that's going to be the last use case.
>> [music] >> If you guys try to build this entire Cloud video editor for yourself for free,
you can do it.
It's just going to take a lot of hours and a lot of refining, a lot of fixing, a lot of
errors and debugging and coding and stuff like that, which I already did the work of doing.
So, if you want a custom built Cloud project that already has all of this stuff in here that
I already took the time to make with all of these skills and all of these assets, docs,
packaging, presets, workflows, and all this stuff, this is all included in my school
community and you can download all of this right away.
So, you don't have to do any of the debugging or coding or customizing.
It already comes like locked in, pretty dialed, and will be able to edit your videos much,
much better right off the bat.
So, if you want to get all these folders, files, assets for this Cloud video editor project
that I've been working on for the past like month and a half, then you can definitely join
my school community and get the files for yourself.
Not only that, but there's also a full walk-through on how to install it and everything.
And you get the support of me in the community.
I respond to everyone with a full Loom breakdown every single day.
And I host group calls twice a week, once on Tuesday, once on Thursday.
I'm literally about to hop on right now and speak to all the members.
So, if you want to speak to me one-on-one and get my one-on-one help, you can do that in the
community right here.
But other than that, guys, that's going to conclude this video.
I really hope you guys enjoyed it.
I hope you got value out of this one.
And happy editing.
I hope you use AI to help you edit faster and better.
I'll see you in the next one.
Peace.
