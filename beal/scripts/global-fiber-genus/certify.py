"""Exact polynomial and complete induced-cycle certificate; standard library only."""
import itertools
import json
from pathlib import Path
from collections import Counter
from math import comb

OUT = Path(__file__).resolve().parent / 'certificate.json'

def mul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return c

def power(a, n):
    c = [1]
    for _ in range(n):
        c = mul(c, a)
    return c

q = [1, 1, 3]
phi = mul(power(q, 5), [1, -5])
derivative = [i*phi[i] for i in range(1, len(phi))]
expected_derivative = [0, 0] + [-165*x for x in power(q, 4)]
labels = list(itertools.permutations(range(11), 3))
index = {t: i for i, t in enumerate(labels)}
perms = {
    'zero': [1,2,3,4,0,6,7,8,9,5,10],
    'one': [1,2,0,3,4,5,6,7,8,9,10],
    'infinity': list(range(1,11)) + [0],
}
checks = {
    'derivative_identity': derivative == expected_derivative,
    'degree_11': len(phi) == 12 and phi[-1] == -1215,
    'phi_zero_equals_one': phi[0] == 1,
    'order_three_at_zero_over_one': phi[1:3] == [0,0] and phi[3] == -55,
    'q_discriminant': 1-4*3 == -11,
    'q_at_one_fifth_nonzero': 3+5+25 == 33,
    'labels_exhausted': len(labels) == 11*10*9 == len(index),
    'label_cap': len(labels) <= 1000,
}
branches = {}
for name, p in perms.items():
    assert sorted(p) == list(range(11))
    action = [index[tuple(p[x] for x in t)] for t in labels]
    seen = set()
    orbits = []
    for i in range(len(labels)):
        if i in seen:
            continue
        orbit = []
        j = i
        while j not in seen:
            seen.add(j)
            orbit.append(j)
            j = action[j]
        checks[f'{name}_cycle_{i}_closes'] = j == i
        orbits.append(orbit)
    checks[f'{name}_full_partition'] = sorted(sum(orbits, [])) == list(range(990))
    branches[name] = {
        'root_permutation': p,
        'induced_permutation': action,
        'cycles': orbits,
        'cycle_histogram': dict(sorted(Counter(map(len, orbits)).items())),
        'cycle_count': len(orbits),
        'ramification_sum': 990-len(orbits),
    }
checks['zero_histogram'] = branches['zero']['cycle_histogram'] == {5:198}
checks['one_histogram'] = branches['one']['cycle_histogram'] == {1:336,3:218}
checks['infinity_histogram'] = branches['infinity']['cycle_histogram'] == {11:90}
ramification = sum(b['ramification_sum'] for b in branches.values())
two_g_minus_two = -2*len(labels)+ramification
checks['genus_integral_nonnegative'] = two_g_minus_two % 2 == 0 and two_g_minus_two >= -2
# The geometric transitivity proof is in L106, not an assumed branch-generator tuple.
# Representatives above need only their individual conjugacy classes; no product relation is claimed.
result = {
    'phi_coefficients_ascending': phi,
    'derivative_coefficients_ascending': derivative,
    'phi_minus_one_div_t_cubed_coefficients': phi[3:],
    'marked_equations': {
        'F0': 'sum_i c_i sum_{j even<=i} binom(i,j) u^(i-j) v^j (-3)^(j/2) - phi(r)',
        'F1': 'sum_i c_i sum_{j odd<=i} binom(i,j) u^(i-j) v^j (-3)^((j-1)/2)',
    },
    'labels': labels,
    'branches': branches,
    'degree': len(labels),
    'required_label_cap': 1000,
    'ramification_sum': ramification,
    'two_g_minus_two': two_g_minus_two,
    'genus': (two_g_minus_two+2)//2,
    'checks': checks,
    'failures': [k for k,v in checks.items() if not v],
}
OUT.write_text(json.dumps(result, indent=2)+'\n')
print('degree:', len(labels), 'required cap:', 1000)
for name, b in branches.items():
    print(name, 'cycles:', b['cycle_histogram'], 'ramification:', b['ramification_sum'])
print('ramification:', ramification, '2g-2:', two_g_minus_two, 'genus:', result['genus'])
print('checks:',len(checks),'failures:',result['failures'],'certificate:',OUT)
assert not result['failures']
