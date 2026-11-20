#!/usr/bin/env python3
"""Scrape YouTube comments with yt-dlp, keep the demand signals, kill the noise.

Writes <run_dir>/signals.json:
  {"stats": [...per video...], "signals": [...ranked...], "dropped": {...counts...},
   "campaigns": {subject: [authors]}}  # suspected shill campaigns, flagged in place

Ranking never happens in Claude's head — this script owns it.
"""
import argparse, json, os, re, subprocess, sys
from collections import defaultdict

# ---- tiers: what kind of demand is this? order matters, first match wins the tier ----
TIERS = [
    ("blocker", 10, [
        r"\b(doesn'?t|does not|didn'?t|won'?t|isn'?t) work\b", r"\bnot working\b",
        r"\b(i'?m |im )?(stuck|stumped)\b", r"\b(getting|got|throws?|keep getting) (an? )?error\b",
        r"\bcan'?t (get|find|install|run|figure|load|connect)\b", r"\bfailed to\b",
        r"\b(tried|followed) (it|this|the|your)\b.{0,40}\b(but|however|and it)\b",
        r"\bi (can'?t|couldn'?t) (get|make) (it|this)\b", r"\bkeeps? (crashing|failing|erroring)\b",
    ]),
    ("buyer", 9, [
        r"\bmy (company|agency|team|studio|business|clients?|production)\b",
        r"\bwe (currently|use|run|have|manage)\b", r"\bmy (workflow|pain point|process|pipeline)\b",
        r"\bi (run|own) an?\b", r"\bpain point\b", r"\bat work\b",
    ]),
    ("request", 7, [
        r"\b(can|could|would) you (please |plz |pls )?(make|do|show|cover|explain|create|upload|post)\b",
        r"\b(please|pls|plz) (make|do|show|cover|explain|create|upload|post)\b",
        r"\b(make|do|upload|post) a (video|tutorial|walkthrough)\b",
        r"\b(video|tutorial|walkthrough|deep ?dive) (on|about|for)\b",
        r"\bcan we get\b", r"\bpart ?2\b", r"\bfollow ?up video\b",
        r"\bwould love (to see|a)\b", r"\bi'?d love (to see|a)\b",
    ]),
    ("objection", 6, [
        r"\bai (will never|can'?t|doesn'?t)\b", r"\b(generic|boring|soulless|slop|bland|mind.?numbing)\b",
        r"\bscreams? ai\b", r"\bai.?(created|generated|looking)\b",
        r"\b(disagree|hard pass|not buying|overhyped|hype)\b",
        r"\bwhat problem does (it|this) solve\b", r"\btoo expensive\b", r"\bnot paying\b",
    ]),
    ("constraint", 6, [
        r"\bwindows\b", r"\bwsl\b", r"\blinux\b", r"\bubuntu\b", r"\bpowershell\b",
        r"\bfree (version|alternative|option|plan|tier)\b", r"\bwithout (paying|a subscription)\b",
        r"\b(cheaper|budget|low.?cost) (option|alternative|way)\b",
        r"\bdon'?t have\b", r"\bany (other )?(alternative|replacement)\b",
        r"\bwork(s)? (on|with|in) (windows|linux|pc|mac)\b",
    ]),
    ("howto", 5, [
        r"\bhow (do|did|does|can|would) (you|i|we)\b", r"\bhow to\b", r"\bhow the hell\b",
        r"\bwhat'?s the (best|right) way\b", r"\bwhere do i\b",
    ]),
    ("question", 3, [
        r"\bis there a way\b", r"\bany chance\b", r"\bwhat about\b", r"\bwhat if\b",
        r"\bdoes (this|it) (work|support)\b", r"\bwhich\b.*\?", r"\?",
    ]),
]
TIERS_C = [(n, w, [re.compile(p, re.I) for p in pats]) for n, w, pats in TIERS]

# praise that happens to contain "how to use X" — drop unless it also asks something
PRAISE = re.compile(
    r"^(?=.{0,400}$)(?=.*\b(great|amazing|awesome|thank|thanks|appreciate|love|best|"
    r"valuable|helpful|excellent|goat|legend|banger|fire)\b)", re.I)
ASKS = re.compile(r"\?|\b(can|could|would|please|pls|plz|how do|how can|how to|what about|any chance)\b", re.I)

NOISE = re.compile(
    r"^(nice|great|good|dope|sick|clean|insane|crazy|wild|w|fire|goat|banger|first|"
    r"thanks?|thank you|ty|tysm|awesome|amazing|love (it|this)|subscribed|new sub|"
    r"underrated|commenting for the algorithm)\W*$", re.I)
SPAM = re.compile(
    r"(t\.me/|wa\.me/|whatsapp|telegram|@gmail\.com|dm me|check out my (channel|page)|"
    r"promo ?code|crypto|forex|投资|무료)", re.I)


def norm(t):
    return re.sub(r"[^a-z0-9 ]", "", t.lower())


STOP = set("""this that with have your the and for you can could would will make video videos
tutorial about more some other another your their next best good great full thing things please how what when where why using with same
these those something anything everything""".split())

# "could you do a video about X" — X is the requested subject
SUBJECT = [
    re.compile(r"\b(?:video|vid|videos|tutorial|walkthrough)s?\s+(?:about|on|covering|regarding)\s+([a-z0-9][a-z0-9 .+-]{1,40})", re.I),
    re.compile(r"\b(?:do|make|cover|create)\s+(?:a\s+|an\s+)?(?:video\s+|tutorial\s+)?(?:about|on)\s+([a-z0-9][a-z0-9 .+-]{1,40})", re.I),
]


def subject_key(text):
    """The thing being requested, normalized to its first real word."""
    for pat in SUBJECT:
        m = pat.search(text)
        if not m:
            continue
        words = [w for w in norm(m.group(1)).split() if w not in STOP and len(w) > 2]
        if words:
            return words[0]
    return None


def find_campaigns(items):
    """A shill campaign is the SAME subject requested by many different authors on
    more than one channel. Organic demand is phrased differently every time and
    clusters on one channel. Suspected campaigns are FLAGGED, never dropped — a
    false positive would cost a real topic, which is worse than one junk idea."""
    from collections import defaultdict
    by_subj = defaultdict(list)
    for it in items:
        k = subject_key(it["text"])
        if k:
            by_subj[k].append(it)
    out = {}
    for k, v in by_subj.items():
        channels = len({i["channel"] for i in v})
        authors = len({i["author"] for i in v})
        # cross-channel is required; then EITHER many authors OR sheer repetition.
        # sockpuppets recycle 2 near-identical account names, so author count alone misses them.
        if channels >= 2 and (authors >= 3 or len(v) >= 4):
            out[k] = v
    return out


def video_urls(target, limit):
    if "watch?v=" in target or "youtu.be/" in target:
        return [target]
    url = target if target.startswith("http") else f"https://www.youtube.com/@{target.lstrip('@')}/videos"
    r = subprocess.run(["yt-dlp", "--flat-playlist", "--playlist-end", str(limit), "-J", url],
                       capture_output=True, text=True)
    if r.returncode != 0 or not r.stdout.strip():
        print(f"  !! could not list videos for {target}: {r.stderr.strip()[:200]}", file=sys.stderr)
        return []
    return [f"https://www.youtube.com/watch?v={e['id']}"
            for e in json.loads(r.stdout).get("entries", []) if e.get("id")]


def scrape(url, max_comments, meta_dir):
    subprocess.run(
        ["yt-dlp", "--skip-download", "--write-comments", "--write-info-json",
         "--extractor-args", f"youtube:comment_sort=top;max_comments={max_comments},all,50,5",
         "-o", "%(id)s", "-P", meta_dir, url],
        capture_output=True, text=True)
    vid = url.split("v=")[-1].split("&")[0].split("/")[-1]
    path = os.path.join(meta_dir, f"{vid}.info.json")
    if not os.path.exists(path):
        return None
    with open(path) as f:
        return json.load(f)


def classify(text):
    tiers, score = [], 0
    for name, weight, pats in TIERS_C:
        if any(p.search(text) for p in pats):
            tiers.append(name)
            score += weight
    return tiers, score


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("run_dir")
    ap.add_argument("targets", nargs="+", help="@handle, channel URL, or video URL")
    ap.add_argument("--own", default="", help="handle that is the user's OWN channel")
    ap.add_argument("--videos", type=int, default=5, help="videos per channel")
    ap.add_argument("--max-comments", type=int, default=400)
    ap.add_argument("--min-score", type=int, default=5)
    a = ap.parse_args()

    meta_dir = os.path.join(a.run_dir, "meta")
    os.makedirs(meta_dir, exist_ok=True)
    own = a.own.lstrip("@").lower()

    raw, stats = [], []
    dropped = defaultdict(int)

    for t in a.targets:
        for url in video_urls(t, a.videos):
            info = scrape(url, a.max_comments, meta_dir)
            if not info:
                print(f"  !! no data for {url}", file=sys.stderr)
                continue
            comments = info.get("comments") or []
            is_own = own and (own in (info.get("uploader_id") or "").lower()
                              or own in (info.get("channel") or "").lower().replace(" ", "")
                              or own in (info.get("uploader") or "").lower().replace(" ", ""))
            kept = 0
            for c in comments:
                txt = (c.get("text") or "").strip()
                if c.get("author_is_uploader"):
                    dropped["uploader"] += 1; continue
                if len(txt) < 15 or NOISE.match(txt):
                    dropped["noise"] += 1; continue
                if SPAM.search(txt):
                    dropped["spam"] += 1; continue
                tiers, score = classify(txt)
                if PRAISE.match(txt) and not ASKS.search(txt):
                    dropped["praise"] += 1; continue
                if score < a.min_score:
                    dropped["low_score"] += 1; continue
                score += min(c.get("like_count") or 0, 15)
                if len(txt) > 220:
                    score += 3          # long comments cost effort; effort is intent
                raw.append({
                    "id": c.get("id"),
                    "channel": info.get("uploader"),
                    "is_own_channel": bool(is_own),
                    "video_title": info.get("title"),
                    "video_id": info.get("id"),
                    "video_url": f"https://youtu.be/{info.get('id')}",
                    "video_views": info.get("view_count"),
                    "author": c.get("author"),
                    "likes": c.get("like_count") or 0,
                    "posted": c.get("_time_text"),
                    "is_reply": bool(c.get("parent") and c.get("parent") != "root"),
                    "tiers": tiers,
                    "score": score,
                    "search_string": " ".join(txt.split()[:6]),
                    "text": txt,
                })
                kept += 1
            stats.append({"channel": info.get("uploader"), "is_own_channel": bool(is_own),
                          "title": info.get("title"), "url": f"https://youtu.be/{info.get('id')}",
                          "views": info.get("view_count"), "comments": len(comments), "signals": kept})
            print(f"  {info.get('uploader')} · {len(comments)} comments → {kept} signals · "
                  f"{(info.get('title') or '')[:60]}", file=sys.stderr)

    # ---- suspected astroturf: flagged in place, never dropped ----
    campaigns = find_campaigns(raw)
    flagged = {i["id"] for v in campaigns.values() for i in v}
    signals = []
    for s in raw:
        s.pop("fp", None)
        if s["id"] in flagged:
            s["suspected_campaign"] = True
            dropped["suspected_campaign"] += 1
        signals.append(s)

    signals.sort(key=lambda s: -s["score"])
    out = {"stats": stats, "signals": signals, "dropped": dict(dropped),
           "campaigns": {k: sorted({i["author"] for i in v}) for k, v in campaigns.items()}}
    path = os.path.join(a.run_dir, "signals.json")
    with open(path, "w") as f:
        json.dump(out, f, indent=1)

    own_n = sum(1 for s in signals if s["is_own_channel"])
    print(f"\n{len(signals)} signals ({own_n} on your channel, {len(signals)-own_n} competitor) "
          f"→ {path}", file=sys.stderr)
    print(f"dropped: {dict(dropped)}", file=sys.stderr)
    if campaigns:
        for k, v in sorted(campaigns.items(), key=lambda kv: -len(kv[1])):
            print(f"?? suspected campaign: \"{k}\" requested by {len({i['author'] for i in v})} authors "
                  f"across {len({i['channel'] for i in v})} channels ({len(v)} comments) — FLAGGED, not dropped. "
                  f"Judge it before clustering.", file=sys.stderr)


if __name__ == "__main__":
    main()
