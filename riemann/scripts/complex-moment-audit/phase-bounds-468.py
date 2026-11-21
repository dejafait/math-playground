"""Exact rational scalar checks for the conditional phase audit (L788).

Run from the active notebook: python3 scripts/complex-moment-audit/phase-bounds-468.py
No sampling of k, z, u or the theta kernel is used. Analytic reductions
and Cauchy/sector domains are proved in L788, not by this certificate.
"""

from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json


def exp_partial(x, n):
    return sum((x**j / factorial(j) for j in range(n + 1)), F(0))


checks = []


def check(name, actual, relation, required):
    actual, required = F(actual), F(required)
    passed = actual < required if relation == "<" else actual > required
    checks.append({
        "name": name,
        "actual_exact": str(actual),
        "required_exact": str(required),
        "relation": relation,
        "passed": passed,
        "actual_decimal_preview": float(actual),
        "required_decimal_preview": float(required),
    })


check("positive series proves exp(6/5)>33/10", exp_partial(F(6, 5), 5), ">", F(33, 10))
check("positive series proves exp(4)>54", exp_partial(F(4), 9), ">", 54)
exponent_floor = 3 * F(25, 8) * F(33, 10) * F(23, 25)
assert exponent_floor == F(2277, 80)
q = F(16) / (54**7 * (1 + exponent_floor - 28))
check("large-tube geometric admissibility", q, "<", 1)
majorant = F(63, 47) * q / (1 - q)
log_majorant = majorant / (1 - majorant)
check("large-tube R majorant", majorant, "<", F(11, 10**12))
check("large-tube logarithm majorant", log_majorant, "<", F(111, 10**13))
check("horizontal second tail derivative", 2 * 20**2 * log_majorant, "<", F(1, 10**8))

rho = F(11, 10**15)
small_log = rho / (1 - rho)
check("small-tube logarithm majorant", small_log, "<", F(12, 10**15))
tail2 = 2 * 25**2 * F(12, 10**15)
tail3 = 6 * 25**3 * F(12, 10**15)

check("horizontal power-sector angle", F(1, 19) + F(2, 7), "<", F(17, 50))
power_floor = F(19, 10) * (1 - F(17, 50)**2 / 2) * F(49, 50)
check("horizontal power curvature factor", power_floor, ">", F(7, 4))
check("horizontal exponential curvature factor", 8 * F(49, 50), ">", F(7, 4))
check("horizontal loss versus floor margin", F(1, 10**8), "<", (F(7, 4) - F(8, 5)) * 252)
check("disk power-sector angle", F(1, 19) + F(1, 12), "<", F(1, 7))
check("exponential upper comparison", F(25, 21), "<", F(6, 5))
lower2 = 8 * F(21, 25) * F(617, 625) - tail2
check("disk normalized curvature lower bound", lower2, ">", F(6633, 1000))
upper2_power = F(21, 10) * F(25, 24)**2
upper2_exp = F(80, 7)
upper2_resolvent = 48 * F(6, 5) * F(25, 21) / (F(83, 100)**2 * 300**2)
upper2 = upper2_power + upper2_exp + upper2_resolvent + tail2
check("disk normalized second derivative", upper2, "<", F(13709, 1000))
check("second derivative versus requested saddle bound", F(13709, 1000), "<", F(14185, 1000))
upper3_power = F(21, 5) * F(25, 24)**3
upper3_exp = F(320, 7)
upper3_resolvent = 192 * F(6, 5) * F(121, 100) * F(25, 21) / (F(83, 100)**3 * 300**2)
upper3 = upper3_power + upper3_exp + upper3_resolvent + tail3
check("disk normalized third derivative ratio", upper3, "<", 51)
check("third derivative versus required bound", 51, "<", 100)

out = {
    "step_id": "2026-11-05-uniform-moment-phase-bounds-audit-468",
    "scope": "Exact rational arithmetic only; analytic proof and conditional hypotheses are in L788.",
    "normalization": "Second derivative and third derivative ratio both divide by H0=1/sigma^2.",
    "checks": checks,
    "all_passed": all(c["passed"] for c in checks),
    "failures": [c["name"] for c in checks if not c["passed"]],
}
path = Path(__file__).with_suffix(".json")
path.write_text(json.dumps(out, indent=2) + "\n")
for c in checks:
    print(f'{c["name"]}: {c["actual_decimal_preview"]:.12g} {c["relation"]} {c["required_decimal_preview"]:.12g}; {"PASS" if c["passed"] else "FAIL"}')
print(f'Failures: {out["failures"]}; full exact certificate: {path}')
if not out["all_passed"]:
    raise SystemExit(1)
