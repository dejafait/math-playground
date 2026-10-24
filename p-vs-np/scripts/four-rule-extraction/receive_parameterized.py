"""Independent bounded typed receiver; imports no emitter or correction code."""
import hashlib
import json
from pathlib import Path
from parameterized_input import (CAPS, Rejected, require, bound, integer, fields,
                                typed, load, request, symbol_map, read_bytes, write_json, input_bounds, parse, exact_equal)

class Arithmetic:
    def __init__(self, req):
        self.alphabet = req['alphabet']
        self.dictionary = req['dictionary']
        self.counts = dict(multiplication_pairs=0, max_polynomial_words=0,
                           max_word_length=0, max_stored_words=0)

    def check(self, poly):
        n = len(poly)
        length = max(map(len, poly), default=0)
        self.counts['max_polynomial_words'] = max(n, self.counts['max_polynomial_words'])
        self.counts['max_word_length'] = max(length, self.counts['max_word_length'])
        bound(n, 'polynomial_words', 'intermediate polynomial')
        bound(length, 'word_length', 'intermediate word')
        return poly

    def add(self, a, b):
        out = set(a)
        for w in b:
            if w in out:
                out.remove(w)
            else:
                bound(len(out)+1,'polynomial_words','addition before insertion')
                out.add(w)
        return self.check(out)

    def mul(self, a, b):
        self.counts['multiplication_pairs'] += len(a)*len(b)
        bound(self.counts['multiplication_pairs'],'multiplication_pairs','before multiplication')
        out = set()
        for u in a:
            for v in b:
                bound(len(u)+len(v),'word_length','before concatenation')
                w = u + v
                if w in out:
                    out.remove(w)
                else:
                    bound(len(out)+1,'polynomial_words','multiplication before insertion')
                    out.add(w)
                self.check(out)
        return out

    def translation(self, t):
        if isinstance(t, str):
            return set() if t == 'true' else {()} if t == 'false' else {(('original', self.alphabet.index(t)),)}
        a = self.translation(t[1])
        return self.add({()}, a) if t[0] == 'not' else self.mul(a, self.translation(t[2]))

    def label(self, label, mode):
        out = set()
        for symbol in label:
            if symbol[0]=='one':
                term = {()}
            elif symbol[0]=='original' or mode=='free':
                term = {(tuple(symbol),)}
            elif mode=='zero':
                term = set()
            else:
                p = self.dictionary['placeholders'][symbol[1]]
                term = {tuple(('original',self.alphabet.index(x)) for x in w)
                        for w in p['polynomial']}
            out = self.add(out, term)
        return out

    def evaluate(self, nv, edges, order, source, sink, mode):
        adj = [[] for _ in range(nv)]
        for u, v, label in edges:
            adj[u].append((v, label))
        table, storage = [set() for _ in range(nv)], 0
        for u in reversed(order):
            value = {()} if u == sink else set()
            for v, label in adj[u]:
                value = self.add(value, self.mul(self.label(label, mode), table[v]))
            table[u] = value
            storage += len(value)
            self.counts['max_stored_words'] = max(storage, self.counts['max_stored_words'])
            bound(storage, 'stored_words', 'stored traversal words')
        return table[source]


def topo(nv, edges, req):
    require(integer(nv) and nv > 0, 'vertex count')
    require(type(edges) is list, 'edges list')
    bound(nv+len(edges),'records','graph before adjacency allocation')
    label_entries = 0
    for edge in edges:
        require(type(edge) is list and len(edge) == 3, 'edge schema')
        u, v, label = edge
        require(integer(u) and integer(v) and 0 <= u < nv and 0 <= v < nv, 'edge index')
        require(type(label) is list, 'affine label list')
        bound(len(label),'label_width','individual affine label')
        label_entries += len(label)
        bound(label_entries,'label_entries','total affine label entries')
        for x in label:
            require(type(x) is list and bool(x), 'typed affine symbol')
            require((x==['one']) or (len(x)==2 and type(x[0]) is str and
                    integer(x[1]) and x[0] in ('original','placeholder') and
                    0<=x[1]<(len(req['alphabet']) if x[0]=='original' else
                             len(req['dictionary']['placeholders']))), 'typed symbol index')
    # Allocate adjacency only after every label/endpoint passes preflight.
    incoming, adj = [0]*nv, [[] for _ in range(nv)]
    for u,v,_ in edges:
        adj[u].append(v)
        incoming[v] += 1
    ready, order = [v for v in range(nv) if incoming[v] == 0], []
    while ready:
        u = ready.pop()
        order.append(u)
        for v in adj[u]:
            incoming[v] -= 1
            if incoming[v] == 0:
                ready.append(v)
    require(len(order) == nv, 'graph cycle')
    return order


def serial(poly):
    return [list(w) for w in sorted(poly, key=lambda w:(len(w),w))]


def receive(path, source_path, request_path):
    # Authorization comes from the caller's paths, never from candidate fields.
    req, raw, records, source_result = request(source_path, request_path)
    certificate_raw = read_bytes(path,'certificate_bytes')
    data = parse(certificate_raw)
    fields(data, 'format caps source_sha256 source_text source_check dictionary symbol_table graph line_roots blocks construction')
    require(data['format']=='L108-parameterized-v1', 'format')
    require(exact_equal(data['caps'],CAPS), 'caps changed')
    require(type(data['source_text']) is str and raw.decode()==data['source_text'], 'source retention')
    require(data['source_sha256']==req['source_sha256'], 'caller source digest retention')
    require(exact_equal(data['source_check'],source_result), 'typed source checker evidence')
    require(exact_equal(data['dictionary'],req['dictionary']), 'complete caller dictionary')
    require(exact_equal(data['symbol_table'],symbol_map(req['alphabet'],req['dictionary'])),
            'typed dense symbol table')
    n = len(records)
    graph = data['graph']
    fields(graph, 'vertices edges source sink')
    nv, edges = graph['vertices'], graph['edges']
    order = topo(nv, edges, req)
    require(integer(graph['source']) and graph['source'] == 0, 'source root')
    require(integer(graph['sink']) and graph['sink'] == n, 'final endpoint')
    require(type(data['line_roots']) is list and all(integer(i) for i in data['line_roots'])
            and data['line_roots'] == list(range(1,n+1)), 'all exact line roots')
    fields(data['construction'], 'max_intermediate_records commutator_calls')
    require(all(integer(v) and 0 <= v <= CAPS['records'] for v in data['construction'].values()),
            'construction counters')
    fs = [r['f'] for r in records]
    expected = []
    for i, r in enumerate(records):
        tag, f, refs = r['rule'], r['f'], r['refs']
        if tag == 'axiom':
            kind, args = 'boolean', [f[2]]
        elif tag == 'contraction':
            kind, args = 'boolean', [f]
        elif tag == 'expansion':
            kind, args = 'commutator', [fs[refs[0]], f[1]]
        elif tag == 'cut':
            kind, args = 'prefixed-commutator', [fs[refs[0]][1], fs[refs[0]][2], fs[refs[1]][2]]
        else:
            kind, args = 'zero', []
        expected.append((i,'seed',kind,args,None))
        factors = ([f[1]] if tag == 'expansion' else ['false'] if tag in ('association','contraction')
                   else [fs[refs[1]][2], fs[refs[0]][2]] if tag == 'cut' else [])
        expected.extend((i,'transition','translation',[factor],j) for j,factor in zip(refs,factors))
    require(type(data['blocks']) is list and len(data['blocks']) == len(expected), 'all seed/transition occurrences')
    arithmetic, block_results = Arithmetic(req), []
    next_vertex, next_edge = n+1, 0
    for k, (block, exp) in enumerate(zip(data['blocks'], expected)):
        fields(block, 'line role kind arguments parent vertex_range edge_range entry exit')
        i, role, kind, args, parent = exp
        require(integer(block['line']) and (block['parent'] is None or integer(block['parent'])), 'block integer fields')
        require((block['line'],block['role'],block['kind'],block['arguments'],block['parent']) == exp,
                'exact source/block provenance')
        for name in ('vertex_range','edge_range'):
            require(type(block[name]) is list and len(block[name]) == 2 and
                    all(integer(v) for v in block[name]), 'block range schema')
        lo, hi = block['vertex_range']
        first, last = block['edge_range']
        require(lo == next_vertex and lo < hi <= nv and first == next_edge and first + 2 <= last <= len(edges),
                'complete contiguous block partition')
        s, t = block['entry'], block['exit']
        require(integer(s) and integer(t) and lo <= s < hi and lo <= t < hi, 'block endpoints')
        require(edges[last-2:last] == [[0 if parent is None else parent+1,s,[['one']]], [t,i+1,[['one']]]],
                'exact block connectors')
        inner = edges[first:last-2]
        require(all(lo <= u < hi and lo <= v < hi for u,v,_ in inner), 'fresh block interior')
        local = [[u-lo,v-lo,label] for u,v,label in inner]
        local_order = topo(hi-lo,local,req)
        if role == 'transition':
            require(all(a[0] in ('one','original') for _,_,lab in inner for a in lab), 'original-only multiplier')
        polys = {mode:arithmetic.evaluate(hi-lo,local,local_order,s-lo,t-lo,mode)
                 for mode in ('free','zero','axioms')}
        vals = [arithmetic.translation(arg) for arg in args]
        if kind == 'zero':
            target = set()
        elif kind == 'translation':
            target = vals[0]
        elif kind == 'boolean':
            target = arithmetic.add(arithmetic.mul(vals[0],vals[0]),vals[0])
        else:
            a, b = vals[-2:]
            target = arithmetic.add(arithmetic.mul(a,b),arithmetic.mul(b,a))
            if kind == 'prefixed-commutator':
                target = arithmetic.mul(arithmetic.add({()},vals[0]),target)
        require(polys['axioms'] == target, f'block {k} substituted identity')
        require(polys['zero'] == (target if role == 'transition' else set()), f'block {k} zero identity')
        if role == 'transition':
            require(polys['free'] == target, f'block {k} free multiplier')
        block_results.append(dict(block=k,line=i,role=role,kind=kind,
                                  polynomials={mode:serial(p) for mode,p in polys.items()},target=serial(target)))
        next_vertex, next_edge = hi,last
    require(next_vertex == nv and next_edge == len(edges), 'unaccounted graph records')
    roots = []
    for i, r in enumerate(records):
        polys = {mode:arithmetic.evaluate(nv,edges,order,0,i+1,mode)
                 for mode in ('free','zero','axioms')}
        target = arithmetic.translation(r['f'])
        require(not polys['zero'] and polys['axioms'] == target, f'line {i} identities')
        roots.append(dict(line=i,root=i+1,formula=r['f'],
                          polynomials={mode:serial(p) for mode,p in polys.items()},target=serial(target)))
    return dict(accepted=True, roots=roots, blocks=block_results, arithmetic=arithmetic.counts,
                bounds=dict(records_actual=nv+len(edges),records_cap=CAPS['records'],
                            bytes_actual=len(certificate_raw),bytes_cap=CAPS['certificate_bytes']),
                source=source_result, input_bounds=input_bounds(req,raw,records,request_path), caps=CAPS,
                certificate_sha256=hashlib.sha256(certificate_raw).hexdigest(), failures=[])


if __name__=='__main__':
    import argparse
    ap=argparse.ArgumentParser()
    ap.add_argument('certificate',type=Path)
    ap.add_argument('source',type=Path)
    ap.add_argument('request',type=Path,help='independently selected caller authorization')
    ap.add_argument('output',type=Path)
    args=ap.parse_args()
    try:
        result=receive(args.certificate,args.source,args.request)
        write_json(args.output,result)
        print(json.dumps(dict(accepted=True,roots=len(result['roots']),
                              blocks=len(result['blocks']), arithmetic=result['arithmetic'],
                              actual_required=result['bounds'], evidence=str(args.output))))
    except Exception as e:
        write_json(args.output.with_suffix('.failure.json'),
                   dict(accepted=False,failure=repr(e),artifact=str(args.certificate),caps=CAPS))
        raise
