"""Step-453 pinned strict receiver: no constructor or correction-evaluator imports."""
import hashlib
import importlib.util
import json
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
OUT = Path(__file__).with_name('output-453')
CAPS = dict(records=2_000_000, certificate_bytes=200_000_000,
            polynomial_words=1_000_000, word_length=256,
            multiplication_pairs=100_000_000, stored_words=20_000_000)
SHA = '004ca652885f26286b576af5b923b89bac8f1f933dedc9c6b800677c564f9335'
GOAL = ['or', 'A', ['or', ['not', 'B'], 'B']]
DICTIONARY = {'alphabet':['A','B'], 'placeholders':[
    {'name':'sigma:A','kind':'boolean','originals':['A'],'polynomial':[['A','A'],['A']]},
    {'name':'sigma:B','kind':'boolean','originals':['B'],'polynomial':[['B','B'],['B']]},
    {'name':'tau:A:B','kind':'commutator','originals':['A','B'],
     'polynomial':[['A','B'],['B','A']]}]}
TRANSPORT = {'1':'1','x1':'A','x2':'B','b:1':'sigma:A','b:2':'sigma:B','t:1:2':'tau:A:B'}
spec = importlib.util.spec_from_file_location('literal_source_checker', BASE / 'parity-four-rule/checker.py')
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class Rejected(ValueError):
    pass


def require(ok, message):
    if not ok:
        raise Rejected(message)


def integer(x):
    return type(x) is int


def fields(x, keys):
    require(type(x) is dict and set(x) == set(keys.split()), 'schema fields: ' + keys)


def no_duplicates(pairs):
    out = {}
    for k, v in pairs:
        require(k not in out, 'duplicate JSON key: ' + k)
        out[k] = v
    return out


def load(path):
    require(path.stat().st_size <= CAPS['certificate_bytes'], 'certificate byte cap')
    return json.loads(path.read_bytes(), object_pairs_hook=no_duplicates)


class Arithmetic:
    def __init__(self):
        self.counts = dict(multiplication_pairs=0, max_polynomial_words=0,
                           max_word_length=0, max_stored_words=0)

    def check(self, poly):
        n = len(poly)
        length = max(map(len, poly), default=0)
        self.counts['max_polynomial_words'] = max(n, self.counts['max_polynomial_words'])
        self.counts['max_word_length'] = max(length, self.counts['max_word_length'])
        require(n <= CAPS['polynomial_words'], f'polynomial word cap: {n}')
        require(length <= CAPS['word_length'], f'word length cap: {length}')
        return poly

    def add(self, a, b):
        return self.check(a.symmetric_difference(b))

    def mul(self, a, b):
        self.counts['multiplication_pairs'] += len(a)*len(b)
        require(self.counts['multiplication_pairs'] <= CAPS['multiplication_pairs'],
                'multiplication pair cap: ' + str(self.counts['multiplication_pairs']))
        out = set()
        for u in a:
            for v in b:
                w = u + v
                require(len(w) <= CAPS['word_length'], 'word length cap before cancellation')
                if w in out:
                    out.remove(w)
                else:
                    out.add(w)
                self.check(out)
        return out

    def translation(self, t):
        if isinstance(t, str):
            return set() if t == 'true' else {()} if t == 'false' else {(t,)}
        a = self.translation(t[1])
        return self.add({()}, a) if t[0] == 'not' else self.mul(a, self.translation(t[2]))

    def label(self, label, mode):
        out = set()
        for symbol in label:
            term = ({()} if symbol == '1' else {(symbol,)} if symbol in ('A','B') or mode == 'free'
                    else set() if mode == 'zero' else
                    {tuple(w) for p in DICTIONARY['placeholders'] if p['name'] == symbol
                     for w in p['polynomial']})
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
            require(storage <= CAPS['stored_words'], 'stored word cap: ' + str(storage))
        return table[source]


def topo(nv, edges):
    require(integer(nv) and 0 < nv <= CAPS['records'], 'vertex count')
    require(type(edges) is list and nv + len(edges) <= CAPS['records'], 'record count cap')
    incoming, adj = [0]*nv, [[] for _ in range(nv)]
    symbols = {'1','A','B','sigma:A','sigma:B','tau:A:B'}
    for edge in edges:
        require(type(edge) is list and len(edge) == 3, 'edge schema')
        u, v, label = edge
        require(integer(u) and integer(v) and 0 <= u < nv and 0 <= v < nv, 'edge index')
        require(type(label) is list and all(type(x) is str and x in symbols for x in label),
                'affine label symbol/schema')
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


def receive(path, source_path):
    data = load(path)
    fields(data, 'format caps source_sha256 source_text source_check dictionary name_transport graph line_roots blocks construction')
    require(data['format'] == 'L108-finite-exercise-v1', 'format')
    # Fixed local caps cannot be raised by an untrusted certificate.
    require(json.dumps(data['caps'], sort_keys=True) == json.dumps(CAPS, sort_keys=True), 'caps changed')
    raw = source_path.read_bytes()
    source_result = checker.check(source_path, GOAL)
    require(raw.decode() == data['source_text'], 'source retention')
    require(hashlib.sha256(raw).hexdigest() == SHA == data['source_sha256'], 'preserved source digest')
    # Python equality identifies True with 1 (and integer counts with floats).
    # This field retains typed checker evidence, not merely equal numeric values.
    require(json.dumps(source_result, sort_keys=True) ==
            json.dumps(data['source_check'], sort_keys=True), 'source checker evidence')
    header, *records = [json.loads(line, object_pairs_hook=no_duplicates) for line in raw.splitlines()]
    require(header['alphabet'] == ['A','B'] and len(records) == 9, 'source alphabet/records')
    require(data['dictionary'] == DICTIONARY, 'complete ordered dictionary')
    require(data['name_transport'] == TRANSPORT, 'collision-free name transport')
    graph = data['graph']
    fields(graph, 'vertices edges source sink')
    nv, edges = graph['vertices'], graph['edges']
    order = topo(nv, edges)
    require(integer(graph['source']) and graph['source'] == 0, 'source root')
    require(integer(graph['sink']) and graph['sink'] == 9, 'final endpoint')
    require(type(data['line_roots']) is list and all(integer(i) for i in data['line_roots'])
            and data['line_roots'] == list(range(1,10)), 'nine exact line roots')
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
    arithmetic, block_results = Arithmetic(), []
    next_vertex, next_edge = 10, 0
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
        require(edges[last-2:last] == [[0 if parent is None else parent+1,s,['1']], [t,i+1,['1']]],
                'exact block connectors')
        inner = edges[first:last-2]
        require(all(lo <= u < hi and lo <= v < hi for u,v,_ in inner), 'fresh block interior')
        local = [[u-lo,v-lo,label] for u,v,label in inner]
        local_order = topo(hi-lo,local)
        if role == 'transition':
            require(all(a in ('1','A','B') for _,_,lab in inner for a in lab), 'original-only multiplier')
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
                            bytes_actual=path.stat().st_size,bytes_cap=CAPS['certificate_bytes']),
                source=source_result, caps=CAPS,
                certificate_sha256=hashlib.sha256(path.read_bytes()).hexdigest(), failures=[])


if __name__ == '__main__':
    try:
        result = receive(OUT/'certificate.json',OUT/'source.jsonl')
    except Exception as err:
        (OUT/'reception-failure.json').write_text(json.dumps({'failure':repr(err),'caps':CAPS},indent=2)+'\n')
        raise
    (OUT/'reception.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ('accepted','bounds','arithmetic','failures')}))
    print('Complete reception:',OUT/'reception.json')
