#!/usr/bin/env python3
"""
generate.py — submit broll.json moments to Higgsfield via the `higgsfield` CLI, wait, collect downloads.

Reads:    /tmp/video-editor/<job>/broll.json
Writes:   /tmp/video-editor/<job>/broll/<id>.mp4          (one per moment)
          /tmp/video-editor/<job>/broll_resolved.json     (manifest + local paths)

Auth: handled by the CLI (`higgsfield auth login`, browser session). No API key.

Usage:
    generate.py <broll.json> [--only <id>[,<id>...]] [--dry-run] [--yes]
"""
import argparse
import json
import re
import shutil
import subprocess
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

DEFAULT_MODEL = "seedance_2_0"
DEFAULT_ASPECT = "9:16"
WAIT_TIMEOUT = "15m"
URL_RE = re.compile(r"https?://[^\s\"'<>]+\.mp4[^\s\"'<>]*")


def extract_video_url(stdout: str) -> str | None:
    # Try JSON first (CLI emits structured output with --json), fall back to regex.
    try:
        data = json.loads(stdout)
        urls: list[str] = []
        def walk(node):
            if isinstance(node, dict):
                for k, v in node.items():
                    if isinstance(v, str) and v.startswith("http") and ".mp4" in v:
                        urls.append(v)
                    else:
                        walk(v)
            elif isinstance(node, list):
                for v in node:
                    walk(v)
        walk(data)
        if urls:
            return urls[0]
    except (json.JSONDecodeError, ValueError):
        pass
    m = URL_RE.search(stdout)
    return m.group(0) if m else None


def download(url: str, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(url, timeout=180) as r, open(dest, "wb") as f:
        while True:
            chunk = r.read(1 << 16)
            if not chunk:
                break
            f.write(chunk)


def ensure_cli() -> None:
    if shutil.which("higgsfield") is None:
        sys.stderr.write(
            "higgsfield CLI not found. Install:\n"
            "  curl -fsSL https://raw.githubusercontent.com/higgsfield-ai/cli/main/install.sh | sh\n"
        )
        sys.exit(1)
    r = subprocess.run(["higgsfield", "account", "status"], capture_output=True, text=True)
    if r.returncode != 0:
        sys.stderr.write(
            "higgsfield CLI not authenticated. Run:\n  higgsfield auth login\n"
            f"(account status said: {(r.stdout or r.stderr).strip()})\n"
        )
        sys.exit(1)


def generate_one(moment: dict, defaults: dict, out_root: Path) -> dict:
    mid = moment["id"]
    model = moment.get("model", defaults["model"])
    duration = int(round(moment.get("duration", defaults["duration"])))
    aspect = moment.get("aspect_ratio", defaults["aspect_ratio"])
    start_image = moment.get("start_image")

    cmd = [
        "higgsfield", "--json", "generate", "create", model,
        "--prompt", moment["prompt"],
        "--duration", str(duration),
        "--aspect_ratio", aspect,
        "--wait", "--wait-timeout", WAIT_TIMEOUT,
    ]
    if start_image:
        cmd += ["--start-image", str(start_image)]

    sys.stderr.write(f"[broll] {mid} submitting ({model}, {duration}s, {aspect}{', i2v' if start_image else ''})\n")
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        err = (r.stderr or r.stdout or "").strip().splitlines()
        return {"id": mid, "status": "error", "error": " | ".join(err[-3:])[:500] or f"exit {r.returncode}"}

    url = extract_video_url(r.stdout)
    if not url:
        return {"id": mid, "status": "error", "error": f"no video url in CLI output: {r.stdout.strip()[:300]}"}

    final_path = out_root / f"{mid}.mp4"
    try:
        download(url, final_path)
    except Exception as e:
        return {"id": mid, "status": "error", "error": f"download {url}: {e}"}
    return {"id": mid, "status": "ok", "path": str(final_path), "source_url": url}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("manifest")
    p.add_argument("--only", help="comma-separated moment ids to (re)generate")
    p.add_argument("--dry-run", action="store_true", help="print what would be submitted, don't call the CLI")
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
    if not moments:
        sys.stderr.write("[broll] no moments to generate\n")
        sys.exit(1)

    defaults = {
        "model": manifest.get("model_default", DEFAULT_MODEL),
        "duration": float(manifest.get("duration_default", 5)),
        "aspect_ratio": manifest.get("aspect_ratio_default", DEFAULT_ASPECT),
    }

    est_low = 0.5 * len(moments)
    est_high = 1.0 * len(moments)
    sys.stderr.write(
        f"[broll] {len(moments)} moments × {defaults['duration']}s each ≈ "
        f"${est_low:.2f}-${est_high:.2f} total\n"
    )

    if args.dry_run:
        for m in moments:
            sys.stderr.write(f"[broll] DRY: {m['id']}  {m['prompt'][:80]}\n")
        sys.exit(0)

    if not args.yes:
        ans = input("[broll] Continue and submit paid generations? [y/N] ").strip().lower()
        if ans not in {"y", "yes"}:
            sys.stderr.write("[broll] cancelled\n")
            sys.exit(0)

    ensure_cli()

    out_root = manifest_path.parent / "broll"
    out_root.mkdir(parents=True, exist_ok=True)

    results = {}
    with ThreadPoolExecutor(max_workers=min(8, len(moments))) as ex:
        futures = {ex.submit(generate_one, m, defaults, out_root): m for m in moments}
        for fut in as_completed(futures):
            r = fut.result()
            results[r["id"]] = r
            tag = "OK " if r["status"] == "ok" else "ERR"
            sys.stderr.write(f"[broll] {tag} {r['id']}: {r.get('path') or r.get('error')}\n")

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
