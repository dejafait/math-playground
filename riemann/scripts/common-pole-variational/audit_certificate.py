#!/usr/bin/env python3
"""Independently assemble and replay L528's six exact comparisons.

This checks arithmetic, not the analytic proof in the canonical lemma.
"""
from fractions import Fraction as Q
from hashlib import sha256
import json
from math import factorial
from pathlib import Path
import subprocess
import sys


directory = Path(__file__).resolve().parent
original = directory / "majorant-certificate.json"
before = original.read_bytes()
saved = json.loads(before)
failures = []


def atan_lower(z, terms):
    return sum(((-1) ** k * z ** (2 * k + 1) / (2 * k + 1)
                for k in range(terms)), Q(0))


atan = atan_lower(Q(1, 2), 4) + atan_lower(Q(1, 3), 2)
cosine = sum(((-1) ** k * Q(5, 4) ** (2 * k) / factorial(2 * k)
              for k in range(3)), Q(0))
e_partial = sum((Q(1, factorial(k)) for k in range(4)), Q(0))
pi_lower = 4 * Q(47, 60)
mean_upper = (Q(5, 4) + Q(6, 5)) / pi_lower
threshold = Q(47, 60)
gap = threshold - mean_upper
expected = {
    "atan_lower": atan,
    "atan_margin": atan - threshold,
    "cosine_upper": cosine,
    "mean_upper_strict": mean_upper,
    "threshold_lower_strict": threshold,
    "uniform_gap_lower_strict": gap,
}
scalar_checks = []
for key, value in expected.items():
    passed = Q(saved[key]) == value
    scalar_checks.append({"field": key, "recorded": saved[key],
                          "recomputed": str(value), "passed": passed})
    if not passed:
        failures.append(key)

comparisons = [
    (atan, ">", threshold),
    (cosine, "<", Q(1, 3)),
    (e_partial, ">", Q(13, 5)),
    (Q(5, 4), "<", pi_lower / 2),
    (mean_upper, "<", threshold),
    (gap, ">", Q(0)),
]
checks = []
if len(saved["checks"]) != len(comparisons):
    failures.append("comparison count")
for i, (actual, relation, required) in enumerate(comparisons):
    lhs = actual.numerator * required.denominator
    rhs = required.numerator * actual.denominator
    positive_integer_margin = rhs - lhs if relation == "<" else lhs - rhs
    record = saved["checks"][i] if i < len(saved["checks"]) else {}
    matches = (record.get("actual") == str(actual)
               and record.get("required") == str(required)
               and record.get("relation") == relation
               and record.get("passed") is True)
    passed = positive_integer_margin > 0 and matches
    checks.append({"index": i, "name": record.get("name"),
                   "actual": str(actual), "relation": relation,
                   "required": str(required),
                   "cross_product_margin": positive_integer_margin,
                   "saved_record_matches": matches, "passed": passed})
    if not passed:
        failures.append(f"comparison {i}")
if saved["failures"] != []:
    failures.append("original certificate reports failures")
if saved["lemma"] != "L528":
    failures.append("lemma identity")

# The square-root step reduces exactly to (2/5)e-26/25>0.
# e>e_partial makes this lower bound strict. No approximate e is used.
square_margin = Q(2, 5) * e_partial - Q(26, 25)
if square_margin != Q(2, 75) or square_margin <= 0:
    failures.append("square-root premise")
if gap != Q(1, 705):
    failures.append("claimed uniform gap")

replay = subprocess.run([sys.executable, str(directory / "majorant_certificate.py")],
                        cwd=directory.parents[1], capture_output=True, text=True)
after = original.read_bytes()
replay_equal = before == after
if replay.returncode != 0 or not replay_equal:
    failures.append("original generator replay")

report = {
    "lemma": "L528",
    "scope": "Exact arithmetic and full original-generator replay only; analytic audit is in L528.",
    "original_sha256": sha256(before).hexdigest(),
    "replay_sha256": sha256(after).hexdigest(),
    "original_generator": "scripts/common-pole-variational/majorant_certificate.py",
    "replay_exit_code": replay.returncode,
    "replay_byte_identical": replay_equal,
    "replay_stdout": replay.stdout,
    "replay_stderr": replay.stderr,
    "scalar_checks": scalar_checks,
    "checks": checks,
    "square_root_difference_strict_lower": str(square_margin),
    "actual_mean_upper_strict": str(mean_upper),
    "required_threshold": "pi/4",
    "threshold_lower_strict": str(threshold),
    "uniform_gap_lower_strict": str(gap),
    "failures": failures,
}
output = directory / "majorant-audit-certificate.json"
output.write_text(json.dumps(report, indent=2) + "\n")
print(f"L528 audit: actual mean <{mean_upper}; required <pi/4; pi/4>{threshold}")
print(f"Strict gap >{gap}; six comparisons; six scalar matches; replay identical={replay_equal}")
print(f"Failures: {failures}")
print(f"Full certificate: {output.relative_to(directory.parents[1])}")
if failures:
    raise SystemExit(1)
