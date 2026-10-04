"""Focus-policy diagnostics and approval without repeating completed mathematics."""
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

import input_scope
import literature
import runner
import test_portfolio
from test_loop import review_fixture
from test_research import report


class ScopeTests(unittest.TestCase):
    def test_local_and_sibling_reads(self):
        slugs = ['riemann', 'collatz']
        self.assertFalse(input_scope.audit('rg claim lemmas', 'riemann', slugs)['broad_read'])
        self.assertEqual(input_scope.audit('sed -n 1,30p ../collatz/PROOF.md', 'riemann', slugs)['sibling_notebooks'], ['collatz'])
        self.assertEqual(input_scope.audit('cat ../GOAL.md', 'riemann', slugs)['sibling_notebooks'], [])
        self.assertEqual(input_scope.audit('git status --short ../collatz/', 'riemann', slugs)['sibling_notebooks'], [])

    def test_broad_patterns_are_flags_not_shell_enforcement(self):
        for text in ['cat ../*/PROGRESS.md', 'rg claim ..', "Path('.').glob('*/PROGRESS.md')"]:
            self.assertTrue(input_scope.audit(text, 'riemann', [])['broad_read'], text)

    def test_new_assessment_defers_only_continuation(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            review_fixture(root, 'SPECIALIZE')
            before = report('before', 'EXPLORATION')
            ctx = literature.prepare(root, before)
            source = root / 'drafts/literature/test.md'
            source.with_name('next.md').write_text(source.read_text().replace('TARGET: test', 'TARGET: next'))
            after = report('proof', 'ADVANCE').replace('STEP_KIND: LITERATURE', 'STEP_KIND: RESEARCH').replace(
                'NOVELTY_UNCHECKED', 'REPRODUCTION').replace('Next action: test', 'Next action: next').replace(
                'NEXT_REVIEW: drafts/literature/test.md', 'NEXT_REVIEW: drafts/literature/next.md')
            self.assertIsNone(literature.validate_turn(root, ctx, after))
            self.assertTrue(literature.continuation_requires_review(root, ctx, after))
            ctx = literature.prepare(root, before)  # Now saved before invocation.
            self.assertFalse(literature.continuation_requires_review(root, ctx, after))


class ContinuationRunnerTests(unittest.TestCase):
    setUp = test_portfolio.PortfolioTests.setUp
    tearDown = test_portfolio.PortfolioTests.tearDown
    state = test_portfolio.PortfolioTests.state
    run_step = test_portfolio.PortfolioTests.run_step

    def test_completed_proof_then_approval_then_mathematics(self):
        notebook = self.root / 'riemann'
        review_fixture(notebook, 'SPECIALIZE')
        def prove(*args):
            self.assertTrue(args[1].startswith((self.root / 'PROMPT.md').read_text()))
            source = notebook / 'drafts/literature/test.md'
            source.with_name('next.md').write_text(source.read_text().replace('TARGET: test', 'TARGET: next'))
            text = report('proof', 'ADVANCE').replace('STEP_KIND: LITERATURE', 'STEP_KIND: RESEARCH').replace(
                'NOVELTY_UNCHECKED', 'REPRODUCTION').replace('Next action: test', 'Next action: next').replace(
                'NEXT_REVIEW: drafts/literature/test.md', 'NEXT_REVIEW: drafts/literature/next.md')
            (notebook / 'PROGRESS.md').write_text(text)
            return 'success', None, 0
        def approve(*args):
            self.assertIn('LITERATURE-ONLY', args[1])
            text = (notebook / 'PROGRESS.md').read_text().replace('STEP_ID: proof', 'STEP_ID: approval').replace(
                'STEP_KIND: RESEARCH', 'STEP_KIND: LITERATURE').replace('REPRODUCTION', 'NOVELTY_UNCHECKED').replace(
                'STEP_REVIEW: drafts/literature/test.md', 'STEP_REVIEW: drafts/literature/next.md')
            (notebook / 'PROGRESS.md').write_text(text)
            return 'success', None, 0
        def following(*args):
            self.assertNotIn('LITERATURE-ONLY', args[1])
            text = (notebook / 'PROGRESS.md').read_text().replace('STEP_ID: approval', 'STEP_ID: following').replace(
                'STEP_KIND: LITERATURE', 'STEP_KIND: RESEARCH').replace('NOVELTY_UNCHECKED', 'REPRODUCTION')
            (notebook / 'PROGRESS.md').write_text(text)
            return 'success', None, 0
        with patch.object(sys, 'argv', ['runner.py', '--once', '--problem', 'riemann']):
            with patch.object(runner, 'run_process', side_effect=prove):
                runner.main()
            local = self.state()['problems']['riemann']
            self.assertEqual(local['research_outcome'], 'ADVANCE')
            self.assertNotIn('research_recovery', local)
            self.assertEqual(local['pending_review_target'], 'next')
            with patch.object(runner, 'run_process', side_effect=approve):
                runner.main()
            self.assertNotIn('pending_review_target', self.state()['problems']['riemann'])
            with patch.object(runner, 'run_process', side_effect=following):
                runner.main()

    def test_historical_next_target_stop_accepts_stalled_process_repair(self):
        directory = self.root / 'scripts/loop-codex'
        directory.mkdir(exist_ok=True)
        reason = 'A new next target needs its own literature review turn.'
        (directory / 'state.json').write_text(json.dumps({'problems': {'riemann': {
            'research_recovery': 'Recovery remains stalled; reassess the route instead of renewing its budget.',
            'first_research_stop': {'reason': reason}, 'require_new_target': True}}}))
        review_fixture(self.root / 'riemann', 'SPECIALIZE')
        def repair(*args):
            self.assertNotIn('A different Next action is required', args[1])
            (args[-1] / 'PROGRESS.md').write_text(report('repair', 'STALLED'))
            return 'success', None, 0
        with patch.object(sys, 'argv', ['runner.py', '--once', '--problem', 'riemann']), patch.object(runner, 'run_process', side_effect=repair):
            runner.main()
        self.assertNotIn('research_recovery', self.state()['problems']['riemann'])


if __name__ == '__main__':
    unittest.main()
