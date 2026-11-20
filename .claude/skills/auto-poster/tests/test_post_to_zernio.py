#!/usr/bin/env python3
"""Regression tests for post_to_zernio.py against a local mock Zernio API.

Nothing here touches the real Zernio account: every run points the script at
a throwaway env file whose ZERNIO_API_URL is a mock server on 127.0.0.1.
Needs python3, curl, ffmpeg/ffprobe. Run from anywhere:

    python3 .claude/skills/auto-poster/tests/test_post_to_zernio.py
"""
import json
import subprocess
import sys
import tempfile
import threading
import unittest
from datetime import datetime, timedelta
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse
from zoneinfo import ZoneInfo

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "post_to_zernio.py"
TZ = "America/Chicago"
ACCOUNTS = {
    "instagram": "a" * 24, "tiktok": "b" * 24, "youtube": "c" * 24,
    "linkedin": "d" * 24, "facebook": "e" * 24, "threads": "f" * 24,
}


class MockZernio(BaseHTTPRequestHandler):
    state = None  # set by the test class

    def log_message(self, *args):
        pass

    def _send(self, code, body=None):
        raw = b"" if body is None else json.dumps(body).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(raw)))
        self.end_headers()
        if self.command != "HEAD":
            self.wfile.write(raw)

    def _record(self):
        length = int(self.headers.get("Content-Length") or 0)
        body = self.rfile.read(length) if length else b""
        self.state["requests"].append((self.command, self.path, body))
        return body

    def do_HEAD(self):
        self._record()
        self._send(200)

    def do_PUT(self):
        self._record()
        self._send(200)

    def do_GET(self):
        self._record()
        path = urlparse(self.path).path
        posts = self.state["posts"]
        if path == "/posts":
            listed = [] if self.state.get("list_misses") else list(posts.values())
            return self._send(200, {"posts": listed})
        if path.startswith("/posts/"):
            post = posts.get(path.rsplit("/", 1)[-1])
            if self.state.get("publish_on_get") and post:
                for pf in post["platforms"]:
                    pf["status"] = "published"
            return self._send(200, {"post": post}) if post else self._send(404, {"error": "not found"})
        self._send(404, {"error": "no route"})

    def do_POST(self):
        body = self._record()
        path = urlparse(self.path).path
        base = f"http://127.0.0.1:{self.server.server_port}"
        if path == "/media/presign":
            name = json.loads(body)["filename"]
            return self._send(200, {"uploadUrl": f"{base}/upload/{name}", "publicUrl": f"{base}/media/{name}"})
        if path != "/posts":
            return self._send(404, {"error": "no route"})

        payload = json.loads(body)
        self.state["payloads"].append(payload)
        mode = self.state.get("create", "ok")
        post_id = f"{len(self.state['posts']) + 1:024x}"
        now = datetime.now(ZoneInfo("UTC"))
        scheduled = payload.get("scheduledFor")
        if scheduled:
            due = datetime.fromisoformat(scheduled)
            if due.tzinfo is None:
                due = due.replace(tzinfo=ZoneInfo(payload["timezone"]))
            scheduled = due.astimezone(ZoneInfo("UTC")).isoformat().replace("+00:00", "Z")
        live = payload.get("publishNow")
        post = {
            "_id": post_id,
            "content": payload.get("content"),
            "createdAt": now.isoformat().replace("+00:00", "Z"),
            "scheduledFor": scheduled,
            "status": "published" if live else "scheduled",
            "mediaItems": payload.get("mediaItems", []),
            "platforms": [
                {"platform": t["platform"], "status": ("published" if live and mode != "pending" else "pending")}
                for t in payload["platforms"]
            ],
        }
        if mode == "partial":
            post["status"] = "partial"
            for pf in post["platforms"]:
                if pf["platform"] == "tiktok":
                    pf.update(status="failed", errorMessage="TikTok direct posting is at capacity right now.")
        self.state["posts"][post_id] = post
        if mode == "partial":
            return self._send(207, {"post": post, "error": "Some platforms failed", "message": "partial"})
        if mode == "existing":
            return self._send(200, {"existingPost": post})
        if mode == "empty":
            return self._send(200, {})
        self._send(201, {"message": "ok", "post": post})


class AutoPosterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = Path(tempfile.mkdtemp(prefix="autoposter-test-"))
        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), MockZernio)
        threading.Thread(target=cls.server.serve_forever, daemon=True).start()
        cls.base = f"http://127.0.0.1:{cls.server.server_port}"
        cls.env = cls.tmp / "test.env"
        lines = ["ZERNIO_API_KEY=test-key", f"ZERNIO_API_URL={cls.base}", f"ZERNIO_TIMEZONE={TZ}"]
        lines += [f"ZERNIO_ACCOUNT_{p.upper()}={i}" for p, i in ACCOUNTS.items()]
        cls.env.write_text("\n".join(lines) + "\n")

        def make(name, size):
            out = cls.tmp / name
            subprocess.run(
                ["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", f"testsrc=size={size}:rate=30:duration=2",
                 "-c:v", "libx264", "-pix_fmt", "yuv420p", str(out)],
                check=True,
            )
            return out

        cls.vert = make("vert.mp4", "1080x1920")
        cls.land = make("land.mp4", "1920x1080")
        cls.square = make("square.mp4", "1080x1080")
        # Phone-style vertical: stored landscape, displayed portrait via rotation metadata.
        cls.rotated = cls.tmp / "rotated.mp4"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-display_rotation:v:0", "90", "-i", str(cls.land),
                        "-c", "copy", str(cls.rotated)], check=True)
        cls.big = cls.tmp / "big.mp4"
        with open(cls.big, "wb") as f:
            f.truncate(301 * 1000 * 1000)
        cls.reels = cls.tmp / "reels.mp4"  # a Reels-size export: over the old 100 MB gate, under Meta's 300
        with open(cls.reels, "wb") as f:
            f.truncate(163 * 1000 * 1000)
        cls.uhd = make("uhd.mp4", "2160x3840")

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()

    def setUp(self):
        MockZernio.state = {"requests": [], "payloads": [], "posts": {}}

    def run_script(self, *args, env_file=None):
        cmd = [sys.executable, str(SCRIPT), *map(str, args), "--env-file", str(env_file or self.env)]
        return subprocess.run(cmd, capture_output=True, text=True, timeout=120)

    def json_out(self, proc):
        return json.loads(proc.stdout)

    def local_due(self, **delta):
        due = datetime.now(ZoneInfo(TZ)) + timedelta(**delta)
        return due.strftime("%Y-%m-%dT%H:%M:00")

    # --- publish results -------------------------------------------------

    def test_partial_publish_exits_2_and_shows_platform_error(self):
        # 207 carries both `post` and `error`; the post exists even when the
        # recent-posts lookup can't see it. Must report it, not claim failure.
        MockZernio.state.update(create="partial", list_misses=True)
        proc = self.run_script(self.vert, "--caption", "hi")
        self.assertEqual(proc.returncode, 2, proc.stderr)
        tiktok = [p for p in self.json_out(proc)["result"]["platforms"] if p["platform"] == "tiktok"][0]
        self.assertIn("at capacity", tiktok["error"])
        self.assertIn("tiktok", proc.stderr)
        self.assertEqual(len(MockZernio.state["payloads"]), 1)

    def test_idempotent_replay_existing_post_is_success(self):
        MockZernio.state.update(create="existing", list_misses=True)
        proc = self.run_script(self.vert, "--caption", "hi")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertTrue(self.json_out(proc)["result"]["post_id"])

    def test_reconcile_lists_newest_created_first(self):
        # Default GET /posts sort is scheduled-desc: future scheduled posts
        # would crowd a just-created post out of the first page.
        MockZernio.state.update(create="empty")
        proc = self.run_script(self.vert, "--caption", "reconcile me")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        lists = [p for m, p, _ in MockZernio.state["requests"] if m == "GET" and urlparse(p).path == "/posts"]
        self.assertTrue(lists and all("sortBy=created-desc" in p for p in lists), lists)

    def test_wait_polls_the_post_by_id(self):
        MockZernio.state.update(create="pending", publish_on_get=True, list_misses=True)
        proc = self.run_script(self.vert, "--caption", "hi", "--wait-seconds", "12")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertTrue(all(p["status"] == "published" for p in self.json_out(proc)["result"]["platforms"]))

    def test_rerun_of_a_landed_post_is_refused_before_upload(self):
        # An interrupted run can still post; a re-run re-uploads (new media URL),
        # so Zernio's content-hash 409 can't catch it. Hit 2026-06-29.
        self.assertEqual(self.run_script(self.vert, "--caption", "same one").returncode, 0)
        MockZernio.state["requests"].clear()
        proc = self.run_script(self.vert, "--caption", "same one")
        self.assertEqual(proc.returncode, 1, proc.stdout)
        self.assertIn("already", proc.stderr.lower())
        self.assertFalse([r for r in MockZernio.state["requests"] if r[0] in ("PUT", "POST")])

    def test_retry_of_only_the_failed_platform_is_allowed(self):
        MockZernio.state.update(create="partial")
        self.assertEqual(self.run_script(self.vert, "--caption", "same one").returncode, 2)
        MockZernio.state.update(create="ok")
        proc = self.run_script(self.vert, "--caption", "same one", "--platforms", "tiktok", "--tiktok-draft")
        self.assertEqual(proc.returncode, 0, proc.stderr)

    def test_status_command_reports_failures(self):
        MockZernio.state.update(create="partial")
        post_id = self.json_out(self.run_script(self.vert, "--caption", "hi"))["result"]["post_id"]
        proc = self.run_script("--status", post_id)
        self.assertEqual(proc.returncode, 2, proc.stderr)
        self.assertIn("at capacity", proc.stdout)

    # --- scheduling -----------------------------------------------------

    def assert_refused_before_any_network(self, proc, needle):
        self.assertEqual(proc.returncode, 1, proc.stdout)
        self.assertIn(needle, proc.stderr.lower())
        self.assertEqual(MockZernio.state["requests"], [], "must refuse before presign/upload/post")

    def test_schedule_in_the_past_is_refused(self):
        # Zernio publishes a past scheduledFor immediately.
        proc = self.run_script(self.vert, "--caption", "x", "--mode", "customScheduled",
                               "--due-at", self.local_due(hours=-3))
        self.assert_refused_before_any_network(proc, "past")

    def test_schedule_past_upload_ttl_is_refused(self):
        # Zernio deletes an unpublished upload after 7 days.
        proc = self.run_script(self.vert, "--caption", "x", "--mode", "customScheduled",
                               "--due-at", self.local_due(days=8))
        self.assert_refused_before_any_network(proc, "7 days")

    def test_schedule_bad_timezone_is_refused(self):
        proc = self.run_script(self.vert, "--caption", "x", "--mode", "customScheduled",
                               "--due-at", self.local_due(days=1), "--timezone", "America/Chicgo")
        self.assert_refused_before_any_network(proc, "timezone")

    def test_schedule_unparseable_due_at_is_refused(self):
        proc = self.run_script(self.vert, "--caption", "x", "--mode", "customScheduled",
                               "--due-at", "tomorrow 3pm")
        self.assert_refused_before_any_network(proc, "due-at")

    def test_schedule_ok_reports_local_time_and_utc(self):
        due = self.local_due(days=1)
        proc = self.run_script(self.vert, "--caption", "sched", "--mode", "customScheduled", "--due-at", due)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        out = self.json_out(proc)
        payload = MockZernio.state["payloads"][0]
        self.assertEqual(payload["scheduledFor"], due)
        self.assertEqual(payload["timezone"], TZ)
        self.assertNotIn("publishNow", payload)
        self.assertIn(due[11:16], out["scheduled_local"])
        expected_utc = datetime.fromisoformat(due).replace(tzinfo=ZoneInfo(TZ)).astimezone(ZoneInfo("UTC"))
        self.assertEqual(datetime.fromisoformat(out["result"]["scheduled_for"].replace("Z", "+00:00")), expected_utc)

    def test_schedule_with_explicit_offset_is_accepted(self):
        due = (datetime.now(ZoneInfo("UTC")) + timedelta(days=1)).strftime("%Y-%m-%dT%H:%M:00Z")
        proc = self.run_script(self.vert, "--caption", "x", "--mode", "customScheduled", "--due-at", due)
        self.assertEqual(proc.returncode, 0, proc.stderr)

    # --- caption limits -------------------------------------------------

    def test_threads_caption_over_500_is_refused(self):
        proc = self.run_script(self.vert, "--caption", "x" * 600, "--platforms", "instagram,threads")
        self.assert_refused_before_any_network(proc, "threads")

    def test_threads_caption_override_goes_to_custom_content(self):
        proc = self.run_script(self.vert, "--caption", "x" * 600, "--platforms", "instagram,threads",
                               "--threads-caption", "short one", "--dry-run")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        targets = {t["platform"]: t for t in self.json_out(proc)["payload"]["platforms"]}
        self.assertEqual(targets["threads"].get("customContent"), "short one")
        self.assertNotIn("customContent", targets["instagram"])

    def test_instagram_caption_over_2200_is_refused(self):
        proc = self.run_script(self.vert, "--caption", "x" * 2300, "--platforms", "instagram")
        self.assert_refused_before_any_network(proc, "instagram")

    # --- media gates ----------------------------------------------------

    def test_instagram_file_over_300mb_is_refused(self):
        proc = self.run_script(self.big, "--caption", "x", "--platforms", "instagram")
        self.assert_refused_before_any_network(proc, "300 mb")

    def test_instagram_4k_source_is_refused(self):
        proc = self.run_script(self.uhd, "--caption", "x", "--platforms", "instagram")
        self.assert_refused_before_any_network(proc, "2160x3840")

    def test_instagram_reels_size_export_passes_the_gate(self):
        proc = self.run_script(self.reels, "--caption", "x", "--platforms", "instagram", "--dry-run")
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)

    def dry_platforms(self, video):
        proc = self.run_script(video, "--caption", "x", "--platforms", "youtube,instagram", "--dry-run")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        return [t["platform"] for t in self.json_out(proc)["payload"]["platforms"]]

    def test_youtube_gate(self):
        self.assertIn("youtube", self.dry_platforms(self.vert))
        self.assertNotIn("youtube", self.dry_platforms(self.land))
        # YouTube counts square as a Short, and a phone clip's rotation flag
        # makes a landscape-stored file display vertical.
        self.assertIn("youtube", self.dry_platforms(self.square))
        self.assertIn("youtube", self.dry_platforms(self.rotated))

    def test_youtube_visibility_goes_to_platform_specific_data(self):
        proc = self.run_script(self.land, "--caption", "desc", "--platforms", "youtube", "--yt-long-form",
                               "--yt-title", "T", "--yt-visibility", "private", "--dry-run")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        yt = self.json_out(proc)["payload"]["platforms"][0]
        self.assertEqual(yt["platformSpecificData"], {"title": "T", "visibility": "private"})

    # --- env ------------------------------------------------------------

    def test_list_accounts_line_pasted_verbatim_still_parses(self):
        # --list-accounts prints `KEY=id    # platform: name`; pasting that
        # line as-is must not smuggle the comment into the account id.
        env = self.tmp / "comment.env"
        env.write_text(self.env.read_text() + f"ZERNIO_ACCOUNT_TIKTOK={'9' * 24}    # tiktok: Some Name\n")
        proc = self.run_script(self.vert, "--caption", "x", "--platforms", "tiktok", "--dry-run", env_file=env)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertEqual(self.json_out(proc)["payload"]["platforms"][0]["accountId"], "9" * 24)


if __name__ == "__main__":
    unittest.main(verbosity=2)
