"""Step 451: complete finite audit, preserving output-449; no all-size claim."""
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
OLD, OUT = HERE/'output-449', HERE/'output-451'
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
    files = sorted(p for p in OLD.rglob('*') if p.is_file())
    before = {str(p.relative_to(NOTEBOOK)): digest(p) for p in files}
    cert, saved, mutations = (read(OLD/n) for n in
                              ('certificate.json','reception.json','mutation-results.json'))
    raw = (OLD/'source.jsonl').read_bytes()
    demand(hashlib.sha256(raw).hexdigest() ==
           '9265d9b95dac5d2c1dcb549722b412454380b21b11d7d116e93cde479b558d7c', 'source SHA')
    header, *records = [json.loads(s, object_pairs_hook=strict_pairs) for s in raw.splitlines()]
    demand(len(records) == 9 and header['alphabet'] == ['A','B'], 'source framing')
    r = module('audited_receiver', HERE/'receive.py')
    result = r.receive(OLD/'certificate.json', OLD/'source.jsonl')
    demand(typed({k:v for k,v in result.items() if k != 'arithmetic'}) ==
           typed({k:v for k,v in saved.items() if k != 'arithmetic'}), 'complete saved reception mismatch')
    counters(result['arithmetic'], saved['arithmetic'])
    write('replayed-reception.json', result)

    # Rebuild the exact fixture in a separate directory, checking every graph
    # record and the constructor counters byte for byte against the saved file.
    emitter = module('audited_emitter', HERE/'emit.py')
    emitter.OUT = OUT/'rebuilt'
    log = io.StringIO()
    with contextlib.redirect_stdout(log):
        emitter.main()
    demand((emitter.OUT/'certificate.json').read_bytes() == (OLD/'certificate.json').read_bytes(),
           'emitter complete certificate reproduction')
    demand((emitter.OUT/'source.jsonl').read_bytes() == raw, 'emitter source reproduction')
    write('rebuild.json', dict(byte_identical=True, construction=cert['construction'],
                              certificate_sha256=digest(OLD/'certificate.json')))

    g = cert['graph']
    values = {m: forward(g['vertices'], g['edges'], g['source'], m) for m in MODES}
    root_results, block_results = [], []
    for i, record in enumerate(records):
        item = dict(line=i, root=i+1, formula=record['f'],
                    polynomials={m:serial(values[m][i+1]) for m in MODES}, target=serial(tr(record['f'])))
        demand(typed(item) == typed(saved['roots'][i]), 'independent root '+str(i))
        root_results.append(item)
    for k, b in enumerate(cert['blocks']):
        lo, hi = b['vertex_range']
        first, last = b['edge_range']
        edges = [[u-lo,v-lo,lab] for u,v,lab in g['edges'][first:last-2]]
        polynomials = {m:serial(forward(hi-lo,edges,b['entry']-lo,m)[b['exit']-lo]) for m in MODES}
        args = [tr(t) for t in b['arguments']]
        if b['kind'] == 'zero':
            target = {}
        elif b['kind'] == 'translation':
            target = args[0]
        elif b['kind'] == 'boolean':
            target = add(mul(args[0],args[0]),args[0])
        else:
            target = add(mul(args[-2],args[-1]),mul(args[-1],args[-2]))
            if b['kind'] == 'prefixed-commutator':
                target = mul(add({():1},args[0]),target)
        item = dict(block=k,line=b['line'],role=b['role'],kind=b['kind'],
                    polynomials=polynomials,target=serial(target))
        demand(typed(item) == typed(saved['blocks'][k]), 'independent block '+str(k))
        block_results.append(item)
    write('independent-polynomials.json', dict(roots=root_results, blocks=block_results,
                                             arithmetic=stats.copy(), caps=CAPS))

    replay = []
    for case in mutations['certificate_tests']:
        p, sp = (NOTEBOOK/case[k] for k in ('certificate_path','source_path'))
        data = read(p)
        try:
            r.receive(p,sp)
            accepted, reason = True, 'both identities and full reception still hold'
        except (r.Rejected,r.checker.Invalid,ValueError,TypeError,KeyError) as e:
            accepted, reason = False,str(e)
        demand(accepted == case['accepted'] == case['expected_accept'] and reason == case['reason'],
               'mutation replay '+case['case'])
        replay.append(dict(case=case['case'],accepted=accepted,reason=reason,
                           changes=changed(cert,data),source_text=sp.read_text(),
                           certificate_sha256=digest(p),source_sha256=digest(sp)))
    source_tests = []
    for case in mutations['source_tests']:
        p = NOTEBOOK/case['path']
        try:
            r.checker.check(p,r.GOAL)
            rejected, reason = False,'accepted'
        except r.checker.Invalid as e:
            rejected, reason = True,str(e)
        demand(rejected and reason == case['reason'], 'source rejection '+str(p))
        source_tests.append(dict(path=case['path'],rejected=rejected,reason=reason,
                                 source_text=p.read_text(),sha256=digest(p)))
    bad = read(OLD/'mutations/unused-B-seed-damage.json')['graph']
    damaged = {m:forward(bad['vertices'],bad['edges'],0,m) for m in ('zero','axioms')}
    probes = []
    for i in (3,8):
        z, s, t = damaged['zero'][i+1],damaged['axioms'][i+1],tr(records[i]['f'])
        probes.append(dict(line=i,zero=serial(z),substituted=serial(s),target=serial(t),
                           both_identities=not z and s == t))
    demand(typed(probes) == typed(mutations['unused_branch_discriminator']), 'unused branch probe')
    demand(len(replay) == 23 and len(source_tests) == 20, 'complete case counts')
    demand(typed(mutations['summary']) == typed(dict(certificate_cases=23,expected_rejections=22,
           neutral_acceptances=1,source_rejections=20,failures=[])), 'saved mutation summary')
    backward = r.Arithmetic()
    order = r.topo(bad['vertices'],bad['edges'])
    for i in (3,8):
        for mode in ('zero','axioms'):
            backward.evaluate(bad['vertices'],bad['edges'],order,0,i+1,mode)
        backward.translation(records[i]['f'])
    counters(backward.counts, mutations['discriminator_arithmetic'])
    write('mutation-replay.json',dict(certificate_tests=replay,source_tests=source_tests,
                                     unused_branch_discriminator=probes,
                                     discriminator_arithmetic=backward.counts,
                                     saved_discriminator_arithmetic=mutations['discriminator_arithmetic'],
                                     transient_word_count_hash_dependent=True))

    # The preserved pre-repair receiver is executed with its original __file__
    # so relative source-checker imports remain exactly the same.
    ns = dict(__file__=str(HERE/'receive.py'),__name__='preserved_receiver')
    exec(compile((OUT/'receiver-before.py').read_text(),str(OUT/'receiver-before.py'),'exec'),ns)
    type_tests = []
    changes = [('acceptance-integer', lambda d:d['source_check'].__setitem__('accepted',1)),
               ('count-boolean',lambda d:d['source_check']['rule_counts'].__setitem__('true',True)),
               ('count-float',lambda d:d['source_check'].__setitem__('records',9.0))]
    for name, mutate in changes:
        d = copy.deepcopy(cert)
        mutate(d)
        p = OUT/(name+'.json')
        p.write_text(typed(d)+'\n')
        old = ns['receive'](p,OLD/'source.jsonl')
        demand(old['accepted'], 'before-repair reproduction')
        try:
            r.receive(p,OLD/'source.jsonl')
            rejected, reason = False,'accepted'
        except r.Rejected as e:
            rejected, reason = True,str(e)
        demand(rejected and reason == 'source checker evidence','typed evidence repair')
        type_tests.append(dict(case=name,changes=changed(cert,d),accepted_before=True,
                               rejected_after=rejected,reason=reason,certificate_path=str(p.relative_to(NOTEBOOK))))
    p = OUT/'duplicate-key.json'
    p.write_text((OLD/'certificate.json').read_text().replace('{','{"format":"duplicate",',1))
    try:
        r.receive(p,OLD/'source.jsonl')
        demand(False,'duplicate key accepted')
    except r.Rejected as e:
        demand(str(e) == 'duplicate JSON key: format','duplicate-key reason')
    write('strict-evidence-repair.json',dict(type_tests=type_tests,duplicate_key_rejected=True,
                                            graph_identities_affected=False))
    after = {str(p.relative_to(NOTEBOOK)): digest(p) for p in files}
    demand(before == after, 'preserved output-449 modified')
    report = dict(accepted=True,failures=[],preserved_files=before,
                  code_sha256={str(p.relative_to(NOTEBOOK)):digest(p) for p in
                               (HERE/'emit.py',HERE/'receive.py',HERE/'mutations.py',Path(__file__),
                                HERE.parent/'parity-four-rule/checker.py',
                                HERE.parent/'affine-abp-boolean/check_suffix_graph.py',
                                HERE.parent/'alternative-abp-commutator/check_marked_edges.py')},
                  roots=9,blocks=15,expected_rejections=22,source_rejections=20,
                  neutral_acceptances=1,type_repairs=3,duplicate_key_rejections=1,
                  bounds=result['bounds'],receiver_arithmetic=result['arithmetic'],
                  forward_audit_arithmetic=stats,caps=CAPS,
                  limitations=['zero cut seed','unused sigma:B','finite word expansion only'])
    write('audit.json',report)
    print(json.dumps({k:report[k] for k in ('accepted','roots','blocks','expected_rejections',
                     'source_rejections','neutral_acceptances','type_repairs','bounds','failures')}))
    print('Arithmetic actual/required:',json.dumps(dict(receiver=result['arithmetic'],forward=stats,caps=CAPS)))
    print('Complete audit evidence:',OUT)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        write('audit-failure.json',dict(failure=repr(e),arithmetic=stats,caps=CAPS))
        raise
