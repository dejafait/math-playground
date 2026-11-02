#!/usr/bin/env python3
"""Replay all L663 intervals without overwriting the original certificate.

This uses the analytically audited producer arithmetic, not an independent
interval backend. It recomputes every terminal integral and angular row,
checks complete covers and thresholds with Fraction, and saves all results.
"""
import importlib.util
import json
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    "l663_producer", HERE / "full-circle-root-compensation.py")
p = importlib.util.module_from_spec(spec)
spec.loader.exec_module(p)
source = HERE / "full-circle-root-compensation-certificate.json"
dest = HERE / "full-circle-root-compensation-audit.json"
old = json.loads(source.read_text())
out = {
    "status": "INCOMPLETE", "scale": str(p.S),
    "scope": "Complete replay with the original interval backend; analytic and rounding audit is in L663 section 7; no independent backend or source-manuscript audit.",
    "source": source.name, "checks": {}, "failures": [],
    "derivative_replay": [], "angular_replay": [],
}


def check(ok, name):
    out["checks"][name] = bool(ok)
    if not ok:
        out["failures"].append(name)


def save():
    dest.write_text(json.dumps(out, indent=2) + "\n")


check(old["status"] == "PASS" and int(old["scale"]) == p.S,
      "source_status_and_scale")
check(not old["failures"] and not old["derivative_failures"],
      "source_failure_lists_empty")
fresh_global = p.global_bounds()
out["global_replay"] = fresh_global
check(fresh_global == old["global_bounds"], "all_global_values_reproduced")
check(all(fresh_global["checks"].values()), "all_global_thresholds")

leaves = old["derivative_leaves"]
check(len(leaves) == 8192, "exact_derivative_count")
out["derivative_extrema"] = {}
for region, el, er in [("top", p.D, p.R), ("bottom", p.E0, p.D)]:
    for sign in [-1, 1]:
        selected = [v for v in leaves
                    if v["region"] == region and v["sign"] == sign]
        by_cell = {}
        shape_ok = True
        for v in selected:
            j, jj, ne = v["e_cell"]
            k, kk, na = v["theta_cell"]
            shape_ok &= (jj, ne, kk, na, v["t_cells"]) == (
                j + 1, 16, k + 1, 128, 256)
            by_cell[(j, k)] = v
        expected = {(j, k) for j in range(16) for k in range(128)}
        label = f"{region}_{sign}"
        check(shape_ok and len(selected) == 2048 and set(by_cell) == expected,
              "complete_disjoint_cover_" + label)
        if not out["checks"]["complete_disjoint_cover_" + label]:
            save()
            raise RuntimeError("Invalid derivative cover: " + label)
        intervals = []
        for j, k in sorted(expected):
            e = p.hull(el + (er - el) * p.rat(j, 16),
                       el + (er - el) * p.rat(j + 1, 16))
            c, s = p.trig_box(k, k + 1, 128)
            val = p.derivative_integral(e, c, s, sign * p.Y, 256)
            original = by_cell[(j, k)]
            same = val.dump() == original["integral_interval"]
            threshold_ok = (F(val.hi, p.S) <= F(-3, 10) if region == "top"
                            else F(val.lo, p.S) >= F(-9, 4))
            if not same or not threshold_ok:
                out["failures"].append(f"derivative_{label}_{j}_{k}")
            out["derivative_replay"].append({
                **original, "replayed_interval": val.dump(),
                "matches": same, "threshold_pass": threshold_ok,
            })
            intervals.append((val.lo, val.hi))
        out["derivative_extrema"][label] = {
            "minimum_lower": str(F(min(v[0] for v in intervals), p.S)),
            "maximum_upper": str(F(max(v[1] for v in intervals), p.S)),
            "required": "upper <= -3/10" if region == "top" else "lower >= -9/4",
        }
        save()
        print("Replayed", label, "2048 boxes; failures:", len(out["failures"]), flush=True)

rows, comparison = p.certify_angular_rates()
out["angular_replay"] = rows
out["comparison"] = comparison
check(rows == old["angular_rows"], "every_angular_row_reproduced")
check(comparison == old["comparison"], "every_comparison_value_reproduced")
check(len(rows) == 513 and all(row["angle"] == [k, 512]
                              for k, row in enumerate(rows)), "complete_angular_grid")
check(all(int(row["maximum_upper"]) == max(map(int, row["rate_uppers"]))
          and len(row["rate_uppers"]) == 4 for row in rows), "every_edge_retained")
weighted = sum((1 if k in (0, 512) else 2) * int(row["maximum_upper"])
               for k, row in enumerate(rows))
exact_mean = F(weighted, 1024 * p.S) + F(int(comparison["angular_error_upper"]), p.S)
stored_mean = F(int(comparison["mean_upper"]), p.S)
check(exact_mean <= stored_mean < exact_mean + F(1, p.S), "exact_mean_aggregation")
check(F(int(comparison["t_error_upper"]), p.S) >= F(70, 12 * 128**2),
      "t_quadrature_charge")
pi_hi = F(p.PI.hi, p.S)
check(F(int(comparison["angular_error_upper"]), p.S) >=
      100 * pi_hi**2 / (12 * 512**2), "angular_quadrature_charge")
check(stored_mean < F(-33, 1000), "strict_mean_rate")
check(F(33, 1000) - F(1, 32) == F(7, 4000), "unsquared_rate_gap")
check(2 * F(33, 1000) - F(1, 16) == F(7, 2000), "squared_rate_gap")
out["summary"] = {
    "derivative_boxes_replayed": len(out["derivative_replay"]),
    "angular_rows_replayed": len(rows), "actual_mean_upper": str(stored_mean),
    "required_mean_upper": "-33/1000",
    "strict_margin": str(F(-33, 1000) - stored_mean),
    "squared_rate_gap": "7/2000", "unsquared_rate_gap": "7/4000",
}
out["status"] = "PASS" if not out["failures"] else "FAIL"
save()
print("Audit replay:", out["status"], "8192 derivative boxes; 513 angular rows")
print("Actual mean upper:", stored_mean, "required < -33/1000")
print("Derivative extrema:", json.dumps(out["derivative_extrema"], sort_keys=True))
print("Failures:", out["failures"], "; complete evidence:", dest)
if out["failures"]:
    raise SystemExit(1)
