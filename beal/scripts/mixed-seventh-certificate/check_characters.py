#!/usr/bin/env python3
"""Exact quadratic-ring checks for the conditional reducible-character audit.

This checks the finite arithmetic in L017. Raynaud's finite-flat theorem and
global/local reciprocity remain named mathematical inputs, not program checks.
"""

import argparse
import json
from fractions import Fraction
from pathlib import Path


def add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def multiply(x, y):
    # epsilon^2 = epsilon + 1 in Z[epsilon].
    a, b = x
    c, d = y
    return (a * c + b * d, a * d + b * c + b * d)


def power(x, exponent):
    result = (1, 0)
    for _ in range(exponent):
        result = multiply(result, x)
    return result


def norm(x):
    a, b = x
    return a * a + a * b - b * b


def residue_at_five(x):
    # sqrt(5)=2 epsilon-1 vanishes; epsilon=3 in F_5.
    return (x[0] + 3 * x[1]) % 5


def positive_at_both_embeddings(x):
    lower, upper = Fraction(2236, 1000), Fraction(2237, 1000)
    assert lower**2 < 5 < upper**2
    epsilon_intervals = (
        ((1 + lower) / 2, (1 + upper) / 2),
        ((1 - upper) / 2, (1 - lower) / 2),
    )
    a, b = x
    return all(min(a + b * lo, a + b * hi) > 0
               for lo, hi in epsilon_intervals)


def check():
    epsilon = (0, 1)
    square_root_five = (-1, 2)
    assert multiply(square_root_five, square_root_five) == (5, 0)
    assert norm(epsilon) == -1

    unit = power(epsilon, 8)
    assert unit == (13, 21)
    assert norm(unit) == 1
    assert tuple(t % 3 for t in unit) == (1, 0)
    assert residue_at_five(unit) == 1
    assert tuple(t % 7 for t in unit) == (6, 0)

    alpha = (6, -1)
    epsilon_squared = power(epsilon, 2)
    inverse_epsilon_squared = (2, -1)
    assert multiply(epsilon_squared, inverse_epsilon_squared) == (1, 0)
    beta = multiply(power(alpha, 2), inverse_epsilon_squared)
    assert beta == (85, -48)
    assert multiply(beta, epsilon_squared) == power(alpha, 2)
    ray_difference = multiply((-3, 6), (-12, 8))
    assert beta == add((1, 0), ray_difference)
    assert norm(alpha) == 29
    assert norm(beta) == 29**2
    assert (alpha[0] + 6 * alpha[1]) % 29 == 0
    assert (alpha[0] + 24 * alpha[1]) % 29 != 0
    assert tuple(t % 3 for t in beta) == (1, 0)
    assert residue_at_five(beta) == 1
    assert all(positive_at_both_embeddings(x)
               for x in (unit, alpha, epsilon_squared, beta))

    # Both 3 and 7 are inert; the finite-flat calculation uses e=1 at 7.
    assert all((x * x - x - 1) % p != 0
               for p in (3, 7) for x in range(p))
    digit_types = [
        {"digits": [r0, r1], "exponent": r0 + 7 * r1,
         "unit_reciprocity_value": (-1)**(r0 + r1)}
        for r0 in (0, 1) for r1 in (0, 1)
    ]
    assert sorted(row["exponent"] for row in digit_types) == [0, 1, 7, 8]
    survivors = sorted(row["exponent"] for row in digit_types
                       if row["unit_reciprocity_value"] == 1)
    assert survivors == [0, 8]
    assert 29 % 7 == 1
    traces = sorted((value + pow(value, -1, 7)) % 7
                    for value in (1, 6))
    assert traces == [2, 5]
    return {
        "ring_basis": ["1", "epsilon"],
        "epsilon_relation": "epsilon^2=epsilon+1",
        "epsilon_eighth_power": unit,
        "prime_generator": alpha,
        "norm_prime_generator": norm(alpha),
        "positive_ray_generator": beta,
        "norm_ray_generator": norm(beta),
        "ray_relation": "beta-1=3*sqrt(5)*(8*epsilon-12)",
        "total_positivity": "all four tested elements certified positive",
        "finite_flat_digit_types": digit_types,
        "surviving_inertia_exponents": survivors,
        "conditional_trace_residues_modulo_7": traces,
        "scope": "exact arithmetic only; finite-flatness and reciprocity are cited",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        help="optional path for the exact JSON certificate")
    args = parser.parse_args()
    result = json.dumps(check(), indent=2) + "\n"
    if args.output:
        args.output.write_text(result)
    print(result, end="")
