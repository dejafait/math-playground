"""Reconstruct all step-512 formula operand records directly from source rows."""
import ast
from collections import Counter
import hashlib
import json
from pathlib import Path
import time

import parameterized_input as p

HERE = Path(__file__).resolve().parent
OUT = HERE/'output-512-repaired'


def main():
    dest = OUT/'receipt-check.json'
    p.require(not dest.exists(), 'fresh reconciliation')
    start = time.monotonic()
    data = json.loads((OUT/'source-equalities.json').read_bytes())
    (OUT/'receipt-check-program.py').write_bytes(Path(__file__).read_bytes())
    units, budget, failures = 0, Counter(), []
    prior, prior_seconds = data['audit_item_event_units'], data['cumulative_elapsed_seconds']

    def tick(kind, n=1):
        nonlocal units
        p.require(prior+units+n <= 100_000_000, 'cumulative unit limit')
        units += n
        budget[kind] += n
        if units % 4096 == 0:
            p.require(prior_seconds+time.monotonic()-start <= 900, 'cumulative timer')

    def same(a, b):
        tick('complete_receipt_value_nodes')
        if type(a) is not type(b):
            return False
        if type(a) is dict:
            return a.keys() == b.keys() and all(same(a[k], b[k]) for k in a)
        if type(a) is list:
            return len(a) == len(b) and all(same(x, y) for x, y in zip(a, b))
        return a == b

    def vol(x):
        tick('operand_nodes')
        p.require(type(x) in (str, list), 'full formula serialization domain')
        return 1 if type(x) is str else 1+sum(vol(y) for y in x)

    try:
        p.require(data['status'] == 'NARROW_FORMULA_COMPARISONS_RECEIVED' and not data['failures'], 'successful probe')
        raw = (HERE/'output-489/inputs/proof.jsonl').read_bytes()
        req_raw = (HERE/'output-489/inputs/request.json').read_bytes()
        tick('source_input_bytes', len(raw)+len(req_raw))
        req = ast.literal_eval(req_raw.decode('ascii'))
        header, *rows = [ast.literal_eval(s.decode('ascii')) for s in raw.splitlines(keepends=True)]
        fs = [z['f'] for z in rows]
        # Lists here are the receipt encoding of the already type-checked
        # tuple/string operands. Construct each primitive directly, without
        # evaluating the probe's expression ASTs or using checker functions.
        expected = [(None, 73, "tree(h['goal']) != expected", header['goal'], req['goal'], False)]
        rule_counts = Counter()
        for i, z in enumerate(rows):
            tick('source_records')
            f, rule, refs = z['f'], z['rule'], z['refs']
            ps = [fs[j] for j in refs]
            rule_counts[rule] += 1
            if rule == 'axiom':
                p.require(f[0] == 'or', 'axiom shape')
                pairs = [(92, "f[1] == ('not', f[2])", f[1], ['not', f[2]])]
            elif rule == 'expansion':
                p.require(f[0] == 'or', 'expansion shape')
                pairs = [(98, 'f[2] == p[0]', f[2], ps[0])]
            elif rule == 'contraction':
                pairs = [(100, "p[0] == ('or', f, f)", ps[0], ['or', f, f])]
            elif rule == 'association':
                q = ps[0]
                p.require(q[0] == q[2][0] == 'or', 'association shape')
                pairs = [(105, "f == ('or', ('or', q[1], q[2][1]), q[2][2])", f, ['or', ['or', q[1], q[2][1]], q[2][2]])]
            elif rule == 'cut':
                a, b = ps
                p.require(a[0] == b[0] == 'or', 'cut shapes')
                pairs = [(110, "b[1] == ('not', a[1])", b[1], ['not', a[1]]),
                         (110, "f == ('or', a[2], b[2])", f, ['or', a[2], b[2]])]
            else:
                raise AssertionError('unexpected actual rule')
            for line, expression, left, right in pairs:
                p.require(same(left, right), 'full independent literal inference')
                expected.append((i, line, expression, left, right, True))
        expected.append((None, 118, 'fs[-1] != expected', fs[-1], req['goal'], False))
        p.require(len(expected) == len(data['comparisons']) == 291, 'all actual comparisons')
        groups = {}
        for j, (actual, want) in enumerate(zip(data['comparisons'], expected)):
            tick('comparison_records')
            i, line, expression, left, right, result = want
            n = vol(left)
            delivery = 'POP_JUMP_IF_FALSE successor' if line in (73, 118) or expression.startswith('b[1]') else 'STORE_FAST ok'
            p.require(actual['index'] == j and actual['record'] == i and actual['line'] == line
                      and actual['expression'] == expression and same(actual['left'], left) and same(actual['right'], right)
                      and actual['expected_result'] is result and actual['actual_result'] is result
                      and actual['received'] is True and actual['direct_original_charge'] == 0
                      and actual['delivery'] == delivery and same(left, right)
                      and actual['left_nodes'] == actual['right_nodes'] == actual['reference_comparator_nodes'] == n,
                      'complete comparison record '+str(j))
            g = groups.setdefault(str(line), dict(calls=0, left_nodes=0, right_nodes=0, reference_comparator_nodes=0))
            g['calls'] += 1
            for key in ('left_nodes', 'right_nodes', 'reference_comparator_nodes'):
                g[key] += n
        p.require(same(groups, data['groups']), 'complete group reconciliation')
        p.require(same(data['primitive_outcomes'], [dict(record=i, rule=z['rule'], ok=True) for i, z in enumerate(rows)]), 'all primitive outcomes')
        old = json.loads((HERE/'output-502/preflight.json').read_bytes())
        p.require(same(data['original_source_observer'], old['source_observer']) and data['original_source_visits'] == 167322
                  and same(data['original_selected_opcode_charges'], {k: 0 for k in groups}), 'complete observer reconciliation')
        for name, path in [('preflight_job7_transport.py', HERE/'preflight_job7_transport.py'),
                           ('parameterized_input.py', Path(p.__file__)), ('literal-checker.py', HERE.parent/'parity-four-rule/checker.py')]:
            body = path.read_bytes()
            tick('source_snapshot_bytes', len(body))
            p.require(body == (OUT/name).read_bytes() == (HERE/'output-511-repaired'/name).read_bytes(), 'complete source snapshots')
        p.require(same(data['caps'], p.CAPS) and data['partial_augmented_source_items'] == 168943
                  and data['partial_augmented_original_three_run_items'] == 75868982
                  and data['logical_volumes_added_to_original_item_subtotal'] is False
                  and sum(data['audit_budget'].values()) == prior, 'caps and selected ledger')
        p.require(data['literal_check']['sha256'] == req['source_sha256'] == hashlib.sha256(raw).hexdigest()
                  and same(data['literal_check']['rule_counts'], dict(rule_counts)), 'caller and primitive count binding')
        total_nodes = sum(g['left_nodes'] for g in groups.values())
        p.require(total_nodes == data['audit_budget']['reference_comparator_nodes'] == 23631, 'logical node reconciliation')
    except Exception as err:
        failures.append(dict(type=type(err).__name__, message=str(err)))
    result = dict(status='PASS' if not failures else 'FAILED', failures=failures,
                  reconciled_comparisons=291 if not failures else 'INCOMPLETE',
                  reconciliation_selected_units=units, reconciliation_budget=dict(budget),
                  cumulative_selected_units=prior+units, required_selected_units=100_000_000,
                  cumulative_seconds=prior_seconds+time.monotonic()-start, required_seconds=900,
                  charged_evidence_bytes=0, required_reserve_bytes=1_000_000,
                  required_evidence_bytes=p.CAPS['certificate_bytes'], total_work_bound=False,
                  qualification='Full fixed finite operands/results and selected ledgers only; C/interpreter, I/O, hashing, tool reads, allocation and bit/index costs remain UNKNOWN.')
    fixed = data['program_snapshots_and_receipt_bytes']+2*Path(__file__).stat().st_size
    while True:
        body = json.dumps(result, separators=(',', ':')).encode()
        total = fixed+len(body)
        if result['charged_evidence_bytes'] == total:
            break
        result['charged_evidence_bytes'] = total
    p.require(total <= 1_000_000 and result['cumulative_seconds'] <= 900, 'cumulative reserve/time')
    with dest.open('xb') as stream:
        stream.write(body)
    print(json.dumps({k: v for k, v in result.items() if k not in ('qualification', 'reconciliation_budget')}, separators=(',', ':')))
    print(str(dest))


if __name__ == '__main__':
    main()
