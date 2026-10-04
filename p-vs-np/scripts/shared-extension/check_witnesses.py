#!/usr/bin/env python3
"""Finite formal-word and sharing checks for L020; no ER/IPS proof verifier."""

import json
from pathlib import Path
import random


def add_poly(left, right):
    return left ^ right


def mul_poly(left, right):
    result = set()
    for u in left:
        for v in right:
            word = u + v
            if word in result:
                result.remove(word)
            else:
                result.add(word)
    return frozenset(result)


ZERO = frozenset()
ONE = frozenset({()})


class Circuit:
    def __init__(self):
        self.nodes = []
        self.cache = {}
        self.zero = self.node(("c", 0))
        self.one = self.node(("c", 1))

    def node(self, spec):
        if spec not in self.cache:
            self.cache[spec] = len(self.nodes)
            self.nodes.append(spec)
        return self.cache[spec]

    def add(self, a, b):
        return self.node(("+", a, b))

    def mul(self, a, b):
        return self.node(("*", a, b))

    def product(self, values):
        root = self.one
        for value in values:
            root = self.mul(root, value)
        return root

    def expand(self, substitute_axioms):
        """Independent exact expansion into words in original x variables."""
        values = []
        for spec in self.nodes:
            kind = spec[0]
            if kind == "c":
                poly = ONE if spec[1] else ZERO
            elif kind == "x":
                poly = frozenset({(spec[1],)})
            elif kind == "t":
                label = spec[1]
                if not substitute_axioms:
                    poly = ZERO
                elif label[0] == "b":
                    i = label[1]
                    poly = frozenset({(i, i), (i,)})
                else:
                    _, i, j = label
                    assert i < j
                    poly = frozenset({(i, j), (j, i)})
            else:
                a, b = values[spec[1]], values[spec[2]]
                poly = add_poly(a, b) if kind == "+" else mul_poly(a, b)
            values.append(poly)
        return values

    def placeholder_degrees(self):
        """Syntactic upper bound; at most one placeholder per witness monomial."""
        degrees = []
        for spec in self.nodes:
            if spec[0] in ("x", "c"):
                value = 0
            elif spec[0] == "t":
                value = 1
            elif spec[0] == "+":
                value = max(degrees[spec[1]], degrees[spec[2]])
            else:
                value = degrees[spec[1]] + degrees[spec[2]]
            degrees.append(value)
        return degrees


def base_circuit(variables, definitions):
    circuit = Circuit()
    positive = [circuit.node(("x", i)) for i in range(variables)]
    negative = [circuit.add(circuit.one, value) for value in positive]

    def literal(lit):
        i = abs(lit) - 1
        return positive[i] if lit > 0 else negative[i]

    for a, b in definitions:
        assert 1 <= abs(a) <= len(positive)
        assert 1 <= abs(b) <= len(positive)
        value = circuit.mul(literal(a), literal(b))
        positive.append(value)
        negative.append(circuit.add(circuit.one, value))
    return circuit, positive, negative


def witnesses(circuit):
    base = tuple(circuit.nodes)
    count = len(base)
    commutators = {}
    for total in range(2 * count - 1):
        for g in range(max(0, total - count + 1), min(count, total + 1)):
            h = total - g
            left, right = base[g], base[h]
            if g == h or left[0] == "c" or right[0] == "c":
                root = circuit.zero
            elif left[0] == right[0] == "x":
                i, j = sorted((left[1], right[1]))
                root = circuit.node(("t", ("c", i, j)))
            elif left[0] == "+":
                root = circuit.add(commutators[left[1], h], commutators[left[2], h])
            elif left[0] == "*":
                a, b = left[1:]
                root = circuit.add(circuit.mul(a, commutators[b, h]),
                                   circuit.mul(commutators[a, h], b))
            elif right[0] == "+":
                root = circuit.add(commutators[g, right[1]], commutators[g, right[2]])
            else:
                assert left[0] == "x" and right[0] == "*"
                a, b = right[1:]
                root = circuit.add(circuit.mul(commutators[g, a], b),
                                   circuit.mul(a, commutators[g, b]))
            commutators[g, h] = root

    boolean = []
    for g, spec in enumerate(base):
        if spec[0] == "c":
            root = circuit.zero
        elif spec[0] == "x":
            root = circuit.node(("t", ("b", spec[1])))
        elif spec[0] == "+":
            a, b = spec[1:]
            root = circuit.add(circuit.add(boolean[a], boolean[b]), commutators[a, b])
        else:
            a, b = spec[1:]
            correction = circuit.mul(circuit.mul(a, commutators[b, a]), b)
            first = circuit.mul(boolean[a], circuit.mul(b, b))
            second = circuit.mul(a, boolean[b])
            root = circuit.add(circuit.add(correction, first), second)
        boolean.append(root)
    return base, commutators, boolean


def normalize(circuit, clause, root, positive, negative, commutators, boolean):
    clause = list(clause)
    swaps = deletions = 0

    def factor(lit):
        return negative[abs(lit) - 1] if lit > 0 else positive[abs(lit) - 1]

    def key(lit):
        return abs(lit), lit < 0

    for end in reversed(range(1, len(clause))):
        for i in range(end):
            if key(clause[i]) > key(clause[i + 1]):
                left = circuit.product([factor(v) for v in clause[:i]])
                right = circuit.product([factor(v) for v in clause[i + 2:]])
                correction = circuit.mul(circuit.mul(left, commutators[factor(clause[i]),
                                                                       factor(clause[i + 1])]), right)
                root = circuit.add(root, correction)
                clause[i], clause[i + 1] = clause[i + 1], clause[i]
                swaps += 1
    i = 0
    while i + 1 < len(clause):
        if clause[i] == clause[i + 1]:
            left = circuit.product([factor(v) for v in clause[:i]])
            right = circuit.product([factor(v) for v in clause[i + 2:]])
            root = circuit.add(root, circuit.mul(circuit.mul(left, boolean[factor(clause[i])]), right))
            del clause[i + 1]
            deletions += 1
        else:
            i += 1
    target = circuit.product([factor(v) for v in clause])
    return root, target, swaps, deletions


def examine(variables, definitions, general=False):
    circuit, positive, negative = base_circuit(variables, definitions)
    if general:
        a = circuit.add(positive[0], positive[1])
        b = circuit.add(positive[1], positive[2])
        circuit.mul(a, b)
    base, commutators, boolean = witnesses(circuit)
    clauses = []
    counts = {"swaps": 0, "duplicate_deletions": 0}
    for i, (a, b) in enumerate(definitions, variables):
        z = i + 1
        av = positive[abs(a) - 1] if a > 0 else negative[abs(a) - 1]
        bv = positive[abs(b) - 1] if b > 0 else negative[abs(b) - 1]
        first = circuit.add(circuit.mul(boolean[av], bv), circuit.mul(av, commutators[bv, av]))
        second = circuit.mul(av, boolean[bv])
        third = boolean[positive[i]]
        for clause, root in (([-z, a], first), ([-z, b], second), ([z, -a, -b], third)):
            raw = circuit.product([negative[abs(v) - 1] if v > 0 else positive[abs(v) - 1]
                                   for v in clause])
            normalized, target, swaps, deletions = normalize(
                circuit, clause, root, positive, negative, commutators, boolean)
            clauses.append((root, raw, normalized, target))
            counts["swaps"] += swaps
            counts["duplicate_deletions"] += deletions

    full, zero = circuit.expand(True), circuit.expand(False)
    degrees = circuit.placeholder_degrees()
    for (g, h), root in commutators.items():
        expected = add_poly(mul_poly(full[g], full[h]), mul_poly(full[h], full[g]))
        assert full[root] == expected
        assert zero[root] == ZERO and degrees[root] <= 1
    for g, root in enumerate(boolean):
        assert full[root] == add_poly(mul_poly(full[g], full[g]), full[g])
        assert zero[root] == ZERO and degrees[root] <= 1
    for root, raw, normalized, target in clauses:
        assert full[root] == full[raw]
        assert full[normalized] == full[target]
        assert zero[root] == zero[normalized] == ZERO
        assert degrees[root] <= 1 and degrees[normalized] <= 1
    assert all(spec[0] in ("c", "x", "t", "+", "*") for spec in circuit.nodes)
    return {"base_gates": len(base), "gate_pairs": len(commutators),
            "boolean_witnesses": len(boolean), "defining_clauses": len(clauses), **counts}


def mutation_checks():
    circuit, p, n = base_circuit(3, [(1, 2)])
    _, k, b = witnesses(circuit)
    x, y, z = p[:3]
    xy = p[3]
    bad_boolean = circuit.add(circuit.mul(b[x], circuit.mul(y, y)), circuit.mul(x, b[y]))
    bad_commutator = circuit.add(circuit.mul(k[y, z], x), circuit.mul(k[x, z], y))
    first = circuit.add(circuit.mul(b[x], y), circuit.mul(x, k[y, x]))
    sorted_projection = circuit.mul(n[0], xy)
    values = circuit.expand(True)
    assert values[bad_boolean] != add_poly(mul_poly(values[xy], values[xy]), values[xy])
    assert values[bad_commutator] != add_poly(mul_poly(values[xy], values[z]), mul_poly(values[z], values[xy]))
    assert values[first] != values[sorted_projection]

    duplicate, p, n = base_circuit(1, [(1, 1)])
    _, _, b = witnesses(duplicate)
    normalized = duplicate.mul(p[0], n[1])
    values = duplicate.expand(True)
    assert values[b[p[1]]] != values[normalized]
    return ["product Booleanity without commutator correction",
            "commutator product with reversed coefficient order",
            "sorted projection without swap correction",
            "duplicate defining literal without Booleanity correction"]


def number_bits(value):
    return 2 * (value + 1).bit_length() - 1


def structural_case(extensions):
    definitions = [(i + 1, i + 1) for i in range(extensions)]
    circuit, positive, _ = base_circuit(1, definitions)
    base, k, b = witnesses(circuit)
    syntactic_degree = []
    unfolded = []
    for spec in base:
        if spec[0] == "c":
            degree, tree = 0, 1
        elif spec[0] == "x":
            degree, tree = 1, 1
        else:
            a, d = spec[1:]
            degree = (max(syntactic_degree[a], syntactic_degree[d]) if spec[0] == "+"
                      else syntactic_degree[a] + syntactic_degree[d])
            tree = 1 + unfolded[a] + unfolded[d]
        syntactic_degree.append(degree)
        unfolded.append(tree)
    assert syntactic_degree[positive[-1]] == 2 ** extensions
    assert unfolded[positive[-1]] == 2 ** (extensions + 1) - 1
    assert len(k) == len(base) ** 2
    assert len(circuit.nodes) <= 3 * len(base) ** 2 + 12 * len(base) + 2
    assert max(circuit.placeholder_degrees()) <= 1
    labels = {spec[1] for spec in circuit.nodes if spec[0] == "t"}
    dense = {label: i for i, label in enumerate(sorted(labels))}
    # Structural diagnostic: gate-record/output-reference payload only.
    # The lemma separately charges full framing, rooted outputs and axioms.
    bits = 0
    for spec in circuit.nodes:
        bits += 3
        if spec[0] == "x":
            # Charge a sparse original identifier rather than its dense index.
            bits += number_bits(2 ** 257 + 5)
        elif spec[0] == "t":
            bits += number_bits(dense[spec[1]])
        elif spec[0] in ("+", "*"):
            bits += number_bits(spec[1]) + number_bits(spec[2])
        else:
            bits += 1
    bits += sum(number_bits(root) for root in list(k.values()) + b)
    return {"extensions": extensions, "base_gates": len(base),
            "gate_pair_states": len(k), "shared_nodes": len(circuit.nodes),
            "shared_binary_bits": bits, "root_syntactic_degree": str(syntactic_degree[positive[-1]]),
            "root_unfolded_nodes": str(unfolded[positive[-1]]), "word_expansion": False}


def main():
    cases = [examine(0, []), examine(3, [], general=True)]
    for a in (1, -1, 2, -2):
        for b in (1, -1, 2, -2):
            cases.append(examine(2, [(a, b), (3, -a)]))
    cases.append(examine(1, [(1, 1), (-2, 2), (-3, -3)]))
    rng = random.Random(20261004)
    for _ in range(48):
        definitions = []
        for i in range(3):
            literals = [sign * (j + 1) for j in range(3 + i) for sign in (1, -1)]
            definitions.append((rng.choice(literals), rng.choice(literals)))
        cases.append(examine(3, definitions))
    result = {"scope": "L020 witness recurrences and normalization; not assembled IPS identities or proof strings",
              "formal_cases": len(cases),
              "checks": {key: sum(case[key] for case in cases) for key in
                         ("gate_pairs", "boolean_witnesses", "defining_clauses", "swaps", "duplicate_deletions")},
              "mutations_detected": mutation_checks(),
              "structural_cases": [structural_case(m) for m in (4, 8, 16, 32, 64, 128)]}
    path = Path(__file__).with_name("witness-results.json")
    path.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
