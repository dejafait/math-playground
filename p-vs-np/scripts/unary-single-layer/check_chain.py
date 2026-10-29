#!/usr/bin/env python3
"""Exact finite replay of L115; writes all graphs, maps and equation defects."""

import argparse
import itertools
import json
from pathlib import Path


def graph(vertices, edges, source, sink):
    return {"vertices": vertices, "edges": edges, "source": source, "sink": sink}


def zero(r, c):
    return [[0] * c for _ in range(r)]


def identity(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def add(a, b):
    return [[x ^ y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def multiply(a, b):
    ans = zero(len(a), len(b[0]))
    for i, row in enumerate(a):
        for k, bit in enumerate(row):
            if bit:
                for j, value in enumerate(b[k]):
                    ans[i][j] ^= value
    return ans


def defects(a, b):
    return [[i, j, x, y] for i, (ar, br) in enumerate(zip(a, b))
            for j, (x, y) in enumerate(zip(ar, br)) if x != y]


def representation(g):
    vs = g["vertices"]
    assert len(vs) == len(set(vs))
    index = {v: i for i, v in enumerate(vs)}
    n = len(vs)
    c, d, adjacency = zero(n, n), zero(n, n), [set() for _ in vs]
    for u, v, label in g["edges"]:
        assert label in (0, 1)
        i, j = index[u], index[v]
        (c if label == 0 else d)[i][j] ^= 1
        adjacency[i].add(j)
    # Acyclicity is checked on every incidence, before parity cancellation.
    indegree = [sum(i in row for row in adjacency) for i in range(n)]
    todo = [i for i, deg in enumerate(indegree) if not deg]
    order = []
    while todo:
        i = todo.pop()
        order.append(i)
        for j in adjacency[i]:
            indegree[j] -= 1
            if not indegree[j]:
                todo.append(j)
    assert len(order) == n
    k, power = identity(n), identity(n)
    for _ in range(1, n):
        power = multiply(power, c)
        k = add(k, power)
    assert not any(map(any, multiply(power, c)))
    alpha = [k[index[g["source"]]]]
    beta = [[int(v == g["sink"])] for v in vs]
    return {"alpha": alpha, "M": multiply(d, k), "beta": beta}


def substitute(g):
    es = []
    for u, v, label in g["edges"]:
        es.append([u, v, label])
        if label:
            es.append([u, v, 0])
    return graph(g["vertices"], es, g["source"], g["sink"])


def products(n, es, p, q, layer_labels):
    gs = [f"g{i}" for i in range(n)]
    internal = [[gs[i], gs[j], l] for i, j, l in es]
    layer = [["f0", "f1", l] for l in layer_labels]
    vertices = ["s", "t", "f0", "f1"] + gs
    a = graph(vertices, internal + layer + [
        ["s", "f0", 0], ["f1", gs[p], 0], [gs[q], "t", 0]], "s", "t")
    b = graph(vertices, internal + layer + [
        ["s", gs[p], 0], [gs[q], "f0", 0], ["f1", "t", 0]], "s", "t")
    return a, b


def build(n, es, p, q):
    # H=T(G), retaining every parallel occurrence.
    hs = [list(e) for e in es] + [[u, v, 0] for u, v, l in es if l]
    gs = [f"g{i}" for i in range(n)]
    us, vs = [f"u{i}" for i in range(n)], [f"v{i}" for i in range(n)]
    ax, bx = products(n, hs, p, q, [1])
    internal = [[gs[u], gs[v], l] for u, v, l in hs]
    a0 = graph(["s", "t", "a"] + gs, internal + [
        ["s", "a", 0], ["a", gs[p], 1], [gs[q], "t", 0]], "s", "t")
    b0 = graph(["s", "t"] + gs, internal + [
        ["s", gs[p], 0], [gs[q], "t", 1]], "s", "t")
    qe = [["s", vs[p], 0], [us[q], "t", 0]]
    re = [["s", vs[p], 0], [vs[q], "t", 1]]
    for i in range(n):
        qe.append([vs[i], us[i], 1])
        re.append([vs[i], us[i], 1])
    for u, v, label in hs:
        if label:
            qe.append([us[u], vs[v], 0])
            re.append([vs[u], vs[v], 1])
        else:
            qe.append([us[u], us[v], 0])
            re.extend([[us[u], us[v], 0], [vs[u], vs[v], 0]])
    qg = graph(["s", "t"] + us + vs, qe, "s", "t")
    rg = graph(["s", "t"] + us + vs, re, "s", "t")
    base = {"A": ax, "A0": a0, "Q": qg, "R": rg, "B0": b0, "B": bx}
    terms = [
        [(v, v) for v in ["s", "t"] + gs] + [("f0", "a")],
        [("s", "s"), ("t", "t"), ("a", vs[p])] +
        [(gs[i], us[i]) for i in range(n)] +
        [(gs[u], vs[v]) for u, v, l in hs if l],
        [(v, v) for v in ["s", "t"] + us + vs] +
        [(ls[u], ls[v]) for u, v, l in hs if not l for ls in (us, vs)],
        [("s", "s"), ("t", "t")] + [(vs[i], gs[i]) for i in range(n)],
        [("s", "s"), ("t", "f1"), ("t", "t"), (gs[q], "f0")] +
        [(v, v) for v in gs],
    ]
    arrow_names = [("A", "A0"), ("A0", "Q"), ("R", "Q"),
                   ("R", "B0"), ("B0", "B")]
    arrows = []
    for (src, dst), entries in zip(arrow_names, terms):
        rows, cols = base[src]["vertices"], base[dst]["vertices"]
        x = zero(len(rows), len(cols))
        for u, v in entries:
            x[rows.index(u)][cols.index(v)] ^= 1
        arrows.append({"source": src, "target": dst, "matrix": x})
    final = {name: substitute(g) for name, g in base.items()}
    transformed_endpoints = {name: final[name] for name in ("A", "B")}
    final["A"], final["B"] = products(n, es, p, q, [0, 1])
    return base, final, transformed_endpoints, arrows


def check_arrows(graphs, arrows):
    reps = {name: representation(g) for name, g in graphs.items()}
    checks = []
    for arrow in arrows:
        u, v = reps[arrow["source"]], reps[arrow["target"]]
        x = arrow["matrix"]
        checks.append({
            "alpha_defects": defects(multiply(u["alpha"], x), v["alpha"]),
            "transition_defects": defects(multiply(u["M"], x), multiply(x, v["M"])),
            "beta_defects": defects(u["beta"], multiply(x, v["beta"])),
        })
    return checks, reps


def fixtures():
    for n in range(1, 4):
        pairs = list(itertools.combinations(range(n), 2))
        for kinds in itertools.product(range(4), repeat=len(pairs)):
            es = [[u, v, label] for (u, v), kind in zip(pairs, kinds)
                  for label in (0, 1) if kind & (1 << label)]
            for p, q in itertools.product(range(n), repeat=2):
                yield "all-parity-dags-n<=3", n, es, p, q
    extra = [
        (2, [[0, 1, l] for l in (0, 0, 1, 1)]),
        (2, [[0, 1, l] for l in (0, 0, 0, 1, 1, 1)]),
        (4, [[0, 1, 0], [0, 2, 1], [1, 3, 1], [2, 3, 0],
             [0, 3, 1], [0, 3, 1], [1, 2, 0], [1, 2, 0]]),
    ]
    for n, es in extra:
        for p, q in itertools.product(range(n), repeat=2):
            yield "parallel-occurrence-fixture", n, es, p, q


def size(g):
    return len(g["vertices"]) + 2 * len(g["edges"])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).resolve().parent / "output-529",
                        help="Fresh output directory; existing evidence is never overwritten.")
    out = parser.parse_args().output.resolve()
    out.mkdir(parents=True, exist_ok=False)
    cases, failures = [], []
    max_support = max_graph = max_combined = 0
    for number, (family, n, es, p, q) in enumerate(fixtures()):
        c, d = sum(l == 0 for _, _, l in es), sum(l == 1 for _, _, l in es)
        base, final, transformed, arrows = build(n, es, p, q)
        base_checks, _ = check_arrows(base, arrows)
        final_checks, reps = check_arrows(final, arrows)
        endpoint_checks = {name: {
            key: defects(representation(transformed[name])[key], reps[name][key])
            for key in ("alpha", "M", "beta")} for name in transformed}
        support = sum(sum(map(sum, arrow["matrix"])) for arrow in arrows)
        repeated = 2 * sum(size(final[name]) for name in ("A0", "Q", "R", "B0"))
        s = size(final["A"]) + size(final["B"])
        expected_sizes = {"A0": n + 2*c + 6*d + 11,
                          "Q": 6*n + 2*c + 4*d + 6,
                          "R": 6*n + 4*c + 8*d + 8,
                          "B0": n + 2*c + 6*d + 8}
        ledger = {
            "S_actual": s, "S_formula": 2*n + 4*c + 4*d + 28,
            "support_actual": support, "support_bound": 6*n + 2*c + 3*d + 14,
            "repeated_graph_actual": repeated,
            "repeated_graph_formula": 28*n + 20*c + 48*d + 66,
            "combined_actual": support + repeated, "combined_required": 17*s,
            "graph_sizes_actual": {name: size(final[name]) for name in expected_sizes},
            "graph_sizes_formula": expected_sizes,
        }
        good = (not any(any(check.values()) for check in base_checks + final_checks)
                and not any(any(check.values()) for check in endpoint_checks.values())
                and s == ledger["S_formula"]
                and support <= ledger["support_bound"]
                and repeated == ledger["repeated_graph_formula"]
                and ledger["graph_sizes_actual"] == expected_sizes
                and support <= 3*s and repeated <= 14*s and support + repeated <= 17*s)
        if not good:
            failures.append(number)
        max_support = max(max_support, support / s)
        max_graph = max(max_graph, repeated / s)
        max_combined = max(max_combined, (support + repeated) / s)
        cases.append({"id": number, "family": family,
                      "input": {"n": n, "edges": es, "p": p, "q": q},
                      "base_graphs": base, "final_graphs": final,
                      "transformed_endpoints": transformed, "arrows": arrows,
                      "base_checks": base_checks, "final_checks": final_checks,
                      "endpoint_checks": endpoint_checks, "ledger": ledger, "passed": good})
    summary = {"cases": len(cases), "arrows_checked": 10*len(cases),
               "failures": failures, "max_support_over_S": max_support,
               "required_support_over_S": 3,
               "max_repeated_graph_over_S": max_graph,
               "required_repeated_graph_over_S": 14,
               "max_combined_over_S": max_combined, "required_combined_over_S": 17,
               "scope": "Finite replay only; universal proof is L115 sections 2-6."}
    path = out / "certificate.json"
    path.write_text(json.dumps({"summary": summary, "cases": cases}, separators=(",", ":")) + "\n")
    (out / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary, indent=2))
    print(f"Full certificate: {path}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
