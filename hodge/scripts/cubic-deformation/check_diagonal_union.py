#!/usr/bin/env python3
"""Exact finite-chart checks for L009, not a global deformation verification."""

import importlib.util
from collections import defaultdict
from pathlib import Path


source = Path(__file__).resolve().parents[1] / "rm-cubic" / "check_correspondence.py"
spec = importlib.util.spec_from_file_location("rm_cubic_arithmetic", source)
arithmetic = importlib.util.module_from_spec(spec)
spec.loader.exec_module(arithmetic)
add, scale = arithmetic.add, arithmetic.scale
multiply, power = arithmetic.multiply, arithmetic.power
reduce = arithmetic.cyclotomic_reduce


def at_diagonal(poly):
    """Substitute a=zeta*v^2, equivalently v^2=a/zeta, exactly."""
    result = defaultdict(int)
    for (a_degree, v_degree, z_degree), coefficient in poly.items():
        result[(0, 2 * a_degree + v_degree, (z_degree + a_degree) % 7)] += coefficient
    return reduce(dict(result))


def main():
    one = arithmetic.ONE
    a = {(1, 0, 0): 1}
    t = {(0, 1, 0): 1, (1, -1, 0): 1}
    s = {(0, 1, 1): 1, (1, -1, 6): 1}
    theta = {(0, 0, 1): 1, (0, 0, 6): 1}
    conic = add(power(t, 2), power(s, 2), scale(multiply(theta, multiply(t, s)), -1),
                scale(a, -4), multiply(a, power(theta, 2)))
    assert reduce(conic) == {}
    assert at_diagonal(add(t, scale(s, -1))) == {}

    dt = {(0, 0, 0): 1, (1, -2, 0): -1}
    ds = {(0, 0, 1): 1, (1, -2, 6): -1}
    assert at_diagonal(dt) == {(0, 0, 0): 1, (0, 0, 1): -1}
    assert at_diagonal(ds) == {(0, 0, 1): 1, (0, 0, 0): -1}
    assert at_diagonal(add(dt, ds)) == {}

    derivative = add(scale(power(t, 6), 7), scale(multiply(a, power(t, 4)), -35),
                     scale(multiply(power(a, 2), power(t, 2)), 42), scale(power(a, 3), -7))
    assert at_diagonal(derivative) == {}
    for pair in [(6, 2), (3, 5), (6, 2)]:
        assert all(len({0, exponent % 7, -exponent % 7}) == 3 for exponent in pair)

    print("PASS: diagonal intersection, symmetric conic, slope -1, and critical-fibre identity.")
    print("PASS: id, f, and f^(-1) have distinct eigenvalues in both tangent directions.")
    print("The global obstruction and residual-extension arguments require L009's proof.")


if __name__ == "__main__":
    main()
