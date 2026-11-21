#!/usr/bin/env python3
"""Audit one essential component of fixed692, without a new construction.

Count a deliberately incomplete subset of source-level scalar operations.
This refutes component domination by12; it does not lower-bound total
necessary setup work or supply a complete alternative upper ledger.
"""
import ast
from collections import Counter
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path

HERE = Path(__file__).resolve()
SOURCE = HERE.with_name('certified-gauss-adaptive-692.py')
TRACE = SOURCE.with_suffix('.json')
REPLAY = HERE.with_name('certified-gauss-adaptive-replay-692.json')
LEDGER = HERE.with_name('certified-gauss-adaptive-ledger-692.json')
OUT = HERE.with_suffix('.json')
source = SOURCE.read_text()
tree = ast.parse(source)
data = json.loads(TRACE.read_text())
replay = json.loads(REPLAY.read_text())
ledger = json.loads(LEDGER.read_text())
checks, failures, conversions = Counter(), [], []


def ck(condition, name):
    checks[name] += 1
    if not condition:
        failures.append(name)
        raise AssertionError(name)


def zi(v):
    return int(v['odd_hex'], 16) << v['shift']


def rf(v):
    return F(zi(v['num']), zi(v['den']))


def count(node):
    """Named assignments, comparisons, ordinary arithmetic, granted halving.

    Remainder and all Boolean/call/control overhead receive ZERO cost.
    A floor division by2 receives only one arithmetic operation, as an
    intentionally generous relaxation on the verified exact-grid path.
    No common-subexpression elimination or source rewriting is applied.
    """
    result = Counter()
    for child in ast.walk(node):
        if isinstance(child, ast.BinOp):
            if isinstance(child.op, (ast.Add, ast.Sub, ast.Mult, ast.Div, ast.FloorDiv)):
                result['arithmetic'] += 1
            elif isinstance(child.op, ast.Mod):
                result['uncharged_remainders'] += 1
        elif isinstance(child, ast.Compare):
            result['comparisons'] += len(child.ops)
        elif isinstance(child, ast.Assign):
            for target in child.targets:
                result['assignments'] += sum(isinstance(v, ast.Name) for v in ast.walk(target))
        elif isinstance(child, ast.AugAssign):
            ck(isinstance(child.op, (ast.Add, ast.FloorDiv)), 'recognized augmented arithmetic')
            ck(isinstance(child.target, ast.Name), 'named augmented assignment')
            result['arithmetic'] += 1
            result['assignments'] += 1
    return result


fragments = []
try:
    ck(data['script_sha256'] == sha256(SOURCE.read_bytes()).hexdigest(), 'constructor source hash')
    ck(replay['source_certificate_sha256'] == sha256(TRACE.read_bytes()).hexdigest(), 'replay trace hash')
    ck(replay['script_sha256'] == sha256(HERE.with_name('certified-gauss-adaptive-replay-692.py').read_bytes()).hexdigest(), 'replay source hash')
    ck(ledger['source_sha256'] == sha256(TRACE.read_bytes()).hexdigest(), 'ledger trace hash')
    ck(ledger['script_sha256'] == sha256(HERE.with_name('certified-gauss-adaptive-ledger-692.py').read_bytes()).hexdigest(), 'ledger source hash')
    ck(replay['result'] == 'PASS_COMPLETE_RECORDED_TRACE' and not replay['failures'], 'saved full replay passed')
    ck(sum(replay['checks_by_name'].values()) == 176788, 'saved full replay check count')
    ck(all(v['pass'] for v in ledger['checks']) and len(ledger['checks']) == 9, 'all saved counter checks')
    fn = next(v for v in tree.body if isinstance(v, ast.FunctionDef) and v.name == 'quantize')
    loop = next(v for v in fn.body if isinstance(v, ast.While))
    ck(ast.unparse(loop.test) == 'h > target_width', 'conversion loop signature')
    # Select every successful-path statement except pay instrumentation;
    # a failure-context body is not executed on these successful traces.
    chosen = [('width test', loop.test)]
    for statement in loop.body:
        if isinstance(statement, ast.Expr) and isinstance(statement.value, ast.Call):
            call = statement.value
            if isinstance(call.func, ast.Name) and call.func.id == 'pay':
                ck(ast.unparse(call) == "pay('binary_conversion_halvings', 12)", 'scheduled charge is12')
                continue
            ck(isinstance(call.func, ast.Name) and call.func.id == 'require', 'recognized loop guard')
            chosen.append((call.args[1].value, call.args[0]))
        elif isinstance(statement, ast.If):
            if ast.unparse(statement.test) == 'depth >= BITS':
                chosen.append(('failure-context depth test', statement.test))
            else:
                ck(ast.unparse(statement.test) == 'mid <= center', 'recognized endpoint branch')
                ck(len(statement.body) == len(statement.orelse) == 1, 'single endpoint copy per branch')
                ck(count(statement.body[0]) == count(statement.orelse[0]), 'both branch costs equal')
                chosen.extend([('center comparison', statement.test), ('endpoint copy', statement.body[0])])
        else:
            ck(isinstance(statement, (ast.Assign, ast.AugAssign)), 'recognized successful-path statement')
            chosen.append((ast.unparse(statement), statement))
    subset = Counter()
    for name, node in chosen:
        costs = count(node)
        subset.update(costs)
        fragments.append({'name': name, 'line': node.lineno,
                          'source': ast.get_source_segment(source, node), 'counts': dict(costs)})
    rate = subset['arithmetic'] + subset['comparisons'] + subset['assignments']
    ck(dict(subset) == {'comparisons': 6, 'arithmetic': 6, 'assignments': 5, 'uncharged_remainders': 2}, 'complete selected-path operation inventory')
    ck(rate == 17 > 12, 'assigned component rate fails domination')
    D = 2**data['grid_bits']
    for row in data['rows']:
        for root in row['positive_roots']:
            # Each input depth is independently reconstructed from the
            # recorded prefix and previous conversions.
            depth = 14 + len(root['bisections'])
            for number, step in enumerate(root['newton']):
                oldlo, oldhi = map(zi, step['old_grid_interval'])
                jl, ju = map(rf, step['intersected_image'])
                ck(jl < ju, 'positive Newton image')
                target = max((ju-jl)*D, F(D, 2**560))
                center = (jl+ju)*D/2
                ll, uu, h = oldlo, oldhi, oldhi-oldlo
                initial_depth = depth
                passes = step['binary_halvings']
                ck(isinstance(passes, int) and passes >= 0, 'nonnegative finite pass count')
                for _ in range(passes):
                    ck(h > target, 'while test true')
                    ck(depth < 640, 'failure-context branch false and depth guard true')
                    ck((ll+uu) % 2 == 0, 'midpoint exactness guard true')
                    mid = (ll+uu)//2
                    if mid <= center:
                        ll = mid
                    else:
                        uu = mid
                    ck(h % 2 == 0, 'width exactness guard true')
                    h //= 2
                    depth += 1
                ck(h <= target, 'terminal while test false')
                ck(uu-ll == h and h > target/2, 'terminal cell invariant')
                ck(depth == step['depth'], 'depth and all passes reconstructed')
                ck((max(oldlo,ll-h), min(oldhi,uu+h)) == tuple(map(zi,step['new_grid_interval'])), 'converted output unchanged')
                conversions.append({'degree': row['degree'], 'root_index': root['index_descending'],
                    'newton_index': number, 'initial_depth': initial_depth, 'final_depth': depth,
                    'passes': passes, 'scheduled_pass_charge': 12*passes,
                    'selected_source_operations': rate*passes})
    passes = sum(v['passes'] for v in conversions)
    ck(len(conversions) == 949 and passes == 71491, 'all949 conversions and71491 passes')
    ck(all(data['guard_counts'][name] == passes for name in (
        'binary conversion grid not exhausted', 'conversion midpoint exact', 'conversion width halving exact')), 'all three guard inventories agree')
    scheduled = data['scalar_work']['scheduled_charge']
    ck(scheduled == ledger['scheduled_counter'] == 4622876, 'unchanged scheduled total')
    ck(data['scalar_work']['by_category']['binary_conversion_halvings'] == 12*passes == 857892, 'scheduled component reconstructed')
    delta = (rate-12)*passes
    ck(rate*passes == 1215347 and delta == 357455, 'selected component discrepancy exact')
    ck(scheduled+delta == 4980331 < 5000000, 'hybrid arithmetic does not prove a cap failure')
except AssertionError:
    pass

report = {'result': 'PASS_COMPONENT_UNDERCHARGE_AUDIT' if not failures else 'FAIL',
    'checks_by_name': dict(sorted(checks.items())), 'failures': failures,
    'source_fragments': fragments, 'conversions': conversions,
    'conclusion': {
        'source_pass_subset': dict(subset) if fragments else {},
        'scheduled_rate': 12, 'selected_source_rate': 17,
        'total_passes': 71491, 'component_scheduled': 857892,
        'component_selected_source': 1215347, 'component_shortfall': 357455,
        'old_scheduled_total': 4622876, 'hybrid_sum_not_a_bound': 4980331,
        'hybrid_headroom_not_certified': 19669, 'required_complete_upper': 5000000,
        'complete_scalar_upper_established': False, 'total_scalar_lower_established': False,
        'decision': 'Stop fixed692 as a paid setup prescription; retain its all261 accuracy result.',
        'unresolved': 'Remainder implementation, complete other-category domination and full scalar transcript.',
        'qualification': 'Source-literal component audit only; two remainders and instrumentation given zero cost. No optimized-program or total-work lower bound. No new Gauss construction.'},
    'input_sha256': {p.name: sha256(p.read_bytes()).hexdigest() for p in (SOURCE, TRACE, REPLAY, LEDGER)},
    'script_sha256': sha256(HERE.read_bytes()).hexdigest()}
OUT.write_text(json.dumps(report, indent=2)+'\n')
print(report['result'])
if failures:
    print('Selected source counts:', dict(subset) if fragments else {})
    print('Checks:', sum(checks.values()), '; failures:', failures)
    print('Failed audit certificate:', OUT.relative_to(HERE.parents[2]))
    raise SystemExit(1)
print('Fixed692 conversion rate: scheduled12; selected executed operations17, plus two unimplemented scalar remainders.')
print('71491 passes: scheduled857892; selected1215347; discrepancy357455.')
print('Hybrid sum4980331 vs required complete upper5000000; hybrid sum is neither an upper nor lower bound.')
print('Complete work proof: NOT ESTABLISHED. Numerical accuracy: unchanged261 outputs.')
print('Checks:', sum(checks.values()), '; failures:', failures)
print('Full certificate:', OUT.relative_to(HERE.parents[2]))
