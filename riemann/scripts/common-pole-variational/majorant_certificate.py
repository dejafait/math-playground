#!/usr/bin/env python3
"""Exact rational assembly for L528; analytic hypotheses remain in its proof."""
from fractions import Fraction as F
import json
from pathlib import Path


def record(name, actual, relation, required):
    passed = actual < required if relation == "<" else actual > required
    return {
        "name": name,
        "actual": str(actual),
        "relation": relation,
        "required": str(required),
        "passed": passed,
    }


atan_lower = F(1, 2) - F(1, 24) + F(1, 160) - F(1, 896) + F(1, 3) - F(1, 81)
cos_upper = 1 - F(25, 32) + F(625, 6144)
pi_lower = F(47, 15)
mu_upper = F(49, 20) / pi_lower
quarter_pi_lower = F(47, 60)
checks = [
    record("atan lower sum exceeds quarter-pi comparator", atan_lower, ">", quarter_pi_lower),
    record("cosine upper polynomial", cos_upper, "<", F(1, 3)),
    record("exponential lower bound exceeds square-root requirement", F(8, 3), ">", F(13, 5)),
    record("cosine argument within half-pi", F(5, 4), "<", pi_lower / 2),
    record("majorant mean bound below threshold lower bound", mu_upper, "<", quarter_pi_lower),
    record("strict uniform gap positive", quarter_pi_lower - mu_upper, ">", F(0)),
]
certificate = {
    "lemma": "L528",
    "scope": "Exact rational assembly only; analytic inequalities and Fourier-series Parseval are proved in the lemma.",
    "atan_lower": str(atan_lower),
    "atan_margin": str(atan_lower - quarter_pi_lower),
    "cosine_upper": str(cos_upper),
    "mean_upper_strict": str(mu_upper),
    "threshold_lower_strict": str(quarter_pi_lower),
    "uniform_gap_lower_strict": str(quarter_pi_lower - mu_upper),
    "checks": checks,
    "failures": [c["name"] for c in checks if not c["passed"]],
}
path = Path(__file__).with_name("majorant-certificate.json")
path.write_text(json.dumps(certificate, indent=2) + "\n")
print(f"L528: actual uniform upper <{mu_upper}; required <pi/4; pi/4>{quarter_pi_lower}")
print(f"Strict gap >{quarter_pi_lower - mu_upper}; checks={len(checks)}; failures={certificate['failures']}")
print(f"Full certificate: {path.relative_to(Path.cwd())}")
if certificate["failures"]:
    raise SystemExit(1)
