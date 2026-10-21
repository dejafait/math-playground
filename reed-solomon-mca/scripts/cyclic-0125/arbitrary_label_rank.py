"""Bounded exact falsification search. The complete list defines coverage."""

from collections import Counter
from itertools import combinations, permutations
import json
from pathlib import Path
from random import Random

P = 97
LIMIT = 4096
SEED = 20261005042
H = [x for x in range(1, P) if pow(x, 16, P) == 1]
PAIRS = list(combinations(range(8), 2))
ROW_PAIRS = list(combinations(range(4), 2))
HERE = Path(__file__).resolve().parent


def labelings():
    seen = set()

    def fresh(label, origin):
        label = tuple(label)
        if label not in seen and len(seen) < LIMIT:
            assert sorted(label) == H
            seen.add(label)
            return label, origin
        return None

    generators = [w for w in H if pow(w, 8, P) != 1]
    controls = [[pow(w, t, P) for t in range(16)] for w in generators]
    for w, label in zip(generators, controls):
        item = fresh(label, f"cyclic-generator-{w}")
        if item:
            yield item
    for w, base in zip(generators, controls):
        for i, j in combinations(range(16), 2):
            label = base[:]
            label[i], label[j] = label[j], label[i]
            item = fresh(label, f"single-transposition-{w}-{i}-{j}")
            if item:
                yield item
    for a in range(1, 16, 2):
        for b in range(16):
            item = fresh([pow(8, (a * t + b) % 16, P) for t in range(16)],
                         f"affine-exponent-{a}-{b}")
            if item:
                yield item
    # All bit-position permutations, with every bit-complement mask.
    for order in permutations(range(4)):
        for mask in range(16):
            exponents = [sum(((t >> bit) & 1) << order[bit]
                             for bit in range(4)) ^ mask for t in range(16)]
            item = fresh([pow(8, e, P) for e in exponents], f"bit-order-{order}-{mask}")
            if item:
                yield item
    for order in permutations(range(4)):
        for reverse in (False, True):
            exponents = [4 * block + i for block in order
                         for i in (range(3, -1, -1) if reverse else range(4))]
            item = fresh([pow(8, e, P) for e in exponents], f"block-order-{order}-{reverse}")
            if item:
                yield item
    for shift in range(16):
        for reverse in (False, True):
            base = H[::-1] if reverse else H
            item = fresh(base[shift:] + base[:shift], f"numeric-rotation-{shift}-{reverse}")
            if item:
                yield item
    rng = Random(SEED)
    draw = 0
    while len(seen) < LIMIT:
        label = H[:]
        rng.shuffle(label)
        draw += 1
        item = fresh(label, f"seeded-shuffle-{draw}")
        if item:
            yield item


def support_block(support):
    coefficients = [1]
    for x in support:
        result = [0] * (len(coefficients) + 1)
        for i, a in enumerate(coefficients):
            result[i] = (result[i] - x * a) % P
            result[i + 1] = (result[i + 1] + a) % P
        coefficients = result
    rows = [[0] * r + coefficients + [0] * (3 - r) for r in range(4)]
    matrix = [[(rows[r][j] * rows[s][k] - rows[r][k] * rows[s][j]) % P
               for j, k in PAIRS] for r, s in ROW_PAIRS]
    return {"support": list(support), "annihilator": rows, "matrix": matrix}


def independent_rows(matrix):
    basis = {}
    selected = []
    for i, original in enumerate(matrix):
        row = original[:]
        for pivot in sorted(basis):
            factor = row[pivot]
            if factor:
                row = [(x - factor * y) % P for x, y in zip(row, basis[pivot])]
        pivot = next((j for j, x in enumerate(row) if x), None)
        if pivot is not None:
            inverse = pow(row[pivot], -1, P)
            basis[pivot] = [x * inverse % P for x in row]
            selected.append(i)
        if len(basis) == 28:
            break
    return selected


def determinant(matrix):
    a = [row[:] for row in matrix]
    det = 1
    for j in range(len(a)):
        pivot = next((i for i in range(j, len(a)) if a[i][j]), None)
        if pivot is None:
            return 0
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            det = -det
        value = a[j][j]
        det = det * value % P
        inv = pow(value, -1, P)
        for i in range(j + 1, len(a)):
            factor = a[i][j] * inv % P
            for k in range(j + 1, len(a)):
                a[i][k] = (a[i][k] - factor * a[j][k]) % P
    return det % P


def reduction_and_kernel(matrix):
    a = [row[:] for row in matrix]
    pivots = []
    for col in range(28):
        pivot = next((i for i in range(len(pivots), len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        i = len(pivots)
        a[i], a[pivot] = a[pivot], a[i]
        inverse = pow(a[i][col], -1, P)
        a[i] = [x * inverse % P for x in a[i]]
        for r in range(len(a)):
            if r != i:
                factor = a[r][col]
                a[r] = [(x - factor * y) % P for x, y in zip(a[r], a[i])]
        pivots.append(col)
    free = next(j for j in range(28) if j not in pivots)
    vector = [0] * 28
    vector[free] = 1
    for i, col in enumerate(pivots):
        vector[col] = -a[i][free] % P
    assert any(vector)
    assert all(sum(x * y for x, y in zip(row, vector)) % P == 0 for row in matrix)
    return a, pivots, vector


def main():
    blocks = {}
    cases = []
    failures = []
    exceptional = None
    for label, origin in labelings():
        keys = []
        matrix = []
        for t in range(16):
            support = tuple(sorted(label[(t + a) % 16] for a in (0, 1, 2, 5)))
            key = ','.join(map(str, support))
            if key not in blocks:
                blocks[key] = support_block(support)
            keys.append(key)
            matrix.extend(blocks[key]["matrix"])
        selected = independent_rows(matrix)
        rank = len(selected)
        case = {"labeling": label, "origin": origin, "support_keys": keys,
                "rank": rank, "selected_rows": selected}
        if rank == 28:
            case["minor_determinant"] = determinant([matrix[i] for i in selected])
            if not case["minor_determinant"]:
                failures.append(f"Zero claimed maximal minor at case {len(cases)}")
        else:
            reduced, pivots, vector = reduction_and_kernel(matrix)
            exceptional = {"case_index": len(cases), "matrix": matrix,
                           "reduced_matrix": reduced, "pivot_columns": pivots,
                           "kernel_vector": vector}
        cases.append(case)
        if exceptional or failures:
            break
    counts = Counter(case["origin"].split('-')[0] for case in cases)
    report = {"modulus": P, "H": H, "seed": SEED, "limit": LIMIT,
              "column_pairs": PAIRS, "row_pairs": ROW_PAIRS,
              "cases": cases, "support_blocks": blocks, "exceptional": exceptional,
              "summary": {"tested": len(cases), "required_rank": 28,
                          "rank_counts": dict(Counter(c["rank"] for c in cases)),
                          "origins": dict(counts), "distinct_support_blocks": len(blocks),
                          "deficient_case": None if exceptional is None else exceptional["case_index"],
                          "failures": failures,
                          "universal_statement_decided": exceptional is not None}}
    output = HERE / 'arbitrary-label-rank-result.json'
    output.write_text(json.dumps(report, separators=(',', ':')) + '\n')
    print(json.dumps(report['summary'], sort_keys=True))
    print(f"Full certificate: {output}")
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
