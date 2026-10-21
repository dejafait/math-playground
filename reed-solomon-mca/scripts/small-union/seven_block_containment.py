"""Exact ordered-edge containment; certificate includes every accepted prefix.

Run from the active notebook root. No graph-matching library is required.
The verifier independently uses incidence-profile counters and set orbits.
"""
from collections import Counter, defaultdict
from functools import lru_cache
from itertools import combinations
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "cyclic-orbits-result.json"
OUT = HERE / "seven-block-containment-result.json"
N = 16
PATTERN = [sorted({t, t + 1, t + 2, t + 5}) for t in range(7)]
FULL = [frozenset((t + a) % N for a in (0, 1, 2, 5)) for t in range(N)]


def mask(values):
    return sum(1 << v for v in values)


def search(edges):
    @lru_cache(None)
    def intersection(indices):
        if not indices:
            return (1 << N) - 1
        return intersection(indices[:-1]) & edges[indices[-1]]

    # At stage k, all old subset intersections are already checked.
    # Only the 2**(k-1) subsets containing the new edge need inspection.
    obligations = []
    for k in range(1, 8):
        stage = []
        for count in range(k):
            for old in combinations(range(k - 1), count):
                positions = old + (k - 1,)
                expected = set(PATTERN[positions[0]])
                for i in positions[1:]:
                    expected.intersection_update(PATTERN[i])
                stage.append((positions, len(expected)))
        obligations.append(stage)
    # The sorted minimum orbit edge is index zero. Translation transitivity
    # normalizes any embedding's first image to this edge.
    levels = [[[0]]]
    trials = [1]
    rejected = [0]
    for k in range(2, 8):
        next_level = []
        tested = 0
        bad = 0
        for prefix in levels[-1]:
            for candidate in range(N):
                if candidate in prefix:
                    continue
                tested += 1
                proposed = prefix + [candidate]
                if all(intersection(tuple(proposed[i] for i in positions)).bit_count()
                       == expected for positions, expected in obligations[k - 1]):
                    next_level.append(proposed)
                else:
                    bad += 1
        levels.append(next_level)
        trials.append(tested)
        rejected.append(bad)
    return levels, trials, rejected


def witness(edges, prefix):
    def profiles(edge_sets):
        classes = defaultdict(list)
        for v in range(N):
            key = tuple(i for i, edge in enumerate(edge_sets) if v in edge)
            classes[key].append(v)
        return classes
    p = profiles(PATTERN)
    h = profiles([edges[i] for i in prefix])
    assert {key: len(value) for key, value in p.items()} == {
        key: len(value) for key, value in h.items()}
    mapping = {}
    for key in p:
        if key:  # Ignore the four pattern vertices absent from the seven edges.
            mapping.update(zip(p[key], h[key]))
    assert len(mapping) == 12 and len(set(mapping.values())) == 12
    assert all({mapping[v] for v in edge} == set(edges[prefix[i]])
               for i, edge in enumerate(PATTERN))
    return {str(v): mapping[v] for v in sorted(mapping)}


def affine_full_copy(edges):
    host = {frozenset(edge) for edge in edges}
    for a in range(1, N, 2):
        for b in range(N):
            mapping = [(a * v + b) % N for v in range(N)]
            if {frozenset(mapping[v] for v in edge) for edge in FULL} == host:
                return mapping
    return None  # This is not an exhaustive nonisomorphism test.


def main():
    saved = json.loads(SOURCE.read_text())
    records = []
    for family in saved["qualifying_families"]:
        edges = family["edges"]
        edge_masks = [mask(edge) for edge in edges]
        assert edge_masks == family["edge_masks"]
        levels, trials, rejected = search(edge_masks)
        positive = bool(levels[-1])
        records.append({
            "seed_mask": family["seed_mask"], "seed": family["seed"],
            "contains": positive, "complete_prefix_levels": levels,
            "candidate_trials_by_depth": trials, "rejections_by_depth": rejected,
            "witness_edge_indices": levels[-1][0] if positive else None,
            "injective_vertex_map": witness(edges, levels[-1][0]) if positive else None,
            "full_L025_isomorphism": affine_full_copy(edges) if positive else None,
        })
    positive = [r for r in records if r["contains"]]
    summary = {
        "families_tested": len(records), "required_families": 62,
        "positive_count": len(positive), "negative_count": len(records) - len(positive),
        "positive_seed_masks": [r["seed_mask"] for r in positive],
        "positive_seeds": [r["seed"] for r in positive],
        "positive_full_L025_isomorphisms": sum(r["full_L025_isomorphism"] is not None
                                               for r in positive),
        "candidate_trials": sum(sum(r["candidate_trials_by_depth"]) for r in records),
        "accepted_prefixes_by_depth": [sum(len(r["complete_prefix_levels"][k])
                                           for r in records) for k in range(7)],
        "failures": [], "status": "INDEPENDENT_VERIFICATION_REQUIRED",
    }
    result = {"scope": "The 62 saved full translation orbits with matching number two only",
              "pattern": PATTERN, "normalization": "First image edge index zero by host translation",
              "source": str(SOURCE.relative_to(Path.cwd())),
              "summary": summary, "families": records}
    OUT.write_text(json.dumps(result, indent=2) + "\n")
    print(f"Containment: {len(positive)}/{len(records)} positive; required coverage 62/62")
    print(f"Positive seed masks: {summary['positive_seed_masks']}")
    print(f"Full L025 copy witnesses: {summary['positive_full_L025_isomorphisms']}/{len(positive)}")
    print(f"Accepted prefixes: {summary['accepted_prefixes_by_depth']}; trials {summary['candidate_trials']}")
    print(f"Failures: []; independent verification required; certificate {OUT.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
