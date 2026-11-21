#!/usr/bin/env python3
"""Supplementary exact rational checks for L966; no theta sign certification."""

from fractions import Fraction as F
from math import comb
from pathlib import Path
import json


def add(a, b):
    result = [F(0)] * max(len(a), len(b))
    for i, value in enumerate(a):
        result[i] += value
    for i, value in enumerate(b):
        result[i] += value
    return result


def scale(a, value):
    return [value * x for x in a]


def mul(a, b):
    result = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i + j] += x * y
    return result


def power(a, n):
    result = [F(1)]
    for _ in range(n):
        result = mul(result, a)
    return result


def check(n):
    b = F(1, 4)
    h = F(64 * 9**n)
    p = (n - 1) // 2
    v = [F(comb(n, 2 * i + 1), 4**i) for i in range(p + 1)]
    w = mul(v, v)
    D = [
        sum(
            (w[s] * comb(n - 1 - s, r) * b**(n - 1 - s - r)
             for s in range(min(2 * p, n - 1 - r) + 1)),
            F(0),
        )
        for r in range(n)
    ]
    d = [
        h * sum(
            (D[r] / (h - b)**(n - k - r + 1) for r in range(n - k + 1)),
            F(0),
        )
        for k in range(1, n + 1)
    ]

    # Build the original B directly by squaring the signed P coefficients.
    # This is independent of the unsigned convolution defining D and d.
    signed_square = mul([(-1)**i * v[i] for i in range(p + 1)],
                        [(-1)**i * v[i] for i in range(p + 1)])
    B = [F(0)] * n
    for s, coefficient in enumerate(signed_square):
        B[n - 1 - s] += coefficient
    lhs = scale(B, h)

    # Clear (t+h)(t+b)^n in the proposed complete partial fraction identity.
    rhs = scale(power([b, F(1)], n), -d[0])
    for k in range(1, n + 1):
        term = mul([h, F(1)], power([b, F(1)], n - k))
        rhs = add(rhs, scale(term, (-1)**(k - 1) * d[k - 1]))
    residual = add(lhs, scale(rhs, -1))

    # Check the actual residue at -h independently of the infinity argument.
    B_at_minus_h = sum((coefficient * (-h)**i for i, coefficient in enumerate(B)), F(0))
    residue = h * B_at_minus_h / (b - h)**n
    residue_error = residue + d[0]
    failures = []
    if any(residual):
        failures.append("nonzero denominator-cleared polynomial")
    if residue_error:
        failures.append("residue at -h differs from -d_1")
    if not all(value > 0 for value in D + d):
        failures.append("nonpositive coefficient")
    return {
        "n": n,
        "h": str(h),
        "B_coefficients_ascending": list(map(str, B)),
        "D_coefficients": list(map(str, D)),
        "d_coefficients_k_1_to_n": list(map(str, d)),
        "polynomial_residual_coefficients_ascending": list(map(str, residual)),
        "max_abs_polynomial_residual": str(max(map(abs, residual))),
        "required_polynomial_residual": "0",
        "residue_cancellation_error": str(residue_error),
        "required_residue_error": "0",
        "minimum_d": str(min(d)),
        "required_coefficient_sign": ">0",
        "failures": failures,
    }


def main():
    cases = [check(n) for n in range(1, 13)]
    failures = [{"n": case["n"], "failures": case["failures"]}
                for case in cases if case["failures"]]
    certificate = {
        "purpose": "Exact finite algebra diagnostics for L966 equations (2),(8)",
        "arithmetic": "Python fractions.Fraction; no floating point",
        "scope": "n=1,...,12 with eta=1/(64*9^n); not an all-n proof or a sign bound",
        "summary": {
            "case_count": len(cases),
            "max_abs_polynomial_residual": str(max(F(c["max_abs_polynomial_residual"]) for c in cases)),
            "required_polynomial_residual": "0",
            "all_residue_cancellations_exact": all(F(c["residue_cancellation_error"]) == 0 for c in cases),
            "all_d_strictly_positive": all(F(c["minimum_d"]) > 0 for c in cases),
            "failures": failures,
        },
        "cases": cases,
    }
    path = Path(__file__).with_suffix(".json")
    path.write_text(json.dumps(certificate, indent=2) + "\n", encoding="utf-8")
    print("Exact rational checks: n=1,...,12")
    print("Maximum polynomial residual: actual",
          certificate["summary"]["max_abs_polynomial_residual"], "; required 0")
    print("Maximum residue error: actual",
          max(abs(F(c["residue_cancellation_error"])) for c in cases), "; required 0")
    print("All coefficients strictly positive:",
          certificate["summary"]["all_d_strictly_positive"], "; required True")
    print("Failures:", failures)
    print("Full certificate:", path.relative_to(Path.cwd()))
    print("No theta-integral sign or uniform-in-n estimate checked.")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

