#!/usr/bin/env python3
"""Independent exact-value audit of L046; its analytic audit is canonical prose."""
import hashlib
import json
import math
import subprocess
import sys
from fractions import Fraction as F
from pathlib import Path

base = Path(__file__).resolve().parent
original = base / "eighteen-height-certificate.json"
before = original.read_bytes()
subprocess.run([sys.executable, str(base / "certify_eighteen_heights.py")], check=True)
after = original.read_bytes()
saved = json.loads(after)
q = F(48, 25)
# Closed form, independent of the generator's termwise summation.
R = F(48**18 - 25**18, 23 * 25**17)
C = 3 * 225640000 // 2
A = F(8, 5) * F(15, 4) * F(133, 10) * 150000
B = (54 + 6 * 3) * 150000 + 2
expected = [
    ("shift constant", F(107, 75), q),
    ("sixth power integer comparison", 48**6, 51 * 25**6),
    ("geometric bound via sixth power", F(25 * (51**3 - 1), 23), 150000),
    ("full exact geometric sum", R, 150000),
    ("e series lower bound reciprocal comparison", F(27, 10), F(163, 60)),
    ("log18 less than 3", 18 * 1000, 27**3),
    ("logC less than 20", C * 10**20, 27**20),
    ("tail contribution", F(3, 2) * F(23 * 18, 517), 2),
    ("derivative threshold", A, C),
    ("entire-ray starting bound", 20 * A + B, C),
]
checks = []


def record(name, actual, relation, required, passed):
    checks.append(dict(name=name, actual=str(actual), relation=relation,
                       required=str(required), passed=bool(passed)))


record("byte-identical regeneration", hashlib.sha256(after).hexdigest(), "=",
       hashlib.sha256(before).hexdigest(), before == after)
record("record count", len(saved["checks"]), "=", len(expected),
       len(saved["checks"]) == len(expected))
for item, (name, actual, required) in zip(saved["checks"], expected):
    a, b = F(actual), F(required)
    valid = (item["name"] == name and F(item["actual"]) == a
             and F(item["required_strict_upper_bound"]) == b
             and item["passed"] is True and a < b)
    record("replay: " + name, a, "<", b, valid)
for key, value in dict(q=q, R18=R, C=C, A=A, B=B).items():
    record("summary: " + key, saved[key], "=", value, F(saved[key]) == value)
record("saved failures", saved["failures"], "=", [], saved["failures"] == [])
identities = [
    ("positive e-series partial sum", sum((F(1, math.factorial(j)) for j in range(6)), F(0)), F(163, 60)),
    ("exp(4/3) partial sum", sum((F(4, 3)**j / math.factorial(j) for j in range(4)), F(0)), F(293, 81)),
    ("height coefficient", F(3, 4) * F(8, 5)**2, q),
    ("transfer constant", F(8, 5) * F(4, 5) * F(4, 3) / 4, F(32, 75)),
    ("prefix height coefficient", F(9, 4) + F(3, 2), F(15, 4)),
    ("prefix constant", F(9, 4) * F(4, 3), 3),
    ("geometric formula", R * (q - 1), q**18 - 1),
    ("strict margin lower bound", C - 20 * A - B, 88259998),
]
for name, actual, required in identities:
    record(name, actual, "=", required, actual == required)
for name, a, b in [
    ("delta upper bound", 3**5, 2**8),
    ("delta lower bound", 2**3, 3**2),
    ("alpha positive", 16, 27),
    ("shift absorption", F(23, 11), F(3, 4) * F(540, 11)),
    ("geometric intermediate bound", R, F(3316250, 23)),
    ("exp(4/3) lower bound", 3, F(293, 81)),
]:
    record(name, a, "<", b, a < b)
failures = [c for c in checks if not c["passed"]]
out = base / "eighteen-height-audit-certificate.json"
out.write_text(json.dumps(dict(lemma="L046", kind="exact arithmetic audit; analytic proof in lemma",
                              checks=checks, failures=failures), indent=2) + "\n")
print(f"audit checks={len(checks)}, failures={len(failures)}; original records={len(expected)}")
print(f"R18={R} < 150000; 20*A+B={20*A+B} < C={C}; margin={C-20*A-B}")
print(f"audit certificate: {out.relative_to(Path.cwd())}")
for failure in failures:
    print(failure)
if failures:
    raise SystemExit(1)
