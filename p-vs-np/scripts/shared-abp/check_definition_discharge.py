#!/usr/bin/env python3
"""Audit gate substitution syntax and sharing; not a CF/EF/ER verifier."""

from itertools import product
import json
from pathlib import Path


class Dag:
    def __init__(self):
        self.nodes = []
        self.intern = {}

    def node(self, operation, *arguments):
        # Hash-cons equal syntax, without any Boolean simplification.
        key = (operation, *arguments)
        if key not in self.intern:
            self.intern[key] = len(self.nodes)
            self.nodes.append(key)
        return self.intern[key]

    def xor(self, terms):
        terms = list(terms)
        if not terms:
            return self.node("c", 0)
        result = terms[0]
        for term in terms[1:]:
            result = self.node("xor", result, term)
        return result

    def reachable(self, root):
        seen, pending = set(), [root]
        while pending:
            vertex = pending.pop()
            if vertex in seen:
                continue
            seen.add(vertex)
            operation, *arguments = self.nodes[vertex]
            if operation in ("and", "xor"):
                pending.extend(arguments)
        return seen

    def values(self, assignment):
        result = []
        for operation, *arguments in self.nodes:
            if operation == "c":
                value = arguments[0]
            elif operation == "x":
                value = assignment[arguments[0]]
            elif operation == "and":
                value = result[arguments[0]] & result[arguments[1]]
            else:
                assert operation == "xor"
                value = result[arguments[0]] ^ result[arguments[1]]
            result.append(value)
        return result


def instantiate(dag, operation, arguments, substitutions, labels):
    if operation == "c":
        return dag.node("c", arguments[0])
    inputs = [substitutions[value] if kind == "g" else dag.node("x", labels[value])
              for kind, value in arguments]
    return dag.node(operation, *inputs)


def flat_evaluator(dag, widths, layers, labels):
    definitions, substitutions, outputs = [], [], []

    def emit(operation, *arguments):
        gate = len(definitions)
        if operation != "c":
            assert all(kind != "g" or 0 <= value < gate for kind, value in arguments)
        definitions.append((operation, arguments))
        substitutions.append(instantiate(dag, operation, arguments, substitutions, labels))
        return ("g", gate)

    zero, one = emit("c", 0), emit("c", 1)
    previous = [one] + [zero] * (widths[0] - 1)
    for i, layer in enumerate(layers):
        current = []
        for v in range(widths[i + 1]):
            terms = [emit("and", previous[u], ("x", a))
                     for a, matrix in enumerate(layer)
                     for u, row in enumerate(matrix) if (row >> v) & 1]
            value = terms[0] if terms else zero
            for term in terms[1:]:
                value = emit("xor", value, term)
            current.append(value)
        outputs.append([value for _, value in current])
        previous = current
    return definitions, substitutions, outputs


def factored_evaluator(dag, widths, layers, labels):
    assert widths[0] == 1
    previous = [dag.node("c", 1)]
    outputs = []
    for i, layer in enumerate(layers):
        current = []
        for v in range(widths[i + 1]):
            terms = []
            for a, matrix in enumerate(layer):
                selected = [previous[u] for u, row in enumerate(matrix) if (row >> v) & 1]
                if selected:
                    variable = dag.node("x", labels[a])
                    # L018's first row omits the scalar-1 AND gates.
                    term = variable if i == 0 else dag.node("and", dag.xor(selected), variable)
                    terms.append(term)
            current.append(dag.xor(terms))
        outputs.append(current)
        previous = current
    return outputs


def nonreflexive_definitions(dag, definitions, substitutions, labels):
    return sum(substitutions[j] != instantiate(dag, op, args, substitutions, labels)
               for j, (op, args) in enumerate(definitions))


def examine(name, widths, layers, labels):
    assert len(widths) == len(layers) + 1
    assert all(len(layer) == len(labels) for layer in layers)
    for i, layer in enumerate(layers):
        assert all(len(matrix) == widths[i] for matrix in layer)
        assert all(0 <= row < 1 << widths[i + 1] for matrix in layer for row in matrix)

    dag = Dag()
    definitions, flat, gate_outputs = flat_evaluator(dag, widths, layers, labels)
    factored = factored_evaluator(dag, widths, layers, labels)
    assert nonreflexive_definitions(dag, definitions, flat, labels) == 0

    # This models directly substituting factored output circuits into definitions
    # whose right sides were built using the flat recurrence. The test rejects
    # reflexivity as a justification; it does NOT assert semantic inequivalence.
    mixed = list(flat)
    for gates, roots in zip(gate_outputs, factored):
        for gate, root in zip(gates, roots):
            if definitions[gate][0] != "c":
                mixed[gate] = root
    missing_reflexivity = nonreflexive_definitions(dag, definitions, mixed, labels)

    assignments = 0
    for bits in product((0, 1), repeat=len(labels)):
        values = dag.values(dict(zip(labels, bits)))
        for gates, roots in zip(gate_outputs, factored):
            assert [values[flat[g]] for g in gates] == [values[root] for root in roots]
        assignments += 1

    # A wrong first AND definition cannot pass the repaired syntax check.
    damaged = list(definitions)
    first_and = next((j for j, (op, _) in enumerate(damaged) if op == "and"), None)
    mutation_rejected = None
    if first_and is not None:
        damaged[first_and] = ("xor", damaged[first_and][1])
        mutation_rejected = nonreflexive_definitions(dag, damaged, flat, labels) > 0
        assert mutation_rejected

    # Charge each rooted substitution circuit in full, while keeping its DAG.
    node_bits = max(1, len(dag.nodes).bit_length())
    label_bits = max([1] + [label.bit_length() for label in labels])
    # A conservative padded record charge includes opcodes, node identifiers,
    # two input references, sparse input names, and a header/root record.
    record_bits = 8 + 4 * node_bits + 2 * label_bits
    root_nodes = root_bits = 0
    for root in flat:
        reachable = dag.reachable(root)
        root_nodes += len(reachable)
        root_bits += (len(reachable) + 1) * record_bits
        for vertex in reachable:
            op, *args = dag.nodes[vertex]
            if op == "x":
                assert args[0] in labels
    assert root_nodes <= len(flat) * len(dag.nodes)
    unfolded = []
    for op, *args in dag.nodes:
        unfolded.append(1 if op in ("c", "x") else 1 + sum(unfolded[v] for v in args))
    return {
        "name": name,
        "evaluation_definitions": len(definitions),
        "dag_nodes": len(dag.nodes),
        "full_rooted_substitution_nodes": root_nodes,
        "full_rooted_substitution_bits_upper_charge": root_bits,
        "largest_unfolded_root_nodes": max(unfolded[root] for root in flat),
        "factored_substitution_nonreflexive_definitions": missing_reflexivity,
        "assignment_checks": assignments,
        "mutated_definition_rejected": mutation_rejected,
        "remaining_input_labels": len(labels),
    }


def main():
    dense_degree, dense_width = 12, 8
    dense_widths = [1] + [dense_width] * (dense_degree - 1) + [1]
    dense_layers = [
        [[(1 << dense_widths[i + 1]) - 1] * dense_widths[i] for _ in range(2)]
        for i in range(dense_degree)
    ]
    cases = [
        examine("empty alphabet", [1, 3, 2, 1], [[], [], []], []),
        examine("scalar-one first layer", [1, 1], [[[1]]], [1 << 257]),
        examine("duplicate paths with zero terminal", [1, 2, 1],
                [[[3], [0]], [[0, 0], [1, 1]]], [0, 1]),
        examine("Boolean-zero formal commutator", [1, 2, 1],
                [[[1], [2]], [[0, 1], [1, 0]]], [0, 1]),
        examine("grouped nonzero row", [1, 3, 2],
                [[[7], [3]], [[3, 1, 2], [1, 3, 2]]], [0, 1]),
        examine("dense sharing stress with sparse labels", dense_widths, dense_layers,
                [(1 << 80) + 1, 1 << 257]),
    ]
    assert cases[1]["factored_substitution_nonreflexive_definitions"] > 0
    assert cases[4]["factored_substitution_nonreflexive_definitions"] > 0
    assert cases[-1]["largest_unfolded_root_nodes"] > 10**12
    result = {
        "scope": "Syntax/finite evaluation and shared description charges; not a propositional proof verifier",
        "cases": len(cases),
        "flat_substitution_all_definitions_reflexive": True,
        "flat_and_factored_outputs_equal_on_checked_assignments": True,
        "factored_substitution_requires_explicit_equality_proofs": True,
        "case_details": cases,
    }
    Path(__file__).with_name("definition-discharge-results.json").write_text(
        json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
