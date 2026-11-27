#!/usr/bin/env bash
# package-for-client.sh — produce a clean, client-ready zip of the content-os system.
#
# Does NOT mutate the working repo. It stages a copy under packaging/dist/, strips the
# owner's content (research, transcripts, corpus, voice, backbone, outputs, secrets),
# drops in the client onboarding files (overlay/), scrubs personal tokens out of the
# skills, runs leak-checks + spec-sync guards, and zips the result.
#
#   ./packaging/package-for-client.sh            # build + zip → packaging/dist/
#   ./packaging/package-for-client.sh --keep     # also leave the staged folder for inspection
#   ./packaging/package-for-client.sh --no-zip   # stage only, don't zip
#
set -euo pipefail

KEEP=0; DOZIP=1
for a in "$@"; do
  case "$a" in
    --keep)   KEEP=1 ;;
    --no-zip) DOZIP=0 ;;
    *) echo "unknown flag: $a" >&2; exit 1 ;;
  esac
done

PKG_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO="$(cd "$PKG_DIR/.." && pwd)"
OVERLAY="$PKG_DIR/overlay"
DIST="$PKG_DIR/dist"
STAGE="$DIST/content-os"

bold() { printf "\033[1m%s\033[0m\n" "$1"; }
step() { printf "\033[36m▸ %s\033[0m\n" "$1"; }
fail() { printf "\033[31m  ✗ %s\033[0m\n" "$1"; }
okay() { printf "\033[32m  ✓ %s\033[0m\n" "$1"; }

bold "Packaging content-os for client distribution"
echo "  source: $REPO"
echo "  stage:  $STAGE"
echo

rm -rf "$STAGE"
mkdir -p "$STAGE"

# ── 1. Copy the repo, excluding owner content / secrets / junk / the packaging tooling ──
step "Copying repo (excluding owner content, secrets, junk)…"
rsync -a \
  --exclude='.git/' \
  --exclude='.DS_Store' \
  --exclude='__pycache__/' \
  --exclude='*.pyc' \
  --exclude='node_modules/' \
  --exclude='.obsidian/' \
  --exclude='.env' \
  --exclude='.claude/settings.local.json' \
  --exclude='.claude/.DS_Store' \
  --exclude='/packaging/' \
  --exclude='/backbone' \
  --exclude='/business.md' \
  --exclude='/assets/' \
  --exclude='/research/' \
  --exclude='/transcripts/' \
  --exclude='/descriptions/' \
  --exclude='/carousel/' \
  --exclude='/voice-corpus/' \
  --exclude='/voice-dna*.md' \
  --exclude='/knowledge/' \
  --exclude='/outreach/' \
  --exclude='/competitor-list.md' \
  --exclude='/notion-pipeline.md' \
  --exclude='/title-corpus/titles.json' \
  --exclude='/thumbnails/' \
  --exclude='/photos/' \
  --exclude='/sponsors/' \
  --exclude='/AGENTS.md' \
  --exclude='/.codex/' \
  --exclude='/.agents/' \
  --exclude='/reports/' \
  --exclude='/research_notes/' \
  --exclude='/.setup-complete' \
  --exclude='/CLAUDE.md' \
  --exclude='.claude/skills/auto-poster/.env' \
  --exclude='.claude/skills/yt-description/references/links.md' \
  --exclude='.claude/skills/carousel-generator/scripts/package-lock.json' \
  --exclude='.claude/skills/dm-setter-flow/' \
  "$REPO/." "$STAGE/"

# ── 2. Overlay the client onboarding files (CLAUDE.md, SETUP.md, setup.sh, brand-kit, templates, READMEs) ──
step "Applying client overlay (onboarding + templates + empty folders)…"
cp -R "$OVERLAY/." "$STAGE/"
mkdir -p "$STAGE/assets/fonts" && cp "$REPO/assets/fonts/Inter-Black.otf" "$STAGE/assets/fonts/"
chmod +x "$STAGE/setup.sh" "$STAGE/check-setup.sh" "$STAGE/.claude/hooks/setup-check.sh"
# The client's .gitignore is update.py's (it lives outside overlay/ so its rules never apply in this repo).
cp "$PKG_DIR/client.gitignore" "$STAGE/.gitignore"

# 2a. Release notes + version stamp (packaging/RELEASE.md → RELEASE.md + VERSION in the zip)
VERSION="$(grep -m1 '^## ' "$PKG_DIR/RELEASE.md" | sed 's/^## *//')"
[ -n "$VERSION" ] || { echo "packaging/RELEASE.md has no '## <version>' section" >&2; exit 1; }
cp "$PKG_DIR/RELEASE.md" "$STAGE/RELEASE.md"
# The preamble under the title is maintainer instruction; a client reads one line in its place.
perl -0777 -i -pe 's{\A(# [^\n]*\n).*?(?=^## )}{$1\nWhat changed in each version, newest first. To update, download the new zip and tell Claude "update" (SETUP.md § 5).\n\n}ms' "$STAGE/RELEASE.md"
printf '%s\n' "$VERSION" > "$STAGE/VERSION"
okay "release $VERSION (RELEASE.md + VERSION stamped into the package)"

# ── 3. Scrub personal tokens in the staged copy ──
step "Scrubbing personal/brand tokens…"
scrub() {  # scrub <stage-relative-file> <perl-expr>
  local f="$STAGE/$1"; shift
  [ -f "$f" ] && perl -0777 -i -pe "$@" "$f" || true
}

# 3a. Targeted rewrites first (sentences the generic passes would mangle or mis-attribute)
scrub ".claude/skills/scriptwriter/SKILL.md" \
  's/`ai-automations`/`current`/g; s/`viral-content`/`previous`/g; s/--era ai-automations/--era current/g; s/in this corpus/in a fresh corpus/g'
scrub ".claude/skills/dm-revival/SKILL.md" 's/in the AI-automations niche/from an AI-automation creator (swap the topic for your niche)/g'
scrub ".claude/skills/scriptwriter/scripts/find_voice.py" \
  's/--era ai-automations/--era current/g; s/e\.g\. ai-automations, viral-content/e.g. current, previous/g'
scrub ".claude/skills/scriptwriter/scripts/find_voice.py" \
  's/ig-DZGTgwDlcrF/<entry-id>/g'
scrub ".claude/skills/carousel-generator/SKILL.md" \
  's/\(700K, \$190K, 20 hrs\)/(a view count, a dollar figure, hours saved)/g; s/\(700K views, \$190K, 20\+ hrs saved, 177K followers\)/(views, revenue, hours saved, followers: exact numbers from backbone\/messaging.md)/g; s/"attribution": "Albert, member"/"attribution": "a member"/g'
scrub ".claude/skills/auto-poster/SKILL.md" \
  's{/Users/jason/\.\.\./final\.mp4}{/path/to/final.mp4}g; s/names the community \(the Skool community, name per/names the community (exactly as named in/g'
scrub ".claude/skills/yt-description/scripts/fetch_skeleton.sh" \
  's{https://www\.youtube\.com/channel/UCN3tZfcySn-VVeSRdGFIYOA/videos}{}g'
for f in ".claude/skills/yt-feed-research/SKILL.md" ".claude/skills/ig-feed-research/SKILL.md"; do
  scrub "$f" 's{<!-- niche-list:start[^\n]*-->.*?<!-- niche-list:end -->}{(No concrete list ships: derive KEEP/DISMISS on the first run from the Niche line in CLAUDE.md, backbone/icp.md, backbone/offer.md and competitor-list.md, state it in the report, and pin it here once the creator confirms it.)}s'
done
scrub ".claude/skills/idea-capture/SKILL.md" \
  's{```bash\n~/\.local/bin/ntn datasources query.*?```}{`notion-search` with the video id as the query, scoped to the DB (`data_source_url: collection://<Data source ID>` from `notion-pipeline.md`), then `notion-fetch` any hit and confirm its `Source URL` matches.}s; s{"data_source_id":"21bf6585-5e6b-81c2-b536-000b0adc0835"}{"data_source_id":"<Data source ID from notion-pipeline.md>"}g; s{\(the Skool, AI Leverage Lab; never a price, never DM/apply\)}{(the offer in `backbone/offer.md`; never a price, never DM/apply)}g'
scrub ".claude/skills/yt-comment-mining/SKILL.md" \
  's{Jason\x27s own channel is \*\*always\*\* in scope: `\@jasoncooperson`\.}{The creator\x27s own channel is **always** in scope: the YouTube handle in `CLAUDE.md`.}g'
scrub ".claude/skills/thumbnail-generator/SKILL.md" \
  's{> \*\*Home: `~/Projects/content-os` \(moved from `video-editor` 2026-09-04, Jason\x27s call\)\.\*\*}{> **Home: this repo.**}g; s{> ⚠️ \*\*NOT part of the pipeline.*?nothing here was deleted\.\n}{> **On request only.** No pipeline step calls this skill and an edit is complete without a thumbnail. Run it when the user asks for a thumbnail by name, once the final export exists.\n}s; s{Jason is on the \*\*\$49/mo Plus plan — 1000 credits/month\*\*, so 1 credit = \*\*\$0\.049\*\*\.}{Pricing below assumes the **\$49/mo Plus plan (1000 credits/month)**, so 1 credit = **\$0.049**; adjust if your plan differs.}g'
scrub ".claude/skills/knowledge-compile/README.md" 's/Karpathy-style, no Obsidian/compiled, plain markdown/g; s/Karpathy-style/compiled/g'
scrub ".claude/skills/knowledge-compile/SKILL.md" 's/Karpathy-style knowledge layer without Obsidian/compiled knowledge layer (plain markdown)/g; s/Karpathy layer, //g; s/Karpathy-style/compiled/g'

# 3b. Offer platform → generic (the client's offer may not be a Skool)
while IFS= read -r f; do
  perl -0777 -i -pe '
    s/Skool (link|URL|line|ask|CTA|mention)/offer $1/g;
    s/Skool community/community/g;
    s/my Skool\b/my community/g;
    s/the Skool\b/the community/g;
    s/or Skool\b/or the offer/g;
    s/\bSkool\b/community/g;
  ' "$f"
done < <(grep -rIlE '\bSkool\b' "$STAGE" 2>/dev/null || true)

# 3c. Owner name + handle → neutral. Third person ("the creator") keeps verb agreement intact.
while IFS= read -r f; do
  perl -0777 -i -pe '
    s/Jason Cooperson/the creator/g;
    s/\@jasoncooperson/\@yourhandle/g;
    s/\bjasoncooperson\b/yourhandle/g;
    s/Jason\x27s/the creator\x27s/g;
    s/\bJason\b/the creator/g;
    s/\bthe creator, the creator\b/the creator/g;
    s/(^|[.!?]\*{0,2}\s+|\n\n[ \t]*(?:\*\*)?|\n[ \t]*(?:[-*>]\s+|\d+\.\s+|\|\s+)(?:\*\*)?)the creator\b/${1}The creator/g;
  ' "$f"
done < <(grep -rIlE 'Jason|jasoncooperson' "$STAGE" 2>/dev/null || true)

# 3d. Pronouns that referred to the owner → they/their/them (+ the verb forms that actually occur).
#     Scoped to skill docs (prose about the creator); scripts and JSON are left alone.
while IFS= read -r f; do
  perl -0777 -i -pe '
    s/\bhis(?=\s*[.,;!?)]|\s*$)/theirs/mg;
    s/\bhis\b/their/g; s/\bHis\b/Their/g;
    s/\bhimself\b/themselves/g;
    s/\bhim\b/them/g; s/\bHim\b/Them/g;
    s/\bhe\b/they/g; s/\bHe\b/They/g;
    s/\bthey\x27s\b/they\x27re/g;
    s/\b([Tt]hey)(?:\s+(also|explicitly|now|just|already|later|then|actually|deliberately|usually|often))?\s+(ask|say|want|need|finish|open|edit|drop|film|record|review|call|approve|name|mean|dial|leave|hand|point|scan|bring|report|pick|use|prefer|like|wrap|talk|show|make|move|keep|get|run|tag|give|send|reply|redirect|arbitrate|change|decline|confirm|type|paste|read|see|watch|know|think|feel|write|post|film|build|sell|teach|own|pitch|mention|demo|walk|share|leak|speak|sound|go|do|have)s\b/$1 . ($2 ? " $2" : "") . " $3"/ge;
    s/\b([Tt]hey) (is|was)\b/$1 . " " . ($2 eq "is" ? "are" : "were")/ge;
    s/\b([Tt]hey) has\b/$1 have/g;
    s/\b([Tt]hey)((?:\s+(?:also|explicitly|now|just|already|later|then|actually|usually|often)))\s+has\b/$1$2 have/g;
    s/\b([Tt]hey) does\b/$1 do/g;
    s/\b([Tt]hey) goes\b/$1 go/g;
    s/\b([Tt]hey) says\b/$1 say/g;
    s/\b([Tt]hey) wants\b/$1 want/g;
    s/\b([Tt]hey)(?:\s+(also|explicitly|now|just|already|later|then|actually|usually|often))?\s+(pitch|teach|watch|reach|finish|push|catch|miss|touch|fix)es\b/$1 . ($2 ? " $2" : "") . " $3"/ge;
  ' "$f"
done < <(find "$STAGE/.claude/skills" -name '*.md' ! -path '*/hook-generator/reference/structures.md' 2>/dev/null)
# (structures.md is excluded from the pronoun pass: its quoted proof hooks are third-party lines
#  whose he/his must stay verbatim; the file has no owner pronouns of its own.)

# ── 3e. Update fingerprints: LAST change to the stage (§ 5 re-hashes it, so a later edit fails the build) ──
# A client's folder is a git repository so update.py can merge a new version into it (the upstream branch
# holds each version as shipped, the client's branch holds their changes). What makes that exact:
#  · every shipped file is one git tracks: a file the shipped .gitignore hides would never receive an update;
#  · .shipped-history.pack: the TEXT of every shipped file of every version (packaging/shipped-history.pack,
#    frozen, plus this build's own text files), so an install that was never baselined merges each file it
#    changed against the version it started from instead of stopping on a base-less conflict;
#  · .shipped-blobs.json: the git blob id of every file of every version ever shipped, and which one each
#    VERSION carried, so that install can tell a file its owner changed from one they did not. The four
#    versions shipped before updates (no VERSION file) were recovered from Skool and recorded under their
#    ship dates; ship-to-skool.py records each new one;
#  · my-rules.md never changes (the client docs promise no update touches it), and no path changes only in
#    case or turns from a file into a folder (either breaks a merge on a case-insensitive disk).
step "Update fingerprints (.gitignore coverage, .shipped-history.pack, .shipped-blobs.json)…"
UPD_GIT="$(mktemp -d)"
git init -q "$UPD_GIT"
IGNORED="$(cd "$STAGE" && git -c core.excludesFile=/dev/null --git-dir="$UPD_GIT/.git" --work-tree="$STAGE" \
  ls-files --others --ignored --exclude-standard)"
python3 -c 'import shutil,sys; shutil.rmtree(sys.argv[1])' "$UPD_GIT"
if [ -n "$IGNORED" ]; then
  fail "shipped files the shipped .gitignore hides (an update could never reach them):"
  echo "$IGNORED" | sed 's#^#    #'
  echo "    Aborting: exclude them in § 1, or narrow packaging/client.gitignore."
  exit 1
fi
[ -f "$PKG_DIR/shipped-history.pack" ] && [ -f "$PKG_DIR/shipped-blobs.json" ] || {
  fail "packaging/shipped-history.pack or shipped-blobs.json is missing (ship-to-skool.py records both)"; exit 1; }
python3 - "$PKG_DIR/shipped-history.pack" "$STAGE" <<'PY' || exit 1
import os, re, shutil, subprocess, sys, tempfile
frozen, stage = sys.argv[1:3]
# the § 4 leak pattern: the pack is binary, so the text leak-check below never reads it
leak = re.compile(r'jasoncooperson|cooperson|creatoreconomy|leveragelab|UCN3tZfcySn|\bJason\b|21bf6585|Leverage Lab'
                  r'|/Users/jason|\bAlbert\b|\bAyden\b|Karpathy|\$190K|177K|\bSkool\b|taskmaster|~/\.local/bin/ntn', re.I)
t = tempfile.mkdtemp()
try:
    def git(*a, data=None):
        return subprocess.run(['git', '-c', 'core.autocrlf=false', '-C', t, *a], input=data, check=True,
                              capture_output=True).stdout
    git('init', '-q')
    git('index-pack', '--stdin', data=open(frozen, 'rb').read())
    text = []
    for r, _ds, fs in os.walk(stage):
        for f in fs:
            p = os.path.join(r, f)
            if os.path.getsize(p) <= 1_000_000:
                with open(p, 'rb') as fh:
                    if b'\0' not in fh.read(8000):
                        text.append(p)
    git('hash-object', '-w', '--stdin-paths', data='\n'.join(text).encode())
    shas = [l.split()[0] for l in git('cat-file', '--batch-all-objects', '--batch-check').decode().splitlines()
            if l.split()[1] == 'blob']
    out, bad, i = git('cat-file', '--batch', data=('\n'.join(shas) + '\n').encode()), [], 0
    while i < len(out):
        nl = out.index(b'\n', i)
        sha, _kind, size = out[i:nl].decode().split()
        body = out[nl + 1:nl + 1 + int(size)]
        i = nl + 1 + int(size) + 1
        if leak.search(body.decode('utf-8', 'replace')):
            bad.append(sha)
    if bad:
        print('\033[31m  ✗ personal tokens inside .shipped-history.pack (blobs %s)\033[0m' % ', '.join(bad[:5]))
        print('    Aborting: drop those blobs from packaging/shipped-history.pack, or scrub the staged file.')
        sys.exit(1)
    name = git('pack-objects', '--window=250', '--depth=50', os.path.join(t, 'h'), data='\n'.join(shas).encode())
    shutil.copyfile(os.path.join(t, 'h-%s.pack' % name.decode().strip()), os.path.join(stage, '.shipped-history.pack'))
finally:
    shutil.rmtree(t, ignore_errors=True)
PY
python3 - "$PKG_DIR/shipped-blobs.json" "$STAGE" "$VERSION" "$PKG_DIR/RELEASE.md" <<'PY' || exit 1
import hashlib, json, os, re, sys
seed, stage, version, notes = sys.argv[1:5]
data = json.load(open(seed, encoding='utf-8'))
labels = re.findall(r'^## +(\S+)', open(notes, encoding='utf-8').read(), re.M)
if len(labels) > 1 and labels[1] not in data['versions']:
    print('\033[31m  ✗ %s shipped but is not recorded in packaging/shipped-blobs.json (ship-to-skool.py records each '
          'version it uploads). Record it from the zip that shipped:\033[0m' % labels[1])
    print('    unzip -p <that zip> content-os/.shipped-blobs.json > packaging/shipped-blobs.json')
    print('    unzip -p <that zip> content-os/.shipped-history.pack > packaging/shipped-history.pack')
    sys.exit(1)
old = sorted(data['blobs'])     # each version is a list aligned to the sorted paths: an index or -1
shipped = {v: {p: data['blobs'][p][i] for p, i in zip(old, idx) if i >= 0} for v, idx in data['versions'].items()}
blobs = {p: set(v) for p, v in data['blobs'].items()}
mine = {}
for r, _ds, fs in os.walk(stage):
    for f in fs:
        path = os.path.join(r, f)
        rel = os.path.relpath(path, stage).replace(os.sep, '/')
        if rel != '.shipped-blobs.json':
            d = open(path, 'rb').read()
            mine[rel] = hashlib.sha1(b'blob %d\0' % len(d) + d).hexdigest()
fail = []
if 'my-rules.md' in data['blobs'] and mine.get('my-rules.md') not in data['blobs']['my-rules.md']:
    fail.append('my-rules.md changed: every client doc promises no update ever touches it (restore the shipped file)')
folds, oldset = {p.lower(): p for p in old}, set(old)
dirs = {q[:i] for q in old for i in range(len(q)) if q[i] == '/'}
for rel in mine:
    if folds.get(rel.lower(), rel) != rel:
        fail.append('%s differs only in case from the shipped %s (a case-insensitive disk cannot merge that)'
                    % (rel, folds[rel.lower()]))
    if rel in dirs:
        fail.append('%s is a file where a shipped version had a folder' % rel)
    if any(rel[:i] in oldset for i in range(len(rel)) if rel[i] == '/'):
        fail.append('%s sits under a path a shipped version had as a file' % rel)
if fail:
    print('\033[31m  ✗ ' + '\n  ✗ '.join(fail) + '\033[0m')
    sys.exit(1)
if version in shipped and shipped[version] != mine:
    # A bare "update" only takes a NEWER version, so a changed build under a label that already shipped
    # would never reach anyone who has it.
    print('\033[31m  ✗ %s already shipped and this build differs from it: add a new ## <version> section at the top '
          'of packaging/RELEASE.md\033[0m' % version)
    sys.exit(1)
for rel, sha in mine.items():
    blobs.setdefault(rel, set()).add(sha)
shipped.setdefault(version, mine)
paths = sorted(blobs)
data['blobs'] = {p: sorted(blobs[p]) for p in paths}
data['versions'] = {v: [data['blobs'][p].index(m[p]) if p in m else -1 for p in paths] for v, m in sorted(shipped.items())}
with open(os.path.join(stage, '.shipped-blobs.json'), 'w', encoding='utf-8') as fh:
    json.dump(data, fh, indent=0, separators=(',', ':'))
    fh.write('\n')
PY
okay "every shipped file is tracked; history pack $(du -h "$STAGE/.shipped-history.pack" | cut -f1), fingerprints for $(python3 -c 'import json,sys; print(len(json.load(open(sys.argv[1]))["blobs"]))' "$STAGE/.shipped-blobs.json") path(s)"

# ── 4. Leak-check — abort on any personal token that survived ──
step "Leak-check (personal tokens)…"
LEAKS="$(grep -rIlE -i 'jasoncooperson|cooperson|creatoreconomy|leveragelab|UCN3tZfcySn|\bJason\b|21bf6585|Leverage Lab|/Users/jason|\bAlbert\b|\bAyden\b|Karpathy|\$190K|177K|`ai-automations`|`viral-content`|--era ai-automations|\bSkool\b|taskmaster|the creator-calibrated|proven the creator|\ba the creator|niche-list:start|~/\.local/bin/ntn' "$STAGE" 2>/dev/null || true)"
if [ -n "$LEAKS" ]; then
  fail "personal tokens still present in:"
  echo "$LEAKS" | sed 's#^'"$STAGE"'/#    #'
  echo "    Aborting: extend the scrub/exclude rules above."
  exit 1
fi
okay "no personal tokens found"

# 4b. Grammar leak-check: a pronoun swap that left third-person-singular verbs behind
step "Leak-check (pronoun/verb agreement after scrub)…"
GRAM="$(grep -rInE '\b[Tt]hey (?:(?:also|explicitly|now|just|already|later|then|actually|usually|often) )?(is|was|has|does|goes|says|wants|asks|needs|scans|brings|names|hands|reports|picks|calls|approves|leaves|means|owns|pitches|mentions|talks|thinks|knows|feels|sees|writes|posts|films|builds|sells|teaches|watches|finishes|reaches|pushes|trains|uses|likes|prefers|gets|makes|keeps|moves|shows|gives|sends|replies|reads|types|edits|drops|records|reviews|opens|dials|points|redirects|confirms|declines|changes|speaks|sounds|walks|shares|leaks|demos|tags|runs|wraps)\b' "$STAGE/.claude/skills" 2>/dev/null || true)"
if [ -n "$GRAM" ]; then
  fail "verb agreement leftovers:"; echo "$GRAM" | sed 's#^'"$STAGE"'/#    #' | cut -c1-160
  exit 1
fi
okay "no agreement leftovers"

# 4c. Placeholder guard: <<TOKENS>> may only appear in the files brand-kit.md Part B owns
step "Leak-check (placeholders only where onboarding expects them)…"
ALLOWED_PH='^(CLAUDE\.md|brand-kit\.md|SETUP\.md|notion-pipeline\.md|backbone/.*\.md|knowledge/index\.md|\.claude/skills/yt-description/references/links\.md|\.claude/skills/voice-corpus-builder/reference/voice-dna-template\.md|\.claude/hooks/setup-check\.sh)$'
PH_BAD="$(cd "$STAGE" && grep -rIlE '<<[A-Z][A-Z0-9_]*(:[^>]*)?>>' . 2>/dev/null | sed 's#^\./##' | grep -vE "$ALLOWED_PH" || true)"
if [ -n "$PH_BAD" ]; then
  fail "<<placeholders>> in files the brand-kit map doesn't cover:"; echo "$PH_BAD" | sed 's#^#    #'
  exit 1
fi
okay "placeholders confined to onboarding files"

# ── 5. Spec-sync guards — client docs must match the engine they describe ──
step "Verifying package integrity + docs ↔ engine sync…"
sync_ok=1
sfail() { fail "$1"; sync_ok=0; }

# secrets / junk must not ship
[ ! -e "$STAGE/.env" ] || sfail "root .env shipped"
[ ! -e "$STAGE/.claude/skills/auto-poster/.env" ] || sfail "auto-poster .env (live secrets) shipped"
[ -f "$STAGE/.claude/skills/auto-poster/.env.example" ] || sfail "auto-poster .env.example missing"
[ -z "$(find "$STAGE" -name node_modules -o -name __pycache__ -o -name .DS_Store -o -name '*.pyc' 2>/dev/null)" ] || sfail "junk (node_modules/__pycache__/.DS_Store/pyc) shipped"
[ ! -e "$STAGE/.claude/settings.local.json" ] || sfail "settings.local.json shipped"
[ ! -e "$STAGE/.obsidian" ] || sfail ".obsidian shipped"

# every skill present with a frontmatter name matching its folder
for s in auto-poster carousel-generator dm-revival hook-generator idea-capture ig-competitor-research ig-feed-research knowledge-compile manychat-flow recording-studio scriptwriter thumbnail-generator transcribe-url voice-corpus-builder yt-comment-mining yt-competitor-research yt-description yt-feed-research; do
  f="$STAGE/.claude/skills/$s/SKILL.md"
  if [ ! -f "$f" ]; then sfail "skill $s missing"; continue; fi
  head -5 "$f" | grep -q "^name: $s\$" || sfail "$s SKILL.md frontmatter name != folder"
  grep -qF "\`$s\`" "$STAGE/CLAUDE.md" || sfail "client CLAUDE.md doesn't mention $s"
done
# root wiring
[ -x "$STAGE/setup.sh" ] || sfail "setup.sh missing or not executable"
[ -x "$STAGE/check-setup.sh" ] || sfail "check-setup.sh missing or not executable"
[ -x "$STAGE/.claude/hooks/setup-check.sh" ] || sfail "SessionStart hook missing or not executable"
grep -q 'setup-check.sh' "$STAGE/.claude/settings.json" || sfail "settings.json doesn't wire the SessionStart hook"
for gm in "setup.sh" ".claude/hooks/setup-check.sh" "CLAUDE.md"; do
  grep -qF ".setup-complete" "$STAGE/$gm" || sfail "$gm doesn't reference the .setup-complete marker"
done
grep -qF "brand-kit.md" "$STAGE/CLAUDE.md" || sfail "CLAUDE.md gate doesn't reference brand-kit.md"
grep -qF "setup.sh" "$STAGE/SETUP.md" || sfail "SETUP.md doesn't document ./setup.sh"
grep -qF "check-setup.sh" "$STAGE/setup.sh" || sfail "setup.sh doesn't call check-setup.sh"
for pair in "SETUP.md:Git Bash" "SETUP.md:winget install" "SETUP.md:apt install" "CLAUDE.md:Git Bash" "check-setup.sh:winget install" "check-setup.sh:apt install"; do
  gf="${pair%%:*}"; gtok="${pair#*:}"
  grep -qF "$gtok" "$STAGE/$gf" || sfail "$gf is missing the '$gtok' onboarding path"
done
# one whisper engine: setup.sh's venv path must equal every transcribing script's path
VENV_TOKEN='content-os/whisper-venv'
grep -qF "$VENV_TOKEN" "$STAGE/setup.sh" || sfail "setup.sh doesn't pre-build $VENV_TOKEN"
grep -qF "content-os/pillow-venv" "$STAGE/setup.sh" || sfail "setup.sh doesn't pre-build the pillow venv"
grep -qF "content-os/pillow-venv" "$STAGE/check-setup.sh" || sfail "check-setup.sh doesn't report the pillow venv"
grep -q '"PYTHONUTF8": "1"' "$STAGE/.claude/settings.json" || sfail "settings.json lacks PYTHONUTF8=1 (Windows UTF-8)"
grep -qE "grep -qE '<<\[A-Z\]" "$STAGE/.claude/hooks/setup-check.sh" || sfail "hook placeholder check is not token-shaped"
# every shell script must resolve python (Windows: python3 is a Store stub); bare `python3 <cmd>` invocations fail there
BARE_PY="$(grep -rInE '(^|[|;&(]|\$\()\s*python3\s' "$STAGE/.claude/skills" --include='*.sh' 2>/dev/null | grep -vE "python3 -c ''" | cut -d: -f1 | sort -u | sed "s#^$STAGE/##" | tr '\n' ' ' || true)"
[ -z "${BARE_PY% }" ] || sfail "shell scripts still call bare python3 (Windows Store stub): $BARE_PY"
for ws in ".claude/skills/transcribe-url/scripts/transcribe-url.sh" ".claude/skills/ig-competitor-research/scripts/reel-breakdown.sh" ".claude/skills/auto-poster/scripts/transcribe_for_caption.sh" ".claude/skills/yt-description/scripts/chapter_index.sh" ".claude/skills/voice-corpus-builder/scripts/transcribe-file.sh"; do
  [ -f "$STAGE/$ws" ] || { sfail "$ws missing"; continue; }
  grep -qF "$VENV_TOKEN" "$STAGE/$ws" || sfail "$ws doesn't use the shared $VENV_TOKEN"
  grep -qF ".deps-ok" "$STAGE/$ws" || sfail "$ws lacks the .deps-ok sentinel gate"
done
# one hardware-detection helper: every transcribing skill carries the SAME fw_fast.py (canonical: transcribe-url)
for fs in auto-poster ig-competitor-research voice-corpus-builder yt-description; do
  cmp -s "$STAGE/.claude/skills/transcribe-url/scripts/fw_fast.py" "$STAGE/.claude/skills/$fs/scripts/fw_fast.py" \
    || sfail "$fs/scripts/fw_fast.py is missing or differs from transcribe-url's copy (copy it over)"
done
if grep -rIn 'device="auto"' "$STAGE/.claude/skills" --include='*.sh' >/dev/null 2>&1; then
  sfail "a script still calls WhisperModel(device=\"auto\") instead of fw_fast.transcribe"
fi
if grep -rIlE 'whisper\.cpp|whisper-cli|whisper-cpp|cmake' "$STAGE/.claude/skills" >/dev/null 2>&1; then
  sfail "a skill still references whisper.cpp / whisper-cli / cmake: $(grep -rIlE 'whisper\.cpp|whisper-cli|whisper-cpp|cmake' "$STAGE/.claude/skills" | sed 's#^'"$STAGE"'/##' | tr '\n' ' ')"
fi
if grep -rIl 'uv run --with' "$STAGE/.claude/skills" >/dev/null 2>&1; then
  sfail "'uv run --with' still present: $(grep -rIl 'uv run --with' "$STAGE/.claude/skills" | sed 's#^'"$STAGE"'/##' | tr '\n' ' ')"
fi
# no env-token fallbacks
if grep -rIn 'APIFY_TOKEN\|NOTION_TOKEN' "$STAGE" >/dev/null 2>&1; then sfail "env-token reference (APIFY_TOKEN/NOTION_TOKEN) shipped"; fi
# backbone is a real folder of templates, not the owner's symlink
[ -d "$STAGE/backbone" ] && [ ! -L "$STAGE/backbone" ] || sfail "backbone/ is missing or still a symlink"
for b in README vision offer icp messaging; do [ -f "$STAGE/backbone/$b.md" ] || sfail "backbone/$b.md template missing"; done
[ ! -d "$STAGE/backbone/archive" ] || sfail "backbone/archive shipped"
# empty output folders + READMEs
for d in research transcripts/url transcripts/local transcripts/analysis descriptions carousel/outputs voice-corpus knowledge assets/face-refs assets/logos assets/fonts title-corpus thumbnails outreach/dm-revival; do
  [ -d "$STAGE/$d" ] || sfail "folder $d missing from stage"
done
[ -z "$(find "$STAGE/research" "$STAGE/transcripts" "$STAGE/descriptions" "$STAGE/carousel" -type f ! -name 'README.md' ! -name '.gitkeep' 2>/dev/null)" ] || sfail "owner outputs leaked into research/transcripts/descriptions/carousel"
[ -z "$(find "$STAGE/voice-corpus" -type f ! -name 'README.md' 2>/dev/null)" ] || sfail "owner voice corpus leaked"
[ -z "$(find "$STAGE/knowledge" -type f ! -name 'index.md' 2>/dev/null)" ] || sfail "owner knowledge pages leaked"
[ -z "$(find "$STAGE/assets" -type f ! -name 'README.md' ! -path '*/assets/fonts/*' 2>/dev/null)" ] || sfail "owner assets leaked"
[ -f "$STAGE/assets/fonts/Inter-Black.otf" ] || sfail "assets/fonts/Inter-Black.otf (add_title.py fallback font) missing"
[ -z "$(find "$STAGE/assets/fonts" -type f ! -name 'Inter-Black.otf' 2>/dev/null)" ] || sfail "extra fonts shipped (only the OFL Inter face is licensed to ship)"
[ -f "$STAGE/title-corpus/build.py" ] || sfail "title-corpus/build.py missing"
[ ! -e "$STAGE/title-corpus/titles.json" ] || sfail "owner title corpus (titles.json) leaked"
[ -z "$(find "$STAGE/thumbnails" -type f ! -name 'README.md' 2>/dev/null)" ] || sfail "owner thumbnails leaked"
# carousel templates: neutral handle
grep -q '"handle": "@yourhandle"' "$STAGE/.claude/skills/carousel-generator/templates/ai-system-breakdown.json" || sfail "carousel template still carries a personal handle"
# every shipped .sh executable
NOEXEC="$(find "$STAGE" -name '*.sh' ! -perm -u+x 2>/dev/null | sed 's#^'"$STAGE"'/##' | tr '\n' ' ')"
[ -z "${NOEXEC% }" ] || sfail "shell scripts missing exec bit: $NOEXEC"
# every shipped script parses
while IFS= read -r f; do bash -n "$f" 2>/dev/null || sfail "bash -n failed: ${f#$STAGE/}"; done < <(find "$STAGE" -name '*.sh')
while IFS= read -r f; do python3 -c "import ast,sys; ast.parse(open(sys.argv[1]).read())" "$f" 2>/dev/null || sfail "python parse failed: ${f#$STAGE/}"; done < <(find "$STAGE" -name '*.py')
if command -v node >/dev/null 2>&1; then
  while IFS= read -r f; do node --check "$f" 2>/dev/null || sfail "node --check failed: ${f#$STAGE/}"; done < <(find "$STAGE" -name '*.js' -o -name '*.mjs' | grep -v node_modules)
fi
python3 -c "import json,sys; json.load(open(sys.argv[1]))" "$STAGE/.claude/settings.json" 2>/dev/null || sfail "settings.json is not valid JSON"
# brand-kit Part B must name every placeholder-bearing file
for pf in "CLAUDE.md" "backbone/" "competitor-list.md" "notion-pipeline.md" "links.md" "voice-corpus-builder" "title-corpus"; do
  grep -qF "$pf" "$STAGE/brand-kit.md" || sfail "brand-kit.md Part B doesn't cover $pf"
done
# Updates: update.py ships, setup.sh baselines every install with it, the hook routes an unfinished update,
# both client docs route "update" to it, CLAUDE.md loads my-rules.md, and § 3e's fingerprints still describe
# every staged file byte for byte.
[ -f "$STAGE/update.py" ] || sfail "update.py missing from stage root"
[ -f "$STAGE/VERSION" ] && [ -f "$STAGE/RELEASE.md" ] || sfail "VERSION or RELEASE.md missing from stage root"
grep -qF 'update.py --init' "$STAGE/setup.sh" || sfail "setup.sh no longer baselines the install (update.py --init)"
grep -qF 'update.py --find-installs' "$STAGE/setup.sh" || sfail "setup.sh no longer asks before a second install"
grep -qF 'cos-update-state.json' "$STAGE/.claude/hooks/setup-check.sh" || sfail "the hook no longer flags an unfinished update"
grep -qF "$(sed -n "s/^STATE = '\([^']*\)'.*/\1/p" "$STAGE/update.py")" "$STAGE/.claude/hooks/setup-check.sh" \
  || sfail "the hook's update-state file name drifted from update.py's STATE"
grep -qF 'refs/cos/snapshot' "$STAGE/.claude/hooks/setup-check.sh" || sfail "the hook no longer snapshots unsaved edits"
grep -qF 'update.py' "$STAGE/CLAUDE.md" || sfail "CLAUDE.md doesn't document updating with update.py"
grep -qF 'update.py' "$STAGE/SETUP.md" || sfail "SETUP.md doesn't document updating with update.py"
grep -qxF '@my-rules.md' "$STAGE/CLAUDE.md" || sfail "CLAUDE.md doesn't load my-rules.md"
grep -qF 'VERSION' "$STAGE/CLAUDE.md" || sfail "CLAUDE.md doesn't mention the VERSION stamp"
python3 - "$STAGE" <<'PY' || sfail ".shipped-blobs.json is stale: a step after § 3e changed the stage"
import hashlib, json, os, sys
stage = sys.argv[1]
blobs = json.load(open(os.path.join(stage, '.shipped-blobs.json'), encoding='utf-8'))['blobs']
for r, _ds, fs in os.walk(stage):
    for f in fs:
        path = os.path.join(r, f)
        rel = os.path.relpath(path, stage).replace(os.sep, '/')
        d = open(path, 'rb').read()
        if rel != '.shipped-blobs.json' and hashlib.sha1(b'blob %d\0' % len(d) + d).hexdigest() not in blobs.get(rel, ()):
            sys.exit('    changed after fingerprinting: ' + rel)
PY

if [ "$sync_ok" -eq 1 ]; then
  okay "package integrity + docs/engine sync"
else
  echo "    Aborting: fix the items above (overlay/ or scrub rules), then re-run."
  exit 1
fi

# ── 6. Zip ──
SIZE="$(du -sh "$STAGE" | cut -f1)"
echo
bold "Staged clean copy: $SIZE"
if [ "$DOZIP" -eq 1 ]; then
  step "Zipping…"
  ZIP="$DIST/content-os-client.zip"
  rm -f "$ZIP"
  ( cd "$DIST" && zip -rqX "$ZIP" "content-os" -x '*.DS_Store' )
  ZSIZE="$(du -sh "$ZIP" | cut -f1)"
  bold "→ $ZIP  ($ZSIZE, version $VERSION)"
fi

if [ "$KEEP" -eq 0 ] && [ "$DOZIP" -eq 1 ]; then
  rm -rf "$STAGE"
else
  echo "  staged folder kept at: $STAGE"
fi
echo
bold "Done. Hand the client the zip + tell them to open it in Claude Code and say \"run the setup\"."
