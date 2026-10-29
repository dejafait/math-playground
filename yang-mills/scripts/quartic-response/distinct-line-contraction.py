"""Exact finite check for L285; no analytic/asymptotic verification.

Independently enumerate the ordered Wilson words, using the anisotropic
H_12 covariance tables in each of the three active plaquette orientations.
Save every monomial contribution and the exact required coefficients.
"""
from fractions import Fraction as Q
from itertools import combinations, product
from math import factorial
from pathlib import Path
import json


def vec(z=0, aa=0, j=0):
    return (Q(z), Q(aa), Q(j))


def add(x, y):
    return tuple(a + b for a, b in zip(x, y))


def scale(c, x):
    return tuple(c * a for a in x)


def strings(x):
    return [str(a) for a in x]


tables = {
    '12': {(0, 0): vec(Q(1, 4)), (2, 2): vec(Q(1, 4)),
           (0, 2): vec(Q(1, 4), Q(-1, 2)),
           (1, 3): vec(Q(1, 4), Q(-1, 2)),
           (0, 1): vec(j=1), (2, 3): vec(j=1),
           (0, 3): vec(j=-1), (1, 2): vec(j=-1),
           (1, 1): vec(Q(1, 4)), (3, 3): vec(Q(1, 4))},
    '13': {(0, 0): vec(Q(1, 4)), (2, 2): vec(Q(1, 4)),
           (0, 2): vec(Q(1, 4), j=-2)},
    '14': {(0, 0): vec(Q(1, 4)), (2, 2): vec(Q(1, 4)),
           (0, 2): vec(Q(1, 4), j=-2)},
}
required = {'12': vec(Q(1, 4), Q(-7, 12), Q(-4, 3)),
            '13': vec(j=Q(-1, 3)), '14': vec(j=Q(-1, 3))}
orientations = {}
failures = []
for orientation, table in tables.items():
    total = vec()
    monomials = []
    for ns in product(range(5), repeat=4):
        if sum(ns) != 4:
            continue
        word = tuple(edge for edge, n in enumerate(ns) for _ in range(n))
        weight = Q(-2)
        for n in ns:
            weight /= factorial(n)
        for edge in word:
            weight *= (1, 1, -1, -1)[edge]
        contribution = vec()
        for external in combinations(range(4), 2):
            if any(word[pos] not in (0, 2) for pos in external):
                continue
            internal = tuple(pos for pos in range(4) if pos not in external)
            trace = Q(0)
            for color in range(3):
                colors = tuple(0 if pos in external else color for pos in range(4))
                alpha, beta, gamma, delta = colors
                trace += Q(int(alpha == beta and gamma == delta)
                           - int(alpha == gamma and beta == delta)
                           + int(alpha == delta and beta == gamma), 8)
            pair = tuple(sorted(word[pos] for pos in internal))
            contribution = add(contribution, scale(weight * trace, table.get(pair, vec())))
        total = add(total, contribution)
        monomials.append({'powers': ns, 'contribution_Z_A_J': strings(contribution)})
    if len(monomials) != 35 or total != required[orientation]:
        failures.append({'orientation': orientation, 'actual': strings(total),
                         'required': strings(required[orientation])})
    orientations[orientation] = {
        'covariance_table_Z_A_J': {f'{i},{j}': strings(v) for (i, j), v in sorted(table.items())},
        'monomials': monomials, 'actual_Z_A_J': strings(total),
        'required_Z_A_J': strings(required[orientation]),
    }

# Normalization E[S4(Z+r y)]_{r^2} = y*A*y/4.
b_zaj = scale(4, tuple(sum(Q(orientations[o]['actual_Z_A_J'][i]) for o in tables)
                       for i in range(3)))
# A=Z-4I; J=1/48-A/12=1/48-Z/12+I/3.
z, aa, j = b_zaj
b_zic = (z + aa - j / 12, -4 * aa + j / 3, j / 48)
required_b = (Q(-2, 3), Q(20, 3), Q(-1, 6))
if b_zic != required_b:
    failures.append({'coefficient': 'b', 'actual': strings(b_zic), 'required': strings(required_b)})
a_zic = (Q(8), Q(4), Q(-3, 2))
complete_j = add(a_zic, scale(-3, b_zic))
required_j = (Q(10), Q(-16), Q(-1))
if complete_j != required_j:
    failures.append({'coefficient': 'a-3b', 'actual': strings(complete_j),
                     'required': strings(required_j)})
actual_residual = max(abs(x-y) for x, y in zip(b_zic + complete_j, required_b + required_j))
summary = {
    'passed': not failures, 'ordered_monomials_per_orientation': 35,
    'orientation_count': 3, 'actual_b_Z_I_constant': strings(b_zic),
    'required_b_Z_I_constant': strings(required_b),
    'actual_a_minus_3b_Z_I_constant': strings(complete_j),
    'required_a_minus_3b_Z_I_constant': strings(required_j),
    'actual_exact_residual': str(actual_residual), 'required_residual': '0',
    'failure_count': len(failures),
    'not_verified': ['Fourier-entry identities', 'uniform local approximation',
                     'boundary and source-half estimates', 'continuum Yang-Mills'],
}
out = Path(__file__).with_name('distinct-line-contraction-certificate.json')
out.write_text(json.dumps({'summary': summary, 'orientations': orientations,
                           'b_Z_A_J': strings(b_zaj), 'failures': failures}, indent=2) + '\n')
print('PASS' if summary['passed'] else 'FAIL', ': 35 exact Wilson monomials in each of 3 orientations')
print('Actual b [Z0,I1,constant]:', strings(b_zic), '; required:', strings(required_b))
print('Actual a-3b:', strings(complete_j), '; required:', strings(required_j))
print('Actual exact residual:', actual_residual, '; required: 0; failures:', len(failures))
print('Full certificate:', out)
raise SystemExit(0 if summary['passed'] else 1)
