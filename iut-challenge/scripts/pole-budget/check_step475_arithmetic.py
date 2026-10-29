"""Exact constant checks for L116; not a check of actual-family pole costs."""
from fractions import Fraction
import json
from pathlib import Path


def check(name, actual, relation, required):
    passed = actual > required if relation == ">" else actual < required
    return {"name": name, "actual": str(actual), "relation": relation,
            "required": str(required), "passed": passed}


checks = [
    check("e lower bound cubed exceeds 20", Fraction(163, 60)**3, ">", 20),
    check("exp(72) lower bound exceeds log-bound argument",
          20**24, ">", 6635520 * 10**24),
    check("residual-to-height coefficient bound",
          Fraction(3 * 3317760 * 72, 10**12), "<", Fraction(1, 1000)),
    check("e lower bound squared exceeds 3", Fraction(163, 60)**2, ">", 3),
    check("minimum height makes 60 smaller than H/1000", 60, "<", 10**21),
]
failures = [item["name"] for item in checks if not item["passed"]]
certificate = {
    "result": "PASS" if not failures else "FAIL",
    "scope": "Exact constants in L116's analytic proof only.",
    "limitations": "No actual member, pole-cost lower bound, or IUT claim is verified.",
    "checks": checks,
    "failures": failures,
}
output = Path(__file__).with_name("step475-arithmetic-certificate.json")
output.write_text(json.dumps(certificate, indent=2) + "\n")
print(f"{certificate['result']}: {len(checks)} exact checks; failures={failures}; {output}")
print("Residual coefficient actual=716636160/10^12; required <1/1000.")
raise SystemExit(bool(failures))
