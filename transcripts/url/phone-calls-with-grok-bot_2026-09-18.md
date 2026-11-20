# Phone calls with Grok Bot

- **Source:** https://www.youtube.com/watch?v=Fmr_72cYZo8
- **Uploader:** Matt Palmer
- **Uploaded:** 2026-09-10
- **Duration:** 6:38
- **Method:** YouTube captions (no transcription needed)

## Transcript

What time do you guys open and close? &gt;&gt; Uh well, during the week we open at about 7:30 a.m. and we close at 4:00. &gt;&gt; Got it. Do you guys sell cappuccinos? &gt;&gt; We do. We sell cappuccinos and other espresso beverages. Hey all, fun video today. I'm going to show you how to give your Grok Bot a phone. And more than a phone, we're going to give it a phone number and the ability to make phone calls. So, by the end of this video, you'll understand how to have your Grok Bot go and call somebody and get some information. And I think that's really amazing. And the cooler part is that it takes like 5 minutes. So, what I've done is I've created a dial bot template. We just launched templates in Grok Bot. And if you open this link, you're going to get taken to this page to install the template effectively. You can find the template in the description where where this video's posted, but essentially all it is is the instructions I gave my Grok Bot in the configurations around using the Bland API and MCP. And once you click install, you're going to get this bot. The bot's pre-configured. It should have all the setup. So, it's just going to ask you for some information on how to get started. And all you're going to need is a Bland API key and then a voice ID. So, I'm going to walk through how to get those right now. So, the first thing you want to do is go to Bland and sign up. From there, you'll be able to go into your personal org into settings and grab a new API key. Now, I'm going to create a key. I'm not going to show that cuz that's sensitive information. But, you'll also want to add some credits to your account. So, we can just create a key, uh copy that. And hopefully by the time you copy that key and you go back to Grok Bot, you'll see that it's asking you for an API key. We're going to paste that in and save that securely. Cool thing about Grok Bot is it takes that sensitive information and just puts it in a vault. So, like it can't even access that API key, Grok Bot. That's you you can access that API key. It's stored completely securely, which means that it never gets exposed. Um which is pretty neat. The other thing we want to do is come into Bland and create a voice. So, we have our API keys here. We're going to go into our voices. And so, by default on their like lowest tier plan, you get one voice. What I did was I created a Matt voice just by uploading a clip of some audio of one of my videos. So, if I click generate speech, this is a test reading for Matt. reading for Matt. &gt;&gt; [laughter] &gt;&gt; [laughter] &gt;&gt; Well, let's try that one again. This is a test reading for Matt. Okay, I definitely like the second one Okay, I definitely like the second one better. better. It can be a little bit wonky. This like voice agent stuff is not perfect by any means. You'll see that in the demo. But, now we essentially have all the pieces we need because we can come over here to our voice and copy the voice ID. And once we have that, if we pop over to once we have that, if we pop over to Grokbot, Grokbot, Grokbot, um um you can see that it's got Bland configured. And then I can say, "Here's the voice ID." And that really should be all we need to get this set up. So, we have the voice ID, we have the API key, and now Grokbot's saying Bland is connected. So, what will we use this for? Well, sometimes I need to call a business. Sometimes I want to check in on something. I don't want to navigate like a phone tree. I have to call like my insurance company. I'm not going to name names here. I don't want to put anybody on blast, but like I have to navigate my insurance company's AI voice system. It's like kind of janky. Isn't really the best. So, it's a kind of a pain. This helps us avoid all of that stuff, right? So, with this, we can just have an agent do it. So, now I'm having my agents talk to your agents. This is just how the world works these days. It's really crazy. But, let's let's take a look at a live demo. Okay, so I gave Grokbot my phone number here in a secure input because as much as I love you all, I don't need to be getting any more phone calls, you know what I'm saying? So, we're going to save that, and I told it to give me a ring. I have my phone right here, and ask me basically right here, and ask me basically um um about my business hours and if I sell cappuccinos. So, you know, the hypothetical situation is like I want to make a call to a business. Maybe I'm a little bit busy. I can have my it. They have a phone number. They can do that for me. So, um, Grokbot says it's calling me. I would expect to get a call any minute and hopefully, uh, that's what we will see in a second uh, that's what we will see in a second here. here. And then I'm going to pull this in. We'll do like a little fancy, uh, phone call on the video thing, you know, we got to make it make it look good. Um, All right. Okay, sick. So, we're getting a phone call. I'm going to answer this and we're see we'll see what goes it on. Um, hello. &gt;&gt; Hey, quick question about your hours. &gt;&gt; Uh, what do you want to know about our &gt;&gt; Uh, what do you want to know about our hours? &gt;&gt; What time do you guys open and close? &gt;&gt; Uh, well, during the week we open at about 7:30 a.m. and we close at 4:00. &gt;&gt; Got it. Do you guys sell cappuccinos? &gt;&gt; We do. We sell cappuccinos and other espresso beverages. Anything else? &gt;&gt; Nope, that's it. Thanks. Bye. &gt;&gt; All right. &gt;&gt; [laughter] &gt;&gt; And it hung up, too. So, you can see the the voice agent is a little iffy. We got to dial in the prompt there. Um, but what I love about this workflow is that you can use this to go get information. Um, and it took like actually 5 minutes to set up. It's also a bit eerie talking to myself on the phone, I have to say. I'm still getting used to that a little bit. And I'm also a little concerned about how easy it is to train a model on my voice. my voice. Uh, Uh, Uh, but but under the hood in the Bland console, you have access to the entire transcript. So, you you can see the agent actually gave me the recording and the full transcript. Um, it also was able to report that the weekday hours were 7:00 to 4:00. Yes, on cappuccinos and other espresso drinks. Um, it gave us the recording and that call cost seven cents. So, just like that, we have a voice agent that can make calls for us, get information, and you can imagine starting to plug this into other bots that you're building. So, already on my mind is like, oh hey, you know, maybe I have um some sort of other workflow uh that can then call, you know, call chat with my dial bot. My dial bot can make phone calls on its behalf, take information down, and continue working through these workflows. Don't use this for like nefarious purposes or sketchy stuff. You're definitely going to get banned. It's definitely also unethical. So, you know, be conscious of whose time you're using, be conscious of what you're doing here, and and use this for good, not evil. Uh but, this was a fun video to make, and I think it's a fun tool to use. I can't wait to see what y'all do with it. Until next time, I'm Matt with SpaceX. Peace.

## Timestamped

`[00:02]` What time do you guys open and close?
`[00:02]` &gt;&gt; Uh well, during the week we open at
`[00:04]` about 7:30 a.m. and we close at 4:00.
`[00:08]` &gt;&gt; Got it. Do you guys sell cappuccinos?
`[00:10]` &gt;&gt; We do. We sell cappuccinos and other
`[00:12]` espresso beverages. Hey all, fun video
`[00:14]` today. I'm going to show you how to give
`[00:15]` your Grok Bot a phone. And more than a
`[00:17]` phone, we're going to give it a phone
`[00:18]` number and the ability to make phone
`[00:20]` calls. So, by the end of this video,
`[00:22]` you'll understand how to have your Grok
`[00:23]` Bot go and call somebody and get some
`[00:25]` information. And I think that's really
`[00:27]` amazing. And the cooler part is that it
`[00:29]` takes like 5 minutes. So, what I've done
`[00:31]` is I've created a dial bot template. We
`[00:33]` just launched templates in Grok Bot. And
`[00:36]` if you open this link, you're going to
`[00:37]` get taken to this page to install the
`[00:40]` template effectively. You can find the
`[00:41]` template in the description where where
`[00:43]` this video's posted, but essentially all
`[00:45]` it is is the instructions I gave my Grok
`[00:48]` Bot in the configurations around using
`[00:50]` the Bland API and MCP.
`[00:52]` And once you click install, you're going
`[00:55]` to get this bot. The bot's
`[00:57]` pre-configured. It should have all the
`[00:58]` setup. So, it's just going to ask you
`[01:00]` for some information on how to get
`[01:01]` started. And all you're going to need is
`[01:03]` a Bland API key and then a voice ID. So,
`[01:06]` I'm going to walk through how to get
`[01:07]` those right now. So, the first thing you
`[01:09]` want to do is go to Bland and sign up.
`[01:12]` From there, you'll be able to go into
`[01:13]` your personal org into settings and grab
`[01:17]` a new API key. Now, I'm going to create
`[01:19]` a key. I'm not going to show that cuz
`[01:21]` that's sensitive information. But,
`[01:22]` you'll also want to add some credits to
`[01:24]` your account. So, we can just create a
`[01:25]` key, uh copy that. And hopefully by the
`[01:28]` time you copy that key and you go back
`[01:31]` to Grok Bot, you'll see that it's asking
`[01:33]` you for an API key. We're going to paste
`[01:35]` that in and save that securely.
`[01:37]` Cool thing about Grok Bot is it takes
`[01:39]` that sensitive information and just puts
`[01:41]` it in a vault. So, like it can't even
`[01:43]` access that API key, Grok Bot.
`[01:46]` That's you you can access that API key.
`[01:48]` It's stored completely securely, which
`[01:50]` means that it never gets exposed.
`[01:52]` Um which is pretty neat. The other thing
`[01:54]` we want to do is come into Bland and
`[01:57]` create a voice. So, we have our API keys
`[01:59]` here. We're going to go into our voices.
`[02:02]` And so, by default on their like lowest
`[02:05]` tier plan, you get one voice. What I did
`[02:07]` was I created a Matt voice just by
`[02:09]` uploading a clip of some
`[02:12]` audio of one of my videos. So, if I
`[02:14]` click generate speech, this is a test
`[02:17]` reading for Matt.
`[02:18]` reading for Matt. &gt;&gt; [laughter]
`[02:19]` &gt;&gt; [laughter]
`[02:19]` &gt;&gt; Well, let's try that one again. This is
`[02:21]` a test reading for Matt.
`[02:23]` Okay, I definitely like the second one
`[02:24]` Okay, I definitely like the second one better.
`[02:25]` better.
`[02:25]` It can be a little bit wonky. This like
`[02:27]` voice agent stuff is not perfect by any
`[02:29]` means. You'll see that in the demo. But,
`[02:31]` now we essentially have all the pieces
`[02:33]` we need because we can come over here to
`[02:36]` our voice and copy the voice ID. And
`[02:38]` once we have that, if we pop over to
`[02:40]` once we have that, if we pop over to Grokbot,
`[02:42]` Grokbot,
`[02:42]` Grokbot, um
`[02:42]` um
`[02:42]` you can see that it's got Bland
`[02:44]` configured. And then I can say, "Here's
`[02:48]` the voice ID."
`[02:51]` And that really should be all we need to
`[02:52]` get this set up. So, we have the voice
`[02:55]` ID, we have the API key, and now
`[02:57]` Grokbot's saying Bland is connected. So,
`[03:01]` what will we use this for? Well,
`[03:02]` sometimes I need to call a business.
`[03:04]` Sometimes I want to check in on
`[03:05]` something. I don't want to navigate like
`[03:07]` a phone tree. I have to call like my
`[03:08]` insurance company. I'm not going to name
`[03:10]` names here. I don't want to put anybody
`[03:12]` on blast, but like I have to navigate my
`[03:14]` insurance company's AI voice system.
`[03:16]` It's like kind of janky. Isn't really
`[03:18]` the best. So, it's a kind of a pain.
`[03:20]` This helps us
`[03:21]` avoid all of that stuff, right? So, with
`[03:24]` this, we can just have an agent do it.
`[03:26]` So, now I'm having my agents talk to
`[03:28]` your agents. This is just how the world
`[03:30]` works these days. It's really crazy.
`[03:32]` But, let's let's take a look at a live
`[03:33]` demo. Okay, so I gave Grokbot my phone
`[03:37]` number here in a secure input because as
`[03:39]` much as I love you all,
`[03:41]` I don't need to be getting any more
`[03:42]` phone calls, you know what I'm saying?
`[03:43]` So, we're going to save that, and I told
`[03:45]` it to give me a ring. I have my phone
`[03:47]` right here, and ask me basically
`[03:50]` right here, and ask me basically um
`[03:51]` um
`[03:51]` about my business hours and if I sell
`[03:53]` cappuccinos. So, you know, the
`[03:55]` hypothetical situation is like I want to
`[03:57]` make a call to a business. Maybe I'm a
`[03:59]` little bit busy. I can have my
`[04:00]` it. They have a phone number. They can
`[04:02]` do that for me. So,
`[04:04]` um, Grokbot says it's calling me. I
`[04:05]` would expect to get a call any minute
`[04:07]` and hopefully,
`[04:09]` uh, that's what we will see in a second
`[04:11]` uh, that's what we will see in a second here.
`[04:12]` here.
`[04:12]` And then I'm going to pull this in.
`[04:13]` We'll do like a little fancy, uh, phone
`[04:15]` call on the video thing, you know, we
`[04:16]` got to make it make it look good. Um,
`[04:20]` All right. Okay, sick. So, we're getting
`[04:22]` a phone call. I'm going to answer this
`[04:24]` and we're see we'll see what goes it on.
`[04:31]` Um, hello.
`[04:31]` &gt;&gt; Hey, quick question about your hours.
`[04:34]` &gt;&gt; Uh, what do you want to know about our
`[04:35]` &gt;&gt; Uh, what do you want to know about our hours?
`[04:39]` &gt;&gt; What time do you guys open and close?
`[04:39]` &gt;&gt; Uh, well, during the week we open at
`[04:41]` about 7:30 a.m. and we close at 4:00.
`[04:46]` &gt;&gt; Got it. Do you guys sell cappuccinos?
`[04:48]` &gt;&gt; We do. We sell cappuccinos and other
`[04:50]` espresso beverages.
`[05:00]` Anything else?
`[05:00]` &gt;&gt; Nope, that's it. Thanks. Bye.
`[05:01]` &gt;&gt; All right.
`[05:04]` &gt;&gt; [laughter]
`[05:04]` &gt;&gt; And it hung up, too. So, you can see the
`[05:07]` the voice agent is a little iffy. We got
`[05:09]` to dial in the prompt there. Um, but
`[05:11]` what I love about this workflow is that
`[05:13]` you can use this to go get information.
`[05:16]` Um, and it took like actually 5 minutes
`[05:18]` to set up. It's also a bit eerie talking
`[05:20]` to myself on the phone, I have to say.
`[05:22]` I'm still getting used to that a little
`[05:23]` bit. And I'm also a little concerned
`[05:25]` about how easy it is to train a model on
`[05:27]` my voice.
`[05:28]` my voice. Uh,
`[05:28]` Uh,
`[05:29]` Uh, but
`[05:30]` but
`[05:30]` under the hood in the Bland console, you
`[05:32]` have access to the entire transcript.
`[05:35]` So, you you can see the agent actually
`[05:36]` gave me the recording and the full
`[05:38]` transcript. Um,
`[05:40]` it also was able to report that the
`[05:43]` weekday hours were 7:00 to 4:00. Yes, on
`[05:46]` cappuccinos and other espresso drinks.
`[05:48]` Um, it gave us the recording and that
`[05:50]` call cost seven cents. So, just like
`[05:53]` that, we have a voice agent that can
`[05:55]` make calls for us, get information, and
`[05:58]` you can imagine starting to plug this
`[05:59]` into other bots that you're building.
`[06:01]` So, already on my mind is like, oh hey,
`[06:03]` you know, maybe I have um some sort of
`[06:05]` other workflow uh that can then call,
`[06:08]` you know, call chat with my dial bot. My
`[06:11]` dial bot can make phone calls on its
`[06:13]` behalf, take information down, and
`[06:15]` continue working through these
`[06:16]` workflows. Don't use this for like
`[06:18]` nefarious purposes or sketchy stuff.
`[06:21]` You're definitely going to get banned.
`[06:22]` It's definitely also unethical. So, you
`[06:25]` know, be conscious of whose time you're
`[06:27]` using, be conscious of what you're doing
`[06:28]` here, and and use this for good, not
`[06:30]` evil. Uh but, this was a fun video to
`[06:32]` make, and I think it's a fun tool to
`[06:33]` use. I can't wait to see what y'all do
`[06:35]` with it. Until next time, I'm Matt with
`[06:36]` SpaceX. Peace.
