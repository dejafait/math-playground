#!/usr/bin/env python3
"""Finite L966 audit: exact replay and an independent formal-log recurrence.

The all-n proof and convergence audit remain in L966. No sign is tested.
"""

from fractions import Fraction as F
from importlib.util import module_from_spec, spec_from_file_location
from math import factorial
from pathlib import Path
import json


def add_scaled(target, source, scale):
    for exponent, coefficient in source.items():
        target[exponent] = target.get(exponent, F(0)) + scale * coefficient
        if not target[exponent]:
            del target[exponent]


def times_variable(polynomial, index):
    result = {}
    for exponent, coefficient in polynomial.items():
        new = list(exponent)
        new[index] += 1
        result[tuple(new)] = coefficient
    return result


def partitions(weight, slots):
    if slots == 0:
        if weight == 0:
            yield ()
        return
    for count in range(weight // slots + 1):
        for prefix in partitions(weight - slots * count, slots - 1):
            yield prefix + (count,)


def serialize(poly):
    return [{"exponent": list(exponent), "coefficient": str(coefficient)}
            for exponent, coefficient in sorted(poly.items())]


def bell_checks(max_order=8):
    # With f(z)=1+sum a_r z^r and log f=sum g_k z^k,
    # f*(log f)'=f' gives k*g_k=k*a_k-sum_{i<k} i*g_i*a_{k-i}.
    # Treat the a_r as algebraically independent, not sampled theta moments.
    logarithm = [{}]
    cases = []
    for k in range(1, max_order + 1):
        unit = [0] * max_order
        unit[k - 1] = 1
        actual = {tuple(unit): F(1)}
        for i in range(1, k):
            add_scaled(actual, times_variable(logarithm[i], k - i - 1), F(-i, k))
        logarithm.append(actual)
        expected = {}
        for m in partitions(k, k):
            ell = sum(m)
            denominator = 1
            for value in m:
                denominator *= factorial(value)
            expected[m + (0,) * (max_order - k)] = F(
                (-1)**(ell - 1) * factorial(ell - 1), denominator)
        residual = dict(actual)
        add_scaled(residual, expected, F(-1))
        cases.append({
            "k": k,
            "normalization": "a_r=F^(r)/(r!*F); g_k=(log F)^(k)/k!",
            "recurrence_coefficients": serialize(actual),
            "partition_coefficients": serialize(expected),
            "residual_coefficients": serialize(residual),
            "max_abs_residual": str(max(map(abs, residual.values()), default=F(0))),
            "required_residual": "0",
        })
    return cases


def main():
    here = Path(__file__).resolve().parent
    spec = spec_from_file_location("construction165", here / "regularized-resolvent-check-165.py")
    construction = module_from_spec(spec)
    spec.loader.exec_module(construction)
    # Importing check avoids rewriting the earlier certificate or calling main.
    replay = [construction.check(n) for n in range(1, 13)]
    saved = json.loads((here / "regularized-resolvent-check-165.json").read_text())
    bell = bell_checks()
    failures = []
    if replay != saved["cases"]:
        failures.append("rational replay differs from saved full cases")
    for case in replay:
        failures.extend(f"n={case['n']}: {failure}" for failure in case["failures"])
    for case in bell:
        if case["residual_coefficients"]:
            failures.append(f"Bell recurrence residual at k={case['k']}")
    summary = {
        "rational_cases_replayed": len(replay),
        "saved_full_cases_match": replay == saved["cases"],
        "max_rational_residual": str(max(F(c["max_abs_polynomial_residual"]) for c in replay)),
        "max_residue_error": str(max(abs(F(c["residue_cancellation_error"])) for c in replay)),
        "all_D_and_d_positive": all(F(v) > 0 for c in replay
                                     for key in ("D_coefficients", "d_coefficients_k_1_to_n")
                                     for v in c[key]),
        "formal_log_orders_checked": len(bell),
        "max_formal_log_residual": str(max(F(c["max_abs_residual"]) for c in bell)),
        "required_residuals": "0",
        "required_coefficient_sign": ">0",
        "failures": failures,
    }
    certificate = {
        "scope": "Exact finite audit only; no all-n or analytic-convergence certificate and no theta sign estimate",
        "arithmetic": "fractions.Fraction; sparse formal polynomials; no floating point",
        "summary": summary,
        "rational_replay": replay,
        "formal_log_checks": bell,
    }
    path = Path(__file__).with_suffix(".json")
    path.write_text(json.dumps(certificate, indent=2) + "\n")
    print("Rational replay: 12 full cases; saved cases match:", summary["saved_full_cases_match"])
    print("Polynomial/residue residuals: actual", summary["max_rational_residual"],
          summary["max_residue_error"], "; required 0, 0")
    print("All D,d positive:", summary["all_D_and_d_positive"], "; required True")
    print("Independent formal-log recurrence: orders 1..8; max residual",
          summary["max_formal_log_residual"], "; required 0")
    print("Failures:", failures)
    print("Full certificate:", path.relative_to(Path.cwd()))
    if failures or not summary["all_D_and_d_positive"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
