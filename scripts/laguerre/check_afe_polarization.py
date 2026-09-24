#!/usr/bin/env python3
"""Exact algebra checks for L317; no numerical zeta or sign certification."""
from fractions import Fraction as F
from math import comb


def check_pair_kernels():
    # Coefficients of nu^j mu^(degree-j), obtained by symmetrizing Q and T.
    q = {0: F(1, 2), 1: F(-1), 2: F(1, 2)}
    t = {0: F(1, 2), 1: F(-2), 2: F(3), 3: F(-2), 4: F(1, 2)}
    for degree, actual in ((2, q), (4, t)):
        expected = {j: F(comb(degree, j) * (-1) ** (degree - j), 2)
                    for j in range(degree + 1)}
        assert actual == expected, (degree, actual, expected)
    print("Q and T: exact pair kernels are (nu-mu)^2/2 and (nu-mu)^4/2")


def check_real_grouping():
    # Rational points on the unit circle permit exact trigonometric products.
    phases = [(F(3, 5), F(4, 5)), (F(5, 13), F(-12, 13)),
              (F(-7, 25), F(24, 25)), (F(0), F(-1))]
    frequencies = [F(1, 7), F(5, 3), F(-2, 5), F(13, 4)]
    amplitudes = [F(2), F(3, 7), F(5, 11), F(1, 3)]
    assert all(c * c + s * s == 1 for c, s in phases)
    checks = 0
    for count in range(1, 5):
        jets = []
        for order in range(5):
            jets.append(sum(2 * amplitudes[n] * frequencies[n] ** order
                            * (phases[n][0], -phases[n][1],
                               -phases[n][0], phases[n][1])[order % 4]
                            for n in range(count)))
        q = jets[1] ** 2 - jets[0] * jets[2]
        t = jets[0] * jets[4] - 4 * jets[1] * jets[3] + 3 * jets[2] ** 2
        for kappa in (F(0), F(1, 2), F(3, 7), F(5)):
            def kernel(v):
                return v ** 4 - kappa * v ** 2

            diagonal = sum(amplitudes[n] ** 2 * kernel(2 * frequencies[n])
                           for n in range(count))
            cross = F(0)
            for n in range(count):
                for m in range(n + 1, count):
                    cn, sn = phases[n]
                    cm, sm = phases[m]
                    cross += 2 * amplitudes[n] * amplitudes[m] * (
                        kernel(frequencies[n] + frequencies[m]) * (cn * cm + sn * sm)
                        + kernel(frequencies[n] - frequencies[m]) * (cn * cm - sn * sm))
            assert t - kappa * q == diagonal + cross, (count, kappa)
            checks += 1
    print(f"Real cosine grouping: {checks} exact rational checks passed")


if __name__ == "__main__":
    check_pair_kernels()
    check_real_grouping()
