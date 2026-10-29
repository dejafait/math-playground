#!/usr/bin/env python3
"""Reconstruct all fixed step-559 evidence using dense F2 matrix products."""

import argparse
import json
from pathlib import Path


def decode(rows, width):
    return [[(row >> j) & 1 for j in range(width)] for row in rows]


def encode(matrix):
    return [sum(value << j for j, value in enumerate(row)) for row in matrix]


def eye(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def mul(a, b):
    bt = list(zip(*b))
    return [[sum(x*y for x, y in zip(row, col)) % 2 for col in bt] for row in a]


def plus(a, b):
    return [[x ^ y for x, y in zip(row, other)] for row, other in zip(a, b)]


def graph_data(graph):
    vertices, edges = graph['vertices'], graph['occurrences']
    width = len(vertices)
    ix = {v: i for i, v in enumerate(vertices)}
    topo = graph['topological_order']
    assert len(set(vertices)) == width and sorted(topo) == sorted(vertices)
    pos = {v: i for i, v in enumerate(topo)}
    c, d = [[0]*width for _ in vertices], [[0]*width for _ in vertices]
    for u, v, label in edges:
        assert label in ('1', 'x') and pos[u] < pos[v] and v != 's' and u != 't'
        (c if label == '1' else d)[ix[u]][ix[v]] ^= 1
    closure, power = eye(width), eye(width)
    for _ in range(1, width):
        power = mul(power, c)
        closure = plus(closure, power)
    assert not any(map(any, mul(power, c)))
    transition = mul(d, closure)
    assert mul(plus(eye(width), c), closure) == mul(closure, plus(eye(width), c)) == eye(width)
    assert encode(c) == graph['C_rows'] and encode(d) == graph['D_rows']
    assert encode(closure) == graph['K_rows'] == graph['constant_inverse_from_powers_rows']
    assert encode(transition) == graph['M_rows']
    assert encode([closure[ix['s']]])[0] == graph['alpha_bits']
    beta = [[int(v == 't')] for v in vertices]
    assert [v[0] for v in beta] == graph['beta_rows']
    assert graph['g'] == width + 2*len(edges)
    return c, d, closure, transition, [closure[ix['s']]], beta


def arrow_data(source, target, receipt):
    *_, m, alpha, beta = graph_data(source)
    *_, other_m, other_alpha, other_beta = graph_data(target)
    x = decode(receipt['X_rows'], len(target['vertices']))
    assert len(x) == len(source['vertices'])
    initial, left, right, final = mul(alpha, x), mul(m, x), mul(x, other_m), mul(x, other_beta)
    assert initial == other_alpha and left == right and final == beta
    assert encode(initial)[0] == receipt['initial_product_bits'] == receipt['required_initial_bits']
    assert encode(left) == receipt['left_transition_rows'] == receipt['right_transition_rows']
    assert [row[0] for row in final] == receipt['final_product_rows'] == receipt['required_final_rows']
    assert receipt['support'] == sum(map(sum, x))


def system_data(source, target, system):
    p, q = len(source['vertices']), len(target['vertices'])
    variables = p*q
    assert system['variable_count'] == variables
    assert system['source_vertices'] == source['vertices'] and system['target_vertices'] == target['vertices']
    assert system['variable_order'] == [[u, v] for u in source['vertices'] for v in target['vertices']]
    *_, m, alpha, beta = graph_data(source)
    *_, om, oa, ob = graph_data(target)
    rhs = oa[0] + [0]*(p*q) + [row[0] for row in beta]
    equations = [value << variables for value in rhs]
    # Evaluate the full linear operator on EACH coordinate basis matrix.
    for i in range(p):
        for j in range(q):
            x = [[0]*q for _ in range(p)]
            x[i][j] = 1
            values = mul(alpha, x)[0]
            values += [v for row in plus(mul(m, x), mul(x, om)) for v in row]
            values += [row[0] for row in mul(x, ob)]
            for e, value in enumerate(values):
                equations[e] |= value << (i*q+j)
    assert equations == system['equation_augmented_rows']
    assert system['equation_tags'] == ([['initial', j] for j in range(q)]
           + [['transition', i, j] for i in range(p) for j in range(q)]
           + [['final', i] for i in range(p)])
    replay = equations[:]
    combinations = [1 << i for i in range(len(equations))]
    for operation, i, j in system['row_operations']:
        assert i != j and 0 <= i < len(equations) and 0 <= j < len(equations)
        if operation == 'swap':
            replay[i], replay[j] = replay[j], replay[i]
            combinations[i], combinations[j] = combinations[j], combinations[i]
        else:
            assert operation == 'xor'
            replay[i] ^= replay[j]
            combinations[i] ^= combinations[j]
    assert replay == system['rref_augmented_rows']
    assert combinations == system['rref_original_equation_combinations']
    for value, combination in zip(replay, combinations):
        total = 0
        for i, equation in enumerate(equations):
            if (combination >> i) & 1:
                total ^= equation
        assert total == value
    mask = (1 << variables)-1
    pivots = system['pivot_columns']
    assert pivots == sorted(set(pivots)) and len(pivots) == system['coefficient_rank']
    for r, pivot in enumerate(pivots):
        assert (replay[r] & mask) & ((1 << pivot)-1) == 0
        assert [((row >> pivot) & 1) for row in replay] == [int(i == r) for i in range(len(replay))]
    assert all((row & mask) == 0 for row in replay[len(pivots):])
    consistent = all(row != (1 << variables) for row in replay)
    assert consistent == system['consistent']
    if consistent:
        solution = system['selected_solution_bits']
        assert all((solution >> j) & 1 == 0 for j in range(variables) if j not in pivots)
        assert all(((row & solution & mask).bit_count() % 2) == (row >> variables) for row in equations)
        assert system['arrow']['X_rows'] == [(solution >> (i*q)) & ((1 << q)-1) for i in range(p)]
        arrow_data(source, target, system['arrow'])
    else:
        witness = system['inconsistency_witness']['original_equation_combination_bits']
        total = 0
        for i, row in enumerate(equations):
            if (witness >> i) & 1:
                total ^= row
        assert total == 1 << variables


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--directory', type=Path, default=Path('scripts/batched-incidence/output-559'))
    directory = parser.parse_args().directory
    path = directory / 'staged-bit-basis-certificate.json'
    certificate = json.loads(path.read_text())
    assert [case['N'] for case in certificate['cases']] == [4, 8]
    summaries = []
    for case in certificate['cases']:
        n, k = case['N'], case['k']
        assert n == 1 << k and case['status'] == 'FINITE_PASS' and case['failure'] is None
        for name in ('A', 'B'):
            original = case['endpoints'][name]
            expected_vertices = ['s'] + [f'f{i}' for i in range(n+1)] + [f'h{i}' for i in range(n+1)] + ['t']
            expected_edges = [(f'f{i}', f'f{i+1}', label) for i in range(n) for label in ('1', 'x')]
            expected_edges += [(f'h{i}', f'h{i+1}', 'x') for i in range(n)]
            expected_edges += ([('s', 'f0', '1'), (f'f{n}', 'h0', '1'), (f'h{n}', 't', '1')]
                               if name == 'A' else [('s', 'h0', '1'), (f'h{n}', 'f0', '1'), (f'f{n}', 't', '1')])
            assert original['vertices'] == expected_vertices and original['occurrences'] == [list(e) for e in expected_edges]
            graph_data(original)
            assert all(original[field] == value for field, value in original['L122_entire_closed_formula'].items())
            previous = original
            assert len(case['stages'][name]) == len(case['stage_arrows'][name]) == k
            for u, stage in enumerate(case['stages'][name]):
                graph = stage['graph']
                assert stage['bit'] == u and graph['vertices'] == expected_vertices
                width = len(expected_vertices)
                e = eye(width)
                for j in range(n):
                    if j & (1 << u) == 0:
                        e[1+j][1+j+(1 << u)] ^= 1
                assert mul(e, e) == eye(width) and encode(e) == stage['E_rows'] == stage['E_inverse_rows']
                pc, pd, pk, pm, _, _ = graph_data(previous)
                c, d, closure, transition, _, _ = graph_data(graph)
                assert c == mul(mul(e, pc), e) and d == mul(mul(e, pd), e)
                assert encode(c) == stage['raw_conjugated_C_rows'] and encode(d) == stage['raw_conjugated_D_rows']
                assert encode(mul(mul(e, pk), e)) == stage['closure_conjugation_rows'] == encode(closure)
                assert encode(mul(mul(e, pm), e)) == stage['closed_transition_conjugation_rows'] == encode(transition)
                expected_occurrences = [(a, b, label) for i, a in enumerate(expected_vertices)
                                        for j, b in enumerate(expected_vertices) for label, matrix in (('1', c), ('x', d))
                                        if matrix[i][j]]
                assert graph['occurrences'] == [list(e) for e in expected_occurrences]
                arrow_data(previous, graph, case['stage_arrows'][name][u])
                assert case['stage_arrows'][name][u]['X_rows'] == encode(e)
                previous = graph
        a, b = (case['stages'][name][-1]['graph'] for name in ('A', 'B'))
        for label, source, target in (('Ak_to_Bk', a, b), ('Bk_to_Ak', b, a)):
            system_data(source, target, case['central_systems'][label])
        ledger = case['ledger']
        first = next(label for label, system in case['central_systems'].items() if system['consistent'])
        assert first == ledger['selected_central_orientation']
        maps = [{'position': item['label'], 'nnz': item['support']}
                for name in ('A', 'B') for item in case['stage_arrows'][name]]
        maps += [{'position': first, 'nnz': case['central_systems'][first]['arrow']['support']}]
        terms = [{'position': f'{name}{u+1}', 'vertices': len(stage['graph']['vertices']),
                  'occurrences': len(stage['graph']['occurrences']), 'g': stage['graph']['g'],
                  'twice_g': 2*stage['graph']['g']}
                 for name in ('A', 'B') for u, stage in enumerate(case['stages'][name])]
        assert maps == ledger['map_terms'] and terms == ledger['intermediate_graph_position_terms']
        assert ledger['chain_position_order'] == ['A0'] + [f'A{i}' for i in range(1, k+1)] + [f'B{i}' for i in range(k, -1, -1)]
        support, graphs = sum(t['nnz'] for t in maps), sum(t['twice_g'] for t in terms)
        assert support == ledger['sum_map_support'] and graphs == ledger['twice_sum_intermediate_g']
        assert support + graphs == ledger['total'] == ledger['finite_ratio_numerator']
        assert case['S'] == 16*n+20 == sum(case['endpoints'][name]['g'] for name in ('A', 'B'))
        assert case['S']*(1+k) == ledger['required_scale_S_times_1_plus_k'] == ledger['finite_ratio_denominator']
        assert ledger['universal_C_established'] is False
        summaries.append({'N': n, 'graphs_received': 2+2*k, 'arrows_received': 2*k+2,
                          'central_systems_received': 2, 'total': support+graphs,
                          'required_scale': case['S']*(1+k), 'all_checks_passed': True})
    receipt = {'input': str(path), 'method': 'Dense F2 reconstruction; all original equations, '
               'basis-variable evaluations, reversible elimination operations and provenance checked.',
               'cases': summaries, 'failures': []}
    result_path = directory / 'staged-bit-basis-receipt.json'
    result_path.write_text(json.dumps(receipt, indent=2) + '\n')
    for summary in summaries:
        print(f'N={summary["N"]}: received {summary["graphs_received"]} graphs, '
              f'{summary["arrows_received"]} arrows and both entire central systems; '
              f'charge={summary["total"]}, required scale={summary["required_scale"]}')
    print(f'Failures: []; complete receipt: {result_path}')


if __name__ == '__main__':
    main()
