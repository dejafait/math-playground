"""Step 459: bounded independent forward audit, with archive-safe replay.

The forward arithmetic uses integer coefficient dictionaries and integer letters;
it imports neither the receiver arithmetic nor any correction implementation.
The existing receiver/test driver is invoked separately as a regression replay.
"""
import contextlib
from collections import Counter, deque
import hashlib
import io
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
NOTEBOOK = HERE.parents[1]
OLD = HERE / 'output-457'
OUT = HERE / 'output-459'
LIMITS = dict(records=2_000_000, certificate_bytes=200_000_000,
              polynomial_words=1_000_000, word_length=256,
              multiplication_pairs=100_000_000, stored_words=20_000_000)


def demand(test, message):
    if not test:
        raise AssertionError(message)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def unique(pairs):
    d = {}
    for k, v in pairs:
        demand(k not in d, 'duplicate key')
        d[k] = v
    return d


def read(path):
    return json.loads(path.read_bytes(), object_pairs_hook=unique)


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w') as f:
        json.dump(value, f, separators=(',', ':'))
        f.write('\n')
    demand(path.stat().st_size <= LIMITS['certificate_bytes'], 'audit evidence bytes')


def exact(a, b):
    return json.dumps(a, sort_keys=True) == json.dumps(b, sort_keys=True)


def source_check(folder):
    """Separate syntax/rule/dictionary checks on the fixed caller paths."""
    q = read(folder / 'request.json')
    raw = (folder / 'source.jsonl').read_bytes()
    demand(sha(folder / 'source.jsonl') == q['source_sha256'], 'authorized digest')
    header, *rows = [json.loads(x, object_pairs_hook=unique) for x in raw.splitlines()]
    alphabet = q['alphabet']
    demand(len(set(alphabet)) == len(alphabet), 'original names')
    demand(header == dict(format='literal-four-rule-v1', alphabet=alphabet, goal=q['goal']), 'header')

    def tree(t):
        if type(t) is str:
            demand(t in alphabet or t in ('true', 'false'), 'source atom')
            return
        demand(type(t) is list and ((len(t) == 2 and t[0] == 'not') or
                                   (len(t) == 3 and t[0] == 'or')), 'source tree')
        for a in t[1:]:
            tree(a)

    fs = []
    needed = dict(axiom=0, true=0, expansion=1, contraction=1, association=1, cut=2)
    needed['not-false'] = 0
    for row in rows:
        tag, f, refs = row['rule'], row['f'], row['refs']
        tree(f)
        demand(tag in needed and len(refs) == needed[tag], 'rule arity')
        demand(all(type(j) is int and 0 <= j < len(fs) for j in refs), 'backward references')
        if tag == 'axiom':
            ok = type(f) is list and f[0] == 'or' and f[1] == ['not', f[2]]
        elif tag == 'true':
            ok = f == 'true'
        elif tag == 'not-false':
            ok = f == ['not', 'false']
        elif tag == 'expansion':
            ok = type(f) is list and f[0] == 'or' and f[2] == fs[refs[0]]
        elif tag == 'contraction':
            ok = fs[refs[0]] == ['or', f, f]
        elif tag == 'association':
            p = fs[refs[0]]
            ok = p[0] == 'or' and p[2][0] == 'or' and f == ['or', ['or', p[1], p[2][1]], p[2][2]]
        else:
            p, z = [fs[j] for j in refs]
            ok = p[0] == z[0] == 'or' and z[1] == ['not', p[1]] and f == ['or', p[2], z[2]]
        demand(ok, 'independent literal ' + tag)
        fs.append(f)
    demand(fs and fs[-1] == q['goal'], 'exact endpoint')
    d = q['dictionary']
    demand(d['alphabet'] == alphabet, 'dictionary order')
    expected = {('boolean', (x,)) for x in alphabet}
    expected |= {('commutator', (x, y)) for i, x in enumerate(alphabet) for y in alphabet[i+1:]}
    seen, names, transport = set(), set(), {'1': ['one']}
    transport.update({'x'+str(i+1): ['original', i] for i in range(len(alphabet))})
    for j, p in enumerate(d['placeholders']):
        key = (p['kind'], tuple(p['originals']))
        demand(key in expected and key not in seen and p['name'] not in names, 'dictionary independence')
        seen.add(key)
        names.add(p['name'])
        a = p['originals']
        terms = [[a[0], a[0]], [a[0]]] if key[0] == 'boolean' else [[a[0], a[1]], [a[1], a[0]]]
        demand(p['polynomial'] == terms, 'ordered dictionary words')
        ids = [alphabet.index(x)+1 for x in a]
        token = 'b:'+str(ids[0]) if key[0] == 'boolean' else 't:'+':'.join(map(str, ids))
        transport[token] = ['placeholder', j]
    demand(seen == expected, 'complete dictionary')
    return q, raw, rows, transport


class Forward:
    def __init__(self, request):
        self.q = request
        self.n = len(request['alphabet'])
        self.metrics = dict(multiplication_pairs=0, polynomial_words=0,
                            word_length=0, stored_words=0)

    def reduce(self, counts):
        self.metrics['polynomial_words'] = max(self.metrics['polynomial_words'], len(counts))
        self.metrics['word_length'] = max(self.metrics['word_length'], max(map(len, counts), default=0))
        for k in ('polynomial_words', 'word_length'):
            demand(self.metrics[k] <= LIMITS[k], 'forward scratch cap '+k)
        return {w: 1 for w, c in counts.items() if c % 2}

    def add(self, *ps):
        counts = Counter()
        for p in ps:
            counts.update(p)
        return self.reduce(counts)

    def mul(self, a, b):
        self.metrics['multiplication_pairs'] += len(a)*len(b)
        demand(self.metrics['multiplication_pairs'] <= LIMITS['multiplication_pairs'], 'forward work cap')
        c = Counter()
        for u, x in a.items():
            for v, y in b.items():
                demand(len(u)+len(v) <= LIMITS['word_length'], 'forward concatenation cap')
                c[u+v] += x*y
                demand(len(c) <= LIMITS['polynomial_words'], 'forward counter cap')
        return self.reduce(c)

    def formula(self, t):
        if type(t) is str:
            return {} if t == 'true' else {(): 1} if t == 'false' else {(self.q['alphabet'].index(t),): 1}
        if t[0] == 'not':
            return self.add({(): 1}, self.formula(t[1]))
        return self.mul(self.formula(t[1]), self.formula(t[2]))

    def label(self, label, mode):
        counts = Counter()
        for s in label:
            if s == ['one']:
                counts[()] += 1
            elif s[0] == 'original':
                counts[(s[1],)] += 1
            elif mode == 'free':
                counts[(self.n+s[1],)] += 1
            elif mode == 'axioms':
                for w in self.q['dictionary']['placeholders'][s[1]]['polynomial']:
                    counts[tuple(self.q['alphabet'].index(x) for x in w)] += 1
        return self.reduce(counts)

    def graph(self, nv, edges, source, mode):
        demand(nv+len(edges) <= LIMITS['records'], 'forward graph cap')
        adj, ind = [[] for _ in range(nv)], [0]*nv
        for u, v, label in edges:
            demand(type(u) is int and type(v) is int and 0 <= u < nv and 0 <= v < nv, 'forward endpoints')
            adj[u].append((v, label))
            ind[v] += 1
        queue = deque(i for i in range(nv) if not ind[i])
        table = [{} for _ in range(nv)]
        table[source] = {(): 1}
        visits, storage = 0, 1
        while queue:
            u = queue.popleft()
            visits += 1
            for v, label in adj[u]:
                storage -= len(table[v])
                table[v] = self.add(table[v], self.mul(table[u], self.label(label, mode)))
                storage += len(table[v])
                self.metrics['stored_words'] = max(self.metrics['stored_words'], storage)
                demand(storage <= LIMITS['stored_words'], 'forward storage cap')
                ind[v] -= 1
                if not ind[v]:
                    queue.append(v)
        demand(visits == nv, 'forward cycle')
        return table

    def serial(self, p):
        return [[[('original' if a < self.n else 'placeholder'), a if a < self.n else a-self.n]
                 for a in w] for w in sorted(p, key=lambda w: (len(w), w))]

    def compare(self, p, serialized, message):
        encoded = [tuple(a[1] if a[0] == 'original' else self.n+a[1] for a in w) for w in serialized]
        demand(len(encoded) == len(set(encoded)) and set(encoded) == set(p), message)


def forward_case(folder, name):
    q, raw, rows, transport = source_check(folder)
    c, saved = read(folder/'certificate.json'), read(folder/'reception.json')
    demand(c['source_text'].encode() == raw and exact(c['dictionary'], q['dictionary']), 'retained caller inputs')
    demand(exact(c['symbol_table'], transport), 'independent typed transport')
    f = Forward(q)
    g = c['graph']
    modes = ('free', 'zero', 'axioms')
    tables = {mode: f.graph(g['vertices'], g['edges'], 0, mode) for mode in modes}
    roots, blocks = [], []
    for i, row in enumerate(rows):
        target = f.formula(row['f'])
        demand(not tables['zero'][i+1] and tables['axioms'][i+1] == target, 'independent root identities')
        rec = saved['roots'][i]
        demand(rec['line'] == i and rec['root'] == i+1 and rec['formula'] == row['f'], 'root evidence')
        for mode in modes:
            f.compare(tables[mode][i+1], rec['polynomials'][mode], 'all saved root words')
        f.compare(target, rec['target'], 'saved root target')
        roots.append(dict(line=i, polynomials={m:f.serial(tables[m][i+1]) for m in modes}, target=f.serial(target)))
    for k, b in enumerate(c['blocks']):
        lo, hi = b['vertex_range']
        first, last = b['edge_range']
        edges = [[u-lo, v-lo, lab] for u, v, lab in g['edges'][first:last-2]]
        ps = {m:f.graph(hi-lo, edges, b['entry']-lo, m)[b['exit']-lo] for m in modes}
        vals = [f.formula(a) for a in b['arguments']]
        kind = b['kind']
        if kind == 'zero':
            target = {}
        elif kind == 'translation':
            target = vals[0]
        elif kind == 'boolean':
            target = f.add(f.mul(vals[0], vals[0]), vals[0])
        else:
            x, y = vals[-2:]
            target = f.add(f.mul(x, y), f.mul(y, x))
            if kind == 'prefixed-commutator':
                target = f.mul(f.add({():1}, vals[0]), target)
        demand(ps['axioms'] == target and ps['zero'] == (target if b['role']=='transition' else {}), 'independent block identities')
        if b['role'] == 'transition':
            demand(ps['free'] == target, 'independent original multiplier')
        rec = saved['blocks'][k]
        for m in modes:
            f.compare(ps[m], rec['polynomials'][m], 'all saved block words')
        f.compare(target, rec['target'], 'saved block target')
        blocks.append(dict(block=k, kind=kind, polynomials={m:f.serial(ps[m]) for m in modes}, target=f.serial(target)))
    demand(len(saved['roots']) == len(roots) and len(saved['blocks']) == len(blocks), 'full evidence lengths')
    evidence = dict(roots=roots, blocks=blocks, actual=f.metrics, required=LIMITS, failures=[])
    write(OUT/'independent'/ (name+'.json'), evidence)
    return dict(name=name, roots=len(roots), blocks=len(blocks), actual=f.metrics,
                evidence=str((OUT/'independent'/(name+'.json')).relative_to(NOTEBOOK)))


def main():
    OUT.mkdir(exist_ok=True)
    preserved = [p for n in (449,451,453,455,457) for p in (HERE/f'output-{n}').rglob('*') if p.is_file()]
    before = {str(p.relative_to(NOTEBOOK)):sha(p) for p in sorted(preserved)}
    write(OUT/'archives-before.json', before)
    summary = read(OLD/'summary.json')
    for name, digest in summary['scripts'].items():
        demand(sha(HERE/name) == digest, 'step-457 program hash '+name)
    historical = read(HERE/'output-453/verification.json')['code_sha256']
    dependency_paths = ['scripts/parity-four-rule/checker.py', 'scripts/affine-abp-boolean/check_suffix_graph.py',
                        'scripts/alternative-abp-commutator/check_marked_edges.py']
    for p in dependency_paths:
        demand(sha(NOTEBOOK/p) == historical[p], 'historically pinned dependency '+p)
    current_code = {str((HERE/n).relative_to(NOTEBOOK)):sha(HERE/n) for n in summary['scripts']}
    current_code.update({p:sha(NOTEBOOK/p) for p in dependency_paths})
    current_code[str(Path(__file__).relative_to(NOTEBOOK))] = sha(Path(__file__))
    write(OUT/'code-hashes.json', current_code)
    for manifest in ('archives-before.json', 'archives-after.json'):
        d = read(OLD/manifest)
        demand(len(d) == 176, 'old archive count')
        for p, digest in d.items():
            demand(sha(HERE/p) == digest, 'archived hash '+p)

    # Directly receive original files; complete comparison permits only the known
    # set-order-dependent transient maximum to differ, still below its fixed cap.
    import receive_parameterized as receiver
    results, replays = [], []
    cases = read(OLD/'accepted-cases.json')
    for case in cases:
        folder = OLD/case['name']
        fresh = receiver.receive(folder/'certificate.json',folder/'source.jsonl',folder/'request.json')
        saved = read(folder/'reception.json')
        for value in (fresh, saved):
            demand(value['arithmetic']['max_polynomial_words'] <= LIMITS['polynomial_words'], 'receiver transient cap')
        replays.append(dict(name=case['name'],saved=saved['arithmetic'].copy(),fresh=fresh['arithmetic'].copy()))
        for value in (fresh, saved):
            value['arithmetic'].pop('max_polynomial_words')
        demand(exact(fresh,saved), 'complete retained receiver evidence '+case['name'])
        results.append(forward_case(folder,case['name']))
    write(OUT/'receiver-replays.json', replays)

    # Import performs only mkdir(exist_ok=True) on OLD; replace OUT before main.
    import test_parameterized as driver
    driver.OUT = OUT/'replay'
    driver.OUT.mkdir(exist_ok=True)
    captured = io.StringIO()
    with contextlib.redirect_stdout(captured):
        driver.main()
    (OUT/'replay.log').write_text(captured.getvalue())
    replay = driver.OUT

    def relocate(x):
        if type(x) is str:
            return x.replace(str(replay),str(OLD)).replace('output-459/replay','output-457')
        if type(x) is dict:
            return {k:relocate(v) for k,v in x.items()}
        if type(x) is list:
            return [relocate(v) for v in x]
        return x

    for case in cases:
        for filename in ('certificate.json','source.jsonl','request.json'):
            demand(sha(OLD/case['name']/filename)==sha(replay/case['name']/filename), 'byte-identical rebuilt '+filename)
        demand(exact(read(OLD/case['name']/'construction.json'), relocate(read(replay/case['name']/'construction.json'))), 'complete construction evidence')
    for filename in ('regressions.json','mutation-results.json','archives-before.json','archives-after.json'):
        demand(exact(read(OLD/filename),relocate(read(replay/filename))), 'complete regression evidence '+filename)
    old_cases, new_cases = read(OLD/'accepted-cases.json'), relocate(read(replay/'accepted-cases.json'))
    for group in (old_cases,new_cases):
        for item in group:
            demand(item['arithmetic']['max_polynomial_words'] <= LIMITS['polynomial_words'], 'case transient bound')
            item['arithmetic'].pop('max_polynomial_words')
    demand(exact(old_cases,new_cases), 'entire accepted-case summary')
    old_summary, new_summary = read(OLD/'summary.json'), read(replay/'summary.json')
    for item in (old_summary,new_summary):
        demand(item['actual_max']['max_polynomial_words'] <= LIMITS['polynomial_words'], 'summary transient bound')
        item['actual_max'].pop('max_polynomial_words')
    demand(exact(old_summary,new_summary), 'entire run summary')
    original_mutations = sorted(p for p in (OLD/'mutations').rglob('*') if p.is_file())
    for p in original_mutations:
        q = replay/p.relative_to(OLD)
        if p.name.endswith('-reception.json'):
            a, b = read(p), read(q)
            a['arithmetic'].pop('max_polynomial_words')
            b['arithmetic'].pop('max_polynomial_words')
            demand(exact(a,b), 'neutral complete reception')
        else:
            demand(sha(p) == sha(q), 'complete mutation artifact '+str(p.relative_to(OLD)))
    # Independently evaluate the accepted neutral graph, and the complete
    # algebraic effect of the two substantive internal-placeholder erasures.
    base = OLD/'old-nonzero'
    q = read(base/'request.json')
    original = read(base/'certificate.json')
    defects = []
    for name, block_index in [('nonzero-cut-erased',12),('used-boolean-erased',1)]:
        c = read(OLD/'mutations'/(name+'.json'))
        f = Forward(q)
        original_values = f.graph(original['graph']['vertices'],original['graph']['edges'],0,'axioms')
        altered_values = f.graph(c['graph']['vertices'],c['graph']['edges'],0,'axioms')
        delta = f.add(original_values[c['graph']['sink']],altered_values[c['graph']['sink']])
        demand(delta, 'erasure must change final polynomial')
        defects.append(dict(name=name,block=block_index,original=f.serial(original_values[c['graph']['sink']]),
                            altered=f.serial(altered_values[c['graph']['sink']]),difference=f.serial(delta),actual=f.metrics))
    write(OUT/'erasure-effects.json', defects)
    neutral = read(OLD/'mutations/neutral-label.json')
    f = Forward(q)
    for mode in ('free','zero','axioms'):
        a=f.graph(original['graph']['vertices'],original['graph']['edges'],0,mode)
        b=f.graph(neutral['graph']['vertices'],neutral['graph']['edges'],0,mode)
        demand(all(a[i]==b[i] for i in original['line_roots']), 'neutral all-root polynomials')
    after = {p:sha(NOTEBOOK/p) for p in before}
    demand(before == after,'preserved archives')
    write(OUT/'archives-after.json',after)
    report = dict(accepted=True, cases=results, roots=sum(x['roots'] for x in results),
                  blocks=sum(x['blocks'] for x in results), comparisons=4*sum(x['roots']+x['blocks'] for x in results),
                  regressions=read(replay/'regressions.json'),mutation_cases=len(read(replay/'mutation-results.json')),
                  rejected=sum(not x['accepted'] for x in read(replay/'mutation-results.json')),
                  mutation_files_checked=len(original_mutations),preserved_files=len(before),
                  saved_max=summary['actual_max'],required=summary['required'],
                  independent_max={k:max(x['actual'][k] for x in results) for k in results[0]['actual']},
                  failures=[],scope='Finite verification only; no all-size executable theorem or SAT conclusion.')
    write(OUT/'verification.json',report)
    print(json.dumps({k:report[k] for k in ('accepted','roots','blocks','comparisons','rejected','preserved_files','saved_max','independent_max','failures')}))
    print('Full evidence and actual/required bounds:', OUT/'verification.json')


if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        write(OUT/'failure.json',dict(accepted=False,reason=repr(exc)))
        raise
