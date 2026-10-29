#!/usr/bin/env python3
"""Exact-rational diagnostics for L297's frozen weighted bulk tensor.

This checks selected Fourier points, not the integral or the theorem.
The complete values are saved beside this script as a JSON certificate.
"""

from fractions import Fraction as F
import json
from pathlib import Path


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(4))
             for j in range(4)] for i in range(4)]


def check(ts, rho, mu):
    d = [4 * t / (1 + t * t) for t in ts]
    c = [(1 - t * t) / (1 + t * t) for t in ts]
    lam = sum(x * x for x in d)
    delta = rho - 1
    v = [-d[1], d[0], F(0), F(0)]
    kap = lam + delta * (d[0] ** 2 + d[1] ** 2)
    g = [[(F(i == j) - d[i] * d[j] / lam) / lam
          - delta * v[i] * v[j] / (lam * kap)
          for j in range(4)] for i in range(4)]
    h = [[F(0) for _ in range(4)] for _ in range(4)]
    quartic = F(0)
    for nu in range(4):
        if nu == mu:
            continue
        w = rho if {mu, nu} == {0, 1} else F(1)
        h[nu][nu] += c[mu] * w * d[mu]
        h[mu][nu] -= c[mu] * w * d[nu] / 2
        h[nu][mu] -= c[mu] * w * d[nu] / 2
        quartic += w * (-d[nu] ** 2 * g[mu][mu] / 12
                        + (1 - d[mu] ** 2 / 2) * g[nu][nu]
                        + d[mu] * d[nu] * g[mu][nu] / 3)
    hg = matmul(h, g)
    cubic = 2 * sum(hg[i][j] * hg[j][i]
                    for i in range(4) for j in range(4))
    density = -F(1, 12) - d[mu] ** 2 / (6 * lam)
    density -= (d[mu] * c[mu]) ** 2 / lam ** 2
    actual = density + cubic - quartic
    k_mu = rho if mu < 2 else F(1)
    lam_first = 2 * d[mu] * c[mu]
    lam_second = 2 - d[mu] ** 2
    required = -(lam_second / lam - lam_first ** 2 / lam ** 2
                 + k_mu * lam_second / kap
                 - k_mu ** 2 * lam_first ** 2 / kap ** 2) / 2
    return {
        "half_angle_parameters": [str(t) for t in ts],
        "rho": str(rho), "direction": mu + 1,
        "density": str(density), "cubic_over_four": str(cubic),
        "quartic_over_four": str(quartic),
        "actual_complete_integrand": str(actual),
        "required_negative_half_log_determinant_hessian": str(required),
        "difference": str(actual - required),
        "passed": actual == required,
    }


def main():
    points = [
        [F(1, 3), F(1, 4), F(-1, 5), F(1, 7)],
        [F(2, 3), F(-3, 5), F(1, 2), F(-2, 7)],
        [F(0), F(1, 5), F(0), F(1, 3)],
        [F(1, 2), F(0), F(0), F(0)],
    ]
    cases = [check(ts, rho, mu) for ts in points
             for rho in [F(1, 2), F(2, 3), F(1), F(4, 3), F(3, 2)]
             for mu in range(4)]
    failures = [i for i, case in enumerate(cases) if not case["passed"]]
    max_error = max(abs(F(case["difference"])) for case in cases)
    result = {
        "scope": "Exact arithmetic at selected Fourier points only; not a proof.",
        "required_difference": "0", "case_count": len(cases),
        "maximum_absolute_difference": str(max_error),
        "failure_indices": failures, "cases": cases,
    }
    path = Path(__file__).with_name("symbol-certificate.json")
    path.write_text(json.dumps(result, indent=2) + "\n")
    print(f"Exact symbol diagnostics: {len(cases) - len(failures)}/{len(cases)} passed")
    print(f"Actual maximum absolute difference: {max_error}; required: 0")
    print(f"Failures: {failures}")
    print(f"Full certificate: {path}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
