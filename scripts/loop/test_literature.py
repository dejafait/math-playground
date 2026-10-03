"""Exercise actual gate transitions, malformed evidence and budget protection."""
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import literature
import runner
from test_loop import review_fixture
from test_research import report
import test_portfolio


class LiteratureTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        review_fixture(self.root)
        self.path = self.root / 'drafts/literature/test.md'
        self.progress = report('initial', 'EXPLORATION')

    def result(self, kind='LITERATURE', classification='NOVELTY_UNCHECKED'):
        return report('new', 'ADVANCE').replace('STEP_KIND: LITERATURE', 'STEP_KIND: ' + kind).replace(
            'STEP_CLASSIFICATION: NOVELTY_UNCHECKED', 'STEP_CLASSIFICATION: ' + classification)

    def test_missing_assessment_selects_review_not_research(self):
        ctx = literature.prepare(self.root, 'Next action: test\n')
        self.assertIn('LITERATURE-ONLY', literature.instruction(ctx))
        self.assertIsNone(literature.validate_turn(self.root, ctx, self.result()))
        self.assertIsNotNone(literature.validate_turn(self.root, ctx, self.result('RESEARCH', 'POTENTIALLY_NEW')))

    def test_review_can_clear_gate_only_for_following_turn(self):
        ctx = literature.prepare(self.root, self.progress)
        review_fixture(self.root, 'SPECIALIZE')
        self.assertIsNone(literature.validate_turn(self.root, ctx, self.result()))
        self.assertIsNotNone(literature.validate_turn(self.root, ctx, self.result('RESEARCH', 'REPRODUCTION')))
        following = literature.prepare(self.root, self.progress)
        self.assertIsNone(literature.validate_turn(self.root, following, self.result('RESEARCH', 'REPRODUCTION')))

    def test_ready_review_is_reusable_without_rewriting_or_searching(self):
        review_fixture(self.root, 'EXPLORE')
        for _ in range(2):
            ctx = literature.prepare(self.root, self.progress)
            self.assertIsNone(literature.validate_turn(self.root, ctx, self.result('RESEARCH', 'POTENTIALLY_NEW')))

    def test_source_blocked_cannot_authorize_research(self):
        review_fixture(self.root, 'SOURCE_BLOCKED')
        ctx = literature.prepare(self.root, self.progress)
        self.assertIsNotNone(literature.validate_turn(self.root, ctx, self.result('RESEARCH', 'REPRODUCTION')))

    def test_ready_requires_source_and_completion_requires_next_assessment(self):
        review_fixture(self.root, 'EXPLORE')
        self.path.write_text(self.path.read_text().replace('https://example.org/paper', 'unread source'))
        ctx = literature.prepare(self.root, self.progress)
        self.assertEqual(ctx['decision'], 'REVIEW_REQUIRED')
        review_fixture(self.root)
        self.assertIsNotNone(literature.validate_turn(self.root, ctx, self.result().replace('NEXT_REVIEW:', 'Next review:')))

    def test_source_links_in_detailed_body_are_accepted(self):
        review_fixture(self.root, 'SPECIALIZE')
        self.path.write_text(self.path.read_text().replace(
            'https://example.org/paper', 'Theorem 1; direct link below.')
            + '\nSource: https://example.org/paper\n')
        self.assertEqual(literature.prepare(self.root, self.progress)['decision'], 'SPECIALIZE')

    def test_import_requires_import_classification(self):
        review_fixture(self.root, 'IMPORT')
        ctx = literature.prepare(self.root, self.progress)
        self.assertIsNone(literature.validate_turn(self.root, ctx, self.result('RESEARCH', 'KNOWN_IMPORTED')))
        for classification in ('REPRODUCTION', 'POTENTIALLY_NEW', 'NOVELTY_UNCHECKED'):
            self.assertIsNotNone(literature.validate_turn(self.root, ctx, self.result('RESEARCH', classification)))

    def test_changed_target_requires_new_review(self):
        changed = self.progress.replace('Next action: test', 'Next action: different')
        self.assertEqual(literature.prepare(self.root, changed)['decision'], 'REVIEW_REQUIRED')

    def test_literature_can_approve_new_next_target(self):
        ctx = literature.prepare(self.root, self.progress)
        other = self.path.with_name('next.md')
        other.write_text(self.path.read_text().replace('TARGET: test', 'TARGET: next').replace('REVIEW_REQUIRED', 'EXPLORE'))
        after = self.result().replace('Next action: test', 'Next action: next').replace(
            'NEXT_REVIEW: drafts/literature/test.md', 'NEXT_REVIEW: drafts/literature/next.md')
        self.assertIsNone(literature.validate_turn(self.root, ctx, after))
        other.write_text(other.read_text().replace('EXPLORE', 'REVIEW_REQUIRED'))
        self.assertIsNone(literature.validate_turn(self.root, ctx, after))

    def test_preapproved_subtarget_reuses_scope(self):
        review_fixture(self.root, 'EXPLORE')
        self.path.write_text(self.path.read_text() + '\nSCOPE: test and its bounded subcases\nCOVERED_TARGET: subcase\n')
        progress = self.progress.replace('Next action: test', 'Next action: subcase')
        self.assertEqual(literature.prepare(self.root, progress)['decision'], 'EXPLORE')
        ctx = literature.prepare(self.root, self.progress)
        after = self.result('RESEARCH', 'POTENTIALLY_NEW').replace('Next action: test', 'Next action: subcase')
        self.assertIsNone(literature.validate_turn(self.root, ctx, after))

    def test_evidence_cannot_be_rewritten_during_research(self):
        review_fixture(self.root, 'EXPLORE')
        ctx = literature.prepare(self.root, self.progress)
        self.path.write_text(self.path.read_text() + '\nChanged hypothesis.\n')
        self.assertIsNotNone(literature.validate_turn(self.root, ctx, self.result('RESEARCH', 'POTENTIALLY_NEW')))

    def test_literature_turn_cannot_add_lemma_or_program(self):
        for folder in ('lemmas', 'scripts'):
            with self.subTest(folder=folder):
                ctx = literature.prepare(self.root, self.progress)
                d = self.root / folder
                d.mkdir(exist_ok=True)
                (d / 'result.txt').write_text('new mathematical artifact')
                self.assertIsNotNone(literature.validate_turn(self.root, ctx, self.result()))

    def test_malformed_evidence_and_duplicate_fields(self):
        original = self.path.read_text()
        for bad in (original + 'DECISION: IMPORT\n', original.replace('TARGET:', 'Target:'),
                    original.replace('2026-09-26', '2026-99-99'),
                    original.replace('REVIEW_REQUIRED', 'UNKNOWN'),
                    original.replace('SOURCE_EVIDENCE:', 'Sources:')):
            with self.subTest(bad=bad):
                self.path.write_text(bad)
                self.assertEqual(literature.prepare(self.root, self.progress)['decision'], 'REVIEW_REQUIRED')
                self.assertIsNotNone(literature.validate_turn(self.root, literature.prepare(self.root, self.progress), self.result()))

    def test_paths_cannot_escape_review_directory(self):
        for reference in ('../outside.md', '/tmp/outside.md', 'PROGRESS.md'):
            with self.assertRaises(ValueError):
                literature.read_review(self.root, reference, 'test')
        outside = self.root / 'outside.md'
        outside.write_text(self.path.read_text())
        link = self.path.with_name('link.md')
        link.symlink_to(outside)
        with self.assertRaises(ValueError):
            literature.read_review(self.root, 'drafts/literature/link.md', 'test')


class LiteratureRunnerTests(unittest.TestCase):
    setUp = test_portfolio.PortfolioTests.setUp
    tearDown = test_portfolio.PortfolioTests.tearDown
    run_step = test_portfolio.PortfolioTests.run_step
    state = test_portfolio.PortfolioTests.state

    def test_ten_notebook_review_then_research_round(self):
        def review(*args):
            notebook = args[-1]
            self.assertIn('LITERATURE-ONLY', args[1])
            review_fixture(notebook, 'SPECIALIZE')
            return self.run_step(*args)
        with patch.object(runner, 'run_process', side_effect=review):
            for _ in self.ids:
                self.assertEqual(runner.main(), 0)
        self.assertEqual(self.calls, self.ids)
        self.assertFalse(any(s.get('research_halt') for s in self.state()['problems'].values()))
        def research(*args):
            self.assertNotIn('LITERATURE-ONLY', args[1])
            notebook = args[-1]
            self.calls.append(notebook.name)
            (notebook / 'PROGRESS.md').write_text(report('research', 'ADVANCE').replace(
                'STEP_KIND: LITERATURE', 'STEP_KIND: RESEARCH').replace('NOVELTY_UNCHECKED', 'REPRODUCTION'))
            return 'success', None, 0
        with patch.object(runner, 'run_process', side_effect=research):
            for _ in self.ids:
                self.assertEqual(runner.main(), 0)
        self.assertEqual(self.calls, self.ids * 2)
        self.assertFalse(any(s.get('research_halt') for s in self.state()['problems'].values()))

    def test_violation_queues_recovery_without_resetting_budget(self):
        directory = self.root / 'scripts/loop-codex'
        directory.mkdir()
        (directory / 'state.json').write_text(json.dumps({'problems': {
            'riemann': {'exploration_turns': 2}}, 'retry_at': 0}))
        def bypass(*args):
            notebook = args[-1]
            self.assertIn('LITERATURE-ONLY', args[1])
            text = report('bypass', 'ADVANCE').replace('STEP_KIND: LITERATURE', 'STEP_KIND: RESEARCH').replace(
                'NOVELTY_UNCHECKED', 'POTENTIALLY_NEW')
            text = text.replace('STATUS: IN_PROGRESS', 'STATUS: PROVED')
            (notebook / 'PROGRESS.md').write_text(text)
            return 'success', None, 0
        with patch.object(runner, 'run_process', side_effect=bypass):
            runner.main()
        state = self.state()['problems']['riemann']
        self.assertIn('research_recovery', state)
        self.assertEqual(state['exploration_turns'], 2)
        runner.main()
        self.assertEqual(self.calls, ['problem-1'])


if __name__ == '__main__':
    unittest.main()
