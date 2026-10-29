#!/usr/bin/env python3
"""One complete N=4 full-relation basis/shift/realization diagnostic.

Enumerates all relation vectors, not candidate subsets. Integer bit j is
column j. Every scalar entry and graph occurrence is expanded and charged.
No asymptotic sparsity, novelty or optimal realization claim is made.
"""

import argparse
import json
from pathlib import Path

from check_elementary_gap import action, multiply, product
from check_endpoint_spine import all_series, check_arrow, close_graph
from check_cross_coupled import row_kernel


def independent_insert(value, pivots):
    while value:
        pivot = value.bit_length() - 1
        if pivot not in pivots:
            pivots[pivot] = value
            return True
        value ^= pivots[pivot]
    return False


def coordinate_solver(basis):
    pivots = {}
    for i, row in enumerate(basis):
        value, coordinates = row, 1 << i
        while value:
            pivot = value.bit_length() - 1
            if pivot not in pivots:
                pivots[pivot] = (value, coordinates)
                break
            old, old_coordinates = pivots[pivot]
            value ^= old
            coordinates ^= old_coordinates
        assert value, 'dependent chosen basis'

    def solve(value):
        original, coordinates = value, 0
        while value:
            pivot = value.bit_length() - 1
            assert pivot in pivots, ('not in full relation', original)
            old, old_coordinates = pivots[pivot]
            value ^= old
            coordinates ^= old_coordinates
        assert action(coordinates, basis) == original
        return coordinates
    return solve


def topological_order(rows):
    size = len(rows)
    indegree = [sum((row >> j) & 1 for row in rows) for j in range(size)]
    todo = [i for i, degree in enumerate(indegree) if degree == 0]
    order = []
    while todo:
        i = todo.pop(0)
        order.append(i)
        for j in range(size):
            if (rows[i] >> j) & 1:
                indegree[j] -= 1
                if indegree[j] == 0:
                    todo.append(j)
    return order if len(order) == size else None


def run():
    n = 4
    path = {'vertices': [f'h{j}' for j in range(n + 1)],
            'edges': [(f'h{j}', f'h{j+1}', 'x') for j in range(n)],
            'roots': ('h0', f'h{n}')}
    a, b = product(n, path, 'FG'), product(n, path, 'GF')
    for graph in (a, b):
        all_series(graph)
    size_a, size_b = len(a['vertices']), len(b['vertices'])
    residuals = (a['all_residual_polynomial_bits']
                 + b['all_residual_polynomial_bits'])
    rank, seed = row_kernel(residuals)
    dimension = len(seed)
    assert (size_a, size_b, rank, dimension) == (12, 12, 9, 15)
    vectors = [action(mask, seed) for mask in range(1 << dimension)]
    assert len(set(vectors)) == 1 << dimension
    assert all(action(row, residuals) == 0 for row in vectors)
    vectors.sort(key=lambda row: (row.bit_count(), row))
    basis, pivots, rank_by_weight = [], {}, []
    for weight in range(size_a + size_b + 1):
        for row in vectors:
            if row.bit_count() == weight and independent_insert(row, pivots):
                basis.append(row)
        rank_by_weight.append(len(basis))
    assert len(basis) == dimension
    # Every weight-threshold span is saturated by this greedy basis.
    for weight, required_rank in enumerate(rank_by_weight):
        threshold_pivots = {}
        for row in vectors:
            if row.bit_count() <= weight:
                independent_insert(row, threshold_pivots)
        assert len(threshold_pivots) == required_rank
        assert sum(row.bit_count() <= weight for row in basis) == required_rank
    minimum = sum(dimension - r for r in rank_by_weight)
    assert sum(row.bit_count() for row in basis) == minimum
    solve = coordinate_solver(basis)
    mask_a = (1 << size_a) - 1
    xa, xb = [row & mask_a for row in basis], [row >> size_a for row in basis]
    combined_m = a['M_rows'] + [row << size_a for row in b['M_rows']]
    images = multiply(basis, combined_m)
    transition = [solve(row) for row in images]
    assert multiply(transition, xa) == multiply(xa, a['M_rows'])
    assert multiply(transition, xb) == multiply(xb, b['M_rows'])
    paired_initial = a['alpha_bits'] | (b['alpha_bits'] << size_a)
    initial = solve(paired_initial)
    da, db = multiply(xa, a['beta_rows']), multiply(xb, b['beta_rows'])
    assert da == db
    assert action(initial, xa) == a['alpha_bits']
    assert action(initial, xb) == b['alpha_bits']
    assert action(initial, da) == 0
    # Save every nilpotent-orbit row. L is first zero image of the full basis.
    orbits, current = [], basis
    for _ in range(size_a + size_b + 1):
        orbits.append(current)
        if not any(current):
            break
        current = multiply(current, combined_m)
    assert not any(orbits[-1])
    length = len(orbits) - 1
    direct_order = topological_order(transition)
    # The actual N=4 shift is acyclic: use its literal adjacency, not the
    # larger orbit fallback preserved in output-542's initial receipt.
    assert direct_order is not None, 'chosen shift has no direct DAG realization'
    names = [f'q{i}' for i in range(dimension)]
    vertices = ['s'] + names + ['t']
    topo = ['s'] + [names[i] for i in direct_order] + ['t']
    edges = [(names[i], names[j], 'x') for i in range(dimension)
             for j in range(dimension) if (transition[i] >> j) & 1]
    edges += [('s', names[i], '1') for i in range(dimension)
              if (initial >> i) & 1]
    output_taps = []
    final_a, final_b = a['vertices'].index('t'), b['vertices'].index('t')
    maps_a, maps_b = [0], [0]
    for i, row in enumerate(basis):
        ua, ub = row & mask_a, row >> size_a
        output = (ua >> final_a) & 1
        assert output == ((ub >> final_b) & 1)
        if output:
            edges.append((names[i], 't', '1'))
            output_taps.append(i)
        # A nonfinal right-closed graph state has final value zero.
        maps_a.append(ua ^ (output << final_a))
        maps_b.append(ub ^ (output << final_b))
    maps_a.append(1 << final_a)
    maps_b.append(1 << final_b)
    q = close_graph(vertices, edges, topo)
    all_series(q)
    arrows = {
        'A': check_arrow(q, a, maps_a, 'Q_to_A'),
        'B': check_arrow(q, b, maps_b, 'Q_to_B'),
    }
    assert q['accepted_polynomial_bits'] == a['accepted_polynomial_bits'] == b['accepted_polynomial_bits']
    received_pairs = [u | (v << size_a) for u, v in zip(maps_a, maps_b)]
    received_pivots = {}
    for row in received_pairs:
        assert action(row, residuals) == 0
        independent_insert(row, received_pivots)
    assert len(received_pivots) == dimension
    support = sum(row.bit_count() for row in basis)
    ledger = {
        'N': n, 'S': a['g'] + b['g'], 'relation_dimension': dimension,
        'minimum_basis_support': minimum, 'basis_support': support,
        'shift_support': sum(row.bit_count() for row in transition),
        'initial_coordinate_support': initial.bit_count(),
        'final_functional_support': sum(da), 'orbit_length': length,
        'Q_vertices': len(vertices),
        'Q_x_occurrences': sum(row.bit_count() for row in transition),
        'Q_initial_constant_occurrences': initial.bit_count(),
        'Q_final_constant_occurrences': len(output_taps),
        'Q_occurrences': len(edges), 'g_Q': q['g'],
        'Q_to_A_support': arrows['A']['support'],
        'Q_to_B_support': arrows['B']['support'],
        'total_expanded_chain_support': arrows['A']['support'] + arrows['B']['support'],
        'two_g_Q': 2 * q['g'],
        'required_asymptotic_threshold': 'One constant C for every dyadic N, simultaneously bounding generator support, occurrences and all expanded maps by C*(16*N+20). No C or uniform mechanism is established.',
        'failures': [],
    }
    return {
        'encoding': 'F2 integer row bitsets; endpoint blocks use their saved vertex orders; basis/shift coordinates use chosen_basis_rows order.',
        'A': a, 'B': b, 'relation_residual_polynomial_bits': residuals,
        'relation_rank': rank, 'seed_kernel_basis_rows': seed,
        'all_relation_vectors_sorted_by_weight_then_integer': vectors,
        'rank_by_weight_0_through_24': rank_by_weight,
        'chosen_basis_rows': basis, 'basis_A_rows': xa, 'basis_B_rows': xb,
        'shift_image_original_coordinate_rows': images,
        'shift_coordinate_rows': transition,
        'shift_A_left_rows': multiply(transition, xa),
        'shift_A_right_rows': multiply(xa, a['M_rows']),
        'shift_B_left_rows': multiply(transition, xb),
        'shift_B_right_rows': multiply(xb, b['M_rows']),
        'initial_coordinates_bits': initial,
        'initial_A_product_bits': action(initial, xa),
        'initial_B_product_bits': action(initial, xb),
        'common_final_functional_rows': da,
        'direct_shift_topological_order': direct_order,
        'orbit_original_coordinate_rows_including_terminal_zero': orbits,
        'basis_literal_rows': [
            {'generator': i,
             'A': [v for j, v in enumerate(a['vertices']) if (xa[i] >> j) & 1],
             'B': [v for j, v in enumerate(b['vertices']) if (xb[i] >> j) & 1],
             'shift_targets': [j for j in range(dimension) if (transition[i] >> j) & 1],
             'initial_coordinate': (initial >> i) & 1, 'final_value': da[i]}
            for i in range(dimension)],
        'Q': q, 'Q_output_taps_generators': output_taps,
        'arrows': arrows, 'received_relation_rank': len(received_pivots),
        'ledger': ledger,
        'qualification': 'Complete finite discriminant and finite minimum-support basis only. The direct N=4 shift graph is acyclic. No uniform O(N) construction or all-basis obstruction is established.',
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path,
                        default=Path('scripts/batched-incidence/output-542-direct'))
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=False)
    result = run()
    destination = args.output / 'residual-relation.json'
    destination.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result['ledger'], indent=2))
    print('direct shift acyclic:', result['direct_shift_topological_order'] is not None)
    print('full certificate:', destination)


if __name__ == '__main__':
    main()
