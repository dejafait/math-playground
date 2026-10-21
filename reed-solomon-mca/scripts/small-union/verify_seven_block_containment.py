"""Independent set-orbit and incidence-profile verification.

Does not import the search or the old orbit generator. Stores every tested
extension and a first incidence-class discrepancy for each rejection.
"""
from collections import Counter, defaultdict
from itertools import combinations
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SAVED = HERE / "cyclic-orbits-result.json"
SEARCH = HERE / "seven-block-containment-result.json"
OUT = HERE / "seven-block-containment-verification.json"
UNIVERSE = set(range(16))
PATTERN = [set((t, t + 1, t + 2, t + 5)) for t in range(7)]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def integer_key(edge):
    return sum(2 ** v for v in edge)


def profile(edges):
    return Counter(sum(2 ** i for i, edge in enumerate(edges) if v in edge)
                   for v in range(16))


def verify(result):
    old = json.loads(SAVED.read_text())
    search = json.loads(SEARCH.read_text())
    require(search["pattern"] == [sorted(edge) for edge in PATTERN], "Pattern mismatch")
    # Reconstruct the partition of all 1820 seeds by explicit set addition,
    # rather than the original generator's bit rotations and representative list.
    remaining = {frozenset(edge) for edge in combinations(range(16), 4)}
    seed_count = len(remaining)
    rebuilt = []
    while remaining:
        seed = min(remaining, key=lambda e: tuple(sorted(e)))
        orbit = {frozenset((v + shift) % 16 for v in seed) for shift in range(16)}
        require(orbit <= remaining, "Translation orbits do not partition remaining seeds")
        remaining.difference_update(orbit)
        ordered = sorted(orbit, key=integer_key)
        row = {"seed_mask": integer_key(ordered[0]), "orbit_size": len(ordered)}
        if len(ordered) == 16:
            pairs = [(i, j) for i, j in combinations(range(16), 2)
                     if ordered[i].isdisjoint(ordered[j])]
            triples = [(i, j, k) for i, j, k in combinations(range(16), 3)
                       if ordered[i].isdisjoint(ordered[j])
                       and ordered[i].isdisjoint(ordered[k])
                       and ordered[j].isdisjoint(ordered[k])]
            category = "at_least_three" if triples else "two" if pairs else "one"
            row.update({"degrees": [sum(v in edge for edge in ordered) for v in range(16)],
                        "disjoint_pairs": len(pairs), "disjoint_triples": len(triples),
                        "matching_category": category})
            require(row["degrees"] == [4] * 16, "Full-orbit regularity failed")
        rebuilt.append((row, ordered))
    rebuilt.sort(key=lambda item: item[0]["seed_mask"])
    orbit_rows = [row for row, _ in rebuilt]
    require(old["orbit_records"] == orbit_rows, "Saved orbit records differ from set reconstruction")
    sizes = Counter(row["orbit_size"] for row in orbit_rows)
    categories = Counter(row["matching_category"] for row in orbit_rows if row["orbit_size"] == 16)
    require(old["seed_count"] == seed_count == 1820, "Seed count mismatch")
    require(old["translation_orbit_count"] == len(rebuilt) == 116, "Orbit count mismatch")
    require(old["orbit_size_counts"] == {str(k): v for k, v in sorted(sizes.items())},
            "Saved orbit sizes mismatch")
    require(old["full_orbit_matching_categories"] == dict(sorted(categories.items())),
            "Saved matching categories mismatch")
    qualifying = [(row, edges) for row, edges in rebuilt
                  if row.get("matching_category") == "two"]
    require(len(qualifying) == len(old["qualifying_families"]) == 62,
            "Qualifying family count mismatch")
    require([r["seed_mask"] for r in old["qualifying_families"]]
            == [r["seed_mask"] for r, _ in qualifying], "Qualifying seeds mismatch")
    require([r["seed_mask"] for r in search["families"]]
            == [r["seed_mask"] for r, _ in qualifying], "Search seeds mismatch")
    result["enumeration"] = {
        "seed_count": seed_count, "translation_orbit_count": len(rebuilt),
        "orbit_size_counts": dict(sorted(sizes.items())),
        "full_orbit_matching_categories": dict(sorted(categories.items())),
        "complete_orbit_records": orbit_rows, "saved_records_equal": True,
        "unused_source_fields": "Six-edge union histograms and minima are not inputs to containment",
    }
    expected = [profile(PATTERN[:k]) for k in range(1, 8)]
    verified = []
    for (row, edges), saved, tested in zip(qualifying, old["qualifying_families"], search["families"]):
        key = row["seed_mask"]
        require(saved["seed"] == sorted(edges[0]) == tested["seed"], f"Seed vertices {key}")
        require(saved["edge_masks"] == [integer_key(edge) for edge in edges], f"Edge masks {key}")
        require(saved["edges"] == [sorted(edge) for edge in edges], f"Edge lists {key}")
        require(saved["degrees"] == row["degrees"], f"Degrees {key}")
        require(saved["disjoint_pairs"] == row["disjoint_pairs"]
                and saved["disjoint_triples"] == row["disjoint_triples"], f"Matching data {key}")
        i, j = saved["disjoint_pair"]
        require(i != j and edges[i].isdisjoint(edges[j]), f"Disjoint-pair witness {key}")
        require(profile([edges[0]]) == expected[0], f"Normalized root {key}")
        levels = [[[0]]]
        audit = []
        trial_counts = [1]
        rejected_counts = [0]
        for depth in range(2, 8):
            next_level = []
            trials = []
            for prefix in levels[-1]:
                for candidate in range(16):
                    if candidate in prefix:
                        continue
                    proposed = prefix + [candidate]
                    actual = profile([edges[index] for index in proposed])
                    differences = [signature for signature in sorted(set(actual) | set(expected[depth - 1]))
                                   if actual[signature] != expected[depth - 1][signature]]
                    accepted = not differences
                    entry = {"prefix": prefix, "candidate": candidate, "accepted": accepted}
                    if accepted:
                        next_level.append(proposed)
                    else:
                        signature = differences[0]
                        entry["first_discrepancy"] = {
                            "incidence_signature": signature,
                            "host_count": actual[signature],
                            "required_pattern_count": expected[depth - 1][signature]}
                    trials.append(entry)
            levels.append(next_level)
            audit.append({"depth": depth, "complete_candidate_checks": trials})
            trial_counts.append(len(trials))
            rejected_counts.append(sum(not trial["accepted"] for trial in trials))
        require(levels == tested["complete_prefix_levels"], f"Complete prefix levels {key}")
        require(trial_counts == tested["candidate_trials_by_depth"], f"Trial counts {key}")
        require(rejected_counts == tested["rejections_by_depth"], f"Rejection counts {key}")
        positive = bool(levels[-1])
        require(positive == tested["contains"], f"Containment classification {key}")
        if positive:
            mapping = {int(v): w for v, w in tested["injective_vertex_map"].items()}
            pattern_union = set().union(*PATTERN)
            require(set(mapping) == pattern_union, f"Witness domain {key}")
            require(len(set(mapping.values())) == 12 and set(mapping.values()) <= UNIVERSE,
                    f"Witness injectivity {key}")
            targets = tested["witness_edge_indices"]
            require(targets in levels[-1], f"Witness edge prefix {key}")
            require(all(frozenset(mapping[v] for v in edge) == edges[targets[t]]
                        for t, edge in enumerate(PATTERN)), f"All seven image edges {key}")
            # A witnessed full isomorphism, rather than a failed affine search,
            # justifies the statement that these positives add no abstract family.
            full_map = tested["full_L025_isomorphism"]
            require(full_map is not None and set(full_map) == UNIVERSE, f"Full map bijectivity {key}")
            full_pattern = [frozenset((t + a) % 16 for a in (0, 1, 2, 5)) for t in range(16)]
            require({frozenset(full_map[v] for v in edge) for edge in full_pattern} == set(edges),
                    f"All sixteen image edges {key}")
        else:
            require(tested["injective_vertex_map"] is None and tested["witness_edge_indices"] is None,
                    f"Negative witness fields {key}")
        verified.append({"seed_mask": key, "seed": sorted(edges[0]),
                         "complete_edges": [sorted(edge) for edge in edges],
                         "contains": positive, "complete_prefix_levels": levels,
                         "complete_extension_audit": audit,
                         "injective_vertex_map": tested["injective_vertex_map"],
                         "witness_edge_indices": tested["witness_edge_indices"],
                         "full_L025_isomorphism": tested["full_L025_isomorphism"],
                         "all_checks_passed": True})
    positives = [row for row in verified if row["contains"]]
    summary = {"families_verified": len(verified), "required_families": 62,
               "positive_count": len(positives), "negative_count": len(verified) - len(positives),
               "positive_seed_masks": [row["seed_mask"] for row in positives],
               "positive_seeds": [row["seed"] for row in positives],
               "all_positives_isomorphic_to_L025": True,
               "accepted_prefixes_by_depth": [sum(len(row["complete_prefix_levels"][k])
                                                   for row in verified) for k in range(7)],
               "candidate_trials": sum(sum(row["candidate_trials_by_depth"])
                                       for row in search["families"]),
               "failures": [], "status": "VERIFIED_EXACT_FINITE_SCOPE"}
    for key in ("positive_count", "negative_count", "positive_seed_masks", "positive_seeds",
                "accepted_prefixes_by_depth", "candidate_trials"):
        require(summary[key] == search["summary"][key], f"Search summary {key}")
    require(search["summary"]["families_tested"] == search["summary"]["required_families"] == 62,
            "Search summary coverage")
    require(search["summary"]["positive_full_L025_isomorphisms"] == len(positives),
            "Search summary isomorphisms")
    result["families"] = verified
    result["positive_witnesses"] = [
        {"seed_mask": row["seed_mask"], "seed": row["seed"],
         "witness_edge_indices": row["witness_edge_indices"],
         "injective_vertex_map": row["injective_vertex_map"],
         "full_L025_isomorphism": row["full_L025_isomorphism"]}
        for row in positives]
    result["summary"] = summary


def main():
    result = {"scope": "Independent verification of exact containment in all 62 saved cyclic families",
              "method": "Set-orbit reconstruction and exhaustive ordered-edge incidence profiles"}
    try:
        verify(result)
    except Exception as error:
        result["summary"] = {"status": "FAILED", "failures": [str(error)]}
        OUT.write_text(json.dumps(result, indent=2) + "\n")
        print(f"Failure: {error}; certificate {OUT.relative_to(Path.cwd())}")
        raise
    OUT.write_text(json.dumps(result, indent=2) + "\n")
    s = result["summary"]
    print(f"Independent verification: {s['families_verified']}/{s['required_families']} families")
    print(f"Positive {s['positive_count']}; exhaustive negative {s['negative_count']}; "
          f"new abstract positive families 0")
    print(f"Prefix counts {s['accepted_prefixes_by_depth']}; candidate trials {s['candidate_trials']}")
    print(f"Failures {s['failures']}; certificate {OUT.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
