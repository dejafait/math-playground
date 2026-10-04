#!/usr/bin/env python3
"""L021: syntactic ER checks and independent finite formal-word IPS checks.

Large cases count the fully framed rooted-DAG/axiom serialization without
expanding words. No general-circuit PIT or optimal-certificate claim is made.
"""

import copy
import importlib.util
import itertools
import json
from pathlib import Path

from check_witnesses import Circuit, ONE, ZERO, add_poly, mul_poly, witnesses


def clause(literals):
    return tuple(sorted(set(literals), key=lambda v: (abs(v), v < 0)))


def verify(original, proof, refutation=True):
    known = {abs(v) for c in original for v in c}
    pending = None
    assert all(len(c) <= 3 and all(v != 0 for v in c) for c in original)
    for number, record in enumerate(proof, 1):
        c, kind = record["clause"], record["kind"]
        assert c == clause(c) and all(v != 0 for v in c)
        if kind == "ext":
            z, a, b, part = (record[k] for k in ("z", "a", "b", "part"))
            if part == 1:
                assert pending is None and z > 0 and z not in known
                assert abs(a) in known and abs(b) in known
                pending = (z, a, b, 1)
            else:
                assert pending == (z, a, b, part - 1)
                pending = (z, a, b, part)
            raw = ((-z, a), (-z, b), (z, -a, -b))[part - 1]
            assert c == clause(raw)
            if part == 3:
                known.add(z)
                pending = None
        else:
            assert pending is None
            if kind == "input":
                assert 1 <= record["source"] <= len(original)
                assert c == clause(original[record["source"] - 1])
            elif kind == "weak":
                assert 1 <= record["source"] < number
                assert set(proof[record["source"] - 1]["clause"]) <= set(c)
                known.update(abs(v) for v in c)
            else:
                assert kind == "res"
                left, right, pivot = (record[k] for k in ("left", "right", "pivot"))
                assert 1 <= left < number and 1 <= right < number and pivot > 0
                l, r = proof[left - 1]["clause"], proof[right - 1]["clause"]
                assert pivot in l and -pivot in r
                assert c == clause([v for v in l if v != pivot] +
                                   [v for v in r if v != -pivot])
    assert pending is None
    if refutation:
        assert proof and proof[-1]["clause"] == ()


def axiom_polys(original):
    variables = sorted({abs(v) for c in original for v in c})
    x = {v: frozenset({(v,)}) for v in variables}
    result = {}
    for i, c in enumerate(original):
        value = ONE
        for v in c:
            factor = add_poly(ONE, x[abs(v)]) if v > 0 else x[abs(v)]
            value = mul_poly(value, factor)
        result[("f", i)] = value
    for v in variables:
        result[("b", v)] = add_poly(mul_poly(x[v], x[v]), x[v])
    for v, w in itertools.combinations(variables, 2):
        result[("c", v, w)] = add_poly(mul_poly(x[v], x[w]), mul_poly(x[w], x[v]))
    return result


def expand(circuit, original, substitute):
    axioms = axiom_polys(original) if substitute else {}
    values = []
    for spec in circuit.nodes:
        kind = spec[0]
        if kind == "c":
            value = ONE if spec[1] else ZERO
        elif kind == "x":
            value = frozenset({(spec[1],)})
        elif kind == "t":
            value = axioms[spec[1]] if substitute else ZERO
        else:
            a, b = values[spec[1]], values[spec[2]]
            value = add_poly(a, b) if kind == "+" else mul_poly(a, b)
        values.append(value)
    return values


def expected_clauses(original, proof):
    """Compute values directly from source records, independently of gate DAGs."""
    variables = {abs(v) for c in original for v in c}
    p = {v: frozenset({(v,)}) for v in variables}

    def literal(v):
        value = p.get(abs(v), ZERO)
        return value if v > 0 else add_poly(ONE, value)

    result = []
    for record in proof:
        if record["kind"] == "ext" and record["part"] == 1:
            p[record["z"]] = mul_poly(literal(record["a"]), literal(record["b"]))
        value = ONE
        for v in record["clause"]:
            value = mul_poly(value, literal(-v))
        result.append(value)
    return result


class Assembly:
    def __init__(self, original, proof, mutation=None):
        self.original, self.proof, self.mutation = original, proof, mutation
        self.circuit = Circuit()
        self.p, self.n = {}, {}
        self.counts = {"swaps": 0, "duplicate_deletions": 0, "resolution": 0,
                       "weakening": 0, "clause_references": 0}
        for v in sorted({abs(v) for c in original for v in c}):
            self.p[v] = self.circuit.node(("x", v))
        for record in proof:
            if record["kind"] == "ext" and record["part"] == 1:
                self.p[record["z"]] = self.circuit.mul(self.value(record["a"]),
                                                      self.value(record["b"]))
            for v in record["clause"]:
                self.p.setdefault(abs(v), self.circuit.zero)
        for v in self.p:
            self.value(-v)
        self.base, self.k, self.b = witnesses(self.circuit)
        self.roots = []
        for record in proof:
            kind, target = record["kind"], record["clause"]
            if kind == "input":
                i = record["source"] - 1
                root = self.circuit.node(("t", ("f", i)))
                root = self.normalize(self.original[i], root)
            elif kind == "ext":
                z, a, b, part = (record[k] for k in ("z", "a", "b", "part"))
                av, bv = self.value(a), self.value(b)
                if part == 1:
                    root = self.circuit.add(self.circuit.mul(self.b[av], bv),
                                            self.circuit.mul(av, self.k[bv, av]))
                elif part == 2:
                    root = self.circuit.mul(av, self.b[bv])
                else:
                    root = self.b[self.p[z]]
                raw = ((-z, a), (-z, b), (z, -a, -b))[part - 1]
                root = self.normalize(raw, root)
            elif kind == "weak":
                index = record["source"] - 1
                source = proof[index]["clause"]
                added = [v for v in target if v not in source]
                root = self.circuit.mul(self.roots[index], self.product(added))
                root = self.normalize(list(source) + added, root)
                self.counts["weakening"] += 1
                self.counts["clause_references"] += 1
            else:
                li, ri, pivot = (record[k] for k in ("left", "right", "pivot"))
                left, right = proof[li - 1]["clause"], proof[ri - 1]["clause"]
                lc, lr = self.front(left, self.roots[li - 1], pivot)
                rc, rr = self.front(right, self.roots[ri - 1], -pivot)
                u, h = self.product_commutator(self.p[pivot], lc[1:])
                v = self.product(rc[1:])
                first = self.circuit.mul(lr, v)
                second = (self.circuit.mul(rr, u) if mutation == "coefficient_order"
                          else self.circuit.mul(u, rr))
                root = self.circuit.add(first, second)
                if mutation != "pivot_commutator":
                    root = self.circuit.add(root, self.circuit.mul(h, v))
                root = self.normalize(lc[1:] + rc[1:], root)
                self.counts["resolution"] += 1
                self.counts["clause_references"] += 2
            self.roots.append(root)

    def value(self, v):
        p = self.p.get(abs(v), self.circuit.zero)
        if v > 0:
            return p
        if abs(v) not in self.n:
            self.n[abs(v)] = self.circuit.add(self.circuit.one, p)
        return self.n[abs(v)]

    def product(self, literals):
        return self.circuit.product([self.value(-v) for v in literals])

    def correction(self, literals, index, witness, removed=2):
        left = self.product(literals[:index])
        right = self.product(literals[index + removed:])
        return self.circuit.mul(self.circuit.mul(left, witness), right)

    def swap(self, literals, root, index):
        a, b = (self.value(-v) for v in literals[index:index + 2])
        if self.mutation != "sorting":
            root = self.circuit.add(root, self.correction(literals, index, self.k[a, b]))
        literals[index], literals[index + 1] = literals[index + 1], literals[index]
        self.counts["swaps"] += 1
        return root

    def normalize(self, literals, root):
        literals = list(literals)
        key = lambda v: (abs(v), v < 0)
        for end in reversed(range(1, len(literals))):
            for i in range(end):
                if key(literals[i]) > key(literals[i + 1]):
                    root = self.swap(literals, root, i)
        i = 0
        while i + 1 < len(literals):
            if literals[i] == literals[i + 1]:
                q = self.value(-literals[i])
                if self.mutation != "duplicate":
                    root = self.circuit.add(root, self.correction(literals, i, self.b[q]))
                del literals[i + 1]
                self.counts["duplicate_deletions"] += 1
            else:
                i += 1
        assert tuple(literals) == clause(literals)
        return root

    def front(self, literals, root, selected):
        literals = list(literals)
        position = literals.index(selected)
        for i in reversed(range(position)):
            root = self.swap(literals, root, i)
        return literals, root

    def product_commutator(self, p, literals):
        product, h = self.circuit.one, self.circuit.zero
        for v in literals:
            q = self.value(-v)
            h = self.circuit.add(self.circuit.mul(h, q),
                                 self.circuit.mul(product, self.k[p, q]))
            product = self.circuit.mul(product, q)
        return product, h

    def formal_check(self, refutation=True):
        full, zero = expand(self.circuit, self.original, True), expand(self.circuit, self.original, False)
        expected = expected_clauses(self.original, self.proof)
        degrees = self.circuit.placeholder_degrees()
        for root, target in zip(self.roots, expected):
            assert full[root] == target and zero[root] == ZERO and degrees[root] <= 1
        if refutation:
            assert full[self.roots[-1]] == ONE
        allowed = set(axiom_polys(self.original))
        assert all(spec[1] in allowed for spec in self.circuit.nodes if spec[0] == "t")
        variables = {abs(v) for c in self.original for v in c}
        assert all(spec[1] in variables for spec in self.circuit.nodes if spec[0] == "x")

    def framed_size(self):
        root = self.roots[-1]
        used, stack = set(), [root]
        while stack:
            g = stack.pop()
            if g in used:
                continue
            used.add(g)
            if self.circuit.nodes[g][0] in ("+", "*"):
                stack.extend(self.circuit.nodes[g][1:])
        remap = {g: i for i, g in enumerate(sorted(used))}
        expr_x = lambda v: ["x", v]
        expr_neg = lambda v: ["+", ["c", 1], expr_x(v)]
        axioms, labels = [], {}
        for i, c in enumerate(self.original):
            value = ["c", 1]
            for v in c:
                factor = expr_neg(abs(v)) if v > 0 else expr_x(abs(v))
                value = ["*", value, factor]
            labels[("f", i)] = len(axioms)
            axioms.append(value)
        variables = sorted({abs(v) for c in self.original for v in c})
        for v in variables:
            labels[("b", v)] = len(axioms)
            axioms.append(["+", ["*", expr_x(v), expr_x(v)], expr_x(v)])
        for v, w in itertools.combinations(variables, 2):
            labels[("c", v, w)] = len(axioms)
            axioms.append(["+", ["*", expr_x(v), expr_x(w)], ["*", expr_x(w), expr_x(v)]])
        records = []
        for g in sorted(used):
            spec = self.circuit.nodes[g]
            if spec[0] in ("+", "*"):
                assert spec[1] < g and spec[2] < g
                records.append([spec[0], remap[spec[1]], remap[spec[2]]])
            elif spec[0] == "t":
                records.append(["t", labels[spec[1]]])
            else:
                records.append(list(spec))
        payload = {"field": "F2", "multiplication": "ordered", "axioms": axioms,
                   "nodes": records, "root": remap[root]}
        bits = 8 * len(json.dumps(payload, separators=(",", ":")).encode("utf8"))
        assert max(self.circuit.placeholder_degrees()) <= 1
        return {"proof_lines": len(self.proof), "network_nodes": len(self.circuit.nodes), "rooted_nodes": len(used),
                "full_serialization_bits": bits, "axioms": len(axioms), **self.counts}


def local_proof(left, right, pivot=1):
    original = (tuple(reversed(left)), tuple(reversed(right)))
    result = clause([v for v in left if v != pivot] + [v for v in right if v != -pivot])
    proof = [{"kind": "input", "source": 1, "clause": clause(left)},
             {"kind": "input", "source": 2, "clause": clause(right)},
             {"kind": "res", "left": 1, "right": 2, "pivot": pivot, "clause": result}]
    return original, proof


def main():
    cases = []
    choices_left = [-1, 2, -2, 3, -3]
    choices_right = [1, 2, -2, 3, -3]
    subsets = lambda values: [c for size in range(3) for c in itertools.combinations(values, size)]
    for left in subsets(choices_left):
        for right in subsets(choices_right):
            original, proof = local_proof((1,) + left, (-1,) + right)
            verify(original, proof, False)
            construction = Assembly(original, proof)
            construction.formal_check(False)
            cases.append(construction.framed_size())

    original = ((3, 3), (-3,))
    proof = [{"kind": "input", "source": 1, "clause": (3,)},
             {"kind": "input", "source": 2, "clause": (-3,)},
             {"kind": "weak", "source": 1, "clause": (1, -2, 3)},
             {"kind": "res", "left": 1, "right": 2, "pivot": 3, "clause": ()}]
    verify(original, proof)
    construction = Assembly(original, proof)
    construction.formal_check()
    cases.append(construction.framed_size())

    for original, proof in [(((),), [{"kind": "input", "source": 1, "clause": ()}]),
                            (((1, -1), (1,), (-1,)),
                             [{"kind": "input", "source": 1, "clause": (1, -1)},
                              {"kind": "input", "source": 2, "clause": (1,)},
                              {"kind": "input", "source": 3, "clause": (-1,)},
                              {"kind": "res", "left": 2, "right": 3, "pivot": 1, "clause": ()}])]:
        verify(original, proof)
        construction = Assembly(original, proof)
        construction.formal_check()
        cases.append(construction.framed_size())

    path = Path(__file__).resolve().parents[1] / "er-unfolding" / "check_literal_substitution.py"
    spec = importlib.util.spec_from_file_location("used_extensions", path)
    used = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(used)
    for a, b in itertools.product((1, -1, 2, -2), repeat=2):
        proof = [{"kind": "input", "source": i + 1, "clause": clause(c)}
                 for i, c in enumerate(used.ORIGINAL)]
        for z, first, second in ((3, a, b), (4, 3, -a)):
            for part, raw in enumerate(((-z, first), (-z, second), (z, -first, -second)), 1):
                proof.append({"kind": "ext", "z": z, "a": first, "b": second,
                              "part": part, "clause": clause(raw)})
        proof.append({"kind": "res", "left": 1, "right": 3, "pivot": 1, "clause": (-2,)})
        proof.append({"kind": "res", "left": 2, "right": 10, "pivot": 2, "clause": ()})
        verify(used.ORIGINAL, proof)
        construction = Assembly(used.ORIGINAL, proof)
        construction.formal_check()
        cases.append(construction.framed_size())
    structural = []
    for m in (2, 3, 4, 5, 8, 16, 32, 64, 128):
        proof, _ = used.make_proof(m)
        verify(used.ORIGINAL, proof)
        construction = Assembly(used.ORIGINAL, proof)
        if m <= 8:
            construction.formal_check()
            cases.append(construction.framed_size())
        sizes, _ = used.unfolded_counts(proof, m)
        structural.append({"m": m, "proof_lines": len(proof),
                           "T_bits": 2 + sum(used.binary_cost(proof)),
                           "unfolded_positive_unit": str(sizes[m + 1]),
                           "word_expansion": m <= 8, **construction.framed_size()})

    # Negative controls distinguish formal corrections and ordered coefficients.
    mutations = []
    for mutation, left, right in [("pivot_commutator", (1, 2), (-1, 3)),
                                   ("coefficient_order", (1, 2), (-1, 3)),
                                   ("sorting", (1, 3), (-1, 2)),
                                   ("duplicate", (1, 2), (-1, 2))]:
        original, proof = local_proof(left, right)
        bad = Assembly(original, proof, mutation)
        try:
            bad.formal_check(False)
        except AssertionError:
            mutations.append(mutation)
        else:
            raise AssertionError("Undetected mutation: " + mutation)
    original, proof = local_proof((1, 2), (-1, 3))
    bad = copy.deepcopy(proof)
    bad[-1]["clause"] = (2,)
    try:
        verify(original, bad, False)
    except AssertionError:
        mutations.append("wrong_resolvent")
    else:
        raise AssertionError("Undetected wrong resolvent")
    result = {"scope": "L021 finite formal per-line and complete IPS identities; large cases count sharing only",
              "formal_cases": len(cases), "formal_line_checks": sum(c["proof_lines"] for c in cases),
              "operations": {key: sum(c[key] for c in cases) for key in
                             ("resolution", "weakening", "swaps", "duplicate_deletions")},
              "mutations_detected": mutations, "used_extension_cases": structural}
    Path(__file__).with_name("assembly-results.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
