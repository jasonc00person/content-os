#!/usr/bin/env -S uv run --quiet --script
# /// script
# requires-python = ">=3.10"
# dependencies = ["obsws-python>=1.8"]
# ///
"""recording-studio CLI: the deterministic half of the OBS integration (see ../SKILL.md).

    studio.py status                    one-glance state of OBS, the mic and the take
    studio.py preflight [--fix]         the "are we good to record?" checklist
    studio.py mode horizontal|vertical  relaunch OBS in that profile + scene collection
    studio.py launch [mode] | quit      start OBS (current mode if none) / quit it safely
    studio.py rec start|stop|pause|resume
    studio.py mark [name]               chapter marker in the take (Hybrid MP4 only)
    studio.py scene [name]              list scenes / switch the program scene
    studio.py shot [--source S]         screenshot of the program output -> PNG path
    studio.py levels [--seconds N]      sample the mic meter while you talk
    studio.py sync [ms]                 read / set the mic's audio sync offset
    studio.py rate [--fix]              audio interface sample rate (must be 48 kHz)
    studio.py test [--seconds N]        short test take into $TMPDIR, then verify it
    studio.py verify [file] [--dupes]   check a finished take (default: the newest)
    studio.py clap [file]               clap-test contact sheets for measuring A/V sync
    studio.py stream status|start|stop
    studio.py call <Request> ['<json>']  raw obs-websocket v5 request (anything not wrapped above)
    studio.py setup                     turn on obs-websocket (OBS must be quit)
    studio.py mcp                       serve all of the above as MCP tools over stdio
"""
import argparse, base64, ctypes, json, logging, math, os, re, secrets, struct, subprocess, sys, time
from array import array
from pathlib import Path

HERE = Path(__file__).resolve().parent
RIG = json.loads((HERE.parent / "studio.json").read_text())
OBS_DIR = Path.home() / "Library/Application Support/obs-studio"
WS_CONF = OBS_DIR / "plugin_config/obs-websocket/config.json"
TMP = Path(os.environ.get("TMPDIR", "/tmp")) / "recording-studio"
FPS = RIG["fps"][0] / RIG["fps"][1]
logging.getLogger("obsws_python").setLevel(logging.CRITICAL)  # it logs every failed request as a traceback
os.environ["PATH"] = os.pathsep.join(["/opt/homebrew/bin", "/usr/local/bin", os.environ.get("PATH", "")])  # MCP hosts launch with a bare PATH; ffmpeg lives here


def die(msg, code=1):
    print(msg, file=sys.stderr)
    sys.exit(code)


def sh(cmd, timeout=60):
    try:
        return subprocess.run(cmd, capture_output=True, text=True, timeout=timeout).stdout
    except (OSError, subprocess.TimeoutExpired):
        return ""


# ── OBS process + log ────────────────────────────────────────────────────────

def obs_pid():
    out = sh(["pgrep", "-x", "OBS"]).split()
    return int(out[0]) if out else None


def newest_log():
    logs = sorted((OBS_DIR / "logs").glob("*.txt"), key=os.path.getmtime)
    return logs[-1] if logs else None


def busy():
    """Recording or streaming, per the current session's log (works with or without the websocket)."""
    if not obs_pid() or not newest_log():
        return None
    t = newest_log().read_text(errors="ignore")
    if t.count("==== Recording Start") > t.count("==== Recording Stop"):
        return "recording"
    if t.count("==== Streaming Start") > t.count("==== Streaming Stop"):
        return "streaming"
    return None


def mic_inits(log_text):
    """Every time the mic's interface (re)initialized this session: [(clock, rate)]."""
    pat = re.compile(r"^(\d\d:\d\d:\d\d)\.\d+: coreaudio: Device '" + re.escape(RIG["mic"]["interface"]) + r"' \[(\d+) Hz\] initialized", re.M)
    return [(m.group(1), int(m.group(2))) for m in pat.finditer(log_text)]


# ── websocket ────────────────────────────────────────────────────────────────

def ws_conf():
    return json.loads(WS_CONF.read_text()) if WS_CONF.exists() else {}


_CLIENT = {}  # pid -> ReqClient; the MCP server is long-lived and OBS relaunches get a new pid


def connect(timeout=3, quiet=False):
    import obsws_python as obs
    c = ws_conf()
    pid = obs_pid()
    if pid in _CLIENT:
        return _CLIENT[pid]
    if not pid:
        if quiet:
            return None
        die("OBS isn't running. Start it with: studio.py launch")
    if not c.get("server_enabled"):
        if quiet:
            return None
        die("obs-websocket is off. Quit OBS, then run: studio.py setup")
    try:
        for old in _CLIENT.values():
            try:
                old.disconnect()
            except Exception:
                pass
        _CLIENT.clear()
        _CLIENT[pid] = obs.ReqClient(host="localhost", port=c.get("server_port", 4455), password=c.get("server_password", ""), timeout=timeout)
        return _CLIENT[pid]
    except Exception as e:  # refused while OBS boots, auth failure, timeout
        if quiet:
            return None
        die(f"Can't reach obs-websocket on port {c.get('server_port', 4455)}: {e}. If OBS was started before the websocket was enabled, relaunch it.")


def req(cl, name, data=None):
    return cl.send(name, data, raw=True) or {}


def wait_ready(seconds=45):
    """OBS accepts the socket before the frontend is loaded; wait until a scene request answers."""
    end = time.time() + seconds
    while time.time() < end:
        cl = connect(timeout=2, quiet=True)
        if cl:
            try:
                req(cl, "GetCurrentProgramScene")
                return cl
            except Exception:
                pass
        time.sleep(0.5)
    die(f"OBS started but the websocket didn't answer within {seconds}s.")


def current_mode(cl):
    prof = req(cl, "GetProfileList")["currentProfileName"]
    coll = req(cl, "GetSceneCollectionList")["currentSceneCollectionName"]
    mode = next((k for k, m in RIG["modes"].items() if m["profile"] == prof), None)
    return mode, prof, coll


def profile_dir(name):
    for ini in (OBS_DIR / "basic/profiles").glob("*/basic.ini"):
        if re.search(r"^Name=" + re.escape(name) + r"$", ini.read_text(errors="ignore"), re.M):
            return ini.parent
    return None


# ── CoreAudio (sample rate of the mic interface) ─────────────────────────────

class _Addr(ctypes.Structure):
    _fields_ = [("sel", ctypes.c_uint32), ("scope", ctypes.c_uint32), ("elem", ctypes.c_uint32)]


_CA = ctypes.cdll.LoadLibrary("/System/Library/Frameworks/CoreAudio.framework/CoreAudio")
_CF = ctypes.cdll.LoadLibrary("/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation")
_CF.CFStringGetCString.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_long, ctypes.c_uint32]
_CF.CFRelease.argtypes = [ctypes.c_void_p]
_cc = lambda s: struct.unpack(">I", s.encode())[0]


def _ca_get(obj, sel, ctype, scope="glob"):
    a, size = _Addr(_cc(sel), _cc(scope), 0), ctypes.c_uint32(0)
    if _CA.AudioObjectGetPropertyDataSize(obj, ctypes.byref(a), 0, None, ctypes.byref(size)) or not size.value:
        return []
    buf = (ctype * (size.value // ctypes.sizeof(ctype)))()
    if _CA.AudioObjectGetPropertyData(obj, ctypes.byref(a), 0, None, ctypes.byref(size), buf):
        return []
    return list(buf)


def audio_devices():
    """[{id, name, rate, input, default_input}] for every CoreAudio device."""
    din = (_ca_get(1, "dIn ", ctypes.c_uint32) or [0])[0]
    out = []
    for d in _ca_get(1, "dev#", ctypes.c_uint32):
        ref = (_ca_get(d, "lnam", ctypes.c_void_p) or [None])[0]
        name = "?"
        if ref:
            b = ctypes.create_string_buffer(512)
            _CF.CFStringGetCString(ref, b, 512, 0x08000100)
            _CF.CFRelease(ref)
            name = b.value.decode()
        rate = (_ca_get(d, "nsrt", ctypes.c_double) or [0])[0]
        out.append({"id": d, "name": name, "rate": int(rate), "input": bool(_ca_get(d, "stm#", ctypes.c_uint32, "inpt")), "default_input": d == din})
    return out


def interface():
    return next((d for d in audio_devices() if d["name"] == RIG["mic"]["interface"] and d["input"]), None)


def set_rate(dev_id, hz):
    a, v = _Addr(_cc("nsrt"), _cc("glob"), 0), ctypes.c_double(hz)
    return _CA.AudioObjectSetPropertyData(dev_id, ctypes.byref(a), 0, None, 8, ctypes.byref(v))


# ── launch / quit / mode ─────────────────────────────────────────────────────

def quit_obs():
    if not obs_pid():
        return
    b = busy()
    if b:
        die(f"OBS is {b}. Stop it first; nothing was changed.")
    sh(["osascript", "-e", 'tell application "OBS" to quit'])  # prints "User canceled (-128)" every time, still quits
    for _ in range(60):
        if not obs_pid():
            return
        time.sleep(0.5)
    die("OBS didn't quit within 30s (a dialog is probably open in OBS).")


def launch(mode):
    m = RIG["modes"][mode]
    subprocess.run(["open", "-a", "OBS", "--args", "--profile", m["profile"], "--collection", m["collection"], "--disable-shutdown-check"], check=True)
    cl = wait_ready()
    _, prof, coll = current_mode(cl)
    if (prof, coll) != (m["profile"], m["collection"]):
        die(f"OBS came up on profile '{prof}' / collection '{coll}', expected '{m['profile']}'.")
    return cl


def relaunch(mode):
    quit_obs()
    launch(mode)


def cmd_mode(a):
    if obs_pid():
        cl = connect()
        mode, prof, coll = current_mode(cl)
        m = RIG["modes"][a.mode]
        if (prof, coll) == (m["profile"], m["collection"]):
            print(f"Already in {a.mode} ({prof}).")
            return
    relaunch(a.mode)
    w, h = RIG["modes"][a.mode]["canvas"]
    print(f"OBS relaunched in {a.mode}: profile + collection '{RIG['modes'][a.mode]['profile']}', canvas {w}x{h}.")


def cmd_launch(a):
    if obs_pid():
        if a.mode:
            return cmd_mode(a)
        print("OBS is already running.")
        return
    mode = a.mode
    if not mode:  # reopen whatever profile OBS last used, if it's one of ours
        ini = (OBS_DIR / "user.ini").read_text(errors="ignore") if (OBS_DIR / "user.ini").exists() else ""
        last = (re.search(r"^Profile=(.+)$", ini, re.M) or [None, ""])[1]
        mode = next((k for k, m in RIG["modes"].items() if m["profile"] == last), "horizontal")
    launch(mode)
    print(f"OBS is up in {mode} ({RIG['modes'][mode]['profile']}).")


def cmd_quit(a):
    quit_obs()
    print("OBS quit.")


def cmd_setup(a):
    if obs_pid():
        die("Quit OBS first (studio.py quit): it rewrites its plugin config on exit.")
    c = ws_conf()
    c.setdefault("server_port", 4455)
    c["server_enabled"] = True
    c["auth_required"] = True
    if not c.get("server_password"):
        c["server_password"] = secrets.token_urlsafe(16)
    c.setdefault("alerts_enabled", False)
    c.setdefault("first_load", False)
    WS_CONF.parent.mkdir(parents=True, exist_ok=True)
    WS_CONF.write_text(json.dumps(c, indent=4))
    print(f"obs-websocket enabled on port {c['server_port']} with auth (password stays in OBS's own config).")


# ── status ───────────────────────────────────────────────────────────────────

def cmd_status(a):
    iface = interface()
    rate = f"{iface['rate']} Hz" if iface else "not connected"
    if not obs_pid():
        print(f"OBS: not running | {RIG['mic']['interface']}: {rate}")
        return
    cl = connect()
    mode, prof, coll = current_mode(cl)
    scene = req(cl, "GetCurrentProgramScene")["currentProgramSceneName"]
    rec = req(cl, "GetRecordStatus")
    stream = req(cl, "GetStreamStatus")
    st = req(cl, "GetStats")
    sync = req(cl, "GetInputAudioSyncOffset", {"inputName": RIG["mic"]["source"]}).get("inputAudioSyncOffset")
    muted = req(cl, "GetInputMute", {"inputName": RIG["mic"]["source"]}).get("inputMuted")
    state = "RECORDING " + rec["outputTimecode"].split(".")[0] if rec["outputActive"] else "idle"
    if rec.get("outputPaused"):
        state = "PAUSED " + rec["outputTimecode"].split(".")[0]
    if stream.get("outputActive"):
        state += f" | LIVE {stream['outputTimecode'].split('.')[0]} (skipped {stream['outputSkippedFrames']})"
    hours = st["availableDiskSpace"] / 1024 / RIG["gb_per_hour"]
    print(f"OBS {state} | {mode or '?'} (profile '{prof}', collection '{coll}') | scene '{scene}'")
    print(f"mic '{RIG['mic']['source']}': {'MUTED' if muted else 'live'}, sync {sync} ms | {RIG['mic']['interface']}: {rate}")
    print(f"render skipped {st['renderSkippedFrames']}/{st['renderTotalFrames']}, output skipped {st['outputSkippedFrames']}/{st['outputTotalFrames']}, "
          f"fps {st['activeFps']:.2f}, CPU {st['cpuUsage']:.0f}% | disk {st['availableDiskSpace'] / 1024:.0f} GB free = {hours:.1f} h of 4K")


# ── preflight ────────────────────────────────────────────────────────────────

def screenshot(cl, source, fmt="png", width=None):
    data = {"sourceName": source, "imageFormat": fmt}
    if width:
        data["imageWidth"] = width
    uri = req(cl, "GetSourceScreenshot", data)["imageData"]
    return base64.b64decode(uri.split(",", 1)[1])


def mean_luma(bmp):
    """Average brightness (0-255) of an uncompressed 24/32-bit BMP."""
    off, bpp = struct.unpack_from("<I", bmp, 10)[0], struct.unpack_from("<H", bmp, 28)[0]
    px = bmp[off:]
    step = bpp // 8
    vals = [sum(px[i:i + 3]) / 3 for i in range(0, len(px) - 2, step)]
    return sum(vals) / max(1, len(vals))


def machine_checks(res, fix):
    therm = sh(["pmset", "-g", "therm"])
    res.append(("OK" if "No thermal warning" in therm or not therm.strip() else "WARN", "machine", "no thermal warnings" if "No thermal warning" in therm else therm.strip()[:120]))
    ps = sh(["pmset", "-g", "ps"])
    res.append(("OK" if "AC Power" in ps else "WARN", "machine", "on AC power" if "AC Power" in ps else "on battery: plug in before a long take"))
    free = re.search(r"free percentage: (\d+)%", sh(["memory_pressure"]))
    if free:
        res.append(("OK" if int(free.group(1)) >= 20 else "WARN", "machine", f"memory {free.group(1)}% free"))
    used = re.search(r"used = ([\d.]+)M", sh(["sysctl", "-n", "vm.swapusage"]))
    if used:
        gb = float(used.group(1)) / 1024
        res.append(("OK" if gb < 5 else "WARN", "machine", f"swap {gb:.1f} GB used" + ("" if gb < 5 else ": restart the Mac before a long take")))
    ws = re.search(r"^\s*([\d.]+)([MG])\+?\s+WindowServer", sh(["top", "-l", "1", "-o", "mem", "-stats", "mem,command", "-n", "30"]), re.M)
    if ws:
        gb = float(ws.group(1)) / (1 if ws.group(2) == "G" else 1024)
        res.append(("OK" if gb < 2.5 else "WARN", "machine", f"WindowServer {gb:.1f} GB" + ("" if gb < 2.5 else ": leaking, restart before a long take")))
    running = set(sh(["ps", "-Aceo", "comm"]).split("\n"))
    for app in RIG["quit_before_recording"]:
        if app in running:
            if fix and not busy():
                sh(["osascript", "-e", f'quit app "{app}"'])
                res.append(("FIXED", "apps", f"quit {app}"))
            else:
                res.append(("WARN", "apps", f"{app} is running (quits with --fix)"))
    for app in RIG["warn_if_running"]:
        if app in running:
            res.append(("WARN", "apps", f"{app} is open: don't let it record or export during the take"))


def fix_rate(iface):
    """Set the interface to the studio rate. Changing it under a running OBS kills OBS's mic (-10863),
    so OBS is quit first. Returns (rate now, mode to relaunch OBS in or None)."""
    mode = None
    if obs_pid():
        mode = current_mode(connect())[0] or "horizontal"
        quit_obs()  # refuses while recording/streaming
    set_rate(iface["id"], RIG["mic"]["sample_rate"])
    time.sleep(2)  # the first readback lags
    return interface()["rate"], mode


def preflight(fix):
    """Returns (results, relaunch_needed). results = [(level, area, message)]."""
    res, need_relaunch = [], None
    iface = interface()
    mic = RIG["mic"]
    if not iface:
        res.append(("FAIL", "mic", f"{mic['interface']} not connected: check its USB cable"))
    else:
        if not iface["default_input"]:
            res.append(("WARN", "mic", f"{mic['interface']} is not the macOS default input"))
        if iface["rate"] != mic["sample_rate"]:
            if fix and busy() is None:
                now, need_relaunch = fix_rate(iface)
                res.append(("FIXED" if now == mic["sample_rate"] else "FAIL", "mic", f"{mic['interface']} {iface['rate']} -> {now} Hz"))
                premiere = "Adobe Premiere Pro" in sh(["ps", "-Aceo", "comm"])
                if premiere:
                    res.append(("WARN", "mic", "Premiere is open: with Bluetooth output it drags the Volt back to 44.1k unless its Audio Hardware Default Input is 'No Input'"))
            else:
                res.append(("FAIL", "mic", f"{mic['interface']} at {iface['rate']} Hz, needs {mic['sample_rate']} (fix: --fix)"))
        else:
            res.append(("OK", "mic", f"{mic['interface']} at {iface['rate']} Hz"))

    machine_checks(res, fix)

    if not obs_pid():
        if fix and need_relaunch is None:
            need_relaunch = "horizontal"
        res.append(("WARN", "obs", "OBS isn't running" + (" (launching)" if fix else ": studio.py launch")))
        return res, need_relaunch
    b = busy()
    if b:
        res.append(("WARN", "obs", f"OBS is {b} right now: fixes that need a restart are skipped"))
    if need_relaunch:  # OBS was quit above for the rate fix; the rest is checked after the relaunch
        return res, need_relaunch

    cl = connect()
    mode, prof, coll = current_mode(cl)
    if not mode:
        res.append(("FAIL", "obs", f"profile '{prof}' isn't one of the studio modes ({', '.join(m['profile'] for m in RIG['modes'].values())})"))
    elif coll != RIG["modes"][mode]["collection"]:
        res.append(("FAIL", "obs", f"profile '{prof}' is paired with collection '{coll}' (canvas and scenes won't match)"))
        need_relaunch = mode if fix and not b else None
    else:
        res.append(("OK", "obs", f"{mode}: profile + collection '{prof}'"))

    inits = mic_inits(newest_log().read_text(errors="ignore"))
    if inits and inits[-1][1] != mic["sample_rate"]:
        res.append(("FAIL", "mic", f"OBS opened {mic['interface']} at {inits[-1][1]} Hz: relaunch OBS"))
        need_relaunch = need_relaunch or (mode if fix and not b else None)
    if len(inits) > 1:
        res.append(("FAIL", "sync", f"{mic['interface']} re-initialized mid-session at {inits[-1][0]}: audio shifts about 160 ms. Relaunch OBS, never retune the offset"))
        need_relaunch = need_relaunch or (mode if fix and not b else None)

    names = {i["inputName"]: i for i in req(cl, "GetInputList")["inputs"]}
    if mic["source"] in names:
        if req(cl, "GetInputMute", {"inputName": mic["source"]})["inputMuted"]:
            if fix:
                req(cl, "SetInputMute", {"inputName": mic["source"], "inputMuted": False})
                res.append(("FIXED", "mic", f"unmuted '{mic['source']}'"))
            else:
                res.append(("FAIL", "mic", f"'{mic['source']}' is MUTED in OBS"))
        sync = req(cl, "GetInputAudioSyncOffset", {"inputName": mic["source"]})["inputAudioSyncOffset"]
        res.append(("OK" if sync == mic["sync_ms"] else "WARN", "sync", f"mic offset {sync} ms" + ("" if sync == mic["sync_ms"] else f", clap-tested value is {mic['sync_ms']} (studio.py sync {mic['sync_ms']})")))
    else:
        res.append(("FAIL", "mic", f"no '{mic['source']}' audio source in OBS"))

    cam = RIG["camera"]
    vs = req(cl, "GetVideoSettings")
    if cam["source"] not in names:
        res.append(("FAIL", "camera", f"no '{cam['source']}' source in collection '{coll}'"))
    else:
        kind = names[cam["source"]]["unversionedInputKind"]
        s = req(cl, "GetInputSettings", {"inputName": cam["source"]})["inputSettings"]
        if kind != cam["kind"] or not s.get("buffering"):
            res.append(("FAIL", "camera", f"source is '{kind}' buffering={s.get('buffering')}: must be {cam['kind']} with buffering on, or frames duplicate"))
        cams = json.loads(sh(["system_profiler", "SPCameraDataType", "-json"]) or "{}").get("SPCameraDataType", [])
        live = next((c["spcamera_unique-id"] for c in cams if c.get("_name") == cam["device_name"]), None)
        if not live:
            res.append(("FAIL", "camera", f"{cam['device_name']} not detected: check its USB cable"))
        elif s.get("device") != live:
            if fix:
                req(cl, "SetInputSettings", {"inputName": cam["source"], "inputSettings": {"device": live, "device_name": cam["device_name"]}})
                res.append(("FIXED", "camera", f"re-pointed the source at {cam['device_name']} (its ID changed {s.get('device')} -> {live})"))
            else:
                res.append(("FAIL", "camera", f"source points at old device ID {s.get('device')}, {cam['device_name']} is now {live}: black preview (fix: --fix)"))
        fr = s.get("frame_rate") or {}
        if fr and abs(fr.get("numerator", 0) / max(1, fr.get("denominator", 1)) - vs["fpsNumerator"] / vs["fpsDenominator"]) > 0.01:
            res.append(("FAIL", "camera", f"source fps {fr} != canvas {vs['fpsNumerator']}/{vs['fpsDenominator']}: judder"))
        try:
            luma = mean_luma(screenshot(cl, cam["source"], "bmp", 64))
            res.append(("OK" if luma > 6 else "FAIL", "camera", f"feed live (brightness {luma:.0f}/255)" if luma > 6 else "feed is BLACK: camera off, lens cap, HDMI out, or wrong device"))
        except Exception as e:
            res.append(("WARN", "camera", f"couldn't grab a frame: {e}"))

    if mode:
        want_w, want_h = RIG["modes"][mode]["canvas"]
        ok = (vs["baseWidth"], vs["baseHeight"], vs["outputWidth"], vs["outputHeight"]) == (want_w, want_h, want_w, want_h)
        ok_fps = (vs["fpsNumerator"], vs["fpsDenominator"]) == tuple(RIG["fps"])
        res.append(("OK" if ok and ok_fps else "FAIL", "video", f"canvas {vs['baseWidth']}x{vs['baseHeight']} -> {vs['outputWidth']}x{vs['outputHeight']} @ {vs['fpsNumerator']}/{vs['fpsDenominator']}"))
    bad = []
    for key, want in RIG["output"].items():
        cat, name = key.split("/")
        got = req(cl, "GetProfileParameter", {"parameterCategory": cat, "parameterName": name}).get("parameterValue")
        if str(got) != want:
            bad.append(f"{key}={got} (want {want})")
    pdir = profile_dir(prof)
    enc = json.loads((pdir / "recordEncoder.json").read_text()) if pdir and (pdir / "recordEncoder.json").exists() else {}
    if enc.get("bitrate") != RIG["record_bitrate_kbps"]:
        bad.append(f"record bitrate {enc.get('bitrate')} kbps (want {RIG['record_bitrate_kbps']})")
    res.append(("FAIL" if bad else "OK", "output", "; ".join(bad) if bad else f"HEVC {RIG['record_bitrate_kbps'] // 1000} Mbps, Hybrid MP4, 1 audio track, no splits"))

    st = req(cl, "GetStats")
    hours = st["availableDiskSpace"] / 1024 / RIG["gb_per_hour"]
    rdir = req(cl, "GetRecordDirectory")["recordDirectory"]
    res.append(("FAIL" if hours < 1 else "WARN" if hours < 3 else "OK", "disk", f"{st['availableDiskSpace'] / 1024:.0f} GB free = {hours:.1f} h of 4K, takes land in {rdir}"))
    if st["renderSkippedFrames"] or st["outputSkippedFrames"]:
        res.append(("WARN", "obs", f"this session skipped frames: render {st['renderSkippedFrames']}, output {st['outputSkippedFrames']}"))
    return res, need_relaunch


def cmd_preflight(a):
    res, need = preflight(a.fix)
    fixed = [r for r in res if r[0] == "FIXED"]
    if need and a.fix:
        relaunch(need) if obs_pid() else launch(need)
        fixed.append(("FIXED", "obs", f"relaunched OBS in {need}"))
        res, _ = preflight(False)
    fails = [r for r in res if r[0] == "FAIL"]
    warns = [r for r in res if r[0] == "WARN"]
    verdict = "NO-GO" if fails else "GO" if not warns else "GO (with notes)"
    print(f"{verdict}: {len(fails)} blocker(s), {len(warns)} note(s)" + (f", {len(fixed)} fixed" if fixed else ""))
    for lvl, area, msg in fixed + fails + warns + [r for r in res if r[0] == "OK"]:
        print(f"  {lvl:5} {area:7} {msg}")
    sys.exit(1 if fails else 0)


# ── recording ────────────────────────────────────────────────────────────────

def stop_record(cl):
    """StopRecord returns before the muxer finishes; wait until the output is really down (else Set* requests fail with 500)."""
    path = req(cl, "StopRecord").get("outputPath")
    for _ in range(60):
        if not req(cl, "GetRecordStatus")["outputActive"]:
            break
        time.sleep(0.5)
    return path


def cmd_rec(a):
    cl = connect()
    if a.action == "start":
        if req(cl, "GetRecordStatus")["outputActive"]:
            die("Already recording.")
        req(cl, "StartRecord")
        mode = current_mode(cl)[0]
        print(f"Recording ({mode}).")
    elif a.action == "stop":
        path = stop_record(cl)
        print(f"Stopped: {path}")
        if path and not a.no_verify:
            verify(Path(path), dupes=False)
    elif a.action == "pause":
        req(cl, "PauseRecord"); print("Paused.")
    elif a.action == "resume":
        req(cl, "ResumeRecord"); print("Recording again.")


def cmd_mark(a):
    cl = connect()
    if not req(cl, "GetRecordStatus")["outputActive"]:
        die("Not recording: nothing to mark.")
    tc = req(cl, "GetRecordStatus")["outputTimecode"].split(".")[0]
    req(cl, "CreateRecordChapter", {"chapterName": a.name} if a.name else None)
    print(f"Marked '{a.name or 'chapter'}' at {tc}.")


def cmd_scene(a):
    cl = connect()
    if a.name:
        req(cl, "SetCurrentProgramScene", {"sceneName": a.name})
        print(f"Program scene: {a.name}")
        return
    cur = req(cl, "GetCurrentProgramScene")["currentProgramSceneName"]
    for s in reversed(req(cl, "GetSceneList")["scenes"]):
        print(("* " if s["sceneName"] == cur else "  ") + s["sceneName"])


def cmd_shot(a):
    cl = connect()
    src = a.source or req(cl, "GetCurrentProgramScene")["currentProgramSceneName"]
    vs = req(cl, "GetVideoSettings")
    width = a.width if vs["baseWidth"] >= vs["baseHeight"] else round(a.width * vs["baseWidth"] / vs["baseHeight"])
    TMP.mkdir(parents=True, exist_ok=True)
    out = Path(a.out) if a.out else TMP / f"shot-{time.strftime('%H%M%S')}.jpg"
    out.write_bytes(screenshot(cl, src, out.suffix.lstrip(".").lower() or "jpg", width))
    print(out)
    return out


def cmd_levels(a):
    import obsws_python as obs
    connect()  # fail fast with a clear message
    c, name, peaks = ws_conf(), RIG["mic"]["source"], []

    def on_input_volume_meters(data):
        for i in data.inputs:
            if i.get("inputName") == name and i.get("inputLevelsMul"):
                peaks.append(max(ch[1] for ch in i["inputLevelsMul"]))

    ev = obs.EventClient(host="localhost", port=c.get("server_port", 4455), password=c.get("server_password", ""), subs=obs.Subs.INPUTVOLUMEMETERS)
    ev.callback.register(on_input_volume_meters)
    time.sleep(a.seconds)
    ev.disconnect()
    if not peaks:
        die(f"No meter data for '{name}'.")
    db = sorted(20 * math.log10(p) if p > 0 else -100 for p in peaks)
    top, speech = db[-1], db[int(len(db) * 0.9)]
    active = sum(d > -45 for d in db) / len(db)
    if active < 0.05:
        verdict = "no voice picked up: talk during the sample, or check the mic cable / mute"
    elif top < -18:
        verdict = "too quiet: one notch more gain on the Volt"
    elif top > -3:
        verdict = "hot: back the Volt gain off a notch"
    else:
        verdict = "good"
    print(f"{verdict} | peak {top:.1f} dBFS, loud speech {speech:.1f} dBFS, voice {active:.0%} of {a.seconds}s (target peaks -12 to -6)")


def cmd_sync(a):
    cl = connect()
    name = RIG["mic"]["source"]
    if a.ms is not None:
        req(cl, "SetInputAudioSyncOffset", {"inputName": name, "inputAudioSyncOffset": a.ms})
    print(f"'{name}' sync offset: {req(cl, 'GetInputAudioSyncOffset', {'inputName': name})['inputAudioSyncOffset']} ms")


def cmd_rate(a):
    iface = interface()
    if not iface:
        die(f"{RIG['mic']['interface']} not connected.")
    if a.fix and iface["rate"] != RIG["mic"]["sample_rate"]:
        _, mode = fix_rate(iface)
        if mode:
            launch(mode)
            print(f"OBS relaunched in {mode} so it opens the interface at the new rate.")
        iface = interface()
    print(f"{iface['name']}: {iface['rate']} Hz" + ("" if iface["rate"] == RIG["mic"]["sample_rate"] else f" (needs {RIG['mic']['sample_rate']}: studio.py rate --fix)"))
    other = [f"{d['name']} {d['rate']}" for d in audio_devices() if d["input"] and d["name"] != iface["name"]]
    print("other inputs: " + ", ".join(other))


def cmd_test(a):
    cl = connect()
    if req(cl, "GetRecordStatus")["outputActive"]:
        die("Already recording.")
    old = req(cl, "GetRecordDirectory")["recordDirectory"]
    tdir = TMP / "test-takes"
    tdir.mkdir(parents=True, exist_ok=True)
    path = None
    try:
        req(cl, "SetRecordDirectory", {"recordDirectory": str(tdir)})
        req(cl, "StartRecord")
        time.sleep(a.seconds)
        path = stop_record(cl)
    finally:
        if req(cl, "GetRecordStatus")["outputActive"]:
            stop_record(cl)
        req(cl, "SetRecordDirectory", {"recordDirectory": old})
    print(f"Test take: {path} (record folder restored to {old})")
    verify(Path(path), dupes=False)


# ── verify a take ────────────────────────────────────────────────────────────

def take_log(path):
    """The log text between this take's 'Writing ... file' line and its Recording Stop, plus the session's mic inits before it."""
    for log in sorted((OBS_DIR / "logs").glob("*.txt"), key=os.path.getmtime, reverse=True)[:5]:
        t = log.read_text(errors="ignore")
        i = t.find(f"file '{path}'")
        if i >= 0:
            j = t.find("==== Recording Stop", i)
            return t[i: j if j > 0 else len(t)], mic_inits(t[:j if j > 0 else len(t)])
    return "", []


def latest_take():
    for log in sorted((OBS_DIR / "logs").glob("*.txt"), key=os.path.getmtime, reverse=True):
        m = re.findall(r"Writing .*? file '(.+?)'", log.read_text(errors="ignore"))
        for p in reversed(m):
            if Path(p).exists():
                return Path(p)
    die("No OBS take found in the recent logs.")


def dupe_rate(path, start, secs):
    tmp = TMP / "yavg.txt"
    TMP.mkdir(parents=True, exist_ok=True)
    subprocess.run(["ffmpeg", "-v", "error", "-hwaccel", "videotoolbox", "-ss", str(start), "-t", str(secs), "-i", str(path), "-an",
                    "-vf", f"scale=480:-2,tblend=all_mode=difference,signalstats,metadata=print:key=lavfi.signalstats.YAVG:file={tmp}", "-f", "null", "-"], check=True)
    v = [float(x) for x in re.findall(r"YAVG=([\d.]+)", tmp.read_text())]
    elig = dup = 0
    for i in range(1, len(v) - 1):
        lo = min(v[i - 1], v[i + 1])
        if lo > 0.4 and v[i - 1] < 5 and v[i + 1] < 5:
            elig += 1
            dup += v[i] < 0.25 * lo
    return elig, dup


def verify(path, dupes):
    if not path.exists():
        die(f"No such file: {path}")
    pr = json.loads(sh(["ffprobe", "-v", "error", "-show_entries", "format=duration,bit_rate,size:stream=codec_type,codec_name,width,height,avg_frame_rate,nb_frames,sample_rate,channels", "-of", "json", str(path)]) or "{}")
    vids = [s for s in pr.get("streams", []) if s["codec_type"] == "video"]
    auds = [s for s in pr.get("streams", []) if s["codec_type"] == "audio"]
    fmt = pr.get("format", {})
    res = []
    if not vids:
        die(f"{path.name}: no video stream (file still being written, or corrupt).")
    v = vids[0]
    dur = float(fmt.get("duration", 0))
    num, den = (int(x) for x in v["avg_frame_rate"].split("/"))
    fps = num / den if den else 0
    canvases = {tuple(m["canvas"]): k for k, m in RIG["modes"].items()}
    mode = canvases.get((v["width"], v["height"]))
    res.append(("OK" if mode else "WARN", "video", f"{v['codec_name']} {v['width']}x{v['height']} ({mode or 'not a studio canvas'}) @ {fps:.3f} fps, {int(fmt.get('bit_rate', 0)) / 1e6:.1f} Mbps"))
    if abs(fps - FPS) > 0.01:
        res.append(("FAIL", "video", f"{fps:.3f} fps, studio runs {FPS:.3f}"))
    if v.get("nb_frames") and dur:
        exp = dur * fps
        off = int(v["nb_frames"]) - exp
        res.append(("OK" if abs(off) <= max(3, exp * 0.002) else "WARN", "frames", f"{v['nb_frames']} frames for {dur:.1f}s (expected {exp:.0f})"))
    if len(auds) != 1:
        res.append(("FAIL", "audio", f"{len(auds)} audio tracks: Premiere silently refuses twin tracks (remux: ffmpeg -i in -map 0:v:0 -map 0:a:0 -c copy out.mp4)"))
    if auds:
        a0 = auds[0]
        res.append(("OK" if a0.get("sample_rate") == "48000" else "FAIL", "audio", f"{a0['codec_name']} {a0.get('sample_rate')} Hz {a0.get('channels')}ch"))
        vd = subprocess.run(["ffmpeg", "-nostats", "-vn", "-i", str(path), "-af", "volumedetect", "-f", "null", "-"], capture_output=True, text=True).stderr
        mx = re.search(r"max_volume: ([-\d.]+) dB", vd)
        mean = re.search(r"mean_volume: ([-\d.]+) dB", vd)
        if mx:
            peak = float(mx.group(1))
            lvl = "WARN" if peak < -18 or peak > -0.5 else "OK"
            note = (": near-silent, nobody talked or the mic isn't feeding OBS" if peak < -35 else ": quiet, add Volt gain next time" if peak < -18
                    else ": touching 0 dB, back the gain off" if peak > -0.5 else "")
            res.append((lvl, "audio", f"peak {peak} dB, mean {mean.group(1) if mean else '?'} dB{note}"))
    seg, inits = take_log(str(path))
    if seg:
        for line in re.findall(r"^.*(?:skipped frames|lagged frames).*$", seg, re.M):
            n = re.search(r": (\d+)", line)
            if n and int(n.group(1)) > 0:
                res.append(("WARN", "log", line.split(": ", 1)[-1].strip()))
        if len(inits) > 1:
            res.append(("FAIL", "sync", f"{RIG['mic']['interface']} re-initialized at {inits[-1][0]} before/during this take: audio likely about 160 ms off. Clap-test it (studio.py clap) or reshoot after relaunching OBS"))
        elif inits:
            res.append(("OK", "sync", f"no mid-session mic re-init (opened at {inits[0][1]} Hz)"))
    chapters = json.loads(sh(["ffprobe", "-v", "error", "-show_chapters", "-of", "json", str(path)]) or "{}").get("chapters", [])
    if len(chapters) > 1:  # OBS always writes a "Start" chapter; more means marks were dropped
        res.append(("OK", "marks", ", ".join(f"{c.get('tags', {}).get('title', '?')} @ {time.strftime('%M:%S', time.gmtime(float(c['start_time'])))}" for c in chapters[1:])))
    if dupes and dur > 5:
        start = dur * 0.25 if dur > 90 else 0
        elig, dup = dupe_rate(path, start, min(60, dur - start))
        if elig:
            res.append(("OK" if dup == 0 else "WARN", "frames", f"{dup} duplicated of {elig} moving frames ({100 * dup / elig:.2f}%)" + ("" if dup == 0 else ": capture source clock drift, check buffering")))
        else:
            res.append(("WARN", "frames", "not enough motion to test for duplicate frames"))
    fails = [r for r in res if r[0] == "FAIL"]
    size = int(fmt.get("size", 0)) / 1e9
    print(f"{'BAD TAKE' if fails else 'CLEAN'}: {path.name}, {time.strftime('%M:%S', time.gmtime(dur)) if dur < 3600 else f'{dur / 3600:.2f} h'}, {size:.2f} GB")
    for lvl, area, msg in sorted(res, key=lambda r: ["FAIL", "WARN", "OK"].index(r[0])):
        print(f"  {lvl:4} {area:6} {msg}")
    return not fails


def cmd_verify(a):
    ok = verify(Path(a.file).expanduser() if a.file else latest_take(), a.dupes)
    sys.exit(0 if ok else 1)


# ── clap test ────────────────────────────────────────────────────────────────

def cmd_clap(a):
    path = Path(a.file).expanduser() if a.file else latest_take()
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(path), "-t", str(a.max_seconds), "-ac", "1", "-ar", "48000", "-f", "f32le", "-"], capture_output=True).stdout
    s = array("f")
    s.frombytes(raw[: len(raw) // 4 * 4])
    env = [max(abs(x) for x in s[i:i + 48]) for i in range(0, len(s) - 48, 48)]  # 1 ms peak envelope
    onsets, last = [], -1000
    for i in range(300, len(env)):
        base = sorted(env[i - 300:i])[150] + 1e-6  # median of the previous 300 ms
        if env[i] > 0.1 and 20 * math.log10(env[i] / base) > 20 and i - last > 300:
            onsets.append((i / 1000, 20 * math.log10(max(env[i:i + 30]))))  # (time, peak dBFS)
            last = i
    if not onsets:
        die("No clap found: clap sharply, 3 times, a second apart, hands in frame.")
    # A clap clips or nearly does; speech plosives also trip the detector but peak 10+ dB under it (10-14).
    loud = max(p for _, p in onsets)
    claps = [t for t, p in onsets if p >= loud - 6][:8]
    speech = [f"{t:.3f}s ({p:.0f} dB)" for t, p in onsets if p < loud - 6]
    w, h = (int(x) for x in sh(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height", "-of", "csv=p=0", str(path)]).strip().split(",")[:2])
    crop = "crop=iw*2/3:ih*3/4:iw/6:ih/4," if w > h else ""  # landscape: the centre two-thirds, chest up, so contact reads at thumbnail size
    out = TMP / f"clap-{path.stem.replace(' ', '_')}"
    out.mkdir(parents=True, exist_ok=True)
    print(f"{len(claps)} clap(s) in {path.name}" + (f", skipped {len(speech)} quieter onset(s) as speech: {', '.join(speech)}" if speech else "") + ".")
    print("Open each sheet, find the first frame where the hands touch.")
    print("offset = frame time - audio onset. Positive = audio is EARLY: add that many ms to the sync offset.")
    for n, t in enumerate(claps, 1):
        start = max(0, t - 0.25)
        probe = sh(["ffprobe", "-v", "error", "-read_intervals", f"{max(0, start - 3)}%{start + 1.0}", "-select_streams", "v:0", "-show_entries", "frame=pts_time", "-of", "csv=p=0", str(path)])
        times = [float(line.split(",")[0]) for line in probe.split() if line.split(",")[0]]
        times = [x for x in times if start <= x < start + 0.5][:12]
        sheet = out / f"clap{n}.png"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(start), "-i", str(path), "-frames:v", "1", "-an",
                        "-vf", f"select='gte(t\\,0)',{crop}scale=480:-2,tile=6x2", str(sheet)], check=True)
        print(f"clap {n}: audio onset {t:.3f}s | {sheet} | frames left-to-right, top row first: " + " ".join(f"{x:.3f}" for x in times))


# ── streaming ────────────────────────────────────────────────────────────────

def cmd_stream(a):
    cl = connect()
    if a.action == "start":
        req(cl, "StartStream"); time.sleep(3)
    elif a.action == "stop":
        req(cl, "StopStream"); time.sleep(1)
    s = req(cl, "GetStreamStatus")
    if not s.get("outputActive"):
        print("Not streaming.")
        return
    print(f"LIVE {s['outputTimecode'].split('.')[0]} | skipped {s['outputSkippedFrames']}/{s['outputTotalFrames']} | congestion {s.get('outputCongestion', 0):.2f} | reconnecting {s['outputReconnecting']}")


# ── raw passthrough ──────────────────────────────────────────────────────────

BLOCKED = {  # requests that crash OBS 32 or bypass the studio's guards
    "SetCurrentSceneCollection": "switching collections live can crash OBS 32 (obs-websocket 1351): use `mode`",
    "SetCurrentProfile": "profile and collection are a pair: use `mode`",
    "CreateProfile": "profiles are managed by hand, see reference/rig.md",
    "RemoveProfile": "profiles are managed by hand, see reference/rig.md",
}


def cmd_call(a):
    if a.request in BLOCKED:
        die(f"{a.request} is blocked: {BLOCKED[a.request]}.")
    cl = connect()
    data = json.loads(a.data) if isinstance(a.data, str) else a.data
    out = req(cl, a.request, data or None)
    print(json.dumps(out, indent=1)[:20000] if out else "ok")


# ── MCP server (same functions, stdio transport) ─────────────────────────────

def _S(**props):
    return {"type": "object", "properties": props, "additionalProperties": False}


MODES = {"type": "string", "enum": list(RIG["modes"])}
TOOLS = {
    "obs_status": (cmd_status, "One-glance studio state: recording/live + timecode, mode, program scene, mic mute + sync offset, interface sample rate, skipped frames, disk hours. Call it when asked; never poll it in a loop (GetStats leaks memory in OBS 32 on macOS).", _S()),
    "obs_preflight": (cmd_preflight, "The 'are we good to record?' checklist: mic interface at 48 kHz, no mid-session mic re-init, mic unmuted + clap-tested sync, camera present/right device/not black/fps-matched/buffered, canvas + output settings, disk hours, thermal/power/memory/swap/WindowServer, competing apps. Verdict first. fix=true applies the safe fixes (quit Loom/Spotify, set 48 kHz with OBS quit, re-point a moved camera, unmute, relaunch OBS) and never touches a live recording.", _S(fix={"type": "boolean"})),
    "obs_mode": (cmd_mode, "Switch the studio to horizontal (long-form, 3840x2160) or vertical (short-form, 2160x3840) by relaunching OBS with the matching profile + scene collection. Refuses while recording or streaming.", _S(mode=MODES)),
    "obs_launch": (cmd_launch, "Start OBS (in the given mode, else the last-used one) and wait until its websocket answers.", _S(mode=MODES)),
    "obs_quit": (cmd_quit, "Quit OBS. Refuses while recording or streaming.", _S()),
    "obs_record": (cmd_rec, "start / stop / pause / resume the recording. stop returns the file path and verifies the take unless no_verify.", _S(action={"type": "string", "enum": ["start", "stop", "pause", "resume"]}, no_verify={"type": "boolean"})),
    "obs_mark": (cmd_mark, "Drop a named chapter marker into the take being recorded (e.g. 'beat 3', 'redo', 'good take'). Shows up in the file's chapters and in obs_verify.", _S(name={"type": "string"})),
    "obs_scene": (cmd_scene, "List scenes, or switch the program scene when name is given.", _S(name={"type": "string"})),
    "obs_screenshot": (None, "Look at what OBS is recording right now (program output, or one source): framing, focus, lighting, headroom, a black camera. Returns the image.", _S(source={"type": "string"}, width={"type": "integer"})),
    "obs_levels": (cmd_levels, "Sample the mic meter for N seconds (default 6) while Jason talks at recording volume; verdict on gain (target peaks -12 to -6 dBFS).", _S(seconds={"type": "integer"})),
    "obs_sync": (cmd_sync, "Read the mic's audio sync offset, or set it (ms). Only change it from a clap test on a fresh OBS launch; after a mid-session interface re-init, relaunch instead.", _S(ms={"type": "integer"})),
    "obs_rate": (cmd_rate, "Sample rate of the mic interface and other inputs. fix=true sets it to 48 kHz (quits and relaunches OBS if it is open).", _S(fix={"type": "boolean"})),
    "obs_test_take": (cmd_test, "Record a short test take (default 10 s) into a temp folder (the real record folder is restored), then verify it.", _S(seconds={"type": "integer"})),
    "obs_verify": (cmd_verify, "Check a finished take (default: the newest): codec/canvas/fps, frame count vs duration, one 48 kHz audio track, audio peak, skipped/lagged frames and mic re-inits from the OBS log, chapter marks. dupes=true also scans 60 s for duplicated frames (slower).", _S(file={"type": "string"}, dupes={"type": "boolean"})),
    "obs_clap": (cmd_clap, "Clap test for A/V sync: finds clap onsets in a take (default: the newest), skips quieter speech onsets, and writes a 12-frame contact sheet per clap (up to 8) with each frame's timestamp. Read the sheets, find the frame where the hands first meet, offset = frame time - onset.", _S(file={"type": "string"}, max_seconds={"type": "integer"})),
    "obs_stream": (cmd_stream, "Streaming status, or start/stop. Only start on Jason's explicit go: it publishes live.", _S(action={"type": "string", "enum": ["status", "start", "stop"]})),
    "obs_call": (cmd_call, "Raw obs-websocket v5 request for anything the other tools don't cover (sources, transforms, filters, transitions, virtual cam, replay buffer...). request = requestType, data = requestData. Spec: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md", {"type": "object", "properties": {"request": {"type": "string"}, "data": {"type": "object"}}, "required": ["request"]}),
}
DEFAULTS = {"fix": False, "mode": None, "action": "status", "no_verify": False, "name": None, "source": None, "width": 1280, "out": None,
            "seconds": None, "ms": None, "file": None, "dupes": False, "max_seconds": 60, "request": None, "data": None}


def run_tool(name, args):
    import contextlib, io
    fn = TOOLS[name][0]
    ns = argparse.Namespace(**{**DEFAULTS, **args})
    if ns.seconds is None:
        ns.seconds = 10 if name == "obs_test_take" else 6
    buf, code, shot = io.StringIO(), 0, None
    with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(buf):
        try:
            if name == "obs_screenshot":
                shot = cmd_shot(ns)
            else:
                fn(ns)
        except SystemExit as e:
            code = e.code if isinstance(e.code, int) else 1
        except Exception as e:
            print(f"{type(e).__name__}: {e}")
            code = 1
    text = buf.getvalue().strip() or "ok"
    content = [{"type": "text", "text": text}]
    if shot:
        content.insert(0, {"type": "image", "data": base64.b64encode(Path(shot).read_bytes()).decode(), "mimeType": "image/jpeg"})
    # preflight/verify exit 1 on NO-GO / BAD TAKE: that's a verdict, not a tool error
    return {"content": content, "isError": bool(code) and name not in ("obs_preflight", "obs_verify")}


def cmd_mcp(a):
    proto = os.fdopen(os.dup(1), "w")
    os.dup2(2, 1)  # stray writes from subprocesses / C libs must never corrupt the protocol stream

    def send(msg):
        proto.write(json.dumps(msg) + "\n")
        proto.flush()

    for line in sys.stdin:
        try:
            msg = json.loads(line)
        except ValueError:
            continue
        mid, method, params = msg.get("id"), msg.get("method"), msg.get("params") or {}
        if mid is None:
            continue  # notifications
        if method == "initialize":
            result = {"protocolVersion": params.get("protocolVersion", "2025-06-18"), "capabilities": {"tools": {}},
                      "serverInfo": {"name": "obs-studio", "version": "1.0.0"},
                      "instructions": "Jason's OBS recording studio. Before a take: obs_preflight (fix=true). Mode = horizontal for long-form, vertical for short-form. After a take: obs_verify. Full workflow: the recording-studio skill in ~/Projects/content-os."}
        elif method == "tools/list":
            result = {"tools": [{"name": n, "description": d, "inputSchema": s} for n, (_, d, s) in TOOLS.items()]}
        elif method == "tools/call":
            if params.get("name") not in TOOLS:
                send({"jsonrpc": "2.0", "id": mid, "error": {"code": -32602, "message": f"unknown tool {params.get('name')}"}})
                continue
            result = run_tool(params["name"], params.get("arguments") or {})
        elif method == "ping":
            result = {}
        else:
            send({"jsonrpc": "2.0", "id": mid, "error": {"code": -32601, "message": f"method not found: {method}"}})
            continue
        send({"jsonrpc": "2.0", "id": mid, "result": result})


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("status").set_defaults(fn=cmd_status)
    x = sub.add_parser("preflight"); x.add_argument("--fix", action="store_true"); x.set_defaults(fn=cmd_preflight)
    x = sub.add_parser("mode"); x.add_argument("mode", choices=RIG["modes"]); x.set_defaults(fn=cmd_mode)
    x = sub.add_parser("launch"); x.add_argument("mode", nargs="?", choices=RIG["modes"]); x.set_defaults(fn=cmd_launch)
    sub.add_parser("quit").set_defaults(fn=cmd_quit)
    sub.add_parser("setup").set_defaults(fn=cmd_setup)
    x = sub.add_parser("rec"); x.add_argument("action", choices=["start", "stop", "pause", "resume"]); x.add_argument("--no-verify", action="store_true"); x.set_defaults(fn=cmd_rec)
    x = sub.add_parser("mark"); x.add_argument("name", nargs="?"); x.set_defaults(fn=cmd_mark)
    x = sub.add_parser("scene"); x.add_argument("name", nargs="?"); x.set_defaults(fn=cmd_scene)
    x = sub.add_parser("shot"); x.add_argument("--source"); x.add_argument("--width", type=int, default=1280); x.add_argument("--out"); x.set_defaults(fn=cmd_shot)
    x = sub.add_parser("levels"); x.add_argument("--seconds", type=int, default=6); x.set_defaults(fn=cmd_levels)
    x = sub.add_parser("sync"); x.add_argument("ms", nargs="?", type=int); x.set_defaults(fn=cmd_sync)
    x = sub.add_parser("rate"); x.add_argument("--fix", action="store_true"); x.set_defaults(fn=cmd_rate)
    x = sub.add_parser("test"); x.add_argument("--seconds", type=int, default=10); x.set_defaults(fn=cmd_test)
    x = sub.add_parser("verify"); x.add_argument("file", nargs="?"); x.add_argument("--dupes", action="store_true"); x.set_defaults(fn=cmd_verify)
    x = sub.add_parser("clap"); x.add_argument("file", nargs="?"); x.add_argument("--max-seconds", type=int, default=60); x.set_defaults(fn=cmd_clap)
    x = sub.add_parser("stream"); x.add_argument("action", choices=["status", "start", "stop"]); x.set_defaults(fn=cmd_stream)
    x = sub.add_parser("call"); x.add_argument("request"); x.add_argument("data", nargs="?"); x.set_defaults(fn=cmd_call)
    sub.add_parser("mcp").set_defaults(fn=cmd_mcp)
    a = p.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
