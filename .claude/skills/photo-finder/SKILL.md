---
name: photo-finder
description: "Finds the most aesthetic, classy lifestyle photos of the user in their iPhone camera roll (macOS Photos library via iCloud) without Claude reviewing photos one by one. osxphotos filters to the user's own face (Photos > People), still photos only, no screenshots/selfies/hidden; a local SigLIP pass scores every candidate (Apple's own hidden aesthetic score + Aesthetic Predictor v2.5 + a 'high-end lifestyle' vibe score), collapses near-duplicates, and renders numbered contact sheets. Claude picks from the sheets, then the picks export as full-res originals (iCloud download included) into a Photos album and ~/Downloads. Triggers: find my best photos, aesthetic photos of me, lifestyle photos, camera roll b-roll, photos for thumbnails, best pictures of myself, classy photos of me, photo finder, dig through my camera roll."
---

# Photo Finder: the camera roll, ranked

Apple already scored every photo (face recognition, scene labels, 27 hidden aesthetic scores in Photos.sqlite). osxphotos reads them; a local SigLIP model adds taste. Claude only looks at contact sheets at the very end: 8 images for the top 200, not 200 images.

## Requirements (one-time)

- macOS with iCloud Photos syncing to `~/Pictures/Photos Library.photoslibrary`.
- **Full Disk Access for the Claude Code binary**, not just Claude.app. The desktop app launches Claude Code through a `disclaimer` helper, so macOS checks the bundle at `~/Library/Application Support/Claude/claude-code/<version>/<hash>/claude.app`. Add that one in System Settings > Privacy & Security > Full Disk Access, then relaunch. Check: `sqlite3 "file:$HOME/Pictures/Photos Library.photoslibrary/database/Photos.sqlite?mode=ro&immutable=1" "select count(*) from ZASSET"` prints a number.
- The user's face is named in Photos > People (the script defaults to the most-photographed named person; `--person` overrides).
- First run builds `~/.cache/content-os/photo-finder-venv` (torch + SigLIP, a few minutes) and downloads SigLIP so400m (3.5 GB) once. On request only: `setup.sh` never pre-builds this venv or model, because most users never run this skill. Tell the user about the one-time wait before the first `find`.

## Run it

```bash
bash .claude/skills/photo-finder/scripts/photo-finder.sh find
```

Prints the run folder, `photos/runs/<stamp>/`. About 3 minutes for 1,100 photos on an M-series Mac; embeddings are cached by uuid in `photos/cache/`, so reruns only embed new photos. Options:
- `--since YYYY-MM-DD` for only new photos
- `--look "..."` (repeatable) to describe a different look
- `--refs <folder>` to match a folder of reference images instead of text
- `--selfies` to include front-camera shots
- `--top N` to change how many go on sheets (default 200)

Then:
1. **Read every `sheets/sheet_NN.jpg`** (5×5, numbered by rank). Pick by eye: one per scene (a shoot leaves 5-10 near-identical variants above the dedupe threshold), favor good light, outfit, and setting, and skip group shots, mirror and gym selfies, desk shots, and text-heavy tees.
2. For a close call, render finalists bigger: `contact_sheets([by[k] for k in ranks], run/'finalists', tile=420)` from `photo_finder.py`.
3. Export the picks:
   ```bash
   bash .claude/skills/photo-finder/scripts/photo-finder.sh export photos/runs/<stamp> 4,82,18 --downloads
   ```
   This pulls originals (edited version if edited, JPEG, no Live Photo clips), adds them to the Photos album `Lifestyle picks` (`--album` overrides), copies them to `~/Downloads/<album> <date>/`, and verifies on disk that each file matches its original's size. Done = the script prints `N/N verified full-res`.

## Gotchas

- **The export needs Photos to download iCloud-only originals over AppleScript.** The first run triggers a macOS "python3.12 wants to control Photos" prompt. Tell the user to click OK before starting. A "User canceled (-128)" error means the prompt was missed.
- **On macOS 27, Photos launched by an AppleScript call hangs that call** (osxphotos logs "AppleScript timed out", a bare photoscript call hangs forever). Launched with `open -g -a Photos`, it answers right away. `export` now pre-launches Photos that way: 20 photos took 15 s instead of more than 2 min. For any other photoscript call (album edits), kill the hung process, `killall Photos`, `open -g -a Photos`, wait about 10 s, then retry.
- **Photos tags your face in saved graphics** (PFPs, YT thumbnails, AI generations, edited video stills). `find` drops any image with no camera EXIF that SigLIP reads as a graphic (the `GRAPHIC` vs `PHOTO` prompts, 0.02 margin). Camera-EXIF photos are never dropped, and real photos with stripped EXIF (IG exports, AirDrops) pass. Still eyeball the sheets for headshot PFPs before exporting.
- Photos has no AppleScript "remove from album": photoscript's `album.remove()` recreates the album. To redo a pick list, delete the album (`PhotosLibrary().delete_album`) and export again; the photos themselves are untouched.
- Some originals are small (saved PNGs and old 1080 shots), so "full-res" means matching the original's size, not a fixed pixel count.
- Read-only on the library, always. Never open Photos.sqlite for writing; albums go through osxphotos/AppleScript only.
