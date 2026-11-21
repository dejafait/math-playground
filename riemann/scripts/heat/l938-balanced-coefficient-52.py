"""Exact 34-term saddle coefficient; no numerical tail-sign experiment."""
from fractions import Fraction as Q
from math import factorial
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "lemmas/L938-actual-h2-fixed-energy-density-and-cell-test.md"
OUT = Path(__file__).with_suffix(".json")
rows = []
for c, alpha in re.findall(r"^\| (-?\d+) \| \(([0-9,]+)\) \|$", SOURCE.read_text(), re.M):
    aa = tuple(map(int, alpha.split(",")))
    assert len(aa) == 7 and sum(aa) == 12
    assert sum(k * a for k, a in enumerate(aa)) == 12
    den = 1
    for k, a in enumerate(aa):
        den *= factorial(2 * k) ** a
    rows.append({"coefficient": int(c), "alpha": aa,
                 "factorial_denominator": str(den), "term": str(Q(int(c), den))})
assert len(rows) == 34
total = sum((Q(row["term"]) for row in rows), Q(0))
absolute = sum((abs(Q(row["term"])) for row in rows), Q(0))
q = [Q((-1) ** n, factorial(2 * n)) for n in range(7)]
s = [Q(0)] * 7
for n in range(1, 7):
    s[n] = -n * q[n] - sum((s[j] * q[n-j] for j in range(1, n)), Q(0))
a, b, c, d, e = s[2:]
det = a*c*e - a*d*d - b*b*e + 2*b*c*d - c*c*c
checks = {"all_34_rows": len(rows) == 34,
          "independent_newton_agrees": det == total,
          "strict_positive_coefficient": total > 0}
out = {"source": str(SOURCE.relative_to(ROOT)), "rows": rows,
       "newton_S1_to_S6": list(map(str, s[1:])),
       "coefficient_C": str(total), "absolute_sum": str(absolute),
       "absolute_to_signed_ratio": str(absolute / total) if total else None,
       "simplex_polynomial_at_balance": str(total / 12**12),
       "newton_determinant": str(det), "checks": checks,
       "failures": [k for k, passed in checks.items() if not passed],
       "scope": "Exact coefficient only; no localization, remainder or tail sign certified."}
OUT.write_text(json.dumps(out, indent=2) + "\n")
print(f"C={total}; required C != 0; actual sign={'positive' if total > 0 else 'nonpositive'}")
print(f"Newton determinant={det}; exact agreement={det == total}; rows={len(rows)}/34")
print(f"absolute/signed={out['absolute_to_signed_ratio']}; failures={out['failures']}")
print(f"certificate={OUT.relative_to(ROOT)}")
if out["failures"]:
    raise SystemExit(1)
