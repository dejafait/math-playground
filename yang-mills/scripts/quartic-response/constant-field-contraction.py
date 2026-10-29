"""Exact rational bookkeeping of L279(8)'s SU(2) quartic plaquette.

Prints the coefficient of r^2 in E[4 p_4(Z+r y)] for constant
y_mu=(1,0,0), y_nu=0. Raw edges are mu(0),nu(mu),mu(nu),nu(0).
The proof of the asymptotic does not rely on this bookkeeping check.
"""
from fractions import Fraction as Q
from itertools import combinations, product
from math import factorial
from pathlib import Path
import json

signs = (1, 1, -1, -1)
coeff = {}
words = 0
for ns in product(range(5), repeat=4):
    if sum(ns) != 4:
        continue
    words += 1
    word = tuple(j for j, n in enumerate(ns) for _ in range(n))
    weight = Q(-2, 1)
    for n in ns:
        weight /= factorial(n)
    for j in word:
        weight *= signs[j]
    for chosen in combinations(range(4), 2):
        if any(word[j] not in (0, 2) for j in chosen):
            continue
        internal = tuple(j for j in range(4) if j not in chosen)
        tr = Q(0)
        for c in range(3):
            colors = tuple(0 if j in chosen else c for j in range(4))
            a, b, c1, d = colors
            tr += Q(int(a == b and c1 == d)
                    - int(a == c1 and b == d)
                    + int(a == d and b == c1), 8)
        key = tuple(sorted(word[j] for j in internal))
        coeff[key] = coeff.get(key, Q(0)) + weight * tr
coeff = {k: v for k, v in coeff.items() if v}
assert words == 35
# Translation/reflection symmetry gives equal same-direction variances.
# The two nu edges are separated by one mu unit.
required = {(0, 0): Q(-1, 12), (0, 1): Q(-1, 3),
            (0, 2): Q(1, 6), (0, 3): Q(1, 3),
            (1, 2): Q(1, 3), (1, 3): Q(1),
            (2, 2): Q(-1, 12), (2, 3): Q(-1, 3)}
# Independent degeneracies: a Gaussian constant only in direction mu
# gives zero; a Gaussian constant only in direction nu gives one.
parallel_constant = sum(v for (i, j), v in coeff.items()
                        if i in (0, 2) and j in (0, 2))
perpendicular_constant = sum(v for (i, j), v in coeff.items()
                             if i in (1, 3) and j in (1, 3))
out = Path(__file__).with_name('constant-field-contraction-certificate.json')
out.write_text(json.dumps({
    'scope': 'Exact single-plaquette constant-mu-field internal contraction only',
    'ordered_words': words,
    'actual': {f'{i},{j}': str(v) for (i, j), v in sorted(coeff.items())},
    'required': {f'{i},{j}': str(v) for (i, j), v in sorted(required.items())},
    'degeneracies': {'parallel_constant': str(parallel_constant),
                    'perpendicular_constant': str(perpendicular_constant)},
    'rejected_provisional_guess': {'1,1': '1/24', '1,3': '1/6', '3,3': '1/24'},
    'passed': coeff == required and parallel_constant == 0 and perpendicular_constant == 1,
    'not_verified': ['finite-domain kernel comparison', 'complete quartic asymptotic'],
}, indent=2) + '\n')
passed = coeff == required and parallel_constant == 0 and perpendicular_constant == 1
print('PASS' if passed else 'FAIL', ': all 35 ordered monomials and both constant-field degeneracies.')
print('Actual:', {str(k): str(v) for k, v in sorted(coeff.items())})
print('Required:', {str(k): str(v) for k, v in sorted(required.items())})
print('Certificate:', out)
raise SystemExit(0 if passed else 1)
