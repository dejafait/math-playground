import json
from pathlib import Path
import tempfile
import unittest

from loop_review import read_rows, summarize


class LoopReviewTests(unittest.TestCase):
    def test_successful_execution_is_not_mathematical_acceptance(self):
        summary = summarize([dict(started_at=1, outcome='success', validation='missing source',
                                  problem='riemann', research_outcome='ADVANCE')])
        self.assertEqual(summary['execution'], {'success': 1})
        self.assertEqual(summary['accepted_outcomes'], {})

    def test_deduplicate_attempts_and_skip_partial_log_lines(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / 'scripts/loop-codex/riemann/routing.jsonl'
            path.parent.mkdir(parents=True)
            row = dict(started_at=10, thread_id='same')
            path.write_text(json.dumps(row)+'\n'+json.dumps(row)+'\n{"partial":\n')
            self.assertEqual(read_rows(root, 5), [row])
            self.assertEqual(read_rows(root, 11), [])

    def test_gap_excludes_work_time_and_empty_accounting_is_safe(self):
        rows = [dict(started_at=0, elapsed_seconds=3600, outcome='quota'),
                dict(started_at=18000, elapsed_seconds=1, outcome='success')]
        summary = summarize(rows)
        self.assertEqual(summary['gaps_over_three_hours'][0]['hours'], 4)
        self.assertEqual(summary['accounting_samples'], 0)


if __name__ == '__main__':
    unittest.main()
