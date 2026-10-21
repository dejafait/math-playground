"""Finite actual-graph diagnostics for L036, not an asymptotic proof."""
import importlib.util
import json
from pathlib import Path
import random

spec = importlib.util.spec_from_file_location(
    "marked", Path(__file__).parents[1] / "alternative-abp-commutator/check_marked_edges.py")
marked = importlib.util.module_from_spec(spec)
spec.loader.exec_module(marked)
graph, plus, times, serial = marked.graph, marked.plus, marked.times, marked.serial


def normalize(g):
    edges = []
    for u, v, lab in g["edges"]:
        if u == g["sink"]:
            continue
        odd = set()
        for a in lab:
            odd.symmetric_difference_update({a})
        edges.extend((u, v, [a]) for a in sorted(odd))
    return graph(g["vertices"], edges, g["source"], g["sink"])


def rooted(g, s):
    return graph(g["vertices"], g["edges"], s, g["sink"])


def atom(a):
    return graph(2, [(0, 1, [a])])


def copy_into(out, g):
    k = out["vertices"]
    out["vertices"] += g["vertices"]
    out["edges"].extend([u + k, v + k, list(lab)] for u, v, lab in g["edges"])
    return g["source"] + k, g["sink"] + k


def product(factors):
    out = graph(2, [], sink=1)
    last = 0
    for g in factors:
        s, t = copy_into(out, g)
        out["edges"].append([last, s, ["1"]])
        last = t
    out["edges"].append([last, 1, ["1"]])
    return out


def prefixed(g, a, v):
    # One extra source realizes a * f_v with no formula unfolding.
    return graph(g["vertices"] + 1,
                 g["edges"] + [[g["vertices"], v, [a]]],
                 g["vertices"], g["sink"])


def construct(g, mutation=None):
    h = normalize(g)
    out = graph(h["vertices"] + 1, h["edges"], h["source"], h["vertices"])
    ledger = []

    def attach(u, kind, block):
        s, t = copy_into(out, block)
        out["edges"].extend([[u, s, ["1"]], [t, out["sink"], ["1"]]])
        ledger.append({"vertex": u, "kind": kind,
                       "vertices": block["vertices"], "edges": len(block["edges"])})

    for u in range(h["vertices"]):
        outgoing = [(v, lab[0]) for z, v, lab in h["edges"] if z == u]
        for v, a in outgoing:
            suffix = rooted(h, v)
            if a != "1":
                attach(u, "edge_boolean", product([atom("b:" + a[1:]), suffix, suffix]))
            if mutation != "omit_product_commutator":
                w, _ = marked.witness(atom(a), suffix)
                attach(u, "product_commutator", product([atom(a), w, suffix]))
        if mutation != "omit_sum_commutator":
            for i, (v, a) in enumerate(outgoing):
                for z, b in outgoing[i + 1:]:
                    w, _ = marked.witness(prefixed(h, a, v), prefixed(h, b, z))
                    attach(u, "sum_commutator", w)
    return out, h, ledger


def label_value(lab, mode):
    pieces = []
    for a in lab:
        if a == "1":
            pieces.append({()})
        elif a.startswith("b:"):
            x = "x" + a[2:]
            pieces.append(set() if mode == "zero" else
                          {(x, x), (x,)} if mode == "axioms" else {(a,)})
        else:
            pieces.append(marked.label_poly([a], mode))
    return plus(*pieces)


def evaluate(g, mode):
    nv = g["vertices"]
    adj = [[] for _ in range(nv)]
    indegree = [0] * nv
    for u, v, lab in g["edges"]:
        adj[u].append((v, lab))
        indegree[v] += 1
    ready = [u for u in range(nv) if not indegree[u]]
    values = [set() for _ in range(nv)]
    marks = [set() for _ in range(nv)]
    values[g["source"]] = {()}
    marks[g["source"]] = {0}
    visited = 0
    while ready:
        u = ready.pop()
        visited += 1
        for v, lab in adj[u]:
            values[v] = plus(values[v], times(values[u], label_value(lab, mode)))
            for a in lab:
                count = int(a.startswith(("b:", "t:")))
                marks[v].update(c + count for c in marks[u])
            indegree[v] -= 1
            if not indegree[v]:
                ready.append(v)
    assert visited == nv, "cycle in actual graph"
    return values[g["sink"]], sorted(marks[g["sink"]])


def main():
    jobs = [
        ("empty_alphabet_unit", 0, graph(1, [])),
        ("empty_alphabet_zero", 0, graph(2, [])),
        ("constant_paths", 0, graph(3, [(0, 1, ["1"]), (1, 2, ["1"]), (0, 2, ["1"])])),
        ("zero_label", 1, graph(2, [(0, 1, [])])),
        ("one_variable_square", 1, graph(3, [(0, 1, ["x1"]), (1, 2, ["x1"])])),
        ("word12", 2, graph(3, [(0, 1, ["x1"]), (1, 2, ["x2"])])),
        ("affine_sum", 2, graph(2, [(0, 1, ["1", "x1", "x2"])])),
        ("unequal_lengths", 3, graph(3, [(0, 2, ["1", "x1"]), (0, 1, ["x2"]), (1, 2, ["1", "x3"])])),
        ("shared_diamond", 3, graph(5, [(0, 1, ["x1"]), (0, 2, ["x2"]), (1, 3, ["x3"]), (2, 3, ["1", "x1"]), (3, 4, ["x2"])])),
        ("parallel_cancel", 2, graph(3, [(0, 1, ["x1"]), (0, 1, ["x1"]), (1, 2, ["x2"])])),
        ("duplicate_label", 2, graph(2, [(0, 1, ["x1", "x1", "1", "1", "x2"])])),
        ("interior_coincident", 2, graph(3, [(0, 1, ["x1"]), (1, 2, ["x2"])], 1, 1)),
        ("incoming_outgoing_roots", 3, graph(5, [(0, 1, ["x1"]), (1, 2, ["x2"]), (2, 3, ["x3"]), (3, 4, ["x1"])], 1, 3)),
        ("nonnumeric_order", 3, graph(4, [(3, 1, ["x1"]), (1, 0, ["x2"]), (0, 2, ["x3"])], 3, 2)),
        ("unreachable_sink", 2, graph(4, [(0, 1, ["x1"]), (2, 3, ["x2"])], 1, 2)),
    ]
    rng = random.Random(3607)
    for j in range(20):
        nv = rng.randrange(2, 5)
        edges = [(u, v, [rng.choice(["1", "x1", "x2"]) for _ in range(rng.randrange(3))])
                 for u in range(nv) for v in range(u + 1, nv) if rng.randrange(2)]
        jobs.append(("seeded_" + str(j), 2, graph(nv, edges)))
    cases, failures = [], []
    detected = {"omit_product_commutator": 0, "omit_sum_commutator": 0}
    for name, n, g in jobs:
        w, h, ledger = construct(g)
        f, _ = evaluate(g, "free")
        normalized, _ = evaluate(h, "free")
        free, path_marks = evaluate(w, "free")
        zero, _ = evaluate(w, "zero")
        sub, _ = evaluate(w, "axioms")
        target = plus(times(f, f), f)
        q = h["vertices"] + len(h["edges"]) + n + 2
        required_v = h["vertices"] + 1 + sum(b["vertices"] for b in ledger)
        required_m = len(h["edges"]) + sum(b["edges"] + 2 for b in ledger)
        full = {"alphabet": [f"x{i}" for i in range(1, n + 1)],
                "axioms": {**{f"b:{i}": [[f"x{i}", f"x{i}"], [f"x{i}"]] for i in range(1, n + 1)},
                           **{f"t:{i}:{j}": [[f"x{i}", f"x{j}"], [f"x{j}", f"x{i}"]]
                              for i in range(1, n + 1) for j in range(i + 1, n + 1)}},
                "graph": w}
        binary_bits = 8 * len(json.dumps(full, separators=(",", ":")).encode())
        checks = {"normalization": normalized == f, "zero": not zero,
                  "substitution": sub == target, "single_placeholder_paths": set(path_marks) <= {1},
                  "exact_vertices": w["vertices"] == required_v,
                  "exact_edges": len(w["edges"]) == required_m,
                  "record_bound": required_v + required_m <= 50 * q**5,
                  "branch_bound": len(ledger) <= (len(h["edges"]) + 1)**2}
        mutations = {}
        for kind in detected:
            bad, _, _ = construct(g, kind)
            actual, _ = evaluate(bad, "axioms")
            hit = actual != target
            detected[kind] += hit
            mutations[kind] = {"detected": hit, "substituted": serial(actual)}
        if not all(checks.values()):
            failures.append({"name": name, "checks": checks})
        cases.append({"name": name, "input": g, "normalized": h, "full_output": full,
                      "blocks": ledger, "polynomials": {"f": serial(f), "free": serial(free),
                      "zero": serial(zero), "substituted": serial(sub), "target": serial(target)},
                      "path_placeholder_counts": path_marks, "checks": checks,
                      "bounds": {"Q": q, "vertices_actual": w["vertices"], "vertices_required": required_v,
                                 "edges_actual": len(w["edges"]), "edges_required": required_m,
                                 "records_actual": required_v + required_m, "records_upper": 50 * q**5,
                                 "full_json_bits": binary_bits}, "mutations": mutations})
    for kind, count in detected.items():
        if not count:
            failures.append({"undetected_mutation": kind})
    summary = {"cases": len(cases), "failures": failures, "mutations_detected": detected,
               "max_vertices": max(c["bounds"]["vertices_actual"] for c in cases),
               "max_edges": max(c["bounds"]["edges_actual"] for c in cases),
               "max_full_json_bits": max(c["bounds"]["full_json_bits"] for c in cases),
               "all_exact_counts_and_polynomial_bounds_pass": all(c["checks"]["exact_vertices"] and
                   c["checks"]["exact_edges"] and c["checks"]["record_bound"] for c in cases)}
    path = Path(__file__).with_name("suffix-graph-results.json")
    path.write_text(json.dumps({"scope": "Finite diagnostics; canonical L036 proves all-input claims.",
                                "summary": summary, "cases": cases}, indent=2) + "\n")
    print(json.dumps(summary))
    print("Required: both formal identities, one placeholder per accepting path, exact copy counts,")
    print("and vertices+edges <= 50 Q^5; complete actual/required bounds and graphs:", path)
    assert not failures, failures


if __name__ == "__main__":
    main()
