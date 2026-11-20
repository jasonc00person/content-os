# Claude Cowork Is REPLACING QuickBooks in Accounting Firms

- **Source:** https://www.youtube.com/watch?v=PwhvAASCJ1I
- **Uploader:** Jason On Firms
- **Uploaded:** 2026-06-03
- **Duration:** 13:15
- **Method:** YouTube captions (no transcription needed)

## Transcript

This is an accounting file I just put together with Claude Cowork. Seriously, I'm shocked at how good Claude is at being a legit accounting system. I'm a CPA, I ran a 40-person accounting firm. I can tell you I spend a huge amount of money on QuickBooks subscriptions for a little tiny baby accounting files, but there's a better way now. Let me show you how to take basic out-of-the-box Claude that's so-so for accounting work and turn it into a proper [music] double-entry ledger system. We're going to run through why default Claude is bad at accounting, [music] the simple change to make it much better at accounting tasks, and third, how to build your own reporting layer on top of Claude that just blows the socks off the crusty old PDFs you get out of QuickBooks, okay? Seriously, what I'm about to show you would have saved me so many recurring subscriptions. You're going to love this because Claude, it is kind of magic. You can do stuff like this. You can just chuck in a pile of bank statements and be like, "Do my books, bro." Seriously, that's the prompt. "Do my bookkeeping, use the QuickBooks default chart of accounts." It just knows that. It can go figure that out. All of these bank statements totaling 6,700 transactions, statements totaling 6,700 transactions, okay? okay? Yeah, right. Off it goes like an eager little beaver. I'll get right to work. What output would you like? Give me balance sheet and P&amp;L. How should I handle personal transactions? It looks like a bookkeeping company. You want to double-check my math? Looks great. Let's spot-check and done. Gives me the headline numbers, but that's not what I want. It actually gives me spreadsheets of everything. Holy I didn't see these. Okay, this took 7 minutes. I said 7. Mark, and I know you're like, "There's no way it's right, though." No, but it is. Like the balance sheet foots. You know, it had to make some guesses because there are some external transfers, like to another savings account, payments to a credit card, but it calls all this stuff out as pretty intelligent. The savings line is the cumulative amount transferred out to some other checking account. I don't have the statements. And the credit card and loan payments, I parked them in equity because I don't have an opening balance. I don't have statements. And honestly, it's so good that I'm like, "Did you actually just classify 6,700 transactions? The behind the scenes of how it did it, actually pretty interesting. First, it's got to pull all the transactions out of the bank statements. Then it cleans up the vendor names because they are like messy, right? They got all those numbers. But then it made a pattern rule classifier. It created about 50 rules. These are basically bank rules that it made on the fly to say, every time you see this company, it should be categorized this way. That ended up handling 96% of transactions, those bank rules. The remaining 250 it actually had an uncategorized and it did another pass going out looking up what those should be. But at the end of the day, everything balances. The only thing that might be wrong is maybe the classifications weren't the same way that you would do them. But but gang, I just gave it 12 months of bank statements. Those were images, not text, images in the PDFs. It did all this in 7 minutes. Oh. Yeah, honey, I got bad news. But in some ways it's like a party trick because how's anybody else going to work in this accounting file? I feel like I need a proper reporting system on top of it and it's not backed by anything. Like there's no database here for like persistent storage of the transactions themselves. This is what makes vanilla cloud very limited but has an ever so simple solution. You ready? It's called Beancount. Hang on. Did he say Beancount. Hang on. Did he say Beancount? Beancount? Beancount. I will explain. Here's another new prompt. Use Beancount to do my bookkeeping here for me, please. Use QuickBooks chart of accounts. Stick closely to the Beancount system. So we have a proper Beancount file for the transaction database. Exact same bank statements. Off it scurries. Good. Beancount is installed. Let me tell you about this Beancounting. Beancount is an open source system for storing double-entry accounting transactions in a text file. So if QuickBooks has like a big old sort of complicated database, Beancount says, how do we do that in just a flat old text file? Now, this is a legitimate project. 5,500 stars. 87 nerds have contributed to Look AT THAT GUY. WHAT were you doing? This guy has children, but I appreciate them nonetheless. Because this is free for anybody to swipe. And what it gives Claude that Claude doesn't natively have is a storage system. Now, look at this. So, this process completes and the result, it's this bean count file, dot bean count. Look what's in it. Whole pile of text. You got all the accounts, you got a journal. But this is a structured programmatic way to store transactions and up to about 50,000 transactions, it is snappy. Starts getting slow around a half million transactions where it'll begin taking a few seconds to load, to add a transaction. But to be clear, I'm not like replacing QuickBooks in the really hairy use cases. What I want is something for the simple simple accounting files. And now because I have a file that represents all of the accounting that it just did, I can share this with a colleague, I can put this in a shared network location, I can start another new Claude conversation and say, "Let's talk about this accounting file." And just point it to this text file. Kind of like QuickBooks desktop. Yeah. There's so much conversation around like who's going to build the next big a ledger like to rival QuickBooks and Xero and nobody talks about the next ledger might be large language models, Claude, ChatGPT, its ability to kind of just do it. Obviously, it can already just do it. What has historically been missing is that back end. But we already have [music] solutions to this. Thanks to these open source meme lords. And maybe my favorite part of all this is Claude gives us the power to build reporting over the top of these bean count files in any format that we want [music] that is vastly better than ye old PDF balance sheet and P&amp;L, like the QuickBooks reporting we've had forever. Let me show you just how cool this is. Oh, but first, I got to throw to Todd. Thank you, Jason. Look upon this view. It is a checklist of every task needed to close a company's books, but look here, an AI agent has already prepared two journal entries I can push direct to QuickBooks. It created a work paper to show its work. I can even drill into the agent session to see all the reasoning. It threw a couple questions to my colleague and then built an entry to book some new asset purchases and the monthly depreciation. What is this sorcery? A new feature from Ramp called Stack. If you're already a Ramp user, this feature is actually live in your Ramp already. Here's the home page, you just toggle over here to the AI experience. toggle over here to the AI experience. &gt;&gt; [music] &gt;&gt; [music] &gt;&gt; And the idea is that I can use an agent to do any of these month-end tasks. Let's look at prepaid expenses. It's built out the monthly accrual entry, created a work paper. But if we dig into the agent session, we can see it used a skill to put this entry together. Schedules and accruals, these are custom instructions that can be set up at the firm level or customized down to the client level to do pretty much any job you want. And each client over here under knowledge has their own app connectors as well. So if I flip back to uh this payroll journal entry, and come down here to the agent session, you can see it asked for a copy of the payroll journal. A teammate provides it via the Google Drive connection. It goes on to build three payroll journal entries, but back here, it suggests the creation of a payroll journal skill to help it accurately do this task each month. Gang, imagine building your own little micro agents for every task of the month-end close. You getting this? Anything they need from you, they request here on this home screen, and then they go off, they do their work. If your firm is not a Ramp user yet, you can still sign up just to get access [music] to Stack. Seems pretty darn cool. To learn more about Ramp Stack, check out the information down in the video description. Jason, right back to you, old boy. But let me show you some sweet, sweet reporting on top of these Bean Count files. It is worth noting Bean Count actually has its own like web interface called ha ha fa fa fa fa and it's okay. Basically, you give it a Bean Count file and it will do like the income statement, the balance sheet stuff. There is some customizability to this. But these days with Claude, why not just let your freak flag fly? Just build your own here, right? Look how easy this is. Make me a wee app to view the reports of any bean count file I point to it. It should have tabs for a trial balance, balance sheet, and profit and loss, and the numbers should be clickable so I can drill into them. I'll say the accounts should be nested according to the account name hierarchy in Beancount. The account naming's like parent name colon subaccount colon sub You know what that looks like. Claude whips up a little user interface, and all of a few minutes, this is what we've got to work with. We've got a trial balance tab, a balance sheet tab, a profit and loss tab with all of the all of the toggles, the wee toggles that I wanted. Car and truck, don't know why there's not any spaces. Cost of goods sold, why are you under car and truck? This is a version one, okay? You can make this whatever you want it to be. But every item here, they've got the trial balance in an in an odd order, too. We can drill into each of these to see the detail. Buck-ee's, that wasn't food. That was one of those those roast beef monstrosities, right? Yeah. You had those? Oh my gosh. So just keep going back and forth with Claude. Make this what you want it to look like. Like build it into a mobile app. I'd probably add a little file dialog here so that I can just point it to a Beancount file rather than it just sitting on top of this one file, right? But I'll I'll show you the version of reporting that I've made that I am most proud of. Back inside of Claude, it's actually under live artifacts. This is a new feature for Co-work. Basically dashboards that you can build that you can even wire up to like update from third-party data services. For a different company called Honeybee Hills. Look at this. Get out of here. Same tabs, trial balance, balance sheet, income statement. But these buttons, they dynamically generate based on whatever the last month's accounting in the file is. So the last month of data is August 25, so that's the first button that it's showing. You've got all these toggles. The sections are actually presented in the order that you would want them, income, expenses, and you can drill into all of these numbers. So this is the detail view, but it opened it in a new tab. See this? These are the tabs we were just looking at. I can close this if I want. I can come over to balance sheet. I can add any number of columns that I want. I can rearrange them around. Did those rearrange? They're the same date. That's why it Oh, no, that Yeah, no, what No. What's happening? Okay, the balances are the same. Let me make this July. Okay, there you go. The numbers are different. You can rearrange. Same on the income statement. Any number of columns, any number of date ranges. How sick is that? That is now a live artifact that I've just pinned in my cloud that points to a Beancount file. Now, you can make a live artifact style that you templatize and use for all of your clients. You can build the creation of this live artifact into a Claude skill and then share that skill with the rest of your org so that other people can make their own live artifacts the same way. And the driver of all of this stuff is a text file, [music] a Beancount text file. I have no affiliation with Beancount. It's actually an open-source thing. It's been around for a long time, but it's for programmatic accounting. And you and I, we probably don't know how to code, but as a backing for something that that Claude can make for us, where Claude is amazing at coding, this library just got incredibly useful and it is totally [music] free and it has the most powerful computer creation of all time sitting on top of that text file. So, you can just chuck a bank statement on it and it'll do it. You could pull an email onto it. Give it a voice note. Claude can make sense of all of this and translate that into like, oh, we should change this entry or that entry in the accounting system. Now, Beancount also supports basically class tracking, any number of tracking categories. Let's say you got a single bank statement activity for, say, three different rentals in there or or a duplex and you wanted to always split certain expenses for the duplex between two classes. Can do all of this stuff for you. You can work with multiple Beancount files and do consolidated reporting. Build a different live artifacts view for several companies side-by-side. When Claude is capable of being able to do a 67 transaction bookkeeping file off the top of its head with a structured data file to then serve as like the long-term storage for all the work that it's done, you have all the power of Claude with the persistence of something to actually track those transactions. And I know it sounds like a kid's toy. We're talking about a text file. And it kind of is. But I can tell you, at least in the US, the way entrepreneurship works right now, is someone will make money with one business, and as a byproduct of that, end up with seven other entities. And they're all annoying and small and don't have that much going on, but they're all one more software subscription. And they want you to do them all. So, they spin up yet another QuickBooks. Do you leave it to the end of the year and then during busy season, you got to do 12 months accounting for it. Gang, that's why I love this. And you know what? This thing is getting better every single day and a way that traditional tools are not. And so, in the end, it is a toy. In many ways, it's not for the most complex things. It's not going to give you a big structured way of interacting with the data in the same way that a traditional app would unless you built it. Before a lot of it, it's just small work that we do. I don't know. Is this just the way we get it done now? Tell me your take. I'd love to hear it down in the comments. It is a very exciting time to be a an accountant. There is so much to Claude. We didn't even touch on, you know, security, which we we touched on a lot in past videos. If you're in an accounting firm, make sure you're using either the team or the enterprise plan and disable Claude for Chrome. That is giving it the ability to go out and bang around on the web. That's kind of the riskiest thing that this could do. Tax security quite a bit on the podcast. But this is something that we and our teams, man, we need to start getting up to speed on. And if you want kind of the soup to nuts like, show me everything that I need to know about how Claude co-work works right now, I got a video for that right up here. Check this one out. No matter where you're at in your Claude journey right now, it'll get you up to speed so you can start using it to get more stuff done. Do it. I know you can do it.

## Timestamped

`[00:01]` This is an accounting file I just put
`[00:01]` together with Claude Cowork. Seriously,
`[00:04]` I'm shocked at how good Claude is at
`[00:06]` being a legit accounting system. I'm a
`[00:08]` CPA, I ran a 40-person accounting firm.
`[00:10]` I can tell you I spend a huge amount of
`[00:12]` money on QuickBooks subscriptions for a
`[00:14]` little tiny baby accounting files, but
`[00:16]` there's a better way now. Let me show
`[00:18]` you how to take basic out-of-the-box
`[00:20]` Claude that's so-so for accounting work
`[00:22]` and turn it into a proper [music]
`[00:24]` double-entry ledger system. We're going
`[00:26]` to run through why default Claude is bad
`[00:28]` at accounting, [music] the simple change
`[00:30]` to make it much better at accounting
`[00:31]` tasks, and third, how to build your own
`[00:33]` reporting layer on top of Claude that
`[00:35]` just blows the socks off the crusty old
`[00:38]` PDFs you get out of QuickBooks, okay?
`[00:40]` Seriously, what I'm about to show you
`[00:41]` would have saved me so many recurring
`[00:43]` subscriptions. You're going to love this
`[00:45]` because Claude, it is kind of magic. You
`[00:47]` can do stuff like this. You can just
`[00:49]` chuck in a pile of bank statements and
`[00:51]` be like, "Do my books, bro." Seriously,
`[00:53]` that's the prompt. "Do my bookkeeping,
`[00:55]` use the QuickBooks default chart of
`[00:56]` accounts." It just knows that. It can go
`[00:58]` figure that out. All of these bank
`[01:00]` statements totaling 6,700 transactions,
`[01:03]` statements totaling 6,700 transactions, okay?
`[01:04]` okay?
`[01:04]` Yeah, right. Off it goes like an eager
`[01:07]` little beaver. I'll get right to work.
`[01:08]` What output would you like? Give me
`[01:09]` balance sheet and P&amp;L. How should I
`[01:11]` handle personal transactions?
`[01:13]` It looks like a bookkeeping company.
`[01:15]` You want to double-check my math? Looks
`[01:16]` great. Let's spot-check and done. Gives
`[01:18]` me the headline numbers, but that's not
`[01:20]` what I want. It actually gives me
`[01:21]` spreadsheets of everything. Holy I
`[01:23]` didn't see these. Okay, this took 7
`[01:25]` minutes. I said 7.
`[01:28]` Mark, and I know you're like, "There's
`[01:29]` no way it's right, though." No, but it
`[01:32]` is. Like the balance sheet foots. You
`[01:34]` know, it had to make some guesses
`[01:35]` because there are some external
`[01:37]` transfers, like to another savings
`[01:39]` account, payments to a credit card, but
`[01:40]` it calls all this stuff out as pretty
`[01:42]` intelligent. The savings line is the
`[01:44]` cumulative amount transferred out to
`[01:46]` some other checking account. I don't
`[01:47]` have the statements. And the credit card
`[01:48]` and loan payments, I parked them in
`[01:50]` equity because I don't have an opening
`[01:51]` balance. I don't have statements. And
`[01:53]` honestly, it's so good that I'm like,
`[01:55]` "Did you actually just classify 6,700
`[01:58]` transactions? The behind the scenes of
`[01:59]` how it did it, actually pretty
`[02:01]` interesting. First, it's got to pull all
`[02:02]` the transactions out of the bank
`[02:04]` statements. Then it cleans up the vendor
`[02:06]` names because they are like messy,
`[02:08]` right? They got all those numbers. But
`[02:09]` then it made a pattern rule classifier.
`[02:11]` It created about 50 rules. These are
`[02:13]` basically bank rules that it made on the
`[02:15]` fly to say, every time you see this
`[02:17]` company, it should be categorized this
`[02:19]` way. That ended up handling 96% of
`[02:22]` transactions, those bank rules. The
`[02:23]` remaining 250 it actually had an
`[02:26]` uncategorized and it did another pass
`[02:28]` going out looking up what those should
`[02:30]` be. But at the end of the day,
`[02:31]` everything balances. The only thing that
`[02:33]` might be wrong is maybe the
`[02:34]` classifications weren't the same way
`[02:36]` that you would do them. But but gang, I
`[02:38]` just gave it 12 months of bank
`[02:40]` statements. Those were images, not text,
`[02:42]` images in the PDFs. It did all this in 7
`[02:45]` minutes. Oh.
`[02:46]` Yeah, honey, I got bad news. But in some
`[02:48]` ways it's like a party trick because
`[02:51]` how's anybody else going to work in this
`[02:53]` accounting file? I feel like I need a
`[02:54]` proper reporting system on top of it and
`[02:56]` it's not backed by anything. Like
`[02:58]` there's no database here for like
`[03:00]` persistent storage of the transactions
`[03:02]` themselves. This is what makes vanilla
`[03:04]` cloud very limited but has an ever so
`[03:07]` simple solution. You ready? It's called
`[03:09]` Beancount. Hang on. Did he say
`[03:11]` Beancount. Hang on. Did he say Beancount?
`[03:12]` Beancount?
`[03:12]` Beancount. I will explain. Here's
`[03:14]` another new prompt. Use Beancount to do
`[03:16]` my bookkeeping here for me, please. Use
`[03:18]` QuickBooks chart of accounts. Stick
`[03:19]` closely to the Beancount system. So we
`[03:22]` have a proper Beancount file for the
`[03:24]` transaction database. Exact same bank
`[03:26]` statements. Off it scurries. Good.
`[03:28]` Beancount is installed. Let me tell you
`[03:30]` about this Beancounting. Beancount is an
`[03:33]` open source system for storing
`[03:34]` double-entry accounting transactions in
`[03:36]` a text file. So if QuickBooks has like a
`[03:38]` big old sort of complicated database,
`[03:41]` Beancount says, how do we do that in
`[03:43]` just a flat old text file? Now, this is
`[03:46]` a legitimate project. 5,500 stars. 87
`[03:49]` nerds have contributed to Look AT THAT
`[03:51]` GUY. WHAT were you doing? This guy has
`[03:54]` children, but I appreciate them
`[03:55]` nonetheless. Because this is free for
`[03:57]` anybody to swipe. And what it gives
`[03:59]` Claude that Claude doesn't natively have
`[04:02]` is a storage system. Now, look at this.
`[04:04]` So, this process completes and the
`[04:06]` result, it's this bean count file, dot
`[04:08]` bean count. Look what's in it. Whole
`[04:10]` pile of text. You got all the accounts,
`[04:12]` you got a journal. But this is a
`[04:13]` structured programmatic way to store
`[04:16]` transactions and up to about 50,000
`[04:19]` transactions, it is snappy. Starts
`[04:22]` getting slow around a half million
`[04:23]` transactions where it'll begin taking a
`[04:25]` few seconds to load, to add a
`[04:27]` transaction. But to be clear, I'm not
`[04:29]` like replacing QuickBooks in the really
`[04:32]` hairy use cases. What I want is
`[04:33]` something for the simple
`[04:35]` simple accounting files. And now because
`[04:38]` I have a file that represents all of the
`[04:41]` accounting that it just did, I can share
`[04:43]` this with a colleague, I can put this in
`[04:44]` a shared network location, I can start
`[04:46]` another new Claude conversation and say,
`[04:49]` "Let's talk about this accounting file."
`[04:50]` And just point it to this text file.
`[04:53]` Kind of like QuickBooks desktop. Yeah.
`[04:55]` There's so much conversation around like
`[04:57]` who's going to build the next big a
`[04:58]` ledger like to rival QuickBooks and Xero
`[05:01]` and nobody talks about the next ledger
`[05:03]` might be
`[05:05]` large language models, Claude, ChatGPT,
`[05:07]` its ability to kind of just do it.
`[05:09]` Obviously, it can already just do it.
`[05:11]` What has historically been missing is
`[05:13]` that back end. But we already have
`[05:15]` [music] solutions to this. Thanks to
`[05:16]` these open source meme lords. And maybe
`[05:19]` my favorite part of all this is Claude
`[05:20]` gives us the power to build reporting
`[05:23]` over the top of these bean count files
`[05:25]` in any format that we want [music] that
`[05:27]` is vastly better than ye old PDF balance
`[05:32]` sheet and P&amp;L, like the QuickBooks
`[05:33]` reporting we've had forever. Let me show
`[05:36]` you just how cool this is. Oh, but
`[05:38]` first, I got to throw to Todd. Thank
`[05:40]` you, Jason. Look upon this view. It is a
`[05:42]` checklist of every task needed to close
`[05:44]` a company's books, but look here, an AI
`[05:46]` agent has already prepared two journal
`[05:48]` entries I can push direct to QuickBooks.
`[05:50]` It created a work paper to show its
`[05:51]` work. I can even drill into the agent
`[05:54]` session to see all the reasoning. It
`[05:55]` threw a couple questions to my colleague
`[05:57]` and then built an entry to book some new
`[05:59]` asset purchases and the monthly
`[06:01]` depreciation. What is this sorcery? A
`[06:03]` new feature from Ramp called Stack.
`[06:07]` If you're already a Ramp user, this
`[06:08]` feature is actually live in your Ramp
`[06:10]` already. Here's the home page, you just
`[06:11]` toggle over here to the AI experience.
`[06:14]` toggle over here to the AI experience. &gt;&gt; [music]
`[06:14]` &gt;&gt; [music]
`[06:14]` &gt;&gt; And the idea is that I can use an agent
`[06:16]` to do any of these month-end tasks.
`[06:19]` Let's look at prepaid expenses. It's
`[06:20]` built out the monthly accrual entry,
`[06:22]` created a work paper. But if we dig into
`[06:24]` the agent session, we can see it used a
`[06:26]` skill to put this entry together.
`[06:28]` Schedules and accruals, these are custom
`[06:30]` instructions that can be set up at the
`[06:32]` firm level or customized down to the
`[06:34]` client level to do pretty much any job
`[06:36]` you want. And each client over here
`[06:38]` under knowledge has their own app
`[06:39]` connectors as well. So if I flip back to
`[06:42]` uh this payroll journal entry, and come
`[06:44]` down here to the agent session, you can
`[06:46]` see it asked for a copy of the payroll
`[06:47]` journal. A teammate provides it via the
`[06:49]` Google Drive connection. It goes on to
`[06:51]` build three payroll journal entries, but
`[06:52]` back here, it suggests the creation of a
`[06:54]` payroll journal skill to help it
`[06:56]` accurately do this task each month.
`[06:59]` Gang, imagine building your own little
`[07:00]` micro agents for every task of the
`[07:03]` month-end close. You getting this?
`[07:05]` Anything they need from you, they
`[07:06]` request here on this home screen, and
`[07:09]` then they go off, they do their work. If
`[07:10]` your firm is not a Ramp user yet, you
`[07:12]` can still sign up just to get access
`[07:14]` [music] to Stack. Seems pretty darn
`[07:16]` cool. To learn more about Ramp Stack,
`[07:17]` check out the information down in the
`[07:19]` video description. Jason, right back to
`[07:21]` you, old boy.
`[07:22]` But let me show you some sweet, sweet
`[07:24]` reporting on top of these Bean Count
`[07:26]` files. It is worth noting Bean Count
`[07:27]` actually has its own like web interface
`[07:30]` called ha ha fa fa
`[07:32]` fa fa and it's okay. Basically, you give
`[07:34]` it a Bean Count file and it will do like
`[07:36]` the income statement, the balance sheet
`[07:38]` stuff. There is some customizability to
`[07:40]` this. But these days with Claude, why
`[07:42]` not just let your freak flag fly? Just
`[07:44]` build your own here, right? Look how
`[07:46]` easy this is. Make me a wee app to view
`[07:48]` the reports of any bean count file I
`[07:50]` point to it. It should have tabs for a
`[07:52]` trial balance, balance sheet, and profit
`[07:53]` and loss, and the numbers should be
`[07:55]` clickable so I can drill into them. I'll
`[07:56]` say the accounts should be nested
`[07:58]` according to the account name hierarchy
`[08:00]` in Beancount. The account naming's like
`[08:02]` parent name colon subaccount colon sub
`[08:05]` You know what that looks like. Claude
`[08:06]` whips up a little user interface, and
`[08:07]` all of a few minutes, this is what we've
`[08:09]` got to work with. We've got a trial
`[08:10]` balance tab, a balance sheet tab, a
`[08:12]` profit and loss tab with all of the all
`[08:14]` of the toggles, the wee toggles that I
`[08:16]` wanted. Car and truck, don't know why
`[08:18]` there's not any spaces. Cost of goods
`[08:19]` sold, why are you under car and truck?
`[08:21]` This is a version one, okay? You can
`[08:23]` make this whatever you want it to be.
`[08:24]` But every item here, they've got the
`[08:26]` trial balance in an in an odd order,
`[08:27]` too. We can drill into each of these to
`[08:30]` see the detail. Buck-ee's, that wasn't
`[08:32]` food. That was one of those those roast
`[08:33]` beef monstrosities, right?
`[08:36]` Yeah. You had those? Oh my gosh. So just
`[08:39]` keep going back and forth with Claude.
`[08:41]` Make this what you want it to look like.
`[08:43]` Like build it into a mobile app. I'd
`[08:45]` probably add a little file dialog here
`[08:47]` so that I can just point it to a
`[08:48]` Beancount file rather than it just
`[08:50]` sitting on top of this one file, right?
`[08:52]` But I'll I'll show you the version of
`[08:53]` reporting that I've made that I am most
`[08:55]` proud of. Back inside of Claude, it's
`[08:57]` actually under live artifacts. This is a
`[08:59]` new feature for Co-work. Basically
`[09:01]` dashboards that you can build that you
`[09:03]` can even wire up to like update from
`[09:05]` third-party data services. For a
`[09:07]` different company called Honeybee Hills.
`[09:10]` Look at this. Get out of here. Same
`[09:11]` tabs, trial balance, balance sheet,
`[09:13]` income statement. But these buttons,
`[09:14]` they dynamically generate based on
`[09:16]` whatever the last month's accounting in
`[09:18]` the file is. So the last month of data
`[09:20]` is August 25, so that's the first button
`[09:22]` that it's showing. You've got all these
`[09:23]` toggles. The sections are actually
`[09:25]` presented in the order that you would
`[09:26]` want them, income, expenses, and you can
`[09:28]` drill into all of these numbers. So this
`[09:31]` is the detail view, but it opened it in
`[09:32]` a new tab. See this? These are the tabs
`[09:34]` we were just looking at. I can close
`[09:35]` this if I want. I can come over to
`[09:37]` balance sheet. I can add any number of
`[09:39]` columns that I want. I can rearrange
`[09:41]` them around. Did those rearrange?
`[09:43]` They're the same date. That's why it Oh,
`[09:44]` no, that Yeah, no, what No. What's
`[09:46]` happening? Okay, the balances are the
`[09:48]` same. Let me make this July. Okay, there
`[09:50]` you go. The numbers are different. You
`[09:51]` can rearrange. Same on the income
`[09:52]` statement. Any number of columns, any
`[09:54]` number of date ranges. How sick is that?
`[09:57]` That is now a live artifact that I've
`[09:59]` just pinned in my cloud that points to a
`[10:02]` Beancount file. Now, you can make a live
`[10:04]` artifact style that you templatize and
`[10:06]` use for all of your clients. You can
`[10:08]` build the creation of this live artifact
`[10:10]` into a Claude skill and then share that
`[10:12]` skill with the rest of your org so that
`[10:14]` other people can make their own live
`[10:16]` artifacts the same way. And the driver
`[10:18]` of all of this stuff is a text file,
`[10:20]` [music] a Beancount text file. I have no
`[10:23]` affiliation with Beancount. It's
`[10:24]` actually an open-source thing. It's been
`[10:25]` around for a long time, but it's for
`[10:27]` programmatic accounting. And you and I,
`[10:30]` we probably don't know how to code, but
`[10:31]` as a backing for something that that
`[10:33]` Claude can make for us, where Claude is
`[10:35]` amazing at coding, this library just got
`[10:37]` incredibly useful and it is totally
`[10:39]` [music] free and it has the most
`[10:41]` powerful computer creation of all time
`[10:43]` sitting on top of that text file. So,
`[10:45]` you can just chuck a bank statement on
`[10:47]` it and it'll do it. You could pull an
`[10:49]` email onto it. Give it a voice note.
`[10:51]` Claude can make sense of all of this and
`[10:53]` translate that into like, oh, we should
`[10:56]` change this entry or that entry in the
`[10:57]` accounting system. Now, Beancount also
`[10:59]` supports basically class tracking, any
`[11:02]` number of tracking categories. Let's say
`[11:03]` you got a single bank statement activity
`[11:06]` for, say, three different rentals in
`[11:07]` there or or a duplex and you wanted to
`[11:10]` always split certain expenses for the
`[11:12]` duplex between two classes. Can do all
`[11:14]` of this stuff for you. You can work with
`[11:15]` multiple Beancount files and do
`[11:17]` consolidated reporting. Build a
`[11:19]` different live artifacts view for
`[11:21]` several companies side-by-side. When
`[11:23]` Claude is capable of being able to do a
`[11:25]` 67 transaction bookkeeping file off the
`[11:28]` top of its head with a structured data
`[11:30]` file to then serve as like the long-term
`[11:32]` storage for all the work that it's done,
`[11:34]` you have all the power of Claude with
`[11:36]` the persistence of something to actually
`[11:38]` track those transactions. And I know it
`[11:40]` sounds like a kid's toy. We're talking
`[11:41]` about a text file. And it kind of is.
`[11:44]` But I can tell you, at least in the US,
`[11:45]` the way entrepreneurship works right
`[11:47]` now, is someone will make money with one
`[11:49]` business, and as a byproduct of that,
`[11:51]` end up with seven other entities. And
`[11:53]` they're all annoying and small and don't
`[11:55]` have that much going on, but they're all
`[11:57]` one more software subscription. And they
`[11:58]` want you to do them all. So, they spin
`[12:00]` up yet another QuickBooks. Do you leave
`[12:03]` it to the end of the year and then
`[12:04]` during busy season, you got to do 12
`[12:05]` months accounting for it. Gang, that's
`[12:07]` why I love this. And you know what? This
`[12:09]` thing is getting better every single day
`[12:11]` and a way that traditional tools are
`[12:13]` not. And so, in the end, it is a toy. In
`[12:16]` many ways, it's not for the most complex
`[12:18]` things. It's not going to give you a big
`[12:19]` structured way of interacting with the
`[12:21]` data in the same way that a traditional
`[12:23]` app would unless you built it. Before a
`[12:24]` lot of it, it's just small work that we
`[12:27]` do. I don't know. Is this just the way
`[12:29]` we get it done now? Tell me your take.
`[12:30]` I'd love to hear it down in the
`[12:31]` comments. It is a very exciting time to
`[12:33]` be a an accountant. There is so much to
`[12:36]` Claude. We didn't even touch on, you
`[12:37]` know, security, which we we touched on a
`[12:39]` lot in past videos. If you're in an
`[12:41]` accounting firm, make sure you're using
`[12:42]` either the team or the enterprise plan
`[12:44]` and disable Claude for Chrome. That is
`[12:47]` giving it the ability to go out and bang
`[12:48]` around on the web. That's kind of the
`[12:49]` riskiest thing that this could do. Tax
`[12:52]` security quite a bit on the podcast. But
`[12:53]` this is something that we and our teams,
`[12:55]` man, we need to start getting up to
`[12:56]` speed on. And if you want kind of the
`[12:58]` soup to nuts like, show me everything
`[13:00]` that I need to know about how Claude
`[13:01]` co-work works right now, I got a video
`[13:03]` for that right up here. Check this one
`[13:05]` out. No matter where you're at in your
`[13:07]` Claude journey right now, it'll get you
`[13:08]` up to speed so you can start using it to
`[13:10]` get more stuff done.
`[13:12]` Do it. I know you can do it.
