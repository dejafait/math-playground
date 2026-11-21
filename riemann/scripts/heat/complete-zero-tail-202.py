"""Exact finite constants for L919; the analytic proof is in the lemma.

Run from the active notebook: python3 scripts/heat/complete-zero-tail-202.py
Only Python's exact integers and fractions are used for the certificate.
"""

from fractions import Fraction as Q
from math import factorial
from pathlib import Path
import json


def rational(value):
    value = Q(value)
    return f"{value.numerator}/{value.denominator}"


checks = []


def check(name, left, relation, right):
    left, right = Q(left), Q(right)
    passed = {"<": left < right, "<=": left <= right,
              ">": left > right, "=": left == right}[relation]
    checks.append({"name": name, "left": rational(left),
                   "relation": relation, "right": rational(right),
                   "passed": passed})


e3_lower = sum((Q(3) ** j / factorial(j) for j in range(9)), Q(0))
e_upper = Q(5, 2) + Q(1, 6) / (1 - Q(1, 4))
check("exp(3) finite positive-series lower bound", e3_lower, ">", 20)
check("exp(1) geometric-series upper bound", e_upper, "<", Q(11, 4))
check("exp(4) upper bound", Q(11, 4) ** 4, "<", 72)
check("pi squared upper bound", Q(22, 7) ** 2, "<", 10)
check("v upper bound on normalizer interval", Q(22, 7) * Q(5, 4), "<", 4)
check("normalizer lower bound", Q(18, 5) / 72, "=", Q(1, 20))
q = Q(1, 20)
numerator = 1 + 11 * q + 11 * q**2 + q**3
check("kernel geometric numerator", numerator, "<", Q(8, 5))
check("kernel Bernoulli denominator", 1 - 5*q, "=", Q(3, 4))
check("kernel constant", 80 * Q(8, 5) / Q(3, 4), "<", 200)
check("count additive constant", Q(3, 2)*(Q(9, 100)+Q(41, 1600)),
      "=", Q(111, 640))
check("count absorption using log(r)>=4", Q(111, 640), "<", Q(4, 16))
check("count logarithmic coefficient", Q(123, 80)+Q(1, 16), "=", Q(8, 5))

radius = Q(100)
power_budgets = {
    p: Q(4*p, 5*(p-1)) * radius**(1-p) * (5 + Q(1, p-1))
    for p in (4, 8, 12)
}
weights = {4: Q(1), 8: Q(40000), 12: Q(1600000000)}
terms = {p: weights[p] * power_budgets[p] for p in power_budgets}
budget = sum(terms.values(), Q(0))
threshold = Q(5691, 10**9)
check("complete matrix budget below stated threshold", budget, "<", threshold)
failures = [item["name"] for item in checks if not item["passed"]]
certificate = {
    "scope": "Exact finite constants only; Jensen, product and full-tail integration are proved/cited in L919.",
    "radius": rational(radius), "time_band": ["0/1", "1/20"],
    "scaling": [1, 200, 40000], "checks": checks,
    "tail": {
        "log_radius_upper_bound": "5/1",
        "power_budgets": {str(p): rational(v) for p, v in power_budgets.items()},
        "weighted_terms": {str(p): rational(v) for p, v in terms.items()},
        "actual_rational_budget": rational(budget),
        "required_upper_threshold": rational(threshold),
        "positive_rounding_reserve": rational(threshold-budget),
    },
    "failures": failures, "passed": not failures,
}
path = Path(__file__).with_suffix(".json")
path.write_text(json.dumps(certificate, indent=2) + "\n")
print(f"{'PASS' if not failures else 'FAIL'}: {len(checks)} exact constant checks")
print(f"Actual rational budget: {rational(budget)}; required upper bound: {rational(threshold)}")
print(f"Failures: {failures}; certificate: {path}")
if failures:
    raise SystemExit(1)
