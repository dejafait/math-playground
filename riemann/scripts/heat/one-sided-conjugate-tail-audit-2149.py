"""Independent finite arithmetic audit of C919a; no analytic claim is computed."""

from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path


def rat(value):
    value = Q(value)
    return f"{value.numerator}/{value.denominator}"


source = Path(__file__).with_name("one-sided-conjugate-tail-2147.json")
original_bytes = source.read_bytes()
original = json.loads(original_bytes)
checks = []


def check(name, left, relation, right):
    left, right = Q(left), Q(right)
    passed = {"=": left == right, "<": left < right,
              "<=": left <= right}[relation]
    checks.append(dict(name=name, left=rat(left), relation=relation,
                       right=rat(right), passed=passed))


# Integrate the already proved bound N(t) <= (4/5)t log(t),
# with log(R) <= 5; use the expanded two-term integral independently.
R = Q(100)
height_squared = Q(1, 4)
components = []
total = Q(0)
for m, scale in ((2, 1), (4, 200), (6, 40000)):
    p = 2*m + 2
    coefficient = height_squared*m*m*scale*scale
    integral = (Q(5, p-1) + Q(1, (p-1)**2)) / R**(p-1)
    power_bound = Q(4, 5)*p*integral
    term = coefficient*power_bound
    for key, value in (("weights", coefficient),
                       ("power_bounds", power_bound),
                       ("weighted_terms", term)):
        check(f"independent {key} p={p}", value, "=",
              Q(original["tail"][key][str(p)]))
    components.append(dict(m=m, scale=scale, p=p,
                           coefficient=rat(coefficient),
                           integrated_log_bound=rat(integral),
                           power_bound=rat(power_bound), weighted_term=rat(term)))
    total += term

epsilon = Q(1, 2_000_000_000)
B = Q(5691, 10**9)
expected = {
    "actual_rational_budget": total,
    "rounded_epsilon": epsilon,
    "required_strict_upper_bound": B/100,
    "rounding_reserve": epsilon-total,
    "threshold_reserve": B/100-epsilon,
    "baseline_B": B,
}
for key, value in expected.items():
    check(f"independent {key}", value, "=", Q(original["tail"][key]))
check("strict rounded bound", total, "<", epsilon)
check("strict hundredfold threshold", epsilon, "<", B/100)
check("baseline ratio", B/epsilon, "=", 11382)
check("source time endpoint", 4*Q(1, 20), "=", Q(1, 5))
check("local height squared endpoint", Q(1, 4)-2*Q(1, 20), "=", Q(3, 20))
check("maximum height below strict tail", Q(1, 2), "<", R)
check("adjacent lower display", Q(4999275434, 10**19), "<", total)
check("original upward display is valid", total, "<", Q(4999275435, 10**19))

# Inspect every original finite comparison, not only its pass flag.
for row in original["checks"]:
    check("stored comparison: " + row["name"], Q(row["left"]),
          row["relation"], Q(row["right"]))

failures = [row["name"] for row in checks if not row["passed"]]
unchanged = source.read_bytes() == original_bytes
if not unchanged:
    failures.append("original certificate changed")
certificate = {
    "scope": "Exact finite arithmetic only; analytic audit is in C919a step2149.",
    "input_path": str(source.relative_to(Path.cwd())),
    "input_sha256": sha256(original_bytes).hexdigest(),
    "input_unchanged": unchanged,
    "band": ["0/1", "1/20"], "radius": rat(R),
    "scaling": [1, 200, 40000],
    "tail": {"components": components,
             **{key: rat(value) for key, value in expected.items()},
             "baseline_ratio": rat(B/epsilon)},
    "checks": checks, "failures": failures, "passed": not failures,
}
output = Path(__file__).with_suffix(".json")
output.write_text(json.dumps(certificate, indent=2) + "\n")
print(f"{'PASS' if not failures else 'FAIL'}: {len(checks)} exact audit checks")
print(f"Actual: {rat(total)}; epsilon: {rat(epsilon)}; required epsilon < {rat(B/100)}")
print(f"Failures: {failures}; certificate: {output}")
if failures:
    raise SystemExit(1)
