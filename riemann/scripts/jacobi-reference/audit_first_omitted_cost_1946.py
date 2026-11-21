#!/usr/bin/env python3
"""Audit C029a's finite rational evidence; no evaluator or analytic replay."""
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "scripts/jacobi-reference"
SOURCE = BASE / "audit-penultimate-1506.json"
SAVED = BASE / "first-omitted-two-site-cost-1944.json"
PROGRAM = BASE / "first_omitted_two_site_cost_1944.py"
OUTPUT = BASE / "audit-first-omitted-cost-1946.json"
raw = {p.name: p.read_bytes() for p in (SOURCE, SAVED, PROGRAM)}
source = json.loads(raw[SOURCE.name])
saved = json.loads(raw[SAVED.name])
records = []


def check(name, actual, required, passed):
    records.append({"name": name, "actual": actual,
                    "required": required, "passed": bool(passed)})


def equal(name, actual, required):
    check(name, actual, required, actual == required)


def greater(name, a, b):
    # Positive rational denominators permit an independent integer comparison.
    cross = a.numerator * b.denominator - b.numerator * a.denominator
    check(name, {"left": str(a), "right": str(b),
                 "cross_product_margin": str(cross)},
          "cross_product_margin > 0", cross > 0)


equal("source_status", source["status"], "PASS")
equal("source_hash", saved["provenance"]["sha256"],
      hashlib.sha256(raw[SOURCE.name]).hexdigest())
equal("source_path", saved["provenance"]["source"], str(SOURCE.relative_to(ROOT)))
equal("source_pointers", saved["provenance"]["selected_pointers"],
      [f"/actual_and_required_bounds/S_{k}" for k in range(2, 6)])
sigma = Q(1, 200)
intervals = {}
expected = {}
printed = {
    2: ("3.7172599285269686e-5", "3.7172599285269687e-5"),
    3: ("1.4417393140097327e-7", "1.4417393140097329e-7"),
    4: ("6.6303168025299086e-10", "6.6303168025299088e-10"),
    5: ("3.2136641506166011e-12", "3.2136641506166013e-12"),
}
for k in range(2, 6):
    key = f"S_{k}"
    src = source["actual_and_required_bounds"][key]
    equal(f"{key}_complete_input_copy", saved["input_records"][key], src)
    equal(f"{key}_printed_endpoints", src["required_open"], list(printed[k]))
    lo, hi = map(Q, src["actual"])
    pl, ph = map(Q, printed[k])
    intervals[k] = (lo * 200**k, hi * 200**k)
    equal(f"{key}_normalized_interval",
          saved["normalized_input_intervals"][f"S_{k}/sigma^{k}"],
          list(map(str, intervals[k])))
    expected[key + "_nonempty"] = (hi - lo, Q(0))
    expected[key + "_printed_lower"] = (lo, pl)
    expected[key + "_printed_upper"] = (ph, hi)

V = Q(3, 2)
T0, T1 = Q(11533, 10000), Q(11534, 10000)
Q0, Q1 = Q(10608, 10000), Q(10609, 10000)
H0 = Q(10283, 10000)
r0, r1, X1, Y1 = Q(57, 100), Q(59, 100), Q(99, 100), Q(59, 100)
box = {"sigma": "1/200", "V_upper": "3/2", "T": list(map(str, (T0, T1))),
       "Q": list(map(str, (Q0, Q1))), "H_lower": str(H0),
       "r": list(map(str, (r0, r1))), "X_upper": str(X1), "Y_upper": str(Y1)}
equal("coarse_box", saved["coarse_bounds"], box)
expected.update({
    "V_positive": (intervals[2][0], Q(0)),
    "V_upper": (V, intervals[2][1]),
    "T_lower": (intervals[3][0], T0), "T_upper": (T1, intervals[3][1]),
    "Q_lower": (intervals[4][0], Q0), "Q_upper": (Q1, intervals[4][1]),
    "H_lower": (intervals[5][0], H0),
    "r_lower_comparison": (T0**4 / Q1**3, (1+r0**3)**4 / (1+r0**4)**3),
    "r_upper_comparison": ((1+r1**3)**4 / (1+r1**4)**3, T1**4 / Q0**3),
    "X_upper_comparison": (X1**4 * (1+r0**4), Q1),
    "Y_upper_comparison": (Y1, r1*X1),
})
gap = H0 - X1**5 - Y1**5
floor = Q(4096, 25) * (sigma**5 / 200)**2 / (V*sigma**2)**4
expected["normalized_fifth_gap"] = (gap, Q(1, 200))
expected["normalized_cost_liminf_floor"] = (floor, Q(1, 50000000))
equal("check_names_and_order", [r["name"] for r in saved["checks"]], list(expected))
for row in saved["checks"]:
    name = row["name"]
    a, b = expected[name]
    equal(name + "_record", row,
          {"name": name, "actual": str(a), "required_strict_lower": str(b),
           "margin": str(a-b), "passed": a > b})
    greater(name + "_independent_comparison", a, b)

equal("gap_fraction", str(gap), "29087601/5000000000")
equal("floor_fraction", str(floor), "16/791015625")
bounds = {"fifth_gap_scaled": {"strict_lower_from_box": str(gap), "required": "1/200"},
          "cost_liminf": {"strict_lower": str(floor), "required": "1/50000000"}}
equal("saved_summary", saved["actual_and_required_bounds"], bounds)
equal("saved_status", saved["status"], "PASS")
equal("saved_failures", saved["failures"], [])
for p in (SOURCE, SAVED, PROGRAM):
    equal(p.name + "_unchanged", p.read_bytes() == raw[p.name], True)

failures = [r["name"] for r in records if not r["passed"]]
result = {
    "status": "FAIL" if failures else "PASS",
    "purpose": "Independent complete rational comparison audit of C029a; no imported program code",
    "hashes": {name: hashlib.sha256(data).hexdigest() for name, data in raw.items()},
    "selected_input_records": {f"S_{k}": source["actual_and_required_bounds"][f"S_{k}"]
                               for k in range(2, 6)},
    "actual_and_required_bounds": bounds,
    "audit_check_count": len(records), "original_comparison_count": len(expected),
    "checks": records, "failures": failures,
    "scope": "All selected1506 intervals and all25 original rational checks; source1506 audit reused",
    "unverified": ["L778 evaluator and Decimal backend attestation",
                   "analytic proof, recorded separately in C029a audit1946",
                   "effective onset, finite sites, other branches, full-cost upper payment, RH"],
}
OUTPUT.write_text(json.dumps(result, indent=2) + "\n")
print(f"{result['status']}: {len(records)} checks; all {len(expected)} original comparisons; failures={failures}")
print(f"Scaled fifth gap: {gap} > 1/200; normalized cost floor: {floor} > 1/50000000")
print(f"Certificate: {OUTPUT.relative_to(ROOT)}")
if failures:
    raise SystemExit(1)
