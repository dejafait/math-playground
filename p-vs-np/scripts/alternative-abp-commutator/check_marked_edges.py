"""Finite free-word diagnostics for L035; no asymptotic claim is inferred."""
import json
from pathlib import Path


def plus(*polys):
    out = set()
    for poly in polys:
        out.symmetric_difference_update(poly)
    return out


def times(a, b):
    out = set()
    for u in a:
        for v in b:
            w = u + v
            if w in out:
                out.remove(w)
            else:
                out.add(w)
    return out


def graph(nv, edges, source=0, sink=None):
    return {"vertices": nv, "source": source,
            "sink": nv - 1 if sink is None else sink,
            "edges": [[u, v, lab] for u, v, lab in edges]}


def label_poly(label, mode):
    parts = []
    for symbol in label:
        if symbol == "1":
            parts.append({()})
        elif symbol.startswith("t:"):
            if mode == "zero":
                parts.append(set())
            elif mode == "axioms":
                _, i, j = symbol.split(":")
                parts.append({("x" + i, "x" + j),
                              ("x" + j, "x" + i)})
            else:
                parts.append({(symbol,)})
        else:
            parts.append({(symbol,)})
    return plus(*parts)


def evaluate(g, mode="free"):
    # Kahn order checks the actual generated graph, not its vertex numbering.
    nv = g["vertices"]
    outgoing = [[] for _ in range(nv)]
    indegree = [0] * nv
    for u, v, label in g["edges"]:
        outgoing[u].append((v, label))
        indegree[v] += 1
    ready = [v for v in range(nv) if indegree[v] == 0]
    values = [set() for _ in range(nv)]
    values[g["source"]] = {()}
    visited = 0
    while ready:
        u = ready.pop()
        visited += 1
        for v, label in outgoing[u]:
            values[v] = plus(values[v], times(values[u], label_poly(label, mode)))
            indegree[v] -= 1
            if indegree[v] == 0:
                ready.append(v)
    assert visited == nv, "generated graph is cyclic"
    return values[g["sink"]]


def witness(f, g, wrong_suffix_order=False):
    out = graph(2, [], sink=1)
    central = 0

    def copy(h, entry, exit_):
        offset = out["vertices"]
        out["vertices"] += h["vertices"]
        out["edges"].extend([u + offset, v + offset, list(label)]
                            for u, v, label in h["edges"])
        return entry + offset, exit_ + offset

    for u, v, elabel in f["edges"]:
        for a, b, dlabel in g["edges"]:
            fp = copy(f, f["source"], u)
            gp = copy(g, g["source"], a)
            gs = copy(g, b, g["sink"])
            fs = copy(f, v, f["sink"])
            third, fourth = (fs, gs) if wrong_suffix_order else (gs, fs)
            out["edges"].extend([[0, fp[0], ["1"]],
                                 [fp[1], gp[0], ["1"]],
                                 [third[1], fourth[0], ["1"]],
                                 [fourth[1], 1, ["1"]]])
            for x in elabel:
                for y in dlabel:
                    if x != "1" and y != "1" and x != y:
                        i, j = sorted((int(x[1:]), int(y[1:])))
                        out["edges"].append([gp[1], third[0], [f"t:{i}:{j}"]])
                        central += 1
    return out, central


def serial(poly):
    return [list(word) for word in sorted(poly, key=lambda w: (len(w), w))]


def main():
    examples = {
        "empty_unit": graph(1, []),
        "zero": graph(2, []),
        "zero_label": graph(2, [(0, 1, [])]),
        "affine_unequal_lengths": graph(3, [
            (0, 2, ["1", "x1", "x2"]), (0, 1, ["x3"]),
            (1, 2, ["1", "x4"])]),
        "shared_diamond": graph(5, [
            (0, 1, ["x1"]), (0, 2, ["x2"]), (1, 3, ["x3"]),
            (2, 3, ["1", "x4"]), (3, 4, ["x2", "x3"]),
            (1, 4, ["1"])]),
        "parallel_cancellation": graph(3, [
            (0, 1, ["x1"]), (0, 1, ["x1"]), (0, 1, ["x2"]),
            (1, 2, ["x3"]), (0, 2, ["1"])]),
        "word12": graph(3, [(0, 1, ["x1"]), (1, 2, ["x2"])]),
        "word34": graph(3, [(0, 1, ["x3"]), (1, 2, ["x4"])]),
        "interior_empty_path": graph(3, [
            (0, 1, ["x1"]), (1, 2, ["x2"])], source=1, sink=1),
    }
    jobs = [(a + "__" + b, 4, f, g)
            for a, f in examples.items() for b, g in examples.items()]
    jobs.extend([
        ("empty_alphabet_constants", 0,
         graph(3, [(0, 1, ["1"]), (1, 2, ["1"])]),
         graph(2, [(0, 1, ["1"])])),
        ("one_variable", 1,
         graph(3, [(0, 1, ["1", "x1"]), (1, 2, ["x1"])]),
         graph(2, [(0, 1, ["x1"])])),
    ])
    cases = []
    failures = []
    mutations_detected = 0
    for name, n, f, g in jobs:
        w, q = witness(f, g)
        fp, gp = evaluate(f), evaluate(g)
        target = plus(times(fp, gp), times(gp, fp))
        free, zero, sub = (evaluate(w, mode) for mode in ("free", "zero", "axioms"))
        p = len(f["edges"]) * len(g["edges"])
        nv = 2 + 2 * p * (f["vertices"] + g["vertices"])
        ne = 2 * p * (len(f["edges"]) + len(g["edges"])) + 4 * p + q
        af = sum(s != "1" for _, _, label in f["edges"] for s in label)
        ag = sum(s != "1" for _, _, label in g["edges"] for s in label)
        checks = {"zero_identity": not zero, "substitution_identity": sub == target,
                  "vertex_count": w["vertices"] == nv,
                  "edge_count": len(w["edges"]) == ne,
                  "central_bound": q <= af * ag,
                  "placeholder_linear": all(sum(s.startswith("t:") for s in t) == 1
                                            for t in free)}
        wrong, _ = witness(f, g, wrong_suffix_order=True)
        wrong_sub = evaluate(wrong, "axioms")
        mutation_detected = wrong_sub != target
        mutations_detected += mutation_detected
        if not all(checks.values()):
            failures.append({"case": name, "checks": checks})
        cases.append({"name": name, "alphabet": [f"x{i}" for i in range(1, n + 1)],
                      "axioms": {f"t:{i}:{j}": [[f"x{i}", f"x{j}"], [f"x{j}", f"x{i}"]]
                                 for i in range(1, n + 1) for j in range(i + 1, n + 1)},
                      "input_F": f, "input_G": g, "witness_graph": w,
                      "polynomials": {"f": serial(fp), "g": serial(gp),
                                      "W_free": serial(free), "W_zero": serial(zero),
                                      "W_substituted": serial(sub), "target": serial(target)},
                      "bounds": {"vertices_actual": w["vertices"], "vertices_required": nv,
                                 "edges_actual": len(w["edges"]), "edges_required": ne,
                                 "central_actual": q, "central_upper_bound": af * ag},
                      "checks": checks,
                      "mutation": {"kind": "reverse_suffix_blocks", "detected": mutation_detected,
                                   "substituted": serial(wrong_sub)}})
    if not mutations_detected:
        failures.append({"mutation_test": "no incorrect suffix order detected"})
    result = {"scope": "Finite diagnostics only; L035 contains the all-input proof and bit bound.",
              "summary": {"cases": len(cases), "failures": failures,
                          "mutations_detected": mutations_detected,
                          "max_vertices": max(c["bounds"]["vertices_actual"] for c in cases),
                          "max_edges": max(c["bounds"]["edges_actual"] for c in cases),
                          "all_exact_counts_match": all(c["checks"]["vertex_count"] and c["checks"]["edge_count"] for c in cases)},
              "cases": cases}
    path = Path(__file__).with_name("marked-edge-results.json")
    path.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result["summary"]))
    print("Required: both formal identities and exact counts on every case; q <= a_F*a_G.")
    print("Certificate:", path)
    assert not failures, failures


if __name__ == "__main__":
    main()
