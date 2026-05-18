#!/usr/bin/env python3
import argparse
import json
import os
import subprocess
import sys
import time
from pathlib import Path
from urllib.parse import urlparse


BUFFER_URL = "https://api.buffer.com"
LITTERBOX_URL = "https://litterbox.catbox.moe/resources/internals/api.php"


def load_env(path):
    env_path = Path(path)
    if not env_path.exists():
        return
    for raw in env_path.read_text().splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        os.environ.setdefault(key, value)


def is_url(value):
    parsed = urlparse(value)
    return parsed.scheme in ("http", "https") and bool(parsed.netloc)


def run(cmd, timeout=120):
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    if result.returncode != 0:
        raise RuntimeError((result.stderr or result.stdout or "command failed").strip())
    return result.stdout.strip()


def upload_to_litterbox(video_path):
    path = Path(video_path).expanduser()
    if not path.exists():
        raise FileNotFoundError(f"Video not found: {path}")
    if not path.is_file():
        raise ValueError(f"Video path is not a file: {path}")

    url = run(
        [
            "curl",
            "-sS",
            "-F",
            "reqtype=fileupload",
            "-F",
            "time=72h",
            "-F",
            f"fileToUpload=@{path}",
            LITTERBOX_URL,
        ],
        timeout=600,
    )
    if not url.startswith("http"):
        raise RuntimeError(f"Litterbox upload failed: {url[:300]}")
    return url


def verify_url(url):
    try:
        headers = run(["curl", "-sI", url], timeout=20)
    except Exception as exc:
        raise RuntimeError(f"Could not verify video URL: {exc}") from exc

    lowered = headers.lower()
    if "404" in lowered or "403" in lowered:
        raise RuntimeError(f"Video URL is not reachable: {url}")

    for line in headers.splitlines():
        if line.lower().startswith("content-length:"):
            try:
                if int(line.split(":", 1)[1].strip()) <= 0:
                    raise RuntimeError(f"Video URL has zero content length: {url}")
            except ValueError:
                pass
            break


def gql(api_key, query, variables=None):
    payload = {"query": query}
    if variables is not None:
        payload["variables"] = variables

    stdout = run(
        [
            "curl",
            "-sS",
            "-X",
            "POST",
            BUFFER_URL,
            "-H",
            f"Authorization: Bearer {api_key}",
            "-H",
            "Content-Type: application/json",
            "-d",
            json.dumps(payload),
        ],
        timeout=90,
    )
    try:
        return json.loads(stdout)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"Buffer returned non-JSON response: {stdout[:500]}") from exc


def caption_from_args(args):
    if args.caption_file:
        return Path(args.caption_file).expanduser().read_text().strip()
    return (args.caption or "").strip()


def yt_title_from_args(args, source, caption):
    if args.yt_title:
        return args.yt_title.strip()
    if caption:
        return caption.splitlines()[0][:95].strip()
    if is_url(source):
        name = Path(urlparse(source).path).stem
        return name or "Video"
    return Path(source).stem or "Video"


def require_env(name):
    value = os.environ.get(name)
    if not value:
        raise RuntimeError(f"Missing required env var: {name}")
    return value


def channel_config(platform, yt_title):
    channel_env = {
        "instagram": "BUFFER_CHANNEL_INSTAGRAM",
        "tiktok": "BUFFER_CHANNEL_TIKTOK",
        "youtube": "BUFFER_CHANNEL_YOUTUBE",
    }
    metadata = {
        "instagram": {"instagram": {"type": "reel", "shouldShareToFeed": True}},
        "tiktok": None,
        "youtube": {
            "youtube": {
                "title": yt_title,
                "privacy": "public",
                "madeForKids": False,
                "notifySubscribers": True,
                "categoryId": "22",
            }
        },
    }
    return {"id": require_env(channel_env[platform]), "metadata": metadata[platform]}


def build_input(channel, text, video_url, mode, due_at):
    payload = {
        "text": text,
        "channelId": channel["id"],
        "schedulingType": "automatic",
        "mode": mode,
        "assets": [{"video": {"url": video_url}}],
    }
    if channel["metadata"]:
        payload["metadata"] = channel["metadata"]
    if mode == "customScheduled":
        payload["dueAt"] = due_at
    return payload


def create_post(api_key, payload):
    mutation = (
        "mutation ($input: CreatePostInput!) { createPost(input: $input) { "
        "... on PostActionSuccess { post { id status dueAt } } "
        "... on MutationError { message } } }"
    )
    for attempt in range(1, 4):
        response = gql(api_key, mutation, {"input": payload})
        if response.get("errors"):
            return {"status": "error", "error": response["errors"], "attempts": attempt}
        result = (response.get("data") or {}).get("createPost") or {}
        message = result.get("message", "")
        if message and "timed out" in message.lower() and attempt < 3:
            time.sleep(5)
            continue
        if message:
            return {"status": "error", "error": message, "attempts": attempt}
        break
    post = result.get("post") or {}
    return {
        "status": post.get("status", "unknown"),
        "post_id": post.get("id"),
        "due_at": post.get("dueAt"),
        "attempts": attempt,
    }


def parse_platforms(value):
    platforms = [p.strip().lower() for p in value.split(",") if p.strip()]
    allowed = {"instagram", "tiktok", "youtube"}
    invalid = sorted(set(platforms) - allowed)
    if invalid:
        raise ValueError(f"Unsupported platform(s): {', '.join(invalid)}")
    return platforms


def main():
    parser = argparse.ArgumentParser(description="Post a provided video directly to Buffer.")
    parser.add_argument("video", help="Local video path or public video URL")
    parser.add_argument("--caption", default="", help="Caption text")
    parser.add_argument("--caption-file", help="Path to a caption text file")
    parser.add_argument("--platforms", default="instagram,tiktok,youtube")
    parser.add_argument(
        "--mode",
        default="shareNow",
        choices=["shareNow", "addToQueue", "shareNext", "customScheduled"],
    )
    parser.add_argument("--due-at", help="UTC ISO time for customScheduled mode")
    parser.add_argument("--yt-title", help="YouTube title")
    parser.add_argument("--env-file", default=".env")
    args = parser.parse_args()

    load_env(args.env_file)

    if args.mode == "customScheduled" and not args.due_at:
        raise RuntimeError("--due-at is required when --mode customScheduled")

    api_key = require_env("BUFFER_API_KEY")
    platforms = parse_platforms(args.platforms)
    caption = caption_from_args(args)
    yt_title = yt_title_from_args(args, args.video, caption)

    video_url = args.video if is_url(args.video) else upload_to_litterbox(args.video)
    verify_url(video_url)

    results = []
    for platform in platforms:
        channel = channel_config(platform, yt_title)
        payload = build_input(channel, caption, video_url, args.mode, args.due_at)
        result = create_post(api_key, payload)
        result["platform"] = platform
        results.append(result)

    print(
        json.dumps(
            {
                "video_url": video_url,
                "mode": args.mode,
                "platforms": platforms,
                "results": results,
            },
            indent=2,
        )
    )

    if any(r.get("status") == "error" for r in results):
        return 1
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
