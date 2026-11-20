# Format breakdown: "I Fully Automated My Video Editing Using Claude Code (Full Walkthrough)"

- **Source:** https://www.youtube.com/watch?v=HzXD4GVqXwM
- **Creator:** Christian Peverelli (We Are No Code)
- **Posted:** 2026-10-04 · **Runtime:** 16:58 (1018s)
- **Stats at pull (2026-11-13):** 915,890 views, 13,643 likes, 502 comments (69x channel median)
- **Transcript:** `transcripts/url/i-fully-automated-my-video-editing-using-claude-code-full-wa_2026-11-13.md` (whisper small.en; captions 429'd)
- **Comments:** top 100 by "top" sort, pulled with yt-dlp
- **Purpose:** format skeleton for Jason's next long-form. Structure, not content.

## Official chapters (from the description)

0:00 Introduction · 0:31 The seven roles of the team · 5:36 The role of the skill · 6:08 System setup guide · 9:41 Training your AI editor · 11:36 Editing in action · 15:12 Costs and conclusion

## Beat-by-beat skeleton

| # | Time | Beat | Job for the viewer | What's on screen / said |
|---|------|------|--------------------|-------------------------|
| 1 | 0:00-0:18 | Self-proving hook | Proof the claim is real, in the first frame | "Everything you're seeing in this video was edited by my Claude Code system while I was asleep." Three animations fire on cue ("like this one, or this one, or this one"). Closes with the objection-killer: "no, I don't know how to code." |
| 2 | 0:18-0:31 | Promise stack | Tells you exactly what you'll get, so you stay | Lists the deliverables in order: tools, setup, how he taught it his style, exact cost, money saved. "Let's go." |
| 3 | 0:31-0:44 | Frame: the team you replace | Gives a mental model that makes a complex stack simple | "Making a video like this used to take a small team." He keeps one job (record + feedback); every other job goes to a tool. |
| 4 | 0:44-1:34 | Role 1: Editor = Claude Code | Anchors the hub of the system | Claude Code desktop, local mode, uses his computer and files, "project manager of the entire video." Ends on a problem ("Claude can't actually hear my videos") that bridges to role 2. |
| 5 | 1:34-2:11 | Role 2: Transcriber = Parakeet | Solves the problem just raised | Free, by NVIDIA. Comic beat ("No, not Doritos or Lays... Mmm, chips. Get back to it."). Explains timestamps let Claude pick takes. |
| 6 | 2:11-2:45 | Role 3: Animator = HyperFrames | Kills the "After Effects" barrier | Free, by HeyGen. "Claude writes each animation like a tiny website," renders 4K. Costs nothing. |
| 7 | 2:45-3:43 | Role 4: Researcher = Chrome | Shows a non-obvious capability | Claude drives Chrome to screenshot X posts / pages, scroll-record, highlight lines, zoom. "I can just say what happens and the proof shows up on screen." |
| 8 | 3:43-4:18 | Role 5: Screen editor = Tella MCP | Covers tutorial creators specifically | Tella records face + screen; MCP lets Claude do cuts, zooms, layout. |
| 9 | 4:18-5:03 | Role 6: Sound designer = Epidemic Sound | Taste layer, shows it can be trained | Paid, connected to Claude. His music rules: suspense on hook, low lo-fi hip-hop after. Teases "I'll talk about how I set up all of this right after." |
| 10 | 5:03-5:28 | Role 7: Finisher = FFmpeg | Closes the team, adds QA credibility | Free, 20+ years old. Removes black frames, checks A/V sync before he sees it. |
| 11 | 5:28-6:08 | The skill (the secret sauce) | Names the thing that ties it together, sets up the giveaway | "A skill is simply just a file of instructions." His is "youtube-edit", about 1,400 lines, Claude built it. "Claude runs the tools, I tell Claude what good looks like." Reassurance: "I'm not technical and you probably aren't either." |
| 12 | 6:08-9:41 | Setup walkthrough (screen) | Lets a beginner follow along click by click | Download desktop app, $20 plan is enough, Claude Code tab, Local, pick folder, permissions to auto, latest model for setup, Settings toggle for browsing. Gives the exact setup prompt. Customize > Connectors for Tella + Epidemic. Save as a skill, new thread, first test. At 9:34 mid-video CTA: download his skill in the free community. |
| 13 | 9:41-11:34 | Training story | Shows taste is learnable, sets realistic expectations | Started with hooks only, timestamped notes. "10 days in" started on sound, tried 8-10 SFX. Key rule: after feedback, tell it to save the lesson to the skill. Now 36 rules. "It never made that same mistake again." |
| 14 | 11:34-13:38 | Live run | The demo payoff: raw footage in, edit out | "Enough talking." Drops a raw hook file, types the prompt, watches Claude probe the clip and run Parakeet. Admits it takes 10-20 min, then plays V1, which is the video's own opening. |
| 15 | 13:38-15:11 | Review + feedback loop | Shows the human-in-the-loop workflow | "2:46 of raw footage into 31 seconds." Gives a revision note (add suspense track), timestamped notes, then "learn from what we just did and add it to the skill." Reveals the whole video was fed in overnight: "I'm the director, Claude's the editor." |
| 16 | 15:11-16:10 | Cost to the dollar | Concrete ROI, the answer to the obvious question | Max $200/mo but measured tokens: $24/video at most. HyperFrames + Parakeet free, Tella approx $2/video, Epidemic approx $1/video. "$27 per video" vs editors at $250-$1,000+. |
| 17 | 16:10-16:58 | Speed benefit + CTA + end screen | Second ROI (time), then the offer and next watch | Same-day plan-shoot-edit-release vs 3-7 days; human revisions repeated mistakes. Free skill in "We Are No Code" free community. End screen to his OpenAI Dev Day video edited with the skill. |

## Hook mechanic (0:00-0:31)

- The hook is a closed loop: the opening IS the output of the system he's about to explain, and he says so in the first sentence. Every animation he points at ("like this one") is live proof, so the viewer never has to take the claim on faith.
- Three stacked hooks in 15s: outcome ("edited while I was asleep"), sensory proof (three animations on cue), objection kill ("I don't know how to code").
- Then an explicit table of contents (tools, setup, style training, exact cost, savings). Cost is promised up front and paid off last, which is a retention anchor across the whole runtime.
- At 13:19 the hook is replayed as "V1" and at 14:33 he reveals "what you see at the beginning of this video is the actual final product." The hook pays off twice.

## Spoken intro (verbatim, 0:00-0:44)

> Everything you're seeing in this video was edited by my Claude Code system while I was asleep. Every cut, every sound, every animation, like this one, or this one, or this one, was made without touching a timeline and no, I don't know how to code. So today I'm going to pull the curtain and show you exactly how I built this expert editor step by step. The tools, how to set them up, how I taught it my style, the exact cost, and how I'm saving thousands of dollars a month. Let's go. Okay, so making a video like this one used to take a small team. And to be clear, I still have one job to hit record and also to provide feedback. But in my system, every other job goes to a different tool. So I'm going to break these down for you one by one.

## Giveaway and CTAs

- **What he gives away:** his "youtube-edit" editing skill (the about 1,400-line instruction file).
- **How you get it:** join his FREE Skool community (skool.com/wearenocode). It's the first line of the description ("✅ Free Editing Skill") and his own comment, which he posted with the same line (17 likes, presumably pinned). No email gate on YouTube itself; the Skool join is the gate.
- **CTAs:**
  - 5:01 soft retention tease: "I'll talk about how I set up all of this right after."
  - 4:41 retention tease: "we'll talk about pricing at the end."
  - 9:34 mid-video: "if you'd like to just download my skill... inside my free community. Link is below." Placed exactly where setup ends and the hard part (fine-tuning taste) begins, so the shortcut is offered at the moment of pain.
  - 16:34 closing: "giving you this skill for free inside of my free community. It's called We Are No Code."
  - 16:44 end screen: watch his OpenAI Dev Day video, framed as "see the editing skill in action for a full video."
- No subscribe ask in the spoken script. No paid offer pitched. Affiliate links (Emergent, Base44, Lovable, Hostinger, HeyReach) sit in the description only, none of them for tools used in the video.

## Proof devices

- The video itself as proof (opening hook edited by the system, replayed as V1).
- Raw footage shown as messy ("I stop in the middle of the hook and look at my notes").
- Claude's live run on screen: skill found, clip probed, Parakeet transcribing.
- Compression number: 2:46 raw to 0:31 finished.
- System size numbers: about 1,400-line skill, 36 rules, 10 days of training, 8-10 SFX tried.
- Cost to the dollar: $24 tokens (measured by Claude), $27 all-in per video vs $250-$1,000+ per editor video.
- Time: same-day release vs 3-7 days.
- Missing: no side-by-side vs a human edit, no full long-form output shown in this video (it's pushed to another video), no Claude output files/timeline/skill text shown in detail.

## Pacing

- First real payoff: the hook itself is the payoff at 0:05. Next concrete payoff (something you can do) starts at 6:08. The live demo starts at 11:36, about 68% through.
- 0:31-6:08 (5.5 min) is explanation-heavy: seven roles, each 30-60s, each framed as a job title. Likely talking head with tool logos/animations over it (HyperFrames showcase), since the video's own edit demonstrates the animator.
- 6:08-9:41 and 11:36-15:11 are screen recordings (Claude desktop UI, connectors, run). Rough split: about 40% talking head + animation, about 45% screen, rest mixed.
- Bridges: each role ends on the problem the next role solves ("Claude can't hear my videos" > transcriber; "up until now we've just been talking visuals" > sound designer; "none of those know what my video is supposed to look like" > skill). Open loops for pricing and setup are planted early and closed late. "All right, my friends, enough talking" signals the demo.
- One comic beat (chips at 1:52) breaks the monotony of the list.

## Why it performed

1. **The title promise is proven in second one.** The opening is the product. Comments show viewers then scanned the whole video for evidence it was AI ("16 minutes in before I saw a blink", 132 likes; "Its an ai avatar of haygen", 9) which is watch time and engagement either way.
2. **"Team of 7 jobs" framing.** Turns a scary toolchain into a familiar org chart. A commenter rewrote the whole list as notes (2 likes), meaning it was easy to retain and screenshot.
3. **Non-technical permission + mostly free stack.** "I don't know how to code," $20 plan is enough, four of seven tools free. Comments: "no BS - to the point" (4), "you not selling something" (3), a 65-year-old asking if they can do it.
4. **Concrete dollar math vs an editor.** $27 vs $250-$1,000+ is shareable and promised from 0:27, so people stay to hear it.
5. **Free skill = do it tonight.** Several comments report actually building it ("downloaded the free skill, and I have a full podcast edit complete"; "took a few hours to set up but this has totally changed my YouTube game").
6. **Controversy fuel.** "AI replaces editors" pulled in editors to argue: the top comment (252) is a rebuttal, plus 15 and 11-like replies. Debate drove comment volume (502).

## Gaps (the opening for a better version)

- **Complex footage, not just talking heads.** "Give it just a little complex video... with multiple retakes... it will fold like a cheap chair" (252). "works very well with talking hat videos... beach... mountains... I don't know how to cut" (4). "This would work best with scripted Teleprompter content, and just one person talking" (2).
- **Taste and pacing are unproven.** "AI isn't nuanced and it isn't me" (15). "an assistant editor, rough cuts maybe, but anything with taste, pacing or intentionality, it won't get there" (11). "Curious how well it handles pacing for longer videos" (6).
- **The researcher role was skimmed.** "I was really hoping you would have gone into greater detail about how your researcher works. That would be a HUGE unlock." (3)
- **Only a 31s hook was demoed.** The full-video edit is pushed to another video. A full long-form run start to finish is the obvious upgrade.
- **Regression testing of the skill.** "When you add a new rule, do you rerun an older clip to check that it hasn't broken something?" (2)
- **Things AI edit still does badly:** "color grading is trash, and for animation to literally have to indicate every frame" (1); "It mostly starts with the worst quality ever" (0); stabilization asked about (2); "connecting and training all those tools became a job itself" (0).
- **Packaging fatigue/trust.** "if i see one more video with 'ITS OVER' in the thumbnail..." (173); "classifies creators who do this as: do not take them serious" (8); "The most common = slop" (9). The thumbnail drew views but cost trust.
- **Access questions unanswered:** older beginners, iPhone-only, non-English languages, ChatGPT/Codex users.

## Modeling notes for Jason

- Steal: self-proving opener, explicit content stack with cost promised up front, roles-as-team list with problem-to-solution bridges, giveaway offered right at the "fine-tuning is the hard part" moment, demo that replays the hook as output.
- Beat him on: a full long-form run (not just a hook), messy multi-take footage, a real before/after vs a human edit, a deeper researcher/b-roll section, how the skill is regression-checked, and actual Premiere handoff (Jason's video-editor project already does rough cut + Premiere, a level past "Claude renders it").
