"""Exact, bounded full-translate-orbit test; run from the notebook root."""
import itertools
import json
from collections import Counter
from pathlib import Path

N = 16
OUT = Path(__file__).with_name("cyclic-orbits-result.json")


def rotate(mask, shift):
    return ((mask << shift) | (mask >> (N - shift))) & ((1 << N) - 1)


def vertices(mask):
    return [v for v in range(N) if mask & (1 << v)]


def main():
    seeds = [sum(1 << v for v in s) for s in itertools.combinations(range(N), 4)]
    representatives = sorted({min(rotate(s, t) for t in range(N)) for s in seeds})
    orbit_sizes = Counter()
    matching_counts = Counter()
    rows = []
    qualifying = []
    for seed in representatives:
        edges = sorted({rotate(seed, t) for t in range(N)})
        orbit_sizes[len(edges)] += 1
        if len(edges) != N:
            rows.append({"seed_mask": seed, "orbit_size": len(edges)})
            continue
        degrees = [sum(bool(e & (1 << v)) for e in edges) for v in range(N)]
        assert degrees == [4] * N
        pairs = [(i, j) for i, j in itertools.combinations(range(N), 2)
                 if edges[i] & edges[j] == 0]
        triples = [(i, j, k) for i, j, k in itertools.combinations(range(N), 3)
                   if edges[i] & edges[j] == 0 and edges[i] & edges[k] == 0
                   and edges[j] & edges[k] == 0]
        category = "at_least_three" if triples else "two" if pairs else "one"
        matching_counts[category] += 1
        row = {"seed_mask": seed, "orbit_size": N, "degrees": degrees,
               "disjoint_pairs": len(pairs), "disjoint_triples": len(triples),
               "matching_category": category}
        rows.append(row)
        if category != "two":
            continue
        histogram = Counter()
        best = None
        witness = None
        for six in itertools.combinations(range(N), 6):
            union = 0
            for i in six:
                union |= edges[i]
            size = union.bit_count()
            histogram[size] += 1
            if best is None or size < best:
                best, witness = size, list(six)
        assert sum(histogram.values()) == 8008
        qualifying.append({"seed": vertices(seed), "seed_mask": seed,
                           "edge_masks": edges, "edges": [vertices(e) for e in edges],
                           "degrees": degrees, "disjoint_pair": list(pairs[0]),
                           "disjoint_pairs": len(pairs), "disjoint_triples": len(triples),
                           "six_union_histogram": dict(sorted(histogram.items())),
                           "minimum_six_union": best, "minimum_witness_indices": witness,
                           "counterexample": best >= 9})
    result = {"scope": "Full sixteen-translate orbits of four-subsets in Z/16Z only",
              "seed_count": len(seeds), "translation_orbit_count": len(representatives),
              "orbit_size_counts": dict(sorted(orbit_sizes.items())),
              "full_orbit_matching_categories": dict(sorted(matching_counts.items())),
              "required_counterexample_minimum": 9,
              "counterexample_count": sum(r["counterexample"] for r in qualifying),
              "orbit_records": rows, "qualifying_families": qualifying,
              "universal_statement": "COUNTEREXAMPLE_CANDIDATES_REQUIRE_INDEPENDENT_VERIFICATION"}
    OUT.write_text(json.dumps(result, indent=2) + "\n")
    print(f"Seeds {len(seeds)}; translation orbits {len(representatives)}; "
          f"sizes {dict(sorted(orbit_sizes.items()))}")
    print(f"Full-orbit matching categories: {dict(sorted(matching_counts.items()))}")
    minimum_counts = Counter(r["minimum_six_union"] for r in qualifying)
    print(f"Minimum-union frequencies: {dict(sorted(minimum_counts.items()))}; "
          "counterexample requires >=9 (criterion requires <=8)")
    print(f"Counterexample candidates: {result['counterexample_count']}; "
          "independent verification required")
    print(f"Certificate: {OUT.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
