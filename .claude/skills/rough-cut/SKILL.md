---
name: rough-cut
description: "Rough-cuts short-form reels from raw clips. Transcribes with WhisperX (large-v3 + wav2vec2 word-level alignment), kills filler + dead air, keeps only the essential lines, stitches with FFmpeg. No captions, no B-roll — just a tight rough cut ready for final polish. Triggers: edit this reel, rough cut, cut this video, edit the latest project, trim this, chop this up, rough-cut, make a rough cut."
---

# Rough Cut — Transcript-Driven Edits

Turns raw talking-head clips into a tight rough cut. You transcribe, you decide the cuts, FFmpeg stitches. The goal: **shortest possible reel that still delivers the value.** Respect the viewer's time.

## How to Trigger
- **"edit the latest project"** → finds the newest job folder, edits it
- **"rough cut [job name]"** → edits a specific job folder
- **"cut this reel"** with a path → edits that folder

---

## Folder Contract

The skill operates out of `/video-editor/` at the repo root.

```
video-editor/
├── projects/
│   └── <job-name>/              ← one folder per reel
│       ├── raw/                 ← raw clips (any name, any count)
│       │   ├── clip-01.mov
│       │   └── clip-02.mov
│       ├── audio/               ← OPTIONAL — music beds / audio assets
│       ├── assets/              ← OPTIONAL — refs, screen recordings, B-roll sources
│       ├── thumbnails/          ← OPTIONAL — thumbnail source images/working files
│       ├── outputs/             ← rendered deliverables for this job
│       │   └── <job-name>.mp4
│       └── intent.md            ← OPTIONAL — what the reel is about
```

Intermediates (transcript, cuts.json, segments, etc.) live in `/tmp/video-editor/<job-name>/` so the job folder stays clean. Read from there when iterating.

If no `intent.md` exists, ask in one line: *"Give me the hook + takeaway in a sentence so I know what to keep."*

---

## The Edit Philosophy (non-negotiable)

**Short and snappy, max value per second, respect the viewer.**

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

**Preserve the creator's cadence though.** Don't surgical-kill every "like" — some are rhythm, some are filler. Taste call.

---

## The Pipeline

### Step 1 — Transcribe

Find the job folder. Run:

```bash
bash .claude/skills/rough-cut/scripts/transcribe.sh <job_dir>
```

This runs WhisperX (large-v3 ASR + wav2vec2 forced alignment) with true word-level timestamps and writes `/tmp/video-editor/<job-name>/words.json`. Word timestamps are tighter than plain faster-whisper, so cuts land more precisely.

**Add `--diarize`** to label each word with a speaker (multi-person clips). Requires `HUGGINGFACE_TOKEN` in env and accepting the pyannote/speaker-diarization-3.1 model on HF.

**Run in background** if expected >2min:
- ~30s of clip = ~10-20s wall time (first run is slower — alignment model downloads)
- ~5min of clip = ~2min wall time

For total clip length >3min, use `run_in_background: true` and Monitor.

### Step 2 — Read the transcript + decide cuts

Read `/tmp/video-editor/<job-name>/words.json`. Each clip has a `words` array of `{w, start, end, prob}` (plus `speaker` when `--diarize` was used).

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
- Trust WhisperX word-level timestamps as the source of truth.
- Start on the first word you want, usually `word.start - 0.03` to `0.08`.
- End after the last word you want, usually `word.end + 0.04` to `0.10`.
- Don't cut mid-word. If a transition feels clipped, adjust `cuts.json` manually and rerender.
- Segments CAN cross clips in any order — that's the whole point.

Include the `transcript` field for each segment so the creator can read the cut sheet and sanity-check it without watching.

### Step 3 — Splice

```bash
bash .claude/skills/rough-cut/scripts/splice.sh <job_dir>
```

Writes `video-editor/projects/<job-name>/outputs/<job-name>.mp4` directly from `/tmp/video-editor/<job-name>/cuts.json`. Uses accurate FFmpeg seeking (`-i clip -ss start -t duration`) so WhisperX timestamps stay authoritative, then re-encodes each segment with h264_videotoolbox and normalizes audio.

**Always run in background** — renders take 15-45s for 60s output.

### Step 4 — Report back

Show the creator:
- Final duration vs raw total (e.g., "3:47 → 0:48, 79% cut")
- The cut sheet (clip + timestamp + line) to review
- Path to the MP4

---

## Output Format

After the cut lands, report like this:

```
✂️ ROUGH CUT DONE

📊 3:47 → 0:48 (79% cut)
📁 video-editor/projects/<job-name>/outputs/<job-name>.mp4

CUT SHEET:
1. [clip-02 @ 1.24-4.60] "Are you still paying a VA three grand a month"
2. [clip-02 @ 4.95-8.10] "to do shit Claude Code can do for free"
...
```

Keep it tight. If a segment feels weak, flag it: **"⚠️ segment 3 is borderline — consider killing."**

---

## Gotchas

- **`-c copy` alone doesn't work on arbitrary cut points** — causes A/V desync. `splice.sh` re-encodes each segment with hardware accel, which is still fast (~15s for a 60s reel). Don't "optimize" to pure stream copy.
- **Don't auto-snap cuts to silence.** WhisperX word alignment is the unlock. Automatic silencedetect snapping can move intentionally chosen boundaries into filler words or awkward pauses.
- **Whisper can mishear.** Always cross-check the transcript before killing a line — sometimes "Claude" becomes "cloud" or "Cloud" and the line looks wrong when it's fine.
- **Don't re-run transcribe.sh** if `/tmp/video-editor/<job-name>/words.json` already exists. Check first. Transcribing is the slowest step.
- **Clip order in `cuts.json` = final order in the reel.** You're writing the script sequence.
- **If intent.md is missing and no direction was given**, ask one question in one sentence. Don't guess.

---

## Handoff

Once the rough cut is approved, continue the repo pipeline: `audio-polish` → `reframe` → `broll` → `captions` → `post-content`.

This skill does ONE thing: cut the reel down to the essential lines. It does not do audio polish, captions, B-roll, zoom effects, or vertical reframing.
