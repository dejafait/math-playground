#!/usr/bin/env python3
"""Exact identities for L014; not a verification of the global lifting proof."""

import importlib.util
from pathlib import Path


source = Path(__file__).resolve().parents[1] / "rm-cubic" / "check_correspondence.py"
spec = importlib.util.spec_from_file_location("rm_cubic_arithmetic", source)
arithmetic = importlib.util.module_from_spec(spec)
spec.loader.exec_module(arithmetic)
add, scale = arithmetic.add, arithmetic.scale
multiply, power = arithmetic.multiply, arithmetic.power
reduce = arithmetic.cyclotomic_reduce
ONE = arithmetic.ONE

# Reinterpret the first two exponents as the degrees of t and s. Normalize a=1;
# t=c*T, s=c*S, a=c^2 restores the identities at every nonzero a.
t = {(1, 0, 0): 1}
s = {(0, 1, 0): 1}
theta = {j: {(0, 0, j): 1, (0, 0, 7 - j): 1} for j in (1, 2, 3)}


def dickson(x):
    return add(power(x, 7), scale(power(x, 5), -7),
               scale(power(x, 3), 14), scale(x, -7))


def derivative(x):
    return add(scale(power(x, 6), 7), scale(power(x, 4), -35),
               scale(power(x, 2), 42), scale(ONE, -7))


def second_derivative(x):
    return add(scale(power(x, 5), 42), scale(power(x, 3), -140), scale(x, 84))


def conic(j, x, y):
    return add(power(x, 2), power(y, 2),
               scale(multiply(theta[j], multiply(x, y)), -1),
               scale(ONE, -4), power(theta[j], 2))


def main():
    factored = add(t, scale(s, -1))
    for j in (1, 2, 3):
        factored = multiply(factored, conic(j, t, s))
    assert reduce(add(dickson(t), scale(dickson(s), -1), scale(factored, -1))) == {}

    incidence = {(1, 2): {1, 3}, (1, 3): {2, 3}, (2, 3): {1, 2}}
    for sign in (-1, 1):
        points = {k: scale(theta[k], sign) for k in (1, 2, 3)}
        for value in points.values():
            assert reduce(add(dickson(value), scale(ONE, -2 * sign))) == {}
            assert reduce(derivative(value)) == {}
            assert reduce(second_derivative(value)) != {}
        for (k, ell), indices in incidence.items():
            for left, right in ((k, ell), (ell, k)):
                x, y = points[left], points[right]
                assert {j for j in (1, 2, 3) if not reduce(conic(j, x, y))} == indices
                i, j = sorted(indices)
                jacobian = scale(multiply(add(theta[i], scale(theta[j], -1)),
                                          add(power(x, 2), scale(power(y, 2), -1))), 2)
                assert reduce(jacobian) != {}
        x, y = points[2], points[3]
        h_without_Rprime = multiply(add(x, scale(y, -1)), conic(3, x, y))
        assert reduce(h_without_Rprime) != {}

    # The two equations a1-a2=a1-a3=0 force the smoothing numerator a3-a2=0.
    # Check the precise linear identity, retaining its signs.
    smooth_numerator = (0, -1, 1)
    edge12, edge13 = (1, -1, 0), (1, 0, -1)
    assert smooth_numerator == tuple(x - y for x, y in zip(edge12, edge13))

    # The extra very-general j-map hypotheses are nonempty: A(z)=z+1, B(z)=z+3.
    for critical_value in (-2, 2):
        A, B = critical_value + 1, critical_value + 3
        discriminant_factor = 4 * A**3 + 27 * B**2
        derivative_factor = A**2 * B * (3 * B - 2 * A)
        assert discriminant_factor != 0 and derivative_factor != 0

    assert reduce(add(power(theta[1], 2), scale(ONE, -2), scale(theta[2], -1))) == {}
    assert reduce(add(ONE, theta[1], theta[2], theta[3])) == {}
    for weights in ((6, 2), (3, 5), (6, 2)):
        for weight in weights:
            assert len({weight * k % 7 for k in (-2, -1, 1, 2)}) == 4

    print("PASS: Dickson factorization and all ordered critical-pair incidences.")
    print("PASS: simple critical points, transverse conics, and nonzero smoothing units.")
    print("PASS: residue compatibility identity, generic j-map conditions, cycle action, and infinity weights.")
    print("The dense-open j-map identity, component extraction, and global kernel require L014's proof.")


if __name__ == "__main__":
    main()
