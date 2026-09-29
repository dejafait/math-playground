"""Exact arithmetic checks for L011, not a four-dimensional cutoff calculation."""

from fractions import Fraction as F
from math import factorial


ZERO = {}
ONE = {(0, 0, 0): F(1)}


def add(*polys):
    result = {}
    for poly in polys:
        for powers, value in poly.items():
            result[powers] = result.get(powers, F(0)) + value
    return {powers: value for powers, value in result.items() if value}


def scale(value, poly):
    return {powers: value * coeff for powers, coeff in poly.items() if value * coeff}


def mul(left, right):
    result = {}
    for lp, lv in left.items():
        for rp, rv in right.items():
            powers = tuple(a + b for a, b in zip(lp, rp))
            result[powers] = result.get(powers, F(0)) + lv * rv
    return {powers: value for powers, value in result.items() if value}


def power(poly, exponent):
    result = ONE
    for _ in range(exponent):
        result = mul(result, poly)
    return result


def moment(poly):
    result = F(0)
    for powers, coeff in poly.items():
        value = coeff
        for exponent in powers:
            if exponent % 2:
                value = F(0)
                break
            for factor in range(1, exponent, 2):
                value *= factor
        result += value
    return result


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
    result = F(0)
    for partition in partitions(list(range(len(polys)))):
        term = F((-1) ** (len(partition) - 1) * factorial(len(partition) - 1))
        for block in partition:
            block_poly = ONE
            for index in block:
                block_poly = mul(block_poly, polys[index])
            term *= moment(block_poly)
        result += term
    return result


def series_mul(left, right):
    return [add(*(mul(left[j], right[n - j]) for j in range(n + 1)))
            for n in range(3)]


def normalized_mean(observable, density):
    # Independent division of the integrated numerator by the partition series.
    numerator = list(map(moment, series_mul(observable, density)))
    denominator = list(map(moment, density))
    result = []
    for order in range(3):
        lower = sum(denominator[k] * result[order - k] for k in range(1, order + 1))
        result.append((numerator[order] - lower) / denominator[0])
    return result


def covariance_series(left, right, cubic, quartic, haar):
    density = [ONE, scale(-1, cubic),
               add(scale(F(1, 2), power(cubic, 2)), scale(-1, quartic), scale(-1, haar))]
    mixed = normalized_mean(series_mul(left, right), density)
    first = normalized_mean(left, density)
    second = normalized_mean(right, density)
    return [mixed[n] - sum(first[j] * second[n - j] for j in range(n + 1))
            for n in range(3)]


def coefficient(left, right, cubic, quartic, haar):
    f0, f1, f2 = left
    r0, r1, r2 = right
    return (cumulant(f2, r0) + cumulant(f1, r1) + cumulant(f0, r2)
            - cumulant(f1, r0, cubic) - cumulant(f0, r1, cubic)
            - cumulant(f0, r0, add(quartic, haar))
            + F(1, 2) * cumulant(f0, r0, cubic, cubic))


x, y, z = ({tuple(int(j == k) for j in range(3)): F(1)} for k in range(3))
x2, y2, z2 = (power(var, 2) for var in (x, y, z))
radius2 = add(x2, y2, z2)
radius4 = power(radius2, 2)
haar = scale(F(1, 12), radius2)

# Nonzero cubic terms test the four-cumulant and both cubic insertion terms.
left = [add(x2, scale(F(1, 2), y2)),
        add(power(x, 3), scale(F(1, 3), mul(mul(x, y), z))),
        add(scale(F(1, 4), power(x, 4)), scale(F(1, 5), mul(y2, z2)))]
right = [add(scale(2, x2), mul(y, z), z2),
         add(scale(F(1, 5), power(x, 3)), scale(F(1, 2), power(y, 3)), mul(x2, z)),
         add(scale(F(1, 7), power(z, 4)), scale(F(1, 3), mul(x2, y2)))]
cubic = add(scale(F(1, 6), power(x, 3)), scale(F(1, 2), mul(x, y2)),
            scale(F(1, 4), mul(mul(x, y), z)))
quartic = add(scale(F(1, 24), power(x, 4)), scale(F(1, 12), power(y, 4)),
              scale(F(1, 8), power(z, 4)))

direct = covariance_series(left, right, cubic, quartic, haar)
combined = coefficient(left, right, cubic, quartic, haar)
assert direct[0] == cumulant(left[0], right[0])
assert direct[1] == 0
assert direct[2] == combined
assert combined != coefficient(left, right, ZERO, quartic, haar)
assert combined != coefficient(left, right, cubic, quartic, ZERO)
print(f"Connected cubic/quartic expansion agrees with normalized moments: {combined}.")

# An independent radial SU(2) example uses S = 4(1-cos(r/2)), V = grad S,
# J = S, and flow dr/dt = -2 sin(r/2). This is a normalization check only.
# At exp(-t)=q, tan(r_t/4)=q tan(r/4), so the exact flowed numerator is
# 8 q^2 tan(r/4)^2 / (1 + q^2 tan(r/4)^2).
q = F(1, 2)
flow_quartic = q*q / 48 - q**4 / 32
# The same coefficient from the cubic flow jet r_t = q r + q(1-q^2)r^3/48.
assert flow_quartic == q*q*(1-q*q)/48 - q**4/96
# Haar: (sin(r/2)/(r/2))^2 = 1 - r^2/12 + O(r^4).
assert 2 * (-F(1, 24)) == -F(1, 12)

action4 = scale(-F(1, 96), radius4)
probe = [scale(q*q/2, radius2), ZERO, scale(flow_quartic, radius4)]
insertion = [scale(F(1, 2), radius2), ZERO, action4]
remaining = [scale(F(1, 2), radius2), ZERO, scale(-F(7, 96), radius4)]
gamma = coefficient(probe, remaining, ZERO, action4, haar)
assert gamma == covariance_series(probe, remaining, ZERO, action4, haar)[2]

# div_H grad S = 3 cos(r/2); its constant has no connected contribution.
gamma_haar_divergence = cumulant(probe[0], scale(F(3, 8), radius2))
ward0 = scale(q*q, radius2)
ward2 = scale(4*flow_quartic - q*q/24, radius4)
ward_coefficient = moment(ward2) - cumulant(ward0, add(action4, haar))
insertion_coefficient = coefficient(probe, insertion, ZERO, action4, haar)
assert ward_coefficient - insertion_coefficient == gamma + gamma_haar_divergence

linear_flow_probe = [probe[0], ZERO, scale(-q**4/96, radius4)]
assert gamma != coefficient(linear_flow_probe, remaining, ZERO, action4, haar)
assert gamma != coefficient(probe, remaining, ZERO, action4, ZERO)
print(f"Radial SU(2): remaining coefficient {gamma}; divergence contribution {gamma_haar_divergence}.")
print("Nonlinear flow and coordinate Haar terms are both detected; Ward sign agrees exactly.")
print("These checks do not evaluate L010's box response or its cutoff logarithm.")
