#!/usr/bin/env python3
"""Exact arithmetic supporting the fixed-pair support proof in L098."""
import json
from fractions import Fraction
from pathlib import Path


def bareiss(matrix):
    a = [row[:] for row in matrix]
    previous, sign = 1, 1
    for k in range(len(a) - 1):
        pivot_row = next((i for i in range(k, len(a)) if a[i][k]), None)
        if pivot_row is None:
            return 0
        if pivot_row != k:
            a[k], a[pivot_row] = a[pivot_row], a[k]
            sign *= -1
        pivot = a[k][k]
        for i in range(k + 1, len(a)):
            for j in range(k + 1, len(a)):
                numerator = pivot * a[i][j] - a[i][k] * a[k][j]
                assert numerator % previous == 0
                a[i][j] = numerator // previous
            a[i][k] = 0
        previous = pivot
    return sign * a[-1][-1]


def rational_determinant(matrix):
    a = [[Fraction(x) for x in row] for row in matrix]
    determinant = Fraction(1)
    for k in range(len(a)):
        pivot_row = next((i for i in range(k, len(a)) if a[i][k]), None)
        if pivot_row is None:
            return Fraction(0)
        if pivot_row != k:
            a[k], a[pivot_row] = a[pivot_row], a[k]
            determinant *= -1
        pivot = a[k][k]
        determinant *= pivot
        for i in range(k + 1, len(a)):
            ratio = a[i][k] / pivot
            for j in range(k + 1, len(a)):
                a[i][j] -= ratio * a[k][j]
            a[i][k] = Fraction(0)
    return determinant


def main():
    coefficients = [55, 165, 594, 1100, 2145, 2475, 2970, 1782, 1215]
    derivative = [i * coefficients[i] for i in range(1, 9)]
    f, g = coefficients[::-1], derivative[::-1]
    matrix = []
    for i in range(7):
        matrix.append([0] * i + f + [0] * (6 - i))
    for i in range(8):
        matrix.append([0] * i + g + [0] * (7 - i))
    resultant = bareiss(matrix)
    cross_check = rational_determinant(matrix)
    b = coefficients[-1]
    assert resultant % b == 0
    discriminant = resultant // b  # (-1)^(8*7/2) = 1
    remaining = abs(discriminant)
    factorization = {}
    for p in (2, 3, 5, 11):
        exponent = 0
        while remaining and remaining % p == 0:
            remaining //= p
            exponent += 1
        if exponent:
            factorization[str(p)] = exponent
    norms = [Fraction(1, b), Fraction(5**11, b)]
    class_representatives = [75, 15]
    cube_scales = [Fraction(1, 45), Fraction(125, 9)]
    checks = {
        "matrix_is_15_by_15": len(matrix) == 15 and all(len(r) == 15 for r in matrix),
        "independent_exact_determinants_agree": resultant == cross_check,
        "discriminant_nonzero": discriminant != 0,
        "factorization_complete": remaining == 1,
        "support_primes_exactly_3_5_11": set(factorization) == {"3", "5", "11"},
        "system_I_norm_scale": norms[0] == class_representatives[0] * cube_scales[0]**3,
        "system_II_norm_scale": norms[1] == class_representatives[1] * cube_scales[1]**3,
    }
    failures = [name for name, passed in checks.items() if not passed]
    certificate = {
        "scope": "Exact polynomial discriminant and norm-scale arithmetic only; the unbounded ideal support proof is in L098.",
        "coefficients_ascending": coefficients,
        "derivative_ascending": derivative,
        "sylvester_matrix": matrix,
        "resultant": resultant,
        "rational_determinant": str(cross_check),
        "discriminant": discriminant,
        "discriminant_factorization": factorization,
        "unfactored_remainder": remaining,
        "norm_multipliers_I_II": list(map(str, norms)),
        "norm_class_representatives_I_II": class_representatives,
        "norm_cube_scales_I_II": list(map(str, cube_scales)),
        "checks": checks,
        "failures": failures,
    }
    output = Path(__file__).with_name("octic-cube-support-certificate.json")
    output.write_text(json.dumps(certificate, indent=2) + "\n")
    print(f"Checks: {sum(checks.values())}/{len(checks)}; failures: {failures}")
    print(f"Disc(h) = {discriminant}; factors: {factorization}; remainder: {remaining}")
    print("Actual/required exceptional support: {3,5,11}/{p dividing 5*1215*Disc(h)}")
    print(f"Norm multipliers: {norms[0]} = 75*(1/45)^3; {norms[1]} = 15*(125/9)^3")
    print(f"Certificate: {output.relative_to(Path.cwd())}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
