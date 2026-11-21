"""Exact rational replay of L818's cap; no transcendental evaluator replay."""

from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "scripts/central-jacobi/audit-600/report.json"
checks = []


def check(name, condition):
    checks.append({"name": name, "pass": bool(condition)})


q = [
    (F("1.07484394250019421126346157158"),
     F("1.07484394250019421126346157162")),
    (F("1.06274366627144916855311401273"),
     F("1.06274366627144916855311401285")),
    (F("1.05430333113463476927545484495"),
     F("1.05430333113463476927545484516")),
]
source = ROOT / "lemmas/L791-fixed-central-five-root-jacobi-model.md"
source_text = source.read_text()
for k, (lo, hi) in enumerate(q):
    check(f"q{k} ordered positive enclosure", 0 < lo < hi)
# Ensure the complete endpoints are the ones printed in the canonical input.
for endpoint in (
    "1.07484394250019421126346157158",
    "1.07484394250019421126346157162",
    "1.06274366627144916855311401273",
    "1.06274366627144916855311401285",
    "1.05430333113463476927545484495",
    "1.05430333113463476927545484516",
):
    check("canonical endpoint " + endpoint, endpoint in source_text)

a, b = F(2687, 2500), F(2657, 2500)
check("whole q0 interval above weakened lower bound", a < q[0][0])
check("whole q1 interval below weakened upper bound", q[1][1] < b)
left = b * F(321, 320) ** 2
right = 2 - 1 / a
check("right threshold", right == F(2874, 2687))
check("strict contradiction at d=320", left < right)
denominator = 2500 * 320**2 * 2687
right_integer = 2874 * 2500 * 320**2
left_integer = 2657 * 321**2 * 2687
check("right integer product", right_integer == 735744000000)
check("left integer product", left_integer == 735646690719)
check("full integer difference", right_integer - left_integer == 97309281)
check("cross multiplication agrees", (right - left) * denominator == 97309281)

report = {
    "target": "L818 necessary inequality and d<=319 cap",
    "status": "PASS" if all(c["pass"] for c in checks) else "FAIL",
    "checks": checks,
    "failures": [c["name"] for c in checks if not c["pass"]],
    "q_enclosures": [[str(x) for x in interval] for interval in q],
    "weakened_q0_lower": str(a), "weakened_q1_upper": str(b),
    "left_upper_at_320": str(left), "required_right_lower": str(right),
    "positive_margin": str(right - left),
    "cross_multiplier": denominator,
    "right_integer": right_integer, "left_integer": left_integer,
    "integer_difference": right_integer - left_integer,
    "input_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
    "limits": "Rational arithmetic only; analytic identity, monotonicity, both "
              "pairings and inherited contracts are reviewed in L818. No "
              "evaluator, software binary, feasibility below320 or RH audit.",
}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(report, indent=2) + "\n")
print(f"{report['status']}: {len(checks)} exact checks; failures={report['failures']}")
print(f"At d=320: upper={left} < required lower={right}; margin={right-left}")
print(f"Complete cross-multiplied margin: {right_integer}-{left_integer}=97309281 > 0")
print(f"Certificate: {OUT.relative_to(ROOT)}")
if report["failures"]:
    raise SystemExit(1)
