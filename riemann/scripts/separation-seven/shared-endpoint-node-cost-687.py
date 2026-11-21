#!/usr/bin/env python3
"""Exact pre-batch scalar cost of ONE interior node construction; no nodes computed."""
from pathlib import Path
from hashlib import sha256
import json

HERE = Path(__file__).resolve()
rows = []
checks = []

def check(name, passed):
    checks.append({"name": name, "pass": bool(passed)})

for n in (117, 81, 63):
    positive = (n - 1) // 2
    degree_steps = n - 2  # k=2,...,N-1; give P0,P1,P2 for free
    updates = 512 - 16
    scalar_per_update = 4 * degree_steps
    work = positive * updates * scalar_per_update
    check(f"N={n}: odd degree and symmetry inventory", n == 2 * positive + 1)
    check(f"N={n}: full recurrence degree inventory", degree_steps == len(range(2, n)))
    check(f"N={n}: dyadic bracket width", 16 + updates == 512)
    rows.append({"nodes": n, "positive_roots": positive,
                 "free_zero_roots": 1, "negative_roots_by_symmetry": positive,
                 "midpoint_updates_per_positive_root": updates,
                 "charged_recurrence_steps_per_update": degree_steps,
                 "charged_multiplications_per_step": 3,
                 "charged_subtractions_per_step": 1,
                 "mandatory_scalar_work": work})

total = sum(row["mandatory_scalar_work"] for row in rows)
check("positive roots total", sum(row["positive_roots"] for row in rows) == 129)
check("exact mandatory total", total == 23_254_464)
check("prescription exceeds total square cap", total > 20_000_000)
report = {
    "result": "PASS_PLANNING_CHECKS_FIXED_NODE_SETUP_FAILS" if all(c["pass"] for c in checks) else "FAIL",
    "scope": "One full-recurrence, fixed-length bisection implementation for three interior Gauss rules; not an algorithm-independent lower bound",
    "checks": checks,
    "prescription": {"endpoint": "shared even power moments on [0,1/8], through power256; not constructed",
                     "interior_panels": ["[1/2,1]", "[1/4,1/2]", "[1/8,1/4]"],
                     "initial_bracket_width": "2^-16, isolation unpaid",
                     "final_bracket_width": "2^-512",
                     "fixed_updates": "496 per positive root; no early-exit or Newton step",
                     "recurrence": "P_(k+1)=((2k+1)/(k+1))*x*P_k-(k/(k+1))*P_(k-1), precomputed coefficients; all full recurrence evaluations independent"},
    "rows": rows,
    "work": {"actual_mandatory_bound": total, "required_total_upper": 20_000_000,
             "excess": total - 20_000_000,
             "omitted": ["root isolation", "zero-root and symmetry work", "P0/P1/P2", "rational coefficient construction", "sign tests, bisection arithmetic and assignments", "Gauss weights", "all endpoint-bank construction and contractions", "all function/interval work", "entry assembly, Z and square contraction"]},
    "error": {"complete_square_required": "1e-10", "achieved_complete_bound": None,
              "reason": "Stopped before bank, nodes, quadrature or error realization; no S_ij evaluated"},
    "service_failures": ["Mandatory interior node setup exceeds complete total-work cap", "All endpoint-bank and finite-error obligations remain unpaid"],
    "script_sha256": sha256(HERE.read_bytes()).hexdigest(),
}
report["failures"] = [c["name"] for c in checks if not c["pass"]]
out = HERE.with_suffix(".json")
out.write_text(json.dumps(report, indent=2) + "\n")
print(report["result"])
print(f"Mandatory scalar work: {total}; required total <=20000000; excess {total-20_000_000}.")
print("Complete square error: UNPAID; required <=1e-10; no evaluated square entries.")
print("Failed planning checks:", report["failures"])
print("Service failures:", "; ".join(report["service_failures"]))
print("Full certificate:", out.relative_to(HERE.parents[2]))
if report["failures"]:
    raise SystemExit(1)
