"""Exact finite arithmetic for C919a; analytic arguments are in the lemma."""

from fractions import Fraction as Q
import json
from pathlib import Path


def rat(q):
    q = Q(q)
    return f"{q.numerator}/{q.denominator}"


checks = []


def check(name, left, relation, right):
    left, right = Q(left), Q(right)
    passed = {"=": left == right, "<": left < right,
              "<=": left <= right}[relation]
    checks.append(dict(name=name, left=rat(left), relation=relation,
                       right=rat(right), passed=passed))


radius = Q(100)
height_squared = Q(1, 4)
weights = {6: Q(1), 10: Q(160000), 14: Q(14400000000)}
for m, scale in ((2, 1), (4, 200), (6, 40000)):
    check(f"imaginary-vector coefficient m={m}",
          height_squared * (m * scale)**2, "=", weights[2*m+2])
check("source-time right endpoint", 4 * Q(1, 20), "=", Q(1, 5))
check("local strip squared right endpoint", (1 - 2*Q(1, 5))/4,
      "=", Q(3, 20))
check("pure imaginary zero cannot enter strict tail", Q(1, 2), "<", radius)

power_bounds = {
    p: Q(4*p, 5*(p-1)) * radius**(1-p) * (5 + Q(1, p-1))
    for p in weights
}
terms = {p: weights[p] * power_bounds[p] for p in weights}
expected_terms = {6: Q(39, 78125000000), 10: Q(23, 31640625000000),
                  14: Q(2079, 3300781250000000000)}
for p in terms:
    check(f"integrated weighted power p={p}", terms[p], "=", expected_terms[p])
actual = sum(terms.values(), Q(0))
epsilon = Q(1, 2000000000)
baseline = Q(5691, 10**9)
required = baseline / 100
check("full rational sum", actual, "=", Q(133662268399, 267363281250000000000))
check("positive rounding reserve", epsilon-actual, "=",
      Q(9686113, 133681640625000000000))
check("rounding upper bound", actual, "<", epsilon)
check("fixed hundredfold threshold", epsilon, "<", required)
check("old budget divided by rounded cost", baseline/epsilon, "=", 11382)

failures = [c["name"] for c in checks if not c["passed"]]
certificate = {
    "scope": "Finite rational arithmetic only; C919a proves strip transfer, conjugate bookkeeping and complete infinite-tail bounds.",
    "radius": rat(radius), "scaling": [1, 200, 40000],
    "time_band": ["0/1", "1/20"],
    "tail": {
        "powers": list(weights),
        "weights": {str(p): rat(v) for p, v in weights.items()},
        "power_bounds": {str(p): rat(v) for p, v in power_bounds.items()},
        "weighted_terms": {str(p): rat(v) for p, v in terms.items()},
        "actual_rational_budget": rat(actual), "rounded_epsilon": rat(epsilon),
        "required_strict_upper_bound": rat(required),
        "rounding_reserve": rat(epsilon-actual),
        "threshold_reserve": rat(required-epsilon),
        "baseline_B": rat(baseline),
    },
    "checks": checks, "failures": failures, "passed": not failures,
}
path = Path(__file__).with_suffix(".json")
path.write_text(json.dumps(certificate, indent=2) + "\n")
print(f"{'PASS' if not failures else 'FAIL'}: {len(checks)} exact arithmetic checks")
print(f"Actual cost: {rat(actual)}; epsilon: {rat(epsilon)}; required epsilon < {rat(required)}")
print(f"Failures: {failures}; certificate: {path}")
if failures:
    raise SystemExit(1)
