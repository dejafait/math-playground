"""Regression coverage for repeated stop reports and bounded discovery."""
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent))
import research
import runner


def report(step, outcome):
    return f'STATUS: IN_PROGRESS\nSTEP_ID: {step}\nSTEP_OUTCOME: {outcome}\nSTEP_EVIDENCE: Tested mechanism; history/test.md\nNext action: test\n'


class ResearchTests(unittest.TestCase):
    def test_history_only_cannot_reuse_old_advance(self):
        state = {}
        text = report('old', 'ADVANCE')
        for _ in range(2):
            self.assertIsNone(research.assess(state, text, text, True))
        self.assertIsNotNone(research.assess(state, text, text, True))

    def test_stalled_reports_stop_despite_new_history(self):
        state = {}
        self.assertIsNone(research.assess(state, '', report('1', 'STALLED'), True))
        self.assertIsNotNone(research.assess(state, report('1', 'STALLED'), report('2', 'STALLED'), True))

    def test_exploration_budget_and_useful_negative(self):
        state = {}
        for i in range(2):
            self.assertIsNone(research.assess(state, '', report(str(i), 'EXPLORATION'), True))
        research.assess(state, '', report('negative', 'NEGATIVE'), True)
        self.assertEqual(state['exploration_turns'], 0)
        for i in range(2):
            self.assertIsNone(research.assess(state, '', report('new'+str(i), 'EXPLORATION'), True))
        self.assertIsNotNone(research.assess(state, '', report('third', 'EXPLORATION'), True))

    def test_invalid_reports_do_not_reset_budget(self):
        for text in ['', report('1', 'UNKNOWN'), report('1', 'ADVANCE')+'STEP_OUTCOME: STALLED\n', report('1', 'ADVANCE').replace('STEP_EVIDENCE:', 'Evidence:'), report('1', 'ADVANCE').replace('Tested mechanism; history/test.md', '')]:
            with self.subTest(text=text):
                state = {'exploration_turns': 2}
                for _ in range(3):
                    reason = research.assess(state, '', text, True)
                self.assertIsNotNone(reason)
                self.assertEqual(state['exploration_turns'], 2)

    def test_resume_preserves_quota_fields(self):
        state = dict(research_halt='stop', exploration_turns=3, stalled_turns=2,
                     retry_at=12345, failures=2, unknowns=1, no_progress=3)
        research.resume(state)
        self.assertNotIn('research_halt', state)
        self.assertEqual((state['retry_at'], state['failures'], state['unknowns']), (12345, 2, 1))
        self.assertEqual(state['exploration_turns'], 0)

    def test_runner_persists_stop_and_requires_explicit_resume(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'scripts/loop').mkdir(parents=True)
            (root / 'history').mkdir()
            for name in ('PROMPT.md', 'GOAL.md', 'PROGRESS.md'):
                (root / name).write_text('fixture\n')
            calls = []
            def run(*args):
                calls.append(1)
                (root / 'PROGRESS.md').write_text(report(str(len(calls)), 'STALLED'))
                (root / 'history/test.md').write_text('No new mechanism supplied.\n' * len(calls))
                return 'success', None, 0
            with patch.object(runner, 'ROOT', root), patch.object(runner, 'STOP', False), patch.object(runner, 'check', return_value='fake'), patch.object(runner, 'validate'), patch.object(runner, 'run_process', side_effect=run), patch.object(runner, 'wait_until'), patch.object(sys, 'argv', ['runner.py']):
                self.assertEqual(runner.main(), 2)
                self.assertEqual(len(calls), 2)
                state_path = root / 'scripts/loop-codex/state.json'
                state = json.loads(state_path.read_text())
                self.assertEqual(state['outcome'], 'research_stalled')
                self.assertEqual(runner.main(), 2)
                self.assertEqual(len(calls), 2)
                state['retry_at'] = 9999999999
                state_path.write_text(json.dumps(state))
                def interrupt_wait(stamp):
                    self.assertEqual(stamp, 9999999999)
                    runner.STOP = True
                with patch.object(sys, 'argv', ['runner.py', '--resume-research']), patch.object(runner, 'wait_until', side_effect=interrupt_wait):
                    self.assertEqual(runner.main(), 130)
                self.assertEqual(len(calls), 2)


if __name__ == '__main__':
    unittest.main()
