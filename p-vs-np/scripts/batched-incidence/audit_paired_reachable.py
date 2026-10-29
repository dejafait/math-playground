#!/usr/bin/env python3
"""Receive N=4 evidence independently using sets and exhaustive codewords.

No constructor imports. Check literal closed rows against occurrence-matrix
closure, build the complete Krylov span by symmetric differences, and obtain
every low-weight row by filtering all 512 codewords, not coordinate search.
"""

import argparse
import json
from math import comb
from pathlib import Path


def support(bits, width):
    assert 0 <= bits < 1 << width
    return {i for i in range(width) if bits & (1 << i)}


def bits(indices):
    return sum(1 << i for i in indices)


def apply(row, matrix):
    result = set()
    for i in row:
        result ^= matrix[i]
    return result


def independent(rows):
    pivots, chosen = {}, []
    for original in rows:
        row = set(original)
        while row:
            pivot = min(row)
            if pivot in pivots:
                row ^= pivots[pivot]
            else:
                pivots[pivot] = row
                chosen.append(original)
                break
    return chosen


def receive_graph(n, name, graph):
    vertices = ['s'] + [f'f{i}' for i in range(n + 1)] + [f'h{i}' for i in range(n + 1)] + ['t']
    width = len(vertices)
    index = {v: i for i, v in enumerate(vertices)}
    assert graph['vertices'] == vertices
    expected = [(f'f{i}', f'f{i+1}', c) for i in range(n) for c in ['1', 'x']]
    expected += [(f'h{i}', f'h{i+1}', 'x') for i in range(n)]
    expected += ([('s', 'f0', '1'), (f'f{n}', 'h0', '1'), (f'h{n}', 't', '1')]
                 if name == 'A' else
                 [('s', 'h0', '1'), (f'h{n}', 'f0', '1'), (f'f{n}', 't', '1')])
    assert sorted(map(tuple, graph['occurrences'])) == sorted(expected)
    pos = {v: i for i, v in enumerate(graph['topological_order'])}
    assert set(pos) == set(vertices) and len(graph['topological_order']) == width
    assert all(pos[u] < pos[v] for u, v, _ in expected)
    constant, letter = [set() for _ in vertices], [set() for _ in vertices]
    for u, v, c in expected:
        (constant if c == '1' else letter)[index[u]] ^= {index[v]}
    closure = []
    for start in range(width):
        total, power = set(), {start}
        for _ in range(width):
            total ^= power
            power = apply(power, constant)
        assert not power
        closure.append(total)
    assert list(map(bits, closure)) == graph['K_rows']
    matrix = [apply(row, closure) for row in letter]
    literal = [set() for _ in vertices]
    for i in range(n):
        literal[index[f'f{i}']] = {index[f'f{j}'] for j in range(i+1, n+1)}
        literal[index[f'f{i}']] ^= {index['h0' if name == 'A' else 't']}
    for i in range(n-1):
        literal[index[f'h{i}']] = {index[f'h{i+1}']}
    literal[index[f'h{n-1}']] = {index[f'h{n}'], index['t']}
    if name == 'B':
        literal[index[f'h{n-1}']] ^= {index[f'f{i}'] for i in range(n+1)}
    assert matrix == literal
    assert list(map(bits, matrix)) == graph['M_rows']
    alpha = {index['s'], index['h0']}
    if name == 'A':
        alpha ^= {index[f'f{i}'] for i in range(n+1)}
    assert alpha == closure[0] and bits(alpha) == graph['alpha_bits']
    assert graph['beta_rows'] == [int(v == 't') for v in vertices]
    residuals = [0] * width
    for i in range(width):
        row = {i}
        for degree in range(width):
            residuals[i] |= int(index['t'] in row) << degree
            row = apply(row, matrix)
        assert not row
    assert residuals == graph['all_residual_polynomial_bits']
    assert graph['g'] == width + 2 * len(expected)
    return matrix, alpha, residuals


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('certificate', type=Path)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    source = json.loads(args.certificate.read_text())
    n = source['N']
    assert n == 4
    width = 2*n+4
    a, alpha, ra = receive_graph(n, 'A', source['A'])
    b, beta, rb = receive_graph(n, 'B', source['B'])
    matrix = a + [{i+width for i in row} for row in b]
    row = alpha | {i+width for i in beta}
    krylov = []
    while row:
        krylov.append(row)
        row = apply(row, matrix)
        assert len(krylov) <= 2*width
    assert list(map(bits, krylov)) == source['all_nonzero_krylov_rows']
    assert source['next_krylov_row'] == 0
    assert len(independent(krylov)) == source['dimension'] == 9
    residuals = ra + rb
    for row in krylov:
        value = 0
        for i in row:
            value ^= residuals[i]
        assert value == 0
    projections = [{n-1-(i-1) for i in row if 1 <= i <= n} for row in krylov]
    assert list(map(bits, projections)) == source['r_projection_rows_reversed']
    assert len(independent(projections)) == source['r_projection_rank'] == n
    all_rows = {frozenset()}
    for row in krylov:
        all_rows |= {v ^ frozenset(row) for v in all_rows}
    assert len(all_rows) == 512
    assert sorted(map(bits, all_rows)) == source['all_K_rows']
    buckets = [sorted(bits(v) for v in all_rows if len(v) == w) for w in range(5)]
    assert buckets == source['all_K_rows_by_exact_weight_0_through_4']
    assert list(map(len, buckets)) == source['counts_by_exact_weight_0_through_4']
    assert source['subsets_examined_by_weight'] == [comb(2*width, w) for w in range(5)]
    ranks = [len(independent([v for v in all_rows if len(v) <= w])) for w in range(2*width+1)]
    assert ranks == source['all_threshold_ranks']
    assert ranks[:5] == source['threshold_ranks_0_through_4'] == [0, 0, 1, 4, 7]
    witnesses = [support(v, 2*width) for v in source['low_weight_rank_witness_rows']]
    assert all(frozenset(v) in all_rows and len(v) <= 4 for v in witnesses)
    assert len(independent(witnesses)) == len(witnesses) == 7
    basis = [support(v, 2*width) for v in source['minimum_support_basis_rows']]
    assert all(frozenset(v) in all_rows for v in basis)
    assert len(independent(basis)) == len(basis) == 9
    # Any basis has at most rank(K_{<=w}) elements of weight <=w.
    lower_bound = sum(9 - ranks[w] for w in range(2*width))
    assert sum(map(len, basis)) == source['minimum_basis_support'] == lower_bound == 38
    assert source['S'] == source['A']['g'] + source['B']['g'] == 84
    assert source['failures'] == []
    report = {'N': n, 'all_codewords_received': len(all_rows),
              'dimension_actual_required': [len(independent(krylov)), 9],
              'r_projection_rank_actual_required': [len(independent(projections)), n],
              'all_nonzero_krylov_rows': list(map(bits, krylov)),
              'counts_by_exact_weight_0_through_4': list(map(len, buckets)),
              'complete_threshold_ranks': ranks,
              'low_weight_rank_actual_full_dimension': [ranks[4], 9],
              'minimum_basis_support_actual_lower_bound': [sum(map(len, basis)), lower_bound],
              'failures': [], 'source_certificate': str(args.certificate),
              'qualification': 'Independent finite reception; not a uniform support proof.'}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + '\n')
    print('Received every graph occurrence, closure, literal closed row, Krylov row and all 512/512 codewords.')
    print('Dimension actual/required: 9/9; reversed r projection rank actual/required: 4/4.')
    print('Weight <=4 counts:', list(map(len, buckets)), '; threshold ranks:', ranks[:5], '; spanning threshold: 9.')
    print(f'Minimum finite basis support actual/required lower bound: {sum(map(len,basis))}/{lower_bound}; failures: []; full receipt: {args.output}')


if __name__ == '__main__':
    main()
