#!/usr/bin/env python3
"""Exact finite coefficient checks for L327; no zeta sign certification."""
from fractions import Fraction as F
from math import factorial


def add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def mul(x, y):
    return (x[0] * y[0] - x[1] * y[1],
            x[0] * y[1] + x[1] * y[0])


def scale(x, c):
    return (c * x[0], c * x[1])


def star(x):
    return (x[0], -x[1])


def total(xs):
    result = (F(0), F(0))
    for x in xs:
        result = add(result, x)
    return result


def check_coefficients():
    phases = [(F(3, 5), F(4, 5)), (F(5, 13), F(-12, 13)),
              (F(-7, 25), F(24, 25)), (F(0), F(-1))]
    amplitudes = [F(2), F(3, 7), F(5, 11), F(1, 3)]
    frequencies = [F(3, 2), F(2, 3), F(0), F(1, 11)]
    chis = [(F(1), F(0)), (F(3, 5), F(4, 5)), (F(0), F(-1))]
    assert all(x * x + y * y == 1 for x, y in phases + chis)
    checks = 0
    for p in (2, 4, 6, 10, 16):
        r = F(4 * p, 3)
        assert 2 * r * F(3, 8) == p
        normalizer = 2 * r
        for count in range(1, 5):
            coeffs = [scale(phases[j], amplitudes[j]) for j in range(count)]
            # Taylor coefficients from the separate finite exponential sums.
            jets = [total(scale(coeffs[j], frequencies[j] ** k / factorial(k))
                          for j in range(count)) for k in range(p + 1)]
            for chi in chis:
                plus = [add(jets[k], scale(mul(chi, star(jets[k])), (-1) ** k))
                        for k in range(p + 1)]
                minus = [star(term) for term in plus]
                coefficient = total(mul(plus[k], minus[p - k]) for k in range(p + 1))
                lhs = scale(coefficient, F(factorial(p), 2) / normalizer ** p)

                # Independently form the two ordered pair sums, including ties.
                ratio = total(scale(mul(coeffs[j], star(coeffs[k])),
                                    ((frequencies[j] + frequencies[k]) / normalizer) ** p)
                              for j in range(count) for k in range(count))
                product = total(scale(mul(coeffs[j], coeffs[k]),
                                      ((frequencies[j] - frequencies[k]) / normalizer) ** p)
                                for j in range(count) for k in range(count))
                rhs = add(ratio, (mul(star(chi), product)[0], F(0)))
                assert lhs[1] == rhs[1] == 0
                assert lhs == rhs, (p, count, chi, lhs, rhs)
                checks += 1
    print(f"Even coefficient/ordered pair identity: {checks} exact rational checks passed")


def check_rates():
    # log 2 strictly exceeds this two-term positive atanh-series sum.
    log_two_lower = 2 * (F(1, 3) + F(1, 81))
    gamma_lower = F(3, 4) * log_two_lower - F(1, 2)
    assert gamma_lower == F(1, 54)
    assert gamma_lower > F(1, 200)
    assert F(3, 4) > F(1, 200)
    assert F(3) > F(1, 200)
    print("Order/radius relation and decay-rate comparisons: exact rational checks passed")


if __name__ == "__main__":
    check_coefficients()
    check_rates()
