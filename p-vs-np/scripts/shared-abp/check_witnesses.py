#!/usr/bin/env python3
"""Finite indexing checks for L017; this is not a CF/EF proof verifier."""

from itertools import product
import json
from pathlib import Path
import random


def row_product(row, matrix):
    result = 0
    for u, image in enumerate(matrix):
        if (row >> u) & 1:
            result ^= image
    return result


def row_basis(rows, width):
    pivots = {}
    for original in rows:
        row = original
        assert 0 <= row < 1 << width
        for p in range(width):
            if not ((row >> p) & 1):
                continue
            if p in pivots:
                row ^= pivots[p]
            else:
                pivots[p] = row
                break
    return [pivots[p] for p in sorted(pivots)]


def coordinates(row, basis):
    coefficients = 0
    for j, vector in enumerate(basis):
        pivot_bit = vector & -vector
        if row & pivot_bit:
            row ^= vector
            coefficients ^= 1 << j
    if row:
        raise ValueError("vector outside the purported basis span")
    return coefficients


def witnesses(widths, matrices, source=0):
    bases = [[1 << source]]
    transitions = []
    for i, layer in enumerate(matrices):
        generators = [
            row_product(row, matrix)
            for matrix in layer
            for row in bases[-1]
        ]
        basis = row_basis(generators, widths[i + 1])
        transition = [
            [coordinates(row_product(row, matrix), basis) for row in bases[-1]]
            for matrix in layer
        ]
        bases.append(basis)
        transitions.append(transition)
    return bases, transitions


def check_tables(widths, matrices, bases, transitions, source=0):
    assert bases[0] == [1 << source]
    assert len(bases) == len(widths)
    assert len(transitions) == len(matrices)
    for i, (layer, transition) in enumerate(zip(matrices, transitions)):
        assert len(bases[i + 1]) <= widths[i + 1]
        assert len(transition) == len(layer)
        for matrix, table in zip(layer, transition):
            assert len(matrix) == widths[i]
            assert all(0 <= row < 1 << widths[i + 1] for row in matrix)
            assert len(table) == len(bases[i])
            for row, coefficient in zip(bases[i], table):
                assert 0 <= coefficient < 1 << len(bases[i + 1])
                assert row_product(row, matrix) == row_product(coefficient, bases[i + 1])


def word_coefficients(matrices, variables, source=0, sink=0):
    """Independent exhaustive semantic test, used only for small examples."""
    coefficients = {}
    for word in product(range(variables), repeat=len(matrices)):
        row = 1 << source
        for layer, a in zip(matrices, word):
            row = row_product(row, layer[a])
        coefficients[word] = (row >> sink) & 1
    return coefficients


def evaluate_invariants(matrices, bases, transitions, variables, source=0):
    count = 0
    for assignment in product((0, 1), repeat=variables):
        p = 1 << source
        q = 1
        assert p == row_product(q, bases[0])
        for i, (layer, transition) in enumerate(zip(matrices, transitions)):
            p_next = 0
            q_next = 0
            for a, bit in enumerate(assignment):
                if bit:
                    p_next ^= row_product(p, layer[a])
                    q_next ^= row_product(q, transition[a])
            p, q = p_next, q_next
            assert p == row_product(q, bases[i + 1])
        count += 1
    return count


def examine(name, widths, matrices, variables, source=0, sink=0):
    bases, transitions = witnesses(widths, matrices, source)
    check_tables(widths, matrices, bases, transitions, source)
    coefficients = word_coefficients(matrices, variables, source, sink)
    formal_zero = not any(coefficients.values())
    terminal_zero = not any((row >> sink) & 1 for row in bases[-1])
    assert formal_zero == terminal_zero
    assignments = evaluate_invariants(matrices, bases, transitions, variables, source)
    return {
        "name": name,
        "widths": widths,
        "variables": variables,
        "ranks": [len(basis) for basis in bases],
        "formal_zero": formal_zero,
        "word_checks": len(coefficients),
        "assignment_checks": assignments,
    }


def duplicate_paths(rng, degree, variables, inner_width):
    """Two equal path sums that cancel after merging into the sink."""
    k = inner_width
    widths = [1] + [2 * k] * (degree - 1) + [1]
    matrices = []
    first = []
    for _ in range(variables):
        row = rng.randrange(1 << k)
        first.append([row | (row << k)])
    matrices.append(first)
    for _ in range(degree - 2):
        layer = []
        for _ in range(variables):
            block = [rng.randrange(1 << k) for _ in range(k)]
            layer.append(block + [row << k for row in block])
        matrices.append(layer)
    last = []
    for _ in range(variables):
        column = [rng.randrange(2) for _ in range(k)]
        last.append(column + column)
    matrices.append(last)
    return widths, matrices


def main():
    rng = random.Random(170104)
    cases = [
        examine("xy+xy cancellation", [1, 2, 1], [[[3], [0]], [[0, 0], [1, 1]]], 2),
        examine("empty coefficient spaces", [1, 2, 1], [[[0], [0]], [[1, 0], [1, 1]]], 2),
        examine("xy+yx formally nonzero", [1, 2, 1], [[[1], [2]], [[0, 1], [1, 0]]], 2),
        examine("unused variable and isolated sink", [1, 2], [[[2], [0], [0]]], 3),
        examine("empty alphabet", [1, 2, 1], [[], []], 0),
    ]
    assert cases[0]["formal_zero"] and cases[1]["formal_zero"]
    assert not cases[2]["formal_zero"]

    # This polynomial vanishes on every Boolean assignment but has two words.
    commutator = [[[1], [2]], [[0, 1], [1, 0]]]
    for assignment in product((0, 1), repeat=2):
        p = 1
        for layer in commutator:
            p_next = 0
            for a, bit in enumerate(assignment):
                if bit:
                    p_next ^= row_product(p, layer[a])
            p = p_next
        assert p == 0

    for degree in range(2, 5):
        for variables in range(1, 4):
            for inner_width in range(1, 3):
                widths, matrices = duplicate_paths(rng, degree, variables, inner_width)
                case = examine("paired path cancellation", widths, matrices, variables)
                assert case["formal_zero"]
                cases.append(case)

    for number in range(120):
        degree = rng.randrange(1, 5)
        variables = rng.randrange(1, 4)
        widths = [1] + [rng.randrange(1, 4) for _ in range(degree - 1)] + [1]
        matrices = [
            [[rng.randrange(1 << widths[i + 1]) for _ in range(widths[i])]
             for _ in range(variables)]
            for i in range(degree)
        ]
        cases.append(examine("random example %d" % number, widths, matrices, variables))

    # A false ground transition must be caught independently of evaluations.
    widths = [1, 2, 1]
    matrices = [[[3], [0]], [[0, 0], [1, 1]]]
    bases, transitions = witnesses(widths, matrices)
    transitions[0][0][0] ^= 1
    try:
        check_tables(widths, matrices, bases, transitions)
    except AssertionError:
        corrupted_transition_rejected = True
    else:
        raise AssertionError("corrupted transition was accepted")

    result = {
        "scope": "Finite recurrence/indexing checks; not a CF/EF proof verifier",
        "seed": 170104,
        "cases": len(cases),
        "formal_zero_cases": sum(case["formal_zero"] for case in cases),
        "formal_nonzero_cases": sum(not case["formal_zero"] for case in cases),
        "word_checks": sum(case["word_checks"] for case in cases),
        "assignment_checks": sum(case["assignment_checks"] for case in cases),
        "corrupted_transition_rejected": corrupted_transition_rejected,
        "boolean_zero_formally_nonzero_rejected": True,
        "named_cases": cases[:5],
    }
    output = Path(__file__).with_name("witness-results.json")
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
