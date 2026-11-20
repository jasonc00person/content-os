# My Claude Code Edits FULL Videos in One Shot (Here's How)

- **Source:** https://www.youtube.com/watch?v=mlhhZSHIS-w
- **Uploader:** Brad Bonanno | AI Automation
- **Uploaded:** 2026-08-06
- **Duration:** 17:00
- **Method:** YouTube captions (no transcription needed)

## Transcript

What I do is drop my raw footage into this folder and Claude edits the entire video for me in one shot. It handles motion graphics like this, generates perfect AI B-roll completely automatically, bakes in captions like these ones, and the music you're hearing right now, all of it. This pipeline has edited every single video on this channel over the past month, but most people trying this are spending hours going back and forth with Claude because they're missing the one skill that turns AI editing into a completely autonomous video production engine. In this video, I'll show you how to build the entire thing, no gatekeeping, starting with how AI editing actually works. AI editing is actually pretty simple because it's essentially the same thing that a human editor would do, just broken down into stages that Claude can actually run. The problem is that Claude code can't just log in to Premiere Pro and start editing for you. So, we need to design an AI editing pipeline around a tool set and the capabilities of what Claude can actually do. And the best part of the one that I've designed is that the whole thing runs on about five tools, and almost all of them are free. Stage one is transcription, and for that we'll use Whisper X. It's a small AI model that runs locally on your machine and transcribes your raw footage word-by-word with a timestamp on every single word. And that matters because Claude can't actually hear the audio for the clips, so it has no idea where a cut should land unless it knows the sub-second timing of what was actually said. It also can't physically make that cut without writing complicated custom code. So, we need a package for that, FFmpeg. Claude can now read the transcript and decide what goes, so it takes out the silences, the bad takes, and the filler. And FFmpeg is what physically makes those cuts for it. It trims the clips, joins them back together, and cleans up your audio. It's free and it's open source, and it turns 25 minutes of raw footage into about 12 minutes of tight video. Once we've taken out all of our mistakes and silences, we've got our rough cut, but without some extra footage, that's going to make a pretty boring video just staring at me for 20 minutes. So next the B-roll comes in. Claude will look at all the screen recordings that I've taken for the video and merge them in where the script calls for it. And when I don't have any footage for a line, I use Higgsfield to automatically generate the B-roll that fits perfectly for that scene. Higgsfield lets Claude access all the best image and video models in one connection using its MCP. So Claude reads the context of the script and then can go and generate footage that fits exactly what I'm saying. B-roll is great but the real power of this editing pipeline is in generating those motion graphics that you saw earlier. And that all happens with HyperFrames which is a 100% free open source graphics engine from the team at Haystack. And it builds every graphic as code so Claude has literally no limits in how many of these it can create for your video. It even handles the scene setup and changes that you're seeing right now. HyperFrames is very much the backbone of this pipeline and what takes it from trimming clips to actually generating videos. Once we've got the graphics in, we layer in the special effects. So that's the background music and the sound effects that you've heard throughout the video. And again that's FFmpeg doing all of the work here. So you're probably wondering how much this all costs because I've been running my edits over the last couple of weeks and each video has averaged out to about $90 worth of tokens. But the thing is I never actually paid that because it all came out of my Claude Code Max plan that I'm already on. The only real cash cost is the AI B-roll which runs a few per segment on Higgsfield. Now compare that to paying an editor which might cost you anywhere between 150 and $3,000 per video. But the thing is these edits come back in 3 hours which is way faster than any editor I've ever worked with. You could 100% try and run this on a cheaper model and optimize it even further than I have and I'm really hoping to seeing what you guys have done there so leave a comment if you've got ideas how to make this cheaper. So that's the pipeline and most AI editing workflows actually stop right here, which is exactly where they fall apart, because here's what actually happens. The first draft comes back, and the captions might be covering your face, the graphics aren't using the space properly. So, you type, "Move that down, make the graphic bigger." And suddenly, you've spent about 2 hours as the director for what is essentially a blind video editor, and you don't save any time at all. So, I plugged that gap, and it's the reason why this whole workflow runs on its own for me now. I gave Claude the ability to actually watch the video it's editing, because see, Claude code can't see video. It can only read the transcript. That's why it always nails the rough cut every time, because cutting raw footage down just needs a good transcript. But the graphics overlays always come back with little issues, because Claude never actually sees the finished result. So, a few months back, I built a skill called watch, and it gives Claude eyes. It pulls out the video's frames one by one, so Claude can see exactly what's going on on screen at every single moment, and it is a massive upgrade to this editing workflow, because once Claude can see its own work, it can edit the way a real editor does. Because think about it for a second. A real editor is working on a timeline, they make a change, they watch it back, they spot what looks off, and then they fix it. They keep doing that until the video looks right. No editor can edit a video in one go with its eyes closed. So, why are we asking Claude to? This cycle is called an agent loop, and it's made up of two ingredients. First is a goal, which is finish the video, and a way for Claude to actually go and check what it's working on. So, that's the watch skill. So, here's exactly what that agent loop looks like in my pipeline. Once the render is finished, I have sub agents use the watch skill to review it like a picky editor. They check for visual glitches, spacing, alignment, and just the general feel of the clip. Then they hand their report back to Claude as a list of fixes. Claude then makes those fixes, renders again, and reviews again. And the whole process keeps going around in that loop until the video passes. So, by the time I sit down for my final review, it's already been through half a dozen reviews using these sub-agents. And that validation loop is the key here because an agent that can't check its own work is really just guessing about the quality of the final result. It's also exactly why I don't use a video understanding model like Gemini because Claude can control exactly where it looks in these clips. So, we can go and inspect the seams between the graphics and those seams specifically. Now, validation is the biggest part of getting these edits done in one shot, but it's not the only job that the watch skill does. It's also how I steal any editing style and how I can pick my B-roll completely automatically, but we'll go through both of those when I run the full pipeline in just a little bit. So, let's get everything set up so you can start running this for yourself today. The first thing that you need to do is go to your desktop or anywhere and create a folder called video editor. Then, open that folder inside of your Claude code. I'm actually running Claude code inside of my Founder OS, which is one folder and workspace that I can run my entire business out of. It has my sales, my delivery, my content, everything. If you want to build a Founder OS just like mine, so you can run your business out of one folder, I'm hosting a live build shop this month and the link for that in is in the description below. But, if you don't want to do that, you don't need the Founder OS or anything fancy to get this to work. You can just open up that folder inside of the desktop app as well. Then, once we've got that set up, we want to start installing everything we need. So, we go and grab the watch skill from the guide a link in the description below, as well as the link to the Hyperframes GitHub, and ask Claude to just install both of those inside of that project. Then, we'll connect Higgsfield as an MCP for the B-roll. So, you'll need to head to B-roll. So, you'll need to head to higgsfield.com/mcp, higgsfield.com/mcp, copy the link, and then ask Claude to install that MCP for you. If you want to use it on Claude chat as well, you can do that. Just go to the connectors menu, then add it in there. Then, we'll grab FFmpeg and WhisperX. These are both doing the heavy lifting for cutting and transcription. Once again, grab the GitHub URLs for both and ask Claude to install it for you. If you want one prompt that will set up absolutely everything for you, it's linked in the description below in my video editing playbook. So, that's the stack, which means that we can point it at some actual footage now. So, what I'm going to do is try and one-shot the intro for the video that we've just recorded. So, let's go ahead and do that. But, quickly, I want to show you what I do in order to prepare the editor to actually get a good result on the first try. So, I have a folder on my computer with all of the footage that I have already recorded. So, I've got my main cam footage, which has all the clips, and then I have the script. So, we're only doing the intro, so I've only done the intro script so far. But, essentially, this is what I said as part of the intro. I actually create this in a Word doc or Google doc because I can then come in and add comments on what I actually want to do. So, I tell it what intro music I want to use. I tell it to start out zoomed in and then rapidly zoom out. I tell it what type of graphics I want to create, and if there's reference images that I want to incorporate into those graphics, then I go and just grab a link to those. This is super, super important because if you don't do the pre-work for the edit, and you don't actually think about what you want the end result to look like, you're going to end up with a really sort of AI slop looking video that doesn't really fit with what you're trying to create. So, now that I have that one folder on my computer, I can just go to Claude now and just say, "Just edit clip one. The intro is here." And then I just give it the the file address of where that folder is located. So, it's just in my movies folder, or you could just tell it. You don't need to do it that way. And then a little bit of a prompt about what I want. So, I always make sure to include like, "Hey, look, there is a Word doc there with the script. Go and check the comments because those comments have all the information that you need." And then I also just include like a bit of a reminder, "Hey, use the watch skill for that self-improvement loop that we talked about earlier." And then we'll hit go. And now Claude is going to start on the rough cut and once that's finished we'll come back and I'll show you what it looks like. So Claude just started working here and it's created a project called Claude code and it's my videos. You can see it has a few folders. We've got assets which it's gone and found a bunch of assets that I linked to it. Uh, some of the screenshots from the YouTube videos that this harness has edited as well as it's gone and found that uh, intro music that I uh, wanted and then it's scaffolded some of the other folders that I'll need later. What it's doing now is it's running Whisper X that local AI model to go and transcribe that clip so it knows exactly where each uh, word lands when I'm saying it so it can start to do that rough cut. And the transcription has just landed. You can see how it looks here. We've got literally sub-second timings for every single word that I say in this intro clip. And this goes on for a couple hundred lines. So So this is what Claude will use to go and find that rough cut and find any silences or gaps. So it looks like the rough cut has just landed so I'll open that up now. &gt;&gt; All I do is drop my raw footage into this folder and Claude edits the entire video for me in one shot. It handles motion graphics like this, generates perfect AI B-roll completely automatically, bakes in captions like these ones, and the music you're hearing right now. All of it. This pipeline has edited every single video on this channel over the past month but most people trying this are spending hours going back and forth with Claude because they're missing the one skill that turns AI editing into a completely autonomous video production engine. In this video I'll show you how to build the entire thing, no gatekeeping. Starting with how AI editing actually works. &gt;&gt; So it's just absolutely nailed that rough cut and that's pretty expected cuz it's just a transcript that it needs to go and take out those uh, silences and gaps. It's cut about I think it was about a minute 30 of footage down to 39 seconds. So now that it's got the rough cut the next thing it's going to to go do is read all my comments and start to create that graphics plan. And that graphics plan is essentially based on all of the comments that we just gave it in that word doc. So, it's going to go read all those and start generating some of that AI B-roll. And then from there it'll merge everything together. So, we'll come back once that is done. You can see that it's started rendering here in Higgs Field. Now, this is using C-Dance 2 at 1080p, so it's probably going to take a few minutes. But while this is happening, Claude is actually still working. It's gone through and started to do graphics plan and then it'll incorporate that footage once the footage is finished rendering. So, it's just finished generating that AI B-roll and it looks pretty good. So, that is now going to be downloaded back into the project and then automatically merged in using hyperframes. So, Claude has just completed the first version of the render, which means it hasn't gone through any of the revision loops yet. This is its first attempt and here it is. What I do is drop my raw footage into this folder and Claude edits the entire video for me in one shot. It handles motion graphics like this, generates perfect AI B-roll completely automatically, bakes in captions like these ones, and the music you're hearing right now, all of it. This pipeline has edited every single video on this channel over the past month, but most people trying this are spending hours going back and forth with Claude because they're missing the one skill that turns AI editing into a completely autonomous video production engine. In this video, I'll show you how to build the entire thing, no gatekeeping. Starting with how AI editing actually works. &gt;&gt; I mean, it's interesting. That's an interesting take, but we'll we'll have to run with it. I think what I'll actually do, like just to remind you, like this is a brand new instance of this editor that I've just set up to do the demos. So, I probably need to give it some more instructions about how it actually renders, uh, Claude. Um, but I might fix that up in the intro that you see at the beginning of this video, so don't hate me. Now, I can see Claude is going through the process of watching that video using the skill and going through frame by frame to find any bugs or any issues. It's going to go fix it all now, and then re-render, and then we'll see the final result. Claude's just finished and it took about 40 minutes to do this intro, but it's important to remember that Claude did this completely autonomously. So, the only thing I told it was to use the second copy of some B-roll that it ended up regenerating asked for my input on. It's gone through and done two passes of technical Q&amp;A and composition fidelity, and here is the final intro. All I do is drop my raw footage into this folder and Claude edits the entire video for me in one shot. It handles motion graphics like this, generates perfect AI B-roll completely automatically, bakes in captions like these ones, and the [music] music you're hearing right now, all of it. This pipeline has edited every single video on this channel [music] over the past month, but most people trying this are spending hours going back and forth with Claude because they're missing the one skill that turns AI editing into a completely autonomous video production engine. [music] In this video, I'll show you how to build the entire thing, no gatekeeping. Starting with how AI editing actually works. [music] Pretty good. There are a few little changes here that I'd probably make, but essentially, I think that's almost perfect. Now, the next step here is just to do the rest of the video. I've only done the intro, but that's exactly how the whole pipeline works. So, the watch skill gives you the loop, but there are four other things that take these edits from pretty good to genuinely one shot. Number one is the taste skill. Every graphic Hyperframes creates is basically front-end design because it's building these graphics in HTML, which means that anything that makes Claude better at front-end design makes your motion graphics better, too. And that's exactly what the taste skill does. Left to its own devices, Claude builds pretty much AI slop for graphics. The taste skill gives it rules that a designer would actually work to, so it all looks a little bit nicer. I like it because it doesn't just give Claude a preset to follow, it gives it a design approach to make better graphics in any style. Number two is generated assets. I told you Higgsfield was being used for the B-roll, but it also earns a spot a second time here because Claude can use it mid-edit to generate an image or a short clip and drop it straight into part of a graphic. And that changes what a graphic can be because up until this point your graphics were just text, charts, and screen recordings, essentially limited by what HTML could do. But sometimes you want icons or graphics that Hyperframes can't build with code. So you can get Higgsfield to generate them and then have Hyperframes incorporate those new images into the graphic. Number three is making your style file absorb every correction because right now every note you give Claude in that final review is a note you're going to give it again next week. The rule I've got in mind is that any correction coming out of the review gets written back into that style file before the edit is closed out. This is really, really important for getting this workflow fully automated over time because that way Claude is always learning from your inputs. And number four is the one that I think matters absolutely most to getting this done in one shot and it's not a tool, it's the pre-work that you put in before you even edit it. One of the biggest learnings I've had from using this over the past month is that the more time you spend planning the closer you will get these edits in one shot because the agent isn't guessing what you want anymore, it's just reading the comments from your script. 10 minutes of comments here will literally save you hours of back and forth and it's the single biggest difference between an edit that comes back usable and that and one that comes back needing hours of back and forth with Claude. So that's the whole system. I've actually packaged the entire pipeline into a guide with every prompt from this video and you can grab it completely free at the link below. And if you want to build the AI OS that runs this, that's what I'm teaching live at the Founder OS Build Shop on August 26th. The link is down there, too.

## Timestamped

`[00:01]` What I do is drop my raw footage into
`[00:01]` this folder and Claude edits the entire
`[00:04]` video for me in one shot. It handles
`[00:06]` motion graphics like this, generates
`[00:09]` perfect AI B-roll completely
`[00:11]` automatically, bakes in captions like
`[00:13]` these ones, and the music you're hearing
`[00:15]` right now, all of it. This pipeline has
`[00:18]` edited every single video on this
`[00:20]` channel over the past month, but most
`[00:22]` people trying this are spending hours
`[00:24]` going back and forth with Claude because
`[00:26]` they're missing the one skill that turns
`[00:28]` AI editing into a completely autonomous
`[00:30]` video production engine. In this video,
`[00:33]` I'll show you how to build the entire
`[00:34]` thing, no gatekeeping, starting with how
`[00:37]` AI editing actually works. AI editing is
`[00:40]` actually pretty simple because it's
`[00:41]` essentially the same thing that a human
`[00:43]` editor would do, just broken down into
`[00:45]` stages that Claude can actually run. The
`[00:47]` problem is that Claude code can't just
`[00:49]` log in to Premiere Pro and start editing
`[00:51]` for you. So, we need to design an AI
`[00:53]` editing pipeline around a tool set and
`[00:56]` the capabilities of what Claude can
`[00:58]` actually do. And the best part of the
`[01:00]` one that I've designed is that the whole
`[01:01]` thing runs on about five tools, and
`[01:03]` almost all of them are free. Stage one
`[01:06]` is transcription, and for that we'll use
`[01:08]` Whisper X. It's a small AI model that
`[01:10]` runs locally on your machine and
`[01:12]` transcribes your raw footage
`[01:13]` word-by-word with a timestamp on every
`[01:16]` single word. And that matters because
`[01:18]` Claude can't actually hear the audio for
`[01:20]` the clips, so it has no idea where a cut
`[01:22]` should land unless it knows the
`[01:24]` sub-second timing of what was actually
`[01:26]` said. It also can't physically make that
`[01:28]` cut without writing complicated custom
`[01:30]` code. So, we need a package for that,
`[01:32]` FFmpeg. Claude can now read the
`[01:34]` transcript and decide what goes, so it
`[01:36]` takes out the silences, the bad takes,
`[01:38]` and the filler. And FFmpeg is what
`[01:40]` physically makes those cuts for it. It
`[01:42]` trims the clips, joins them back
`[01:44]` together, and cleans up your audio. It's
`[01:46]` free and it's open source, and it turns
`[01:48]` 25 minutes of raw footage into about 12
`[01:50]` minutes of tight video. Once we've taken
`[01:52]` out all of our mistakes and silences,
`[01:54]` we've got our rough cut, but without
`[01:56]` some extra footage, that's going to make
`[01:57]` a pretty boring video just staring at me
`[02:00]` for 20 minutes. So next the B-roll comes
`[02:02]` in. Claude will look at all the screen
`[02:04]` recordings that I've taken for the video
`[02:05]` and merge them in where the script calls
`[02:07]` for it. And when I don't have any
`[02:08]` footage for a line, I use Higgsfield to
`[02:10]` automatically generate the B-roll that
`[02:12]` fits perfectly for that scene.
`[02:14]` Higgsfield lets Claude access all the
`[02:16]` best image and video models in one
`[02:18]` connection using its MCP. So Claude
`[02:20]` reads the context of the script and then
`[02:22]` can go and generate footage that fits
`[02:24]` exactly what I'm saying. B-roll is great
`[02:26]` but the real power of this editing
`[02:28]` pipeline is in generating those motion
`[02:30]` graphics that you saw earlier. And that
`[02:32]` all happens with HyperFrames which is a
`[02:33]` 100% free open source graphics engine
`[02:36]` from the team at Haystack. And it builds
`[02:38]` every graphic as code so Claude has
`[02:41]` literally no limits in how many of these
`[02:43]` it can create for your video. It even
`[02:45]` handles the scene setup and changes that
`[02:48]` you're seeing right now. HyperFrames is
`[02:50]` very much the backbone of this pipeline
`[02:53]` and what takes it from trimming clips to
`[02:55]` actually generating videos. Once we've
`[02:57]` got the graphics in, we layer in the
`[02:58]` special effects. So that's the
`[03:00]` background music and the sound effects
`[03:01]` that you've heard throughout the video.
`[03:03]` And again that's FFmpeg doing all of the
`[03:05]` work here. So you're probably wondering
`[03:07]` how much this all costs because I've
`[03:09]` been running my edits over the last
`[03:11]` couple of weeks and each video has
`[03:12]` averaged out to about $90 worth of
`[03:15]` tokens. But the thing is I never
`[03:17]` actually paid that because it all came
`[03:19]` out of my Claude Code Max plan that I'm
`[03:21]` already on. The only real cash cost is
`[03:24]` the AI B-roll which runs a few per
`[03:26]` segment on Higgsfield. Now compare that
`[03:28]` to paying an editor which might cost you
`[03:30]` anywhere between 150 and $3,000 per
`[03:33]` video. But the thing is these edits come
`[03:35]` back in 3 hours which is way faster than
`[03:38]` any editor I've ever worked with. You
`[03:40]` could 100% try and run this on a cheaper
`[03:42]` model and optimize it even further than
`[03:44]` I have and I'm really hoping to seeing
`[03:47]` what you guys have done there so leave a
`[03:48]` comment if you've got ideas how to make
`[03:50]` this cheaper. So that's the pipeline and
`[03:52]` most AI editing workflows actually stop
`[03:54]` right here, which is exactly where they
`[03:56]` fall apart, because here's what actually
`[03:58]` happens. The first draft comes back, and
`[04:00]` the captions might be covering your
`[04:02]` face, the graphics aren't using the
`[04:03]` space properly. So, you type, "Move that
`[04:06]` down, make the graphic bigger." And
`[04:07]` suddenly, you've spent about 2 hours as
`[04:09]` the director for what is essentially a
`[04:11]` blind video editor, and you don't save
`[04:14]` any time at all. So, I plugged that gap,
`[04:16]` and it's the reason why this whole
`[04:18]` workflow runs on its own for me now. I
`[04:21]` gave Claude the ability to actually
`[04:22]` watch the video it's editing, because
`[04:24]` see, Claude code can't see video. It can
`[04:26]` only read the transcript. That's why it
`[04:28]` always nails the rough cut every time,
`[04:30]` because cutting raw footage down just
`[04:33]` needs a good transcript. But the
`[04:34]` graphics overlays always come back with
`[04:37]` little issues, because Claude never
`[04:38]` actually sees the finished result. So, a
`[04:40]` few months back, I built a skill called
`[04:42]` watch, and it gives Claude eyes. It
`[04:45]` pulls out the video's frames one by one,
`[04:47]` so Claude can see exactly what's going
`[04:49]` on on screen at every single moment, and
`[04:52]` it is a massive upgrade to this editing
`[04:54]` workflow, because once Claude can see
`[04:56]` its own work, it can edit the way a real
`[04:59]` editor does. Because think about it for
`[05:00]` a second. A real editor is working on a
`[05:02]` timeline, they make a change, they watch
`[05:04]` it back, they spot what looks off, and
`[05:06]` then they fix it. They keep doing that
`[05:08]` until the video looks right. No editor
`[05:11]` can edit a video in one go with its eyes
`[05:13]` closed. So, why are we asking Claude to?
`[05:15]` This cycle is called an agent loop, and
`[05:17]` it's made up of two ingredients. First
`[05:20]` is a goal, which is finish the video,
`[05:22]` and a way for Claude to actually go and
`[05:23]` check what it's working on. So, that's
`[05:25]` the watch skill. So, here's exactly what
`[05:27]` that agent loop looks like in my
`[05:29]` pipeline. Once the render is finished, I
`[05:31]` have sub agents use the watch skill to
`[05:34]` review it like a picky editor. They
`[05:35]` check for visual glitches, spacing,
`[05:37]` alignment, and just the general feel of
`[05:40]` the clip. Then they hand their report
`[05:42]` back to Claude as a list of fixes.
`[05:44]` Claude then makes those fixes, renders
`[05:46]` again, and reviews again. And the whole
`[05:48]` process keeps going around in that loop
`[05:50]` until the video passes. So, by the time
`[05:52]` I sit down for my final review, it's
`[05:54]` already been through half a dozen
`[05:56]` reviews using these sub-agents. And that
`[05:58]` validation loop is the key here because
`[06:00]` an agent that can't check its own work
`[06:02]` is really just guessing about the
`[06:03]` quality of the final result. It's also
`[06:05]` exactly why I don't use a video
`[06:07]` understanding model like Gemini because
`[06:09]` Claude can control exactly where it
`[06:11]` looks in these clips. So, we can go and
`[06:13]` inspect the seams between the graphics
`[06:15]` and those seams specifically. Now,
`[06:17]` validation is the biggest part of
`[06:19]` getting these edits done in one shot,
`[06:22]` but it's not the only job that the watch
`[06:23]` skill does. It's also how I steal any
`[06:26]` editing style and how I can pick my
`[06:28]` B-roll completely automatically, but
`[06:30]` we'll go through both of those when I
`[06:32]` run the full pipeline in just a little
`[06:33]` bit. So, let's get everything set up so
`[06:35]` you can start running this for yourself
`[06:37]` today. The first thing that you need to
`[06:39]` do is go to your desktop or anywhere and
`[06:40]` create a folder called video editor.
`[06:43]` Then, open that folder inside of your
`[06:45]` Claude code. I'm actually running Claude
`[06:46]` code inside of my Founder OS, which is
`[06:49]` one folder and workspace that I can run
`[06:51]` my entire business out of. It has my
`[06:53]` sales, my delivery, my content,
`[06:55]` everything. If you want to build a
`[06:56]` Founder OS just like mine, so you can
`[06:58]` run your business out of one folder, I'm
`[07:00]` hosting a live build shop this month and
`[07:02]` the link for that in is in the
`[07:03]` description below. But, if you don't
`[07:05]` want to do that, you don't need the
`[07:06]` Founder OS or anything fancy to get this
`[07:08]` to work. You can just open up that
`[07:09]` folder inside of the desktop app as
`[07:12]` well. Then, once we've got that set up,
`[07:13]` we want to start installing everything
`[07:15]` we need. So, we go and grab the watch
`[07:17]` skill from the guide a link in the
`[07:18]` description below, as well as the link
`[07:20]` to the Hyperframes GitHub, and ask
`[07:22]` Claude to just install both of those
`[07:24]` inside of that project. Then, we'll
`[07:26]` connect Higgsfield as an MCP for the
`[07:28]` B-roll. So, you'll need to head to
`[07:29]` B-roll. So, you'll need to head to higgsfield.com/mcp,
`[07:32]` higgsfield.com/mcp,
`[07:32]` copy the link, and then ask Claude to
`[07:33]` install that MCP for you. If you want to
`[07:36]` use it on Claude chat as well, you can
`[07:37]` do that. Just go to the connectors menu,
`[07:39]` then add it in there. Then, we'll grab
`[07:41]` FFmpeg and WhisperX. These are both
`[07:43]` doing the heavy lifting for cutting and
`[07:45]` transcription. Once again, grab the
`[07:47]` GitHub URLs for both and ask Claude to
`[07:49]` install it for you. If you want one
`[07:51]` prompt that will set up absolutely
`[07:53]` everything for you, it's linked in the
`[07:55]` description below in my video editing
`[07:57]` playbook. So, that's the stack, which
`[07:58]` means that we can point it at some
`[08:00]` actual footage now. So, what I'm going
`[08:01]` to do is try and one-shot the intro for
`[08:03]` the video that we've just recorded. So,
`[08:05]` let's go ahead and do that. But,
`[08:07]` quickly, I want to show you what I do in
`[08:10]` order to prepare the editor to actually
`[08:12]` get a good result on the first try. So,
`[08:15]` I have a folder on my computer with all
`[08:16]` of the footage that I have already
`[08:18]` recorded. So, I've got my main cam
`[08:19]` footage, which has all the clips, and
`[08:21]` then I have the script. So, we're only
`[08:24]` doing the intro, so I've only done the
`[08:25]` intro script so far. But, essentially,
`[08:27]` this is what I said as part of the
`[08:28]` intro. I actually create this in a Word
`[08:30]` doc or Google doc because I can then
`[08:32]` come in and add comments on what I
`[08:35]` actually want to do. So, I tell it what
`[08:38]` intro music I want to use. I tell it to
`[08:39]` start out zoomed in and then rapidly
`[08:42]` zoom out. I tell it what type of
`[08:44]` graphics I want to create, and if
`[08:45]` there's reference images that I want to
`[08:47]` incorporate into those graphics, then I
`[08:48]` go and just grab a link to those. This
`[08:50]` is super, super important because if you
`[08:53]` don't do the pre-work for the edit, and
`[08:56]` you don't actually think about what you
`[08:57]` want the end result to look like, you're
`[08:59]` going to end up with a really sort of AI
`[09:01]` slop looking video that doesn't really
`[09:04]` fit with what you're trying to create.
`[09:05]` So, now that I have that one folder on
`[09:07]` my computer, I can just go to Claude now
`[09:10]` and just say, "Just edit clip one. The
`[09:12]` intro is here." And then I just give it
`[09:14]` the the file address of where that
`[09:16]` folder is located. So, it's just in my
`[09:17]` movies folder, or you could just tell
`[09:18]` it. You don't need to do it that way.
`[09:21]` And then a little bit of a prompt about
`[09:22]` what I want. So, I always make sure to
`[09:23]` include like, "Hey, look, there is a
`[09:25]` Word doc there with the script. Go and
`[09:27]` check the comments because those
`[09:28]` comments have all the information that
`[09:29]` you need." And then I also just include
`[09:31]` like a bit of a reminder, "Hey, use the
`[09:33]` watch skill for that self-improvement
`[09:35]` loop that we talked about earlier."
`[09:37]` And then we'll hit go. And now Claude is
`[09:39]` going to start on the rough cut and once
`[09:41]` that's finished we'll come back and I'll
`[09:43]` show you what it looks like. So Claude
`[09:44]` just started working here and it's
`[09:46]` created a project called Claude code and
`[09:48]` it's my videos. You can see it has a few
`[09:50]` folders. We've got assets which it's
`[09:51]` gone and found a bunch of assets that I
`[09:53]` linked to it. Uh, some of the
`[09:55]` screenshots from the YouTube videos that
`[09:57]` this harness has edited as well as it's
`[09:59]` gone and found that uh, intro music that
`[10:01]` I uh, wanted and then it's scaffolded
`[10:04]` some of the other folders that I'll need
`[10:05]` later. What it's doing now is it's
`[10:06]` running Whisper X that local AI model to
`[10:09]` go and transcribe that clip so it knows
`[10:11]` exactly where each uh, word lands when
`[10:14]` I'm saying it so it can start to do that
`[10:15]` rough cut. And the transcription has
`[10:17]` just landed. You can see how it looks
`[10:18]` here. We've got literally sub-second
`[10:20]` timings for every single word that I say
`[10:23]` in this intro clip. And this goes on for
`[10:26]` a couple hundred lines. So So this is
`[10:28]` what Claude will use to go and find that
`[10:29]` rough cut and find any silences or gaps.
`[10:32]` So it looks like the rough cut has just
`[10:33]` landed so I'll open that up now.
`[10:35]` &gt;&gt; All I do is drop my raw footage into
`[10:37]` this folder and Claude edits the entire
`[10:39]` video for me in one shot. It handles
`[10:42]` motion graphics like this, generates
`[10:44]` perfect AI B-roll completely
`[10:46]` automatically, bakes in captions like
`[10:49]` these ones, and the music you're hearing
`[10:51]` right now. All of it. This pipeline has
`[10:53]` edited every single video on this
`[10:55]` channel over the past month but most
`[10:57]` people trying this are spending hours
`[10:59]` going back and forth with Claude because
`[11:01]` they're missing the one skill that turns
`[11:03]` AI editing into a completely autonomous
`[11:06]` video production engine. In this video
`[11:08]` I'll show you how to build the entire
`[11:10]` thing, no gatekeeping. Starting with how
`[11:12]` AI editing actually works.
`[11:14]` &gt;&gt; So it's just absolutely nailed that
`[11:16]` rough cut and that's pretty expected cuz
`[11:18]` it's just a transcript that it needs to
`[11:21]` go and take out those uh,
`[11:22]` silences and gaps. It's cut about I
`[11:24]` think it was about a minute 30 of
`[11:26]` footage down to 39 seconds. So
`[11:28]` now that it's got the rough cut the next
`[11:30]` thing it's going to to go do is read all
`[11:31]` my comments and start to create that
`[11:33]` graphics plan. And that graphics plan is
`[11:35]` essentially based on all of the comments
`[11:37]` that we just gave it in that word doc.
`[11:39]` So, it's going to go read all those and
`[11:41]` start generating some of that AI B-roll.
`[11:44]` And then from there it'll merge
`[11:45]` everything together. So, we'll come back
`[11:46]` once that is done. You can see that it's
`[11:48]` started rendering here in Higgs Field.
`[11:50]` Now, this is using C-Dance 2 at 1080p,
`[11:53]` so it's probably going to take a few
`[11:54]` minutes. But while this is happening,
`[11:55]` Claude is actually still working. It's
`[11:58]` gone through and started to do graphics
`[12:00]` plan and then it'll incorporate that
`[12:02]` footage once the footage is finished
`[12:03]` rendering. So, it's just finished
`[12:04]` generating that AI B-roll and it looks
`[12:07]` pretty good. So, that is now going to be
`[12:08]` downloaded back into the project and
`[12:11]` then automatically merged in using
`[12:13]` hyperframes. So, Claude has just
`[12:14]` completed the first version of the
`[12:15]` render, which means it hasn't gone
`[12:16]` through any of the revision loops yet.
`[12:18]` This is its first attempt and here it
`[12:20]` is. What I do is drop my raw footage
`[12:21]` into this folder and Claude edits the
`[12:23]` entire video for me in one shot. It
`[12:26]` handles motion graphics like this,
`[12:28]` generates perfect AI B-roll completely
`[12:31]` automatically, bakes in captions like
`[12:33]` these ones, and the music you're hearing
`[12:36]` right now, all of it. This pipeline has
`[12:38]` edited every single video on this
`[12:40]` channel over the past month, but most
`[12:42]` people trying this are spending hours
`[12:44]` going back and forth with Claude because
`[12:46]` they're missing the one skill that turns
`[12:48]` AI editing into a completely autonomous
`[12:51]` video production engine. In this video,
`[12:53]` I'll show you how to build the entire
`[12:55]` thing, no gatekeeping. Starting with how
`[12:57]` AI editing actually works.
`[12:59]` &gt;&gt; I mean, it's interesting. That's an
`[13:00]` interesting take, but we'll we'll have
`[13:02]` to run with it. I think what I'll
`[13:03]` actually do, like just to remind you,
`[13:05]` like this is a brand new instance of
`[13:08]` this editor that I've just set up to do
`[13:09]` the demos. So, I probably need to give
`[13:10]` it some more instructions about how it
`[13:12]` actually renders, uh, Claude.
`[13:15]` Um, but I might fix that up in the intro
`[13:16]` that you see at the beginning of this
`[13:17]` video, so don't hate me. Now, I can see
`[13:19]` Claude is going through the process of
`[13:21]` watching that video using the skill and
`[13:23]` going through frame by frame to find any
`[13:25]` bugs or any issues. It's going to go fix
`[13:26]` it all now, and then re-render, and then
`[13:28]` we'll see the final result. Claude's
`[13:30]` just finished and it took about 40
`[13:31]` minutes to do this intro, but it's
`[13:32]` important to remember that Claude did
`[13:33]` this completely autonomously. So, the
`[13:35]` only thing I told it was to use the
`[13:37]` second copy of some B-roll that it ended
`[13:39]` up regenerating asked for my input on.
`[13:41]` It's gone through and done two passes of
`[13:43]` technical Q&amp;A and composition fidelity,
`[13:45]` and here is the final intro. All I do is
`[13:47]` drop my raw footage into this folder and
`[13:49]` Claude edits the entire video for me in
`[13:52]` one shot. It handles motion graphics
`[13:54]` like this, generates perfect AI B-roll
`[13:57]` completely automatically, bakes in
`[13:59]` captions like these ones, and the
`[14:01]` [music] music you're hearing right now,
`[14:03]` all of it. This pipeline has edited
`[14:05]` every single video on this channel
`[14:07]` [music] over the past month, but most
`[14:09]` people trying this are spending hours
`[14:11]` going back and forth with Claude because
`[14:13]` they're missing the one skill that turns
`[14:15]` AI editing into a completely autonomous
`[14:17]` video production engine. [music]
`[14:19]` In this video, I'll show you how to
`[14:20]` build the entire thing, no gatekeeping.
`[14:23]` Starting with how AI editing actually
`[14:25]` works. [music] Pretty good. There are a
`[14:27]` few little changes here that I'd
`[14:28]` probably make, but essentially, I think
`[14:30]` that's almost perfect. Now, the next
`[14:31]` step here is just to do the rest of the
`[14:32]` video. I've only done the intro, but
`[14:34]` that's exactly how the whole pipeline
`[14:35]` works. So, the watch skill gives you the
`[14:37]` loop, but there are four other things
`[14:39]` that take these edits from pretty good
`[14:40]` to genuinely one shot. Number one is the
`[14:43]` taste skill. Every graphic Hyperframes
`[14:45]` creates is basically front-end design
`[14:47]` because it's building these graphics in
`[14:49]` HTML, which means that anything that
`[14:51]` makes Claude better at front-end design
`[14:53]` makes your motion graphics better, too.
`[14:55]` And that's exactly what the taste skill
`[14:57]` does. Left to its own devices, Claude
`[14:59]` builds pretty much AI slop for graphics.
`[15:01]` The taste skill gives it rules that a
`[15:03]` designer would actually work to, so it
`[15:05]` all looks a little bit nicer. I like it
`[15:06]` because it doesn't just give Claude a
`[15:08]` preset to follow, it gives it a design
`[15:10]` approach to make better graphics in any
`[15:12]` style. Number two is generated assets. I
`[15:15]` told you Higgsfield was being used for
`[15:16]` the B-roll, but it also earns a spot a
`[15:18]` second time here because Claude can use
`[15:20]` it mid-edit to generate an image or a
`[15:22]` short clip and drop it straight into
`[15:24]` part of a graphic. And that changes what
`[15:26]` a graphic can be because up until this
`[15:28]` point your graphics were just text,
`[15:29]` charts, and screen recordings,
`[15:31]` essentially limited by what HTML could
`[15:33]` do. But sometimes you want icons or
`[15:35]` graphics that Hyperframes can't build
`[15:37]` with code. So you can get Higgsfield to
`[15:39]` generate them and then have Hyperframes
`[15:41]` incorporate those new images into the
`[15:43]` graphic. Number three is making your
`[15:45]` style file absorb every correction
`[15:47]` because right now every note you give
`[15:49]` Claude in that final review is a note
`[15:51]` you're going to give it again next week.
`[15:53]` The rule I've got in mind is that any
`[15:55]` correction coming out of the review gets
`[15:57]` written back into that style file before
`[15:59]` the edit is closed out. This is really,
`[16:02]` really important for getting this
`[16:04]` workflow fully automated over time
`[16:06]` because that way Claude is always
`[16:07]` learning from your inputs. And number
`[16:09]` four is the one that I think matters
`[16:11]` absolutely most to getting this done in
`[16:13]` one shot and it's not a tool, it's the
`[16:15]` pre-work that you put in before you even
`[16:17]` edit it. One of the biggest learnings
`[16:19]` I've had from using this over the past
`[16:20]` month is that the more time you spend
`[16:22]` planning the closer you will get these
`[16:24]` edits in one shot because the agent
`[16:26]` isn't guessing what you want anymore,
`[16:28]` it's just reading the comments from your
`[16:30]` script. 10 minutes of comments here will
`[16:32]` literally save you hours of back and
`[16:34]` forth and it's the single biggest
`[16:35]` difference between an edit that comes
`[16:37]` back usable and that and one that comes
`[16:39]` back needing hours of back and forth
`[16:41]` with Claude. So that's the whole system.
`[16:43]` I've actually packaged the entire
`[16:45]` pipeline into a guide with every prompt
`[16:47]` from this video and you can grab it
`[16:49]` completely free at the link below. And
`[16:51]` if you want to build the AI OS that runs
`[16:53]` this, that's what I'm teaching live at
`[16:55]` the Founder OS Build Shop on August
`[16:57]` 26th. The link is down there, too.
