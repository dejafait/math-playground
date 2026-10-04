"""Best-effort local accounting: no model calls or source-content copies."""
import json
from pathlib import Path
import sqlite3
import time

from routing import profile_home
from input_scope import notebooks, audit

SCHEMA_VERSION = 1
TOKEN_KEYS = ('input_tokens', 'cached_input_tokens', 'output_tokens', 'reasoning_output_tokens', 'total_tokens')


def normalize(usage):
    if not isinstance(usage, dict):
        return None
    result = {k: usage.get(k) for k in TOKEN_KEYS}
    if not all(isinstance(result[k], int) and result[k] >= 0 for k in ('input_tokens', 'cached_input_tokens', 'output_tokens')):
        return None
    result['fresh_input_tokens'] = max(0, result['input_tokens'] - result['cached_input_tokens'])
    return result


def summarize(path):
    requests, fallback, seen = [], [], set()
    tools, outputs, pending = {}, [], {}
    compactions, malformed, resets = 0, 0, 0
    previous = {}
    active, slugs = None, []
    broad_reads, sibling_reads = 0, {}
    actual_model = actual_effort = allowance = None
    with Path(path).open() as handle:
        for line in handle:
            try:
                event = json.loads(line)
                payload = event.get('payload', {})
                category, kind = event.get('type'), payload.get('type')
            except (ValueError, AttributeError):
                malformed += 1
                continue
            if category == 'session_meta' and payload.get('cwd'):
                active = Path(payload['cwd']).name
                slugs = notebooks(payload['cwd'])
            if category == 'turn_context':
                actual_model, actual_effort = payload.get('model'), payload.get('effort')
            if category == 'compacted' or kind == 'context_compacted':
                compactions += 1
            if category == 'response_item' and kind in ('function_call', 'custom_tool_call'):
                name = payload.get('name', 'unknown')
                tools[name] = tools.get(name, 0) + 1
                pending[payload.get('call_id')] = name
                scope = audit(payload.get('arguments', payload.get('input', '')), active, slugs)
                broad_reads += int(scope['broad_read'])
                for slug in scope['sibling_notebooks']:
                    sibling_reads[slug] = sibling_reads.get(slug, 0) + 1
            if category == 'response_item' and kind in ('function_call_output', 'custom_tool_call_output'):
                output = payload.get('output', '')
                size = len((output if isinstance(output, str) else json.dumps(output)).encode())
                outputs.append({'tool': pending.pop(payload.get('call_id'), 'unknown'), 'bytes': size})
            if category == 'token_usage_record':
                ident = payload.get('response_id')
                usage = normalize(payload.get('usage'))
                if ident and ident not in seen and usage:
                    seen.add(ident)
                    requests.append(dict(usage, response_id=ident, timestamp=event.get('timestamp'),
                                         model=actual_model, effort=actual_effort))
            if category == 'event_msg' and kind == 'token_count':
                if payload.get('rate_limits') is not None:
                    allowance = payload['rate_limits']
                total = normalize((payload.get('info') or {}).get('total_token_usage'))
                if total:
                    values = {k: v for k, v in total.items() if isinstance(v, int)}
                    if any(values.get(k, 0) < previous.get(k, 0) for k in values):
                        resets += 1
                        previous = {}
                    delta = {k: v - previous.get(k, 0) for k, v in values.items()}
                    if delta.get('input_tokens', 0) or delta.get('output_tokens', 0):
                        fallback.append(dict(delta, timestamp=event.get('timestamp'), model=actual_model, effort=actual_effort))
                    previous = values
    source = 'response_usage' if requests else 'cumulative_deltas'
    requests = requests or fallback
    totals = {k: sum(r[k] for r in requests) if requests and all(isinstance(r.get(k), int) for r in requests) else None
              for k in (*TOKEN_KEYS, 'fresh_input_tokens')}
    summary = dict(schema_version=SCHEMA_VERSION, collector_version=1,
                   collection_status='complete' if requests and not malformed else 'partial',
                   usage_source=source if requests else 'unavailable', tokens=totals,
                   request_count=len(requests) if requests else None, compactions=compactions,
                   counter_resets=resets, malformed_events=malformed, tool_calls=tools,
                   input_scope_audit={'broad_read_commands': broad_reads, 'sibling_read_commands': sibling_reads,
                                      'coverage': 'heuristic_command_patterns_not_read_enforcement'},
                   tool_output_bytes=sum(r['bytes'] for r in outputs),
                   largest_tool_outputs=sorted(outputs, key=lambda r: r['bytes'], reverse=True)[:10],
                   actual_model=actual_model, actual_effort=actual_effort,
                   allowance_observation=allowance, output_size_unit='bytes_not_tokens')
    return summary, requests


def collect(thread_id, directory, home=None):
    started = time.monotonic()
    summary = dict(schema_version=SCHEMA_VERSION, collector_version=1, collection_status='unavailable')
    try:
        if thread_id:
            home = home or profile_home()
            with sqlite3.connect((home / 'state_5.sqlite').as_uri() + '?mode=ro', uri=True) as db:
                row = db.execute('SELECT rollout_path FROM threads WHERE id=?', (thread_id,)).fetchone()
            if row:
                summary, requests = summarize(row[0])
                with (Path(directory) / 'requests.jsonl').open('a') as handle:
                    for index, request in enumerate(requests):
                        handle.write(json.dumps(dict(request, thread_id=thread_id, request_index=index,
                                                     schema_version=SCHEMA_VERSION)) + '\n')
    except (OSError, sqlite3.Error, ValueError, TypeError) as exc:
        summary.update(collection_status='partial', collection_error=type(exc).__name__)
    summary['collection_seconds'] = time.monotonic() - started
    return summary
