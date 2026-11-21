"""Independent exact audit of L919's finite constants; no analytic claims.

Run from riemann: python3 scripts/heat/complete-zero-tail-audit-204.py
Replays the original program with only its output basename redirected,
then reconstructs all load-bearing values independently. Old files stay intact.
"""

from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import json

base = Path(__file__).parent
source = base / "complete-zero-tail-202.py"
original_path = base / "complete-zero-tail-202.json"
replay_path = base / "complete-zero-tail-replay-204.json"
output_path = Path(__file__).with_suffix(".json")
source_bytes = source.read_bytes()
original_bytes = original_path.read_bytes()
original = json.loads(original_bytes)

# __file__ is only used by the original to select its JSON output path.
replay_exit = None
try:
    exec(compile(source_bytes, str(source), "exec"), {
        "__name__": "__main__",
        "__file__": str(replay_path.with_suffix(".py")),
    })
except SystemExit as error:
    replay_exit = error.code
replay = json.loads(replay_path.read_text())

checks = []


def record(name, actual, expected):
    checks.append({"name": name, "actual": actual,
                   "expected": expected, "passed": actual == expected})


def rat(value):
    value = Q(value)
    return f"{value.numerator}/{value.denominator}"


record("replay normal completion", replay_exit, None)
record("replay equals entire original certificate", replay, original)
record("original source unchanged", source.read_bytes() == source_bytes, True)
record("original certificate unchanged", original_path.read_bytes() == original_bytes, True)
record("radius", original["radius"], "100/1")
record("time interval", original["time_band"], ["0/1", "1/20"])
record("diagonal scaling", original["scaling"], [1, 200, 40000])

# Recurrence, rather than factorial summation, reconstructs exp(3)'s
# degree-eight partial sum. Every subsequent item is exact rational data.
term = Q(1)
partial = term
for n in range(1, 9):
    term *= Q(3, n)
    partial += term

finite_expected = [
    (partial, ">", Q(20)),
    (Q(1)+Q(1)+Q(1, 2)+Q(2, 9), "<", Q(11, 4)),
    (Q(14641, 256), "<", Q(72)),
    (Q(484, 49), "<", Q(10)),
    (Q(55, 14), "<", Q(4)),
    (Q(1, 20), "=", Q(1, 20)),
    (Q(8000+4400+220+1, 8000), "<", Q(8, 5)),
    (Q(3, 4), "=", Q(3, 4)),
    (Q(512, 3), "<", Q(200)),
    (Q(27, 200)+Q(123, 3200), "=", Q(111, 640)),
    (Q(111, 640), "<", Q(1, 4)),
    (Q(123+5, 80), "=", Q(8, 5)),
]

# Integral of (4/5) t log(t) against p t^(-p-1) dt, evaluated
# at R=100 and with log(R)<5; weights come directly from D's squares.
R = 100
power_bounds = {}
weighted = {}
for i, diagonal in enumerate((1, 200, 40000)):
    p = 4 + 4*i
    integral = Q(5, (p-1)*R**(p-1)) + Q(1, (p-1)**2*R**(p-1))
    bound = Q(4*p, 5)*integral
    power_bounds[str(p)] = rat(bound)
    weighted[str(p)] = rat(diagonal**2*bound)
budget = sum((Q(value) for value in weighted.values()), Q(0))
threshold = Q(5691, 10**9)
finite_expected.append((budget, "<", threshold))

record("finite check count", len(original["checks"]), len(finite_expected))
for index, (left, relation, right) in enumerate(finite_expected):
    old = original["checks"][index]
    record(f"finite check {index+1} operands",
           [old["left"], old["relation"], old["right"]],
           [rat(left), relation, rat(right)])
    truth = {"<": left < right, ">": left > right, "=": left == right}[relation]
    record(f"finite check {index+1} independent truth", truth, True)
    record(f"finite check {index+1} stored truth", old["passed"], truth)

tail_expected = {
    "log_radius_upper_bound": "5/1",
    "power_budgets": power_bounds,
    "weighted_terms": weighted,
    "actual_rational_budget": rat(budget),
    "required_upper_threshold": rat(threshold),
    "positive_rounding_reserve": rat(threshold-budget),
}
record("complete tail data", original["tail"], tail_expected)
record("printed lemma budget", rat(budget), "74137011761/13027587890625000")
record("original failure list", original["failures"], [])
record("original pass flag", original["passed"], True)
failures = [item["name"] for item in checks if not item["passed"]]
certificate = {
    "scope": "Exact finite audit only; analytic audit is canonical in L919 step204.",
    "original_source_sha256": sha256(source_bytes).hexdigest(),
    "original_certificate_sha256": sha256(original_bytes).hexdigest(),
    "replay_certificate": str(replay_path),
    "checks": checks,
    "tail": tail_expected,
    "failures": failures,
    "passed": not failures,
}
output_path.write_text(json.dumps(certificate, indent=2)+"\n")
print(f"{'PASS' if not failures else 'FAIL'}: {len(checks)} independent audit checks")
print(f"Actual budget {rat(budget)}; required < {rat(threshold)}")
print(f"Reserve {rat(threshold-budget)}; failures {failures}")
print(f"Audit certificate: {output_path}; replay: {replay_path}")
if failures:
    raise SystemExit(1)
