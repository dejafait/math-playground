"""Step 506: reconcile the entered explicit source loops, not total work.

Archives and production code are read-only. No graph/word/coordinate work.
"""
import ast
from collections import Counter
import json
from pathlib import Path
import sys
import time

import parameterized_input as p
import preflight_job7_transport as original

HERE = Path(__file__).resolve().parent
OUT = HERE / 'output-506/reconciled'
LIMIT, SECONDS, RESERVE = 100_000_000, 900, 1_000_000
PRIOR_UNITS = 56_553 + 1_856_194  # Both preserved probes; neither is zero work.


def main():
    p.require(not OUT.exists(), 'fresh output only')
    OUT.mkdir()
    start = time.monotonic()
    budget = Counter()
    units = 0
    report = dict(status='IN_PROGRESS', required_item_units=LIMIT,
                  required_seconds=SECONDS, reserve_bytes=RESERVE,
                  total_work_bound=False, graph_regeneration=False,
                  word_expansion=False, coordinate_search=False)

    def tick(kind, n=1):
        nonlocal units
        p.require(PRIOR_UNITS+units+n <= LIMIT, 'cumulative audit event/item limit before next work')
        units += n
        budget[kind] += n
        if units % 4096 == 0:
            p.require(time.monotonic()-start < SECONDS, 'audit timer')

    def eq(a, b):
        tick('complete_comparison_items')
        if type(a) is not type(b):
            return False
        if type(a) is dict:
            if a.keys() != b.keys():
                return False
            return all(eq(a[k], b[k]) for k in a)
        if type(a) in (list, tuple):
            return len(a) == len(b) and all(eq(x, y) for x, y in zip(a, b))
        return a == b

    def walk(x):
        tick('independent_json_items')
        if type(x) is dict:
            for k, v in x.items():
                walk(k); walk(v)
        elif type(x) in (list, tuple):
            for v in x:
                walk(v)

    try:
        p.require(p.CAPS == original.EXPECTED_CAPS, 'all original caps unchanged')
        source = HERE / 'output-489/inputs/proof.jsonl'
        request = HERE / 'output-489/inputs/request.json'
        source_raw = p.read_bytes(source, 'input_bytes')
        request_raw = p.read_bytes(request, 'input_bytes')
        # Independent bottom-up object hook sequence for exactly the strict
        # request parse followed by all source-line parses. No p.parse here.
        expected_hooks, expected_parses = [], []

        def oracle_hook(pairs):
            out = {}
            for k, v in pairs:
                tick('independent_hook_pairs')
                p.require(k not in out, 'independent duplicate check')
                out[k] = v
            expected_hooks.append((list(pairs), out))
            return out

        for raw in [request_raw] + source_raw.splitlines():
            tick('independent_parse_selection')
            text = raw.decode('utf-8', errors='strict')
            value = json.loads(text, object_pairs_hook=oracle_hook,
                               parse_float=p.reject_number,
                               parse_constant=p.reject_number)
            walk(value)
            expected_parses.append((text, value))
        req = expected_parses[0][1]
        records = [value for _, value in expected_parses[2:]]
        expected_nodes = 0
        for t in [req['goal']] + [row['f'] for row in records]:
            stack = [t]
            while stack:
                tick('independent_tree_nodes')
                x = stack.pop()
                expected_nodes += 1
                if type(x) is list:
                    for child in x[1:]:
                        tick('independent_tree_links')
                        stack.append(child)

        paths = [Path(p.__file__), HERE.parent / 'parity-four-rule/checker.py']
        modules = {str(path): path.read_text() for path in paths}
        inventory = []
        for path, text in modules.items():
            module = ast.parse(text)
            funcs = [x for x in ast.walk(module)
                     if isinstance(x, (ast.FunctionDef, ast.AsyncFunctionDef))]
            for node in ast.walk(module):
                tick('ast_nodes')
                if isinstance(node, (ast.For, ast.While, ast.AsyncFor)):
                    owners = [f for f in funcs if f.lineno <= node.lineno <= f.end_lineno]
                    owner = min(owners, key=lambda f: f.end_lineno-f.lineno) if owners else None
                    inventory.append(dict(file=Path(path).name,
                        function=owner.name if owner else '<module>', line=node.lineno,
                        body_line=node.body[0].lineno, kind=type(node).__name__,
                        header=ast.unparse(node.target)+' in '+ast.unparse(node.iter)
                            if isinstance(node, (ast.For, ast.AsyncFor)) else ast.unparse(node.test)))

        # Exact pins also detect source/line drift before interpreting a trace.
        pins = [
            ('parameterized_input.py', 'no_duplicates', '(k, v) in pairs'),
            ('parameterized_input.py', 'parse', 'c in raw'),
            ('parameterized_input.py', 'check_tree', 'stack'),
            ('parameterized_input.py', 'request', 'x in alphabet'),
            ('parameterized_input.py', 'request', 'p in ps'),
            ('parameterized_input.py', 'request', '(i, r) in enumerate(records)'),
            ('parameterized_input.py', 'size_depth', 'stack'),
            ('checker.py', '_check_stream', '(i, raw) in enumerate(stream)')]
        selected = [x for x in inventory if (x['file'], x['function'], x['header']) in pins]
        p.require(len(selected) == len(pins), 'unique exact explicit-loop pins')
        index = {(x['file'], x['function'], x['body_line']): x for x in selected}
        p.require(len(index) == len(selected), 'distinct loop-body event sites')
        counts, charges, calls = Counter(), Counter(), set()
        parse_evidence, hook_evidence = [], []
        r = original.Run()
        r.stage = 'fixed source phase only'
        original.R = r

        def observer(frame, event, arg):
            tick('trace_events')
            before = r.visits
            original.observe_source(frame, event, arg)
            delta = r.visits-before
            filename = frame.f_code.co_filename
            if filename in modules:
                file, name, line = Path(filename).name, frame.f_code.co_name, frame.f_lineno
                if event == 'call':
                    calls.add((file, name))
                if event == 'line':
                    key = (file, name, line)
                    if key in index:
                        counts[key] += 1
                        charges[key] += delta
                if event == 'return' and file == 'parameterized_input.py':
                    if name == 'parse':
                        i = len(parse_evidence)
                        p.require(i < len(expected_parses), 'no extra strict parse')
                        text, value = expected_parses[i]
                        p.require(eq(frame.f_locals['raw'], text) and eq(arg, value),
                                  'every complete strict parse input and output')
                        parse_evidence.append(dict(index=i, characters=len(text),
                                                   utf8_bytes=len(text.encode('utf-8'))))
                    elif name == 'no_duplicates':
                        i = len(hook_evidence)
                        p.require(i < len(expected_hooks), 'no extra duplicate hook')
                        pairs, out = expected_hooks[i]
                        p.require(eq(frame.f_locals['pairs'], pairs) and eq(arg, out),
                                  'every complete ordered pair list and duplicate-hook output')
                        hook_evidence.append(dict(index=i, pairs=len(pairs), keys=list(out)))
            return observer

        sys.settrace(observer)
        try:
            actual_req, actual_raw, actual_rows, checked = p.request(source, request)
            bounds = p.input_bounds(actual_req, actual_raw, actual_rows, request)
        finally:
            sys.settrace(None)
        p.require(len(parse_evidence) == len(expected_parses), 'all complete strict parses')
        p.require(len(hook_evidence) == len(expected_hooks), 'all complete duplicate hooks')
        p.require(eq(actual_req, req) and eq(actual_rows, records) and actual_raw == source_raw,
                  'complete source-phase input correspondence')
        p.require(p.read_bytes(source, 'input_bytes') == source_raw and
                  p.read_bytes(request, 'input_bytes') == request_raw, 'unchanged input bytes')
        entered_loops = [x for x in inventory if (x['file'], x['function']) in calls]
        p.require(eq(entered_loops, selected), 'all explicit loops in all entered local functions')
        expected = [sum(len(text) for text, _ in expected_parses),
                    sum(len(pairs) for pairs, _ in expected_hooks)]
        table = []
        for item in selected:
            key = (item['file'], item['function'], item['body_line'])
            file, name, header = item['file'], item['function'], item['header']
            n = (expected[0] if name == 'parse' else expected[1] if name == 'no_duplicates'
                 else expected_nodes if name in ('check_tree', 'size_depth')
                 else len(req['alphabet']) if header == 'x in alphabet'
                 else len(req['dictionary']['placeholders']) if header == 'p in ps'
                 else len(records))
            p.require(counts[key] == n, 'every explicit loop count agrees with independent inputs')
            charged = name not in ('parse', 'no_duplicates')
            p.require(charges[key] == (n if charged else 0), 'exact original charges on each loop')
            table.append(item | dict(body_entries=n, original_charges=charges[key],
                accounting_class='separate_character_scan' if name == 'parse' else 'item_visit',
                omitted_item_visits=n if name == 'no_duplicates' else 0))
        old_raw = p.read_bytes(HERE/'output-502/preflight.json', 'certificate_bytes')
        old = json.loads(old_raw, object_pairs_hook=p.no_duplicates, parse_constant=p.reject_number)
        walk(old)
        p.require(eq(dict(r.source_observer), old['source_observer']), 'entire original source observer')
        p.require('JSON character scans/UTF-8/I/O' in old['accounting'],
                  'original metric explicitly separates character scans')
        p.require(checked['accepted'] and checked['records'] == len(records) == 212,
                  'complete unchanged literal acceptance')
        omitted = sum(x['omitted_item_visits'] for x in table)
        report.update(status='EXPLICIT_LOCAL_LOOP_CLASS_RECONCILED', caps=p.CAPS,
            loop_table=table, full_local_explicit_loop_inventory=inventory,
            entered_local_functions=[list(x) for x in sorted(calls)],
            all_strict_parse_checks=parse_evidence, all_duplicate_hook_checks=hook_evidence,
            original_source_observer=dict(r.source_observer), original_source_visits=r.visits,
            new_omitted_item_visits=omitted, prior_distinct_inline_omissions=885,
            separate_strict_parser_character_scans=expected[0],
            original_accounting_qualification=old['accounting'],
            partial_augmented_source_visits=r.visits+885+omitted,
            partial_augmented_three_run_visits=75_385_009+885+omitted,
            literal_check=checked, input_bounds=bounds,
            independent_source_nodes=expected_nodes,
            input_read_bytes=dict(source=len(source_raw), request=len(request_raw)),
            scanned_local_module_bytes=sum(len(s.encode()) for s in modules.values()),
            inspected_primary_receipt_bytes=len(old_raw),
            failures=[], remaining='Generators and implicit operations, failed/supplement work, transport/schema/byte/live peaks, bit/index and total interpreter work are NOT reconciled.')
    except Exception as err:
        sys.settrace(None)
        report.update(status='FAILED', failures=[dict(type=type(err).__name__, message=str(err))])
    prior_files = [z for z in OUT.parent.rglob('*') if z.is_file()]
    prior_bytes = sum(z.stat().st_size for z in prior_files)
    report.update(audit_event_item_units=units, audit_budget=dict(budget),
                  prior_failed_audit_units=PRIOR_UNITS, cumulative_audit_units=PRIOR_UNITS+units,
                  preserved_prior_failure_bytes=prior_bytes,
                  prior_probe_artifacts=[dict(path=str(z.relative_to(HERE)), bytes=z.stat().st_size)
                                         for z in sorted(prior_files)],
                  elapsed_seconds=time.monotonic()-start, program_and_receipt_bytes=0)
    program_bytes = Path(__file__).stat().st_size
    while True:
        raw = json.dumps(report, ensure_ascii=True, separators=(',', ':')).encode()
        total = prior_bytes+program_bytes+len(raw)
        if report['program_and_receipt_bytes'] == total:
            break
        report['program_and_receipt_bytes'] = total
    p.require(total <= RESERVE and PRIOR_UNITS+units <= LIMIT and time.monotonic()-start <= SECONDS,
              'complete bounded audit evidence')
    path = OUT/'explicit-source-loops.json'
    with path.open('xb') as stream:
        stream.write(raw)
    print(json.dumps(dict(status=report['status'], units=units, required_units=LIMIT,
        new_omitted_item_visits=report.get('new_omitted_item_visits', 'UNKNOWN'),
        evidence_bytes=total, required_evidence_bytes=RESERVE, failures=report['failures'],
        path=str(path))))


if __name__ == '__main__':
    main()
