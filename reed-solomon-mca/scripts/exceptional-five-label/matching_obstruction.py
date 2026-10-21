"""Complete K_5 edge-partition check, not a field-label or pencil search.

Run from the notebook: python3 scripts/exceptional-five-label/matching_obstruction.py
The elementary exhaustive proof is in L038; this checks its full table.
"""

import itertools
import json
from pathlib import Path


def main():
    vertices = range(5)
    edges = tuple(itertools.combinations(vertices, 2))
    matchings = tuple(
        pair for pair in itertools.combinations(edges, 2)
        if set(pair[0]).isdisjoint(pair[1])
    )
    partitions = tuple(
        candidate for candidate in itertools.combinations(matchings, 5)
        if len(set(itertools.chain.from_iterable(candidate))) == 10
    )

    # Independent branching on the least uncovered edge, choosing its partner.
    recursive = set()

    def visit(remaining, chosen):
        if not remaining:
            recursive.add(tuple(sorted(chosen)))
            return
        first = min(remaining)
        for partner in sorted(remaining - {first}):
            if set(first).isdisjoint(partner):
                visit(remaining - {first, partner},
                      chosen + [tuple(sorted((first, partner)))])

    visit(set(edges), [])

    # Order the canonical table by the matching missing vertex 0, then
    # by the partner of edge 01. These are the exhaustive proof branches.
    def table_key(partition):
        missing_zero = next(m for m in partition if all(0 not in e for e in m))
        partner_01 = next(e for m in partition if (0, 1) in m
                          for e in m if e != (0, 1))
        return missing_zero, partner_01

    partitions = tuple(sorted(partitions, key=table_key))
    intersections = [
        [len(set(left) & set(right)) for right in partitions]
        for left in partitions
    ]
    witnesses = [
        {"partitions": [i + 1, j + 1],
         "common_matchings": sorted(set(partitions[i]) & set(partitions[j]))}
        for i, j in itertools.combinations(range(len(partitions)), 2)
    ]
    failures = []
    if set(partitions) != recursive:
        failures.append("Combination and least-uncovered-edge enumerations differ.")
    if len(matchings) != 15 or len(partitions) != 6:
        failures.append("Expected 15 matchings and six complete partitions.")
    if any(w["common_matchings"] == [] for w in witnesses):
        failures.append("A pair with no common matching exists.")
    if any(len(w["common_matchings"]) != 1 for w in witnesses):
        failures.append("The table's exactly-one assertion fails.")
    minimum = min(len(w["common_matchings"]) for w in witnesses)
    result = {
        "scope": "All partitions of the ten K_5 edges into five two-edge matchings.",
        "vertices": list(vertices), "edges": edges, "matchings": matchings,
        "partitions": partitions, "intersection_matrix": intersections,
        "pair_witnesses": witnesses,
        "counts": {"edges": len(edges), "matchings": len(matchings),
                   "combination_candidates": 3003, "partitions": len(partitions),
                   "distinct_partition_pairs": len(witnesses)},
        "independent_enumeration_agrees": set(partitions) == recursive,
        "actual_minimum_common_matchings_distinct_partitions": minimum,
        "required_common_matchings_for_exceptional_completion": 0,
        "failures": failures,
    }
    destination = Path(__file__).with_name("matching-obstruction-result.json")
    destination.write_text(json.dumps(result, indent=2) + "\n")
    print(f"Complete partitions: {len(partitions)}; distinct pairs checked: {len(witnesses)}.")
    print(f"Actual minimum common matchings: {minimum}; completion requires 0.")
    print(f"Independent enumeration agrees: {set(partitions) == recursive}; failures: {failures}.")
    print(f"Full certificate: {destination}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
