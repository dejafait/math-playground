"""Check a used-extension ER family and the cost of literal tree substitution.

This checks syntactic ER inferences, not Frege/IPS translation proof strings.
The binary encoding is a fixed 2-bit record kind, Elias-gamma positive
integers, signed literals, explicit clauses, and explicit inference data.
Gamma(len+1) prefixes each clause and the original/proof record lists.
"""

import copy
import json
from pathlib import Path


ORIGINAL = ((1,), (2,), (-1, -2))


def clause(literals):
    return tuple(sorted(set(literals), key=lambda x: (abs(x), x < 0)))


def resolve(left, right, pivot):
    assert pivot > 0 and pivot in left and -pivot in right
    return clause((set(left) - {pivot}) | (set(right) - {-pivot}))


def make_proof(m):
    assert m >= 2
    proof = []

    def add(record):
        record["clause"] = clause(record["clause"])
        proof.append(record)
        return len(proof)

    def res(left, right, pivot):
        return add({"kind": "res", "left": left, "right": right,
                    "pivot": pivot,
                    "clause": resolve(proof[left - 1]["clause"],
                                      proof[right - 1]["clause"], pivot)})

    units = {}
    for source, initial in enumerate(ORIGINAL, 1):
        line = add({"kind": "input", "source": source, "clause": initial})
        if source <= 2:
            units[source] = line
    projections = {}
    for i in range(2, m + 1):
        z, a, b = i + 1, i, i - 1
        defining = ((-z, a), (-z, b), (z, -a, -b))
        ids = []
        for part, defining_clause in enumerate(defining, 1):
            ids.append(add({"kind": "ext", "z": z, "a": a, "b": b,
                            "part": part, "clause": defining_clause}))
        projections[z] = ids[:2]
        intermediate = res(units[a], ids[2], a)
        units[z] = res(units[b], intermediate, b)
    intermediate = res(projections[3][0], 3, 2)
    negative = res(projections[3][1], intermediate, 1)
    for z in range(4, m + 2):
        negative = res(projections[z][0], negative, z - 1)
    res(units[m + 1], negative, m + 1)
    return proof, units[m + 1]


def verify(proof):
    known = {1, 2}
    pending = None
    for number, record in enumerate(proof, 1):
        c = record["clause"]
        assert c == clause(c)
        if record["kind"] == "ext":
            z, a, b, part = (record[k] for k in ("z", "a", "b", "part"))
            if part == 1:
                assert pending is None and z > 0 and z not in known
                assert abs(a) in known and abs(b) in known
                pending = (z, a, b, 1)
            else:
                assert pending == (z, a, b, part - 1)
                pending = (z, a, b, part)
            expected = ((-z, a), (-z, b), (z, -a, -b))
            assert c == clause(expected[part - 1])
            if part == 3:
                known.add(z)
                pending = None
        else:
            assert pending is None
            assert all(abs(literal) in known for literal in c)
            if record["kind"] == "input":
                assert 1 <= record["source"] <= len(ORIGINAL)
                assert c == clause(ORIGINAL[record["source"] - 1])
            else:
                assert record["kind"] == "res"
                left, right, pivot = (record[k] for k in ("left", "right", "pivot"))
                assert 1 <= left < number and 1 <= right < number
                assert c == resolve(proof[left - 1]["clause"],
                                    proof[right - 1]["clause"], pivot)
    assert pending is None and proof[-1]["clause"] == ()


def ancestors(proof):
    used = set()
    stack = [len(proof)]
    while stack:
        number = stack.pop()
        if number in used:
            continue
        used.add(number)
        record = proof[number - 1]
        if record["kind"] == "res":
            stack.extend((record["left"], record["right"]))
    return used


def gamma(n):
    assert n >= 1
    bits = format(n, "b")
    return "0" * (len(bits) - 1) + bits


def literal_bits(literal):
    return str(int(literal < 0)) + gamma(abs(literal))


def clause_bits(c):
    return gamma(len(c) + 1) + "".join(literal_bits(literal) for literal in c)


def binary_cost(proof):
    original = gamma(len(ORIGINAL) + 1) + "".join(clause_bits(c) for c in ORIGINAL)
    records = []
    for record in proof:
        kind = record["kind"]
        if kind == "input":
            prefix = "00" + gamma(record["source"])
        elif kind == "ext":
            prefix = ("01" + gamma(record["z"]) + literal_bits(record["a"])
                      + literal_bits(record["b"]) + gamma(record["part"]))
        else:
            prefix = ("10" + gamma(record["left"]) + gamma(record["right"])
                      + gamma(record["pivot"]))
        records.append(prefix + clause_bits(record["clause"]))
    encoded = gamma(len(proof) + 1) + "".join(records)
    return len(original), len(encoded)


def unfolded_counts(proof, m):
    sizes = {1: 1, 2: 1}
    for z in range(3, m + 2):
        sizes[z] = 1 + sizes[z - 1] + sizes[z - 2]

    def size(c):
        if not c:
            return 1  # False constant.
        return len(c) - 1 + sum(sizes[abs(v)] + (v < 0) for v in c)

    counts = [size(record["clause"]) for record in proof]
    return sizes, counts


def expand_variable(v):
    if v <= 2:
        return ("var", v)
    # Recursive copies are made separately; this is deliberately not memoized.
    return ("and", expand_variable(v - 1), expand_variable(v - 2))


def expand_clause(c):
    if not c:
        return ("false",)
    trees = []
    for literal in c:
        tree = expand_variable(abs(literal))
        trees.append(("not", tree) if literal < 0 else tree)
    result = trees[-1]
    for tree in reversed(trees[:-1]):
        result = ("or", tree, result)
    return result


def count_tree(tree):
    return 1 + sum(count_tree(child) for child in tree[1:] if isinstance(child, tuple))


def evaluate(tree, assignment):
    kind = tree[0]
    if kind == "var":
        assert tree[1] in (1, 2)  # Every extension label was eliminated.
        return assignment[tree[1]]
    if kind == "false":
        return False
    if kind == "not":
        return not evaluate(tree[1], assignment)
    left, right = evaluate(tree[1], assignment), evaluate(tree[2], assignment)
    return left and right if kind == "and" else left or right


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def main():
    rows = []
    checked_expanded_clauses = 0
    for m in (2, 3, 4, 5, 8, 12, 16, 32, 64, 128):
        proof, final_positive = make_proof(m)
        verify(proof)
        assert len(proof) == 6 * m - 1
        used = ancestors(proof)
        used_extensions = {proof[i - 1]["z"] for i in used
                           if proof[i - 1]["kind"] == "ext"}
        assert used_extensions == set(range(3, m + 2))
        assert {proof[i - 1]["source"] for i in used
                if proof[i - 1]["kind"] == "input"} == {1, 2, 3}
        assert final_positive in used
        sizes, counts = unfolded_counts(proof, m)
        assert sizes[m + 1] == 2 * fibonacci(m + 1) - 1
        assert sizes[m + 1] >= 2 ** (m // 2)
        if m <= 12:
            trees = [expand_clause(record["clause"]) for record in proof]
            assert [count_tree(tree) for tree in trees] == counts
            checked_expanded_clauses += len(trees)
            for x in (False, True):
                for y in (False, True):
                    values = [evaluate(tree, {1: x, 2: y}) for tree in trees]
                    for record, value in zip(proof, values):
                        if record["kind"] == "ext":
                            assert value
                        elif record["kind"] == "res":
                            both = values[record["left"] - 1] and values[record["right"] - 1]
                            assert not both or value
        original_bits, proof_bits = binary_cost(proof)
        rows.append({"m": m, "clauses": len(proof), "original_bits": original_bits,
                     "proof_bits": proof_bits, "T_bits": 2 + original_bits + proof_bits,
                     "last_positive_unit_nodes": sizes[m + 1],
                     "all_unfolded_clause_nodes_U": sum(counts),
                     "ancestor_unfolded_clause_nodes": sum(counts[i - 1] for i in used),
                     "all_extensions_used": True})

    # Discriminating checks: the verifier must reject a wrong inference and
    # an attempted extension using an original variable as its fresh name.
    proof, _ = make_proof(4)
    bad_resolution = copy.deepcopy(proof)
    next(record for record in bad_resolution if record["kind"] == "res")["clause"] = (1,)
    bad_freshness = copy.deepcopy(proof)
    next(record for record in bad_freshness if record["kind"] == "ext")["z"] = 1
    rejected = 0
    for bad in (bad_resolution, bad_freshness):
        try:
            verify(bad)
        except AssertionError:
            rejected += 1
    assert rejected == 2

    result = {"scope": "literal extension substitution only; no IPS lower bound",
              "valid_ER_families_checked": len(rows),
              "independently_expanded_clauses_checked": checked_expanded_clauses,
              "rejected_corruptions": rejected, "cases": rows}
    output = Path(__file__).with_name("literal-substitution-results.json")
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
