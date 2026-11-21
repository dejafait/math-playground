#!/usr/bin/env python3
"""Exact rational comparisons for C029a; reuses, does not reverify, input1506."""
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "scripts/jacobi-reference/audit-penultimate-1506.json"
OUTPUT = ROOT / "scripts/jacobi-reference/first-omitted-two-site-cost-1944.json"
raw = SOURCE.read_bytes()
source = json.loads(raw)
sigma = F(1, 200)
inputs = {}
normalized = {}
checks = []


def positive(name, actual, required=F(0)):
    checks.append({"name": name, "actual": str(actual),
                   "required_strict_lower": str(required),
                   "margin": str(actual - required), "passed": actual > required})


for k in range(2, 6):
    key = f"S_{k}"
    record = source["actual_and_required_bounds"][key]
    lo, hi = map(F, record["actual"])
    req_lo, req_hi = map(F, record["required_open"])
    inputs[key] = record
    positive(f"{key}_nonempty", hi - lo)
    positive(f"{key}_printed_lower", lo, req_lo)
    positive(f"{key}_printed_upper", req_hi, hi)
    normalized[k] = (lo / sigma**k, hi / sigma**k)

Vhi = F(3, 2)
Tlo, Thi = F(11533, 10000), F(11534, 10000)
Qlo, Qhi = F(10608, 10000), F(10609, 10000)
Hlo = F(10283, 10000)
positive("V_positive", normalized[2][0])
positive("V_upper", Vhi, normalized[2][1])
for k, label, lo, hi in [(3, "T", Tlo, Thi), (4, "Q", Qlo, Qhi)]:
    positive(label + "_lower", normalized[k][0], lo)
    positive(label + "_upper", hi, normalized[k][1])
positive("H_lower", normalized[5][0], Hlo)

rlo, rhi = F(57, 100), F(59, 100)
Xhi, Yhi = F(99, 100), F(59, 100)


def f(r):
    return (1 + r**3)**4 / (1 + r**4)**3


positive("r_lower_comparison", Tlo**4 / Qhi**3, f(rlo))
positive("r_upper_comparison", f(rhi), Thi**4 / Qlo**3)
positive("X_upper_comparison", Xhi**4 * (1 + rlo**4), Qhi)
positive("Y_upper_comparison", Yhi, rhi * Xhi)
gap = Hlo - Xhi**5 - Yhi**5
positive("normalized_fifth_gap", gap, F(1, 200))
cost_floor = F(8)**4 / 25 * (sigma**5 / 200)**2 / (Vhi * sigma**2)**4
positive("normalized_cost_liminf_floor", cost_floor, F(1, 50000000))

failures = [c["name"] for c in checks if not c["passed"]]
certificate = {
    "status": "PASS" if not failures else "FAIL",
    "purpose": "C029a rational input and strict-gap comparisons only",
    "provenance": {"source": str(SOURCE.relative_to(ROOT)),
                   "sha256": hashlib.sha256(raw).hexdigest(),
                   "selected_pointers": [f"/actual_and_required_bounds/S_{k}" for k in range(2, 6)],
                   "mode": "reuse audited input1506; no evaluator replay or backend attestation"},
    "inherited_assumptions": ["C028c/L778 entire-evaluator remainder and arithmetic contracts",
                              "Python3.15.2/Decimal1.70/libmpdec4.0.1 correctly rounded exp/sqrt; allcr=1",
                              "C028z accepted strict point and common local exact-cancellation branch"],
    "input_records": inputs,
    "normalized_input_intervals": {f"S_{k}/sigma^{k}": list(map(str, normalized[k])) for k in range(2, 6)},
    "coarse_bounds": {"sigma": str(sigma), "V_upper": str(Vhi),
                      "T": list(map(str, [Tlo, Thi])), "Q": list(map(str, [Qlo, Qhi])),
                      "H_lower": str(Hlo), "r": list(map(str, [rlo, rhi])),
                      "X_upper": str(Xhi), "Y_upper": str(Yhi)},
    "actual_and_required_bounds": {
        "fifth_gap_scaled": {"strict_lower_from_box": str(gap), "required": "1/200"},
        "cost_liminf": {"strict_lower": str(cost_floor), "required": "1/50000000"}},
    "checks": checks, "failures": failures,
    "not_verified_by_script": ["C029a analytic trace extension and coefficient proof",
                               "effective degree onset or finite-degree parameter values",
                               "other branches, full cost upper bound, actual-root reality, RH"]}
OUTPUT.write_text(json.dumps(certificate, indent=2) + "\n")
print(f"{certificate['status']}: {len(checks)} exact rational checks; failures={failures}")
print(f"Scaled fifth gap > {gap} > 1/200")
print(f"Normalized cost liminf > {cost_floor} > 1/50000000 (analytic proof required)")
print(f"Certificate: {OUTPUT.relative_to(ROOT)}")
if failures:
    raise SystemExit(1)
