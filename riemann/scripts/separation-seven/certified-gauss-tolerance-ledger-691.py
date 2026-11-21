#!/usr/bin/env python3
"""Reconstruct the stopped prescription's counter, not an operation lower bound."""
from collections import Counter
from hashlib import sha256
from pathlib import Path
import json

HERE = Path(__file__).resolve()
SOURCE = HERE.with_name('certified-gauss-tolerance-cap-691.json')
OUT = HERE.with_suffix('.json')
data = json.loads(SOURCE.read_text())
expected = Counter({
    'grid_constant': 640*6,
    'fixed_constant_and_output_administration': 10000,
    'tolerance_constant_reserve': 4000,
    'recurrence_constant_tables': 117*20,
    'degree_constants': 3*30,
    'mesh_generation': 128*20,
    'mesh_domain_and_order': 600})
checks, failures, rows = [], [], []


def ck(name, condition):
    checks.append({'name': name, 'pass': bool(condition)})
    if not condition:
        failures.append(name)


for row in data['rows']:
    n = row['degree']
    mesh = len(row['mesh_sign_evidence'])
    roots = len(row['positive_roots'])
    bis = sum(len(r['bisections']) for r in row['positive_roots'])
    newton = sum(len(r['newton']) for r in row['positive_roots'])
    halvings = sum(s['binary_halvings'] for r in row['positive_roots'] for s in r['newton'])
    final = sum('final' in r for r in row['positive_roots'])
    zero = int('zero_node' in row)
    # At the last root's third bisection, overhead and the midpoint guard
    # completed, then ev's upfront payment crossed the cap before evaluation.
    aborted = int(n == 117)
    calls = mesh+bis+newton+final+zero+aborted
    expected.update({
        'mesh_evaluation_control': mesh*12,
        'sign_bracket_inventory': 127*12,
        'root_count_check': 20,
        'root_initialization_and_output': roots*100,
        'bisection_overhead': (bis+aborted)*40,
        'newton_image_and_control': newton*90,
        'derivative_enclosures': (newton+final)*120,
        'point_recurrence': calls*(13*(n-1)+24),
        'binary_conversion_fixed': newton*40,
        'tolerance_cap_construction': newton*16,
        'binary_conversion_halvings': halvings*12,
        'weight_formation_and_output': final*100,
        'reflection_and_exact_output': final*40,
        'zero_root_and_weight': zero*80})
    rows.append({'degree': n, 'recorded_bisections': bis,
                 'accepted_newton_updates': newton, 'positive_outputs': final,
                 'zero_outputs': zero, 'completed_point_evaluations': calls-aborted,
                 'aborted_upfront_point_payments': aborted})

ck('all category counters reconstructed', dict(expected) == data['scalar_work']['by_category'])
total = sum(expected.values())
last = 13*(117-1)+24
ck('unique counter stop', data['result'] == 'PRESCRIPTION_STOPPED'
   and data['failures'] == ['scalar setup cap exceeded'])
ck('last prefix location', len(data['rows']) == 3
   and len(data['rows'][2]['positive_roots']) == 53
   and len(data['rows'][2]['positive_roots'][-1]['bisections']) == 2
   and not data['rows'][2]['positive_roots'][-1]['newton'])
ck('last payment crosses cap', total-last == 4998958 <= 5000000 < total == 5000490)
ck('recorded and aborted point calls distinguished',
   data['guard_counts']['point in [0,1]'] == sum(r['completed_point_evaluations'] for r in rows) == 3214)
ck('failed evaluation not recorded', data['guard_counts']['bisection midpoint exact'] == 1971
   and data['guard_counts']['bisection point nonzero'] == 1970)
report = {'result': 'PASS_EXACT_COUNTER_RECONSTRUCTION' if not failures else 'FAIL',
          'checks': checks, 'failures': failures, 'rows': rows,
          'counter_by_category': dict(sorted(expected.items())),
          'actual_counter': total, 'required_cap': 5000000,
          'prefix_before_last_payment': total-last, 'last_upfront_payment': last,
          'qualification': 'A conservative scheduled charge exceeding a cap is not an actual work lower bound; no full setup upper bound is asserted.',
          'source_sha256': sha256(SOURCE.read_bytes()).hexdigest(),
          'script_sha256': sha256(HERE.read_bytes()).hexdigest()}
OUT.write_text(json.dumps(report, indent=2)+'\n')
print(report['result'])
print('Actual counter:', total, '; required <=5000000; final upfront charge:', last)
print('Exact checks:', len(checks), '; failures:', failures)
print('Full counter certificate:', OUT.relative_to(HERE.parents[2]))
if failures:
    raise SystemExit(1)
