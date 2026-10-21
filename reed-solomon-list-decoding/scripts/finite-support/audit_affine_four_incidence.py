#!/usr/bin/env python3
"""Independently intersect all 840*125 normalized candidate quadruples."""
import hashlib
import json
from collections import Counter
from itertools import combinations, product
from pathlib import Path


def main():
    source = Path(__file__).with_name("affine-four-incidence-results.json")
    source_bytes = source.read_bytes()
    data = json.loads(source_bytes)
    triples = list(combinations(range(8), 3))
    edge_indices = list(combinations(range(4), 2))
    triple_indices = list(combinations(range(4), 3))
    configurations = []
    # Independent head test: precisely six head points of multiplicity two,
    # with each edge receiving one of those points.
    for keys in combinations(range(56), 4):
        multiplicities = Counter(h for key in keys for h in triples[key])
        if sorted(multiplicities.values()) != [2]*6:
            continue
        edge_points = [set(triples[keys[i]]) & set(triples[keys[j]])
                       for i, j in edge_indices]
        if all(len(p) == 1 for p in edge_points):
            configurations.append(keys)
    records = []
    restricted = []
    counts = Counter()
    for keys in configurations:
        for coordinates in product(range(5), repeat=3):
            # Solve equality with line 1 at the three chosen coordinates.
            bs = [0] + [(keys[0]*x - keys[j]*x) % 191
                        for j, x in enumerate(coordinates, start=1)]
            tails = [set((x, (keys[i]*x+bs[i]) % 191) for x in range(5))
                     for i in range(4)]
            pair_sizes = [len(tails[i] & tails[j]) for i, j in edge_indices]
            triple_sizes = [len(set.intersection(*(tails[i] for i in tri)))
                            for tri in triple_indices]
            all_pairs = pair_sizes == [1]*6
            no_triples = triple_sizes == [0]*4
            counts["tested"] += 1
            counts["all_six_tail_pairs"] += all_pairs
            counts["all_six_tail_pairs_with_empty_triples"] += all_pairs and no_triples
            if len(set(coordinates)) == 3:
                counts["distinct_first_coordinates"] += 1
                # Compare every stored modular crossing with an independent
                # trial over all 191 possible coordinates, not a modular inverse.
                crossings = []
                for i, j in edge_indices:
                    solutions = [x for x in range(191)
                                 if (keys[i]*x+bs[i]) % 191 == (keys[j]*x+bs[j]) % 191]
                    if len(solutions) != 1:
                        raise RuntimeError("Distinct lines must have exactly one field crossing")
                    crossings.append(solutions[0])
                restricted.append({"slopes": list(keys), "first_crossings": list(coordinates),
                                   "intercepts": bs, "all_crossings": crossings,
                                   "all_crossings_in_evaluation_set": all_pairs,
                                   "no_tail_triple": all_pairs and no_triples})
            records.append({"slopes": list(keys), "first_coordinates": list(coordinates),
                            "intercepts": bs, "six_tail_pair_sizes": pair_sizes,
                            "four_tail_triple_sizes": triple_sizes})
    expected_parameters = {
        "q_aux": 191, "head_length": 8, "evaluation_points": list(range(5)),
        "slope_assignment": "lexicographic three-subsets -> 0,...,55",
        "all_intercepts_allowed": True,
    }
    expected_reduction = {
        "distinct_head_configurations": 840,
        "all_head_configurations": [list(s) for s in configurations],
        "normalized_intercept_first": 0, "translation_orbit_size": 191,
        "first_crossing_options_per_head": 60,
        "complete_normalized_candidate_count": 50400,
        "attempts_executed": 50400, "search_complete": True,
        "stopped_on_verified_witness": False,
    }
    checks = {
        "primary_parameters_exact": data["parameters"] == expected_parameters,
        "all_reduction_fields_exact": data["reduction"] == expected_reduction,
        "independent_head_count": len(configurations) == 840,
        "all_125_coordinate_triples_per_head": counts["tested"] == 105000,
        "all_60_distinct_coordinate_triples_per_head": counts["distinct_first_coordinates"] == 50400,
        "all_50400_primary_records_match": restricted == data["attempts"],
        "no_complete_incidence": counts["all_six_tail_pairs_with_empty_triples"] == 0,
        "primary_no_witness": data["witness"] is None,
        "primary_no_failures": data["failures"] == [],
        "primary_checks_exact": data["checks"] == {
            "prime_191": True, "heads_count_56": True,
            "head_configuration_count_840": True, "first_crossing_options_60": True,
            "witness_or_complete_search": True},
    }
    failures = [key for key, value in checks.items() if not value]
    output = {"source_sha256": hashlib.sha256(source_bytes).hexdigest(),
              "counts": dict(counts), "checks": checks, "failures": failures,
              "all_head_configurations": [list(s) for s in configurations],
              "direct_intersection_records": records,
              "qualification": "All intercepts relevant to the incidence pattern are covered after common translation; 125 includes repeated incident coordinates. No actual-label or RS-rank conclusion."}
    path = Path(__file__).with_name("affine-four-incidence-audit-results.json")
    path.write_text(json.dumps(output, indent=2)+"\n")
    print(f"Direct candidate tests: {counts['tested']}/105000; matched primary records: {len(restricted)}/50400")
    print(f"All six tail pairs: {counts['all_six_tail_pairs']}; empty-triple successes: {counts['all_six_tail_pairs_with_empty_triples']}; required witness: 1")
    print(f"Checks: {sum(checks.values())}/{len(checks)}; failures: {failures}")
    print(f"Certificate: {path.relative_to(Path.cwd())}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
