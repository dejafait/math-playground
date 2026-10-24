"""Regression checks for the compact canonical dependency format."""
import unittest
from check_structure import parse_dag, overview_errors

HEADER = ('# Lemma dependencies\n\n'
          '`ID: inputs` lists direct mathematical dependencies; empty means none. '
          'Find statements in `lemmas/ID-*.md`.\n\n')


def document(rows):
    return HEADER + '```text\n' + rows + '\n```\n'


class CompactDagTests(unittest.TestCase):
    def test_direction_roots_and_corollaries(self):
        nodes, edges, errors = parse_dag(document('L001:\nL002: L001\nC002a: L001 L002'))
        self.assertFalse(errors)
        self.assertEqual(nodes, {'L001', 'L002', 'C002a'})
        self.assertEqual(edges, {('L001', 'L002'), ('L001', 'C002a'), ('L002', 'C002a')})

    def test_rejects_duplicate_rows_and_inputs(self):
        for rows in ('L001:\nL001:', 'L001:\nL002: L001 L001'):
            with self.subTest(rows=rows):
                self.assertTrue(parse_dag(document(rows))[2])

    def test_rejects_redundant_or_malformed_rows(self):
        for row in ('L001: long title', 'L001: lemmas/L001-example.md',
                    'L001 --> L002', 'L1:', 'L001: L002, L003'):
            with self.subTest(row=row):
                self.assertTrue(parse_dag(document(row))[2])

    def test_rejects_mermaid_and_extra_narrative(self):
        for text in ('```mermaid\nflowchart TD\n```\n',
                     document('L001:') + 'Extra narrative\n', ''):
            self.assertTrue(parse_dag(text)[2])


class StartupBudgetTests(unittest.TestCase):
    def test_single_line_cannot_hide_unbounded_overview(self):
        self.assertIn('UTF-8 bytes', overview_errors('PROOF.md', 'x' * 8193)[0])
        self.assertFalse(overview_errors('PROOF.md', 'x' * 8192))

    def test_measure_utf8_bytes_not_character_count(self):
        self.assertFalse(overview_errors('PROGRESS.md', 'α' * 4096))
        self.assertIn('8194', overview_errors('PROGRESS.md', 'α' * 4097)[0])

    def test_line_budgets_remain_independent(self):
        self.assertIn('100 lines', overview_errors('PROOF.md', 'x\n' * 101)[0])
        self.assertIn('40 lines', overview_errors('PROGRESS.md', 'x\n' * 41)[0])
        self.assertFalse(overview_errors('PROOF.md', 'x\n' * 100))


if __name__ == '__main__':
    unittest.main()
