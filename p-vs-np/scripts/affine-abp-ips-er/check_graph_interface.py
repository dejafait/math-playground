#!/usr/bin/env python3
"""Finite graph-interface checks for L038; not a propositional proof verifier."""
from itertools import product
from pathlib import Path
import json
import random
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'shared-abp'))
from check_formula_assembly import component_tables
from check_witnesses import row_product, witnesses, check_tables


def add(a, b):
    return a ^ b


def mul(a, b):
    out = set()
    for u in a:
        for v in b:
            out ^= {u + v}
    return out


def direct(g, images):
    """Independent topological formal-polynomial evaluation of affine labels."""
    values = [set() for _ in range(g['vertices'])]
    values[g['source']] = {()}
    for v in range(g['vertices']):
        for u, w, label in g['edges']:
            if u == v:
                p = set()
                for symbol in label:
                    p ^= {()} if symbol is None else images[symbol]
                values[w] ^= mul(values[u], p)
    return values[g['sink']]


def replace(g, images, plus_one=False):
    """Disjoint monomial gadgets, fresh endpoints, then topological renumbering."""
    edges = []
    count = g['vertices'] + 2
    alpha, omega = g['vertices'], g['vertices'] + 1
    edges.extend([(alpha, g['source'], None), (g['sink'], omega, None)])
    if plus_one:
        edges.append((alpha, omega, None))
    occurrences = 0
    for u, v, label in g['edges']:
        for symbol in label:
            words = {()} if symbol is None else images[symbol]
            for word in sorted(words):
                occurrences += 1
                previous = u
                if not word:
                    edges.append((u, v, None))
                for j, letter in enumerate(word):
                    nxt = v if j == len(word) - 1 else count
                    if nxt == count:
                        count += 1
                    edges.append((previous, nxt, letter))
                    previous = nxt
    incoming = [0] * count
    outgoing = [[] for _ in range(count)]
    for u, v, _ in edges:
        incoming[v] += 1
        outgoing[u].append(v)
    # Prefer alpha first and omega last among available vertices.
    available = [v for v in range(count) if incoming[v] == 0]
    order = []
    while available:
        v = min(available, key=lambda q: (-1 if q == alpha else count if q == omega else q))
        available.remove(v)
        order.append(v)
        for w in outgoing[v]:
            incoming[w] -= 1
            if incoming[w] == 0:
                available.append(w)
    assert len(order) == count and order[0] == alpha and order[-1] == omega
    index = {v: j for j, v in enumerate(order)}
    result = [(index[u], index[v], ('c', 1) if a is None else ('x', a))
              for u, v, a in edges]
    assert all(u < v for u, v, _ in result)
    # Each axiom has <=8 words of length <=3.
    entries = sum(len(label) for _, _, label in g['edges'])
    assert count <= g['vertices'] + 2 + 16 * entries
    assert len(result) <= 3 + 24 * entries
    return count, result, {'label_entries': entries, 'word_gadgets': occurrences,
                           'vertices': count, 'vertex_bound': g['vertices'] + 2 + 16 * entries,
                           'edges': len(result), 'edge_bound': 3 + 24 * entries}


def examine(name, g, images, plus_one=False):
    expected = direct(g, images) ^ ({()} if plus_one else set())
    vertices, edges, ledger = replace(g, images, plus_one)
    constants, variable, closure, step, first = component_tables(vertices, edges, 2)
    rows = {(): closure[0]}
    components = [[[]] if closure[0] >> (vertices - 1) & 1 else []]
    for k in range(1, vertices):
        nxt = {}
        for word, row in rows.items():
            for a, matrix in enumerate(step):
                image = row_product(row, matrix)
                if image:
                    nxt[word + (a,)] = image
        rows = nxt
        component = {word for word, row in rows.items() if row >> (vertices - 1) & 1}
        assert component == {w for w in expected if len(w) == k}
        assert all(row & ((1 << k) - 1) == 0 for row in rows.values())
        components.append([list(w) for w in sorted(component)])
    assert set(map(tuple, components[0])) == {w for w in expected if not w}
    assert all(row_product(row, m) == 0 for row in rows.values() for m in step)
    layers = [first] + [step] * (vertices - 2)
    widths = [1] + [vertices] * (vertices - 1)
    basis, transitions = witnesses(widths, layers)
    check_tables(widths, layers, basis, transitions)
    for k in range(1, vertices):
        assert (not any(row >> (vertices - 1) & 1 for row in basis[k])) == (not components[k])
    values = []
    boundary_nonzero = False
    for assignment in product((0, 1), repeat=2):
        p = [0] * vertices
        p[0] = 1
        for u in range(vertices):
            for a, v, label in edges:
                if a == u:
                    p[v] ^= p[u] & (1 if label[0] == 'c' else assignment[label[1]])
        h = closure[0]
        total = h
        for k in range(1, vertices):
            h = row_product(h, [variable[0][u] * assignment[0] ^ variable[1][u] * assignment[1]
                                  for u in range(vertices)])
            h = row_product(h, closure)
            total ^= h
        boundary_nonzero |= bool(h)
        assert all(row_product(h, m) == 0 for m in step)
        assert total == sum(bit << v for v, bit in enumerate(p))
        assert p[-1] == (sum(all(assignment[a] for a in word) for word in expected) % 2)
        values.append({'assignment': list(assignment), 'graph_row': total, 'last_row': h})
    return {'name': name, 'input': g, 'images': {k: [list(w) for w in sorted(v)] for k, v in images.items()},
            'plus_one': plus_one, 'normalized_vertices': vertices, 'normalized_edges': edges,
            'polynomial': [list(w) for w in sorted(expected)], 'components': components,
            'closure': closure, 'step': step, 'first': first, 'basis': basis,
            'transitions': transitions, 'assignments': values, 'ledger': ledger,
            'formal_zero': not expected, 'last_row_nonzero': boundary_nonzero}


def main():
    x, y = {(0,)}, {(1,)}
    axioms = {'x': x, 'y': y, 't0': {()} ^ x, 't1': x,
              't2': mul({()} ^ y, y), 't3': mul(x, x) ^ x,
              't4': mul(y, y) ^ y, 't5': mul(x, y) ^ mul(y, x)}
    zero = {key: val if key in ('x', 'y') else set() for key, val in axioms.items()}
    identity = {'x': x, 'y': y}
    cases = []
    def case(name, n, edges, s=0, t=None, images=identity, one=False):
        cases.append(examine(name, {'vertices': n, 'edges': edges, 'source': s,
                                   'sink': n - 1 if t is None else t}, images, one))
    case('coincident-nonextremal', 4, [(0, 1, ['x']), (1, 2, ['y']), (2, 3, [None])], 1, 1)
    case('no-path', 4, [(0, 1, ['x']), (2, 3, ['y'])], 1, 2)
    case('affine-cancellation', 3, [(0, 2, [None, 'x', 'x', 'y']), (0, 2, ['y']),
                                   (0, 1, ['x']), (1, 2, ['y'])])
    case('boundary-row-nonzero', 2, [(0, 1, ['x'])])
    # Internal source/sink, shared vertices and nonlinear placeholders; two x^2 paths cancel.
    cert = [(0, 1, ['y']), (1, 5, ['t0', 't1']), (1, 2, ['t0']), (2, 5, ['t1']),
            (1, 3, ['t1']), (3, 5, ['t0']), (1, 4, ['x']), (1, 4, ['x']),
            (4, 5, ['x']), (5, 6, ['y'])]
    case('ips-zero-nonlinear-cancellation', 7, cert, 1, 5, zero)
    case('ips-one-nonlinear-cancellation', 7, cert, 1, 5, axioms, True)
    assert cases[-1]['formal_zero'] and cases[-2]['formal_zero']
    rng = random.Random(38091)
    alphabet = list(axioms) + [None]
    for j in range(24):
        n = rng.randrange(2, 8)
        edges = [(u, v, [rng.choice(alphabet) for _ in range(rng.randrange(4))])
                 for u in range(n) for v in range(u + 1, n) if rng.random() < .35]
        s, t = rng.randrange(n), rng.randrange(n)
        case(f'random-{j}-zero-substitution', n, edges, s, t, zero)
        case(f'random-{j}-axiom-substitution', n, edges, s, t, axioms)
    # Missing trailing closure must be detected even for x followed by a constant edge.
    n, edges, _ = replace({'vertices': 3, 'source': 0, 'sink': 2,
                           'edges': [(0, 1, ['x']), (1, 2, [None])]}, identity)
    _, variable, closure, step, _ = component_tables(n, edges, 2)
    correct = row_product(closure[0], step[0])
    damaged = row_product(closure[0], variable[0])
    assert (correct >> (n - 1) & 1) and not (damaged >> (n - 1) & 1)
    # Endpoint wrappers add constants, so their top-degree row is zero.
    # Check the nonzero-last-row case directly on an unwrapped linear graph.
    bc, bv, bk, bg, bf = component_tables(2, [(0, 1, ('x', 0))], 2)
    last = row_product(bk[0], bg[0])
    after = [row_product(last, matrix) for matrix in bg]
    assert last == 2 and after == [0, 0]
    boundary = {'vertices': 2, 'edges': [(0, 1, ('x', 0))], 'constants': bc,
                'variable': bv, 'closure': bk, 'step': bg, 'first': bf,
                'assignment': [1, 0], 'last_row': last, 'next_rows': after}
    summary = {'cases': len(cases), 'assignment_checks': sum(len(c['assignments']) for c in cases),
               'components': sum(len(c['components']) for c in cases), 'failures': [],
               'mutation_detected': True, 'proof_strings_verified': False,
               'separate_nonzero_last_row_test': True,
               'max_vertices': max(c['normalized_vertices'] for c in cases)}
    output = Path(__file__).with_name('graph-interface-results.json')
    output.write_text(json.dumps({'summary': summary, 'cases': cases,
                                 'boundary': boundary,
                                 'mutation': {'correct_row': correct, 'damaged_row': damaged,
                                              'sink': n - 1}}, indent=2) + '\n')
    print(json.dumps(summary))
    print('Bounds: each case ledger records actual/required vertices and edges; all pass.')
    print(f'Full certificate: {output}')


if __name__ == '__main__':
    main()
