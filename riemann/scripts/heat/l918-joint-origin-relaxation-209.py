#!/usr/bin/env python3
"""One exact witness for the preapproved L918 finite-moment relaxation.

Uses Python integers/Fraction only. No search, numerical optimization,
external package, theta approximation, or representing-measure claim.
Run from the riemann notebook: python3 scripts/heat/l918-joint-origin-relaxation-209.py
"""

from fractions import Fraction as F
from itertools import combinations, permutations
from math import factorial
from pathlib import Path
import json


def rational(value):
    value = F(value)
    return str(value.numerator) if value.denominator == 1 else str(value)


def encode(value):
    if isinstance(value, F):
        return rational(value)
    if isinstance(value, dict):
        return {str(k): encode(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [encode(v) for v in value]
    return value


def multiply(left, right, degree=6):
    result = [F(0) for _ in range(degree + 1)]
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            if i + j <= degree:
                result[i + j] += a * b
    return result


def determinant(matrix):
    size = len(matrix)
    total = F(0)
    for permutation in permutations(range(size)):
        inversions = sum(permutation[i] > permutation[j]
                         for i in range(size) for j in range(i + 1, size))
        product = F((-1) ** inversions)
        for row, column in enumerate(permutation):
            product *= matrix[row][column]
        total += product
    return total


def principal_minors(matrix):
    result = []
    for size in range(1, len(matrix) + 1):
        for indices in combinations(range(len(matrix)), size):
            minor = determinant([[matrix[i][j] for j in indices] for i in indices])
            result.append({"indices": list(indices), "determinant": minor})
    return result


def main():
    failures = []
    checks = {}

    def check(name, value):
        checks[name] = bool(value)
        if not value:
            failures.append(name)

    epsilon = F(1, 1000000)
    # The single chosen point of the exact joint-row reduction.
    h, b, d, p, q = F(1), epsilon, epsilon, F(1), F(-3)
    S = [F(0), h, b, d, -p * b - q * d,
         p * q * b + (q * q - p) * d,
         (p * p - p * q * q) * b + (2 * p * q - q ** 3) * d]
    # The name q above denotes c1/c2; g_coeff below denotes cosine coefficients.
    g_coeff, inverse = [F(1)], [F(1)]
    for n in range(1, 7):
        g_coeff.append(-sum(S[k] * g_coeff[n - k] for k in range(1, n + 1)) / n)
        inverse.append(sum(S[k] * inverse[n - k] for k in range(1, n + 1)) / n)
    y = [F((-1) ** n * factorial(2 * n)) * g_coeff[n] for n in range(7)]

    # Independent finite-log reconstruction, rather than merely rerunning the recurrence.
    g_minus_one = [F(0)] + g_coeff[1:]
    power, log_coeff = [F(1)] + [F(0)] * 6, [F(0)] * 7
    for r in range(1, 7):
        power = multiply(power, g_minus_one)
        for n in range(7):
            log_coeff[n] += F((-1) ** (r + 1), r) * power[n]
    log_residual = [log_coeff[n] + S[n] / n for n in range(1, 7)]
    inverse_residual = multiply(g_coeff, inverse)
    inverse_residual[0] -= 1
    check("cosine_coefficient_interface", all(
        g_coeff[n] == F((-1) ** n, factorial(2 * n)) * y[n] for n in range(7)))
    check("finite_log_through_x6", all(value == 0 for value in log_residual))
    check("finite_inverse_through_x6", all(value == 0 for value in inverse_residual))
    check("y0_equals_one", y[0] == 1)
    check("y1_strictly_positive", y[1] > 0)

    M = [[y[i + j] for j in range(4)] for i in range(4)]
    N = [[y[i + j + 1] for j in range(3)] for i in range(3)]
    H = [[S[i + j + 2] for j in range(3)] for i in range(3)]
    minor_records = {"M3": principal_minors(M), "N2": principal_minors(N),
                     "H2": principal_minors(H)}
    for name, records in minor_records.items():
        for item in records:
            check(name + "_minor_" + "_".join(map(str, item["indices"])),
                  item["determinant"] >= 0)
    check("M3_all_nonempty_principal_minors_strict", all(
        item["determinant"] > 0 for item in minor_records["M3"]))
    check("N2_all_nonempty_principal_minors_strict", all(
        item["determinant"] > 0 for item in minor_records["N2"]))
    check("H2_rank_exactly_two", determinant(H) == 0 and
          determinant([[H[i][j] for j in range(2)] for i in range(2)]) > 0)

    # c=v/sqrt(norm_squared): all needed products are exact rational numbers.
    v = [p, q, F(1)]
    norm_squared = sum(value * value for value in v)
    cc = [[v[i] * v[j] / norm_squared for j in range(3)] for i in range(3)]
    null_rows = [sum(H[i][j] * v[j] for j in range(3)) for i in range(3)]
    A = [[b, d], [d, -p * b - q * d]]
    B = [[F(1), F(0), -p], [F(0), F(1), -q]]
    congruence_residual = [[H[i][j] - sum(B[k][i] * A[k][l] * B[l][j]
                              for k in range(2) for l in range(2))
                            for j in range(3)] for i in range(3)]
    check("all_three_null_rows", all(value == 0 for value in null_rows))
    check("joint_row_congruence", all(value == 0 for row in congruence_residual for value in row))
    check("unit_normalization", sum(cc[i][i] for i in range(3)) == 1)
    check("c2_nonzero", cc[2][2] > 0)

    J_terms = [[cc[i][j] * ((i + j + 2) * inverse[i + j + 2] + inverse[i + j + 1])
                for j in range(3)] for i in range(3)]
    J = sum(value for row in J_terms for value in row)
    weights = [p * p, 2 * p * q, q * q + 2 * p, 2 * q, F(1)]
    joint_value = sum(weights[n - 2] * (n * inverse[n] + inverse[n - 1])
                      for n in range(2, 7)) / norm_squared
    # Independent inverse reconstruction from the cosine coefficients.
    inverse_direct = [F(1)]
    for n in range(1, 7):
        inverse_direct.append(-sum(g_coeff[k] * inverse_direct[n - k]
                                   for k in range(1, n + 1)))
    check("inverse_independent_reconstruction", inverse == inverse_direct)
    check("J_joint_reduction", J == joint_value)
    check("J_strictly_negative", J < 0)
    lower, upper = F(-3, 40), F(-7, 100)
    check("J_exact_rational_bracket", lower < J < upper)

    counts = {name: {"total": len(records),
                     "positive": sum(item["determinant"] > 0 for item in records),
                     "zero": sum(item["determinant"] == 0 for item in records),
                     "negative": sum(item["determinant"] < 0 for item in records)}
              for name, records in minor_records.items()}
    certificate = {
        "schema": "l918-fixed-finite-relaxation-one-witness-v1",
        "scope": "Fixed finite-moment relaxation only; no actual theta contact or representing measure asserted.",
        "omitted_actual_conditions": ["Equality with the actual theta moments",
            "lambda-dependent exponential-tilt relations and the actual lambda band",
            "Full-support theta density", "All higher-moment and analytic theta relations"],
        "selection": "One fixed exact tuple; no parameter or support-family sweep.",
        "point": {"h": h, "b": b, "d": d, "p": p, "q": q, "epsilon": epsilon},
        "S1_through_S6": S[1:], "g_coefficients": g_coeff, "y0_through_y6": y,
        "inverse_coefficients": inverse, "finite_log_residual": log_residual,
        "finite_inverse_residual": inverse_residual,
        "matrices": {"M3": M, "N2": N, "H2": H},
        "principal_minors": minor_records, "minor_counts": counts,
        "normalization": {"vector_numerator": v, "norm_squared": norm_squared,
            "c_description": "(1,-3,1)/sqrt(11)", "products_ci_cj": cc,
            "sum_ci_squared": sum(cc[i][i] for i in range(3)), "c2_squared": cc[2][2]},
        "joint_rows": {"null_rows_before_normalization": null_rows,
                       "congruence_residual": congruence_residual},
        "J": {"value": J, "terms": J_terms, "joint_value": joint_value,
              "strict_lower_bound": lower, "strict_upper_bound": upper,
              "required_nonnegative_threshold": F(0)},
        "checks": checks, "failures": failures, "passed": not failures,
    }
    path = Path(__file__).with_suffix(".json")
    path.write_text(json.dumps(encode(certificate), indent=2) + "\n", encoding="utf-8")
    print("PASS" if not failures else "FAIL", "one exact finite-relaxation witness")
    print("J =", rational(J), "; required J >= 0")
    print("Checked strict bracket:", rational(lower), "< J <", rational(upper))
    print("All principal minors:", json.dumps(counts, sort_keys=True))
    print("Exact checks:", len(checks), "; failures:", failures)
    print("Certificate:", path.relative_to(Path.cwd()))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
