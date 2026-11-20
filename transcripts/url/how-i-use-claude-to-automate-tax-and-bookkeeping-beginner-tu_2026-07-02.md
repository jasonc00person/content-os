# How I Use Claude to Automate Tax and Bookkeeping (Beginner Tutorial)

- **Source:** https://www.youtube.com/watch?v=ztXUJa58r9o
- **Uploader:** Softgirlnocode
- **Uploaded:** 2026-03-21
- **Duration:** 9:33
- **Method:** YouTube captions (no transcription needed)

## Transcript

So, what is Claude code? The name itself, it's a little misleading. Claude code is basically Claude, but instead of living in a browser, it lives inside of your computer's terminal. And your terminal is just a text interface for your computer. When you chat with Claude normally, it gives you answer, but it doesn't really do anything on your computer. It can't create files, it can't touch your Google Drive, or organize your desktop for you. But Claude code can. Think of it like the difference between calling a contractor on the phone for advice versus actually letting them into your house to do the work. Claude code is the contractor walking through your front door, rolling up their sleeves, and building the thing. Now, how do you access it? You want to access it through an IDE. IDE stands for integrated developer environment, basically just a coding workspace. VS Code is the one I use. It is completely free. It might seem unfamiliar at first when you open it up for the first time, but this is really what it is. On the left side, you have your folder structure, all your files, scripts, documents, and on the right side, you have your chat window where you talk to Claude in plain English. Claude code's real power is its ability to write code so well that it can basically build any program or system for you. To get its full capacity, you have to use it as a terminal through an IDE, and that's where you get the best quality output and the most efficient use of your tokens. If you're using Claude code through the built-in Claude interface or the Chrome extension, you're essentially using a lighter version of it. It is good for quick tasks, but it can't fully execute Python scripts on your machine, and you will burn through your token limit faster because the back and forth is less efficient. When you access it through an IDE like VS Code, you're giving it real workspace. It can see your entire folder structure, write scripts, run them, catch errors, fix them, and iterate all in one session. So, if you're serious about building something and automation a tool, I would definitely install VS Code. It is free, takes 5 minutes to set up, and the difference between getting 20% of what Claude code can do versus the whole thing. Now that we established the basic, let's install VS Code and start setting it up. Open VS Code, go to extension tab, and search Claude code to install it, and you will see this one from Anthropic. Once you do that, you will see the Claude code icon appear as an agent window, and then you can start using it as your chat interface. And next, before you open anything, go to your desktop and create a folder. In my case, it's called Bookkeeper Tax. Then, open VS Code and open that folder as your workspace. Now, Claude code is going to operate within that folder. Then, the next thing you want to do is go to setting and enable allow dangerously skip permission. What this does is is stop Claude from pausing every 2 minutes to ask, "Can I run this command? Can I access this file?" It lets it work continuously without having you click approve all the time. Now, the next step is to generate Claude MD file. This is a very important thing you need to set up before you start building anything. MD file is basically a permanent briefing document Claude reads automatically at the start of every single session. It is where you define what the project is, what's the folder structure, how should files be organized, what are some of the rules, so you're just setting up the guardrails. Now, how do you get a Claude MD file? You have two options. Option one, you can find a template online. There are great creators sharing Claude MD files everywhere on GitHub, YouTube. I use one from a YouTuber called Nate. He is an incredible resource for AI automation. I will drop his file in the description, so you can start from the same foundation I did. Option two is you can build one yourself by giving Claude high-level context about your projects, or you can use the shortcut {slash} init at any point, and Claude will generate a Claude MD file based on everything it knows about your project so far. So, even if you don't have one set up up front, you can always generate one once you have started building. Now, I'm going to drop my Claude MD file, and you can see that it outlines folder structure, the role of each folder. There's a workflow folder for the high-level process logic, and we also have an agent folder for decision-making layer, and we also have a tools folder where we want all the Python scripts to be stored at. It also defines a self-improvement loop, folder structures. But, having the Claude MD means you're defining the architecture, keeps it consistent across all your projects. You can see there's a lot more specification inside of the Claude MD file. For example, API keys and secrets to be stored in a hidden folder. That's what this dot prefix on the folder name means, it's hidden by default. This matters if your project ever gets pushed to GitHub, you want to make sure nobody sees your credentials. Now, just type "Initiate this project based on Claude MD file", and Claude reads and creates the entire folder structure, every subfolder, just like how it's indicated inside of the Claude MD file. And now, you're ready to cook. Now, Claude code has different mode, and you want to first switch to planning mode. This tells Claude, "Don't start creating files yet, just give the full plan, and let's strategize and brainstorm first." You always want to see the whole plan before execution starts. It's way easier to redirect at the planning stage rather than it's already started building and then it's going down the wrong direction. And here's what I asked it to do. I just kind of blurted out using Whisper Flow. "I want to automate the bookkeeping process for my one-person business. This should be an ongoing automation to help me keep track invoices and expenses with the goal of organizing my monthly record and making year-end tax reporting easier. I'm a Canadian resident, so please incorporate all Canadian tax compliance requirements in your planning. For invoices, auto-generate based on number sequence, track in Google Sheets, generate a PDF and upload it to the corresponding folder in Google Drive. For expenses, I want to import a bank statement or credit card transaction statement, have expenses have expenses categorized intelligently, update my expense tracker, and create formula directly inside Google Sheet." see it immediately went into research mode and started asking me smart and relevant questions, like do I have GST/HST registration, which bank do I use? So, it's actually really interesting to kind of see what the thought process is and how he plans out the whole thing. But, in under 30 seconds, we have a pretty comprehensive plan. We have the system architecture with Google Sheets, it will create and research all the expense categories and its deductibility and corresponding tax document line ID. I have all the Python scripts, setting up Google Sheets, generating invoices, logging invoices, uploading PDF to Drive, categorizing expenses, logging expenses, and all the SOP it will create for the workflow folder. This looks pretty good to me. I think we're just going to roll with it. Now, it literally took 2 minutes. You can see now I have eight tools and three workflows all created under my folder structure, and you can review them. It also tells me exactly what I need to do next, which is to enter my credentials so it can connect to Google API. Now, I'm going to set this up and come back. All right. Now, everything it needs to be set up has been set up, and we can run a test now. And all you need to do is tell it the invoice details. "Generate invoice 003 for client Google, one standard video, $1,000." Let's see what it comes back with. It followed up with a good question. It's asking if it's Google Canada or Google US because the tax treatment is going to be different. Now, let's select this, and now, after it runs for like 20 seconds, three steps have been completed. We have our PDF generated with the correct information. Some of them I left as placeholder for this demonstration purpose, and we also have our PDF uploaded to the right folder in my Google Drive, and we have Google Sheet updated with the invoice summary with a direct link to the Drive file. And I can take this further. I can add a step where it automatically emails the PDF to the client, and that will be a true end-to-end automation. But for now, we're just going to leave it like this. And now, we're going to test the expense side. Okay, so I dropped my February 2026 bank statement into the chat. So, it's asking me to set up an Anthropic API connection so it can do live search to figure out what category of vendor belongs to on my statement. For now, I'm just going to ask it to skip that and search it live for this time. The good news is it has a memory file. Once it learns the vendor, it will remember it for the next time. So, in about 20 seconds, it processed 40 lines of transaction. Every expense was categorized with deductibility status, the CRA category, and ITC eligibility. That's the input tax credit for HST in Canada. You can claim back your HST on any business expense. I love how everything is built on formulas, so when I go into the sheet and change anything, like marking an expense as non-deductible or change the percentage, it automatically updates my monthly summary and my tax summary report. So, it all feeds into the final tax calculation. Notice that this entire time, I didn't look at the code base once. The only thing I was managing were understanding the overall structure of what was being built, reviewing the plan before execution, and giving feedback when something needed adjusting. Any question I had, I just asked Claude directly, "Hey, where did you put this file? How do I get the API key? I can't find this." And it just answers everything very clearly. I hope that got you excited to start building. The learning curve is really not coding. It's just understanding the structure and be comfortable with using a terminal, using IDE. I'm leaving my Claude MD file and my full prompt in the description, so you can start from the same foundation I used. I will keep sharing what I learn and translating it as plainly as possible. Thank you so much for watching. I'll see you in the next one.

## Timestamped

`[00:02]` So, what is Claude code? The name
`[00:02]` itself, it's a little misleading. Claude
`[00:03]` code is basically Claude, but instead of
`[00:06]` living in a browser, it lives inside of
`[00:08]` your computer's terminal. And your
`[00:10]` terminal is just a text interface for
`[00:13]` your computer. When you chat with Claude
`[00:14]` normally, it gives you answer, but it
`[00:16]` doesn't really do anything on your
`[00:18]` computer. It can't create files, it
`[00:20]` can't touch your Google Drive, or
`[00:22]` organize your desktop for you. But
`[00:24]` Claude code can. Think of it like the
`[00:26]` difference between calling a contractor
`[00:28]` on the phone for advice versus actually
`[00:30]` letting them into your house to do the
`[00:32]` work. Claude code is the contractor
`[00:34]` walking through your front door, rolling
`[00:36]` up their sleeves, and building the
`[00:38]` thing. Now, how do you access it? You
`[00:40]` want to access it through an IDE. IDE
`[00:42]` stands for integrated developer
`[00:44]` environment, basically just a coding
`[00:46]` workspace. VS Code is the one I use. It
`[00:49]` is completely free. It might seem
`[00:51]` unfamiliar at first when you open it up
`[00:54]` for the first time, but this is really
`[00:55]` what it is. On the left side, you have
`[00:57]` your folder structure, all your files,
`[01:00]` scripts, documents, and on the right
`[01:02]` side, you have your chat window where
`[01:04]` you talk to Claude in plain English.
`[01:06]` Claude code's real power is its ability
`[01:08]` to write code so well that it can
`[01:10]` basically build any program or system
`[01:12]` for you. To get its full capacity, you
`[01:15]` have to use it as a terminal through an
`[01:17]` IDE, and that's where you get the best
`[01:19]` quality output and the most efficient
`[01:21]` use of your tokens. If you're using
`[01:23]` Claude code through the built-in Claude
`[01:24]` interface or the Chrome extension,
`[01:26]` you're essentially using a lighter
`[01:28]` version of it. It is good for quick
`[01:30]` tasks, but it can't fully execute Python
`[01:33]` scripts on your machine, and you will
`[01:34]` burn through your token limit faster
`[01:36]` because the back and forth is less
`[01:38]` efficient. When you access it through an
`[01:39]` IDE like VS Code, you're giving it real
`[01:42]` workspace. It can see your entire folder
`[01:44]` structure, write scripts, run them,
`[01:46]` catch errors, fix them, and iterate all
`[01:49]` in one session. So, if you're serious
`[01:51]` about building something and automation
`[01:53]` a tool, I would definitely install VS
`[01:55]` Code. It is free, takes 5 minutes to set
`[01:57]` up, and the difference between getting
`[01:59]` 20% of what Claude code can do versus
`[02:01]` the whole thing. Now that we established
`[02:03]` the basic, let's install VS Code and
`[02:05]` start setting it up. Open VS Code, go to
`[02:07]` extension tab, and search Claude code to
`[02:10]` install it, and you will see this one
`[02:12]` from Anthropic. Once you do that, you
`[02:14]` will see the Claude code icon appear as
`[02:16]` an agent window, and then you can start
`[02:18]` using it as your chat interface. And
`[02:20]` next, before you open anything, go to
`[02:22]` your desktop and create a folder. In my
`[02:24]` case, it's called Bookkeeper Tax. Then,
`[02:27]` open VS Code and open that folder as
`[02:29]` your workspace. Now, Claude code is
`[02:31]` going to operate within that folder.
`[02:33]` Then, the next thing you want to do is
`[02:34]` go to setting and enable allow
`[02:37]` dangerously skip permission. What this
`[02:39]` does is is stop Claude from pausing
`[02:41]` every 2 minutes to ask, "Can I run this
`[02:44]` command? Can I access this file?" It
`[02:46]` lets it work continuously without having
`[02:48]` you click approve all the time. Now, the
`[02:50]` next step is to generate Claude MD file.
`[02:52]` This is a very important thing you need
`[02:54]` to set up before you start building
`[02:56]` anything. MD file is basically a
`[02:58]` permanent briefing document Claude reads
`[03:00]` automatically at the start of every
`[03:02]` single session. It is where you define
`[03:04]` what the project is, what's the folder
`[03:06]` structure, how should files be
`[03:08]` organized, what are some of the rules,
`[03:10]` so you're just setting up the
`[03:11]` guardrails. Now, how do you get a Claude
`[03:13]` MD file? You have two options. Option
`[03:15]` one, you can find a template online.
`[03:17]` There are great creators sharing Claude
`[03:19]` MD files everywhere on GitHub, YouTube.
`[03:21]` I use one from a YouTuber called Nate.
`[03:23]` He is an incredible resource for AI
`[03:25]` automation. I will drop his file in the
`[03:27]` description, so you can start from the
`[03:29]` same foundation I did. Option two is you
`[03:31]` can build one yourself by giving Claude
`[03:33]` high-level context about your projects,
`[03:35]` or you can use the shortcut {slash} init
`[03:38]` at any point, and Claude will generate a
`[03:40]` Claude MD file based on everything it
`[03:42]` knows about your project so far. So,
`[03:44]` even if you don't have one set up up
`[03:46]` front, you can always generate one once
`[03:48]` you have started building. Now, I'm
`[03:49]` going to drop my Claude MD file, and you
`[03:52]` can see that it outlines folder
`[03:54]` structure, the role of each folder.
`[03:56]` There's a workflow folder for the
`[03:58]` high-level process logic, and we also
`[04:00]` have an agent folder for decision-making
`[04:03]` layer, and we also have a tools folder
`[04:05]` where we want all the Python scripts to
`[04:07]` be stored at. It also defines a
`[04:09]` self-improvement loop, folder
`[04:10]` structures. But, having the Claude MD
`[04:12]` means you're defining the architecture,
`[04:14]` keeps it consistent across all your
`[04:16]` projects. You can see there's a lot more
`[04:18]` specification inside of the Claude MD
`[04:21]` file. For example, API keys and secrets
`[04:23]` to be stored in a hidden folder. That's
`[04:26]` what this dot prefix on the folder name
`[04:28]` means, it's hidden by default. This
`[04:31]` matters if your project ever gets pushed
`[04:33]` to GitHub, you want to make sure nobody
`[04:35]` sees your credentials. Now, just type
`[04:36]` "Initiate this project based on Claude
`[04:38]` MD file", and Claude reads and creates
`[04:41]` the entire folder structure, every
`[04:42]` subfolder, just like how it's indicated
`[04:45]` inside of the Claude MD file. And now,
`[04:47]` you're ready to cook. Now, Claude code
`[04:48]` has different mode, and you want to
`[04:49]` first switch to planning mode. This
`[04:51]` tells Claude, "Don't start creating
`[04:53]` files yet, just give the full plan, and
`[04:55]` let's strategize and brainstorm first."
`[04:57]` You always want to see the whole plan
`[04:59]` before execution starts. It's way easier
`[05:01]` to redirect at the planning stage rather
`[05:04]` than it's already started building and
`[05:07]` then it's going down the wrong
`[05:08]` direction. And here's what I asked it to
`[05:10]` do. I just kind of blurted out using
`[05:12]` Whisper Flow. "I want to automate the
`[05:14]` bookkeeping process for my one-person
`[05:16]` business. This should be an ongoing
`[05:17]` automation to help me keep track
`[05:19]` invoices and expenses with the goal of
`[05:22]` organizing my monthly record and making
`[05:24]` year-end tax reporting easier. I'm a
`[05:26]` Canadian resident, so please incorporate
`[05:28]` all Canadian tax compliance requirements
`[05:30]` in your planning. For invoices,
`[05:32]` auto-generate based on number sequence,
`[05:35]` track in Google Sheets, generate a PDF
`[05:38]` and upload it to the corresponding
`[05:39]` folder in Google Drive. For expenses, I
`[05:42]` want to import a bank statement or
`[05:44]` credit card transaction statement, have
`[05:46]` expenses have expenses categorized
`[05:48]` intelligently, update my expense
`[05:50]` tracker, and create formula directly
`[05:52]` inside Google Sheet." see it immediately
`[05:54]` went into research mode and started
`[05:55]` asking me smart and relevant questions,
`[05:58]` like do I have GST/HST registration,
`[06:01]` which bank do I use? So, it's actually
`[06:02]` really interesting to kind of see what
`[06:04]` the thought process is and how he plans
`[06:06]` out the whole thing. But, in under 30
`[06:08]` seconds, we have a pretty comprehensive
`[06:10]` plan. We have the system architecture
`[06:12]` with Google Sheets, it will create and
`[06:14]` research all the expense categories and
`[06:16]` its deductibility and corresponding tax
`[06:18]` document line ID. I have all the Python
`[06:20]` scripts, setting up Google Sheets,
`[06:22]` generating invoices, logging invoices,
`[06:25]` uploading PDF to Drive, categorizing
`[06:27]` expenses, logging expenses, and all the
`[06:30]` SOP it will create for the workflow
`[06:32]` folder. This looks pretty good to me. I
`[06:34]` think we're just going to roll with it.
`[06:36]` Now, it literally took 2 minutes. You
`[06:38]` can see now I have eight tools and three
`[06:40]` workflows all created under my folder
`[06:43]` structure, and you can review them. It
`[06:45]` also tells me exactly what I need to do
`[06:46]` next, which is to enter my credentials
`[06:48]` so it can connect to Google API. Now,
`[06:51]` I'm going to set this up and come back.
`[06:52]` All right. Now, everything it needs to
`[06:54]` be set up has been set up, and we can
`[06:56]` run a test now. And all you need to do
`[06:58]` is tell it the invoice details.
`[07:00]` "Generate invoice 003 for client Google,
`[07:03]` one standard video, $1,000." Let's see
`[07:06]` what it comes back with. It followed up
`[07:07]` with a good question. It's asking if
`[07:09]` it's Google Canada or Google US because
`[07:12]` the tax treatment is going to be
`[07:14]` different. Now, let's select this, and
`[07:16]` now, after it runs for like 20 seconds,
`[07:18]` three steps have been completed. We have
`[07:20]` our PDF generated with the correct
`[07:22]` information. Some of them I left as
`[07:25]` placeholder for this demonstration
`[07:27]` purpose, and we also have our PDF
`[07:29]` uploaded to the right folder in my
`[07:30]` Google Drive, and we have Google Sheet
`[07:32]` updated with the invoice summary with a
`[07:35]` direct link to the Drive file. And I can
`[07:38]` take this further. I can add a step
`[07:40]` where it automatically emails the PDF to
`[07:42]` the client, and that will be a true
`[07:44]` end-to-end automation. But for now,
`[07:46]` we're just going to leave it like this.
`[07:48]` And now, we're going to test the expense
`[07:50]` side. Okay, so I dropped my February
`[07:52]` 2026 bank statement into the chat. So,
`[07:55]` it's asking me to set up an Anthropic
`[07:57]` API connection so it can do live search
`[07:59]` to figure out what category of vendor
`[08:01]` belongs to on my statement. For now, I'm
`[08:03]` just going to ask it to skip that and
`[08:05]` search it live for this time. The good
`[08:07]` news is it has a memory file. Once it
`[08:10]` learns the vendor, it will remember it
`[08:12]` for the next time. So, in about 20
`[08:14]` seconds, it processed 40 lines of
`[08:16]` transaction. Every expense was
`[08:18]` categorized with deductibility status,
`[08:21]` the CRA category, and ITC eligibility.
`[08:24]` That's the input tax credit for HST in
`[08:26]` Canada. You can claim back your HST on
`[08:29]` any business expense. I love how
`[08:31]` everything is built on formulas, so when
`[08:32]` I go into the sheet and change anything,
`[08:35]` like marking an expense as
`[08:37]` non-deductible or change the percentage,
`[08:40]` it automatically updates my monthly
`[08:42]` summary and my tax summary report. So,
`[08:45]` it all feeds into the final tax
`[08:47]` calculation. Notice that this entire
`[08:49]` time, I didn't look at the code base
`[08:51]` once. The only thing I was managing were
`[08:54]` understanding the overall structure of
`[08:56]` what was being built, reviewing the plan
`[08:58]` before execution, and giving feedback
`[09:00]` when something needed adjusting. Any
`[09:02]` question I had, I just asked Claude
`[09:04]` directly, "Hey, where did you put this
`[09:05]` file? How do I get the API key? I can't
`[09:08]` find this." And it just answers
`[09:10]` everything very clearly. I hope that got
`[09:12]` you excited to start building. The
`[09:14]` learning curve is really not coding.
`[09:16]` It's just understanding the structure
`[09:17]` and be comfortable with using a
`[09:19]` terminal, using IDE. I'm leaving my
`[09:21]` Claude MD file and my full prompt in the
`[09:23]` description, so you can start from the
`[09:25]` same foundation I used. I will keep
`[09:27]` sharing what I learn and translating it
`[09:28]` as plainly as possible. Thank you so
`[09:30]` much for watching. I'll see you in the
`[09:32]` next one.
