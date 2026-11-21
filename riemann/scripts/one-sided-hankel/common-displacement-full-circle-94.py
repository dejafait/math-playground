#!/usr/bin/env python3
"""Replay the complete angular evidence for the common-shift contour test.

All load-bearing comparisons use integers or Fractions. The inherited
L663 interval backend is reused, not independently implemented here.
The original files are read only. Full new angular rows and exact bounds
are saved before a concise report is printed.
"""
import argparse
import hashlib
import importlib.util
import json
from fractions import Fraction
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        help="Save a separate replay without replacing the original certificate.")
    args = parser.parse_args()
    base = Path(__file__).resolve().parent
    producer = base / "full-circle-root-compensation.py"
    original = base / "full-circle-root-compensation-certificate.json"
    spec = importlib.util.spec_from_file_location("inherited_contour", producer)
    backend = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(backend)
    raw = original.read_bytes()
    old = json.loads(raw)
    failures = []
    checks = {}

    def check(label, condition):
        checks[label] = bool(condition)
        if not condition:
            failures.append(label)

    scale = backend.S
    check("original_status", old["status"] == "PASS")
    check("original_scale", int(old["scale"]) == scale)
    check("original_failures_empty", not old["failures"] and not old["derivative_failures"])
    global_bounds = backend.global_bounds()
    check("global_arithmetic_replayed", global_bounds == old["global_bounds"])
    check("global_checks", all(global_bounds["checks"].values()))

    # Inspect every inherited derivative value and complete rectangle cover.
    # Their interval operations were replayed in the prior L663 audit.
    derivative_groups = {}
    expected = {(j, k) for j in range(16) for k in range(128)}
    leaves = old["derivative_leaves"]
    for region in ("top", "bottom"):
        for sign in (-1, 1):
            group = [v for v in leaves if v["region"] == region and v["sign"] == sign]
            cells, values = [], []
            valid_shape = valid_order = valid_threshold = True
            for row in group:
                j, jj, ne = row["e_cell"]
                k, kk, na = row["theta_cell"]
                valid_shape &= (jj, ne, kk, na, row["t_cells"]) == (j + 1, 16, k + 1, 128, 256)
                lo, hi = map(int, row["integral_interval"])
                valid_order &= lo <= hi
                valid_threshold &= 10 * hi <= -3 * scale if region == "top" else 4 * lo >= -9 * scale
                cells.append((j, k))
                values.append((lo, hi))
            name = f"{region}_{sign}"
            check(name + "_complete_disjoint_cover", len(cells) == len(expected) and set(cells) == expected)
            check(name + "_shape", valid_shape)
            check(name + "_interval_order", valid_order)
            check(name + "_threshold", valid_threshold)
            derivative_groups[name] = {
                "count": len(group),
                "minimum_lower": str(min(v[0] for v in values)),
                "maximum_upper": str(max(v[1] for v in values)),
                "required": "upper <= -3/10" if region == "top" else "lower >= -9/4",
            }
    check("all_derivative_rows_accounted_for", len(leaves) == 8192)

    # Recompute every interval at all four edges and all 513 angles.
    rows, comparison = backend.certify_angular_rates(na=512, nt=128)
    check("all_angular_rows_reproduced", rows == old["angular_rows"])
    check("inherited_mean_comparison_reproduced", comparison == old["comparison"])
    check("full_angular_cover", [r["angle"] for r in rows] == [[k, 512] for k in range(513)])
    check("every_edge_retained", all(len(r["rate_uppers"]) == 4 and int(r["maximum_upper"]) == max(map(int, r["rate_uppers"])) for r in rows))

    # Pointwise chord error C*delta^2/8, not the old integrated error /12.
    angular_error = (100 * backend.PI.sq() / backend.rat(8 * 512**2)).hi
    node_maximum = max(int(r["maximum_upper"]) for r in rows)
    uniform_upper = Fraction(node_maximum + angular_error, scale)
    required = Fraction(-1, 500)
    check("uniform_contour_rate", uniform_upper < required)

    d, radius, u, y = Fraction(5, 4), Fraction(11, 8), Fraction(121, 64), Fraction(9, 20)
    e0, amax = Fraction(117, 100), Fraction(29, 20)
    ordinate_lipschitz = 1 / (e0 - 1) + 1 / (u - amax) + 1 / (3 * e0)
    check("ordinate_lipschitz_below_10", ordinate_lipschitz < 10)
    check("full_rectangle_radius", radius**2 + y**2 < amax**2)
    motion_charge = 10 * Fraction(27, 20)
    total_constant_charge = 8 + motion_charge
    check("constant_charge_below_22", total_constant_charge < 22)
    contour_prefactor = Fraction(221, 100) * Fraction(20, 27) / (3 * radius)
    check("contour_prefactor_below_one", contour_prefactor < 1)

    # M>=1: |H_M((-10/11)zeta)|/R >= 8/231 > 1/32.
    anchor_lower = Fraction(8, 231)
    check("anchor_modulus_above_1_32", anchor_lower > Fraction(1, 32))
    onset = 30000
    # E_n = n^2 exp(22-n/500) is decreasing for n>1000.
    check("onset_in_decreasing_region", onset > 1000)
    onset_exponent = Fraction(onset, 500) - 22
    check("onset_exponent_is_38", onset_exponent == 38)
    onset_error_upper = Fraction(onset**2, 2**38)  # exp(38)>2^38.
    check("uniform_anchor_error", onset_error_upper < Fraction(1, 64))
    rate_margin = Fraction(1, 16) - 2 * Fraction(91, 5000)
    check("positive_original_D_margin", rate_margin == Fraction(261, 10000) and rate_margin > 0)

    out = {
        "status": "PASS" if not failures else "FAIL",
        "scope": "Complete angular interval replay, inherited derivative terminal/cover inspection, and exact specialization constants; the analytic argument and source manuscripts require their stated separate review.",
        "original_certificate": str(original.relative_to(base.parent.parent)),
        "original_sha256": hashlib.sha256(raw).hexdigest(),
        "interval_producer": str(producer.relative_to(base.parent.parent)),
        "interval_producer_sha256": hashlib.sha256(producer.read_bytes()).hexdigest(),
        "scale": str(scale),
        "checks": checks,
        "global_bounds": global_bounds,
        "inherited_derivative_groups": derivative_groups,
        "derivative_rows_inspected": len(leaves),
        "angular_rows": rows,
        "uniform_comparison": {
            "node_maximum_upper": str(node_maximum),
            "pointwise_angular_error_upper": str(angular_error),
            "actual_upper": str(uniform_upper),
            "required_upper": str(required),
            "positive_margin": str(required - uniform_upper),
        },
        "specialization": {
            "ordinate_lipschitz_upper": str(ordinate_lipschitz),
            "moving_side_exponent_charge": str(motion_charge),
            "total_constant_exponent_charge": str(total_constant_charge),
            "contour_prefactor": str(contour_prefactor),
            "anchor_modulus_lower": str(anchor_lower),
            "onset": onset,
            "onset_error_upper_using_exp_gt_2": str(onset_error_upper),
            "required_error_upper": "1/64",
            "original_D_rate_margin": str(rate_margin),
        },
        "failures": failures,
    }
    dest = (args.output.resolve() if args.output else
            base / "common-displacement-full-circle-certificate-94.json")
    dest.write_text(json.dumps(out, indent=2) + "\n")
    print("Certificate:", out["status"], "; angular rows replayed:", len(rows), "; inherited derivative rows inspected:", len(leaves))
    print("Uniform contour upper:", uniform_upper, "; required <", required)
    print("Onset error upper:", onset_error_upper, "; required < 1/64; onset:", onset)
    print("Original-D rate margin:", rate_margin, "; required > 0")
    print("Failures:", failures)
    print("Full certificate:", dest.relative_to(base.parent.parent))
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
