import json
from pathlib import Path
import tempfile
import unittest

from quota_history import reconstruct, segment


class QuotaHistoryTests(unittest.TestCase):
    def point(self, time, used, reset=10000, plan='pro'):
        return dict(time=time, used=used, reset=reset, plan=plan, minutes=10080)

    def test_deadline_jitter_does_not_invent_resets(self):
        self.assertEqual(len(segment([self.point(1, 10), self.point(2, 11, 10001)])), 1)

    def test_changed_deadline_plan_and_counter_drop_start_new_episodes(self):
        for later in (self.point(2, 11, 20000), self.point(2, 11, plan='prolite'),
                      self.point(2, 0)):
            self.assertEqual(len(segment([self.point(1, 10), later])), 2)

    def test_reconstruction_deduplicates_and_retains_peak_and_missing_numeric_stop(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            logs = root / 'scripts/loop-codex/rh'
            logs.mkdir(parents=True)
            def row(start, used):
                return dict(started_at=start, elapsed_seconds=1, thread_id=str(start),
                            accounting={'allowance_observation': {'plan_type': 'pro',
                            'primary': {'used_percent': used, 'resets_at': 10000,
                                        'window_minutes': 10080}}})
            rows = [row(1, 99), row(2, 100), row(2, 100),
                    dict(started_at=3, elapsed_seconds=1, thread_id='3', outcome='quota')]
            (logs / 'routing.jsonl').write_text('\n'.join(map(json.dumps, rows))+'\ninvalid\n')
            result = reconstruct(root)
            self.assertEqual(result['samples'], 2)
            self.assertEqual(result['episodes'][0]['max_used'], 100)
            self.assertEqual(result['stops'], [{'time': 4, 'limit': None}])
            self.assertEqual(result['malformed'], 1)


if __name__ == '__main__':
    unittest.main()
