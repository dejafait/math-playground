"""L037 finite actual-graph diagnostic; no asymptotic inference from tests."""
import importlib.util
import json
from pathlib import Path
import sys

BASE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "boolean", BASE / "affine-abp-boolean/check_suffix_graph.py")
boolean = importlib.util.module_from_spec(spec)
spec.loader.exec_module(boolean)
marked = boolean.marked
graph, plus, times, serial = marked.graph, marked.plus, marked.times, marked.serial
copy_into, product, atom = boolean.copy_into, boolean.product, boolean.atom
sys.path.insert(0, str(BASE / "shared-extension"))
from check_assembly import verify  # Separate existing syntactic ER verifier.


def summation(*blocks):
    out = graph(2, [], sink=1)
    for block in blocks:
        a, b = copy_into(out, block)
        out["edges"].extend([[0, a, ["1"]], [b, 1, ["1"]]])
    return out


def evaluate(g, axioms, mode):
    adj = [[] for _ in range(g["vertices"])]
    indegree = [0] * g["vertices"]
    for u, v, label in g["edges"]:
        adj[u].append((v, label))
        indegree[v] += 1
    ready = [u for u, deg in enumerate(indegree) if deg == 0]
    values = [set() for _ in indegree]
    values[g["source"]] = {()}
    visited = 0
    for_pop = ready
    while for_pop:
        u = for_pop.pop()
        visited += 1
        for v, label in adj[u]:
            label_value = set()
            for symbol in label:
                if symbol == "1":
                    term = {()}
                elif symbol in axioms:
                    term = (set() if mode == "zero" else
                            axioms[symbol] if mode == "axioms" else {(symbol,)})
                else:
                    term = {(symbol,)}
                label_value = plus(label_value, term)
            values[v] = plus(values[v], times(values[u], label_value))
            indegree[v] -= 1
            if indegree[v] == 0:
                for_pop.append(v)
    assert visited == g["vertices"], "cycle"
    return values


def run():
    one = graph(1, [])
    x = {i: atom(f"x{i}") for i in (1, 2, 3)}
    # Reordered representative and a genuine nonlinear kernel contribution.
    x[4] = product([x[2], x[1]])
    neg = {i: summation(one, value) for i, value in x.items()}
    factor = {**{i: neg[i] for i in x}, **{-i: x[i] for i in x}}
    H = summation(atom("t:1:2"),
                  product([atom("b:1"), atom("b:2")]),
                  product([summation(product([x[1], x[1]]), x[1]), atom("b:2")]))
    original = [(1,), (-1,), (2,), (3, -3)]
    axioms = {f"b:{i}": {(f"x{i}", f"x{i}"), (f"x{i}",)} for i in (1, 2, 3)}
    axioms.update({f"t:{i}:{j}": {(f"x{i}", f"x{j}"), (f"x{j}", f"x{i}")}
                   for i in (1, 2, 3) for j in range(i + 1, 4)})

    def value(g, mode="free"):
        return evaluate(g, axioms, mode)[g["sink"]]

    def factors(literals):
        return product([factor[v] for v in literals])

    for i, clause in enumerate(original):
        axioms[f"c:{i}"] = value(factors(clause))
    assert value(H, "zero") == set()
    assert value(H, "axioms") == plus(value(x[4]), times(value(x[1]), value(x[2])))
    assert any(sum(s in axioms for s in word) == 2 for word in value(H))

    bool_cache = {}
    pair_cache = {}

    def B(lit):
        if lit not in bool_cache:
            bool_cache[lit] = boolean.construct(factor[lit])[0]
        return bool_cache[lit]

    def W(a, b):
        return marked.witness(a, b)[0]

    def correction_swap(ls, i):
        pair = (ls[i], ls[i + 1])
        if pair not in pair_cache:
            pair_cache[pair] = W(factor[pair[0]], factor[pair[1]])
        return product([factors(ls[:i]), pair_cache[pair], factors(ls[i + 2:])])

    def normalize(literals):
        ls, corrections = list(literals), []
        key = lambda v: (abs(v), v < 0)
        for end in reversed(range(1, len(ls))):
            for i in range(end):
                if key(ls[i]) > key(ls[i + 1]):
                    corrections.append(correction_swap(ls, i))
                    ls[i], ls[i + 1] = ls[i + 1], ls[i]
        i = 0
        while i + 1 < len(ls):
            if ls[i] == ls[i + 1]:
                corrections.append(product([factors(ls[:i]), B(ls[i]), factors(ls[i + 2:])]))
                del ls[i + 1]
            else:
                i += 1
        return ls, summation(*corrections)

    def front(literals, pivot):
        ls, corrections = list(literals), []
        for i in reversed(range(ls.index(pivot))):
            corrections.append(correction_swap(ls, i))
            ls[i], ls[i + 1] = ls[i + 1], ls[i]
        return ls, summation(*corrections)

    out = graph(2, [], sink=1)
    rows, proof, ledger, mutations = [], [], [], []

    def save(literals, local, parents, record):
        node = out["vertices"]
        out["vertices"] += 1
        blocks = [(0, "local", local)] + [(rows[j]["node"], "transition", m) for j, m in parents]
        for start, kind, block in blocks:
            entry, exit_ = copy_into(out, block)
            out["edges"].extend([[start, entry, ["1"]], [exit_, node, ["1"]]])
            ledger.append({"line": len(rows), "kind": kind, "start": start,
                           "vertices": block["vertices"], "edges": len(block["edges"])})
        free = plus(value(local), *(times(rows[j]["free"], value(m)) for j, m in parents))
        assert value(local, "zero") == set()
        rows.append({"literals": list(literals), "node": node, "free": free,
                     "local": local, "parents": [(j, m) for j, m in parents]})
        record["clause"] = tuple(literals)
        proof.append(record)

    for i, clause in enumerate(original):
        save(list(clause), atom(f"c:{i}"), [], {"kind": "input", "source": i + 1})

    def weaken(j, clause):
        added = [v for v in clause if v not in rows[j]["literals"]]
        ls, corr = normalize(rows[j]["literals"] + added)
        save(ls, corr, [(j, factors(added))], {"kind": "weak", "source": j + 1})

    def resolve(j, l, p):
        ls, ej = front(rows[j]["literals"], p)
        rs, el = front(rows[l]["literals"], -p)
        U, V = factors(ls[1:]), factors(rs[1:])
        dest, eo = normalize(ls[1:] + rs[1:])
        comm = product([x[p], W(U, V)])
        local = summation(product([ej, V]), product([el, U]), comm, eo)
        # Detect omission on the substituted formal identity, not on assignments.
        proper = plus(times(plus(value(factors(rows[j]["literals"])), value(ej, "axioms")), value(V)),
                      times(plus(value(factors(rows[l]["literals"])), value(el, "axioms")), value(U)),
                      value(comm, "axioms"))
        assert proper == times(value(U), value(V))
        omitted = plus(proper, value(comm, "axioms"))
        mutations.append({"line": len(rows), "kind": "omit_residual_commutator",
                          "detected": omitted != proper, "actual": serial(omitted), "required": serial(proper)})
        save(dest, local, [(j, V), (l, U)], {"kind": "res", "left": j + 1, "right": l + 1, "pivot": p})

    weaken(0, [1, 2, 3])
    weaken(1, [-1, 2, -3])
    resolve(4, 5, 1)  # shared ancestry, duplicate 2, complementary 3 and -3
    assert rows[-1]["literals"] == [2, 3, -3]

    a, b = x[1], x[2]
    ba, bb = boolean.construct(a)[0], boolean.construct(b)[0]
    kba = W(b, a)
    M = summation(product([a, kba, b]), product([ba, b, b]), product([a, bb]))
    definitions = [summation(product([ba, b]), product([a, kba]), product([H, neg[1]])),
                   summation(product([a, bb]), product([H, neg[2]])),
                   summation(M, product([H, a, b]))]
    raw_clauses = [(-4, 1), (-4, 2), (4, -1, -2)]
    for part, (raw, seed) in enumerate(zip(raw_clauses, definitions), 1):
        assert value(seed, "axioms") == value(factors(raw))
        assert value(seed, "zero") == set()
        ls, corr = normalize(raw)
        save(ls, summation(seed, corr), [], {"kind": "ext", "z": 4, "a": 1, "b": 2, "part": part})
    resolve(0, 9, 1)
    resolve(2, 10, 2)
    resolve(7, 1, 1)
    resolve(11, 12, 4)
    verify(original, proof)
    out["edges"].append([rows[-1]["node"], 1, ["1"]])

    failures = []
    line_evidence = []
    all_values = {mode: evaluate(out, axioms, mode) for mode in ("free", "zero", "axioms")}
    for i, row in enumerate(rows):
        node = row["node"]
        target = value(factors(row["literals"]))
        checks = {"free_recurrence": all_values["free"][node] == row["free"],
                  "zero": not all_values["zero"][node],
                  "substitution": all_values["axioms"][node] == target}
        if not all(checks.values()):
            failures.append({"line": i, "checks": checks})
        line_evidence.append({"line": i, "node": node, "clause": row["literals"], "checks": checks,
                              "polynomials": {"free": serial(all_values["free"][node]),
                                              "zero": serial(all_values["zero"][node]),
                                              "substituted": serial(all_values["axioms"][node]),
                                              "target": serial(target)}})
    required_v = 2 + len(rows) + sum(b["vertices"] for b in ledger)
    required_e = 1 + sum(b["edges"] + 2 for b in ledger)
    degree = max(map(len, all_values["free"][1]), default=0)
    graph_checks = {"vertices_exact": out["vertices"] == required_v,
                    "edges_exact": len(out["edges"]) == required_e,
                    "degree_bound": degree <= out["vertices"] - 1,
                    "IPS_zero": not all_values["zero"][1],
                    "IPS_one": all_values["axioms"][1] == {()},
                    "mutation_detected": any(m["detected"] for m in mutations)}
    if not all(graph_checks.values()):
        failures.append({"graph_checks": graph_checks})
    # Focused graph-operation boundary checks; also apply W to these x-only inputs.
    boundaries = [graph(3, [(0, 1, ["x1"]), (1, 2, ["x2"])], 1, 1),
                  graph(4, [(3, 1, ["1", "x1"]), (1, 0, ["x2"]), (0, 2, ["x3"])], 1, 0),
                  graph(3, [(0, 2, ["x1"]), (0, 2, ["x1"]), (0, 1, ["1"]), (1, 2, ["x2"])])]
    boundary_evidence = []
    for g in boundaries:
        composite = product([g, H, g])
        expected = times(times(value(g), value(H)), value(g))
        wg = W(g, x[2])
        checks = {"composition": value(composite) == expected,
                  "commutator": value(wg, "axioms") == plus(times(value(g), value(x[2])), times(value(x[2]), value(g))),
                  "zero": not value(wg, "zero")}
        if not all(checks.values()):
            failures.append({"boundary": checks})
        boundary_evidence.append({"input": g, "composite": composite, "W": wg, "checks": checks,
                                  "composition_actual": serial(value(composite)), "composition_required": serial(expected)})
    result = {"scope": "Finite diagnostic only; full proof and asymptotic ledger are in L037.",
              "summary": {"lines": len(rows), "failures": failures, "graph_checks": graph_checks,
                          "mutations_detected": sum(m["detected"] for m in mutations),
                          "boundary_cases": len(boundaries)},
              "source": {"F": original, "pi": proof, "ER_verified": True},
              "supplied_representatives": x, "supplied_H": H,
              "H_free": serial(value(H)), "H_substituted": serial(value(H, "axioms")),
              "axioms": {k: serial(v) for k, v in axioms.items()},
              "output_graph": out, "ledger": ledger, "lines": line_evidence,
              "bounds": {"vertices_actual": out["vertices"], "vertices_required": required_v,
                         "edges_actual": len(out["edges"]), "edges_required": required_e,
                         "formal_degree_actual": degree, "formal_degree_upper": out["vertices"] - 1},
              "mutations": mutations, "boundaries": boundary_evidence}
    path = Path(__file__).with_name("assembly-results.json")
    path.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result["summary"]))
    print("Actual/required bounds:", json.dumps(result["bounds"]))
    print("Full certificate:", path)
    assert not failures, failures


if __name__ == "__main__":
    run()
