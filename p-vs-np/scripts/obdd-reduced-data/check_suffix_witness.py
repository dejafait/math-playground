"""Exact finite free-word tests of the shared OBDD suffix construction.

No Boolean quotient reduction is used in comparing substituted polynomials.
The complete finite evidence and arithmetic DAGs are written to disk.
"""
import json
from functools import lru_cache
from pathlib import Path

ZERO, ONE = frozenset(), frozenset({()})


def add(*ps):
    out = set()
    for p in ps:
        out.symmetric_difference_update(p)
    return frozenset(out)


def mul(a, b):
    out = set()
    for u in a:
        for v in b:
            word = u + v
            if word in out:
                out.remove(word)
            else:
                out.add(word)
    return frozenset(out)


def var(name):
    return frozenset({(name,)})


def degree(p):
    return max(map(len, p), default=0)


def enc(p):
    return [list(word) for word in sorted(p)]


def substitute(p, mapping):
    out = ZERO
    for word in p:
        term = ONE
        for name in word:
            term = mul(term, mapping.get(name, var(name)))
        out = add(out, term)
    return out


class DAG:
    def __init__(self):
        self.nodes = []
        self.index = {}
        self.zero = self.node(('const', 0))
        self.one = self.node(('const', 1))

    def node(self, record):
        if record not in self.index:
            self.index[record] = len(self.nodes)
            self.nodes.append(record)
        return self.index[record]

    def variable(self, name):
        return self.node(('var', name))

    def plus(self, *roots):
        out = self.zero
        for root in roots:
            out = self.node(('add', out, root))
        return out

    def times(self, *roots):
        out = self.one
        for root in roots:
            out = self.node(('mul', out, root))
        return out

    def evaluate(self, mapping=None):
        mapping = mapping or {}
        values, syntactic = [], []
        for rec in self.nodes:
            if rec[0] == 'const':
                p, d = (ONE if rec[1] else ZERO), 0
            elif rec[0] == 'var':
                p, d = mapping.get(rec[1], var(rec[1])), 1
            elif rec[0] == 'add':
                p = add(values[rec[1]], values[rec[2]])
                d = max(syntactic[rec[1]], syntactic[rec[2]])
            else:
                p = mul(values[rec[1]], values[rec[2]])
                d = syntactic[rec[1]] + syntactic[rec[2]]
            values.append(p)
            syntactic.append(d)
        return values, syntactic


def diagram(table, n, expanded=False):
    """Explicit dense layers; terminals are bits. Optionally keep duplicates."""
    layers = [[] for _ in range(n)]
    maps = [{} for _ in range(n)]

    def visit(k, suffix):
        if k == n:
            return suffix[0]
        if not expanded and suffix in maps[k]:
            return maps[k][suffix]
        mid = len(suffix) // 2
        children = (visit(k + 1, suffix[:mid]), visit(k + 1, suffix[mid:]))
        idx = len(layers[k])
        layers[k].append(children)
        maps[k][suffix] = idx
        return idx

    root = visit(0, tuple(table))
    return {'layers': layers, 'root': root, 'table': list(table)}


def case(n, af, bf, signs=(0, 0), expanded=False, reverse_order=False):
    order = list(reversed(range(n))) if reverse_order else list(range(n))
    at = [(af >> j) & 1 for j in range(1 << n)]
    bt = [(bf >> j) & 1 for j in range(1 << n)]
    ct = [(a ^ signs[0]) & (b ^ signs[1]) for a, b in zip(at, bt)]
    diagrams = [diagram(at, n, expanded), diagram(bt, n, not expanded),
                diagram(ct, n, expanded)]
    dag = DAG()
    xs = [dag.variable('x' + str(j)) for j in order]
    es = [(dag.plus(dag.one, x), x) for x in xs]
    axioms = {}
    for j in range(n):
        x = var('x' + str(j))
        axioms['b' + str(j)] = add(mul(x, x), x)
        for k in range(j + 1, n):
            y = var('x' + str(k))
            axioms['c' + str(j) + '_' + str(k)] = add(mul(x, y), mul(y, x))

    def child(di, level, state, bit):
        return diagrams[di]['layers'][level][state][bit]

    @lru_cache(None)
    def rep(di, k, state, sign):
        if k == n:
            return dag.one if state ^ sign else dag.zero
        return dag.plus(*(dag.times(es[k][bit], rep(di, k + 1, child(di, k, state, bit), sign))
                          for bit in (0, 1)))

    @lru_cache(None)
    def commute(di, k, state, sign, early):
        if k == n:
            return dag.zero
        assert early < k
        u = [child(di, k, state, bit) for bit in (0, 1)]
        a, b = sorted((order[early], order[k]))
        c = dag.variable('c' + str(a) + '_' + str(b))
        return dag.plus(*(dag.times(es[k][bit], commute(di, k + 1, u[bit], sign, early))
                          for bit in (0, 1)),
                        dag.times(c, dag.plus(*(rep(di, k + 1, s, sign) for s in u))))

    @lru_cache(None)
    def pair(k, u, v):
        if k == n:
            return (dag.one if (u ^ signs[0]) & (v ^ signs[1]) else dag.zero,
                    dag.zero, dag.zero, dag.zero, dag.zero)
        us = [child(0, k, u, bit) for bit in (0, 1)]
        vs = [child(1, k, v, bit) for bit in (0, 1)]
        ur = [rep(0, k + 1, s, signs[0]) for s in us]
        vr = [rep(1, k + 1, s, signs[1]) for s in vs]
        lower = [pair(k + 1, us[bit], vs[bit]) for bit in (0, 1)]
        p = dag.plus(*(dag.times(es[k][bit], lower[bit][0]) for bit in (0, 1)))
        kval = dag.plus(*(dag.times(es[k][bit], commute(0, k + 1, us[bit], signs[0], k))
                         for bit in (0, 1)))
        vsum = dag.plus(*vr)
        kt = dag.times(kval, vsum)
        bt = dag.times(dag.variable('b' + str(order[k])), dag.plus(*ur), vsum)
        w = dag.plus(kt, bt, *(dag.times(es[k][bit], lower[bit][1]) for bit in (0, 1)))
        return p, w, kt, bt, dag.times(vsum, kval)

    roots = [d['root'] for d in diagrams]
    positive = [rep(di, 0, roots[di], 0) for di in range(3)]
    negative = [rep(di, 0, roots[di], 1) for di in range(3)]
    exact_signed = [dag.plus(dag.one, positive[di]) if signs[di] else positive[di] for di in (0, 1)]
    p, h, kt, bt, reversed_kt = pair(0, roots[0], roots[1])
    # Populate/check every suffix commutator, not only those needed at this root.
    comm_checks = []
    for di, d in enumerate(diagrams):
        for k, states in enumerate(d['layers']):
            for state in range(len(states)):
                for sign in (0, 1):
                    for early in range(k):
                        r = rep(di, k, state, sign)
                        c = commute(di, k, state, sign, early)
                        comm_checks.append((r, c, early, n - k))
    formal, syntactic = dag.evaluate()
    actual, _ = dag.evaluate(axioms)
    zero, _ = dag.evaluate({name: ZERO for name in axioms})
    expected = add(formal[positive[2]], mul(formal[exact_signed[0]], formal[exact_signed[1]]))
    failures = []
    def check(condition, label):
        if not condition:
            failures.append(label)
    check(formal[p] == formal[positive[2]], 'ordered_output_identification')
    check(actual[h] == expected, 'H_axiom_identity')
    check(zero[h] == ZERO, 'H_zero_identity')
    for di in range(3):
        check(formal[negative[di]] == add(ONE, formal[positive[di]]), 'exact_complement')
    for r, c, early, bound in comm_checks:
        x = formal[xs[early]]
        check(actual[c] == add(mul(formal[r], x), mul(x, formal[r])), 'suffix_commutator')
        check(zero[c] == ZERO and syntactic[c] <= bound, 'commutator_zero_or_degree')
    dbound, hbound = max(1, n), max(1, 2 * n - 1)
    check(max(syntactic[r] for r in positive + negative) <= dbound, 'value_degree')
    check(syntactic[h] <= hbound, 'witness_syntactic_degree')
    check(all(sum(name.startswith(('b', 'c')) for name in word) == 1 for word in formal[h]),
          'placeholder_linearity')
    mutations = {'omit_commutator': add(actual[h], actual[kt]) != expected,
                 'omit_boolean': add(actual[h], actual[bt]) != expected,
                 'reverse_coefficient': add(actual[h], actual[kt], actual[reversed_kt]) != expected}
    width = max([1] + [len(layer) for d in diagrams for layer in d['layers']])
    return {'n': n, 'order': order, 'signs': signs, 'diagrams': diagrams,
            'gates': dag.nodes, 'roots': {'values': positive, 'signed_operands': exact_signed,
                                       'ordered_product': p, 'H': h},
            'axioms': {name: enc(polynomial) for name, polynomial in axioms.items()},
            'formal_H': enc(formal[h]), 'substituted_H': enc(actual[h]), 'required_H': enc(expected),
            'zero_H': enc(zero[h]), 'failures': failures, 'mutations_detected': mutations,
            'bounds': {'width': width, 'gates': len(dag.nodes), 'value_actual': max(syntactic[r] for r in positive + negative),
                       'value_required': dbound, 'H_formal_actual': degree(formal[h]),
                       'H_syntactic_actual': syntactic[h], 'H_required': hbound},
            'commutator_checks': len(comm_checks)}


def local_identity():
    # A separate generic free-algebra identity, with no suffix Boolean promise.
    x, u0, u1, v0, v1, p0, p1 = map(var, ['x', 'u0', 'u1', 'v0', 'v1', 'p0', 'p1'])
    e0, e1 = add(ONE, x), x
    k0, k1, b, w0, w1 = map(var, ['k0', 'k1', 'b', 'w0', 'w1'])
    witness = add(mul(add(mul(e0, k0), mul(e1, k1)), add(v0, v1)),
                  mul(mul(b, add(u0, u1)), add(v0, v1)), mul(e0, w0), mul(e1, w1))
    mapping = {'k0': add(mul(u0, x), mul(x, u0)), 'k1': add(mul(u1, x), mul(x, u1)),
               'b': add(mul(x, x), x), 'w0': add(mul(u0, v0), p0), 'w1': add(mul(u1, v1), p1)}
    required = add(mul(add(mul(e0, u0), mul(e1, u1)), add(mul(e0, v0), mul(e1, v1))),
                   mul(e0, p0), mul(e1, p1))
    actual = substitute(witness, mapping)
    zero = substitute(witness, {name: ZERO for name in mapping})
    return {'witness': enc(witness), 'mapping': {k: enc(v) for k, v in mapping.items()},
            'actual': enc(actual), 'required': enc(required), 'zero': enc(zero),
            'passed': actual == required and zero == ZERO}


def main():
    cases = []
    for n in (0, 1, 2):
        count = 1 << (1 << n)
        for a in range(count):
            for b in range(count):
                cases.append(case(n, a, b, expanded=(a + b) % 2 == 0))
    for n, a, b in [(1, 2, 1), (2, 6, 9), (2, 8, 14), (3, 150, 232),
                     (3, 128, 254), (3, 0, 255), (3, 170, 204), (3, 105, 23)]:
        for sa in (0, 1):
            for sb in (0, 1):
                cases.append(case(n, a, b, (sa, sb), expanded=True, reverse_order=True))
    local = local_identity()
    failures = [{'case': i, 'errors': c['failures']} for i, c in enumerate(cases) if c['failures']]
    mutations = {name: sum(c['mutations_detected'][name] for c in cases)
                 for name in ('omit_commutator', 'omit_boolean', 'reverse_coefficient')}
    if not local['passed']:
        failures.append({'local_identity': 'failed'})
    for name, count in mutations.items():
        if not count:
            failures.append({'mutation_undetected': name})
    summary = {'cases': len(cases), 'suffix_commutator_checks': sum(c['commutator_checks'] for c in cases),
               'failures': failures, 'mutations_detected': mutations,
               'max_actual_value_degree': max(c['bounds']['value_actual'] for c in cases),
               'required_value_bound': 'max(1,n)',
               'max_actual_H_syntactic_degree': max(c['bounds']['H_syntactic_actual'] for c in cases),
               'required_H_bound': 'max(1,2n-1)', 'generic_identity_passed': local['passed']}
    path = Path(__file__).with_name('suffix-witness-results.json')
    path.write_text(json.dumps({'summary': summary, 'generic_local_identity': local, 'cases': cases}, separators=(',', ':')) + '\n')
    print(json.dumps(summary, indent=2))
    print('Complete certificate:', path.relative_to(Path.cwd()))
    raise SystemExit(bool(failures))


if __name__ == '__main__':
    main()
