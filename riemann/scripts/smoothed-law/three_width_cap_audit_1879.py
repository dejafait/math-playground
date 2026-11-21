"""Exact rational checks for C034k's audit1879; no scalar transforms."""

from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json


def partial_exp(x, degree):
    return sum((x**k / factorial(k) for k in range(degree + 1)), F(0))


checks = []


def check(name, actual, relation, required):
    passed = {"<": actual < required, ">": actual > required,
              "=": actual == required}[relation]
    checks.append(dict(name=name, actual=str(actual), relation=relation,
                       required=str(required), passed=passed))


check("exp(3/4) partial degree3", partial_exp(F(3, 4), 3), ">", F(2))
check("exp(11/4) partial degree5", partial_exp(F(11, 4), 5), ">", F(14))
check("weighted Gaussian quadratic maximum", F(1024, 9 * 14**2), "<", F(2, 3))
check("weighted Gaussian middle endpoint", F(3) - F(196, 64), "<", F(0))
check("weighted Gaussian endpoint1", F(11) - F(169, 16), "<", F(2, 3))
check("inverse sqrt2 comparison, squared", F(1, 2), "<", F(9, 16))
check("absolute member derivative coefficient", F(96, 5) + F(2, 125) + F(1, 10000), "<", F(20))
check("determinant denominator", F(32 * 16000), "=", F(512000))
check("exp(3) partial degree8", partial_exp(F(3), 8), ">", F(20))
alpha = F(1, 5 * 10**12)
check("compact excision coefficient", F(4 * 14**4, 15 * 20**13), "<", alpha)
check("cofactor multiplier", F(180 * 512000), "=", F(92160000))
check("sqrt10 comparison, squared", F(10), ">", F(9))
check("e upper series bound", partial_exp(F(1), 4) + F(1, 100), "<", F(11, 4))
check("exponent bound at S=1/100", (100 + alpha) / 100, "<", F(21, 20))
check("exp(21/20) upper bound", F(11, 4) * F(20, 19), "<", F(3))
check("variation excess constant", F(92160000) * alpha * F(15**4, 2), "=", F(1458, 3125))
check("variation excess threshold", F(1458, 3125), "<", F(1, 2))
check("e lower partial degree3", partial_exp(F(1), 3), "=", F(8, 3))
check("exp(5) lower comparison", F(8, 3)**5, ">", F(100))
B_upper = F(1038, 10000) * 5 + F(2573, 10000) * 5 + F(93675, 10000)
check("HSW B(100) upper allowance", B_upper, "=", F(11173, 1000))
count_upper = F(250, 3) + B_upper
check("HSW total upper allowance", count_upper, "=", F(283519, 3000))
check("inclusive count sufficient threshold", count_upper, "<", F(100))
check("S4 sufficient threshold", F(100, 14**4) + F(1, 10000), "<", F(1, 100))

failures = [c["name"] for c in checks if not c["passed"]]
out = Path(__file__).with_suffix(".json")
certificate = dict(
    scope="Exact rational arithmetic only; analytic inequalities and imported HSW theorem are justified in C034k audit1879.",
    all_passed=not failures, failures=failures, checks=checks,
    count_upper=str(count_upper), S4_upper=str(F(100, 14**4) + F(1, 10000)),
    TV_upper=str(1 + F(1458, 3125)),
    limitations="No zero coordinates, transform evaluations, source-wide proof validation, full-observation match or Xi realization. All inherited C034k qualifications remain.",
)
out.write_text(json.dumps(certificate, indent=2) + "\n")
for c in checks:
    print(f"{c['name']}: {c['actual']} {c['relation']} {c['required']} — {'PASS' if c['passed'] else 'FAIL'}")
print(f"Failures: {failures}; certificate: {out.relative_to(Path.cwd())}")
raise SystemExit(bool(failures))
