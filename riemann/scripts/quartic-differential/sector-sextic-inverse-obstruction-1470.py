"""Exact certificate for the sextic inverse-positivity obstruction C020o.

This does not certify or exclude the requested nonreal-count pair (2,4).
Uses only rational polynomial algebra; Walsh supplies universal preservation.
"""
from fractions import Fraction as F
from itertools import permutations
from math import factorial
from pathlib import Path
import json


def mul(p, q):
    out = [F(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i+j] += a*b
    return out


def act(coeffs, p):
    return [sum((coeffs[k] * p[j+k] * F(factorial(j+k), factorial(j))
                 for k in range(min(len(coeffs), len(p)-j))), F(0))
            for j in range(len(p))]


def det(matrix):
    n = len(matrix)
    total = F(0)
    for perm in permutations(range(n)):
        term = F((-1) ** sum(perm[i] > perm[j]
                             for i in range(n) for j in range(i+1, n)))
        for i in range(n):
            term *= matrix[i][perm[i]]
        total += term
    return total


def encode(obj):
    if isinstance(obj, F):
        return str(obj)
    if isinstance(obj, list):
        return [encode(x) for x in obj]
    if isinstance(obj, dict):
        return {k: encode(v) for k, v in obj.items()}
    return obj


q = [F(1), F(1), F(5, 18)]
r = [F(1), F(-1)]
for k in range(2, 7):
    r.append(-r[-1] - q[2]*r[-2])
product = mul(q, r)[:7]
moments = [F(factorial(k))*r[k] for k in range(7)]
H = [[moments[i+j] for j in range(4)] for i in range(4)]
minors = [det([row[:k] for row in H[:k]]) for k in range(1, 5)]
h = [F(558), F(2084), F(1782), F(393)]
f = mul(h, h)
f[0] += 1
p = act(r, f)
image = act(q, p)
quadratic_form = sum((h[i]*h[j]*H[i][j] for i in range(4)
                      for j in range(4)), F(0))
appell = act(q, [F(0)]*6+[F(1)])
walsh_coeffs = [F(factorial(6-k), factorial(6))*appell[6-k]
                for k in range(7)]
basis_flags = []
for j in range(7):
    monomial = [F(0)]*j+[F(1)]
    basis_flags.append(act(walsh_coeffs, monomial) == act(q, monomial))

checks = {
    'inverse_product_mod_D7': product == [F(1)]+[F(0)]*6,
    'inverse_coefficients': r == list(map(F, ['1', '-1', '13/18', '-4/9',
                                             '79/324', '-13/108', '307/5832'])),
    'moment_minors': minors == list(map(F, ['1', '4/9', '131/729', '-1238/19683'])),
    'quadratic_form': quadratic_form == F(-162178, 3),
    'negative_inverse_value': p[0] == F(-162175, 3) and p[0] < 0,
    'operator_image_identity': image == f,
    'strictly_positive_input_representation': f == [mul(h, h)[0]+1]+mul(h, h)[1:],
    'sector_root_sum': 2*F(-9, 5) == -q[1]/q[2],
    'sector_root_product': F(9, 5)**2+F(3, 5)**2 == q[0]/q[2],
    'sector_boundary': F(3, 5) == F(9, 5)/3,
    'appell_factorization': appell == [F(0)]*4+[F(25, 3), F(6), F(1)],
    'appell_quadratic_discriminant': 36-4*F(25, 3) == F(8, 3),
    'walsh_identity_all_basis_vectors': all(basis_flags),
}
certificate = encode({
    'scope': 'Fixed admissible sextic preserver; failure of strict inverse positivity only.',
    'coefficient_order': 'Ascending powers; exact rational strings.',
    'q': q, 'inverse': r, 'product_mod_D7': product,
    'moments': moments, 'moment_matrix': H, 'leading_minors': minors,
    'h': h, 'f_equals_h_squared_plus_one': f, 'inverse_f': p,
    'qD_inverse_f': image, 'quadratic_form': quadratic_form,
    'appell': appell, 'walsh_coefficients': walsh_coeffs,
    'walsh_basis_checks': basis_flags,
    'actual': {'f_real_lower_bound': 1, 'inverse_f_at_zero': p[0],
               'moment_determinant': minors[-1],
               'appell_discriminant': F(8, 3)},
    'required': {'inverse_positivity': 'inverse_f_at_zero > 0 for every f strictly positive on R',
                 'main_test': 'Nonreal counts (2,4), or an impossibility proof for the whole class'},
    'main_test_status': 'UNRESOLVED; this obstruction is not a (2,4) witness.',
    'checks': checks, 'failures': [k for k, value in checks.items() if not value],
    'limits': 'Finite algebra only. See C020o for sector roots, Walsh applicability and strict positivity. No root counts for f or inverse_f are asserted here.',
})
path = Path(__file__).with_name('sector-sextic-inverse-obstruction-1470.json')
path.write_text(json.dumps(certificate, indent=2)+'\n')
print('Actual: f(x)>=1; inverse_f(0) =', certificate['actual']['inverse_f_at_zero'])
print('Required for inverse positivity: >0; this method fails.')
print('Appell discriminant:', certificate['actual']['appell_discriminant'], '(required >=0).')
print('Requested count pair (2,4): UNRESOLVED.')
print('Algebra failures:', certificate['failures'])
print('Full certificate:', path)
if certificate['failures']:
    raise SystemExit(1)
