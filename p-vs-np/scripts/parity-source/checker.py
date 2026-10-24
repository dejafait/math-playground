"""Independent exact Schoenfield source-stream checker. No emitter import."""
import hashlib
import itertools
import json
from pathlib import Path


class Invalid(ValueError):
    pass


def parse(s):
    p = 0

    def term():
        nonlocal p
        if p >= len(s):
            raise Invalid('unexpected end')
        if s[p] != '(':
            start = p
            while p < len(s) and (s[p].isalnum() or s[p] == '_'):
                p += 1
            if start == p:
                raise Invalid('bad name')
            return s[start:p]
        p += 1
        if s[p] == '~':
            p += 1
            t = ('n', term())
        else:
            a = term()
            if s[p] != '|':
                raise Invalid('only literal OR is a binary connective')
            p += 1
            t = ('o', a, term())
        if s[p] != ')':
            raise Invalid('missing close')
        p += 1
        return t

    try:
        t = term()
    except IndexError as err:
        raise Invalid('truncated syntax') from err
    if p != len(s):
        raise Invalid('trailing syntax')
    return t


def spell(t):
    if isinstance(t, str):
        return t
    if t[0] == 'n':
        return '(~' + spell(t[1]) + ')'
    return '(' + spell(t[1]) + '|' + spell(t[2]) + ')'


def implies(a, b):
    return ('o', ('n', a), b)


def pattern(rule):
    a, b, c = '$A', '$B', '$C'
    na, nb = ('n', a), ('n', b)
    if rule == 'ax1':
        return implies(a, implies(b, a))
    if rule == 'axS':
        return implies(implies(na, nb), implies(implies(na, b), a))
    if rule == 'ax2':
        return implies(implies(a, implies(b, c)), implies(implies(a, b), implies(a, c)))
    raise Invalid('unapproved rule ' + str(rule))


def match(p, t, env):
    if isinstance(p, str):
        if p in env and env[p] != t:
            raise Invalid('inconsistent substitution')
        env[p] = t
        return
    if not isinstance(t, tuple) or len(p) != len(t) or p[0] != t[0]:
        raise Invalid('axiom shape mismatch')
    for a, b in zip(p[1:], t[1:]):
        match(a, b, env)


def nodes(t):
    return 1 if isinstance(t, str) else 1 + sum(nodes(x) for x in t[1:])


def names(t):
    if isinstance(t, str):
        return [] if t in ('true', 'false') else [t]
    return [v for x in t[1:] for v in names(x)]


def check(path, expected):
    fs = []
    stats = dict(records=0, formula_nodes=0, substitution_nodes=0,
                 name_occurrences=0, name_bytes=0, reference_occurrences=0,
                 reference_decimal_bytes=0, max_formula_nodes=0)
    digest = hashlib.sha256()
    byte_count = 0
    with Path(path).open('rb') as stream:
        raw = stream.readline()
        digest.update(raw)
        byte_count += len(raw)
        header = json.loads(raw)
        if set(header) != {'format', 'goal'} or header['format'] != 'exact-not-or':
            raise Invalid('header')
        if header['goal'] != expected:
            raise Invalid('requested endpoint mismatch')
        parse(expected)
        for j, raw in enumerate(stream):
            digest.update(raw)
            byte_count += len(raw)
            try:
                r = json.loads(raw)
                t = parse(r['f'])
                rule = r['rule']
                if rule == 'mp':
                    if set(r) != {'f', 'rule', 'refs'}:
                        raise Invalid('MP fields')
                    refs = r['refs']
                    if len(refs) != 2 or any(type(k) is not int or not 0 <= k < j for k in refs):
                        raise Invalid('reference not strictly earlier')
                    a, conditional = [fs[k] for k in refs]
                    if conditional != implies(a, t):
                        raise Invalid('MP mismatch')
                    stats['reference_occurrences'] += 2
                    stats['reference_decimal_bytes'] += sum(len(str(k)) for k in refs)
                elif rule in ('true', 'not-false'):
                    if set(r) != {'f', 'rule'}:
                        raise Invalid('ground fields')
                    if t != ('true' if rule == 'true' else ('n', 'false')):
                        raise Invalid('ground constant misuse')
                else:
                    if set(r) != {'f', 'rule', 'subs'}:
                        raise Invalid('axiom fields')
                    env = {}
                    match(pattern(rule), t, env)
                    if set(r['subs']) != {k[1:] for k in env}:
                        raise Invalid('substitution keys')
                    for k, s in r['subs'].items():
                        st = parse(s)
                        if st != env['$' + k]:
                            raise Invalid('declared substitution mismatch')
                        stats['substitution_nodes'] += nodes(st)
                        ns = names(st)
                        stats['name_occurrences'] += len(ns)
                        stats['name_bytes'] += sum(len(v.encode()) for v in ns)
                stats['formula_nodes'] += nodes(t)
                stats['max_formula_nodes'] = max(stats['max_formula_nodes'], nodes(t))
                ns = names(t)
                stats['name_occurrences'] += len(ns)
                stats['name_bytes'] += sum(len(v.encode()) for v in ns)
                fs.append(t)
            except (ValueError, TypeError, KeyError) as err:
                raise Invalid('record %d: %s' % (j, err)) from err
    if not fs or spell(fs[-1]) != expected:
        raise Invalid('last line mismatch')
    stats.update(accepted=True, records=len(fs), bytes=byte_count,
                 bits=8*byte_count, sha256=digest.hexdigest())
    return stats


def fixture_endpoint(data):
    """Rebuild canonical forbidden clauses and actual F independently."""
    clauses = []
    parity = {}
    rhs = 0
    if len(data['rows']) != len(data['lambda']):
        raise Invalid('lambda length')
    for row, selected in zip(data['rows'], data['lambda']):
        vs, b = row['names'], row['rhs']
        if len(vs) > 3 or len(set(vs)) != len(vs) or b not in (0, 1) or selected not in (0, 1):
            raise Invalid('row data')
        if any(v in ('true', 'false') or parse(v) != v for v in vs):
            raise Invalid('reserved or malformed name')
        rhs ^= selected & b
        for v in vs:
            parity[v] = parity.get(v, 0) ^ selected
        for bits in itertools.product((0, 1), repeat=len(vs)):
            if sum(bits) % 2 != b:
                clauses.append([v if bit == 0 else ('n', v) for v, bit in zip(vs, bits)])
    if rhs != 1 or any(parity.values()):
        raise Invalid('row combination not contradictory')
    expected_literals = [[spell(t) for t in c] for c in clauses]
    if data['clauses'] != expected_literals:
        raise Invalid('canonical clause mismatch')
    def clause(c):
        if not c:
            return 'false'
        if len(c) == 1:
            return c[0]
        # These fixtures use explicitly recorded right-associated clause trees.
        return ('o', c[0], clause(c[1:]))
    actual = [clause(c) for c in clauses]
    seen = []
    def global_tree(t):
        if type(t) is int:
            if not 0 <= t < len(actual):
                raise Invalid('clause position')
            seen.append(t)
            return actual[t]
        if not isinstance(t, list) or len(t) != 2:
            raise Invalid('global tree')
        a, b = map(global_tree, t)
        return ('n', ('o', ('n', a), ('n', b)))
    f = global_tree(data['global_tree'])
    if seen != list(range(len(actual))):
        raise Invalid('missing, reordered or repeated clause positions')
    return spell(('n', f))
