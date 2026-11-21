#!/usr/bin/env python3
"""Bounded original-Gram/rounded-weight test with fixed734 preconditioners.

Reuses735's completed interpolation certificate; no new inverse/NNLS.
All work counters are mandatory LOWER bounds, never complete upper costs.
"""
from pathlib import Path
from hashlib import sha256
from decimal import Decimal as D, localcontext
from fractions import Fraction as F
from math import comb
import json
import sys

sys.set_int_max_str_digits(0)
HERE = Path(__file__).resolve()
OUT = HERE.with_suffix('.json')
HELPER = HERE.with_name('fixed-support-shared-734.py')
ANCHOR = HERE.with_name('fixed-support-shared-734.json')
INTERP = HERE.with_name('fixed-support-componentwise-735.json')
REPLAY = HERE.with_name('fixed-support-componentwise-replay-735.json')
ns = {'__file__': str(HELPER)}
exec(compile(HELPER.read_text().split('# Before numerical work:')[0], str(HELPER), 'exec'), ns)
down, up = ns['DOWN'], ns['UP']
add, sub, scale = ns['add'], ns['sub'], ns['scale']
sum_intervals, export = ns['sum_intervals'], ns['export']
anchor, interp, replay = [json.loads(p.read_text()) for p in [ANCHOR, INTERP, REPLAY]]
assert sha256(HELPER.read_bytes()).hexdigest() == anchor['script_sha256']
assert sha256(ANCHOR.read_bytes()).hexdigest() == interp['input_sha256']
assert sha256(INTERP.read_bytes()).hexdigest() == replay['input_sha256']
assert replay['failed_checks'] == [] and interp['failed_checks'] == []
N, CAP, WORK_CAP = 35, 15, 10**8
RA = [[D(v) for v in row] for row in anchor['anchor']['interpolation_preconditioner']]
RH = [[D(v) for v in row] for row in anchor['anchor']['gram_preconditioner']]
d = list(map(D, interp['prefix_radius_tests'][-1]['trials'][-1]['d']))
M = [[D(v) for v in row] for row in interp['common_absolute_upper_matrix']]
assert min(d) > 0 and len(d) == N
counts = {'candidate_dot_terms': 0, 'candidate_updates': 0,
          'interval_vector_terms': 0, 'radius_terms': 0}
report = {
    'script_sha256': sha256(HERE.read_bytes()).hexdigest(),
    'input_hashes': {p.name: sha256(p.read_bytes()).hexdigest() for p in [HELPER, ANCHOR, INTERP, REPLAY]},
    'parameters': {'precision': 256, 'iteration_cap': CAP, 'inflation': '1.125',
        'labels': ns['LABELS'], 'required_k': list(range(11,72)),
        'epsilon_limit': '5e-19', 'work_cap': WORK_CAP, 'new_inverse_calls': 0},
    'blocks': [], 'checks': {}, 'failures': [],
    'pricing': {'two_full_family_products_lower': 61*2*N**3*12,
        'complete_work_upper': None, 'peak_bytes_upper': None,
        'boundary': 'incremental test;734/731 production and735 replay not free in a full construction'}}
assert report['pricing']['two_full_family_products_lower'] <= WORK_CAP


def point_dot(a, b):
    total = D(0)
    for j in range(N):
        total += a[j]*b[j]
        counts['candidate_dot_terms'] += 1
    return total


def interval_dot(row, x):
    total = (D(0), D(0))
    for j in range(N):
        total = add(total, scale(row[j], x[j]))
        counts['interval_vector_terms'] += 1
    return total


def upper_dot(row, x):
    total = D(0)
    for j in range(N):
        total = up.add(total, up.multiply(row[j], x[j]))
        counts['radius_terms'] += 1
    return total


def abs_upper(v):
    return max(v[0].copy_abs(), v[1].copy_abs())


def lower_work():
    # Candidate term: mult/add/total store/j binding/advance =5.
    # Candidate update: add + store =2. Interval term: four arithmetic,
    # total store, j binding, advance =7. Radius term: same5 as point.
    return (interp['pricing']['executed_mandatory_lower']
        + ns['counts']['directed_scalar_product_terms']*12
        + counts['candidate_dot_terms']*5 + counts['candidate_updates']*2
        + counts['interval_vector_terms']*7 + counts['radius_terms']*5)


with localcontext() as ctx:
    ctx.prec = 256
    q = max(up.divide(upper_dot(M[i], d), d[i]) for i in range(N))
    assert q < D('0.897')
    report['common_interpolation_q_upper'] = q
    rh_norm = max(ns['sum_up']([v.copy_abs() for v in row]) for row in RH)
    bern = [F(1)]
    for n in range(1, 129):
        bern.append(-sum((F(comb(n+1,j))*bern[j] for j in range(n)), F(0))/(n+1))
    periodic = abs(bern[128])+sum((F(comb(128,j))*abs(bern[j]) for j in range(129)), F(0))
    for k in range(11,72):
        J = 2**k
        moments, evidence = ns['original_moments'](J, bern, periodic)
        indices, nodes, exactA, A = ns['nodes_and_matrix'](J)
        H = ns['gram'](moments)
        gram = ns['error_certificate'](RH, H)
        block = {'k': k, 'indices': indices, 'nodes': list(map(str,nodes)),
            'original_moments': moments, 'moment_evidence': evidence, 'gram': gram}
        report['blocks'].append(block)
        if not gram['contraction_pass']:
            report['failures'].append({'k':k, 'reason':'bounded shared Gram contraction not certified'})
            break
        am = [[ns['midpoint'](v) for v in row] for row in A]
        bm = [ns['midpoint'](v) for v in moments[:N]]
        x, trace = [D(0)]*N, []
        for iteration in range(1,CAP+1):
            rr = [bm[i]-point_dot(am[i],x) for i in range(N)]
            xx = [x[i]+point_dot(RA[i],rr) for i in range(N)]
            counts['candidate_updates'] += N
            x = xx
            trace.append({'iteration':iteration, 'midpoint_residual_max':
                max(abs(bm[i]-point_dot(am[i],x)) for i in range(N))})
        residual = [sub(moments[i], interval_dot(A[i],x)) for i in range(N)]
        z = [interval_dot([residual[j] for j in range(N)],RA[i]) for i in range(N)]
        znorm = max(up.divide(abs_upper(z[i]),d[i]) for i in range(N))
        t = up.multiply(D('1.125'),up.divide(znorm,down.subtract(D(1),q)))
        radii = [up.multiply(t,v) for v in d]
        image_radii = [up.add(abs_upper(z[i]),upper_dot(M[i],radii)) for i in range(N)]
        inclusion = all(image_radii[i] < radii[i] for i in range(N))
        lower = [down.subtract(x[i],radii[i]) for i in range(N)]
        rmax = max(map(abs_upper,residual))
        inverse_bound = up.divide(rh_norm,down.subtract(D(1),gram['norm_upper']))
        eps2 = up.multiply(D(N),up.multiply(up.multiply(rmax,rmax),inverse_bound))
        lower_abs = [D(0) if a <= 0 <= b else min(a.copy_abs(),b.copy_abs()) for a,b in residual]
        checks = {'original_mass_below_one': D(0) < moments[0][0] <= moments[0][1] < 1,
            'strict_residual_centered_inclusion': inclusion,
            'all_rounded_weights_positive': min(x) > 0,
            'exact_interpolation_solution_positive': min(lower) > 0,
            'original_rounded_residual_bound_pass': F(eps2) <= F(5,10**19)**2}
        block.update({'candidate_trace':trace, 'weights':x, 'original_residual':residual,
            'preconditioned_residual':z, 'box_scale_upper':t, 'box_radii':radii,
            'image_radii_upper':image_radii, 'weight_solution_lower':lower,
            'gram_inverse_norm_upper':inverse_bound, 'epsilon_squared_upper':eps2,
            'chebyshev_residual_absolute_lower_max':max(lower_abs),
            'certified_rounded_residual_failure': max(lower_abs)>D('5e-19'),
            'checks':checks, 'mandatory_work_lower':lower_work()})
        print('k='+str(k), '; Gram q<'+format(gram['norm_upper'],'.7g'),
            '; eps^2 upper='+format(eps2,'.7g'), '; required<=2.5e-37',
            '; inclusion='+str(inclusion), '; positive='+str(min(x)>0), flush=True)
        failed = [key for key,value in checks.items() if not value]
        if failed:
            report['failures'].append({'k':k,'reason':'fixed15-step sufficient weight/residual validation failed',
                'failed_checks':failed, 'genuine_residual_failure_certified':block['certified_rounded_residual_failure']})
            break
        if lower_work()>WORK_CAP:
            report['failures'].append({'k':k,'reason':'mandatory-work lower exceeds cap'})
            break

report['counts_lower_subtotals'] = {**counts, 'gram_product_terms':ns['counts']['directed_scalar_product_terms']}
report['pricing']['executed_combined_lower'] = lower_work()
report['status'] = 'STOP_BOUNDED_TEST' if report['failures'] else 'NUMERICAL_PASS_COST_UNPAID'
report['checks'] = {
    'unchanged35_labels': ns['LABELS']==anchor['parameters']['labels']==interp['parameters']['labels'],
    'zero_new_inverses':ns['counts']['single_anchor_inverse_calls']==0,
    'bounded15_candidate_iterations':all(len(b.get('candidate_trace',[]))<=CAP for b in report['blocks']),
    'all_original_moment_intervals_ordered':all(a<=b for block in report['blocks'] for a,b in block['original_moments']),
    'all_gram_error_intervals_ordered':all(a<=b for block in report['blocks'] for row in block['gram']['error_intervals'] for a,b in row),
    'stop_or_all61_blocks':bool(report['failures']) or len(report['blocks'])==61}
report['failed_integrity_checks'] = [key for key,value in report['checks'].items() if not value]
OUT.write_text(json.dumps(export(report),indent=2)+'\n')
print('Status:',report['status'],'; failures:',report['failures'])
print('Combined mandatory LOWER work:',lower_work(),'; required complete UPPER<=',WORK_CAP,'; not established')
print('Integrity checks:',sum(report['checks'].values()),'/',len(report['checks']),'; failures:',report['failed_integrity_checks'])
print('Certificate:',OUT.relative_to(HERE.parents[2]),'; bytes:',OUT.stat().st_size,'; peak bytes upper UNPAID')
if report['failed_integrity_checks']:
    raise SystemExit(1)
