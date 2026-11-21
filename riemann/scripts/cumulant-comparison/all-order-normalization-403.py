#!/usr/bin/env python3
"""Finite exact normalization checks for L771; not an all-order proof."""

import json
import math
from fractions import Fraction as F
from pathlib import Path


def transform(poly):
    out = [F(0)] * (len(poly) + 1)
    for degree, coefficient in enumerate(poly):
        out[degree] += degree * coefficient
        out[degree + 1] -= coefficient
    return out


def evaluate(poly, node):
    out = F(0)
    for coefficient in reversed(poly):
        out = out * node + coefficient
    return out


def determinant(matrix):
    rows = [[F(entry) for entry in row] for row in matrix]
    result = F(1)
    for col in range(len(rows)):
        pivot = next((i for i in range(col, len(rows)) if rows[i][col]), None)
        if pivot is None:
            return F(0)
        if pivot != col:
            rows[col], rows[pivot] = rows[pivot], rows[col]
            result = -result
        value = rows[col][col]
        result *= value
        for i in range(col + 1, len(rows)):
            multiple = rows[i][col] / value
            for j in range(col + 1, len(rows)):
                rows[i][j] -= multiple * rows[col][j]
            rows[i][col] = F(0)
    return result


def vandermonde(nodes):
    return math.prod(nodes[j] - nodes[i]
                     for i in range(len(nodes)) for j in range(i + 1, len(nodes)))


def check_order(r):
    q_polys, pure_polys = [[F(-3, 2), F(1)]], [[F(0), F(1)]]
    for _ in range(1, r):
        q_polys.append(transform(q_polys[-1]))
        pure_polys.append(transform(pure_polys[-1]))
    h_polys = [list(reversed(poly + [F(0)] * (r + 1 - len(poly))))
               for poly in q_polys]
    x_nodes = [F(4 + i) for i in range(r)]
    y_nodes = [1 / x for x in x_nodes]
    parity = (-1) ** (r * (r - 1) // 2)
    reference = vandermonde(x_nodes) * math.prod(x_nodes)
    pure_ratio = parity * determinant([[evaluate(p, x) for x in x_nodes]
                                      for p in pure_polys]) / reference
    signed_ratio = parity * determinant([[evaluate(p, x) for x in x_nodes]
                                        for p in q_polys]) / reference
    reciprocal_ratio = determinant([[evaluate(h, y) for y in y_nodes]
                                     for h in h_polys]) / vandermonde(y_nodes)
    confluent = determinant([h[:r] for h in h_polys])
    coefficient_norms = [sum(map(abs, poly)) for poly in q_polys]
    leading_ok = all(len(poly) == j + 2 and poly[-1] == (-1) ** j
                     for j, poly in enumerate(q_polys))
    checks = {
        "pure_signed_ratio_one": pure_ratio == 1,
        "reciprocal_parity_identity": signed_ratio == reciprocal_ratio,
        "confluent_determinant_one": confluent == 1,
        "coefficient_bound": max(coefficient_norms) <= 3 * math.factorial(r),
        "least_degree_and_leading_sign": leading_ok,
    }
    return {
        "r": r, "parity": parity,
        "x_nodes": list(map(str, x_nodes)),
        "q_coefficients_ascending": [list(map(str, poly)) for poly in q_polys],
        "h_coefficients_ascending": [list(map(str, poly)) for poly in h_polys],
        "actual": {
            "pure_signed_ratio": str(pure_ratio),
            "signed_base_ratio": str(signed_ratio),
            "reciprocal_base_ratio": str(reciprocal_ratio),
            "confluent_determinant": str(confluent),
            "coefficient_norms": list(map(str, coefficient_norms)),
        },
        "required": {
            "pure_signed_ratio": "1", "confluent_determinant": "1",
            "coefficient_norm_at_most": str(3 * math.factorial(r)),
            "signed_and_reciprocal_ratios_equal": True,
        },
        "checks": checks,
    }


orders = [check_order(r) for r in range(2, 8)]
failures = [f"r={row['r']}: {name}" for row in orders
            for name, passed in row["checks"].items() if not passed]
certificate = {
    "scope": "Finite exact algebra only; universal analytic bounds and M(r) unaudited.",
    "orders": orders,
    "failures": failures,
    "all_checks_pass": not failures,
    "check_count": sum(len(row["checks"]) for row in orders),
    "analytic_thresholds_from_proof_not_verified_by_script": {
        "base_over_reference_at_least": "11/16",
        "absolute_error_over_reference_less_than": "1/8",
        "relative_error_less_than": "2/11",
        "target_relative_error_less_than": "1/2",
    },
}
destination = Path(__file__).with_suffix(".json")
destination.write_text(json.dumps(certificate, indent=2) + "\n")
print(f"Finite exact checks: {certificate['check_count']}; failures: {len(failures)}")
print("r=2..7: actual/required pure signed ratio=1/1; confluent determinant=1/1")
for row in orders:
    norms = list(map(F, row["actual"]["coefficient_norms"]))
    print(f"r={row['r']}: max coefficient norm {max(norms)} <= "
          f"{row['required']['coefficient_norm_at_most']}")
print("Reciprocal parity identities: " + ("PASS" if not failures else "FAIL"))
print("Universal analytic estimates and M(r): NOT verified by these finite checks")
print(f"Certificate: {destination.relative_to(Path.cwd())}")
if failures:
    print("Failures: " + "; ".join(failures))
    raise SystemExit(1)
