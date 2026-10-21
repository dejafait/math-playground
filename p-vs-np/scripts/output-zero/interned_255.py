"""Standalone complete-record interned reception; never constructs coordinates.

IDs have meaning only in Package.syntax. Sharing never merges proof rows.
Literal images are compared field-for-field, not accepted via JSON numeric equality.
"""
import copy
import gc
import gzip
import hashlib
import importlib.util
import json
import pickle
import resource
import sys
import time
from dataclasses import dataclass
from itertools import zip_longest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT/'scripts/left-closure'))
import replay_star as replay
f = replay.f
a = replay.a
MODES = ('native', 'not-or')
SOURCE = ROOT/'scripts/output-zero/output/nonempty-253'
OUT = ROOT/'scripts/output-zero/output/interned-255'


def enc(obj):
    return (json.dumps(obj, separators=(',', ':'), ensure_ascii=True)+'\n').encode('ascii')


class Syntax(f.FastSyntax):
    def __init__(self):
        super().__init__()
        self.text.cache_clear()
        # Expanded strings have only line-local lifetimes. Iteration supports
        # the compiled parser's full declared depth, without Python recursion.
        self.text = self.spelling

    def spelling(self, j, image=False):
        todo = [j]; parts = []
        while todo:
            item = todo.pop()
            if isinstance(item, str):
                parts.append(item); continue
            tag, *args = self.nodes[item]
            if tag == 'v': parts.append(args[0])
            elif tag == 'n': todo.extend([')', args[0], '(~'])
            elif image: todo.extend([')', args[1], ')|', args[0], '((~'])
            else: todo.extend([')', args[1], '>', args[0], '('])
        return ''.join(parts)

    def close(self):
        self.parse.cache_clear()
        f.LIB.parser_free(self.pool); self.pool = None

    def ax_ids(self, rule, subs):
        required = {'A', 'B', 'C'} if rule == 'ax2' else {'A', 'B'}
        assert rule in ('ax1', 'ax2', 'ax3') and set(subs) == required
        A, B = subs['A'], subs['B']
        I = lambda x,y: self.node('i', x,y)
        N = lambda x: self.node('n', x)
        if rule == 'ax1': return I(A,I(B,A))
        if rule == 'ax3': return I(I(N(A),N(B)),I(B,A))
        C = subs['C']
        return I(I(A,I(B,C)),I(I(A,B),I(A,C)))

    def substitute(self, root, env, memo):
        todo = [(root, False)]
        while todo:
            j, done = todo.pop()
            if j in memo: continue
            tag, *args = self.nodes[j]
            if tag == 'v': memo[j] = env.get(args[0], j)
            elif done: memo[j] = self.node(tag, *(memo[x] for x in args))
            else:
                todo.append((j,True)); todo.extend((x,False) for x in args)
        return memo[root]


@dataclass
class Package:
    syntax: Syntax
    goal: int
    rows: list
    paths: tuple
    checked: dict

    def record(self, row, image=False):
        formula, rule, refs, subs = row
        result = dict(f=self.syntax.text(formula,image), rule=rule)
        if rule == 'mp': result['refs'] = list(refs)
        else: result['subs'] = {k:self.syntax.text(v,image) for k,v in subs}
        return result


def check_row(s, rows, row):
    assert isinstance(row,dict)
    rule = row.get('rule')
    if rule == 'mp':
        assert set(row) == {'f','rule','refs'}
        refs = row['refs']
        assert type(refs) is list and len(refs) == 2
        assert all(type(k) is int and 0 <= k < len(rows) for k in refs)
        left, right = [rows[k][0] for k in refs]
        tag, *args = s.nodes[right]
        assert tag == 'i' and args[0] == left, 'MP mismatch'
        formula = args[1]; subs = ()
    else:
        assert set(row) == {'f','rule','subs'} and type(row['subs']) is dict
        subs = tuple((k,s.parse(v)) for k,v in row['subs'].items())
        formula = s.ax_ids(rule,dict(subs)); refs = ()
    assert type(row['f']) is str and row['f'] == s.text(formula), 'native formula'
    return (formula, rule, tuple(refs), subs)


def load(paths, expected):
    s = Syntax(); rows = []
    p = Package(s,s.parse(expected),rows,tuple(str(x.relative_to(ROOT)) for x in paths),{})
    measurements = {}; sums = dict.fromkeys(MODES,0); depths = dict.fromkeys(MODES,0)
    payload = 1; hashes = [hashlib.sha256(),hashlib.sha256()]
    streams = [gzip.open(x,'rb') for x in paths]
    try:
        for m,stream,digest in zip(MODES,streams,hashes):
            raw = stream.readline(); digest.update(raw)
            assert replay.strict_read(raw) == dict(format=m,goal=s.text(p.goal,m=='not-or'))
            off = 2 if m == 'not-or' else 0; st = s.stats[p.goal]
            measurements[m] = dict(path=p.paths[len(measurements)],format=m,accepted=True,
                lines=0,bytes=len(raw),formula_nodes=0,substitution_nodes=0,
                max_line_nodes=0,max_record_nodes=0,max_line_depth=0,
                goal_nodes=st[off],goal_depth=st[off+1])
        for raws in zip_longest(*streams):
            assert all(raw is not None for raw in raws), 'simultaneous EOF'
            retained = check_row(s,rows,replay.strict_read(raws[0])); rows.append(retained)
            # Full every-row reconstruction, including native formula/substitution
            # round trip; image never needs a permissive independent parser.
            fields = [retained[0]]+[v for k,v in retained[3]]
            payload = max(payload,*(s.stats[t][4] for t in fields))
            for m,raw,digest in zip(MODES,raws,hashes):
                image = m == 'not-or'; off = 2 if image else 0
                assert replay.strict_read(raw) == p.record(retained,image), 'complete retained record'
                count = s.stats[fields[0]][off]; depth = s.stats[fields[0]][off+1]
                scount = sum(s.stats[t][off] for t in fields[1:]); info = measurements[m]
                info['lines'] += 1; info['bytes'] += len(raw); digest.update(raw)
                info['formula_nodes'] += count; info['substitution_nodes'] += scount
                info['max_line_nodes'] = max(info['max_line_nodes'],count)
                info['max_record_nodes'] = max(info['max_record_nodes'],count+scount)
                info['max_line_depth'] = max(info['max_line_depth'],depth)
                sums[m] += count+scount
                depths[m] = max(depths[m],*(s.stats[t][off+1] for t in fields))
        assert rows and rows[-1][0] == p.goal, 'actual final endpoint'
        for m,digest in zip(MODES,hashes): measurements[m]['sha256'] = digest.hexdigest()
        p.checked = dict(measurements=measurements,node_sums=sums,depths=depths,name_bytes=payload)
        return p
    except BaseException:
        s.close(); raise
    finally:
        for stream in streams: stream.close()


def compare_archives(p):
    """Compare ALL fields again after retention/reload, with simultaneous EOF."""
    streams = [gzip.open(ROOT/x,'rb') for x in p.paths]
    try:
        for m,stream in zip(MODES,streams):
            assert replay.strict_read(next(stream)) == dict(format=m,goal=p.syntax.text(p.goal,m=='not-or'))
        sentinel = object(); count = 0
        for row,raw0,raw1 in zip_longest(p.rows,*streams,fillvalue=sentinel):
            assert all(x is not sentinel for x in (row,raw0,raw1))
            for raw,image in ((raw0,False),(raw1,True)):
                assert replay.strict_read(raw) == p.record(row,image)
            count += 1
        assert count == len(p.rows)
        return count
    finally:
        for stream in streams: stream.close()


def write_pair(stem, rows, s):
    paths = [OUT/(stem+'.'+m+'.jsonl.gz') for m in MODES]
    p = Package(s,rows[-1][0],rows,(),{})
    for image,path,m in zip((False,True),paths,MODES):
        with gzip.open(path,'wb') as stream:
            stream.write(enc(dict(format=m,goal=s.text(p.goal,image))))
            for row in rows: stream.write(enc(p.record(row,image)))
    return paths


def small_tests():
    s = Syntax(); rows = []
    def ax(rule,subs):
        ids = {k:s.parse(v) for k,v in subs.items()}
        j = s.ax_ids(rule,ids); rows.append((j,rule,(),tuple(ids.items())))
    # Deliberately unused deep record, duplicate occurrences and q/A/B/C.
    ax('ax1',dict(A='(~'*80+'q'+')'*80,B='C'))
    ax('ax1',dict(A='A',B='B')); ax('ax1',dict(A='A',B='B'))
    T = s.text(rows[1][0]); ax('ax1',dict(A=T,B='q'))
    rows.append((s.nodes[rows[3][0]][2],'mp',(1,3),()))
    paths = write_pair('small',rows,s); p = load(paths,s.text(rows[-1][0]))
    assert len(p.rows) == 5 and p.rows[1][0] == p.rows[2][0]
    assert compare_archives(p) == 5
    # Differential oracle is the preexisting append-only tree copier, small only.
    agg = f.h.b.aggregate; primitive = agg.primitive
    trees = agg.load(paths[0],s.text(rows[-1][0]))
    combination = object.__new__(agg.Combination); combination.p = agg.AppendProof()
    combination.p.ax('ax1','offset','padding')
    env_text = dict(A='(B>C)',B='(~A)',C='q',q='(A>B)')
    env_tree = {k:agg.native(agg.checker.parse(v,'native')[0]) for k,v in env_text.items()}
    combination.copy(trees['rows'],env_tree)
    env_ids = {k:p.syntax.parse(v) for k,v in env_text.items()}; memo = {}
    moved = []
    for formula,rule,refs,subs in p.rows:
        moved.append((p.syntax.substitute(formula,env_ids,memo),rule,
            tuple(k+1 for k in refs),tuple((k,p.syntax.substitute(v,env_ids,memo)) for k,v in subs)))
    for row,want in zip(moved,combination.p.rows[1:]):
        wf,wr,wrefs,wsubs,deps = want
        assert p.syntax.text(row[0]) == primitive.text(wf) and row[1] == wr
        assert list(row[2]) == list(wrefs)
        assert {k:p.syntax.text(v) for k,v in row[3]} == {k:primitive.text(v) for k,v in (wsubs or {}).items()}
    # Replay relocated output including its explicit prefix, both full formats.
    offset = p.syntax.ax_ids('ax1',dict(A=p.syntax.parse('offset'),B=p.syntax.parse('padding')))
    relocated = [(offset,'ax1',(),(('A',p.syntax.parse('offset')),('B',p.syntax.parse('padding'))))]+moved
    relocated_paths = write_pair('relocated',relocated,p.syntax)
    cp = load(relocated_paths,p.syntax.text(relocated[-1][0])); assert compare_archives(cp) == 6; cp.syntax.close()
    rejected = []
    # Reuse ALL preserved strict format corruptions (not positive archives).
    for bad in sorted((ROOT/'scripts/left-closure/output').glob('parser-207-strict-*.jsonl.gz')):
        if '-valid.' in bad.name: continue
        base = ROOT/'scripts/left-closure/output/parser-207-strict-valid'
        im = any(x in bad.name for x in ('image_formula','image_substitution','image_bool','image_float'))
        pair = [Path(str(base)+'.native.jsonl.gz'),Path(str(base)+'.not-or.jsonl.gz')]
        pair[int(im)] = bad
        with gzip.open(pair[0] if im else Path(str(base)+'.native.jsonl.gz'),'rb') as stream:
            goal = replay.strict_read(stream.readline())['goal']
        try: z = load(pair,goal)
        except (AssertionError,ValueError,KeyError,TypeError,UnicodeError): rejected.append(bad.name)
        else: z.syntax.close(); raise AssertionError('accepted corruption '+bad.name)
    # Declared parser boundary is explicit; spelling/statistics remain iterative.
    for depth in (4096,4097):
        text = '(~'*depth+'A'+')'*depth
        if depth == 4096:
            j=s.parse(text); assert s.text(j)==text and s.stats[j][1]==depth
        else:
            try: s.parse(text)
            except ValueError as error: assert 'depth resource limit' in str(error)
            else: raise AssertionError('depth boundary not enforced')
    p.syntax.close(); s.close()
    return dict(complete=True,ordered_rows=5,relocated_rows=6,offset=1,
        simultaneous_substitution=env_text,tree_copier_all_fields=True,unused_depth=80,
        rejections=rejected,parser_max_accepted_depth=4096,parser_rejected_depth=4097)


def save(cert):
    cert['worker_peak_rss_bytes'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*(1 if sys.platform=='darwin' else 1024)
    (OUT/'certificate.json').write_text(json.dumps(cert,indent=2)+'\n')


def main():
    start=time.monotonic(); cert=dict(complete=False,stage='small regressions',failures=[],packages=[])
    save(cert); packages=[]; reloaded=[]
    try:
        cert['small']=small_tests(); save(cert)
        spec=importlib.util.spec_from_file_location('interned255_contract',ROOT/'scripts/actual-tree/verify.py')
        verifier=importlib.util.module_from_spec(spec); spec.loader.exec_module(verifier)
        envelope=json.loads((SOURCE/'source-envelope.json').read_text())
        goals=verifier.contract(envelope['source'],envelope['edges'],envelope['request'])
        old=json.loads((SOURCE/'certificate.json').read_text())
        assert len(goals)==6 and len(old['certified_locals'])==6
        for i,goal in enumerate(goals):
            cert['stage']='load local '+str(i); save(cert)
            paths=[SOURCE/f'local-{i}.{m}.jsonl.gz' for m in MODES]
            p=load(paths,goal); packages.append(p)
            assert p.checked == old['certified_locals'][i]['checked'], 'saved expanded statistics'
            assert old['certified_locals'][i]['info']['expected']==goal
            cert['packages'].append(dict(vertex=i,checked=p.checked,unique_nodes=len(p.syntax.nodes),retained_rows=len(p.rows)))
            save(cert); print('PASS retained local',i,'rows',len(p.rows),'unique syntax',len(p.syntax.nodes),flush=True)
        cert['stage']='checkpoint all six'; save(cert)
        snapshots=[dict(nodes=p.syntax.nodes,goal=p.goal,rows=p.rows,paths=p.paths,checked=p.checked) for p in packages]
        checkpoint=OUT/'packages.pkl.gz'
        with gzip.open(checkpoint,'wb',compresslevel=1) as stream: pickle.dump(snapshots,stream,protocol=5)
        del snapshots; gc.collect()
        cert['stage']='reload all six'; save(cert)
        with gzip.open(checkpoint,'rb') as stream:
            snapshots=pickle.load(stream); assert stream.read()==b''
        for p,snapshot in zip(packages,snapshots):
            s=Syntax()
            for i,node in enumerate(snapshot['nodes']): assert s.node(*node)==i
            q=Package(s,snapshot['goal'],snapshot['rows'],snapshot['paths'],snapshot['checked']); reloaded.append(q)
            assert s.nodes==p.syntax.nodes and s.stats==p.syntax.stats
            assert q.goal==p.goal and q.rows==p.rows and q.paths==p.paths and q.checked==p.checked
        assert len(reloaded)==len(snapshots)==6
        del snapshots; gc.collect()
        cert['stage']='full reloaded archive comparison'; save(cert)
        counts=[]
        for q in reloaded:
            counts.append(compare_archives(q))
            print('PASS complete reloaded records',counts[-1],flush=True)
        cert.update(complete=True,stage='complete',all_six_held_together=True,
            checkpoint=dict(path=str(checkpoint.relative_to(ROOT)),bytes=checkpoint.stat().st_size,
                full_pool_row_equality=True,all_record_archive_comparisons=counts),
            source_identity=dict(path=str((SOURCE/'source-envelope.json').relative_to(ROOT)),
                sha256=hashlib.sha256((SOURCE/'source-envelope.json').read_bytes()).hexdigest()),
            qualifications=['Standalone loader only; tuple-consuming downstream copier unchanged.',
                'Compiled parser rejects depth >4096; no all-input memory theorem.',
                'Sampling is not a mathematical hard RSS guarantee; watchdog evidence is separate.'])
    except BaseException as error:
        cert['failures'].append(type(error).__name__+': '+str(error)); raise
    finally:
        cert['elapsed_seconds']=time.monotonic()-start; save(cert)
        for p in packages+reloaded: p.syntax.close()
    print('RESULT complete standalone six-package reception; certificate',str((OUT/'certificate.json').relative_to(ROOT)),flush=True)


if __name__=='__main__': main()
