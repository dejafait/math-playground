#!/usr/bin/env python3
"""Exact constant checks for L646; the uniform analytic proof is in the lemma."""

from fractions import Fraction as F
import json
from pathlib import Path


checks = []


def check(name, actual, relation, required):
    actual, required = F(actual), F(required)
    passed = {"<": actual < required, "<=": actual <= required,
              "=": actual == required, ">": actual > required,
              ">=": actual >= required}[relation]
    direction = -1 if relation in ("<", "<=") else 1
    checks.append({"name": name, "actual": str(actual),
                   "relation": relation, "required": str(required),
                   "margin": str(direction * (actual - required)),
                   "passed": passed})


h, d, radius, alpha_abs = F(1, 100), F(5, 4), F(11, 8), F(10, 11)
n0 = 50_400_000**2
phase_bound = F(19, 63) * F(100, 99)**2
check("grid radius below anchor", F(1, 1) / radius, "<", alpha_abs)
check("angular derivative at minus one", (1-alpha_abs)/(1+alpha_abs), "=", F(1, 21))
check("single transformed phase at minus one", F(1, 21)*F(19, 3), "=", F(19, 63))
check("arc phase bound", phase_bound, "<", F(5, 16))
check("arc phase derivative bound", 2/(1-h)**4, "<", 3)
check("sqrt21 less than five squared", 21, "<", 25)
check("amplitude derivative L1 bound", 2*5+2*h*50, "=", 11)
check("amplitude L1 bound", 2*h*5, "=", F(1, 10))
check("overlap from pi less than four", 8/(F(31500)*4), "=", F(1, 15750))
check("floor cutoff gap at n=96", F(1, 3)-F(5, 16)-F(1, 96), ">=", F(1, 96))
tail_constant = 242*192+F(8, 3)*96**3
check("Fourier tail sum constant", tail_constant, "=", 2_405_760)
check("Fourier tail square bound", tail_constant, "<", 1600**2)
check("onset square", n0, "=", (3200*15750)**2)
check("onset tail amplitude", F(1600, 50_400_000), "=", F(1, 31500))
check("confluent projection residual", F(1, 15750)-F(1, 31500), "=", F(1, 31500))
check("cluster displacement for n>=5", F(2, 5**3), "<", F(1, 16))
check("cluster physical radius", d+F(1, 16), "=", F(21, 16))
check("cluster required clearance", F(21, 16), "<", radius-F(1, 100))
check("cluster normalized radius", F(21, 16)/radius, "=", F(21, 22))
check("Blaschke difference constant", 4*22*11, "<=", 1000)
check("projection perturbation at n>=200", F(12000, 200**4), "<=", F(1, 63000))
check("distinct projection residual", F(1, 31500)-F(1, 63000), "=", F(1, 63000))
check("onset exceeds perturbation threshold", n0, ">=", 200)
check("resolvent squared denominator", radius**2-F(21, 16)**2, "=", F(43, 256))
check("resolvent norm less than three squared", F(256, 43), "<", 9)
check("anchor rate gap", F(47, 1000)-F(1, 32), "=", F(63, 4000))
check("logarithmic derivative bound", 4+F(64, 37), "<", 6)
check("log ratio bound at n>=5", F(144, 5**6), "<", F(1, 2))
check("resolvent perturbation coefficient", 192+F(128, 5), "<=", 220)
check("full response error at n>=5", F(26400, 5**8), "<", F(1, 2))
check("anchor resolvent exceeds three halves squared", F(64, 21), ">", F(9, 4))

failures = [item["name"] for item in checks if not item["passed"]]
certificate = {
    "lemma": "L646",
    "scope": "Exact constant comparisons only; not an independent verification of the Fourier and projection proof.",
    "onset": n0,
    "actual_phase_bound": str(phase_bound),
    "required_phase_bound": "5/16",
    "actual_rate_lower_bound": "47/1000 (imported from C645n)",
    "required_rate": "1/32",
    "checks": checks,
    "failures": failures,
    "passed": not failures,
}
output = Path(__file__).with_suffix(".json")
output.write_text(json.dumps(certificate, indent=2) + "\n")
print(f"L646 exact comparisons: {len(checks)-len(failures)}/{len(checks)} passed")
print(f"Phase: {phase_bound} < 5/16; rate: lambda > 47/1000 > required 1/32")
print(f"Input norm >= 1/63000 for n >= {n0}; full response >= floor(n/3)")
print(f"Failures: {failures}")
print(f"Certificate: {output.relative_to(Path.cwd())}")
raise SystemExit(bool(failures))
