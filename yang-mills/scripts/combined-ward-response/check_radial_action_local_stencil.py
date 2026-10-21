"""Exact constant-displacement inversion check for L009's d C_u stencil."""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
import json
from pathlib import Path


def shift(x, direction, amount):
    y = list(x)
    y[direction] += amount
    return tuple(y)


def clover(x, rho, nu):
    if rho == nu:
        return {}
    plane = tuple(sorted((rho, nu)))
    sign = 1 if rho < nu else -1
    return {(plane, shift(shift(x, rho, s), nu, t)): Fraction(sign, 4)
            for s in (-1, 1) for t in (-1, 1)}


def link_contraction(x, nu, rho):
    row = defaultdict(Fraction)
    for endpoint in (x, shift(x, nu, 2)):
        for key, value in clover(endpoint, rho, nu).items():
            row[key] += value / 2
    return row


def curl_row(mu, nu, rho):
    x = (0, 0, 0, 0)
    row = defaultdict(Fraction)
    for start, component, sign in ((shift(x, mu, 2), nu, 1),
                                    (x, nu, -1),
                                    (shift(x, nu, 2), mu, -1),
                                    (x, mu, 1)):
        for key, value in link_contraction(start, component, rho).items():
            row[key] += sign * value
    return {key: value for key, value in row.items() if value}


def main():
    checks = []
    for mu, nu in combinations(range(4), 2):
        center = shift(shift((0, 0, 0, 0), mu, 1), nu, 1)
        for rho in range(4):
            row = curl_row(mu, nu, rho)
            failures = []
            for (plane, position), value in row.items():
                reflected = tuple(2 * c - x for c, x in zip(center, position))
                if row.get((plane, reflected), 0) != -value:
                    failures.append([plane, position, str(value)])
            checks.append({"output_plane": [mu, nu], "displacement": rho,
                           "nonzero_entries": len(row),
                           "row_l1_at_a_1": str(sum(map(abs, row.values()))),
                           "failures": failures})
    artifact = Path(__file__).with_name("radial-action-local-stencil-certificate.json")
    artifact.write_text(json.dumps({"coordinate_unit": "a/2", "checks": checks,
                                   "scope": "Exact stencil parity only; boundary and asymptotic bounds are proved in L024."}, indent=2) + "\n")
    failed = sum(bool(check["failures"]) for check in checks)
    print(f"Constant-displacement inversion: {len(checks) - failed}/{len(checks)} exact checks pass; failed={failed}.")
    print("Required stencil defect: 0; actual: 0." if not failed else "Nonzero stencil defect: inspect certificate.")
    print(f"Artifact: {artifact.relative_to(Path.cwd())}")
    assert not failed


if __name__ == "__main__":
    main()
