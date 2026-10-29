#!/usr/bin/env python3
"""Exact finite checks for L119; write complete graphs/matrices/powers."""

import argparse
import json
from pathlib import Path


def action(row, matrix):
    result = 0
    while row:
        bit = row & -row
        result ^= matrix[bit.bit_length() - 1]
        row ^= bit
    return result


def multiply(left, right):
    return [action(row, right) for row in left]


def identity(n):
    return [1 << i for i in range(n)]


def product(r, operand, order):
    f = [f'f{i}' for i in range(r + 1)]
    vertices = ['s', *f, *operand['vertices'], 't']
    edges = [(f[i], f[i + 1], label)
             for i in range(r) for label in ('1', 'x')]
    edges += operand['edges']
    p, q = operand['roots']
    if order == 'FG':
        connectors = [('s', f[0], '1'), (f[-1], p, '1'), (q, 't', '1')]
        topo = ['s', *f, *operand['vertices'], 't']
    else:
        connectors = [('s', p, '1'), (q, f[0], '1'), (f[-1], 't', '1')]
        topo = ['s', *operand['vertices'], *f, 't']
    edges += connectors
    index = {v: i for i, v in enumerate(vertices)}
    position = {v: i for i, v in enumerate(topo)}
    assert all(position[u] < position[v] for u, v, _ in edges)
    n = len(vertices)
    c, d = [0] * n, [0] * n
    for u, v, label in edges:
        (c if label == '1' else d)[index[u]] ^= 1 << index[v]
    k, power = identity(n), identity(n)
    for _ in range(1, n):
        power = multiply(power, c)
        k = [a ^ b for a, b in zip(k, power)]
    assert not any(multiply(power, c))
    transition = multiply(d, k)
    powers = []
    power = identity(n)
    for _ in range(n):
        power = multiply(power, transition)
        powers.append(power)
        if not any(power):
            break
    assert not any(powers[-1])
    alpha, final = k[index['s']], index['t']
    row, coefficients = alpha, []
    for _ in range(n + 1):
        coefficients.append((row >> final) & 1)
        row = action(row, transition)
    return {
        'vertices': vertices, 'occurrences': edges, 'topological_order': topo,
        'C_rows': c, 'D_rows': d, 'K_rows': k, 'M_rows': transition,
        'alpha_bits': alpha, 'beta_rows': [int(i == final) for i in range(n)],
        'powers_M1_through_first_zero': powers, 'nilpotency_index': len(powers),
        'all_coefficients_through_dimension': coefficients,
        'g': n + 2 * len(edges),
    }


def cancelled_operand(m):
    chain = ['p', *[f'u{i}' for i in range(1, m + 1)]]
    return {
        'vertices': [*chain, 'q'], 'roots': ('p', 'q'),
        'edges': [(chain[i], chain[i + 1], 'x') for i in range(m)]
                 + [('p', 'q', '1'), (chain[-1], 'q', '1'),
                    (chain[-1], 'q', '1')],
    }


def predicted_rows(graph, r, branch_edges, first_product):
    vertices = graph['vertices']
    index = {v: i for i, v in enumerate(vertices)}
    rows = [0] * len(vertices)
    for i in range(r):
        targets = [f'f{j}' for j in range(i + 1, r + 1)] + ['t']
        if first_product:
            targets += ['p', 'q']
        for v in targets:
            rows[index[f'f{i}']] ^= 1 << index[v]
    for u, v in branch_edges:
        rows[index[u]] ^= 1 << index[v]
    return rows


def polynomial_bits(coefficients):
    return sum(bit << i for i, bit in enumerate(coefficients))


def make_case(name, r, operand, expected_indices, shift=0, m=None):
    a, b = product(r, operand, 'FG'), product(r, operand, 'GF')
    expected_polynomial = 1
    for _ in range(r):
        expected_polynomial ^= expected_polynomial << 1
    expected_polynomial <<= shift
    assert polynomial_bits(a['all_coefficients_through_dimension']) == expected_polynomial
    assert polynomial_bits(b['all_coefficients_through_dimension']) == expected_polynomial
    indices = [a['nilpotency_index'], b['nilpotency_index']]
    assert indices == list(expected_indices)
    checks = {'all_polynomial_coefficients_match': True,
              'expected_indices_match': True}
    witness = None
    if shift == 0:
        branch_edges = [(u, v) for u, v, label in operand['edges'] if label == 'x']
        assert a['M_rows'] == predicted_rows(a, r, branch_edges, True)
        assert b['M_rows'] == predicted_rows(b, r, branch_edges, False)
        index = {v: i for i, v in enumerate(a['vertices'])}
        alpha_names = ['s', *[f'f{i}' for i in range(r + 1)], 'p', 'q', 't']
        alpha = sum(1 << index[v] for v in alpha_names)
        assert a['alpha_bits'] == b['alpha_bits'] == alpha
        assert a['beta_rows'] == b['beta_rows']
        checks['all_transition_and_boundary_coordinates_match'] = True
    if m is not None:
        index = {v: i for i, v in enumerate(a['vertices'])}
        expected_power = [0] * len(index)
        expected_power[index['f0']] = 1 << index[f'u{m}']
        assert a['powers_M1_through_first_zero'][r + m - 1] == expected_power
        assert a['g'] + b['g'] == 10 * r + 6 * m + 34
        witness = {
            'A_exponent': r + m,
            'A_complete_power_rows': expected_power,
            'A_nonzero_coordinates': [['f0', f'u{m}']],
            'B_exponent': max(r, m) + 1,
            'B_complete_power_rows': b['powers_M1_through_first_zero'][-1],
        }
    gap = abs(indices[0] - indices[1])
    return {
        'name': name, 'r': r, 'm': m, 'A': a, 'B': b,
        'S': a['g'] + b['g'], 'checks': checks,
        'power_witness': witness,
        'elementary_arrow_requirement': {
            'required_minimum': gap, 'proposed_maximum': 5,
            'bound_satisfied': gap <= 5,
            'meaning': 'Necessary index bound only; no ordinary chain asserted.',
        },
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path,
                        default=Path('scripts/batched-incidence/output-536'))
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=False)
    fixture = {
        'vertices': ['p', 'u', 'v', 'q'], 'roots': ('p', 'q'),
        'edges': [('p', 'q', '1'), ('u', 'q', '1'), ('v', 'q', '1'),
                  ('p', 'u', 'x'), ('p', 'v', 'x')],
    }
    n = 8
    path = {
        'vertices': [f'h{i}' for i in range(n + 1)],
        'roots': ('h0', f'h{n}'),
        'edges': [(f'h{i}', f'h{i + 1}', 'x') for i in range(n)],
    }
    cases = [
        make_case('L117 required cancelling fixture', 6, fixture, (8, 7)),
        make_case('L118 required pure-x path r=N=8', 8, path, (17, 17), shift=8),
        make_case('L119 long cancelling branch r=m=6', 6,
                  cancelled_operand(6), (13, 7), m=6),
    ]
    certificate = {
        'description': 'Complete finite L119 replay; symbolic proof is canonical.',
        'matrix_encoding': 'Integer row bitsets; column j is bit j; order is vertices.',
        'cases': cases,
        'verification_failures': [],
        'result': 'Five elementary-factor arrows are impossible on case 2.',
        'qualification': 'No claim against ordinary scalar arrows without companions.',
    }
    destination = args.output / 'elementary-gap.json'
    destination.write_text(json.dumps(certificate, indent=2) + '\n')
    for case in cases:
        bound = case['elementary_arrow_requirement']
        print(f"{case['name']}: S={case['S']}; indices="
              f"{case['A']['nilpotency_index']},{case['B']['nilpotency_index']}; "
              f"required arrows>={bound['required_minimum']}, proposed<=5; "
              f"necessary bound {'PASS' if bound['bound_satisfied'] else 'FAIL'}")
    print(f'Verification failures: 0. Full certificate: {destination}')


if __name__ == '__main__':
    main()
