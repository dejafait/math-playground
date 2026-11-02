#!/usr/bin/env python3
"""Exact finite certificates for the half-turn phase-census contour test.

Floating point chooses proposed factor bounds only. Every accepted bound
is then certified on the full interval by exact rational arithmetic.
"""
from fractions import Fraction as F
from pathlib import Path
from math import ceil, sqrt
import importlib.util
import json

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    "factor_arithmetic", HERE / "logarithmic-amplitude-factor-certificate.py")
arith = importlib.util.module_from_spec(spec)
spec.loader.exec_module(arith)


def choose_bound(t):
    """Proposal only; the exact Bernstein test supplies all evidence."""
    t, d, U = float(t), 1.25, 121 / 64
    peak = 1.0
    for j in range(4097):
        c = -1 + j / 2048
        s2 = 1 - c * c
        n0 = d * d + t * t + 2 * d * t * c
        d0 = U * U + d * d * t * t + 2 * U * d * t * c
        det_n = (d + t * c) ** 2
        det_d = t * t * (U * c + d * t) ** 2
        middle = t * t * n0 + d0 - 2 * U * t * t * s2
        eigen = (middle + sqrt(max(0, middle * middle - 4 * det_n * det_d))) / (2 * det_n)
        peak = max(peak, eigen * n0 / d0)
    return F(ceil(peak * 10000) + 2, 10000)


def atan_small_lower(z):
    assert 0 <= z <= F(1, 2)
    return sum(((-1) ** k * z ** (2 * k + 1) / (2 * k + 1)
                for k in range(8)), F(0))


def atan_lower(z):
    if z <= F(1, 2):
        return atan_small_lower(z)
    if z <= 1:
        return atan_small_lower(F(1, 2)) + atan_small_lower((z - F(1, 2)) / (1 + z / 2))
    return (atan_small_lower(F(1, 2)) + atan_small_lower(F(1, 3))
            + atan_small_lower((z - 1) / (z + 1)))


def main():
    d, U, Y = F(5, 4), F(121, 64), F(27, 100)
    checks, failures = [], []
    rate = F(0)
    for j in range(1, 129):
        t, L = F(j, 128), choose_bound(F(j, 128))
        N0, D0 = [d * d + t * t, 2 * d * t], [U * U + d * d * t * t, 2 * U * d * t]
        A = arith.add(arith.scale(D0, L), arith.scale(N0, -t * t))
        C = arith.scale(arith.mul(D0, N0), L - 1)
        middle = arith.add(arith.scale(D0, L), arith.scale(N0, -U))
        determinant = arith.add(arith.mul(A, C), arith.scale(
            arith.mul([F(1), F(0), F(-1)], arith.mul(middle, middle)), -t * t))
        cells, bad, covered = arith.positive_cover(determinant)
        failures.extend({"t": str(t), "detail": item} for item in bad)
        if not covered:
            failures.append({"t": str(t), "failure": "incomplete interval cover"})
        e = L - 1
        if not 0 < e < 1:
            failures.append({"t": str(t), "failure": "log-series range"})
        log_upper = (e - e * e / 2 + e * e * e / 3) / 2
        rate += log_upper / 128
        checks.append({"t": str(t), "squared_factor_bound": str(L),
                       "determinant_power_coefficients": list(map(str, determinant)),
                       "cells": cells, "full_interval_covered": covered,
                       "minimum_bernstein_coefficient": str(min(F(cell["minimum"]) for cell in cells)),
                       "half_log_upper": str(log_upper)})

    phase_rows = []
    phase_lower = F(0)
    for j in range(128):
        t = F(j, 128)
        args = [Y / (d - t), t * Y / (U - d * t)]
        raw = [atan_lower(z) for z in args]
        rounded = [F((value * 10 ** 12).__floor__(), 10 ** 12) for value in raw]
        phase_lower += sum(rounded, F(0)) / 128
        phase_rows.append({"t": str(t), "atan_arguments": list(map(str, args)),
                           "raw_lower_bounds": list(map(str, raw)),
                           "rounded_lower_bounds": list(map(str, rounded))})
    phase_margin = phase_lower - F(11, 21)
    onset = int(4 // phase_margin) + 1 if phase_margin > 0 else None
    margins = {
        "factor_rate_actual": str(rate),
        "factor_rate_required_strict_upper": "91/5000",
        "factor_rate_margin": str(F(91, 5000) - rate),
        "factor_additive_actual": str(128 * rate),
        "factor_additive_required_strict_upper": "3",
        "factor_additive_margin": str(3 - 128 * rate),
        "phase_integral_lower": str(phase_lower),
        "phase_required_upper_for_pi_over_6": "11/21",
        "phase_margin": str(phase_margin),
        "valid_onset_for_n": onset,
        "pole_radius_squared_margin": str(F(273, 200) ** 2 - d * d - Y * Y),
        "endpoint_log_rate": str(Y * Y / 2 * F(16, 45)),
        "endpoint_additive": str(Y * Y / 2 * F(16, 25)),
        "scaled_cost_growth_rate": str(F(1, 32) - F(91, 5000) - F(81, 6250)),
        "phase_derivative_endpoint_A_min_margin": str(F(4, 5) / (1 + F(4, 5) ** 2 * Y ** 2) - F(3, 4)),
        "phase_derivative_endpoint_A_max_margin": str(4 / (1 + 16 * Y ** 2) - F(3, 4)),
        "phi_second_derivative_upper": "320/9",
        "phi_second_derivative_required_upper": "36",
        "local_phi_prime_lower_margin_at_n5": str(F(3, 4) * 5 - F(36, 100) - F(5, 2)),
        "local_exponential_argument_upper": "16/75",
        "local_exponential_bound_via_geometric": str(1 / (1 - F(16, 75))),
    }
    if not rate < F(91, 5000) or not 128 * rate < 3:
        failures.append({"failure": "factor envelope rate/additive"})
    if not phase_margin > 0:
        failures.append({"failure": "phase endpoint below rational cap unproved"})
    for name in ["pole_radius_squared_margin", "scaled_cost_growth_rate",
                 "phase_derivative_endpoint_A_min_margin", "phase_derivative_endpoint_A_max_margin",
                 "local_phi_prime_lower_margin_at_n5"]:
        if F(margins[name]) <= 0:
            failures.append({"failure": name})
    if not F(margins["endpoint_additive"]) < 1 or not F(margins["local_exponential_bound_via_geometric"]) < 2:
        failures.append({"failure": "local additive or exponential constant"})
    certificate = {"kind": "EXACT_RATIONAL_CERTIFICATE",
                   "scope": "Full factor intervals and rational phase/cost constants; analytic contour identity and interpretation require the canonical proof.",
                   "factor_checks": checks, "phase_riemann_rows": phase_rows,
                   "comparisons": margins, "failures": failures}
    path = Path(__file__).with_suffix(".json")
    path.write_text(json.dumps(certificate, indent=2) + "\n")
    print(f"Factor intervals certified: {sum(v['full_interval_covered'] for v in checks)}/128; cells: {sum(len(v['cells']) for v in checks)}")
    print(f"Log rate actual {float(rate):.12g}, required < .0182, passed {rate < F(91, 5000)}; additive {float(128 * rate):.12g}, required < 3")
    print(f"Phase integral lower {float(phase_lower):.12g} > required 11/21; onset n>={onset}")
    print(f"Endpoint rate actual {margins['endpoint_log_rate']}; allowed comparison rate 261/20000; gap {margins['scaled_cost_growth_rate']}")
    print(f"Failures: {len(failures)}; full certificate: {path}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
