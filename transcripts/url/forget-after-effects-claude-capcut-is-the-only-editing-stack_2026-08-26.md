# Forget After Effects: Claude + CapCut Is the Only Editing Stack You Need

- **Source:** https://www.youtube.com/watch?v=j4FzO2fF1kg
- **Uploader:** Sanji Nai-Chien
- **Uploaded:** 2026-08-19
- **Duration:** 22:39
- **Method:** YouTube captions (no transcription needed)

## Transcript

What you just watched, every cut, every animation, and every transition was created by Claude within Cap Cut in less than 20 minutes. So far, there honestly hasn't been a single edit or really a single thing that this combination couldn't handle. But to get it to this point, I've spent weeks of trial and error and a ton of credits. But that way, you won't have to. So, in this video, I'm going to tell you everything you need to know to create stunning videos with color grading, motion design, and animation. And the best part is that it'll all be done by AI. So, here's the plan. I took one raw video and by the end of this tutorial, we will transform it completely. Every improvement goes into a different part of the same video. So, watch the before and make sure to stick around for the after. So, first you'll need to install Claude on your computer. And in the previous video, we talked about how to use one of Claude's features called design to create highquality motion effects. Today we're going to talk about another killer combination of Claude, Cap Cut and Claude. So if you don't have Claude yet, make sure to go to Claudeai and download the app for Mac or PC. If you don't have Cap Cut, you'll need to do the same. Now, let's jump back to Claude. When you log in for the first time, it'll likely appear exactly as you see on my screen. So, previously when I shot this video, we threw together a rough edit, and honestly, it looked bad. Flat colors, no life in it. Now, normally this is where you'd give up or you'd hire a colorist, but instead we're going to fix the color foundation and we're going to do it right inside of Clot. So, let's take our single timeline, drop the raw footage in, and look at the first problem. Now, every editor knows the pain of spending hours tweaking color wheels just to fix flat log footage, only for it to still look washed out. This is where we will need LUT. LUT is an instruction file that tells the program to replace each color in the picture with a different one. For example, make this shade of blue a little warmer, these shadows are greenish, the skin is softer, etc. We need an LUT, particularly because it's the only way to package an entire color grade into a single small file that Claude can generate from using a text prompt or any editor like Cap Cut, which can instantly apply it to your footage. So all that I need to do is ask, "Please generate a clean soft pastel LUT file for my YouTube videos. Cinematic and clean." Then I just click send. Now after generating, Claude gives you a summary of the look. Lifted shadows, subtle teal and peach split toning, reduced saturation, low contrast, ultimately a clean studio aesthetic with friendly skin tones. Now, if you go a bit further, you'll find the actual file. Click on it and then find the arrow and choose download. Save the file to your downloads folder or really any preferred location. So let's click save. And since I've already generated the file, I'm just going to click replace. Now in Cap Cut, go to adjustment and select LUT. Then click import to find and open the cube file. This imports it into Cap Cut for your project. Next, we'll click the plus icon to add a new layer to the timeline, which you can extend over your footage. Switching it on and off will show the filter applied to your footage. Now, I felt like it was a bit too intense, so I adjusted the selection to about 50%. That looks great. Claude's main strength lies in its precise adjustment capabilities. For instance, I dislike the shadow in this design because it clashed with the clean look. I requested Claude to create a version without the teal, and the difference was evident. Now, setting this to 50% produced a gentle pastel studio vibe. So, that's the entire base video graded. Now that the whole timeline looks clean, we can start layering effects on top of specific moments. Now that the color of our video looks great, let's take it one step further and make it even better by adding some visualization. Now, usually doing a dynamic counting animation means manually placing hundreds of key frames in in After Effects or buying a bunch of templates that ultimately break your project file. Now, the first moment that I want to upgrade is right here. The part of the video where I talk about numbers. A static number on screen is boring. So, let's make it count up. For example, do you guys remember in the Mr. Beast videos when the dollar icon wildly spins up? That's the kind of effect that I want to achieve in this part of video, but without After Effects. Now, all that we need is an SRT file. This is an ordinary text file. So, let's navigate to Claude and paste in our prompt. All it says is, "Generate an SRT file for me with numbers counting from 0 to 600. Make each subtitle.1 seconds long and add a dollar sign in front of each." Now, let's go ahead and click send. Once you've completed this, just like with the LUT, click on the file, find the arrow, and select download. Save it to your downloads folder, and then open Cap Cut and drag the SRT file directly onto your timeline. Zooming into the timeline reveals how many small subtitle clips are being created. Now, [music] the great part is you can customize all of these directly in Cap Cut. Then you can adjust the font size, change it, or even modify the color. But you can see an issue. It's way too long for our timeline. So, staying selected on all of them, I'm going to create a compound clip. What this does is it groups all of our subtitles together. In this compound clip, I can then go to speed and let's ramp up the maker speed to make it a lot shorter. Think I'll be going for 10 times shorter. Now, I can reposition that to whatever I want. And if we play that, then you can see that we have this really premium looking numbers counting effect. Usually to make this by hand, it would take about an hour. But we've been able to do it in just 2 minutes. But there's one last bonus trick. If I wanted to hold on to, let's say, 600, if that's the point I'm making in my video, then I need to go ahead and doubleclick into that compound clip to access my subtitle files. And what I'm going to do is drag that individual layer a lot longer. So then I can go back to my compound clip. And let's go ahead and drag it. Now, when it reaches the end of our numbers, you'll see that it pauses for a few seconds at that 600 mark. All right. So far, we've fixed the colors and we've added the counter to our clip. Now, we're entering the territory where After Effects usually eats away all of your RAM, crashes at 99% render, or demands another purchase of Adobe services just to keep working. Everything we've upgraded so far has been relatively easy. But the next three effects, the intro background, the explainer graphics, and the outro map, need heavier tooling. So, let's set them up once and then knock out the rest of this video. [music] Now, in this segment, I'm going to demonstrate how to create more complex and applied motion effects. So, I'll break down how to install them and how to get ready for the generation. For the upcoming steps, we'll need to use Claw Code for handling code or [music] systems files. Now, if you're on the free version, you'll only see the chat option, but if you upgrade to the pro plan at $17 a month, you're going to gain access to co-work. We'll be using Cloud Code for this next set of tricks. Once you have Cloud Code, the next step is installing Remotion, a tool that gives Claude all the knowledge it needs to create stunning motion graphics. But before that, we'll need one extra app, Node.js. So, click the download link that I've left in the description. Select get Node.js. js and install [music] it. This is what your computer needs to run remotion. So next, let's open cloud and paste the phrase npx create video at sign latest. Choose bypass permissions so Claude can automatically install everything it needs without asking you and then simply press enter. Now if a prompt appears as code, just copy it and paste it into the terminal. Since I've already got a project on my computer, it'll show a file path with a complete Remotion template. But on your first install, it's going to ask you to create a folder where all of your Remotion projects will be saved. Now, if you're confused at any point, simply ask Claude, "Hey, I don't get what we're doing right now. Can you please help me install this?" Now, after the installation, type the following and press enter. What this does is installs the additional packages and dependencies that optimize Remotion's performance. What you're going to see is 562 packages installed. Now, with Remotion set up, a wide range of creative possibilities open up. You can truly create anything that you envision. All right, everything is set up. So, let's go ahead and get generating. Now, we're going to start with the intro to our video. Right now, it opens on a plain frame. Let's replace that with a premium motion background. We'll begin by creating some highquality motion backgrounds. First, I went ahead and visited Pinterest, which is a great resource because you can search terms like gradient background or gradient figures to find highquality references. I especially like this one right here. So, let's go ahead and download it as an asset. Then, we'll switch over to Claude. Make sure that again you're using Claude Code. create a new session and drag the image directly into the chat. This lets Claude view the screenshot or image as a reference. Next, we'll paste my motion background prompt into the command bar. If you'd like to access all these prompts, there's a link in the description below that you can use to follow along. Basically, the instruction is to use the motion skill to transform this into an attractive motion background without altering the colors, textures, or the overall appearance. It should look like a premium motion background. Additionally, I requested Claude to rotate the image 90° and set the aspect ratio to 16 by9. This entire project should have a duration of only 10 seconds. What you're going to do, just like we did with our installations, is go to accept edits and say bypass permissions. You don't need to be on Fable 5 since it's super expensive. So, you can go ahead and select lower models. Let me walk you through what this process first does. It's super important to make all the manipulations and to insert all of your references into cloud code, not the regular chat. Now, it's going to show you something like running the skill reotion best practices and it'll state that it's using Remotion. Now, if it doesn't say that, make sure to revisit the session where you installed Remotion and ask Claude. If you followed my steps so far, you should have successfully installed Remotion directly into Claude. There we go. Now that it's finished, after taking a couple of tries, Claude is then going to open your browser to display a preview of the file. I'll take a quick look and we'll see a short full HD video, which you can actually also upgrade to 4K. The blue reference color is going to remain consistent. And scrubbing through quickly, you'll notice that there's been some motion added to the blue glow, resulting [music] in this dynamic motion background. Overall, I like the generation, but I'd like to change the speed of the effect. Right now, I find it to be really slow and a bit dim. So, I'll ask Claude to make the blue gradient move much faster, about three times. Then, I just click enter. Now, the great thing about this process is that there's no need to edit or really to know any code. You simply tell it in any language to Claude and it'll start editing the composition immediately. Now, just in 5 seconds, if we return to the web browser without reloading, you'll notice that that orb is now moving significantly faster than before. Now, in this next segment of our video, the middle part, I'll explain the process step by step. Now, instead of just talking, let's visualize it with animated boxes and drop them right over the footage that we already have graded. That's exactly why we made the background transparent earlier. Now, in this step, we'll look at how to create motion design generations that'll give a direct impact to your viewership if you're working with e-commerce or on a marketing campaign. Just imagine that you need to schematically explain a very complex topic in your video using just blocks. Now, creating such a motion design typically takes around 2 hours at minimum. I'll show you how to do it much faster in just a few minutes. I began by visiting Pinterest and searching for square shaped UI boxes. I found something super aesthetic and good references. So, I downloaded the files that I liked. Next, I created a new session in Cloud Code, fed it the file, and dragged it into the session. Finally, I pasted the prompt that I used to generate that effect, the link for which you can find in the description below. So, let's [music] quickly go through the prompt. This final line should be included in all of your creations. I didn't add it to the motion background initially because we were just starting out, but now I'm always going to end my prompts with this line. Ask me any clarifying questions so that we nail this spot on. Now let's press enter. Let's see what Claude does next. It comprehends the first part of our prompt, but some ambiguity remains about what it's actually going to generate. So here we go. It begins by providing a list of questions using Remotion to guide these questions which we can then answer. So let's go ahead and respond to them. Let's go ahead and stack these [music] vertically. For that, I'm going to say sequential start. So 1 2 3 4 5. They're all going to appear in kind of a staggered order. staggered order. Yes. Yes. Let's do text only. [music] We're going to use this in a horizontal video. If you wanted to use it in a vertical video, you could obviously type 1080 by 1920. I'm going to say hold and then fade at the end. I'm also going to add while they're holding, add some motion to the boxes. Let's clarify the motion that we want. Add some subtle smooth motion to the boxes. That's good. Let's stick with pure black for now. So, now that we've taken the time to answer its questions, you can see that it's taking the time to do some final self- auditing and sanity checks. That's the amazing thing about Claude. It kind of selfch checkcks what it's created. Now, obviously, we do sometimes have to do some manual tweaking. This pop-up that's just shown is now actually really important because what I didn't do is at the bottom left here where it says accept edits. I didn't say bypass permissions. So because of that, Claude is now asking us if it's okay to do things. It wants to check the PNG file that it created. So essentially access that PNG file on our computer. I'm going to go ahead and say always allow. Now just to clarify, if you don't want those pop-ups to happen, then change this from accept edits to bypass permissions. and it's just going to allow Claude to do everything that it needs to do in the background. All right, you can see that it says done, which took about four minutes to create. Now, when we open the browser, you'll notice it's a part of our Remotion project. Let's click play. Wow, [music] the result is even better than my previous tests. I really like the simplicity and the conciseness. The only adjustment I'd suggest is that it feels like it takes a little bit too long to appear. I'll make a few quick tweaks to demonstrate how easy it is to modify things when needed. I already like the current sizing, but for this demo, let's speed everything up by about 10%. I'll also update the font to enter semibold. Now, aside from these three adjustments, the overall look really does appear premium. So, let's go ahead and click enter. If we play our sequence here, we'll see that we've now assembled a 9-second 29 frame composition. So, almost 10 seconds. The font does in fact appear larger and all of the elements are slightly bigger which looks good. But this setup won't work directly in our Cap Cut project because of the black background. So at this point I'll tell Claude, "This looks great. Please make me the background transparent but keep the box's transparency off." Now I'm doing this so that I can download it directly from Remotion and incorporate into our Cap Cut project directly. Now, if you do prefer that black background, that's fine. But what I want to do is overlay it on my footage or on a custom motion background that I created in Claude. So, that's why I'm requesting a transparent background. [music] Now, in 30 seconds, if we jump back to our project, you'll see that we now have a transparent background. Once you're happy with your motion graphic, go ahead and click render. You can save that to your computer and import the file directly into your Cap Cut and create something that looks about like this. And through these examples of the motion background and now this kinds of effects, square shaped motion graphic figures, you have a great understanding of exactly what Claude can do. Honestly, it's mind-blowing. We've got two segments of our video left. In one, I quote an article on screen will highlight the keywords as they're read. And the ending where I mention the trip from LA to New York, that's getting a full map animation. The next feature that we can describe is designed for people who frequently work with large volumes of references such as news bulletins or article news searches. Now, those are just two examples of some wild motion graphics, and I've got two more to show you. One is a highlighting effect and the other is a map animation perfect for travel videos. Now, the beauty of our system lies in the fact that you can also create several parallel projects, so you won't waste extra time implementing and creating effects gradually. Simultaneous or concurrent creation allows me to save an insane amount of time, which in the case of working with After Effects still meant having two separate windows open. The first one is the highlighting effect. So, you'll actually need a screenshot of what you want to highlight. What I did is I just took a screenshot from a news site. I'll paste this prompt now, and I won't read it all, but what's important to note is that I've asked it to highlight specific words from our screenshot. For example, I requested this, this, and this. Now, if your screenshot contains a lot of different words, be sure to specify which ones to highlight. Now, once that's clear, I'll click enter and see the results. So what you're seeing here is because we attached an actual image, Claude needs to then source that image from our computer. So I'm giving it access to the actual file in the web. access to the actual file in the web. [music] [music] Now as we proceed, we'll create the final map animation. I'll start a new session and paste in this prompt. Then I'll change the accept edit setting to bypass permissions as I did in the beginning. Finally, I'll click enter to continue. [music] All right, let's quickly answer those. Create new project 1920x 1080. [music] Yeah, let's do country state borders visible. Follow the line at low altitude. This is going to be whatever you want. And once I've answered those questions, let's go ahead and click enter. Currently, we're running two animation builds simultaneously. The first is our map and the second is the text chat featuring our text highlighting effect. The highlight effect is now complete and generally it looks pretty good. But one thing I noticed is that it appears a bit choppy, which I'll want to fix. So, I'll talk to Claude and tell it the highlight effect looks staggered or choppy. Please make it smooth. Submit. And after 45 seconds, the adjustment is done. Now, returning to your project, you'll now see a smooth highlight that introduces the words as they're read. And lastly, if we go back to Claude and we select our animated map project, you'll see that it says it's complete. We can go ahead and say please open this remote project. [music] And just like that, our map animation is done. Now, the important thing I need to show you when creating this map is an error occurred because Remotion tried to use a Mapbox token that we don't have. I then directed it to use a different open- source map and it successfully created our effect. Since this requires a map, we couldn't render it in the usual way. You'll see here that the motion map rule suggests using GL and this specific code. I instructed it to render it with this code. And after the rendering finished, I located the output file on my computer. This is what it produced. Now, let's make some quick changes to this. I want the map to actually feel colorful. And I want to add a globe effect so it doesn't just look like a flat map. And there we go. Now, if we go to Remotion Studio, we can go ahead and play our video. What we have is an animation out of Los Angeles. And if we swipe all the way over, we'll be in New York. and we have that globe effect with the color on the water. So, we don't need the black and white. Additionally, I plan to use Claw's extensions like Hixfield MCP and apply the Miniax H3 model to add effects to the map. To enhance the beauty of our animation, especially when the dotted line travels from New York City to LA, I suggested designing it to resemble the style of the Civilization game. The model's simplicity is characterized by ultrarecise detailing of various objects which led us to choose a really accurate map design. Now to access the Hixo MCP feature, we just need to enable Claude's extension and request access which can be done through a careful subscription process. To render this, especially when the preview appears a bit spotty, I return to Claude, swipe up to copy the prompt, and then confirm that it's perfect. I'll then paste the prompt onto my computer to generate the image. Now, we'll wait for a moment. And once the rendering is complete, you'll notice that the map is flawlessly rendered and the animations are looking great. Now, just zoom out, swipe across, and voila, our effects are in a designed background. That's crazy. And now, the moment of truth. Here is the video that we started with side by side. Raw footage on the left and on the right graded with the money counter, motion background, animated boxes with highlights, and the map. One video, zero After Effects. Now, here are a few examples of the motion graphics, effects, and other features that you can create with Claude. We began with the free version of Claude, using it to generate a stylish LUT and an SRT file with animated counting numbers. Now later we switched the paid version and combined it with Remotion to produce motion graphics that continue to amaze me. I hope you enjoyed this video. I really enjoyed creating it and experimenting with everything. Thank you so much for watching and I'll see you guys in the next

## Timestamped

`[00:02]` What you just watched, every cut, every
`[00:02]` animation, and every transition was
`[00:04]` created by Claude within Cap Cut in less
`[00:07]` than 20 minutes. So far, there honestly
`[00:10]` hasn't been a single edit or really a
`[00:12]` single thing that this combination
`[00:14]` couldn't handle. But to get it to this
`[00:16]` point, I've spent weeks of trial and
`[00:18]` error and a ton of credits. But that
`[00:21]` way, you won't have to. So, in this
`[00:23]` video, I'm going to tell you everything
`[00:24]` you need to know to create stunning
`[00:25]` videos with color grading, motion
`[00:27]` design, and animation. And the best part
`[00:30]` is that it'll all be done by AI. So,
`[00:33]` here's the plan. I took one raw video
`[00:35]` and by the end of this tutorial, we will
`[00:37]` transform it completely. Every
`[00:39]` improvement goes into a different part
`[00:41]` of the same video. So, watch the before
`[00:44]` and make sure to stick around for the
`[00:45]` after. So, first you'll need to install
`[00:48]` Claude on your computer. And in the
`[00:49]` previous video, we talked about how to
`[00:51]` use one of Claude's features called
`[00:52]` design to create highquality motion
`[00:54]` effects. Today we're going to talk about
`[00:57]` another killer combination of Claude,
`[00:59]` Cap Cut and Claude. So if you don't have
`[01:01]` Claude yet, make sure to go to Claudeai
`[01:03]` and download the app for Mac or PC. If
`[01:06]` you don't have Cap Cut, you'll need to
`[01:08]` do the same. Now, let's jump back to
`[01:11]` Claude. When you log in for the first
`[01:13]` time, it'll likely appear exactly as you
`[01:15]` see on my screen. So, previously when I
`[01:17]` shot this video, we threw together a
`[01:19]` rough edit, and honestly, it looked bad.
`[01:21]` Flat colors, no life in it. Now,
`[01:24]` normally this is where you'd give up or
`[01:25]` you'd hire a colorist, but instead we're
`[01:28]` going to fix the color foundation and
`[01:30]` we're going to do it right inside of
`[01:31]` Clot. So, let's take our single
`[01:33]` timeline, drop the raw footage in, and
`[01:35]` look at the first problem. Now, every
`[01:37]` editor knows the pain of spending hours
`[01:39]` tweaking color wheels just to fix flat
`[01:42]` log footage, only for it to still look
`[01:45]` washed out. This is where we will need
`[01:48]` LUT. LUT is an instruction file that
`[01:51]` tells the program to replace each color
`[01:53]` in the picture with a different one. For
`[01:55]` example, make this shade of blue a
`[01:57]` little warmer, these shadows are
`[01:59]` greenish, the skin is softer, etc. We
`[02:02]` need an LUT, particularly because it's
`[02:05]` the only way to package an entire color
`[02:07]` grade into a single small file that
`[02:10]` Claude can generate from using a text
`[02:12]` prompt or any editor like Cap Cut, which
`[02:14]` can instantly apply it to your footage.
`[02:17]` So all that I need to do is ask, "Please
`[02:19]` generate a clean soft pastel LUT file
`[02:22]` for my YouTube videos. Cinematic and
`[02:25]` clean." Then I just click send. Now
`[02:27]` after generating, Claude gives you a
`[02:29]` summary of the look. Lifted shadows,
`[02:32]` subtle teal and peach split toning,
`[02:34]` reduced saturation, low contrast,
`[02:36]` ultimately a clean studio aesthetic with
`[02:39]` friendly skin tones. Now, if you go a
`[02:41]` bit further, you'll find the actual
`[02:44]` file. Click on it and then find the
`[02:46]` arrow and choose download. Save the file
`[02:49]` to your downloads folder or really any
`[02:51]` preferred location. So let's click save.
`[02:53]` And since I've already generated the
`[02:55]` file, I'm just going to click replace.
`[02:58]` Now in Cap Cut, go to adjustment and
`[03:01]` select LUT. Then click import to find
`[03:04]` and open the cube file. This imports it
`[03:07]` into Cap Cut for your project. Next,
`[03:10]` we'll click the plus icon to add a new
`[03:12]` layer to the timeline, which you can
`[03:13]` extend over your footage. Switching it
`[03:16]` on and off will show the filter applied
`[03:18]` to your footage. Now, I felt like it was
`[03:21]` a bit too intense, so I adjusted the
`[03:24]` selection to about 50%. That looks
`[03:27]` great. Claude's main strength lies in
`[03:28]` its precise adjustment capabilities. For
`[03:31]` instance, I dislike the shadow in this
`[03:33]` design because it clashed with the clean
`[03:35]` look. I requested Claude to create a
`[03:37]` version without the teal, and the
`[03:39]` difference was evident. Now, setting
`[03:41]` this to 50% produced a gentle pastel
`[03:44]` studio vibe. So, that's the entire base
`[03:46]` video graded. Now that the whole
`[03:48]` timeline looks clean, we can start
`[03:50]` layering effects on top of specific
`[03:52]` moments. Now that the color of our video
`[03:55]` looks great, let's take it one step
`[03:57]` further and make it even better by
`[03:59]` adding some visualization. Now, usually
`[04:01]` doing a dynamic counting animation means
`[04:03]` manually placing hundreds of key frames
`[04:05]` in in After Effects or buying a bunch of
`[04:08]` templates that ultimately break your
`[04:10]` project file. Now, the first moment that
`[04:12]` I want to upgrade is right here. The
`[04:14]` part of the video where I talk about
`[04:16]` numbers. A static number on screen is
`[04:18]` boring. So, let's make it count up. For
`[04:21]` example, do you guys remember in the Mr.
`[04:23]` Beast videos when the dollar icon wildly
`[04:25]` spins up? That's the kind of effect that
`[04:27]` I want to achieve in this part of video,
`[04:29]` but without After Effects. Now, all that
`[04:32]` we need is an SRT file. This is an
`[04:34]` ordinary text file. So, let's navigate
`[04:36]` to Claude and paste in our prompt. All
`[04:39]` it says is, "Generate an SRT file for me
`[04:42]` with numbers counting from 0 to 600.
`[04:45]` Make each subtitle.1 seconds long and
`[04:47]` add a dollar sign in front of each."
`[04:50]` Now, let's go ahead and click send. Once
`[04:53]` you've completed this, just like with
`[04:55]` the LUT, click on the file, find the
`[04:57]` arrow, and select download. Save it to
`[05:00]` your downloads folder, and then open Cap
`[05:02]` Cut and drag the SRT file directly onto
`[05:05]` your timeline. Zooming into the timeline
`[05:07]` reveals how many small subtitle clips
`[05:10]` are being created. Now, [music] the
`[05:12]` great part is you can customize all of
`[05:14]` these directly in Cap Cut. Then you can
`[05:16]` adjust the font size, change it, or even
`[05:19]` modify the color. But you can see an
`[05:21]` issue. It's way too long for our
`[05:24]` timeline. So, staying selected on all of
`[05:27]` them, I'm going to create a compound
`[05:28]` clip. What this does is it groups all of
`[05:31]` our subtitles together. In this compound
`[05:33]` clip, I can then go to speed and let's
`[05:36]` ramp up the maker speed to make it a lot
`[05:38]` shorter. Think I'll be going for 10
`[05:41]` times shorter. Now, I can reposition
`[05:43]` that to whatever I want. And if we play
`[05:45]` that, then you can see that we have this
`[05:47]` really premium looking numbers counting
`[05:49]` effect. Usually to make this by hand, it
`[05:52]` would take about an hour. But we've been
`[05:54]` able to do it in just 2 minutes. But
`[05:56]` there's one last bonus trick. If I
`[05:58]` wanted to hold on to, let's say, 600, if
`[06:00]` that's the point I'm making in my video,
`[06:02]` then I need to go ahead and doubleclick
`[06:04]` into that compound clip to access my
`[06:06]` subtitle files. And what I'm going to do
`[06:08]` is drag that individual layer a lot
`[06:11]` longer. So then I can go back to my
`[06:14]` compound clip. And let's go ahead and
`[06:16]` drag it. Now, when it reaches the end of
`[06:18]` our numbers, you'll see that it pauses
`[06:20]` for a few seconds at that 600 mark. All
`[06:23]` right. So far, we've fixed the colors
`[06:25]` and we've added the counter to our clip.
`[06:28]` Now, we're entering the territory where
`[06:30]` After Effects usually eats away all of
`[06:32]` your RAM, crashes at 99% render, or
`[06:35]` demands another purchase of Adobe
`[06:37]` services just to keep working.
`[06:39]` Everything we've upgraded so far has
`[06:41]` been relatively easy. But the next three
`[06:43]` effects, the intro background, the
`[06:46]` explainer graphics, and the outro map,
`[06:49]` need heavier tooling. So, let's set them
`[06:51]` up once and then knock out the rest of
`[06:53]` this video. [music] Now, in this
`[06:54]` segment, I'm going to demonstrate how to
`[06:56]` create more complex and applied motion
`[06:59]` effects. So, I'll break down how to
`[07:01]` install them and how to get ready for
`[07:03]` the generation. For the upcoming steps,
`[07:05]` we'll need to use Claw Code for handling
`[07:08]` code or [music] systems files. Now, if
`[07:11]` you're on the free version, you'll only
`[07:13]` see the chat option, but if you upgrade
`[07:15]` to the pro plan at $17 a month, you're
`[07:17]` going to gain access to co-work.
`[07:20]` We'll be using Cloud Code for this next
`[07:22]` set of tricks. Once you have Cloud Code,
`[07:24]` the next step is installing Remotion, a
`[07:27]` tool that gives Claude all the knowledge
`[07:28]` it needs to create stunning motion
`[07:30]` graphics. But before that, we'll need
`[07:32]` one extra app, Node.js.
`[07:35]` So, click the download link that I've
`[07:37]` left in the description. Select get
`[07:39]` Node.js. js and install [music] it. This
`[07:42]` is what your computer needs to run
`[07:44]` remotion. So next, let's open cloud and
`[07:47]` paste the phrase npx create video at
`[07:51]` sign latest. Choose bypass permissions
`[07:54]` so Claude can automatically install
`[07:55]` everything it needs without asking you
`[07:57]` and then simply press enter. Now if a
`[08:00]` prompt appears as code, just copy it and
`[08:03]` paste it into the terminal. Since I've
`[08:05]` already got a project on my computer,
`[08:07]` it'll show a file path with a complete
`[08:09]` Remotion template. But on your first
`[08:11]` install, it's going to ask you to create
`[08:13]` a folder where all of your Remotion
`[08:15]` projects will be saved. Now, if you're
`[08:17]` confused at any point, simply ask
`[08:19]` Claude, "Hey, I don't get what we're
`[08:21]` doing right now. Can you please help me
`[08:23]` install this?" Now, after the
`[08:26]` installation, type the following and
`[08:28]` press enter. What this does is installs
`[08:31]` the additional packages and dependencies
`[08:33]` that optimize Remotion's performance.
`[08:36]` What you're going to see is 562 packages
`[08:38]` installed. Now, with Remotion set up, a
`[08:42]` wide range of creative possibilities
`[08:44]` open up. You can truly create anything
`[08:46]` that you envision. All right, everything
`[08:49]` is set up. So, let's go ahead and get
`[08:51]` generating. Now, we're going to start
`[08:52]` with the intro to our video. Right now,
`[08:55]` it opens on a plain frame. Let's replace
`[08:58]` that with a premium motion background.
`[09:00]` We'll begin by creating some highquality
`[09:02]` motion backgrounds. First, I went ahead
`[09:05]` and visited Pinterest, which is a great
`[09:07]` resource because you can search terms
`[09:08]` like gradient background or gradient
`[09:10]` figures to find highquality references.
`[09:13]` I especially like this one right here.
`[09:16]` So, let's go ahead and download it as an
`[09:18]` asset. Then, we'll switch over to
`[09:20]` Claude. Make sure that again you're
`[09:23]` using Claude Code. create a new session
`[09:25]` and drag the image directly into the
`[09:28]` chat. This lets Claude view the
`[09:30]` screenshot or image as a reference.
`[09:32]` Next, we'll paste my motion background
`[09:34]` prompt into the command bar. If you'd
`[09:37]` like to access all these prompts,
`[09:38]` there's a link in the description below
`[09:40]` that you can use to follow along.
`[09:42]` Basically, the instruction is to use the
`[09:44]` motion skill to transform this into an
`[09:46]` attractive motion background without
`[09:48]` altering the colors, textures, or the
`[09:51]` overall appearance. It should look like
`[09:53]` a premium motion background.
`[09:55]` Additionally, I requested Claude to
`[09:57]` rotate the image 90° and set the aspect
`[10:00]` ratio to 16 by9. This entire project
`[10:03]` should have a duration of only 10
`[10:05]` seconds. What you're going to do, just
`[10:07]` like we did with our installations, is
`[10:09]` go to accept edits and say bypass
`[10:12]` permissions. You don't need to be on
`[10:14]` Fable 5 since it's super expensive. So,
`[10:16]` you can go ahead and select lower
`[10:18]` models. Let me walk you through what
`[10:20]` this process first does. It's super
`[10:22]` important to make all the manipulations
`[10:23]` and to insert all of your references
`[10:25]` into cloud code, not the regular chat.
`[10:28]` Now, it's going to show you something
`[10:29]` like running the skill reotion best
`[10:31]` practices and it'll state that it's
`[10:33]` using Remotion. Now, if it doesn't say
`[10:35]` that, make sure to revisit the session
`[10:37]` where you installed Remotion and ask
`[10:39]` Claude. If you followed my steps so far,
`[10:42]` you should have successfully installed
`[10:43]` Remotion directly into Claude. There we
`[10:46]` go. Now that it's finished, after taking
`[10:48]` a couple of tries, Claude is then going
`[10:50]` to open your browser to display a
`[10:52]` preview of the file. I'll take a quick
`[10:54]` look and we'll see a short full HD
`[10:56]` video, which you can actually also
`[10:58]` upgrade to 4K. The blue reference color
`[11:01]` is going to remain consistent. And
`[11:03]` scrubbing through quickly, you'll notice
`[11:05]` that there's been some motion added to
`[11:06]` the blue glow, resulting [music] in this
`[11:09]` dynamic motion background. Overall, I
`[11:11]` like the generation, but I'd like to
`[11:13]` change the speed of the effect. Right
`[11:15]` now, I find it to be really slow and a
`[11:17]` bit dim. So, I'll ask Claude to make the
`[11:19]` blue gradient move much faster, about
`[11:21]` three times. Then, I just click enter.
`[11:24]` Now, the great thing about this process
`[11:26]` is that there's no need to edit or
`[11:28]` really to know any code. You simply tell
`[11:30]` it in any language to Claude and it'll
`[11:33]` start editing the composition
`[11:34]` immediately. Now, just in 5 seconds, if
`[11:37]` we return to the web browser without
`[11:39]` reloading, you'll notice that that orb
`[11:41]` is now moving significantly faster than
`[11:43]` before. Now, in this next segment of our
`[11:45]` video, the middle part, I'll explain the
`[11:48]` process step by step. Now, instead of
`[11:50]` just talking, let's visualize it with
`[11:52]` animated boxes and drop them right over
`[11:55]` the footage that we already have graded.
`[11:57]` That's exactly why we made the
`[11:59]` background transparent earlier. Now, in
`[12:02]` this step, we'll look at how to create
`[12:03]` motion design generations that'll give a
`[12:06]` direct impact to your viewership if
`[12:08]` you're working with e-commerce or on a
`[12:10]` marketing campaign. Just imagine that
`[12:13]` you need to schematically explain a very
`[12:15]` complex topic in your video using just
`[12:18]` blocks. Now, creating such a motion
`[12:20]` design typically takes around 2 hours at
`[12:23]` minimum. I'll show you how to do it much
`[12:25]` faster in just a few minutes. I began by
`[12:28]` visiting Pinterest and searching for
`[12:30]` square shaped UI boxes. I found
`[12:32]` something super aesthetic and good
`[12:34]` references. So, I downloaded the files
`[12:36]` that I liked. Next, I created a new
`[12:38]` session in Cloud Code, fed it the file,
`[12:40]` and dragged it into the session.
`[12:42]` Finally, I pasted the prompt that I used
`[12:44]` to generate that effect, the link for
`[12:46]` which you can find in the description
`[12:47]` below. So, let's [music] quickly go
`[12:49]` through the prompt. This final line
`[12:51]` should be included in all of your
`[12:53]` creations. I didn't add it to the motion
`[12:55]` background initially because we were
`[12:57]` just starting out, but now I'm always
`[12:59]` going to end my prompts with this line.
`[13:01]` Ask me any clarifying questions so that
`[13:03]` we nail this spot on. Now let's press
`[13:06]` enter. Let's see what Claude does next.
`[13:09]` It comprehends the first part of our
`[13:11]` prompt, but some ambiguity remains about
`[13:13]` what it's actually going to generate. So
`[13:15]` here we go. It begins by providing a
`[13:17]` list of questions using Remotion to
`[13:20]` guide these questions which we can then
`[13:22]` answer. So let's go ahead and respond to
`[13:24]` them. Let's go ahead and stack these
`[13:26]` [music] vertically. For that, I'm going
`[13:29]` to say sequential start. So 1 2 3 4 5.
`[13:33]` They're all going to appear in kind of a
`[13:35]` staggered order.
`[13:37]` staggered order. Yes.
`[13:40]` Yes.
`[13:40]` Let's do text only. [music]
`[13:43]` We're going to use this in a horizontal
`[13:44]` video. If you wanted to use it in a
`[13:46]` vertical video, you could obviously type
`[13:48]` 1080 by 1920. I'm going to say hold and
`[13:51]` then fade at the end. I'm also going to
`[13:54]` add while they're holding, add some
`[13:56]` motion to the boxes. Let's clarify the
`[13:58]` motion that we want. Add some subtle
`[14:01]` smooth motion to the boxes. That's good.
`[14:04]` Let's stick with pure black for now. So,
`[14:07]` now that we've taken the time to answer
`[14:08]` its questions, you can see that it's
`[14:10]` taking the time to do some final self-
`[14:12]` auditing and sanity checks. That's the
`[14:15]` amazing thing about Claude. It kind of
`[14:17]` selfch checkcks what it's created. Now,
`[14:19]` obviously, we do sometimes have to do
`[14:22]` some manual tweaking. This pop-up that's
`[14:24]` just shown is now actually really
`[14:26]` important because what I didn't do is at
`[14:28]` the bottom left here where it says
`[14:30]` accept edits. I didn't say bypass
`[14:32]` permissions. So because of that, Claude
`[14:34]` is now asking us if it's okay to do
`[14:36]` things. It wants to check the PNG file
`[14:38]` that it created. So essentially access
`[14:41]` that PNG file on our computer. I'm going
`[14:43]` to go ahead and say always allow. Now
`[14:46]` just to clarify, if you don't want those
`[14:48]` pop-ups to happen, then change this from
`[14:50]` accept edits to bypass permissions. and
`[14:52]` it's just going to allow Claude to do
`[14:54]` everything that it needs to do in the
`[14:56]` background. All right, you can see that
`[14:58]` it says done, which took about four
`[15:00]` minutes to create. Now, when we open the
`[15:02]` browser, you'll notice it's a part of
`[15:04]` our Remotion project. Let's click play.
`[15:08]` Wow, [music]
`[15:09]` the result is even better than my
`[15:11]` previous tests. I really like the
`[15:13]` simplicity and the conciseness. The only
`[15:16]` adjustment I'd suggest is that it feels
`[15:18]` like it takes a little bit too long to
`[15:20]` appear. I'll make a few quick tweaks to
`[15:23]` demonstrate how easy it is to modify
`[15:25]` things when needed. I already like the
`[15:27]` current sizing, but for this demo, let's
`[15:29]` speed everything up by about 10%. I'll
`[15:32]` also update the font to enter semibold.
`[15:35]` Now, aside from these three adjustments,
`[15:37]` the overall look really does appear
`[15:39]` premium. So, let's go ahead and click
`[15:41]` enter. If we play our sequence here,
`[15:44]` we'll see that we've now assembled a
`[15:46]` 9-second 29 frame composition. So,
`[15:49]` almost 10 seconds. The font does in fact
`[15:51]` appear larger and all of the elements
`[15:53]` are slightly bigger which looks good.
`[15:56]` But this setup won't work directly in
`[15:57]` our Cap Cut project because of the black
`[16:00]` background. So at this point I'll tell
`[16:02]` Claude, "This looks great. Please make
`[16:04]` me the background transparent but keep
`[16:07]` the box's transparency off." Now I'm
`[16:10]` doing this so that I can download it
`[16:11]` directly from Remotion and incorporate
`[16:14]` into our Cap Cut project directly. Now,
`[16:17]` if you do prefer that black background,
`[16:19]` that's fine. But what I want to do is
`[16:21]` overlay it on my footage or on a custom
`[16:23]` motion background that I created in
`[16:25]` Claude. So, that's why I'm requesting a
`[16:27]` transparent background. [music]
`[16:29]` Now, in 30 seconds, if we jump back to
`[16:32]` our project, you'll see that we now have
`[16:34]` a transparent background. Once you're
`[16:36]` happy with your motion graphic, go ahead
`[16:38]` and click render. You can save that to
`[16:40]` your computer and import the file
`[16:42]` directly into your Cap Cut and create
`[16:44]` something that looks about like this.
`[16:47]` And through these examples of the motion
`[16:48]` background and now this kinds of
`[16:50]` effects, square shaped motion graphic
`[16:52]` figures, you have a great understanding
`[16:55]` of exactly what Claude can do. Honestly,
`[16:58]` it's mind-blowing. We've got two
`[16:59]` segments of our video left. In one, I
`[17:02]` quote an article on screen will
`[17:03]` highlight the keywords as they're read.
`[17:06]` And the ending where I mention the trip
`[17:08]` from LA to New York, that's getting a
`[17:10]` full map animation. The next feature
`[17:13]` that we can describe is designed for
`[17:15]` people who frequently work with large
`[17:17]` volumes of references such as news
`[17:19]` bulletins or article news searches. Now,
`[17:22]` those are just two examples of some wild
`[17:24]` motion graphics, and I've got two more
`[17:27]` to show you. One is a highlighting
`[17:29]` effect and the other is a map animation
`[17:31]` perfect for travel videos. Now, the
`[17:34]` beauty of our system lies in the fact
`[17:36]` that you can also create several
`[17:38]` parallel projects, so you won't waste
`[17:40]` extra time implementing and creating
`[17:42]` effects gradually. Simultaneous or
`[17:45]` concurrent creation allows me to save an
`[17:47]` insane amount of time, which in the case
`[17:49]` of working with After Effects still
`[17:52]` meant having two separate windows open.
`[17:54]` The first one is the highlighting
`[17:56]` effect. So, you'll actually need a
`[17:58]` screenshot of what you want to
`[17:59]` highlight. What I did is I just took a
`[18:01]` screenshot from a news site. I'll paste
`[18:03]` this prompt now, and I won't read it
`[18:05]` all, but what's important to note is
`[18:06]` that I've asked it to highlight specific
`[18:08]` words from our screenshot. For example,
`[18:10]` I requested this, this, and this. Now,
`[18:13]` if your screenshot contains a lot of
`[18:15]` different words, be sure to specify
`[18:18]` which ones to highlight. Now, once
`[18:20]` that's clear, I'll click enter and see
`[18:22]` the results. So what you're seeing here
`[18:24]` is because we attached an actual image,
`[18:27]` Claude needs to then source that image
`[18:29]` from our computer. So I'm giving it
`[18:31]` access to the actual file in the web.
`[18:33]` access to the actual file in the web. [music]
`[18:34]` [music]
`[18:34]` Now as we proceed, we'll create the
`[18:36]` final map animation. I'll start a new
`[18:38]` session and paste in this prompt. Then
`[18:41]` I'll change the accept edit setting to
`[18:43]` bypass permissions as I did in the
`[18:45]` beginning. Finally, I'll click enter to
`[18:47]` continue. [music]
`[18:49]` All right, let's quickly answer those.
`[18:51]` Create new project 1920x 1080. [music]
`[18:55]` Yeah, let's do country state borders
`[18:58]` visible. Follow the line at low
`[18:59]` altitude. This is going to be whatever
`[19:01]` you want. And once I've answered those
`[19:03]` questions, let's go ahead and click
`[19:05]` enter. Currently, we're running two
`[19:07]` animation builds simultaneously. The
`[19:09]` first is our map and the second is the
`[19:11]` text chat featuring our text
`[19:13]` highlighting effect. The highlight
`[19:15]` effect is now complete and generally it
`[19:16]` looks pretty good. But one thing I
`[19:18]` noticed is that it appears a bit choppy,
`[19:20]` which I'll want to fix. So, I'll talk to
`[19:22]` Claude and tell it the highlight effect
`[19:24]` looks staggered or choppy. Please make
`[19:26]` it smooth. Submit. And after 45 seconds,
`[19:29]` the adjustment is done. Now, returning
`[19:32]` to your project, you'll now see a smooth
`[19:34]` highlight that introduces the words as
`[19:37]` they're read. And lastly, if we go back
`[19:39]` to Claude and we select our animated map
`[19:42]` project, you'll see that it says it's
`[19:44]` complete. We can go ahead and say please
`[19:46]` open this remote project. [music] And
`[19:48]` just like that, our map animation is
`[19:51]` done. Now, the important thing I need to
`[19:52]` show you when creating this map is an
`[19:54]` error occurred because Remotion tried to
`[19:57]` use a Mapbox token that we don't have. I
`[20:00]` then directed it to use a different
`[20:01]` open- source map and it successfully
`[20:03]` created our effect. Since this requires
`[20:06]` a map, we couldn't render it in the
`[20:08]` usual way. You'll see here that the
`[20:10]` motion map rule suggests using GL and
`[20:12]` this specific code. I instructed it to
`[20:14]` render it with this code. And after the
`[20:16]` rendering finished, I located the output
`[20:18]` file on my computer. This is what it
`[20:21]` produced. Now, let's make some quick
`[20:23]` changes to this. I want the map to
`[20:25]` actually feel colorful. And I want to
`[20:27]` add a globe effect so it doesn't just
`[20:29]` look like a flat map. And there we go.
`[20:32]` Now, if we go to Remotion Studio, we can
`[20:34]` go ahead and play our video. What we
`[20:36]` have is an animation out of Los Angeles.
`[20:39]` And if we swipe all the way over, we'll
`[20:41]` be in New York. and we have that globe
`[20:43]` effect with the color on the water. So,
`[20:45]` we don't need the black and white.
`[20:47]` Additionally, I plan to use Claw's
`[20:49]` extensions like Hixfield MCP and apply
`[20:52]` the Miniax H3 model to add effects to
`[20:54]` the map. To enhance the beauty of our
`[20:56]` animation, especially when the dotted
`[20:59]` line travels from New York City to LA, I
`[21:01]` suggested designing it to resemble the
`[21:03]` style of the Civilization game. The
`[21:06]` model's simplicity is characterized by
`[21:08]` ultrarecise detailing of various objects
`[21:11]` which led us to choose a really accurate
`[21:13]` map design. Now to access the Hixo MCP
`[21:16]` feature, we just need to enable Claude's
`[21:18]` extension and request access which can
`[21:20]` be done through a careful subscription
`[21:22]` process. To render this, especially when
`[21:24]` the preview appears a bit spotty, I
`[21:26]` return to Claude, swipe up to copy the
`[21:28]` prompt, and then confirm that it's
`[21:30]` perfect. I'll then paste the prompt onto
`[21:33]` my computer to generate the image. Now,
`[21:35]` we'll wait for a moment. And once the
`[21:37]` rendering is complete, you'll notice
`[21:39]` that the map is flawlessly rendered and
`[21:41]` the animations are looking great. Now,
`[21:44]` just zoom out, swipe across, and voila,
`[21:47]` our effects are in a designed
`[21:49]` background. That's crazy. And now, the
`[21:52]` moment of truth. Here is the video that
`[21:54]` we started with side by side. Raw
`[21:56]` footage on the left and on the right
`[21:59]` graded with the money counter, motion
`[22:01]` background, animated boxes with
`[22:03]` highlights, and the map. One video, zero
`[22:07]` After Effects. Now, here are a few
`[22:09]` examples of the motion graphics,
`[22:11]` effects, and other features that you can
`[22:13]` create with Claude. We began with the
`[22:15]` free version of Claude, using it to
`[22:17]` generate a stylish LUT and an SRT file
`[22:20]` with animated counting numbers. Now
`[22:22]` later we switched the paid version and
`[22:25]` combined it with Remotion to produce
`[22:27]` motion graphics that continue to amaze
`[22:29]` me. I hope you enjoyed this video. I
`[22:32]` really enjoyed creating it and
`[22:33]` experimenting with everything. Thank you
`[22:35]` so much for watching and I'll see you
`[22:37]` guys in the next
