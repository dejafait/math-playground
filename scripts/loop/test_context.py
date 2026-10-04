"""Startup context preserves mathematics and avoids redundant pipe reads."""
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

import context
import inspect_json
import runner


class ContextTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.notebook = self.root / 'riemann'
        self.notebook.mkdir()
        for name in ('GOAL.md', 'PROOF.md', 'DAG.md'):
            (self.notebook / name).write_text('Exact α proof hypothesis\n' + name)
        (self.root / 'GOAL.md').write_text('Shared exact policy\n')

    def test_full_orientation_and_stable_shared_prefix(self):
        shared = context.shared(self.root, 'Literal $(not-shell) prompt')
        self.assertTrue(shared.startswith('Literal $(not-shell) prompt'))
        self.assertIn('Shared exact policy\n', shared)
        text = context.notebook_context(self.notebook, 'STATUS: IN_PROGRESS\n', None)
        for name in ('GOAL.md', 'PROOF.md', 'DAG.md'):
            self.assertIn((self.notebook / name).read_text(), text)
        self.assertIn('STATUS: IN_PROGRESS\n', text)
        self.assertNotIn('collatz', text)

    def test_large_assessment_is_marked_omitted_not_truncated(self):
        directory = self.notebook / 'drafts/literature'
        directory.mkdir(parents=True)
        path = directory / 'review.md'
        path.write_text('never silently truncated ' * 2000)
        text = context.notebook_context(self.notebook, 'checkpoint', 'drafts/literature/review.md')
        self.assertIn('NOT SUPPLIED', text)
        self.assertNotIn('never silently truncated', text)

    def test_optional_path_cannot_load_sibling(self):
        sibling = self.root / 'collatz'
        sibling.mkdir()
        (sibling / 'proof.md').write_text('secret sibling hypothesis')
        text = context.notebook_context(self.notebook, 'checkpoint', '../collatz/proof.md')
        self.assertNotIn('secret sibling', text)

    def test_symlink_assessment_cannot_load_outside(self):
        directory = self.notebook / 'drafts/literature'
        directory.mkdir(parents=True)
        outside = self.root / 'outside.md'
        outside.write_text('outside content')
        (directory / 'link.md').symlink_to(outside)
        text = context.notebook_context(self.notebook, 'checkpoint', 'drafts/literature/link.md')
        self.assertNotIn('outside content', text)

    def test_large_literal_stdin_does_not_deadlock(self):
        value = 'α $(literal)\n' * 100000
        code = "import sys; text=sys.stdin.read(); assert len(text)==%d; print('{\"type\":\"turn.completed\"}')" % len(value)
        with patch.object(runner, 'STOP', False):
            result = runner.run_process([sys.executable, '-c', code], value, self.root, 10, notebook=self.notebook)
        self.assertEqual(result, ('success', None, 0))

    def test_preview_explicitly_marks_omissions_and_exact_selection(self):
        data = {'certificate': [str(i) for i in range(100)], 'large': 'x' * 1000}
        result = inspect_json.preview(data)
        self.assertEqual(result['preview']['certificate']['length'], 100)
        self.assertEqual(result['preview']['certificate']['omitted_items'], 97)
        self.assertTrue(result['preview']['large']['truncated'])
        self.assertEqual(inspect_json.select(data, '/certificate/99'), '99')
        self.assertEqual(inspect_json.select({'a/b': {'~': 4}}, '/a~1b/~0'), 4)


if __name__ == '__main__':
    unittest.main()
