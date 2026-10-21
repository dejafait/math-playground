#!/usr/bin/env python3
"""Exact small auxiliary-code counts for L028; PSD is proved symbolically."""
import json
from collections import Counter
from fractions import Fraction
from math import comb, isqrt
from pathlib import Path


def rational(x):
    return {"numerator": x.numerator, "denominator": x.denominator}


def main():
    q, n, w = 137, 963, 7
    # Normalize each nonzero polynomial by its leading coefficient.
    monic = Counter()
    monic[0] += 1  # Constant 1.
    for b in range(q):
        monic[sum((x + b) % q == 0 for x in range(w))] += 1
    for b in range(q):
        for c in range(q):
            monic[sum((x*x + b*x + c) % q == 0 for x in range(w))] += 1
    neighbors = {i: (q-1)*monic[i] for i in range(3)}
    size = q**3
    orbit_sizes = {i: comb(w, i)*comb(n-w, w-i) for i in range(3)}
    conditional = {i: Fraction(neighbors[i], orbit_sizes[i]) for i in range(3)}
    tau = conditional[2]
    checks = {
        "auxiliary_field_prime": all(q % d for d in range(2, isqrt(q)+1)),
        "seven_groups_fit": w*q <= n,
        "all_monic_polynomials_counted": sum(monic.values()) == 1+q+q*q,
        "nonzero_root_bound": max(monic) <= 2,
        "all_nonzero_polynomials_counted": sum(neighbors.values()) == size-1,
        "two_root_count": neighbors[2] == comb(w, 2)*(q-1),
        "one_root_incidence": neighbors[1]+2*neighbors[2] == w*(q*q-1),
        "conditional_two_formula": tau == Fraction(q-1, comb(n-w, 5)),
        "link_mixture_weight_at_most_one": 0 <= comb(w, 2)*tau <= 1,
        "objective_exceeds_required_cap": size > 1532496,
        "objective_below_ordinary_upper_cap": size < Fraction(comb(n, 3), comb(w, 3)),
    }
    result = {
        "parameters": {"q": q, "n": n, "w": w, "unused_points": n-w*q},
        "monic_root_histogram": dict(sorted(monic.items())),
        "neighbors_by_intersection": neighbors,
        "ordered_pair_orbit_sizes": orbit_sizes,
        "diagonal": rational(Fraction(size, comb(n, w))),
        "conditional_row_values": {i: rational(t) for i, t in conditional.items()},
        "link_certificate": {
            "independent_parts": comb(w, 2),
            "constant_row": rational(tau),
            "nonempty_mixture_weight": rational(comb(w, 2)*tau),
            "empty_set_weight": rational(1-comb(w, 2)*tau),
        },
        "objective": size,
        "required_strict_upper_cap": 1532496,
        "excess": size-1532496,
        "checks": checks,
        "failures": [name for name, ok in checks.items() if not ok],
        "limitations": "Finite counts only: the permutation-average PSD identity and all-core link applicability are proved in L028, not numerically checked here. No actual RS list realization.",
    }
    path = Path(__file__).with_name("core-theta-obstruction-results.json")
    path.write_text(json.dumps(result, indent=2)+"\n")
    print(f"Feasible-lift objective: {size}; required upper cap: <1532496; excess: {size-1532496}")
    print(f"Link mixture weight: {comb(w, 2)*tau} <= 1")
    print(f"Checks: {sum(checks.values())}/{len(checks)}; failures: {result['failures']}")
    print(f"Certificate: {path.relative_to(Path.cwd())}")
    if result["failures"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
