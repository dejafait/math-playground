"""Small exact support-only elimination certificate; no family census.

Run from the notebook: python3 scripts/seven-coordinate/zero_anchor_support_filter.py
"""
from itertools import combinations
from pathlib import Path
import json

P = 97
H = [x for x in range(1, P) if pow(x, 16, P) == 1]
S = [1, 8, 12, 18, 22, 27, 33]
J = [x for x in H if x not in S]
PAIRS = list(combinations(range(7), 2))
SUPPORTS = [([1, 8], [47, 50]), ([12, 18], [64, 70]),
            ([22, 27], [75, 79]), ([1, 33], [85, 89])]


def g(k, x):
    out = 1
    for y in J:
        if y not in k:
            out = out * (x-y) % P
    return out


def block(i, k):
    observed = [x for x in S if x not in i]
    z = observed[0]
    covectors = []
    for x in observed[1:]:
        c = [0]*7
        c[S.index(x)] = g(k, z)
        c[S.index(z)] = -g(k, x) % P
        covectors.append(c)
    matrix = [[(a[x]*b[y]-a[y]*b[x]) % P for x, y in PAIRS]
              for a, b in combinations(covectors, 2)]
    return {'I': i, 'K': k, 'pivot': z, 'covectors': covectors,
            'matrix': matrix}


def rank_and_rows(matrix):
    basis, indices = {}, []
    for index, original in enumerate(matrix):
        row = original[:]
        for col, pivot in sorted(basis.items()):
            c = row[col]
            row = [(a-c*b) % P for a, b in zip(row, pivot)]
        col = next((c for c, value in enumerate(row) if value), None)
        if col is not None:
            inv = pow(row[col], -1, P)
            basis[col] = [a*inv % P for a in row]
            indices.append(index)
    return len(basis), indices


def determinant(matrix):
    a = [row[:] for row in matrix]
    out = 1
    for j in range(len(a)):
        pivot = next((i for i in range(j, len(a)) if a[i][j]), None)
        if pivot is None:
            return 0
        if pivot != j:
            a[pivot], a[j] = a[j], a[pivot]
            out = -out
        value = a[j][j]
        out = out*value % P
        for i in range(j+1, len(a)):
            c = a[i][j]*pow(value, -1, P) % P
            for k in range(j, len(a)):
                a[i][k] = (a[i][k]-c*a[j][k]) % P
    return out


def wedge(a, b):
    return [(a[x]*b[y]-a[y]*b[x]) % P for x, y in PAIRS]


def integer_determinant(matrix):
    """Independent fraction-free integer evaluation of the selected minor."""
    a = [row[:] for row in matrix]
    sign, previous = 1, 1
    for k in range(len(a)-1):
        pivot = next((i for i in range(k, len(a)) if a[i][k]), None)
        if pivot is None:
            return 0
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            sign = -sign
        value = a[k][k]
        for i in range(k+1, len(a)):
            for j in range(k+1, len(a)):
                numerator = value*a[i][j]-a[i][k]*a[k][j]
                assert numerator % previous == 0
                a[i][j] = numerator//previous
            a[i][k] = 0
        previous = value
    return sign*a[-1][-1]


def run():
    blocks = [block(i, k) for i, k in SUPPORTS]
    matrix = [row for b in blocks for row in b['matrix']]
    rank, indices = rank_and_rows(matrix)
    minor = [matrix[i] for i in indices] if rank == 21 else []
    det = determinant(minor) if minor else None
    integer_det = integer_determinant(minor) if minor else None
    prefix_ranks = [rank_and_rows(matrix[:6*r])[0] for r in range(1, 5)]
    supports = [set(i+k) for i, k in SUPPORTS]
    intersections = [len(a & b) for a, b in combinations(supports, 2)]
    # L104's two-disjoint-row local construction is a positive control.
    endpoints = [[(g(k, x)+(x in i)) % P for x in S]
                 for i, k in SUPPORTS[:2]]
    u = endpoints[0]
    v = [(b-a) % P for a, b in zip(*endpoints)]
    bivector = wedge(u, v)
    residuals = [sum(a*b for a, b in zip(row, bivector)) % P
                 for row in matrix[:12]]
    moments, weights = [], []
    for j, (i, k) in enumerate(SUPPORTS[:2]):
        error = {x: 1 for x in i}
        error.update({x: -g(k, x) % P for x in k})
        weights.append(error)
        moments.append([sum(((endpoints[j][S.index(x)] if x in S else 0)
                            - error.get(x, 0))*pow(x, d, P)
                            for x in H) % P for d in range(1, 9)])
    failures = []
    if rank != 21 or not det:
        failures.append('fixed four-row full-rank test failed')
    if integer_det is None or integer_det % P != det:
        failures.append('integer determinant replay disagrees')
    if max(intersections) > 1:
        failures.append('supports not pairwise linear')
    if not any(bivector) or any(residuals) or any(map(any, moments)):
        failures.append('two-row positive control failed')
    if any(value == 0 for error in weights for value in error.values()):
        failures.append('positive-control error not full')
    out = {'modulus': P, 'H': H, 'S': S, 'J': J,
           'scope': 'four fixed rows only; not a t=0 census or survivor',
           'column_pairs': [[S[x], S[y]] for x, y in PAIRS],
           'blocks': blocks, 'prefix_ranks': prefix_ranks,
           'actual_rank': rank, 'required_exclusion_rank': 21,
           'minor_row_indices_zero_based': indices, 'minor': minor,
           'minor_determinant': det, 'integer_minor_determinant': integer_det,
           'pair_intersections': intersections,
           'positive_control': {'u': u, 'v': v, 'bivector': bivector,
                                'matrix_residuals': residuals,
                                'errors': weights, 'moment_residuals': moments},
           'failures': failures}
    path = Path(__file__).with_name('zero-anchor-support-filter.json')
    path.write_text(json.dumps(out, indent=2)+'\n')
    print(f'Rank {rank}/21; prefix ranks {prefix_ranks}; minor determinant {det}; '
          f'failures {failures}; certificate {path}')
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    run()
