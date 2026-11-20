#!/usr/bin/env bash
# SessionStart hook: on a fresh install, inject a reminder telling Claude to run the
# onboarding flow (CLAUDE.md "FIRST RUN" gate) before doing anything else. Emits NOTHING
# once setup AND personalization are done. Always exits 0 so it can never break a session.
#
# Pure bash + printf on purpose (NO jq / python dependency): on a brand-new machine those
# may not be installed yet, and this is the very hook that's supposed to get them installed.
# Runs on macOS, Linux, and Windows (Claude Code on Windows runs hooks through Git Bash).
#
# cwd is the project root. Two deterministic states:
#   tools done      = the .setup-complete marker exists (written by ./setup.sh after verify)
#   personalized    = CLAUDE.md contains no <<ALL_CAPS>> placeholder tokens (written by "apply my brand kit")
# An update (update.py) that stopped half way outranks both: it is said first.
#
# NOTE: newlines in the messages are the literal two-character sequence \n (valid JSON string escapes);
# printf %s passes them through verbatim, and the messages hold no " or \ or apostrophe to break the JSON.

TOOLS=0; BRAND=0
[ -f .setup-complete ] && TOOLS=1
if [ -f CLAUDE.md ] && ! grep -qE '<<[A-Z][A-Z0-9_]*(:[^>]*)?>>' CLAUDE.md 2>/dev/null; then BRAND=1; fi

# A set-up project registers itself (update.py keeps the same list), so a new version the user downloads
# and opens by mistake can find it. Windows paths are stored the way Python writes them.
reg="$HOME/.content-os/installs"
if [ "$TOOLS" -eq 1 ]; then
  here="$(pwd -P)"
  command -v cygpath >/dev/null 2>&1 && here="$(cygpath -w "$here")"
  { [ -f "$reg" ] && grep -qxF "$here" "$reg"; } || { mkdir -p "$HOME/.content-os" && printf '%s\n' "$here" >> "$reg"; } 2>/dev/null
fi

msg=''
if [ -f .git/MERGE_HEAD ]; then
  msg='⚠️ AN UPDATE STOPPED ON CONFLICTS and is not finished. Before anything else run: uv run update.py --continue. It lists the files that still hold conflict markers (CLAUDE.md can be one of them, so read it from disk); resolve them per CLAUDE.md § Updating, then run --continue again. uv run update.py --abort cancels the update instead.'
elif [ -f .git/REVERT_HEAD ] || grep -qs '"stopped": "undo"' .git/cos-update-state.json; then
  msg='⚠️ AN UNDO OF THE LAST UPDATE STOPPED ON CONFLICTS and is not finished. Before anything else run: uv run update.py --continue. It lists the files still holding conflict markers; in each, take the before-the-update side, except for later edits the user made, then run --continue again. uv run update.py --abort cancels the undo instead.'
elif [ -f .git/cos-update-state.json ]; then
  # the state file with no MERGE_HEAD / REVERT_HEAD: an update was killed half way (update.py puts it back first)
  msg='⚠️ AN UPDATE WAS INTERRUPTED and is not finished. Before anything else run: uv run update.py again. It puts the interrupted run back first, then updates.'
elif [ "$TOOLS" -eq 0 ] && [ -f check-setup.sh ]; then
  # Another folder on this machine already takes updates: this one is most likely a NEW VERSION the user
  # downloaded and opened, not a second install. Only folders that still exist count.
  others=''
  if [ -f "$reg" ]; then
    while IFS= read -r line || [ -n "$line" ]; do
      line="$(printf '%s' "$line" | tr -d '\r\t')"
      [ -n "$line" ] || continue
      p="$line"; command -v cygpath >/dev/null 2>&1 && p="$(cygpath -u "$line" 2>/dev/null || printf '%s' "$line")"
      [ -f "$p/.setup-complete" ] || continue
      others="${others:+$others; }$line"
    done < "$reg"
    others="$(printf '%s' "$others" | sed 's/\\/\\\\/g; s/"/\\"/g')"
  fi
  if [ -n "$others" ]; then
    msg='⚠️ NEW DOWNLOAD: this folder was never set up, and this machine already has Content OS installed ('"$others"'). If the user wants to UPDATE, do not run setup here: run uv run update.py in this folder (it updates their folder from this download), then tell them to reopen their own folder. Only if they want a second, separate install, follow FIRST RUN in CLAUDE.md.'
  else
    msg='⚠️ FRESH INSTALL: setup has not finished yet (no .setup-complete marker).\n\nFollow the FIRST RUN gate in CLAUDE.md before running any skill:\n  1. Run ./setup.sh yourself (no need to ask). It detects the OS, installs every missing tool, pre-builds the transcription engine + carousel renderer, verifies with ./check-setup.sh, then prints the CONNECTIONS checklist. It is idempotent; re-run it any time.\n  2. Handle its exit codes: 2 = walk the user through restarting Claude Code, then re-run it. 1 = read the output and fix what it names (Homebrew one-liner on macOS, sudo apt lines on Linux; ACTION FOR CLAUDE = do what that line says). 0 = tools done: check which MCPs are already connected (ToolSearch for notion-search, call-actor, tabs_context_mcp) and list only the missing connections, once, in one message.\n  3. Then offer the brand kit (fill brand-kit.md, say apply my brand kit). Personalization is what makes scriptwriter/hooks/carousels sound like the user; the research skills work before it.\n\nIf the user asks for a skill right now, run setup first (nothing transcribes or renders without the tools). If the user says they are UPDATING a Content OS they already use, do not run setup here: run uv run update.py in this folder, which finds their folder and updates it from this download.'
  fi
elif [ "$BRAND" -eq 0 ] && [ -f brand-kit.md ]; then
  msg='ℹ️ Tools are installed but the system is not personalized yet: CLAUDE.md still has ALL-CAPS <<placeholder>> tokens. If the user asks for anything voice- or offer-dependent (scripts, hooks, carousels, captions, DMs, descriptions), first run the brand-kit flow in CLAUDE.md (fill brand-kit.md Part A, then apply it: CLAUDE.md profile, backbone/, competitor-list.md, Notion DB via notion-create-database into notion-pipeline.md, auto-poster .env, then voice-corpus-builder to build voice-corpus/ + voice-dna.md). Research and transcription skills work without it; do not block those.'
fi
if [ -n "$msg" ]; then
  printf '{"hookSpecificOutput":{"hookEventName":"SessionStart","additionalContext":"%s"}}\n' "$msg"
fi

# Unsaved-to-git edits are snapshotted each session (no file is touched), so a new version later unzipped
# OVER this folder cannot silently erase them: update.py restores from the snapshot. Never over a folder
# that already holds a newer VERSION than its last update (that IS the overwrite), and none kept once
# nothing is unsaved.
if [ -f .git/refs/heads/upstream ] || grep -qs 'refs/heads/upstream' .git/packed-refs; then
  if [ "$(git -c safe.directory='*' show HEAD:VERSION 2>/dev/null)" = "$(cat VERSION 2>/dev/null)" ]; then
    snap="$(git -c core.hooksPath=/dev/null -c safe.directory='*' -c core.autocrlf=false stash create 2>/dev/null)"
    if [ -n "$snap" ]; then git -c safe.directory='*' update-ref refs/cos/snapshot "$snap" 2>/dev/null
    else git -c safe.directory='*' update-ref -d refs/cos/snapshot 2>/dev/null; fi
  fi
fi
exit 0
