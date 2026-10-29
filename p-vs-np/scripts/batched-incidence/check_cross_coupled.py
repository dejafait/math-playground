#!/usr/bin/env python3
"""Complete exact receipts for one two-stage boundary-coupled lift.

Uses existing finite graph/matrix helpers, not saved pass flags. Every
occurrence, scalar map, equation product and kernel basis is written out.
The diagnostic expands matrices and claims no sparse generation oracle.
"""

import argparse
import json
from pathlib import Path

from check_elementary_gap import action, identity, multiply, product
from check_endpoint_spine import (
    all_series, check_arrow, close_graph, endpoint_spine, finite_trial_rows,
)


def xor_rows(*matrices):
    rows = [0] * len(matrices[0])
    for matrix in matrices:
        rows = [a ^ b for a, b in zip(rows, matrix)]
    return rows


def row_kernel(rows):
    """Eliminate every row, retaining full domain vectors for dependencies."""
    pivots, kernel = {}, []
    for i, initial in enumerate(rows):
        value, origin = initial, 1 << i
        while value:
            pivot = value.bit_length() - 1
            if pivot not in pivots:
                pivots[pivot] = (value, origin)
                break
            value ^= pivots[pivot][0]
            origin ^= pivots[pivot][1]
        if value == 0:
            kernel.append(origin)
    assert len(kernel) + len(pivots) == len(rows)
    assert not any(multiply(kernel, rows))
    # Each dependency has a new, largest input coordinate; hence independent.
    assert len({v.bit_length() for v in kernel}) == len(kernel)
    return len(pivots), kernel


def make_coupled(n, old):
    vertices = old['vertices']
    ix = {v: i for i, v in enumerate(vertices)}
    size = len(vertices)
    h = [0] * size
    for kind in ('f', 'h'):
        for i in range(n + 1):
            h[ix[f'a_{kind}{i}']] = 1 << ix[f'b_{kind}{i}']
    for i in range(n):
        h[ix[f'b_h{i}']] = 1 << ix[f'd{i}']
        h[ix[f'b_f{i}']] = 1 << ix[f'd{n+i}']
    h2 = multiply(h, h)
    assert not any(multiply(h2, h))
    t = xor_rows(identity(size), h)
    u = xor_rows(identity(size), h, h2)
    assert multiply(t, u) == multiply(u, t) == identity(size)

    occurrences, origins = [], []
    for edge_number, (old_source, old_target, label) in enumerate(old['occurrences']):
        source_index, target_index = ix[old_source], ix[old_target]
        first = len(occurrences)
        for w, urow in enumerate(u):
            if not ((urow >> source_index) & 1):
                continue
            for z in range(size):
                if (t[target_index] >> z) & 1:
                    occurrences.append((vertices[w], vertices[z], label))
        origins.append({'old_edge_index': edge_number,
                        'new_edge_range': [first, len(occurrences)]})
    q = close_graph(vertices, occurrences, old['topological_order'])
    for key in ('C_rows', 'D_rows', 'K_rows', 'M_rows'):
        assert q[key] == multiply(multiply(u, old[key]), t)
    assert q['alpha_bits'] == action(old['alpha_bits'], t)
    assert q['beta_rows'] == multiply(u, old['beta_rows'])
    assert len(vertices) == 6 * n + 6
    assert len(occurrences) == 24 * n + 11
    return q, {'H_rows': h, 'T_rows': t, 'U_rows': u,
               'occurrence_origin_ranges': origins}


def run_case(k):
    n = 1 << k
    path = {'vertices': [f'h{j}' for j in range(n + 1)],
            'edges': [(f'h{j}', f'h{j+1}', 'x') for j in range(n)],
            'roots': ('h0', f'h{n}')}
    a, b = product(n, path, 'FG'), product(n, path, 'GF')
    old = endpoint_spine(n, a, b)
    q, construction = make_coupled(n, old)
    for graph in (a, b, old, q):
        all_series(graph)
        assert graph['accepted_polynomial_bits'] == (1 << n) ^ (1 << (2*n))
    arrows, kernels = {}, {}
    for name, target in (('A', a), ('B', b)):
        old_rows = finite_trial_rows(old, target, n)
        check_arrow(old, target, old_rows, f'Q0_to_{name}')
        rows = multiply(construction['U_rows'], old_rows)
        arrows[name] = check_arrow(q, target, rows, f'Q_to_{name}')
        rank, kernel = row_kernel(rows)
        images = multiply(kernel, q['M_rows'])
        image_outputs = multiply(images, rows)
        final_outputs = multiply(kernel, q['beta_rows'])
        assert not any(image_outputs) and not any(final_outputs)
        kernels[name] = {'rank': rank, 'dimension': len(kernel),
                         'basis_rows': kernel, 'images_under_M_rows': images,
                         'image_outputs_rows': image_outputs,
                         'final_outputs': final_outputs}
    assert kernels['A']['rank'] == kernels['B']['rank'] == 2*n + 1
    assert not any(multiply(kernels['A']['basis_rows'], arrows['B']['X_rows']))
    assert not any(multiply(kernels['B']['basis_rows'], arrows['A']['X_rows']))

    qi = {v: i for i, v in enumerate(q['vertices'])}
    ai = {v: i for i, v in enumerate(a['vertices'])}
    changed, forced = [], []
    for j in range(n):
        row = qi[f'b_h{j}']
        assert q['all_residual_polynomial_bits'][row] == 0
        assert arrows['A']['X_rows'][row] == arrows['B']['X_rows'][row] == 0
        assert q['all_prefix_polynomial_bits'][row] == 1 << (n+j)
        assert q['all_prefix_polynomial_bits'][qi[f'd{j}']] == 0
    for i in range(n):
        exponent = n - i - 1
        binomial = sum(int((j & exponent) == j) << j
                       for j in range(exponent + 1))
        expected = (binomial << 1) ^ (1 << (n-i))
        actual = q['all_residual_polynomial_bits'][qi[f'b_f{i}']]
        assert actual == expected
        changed.append({'vertex': f'b_f{i}', 'old_residual_bits': binomial << 1,
                        'new_residual_bits': actual, 'required_bits': expected})
        for j in range(n):
            required = int((j & exponent) == j) ^ int(j == exponent)
            column = ai[f'h{n-1-j}']
            got = (arrows['A']['X_rows'][qi[f'b_f{i}']] >> column) & 1
            assert got == required
            forced.append([f'b_f{i}', f'h{n-1-j}', got, required])
    bound = sum(entry[3] for entry in forced)
    assert bound == 3**k - n
    s = a['g'] + b['g']
    assert s == 16*n + 20
    assert 2*q['g'] == 108*n + 56 <= 7*s
    support = arrows['A']['support'] + arrows['B']['support']
    return {
        'k': k, 'N': n, 'A': a, 'B': b, 'Q0_construction_only': old,
        'Q': q, 'construction': construction, 'arrows': arrows,
        'kernels': kernels, 'changed_b_f_residuals': changed,
        'complete_forced_rectangle': forced,
        'ledger': {'S': s, 'Q_vertices': len(q['vertices']),
                   'Q_occurrences': len(q['occurrences']),
                   'twice_Q_g': 2*q['g'], 'graph_upper_bound_7S': 7*s,
                   'full_map_support': support,
                   'support_plus_twice_Q_g': support + 2*q['g'],
                   'forced_Q_to_A_support_lower_bound': bound,
                   'required_bound': 'support + 2g(Q) <= C*S for ONE universal C'},
        'verification_failures': [],
        'qualification': 'Finite replay is not the asymptotic proof. Q0 and expanded conjugation matrices are diagnostic construction data, not free certificate entries. Only this Q and these two arrow orientations are tested.',
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--ks', nargs='+', type=int, default=[2])
    parser.add_argument('--output', type=Path,
                        default=Path('scripts/batched-incidence/output-540'))
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    for k in args.ks:
        if k < 0:
            raise ValueError('k must be nonnegative')
        destination = args.output / f'cross-coupled-N{1 << k}.json'
        if destination.exists():
            raise FileExistsError(destination)
        case = run_case(k)
        destination.write_text(json.dumps(case, indent=2) + '\n')
        ledger = case['ledger']
        print(f"N={case['N']}: both complete maps and all equations pass; "
              f"common zero-final invariant kernel dimension={case['kernels']['A']['dimension']}; "
              f"S={ledger['S']}, 2g(Q)={ledger['twice_Q_g']} <= {ledger['graph_upper_bound_7S']}=7S; "
              f"actual total charge={ledger['support_plus_twice_Q_g']}; "
              f"forced Q->A support={ledger['forced_Q_to_A_support_lower_bound']}. "
              'Verification failures: none.')
        print('Required: one universal C. Finite ratios are insufficient; '
              'the symbolic lower bound 3^k-2^k must be proved separately.')
        print(f'Full certificate: {destination}')


if __name__ == '__main__':
    main()
