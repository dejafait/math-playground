#!/usr/bin/env python3
"""Exact finite checks of the L018 encoding; not a CF/EF/ER verifier."""

from itertools import product
import json
from pathlib import Path
import random

from check_witnesses import check_tables, evaluate_invariants, row_product, witnesses


def xor_polynomials(left, right):
    result = set(left)
    result.symmetric_difference_update(right)
    return result


def polynomial(tree):
    kind = tree[0]
    if kind == "c":
        return {()} if tree[1] else set()
    if kind == "x":
        return {(tree[1],)}
    left, right = polynomial(tree[1]), polynomial(tree[2])
    if kind == "+":
        return xor_polynomials(left, right)
    assert kind == "*"
    result = set()
    for u in left:
        for v in right:
            word = u + v
            if word in result:
                result.remove(word)
            else:
                result.add(word)
    return result


def evaluate(tree, assignment):
    kind = tree[0]
    if kind == "c":
        return tree[1]
    if kind == "x":
        return assignment[tree[1]]
    left, right = evaluate(tree[1], assignment), evaluate(tree[2], assignment)
    return left ^ right if kind == "+" else left & right


def substitute(tree, axioms):
    if tree[0] == "y":
        return axioms[tree[1]]
    if tree[0] in ("c", "x"):
        return tree
    return (tree[0], substitute(tree[1], axioms), substitute(tree[2], axioms))


def formula_graph(tree):
    edges = []
    vertices = 0

    def fresh():
        nonlocal vertices
        vertex = vertices
        vertices += 1
        return vertex

    def build(node):
        source = fresh()
        if node[0] in ("c", "x"):
            sink = fresh()
            edges.append((source, sink, node))
            return source, sink
        ls, lt = build(node[1])
        rs, rt = build(node[2])
        sink = fresh()
        if node[0] == "+":
            connectors = [(source, ls), (source, rs), (lt, sink), (rt, sink)]
        else:
            assert node[0] == "*"
            connectors = [(source, ls), (lt, rs), (rt, sink)]
        edges.extend((u, v, ("c", 1)) for u, v in connectors)
        return source, sink

    source, sink = build(tree)
    assert source == 0 and sink == vertices - 1
    assert all(u < v for u, v, _ in edges)
    return vertices, edges, source, sink


def component_tables(vertices, edges, variables):
    constants = [0] * vertices
    variable = [[0] * vertices for _ in range(variables)]
    for u, v, label in edges:
        if label[0] == "c":
            if label[1]:
                constants[u] ^= 1 << v
        else:
            variable[label[1]][u] ^= 1 << v

    # Reverse triangular substitution computes all constant-path coefficients.
    closure = [0] * vertices
    for u in reversed(range(vertices)):
        closure[u] = 1 << u
        for v in range(u + 1, vertices):
            if (constants[u] >> v) & 1:
                closure[u] ^= closure[v]

    for u in range(vertices):
        assert row_product(closure[u], constants) == closure[u] ^ (1 << u)
        assert row_product(constants[u], closure) == closure[u] ^ (1 << u)
        assert closure[u] & ((1 << u) - 1) == 0
    step = [[row_product(row, closure) for row in matrix] for matrix in variable]
    first = [[row_product(closure[0], matrix)] for matrix in step]
    for matrix in step:
        assert all(row & ((1 << (u + 1)) - 1) == 0 for u, row in enumerate(matrix))
    return constants, variable, closure, step, first


def graph_polynomial(vertices, edges):
    values = [set() for _ in range(vertices)]
    values[0] = {()}
    for u in range(vertices):
        for source, v, label in edges:
            if source != u:
                continue
            if label[0] == "c":
                term = values[u] if label[1] else set()
            else:
                term = {word + (label[1],) for word in values[u]}
            values[v] = xor_polynomials(values[v], term)
    return values[-1]


def examine(name, tree, variables):
    vertices, edges, source, sink = formula_graph(tree)
    constants, variable, closure, step, first = component_tables(vertices, edges, variables)
    expected = polynomial(tree)
    assert graph_polynomial(vertices, edges) == expected
    degree = vertices - 1
    layers = [first] + [step] * (degree - 1)
    widths = [1] + [vertices] * degree
    bases, transitions = witnesses(widths, layers)
    check_tables(widths, layers, bases, transitions)

    # Independent word enumeration is confined to these finite examples.
    coefficient_rows = {(): closure[source]}
    components = [{()} if (closure[source] >> sink) & 1 else set()]
    row_checks = 1
    for k in range(1, degree + 1):
        next_rows = {}
        for word, row in coefficient_rows.items():
            for a, matrix in enumerate(step):
                image = row_product(row, matrix)
                if image:
                    key = word + (a,)
                    next_rows[key] = next_rows.get(key, 0) ^ image
        coefficient_rows = {word: row for word, row in next_rows.items() if row}
        component = {word for word, row in coefficient_rows.items() if (row >> sink) & 1}
        assert component == {word for word in expected if len(word) == k}
        terminal_zero = not any((row >> sink) & 1 for row in bases[k])
        assert terminal_zero == (not component)
        assert all(row & ((1 << k) - 1) == 0 for row in coefficient_rows.values())
        row_checks += len(coefficient_rows)
        components.append(component)
    assert components[0] == {word for word in expected if len(word) == 0}
    assert all(row_product(row, matrix) == 0
               for row in coefficient_rows.values() for matrix in step)

    boolean_values = []
    for assignment in product((0, 1), repeat=variables):
        graph = 1
        for u in range(vertices):
            if not ((graph >> u) & 1):
                continue
            graph ^= constants[u]
            for a, bit in enumerate(assignment):
                if bit:
                    graph ^= variable[a][u]

        h = closure[source]
        total = h
        first_value = 0
        for a, bit in enumerate(assignment):
            if bit:
                first_value ^= first[a][0]
        for k in range(1, degree + 1):
            h_next = 0
            for a, bit in enumerate(assignment):
                if bit:
                    h_next ^= row_product(h, step[a])
            h = h_next
            if k == 1:
                assert h == first_value
            assert h & ((1 << k) - 1) == 0
            component_value = sum(
                all(assignment[a] for a in word) for word in components[k]
            ) % 2
            assert (h >> sink) & 1 == component_value
            total ^= h
        assert all(row_product(h, matrix) == 0 for matrix in step)
        assert total == graph
        value = (graph >> sink) & 1
        assert value == evaluate(tree, assignment)
        boolean_values.append(value)
    invariant_assignments = evaluate_invariants(layers, bases, transitions, variables)
    assert invariant_assignments == len(boolean_values)
    return {
        "name": name,
        "vertices": vertices,
        "positive_degree_components": degree,
        "formal_zero": not expected,
        "boolean_zero": not any(boolean_values),
        "coefficient_row_checks": row_checks,
        "assignment_checks": len(boolean_values),
    }


def random_tree(rng, depth, variables):
    if depth == 0 or rng.random() < 0.3:
        return ("c", rng.randrange(2)) if rng.random() < 0.4 else ("x", rng.randrange(variables))
    return (rng.choice(("+", "*")), random_tree(rng, depth - 1, variables),
            random_tree(rng, depth - 1, variables))


def balanced_product(items):
    if len(items) == 1:
        return items[0]
    middle = len(items) // 2
    return ("*", balanced_product(items[:middle]), balanced_product(items[middle:]))


def ips_examples():
    x, z = ("x", 0), ("x", 1)
    one = ("c", 1)
    nx, nz = ("+", one, x), ("+", one, z)
    base = ("+", ("+", ("y", 0), ("y", 1)), ("+", ("y", 2), ("y", 3)))
    term = balanced_product([x, ("y", 0), z, ("y", 1)])
    augmented = ("+", base, ("+", term, term))
    return [
        ("opposing units", 1, [nx, x, ("+", ("*", x, x), x)],
         ("+", ("y", 0), ("y", 1))),
        ("four two-variable clauses with degree-four cancellation", 2,
         [("*", nx, nz), ("*", nx, z), ("*", x, nz), ("*", x, z),
          ("+", ("*", x, x), x), ("+", ("*", z, z), z),
          ("+", ("*", x, z), ("*", z, x))],
         augmented),
    ]


def main():
    rng = random.Random(180104)
    x, z, one = ("x", 0), ("x", 1), ("c", 1)
    long_word = balanced_product([x] * 32)
    cases = [
        examine("constant zero", ("c", 0), 0),
        examine("constant one", one, 0),
        examine("constant cancellation", ("+", one, one), 0),
        examine("constant paths before and after a variable", ("*", ("+", x, one), one), 1),
        examine("mixed degrees", ("+", ("*", x, z), ("+", x, one)), 2),
        examine("Boolean-zero commutator is formally nonzero", ("+", ("*", x, z), ("*", z, x)), 2),
        examine("Boolean-zero Boolean axiom is formally nonzero", ("+", ("*", x, x), x), 1),
        examine("balanced degree-32 formal cancellation", ("+", long_word, long_word), 1),
    ]
    for i in range(40):
        cases.append(examine("random tree %d" % i, random_tree(rng, 3, 2), 2))
    for i in range(12):
        term = random_tree(rng, 2, 2)
        case = examine("paired formal cancellation %d" % i, ("+", term, term), 2)
        assert case["formal_zero"]
        cases.append(case)

    ips_checks = 0
    for name, variables, axioms, certificate in ips_examples():
        f0 = substitute(certificate, [("c", 0)] * len(axioms))
        fa = substitute(certificate, axioms)
        f1 = ("+", fa, one)
        assert not polynomial(f0) and not polynomial(f1)
        cases.append(examine(name + ": C(x,0)", f0, variables))
        cases.append(examine(name + ": C(x,A)+1", f1, variables))
        for assignment in product((0, 1), repeat=variables):
            assert evaluate(f0, assignment) == 0
            assert evaluate(fa, assignment) == 1
            ips_checks += 1

    # Omitting trailing constant paths must be detected by an ordinary example.
    vertices, edges, _, sink = formula_graph(("+", x, one))
    _, variable, closure, _, first = component_tables(vertices, edges, 1)
    wrong_first = row_product(closure[0], variable[0])
    assert (wrong_first >> sink) & 1 != (first[0][0] >> sink) & 1
    damaged_closure = closure[:]
    damaged_closure[0] ^= 1 << sink
    constants, _, _, _, _ = component_tables(vertices, edges, 1)
    assert row_product(damaged_closure[0], constants) != damaged_closure[0] ^ 1

    result = {
        "scope": "Exact finite encoding and identity checks; not a propositional proof verifier",
        "seed": 180104,
        "cases": len(cases),
        "formal_zero_cases": sum(case["formal_zero"] for case in cases),
        "components_checked": sum(case["positive_degree_components"] + 1 for case in cases),
        "coefficient_row_checks": sum(case["coefficient_row_checks"] for case in cases),
        "assignment_checks": sum(case["assignment_checks"] for case in cases),
        "ips_identity_assignment_checks": ips_checks,
        "omitted_trailing_closure_detected": True,
        "corrupted_constant_closure_detected": True,
        "boolean_only_zero_not_accepted_as_formal_zero": True,
        "named_cases": cases[:8],
    }
    Path(__file__).with_name("formula-assembly-results.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
