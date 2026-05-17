#!/usr/bin/env python3
"""
generate.py — submit broll.json moments to Higgsfield, poll, download.

Reads:    /tmp/video-editor/<job>/broll.json
Writes:   /tmp/video-editor/<job>/broll/<id>.mp4   (one per moment)
          /tmp/video-editor/<job>/broll_resolved.json   (manifest + local paths)

Auth: HIGGSFIELD_API_KEY env var.

Usage:
    generate.py <broll.json> [--only <id>[,<id>...]] [--dry-run] [--yes]
"""
import argparse
import json
import os
import sys
import time
import urllib.request
import urllib.error
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

API_BASE = "https://api.higgsfield.ai"
POLL_INTERVAL_S = 6
POLL_TIMEOUT_S = 600  # 10 min cap per clip


def api_post(path: str, body: dict, api_key: str) -> dict:
    req = urllib.request.Request(
        API_BASE + path,
        data=json.dumps(body).encode(),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read())


def api_get(path: str, api_key: str) -> dict:
    req = urllib.request.Request(
        API_BASE + path,
        headers={"Authorization": f"Bearer {api_key}"},
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read())


def download(url: str, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(url, timeout=120) as r, open(dest, "wb") as f:
        while True:
            chunk = r.read(1 << 16)
            if not chunk:
                break
            f.write(chunk)


def generate_one(moment: dict, duration: float, out_dir: Path, api_key: str) -> dict:
    """Submit one moment, poll until done, download. Returns {id, status, path|error}."""
    mid = moment["id"]
    prompt = moment["prompt"]

    body = {
        "task": "text-to-video",
        "model": "default-video-model",
        "prompt": prompt,
        "duration": duration,
        "fps": 30,
    }

    try:
        sub = api_post("/v1/generations", body, api_key)
        gen_id = sub.get("generation_id") or sub.get("id") or sub.get("request_id")
        if not gen_id:
            return {"id": mid, "status": "error", "error": f"no id in response: {sub}"}
    except urllib.error.HTTPError as e:
        return {"id": mid, "status": "error", "error": f"submit HTTP {e.code}: {e.read().decode(errors='replace')[:300]}"}
    except Exception as e:
        return {"id": mid, "status": "error", "error": f"submit: {e}"}

    sys.stderr.write(f"[broll] {mid} submitted gen={gen_id}\n")

    started = time.time()
    while time.time() - started < POLL_TIMEOUT_S:
        try:
            res = api_get(f"/v1/generations/{gen_id}", api_key)
        except Exception as e:
            sys.stderr.write(f"[broll] {mid} poll error: {e} — retrying\n")
            time.sleep(POLL_INTERVAL_S)
            continue
        status = (res.get("status") or "").lower()
        if status in {"completed", "succeeded", "success", "done"}:
            video_url = (
                res.get("video_url")
                or res.get("output_url")
                or (res.get("output") or {}).get("video_url")
                or (res.get("result") or {}).get("video_url")
            )
            if not video_url:
                return {"id": mid, "status": "error", "error": f"no video_url in: {res}"}
            local = out_dir / f"{mid}.mp4"
            try:
                download(video_url, local)
            except Exception as e:
                return {"id": mid, "status": "error", "error": f"download: {e}"}
            return {"id": mid, "status": "ok", "path": str(local), "generation_id": gen_id}
        if status in {"failed", "error", "cancelled"}:
            return {"id": mid, "status": "error", "error": f"higgsfield status={status}: {res.get('error') or res.get('message')}"}
        time.sleep(POLL_INTERVAL_S)

    return {"id": mid, "status": "error", "error": f"poll timeout after {POLL_TIMEOUT_S}s"}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("manifest")
    p.add_argument("--only", help="comma-separated moment ids to (re)generate")
    p.add_argument("--dry-run", action="store_true", help="print what would be submitted, don't call API")
    p.add_argument("--yes", action="store_true", help="skip the spending confirmation prompt")
    args = p.parse_args()

    manifest_path = Path(args.manifest)
    manifest = json.loads(manifest_path.read_text())
    moments = manifest.get("moments") or []
    if args.only:
        wanted = set(args.only.split(","))
        moments = [m for m in moments if m["id"] in wanted]
        if not moments:
            sys.stderr.write(f"no moments matched --only={args.only}\n")
            sys.exit(1)

    duration = float(manifest.get("duration_default", 5))
    out_dir = manifest_path.parent / "broll"
    out_dir.mkdir(parents=True, exist_ok=True)

    if not moments:
        sys.stderr.write("[broll] no moments to generate\n")
        sys.exit(1)

    est_low = 0.5 * len(moments)
    est_high = 1.0 * len(moments)
    sys.stderr.write(
        f"[broll] {len(moments)} moments × {duration}s each ≈ ${est_low:.2f}-${est_high:.2f} total\n"
    )

    if args.dry_run:
        for m in moments:
            sys.stderr.write(f"[broll] DRY: {m['id']}  {m['prompt'][:80]}\n")
        sys.exit(0)

    if not args.yes:
        answer = input("[broll] Continue and submit paid generations? [y/N] ").strip().lower()
        if answer not in {"y", "yes"}:
            sys.stderr.write("[broll] cancelled\n")
            sys.exit(0)

    api_key = os.environ.get("HIGGSFIELD_API_KEY", "").strip()
    if not api_key:
        sys.stderr.write("HIGGSFIELD_API_KEY not set in env\n")
        sys.exit(1)

    results = {}
    with ThreadPoolExecutor(max_workers=min(8, len(moments))) as ex:
        futures = {ex.submit(generate_one, m, duration, out_dir, api_key): m for m in moments}
        for fut in as_completed(futures):
            r = fut.result()
            results[r["id"]] = r
            tag = "OK " if r["status"] == "ok" else "ERR"
            sys.stderr.write(f"[broll] {tag} {r['id']}: {r.get('path') or r.get('error')}\n")

    # Write resolved manifest (original + per-moment status/path)
    resolved = dict(manifest)
    resolved["moments"] = []
    for m in manifest.get("moments") or []:
        r = results.get(m["id"])
        if r:
            entry = dict(m)
            entry.update({k: v for k, v in r.items() if k != "id"})
            resolved["moments"].append(entry)
        else:
            resolved["moments"].append(m)
    resolved_path = manifest_path.parent / "broll_resolved.json"
    resolved_path.write_text(json.dumps(resolved, indent=2))
    sys.stderr.write(f"[broll] wrote {resolved_path}\n")

    failed = [r for r in results.values() if r["status"] != "ok"]
    if failed:
        sys.stderr.write(f"[broll] {len(failed)} failed — re-run with --only={','.join(r['id'] for r in failed)}\n")
        sys.exit(2)


if __name__ == "__main__":
    main()
