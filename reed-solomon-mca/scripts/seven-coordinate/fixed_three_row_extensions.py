"""Complete fixed-seed support/rank test, retaining every deficient kernel.

Run: python3 scripts/seven-coordinate/fixed_three_row_extensions.py
No field descent, Plucker feasibility, or actual-event claim is made.
"""
from collections import Counter
from itertools import combinations
from pathlib import Path
import json

import zero_anchor_support_filter as original

P = 97
S = original.S
H = sorted({pow(5, 6*j, P) for j in range(16)})
assert H == original.H and len(H) == 16
J = [x for x in H if x not in S]
PAIRS = list(combinations(range(7), 2))
SEED = original.SUPPORTS[:3]


def ratio_block(i, k):
    """Rebuild quotients w_x/g(x)-w_z/g(z), independently of producer."""
    coeff = [1]
    for root in J:
        if root in k:
            continue
        new = [0]*(len(coeff)+1)
        for d, value in enumerate(coeff):
            new[d] = (new[d]-root*value) % P
            new[d+1] = (new[d+1]+value) % P
        coeff = new
    values = []
    for x in S:
        value = 0
        for a in reversed(coeff):
            value = (value*x+a) % P
        assert value
        values.append(value)
    observed = [a for a, x in enumerate(S) if x not in i]
    z = observed[0]
    covectors = []
    for x in observed[1:]:
        row = [0]*7
        row[x] = pow(values[x], -1, P)
        row[z] = -pow(values[z], -1, P) % P
        covectors.append(row)
    return [[(a[x]*b[y]-a[y]*b[x]) % P for x, y in PAIRS]
            for a, b in combinations(covectors, 2)]


def rref_kernel(matrix):
    a = [row[:] for row in matrix]
    pivots = []
    for col in range(21):
        pivot = next((r for r in range(len(pivots), len(a)) if a[r][col]), None)
        if pivot is None:
            continue
        r = len(pivots)
        a[r], a[pivot] = a[pivot], a[r]
        inv = pow(a[r][col], -1, P)
        a[r] = [v*inv % P for v in a[r]]
        for other in range(len(a)):
            if other == r:
                continue
            scale = a[other][col]
            if scale:
                a[other] = [(x-scale*y) % P for x, y in zip(a[other], a[r])]
        pivots.append(col)
    free = [c for c in range(21) if c not in pivots]
    basis = []
    for c in free:
        vector = [0]*21
        vector[c] = 1
        for r, pivot in enumerate(pivots):
            vector[pivot] = -a[r][c] % P
        basis.append(vector)
    return pivots, basis


def run():
    seed_sets = [set(i+k) for i, k in SEED]
    seed_matrix = [row for i, k in SEED for row in original.block(i, k)['matrix']]
    ratio_seed = [row for i, k in SEED for row in ratio_block(i, k)]
    assert original.rank_and_rows(seed_matrix)[0] == 18
    assert len(rref_kernel(ratio_seed)[0]) == 18
    counts = Counter()
    linear_counts = Counter()
    records, survivors, failures = [], [], []
    for i_tuple in combinations(S, 2):
        for k_tuple in combinations(J, 2):
            i, k = list(i_tuple), list(k_tuple)
            support = set(i+k)
            intersections = [len(support & a) for a in seed_sets]
            linear = max(intersections) <= 1
            matrix = seed_matrix + original.block(i, k)['matrix']
            rank, independent = original.rank_and_rows(matrix)
            pivots, basis = rref_kernel(ratio_seed+ratio_block(i, k))
            row_failures = []
            if rank != len(pivots) or len(basis) != 21-rank:
                row_failures.append('independent ranks/nullity disagree')
            for vector in basis:
                if not any(vector) or any(sum(x*y for x, y in zip(row, vector)) % P
                                          for row in matrix):
                    row_failures.append('kernel vector failed original matrix')
            record = {'I': i, 'K': k, 'seed_intersections': intersections,
                      'pairwise_linear': linear, 'rank': rank,
                      'kernel_dimension': len(basis), 'kernel_basis': basis,
                      'pivot_columns': pivots}
            if rank == 21:
                minor = [matrix[r] for r in independent]
                det = original.determinant(minor)
                if not det:
                    row_failures.append('full-rank minor is zero')
                record.update(minor_row_indices=independent, minor_residue=det)
            if row_failures:
                failures.append({'I': i, 'K': k, 'failures': row_failures})
            records.append(record)
            counts[rank] += 1
            if linear:
                linear_counts[rank] += 1
                if rank <= 20:
                    survivors.append({'I': i, 'K': k, 'rank': rank})
    expected = {(i, k) for i in combinations(S, 2) for k in combinations(J, 2)}
    actual = {(tuple(r['I']), tuple(r['K'])) for r in records}
    if len(records) != 756 or len(actual) != 756 or actual != expected:
        failures.append({'coverage': '756 distinct supports not completely covered'})
    output = {'modulus': P, 'H': H, 'S': S, 'J': J,
              'seed': [{'I': i, 'K': k} for i, k in SEED], 'seed_rank': 18,
              'column_pairs': [[S[a], S[b]] for a, b in PAIRS],
              'scope': 'fixed three-row seed; necessary rank filter only',
              'summary': {'actual_cases': len(records), 'required_cases': 756,
                          'all_rank_histogram': dict(sorted(counts.items())),
                          'linear_cases': sum(linear_counts.values()),
                          'linear_rank_histogram': dict(sorted(linear_counts.items())),
                          'linear_survivor_count': len(survivors),
                          'required_exclusion_rank': 21},
              'unresolved_gates': ['nonzero decomposable kernel tensor over F_(97^20)',
                                  'each projected restriction has rank one',
                                  'lambda and both overlap weights nonzero',
                                  'prescribed original finite-chart gate',
                                  'remaining t=0 equality events and balance'],
              'linear_survivors': survivors, 'cases': records, 'failures': failures}
    path = Path(__file__).with_name('fixed-three-row-extensions.json')
    path.write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps(output['summary'], sort_keys=True))
    print(f'Failures: {len(failures)}; certificate: {path}')
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    run()
