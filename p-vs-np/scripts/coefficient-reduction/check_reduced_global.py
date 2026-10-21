"""Finite free-word audit of reduced global propagation; no quotient reductions."""
import json
import sys
from pathlib import Path

from check_correction_update import add, degree, mul, subst, var
from check_reduced_product import formulas, targets

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "shared-extension"))
from check_assembly import verify

ZERO, ONE = set(), {()}


def encoded(poly):
    return [list(word) for word in sorted(poly)]


def main():
    # Independently check the formerly untested second product-pair orientation.
    g, a, b, z, ka, kb, h = map(var, "g a b z ka kb h".split())
    second = add(mul(ka, b), mul(a, kb), mul(g, h), mul(h, g))
    assignment = {"ka": add(mul(g, a), mul(a, g)),
                  "kb": add(mul(g, b), mul(b, g)), "h": add(z, mul(a, b))}
    assert subst(second, assignment) == add(mul(g, z), mul(z, g))
    assert subst(second, {"ka": ZERO, "kb": ZERO, "h": ZERO}) == ZERO
    corrupted = add(second, mul(a, kb), mul(kb, a))
    assert subst(corrupted, assignment) != add(mul(g, z), mul(z, g))

    x, y, bx, by, c, f0, f1, f2 = map(var, "x y bx by c f0 f1 f2".split())
    axioms = {"bx": add(mul(x, x), x), "by": add(mul(y, y), y),
              "c": add(mul(x, y), mul(y, x)),
              "f0": add(ONE, x), "f1": x,
              "f2": mul(add(ONE, y), y)}
    zero = {label: ZERO for label in axioms}
    # A nonlinear supplied relation includes a nonzero polynomial in the kernel
    # of axiom substitution. Neither formal degree nor sectors are discarded.
    kernel = add(mul(bx, by), mul(add(mul(x, x), x), by))
    hyx = add(mul(mul(y, c), x), mul(by, mul(x, x)), mul(y, bx))
    values = [ZERO, ONE, x, y, add(ONE, x), add(ONE, y), x,
              add(ONE, x), mul(y, x), add(ONE, mul(y, x)), mul(y, x)]
    kinds = [("constant",), ("constant",), ("input", "bx"), ("input", "by"),
             ("signed", 2), ("signed", 3), ("and", 2, 2), ("signed", 6),
             ("and", 6, 3), ("signed", 8), ("and", 8, 8)]
    relations = {6: add(bx, kernel), 8: c, 10: hyx}
    S, d = len(values), max(map(degree, values))
    hbound = max(degree(p) for p in relations.values())
    for i, relation in relations.items():
        _, ai, bi = kinds[i]
        assert subst(relation, axioms) == add(values[i], mul(values[ai], values[bi]))
        assert subst(relation, zero) == ZERO

    table, dependencies = {}, {}
    for total in range(2 * S - 1):
        for i in range(S):
            j = total - i
            if not 0 <= j < S:
                continue
            vi, vj = values[i], values[j]
            ki, kj = kinds[i], kinds[j]
            dep = []
            if i == j or ki[0] == "constant" or kj[0] == "constant":
                out = ZERO
            elif ki[0] == kj[0] == "input":
                out = c
            elif ki[0] in ("and", "signed"):
                if ki[0] == "signed":
                    dep = [(ki[1], j)]
                    out = table[dep[0]]
                else:
                    _, ai, bi = ki
                    dep = [(bi, j), (ai, j)]
                    out = add(mul(values[ai], table[bi, j]),
                              mul(table[ai, j], values[bi]),
                              mul(relations[i], vj), mul(vj, relations[i]))
            else:
                if kj[0] == "signed":
                    dep = [(i, kj[1])]
                    out = table[dep[0]]
                else:
                    _, ai, bi = kj
                    dep = [(i, ai), (i, bi)]
                    out = add(mul(table[i, ai], values[bi]),
                              mul(values[ai], table[i, bi]),
                              mul(vi, relations[j]), mul(relations[j], vi))
            assert all(sum(pair) < total for pair in dep)
            assert subst(out, axioms) == add(mul(vi, vj), mul(vj, vi))
            assert subst(out, zero) == ZERO
            assert degree(out) <= hbound + (i + j + 2) * d
            table[i, j], dependencies[i, j] = out, dep

    boolean, definitions = [], {}
    for i, kind in enumerate(kinds):
        if kind[0] == "constant":
            out = ZERO
        elif kind[0] == "input":
            out = var(kind[1])
        elif kind[0] == "signed":
            out = boolean[kind[1]]
        else:
            _, ai, bi = kind
            local = formulas(values[ai], values[bi], values[i], ONE,
                             boolean[ai], boolean[bi], table[bi, ai],
                             ZERO, ZERO, relations[i])
            out = local["reduced_boolean"]
            definitions[i] = {name: local[name] for name in
                              ("definition_1", "definition_2", "definition_3")}
            expected = targets(values[ai], values[bi], values[i], ONE)
            for name, polynomial in definitions[i].items():
                assert subst(polynomial, axioms) == expected[name]
                assert subst(polynomial, zero) == ZERO
                assert degree(polynomial) <= hbound + (4 * S + 2) * d
        assert subst(out, axioms) == add(mul(values[i], values[i]), values[i])
        assert subst(out, zero) == ZERO
        assert degree(out) <= hbound + (2 * S + 2 * (i + 1)) * d
        boolean.append(out)

    # Complete ER derivation from units x, NOT x, using z iff x AND x.
    # Signed literal -> abstract falsity-value node; clause order is numerical.
    factor = {1: 4, -1: 2, 2: 5, -2: 3, 3: 7, -3: 6}
    def product(literals):
        result = ONE
        for literal in literals:
            result = mul(result, values[factor[literal]])
        return result

    def normalize(literals, root):
        literals = list(literals)
        key = lambda v: (abs(v), v < 0)
        for end in reversed(range(1, len(literals))):
            for i in range(end):
                if key(literals[i]) > key(literals[i + 1]):
                    root = add(root, mul(mul(product(literals[:i]),
                                           table[factor[literals[i]], factor[literals[i + 1]]]),
                                        product(literals[i + 2:])))
                    literals[i], literals[i + 1] = literals[i + 1], literals[i]
        i = 0
        while i + 1 < len(literals):
            if literals[i] == literals[i + 1]:
                root = add(root, mul(mul(product(literals[:i]),
                                       boolean[factor[literals[i]]]), product(literals[i + 2:])))
                del literals[i + 1]
            else:
                i += 1
        return literals, root

    def front(literals, root, pivot):
        literals = list(literals)
        for i in reversed(range(literals.index(pivot))):
            root = add(root, mul(mul(product(literals[:i]),
                                   table[factor[literals[i]], factor[literals[i + 1]]]),
                                product(literals[i + 2:])))
            literals[i], literals[i + 1] = literals[i + 1], literals[i]
        return literals, root

    rows = []
    def save(literals, root):
        assert subst(root, axioms) == product(literals)
        assert subst(root, zero) == ZERO
        rows.append((list(literals), root))

    save([1], f0)
    save([-1], f1)
    save([2, -2], f2)
    for literals, name in [([-3, 1], "definition_1"),
                           ([-3, 1], "definition_2"),
                           ([3, -1, -1], "definition_3")]:
        ls, root = normalize(literals, definitions[6][name])
        save(ls, root)

    def resolve(left, right, pivot):
        lc, lr = front(*rows[left], pivot)
        rc, rr = front(*rows[right], -pivot)
        U, witness = ONE, ZERO
        # Positive-value node is the falsity factor of the negative pivot.
        pnode = factor[-pivot]
        for literal in lc[1:]:
            qnode = factor[literal]
            witness = add(mul(witness, values[qnode]), mul(U, table[pnode, qnode]))
            U = mul(U, values[qnode])
        V = product(rc[1:])
        raw = add(mul(lr, V), mul(U, rr), mul(witness, V))
        literals, root = normalize(lc[1:] + rc[1:], raw)
        save(literals, root)

    resolve(0, 5, 1)  # z
    resolve(3, 1, 1)  # NOT z
    resolve(6, 7, 3)  # empty clause
    assert rows[-1][0] == [] and subst(rows[-1][1], axioms) == ONE

    original = [(1,), (-1,), (2, -2)]
    proof = [{"kind": "input", "source": i + 1, "clause": tuple(rows[i][0])}
             for i in range(3)]
    proof += [{"kind": "ext", "z": 3, "a": 1, "b": 1,
               "part": i + 1, "clause": tuple(rows[i + 3][0])} for i in range(3)]
    proof += [{"kind": "res", "left": left, "right": right, "pivot": pivot,
               "clause": tuple(rows[i + 6][0])}
              for i, (left, right, pivot) in enumerate([(1, 6, 1), (4, 2, 1), (7, 8, 3)])]
    verify(original, proof)
    # Fully written JSON is one explicit binary encoding; its bits give T here.
    T = 2 + 8 * len(json.dumps({"F": original, "pi": proof}, separators=(",", ":")).encode())
    required_degree = hbound + (4 * S + T * T + 2 * T + 2) * d
    assert max(degree(root) for _, root in rows) <= required_degree
    result = {
        "scope": "Finite exact word expansion; the all-S,T bound is proved in L025, not inferred from this sample.",
        "parameters": {"S": S, "d": d, "h": hbound, "T_written_json_bits": T},
        "source_ER_checked": True, "source": {"F": original, "pi": proof},
        "pairs_checked": len(table), "boolean_outputs_checked": len(boolean),
        "defining_outputs_checked": 3 * len(definitions), "clause_lines_checked": len(rows),
        "actual_degree": {"pair": max(map(degree, table.values())),
                          "boolean": max(map(degree, boolean)),
                          "certificate": degree(rows[-1][1])},
        "required_bounds": {"pair": hbound + 2 * S * d,
                            "boolean": hbound + 4 * S * d,
                            "certificate": required_degree},
        "failed_checks": [], "errors_detected": ["reversed coefficient in second pair orientation"],
        "axioms": {name: encoded(poly) for name, poly in axioms.items()},
        "values": list(map(encoded, values)),
        "relations": {str(i): encoded(poly) for i, poly in relations.items()},
        "pairs": {f"{i},{j}": {"rank": i + j, "recursive_pairs": dependencies[i, j],
                                "polynomial": encoded(poly)} for (i, j), poly in table.items()},
        "boolean": list(map(encoded, boolean)),
        "definitions": {str(i): {name: encoded(poly) for name, poly in outputs.items()}
                        for i, outputs in definitions.items()},
        "clauses": [{"literals": ls, "polynomial": encoded(root)} for ls, root in rows],
    }
    path = Path(__file__).with_name("reduced-global-results.json")
    path.write_text(json.dumps(result, indent=2) + "\n")
    print(f"PASS: {len(table)} pairs, {len(boolean)} Boolean outputs, {3 * len(definitions)} defining outputs, {len(rows)} clause lines; both IPS identities.")
    print(f"Actual degrees: {result['actual_degree']}; required upper bounds: {result['required_bounds']}.")
    print("Failed checks: none; one corrupt second-orientation recurrence detected.")
    print("Artifact: scripts/coefficient-reduction/reduced-global-results.json; sample includes nonlinear local relation witnesses.")


if __name__ == "__main__":
    main()
