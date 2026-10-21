"""Complete unordered-label and invariant-remainder certificate for L107."""
from collections import Counter
from itertools import combinations
from math import comb
from pathlib import Path
import json

OUT = Path(__file__).resolve().parent / 'quotient-certificate.json'
checks = {}


def check(name, value):
    checks[name] = bool(value)


def mul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return c


phi = [1]
for _ in range(5):
    phi = mul(phi, [1, 1, 3])
phi = mul(phi, [1, -5])

# Sparse polynomials in (r,u,z), with full coefficients saved below.
def add(*polys):
    ans = Counter()
    for p in polys:
        for monomial, c in p.items():
            ans[monomial] += c
    return {m: c for m, c in ans.items() if c}


def scale(p, c):
    return {m: c*a for m, a in p.items() if c*a}


def times(p, q):
    ans = Counter()
    for m, a in p.items():
        for n, b in q.items():
            ans[tuple(x+y for x, y in zip(m, n))] += a*b
    return {m: c for m, c in ans.items() if c}


one = {(0, 0, 0): 1}
u = {(0, 1, 0): 1}
constant_term = {(0, 2, 0): -1, (0, 0, 1): -3}
# Independently reduce T^i modulo T²−2uT+u²+3z, as A_i+B_i*T.
A, B = one, {}
sum_A, sum_B = {}, {}
for c in phi:
    sum_A = add(sum_A, scale(A, c))
    sum_B = add(sum_B, scale(B, c))
    A, B = times(constant_term, B), add(A, scale(times(u, B), 2))
minus_phi_r = {(i, 0, 0): -c for i, c in enumerate(phi) if c}
remainder_G0 = add(sum_A, times(u, sum_B), minus_phi_r)
remainder_G1 = sum_B

# Binomial evaluation at u+v*w with w²=−3 and z=v².
even, odd = Counter(), Counter()
for i, c in enumerate(phi):
    for j in range(i+1):
        term = c * comb(i, j) * (-3)**(j//2)
        target = even if j % 2 == 0 else odd
        target[(0, i-j, j//2)] += term
G0 = add(dict(even), minus_phi_r)
G1 = add(dict(odd))
check('invariant_G0_equals_quadratic_remainder', G0 == remainder_G0)
check('invariant_G1_equals_quadratic_remainder', G1 == remainder_G1)
check('quadratic_discriminant', add(scale(times(u, u), 4),
      scale({(0, 2, 0): 1, (0, 0, 1): 3}, -4)) == {(0, 0, 1): -12})
check('square_class_constant', -12 == -3 * 2**2)

labels = [(r, a, b) for r in range(11)
          for a, b in combinations([t for t in range(11) if t != r], 2)]
index = {t: i for i, t in enumerate(labels)}
check('complete_quotient_labels', len(labels) == len(index) == 495)
check('maximum_label_universe_within_cap', 11*10*9 == 990 <= 1000)
perms = {
    'zero': [1, 2, 3, 4, 0, 6, 7, 8, 9, 5, 10],
    'one': [1, 2, 0, 3, 4, 5, 6, 7, 8, 9, 10],
    'infinity': list(range(1, 11)) + [0],
}
expected = {'zero': {5: 99}, 'one': {1: 168, 3: 109}, 'infinity': {11: 45}}
branches = {}
for name, p in perms.items():
    check(name+'_root_permutation', sorted(p) == list(range(11)))
    action = [index[(p[r], *sorted((p[a], p[b])))] for r, a, b in labels]
    check(name+'_quotient_action_bijective', sorted(action) == list(range(495)))
    cycles, return_data, seen = [], [], set()
    for start in range(495):
        if start in seen:
            continue
        cycle, pos = [], start
        while pos not in seen:
            seen.add(pos)
            cycle.append(pos)
            pos = action[pos]
        check(f'{name}_cycle_{start}_closes', pos == start)
        ordered_start = labels[start]
        ordered_return = ordered_start
        for _ in cycle:
            ordered_return = tuple(p[t] for t in ordered_return)
        check(f'{name}_cycle_{start}_ordered_return_has_no_swap',
              ordered_return == ordered_start)
        return_data.append({'start': ordered_start, 'after_one_quotient_cycle': ordered_return,
                            'local_degree_ratio': 1 if ordered_return == ordered_start else 2})
        cycles.append(cycle)
    check(name+'_full_disjoint_partition',
          sorted(t for c in cycles for t in c) == list(range(495)))
    histogram = dict(Counter(map(len, cycles)))
    check(name+'_expected_histogram', histogram == expected[name])
    ramification = sum(len(c)-1 for c in cycles)
    branches[name] = {'root_permutation': p, 'quotient_action': action,
                      'cycles': cycles, 'ordered_returns': return_data,
                      'cycle_histogram': histogram, 'ramification_sum': ramification,
                      'ordered_cycle_histogram': {e: 2*n for e, n in histogram.items()}}

ramification = sum(b['ramification_sum'] for b in branches.values())
rhs = -2*495 + ramification
genus = (rhs+2)//2
check('quotient_ramification_sum', ramification == 1064)
check('quotient_rh_and_genus', rhs == 74 and genus == 38)
check('unramified_double_cover_genus_consistency', 2*75-2 == 2*(2*genus-2))
result = {
    'degree': 495, 'ordered_degree': 990, 'required_label_cap': 1000,
    'phi_coefficients_ascending': phi,
    'invariant_polynomials': {
        name: [{'exponents_r_u_z': list(m), 'coefficient': c} for m, c in sorted(p.items())]
        for name, p in [('G0', G0), ('G1', G1)]},
    'quotient_labels': labels, 'branches': branches,
    'ramification_sum': ramification, 'two_g_minus_two': rhs, 'genus': genus,
    'checks': checks, 'check_count': len(checks),
    'failures': [k for k, v in checks.items() if not v],
    'limits': 'Actual monodromy and the marked-cover comparison come from audited L106; '
              'invariant rings, normalization, and rational lifting are proved in L107. '
              'Individual branch representatives are not a branch-generator tuple.',
}
OUT.write_text(json.dumps(result, indent=2)+'\n')
print('Quotient degree:', 495, 'ordered degree:', 990, 'required label cap:', 1000)
for name, b in branches.items():
    print(name, 'cycles:', b['cycle_histogram'], 'ramification:', b['ramification_sum'],
          'boundary double-cover degree ratios:', sorted({x['local_degree_ratio']
                                                        for x in b['ordered_returns']}))
print('Total ramification:', ramification, '2g-2:', rhs, 'genus:', genus)
print('Checks:', len(checks), 'failures:', result['failures'], 'certificate:', OUT)
assert not result['failures']
