---
name: video-editor
description: "Rough-cuts short-form reels from raw clips. Transcribes with faster-whisper, kills filler + dead air, keeps only the essential lines, stitches with FFmpeg. No captions, no B-roll — just a tight rough cut ready for final polish. Triggers: edit this reel, rough cut, cut this video, edit the inbox, trim this, chop this up, video-editor, make a rough cut."
---

# Video Editor — Transcript-Driven Rough Cuts

Turns raw talking-head clips into a tight rough cut. You transcribe, you decide the cuts, FFmpeg stitches. The goal: **shortest possible reel that still delivers the value.** Respect the viewer's time.

## How to Trigger
- **"edit the inbox"** → finds the newest job folder, edits it
- **"rough cut [job name]"** → edits a specific job folder
- **"cut this reel"** with a path → edits that folder

---

## Folder Contract

Jason works out of `/video-editor/` at the repo root.

```
video-editor/
├── inbox/
│   └── <job-name>/              ← one folder per reel
│       ├── clip-01.mov          ← raw clips (any name, any count)
│       ├── clip-02.mov
│       └── intent.md            ← OPTIONAL — what the reel is about
└── outputs/
    └── <job-name>.mp4           ← final deliverable (named after job folder)
```

Intermediates (transcript, cuts.json, segments, etc.) live in `/tmp/video-editor/<job-name>/` so the job folder stays clean. Read from there when iterating.

If no `intent.md` exists, ask Jason in one line: *"Give me the hook + takeaway in a sentence so I know what to keep."*

---

## The Edit Philosophy (non-negotiable)

Jason's rule: **short and snappy, max value per second, respect the viewer.**

Every cut decision runs through this filter:
1. **Does this line deliver value?** If not, kill it.
2. **Is this the tightest version?** If there's a shorter take, use it.
3. **Would a viewer skip past this?** If yes, it's dead.

Target length: **30-60 seconds** unless intent says otherwise. If the raw clips add up to 4 minutes, your job is to cut 75%+ out.

---

## Auto-Kill Rules (always apply)

When building `cuts.json`, automatically remove:

| Kill | Why |
|------|-----|
| Filler words: *um, uh, like, you know, so yeah, basically* (when vestigial) | Dead weight |
| Stutters + false starts: *"I- I was gonna-"* | Breaks flow |
| Restarted takes | Keep the best take, kill the rest |
| Silences > 0.4s | Dead air |
| Tangents + asides that don't serve the hook/takeaway | Respect viewer time |
| Throat-clears, "okay let me start over", etc. | Production noise |
| Preamble before the hook lands | Every reel opens ON the hook |

**Preserve Jason's cadence though.** Don't surgical-kill every "like" — some are rhythm, some are filler. Taste call.

---

## The Pipeline

### Step 1 — Transcribe

Find the job folder. Run:

```bash
bash .claude/skills/video-editor/scripts/transcribe.sh <job_dir>
```

This runs faster-whisper large-v3 with word-level timestamps and writes `/tmp/video-editor/<job-name>/words.json`.

**Run in background** if expected >2min:
- ~30s of clip = ~8-15s wall time
- ~5min of clip = ~90s wall time

For total clip length >3min, use `run_in_background: true` and Monitor.

### Step 2 — Read the transcript + decide cuts

Read `/tmp/video-editor/<job-name>/words.json`. Each clip has a `words` array of `{w, start, end, prob}`.

Apply the auto-kill rules and the edit philosophy. Output `/tmp/video-editor/<job-name>/cuts.json` in this shape:

```json
{
  "segments": [
    { "clip": "clip-02.mov", "start": 1.24, "end": 4.60, "transcript": "Are you still paying a VA three grand a month" },
    { "clip": "clip-02.mov", "start": 4.95, "end": 8.10, "transcript": "to do shit Claude Code can do for free in five minutes" },
    { "clip": "clip-01.mov", "start": 12.20, "end": 18.80, "transcript": "..." }
  ]
}
```

**Timestamp rules:**
- Add ~0.1-0.2s headroom on each cut so you don't clip the start/end of a word
- Don't cut mid-word. Find the gap between words.
- Segments CAN cross clips in any order — that's the whole point

Include the `transcript` field for each segment so Jason can read the cut sheet and sanity-check it without watching.

### Step 3 — Splice

```bash
bash .claude/skills/video-editor/scripts/splice.sh <job_dir>
```

Writes `video-editor/outputs/<job-name>.mp4`. Runs silence-snap on `cuts.json` first (FFmpeg silencedetect → `cuts_snapped.json`) so every cut lands in silence, not mid-word. Uses h264_videotoolbox (hardware accel on M-series) for the encode, loudnorm for audio levels.

**Always run in background** — renders take 15-45s for 60s output.

### Step 4 — Report back

Show Jason:
- Final duration vs raw total (e.g., "3:47 → 0:48, 79% cut")
- The cut sheet (clip + timestamp + line) so he can review
- Path to the MP4

---

## Output Format

After the cut lands, report like this:

```
✂️ ROUGH CUT DONE

📊 3:47 → 0:48 (79% cut)
📁 video-editor/outputs/<job-name>.mp4

CUT SHEET:
1. [clip-02 @ 1.24-4.60] "Are you still paying a VA three grand a month"
2. [clip-02 @ 4.95-8.10] "to do shit Claude Code can do for free"
...
```

Keep it tight. If a segment feels weak, flag it: **"⚠️ segment 3 is borderline — consider killing."**

---

## Gotchas

- **`-c copy` alone doesn't work on arbitrary cut points** — causes A/V desync. `splice.sh` re-encodes each segment with hardware accel, which is still fast (~15s for a 60s reel). Don't "optimize" to pure stream copy.
- **Whisper can mishear.** Always cross-check the transcript before killing a line — sometimes "Claude" becomes "cloud" or "Cloud" and the line looks wrong when it's fine.
- **Don't re-run transcribe.sh** if `/tmp/video-editor/<job-name>/words.json` already exists. Check first. Transcribing is the slowest step.
- **Clip order in `cuts.json` = final order in the reel.** You're writing the script sequence.
- **If intent.md is missing and Jason didn't specify**, ask one question in one sentence. Don't guess.

---

## Handoff

Once the rough cut is approved, Jason takes it into Submagic / CapCut for captions + polish, OR triggers the `post-content` skill to schedule it.

This skill does ONE thing: cut the reel down to the essential lines. It does not do captions, B-roll, zoom effects, or vertical reframing. That's Phase 2+.
