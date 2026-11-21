"""Exact finite algebra for C020n; the analytic positivity proof is in the lemma."""
from fractions import Fraction as F
from itertools import permutations
from math import factorial
from pathlib import Path
import json


def add(p, q):
    r = dict(p)
    for k, v in q.items():
        r[k] = r.get(k, F(0)) + v
    return {k: v for k, v in r.items() if v}


def scale(p, c):
    return {k: v*c for k, v in p.items() if v*c}


def mul(p, q):
    r = {}
    for i, a in p.items():
        for j, b in q.items():
            r[i+j] = r.get(i+j, F(0)) + a*b
    return {k: v for k, v in r.items() if v}


def power(p, k):
    r = {0: F(1)}
    for _ in range(k):
        r = mul(r, p)
    return r


def evaluate(p, x):
    return sum((v*x**k for k, v in p.items()), F(0))


def encode(p):
    return [str(p.get(k, F(0))) for k in range(max(p, default=0)+1)]


# All entries are exact polynomials in t=b/a^2; a>0 is restored by
# congruence with diag(1,a,a^2), as proved in C020n.
one, t = {0: F(1)}, {1: F(1)}
r = [one, scale(one, -1), add(one, scale(t, -1)),
     add(scale(one, -1), scale(t, 2)),
     add(add(one, scale(t, -3)), power(t, 2))]
q = [one, one, t]
convolution = []
for k in range(5):
    value = {}
    for j in range(min(k, 2)+1):
        value = add(value, mul(q[j], r[k-j]))
    convolution.append(value)
moments = [scale(v, factorial(k)) for k, v in enumerate(r)]
H = [[moments[i+j] for j in range(3)] for i in range(3)]
det = {}
for perm in permutations(range(3)):
    inversions = sum(perm[i] > perm[j] for i in range(3) for j in range(i+1, 3))
    term = one
    for i in range(3):
        term = mul(term, H[i][perm[i]])
    det = add(det, scale(term, (-1)**inversions))
minor = add(moments[2], scale(mul(moments[1], moments[1]), -1))
endpoint = F(5, 18)
# Substitute t=5/18-delta, checking an identity over the whole interval.
substituted = {}
for k, v in det.items():
    substituted = add(substituted, scale(power({0: endpoint, 1: F(-1)}, k), v))
expected_det = {0: F(4), 1: F(-24), 2: F(48), 3: F(-40)}
expected_substitution = {0: F(131, 729), 1: F(178, 27),
                         2: F(44, 3), 3: F(40)}
checks = {
    'inverse_identity_mod_D5': convolution == [one, {}, {}, {}, {}],
    'leading_minor_identity': minor == {0: F(1), 1: F(-2)},
    'determinant_identity': det == expected_det,
    'endpoint_shift_identity': substituted == expected_substitution,
    'all_shifted_determinant_coefficients_positive': all(v > 0 for v in substituted.values()),
    'leading_minor_lower_bound_positive': evaluate(minor, endpoint) == F(4, 9),
    'determinant_lower_bound_positive': evaluate(det, endpoint) == F(131, 729),
    'sector_parameter_endpoint': (1+F(1, 9))/4 == endpoint,
}
certificate = {
    'scope': 'Degree at most four only; sector |Im root|<=-Re root/3; a>0.',
    'coefficient_order': 'ascending powers of t, exact rational strings',
    'inverse_coefficients': [encode(v) for v in r],
    'inverse_product_mod_D5': [encode(v) for v in convolution],
    'moments': [encode(v) for v in moments],
    'H': [[encode(v) for v in row] for row in H],
    'leading_minor': encode(minor),
    'determinant': encode(det),
    'determinant_at_t_equals_5over18_minus_delta': encode(substituted),
    'actual': {'leading_minor_lower_bound': str(evaluate(minor, endpoint)),
               'determinant_lower_bound': str(evaluate(det, endpoint)),
               'interval': '1/4<t<=5/18; delta=5/18-t>=0'},
    'required': {'leading_minor_lower_bound': '>0', 'determinant_lower_bound': '>0',
                 'witness_nonreal_counts': [2, 4],
                 'proved_count_implication': 'Z_c(p)=2 implies Z_c(q(D)p)<=2, under preservation hypothesis for full contraction'},
    'checks': checks,
    'failures': [name for name, ok in checks.items() if not ok],
    'proof_limits': 'Checks finite algebra, not factorization, sums of squares, positivity composition or the imported Walsh theorem. See C020n.',
}
path = Path(__file__).with_name('sector-inverse-certificate-1466.json')
path.write_text(json.dumps(certificate, indent=2)+'\n')
print('actual bounds:', certificate['actual'])
print('required: both principal-minor bounds >0; proposed count threshold (2,4) is excluded by the lemma')
print('failures:', certificate['failures'])
print('full certificate:', path)
if certificate['failures']:
    raise SystemExit(1)
