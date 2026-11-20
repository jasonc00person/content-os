# How I Turned Claude Into My Personal Assistant (Full Guide)

- **Source:** https://www.youtube.com/watch?v=CvLkhGWZlvE
- **Uploader:** AI Edge
- **Uploaded:** 2026-05-14
- **Duration:** 18:08
- **Method:** YouTube captions (no transcription needed)

## Transcript

I spent two weeks building a custom personal operating system which runs my life. It manages all my tasks, finances, calendar, and automatically prioritizes my day based on the things that matter. It allows me to send voice notes from anywhere and have AI automatically populate my to-do list instead of what I used to do which was going into notion and having to manually log everything. And for me, that system just didn't work. Needing to constantly remember to go into notion and write something meant that things weren't getting logged, so things were getting missed. I had deals falling through, for example, an opportunity to invest in Anthropic, the creators of Claude, in May 2025, which ended up costing me over $1.2 million in opportunity cost because I just wasn't organized. So, I knew I needed to do something once and for all. So, over the past couple of weeks, I really spent the time to create the best operating system I could. And I've got to say, this has been by far the biggest upgrade that I have ever made to my life using AI. It has a custom cloud memory system, so it remembers everything about me. That memory system can be transported into any LLM, and I can constantly update the front end based on my interests and priorities, whilst the back end stores all the data. I truly believe when moving away from the SaaS era, the era where you pay a subscription to use a tool which is built for everyone, and into an era of purpose-built tools, an exact dashboard that matches your specific pain points. And today, I'm going to show you how I built mine and how you can build your very own. So, if you don't know who I am, my name is Miles Deutscher, the founder of AI Edge. I've scaled my AI agency to over $20 million in revenue. I've sold over $5.5 million of digital products, and I created this channel to help you achieve your goals with AI just as I've been able to achieve some of mine with this incredible new technology. So, if you enjoy content like this, make sure you click that subscribe button so you don't miss a single video. Now, before I show you how I built the OS from scratch, let me quickly show you some of the things that it can do. And then at the end of the video, I'll give you a full walk-through as to how I've laid out my dashboard. All right, so firstly, and this is probably the coolest part about it and it solved the biggest pain points that other task management systems like Notion couldn't solve, I can voice note from anywhere. So, I have a Telegram chat where I can send it a voice note when a new task comes up. So, let's say in my head I remember, "Oh, I have a new proposal to send a client." I can simply just open up Telegram, which I've conveniently made the action button on my phone, so I can just click a button, it opens up Telegram and I just voice note exactly what I want to log into the CRM system. Then, I've configured a back-end memory system where that is sent to the cloud through Whisper. It connects to my memory database on Superbase. The AI automatically categorizes it in terms of priority and it populates it on the dashboard. So, the dashboard is the front-end reflecting the memory system in the back-end. So, whenever I have an idea, a thought, something I need to do, I simply paste it or voice prompt into Telegram and it automatically updates and prioritizes my task management system. If you don't have a system like this, you're literally reliant on opening up the Notion app or opening up your Apple notes or wherever you store tasks, writing it in manually, and then you have to click and drag and manually reorder things when you want to sort by priority. That wasn't working for me because then my to-do list just ended up being a 200 long list that I would never get to because new things would go to the top and then I'd forget other things. This way, things are always organized automatically by the AI. The next thing that was a real pain point for me was finances because I used to have my finances all over the place. I had bank accounts, I had exchanges, I had other documents all over the place. So, what I did is I created a Google Sheet with an API to pull in the data live that reflects on the dashboard. So, on the dashboard I can see at any moment in time what my exact net worth is. Now, of course, the data I'm showing you in today's video has been slightly changed so you don't see the real numbers, but it's exactly how my real dashboard looks. So, I'm going to walk you through the whole thing, but firstly, let's go through step by step how I actually built it because this is the real source. All right, so the first thing I did is mock the entire design in Claude design. So, before I committed to the full build on Claude code, I wanted to see exactly how it would look. I honestly spent way too long on this going through all the mocks for all the different sections, but I think it came out super cool. And my plan is to make it better over time. So, once I was happy with the design, I exported it into Claude code. This is how you actually take it from a design into a functional website. And I got Claude code to mock the entire architecture, which will be available for you to claim for free below. If you click the link in the description, become a member of the AI Edge newsletter, you'll get access to our Instagram community. Or in the pin drive, you'll be able to find the full architecture. And then you can take that PDF, put it into Claude code yourself, and it will run you through the exact steps. Because it took me days to figure out the exact architecture for this and many, many mistakes. So, hopefully, it's able to save you time when you build your own. So, the next step for me was to pick a memory system. I decided to go with Superbase. You also have Firebase and other solutions, Super memory as well, but Superbase was the most sovereign configuration. Lots of big applications use it. It's basically the brain behind everything. So, all the data gets stored and logged on Superbase, and then the interface is how you interact with that memory. Then I needed to go to Anthropic, get an API key, because I built this on Claude. I actually think you could build this on Codex. The only reason I built it on Claude is cuz I started this build before 5.5 was released. But if you're building today, you can do this exact same thing on ChatGPT. And to be honest, I think it would do a better job. And you can still import the Claude design. The next thing I did is I wrote the schema, so exactly what I wanted in there, content, products, business ops, business finance, etc. This is going to be completely custom to you, but my build is what I wanted. Then, I wanted a way to log my tasks via voice prompting when I wasn't on my computer. So, I decided to connect Telegram, which was really easy, because I just set up a Telegram bot through Bot Father. I pointed its webhook at the Versal function through Claude code, and now basically all my voice notes get transcribed by OpenAI Whisper. So, Claude can read the text and classify it into the corresponding category and log it on Superbase. This is absolutely amazing. Then I worked on some security stuff to make sure it was password protected before I moved on to the actual component. So, first I did the calendar. I basically connected Google Calendar so it refreshes live. Then I built the habit tracking. This is pretty simple. Whenever you check all of the boxes under a drop down, it ticks off a task for the day. Then added the journaling function, then added the CRM, which was by far the hardest part because I just had so many glitches which were honestly really frustrating where, you know, I'd refresh, data wouldn't log, and things were getting lost. So, I had to go through multiple debugging stages to make sure it actually worked. So, just keep this in mind if you're going to build this yourself, you might get some bugs, and I spent hours doing this. The entire build took me a couple of weeks. So, this was over a few different days. Then I added nutrition, which I also had to rebuild a few times because the data wasn't logging properly, but now it's pretty good, and it's actually connected to a smart AI algorithm which can estimate the calories of a particular meal. Added the health tab corresponding to the data. Added the goals section so I could see my goals, and then I created the finance section. The finance section I had to connect to a Google Sheet, which I'm going to do a future video on finances more in depth because it deserves its own video. And then for the last couple of days, I basically just used it, and every single time I noticed a feature that I wanted added, I added it. And every single time there was an issue with the feature, I got it fixed. So, this is really a process of trial and error. The sooner you start using it, the sooner you'll realize things that you want to tweak. All right, so now you know how I built it. Here is the dashboard. I'm going to give you a full run through, and then I'm going to show you some examples of how I use it. In the top left, it's got me. I'm the operator, obviously for you, it'll have your own name. One block down, it has a finance pulse. It's actually hidden by default, so if you leave your computer open, you're not going to leak your network to someone. But when you want to review it, you can click reveal. This tracks my net worth over time, how much I've made in the month, how much I've made on the day, and what my current net worth is, and this is connected to all of the data on the back end. Then down here, I have key tasks. These are the tasks that I've starred and flagged as key priorities for the day. Really, productivity a lot of the time just comes down to identifying the top task for the day and making sure you get those tasks done. So, what I do every morning is I go through the CRM section of the dashboard, and then I simply select I star the three to five things I want to get done every day. And then if you go back into the home section, these are marked down as key items. So, these are the things that I need to complete as priorities every day. And obviously, once I complete them, then I can go and add new tasks in, but this gives me a bit of a pulse on the main things that I need to hit. Now, in the middle, this is a really powerful system and maybe you watch my other habit tracker video. This is the next step further from that. I have my daily habits. So, these are the things that aside from the main priorities I want to get done, I need to do every day. So, there are a few habits that I like doing. For example, I need to go to the gym every day to feel good. So, once it's done, I tick it off. Then, I need to remember to take my supplements. This just takes the brain power out of needing to remember to do things. I've actually changed the data cuz I didn't want to reveal my personal data, but you'd list basically every single one of your sub supplements here and you would tick it off like this, 1 2 3. When you tick off all the sub tasks, the main task gets completed and it shows you the percentage of your habits that you've completed for the day. The next thing that's really important for me is my creative session. So, I have a process I follow every day in the morning where I go through X, I do market research, and then I come up with ideas. I find it's really important to be creative in the morning. So, once I tick off all the sub tasks, then the creative session gets complete. Then I move on to a community session to engage with my community. Then I move on to a finance check. Well, have a few things that I tick off like run through my portfolio, quickly look for risks, go through the finance section of the dashboard, and then finally I have an evening wind down routine. Now, in the wind down routine, this is really cool. There's actually a journaling feature, and you can do this through the Telegram interface as well. But if you click the microphone, you can actually just speak what happened in the day. So, I basically say, "I had a good day. I did this, this, and this. This is where I struggled. This is where I did well. These are the reasons why. This is how the business is going." And this is actually really powerful because remember, all of this data is being saved in the back end. So, by doing this, I essentially I'm training the AI every single day on how I think. So, if you go to the journaling section where all of this is logged, it has a summary of every single day. And if you click show raw, it shows the full transcript that you left for that day. So, imagine after a year of doing this, you have a year worth of logs. The AI is really smart at pattern recognition. It might be able to say when you don't get enough sleep, you tend to not be as productive. So, maybe focus on this first so you can solve this. Or it might say, you know, you constantly identify loneliness as an issue in your life. Maybe you should address it through this, this, and this. Like, just patterns that you might even not realize you're bringing up in your speech. The AI can basically act as a psychologist or a mentor and coach you through solving some of these patterns. So, the journaling process every single day, I think it's so crucial. And it also trains the AI on you, what your days look like, what you get up to, what you do. And because all this memory is being stored, you actually have a transportable system. So, if you do speak with ChatGPT, if you do speak with Claude, you can plug in this system into Claude code or Codex. And every single time you prompt, ask for personal advice, ask for business strategy, it has your exact context in a memory system that you own. Versus what happens if you just speak to the chat normally, basically your memory is in a black box. So, you don't know what ChatGPT knows about you. It does remember some stuff, but you don't have control over that memory system. So, this solves the memory system once and for all. Cuz let's be honest, you can redesign this dashboard. You can always create a new dashboard. There's probably going to be better design applications for me to make this even better in the future. But that's not the real source. The real source here is the back end memory system that we've built on Superbase. And then you can just apply this to any front end you want in the future. That's the real real magic here. And a couple of other things which are specific to me. And remember, in your own custom builds, you can change this. You know, you might not care about nutrition, but for me, I actually like logging my meals. So, when I eat a meal, I log it. It shows me what time I ate that meal, and it shows me the calories of that meal. So, chicken and rice, 550 calories. It's connected to the latest Claude model, so it can estimate. You can also give it more details. You can even send a photo into Telegram if you want to actually photograph your meal. It's basically like having Cal AI built into the dashboard. And then I could see, you know, my protein for the day, my nutrition, how many calories I have left. And this also gets logged under the health section of the dashboard, where it shows my daily protein intake, calorie intake every single day. Uh so, I can make sure, you know, I'm eating right. And you can actually go a step further. You could connect this to your wearable like Oura Ring or Whoop, and actually import the data, and then have it weighed against other metrics. I haven't done that step yet, but this is the architecture you can build upon. Like, essentially, the goal here is to build an operating system that controls your life or has your entire life summarized here. Now, there are some things that I keep off the app. Like, for example, I still do keep big picture stuff on Notion. So, big picture goals, my compliance setups, my company roster, and just general information that doesn't change much. I'll keep somewhere else cuz I want to make sure I have that data. But, basically, for anything else, any active task, I keep it on the application. I also have a system where things automatically get backed up. So, if for some reason Claude deletes all the data, it's actually backed up in Superbase, and archived, and stored. So, you don't need to worry about losing data. You can always re-export. The full guide to this, once again, is going to be in the description below. It's in my Instagram community. You can access it by signing up to the newsletter, and that's going to have the full prompt that you can take and put into Claude code yourself or Codex, which is to be honest, probably the better coding model, but I did this on Claude code beforehand. And it's going to run you step-by-step through my process because, honestly, this video would be hours and hours and hours if I went through every single little finicky thing that I had to fix to build this. If you like this video, let me know in the comments below. I can actually do a follow-up where I go in depth on specific elements of the dashboard, but I wanted to show you what I've been building and working on in this video and give you an overview. And then it connects to my Google Calendar below. You can actually edit it directly from here. I still like using Google Calendar though. I just like having this open all day, so I have it on a screen on my computer so I can see what upcoming meetings I have. I'm constantly referring back to it. And then the top right-hand corner I have some goals for the week, for the month. They actually store and there's a list here. Usually I'll just have three to five goals for a month so I can see right, I want to ship a product, I want to get out 20 videos, I want to go to the gym every day. And then I have all the goals there so I'm constantly reminded and I'm just aware every single day of what I'm actually working towards which I think is so powerful because if it's not in front of you every day, you're actually just going to forget. So this way I'm actually forced to stick to the things that I want to do. Going into the CRM system, you can actually drag things around in terms of priorities. You can tick things off once you do them and they'll automatically get sent to the archive section. I continuously improve this over time but it's basically in my opinion a better version of the Notion task management system. I will say there were a lot of glitches, there still are from time to time, but every time there is a bug, I fix it and then over the last few days I've found I've had less and less bugs. You're just going to have to be aware that if you're going to build your own OS because you don't have thousands of engineers like Notion who over time have fixed a lot of their issues, you're going to run into your own. But because it's custom built, that trade-off becomes a pro because you can build it exactly how you want to build it. I can also switch to the Kanban view just like Notion so I can actually drag things along from this week to today to this month so I can have an overview of all my tasks. And if you go into the brain section of the application, it actually opens up a view where you can view the current status on different elements of your life. So legal, personal finance, content, products, opsec, business opportunities. If you click on one, it'll actually bring up all of the tasks underneath this category and then you can actually leave notes here or links here just like you can in Notion pages so you can easily refer back to it. And it also has a summary of the key things within each category. Like there might be some clear security risks that you're taking on. So there might be key life admin things that you need to fix that will be highlighted here in the summary as things that you need to do. And the best part is because you have all of this in a memory system, you can simply prompt the AI and ask, "Look, what are the top three things right now that if you were a strategic CEO or consultant, you would recommend that I need to do right now?" And it will actually be able to go through hundreds or thousands of entries and look at the few things which are actually going to move the needle for you or your business, which I think is really important. The finance section I'm not going to get into in today's video because honestly, it's its own video and I'm going to do a follow-up, so make sure you subscribe. But of course, remember you can tweak this any way that you want. The world is your oyster with AI. This is just what I found impactful for my V1 build, but I'm going to keep improving this over time as things change. And also, I have room to add more things. I just didn't want to clutter my dashboard too much in the early days. All right, now let me give you a quick practical example of how I use this in my daily life. So basically, this is how I use this setup. So I have three monitors. You don't need three monitors for this. If you're on your laptop, you can just have three different desktops. So this is just how I operate in my daily life. On my left-hand screen here, I have the dashboard open at all times, then I get to see what my upcoming meetings are, everything that I need to see, and then I work on the middle screen. So I'm doing work, writing tweets, reviewing proposals, taking meetings, whatever I'm doing on the middle screen, and then on the left, I'll just glance over and make sure that my day is in order. Then on the right-hand side, I have Claude open. This is Claude Codor, you know, the normal Claude app if I'm chatting there. And then I have GPT open as well. So I have my two AIs. If I ever need to make tweaks on Claude Codor to the dashboard, I can just do it up here and I just have these open all day, you know, in case I need them. And then, when I need to enter something, so a new task comes up, let's say I get a message from someone I need to do something, I just add it here so I can quickly capture it. I also have Whisper on my computer so I can use the command and it basically records audio for me if I just want to speak it. If not, I'll just type it in. If I'm on the go or, you know, if I'm just doing something on my phone, then it's actually easier for me to hit the action button and then voice prompt into Telegram. And when I voice prompt, it auto-populates in the CRM over here anyway. And the other thing that I do a lot, especially when I'm out, is I actually use the weather app. So, I've created a mobile version which I'm optimizing to be even better for mobile. So, I can do this on the go and it's connected to the same memory system. So, you don't even need your computer. That's basically how I use it in my day-to-day life. Thank you guys so much for watching this video. This was a really intense build to put together, but I'm so glad I went through this process because I think it's going to be a part of my life for many months and hopefully years to come. I'm just going to keep upgrading this over time and I'm going to keep making videos on it. So, if you enjoyed this, make sure to subscribe. Obviously, the full prompt is available down below to help you build your own. It is going to take a bit of time, but it's definitely worth it because I honestly think having a system like this can make me millions of dollars and can make me a 10x more productive human because it's custom-built for exactly what I need. Thank you guys for watching. I'll see you in the next one. Peace out.

## Timestamped

`[00:02]` I spent two weeks building a custom
`[00:02]` personal operating system which runs my
`[00:05]` life. It manages all my tasks, finances,
`[00:08]` calendar, and automatically prioritizes
`[00:10]` my day based on the things that matter.
`[00:12]` It allows me to send voice notes from
`[00:14]` anywhere and have AI automatically
`[00:16]` populate my to-do list instead of what I
`[00:18]` used to do which was going into notion
`[00:20]` and having to manually log everything.
`[00:21]` And for me, that system just didn't
`[00:23]` work. Needing to constantly remember to
`[00:24]` go into notion and write something meant
`[00:26]` that things weren't getting logged, so
`[00:28]` things were getting missed. I had deals
`[00:30]` falling through, for example, an
`[00:31]` opportunity to invest in Anthropic, the
`[00:33]` creators of Claude, in May 2025, which
`[00:36]` ended up costing me over $1.2 million in
`[00:39]` opportunity cost because I just wasn't
`[00:41]` organized. So, I knew I needed to do
`[00:42]` something once and for all. So, over the
`[00:44]` past couple of weeks, I really spent the
`[00:46]` time to create the best operating system
`[00:48]` I could. And I've got to say, this has
`[00:50]` been by far the biggest upgrade that I
`[00:52]` have ever made to my life using AI. It
`[00:55]` has a custom cloud memory system, so it
`[00:57]` remembers everything about me. That
`[00:59]` memory system can be transported into
`[01:01]` any LLM, and I can constantly update the
`[01:03]` front end based on my interests and
`[01:05]` priorities, whilst the back end stores
`[01:08]` all the data. I truly believe when
`[01:09]` moving away from the SaaS era, the era
`[01:12]` where you pay a subscription to use a
`[01:13]` tool which is built for everyone, and
`[01:16]` into an era of purpose-built tools, an
`[01:18]` exact dashboard that matches your
`[01:20]` specific pain points. And today, I'm
`[01:22]` going to show you how I built mine and
`[01:23]` how you can build your very own. So, if
`[01:25]` you don't know who I am, my name is
`[01:27]` Miles Deutscher, the founder of AI Edge.
`[01:29]` I've scaled my AI agency to over $20
`[01:31]` million in revenue. I've sold over $5.5
`[01:33]` million of digital products, and I
`[01:35]` created this channel to help you achieve
`[01:37]` your goals with AI just as I've been
`[01:38]` able to achieve some of mine with this
`[01:40]` incredible new technology. So, if you
`[01:42]` enjoy content like this, make sure you
`[01:44]` click that subscribe button so you don't
`[01:45]` miss a single video. Now, before I show
`[01:47]` you how I built the OS from scratch, let
`[01:50]` me quickly show you some of the things
`[01:52]` that it can do. And then at the end of
`[01:53]` the video, I'll give you a full
`[01:55]` walk-through as to how I've laid out my
`[01:57]` dashboard. All right, so firstly, and
`[01:59]` this is probably the coolest part about
`[02:01]` it and it solved the biggest pain points
`[02:02]` that other task management systems like
`[02:04]` Notion couldn't solve, I can voice note
`[02:06]` from anywhere. So, I have a Telegram
`[02:07]` chat where I can send it a voice note
`[02:10]` when a new task comes up. So, let's say
`[02:11]` in my head I remember, "Oh, I have a new
`[02:13]` proposal to send a client." I can simply
`[02:15]` just open up Telegram, which I've
`[02:17]` conveniently made the action button on
`[02:18]` my phone, so I can just click a button,
`[02:20]` it opens up Telegram and I just voice
`[02:22]` note exactly what I want to log into the
`[02:24]` CRM system. Then, I've configured a
`[02:26]` back-end memory system where that is
`[02:28]` sent to the cloud through Whisper. It
`[02:30]` connects to my memory database on
`[02:31]` Superbase. The AI automatically
`[02:33]` categorizes it in terms of priority and
`[02:36]` it populates it on the dashboard. So,
`[02:38]` the dashboard is the front-end
`[02:40]` reflecting the memory system in the
`[02:41]` back-end. So, whenever I have an idea, a
`[02:43]` thought, something I need to do, I
`[02:45]` simply paste it or voice prompt into
`[02:47]` Telegram and it automatically updates
`[02:50]` and prioritizes my task management
`[02:51]` system. If you don't have a system like
`[02:53]` this, you're literally reliant on
`[02:55]` opening up the Notion app or opening up
`[02:57]` your Apple notes or wherever you store
`[02:58]` tasks, writing it in manually, and then
`[03:00]` you have to click and drag and manually
`[03:02]` reorder things when you want to sort by
`[03:04]` priority. That wasn't working for me
`[03:05]` because then my to-do list just ended up
`[03:07]` being a 200 long list that I would never
`[03:10]` get to because new things would go to
`[03:12]` the top and then I'd forget other
`[03:13]` things. This way, things are always
`[03:15]` organized automatically by the AI. The
`[03:17]` next thing that was a real pain point
`[03:18]` for me was finances because I used to
`[03:20]` have my finances all over the place. I
`[03:22]` had bank accounts, I had exchanges, I
`[03:24]` had other documents all over the place.
`[03:26]` So, what I did is I created a Google
`[03:28]` Sheet with an API to pull in the data
`[03:30]` live that reflects on the dashboard. So,
`[03:33]` on the dashboard I can see at any moment
`[03:35]` in time what my exact net worth is. Now,
`[03:37]` of course, the data I'm showing you in
`[03:38]` today's video has been slightly changed
`[03:40]` so you don't see the real numbers, but
`[03:42]` it's exactly how my real dashboard
`[03:44]` looks. So, I'm going to walk you through
`[03:45]` the whole thing, but firstly, let's go
`[03:47]` through step by step how I actually
`[03:48]` built it because this is the real
`[03:50]` source. All right, so the first thing I
`[03:52]` did is mock the entire design in Claude
`[03:54]` design. So, before I committed to the
`[03:56]` full build on Claude code, I wanted to
`[03:57]` see exactly how it would look. I
`[03:59]` honestly spent way too long on this
`[04:01]` going through all the mocks for all the
`[04:03]` different sections, but I think it came
`[04:04]` out super cool. And my plan is to make
`[04:06]` it better over time. So, once I was
`[04:08]` happy with the design, I exported it
`[04:10]` into Claude code. This is how you
`[04:12]` actually take it from a design into a
`[04:14]` functional website. And I got Claude
`[04:16]` code to mock the entire architecture,
`[04:18]` which will be available for you to claim
`[04:20]` for free below. If you click the link in
`[04:21]` the description, become a member of the
`[04:23]` AI Edge newsletter, you'll get access to
`[04:25]` our Instagram community. Or in the pin
`[04:26]` drive, you'll be able to find the full
`[04:28]` architecture. And then you can take that
`[04:29]` PDF, put it into Claude code yourself,
`[04:31]` and it will run you through the exact
`[04:33]` steps. Because it took me days to figure
`[04:35]` out the exact architecture for this and
`[04:36]` many, many mistakes. So, hopefully, it's
`[04:38]` able to save you time when you build
`[04:39]` your own. So, the next step for me was
`[04:41]` to pick a memory system. I decided to go
`[04:42]` with Superbase. You also have Firebase
`[04:44]` and other solutions, Super memory as
`[04:46]` well, but Superbase was the most
`[04:47]` sovereign configuration. Lots of big
`[04:50]` applications use it. It's basically the
`[04:51]` brain behind everything. So, all the
`[04:53]` data gets stored and logged on
`[04:54]` Superbase, and then the interface is how
`[04:56]` you interact with that memory. Then I
`[04:58]` needed to go to Anthropic, get an API
`[05:00]` key, because I built this on Claude. I
`[05:03]` actually think you could build this on
`[05:04]` Codex. The only reason I built it on
`[05:05]` Claude is cuz I started this build
`[05:07]` before 5.5 was released. But if you're
`[05:09]` building today, you can do this exact
`[05:11]` same thing on ChatGPT. And to be honest,
`[05:13]` I think it would do a better job. And
`[05:15]` you can still import the Claude design.
`[05:16]` The next thing I did is I wrote the
`[05:17]` schema, so exactly what I wanted in
`[05:20]` there, content, products, business ops,
`[05:21]` business finance, etc. This is going to
`[05:23]` be completely custom to you, but my
`[05:25]` build is what I wanted. Then, I wanted a
`[05:27]` way to log my tasks via voice prompting
`[05:30]` when I wasn't on my computer. So, I
`[05:31]` decided to connect Telegram, which was
`[05:33]` really easy, because I just set up a
`[05:34]` Telegram bot through Bot Father. I
`[05:36]` pointed its webhook at the Versal
`[05:38]` function through Claude code, and now
`[05:39]` basically all my voice notes get
`[05:41]` transcribed by OpenAI Whisper. So,
`[05:43]` Claude can read the text and classify it
`[05:45]` into the corresponding category and log
`[05:47]` it on Superbase. This is absolutely
`[05:48]` amazing. Then I worked on some security
`[05:50]` stuff to make sure it was password
`[05:51]` protected before I moved on to the
`[05:53]` actual component. So, first I did the
`[05:55]` calendar. I basically connected Google
`[05:57]` Calendar so it refreshes live. Then I
`[05:59]` built the habit tracking. This is pretty
`[06:01]` simple. Whenever you check all of the
`[06:02]` boxes under a drop down, it ticks off a
`[06:04]` task for the day. Then added the
`[06:06]` journaling function, then added the CRM,
`[06:08]` which was by far the hardest part
`[06:09]` because I just had so many glitches
`[06:11]` which were honestly really frustrating
`[06:13]` where, you know, I'd refresh, data
`[06:14]` wouldn't log, and things were getting
`[06:16]` lost. So, I had to go through multiple
`[06:17]` debugging stages to make sure it
`[06:19]` actually worked. So, just keep this in
`[06:20]` mind if you're going to build this
`[06:21]` yourself, you might get some bugs, and I
`[06:23]` spent hours doing this. The entire build
`[06:25]` took me a couple of weeks. So, this was
`[06:26]` over a few different days. Then I added
`[06:28]` nutrition, which I also had to rebuild a
`[06:30]` few times because the data wasn't
`[06:31]` logging properly, but now it's pretty
`[06:33]` good, and it's actually connected to a
`[06:35]` smart AI algorithm which can estimate
`[06:37]` the calories of a particular meal. Added
`[06:39]` the health tab corresponding to the
`[06:40]` data. Added the goals section so I could
`[06:43]` see my goals, and then I created the
`[06:45]` finance section. The finance section I
`[06:47]` had to connect to a Google Sheet, which
`[06:49]` I'm going to do a future video on
`[06:50]` finances more in depth because it
`[06:52]` deserves its own video. And then for the
`[06:53]` last couple of days, I basically just
`[06:55]` used it, and every single time I noticed
`[06:57]` a feature that I wanted added, I added
`[06:59]` it. And every single time there was an
`[07:00]` issue with the feature, I got it fixed.
`[07:02]` So, this is really a process of trial
`[07:04]` and error. The sooner you start using
`[07:05]` it, the sooner you'll realize things
`[07:07]` that you want to tweak. All right, so
`[07:08]` now you know how I built it. Here is the
`[07:10]` dashboard. I'm going to give you a full
`[07:11]` run through, and then I'm going to show
`[07:13]` you some examples of how I use it. In
`[07:14]` the top left, it's got me. I'm the
`[07:15]` operator, obviously for you, it'll have
`[07:17]` your own name. One block down, it has a
`[07:19]` finance pulse. It's actually hidden by
`[07:21]` default, so if you leave your computer
`[07:22]` open, you're not going to leak your
`[07:23]` network to someone. But when you want to
`[07:24]` review it, you can click reveal. This
`[07:26]` tracks my net worth over time, how much
`[07:28]` I've made in the month, how much I've
`[07:30]` made on the day, and what my current net
`[07:31]` worth is, and this is connected to all
`[07:33]` of the data on the back end. Then down
`[07:35]` here, I have key tasks. These are the
`[07:37]` tasks that I've starred and flagged as
`[07:40]` key priorities for the day. Really,
`[07:41]` productivity a lot of the time just
`[07:43]` comes down to identifying the top task
`[07:46]` for the day and making sure you get
`[07:47]` those tasks done. So, what I do every
`[07:48]` morning is I go through the CRM section
`[07:50]` of the dashboard, and then I simply
`[07:52]` select I star the three to five things I
`[07:55]` want to get done every day. And then if
`[07:57]` you go back into the home section, these
`[07:59]` are marked down as key items. So, these
`[08:01]` are the things that I need to complete
`[08:02]` as priorities every day. And obviously,
`[08:04]` once I complete them, then I can go and
`[08:05]` add new tasks in, but this gives me a
`[08:08]` bit of a pulse on the main things that I
`[08:10]` need to hit. Now, in the middle, this is
`[08:12]` a really powerful system and maybe you
`[08:13]` watch my other habit tracker video. This
`[08:15]` is the next step further from that. I
`[08:17]` have my daily habits. So, these are the
`[08:19]` things that aside from the main
`[08:20]` priorities I want to get done, I need to
`[08:22]` do every day. So, there are a few habits
`[08:24]` that I like doing. For example, I need
`[08:25]` to go to the gym every day to feel good.
`[08:27]` So, once it's done, I tick it off. Then,
`[08:29]` I need to remember to take my
`[08:30]` supplements. This just takes the brain
`[08:32]` power out of needing to remember to do
`[08:33]` things. I've actually changed the data
`[08:35]` cuz I didn't want to reveal my personal
`[08:37]` data, but you'd list basically every
`[08:39]` single one of your sub supplements here
`[08:40]` and you would tick it off like this, 1 2
`[08:42]` 3. When you tick off all the sub tasks,
`[08:43]` the main task gets completed and it
`[08:45]` shows you the percentage of your habits
`[08:47]` that you've completed for the day. The
`[08:48]` next thing that's really important for
`[08:50]` me is my creative session. So, I have a
`[08:52]` process I follow every day in the
`[08:54]` morning where I go through X, I do
`[08:56]` market research, and then I come up with
`[08:57]` ideas. I find it's really important to
`[08:59]` be creative in the morning. So, once I
`[09:01]` tick off all the sub tasks, then the
`[09:03]` creative session gets complete. Then I
`[09:05]` move on to a community session to engage
`[09:07]` with my community. Then I move on to a
`[09:08]` finance check. Well, have a few things
`[09:11]` that I tick off like run through my
`[09:12]` portfolio, quickly look for risks, go
`[09:14]` through the finance section of the
`[09:15]` dashboard, and then finally I have an
`[09:17]` evening wind down routine. Now, in the
`[09:19]` wind down routine, this is really cool.
`[09:21]` There's actually a journaling feature,
`[09:22]` and you can do this through the Telegram
`[09:24]` interface as well. But if you click the
`[09:25]` microphone, you can actually just speak
`[09:27]` what happened in the day. So, I
`[09:27]` basically say, "I had a good day. I did
`[09:29]` this, this, and this. This is where I
`[09:31]` struggled. This is where I did well.
`[09:33]` These are the reasons why. This is how
`[09:34]` the business is going." And this is
`[09:36]` actually really powerful because
`[09:38]` remember, all of this data is being
`[09:39]` saved in the back end. So, by doing
`[09:41]` this, I essentially I'm training the AI
`[09:44]` every single day on how I think. So, if
`[09:46]` you go to the journaling section where
`[09:48]` all of this is logged, it has a summary
`[09:50]` of every single day. And if you click
`[09:52]` show raw, it shows the full transcript
`[09:55]` that you left for that day. So, imagine
`[09:57]` after a year of doing this, you have a
`[09:58]` year worth of logs. The AI is really
`[10:00]` smart at pattern recognition. It might
`[10:02]` be able to say when you don't get enough
`[10:04]` sleep, you tend to not be as productive.
`[10:06]` So, maybe focus on this first so you can
`[10:07]` solve this. Or it might say, you know,
`[10:09]` you constantly identify loneliness as an
`[10:11]` issue in your life. Maybe you should
`[10:12]` address it through this, this, and this.
`[10:14]` Like, just patterns that you might even
`[10:15]` not realize you're bringing up in your
`[10:17]` speech. The AI can basically act as a
`[10:19]` psychologist or a mentor and coach you
`[10:22]` through solving some of these patterns.
`[10:24]` So, the journaling process every single
`[10:25]` day, I think it's so crucial. And it
`[10:27]` also trains the AI on you, what your
`[10:29]` days look like, what you get up to, what
`[10:31]` you do. And because all this memory is
`[10:32]` being stored, you actually have a
`[10:34]` transportable system. So, if you do
`[10:36]` speak with ChatGPT, if you do speak with
`[10:38]` Claude, you can plug in this system into
`[10:41]` Claude code or Codex. And every single
`[10:43]` time you prompt, ask for personal
`[10:45]` advice, ask for business strategy, it
`[10:47]` has your exact context in a memory
`[10:49]` system that you own. Versus what happens
`[10:52]` if you just speak to the chat normally,
`[10:54]` basically your memory is in a black box.
`[10:55]` So, you don't know what ChatGPT knows
`[10:57]` about you. It does remember some stuff,
`[10:59]` but you don't have control over that
`[11:00]` memory system. So, this solves the
`[11:02]` memory system once and for all. Cuz
`[11:03]` let's be honest, you can redesign this
`[11:05]` dashboard. You can always create a new
`[11:06]` dashboard. There's probably going to be
`[11:07]` better design applications for me to
`[11:09]` make this even better in the future. But
`[11:11]` that's not the real source. The real
`[11:12]` source here is the back end memory
`[11:14]` system that we've built on Superbase.
`[11:16]` And then you can just apply this to any
`[11:18]` front end you want in the future. That's
`[11:20]` the real real magic here. And a couple
`[11:21]` of other things which are specific to
`[11:23]` me. And remember, in your own custom
`[11:24]` builds, you can change this. You know,
`[11:26]` you might not care about nutrition, but
`[11:27]` for me, I actually like logging my
`[11:29]` meals. So, when I eat a meal, I log it.
`[11:32]` It shows me what time I ate that meal,
`[11:33]` and it shows me the calories of that
`[11:35]` meal. So, chicken and rice, 550
`[11:36]` calories. It's connected to the latest
`[11:38]` Claude model, so it can estimate. You
`[11:40]` can also give it more details. You can
`[11:41]` even send a photo into Telegram if you
`[11:43]` want to actually photograph your meal.
`[11:45]` It's basically like having Cal AI built
`[11:47]` into the dashboard. And then I could
`[11:48]` see, you know, my protein for the day,
`[11:50]` my nutrition, how many calories I have
`[11:51]` left. And this also gets logged under
`[11:53]` the health section of the dashboard,
`[11:55]` where it shows my daily protein intake,
`[11:57]` calorie intake every single day. Uh so,
`[11:59]` I can make sure, you know, I'm eating
`[12:01]` right. And you can actually go a step
`[12:02]` further. You could connect this to your
`[12:03]` wearable like Oura Ring or Whoop, and
`[12:05]` actually import the data, and then have
`[12:07]` it weighed against other metrics. I
`[12:09]` haven't done that step yet, but this is
`[12:10]` the architecture you can build upon.
`[12:11]` Like, essentially, the goal here is to
`[12:13]` build an operating system that controls
`[12:15]` your life or has your entire life
`[12:17]` summarized here. Now, there are some
`[12:18]` things that I keep off the app. Like,
`[12:20]` for example, I still do keep big picture
`[12:22]` stuff on Notion. So, big picture goals,
`[12:24]` my compliance setups, my company roster,
`[12:27]` and just general information that
`[12:29]` doesn't change much. I'll keep somewhere
`[12:30]` else cuz I want to make sure I have that
`[12:32]` data. But, basically, for anything else,
`[12:34]` any active task, I keep it on the
`[12:36]` application. I also have a system where
`[12:38]` things automatically get backed up. So,
`[12:39]` if for some reason Claude deletes all
`[12:41]` the data, it's actually backed up in
`[12:42]` Superbase, and archived, and stored. So,
`[12:44]` you don't need to worry about losing
`[12:45]` data. You can always re-export. The full
`[12:47]` guide to this, once again, is going to
`[12:48]` be in the description below. It's in my
`[12:50]` Instagram community. You can access it
`[12:51]` by signing up to the newsletter, and
`[12:53]` that's going to have the full prompt
`[12:55]` that you can take and put into Claude
`[12:57]` code yourself or Codex, which is to be
`[13:00]` honest, probably the better coding
`[13:01]` model, but I did this on Claude code
`[13:02]` beforehand. And it's going to run you
`[13:04]` step-by-step through my process because,
`[13:05]` honestly, this video would be hours and
`[13:07]` hours and hours if I went through every
`[13:09]` single little finicky thing that I had
`[13:11]` to fix to build this. If you like this
`[13:13]` video, let me know in the comments
`[13:14]` below. I can actually do a follow-up
`[13:15]` where I go in depth on specific elements
`[13:17]` of the dashboard, but I wanted to show
`[13:19]` you what I've been building and working
`[13:20]` on in this video and give you an
`[13:22]` overview. And then it connects to my
`[13:23]` Google Calendar below. You can actually
`[13:25]` edit it directly from here. I still like
`[13:27]` using Google Calendar though. I just
`[13:28]` like having this open all day, so I have
`[13:30]` it on a screen on my computer so I can
`[13:32]` see what upcoming meetings I have. I'm
`[13:33]` constantly referring back to it. And
`[13:35]` then the top right-hand corner I have
`[13:36]` some goals for the week, for the month.
`[13:38]` They actually store and there's a list
`[13:39]` here. Usually I'll just have three to
`[13:40]` five goals for a month so I can see
`[13:42]` right, I want to ship a product, I want
`[13:43]` to get out 20 videos, I want to go to
`[13:45]` the gym every day. And then I have all
`[13:46]` the goals there so I'm constantly
`[13:47]` reminded and I'm just aware every single
`[13:50]` day of what I'm actually working towards
`[13:52]` which I think is so powerful because if
`[13:54]` it's not in front of you every day,
`[13:55]` you're actually just going to forget. So
`[13:57]` this way I'm actually forced to stick to
`[13:59]` the things that I want to do. Going into
`[14:00]` the CRM system, you can actually drag
`[14:01]` things around in terms of priorities.
`[14:03]` You can tick things off once you do them
`[14:05]` and they'll automatically get sent to
`[14:07]` the archive section. I continuously
`[14:09]` improve this over time but it's
`[14:10]` basically in my opinion a better version
`[14:12]` of the Notion task management system. I
`[14:14]` will say there were a lot of glitches,
`[14:16]` there still are from time to time, but
`[14:18]` every time there is a bug, I fix it and
`[14:20]` then over the last few days I've found
`[14:22]` I've had less and less bugs. You're just
`[14:24]` going to have to be aware that if you're
`[14:25]` going to build your own OS because you
`[14:26]` don't have thousands of engineers like
`[14:28]` Notion who over time have fixed a lot of
`[14:30]` their issues, you're going to run into
`[14:31]` your own. But because it's custom built,
`[14:34]` that trade-off becomes a pro because you
`[14:35]` can build it exactly how you want to
`[14:37]` build it. I can also switch to the
`[14:39]` Kanban view just like Notion so I can
`[14:41]` actually drag things along from this
`[14:43]` week to today to this month so I can
`[14:44]` have an overview of all my tasks. And if
`[14:46]` you go into the brain section of the
`[14:47]` application, it actually opens up a view
`[14:50]` where you can view the current status on
`[14:52]` different elements of your life. So
`[14:53]` legal, personal finance, content,
`[14:55]` products, opsec, business opportunities.
`[14:58]` If you click on one, it'll actually
`[14:59]` bring up all of the tasks underneath
`[15:01]` this category and then you can actually
`[15:03]` leave notes here or links here just like
`[15:05]` you can in Notion pages so you can
`[15:07]` easily refer back to it. And it also has
`[15:09]` a summary of the key things within each
`[15:11]` category. Like there might be some clear
`[15:12]` security risks that you're taking on. So
`[15:14]` there might be key life admin things
`[15:16]` that you need to fix that will be
`[15:18]` highlighted here in the summary as
`[15:20]` things that you need to do. And the best
`[15:21]` part is because you have all of this in
`[15:23]` a memory system, you can simply prompt
`[15:25]` the AI and ask, "Look, what are the top
`[15:27]` three things right now that if you were
`[15:29]` a strategic CEO or consultant, you would
`[15:32]` recommend that I need to do right now?"
`[15:35]` And it will actually be able to go
`[15:36]` through hundreds or thousands of entries
`[15:38]` and look at the few things which are
`[15:40]` actually going to move the needle for
`[15:41]` you or your business, which I think is
`[15:43]` really important. The finance section
`[15:44]` I'm not going to get into in today's
`[15:46]` video because honestly, it's its own
`[15:48]` video and I'm going to do a follow-up,
`[15:49]` so make sure you subscribe. But of
`[15:51]` course, remember you can tweak this any
`[15:52]` way that you want. The world is your
`[15:54]` oyster with AI. This is just what I
`[15:56]` found impactful for my V1 build, but I'm
`[15:58]` going to keep improving this over time
`[15:59]` as things change. And also, I have room
`[16:01]` to add more things. I just didn't want
`[16:03]` to clutter my dashboard too much in the
`[16:05]` early days. All right, now let me give
`[16:06]` you a quick practical example of how I
`[16:08]` use this in my daily life. So basically,
`[16:10]` this is how I use this setup. So I have
`[16:13]` three monitors. You don't need three
`[16:14]` monitors for this. If you're on your
`[16:15]` laptop, you can just have three
`[16:17]` different desktops. So this is just how
`[16:18]` I operate in my daily life. On my
`[16:20]` left-hand screen here, I have the
`[16:22]` dashboard open at all times, then I get
`[16:23]` to see what my upcoming meetings are,
`[16:26]` everything that I need to see, and then
`[16:27]` I work on the middle screen. So I'm
`[16:29]` doing work, writing tweets, reviewing
`[16:31]` proposals, taking meetings, whatever I'm
`[16:32]` doing on the middle screen, and then on
`[16:34]` the left, I'll just glance over and make
`[16:35]` sure that my day is in order. Then on
`[16:38]` the right-hand side, I have Claude open.
`[16:40]` This is Claude Codor, you know, the
`[16:41]` normal Claude app if I'm chatting there.
`[16:43]` And then I have GPT open as well. So I
`[16:45]` have my two AIs. If I ever need to make
`[16:47]` tweaks on Claude Codor to the dashboard,
`[16:49]` I can just do it up here and I just have
`[16:51]` these open all day, you know, in case I
`[16:53]` need them. And then, when I need to
`[16:54]` enter something, so a new task comes up,
`[16:56]` let's say I get a message from someone I
`[16:57]` need to do something, I just add it here
`[16:59]` so I can quickly capture it. I also have
`[17:01]` Whisper on my computer so I can
`[17:03]` use the command and it basically records
`[17:04]` audio for me if I just want to speak it.
`[17:07]` If not, I'll just type it in. If I'm on
`[17:08]` the go or, you know, if I'm just doing
`[17:10]` something on my phone, then it's
`[17:11]` actually easier for me to hit the action
`[17:12]` button and then voice prompt into
`[17:14]` Telegram. And when I voice prompt, it
`[17:16]` auto-populates in the CRM over here
`[17:18]` anyway. And the other thing that I do a
`[17:19]` lot, especially when I'm out, is I
`[17:21]` actually use the weather app. So, I've
`[17:22]` created a mobile version which I'm
`[17:24]` optimizing to be even better for mobile.
`[17:26]` So, I can do this on the go and it's
`[17:28]` connected to the same memory system. So,
`[17:30]` you don't even need your computer.
`[17:31]` That's basically how I use it in my
`[17:32]` day-to-day life. Thank you guys so much
`[17:33]` for watching this video. This was a
`[17:36]` really intense build to put together,
`[17:38]` but I'm so glad I went through this
`[17:39]` process because I think it's going to be
`[17:41]` a part of my life for many months and
`[17:43]` hopefully years to come. I'm just going
`[17:44]` to keep upgrading this over time and I'm
`[17:46]` going to keep making videos on it. So,
`[17:47]` if you enjoyed this, make sure to
`[17:49]` subscribe. Obviously, the full prompt is
`[17:51]` available down below to help you build
`[17:53]` your own. It is going to take a bit of
`[17:54]` time, but it's definitely worth it
`[17:56]` because I honestly think having a system
`[17:58]` like this can make me millions of
`[17:59]` dollars and can make me a 10x more
`[18:01]` productive human because it's
`[18:03]` custom-built for exactly what I need.
`[18:05]` Thank you guys for watching. I'll see
`[18:06]` you in the next one. Peace out.
