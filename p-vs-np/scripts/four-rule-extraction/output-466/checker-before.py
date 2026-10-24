"""Independent literal four-rule checker; deliberately imports no emitter.

Trees are JSON prefix arrays ["not", A], ["or", A, B] or name strings.
Only the strings true and false are constants. All indices are zero-based.
"""
import hashlib
import itertools
import json
from pathlib import Path


class Invalid(ValueError):
    pass


def tree(x):
    if isinstance(x, str) and x and all(c.isalnum() or c == '_' for c in x):
        return x
    if isinstance(x, list) and x:
        if x[0] == 'not' and len(x) == 2:
            return ('not', tree(x[1]))
        if x[0] == 'or' and len(x) == 3:
            return ('or', tree(x[1]), tree(x[2]))
    raise Invalid('formula syntax')


def variables(t):
    if isinstance(t, str):
        return set() if t in ('true', 'false') else {t}
    return set().union(*(variables(c) for c in t[1:]))


def nodes(t):
    return 1 if isinstance(t, str) else 1 + sum(nodes(c) for c in t[1:])


def check(path, expected):
    expected = tree(json.loads(json.dumps(expected)))
    fs, counts = [], {}
    digest, size, total_nodes = hashlib.sha256(), 0, 0
    with Path(path).open('rb') as stream:
        raw = stream.readline()
        digest.update(raw)
        size += len(raw)
        try:
            h = json.loads(raw)
            if set(h) != {'format', 'alphabet', 'goal'} or h['format'] != 'literal-four-rule-v1':
                raise Invalid('header fields')
            alphabet = h['alphabet']
            if not isinstance(alphabet, list) or any(not isinstance(v, str) for v in alphabet):
                raise Invalid('alphabet type')
            if len(set(alphabet)) != len(alphabet) or any(tree(v) in ('true', 'false') for v in alphabet):
                raise Invalid('alphabet names')
            if tree(h['goal']) != expected:
                raise Invalid('header endpoint')
            for i, raw in enumerate(stream):
                digest.update(raw)
                size += len(raw)
                r = json.loads(raw)
                if set(r) != {'rule', 'f', 'refs'}:
                    raise Invalid('record fields')
                f, tag, refs = tree(r['f']), r['rule'], r['refs']
                if not variables(f) <= set(alphabet):
                    raise Invalid('foreign name')
                if not isinstance(refs, list) or any(type(j) is not int or not 0 <= j < i for j in refs):
                    raise Invalid('non-backward reference')
                needed = {'axiom': 0, 'true': 0, 'not-false': 0, 'expansion': 1,
                          'contraction': 1, 'association': 1, 'cut': 2}
                if tag not in needed or len(refs) != needed[tag]:
                    raise Invalid('primitive tag/arity')
                p = [fs[j] for j in refs]
                if tag == 'axiom':
                    ok = isinstance(f, tuple) and f[0] == 'or' and f[1] == ('not', f[2])
                elif tag == 'true':
                    ok = f == 'true'
                elif tag == 'not-false':
                    ok = f == ('not', 'false')
                elif tag == 'expansion':
                    ok = isinstance(f, tuple) and f[0] == 'or' and f[2] == p[0]
                elif tag == 'contraction':
                    ok = p[0] == ('or', f, f)
                elif tag == 'association':
                    q = p[0]
                    ok = (isinstance(q, tuple) and q[0] == 'or'
                          and isinstance(q[2], tuple) and q[2][0] == 'or'
                          and f == ('or', ('or', q[1], q[2][1]), q[2][2]))
                else:
                    a, b = p
                    ok = (isinstance(a, tuple) and a[0] == 'or'
                          and isinstance(b, tuple) and b[0] == 'or'
                          and b[1] == ('not', a[1]) and f == ('or', a[2], b[2]))
                if not ok:
                    raise Invalid('literal ' + tag + ' mismatch at ' + str(i))
                fs.append(f)
                total_nodes += nodes(f)
                counts[tag] = counts.get(tag, 0) + 1
        except (KeyError, TypeError, json.JSONDecodeError, RecursionError) as err:
            raise Invalid('malformed serialized stream') from err
    if not fs or fs[-1] != expected:
        raise Invalid('last endpoint')
    return dict(accepted=True, records=len(fs), rule_counts=counts,
                formula_nodes=total_nodes, bytes=size, sha256=digest.hexdigest())


def fixture_endpoint(data):
    """Reconstruct the entire canonical source independently of the emitter."""
    rows, lam = data['rows'], data['lambda']
    if not isinstance(rows, list) or not isinstance(lam, list) or len(rows) != len(lam):
        raise Invalid('row/lambda lengths')
    clauses, literal_lists, parity, rhs_parity = [], [], {}, 0
    for row, selected in zip(rows, lam):
        vs, rhs = row['names'], row['rhs']
        if (not isinstance(vs, list) or len(vs) > 3 or len(set(vs)) != len(vs)
                or type(rhs) is not int or rhs not in (0, 1)
                or type(selected) is not int or selected not in (0, 1)):
            raise Invalid('row syntax')
        for v in vs:
            if not isinstance(v, str) or tree(v) in ('true', 'false'):
                raise Invalid('row name')
            parity[v] = parity.get(v, 0) ^ selected
        rhs_parity ^= rhs & selected
        for bits in itertools.product((0, 1), repeat=len(vs)):
            if sum(bits) % 2 != rhs:
                lits = [v if not bit else ('not', v) for v, bit in zip(vs, bits)]
                literal_lists.append([v if not bit else '(~' + v + ')' for v, bit in zip(vs, bits)])
                c = 'false'
                if lits:
                    c = lits[-1]
                    for v in reversed(lits[:-1]):
                        c = ('or', v, c)
                clauses.append(c)
    if any(parity.values()) or rhs_parity != 1:
        raise Invalid('not a supplied parity contradiction')
    if data['clauses'] != literal_lists or data['clause_tree_policy'] != 'right-associated actual trees; empty=false':
        raise Invalid('canonical clause comparison')
    order = []

    def assemble(s):
        if type(s) is int and 0 <= s < len(clauses):
            order.append(s)
            return clauses[s]
        if isinstance(s, list) and len(s) == 2:
            a, b = assemble(s[0]), assemble(s[1])
            return ('not', ('or', ('not', a), ('not', b)))
        raise Invalid('global actual tree')

    f = assemble(data['global_tree']) if clauses else 'true'
    if order != list(range(len(clauses))):
        raise Invalid('clause occurrence/order mismatch')
    return ('not', f)
