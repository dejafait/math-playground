#!/usr/bin/env python3
"""Exact rational checks for the step316 proof; no numerical kernel fitting."""

import json
from fractions import Fraction as F
from pathlib import Path


def entry(actual, required, relation="<"):
    ok = actual < required if relation == "<" else actual <= required
    return {
        "actual": str(actual),
        "required": str(required),
        "relation": relation,
        "pass": ok,
    }


root_distance = F(1, 31) + F(5, 16)
root_denominator = 2 - F(25, 512)
exponent_abs = F(3, 16) + F(9, 16) * F(11, 10)
exponent_real = F(11, 10) / 48 - F(1, 16)
ratio = (exponent_abs + root_distance) / root_denominator
q = F(3, 5)
derivative_factor = F(7, 4) * q + F(1, 2) / root_denominator
main_constant = 128 / q / (1 - F(7, 24))
total_constant = F(320 + 9, 21 * 22) + 32 + 18

checks = {
    "root_distance": entry(root_distance, F(7, 20)),
    "root_denominator": entry(F(19, 10), root_denominator),
    "exponent_abs": entry(exponent_abs, F(129, 160), "<="),
    "exponent_real": entry(exponent_real, F(-19, 480), "<="),
    "root_ratio": entry(ratio, q),
    "polynomial_derivative_factor": entry(derivative_factor, F(2)),
    "main_constant": entry(main_constant, F(320)),
    "upper_base": entry(2 * q**2, F(1)),
    "main_decay_comparison": entry(F(3, 16), F(7, 24)),
    "reflected_decay_comparison": entry(F(3, 16), F(7, 8)),
    "total_constant": entry(total_constant, F(64)),
}

failures = [name for name, value in checks.items() if not value["pass"]]
certificate = {
    "status": "PASS" if not failures else "FAIL",
    "scope": (
        "Exact rational inequalities used in C997b for integer n>=20, "
        "k=2n. This checks constants only; the coefficient identity, "
        "quartet decomposition and all-n proof are in the canonical lemma."
    ),
    "kernel_samples": False,
    "checks": checks,
    "failures": failures,
    "conclusion": {
        "selected_response_upper_bound": "64*(n+2)*exp(-3*n/16)*raw_TV",
        "normalized_TV_lower_bound": "exp(3*n/16)/(64*(n+2))",
        "required_TV": "For every epsilon>0, C_epsilon*exp(epsilon*n)",
        "qualification": "This Chebyshev atomic family only; not all measures.",
    },
}
path = Path(__file__).with_suffix(".json")
path.write_text(json.dumps(certificate, indent=2) + "\n", encoding="utf-8")
print(f"Exact rational checks: {certificate['status']}; failures={failures}")
print(f"Root ratio actual={ratio}; required < {q}")
print(f"Total constant actual={total_constant}; required < 64")
print("Normalized TV >= exp(3*n/16)/(64*(n+2)); required subexponential")
print(f"Certificate: {path.relative_to(Path.cwd())}")
raise SystemExit(bool(failures))
