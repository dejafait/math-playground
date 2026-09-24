#!/usr/bin/env python3
"""Exact finite algebra checks for L338; not an asymptotic certificate."""

from fractions import Fraction as Q
from math import factorial


def main():
    degree = 16
    checked = 0
    for cosine in (Q(-1), Q(-4, 5), Q(-3, 5), Q(0), Q(3, 5), Q(4, 5), Q(1)):
        # Inverse of 1 - 2*cosine*x + x^2, computed as a power series.
        inverse = [Q(1), 2 * cosine]
        for n in range(2, degree):
            inverse.append(2 * cosine * inverse[-1] - inverse[-2])

        # cos(m*theta), where cos(theta)=cosine, with exact rationals.
        multiple_cosine = [Q(1), cosine]
        for n in range(2, degree + 1):
            multiple_cosine.append(
                2 * cosine * multiple_cosine[-1] - multiple_cosine[-2]
            )

        for m in range(1, degree + 1):
            # log((1+x)^2 / (1-2*cosine*x+x^2)), from its derivative.
            denominator_log = -2 * cosine * inverse[m - 1]
            if m >= 2:
                denominator_log += 2 * inverse[m - 2]
            coefficient = Q(2 * (-1) ** (m + 1), m) - denominator_log / m
            expected = 2 * (Q((-1) ** (m + 1)) + multiple_cosine[m]) / m
            assert coefficient == expected
            assert abs(coefficient) <= Q(4, m)
            if cosine == -1:
                assert coefficient == 0
            if cosine == 1:
                assert coefficient == (Q(4, m) if m % 2 else 0)
            checked += 1

    # The exact rational comparisons used to select b=6 and alpha=1/2.
    assert sum(Q(3**k, factorial(k)) for k in range(9)) > 20
    assert 4 * Q(1, 60) == Q(1, 15)
    assert 1 / (1 - Q(1, 15)) - 1 == Q(1, 14)
    assert Q(1, 4) - Q(1, 14) == Q(5, 28) > Q(1, 8)
    assert Q(1, 2) ** 2 + Q(1, 4) == Q(1, 2)

    print(f"OK: {checked} paired Euler-log coefficients and bounds; "
          "five rational margin comparisons. No asymptotic or height certificate.")


if __name__ == "__main__":
    main()
