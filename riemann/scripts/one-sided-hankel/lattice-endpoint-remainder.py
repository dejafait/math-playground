#!/usr/bin/env python3
"""Exact new maximum aggregation of the already audited L663 certificate.

All 513 angular rows are compared with their complete prior replay.
Every angular interval is charged the semiconvex chord error, for the
top and both endpoint bounds. This does not replay the interval backend
or assert an estimate for the omitted lower horizontal edge.
"""
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path


HERE = Path(__file__).resolve().parent
source = HERE / "full-circle-root-compensation-certificate.json"
audit = HERE / "full-circle-root-compensation-audit.json"
dest = HERE / "lattice-endpoint-remainder.json"
old = json.loads(source.read_text())
prior = json.loads(audit.read_text())
out = {
    "status": "INCOMPLETE",
    "scope": "Exact continuum-maximum aggregation of audited terminal bounds; no fresh interval-backend replay or signed lower-edge estimate.",
    "sources": {
        p.name: hashlib.sha256(p.read_bytes()).hexdigest()
        for p in (source, audit)
    },
    "checks": {}, "failures": [], "angular_cells": [],
}


def check(ok, label):
    out["checks"][label] = bool(ok)
    if not ok:
        out["failures"].append(label)


S = int(old["scale"])
check(S == 2**72 == int(prior["scale"]), "audited_scale")
check(old["status"] == prior["status"] == "PASS", "source_and_replay_pass")
check(not old["failures"] and not old["derivative_failures"]
      and not prior["failures"], "source_and_replay_no_failures")
check(all(prior["checks"].values()), "every_prior_replay_check_passes")
check(prior["summary"]["derivative_boxes_replayed"] == 8192,
      "inherited_vertical_derivative_replay_count")
check(old["global_bounds"] == prior["global_replay"],
      "global_bounds_match_audit")
check(old["global_bounds"]["checks"]["second_angle_derivative_100"],
      "audited_semiconvex_bound")
rows = old["angular_rows"]
check(rows == prior["angular_replay"], "all_angular_values_match_audit")
check(len(rows) == 513 and all(row["angle"] == [k, 512]
                              for k, row in enumerate(rows)),
      "complete_angular_grid")
check(all(len(row["rate_uppers"]) == 4 and
          int(row["maximum_upper"]) == max(map(int, row["rate_uppers"]))
          for row in rows), "all_four_source_columns_retained")
check(old["comparison"] == prior["comparison"], "source_quadrature_matches")
check(F(int(old["comparison"]["t_error_upper"]), S)
      >= F(70, 12 * 128**2), "source_t_error_is_already_charged")
pi_hi = F(int(old["global_bounds"]["pi_interval"][1]), S)
check(pi_hi < F(22, 7), "audited_pi_upper_below_22_over_7")

charge = F(100, 8) * F(22, 7 * 512)**2
required = F(-29, 1000)
selected = {"top": 0, "positive_endpoint": 2, "negative_endpoint": 3}
extrema = {}
for label, j in selected.items():
    kmax = max(range(513), key=lambda k: int(rows[k]["rate_uppers"][j]))
    maximum_grid = F(int(rows[kmax]["rate_uppers"][j]), S)
    maximum_continuous = maximum_grid + charge
    extrema[label] = {
        "maximizing_grid_angle": [kmax, 512],
        "grid_upper": str(maximum_grid),
        "continuous_upper": str(maximum_continuous),
        "required_upper": str(required),
        "strict_margin": str(required - maximum_continuous),
    }
    check(maximum_continuous < required, "continuous_rate_" + label)

for k in range(512):
    bounds = {
        label: max(F(int(rows[k]["rate_uppers"][j]), S),
                   F(int(rows[k + 1]["rate_uppers"][j]), S)) + charge
        for label, j in selected.items()
    }
    passes = all(v < required for v in bounds.values())
    if not passes:
        out["failures"].append("angular_cell_" + str(k))
    out["angular_cells"].append({
        "theta_cell_pi_units": [k, k + 1, 512],
        "continuous_uppers": {key: str(v) for key, v in bounds.items()},
        "all_below_required": passes,
    })

gamma, rho_star = F(29, 1000), F(1, 32) - F(91, 5000)
check(rho_star == F(261, 20000), "sufficient_coefficient_rate")
check(gamma - rho_star == F(319, 20000) > 0,
      "strict_endpoint_rate_deficit")
out["summary"] = {
    "angular_rows_inspected": len(rows),
    "angular_cells_inspected": len(out["angular_cells"]),
    "bounds_per_cell": 3,
    "angular_chord_charge": str(charge),
    "extrema": extrema,
    "required_continuous_upper": str(required),
    "remainder_decay_rate": str(gamma),
    "sufficient_coefficient_loss_requires_rho_below": str(rho_star),
    "strict_exponent_gap_at_threshold": str(gamma - rho_star),
    "remainder_polynomial_factor": "n^2",
    "bottom_edge": "Retained as an exact signed integral, no lower or upper target-scale estimate.",
}
out["status"] = "PASS" if not out["failures"] else "FAIL"
dest.write_text(json.dumps(out, indent=2) + "\n")
print(out["status"], ": 513 audited rows; 512 cells; 3 bounds per cell")
for label, values in extrema.items():
    print(label, "continuous upper:", values["continuous_upper"],
          "required <", required)
print("Endpoint decay", gamma, "; sufficient loss must be <", rho_star,
      "; strict exponent gap:", gamma - rho_star)
print("Failures:", out["failures"], "; complete evidence:", dest)
if out["failures"]:
    raise SystemExit(1)
