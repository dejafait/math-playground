#!/usr/bin/env python3
"""Complete low-weight enumeration in the original dyadic endpoint coordinates.

Construct the literal graphs and right closures first. Enumerate coordinate
subsets, not all parameter vectors. Retain every passing row and rank witness.
"""

import argparse
import itertools
import json
from math import comb
from pathlib import Path


def act(row, values):
    out = 0
    while row:
        bit = row & -row
        out ^= values[bit.bit_length() - 1]
        row ^= bit
    return out


def insert(row, pivots):
    value = row
    while value:
        index = value.bit_length() - 1
        if index not in pivots:
            pivots[index] = value
            return True
        value ^= pivots[index]
    return False


def rank(rows):
    pivots = {}
    for row in rows:
        insert(row, pivots)
    return len(pivots)


def endpoint(n, name):
    f = [f'f{i}' for i in range(n + 1)]
    h = [f'h{i}' for i in range(n + 1)]
    vertices = ['s'] + f + h + ['t']
    topo = ['s'] + (f + h if name == 'A' else h + f) + ['t']
    ix = {v: i for i, v in enumerate(vertices)}
    pos = {v: i for i, v in enumerate(topo)}
    edges = [(f[i], f[i + 1], c) for i in range(n) for c in ('1', 'x')]
    edges += [(h[i], h[i + 1], 'x') for i in range(n)]
    edges += ([('s', f[0], '1'), (f[-1], h[0], '1'), (h[-1], 't', '1')]
              if name == 'A' else
              [('s', h[0], '1'), (h[-1], f[0], '1'), (f[-1], 't', '1')])
    assert all(pos[u] < pos[v] for u, v, _ in edges)
    width = len(vertices)
    closure = []
    for start in range(width):
        row = 1 << start
        for u in topo:
            if (row >> ix[u]) & 1:
                for tail, head, label in edges:
                    if tail == u and label == '1':
                        row ^= 1 << ix[head]
        closure.append(row)
    m = [0] * width
    for u, v, label in edges:
        if label == 'x':
            m[ix[u]] ^= closure[ix[v]]
    beta = [int(v == 't') for v in vertices]
    residuals = [0] * width
    column = beta[:]
    for degree in range(width):
        for i, coefficient in enumerate(column):
            residuals[i] |= coefficient << degree
        column = [act(row, column) for row in m]
    assert not any(column)
    return {'vertices': vertices, 'topological_order': topo,
            'occurrences': edges, 'K_rows': closure, 'M_rows': m,
            'alpha_bits': closure[ix['s']], 'beta_rows': beta,
            'all_residual_polynomial_bits': residuals,
            'g': width + 2 * len(edges)}


def pascal(n):
    return [sum((comb(j, i) & 1) << i for i in range(j + 1)) for j in range(n)]


def original_core(r, b, p, n):
    width = 2 * n + 4
    blocks = [r, act(r ^ b, p), b, act(r, p)]
    out = 0
    for block, value in enumerate(blocks):
        offset = (block // 2) * width + (1 if block % 2 == 0 else n + 2)
        for j in range(n):
            if (value >> j) & 1:
                out |= 1 << (offset + n - 1 - j)
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--n', type=int, default=16)
    parser.add_argument('--max-weight', type=int, default=4)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    n, bound = args.n, args.max_weight
    assert n >= 1 and n & (n - 1) == 0 and 0 <= bound <= 4
    a, b = endpoint(n, 'A'), endpoint(n, 'B')
    width = 2 * n + 4
    residuals = a['all_residual_polynomial_bits'] + b['all_residual_polynomial_bits']
    p = pascal(n)
    core_basis = [original_core(1 << j, 0, p, n) for j in range(n)]
    core_basis += [original_core(0, 1 << j, p, n) for j in range(n)]
    core_mask = 0
    for row in core_basis:
        core_mask |= row
    assert core_mask.bit_count() == 4 * n
    assert rank(core_basis) == 2 * n
    assert all(act(row, residuals) == 0 for row in core_basis)
    assert rank(residuals) == 2 * n + 1
    assert a['g'] + b['g'] == 16 * n + 20
    zero_mask = sum(1 << i for i, value in enumerate(residuals) if value == 0)
    final_mask = (1 << (width - 1)) | (1 << (2 * width - 1))
    assert zero_mask.bit_count() == 6
    assert core_mask ^ zero_mask ^ final_mask == (1 << (2 * width)) - 1
    rows_by_weight, examined, core_counts = [], [], []
    full_pivots, core_pivots = {}, {}
    full_greedy, core_greedy, full_ranks, core_ranks = [], [], [], []
    for weight in range(bound + 1):
        passing = []
        count = 0
        for indices in itertools.combinations(range(2 * width), weight):
            count += 1
            syndrome = 0
            row = 0
            for i in indices:
                syndrome ^= residuals[i]
                row |= 1 << i
            if syndrome == 0:
                passing.append(row)
        assert count == comb(2 * width, weight)
        passing.sort()
        rows_by_weight.append(passing)
        examined.append(count)
        core_counts.append(sum(row & core_mask == row for row in passing))
        for row in passing:
            assert row & final_mask in (0, final_mask)
            if insert(row, full_pivots):
                full_greedy.append(row)
            core_row = row & core_mask
            assert act(core_row, residuals) == 0
            if insert(core_row, core_pivots):
                core_greedy.append(core_row)
        full_ranks.append(len(full_pivots))
        core_ranks.append(len(core_pivots))
        assert full_ranks[-1] == core_ranks[-1] + 6 * (weight >= 1) + (weight >= 2)
    prediction = 16 if n == 16 and bound == 4 else None
    prediction_pass = core_ranks[-1] == prediction if prediction is not None else None
    report = {'N': n, 'max_weight': bound, 'S': a['g'] + b['g'],
              'A': a, 'B': b, 'core_parameter_basis_rows': core_basis,
              'core_mask': core_mask, 'zero_mask': zero_mask, 'paired_final_mask': final_mask,
              'subsets_examined_by_weight': examined,
              'all_relation_rows_by_exact_weight': rows_by_weight,
              'relation_counts_by_exact_weight': list(map(len, rows_by_weight)),
              'core_counts_by_exact_weight': core_counts,
              'full_threshold_ranks': full_ranks, 'core_threshold_ranks': core_ranks,
              'full_rank_witness_rows': full_greedy, 'core_rank_witness_rows': core_greedy,
              'prediction': {'core_rank_required': prediction,
                             'core_rank_actual': core_ranks[-1], 'matched': prediction_pass},
              'failures': [] if prediction_pass is not False else ['core rank prediction failed'],
              'qualification': 'Complete finite low-weight enumeration only; no all-N inequality or O(N) basis/realization follows.'}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + '\n')
    print(f'N={n}, S={report["S"]}; enumerated {sum(examined)} / {sum(comb(2 * width, w) for w in range(bound + 1))} coordinate subsets.')
    print('Full threshold ranks:', full_ranks, '; core threshold ranks:', core_ranks)
    print('Passing counts by exact weight:', report['relation_counts_by_exact_weight'])
    print(f'Core rank actual/required at weight {bound}: {core_ranks[-1]}/{prediction}; matched={prediction_pass}.')
    print('Uniform superlinear all-basis support bound: NOT ESTABLISHED by this finite enumeration.')
    print('Failures:', report['failures'], '; full certificate:', args.output)


if __name__ == '__main__':
    main()
