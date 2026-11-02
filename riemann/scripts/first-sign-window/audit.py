#!/usr/bin/env python3
"""Exact rational normalization check for the approved p=1, d<=1 audit.

No numerical zeta evaluation. Check the finite six-term Taylor identity
against polynomial division and the two elementary kernel integrals.
Run from the notebook: python3 scripts/first-sign-window/audit.py
"""
from fractions import Fraction as F
from itertools import combinations
from math import factorial
from pathlib import Path
import json

ZERO = (0, 0, 0, 0)


def add(a, b):
    out = a.copy()
    for m, c in b.items():
        out[m] = out.get(m, F(0)) + c
        if not out[m]:
            del out[m]
    return out


def scale(a, c):
    return {m: v*c for m, v in a.items() if v*c}


def mul(a, b):
    out = {}
    for m, c in a.items():
        for n, d in b.items():
            k = tuple(x+y for x, y in zip(m, n))
            out[k] = out.get(k, F(0)) + c*d
    return {m: c for m, c in out.items() if c}


def power(a, n):
    out = {ZERO: F(1)}
    for _ in range(n):
        out = mul(out, a)
    return out


def divexact(a, b):
    rem, quot = a.copy(), {}
    lm = max(b)
    while rem:
        top = max(rem)
        if any(x < y for x, y in zip(top, lm)):
            raise AssertionError(('nonzero division remainder', rem))
        mon = tuple(x-y for x, y in zip(top, lm))
        term = {mon: rem[top]/b[lm]}
        quot = add(quot, term)
        rem = add(rem, scale(mul(term, b), -1))
    assert mul(quot, b) == a
    return quot


def derivative_at_zero(poly, orders):
    value = poly.get(tuple(orders), F(0))
    for k in orders:
        value *= factorial(k)
    return value


def rational_poly(poly):
    return [{'powers': list(m), 'coefficient': str(c)}
            for m, c in sorted(poly.items())]


r = []
for j in range(4):
    e = list(ZERO)
    e[j] = 1
    r.append({tuple(e): F(1)})
delta = {ZERO: F(1)}
for j, k in combinations(range(4), 2):
    delta = mul(delta, add(r[j], scale(r[k], -1)))

subsets = []
for ss in combinations(range(4), 2):
    complement = tuple(j for j in range(4) if j not in ss)
    u, denominator = {}, {ZERO: F(1)}
    for j in range(4):
        u = add(u, scale(r[j], 1 if j in ss else -1))
    for j in ss:
        for k in complement:
            denominator = mul(denominator, add(r[j], scale(r[k], -1)))
    subsets.append((ss, u, divexact(delta, denominator)))

# H(r)=sum exp(U_S/2)/D_S. Multiplication by Delta cancels all
# denominators. Its terms of numerator degree <6 must vanish.
jets, evidence = {}, []
for n in range(9):
    numerator = {}
    for ss, u, quotient in subsets:
        numerator = add(numerator, mul(quotient, power(u, n)))
    numerator = scale(numerator, F(1, 2**n*factorial(n)))
    if n < 4:
        assert not numerator
        q = {}
    else:
        q = divexact(numerator, delta)
        jets[n-4] = q
        assert all(sum(m) == n-4 for m in q)
    evidence.append({'exponential_degree': n,
                     'numerator': rational_poly(numerator),
                     'quotient': rational_poly(q),
                     'identity_checked': True})

assert not jets[1] and not jets[3]
# G(a)=6/pi^2 H(i a). Store pi^2-scaled differential coefficients.
def coefficient(j, k):
    total_degree = 2+j+k
    terms = [((1, 1, j, k), F(1)),
             ((2, 0, j, k), F(-1, 2)),
             ((0, 2, j, k), F(-1, 2))]
    if total_degree % 2:
        assert not jets[total_degree]
        return F(0)
    return 6*((-1)**(total_degree//2))*sum(
        c*derivative_at_zero(jets[total_degree], orders)
        for orders, c in terms)

b00 = coefficient(0, 0)
b01 = coefficient(0, 1)+coefficient(1, 0)
b11 = coefficient(1, 1)

# u=x-y, v=x+y; Jacobian 1/2. Evenness in u leaves u in [0,1]
# and v in [-(1-u),1-u]. Integrate the v monomials exactly.
def beta_integral(a, b):
    return F(factorial(a)*factorial(b), factorial(a+b+1))

i00 = F(8, 5)*beta_integral(0, 5)
i11 = F(2, 21)*beta_integral(0, 7)-F(2, 5)*beta_integral(2, 5)
assert (i00, i11) == (F(4, 15), F(1, 105))
assert (b00, b01, b11) == (i00/8, F(0), i11/8)
assert (b00, b01, b11) == (F(1, 30), F(0), F(1, 840))

certificate = {
    'task': 'p=1, degree<=1 six-term normalization audit',
    'arithmetic': 'exact rational polynomial identities, not numerical evidence',
    'definitions': {'Delta': 'product_(j<k)(r_j-r_k)',
                    'U_S': 'sum_(j in S)r_j-sum_(j not in S)r_j',
                    'D_S': 'product_(j in S,k not in S)(r_j-r_k)',
                    'H': 'sum_(|S|=2) exp(U_S/2)/D_S',
                    'G': '6/pi^2 H(i*a)'},
    'six_terms': [{'subset': list(ss), 'U_S': rational_poly(u),
                   'Delta_over_D_S': rational_poly(q)} for ss, u, q in subsets],
    'taylor_identity_evidence': evidence,
    'B1_pi_squared': {'c0_squared': str(b00), 'c0_c1': str(b01),
                      'c1_squared': str(b11)},
    'kernel_integrals': {'I00': str(i00), 'I11': str(i11)},
    'actual_relative_coercivity': 'B1 >= (c0^2+c1^2)/(840*pi^2)',
    'required_relative_coercivity': 'fixed positive multiple of c0^2+c1^2',
    'scope_limits': ['No proof of Hughes-Young arithmetic',
                     'No numerical or effective onset',
                     'Analytic uniformity and completion proved in L619'],
    'failures': [],
    'passed': True,
}
out = Path(__file__).with_name('certificate.json')
out.write_text(json.dumps(certificate, indent=2)+'\n')
print('PASS: exact six-term identities through exponential degree 8; all remainders zero.')
print('Actual pi^2 B1 = c0^2/30 + c1^2/840; required: positive coefficient-uniform form.')
print('Kernel integrals match; failures: none.')
print('Certificate:', out.relative_to(Path.cwd()) if out.is_absolute() else out)
