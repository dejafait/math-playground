#!/usr/bin/env python3
"""Exact finite replay of L120; retain full occurrences, maps and checks."""

import argparse
import json
from pathlib import Path

from check_elementary_gap import action, cancelled_operand, identity, multiply, product


def representation(vertices, occurrences, source, sink):
    index = {v: i for i, v in enumerate(vertices)}
    n = len(vertices)
    c, d = [0] * n, [0] * n
    for u, v, label in occurrences:
        assert index[u] < index[v], (u, v)
        assert label in ('1', 'x')
        (c if label == '1' else d)[index[u]] ^= 1 << index[v]
    k, power = identity(n), identity(n)
    for _ in range(1, n):
        power = multiply(power, c)
        k = [a ^ b for a, b in zip(k, power)]
    assert not any(multiply(power, c))
    m = multiply(d, k)
    beta = [int(v == sink) for v in vertices]
    column, residuals = beta[:], [0] * n
    for degree in range(n):
        residuals = [p | (b << degree) for p, b in zip(residuals, column)]
        column = [(row & sum(b << j for j, b in enumerate(column))).bit_count() & 1
                  for row in m]
    assert not any(column)
    return {
        'vertices': vertices, 'occurrences': occurrences,
        'source': source, 'sink': sink,
        'C_rows': c, 'D_rows': d, 'K_rows': k, 'M_rows': m,
        'alpha_bits': k[index[source]], 'beta_rows': beta,
        'state_residual_polynomial_bits': residuals,
        'g': n + 2 * len(occurrences),
    }


def arrow(source, target, rows, require_initial=True):
    lhs = multiply(source['M_rows'], rows)
    rhs = multiply(rows, target['M_rows'])
    initial = action(source['alpha_bits'], rows)
    final = multiply(rows, target['beta_rows'])
    checks = {
        'transition_all_coordinates': lhs == rhs,
        'final_all_coordinates': final == source['beta_rows'],
        'initial_all_coordinates': initial == target['alpha_bits'],
        'initial_equation_required': require_initial,
    }
    assert checks['transition_all_coordinates'] and checks['final_all_coordinates']
    assert checks['initial_all_coordinates'] or not require_initial
    return {
        'rows': rows, 'support': sum(row.bit_count() for row in rows),
        'M_source_X_rows': lhs, 'X_M_target_rows': rhs,
        'alpha_source_X_bits': initial, 'target_alpha_bits': target['alpha_bits'],
        'X_beta_target_rows': final, 'source_beta_rows': source['beta_rows'],
        'checks': checks,
    }


def unit_polynomial(r):
    p = 1
    for _ in range(r):
        p ^= p << 1
    return p


def cancellation_case(name, r, operand):
    a, b = product(r, operand, 'FG'), product(r, operand, 'GF')
    vertices = ['s', *[f'f{i}' for i in range(r + 1)], 't']
    occurrences = [('s', 'f0', '1')]
    occurrences += [(f'f{i}', f'f{i+1}', label)
                    for i in range(r) for label in ('1', 'x')]
    occurrences += [(f'f{r}', 't', '1')]
    h = representation(vertices, occurrences, 's', 't')
    index = {v: i for i, v in enumerate(vertices)}
    maps = [arrow(g, h, [1 << index[v] if v in index else 0
                        for v in g['vertices']]) for g in (a, b)]
    s = a['g'] + b['g']
    charge = sum(x['support'] for x in maps) + 2 * h['g']
    assert charge == 12 * r + 20 <= 2 * s
    return {
        'name': name, 'r': r, 'A': a, 'B': b, 'common_H': h,
        'arrows_A_to_H_B_to_H': maps, 'S': s,
        'support_plus_twice_intermediate': charge, 'proved_upper_bound_2S': 2 * s,
    }


def placement(r, n, i):
    # Omit zero-layer factors, so i=r and i=0 are the ORIGINAL endpoints.
    factors = []
    if i:
        factors.append(([f'l{k}' for k in range(i + 1)],
                        [(f'l{k}', f'l{k+1}', label)
                         for k in range(i) for label in ('1', 'x')]))
    factors.append(([f'h{j}' for j in range(n + 1)],
                    [(f'h{j}', f'h{j+1}', 'x') for j in range(n)]))
    if r - i:
        factors.append(([f'z{k}' for k in range(r - i + 1)],
                        [(f'z{k}', f'z{k+1}', label)
                         for k in range(r - i) for label in ('1', 'x')]))
    vertices, occurrences, previous = ['s'], [], 's'
    for names, edges in factors:
        vertices.extend(names)
        occurrences.extend(edges)
        occurrences.append((previous, names[0], '1'))
        previous = names[-1]
    vertices.append('t')
    occurrences.append((previous, 't', '1'))
    return representation(vertices, occurrences, 's', 't')


def path_case(r, n):
    placements = [placement(r, n, i) for i in range(r + 1)]
    vertices, occurrences = [], []
    for i, h in enumerate(placements):
        rename = lambda v: 't' if v == 't' else f'{i}:{v}'
        vertices.extend(rename(v) for v in h['vertices'] if v != 't')
        occurrences.extend((rename(u), rename(v), label)
                           for u, v, label in h['occurrences'])
    vertices.append('t')
    u = representation(vertices, occurrences, f'{r}:s', 't')
    index = {v: j for j, v in enumerate(vertices)}
    inclusions, residual_evidence = [], []
    for i, h in enumerate(placements):
        rows = [1 << index['t' if v == 't' else f'{i}:{v}'] for v in h['vertices']]
        inclusions.append(arrow(h, u, rows, require_initial=(i == r)))
        for j in range(n):
            observed = h['state_residual_polynomial_bits'][h['vertices'].index(f'h{j}')]
            union_observed = u['state_residual_polynomial_bits'][index[f'{i}:h{j}']]
            expected = unit_polynomial(r - i) << (n - j)
            assert observed == union_observed == expected
            residual_evidence.append({
                'i': i, 'j': j, 'order_at_zero': n - j, 'order_at_one': r - i,
                'observed_bits': observed, 'union_observed_bits': union_observed,
                'expected_bits': expected,
            })
    distinct = {p['observed_bits'] for p in residual_evidence}
    assert len(distinct) == n * (r + 1) and 0 not in distinct and 1 not in distinct
    s = placements[0]['g'] + placements[-1]['g']
    assert s == 10 * r + 6 * n + 20
    assert len(vertices) == (r + 1) * (r + n + 4) - 1
    assert len(occurrences) == (r + 1) * (2 * r + n + 4) - 2
    return {
        'r': r, 'N': n, 'placements': placements, 'auxiliary_U': u,
        'copy_incidences': inclusions,
        'qualification': 'Only inclusion i=r is an accepting arrow; other inclusions preserve M and beta only.',
        'complete_distinguished_residuals': residual_evidence,
        'ledger': {
            'S': s, 'distinct_nonzero_residuals': len(distinct),
            'required_compressed_vertices_including_final': len(distinct) + 1,
            'required_twice_graph_size_lower_bound': 2 * (len(distinct) + 1),
            'actual_uncompressed_vertices': len(vertices), 'actual_uncompressed_g': u['g'],
            'target': 'A universal C times S; finite ratios do not establish asymptotics.',
        },
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path,
                        default=Path('scripts/batched-incidence/output-537'))
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=False)
    fixture = {
        'vertices': ['p', 'u', 'v', 'q'], 'roots': ('p', 'q'),
        'edges': [('p', 'q', '1'), ('u', 'q', '1'), ('v', 'q', '1'),
                  ('p', 'u', 'x'), ('p', 'v', 'x')],
    }
    cancellation = [
        cancellation_case('L117 cancelling fixture', 6, fixture),
        cancellation_case('L119 long branch r=m=6', 6, cancelled_operand(6)),
    ]
    path = path_case(8, 8)
    certificate = {
        'result': 'Cancellation projections pass; coordinate folding has a quadratic symbolic obstruction (L120).',
        'encoding': 'Row bitsets, column j is bit j; polynomial bit k is the coefficient of x^k.',
        'cancellation_cases': cancellation, 'path_case': path,
        'verification_failures': [],
        'symbolic_threshold': 'At r=N, twice the compressed graph size is at least 2*(N*(N+1)+1), versus C*(16*N+20). This is unbounded for every fixed C.',
    }
    destination = args.output / 'parity-folding.json'
    destination.write_text(json.dumps(certificate, indent=2) + '\n')
    for case in cancellation:
        print(f"{case['name']}: all three equations PASS for both projections; "
              f"charge={case['support_plus_twice_intermediate']} <= 2S={case['proved_upper_bound_2S']}")
    ledger = path['ledger']
    print(f"Path r=N=8: all 72 residuals checked; required compressed vertices>="
          f"{ledger['required_compressed_vertices_including_final']}; S={ledger['S']}; "
          f"uncompressed vertices={ledger['actual_uncompressed_vertices']}, g={ledger['actual_uncompressed_g']}")
    print('Required threshold: O(S) for one universal C. Symbolic lower bound: Omega(N^2), S=16N+20; FAIL for this template.')
    print(f'Verification failures: 0. Full certificate: {destination}')


if __name__ == '__main__':
    main()
