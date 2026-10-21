#!/usr/bin/env python3
"""Exact fixed L035 incidence test; stop at the first fully verified witness."""
import json
from itertools import combinations, permutations
from math import comb, isqrt
from pathlib import Path


def point_list(points):
    return [list(p) for p in sorted(points)]


def main():
    q = 191
    xs = tuple(range(5))
    heads = list(combinations(range(8), 3))
    edges = list(combinations(range(4), 2))
    triples = list(combinations(range(4), 3))
    head_configurations = []
    for slopes in combinations(range(56), 4):
        hs = [set(heads[s]) for s in slopes]
        if any(len(hs[i] & hs[j]) != 1 for i, j in edges):
            continue
        if any(set.intersection(*(hs[i] for i in tri)) for tri in triples):
            continue
        head_configurations.append(slopes)
    attempts = []
    witness = None
    for slopes in head_configurations:
        for first_crossings in permutations(xs, 3):
            intercepts = [0] + [((slopes[0]-slopes[j])*first_crossings[j-1]) % q
                                 for j in range(1, 4)]
            crossings = [((intercepts[j]-intercepts[i]) *
                           pow((slopes[i]-slopes[j]) % q, -1, q)) % q
                          for i, j in edges]
            outside = all(x in xs for x in crossings)
            no_triple = outside and all(
                len({crossings[e] for e, edge in enumerate(edges) if i in edge}) == 3
                for i in range(4))
            attempts.append({"slopes": list(slopes),
                             "first_crossings": list(first_crossings),
                             "intercepts": intercepts, "all_crossings": crossings,
                             "all_crossings_in_evaluation_set": outside,
                             "no_tail_triple": no_triple})
            if not no_triple:
                continue
            # Tagged points keep head and tail disjoint; retain all entries.
            blocks = [set(("H", h) for h in heads[s]) |
                      set(("T", x, (s*x+b) % q) for x in xs)
                      for s, b in zip(slopes, intercepts)]
            pair_sets = [blocks[i] & blocks[j] for i, j in edges]
            triple_sets = [set.intersection(*(blocks[i] for i in tri)) for tri in triples]
            private = [blocks[i] - set.union(*(blocks[j] for j in range(4) if j != i))
                       for i in range(4)]
            checks = {
                "four_distinct_keys": len(set(zip(slopes, intercepts))) == 4,
                "four_distinct_blocks": len({frozenset(b) for b in blocks}) == 4,
                "all_eight_points": all(len(b) == 8 for b in blocks),
                "all_head_tail_weights": all(sum(p[0] == "H" for p in b) == 3 and
                                             sum(p[0] == "T" for p in b) == 5 for b in blocks),
                "lexicographic_slopes": all(heads[s] == tuple(sorted(p[1] for p in blocks[i]
                                                        if p[0] == "H"))
                                            for i, s in enumerate(slopes)),
                "line_equations": all(p[2] == (slopes[i]*p[1]+intercepts[i]) % q
                                      for i, b in enumerate(blocks) for p in b if p[0] == "T"),
                "every_pair_has_two_points": all(len(p) == 2 for p in pair_sets),
                "pair_sets_mutually_disjoint": all(not (a & b)
                                                     for a, b in combinations(pair_sets, 2)),
                "all_triples_empty": all(not t for t in triple_sets),
                "quadruple_empty": not set.intersection(*blocks),
                "every_private_part_has_two_points": all(len(p) == 2 for p in private),
                "union_has_twenty_points": len(set.union(*blocks)) == 20,
                "spare_unused": all(all(p[0] in ("H", "T") for p in b) for b in blocks),
            }
            if not all(checks.values()):
                raise RuntimeError(f"Candidate failed direct checks: {checks}")
            witness = {
                "keys": [{"head": list(heads[s]), "slope": s, "intercept": b}
                         for s, b in zip(slopes, intercepts)],
                "blocks": [point_list(b) for b in blocks],
                "pair_intersections": [{"edge": [i+1, j+1], "points": point_list(p)}
                                       for (i, j), p in zip(edges, pair_sets)],
                "triple_intersections": [{"indices": [i+1 for i in tri], "points": point_list(p)}
                                         for tri, p in zip(triples, triple_sets)],
                "quadruple_intersection": point_list(set.intersection(*blocks)),
                "private_parts": [point_list(p) for p in private],
                "tail_value_table": [[x]+[(s*x+b) % q for s, b in zip(slopes, intercepts)]
                                     for x in xs],
                "checks": checks,
            }
            break
        if witness is not None:
            break
    checks = {
        "prime_191": all(q % d for d in range(2, isqrt(q)+1)),
        "heads_count_56": len(heads) == comb(8, 3) == 56,
        "head_configuration_count_840": len(head_configurations) == comb(8, 6)*30 == 840,
        "first_crossing_options_60": len(list(permutations(xs, 3))) == 60,
        "witness_or_complete_search": witness is not None or len(attempts) == 840*60,
    }
    failures = [name for name, passed in checks.items() if not passed]
    result = {
        "parameters": {"q_aux": q, "head_length": 8, "evaluation_points": list(xs),
                       "slope_assignment": "lexicographic three-subsets -> 0,...,55",
                       "all_intercepts_allowed": True},
        "reduction": {"distinct_head_configurations": len(head_configurations),
                      "all_head_configurations": [list(s) for s in head_configurations],
                      "normalized_intercept_first": 0, "translation_orbit_size": q,
                      "first_crossing_options_per_head": 60,
                      "complete_normalized_candidate_count": 50400,
                      "attempts_executed": len(attempts),
                      "search_complete": len(attempts) == 50400,
                      "stopped_on_verified_witness": witness is not None},
        "attempts": attempts, "witness": witness, "checks": checks, "failures": failures,
        "qualification": "Abstract incidence only; no actual F_65537 labels, L031 rank, L033 restriction, family-cap conversion, common-center RS realization or boundary improvement is claimed.",
    }
    path = Path(__file__).with_name("affine-four-incidence-results.json")
    path.write_text(json.dumps(result, indent=2)+"\n")
    print(f"Head configurations: {len(head_configurations)}/840; candidates tested: {len(attempts)}/50400")
    print(f"Incidence witness: {witness is not None}; required: six disjoint pairs, empty triples, four private pairs")
    print(f"Checks: {sum(checks.values())}/{len(checks)}; witness checks: {sum(witness['checks'].values()) if witness else 'n/a'}; failures: {failures}")
    print(f"Certificate: {path.relative_to(Path.cwd())}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
