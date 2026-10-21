#!/usr/bin/env python3
"""Check L029's finite affine family; arbitrary-label averaging is symbolic."""
import json
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb, isqrt
from pathlib import Path


def rat(x):
    return {"numerator": x.numerator, "denominator": x.denominator}


def main():
    q = 191
    pairs = list(combinations(range(7), 2))
    blocks = [(frozenset(u), frozenset(x*q + (s*x+b) % q for x in range(5)))
              for s, u in enumerate(pairs) for b in range(q)]
    histogram = Counter()
    failures = []
    checked = 0
    for i, (u, r) in enumerate(blocks):
        for v, t in blocks[i+1:]:
            a, b = len(u & v), len(r & t)
            histogram[a, b] += 1
            checked += 1
            if a+b >= 3 or (a == 0 and b == 2):
                failures.append({"pair_index": checked, "A_intersection": a, "outside_intersection": b})
    denom = comb(956, 5)
    available = Fraction(q, denom)
    required = Fraction(136, denom)
    mix = Fraction(136, q)
    checks = {
        "prime": all(q % d for d in range(2, isqrt(q)+1)),
        "outside_space_fits": 5*q+1 == 956,
        "enough_distinct_slopes": len(pairs) <= q,
        "block_count": len(blocks) == 4011,
        "blocks_distinct": len(set(blocks)) == len(blocks),
        "all_outside_parts_size_five": all(len(r) == 5 for u, r in blocks),
        "all_unordered_pairs_checked": checked == comb(4011, 2),
        "same_slope_disjoint": all(b == 0 for (a,b) in histogram if a == 2),
        "different_slopes_intersect_at_most_once": all(b <= 1 for (a,b) in histogram if a < 2),
        "no_forbidden_pairs": not failures,
        "target_tau_matches": required == Fraction(1, 48419392161),
        "valid_mixture": 0 < mix < 1 and mix*available == required,
    }
    result = {
        "parameters": {"q": q, "outside_size": 956, "groups": 5, "slopes": 21, "spare_points": 1},
        "family": {"vertices": len(blocks), "unordered_pairs_checked": checked,
                   "intersection_histogram": [{"A_intersection": a, "outside_intersection": b, "count": n}
                                              for (a,b), n in sorted(histogram.items())]},
        "mixture": {"binomial_956_5": denom, "available_coordinate": rat(available),
                    "required_coordinate": rat(required), "nonempty_weight": rat(mix),
                    "empty_weight": rat(1-mix), "available_over_required": rat(available/required)},
        "checks": checks,
        "failures": failures + [k for k, ok in checks.items() if not ok],
        "limitations": "Checks one abstract affine family completely. Uniform random bijection, restriction to every actual W_A and all-label theta membership are proved in L029; no labeled graph enumeration, global cap or RS realization is claimed.",
    }
    path = Path(__file__).with_name("conditional-pair-link-results.json")
    path.write_text(json.dumps(result, indent=2)+"\n")
    print(f"Independent-family vertices: {len(blocks)}; unordered pairs checked: {checked}")
    print(f"Available coordinate: {available}; required: {required}; ratio: {available/required}")
    print(f"Checks: {sum(checks.values())}/{len(checks)}; failures: {result['failures']}")
    print(f"Certificate: {path.relative_to(Path.cwd())}")
    if result["failures"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
