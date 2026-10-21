"""Exact arithmetic for L050's separate audit; no rank or list certificate."""

import json
from math import comb
from pathlib import Path


def main():
    total, deleted = 137**3, 137**2
    remaining = total - deleted
    numerator, denominator = 65537**28, 2**128
    threshold_floor = numerator // denominator
    cores, incidence = comb(1024, 61), comb(68, 61)
    strict_endpoint = incidence * (threshold_floor + 1)
    largest_cap = (strict_endpoint - 1) // cores
    checks = {
        "total": total == 2571353,
        "deleted": deleted == 18769,
        "remaining": remaining == 2552584 == 136 * deleted,
        "largest_sufficient_cap": largest_cap == 1532495,
        "strict_lower_endpoint": cores * largest_cap < strict_endpoint,
        "next_cap_fails": strict_endpoint <= cores * (largest_cap + 1),
        "passing_floored_certificate": cores * largest_cap // incidence <= threshold_floor,
        "failing_floored_certificate": cores * (largest_cap + 1) // incidence > threshold_floor,
        "excess": remaining - largest_cap == 1020089,
        "above_cap": remaining > largest_cap,
    }
    certificate = {
        "scope": "L050 arithmetic only; logical cases are proved in L050; imported L030/L049 certificates are not rerun",
        "counts": {"total": total, "deleted": deleted, "remaining": remaining,
                   "largest_sufficient_cap": largest_cap, "excess": remaining - largest_cap},
        "threshold": {"numerator": numerator, "denominator": denominator,
                      "floor": threshold_floor, "N": cores, "D": incidence,
                      "strict_endpoint": strict_endpoint,
                      "passing_product": cores * largest_cap,
                      "failing_product": cores * (largest_cap + 1)},
        "checks": checks,
        "failures": [name for name, passed in checks.items() if not passed],
    }
    path = Path(__file__).with_name("fixed-core-transversal-audit-results.json")
    path.write_text(json.dumps(certificate, indent=2) + "\n")
    print(f"Checks: {sum(checks.values())}/{len(checks)}; failures: {certificate['failures']}")
    print(f"Actual survivors: {remaining}; required uniform cap <= {largest_cap}; excess: {remaining - largest_cap}")
    print(f"Deleted: {deleted}; original: {total}; certificate: {path}")
    if certificate["failures"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
