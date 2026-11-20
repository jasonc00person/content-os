#!/usr/bin/env python3
"""Build title-corpus/titles.json: every long-form title on the creator's channel + every
tracked YouTube competitor, with views, approximate date, and a per-channel BREAKOUT score
(views / that channel's median), so titles rank by how hard they beat their own baseline,
not by channel size.

    python3 title-corpus/build.py                       # own handle + all ## YouTube handles in competitor-list.md
    python3 title-corpus/build.py --own yourhandle --extra @somebody   # --own defaults to the YouTube handle in CLAUDE.md
    python3 title-corpus/build.py --min-age 14 --window 540 --cap 400

One yt-dlp flat-playlist call per channel (~2s each, no downloads, no cookies, no key).
Re-run whenever a batch of winners lands (quarterly at minimum: recent uploads can't be
scored until their views settle, so a stale corpus is always missing the newest wave).
"""
import argparse, json, os, re, statistics, subprocess, sys, time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "title-corpus", "titles.json")
COMP = os.path.join(ROOT, "competitor-list.md")
CLAUDE_MD = os.path.join(ROOT, "CLAUDE.md")


def own_handle_from_claude_md():
    if not os.path.exists(CLAUDE_MD):
        return None
    m = re.search(r"youtube\.com/@([A-Za-z0-9._-]+)", open(CLAUDE_MD, encoding="utf-8").read())
    return m.group(1) if m else None


def yt_handles_from_competitor_list():
    if not os.path.exists(COMP):
        return []
    txt = open(COMP, encoding="utf-8").read()
    m = re.search(r"^## YouTube\s*$(.*?)(?=^## |\Z)", txt, re.M | re.S)
    if not m:
        return []
    out = []
    for block in re.split(r"^### ", m.group(1), flags=re.M)[1:]:
        if block.lstrip().upper().startswith("EXAMPLE"):
            continue
        h = re.search(r"youtube\.com/@([A-Za-z0-9._-]+)", block)
        if h and h.group(1) not in out:
            out.append(h.group(1))
    return out


def pull(handle, cap):
    url = f"https://www.youtube.com/@{handle}/videos"
    r = subprocess.run(["yt-dlp", "--flat-playlist", "-J", "--playlist-end", str(cap),
                        "--extractor-args", "youtubetab:approximate_date", url],
                       capture_output=True, text=True)
    if r.returncode != 0 or not r.stdout.strip():
        print(f"  !! {handle}: {r.stderr.strip().splitlines()[-1] if r.stderr.strip() else 'no output'}",
              file=sys.stderr)
        return None, []
    d = json.loads(r.stdout)
    return d.get("channel") or d.get("uploader") or handle, d.get("entries") or []


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--own", default=None, help="the creator's own handle (default: the YouTube handle in CLAUDE.md)")
    ap.add_argument("--extra", nargs="*", default=[], help="additional @handles")
    ap.add_argument("--min-age", type=int, default=14,
                    help="days before a video is old enough to score (views still climbing)")
    ap.add_argument("--window", type=int, default=540,
                    help="days of history used for each channel's median (older titles still kept, "
                         "just scored against this baseline)")
    ap.add_argument("--cap", type=int, default=400,
                    help="newest N uploads per channel (the /videos tab is newest-first; a daily poster's "
                         "2019 back-catalog is noise, not signal)")
    ap.add_argument("--out", default=OUT)
    a = ap.parse_args()
    a.own = a.own or own_handle_from_claude_md()
    if not a.own or a.own.startswith("<<"):
        sys.exit("pass --own <your YouTube handle> (or fill the YouTube link in CLAUDE.md)")

    handles = [a.own.lstrip("@")] + [h for h in yt_handles_from_competitor_list() if h != a.own.lstrip("@")]
    handles += [h.lstrip("@") for h in a.extra if h.lstrip("@") not in handles]
    now = int(time.time())

    videos, channels = [], {}
    for h in handles:
        name, entries = pull(h, a.cap)
        rows = []
        for e in entries:
            v = e.get("view_count")
            if v is None or e.get("live_status") in ("is_live", "is_upcoming"):
                continue
            ts = e.get("timestamp")
            age = (now - ts) // 86400 if ts else None
            rows.append({"handle": h, "channel": name, "id": e.get("id"), "title": e.get("title"),
                         "views": int(v), "duration": e.get("duration"), "ts": ts, "age_days": age,
                         "is_own": h.lower() == a.own.lstrip("@").lower()})
        scoreable = [r["views"] for r in rows
                     if r["age_days"] is not None and a.min_age <= r["age_days"] <= a.window]
        if len(scoreable) < 8:                       # thin channel: fall back to everything old enough
            scoreable = [r["views"] for r in rows if (r["age_days"] or 0) >= a.min_age] or [r["views"] for r in rows]
        med = statistics.median(scoreable) if scoreable else 0
        for r in rows:
            fresh = r["age_days"] is not None and r["age_days"] < a.min_age
            r["too_fresh"] = fresh
            r["breakout"] = round(r["views"] / med, 2) if med and not fresh else None
        channels[h] = {"channel": name, "videos": len(rows), "median_views": med,
                       "baseline_n": len(scoreable), "is_own": h.lower() == a.own.lstrip("@").lower()}
        videos += rows
        print(f"  {name:<28} {len(rows):>4} videos · median {int(med):>7,} views", file=sys.stderr)

    videos.sort(key=lambda r: -(r["breakout"] or 0))
    out = {"built": time.strftime("%Y-%m-%d"), "own": a.own.lstrip("@"), "min_age_days": a.min_age,
           "window_days": a.window, "channels": channels, "videos": videos}
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    with open(a.out, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1, ensure_ascii=False)
    print(f"\n{len(videos)} titles across {len(channels)} channels → {a.out}", file=sys.stderr)


if __name__ == "__main__":
    main()
