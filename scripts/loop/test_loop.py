"""Offline regression tests: fake processes only, no model requests."""
import json
import os
from pathlib import Path
import signal
import shutil
import subprocess
import sys
import tempfile
import time
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent))
from events import Events, reset_time
import codex
import runner


class EventTests(unittest.TestCase):
    def test_success_after_recovered_error(self):
        events = Events()
        events.line('{"type":"error","message":"429 retry in 5 minutes"}')
        events.line('{"type":"turn.completed"}')
        self.assertEqual(events.outcome(0)[0], 'success')

    def test_structured_quota_even_with_zero_exit(self):
        for event in [
            {'type': 'error', 'message': "You've hit your limit", 'retry_after': 4000},
            {'type': 'turn.failed', 'error': {'message': 'usage limit reached', 'resets_at': 5000}},
            {'type': 'error', 'message': 'Rate limit exceeded', 'retry_after': 4000},
            {'type': 'turn.failed', 'error': {'message': 'RESOURCE_EXHAUSTED', 'retry_after': 4000}},
        ]:
            with self.subTest(event=event):
                events = Events()
                events.line(json.dumps(event))
                self.assertEqual(events.outcome(0, now=1000), ('quota', 5000))

    def test_tool_text_is_not_a_failure(self):
        events = Events()
        events.line(json.dumps({'type': 'item.completed', 'item': {'type': 'command_execution', 'aggregated_output': 'usage limit reached'}}))
        events.line('{"type":"turn.completed"}')
        self.assertEqual(events.outcome(0)[0], 'success')

    def test_auth_and_network(self):
        for text, expected in [('Not logged in', 'fatal'), ('unknown option --bad', 'fatal'), ('Connection reset ECONNRESET', 'transient'), ('unexplained crash', 'unknown')]:
            events = Events()
            events.line(text, stderr=True)
            self.assertEqual(events.outcome(1)[0], expected)

    def test_reset_formats_and_multiple_windows(self):
        self.assertEqual(reset_time({}, 'Try again in 2h 30m', 1000), 10000)
        self.assertEqual(reset_time({'a': {'reset_at': 2000}, 'b': {'reset_at': 5000}}, '', 1000), 5000)
        self.assertIsNone(reset_time({}, 'resets at 5pm (Europe/Brussels)', 1000))
        stamp = 1789000000
        self.assertEqual(reset_time({'resetsAt': (stamp + 100) * 1000}, '', stamp), stamp + 100)
        self.assertEqual(reset_time({}, 'resets at 2026-09-10T10:00:00Z', 1788990000), 1789034400)


class AdapterTests(unittest.TestCase):
    def test_prompt_is_passed_literally(self):
        prompt = 'Literal $(touch NEVER) `echo not-shell`\nProof α'
        argv, stdin = codex.command('codex', prompt)
        self.assertEqual(stdin, prompt)
        self.assertNotIn('--dangerously-bypass-approvals-and-sandbox', argv)

    def test_api_env_fails_without_exposing_secret(self):
        with patch.dict(os.environ, {'OPENAI_API_KEY': 'private-test-value'}, clear=True), patch('codex.shutil.which', return_value='/fake/codex'):
            with self.assertRaises(RuntimeError) as caught:
                codex.check(Path('/tmp'))
            self.assertNotIn('private-test-value', str(caught.exception))

    def test_custom_provider_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            home = Path(tmp)
            (home / 'config.toml').write_text('[model_providers.paid]\napi_key = "secret"\n')
            with patch.dict(os.environ, {'CODEX_HOME': tmp}, clear=True), patch('codex.shutil.which', return_value='/fake/codex'):
                with self.assertRaises(RuntimeError):
                    codex.check(home)


class ProcessTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='notebook-loop-test-')
        self.root = Path(self.tmp.name)
        (self.root / 'history').mkdir()
        (self.root / 'PROGRESS.md').write_text('STATUS: IN_PROGRESS\nNext action: test\n')
        (self.root / 'PROMPT.md').write_text('test prompt\n')
        (self.root / 'GOAL.md').write_text('test rules\n')
        (self.root / 'scripts/loop').mkdir(parents=True)
        self.root_patch = patch.object(runner, 'ROOT', self.root)
        self.root_patch.start()
        runner.STOP = False

    def tearDown(self):
        self.root_patch.stop()
        self.tmp.cleanup()
        runner.STOP = False

    def fake(self, code):
        path = self.root / 'fake.py'
        path.write_text(code)
        return [sys.executable, '-u', str(path)]

    def test_stream_process_and_literal_stdin(self):
        argv = self.fake('import sys,json\ns=sys.stdin.read()\nprint(json.dumps({"type":"message","text":s}))\nprint(json.dumps({"type":"turn.completed"}))\n')
        kind, _, code = runner.run_process(argv, '$(do-not-execute)\n', self.root, 5)
        self.assertEqual((kind, code), ('success', 0))
        self.assertIn('$(do-not-execute)', (self.root / 'stdout.log').read_text())

    def test_timeout_kills_child(self):
        argv = self.fake('import time\ntime.sleep(60)\n')
        start = time.monotonic()
        result = runner.run_process(argv, None, self.root, 0.2)
        self.assertEqual(result[0], 'unknown')
        self.assertLess(time.monotonic() - start, 8)

    def test_lock_is_exclusive_and_reusable(self):
        path = self.root / 'scripts/loop/workspace.lock'
        with runner.lock(path):
            with self.assertRaises(RuntimeError):
                with runner.lock(path):
                    pass
        with runner.lock(path):
            pass

    def test_quota_persisted_and_honored_on_restart(self):
        def fake_run(*args):
            return 'quota', time.time() + 86400, 1
        with patch.object(sys, 'argv', ['runner.py', '--once']), patch.object(runner, 'check', return_value='fake'), patch.object(runner, 'run_process', side_effect=fake_run):
            self.assertEqual(runner.main(), 1)
        state = json.loads((self.root / 'scripts/loop-codex/state.json').read_text())
        self.assertGreater(state['retry_at'], time.time() + 86390)
        def interrupt_wait(stamp):
            self.assertEqual(stamp, state['retry_at'])
            runner.STOP = True
        with patch.object(sys, 'argv', ['runner.py', '--once']), patch.object(runner, 'check', return_value='fake'), patch.object(runner, 'wait_until', side_effect=interrupt_wait), patch.object(runner, 'run_process') as run:
            self.assertEqual(runner.main(), 130)
            run.assert_not_called()

    def test_success_checkpoint_and_proved_stop(self):
        def fake_run(*args):
            (self.root / 'PROGRESS.md').write_text('STATUS: IN_PROGRESS\nNext action: next test\n')
            return 'success', None, 0
        with patch.object(sys, 'argv', ['runner.py', '--once']), patch.object(runner, 'check', return_value='fake'), patch.object(runner, 'run_process', side_effect=fake_run), patch.object(runner, 'validate'):
            self.assertEqual(runner.main(), 0)
        (self.root / 'PROGRESS.md').write_text('STATUS: PROVED\n')
        with patch.object(sys, 'argv', ['runner.py']), patch.object(runner, 'check', return_value='fake'), patch.object(runner, 'run_process') as run, patch.object(runner, 'validate'):
            self.assertEqual(runner.main(), 0)
            run.assert_not_called()

    def test_log_rotation_is_bounded(self):
        handlers = runner.logs(self.root)
        try:
            for _ in range(150):
                runner.write_log(handlers[0], 'x' * 65536)
        finally:
            for handler in handlers:
                handler.close()
        files = list(self.root.glob('stdout.log*'))
        self.assertEqual(len(files), 3)
        self.assertLess(sum(p.stat().st_size for p in files), 7 * 1024 * 1024)

    def test_invalid_state_fails(self):
        path = self.root / 'state.json'
        path.write_text('{bad json')
        with self.assertRaises(RuntimeError):
            runner.read_state(path)


class LauncherTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='loop-launcher-')
        self.root = Path(self.tmp.name) / 'notebook with spaces'
        self.root.mkdir()
        source = Path(__file__).resolve().parents[2]
        shutil.copytree(source / 'scripts/loop', self.root / 'scripts/loop', ignore=shutil.ignore_patterns('__pycache__'))
        shutil.copy2(source / 'loop-codex.sh', self.root)
        (self.root / 'scripts/docs').mkdir()
        (self.root / 'scripts/docs/check_structure.py').write_text('print("fixture structure OK")')
        (self.root / 'history').mkdir()
        (self.root / 'GOAL.md').write_text('Test rules')
        (self.root / 'PROGRESS.md').write_text('STATUS: IN_PROGRESS\nNext action: fixture\n')
        (self.root / 'PROMPT.md').write_text('Literal $(touch NEVER) `touch ALSO_NEVER` α\n')
        bindir = self.root / 'bin'
        bindir.mkdir()
        fake = r"""import sys, json, pathlib, time, subprocess
args = sys.argv[1:]
name = pathlib.Path(sys.argv[0]).name
if args == ['login', 'status']:
    print('Logged in using ChatGPT')
    sys.exit(0)
expected = pathlib.Path('PROMPT.md').read_text()
actual = sys.stdin.read()
assert actual == expected
pathlib.Path('invoked-'+name).write_text(json.dumps(args))
if pathlib.Path('hold').exists():
    child = subprocess.Popen([sys.executable, '-c', 'import time; time.sleep(60)'])
    pathlib.Path('child.pid').write_text(str(child.pid))
    time.sleep(60)
with pathlib.Path('PROGRESS.md').open('a') as f:
    f.write('Checkpoint from '+name+'\n')
print('{"type":"turn.completed"}')
"""
        path = bindir / 'codex'
        path.write_text('#!' + sys.executable + '\n' + fake)
        path.chmod(0o755)
        self.env = {key:value for key,value in os.environ.items() if key not in codex.BILLING_ENV}
        self.env.update(PATH=str(bindir) + os.pathsep + os.environ['PATH'], CODEX_HOME=str(self.root / '.codex'))

    def tearDown(self):
        self.tmp.cleanup()

    def test_launcher_from_other_directory(self):
        result = subprocess.run(['bash', str(self.root / 'loop-codex.sh'), '--once'], cwd='/tmp', env=self.env, text=True, capture_output=True, timeout=15)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertTrue((self.root / 'invoked-codex').exists())
        self.assertFalse((self.root / 'NEVER').exists())
        self.assertFalse((self.root / 'ALSO_NEVER').exists())
        state = json.loads((self.root / 'scripts/loop-codex/state.json').read_text())
        self.assertEqual(state['outcome'], 'success')

    def test_sigint_stops_loop_and_child(self):
        (self.root / 'hold').touch()
        process = subprocess.Popen(['bash', str(self.root / 'loop-codex.sh')], cwd='/tmp', env=self.env, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        try:
            deadline = time.monotonic() + 10
            while not (self.root / 'child.pid').exists() and time.monotonic() < deadline:
                time.sleep(0.05)
            self.assertTrue((self.root / 'child.pid').exists())
            process.send_signal(signal.SIGINT)
            output, errors = process.communicate(timeout=15)
            self.assertEqual(process.returncode, 130, output + errors)
            state = json.loads((self.root / 'scripts/loop-codex/state.json').read_text())
            self.assertEqual(state['outcome'], 'interrupted')
            child = (self.root / 'child.pid').read_text()
            status = subprocess.run(['ps', '-o', 'stat=', '-p', child], capture_output=True, text=True)
            self.assertTrue(not status.stdout.strip() or status.stdout.strip().startswith('Z'), status.stdout)
        finally:
            if process.poll() is None:
                process.kill()
                process.wait()
            process.stdout.close()
            process.stderr.close()


if __name__ == '__main__':
    unittest.main()
