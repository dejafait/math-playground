"""Replay only the rational margins of C997p; not an analytic proof audit."""
from fractions import Fraction as F
import json
from pathlib import Path


def frac(x):
    return {"numerator": x.numerator, "denominator": x.denominator}


checks = []


def check(name, actual, relation, required):
    passed = {"<": actual < required, "<=": actual <= required,
              "=": actual == required}[relation]
    checks.append({"name": name, "actual": frac(actual), "relation": relation,
                   "required": frac(required), "passed": passed})
    print(f"{name}: {actual} {relation} {required}: {'PASS' if passed else 'FAIL'}")


radius = F(1, 112)
check("saddle log argument", 64 * radius**2, "=", F(1, 196))
check("log series bound", F(1, 196) / (1 - F(1, 196)), "=", F(1, 195))
check("rate loss", F(9, 896) + F(1, 195), "<", F(1, 64))
check("whole rectangle q disk", 2 * (F(1, 8) + radius) / F(15, 8), "=", F(1, 7))
check("q real part squared", F(4, 9), "<", F(6, 7))
check("saddle q difference", F(1, 223), "<", radius)
check("nonvanishing error", 5 * radius, "<", F(1, 16))
outer = F(3, 4) + 16 * radius + 64 * radius**2
check("horizontal outer bound", outer, "=", F(44, 49))
check("vertical bound", 16 * radius + 64 * radius**2, "=", F(29, 196))
check("vertical versus outer", F(29, 196), "<", outer)
check("outer rate", F(17, 64) - F(5, 49), "<", F(13, 64))
check("central log argument", F(1, 4) + 64 * radius**2, "=", F(25, 98))
check("central radius", F(25, 98), "<", F(1, 3))
r = F(1, 3)
check("curvature numerator", 1-r-3*r*r-r**3, "=", F(8, 27))
check("curvature ratio", F(8, 27) / (1+r)**4, "=", F(3, 32))
check("curvature lower bound", 128 * F(3, 32), "=", F(12))
check("saddle inside center", radius, "<", F(1, 16))
check("correction versus chosen rho", F(13, 64), "<", F(7, 32))
check("chosen rho versus rate floor", F(7, 32), "<", F(15, 64))

certificate = {
    "step": 359, "claim": "C997p rational margins only",
    "method": "exact fractions; no floating-point or sampling",
    "analytic_proof_verified": False,
    "checks": checks,
    "failures": [c["name"] for c in checks if not c["passed"]],
    "all_passed": all(c["passed"] for c in checks),
}
path = Path(__file__).with_suffix(".json")
path.write_text(json.dumps(certificate, indent=2) + "\n")
print(f"Full certificate: {path}; failures: {certificate['failures']}")
raise SystemExit(0 if certificate["all_passed"] else 1)
