"""Step 507: complete fixed-source generator-expression reconciliation.

Original production code and archives are read-only. No graph/word/row work.
"""
import ast
from collections import Counter
import dis
import json
from pathlib import Path
import sys
import time

import parameterized_input as p
import preflight_job7_transport as original

HERE = Path(__file__).resolve().parent
OUT = HERE / 'output-507'
LIMIT, SECONDS, RESERVE = 100_000_000, 900, 1_000_000


def main():
    p.require(not OUT.exists(), 'fresh output only')
    OUT.mkdir()
    start = time.monotonic()
    units = 0
    budget = Counter()
    report = dict(status='IN_PROGRESS', total_interpreter_bound=False,
                  graph_regeneration=False, word_expansion=False, coordinate_search=False)

    def tick(kind, n=1):
        nonlocal units
        p.require(units+n <= LIMIT, 'audit event/item ceiling before next work')
        units += n
        budget[kind] += n
        if units % 4096 == 0:
            p.require(time.monotonic()-start < SECONDS, 'audit timer')

    def eq(a, b):
        tick('complete_value_comparisons')
        if type(a) is not type(b):
            return False
        if type(a) is dict:
            return a.keys() == b.keys() and all(eq(a[k], b[k]) for k in a)
        if type(a) in (list, tuple):
            return len(a) == len(b) and all(eq(x, y) for x, y in zip(a, b))
        if type(a) is set:
            tick('set_comparison_items', len(a)+len(b))
        return a == b

    def walk(x):
        tick('independent_json_items')
        if type(x) is dict:
            for k, v in x.items():
                walk(k); walk(v)
        elif type(x) is list:
            for v in x:
                walk(v)

    try:
        p.require(p.CAPS == original.EXPECTED_CAPS, 'unchanged original CAPS')
        source, request = HERE/'output-489/inputs/proof.jsonl', HERE/'output-489/inputs/request.json'
        raw, req_raw = p.read_bytes(source, 'input_bytes'), p.read_bytes(request, 'input_bytes')
        # Independent complete input decode, not the original strict parser.
        req = json.loads(req_raw)
        rows = []
        for line in raw.splitlines():
            tick('independent_source_lines')
            rows.append(json.loads(line))
        walk(req); walk(rows)
        records = rows[1:]
        alphabet = req['alphabet']
        trees = [req['goal']] + [row['f'] for row in records]
        paths = [Path(p.__file__), HERE.parent/'parity-four-rule/checker.py']
        texts = {str(path): path.read_text() for path in paths}
        inventory = []
        for path, text in texts.items():
            module = ast.parse(text)
            funcs = [n for n in ast.walk(module) if isinstance(n, ast.FunctionDef)]
            for node in ast.walk(module):
                tick('ast_nodes')
                if isinstance(node, ast.GeneratorExp):
                    owners = [f for f in funcs if f.lineno <= node.lineno <= f.end_lineno]
                    owner = min(owners, key=lambda f: f.end_lineno-f.lineno)
                    inventory.append(dict(file=Path(path).name, function=owner.name,
                        line=node.lineno, column=node.col_offset, end_line=node.end_lineno,
                        end_column=node.end_col_offset, expression=ast.unparse(node)))
        inventory.sort(key=lambda x: (x['file'], x['line'], x['column']))
        p.require(len(inventory) == 19, 'full local generator inventory pin')
        sites = {(x['file'], x['line'], x['column']): x for x in inventory}
        expected = {key: [] for key in sites}

        def add(file, line, values, column=None):
            keys = [key for key in sites if key[0] == file and key[1] == line
                    and (column is None or key[2] == column)]
            p.require(len(keys) == 1, 'unique oracle site, including same-line sites')
            out = []
            for v in values:
                tick('independent_expected_yields')
                out.append(v)
            expected[keys[0]].append(out)
            tick('independent_expected_invocations')

        pf, cf = 'parameterized_input.py', 'checker.py'
        add(pf, 133, [c in '0123456789abcdef' for c in req['source_sha256']])
        for name in alphabet:
            add(pf, 141, [c.isalnum() or c == '_' for c in name])
        pairs = []
        for i, x in enumerate(alphabet):
            for y in alphabet[i+1:]:
                tick('independent_dictionary_pairs')
                pairs.append(('commutator', (x, y)))
        add(pf, 153, pairs)
        for entry in req['dictionary']['placeholders']:
            add(pf, 161, [type(x) is str for x in entry['originals']])
        for i, row in enumerate(records):
            add(pf, 184, [type(j) is int and 0 <= j < i for j in row['refs']])

        sizes = []
        # Independent explicit stacks reconstruct every extend invocation in
        # the LIFO traversal, without calling check_tree or size_depth.
        for t in trees:
            stack = [(t, 1)]
            count, depth = 0, 0
            while stack:
                tick('independent_stack_nodes')
                x, d = stack.pop()
                count += 1; depth = max(depth, d)
                if type(x) is list:
                    children = []
                    for child in x[1:]:
                        tick('independent_stack_links')
                        children.append((child, d+1))
                    add(pf, 115, children)
                    add(pf, 207, children)
                    stack.extend(children)
            sizes.append((count, depth))
        same_line = sorted(x['column'] for x in inventory if x['file'] == pf and x['line'] == 213)
        add(pf, 213, [x[1] for x in sizes], same_line[0])
        add(pf, 213, [x[0] for x in sizes], same_line[1])
        names = alphabet + [x['name'] for x in req['dictionary']['placeholders']]
        add(pf, 216, [len(x.encode()) for x in names])
        expected_actual = dict(source_bytes=len(raw), request_bytes=len(req_raw),
            tree_depth=max(x[1] for x in sizes), tree_nodes=sum(x[0] for x in sizes),
            source_lines=len(records), alphabet=len(alphabet),
            dictionary_entries=len(req['dictionary']['placeholders']),
            name_bytes=max(len(x.encode()) for x in names))
        expected_required = {k: p.CAPS['input_bytes'] if k in ('source_bytes', 'request_bytes')
                             else p.CAPS[k] for k in expected_actual}
        add(pf, 218, [expected_actual[k] <= expected_required[k] for k in expected_actual])

        def tree_character_oracle(t):
            stack = [t]
            while stack:
                tick('independent_checker_syntax_nodes')
                x = stack.pop()
                if type(x) is str:
                    add(cf, 18, [c.isalnum() or c == '_' for c in x])
                else:
                    for child in reversed(x[1:]):
                        tick('independent_checker_syntax_links')
                        stack.append(child)

        # Actual checker syntax order: expected, header names, header goal,
        # then each source formula. The literal checker is never called here.
        tree_character_oracle(req['goal'])
        for name in alphabet:
            tree_character_oracle(name)
        tree_character_oracle(rows[0]['goal'])
        add(cf, 69, [not isinstance(v, str) for v in alphabet])
        add(cf, 71, [v in ('true', 'false') for v in alphabet])
        for i, row in enumerate(records):
            tree_character_oracle(row['f'])
            add(cf, 84, [type(j) is not int or not 0 <= j < i for j in row['refs']])
            # Bottom-up attributes computed by explicit stack; then preorder
            # invocation order matches recursively entered generator frames.
            attrs, stack = {}, [(row['f'], False)]
            while stack:
                tick('independent_attribute_nodes')
                x, done = stack.pop()
                if type(x) is str:
                    attrs[id(x)] = (1, set() if x in ('true', 'false') else {x})
                elif not done:
                    stack.append((x, True))
                    for child in reversed(x[1:]):
                        tick('independent_attribute_links')
                        stack.append((child, False))
                else:
                    n, vs = 1, set()
                    for child in x[1:]:
                        tick('independent_attribute_reductions')
                        cn, cvs = attrs[id(child)]
                        n += cn; vs.update(cvs)
                    attrs[id(x)] = (n, vs)
            stack = [row['f']]
            while stack:
                tick('independent_checker_semantic_nodes')
                x = stack.pop()
                if type(x) is list:
                    add(cf, 31, [attrs[id(c)][1] for c in x[1:]])
                    add(cf, 35, [attrs[id(c)][0] for c in x[1:]])
                    for child in reversed(x[1:]):
                        tick('independent_checker_semantic_links')
                        stack.append(child)

        state, completed, counts, charges = {}, Counter(), Counter(), Counter()
        calls = set()
        code_sites, opnames = {}, {}
        r = original.Run(); original.R = r
        r.stage = 'fixed source generator subaudit'

        def key_for(code):
            if code not in code_sites:
                pos = next(z for z in code.co_positions() if z[2] is not None)
                matches = [key for key, item in sites.items()
                    if key[0] == Path(code.co_filename).name and item['line'] == code.co_firstlineno
                    and item['column'] <= pos[2] < item['end_column']]
                p.require(len(matches) == 1, 'unique runtime code/AST site')
                code_sites[code] = matches[0]
                opnames[code] = {i.offset: i.opname for i in dis.get_instructions(code)}
            return code_sites[code]

        def observer(frame, event, arg):
            tick('trace_events')
            before = r.visits
            original.observe_source(frame, event, arg)
            if frame.f_code.co_filename in texts:
                if event == 'call':
                    calls.add((Path(frame.f_code.co_filename).name, frame.f_code.co_name))
                if frame.f_code.co_name == '<genexpr>':
                    key = key_for(frame.f_code)
                    ident = id(frame)
                    if event == 'call':
                        if ident not in state:
                            i = counts[(key, 'invocations')]
                            p.require(i < len(expected[key]), 'no unexpected generator invocation')
                            state[ident] = [key, i, 0]
                            counts[(key, 'invocations')] += 1
                        counts[(key, 'resumes')] += 1
                        charges[key] += r.visits-before
                        p.require(r.visits-before == 1, 'exactly one original charge per resume')
                    elif event == 'return':
                        p.require(ident in state, 'generator return has an entered frame')
                        skey, i, j = state[ident]
                        p.require(skey == key, 'live generator identity')
                        opcode = opnames[frame.f_code][frame.f_lasti]
                        if opcode == 'YIELD_VALUE':
                            p.require(j < len(expected[key][i]) and eq(arg, expected[key][i][j]),
                                      'complete next yielded value equals independent oracle')
                            state[ident][2] += 1
                            counts[(key, 'yields')] += 1
                        else:
                            p.require(opcode in ('RETURN_VALUE', 'RETURN_CONST') and arg is None,
                                      'normal generator exhaustion, no close/throw')
                            p.require(j == len(expected[key][i]), 'no missing yielded suffix')
                            counts[(key, 'exhaustions')] += 1
                            completed[key] += 1
                            del state[ident]
                    elif event == 'exception':
                        p.require(False, 'unexpected local generator exception')
            return observer

        sys.settrace(observer)
        try:
            actual_req, actual_raw, actual_records, checked = p.request(source, request)
            bounds = p.input_bounds(actual_req, actual_raw, actual_records, request)
        finally:
            sys.settrace(None)
        p.require(not state, 'no suspended or partially consumed local generator')
        entered_inventory = [x for x in inventory if (x['file'], x['function']) in calls]
        selected = [x for key, x in sites.items() if expected[key]]
        p.require(eq(entered_inventory, selected) and len(selected) == 17,
                  'all generator sites in every entered local function accounted for')
        table = []
        for key, item in sites.items():
            if not expected[key]:
                p.require(completed[key] == 0, 'unentered helper generator stays unentered')
                continue
            inv, yields = len(expected[key]), sum(len(seq) for seq in expected[key])
            p.require(completed[key] == inv == counts[(key, 'invocations')]
                      == counts[(key, 'exhaustions')], 'every oracle invocation fully exhausted')
            p.require(counts[(key, 'yields')] == yields and counts[(key, 'resumes')] == inv+yields
                      and charges[key] == inv+yields, 'complete yield/resume/charge reconciliation')
            table.append(item | dict(invocations=inv, yielded_items=yields,
                normal_exhaustions=inv, resumes=inv+yields, original_item_charges=charges[key],
                all_yielded_values_checked=True, missing_item_charges=0))
        old_raw = p.read_bytes(HERE/'output-502/preflight.json', 'certificate_bytes')
        old = json.loads(old_raw)
        walk(old)
        p.require(eq(dict(r.source_observer), old['source_observer']), 'entire original observer')
        p.require(sum(charges.values()) == r.source_observer['<genexpr>'] == 101_874,
                  'all original generator charges partitioned')
        p.require(eq(actual_req, req) and eq(actual_records, records) and actual_raw == raw,
                  'complete fixed input correspondence')
        p.require(eq(bounds, dict(actual=expected_actual, required=expected_required)),
                  'all independently reconstructed input metrics')
        p.require(checked['accepted'] and checked['records'] == 212 and
                  eq(checked, old['literal_check']), 'complete literal receipt')
        p.require(p.read_bytes(source, 'input_bytes') == raw and
                  p.read_bytes(request, 'input_bytes') == req_raw, 'unchanged input bytes after checking')
        report.update(status='SOURCE_GENERATOR_CLASS_RECONCILED', generator_table=table,
            full_local_generator_inventory=inventory,
            entered_local_functions=[list(x) for x in sorted(calls)],
            original_source_observer=dict(r.source_observer), original_source_visits=r.visits,
            generator_invocations=sum(x['invocations'] for x in table),
            generator_yielded_items=sum(x['yielded_items'] for x in table),
            generator_original_charges=sum(charges.values()), missing_generator_item_charges=0,
            prior_distinct_omitted_items=1615, partial_augmented_source_items=r.visits+1615,
            partial_augmented_original_three_run_items=75_385_009+1615,
            caps=p.CAPS, literal_check=checked, input_bounds=bounds,
            read_bytes=dict(source=len(raw), request=len(req_raw),
                            primary_receipt=len(old_raw), modules=sum(len(v.encode()) for v in texts.values())),
            failures=[], remaining='Implicit operations, all failed/supplement work, parse/read/bit/index costs, full transport/schema/byte/live peaks remain UNKNOWN. No equality, rank, cap overflow or complete ledger follows.')
    except Exception as err:
        sys.settrace(None)
        report.update(status='FAILED', failures=[dict(type=type(err).__name__, message=str(err))])
    report.update(audit_event_item_units=units, audit_budget=dict(budget),
                  required_event_item_units=LIMIT, elapsed_seconds=time.monotonic()-start,
                  required_seconds=SECONDS, reserve_bytes=RESERVE,
                  required_aggregate_evidence_bytes=p.CAPS['certificate_bytes'],
                  program_and_receipt_bytes=0)
    program_bytes = Path(__file__).stat().st_size
    while True:
        encoded = json.dumps(report, ensure_ascii=True, separators=(',', ':')).encode()
        total = program_bytes+len(encoded)
        if total == report['program_and_receipt_bytes']:
            break
        report['program_and_receipt_bytes'] = total
    p.require(total <= RESERVE and time.monotonic()-start <= SECONDS, 'complete evidence bounds')
    path = OUT/'source-generators.json'
    with path.open('xb') as stream:
        stream.write(encoded)
    print(json.dumps(dict(status=report['status'], actual_units=units, required_units=LIMIT,
        original_generator_charges=report.get('generator_original_charges', 'UNKNOWN'),
        missing_generator_charges=report.get('missing_generator_item_charges', 'UNKNOWN'),
        actual_evidence_bytes=total, required_reserve_bytes=RESERVE,
        failures=report['failures'], path=str(path))))


if __name__ == '__main__':
    main()
