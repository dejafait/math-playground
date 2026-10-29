#!/usr/bin/env python3
"""Exact necessary-condition test for the two-fiber reflection ansatz.

This does not construct quadratics or certify compatibility. It records
the complete auxiliary graphs and the equality propagation forced from
their six loop vertices. Run from the active notebook directory.
"""

import json
from pathlib import Path


Q = 137
P = 65537
T = [16, 64, 70, 102, 112, 118, 121]


def analyze(a):
    shifts = {r: pow((r - a) % Q, -1, Q) for r in T if r != a}
    loops = {r: d * pow(2, -1, Q) % Q for r, d in shifts.items()}
    adjacency = [[] for _ in range(Q)]
    edges = []
    for r, d in shifts.items():
        for w in range(Q):
            v = (d - w) % Q
            if w < v:
                edges.append([r, w, v])
                adjacency[w].append(v)
                adjacency[v].append(w)

    marked = set(loops.values())
    parent = list(range(Q))
    events = []

    def root(w):
        while parent[w] != w:
            w = parent[w]
        return w

    def merge(w, v):
        rw, rv = root(w), root(v)
        if rw == rv:
            return False
        parent[max(rw, rv)] = min(rw, rv)
        return True

    while True:
        changed = False
        for r, w, v in edges:
            if w in marked and v in marked and merge(w, v):
                events.append({"rule": "even_neighbors", "direction": r,
                               "vertices": [w, v]})
                changed = True
        for w in range(Q):
            if w in marked:
                continue
            groups = {}
            for v in adjacency[w]:
                if v in marked:
                    groups.setdefault(root(v), []).append(v)
            witnesses = [sorted(vs) for vs in groups.values() if len(vs) >= 2]
            if witnesses:
                vs = sorted(witnesses)[0]
                marked.add(w)
                merge(w, vs[0])
                events.append({"rule": "two_equal_neighbors_and_anchor", "vertex": w,
                               "neighbors": vs})
                changed = True
        if not changed:
            break

    classes = {}
    for w in sorted(marked):
        classes.setdefault(root(w), []).append(w)
    final_classes = sorted(classes.values())
    max_same_class_neighbors = max(
        (len(set(adjacency[w]) & set(c))
         for w in range(Q) if w not in marked for c in final_classes),
        default=0,
    )
    checks = {
        "six_distinct_shifts": len(set(shifts.values())) == 6,
        "six_distinct_loops": len(set(loops.values())) == 6,
        "408_nonloop_edges": len(edges) == 408,
        "simple_nonloop_graph": len({(w, v) for _, w, v in edges}) == 408,
        "matching_involutions": all(
            (d - ((d - w) % Q)) % Q == w
            for d in shifts.values() for w in range(Q)
        ),
        "no_missing_even_merge": all(
            w not in marked or v not in marked or root(w) == root(v)
            for _, w, v in edges
        ),
        "closure_exhausted": max_same_class_neighbors < 2,
    }
    return {
        "a": a, "shifts": shifts, "loop_vertices": loops,
        "nonloop_edges": edges, "adjacency": adjacency,
        "propagation_events": events, "final_even_classes": final_classes,
        "forced_even_vertices": len(marked),
        "largest_equal_class": max(map(len, final_classes)),
        "max_unmarked_same_class_neighbors": max_same_class_neighbors,
        "checks": checks,
        "decision": "collapse" if len(final_classes) == 1 and len(marked) == Q
                    else "unresolved",
    }


def main():
    subgroup = sorted({pow(19139, i, P) for i in range(1024)})
    antipodal = sorted({tuple(sorted((x, (-x) % P))) for x in subgroup})
    checks = {
        "generator_exact_order_1024": pow(19139, 1024, P) == 1
        and pow(19139, 512, P) != 1,
        "subgroup_size_1024": len(subgroup) == 1024,
        "anchors_present": 1 in subgroup and P - 1 in subgroup,
        "512_antipodal_pairs": len(antipodal) == 512,
    }
    cases = [analyze(a) for a in T]
    failures = [name for name, good in checks.items() if not good]
    failures += [f'a={case["a"]}:{name}' for case in cases
                 for name, good in case["checks"].items() if not good]
    report = {
        "purpose": "Necessary-condition propagation for a proposed reflection witness",
        "scope": "h=1; anchors 1,-1; K=E; all seven choices of a; no witness assigned",
        "q": Q, "p": P, "T": T, "subgroup": subgroup,
        "antipodal_pairs": antipodal, "checks": checks, "cases": cases,
        "label_capacity": {"nonanchor_pairs": 511, "required_edge_pairs": 408,
                           "remaining_individual_labels": 206,
                           "required_loop_labels": 6,
                           "remaining_after_transverse_and_anchors": 200,
                           "required_remaining_sigma_labels_and_core": 200},
        "failures": failures,
        "witness_found": False,
        "uniform_impossibility_proved": False,
        "unresolved": "408 compatible distinct antipodal edge pairs and coefficients of affine dimension two",
    }
    path = Path(__file__).with_name("two-fiber-reflection-closure.json")
    path.write_text(json.dumps(report, indent=2) + "\n")
    for case in cases:
        print(f'a={case["a"]}: forced even {case["forced_even_vertices"]}/137; '
              f'largest equal class {case["largest_equal_class"]}/137; '
              f'max same-class neighbors {case["max_unmarked_same_class_neighbors"]} '
              f'(propagation requires 2); {case["decision"]}')
    print("Label capacity: 408 edge pairs required, 511 available; "
          "6 loop labels required, 206 left after edge pairs.")
    print(f"Failures: {len(failures)}. Witness: no. Universal obstruction: no.")
    print(f"Certificate: {path}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
