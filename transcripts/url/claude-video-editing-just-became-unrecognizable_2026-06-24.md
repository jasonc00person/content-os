# Claude Video Editing Just Became Unrecognizable

- **Source:** https://www.youtube.com/watch?v=Aw3BkmhYu4I
- **Uploader:** Nate Herk | AI Automation
- **Uploaded:** 2026-04-23
- **Duration:** 28:12
- **Method:** YouTube captions (no transcription needed)

## Transcript

Claude is now editing my videos end-to-end. All I have to do is drop in a raw file and it is trimming out the mistakes and the dead space. It's adding motion graphics like you see over here. It's adding dynamic elements like you see over here. It can even add subtitles at the bottom of the screen like you're looking at right here. So, even if you've never coded before or you've never edited videos before, I'm going to show you guys exactly how you can get set up and get outputs that look pretty incredible just like this. All you have to do is use your natural language. It is so insane. Don't want to waste any of you guys' time, so let's just get straight into the video. So, yeah, I was able to take this you know, 50-second clip, drop it into Claude, and then it basically cut out all of the mistakes, all of the filler words, and now we have a 27-second clip with all of the motion graphics that you guys just saw. But, not only that, you can see we also have this timeline editor, which has all of the actual elements down here, all of the different motion graphics. So, if I wanted to, I could delete these. I could move them around, and I could change the timing. Because obviously what's super important about motion graphics is the timing. So, now we have this actual interface within our HyperFrames dashboard to make some really quick iterations. So, today I'm going to show you guys step-by-step setting up a fresh Claude project. We're going to get everything we need to get installed installed, and by the end you're going to know exactly how to edit videos just like you saw in the intro. All right. So, before we get into it, let's talk about the way that this actually works and sort of the tech stack that we're using. So, before we were able to use Claude and these other tools to edit videos, this was basically my process. I would have some sort of raw file, which would be a recording, and then I would go in there manually into, you know, like Adobe Premiere Pro, and I would trim out all of my mistakes, and I would trim out all of the retakes and things like that. And this was all very manual. So, I was doing this manually, and I was doing this manually, and then if I wanted to add any animations, I would be doing that manually, and then rendering is not a big deal, but I would be doing that manually as well. And then a few days back, this tool from HeyGen just dropped called HyperFrames. And I made a video about how we were able to use Claude with HyperFrames to get motion graphics and animations like this. And what I showed you guys in that video was basically us doing these first two pieces manually, but then we were using hyperframes to actually do the animations and the rendering. So, still a huge productivity boost, but we were still manually doing the trimming and editing. But now, we're taking a step farther because we have this new tool called Videouse, and Videouse is going to be the one that's doing the trimming and editing for us. So, right now, what we're doing is we're dropping in a raw file, and then it's basically being trimmed, edited, animated, and rendered for us, and it's really cool. Now, yes, we could get rid of the manual step of recording the raw file. I don't want to do that for YouTube because I want to keep these videos real, but I did actually make a video about that as well. In this video, I talked about how I used HeyGen to basically automate me recording the videos. So, I would drop in a script, and then it would give us the raw file. So, this step would actually change to a HeyGen avatar. And then because of the fact that the HeyGen avatar is perfect, we basically were able to just remove this trimming and editing step entirely, and then we would just get the animations and the rendering done. So, there's lots of ways that you can skin the cat here, but today what I'm showing you is basically just manual recording, and then the rest from there is taken care of us. And like I said, I'm going to show you guys this step-by-step. And of course, at the core of all of this, we're using Cloud Code as the orchestrator to connect all these different tools together. Don't be scared by the word Cloud Code. I'm going to show you how this works. It's super simple. So, today I'm going to be showing you guys how to do this with the desktop app of Cloud Code. Right here, you can see this is what VS Code looks like, which I've shown in a lot of my previous tutorials. I'm not going to use it today, but that is usually the main way I like to use it. Today, we're going to be using the Cloud desktop app just because the interface might feel a little less scary. Also, kind of funny, when you search Cloud desktop app, at least right now, Codex pops up. But anyways, you're going to install the Cloud desktop app. You can see you would go to this Cloud download page and just download this for your operating system right here. Now, once you open that up, it's obviously going to prompt you to sign in, and because we're using Cloud Code, you do need to be on a paid plan that it has access to Cloud Code. So, then what you're going to want to do is you're going to choose a folder to work in. So, you can come in here, open a folder, and just choose a brand new one. It can be completely empty, and you'll be all good to get set up. Or, what you could do is you could go over to my free school community. The link for that is down in the description, and you could grab this HyperFrame student kit. And all you need to do from here is you need to just grab the URL of this and give it to Cloud Code and say, "Hey, clone this repo, set up this project for me just like this." Like I said, link for this is in my free school community. Okay, but let's say you don't do that. What are the other tools you'll need? Well, I'm also going to attach in the description of this video this HyperFrames GitHub repo and the video use GitHub repo. A GitHub repo is basically just a project. It's a collection of folders and files, and Cloud is able to look through this and pull in the elements that it needs. So, literally all you would do is you would copy this link, go into Cloud Desktop, just paste it in, and then I'm going to go grab the other one as well for video use, and I'm going to paste that in, and I would just say, "Hey, I'm setting up this project to be basically my video editing studio. So, I want you to look at these two GitHub repos, and I want you to pull in the skills and pull in the important information that we need from these so that I could basically give you a raw video file, and you would be able to edit it, remove the filler words, and then help me add motion graphics to it. So, basically the full pipeline." And then, you just go ahead and shoot that off and let it do its thing, let it look through those, and let it pull in any of the files that it needs. Now, while this is running real quick, you guys might be asking like, "Why do you prefer to use the desktop app over VS Code or vice versa?" Well, typically for me, the reason why I like VS Code is because I can see all of my files. So, this is my Cloud Code project, right? And over here, I can see my assets. I can see my projects. I can see everything that I've dropped into here, whereas in the desktop app, you don't have visibility. Even though they're working out of the same folder, we just don't have that visibility because on the left-hand side here, all we are seeing is our other projects that we could switch into. We don't actually get to see all of the files. So, anyways, you can see it says, "Okay, good news. Almost all of this is already wired up. Everything's already set up because is project is already set up." So, you guys can either grab the repos or you can just basically do this exact same prompt and it will set up everything for you. Because all we need is we need the skills from Hyperframes and the skills from Video Use and then we're just going to start building some videos here. Okay, so because that's already happened, I'm just going to go in here and I'm going to do a slash command, which means I'm just going to clear out this conversation so we can start fresh. Okay, so I recorded this video right here. It's 50 seconds and it's basically just me kind of blabbing about what we're doing in this video, but I purposely made a few mistakes. I left a lot of, you know, silences and filler words in here. And remember, this is 50 seconds long. So, I dropped this into the project right here and I'm going to ask it to trim it for us. So, in here, if I type the at sign, it will show all of the different things that are in this project. And right here, if I go to the bottom, you can see we have edit demo raw, which is that video that I was just talking about. And so now it knows exactly what I'm actually referring to. And I'm just going to say, "Hey Cloud Code, I would like you to use the Video Use tool just to edit this video. I want you to analyze it. I want you to remove any filler words or silences or retakes. And then, what we're going to do after that is we're going to use Hyperframes to actually add the motion graphics to it. So, your first task is just to edit out the mistakes and the filler words." Okay, cool. So, while that's running, let me explain why we're doing it that way. Because like I showed you guys, ultimately what we're able to do is completely automate this pipeline, but we have to kind of work our way up there. And if we wanted to use Video Use to basically do everything, it could. Because within Video Use, there's actually kind of like a motion graphics actually kind of like a motion graphics skill skill called Remotion, which you guys might have been familiar with already. And the reason why we're using Hyperframes over Remotion is because we just like it better. I'll show you guys a comparison in just a sec here, but what you could do is say, "Hey, run the full Video Use pipeline, trim, animate, and render. I don't want to touch anything." And it would do it. It would do it with Remotion. So, let me show you an example. So, if you guys remember the intro to this video, we had these motion graphics, we had these kind of liquid glass cards and I thought this looks really, really good. We had this little, you know, animation there. I love this. This was hyper frames. Now, I dropped in that same raw video that you guys looked at here. I dropped in the same raw one into Cloud Code and I said, "Hey, do the full video use pipeline." And this is what it gave me when it used Re-motion. Cloud is now editing my videos end to end. All I have to do is drop in a raw file and it is trimming out the mistakes and the dead space. It's adding motion graphics like you see over here. It's adding dynamic elements like you see over here. It can even add subtitles at the bottom of the screen like you're looking at right here. So, even if you've never coded before or you've you've never coded before or you've never never So, you can see it trimmed it just fine because it went from 50 seconds to again about 27. It added things like this. It synced it up to the time that I was actually saying them. So, it all felt good, but I just like the hyper frames animations a little bit more. Real quick, I'll just show you guys a few other examples of what's possible. Here is Re-motion. So, it has a nice little background. It's got my face in the lower right corner. It has these motion graphics coming in. So, it's not to say that Re-motion isn't capable. It's just to say that right now with the new hyper frames, the way that it works with HTML, I just think I like it a little bit more. Here's another example where I changed the background and once again, we're still able to have animations come in and we can still make things look really, really nice just by using our natural language, which is obviously the big unlock. But, that same style of like animating a course or like a lesson, this is what we got with hyper frames. [snorts] So, once again, I think it's just a little bit more sophisticated and it just feels a little bit more engaging. So, that's really the main difference between Re-motion and hyper frames. They don't actually work under the hood the exact same way, so that's important to understand. But, as far as like this actual flow, they both basically do this step, which is the animate step. And then, they will both go ahead and do the rendering as well. But, really the most important part is that you trim it first and that you have the motion graphics synced up to the exact moments that you're saying the words that you want those animations to pop in at. So, what's important is that while you're trimming it and then before you animate, you're doing something to get the transcript and have like a timestamp correlated with every single word that you say. And all of that is obviously baked into our pipeline right here. Now, the other thing that I want you guys to think about is the fact that none of this is going to be perfect because it has to get used to your style and the way that you work. I always tell people to think about it like you're teaching a kid to ride a bike. You can't just chuck a kid on a bike and he or she's going to ride it perfectly. You have to hold the handlebars. You have to, you know, make sure that they're balancing properly. You have to help them adjust. And over time, it's going to get to the point where that kid is just riding the bike and you don't have to think about it. But, you have to steer it in the right way at first. So, inside of this Video Use project, there's going to be a few skills. And right here you can see when we were actually doing that thing to just edit it, it used one of its skills called Video Use and it was just basically doing an edit only for Hyperframes handoff. Now, within this skill, it has to actually transcribe the video. And there's a few different ways that you can do this. You can use OpenAI for a Whisper API. You can use a local sort of like tool which it can install for you and run in the background. That would be and run in the background. That would be free. free. Or you could use also 11 Labs API, which is what Video Use likes to default to. Hyperframes likes to default to OpenAI Whisper or just Whisper. For this video, I am using 11 Labs API because I think that it's actually better at finding the right moments to cut. But, all three of those methods are just fine. So, let's say you did want to use 11 Labs. Okay, what you would do is you would go to 11 Labs. You would come into the bottom left and click on developers and you would go to your API keys and then you would basically just create a key right here and then copy that value it gives you. you would just need to come into your Cloud Code project and drop that key into a file called a .env. So, the way that I would do that is I would basically pull up your project in an actual environment like this and I would create a new file called a .env or say, "Hey, Cloud Code, create me the .env." and then I'll go ahead and drop my 11 Labs API key inside of it. Or if you do want to use Visual Studio Code, which is like one of the reasons why I like to use it is cuz I can see everything right here, and I could literally just click on my dot env. This is the example, but I could click on the dot env, and then I could just paste in my API key right there. So, either way you want to do it, just I typically try to avoid just pasting it straight into the actual chat. And the reason for that is just because that would stay in the conversation history, and just best practice to not do that. So, what you can see is that it comes over here, and it says, "Okay, here's what I've got from the transcript. The raw clip is 50 seconds, and there are two clear retake moments to cut." So, here's what it wants to keep. Here's the clean intro. Here's what it wants to cut. I have a false start, so I kind of like started talking, and then I paused, and then I retake. So, it knows to cut that. It's going to keep the next take. It's going to cut another section where I stutter, and then it's going to keep the end. So, it's going to basically cut it down to about 37 seconds. And then it says, "Okay, I've got two taste calls for you. There's a trailing so at 42 20. Do you want to leave this as a natural breath, or get rid of it?" And then it says, "Cut edges around retakes. I'll snap to word boundaries with 50 ms leads." I'm just going to say, "Yep, make this as punchy as possible." And we'll shoot that off, and it will come back with a fully edited version for us. And then we'll add the motion graphics. And by the way, while we're waiting for all this, if you guys do want a bit of a deeper dive as far as like some other methods to edit videos with Claude, and I go into hyper frames a little bit more, I do an even more depth setup, and I talk at the end about like some cost and speed stuff, then definitely check out this video after the one that you're watching right now. All right, so that edit is complete. It is called edited.mp4. It is 32 seconds long, and let's go ahead and take a look to make sure that we're all good. Okay, I actually don't know where it put this, so I'm just going to say, "Give me the file path." It gave me the file path right here. I'm going to copy this, and we're going to paste that in to my explorer, and now we have the edited version. Okay, so this is going to be the example video that we're editing together live in this YouTube tutorial. So, I might make a few mistakes, and that's okay, because I'm going to show you exactly how we edit those out with AI without me having to do it. So, what did we go over today? We went over using video use to run the full pipeline, where you can drop in a raw file, it will edit it, and then it will do re-motion graphics. But, if you don't want to use the re-motion graphics, we also talked about how you can use hyperframes for those motion graphics as well. Hopefully now you guys understand. Let's keep on getting this video edited, and I hope that you all enjoy this YouTube video. Perfect. I mean, that was edited exactly the way that I would have done it myself manually, and now we're ready to move on to the next step. And you can see what else it created was the transcript. So, this should have all of the timestamps associated with it as well. You can see here if I go into my video projects, and I go into the edit demo, and I go into the assets, right here is where we see that edited MP4, and right here we can also see transcripts. And if we open up this JSON file, we can see the actual transcript, right? We see the full thing, but we also get the word-by-word breakdown. So, we can see that okay starts at 1.599 seconds. And if we wanted a motion graphic to start when I say the word you, then we would just need that motion graphic to start at 11 seconds.199. So, you can see this is super super precise, and that's going to help a ton with the motion graphics. Okay, so how do I like to do this? Well, on the first pass, because we don't yet have a style figured out, we have to sort of steer it, like I told you guys earlier. So, what I'm going to do is open this file back up, and I want to figure out when we want certain elements to pop in. So, here's kind of my process. I'm going to use my voice-to-text tool, which you guys can see in the description, and I'm just going to start talking and telling it how I want it to edit this video. Okay, so I need you to add motion graphics using hyperframes to this video. I'm going to give you some direction as far as what we're looking for. Okay, so this is going to be the example video that we're editing together live in this YouTube tutorial. together live in this YouTube tutorial. So, So, Okay, so at the beginning when I say this is the example video that we're editing live together, I want you to pop up a liquid glass style card on the left half of the screen, and I want the words to sort of appear as if they are karaoke style words popping in karaoke style subtitles and it should look like a title of a video. I might make a few mistakes and that's okay because I'm going to show you exactly how we edit those out with AI without me having to do it. So Okay and then the next part when I talk about I might make a few mistakes and that's okay. What I want you to do is add a card at the bottom of the screen that says you know, mistakes will be cut and then also add a motion graphic on the right side of the screen that just shows like an animation, you know, a visual understanding of what does it mean to edit out and trim mistakes. What did we go over today? We went over using video use to run the full pipeline where you can drop in a raw file, it will edit it and then it will do re motion graphics. But if you don't Okay and then the next part when I talk about the video use pipeline of dropping in a raw file and having it be edited and re motion graphics, I want you to animate that. I want you to show me on a liquid glass card an actual animation of raw file being edited up with motion graphics applied. So just, you know, show me, tell me a story. Paint a story here with these animations. Don't want to use the re motion graphics, we also talked about how you can use hyper frames for those motion graphics as well. Hope Okay and then the next piece when I talk about using hyper frames instead, I want you to just show a different version of motion graphics, maybe a different color or some other different animation style and you can do that as cards both on the left hand side of the screen and the right hand side of the screen. So that's what we want for this video. Make sure that everything is syncing up to the exact second where it makes the most sense for that motion graphic or that text to pop that motion graphic or that text to pop in. in. And yeah, that is your task. Let's see what you can do. Okay, so we've just shut off that prompt. What I like to do now is I like to switch this to plan mode. So, now it's able to basically look at the transcript, it's able to understand our request, and it's going to start to plan out, "Okay, I'm going to make this card, and here's what it's going to say, here's what's going to be on it. I'm going to have this come in at this timestamp. Are you okay with that?" And we're basically able to say, "Yes, I like this plan. Go build the motion graphics now." Or we can iterate a little bit before it actually wastes our time and our Cloud session limit actually coding out and building the HTML for the video. So, this planning stage is very important. All right, awesome. So, we got a plan back, which I can go ahead and make a little bit larger here. Okay, so, we have our talking head clip. We have the goal to add four HyperFrames motion graphics beats, which are kind of just like scenes, that feel like iOS 26 liquid glass premium UI over a lightly dimmed talking head, each synced to the exact spoken phrase, blah blah blah. That sounds good. We have an aesthetic direction. We have a motion philosophy doc, which if you download this um GitHub repo that I am giving you guys, then that will be in there as well. But that just has some best practices that I found for creating these motion graphics. But anyways, we have some color palette stuff. So, beat A is going to be an intro glow with teal. We've got orange, we've got purple, we've got graphite. But now let's go to the actual timeline. So, this is where we have to potentially make some changes to the plan. There's a bit of a bug here. It looks like this column is getting Oh, okay, never mind. I just had to scroll over a little bit. That does seem like a bit of a bug, but either way, the beat timeline. So, the intro is basically from 0 seconds to 5 seconds, and then we have 5 to 12, 12 to 20, and then we have different things going on. So, it's basically showing us what word is the anchor. So, what word is going to trigger the scene to basically start. So, this point we'd basically go through each of the beats or the scenes to make sure we like what it's saying. So, I'll go through one with you guys. I'm not going to read all of them cuz I don't want to bore you. But let's say beat A. And by the way, when I highlight, you can actually leave comments. So, if we need to comment, we can comment on something very specific, which is nice. But, I'm going to stop highlighting so that stops popping up. We've got a liquid glass card positioned on the left side, fills left half centered vertically. It covers the empty wall and door area, if you guys remember the camera, but it does not cover the speaker, which is great. It's going to have a tiny uppercase eyebrow that says edit demo chapter one. It's going to have a chrome gradient. It's going to have a large title that says the edit live, and that's going to be on two different lines, and then karaoke run beneath, so it's going to say, "This is going to be the example in 34 font." Okay. Timing anchors, cool. So, that sounds like it lines up with what I want. I'm going to quickly scan through these other beats, and then I'm going to shoot it off. Actually, I realized there's one more thing that we showed in that intro that I didn't do here. So, let me make a change. I'm going to click on revise, and I'm just going to say, "This all looks good, but I do want to add one more scene at the very end." For most of the video, or pretty much so far the whole video is just my face cam full screen. But, what I want to do is in the last 5 seconds, I want to transition. I want to take the face cam, and I want to vertical crop it with rounded edges and a drop shadow, and I want to reveal kind of just a dark mode modern-looking background, and I want the face cam to shift over to the right half of the screen. On the left half of the screen, I want there just to be text that says, "Thanks for watching." So, now I can just shoot off that revision. It's going to come back with another plan, and then I'm going to go ahead and approve it, and I'll check in with you guys when we have that first iteration done. But, basically, that's it. As you guys saw, I was just using my natural language. I was being very, very specific. And I know you guys are thinking, "Okay, well, how much time does that really save if you're being that specific every time?" Well, think about it like this. In my real project, I have video projects, right? So, if I open this up, you can see how many different videos I've made. I've made an app release video. I made a hype video. I made a lesson video. I made an intro. I made demos. All of these videos are training data. So, let's say I make five different lessons. Now, I can basically say, "Okay, cool. Build a lesson design markdown philosophy file." which means every time I build a lesson, just use that. And that's where you truly get to the point of dropping in a raw file and having it edited end-to-end once you've kind of established a style for that type of video. So, like here, you can see I've built three different YouTube shorts. They're not that great. We're still iterating a little bit, but we're going to get to a point where our shorts automation is so good that all I have to do is drop in a raw video and it will turn it into a short. So, that's kind of the mindset that I have here and that's the mindset you guys should have and that's why in this example I wanted to show you guys how specific I had to be to get a good output. Okay, so it looks like we're at a spot where this has come back with a version for us to look at. Now, if you come into the top right of the desktop app and you click on preview, you actually can preview it right here, which is kind of a nice feature and it's just not full screen. So, so you could definitely do it here if you wanted to, you know, not context switch out, but it's also as simple as just clicking into the tab. But anyways, now we are in here and let's just give this a quick watch and see what we've got. So, this is going to be the example video that we're editing together live in this YouTube tutorial. So, I might make a few mistakes and that's okay because I'm going to show you exactly how we edit those out with AI without me having to do it. So, what did we go over today? We went over using video use to run the full pipeline where you can drop in a raw file, it will edit it and then it will do re motion graphics. But if you don't want to use the re motion graphics, we also talked about how you can use hyperframes for those motion graphics as well. Hopefully now you guys understand. Let's keep on getting this video edited and I hope that you all enjoy this YouTube video. Okay, so not too bad. Obviously there's some things we need to fix like this was obviously horrible. It didn't get that right. Um the other thing I noticed is that this kind of covers my face a little bit which we'll want to tweak and then also um where was it? It Oh, just in general, there's like a grid and I think it's because when they go into this background, they want the grid to be there, which is fine, but having this grid just be there naturally is not what I want. So, at this point we just have to go back and make some more comments. Okay, so not bad. All of the motion graphics are coming in at the right time. I think you just made a few mistakes when it comes to the actual visuals. So, the first thing is in beat visuals. So, the first thing is in beat one, one, the liquid glass looks good, but it's actually covering my face a little bit. So, if you could just scale this down and then maybe crop off the right side a little bit so it doesn't cover my face, that would be beautiful. The next thing is that across the whole video, there's kind of like a grid pattern overlay that is visible and it shouldn't be there at all. I like the rest of the beats until we get to the end where you transition into the video crop. So, the problem is you need to crop the left side in and the right side in so we keep the center. We keep the face cam and that's a We keep the face cam and that's a vertical vertical ratio with rounded crop corners. ratio with rounded crop corners. And And that's mainly the issue because right now what you did is you just cropped the right side of the screen. Everything else about the video looks good. So, implement those changes and then we'll give it a look. So, I'll just paste that in and then once again I'm going to shoot this off. Also, I apologize if that video was like insanely loud. For some reason when it pulled it up in that local host, it just like tripled the decibels. I'm not exactly sure why. So, when we render it, it would be fine, but sometimes in the preview we get little things like that. But, we are lucky that the timing was good cuz iterating on the timing used to be a little bit annoying, but now you can see if I just kind of move this up, we have the audio. Aha, okay, so this is the actual I believe this is probably the um beat that is associated with sort of like the graph background. Um but, we could move these around, right? I don't have to because they all come in at the right times, but this is where the timeline editor is actually huge because you can, you know, shorten things like, you know, we could move this in or out, we could delete things, and what happens is because we make that change here, that change actually gets reflected in the actual code and then Cloud Code would see that and just make sure it reflects that change as well. So, for quick iterations, that can be a huge time saver. Okay, so here is the new version. I'm going to open up this localhost and let's give it a quick watch. Hopefully, it's not absurdly loud again. Okay, so this is going to be the example video that we're editing together live in this YouTube tutorial. So, I might make a few mistakes and that's okay because I'm going to show you exactly how we edit those out with AI without me. By the way, maybe I want to play with the spacing because it might look weird with like a right card and then this thing at the bottom and nothing on the left. But, I really like this this animation. Look at this. Those cards go red and then we have a scissor come across and cut those out. Like, remember, I didn't ask it to do that. I just said make an animation that looks like we're editing the video and it did that. Very nice. exactly how we edit those out with AI without me having to do it. So, what did we go over today? We went over using video use to run the full pipeline where you can drop in a raw file, it will edit it, and then it will do re-motion graphics. But, if you don't want to use the re-motion graphics, we also talked about how you can use hyper frames for those motion graphics as well. Hopefully, now you guys understand. Let's keep on getting this video edited and I hope that you all enjoy Okay, beautiful. Now that we have that, we could either keep going back and forth in editing like you guys saw, or we just basically say, "Hey, give me the render." And then it pops it into your project and you would just be able to, you know, throw that into whatever else you want, upload it. That's basically it. And like I said, just to switch back to the VS Code version now, because of the way that I've set up this project, every time I drop in raw assets, it all gets organized by project. So, for example, if we look at the edit demo, we now have assets. We have the clips, we have the transcripts, we have anything else that it needs. We have the compositions, which are the actual beats HTML, and this is what it's using in order to make those animations display, and this is what we're actually rendering. We have different components and then we have any final renders in here, and this is where it's verifying the actual screenshots, which is really cool. I'm basically telling it to take screenshots of what's going on in the scene to make sure that it looks good because sometimes it'll just come back and say, "Hey, I've done this but it doesn't look good at all." So, if we tell it to take screenshots, it has to go verify for itself. And that is just a really nice trick that I found out to do. So, anyways, like I said, now you have all these projects and you can start to make different folders. Every time you want to do an intro, if you want your intros to look like this, now you use this one as a reference and you just make your intros better every single time and that's where you get to the point where this is like way more automated. And the other thing I did want to call out is you guys watched me shoot off all of these prompts and you guys saw everything that it built, all of those different HTML files it had to make. How many tokens did this cost? This took us about 238,000 tokens. So, not too bad but not great either because this will eat some tokens. And that's why the more specific you can be with your planning and with your iterating, the better because you don't want it to go down the wrong path and then it waste tokens and it waste your time. So, be specific and if you guys want to dive into more stuff, then you can check out this video where I go deeper, like I said earlier, into some other tactics and show off some other examples and how you can get the most out of hyperframes. But anyways, as this slide says, thanks for watching. This is going to do it for today. I noticed that this is a little bit of a blurry thing that I would want to fix but that would be a super simple iteration for us. But anyways, if you enjoyed the video, please give it a like. It helps me out a ton. And as always, I appreciate you guys making it to the end of the video and I will see you all in the next one. Thanks you all in the next one. Thanks everyone.

## Timestamped

`[00:01]` Claude is now editing my videos
`[00:01]` end-to-end. All I have to do is drop in
`[00:03]` a raw file and it is trimming out the
`[00:05]` mistakes and the dead space. It's adding
`[00:07]` motion graphics like you see over here.
`[00:08]` It's adding dynamic elements like you
`[00:10]` see over here. It can even add subtitles
`[00:11]` at the bottom of the screen like you're
`[00:12]` looking at right here. So, even if
`[00:14]` you've never coded before or you've
`[00:15]` never edited videos before, I'm going to
`[00:17]` show you guys exactly how you can get
`[00:18]` set up and get outputs that look pretty
`[00:20]` incredible just like this. All you have
`[00:22]` to do is use your natural language. It
`[00:24]` is so insane. Don't want to waste any of
`[00:26]` you guys' time, so let's just get
`[00:27]` straight into the video. So, yeah, I was
`[00:28]` able to take this you know, 50-second
`[00:30]` clip, drop it into Claude, and then it
`[00:33]` basically cut out all of the mistakes,
`[00:35]` all of the filler words, and now we have
`[00:37]` a 27-second clip with all of the motion
`[00:39]` graphics that you guys just saw. But,
`[00:41]` not only that, you can see we also have
`[00:43]` this timeline editor, which has all of
`[00:44]` the actual elements down here, all of
`[00:46]` the different motion graphics. So, if I
`[00:47]` wanted to, I could delete these. I could
`[00:49]` move them around, and I could change the
`[00:51]` timing. Because obviously what's super
`[00:52]` important about motion graphics is the
`[00:54]` timing. So, now we have this actual
`[00:56]` interface within our HyperFrames
`[00:57]` dashboard to make some really quick
`[00:59]` iterations. So, today I'm going to show
`[01:01]` you guys step-by-step setting up a fresh
`[01:02]` Claude project. We're going to get
`[01:04]` everything we need to get installed
`[01:05]` installed, and by the end you're going
`[01:07]` to know exactly how to edit videos just
`[01:08]` like you saw in the intro. All right.
`[01:10]` So, before we get into it, let's talk
`[01:12]` about the way that this actually works
`[01:14]` and sort of the tech stack that we're
`[01:15]` using. So, before we were able to use
`[01:17]` Claude and these other tools to edit
`[01:19]` videos, this was basically my process. I
`[01:21]` would have some sort of raw file, which
`[01:22]` would be a recording, and then I would
`[01:24]` go in there manually into, you know,
`[01:26]` like Adobe Premiere Pro, and I would
`[01:27]` trim out all of my mistakes, and I would
`[01:29]` trim out all of the retakes and things
`[01:31]` like that. And this was all very manual.
`[01:34]` So, I was doing this manually, and I was
`[01:35]` doing this manually, and then if I
`[01:37]` wanted to add any animations, I would be
`[01:38]` doing that manually, and then rendering
`[01:40]` is not a big deal, but I would be doing
`[01:42]` that manually as well. And then a few
`[01:44]` days back, this tool from HeyGen just
`[01:45]` dropped called HyperFrames. And I made a
`[01:47]` video about how we were able to use
`[01:48]` Claude with HyperFrames to get motion
`[01:49]` graphics and animations like this. And
`[01:52]` what I showed you guys in that video was
`[01:54]` basically us doing these first two
`[01:57]` pieces manually, but then we were using
`[01:58]` hyperframes to actually do the
`[02:00]` animations and the rendering. So, still
`[02:03]` a huge productivity boost, but we were
`[02:06]` still manually doing the trimming and
`[02:07]` editing. But now, we're taking a step
`[02:09]` farther because we have this new tool
`[02:11]` called Videouse, and Videouse is going
`[02:14]` to be the one that's doing the trimming
`[02:15]` and editing for us. So, right now, what
`[02:17]` we're doing is we're dropping in a raw
`[02:18]` file, and then it's basically being
`[02:20]` trimmed, edited, animated, and rendered
`[02:23]` for us, and it's really cool. Now, yes,
`[02:25]` we could get rid of the manual step of
`[02:26]` recording the raw file. I don't want to
`[02:28]` do that for YouTube because I want to
`[02:29]` keep these videos real, but I did
`[02:31]` actually make a video about that as
`[02:33]` well. In this video, I talked about how
`[02:35]` I used HeyGen to basically automate me
`[02:38]` recording the videos. So, I would drop
`[02:40]` in a script, and then it would give us
`[02:41]` the raw file. So, this step would
`[02:43]` actually change to a HeyGen avatar. And
`[02:45]` then because of the fact that the HeyGen
`[02:46]` avatar is perfect, we basically were
`[02:48]` able to just remove this trimming and
`[02:50]` editing step entirely, and then we would
`[02:52]` just get the animations and the
`[02:53]` rendering done. So, there's lots of ways
`[02:55]` that you can skin the cat here, but
`[02:56]` today what I'm showing you is basically
`[02:58]` just manual recording, and then the rest
`[03:00]` from there is taken care of us. And like
`[03:02]` I said, I'm going to show you guys this
`[03:03]` step-by-step. And of course, at the core
`[03:05]` of all of this, we're using Cloud Code
`[03:07]` as the orchestrator to connect all these
`[03:08]` different tools together. Don't be
`[03:10]` scared by the word Cloud Code. I'm going
`[03:12]` to show you how this works. It's super
`[03:13]` simple. So, today I'm going to be
`[03:14]` showing you guys how to do this with the
`[03:15]` desktop app of Cloud Code. Right here,
`[03:17]` you can see this is what VS Code looks
`[03:19]` like, which I've shown in a lot of my
`[03:20]` previous tutorials. I'm not going to use
`[03:22]` it today, but that is usually the main
`[03:23]` way I like to use it. Today, we're going
`[03:25]` to be using the Cloud desktop app just
`[03:26]` because the interface might feel a
`[03:28]` little less scary. Also, kind of funny,
`[03:30]` when you search Cloud desktop app, at
`[03:31]` least right now, Codex pops up. But
`[03:33]` anyways, you're going to install the
`[03:35]` Cloud desktop app. You can see you would
`[03:36]` go to this Cloud download page and just
`[03:38]` download this for your operating system
`[03:40]` right here. Now, once you open that up,
`[03:41]` it's obviously going to prompt you to
`[03:42]` sign in, and because we're using Cloud
`[03:43]` Code, you do need to be on a paid plan
`[03:45]` that it has access to Cloud Code. So,
`[03:47]` then what you're going to want to do is
`[03:48]` you're going to choose a folder to work
`[03:50]` in. So, you can come in here, open a
`[03:51]` folder, and just choose a brand new one.
`[03:53]` It can be completely empty, and you'll
`[03:54]` be all good to get set up. Or, what you
`[03:57]` could do is you could go over to my free
`[03:58]` school community. The link for that is
`[03:59]` down in the description, and you could
`[04:01]` grab this HyperFrame student kit. And
`[04:03]` all you need to do from here is you need
`[04:04]` to just grab the URL of this and give it
`[04:06]` to Cloud Code and say, "Hey,
`[04:08]` clone this repo, set up this project for
`[04:09]` me just like this." Like I said, link
`[04:11]` for this is in my free school community.
`[04:13]` Okay, but let's say you don't do that.
`[04:14]` What are the other tools you'll need?
`[04:16]` Well, I'm also going to attach in the
`[04:17]` description of this video this
`[04:19]` HyperFrames GitHub repo and the video
`[04:22]` use GitHub repo. A GitHub repo is
`[04:24]` basically just a project. It's a
`[04:25]` collection of folders and files, and
`[04:27]` Cloud is able to look through this and
`[04:29]` pull in the elements that it needs. So,
`[04:31]` literally all you would do is you would
`[04:32]` copy this link, go into Cloud Desktop,
`[04:35]` just paste it in, and then I'm going to
`[04:37]` go grab the other one as well for video
`[04:38]` use, and I'm going to paste that in, and
`[04:40]` I would just say,
`[04:41]` "Hey, I'm setting up this project to be
`[04:43]` basically my video editing studio. So, I
`[04:45]` want you to look at these two GitHub
`[04:47]` repos, and I want you to pull in the
`[04:48]` skills and pull in the important
`[04:49]` information that we need from these so
`[04:51]` that I could basically give you a raw
`[04:53]` video file, and you would be able to
`[04:56]` edit it, remove the filler words, and
`[04:58]` then help me add motion graphics to it.
`[05:00]` So, basically the full pipeline." And
`[05:02]` then, you just go ahead and shoot that
`[05:03]` off and let it do its thing, let it look
`[05:05]` through those, and let it pull in any of
`[05:06]` the files that it needs.
`[05:08]` Now, while this is running real quick,
`[05:10]` you guys might be asking like, "Why do
`[05:11]` you prefer to use the desktop app over
`[05:13]` VS Code or vice versa?" Well, typically
`[05:16]` for me, the reason why I like VS Code is
`[05:18]` because I can see all of my files. So,
`[05:20]` this is my Cloud Code project, right?
`[05:22]` And over here, I can see my assets. I
`[05:24]` can see my projects. I can see
`[05:25]` everything that I've dropped into here,
`[05:27]` whereas in the desktop app, you don't
`[05:29]` have visibility. Even though they're
`[05:30]` working out of the same folder, we just
`[05:32]` don't have that visibility because on
`[05:33]` the left-hand side here, all we are
`[05:35]` seeing is our other projects that we
`[05:37]` could switch into. We don't actually get
`[05:39]` to see all of the files. So, anyways,
`[05:40]` you can see it says, "Okay, good news.
`[05:42]` Almost all of this is already wired up.
`[05:43]` Everything's already set up because is
`[05:45]` project is already set up." So, you guys
`[05:47]` can either grab the repos or you can
`[05:48]` just basically do this exact same prompt
`[05:50]` and it will set up everything for you.
`[05:52]` Because all we need is we need the
`[05:53]` skills from Hyperframes and the skills
`[05:55]` from Video Use and then we're just going
`[05:57]` to start building some videos here.
`[05:59]` Okay, so because that's already
`[05:59]` happened, I'm just going to go in here
`[06:01]` and I'm going to do a slash command,
`[06:02]` which means I'm just going to clear out
`[06:03]` this conversation so we can start fresh.
`[06:06]` Okay, so I recorded this video right
`[06:07]` here. It's 50 seconds and it's basically
`[06:09]` just me kind of blabbing about what
`[06:11]` we're doing in this video, but I
`[06:12]` purposely made a few mistakes. I left a
`[06:14]` lot of, you know, silences and filler
`[06:16]` words in here. And remember, this is 50
`[06:18]` seconds long. So, I dropped this into
`[06:20]` the project right here and I'm going to
`[06:22]` ask it to trim it for us. So, in here,
`[06:25]` if I type the at sign, it will show all
`[06:27]` of the different things that are in this
`[06:28]` project. And right here, if I go to the
`[06:30]` bottom, you can see we have edit demo
`[06:32]` raw, which is that video that I was just
`[06:33]` talking about. And so now it knows
`[06:35]` exactly what I'm actually referring to.
`[06:37]` And I'm just going to say,
`[06:38]` "Hey Cloud Code, I would like you to use
`[06:40]` the Video Use tool just to edit this
`[06:42]` video. I want you to analyze it. I want
`[06:44]` you to remove any filler words or
`[06:48]` silences or retakes. And then, what
`[06:50]` we're going to do after that is we're
`[06:51]` going to use Hyperframes to actually
`[06:53]` add the motion graphics to it. So, your
`[06:55]` first task is just to edit out the
`[06:58]` mistakes and the filler words." Okay,
`[07:00]` cool. So, while that's running, let me
`[07:01]` explain why we're doing it that way.
`[07:03]` Because like I showed you guys,
`[07:04]` ultimately what we're able to do is
`[07:06]` completely automate this pipeline, but
`[07:08]` we have to kind of work our way up
`[07:09]` there. And if we wanted to use Video Use
`[07:11]` to basically do everything, it could.
`[07:13]` Because within Video Use, there's
`[07:15]` actually kind of like a motion graphics
`[07:16]` actually kind of like a motion graphics skill
`[07:17]` skill
`[07:17]` called Remotion, which you guys might
`[07:19]` have been familiar with already.
`[07:21]` And the reason why we're using
`[07:22]` Hyperframes over Remotion is because we
`[07:25]` just like it better. I'll show you guys
`[07:26]` a comparison in just a sec here, but
`[07:29]` what you could do is say, "Hey, run the
`[07:30]` full Video Use pipeline, trim, animate,
`[07:32]` and render.
`[07:34]` I don't want to touch anything." And it
`[07:35]` would do it. It would do it with
`[07:36]` Remotion. So, let me show you an
`[07:37]` example. So, if you guys remember the
`[07:38]` intro to this video, we had these motion
`[07:40]` graphics, we had these kind of liquid
`[07:42]` glass cards and I thought this looks
`[07:43]` really, really good. We had this little,
`[07:45]` you know, animation there. I love this.
`[07:47]` This was hyper frames. Now, I dropped in
`[07:49]` that same raw video that you guys looked
`[07:52]` at here. I dropped in the same raw one
`[07:54]` into Cloud Code and I said, "Hey, do the
`[07:56]` full video use pipeline." And this is
`[07:58]` what it gave me when it used Re-motion.
`[08:00]` Cloud is now editing my videos end to
`[08:02]` end. All I have to do is drop in a raw
`[08:04]` file and it is trimming out the mistakes
`[08:06]` and the dead space. It's adding motion
`[08:07]` graphics like you see over here. It's
`[08:09]` adding dynamic elements like you see
`[08:10]` over here. It can even add subtitles at
`[08:12]` the bottom of the screen like you're
`[08:13]` looking at right here. So, even if
`[08:15]` you've never coded before or you've
`[08:16]` you've never coded before or you've never
`[08:17]` never
`[08:17]` So, you can see it trimmed it just fine
`[08:19]` because it went from 50 seconds to again
`[08:21]` about 27. It added things like this. It
`[08:23]` synced it up to the time that I was
`[08:24]` actually saying them. So, it all felt
`[08:26]` good, but I just like the hyper frames
`[08:29]` animations a little bit more. Real
`[08:31]` quick, I'll just show you guys a few
`[08:32]` other examples of what's possible. Here
`[08:33]` is Re-motion. So, it has a nice little
`[08:35]` background. It's got my face in the
`[08:36]` lower right corner. It has these motion
`[08:38]` graphics coming in. So, it's not to say
`[08:40]` that Re-motion isn't capable. It's just
`[08:42]` to say that right now with the new hyper
`[08:44]` frames, the way that it works with HTML,
`[08:45]` I just think I like it a little bit
`[08:47]` more. Here's another example where I
`[08:48]` changed the background and once again,
`[08:50]` we're still able to have animations come
`[08:51]` in and we can still make things look
`[08:52]` really, really nice just by using our
`[08:54]` natural language, which is obviously the
`[08:56]` big unlock. But, that same style of like
`[08:59]` animating a course or like a lesson,
`[09:01]` this is what we got with hyper frames.
`[09:03]` [snorts] So, once again, I think it's
`[09:04]` just a little bit more sophisticated and
`[09:06]` it just feels a little bit more
`[09:07]` engaging. So, that's really the main
`[09:09]` difference between Re-motion and hyper
`[09:11]` frames. They don't actually work under
`[09:13]` the hood the exact same way, so that's
`[09:14]` important to understand. But, as far as
`[09:16]` like this actual flow, they both
`[09:18]` basically do this step, which is the
`[09:20]` animate step. And then, they will both
`[09:21]` go ahead and do the rendering as well.
`[09:23]` But, really the most important part is
`[09:25]` that you trim it first and that you have
`[09:27]` the motion graphics synced up to the
`[09:30]` exact moments that you're saying the
`[09:31]` words that you want those animations to
`[09:32]` pop in at. So, what's important is that
`[09:34]` while you're trimming it and then before
`[09:35]` you animate, you're doing something to
`[09:38]` get the transcript and have like a
`[09:39]` timestamp correlated with every single
`[09:41]` word that you say. And all of that is
`[09:43]` obviously baked into our pipeline right
`[09:44]` here. Now, the other thing that I want
`[09:45]` you guys to think about is the fact that
`[09:47]` none of this is going to be perfect
`[09:49]` because it has to get used to your style
`[09:51]` and the way that you work. I always tell
`[09:53]` people to think about it like you're
`[09:54]` teaching a kid to ride a bike. You can't
`[09:56]` just chuck a kid on a bike and he or
`[09:58]` she's going to ride it perfectly. You
`[09:59]` have to hold the handlebars. You have
`[10:00]` to, you know, make sure that they're
`[10:02]` balancing properly. You have to help
`[10:03]` them adjust. And over time, it's going
`[10:05]` to get to the point where that kid is
`[10:06]` just riding the bike and you don't have
`[10:07]` to think about it. But, you have to
`[10:09]` steer it in the right way at first. So,
`[10:11]` inside of this Video Use project,
`[10:13]` there's going to be a few skills. And
`[10:14]` right here you can see when we were
`[10:15]` actually doing that thing to just edit
`[10:17]` it, it used one of its skills called
`[10:19]` Video Use and it was just basically
`[10:21]` doing an edit only for Hyperframes
`[10:23]` handoff. Now, within this skill, it has
`[10:25]` to actually transcribe the video. And
`[10:27]` there's a few different ways that you
`[10:27]` can do this. You can use OpenAI for a
`[10:30]` Whisper API. You can use a local sort of
`[10:33]` like tool which it can install for you
`[10:35]` and run in the background. That would be
`[10:37]` and run in the background. That would be free.
`[10:38]` free.
`[10:38]` Or you could use also 11 Labs API, which
`[10:40]` is what Video Use likes to default to.
`[10:43]` Hyperframes likes to default to OpenAI
`[10:44]` Whisper or just Whisper. For this video,
`[10:47]` I am using 11 Labs API because I think
`[10:49]` that it's actually better at finding the
`[10:51]` right moments to cut. But, all three of
`[10:53]` those methods are just fine. So, let's
`[10:54]` say you did want to use 11 Labs. Okay,
`[10:56]` what you would do is you would go to 11
`[10:58]` Labs. You would come into the bottom
`[10:59]` left and click on developers and you
`[11:01]` would go to your API keys and then you
`[11:03]` would basically just create a key right
`[11:04]` here and then copy that value it gives
`[11:06]` you. you would just need to come into
`[11:08]` your Cloud Code project and drop that
`[11:10]` key into a file called a .env. So, the
`[11:13]` way that I would do that is I would
`[11:14]` basically pull up your project in an
`[11:16]` actual environment like this and I would
`[11:18]` create a new file called a .env or say,
`[11:21]` "Hey, Cloud Code, create me the .env."
`[11:23]` and then I'll go ahead and drop my 11
`[11:25]` Labs API key inside of it. Or if you do
`[11:27]` want to use Visual Studio Code, which is
`[11:29]` like one of the reasons why I like to
`[11:31]` use it is cuz I can see everything right
`[11:32]` here, and I could literally just click
`[11:34]` on my dot env. This is the example, but
`[11:36]` I could click on the dot env, and then I
`[11:37]` could just paste in my API key right
`[11:39]` there. So, either way you want to do it,
`[11:42]` just I typically try to avoid just
`[11:44]` pasting it straight into the actual
`[11:45]` chat. And the reason for that is just
`[11:46]` because that would stay in the
`[11:48]` conversation history, and
`[11:50]` just best practice to not do that. So,
`[11:52]` what you can see is that it comes over
`[11:53]` here, and it says, "Okay, here's what
`[11:54]` I've got from the transcript. The raw
`[11:56]` clip is 50 seconds, and there are two
`[11:58]` clear retake moments to cut." So, here's
`[12:00]` what it wants to keep. Here's the clean
`[12:01]` intro. Here's what it wants to cut. I
`[12:03]` have a false start, so I kind of like
`[12:05]` started talking, and then I paused, and
`[12:06]` then I retake. So, it knows to cut that.
`[12:09]` It's going to keep the next take. It's
`[12:10]` going to cut another section where I
`[12:11]` stutter, and then it's going to keep the
`[12:13]` end. So, it's going to basically cut it
`[12:14]` down to about 37 seconds. And then it
`[12:17]` says, "Okay, I've got two taste calls
`[12:18]` for you. There's a trailing so at 42 20.
`[12:21]` Do you want to leave this as a natural
`[12:22]` breath, or get rid of it?" And then it
`[12:25]` says, "Cut edges around retakes. I'll
`[12:26]` snap to word boundaries with 50 ms
`[12:28]` leads." I'm just going to say, "Yep,
`[12:31]` make this as punchy
`[12:33]` as possible."
`[12:35]` And we'll shoot that off, and it will
`[12:36]` come back with a fully edited version
`[12:38]` for us. And then we'll add the motion
`[12:40]` graphics. And by the way, while we're
`[12:41]` waiting for all this, if you guys do
`[12:42]` want a bit of a deeper dive as far as
`[12:44]` like some other methods to edit videos
`[12:45]` with Claude, and I go into hyper frames
`[12:48]` a little bit more, I do an even more
`[12:49]` depth setup, and I talk at the end about
`[12:51]` like some cost and speed stuff, then
`[12:53]` definitely check out this video after
`[12:55]` the one that you're watching right now.
`[12:57]` All right, so that edit is complete. It
`[12:58]` is called edited.mp4. It is 32 seconds
`[13:01]` long, and let's go ahead and take a look
`[13:02]` to make sure that we're all good. Okay,
`[13:04]` I actually don't know where it put this,
`[13:05]` so I'm just going to say, "Give me the
`[13:07]` file path." It gave me the file path
`[13:09]` right here. I'm going to copy this,
`[13:11]` and we're going to paste that in to my
`[13:13]` explorer, and now we have the edited
`[13:15]` version. Okay, so this is going to be
`[13:17]` the example video that we're editing
`[13:19]` together live in this YouTube tutorial.
`[13:21]` So, I might make a few mistakes, and
`[13:23]` that's okay, because I'm going to show
`[13:24]` you exactly how we edit those out with
`[13:26]` AI without me having to do it. So, what
`[13:28]` did we go over today? We went over using
`[13:30]` video use to run the full pipeline,
`[13:32]` where you can drop in a raw file, it
`[13:34]` will edit it, and then it will do
`[13:36]` re-motion graphics. But, if you don't
`[13:37]` want to use the re-motion graphics, we
`[13:39]` also talked about how you can use
`[13:40]` hyperframes for those motion graphics as
`[13:42]` well. Hopefully now you guys understand.
`[13:44]` Let's keep on getting this video edited,
`[13:46]` and I hope that you all enjoy this
`[13:47]` YouTube video.
`[13:49]` Perfect. I mean, that was edited exactly
`[13:51]` the way that I would have done it myself
`[13:53]` manually, and now we're ready to move on
`[13:55]` to the next step. And you can see what
`[13:56]` else it created was the transcript. So,
`[13:58]` this should have all of the timestamps
`[14:00]` associated with it as well. You can see
`[14:02]` here if I go into my video projects, and
`[14:03]` I go into the edit demo, and I go into
`[14:05]` the assets, right here is where we see
`[14:07]` that edited MP4, and right here we can
`[14:09]` also see transcripts. And if we open up
`[14:11]` this JSON file, we can see the actual
`[14:13]` transcript, right? We see the full
`[14:15]` thing, but we also get the word-by-word
`[14:17]` breakdown. So, we can see that okay
`[14:19]` starts at 1.599
`[14:21]` seconds. And if we wanted a motion
`[14:23]` graphic to start when I say the word
`[14:25]` you, then we would just need that motion
`[14:27]` graphic to start at 11 seconds.199. So,
`[14:30]` you can see this is super super precise,
`[14:31]` and that's going to help a ton with the
`[14:33]` motion graphics. Okay, so how do I like
`[14:34]` to do this? Well, on the first pass,
`[14:36]` because we don't yet have a style
`[14:38]` figured out, we have to sort of steer
`[14:40]` it, like I told you guys earlier. So,
`[14:41]` what I'm going to do is open this file
`[14:43]` back up, and I want to figure out
`[14:45]` when we want certain elements to pop in.
`[14:48]` So, here's kind of my process. I'm going
`[14:50]` to use my voice-to-text tool, which you
`[14:52]` guys can see in the description, and I'm
`[14:54]` just going to start talking and telling
`[14:55]` it how I want it to edit this video.
`[14:57]` Okay, so I need you to add motion
`[14:59]` graphics using hyperframes to this
`[15:01]` video. I'm going to give you some
`[15:03]` direction as far as what we're looking
`[15:04]` for. Okay, so this is going to be the
`[15:06]` example video that we're editing
`[15:07]` together live in this YouTube tutorial.
`[15:10]` together live in this YouTube tutorial. So,
`[15:11]` So,
`[15:11]` Okay, so at the beginning when I say
`[15:13]` this is the example video that we're
`[15:14]` editing live together, I want you to pop
`[15:17]` up a liquid glass style card on the left
`[15:19]` half of the screen, and I want the words
`[15:21]` to sort of appear as if they are karaoke
`[15:24]` style words popping in karaoke style
`[15:26]` subtitles and it should look like a
`[15:29]` title of a video.
`[15:34]` I might make a few mistakes and that's
`[15:34]` okay because I'm going to show you
`[15:35]` exactly how we edit those out with AI
`[15:37]` without me having to do it. So
`[15:40]` Okay and then the next part when I talk
`[15:41]` about I might make a few mistakes and
`[15:43]` that's okay. What I want you to do is
`[15:46]` add a card at the bottom of the screen
`[15:49]` that says you know, mistakes will be cut
`[15:52]` and then also add a motion graphic on
`[15:54]` the right side of the screen that just
`[15:55]` shows like an animation, you know, a
`[15:57]` visual understanding of what does it
`[15:59]` mean to edit out and trim mistakes.
`[16:01]` What did we go over today? We went over
`[16:03]` using video use to run the full pipeline
`[16:06]` where you can drop in a raw file, it
`[16:07]` will edit it and then it will do re
`[16:09]` motion graphics. But if you don't
`[16:11]` Okay and then the next part when I talk
`[16:13]` about the video use pipeline of dropping
`[16:16]` in a raw file and having it be edited
`[16:19]` and re motion graphics, I want you to
`[16:21]` animate that. I want you to show me on a
`[16:23]` liquid glass card an actual animation of
`[16:26]` raw file being edited up with motion
`[16:29]` graphics applied. So just, you know,
`[16:31]` show me, tell me a story. Paint a story
`[16:33]` here with these animations. Don't want
`[16:35]` to use the re motion graphics, we also
`[16:37]` talked about how you can use hyper
`[16:38]` frames for those motion graphics as
`[16:40]` well. Hope
`[16:41]` Okay and then the next piece when I talk
`[16:42]` about using hyper frames instead, I want
`[16:45]` you to
`[16:46]` just show a different version of motion
`[16:48]` graphics, maybe a different color or
`[16:49]` some other different animation style and
`[16:51]` you can do that as cards both on the
`[16:54]` left hand side of the screen and the
`[16:55]` right hand side of the screen.
`[16:57]` So that's what we want for this video.
`[17:00]` Make sure that everything is syncing up
`[17:01]` to the exact second where it makes the
`[17:04]` most sense for
`[17:05]` that motion graphic or that text to pop
`[17:07]` that motion graphic or that text to pop in.
`[17:08]` in.
`[17:08]` And yeah, that is your task. Let's see
`[17:11]` what you can do.
`[17:13]` Okay, so we've just shut off that
`[17:15]` prompt. What I like to do now is I like
`[17:17]` to switch this to plan mode. So, now
`[17:19]` it's able to basically
`[17:20]` look at the transcript, it's able to
`[17:23]` understand our request, and it's going
`[17:25]` to start to plan out, "Okay, I'm going
`[17:27]` to make this card, and here's what it's
`[17:28]` going to say, here's what's going to be
`[17:29]` on it. I'm going to have this come in at
`[17:31]` this timestamp. Are you okay with that?"
`[17:33]` And we're basically able to say, "Yes, I
`[17:35]` like this plan. Go build the motion
`[17:37]` graphics now." Or we can iterate a
`[17:38]` little bit before it actually wastes our
`[17:40]` time and our Cloud session limit
`[17:43]` actually coding out and building the
`[17:45]` HTML for the video. So, this planning
`[17:47]` stage is very important. All right,
`[17:49]` awesome. So, we got a plan back, which I
`[17:51]` can go ahead and make a little bit
`[17:52]` larger here. Okay, so, we have our
`[17:54]` talking head clip. We have the goal to
`[17:56]` add four HyperFrames motion graphics
`[17:58]` beats, which are kind of just like
`[17:59]` scenes, that feel like iOS 26 liquid
`[18:02]` glass premium UI over a lightly dimmed
`[18:04]` talking head, each synced to the exact
`[18:06]` spoken phrase, blah blah blah. That
`[18:08]` sounds good.
`[18:10]` We have an aesthetic direction. We have
`[18:11]` a motion philosophy doc, which if you
`[18:14]` download this um GitHub repo that I am
`[18:16]` giving you guys, then that will be in
`[18:18]` there as well. But that just has some
`[18:19]` best practices that I found for creating
`[18:22]` these motion graphics. But anyways, we
`[18:24]` have some color palette stuff. So, beat
`[18:26]` A is going to be an intro glow with
`[18:29]` teal. We've got orange, we've got
`[18:31]` purple, we've got graphite. But now
`[18:32]` let's go to the actual timeline. So,
`[18:34]` this is where we have to potentially
`[18:35]` make some changes to the plan. There's a
`[18:37]` bit of a bug here. It looks like this
`[18:38]` column is getting Oh, okay, never mind.
`[18:40]` I just had to scroll over a little bit.
`[18:41]` That does seem like a bit of a bug, but
`[18:42]` either way, the beat timeline. So, the
`[18:44]` intro is basically from 0 seconds to 5
`[18:47]` seconds, and then we have 5 to 12, 12 to
`[18:50]` 20, and then we have different things
`[18:51]` going on. So, it's basically showing us
`[18:53]` what word is the anchor. So, what word
`[18:55]` is going to trigger the scene to
`[18:57]` basically start. So, this point we'd
`[18:58]` basically go through each of the beats
`[19:00]` or the scenes to make sure we like what
`[19:01]` it's saying. So, I'll go through one
`[19:03]` with you guys. I'm not going to read all
`[19:04]` of them cuz I don't want to bore you.
`[19:05]` But let's say beat A.
`[19:07]` And by the way, when I highlight, you
`[19:08]` can actually leave comments. So, if we
`[19:09]` need to comment, we can comment on
`[19:11]` something very specific, which is nice.
`[19:12]` But, I'm going to stop highlighting so
`[19:13]` that stops popping up. We've got a
`[19:15]` liquid glass card positioned on the left
`[19:17]` side, fills left half centered
`[19:19]` vertically. It covers the empty wall and
`[19:22]` door area, if you guys remember the
`[19:23]` camera, but it does not cover the
`[19:25]` speaker, which is great. It's going to
`[19:26]` have a tiny uppercase eyebrow that says
`[19:28]` edit demo chapter one. It's going to
`[19:30]` have a chrome gradient. It's going to
`[19:32]` have a large title that says the edit
`[19:33]` live, and that's going to be on two
`[19:35]` different lines, and then karaoke run
`[19:37]` beneath, so it's going to say, "This is
`[19:38]` going to be the example in 34 font."
`[19:42]` Okay. Timing anchors, cool. So, that
`[19:45]` sounds like it lines up with what I
`[19:46]` want. I'm going to quickly scan through
`[19:48]` these other beats, and then I'm going to
`[19:50]` shoot it off. Actually, I realized
`[19:51]` there's one more thing that we showed in
`[19:53]` that intro that I didn't do here. So,
`[19:55]` let me make a change.
`[19:57]` I'm going to click on revise, and I'm
`[19:58]` just going to say,
`[20:00]` "This all looks good, but I do want to
`[20:01]` add one more scene at the very end."
`[20:03]` For most of the video, or pretty much so
`[20:06]` far the whole video is just my face cam
`[20:08]` full screen. But, what I want to do is
`[20:10]` in the last 5 seconds, I want to
`[20:11]` transition. I want to take the face cam,
`[20:14]` and I want to vertical crop it with
`[20:15]` rounded edges and a drop shadow, and I
`[20:17]` want to reveal kind of just a dark mode
`[20:20]` modern-looking background, and I want
`[20:22]` the face cam to shift over to the right
`[20:25]` half of the screen. On the left half of
`[20:26]` the screen, I want there just to be text
`[20:28]` that says, "Thanks for watching." So,
`[20:29]` now I can just shoot off that revision.
`[20:31]` It's going to come back with another
`[20:32]` plan, and then I'm going to go ahead and
`[20:33]` approve it, and I'll check in with you
`[20:34]` guys when we have that first iteration
`[20:36]` done. But, basically, that's it. As you
`[20:37]` guys saw, I was just using my natural
`[20:40]` language. I was being very, very
`[20:41]` specific. And I know you guys are
`[20:42]` thinking, "Okay, well, how much time
`[20:43]` does that really save if you're being
`[20:44]` that specific every time?" Well, think
`[20:46]` about it like this. In my real project,
`[20:49]` I have video projects, right? So, if I
`[20:51]` open this up, you can see how many
`[20:52]` different videos I've made. I've made an
`[20:54]` app release video. I made a hype video.
`[20:55]` I made a lesson video. I made an intro.
`[20:57]` I made demos. All of these videos are
`[20:59]` training data. So, let's say I make five
`[21:01]` different lessons. Now, I can basically
`[21:03]` say, "Okay, cool. Build a lesson design
`[21:06]` markdown philosophy file." which means
`[21:08]` every time I build a lesson, just use
`[21:10]` that. And that's where you truly get to
`[21:12]` the point of dropping in a raw file and
`[21:14]` having it edited end-to-end once you've
`[21:16]` kind of established a style for that
`[21:18]` type of video. So, like here, you can
`[21:20]` see I've built three different YouTube
`[21:21]` shorts. They're not that great. We're
`[21:23]` still iterating a little bit, but we're
`[21:24]` going to get to a point where our shorts
`[21:25]` automation is so good that all I have to
`[21:27]` do is drop in a raw video and it will
`[21:28]` turn it into a short. So, that's kind of
`[21:30]` the mindset that I have here and that's
`[21:31]` the mindset you guys should have and
`[21:33]` that's why in this example I wanted to
`[21:34]` show you guys how specific I had to be
`[21:37]` to get a good output. Okay, so it looks
`[21:39]` like we're at a spot where this has come
`[21:41]` back with a version for us to look at.
`[21:43]` Now, if you come into the top right of
`[21:44]` the desktop app and you click on
`[21:45]` preview, you actually can preview it
`[21:47]` right here, which is kind of a nice
`[21:48]` feature and it's just not full screen.
`[21:50]` So, so you could definitely do it here
`[21:52]` if you wanted to, you know, not context
`[21:53]` switch out, but it's also as simple as
`[21:55]` just clicking into the tab. But anyways,
`[21:58]` now we are in here and let's just give
`[21:59]` this a quick watch and see what we've
`[22:00]` got. So, this is going to be the example
`[22:02]` video that we're editing together live
`[22:04]` in this YouTube tutorial. So, I might
`[22:07]` make a few mistakes and that's okay
`[22:08]` because I'm going to show you exactly
`[22:09]` how we edit those out with AI without me
`[22:12]` having to do it. So, what did we go over
`[22:13]` today? We went over using video use to
`[22:16]` run the full pipeline where you can drop
`[22:18]` in a raw file, it will edit it and then
`[22:20]` it will do re motion graphics. But if
`[22:22]` you don't want to use the re motion
`[22:23]` graphics, we also talked about how you
`[22:24]` can use hyperframes for those motion
`[22:26]` graphics as well. Hopefully now you guys
`[22:28]` understand. Let's keep on getting this
`[22:30]` video edited and I hope that you all
`[22:31]` enjoy this YouTube video.
`[22:34]` Okay, so not too bad. Obviously there's
`[22:35]` some things we need to fix like this was
`[22:37]` obviously horrible. It didn't get that
`[22:40]` right. Um the other thing I noticed is
`[22:42]` that this kind of covers my face a
`[22:43]` little bit which we'll want to tweak and
`[22:45]` then also um where was it? It Oh, just
`[22:48]` in general, there's like a grid and I
`[22:49]` think it's because when they go into
`[22:50]` this background, they want the grid to
`[22:52]` be there, which is fine, but having this
`[22:54]` grid just be there naturally is not what
`[22:57]` I want. So, at this point we just have
`[22:58]` to go back and make some more comments.
`[23:01]` Okay, so not bad. All of the motion
`[23:04]` graphics are coming in at the right
`[23:05]` time. I think you just made a few
`[23:07]` mistakes when it comes to the actual
`[23:09]` visuals. So, the first thing is in beat
`[23:12]` visuals. So, the first thing is in beat one,
`[23:13]` one,
`[23:13]` the liquid glass looks good, but it's
`[23:16]` actually covering my face a little bit.
`[23:17]` So, if you could just scale this down
`[23:19]` and then maybe crop off the right side a
`[23:22]` little bit so it doesn't cover my face,
`[23:23]` that would be beautiful. The next thing
`[23:26]` is that across the whole video, there's
`[23:28]` kind of like a grid pattern overlay that
`[23:31]` is visible and it shouldn't be there
`[23:34]` at all. I like the rest of the beats
`[23:37]` until we get to the end where you
`[23:39]` transition into the video crop. So, the
`[23:41]` problem is
`[23:43]` you need to crop the left side in and
`[23:45]` the right side in so we keep the center.
`[23:47]` We keep the face cam and that's a
`[23:49]` We keep the face cam and that's a vertical
`[23:50]` vertical
`[23:50]` ratio with rounded crop corners.
`[23:54]` ratio with rounded crop corners. And
`[23:56]` And
`[23:56]` that's mainly the issue because right
`[23:58]` now what you did is you just cropped the
`[23:59]` right side of the screen. Everything
`[24:01]` else about the video looks good. So,
`[24:03]` implement those changes and then we'll
`[24:04]` give it a look. So, I'll just paste that
`[24:06]` in and then once again I'm going to
`[24:07]` shoot this off. Also, I apologize if
`[24:09]` that video was like insanely loud. For
`[24:11]` some reason when it pulled it up in that
`[24:12]` local host, it just like tripled the
`[24:14]` decibels. I'm not exactly sure why. So,
`[24:16]` when we render it, it would be fine, but
`[24:18]` sometimes in the preview we get little
`[24:19]` things like that. But, we are lucky that
`[24:21]` the timing was good cuz iterating on the
`[24:22]` timing used to be a little bit annoying,
`[24:24]` but now you can see if I just kind of
`[24:26]` move this up, we have the audio. Aha,
`[24:28]` okay, so this is the actual I believe
`[24:31]` this is probably the
`[24:33]` um beat that is associated with sort of
`[24:34]` like the graph background. Um but, we
`[24:37]` could move these around, right? I don't
`[24:38]` have to because they all come in at the
`[24:39]` right times, but this is where the
`[24:41]` timeline editor is actually huge because
`[24:43]` you can, you know, shorten things like,
`[24:45]` you know, we could move this in or out,
`[24:46]` we could delete things, and what happens
`[24:49]` is because we make that change here,
`[24:51]` that change actually gets reflected in
`[24:52]` the actual code and then Cloud Code
`[24:55]` would see that and just make sure it
`[24:56]` reflects that change as well.
`[24:58]` So, for quick iterations, that can be a
`[25:00]` huge time saver. Okay, so here is the
`[25:03]` new version. I'm going to open up this
`[25:04]` localhost and let's give it a quick
`[25:06]` watch. Hopefully, it's not absurdly loud
`[25:07]` again. Okay, so this is going to be the
`[25:09]` example video that we're editing
`[25:11]` together live in this YouTube tutorial.
`[25:14]` So, I might make a few mistakes and
`[25:15]` that's okay because I'm going to show
`[25:16]` you exactly how we edit those out with
`[25:18]` AI without me. By the way, maybe I want
`[25:21]` to play with the spacing because it
`[25:22]` might look weird with like a right card
`[25:24]` and then this thing at the bottom and
`[25:25]` nothing on the left. But, I really like
`[25:26]` this this animation. Look at this. Those
`[25:29]` cards go red and then we have a scissor
`[25:31]` come across and cut those out. Like,
`[25:34]` remember, I didn't ask it to do that. I
`[25:35]` just said make an animation that looks
`[25:36]` like we're editing the video and it did
`[25:38]` that. Very nice.
`[25:40]` exactly how we edit those out with AI
`[25:42]` without me having to do it. So, what did
`[25:44]` we go over today? We went over using
`[25:45]` video use to run the full pipeline where
`[25:48]` you can drop in a raw file, it will edit
`[25:50]` it, and then it will do re-motion
`[25:52]` graphics. But, if you don't want to use
`[25:53]` the re-motion graphics, we also talked
`[25:55]` about how you can use hyper frames for
`[25:57]` those motion graphics as well.
`[25:58]` Hopefully, now you guys understand.
`[26:00]` Let's keep on getting this video edited
`[26:01]` and I hope that you all enjoy Okay,
`[26:03]` beautiful. Now that we have that, we
`[26:05]` could either keep going back and forth
`[26:07]` in editing like you guys saw, or we just
`[26:09]` basically say, "Hey, give me the
`[26:10]` render." And then it pops it into your
`[26:11]` project and you would just be able to,
`[26:13]` you know, throw that into whatever else
`[26:14]` you want, upload it. That's basically
`[26:17]` it. And like I said, just to switch back
`[26:18]` to the VS Code version now, because of
`[26:21]` the way that I've set up this project,
`[26:23]` every time I drop in raw assets, it all
`[26:25]` gets organized by project. So, for
`[26:27]` example, if we look at the edit demo, we
`[26:29]` now have assets. We have the clips, we
`[26:32]` have the transcripts, we have anything
`[26:33]` else that it needs. We have the
`[26:34]` compositions, which are the actual beats
`[26:36]` HTML, and this is what it's using in
`[26:38]` order to make those animations display,
`[26:40]` and this is what we're actually
`[26:41]` rendering. We have different components
`[26:43]` and then we have any final renders in
`[26:44]` here, and this is where it's verifying
`[26:46]` the actual screenshots, which is really
`[26:48]` cool. I'm basically telling it to take
`[26:49]` screenshots of what's going on in the
`[26:51]` scene to make sure that it looks good
`[26:53]` because sometimes it'll just come back
`[26:55]` and say, "Hey, I've done this but it
`[26:56]` doesn't look good at all." So, if we
`[26:58]` tell it to take screenshots, it has to
`[26:59]` go verify for itself. And that is just a
`[27:01]` really nice trick that I found out to
`[27:03]` do. So, anyways, like I said, now you
`[27:05]` have all these projects and you can
`[27:06]` start to make different folders. Every
`[27:08]` time you want to do an intro, if you
`[27:09]` want your intros to look like this, now
`[27:11]` you use this one as a reference and you
`[27:13]` just make your intros better every
`[27:14]` single time and that's where you get to
`[27:16]` the point where this is like way more
`[27:18]` automated. And the other thing I did
`[27:19]` want to call out is you guys watched me
`[27:21]` shoot off all of these prompts and you
`[27:23]` guys saw everything that it built, all
`[27:24]` of those different HTML files it had to
`[27:26]` make. How many tokens did this cost?
`[27:28]` This took us about 238,000 tokens. So,
`[27:31]` not too bad but not great either because
`[27:34]` this will eat some tokens. And that's
`[27:36]` why the more specific you can be with
`[27:38]` your planning and with your iterating,
`[27:40]` the better because you don't want it to
`[27:41]` go down the wrong path and then it waste
`[27:43]` tokens and it waste your time. So, be
`[27:45]` specific and if you guys want to dive
`[27:46]` into more stuff, then you can check out
`[27:48]` this video where I go deeper, like I
`[27:49]` said earlier, into some other tactics
`[27:51]` and show off some other examples and how
`[27:53]` you can get the most out of hyperframes.
`[27:56]` But anyways, as this slide says, thanks
`[27:58]` for watching. This is going to do it for
`[27:59]` today. I noticed that this is a little
`[28:00]` bit of a blurry thing that I would want
`[28:02]` to fix but that would be a super simple
`[28:04]` iteration for us. But anyways, if you
`[28:05]` enjoyed the video, please give it a
`[28:07]` like. It helps me out a ton. And as
`[28:08]` always, I appreciate you guys making it
`[28:09]` to the end of the video and I will see
`[28:10]` you all in the next one. Thanks
`[28:11]` you all in the next one. Thanks everyone.
