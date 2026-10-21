#!/usr/bin/env python3
"""Exact arithmetic supporting L046; analytic implications are proved there."""
import json
from fractions import Fraction as F
from pathlib import Path

q = F(48, 25)
R = sum((q**j for j in range(18)), F(0))
C = 338460000
A = 11970000
B = 10800002
checks = []


def lt(name, actual, required):
    actual, required = F(actual), F(required)
    checks.append({"name": name, "actual": str(actual),
                   "required_strict_upper_bound": str(required),
                   "passed": actual < required})


lt("shift constant", F(32, 75) + 1, q)
lt("sixth power integer comparison", 48**6, 51 * 25**6)
lt("geometric bound via sixth power", F(25 * (51**3 - 1), 23), 150000)
lt("full exact geometric sum", R, 150000)
lt("e series lower bound reciprocal comparison", F(27, 10), F(163, 60))
lt("log18 less than 3", 18 * 10**3, 27**3)
lt("logC less than 20", C * 10**20, 27**20)
lt("tail contribution", F(69 * 18, 1034), 2)
lt("derivative threshold", A, C)
lt("entire-ray starting bound", 20 * A + B, C)

certificate = {
    "lemma": "L046", "kind": "exact rational arithmetic, not a proof audit",
    "q": str(q), "R18": str(R), "C": C, "A": A, "B": B,
    "checks": checks, "failures": [c for c in checks if not c["passed"]],
    "analytic_scope": "L046 proves real-height transfer and all-real monotonicity; no finite parameter screen",
}
path = Path(__file__).with_name("eighteen-height-certificate.json")
path.write_text(json.dumps(certificate, indent=2) + "\n")
print(f"checks={len(checks)}, failures={len(certificate['failures'])}")
print(f"R18={R} < 150000; A={A} < C={C}")
print(f"length RHS at C < {20*A+B}; required < {C}; margin={C-(20*A+B)}")
print(f"certificate: {path.relative_to(Path.cwd())}")
if certificate["failures"]:
    print(certificate["failures"])
    raise SystemExit(1)
