#!/usr/bin/env python3
"""Exact balanced Pascal-product extension of the full residual basis.

Keep the original endpoint graphs. Save every basis/shift/map entry and
all literal occurrences. The support recurrence rejects this particular
linear-bound proposal; it says nothing universal about other bases.
"""

import argparse
import json
from pathlib import Path

from check_elementary_gap import action, multiply, product
from check_endpoint_spine import all_series, check_arrow, close_graph
from check_residual_relation import coordinate_solver, topological_order


def binomial_row(exponent):
    return sum(1 << i for i in range(exponent + 1)
               if i & exponent == i)


def split_index(index, high):
    bits = [1 << j for j in range(index.bit_length()) if (index >> j) & 1]
    weight = len(bits)
    # Choose the low-family tie so N=4 reproduces L124 exactly.
    count = min(weight, weight // 2 + 1) if high else weight // 2
    a = sum(bits[:count])
    return a, index ^ a


def support_recurrence(k):
    values = [5, 12]
    while len(values) <= k:
        values.append(2 * values[-1] + values[-2])
    return values[k]


def run_case(k):
    n = 1 << k
    path = {'vertices': [f'h{j}' for j in range(n + 1)],
            'edges': [(f'h{j}', f'h{j+1}', 'x') for j in range(n)],
            'roots': ('h0', f'h{n}')}
    a, b = product(n, path, 'FG'), product(n, path, 'GF')
    for graph in (a, b):
        all_series(graph)
    width = len(a['vertices'])
    index = {v: i for i, v in enumerate(a['vertices'])}
    assert a['vertices'] == b['vertices']

    def row(names):
        return sum(1 << index[name] for name in names)

    def polynomial_block(poly, block):
        return row([f'{block}{n-1-j}' for j in range(n) if (poly >> j) & 1])

    basis, labels, factors = [], [], []
    for endpoint in range(2):
        for vertex in ('s', f'f{n}', f'h{n}'):
            basis.append(row([vertex]) << (endpoint * width))
            labels.append(('A' if endpoint == 0 else 'B') + '_' + vertex)
    final_pair = row(['t']) | (row(['t']) << width)
    basis.append(final_pair)
    labels.append('final')
    for high in (False, True):
        for j in range(n):
            aa, bb = split_index(j, high)
            qz, qy = binomial_row(bb) << aa, binomial_row(aa) << bb
            assert aa & bb == 0 and aa + bb == j
            if high:
                ua = polynomial_block(qy, 'f') | polynomial_block(qz, 'h')
                ub = polynomial_block(qz, 'h')
            else:
                ua, ub = polynomial_block(qz, 'h'), polynomial_block(qy, 'f')
            basis.append(ua | (ub << width))
            labels.append(('H' if high else 'L') + str(j))
            factors.append({'label': labels[-1], 'j': j, 'a': aa, 'b': bb,
                            'q_z_coefficients': qz, 'q_y_coefficients': qy,
                            'weight': ua.bit_count() + ub.bit_count()})

    dimension = 2 * n + 7
    assert len(basis) == dimension
    solve = coordinate_solver(basis)
    residuals = a['all_residual_polynomial_bits'] + b['all_residual_polynomial_bits']
    assert all(action(value, residuals) == 0 for value in basis)
    # Independent residual rank witness: A's nonzero residuals have all
    # distinct degrees 0,...,2N, and each is monic at its displayed degree.
    degrees = sorted(value.bit_length() - 1
                     for value in a['all_residual_polynomial_bits'] if value)
    assert degrees == list(range(2 * n + 1))
    mask = (1 << width) - 1
    xa, xb = [v & mask for v in basis], [v >> width for v in basis]
    block_m = a['M_rows'] + [v << width for v in b['M_rows']]
    images = multiply(basis, block_m)
    shift = [solve(v) for v in images]
    shift_products = {
        'A_left': multiply(shift, xa), 'A_right': multiply(xa, a['M_rows']),
        'B_left': multiply(shift, xb), 'B_right': multiply(xb, b['M_rows'])}
    assert shift_products['A_left'] == shift_products['A_right']
    assert shift_products['B_left'] == shift_products['B_right']
    initial = solve(a['alpha_bits'] | (b['alpha_bits'] << width))
    da, db = multiply(xa, a['beta_rows']), multiply(xb, b['beta_rows'])
    assert da == db == [int(i == 6) for i in range(dimension)]
    assert action(initial, da) == 0
    order = topological_order(shift)
    assert order is not None
    # The degree proof gives an explicit fixed topological order as well.
    degree_order = list(range(dimension - 1, 6, -1)) + list(range(7))
    position = {i: pos for pos, i in enumerate(degree_order)}
    assert all(position[i] < position[j] for i in range(dimension)
               for j in range(dimension) if (shift[i] >> j) & 1)
    names = [f'q{i}' for i in range(dimension)]
    edges = [(names[i], names[j], 'x') for i in range(dimension)
             for j in range(dimension) if (shift[i] >> j) & 1]
    edges += [('s', names[i], '1') for i in range(dimension) if (initial >> i) & 1]
    edges.append((names[6], 't', '1'))
    q = close_graph(['s'] + names + ['t'], edges,
                    ['s'] + [names[i] for i in degree_order] + ['t'])
    all_series(q)
    final = 1 << index['t']
    ya = [0] + [value ^ (d * final) for value, d in zip(xa, da)] + [final]
    yb = [0] + [value ^ (d * final) for value, d in zip(xb, db)] + [final]
    arrows = {'A': check_arrow(q, a, ya, 'Q_to_A'),
              'B': check_arrow(q, b, yb, 'Q_to_B')}
    assert a['accepted_polynomial_bits'] == b['accepted_polynomial_bits'] == q['accepted_polynomial_bits']
    support = sum(v.bit_count() for v in basis)
    assert support == 8 + support_recurrence(k)
    assert arrows['A']['support'] + arrows['B']['support'] == support
    ledger = {
        'k': k, 'N': n, 'S': 16 * n + 20, 'dimension': dimension,
        'basis_support': support, 'required_recurrence_value': 8 + support_recurrence(k),
        'shift_support': sum(v.bit_count() for v in shift),
        'initial_support': initial.bit_count(), 'final_support': sum(da),
        'Q_vertices': len(q['vertices']), 'Q_occurrences': len(edges), 'g_Q': q['g'],
        'map_A_support': arrows['A']['support'], 'map_B_support': arrows['B']['support'],
        'expanded_map_support': arrows['A']['support'] + arrows['B']['support'],
        'required_asymptotic_threshold': 'One constant C times N (equivalently S) for all k. This basis fails because H_(k+2)=2H_(k+1)+H_k, H_0=5, H_1=12.',
        'equation_or_graph_failures': [],
        'linear_bound_failure': 'Proved symbolically for this basis only; finite values are not a proof of asymptotic failure.'}
    return {
        'A': a, 'B': b, 'factor_choices': factors, 'basis_labels': labels,
        'basis_rows': basis, 'basis_A_rows': xa, 'basis_B_rows': xb,
        'relation_residual_columns': residuals, 'A_residual_degree_rank_witness': degrees,
        'shift_images_original_coordinates': images, 'shift_rows': shift,
        'shift_products': shift_products, 'degree_topological_order': degree_order,
        'initial_coordinates': initial, 'common_final_functional': da,
        'initial_A_product': action(initial, xa), 'initial_B_product': action(initial, xb),
        'Q': q, 'arrows': arrows, 'ledger': ledger,
        'literal_table': [
            {'label': labels[i],
             'A': [v for j, v in enumerate(a['vertices']) if (xa[i] >> j) & 1],
             'B': [v for j, v in enumerate(b['vertices']) if (xb[i] >> j) & 1],
             'shift': [labels[j] for j in range(dimension) if (shift[i] >> j) & 1],
             'initial': (initial >> i) & 1, 'final': da[i]}
            for i in range(dimension)]}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--max-k', type=int, default=3)
    args = parser.parse_args()
    assert 0 <= args.max_k <= 6, 'bounded finite check only'
    args.output.mkdir(parents=True, exist_ok=False)
    cases = [run_case(k) for k in range(args.max_k + 1)]
    certificate = {'encoding': 'F2 integer bitsets in stored vertex/basis order.',
                   'low_family_split': 'a uses the floor(popcount(j)/2) lowest set bits',
                   'cases': cases, 'scope': 'Balanced Pascal-product basis only.'}
    path = args.output / 'residual-dyadic.json'
    path.write_text(json.dumps(certificate, indent=2) + '\n')
    print(json.dumps({'ledgers': [v['ledger'] for v in cases], 'certificate': str(path)}, indent=2))


if __name__ == '__main__':
    main()
