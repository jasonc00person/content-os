# I taught Claude how to use Premiere Pro and it’s INSANE.

- **Source:** https://www.youtube.com/watch?v=CK5per-3T5s
- **Uploader:** Soroosh Hedayati
- **Uploaded:** 2026-04-22
- **Duration:** 7:27
- **Method:** YouTube captions (no transcription needed)

## Transcript

What you're watching right now, every cut, transition, and pop-in was done by Claude. Claude opened the Premiere Pro video editor, looked at my raw footage, and edited this video. I'll let you be the judge of how well it did. But, this is just the beginning. I'm building a system that automates every step of YouTube video production, and I'm going to use that system to produce these videos as I build it. Here's the full road map. Here's everything that's automated today, and then everything else is what's coming. And by the way, that fancy animated road map graphic, yeah, Claude made that. So, I know you want to see this in action. Here it is. I've Claude open in a window that's just hovering over the Premiere Pro video editor. I'm going to tell it to edit my A-roll for me. So, spoiler alert, when I film these videos, I am reading off of a teleprompter. I do my script beforehand, put it up, and I read it word for word. And in the moment, if I do a take that I don't like, I will just repeat myself. I will reread it off until I get it right. So, this sequence that we're looking at here is just a raw sequence of me talking in front of the camera, a bunch of bad takes, you know, me flubbing it around, me doing whatever. Interestingly, Claude, through this entire process, can only ever read the transcript. It can't actually watch the video itself. But, it's pretty shocking how many things it can do just based on that alone. So, you'll see that it went and it did all of those cuts for me. Now, it's going and it's removing the silences out of Premiere Pro. Zoom in here so we can see it a little bit better. Pull it back up. So, the next thing that it's going to do is to close up the gap. Sometimes, when you're doing this A-roll editing, you'll have little fragments of gaps in between the individual clips. Um one other fun little thing that you can actually do with this setup is that you can have multiple Clauds working on the same Premiere Pro timeline at the exact same time. So, you can imagine you have one of them that's building animations for it, the other one that's doing transitions, maybe another one that's working on the transcript, whatever. It's deleting off individual clips cuz it noticed that it missed that on its earlier pass. And it's all done. For the non-video editors watching this, to be clear, this would have been about an hour's worth of work that it did on its own in what, a minute? I know people are going to ask, so yes, you can try this yourself right now. It's early access. Set up is manual. Things are going to break. But, if you still want to try it, I put a link in the description. So, how does this actually work? Claude does not know how to click buttons in Premiere to edit videos. But, what it does know is how to use tools. So, let's say that Claude wants to remove all the silences in a video. It's not literally going to go through and select the portions of the videos that have silence and then delete them off. Instead, it performs a tool call called remove silences, which then runs a computer script that removes out all the silences for Claude. Claude doesn't need to know how that script works. It just needs to know that this is a tool that it is allowed to use. And in case you're curious, this is what it looks like when Claude asks to use the remove silences tool. The Claude desktop app sees that and then runs the silence removal script inside of Premiere. Going back to the road map, each one of these icons is an individual tool that Claude will get access to. For example, when Claude thinks that a part of the video would look good having an animated graphic in it, it will call a tool call called create animated graphic, where it describes what kind of graphic it wants to get made, and then a bunch of magic happens inside of the box to create an animated graphic. But, video editor Claude doesn't need to know what's happening inside that box. All it knows is that it asked for an animated graphic, told it what it should look like, and then the magic box spit out an animated graphic for it that video editor Claude can put into the video. Inside of these magic boxes, a lot of cool stuff is happening. And every week, I'm going to build another magic box and make a video about it. Some of these magic boxes I already have built. For example, choosing stock footage is done. I built a Premiere Pro plugin called Buzz Rolls, where editors tell it where they want B-roll, hit go, and it handles the rest. Searches stock video sites, chooses the best match, downloads, and inserts it. As a human, you can download and use Buzz Rolls right now. But, it was built for humans with clickable buttons. I haven't set it up for Claude to use yet, but you can imagine how Buzz Rolls would get turned into a magic box that Claude can use. It calls the find B-roll tool call, tells it where it wants B-roll to cover, and then the magic box, which is Buzz Rolls in this case, takes care of the rest. As a test for Claude, I went and I ordered all of our timeline clips into a completely random order. I scrambled them, and this new instance of Claude has absolutely no idea what the right order should be. And I actually I had to tell it explicitly don't go and read our original script cuz it's smart enough to be like, "Well, the easy thing to do for me to do is just go find the script file and then put everything back in the right order." But, I want it to do it based on its own intelligence of understanding and deducing out what the correct narrative order should be. So, if you were to look at the transcript of this video right now, it makes absolutely no sense. It's completely completely scrambled, and we'll see what it does. So, it's going through, it's, you know, getting all the sections, thinking to itself, you know, trying to do all of the math on that. And it looks like it's already kind of coming up with an answer. So, we'll let it run a little bit, see what it does. Okay, so after a few minutes of Claude deeply thinking to itself to make sure that it's getting this right, it is finally going through and reordering everything. It really wanted to make sure it got it right. It was just over and over again thinking to itself being like, "Oh, wait, no, I didn't catch that one little thing. Let's go back and do this and do that." And then it finally locked it in, and now it's doing it. So, I noticed a couple of problems looking on this. Most of them are bugs in my software, not actually Claude messing up. But, if you watch through the video, it does make sense, and it did work. It did it right. It doesn't exactly match my original script, but if this was your first time watching the video, you wouldn't have questioned it. I wanted to clarify what in the edit was done by Claude versus what was done by me. So, as shown in the demo earlier, the A-roll talking head footage was 99% edited by Claude. There was one duplicate sentence that I went and manually removed myself. Otherwise, the biggest other thing were these animations. These were all done by Claude. The way it works is I just selected the in and the out points, went over Claude, and I literally made a command called make animation for Premiere here, which kicks off a whole workflow. I'll talk about that in next week's video, likely. Um but, I described exactly what I wanted in those animations. And then I often was getting the assets that contributed to the animation. So, for example, these portions were screen recordings of different windows that Claude used. But, the composition itself, all of the animations and the drop shadows, stuff like that, was Claude doing that. Otherwise, the cross dissolves at the end of these guys were Claude. I told it at the end of any animation, the end of the beginning, add a cross dissolve. It did that. And then there was like a pop-in here. In this case, I told it selected the section and then told it put a pop-in here. Um little other things such as doing music and audio balancing was done by me. There's no automation for that stuff yet, but the plan is to continue automating more and more of the process over time. That's it for today. Next week, we teach Claude how to make its own animations on the fly. Subscribe if you want to see that. Otherwise, I'll see you next time.

## Timestamped

`[00:01]` What you're watching right now, every
`[00:01]` cut, transition, and pop-in was done by
`[00:04]` Claude. Claude opened the Premiere Pro
`[00:06]` video editor, looked at my raw footage,
`[00:08]` and edited this video. I'll let you be
`[00:10]` the judge of how well it did. But, this
`[00:12]` is just the beginning. I'm building a
`[00:13]` system that automates every step of
`[00:15]` YouTube video production, and I'm going
`[00:17]` to use that system to produce these
`[00:18]` videos as I build it. Here's the full
`[00:21]` road map. Here's everything that's
`[00:22]` automated today, and then everything
`[00:24]` else is what's coming. And by the way,
`[00:26]` that fancy animated road map graphic,
`[00:28]` yeah, Claude made that. So, I know you
`[00:30]` want to see this in action. Here it is.
`[00:32]` I've Claude open in a window that's just
`[00:34]` hovering over the Premiere Pro video
`[00:36]` editor. I'm going to tell it to edit my
`[00:38]` A-roll for me. So, spoiler alert, when I
`[00:40]` film these videos, I am reading off of a
`[00:42]` teleprompter. I do my script beforehand,
`[00:44]` put it up, and I read it word for word.
`[00:46]` And in the moment, if I do a take that I
`[00:48]` don't like, I will just repeat myself. I
`[00:50]` will reread it off until I get it right.
`[00:53]` So, this sequence that we're looking at
`[00:55]` here is just a raw sequence of me
`[00:57]` talking in front of the camera, a bunch
`[00:58]` of bad takes, you know, me flubbing it
`[01:00]` around, me doing whatever.
`[01:02]` Interestingly, Claude, through this
`[01:03]` entire process, can only ever read the
`[01:06]` transcript. It can't actually watch the
`[01:08]` video itself. But, it's pretty shocking
`[01:10]` how many things it can do just based on
`[01:12]` that alone. So, you'll see that it went
`[01:14]` and it did all of those cuts for me.
`[01:16]` Now, it's going and it's removing the
`[01:18]` silences out of Premiere Pro. Zoom in
`[01:21]` here so we can see it a little bit
`[01:22]` better. Pull it back up. So, the next
`[01:25]` thing that it's going to do is to close
`[01:27]` up the gap. Sometimes, when you're doing
`[01:28]` this A-roll editing, you'll have little
`[01:31]` fragments of gaps in between the
`[01:33]` individual clips. Um one other fun
`[01:36]` little thing that you can actually do
`[01:38]` with this setup is that you can have
`[01:41]` multiple Clauds working on the same
`[01:44]` Premiere Pro timeline at the exact same
`[01:46]` time. So, you can imagine you have one
`[01:47]` of them that's building animations for
`[01:50]` it, the other one that's doing
`[01:51]` transitions, maybe another one that's
`[01:53]` working on the transcript, whatever.
`[01:54]` It's deleting off individual clips cuz
`[01:57]` it noticed that it missed that on its
`[01:59]` earlier pass. And it's all done.
`[02:02]` For the non-video editors watching this,
`[02:04]` to be clear, this would have been about
`[02:06]` an hour's worth of work that it did on
`[02:08]` its own in what, a minute? I know people
`[02:10]` are going to ask, so yes, you can try
`[02:12]` this yourself right now. It's early
`[02:14]` access. Set up is manual. Things are
`[02:16]` going to break. But, if you still want
`[02:18]` to try it, I put a link in the
`[02:19]` description. So, how does this actually
`[02:21]` work? Claude does not know how to click
`[02:23]` buttons in Premiere to edit videos. But,
`[02:25]` what it does know is how to use tools.
`[02:27]` So, let's say that Claude wants to
`[02:28]` remove all the silences in a video. It's
`[02:30]` not literally going to go through and
`[02:32]` select the portions of the videos that
`[02:33]` have silence and then delete them off.
`[02:35]` Instead, it performs a tool call called
`[02:38]` remove silences, which then runs a
`[02:41]` computer script that removes out all the
`[02:43]` silences for Claude. Claude doesn't need
`[02:46]` to know how that script works. It just
`[02:47]` needs to know that this is a tool that
`[02:49]` it is allowed to use. And in case you're
`[02:51]` curious, this is what it looks like when
`[02:53]` Claude asks to use the remove silences
`[02:55]` tool. The Claude desktop app sees that
`[02:58]` and then runs the silence removal script
`[03:00]` inside of Premiere. Going back to the
`[03:02]` road map, each one of these icons is an
`[03:04]` individual tool that Claude will get
`[03:06]` access to. For example, when Claude
`[03:09]` thinks that a part of the video would
`[03:10]` look good having an animated graphic in
`[03:12]` it, it will call a tool call called
`[03:15]` create animated graphic, where it
`[03:17]` describes what kind of graphic it wants
`[03:19]` to get made, and then a bunch of magic
`[03:21]` happens inside of the box to create an
`[03:24]` animated graphic. But, video editor
`[03:26]` Claude doesn't need to know what's
`[03:28]` happening inside that box. All it knows
`[03:31]` is that it asked for an animated
`[03:32]` graphic, told it what it should look
`[03:34]` like, and then the magic box spit out an
`[03:37]` animated graphic for it that video
`[03:38]` editor Claude can put into the video.
`[03:41]` Inside of these magic boxes, a lot of
`[03:43]` cool stuff is happening. And every week,
`[03:45]` I'm going to build another magic box and
`[03:47]` make a video about it. Some of these
`[03:49]` magic boxes I already have built. For
`[03:51]` example, choosing stock footage is done.
`[03:53]` I built a Premiere Pro plugin called
`[03:55]` Buzz Rolls, where editors tell it where
`[03:57]` they want B-roll, hit go, and it handles
`[04:00]` the rest. Searches stock video sites,
`[04:02]` chooses the best match, downloads, and
`[04:04]` inserts it. As a human, you can download
`[04:06]` and use Buzz Rolls right now. But, it
`[04:09]` was built for humans with clickable
`[04:11]` buttons. I haven't set it up for Claude
`[04:13]` to use yet, but you can imagine how Buzz
`[04:15]` Rolls would get turned into a magic box
`[04:17]` that Claude can use. It calls the find
`[04:20]` B-roll tool call, tells it where it
`[04:22]` wants B-roll to cover, and then the
`[04:23]` magic box, which is Buzz Rolls in this
`[04:25]` case, takes care of the rest. As a test
`[04:28]` for Claude, I went and I ordered all of
`[04:30]` our timeline clips into a completely
`[04:32]` random order. I scrambled them, and this
`[04:34]` new instance of Claude has absolutely no
`[04:37]` idea what the right order should be. And
`[04:40]` I actually I had to tell it explicitly
`[04:42]` don't go and read our original script
`[04:44]` cuz it's smart enough to be like, "Well,
`[04:45]` the easy thing to do for me to do is
`[04:46]` just go find the script file and then
`[04:48]` put everything back in the right order."
`[04:50]` But, I want it to do it based on its own
`[04:52]` intelligence of understanding and
`[04:54]` deducing out what the correct narrative
`[04:57]` order should be.
`[04:58]` So, if you were to look at the
`[04:59]` transcript of this video right now, it
`[05:01]` makes absolutely no sense. It's
`[05:03]` completely completely scrambled, and
`[05:05]` we'll see what it does. So, it's going
`[05:06]` through, it's, you know, getting all the
`[05:07]` sections, thinking to itself, you know,
`[05:10]` trying to do all of the math on that.
`[05:12]` And it looks like it's already kind of
`[05:14]` coming up with an answer.
`[05:16]` So, we'll let it run a little bit, see
`[05:18]` what it does.
`[05:26]` Okay, so after a few minutes of Claude
`[05:26]` deeply thinking to itself to make sure
`[05:28]` that it's getting this right, it is
`[05:29]` finally going through and reordering
`[05:31]` everything. It really wanted to make
`[05:33]` sure it got it right. It was just over
`[05:35]` and over again
`[05:37]` thinking to itself being like, "Oh,
`[05:38]` wait, no, I didn't catch that one little
`[05:40]` thing. Let's go back and do this and do
`[05:41]` that." And then it finally locked it in,
`[05:43]` and now it's doing it. So, I noticed a
`[05:46]` couple of problems looking on this. Most
`[05:47]` of them are bugs in my software, not
`[05:49]` actually Claude messing up. But, if you
`[05:51]` watch through the video, it does make
`[05:53]` sense, and it did work. It did it right.
`[05:55]` It doesn't exactly match my original
`[05:56]` script, but if this was your first time
`[05:58]` watching the video, you wouldn't have
`[06:00]` questioned it. I wanted to clarify what
`[06:02]` in the edit was done by Claude versus
`[06:03]` what was done by me. So, as shown in the
`[06:05]` demo earlier, the A-roll talking head
`[06:07]` footage was 99% edited by Claude. There
`[06:10]` was one duplicate sentence that I went
`[06:12]` and manually removed myself. Otherwise,
`[06:14]` the biggest other thing were these
`[06:16]` animations. These were all done by
`[06:18]` Claude. The way it works is I just
`[06:20]` selected the in and the out points, went
`[06:22]` over Claude, and I literally made a
`[06:23]` command called make animation for
`[06:25]` Premiere here, which kicks off a whole
`[06:27]` workflow. I'll talk about that in next
`[06:30]` week's video, likely. Um but, I
`[06:32]` described exactly what I wanted in those
`[06:34]` animations. And then I often was getting
`[06:36]` the assets that contributed to the
`[06:38]` animation. So, for example, these
`[06:40]` portions were screen recordings of
`[06:42]` different windows that Claude used. But,
`[06:44]` the composition itself, all of the
`[06:46]` animations and the drop shadows, stuff
`[06:49]` like that, was Claude doing that.
`[06:51]` Otherwise, the cross dissolves at the
`[06:53]` end of these guys were Claude. I told it
`[06:56]` at the end of any animation, the end of
`[06:57]` the beginning, add a cross dissolve. It
`[06:59]` did that. And then there was like a
`[07:01]` pop-in here. In this case, I told it
`[07:04]` selected the section and then told it
`[07:05]` put a pop-in here.
`[07:07]` Um little other things such as doing
`[07:09]` music and audio balancing was done by
`[07:12]` me. There's no automation for that stuff
`[07:14]` yet, but the plan is to continue
`[07:15]` automating more and more of the process
`[07:18]` over time. That's it for today. Next
`[07:20]` week, we teach Claude how to make its
`[07:21]` own animations on the fly. Subscribe if
`[07:23]` you want to see that. Otherwise, I'll
`[07:25]` see you next time.
