#!/usr/bin/env python3
"""Exact free-word diagnostics for L029; small n is not an all-n proof."""
import importlib.util
import json
from functools import lru_cache
from pathlib import Path

SOURCE = Path(__file__).parents[1] / 'hwb-reduced-data' / 'check_data.py'
spec = importlib.util.spec_from_file_location('fixed_hwb', SOURCE)
old = importlib.util.module_from_spec(spec)
spec.loader.exec_module(old)


class DAG:
    def __init__(self, n):
        self.nodes, self.degrees, self.index = [], [], {}
        self.zero, self.one = self.put('const', 0), self.put('const', 1)
        self.x = {i: self.put('var', i) for i in range(1, n + 1)}
        self.b = {i: self.put('bool', i) for i in self.x}
        self.c = {(i, j): self.put('comm', i, j) for i in self.x for j in self.x if i < j}

    def put(self, op, *args):
        key = (op, *args)
        if key in self.index:
            return self.index[key]
        idx = len(self.nodes)
        self.index[key] = idx
        self.nodes.append(key)
        if op == 'const':
            degree = 0
        elif op in ('var', 'bool', 'comm'):
            degree = 1
        elif op == 'add':
            degree = max(self.degrees[a] for a in args)
        else:
            degree = sum(self.degrees[a] for a in args)
        self.degrees.append(degree)
        return idx

    def add(self, *args):
        out = self.zero
        for a in args:
            if out == self.zero:
                out = a
            elif a == out:
                out = self.zero
            elif a != self.zero:
                out = self.put('add', out, a)
        return out

    def mul(self, *args):
        out = self.one
        for a in args:
            if a == self.zero or out == self.zero:
                out = self.zero
            elif out == self.one:
                out = a
            elif a != self.one:
                out = self.put('mul', out, a)
        return out

    def words(self, mode):
        values = []
        for op, *args in self.nodes:
            if op == 'const':
                p = {()} if args[0] else set()
            elif op == 'var':
                p = {(f'x{args[0]}',)}
            elif op in ('bool', 'comm'):
                if mode == 'zero':
                    p = set()
                elif mode == 'formal':
                    p = {(op + ':' + ':'.join(map(str, args)),)}
                elif op == 'bool':
                    x = f'x{args[0]}'
                    p = {(x, x), (x,)}
                else:
                    x, y = (f'x{i}' for i in args)
                    p = {(x, y), (y, x)}
            elif op == 'add':
                p = values[args[0]] ^ values[args[1]]
            else:
                p = old.word_product(values[args[0]], values[args[1]])
            values.append(p)
        return values


def enc(poly):
    return [list(w) for w in sorted(poly)]


def run(n):
    proof, prior, positive, signed, _, _, prefixes = old.build_data(n)
    dag = DAG(n)

    @lru_cache(None)
    def copy(root):
        op, *args = prior.nodes[root]
        if op == 'const':
            return dag.one if args[0] else dag.zero
        if op == 'var':
            return dag.x[args[0]]
        assert op in ('add', 'mul'), 'A fixed root reached a clause placeholder'
        return (dag.add if op == 'add' else dag.mul)(*(copy(a) for a in args))

    actual = {v: copy(r) for v, r in positive.items()}
    actual.update({-v: copy(r) for v, r in signed.items()})
    diagrams, atom_ids = [], {}

    def atom(t, weight, literal=0, bit=0):
        key = (t, weight, literal, bit)
        if key in atom_ids:
            return atom_ids[key]
        states = []

        @lru_cache(None)
        def visit(k, count):
            if k == n + 1:
                return int(count == weight and count != -1)
            children = []
            for value in (0, 1):
                nxt = count
                if count == -1 or (k == literal and value != bit):
                    nxt = -1
                elif k <= t:
                    nxt += value
                children.append(visit(k + 1, nxt))
            idx = len(states) + 2
            states.append([k, *children])
            return idx

        root = visit(1, 0)
        idx = len(diagrams)
        widths = [sum(s[0] == k for s in states) for k in range(1, n + 1)]
        assert max(widths) <= n + 2
        diagrams.append(dict(spec=list(key), root=root, states=states, widths=widths))
        atom_ids[key] = idx
        return idx

    def state(di, sid):
        return diagrams[di]['states'][sid - 2]

    @lru_cache(None)
    def rep(di, sid):
        if sid < 2:
            return dag.one if sid else dag.zero
        k, lo, hi = state(di, sid)
        return dag.add(dag.mul(dag.add(dag.one, dag.x[k]), rep(di, lo)),
                       dag.mul(dag.x[k], rep(di, hi)))

    @lru_cache(None)
    def comm(di, sid, early):
        if sid < 2:
            return dag.zero
        k, lo, hi = state(di, sid)
        assert early < k
        return dag.add(dag.mul(dag.add(dag.one, dag.x[k]), comm(di, lo, early)),
                       dag.mul(dag.x[k], comm(di, hi, early)),
                       dag.mul(dag.c[early, k], dag.add(rep(di, lo), rep(di, hi))))

    @lru_cache(None)
    def pair(di, si, dj, sj):
        if si < 2:
            assert sj < 2
            return (dag.one if si * sj else dag.zero), dag.zero
        k, u0, u1 = state(di, si)
        kk, v0, v1 = state(dj, sj)
        assert k == kk
        p0, w0 = pair(di, u0, dj, v0)
        p1, w1 = pair(di, u1, dj, v1)
        e0, e1 = dag.add(dag.one, dag.x[k]), dag.x[k]
        us = dag.add(rep(di, u0), rep(di, u1))
        vs = dag.add(rep(dj, v0), rep(dj, v1))
        p = dag.add(dag.mul(e0, p0), dag.mul(e1, p1))
        w = dag.add(dag.mul(dag.add(dag.mul(e0, comm(di, u0, k)),
                                     dag.mul(e1, comm(di, u1, k))), vs),
                    dag.mul(dag.b[k], us, vs), dag.mul(e0, w0), dag.mul(e1, w1))
        return p, w

    def atom_pair(a, b):
        return pair(a, diagrams[a]['root'], b, diagrams[b]['root'])

    one = atom(0, 0)
    zero = atom(0, 1)

    def q(i, j):
        return atom(i, j) if 0 <= j <= i else zero

    lists = {v: {atom(0, 0, v, 1)} for v in range(1, n + 1)}
    bridge = {v: dag.zero for v in lists}
    for v in list(lists):
        lists[-v], bridge[-v] = lists[v] ^ {one}, dag.zero
    cursor = 0
    kinds = {}

    def assign(kind, terms, d=dag.zero):
        nonlocal cursor
        v, _, _ = proof['gates'][cursor]
        cursor += 1
        lists[v], bridge[v] = set(terms), d
        lists[-v], bridge[-v] = set(terms) ^ {one}, d
        kinds[v] = kind
        return v

    assign('z0', set())
    for i in range(1, n + 1):
        for j in range(i + 1):
            assign('u', {atom(i - 1, j, i, 0)})
            assign('v', {atom(i - 1, j - 1, i, 1)})
            assign('w', {one} ^ {q(i, j)})
    selectors, selector_bridges = [], []
    for j in range(1, n + 1):
        s = atom(n, j, j, 1)
        _, d = atom_pair(q(n, j), atom(0, 0, j, 1))
        selectors.append(s)
        selector_bridges.append(d)
        assign('t', {s}, d)
    for j in range(2, n + 1):
        assign('d', {one} ^ set(selectors[:j]), dag.add(*selector_bridges[:j]))
    assign('h', set(selectors), dag.add(*selector_bridges))
    assert cursor == proof['circuit_gate_count']
    for v, _, _ in proof['gates'][cursor:]:
        m = prefixes[v]
        assign('accumulator', {q(m, m)})
    assert cursor == len(proof['gates'])
    assert max(map(len, lists.values())) <= n + 1

    normalized = {v: dag.add(*(rep(a, diagrams[a]['root']) for a in sorted(atoms)))
                  for v, atoms in lists.items()}
    relations = []
    for v, a, b in proof['gates']:
        pairs = [atom_pair(aa, bb) for aa in sorted(lists[a]) for bb in sorted(lists[b])]
        p, w = dag.add(*(p for p, _ in pairs)), dag.add(*(w for _, w in pairs))
        right_bridge = dag.mul(actual[a], bridge[b])
        h = dag.add(bridge[v], dag.mul(bridge[a], normalized[b]), right_bridge, w)
        broken = dag.add(bridge[v], dag.mul(bridge[a], normalized[b]), w)
        delta = dag.add(actual[v], dag.mul(actual[a], actual[b]))
        relations.append(dict(node=v, operands=[a, b], kind=kinds[v], root=h,
                              product=p, delta=delta, mutation=broken))
    substituted, zeros = dag.words('axioms'), dag.words('zero')
    failures = []
    for v in lists:
        if substituted[bridge[v]] != substituted[actual[v]] ^ substituted[normalized[v]]:
            failures.append(['bridge', v])
        if zeros[bridge[v]]:
            failures.append(['bridge-zero', v])
    mutation_rejections = 0
    for r in relations:
        v, h, delta, p = r['node'], r['root'], r['delta'], r['product']
        for name, ok in [('identity', substituted[h] == substituted[delta]),
                         ('zero', not zeros[h]),
                         ('ordered-output', substituted[p] == substituted[normalized[v]]),
                         ('degree', dag.degrees[h] <= 3 * n)]:
            if not ok:
                failures.append([name, v])
        mutation_rejections += substituted[r['mutation']] != substituted[delta]
        r['substituted_words'] = enc(substituted[h])
        r['delta_words'] = enc(substituted[delta])
        r['zero_words'] = enc(zeros[h])
        r['output_words'] = enc(substituted[p])
        r['normalized_words'] = enc(substituted[normalized[v]])
    assert mutation_rejections > 0
    assert not failures, failures
    roots = list(actual.values()) + [dag.zero, dag.one] + [r['root'] for r in relations]
    ell = (len(dag.nodes) + len(lists) + n*n + 2).bit_length()
    root_bits = 0
    for root in roots:
        pending, seen = [root], set()
        while pending:
            idx = pending.pop()
            if idx in seen:
                continue
            seen.add(idx)
            if dag.nodes[idx][0] in ('add', 'mul'):
                pending.extend(dag.nodes[idx][1:])
        root_bits += 16 * (len(seen) + 1) * ell
    framing = 16 * len(actual) * ell + 128 * (n + 2)**2 * ell
    full_bits = root_bits + framing
    required_bits = 16 * len(roots) * (len(dag.nodes) + 1) * ell + framing
    assert full_bits <= required_bits
    result = dict(n=n, theorem_family_member=n >= 10 and n % 10 == 0,
                  checked_relations=len(relations), checked_signed_bridges=len(lists),
                  max_h=max(dag.degrees[r['root']] for r in relations), required_h=3*n,
                  max_d=max(dag.degrees[root] for root in actual.values()), required_d=n+1,
                  actual_padded_encoding_bits=full_bits, common_dag_copy_ceiling_bits=required_bits,
                  failures=failures, mutation_rejections=mutation_rejections,
                  dag_nodes=dag.nodes, diagrams=diagrams, actual_roots=actual,
                  normalized_roots=normalized, bridges=bridge, atom_lists={v: sorted(s) for v,s in lists.items()},
                  relations=relations)
    return result


def main():
    results = [run(n) for n in (2, 3)]
    path = Path(__file__).with_name('relations-results.json')
    path.write_text(json.dumps(dict(scope='exact free-word finite diagnostics; not an all-n proof',
                                    cases=results), indent=2) + '\n')
    for r in results:
        print('n={n}: relations={checked_relations}, signed bridges={checked_signed_bridges}, '
              'h={max_h}/{required_h}, d={max_d}/{required_d}, '
              'encoding={actual_padded_encoding_bits}/{common_dag_copy_ceiling_bits}, '
              'mutation rejections={mutation_rejections}, failures={failures}'.format(**r))
    print('Full certificate:', path.relative_to(Path.cwd()))


if __name__ == '__main__':
    main()
