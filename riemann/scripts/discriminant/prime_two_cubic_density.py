#!/usr/bin/env python3
"""Exact algebra checks for L433; the written proof justifies infinite sums."""
from fractions import Fraction as F
from pathlib import Path
import json

# Laurent polynomials over Q, represented by degree -> coefficient.
def add(*ps):
    out = {}
    for p in ps:
        for k, v in p.items():
            out[k] = out.get(k, F(0)) + v
    return {k: v for k, v in out.items() if v}

def scale(p, c):
    return {k: c*v for k, v in p.items() if c*v}

def mul(*ps):
    out = {0: F(1)}
    for p in ps:
        new = {}
        for k, v in out.items():
            for j, w in p.items():
                new[k+j] = new.get(k+j, F(0)) + v*w
        out = {k: v for k, v in new.items() if v}
    return out

def power(p, n):
    return mul(*([p]*n))

def reflect(p):
    # u -> 2/u, the circle conjugation when |u|=sqrt(2).
    return {-k: v*F(2)**k for k, v in p.items()}

def serial(p):
    return {str(k): str(v) for k, v in sorted(p.items())}

u = {1: F(1)}
one = {0: F(1)}
f1, f2, f4, f8 = (add(u, scale(one, -1)),
    add(u, scale(one, -2)), add(scale(u, 4), scale(one, -1)),
    add(scale(u, -1), scale(one, 8)))
# Cleared numerator for u/(u-1)+u/(2-u)+u/(2-u)^2.
geometric = add(mul(u, power(f2, 2)), scale(mul(u, f1, f2), -1),
                mul(u, f1), scale(u, -1))
num = scale(power(u, 3), 128)
den = mul(f1, power(f2, 2), power(f4, 2), f8)
X = scale(add(u, reflect(u)), F(1, 2))
a = add(scale(one, 3), scale(X, -2))
b = add(scale(one, 33), scale(X, -8))
P = scale(add(scale(one, 9), scale(X, -5)), 128)
D = mul(power(a, 2), power(b, 2))
left = mul(add(mul(num, reflect(den)), mul(reflect(num), den)), D)
right = scale(mul(P, den, reflect(den)), 2)
realpart = add(left, scale(right, -1))

# Independent exact evaluation of the two transition tails in L432 (12).
def B(j):
    x, y, z, d0 = F(1,4), F(1,8), F(1,8), F(31,32)
    lo, m = max(0, -j), max(1, j)
    s0 = z**lo/(1-z)
    s1 = z**lo*(F(lo)/(1-z)+z/(1-z)**2)
    s2 = z**lo*(F(lo*lo)/(1-z)+2*lo*z/(1-z)**2+z*(1+z)/(1-z)**3)
    result = sum((x**d*(1+d0*d) for d in range(lo)), F(0))
    result += F(2)**(-j)*((1+F(j,2))*s0+(d0*(1+F(j,2))+F(1,2))*s1+d0*s2/2)
    result += sum((y**h*F(2)**(h-j)*(1+F(j-h,2)) for h in range(1,m)), F(0))
    result += y**m/(1-y)
    return result/d0**2

# Rational multiplier of sqrt(2) for odd j, rational value for even j.
expected = [F(1), F(1161,1786), F(3504,4465), F(52201,114304), F(594309,1143040)]
actual = []
for j in range(5):
    n = j//2
    plus = F(2)**n
    minus = F(2)**(-n-(j%2))
    actual.append((plus*B(j)+minus*B(-j))/(2*B(0)))
checks = {
    'geometric_identity_zero': not geometric,
    'circle_realpart_cleared_identity_zero': not realpart,
    'B0_matches': B(0) == F(571520,329623),
    'audited_prefix_matches': actual == expected,
    'B0_less_than_two': B(0) < 2,
    'sqrt2_less_than_three_halves_squared': F(2) < F(9,4),
    'denominator_one_strict_positive_squared': 9 > 8,
    'denominator_two_strict_positive_squared': 33**2 > 8**2*2,
    'uniform_lower_bound_exact': F(128)*F(3,2)/(2*6**2*45**2) == F(8,6075),
}
failures = [k for k,v in checks.items() if not v]
certificate = {
    'scope': 'Exact finite algebra only; convergence and physical transfer are proved in L433.',
    'checks': checks, 'failures': failures,
    'geometric_residual': serial(geometric),
    'circle_identity_residual': serial(realpart),
    'Q_numerator': serial(num), 'Q_denominator': serial(den),
    'realpart_numerator': serial(P), 'realpart_denominator': serial(D),
    'B0': str(B(0)),
    'prefix_rational_multipliers': [str(v) for v in actual],
    'prefix_expected': [str(v) for v in expected],
    'prefix_sqrt2_power': [j%2 for j in range(5)],
    'global_density_bound': {'proved_strict_lower': '8/6075', 'required_lower': '0'},
}
path = Path(__file__).with_name('prime_two_cubic_density_certificate.json')
path.write_text(json.dumps(certificate, indent=2)+'\n')
print(f'Exact checks: {sum(checks.values())}/{len(checks)}; failures={failures}')
print('Density bound: >8/6075; required: >=0. No increased Toeplitz cutoff.')
print(f'Full certificate: {path}')
if failures:
    raise SystemExit(1)
