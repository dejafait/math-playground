#!/usr/bin/env python3
"""The fixed step-559 upper-bit raw conjugation test, only N=4,8.

Save literal graphs, all scalar products, full central systems and exact
row-operation certificates. No sparse-solution or asymptotic claim.
"""

import argparse
import json
from pathlib import Path

from check_elementary_gap import action, identity, multiply, product
from check_endpoint_spine import close_graph
from check_weight_filtration import endpoint


def xor_rows(a, b):
    return [x ^ y for x, y in zip(a, b)]


def topological_order(vertices, edges):
    outgoing = {v: [] for v in vertices}
    degree = {v: 0 for v in vertices}
    for u, v, _ in edges:
        outgoing[u].append(v)
        degree[v] += 1
    order = []
    remaining = set(vertices)
    while remaining:
        ready = next((v for v in vertices if v in remaining and degree[v] == 0), None)
        if ready is None:
            # Follow incoming edges in the remaining finite graph to a cycle.
            walk, seen = [], {}
            v = next(v for v in vertices if v in remaining)
            while v not in seen:
                seen[v] = len(walk)
                walk.append(v)
                v = next(u for u, w, _ in edges if w == v and u in remaining)
            return None, list(reversed(walk[seen[v]:] + [v]))
        remaining.remove(ready)
        order.append(ready)
        for v in outgoing[ready]:
            degree[v] -= 1
    return order, None


def literal_graph(vertices, edges):
    order, cycle = topological_order(vertices, edges)
    checks = {
        'distinct_vertices': len(vertices) == len(set(vertices)),
        'singleton_labels': all(label in ('1', 'x') for _, _, label in edges),
        'no_incoming_s': all(v != 's' for _, v, _ in edges),
        'no_outgoing_t': all(u != 't' for u, _, _ in edges),
        'simultaneous_acyclicity': order is not None,
    }
    if not all(checks.values()):
        return {'vertices': vertices, 'occurrences': edges,
                'graph_checks': checks, 'cycle': cycle}, False
    graph = close_graph(vertices, edges, order)
    width = len(vertices)
    # A second finite-power computation checks the complete constant inverse.
    inverse, power = identity(width), identity(width)
    for _ in range(1, width):
        power = multiply(power, graph['C_rows'])
        inverse = xor_rows(inverse, power)
    checks['constant_power_nilpotence'] = not any(multiply(power, graph['C_rows']))
    checks['topological_closure_equals_full_power_sum'] = inverse == graph['K_rows']
    graph['constant_inverse_from_powers_rows'] = inverse
    graph['I_plus_C_rows'] = xor_rows(identity(width), graph['C_rows'])
    graph['graph_checks'] = checks
    graph['cycle'] = cycle
    return graph, all(checks.values())


def endpoint_formula(n, name, vertices):
    ix = {v: i for i, v in enumerate(vertices)}

    def bits(names):
        return sum(1 << ix[v] for v in names)

    rows = [0] * len(vertices)
    for i in range(n):
        rows[ix[f'f{i}']] = bits([f'f{j}' for j in range(i + 1, n + 1)]
                                 + (['h0'] if name == 'A' else ['t']))
    for j in range(n - 1):
        rows[ix[f'h{j}']] = bits([f'h{j+1}'])
    rows[ix[f'h{n-1}']] = bits([f'h{n}', 't']
                               + ([] if name == 'A' else [f'f{i}' for i in range(n + 1)]))
    alpha = bits(['s'] + ([f'f{i}' for i in range(n + 1)] + ['h0']
                          if name == 'A' else ['h0']))
    return {'M_rows': rows, 'alpha_bits': alpha,
            'beta_rows': [int(v == 't') for v in vertices]}


def arrow(source, target, rows, label):
    # Reconstruct closures from the saved literal occurrences on every call.
    source, ok_s = literal_graph(source['vertices'], source['occurrences'])
    target, ok_t = literal_graph(target['vertices'], target['occurrences'])
    assert ok_s and ok_t
    initial = action(source['alpha_bits'], rows)
    left = multiply(source['M_rows'], rows)
    right = multiply(rows, target['M_rows'])
    final = multiply(rows, target['beta_rows'])
    checks = {'initial': initial == target['alpha_bits'], 'transition': left == right,
              'final': final == source['beta_rows']}
    differences = [[source['vertices'][i], target['vertices'][j]]
                   for i, (a, b) in enumerate(zip(left, right))
                   for j in range(len(target['vertices'])) if ((a ^ b) >> j) & 1]
    return {'label': label, 'X_rows': rows, 'support': sum(x.bit_count() for x in rows),
            'initial_product_bits': initial, 'required_initial_bits': target['alpha_bits'],
            'left_transition_rows': left, 'right_transition_rows': right,
            'final_product_rows': final, 'required_final_rows': source['beta_rows'],
            'unequal_transition_entries': differences, 'checks': checks}


def central_system(source, target, label):
    p, q = len(source['vertices']), len(target['vertices'])
    variables = p * q
    equations, tags = [], []

    def add(indices, rhs, tag):
        row = rhs << variables
        for i, j in indices:
            row ^= 1 << (i * q + j)
        equations.append(row)
        tags.append(tag)

    for j in range(q):
        add([(i, j) for i in range(p) if (source['alpha_bits'] >> i) & 1],
            (target['alpha_bits'] >> j) & 1, ['initial', j])
    for i in range(p):
        for j in range(q):
            add([(a, j) for a in range(p) if (source['M_rows'][i] >> a) & 1]
                + [(i, b) for b in range(q) if (target['M_rows'][b] >> j) & 1],
                0, ['transition', i, j])
    for i in range(p):
        add([(i, j) for j in range(q) if target['beta_rows'][j]],
            source['beta_rows'][i], ['final', i])

    reduced = equations[:]
    combinations = identity(len(equations))
    operations, pivots = [], []
    for column in range(variables):
        r = len(pivots)
        pivot = next((i for i in range(r, len(reduced)) if (reduced[i] >> column) & 1), None)
        if pivot is None:
            continue
        if pivot != r:
            reduced[r], reduced[pivot] = reduced[pivot], reduced[r]
            combinations[r], combinations[pivot] = combinations[pivot], combinations[r]
            operations.append(['swap', r, pivot])
        for i in range(len(reduced)):
            if i != r and (reduced[i] >> column) & 1:
                reduced[i] ^= reduced[r]
                combinations[i] ^= combinations[r]
                operations.append(['xor', i, r])
        pivots.append(column)

    # Replay every elementary operation, and independently check provenance.
    replay = equations[:]
    for kind, i, j in operations:
        if kind == 'swap':
            replay[i], replay[j] = replay[j], replay[i]
        else:
            replay[i] ^= replay[j]
    assert replay == reduced
    assert multiply(combinations, equations) == reduced
    mask = (1 << variables) - 1
    assert all((reduced[r] & mask) & ((1 << col) - 1) == 0 for r, col in enumerate(pivots))
    assert all(sum(((row >> col) & 1) << i for i, row in enumerate(reduced)) == 1 << r
               for r, col in enumerate(pivots))
    assert all((row & mask) == 0 for row in reduced[len(pivots):])
    inconsistent = next((i for i, row in enumerate(reduced) if row == 1 << variables), None)
    result = {'label': label, 'source_vertices': source['vertices'],
              'target_vertices': target['vertices'],
              'variable_order': [[u, v] for u in source['vertices'] for v in target['vertices']],
              'variable_count': variables, 'equation_tags': tags,
              'equation_augmented_rows': equations, 'rref_augmented_rows': reduced,
              'row_operations': operations, 'rref_original_equation_combinations': combinations,
              'pivot_columns': pivots, 'coefficient_rank': len(pivots),
              'consistent': inconsistent is None, 'free_variables_set_to_zero': True}
    if inconsistent is not None:
        witness = combinations[inconsistent]
        assert action(witness, equations) == 1 << variables
        result['inconsistency_witness'] = {'original_equation_combination_bits': witness,
                                          'augmented_sum': 1 << variables}
    else:
        solution = sum(((reduced[r] >> variables) & 1) << col for r, col in enumerate(pivots))
        assert all(((row & mask & solution).bit_count() & 1) == (row >> variables)
                   for row in equations)
        rows = [(solution >> (i * q)) & ((1 << q) - 1) for i in range(p)]
        result['selected_solution_bits'] = solution
        result['arrow'] = arrow(source, target, rows, label)
        assert all(result['arrow']['checks'].values())
    return result


def run_case(n):
    k = n.bit_length() - 1
    case = {'N': n, 'k': k, 'endpoints': {}, 'stages': {}, 'stage_arrows': {},
            'central_systems': {}, 'status': 'IN_PROGRESS', 'failure': None}
    path = {'vertices': [f'h{i}' for i in range(n + 1)], 'roots': ('h0', f'h{n}'),
            'edges': [(f'h{i}', f'h{i+1}', 'x') for i in range(n)]}
    for name, order in (('A', 'FG'), ('B', 'GF')):
        original = product(n, path, order)
        graph, ok = literal_graph(original['vertices'], original['occurrences'])
        assert ok
        independently_built = endpoint(n, name)
        formula = endpoint_formula(n, name, graph['vertices'])
        comparisons = {field: graph[field] == original[field] == independently_built[field]
                       for field in ('vertices', 'occurrences', 'K_rows', 'M_rows',
                                     'alpha_bits', 'beta_rows', 'g')}
        comparisons['entire_L122_equation_6'] = all(graph[field] == value for field, value in formula.items())
        comparisons['literal_size'] = (len(graph['vertices']) == 2*n+4
                                       and len(graph['occurrences']) == 3*n+3 and graph['g'] == 8*n+10)
        assert all(comparisons.values())
        graph['endpoint_comparisons'] = comparisons
        graph['L122_entire_closed_formula'] = formula
        case['endpoints'][name] = graph
        case['stages'][name] = []
        case['stage_arrows'][name] = []
    case['S'] = case['endpoints']['A']['g'] + case['endpoints']['B']['g']
    assert case['S'] == 16*n + 20

    # Complete corresponding stages on A and B before proceeding to the next bit.
    for u in range(k):
        for name in ('A', 'B'):
            previous = case['stages'][name][-1]['graph'] if u else case['endpoints'][name]
            vertices = previous['vertices']
            ix = {v: i for i, v in enumerate(vertices)}
            e = identity(len(vertices))
            for j in range(n):
                if not (j >> u) & 1:
                    e[ix[f'f{j}']] ^= 1 << ix[f'f{j+(1<<u)}']
            inverse = e[:]
            assert multiply(e, inverse) == multiply(inverse, e) == identity(len(vertices))
            raw_c = multiply(multiply(inverse, previous['C_rows']), e)
            raw_d = multiply(multiply(inverse, previous['D_rows']), e)
            edges = [(a, b, label) for i, a in enumerate(vertices)
                     for j, b in enumerate(vertices) for label, matrix in (('1', raw_c), ('x', raw_d))
                     if (matrix[i] >> j) & 1]
            graph, ok = literal_graph(vertices, edges)
            stage = {'bit': u, 'E_rows': e, 'E_inverse_rows': inverse,
                     'raw_conjugated_C_rows': raw_c, 'raw_conjugated_D_rows': raw_d,
                     'graph': graph}
            case['stages'][name].append(stage)
            if not ok:
                case['status'] = 'STOP_GRAPH'
                case['failure'] = {'side': name, 'bit': u, 'graph_checks': graph['graph_checks'],
                                   'cycle': graph['cycle']}
                return case
            assert graph['C_rows'] == raw_c and graph['D_rows'] == raw_d
            stage['closure_conjugation_rows'] = multiply(multiply(inverse, previous['K_rows']), e)
            stage['closed_transition_conjugation_rows'] = multiply(multiply(inverse, previous['M_rows']), e)
            assert stage['closure_conjugation_rows'] == graph['K_rows']
            assert stage['closed_transition_conjugation_rows'] == graph['M_rows']
            receipt = arrow(previous, graph, e, f'{name}{u}_to_{name}{u+1}')
            case['stage_arrows'][name].append(receipt)
            if not all(receipt['checks'].values()):
                case['status'] = 'STOP_EQUATION'
                case['failure'] = {'side': name, 'bit': u, 'arrow': receipt}
                return case

    a, b = (case['stages'][name][-1]['graph'] for name in ('A', 'B'))
    for label, source, target in (('Ak_to_Bk', a, b), ('Bk_to_Ak', b, a)):
        case['central_systems'][label] = central_system(source, target, label)
    consistent = [label for label, system in case['central_systems'].items() if system['consistent']]
    if not consistent:
        case['status'] = 'STOP_BOTH_CENTRAL_INCONSISTENT'
        case['failure'] = 'Both complete central systems are inconsistent.'
        return case

    # Select the first consistent orientation, not the sparsest solution.
    selected = consistent[0]
    map_terms = [{'position': receipt['label'], 'nnz': receipt['support']}
                 for name in ('A', 'B') for receipt in case['stage_arrows'][name]]
    map_terms += [{'position': selected, 'nnz': case['central_systems'][selected]['arrow']['support']}]
    graph_terms = [{'position': f'{name}{u+1}', 'vertices': len(stage['graph']['vertices']),
                    'occurrences': len(stage['graph']['occurrences']), 'g': stage['graph']['g'],
                    'twice_g': 2*stage['graph']['g']}
                   for name in ('A', 'B') for u, stage in enumerate(case['stages'][name])]
    total = sum(t['nnz'] for t in map_terms) + sum(t['twice_g'] for t in graph_terms)
    scale = case['S'] * (1+k)
    case['ledger'] = {'selected_central_orientation': selected, 'map_terms': map_terms,
                      'intermediate_graph_position_terms': graph_terms,
                      'sum_map_support': sum(t['nnz'] for t in map_terms),
                      'twice_sum_intermediate_g': sum(t['twice_g'] for t in graph_terms),
                      'total': total, 'required_scale_S_times_1_plus_k': scale,
                      'finite_ratio_numerator': total, 'finite_ratio_denominator': scale,
                      'universal_C_established': False,
                      'chain_position_order': ['A0'] + [f'A{u+1}' for u in range(k)]
                                              + [f'B{u}' for u in range(k, -1, -1)]}
    case['status'] = 'FINITE_PASS'
    return case


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, default=Path('scripts/batched-incidence/output-559'))
    output = parser.parse_args().output
    output.mkdir(exist_ok=False)
    certificate = {'encoding': 'F2; row bit j is column j; augmented RHS is bit variable_count; '
                               'source-major variable order in saved vertex lists (numeric f indices).',
                   'cases': [], 'scope': 'Exactly approved N=4,8 recipe, least significant bit first; '
                                         'no bit reversal, graph substitution or asymptotic inference.'}
    path = output / 'staged-bit-basis-certificate.json'
    for n in (4, 8):
        case = run_case(n)
        certificate['cases'].append(case)
        path.write_text(json.dumps(certificate, indent=2) + '\n')
        print(f'N={n}: {case["status"]}; failure={case["failure"]}')
        if 'ledger' in case:
            ledger = case['ledger']
            print(f'  expanded charge={ledger["total"]}; required scale S*(1+k)='
                  f'{ledger["required_scale_S_times_1_plus_k"]}; universal C unproved')
            print('  central systems: ' + ', '.join(f'{key}:consistent={value["consistent"]}'
                                                       for key, value in case['central_systems'].items()))
        if case['status'] != 'FINITE_PASS':
            break
    print(f'Complete certificate: {path}')


if __name__ == '__main__':
    main()
