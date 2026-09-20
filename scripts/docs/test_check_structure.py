"""Regression checks for the compact canonical dependency format."""
import unittest
from check_structure import parse_dag

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


if __name__ == '__main__':
    unittest.main()
