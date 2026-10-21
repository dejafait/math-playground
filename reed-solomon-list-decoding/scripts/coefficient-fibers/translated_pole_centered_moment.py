"""Exact normalization/overlap diagnostic, not an estimate of bulk collisions."""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations
from math import comb, factorial, prod
from pathlib import Path
import json

OUT = Path(__file__).with_name('translated-pole-centered-moment-results.json')
checks = []
def check(name, condition):
    checks.append({'name': name, 'passed': bool(condition)})
def rat(x):
    x = F(x)
    return {'numerator': x.numerator, 'denominator': x.denominator}
def bracket(x, scale):
    x = F(x)
    lo = x.numerator * scale // x.denominator
    check(f'bracket {len(checks)}', F(lo, scale) < x < F(lo+1, scale))
    return {'lower_numerator': lo, 'upper_numerator': lo+1, 'denominator': scale}

Q, n, s = 65537, 1024, 67
C, D, T = comb(n, s), (Q-1)*Q**2, F(Q**28, 2**128)
mu = F(C, D)
B = (T-mu)**2
baseline = F(C*C, D)
check('mean below threshold', 0 < mu < T)
check('factorial reconstruction', C == prod(range(n-s+1, n+1))//factorial(s))
rows = []
for r in range(s+1):
    w = comb(n-2*r, s-r)
    P = comb(n, r)*comb(n-r, r)
    fixed_first = comb(s, r)*comb(n-s, r)
    check(f'ordered overlap identity {r}', w*P == C*fixed_first)
    rows.append({'r': r, 'common_set_weight': w, 'ordered_disjoint_pairs': P,
                 'ordered_support_pairs': w*P, 'fixed_first_support_choices': fixed_first,
                 'forced_K': 1 if r == 0 else (0 if r <= 3 else None)})
check('all ordered support pairs', sum(x['ordered_support_pairs'] for x in rows) == C*C)
low_uniform = F(sum(x['ordered_support_pairs'] for x in rows[:4]), D)
delta = C-low_uniform
bulk_baseline = baseline-low_uniform
check('positive bulk baseline', 0 < low_uniform < baseline)
bulk_excess_required = B-delta
raw_required = baseline+B
bulk_raw_required = raw_required-C
check('positive forced low-overlap correction', 0 < delta < C)
check('low-overlap scale versus required energy', 0 < delta < B/F(2**280))
check('positive remaining excess budget', bulk_excess_required > 0)
check('bulk threshold decomposition', bulk_baseline+bulk_excess_required == bulk_raw_required)
check('raw threshold decomposition', C+bulk_raw_required == raw_required)
check('integer raw endpoint', raw_required.numerator//raw_required.denominator ==
      C+bulk_raw_required.numerator//bulk_raw_required.denominator)

# Complete direct finite checks, including empty labels. No floating Fourier sums.
q, hsize, pole = 17, 8, 3
H = tuple(sorted({pow(9, j, q) for j in range(hsize)}))
check('small domain avoids pole', len(H) == hsize and pole not in H)
def label(S):
    coeff = [1, 0, 0]
    for x in S:
        a = (pole-x) % q
        coeff = [(a*coeff[0]) % q, (a*coeff[1]+coeff[0]) % q,
                 (a*coeff[2]+coeff[1]) % q]
    return tuple(coeff)
sets = {r: tuple(frozenset(S) for S in combinations(H, r)) for r in range(hsize+1)}
labels = {S: label(S) for subsets in sets.values() for S in subsets}
K, Psmall = [], []
for r in range(hsize//2+1):
    count = sum(1 for A in sets[r] for J in combinations(sorted(set(H)-A), r)
                if labels[A] == labels[frozenset(J)])
    K.append(count)
    Psmall.append(comb(hsize, r)*comb(hsize-r, r))
    if r <= 3:
        check(f'small forced K_{r}', count == int(r == 0))
small = []
Dsmall = (q-1)*q*q
for ss in range(hsize+1):
    counts = Counter(labels[S] for S in sets[ss])
    M = sum(v*v for v in counts.values())
    weights = [comb(hsize-2*r, ss-r) if 0 <= ss-r <= hsize-2*r else 0
               for r in range(hsize//2+1)]
    pred = sum(w*k for w,k in zip(weights,K))
    total = sum(w*p for w,p in zip(weights,Psmall))
    Cs = comb(hsize, ss)
    check(f'small raw collision decomposition {ss}', pred == M)
    check(f'small all-pair decomposition {ss}', total == Cs*Cs)
    mus = F(Cs, Dsmall)
    V_direct = sum((v-mus)**2 for v in counts.values())+(Dsmall-len(counts))*mus**2
    V_centered = F(M)-F(Cs*Cs, Dsmall)
    V_overlap = sum(w*(F(k)-F(p,Dsmall)) for w,k,p in zip(weights,K,Psmall))
    check(f'small empty-label centering {ss}', V_direct == V_centered == V_overlap)
    # Directly classify EVERY ordered support pair by its canceled differences.
    histogram = Counter()
    for S in sets[ss]:
        for U in sets[ss]:
            r = len(S-U)
            check(f'small unit cancellation {ss}:{len(histogram)}:{len(checks)}',
                  (labels[S] == labels[U]) == (labels[S-U] == labels[U-S]))
            if labels[S] == labels[U]:
                histogram[r] += 1
    for r,w in enumerate(weights):
        check(f'small overlap cell {ss}:{r}', histogram[r] == w*K[r])
    small.append({'s': ss, 'C': Cs, 'occupied_labels': len(counts),
                  'raw_collisions': M, 'variance': rat(V_centered),
                  'weights': weights, 'collision_histogram': dict(histogram)})

summary = {
    'mean_over_T': bracket(mu/T, 10**12),
    'uniform_collision_baseline_over_required_energy': bracket(baseline/B, 1000),
    'allowed_relative_raw_collision_excess': bracket(B/baseline, 10**12),
    'allowed_relative_bulk_collision_excess': bracket(bulk_excess_required/bulk_baseline, 10**12),
    'delta_over_C': bracket(delta/C, 10**9),
    'forced_small_overlap_correction_below_energy_times_2_to_minus_280': delta*2**280 < B,
    'bulk_bound_established': False,
    'uniform_fiber_bound_established': False,
}
result = {'parameters': {'Q':Q, 'n':n, 's':s, 'C':C, 'D':D, 'T':rat(T)},
          'exact_thresholds': {'mean':rat(mu), 'required_energy':rat(B),
             'uniform_collision_baseline':rat(baseline), 'low_overlap_uniform_baseline':rat(low_uniform),
             'delta':rat(delta), 'bulk_uniform_baseline':rat(bulk_baseline),
             'required_bulk_centered_excess':rat(bulk_excess_required),
             'raw_collision_upper_endpoint':rat(raw_required),
             'bulk_raw_collision_upper_endpoint':rat(bulk_raw_required),
             'integer_bulk_raw_upper_endpoint':bulk_raw_required.numerator//bulk_raw_required.denominator},
          'overlap_rows': rows, 'small_field': {'q':q, 'H':H, 'pole':pole, 'D':Dsmall,
                    'ordered_disjoint_collisions':K, 'all_cardinalities':small},
          'summary': summary, 'checks':checks,
          'failures':[c['name'] for c in checks if not c['passed']]}
OUT.write_text(json.dumps(result, indent=2)+'\n')
print(f'checks={len(checks)} failures={len(result["failures"])} certificate={OUT}')
for name,value in summary.items():
    print(f'{name}={value}')
if result['failures']:
    print('FAILURES:', result['failures'])
    raise SystemExit(1)
