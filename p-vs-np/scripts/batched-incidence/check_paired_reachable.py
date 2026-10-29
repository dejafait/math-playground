#!/usr/bin/env python3
"""Exact N=4 paired Krylov and complete original-coordinate low-weight test."""

import argparse
import itertools
import json
from math import comb
from pathlib import Path

from check_weight_filtration import act, endpoint, insert, rank


def reduce_row(row, pivots):
    for index in sorted(pivots, reverse=True):
        if row & (1 << index):
            row ^= pivots[index]
    return row


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    n = 4
    a, b = endpoint(n, 'A'), endpoint(n, 'B')
    width = len(a['vertices'])
    mask = (1 << width) - 1
    transition = a['M_rows'] + [r << width for r in b['M_rows']]
    row = a['alpha_bits'] | (b['alpha_bits'] << width)
    krylov, pivots = [], {}
    while row:
        krylov.append(row)
        insert(row, pivots)
        row = act(row, transition)
        assert len(krylov) <= 2 * width
    assert all(act(r, a['all_residual_polynomial_bits'] +
                   b['all_residual_polynomial_bits']) == 0 for r in krylov)
    projections = [sum(((r >> (1 + n - 1 - j)) & 1) << j for j in range(n))
                   for r in krylov]
    examined, buckets, threshold_ranks = [], [], []
    selected, low_pivots = [], {}
    for weight in range(5):
        passing, count = [], 0
        for indices in itertools.combinations(range(2 * width), weight):
            count += 1
            candidate = sum(1 << i for i in indices)
            if reduce_row(candidate, pivots) == 0:
                passing.append(candidate)
        assert count == comb(2 * width, weight)
        passing.sort()
        for candidate in passing:
            if insert(candidate, low_pivots):
                selected.append(candidate)
        examined.append(count)
        buckets.append(passing)
        threshold_ranks.append(len(low_pivots))
    all_rows = [0]
    for r in krylov:
        assert r not in all_rows
        all_rows += [v ^ r for v in all_rows]
    assert len(all_rows) == len(set(all_rows)) == 1 << len(krylov)
    all_rows.sort()
    by_weight = sorted(all_rows, key=lambda r: (r.bit_count(), r))
    minimum_basis, greedy_pivots, full_ranks = [], {}, []
    for weight in range(2 * width + 1):
        for r in by_weight:
            if r.bit_count() == weight and insert(r, greedy_pivots):
                minimum_basis.append(r)
        full_ranks.append(len(greedy_pivots))
    report = {
        'N': n, 'S': a['g'] + b['g'], 'A': a, 'B': b,
        'paired_coordinate_order': ['A_' + v for v in a['vertices']] +
                                   ['B_' + v for v in b['vertices']],
        'all_nonzero_krylov_rows': krylov, 'next_krylov_row': row,
        'dimension': rank(krylov), 'r_projection_rows_reversed': projections,
        'r_projection_rank': rank(projections),
        'subsets_examined_by_weight': examined,
        'all_K_rows_by_exact_weight_0_through_4': buckets,
        'counts_by_exact_weight_0_through_4': list(map(len, buckets)),
        'threshold_ranks_0_through_4': threshold_ranks,
        'low_weight_rank_witness_rows': selected,
        'all_K_rows': all_rows, 'all_threshold_ranks': full_ranks,
        'minimum_support_basis_rows': minimum_basis,
        'minimum_basis_support': sum(r.bit_count() for r in minimum_basis),
        'failures': [],
        'qualification': 'Exact finite evidence only. Uniform projection and support claims require the written proof.'}
    assert report['dimension'] == 9
    assert report['r_projection_rank'] == n
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + '\n')
    print(f'N={n}, S={report["S"]}; Krylov dimension actual/expected: {report["dimension"]}/9; r projection rank actual/required: {rank(projections)}/{n}.')
    print(f'Coordinate subsets examined actual/required: {sum(examined)}/{sum(comb(2*width,w) for w in range(5))}; K rows: {len(all_rows)}/{1 << report["dimension"]}.')
    print('Weight <=4 counts:', report['counts_by_exact_weight_0_through_4'], '; threshold ranks:', threshold_ranks, '; full dimension:', report['dimension'])
    print('Finite minimum basis support:', report['minimum_basis_support'], '; O(N) asymptotics: not established by enumeration.')
    print('Failures:', report['failures'], '; full certificate:', args.output)


if __name__ == '__main__':
    main()
