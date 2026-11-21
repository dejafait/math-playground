#!/usr/bin/env python3
"""Fixed prescribed common-radius prerequisite; no inverses or new moments.

Incremental certificate only. Counters are mandatory-work LOWER bounds,
not complete construction/validation upper bounds. See saved draft735.
"""
from pathlib import Path
from hashlib import sha256
from decimal import Decimal as D, localcontext
import json

HERE = Path(__file__).resolve()
SOURCE = HERE.with_name('fixed-support-shared-734.py')
INPUT = HERE.with_name('fixed-support-shared-734.json')
OUT = HERE.with_suffix('.json')
# Reuse only definitions/constants before734's explicitly marked execution.
# This executes no anchor construction, top-level numerical test or file write.
namespace = {'__file__': str(SOURCE)}
exec(compile(SOURCE.read_text().split('# Before numerical work:')[0],
             str(SOURCE), 'exec'), namespace)
q = namespace['q']
DOWN, UP = namespace['DOWN'], namespace['UP']
nodes_and_matrix = namespace['nodes_and_matrix']
error_certificate = namespace['error_certificate']
export = namespace['export']
N, CAP, WORK_CAP = 35, 15, 10**8
data = json.loads(INPUT.read_text())
assert sha256(SOURCE.read_bytes()).hexdigest() == data['script_sha256']
assert data['parameters']['labels'] == namespace['LABELS']
assert data['parameters']['precision'] == 256
RA = [[D(v) for v in row] for row in data['anchor']['interpolation_preconditioner']]
assert len(RA) == N and all(len(row) == N for row in RA)

report = {
    'scope': 'interpolation common-componentwise-radius prerequisite only',
    'script_sha256': sha256(HERE.read_bytes()).hexdigest(),
    'input_sha256': sha256(INPUT.read_bytes()).hexdigest(),
    'helper_sha256': sha256(SOURCE.read_bytes()).hexdigest(),
    'parameters': {'precision': 256, 'iteration_cap': CAP, 'inflation': '1.125',
                   'initial_radius': '1', 'required_k': list(range(11,72)),
                   'labels': data['parameters']['labels'], 'work_cap': WORK_CAP},
    'pricing': {'full_interpolation_products_lower': 61*N**3*12,
                'complete_work_upper': None, 'complete_byte_storage_upper': None,
                'reference_production': '734/731 supplied inputs; NOT free full construction'},
    'blocks': [], 'prefix_radius_tests': [], 'checks': {}, 'failures': []}
M = [[D(0) for _ in range(N)] for _ in range(N)]
radius_terms, radius_updates = 0, 0

with localcontext() as ctx:
    ctx.prec = 256
    for k in range(11,72):
        indices, nodes, exactA, A = nodes_and_matrix(2**k)
        cert = error_certificate(RA, A)
        report['blocks'].append({'k': k, 'indices': indices, 'nodes': list(map(str,nodes)),
                                 'error_intervals': cert['error_intervals']})
        for i in range(N):
            for j in range(N):
                a,b = cert['error_intervals'][i][j]
                M[i][j] = max(M[i][j], a.copy_abs(), b.copy_abs())
        d = [D(1)]*N
        trials = []
        passed = False
        for iteration in range(1,CAP+1):
            y = []
            for i in range(N):
                total = D(0)
                for j in range(N):
                    total = UP.add(total, UP.multiply(M[i][j], d[j]))
                    radius_terms += 1
                y.append(total)
            inequalities = [y[i] < d[i] for i in range(N)]
            trials.append({'iteration': iteration, 'd': d, 'y_upper': y,
                           'all_strict': all(inequalities),
                           'failed_coordinates': [i for i,v in enumerate(inequalities) if not v]})
            if all(inequalities):
                passed = True
                break
            # Every scalar term costs at least multiply, add, total store,
            # j binding and successful loop advance =5 units (under-count).
            # Every update costs multiply,add,d store =3 units (under-count).
            charged = namespace['counts']['directed_scalar_product_terms']*12 + radius_terms*5 + radius_updates*3
            if charged > WORK_CAP:
                report['failures'].append({'k': k, 'reason': 'mandatory-work lower bound exceeds cap'})
                break
            if iteration < CAP:
                d = [UP.add(D(1), UP.multiply(D('1.125'), v)) for v in y]
                radius_updates += N
        report['prefix_radius_tests'].append({'last_k': k, 'pass': passed, 'trials': trials})
        print('Prefix 11..'+str(k)+':', 'PASS' if passed else 'STOP',
              '; checks:', len(trials), '; required: all35 strict y_i<d_i', flush=True)
        if not passed:
            if not report['failures']:
                report['failures'].append({'k': k, 'reason': 'fixed15-check common-radius inclusion not certified'})
            break

report['common_absolute_upper_matrix'] = M
report['counts'] = {'matrix_product_terms': namespace['counts']['directed_scalar_product_terms'],
                    'radius_product_terms': radius_terms, 'radius_updates': radius_updates,
                    'new_inverse_calls': namespace['counts']['single_anchor_inverse_calls']}
report['pricing']['executed_mandatory_lower'] = report['counts']['matrix_product_terms']*12 + radius_terms*5 + radius_updates*3
report['status'] = 'STOP_BOUNDED_INCLUSION' if report['failures'] else 'INTERPOLATION_PREREQUISITE_ONLY'
report['checks'] = {
    'unchanged_helper_hash': report['helper_sha256'] == data['script_sha256'],
    'fixed35_labels': len(namespace['LABELS']) == len(set(namespace['LABELS'])) == 35,
    'no_new_inverse_calls': report['counts']['new_inverse_calls'] == 0,
    'no_more_than15_checks': all(len(p['trials']) <= CAP for p in report['prefix_radius_tests']),
    'all_intervals_ordered': all(a <= b for block in report['blocks'] for row in block['error_intervals'] for a,b in row),
    'common_M_dominates_every_recorded_error': all(max(a.copy_abs(),b.copy_abs()) <= M[i][j]
        for block in report['blocks'] for i,row in enumerate(block['error_intervals']) for j,(a,b) in enumerate(row)),
    'stop_or_complete61_prefixes': bool(report['failures']) or len(report['blocks']) == 61}
report['failed_checks'] = [k for k,v in report['checks'].items() if not v]
OUT.write_text(json.dumps(export(report),indent=2)+'\n')
print('Status:', report['status'], '; failures:', report['failures'])
print('Mandatory-work lower:', report['pricing']['executed_mandatory_lower'],
      '; cap:', WORK_CAP, '; full upper ledger/storage UNPAID')
print('Checks:', sum(report['checks'].values()), '/', len(report['checks']), '; failed:', report['failed_checks'])
print('Certificate:', OUT.relative_to(HERE.parents[2]))
if report['failed_checks']:
    raise SystemExit(1)
