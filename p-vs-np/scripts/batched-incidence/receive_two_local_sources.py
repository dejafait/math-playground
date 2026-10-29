#!/usr/bin/env python3
"""Receive every weight<=6 row by independent coordinate-subset enumeration.

This does not import the producer or its helpers. Rebuild closure by matrix
powers and residuals by reverse topological substitution. The conceptual
scope and the symbolic lower bound still require a separate later audit.
"""

import argparse
import itertools
import json
from math import comb
from pathlib import Path


def xor_selected(mask, rows):
    answer = 0
    for i, row in enumerate(rows):
        if (mask >> i) & 1:
            answer ^= row
    return answer


def remainder(row, pivots):
    for bit in sorted(pivots):
        if (row >> bit) & 1:
            row ^= pivots[bit]
    return row


def add(row, pivots):
    row = remainder(row, pivots)
    if row:
        pivots[(row & -row).bit_length() - 1] = row


def matrix_rank(rows):
    pivots = {}
    for row in rows:
        add(row, pivots)
    return len(pivots)


def graph_receipt(graph, n, name):
    vertices = graph['vertices']
    if name in ('A', 'B'):
        f, h = [f'f{i}' for i in range(n + 1)], [f'h{i}' for i in range(n + 1)]
        expected_vertices = ['s'] + f + h + ['t']
        expected_edges = [(f[i], f[i + 1], label) for i in range(n) for label in ('1', 'x')]
        expected_edges += [(h[i], h[i + 1], 'x') for i in range(n)]
        chain = ['s', f[0], f[-1], h[0], h[-1], 't'] if name == 'A' else ['s', h[0], h[-1], f[0], f[-1], 't']
        expected_edges += [(chain[i], chain[i + 1], '1') for i in (0, 2, 4)]
    else:
        expected_vertices = ['s'] + [f'd{i}' for i in range(2 * n)] + ['t']
        expected_edges = [('s', 'd0', '1'), (f'd{n}', 't', '1')]
        expected_edges += [(f'd{i}', f'd{i+1}', 'x') for i in range(2 * n - 1)]
        expected_edges += [(f'd{2*n-1}', 't', 'x')]
    assert vertices == expected_vertices
    assert sorted(tuple(edge) for edge in graph['occurrences']) == sorted(expected_edges)
    width = len(vertices)
    ix = {v: i for i, v in enumerate(vertices)}
    topo = graph['topological_order']
    position = {v: i for i, v in enumerate(topo)}
    assert len(ix) == width and set(topo) == set(vertices) and len(topo) == width
    constant, letter = [0] * width, [0] * width
    for u, v, label in graph['occurrences']:
        assert label in ('1', 'x') and position[u] < position[v]
        rows = constant if label == '1' else letter
        rows[ix[u]] ^= 1 << ix[v]
    power = [1 << i for i in range(width)]
    closure = [0] * width
    for _ in range(width):
        closure = [a ^ b for a, b in zip(closure, power)]
        power = [xor_selected(row, constant) for row in power]
    assert not any(power)
    transition = [xor_selected(row, closure) for row in letter]
    residuals = [0] * width
    for v in reversed(topo):
        i = ix[v]
        assert all(position[v] < position[w] for j, w in enumerate(vertices) if (transition[i] >> j) & 1)
        residuals[i] = int(v == 't') ^ (xor_selected(transition[i], residuals) << 1)
    assert closure == graph['K_rows'] and transition == graph['M_rows']
    assert closure[ix['s']] == graph['alpha_bits']
    assert graph['beta_rows'] == [int(v == 't') for v in vertices]
    assert residuals == graph['all_residual_polynomial_bits']
    assert graph['g'] == width + 2 * len(graph['occurrences'])
    return {'vertices_checked': width, 'occurrences_checked': len(graph['occurrences']),
            'all_closure_rows_equal': True, 'all_transition_rows_equal': True,
            'all_residuals_and_boundaries_equal': True}


def receive_pair(test, left, right):
    columns = left['all_residual_polynomial_bits'] + right['all_residual_polynomial_bits']
    width, left_width = len(columns), len(left['vertices'])
    shift = left['M_rows'] + [row << left_width for row in right['M_rows']]
    initial = left['alpha_bits'] | (right['alpha_bits'] << left_width)
    assert columns == test['residual_columns_bits'] and shift == test['block_shift_rows']
    assert initial == test['initial_pair'] and test['coordinate_width'] == width
    kernel = test['complete_kernel_basis_bits']
    rank = matrix_rank(columns)
    assert rank == test['residual_rank']
    assert matrix_rank(kernel) == len(kernel) == width - rank == test['relation_dimension']
    assert all(0 <= row < (1 << width) and xor_selected(row, columns) == 0 for row in kernel)
    assert test['enumerated_relation_rows'] == test['required_relation_rows'] == 1 << len(kernel)
    pivots, ranks, counts, examined = {}, [], [], []
    coordinate_one_count = 0
    for weight in range(7):
        passing, count = [], 0
        for indices in itertools.combinations(range(width), weight):
            count += 1
            syndrome, row = 0, 0
            for i in indices:
                syndrome ^= columns[i]
                row |= 1 << i
            if syndrome == 0:
                passing.append(row)
        assert count == comb(width, weight)
        passing.sort()
        assert passing == test['all_weight_at_most_six_rows_by_weight'][weight]
        for row in passing:
            add(row, pivots)
        if test['pair'] == 'AV':
            coordinate_one_count += sum((row >> 1) & 1 for row in passing)
        ranks.append(len(pivots))
        counts.append(len(passing))
        examined.append(count)
    assert ranks == test['low_weight_span_ranks'] and counts == test['low_weight_counts']
    assert (remainder(initial, pivots) == 0) == test['initial_in_low_weight_span']
    pool_basis = test['low_weight_span_basis']
    assert matrix_rank(pool_basis) == len(pool_basis) == len(pivots)
    assert all(row.bit_count() <= 6 and xor_selected(row, columns) == 0 and remainder(row, pivots) == 0 for row in pool_basis)
    invariant = all(remainder(xor_selected(row, shift), pivots) == 0 for row in pool_basis)
    assert invariant == test['low_weight_span_is_invariant']
    row, krylov_in_pool = initial, True
    for saved in test['paired_krylov_rows']:
        assert row == saved and xor_selected(row, columns) == 0
        krylov_in_pool &= remainder(row, pivots) == 0
        row = xor_selected(row, shift)
    assert row == 0
    assert krylov_in_pool == test['all_paired_krylov_rows_in_low_weight_span']
    if test['pair'] == 'AV':
        item = test['A_f0_test']
        assert item['coordinate_index'] == 1 and left['vertices'][1] == 'f0'
        assert coordinate_one_count == item['pool_rows_with_coordinate_one']
        witness = item['minimum_weight_witness']
        assert 0 <= witness < (1 << width) and (witness >> 1) & 1
        assert xor_selected(witness, columns) == 0
        assert witness.bit_count() == item['minimum_weight_with_coordinate_one']
        assert ((initial >> 1) & 1) == item['initial_coordinate'] == 1
        assert item['coordinate_separates_initial_from_pool'] == (coordinate_one_count == 0)
    return {'pair': test['pair'], 'N': test['N'], 'coordinate_subsets_examined_by_weight': examined,
            'coordinate_subsets_examined': sum(examined),
            'coordinate_subsets_required': sum(comb(width, w) for w in range(7)),
            'all_complete_low_weight_lists_equal': True, 'counts': counts, 'ranks': ranks,
            'initial_in_span': remainder(initial, pivots) == 0,
            'span_invariant': invariant, 'krylov_in_span': krylov_in_pool}


def receive_parameters(case):
    n = case['N']
    item = case['complete_A_f0_parameter_test']
    powers, value = [], 1
    for _ in range(n):
        powers.append(value)
        value ^= value << 1
    expected = []
    products = []
    for r in range(1 << (n - 1), 1 << n):
        q = xor_selected(r, powers)
        a, b = r.bit_count(), q.bit_count()
        expected.append({'r_bits': r, 'q_bits': q, 'r_weight': a,
                         'q_weight': b, 'row_weight_lower_bound': a + 2 * b})
        products.append({'r_bits': r, 'actual_support_product': a * b, 'required_support_product': n})
        assert a * b >= n
    assert expected == item['all_r_with_top_coordinate_one']
    assert len(expected) == item['examined'] == item['required'] == 1 << (n - 1)
    minimum = min(row['row_weight_lower_bound'] for row in expected)
    assert minimum == item['minimum_row_weight_lower_bound']
    assert minimum == case['local_tests']['AV']['A_f0_test']['minimum_weight_with_coordinate_one']
    return {'N': n, 'examined': len(expected), 'required': 1 << (n - 1),
            'all_parameter_values_equal': True, 'minimum_weight_lower_bound': minimum,
            'every_support_product_comparison': products}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('certificate', type=Path)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    data = json.loads(args.certificate.read_text())
    receipt = {'input': str(args.certificate), 'cases': [], 'verification_failures': []}
    assert [case['N'] for case in data['cases']] == [4, 8]
    for case in data['cases']:
        n = case['N']
        received = {'N': n, 'graphs': {name: graph_receipt(case[name], n, name) for name in ('A', 'V', 'B')}}
        assert case['S'] == case['A']['g'] + case['B']['g'] == 16 * n + 20
        received['local_tests'] = [receive_pair(case['local_tests'][pair], case[pair[0]], case[pair[1]])
                                   for pair in ('AV', 'VB')]
        received['parameter_test'] = receive_parameters(case)
        receipt['cases'].append(received)
    assert data['uniform_weight_six_fixture_rejected']
    assert data['fixture_failures'] == [{'N': 8, 'pair': 'AV', 'test': 'required initial pair outside complete weight-six span'}]
    assert data['verification_failures'] == []
    receipt['fixture_failure_received'] = data['fixture_failures']
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(receipt, indent=2) + '\n')
    for case in receipt['cases']:
        for item in case['local_tests']:
            print(f"N={case['N']} {item['pair']}: coordinate subsets {item['coordinate_subsets_examined']}/{item['coordinate_subsets_required']}; "
                  f"all lists/ranks/initial/shift checks pass; initial in span={item['initial_in_span']}")
    print('Received fixture failure:', receipt['fixture_failure_received'])
    print('Verification failures:', receipt['verification_failures'])
    print('Complete receipt:', args.output)


if __name__ == '__main__':
    main()
