"""Offline regression tests for packaging/overlay/update.py, the client updater. Every case builds real
package zips in a temp folder (with the .shipped-blobs.json and .shipped-history.pack the build ships),
installs one the way a client does, changes it the way a client does, and runs the updater as a
subprocess against a hermetic git config and HOME, so what passes here is what a fresh machine gets.

What they hold, each a way an update could silently eat a client's work or strand them on old code:

  * a line only the client changed survives; a line only the package changed lands; a file the
    package retired goes; the client's own files, outputs, .env, .mcp.json and large media are never touched;
  * a bare "update" finds the newest download by the VERSION inside it (a second download is saved as
    "content-os-client (1).zip"), and a stale file named by hand is swapped for the newest;
  * the update always runs on the NEW package's own updater, so a fix to it lands with that version;
  * a spot both changed stops as a conflict with the base shown; --continue refuses while a marker is
    left; --abort puts every byte back and a retry reports the right versions; --undo takes an update
    back out and keeps everything done since; a locked file stops the update before anything changes;
  * the client's own git config (hooks, signing, merge.ff, ownership checks, autocrlf) never breaks it;
  * an install from before update.py existed (no .git, no fingerprints, the old maintainer .gitignore)
    merges each file it changed against the shipped version closest to it, whatever its VERSION says;
  * the new version opened by mistake updates the real project; a damaged or unrelated zip (a video-editor
    one included), the maintainer repo and a stale lock are each handled with a clear line;
  * Content OS's own cases: an install from before VERSION files existed is placed by its files, the output
    folders are never tracked, and new brand-kit fields after an update are named.

    uv run packaging/test_client_update.py
"""
import hashlib
import json
import os
import shutil
import stat
import subprocess
import sys
import tempfile
import time
import unittest
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
UPDATE = HERE / 'overlay' / 'update.py'
GITIGNORE = (HERE / 'client.gitignore').read_text(encoding="utf-8")
DOC = ''.join('line %d\n' % i for i in range(1, 13))
MARKER = '.claude/skills/scriptwriter/SKILL.md'


def blob(data):
    return hashlib.sha1(b'blob %d\0' % len(data) + data).hexdigest()


def raw(t):
    return t.encode() if isinstance(t, str) else t


def put(path, text):
    """Write a fixture byte for byte. A client's editor keeps a shipped file's LF endings; Python's text mode
    writes CRLF on Windows, which would turn every one-line edit here into a whole-file rewrite."""
    Path(path).write_bytes(raw(text))


class Case(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix='cos-update-test-'))
        self.cfg = self.tmp / 'gitconfig'
        put(self.cfg, '')
        self.env = dict(os.environ, HOME=str(self.tmp), GIT_CONFIG_GLOBAL=str(self.cfg), GIT_CONFIG_NOSYSTEM='1',
                        USERPROFILE=str(self.tmp))
        for k in ('GIT_DIR', 'GIT_WORK_TREE', 'GIT_INDEX_FILE', 'GIT_AUTHOR_NAME', 'GIT_AUTHOR_EMAIL',
                  'GIT_COMMITTER_NAME', 'GIT_COMMITTER_EMAIL', 'EMAIL', 'COS_UPDATE_HANDOFF'):
            self.env.pop(k, None)
        self.texts = {}          # version -> {path: bytes} of every package built in this test

    def tearDown(self):
        for r, ds, fs in os.walk(self.tmp):
            for n in ds + fs:
                try:
                    os.chmod(os.path.join(r, n), 0o755)
                except OSError:
                    pass
        shutil.rmtree(self.tmp, ignore_errors=True)

    # ── builders ──────────────────────────────────────────────────────────────
    def package(self, version, files, history=(), updater=True, updater_text=None, name=None, legacy=False):
        """A package zip: files + the scaffolding every real one has. history: earlier versions (built in
        this test) whose files go into its .shipped-blobs.json and .shipped-history.pack, as the build does.
        legacy: a zip from before updates (no VERSION, .gitignore, RELEASE.md or updater), recorded under `version`."""
        d = self.tmp / ('pkg-' + version) / 'content-os'
        base = {'VERSION': version + '\n', 'CLAUDE.md': '# CLAUDE.md\n', 'check-setup.sh': '#!/bin/bash\necho ok\n',
                MARKER: '---\nname: scriptwriter\n---\n', '.gitignore': GITIGNORE,
                'research/README.md': 'Reports land here.\n', 'transcripts/url/.gitkeep': '',
                'RELEASE.md': '# Release notes\n\n## %s\n\n- something new in %s\n' % (version, version)}
        if legacy:
            updater = False
            for k in ('VERSION', '.gitignore', 'RELEASE.md'):
                del base[k]
        if updater:
            base['update.py'] = updater_text or UPDATE.read_text(encoding="utf-8")
        base.update(files)
        for rel, text in base.items():
            p = d / rel
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes(raw(text))
            if rel.endswith('.sh'):
                p.chmod(0o755)
        self.texts[version] = {rel: raw(t) for rel, t in base.items()}
        if updater:
            self.write_history(d, {v: self.texts[v] for v in list(history) + [version]})
        z = self.tmp / (name or 'content-os-client-%s.zip' % version)
        z.parent.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(z, 'w', zipfile.ZIP_DEFLATED) as zf:
            for p in sorted(d.rglob('*')):
                if p.is_file():
                    info = zipfile.ZipInfo('content-os/' + p.relative_to(d).as_posix())
                    info.external_attr = (stat.S_IFREG | (p.stat().st_mode & 0o777)) << 16
                    zf.writestr(info, p.read_bytes())
        return z

    def write_history(self, d, shipped):
        blobs, content = {}, {}
        for m in shipped.values():
            for rel, data in m.items():
                blobs.setdefault(rel, set()).add(blob(data))
                content[blob(data)] = data
        paths = sorted(blobs)
        blist = {p: sorted(blobs[p]) for p in paths}
        versions = {v: [blist[p].index(blob(m[p])) if p in m else -1 for p in paths] for v, m in shipped.items()}
        put(d / '.shipped-blobs.json', json.dumps({'blobs': blist, 'versions': versions}))
        g = Path(tempfile.mkdtemp(dir=self.tmp, prefix='histrepo-'))
        subprocess.run(['git', 'init', '-q', str(g)], env=self.env, check=True)
        for sha, data in content.items():
            (g / sha).write_bytes(data)
        subprocess.run(['git', '-C', str(g), 'hash-object', '-w', '--stdin-paths'], env=self.env, check=True,
                       input='\n'.join(str(g / s) for s in content).encode(), capture_output=True)
        name = subprocess.run(['git', '-C', str(g), 'pack-objects', str(g / 'h')], env=self.env, check=True,
                              input='\n'.join(content).encode(), capture_output=True).stdout.decode().strip()
        shutil.copyfile(g / ('h-%s.pack' % name), d / '.shipped-history.pack')

    def install(self, z, name='client', setup=True):
        dest = self.tmp / name
        with zipfile.ZipFile(z) as zf:
            for info in zf.infolist():
                t = dest / info.filename.split('/', 1)[1]
                t.parent.mkdir(parents=True, exist_ok=True)
                t.write_bytes(zf.read(info))
                t.chmod((info.external_attr >> 16) & 0o777)
        if setup:
            put(dest / '.setup-complete', '')
        return dest

    def run_update(self, project, *args, script=None, env=None):
        r = subprocess.run([sys.executable, str(script or project / 'update.py'), *map(str, args)],
                           cwd=str(project), env=dict(self.env, **(env or {})), capture_output=True, text=True,
                           encoding='utf-8')     # update.py prints UTF-8 on every OS, whatever the locale's codepage
        return r.returncode, r.stdout + r.stderr

    def git(self, project, *args):
        return subprocess.run(['git', *args], cwd=str(project), env=self.env, capture_output=True,
                              text=True, encoding='utf-8').stdout.strip()

    def assertClean(self, project):
        self.assertEqual(self.git(project, 'status', '--porcelain'), '')

    # ── fixtures ──────────────────────────────────────────────────────────────
    V1 = {'doc.md': DOC, 'tool.sh': '#!/bin/bash\necho v1\n', 'retired.md': 'old\n', 'keep.md': 'keep\n',
          'presets/x/style.md': 'x style v1\n'}

    def v2_files(self, **over):
        f = dict(self.V1)
        f['doc.md'] = DOC.replace('line 10\n', 'line 10 (package)\n')
        f['tool.sh'] = '#!/bin/bash\necho v2\n'
        f['new.md'] = 'new in v2\n'
        del f['retired.md']
        f.update(over)
        return f

    def fresh(self):
        p = self.install(self.package('2026.09.01', self.V1))
        rc, out = self.run_update(p, '--init')
        self.assertEqual(rc, 0, out)
        return p

    def v2(self, **over):
        return self.package('2026.09.02', self.v2_files(**over), history=['2026.09.01'])


class FreshInstall(Case):
    def test_init_baselines_and_is_idempotent(self):
        p = self.fresh()
        self.assertTrue(self.git(p, 'rev-parse', '--verify', 'refs/heads/upstream'))
        self.assertEqual(self.git(p, 'rev-parse', 'HEAD'), self.git(p, 'rev-parse', 'refs/heads/upstream'))
        self.assertClean(p)
        self.assertIn(str(p.resolve()), (self.tmp / '.content-os' / 'installs').read_text(encoding="utf-8"))
        rc, out = self.run_update(p, '--init')
        self.assertEqual(rc, 0, out)
        self.assertIn('already set up', out)

    def test_both_sides_land(self):
        p = self.fresh()
        put(p / 'doc.md', DOC.replace('line 2\n', 'line 2 (mine)\n'))
        (p / 'presets/mine').mkdir(parents=True)
        put(p / 'presets/mine/style.md', 'my own preset\n')
        (p / 'keep.md').unlink()
        put(p / 'research/YT-Research_2026-09-01.html', '<html>report</html>\n')
        put(p / 'transcripts/url/talk_2026-09-01.md', 'a transcript\n')
        put(p / '.env', 'KEY=secret\n')
        put(p / '.mcp.json', '{"machine": "local"}\n')
        rc, out = self.run_update(p, self.v2())
        self.assertEqual(rc, 0, out)
        doc = (p / 'doc.md').read_text(encoding="utf-8")
        self.assertIn('line 2 (mine)', doc)
        self.assertIn('line 10 (package)', doc)
        self.assertEqual((p / 'presets/mine/style.md').read_text(encoding="utf-8"), 'my own preset\n')
        self.assertFalse((p / 'keep.md').exists(), 'a file the client deleted came back')
        self.assertFalse((p / 'retired.md').exists(), 'a file the package retired survived')
        self.assertEqual((p / 'new.md').read_text(encoding="utf-8"), 'new in v2\n')
        self.assertEqual((p / 'tool.sh').read_text(encoding="utf-8"), '#!/bin/bash\necho v2\n')
        if os.name != 'nt':
            self.assertTrue(os.access(p / 'tool.sh', os.X_OK), 'the update dropped the exec bit')
        self.assertEqual((p / 'research/YT-Research_2026-09-01.html').read_text(encoding="utf-8"), '<html>report</html>\n')
        self.assertEqual((p / '.env').read_text(encoding="utf-8"), 'KEY=secret\n')
        self.assertEqual((p / '.mcp.json').read_text(encoding="utf-8"), '{"machine": "local"}\n')
        self.assertEqual((p / 'VERSION').read_text(encoding="utf-8").strip(), '2026.09.02')
        self.assertClean(p)
        self.assertEqual(self.git(p, 'ls-files', 'research/YT-Research_2026-09-01.html',
                                  'transcripts/url/talk_2026-09-01.md', '.env', '.mcp.json'), '')
        self.assertTrue(self.git(p, 'rev-parse', '--verify', 'refs/tags/before-update-2026.09.02'))
        self.assertIn('2026.09.01 → 2026.09.02', out)
        self.assertIn('something new in 2026.09.02', out)
        self.assertIn('doc.md', out, 'the report should name the files carrying the client\'s changes')
        self.assertIn('/clear', out, 'the report should say to load the new instructions')

    def test_bare_update_finds_the_newest_download_by_version(self):
        p = self.fresh()
        dl = self.tmp / 'Downloads'
        self.package('2026.09.01', self.V1, name='Downloads/content-os-client.zip')
        self.package('2026.09.02', self.v2_files(), history=['2026.09.01'], name='Downloads/content-os-client (1).zip')
        rc, out = self.run_update(p)
        self.assertEqual(rc, 0, out)
        self.assertIn('content-os-client (1).zip', out)
        self.assertEqual((p / 'VERSION').read_text(encoding="utf-8").strip(), '2026.09.02')
        # the canonical name now holds a stale copy: naming it by hand still reaches the newest
        self.package('2026.09.03', self.v2_files(**{'new.md': 'v3\n'}), history=['2026.09.01', '2026.09.02'],
                     name='Downloads/content-os-client (2).zip')
        rc, out = self.run_update(p, dl / 'content-os-client.zip')
        self.assertEqual(rc, 0, out)
        self.assertIn('not newer than this project', out)
        self.assertEqual((p / 'VERSION').read_text(encoding="utf-8").strip(), '2026.09.03')
        rc, out = self.run_update(p)
        self.assertEqual(rc, 1, out)
        self.assertIn('no newer version found', out)

    def test_same_zip_twice_is_a_noop_and_older_is_refused(self):
        p = self.fresh()
        z2 = self.v2()
        self.assertEqual(self.run_update(p, z2)[0], 0)
        head = self.git(p, 'rev-parse', 'HEAD')
        put(p / 'doc.md', DOC.replace('line 1\n', 'line 1 (pending edit)\n'))
        rc, out = self.run_update(p, z2)
        self.assertEqual(rc, 0, out)
        self.assertIn('Already up to date', out)
        self.assertEqual(self.git(p, 'rev-parse', 'HEAD'), head, 'a no-op run must not commit anything')
        rc, out = self.run_update(p, self.package('2026.08.30', self.V1))
        self.assertEqual(rc, 1, out)
        self.assertIn('older', out)
        self.assertNotIn('--force', out, 'the refusal must never suggest a downgrade')
        self.assertEqual(self.git(p, 'rev-parse', 'HEAD'), head)

    def test_unzipped_folder_works_as_source(self):
        p = self.fresh()
        folder = self.install(self.v2(), 'downloads-unzipped', setup=False)
        rc, out = self.run_update(p, os.path.relpath(folder, p))    # a relative path, as a person types it
        self.assertEqual(rc, 0, out)
        self.assertEqual((p / 'VERSION').read_text(encoding="utf-8").strip(), '2026.09.02')

    def test_autocrlf_true_never_writes_crlf(self):
        put(self.cfg, '[core]\n\tautocrlf = true\n')   # what Git for Windows ships
        p = self.fresh()
        put(p / 'doc.md', DOC.replace('line 2\n', 'line 2 (mine)\n'))
        rc, out = self.run_update(p, self.v2())
        self.assertEqual(rc, 0, out)
        for f in ('tool.sh', 'doc.md', 'new.md'):
            self.assertNotIn(b'\r\n', (p / f).read_bytes(), f)

    def test_the_clients_own_git_config_never_breaks_it(self):
        hooks = self.tmp / 'hooks'
        hooks.mkdir()
        for h in ('pre-commit', 'commit-msg', 'pre-merge-commit', 'post-merge'):
            put(hooks / h, '#!/bin/sh\necho HOOK-RAN >&2\nexit 1\n')
            (hooks / h).chmod(0o755)
        # as_posix: git reads a backslash in a config value as an escape, so a C:\Users\... path is a bad config line
        put(self.cfg, '[core]\n\thooksPath = %s\n[commit]\n\tgpgsign = true\n[gpg]\n\tprogram = false\n'
                      '[merge]\n\tff = only\n\tconflictStyle = zdiff3\n[init]\n\tdefaultBranch = trunk\n' % hooks.as_posix())
        p = self.fresh()
        put(p / 'doc.md', DOC.replace('line 2\n', 'line 2 (mine)\n'))
        rc, out = self.run_update(p, self.v2(), env={'GIT_TEST_ASSUME_DIFFERENT_OWNER': '1'})
        self.assertEqual(rc, 0, out)
        self.assertNotIn('HOOK-RAN', out)
        self.assertEqual((p / 'VERSION').read_text(encoding="utf-8").strip(), '2026.09.02')

    def test_large_media_stays_out_of_git(self):
        p = self.fresh()
        (p / 'presets/x/broll.mov').write_bytes(b'\0' * (51 * 1024 * 1024))
        (p / 'take.MOV').write_bytes(b'\0' * 1024)          # media at the top is ignored whatever its size
        rc, out = self.run_update(p, self.v2())
        self.assertEqual(rc, 0, out)
        self.assertIn('presets/x/broll.mov', out)
        self.assertEqual(self.git(p, 'ls-files', 'presets/x/broll.mov', 'take.MOV'), '')
        self.assertEqual((p / 'presets/x/broll.mov').stat().st_size, 51 * 1024 * 1024)
        self.assertClean(p)

    def test_the_new_versions_own_updater_runs_the_update(self):
        p = self.fresh()
        marked = UPDATE.read_text(encoding="utf-8").replace('import argparse\n', "print('NEW-UPDATER-RAN')\nimport argparse\n", 1)
        rc, out = self.run_update(p, self.package('2026.09.02', self.v2_files(), history=['2026.09.01'],
                                                  updater_text=marked))
        self.assertEqual(rc, 0, out)
        self.assertIn('NEW-UPDATER-RAN', out)
        self.assertEqual((p / 'update.py').read_text(encoding="utf-8"), marked)

    def test_a_download_opened_by_mistake_updates_the_real_project(self):
        p = self.fresh()
        d = self.install(self.v2(), 'Downloads/content-os', setup=False)
        rc, out = self.run_update(d)
        self.assertEqual(rc, 0, out)
        self.assertIn('never set up', out)
        self.assertEqual((p / 'VERSION').read_text(encoding="utf-8").strip(), '2026.09.02')
        self.assertFalse((d / '.git').exists(), 'the download itself must stay untouched')

    def test_damaged_and_unrelated_downloads_are_refused(self):
        p = self.fresh()
        z = self.v2()
        bad = self.tmp / 'broken.zip'
        data = z.read_bytes()
        bad.write_bytes(data[:len(data) // 2])
        rc, out = self.run_update(p, bad)
        self.assertEqual(rc, 1, out)
        self.assertIn('download it again', out)
        other = self.tmp / 'other-kit.zip'
        with zipfile.ZipFile(other, 'w') as zf:
            zf.writestr('some-kit/VERSION', '2027.01.01\n')
            zf.writestr('some-kit/CLAUDE.md', '# other\n')
        rc, out = self.run_update(p, other)
        self.assertEqual(rc, 1, out)
        ve = self.tmp / 'content-os-client.zip'
        with zipfile.ZipFile(ve, 'w') as zf:
            for f, t in (('VERSION', '2027.01.01\n'), ('CLAUDE.md', '# editor\n'), ('check-setup.sh', 'echo\n'),
                         ('update.py', '#\n')):
                zf.writestr('video-editor/' + f, t)
        rc, out = self.run_update(p, ve)
        self.assertEqual(rc, 1, out)
        self.assertIn('not a Content OS download', out)
        self.assertEqual((p / 'VERSION').read_text(encoding="utf-8").strip(), '2026.09.01')
        self.assertClean(p)

    def test_a_stale_lock_from_an_interrupted_run_is_cleared(self):
        p = self.fresh()
        lock = p / '.git' / 'index.lock'
        put(lock, '')
        old = time.time() - 600
        os.utime(lock, (old, old))
        rc, out = self.run_update(p, self.v2())
        self.assertEqual(rc, 0, out)
        self.assertIn('interrupted', out)


class Conflicts(Case):
    def conflicted(self):
        p = self.fresh()
        put(p / 'doc.md', DOC.replace('line 5\n', 'line 5 (mine)\n'))
        z = self.v2(**{'doc.md': DOC.replace('line 5\n', 'line 5 (package)\n')})
        rc, out = self.run_update(p, z)
        self.assertEqual(rc, 3, out)
        self.assertIn('doc.md', out)
        return p, z

    def test_stops_with_base_then_continue(self):
        p, _ = self.conflicted()
        doc = (p / 'doc.md').read_text(encoding="utf-8")
        for marker in ('<<<<<<< HEAD', '|||||||', '>>>>>>> '):
            self.assertIn(marker, doc)
        self.assertIn('line 5 (mine)', doc)
        self.assertIn('line 5 (package)', doc)
        self.assertEqual((p / 'new.md').read_text(encoding="utf-8"), 'new in v2\n', 'the rest of the update must already be in')
        rc, out = self.run_update(p, '--continue')
        self.assertEqual(rc, 3, 'continue must refuse while markers remain\n' + out)
        put(p / 'doc.md', DOC.replace('line 5\n', 'line 5 (mine + package)\n'))
        rc, out = self.run_update(p, '--continue')
        self.assertEqual(rc, 0, out)
        self.assertClean(p)
        self.assertEqual(len(self.git(p, 'rev-list', '--parents', '-n1', 'HEAD').split()), 3)
        self.assertIn('line 5 (mine + package)', (p / 'doc.md').read_text(encoding="utf-8"))

    def test_abort_puts_every_byte_back_and_a_retry_reports_right(self):
        p = self.fresh()
        put(p / 'doc.md', DOC.replace('line 5\n', 'line 5 (mine)\n'))
        snap = {f: (p / f).read_bytes() for f in ('doc.md', 'tool.sh', 'retired.md', 'VERSION')}
        z = self.v2(**{'doc.md': DOC.replace('line 5\n', 'line 5 (package)\n')})
        self.assertEqual(self.run_update(p, z)[0], 3)
        rc, out = self.run_update(p, '--abort')
        self.assertEqual(rc, 0, out)
        for f, data in snap.items():
            self.assertEqual((p / f).read_bytes(), data, f)
        self.assertFalse((p / 'new.md').exists())
        rc, out = self.run_update(p, z)
        self.assertEqual(rc, 3, 'the same update must be retryable after an abort')
        self.assertIn('2026.09.01 → 2026.09.02', out)
        mine = [l for l in out.splitlines() if 'Your own changes' in l][0]
        self.assertNotIn('VERSION', mine, 'the new version\'s files are not the user\'s changes')

    def test_undo_takes_the_update_back_and_keeps_later_work(self):
        p = self.fresh()
        z = self.v2()
        self.assertEqual(self.run_update(p, z)[0], 0)
        put(p / 'presets/x/style.md', 'x style v1\nmy tweak after the update\n')
        rc, out = self.run_update(p, '--undo')
        self.assertEqual(rc, 0, out)
        self.assertEqual((p / 'VERSION').read_text(encoding="utf-8").strip(), '2026.09.01')
        self.assertEqual((p / 'tool.sh').read_text(encoding="utf-8"), '#!/bin/bash\necho v1\n')
        self.assertFalse((p / 'new.md').exists())
        self.assertIn('my tweak after the update', (p / 'presets/x/style.md').read_text(encoding="utf-8"))
        self.assertClean(p)
        rc, out = self.run_update(p, z)
        self.assertEqual(rc, 0, 'the undone version must be takeable again\n' + out)
        self.assertEqual((p / 'VERSION').read_text(encoding="utf-8").strip(), '2026.09.02')
        self.assertIn('my tweak after the update', (p / 'presets/x/style.md').read_text(encoding="utf-8"))

    def test_a_locked_file_stops_the_update_before_anything_changes(self):
        p = self.fresh()
        (p / 'tool.sh').chmod(0o555)
        rc, out = self.run_update(p, self.v2())
        self.assertEqual(rc, 1, out)
        self.assertIn('tool.sh', out)
        self.assertEqual((p / 'VERSION').read_text(encoding="utf-8").strip(), '2026.09.01')
        self.assertFalse((p / 'new.md').exists())
        (p / 'tool.sh').chmod(0o755)
        rc, out = self.run_update(p, self.v2())
        self.assertEqual(rc, 0, out)
        self.assertIn('2026.09.01 → 2026.09.02', out)


class PreUpdateInstall(Case):
    """An install from before update.py existed: no .git, no fingerprints, the maintainer .gitignore."""
    OLD_GITIGNORE = '/projects/\n/vendor/\n.env\n/.mcp.json\npresets/youtube/default/backgrounds/renders/\n'

    def old_install(self, files=None, version='2026.09.01'):
        files = dict(files or self.V1, **{'.gitignore': self.OLD_GITIGNORE})
        p = self.install(self.package(version, files, updater=False), 'old-' + version)
        self.assertFalse((p / '.git').exists())
        return p

    def test_baselines_against_every_shipped_version(self):
        p = self.old_install(dict(self.V1, **{'touched.md': 'shipped\n', 'both.md': DOC, 'retired-touched.md': 'gone soon\n'}))
        self.package('2026.08.20', {'frank.md': 'frank as an older version shipped it\n'}, updater=False)
        put(p / 'frank.md', 'frank as an older version shipped it\n')
        put(p / 'touched.md', 'my rewrite\n')                            # the package leaves it alone
        put(p / 'both.md', DOC.replace('line 3\n', 'line 3 (mine)\n'))  # the package changes it too
        put(p / 'retired-touched.md', 'I use this\n')                    # the package retires it
        put(p / 'mine.md', 'my own file\n')
        put(p / 'research/old-report.html', 'report\n')
        v2 = self.v2_files(**{'touched.md': 'shipped\n', 'both.md': DOC.replace('line 9\n', 'line 9 (package)\n'),
                             'frank.md': 'frank v2\n'})
        rc, out = self.run_update(p, self.package('2026.09.02', v2, history=['2026.08.20', '2026.09.01']), script=UPDATE)
        self.assertEqual(rc, 0, out)       # nothing to decide: every changed file had its shipped base on hand
        self.assertIn('retired these, but the user had changed them', out)
        both = (p / 'both.md').read_text(encoding="utf-8")
        self.assertIn('line 3 (mine)', both, 'a changed file merges against its shipped base: no conflict')
        self.assertIn('line 9 (package)', both)
        self.assertIn('line 10 (package)', (p / 'doc.md').read_text(encoding="utf-8"), 'an unchanged file must take the new version')
        self.assertEqual((p / 'frank.md').read_text(encoding="utf-8"), 'frank v2\n', 'a file matching ANY shipped version is unchanged')
        self.assertEqual((p / 'touched.md').read_text(encoding="utf-8"), 'my rewrite\n')
        self.assertEqual((p / 'retired-touched.md').read_text(encoding="utf-8"), 'I use this\n')
        self.assertFalse((p / 'retired.md').exists())
        self.assertEqual((p / 'mine.md').read_text(encoding="utf-8"), 'my own file\n')
        self.assertEqual((p / 'research/old-report.html').read_text(encoding="utf-8"), 'report\n')
        self.assertEqual((p / 'update.py').read_text(encoding="utf-8"), UPDATE.read_text(encoding="utf-8"), 'the updater itself must arrive')
        self.assertClean(p)
        self.assertEqual((p / '.gitignore').read_text(encoding="utf-8"), GITIGNORE, 'the new ignore rules must replace the old')

    def test_a_changed_file_merges_against_the_version_it_came_from_whatever_VERSION_says(self):
        # A careful hand-merge left the folder: VERSION and every untouched file are 09.05's, but the one file
        # the user edited was kept as 09.01's. Trusting VERSION would treat 09.05 as its base and keep the
        # old text silently; its closest shipped form is 09.01's, so the package's later lines land.
        old = DOC
        mid = DOC.replace('line 7\n', 'line 7 (09.05)\n')
        new = mid.replace('line 11\n', 'line 11 (09.06)\n')
        p = self.old_install(dict(self.V1, **{'guide.md': old}), '2026.09.01')
        self.package('2026.09.05', dict(self.V1, **{'guide.md': mid}), updater=False)
        put(p / 'VERSION', '2026.09.05\n')
        put(p / 'guide.md', old.replace('line 2\n', 'line 2 (mine)\n'))
        z = self.package('2026.09.06', dict(self.V1, **{'guide.md': new}), history=['2026.09.01', '2026.09.05'])
        rc, out = self.run_update(p, z, script=UPDATE)
        self.assertEqual(rc, 0, out)
        g = (p / 'guide.md').read_text(encoding="utf-8")
        for line in ('line 2 (mine)', 'line 7 (09.05)', 'line 11 (09.06)'):
            self.assertIn(line, g)

    def test_a_shipped_file_the_user_deleted_stays_deleted(self):
        p = self.old_install()
        (p / 'keep.md').unlink()
        rc, out = self.run_update(p, self.v2(), script=UPDATE)
        self.assertEqual(rc, 0, out)
        self.assertFalse((p / 'keep.md').exists())
        self.assertClean(p)

    def test_existing_client_repo_keeps_its_history_and_tracked_jobs(self):
        p = self.old_install()
        (p / 'research/job1').mkdir(parents=True)
        put(p / 'research/job1/cuts.json', '{}\n')
        for args in (('init', '-q'), ('config', 'user.name', 'Client'), ('config', 'user.email', 'c@example.com'),
                     ('add', '-A'), ('add', '-f', 'research/job1/cuts.json'), ('commit', '-qm', 'my own history')):
            subprocess.run(['git', *args], cwd=str(p), env=self.env, check=True, capture_output=True)
        mine = self.git(p, 'rev-parse', 'HEAD')
        rc, out = self.run_update(p, self.v2(), script=UPDATE)
        self.assertEqual(rc, 0, out)
        self.assertEqual(subprocess.run(['git', 'merge-base', '--is-ancestor', mine, 'HEAD'], cwd=str(p),
                                        env=self.env).returncode, 0, 'the client\'s own commits must stay in history')
        self.assertEqual(self.git(p, 'ls-files', 'research/job1/cuts.json'), 'research/job1/cuts.json',
                         'a file the client tracked must stay tracked')
        self.assertIn('line 10 (package)', (p / 'doc.md').read_text(encoding="utf-8"))
        self.assertClean(p)


class RoundTwo(Case):
    """What the second round of client simulations broke (2026-09-25)."""

    def conflict_on(self, p, line=5):
        put(p / 'doc.md', DOC.replace('line %d\n' % line, 'line %d (mine)\n' % line))
        z = self.v2(**{'doc.md': DOC.replace('line %d\n' % line, 'line %d (package)\n' % line)})
        rc, out = self.run_update(p, z)
        self.assertEqual(rc, 3, out)
        return z

    def test_work_done_while_an_update_is_stopped_survives_an_undo(self):
        p = self.fresh()
        self.conflict_on(p)
        put(p / 'my-rules.md', 'a rule written mid-update\n')
        (p / 'presets/mine').mkdir(parents=True)
        put(p / 'presets/mine/mid.md', 'made mid-update\n')
        put(p / 'doc.md', DOC.replace('line 5\n', 'line 5 (both)\n'))
        rc, out = self.run_update(p, '--continue')
        self.assertEqual(rc, 0, out)
        self.assertNotIn('mid.md', self.git(p, 'show', '--stat', '--format=', 'HEAD^'), 'the update commit took the user\'s side work')
        rc, out = self.run_update(p, '--undo')
        self.assertEqual(rc, 0, out)
        self.assertEqual((p / 'my-rules.md').read_text(encoding="utf-8"), 'a rule written mid-update\n')
        self.assertEqual((p / 'presets/mine/mid.md').read_text(encoding="utf-8"), 'made mid-update\n')
        self.assertEqual((p / 'VERSION').read_text(encoding="utf-8").strip(), '2026.09.01')
        self.assertClean(p)

    def test_rerere_in_the_clients_config_never_blocks_a_re_update(self):
        put(self.cfg, '[rerere]\n\tenabled = true\n\tautoupdate = true\n')
        p = self.fresh()
        z = self.conflict_on(p)
        put(p / 'doc.md', DOC.replace('line 5\n', 'line 5 (both)\n'))
        self.assertEqual(self.run_update(p, '--continue')[0], 0)
        self.assertEqual(self.run_update(p, '--undo')[0], 0)
        rc, out = self.run_update(p, z)
        self.assertIn(rc, (0, 3), out)
        self.assertNotIn('could not finish', out)

    def test_undo_conflicts_say_undo_and_the_sides_are_named_right(self):
        p = self.fresh()
        self.assertEqual(self.run_update(p, self.v2())[0], 0)
        put(p / 'doc.md', (p / 'doc.md').read_text(encoding="utf-8").replace('line 10 (package)', 'line 10 (package, then mine)'))
        rc, out = self.run_update(p, '--undo')
        self.assertEqual(rc, 3, out)
        self.assertIn('The undo stopped', out)
        self.assertIn('before the update', out)
        rc, out = self.run_update(p, '--abort')
        self.assertEqual(rc, 0, out)
        self.assertIn('line 10 (package, then mine)', (p / 'doc.md').read_text(encoding="utf-8"))
        self.assertEqual((p / 'VERSION').read_text(encoding="utf-8").strip(), '2026.09.02')
        self.assertClean(p)

    def test_a_binary_conflict_is_settled_with_keep_mine_or_take_new(self):
        p = self.install(self.package('2026.09.01', dict(self.V1, **{'assets/fx.wav': b'RIFF\0\0v1'})))
        self.assertEqual(self.run_update(p, '--init')[0], 0)
        (p / 'assets/fx.wav').write_bytes(b'RIFF\0\0mine')
        rc, out = self.run_update(p, self.package('2026.09.02', self.v2_files(**{'assets/fx.wav': b'RIFF\0\0v2'}),
                                                  history=['2026.09.01']))
        self.assertEqual(rc, 3, out)
        self.assertIn('--keep-mine', out)
        rc, out = self.run_update(p, '--continue')
        self.assertEqual(rc, 3, 'a binary conflict must be settled, not kept silently\n' + out)
        self.assertEqual(self.run_update(p, '--take-new', 'assets/fx.wav')[0], 0)
        self.assertEqual(self.run_update(p, '--continue')[0], 0)
        self.assertEqual((p / 'assets/fx.wav').read_bytes(), b'RIFF\0\0v2')
        self.assertClean(p)

    def test_a_conflict_from_a_redirected_update_is_finished_from_the_download(self):
        p = self.fresh()
        put(p / 'doc.md', DOC.replace('line 5\n', 'line 5 (mine)\n'))
        d = self.install(self.v2(**{'doc.md': DOC.replace('line 5\n', 'line 5 (package)\n')}),
                         'Downloads/content-os', setup=False)
        rc, out = self.run_update(d)
        self.assertEqual(rc, 3, out)
        self.assertIn('--project "%s"' % p.resolve(), out)
        put(p / 'doc.md', DOC.replace('line 5\n', 'line 5 (both)\n'))
        rc, out = self.run_update(d, '--continue')
        self.assertEqual(rc, 0, out)
        self.assertIn('open that folder in Claude Code', out)
        self.assertEqual((p / 'VERSION').read_text(encoding="utf-8").strip(), '2026.09.02')

    def test_downloads_it_cannot_use_are_named(self):
        p = self.fresh()
        z = self.package('2026.09.02', self.v2_files(), history=['2026.09.01'], name='store/v2.zip')
        broken = self.tmp / 'Downloads' / 'content-os-client (1).zip'
        broken.parent.mkdir(parents=True)
        broken.write_bytes(z.read_bytes()[:4000])
        rc, out = self.run_update(p)
        self.assertEqual(rc, 1, out)
        self.assertIn('still downloading', out)
        shutil.copyfile(z, p / 'content-os-client.zip')          # dropped into the project folder itself
        rc, out = self.run_update(p)
        self.assertEqual(rc, 0, out)
        self.assertEqual((p / 'VERSION').read_text(encoding="utf-8").strip(), '2026.09.02')
        self.assertEqual(self.git(p, 'ls-files', 'content-os-client.zip'), '')

    def test_abort_puts_a_moved_aside_file_back(self):
        p = self.install(self.package('2026.09.01', dict(self.V1, **{'.gitignore': GITIGNORE + 'presets/keep/\n'})))
        self.assertEqual(self.run_update(p, '--init')[0], 0)
        (p / 'presets/keep').mkdir(parents=True)
        put(p / 'presets/keep/look.md', 'mine\n')
        put(p / 'doc.md', DOC.replace('line 5\n', 'line 5 (mine)\n'))
        z = self.package('2026.09.02', self.v2_files(**{'doc.md': DOC.replace('line 5\n', 'line 5 (package)\n'),
                                                     'presets/keep/look.md': 'shipped\n'}), history=['2026.09.01'])
        rc, out = self.run_update(p, z)
        self.assertEqual(rc, 3, out)
        self.assertTrue((p / 'presets/keep/look (yours).md').exists())
        self.assertEqual(self.run_update(p, '--abort')[0], 0)
        self.assertEqual((p / 'presets/keep/look.md').read_text(encoding="utf-8"), 'mine\n')
        self.assertFalse((p / 'presets/keep/look (yours).md').exists())

    def test_the_download_the_updater_runs_from_is_used_when_downloads_is_empty(self):
        p = self.fresh()
        d = self.install(self.v2(), 'elsewhere/New Editor', setup=False)
        rc, out = self.run_update(p, script=d / 'update.py')
        self.assertEqual(rc, 0, out)
        self.assertEqual((p / 'VERSION').read_text(encoding="utf-8").strip(), '2026.09.02')

    def test_a_pre_update_install_is_found_when_its_download_is_opened(self):
        p = self.install(self.package('2026.09.01', dict(self.V1, **{'.gitignore': '/projects/\n'}), updater=False),
                         'Documents/content-os')
        d = self.install(self.v2(), 'Downloads/content-os', setup=False)
        rc, out = self.run_update(d)
        self.assertEqual(rc, 0, out)
        self.assertEqual((p / 'VERSION').read_text(encoding="utf-8").strip(), '2026.09.02')

    def test_undoing_a_first_update_keeps_the_updater_rules_and_hidden_shipped_files(self):
        files = dict(self.V1, **{'.gitignore': '/projects/\nrenders/\n', 'renders/bg.mp4': 'pre-rendered\n',
                                 'my-rules.md': 'template\n'})
        p = self.install(self.package('2026.09.01', files, updater=False), 'old')
        rc, out = self.run_update(p, self.v2(**{'renders/bg.mp4': 'pre-rendered\n', 'my-rules.md': 'template\n'}),
                                  script=UPDATE)
        self.assertEqual(rc, 0, out)
        put(p / 'my-rules.md', 'template\nmy rule\n')
        rc, out = self.run_update(p, '--undo')
        self.assertEqual(rc, 0, out)
        self.assertTrue((p / 'update.py').exists(), 'the undo removed the tool that finishes it')
        self.assertEqual((p / 'my-rules.md').read_text(encoding="utf-8"), 'template\nmy rule\n')
        self.assertEqual((p / 'renders/bg.mp4').read_text(encoding="utf-8"), 'pre-rendered\n')
        self.assertEqual((p / 'VERSION').read_text(encoding="utf-8").strip(), '2026.09.01')

    def test_a_shipped_script_deleted_before_setup_stays_deleted_without_a_conflict(self):
        p = self.install(self.package('2026.09.01', self.V1))
        (p / 'tool.sh').unlink()
        self.assertEqual(self.run_update(p, '--init')[0], 0)
        rc, out = self.run_update(p, self.v2(**{'tool.sh': '#!/bin/bash\necho v1\n'}))
        self.assertEqual(rc, 0, out)
        self.assertFalse((p / 'tool.sh').exists())

    def test_a_new_version_copied_over_the_project_keeps_the_users_edits(self):
        p = self.fresh()
        put(p / 'presets/x/style.md', 'x style v1\nmine\n')
        self.git(p, 'add', '-A')
        subprocess.run(['git', 'commit', '-qm', 'my edit'], cwd=str(p), env=self.env, check=True)
        z = self.v2()
        with zipfile.ZipFile(z) as zf:                                   # Extract All → Replace
            for info in zf.infolist():
                (p / info.filename.split('/', 1)[1]).write_bytes(zf.read(info))
        rc, out = self.run_update(p, z)
        self.assertEqual(rc, 0, out)
        self.assertIn('copied over', out)
        self.assertEqual((p / 'presets/x/style.md').read_text(encoding="utf-8"), 'x style v1\nmine\n')
        self.assertIn('line 10 (package)', (p / 'doc.md').read_text(encoding="utf-8"))

    def test_the_incoming_version_is_never_taken_as_where_the_user_started(self):
        v1 = DOC
        v2 = DOC.replace('line 3\n', 'line 3 v2\n').replace('line 7\n', 'line 7 v2\n').replace('line 9\n', 'line 9 v2\n')
        p = self.install(self.package('2026.09.01', dict(self.V1, **{'guide.md': v1}), updater=False), 'old')
        put(p / 'guide.md', v2.replace('line 9 v2\n', 'line 9\n').replace('line 1\n', 'line 1 mine\n'))
        rc, out = self.run_update(p, self.package('2026.09.02', dict(self.V1, **{'guide.md': v2}),
                                                  history=['2026.09.01']), script=UPDATE)
        self.assertEqual(rc, 0, out)
        g = (p / 'guide.md').read_text(encoding="utf-8")
        self.assertIn('line 9 v2', g, 'the part of the update the user had not hand-applied was dropped')
        self.assertIn('line 1 mine', g)

    def test_init_leaves_large_media_out(self):
        p = self.install(self.package('2026.09.01', self.V1))
        (p / 'presets/x/take.mov').write_bytes(b'\0' * (51 * 1024 * 1024))
        rc, out = self.run_update(p, '--init')
        self.assertEqual(rc, 0, out)
        self.assertEqual(self.git(p, 'ls-files', 'presets/x/take.mov'), '')


class RoundThree(Case):
    """What the third round of client simulations broke (2026-09-25)."""

    def test_settling_a_file_by_its_printed_full_path_never_deletes_it(self):
        p = self.install(self.package('2026.09.01', dict(self.V1, **{'assets/fx.wav': b'RIFF\0\0v1'})))
        self.assertEqual(self.run_update(p, '--init')[0], 0)
        (p / 'assets/fx.wav').write_bytes(b'RIFF\0\0mine')
        z = self.package('2026.09.02', self.v2_files(**{'assets/fx.wav': b'RIFF\0\0v2'}), history=['2026.09.01'])
        self.assertEqual(self.run_update(p, z)[0], 3)
        rc, out = self.run_update(p, '--keep-mine', str(p / 'doc.md'))
        self.assertEqual(rc, 1, out)
        self.assertIn('not one of the files', out)
        self.assertTrue((p / 'doc.md').exists())
        rc, out = self.run_update(p, '--keep-mine', str(p.resolve() / 'assets/fx.wav'))
        self.assertEqual(rc, 0, out)
        self.assertEqual((p / 'assets/fx.wav').read_bytes(), b'RIFF\0\0mine')
        self.assertEqual(self.run_update(p, '--continue')[0], 0)
        self.assertClean(p)

    def test_continue_waits_for_a_decision_on_a_file_deleted_on_one_side(self):
        p = self.fresh()
        (p / 'presets/x/style.md').unlink()
        rc, out = self.run_update(p, self.v2(**{'presets/x/style.md': 'x style v2\n'}))
        self.assertEqual(rc, 3, out)
        rc, out = self.run_update(p, '--continue')
        self.assertEqual(rc, 3, 'an unsettled deleted-vs-changed file went through\n' + out)
        (p / 'presets/x/style.md').unlink()          # Claude's decision: keep it deleted
        rc, out = self.run_update(p, '--continue')
        self.assertEqual(rc, 0, out)
        self.assertFalse((p / 'presets/x/style.md').exists())
        self.assertClean(p)

    def test_undo_keeps_what_the_user_deleted_and_edited_since(self):
        p = self.fresh()
        self.assertEqual(self.run_update(p, self.v2())[0], 0)
        (p / 'doc.md').unlink()                          # the update changed it; the user then deleted it
        put(p / 'new.md', 'new in v2\nand mine\n')  # the update added it; the user then edited it
        rc, out = self.run_update(p, '--undo')
        self.assertEqual(rc, 0, out)
        self.assertFalse((p / 'doc.md').exists(), 'the undo brought back a file the user deleted')
        self.assertEqual((p / 'new.md').read_text(encoding="utf-8"), 'new in v2\nand mine\n')
        self.assertEqual((p / 'VERSION').read_text(encoding="utf-8").strip(), '2026.09.01')
        self.assertClean(p)

    def test_taking_the_update_again_after_an_undo_merges_what_the_undo_kept(self):
        p = self.fresh()
        z = self.v2(**{'my-rules.md': 'template\n'})
        self.assertEqual(self.run_update(p, z)[0], 0)
        put(p / 'my-rules.md', 'template\nmy rule\n')
        put(p / 'new.md', 'new in v2\nbranded\n')
        self.assertEqual(self.run_update(p, '--undo')[0], 0)
        rc, out = self.run_update(p, z)
        self.assertEqual(rc, 0, out)
        self.assertEqual((p / 'my-rules.md').read_text(encoding="utf-8"), 'template\nmy rule\n')
        self.assertEqual((p / 'new.md').read_text(encoding="utf-8"), 'new in v2\nbranded\n')
        mine = [l for l in out.splitlines() if 'Your own changes' in l]
        self.assertFalse(mine and 'update.py' in mine[0], 'the kept updater is not the user\'s change')
        self.assertClean(p)

    def test_edits_git_never_saw_survive_a_new_version_copied_over_the_folder(self):
        p = self.fresh()
        put(p / 'presets/x/style.md', 'x style v1\nunsaved edit\n')
        snap = self.git(p, '-c', 'core.hooksPath=/dev/null', 'stash', 'create')     # what the hook does
        self.git(p, 'update-ref', 'refs/cos/snapshot', snap)
        z = self.v2()
        with zipfile.ZipFile(z) as zf:
            for info in zf.infolist():
                (p / info.filename.split('/', 1)[1]).write_bytes(zf.read(info))
        rc, out = self.run_update(p, z)
        self.assertEqual(rc, 0, out)
        self.assertEqual((p / 'presets/x/style.md').read_text(encoding="utf-8"), 'x style v1\nunsaved edit\n')
        self.assertIn('line 10 (package)', (p / 'doc.md').read_text(encoding="utf-8"))

    def test_a_package_copy_unzipped_inside_the_project_is_never_committed(self):
        p = self.fresh()
        self.install(self.v2(), 'client/new-version/content-os', setup=False)
        rc, out = self.run_update(p, self.v2())
        self.assertEqual(rc, 0, out)
        self.assertEqual(self.git(p, 'ls-files', 'new-version'), '')
        self.assertNotIn('new-version', ''.join(l for l in out.splitlines() if 'Your own changes' in l))

    def test_release_notes_skip_update_howtos_and_keep_every_section(self):
        p = self.fresh()
        notes = '# Release notes\n\n## 2026.09.03\n\nLead 3.\n\n- To update, say update\n- real 3\n\n'
        notes += ''.join('## 2026.09.02\n\nLead 2.\n\n' + ''.join('- item %d\n' % i for i in range(60)) for _ in [0])
        z = self.package('2026.09.03', self.v2_files(**{'RELEASE.md': notes}), history=['2026.09.01'])
        rc, out = self.run_update(p, z)
        self.assertEqual(rc, 0, out)
        self.assertNotIn('To update', out)
        self.assertIn('real 3', out)
        self.assertIn('Lead 2.', out)


class RoundFour(Case):
    """What the final round of client simulations found (2026-09-25)."""

    def test_a_reverted_edit_is_not_brought_back_by_an_old_snapshot(self):
        p = self.fresh()
        put(p / 'presets/x/style.md', 'x style v1\ntrial line\n')
        self.git(p, 'update-ref', 'refs/cos/snapshot', self.git(p, '-c', 'core.hooksPath=/dev/null', 'stash', 'create'))
        put(p / 'presets/x/style.md', 'x style v1\n')        # the user dropped the trial
        rc, out = self.run_update(p, self.v2())
        self.assertEqual(rc, 0, out)
        self.assertEqual((p / 'presets/x/style.md').read_text(encoding="utf-8"), 'x style v1\n')
        self.assertNotIn('copied over', out)

    def test_going_back_to_an_older_version_keeps_the_newer_updater(self):
        p = self.fresh()
        self.assertEqual(self.run_update(p, self.v2())[0], 0)
        old = self.package('2026.08.30', self.V1, updater_text='# an older updater\n')
        rc, out = self.run_update(p, old, '--force')
        self.assertEqual(rc, 0, out)
        self.assertEqual((p / 'VERSION').read_text(encoding="utf-8").strip(), '2026.08.30')
        self.assertEqual((p / 'update.py').read_text(encoding="utf-8"), UPDATE.read_text(encoding="utf-8"))
        self.assertClean(p)


class MyRules(Case):
    """Lines a user added to CLAUDE.md (an old "apply my brand kit" wrote their identity there) move to
    my-rules.md on the first update that ships it, so CLAUDE.md never conflicts over them again."""
    OLD = '# CLAUDE.md\n\n## Brand Kit\n\nVoice comes entirely from brand-kit.md.\n\n## Rules\n\n- rule one\n- rule two\n'
    NEW = ('# CLAUDE.md\n\n## Brand Kit\n\nVoice comes wholly from brand-kit.md.\n\n## Rules\n\n- rule one, sharper\n'
           '- rule two\n\n## Your rules\n\n@my-rules.md\n')
    STUB = '# My rules\n\nWrite your rules below.\n'

    def v2_rules(self):
        return self.v2(**{'CLAUDE.md': self.NEW, 'my-rules.md': self.STUB})

    def test_added_lines_move_and_claude_md_takes_the_new_version(self):
        p = self.install(self.package('2026.09.01', dict(self.V1, **{'CLAUDE.md': self.OLD})))
        self.assertEqual(self.run_update(p, '--init')[0], 0)
        put(p / 'CLAUDE.md', self.OLD.replace(
            'brand-kit.md.\n', 'brand-kit.md.\n- **Creator:** Maya\n- **Niche:** pottery\n').replace(
            '- rule one\n', '- rule one\n- **Maya\'s rule:** never say hack\n'))
        rc, out = self.run_update(p, self.v2_rules())
        self.assertEqual(rc, 0, out)
        self.assertEqual((p / 'CLAUDE.md').read_text(encoding="utf-8"), self.NEW)
        rules = (p / 'my-rules.md').read_text(encoding="utf-8")
        self.assertNotIn(b'\r', (p / 'my-rules.md').read_bytes(), 'the move rewrote my-rules.md as CRLF (Windows text mode)')
        self.assertTrue(rules.startswith(self.STUB.rstrip('\n')), rules)
        for line in ('- **Creator:** Maya', '- **Niche:** pottery', "- **Maya's rule:** never say hack",
                     '(from its "Brand Kit" section)', '(from its "Rules" section)'):
            self.assertIn(line, rules)
        self.assertIn('3 lines the user had added to CLAUDE.md', out)
        self.assertClean(p)
        rc, out = self.run_update(p, '--undo')                    # the undo gives CLAUDE.md its lines back
        self.assertEqual(rc, 0, out)
        self.assertIn('- **Niche:** pottery', (p / 'CLAUDE.md').read_text(encoding="utf-8"))

    def test_a_pre_update_install_moves_them_too(self):
        files = dict(self.V1, **{'CLAUDE.md': self.OLD, '.gitignore': PreUpdateInstall.OLD_GITIGNORE})
        p = self.install(self.package('2026.09.01', files, updater=False), 'old')
        put(p / 'CLAUDE.md', self.OLD.replace('## Rules\n\n', '## Rules\n\n- my own rule\n'))
        rc, out = self.run_update(p, self.v2_rules(), script=UPDATE)
        self.assertEqual(rc, 0, out)
        self.assertEqual((p / 'CLAUDE.md').read_text(encoding="utf-8"), self.NEW)
        self.assertIn('- my own rule', (p / 'my-rules.md').read_text(encoding="utf-8"))
        self.assertClean(p)

    def test_an_edited_shipped_line_stays_an_ordinary_merge(self):
        p = self.install(self.package('2026.09.01', dict(self.V1, **{'CLAUDE.md': self.OLD})))
        self.assertEqual(self.run_update(p, '--init')[0], 0)
        put(p / 'CLAUDE.md', self.OLD.replace('# CLAUDE.md\n', '# CLAUDE.md, my way\n'))
        rc, out = self.run_update(p, self.v2_rules())
        self.assertEqual(rc, 0, out)
        self.assertEqual((p / 'CLAUDE.md').read_text(encoding="utf-8"), self.NEW.replace('# CLAUDE.md\n', '# CLAUDE.md, my way\n'))
        self.assertEqual((p / 'my-rules.md').read_text(encoding="utf-8"), self.STUB)
        self.assertNotIn('added to CLAUDE.md', out)


class Refusals(Case):
    def test_maintainer_repo_and_non_projects_are_refused(self):
        repo = self.tmp / 'maintainer'
        (repo / 'packaging').mkdir(parents=True)
        for f in ('CLAUDE.md', 'check-setup.sh', 'packaging/package-for-client.sh'):
            put(repo / f, 'x\n')
        rc, out = self.run_update(repo, '--init', script=UPDATE)
        self.assertEqual(rc, 1, out)
        self.assertFalse((repo / '.git').exists())
        rc, out = self.run_update(self.tmp, self.package('2026.09.02', self.V1), script=UPDATE)
        self.assertEqual(rc, 1, out)
        self.assertIn('not a Content OS folder', out)

    def test_nothing_to_continue_abort_or_undo(self):
        p = self.fresh()
        self.assertEqual(self.run_update(p, '--continue')[0], 0)
        self.assertEqual(self.run_update(p, '--abort')[0], 0)
        rc, out = self.run_update(p, '--undo')
        self.assertEqual(rc, 1, out)
        self.assertIn('no update to undo', out)



class RoundFive(Case):
    """The 2026-09-25 audit: an unzip over a pre-update install, media at any size, an interrupted apply, the undo's
    copy instruction, and the setup-time install finder."""
    OLD_GITIGNORE = PreUpdateInstall.OLD_GITIGNORE

    def test_a_new_version_unzipped_over_a_pre_update_install_says_so_and_never_up_to_date(self):
        p = PreUpdateInstall.old_install(self)
        z = self.v2()
        with zipfile.ZipFile(z) as zf:                                   # Extract All → Replace, no .git anywhere
            for info in zf.infolist():
                t = p / info.filename.split('/', 1)[1]
                t.parent.mkdir(parents=True, exist_ok=True)
                t.write_bytes(zf.read(info))
        rc, out = self.run_update(p)
        self.assertEqual(rc, 1, out)
        self.assertIn('unzipped OVER this folder', out)
        self.assertIn('retired.md', out)
        self.assertIn('separate folder', out)
        self.assertNotIn('up to date', out)

    def test_media_of_any_size_stays_out_of_git(self):
        p = self.fresh()
        (p / 'presets/x/clips').mkdir(parents=True)
        (p / 'presets/x/clips/take.mp4').write_bytes(b'\0' * (1024 * 1024))
        (p / 'thumb.png').write_bytes(b'\x89PNG' + b'\0' * 64)
        rc, out = self.run_update(p, self.v2())
        self.assertEqual(rc, 0, out)
        self.assertIn('media, untouched', out)
        self.assertEqual(self.git(p, 'ls-files', 'presets/x/clips/take.mp4', 'thumb.png'), '')
        self.assertEqual((p / 'presets/x/clips/take.mp4').stat().st_size, 1024 * 1024)
        self.assertTrue((p / 'thumb.png').is_file())
        self.assertClean(p)

    def test_an_interrupted_apply_is_put_back_before_the_next_update(self):
        import importlib.util
        from unittest.mock import patch
        p = self.fresh()
        put(p / 'doc.md', DOC.replace('line 2\n', 'line 2 (mine)\n'))
        z = self.v2()
        pkg = self.texts['2026.09.02']
        with patch.dict(os.environ, self.env, clear=True):
            spec = importlib.util.spec_from_file_location('cos_update_under_test', p / 'update.py')
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            real = mod.git_rc

            def killed_mid_merge(cwd, *args, **kw):
                if 'merge' in args and '--no-ff' in args:        # the checkout had written two files, then the kill
                    (p / 'doc.md').write_bytes(pkg['doc.md'])
                    (p / 'new.md').write_bytes(pkg['new.md'])
                    raise KeyboardInterrupt
                return real(cwd, *args, **kw)
            import contextlib, io as _io
            with patch.object(mod, 'git_rc', killed_mid_merge), self.assertRaises(KeyboardInterrupt), \
                    contextlib.redirect_stdout(_io.StringIO()):
                mod.main([str(z), '--project', str(p)])
        self.assertTrue((p / '.git' / 'cos-update-state.json').exists())
        rc, out = self.run_update(p, z)
        self.assertEqual(rc, 0, out)
        self.assertIn('interrupted; it was put back first', out)
        doc = (p / 'doc.md').read_text(encoding="utf-8")
        self.assertIn('line 2 (mine)', doc, 'the user\'s edit the interrupted checkout overwrote is back')
        self.assertIn('line 10 (package)', doc)
        self.assertEqual((p / 'new.md').read_text(encoding="utf-8"), 'new in v2\n')
        self.assertClean(p)

    def test_the_undo_names_only_rules_the_restored_claude_md_lacks(self):
        mr = MyRules
        p = self.install(self.package('2026.09.01', dict(self.V1, **{'CLAUDE.md': mr.OLD})))
        self.assertEqual(self.run_update(p, '--init')[0], 0)
        put(p / 'CLAUDE.md', mr.OLD.replace('## Rules\n\n', '## Rules\n\n- my own rule\n'))
        rc, out = self.run_update(p, self.v2(**{'CLAUDE.md': mr.NEW, 'my-rules.md': mr.STUB}))
        self.assertEqual(rc, 0, out)
        rc, out = self.run_update(p, '--undo')
        self.assertEqual(rc, 0, out)
        self.assertIn('- my own rule', (p / 'CLAUDE.md').read_text(encoding="utf-8"))
        self.assertNotIn('does not read my-rules.md', out, 'the moved line is back in CLAUDE.md: nothing to copy')
        p2 = self.install(self.package('2026.09.01', dict(self.V1, **{'CLAUDE.md': mr.OLD})), 'client2')
        self.assertEqual(self.run_update(p2, '--init')[0], 0)
        rc, out = self.run_update(p2, self.v2(**{'CLAUDE.md': mr.NEW, 'my-rules.md': mr.STUB}))
        self.assertEqual(rc, 0, out)
        with open(p2 / 'my-rules.md', 'a', encoding="utf-8", newline='') as fh:
            fh.write('- a rule written after the update\n')
        rc, out = self.run_update(p2, '--undo')
        self.assertEqual(rc, 0, out)
        self.assertIn('does not read my-rules.md', out)
        self.assertIn('a rule written after the update', out)
        self.assertIn('1 line', out)

    def test_find_installs_lists_the_set_up_installs_but_never_itself(self):
        home = self.fresh()
        download = self.install(self.v2(), 'new-download', setup=False)
        rc, out = self.run_update(download, '--find-installs')
        self.assertEqual(rc, 0, out)
        self.assertEqual([Path(l).resolve() for l in out.split()], [home.resolve()])
        rc, out = self.run_update(home, '--find-installs')
        self.assertEqual((rc, out.strip()), (0, ''))


class ContentOS(Case):
    """What only Content OS has: installs from before VERSION files existed, output folders, brand-kit fields."""

    def test_output_folders_are_never_tracked_or_touched(self):
        p = self.fresh()
        mine = {'research/IG-Research_2026-09-01.html': '<html>r</html>\n', 'transcripts/url/a_2026-09-01.md': 't\n',
                'voice-corpus/yt-abc.md': 'v\n', 'voice-corpus/index.md': 'i\n', 'knowledge/strategy.md': 'k\n',
                'carousel/outputs/slug/caption.md': 'c\n', 'descriptions/job_2026-09-01.md': 'd\n',
                'thumbnails/slug/thumb.json': '{}\n', 'outreach/dm-revival/log.json': '[]\n',
                'title-corpus/titles.json': '[]\n', 'assets/face-refs/me.txt': 'f\n', 'assets/logos/logo.svg': '<svg/>\n',
                '.claude/skills/auto-poster/.env': 'ZERNIO_API_KEY=secret\n',
                '.claude/skills/carousel-generator/scripts/package-lock.json': '{}\n'}
        for f, t in mine.items():
            (p / f).parent.mkdir(parents=True, exist_ok=True)
            put(p / f, t)
        rc, out = self.run_update(p, self.v2())
        self.assertEqual(rc, 0, out)
        for f, t in mine.items():
            self.assertEqual((p / f).read_text(encoding="utf-8"), t, f)
        self.assertEqual(self.git(p, 'ls-files', *mine), '', 'an output or secret was committed')
        self.assertEqual(self.git(p, 'ls-files', 'research/README.md'), 'research/README.md')
        self.assertNotIn('Your own changes', out, 'outputs are not changes to Content OS')
        self.assertClean(p)

    def legacy(self):
        """Two zips from before updates (no VERSION); the user installed the second and worked in it."""
        self.package('2026.09.11', self.V1, legacy=True)
        v23 = dict(self.V1, **{'doc.md': DOC.replace('line 7\n', 'line 7 (09.23)\n')})
        return self.install(self.package('2026.09.23', v23, legacy=True), 'Documents/content-os')

    def test_a_legacy_install_is_placed_by_its_files(self):
        p = self.legacy()
        self.assertFalse((p / 'VERSION').exists())
        (p / 'keep.md').unlink()
        put(p / 'doc.md', DOC.replace('line 7\n', 'line 7 (09.23)\n').replace('line 2\n', 'line 2 (mine)\n'))
        put(p / 'research/YT-Research_2026-09-20.html', 'report\n')
        v = self.v2_files(**{'doc.md': DOC.replace('line 7\n', 'line 7 (09.23)\n').replace('line 10\n', 'line 10 (new)\n')})
        rc, out = self.run_update(p, self.package('2026.09.29.2', v, history=['2026.09.11', '2026.09.23']), script=UPDATE)
        self.assertEqual(rc, 0, out)
        self.assertIn('2026.09.23 → 2026.09.29.2', out, 'the version it started from is named from its files')
        doc = (p / 'doc.md').read_text(encoding="utf-8")
        for line in ('line 2 (mine)', 'line 7 (09.23)', 'line 10 (new)'):
            self.assertIn(line, doc)
        self.assertFalse((p / 'keep.md').exists(), 'a shipped file the user deleted came back')
        self.assertEqual((p / 'research/YT-Research_2026-09-20.html').read_text(encoding="utf-8"), 'report\n')
        self.assertEqual(self.git(p, 'ls-files', 'research/YT-Research_2026-09-20.html'), '')
        self.assertEqual((p / 'VERSION').read_text(encoding="utf-8").strip(), '2026.09.29.2')
        self.assertEqual((p / '.gitignore').read_text(encoding="utf-8"), GITIGNORE)
        self.assertClean(p)

    def test_a_legacy_install_is_found_from_the_new_download(self):
        p = self.legacy()
        d = self.install(self.package('2026.09.29.2', self.v2_files(), history=['2026.09.11', '2026.09.23']),
                         'Downloads/content-os', setup=False)
        rc, out = self.run_update(d)
        self.assertEqual(rc, 0, out)
        self.assertIn('never set up', out)
        self.assertEqual((p / 'VERSION').read_text(encoding="utf-8").strip(), '2026.09.29.2')
        self.assertIn(str(p.resolve()), (self.tmp / '.content-os' / 'installs').read_text(encoding="utf-8"))

    TEMPLATE = '# CLAUDE.md\n\n## Creator Profile\n\n- **Name:** <<YOUR_NAME>>\n- **Niche:** <<YOUR_NICHE>>\n\n## Rules\n\n- one\n'

    def test_new_brand_kit_fields_are_named_after_the_update(self):
        p = self.install(self.package('2026.09.01', dict(self.V1, **{'CLAUDE.md': self.TEMPLATE})))
        self.assertEqual(self.run_update(p, '--init')[0], 0)
        put(p / 'CLAUDE.md', self.TEMPLATE.replace('<<YOUR_NAME>>', 'Maya').replace('<<YOUR_NICHE>>', 'pottery'))
        new = self.TEMPLATE.replace('- **Niche:** <<YOUR_NICHE>>\n', '- **Niche:** <<YOUR_NICHE>>\n- **Newsletter:** <<YOUR_NEWSLETTER>>\n')
        rc, out = self.run_update(p, self.v2(**{'CLAUDE.md': new}))
        self.assertEqual(rc, 3, out)              # the new field sits next to a line the user filled in
        self.assertIn('keeps every value they gave', out)
        put(p / 'CLAUDE.md', new.replace('<<YOUR_NAME>>', 'Maya').replace('<<YOUR_NICHE>>', 'pottery'))  # Claude's merge
        rc, out = self.run_update(p, '--continue')
        self.assertEqual(rc, 0, out)
        self.assertIn('YOUR_NEWSLETTER', out)
        self.assertIn('personalized', out)
        # a field that lands away from the user's lines merges on its own, and is still named
        again = new.replace('## Rules\n', '## Rules\n\n- **Timezone:** <<YOUR_TIMEZONE>>\n')
        rc, out = self.run_update(p, self.package('2026.09.03', self.v2_files(**{'CLAUDE.md': again}),
                                                  history=['2026.09.01', '2026.09.02']))
        self.assertEqual(rc, 0, out)
        md = (p / 'CLAUDE.md').read_text(encoding="utf-8")
        for line in ('- **Name:** Maya', '<<YOUR_TIMEZONE>>'):
            self.assertIn(line, md)
        self.assertIn('YOUR_TIMEZONE', out)
        self.assertNotIn('YOUR_NEWSLETTER', out, 'only the fields new in this version are named')

    def test_an_unpersonalized_folder_gets_no_brand_kit_line(self):
        p = self.install(self.package('2026.09.01', dict(self.V1, **{'CLAUDE.md': self.TEMPLATE})))
        self.assertEqual(self.run_update(p, '--init')[0], 0)
        rc, out = self.run_update(p, self.v2(**{'CLAUDE.md': self.TEMPLATE + '- two\n'}))
        self.assertEqual(rc, 0, out)
        self.assertNotIn('personalized', out)


if __name__ == '__main__':
    unittest.main()
