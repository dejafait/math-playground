"""Fixed-schema Hilbert synthesis and balanced-slot proof emitter (no search oracle)."""
import argparse
import hashlib
import gzip
import itertools
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent

def N(a): return ('n', a)
def I(a, b): return ('i', a, b)
def X(a, b): return I(I(a, b), N(I(b, a)))
def E(a, b): return N(X(a, b))
Q = 'q'
Z = N(I(Q, Q))

def text(f, image=False):
    if isinstance(f, str): return f
    if f[0] == 'n': return '(~' + text(f[1], image) + ')'
    a, b = text(f[1], image), text(f[2], image)
    return '((~' + a + ')|' + b + ')' if image else '(' + a + '>' + b + ')'

def sub(f, env):
    if isinstance(f, str): return env.get(f, f)
    return tuple([f[0]] + [sub(t, env) for t in f[1:]])

def variables(f):
    if isinstance(f, str): return {f}
    return set().union(*(variables(x) for x in f[1:]))

class Proof:
    def __init__(self):
        self.rows = []
        self.cache = {}
        self.discharge_cache = {}
        self.instance_cache = {}

    def add(self, f, rule, refs=(), env=None, deps=frozenset()):
        key = (f, deps)
        if key in self.cache: return self.cache[key]
        j = len(self.rows)
        self.rows.append((f, rule, refs, env, deps))
        self.cache[key] = j
        return j

    def assume(self, f): return self.add(f, 'assume', deps=frozenset([f]))

    def ax(self, tag, a, b, c=None):
        if tag == 'ax1': f = I(a, I(b, a))
        elif tag == 'ax2': f = I(I(a, I(b, c)), I(I(a, b), I(a, c)))
        elif tag == 'ax3': f = I(I(N(a), N(b)), I(b, a))
        else: raise ValueError(tag)
        env = {'A': a, 'B': b}
        if tag == 'ax2': env['C'] = c
        return self.add(f, tag, env=env)

    def mp(self, p, implication):
        f, g = self.rows[p][0], self.rows[implication][0]
        assert g[0] == 'i' and g[1] == f, (f, g)
        return self.add(g[2], 'mp', (p, implication),
                        deps=self.rows[p][4] | self.rows[implication][4])

    def identity(self, a):
        p = self.ax('ax1', a, I(a, a))
        q = self.ax('ax1', a, a)
        r = self.ax('ax2', a, I(a, a), a)
        return self.mp(q, self.mp(p, r))

    def discharge(self, h, root):
        key = (h, root)
        if key in self.discharge_cache: return self.discharge_cache[key]
        f, rule, refs, env, deps = self.rows[root]
        if h not in deps:
            out = self.mp(root, self.ax('ax1', f, h))
        elif rule == 'assume':
            assert f == h
            out = self.identity(h)
        else:
            assert rule == 'mp'
            p, implication = refs
            a = self.rows[p][0]
            hp = self.discharge(h, p)
            hi = self.discharge(h, implication)
            out = self.mp(hp, self.mp(hi, self.ax('ax2', h, a, f)))
        assert self.rows[out][0] == I(h, f)
        assert self.rows[out][4] == deps - {h}
        self.discharge_cache[key] = out
        return out

    def instance(self, root, env):
        key = (root, tuple(sorted(env.items())))
        if key in self.instance_cache: return self.instance_cache[key]
        f, rule, refs, oldenv, deps = self.rows[root]
        assert not deps
        if rule == 'mp':
            out = self.mp(*(self.instance(j, env) for j in refs))
        else:
            assert rule in ('ax1', 'ax2', 'ax3')
            e = {k: sub(v, env) for k, v in oldenv.items()}
            out = self.ax(rule, e['A'], e['B'], e.get('C'))
        assert self.rows[out][0] == sub(f, env)
        self.instance_cache[key] = out
        return out

    def explosion(self, positive, negative, goal):
        a = self.rows[positive][0]
        assert self.rows[negative][0] == N(a)
        p = self.mp(negative, self.ax('ax1', N(a), N(goal)))
        return self.mp(positive, self.mp(p, self.ax('ax3', goal, a)))

    def clavius(self, a):
        h = I(N(a), a)
        ph, pn = self.assume(h), self.assume(N(a))
        pa = self.mp(pn, ph)
        nh = self.explosion(pa, pn, N(h))
        conditional = self.discharge(N(a), nh)
        ha = self.mp(conditional, self.ax('ax3', a, h))
        return self.discharge(h, self.mp(ph, ha))

    def raa(self, goal, positive, negative):
        # The supplied contradiction may depend on the assumption NOT goal.
        out = self.explosion(positive, negative, goal)
        conditional = self.discharge(N(goal), out)
        return self.mp(conditional, self.clavius(goal))

    def build_helpers(self):
        a, b = 'A', 'B'
        nn = self.assume(N(N(a)))
        na = self.assume(N(a))
        pa = self.explosion(na, nn, a)
        conditional = self.discharge(N(a), pa)
        self.dne = self.discharge(N(N(a)), self.mp(conditional, self.clavius(a)))
        triple_to_single = self.instance(self.dne, {'A': N(a)})
        self.dni = self.mp(triple_to_single, self.ax('ax3', N(N(a)), a))

        # A -> (NOT B -> NOT (A -> B)).
        pa, nb = self.assume(a), self.assume(N(b))
        h = I(a, b)
        nnh = self.assume(N(N(h)))
        ph = self.mp(nnh, self.instance(self.dne, {'A': h}))
        pb = self.mp(pa, ph)
        result = self.raa(N(h), pb, nb)
        self.imp_false = self.discharge(a, self.discharge(N(b), result))

        # (A -> B) -> ((NOT A -> B) -> B).
        f, g = I(a, b), I(N(a), b)
        pf, pg, nb = self.assume(f), self.assume(g), self.assume(N(b))
        nna = self.assume(N(N(a)))
        pa = self.mp(nna, self.instance(self.dne, {'A': a}))
        pb = self.mp(pa, pf)
        pna = self.raa(N(a), pb, nb)
        pb = self.mp(pna, pg)
        pb = self.raa(b, pb, nb)
        self.cases = self.discharge(f, self.discharge(g, pb))

    def prove_fixed(self, goal):
        vs = sorted(variables(goal))
        # Truth evaluation is an emitter tactic, never a checker rule.
        def leaf(env):
            memo = {}
            def signed(f):
                if f in memo: return memo[f]
                if isinstance(f, str):
                    val = env[f]
                    p = self.assume(f if val else N(f))
                elif f[0] == 'n':
                    val0, p0 = signed(f[1])
                    val = not val0
                    p = self.mp(p0, self.instance(self.dni, {'A': f[1]})) if val0 else p0
                else:
                    va, pa = signed(f[1])
                    vb, pb = signed(f[2])
                    val = not va or vb
                    if vb:
                        p = self.mp(pb, self.ax('ax1', f[2], f[1]))
                    elif not va:
                        # NOT A -> (A -> B) via ax-3.
                        h = self.mp(pa, self.ax('ax1', N(f[1]), N(f[2])))
                        p = self.mp(h, self.ax('ax3', f[2], f[1]))
                    else:
                        h = self.instance(self.imp_false, {'A': f[1], 'B': f[2]})
                        p = self.mp(pb, self.mp(pa, h))
                assert self.rows[p][0] == (f if val else N(f))
                memo[f] = (val, p)
                return val, p
            val, root = signed(goal)
            if not val: raise ValueError('fixed schema is not tautological: ' + repr(env))
            return root
        def go(k, env):
            if k == len(vs): return leaf(env)
            a = vs[k]
            pos = go(k+1, dict(env, **{a: True}))
            neg = go(k+1, dict(env, **{a: False}))
            p = self.discharge(a, pos)
            n = self.discharge(N(a), neg)
            c = self.instance(self.cases, {'A': a, 'B': goal})
            return self.mp(n, self.mp(p, c))
        root = go(0, {})
        assert not self.rows[root][4]
        return root

    def reachable(self, root):
        seen = set()
        def visit(j):
            if j in seen: return
            seen.add(j)
            for k in self.rows[j][2]: visit(k)
        visit(root)
        return sorted(seen)

    def write(self, root, path, image=False):
        order = self.reachable(root)
        assert order[-1] == root
        renum = {j: k for k, j in enumerate(order)}
        digest = hashlib.sha256()
        size = 0
        with (gzip.open(path, 'wb') if str(path).endswith('.gz') else path.open('wb')) as f:
            def write_line(s):
                nonlocal size
                data = (s+'\n').encode('utf8')
                size += len(data); digest.update(data); f.write(data)
            write_line(json.dumps({'format': 'not-or' if image else 'native',
                                'goal': text(self.rows[root][0], image)}, separators=(',', ':')))
            for j in order:
                formula, rule, refs, env, deps = self.rows[j]
                assert not deps and rule != 'assume'
                row = {'f': text(formula, image), 'rule': rule}
                if refs: row['refs'] = [renum[k] for k in refs]
                if env: row['subs'] = {k: text(v, image) for k, v in env.items()}
                write_line(json.dumps(row, separators=(',', ':')))
        return {'lines': len(order), 'bytes': size, 'storage_bytes': path.stat().st_size,
                'sha256': digest.hexdigest()}

def schemas():
    a, b, c = 'A', 'B', 'C'
    return {
        'assoc': E(X(X(a, b), c), X(a, X(b, c))),
        'comm': E(X(a, b), X(b, a)),
        'cancel': E(X(a, a), Z),
        'zero_slots': E(Z, X(Z, Z)),
        'trans': I(E(a, b), I(E(b, c), E(a, c))),
        'symm': I(E(a, b), E(b, a)),
        'congL': I(E(a, b), E(X(a, c), X(b, c))),
        'congR': I(E(a, b), E(X(c, a), X(c, b))),
        'refl': E(a, a),
        # Native OR is NOT A -> B. This explicitly pays the double-negation bridge.
        'imp_bridge': E(I(a, b), I(N(N(a)), b)),
        'double_neg_bridge': E(a, N(N(a))),
    }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--library', action='store_true')
    args = parser.parse_args()
    p = Proof()
    p.build_helpers()
    results = {}
    for name, goal in schemas().items():
        root = p.prove_fixed(goal)
        entry = {}
        for image, suffix in [(False, 'native'), (True, 'not-or')]:
            path = HERE / 'output' / (name + '.' + suffix + '.jsonl.gz')
            entry[suffix] = p.write(root, path, image)
        results[name] = entry
        print(name, 'primitive_lines', entry['native']['lines'], 'native_bytes', entry['native']['bytes'], flush=True)
    (HERE/'output'/'library-emission.json').write_text(json.dumps(results, indent=2)+'\n')

if __name__ == '__main__': main()
