"""Independent backward replay of L037's saved finite graph certificate.

No constructor/evaluator imports. The all-input proof remains in L037.
"""
from collections import Counter
from hashlib import sha256
import json
from pathlib import Path


def add(*polys):
    counts = Counter(w for p in polys for w in p)
    return frozenset(w for w, n in counts.items() if n % 2)


def mul(a, b):
    counts = Counter(u + v for u in a for v in b)
    return frozenset(w for w, n in counts.items() if n % 2)


ONE = frozenset([()])
ZERO = frozenset()


def decode(p):
    return frozenset(map(tuple, p))


def encode(p):
    return [list(w) for w in sorted(p)]


def backward(g, axioms, mode, target=None):
    """Sum all paths to target, including its empty path and arbitrary roots."""
    target = g['sink'] if target is None else target
    adj = [[] for _ in range(g['vertices'])]
    indeg = [0] * len(adj)
    for u, v, label in g['edges']:
        adj[u].append((v, label))
        indeg[v] += 1
    order = [u for u, d in enumerate(indeg) if d == 0]
    for u in order:
        for v, _ in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                order.append(v)
    assert len(order) == len(adj), 'cycle'
    val = [ZERO] * len(adj)
    for u in reversed(order):
        terms = [ONE] if u == target else []
        for v, label in adj[u]:
            terms.append(mul(add(*(ONE if s == '1' else
                                  ZERO if s in axioms and mode == 'zero' else
                                  axioms[s] if s in axioms and mode == 'axioms' else
                                  frozenset([(s,)]) for s in label)), val[v]))
        val[u] = add(*terms)
    return val[g['source']]


def run():
    path = Path(__file__).with_name('assembly-results.json')
    raw = path.read_bytes()
    data = json.loads(raw)
    failures, checks = [], []

    def check(name, condition):
        checks.append({'name': name, 'passed': bool(condition)})
        if not condition:
            failures.append(name)

    axioms = {k: decode(v) for k, v in data['axioms'].items()}
    reps = {int(k): backward(g, axioms, 'free')
            for k, g in data['supplied_representatives'].items()}

    def factors(clause):
        p = ONE
        for lit in clause:
            p = mul(p, add(ONE, reps[lit]) if lit > 0 else reps[-lit])
        return p

    # Check the full axiom dictionary, with no trusted stored target.
    expected_axioms = {f'b:{i}': decode([[f'x{i}', f'x{i}'], [f'x{i}']])
                       for i in (1, 2, 3)}
    expected_axioms.update({f't:{i}:{j}': decode([[f'x{i}', f'x{j}'], [f'x{j}', f'x{i}']])
                            for i in (1, 2, 3) for j in range(i + 1, 4)})
    expected_axioms.update({f'c:{i}': factors(c) for i, c in enumerate(data['source']['F'])})
    check('full_dictionary', axioms == expected_axioms)
    H = data['supplied_H']
    check('H_zero', backward(H, axioms, 'zero') == ZERO)
    check('H_relation', backward(H, axioms, 'axioms') == add(reps[4], mul(reps[1], reps[2])))
    check('H_saved_free', backward(H, axioms, 'free') == decode(data['H_free']))
    check('H_saved_substitution', backward(H, axioms, 'axioms') == decode(data['H_substituted']))

    # Independently validate this diagnostic's selected-pivot ER source.
    proof = data['source']['pi']
    clauses, definitions = [], {}
    seen = {abs(l) for c in data['source']['F'] for l in c}
    for i, record in enumerate(proof):
        c = set(record['clause'])
        kind = record['kind']
        check(f'line_{i}_sorted_set', record['clause'] == sorted(c, key=lambda l: (abs(l), l < 0)))
        if kind == 'input':
            valid = c == set(data['source']['F'][record['source'] - 1])
        elif kind == 'ext':
            z, a, b = (record[k] for k in ('z', 'a', 'b'))
            if z not in definitions:
                check(f'line_{i}_fresh_definition', z not in seen and abs(a) in seen and abs(b) in seen)
                definitions[z] = (a, b)
                seen.add(z)
            valid = definitions[z] == (a, b) and c == [{-z, a}, {-z, b}, {z, -a, -b}][record['part'] - 1]
        elif kind == 'weak':
            j = record['source'] - 1
            valid = 0 <= j < i and clauses[j] <= c
        else:
            j, k, p = record['left'] - 1, record['right'] - 1, record['pivot']
            valid = (0 <= j < i and 0 <= k < i and p in clauses[j] and -p in clauses[k]
                     and c == (clauses[j] - {p}) | (clauses[k] - {-p}))
        check(f'line_{i}_ER_rule', valid)
        clauses.append(c)
    check('empty_final_clause', not clauses[-1])

    out = data['output_graph']
    replay = []
    for i, line in enumerate(data['lines']):
        values = {mode: backward(out, axioms, mode, line['node'])
                  for mode in ('free', 'zero', 'axioms')}
        target = factors(line['clause'])
        check(f'line_{i}_source_agreement', line['clause'] == proof[i]['clause'])
        for mode, saved in [('free', 'free'), ('zero', 'zero'), ('axioms', 'substituted')]:
            check(f'line_{i}_{mode}_saved', values[mode] == decode(line['polynomials'][saved]))
        check(f'line_{i}_zero', values['zero'] == ZERO)
        check(f'line_{i}_substitution', values['axioms'] == target)
        check(f'line_{i}_saved_target', target == decode(line['polynomials']['target']))
        replay.append({'line': i, 'polynomials': {k: encode(v) for k, v in values.items()},
                       'target': encode(target)})

    # Count real copied interiors and exterior connectors from the saved layout.
    # The ledger claims the size of each copy; verify its entire edge interval.
    position, edge_position = 2, 0
    blocks = []
    for i, line in enumerate(data['lines']):
        check(f'line_{i}_vertex_allocation', line['node'] == position)
        position += 1
        for block in [b for b in data['ledger'] if b['line'] == i]:
            lo, hi = position, position + block['vertices']
            interior = out['edges'][edge_position:edge_position + block['edges']]
            connectors = out['edges'][edge_position + block['edges']:edge_position + block['edges'] + 2]
            valid = (len(interior) == block['edges'] and len(connectors) == 2
                     and all(lo <= u < hi and lo <= v < hi for u, v, _ in interior)
                     and connectors[0][0] == block['start'] and lo <= connectors[0][1] < hi
                     and lo <= connectors[1][0] < hi and connectors[1][1] == line['node']
                     and connectors[0][2] == connectors[1][2] == ['1'])
            check(f'block_{len(blocks)}_complete_copy', valid)
            blocks.append({'line': i, 'vertices': hi - lo, 'edges': len(interior), 'valid': valid})
            position = hi
            edge_position += block['edges'] + 2
    check('final_edge_only', out['edges'][edge_position:] == [[data['lines'][-1]['node'], out['sink'], ['1']]])
    check('vertices_exact', position == out['vertices'])
    check('edges_exact', edge_position + 1 == len(out['edges']))
    final = {m: backward(out, axioms, m) for m in ('free', 'zero', 'axioms')}
    degree = max(map(len, final['free']), default=0)
    check('IPS_zero', final['zero'] == ZERO)
    check('IPS_one', final['axioms'] == ONE)
    bounds = {'vertices_actual': out['vertices'], 'vertices_required': position,
              'edges_actual': len(out['edges']), 'edges_required': edge_position + 1,
              'formal_degree_actual': degree, 'formal_degree_upper': out['vertices'] - 1}
    check('degree_bound', degree <= out['vertices'] - 1)
    check('saved_bounds', bounds == data['bounds'])
    for i, boundary in enumerate(data['boundaries']):
        g = backward(boundary['input'], axioms, 'free')
        h = backward(H, axioms, 'free')
        expected = mul(mul(g, h), g)
        actual = backward(boundary['composite'], axioms, 'free')
        check(f'boundary_{i}_composition', actual == expected)
        check(f'boundary_{i}_saved_actual', actual == decode(boundary['composition_actual']))
        check(f'boundary_{i}_saved_required', expected == decode(boundary['composition_required']))
        check(f'boundary_{i}_W', backward(boundary['W'], axioms, 'axioms') == add(mul(g, reps[2]), mul(reps[2], g)))
        check(f'boundary_{i}_zero', backward(boundary['W'], axioms, 'zero') == ZERO)

    # A same-parent two-transition graph with cancellation-based local zeros.
    # Local L0 has two placeholder-free x1 paths and one b:1 path. L1 has
    # two placeholder-free x2 paths. Both transitions reuse the same v0;
    # different multipliers x1,x2 make loss of either occurrence detectable.
    extra = {'vertices': 5, 'source': 0, 'sink': 4,
             'edges': [[0, 1, ['x1']], [0, 1, ['x1']], [0, 1, ['b:1']],
                       [0, 3, ['x2']], [0, 3, ['x2']],
                       [1, 3, ['x1']], [1, 3, ['x2']], [3, 4, ['1']]]}
    extra_values = {m: backward(extra, axioms, m) for m in ('free', 'zero', 'axioms')}
    wanted = decode([['b:1', 'x1'], ['b:1', 'x2']])
    check('repeated_parent_free', extra_values['free'] == wanted)
    check('cancellation_based_zero', extra_values['zero'] == ZERO)
    check('repeated_parent_substitution', extra_values['axioms'] == mul(axioms['b:1'], decode([['x1'], ['x2']])))
    mutant = {**extra, 'edges': extra['edges'][:5] + extra['edges'][6:]}
    check('deleted_parent_occurrence_detected', backward(mutant, axioms, 'free') != wanted)
    check('source_certificate_unchanged', path.read_bytes() == raw)
    result = {'scope': 'Independent finite audit only; all-input proof is canonical in L037.',
              'source_sha256': sha256(raw).hexdigest(), 'summary': {'checks': len(checks),
              'failures': failures, 'lines': len(replay), 'boundary_cases': len(data['boundaries'])},
              'checks': checks, 'bounds': bounds, 'blocks': blocks, 'lines': replay,
              'final': {m: encode(p) for m, p in final.items()},
              'extra_graph': extra, 'extra_values': {m: encode(p) for m, p in extra_values.items()},
              'mutation_graph': mutant}
    dest = path.with_name('assembly-audit-results.json')
    dest.write_text(json.dumps(result, indent=2) + '\n')
    print('Summary:', json.dumps(result['summary']))
    print('Actual/required bounds:', json.dumps(bounds))
    print('Full certificate:', dest)
    assert not failures, failures


if __name__ == '__main__':
    run()
