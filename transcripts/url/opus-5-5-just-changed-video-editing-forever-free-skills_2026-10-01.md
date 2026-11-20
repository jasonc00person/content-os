# Opus 5.5 Just Changed Video Editing Forever (free skills)

- **Source:** https://www.youtube.com/watch?v=7jHXoPGnA4c
- **Uploader:** Nate Herk | AI Automation
- **Uploaded:** 2026-09-25
- **Duration:** 19:22
- **Detected language:** en (p=1.00)
- **Model:** small.en

## Transcript

So I've been experimenting with AI models, editing videos for me for a long time. Super powerful models like Fable 5.1 and GBB 6 Astra. But Opus 5.5 is giving me some of the best outputs ever. Take a look at this example, which was just one prompt. Not only does this thing do the motion design and the sound design, but it also will go out and it will grab the B-roll and it will grab screenshots or even generate images and videos for you if it needs it. It has amazing taste and it does good with verification. So today I'm just going to talk about how you actually get this set up because all you have to do is use your natural language. And yes, of course, that entire intro that you just watched was edited with Opus 5.5. This is the actual video. As you can see, all of these motion graphics that it did were created right inside of here, inside of Claude. And what's cool about this is I specified a lot of things that I wanted, but it got really creative here. And that's one of the things about Opus 5.5 is that it has amazing, amazing taste. So let me show you what I actually said in this prompt. So I gave it the original video and I said that I need you to edit this to be super engaging and clean with Hyperframes, which is the actual tool that we're using here. It's completely free and we give Claude code this tool and it basically writes HTML and animates it. So if you need to get set up with Hyperframes and just go to Google, type Hyperframes, you can go to the website here, but ultimately you're just going to want to go to this GitHub repo for Hyperframes. And then you just need to literally copy this link, the URL, give it to Claude code and say, hey, set up Hyperframes so that we can use it to animate videos. That's it. And then on top of that, I have this free repo called Hyperframes Student Kit. And in here, it has all of the skills and examples that I actually have done with my pipeline of editing videos. And if you want to get this, you can go to my free school community, the link for that is down in the description. In here, you go to classroom and you can click on all YouTube resources, or you can go to AI skills and you can access that Hyperframes Student Kit. Anyways, I said the first step is for you to transcribe the video so you can make sure that motion graphics and animations come in at the exact perfect time. So it has to transcribe the video. You can do that using something like 11Labs API, or you can do that with something like Whisper, which is more of a local model that can run and transcribe videos, but 11Labs is a little bit quicker. So 11Labs you pay per usage and Whisper is gonna be free, but it's just a little slower. So you can use either one, and it's really simple to get that set up. You just ask Cloud Code to help you set that up. I said, then you will build the animations based on my instructions. When I say powerful models like Fable 5.1 and GBD6 Astra, I want you to have animations come in where I'm pointing. So that was basically right here where I point and I have Fable 5.1 come in right over here, and then I have GBD6 Astra come over here. And I told it that I wanted to have a Cloud logo and I wanted to have an OpenAI logo. I wanted it to be animated. That's basically all I said, besides also saying, make sure there's some sort of liquid glass card behind the element as it's animated, otherwise it will be hard to see. And as you saw right here, we got liquid glass right behind it so that we could actually read the text and see the logo. So that was me using natural language as you see. Then I said, when I say best outputs ever, I want you to have all three of those words at the bottom and highlight them. And so that's what it did right down here. Opus 5.5, best outputs ever. And you'll notice that it also put a little bit of an overlay under this text because once again, it wanted to make sure that we could actually read it. So very, very well done there. Then I said, for the rest of the video, when I'm talking about B roll and screenshots and generating images and videos, I want you to have things come in on the left and right side of the screen. Once again, they should have some sort of overlay. And I want you to actually go off and get a B roll screen recording and get a screenshot and pull in stuff because I want you to prove to the viewers that you're able to do all of this. The whole point is that I'm explaining what Opus is capable of when it comes to animating and editing videos and I want you to prove it in real time. Now that is basically my entire prompt. And what's so cool about that is that it goes off and it does it, but it also puts its own spin on things. Like you'll notice at the very beginning, it's doing this very subtle zoom in effect. I didn't ask for that, but it just kind of knew to do that to make it more engaging. I didn't ask for this either when I said the one prompt thing right there, it just did that by itself with a super cool, cloud-looking interface. I didn't ask for this either, but I absolutely love it. And then you'll see what it interpreted when I said get the screen recording, get the screenshot, generate an image, generate video. It did all of that on its own, amazing taste, the verification. I thought this was a super clean animation right here. The verification with like screenshots and checking, you guys will notice in my prompt, I didn't actually ask for that at all. It just did it because it thought that it would make the intro more engaging. And I would argue that it definitely did. And now you can see that's all I said. I didn't ask another prompt. And what we got was that exact video right back here with all of these things that we just saw. Now let's break down that other example that you guys saw inside of the actual intro itself. This little YouTube show reel, which I was super, super impressed by. This was also a one-shot prompt, like I said. Really, really impressive. There's so many things that wanted to play here. It had to go get screenshots of so many of my thumbnails. And then it zoomed in on the thank you one, which I think was amazing reasoning. It literally said, okay, this is Nate holding up the play button saying thank you. This is the one that we're gonna put in the center. And this is the one that we're gonna zoom in on, because I think that highlights the branding and the culture of YouTube, which was just insane. So anyways, it generated all of this stuff and the sound and the music, all of that, right? Now here's what I did in this example. What's important is that you're clear on what you want. And you'll notice in the previous version, I was like speaking very emotionally. And that's what's cool about it is sometimes you don't always know exactly what you want, but you know the emotions you want the video to create inside of you, right? So what I did is I downloaded an example that I saw on X. I saw this example from Ken, amazing output here using hyperframes and using Opus. And you'll notice there's a lot of similarities with this reel and the one that we just looked at with YouTube. So basically what I did is I used this as inspiration. I downloaded this video. I then came into Cloud Code and I gave it to Cloud Code. And I said, analyze this video, which was created by Opus 5.5 and figure out why this is so good. So I liked this video and I wanted to do something similar and I had Cloud Code figure out what that is. I had Opus figure out why it's so good. And then I said, turn that into a skill. So now we have this skill called motion reel or something. And I'm gonna give that to you guys for free, just a sec. And then I said, okay, use that skill, create me my own show reel about YouTube. I said, collect B-roll images, any assets you need, make sure the whole thing feels branded to YouTube, typography, design, language, colors, branding, all that type of stuff that makes YouTube YouTube should be unmistakable in this show reel. And now we have our output. You can see here, I wrote this skill called motion show reel. So if I go into my files real quick and I go to the skills and we go all the way down to the M's, we go to the motion show reel. We now have this motion show reel skill with all of this information like about how we actually design reels like this. So I'm going to put this inside of my free school community once again. So if you guys want it, hop into my free school community and you can grab it in the YouTube resources or inside of the AI skills, it'll be in there. And now you can do reels just like that. What you'll also notice is that it had to go generate these images. So you can see it created these images and then it sent them to cling in order to turn those images into videos. And that's how we actually got these animations inside of the video right about here where we see the actual play button sort of being animated. These two scenes were because it created an image and then it created a video and then it sent it back to Claude and then Opus took all that stuff and put it into one consistent video. Now here's another show reel style video but this one didn't use that skill that we built at all. And just to show you how cool stuff can be made even with a show reel. So I said, make a dynamic 15 second motion graphics video that shows what an incredible motion designer you are like it's your show reel for a resume, go all out. I actually saw this from someone on X, they made a demo and they said this is what they prompted it with so I tried it out. I said, make it about our company, AIS, use real assets and logos from our products when possible. You can also use key.ai to generate any assets you need and use hyper frames or any other tools for motion design and music and sound effects. And with one shot prompts, this is what we got back right here. So let's take a look. You can see the similarities at the beginning with the little bead that like drops and there's sound effects. But then with the motion graphics, with the color schemes, with the same sort of like spatial awareness of doing things like this, I thought was so cool. It pulled pictures from our website. It knew how many members we had. It had this 3D sort of image which I think was an image that was generated and then it was turned into a video similar to that YouTube show reel. Anyways, this background image is from our website as well. So just very, very well done. Real quick guys, I've got this completely free website design skill that I'm giving away. I use this for every single website that I build including our AI Automation Society site which I think is pretty slick and I absolutely love this website. It's called Scrollcraft and it understands things like scroll-driven animations and layering, but also it has things in there like taste, typography, spacing, depth. It's just a really good website design skill in general and it's completely free. So the link for this will be down in the description, but let's get back to the video. Now, let me show you guys, this is one of my new favorite benchmarks. I basically give Cloud Code access to a folder which has 105 gigabytes of YouTube videos, or sorry, not YouTube videos, videos and recordings and resources from our event, AIS Live. And then I say, hey, look through all this and create me a sizzle reel. Tell a story out of this and look what I got here. Now, this wasn't a one-shot prompt. This was one prompt and then me giving one round of iteration and then having it fix one thing. So technically three prompts. That's why it is V2.1, but let's take a look at this output right here. Hello, hello, AIS Live. I'm so, so pumped. It was electric. Let's go. Never even opened VS Code. Signed the deal. The chat's going crazy. Trippie. Fantastic event. This was amazing. Such a fun two days. I literally like logged off yesterday just buzzing. I had goosebumps. Can't wait for the next one. I mean, do you guys have any idea of how complicated that process is just to tell a story out of an event when you just are given a folder of resources? And of course it's marketing for our next one, which is actually real coming up October 17th and 18th. So mark your calendars if you guys wanna show up. More details will be in the description. But I know there were a few things that weren't great. There were some times where there was like an awkward cut of the speech and a few things that we could tweak. But look at this. Look how it made like this tunnel of all the screens. Look at the beginning, how it was zooming in on different screens. Like it was really aware of the spacing and this is just really, really cool. It was also pulling out specific moments in the transcripts of these calls that were showing kind of like the vibe and the energy within the live event. This is my favorite scene here at the end where it has all of these scenes come together and it forms the actual AS Live logo even with the little red dot. And then it zooms in on the red dot and it says, your seat is in the middle. I just thought that the way that it was able to actually bring all of this to life is really, really impressive to me. Now I also wanted to show you guys what else is possible. Like a lot of times it's about thinking of the use case. So I recorded this really simple video of me explaining how to make avocado toast. And I perfected that by the way. My avocado toast is so good. But anyways, I just wanted to show you, I did three different edits with this avocado toast video. This one I said, hey, I want you to edit this using hyperframes. I'm looking for a simple and clean whiteboard, hand-drawn style animation. And it's really simple as if you're trying to explain to a kid how to make avocado toast, simple graphics, simple animations, easy to understand. If you need to generate any images or sorry, assets like images or videos, you can use key.ai. I then said that some scenes should be a full screen whiteboard takeover. And some scenes should just be the left half as the whiteboard and the right half is my face. So it then went ahead and started generating things. It started reasoning, it started testing things out. And now we have this output which I'll go ahead and play right now. All right, so here's how I make avocado toast. When you put the toast in the toaster, when you're letting it sit, you don't set it flat on the plate because then that bottom side gets a little soggy. You want that both sides to be crispy. Then you put the eggs on the pan, you mash up the avocado, you spread the avocado on the crispy bread. I put like everything bagel seasoning on the avocado mash and then I do some balsamic vinegar. And then you put the eggs on top of the toast and that's how it's done. Now my main critique here is that the eggs are super tiny and the balsamic glaze is only on one little piece of the toast. So that wouldn't taste as good as if it was everywhere. But anyways, look how good this was able to in one prompt just animate the stuff in a very simple and engaging way. It's hand-drawn, it is, like I said, it's kind of friendly and playful as if you wanted to show a kid. But this was literally just one prompt and it took care of everything. Now, when I first really started using AI to edit videos, it was for course style videos, things that were super easy. We just wanted them animated with like bullet points and super simple images and graphics. So here's what I did in this one. I need you to edit a course style video for me using hyperframes. My camera will start off full screen and then I want it to be a rounded crop. The background's gonna be super simple, super minimalistic and the style I'm looking for is just bullet points with important takeaways, not too wordy and they should be big. And then visual aids should just be AI generated images, very simple, very light motion graphics to help illustrate concepts. And here is what we got. This was once again, a one-shot prompt. Oh wait, that was just an image. It was just doing verification. Here we go. All right, so here's how I make avocado toast. When you put the toast in the toaster, when you're letting it sit, you don't set it flat on the plate because then that bottom side gets a little soggy. You want both sides to be crispy. Then you put the eggs on the pan, you mash up the avocado, you spread the avocado on the crispy bread. I put everything bagel seasoning on the avocado mash and then I do some balsamic vinegar and then you put the eggs on top of the toast and that's how it's done. So all of the images and videos in this video were AI generated. All of this was AI generated and you can see that it's gonna save you so much time because it can go get B-roll, it can take screenshots, it can generate things if you need it to. It's just really cool because now you can film content and editing doesn't have to be the bottleneck anymore, especially when you start to build skills around stuff like your preferences and motion styles and all that kind of stuff, your brand guidelines. And then the last one I did here was kind of a short form video and this was using hyperframes once again. And you'll notice that I'm not really having this leverage other skills. So I wanted to show you how easy it is to do a one-shot prompts with Obas 5.5. Pretty much all these examples I've been running on high by the way, high meaning the effort level. And I just said basically this, generate the assets you need, have it be engaging, have it be fast paced, easy to understand. So let's see what we got down here for this short. Here's how I make avocado toast. When you put the toast in the toaster, when you're letting it sit, you don't set it flat on the plate because then that bottom side gets a little sog. You want that both sides to be crispy. Then you put the eggs on the pan, you mash up the avocado, you spread the avocado on the crispy bread. I put like everything bagel seasoning on the avocado mash and then I do some balsamic vinegar. And then you put the eggs on top of the toast and that's how it's done. I mean, it's not perfect, right? But a one-shot prompt and it's just, it's really cool that it's able to switch between these different scenes. It definitely keeps my attention because we have all this different sorts of B-roll going on in the background. It is just a really, really decent output when you consider what this would have taken for a human to do it for you. And now one-shot prompt, you iterate, you iterate, you build skills. And I wanted to show you guys one more example with Lululemon because this is like a physical tangible product. Look how good it did at making this video feel like Lululemon. So if you guys think about what it actually had to do there, all of these videos were obviously AI generated. But what I'm pretty sure it did is it went to Lululemon and it found all these actual pieces of clothing. It found them, it took pictures of the actual model here and then generated videos of them running or jumping or whatever it is in the clothes. And then of course it brings it all together here with actual catalog images. It's just really cool to think about how many little pieces would have had to go into this if you were editing this or creating this as a human. But really as a human, all I did was I told it what I wanted and sort of the emotional feeling I wanted it to carry throughout. The vibe, high energy, fast paced, engaging, sync the music to the beats, sound effects, things like that. So I just wanted to talk about the five things that I'm constantly thinking about when I'm actually editing videos with AI. I'm just gonna run through these super simply because you just, you could basically give the transcript of this section to your AI agent and it would be fine. So the first piece is to transcribe. If you're starting off with a clip and you need it to be edited like a video or a course or whatever it is, you obviously want to transcribe first so that the beats can come in at the right time and so that the AI knows how to tell a story out of it. Transcribe is essential whether you wanna use Whisper or 11 Labs or some other tool, transcribing is essential. From there, you're going to have it cut things out. So if it's mistakes, cut out the mistakes. If it notices in the transcript that there's like 20 seconds of dead space, cut out the dead space, things like that. You're cutting things up. And a lot of times I'll use AI just to literally cut out mistakes and then I'll take the clip and do whatever I want with it, but it's able to just clean out your content so much quicker than you could because you'd be in the editor looking for the dead space and then, you know, snipping everything out. And then number three is to plan the beats. A lot of times from there, what I like to do is I like to be very specific about what it is that I want. As you guys saw in this intro version, the intro for this video, I was basically just planning out what I wanted. Now, obviously it went off the cuff a little bit and it was creative, but if I would have said like, these are the only beats I want you to actually create nothing else, it would have done that, but I let it be creative here. But I basically said, hey, at this point, I want this to come in. I want this to come in. I want this to come in. And the better you can set expectations of what you're looking for and what you would consider good, obviously the better or not better, but the more aligned your output is going to be. Number four is to use skills. So build skills around things. If you build a lot of reels, then build skills around reels. Use my Hyperframe student kit. Use resources and use inspiration. Like you guys saw me do, I took a video that I really liked and I told it to build a skill. Now, guess what? Every time I run that skill, I will look at the output and say, hey, in this version, I really liked this and I really didn't like this. Update the skill with that information, run it again, and then I'll give you more feedback. And that way you're actually building a reusable component where every single time you run the skill, it's getting better and you're able to just move faster and faster. You don't wanna have to repeat yourself every time. If you ever find yourself repeating something, just throw it in the skill. And then the fifth one, probably the most important one, is the verification loop. You'll notice how as it's going through a lot of my videos, it's taking screenshots and looking at them and then making iterations. And that's how you get in that loop where you're not just basically saying, okay, here is my output number one. You're getting output number like five or six because the agent basically did this. It delivered output one and then it watched it. It realized there was some mistakes and then it came back and it delivered output two. And then it watched output two and then it kept iterating on its outputs until it realized, okay, this one is finally good enough where I'm gonna give it to Nate and here you go, Nate, this is the finished video. So now you're getting something that has already been checked by the AI and iterated on, then compared to if it just handed you this first version and then you're frustrated and you have to make all these prompts. But anyways, guys, there are so many use cases when it comes to using AI to help you edit things or add motion design because it's not really something that you had to have previous video editing experience in order to take advantage of now. So don't let editing be your bottleneck, but that's gonna do it for today. If you enjoyed or you learned something new, please give it a like, it helps me out a ton. And as always, I appreciate you guys making it to the end of the video. I'll see you all in the next one. Thanks everyone.

## Timestamped

`[00:00]` So I've been experimenting with AI models, editing videos for me for a long time.
`[00:03]` Super powerful models like Fable 5.1 and GBB 6 Astra.
`[00:07]` But Opus 5.5 is giving me some of the best outputs ever.
`[00:10]` Take a look at this example, which was just one prompt.
`[00:27]` Not only does this thing do the motion design and the sound design,
`[00:30]` but it also will go out and it will grab the B-roll and it will grab screenshots
`[00:33]` or even generate images and videos for you if it needs it.
`[00:36]` It has amazing taste and it does good with verification.
`[00:39]` So today I'm just going to talk about how you actually get this set up
`[00:41]` because all you have to do is use your natural language.
`[00:43]` And yes, of course, that entire intro that you just watched was edited with Opus 5.5.
`[00:48]` This is the actual video.
`[00:48]` As you can see, all of these motion graphics that it did
`[00:51]` were created right inside of here, inside of Claude.
`[00:53]` And what's cool about this is I specified a lot of things that I wanted,
`[00:56]` but it got really creative here.
`[00:58]` And that's one of the things about Opus 5.5 is that it has amazing, amazing taste.
`[01:02]` So let me show you what I actually said in this prompt.
`[01:04]` So I gave it the original video and I said that I need you to edit this
`[01:07]` to be super engaging and clean with Hyperframes,
`[01:09]` which is the actual tool that we're using here.
`[01:12]` It's completely free and we give Claude code this tool
`[01:14]` and it basically writes HTML and animates it.
`[01:16]` So if you need to get set up with Hyperframes
`[01:17]` and just go to Google, type Hyperframes,
`[01:19]` you can go to the website here,
`[01:20]` but ultimately you're just going to want to go to this GitHub repo for Hyperframes.
`[01:24]` And then you just need to literally copy this link, the URL,
`[01:27]` give it to Claude code and say,
`[01:28]` hey, set up Hyperframes so that we can use it to animate videos.
`[01:31]` That's it.
`[01:31]` And then on top of that,
`[01:32]` I have this free repo called Hyperframes Student Kit.
`[01:34]` And in here, it has all of the skills and examples
`[01:36]` that I actually have done with my pipeline of editing videos.
`[01:40]` And if you want to get this,
`[01:40]` you can go to my free school community,
`[01:42]` the link for that is down in the description.
`[01:43]` In here, you go to classroom
`[01:44]` and you can click on all YouTube resources,
`[01:46]` or you can go to AI skills
`[01:48]` and you can access that Hyperframes Student Kit.
`[01:50]` Anyways, I said the first step is for you to transcribe the video
`[01:53]` so you can make sure that motion graphics
`[01:54]` and animations come in at the exact perfect time.
`[01:56]` So it has to transcribe the video.
`[01:58]` You can do that using something like 11Labs API,
`[02:00]` or you can do that with something like Whisper,
`[02:02]` which is more of a local model
`[02:03]` that can run and transcribe videos,
`[02:05]` but 11Labs is a little bit quicker.
`[02:06]` So 11Labs you pay per usage
`[02:08]` and Whisper is gonna be free,
`[02:10]` but it's just a little slower.
`[02:11]` So you can use either one,
`[02:12]` and it's really simple to get that set up.
`[02:13]` You just ask Cloud Code to help you set that up.
`[02:15]` I said, then you will build the animations
`[02:17]` based on my instructions.
`[02:18]` When I say powerful models like Fable 5.1 and GBD6 Astra,
`[02:21]` I want you to have animations come in where I'm pointing.
`[02:23]` So that was basically right here where I point
`[02:25]` and I have Fable 5.1 come in right over here,
`[02:28]` and then I have GBD6 Astra come over here.
`[02:31]` And I told it that I wanted to have a Cloud logo
`[02:33]` and I wanted to have an OpenAI logo.
`[02:34]` I wanted it to be animated.
`[02:36]` That's basically all I said,
`[02:37]` besides also saying,
`[02:38]` make sure there's some sort of liquid glass card
`[02:40]` behind the element as it's animated,
`[02:42]` otherwise it will be hard to see.
`[02:43]` And as you saw right here,
`[02:44]` we got liquid glass right behind it
`[02:46]` so that we could actually read the text and see the logo.
`[02:49]` So that was me using natural language as you see.
`[02:51]` Then I said, when I say best outputs ever,
`[02:53]` I want you to have all three of those words at the bottom
`[02:55]` and highlight them.
`[02:56]` And so that's what it did right down here.
`[02:57]` Opus 5.5, best outputs ever.
`[03:00]` And you'll notice that it also put
`[03:01]` a little bit of an overlay under this text
`[03:04]` because once again, it wanted to make sure
`[03:05]` that we could actually read it.
`[03:07]` So very, very well done there.
`[03:08]` Then I said, for the rest of the video,
`[03:09]` when I'm talking about B roll and screenshots
`[03:11]` and generating images and videos,
`[03:13]` I want you to have things come in on the left
`[03:14]` and right side of the screen.
`[03:16]` Once again, they should have some sort of overlay.
`[03:17]` And I want you to actually go off
`[03:19]` and get a B roll screen recording
`[03:20]` and get a screenshot and pull in stuff
`[03:22]` because I want you to prove to the viewers
`[03:23]` that you're able to do all of this.
`[03:25]` The whole point is that I'm explaining
`[03:27]` what Opus is capable of
`[03:28]` when it comes to animating and editing videos
`[03:30]` and I want you to prove it in real time.
`[03:32]` Now that is basically my entire prompt.
`[03:34]` And what's so cool about that
`[03:35]` is that it goes off and it does it,
`[03:37]` but it also puts its own spin on things.
`[03:39]` Like you'll notice at the very beginning,
`[03:40]` it's doing this very subtle zoom in effect.
`[03:42]` I didn't ask for that,
`[03:43]` but it just kind of knew to do that
`[03:45]` to make it more engaging.
`[03:46]` I didn't ask for this either
`[03:47]` when I said the one prompt thing right there,
`[03:49]` it just did that by itself
`[03:50]` with a super cool, cloud-looking interface.
`[03:53]` I didn't ask for this either,
`[03:54]` but I absolutely love it.
`[03:55]` And then you'll see what it interpreted
`[03:56]` when I said get the screen recording,
`[03:58]` get the screenshot, generate an image, generate video.
`[04:01]` It did all of that on its own,
`[04:03]` amazing taste, the verification.
`[04:05]` I thought this was a super clean animation right here.
`[04:07]` The verification with like screenshots and checking,
`[04:09]` you guys will notice in my prompt,
`[04:11]` I didn't actually ask for that at all.
`[04:13]` It just did it because it thought
`[04:14]` that it would make the intro more engaging.
`[04:15]` And I would argue that it definitely did.
`[04:17]` And now you can see that's all I said.
`[04:18]` I didn't ask another prompt.
`[04:20]` And what we got was that exact video right back here
`[04:23]` with all of these things that we just saw.
`[04:24]` Now let's break down that other example
`[04:25]` that you guys saw inside of the actual intro itself.
`[04:28]` This little YouTube show reel,
`[04:30]` which I was super, super impressed by.
`[04:31]` This was also a one-shot prompt, like I said.
`[04:34]` Really, really impressive.
`[04:35]` There's so many things that wanted to play here.
`[04:37]` It had to go get screenshots of so many of my thumbnails.
`[04:39]` And then it zoomed in on the thank you one,
`[04:41]` which I think was amazing reasoning.
`[04:43]` It literally said, okay,
`[04:44]` this is Nate holding up the play button saying thank you.
`[04:47]` This is the one that we're gonna put in the center.
`[04:48]` And this is the one that we're gonna zoom in on,
`[04:50]` because I think that highlights the branding
`[04:52]` and the culture of YouTube, which was just insane.
`[04:54]` So anyways, it generated all of this stuff
`[04:56]` and the sound and the music, all of that, right?
`[04:59]` Now here's what I did in this example.
`[05:01]` What's important is that you're clear on what you want.
`[05:03]` And you'll notice in the previous version,
`[05:04]` I was like speaking very emotionally.
`[05:07]` And that's what's cool about it is sometimes
`[05:08]` you don't always know exactly what you want,
`[05:10]` but you know the emotions you want the video to create
`[05:13]` inside of you, right?
`[05:14]` So what I did is I downloaded an example that I saw on X.
`[05:17]` I saw this example from Ken,
`[05:19]` amazing output here using hyperframes and using Opus.
`[05:21]` And you'll notice there's a lot of similarities
`[05:22]` with this reel and the one
`[05:24]` that we just looked at with YouTube.
`[05:25]` So basically what I did is I used this as inspiration.
`[05:27]` I downloaded this video.
`[05:29]` I then came into Cloud Code
`[05:30]` and I gave it to Cloud Code.
`[05:32]` And I said, analyze this video,
`[05:33]` which was created by Opus 5.5
`[05:35]` and figure out why this is so good.
`[05:37]` So I liked this video and I wanted to do something similar
`[05:40]` and I had Cloud Code figure out what that is.
`[05:42]` I had Opus figure out why it's so good.
`[05:44]` And then I said, turn that into a skill.
`[05:46]` So now we have this skill called motion reel or something.
`[05:48]` And I'm gonna give that to you guys for free,
`[05:49]` just a sec.
`[05:50]` And then I said, okay, use that skill,
`[05:52]` create me my own show reel about YouTube.
`[05:54]` I said, collect B-roll images, any assets you need,
`[05:57]` make sure the whole thing feels branded to YouTube,
`[05:59]` typography, design, language, colors, branding,
`[06:01]` all that type of stuff that makes YouTube YouTube
`[06:03]` should be unmistakable in this show reel.
`[06:05]` And now we have our output.
`[06:07]` You can see here, I wrote this skill called motion show reel.
`[06:09]` So if I go into my files real quick
`[06:11]` and I go to the skills and we go all the way down
`[06:13]` to the M's, we go to the motion show reel.
`[06:15]` We now have this motion show reel skill
`[06:18]` with all of this information
`[06:19]` like about how we actually design reels like this.
`[06:21]` So I'm going to put this inside
`[06:23]` of my free school community once again.
`[06:25]` So if you guys want it, hop into my free school community
`[06:27]` and you can grab it in the YouTube resources
`[06:29]` or inside of the AI skills, it'll be in there.
`[06:32]` And now you can do reels just like that.
`[06:34]` What you'll also notice is that
`[06:35]` it had to go generate these images.
`[06:37]` So you can see it created these images
`[06:38]` and then it sent them to cling
`[06:39]` in order to turn those images into videos.
`[06:41]` And that's how we actually got these animations
`[06:43]` inside of the video right about here
`[06:46]` where we see the actual play button sort of being animated.
`[06:48]` These two scenes were because it created an image
`[06:51]` and then it created a video
`[06:52]` and then it sent it back to Claude
`[06:53]` and then Opus took all that stuff
`[06:55]` and put it into one consistent video.
`[06:58]` Now here's another show reel style video
`[07:00]` but this one didn't use that skill that we built at all.
`[07:03]` And just to show you how cool stuff can be made
`[07:05]` even with a show reel.
`[07:07]` So I said, make a dynamic 15 second motion graphics video
`[07:09]` that shows what an incredible motion designer you are
`[07:11]` like it's your show reel for a resume, go all out.
`[07:14]` I actually saw this from someone on X, they made a demo
`[07:16]` and they said this is what they prompted it with
`[07:17]` so I tried it out.
`[07:19]` I said, make it about our company, AIS,
`[07:20]` use real assets and logos from our products when possible.
`[07:22]` You can also use key.ai to generate any assets you need
`[07:25]` and use hyper frames or any other tools
`[07:26]` for motion design and music and sound effects.
`[07:28]` And with one shot prompts,
`[07:30]` this is what we got back right here.
`[07:32]` So let's take a look.
`[07:48]` You can see the similarities at the beginning
`[07:49]` with the little bead that like drops
`[07:51]` and there's sound effects.
`[07:53]` But then with the motion graphics,
`[07:54]` with the color schemes,
`[07:56]` with the same sort of like spatial awareness
`[07:58]` of doing things like this, I thought was so cool.
`[08:00]` It pulled pictures from our website.
`[08:02]` It knew how many members we had.
`[08:03]` It had this 3D sort of image
`[08:05]` which I think was an image that was generated
`[08:07]` and then it was turned into a video
`[08:08]` similar to that YouTube show reel.
`[08:10]` Anyways, this background image is from our website as well.
`[08:13]` So just very, very well done.
`[08:15]` Real quick guys,
`[08:16]` I've got this completely free website design skill
`[08:18]` that I'm giving away.
`[08:19]` I use this for every single website that I build
`[08:21]` including our AI Automation Society site
`[08:23]` which I think is pretty slick
`[08:25]` and I absolutely love this website.
`[08:27]` It's called Scrollcraft
`[08:28]` and it understands things like scroll-driven animations
`[08:30]` and layering, but also it has things in there
`[08:32]` like taste, typography, spacing, depth.
`[08:35]` It's just a really good website design skill in general
`[08:38]` and it's completely free.
`[08:39]` So the link for this will be down in the description,
`[08:40]` but let's get back to the video.
`[08:42]` Now, let me show you guys,
`[08:42]` this is one of my new favorite benchmarks.
`[08:45]` I basically give Cloud Code access to a folder
`[08:48]` which has 105 gigabytes of YouTube videos,
`[08:51]` or sorry, not YouTube videos,
`[08:52]` videos and recordings and resources from our event, AIS Live.
`[08:56]` And then I say, hey, look through all this
`[08:57]` and create me a sizzle reel.
`[08:58]` Tell a story out of this and look what I got here.
`[09:01]` Now, this wasn't a one-shot prompt.
`[09:02]` This was one prompt
`[09:03]` and then me giving one round of iteration
`[09:05]` and then having it fix one thing.
`[09:07]` So technically three prompts.
`[09:08]` That's why it is V2.1,
`[09:10]` but let's take a look at this output right here.
`[09:14]` Hello, hello, AIS Live.
`[09:16]` I'm so, so pumped.
`[09:17]` It was electric.
`[09:18]` Let's go.
`[09:19]` Never even opened VS Code.
`[09:21]` Signed the deal.
`[09:23]` The chat's going crazy.
`[09:25]` Trippie.
`[09:27]` Fantastic event.
`[09:28]` This was amazing.
`[09:30]` Such a fun two days.
`[09:32]` I literally like logged off yesterday just buzzing.
`[09:35]` I had goosebumps.
`[09:38]` Can't wait for the next one.
`[09:41]` I mean, do you guys have any idea
`[09:43]` of how complicated that process is
`[09:45]` just to tell a story out of an event
`[09:47]` when you just are given a folder of resources?
`[09:50]` And of course it's marketing for our next one,
`[09:52]` which is actually real coming up October 17th and 18th.
`[09:54]` So mark your calendars if you guys wanna show up.
`[09:57]` More details will be in the description.
`[09:58]` But I know there were a few things that weren't great.
`[10:00]` There were some times where there was like an awkward cut
`[10:02]` of the speech and a few things that we could tweak.
`[10:05]` But look at this.
`[10:07]` Look how it made like this tunnel of all the screens.
`[10:09]` Look at the beginning,
`[10:10]` how it was zooming in on different screens.
`[10:11]` Like it was really aware of the spacing
`[10:14]` and this is just really, really cool.
`[10:15]` It was also pulling out specific moments
`[10:17]` in the transcripts of these calls
`[10:19]` that were showing kind of like the vibe
`[10:21]` and the energy within the live event.
`[10:23]` This is my favorite scene here at the end
`[10:24]` where it has all of these scenes come together
`[10:27]` and it forms the actual AS Live logo
`[10:29]` even with the little red dot.
`[10:30]` And then it zooms in on the red dot
`[10:32]` and it says, your seat is in the middle.
`[10:34]` I just thought that the way that it was able
`[10:36]` to actually bring all of this to life
`[10:38]` is really, really impressive to me.
`[10:40]` Now I also wanted to show you guys
`[10:41]` what else is possible.
`[10:42]` Like a lot of times it's about thinking of the use case.
`[10:45]` So I recorded this really simple video
`[10:47]` of me explaining how to make avocado toast.
`[10:49]` And I perfected that by the way.
`[10:51]` My avocado toast is so good.
`[10:52]` But anyways, I just wanted to show you,
`[10:53]` I did three different edits with this avocado toast video.
`[10:56]` This one I said, hey, I want you to edit this
`[10:58]` using hyperframes.
`[10:59]` I'm looking for a simple and clean whiteboard,
`[11:01]` hand-drawn style animation.
`[11:03]` And it's really simple as if you're trying to explain
`[11:05]` to a kid how to make avocado toast, simple graphics,
`[11:07]` simple animations, easy to understand.
`[11:09]` If you need to generate any images
`[11:11]` or sorry, assets like images or videos,
`[11:13]` you can use key.ai.
`[11:14]` I then said that some scenes
`[11:16]` should be a full screen whiteboard takeover.
`[11:18]` And some scenes should just be the left half
`[11:20]` as the whiteboard and the right half is my face.
`[11:22]` So it then went ahead and started generating things.
`[11:25]` It started reasoning, it started testing things out.
`[11:27]` And now we have this output
`[11:28]` which I'll go ahead and play right now.
`[11:30]` All right, so here's how I make avocado toast.
`[11:32]` When you put the toast in the toaster,
`[11:34]` when you're letting it sit,
`[11:35]` you don't set it flat on the plate
`[11:37]` because then that bottom side gets a little soggy.
`[11:39]` You want that both sides to be crispy.
`[11:41]` Then you put the eggs on the pan,
`[11:43]` you mash up the avocado,
`[11:44]` you spread the avocado on the crispy bread.
`[11:46]` I put like everything bagel seasoning on the avocado mash
`[11:49]` and then I do some balsamic vinegar.
`[11:51]` And then you put the eggs on top of the toast
`[11:53]` and that's how it's done.
`[11:54]` Now my main critique here is that the eggs are super tiny
`[11:57]` and the balsamic glaze
`[11:58]` is only on one little piece of the toast.
`[12:00]` So that wouldn't taste as good as if it was everywhere.
`[12:03]` But anyways, look how good this was able to
`[12:06]` in one prompt just animate the stuff
`[12:07]` in a very simple and engaging way.
`[12:10]` It's hand-drawn, it is, like I said,
`[12:11]` it's kind of friendly and playful
`[12:12]` as if you wanted to show a kid.
`[12:14]` But this was literally just one prompt
`[12:15]` and it took care of everything.
`[12:17]` Now, when I first really started using AI to edit videos,
`[12:19]` it was for course style videos,
`[12:21]` things that were super easy.
`[12:22]` We just wanted them animated with like bullet points
`[12:25]` and super simple images and graphics.
`[12:27]` So here's what I did in this one.
`[12:29]` I need you to edit a course style video
`[12:31]` for me using hyperframes.
`[12:32]` My camera will start off full screen
`[12:33]` and then I want it to be a rounded crop.
`[12:35]` The background's gonna be super simple,
`[12:36]` super minimalistic and the style I'm looking for
`[12:39]` is just bullet points with important takeaways,
`[12:41]` not too wordy and they should be big.
`[12:43]` And then visual aids should just be AI generated images,
`[12:45]` very simple, very light motion graphics
`[12:47]` to help illustrate concepts.
`[12:49]` And here is what we got.
`[12:49]` This was once again, a one-shot prompt.
`[12:52]` Oh wait, that was just an image.
`[12:53]` It was just doing verification.
`[12:54]` Here we go.
`[12:55]` All right, so here's how I make avocado toast.
`[12:57]` When you put the toast in the toaster,
`[12:59]` when you're letting it sit,
`[13:01]` you don't set it flat on the plate
`[13:02]` because then that bottom side gets a little soggy.
`[13:04]` You want both sides to be crispy.
`[13:06]` Then you put the eggs on the pan,
`[13:08]` you mash up the avocado,
`[13:09]` you spread the avocado on the crispy bread.
`[13:11]` I put everything bagel seasoning on the avocado mash
`[13:14]` and then I do some balsamic vinegar
`[13:16]` and then you put the eggs on top of the toast
`[13:18]` and that's how it's done.
`[13:19]` So all of the images and videos in this video
`[13:22]` were AI generated.
`[13:23]` All of this was AI generated
`[13:25]` and you can see that it's gonna save you so much time
`[13:26]` because it can go get B-roll, it can take screenshots,
`[13:29]` it can generate things if you need it to.
`[13:32]` It's just really cool because now you can film content
`[13:35]` and editing doesn't have to be the bottleneck anymore,
`[13:37]` especially when you start to build skills
`[13:38]` around stuff like your preferences and motion styles
`[13:42]` and all that kind of stuff, your brand guidelines.
`[13:44]` And then the last one I did here
`[13:45]` was kind of a short form video
`[13:47]` and this was using hyperframes once again.
`[13:49]` And you'll notice that I'm not really having this
`[13:51]` leverage other skills.
`[13:52]` So I wanted to show you how easy it is
`[13:53]` to do a one-shot prompts with Obas 5.5.
`[13:56]` Pretty much all these examples
`[13:57]` I've been running on high by the way,
`[13:58]` high meaning the effort level.
`[14:00]` And I just said basically this,
`[14:01]` generate the assets you need, have it be engaging,
`[14:03]` have it be fast paced, easy to understand.
`[14:05]` So let's see what we got down here for this short.
`[14:09]` Here's how I make avocado toast.
`[14:10]` When you put the toast in the toaster,
`[14:12]` when you're letting it sit,
`[14:13]` you don't set it flat on the plate
`[14:15]` because then that bottom side gets a little sog.
`[14:17]` You want that both sides to be crispy.
`[14:19]` Then you put the eggs on the pan,
`[14:20]` you mash up the avocado,
`[14:21]` you spread the avocado on the crispy bread.
`[14:23]` I put like everything bagel seasoning on the avocado mash
`[14:26]` and then I do some balsamic vinegar.
`[14:27]` And then you put the eggs on top of the toast
`[14:29]` and that's how it's done.
`[14:32]` I mean, it's not perfect, right?
`[14:33]` But a one-shot prompt and it's just,
`[14:36]` it's really cool that it's able to switch
`[14:37]` between these different scenes.
`[14:39]` It definitely keeps my attention
`[14:40]` because we have all this different sorts
`[14:42]` of B-roll going on in the background.
`[14:43]` It is just a really, really decent output
`[14:46]` when you consider what this would have taken
`[14:48]` for a human to do it for you.
`[14:49]` And now one-shot prompt, you iterate,
`[14:52]` you iterate, you build skills.
`[14:53]` And I wanted to show you guys one more example
`[14:55]` with Lululemon because this is like
`[14:57]` a physical tangible product.
`[14:59]` Look how good it did at making this video feel
`[15:02]` like Lululemon.
`[15:30]` So if you guys think about what it actually had to do there,
`[15:32]` all of these videos were obviously AI generated.
`[15:35]` But what I'm pretty sure it did is it went to Lululemon
`[15:37]` and it found all these actual pieces of clothing.
`[15:40]` It found them, it took pictures of the actual model here
`[15:43]` and then generated videos of them running
`[15:45]` or jumping or whatever it is in the clothes.
`[15:49]` And then of course it brings it all together here
`[15:50]` with actual catalog images.
`[15:52]` It's just really cool to think about
`[15:53]` how many little pieces would have had to go into this
`[15:56]` if you were editing this or creating this as a human.
`[15:58]` But really as a human, all I did was I told it
`[16:01]` what I wanted and sort of the emotional feeling
`[16:03]` I wanted it to carry throughout.
`[16:05]` The vibe, high energy, fast paced, engaging,
`[16:08]` sync the music to the beats, sound effects,
`[16:11]` things like that.
`[16:12]` So I just wanted to talk about the five things
`[16:13]` that I'm constantly thinking about
`[16:14]` when I'm actually editing videos with AI.
`[16:16]` I'm just gonna run through these super simply
`[16:17]` because you just, you could basically give the transcript
`[16:21]` of this section to your AI agent and it would be fine.
`[16:23]` So the first piece is to transcribe.
`[16:25]` If you're starting off with a clip
`[16:27]` and you need it to be edited like a video
`[16:29]` or a course or whatever it is,
`[16:31]` you obviously want to transcribe first
`[16:32]` so that the beats can come in at the right time
`[16:35]` and so that the AI knows how to tell a story out of it.
`[16:37]` Transcribe is essential whether you wanna use Whisper
`[16:40]` or 11 Labs or some other tool, transcribing is essential.
`[16:44]` From there, you're going to have it cut things out.
`[16:46]` So if it's mistakes, cut out the mistakes.
`[16:48]` If it notices in the transcript
`[16:50]` that there's like 20 seconds of dead space,
`[16:52]` cut out the dead space, things like that.
`[16:53]` You're cutting things up.
`[16:54]` And a lot of times I'll use AI
`[16:55]` just to literally cut out mistakes
`[16:57]` and then I'll take the clip
`[16:58]` and do whatever I want with it,
`[16:59]` but it's able to just clean out your content
`[17:02]` so much quicker than you could
`[17:03]` because you'd be in the editor looking for the dead space
`[17:05]` and then, you know, snipping everything out.
`[17:07]` And then number three is to plan the beats.
`[17:09]` A lot of times from there, what I like to do
`[17:11]` is I like to be very specific about what it is
`[17:13]` that I want.
`[17:14]` As you guys saw in this intro version,
`[17:15]` the intro for this video,
`[17:16]` I was basically just planning out what I wanted.
`[17:18]` Now, obviously it went off the cuff a little bit
`[17:20]` and it was creative,
`[17:21]` but if I would have said like,
`[17:22]` these are the only beats I want you
`[17:23]` to actually create nothing else,
`[17:24]` it would have done that,
`[17:26]` but I let it be creative here.
`[17:27]` But I basically said, hey, at this point,
`[17:29]` I want this to come in.
`[17:30]` I want this to come in.
`[17:31]` I want this to come in.
`[17:33]` And the better you can set expectations
`[17:34]` of what you're looking for
`[17:35]` and what you would consider good,
`[17:36]` obviously the better or not better,
`[17:38]` but the more aligned your output is going to be.
`[17:39]` Number four is to use skills.
`[17:41]` So build skills around things.
`[17:42]` If you build a lot of reels,
`[17:44]` then build skills around reels.
`[17:45]` Use my Hyperframe student kit.
`[17:46]` Use resources and use inspiration.
`[17:50]` Like you guys saw me do,
`[17:51]` I took a video that I really liked
`[17:52]` and I told it to build a skill.
`[17:53]` Now, guess what?
`[17:54]` Every time I run that skill,
`[17:56]` I will look at the output and say,
`[17:57]` hey, in this version, I really liked this
`[17:59]` and I really didn't like this.
`[18:01]` Update the skill with that information,
`[18:02]` run it again, and then I'll give you more feedback.
`[18:04]` And that way you're actually building a reusable component
`[18:07]` where every single time you run the skill,
`[18:08]` it's getting better
`[18:09]` and you're able to just move faster and faster.
`[18:11]` You don't wanna have to repeat yourself every time.
`[18:13]` If you ever find yourself repeating something,
`[18:15]` just throw it in the skill.
`[18:16]` And then the fifth one,
`[18:17]` probably the most important one,
`[18:18]` is the verification loop.
`[18:20]` You'll notice how as it's going through
`[18:21]` a lot of my videos,
`[18:22]` it's taking screenshots and looking at them
`[18:25]` and then making iterations.
`[18:26]` And that's how you get in that loop
`[18:26]` where you're not just basically saying,
`[18:28]` okay, here is my output number one.
`[18:30]` You're getting output number like five or six
`[18:33]` because the agent basically did this.
`[18:35]` It delivered output one and then it watched it.
`[18:38]` It realized there was some mistakes
`[18:39]` and then it came back and it delivered output two.
`[18:41]` And then it watched output two
`[18:42]` and then it kept iterating on its outputs
`[18:45]` until it realized, okay, this one is finally good enough
`[18:47]` where I'm gonna give it to Nate
`[18:49]` and here you go, Nate,
`[18:50]` this is the finished video.
`[18:51]` So now you're getting something
`[18:52]` that has already been checked by the AI and iterated on,
`[18:55]` then compared to if it just handed you this first version
`[18:58]` and then you're frustrated
`[18:59]` and you have to make all these prompts.
`[19:01]` But anyways, guys, there are so many use cases
`[19:03]` when it comes to using AI to help you edit things
`[19:05]` or add motion design
`[19:07]` because it's not really something
`[19:08]` that you had to have previous video editing experience
`[19:10]` in order to take advantage of now.
`[19:11]` So don't let editing be your bottleneck,
`[19:13]` but that's gonna do it for today.
`[19:14]` If you enjoyed or you learned something new,
`[19:16]` please give it a like, it helps me out a ton.
`[19:17]` And as always, I appreciate you guys
`[19:18]` making it to the end of the video.
`[19:19]` I'll see you all in the next one.
`[19:21]` Thanks everyone.
