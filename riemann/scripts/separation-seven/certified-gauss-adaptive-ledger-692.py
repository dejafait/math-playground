#!/usr/bin/env python3
"""Independently reconstruct scheduled charges; do not certify their completeness."""
from collections import Counter
from hashlib import sha256
from pathlib import Path
import json

HERE = Path(__file__).resolve()
SOURCE = HERE.with_name('certified-gauss-adaptive-692.json')
OUT = HERE.with_suffix('.json')
data = json.loads(SOURCE.read_text())
expected = Counter({'grid_constant':640*6,
    'fixed_constant_and_output_administration':10000,
    'tolerance_constant_reserve':4000,'recurrence_constant_tables':117*20,
    'degree_constants':3*30,'mesh_generation':128*20,
    'mesh_domain_and_order':600,'final_global_guards':100})
checks, failures, rows = [], [], []
def ck(name, condition):
    checks.append({'name':name,'pass':bool(condition)})
    if not condition:
        failures.append(name)
for row in data['rows']:
    n = row['degree']
    mesh = len(row['mesh_sign_evidence'])
    roots = len(row['positive_roots'])
    trials = sum(len(r['adaptive_trials']) for r in row['positive_roots'])
    bis = sum(len(r['bisections']) for r in row['positive_roots'])
    newton = sum(len(r['newton']) for r in row['positive_roots'])
    halvings = sum(s['binary_halvings'] for r in row['positive_roots'] for s in r['newton'])
    final = sum('final' in r for r in row['positive_roots'])
    zero = int('zero_node' in row)
    deriv = trials+newton-roots+final
    calls = mesh+deriv+zero
    expected.update({'mesh_evaluation_control':mesh*12,
        'sign_bracket_inventory':127*12,'root_count_check':20,
        'root_initialization_and_output':roots*100,'adaptive_prefix_control':trials*100,
        'newton_image_and_control':newton*90,'derivative_enclosures':deriv*120,
        'point_recurrence':calls*(13*(n-1)+24),'binary_conversion_fixed':newton*40,
        'tolerance_cap_construction':newton*16,'binary_conversion_halvings':halvings*12,
        'weight_formation_and_output':final*100,'reflection_and_exact_output':final*40,
        'zero_root_and_weight':zero*80})
    ck(f'degree{n} complete prefix counts',trials == bis+roots and final == roots == (n-1)//2 and zero == 1)
    rows.append({'degree':n,'adaptive_trials':trials,'fallback_bisections':bis,
        'newton_updates':newton,'conversion_halvings':halvings,'derivative_calls':deriv,
        'point_calls':calls,'positive_outputs':final,'zero_outputs':zero})
ck('all category charges reconstructed',dict(expected) == data['scalar_work']['by_category'])
total = sum(expected.values())
ck('scheduled counter meets cap',total == data['scalar_work']['scheduled_charge'] == 4622876 <= 5000000)
ck('all point calls accounted for',sum(r['point_calls'] for r in rows) == data['guard_counts']['point in [0,1]'] == 2606)
ck('all derivative calls accounted for',sum(r['derivative_calls'] for r in rows) == data['guard_counts']['exact grid midpoint'] == 2219)
ck('all conversion passes accounted for',sum(r['conversion_halvings'] for r in rows) == data['guard_counts']['conversion midpoint exact'] == 71491)
ck('construction guard outcome',data['failures'] == [] and data['summary']['all_nodes'] == data['summary']['all_weights'] == 261)
report = {'result':'PASS_SCHEDULED_COUNTER_RECONSTRUCTION' if not failures else 'FAIL',
    'checks':checks,'failures':failures,'rows':rows,'scheduled_by_category':dict(sorted(expected.items())),
    'scheduled_counter':total,'required_upper':5000000,'headroom':5000000-total,
    'complete_scalar_work_upper_bound_established':False,
    'unresolved':'Code-level domination of every operation, especially conversion parity/domain guards and assignments, remains to audit; no actual total-work claim.',
    'source_sha256':sha256(SOURCE.read_bytes()).hexdigest(),
    'script_sha256':sha256(HERE.read_bytes()).hexdigest()}
OUT.write_text(json.dumps(report,indent=2)+'\n')
print(report['result'])
print('Scheduled counter:',total,'; required <=5000000; headroom:',5000000-total)
print('Full operation upper bound established:',report['complete_scalar_work_upper_bound_established'])
print('Exact checks:',len(checks),'; failures:',failures)
print('Certificate:',OUT.relative_to(HERE.parents[2]))
if failures:
    raise SystemExit(1)
