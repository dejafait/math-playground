#!/usr/bin/env python3
"""Exact six-parameter algebra for L401; no analytic or RH verification.
Polynomial/kernel routines reused from check_wronskian_weight.py."""
from fractions import Fraction as F
from itertools import combinations, permutations
from math import factorial
from pathlib import Path
import json


def add(a, b):
    out = dict(a)
    for key, value in b.items():
        out[key] = out.get(key, F(0)) + value
    return {key: value for key, value in out.items() if value}


def scale(a, value):
    return {key: coefficient * value for key, coefficient in a.items()
            if coefficient * value}


def mul(a, b):
    out = {}
    for m, x in a.items():
        for n, y in b.items():
            key = tuple(i + j for i, j in zip(m, n))
            out[key] = out.get(key, F(0)) + x * y
    return {key: value for key, value in out.items() if value}


def power(a, n):
    assert a
    out = {(0,) * len(next(iter(a))): F(1)}
    for _ in range(n):
        out = mul(out, a)
    return out


def variables(count):
    return [{tuple(int(i == j) for i in range(count)): F(1)}
            for j in range(count)]


def divide(a, b):
    remainder, quotient = dict(a), {}
    leading = max(b)
    while remainder:
        term = max(remainder)
        assert all(i >= j for i, j in zip(term, leading))
        exponent = tuple(i - j for i, j in zip(term, leading))
        value = remainder[term] / b[leading]
        quotient[exponent] = quotient.get(exponent, F(0)) + value
        remainder = add(remainder, scale(mul({exponent: value}, b), -1))
    assert mul(quotient, b) == a
    return quotient


def cmul(a, b):
    return (add(mul(a[0], b[0]), scale(mul(a[1], b[1]), -1)),
            add(mul(a[0], b[1]), mul(a[1], b[0])))


def real_product(a, b):
    return add(mul(a[0], b[0]), scale(mul(a[1], b[1]), -1))


def serialized(poly):
    return [{"powers": list(key), "coefficient": str(value)}
            for key, value in sorted(poly.items(), reverse=True)]


u = variables(4)
vandermonde = {(0, 0, 0, 0): F(1)}
for i, j in combinations(range(4), 2):
    vandermonde = mul(vandermonde, add(u[i], scale(u[j], -1)))
terms = []
for chosen in combinations(range(4), 2):
    cross = {(0, 0, 0, 0): F(1)}
    centered = {}
    for i in range(4):
        centered = add(centered, scale(u[i], F(1, 2) if i in chosen else F(-1, 2)))
    for i in chosen:
        for j in range(4):
            if j not in chosen:
                cross = mul(cross, add(u[i], scale(u[j], -1)))
    terms.append((divide(vandermonde, cross), centered))
kernel, divisions = {}, []
for n in range(13):
    numerator = {}
    for within, centered in terms:
        numerator = add(numerator, mul(within, power(centered, n)))
    quotient = divide(numerator, vandermonde) if numerator else {}
    if n < 4 or n % 2:
        assert not quotient
    else:
        kernel.update(scale(quotient, F((-1) ** (n // 2), factorial(n))))
    divisions.append({"exponential_degree": n, "exact_division": True,
                      "zero_quotient": not quotient})
for orders, value in kernel.items():
    for permuted in set(permutations(orders)):
        assert kernel.get(permuted, F(0)) == value


x, y, z, a, h, *params = variables(11)
u, v = params[:3], params[3:]
jets = [x, y, z]
A, B = {}, {}
for ui, vi, jet in zip(u, v, jets):
    A = add(A, mul(ui, jet))
    B = add(B, mul(vi, jet))
M = add(add(scale(power(z, 2), F(1, 2)), scale(mul(x, z), F(3, 4))),
        add(scale(power(x, 2), F(1, 32)), scale(power(y, 2), F(-1, 2))))
b = add(z, scale(x, F(-1, 4)))
K = (scale(add(power(b, 2), scale(power(y, 2), -1)), F(1, 2)),
     scale(mul(b, y), -1))
V = scale(add(power(A, 2), power(B, 2)), F(1, 2))
J = (scale(add(power(A, 2), scale(power(B, 2), -1)), F(1, 2)),
     scale(mul(A, B), -1))
P = add(mul(M, V), scale(add(mul(K[0], J[0]), mul(K[1], J[1])), F(1, 2)))
P1 = (add(mul(M, J[0]), mul(V, K[0])),
      add(mul(M, J[1]), mul(V, K[1])))
P2 = tuple(scale(part, F(1, 2)) for part in cmul(K, J))
r = add(power(a, 2), power(h, 2))
q = (add(power(a, 2), scale(power(h, 2), -1)), scale(mul(a, h), 2))
weight_direct = power(add(mul(a, A), mul(h, B)), 2)
weight_harmonics = add(mul(V, r), real_product(J, q))
direct = mul(add(mul(M, r), real_product(K, q)), weight_direct)
harmonics = add(mul(P, power(r, 2)),
                add(mul(real_product(P1, q), r), real_product(P2, cmul(q, q))))
S = add(scale(M, F(1, 2)), scale(K[0], F(1, 4)))
T = add(scale(M, F(1, 2)), scale(K[0], F(-1, 4)))
P_formula = add(add(mul(S, power(A, 2)), mul(T, power(B, 2))),
                scale(mul(mul(b, y), mul(A, B)), F(1, 2)))
residuals = [add(weight_direct, scale(weight_harmonics, -1)),
             add(direct, scale(harmonics, -1)),
             add(P, scale(P_formula, -1))]
assert all(not r for r in residuals)

coefficient = {}
table = []
for exponents, factor in sorted(P.items(), reverse=True):
    nx, ny, nz, na, nh, *param_powers = exponents
    assert nx + ny + nz == 4 and na == nh == 0 and sum(param_powers) == 2
    orders = (0,) * nx + (1,) * ny + (2,) * nz
    moment = kernel.get(orders, F(0))
    for order in orders:
        moment *= factorial(order)
    contribution = factor * moment
    key = tuple(param_powers)
    coefficient[key] = coefficient.get(key, F(0)) + contribution
    table.append({'powers_xyz': list(exponents[:3]), 'parameter_powers': param_powers,
                  'factor': str(factor), 'orders': list(orders),
                  'moment': str(moment), 'contribution': str(contribution)})
coefficient = {k: val for k, val in coefficient.items() if val}
C = [[F(0) for _ in range(6)] for _ in range(6)]
for powers, value in coefficient.items():
    selected = [i for i, degree in enumerate(powers) for _ in range(degree)]
    i, j = selected
    C[i][j] = C[j][i] = value if i == j else value / 2
# Reconstruct the coefficient from the complete symmetric matrix.
reconstructed = {}
for i in range(6):
    for j in range(6):
        powers = tuple(int(k == i) + int(k == j) for k in range(6))
        reconstructed[powers] = reconstructed.get(powers, F(0)) + C[i][j]
assert {k: val for k, val in reconstructed.items() if val} == coefficient

# Exact scalar LDL^T, with block ordering selected by parity, no floating point.
permutation = [0, 2, 4, 3, 5, 1]
Cp = [[C[i][j] for j in permutation] for i in permutation]
assert all(Cp[i][j] == 0 for i in range(3) for j in range(3, 6))
Lmat = [[F(int(i == j)) for j in range(6)] for i in range(6)]
pivots = []
for j in range(6):
    pivot = Cp[j][j] - sum(Lmat[j][k] ** 2 * pivots[k] for k in range(j))
    assert pivot != 0
    pivots.append(pivot)
    for i in range(j + 1, 6):
        Lmat[i][j] = (Cp[i][j] - sum(Lmat[i][k] * Lmat[j][k] * pivots[k]
                                   for k in range(j))) / pivot
rebuilt = [[sum(Lmat[i][k] * pivots[k] * Lmat[j][k] for k in range(6))
            for j in range(6)] for i in range(6)]
assert rebuilt == Cp
inertia = {'positive': sum(p > 0 for p in pivots),
           'negative': sum(p < 0 for p in pivots), 'zero': 0}
# L400 is the subdirection u=(0,1,0),v=(1/2,0,0), apart from its c in the weight.
w = [F(0), F(1), F(0), F(1,2), F(0), F(0)]
qW = sum(w[i] * C[i][j] * w[j] for i in range(6) for j in range(6))
assert qW == F(-281,604800)
# Extract a rational positive witness if LDL has a positive pivot.
witness = None
for j, pivot in enumerate(pivots):
    if pivot > 0:
        target = [F(int(k == j)) for k in range(6)]
        perm_vector = [F(0) for _ in range(6)]
        for i in reversed(range(6)):
            perm_vector[i] = target[i] - sum(Lmat[k][i] * perm_vector[k] for k in range(i + 1, 6))
        vector = [F(0) for _ in range(6)]
        for i, original in enumerate(permutation):
            vector[original] = perm_vector[i]
        value = sum(vector[i] * C[i][k] * vector[k] for i in range(6) for k in range(6))
        assert value == pivot and value > 0
        witness = {'vector': [str(t) for t in vector], 'value': str(value)}
        break
report = {
    'kind': 'exact_finite_algebra_only', 'analytic_claim_verified': False,
    'failures': [], 'variables': ['x','y','z','a','h','u0','u1','u2','v0','v1','v2'],
    'residuals': [serialized(r) for r in residuals],
    'balanced_polynomial': serialized(P),
    'k1_polynomial': {'real': serialized(P1[0]), 'imaginary': serialized(P1[1])},
    'k2_polynomial': {'real': serialized(P2[0]), 'imaginary': serialized(P2[1])},
    'complete_moment_table': table, 'coefficient_polynomial': serialized(coefficient),
    'matrix': [[str(value) for value in row] for row in C],
    'ldlt': {'permutation': permutation, 'L': [[str(t) for t in row] for row in Lmat],
             'pivots': [str(t) for t in pivots], 'identity_residual': [[str(rebuilt[i][j]-Cp[i][j]) for j in range(6)] for i in range(6)]},
    'inertia': inertia, 'positive_witness': witness, 'L400_check': str(qW),
    'division_checks': divisions, 'permutation_symmetry': True,
    'kernel_coefficients': serialized(kernel),
    'required_bound': 'some fixed u,v has q(u,v)>0 with complete error o(log^4 H)',
    'actual_bound': f'inertia={inertia}; analytic obligations in L401',
}
destination = Path(__file__).with_name('response-linear-family-certificate.json')
destination.write_text(json.dumps(report, indent=2) + '\n')
print('RESULT: full parameter polynomial identities and LDL identity exact; failures=0')
print(f'ACTUAL: inertia={inertia}; positive_witness={witness}')
print('REQUIRED: a strictly positive complete coefficient with o(log^4 H) error')
print(f'CERTIFICATE: {destination}')
print('LIMITATION: finite algebra only; analytic asymptotic and RH not verified')
