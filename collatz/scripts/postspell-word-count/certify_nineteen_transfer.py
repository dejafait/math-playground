#!/usr/bin/env python3
"""Exact support for L047's fixed-comparison obstruction, not cycle feasibility."""
import json
from fractions import Fraction as F
from pathlib import Path

q = F(48, 25)
R = sum((q**j for j in range(19)), F(0))
R_closed = F(48**19 - 25**19, 23 * 25**18)
A = F(399, 5) * R
C = 338460000
M = 225640000
Nstar = 370000000
T = 1000000000
lower_rhs = (F(399, 5) * 19 + 54) * 250000
upper_rhs = 21 * F(399, 5) * 300000 + 72 * 300000 + 2
checks = []


def check(name, actual, relation, required):
    actual, required = F(actual), F(required)
    passed = {"<": actual < required, ">": actual > required,
              "=": actual == required}[relation]
    checks.append({"name": name, "actual": str(actual),
                   "relation": relation, "required": str(required),
                   "passed": passed})


check("geometric closed-form agreement", R, "=", R_closed)
check("geometric lower bound", R, ">", 250000)
check("geometric upper bound", R, "<", 300000)
check("e tail upper bound", F(8, 3) + F(5, 96), "=", F(87, 32))
check("e upper comparison", F(87, 32), "<", F(11, 4))
check("log Nstar greater than 19", 11**19, "<", Nstar * 4**19)
check("scalar witness above coarse threshold", Nstar, ">", C)
check("scalar witness above stronger sourced count-ray start", Nstar, ">", F(8, 5) * M)
check("scalar witness satisfies assembled upper inequality", lower_rhs, ">", Nstar)
check("positive derivative throughout coarse ray", A, "<", C)
check("e lower comparison", F(163, 60), ">", F(27, 10))
check("log19 less than 3", 27**3, ">", 19 * 10**3)
check("logT less than 21", 27**21, ">", T * 10**21)
check("tail upper bound", F(69 * 19, 1034), "<", 2)
check("eventual upper comparison", upper_rhs, "<", T)

failures = [record for record in checks if not record["passed"]]
certificate = {
    "lemma": "L047", "kind": "exact arithmetic for failed fixed scalar comparison",
    "q": str(q), "R19": str(R), "A": str(A),
    "C": C, "M": M, "Nstar": Nstar, "T": T,
    "witness_rhs_strict_lower_bound": str(lower_rhs),
    "witness_positive_margin": str(lower_rhs - Nstar),
    "eventual_rhs_strict_upper_bound": str(upper_rhs),
    "eventual_positive_margin": str(T - upper_rhs),
    "checks": checks, "failures": failures,
    "scope": "Scalar N bound only; not simultaneous constraints, actual words, integer closure, or cycle feasibility. Analytic justification is in L047.",
}
path = Path(__file__).with_name("nineteen-transfer-certificate.json")
path.write_text(json.dumps(certificate, indent=2) + "\n")
print(f"checks={len(checks)}, failures={len(failures)}")
print(f"250000 < R19={R} < 300000; A={A} < C={C}")
print(f"at Nstar={Nstar}, RHS > {lower_rhs}; exclusion requires RHS <= {Nstar}; excess > {lower_rhs-Nstar}")
print(f"at T={T}, RHS < {upper_rhs}; margin > {T-upper_rhs}")
print(f"certificate: {path.relative_to(Path.cwd())}")
if failures:
    print(failures)
    raise SystemExit(1)
