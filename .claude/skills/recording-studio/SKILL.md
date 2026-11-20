---
name: recording-studio
description: "The AI recording assistant for OBS Studio: pre-flight the Mac + rig ('are we good to record?'), switch between the Horizontal 4K (long-form) and Vertical 4K (short-form) setups, check framing from a live screenshot, check mic levels, start/stop/pause the recording, drop chapter markers, verify every take (codec, frames, audio track, levels, dropped frames, mic re-inits), run clap tests to set A/V sync, and monitor a YouTube stream. Drives OBS through obs-websocket via the first-party `obs` MCP server (same code as scripts/studio.py). Pipeline step 5: beat sheet in, verified takes out to video-editor. Triggers: are we good to record, are we all good for a smooth recording, obs check, preflight, set up obs, open obs, switch to vertical, switch to horizontal, start recording, stop recording, pause recording, mark that, check my framing, how do I look, mic check, check my levels, clap test, audio out of sync, lips out of sync, check the take, verify the recording, let's film, film this video, recording studio, go live, stream to youtube, obs settings."
---

# recording-studio — the AI recording assistant for OBS

Step 5 of the pipeline: `scriptwriter` lands a beat sheet → **Jason films here** → verified takes go to the `video-editor` project. This skill owns everything about OBS: the rig check, the camera and mic, the take, the file.

## The control surface

- **MCP server `obs`** (user scope, so every project has it: `mcp__obs__obs_*`). First-party, 17 tools. Use these whenever they're loaded.
- **The same code as a CLI**: `uv run --quiet --script .claude/skills/recording-studio/scripts/studio.py <cmd>` (`--help` lists them). Same functions, different transport. Use it only when the MCP tools aren't loaded (the first session after install, or a client machine before registration).
- **`studio.json`** = the rig the checks compare against (profiles, canvas, fps, encoder, bitrate, camera, mic, sync offset, apps to quit). When a setting changes on purpose, change it there too, or pre-flight will flag the new truth as wrong.
- **`reference/rig.md`** = why every value is what it is, the incident history, and the measurement recipes. Read it before changing any OBS setting or diagnosing a bad take.
- The websocket password is never copied anywhere. The script reads it from OBS's own `plugin_config/obs-websocket/config.json`.

Nothing here polls. `obs_status` calls GetStats, which leaks memory in OBS 32 on macOS, so call it when asked, never in a loop.

## 1. "Are we good to record?"

Run `obs_preflight` with `fix=true`. It checks, in order:

- **mic:** Volt 1 connected, default input, at 48 kHz.
- **machine:** thermal, AC power, memory, swap, WindowServer size, competing apps.
- **OBS mode:** the profile and collection are a matching pair.
- **mic in OBS:** OBS opened the Volt at 48k, no mid-session re-init, mic unmuted, sync offset at the clap-tested value.
- **camera:** Cam Link present, the source points at its current device ID, the source is buffered and fps-matched, and the feed isn't black.
- **canvas and output:** canvas + fps, output settings, record bitrate, and disk hours.

`fix=true` applies only the safe fixes:
- quits Loom and Spotify
- sets the Volt to 48k with OBS quit, then relaunches
- re-points a moved Cam Link
- unmutes the mic
- relaunches OBS after a mid-session re-init

It never touches a live recording.

**Report it Jason's way:** the verdict line first (GO / GO with notes / NO-GO), then only what was fixed, what blocks, and the notes. Skip the OK list. Name every app quit and every OBS restart. Blockers only Jason can clear:
- **camera black:** the camera is off, the lens cap is on, or HDMI is out. The feed shows Elgato's "NO SIGNAL" card.
- **Volt missing:** check the cable.
- **swap or WindowServer flagged:** restart the Mac before a long take.

Before a take longer than 30 min, also confirm the disk hours cover it with room to spare.

Want the mic checked too? Run `obs_levels` while he talks at recording volume. Target peaks are -12 to -6 dBFS. "Too quiet" means one notch more gain on the Volt.

## 2. Film a video ("let's film X")

1. **Resolve the Notion page** for X (the standard `ntn datasources query` in CLAUDE.md). Its `Format` picks the mode: Long-form = `horizontal`, Short-form = `vertical`.
2. **Set the mode:** `obs_mode` if OBS is on the other one. It relaunches OBS in about 9s and refuses while recording.
3. **Run the pre-flight** as in section 1.
4. **Check framing:** `obs_screenshot`, then look at it. Check:
   - eyes around the upper third, headroom not cropped
   - in focus, exposure not blown
   - nothing odd in the background
   - vertical: face in the upper-middle, since the bottom third carries captions
   
   Say what to fix in one line, or "framing's good."
5. **Check the mic:** `obs_levels` while he says his first line.
6. **Roll:** `obs_record start`.
   - During the take, `obs_mark` on request ("mark that", "redo", "beat 3", "good one"). The marks become chapters in the file.
   - `pause` and `resume` work too.
7. **Cut:** `obs_record stop`. It returns the file and auto-verifies it. Report CLEAN or BAD TAKE, the duration, and the path. A BAD TAKE says what's wrong and whether it needs a reshoot.
8. **Wrap:**
   - List the session's takes with their full paths.
   - Flip the Notion page to `To Edit` (the standing rule; add `Raw Footage` only if Jason gives a link).
   - Hand off: Jason opens `video-editor` and points it at the take. Its intake copies the file. Never move or rename takes here.

**Takes are separate files, each named by OBS's timestamp, in `~/Downloads`.** Repeats of a line can live inside one file: the editor keeps the last clean take. This skill never deletes a real take.

## 3. Horizontal ↔ vertical

`obs_mode horizontal|vertical` quits OBS and relaunches it with `--profile X --collection X`, then confirms both over the websocket.

- **Horizontal 4K:** 3840x2160. Two scenes:
  - `4K`: camera full frame.
  - `Screen Capture`: the LG display 1:1 with a camera picture-in-picture.
- **Vertical 4K:** 2160x3840. The Cam Link feed is rotated 90°, because the camera is mounted sideways for full-sensor 9:16.

Jason's `~/Applications/OBS {Horizontal,Vertical} 4K.app` launchers do the same thing by hand. Never switch the profile or collection live over the websocket: switching collections can crash OBS 32. The raw tool blocks it.

## 4. A/V sync (clap test)

**When:** a new camera, interface, cable or OBS version, Jason says the lips look off, or right before any session that matters: a fresh launch with no re-init still ran audio 140–190 ms early at 255 (2026-10-02 takes, measured 10-04), so only a recorded clap take proves sync, never the preview. The offset lives on the `Shure SM7B` source. It was 402 ms at the last clap test (2026-10-05), but the right value moves per launch (255 on 09-18 and 09-25), so `studio.json` holds the last measured value, not a constant.

**Never retune after a mid-session interface re-init.** Pre-flight and verify both flag it. The lag jumps about 160 ms per audio-device session, so relaunch OBS and re-check instead.

1. **Start fresh:** relaunch OBS (`obs_mode` to its current mode), then run the pre-flight.
2. **Record the claps:** `obs_test_take` with `seconds: 15`. Jason claps sharply 3 times, a second apart, with his hands in frame.
3. **Measure:** `obs_clap` defaults to the newest take. It skips onsets more than 6 dB under the loudest one (speech plosives) and lists them. For each clap (up to 8) it gives:
   - the audio onset time
   - a contact sheet of 12 frames (6 per row, top row first) with each frame's timestamp, cropped to the centre on horizontal takes
   
   Read each sheet. Contact falls between the blurred frame where the hands meet and the first sharp closed frame, so measure to their midpoint. Offset = that time - the onset. Positive means the audio is early.
4. **Set it:** new offset = current + the average offset. Apply it with `obs_sync`.
5. **Confirm:** repeat steps 2-3 on the new value. Accept within ±40 ms (one frame is 42 ms).
6. **Record the value:** update `mic.sync_ms` in `studio.json` and the sync history in `reference/rig.md`.

The clap is the only proof BEFORE a session. After it, video-editor measures every take at intake with `workflows/lip-sync.py --mouth-crop 640:480:1680:880` (the horizontal 4K framing; the default crop answers UNMEASURED on this wide shot) and lays the picture slipped by what it finds, so a missed clap costs a measured correction, not a re-record. A non-zero slip there means this rig needs its clap test before the next session.

## 5. Checking a take

`obs_verify` (default: the newest take) checks:
- HEVC at the studio canvas and 23.976 fps
- frame count vs duration
- exactly **one** 48 kHz AAC track (twin tracks make Premiere's import fail silently)
- audio peak
- skipped or lagged frames, and mic re-inits, from that take's slice of the OBS log
- chapter marks

When a take *looks* choppy but the log is clean, run `dupes=true`. That means duplicated frames at capture (see rig.md).

"Total drawn minus total output" in the log is a fixed 5-6 frame tail at stop. It is **not** dropped frames. The real counters are the `skipped` and `lagged` lines.

## 6. Streaming to YouTube

The profile streams YouTube RTMPS: canvas rescaled to 1080p, H.264 CBR 8 Mbps, account connected in OBS (no stream key in any file).

**Going live is Jason's click.** In OBS it's Manage Broadcast → Select existing broadcast → Select broadcast and start streaming. That's publishing, so `obs_stream start` only runs on his explicit go. It has not been tested headless with the connected account, so the first time, confirm in YouTube Studio that the broadcast went live.

`obs_stream status` shows skipped frames, congestion and reconnects. Recording while streaming is off (`RecordWhenStreaming=false`). Start a recording too if he wants a master file.

## 7. Changing OBS settings

1. **Change it live when you can.** Use `obs_call` with a raw obs-websocket v5 request for sources, transforms, filters, input settings and profile parameters. Output and encoder changes only take effect after a relaunch.
2. **Edit files only with OBS quit.** OBS rewrites the profile and scene files on exit. `obs_quit` first, then:
   - back up to `*.pre-<reason>.bak`
   - patch `basic.ini` section-aware: `RecFormat2`, `RecEncoder` and friends also exist, inert, under `[SimpleOutput]`
   - relaunch with `obs_launch`
   - `obs_preflight` to confirm
3. **Never print `basic.ini` whole.** It holds the YouTube OAuth token in plain text. Grep specific keys.
4. **The Settings window through computer use** needs full-screen control. Background clicks report success but never switch Settings pages. The OBS windows live on the Built-in Retina display.
5. **Update `studio.json`** and the changelog in `reference/rig.md` in the same turn.

## Setup (once per machine)

1. **Turn on obs-websocket:** OBS quit, then `studio.py setup`. It enables the server with auth on port 4455 and generates a password only if none exists. Relaunch OBS.
2. **Register the MCP** at user scope:
   ```bash
   claude mcp add obs -s user -- "$(command -v uv)" run --quiet --script "$PWD/.claude/skills/recording-studio/scripts/studio.py" mcp
   ```
   Run it from the repo root. New sessions get the `obs_*` tools.
3. **Describe your rig in `studio.json`.** The OBS profile and collection names for each mode, canvas, fps, the camera source + device name, the mic source + interface name, and the sync offset once clap-tested.

macOS only: CoreAudio for the sample rate, plus pmset/osascript. Deps: `uv` (the script pins `obsws-python` inline) and `ffmpeg`/`ffprobe`.

## Gotchas

- **The Volt drops to 44.1 kHz** when Premiere is open with Bluetooth headphones as the output: Premiere clocks the Volt to the 44.1k-only Bose. The fix is settings-only: Premiere › Audio Hardware › Default Input = No Input. Jason deleted the 30s watchdog agent on purpose, so never add a background watcher for this.
- **Changing the interface rate while OBS is open kills OBS's mic** (`-10863`). `fix` quits OBS first for this reason.
- **Black preview:** the camera is off (the NO SIGNAL card). Or, after a USB port change, the Cam Link's device ID changed and OBS logs `Unable to initialize device`. Pre-flight's `fix` re-points the source.
- **Camera fps ≠ canvas fps means judder** (a 20% duplicate cadence at 24p into 30). The camera outputs 4K 23.98 over HDMI.
  - On the ZV-E10, 4K30 crops 1.23x and 4K24 uses the full sensor.
  - The Cam Link maxes out at 4K30.
- **The quit command errors every time.** `tell application "OBS" to quit` prints `User canceled (-128)`, but OBS does quit.
- **`user.ini` can name a different collection than the one loaded.** Trust the websocket (what the tools report) or the log's `Command Line Arguments`.
- **`StopRecord` returns before the muxer finishes.** Until `outputActive` goes false, `SetRecordDirectory` fails with code 500. The script waits for it.
- **Never let Loom record, or Screen Studio export, during a take.** Loom cancels whole takes when ScreenCaptureKit stalls. Keep Notion open (the script is in it). Jason quits Premiere himself, so never force-quit it.
