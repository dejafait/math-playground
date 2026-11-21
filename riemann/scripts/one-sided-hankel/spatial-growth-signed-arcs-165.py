#!/usr/bin/env python3
"""Exact auxiliary arithmetic for C708a; not an analytic-proof certificate."""

from fractions import Fraction as F
import json
from pathlib import Path


def value(x):
    return {"exact": str(x), "decimal_diagnostic": float(x)}


def main():
    d, R = F(5, 4), F(11, 8)
    s, outer = F(65, 64), F(33, 32)
    rho_sq = F(2824, 3025)
    rows = []

    def check(name, actual, relation, required):
        passed = {"<": actual < required, ">": actual > required,
                  "=": actual == required}[relation]
        rows.append({"name": name, "actual": value(actual),
                     "relation": relation, "required": value(required),
                     "passed": passed})

    check("outer_spatial_poles_excluded", outer**2 * rho_sq, "<", F(1))
    check("target_spatial_poles_excluded", s**2 * rho_sq, "=", F(59657, 61952))
    check("target_spatial_radius_margin", s**2 * rho_sq, "<", F(1))
    check("anchor_outer_denominator", R - d * outer, "=", F(11, 128))
    check("anchor_target_denominator", R - d * s, "=", F(27, 256))
    check("anchor_growth_ratio", (R - d) / (R - d * s), "=", F(32, 27))
    # theta=log(outer/s)/log(outer)>1/3 is exactly this comparison.
    check("three_circles_weight_gt_one_third", (outer / s)**3, ">", outer)
    check("interpolated_rate_fraction", F(1, 3) - F(2, 3) / 8, "=", F(1, 4))
    # The previous off-center disk does not automatically cover the target.
    check("offcenter_full_target_reaches_pole_limit", (s + F(1, 2))**2,
          ">", F(6481, 2824))

    out = Path(__file__).with_suffix(".json")
    failures = [row["name"] for row in rows if not row["passed"]]
    certificate = {
        "scope": "Exact auxiliary rational comparisons only; no proof of uniform analytic limits or B_sp=o(n).",
        "parameters": {"s": str(s), "outer_radius": str(outer), "rho_squared": str(rho_sq)},
        "checks": rows,
        "summary": {"passed": len(rows) - len(failures), "total": len(rows), "failures": failures},
        "unresolved": ["complementary angular growth", "effective arc widths and onsets",
                       "full B_sp=o(n)", "amplitude/full charge/H/support/Xi realization"]
    }
    out.write_text(json.dumps(certificate, indent=2) + "\n")
    for row in rows:
        print(f"{row['name']}: {row['actual']['exact']} {row['relation']} "
              f"{row['required']['exact']}; {'PASS' if row['passed'] else 'FAIL'}")
    print(f"Passed {len(rows) - len(failures)}/{len(rows)}; failures={failures}; certificate={out}")
    raise SystemExit(bool(failures))


if __name__ == "__main__":
    main()
