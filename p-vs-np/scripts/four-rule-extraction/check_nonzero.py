"""Step 453: independent forward arithmetic and contribution diagnostics; finite only."""
import contextlib
import copy
from collections import Counter, deque
import hashlib
import importlib.util
import io
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
NOTEBOOK = HERE.parents[1]
OUT = HERE/'output-453'
OUT.mkdir(exist_ok=True)
MODES = ('free', 'zero', 'axioms')
CAPS = dict(records=2_000_000, certificate_bytes=200_000_000,
            polynomial_words=1_000_000, word_length=256,
            multiplication_pairs=100_000_000, stored_words=20_000_000)
stats = dict(multiplication_pairs=0, max_polynomial_words=0,
             max_word_length=0, max_stored_words=0)


def demand(ok, msg):
    if not ok:
        raise AssertionError(msg)


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def strict_pairs(pairs):
    d = {}
    for k, v in pairs:
        demand(k not in d, 'duplicate key ' + k)
        d[k] = v
    return d


def read(p):
    return json.loads(p.read_bytes(), object_pairs_hook=strict_pairs)


def typed(x):
    return json.dumps(x, sort_keys=True, separators=(',', ':'))


def counters(actual, saved):
    # Transient word-set sizes depend on salted string-hash iteration order;
    # completed polynomials and the other counters do not on this fixture.
    for key in actual:
        if key != 'max_polynomial_words':
            demand(actual[key] == saved[key], 'stable arithmetic counter '+key)
    demand(0 <= actual['max_polynomial_words'] <= CAPS['polynomial_words'] and
           0 <= saved['max_polynomial_words'] <= CAPS['polynomial_words'], 'word count caps')


def write(name, value):
    (OUT/name).write_text(json.dumps(value, indent=2)+'\n')


def module(name, p):
    spec = importlib.util.spec_from_file_location(name, p)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def reduced(c):
    p = {w: 1 for w, n in c.items() if n % 2}
    stats['max_polynomial_words'] = max(stats['max_polynomial_words'], len(p))
    stats['max_word_length'] = max(stats['max_word_length'], max(map(len, p), default=0))
    demand(len(p) <= CAPS['polynomial_words'], 'audit polynomial cap')
    demand(stats['max_word_length'] <= CAPS['word_length'], 'audit word length cap')
    return p


def add(a, b):
    c = Counter(a)
    c.update(b)
    return reduced(c)


def mul(a, b):
    stats['multiplication_pairs'] += len(a)*len(b)
    demand(stats['multiplication_pairs'] <= CAPS['multiplication_pairs'], 'audit pair cap')
    c = Counter()
    for u, av in a.items():
        for v, bv in b.items():
            demand(len(u)+len(v) <= CAPS['word_length'], 'audit concatenation cap')
            c[u+v] += av*bv
    demand(len(c) <= CAPS['polynomial_words'], 'audit unreduced word cap')
    return reduced(c)


def tr(t):
    if type(t) is str:
        return {} if t == 'true' else {(): 1} if t == 'false' else {(t,): 1}
    demand(type(t) is list, 'audit tree type')
    if t[0] == 'not' and len(t) == 2:
        return add({(): 1}, tr(t[1]))
    demand(t[0] == 'or' and len(t) == 3, 'audit tree shape')
    return mul(tr(t[1]), tr(t[2]))


SUB = {'sigma:A': {('A','A'): 1, ('A',): 1},
       'sigma:B': {('B','B'): 1, ('B',): 1},
       'tau:A:B': {('A','B'): 1, ('B','A'): 1}}


def label(lab, mode):
    v = {}
    for a in lab:
        demand(a in ('1','A','B') or a in SUB, 'audit unknown name')
        p = {(): 1} if a == '1' else {(a,): 1}
        if a in SUB and mode != 'free':
            p = {} if mode == 'zero' else SUB[a]
        v = add(v, p)
    return v


def forward(nv, edges, source, mode):
    """Independent FIFO forward coefficient accumulation; returns every root."""
    demand(type(nv) is int and nv+len(edges) <= CAPS['records'], 'audit records cap')
    incoming, adj = [0]*nv, [[] for _ in range(nv)]
    for u, v, lab in edges:
        demand(type(u) is int and type(v) is int and 0 <= u < nv and 0 <= v < nv,
               'audit endpoint')
        incoming[v] += 1
        adj[u].append((v, label(lab, mode)))
    ready = deque(i for i, n in enumerate(incoming) if n == 0)
    values, seen, stored = [{} for _ in range(nv)], 0, 1
    values[source] = {(): 1}
    while ready:
        u = ready.popleft()
        seen += 1
        for v, p in adj[u]:
            old = len(values[v])
            values[v] = add(values[v], mul(values[u], p))
            stored += len(values[v])-old
            stats['max_stored_words'] = max(stats['max_stored_words'], stored)
            demand(stored <= CAPS['stored_words'], 'audit stored cap')
            incoming[v] -= 1
            if incoming[v] == 0:
                ready.append(v)
    demand(seen == nv, 'audit cycle')
    return values


def serial(p):
    return [list(w) for w in sorted(p, key=lambda w: (len(w), w))]


def changed(a, b, path=''):
    if type(a) is not type(b):
        return [dict(pointer=path, before=a, after=b)]
    if isinstance(a, dict) and set(a) == set(b):
        return [c for k in a for c in changed(a[k], b[k], path+'/'+k)]
    if isinstance(a, list) and len(a) == len(b):
        return [c for i, (x,y) in enumerate(zip(a,b)) for c in changed(x,y,path+'/'+str(i))]
    return [] if a == b else [dict(pointer=path, before=a, after=b)]


def main():
    # Independently fixed input authorization, not a digest supplied by a certificate.
    raw = (OUT/'source.jsonl').read_bytes()
    demand(hashlib.sha256(raw).hexdigest() ==
           '004ca652885f26286b576af5b923b89bac8f1f933dedc9c6b800677c564f9335', 'source SHA')
    header, *records = [json.loads(s, object_pairs_hook=strict_pairs) for s in raw.splitlines()]
    demand(header == dict(format='literal-four-rule-v1', alphabet=['A','B'],
                          goal=['or','A',['or',['not','B'],'B']]), 'fixed header')
    demand(len(records) == 9, 'fixed record count')
    cert, saved = (read(OUT/n) for n in ('certificate.json','reception.json'))
    r = module('nonzero_receiver', HERE/'receive_nonzero.py')
    result = r.receive(OUT/'certificate.json', OUT/'source.jsonl')
    demand(typed({k:v for k,v in result.items() if k != 'arithmetic'}) ==
           typed({k:v for k,v in saved.items() if k != 'arithmetic'}), 'complete reception replay')
    counters(result['arithmetic'], saved['arithmetic'])
    write('replayed-reception.json', result)
    g = cert['graph']
    values = {m:forward(g['vertices'],g['edges'],0,m) for m in MODES}
    roots = []
    for i, rec in enumerate(records):
        item = dict(line=i, root=i+1, formula=rec['f'],
                    polynomials={m:serial(values[m][i+1]) for m in MODES},
                    target=serial(tr(rec['f'])))
        demand(typed(item) == typed(saved['roots'][i]), 'independent root '+str(i))
        roots.append(item)
    blocks = []
    for k, b in enumerate(cert['blocks']):
        lo, hi = b['vertex_range']
        first, last = b['edge_range']
        es = [[u-lo,v-lo,l] for u,v,l in g['edges'][first:last-2]]
        polynomials = {m:serial(forward(hi-lo,es,b['entry']-lo,m)[b['exit']-lo]) for m in MODES}
        args = [tr(t) for t in b['arguments']]
        if b['kind'] == 'zero':
            target = {}
        elif b['kind'] == 'translation':
            target = args[0]
        elif b['kind'] == 'boolean':
            target = add(mul(args[0],args[0]), args[0])
        else:
            target = add(mul(args[-2],args[-1]), mul(args[-1],args[-2]))
            if b['kind'] == 'prefixed-commutator':
                target = mul(add({():1},args[0]), target)
        item = dict(block=k,line=b['line'],role=b['role'],kind=b['kind'],
                    polynomials=polynomials,target=serial(target))
        demand(typed(item) == typed(saved['blocks'][k]), 'independent block '+str(k))
        blocks.append(item)
    write('independent-polynomials.json', dict(roots=roots,blocks=blocks,
                                             arithmetic=stats.copy(),caps=CAPS))
    cut = next(k for k,b in enumerate(cert['blocks']) if b['line'] == 8 and b['role'] == 'seed')
    boolean = next(k for k,b in enumerate(cert['blocks']) if b['line'] == 1 and b['role'] == 'seed')

    def delete_cut(d):
        first, last = d['blocks'][cut]['edge_range']
        hits = 0
        for _,_,lab in d['graph']['edges'][first:last-2]:
            hits += lab.count('tau:A:B')
            lab[:] = [a for a in lab if a != 'tau:A:B']
        demand(hits > 0, 'selected cut placeholder labels exist')

    def delete_sigma(d):
        first, last = d['blocks'][boolean]['edge_range']
        hits = 0
        for _,_,lab in d['graph']['edges'][first:last-2]:
            hits += lab.count('sigma:B')
            lab[:] = [a for a in lab if a != 'sigma:B']
        demand(hits > 0, 'selected sigma_B labels exist')

    tests, contributions = [], []
    mut = OUT/'mutations'
    mut.mkdir(exist_ok=True)

    def case(name, change, accept=False):
        d = copy.deepcopy(cert)
        change(d)
        p = mut/(name+'.json')
        p.write_text(typed(d)+'\n')
        try:
            r.receive(p,OUT/'source.jsonl')
            accepted, reason = True, 'full strict reception accepted'
        except (r.Rejected,r.checker.Invalid,ValueError,TypeError,KeyError) as e:
            accepted, reason = False,str(e)
        demand(accepted == accept, 'mutation expected verdict '+name)
        tests.append(dict(case=name,accepted=accepted,expected_accept=accept,reason=reason,
                          changes=changed(cert,d),certificate_path=str(p.relative_to(NOTEBOOK)),
                          sha256=digest(p)))
        return d

    # Full graph subtraction isolates exactly the contribution removed. It also
    # retains all earlier/later seeds in the diagnostic, allowing cancellations.
    for name, k, change in (('delete-selected-cut-seed',cut,delete_cut),
                            ('delete-selected-sigma-B',boolean,delete_sigma)):
        d = case(name,change)
        h = d['graph']
        probes = {m:forward(h['vertices'],h['edges'],0,m) for m in MODES}
        local_line, final_root = cert['blocks'][k]['line'], g['sink']
        final = {m:add(values[m][final_root],probes[m][final_root]) for m in MODES}
        local = {m:add(values[m][local_line+1],probes[m][local_line+1]) for m in MODES}
        demand(final['free'] and final['axioms'] and not final['zero'], 'nonzero final contribution '+name)
        demand(local['free'] and local['axioms'] and not local['zero'], 'nonzero local contribution '+name)
        demand(probes['axioms'][final_root] != tr(header['goal']), 'final identity must fail '+name)
        demand(probes['axioms'][local_line+1] != tr(records[local_line]['f']), 'local identity must fail '+name)
        # Independent direct expected word lists, not graph-produced values.
        expected = ({('A','A','B'):1,('A','A','B','B'):1,
                     ('A','B','A'):1,('A','B','B','A'):1} if k == cut else
                    {('B','A','A'):1,('B','B','A','A'):1})
        demand(final['axioms'] == expected, 'complete expected substituted contribution '+name)
        if k == cut:
            demand(local == final, 'final cut has unit continuation')
        else:
            demand(local['free'] == {('sigma:B',):1}, 'selected sigma_B free seed')
            demand(final['free'] == {('sigma:B','A','A'):1}, 'complete sigma_B right continuation')
        contributions.append(dict(case=name,block=k,line=local_line,
            block_provenance=cert['blocks'][k],
            local_removed={m:serial(p) for m,p in local.items()},
            final_removed={m:serial(p) for m,p in final.items()},
            mutated_final={m:serial(probes[m][final_root]) for m in MODES},
            mutated_local={m:serial(probes[m][local_line+1]) for m in MODES},
            target=serial(tr(header['goal'])),expected_final_axioms=serial(expected),
            final_identity_failed=True,local_identity_failed=True))
    write('contributions.json',dict(discriminators=contributions,arithmetic=stats.copy(),caps=CAPS))

    case('missing-boolean-entry',lambda d:d['dictionary']['placeholders'].pop(1))
    case('pair-polynomial',lambda d:d['dictionary']['placeholders'][2]['polynomial'].pop())
    case('alphabet-order',lambda d:d['dictionary']['alphabet'].reverse())
    case('placeholder-alias',lambda d:d['dictionary']['placeholders'][1].update(name='sigma:A'))
    case('transport-alias',lambda d:d['name_transport'].update(x2='A'))
    case('foreign-edge-label',lambda d:d['graph']['edges'][0][2].append('foreign'))
    case('boolean-edge-index',lambda d:d['graph']['edges'][0].__setitem__(0,True))
    case('float-edge-index',lambda d:d['graph']['edges'][0].__setitem__(0,0.0))
    case('boolean-root-index',lambda d:d['line_roots'].__setitem__(0,True))
    case('float-sink',lambda d:d['graph'].__setitem__('sink',9.0))
    case('missing-root',lambda d:d['line_roots'].pop())
    case('changed-block-argument',lambda d:d['blocks'][cut].__setitem__('arguments',['A','B','B']))
    case('changed-block-parent',lambda d:d['blocks'][-1].__setitem__('parent',1))
    case('boolean-block-entry',lambda d:d['blocks'][0].__setitem__('entry',True))
    case('boolean-counter',lambda d:d['construction'].__setitem__('commutator_calls',True))
    case('evidence-accepted-integer',lambda d:d['source_check'].__setitem__('accepted',1))
    case('evidence-count-boolean',lambda d:d['source_check']['rule_counts'].__setitem__('true',True))
    case('evidence-count-float',lambda d:d['source_check'].__setitem__('records',9.0))
    case('changed-caps',lambda d:d['caps'].__setitem__('records',3_000_000))
    case('unretained-source',lambda d:d.__setitem__('source_text',d['source_text']+'\n'))
    case('false-source-digest',lambda d:d.__setitem__('source_sha256','0'*64))
    case('neutral-affine-cancellation',lambda d:d['graph']['edges'][0][2].extend(['A','A']),True)
    p = mut/'duplicate-key.json'
    p.write_text((OUT/'certificate.json').read_text().replace('{','{"format":"duplicate",',1))
    try:
        r.receive(p,OUT/'source.jsonl')
        demand(False,'duplicate key accepted')
    except r.Rejected as e:
        demand(str(e) == 'duplicate JSON key: format','duplicate rejection reason')
        tests.append(dict(case='duplicate-key',accepted=False,expected_accept=False,reason=str(e),
                          certificate_path=str(p.relative_to(NOTEBOOK)),sha256=digest(p)))

    # Mutate THIS source so every rejection tests its actual literal premises.
    source_cases = [
        ('axiom-order',0,'f',['or','A',['not','A']]),
        ('true-ground',2,'f','false'), ('not-false-ground',3,'f',['not','true']),
        ('expansion-premise',4,'refs',[0]), ('contraction-premise',6,'refs',[4]),
        ('association-bracketing',7,'f',records[4]['f']),
        ('cut-premise-order',8,'refs',[4,0]), ('cut-pivot',8,'refs',[1,4]),
        ('boolean-ref',4,'refs',[True]), ('float-ref',4,'refs',[1.0]),
        ('forward-ref',4,'refs',[4]), ('foreign-name',1,'f',['or',['not','C'],'C']),
        ('wrong-endpoint',8,'f',['or',['or','A',['not','B']],'B']),
        ('unsupported-rule',6,'rule','rewrite')]
    sources = []
    for name,i,field,value in source_cases:
        rs = copy.deepcopy(records)
        rs[i][field] = value
        p = mut/(name+'.jsonl')
        p.write_text('\n'.join(typed(x) for x in [header]+rs)+'\n')
        try:
            r.checker.check(p,r.GOAL)
            demand(False,'malformed source accepted '+name)
        except r.checker.Invalid as e:
            sources.append(dict(case=name,rejected=True,reason=str(e),
                                path=str(p.relative_to(NOTEBOOK)),sha256=digest(p)))
    write('mutation-results.json',dict(certificate_tests=tests,source_tests=sources))
    preserved = read(OUT/'preserved-input-hashes.json')
    demand(all(digest(NOTEBOOK/p) == sha for p,sha in preserved.items()), 'old archives changed')
    actual = dict(records=g['vertices']+len(g['edges']),certificate_bytes=(OUT/'certificate.json').stat().st_size,
                  polynomial_words=stats['max_polynomial_words'],word_length=stats['max_word_length'],
                  multiplication_pairs=stats['multiplication_pairs'],stored_words=stats['max_stored_words'])
    demand(all(actual[k] <= CAPS[k] for k in CAPS), 'complete independent caps')
    report = dict(accepted=True,roots=len(roots),blocks=len(blocks),contributions=2,
                  expected_rejections=sum(not t['expected_accept'] for t in tests),
                  neutral_acceptances=sum(t['expected_accept'] for t in tests),
                  source_rejections=len(sources),actual=actual,required=CAPS,
                  receiver_arithmetic=result['arithmetic'],construction=cert['construction'],
                  certificate_sha256=digest(OUT/'certificate.json'),preserved_files=len(preserved),
                  code_sha256={str(p.relative_to(NOTEBOOK)):digest(p) for p in
                               (HERE/'emit_nonzero.py',HERE/'receive_nonzero.py',Path(__file__),
                                HERE.parent/'parity-four-rule/checker.py',
                                HERE.parent/'affine-abp-boolean/check_suffix_graph.py',
                                HERE.parent/'alternative-abp-commutator/check_marked_edges.py')},
                  failures=[],limitations=['finite supplied fixture only','separate critical code audit pending'])
    write('verification.json',report)
    print(json.dumps({k:report[k] for k in ('accepted','roots','blocks','contributions',
                                          'expected_rejections','source_rejections','neutral_acceptances','failures')}))
    print('Independent actual/required:',typed(dict(actual=actual,required=CAPS)))
    print('Complete verification, polynomials, diagnostic copies:',OUT)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        write('verification-failure.json',dict(failure=repr(e),arithmetic=stats,caps=CAPS))
        raise


