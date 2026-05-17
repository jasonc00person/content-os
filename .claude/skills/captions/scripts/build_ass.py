#!/usr/bin/env python3
"""
build_ass.py — render words.json (+ optional emphasis.json) to a libass .ass file.

Per-word reveal + style-dependent emphasis treatment. Used by burn.sh with
ffmpeg-full's `ass` filter.

Usage:
    build_ass.py <words.json> <out.ass> [emphasis.json] [--style <name>]
                 [--face-track <path>] [--chin-gap <px>]

Styles (--style):
    clean  — minimal: Helvetica Neue, white only, bold emphasis (DEFAULT)
    punch  — viral Submagic-style: Arial Black, yellow emphasis pop, scale animation
    mono   — technical: Menlo monospace, small, white only, bold emphasis, snappy reveal

Face-tracked positioning:
    --face-track <track.json>  Per-line MarginV computed from median chin y across
                               the line's time range; lines land a fixed gap below
                               the speaker's chin. Falls back to the style's static
                               margin_v if no track data covers a line.
    --chin-gap <px>            Gap between chin and caption top. Default 80.
"""
import argparse
import json
import re
import sys
from pathlib import Path

# --- Style presets -----------------------------------------------------------
STYLES = {
    "punch": {
        "font_name": "Arial Black",
        "size_default": 84,
        "size_emphasis": 88,
        "primary_color": "&H00FFFFFF",   # white
        "emphasis_color": "&H0000FFFF",  # yellow
        "outline_color": "&H00000000",
        "shadow_color": "&H80000000",
        "bold_default": -1,
        "bold_emphasis": -1,
        "outline_width": 5,
        "shadow": 2,
        "margin_v": 620,
        "word_fade_ms": 60,
        "pop_peak_pct": 118,
        "pop_up_ms": 100,
        "pop_down_ms": 100,
        "line_fade_in_ms": 120,
        "line_fade_out_ms": 80,
        "line_tail_s": 0.20,
        "max_words_per_line": 5,
    },
    "clean": {
        "font_name": "Helvetica Neue",
        "size_default": 68,
        "size_emphasis": 68,
        "primary_color": "&H00FFFFFF",
        "emphasis_color": "&H00FFFFFF",  # same — distinction is bold weight
        "outline_color": "&H00000000",
        "shadow_color": "&HA0000000",
        "bold_default": 0,
        "bold_emphasis": -1,
        "outline_width": 2,
        "shadow": 3,
        "margin_v": 580,
        "word_fade_ms": 80,
        "pop_peak_pct": 100,           # no scale animation
        "pop_up_ms": 100,
        "pop_down_ms": 100,
        "line_fade_in_ms": 150,
        "line_fade_out_ms": 120,
        "line_tail_s": 0.25,
        "max_words_per_line": 5,
    },
    "mono": {
        "font_name": "Menlo",
        "size_default": 54,
        "size_emphasis": 54,
        "primary_color": "&H00FFFFFF",
        "emphasis_color": "&H00FFFFFF",
        "outline_color": "&H00000000",
        "shadow_color": "&H80000000",
        "bold_default": 0,
        "bold_emphasis": -1,
        "outline_width": 3,
        "shadow": 1,
        "margin_v": 580,
        "word_fade_ms": 50,
        "pop_peak_pct": 100,
        "pop_up_ms": 100,
        "pop_down_ms": 100,
        "line_fade_in_ms": 80,
        "line_fade_out_ms": 60,
        "line_tail_s": 0.15,
        "max_words_per_line": 4,
    },
}
DEFAULT_STYLE = "clean"

MAX_GAP_BEFORE_BREAK = 0.5
PLAY_RES_X = 1080
PLAY_RES_Y = 1920
ALIGNMENT = 2
MARGIN_L = 80
MARGIN_R = 80

STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "but", "by", "can", "do", "for",
    "from", "had", "has", "have", "i", "if", "in", "is", "it", "its", "me", "my",
    "no", "not", "of", "on", "or", "so", "that", "the", "this", "to", "us", "was",
    "we", "were", "will", "with", "you", "your", "they", "them", "what", "when",
    "how", "why", "who", "all",
}
# ----------------------------------------------------------------------------


def norm(w: str) -> str:
    return re.sub(r"[^\w'-]", "", w).lower()


def format_time(t: float) -> str:
    cs = int(round(t * 100))
    h = cs // 360000
    cs -= h * 360000
    m = cs // 6000
    cs -= m * 6000
    s = cs // 100
    cs -= s * 100
    return f"{h}:{m:02d}:{s:02d}.{cs:02d}"


def ass_escape(text: str) -> str:
    """Escape transcript text so it cannot be parsed as ASS override syntax."""
    return (
        str(text)
        .replace("\\", "\\\\")
        .replace("{", r"\{")
        .replace("}", r"\}")
        .replace("\n", " ")
        .replace("\r", " ")
    )


def normalize_word(raw, idx):
    try:
        start = float(raw["start"])
        end = float(raw["end"])
    except (KeyError, TypeError, ValueError) as exc:
        raise ValueError(f"word #{idx} missing numeric start/end: {raw!r}") from exc
    if end < start:
        raise ValueError(f"word #{idx} has end before start: {raw!r}")
    text = str(raw.get("w", "")).strip()
    if not text:
        raise ValueError(f"word #{idx} has empty text: {raw!r}")
    return {**raw, "w": text, "start": start, "end": end}


def group_lines(words, max_words_per_line):
    lines, cur = [], []
    for i, w in enumerate(words):
        cur.append(w)
        text = w["w"].rstrip()
        end_of_sentence = bool(text) and text[-1] in ".?!"
        gap = words[i + 1]["start"] - w["end"] if i + 1 < len(words) else 0
        if end_of_sentence or len(cur) >= max_words_per_line or gap > MAX_GAP_BEFORE_BREAK:
            lines.append(cur)
            cur = []
    if cur:
        lines.append(cur)
    return lines


def emphasis_indices(line, emphasis_set):
    if not emphasis_set:
        cand = [
            (len(norm(w["w"])), -i, i)
            for i, w in enumerate(line)
            if norm(w["w"]) not in STOPWORDS
        ]
        if not cand:
            return set()
        cand.sort(reverse=True)
        return {cand[0][2]}
    hits = set()
    norm_line = [norm(w["w"]) for w in line]
    for emph in emphasis_set:
        e_norm = [norm(p) for p in emph.split() if norm(p)]
        if not e_norm:
            continue
        for s in range(len(norm_line) - len(e_norm) + 1):
            if norm_line[s:s + len(e_norm)] == e_norm:
                hits.update(range(s, s + len(e_norm)))
    return hits or emphasis_indices(line, [])


def build_word_text(line, emph_idx, st):
    line_start = line[0]["start"]
    parts = []
    prev_was_emphasis = False
    for i, w in enumerate(line):
        local_ms = int(round((w["start"] - line_start) * 1000))
        fade_end = local_ms + st["word_fade_ms"]
        is_emph = i in emph_idx

        overrides = []
        if is_emph:
            overrides.append("\\rEmphasis")
        elif prev_was_emphasis:
            overrides.append("\\r")
        overrides.append(f"\\alpha&HFF&\\t({local_ms},{fade_end},\\alpha&H00&)")
        # Pop animation only if peak != 100%
        if is_emph and st["pop_peak_pct"] != 100:
            pop_start = fade_end
            pop_peak = pop_start + st["pop_up_ms"]
            pop_end = pop_peak + st["pop_down_ms"]
            overrides.append(
                f"\\t({pop_start},{pop_peak},\\fscx{st['pop_peak_pct']}\\fscy{st['pop_peak_pct']})"
            )
            overrides.append(
                f"\\t({pop_peak},{pop_end},\\fscx100\\fscy100)"
            )
        parts.append("{" + "".join(overrides) + "}" + ass_escape(w["w"]))
        prev_was_emphasis = is_emph
    fade = f"{{\\fad({st['line_fade_in_ms']},{st['line_fade_out_ms']})}}"
    return fade + " ".join(parts)


def line_margin_v(line, face_track, chin_gap_px, st):
    """Per-line MarginV in ASS px, or None if track has no data covering the line."""
    if not face_track:
        return None
    samples = face_track.get("samples") or []
    if not samples:
        return None
    t0 = float(line[0]["start"])
    t1 = float(line[-1]["end"])
    relevant = [float(s["chin_y"]) for s in samples if t0 <= float(s["t"]) <= t1]
    if not relevant:
        # Fall back to nearest sample by time
        nearest = min(samples, key=lambda s: min(abs(float(s["t"]) - t0), abs(float(s["t"]) - t1)))
        relevant = [float(nearest["chin_y"])]
    relevant.sort()
    chin_y = relevant[len(relevant) // 2]  # median
    src_h = float(face_track.get("src_h") or PLAY_RES_Y)
    cap_h = st["size_default"] * 1.4  # font + outline + padding rule of thumb
    target_bottom_y = chin_y + chin_gap_px + cap_h
    margin_v = src_h - target_bottom_y
    if src_h and src_h != PLAY_RES_Y:
        margin_v = margin_v * (PLAY_RES_Y / src_h)
    return max(40, min(PLAY_RES_Y - 200, int(round(margin_v))))


def main():
    p = argparse.ArgumentParser()
    p.add_argument("words", help="path to words.json")
    p.add_argument("out", help="path to write .ass to")
    p.add_argument("emphasis", nargs="?", help="optional emphasis.json")
    p.add_argument("--style", default=DEFAULT_STYLE, choices=list(STYLES.keys()),
                   help=f"style preset (default: {DEFAULT_STYLE})")
    p.add_argument("--face-track", help="optional track_face.py JSON for chin-following position")
    p.add_argument("--chin-gap", type=int, default=80, help="px gap below chin to caption top (default 80)")
    args = p.parse_args()

    st = STYLES[args.style]

    words_path = Path(args.words)
    out_path = Path(args.out)
    emph_path = Path(args.emphasis) if args.emphasis else None

    data = json.loads(words_path.read_text())
    words = []
    word_idx = 0
    for c in data.get("clips") or []:
        for raw in c.get("words") or []:
            words.append(normalize_word(raw, word_idx))
            word_idx += 1
    if not words:
        sys.stderr.write("no words in input\n")
        sys.exit(1)

    emphasis_set = []
    if emph_path and emph_path.exists():
        emphasis_set = (json.loads(emph_path.read_text()).get("emphasis") or [])

    face_track = None
    if args.face_track and Path(args.face_track).exists():
        face_track = json.loads(Path(args.face_track).read_text())

    lines = group_lines(words, st["max_words_per_line"])

    header = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {PLAY_RES_X}
PlayResY: {PLAY_RES_Y}
ScaledBorderAndShadow: yes
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Default,{st['font_name']},{st['size_default']},{st['primary_color']},{st['primary_color']},{st['outline_color']},{st['shadow_color']},{st['bold_default']},0,0,0,100,100,0,0,1,{st['outline_width']},{st['shadow']},{ALIGNMENT},{MARGIN_L},{MARGIN_R},{st['margin_v']},1
Style: Emphasis,{st['font_name']},{st['size_emphasis']},{st['emphasis_color']},{st['emphasis_color']},{st['outline_color']},{st['shadow_color']},{st['bold_emphasis']},0,0,0,100,100,0,0,1,{st['outline_width']},{st['shadow']},{ALIGNMENT},{MARGIN_L},{MARGIN_R},{st['margin_v']},1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""

    events = []
    used_dynamic = 0
    for line in lines:
        start = format_time(line[0]["start"])
        end = format_time(line[-1]["end"] + st["line_tail_s"])
        emph_idx = emphasis_indices(line, emphasis_set)
        text = build_word_text(line, emph_idx, st)
        mv = line_margin_v(line, face_track, args.chin_gap, st)
        margin_v_field = mv if mv is not None else 0   # 0 = fall through to Style's MarginV
        if mv is not None:
            used_dynamic += 1
        events.append(f"Dialogue: 0,{start},{end},Default,,0,0,{margin_v_field},,{text}")

    out_path.write_text(header + "\n".join(events) + "\n")
    track_note = f"  face-tracked: {used_dynamic}/{len(lines)} lines" if face_track else ""
    sys.stderr.write(f"[captions] style={args.style}  wrote {len(lines)} lines → {out_path}{track_note}\n")


if __name__ == "__main__":
    main()
