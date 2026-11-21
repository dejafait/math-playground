#!/usr/bin/env python3
"""Exhaustive independent exact-integer replay of the common A contraction.

No import of either constructor. Integer polynomial coefficients/Horner
replace the constructor's rational value recurrence and directed products.
All61*35*35 errors are checked, not sampled. The full2135 exact row ratios
are saved; hashes bind each complete error matrix without log dumping.
This verification is not a cost upper bound for a production algorithm.
"""
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as F
from decimal import Decimal as D, localcontext
from math import lcm
import json
import sys

sys.set_int_max_str_digits(0)
HERE = Path(__file__).resolve()
INPUT = HERE.with_name('fixed-support-componentwise-735.json')
ANCHOR = HERE.with_name('fixed-support-shared-734.json')
OUT = HERE.with_suffix('.json')
data, anchor = json.loads(INPUT.read_text()), json.loads(ANCHOR.read_text())
N = 35
labels = data['parameters']['labels']
df = list(map(F,data['prefix_radius_tests'][-1]['trials'][-1]['d']))
rf = [[F(v) for v in row] for row in anchor['anchor']['interpolation_preconditioner']]
ld = lcm(*(v.denominator for v in df))
lr = lcm(*(v.denominator for row in rf for v in row))
di = [v.numerator*(ld//v.denominator) for v in df]
ri = [[v.numerator*(lr//v.denominator) for v in row] for row in rf]
polys = [[1], [0,1]]
for n in range(2,N):
    p = [0]*(n+1)
    for i,v in enumerate(polys[-1]):
        p[i+1] += 2*v
    for i,v in enumerate(polys[-2]):
        p[i] -= v
    polys.append(p)


def numerator(poly,h,Q):
    # Homogeneous integer Horner: return Q^34 T_a(h/Q).
    acc, power = poly[-1], Q
    for c in reversed(poly[:-1]):
        acc = acc*h+c*power
        power *= Q
    return acc*Q**(34-(len(poly)-1))


checks = {
    'constructor_hash_matches': data['script_sha256'] == sha256(HERE.with_name('fixed-support-componentwise-735.py').read_bytes()).hexdigest(),
    'anchor_hash_matches': data['input_sha256'] == sha256(ANCHOR.read_bytes()).hexdigest(),
    'same35_labels': labels == anchor['parameters']['labels'] and len(set(labels)) == N,
    'all61_actual_blocks': [b['k'] for b in data['blocks']] == list(range(11,72)),
    'full_preconditioner': len(rf) == N and all(len(row) == N for row in rf),
    'full_positive_common_radius': len(di) == N and min(di)>0,
    'all_floor_indices_and_nodes': True,
    'all74725_errors_enclosed': True,
    'all2135_exact_row_ratios_below_one': True,
    'common_M_dominates_all_exact_errors': True}
blocks, count = [], 0
max_ratio, max_location = F(0), None
for block in data['blocks']:
    k = block['k']
    J, Q = 2**k, 2**(k+1)
    indices = [J+(i*(J-1))//128 for i in labels]
    hs = [4*j+1-6*J for j in indices]
    checks['all_floor_indices_and_nodes'] &= (indices == block['indices'] and
        [F(h,Q) for h in hs] == list(map(F,block['nodes'])))
    ai = [[numerator(p,h,Q) for h in hs] for p in polys]
    denom = lr*Q**34
    ratios, digest = [], sha256()
    for i in range(N):
        row_abs_numerator = 0
        for j in range(N):
            e = int(i==j)*denom-sum(ri[i][a]*ai[a][j] for a in range(N))
            lo,hi = map(F,block['error_intervals'][i][j])
            checks['all74725_errors_enclosed'] &= (lo.numerator*denom <= e*lo.denominator and
                e*hi.denominator <= hi.numerator*denom)
            m = F(data['common_absolute_upper_matrix'][i][j])
            checks['common_M_dominates_all_exact_errors'] &= abs(e)*m.denominator <= m.numerator*denom
            row_abs_numerator += abs(e)*di[j]
            digest.update((str(e)+'/'+str(denom)+'\n').encode())
            count += 1
        ratio = F(row_abs_numerator,denom*di[i])
        ratios.append(str(ratio))
        checks['all2135_exact_row_ratios_below_one'] &= ratio < 1
        if ratio > max_ratio:
            max_ratio, max_location = ratio, [k,i]
    blocks.append({'k':k, 'exact_weighted_row_ratios': ratios,
                   'complete_error_matrix_unreduced_fraction_sha256': digest.hexdigest()})

# Independently check the FINAL common M certificate with exact rationals.
# This also covers simultaneous boxes, not just every single-matrix norm.
M = [[F(v) for v in row] for row in data['common_absolute_upper_matrix']]
common_ratios = [sum((M[i][j]*df[j] for j in range(N)),F(0))/df[i] for i in range(N)]
common_q = max(common_ratios)
checks['exact_common_M_radius_strict'] = common_q < 1
checks['exact_common_q_below_897_over1000'] = common_q < F(897,1000)
checks['exact_all35_final_y_upper'] = all(sum((M[i][j]*df[j] for j in range(N)),F(0)) <=
    F(data['prefix_radius_tests'][-1]['trials'][-1]['y_upper'][i]) for i in range(N))
checks['exact_entry_count'] = count == 74725
checks['no_constructor_failure'] = data['failures'] == [] and data['failed_checks'] == []
report = {'scope': 'all61 interpolation matrices and one common radius only; no Gram/weights/cost upper bound',
    'script_sha256': sha256(HERE.read_bytes()).hexdigest(),
    'input_sha256': sha256(INPUT.read_bytes()).hexdigest(),
    'anchor_sha256': sha256(ANCHOR.read_bytes()).hexdigest(),
    'common_radius_exact': list(map(str,df)), 'blocks': blocks,
    'common_M_weighted_row_ratios_exact': list(map(str,common_ratios)),
    'summary': {'exact_entries_checked':count, 'exact_rows_checked':len(blocks)*N,
        'max_actual_ratio_exact':str(max_ratio), 'max_actual_ratio_location':max_location,
        'common_q_exact':str(common_q), 'common_q_below_99_over100':common_q < F(99,100),
        'common_q_below_97_over100':common_q < F(97,100),
        'common_q_below_897_over1000':common_q < F(897,1000),
        'all_inclusion_threshold':'strictly below1',
        'gram_and_weights_validated':False, 'complete_work_upper':None},
    'checks': checks, 'failed_checks':[k for k,v in checks.items() if not v]}
OUT.write_text(json.dumps(report,indent=2)+'\n')
with localcontext() as ctx:
    ctx.prec = 15
    print('Exact common weighted ratio:', D(common_q.numerator)/D(common_q.denominator),
          '; required <1; actual matrix maximum:', D(max_ratio.numerator)/D(max_ratio.denominator))
print('Exact entries/rows:',count,len(blocks)*N,'; checks:',sum(checks.values()),'/',len(checks),'; failures:',report['failed_checks'])
print('Certificate:',OUT.relative_to(HERE.parents[2]))
if report['failed_checks']:
    raise SystemExit(1)
