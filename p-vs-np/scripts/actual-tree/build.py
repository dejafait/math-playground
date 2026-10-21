"""Native actual-occurrence suffixes and exact L065 local packages.

No closure, PIT, coordinate or whole-receiver invocation. Tree leaves use
explicit letter POSITIONS; equal payloads never duplicate an edge.
"""
import importlib.util
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'backward-zero'))

def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    obj = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(obj)
    return obj

b = module('actual_zero_build', HERE.parent / 'backward-zero' / 'build.py')
p, c = b.p, b.checker
ep = module('actual_closure_endpoints', HERE.parent / 'left-closure' / 'endpoints.py')

def fixed():
    a, bb, cc = 'A', 'B', 'C'
    y, z = p.I('q', 'q'), p.N(p.I('q', 'q'))
    return dict(prod_assoc=p.E(b.P(b.P(a, bb), cc), b.P(a, b.P(bb, cc))),
                right_dist=p.E(b.P(p.X(a, bb), cc), p.X(b.P(a, cc), b.P(bb, cc))),
                unitL=p.E(b.P(y, a), a), unitR=p.E(b.P(a, y), a),
                zero_prodL=p.E(b.P(z, a), z))

def validate_input(d, depth_factor=4):
    if set(d) != {'tree', 'letters', 'q', 'delete_zero'}:
        raise c.Invalid('actual-tree input fields')
    if type(d['delete_zero']) is not bool:
        raise c.Invalid('zero-edge convention')
    if not isinstance(d['letters'], list) or any(
        not isinstance(x, str) or not re.fullmatch(r'[A-Za-z0-9_]+', x)
        for x in d['letters'] + [d['q']]):
        raise c.Invalid('ASCII letter/q payload')
    def go(t):
        if not isinstance(t, list) or not t: raise c.Invalid('tree syntax')
        if t[0] in ('add', 'mul') and len(t) == 3:
            ul, dl = go(t[1]); ur, dr = go(t[2])
            return 1 + ul + ur, 1 + max(dl, dr)
        elif t[0] == 'var' and len(t) == 2:
            if type(t[1]) is not int or not 0 <= t[1] < len(d['letters']):
                raise c.Invalid('edge-to-letter position')
        elif t[0] in ('zero', 'one') and len(t) == 1: pass
        else: raise c.Invalid('tree operator/arity')
        return 1, 0
    U, depth = go(d['tree'])
    if type(depth_factor) is not int or depth_factor < 1:
        raise c.Invalid('fixed positive depth factor')
    if depth > depth_factor * (U + 1).bit_length():
        raise c.Invalid('source logarithmic-depth promise')
    return U, depth

def construct(d, depth_factor=4):
    validate_input(d, depth_factor)
    q = d['q']; y = b.atom((0,), p.I(q, q)); z = b.atom((9,), p.N(p.I(q, q)))
    occurrences = []; vertices = []; edges = []
    def walk(t, parent=None, side=None):
        oid = len(occurrences)
        node = dict(id=oid, tree=t, parent=parent, side=side, entry=len(vertices))
        occurrences.append(node); vertices.append((oid, 'entry'))
        if t[0] in ('add', 'mul'):
            left = walk(t[1], oid, 'left'); right = walk(t[2], oid, 'right')
            node['children'] = [left, right]
            node['value'] = (b.X if t[0] == 'add' else b.product)(
                occurrences[left]['value'], occurrences[right]['value'])
        else:
            node['value'] = y if t[0] == 'one' else z if t[0] == 'zero' else b.atom(
                (3, t[1]), d['letters'][t[1]])
        node['exit'] = len(vertices); vertices.append((oid, 'exit'))
        if t[0] in ('add', 'mul'):
            l, r = [occurrences[i] for i in node['children']]
            pairs = [(node['entry'], l['entry']), (l['exit'], node['exit']),
                     (node['entry'], r['entry']), (r['exit'], node['exit'])] if t[0] == 'add' else [
                     (node['entry'], l['entry']), (l['exit'], r['entry']), (r['exit'], node['exit'])]
            edges.extend(dict(v=v, w=w, kind='one') for v, w in pairs)
        elif t[0] != 'zero' or not d['delete_zero']:
            edge = dict(v=node['entry'], w=node['exit'], kind=t[0])
            if t[0] == 'var': edge['position'] = t[1]
            edges.append(edge)
        return oid
    walk(d['tree'])
    suffix = [None] * len(vertices)
    def continuation(i, tail):
        node = occurrences[i]; node['tail'] = tail
        suffix[node['entry']] = b.product(node['value'], tail)
        suffix[node['exit']] = tail
        if 'children' in node:
            l, r = node['children']
            continuation(l, tail if node['tree'][0] == 'add' else b.product(occurrences[r]['value'], tail))
            continuation(r, tail)
    continuation(0, y)
    N, n = len(vertices), len(d['letters'])
    E0 = [[0] * N for _ in range(N)]; Eb = [[[0] * N for _ in range(N)] for _ in range(n)]
    for edge in edges:
        v, w = edge['v'], edge['w']
        assert v < w
        if edge['kind'] == 'one': E0[v][w] ^= 1
        elif edge['kind'] == 'var': Eb[edge['position']][v][w] ^= 1
    request = dict(N=N, n=n, q=q, t=occurrences[0]['exit'],
                   suffixes=[p.text(b.nt(t)) for t in suffix], letters=d['letters'], E0=E0, Eb=Eb)
    return dict(request=request, occurrences=occurrences, vertices=vertices, edges=edges,
                suffix=suffix, y=y, z=z)

def local(o, data, v):
    """Generate one recurrence; all arrays/terms are original input data."""
    d, y, z = data['request'], data['y'], data['z']
    # Suffixes are opaque atoms in list reduction, retaining their full trees.
    S = [b.atom((1, w), b.nt(t)) for w, t in enumerate(data['suffix'])]
    q = d['q']; oid, kind = data['vertices'][v]; node = data['occurrences'][oid]
    const = b.W(d['E0'][v], S, z)
    active = [(a, w) for a in range(d['n']) for w in range(d['N']) if d['Eb'][a][v][w]]
    if len(active) > 1: raise c.Invalid('actual leaf has multiple letter edges')
    nonzero = y if v == d['t'] else const if not active else b.product(
        b.atom((3, active[0][0]), d['letters'][active[0][0]]), S[active[0][1]])
    if kind == 'exit':
        if b.nt(S[v]) != b.nt(nonzero): raise c.Invalid('connector continuation mismatch')
        seed = o.refl(S[v]); case = 'terminal' if v == d['t'] else (
            'add-exit-' + node['side'] if data['occurrences'][node['parent']]['tree'][0] == 'add'
            else 'mul-exit-' + node['side'])
    else:
        op = node['tree'][0]; tail = node['tail']
        if op == 'add':
            l, r = [data['occurrences'][i]['value'] for i in node['children']]
            seed = o.law('right_dist', {'A': l, 'B': r, 'C': tail})
        elif op == 'mul':
            l, r = [data['occurrences'][i]['value'] for i in node['children']]
            seed = o.law('prod_assoc', {'A': l, 'B': r, 'C': tail})
        elif op == 'one': seed = o.law('unitL', {'A': tail})
        elif op == 'zero': seed = o.law('zero_prodL', {'A': tail})
        else: seed = o.refl(S[v])
        case = op + '-entry'
    if o.p.rows[seed][0] != p.E(b.nt(S[v]), b.nt(nonzero)):
        raise c.Invalid('actual outgoing seed endpoint')
    # Form every absent product before balancing; its paid proof reduces it.
    old, new, roots = [], [], []
    for a, name in enumerate(d['letters']):
        x = b.atom((3, a), name); chosen = b.W(d['Eb'][a][v], S, z)
        term = b.product(x, chosen); old.append(term)
        if active and a == active[0][0]:
            new.append(b.atom((2, a, active[0][1]), b.nt(term)))
            roots.append(o.refl(term))
        else:
            if chosen != z: raise c.Invalid('unassigned letter edge')
            new.append(z); roots.append(o.law('prod_zero', {'A': x}))
    letter_sum, reduced_sum, j = b.combine(o, old, new, roots, z)
    reduced, k = b.erase_zeros(o, reduced_sum, z)
    letter_proof = o.trans(letter_sum, reduced_sum, reduced, j, k)
    inner = b.X(const, letter_sum); mid = b.X(const, reduced)
    j = o.p.mp(letter_proof, o.law('congR', {'A': letter_sum, 'B': reduced, 'C': const}))
    inner_result, k = b.erase_zeros(o, mid, z)
    j = o.trans(inner, mid, inner_result, j, k)
    terminal = y if v == d['t'] else z
    rhs = b.X(terminal, inner); mid = b.X(terminal, inner_result)
    j = o.p.mp(j, o.law('congR', {'A': inner, 'B': inner_result, 'C': terminal}))
    final, k = b.erase_zeros(o, mid, z)
    j = o.trans(rhs, mid, final, j, k)
    if b.nt(final) != b.nt(nonzero): raise c.Invalid('literal RHS reduction mismatch')
    root = o.trans(S[v], nonzero, rhs, seed, o.symm(rhs, final, j))
    expected = ep.e.c.serialize(ep.request(d)['local'][v])
    if p.text(o.p.rows[root][0]) != expected: raise c.Invalid('L065 exact endpoint')
    # All records, even unused imports, stay. Force the exact endpoint last.
    conditional = o.p.mp(root, o.p.ax('ax1', o.p.rows[root][0], p.I(q, q)))
    root = o.p.mp(o.p.identity(q), conditional)
    o.root = root
    return dict(case=case, root=root, expected=expected, law_calls=len(o.calls),
                argument_height=o.max_argument_height)
