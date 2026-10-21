"""Exact abstract witness; this supplies no error weights or moments."""

from collections import Counter
from itertools import combinations
import json
from pathlib import Path


def factorization():
    # W is {0,...,4,5}; 5 is the fixed vertex in the round-robin formula.
    return [
        [tuple(sorted((5, r)))]
        + [tuple(sorted(((r + i) % 5, (r - i) % 5))) for i in (1, 2)]
        for r in range(5)
    ]


factors = factorization()
triples = [(a, edge) for a in range(4) for edge in factors[a]]


def find_pairs(remaining):
    if not remaining:
        return []
    i = remaining[0]
    a, edge = triples[i]
    for j in remaining[1:]:
        b, other = triples[j]
        if a == b or set(edge) & set(other):
            continue
        tail = find_pairs([k for k in remaining if k not in (i, j)])
        if tail is not None:
            return [(i, j)] + tail
    return None


pairs = find_pairs(list(range(12)))
assert pairs is not None
U, K0, W = set(range(6)), set(range(6, 10)), set(range(10, 16))
selected = [sorted(U - {2 * i, 2 * i + 1}) for i in range(3)]
supports = list(selected) + [sorted(K0)]
tagged = []
for tag, pair in enumerate(pairs):
    for index in pair:
        a, edge = triples[index]
        outside = [6 + a] + [10 + w for w in edge]
        tagged.append({"tag": tag, "factor": a, "W_edge": list(edge),
                       "outside": sorted(outside)})
        supports.append(sorted([tag] + outside))

support_sets = [set(s) for s in supports]
degree = Counter(v for s in supports for v in s)
triple_checks = []
failures = []
for indices in combinations(range(16), 3):
    edges = [support_sets[i] for i in indices]
    union = set.union(*edges)
    common = set.intersection(*edges)
    omitted = [union - e for e in edges]
    valid = len(union) > 8 or (
        len(union) in (5, 6)
        and len(common) == 12 - 2 * len(union)
        and all(len(z) == len(union) - 4 for z in omitted)
        and all(not omitted[i] & omitted[j] for i, j in combinations(range(3), 2))
    )
    row = {"indices": list(indices), "union": sorted(union),
           "common": sorted(common), "L032_condition": valid}
    triple_checks.append(row)
    if not valid:
        failures.append({"check": "L032", **row})

six_checks = [
    {"indices": list(indices),
     "union_size": len(set.union(*(support_sets[i] for i in indices)))}
    for indices in combinations(range(16), 6)
]
for row in six_checks:
    if row["union_size"] <= 8:
        failures.append({"check": "L031", **row})

checks = {
    "five_factors_partition_K6": Counter(e for f in factors for e in f)
                                  == Counter(combinations(range(6), 2)),
    "each_factor_perfect_matching": all(
        Counter(v for e in f for v in e) == Counter(range(6)) for f in factors),
    "six_disjoint_tag_pairs": len(pairs) == 6 and all(
        not set(tagged[2 * i]["outside"]) & set(tagged[2 * i + 1]["outside"])
        for i in range(6)),
    "all_degrees_four": dict(degree) == {v: 4 for v in range(16)},
    "sixteen_distinct_four_supports": len({tuple(s) for s in supports}) == 16
                                        and all(len(s) == 4 for s in supports),
    "outside_pair_packing": all(
        len(set(a["outside"]) & set(b["outside"])) <= 1
        for a, b in combinations(tagged, 2)),
    "all_outside_triples_have_one_K0_label": all(
        len(set(row["outside"]) & K0) == 1 for row in tagged),
    "leave_on_W_is_fifth_factor":
        set(combinations(range(6), 2)) - {e for f in factors[:4] for e in f}
        == set(factors[4]),
}
failures.extend({"check": k} for k, v in checks.items() if not v)
result = {
    "scope": "Abstract supports only; arbitrary auxiliary labels, no F97 assignment, weights, parameters or moments.",
    "factors": factors, "tag_pairing": pairs, "tagged_triples": tagged,
    "supports": supports, "degrees": dict(degree), "checks": checks,
    "triple_checks": triple_checks, "six_checks": six_checks,
    "summary": {
        "triple_count": len(triple_checks),
        "triple_union_histogram": dict(sorted(Counter(len(r["union"]) for r in triple_checks).items())),
        "small_union_triples": [r for r in triple_checks if len(r["union"]) <= 8],
        "six_subset_count": len(six_checks),
        "minimum_six_union": min(r["union_size"] for r in six_checks),
        "required_minimum_six_union": 9,
        "failure_count": len(failures),
    },
    "failures": failures,
}
path = Path(__file__).with_name("profile-witness-result.json")
path.write_text(json.dumps(result, indent=2) + "\n")
print(f"Abstract witness: {len(supports)} supports, degrees {min(degree.values())}–{max(degree.values())} (required 4).")
print(f"L032 checks: {len(triple_checks)} complete triples; small-union triples: {len(result['summary']['small_union_triples'])}.")
print(f"L031 checks: {len(six_checks)} complete six-subsets; actual minimum union {result['summary']['minimum_six_union']}, required >=9.")
print(f"Failures: {len(failures)}. Certificate: {path.relative_to(Path.cwd())}")
if failures:
    raise SystemExit(1)
