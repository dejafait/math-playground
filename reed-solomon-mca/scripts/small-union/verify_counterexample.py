"""Independent set-based verification of the selected incidence counterexample."""
import itertools
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).parent
OUT = ROOT / "selected-counterexample-verification.json"


def main():
    # Reconstruct directly from the stated seed; do not import the generator.
    seed = {0, 1, 2, 5}
    edges = [{(a + t) % 16 for a in seed} for t in range(16)]
    degrees = [sum(v in edge for edge in edges) for v in range(16)]
    distinct = len({frozenset(edge) for edge in edges})
    pairs = [(i, j) for i, j in itertools.combinations(range(16), 2)
             if edges[i].isdisjoint(edges[j])]
    triples = [(i, j, k) for i, j, k in itertools.combinations(range(16), 3)
               if edges[i].isdisjoint(edges[j]) and edges[i].isdisjoint(edges[k])
               and edges[j].isdisjoint(edges[k])]
    histogram = Counter()
    witnesses = {}
    violations = []
    for six in itertools.combinations(range(16), 6):
        union = set().union(*(edges[i] for i in six))
        size = len(union)
        histogram[size] += 1
        witnesses.setdefault(size, {"translate_indices": list(six),
                                    "union": sorted(union)})
        if size <= 8:
            violations.append(list(six))
    source = json.loads((ROOT / "cyclic-orbits-result.json").read_text())
    saved = next(r for r in source["qualifying_families"] if r["seed"] == sorted(seed))
    failures = []
    checks = {
        "sixteen_distinct_four_edges": distinct == 16 and all(len(e) == 4 for e in edges),
        "sixteen_vertices": set().union(*edges) == set(range(16)),
        "degree_four": degrees == [4] * 16,
        "matching_exactly_two": bool(pairs) and not triples,
        "all_8008_six_subsets_checked": sum(histogram.values()) == 8008,
        "no_union_at_most_eight": not violations,
        "saved_edges_match": {frozenset(e) for e in saved["edges"]} ==
                             {frozenset(e) for e in edges},
        "saved_histogram_matches": {int(k): v for k, v in saved["six_union_histogram"].items()}
                                   == dict(histogram),
        "saved_matching_counts_match": saved["disjoint_pairs"] == len(pairs)
                                       and saved["disjoint_triples"] == len(triples),
        "saved_minimum_matches": saved["minimum_six_union"] == min(histogram),
    }
    failures = [name for name, passed in checks.items() if not passed]
    result = {"seed": sorted(seed), "edges_by_translate": [sorted(e) for e in edges],
              "degrees": degrees, "disjoint_pair_count": len(pairs),
              "disjoint_pair": list(pairs[0]) if pairs else None,
              "triples_checked": 560, "disjoint_triples": [list(t) for t in triples],
              "six_subsets_checked": sum(histogram.values()),
              "six_union_histogram": dict(sorted(histogram.items())),
              "actual_minimum_union": min(histogram), "counterexample_required_minimum": 9,
              "criterion_threshold": 8, "minimum_witness": witnesses[min(histogram)],
              "union_threshold_violations": violations, "checks": checks,
              "failures": failures, "verified": not failures}
    OUT.write_text(json.dumps(result, indent=2) + "\n")
    print(f"Distinct edges {distinct}/16; degrees {sorted(set(degrees))}, required [4]")
    print(f"Disjoint pairs {len(pairs)}; disjoint triples {len(triples)}/560 checked")
    print(f"Six-edge subsets {sum(histogram.values())}/8008; actual minimum union "
          f"{min(histogram)}, required >=9; histogram {dict(sorted(histogram.items()))}")
    print(f"Failures: {failures}; verified: {not failures}")
    print(f"Certificate: {OUT.relative_to(Path.cwd())}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
