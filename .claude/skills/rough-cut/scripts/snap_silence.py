#!/usr/bin/env python3
"""
snap_silence.py — word-aware cut snapping.

Reads: /tmp/video-editor/<job>/cuts.json
Uses:  /tmp/video-editor/<job>/words.json (from WhisperX)
       + FFmpeg silencedetect (on each clip)
Writes: /tmp/video-editor/<job>/cuts_snapped.json

Why word-aware:
Whisper word timestamps tell us where WORDS are. silencedetect tells us where
AUDIO SILENCE is. Intersecting them gives cuts that:
  - land in real gaps between words (not inside a word's consonant closure)
  - never overshoot into the next word or undershoot the previous one
Special case: if two Whisper words are suspiciously jammed together (< 0.1s apart)
the boundary is probably misaligned — we expand the search window to catch the
real gap detected by silencedetect.

Per-segment: set "no_snap": true on a segment in cuts.json to bypass snapping.
"""

import json, os, re, subprocess, sys

if len(sys.argv) != 2:
    sys.stderr.write("usage: snap_silence.py <job_dir>\n")
    sys.exit(1)

JOB_DIR = sys.argv[1]
JOB_NAME = os.path.basename(os.path.normpath(JOB_DIR))
WORK = f"/tmp/video-editor/{JOB_NAME}"
CUTS = os.path.join(WORK, "cuts.json")
OUT = os.path.join(WORK, "cuts_snapped.json")
WORDS = os.path.join(WORK, "words.json")

# Tuning
NOISE_THRESHOLD = "-35dB"
MIN_SILENCE_DURATION = "0.05"
LEAD_IN = 0.04                # seconds of breath/lead-in to keep before word
TAIL_OUT = 0.08               # seconds of natural decay to keep after word
TARGET_SEARCH_TOL = 0.35      # how far from user's t we'll look for a target word
SUSPICIOUS_GAP = 0.10         # Whisper word-merge heuristic threshold
EXPANDED_WINDOW = 1.00        # how far to search when Whisper boundary is suspicious

# ---------- Load cuts + words ----------

if not os.path.isdir(JOB_DIR):
    sys.stderr.write(f"job dir not found: {JOB_DIR}\n")
    sys.exit(1)
if not os.path.exists(CUTS):
    sys.stderr.write(f"missing cuts file: {CUTS}\n")
    sys.exit(1)

with open(CUTS) as f:
    cuts = json.load(f)
if not isinstance(cuts.get("segments"), list):
    sys.stderr.write(f"{CUTS} must contain a segments array\n")
    sys.exit(1)
for i, seg in enumerate(cuts["segments"]):
    missing = [key for key in ("clip", "start", "end") if key not in seg]
    if missing:
        sys.stderr.write(f"segment #{i} missing required keys: {', '.join(missing)}\n")
        sys.exit(1)
    try:
        seg["start"] = float(seg["start"])
        seg["end"] = float(seg["end"])
    except (TypeError, ValueError):
        sys.stderr.write(f"segment #{i} has non-numeric start/end: {seg!r}\n")
        sys.exit(1)
    if seg["end"] <= seg["start"]:
        sys.stderr.write(f"segment #{i} has end <= start: {seg!r}\n")
        sys.exit(1)

words_by_clip = {}
if os.path.exists(WORDS):
    with open(WORDS) as f:
        wdata = json.load(f)
    for c in wdata.get("clips", []):
        words_by_clip[c["clip"]] = c["words"]
    total = sum(len(v) for v in words_by_clip.values())
    print(f"[snap] loaded {total} word-level timestamps", file=sys.stderr)
else:
    print(f"[snap] no words.json at {WORDS} — word-aware snap DISABLED", file=sys.stderr)


# ---------- Silence detection ----------

def detect_silences(clip_path):
    result = subprocess.run(
        [
            "ffmpeg", "-nostdin", "-hide_banner",
            "-i", clip_path,
            "-af", f"silencedetect=noise={NOISE_THRESHOLD}:d={MIN_SILENCE_DURATION}",
            "-f", "null", "-",
        ],
        capture_output=True, text=True, check=True,
    )
    silences = []
    cur_start = None
    for line in result.stderr.splitlines():
        m = re.search(r"silence_start:\s*([\d.]+)", line)
        if m:
            cur_start = float(m.group(1))
            continue
        m = re.search(r"silence_end:\s*([\d.]+)", line)
        if m and cur_start is not None:
            silences.append((cur_start, float(m.group(1))))
            cur_start = None
    return silences


# ---------- Word-aware snap ----------

def target_word_in(t, words):
    """Find the word the user likely wants to START on."""
    near = [(i, w) for i, w in enumerate(words)
            if w["start"] >= t - TARGET_SEARCH_TOL]
    if near:
        return min(near, key=lambda p: abs(p[1]["start"] - t))
    # No word at/after t → fall back to last word before t
    before = [(i, w) for i, w in enumerate(words) if w["end"] <= t]
    return before[-1] if before else None


def target_word_out(t, words):
    """Find the word the user likely wants to END on."""
    near = [(i, w) for i, w in enumerate(words)
            if w["end"] <= t + TARGET_SEARCH_TOL]
    if near:
        return max(near, key=lambda p: p[1]["end"])
    after = [(i, w) for i, w in enumerate(words) if w["start"] >= t]
    return after[0] if after else None


def snap_in_word_aware(t, silences, words):
    found = target_word_in(t, words)
    if not found:
        return t, "no-target"
    idx, target = found
    prev_end = words[idx - 1]["end"] if idx > 0 else 0.0
    gap = target["start"] - prev_end
    # Window bounds
    lo = max(0.0, prev_end - 0.03)
    if gap < SUSPICIOUS_GAP:
        # Whisper probably merged two words — search forward aggressively
        hi = target["start"] + EXPANDED_WINDOW
    else:
        hi = target["start"] + 0.05
    # Candidates: silence_end boundaries in [lo, hi]
    candidates = [s_end for _, s_end in silences if lo <= s_end <= hi]
    if candidates:
        # Prefer closest to target.start (on either side)
        best = min(candidates, key=lambda x: abs(x - target["start"]))
        return best, f"word[{target['w']}]{'+exp' if gap < SUSPICIOUS_GAP else ''}"
    # Fallback: word.start minus a small lead-in
    return max(target["start"] - LEAD_IN, prev_end), f"word-start[{target['w']}]"


def snap_out_word_aware(t, silences, words):
    found = target_word_out(t, words)
    if not found:
        return t, "no-target"
    idx, target = found
    next_start = (words[idx + 1]["start"] if idx + 1 < len(words)
                  else float("inf"))
    gap = next_start - target["end"]
    hi = next_start + 0.03 if next_start != float("inf") else target["end"] + EXPANDED_WINDOW
    if gap < SUSPICIOUS_GAP:
        lo = target["end"] - EXPANDED_WINDOW
    else:
        lo = target["end"] - 0.05
    candidates = [s_start for s_start, _ in silences if lo <= s_start <= hi]
    if candidates:
        best = min(candidates, key=lambda x: abs(x - target["end"]))
        return best, f"word[{target['w']}]{'+exp' if gap < SUSPICIOUS_GAP else ''}"
    # Fallback: word.end plus a small tail
    tail = min(target["end"] + TAIL_OUT, next_start)
    return tail, f"word-end[{target['w']}]"


# ---------- Silencedetect-only fallback (no words.json) ----------

FORWARD_TOL = 1.00
BACKWARD_TOL = 0.15


def snap_in_silence_only(t, silences):
    for s_start, s_end in silences:
        if s_start <= t <= s_end:
            return s_end, "inside-silence"
    best = None
    for _, s_end in silences:
        diff = s_end - t
        if 0 <= diff <= FORWARD_TOL or -BACKWARD_TOL <= diff < 0:
            if best is None or abs(diff) < abs(best[1]):
                best = (s_end, diff)
    return (best[0], f"snap{best[1]:+.3f}s") if best else (t, "no-snap")


def snap_out_silence_only(t, silences):
    for s_start, s_end in silences:
        if s_start <= t <= s_end:
            return s_start, "inside-silence"
    best = None
    for s_start, _ in silences:
        diff = s_start - t
        if -FORWARD_TOL <= diff <= 0 or 0 < diff <= BACKWARD_TOL:
            if best is None or abs(diff) < abs(best[1]):
                best = (s_start, diff)
    return (best[0], f"snap{best[1]:+.3f}s") if best else (t, "no-snap")


# ---------- Run snap for each segment ----------

silences_by_clip = {}
for clip_name in sorted({seg["clip"] for seg in cuts["segments"]}):
    clip_path = os.path.join(JOB_DIR, clip_name)
    if not os.path.exists(clip_path):
        sys.stderr.write(f"clip not found for cuts.json segment: {clip_path}\n")
        sys.exit(1)
    print(f"[snap] scanning {clip_name}", file=sys.stderr)
    silences_by_clip[clip_name] = detect_silences(clip_path)
    print(f"[snap]   {len(silences_by_clip[clip_name])} silence ranges",
          file=sys.stderr)

snapped = {"segments": []}
for seg in cuts["segments"]:
    sil = silences_by_clip[seg["clip"]]
    words = words_by_clip.get(seg["clip"], [])
    if seg.get("no_snap"):
        new_in, in_note = seg["start"], "no_snap"
        new_out, out_note = seg["end"], "no_snap"
    elif words:
        new_in, in_note = snap_in_word_aware(seg["start"], sil, words)
        new_out, out_note = snap_out_word_aware(seg["end"], sil, words)
    else:
        new_in, in_note = snap_in_silence_only(seg["start"], sil)
        new_out, out_note = snap_out_silence_only(seg["end"], sil)
    new_seg = dict(seg)
    new_seg["start"] = round(new_in, 3)
    new_seg["end"] = round(new_out, 3)
    if new_seg["end"] <= new_seg["start"]:
        sys.stderr.write(
            f"[snap] invalid snapped segment for {seg['clip']}: "
            f"{new_seg['start']}→{new_seg['end']} "
            f"(original {seg['start']}→{seg['end']})\n"
        )
        sys.exit(1)
    new_seg["_snap"] = {
        "in": in_note, "out": out_note,
        "orig_start": seg["start"], "orig_end": seg["end"],
    }
    snapped["segments"].append(new_seg)
    di, do = new_in - seg["start"], new_out - seg["end"]
    print(f"[snap] {seg['clip']} {seg['start']:7.2f}→{seg['end']:7.2f}  "
          f"Δin={di:+.3f}  Δout={do:+.3f}  in={in_note}  out={out_note}",
          file=sys.stderr)

with open(OUT, "w") as f:
    json.dump(snapped, f, indent=2)
print(f"[snap] wrote {OUT}", file=sys.stderr)
