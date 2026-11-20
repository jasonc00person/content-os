# 🛠️ Setup — read this first

This is a **content system you run with [Claude Code](https://claude.com/claude-code).** Research
your niche, generate hooks, write scripts in your own voice, keep a Notion pipeline, design Instagram
carousels, write YouTube descriptions, post to every platform. Claude runs each step through a skill;
you talk to it in plain English.

**Runs natively on macOS, Windows, and Linux.**

The fastest path: unzip, open this folder in Claude Code, and say **"run the setup"**. Claude runs the
one-command installer (**`./setup.sh`**: installs every tool via Homebrew on macOS / winget on Windows /
apt+uv on Linux, pre-builds the transcription engine and the carousel renderer, verifies itself, safe to
re-run), tells you which accounts still need connecting, and then walks you through
**`brand-kit.md`**, the one file that makes the system yours. Everything below is the same setup by
hand, if you prefer to see each step.

### 🪟 On Windows — one install first

No WSL, no VM. The scripts run through **Git Bash**, the shell that ships with **Git for Windows**
(also the shell Claude Code uses on Windows):

1. `winget install Git.Git` (in PowerShell), then restart Claude Code so it finds Git Bash.
2. Unzip the project anywhere normal (e.g. `C:\Users\<you>\content-os`) and open that folder in
   Claude Code.
3. Everything below runs unchanged; wherever a command says `brew`, use the **Windows (winget)**
   line. After any `winget install`, open a **new** terminal (and restart Claude Code once) so PATH
   picks the tool up. Python on Windows is `python`, not `python3` (the scripts handle it).

---

## 1. Install the tools

**Automatic** (recommended):

```bash
./setup.sh
```

Installs everything missing, builds the shared faster-whisper engine
(`~/.cache/content-os/whisper-venv`) and the carousel renderer (Playwright, driving your Google Chrome), runs
`./check-setup.sh`, and writes the `.setup-complete` marker. Re-run after any restart; it skips what's
done. The one manual step it can ask of you: installing Homebrew on a fresh Mac (needs your password),
or the `sudo apt` lines on Linux.

**Manual**, if you'd rather:

```bash
./check-setup.sh      # report-only: prints the exact install command for anything missing
```

macOS: `brew install uv ffmpeg yt-dlp jq node python`
Windows: `winget install astral-sh.uv Gyan.FFmpeg yt-dlp.yt-dlp jqlang.jq OpenJS.NodeJS.LTS Python.Python.3.12`
Linux: `sudo apt install -y ffmpeg jq curl python3` + Node ≥ 22 via NodeSource + `curl -LsSf https://astral.sh/uv/install.sh | sh` + `uv tool install yt-dlp`

Then, once: `bash .claude/skills/carousel-generator/install.sh` (npm deps; renders through Google Chrome, so install Chrome first).

Whisper models (~75 MB to ~460 MB) download from Hugging Face the first time each skill transcribes.
Needs internet once.

## 2. Connect your accounts (Claude tells you which of these are still missing)

| Connection | Used by | How |
|---|---|---|
| **Notion MCP** | the content pipeline DB, `scriptwriter`, `yt-description` | `claude mcp add --transport http notion https://mcp.notion.com/mcp`, then `/mcp` inside Claude Code to sign in, then restart Claude Code |
| **Apify MCP** | `ig-competitor-research`, the Instagram half of your voice corpus | `claude mcp add --transport http Apify https://mcp.apify.com` (capital A), then `/mcp` to sign in. Pay-as-you-go, roughly $0.20 per research run |
| **Claude in Chrome** (extension) | `yt-feed-research`, `ig-feed-research`, `dm-revival`, `manychat-flow` | Install the extension in the Chrome profile that's logged in to YouTube/Instagram. Run Claude Code from the **terminal** for these skills (the desktop app can't drive the tab) |
| **ManyChat** (optional) | `manychat-flow` | A ManyChat account connected to your Instagram, logged in in the same Chrome profile, with at least one comment-keyword promo flow to duplicate |
| **Zernio** (posting) | `auto-poster` | Create an account, connect your platforms, copy the API key: `cp .claude/skills/auto-poster/.env.example .claude/skills/auto-poster/.env` and paste it there. Claude fills the account IDs for you |
| **OBS Studio** (optional, macOS) | `recording-studio` | OBS 30+ with a horizontal and a vertical profile + scene collection. Quit OBS, then ask Claude to "set up the recording studio": it turns on obs-websocket, registers the `obs` MCP server, and fills `.claude/skills/recording-studio/studio.json` with your gear |
| **Higgsfield** (optional) | `thumbnail-generator`, AI covers in `carousel-generator` | `curl -fsSL https://raw.githubusercontent.com/higgsfield-ai/cli/main/install.sh \| sh` then `higgsfield auth login`. Skip it and carousels use a typographic cover (thumbnails do need it) |

Using the Claude desktop app instead of the CLI? Add Notion and Apify under Settings → Connectors;
the skill instructions are the same.

## 3. Make it yours (required for anything in your voice)

1. Open **`brand-kit.md`** and fill in Part A: name, handles, niche, offer (name, URL, price,
   deliverables, comment keyword), who it's for, proof, competitors, your Notion parent page.
   Ten minutes. Leave blanks if you must; Claude asks for them.
2. Say **"apply my brand kit"**. Claude writes your `CLAUDE.md` profile, the four `backbone/` files,
   `competitor-list.md`, creates the Notion content database (schema in `notion-pipeline.md`), fills
   the auto-poster account IDs, then runs **`voice-corpus-builder`**: it pulls your top YouTube uploads
   and Instagram reels, transcribes them into `voice-corpus/`, and drafts `voice-dna.md`, the rulebook
   every writing skill uses. That last step is what makes scripts sound like you instead of like AI.
3. Optional: drop 4-8 photos of your face into `assets/face-refs/` for AI thumbnails and carousel covers.
4. Optional: `python3 title-corpus/build.py` (30s) builds the YouTube title bank that `hook-generator` uses for
   long-form titles; re-run it whenever a batch of winners lands.

## 4. First things to try

- **"research my competitors on YouTube"** (yt-competitor-research, no accounts needed; needs your
  competitor list from the brand kit, or just name the channels inline) or **"instagram competitor
  research"** (same, plus Apify).
- **"write me hooks for a video about X"** (hook-generator).
- **"script this: <a research pick or an idea>"** (scriptwriter → beat sheet in Notion).
- **"make a carousel about X"** (carousel-generator → PNGs + caption in `carousel/outputs/`).
- **"post this video: ~/Downloads/final.mp4"** (auto-poster → Zernio → every connected platform).
- **"write the youtube description for <video>"** (yt-description).
- **"transcribe this link: <url>"** (transcribe-url).
- **"add this idea to notion: <link>"** (idea-capture → a fully formatted Idea page in your pipeline).
- **"mine my comments"** (yt-comment-mining → demand clusters + a reply queue in `research/`).
- **"are we good to record?"** (recording-studio → the OBS + Mac pre-flight, fixes what it safely can).
- **"make a thumbnail for <title>"** (thumbnail-generator → `thumbnails/<slug>/`, needs Higgsfield + face refs).

The whole pipeline and every rule is documented in `CLAUDE.md`; each skill's own README lives in
its folder under `.claude/skills/`.

## 5. Update to a new version

New versions ship often. Download the new zip, keep working in the folder you already have, and tell
Claude **"update"**. It finds the newest download in your Downloads folder (by its version, so a second
download named `content-os-client (1).zip` is fine) and merges it in with `update.py` without touching
your work: your brand kit, backbone, voice corpus, research, transcripts, carousels and every other
output stay yours, and anything you and the new version both changed is sorted out with you. Your own
standing instructions for Claude go in `my-rules.md`, which no update ever changes. Changed your mind?
Tell Claude **"undo the update"**. `RELEASE.md` lists what changed in each version, `VERSION` says which
one you have.

**Installed before updates existed (any version up to Sep 29, 2026)?** The first time, unzip the new
download, open THAT folder in Claude Code and say **"update my Content OS"**. Claude finds your folder
and brings it up to date (if it can't find it, it asks where it is). After that, "update" in your own
folder is all it takes.

---

## What's in the box

| Path | What it is |
|------|-----------|
| `CLAUDE.md` | The system's brain: the pipeline, the Notion rules, the folder map, the gotchas. |
| `SETUP.md` | This file. |
| `brand-kit.md` | The one file you fill in; "apply my brand kit" pushes it everywhere. |
| `setup.sh` / `check-setup.sh` | One-command installer / report-only checker (macOS, Windows, Linux). |
| `update.py` | Brings in a new version without touching your work (§ 5). |
| `my-rules.md` | Your own standing instructions for Claude; updates never change it. |
| `RELEASE.md` / `VERSION` | What changed in each version; which version you have. |
| `.claude/skills/` | The 18 skills (each with a SKILL.md, most with a README and scripts). |
| `backbone/` | Your business docs (templates until you apply the brand kit). |
| `voice-corpus/`, `voice-dna.md` | Your voice, built from your own videos by voice-corpus-builder. |
| `competitor-list.md`, `notion-pipeline.md` | Who to research; the Notion schema + your DB ids. |
| `knowledge/`, `research/`, `transcripts/`, `carousel/outputs/`, `descriptions/`, `thumbnails/` | Where the outputs land (start empty, each has a README). |
| `title-corpus/`, `assets/` | The long-form title bank (built by `build.py`) and your face refs / logos / fonts. |
