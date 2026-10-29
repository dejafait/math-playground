#!/usr/bin/env python3
"""Exact diagnostic for one endpoint-only parallel/spine lift.

All graph occurrences, full maps and every equation product are saved.
The finite map construction is diagnostic; every expanded scalar entry
is charged. It supplies no coordinate oracle or linear-support algorithm.
"""

import argparse
import json
from pathlib import Path

from check_elementary_gap import action, identity, multiply, product


def close_graph(vertices, edges, topo):
    index = {v: i for i, v in enumerate(vertices)}
    position = {v: i for i, v in enumerate(topo)}
    assert set(topo) == set(vertices) and len(topo) == len(vertices)
    assert all(position[u] < position[v] for u, v, _ in edges)
    n = len(vertices)
    c, d = [0] * n, [0] * n
    for u, v, label in edges:
        assert label in ('1', 'x')
        (c if label == '1' else d)[index[u]] ^= 1 << index[v]
    # Constant closure by the literal topological occurrence sweep.
    outgoing = {v: [] for v in vertices}
    for u, v, label in edges:
        if label == '1':
            outgoing[u].append(v)
    k = []
    for initial in vertices:
        row = 1 << index[initial]
        for u in topo:
            for v in outgoing[u]:
                if (row >> index[u]) & 1:
                    row ^= 1 << index[v]
        k.append(row)
    w = [row ^ (1 << i) for i, row in enumerate(c)]
    assert multiply(w, k) == multiply(k, w) == identity(n)
    m = multiply(d, k)
    graph = {
        'vertices': vertices, 'occurrences': edges, 'topological_order': topo,
        'C_rows': c, 'D_rows': d, 'K_rows': k, 'M_rows': m,
        'alpha_bits': k[index['s']],
        'beta_rows': [int(v == 't') for v in vertices],
        'g': n + 2 * len(edges),
    }
    return graph


def endpoint_spine(n, a, b):
    # Two full endpoint branches share just their boundary vertices.
    def rename(name, branch):
        return name if name in ('s', 't') else branch + '_' + name

    vertices = ['s']
    edges, topo = [], ['s']
    for branch, graph in (('a', a), ('b', b)):
        vertices += [rename(v, branch) for v in graph['vertices']
                     if v not in ('s', 't')]
        topo += [rename(v, branch) for v in graph['topological_order']
                 if v not in ('s', 't')]
        edges += [(rename(u, branch), rename(v, branch), label)
                  for u, v, label in graph['occurrences']]
    spine = [f'd{j}' for j in range(2 * n)]
    vertices += spine + ['t']
    topo += spine + ['t']
    edges += [(spine[j], spine[j + 1], 'x') for j in range(2 * n - 1)]
    edges += [(spine[-1], 't', 'x'), ('s', spine[0], '1'),
              (spine[n], 't', '1')]
    return close_graph(vertices, edges, topo)


def all_series(graph):
    size = len(graph['vertices'])
    final = graph['vertices'].index('t')
    prefix = [0] * size
    reachable, row = [], graph['alpha_bits']
    residual, column = [0] * size, 1 << final
    for degree in range(size + 1):
        reachable.append(row)
        for i in range(size):
            prefix[i] |= ((row >> i) & 1) << degree
            residual[i] |= ((column >> i) & 1) << degree
        row = action(row, graph['M_rows'])
        column = sum(((mrow & column).bit_count() & 1) << i
                     for i, mrow in enumerate(graph['M_rows']))
    assert row == column == 0
    graph['all_prefix_polynomial_bits'] = prefix
    graph['all_residual_polynomial_bits'] = residual
    graph['all_initial_orbit_rows'] = reachable
    graph['accepted_polynomial_bits'] = prefix[final]


def finite_trial_rows(source, target, n):
    # Explicit finite bit operations on already saved incidence actions.
    # No sparsity or asymptotic construction claim is made for these rows.
    orbit = target['all_initial_orbit_rows']
    monomials = []
    for degree in range(2 * n + 1):
        row = 0
        for j in range(degree // n + 1):
            row ^= orbit[2 * n - degree + j * n]
        monomials.append(row)
    return [action(poly, monomials)
            for poly in source['all_residual_polynomial_bits']]


def check_arrow(source, target, rows, orientation):
    left, right = multiply(source['M_rows'], rows), multiply(rows, target['M_rows'])
    initial = action(source['alpha_bits'], rows)
    final = multiply(rows, target['beta_rows'])
    failures = []
    for i, (a, b) in enumerate(zip(left, right)):
        for j in range(len(target['vertices'])):
            if ((a ^ b) >> j) & 1:
                failures.append([source['vertices'][i], target['vertices'][j]])
    checks = {
        'initial': initial == target['alpha_bits'],
        'transition': left == right,
        'final': final == source['beta_rows'],
    }
    assert all(checks.values()), (orientation, checks, failures)
    return {
        'orientation': orientation, 'X_rows': rows,
        'literal_map_rows': {
            source['vertices'][i]: [v for j, v in enumerate(target['vertices'])
                                    if (row >> j) & 1]
            for i, row in enumerate(rows)},
        'support': sum(row.bit_count() for row in rows),
        'left_transition_rows': left, 'right_transition_rows': right,
        'initial_product_bits': initial, 'required_initial_bits': target['alpha_bits'],
        'final_product_rows': final, 'required_final_rows': source['beta_rows'],
        'checks': checks, 'failed_transition_coordinates': failures,
    }


def binary_binomial(j, i):
    return int((i & j) == i)


def run_case(k):
    n = 1 << k
    path = {
        'vertices': [f'h{j}' for j in range(n + 1)],
        'edges': [(f'h{j}', f'h{j + 1}', 'x') for j in range(n)],
        'roots': ('h0', f'h{n}'),
    }
    a, b = product(n, path, 'FG'), product(n, path, 'GF')
    q = endpoint_spine(n, a, b)
    for graph in (a, b, q):
        all_series(graph)
        assert graph['accepted_polynomial_bits'] == (1 << n) ^ (1 << (2 * n))
    assert a['g'] + b['g'] == 16 * n + 20
    assert len(q['vertices']) == 6 * n + 6
    assert len(q['occurrences']) == 8 * n + 8
    assert q['g'] == 22 * n + 22
    arrows = {}
    for name, source, target in (('A_to_Q', a, q), ('B_to_Q', b, q),
                                 ('Q_to_A', q, a)):
        arrows[name] = check_arrow(source, target,
                                   finite_trial_rows(source, target, n), name)
    ai = {v: i for i, v in enumerate(a['vertices'])}
    qi = {v: i for i, v in enumerate(q['vertices'])}
    incoming = arrows['A_to_Q']['X_rows']
    outgoing = arrows['Q_to_A']['X_rows']
    forced_incoming = []
    for branch in ('b_h', 'd'):
        for j in range(n):
            for i in range(1, n):
                actual = (incoming[ai[f'f{i}']] >> qi[f'{branch}{j}']) & 1
                required = binary_binomial(j, i)
                assert actual == required
                forced_incoming.append([f'f{i}', f'{branch}{j}', actual, required])
    forced_outgoing = []
    for i in range(n):
        for j in range(n):
            actual = (outgoing[qi[f'b_f{i}']] >> ai[f'h{n - 1 - j}']) & 1
            required = binary_binomial(n - 1 - i, j)
            assert actual == required
            forced_outgoing.append([f'b_f{i}', f'h{n - 1 - j}', actual, required])
    in_bound = sum(row[3] for row in forced_incoming)
    out_bound = sum(row[3] for row in forced_outgoing)
    assert in_bound == 2 * (3 ** k - n)
    assert out_bound == 3 ** k
    support = arrows['A_to_Q']['support'] + arrows['B_to_Q']['support']
    return {
        'k': k, 'N': n, 'A': a, 'B': b, 'Q': q, 'arrows': arrows,
        'complete_forced_incoming_rectangle': forced_incoming,
        'complete_forced_outgoing_rectangle': forced_outgoing,
        'ledger': {
            'S': a['g'] + b['g'], 'Q_vertices': len(q['vertices']),
            'Q_edges': len(q['occurrences']), 'twice_Q_g': 2 * q['g'],
            'incoming_support_lower_bound': in_bound,
            'outgoing_support_lower_bound': out_bound,
            'explicit_common_target_support': support,
            'explicit_common_target_charge': support + 2 * q['g'],
            'required_asymptotic_bound': 'support + 2g(Q) <= C*S, ONE universal C',
        },
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path,
                        default=Path('scripts/batched-incidence/output-539'))
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=False)
    cases = [run_case(k) for k in range(5)]
    result = {
        'result': 'The parallel endpoint/spine lift has valid finite maps but forced superlinear support in either orientation next to A.',
        'encoding': 'Matrix row bit j is column j in vertices; polynomial bit d is coefficient of z^d.',
        'cases': cases,
        'symbolic_bounds': {
            'N': '2^k', 'S': '16*2^k+20', 'twice_Q_g': '44*2^k+44',
            'A_to_Q_support': '>=2*(3^k-2^k)',
            'Q_to_A_support': '>=3^k',
            'either_orientation_ratio': '>= (3/2)^k/36 for k>=2; unbounded',
        },
        'verification_failures': [],
        'qualification': 'Finite checks do not prove the universal bounds; their canonical symbolic proof is required. No arbitrary-chain obstruction is asserted.',
    }
    destination = args.output / 'endpoint-spine.json'
    destination.write_text(json.dumps(result, indent=2) + '\n')
    for case in cases:
        ledger = case['ledger']
        print(f"N={case['N']}: all 3 equations pass for A->Q, B->Q, Q->A; "
              f"S={ledger['S']}, 2g(Q)={ledger['twice_Q_g']}, "
              f"actual common-target charge={ledger['explicit_common_target_charge']}, "
              f"forced A->Q/Q->A supports={ledger['incoming_support_lower_bound']}/"
              f"{ledger['outgoing_support_lower_bound']}")
    print('Required: one universal C; symbolic forced-support/S is unbounded. Failures: none.')
    print(f'Full certificate: {destination}')


if __name__ == '__main__':
    main()
