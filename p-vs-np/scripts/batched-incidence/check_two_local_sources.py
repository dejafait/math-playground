#!/usr/bin/env python3
"""Exhaust the approved weight-six local relations at N=4,8.

All coordinates, literal occurrences, closures, residual coefficients,
kernel generators, passing rows, rank witnesses and failed tests are saved.
Finite success is only a necessary test, never a source-graph construction.
"""

import argparse
import json
from collections import Counter
from pathlib import Path

from check_weight_filtration import act, endpoint, insert, pascal, rank


def reduce_row(row, pivots):
    for pivot in sorted(pivots, reverse=True):
        if (row >> pivot) & 1:
            row ^= pivots[pivot]
    return row


def spine(n):
    vertices = ['s'] + [f'd{i}' for i in range(2 * n)] + ['t']
    width = len(vertices)
    edges = [('s', 'd0', '1'), (f'd{n}', 't', '1')]
    edges += [(f'd{i}', f'd{i+1}', 'x') for i in range(2 * n - 1)]
    edges += [(f'd{2*n-1}', 't', 'x')]
    ix = {v: i for i, v in enumerate(vertices)}
    assert all(ix[u] < ix[v] for u, v, _ in edges)
    closure = [1 << i for i in range(width)]
    for i in reversed(range(width)):
        for u, v, label in edges:
            if ix[u] == i and label == '1':
                closure[i] ^= closure[ix[v]]
    m = [0] * width
    for u, v, label in edges:
        if label == 'x':
            m[ix[u]] ^= closure[ix[v]]
    beta = [int(v == 't') for v in vertices]
    column, residuals = beta[:], [0] * width
    for degree in range(width):
        for i, coefficient in enumerate(column):
            residuals[i] |= coefficient << degree
        column = [act(row, column) for row in m]
    assert not any(column)
    return {'vertices': vertices, 'topological_order': vertices,
            'occurrences': edges, 'K_rows': closure, 'M_rows': m,
            'alpha_bits': closure[0], 'beta_rows': beta,
            'all_residual_polynomial_bits': residuals,
            'g': width + 2 * len(edges)}


def verify_formulas(graph, n, name):
    """Compare every matrix row and residual with literal closed formulas."""
    vertices = graph['vertices']
    ix = {v: i for i, v in enumerate(vertices)}
    m = [0] * len(vertices)
    residuals = [0] * len(vertices)
    p = pascal(n)

    def bits(names):
        return sum(1 << ix[v] for v in names)

    if name in ('A', 'B'):
        for i in range(n):
            m[ix[f'f{i}']] = bits([f'f{j}' for j in range(i + 1, n + 1)]
                                  + (['h0'] if name == 'A' else ['t']))
            residuals[ix[f'f{i}']] = p[n - 1 - i] << (n + 1 if name == 'A' else 1)
        for i in range(n - 1):
            m[ix[f'h{i}']] = bits([f'h{i+1}'])
        m[ix[f'h{n-1}']] = bits([f'h{n}', 't']
                                     + ([] if name == 'A' else [f'f{i}' for i in range(n + 1)]))
        for i in range(n):
            residuals[ix[f'h{i}']] = ((1 << (n - i)) if name == 'A'
                                      else (1 << (n - i)) ^ (1 << (2 * n - i)))
        alpha = bits(['s'] + ([f'f{i}' for i in range(n + 1)] + ['h0']
                              if name == 'A' else ['h0']))
    else:
        for i in range(2 * n - 1):
            m[ix[f'd{i}']] = bits([f'd{i+1}'] + (['t'] if i == n - 1 else []))
        m[ix[f'd{2*n-1}']] = bits(['t'])
        for i in range(2 * n):
            residuals[ix[f'd{i}']] = ((1 << (n - i)) ^ (1 << (2 * n - i))
                                      if i < n else 1 << (2 * n - i))
        alpha = bits(['s', 'd0'])
    residuals[ix['t']] = 1
    assert graph['M_rows'] == m
    assert graph['all_residual_polynomial_bits'] == residuals
    assert graph['alpha_bits'] == alpha
    assert act(alpha, residuals) == (1 << n) ^ (1 << (2 * n))
    assert graph['g'] == (8 * n + 10 if name in ('A', 'B') else 6 * n + 6)


def kernel(columns):
    """Eliminate columns with coordinate witnesses; return the full kernel."""
    pivots, relations = {}, []
    for i, column in enumerate(columns):
        value, witness = column, 1 << i
        while value:
            pivot = value.bit_length() - 1
            if pivot not in pivots:
                pivots[pivot] = (value, witness)
                break
            old_value, old_witness = pivots[pivot]
            value ^= old_value
            witness ^= old_witness
        if value == 0:
            relations.append(witness)
    assert len(relations) + len(pivots) == len(columns)
    assert rank(relations) == len(relations)
    assert all(act(row, columns) == 0 for row in relations)
    return relations, len(pivots)


def local_test(left, right, n, label):
    width_left, width_right = len(left['vertices']), len(right['vertices'])
    width = width_left + width_right
    columns = left['all_residual_polynomial_bits'] + right['all_residual_polynomial_bits']
    shift = left['M_rows'] + [row << width_left for row in right['M_rows']]
    initial = left['alpha_bits'] | (right['alpha_bits'] << width_left)
    assert act(initial, columns) == 0
    basis, residual_rank = kernel(columns)
    assert residual_rank == 2 * n + 1
    assert len(basis) == 2 * n + 5
    rows_by_weight = [[] for _ in range(7)]
    histogram = [0] * (width + 1)
    coordinate_histogram = [0] * (width + 1)
    coordinate_witness = None
    coordinate_minimum = width + 1
    row = 0
    for index in range(1 << len(basis)):
        if index:
            row ^= basis[(index & -index).bit_length() - 1]
        weight = row.bit_count()
        histogram[weight] += 1
        if weight <= 6:
            rows_by_weight[weight].append(row)
        if label == 'AV' and (row >> left['vertices'].index('f0')) & 1:
            coordinate_histogram[weight] += 1
            if weight < coordinate_minimum:
                coordinate_minimum, coordinate_witness = weight, row
    assert sum(histogram) == 1 << len(basis)
    pivots, pool_basis, threshold_ranks = {}, [], []
    for rows in rows_by_weight:
        rows.sort()
        assert len(rows) == len(set(rows))
        for row in rows:
            assert row.bit_count() <= 6 and act(row, columns) == 0
            if insert(row, pivots):
                pool_basis.append(row)
        threshold_ranks.append(len(pivots))
    krylov, remainders = [], []
    row = initial
    for _ in range(max(width_left, width_right) + 1):
        krylov.append(row)
        remainders.append(reduce_row(row, pivots))
        row = act(row, shift)
    assert row == 0 and krylov[-1] == 0
    assert all(act(row, columns) == 0 for row in krylov)
    shifted_basis = [act(row, shift) for row in pool_basis]
    shift_remainders = [reduce_row(row, pivots) for row in shifted_basis]
    result = {'pair': label, 'N': n, 'coordinate_width': width,
              'coordinate_names': [label[0] + ':' + v for v in left['vertices']]
                                  + [label[1] + ':' + v for v in right['vertices']],
              'residual_columns_bits': columns, 'block_shift_rows': shift,
              'residual_rank': residual_rank, 'relation_dimension': len(basis),
              'complete_kernel_basis_bits': basis,
              'enumerated_relation_rows': sum(histogram),
              'required_relation_rows': 1 << len(basis),
              'complete_weight_histogram': histogram,
              'all_weight_at_most_six_rows_by_weight': rows_by_weight,
              'low_weight_counts': [len(rows) for rows in rows_by_weight],
              'low_weight_span_ranks': threshold_ranks,
              'low_weight_span_basis': pool_basis,
              'low_weight_span_pivots': {str(i): row for i, row in sorted(pivots.items())},
              'initial_pair': initial, 'initial_remainder': remainders[0],
              'initial_in_low_weight_span': remainders[0] == 0,
              'paired_krylov_rows': krylov, 'paired_krylov_span_remainders': remainders,
              'all_paired_krylov_rows_in_low_weight_span': not any(remainders),
              'shifted_pool_basis': shifted_basis, 'shifted_pool_basis_remainders': shift_remainders,
              'low_weight_span_is_invariant': not any(shift_remainders),
              'generator_cap': 8 * n,
              'source_graphs_constructed': False}
    if label == 'AV':
        bit = left['vertices'].index('f0')
        assert coordinate_witness is not None
        assert act(coordinate_witness, columns) == 0
        assert sum(coordinate_histogram) == (1 << (len(basis) - 1))
        result['A_f0_test'] = {
            'coordinate_index': bit, 'initial_coordinate': (initial >> bit) & 1,
            'full_coordinate_nonzero_weight_histogram': coordinate_histogram,
            'minimum_weight_with_coordinate_one': coordinate_minimum,
            'minimum_weight_witness': coordinate_witness,
            'pool_rows_with_coordinate_one': sum((row >> bit) & 1 for rows in rows_by_weight for row in rows),
            'coordinate_separates_initial_from_pool': coordinate_minimum > 6 and ((initial >> bit) & 1) == 1}
    return result


def full_parameter_test(n):
    p = pascal(n)
    table = []
    for r in range(1 << (n - 1), 1 << n):
        q = act(r, p)
        table.append({'r_bits': r, 'q_bits': q, 'r_weight': r.bit_count(),
                      'q_weight': q.bit_count(), 'row_weight_lower_bound': r.bit_count() + 2 * q.bit_count()})
    minimum = min(item['row_weight_lower_bound'] for item in table)
    return {'N': n, 'all_r_with_top_coordinate_one': table,
            'examined': len(table), 'required': 1 << (n - 1),
            'minimum_row_weight_lower_bound': minimum,
            'lower_bound_histogram': dict(sorted(Counter(item['row_weight_lower_bound'] for item in table).items()))}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    report = {'scope': 'Fixed original endpoints, pure-letter V, full paired coordinates over F2; necessary weight-six tests only.',
              'cases': [], 'fixture_failures': [], 'verification_failures': []}
    for n in (4, 8):
        a, v, b = endpoint(n, 'A'), spine(n), endpoint(n, 'B')
        for name, graph in (('A', a), ('V', v), ('B', b)):
            verify_formulas(graph, n, name)
        av, vb = local_test(a, v, n, 'AV'), local_test(v, b, n, 'VB')
        parameters = full_parameter_test(n)
        assert parameters['minimum_row_weight_lower_bound'] == av['A_f0_test']['minimum_weight_with_coordinate_one']
        report['cases'].append({'N': n, 'S': a['g'] + b['g'], 'A': a, 'V': v, 'B': b,
                                'local_tests': {'AV': av, 'VB': vb}, 'complete_A_f0_parameter_test': parameters})
        for test in (av, vb):
            if not test['initial_in_low_weight_span']:
                report['fixture_failures'].append({'N': n, 'pair': test['pair'],
                                                   'test': 'required initial pair outside complete weight-six span'})
    report['uniform_weight_six_fixture_rejected'] = bool(report['fixture_failures'])
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + '\n')
    for case in report['cases']:
        for label, test in case['local_tests'].items():
            print(f"N={case['N']} {label}: full rows {test['enumerated_relation_rows']}/{test['required_relation_rows']}; "
                  f"weight<=6 span {test['low_weight_span_ranks'][-1]}/{test['relation_dimension']}; "
                  f"initial in span={test['initial_in_low_weight_span']}; invariant={test['low_weight_span_is_invariant']}")
        item = case['local_tests']['AV']['A_f0_test']
        print(f"N={case['N']} AV: minimum row weight with A:f0=1 is {item['minimum_weight_with_coordinate_one']}; allowed <=6")
    print('Fixture failures:', report['fixture_failures'])
    print('Verification failures:', report['verification_failures'])
    print('Complete certificate:', args.output)


if __name__ == '__main__':
    main()
