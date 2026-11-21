#!/usr/bin/env python3
"""Check C048c's saved rational evidence and reconstruct its constant bounds.

This checks fixed coefficients only. The uniform analytic audit is in C048c.
"""
from fractions import Fraction as F
from pathlib import Path
import json


def read_fraction(value):
    return F(int(value["numerator"]), int(value["denominator"]))


def save_fraction(value):
    return {"numerator": str(value.numerator),
            "denominator": str(value.denominator)}


source = Path(__file__).with_name("local_constants_1628.json")
old = json.loads(source.read_text())
checks = []


def check(name, actual, relation, required):
    actual, required = F(actual), F(required)
    passed = {"<": actual < required, "<=": actual <= required,
              ">": actual > required, "=": actual == required}[relation]
    checks.append({"name": name, "actual": save_fraction(actual),
                   "relation": relation, "required": save_fraction(required),
                   "passed": passed})


check("saved_comparison_count", len(old["checks"]), "=", 16)
for item in old["checks"]:
    check(item["name"], read_fraction(item["actual"]), item["relation"],
          read_fraction(item["required"]))

roots = {}
for name, expected in (("sqrt6", F(6)), ("sqrt39_over10", F(39, 10)),
                       ("sqrt799_over300", F(799, 300))):
    item = old["roots"][name]
    lower, upper = read_fraction(item["lower"]), read_fraction(item["upper"])
    check(name + "_radicand", read_fraction(item["radicand"]), "=", expected)
    check(name + "_positive", lower, ">", 0)
    check(name + "_ordered", lower, "<", upper)
    check(name + "_lower_square", lower**2, "<=", expected)
    check(name + "_upper_square", upper**2, ">", expected)
    roots[name] = (lower, upper)

x, y = F(39, 10), F(799, 300)
lo6, hi6 = roots["sqrt6"]
lox, hix = roots["sqrt39_over10"]
loy, hiy = roots["sqrt799_over300"]
lower = lo6 * (F(13)/(288*x*hix) + F(33)/(24*x**2*hix)
               + F(15)/(y**3*hiy))
upper = hi6 * (F(13)/(288*x*lox) + F(33)/(24*x**2*lox)
               + F(15)/(y**3*loy))
required = F(659107, 500000)
check("reconstructed_lower", lower, "=", read_fraction(old["A_loc"]["lower"]))
check("reconstructed_upper", upper, "=", read_fraction(old["A_loc"]["upper"]))
check("constant_enclosure_ordered", lower, "<", upper)
check("required_constant", read_fraction(old["A_loc"]["required_strict_upper"]),
      "=", required)
check("target_ceiling", upper, "<", required)
check("reconstructed_slack", required-upper, "=",
      read_fraction(old["A_loc"]["upper_slack"]))
check("strict_margin", required-upper, ">", F(39, 125000000))
check("absorption_coefficient", F(39, 10)-F(371, 300), "=", F(799, 300))
check("saved_absorption_coefficient",
      read_fraction(old["absorbed_curvature_coefficient"]), "=", F(799, 300))

failures = [item["name"] for item in checks if not item["passed"]]
result = {"scope": "Saved exact arithmetic only; no sector grid or analytic proof.",
          "source": str(source.relative_to(Path.cwd())),
          "checks": checks,
          "A_loc": {"lower": save_fraction(lower), "upper": save_fraction(upper),
                    "required_strict_upper": save_fraction(required),
                    "slack": save_fraction(required-upper),
                    "certified_strict_margin": save_fraction(F(39, 125000000))},
          "failures": failures}
destination = Path(__file__).with_suffix(".json")
destination.write_text(json.dumps(result, indent=2)+"\n")
print(f"Exact evidence checks: {len(checks)}; failures: {failures}")
print(f"A_loc upper (decimal display): {float(upper):.15f}; required <1.318214")
print("Exact slack >0.000000312: " + str(required-upper > F(39, 125000000)))
print(f"Certificate: {destination.relative_to(Path.cwd())}")
if failures:
    raise SystemExit(1)
