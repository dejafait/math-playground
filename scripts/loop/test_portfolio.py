"""Offline scheduling, isolation, migration and restart regression tests."""
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
import runner
from portfolio import registry, migrate, choose
from test_research import report


class PortfolioTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / 'scripts/loop').mkdir(parents=True)
        self.ids = ['riemann'] + [f'problem-{i}' for i in range(1, 10)]
        for slug in self.ids:
            d = self.root / slug
            d.mkdir()
            (d / 'history').mkdir()
            for name in ('GOAL.md', 'PROOF.md', 'DAG.md'):
                (d / name).write_text('fixture')
            (d / 'PROGRESS.md').write_text(report('initial', 'EXPLORATION'))
        self.rows = [{'id': s, 'enabled': True} for s in self.ids]
        (self.root / 'scripts/loop/problems.json').write_text(json.dumps(self.rows))
        (self.root / 'PROMPT.md').write_text('shared literal prompt $(not-shell)')
        (self.root / 'GOAL.md').write_text('shared policy')
        self.calls = []
        self.stack = []
        for patcher in [patch.object(runner, 'ROOT', self.root), patch.object(runner, 'STOP', False),
                        patch.object(runner, 'check', return_value='fake'),
                        patch.object(runner, 'validate'), patch.object(runner, 'wait_until'),
                        patch.object(sys, 'argv', ['runner.py', '--once']),
                        patch.object(runner, 'run_process', side_effect=self.run_step)]:
            patcher.start(); self.stack.append(patcher)

    def tearDown(self):
        for p in reversed(self.stack):
            p.stop()
        self.tmp.cleanup()

    def run_step(self, argv, prompt, output, timeout, verbose, notebook):
        self.calls.append(notebook.name)
        self.assertIn('Active problem: ' + notebook.name, prompt)
        self.assertEqual(output.name, notebook.name)
        (notebook / 'PROGRESS.md').write_text(report(str(len(self.calls)), 'ADVANCE'))
        return 'success', None, 0

    def state(self):
        return json.loads((self.root / 'scripts/loop-codex/state.json').read_text())

    def test_rotation_survives_restart_and_wraps(self):
        for _ in range(11):
            self.assertEqual(runner.main(), 0)
        self.assertEqual(self.calls, self.ids + ['riemann'])
        self.assertEqual(self.state()['problems']['riemann']['turns'], 2)
        self.assertEqual(self.state()['next_problem'], 'problem-1')

    def test_halted_and_resolved_notebooks_are_skipped(self):
        directory = self.root / 'scripts/loop-codex'; directory.mkdir()
        (directory / 'state.json').write_text(json.dumps({'research_halt': 'legacy stop', 'retry_at': 0}))
        (self.root / 'problem-1/PROGRESS.md').write_text('STATUS: DISPROVED\n')
        runner.main()
        self.assertEqual(self.calls, ['problem-2'])
        self.assertEqual(self.state()['problems']['riemann']['research_halt'], 'legacy stop')

    def test_stall_counters_are_independent(self):
        def stall(*args):
            notebook = args[-1]
            self.calls.append(notebook.name)
            (notebook / 'PROGRESS.md').write_text(report(str(len(self.calls)), 'STALLED'))
            return 'success', None, 0
        with patch.object(runner, 'run_process', side_effect=stall):
            for _ in range(11):
                runner.main()
        state = self.state()['problems']
        self.assertIn('research_halt', state['riemann'])
        self.assertNotIn('research_halt', state['problem-1'])
        runner.main()
        self.assertEqual(self.calls[-1], 'problem-1')

    def test_quota_does_not_rotate_or_charge_research_turn(self):
        with patch.object(runner, 'run_process', return_value=('quota', None, 1)):
            self.assertEqual(runner.main(), 1)
        state = self.state()
        self.assertEqual(state['next_problem'], 'riemann')
        self.assertEqual(state['problems']['riemann'].get('turns', 0), 0)
        self.assertGreater(state['retry_at'], 0)

    def test_targeted_resume_does_not_reset_other_stops_or_quota(self):
        directory = self.root / 'scripts/loop-codex'; directory.mkdir()
        original = {'next_problem': 'riemann', 'retry_at': 9999999999, 'problems': {
            'riemann': {'research_halt': 'one'}, 'problem-1': {'research_halt': 'two'}}}
        (directory / 'state.json').write_text(json.dumps(original))
        def stop_wait(stamp):
            self.assertEqual(stamp, original['retry_at']); runner.STOP = True
        with patch.object(sys, 'argv', ['runner.py', '--resume-research', 'riemann']), patch.object(runner, 'wait_until', side_effect=stop_wait):
            self.assertEqual(runner.main(), 130)
        self.assertNotIn('research_halt', self.state()['problems']['riemann'])
        self.assertEqual(self.state()['problems']['problem-1']['research_halt'], 'two')
        self.assertFalse(self.calls)

    def test_one_notebook_failure_budget_survives_other_successes(self):
        successful = self.run_step
        def selective_failure(*args):
            if args[-1].name == 'riemann':
                self.calls.append('riemann')
                return 'unknown', None, 1
            return successful(*args)
        with patch.object(runner, 'run_process', side_effect=selective_failure):
            for _ in range(21):
                runner.main()
        self.assertIn('research_halt', self.state()['problems']['riemann'])
        self.assertNotIn('research_halt', self.state()['problems']['problem-1'])

    def test_validation_failure_halts_only_active_notebook(self):
        with patch.object(runner, 'validate', side_effect=RuntimeError('broken DAG')):
            runner.main()
        self.assertIn('research_halt', self.state()['problems']['riemann'])
        runner.main()
        self.assertEqual(self.calls, ['riemann', 'problem-1'])

    def test_registry_rejects_path_traversal_and_duplicates(self):
        for rows in [[{'id': '../escape', 'enabled': True}], [self.rows[0], self.rows[0]]]:
            (self.root / 'scripts/loop/problems.json').write_text(json.dumps(rows))
            with self.assertRaises(RuntimeError):
                registry(self.root)

    def test_legacy_migration_is_idempotent(self):
        state = {'retry_at': 456, 'research_halt': 'stop', 'exploration_turns': 3}
        migrate(state); migrate(state)
        self.assertEqual(state['retry_at'], 456)
        self.assertEqual(state['problems']['riemann']['exploration_turns'], 3)
        self.assertNotIn('research_halt', state)
