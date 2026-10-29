#!/usr/bin/env python3
"""Exact, bounded tests of the saved reflected conic subconstruction.

This does not decide arbitrary reflected coefficients or arbitrary fibers.
All certificates are written beside this script; output stays concise.
"""

import json
import random
from functools import lru_cache
from pathlib import Path


P = 65537
Q = 137
T = [16, 64, 70, 102, 112, 118, 121]
A = 64
SEARCH_NODES = 8192
SEARCH_SEED = 541137


def graph():
    shifts = {r: pow((r - A) % Q, -1, Q) for r in T if r != A}
    loops = sorted({d * pow(2, -1, Q) % Q for d in shifts.values()})
    edges = [(r, w, (d - w) % Q)
             for r, d in shifts.items() for w in range(Q)
             if w < (d - w) % Q]
    adjacency = [set() for _ in range(Q)]
    for _, w, v in edges:
        adjacency[w].add(v)
        adjacency[v].add(w)
    return shifts, loops, edges, adjacency


def propagate(mask, loops, edges, adjacency):
    colors = {w: (mask >> i) & 1 for i, w in enumerate(loops)}
    events = []
    contradiction = None
    while True:
        for r, w, v in edges:
            if w in colors and v in colors and colors[w] != colors[v]:
                contradiction = {"rule": "different_even_neighbors",
                                 "edge": [r, w, v]}
                break
        if contradiction:
            break
        event = None
        for w in range(Q):
            if w in colors:
                continue
            for c in [0, 1]:
                ns = sorted(v for v in adjacency[w] if colors.get(v) == c)
                if len(ns) >= 2:
                    colors[w] = c
                    event = {"rule": "two_equal_neighbors_and_anchor",
                             "vertex": w, "color": c, "neighbors": ns[:2]}
                    events.append(event)
                    break
            if event:
                break
        if not event:
            break
    return {"mask": mask, "initial_colors": [[w, (mask >> i) & 1]
                                                for i, w in enumerate(loops)],
            "events": events, "final_colors": sorted(colors.items()),
            "contradiction": contradiction,
            "status": "inconsistent" if contradiction else
                      "constant" if len(colors) == Q else "unresolved"}


def bounded_search(case, h, edges, adjacency):
    """Search one binary boundary case; a budget stop proves no exclusion."""
    antipodal = sorted({tuple(sorted((x, (-x) % P))) for x in h
                        if x not in [1, P - 1]})
    pair_index = {x: i for i, pair in enumerate(antipodal) for x in pair}
    transforms = [((1 - x) * pow(1 + x, -1, P) % P,
                   1 << pair_index[x])
                  for x in h if x not in [1, P - 1]]

    @lru_cache(maxsize=64)
    def neighbors(t):
        result = {}
        for m, bit in transforms:
            for s in [t * m % P, (1 + (1 - t) * m) % P]:
                result[s] = result.get(s, 0) | bit
        return result

    assigned = dict(case["final_colors"])
    domains = {}
    for w in range(Q):
        if w in assigned:
            continue
        d = None
        for v in adjacency[w]:
            if v in assigned:
                ns = neighbors(assigned[v]).keys()
                d = set(ns) if d is None else d.intersection(ns)
        domains[w] = d
    rng = random.Random(SEARCH_SEED)
    stats = {"candidate_trials": 0, "recursive_calls": 0,
             "used_pair_rejections": 0, "empty_domain_rejections": 0,
             "budget_reached": False, "best_assigned_vertices": len(assigned)}
    best = {"parameters": sorted(assigned.items()), "edge_pairs": []}
    trace = []
    chosen = {}
    solution = None

    def choices(reqs, at, used, picked):
        if at == len(reqs):
            yield used, picked
            return
        edge, options = reqs[at]
        available = options & ~used
        while available:
            bit = available & -available
            available -= bit
            yield from choices(reqs, at + 1, used | bit,
                               picked + [(edge, bit.bit_length() - 1)])

    def visit(current_domains, used):
        nonlocal best, solution
        stats["recursive_calls"] += 1
        if len(assigned) > stats["best_assigned_vertices"]:
            stats["best_assigned_vertices"] = len(assigned)
            best = {"parameters": sorted(assigned.items()),
                    "edge_pairs": [[w, v, i] for (w, v), i in sorted(chosen.items())]}
        if not current_domains:
            solution = best
            return True
        w = min(current_domains, key=lambda u: (
            P if current_domains[u] is None else len(current_domains[u]),
            -len(adjacency[u] & assigned.keys()), u))
        values = sorted(current_domains[w]) if current_domains[w] is not None else list(range(P))
        rng.shuffle(values)
        for t in values:
            if stats["candidate_trials"] >= SEARCH_NODES:
                stats["budget_reached"] = True
                return False
            stats["candidate_trials"] += 1
            reqs = []
            impossible = False
            for v in sorted(adjacency[w] & assigned.keys()):
                s = assigned[v]
                if t == s and t in [0, 1]:
                    continue  # identically zero; allocate these labels last
                options = neighbors(s).get(t, 0) & ~used
                if not options:
                    impossible = True
                    break
                reqs.append((tuple(sorted((w, v))), options))
            if impossible:
                stats["used_pair_rejections"] += 1
                trace.append([stats["candidate_trials"], len(assigned), w, t, "pair"])
                continue
            next_domains = current_domains.copy()
            del next_domains[w]
            ns = neighbors(t).keys()
            for v in adjacency[w] & next_domains.keys():
                old = next_domains[v]
                new = set(ns) if old is None else old.intersection(ns)
                next_domains[v] = new
                if not new:
                    impossible = True
                    break
            if impossible:
                stats["empty_domain_rejections"] += 1
                trace.append([stats["candidate_trials"], len(assigned), w, t, "domain"])
                continue
            trace.append([stats["candidate_trials"], len(assigned), w, t, "descend"])
            assigned[w] = t
            reqs.sort(key=lambda z: z[1].bit_count())
            for new_used, picked in choices(reqs, 0, used, []):
                chosen.update(picked)
                if visit(next_domains, new_used):
                    return True
                for edge, _ in picked:
                    del chosen[edge]
                if stats["budget_reached"]:
                    break
            del assigned[w]
            if stats["budget_reached"]:
                return False
        return False

    found = visit(domains, 0)
    params = dict(best["parameters"])
    selected = {(w, v): i for w, v, i in best["edge_pairs"]}
    edge_checks = []
    failures = []
    for r, w, v in edges:
        if w not in params or v not in params:
            continue
        t, s = params[w], params[v]
        if t == s and t in [0, 1]:
            edge_checks.append({"edge": [r, w, v], "type": "identically_zero"})
            continue
        if (w, v) not in selected:
            failures.append(f"missing chosen pair on {w},{v}")
            continue
        pair = antipodal[selected[w, v]]
        # Verify the original polynomial equality, not just the factorization.
        roots = [x for x in pair if
                 ((1 + t * (x - 1)) ** 2
                  - (1 + s * (-x - 1)) ** 2) % P == 0]
        if not roots:
            failures.append(f"original equality fails on {w},{v}")
        edge_checks.append({"edge": [r, w, v], "type": "nonzero",
                            "pair_index": selected[w, v], "roots": roots})
    if len(set(selected.values())) != len(selected):
        failures.append("repeated antipodal pair")
    # Complete labels only on the induced partial graph, then replay every
    # available original matching in both orientations. This is not a full
    # assignment on the 137 vertices or a sigma/core extension certificate.
    used_indices = set(selected.values())
    free_indices = iter(i for i in range(len(antipodal)) if i not in used_indices)
    partial_labels = {}
    for record in edge_checks:
        r, w, v = record["edge"]
        if record["type"] == "identically_zero":
            i = next(free_indices)
            x = antipodal[i][0]
            record["pair_index"] = i
            record["roots"] = list(antipodal[i])
        else:
            x = record["roots"][0]
        partial_labels[r, (r - A) * w % Q] = x
        partial_labels[r, (r - A) * v % Q] = (-x) % P
    used_labels = set(partial_labels.values()) | {1, P - 1}
    free_labels = iter(x for x in h if x not in used_labels)
    for r in T:
        if r != A:
            d = pow((r - A) % Q, -1, Q)
            w = d * pow(2, -1, Q) % Q
            if w not in params or params[w] not in [0, 1]:
                failures.append(f"missing or invalid loop parameter in direction {r}")
            partial_labels[r, (r - A) * w % Q] = next(free_labels)
    matching_checks = []
    for r in T:
        if r == A:
            continue
        d = pow((r - A) % Q, -1, Q)
        for w, t in sorted(params.items()):
            v = (d - w) % Q
            if v not in params:
                continue
            y = (r - A) * w % Q
            x = partial_labels[r, y]
            residual = ((1 + t * (x - 1)) ** 2
                        - (1 + params[v] * (-x - 1)) ** 2) % P
            matching_checks.append([r, w, v, x, residual])
            if residual:
                failures.append(f"original oriented matching fails at {r},{w}")
    rank_vertices = [next(w for w, t in sorted(params.items()) if t == c)
                     for c in [0, 1]]
    rank_vertices.append(next(w for w, t in sorted(params.items()) if t not in [0, 1]))
    uv = [(2 * params[w] * (1 - params[w]) % P, params[w] ** 2 % P)
          for w in rank_vertices]
    determinant = ((uv[1][0] - uv[0][0]) * (uv[2][1] - uv[0][1])
                   - (uv[2][0] - uv[0][0]) * (uv[1][1] - uv[0][1])) % P
    partial_checks = {
        "labels_are_distinct": len(set(partial_labels.values())) == len(partial_labels),
        "labels_are_nonanchor_subgroup_elements":
            all(x in h and x not in [1, P - 1] for x in partial_labels.values()),
        "all_induced_oriented_matchings_checked":
            len(matching_checks) == 2 * len(edge_checks) + 6,
        "all_induced_oriented_matchings_hold": all(c[-1] == 0 for c in matching_checks),
        "both_anchor_constancies": all(
            ((1 + t * (1 - 1)) ** 2 - 1) % P == 0 and
            ((1 + t * (-(-1) - 1)) ** 2 - 1) % P == 0
            for t in params.values()),
        "partial_affine_rank_two": determinant != 0,
    }
    failures.extend(name for name, good in partial_checks.items() if not good)
    return {"mask": case["mask"], "seed": SEARCH_SEED,
            "node_limit": SEARCH_NODES, "stats": stats,
            "search_exhaustive_for_boundary_case": not stats["budget_reached"],
            "solution_found": found, "solution": solution,
            "best_partial_assignment": best, "best_partial_edge_checks": edge_checks,
            "partial_labels": [[r, y, x] for (r, y), x in sorted(partial_labels.items())],
            "partial_oriented_matching_checks": matching_checks,
            "partial_rank_minor": {"vertices": rank_vertices, "uv": uv,
                                   "determinant": determinant},
            "partial_checks": partial_checks,
            "partial_summary": {"assigned_vertices": len(params),
                                "required_vertices": Q,
                                "induced_nonloop_edges": len(edge_checks),
                                "required_nonloop_edges": 408,
                                "distinct_transverse_labels": len(partial_labels),
                                "verified_original_matchings": len(matching_checks),
                                "required_original_matchings": 822,
                                "nonzero_edge_pairs": len(selected),
                                "free_label_zero_edges": sum(c["type"] == "identically_zero"
                                                             for c in edge_checks)},
            "antipodal_pairs": antipodal, "trace": trace,
            "verification_failures": failures,
            "required_assigned_vertices": Q,
            "required_distinct_nonloop_pairs_in_complete_assignment": 408}


def main():
    h = sorted({pow(19139, i, P) for i in range(1024)})
    nonanchor = [x for x in h if x not in [1, P - 1]]
    domains = {
        0: sorted({0} | {2 * pow(1 + x, -1, P) % P for x in nonanchor}),
        1: sorted({1} | {(1 - x) * pow(1 + x, -1, P) % P
                        for x in nonanchor}),
    }
    shifts, loops, edges, adjacency = graph()
    cases = [propagate(mask, loops, edges, adjacency) for mask in range(64)]
    checks = {
        "generator_order_1024": pow(19139, 1024, P) == 1
        and pow(19139, 512, P) != 1 and len(h) == 1024,
        "six_distinct_loops": len(loops) == 6,
        "408_distinct_nonloop_edges": len(edges) == 408
        and len({(w, v) for _, w, v in edges}) == 408,
        "64_binary_assignments": len(cases) == 64,
        "each_even_neighbor_domain_has_1023_values":
            all(len(d) == 1023 for d in domains.values()),
    }
    failures = [name for name, good in checks.items() if not good]
    counts = {s: sum(c["status"] == s for c in cases)
              for s in ["inconsistent", "constant", "unresolved"]}
    eligible = [c for c in cases if c["status"] == "unresolved"
                and c["mask"].bit_count() == 3]
    selected_case = min(eligible, key=lambda c: (-len(c["final_colors"]), c["mask"]))
    search = bounded_search(selected_case, h, edges, adjacency)
    failures.extend(search["verification_failures"])
    report = {
        "scope": "Conic reflection ansatz only; a=64,h=1,K=E; anchors 1,-1",
        "q": Q, "p": P, "a": A, "T": T, "shifts": shifts,
        "loops": loops, "edges": edges,
        "loop_neighbor_counts": [len(set(loops) & ns) for ns in adjacency],
        "subgroup": h, "even_neighbor_domains": domains,
        "mixed_even_neighbor_domain": sorted(set(domains[0]) & set(domains[1])),
        "cases": cases, "case_counts": counts, "checks": checks,
        "search": search, "failures": failures,
        "witness_found": False,
        "uniform_two_fiber_impossibility_proved": False,
    }
    path = Path(__file__).with_name("two-fiber-conic-compatibility.json")
    path.write_text(json.dumps(report, indent=2) + "\n")
    print(f"Binary loop assignments: {counts}; required for exclusion: 0 unresolved.")
    print(f"Mixed even-neighbor domain: {len(report['mixed_even_neighbor_domain'])} values.")
    print(f"Bounded search mask {selected_case['mask']}: "
          f"{search['stats']['candidate_trials']}/{SEARCH_NODES} trials; "
          f"best {search['stats']['best_assigned_vertices']}/{Q} vertices; "
          f"budget reached {search['stats']['budget_reached']}.")
    print(f"Partial original matching replay: "
          f"{search['partial_summary']['verified_original_matchings']}/822; "
          f"affine minor {search['partial_rank_minor']['determinant']} (required nonzero).")
    print(f"Failures: {len(failures)}. Full witness: no. General obstruction: no.")
    print(f"Certificate: {path}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
