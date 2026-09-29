"""Recovery keeps enabled unresolved work alive without bypassing evidence gates."""
import contextlib
import io
import json
import sys
import unittest
from unittest.mock import patch

import runner
import test_portfolio
from test_research import report


class RecoveryTests(unittest.TestCase):
    setUp = test_portfolio.PortfolioTests.setUp
    tearDown = test_portfolio.PortfolioTests.tearDown
    run_step = test_portfolio.PortfolioTests.run_step
    state = test_portfolio.PortfolioTests.state

    def seed(self, local, **global_fields):
        directory = self.root / 'scripts/loop-codex'
        directory.mkdir(exist_ok=True)
        path = directory / 'state.json'
        path.write_text(json.dumps(dict(problems={'riemann': local}, **global_fields)))
        return path

    def test_all_halted_migrate_without_model_calls_or_quota_reset(self):
        original = dict(retry_at=9999999999, problems={slug: {
            'research_halt': 'Two consecutive stalled research turns, regardless of history edits.',
            'stalled_turns': 2} for slug in self.ids})
        path = self.seed({})
        path.write_text(json.dumps(original))
        with patch.object(sys, 'argv', ['runner.py', '--recover-research']), patch.object(runner, 'check') as check:
            self.assertEqual(runner.main(), 0)
            check.assert_not_called()
        self.assertFalse(self.calls)
        state = self.state()
        self.assertEqual(state['retry_at'], original['retry_at'])
        for local in state['problems'].values():
            self.assertNotIn('research_halt', local)
            self.assertEqual(local['stalled_turns'], 2)
            self.assertTrue(local['require_new_target'])
        self.assertEqual(runner.choose(self.rows, state, lambda _: False)[0], 'riemann')

    def test_status_is_read_only_and_does_not_check_login(self):
        path = self.seed({'research_halt': 'saved reason'})
        before = path.read_bytes()
        output = io.StringIO()
        with patch.object(sys, 'argv', ['runner.py', '--status']), patch.object(runner, 'check') as check, contextlib.redirect_stdout(output):
            self.assertEqual(runner.main(), 0)
            check.assert_not_called()
        self.assertEqual(path.read_bytes(), before)
        self.assertIn('saved reason', output.getvalue())
        self.assertFalse(self.calls)

    def test_stalled_rotation_continues_beyond_every_budget(self):
        def stall(*args):
            self.calls.append(args[-1].name)
            (args[-1] / 'PROGRESS.md').write_text(report(str(len(self.calls)), 'STALLED'))
            return 'success', None, 0
        with patch.object(runner, 'run_process', side_effect=stall):
            for _ in range(4 * len(self.ids)):
                self.assertEqual(runner.main(), 0)
        self.assertEqual(self.calls, self.ids * 4)
        for local in self.state()['problems'].values():
            self.assertNotIn('research_halt', local)
            self.assertIn('research_recovery', local)
            self.assertEqual(local['stalled_turns'], 2)

    def test_single_notebook_keeps_running_until_interrupted(self):
        def stall(*args):
            self.calls.append(args[-1].name)
            if len(self.calls) == 7:
                runner.STOP = True
                return 'interrupted', None, 130
            (args[-1] / 'PROGRESS.md').write_text(report(str(len(self.calls)), 'STALLED'))
            return 'success', None, 0
        with patch.object(sys, 'argv', ['runner.py', '--problem', 'riemann']), patch.object(runner, 'run_process', side_effect=stall):
            self.assertEqual(runner.main(), 130)
        self.assertEqual(self.calls, ['riemann'] * 7)
        self.assertNotIn('research_halt', self.state()['problems']['riemann'])

    def test_exhausted_route_requires_new_target_then_resumes(self):
        self.seed({'research_halt': 'Three exploration turns without an advance or informative negative result.',
                   'exploration_turns': 3})
        runner.main()  # Fresh ADVANCE report alone cannot renew the same target.
        self.assertIn('research_recovery', self.state()['problems']['riemann'])
        self.assertEqual(self.state()['problems']['riemann']['exploration_turns'], 3)
        def redirect(*args):
            notebook = args[-1]
            self.assertIn('A different Next action is required', args[1])
            self.assertIn('LITERATURE-ONLY', args[1])
            source = notebook / 'drafts/literature/test.md'
            source.with_name('next.md').write_text(source.read_text().replace('TARGET: test', 'TARGET: independent target'))
            text = report('redirect', 'EXPLORATION').replace('Next action: test', 'Next action: independent target').replace(
                'NEXT_REVIEW: drafts/literature/test.md', 'NEXT_REVIEW: drafts/literature/next.md')
            (notebook / 'PROGRESS.md').write_text(text)
            return 'success', None, 0
        with patch.object(sys, 'argv', ['runner.py', '--once', '--problem', 'riemann']), patch.object(runner, 'run_process', side_effect=redirect):
            runner.main()
        local = self.state()['problems']['riemann']
        self.assertNotIn('research_recovery', local)
        self.assertEqual(local['exploration_turns'], 1)
        self.assertIn('last_research_stop', local)

    def test_invalid_recovery_cannot_derive_or_accept_resolution(self):
        self.seed({'research_halt': 'invalid report', 'exploration_turns': 2})
        def bypass(*args):
            self.assertIn('LITERATURE-ONLY', args[1])
            (args[-1] / 'PROGRESS.md').write_text(report('bypass', 'ADVANCE').replace(
                'STATUS: IN_PROGRESS', 'STATUS: PROVED').replace('STEP_KIND: LITERATURE', 'STEP_KIND: RESEARCH'))
            return 'success', None, 0
        with patch.object(runner, 'run_process', side_effect=bypass):
            runner.main()
        local = self.state()['problems']['riemann']
        self.assertIn('research_recovery', local)
        self.assertEqual(local['exploration_turns'], 2)
        self.assertEqual(runner.choose(self.rows, self.state(), lambda _: True)[0], 'riemann')

    def test_configuration_failure_waits_until_user_interrupt(self):
        def stop_wait(stamp):
            self.assertGreater(stamp, 0)
            runner.STOP = True
        with patch.object(sys, 'argv', ['runner.py']), patch.object(runner, 'check', side_effect=RuntimeError('login required')), patch.object(runner, 'wait_until', side_effect=stop_wait):
            self.assertEqual(runner.main(), 130)
        self.assertFalse(self.calls)
        self.assertEqual(self.state()['outcome'], 'configuration')

    def test_fatal_service_response_is_retried_not_permanently_stopped(self):
        with patch.object(runner, 'run_process', return_value=('fatal', None, 1)):
            self.assertEqual(runner.main(), 1)
        self.assertGreater(self.state()['retry_at'], 0)
        self.assertEqual(runner.main(), 0)
        self.assertEqual(self.calls, ['riemann'])


if __name__ == '__main__':
    unittest.main()
