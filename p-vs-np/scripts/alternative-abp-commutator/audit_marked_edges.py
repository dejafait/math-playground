"""Independent suffix evaluation and structural path audit of L035 diagnostics.

The original certificate is read completely and never rewritten. Finite tests
are not a proof of the all-input identities or asymptotic encoding bound.
"""
from collections import Counter
import hashlib
import json
from pathlib import Path
import runpy


def parity(counter):
    return {word: 1 for word, count in counter.items() if count % 2}


def add(*polys):
    total = Counter()
    for poly in polys:
        total.update(poly)
    return parity(total)


def multiply(left, right):
    total = Counter()
    for u in left:
        for v in right:
            total[u + v] += 1
    return parity(total)


def label_terms(label, mode):
    terms = Counter()
    for symbol in label:
        if symbol == "1":
            terms[()] += 1
        elif symbol.startswith("t:"):
            _, i, j = symbol.split(":")
            if mode == "axioms":
                terms[("x" + i, "x" + j)] += 1
                terms[("x" + j, "x" + i)] += 1
            elif mode == "free":
                terms[(symbol,)] += 1
        else:
            terms[(symbol,)] += 1
    return parity(terms)


def suffix_evaluate(graph, mode):
    nv = graph["vertices"]
    outgoing = [[] for _ in range(nv)]
    indegrees = [0] * nv
    for u, v, label in graph["edges"]:
        assert 0 <= u < nv and 0 <= v < nv
        outgoing[u].append((v, label))
        indegrees[v] += 1
    ready = [u for u in range(nv) if indegrees[u] == 0]
    order = []
    while ready:
        u = ready.pop()
        order.append(u)
        for v, _ in outgoing[u]:
            indegrees[v] -= 1
            if not indegrees[v]:
                ready.append(v)
    assert len(order) == nv, "cycle"
    values = [{} for _ in range(nv)]
    # These sets count placeholders on graph paths, even on zero-label paths
    # and paths whose polynomial contributions subsequently cancel.
    path_markers = [set() for _ in range(nv)]
    for u in reversed(order):
        parts = [{(): 1}] if u == graph["sink"] else []
        if u == graph["sink"]:
            path_markers[u].add(0)
        for v, label in outgoing[u]:
            parts.append(multiply(label_terms(label, mode), values[v]))
            has_placeholder = any(s.startswith("t:") for s in label)
            if has_placeholder:
                assert len(label) == 1, "central edge must have one symbol"
            path_markers[u].update(c + int(has_placeholder)
                                   for c in path_markers[v])
        values[u] = add(*parts)
    return values[graph["source"]], sorted(path_markers[graph["source"]])


def serial(poly):
    return [list(w) for w in sorted(poly, key=lambda w: (len(w), w))]


def normalize_labels(graph):
    normalized = dict(graph)
    normalized["edges"] = [[u, v, sorted(s for s, count in Counter(label).items() if count % 2)]
                           for u, v, label in graph["edges"]]
    assert suffix_evaluate(normalized, "free")[0] == suffix_evaluate(graph, "free")[0]
    return normalized


def inspect_case(name, n, f, g, w):
    fp, _ = suffix_evaluate(f, "free")
    gp, _ = suffix_evaluate(g, "free")
    free, markers = suffix_evaluate(w, "free")
    zero, _ = suffix_evaluate(w, "zero")
    sub, _ = suffix_evaluate(w, "axioms")
    target = add(multiply(fp, gp), multiply(gp, fp))
    p = len(f["edges"]) * len(g["edges"])
    af = sum(s != "1" for _, _, label in f["edges"] for s in label)
    ag = sum(s != "1" for _, _, label in g["edges"] for s in label)
    q = sum(x != "1" and y != "1" and x != y
            for _, _, elabel in f["edges"] for _, _, dlabel in g["edges"]
            for x in elabel for y in dlabel)
    required_nv = 2 + 2 * p * (f["vertices"] + g["vertices"])
    required_ne = 2 * p * (len(f["edges"]) + len(g["edges"])) + 4 * p + q
    bounds = {"vertices_actual": w["vertices"], "vertices_required": required_nv,
              "edges_actual": len(w["edges"]), "edges_required": required_ne,
              "central_actual": q, "central_upper_bound": af * ag}
    checks = {"zero_identity": not zero, "substitution_identity": sub == target,
              "all_graph_paths_have_one_placeholder": set(markers) <= {1},
              "vertex_count": w["vertices"] == required_nv,
              "edge_count": len(w["edges"]) == required_ne,
              "central_bound": q <= af * ag}
    assert all(checks.values()), (name, checks)
    return {"name": name, "alphabet_size": n, "checks": checks, "bounds": bounds,
            "graph_path_placeholder_counts": markers,
            "polynomials": {"f": serial(fp), "g": serial(gp),
                            "W_free": serial(free), "W_zero": serial(zero),
                            "W_substituted": serial(sub), "target": serial(target)}}


def main():
    here = Path(__file__).parent
    original = here / "marked-edge-results.json"
    old_bytes = original.read_bytes()
    old = json.loads(old_bytes)
    implementation = runpy.run_path(str(here / "check_marked_edges.py"))
    make_witness = implementation["witness"]
    graph = implementation["graph"]
    records = []
    for case in old["cases"]:
        f, g, w = case["input_F"], case["input_G"], case["witness_graph"]
        rebuilt, _ = make_witness(f, g)
        assert rebuilt == w, case["name"]
        result = inspect_case(case["name"], len(case["alphabet"]), f, g, w)
        assert result["polynomials"] == case["polynomials"], case["name"]
        assert result["bounds"] == case["bounds"], case["name"]
        assert all(case["checks"].values()), case["name"]
        expected_axioms = {f"t:{i}:{j}": [[f"x{i}", f"x{j}"], [f"x{j}", f"x{i}"]]
                           for i in range(1, len(case["alphabet"]) + 1)
                           for j in range(i + 1, len(case["alphabet"]) + 1)}
        assert case["axioms"] == expected_axioms
        wrong, _ = make_witness(f, g, wrong_suffix_order=True)
        mutated, _ = suffix_evaluate(wrong, "axioms")
        assert serial(mutated) == case["mutation"]["substituted"]
        detected = serial(mutated) != result["polynomials"]["target"]
        assert detected == case["mutation"]["detected"]
        result["mutation_detected"] = detected
        records.append(result)
    # Extra cases exercise normalization and designated endpoints that are
    # neither graph roots nor extremal vertices in numeric/topological order.
    extras = {
        "non_numeric_order": graph(5, [(4, 1, ["x1"]), (1, 3, ["x2"]),
                                      (3, 0, ["x3"]), (0, 2, ["x4"])], 1, 0),
        "duplicate_label_entries": graph(2, [(0, 1, ["x1", "x1", "x2", "1", "1"])]),
        "sink_outgoing_source_incoming": graph(4, [(0, 1, ["x3"]),
                                                   (1, 2, ["x1", "x2"]),
                                                   (2, 3, ["x4"])], 1, 2),
        "unreachable_root": graph(4, [(0, 1, ["x1"]), (2, 3, ["x2"])], 1, 2),
    }
    extra_records = []
    for a, raw_f in extras.items():
        for b, raw_g in extras.items():
            f, g = normalize_labels(raw_f), normalize_labels(raw_g)
            w, _ = make_witness(f, g)
            result = inspect_case(a + "__" + b, 4, f, g, w)
            result.update({"raw_input_F": raw_f, "raw_input_G": raw_g,
                           "normalized_input_F": f, "normalized_input_G": g,
                           "witness_graph": w})
            extra_records.append(result)
    assert original.read_bytes() == old_bytes
    summary = {"saved_cases_replayed_completely": len(records),
               "extra_cases": len(extra_records), "failures": [],
               "wrong_suffix_mutations_detected": sum(r["mutation_detected"] for r in records),
               "max_vertices_actual": max(r["bounds"]["vertices_actual"] for r in records + extra_records),
               "max_edges_actual": max(r["bounds"]["edges_actual"] for r in records + extra_records),
               "required": "Both identities; exact N,M; q<=a_F*a_G; all graph paths have exactly one placeholder.",
               "original_sha256": hashlib.sha256(old_bytes).hexdigest()}
    certificate = here / "marked-edge-audit-results.json"
    certificate.write_text(json.dumps({"scope": "Finite audit; all-input proof and bit ledger are in L035.",
                                       "summary": summary, "saved_case_audits": records,
                                       "extra_case_audits": extra_records}, indent=2) + "\n")
    print(json.dumps(summary))
    print("Certificate:", certificate)


if __name__ == "__main__":
    main()
