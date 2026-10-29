#!/usr/bin/env python3
"""Exact replay of the retained dyadic-sum template, including its failures."""

import argparse
import json
from pathlib import Path

from check_elementary_gap import action, multiply, product


def binomial_bits(exponent):
    value = 1
    for _ in range(exponent):
        value ^= value << 1
    return value


def raw_suffixes(graph):
    vertices = graph['vertices']
    index = {v: i for i, v in enumerate(vertices)}
    position = {v: i for i, v in enumerate(graph['topological_order'])}
    outgoing = {v: [] for v in vertices}
    for u, v, label in graph['occurrences']:
        assert position[u] < position[v]
        outgoing[u].append((v, label))
    values = [0] * len(vertices)
    for u in reversed(graph['topological_order']):
        value = int(u == 't')
        for v, label in outgoing[u]:
            value ^= values[index[v]] << int(label == 'x')
        values[index[u]] = value
    return values


def state_residuals(graph):
    n = len(graph['vertices'])
    column = sum(b << j for j, b in enumerate(graph['beta_rows']))
    values = [0] * n
    for degree in range(n):
        for i in range(n):
            values[i] |= ((column >> i) & 1) << degree
        column = sum(((row & column).bit_count() & 1) << i
                     for i, row in enumerate(graph['M_rows']))
    assert column == 0
    return values


def make_operand(k):
    n = 1 << k
    current = [f'b{j}' for j in range(n)]
    stages = [current[:]]
    gates, gate_edges = [], []
    for scale in range(k):
        previous = current
        current = previous[:]
        for j in range(n):
            if j & (1 << scale):
                name = f'v{scale}_{j}'
                children = [previous[j], previous[j - (1 << scale)]]
                assert children[0] != children[1]
                gate_edges.extend((name, child, '1') for child in children)
                gates.append({'name': name, 'scale': scale, 'j': j,
                              'children': children})
                current[j] = name
        stages.append(current[:])
    vertices = [f'p{j}' for j in range(n)]
    vertices += [gate['name'] for gate in reversed(gates)]
    vertices += [f'b{j}' for j in reversed(range(n))]
    edges = [(f'p{j}', current[j], 'x') for j in range(n)]
    edges += gate_edges
    edges += [(f'b{j}', f'b{j-1}', label)
              for j in range(1, n) for label in ('1', 'x')]
    return {'vertices': vertices, 'edges': edges,
            'roots': (f'p{n-1}', 'b0')}, stages, gates


def compare_arrow(source, target, rows):
    left = multiply(source['M_rows'], rows)
    right = multiply(rows, target['M_rows'])
    initial = action(source['alpha_bits'], rows)
    final = multiply(rows, target['beta_rows'])
    differences = [a ^ b for a, b in zip(left, right)]
    failed_rows = [source['vertices'][i] for i, row in enumerate(differences) if row]
    failures = [[source['vertices'][i], target['vertices'][j]]
                for i, row in enumerate(differences)
                for j in range(len(target['vertices'])) if (row >> j) & 1]
    return {
        'orientation': 'A -> Q', 'X_rows': rows,
        'support': sum(row.bit_count() for row in rows),
        'M_A_X_rows': left, 'X_M_Q_rows': right,
        'transition_difference_rows': differences,
        'all_failed_transition_rows': failed_rows,
        'all_failed_transition_coordinates': failures,
        'alpha_A_X_bits': initial, 'alpha_Q_bits': target['alpha_bits'],
        'X_beta_Q_rows': final, 'beta_A_rows': source['beta_rows'],
        'checks': {'initial': initial == target['alpha_bits'],
                   'final': final == source['beta_rows'],
                   'transition': left == right},
    }


def run_case(k):
    n = 1 << k
    path = {'vertices': [f'h{j}' for j in range(n + 1)],
            'edges': [(f'h{j}', f'h{j+1}', 'x') for j in range(n)],
            'roots': ('h0', f'h{n}')}
    a, b = product(n, path, 'FG'), product(n, path, 'GF')
    operand, stages, gates = make_operand(k)
    q = product(n, operand, 'FG')
    index = {v: i for i, v in enumerate(q['vertices'])}
    full = raw_suffixes(q)
    residual = state_residuals(q)
    q['full_raw_suffix_polynomial_bits'] = full
    q['right_closed_state_residual_polynomial_bits'] = residual
    stages_evidence = []
    for scale, registers in enumerate(stages):
        expected = []
        actual = []
        for j, name in enumerate(registers):
            low = j % (1 << scale)
            value = binomial_bits(j - low) << low
            expected.append(value)
            actual.append(full[index[name]])
        assert actual == expected
        stages_evidence.append({'scale': scale, 'register_vertices': registers,
                                'expected_bits': expected, 'actual_bits': actual})
    gate_values = []
    for gate in gates:
        low = gate['j'] % (1 << (gate['scale'] + 1))
        high = gate['j'] - low
        actual = full[index[gate['name']]]
        assert actual == binomial_bits(high) << low
        assert low.bit_length() - 1 == gate['scale']
        assert residual[index[gate['name']]] == 0
        gate.update({'order_at_zero': low, 'order_at_one': high,
                     'raw_suffix_bits': actual, 'right_closed_residual_bits': 0})
        gate_values.append(actual)
    base_values = [full[index[f'b{j}']] for j in range(n)]
    assert base_values == [binomial_bits(j) for j in range(n)]
    assert len(gates) == k * n // 2
    assert len(set(gate_values + base_values)) == len(gates) + n
    probes = [residual[index[f'p{j}']] for j in range(n)]
    assert probes == [1 << (j + 1) for j in range(n)]
    expected_polynomial = binomial_bits(n) << n
    for graph in (a, b, q):
        actual = sum(bit << j for j, bit in
                     enumerate(graph['all_coefficients_through_dimension']))
        assert actual == expected_polynomial
    assert full[index['s']] == expected_polynomial
    expected_alpha = sum(1 << index[v] for v in
                         ['s', *[f'f{i}' for i in range(n + 1)], f'p{n-1}'])
    assert q['alpha_bits'] == expected_alpha
    rename = {f'h{j}': f'p{n-j-1}' for j in range(n)}
    rename[f'h{n}'] = 'b0'
    rows = [1 << index[rename.get(v, v)] for v in a['vertices']]
    trial = compare_arrow(a, q, rows)
    assert trial['checks']['initial'] and trial['checks']['final']
    assert trial['support'] == 2 * n + 4
    assert trial['all_failed_transition_rows'] == [f'h{j}' for j in range(n - 1)]
    witness = None
    if n >= 2:
        source_row = a['vertices'].index(f'h{n-2}')
        lhs = trial['M_A_X_rows'][source_row]
        rhs = trial['X_M_Q_rows'][source_row]
        assert lhs == 1 << index['p0']
        assert rhs == (1 << index['v0_1']) ^ (1 << index['b1'])
        witness = {'source_row': f'h{n-2}', 'left_vertices': ['p0'],
                   'right_vertices': ['v0_1', 'b1'], 'left_bits': lhs,
                   'right_bits': rhs, 'equation_satisfied': False}
    else:
        assert trial['checks']['transition']
    s = a['g'] + b['g']
    assert s == 16 * n + 20
    assert len(q['vertices']) == 3 * n + k * n // 2 + 3
    assert len(q['occurrences']) == 5 * n + k * n + 1
    assert q['g'] == 13 * n + 5 * k * n // 2 + 5
    return {
        'k': k, 'N': n, 'A': a, 'B': b, 'Q': q,
        'all_dyadic_stages': stages_evidence, 'all_changed_gates': gates,
        'probe_state_residuals_bits': probes,
        'trial_first_arrow': trial, 'decisive_equation': witness,
        'ledger': {'S': s, 'changed_gate_vertices': len(gates),
                   'literal_Q_vertices': len(q['vertices']),
                   'literal_Q_edges': len(q['occurrences']),
                   'literal_Q_g': q['g'], 'twice_literal_Q_g': 2 * q['g'],
                   'coalesced_vertices_lower_bound': n + len(gates),
                   'twice_coalesced_graph_lower_bound': 2 * (n + len(gates)),
                   'trial_map_support': trial['support'],
                   'target': 'support + twice-counted graph size <= C*S for ONE universal C'},
        'qualification': 'Correct series is not an accepting arrow; no second map or complete chain is supplied.',
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path,
                        default=Path('scripts/batched-incidence/output-538'))
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=False)
    cases = [run_case(k) for k in range(6)]
    certificate = {
        'result': 'Retained dyadic sums have superlinear size; the probe first arrow fails for every N>=2.',
        'encoding': 'Matrix rows are integer bitsets; polynomial bit d is coefficient of z^d.',
        'cases': cases,
        'symbolic_bounds': {
            'N': '2^k', 'S': '16*N+20', 'changed_gates': 'k*N/2',
            'twice_literal_Q_size': '26*N+5*k*N+10',
            'twice_coalesced_graph_lower_bound': 'N*(k+2)',
            'coalesced_lower_bound_over_S': 'at least (k+2)/36; unbounded in k',
            'failed_first_arrow_row': 'h_(N-2): e_p0 != e_v(0,1)+e_b1, N>=2',
        },
        'verification_failures': [],
        'expected_template_failures': [
            'The initial and final equations pass, but N-1 transition rows fail for N>=2.',
            'Every fixed C fails asymptotically for the compulsory retained gate set.',
        ],
        'not_claimed': 'No general scalar-chain lower bound, impossibility of all XOR circuits, cancellation re-audit, or production receipt.',
    }
    destination = args.output / 'dyadic-sums.json'
    destination.write_text(json.dumps(certificate, indent=2) + '\n')
    for case in cases:
        ledger = case['ledger']
        failures = len(case['trial_first_arrow']['all_failed_transition_rows'])
        print(f"N={case['N']}: S={ledger['S']}, Q_g={ledger['literal_Q_g']}, "
              f"2Q_g={ledger['twice_literal_Q_g']}, changed gates={ledger['changed_gate_vertices']}; "
              f"boundaries PASS, failed transition rows={failures} (expected {case['N']-1})")
    print('Required: <= C*S for one universal C. Proved retained/coalesced lower ratio >= (k+2)/36 -> infinity.')
    print('All coefficients, equation coordinates, named gates and counts checked; verification failures: 0.')
    print(f'Full certificate, including every failed equation coordinate: {destination}')


if __name__ == '__main__':
    main()
