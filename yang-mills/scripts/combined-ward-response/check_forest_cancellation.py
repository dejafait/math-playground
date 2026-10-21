"""Exact jet/cumulant diagnostic; does not evaluate L010's box coefficient."""

from fractions import Fraction as F
from math import factorial

DIM = 6
ONE = {(0,) * DIM: F(1)}
ZERO = {}
VARIANCES = (F(1),) * DIM


def add(*polys):
    out = {}
    for poly in polys:
        for powers, value in poly.items():
            out[powers] = out.get(powers, F(0)) + value
    return {key: value for key, value in out.items() if value}


def scale(value, poly):
    return {key: value * coeff for key, coeff in poly.items() if value * coeff}


def mul(left, right):
    out = {}
    for lp, lv in left.items():
        for rp, rv in right.items():
            key = tuple(a + b for a, b in zip(lp, rp))
            out[key] = out.get(key, F(0)) + lv * rv
    return {key: value for key, value in out.items() if value}


def power(poly, exponent):
    out = ONE
    for _ in range(exponent):
        out = mul(out, poly)
    return out


def derivative(poly, index):
    out = {}
    for powers, coeff in poly.items():
        if powers[index]:
            key = list(powers)
            key[index] -= 1
            out[tuple(key)] = coeff * powers[index]
    return out


def directional(vector, poly):
    return add(*(mul(vector[j], derivative(poly, j)) for j in range(DIM)))


def divergence(vector):
    return add(*(derivative(vector[j], j) for j in range(DIM)))


def bracket(left, right):
    # [i sigma_a/2, i sigma_b/2] = -epsilon_abc i sigma_c/2.
    return [add(mul(left[k], right[j]), scale(-1, mul(left[j], right[k])))
            for j, k in ((1, 2), (2, 0), (0, 1))]


def moment(poly):
    out = F(0)
    for powers, coeff in poly.items():
        if any(exponent % 2 for exponent in powers):
            continue
        value = coeff
        for index, exponent in enumerate(powers):
            value *= VARIANCES[index] ** (exponent // 2)
            for factor in range(1, exponent, 2):
                value *= factor
        out += value
    return out


def partitions(labels):
    if not labels:
        yield []
        return
    first, *rest = labels
    for partition in partitions(rest):
        yield [(first,), *partition]
        for index, block in enumerate(partition):
            yield [*partition[:index], (first, *block), *partition[index + 1:]]


def cumulant(*polys):
    out = F(0)
    for partition in partitions(list(range(len(polys)))):
        value = F((-1) ** (len(partition) - 1) * factorial(len(partition) - 1))
        for block in partition:
            term = ONE
            for index in block:
                term = mul(term, polys[index])
            value *= moment(term)
        out += value
    return out


def groups(left, right, cubic, effective4):
    f0, f1, f2 = left
    r0, r1, r2 = right
    measure_action = (-cumulant(f0, r0, effective4)
                      + F(1, 2) * cumulant(f0, r0, cubic, cubic))
    observable = (cumulant(f2, r0) + cumulant(f1, r1) + cumulant(f0, r2)
                  - cumulant(f1, r0, cubic) - cumulant(f0, r1, cubic))
    return measure_action, observable


def series_mul(left, right):
    return [add(*(mul(left[j], right[n - j]) for j in range(n + 1)))
            for n in range(3)]


def mean_series(observable, density):
    numerator = list(map(moment, series_mul(observable, density)))
    denominator = list(map(moment, density))
    out = []
    for n in range(3):
        out.append((numerator[n] - sum(denominator[j] * out[n - j]
                                      for j in range(1, n + 1))) / denominator[0])
    return out


def direct_covariance(left, right, cubic, effective4):
    density = [ONE, scale(-1, cubic),
               add(scale(F(1, 2), power(cubic, 2)), scale(-1, effective4))]
    mixed = mean_series(series_mul(left, right), density)
    first = mean_series(left, density)
    second = mean_series(right, density)
    return [mixed[n] - sum(first[j] * second[n - j] for j in range(n + 1))
            for n in range(3)]


variables = [{tuple(int(j == k) for j in range(DIM)): F(1)} for k in range(DIM)]
u, v = variables[:3], variables[3:]
u2 = add(*(power(value, 2) for value in u))
v2 = add(*(power(value, 2) for value in v))
radius2 = add(u2, v2)
S2 = scale(F(1, 2), radius2)
M2 = scale(F(1, 12), radius2)
M2prime = scale(F(1, 12), add(u2, *(power(add(a, b), 2) for a, b in zip(u, v))))
uv = bracket(u, v)
q = [ZERO] * 3 + [scale(F(1, 2), value) for value in uv]
uuv, vvu = bracket(u, uv), bracket(v, bracket(v, u))
c = [ZERO] * 3 + [scale(F(1, 12), add(a, b)) for a, b in zip(uuv, vvu)]
p = [add(c[j], scale(-F(1, 2), directional(q, q[j]))) for j in range(DIM)]
L = lambda poly: directional(q, poly)
P = lambda poly: directional(p, poly)
assert divergence(q) == ZERO
assert divergence(p) == add(M2prime, scale(-1, M2))
W = L(S2)
Z = add(P(S2), scale(-1, divergence(p)))
assert W == ZERO  # Specific isotropic diagnostic, not the box Hessian.


def transform_jets(jets):
    f0, f1, f2 = jets
    return [f0, add(f1, scale(-1, L(f0))),
            add(f2, scale(-1, L(f1)), scale(F(1, 2), L(L(f0))), scale(-1, P(f0)))]


def test_case(label, left, right, S3, S4):
    E = add(S4, M2)
    changed_left, changed_right = transform_jets(left), transform_jets(right)
    changed_S3 = add(S3, scale(-1, W))
    changed_S4 = add(S4, scale(-1, L(S3)), scale(F(1, 2), L(W)), scale(-1, P(S2)))
    changed_E = add(changed_S4, M2prime)
    before = groups(left, right, S3, E)
    after = groups(changed_left, changed_right, changed_S3, changed_E)
    f0, r0 = left[0], right[0]
    predicted = (-cumulant(L(f0), r0, S3) - cumulant(f0, L(r0), S3)
                 + F(1, 2) * cumulant(L(L(f0)), r0) + cumulant(L(f0), L(r0))
                 + F(1, 2) * cumulant(f0, L(L(r0)))
                 + cumulant(P(f0), r0) + cumulant(f0, P(r0)))
    assert after[0] - before[0] == predicted
    assert after[1] - before[1] == -predicted
    assert sum(before) == sum(after)
    direct_before = direct_covariance(left, right, S3, E)
    direct_after = direct_covariance(changed_left, changed_right, changed_S3, changed_E)
    assert direct_before == direct_after
    assert direct_before[2] == sum(before)
    for vec, score in ((q, W), (p, Z)):
        deriv = lambda poly: directional(vec, poly)
        assert cumulant(f0, r0, score) == cumulant(deriv(f0), r0) + cumulant(f0, deriv(r0))
    haar_change = -cumulant(f0, r0, add(M2prime, scale(-1, M2)))
    print(f"{label}: action/measure {before[0]} -> {after[0]}; "
          f"observable {before[1]} -> {after[1]}; full {sum(before)}; "
          f"Haar-only change {haar_change}.")
    return predicted


f0 = power(add(u[0], scale(2, v[0])), 2)
r0 = power(v[0], 2)
minimal = test_case("quadratic jets", [f0, ZERO, ZERO], [r0, ZERO, ZERO], ZERO, ZERO)
assert minimal != 0
populated = test_case(
    "populated jets",
    [f0, mul(u[0], power(v[1], 2)), scale(F(1, 7), power(v[0], 4))],
    [r0, mul(v[0], power(u[1], 2)), scale(F(1, 5), mul(u2, v2))],
    add(scale(F(1, 6), mul(u[0], power(v[0], 2))), mul(mul(u[1], v[0]), v[2])),
    scale(F(1, 96), power(radius2, 2)))
assert populated != 0
# Repeat with a nonisotropic Gaussian: the cubic action also changes.
VARIANCES = tuple(F(j + 1) for j in range(DIM))
S2 = add(*(scale(F(1, 2) / variance, power(value, 2))
           for value, variance in zip(variables, VARIANCES)))
W = L(S2)
Z = add(P(S2), scale(-1, divergence(p)))
assert W != ZERO
anisotropic = test_case(
    "nonisotropic populated jets",
    [f0, mul(u[0], power(v[1], 2)), scale(F(1, 7), power(v[0], 4))],
    [r0, mul(v[0], power(u[1], 2)), scale(F(1, 5), mul(u2, v2))],
    add(scale(F(1, 6), mul(u[0], power(v[0], 2))), mul(mul(u[1], v[0]), v[2])),
    scale(F(1, 96), power(radius2, 2)))
assert anisotropic != 0
print("Exact Haar/BCH divergence, connected integration by parts, and normalized moments agree.")
print("The partial group changes: this diagnostic is not the original box/probe contraction or a cutoff estimate.")
