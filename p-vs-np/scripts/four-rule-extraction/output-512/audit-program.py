"""Step 512: full finite formula-comparison reception, not a C-cost bound."""
import ast
from collections import Counter
import dis
import hashlib
import json
from pathlib import Path
import sys
import time
import traceback

import parameterized_input as p
import preflight_job7_transport as original

HERE = Path(__file__).resolve().parent
OUT = HERE/'output-512'
LIMIT, SECONDS, RESERVE = 100_000_000, 900, 1_000_000


def main():
    p.require(not OUT.exists(), 'fresh output required')
    OUT.mkdir()
    (OUT/'audit-program.py').write_bytes(Path(__file__).read_bytes())
    start = time.monotonic()
    units = 0
    budget = Counter()
    comparisons, outcomes, census = [], [], []
    charges = Counter()
    report = dict(status='IN_PROGRESS', failures=[], total_work_bound=False,
                  actual_c_comparison_cost='UNKNOWN', graph_regeneration=False,
                  coordinate_search=False, word_expansion=False)

    def tick(kind, n=1):
        nonlocal units
        p.require(units+n <= LIMIT, 'selected units before work')
        units += n
        budget[kind] += n
        if units % 4096 == 0:
            p.require(time.monotonic()-start <= SECONDS, 'periodic time cap')

    def same(a, b, kind='operand_binding_nodes'):
        # An explicit full structural comparator, without identity shortcuts.
        # Its calls are audit work, not the original C comparator's work.
        tick(kind)
        if type(a) is not type(b):
            return False
        if type(a) is dict:
            return a.keys() == b.keys() and all(same(a[k], b[k], kind) for k in a)
        if type(a) in (tuple, list):
            return len(a) == len(b) and all(same(x, y, kind) for x, y in zip(a, b))
        return a == b

    def norm(x):
        tick('independent_normalization_nodes')
        if type(x) is str:
            p.require(bool(x) and all(c.isalnum() or c == '_' for c in x), 'formula leaf')
            return x
        p.require(type(x) is list and x and ((len(x) == 2 and x[0] == 'not') or
                  (len(x) == 3 and x[0] == 'or')), 'formula syntax')
        return tuple([x[0]]+[norm(y) for y in x[1:]])

    def volume(x):
        tick('logical_operand_nodes')
        p.require(type(x) in (str, tuple), 'formula operand domain')
        return 1 if type(x) is str else 1+sum(volume(y) for y in x)

    def expr(node, env):
        tick('operand_expression_nodes')
        if isinstance(node, ast.Name):
            return env[node.id]
        if isinstance(node, ast.Constant):
            return node.value
        if isinstance(node, ast.Tuple):
            return tuple(expr(v, env) for v in node.elts)
        if isinstance(node, ast.Subscript):
            return expr(node.value, env)[expr(node.slice, env)]
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
            return -expr(node.operand, env)
        if isinstance(node, ast.Call):
            p.require(ast.unparse(node) == "tree(h['goal'])", 'only observed header-tree call')
            return env['header_tree']
        raise AssertionError('uncovered operand AST '+ast.dump(node))

    try:
        p.require(p.CAPS == original.EXPECTED_CAPS and sys.version_info[:3] == (3, 15, 0)
                  and sys.gettrace() is None, 'fixed caps/runtime/tracer')
        source, request = HERE/'output-489/inputs/proof.jsonl', HERE/'output-489/inputs/request.json'
        raw, req_raw = source.read_bytes(), request.read_bytes()
        tick('independent_input_bytes', len(raw)+len(req_raw))
        # Independently implemented parser on the finite safe-ASCII/no-escape
        # string and unsigned-integer domain established by step 511. Verify
        # that domain anew, and compare both complete parses on every input.
        def decode(body):
            text = body.decode('ascii')
            for c in text:
                tick('finite_lexical_characters')
                p.require(c != '\\' and (32 <= ord(c) <= 126 or c in '\t\r\n'), 'actual finite lexical domain')
            a = ast.literal_eval(text)
            b = json.loads(text, object_pairs_hook=unique)
            p.require(same(a, b, 'independent_parse_value_nodes'), 'complete independent parsed value')
            def domain(v):
                tick('finite_domain_nodes')
                if type(v) is str:
                    return
                if type(v) is int:
                    p.require(v >= 0, 'unsigned finite integers')
                    return
                p.require(type(v) in (dict, list), 'finite JSON domain')
                for w in (list(v.keys())+list(v.values()) if type(v) is dict else v):
                    domain(w)
            domain(a)
            return a

        def unique(pairs):
            result = {}
            for k, v in pairs:
                tick('independent_unique_pairs')
                p.require(k not in result, 'unique keys')
                result[k] = v
            return result

        req = decode(req_raw)
        header, *rows = [decode(line) for line in raw.splitlines(keepends=True)]
        fs = [norm(z['f']) for z in rows]
        goal, header_goal = norm(req['goal']), norm(header['goal'])
        p.require(len(rows) == 212 and hashlib.sha256(raw).hexdigest() == req['source_sha256'], 'original caller binding')
        paths = [HERE/'preflight_job7_transport.py', Path(p.__file__), HERE.parent/'parity-four-rule/checker.py']
        bodies = {}
        for path in paths:
            body = path.read_bytes()
            tick('source_snapshot_bytes', len(body))
            name = 'literal-checker.py' if path.name == 'checker.py' else path.name
            p.require(body == (HERE/'output-511-repaired'/name).read_bytes(), 'full unchanged prior source')
            (OUT/name).write_bytes(body)
            bodies[path] = body
        manifest = json.loads((HERE/'output-502/manifest.json').read_bytes())
        p.require(hashlib.sha256(bodies[paths[0]]).hexdigest() == manifest['script_sha256'], 'original program binding')
        tree = ast.parse(bodies[paths[2]])
        chosen = {73, 94, 96, 100, 105, 110, 118}
        selected = []
        for n in ast.walk(tree):
            tick('ast_nodes')
            if isinstance(n, ast.Compare) and (n.lineno in chosen or
                    (n.lineno in (92, 98) and n.col_offset == 63)):
                p.require(len(n.ops) == 1 and isinstance(n.ops[0], (ast.Eq, ast.NotEq)), 'single comparison')
                selected.append(n)
        p.require(len(selected) == 10, 'complete ten-site formula comparison census')
        nodes = {(n.lineno, n.end_lineno, n.col_offset, n.end_col_offset): n for n in selected}
        r = original.Run()
        original.R = r
        r.stage = 'formula equality audit only'
        instructions, matched, pending = {}, {}, None
        header_received, row_entries = None, []
        cf = str(paths[2])

        def oracle_env(i):
            if i < 0:
                return dict(expected=goal, header_tree=header_goal, fs=fs)
            z = rows[i]
            ps = [fs[j] for j in z['refs']]
            env = dict(f=fs[i], p=ps, expected=goal, fs=fs, header_tree=header_goal)
            if z['rule'] == 'association':
                env['q'] = ps[0]
            if z['rule'] == 'cut':
                env['a'], env['b'] = ps
            return env

        def finish(value, delivery):
            nonlocal pending
            entry = comparisons[pending['index']]
            p.require(type(value) is bool and value == entry['expected_result'], 'actual comparison Boolean delivery')
            entry.update(actual_result=value, delivery=delivery, received=True)
            pending = None

        def observe(frame, event, arg):
            nonlocal pending, header_received
            tick('trace_events')
            before = r.visits
            original.observe_source(frame, event, arg)
            delta = r.visits-before
            if frame.f_code.co_filename != cf:
                return observe
            name = frame.f_code.co_name
            if name == 'tree' and event == 'return' and frame.f_back.f_code.co_name == '_check_stream' and frame.f_back.f_lineno == 73:
                p.require(same(arg, header_goal), 'complete normalized header operand')
                header_received = arg
            if name != '_check_stream':
                return observe
            if event == 'call':
                p.require(same(frame.f_locals['expected'], goal), 'actual normalized caller goal')
                frame.f_trace_opcodes = True
                ins = list(dis.get_instructions(frame.f_code))
                instructions.update({v.offset: v for v in ins})
                for v in ins:
                    tick('disassembled_instructions')
                    pos = tuple(v.positions)
                    if v.opname == 'COMPARE_OP' and pos in nodes:
                        matched[v.offset] = nodes[pos]
                p.require(len(matched) == 10, 'all selected AST positions matched to opcodes')
                for offset, n in sorted(matched.items()):
                    census.append(dict(offset=offset, line=n.lineno, expression=ast.unparse(n)))
            if event == 'exception':
                raise AssertionError('unexpected checker exception')
            if event == 'line' and frame.f_lineno == 91:
                i = frame.f_locals['i']
                p.require(i == len(row_entries), 'complete primitive record order')
                env = oracle_env(i)
                p.require(same(frame.f_locals['f'], fs[i]) and same(frame.f_locals['p'], env['p'])
                          and frame.f_locals['tag'] == rows[i]['rule'] and same(frame.f_locals['refs'], rows[i]['refs']), 'full actual formula/reference operands')
                row_entries.append(i)
            if event == 'line' and frame.f_lineno == 111:
                i = frame.f_locals['i']
                p.require(frame.f_locals['ok'] is True and i == len(outcomes), 'complete successful primitive predicate')
                outcomes.append(dict(record=i, rule=rows[i]['rule'], ok=True))
            if event == 'opcode':
                ins = instructions[frame.f_lasti]
                if pending is not None:
                    if pending.get('store') is not None:
                        finish(frame.f_locals[pending['store']], 'STORE_FAST '+pending['store'])
                    elif pending.get('jump') is not None:
                        finish(ins.offset != pending['jump'], 'POP_JUMP_IF_FALSE successor')
                    elif ins.opname == 'STORE_FAST':
                        pending['store'] = ins.argval
                    elif ins.opname == 'POP_JUMP_IF_FALSE':
                        pending['jump'] = ins.argval
                    else:
                        p.require(ins.opname in ('COPY', 'TO_BOOL', 'EXTENDED_ARG'), 'only transparent comparison delivery instructions')
                if ins.offset in matched:
                    p.require(pending is None, 'previous comparison delivered')
                    n = matched[ins.offset]
                    i = -1 if n.lineno in (73, 118) else frame.f_locals['i']
                    env = dict(frame.f_locals, header_tree=header_received)
                    other = oracle_env(i)
                    left, right = expr(n.left, env), expr(n.comparators[0], env)
                    p.require(same(left, expr(n.left, other)) and same(right, expr(n.comparators[0], other)), 'complete independent comparison operands')
                    logical_before = budget['reference_comparator_nodes']
                    equality = same(left, right, 'reference_comparator_nodes')
                    result = equality if isinstance(n.ops[0], ast.Eq) else not equality
                    entry = dict(index=len(comparisons), record=None if i < 0 else i, line=n.lineno,
                                 expression=ast.unparse(n), offset=ins.offset, left=left, right=right,
                                 left_nodes=volume(left), right_nodes=volume(right), expected_result=result,
                                 reference_comparator_nodes=budget['reference_comparator_nodes']-logical_before,
                                 received=False, direct_original_charge=delta)
                    comparisons.append(entry)
                    pending = dict(index=entry['index'])
                    charges[str(n.lineno)] += delta
            return observe

        sys.settrace(observe)
        try:
            actual_req, actual_raw, actual_rows, checked = p.request(source, request)
            bounds = p.input_bounds(actual_req, actual_raw, actual_rows, request)
        finally:
            sys.settrace(None)
        p.require(pending is None and len(row_entries) == len(outcomes) == 212
                  and len(comparisons) == 291 and all(v['received'] for v in comparisons), 'all formula comparisons and outcomes received')
        p.require(same(actual_req, req) and same(actual_rows, rows) and actual_raw == raw, 'full returned input binding')
        old = json.loads((HERE/'output-502/preflight.json').read_bytes())
        p.require(same(dict(r.source_observer), old['source_observer']) and r.visits == 167_322, 'unchanged complete original observer')
        p.require(all(v == 0 for v in charges.values()), 'no direct selected opcode charges')
        for path, body in bodies.items():
            p.require(path.read_bytes() == body, 'program unchanged')
        p.require(source.read_bytes() == raw and request.read_bytes() == req_raw, 'inputs unchanged')
        groups = {}
        for c in comparisons:
            key = str(c['line'])
            g = groups.setdefault(key, dict(calls=0, left_nodes=0, right_nodes=0, reference_comparator_nodes=0))
            g['calls'] += 1
            for field in ('left_nodes', 'right_nodes', 'reference_comparator_nodes'):
                g[field] += c[field]
        report.update(status='NARROW_FORMULA_COMPARISONS_RECEIVED', caps=p.CAPS, runtime=sys.version,
                      census=census, groups=groups, comparisons=comparisons, primitive_outcomes=outcomes,
                      original_selected_opcode_charges=dict(charges), original_source_visits=r.visits,
                      original_source_observer=dict(r.source_observer), literal_check=checked, input_bounds=bounds,
                      partial_augmented_source_items=168_943, partial_augmented_original_three_run_items=75_868_982,
                      logical_volumes_added_to_original_item_subtotal=False,
                      remaining='Actual C comparison/container/hash/decoder/read/bit/index work, complete historical work, independent transport/schema/framing/live peaks and all coordinate/equality obligations remain unresolved.')
    except Exception as err:
        sys.settrace(None)
        report.update(status='FAILED', failures=[dict(type=type(err).__name__, message=str(err), traceback=traceback.format_exc())],
                      partial_comparisons=comparisons, partial_outcomes=outcomes, partial_census=census)
    report.update(audit_item_event_units=units, audit_budget=dict(budget), required_item_event_units=LIMIT,
                  elapsed_seconds=time.monotonic()-start, required_seconds=SECONDS,
                  required_evidence_bytes=p.CAPS['certificate_bytes'], reserve_bytes=RESERVE,
                  program_snapshots_and_receipt_bytes=0)
    fixed = Path(__file__).stat().st_size+sum(z.stat().st_size for z in OUT.iterdir() if z.is_file())
    while True:
        data = json.dumps(report, ensure_ascii=True, separators=(',', ':')).encode()
        total = fixed+len(data)
        if report['program_snapshots_and_receipt_bytes'] == total:
            break
        report['program_snapshots_and_receipt_bytes'] = total
    p.require(total <= RESERVE and time.monotonic()-start <= SECONDS, 'final evidence/time reserve')
    dest = OUT/'source-equalities.json'
    with dest.open('xb') as stream:
        stream.write(data)
    print(json.dumps(dict(status=report['status'], actual_units=units, required_units=LIMIT,
                          actual_evidence_bytes=total, required_reserve_bytes=RESERVE,
                          comparisons=len(comparisons), outcomes=len(outcomes), failures=report['failures'], path=str(dest))))


if __name__ == '__main__':
    main()
