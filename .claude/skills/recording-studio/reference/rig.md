# The rig: settings, why, history, recipes

This file is compiled from every OBS session since 2026-07-28 (the pre-flight sessions and the video-editor footage work). `studio.json` holds the values the checks enforce; this file holds the reasons. Update both when anything changes. On a different rig, rewrite Hardware and Current recording settings for your gear and keep the rest: the failure modes and recipes carry over.

## Hardware

- **Mac:** Mac Studio, M5 Ultra, 30 cores (10 super + 20 performance), 64-core GPU, 96 GB RAM, about 926 GB SSD (since 2026-11-20). Before that: M4 Pro MacBook Pro, 14 cores, 24 GB.
- **Display:** LG ULTRAGEAR 27" 4K, looks like 1920x1080, at 120 Hz, over HDMI. It is the only display, so **the OBS windows live on it**, and the `Screen` capture source has `hide_obs: true` to keep them out of screen recordings. Display UUID `6C2FB439-C053-4D38-BF5A-7361999969F6` (it was `AB422C89-…` on the MacBook, which also had a built-in XDR display).
- **Camera:** Sony ZV-E10 over HDMI into an Elgato **Cam Link 4K** on USB 3 (`ioreg -p IOUSB -l -w0 | grep -A12 -i "cam link"` shows `Device Speed 3`).
  - The Cam Link only exposes what the camera pushes over HDMI, and it maxes out at 4K30.
  - At 4K 60p the camera falls back to 1080p59.94.
  - 4K 30p crops the sensor 1.23x; **4K 24p is full width**, hence the 23.976 studio.
  - Mounted sideways for vertical.
- **Mic:** Shure SM7B into a Universal Audio **Volt 1**.
  - The SM7B wants about 60 dB of gain and the Volt gives about 55, so the knob lives near max.
  - OBS's global mic source `Shure SM7B` (`AuxAudioDevice1`) carries a compressor and a limiter filter.
- **Other audio devices:**
  - Cam Link 4K audio (the camera's own mic over HDMI; the source has `enable_audio: false` so it never mixes into the take)
  - Bose QC Ultra over Bluetooth (44.1k output only, 16k headset mic)
  - Loom virtual driver, iPhone Continuity mic (harmless)
- **OBS:** 33.0.1, Metal renderer (`global.ini` `[Video] Renderer=Metal`; a fresh install defaults to OpenGL), obs-websocket 5.7.6. The MacBook ran 32.2.2 / 5.7.4.

## OBS layout on disk

Everything below is under `~/Library/Application Support/obs-studio/`.

- **Profiles:** `basic/profiles/<Dir>/`
  - `basic.ini` (+ `recordEncoder.json`, `streamEncoder.json`, `service.json`)
  - Dirs `Horizontal_4K` and `Vertical_4K`; the display names have spaces.
- **Scene collections:** `basic/scenes/Horizontal_4K.json` and `Vertical_4K.json`. The `*.bak` files are the change history.
- **Logs:** `logs/YYYY-MM-DD HH-MM-SS.txt`, one per launch. `MaxLogs=10`, so read them soon after a take.
- **Websocket config:** `plugin_config/obs-websocket/config.json` (port 4455, auth on).
- **When OBS writes:**
  - `basic.ini` on Settings › Apply and on exit.
  - Scene JSON on exit only, so a force-quit loses live scene changes.
- **`basic.ini` holds the YouTube OAuth token in plain text.** Grep keys, never print the file.

## Current recording settings (both profiles)

| Setting | Value | Why |
|---|---|---|
| Output mode | Advanced | Only `[AdvOut]` keys are live; `[SimpleOutput]` is dead config that repeats the same key names |
| Canvas = output | 3840x2160 (vertical 2160x3840) | Native 4K; 1080p takes forced upscaling in 4K jobs (09-07) |
| FPS | 24000/1001 | Must equal the camera's HDMI rate; 24p = full sensor |
| Color | NV12, Rec.709, partial | Matches the Cam Link feed |
| Encoder | Apple VT HEVC hardware, CBR 40 Mbps, keyint 2s, main | Measured about 40.3 Mbps, about 18 GB/hour. `rc_max_bitrate 6000` in the log is inert |
| Container | Hybrid MP4, no splits | Crash-recoverable, Premiere imports it, supports chapter marks. Jason wants one file per take |
| Audio | AAC 320 on **1 track**, 48 kHz stereo | Twin tracks made Premiere's import fail silently (07-29) |
| Path | `~/Downloads`, `%CCYY-%MM-%DD %hh-%mm-%ss.mp4` | Where video-editor's intake looks |
| Renderer | Metal | 2026-11-23 on the M5 Ultra, 30s takes: graphics thread median 1.9 ms / 99th percentile 3.1 ms on Metal vs 2.4 / 8.2 ms on OpenGL, against a 41.7 ms frame budget. Both clean; Metal has the tighter tail |
| Cam Link source | `macos-avcapture`, `buffering: true`, `use_preset: false`, `enable_audio: false`, `supported_format` = the device's one 3840x2160 23.98 NV12 entry, `frame_rate 24000/1001` | The unbuffered `macos-avcapture-fast` duplicated frames (09-17) |
| Mic sync offset | 235 ms (last measured; moves per launch) | Clap-tested and confirmed 11-23 on the Mac Studio, fresh launch (see A/V sync) |
| Mic filters | Compressor 4:1 at -18 dB (6 ms attack, 60 ms release, 0 dB makeup), then Limiter at -6 dB | Rebuilt 2026-11-23. The MacBook's values were never written down, so these are fresh, mild settings, not the old ones |
| Streaming | YouTube RTMPS, VT H.264 CBR 8 Mbps high, keyint 2, rescale to 1080p (`RescaleFilter=2`, bicubic) | Account connected in OBS, no stream key on disk |

**Scenes:**
- Horizontal:
  - `4K`: the Cam Link full frame.
  - `Screen Capture`: the LG display 1:1 (`Screen`, a `screen_capture` source, cursor on, OBS windows hidden) plus a camera box, bottom-right (860x484 at 2980,1676). The box is the shared **Cam Link** source (`Capture Card Device`, scale 0.224), so it rides the same clap-tested mic offset as `4K`. The Mac Studio has no built-in camera, so the MacBook-camera box (and macOS Studio Light with it) is gone.
- Vertical: `4K Vertical`, the Cam Link rotated 90° at pos (2160,0).

## Changelog

- **07-28:** laggy footage.
  - Cause: the camera sent 23.976p into a 30 fps canvas, so 20% of frames were duplicates.
  - The Mac had 0 skipped frames. The fix was matching fps.
- **07-29:** recording had been using the stream encoder (CBR 6000 H.264). Moved to a dedicated HEVC encoder.
- **08-04:**
  - Deleted a dead Screen Recording scene. Its capture had no display, and a stray MacBook camera source was holding the camera open.
  - Loom was quit.
- **09-01:** the Cam Link device ID changed after a port change (`0x2412000fd9007b` → `0x12412000fd9007b`), giving a black preview.
- **09-07:**
  - Container went `mkv` → `hybrid_mp4`.
  - Splits went on for a 3-hour run, then off again at Jason's request.
  - A 35-minute proof run had 0 skipped and 0 lagged frames.
- **09-11:**
  - The canvas went to 4K, the camera to 4K 24p, and FPS to 24000/1001.
  - Bitrate went 16 → 40 Mbps.
  - The PiP camera was rescaled 0.425 → 0.2125.
- **09-14:** YouTube streaming added (`*.pre-youtube.bak`).
- **09-17:** Cam Link source changed to buffered `macos-avcapture` (`*.pre-buffered.bak`), which killed the duplicated frames.
- **09-18:** mic sync 170 → 255 ms (`*.pre-sync255.bak`).
- **09-19:** the Volt 44.1k cause was found (Premiere). Jason deleted the 30s Volt watchdog LaunchAgent.
- **09-20:** created the Vertical 4K profile and collection.
- **09-25:**
  - `Untitled` renamed to Horizontal 4K.
  - The `~/Applications` launchers were built.
  - A 410 ms retune was reverted (see Sync).
- **09-26:**
  - obs-websocket turned on (`config.json.pre-enable.bak`).
  - This skill and the `obs` MCP were built.

- **09-27:** hid the YouTube Live Control Panel dock in both profiles (Docks menu toggle, then a quit so OBS saved it). Its visibility lives per profile in `basic.ini` `[YouTube - RTMP] DockState`, a base64 Qt state that is only saved on quit. Bring it back with Docks › YouTube Live Control Panel. Going live doesn't need it: Manage Broadcast sits in Controls.
- **09-28:** the `Screen Capture` camera box moved from the MacBook Pro Camera to the Cam Link. The MacBook camera's latency never matched the 255 ms mic offset. First clap take after the swap (fast, continuous claps) read audio about 120 ms early on all 4 claps (114/126/124/123) with no re-init logged; after an OBS relaunch, 4 slow claps landed within ±25 ms (onset between the meeting frame and the first closed frame every time), so 255 holds for the corner box too. Relaunching fixed it; the offset was not touched.
- **09-28, later:** Jason put the MacBook Pro Camera back as the `Screen Capture` corner box (`Video Capture Device`) on purpose. While OBS holds the built-in camera open, macOS Studio Light (Control Center › Video Effects, per app) also applies to the Cam Link feed, even with `4K` on program. Only Horizontal 4K carries the MacBook camera, so Vertical takes get no Studio Light. Clap take `2026-09-28 18-18-55.mp4` with Studio Light on, `4K` scene: claps at 5.273 s and 6.439 s read audio 18 and 16 ms *late* (within a frame), verify CLEAN, so 255 holds with the effect on. The corner box is the MacBook camera again, whose latency never matched 255 (entry above).
- **11-23: new Mac (Mac Studio M5 Ultra), rig rebuilt from this file.** OBS 33.0.1 was a fresh install on stock settings: profile `Untitled` in Simple mode (H.264, `hybrid_mov`, takes to `~/Movies`, 160k audio), OpenGL renderer, the unbuffered `macos-avcapture-fast` camera source, mic on `default` with no filters and 0 ms sync, websocket off, no Vertical profile, no launchers. Nothing from the MacBook had been migrated and no backup of its `obs-studio` folder exists.
  - Rebuilt: both profiles (`basic.ini` patched section-aware with OBS quit, `recordEncoder.json` / `streamEncoder.json` written), both scene collections, the mic source + filters, the `Screen Capture` scene, `~/Applications/OBS {Horizontal,Vertical} 4K.app` (osacompile applets around `open -a OBS --args --profile … --collection …`), websocket on, renderer Metal. The stock config is kept at `~/Library/Application Support/obs-studio.pre-rig-rebuild-2026-11-23.bak`.
  - Proof: horizontal 75s take 1796/1796 frames, 0 irregular packet gaps, 0 of 555 moving frames duplicated, no skipped or lagged lines, 40.4 Mbps HEVC Main, one 48k AAC track at 320k. Vertical 12s take 285/285 at 2160x3840. While recording: OBS about 15% of one core, UVCAssistant 29%, WindowServer 37%. Encode takes 0.7 ms a frame. The Mac was never the limit on the MacBook either; the ceiling is the camera chain (ZV-E10 over HDMI into the Cam Link: 4K 23.98, 8-bit 4:2:0).
  - **Still open:** a mic level check at recording volume, and the YouTube account in OBS (Settings › Stream › Connect Account; the stream encoder and 1080p rescale are set but untested here).
  - Cam Link device ID on this Mac: `0x32412000fd9007b`. Volt 1 CoreAudio UID: `AppleUSBAudioEngine:Universal Audio:Volt 1:23202036049256:1,2`.
  - Building a collection by copying the other one's JSON: scene items carry `pos_rel` / `scale_rel` / `scale_ref`, and OBS 33 loads those over `pos` / `scale`, so the copied Vertical item came up at scale 1.78, x -2333. Set the transform live (`SetSceneItemTransform`) after the first launch instead of editing the JSON.
  - OBS 33 writes the scene JSON as changes happen (the collection survived the crash below), not only on exit.

## A/V sync

- **Where it lives:** `AuxAudioDevice1.sync` in each scene JSON, in nanoseconds (`255000000`). Live, it's `SetInputAudioSyncOffset` in ms.
- **History:**
  - 170 ms at 1080p30 (07-29).
  - 255 ms after the Cam Link buffering change (09-18). At 170 the audio led by about 85 ms.
- **09-25, a mid-session re-init:**
  - Takes at 255 ran audio about 160 ms early, and all of them came after a `Channel map enabled` / `coreaudio: Device 'Volt 1' [48000 Hz] initialized` pair logged long after startup.
  - A 410 ms retune then measured about 160 ms *late* on a fresh launch, so it was reverted to 255, which measured within 0-40 ms.
  - Rule: **the lag shifts per audio-device session. After a mid-session re-init, relaunch OBS; never retune.** The trigger (a USB blip or a mic property change) is unproven.
- **10-02, a fresh launch, no re-init:** all three takes ran audio 140–190 ms early at 255 (measured 10-04 by `lip-sync.py` on a mouth crop `640:480:1680:880` of the 4K horizontal framing, and by plosive bursts vs the lips parting). The right offset moves per launch, not only per re-init. A take already recorded off is fixed in the edit by slipping picture: video-editor `lanes/premiere/lab-notes.md` § Step 2.
- **10-05, a fresh launch, no re-init, clap-tested:** 4 claps at 255 read +142, +138, +152, +156 ms (audio early, mean 147), so it was set to **402**. Confirmed on the same launch: 6 claps read +9 to +30 ms (mean +20, inside the ±40 window). The right value looks bimodal per launch, either about 255 or about 400-410 (09-25's 410 measured 160 ms late on a different launch), so clap every launch and read the sheets; never carry the last value forward on trust. Plosives in speech trigger onsets too; since 10-14 `obs_clap` skips them by peak (entry below).
- **10-14, a fresh launch, no re-init, clap-tested:** clap take `2026-10-14 16-57-19.mp4` (Jason talked first, so onsets 1-3 were plosives; the 4 claps were onsets 4-7, sheeted by hand). At 402 every onset landed 50-78 ms *after* the first closed frame; measured to the midpoint of the meeting and closed frames: -87, -99, -71, -91 (audio late, mean -87), so it was set to **315**. That is neither 255 nor 400, so the "bimodal" read above is wrong: the value just moves per launch. Speech peaked -10.5 dBFS (in target). Same pre-flight re-pointed the Cam Link (ID back to `0x2412000fd9007b`); the first `fix` run relaunched OBS and missed the re-point, the second caught it. Confirmed on the same launch: `2026-10-14 17-01-55.mp4`, 6 claps read +8, +10, +19, +27, +21, +7 ms (mean +15, inside ±40), every onset between the meeting frame and the first closed frame; verify CLEAN, no re-init.
- **11-23, Mac Studio, a fresh launch, no re-init, clap-tested:** take `2026-11-23 17-37-00.mp4` at 315 (the MacBook's last value), 8 claps, no speech. On every sheet frame 4 was the blurred meeting frame and frame 5 the first sharp closed one; measured to their midpoint: -91, -62, -91, -77, -88, -90, -74, -63 ms (audio late, mean -80), so it was set to **235**. The claps peaked at exactly -6.0 dBFS, the new limiter's ceiling. The first confirm take (`17-38-15`) had no claps in it (Jason was talking; the one onset `obs_clap` sheeted was speech). Confirmed on the same launch with `2026-11-23 17-39-37.mp4`: 8 claps, 6 sheets read, -2, -11, -19, +13, +14, +3 ms (mean about 0, inside ±40); every onset fell between the blurred meeting frame (frame 6) and the first sharp closed frame. On claps 2 and 3 frame 7 still carried a little blur; reading those one frame later gives +30 and +23, still inside the window. Verify CLEAN, no re-init.
- **Clap method** (`studio.py clap` automates the first half):
  - Audio onsets come from a 1 ms peak envelope: a point above -20 dBFS that is more than 20 dB over the prior 300 ms median.
  - Only onsets within 6 dB of the loudest one get a sheet (up to 8). Claps clip or nearly do; speech plosives peaked -11 to -17 dBFS on 10-14, so they're listed as skipped. Before 10-14 it sheeted the first 4 onsets, which were all speech when Jason talked first.
  - Landscape sheets crop to the centre two-thirds, chest up (`crop=iw*2/3:ih*3/4:iw/6:ih/4`), so contact reads at thumbnail size. Vertical sheets are uncropped.
  - Contact sits between the blurred meeting frame and the first sharp closed frame: measure to their midpoint. In sync = the onset lands between them.
  - Compare each onset with the frame where the hands **first meet**, not the frame at the onset.
  - Frame n sits at n × 1001/24000 s.

## Frame integrity recipes

- **Real drops** show up in the log as `skipped frames due to encoding lag` and `lagged frames due to rendering lag`. The profiler dump at the end (`obs_graphics_thread … % below 41.7 ms`) shows the headroom.
  - They have never been non-zero on this rig; load was never the lever.
  - Normal background CPU while recording (percent of one core): UVCAssistant 35-50%, WindowServer about 40%, OBS 20-57% on the M4 Pro; UVCAssistant 29%, WindowServer 37%, OBS 15% on the M5 Ultra.
- **Drawn minus output** is a fixed 5-6 frame tail at stop. Examples: 411/406, 12329/12323, 293/287.
- **Duplicated frames with a clean log:** the tblend/YAVG neighbour test (`studio.py verify --dupes`).
  - A duplicate is a frame whose YAVG is under 25% of both neighbours, where the neighbours sit between 0.4 and 5.
  - Only moving footage counts.
  - `mpdecimate` gives false positives here.
- **Frame timing:** check `nb_frames` against duration × 23.976. Gaps between packets should sit at 0.0417 s:
  ```bash
  ffprobe -v error -select_streams v:0 -show_entries packet=pts_time -of csv=p=0 "$F" | sort -n | awk 'NR>1{d=$1-p; if(d>0.0425||d<0.041) bad++} {p=$1} END{print NR" frames, irregular gaps: "bad+0}'
  ```
- **Choppy only on playback review:** the LG's refresh (120 Hz now, 95 Hz on the MacBook) vs 24p can judder on playback. The file is fine.

## Volt 1 sample rate

- **The one recurring real failure:** found at 44.1k on 08-04, 08-27, 09-11 and 09-19. At 44.1k, OBS resamples silently and the audio drifts on long takes.
- **Cause, proven 09-19:** Premiere with Default Input = Volt, plus Bluetooth output. Premiere clocks the Volt to the 44.1k Bose within 2s of launch. The fix is Premiere › Settings › Audio Hardware › Default Input = **No Input**.
- **If it drifts again:** find the setter before blaming hardware:
  ```bash
  /usr/bin/log show --last 26h --predicate 'process == "usbaudiod" AND eventMessage CONTAINS "setSamplingRate newRate"' --style compact | tail -30
  ```
  Match the timestamps to app launch times (`ps -p PID -o lstart`). Always call `/usr/bin/log`: a zsh `log` function shadows it.
- **What survives a reboot:** `plutil -p /Library/Preferences/Audio/com.apple.audio.DeviceSettings.plist | grep -i -A12 volt`.
- **No background watchers.** The 30s LaunchAgent fought Premiere and Jason deleted it.

## Dead ends (don't retry)

- **Closing apps to fix drops.** There was 26x render headroom. Screen Studio exporting is the only real conflict.
- **The display refresh theory** (95 Hz on the MacBook; the Mac Studio runs the LG at 120 Hz and takes are clean). The NTSC 29.97 drift theory.** Always check whether the loss scales with take length first.
- **Recording at 59.94 "for smoothness".** The HDMI 59.94 stream carries each 30p frame twice.
- **`killall replayd`** (SIP-protected). **Reduce Transparency.** **Blaming the Volt firmware or Wispr Flow.**
- **Premiere at 48k with a Bluetooth output.** The Bose clock only allows 44.1k.
- **`lip-sync.py` on wide talking takes without `--mouth-crop`.** It returns UNMEASURED; with a tight mouth crop it works (10-04).
- **Tools that don't work here:**
  - `system_profiler SPUSBDataType` returns nothing (use `ioreg`).
  - `ps rss` understates WindowServer (use `top`).
  - Homebrew ffmpeg has no `drawtext`.
  - `timeout` isn't installed.
- **Clicking through the Settings window in the background.** Clicks on a page report ok but never switch it. Full-screen control works.
  - Start/Stop Recording clicks do work in the background.
  - The websocket makes all of this moot.
- **Third-party OBS MCP servers** (evaluated 09-26):
  - royshil/obs-mcp: stale, and its screenshot tool truncates the image.
  - Tom-R-Main/OBS-MCP: 5 weeks old, 3 stars.
  - xDarkzx (PyPI `obs-mcp`): breaks on import with mcp 2.x.
  - The rest are Windows/Linux-only or thin.
  
  `studio.py mcp` is a hand-rolled stdio JSON-RPC server with no SDK dependency.

## OBS 32 automation hazards

- **GetStats leaks memory on macOS** (obs-studio 13918, about 2 MB/min at 1 call/s). Never poll it.
- **Switching scene collections over the websocket can crash OBS** (obs-websocket 1351). Relaunch with `--collection` instead; the raw tool blocks it.
- **Calling StartStream twice, or switching scenes while a stream is starting,** can crash OBS.
- **Chapters are Hybrid MP4 only.**
- **`GetInputPropertiesListPropertyItems` on a `screen_capture` source's `display_uuid` crashed OBS 33.0.1** (2026-11-23: SIGSEGV in obs-websocket, `strlen` of a null item name; the source had no display set yet). Get the display UUID outside OBS (`CGDisplayCreateUUIDFromDisplayID`, needs `import ColorSync` in Swift) and write `display_uuid` into the scene JSON with OBS quit.
- **A `macos-avcapture` source created over the websocket needs `supported_format`** as well as `frame_rate`, or it logs `Configured format not found on device` and stays black. Read the value from `GetInputPropertiesListPropertyItems` → `supported_format` (safe on this source).
- **Camera switched on after OBS launched = pure black feed** (not the NO SIGNAL card), logged as `Capture Card Device: Configured format not found on device`, and OBS never reopens it on its own. Fix without a relaunch: `SetInputSettings` on `Capture Card Device` with its own current settings (`overlay: true`) reopens the device. Hit 2026-10-05.
