#!/usr/bin/env python3
"""Replay complete dyadic certificates independently of their constructor.

Use the existing independent bit-matrix/closure replay primitives; do not
import the new construction or its formula. Optionally enumerate the
entire 16-dimensional N=8 core, retaining all evidence on disk.
"""

import argparse
import json
from pathlib import Path

from audit_residual_relation import act, rank, reconstruct


def insert(value, pivots):
    while value:
        i = value.bit_length() - 1
        if i not in pivots:
            pivots[i] = value
            return True
        value ^= pivots[i]
    return False


def expected_endpoint(n, order):
    f, h = [f'f{i}' for i in range(n + 1)], [f'h{i}' for i in range(n + 1)]
    edges = [(f[i], f[i+1], label) for i in range(n) for label in ('1', 'x')]
    edges += [(h[i], h[i+1], 'x') for i in range(n)]
    edges += ([('s', f[0], '1'), (f[-1], h[0], '1'), (h[-1], 't', '1')]
              if order == 'A' else
              [('s', h[0], '1'), (h[-1], f[0], '1'), (f[-1], 't', '1')])
    return ['s'] + f + h + ['t'], sorted(edges)


def replay(saved):
    n = saved['ledger']['N']
    assert n > 0 and n & (n - 1) == 0
    for name in ('A', 'B'):
        vertices, edges = expected_endpoint(n, name)
        assert saved[name]['vertices'] == vertices
        assert sorted(tuple(e) for e in saved[name]['occurrences']) == edges
    rebuilt = {name: reconstruct(saved[name]) for name in ('A', 'B', 'Q')}
    ma, aa, ba, ra = rebuilt['A']
    mb, ab, bb, rb = rebuilt['B']
    mq, aq, bq, _ = rebuilt['Q']
    width, dim = 2 * n + 4, 2 * n + 7
    basis = saved['basis_rows']
    assert len(basis) == rank(basis) == dim
    assert rank(ra + rb) == 2 * n + 1
    assert all(act(row, ra + rb) == 0 for row in basis)
    xa, xb = saved['basis_A_rows'], saved['basis_B_rows']
    assert basis == [u | (v << width) for u, v in zip(xa, xb)]
    t, c, d = saved['shift_rows'], saved['initial_coordinates'], saved['common_final_functional']
    products = {'A_left': [act(row, xa) for row in t],
                'A_right': [act(row, ma) for row in xa],
                'B_left': [act(row, xb) for row in t],
                'B_right': [act(row, mb) for row in xb]}
    assert products == saved['shift_products']
    assert products['A_left'] == products['A_right']
    assert products['B_left'] == products['B_right']
    assert act(c, xa) == aa and act(c, xb) == ab
    assert [act(row, ba) for row in xa] == [act(row, bb) for row in xb] == d
    assert d == [int(i == 6) for i in range(dim)] and act(c, d) == 0
    pos = {value: i for i, value in enumerate(saved['degree_topological_order'])}
    assert set(pos) == set(range(dim))
    assert all(pos[i] < pos[j] for i in range(dim) for j in range(dim) if (t[i] >> j) & 1)
    expected_edges = [(f'q{i}', f'q{j}', 'x') for i in range(dim)
                      for j in range(dim) if (t[i] >> j) & 1]
    expected_edges += [('s', f'q{i}', '1') for i in range(dim) if (c >> i) & 1]
    expected_edges += [('q6', 't', '1')]
    assert sorted(tuple(e) for e in saved['Q']['occurrences']) == sorted(expected_edges)
    evidence = {}
    for name, matrix, alpha, beta in [('A', ma, aa, ba), ('B', mb, ab, bb)]:
        y = saved['arrows'][name]['X_rows']
        left, right = [act(row, y) for row in mq], [act(row, matrix) for row in y]
        actual_final = [act(row, beta) for row in y]
        assert left == right and act(aq, y) == alpha and actual_final == bq
        evidence[name] = {'left': left, 'right': right, 'initial_actual': act(aq, y),
                          'initial_required': alpha, 'final_actual': actual_final,
                          'final_required': bq, 'support': sum(v.bit_count() for v in y)}
    pairs = [u | (v << width) for u, v in zip(saved['arrows']['A']['X_rows'], saved['arrows']['B']['X_rows'])]
    assert rank(pairs) == dim and all(act(v, ra + rb) == 0 for v in pairs)
    support = sum(v.bit_count() for v in basis)
    # Reconstruct the row-weight formula from literal factors and integer
    # binomial coefficients; no constructor recurrence is invoked.
    from math import comb
    predicted = 8
    k = n.bit_length() - 1
    for w in range(k + 1):
        predicted += comb(k, w) * ((5 if w % 2 == 0 else 7) << (w // 2))
    assert support == predicted == saved['ledger']['basis_support']
    assert sum(e['support'] for e in evidence.values()) == support
    ledger = saved['ledger']
    assert ledger['S'] == saved['A']['g'] + saved['B']['g'] == 16 * n + 20
    assert ledger['shift_support'] == sum(v.bit_count() for v in t)
    assert ledger['Q_vertices'] == len(saved['Q']['vertices']) == dim + 2
    assert ledger['Q_occurrences'] == len(expected_edges)
    assert ledger['g_Q'] == saved['Q']['g']
    assert ledger['initial_support'] == c.bit_count() and ledger['final_support'] == sum(d)
    return {'N': n, 'result': 'PASS', 'rank_actual_required': [dim, dim],
            'support_actual_formula': [support, predicted], 'shift_products': products,
            'arrows': evidence, 'received_rank': rank(pairs), 'ledger': ledger,
            'failures': []}


def enumerate_core(saved):
    assert saved['ledger']['N'] == 8
    basis = saved['basis_rows'][7:]
    assert len(basis) == rank(basis) == 16
    # Every core vector, not a sampled candidate set; zeros/final are separate.
    vectors = [0] * (1 << 16)
    for mask in range(1, 1 << 16):
        bit = mask & -mask
        vectors[mask] = vectors[mask ^ bit] ^ basis[bit.bit_length() - 1]
    assert len(set(vectors)) == 1 << 16
    buckets = [[] for _ in range(33)]
    for v in vectors:
        buckets[v.bit_count()].append(v)
    pivots, greedy, ranks = {}, [], []
    for bucket in buckets:
        for v in sorted(bucket):
            if insert(v, pivots):
                greedy.append(v)
        ranks.append(len(pivots))
    assert len(greedy) == 16
    minimum = sum(16 - r for r in ranks)
    assert minimum == sum(v.bit_count() for v in greedy)
    return {'all_core_vectors_in_mask_order': vectors,
            'rank_by_weight_0_through_32': ranks,
            'greedy_minimum_basis_rows': greedy, 'minimum_core_basis_support': minimum,
            'minimum_full_basis_support': minimum + 8,
            'qualification': 'Finite N=8 only. Additivity uses the disjoint zero/final factors; no uniform optimality inferred.'}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('certificate', type=Path)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--enumerate-core', action='store_true')
    args = parser.parse_args()
    source = json.loads(args.certificate.read_text())
    cases = [replay(case) for case in source['cases']]
    report = {'result': 'PASS', 'cases': cases, 'failures': [], 'certificate': str(args.certificate)}
    if args.enumerate_core:
        case = next(v for v in source['cases'] if v['ledger']['N'] == 8)
        report['finite_core_enumeration'] = enumerate_core(case)
    args.output.write_text(json.dumps(report, indent=2) + '\n')
    print('PASS: all original-coordinate equations, boundaries, full ranks and literal acyclic graphs.')
    for case in cases:
        ledger = case['ledger']
        print('N={N}, S={S}, basis/maps={basis_support}, shift={shift_support}, Q={Q_vertices} vertices/{Q_occurrences} occurrences'.format(**ledger))
    if args.enumerate_core:
        result = report['finite_core_enumeration']
        print('Exhaustive N=8 core vectors: 65536; minimum full basis support:', result['minimum_full_basis_support'])
    print('Required uniform O(N) threshold: this basis fails its symbolic recurrence; no all-basis claim.')
    print('Failures: none in finite equations. Full audit:', args.output)


if __name__ == '__main__':
    main()
