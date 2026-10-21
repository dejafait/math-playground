#!/usr/bin/env python3
"""Independent full-certificate audit of L035, using point incidences."""
import hashlib
import json
from collections import Counter
from itertools import combinations
from math import comb
from pathlib import Path


def main():
    source = Path(__file__).with_name("affine-neighborhood-results.json")
    raw = source.read_bytes()
    saved = json.loads(raw)
    failures = []
    comparisons = Counter()

    def check(label, actual, required):
        comparisons[label.split(":")[0]] += 1
        if actual != required:
            failures.append({"label": label, "actual": actual, "required": required})

    q, n = 191, 10696
    heads = list(combinations(range(8), 3))
    check("parameters", saved["parameters"], {
        "head_length": 8, "head_weight": 3, "tail_length": 956,
        "tail_weight": 5, "distance": 10, "q_aux": q,
        "evaluation_points": list(range(5)), "spare_point": 955})
    prime_remainders = {str(d): q % d for d in [2, 3, 5, 7, 11, 13]}
    check("primality", all(prime_remainders.values()), True)
    vertices = saved["vertices"]
    check("vertex_count", len(vertices), n)
    buckets = [[] for _ in range(956)]
    keys, supports = set(), set()
    # Each stored point is decoded, rather than regenerating the producer's sets.
    for i, v in enumerate(vertices):
        s, b = divmod(i, q)
        check("vertex_schema", sorted(v), ["head", "intercept", "outside_points", "slope"])
        check("vertex_key", (v["slope"], v["intercept"]), (s, b))
        check("vertex_head", v["head"], list(heads[s]))
        points = v["outside_points"]
        check("vertex_tail_size", len(points), 5)
        check("vertex_coordinates", sorted(p // q for p in points), list(range(5)))
        check("vertex_equations", [(p % q - s * (p // q) - b) % q for p in points], [0]*5)
        check("vertex_point_range", all(0 <= p < 955 for p in points), True)
        check("vertex_order", points, sorted(set(points)))
        keys.add((s, b))
        supports.add((tuple(v["head"]), tuple(points)))
        for p in points:
            buckets[p].append(i)
    check("complete_keys", len(keys), n)
    check("distinct_supports", len(supports), n)
    check("point_degrees", [len(bucket) for bucket in buckets], [56]*955+[0])

    # All positive tail intersections, including all intercept choices.
    # Repeated pair keys would detect two or more shared outside points.
    common = Counter()
    for bucket in buckets:
        for i, j in combinations(bucket, 2):
            common[i*n+j] += 1
    check("outside_intersection_sizes", dict(Counter(common.values())), {1: 955*comb(56, 2)})
    head_common = {(s, t): len(set(heads[s]) & set(heads[t]))
                   for s, t in combinations(range(56), 2)}
    all_hist = Counter({(3, 0): 56*comb(q, 2)})
    for h in head_common.values():
        all_hist[h, 0] += q*q
    same_positive = Counter()
    for key, count in common.items():
        i, j = divmod(key, n)
        s, t = i//q, j//q
        h = 3 if s == t else head_common[s, t]
        all_hist[h, 0] -= 1
        all_hist[h, count] += 1
        if s == t:
            same_positive[s] += 1
    actual_hist = [{"head_common": h, "outside_common": c, "count": count}
                   for (h, c), count in sorted(all_hist.items()) if count]
    pe = saved["pair_evidence"]
    check("aggregate_histogram", pe["histogram"], actual_hist)
    check("pair_total", sum(all_hist.values()), comb(n, 2))
    check("saved_pair_total", pe["unordered_pairs_covered"], comb(n, 2))
    check("pair_conflicts", sum(count for (h, c), count in all_hist.items() if h+c >= 4), 0)
    check("anchored_incidence", all_hist[0, 3], 0)

    same_records = []
    check("same_record_count", len(pe["same_slope"]), 56)
    for s in range(56):
        record = {"slope": s, "head": list(heads[s]), "pairs": comb(q, 2),
                  "all_disjoint": same_positive[s] == 0}
        check("same_record", pe["same_slope"][s], record)
        same_records.append(record)
    offset_records = []
    check("offset_record_count", len(pe["distinct_slope_offsets"]), comb(56, 2))
    # Compare every offset entry, extracted from the full incidence enumeration.
    for index, (s, t) in enumerate(combinations(range(56), 2)):
        sizes = [common[(s*q)*n+t*q+delta] for delta in range(q)]
        record = {"slopes": [s, t], "heads": [list(heads[s]), list(heads[t])],
                  "head_common": head_common[s, t], "outside_sizes_by_offset": sizes,
                  "offset_histogram": {str(k): v for k, v in sorted(Counter(sizes).items())},
                  "multiplicity_each_offset": q}
        check("offset_record", pe["distinct_slope_offsets"][index], record)
        check("offset_histogram", record["offset_histogram"], {"0": 186, "1": 5})
        # Directly count all b,c for this slope pair using the incidence table.
        # Every positive offset is checked for all 191 common translates;
        # total positive-pair count then exhausts all remaining possibilities.
        for delta, size in enumerate(sizes):
            if size:
                for b in range(q):
                    check("positive_translation", common[(s*q+b)*n+t*q+(b+delta)%q], size)
        offset_records.append(record)

    stages = []
    cap = 956//5
    for w, length, dividend, divisor in [(0, 5, 956, 5), (1, 6, 1146, 1),
                                        (2, 7, 8022, 2), (3, 8, 32088, 3)]:
        if w:
            check("shortening_recurrence", dividend, length*cap)
        cap, remainder = divmod(dividend, divisor)
        stage = {"head_weight": w, "head_length": length, "tail_weight": 5,
                 "tail_length": 956, "distance": 10, "dividend": dividend,
                 "divisor": divisor, "cap": cap, "remainder": remainder}
        check("stage_octant", length <= 956 and 2*w <= length and 10 <= 956, True)
        stages.append(stage)
    check("benchmark", saved["benchmark"], {"stages_inside_out": stages,
          "ordinary_cap": cap, "construction_size": n})
    check("sharpness", cap, n)
    # These flags are compared only after independent evidence above.
    check("producer_check_count", len(saved["checks"]), 15)
    for key, value in saved["checks"].items():
        check("producer_flag:"+key, value, True)
    check("producer_failures", saved["failures"], [])
    result = {
        "source": str(source.relative_to(Path.cwd())),
        "source_sha256": hashlib.sha256(raw).hexdigest(),
        "method": "Decode every vertex and enumerate every shared-point pair; zero-intersection pairs follow by exact complement counts. Check offsets and all positive translates against these direct counts.",
        "prime_remainders": prime_remainders,
        "coverage": {"vertices": len(vertices), "point_buckets": len(buckets),
                     "positive_outside_pairs": len(common), "unordered_pairs": comb(n, 2),
                     "same_slope_pairs": 56*comb(q, 2), "distinct_slope_offset_entries": 1540*q,
                     "positive_translates_checked": 1540*5*q},
        "benchmark": {"actual_size": n, "required_upper_bound": cap, "stages": stages},
        "histogram": actual_hist,
        "same_slope": same_records, "distinct_slope_offsets": offset_records,
        "comparisons": dict(sorted(comparisons.items())), "failures": failures,
        "qualification": "Finite evidence only; L035 contains the all-bijection proof and scope audit. No full L034 admissibility or RS realization is certified."}
    target = source.with_name("affine-neighborhood-audit-results.json")
    target.write_text(json.dumps(result, indent=2)+"\n")
    print(f"Actual size {n}; required ordinary upper bound {cap}")
    print(f"Vertices {len(vertices)}; unordered pairs {comb(n, 2)}; offset entries {1540*q}")
    print(f"Comparisons {sum(comparisons.values())}; failures {len(failures)}")
    print(f"Full certificate: {target.relative_to(Path.cwd())}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
