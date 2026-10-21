#!/usr/bin/env python3
"""Exhaustively audit L025's finite arithmetic; not a packet certificate."""
import json
from pathlib import Path


def add(x, y):
    return ((x[0] + y[0]) % 7, (x[1] + y[1]) % 7)


def mul(x, y):
    return ((x[0] * y[0] + 5 * x[1] * y[1]) % 7,
            (x[0] * y[1] + x[1] * y[0]) % 7)


def power(x, n):
    result = (1, 0)
    for _ in range(n):
        result = mul(result, x)
    return result


def evaluate(x, b, c):
    return add(add(mul(x, x), mul((b, 0), x)), (c, 0))


def main():
    # Transcribed from L016's integer A,B rows, independently of L025's roots.
    inputs = [(14, 1, 57, [(4, 4), (4, 3)]),
              (10, 8, 69, [(4, 1), (4, 6)]),
              (25, -7, 69, [(0, 4), (0, 3)]),
              (15, 5, 33, [(6, 1), (6, 6)])]
    field = [(a, b) for a in range(7) for b in range(7)]
    squares = sorted({a * a % 7 for a in range(7)})
    failures = []
    rows = []
    for r, a, big_b, expected in inputs:
        b, c = -a % 7, (big_b - 58) % 7
        disc = (b * b - 4 * c) % 7
        base_values = [(x * x + b * x + c) % 7 for x in range(7)]
        evaluations = [dict(x=x, value=evaluate(x, b, c)) for x in field]
        roots = [x for x in field if evaluate(x, b, c) == (0, 0)]
        checks = {
            "no_base_root": 0 not in base_values,
            "nonsquare_discriminant": disc not in squares,
            "exact_claimed_roots": sorted(roots) == sorted(expected),
            "root_sum": len(roots) == 2 and add(*roots) == (-b % 7, 0),
            "root_product": len(roots) == 2 and mul(*roots) == (c, 0),
            "frobenius_swaps_roots": len(roots) == 2 and
                power(roots[0], 7) == roots[1] and power(roots[1], 7) == roots[0],
        }
        failures.extend(f"r={r}: {name}" for name, ok in checks.items() if not ok)
        rows.append(dict(r=r, coefficients_constant_first=[c, b, 1],
                         discriminant=disc, F7_values_at_0_through_6=base_values,
                         F49_evaluations=evaluations, roots=roots, checks=checks))
        print(f"r={r}: discriminant={disc}, F7 roots={base_values.count(0)}, "
              f"F49 roots={roots}, all checks={all(checks.values())}")
    path = Path(__file__).with_name("residue-degree-audit.json")
    path.write_text(json.dumps(dict(
        scope="L025 arithmetic only; L020/L024 interfaces audited in prose",
        modulus=7, extension_relation="w^2=5", F7_squares=squares,
        required=dict(rows=4, base_roots_per_row=0, extension_roots_per_row=2),
        actual=dict(rows=len(rows), base_elements_per_row=7, extension_elements_per_row=49),
        rows=rows, failures=failures, passed=not failures), indent=2) + "\n")
    print(f"Actual/required: {len(rows)}/4 rows, 7/7 base and 49/49 extension elements per row")
    print(f"Failures: {failures}; certificate: {path}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
