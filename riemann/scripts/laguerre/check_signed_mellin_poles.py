#!/usr/bin/env python3
"""Exact local correlation and centered grouping checks for L353.

Rational toy Euler parameters are used, not the actual sampled heights.
These checks do not prove the infinite Euler product or a bound for D_N^w.
"""

from collections import defaultdict
from fractions import Fraction as F
from itertools import product


def local_coefficients(t, q, degree, squared):
    """Expand the rational function using its denominator recurrence."""
    denominator = [F(1), -t]
    numerator = [F(1), -q]
    if squared:
        denominator = [F(1), -2 * t, t * t]
        numerator = [F(1), -2 * q, q * q]
    values = []
    for j in range(degree + 1):
        value = numerator[j] if j < len(numerator) else F(0)
        value -= sum(denominator[k] * values[j - k]
                     for k in range(1, min(j, len(denominator) - 1) + 1))
        values.append(value)
    return values


def residue_correlation(t, q, k, squared):
    """Coefficient of X^k in A(X)A(1/X) via residues at 0 and t.

    A(X)=(1-qX)^m/(1-tX)^m, m=1 or 2. The first term is the
    Taylor coefficient of the rational product at zero (inside |X|<t),
    while the second is the residue at t. Their sum is the Laurent
    coefficient on t<|X|<1/t. This is independent of the geometric-sum
    formula being tested.
    """
    forward = local_coefficients(t, q, k, squared)
    # A(1/X)=(q/t)^m (1-X/q)^m/(1-X/t)^m near zero.
    reverse = local_coefficients(1 / t, 1 / q, k, squared)
    power = 2 if squared else 1
    at_zero = (q / t) ** power * sum(
        forward[j] * reverse[k - j] for j in range(k + 1))
    if squared:
        regular = (t ** (-k - 1) * (1 - q * t) ** 2
                   * (t - q) ** 2 / (1 - t * t) ** 2)
        log_derivative = (F(-k - 1) / t - 2 * q / (1 - q * t)
                          + 2 / (t - q) + 2 * t / (1 - t * t))
        at_t = regular * log_derivative
    else:
        at_t = t ** (-k - 1) * (1 - q * t) * (t - q) / (1 - t * t)
    return at_zero + at_t


def displayed_correlations(t, q, k):
    x, z = q / t, t * t
    a, b = 1 - x * x, (1 - x) ** 2
    s0 = z / (1 - z)
    s1 = z / (1 - z) ** 2
    s2 = z * (1 + z) / (1 - z) ** 3
    if k == 0:
        joint = 1 + a * a * s0 + 2 * a * b * s1 + b * b * s2
        single = (1 - 2 * t * q + q * q) / (1 - t * t)
    else:
        joint = t ** k * ((a + k * b) + a * (a + k * b) * s0
                          + b * (2 * a + k * b) * s1 + b * b * s2)
        single = (t - q) * t ** (k - 1) * (1 - t * q) / (1 - t * t)
    return joint, single


def combine(left, right, sign=1):
    out = defaultdict(F)
    for x, a in left.items():
        for y, b in right.items():
            out[tuple(u + sign * v for u, v in zip(x, y))] += a * b
    return {key: value for key, value in out.items() if value}


def centered(polynomial):
    out = dict(polynomial)
    out[(0, 0)] = out.get((0, 0), F(0)) - 1
    return {key: value for key, value in out.items() if value}


def tensor_coefficients(parameters):
    local = [local_coefficients(t, q, 2, False) for t, q in parameters]
    return {(j, k): local[0][j] * local[1][k]
            for j, k in product(range(3), repeat=2)}


def main():
    parameters = [(F(1, 2), F(1, 4)), (F(2, 3), F(1, 3)),
                  (F(3, 5), F(2, 5)), (F(4, 5), F(1, 5)),
                  (F(2, 5), F(1, 7))]
    residue_checks = 0
    for t, q in parameters:
        for k in range(9):
            joint, single = displayed_correlations(t, q, k)
            assert joint == residue_correlation(t, q, k, True)
            assert single == residue_correlation(t, q, k, False)
            assert joint > 0 and single > 0
            residue_checks += 2

    # Distinct shift parameters, including negative nonconstant e_j.
    # Every prime-exponent difference is grouped before comparison.
    grouping_checks = 0
    for offset in range(3):
        ea = tensor_coefficients([(F(1, 3 + offset), F(1, 2)),
                                  (F(3, 5), F(1, 4))])
        eb = tensor_coefficients([(F(2, 3), F(1, 2)),
                                  (F(1, 5 + offset), F(1, 4))])
        pa, pb = combine(ea, ea, -1), combine(eb, eb, -1)
        direct = combine(centered(pa), centered(pb))
        d = combine(ea, eb)
        grouped = defaultdict(F, combine(d, d, -1))
        for polynomial in (pa, pb):
            for frequency, value in polynomial.items():
                grouped[frequency] -= value
        grouped[(0, 0)] += 1
        grouped = {key: value for key, value in grouped.items() if value}
        assert direct == grouped
        grouping_checks += 1

    print(f"OK: {residue_checks} exact local correlation checks by rational residues.")
    print(f"OK: {grouping_checks} signed two-prime centered correlation checks, with every collision.")
    print("Finite algebra only; no infinite-product or actual-sample bound is tested.")


if __name__ == "__main__":
    main()
