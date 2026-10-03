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
from test_loop import portfolio_fixture


def report(step, outcome):
    return f'STATUS: IN_PROGRESS\nSTEP_ID: {step}\nSTEP_OUTCOME: {outcome}\nSTEP_EVIDENCE: Tested mechanism; history/test.md\nSTEP_KIND: LITERATURE\nSTEP_CLASSIFICATION: NOVELTY_UNCHECKED\nSTEP_REVIEW: drafts/literature/test.md\nNEXT_REVIEW: drafts/literature/test.md\nNext action: test\n'


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
            self.assertIsNone(research.assess(state, '', report(str(i), 'EXPLORATION').replace('STEP_KIND: LITERATURE', 'STEP_KIND: RESEARCH'), True))
        research.assess(state, '', report('negative', 'NEGATIVE').replace('STEP_KIND: LITERATURE', 'STEP_KIND: RESEARCH'), True)
        self.assertEqual(state['exploration_turns'], 0)
        for i in range(2):
            self.assertIsNone(research.assess(state, '', report('new'+str(i), 'EXPLORATION').replace('STEP_KIND: LITERATURE', 'STEP_KIND: RESEARCH'), True))
        self.assertIsNotNone(research.assess(state, '', report('third', 'EXPLORATION').replace('STEP_KIND: LITERATURE', 'STEP_KIND: RESEARCH'), True))

    def test_literature_does_not_spend_calculation_budget(self):
        state = {'exploration_turns': 2}
        for i in range(5):
            self.assertIsNone(research.assess(state, '', report(str(i), 'EXPLORATION'), True))
        self.assertEqual(state['exploration_turns'], 2)
        self.assertIn('20%', research.balance_instruction({'turn_mix': ['RESEARCH'] * 4}, True))
        self.assertIn('mathematical attempt now', research.balance_instruction(state, True))

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
        self.assertEqual((state['retry_at'], state['failures'], state['unknowns']), (12345, 2, 0))
        self.assertEqual(state['exploration_turns'], 0)



if __name__ == '__main__':
    unittest.main()
