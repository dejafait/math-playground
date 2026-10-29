#!/usr/bin/env python3
"""Independent full finite replay of L124's certificate (no helper imports)."""

import argparse
import json
from pathlib import Path


def act(row, matrix):
    value = 0
    for i, entry in enumerate(matrix):
        if (row >> i) & 1:
            value ^= entry
    return value


def rank(rows):
    pivots = {}
    for value in rows:
        while value:
            i = value.bit_length() - 1
            if i not in pivots:
                pivots[i] = value
                break
            value ^= pivots[i]
    return len(pivots)


def reconstruct(graph):
    vertices = graph['vertices']
    ix = {v: i for i, v in enumerate(vertices)}
    position = {v: i for i, v in enumerate(graph['topological_order'])}
    assert set(position) == set(vertices) and len(position) == len(vertices)
    size = len(vertices)
    c, d = [0] * size, [0] * size
    for u, v, label in graph['occurrences']:
        assert position[u] < position[v] and label in ('1', 'x')
        (c if label == '1' else d)[ix[u]] ^= 1 << ix[v]
    # Matrix powers, independent of the generator's occurrence sweep.
    power = [1 << i for i in range(size)]
    closure = power[:]
    for _ in range(1, size):
        power = [act(row, c) for row in power]
        closure = [a ^ b for a, b in zip(closure, power)]
    assert not any(act(row, c) for row in power)
    m = [act(row, closure) for row in d]
    alpha = closure[ix['s']]
    beta = [int(v == 't') for v in vertices]
    for key, value in [('C_rows', c), ('D_rows', d), ('K_rows', closure),
                       ('M_rows', m), ('alpha_bits', alpha), ('beta_rows', beta)]:
        assert graph[key] == value, key
    residual, column = [0] * size, beta
    for degree in range(size + 1):
        residual = [a | (b << degree) for a, b in zip(residual, column)]
        column = [act(row, column) for row in m]
    assert not any(column)
    assert graph['all_residual_polynomial_bits'] == residual
    assert graph['g'] == size + 2 * len(graph['occurrences'])
    return m, alpha, beta, residual


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('certificate', type=Path)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    saved = json.loads(args.certificate.read_text())
    rebuilt = {name: reconstruct(saved[name]) for name in ('A', 'B', 'Q')}
    ma, aa, ba, ra = rebuilt['A']
    mb, ab, bb, rb = rebuilt['B']
    mq, aq, bq, _ = rebuilt['Q']
    basis = saved['chosen_basis_rows']
    expected_ranks = [0, 6, 8, 11, 14, 14] + [15] * 19
    assert saved['rank_by_weight_0_through_24'] == expected_ranks
    assert rank(ra + rb) == 9 and rank(basis) == 15
    all_vectors = []
    for mask in range(1 << 15):
        value = act(mask, basis)
        assert act(value, ra + rb) == 0
        assert mask < 1 << expected_ranks[value.bit_count()]
        all_vectors.append(value)
    assert len(set(all_vectors)) == 1 << 15
    assert sorted(all_vectors, key=lambda v: (v.bit_count(), v)) == saved['all_relation_vectors_sorted_by_weight_then_integer']
    assert sum(row.bit_count() for row in basis) == 37
    assert sum(15 - r for r in expected_ranks[:24]) == 37
    xa, xb = saved['basis_A_rows'], saved['basis_B_rows']
    assert basis == [u | (v << 12) for u, v in zip(xa, xb)]
    t, c, d = (saved['shift_coordinate_rows'], saved['initial_coordinates_bits'],
               saved['common_final_functional_rows'])
    assert [act(row, xa) for row in t] == [act(row, ma) for row in xa]
    assert [act(row, xb) for row in t] == [act(row, mb) for row in xb]
    assert act(c, xa) == aa and act(c, xb) == ab
    assert [act(row, ba) for row in xa] == [act(row, bb) for row in xb] == d
    pos = {v: i for i, v in enumerate(saved['direct_shift_topological_order'])}
    assert set(pos) == set(range(15))
    assert all(pos[i] < pos[j] for i in range(15) for j in range(15)
               if (t[i] >> j) & 1)
    arrow_evidence = {}
    for name, m, alpha, beta in [('A', ma, aa, ba), ('B', mb, ab, bb)]:
        y = saved['arrows'][name]['X_rows']
        left, right = [act(row, y) for row in mq], [act(row, m) for row in y]
        assert left == right
        assert act(aq, y) == alpha
        assert [act(row, beta) for row in y] == bq
        arrow_evidence[name] = {'transition_left': left, 'transition_right': right,
                                'initial_actual': act(aq, y), 'initial_required': alpha,
                                'final_actual': [act(row, beta) for row in y],
                                'final_required': bq,
                                'support': sum(row.bit_count() for row in y)}
    pairs = [u | (v << 12) for u, v in zip(saved['arrows']['A']['X_rows'], saved['arrows']['B']['X_rows'])]
    assert rank(pairs) == 15 and all(act(row, ra + rb) == 0 for row in pairs)
    ledger = saved['ledger']
    assert ledger['Q_vertices'] == 17 and ledger['Q_occurrences'] == 29
    assert ledger['g_Q'] == 75 and ledger['two_g_Q'] == 150
    assert ledger['total_expanded_chain_support'] == sum(e['support'] for e in arrow_evidence.values()) == 37
    report = {'result': 'PASS', 'all_masks_checked': 32768,
              'dimension_actual_required': [15, 15],
              'minimum_basis_support_actual_required': [37, 37],
              'weight_threshold_ranks': expected_ranks, 'arrows': arrow_evidence,
              'full_relation_image_rank': rank(pairs), 'ledger': ledger,
              'failures': [], 'certificate': str(args.certificate),
              'qualification': 'Finite N=4 replay only; no uniform asymptotic bound.'}
    args.output.write_text(json.dumps(report, indent=2) + '\n')
    print('PASS: all 32768 vectors; full rank 15/15; minimum basis support 37/37.')
    print('PASS: both full arrow equations and boundaries; received rank 15/15.')
    print('Finite costs: S=84; Q=17 vertices/29 occurrences; 2g(Q)=150; maps=37.')
    print('Required uniform O(N) threshold: NOT ESTABLISHED. Failures: none.')
    print('Full audit:', args.output)


if __name__ == '__main__':
    main()
