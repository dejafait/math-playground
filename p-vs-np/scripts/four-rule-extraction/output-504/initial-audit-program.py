"""Step 504: bounded fixed-source observer audit; never run graph preflight.

Observe actual reference selections in the unchanged literal checker. Keep
the original observer running as-is, and compare every selected reference
against the complete immutable source. This is an incompleteness witness,
not a corrected whole-preflight ledger or a graph/equality certificate.
"""
from collections import Counter
import ast
import dis
import json
from pathlib import Path
import sys
import time

import parameterized_input as p
import preflight_job7_transport as original

HERE = Path(__file__).resolve().parent
OUT = HERE / 'output-504'
LIMIT = 100_000_000
SECONDS = 900
RESERVE = 1_000_000


def main():
    p.require(not OUT.exists(), 'fresh audit output; never overwrite')
    OUT.mkdir()
    start = time.monotonic()
    r = original.Run()
    original.R = r
    r.stage = 'fixed source observer audit only'
    p.require(p.CAPS == original.EXPECTED_CAPS, 'unchanged original CAPS')
    report = dict(status='IN_PROGRESS', caps=p.CAPS, item_limit=LIMIT,
                  seconds_limit=SECONDS, reserve_bytes=RESERVE,
                  original_outputs_overwritten=False, graph_regeneration=False,
                  coordinate_search=False, word_expansion=False)
    budget = Counter()
    operations = Counter()
    selections = []
    offsets = {}
    line_charges = Counter()
    checker_path = str(HERE.parent / 'parity-four-rule/checker.py')
    source_path = HERE / 'output-489/inputs/proof.jsonl'
    request_path = HERE / 'output-489/inputs/request.json'

    def tick(kind, n=1):
        if sum(budget.values()) + n > LIMIT:
            raise RuntimeError('audit event/item limit before next event')
        budget[kind] += n
        if sum(budget.values()) % 4096 == 0 and time.monotonic()-start > SECONDS:
            raise RuntimeError('audit timer limit')

    def walk(x):
        tick('independent_json_items')
        if type(x) is dict:
            for k, v in x.items():
                walk(k); walk(v)
        elif type(x) is list:
            for v in x:
                walk(v)

    def observer(frame, event, arg):
        tick('trace_events')
        local = frame.f_code.co_filename == checker_path and frame.f_code.co_name == '_check_stream'
        if local and event == 'call':
            frame.f_trace_opcodes = True
            candidates = [i for i in dis.get_instructions(frame.f_code) if i.opname == 'LIST_APPEND']
            p.require(len(candidates) == 1, 'one reference list comprehension in actual code')
            offsets[candidates[0].offset] = candidates[0].positions.lineno
        before = r.visits
        original.observe_source(frame, event, arg)
        delta = r.visits-before
        if local and frame.f_lineno in offsets.values():
            line_charges[event] += delta
            operations['comprehension_'+event+'_events'] += 1
        if local and event == 'opcode' and frame.f_lasti in offsets:
            tick('reference_selections')
            i, j = frame.f_locals['i'], frame.f_locals['j']
            selections.append(dict(record=i, reference=j, original_charge=delta))
        return observer

    try:
        checker_text = Path(checker_path).read_text()
        node = ast.parse(checker_text)
        fn = next(x for x in node.body if isinstance(x, ast.FunctionDef) and x.name == '_check_stream')
        comps = [x for x in ast.walk(fn) if isinstance(x, ast.ListComp)]
        p.require(len(comps) == 1 and ast.unparse(comps[0]) == '[fs[j] for j in refs]',
                  'independently identify the reference-selection comprehension')
        report['comprehension_source'] = dict(path='scripts/parity-four-rule/checker.py',
            line=comps[0].lineno, expression=ast.unparse(comps[0]))
        raw_before = p.read_bytes(source_path, 'input_bytes')
        request_before = p.read_bytes(request_path, 'input_bytes')
        sys.settrace(observer)
        try:
            req, raw, rows, checked = p.request(source_path, request_path)
            bounds = p.input_bounds(req, raw, rows, request_path)
        finally:
            sys.settrace(None)
        p.require(raw_before == raw and p.read_bytes(source_path, 'input_bytes') == raw and
                  p.read_bytes(request_path, 'input_bytes') == request_before,
                  'unchanged bytes before and after fixed check')
        independent = [p.parse(line) for line in raw_before.splitlines()]
        walk(independent)
        expected = []
        for i, row in enumerate(independent[1:]):
            tick('independent_source_records')
            for j in row['refs']:
                tick('independent_source_references')
                expected.append(dict(record=i, reference=j, original_charge=0))
        p.require(len(rows) == 212 and checked['accepted'] is True, 'fixed complete literal source')
        p.require(selections == expected and len(selections) > 0,
                  'every real source reference selected in source order, with no original charge')
        p.require(sum(line_charges.values()) == 0, 'no charge at any event on selection line')
        old_raw = p.read_bytes(HERE/'output-502/preflight.json', 'certificate_bytes')
        old = json.loads(old_raw, object_pairs_hook=p.no_duplicates, parse_constant=p.reject_number)
        walk(old)
        p.require(dict(r.source_observer) == old['source_observer'],
                  'unchanged observer counters reproduce primary source-phase receipt')
        report.update(status='OBSERVER_INCOMPLETE', fixed_source=checked,
            source_bounds=bounds, source_bytes=len(raw), request_bytes=len(request_before),
            complete_reference_selections=selections, omitted_reference_visits=len(selections),
            comprehension_event_counts=dict(operations), comprehension_original_charges=dict(line_charges),
            original_source_observer=dict(r.source_observer), original_source_visits=r.visits,
            original_source_counters_match=True,
            original_total_reported_visits=75_385_009,
            reported_total_plus_this_witness=75_385_009+len(selections),
            corrected_complete_total='UNKNOWN', transport_and_equalities='NOT_AUDITED',
            conclusion='At least these distinct source-reference selections are absent from the original item ledger; no cap overflow is established.')
    except Exception as err:
        report.update(status='AUDIT_UNFINISHED', error=dict(type=type(err).__name__, message=str(err)),
                      partial_reference_selections=selections)
    finally:
        sys.settrace(None)
    report.update(runtime=sys.version, elapsed_seconds=time.monotonic()-start,
        audit_budget=dict(budget), audit_event_item_upper=sum(budget.values()),
        audit_budget_scope='Trace events plus independent JSON/item walks and explicit source/reference iterations; not total Python work.',
        extra_work='Bounded raw UTF-8/JSON scans, source disassembly/AST, equality comparisons and receipt encoding; no graph construction or word/coordinate evaluation.',
        receipt_policy='one sized exclusive write; no payload/temp files or replacement',
        failures=[] if report['status']=='OBSERVER_INCOMPLETE' else [report.get('error')])
    raw = json.dumps(report, ensure_ascii=True, separators=(',', ':')).encode()
    program_bytes = Path(__file__).stat().st_size
    p.require(len(raw)+program_bytes < RESERVE, 'new program and full receipt fit reserve')
    p.require(time.monotonic()-start < SECONDS, 'bounded targeted audit time')
    output = OUT/'source-observer-audit.json'
    with output.open('xb') as stream:
        stream.write(raw)
    print(json.dumps(dict(status=report['status'], omitted_reference_visits=report.get('omitted_reference_visits'),
        audit_event_item_upper=sum(budget.values()), required_item_limit=LIMIT,
        artifact_bytes=len(raw)+program_bytes, required_reserve_bytes=RESERVE,
        failures=report['failures'], path=str(output))))


if __name__ == '__main__':
    main()
