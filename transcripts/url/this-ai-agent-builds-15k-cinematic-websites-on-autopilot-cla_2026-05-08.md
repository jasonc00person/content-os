# This AI Agent Builds $15K Cinematic Websites on Autopilot (Claude Code + Nanobanana 2)

- **Source:** https://www.youtube.com/watch?v=bUt1WpDlI6E
- **Uploader:** Jay E | RoboNuggets
- **Uploaded:** 2026-04-01
- **Duration:** 15:59
- **Detected language:** en (p=1.00)
- **Model:** small.en

## Transcript

I just created an agent that auto-builds cinematic, responsive websites from scratch. You drop in your current website, it analyzes your brand's color palette, your company's details, and designs a new website for you. Using this, I was able to build more than 10 different cinematic websites in a matter of minutes. So whether you're using cloud code, OpenClaw, or another authentic platform entirely, by the end of this video, you'll learn exactly how it works and how you can replicate it for your own setup. And if you're new here, my name's Jay. I spent over a decade working with brands you probably know have been in AI since my master's in data science. And now I run our AI solutions practice in one of the largest AI communities globally. Let's get started. Just to give you some examples of what this agent created for us, it transformed this website into this with the pizza looking delicious in the background. And if I scroll down, it even has an accordion piece in here to show the different menu options. I gave it this website for a flower shop, turned it into this website where as you scroll, it forms this image of a flower and even this responsive page where your mouse just becomes photos of flowers that they have. It also created this landing page for Monos, which I think is really cool. This page for a shoe cleaning service here in Sydney, even making the section on how it works really interactive and responsive. You also have this landing page for a brewing company that also shows the brand story in their colors. This one is for a local cupcake shop here in Sydney. And you can see just how good that animation is, especially for people who are scrolling through these websites. You have one here for a jewelry company, letting you just browse their different categories in here. This one is for a chocolate company, and this is an example for a watch company. So that looks quite nice along with that responsiveness as you scroll down the page. This one turned out really well, where you can see it's for a perfume brand where if you scroll down, it just shows that perfume bottle exploding into flowers, which is looking really nice. And of course, it was able to get from their original website, the brand story as well, including a few keywords in here. This one is for a ramen shop. And then when you click explore the menu, we'll also navigate to the menu that they have. This one is for a demo website for Roomcraft, which is an IKEA service that basically gives you complete room designs delivered and assembled. So this scrolling animation right here where it unpacks the boxes and brings out the whole bedroom all the furniture that encapsulates this service perfectly. So there you go. All of this was made by this agent, and I'll be taking you through it today. Now this agent kit, which we are calling cinematic sites, we originally built this for our community. So if you're watching this and you're part of the community, then remember that you can just grab this whole agent kit in the classroom. But if you want to learn how this works yourself so that you can set it up from scratch, then don't worry because that is exactly what we'll be doing in this video. And just to give you an overview, this agent kit, the one that runs it is this skill.md. And this agent skill is simply a markdown file, which is basically an instruction manual for your agent to follow through the four steps that it will do in order to make these cinematic sites automatically. And those four steps are as follows, where when you give your agent a website to copy, what it will basically do is analyze that brand to give you the brand colors, the brand palette, it will generate the scene, which it uses to make the website more cinematic. And when we talk about the cinematic scene, basically it's this hero video where it shows the specific product in action as you scroll through the page. And then it builds out the website itself using all the HTML knowledge that it had during the brand analysis part, and then it deploys it for you so that immediately you have a website that is accessible anywhere using this tool called Vercel. Like I mentioned earlier, you can do this on OpenCloud, on Cloud Code, or whatever agentic platform you're using. For what I'll demo now, I'll do it via this Telegram agent, which is actually connected to Cloud Code, so it's not OpenCloud. And if you're curious how I do this, it's basically a long running session that I have over at my terminal, and I just connect Cloud Code using the new Telegram channels feature. So I'll link that tutorial somewhere in this video. But you can see for this agent, we do have this cinematic sites skill and agent kit already installed, which means that if we give it a website to improve, then it'll be able to run through this process with us. Now, real quick, we just released the agentic AI master class for our members at RoboNuggets, which takes you from zero to mastery when working with agents. There's a link to the community in the pinned comment below. We've got founders in there who landed their first client in weeks, live build sessions where we create this stuff together, and the actual templates behind what I showed in this video. The community is also the reason these lessons get made, so see that below if that's for you. And for this demo, what I'll do is improve the website of this restaurant called Ichiraku Canteen. They're basically a ramen restaurant here in Sydney, and you can see their current website doesn't really have anything in it. It's just a reservation page, so they're a good candidate for this service. And so what I will do is just give the current website of Ichiraku and just say, all right, can you use a cinematic sites skill in order to improve this website? Also, for this specific run, go through the steps one by one so that we can observe you running it for this demo. And I just sent that part of the prompt so that we can observe it. But obviously, if you are running this in the background, then you can just have it run through all of the steps automatically. And over here, you can see that it is now conducting that brand analysis, and it's extracting the brand colors, the brand palette, and just overall crafting a brand for us using the information that it has. And if you're curious how it does that, basically, it's all just written in this skill.md that just basically provides the instructions for the agent on what to extract a couple of methodologies on how to do that. And by the end, it gives a pause point for the user, because maybe you would want to approve the brand card first before you continue. So when it's completed that, you can see it created this brand card for me, put it in this HTML page, and I just ask it to open it for me. And this is what it looks like. So this is just a staging step so that you can approve if this is up to spec. So what's good is it was able to capture the industry, the color palette, and even the typography. It made sure to include some Japanese characters in there, which I think is a nice touch. And if I go and scroll down, it even gave you a headline, gives you a tagline, a suggested hero line, and an overall theme direction. So I think this is a nice visual way for you to just approve the branding of this website, and it gives you a proper pause point in order to make the output of this the best that it can be. And for this step one, you actually don't need any external tools. You do have the option to use Firecrawl, but since agentic platforms like Cloud Code or Antigravity or even OpenClaw can read HTML files, then if you provide the website that you want to extract these components for, they will be able to do a pretty good job with it. But when we're OK with that, we can just continue to step two. We're now what it will do is to just go ahead and create those scenes for us. Now, by default, this skill allows your agent to suggest three high quality ideas, and of course, you can have more or you can also just let it go do its thing and select for you. But you can see here that for step two, it gave me some options for the hero animation. So this is pretty cool that it even gave us emojis to guide that. So one is Steam Rising, a single bowl of Tonkotsu ramen on a dark wooden counter. So that sounds good. There's also this option of, I guess, the ramen pouring an overhead ankle, rich golden broth being poured slowly into a dark ceramic bowl or this third option, the wide shot of an empty ramen bar counter. I think we'll either do number one or number two. So what we can actually do. Hey, so I think number one and number two are looking really good. I do want to feature a ramen that is shrimp based, though. So let's try that. And can you generate those images for me before we animate them into videos? And with that command, what it is now doing is to generate both images using nano banana. And similarly, if you're curious how to set that up, it's all just within this skill file as well. So if we go to step two scene generation, here is where we instructed it to suggest three concepts. And then to generate an image, we gave it this code to call on Google's APIs, which is how it accesses nano banana. And then later on, when we get those images, we will be animating them via cling 3.0. Now, the reason why we're using Google's APIs by default here is because for each Gmail account that you have, they actually give you a $300 welcome credit, which lasts you a long time, especially if you're just using their nano banana or video models. So when you set up this skill for the first time, that will also show you where to find your API keys that you can just provide your agent so that they're also able to tap into the nano banana models directly. Now, if you're curious how to develop this yourself and how to give your agent the skill to actually use nano banana, then what you can do is just provide your agent with this link, which is just all the documentation that Google has regarding nano banana and your agent will scour this page in order to find the right commands to use nano banana, nano banana 2 or nano banana pro. So if you want to replicate what I did, then this would be your master page. And you don't need to go through third party resellers like Higgsfield or FreePick for the same models. And you can see here that both images generated and open. So I just asked our agent to put them on the generations tab. And the tab is just here in our command center. So if you go to the generations tab, you can see here, it's basically a Google flow studio or Higgsfield equivalent, where I just connected my cloud code to this so that whenever I need to generate images or videos, I'll be able to display them visually here. I can also download them or if I click on it, that copies the path so that it's much easier to provide to our agents. But all right, so for our ramen shop, basically, you can see here that it created these two images, which is both looking quite good. But I think the one that we will go for would be this one, because I can just imagine this in the website to be looking really good. So what we'll do now is I'll just copy that, give that to our agent and I'll say, hey, this one looked really good. I think it's ready for animation. What I want you to do is animate it so that the ingredients settle into the ramen bowl and then the camera zooms in to the ramen to show the rich flavor of it. And for this one, let's actually try for it to do two videos just so that there's more optionality, because with a lot of these models, the more volume that you do, the sort of higher chances of winning that you have, and it's just the probabilistic nature of these. So you can see that what it is doing now is to use cling to animate the trim ramen, and that will basically happen just in the background. So you can see it's generating the scenes now, but if you're curious how that happens, going back to the skill once again, you can see that how the agent is accessing cling is through this website called wave speed. And wave speed is basically an AI model aggregator, sort of like Higgs field or free pick, but the difference is you don't need to pay like a monthly subscription to access these models. And apart from that, they also have a lot more models in place in here. So you can see if you just go and explore, you have the prime models here like nano banana, Sea Dream, et cetera, and also cling. There's other websites like file.ai or key.ai, but I think in terms of reliability, wave speed has been pretty good. So we are using them as well, but you have the optionality to use the others. Any case, so if you want to set this up by yourself, all you need to do is to find the model that you are after, at least for this build, what we are using is cling v3, image to video, and for our agent, what it's basically doing is calling on this model, uploading the images that it just created using nano banana, using Google's free credit, and also it writes the prompt here, and then it runs it to give us back that video. Now, if you want to equip your agent with the knowledge to understand how this works, all you need to do with a lot of these websites like wave speed, key.ai, is that you just need to copy the content here. And let's say you want to give that to your cloud code agent. If you copy that over, that will just provide all of the documentation around cling 3.0 pro. So that is basically what I did in order to give it that capability so that you don't need to type in your prompts and go to these websites like Google flow studio and other creative website equivalents. And so you can see here in the skill, we just standardized that and also gave a bit more control so that it knows exactly what it is that it needs to do. All right, so I think it's done with scene generation. And you can see it's saying here that those two videos are now in our generations tab. This one looked pretty cool. And this one, I think this one's better because there's a bit of a camera zoom effect in there. But for some reason, I think the camera is shaky on this one. So I'll probably actually just use this because it's a bit more consistent. So let's copy the path of that and I'll say, okay, this is the final video. Can you now go to step three and build out our website? And once we send that, you can see that it is now building that website for us. And just to show you under the hood what specifically this skill is invoking so that you understand how the agent is doing this, you can see under this step, there's rules around the architecture of the websites that it's building a lot of controls around the design system. And essentially what this is doing is it's codifying that effect where let's say you have that video, it will extract the individual frames of this video and map it to this scrolling action so that it gives that effect that as you scroll down, it runs through the frames for you. And so that whole thing has been codified in this skill already. The other thing that is part of this skill is this cinematic modules integration. And so if I scroll down here, you can see this particular site actually turned out well where it has this accordion elements in here, right? Which is really responsive, really professional. And the reason why it was able to do that is because of this cinematic module spec that we created in Robolabs as well. Now this one, because it is quite hard to recreate, we are giving it away for free. So you can just grab that in the description below, but this just gives you a lot of modular elements to enrich any website build that you have for your agents. So there's this one with a reveal text effect, modular components around future scrolling. This one has that kinetic text effect that you saw earlier, typewritten text effects, glitch effects like this one, image trails like the one that you saw here, flip cards that are pretty useful, I guess for testimonials and such, the flower animation that you saw earlier is basically just an SVG draw animation and several others in here that I think is going to help you a lot when you're coming up with website designs of your own. And there's 30 plus of these cinematic modules, by the way. So feel free to grab that below if that helps. But here you can see that the website is now done. So it gave us this landing page, and you can see this is really good. So you have the Japanese branding in there. And if we scroll down, that should animate the bowl nicely for us. So that look really well. And this scrolling animation that was coming from our cinematic modules as well. So it even included some Japanese characters in here. Let's actually translate that just to make sure that it's not putting something weird. So it says, there is a story in every cup. So I think that is pretty cool. And it even has the story, the menu, and so on. And it was even able to grab the address as well as the opening hours for us. So that is really nice. And you can see this is probably interactive. Yeah, there you go. So if I scroll down to the menu, to the hour story and visit, then that is all part of the website now, pretty much in one shot. And of course you can improve this further, right? So let's say, hey, so I actually want to add a section below, or at least have the menu use the accordion module, because I think that is a nice way to display the ramen bowls. Can you do that? And when I send that to the agent, it will understand what I'm saying, because remember in that skill, it gives it access to these cinematic modules. And the one that I'm talking about is this accordion slider, where if you look at this as a sample, that is the one where if I hover over each image, it expands and there is even an option to have a vertical variant. And here you can see that it is now doing that. And when it's done with that, we can check back on our site. And here, if we scroll down, you should now see the accordion fully built in there. And this looks really good and definitely more professional than what we started with. So now if we head to step four, this will be a simple matter for our agent, because what it is going to do is to just deploy that to Vercel. And basically Vercel is a service that hosts websites for you. And they actually do this for free, which is really good. And for you to equip your agent with this knowledge, all you need to do, once again, is to give your agent the documentation for Vercel, and they'll be able to do exactly what it did here. And so here you can see that it is now live at this website, and you can send that to your client as a demo site that people can visit and also provide some feedback on. So that's looking really good. And just to recap, we went from this, which is practically not even a website, it's just a booking form, into this, which has a cinematic background, a much more rich experience for the users of this website, and is definitely more premium versus how we started. And there you have it, that is the full agent pipeline, where you give it a website, it analyzes the brand, generates the scenes, builds the website, and even deploys it online. Now, if you need the 31 module cinematic pack, that's available free for everyone just in our network, so you can grab that. And for this full cinematic website, you can get that inside the RoboNuggets community. I hope that was helpful. And if it is, then consider subscribing because that helps us a lot to put out more educational content like this. And if you want to understand further how I'm running cloud code as a 24 seven AI assistant, then you can watch this video next. I'll see you guys next time. Thank you.

## Timestamped

`[00:00]` I just created an agent that auto-builds cinematic, responsive websites from scratch.
`[00:04]` You drop in your current website, it analyzes your brand's color palette, your company's
`[00:07]` details, and designs a new website for you.
`[00:10]` Using this, I was able to build more than 10 different cinematic websites in a matter
`[00:13]` of minutes.
`[00:14]` So whether you're using cloud code, OpenClaw, or another authentic platform entirely, by the
`[00:18]` end of this video, you'll learn exactly how it works and how you can replicate it for
`[00:21]` your own setup.
`[00:22]` And if you're new here, my name's Jay.
`[00:23]` I spent over a decade working with brands you probably know have been in AI since my
`[00:26]` master's in data science.
`[00:27]` And now I run our AI solutions practice in one of the largest AI communities globally.
`[00:31]` Let's get started.
`[00:36]` Just to give you some examples of what this agent created for us, it transformed this website
`[00:40]` into this with the pizza looking delicious in the background.
`[00:43]` And if I scroll down, it even has an accordion piece in here to show the different menu
`[00:46]` options.
`[00:47]` I gave it this website for a flower shop, turned it into this website where as you scroll,
`[00:51]` it forms this image of a flower and even this responsive page where your mouse just
`[00:54]` becomes photos of flowers that they have.
`[00:57]` It also created this landing page for Monos, which I think is really cool.
`[01:00]` This page for a shoe cleaning service here in Sydney, even making the section on how
`[01:04]` it works really interactive and responsive.
`[01:06]` You also have this landing page for a brewing company that also shows the brand story in
`[01:10]` their colors.
`[01:11]` This one is for a local cupcake shop here in Sydney.
`[01:13]` And you can see just how good that animation is, especially for people who are scrolling
`[01:17]` through these websites.
`[01:18]` You have one here for a jewelry company, letting you just browse their different categories
`[01:22]` in here.
`[01:23]` This one is for a chocolate company, and this is an example for a watch company.
`[01:27]` So that looks quite nice along with that responsiveness as you scroll down the page.
`[01:32]` This one turned out really well, where you can see it's for a perfume brand where if you
`[01:34]` scroll down, it just shows that perfume bottle exploding into flowers, which is looking really
`[01:39]` nice.
`[01:40]` And of course, it was able to get from their original website, the brand story as well,
`[01:45]` including a few keywords in here.
`[01:47]` This one is for a ramen shop.
`[01:48]` And then when you click explore the menu, we'll also navigate to the menu that they
`[01:51]` have.
`[01:52]` This one is for a demo website for Roomcraft, which is an IKEA service that basically gives
`[01:57]` you complete room designs delivered and assembled.
`[02:00]` So this scrolling animation right here where it unpacks the boxes and brings out the whole
`[02:04]` bedroom all the furniture that encapsulates this service perfectly.
`[02:08]` So there you go.
`[02:09]` All of this was made by this agent, and I'll be taking you through it today.
`[02:12]` Now this agent kit, which we are calling cinematic sites, we originally built this for our community.
`[02:17]` So if you're watching this and you're part of the community, then remember that you can
`[02:20]` just grab this whole agent kit in the classroom.
`[02:23]` But if you want to learn how this works yourself so that you can set it up from scratch, then
`[02:26]` don't worry because that is exactly what we'll be doing in this video.
`[02:29]` And just to give you an overview, this agent kit, the one that runs it is this skill.md.
`[02:34]` And this agent skill is simply a markdown file, which is basically an instruction manual
`[02:38]` for your agent to follow through the four steps that it will do in order to make
`[02:42]` these cinematic sites automatically.
`[02:44]` And those four steps are as follows, where when you give your agent a website to copy,
`[02:48]` what it will basically do is analyze that brand to give you the brand colors, the brand
`[02:52]` palette, it will generate the scene, which it uses to make the website more cinematic.
`[02:56]` And when we talk about the cinematic scene, basically it's this hero video where it shows
`[02:59]` the specific product in action as you scroll through the page.
`[03:03]` And then it builds out the website itself using all the HTML knowledge that it had
`[03:07]` during the brand analysis part, and then it deploys it for you so that immediately
`[03:11]` you have a website that is accessible anywhere using this tool called Vercel.
`[03:15]` Like I mentioned earlier, you can do this on OpenCloud, on Cloud Code, or whatever
`[03:18]` agentic platform you're using.
`[03:20]` For what I'll demo now, I'll do it via this Telegram agent, which is actually connected
`[03:23]` to Cloud Code, so it's not OpenCloud.
`[03:25]` And if you're curious how I do this, it's basically a long running session that I have
`[03:28]` over at my terminal, and I just connect Cloud Code using the new Telegram channels feature.
`[03:32]` So I'll link that tutorial somewhere in this video.
`[03:34]` But you can see for this agent, we do have this cinematic sites skill and agent kit
`[03:38]` already installed, which means that if we give it a website to improve, then it'll
`[03:41]` be able to run through this process with us.
`[03:43]` Now, real quick, we just released the agentic AI master class for our members at RoboNuggets,
`[03:47]` which takes you from zero to mastery when working with agents.
`[03:51]` There's a link to the community in the pinned comment below.
`[03:53]` We've got founders in there who landed their first client in weeks, live build sessions
`[03:56]` where we create this stuff together, and the actual templates behind what I showed
`[03:59]` in this video.
`[04:00]` The community is also the reason these lessons get made, so see that below if that's
`[04:03]` for you.
`[04:03]` And for this demo, what I'll do is improve the website of this restaurant called
`[04:07]` Ichiraku Canteen.
`[04:08]` They're basically a ramen restaurant here in Sydney, and you can see their current
`[04:11]` website doesn't really have anything in it.
`[04:13]` It's just a reservation page, so they're a good candidate for this service.
`[04:17]` And so what I will do is just give the current website of Ichiraku and just say,
`[04:21]` all right, can you use a cinematic sites skill in order to improve this website?
`[04:26]` Also, for this specific run, go through the steps one by one so that we can
`[04:29]` observe you running it for this demo.
`[04:31]` And I just sent that part of the prompt so that we can observe it.
`[04:34]` But obviously, if you are running this in the background, then you can just have
`[04:36]` it run through all of the steps automatically.
`[04:38]` And over here, you can see that it is now conducting that brand analysis,
`[04:41]` and it's extracting the brand colors, the brand palette, and just overall
`[04:44]` crafting a brand for us using the information that it has.
`[04:47]` And if you're curious how it does that, basically, it's all just written in
`[04:50]` this skill.md that just basically provides the instructions for the agent
`[04:54]` on what to extract a couple of methodologies on how to do that.
`[04:57]` And by the end, it gives a pause point for the user, because maybe you would
`[05:00]` want to approve the brand card first before you continue.
`[05:03]` So when it's completed that, you can see it created this brand card for me,
`[05:06]` put it in this HTML page, and I just ask it to open it for me.
`[05:09]` And this is what it looks like.
`[05:11]` So this is just a staging step so that you can approve if this is up to spec.
`[05:15]` So what's good is it was able to capture the industry, the color palette,
`[05:19]` and even the typography.
`[05:20]` It made sure to include some Japanese characters in there,
`[05:22]` which I think is a nice touch.
`[05:24]` And if I go and scroll down, it even gave you a headline, gives you a tagline,
`[05:28]` a suggested hero line, and an overall theme direction.
`[05:32]` So I think this is a nice visual way for you to just approve
`[05:34]` the branding of this website, and it gives you a proper pause point
`[05:37]` in order to make the output of this the best that it can be.
`[05:40]` And for this step one, you actually don't need any external tools.
`[05:43]` You do have the option to use Firecrawl, but since agentic platforms
`[05:46]` like Cloud Code or Antigravity or even OpenClaw can read HTML files,
`[05:50]` then if you provide the website that you want to extract these components for,
`[05:54]` they will be able to do a pretty good job with it.
`[05:56]` But when we're OK with that, we can just continue to step two.
`[05:58]` We're now what it will do is to just go ahead and create those scenes for us.
`[06:03]` Now, by default, this skill allows your agent to suggest
`[06:06]` three high quality ideas, and of course, you can have more
`[06:09]` or you can also just let it go do its thing and select for you.
`[06:12]` But you can see here that for step two,
`[06:14]` it gave me some options for the hero animation.
`[06:16]` So this is pretty cool that it even gave us emojis to guide that.
`[06:19]` So one is Steam Rising, a single bowl of Tonkotsu ramen
`[06:22]` on a dark wooden counter. So that sounds good.
`[06:24]` There's also this option of, I guess, the ramen pouring
`[06:27]` an overhead ankle, rich golden broth being poured slowly
`[06:30]` into a dark ceramic bowl or this third option,
`[06:32]` the wide shot of an empty ramen bar counter.
`[06:35]` I think we'll either do number one or number two.
`[06:38]` So what we can actually do.
`[06:39]` Hey, so I think number one and number two are looking really good.
`[06:42]` I do want to feature a ramen that is shrimp based, though.
`[06:46]` So let's try that.
`[06:47]` And can you generate those images for me before we animate them into videos?
`[06:52]` And with that command, what it is now doing is to generate both images
`[06:55]` using nano banana. And similarly, if you're curious how to set that up,
`[06:59]` it's all just within this skill file as well.
`[07:01]` So if we go to step two scene generation,
`[07:03]` here is where we instructed it to suggest three concepts.
`[07:06]` And then to generate an image,
`[07:07]` we gave it this code to call on Google's APIs,
`[07:10]` which is how it accesses nano banana.
`[07:13]` And then later on, when we get those images,
`[07:15]` we will be animating them via cling 3.0.
`[07:17]` Now, the reason why we're using Google's APIs by default here is because
`[07:21]` for each Gmail account that you have,
`[07:23]` they actually give you a $300 welcome credit,
`[07:25]` which lasts you a long time, especially if you're just using
`[07:27]` their nano banana or video models.
`[07:29]` So when you set up this skill for the first time,
`[07:32]` that will also show you where to find your API keys
`[07:34]` that you can just provide your agent so that they're also able
`[07:37]` to tap into the nano banana models directly.
`[07:39]` Now, if you're curious how to develop this yourself
`[07:41]` and how to give your agent the skill to actually use nano banana,
`[07:45]` then what you can do is just provide your agent with this link,
`[07:48]` which is just all the documentation that Google has regarding nano banana
`[07:52]` and your agent will scour this page in order to find the right commands
`[07:55]` to use nano banana, nano banana 2 or nano banana pro.
`[07:59]` So if you want to replicate what I did,
`[08:00]` then this would be your master page.
`[08:02]` And you don't need to go through third party resellers like Higgsfield
`[08:05]` or FreePick for the same models.
`[08:06]` And you can see here that both images generated and open.
`[08:09]` So I just asked our agent to put them on the generations tab.
`[08:12]` And the tab is just here in our command center.
`[08:15]` So if you go to the generations tab, you can see here,
`[08:17]` it's basically a Google flow studio or Higgsfield equivalent,
`[08:21]` where I just connected my cloud code to this
`[08:23]` so that whenever I need to generate images or videos,
`[08:26]` I'll be able to display them visually here.
`[08:28]` I can also download them or if I click on it,
`[08:30]` that copies the path so that it's much easier to provide to our agents.
`[08:34]` But all right, so for our ramen shop,
`[08:36]` basically, you can see here that it created these two images,
`[08:40]` which is both looking quite good.
`[08:41]` But I think the one that we will go for would be this one,
`[08:44]` because I can just imagine this in the website to be looking really good.
`[08:48]` So what we'll do now is I'll just copy that,
`[08:51]` give that to our agent and I'll say, hey, this one looked really good.
`[08:55]` I think it's ready for animation.
`[08:57]` What I want you to do is animate it
`[08:59]` so that the ingredients settle into the ramen bowl
`[09:02]` and then the camera zooms in to the ramen to show the rich flavor of it.
`[09:06]` And for this one, let's actually try for it to do two videos
`[09:10]` just so that there's more optionality,
`[09:11]` because with a lot of these models, the more volume that you do,
`[09:14]` the sort of higher chances of winning that you have,
`[09:17]` and it's just the probabilistic nature of these.
`[09:19]` So you can see that what it is doing now is to use cling
`[09:22]` to animate the trim ramen,
`[09:24]` and that will basically happen just in the background.
`[09:26]` So you can see it's generating the scenes now,
`[09:28]` but if you're curious how that happens, going back to the skill once again,
`[09:31]` you can see that how the agent is accessing cling
`[09:33]` is through this website called wave speed.
`[09:35]` And wave speed is basically an AI model aggregator,
`[09:38]` sort of like Higgs field or free pick,
`[09:39]` but the difference is you don't need to pay like a monthly subscription
`[09:42]` to access these models.
`[09:43]` And apart from that, they also have a lot more models in place in here.
`[09:47]` So you can see if you just go and explore,
`[09:49]` you have the prime models here like nano banana,
`[09:51]` Sea Dream, et cetera, and also cling.
`[09:53]` There's other websites like file.ai or key.ai,
`[09:56]` but I think in terms of reliability, wave speed has been pretty good.
`[09:59]` So we are using them as well,
`[10:01]` but you have the optionality to use the others.
`[10:04]` Any case, so if you want to set this up by yourself,
`[10:06]` all you need to do is to find the model that you are after,
`[10:08]` at least for this build, what we are using is cling v3,
`[10:11]` image to video, and for our agent,
`[10:13]` what it's basically doing is calling on this model,
`[10:17]` uploading the images that it just created using nano banana,
`[10:19]` using Google's free credit,
`[10:21]` and also it writes the prompt here,
`[10:23]` and then it runs it to give us back that video.
`[10:25]` Now, if you want to equip your agent
`[10:27]` with the knowledge to understand how this works,
`[10:30]` all you need to do with a lot of these websites
`[10:32]` like wave speed, key.ai,
`[10:34]` is that you just need to copy the content here.
`[10:36]` And let's say you want to give that to your cloud code agent.
`[10:39]` If you copy that over,
`[10:40]` that will just provide all of the documentation
`[10:43]` around cling 3.0 pro.
`[10:44]` So that is basically what I did
`[10:46]` in order to give it that capability
`[10:48]` so that you don't need to type in your prompts
`[10:49]` and go to these websites like Google flow studio
`[10:52]` and other creative website equivalents.
`[10:54]` And so you can see here in the skill,
`[10:55]` we just standardized that
`[10:56]` and also gave a bit more control
`[10:58]` so that it knows exactly what it is that it needs to do.
`[11:01]` All right, so I think it's done with scene generation.
`[11:04]` And you can see it's saying here
`[11:05]` that those two videos are now in our generations tab.
`[11:08]` This one looked pretty cool.
`[11:10]` And this one, I think this one's better
`[11:12]` because there's a bit of a camera zoom effect in there.
`[11:16]` But for some reason,
`[11:17]` I think the camera is shaky on this one.
`[11:19]` So I'll probably actually just use this
`[11:21]` because it's a bit more consistent.
`[11:23]` So let's copy the path of that
`[11:25]` and I'll say, okay, this is the final video.
`[11:28]` Can you now go to step three and build out our website?
`[11:31]` And once we send that,
`[11:32]` you can see that it is now building that website for us.
`[11:35]` And just to show you under the hood
`[11:36]` what specifically this skill is invoking
`[11:38]` so that you understand how the agent is doing this,
`[11:40]` you can see under this step,
`[11:41]` there's rules around the architecture of the websites
`[11:44]` that it's building a lot of controls
`[11:45]` around the design system.
`[11:47]` And essentially what this is doing
`[11:48]` is it's codifying that effect
`[11:50]` where let's say you have that video,
`[11:51]` it will extract the individual frames of this video
`[11:54]` and map it to this scrolling action
`[11:56]` so that it gives that effect that as you scroll down,
`[11:58]` it runs through the frames for you.
`[12:00]` And so that whole thing has been codified
`[12:02]` in this skill already.
`[12:03]` The other thing that is part of this skill
`[12:05]` is this cinematic modules integration.
`[12:07]` And so if I scroll down here,
`[12:08]` you can see this particular site actually turned out well
`[12:11]` where it has this accordion elements in here, right?
`[12:14]` Which is really responsive, really professional.
`[12:16]` And the reason why it was able to do that
`[12:18]` is because of this cinematic module spec
`[12:20]` that we created in Robolabs as well.
`[12:22]` Now this one, because it is quite hard to recreate,
`[12:25]` we are giving it away for free.
`[12:26]` So you can just grab that in the description below,
`[12:28]` but this just gives you a lot of modular elements
`[12:30]` to enrich any website build that you have for your agents.
`[12:33]` So there's this one with a reveal text effect,
`[12:36]` modular components around future scrolling.
`[12:39]` This one has that kinetic text effect
`[12:40]` that you saw earlier, typewritten text effects,
`[12:43]` glitch effects like this one,
`[12:45]` image trails like the one that you saw here,
`[12:47]` flip cards that are pretty useful,
`[12:49]` I guess for testimonials and such,
`[12:50]` the flower animation that you saw earlier
`[12:52]` is basically just an SVG draw animation
`[12:55]` and several others in here that I think
`[12:57]` is going to help you a lot when you're coming up
`[12:59]` with website designs of your own.
`[13:00]` And there's 30 plus of these cinematic modules, by the way.
`[13:02]` So feel free to grab that below if that helps.
`[13:05]` But here you can see that the website is now done.
`[13:07]` So it gave us this landing page,
`[13:09]` and you can see this is really good.
`[13:11]` So you have the Japanese branding in there.
`[13:12]` And if we scroll down,
`[13:13]` that should animate the bowl nicely for us.
`[13:16]` So that look really well.
`[13:17]` And this scrolling animation that was coming
`[13:19]` from our cinematic modules as well.
`[13:21]` So it even included some Japanese characters in here.
`[13:23]` Let's actually translate that just to make sure
`[13:25]` that it's not putting something weird.
`[13:26]` So it says, there is a story in every cup.
`[13:29]` So I think that is pretty cool.
`[13:30]` And it even has the story, the menu, and so on.
`[13:34]` And it was even able to grab the address
`[13:35]` as well as the opening hours for us.
`[13:37]` So that is really nice.
`[13:39]` And you can see this is probably interactive.
`[13:41]` Yeah, there you go.
`[13:42]` So if I scroll down to the menu,
`[13:44]` to the hour story and visit,
`[13:45]` then that is all part of the website now,
`[13:49]` pretty much in one shot.
`[13:51]` And of course you can improve this further, right?
`[13:53]` So let's say, hey,
`[13:54]` so I actually want to add a section below,
`[13:58]` or at least have the menu use the accordion module,
`[14:01]` because I think that is a nice way to display the ramen bowls.
`[14:04]` Can you do that?
`[14:05]` And when I send that to the agent,
`[14:06]` it will understand what I'm saying,
`[14:08]` because remember in that skill,
`[14:09]` it gives it access to these cinematic modules.
`[14:11]` And the one that I'm talking about
`[14:12]` is this accordion slider,
`[14:14]` where if you look at this as a sample,
`[14:16]` that is the one where if I hover over each image,
`[14:19]` it expands and there is even an option
`[14:21]` to have a vertical variant.
`[14:23]` And here you can see that it is now doing that.
`[14:26]` And when it's done with that,
`[14:27]` we can check back on our site.
`[14:28]` And here, if we scroll down,
`[14:30]` you should now see the accordion fully built in there.
`[14:33]` And this looks really good
`[14:34]` and definitely more professional than what we started with.
`[14:37]` So now if we head to step four,
`[14:39]` this will be a simple matter for our agent,
`[14:42]` because what it is going to do
`[14:45]` is to just deploy that to Vercel.
`[14:46]` And basically Vercel is a service
`[14:48]` that hosts websites for you.
`[14:50]` And they actually do this for free, which is really good.
`[14:52]` And for you to equip your agent with this knowledge,
`[14:55]` all you need to do, once again,
`[14:56]` is to give your agent the documentation for Vercel,
`[14:59]` and they'll be able to do exactly what it did here.
`[15:01]` And so here you can see that it is now live
`[15:04]` at this website,
`[15:05]` and you can send that to your client
`[15:06]` as a demo site that people can visit
`[15:08]` and also provide some feedback on.
`[15:11]` So that's looking really good.
`[15:12]` And just to recap,
`[15:12]` we went from this, which is practically not even a website,
`[15:16]` it's just a booking form,
`[15:17]` into this, which has a cinematic background,
`[15:19]` a much more rich experience for the users of this website,
`[15:23]` and is definitely more premium versus how we started.
`[15:27]` And there you have it, that is the full agent pipeline,
`[15:29]` where you give it a website, it analyzes the brand,
`[15:31]` generates the scenes, builds the website,
`[15:33]` and even deploys it online.
`[15:35]` Now, if you need the 31 module cinematic pack,
`[15:37]` that's available free for everyone just in our network,
`[15:40]` so you can grab that.
`[15:41]` And for this full cinematic website,
`[15:43]` you can get that inside the RoboNuggets community.
`[15:46]` I hope that was helpful.
`[15:47]` And if it is, then consider subscribing
`[15:49]` because that helps us a lot
`[15:50]` to put out more educational content like this.
`[15:52]` And if you want to understand further
`[15:53]` how I'm running cloud code as a 24 seven AI assistant,
`[15:56]` then you can watch this video next.
`[15:58]` I'll see you guys next time.
`[15:58]` Thank you.
