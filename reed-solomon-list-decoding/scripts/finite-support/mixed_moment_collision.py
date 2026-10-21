"""Bounded cyclic diagnostic for the fixed map; not a universal search."""

import itertools
import json
from collections import Counter
from pathlib import Path

Q = 107
OUTPUT = Path(__file__).with_name("mixed-moment-collision-results.json")


def block(values):
    return [(0, 0), (0, 1), (0, 2)] + [
        point for c, x in enumerate(values, start=1)
        for point in [(c, 10), (c, x)]
    ]


def totals(points):
    return [sum(x for c, x in points),
            sum(x*x for c, x in points),
            sum(x*x*x for c, x in points),
            sum(c*x for c, x in points)]


def inspect_pair(left, right):
    left, right = sorted(left), sorted(right)
    common = sorted(set(left) & set(right))
    raw_left, raw_right = totals(left), totals(right)
    syndrome_left = [s % Q for s in raw_left]
    syndrome_right = [s % Q for s in raw_right]
    profiles = [sorted(Counter(c for c, x in points).values(), reverse=True)
                for points in (left, right)]
    checks = {
        "ambient_points": all(0 <= c < 9 and 0 <= x < Q
                              for c, x in left + right),
        "nine_distinct_points_each": all(len(points) == len(set(points)) == 9
                                        for points in (left, right)),
        "distinct_blocks": set(left) != set(right),
        "required_profiles": profiles == [[3, 2, 2, 2], [3, 2, 2, 2]],
        "same_syndrome": syndrome_left == syndrome_right,
        "conflict": len(common) >= 5,
    }
    return {
        "left": left, "right": right, "profiles": profiles,
        "raw_totals_left": raw_left, "raw_totals_right": raw_right,
        "syndrome_left": syndrome_left, "syndrome_right": syndrome_right,
        "intersection": common, "intersection_size": len(common),
        "required_intersection_size": 5, "checks": checks,
    }


def main():
    trials = []
    witnesses = []
    for values in itertools.permutations(range(3)):
        rotated = values[1:] + values[:1]
        result = inspect_pair(block(values), block(rotated))
        passes = all(result["checks"].values())
        trials.append({"values": values, "rotated": rotated,
                       "syndrome_left": result["syndrome_left"],
                       "syndrome_right": result["syndrome_right"],
                       "intersection_size": result["intersection_size"],
                       "is_witness": passes})
        if passes:
            witnesses.append(result)
    certificate = {
        "field_order": Q, "columns": list(range(9)),
        "profile": [3, 2, 2, 2],
        "map": ["sum x", "sum x^2", "sum x^3", "sum c*x"],
        "search_scope": "six cyclic reassignments of distinct values 0,1,2 on columns 1,2,3",
        "universal_search": False, "trials": trials,
        "witness_count": len(witnesses),
        "witness": witnesses[0] if witnesses else None,
        "failures": [] if witnesses else ["no collision in bounded test"],
    }
    OUTPUT.write_text(json.dumps(certificate, indent=2) + "\n")
    print(f"Tested {len(trials)} cyclic assignments; witnesses={len(witnesses)}")
    if witnesses:
        witness = witnesses[0]
        print(f"Intersection: actual={witness['intersection_size']}, required>=5")
        print(f"Syndromes: {witness['syndrome_left']} = {witness['syndrome_right']}")
        print(f"Failed witness checks: {[k for k, v in witness['checks'].items() if not v]}")
    print(f"Full certificate: {OUTPUT.relative_to(Path.cwd())}")
    assert witnesses, "Bounded test inconclusive; do not infer separation"


if __name__ == "__main__":
    main()
