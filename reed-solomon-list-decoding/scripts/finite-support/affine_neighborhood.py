#!/usr/bin/env python3
"""Exact L035 test; offset reduction covers every pair by common translation."""
import json
from collections import Counter
from itertools import combinations
from math import comb, isqrt
from pathlib import Path


def main():
    q = 191
    heads = list(combinations(range(8), 3))
    tails = [[frozenset(x*q + (s*x+b) % q for x in range(5))
              for b in range(q)] for s in range(len(heads))]
    failures = []
    histogram = Counter()
    same = []
    different = []
    for s, head in enumerate(heads):
        disjoint = all(not (tails[s][b] & tails[s][c])
                       for b, c in combinations(range(q), 2))
        same.append({"slope": s, "head": head, "pairs": comb(q, 2),
                     "all_disjoint": disjoint})
        if not disjoint:
            failures.append({"same_slope": s})
        histogram[3, 0] += comb(q, 2)
    # Translation (x,y) -> (x,y-b) sends (s,b),(t,c) to
    # (s,0),(t,c-b). Each offset occurs exactly q times.
    for s, t in combinations(range(len(heads)), 2):
        head_common = len(set(heads[s]) & set(heads[t]))
        sizes = [len(tails[s][0] & tails[t][delta]) for delta in range(q)]
        for delta, outside_common in enumerate(sizes):
            histogram[head_common, outside_common] += q
            if outside_common > 1 or head_common+outside_common >= 4:
                failures.append({"slopes": [s, t], "offset": delta,
                                 "head_common": head_common,
                                 "outside_common": outside_common})
            if head_common == 0 and outside_common == 3:
                failures.append({"anchored_incidence": [s, t, delta]})
        different.append({"slopes": [s, t], "heads": [heads[s], heads[t]],
                          "head_common": head_common,
                          "outside_sizes_by_offset": sizes,
                          "offset_histogram": dict(sorted(Counter(sizes).items())),
                          "multiplicity_each_offset": q})
    stages = [{"head_weight": 0, "head_length": 5,
               "tail_weight": 5, "tail_length": 956, "distance": 10,
               "dividend": 956, "divisor": 5, "cap": 956//5,
               "remainder": 956 % 5}]
    cap = 956//5
    for weight, length in [(1, 6), (2, 7), (3, 8)]:
        dividend = length*cap
        cap, remainder = divmod(dividend, weight)
        stages.append({"head_weight": weight, "head_length": length,
                       "tail_weight": 5, "tail_length": 956, "distance": 10,
                       "dividend": dividend, "divisor": weight,
                       "cap": cap, "remainder": remainder})
    cardinality = len(heads)*q
    vertices = [{"head": heads[s], "slope": s, "intercept": b,
                 "outside_points": sorted(tails[s][b])}
                for s in range(len(heads)) for b in range(q)]
    checks = {
        "prime_191": all(q % d for d in range(2, isqrt(q)+1)),
        "outside_space": 5*q+1 == 956,
        "distinct_56_slopes": len(heads) == comb(8, 3) == 56 < q,
        "every_vertex_has_sizes_3_5": all(len(v["head"]) == 3 and
                                                 len(v["outside_points"]) == 5 for v in vertices),
        "vertices_distinct": len({(tuple(v["head"]), tuple(v["outside_points"]))
                                   for v in vertices}) == cardinality,
        "same_slope_all_disjoint": all(r["all_disjoint"] for r in same),
        "all_slope_pairs_recorded": len(different) == comb(56, 2),
        "all_offset_records": all(len(r["outside_sizes_by_offset"]) == q for r in different),
        "every_slope_pair_histogram": all(r["offset_histogram"] == {0: 186, 1: 5}
                                          for r in different),
        "covers_every_unordered_vertex_pair": sum(histogram.values()) == comb(cardinality, 2),
        "no_pair_conflict": all(a+b <= 3 for a, b in histogram),
        "no_anchored_L033_incidence": all(not (a == 0 and b == 3) for a, b in histogram),
        "source_octant_all_stages": all(r["head_length"] <= r["tail_length"] and
                                          2*r["head_weight"] <= r["head_length"] and
                                          2*r["tail_weight"] <= r["tail_length"] for r in stages),
        "nested_caps": [r["cap"] for r in stages] == [191, 1146, 4011, 10696],
        "attains_upper_bound": cardinality == cap == 10696,
    }
    failures.extend(k for k, ok in checks.items() if not ok)
    result = {"parameters": {"head_length": 8, "head_weight": 3, "tail_length": 956,
                              "tail_weight": 5, "distance": 10, "q_aux": q,
                              "evaluation_points": list(range(5)), "spare_point": 955},
              "benchmark": {"stages_inside_out": stages, "ordinary_cap": cap,
                            "construction_size": cardinality},
              "vertices": vertices,
              "pair_evidence": {"same_slope": same, "distinct_slope_offsets": different,
                                "unordered_pairs_covered": sum(histogram.values()),
                                "histogram": [{"head_common": a, "outside_common": b, "count": n}
                                              for (a, b), n in sorted(histogram.items())]},
              "checks": checks, "failures": failures,
              "qualification": "Offset evidence plus common vertical translation covers every abstract pair. The all-bijection graph proof is in L035; full L034 admissibility, family-cap conversion and RS realization are not checked or claimed."}
    path = Path(__file__).with_name("affine-neighborhood-results.json")
    path.write_text(json.dumps(result, indent=2)+"\n")
    print(f"Construction size: {cardinality}; ordinary upper benchmark: {cap}")
    print(f"Pairs covered: {sum(histogram.values())}; offset cases: {len(different)*q}")
    print(f"Checks: {sum(checks.values())}/{len(checks)}; failures: {failures}")
    print(f"Certificate: {path.relative_to(Path.cwd())}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
