# Link registry

Every URL that goes in a description comes from here or from the live skeleton
pull. **Never type a URL from memory and never guess a repo path** — a dead link
in the top block is the most visible possible mistake.

---

## Fixed — in every description

| Slot | What | URL |
|------|------|-----|
| 1 (always first) | The Skool community (name/price per `backbone/offer.md`). The only offer, the only CTA. | https://www.skool.com/leveragelab/about |
| Follow block | Instagram | https://www.instagram.com/jasoncooperson/ |
| Follow block | TikTok | https://www.tiktok.com/@jasoncooperson |

The slot-1 line is **rewritten every video** to name what that video's viewer
actually wants from the community (the pre-built project from *this* build), then
the same Skool URL underneath. Look at the skeleton for how the newest one reads.

Never in a description: an "apply" link, a call-booking link, a DM-to-call CTA,
or any high-ticket DFY offer. That was retired 2026-06-09.

## Tools already used on the channel

Resolved and shipped before, safe to reuse:

| Tool | URL | Appeared in |
|------|-----|-------------|
| HyperFrames (motion graphics toolkit) | https://github.com/heygen-com/hyperframes | Premiere Pro build, video editor build |
| Premiere Pro MCP | https://github.com/hetpatel-11/Adobe_Premiere_Pro_MCP | Premiere Pro build |
| Beancount (double-entry accounting) | https://github.com/beancount/beancount | Finance build |
| DaVinci Resolve MCP (the bridge that lets Claude control Resolve) | https://github.com/samuelgursky/davinci-resolve-mcp | DaVinci Resolve build |
| DaVinci Resolve Studio (not affiliated, just where you get it) | https://www.blackmagicdesign.com/products/davinciresolve/studio | DaVinci Resolve build |

Every video-editor build carries a `🎁` free-resource block right under slot 1: the
free blueprint + starter prompt, a public Claude artifact. Always this exact URL
(the one the artifact's Share → Copy link gives out; it loads instantly for
logged-out viewers):

https://claude.ai/artifact/BYH6Mcma5to3kt2KogkEzB

Never the `claude.ai/code/artifact/<uuid>` form. That's the owner URL for the same
page and sits on a spinner for about 10 seconds for viewers. All 7 video-editor
descriptions were unified onto the short link 2026-09-29.

## Referral links — only when the video actually uses that product

These earn Jason money, so they're worth including, but only in a video where he
genuinely walks through the product. Dropping them into an unrelated video reads
as spam. When two or more appear, group them under a `💳` block with a plain
`(referral links — most get you a bonus)` note, the way the finance video did.

| Product | URL |
|---------|-----|
| Sequence (money routing) | https://go.getsequence.io/landing/join-and-earn-75?code=5EHKY |
| Origin (transaction tracking) | https://www.useorigin.com/referral?referral_code=0d21a670-5270-4467-8d2c-df35e1da243a |
| Mercury (business checking) | https://mercury.com/r/creator-economy-llc |
| Amex Business Gold | https://americanexpress.com/en-us/referral/businessgold-card?ref=JASONCDJTx&xl=cp01 |
| Amex Personal Gold | https://americanexpress.com/en-us/referral/gold-card?ref=JASONCuz9s&xl=cp01 |
| Schwab | https://www.schwab.com/client-referral?refrid=REFERAPZFB8B8 |

## A tool that isn't in this file

The script names something new (a repo, an MCP, an app, a model). Then:

1. Search for the official source: the GitHub repo, the product's own domain. Not
   a blog post, not a listicle, not a mirror.
2. Open it and confirm it's the thing Jason actually demoed in the video.
3. Put it in the draft with the URL visible, and flag it to Jason in chat as new:
   `new link — HyperFrames → github.com/... (verify)`.
4. After he confirms, add a row to the table above so the next video reuses it.

If the search doesn't produce a confident answer, leave the block out of the
draft and tell him which tool needs a link. An empty slot is fixable in ten
seconds; a wrong URL ships to 10K subscribers.
