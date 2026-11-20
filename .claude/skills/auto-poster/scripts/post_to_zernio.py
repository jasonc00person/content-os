#!/usr/bin/env python3
import argparse
import json
import mimetypes
import os
import re
import subprocess
import sys
import time
import uuid
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import urlparse
from zoneinfo import ZoneInfo


ZERNIO_URL = "https://zernio.com/api/v1"


def load_env(path):
    env_path = Path(path)
    if not env_path.exists():
        return
    for raw in env_path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key, value = key.strip(), value.strip()
        if value[:1] in ('"', "'"):
            value = value.strip('"').strip("'")
        else:
            # `KEY=id    # platform: name` (the --list-accounts line) pasted
            # verbatim: the comment must not become part of the account id.
            value = re.split(r"\s+#", value, maxsplit=1)[0]
        # The skill .env is authoritative for ZERNIO_* keys: it must win over
        # anything already exported in the shell (a stale ID in the environment
        # would otherwise silently override the file).
        if key.startswith("ZERNIO_"):
            os.environ[key] = value
        else:
            os.environ.setdefault(key, value)


def is_url(value):
    parsed = urlparse(value)
    return parsed.scheme in ("http", "https") and bool(parsed.netloc)


def run(cmd, timeout=120):
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    if result.returncode != 0:
        raise RuntimeError((result.stderr or result.stdout or "command failed").strip())
    return result.stdout.strip()


def curl_json(method, url, api_key=None, payload=None, headers=None, timeout=120):
    cmd = ["curl", "-sS", "-X", method, url]
    if api_key:
        cmd.extend(["-H", f"Authorization: Bearer {api_key}"])
    for header in headers or []:
        cmd.extend(["-H", header])
    if payload is not None:
        cmd.extend(["-H", "Content-Type: application/json", "-d", json.dumps(payload)])

    stdout = run(cmd, timeout=timeout)
    try:
        return json.loads(stdout)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"Zernio returned non-JSON response: {stdout[:500]}") from exc


def guess_content_type(path):
    guessed, _ = mimetypes.guess_type(str(path))
    suffix = path.suffix.lower()
    overrides = {
        ".mp4": "video/mp4",
        ".mov": "video/quicktime",
        ".m4v": "video/x-m4v",
        ".avi": "video/x-msvideo",
        ".webm": "video/webm",
    }
    return overrides.get(suffix, guessed or "video/mp4")


def verify_url(url, required=True, attempts=5, delay=3):
    # Check the actual HTTP status code, NOT a substring of the header dump:
    # a Content-Length like 102040443 contains "404" and would false-positive.
    # Retry a few times because freshly-uploaded objects can 404 briefly while
    # they propagate.
    last = None
    for attempt in range(attempts):
        try:
            last = run(
                ["curl", "-sI", "-o", os.devnull, "-w", "%{http_code}", url],
                timeout=20,
            ).strip()
        except Exception as exc:
            last = f"err:{exc}"
        else:
            if last not in ("403", "404", "000"):
                return
        if attempt < attempts - 1:
            time.sleep(delay)

    msg = f"Media URL not reachable (last status {last}): {url}"
    if required:
        raise RuntimeError(msg)
    # Media we uploaded ourselves: the PUT already succeeded, and Zernio reads it
    # server-side, so a client-side HEAD failure shouldn't block the post.
    print(f"warning: {msg} — proceeding (media was uploaded by us)", file=sys.stderr)


def zernio_base_url():
    return (os.environ.get("ZERNIO_API_URL") or ZERNIO_URL).rstrip("/")


def upload_to_zernio(api_key, video_path):
    path = Path(video_path).expanduser()
    if not path.exists():
        raise FileNotFoundError(f"Video not found: {path}")
    if not path.is_file():
        raise ValueError(f"Video path is not a file: {path}")

    content_type = guess_content_type(path)
    presign = curl_json(
        "POST",
        f"{zernio_base_url()}/media/presign",
        api_key=api_key,
        payload={
            "filename": path.name,
            "contentType": content_type,
            "size": path.stat().st_size,
        },
        timeout=90,
    )
    if presign.get("error"):
        raise RuntimeError(f"Zernio presign failed: {presign}")

    upload_url = presign.get("uploadUrl")
    public_url = presign.get("publicUrl")
    if not upload_url or not public_url:
        raise RuntimeError(f"Zernio presign response missing uploadUrl/publicUrl: {presign}")

    run(
        [
            "curl",
            "-sS",
            "--fail",
            "-X",
            "PUT",
            upload_url,
            "-H",
            f"Content-Type: {content_type}",
            "--upload-file",
            str(path),
        ],
        timeout=3600,
    )
    return public_url


def caption_from_args(args):
    if args.caption_file:
        return Path(args.caption_file).expanduser().read_text(encoding="utf-8").strip()
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


def optional_env(*names):
    for name in names:
        value = os.environ.get(name)
        if value:
            return value
    return None


def parse_platforms(value):
    platforms = [p.strip().lower() for p in value.split(",") if p.strip()]
    aliases = {"x": "twitter", "twitter/x": "twitter"}
    platforms = [aliases.get(platform, platform) for platform in platforms]
    allowed = {
        "instagram",
        "tiktok",
        "youtube",
        "twitter",
        "linkedin",
        "facebook",
        "threads",
        "pinterest",
        "reddit",
        "bluesky",
    }
    invalid = sorted(set(platforms) - allowed)
    if invalid:
        raise ValueError(f"Unsupported platform(s): {', '.join(invalid)}")
    return platforms


def account_id_for(platform):
    normalized = platform.upper().replace("-", "_")
    return optional_env(
        f"ZERNIO_ACCOUNT_{normalized}",
        f"ZERNIO_ACCOUNT_ID_{normalized}",
    )


def configured_platforms():
    # Default target set = every account with an ID in the env after load_env,
    # i.e. every ZERNIO_ACCOUNT_<PLATFORM> / ZERNIO_ACCOUNT_ID_<PLATFORM> key.
    found = []
    for key, value in os.environ.items():
        if not value:
            continue
        for prefix in ("ZERNIO_ACCOUNT_ID_", "ZERNIO_ACCOUNT_"):
            if key.startswith(prefix):
                platform = key[len(prefix):].lower()
                if platform not in found:
                    found.append(platform)
                break
    if not found:
        raise RuntimeError(
            "No platforms given and no ZERNIO_ACCOUNT_<PLATFORM> keys in the env file; "
            "add your connected account IDs or pass --platforms"
        )
    return sorted(found)


def platform_targets(platforms, require_accounts):
    targets = []
    missing = []
    for platform in platforms:
        account_id = account_id_for(platform)
        target = {"platform": platform}
        if account_id:
            target["accountId"] = account_id
        elif require_accounts:
            missing.append(f"ZERNIO_ACCOUNT_{platform.upper()}")
        targets.append(target)
    if missing:
        raise RuntimeError("Missing required env var(s): " + ", ".join(missing))
    return targets


def media_item(media_url):
    path = Path(urlparse(media_url).path)
    guessed = guess_content_type(path)
    media_type = "image" if guessed.startswith("image/") else "video"
    return {"type": media_type, "url": media_url}


SHORT_MAX_SECONDS = 180


def probe_media(source):
    """Return displayed (width, height, duration_seconds) via ffprobe, or None if it can't be read."""
    try:
        out = run(
            [
                "ffprobe", "-v", "error", "-select_streams", "v:0",
                "-show_streams", "-show_format", "-of", "json", source,
            ],
            timeout=60,
        )
        data = json.loads(out)
        stream = (data.get("streams") or [{}])[0]
        width, height = int(stream.get("width") or 0), int(stream.get("height") or 0)
        duration = float((data.get("format") or {}).get("duration") or 0)
        if not (width and height and duration):
            return None
        # Phone clips store landscape pixels plus a rotation flag and display
        # vertical; YouTube classifies on the displayed shape.
        rotation = (stream.get("tags") or {}).get("rotate") or next(
            (sd["rotation"] for sd in stream.get("side_data_list", []) if "rotation" in sd), 0
        )
        if abs(int(float(rotation))) % 180 == 90:
            width, height = height, width
        return width, height, duration
    except Exception:
        return None


def youtube_gate(platforms, source, allow_long_form):
    """YouTube has no Shorts flag: it classifies a Short purely from the file
    (vertical or square AND <= 3 min). Anything else uploads as a LONG-FORM video on the
    channel. This skill posts short-form, so YouTube is dropped unless the
    file will land as a Short or --yt-long-form was passed on purpose."""
    if "youtube" not in platforms:
        return platforms
    probe = probe_media(source)
    if probe:
        width, height, duration = probe
        is_short = height >= width and duration <= SHORT_MAX_SECONDS
        shape = f"{width}x{height}, {duration:.0f}s"
    else:
        is_short = False
        shape = "ffprobe could not read the file"
    if is_short:
        return platforms
    if allow_long_form:
        print(f"warning: YouTube: {shape} → publishing as a LONG-FORM video (--yt-long-form)", file=sys.stderr)
        return platforms
    print(
        f"warning: YouTube DROPPED: {shape} would upload as a LONG-FORM video, not a Short "
        f"(a Short must be vertical or square and <= {SHORT_MAX_SECONDS}s). Reframe to 9:16 for a Short, "
        f"or pass --yt-long-form to publish long-form on purpose.",
        file=sys.stderr,
    )
    remaining = [p for p in platforms if p != "youtube"]
    if not remaining:
        raise RuntimeError("no platforms left after the YouTube Shorts gate; nothing posted")
    return remaining


# Zernio deletes an upload after 7 days if no post using it has published.
UPLOAD_TTL = timedelta(days=6)  # one day of margin
CAPTION_LIMITS = {"threads": 500, "instagram": 2200, "tiktok": 2200, "linkedin": 3000}
# Meta's Reels cap for API publishing (IG User Media reference), the same 300 MB the video-editor's Reels export
# is sized under (1080x1920, CBR 14). The 2026-08-07 hang was a 612 MB 4K export, so 4K is refused too.
IG_MAX_BYTES = 300 * 1000 * 1000
IG_MAX_SHORT_SIDE = 1080
RESCALE_1080 = (
    "ffmpeg -i IN.mp4 -vf \"scale='if(gt(iw,ih),-2,1080)':'if(gt(iw,ih),1080,-2)'\" "
    "-c:v libx264 -crf 20 -maxrate 12M -bufsize 24M -c:a aac -b:a 160k -movflags +faststart OUT.mp4"
)


def resolve_due(due_at, tz_name):
    """Read --due-at exactly as Zernio will (no offset = local time in tz_name)."""
    try:
        tz = ZoneInfo(tz_name)
    except Exception:
        raise RuntimeError(
            f"unknown timezone {tz_name!r}: use an IANA name like America/Chicago "
            "(on Windows, `python -m pip install tzdata` first)"
        )
    try:
        due = datetime.fromisoformat(due_at.strip().replace("Z", "+00:00"))
    except ValueError:
        raise RuntimeError(f"--due-at {due_at!r} is not an ISO time; use e.g. 2026-09-25T11:30:00")
    if due.tzinfo is None:
        due = due.replace(tzinfo=tz)
    return due.astimezone(tz)


def check_schedule(due, uploading):
    now = datetime.now(timezone.utc)
    when = due.strftime("%a %Y-%m-%d %H:%M %Z")
    if due <= now + timedelta(minutes=2):
        raise RuntimeError(
            f"--due-at resolves to {when}, which is in the past (or under 2 minutes out): Zernio "
            "publishes a past time IMMEDIATELY. Fix the date, or use --mode shareNow to post now."
        )
    if uploading and due - now > UPLOAD_TTL:
        raise RuntimeError(
            f"--due-at resolves to {when}, more than 6 days out: Zernio deletes an upload after 7 days "
            "if its post hasn't published, so the video would be gone at publish time. "
            "Schedule within 6 days, or run this again closer to the date."
        )


def check_caption_limits(platforms, caption, threads_caption):
    over = []
    for platform in platforms:
        text = threads_caption if platform == "threads" and threads_caption else caption
        limit = CAPTION_LIMITS.get(platform)
        if limit and len(text) > limit:
            over.append(f"{platform} {len(text)}/{limit} chars")
    if over:
        hint = ""
        if any(o.startswith("threads") for o in over):
            hint = " For Threads, pass --threads-caption with an under-500-character version."
        raise RuntimeError(
            "caption too long for " + ", ".join(over) + " (the platform rejects it at publish time)." + hint
        )


def check_instagram_size(platforms, source):
    if "instagram" not in platforms or is_url(source):
        return
    size = Path(source).expanduser().stat().st_size
    shape = probe_media(source)
    too_sharp = shape is not None and min(shape[0], shape[1]) > IG_MAX_SHORT_SIDE
    if size > IG_MAX_BYTES or too_sharp:
        dims = f", {shape[0]}x{shape[1]}" if shape else ""
        raise RuntimeError(
            f"{size / 1e6:.0f} MB{dims}: Instagram's API takes Reels up to 300 MB, and a 4K source hangs at "
            "awaiting-finalize (612 MB 4K, hit 2026-08-07). Post the video-editor's Reels export (1080 short side, "
            f"under 300 MB), or re-encode with the framing untouched, then post the new file:\n  {RESCALE_1080}"
        )


def check_not_already_posted(api_key, caption, platforms):
    """An interrupted run can still have posted, and a re-run re-uploads the file
    (new media URL), so Zernio's own 24h content-hash 409 misses the duplicate
    (hit 2026-06-29). Refuse when the same caption already has a live or queued
    entry on a target platform; failed/cancelled entries may be retried."""
    if not caption:
        return
    for post in list_recent_posts(api_key, limit=50):
        if (post.get("content") or "").strip() != caption or not _is_recent(post, minutes=24 * 60):
            continue
        clash = [
            pf.get("platform")
            for pf in post.get("platforms", [])
            if pf.get("platform") in platforms and (pf.get("status") or "").lower() not in ("failed", "cancelled")
        ]
        if clash:
            raise RuntimeError(
                f"this caption is already {post.get('status')} on {', '.join(clash)} as post "
                f"{post.get('_id') or post.get('id')} (created {post.get('createdAt')}). Not posting a duplicate. "
                "Check it with --status <post_id>; to replace a scheduled one, DELETE /posts/<post_id> first; "
                "to retry only failed platforms, pass --platforms with just those."
            )


def build_payload(args, platforms, media_url, caption, title):
    require_accounts = not args.allow_default_accounts
    payload = {
        "content": caption,
        "mediaItems": [media_item(media_url)],
        "platforms": platform_targets(platforms, require_accounts),
    }
    if args.timezone:
        # Only meaningful for customScheduled (main() enforces it there);
        # shareNow/addToQueue/draft just pass it through when configured.
        payload["timezone"] = args.timezone

    if "youtube" in platforms and (title or args.yt_visibility):
        # Zernio ignores a top-level "title" (verified 2026-09-08: the Short went
        # up titled with the caption's first line). YouTube options live in the
        # target's platformSpecificData per docs.zernio.com/platforms/youtube.
        # Visibility defaults to public on Zernio's side when omitted.
        yt_data = {}
        if title:
            yt_data["title"] = title[:100]
        if args.yt_visibility:
            yt_data["visibility"] = args.yt_visibility
        for target in payload["platforms"]:
            if target.get("platform") == "youtube":
                target["platformSpecificData"] = yt_data

    if "threads" in platforms and args.threads_caption:
        for target in payload["platforms"]:
            if target.get("platform") == "threads":
                target["customContent"] = args.threads_caption

    if "instagram" in platforms and args.ig_collaborators:
        # Collab invite (docs.zernio.com/platforms/instagram: up to 3 usernames of
        # public Business/Creator accounts). A rejected username is dropped, not
        # fatal: GET the post and read droppedCollaborators to see it.
        names = [n.strip().lstrip("@") for n in args.ig_collaborators.split(",") if n.strip()]
        for target in payload["platforms"]:
            if target.get("platform") == "instagram":
                target["platformSpecificData"] = {"collaborators": names[:3]}

    if "tiktok" in platforms and args.tiktok_draft:
        # Zernio's TikTok app shares TikTok's rolling-24h direct-post cap across
        # all its users; when it is "at capacity" the only same-day route is the
        # Creator Inbox draft (Jason finishes the post in the TikTok app).
        payload["tiktokSettings"] = {"draft": True}

    if args.mode == "shareNow":
        payload["publishNow"] = True
    elif args.mode == "customScheduled":
        payload["scheduledFor"] = args.due_at
    elif args.mode == "addToQueue":
        payload["queuedFromProfile"] = require_env("ZERNIO_PROFILE_ID")
        queue_id = optional_env("ZERNIO_QUEUE_ID")
        if queue_id:
            payload["queueId"] = queue_id
    elif args.mode == "draft":
        payload["isDraft"] = True

    return payload


def create_post(api_key, payload, request_id, timeout=240):
    return curl_json(
        "POST",
        f"{zernio_base_url()}/posts",
        api_key=api_key,
        payload=payload,
        headers=[f"x-request-id: {request_id}"],
        timeout=timeout,
    )


def extract_posts(data):
    if isinstance(data, list):
        return data
    if isinstance(data, dict):
        for key in ("posts", "data", "results", "items"):
            value = data.get(key)
            if isinstance(value, list):
                return value
            if isinstance(value, dict):
                nested = extract_posts(value)
                if nested:
                    return nested
    return []


def extract_post(response):
    if not isinstance(response, dict):
        return {}
    # `existingPost` = Zernio replaying the original for a repeated x-request-id.
    return response.get("post") or response.get("existingPost") or response.get("data", {}).get("post") or {}


def list_recent_posts(api_key, limit=10):
    # created-desc: the default sort is scheduled-desc, where future scheduled
    # posts crowd a just-created one off the page.
    data = curl_json(
        "GET", f"{zernio_base_url()}/posts?limit={limit}&sortBy=created-desc", api_key=api_key, timeout=60
    )
    return extract_posts(data)


def get_post(api_key, post_id):
    data = curl_json("GET", f"{zernio_base_url()}/posts/{post_id}", api_key=api_key, timeout=60)
    post = extract_post(data)
    if not post:
        raise RuntimeError(f"Zernio returned no post for {post_id}: {json.dumps(data)[:300]}")
    return post


def _is_recent(post, minutes=15):
    ts = post.get("createdAt") or post.get("updatedAt")
    if not ts:
        return True
    try:
        dt = datetime.fromisoformat(str(ts).replace("Z", "+00:00"))
    except ValueError:
        return True
    return (datetime.now(timezone.utc) - dt).total_seconds() <= minutes * 60


def find_recent_post(api_key, caption, media_basename=None):
    # Used to recover after a timed-out create: a create request can succeed
    # server-side even when the client's HTTP call times out. Match on the
    # exact caption (recent only) so we never confuse it with an older post.
    try:
        posts = list_recent_posts(api_key, limit=10)
    except Exception:
        return None
    target = (caption or "").strip()
    # An empty caption would match any recent captionless post, so only match on
    # caption when there is one; otherwise fall through to the media basename.
    if target:
        for post in posts:
            if not _is_recent(post):
                continue
            if (post.get("content") or "").strip() == target:
                return post
    if media_basename:
        for post in posts:
            if not _is_recent(post):
                continue
            for item in post.get("mediaItems", []):
                if str(item.get("url", "")).rsplit("/", 1)[-1] == media_basename:
                    return post
    return None


def reconcile(api_key, caption, media_basename=None, attempts=4, delay=4):
    for attempt in range(attempts):
        found = find_recent_post(api_key, caption, media_basename)
        if found:
            return found
        if attempt < attempts - 1:
            time.sleep(delay)
    return None


def create_post_resilient(api_key, payload, caption, media_basename, max_retries=1):
    # One stable request id for the whole logical post: if Zernio honors
    # x-request-id for idempotency, retries dedupe; if it doesn't, the
    # reconcile() guard below still prevents duplicates.
    request_id = str(uuid.uuid4())
    caption = (caption or "").strip()
    last_error = None

    for attempt in range(max_retries + 1):
        try:
            response = create_post(api_key, payload, request_id)
        except Exception as exc:
            # Network error or timeout: the post MAY have landed. Never blind-retry.
            last_error = exc
            recovered = reconcile(api_key, caption, media_basename)
            if recovered:
                return recovered, "recovered-after-timeout"
            continue  # genuinely didn't land -> safe retry with same request_id

        post = extract_post(response)
        if post:
            # Includes a 207 (inline publish partly failed), which carries both
            # `post` and `error`: the post exists, so report it, never raise.
            return post, "created"

        if isinstance(response, dict) and response.get("error"):
            recovered = reconcile(api_key, caption, media_basename, attempts=2, delay=3)
            if recovered:
                return recovered, "recovered-after-error"
            raise RuntimeError(f"Zernio create failed: {json.dumps(response)[:500]}")

        recovered = reconcile(api_key, caption, media_basename, attempts=2, delay=3)
        if recovered:
            return recovered, "recovered"
        raise RuntimeError(f"Zernio returned no post and no error: {json.dumps(response)[:500]}")

    recovered = reconcile(api_key, caption, media_basename)
    if recovered:
        return recovered, "recovered-after-retries"
    raise RuntimeError(f"create_post failed and no matching post was found: {last_error}")


FAILED_STATUSES = {"failed", "error", "rejected"}
TERMINAL_STATUSES = {"published", "posted", "cancelled"} | FAILED_STATUSES


def wait_for_terminal(api_key, post, max_seconds, delay=5):
    post_id = post.get("_id") or post.get("id")
    if not post_id or max_seconds <= 0:
        return post
    latest, waited = post, 0
    while waited < max_seconds:
        platforms = latest.get("platforms", [])
        if platforms and all(
            (pf.get("status") or "").lower() in TERMINAL_STATUSES for pf in platforms
        ):
            return latest
        time.sleep(delay)
        waited += delay
        try:
            latest = get_post(api_key, post_id)
        except Exception:
            pass  # the post exists; a failed poll must not turn into a failed run
    return latest


def list_accounts(api_key):
    # The one hardened way to get ZERNIO_ACCOUNT_<PLATFORM> ids: prints
    # platform + id + display name as paste-ready .env lines. Never prints the key.
    data = curl_json("GET", f"{zernio_base_url()}/accounts", api_key=api_key, timeout=60)
    if isinstance(data, dict) and data.get("error"):
        raise RuntimeError(f"Zernio accounts request failed: {json.dumps(data)[:500]}")
    accounts = data.get("accounts") if isinstance(data, dict) else data
    if not isinstance(accounts, list):
        raise RuntimeError(f"Zernio returned no accounts list: {json.dumps(data)[:500]}")
    if not accounts:
        print("# 0 connected Zernio accounts. Connect a platform in Zernio first, then re-run.")
        return
    print(
        f"# {len(accounts)} connected Zernio account(s). Paste the lines you want as "
        "default posting targets into .claude/skills/auto-poster/.env"
    )
    for acct in accounts:
        platform = str(acct.get("platform") or "unknown")
        key = "ZERNIO_ACCOUNT_" + platform.upper().replace("-", "_")
        account_id = acct.get("_id") or acct.get("id") or ""
        name = acct.get("displayName") or acct.get("username") or acct.get("name") or ""
        print(f"{key}={account_id}    # {platform}: {name}")


def summarize_post(post):
    if not post:
        return {}
    return {
        "post_id": post.get("_id") or post.get("id"),
        "status": post.get("status"),
        "scheduled_for": post.get("scheduledFor"),
        "platforms": [
            {
                "platform": platform.get("platform"),
                "status": platform.get("status"),
                "platform_post_url": platform.get("platformPostUrl"),
                # Zernio puts the reason in errorMessage; `error` was always null.
                "error": platform.get("errorMessage") or platform.get("error"),
            }
            for platform in post.get("platforms", [])
        ],
    }


def failed_platforms(summary):
    return [
        f"{p['platform']}: {p['error'] or p['status']}"
        for p in summary.get("platforms", [])
        if (p.get("status") or "").lower() in FAILED_STATUSES
    ]


def status_report(api_key, post_id):
    """--status POST_ID: one post. --status alone: everything queued or in
    flight, plus anything that failed in the last 14 days. Returns failures."""
    if post_id:
        summaries = [summarize_post(get_post(api_key, post_id))]
    else:
        summaries = [
            summarize_post(p)
            for p in list_recent_posts(api_key, limit=100)
            if p.get("status") in ("scheduled", "publishing")
            or (p.get("status") in ("partial", "failed") and _is_recent(p, minutes=14 * 24 * 60))
        ]
    print(json.dumps(summaries[0] if post_id else summaries, indent=2))
    return [f for s in summaries for f in failed_platforms(s)]


def main():
    parser = argparse.ArgumentParser(description="Post a provided video directly to Zernio.")
    parser.add_argument("video", nargs="?", help="Local video path or public video URL (omit only with --list-accounts)")
    parser.add_argument("--list-accounts", action="store_true", help="List the connected Zernio accounts (platform, id, display name) as paste-ready ZERNIO_ACCOUNT_<PLATFORM>= lines and exit; the API key is never printed")
    parser.add_argument("--status", nargs="?", const="", metavar="POST_ID", help="Check a post by id (did it go out?), or with no id list everything scheduled/in flight plus failures from the last 14 days, and exit. Exit 2 if any platform failed")
    parser.add_argument("--caption", default="", help="Caption text")
    parser.add_argument("--threads-caption", help="Under-500-character Threads version of the caption (sent as Threads customContent); required when the caption is over 500 chars and Threads is a target")
    parser.add_argument("--caption-file", help="Path to a caption text file")
    parser.add_argument("--platforms", default=None, help="Comma-separated platform list; default = every ZERNIO_ACCOUNT_<PLATFORM> key in the env file")
    parser.add_argument(
        "--mode",
        default="shareNow",
        choices=["shareNow", "addToQueue", "customScheduled", "draft"],
    )
    parser.add_argument("--due-at", help="ISO time for customScheduled mode")
    parser.add_argument("--timezone", default=None, help="IANA timezone for --mode customScheduled, e.g. America/New_York; default = ZERNIO_TIMEZONE from the env file. Required for customScheduled, ignored by shareNow")
    parser.add_argument("--yt-title", help="YouTube title")
    parser.add_argument("--yt-visibility", choices=["public", "private", "unlisted"], help="YouTube visibility; default = Zernio's default (public)")
    parser.add_argument("--ig-collaborators", help="Comma-separated Instagram usernames to invite as collaborators on the Reel (up to 3, e.g. a sponsor's handle)")
    parser.add_argument("--tiktok-draft", action="store_true", help="Deliver TikTok to the Creator Inbox as a draft instead of direct-publishing (the workaround when Zernio reports TikTok direct posting is at capacity)")
    parser.add_argument("--yt-long-form", action="store_true", help="Deliberately publish to YouTube as a long-form video. Without it, YouTube is dropped unless the file qualifies as a Short (vertical, <= 3 min)")
    parser.add_argument("--allow-default-accounts", action="store_true", help="Send platform names without explicit account IDs")
    parser.add_argument("--dry-run", action="store_true", help="Print the Zernio payload and exit before any upload, verify, or post (zero network calls)")
    parser.add_argument("--skip-verify", action="store_true", help="Skip the media URL reachability check")
    parser.add_argument("--wait-seconds", type=int, default=0, help="shareNow only: poll the created post until every platform reaches a terminal state, up to N seconds (ignored for scheduled/queued/draft)")
    parser.add_argument("--max-retries", type=int, default=1, help="Safe create retries; each is guarded by reconciliation so timeouts never duplicate")
    parser.add_argument("--env-file", default=str(Path(__file__).resolve().parent.parent / ".env"))
    args = parser.parse_args()

    load_env(args.env_file)

    if args.list_accounts:
        list_accounts(require_env("ZERNIO_API_KEY"))
        return
    if args.status is not None:
        failures = status_report(require_env("ZERNIO_API_KEY"), args.status)
        if failures:
            print("error: failed platform(s): " + "; ".join(failures), file=sys.stderr)
            sys.exit(2)
        return
    if not args.video:
        parser.error("video is required (local path or public URL) unless --list-accounts or --status is given")

    if not args.timezone:
        # Resolved after load_env so ZERNIO_TIMEZONE in the env file is honored.
        args.timezone = os.environ.get("ZERNIO_TIMEZONE")

    if args.mode == "customScheduled":
        if not args.due_at:
            raise RuntimeError("--due-at is required when --mode customScheduled")
        if not args.timezone:
            raise RuntimeError(
                "--mode customScheduled needs a timezone: pass --timezone <IANA zone> "
                "(e.g. America/New_York) or set ZERNIO_TIMEZONE in the skill .env"
            )

    api_key = require_env("ZERNIO_API_KEY")
    platforms = parse_platforms(args.platforms) if args.platforms else configured_platforms()
    platforms = youtube_gate(platforms, args.video, args.yt_long_form)
    caption = caption_from_args(args)
    args.threads_caption = (args.threads_caption or "").strip() or None
    title = yt_title_from_args(args, args.video, caption)

    # Every gate runs before any upload or post, dry run included: a scheduled
    # post that breaks one of these fails later with nobody watching.
    due = None
    if args.mode == "customScheduled":
        due = resolve_due(args.due_at, args.timezone)
        check_schedule(due, uploading=not is_url(args.video))
    check_caption_limits(platforms, caption, args.threads_caption)
    check_instagram_size(platforms, args.video)

    if args.dry_run:
        # Zero network side effects: no presign, no upload, no reachability
        # check, no post. The local path stands in for the media URL.
        payload = build_payload(args, platforms, args.video, caption, title)
        print(
            json.dumps(
                {
                    "media_url": args.video,
                    "would_upload": not is_url(args.video),
                    "scheduled_local": due.strftime("%a %Y-%m-%d %H:%M %Z") if due else None,
                    "payload": payload,
                },
                indent=2,
            )
        )
        return

    check_not_already_posted(api_key, caption, platforms)
    media_url = args.video if is_url(args.video) else upload_to_zernio(api_key, args.video)
    media_basename = Path(urlparse(media_url).path).name

    if not args.skip_verify:
        # Hard-fail only for URLs the user gave us; for media we just uploaded,
        # a client-side reachability failure is a warning, not a blocker.
        verify_url(media_url, required=is_url(args.video))

    payload = build_payload(args, platforms, media_url, caption, title)

    post, source = create_post_resilient(
        api_key, payload, caption, media_basename, max_retries=args.max_retries
    )
    if args.mode == "shareNow":
        # Only shareNow reaches a terminal per-platform state; scheduled, queued,
        # and draft posts would sit in a pending state until the full timeout.
        post = wait_for_terminal(api_key, post, args.wait_seconds)

    result = summarize_post(post)
    problems = failed_platforms(result)
    if due and result.get("scheduled_for"):
        landed = datetime.fromisoformat(str(result["scheduled_for"]).replace("Z", "+00:00"))
        if abs((landed - due).total_seconds()) > 60:
            problems.append(
                f"Zernio scheduled it for {landed.astimezone(due.tzinfo):%a %Y-%m-%d %H:%M %Z}, "
                f"not {due:%a %Y-%m-%d %H:%M %Z}"
            )
    print(
        json.dumps(
            {
                "media_url": media_url,
                "mode": args.mode,
                "platforms": platforms,
                "scheduled_local": due.strftime("%a %Y-%m-%d %H:%M %Z") if due else None,
                "source": source,
                "result": result,
            },
            indent=2,
        )
    )
    if problems:
        print(
            f"error: post {result.get('post_id')} was created but: " + "; ".join(problems)
            + ". Do NOT re-run the same command: retry only the failed platform(s) with --platforms "
            "(TikTok at capacity: add --tiktok-draft), or fix the schedule in Zernio.",
            file=sys.stderr,
        )
        sys.exit(2)


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        sys.exit(1)
