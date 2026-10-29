#!/usr/bin/env python3
"""Exact L109 stack for the complete E_2 in the canonical L167 table."""
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
P = 97
S = [1, 8, 12, 18, 22, 27, 33]
J = [47, 50, 64, 70, 75, 79, 85, 89, 96]
IDS = [2, 3, 4, 5, 7, 8, 9, 11, 12, 13, 15, 16]
SOURCE = ROOT / 'lemmas/L167-completed-family-marked-extraction-counterexample.md'
REDUCTION = ROOT / 'lemmas/L109-seven-coordinate-parameter-free-support-filter.md'


def table(text):
    lines = text.splitlines()
    start = next(i for i, line in enumerate(lines) if line.startswith('| Row | Class'))
    result = []
    for line in lines[start + 2:]:
        if not line.startswith('|'):
            break
        cells = [c.strip() for c in line.strip('|').split('|')]
        result.append({'id': int(cells[0]),
                       'I': [int(x) for x in cells[2].split(',')],
                       'K': [int(x) for x in cells[3].split(',')]})
    return result


def reduce_matrix(matrix):
    a = [r[:] for r in matrix]
    origins = list(range(len(a)))
    pivots, selected = [], []
    for col in range(len(a[0])):
        k = len(pivots)
        pos = next((i for i in range(k, len(a)) if a[i][col]), None)
        if pos is None:
            continue
        a[k], a[pos] = a[pos], a[k]
        origins[k], origins[pos] = origins[pos], origins[k]
        selected.append(origins[k])
        inv = pow(a[k][col], -1, P)
        a[k] = [x * inv % P for x in a[k]]
        for i in range(len(a)):
            if i != k:
                factor = a[i][col]
                a[i] = [(x - factor*y) % P for x, y in zip(a[i], a[k])]
        pivots.append(col)
    return a, pivots, selected


def determinant(matrix):
    a = [row[:] for row in matrix]
    det = 1
    for j in range(len(a)):
        k = next((i for i in range(j, len(a)) if a[i][j]), None)
        if k is None:
            return 0
        if j != k:
            a[j], a[k] = a[k], a[j]
            det = -det
        pivot = a[j][j]
        det = det * pivot % P
        inv = pow(pivot, -1, P)
        for i in range(j + 1, len(a)):
            factor = a[i][j] * inv % P
            a[i] = [(x - factor*y) % P for x, y in zip(a[i], a[j])]
    return det % P


def main():
    rows = table(SOURCE.read_text())
    assert [r['id'] for r in rows] == list(range(1, 17))
    assert sorted(x for r in rows for x in r['I'] + r['K']) == sorted((S + J)*4)
    assert all(set(r['I']) <= set(S) and set(r['K']) <= set(J) for r in rows)
    selected = [r for r in rows if len(r['I']) == 2]
    assert [r['id'] for r in selected] == IDS
    assert all(len(r['K']) == 2 for r in selected)
    assert sorted(S + J) == [x for x in range(1, P) if pow(x, 16, P) == 1]
    pairs = list(combinations(S, 2))
    blocks, stack, identities = [], [], []
    for r in selected:
        roots = sorted(set(J) - set(r['K']))
        g = {}
        for x in sorted(S + J):
            val = 1
            for y in roots:
                val = val * (x-y) % P
            g[x] = val
        observed = sorted(set(S) - set(r['I']))
        z = observed[0]
        others = observed[1:]
        covectors = [[(g[z]*(a == x) - g[x]*(a == z)) % P for a in S]
                     for x in others]
        block = []
        for i, j in combinations(range(4), 2):
            block.append([(covectors[i][a]*covectors[j][b] -
                           covectors[i][b]*covectors[j][a]) % P
                          for a, b in combinations(range(7), 2)])
            identities.append({'support_row': r['id'], 'pivot': z,
                               'covector_pair': [others[i], others[j]]})
        blocks.append({**r, 'roots': roots, 'g': {str(x): g[x] for x in sorted(g)},
                       'pivot': z, 'covector_labels': others,
                       'Q': covectors, 'N': block})
        stack.extend(block)
    reduced, pivots, selected_rows = reduce_matrix(stack)
    rank = len(pivots)
    free = [j for j in range(21) if j not in pivots]
    kernel = []
    for j in free:
        v = [0]*21
        v[j] = 1
        for i, col in enumerate(pivots):
            v[col] = -reduced[i][j] % P
        kernel.append(v)
    minor = [[stack[i][j] for j in pivots] for i in selected_rows]
    residue = determinant(minor)
    assert residue != 0
    assert len(kernel) == 21-rank
    assert all(sum(a*b for a, b in zip(row, v)) % P == 0 for row in stack for v in kernel)
    out = {'modulus': P, 'S': S, 'J': J, 'E2_rows': IDS,
           'source_sha256': {str(p.relative_to(ROOT)): sha256(p.read_bytes()).hexdigest()
                             for p in (SOURCE, REDUCTION)},
           'canonical_table': rows, 'column_pairs': list(map(list, pairs)),
           'blocks': blocks, 'row_identities': identities, 'stack': stack,
           'rref': reduced, 'pivot_columns': pivots, 'free_columns': free,
           'kernel_basis': kernel, 'minor_row_indices': selected_rows,
           'minor_column_indices': pivots, 'minor_row_identities': [identities[i] for i in selected_rows],
           'minor': minor, 'minor_determinant_mod_97': residue,
           'summary': {'actual_rank': rank, 'required_rank': 21,
                       'kernel_dimension': len(kernel), 'matrix_shape': [len(stack), 21],
                       'failures': []}}
    path = HERE / 'certificate.json'
    path.write_text(json.dumps(out, indent=2) + '\n')
    print(f'Rank {rank}; required 21; kernel dimension {len(kernel)}; minor residue {residue}; failures 0.')
    print(f'Complete blocks/stack/minor/kernel: {path.relative_to(ROOT)}')


if __name__ == '__main__':
    main()
