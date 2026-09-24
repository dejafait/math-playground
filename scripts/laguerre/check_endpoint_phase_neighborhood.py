#!/usr/bin/env python3
"""Exact algebra and margin checks for L339; no asymptotic certificate."""

from fractions import Fraction as F


def quotient_series(numerator, denominator, degree):
    """Formal quotient through the given degree over the rationals."""
    result = []
    for k in range(degree + 1):
        value = numerator[k] if k < len(numerator) else F(0)
        for j in range(1, min(k, len(denominator) - 1) + 1):
            value -= denominator[j] * result[k - j]
        result.append(value / denominator[0])
    return result


def check_paired_logarithm():
    # Differentiate the rational paired factor, divide by that factor,
    # and compare with the independently generated cosine coefficients.
    degree = 12
    checks = 0
    for cosine in [F(1), F(1999, 2001), F(3, 5), F(-1, 3), F(-1)]:
        paired = quotient_series(
            [F(1), F(2), F(1)], [F(1), 2 * cosine, F(1)], degree
        )
        derivative = [(k + 1) * paired[k + 1] for k in range(degree)]
        log_derivative = quotient_series(derivative, paired, degree - 1)
        cosines = [F(1), cosine]
        for m in range(2, degree + 1):
            cosines.append(2 * cosine * cosines[-1] - cosines[-2])
        for m in range(1, degree + 1):
            expected = 2 * (-1) ** (m + 1) * (1 - cosines[m])
            assert log_derivative[m - 1] == expected
            checks += 1
    return checks


def check_margins():
    q = F(1, 2)
    assert (q / (1 - q) ** 2 - q) / q**2 == 6
    assert (q * (1 + q) / (1 - q) ** 3 - q) / q**2 == 22
    assert F(1, 16) - F(6, 100) == F(1, 400)
    assert F(1) + F(1, 2) + F(1, 8) / (1 - F(1, 6)) == F(33, 20)
    assert F(33, 20) < F(5, 3)
    assert F(1, 32) + F(1, 15) == F(47, 480)
    assert 1 / (1 - F(47, 480)) == F(480, 433)
    assert 2 / (2 - F(1, 32)) == F(64, 63)
    beta = F(5, 6) * (F(480, 433) * F(64, 63) ** 2 - 1)
    assert beta == F(412505, 3437154)
    assert F(1, 8) - beta == F(68557, 13748616) > 0
    return beta


if __name__ == "__main__":
    count = check_paired_logarithm()
    beta = check_margins()
    print(f"OK: {count} exact paired-log coefficients and 10 rational checks.")
    print(f"Gaussian error bound {beta} < 1/8; slope slack 1/400.")
