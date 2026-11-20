# Release notes: Content OS

The top section is the current build. `packaging/package-for-client.sh` stamps its version into the
zip as `VERSION` and copies this file in; `update.py` shows a client every section newer than the
version they had. Add a new `## <version>` section at the top for every ship; version = the ship date,
`.2`, `.3` suffix for a second ship the same day. Bullets are client-facing and PLAIN: one short line
each, what changed for them in everyday words, no jargon, no internal names, no em dashes; a creator
reads the whole section in ten seconds. After a ship, `ship-to-skool.py` records the version in
`packaging/shipped-blobs.json` + `shipped-history.pack` (keep both: they are how an install from any
earlier version merges cleanly).

Versions shipped before updates existed carry no VERSION file; their fingerprints are recorded under
the ship date: 2026.09.11, 2026.09.23, 2026.09.26, 2026.09.29.

## 2026.11.02.2

- Carousels now render with your own Google Chrome: setup skips a 130 MB download, and a computer cleanup can no longer break carousel exports. No Chrome yet? Get it at google.com/chrome

## 2026.11.02

- Instagram feed research uses every button Instagram's website has: it hides off-niche posts, saves the good ones, and favorites the right accounts
- Instagram feed research works again on Instagram's new layout (scrolling and like counts had stopped working)
- Feed research asks your niche in one line the first time you run it, so you can start before the full brand kit
- New on Mac: photo finder pulls your best photos of yourself out of your camera roll. It downloads what it needs the first time you ask for it, not during setup

## 2026.10.30

- Posting: a normal 1080p reel export now goes to Instagram as is, no extra re-encode first
- Recording: the clap test skips your speech, measures only the real claps, and zooms in on your hands so contact is easy to spot
- Recording: clearer steps for re-checking mic sync before a session that matters
- Instagram feed research: finds an account's top reels faster and keeps loading when Chrome is in the background
- Removed a folder of private notes that was included by mistake in earlier versions

## 2026.09.29.2

Updating is built in now: a new version merges into the folder you already use, and your own work stays yours.

- To update, download the new zip, open the folder you already use in Claude Code and say "update". Claude finds the newest download in your Downloads folder itself
- Your brand kit, backbone, voice corpus, research, transcripts, carousels and everything else you made stay exactly as they are
- Anything you and the new version both changed is sorted out with you, never overwritten
- Changed your mind after an update? Tell Claude "undo the update". Anything you did since stays
- Your own standing rules for Claude now have a home no update touches: my-rules.md
- Installed before this version? This one time, unzip the new download, open THAT folder in Claude Code and say "update my Content OS". Claude finds your folder and runs update.py on it. After that, "update" in your own folder is all it takes
