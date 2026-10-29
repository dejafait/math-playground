"""Step 513: complete scalar-helper delivery census, not an internal-cost bound."""
import ast
from collections import Counter
import hashlib
import json
from pathlib import Path
import sys
import time
import traceback

import parameterized_input as p
import preflight_job7_transport as original

HERE = Path(__file__).resolve().parent
OUT = HERE/'output-513'
LIMIT, SECONDS, RESERVE = 100_000_000, 900, 1_000_000
HELPERS = ('require', 'bound', 'name', 'integer')


def main():
    p.require(not OUT.exists(), 'fresh output required')
    OUT.mkdir()
    (OUT/'audit-program.py').write_bytes(Path(__file__).read_bytes())
    start = time.monotonic()
    units, budget = 0, Counter()
    report = dict(status='IN_PROGRESS', failures=[], total_work_bound=False,
                  actual_internal_cost='UNKNOWN', graph_regeneration=False,
                  coordinate_search=False, word_expansion=False)
    calls, returns, charges, sites = Counter(), Counter(), Counter(), Counter()
    expected_bounds, expected_names, expected_integers = [], [], []
    positions = Counter()
    active, bound_groups, name_groups, observed_integers = {}, {}, Counter(), []

    def tick(kind, n=1):
        nonlocal units
        p.require(units+n <= LIMIT, 'selected units before work')
        units += n
        budget[kind] += n
        if units % 4096 == 0:
            p.require(time.monotonic()-start <= SECONDS, 'periodic time cap')

    def same(a, b):
        tick('full_value_nodes')
        if type(a) is not type(b):
            return False
        if type(a) is dict:
            return a.keys() == b.keys() and all(same(a[k], b[k]) for k in a)
        if type(a) in (list, tuple):
            return len(a) == len(b) and all(same(x, y) for x, y in zip(a, b))
        return a == b

    def add_bound(actual, key, stage):
        tick('independent_bound_arguments')
        p.require(type(actual) is int and 0 <= actual <= p.CAPS[key], 'independent bound')
        expected_bounds.append((actual, key, stage))

    def read_plan(path, body):
        # No new read is performed by this oracle; lengths are bound to the
        # complete immutable bytes independently loaded before observation.
        add_bound(len(body), 'input_bytes', 'file size before read: '+str(path))
        add_bound(len(body), 'input_bytes', 'bounded read: '+str(path))

    def parse_plan(body):
        # Actual inputs have safe ASCII with no escapes, as rechecked here.
        # Track only nesting outside string literals, independently of p.parse.
        text, depth, quoted = body.decode('ascii'), 0, False
        for c in text:
            tick('independent_lexical_characters')
            p.require(c != '\\' and (32 <= ord(c) <= 126 or c in '\t\r\n'), 'finite lexical domain')
            if c == '"':
                quoted = not quoted
            elif not quoted and c in '[{':
                depth += 1
                add_bound(depth, 'json_depth', 'JSON nesting before parse')
            elif not quoted and c in ']}':
                depth -= 1
                p.require(depth >= 0, 'independent nonnegative nesting')
        p.require(depth == 0 and not quoted, 'complete independent nesting')

    def name_plan(value):
        tick('independent_name_arguments')
        p.require(type(value) is str and bool(value), 'independent nonempty name')
        expected_names.append(value)
        add_bound(len(value.encode('utf-8')), 'name_bytes', 'name bytes')

    def tree_plan(tree):
        # Recursive reverse-child order reproduces the specified LIFO visit
        # order, without calling or copying p.check_tree's iterative code.
        count = 0

        def visit(value, depth):
            nonlocal count
            tick('independent_formula_nodes')
            count += 1
            add_bound(depth, 'tree_depth', 'formula tree depth')
            add_bound(count, 'tree_nodes', 'formula nodes')
            if type(value) is str:
                name_plan(value)
                p.require(value in alphabet or value in ('true', 'false'), 'independent formula name')
            else:
                p.require(type(value) is list and ((len(value) == 2 and value[0] == 'not') or
                          (len(value) == 3 and value[0] == 'or')), 'independent formula syntax')
                for child in reversed(value[1:]):
                    visit(child, depth+1)

        visit(tree, 1)
        return count

    try:
        p.require(p.CAPS == original.EXPECTED_CAPS and sys.version_info[:3] == (3, 15, 0)
                  and sys.gettrace() is None, 'fixed caps/runtime/tracer')
        source, request = HERE/'output-489/inputs/proof.jsonl', HERE/'output-489/inputs/request.json'
        raw, req_raw = source.read_bytes(), request.read_bytes()
        tick('input_bytes', len(raw)+len(req_raw))

        def unique(pairs):
            result = {}
            for key, value in pairs:
                tick('independent_object_pairs')
                p.require(key not in result, 'independent unique keys')
                result[key] = value
            return result

        # Decoding here is an existing source interface, not a new claim about
        # the JSON implementation. Entire values also equal ast.literal_eval.
        def decode(body):
            value = json.loads(body, object_pairs_hook=unique)
            p.require(same(value, ast.literal_eval(body.decode('ascii'))), 'independent full finite parse')
            return value

        req = decode(req_raw)
        lines = raw.splitlines()
        header, *rows = [decode(line) for line in lines]
        alphabet = req['alphabet']
        p.require(len(rows) == 212 and hashlib.sha256(raw).hexdigest() == req['source_sha256'], 'original binding')
        bodies = {}
        paths = [HERE/'preflight_job7_transport.py', Path(p.__file__), HERE.parent/'parity-four-rule/checker.py']
        for path in paths:
            body = path.read_bytes()
            tick('source_snapshot_bytes', len(body))
            name = 'literal-checker.py' if path.name == 'checker.py' else path.name
            p.require(body == (HERE/'output-512-repaired'/name).read_bytes(), 'full unchanged prior source')
            (OUT/name).write_bytes(body)
            bodies[path] = body
        manifest = json.loads((HERE/'output-502/manifest.json').read_bytes())
        p.require(hashlib.sha256(bodies[paths[0]]).hexdigest() == manifest['script_sha256'], 'original program manifest')

        read_plan(request, req_raw)
        parse_plan(req_raw)
        add_bound(len(alphabet), 'alphabet', 'alphabet length')
        for value in alphabet:
            name_plan(value)
        nodes = tree_plan(req['goal'])
        add_bound(len(alphabet)*(len(alphabet)+1)//2, 'dictionary_entries', 'dictionary cardinality before pair allocation')
        for placeholder in req['dictionary']['placeholders']:
            name_plan(placeholder['name'])
        read_plan(source, raw)
        for line in lines:
            parse_plan(line)
        for i, row in enumerate(rows):
            for j in row['refs']:
                tick('independent_reference_integers')
                p.require(type(j) is int and 0 <= j < i, 'independent backward reference')
                expected_integers.append(j)
            nodes += tree_plan(row['f'])
            add_bound(nodes, 'tree_nodes', 'aggregate source/request nodes')
        read_plan(source, raw)

        module = ast.parse(bodies[paths[1]])
        census = []
        for node in ast.walk(module):
            tick('ast_nodes')
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in HELPERS:
                census.append(dict(helper=node.func.id, line=node.lineno, end_line=node.end_lineno,
                                   expression=ast.unparse(node)))
        r = original.Run()
        original.R = r
        r.stage = 'scalar helper audit only'

        def observe(frame, event, arg):
            tick('trace_events')
            before = r.visits
            original.observe_source(frame, event, arg)
            delta = r.visits-before
            helper = frame.f_code.co_name
            if frame.f_code.co_filename != p.__file__ or helper not in HELPERS:
                return observe
            charges[helper+':'+event] += delta
            if event == 'exception':
                raise AssertionError('unexpected scalar-helper exception')
            if event == 'call':
                caller = frame.f_back
                p.require(caller.f_code.co_filename == p.__file__, 'actual helper caller source')
                matching = [site for site in census if site['helper'] == helper and
                            site['line'] <= caller.f_lineno <= site['end_line']]
                p.require(len(matching) == 1, 'unique static helper call site')
                site = matching[0]
                key = helper+' <- '+caller.f_code.co_name+':'+str(site['line'])
                sites[key] += 1
                calls[helper] += 1
                p.require(id(frame) not in active, 'fresh helper frame')
                active[id(frame)] = helper
                values = frame.f_locals
                if helper == 'require':
                    p.require(type(values['ok']) is bool and values['ok'] is True, 'actual complete successful condition')
                    if caller.f_code.co_name == 'bound':
                        c = caller.f_locals
                        p.require(same(values['message'], dict(stage=c['stage'], actual=c['actual'],
                                  required=p.CAPS[c['key']], resource=c['key'])), 'full bound failure payload')
                else:
                    expected = {'bound': expected_bounds, 'name': expected_names, 'integer': expected_integers}[helper]
                    index = positions[helper]
                    actual = ((values['actual'], values['key'], values['stage']) if helper == 'bound' else values['x'])
                    p.require(index < len(expected) and same(actual, expected[index]), 'entire ordered helper argument')
                    positions[helper] += 1
                    if helper == 'bound':
                        actual, resource, stage = actual
                        g = bound_groups.setdefault(resource+' | '+stage, dict(calls=0, minimum=actual, maximum=actual, required=p.CAPS[resource]))
                        g['calls'] += 1
                        g['minimum'], g['maximum'] = min(g['minimum'], actual), max(g['maximum'], actual)
                    elif helper == 'name':
                        name_groups[actual] += 1
                    else:
                        observed_integers.append(actual)
            elif event == 'return':
                p.require(active.pop(id(frame), None) == helper, 'matched helper return')
                p.require(arg is (True if helper == 'integer' else None), 'actual helper return value')
                returns[helper] += 1
            return observe

        sys.settrace(observe)
        try:
            actual_req, actual_raw, actual_rows, checked = p.request(source, request)
            bounds = p.input_bounds(actual_req, actual_raw, actual_rows, request)
        finally:
            sys.settrace(None)
        p.require(not active and calls == returns, 'all calls returned normally')
        p.require(positions['bound'] == len(expected_bounds) and positions['name'] == len(expected_names)
                  and positions['integer'] == len(expected_integers), 'every independent argument consumed')
        p.require(same(actual_req, req) and same(actual_rows, rows) and actual_raw == raw, 'complete returned inputs')
        old = json.loads((HERE/'output-502/preflight.json').read_bytes())
        p.require(same(dict(r.source_observer), old['source_observer']) and r.visits == 167_322, 'unchanged complete observer')
        p.require(all(value == 0 for value in charges.values()), 'zero selected helper-event direct charges')
        for path, body in bodies.items():
            p.require(path.read_bytes() == body, 'unchanged complete program bytes')
        p.require(source.read_bytes() == raw and request.read_bytes() == req_raw, 'unchanged immutable input bytes')
        report.update(status='SCALAR_HELPER_DELIVERIES_RECEIVED', caps=p.CAPS, runtime=sys.version,
                      static_call_sites=census, actual_call_sites=dict(sites), calls=dict(calls), returns=dict(returns),
                      direct_original_charges=dict(charges), argument_positions=dict(positions),
                      bound_groups=bound_groups, name_frequencies=dict(name_groups), integer_arguments=observed_integers,
                      original_source_visits=r.visits, original_source_observer=dict(r.source_observer),
                      literal_check=checked, input_bounds=bounds, independent_tree_nodes=nodes,
                      partial_augmented_source_items=168_943, partial_augmented_original_three_run_items=75_868_982,
                      dispatches_added_to_original_item_subtotal=False,
                      remaining='Actual C/container/read/hash/serialization/bit/index costs; historical failed/supplement work; independent transport/schema/byte/live peaks; all ranks/coordinates/equalities and unrestricted complexity gaps.')
    except Exception as error:
        sys.settrace(None)
        report.update(status='FAILED', failures=[dict(type=type(error).__name__, message=str(error), traceback=traceback.format_exc())],
                      partial_calls=dict(calls), partial_returns=dict(returns), partial_argument_positions=dict(positions),
                      partial_call_sites=dict(sites), pending_frames=len(active))
    report.update(audit_item_event_units=units, audit_budget=dict(budget), required_item_event_units=LIMIT,
                  elapsed_seconds=time.monotonic()-start, required_seconds=SECONDS,
                  required_evidence_bytes=p.CAPS['certificate_bytes'], reserve_bytes=RESERVE,
                  program_snapshots_and_receipt_bytes=0)
    fixed = Path(__file__).stat().st_size+sum(path.stat().st_size for path in OUT.iterdir() if path.is_file())
    while True:
        data = json.dumps(report, ensure_ascii=True, separators=(',', ':')).encode()
        total = fixed+len(data)
        if report['program_snapshots_and_receipt_bytes'] == total:
            break
        report['program_snapshots_and_receipt_bytes'] = total
    p.require(total <= RESERVE and time.monotonic()-start <= SECONDS, 'final evidence/time reserve')
    dest = OUT/'source-helpers.json'
    with dest.open('xb') as stream:
        stream.write(data)
    print(json.dumps(dict(status=report['status'], actual_units=units, required_units=LIMIT,
                          actual_evidence_bytes=total, required_reserve_bytes=RESERVE,
                          calls=dict(calls), failures=report['failures'], path=str(dest))))
    return 0 if report['status'] == 'SCALAR_HELPER_DELIVERIES_RECEIVED' else 1


if __name__ == '__main__':
    raise SystemExit(main())
