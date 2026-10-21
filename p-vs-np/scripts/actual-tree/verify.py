"""Independent source/graph/suffix contract; imports no actual-tree emitter."""
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('tree_contract_ep', HERE.parent / 'left-closure' / 'endpoints.py')
ep = importlib.util.module_from_spec(spec); spec.loader.exec_module(ep)
e, c = ep.e, ep.c

def contract(source, graph, request):
    letters, q = source['letters'], source['q']
    y, z = e.imp(q, q), e.neg(e.imp(q, q))
    vertices, expected_edges, records = [], [], []
    def visit(t):
        rec = dict(tree=t, entry=len(vertices)); vertices.append(rec)
        records.append(rec)
        if t[0] in ('add', 'mul'):
            l, r = visit(t[1]), visit(t[2]); rec['children'] = (l, r)
            rec['value'] = (e.xor if t[0] == 'add' else e.prod)(l['value'], r['value'])
        else: rec['value'] = y if t[0] == 'one' else z if t[0] == 'zero' else letters[t[1]]
        rec['exit'] = len(vertices); vertices.append(rec)
        if t[0] in ('add', 'mul'):
            l, r = rec['children']
            pairs = [(rec['entry'], l['entry']), (rec['entry'], r['entry']),
                     (l['exit'], rec['exit']), (r['exit'], rec['exit'])] if t[0] == 'add' else [
                     (rec['entry'], l['entry']), (l['exit'], r['entry']), (r['exit'], rec['exit'])]
            expected_edges.extend(dict(v=v, w=w, kind='one') for v, w in pairs)
        elif t[0] != 'zero' or not source['delete_zero']:
            edge = dict(v=rec['entry'], w=rec['exit'], kind=t[0])
            if t[0] == 'var': edge['position'] = t[1]
            expected_edges.append(edge)
        return rec
    root = visit(source['tree']); N = len(vertices)
    S = [None] * N
    def fill(rec, continuation):
        S[rec['entry']] = e.prod(rec['value'], continuation); S[rec['exit']] = continuation
        if 'children' in rec:
            l, r = rec['children']
            fill(l, continuation if rec['tree'][0] == 'add' else e.prod(r['value'], continuation))
            fill(r, continuation)
    fill(root, y)
    key = lambda edge: (edge['v'], edge['w'], edge['kind'], edge.get('position', -1))
    if sorted(graph, key=key) != sorted(expected_edges, key=key): raise c.Invalid('actual connector graph')
    E0 = [[0] * N for _ in range(N)]; Eb = [[[0] * N for _ in range(N)] for _ in letters]
    for edge in expected_edges:
        v, w = edge['v'], edge['w']
        if not v < w: raise c.Invalid('actual topological order')
        if edge['kind'] == 'one': E0[v][w] ^= 1
        elif edge['kind'] == 'var': Eb[edge['position']][v][w] ^= 1
    expected = dict(N=N, n=len(letters), t=root['exit'], q=q, letters=letters,
                    suffixes=[c.serialize(t) for t in S], E0=E0, Eb=Eb)
    if request != expected: raise c.Invalid('actual suffix/table/order/constant mismatch')
    local = []
    for v in range(N):
        rhs = e.xor(y if v == root['exit'] else z, e.xor(e.choose(E0[v], S, z),
                    e.bal([e.prod(x, e.choose(Eb[a][v], S, z)) for a, x in enumerate(letters)], z)))
        local.append(c.serialize(e.eq(S[v], rhs)))
    # Independent literal construction agrees with the unchanged receiver.
    if local != [c.serialize(t) for t in ep.request(request)['local']]:
        raise c.Invalid('receiving endpoint mismatch')
    return local
