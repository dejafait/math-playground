"""Bounded primitive-only library preparation for L106 section 6.

No old parity compiler, Hilbert synthesizer or checker is imported.
All incomplete search records are retained, with their actual last goal.
Run: python3 scripts/parity-four-rule/run.py
"""
from collections import defaultdict, deque
from functools import lru_cache
import itertools
import json
import time


def N(a):
    return ('not', a)


def O(a, b):
    return ('or', a, b)


def I(a, b):
    return O(N(a), b)


def And(a, b):
    return N(O(N(a), N(b)))


def E(a, b):
    return And(I(a, b), I(b, a))


def X(a, b):
    return And(O(a, b), N(And(a, b)))


def EG(a, b):
    return I('G', E(a, b))


@lru_cache(maxsize=200000)
def nodes(t):
    return 1 if isinstance(t, str) else 1 + sum(nodes(x) for x in t[1:])


def names(t):
    if isinstance(t, str):
        return set() if t in ('true', 'false') else {t}
    return set().union(*(names(x) for x in t[1:]))


def evaluate(t, env):
    if isinstance(t, str):
        return {'true': True, 'false': False}.get(t, env.get(t))
    if t[0] == 'not':
        return not evaluate(t[1], env)
    return evaluate(t[1], env) or evaluate(t[2], env)


def shapes(items):
    if not items:
        return ['false']
    if len(items) == 1:
        return items
    return [O(a, b) for k in range(1, len(items))
            for a in shapes(items[:k]) for b in shapes(items[k:])]


def conjunction(items):
    if not items:
        return 'true'
    out = items[-1]
    for a in reversed(items[:-1]):
        out = And(a, out)
    return out


def manifest():
    a, b, c, d, g, h, p, x = 'A', 'B', 'C', 'D', 'G', 'H', 'P', 'X'
    entries = []

    def add(label, f, origin):
        vs = sorted(names(f))
        vals = [dict(zip(vs, bits)) for bits in itertools.product((False, True), repeat=len(vs))]
        counter = next((v for v in vals if not evaluate(f, v)), None)
        if counter is not None:
            raise ValueError((label, counter))
        entries.append(dict(id=label, origin=origin, target=f, slots=vs,
                            nodes=nodes(f), assignments_checked=len(vals), boolean_valid=True))

    base = [
        ('identity', I(a, a)),
        ('projection-left', I(And(a, b), a)), ('projection-right', I(And(a, b), b)),
        ('guard-compose', I(I(g, a), I(I(a, b), I(g, b)))),
        ('same-positive', I(I(x, a), I(I(x, b), I(x, E(a, b))))),
        ('same-negative', I(I(x, N(a)), I(I(x, N(b)), I(x, E(a, b))))),
        ('cases', I(I(g, O(a, b)), I(I(a, h), I(I(b, h), I(g, h))))),
        ('guard-reflexive', EG(a, a)), ('guard-symmetric', I(EG(a, b), EG(b, a))),
        ('guard-negation', I(EG(a, b), EG(N(a), N(b)))),
        ('guard-or', I(EG(a, b), I(EG(c, d), EG(O(a, c), O(b, d))))),
        ('guard-transport', I(I(g, a), I(EG(a, b), I(g, b)))),
        ('guard-resolution', I(I(g, O(p, a)), I(I(g, O(N(p), b)), I(g, O(a, b))))),
        ('guard-weakening', I(I(g, a), I(g, O(a, b)))),
        ('list-commute', EG(O(a, b), O(b, a))),
        ('list-associate', EG(O(a, O(b, c)), O(O(a, b), c))),
        ('list-contract', EG(O(a, a), a)), ('list-zero-right', EG(O(a, 'false'), a)),
        ('list-zero-left', EG(O('false', a), a)), ('final-discharge', I(I(g, 'false'), N(g))),
    ]
    for label, f in base:
        add(label, f, 'L097 section 6.1')
    extra = [
        ('guard-introduction', I(a, I(g, a))),
        ('guard-conjunction', I(I(g, a), I(I(g, b), I(g, And(a, b))))),
        ('guard-true', I(g, 'true')),
        ('xor-commute', E(X(a, b), X(b, a))),
        ('xor-associate', E(X(X(a, b), c), X(a, X(b, c)))),
        ('xor-zero-right', E(X(a, 'false'), a)),
        ('xor-zero-left', E(X('false', a), a)),
        ('xor-cancel', E(X(a, a), 'false')),
        ('guard-transitive', I(EG(a, b), I(EG(b, c), EG(a, c)))),
        ('guard-xor-right', I(EG(a, b), EG(X(a, c), X(b, c)))),
        ('guard-xor-left', I(EG(a, b), EG(X(c, a), X(c, b)))),
        ('guard-zero-sum', I(EG(a, 'false'), I(EG(b, 'false'), EG(X(a, b), 'false')))),
        ('inconsistent-discharge', I(I(g, E('false', 'true')), N(g))),
        ('refutation-transport', I(N(a), I(I(g, a), N(g)))),
    ]
    for label, f in extra:
        add(label, f, 'L106 section 6.2')
    for arity in range(4):
        vs = ['x' + str(i + 1) for i in range(arity)]
        for rhs in (0, 1):
            choices = []
            for bits in itertools.product((0, 1), repeat=arity):
                if sum(bits) % 2 != rhs:
                    choices.append(shapes([v if not bit else N(v) for v, bit in zip(vs, bits)]))
            for k, clauses in enumerate(itertools.product(*choices)):
                leaves = vs + ['false'] * (3 - arity)
                r = X(X(leaves[0], leaves[1]), X(leaves[2], 'true' if rhs else 'false'))
                add('row-' + str(arity) + '-' + str(rhs) + '-shape-' + str(k),
                    I(conjunction(clauses), E(r, 'false')), 'L106 section 6.2 row family')
    return entries


LIMITS = dict(template_records=50000, template_cut_pairs=1000000, template_seconds=15,
              library_records=250000, library_cut_pairs=5000000, library_seconds=90,
              formula_nodes='max(16, target nodes + 8)')


class Exhausted(Exception):
    pass


def saturate(target, remaining):
    start = time.monotonic()
    cap = max(16, nodes(target) + 8)
    rows, indices, queue = [], {}, deque()
    left, negleft = defaultdict(list), defaultdict(list)
    stats = dict(cut_pairs=0, candidates=0, rejected_size=0, duplicate_candidates=0,
                 processed_records=0, max_nodes=0)
    pool = {'true', 'false'}

    def collect(t):
        pool.add(t)
        if isinstance(t, tuple):
            for child in t[1:]:
                collect(child)

    collect(target)
    pool |= {N(t) for t in list(pool)}
    pool = sorted(pool, key=lambda t: (nodes(t), repr(t)))
    max_records = min(LIMITS['template_records'], remaining['records'])
    max_pairs = min(LIMITS['template_cut_pairs'], remaining['pairs'])
    max_seconds = min(LIMITS['template_seconds'], remaining['seconds'])
    reason = None

    def budget():
        if time.monotonic() - start >= max_seconds:
            raise Exhausted('seconds')

    def add(f, rule, refs=()):
        stats['candidates'] += 1
        if nodes(f) > cap:
            stats['rejected_size'] += 1
            return
        if f in indices:
            stats['duplicate_candidates'] += 1
            return
        budget()
        if len(rows) >= max_records - 2:
            raise Exhausted('stored-records')
        i = len(rows)
        rows.append(dict(f=f, rule=rule, refs=list(refs)))
        indices[f] = i
        queue.append(i)
        stats['max_nodes'] = max(stats['max_nodes'], nodes(f))
        if isinstance(f, tuple) and f[0] == 'or':
            left[f[1]].append(i)
            if isinstance(f[1], tuple) and f[1][0] == 'not':
                negleft[f[1][1]].append(i)

    def cut(i, j):
        budget()
        if stats['cut_pairs'] >= max_pairs:
            raise Exhausted('cut-pairs')
        stats['cut_pairs'] += 1
        add(O(rows[i]['f'][2], rows[j]['f'][2]), 'cut', (i, j))

    try:
        add('true', 'true')
        add(N('false'), 'not-false')
        for t in pool:
            add(O(N(t), t), 'axiom')
        while queue and target not in indices:
            i = queue.popleft()
            f = rows[i]['f']
            stats['processed_records'] += 1
            if isinstance(f, tuple) and f[0] == 'or':
                if f[1] == f[2]:
                    add(f[1], 'contraction', (i,))
                if isinstance(f[2], tuple) and f[2][0] == 'or':
                    add(O(O(f[1], f[2][1]), f[2][2]), 'association', (i,))
                for j in list(negleft.get(f[1], ())):
                    cut(i, j)
                if isinstance(f[1], tuple) and f[1][0] == 'not':
                    for j in list(left.get(f[1][1], ())):
                        cut(j, i)
            for t in pool:
                add(O(t, f), 'expansion', (i,))
            budget()
        if target not in indices:
            reason = 'finite-fragment-closure'
    except Exhausted as err:
        reason = str(err)
    success = target in indices
    # Retain all generated records, even if a target was found earlier.
    # Restore the exact target last with two legal records, never an alias.
    if success:
        i = indices[target]
        rows.append(dict(f=O(target, target), rule='expansion', refs=[i]))
        rows.append(dict(f=target, rule='contraction', refs=[len(rows) - 1]))
    return rows, dict(status='PREPARED' if success else 'UNPREPARED', reason=reason,
                      records=len(rows), search_records=len(indices), seconds=time.monotonic() - start,
                      formula_node_cap=cap, pool=pool, stats=stats,
                      effective_limits=dict(records=max_records, cut_pairs=max_pairs, seconds=max_seconds))


def write_stream(path, rows, alphabet, goal):
    header = dict(format='literal-four-rule-v1', alphabet=alphabet, goal=goal)
    with path.open('w') as out:
        for row in [header] + rows:
            out.write(json.dumps(row, separators=(',', ':')) + '\n')
