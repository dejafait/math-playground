#!/usr/bin/env python3
"""Traverse both saved L036 certificates using K4 stars and full blocks."""
import hashlib
import json
from collections import Counter
from itertools import combinations, permutations, product
from pathlib import Path


def main():
    root = Path(__file__).parent
    producer_bytes = (root / "affine-four-incidence-results.json").read_bytes()
    audit_bytes = (root / "affine-four-incidence-audit-results.json").read_bytes()
    producer = json.loads(producer_bytes)
    audit = json.loads(audit_bytes)
    heads = list(combinations(range(8), 3))
    slope_of = {h: s for s, h in enumerate(heads)}
    edges = list(combinations(range(4), 2))
    triangles = list(combinations(range(4), 3))
    configurations = set()
    assignment_multiplicities = Counter()
    for labels in combinations(range(8), 6):
        for assignment in permutations(labels):
            stars = [tuple(sorted(assignment[e] for e, edge in enumerate(edges)
                                  if vertex in edge)) for vertex in range(4)]
            keys = tuple(sorted(slope_of[h] for h in stars))
            configurations.add(keys)
            assignment_multiplicities[keys] += 1
    configurations = sorted(configurations)
    checks = {}
    failures = []

    def check(name, condition):
        checks[name] = bool(condition)
        if not condition:
            failures.append(name)

    check("prime_191", all(191 % d for d in range(2, 14)))
    check("heads_56", len(heads) == 56)
    check("k4_configurations_840", len(configurations) == 840)
    check("each_k4_configuration_has_24_edge_assignments",
          set(assignment_multiplicities.values()) == {24})
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
    check("producer_parameters", producer["parameters"] == expected_parameters)
    check("producer_reduction_all_fields", producer["reduction"] == expected_reduction)
    check("saved_audit_heads", audit["all_head_configurations"] ==
          [list(s) for s in configurations])
    check("saved_audit_producer_sha256", audit["source_sha256"] ==
          hashlib.sha256(producer_bytes).hexdigest())
    p_index = a_index = 0
    counts = Counter()
    head_summaries = []
    row_failures = []
    for slopes in configurations:
        local = Counter()
        head_sets = [set(heads[s]) for s in slopes]
        check(f"head_structure_{slopes}",
              all(len(head_sets[i] & head_sets[j]) == 1 for i, j in edges)
              and all(not set.intersection(*(head_sets[i] for i in tri))
                      for tri in triangles))
        for coordinates in product(range(5), repeat=3):
            intercepts = [0] + [((slopes[0] - slopes[j]) * coordinates[j-1]) % 191
                                for j in range(1, 4)]
            # Integers 0..7 tag the head; integers >=8 tag outside points.
            blocks = [head_sets[i] | {8 + 191*x + (slopes[i]*x + intercepts[i]) % 191
                                     for x in range(5)} for i in range(4)]
            pairs = [blocks[i] & blocks[j] for i, j in edges]
            triples = [set.intersection(*(blocks[i] for i in tri)) for tri in triangles]
            pair_sizes = [len(p) - 1 for p in pairs]
            triple_sizes = [len(t) for t in triples]
            all_pairs = all(len(p) == 2 for p in pairs)
            no_triples = all(not t for t in triples)
            full_pattern = all_pairs and no_triples
            local["tested"] += 1
            local["all_six_tail_pairs"] += all_pairs
            local["all_six_tail_pairs_with_empty_triples"] += full_pattern
            local["equal_intercept_candidates"] += len(set(intercepts)) < 4
            local["repeated_first_coordinate_candidates"] += len(set(coordinates)) < 3
            expected_audit = {
                "slopes": list(slopes), "first_coordinates": list(coordinates),
                "intercepts": intercepts, "six_tail_pair_sizes": pair_sizes,
                "four_tail_triple_sizes": triple_sizes,
            }
            if (a_index >= len(audit["direct_intersection_records"]) or
                    audit["direct_intersection_records"][a_index] != expected_audit):
                row_failures.append({"certificate": "audit", "index": a_index,
                                     "expected": expected_audit})
            a_index += 1
            if len(set(coordinates)) == 3:
                local["distinct_first_coordinates"] += 1
                crossings = []
                for i, j in edges:
                    solutions = [x for x in range(191)
                                 if (slopes[i]*x + intercepts[i]) % 191 ==
                                    (slopes[j]*x + intercepts[j]) % 191]
                    if len(solutions) != 1:
                        row_failures.append({"certificate": "crossing", "index": p_index,
                                             "edge": [i, j], "solutions": solutions})
                    crossings.append(solutions[0])
                expected_producer = {
                    "slopes": list(slopes), "first_crossings": list(coordinates),
                    "intercepts": intercepts, "all_crossings": crossings,
                    "all_crossings_in_evaluation_set": all_pairs,
                    "no_tail_triple": full_pattern,
                }
                if (p_index >= len(producer["attempts"]) or
                        producer["attempts"][p_index] != expected_producer):
                    row_failures.append({"certificate": "producer", "index": p_index,
                                         "expected": expected_producer})
                p_index += 1
            if full_pattern:
                row_failures.append({"certificate": "incidence_witness",
                                     "slopes": list(slopes), "intercepts": intercepts,
                                     "blocks": [sorted(b) for b in blocks]})
        counts.update(local)
        head_summaries.append({"slopes": list(slopes), "counts": dict(local)})
    check("all_105000_audit_rows_exact", a_index == 105000 ==
          len(audit["direct_intersection_records"]) and
          not any(r["certificate"] == "audit" for r in row_failures))
    check("all_50400_producer_rows_exact", p_index == 50400 == len(producer["attempts"])
          and not any(r["certificate"] in ("producer", "crossing") for r in row_failures))
    expected_counts = {k: counts[k] for k in (
        "tested", "all_six_tail_pairs", "all_six_tail_pairs_with_empty_triples",
        "distinct_first_coordinates")}
    check("saved_audit_counts_all_fields", audit["counts"] == expected_counts)
    check("all_pairs_count_4220", counts["all_six_tail_pairs"] == 4220)
    check("zero_full_pattern_successes", counts["all_six_tail_pairs_with_empty_triples"] == 0)
    check("producer_checks_all_fields", producer["checks"] == {
        "prime_191": checks["prime_191"], "heads_count_56": checks["heads_56"],
        "head_configuration_count_840": checks["k4_configurations_840"],
        "first_crossing_options_60": counts["distinct_first_coordinates"] == 840*60,
        "witness_or_complete_search": checks["all_50400_producer_rows_exact"],
    })
    expected_audit_checks = {
        "primary_parameters_exact": checks["producer_parameters"],
        "all_reduction_fields_exact": checks["producer_reduction_all_fields"],
        "independent_head_count": checks["k4_configurations_840"],
        "all_125_coordinate_triples_per_head": counts["tested"] == 840*125,
        "all_60_distinct_coordinate_triples_per_head": counts["distinct_first_coordinates"] == 840*60,
        "all_50400_primary_records_match": checks["all_50400_producer_rows_exact"],
        "no_complete_incidence": checks["zero_full_pattern_successes"],
        "primary_no_witness": producer["witness"] is None,
        "primary_no_failures": producer["failures"] == [],
        "primary_checks_exact": checks["producer_checks_all_fields"],
    }
    check("saved_audit_checks_all_fields", audit["checks"] == expected_audit_checks)
    check("both_saved_failure_arrays_empty", producer["failures"] == audit["failures"] == [])
    check("producer_witness_null", producer["witness"] is None)
    check("no_row_failures", not row_failures)
    result = {
        "input_sha256": {"producer": hashlib.sha256(producer_bytes).hexdigest(),
                         "audit": hashlib.sha256(audit_bytes).hexdigest()},
        "method": "K4 edge assignments; full tagged eight-point blocks; exhaustive field crossings",
        "counts": dict(counts), "required": {"heads": 840, "producer_rows": 50400,
            "audit_rows": 105000, "all_pairs": 4220, "full_pattern_successes": 0},
        "head_summaries": head_summaries, "checks": checks,
        "failures": failures, "row_failures": row_failures,
        "qualification": "Fixed auxiliary family only; no labeled rank or full-family/RS conclusion.",
    }
    path = root / "affine-four-critical-audit-results.json"
    path.write_text(json.dumps(result, indent=2) + "\n")
    print(f"Heads: {len(configurations)}/840; producer rows: {p_index}/50400; audit rows: {a_index}/105000")
    print(f"All-pair cases: {counts['all_six_tail_pairs']}/4220; full-pattern successes: {counts['all_six_tail_pairs_with_empty_triples']}/0")
    print(f"Checks: {sum(checks.values())}/{len(checks)}; failures: {failures}; row failures: {len(row_failures)}")
    print(f"Certificate: {path.relative_to(Path.cwd())}")
    if failures or row_failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
