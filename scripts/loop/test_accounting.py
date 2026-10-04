"""Accounting must not double-count usage or burden mathematical reports."""
import json
from pathlib import Path
import tempfile
import unittest

from accounting import summarize, collect


def usage(i=100, cached=80, out=10, reasoning=4):
    return dict(input_tokens=i, cached_input_tokens=cached, output_tokens=out,
                reasoning_output_tokens=reasoning, total_tokens=i+out)


class AccountingTests(unittest.TestCase):
    def parse(self, events):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'session.jsonl'
            path.write_text(''.join(json.dumps(e)+'\n' for e in events))
            return summarize(path)

    def test_response_records_deduplicate_and_exclude_subcategory_double_count(self):
        event = {'type': 'token_usage_record', 'payload': {'response_id': 'r1', 'usage': usage()}}
        summary, requests = self.parse([{'type': 'turn_context', 'payload': {'model': 'gpt-6-astra', 'effort': 'high'}},
                                        event, event,
                                        {'type': 'token_usage_record', 'payload': {'response_id': 'r2', 'usage': usage()}}])
        self.assertEqual(summary['request_count'], 2)
        self.assertEqual(summary['tokens']['total_tokens'], 220)
        self.assertEqual(summary['tokens']['fresh_input_tokens'], 40)
        self.assertEqual(summary['tokens']['reasoning_output_tokens'], 8)
        self.assertEqual(requests[0]['model'], 'gpt-6-astra')

    def test_old_counter_deltas_repeats_and_resets(self):
        def event(u):
            return {'type': 'event_msg', 'payload': {'type': 'token_count', 'info': {'total_token_usage': u}}}
        summary, requests = self.parse([event(usage()), event(usage()), event(usage(200,160,20,8)), event(usage())])
        self.assertEqual(summary['request_count'], 3)
        self.assertEqual(summary['counter_resets'], 1)
        self.assertEqual(summary['tokens']['input_tokens'], 300)
        self.assertEqual(summary['usage_source'], 'cumulative_deltas')

    def test_output_sizes_no_content_and_compaction(self):
        summary, _ = self.parse([
            {'type': 'response_item', 'payload': {'type': 'function_call', 'call_id': 'c', 'name': 'read_file'}},
            {'type': 'response_item', 'payload': {'type': 'function_call_output', 'call_id': 'c', 'output': 'private passage'}},
            {'type': 'compacted', 'payload': {}}])
        self.assertEqual(summary['tool_output_bytes'], 15)
        self.assertEqual(summary['compactions'], 1)
        self.assertNotIn('private passage', json.dumps(summary))
        self.assertIsNone(summary['tokens']['input_tokens'])

    def test_missing_session_is_nonfatal_and_timed(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = collect('missing', Path(tmp), Path(tmp))
            self.assertEqual(result['collection_status'], 'partial')
            self.assertGreaterEqual(result['collection_seconds'], 0)
            self.assertEqual(collect(None, Path(tmp))['collection_status'], 'unavailable')

    def test_input_scope_audit_uses_registry_without_source_copy(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'scripts/loop').mkdir(parents=True)
            (root / 'scripts/loop/problems.json').write_text(json.dumps([{'id': 'riemann'}, {'id': 'collatz'}]))
            path = root / 'session.jsonl'
            events = [
                {'type': 'session_meta', 'payload': {'cwd': str(root / 'riemann')}},
                {'type': 'response_item', 'payload': {'type': 'custom_tool_call', 'name': 'exec',
                                                     'input': 'cat ../collatz/PROOF.md'}},
                {'type': 'response_item', 'payload': {'type': 'custom_tool_call', 'name': 'exec',
                                                     'input': 'rg claim ..'}}]
            path.write_text(''.join(json.dumps(e)+'\n' for e in events))
            summary, _ = summarize(path)
            self.assertEqual(summary['input_scope_audit']['sibling_read_commands'], {'collatz': 1})
            self.assertEqual(summary['input_scope_audit']['broad_read_commands'], 1)
            self.assertNotIn('cat ../collatz', json.dumps(summary))

    def test_reasoning_unavailable_is_null(self):
        u=usage();del u['reasoning_output_tokens']
        summary,_=self.parse([{'type': 'token_usage_record', 'payload': {'response_id': 'r', 'usage': u}}])
        self.assertIsNone(summary['tokens']['reasoning_output_tokens'])


if __name__ == '__main__':
    unittest.main()
