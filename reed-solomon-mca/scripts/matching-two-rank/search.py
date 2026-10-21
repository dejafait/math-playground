"""One preplanned <=256-pair exact falsification test, not a classification."""
from collections import Counter
from itertools import combinations
import json
from pathlib import Path
from random import Random

P = 97
H = [x for x in range(1, P) if pow(x, 16, P) == 1]
CP = list(combinations(range(8), 2))
RP = list(combinations(range(4), 2))
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent


def rref(matrix):
    a = [row[:] for row in matrix]
    pivots = []
    for col in range(len(a[0])):
        k = len(pivots)
        pivot = next((i for i in range(k, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[k], a[pivot] = a[pivot], a[k]
        inv = pow(a[k][col], -1, P)
        a[k] = [v * inv % P for v in a[k]]
        for i in range(len(a)):
            if i != k and a[i][col]:
                factor = a[i][col]
                a[i] = [(v - factor * w) % P for v, w in zip(a[i], a[k])]
        pivots.append(col)
    return a, pivots


def kernels(reduced, pivots):
    result = []
    for free in range(len(reduced[0])):
        if free in pivots:
            continue
        v = [0] * len(reduced[0])
        v[free] = 1
        for i, pivot in enumerate(pivots):
            v[pivot] = -reduced[i][free] % P
        result.append(v)
    return result


def selected_rows(matrix):
    basis = {}
    indices = []
    for i, original in enumerate(matrix):
        row = original[:]
        for col in sorted(basis):
            factor = row[col]
            row = [(v - factor * w) % P for v, w in zip(row, basis[col])]
        col = next((j for j, v in enumerate(row) if v), None)
        if col is not None:
            inv = pow(row[col], -1, P)
            basis[col] = [v * inv % P for v in row]
            indices.append(i)
    return indices


def determinant(matrix):
    a = [row[:] for row in matrix]
    det = 1
    for col in range(len(a)):
        pivot = next((i for i in range(col, len(a)) if a[i][col]), None)
        if pivot is None:
            return 0
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            det = -det
        det = det * a[col][col] % P
        inv = pow(a[col][col], -1, P)
        for i in range(col + 1, len(a)):
            factor = a[i][col] * inv % P
            a[i] = [(v - factor * w) % P for v, w in zip(a[i], a[col])]
    return det


def block(labels):
    polynomial = [1]
    for x in labels:
        new = [0] * (len(polynomial) + 1)
        for j, value in enumerate(polynomial):
            new[j] = (new[j] - x * value) % P
            new[j + 1] = (new[j + 1] + value) % P
        polynomial = new
    rows = [[0] * r + polynomial + [0] * (3 - r) for r in range(4)]
    matrix = [[(rows[r][j] * rows[s][k] - rows[r][k] * rows[s][j]) % P
               for j, k in CP] for r, s in RP]
    return {"labels": labels, "annihilator": rows, "matrix": matrix}


def incidence(edges):
    masks = [sum(1 << v for v in e) for e in edges]
    degrees = [sum(v in e for e in edges) for v in range(16)]
    pairs = [list(c) for c in combinations(range(len(edges)), 2)
             if not masks[c[0]] & masks[c[1]]]
    triples = [list(c) for c in combinations(range(len(edges)), 3)
               if all(not masks[i] & masks[j] for i, j in combinations(c, 2))]
    valid = (len(edges) == len(set(masks)) == 16
             and all(len(e) == len(set(e)) == 4 and set(e) <= set(range(16)) for e in edges)
             and degrees == [4] * 16 and bool(pairs) and not triples)
    return {"admissible": valid, "degrees": degrees,
            "disjoint_pairs": pairs, "disjoint_triples": triples}


def make_plan():
    saved = json.loads((ROOT / 'scripts/small-union/cyclic-orbits-result.json').read_text())
    families = []
    for item in saved['qualifying_families']:
        seed = item['seed']
        edges = [sorted((v + t) % 16 for v in seed) for t in range(16)]
        assert {tuple(e) for e in edges} == {tuple(e) for e in item['edges']}
        families.append({"id": f"cyclic-{item['seed_mask']}", "seed": seed,
                         "edges": edges, "incidence": incidence(edges)})
    assert len(families) == 62
    controls = [next(f for f in families if f['seed'] == seed)
                for seed in ([0, 1, 2, 5], [0, 1, 3, 5])]
    two_block = {"id": "two-block-0124", "seed": [0, 1, 2, 4],
                 "edges": [sorted(8 * b + (v + t) % 8 for v in (0, 1, 2, 4))
                           for b in range(2) for t in range(8)]}
    two_block['incidence'] = incidence(two_block['edges'])
    families = controls + [two_block] + [f for f in families if f not in controls]
    cyclic = [pow(8, i, P) for i in range(16)]
    swap = cyclic[:]
    swap[0], swap[1] = swap[1], swap[0]
    shuffled = H[:]
    Random(20261006058).shuffle(shuffled)
    labels = [('powers-8', cyclic), ('sorted-H', H), ('swap-0-1', swap),
              ('shuffle-20261006058', shuffled)]
    assert len({tuple(l) for _, l in labels}) == 4
    assert all(sorted(l) == H for _, l in labels)
    cases = [{"family_id": f['id'], "labeling_id": name, "labeling": lab,
              "control": f in controls} for f in families for name, lab in labels]
    assert len(cases) == 252 <= 256
    assert len({(tuple(sorted(tuple(e) for e in f['edges'])), tuple(lab))
                for f in families for _, lab in labels}) == 252
    return {"limit": 256, "modulus": P, "H": H, "column_pairs": CP,
            "row_pairs": RP, "families": families, "cases": cases,
            "rejected_families": [f['id'] for f in families if not f['incidence']['admissible']]}


def main():
    plan = make_plan()
    # Freeze all inputs before any matrix or rank is calculated.
    (HERE / 'plan.json').write_text(json.dumps(plan, separators=(',', ':')) + '\n')
    assert not plan['rejected_families'], plan['rejected_families']
    families = {f['id']: f for f in plan['families']}
    blocks, cases, failures = {}, [], []
    defect = None
    for ci, case in enumerate(plan['cases']):
        keys, matrix = [], []
        for edge in families[case['family_id']]['edges']:
            labels = sorted(case['labeling'][v] for v in edge)
            key = ','.join(map(str, labels))
            if key not in blocks:
                blocks[key] = block(labels)
            keys.append(key)
            matrix.extend(blocks[key]['matrix'])
        indices = selected_rows(matrix)
        selected = [matrix[i] for i in indices]
        reduced, pivots = rref(selected)
        minor = [[row[j] for j in pivots] for row in selected]
        det = determinant(minor)
        rank = len(indices)
        result = {"plan_index": ci, "support_keys": keys, "rank": rank,
                  "selected_rows": indices, "minor_columns": pivots,
                  "minor_determinant": det}
        cases.append(result)
        if not det or len(pivots) != rank:
            failures.append(f'Invalid lower-rank certificate at case {ci}')
        if case['control'] and rank != 28:
            failures.append(f'Failed known rank control at case {ci}')
        if rank < 28:
            kernel = kernels(reduced, pivots)
            assert all(sum(a * b for a, b in zip(row, v)) % P == 0
                       for row in matrix for v in kernel)
            defect = {"plan_index": ci, "matrix": matrix, "kernel_basis": kernel,
                      "selected_reduced": reduced, "pivot_columns": pivots}
        if defect or failures:
            break
    summary = {"planned": len(plan['cases']), "limit": 256, "tested": len(cases),
               "required_rank": 28, "rank_counts": dict(Counter(c['rank'] for c in cases)),
               "defect_index": None if defect is None else defect['plan_index'],
               "controls_passed": sum(plan['cases'][c['plan_index']]['control'] and c['rank'] == 28 for c in cases),
               "rejected_families": plan['rejected_families'], "failures": failures,
               "universal_rank_refuted_pending_independent_check": defect is not None and not failures}
    report = {"summary": summary, "cases": cases, "support_blocks": blocks, "defect": defect}
    (HERE / 'result.json').write_text(json.dumps(report, separators=(',', ':')) + '\n')
    print(json.dumps(summary, sort_keys=True))
    print('Inputs: scripts/matching-two-rank/plan.json')
    print('Full certificate: scripts/matching-two-rank/result.json')
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
