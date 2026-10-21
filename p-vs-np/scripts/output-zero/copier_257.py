"""Bounded cross-pool reproduction; syntax sharing never merges proof rows.

Only local trusted pickle checkpoints are deserialized. All reconstructed node,
row, provenance and endpoint fields are checked, then compared with archives.
No Closure, coordinate or joined receiver is constructed.
"""
import copy
import gc
import gzip
import hashlib
import importlib.util
import json
import pickle
import re
import resource
import sys
import time
from dataclasses import dataclass
from itertools import zip_longest
import interned_255 as h

ROOT = h.ROOT
OUT = ROOT/'scripts/output-zero/output/copier-257'
GiB = 2**30
MAX_EXPANDED = 128*GiB


def exact(left, right):
    """Internal metadata equality includes types (True != 1 != 1.0 here)."""
    if type(left) is not type(right): return False
    if type(left) is dict:
        return list(left)==list(right) and all(exact(left[k],right[k]) for k in left)
    if type(left) in (tuple,list):
        return len(left)==len(right) and all(exact(x,y) for x,y in zip(left,right))
    return left==right


@dataclass(frozen=True)
class Term:
    syntax: object
    index: int


def term(s, j):
    assert s.pool is not None, 'closed pool'
    assert type(j) is int and 0 <= j < len(s.nodes), 'invalid pool index'
    return Term(s, j)


def owned(value, s):
    assert isinstance(value, Term) and value.syntax is s, 'wrong-pool operand'
    return term(s, value.index).index


class Translation:
    """One-call cache: source, destination and environment cannot change."""
    def __init__(self, source, destination, env):
        self.source, self.destination = source, destination
        assert type(env) is dict
        assert all(type(k) is str and re.fullmatch(r'[A-Za-z0-9_]+', k) for k in env)
        self.env = {k:owned(v, destination) for k,v in env.items()}
        self.memo = {}

    def __call__(self, value):
        root = owned(value, self.source); todo = [(root, False)]
        while todo:
            j, done = todo.pop()
            if j in self.memo: continue
            tag, *args = self.source.nodes[j]
            if tag == 'v':
                # Replacements are destination terms, never visited recursively.
                self.memo[j] = self.env[args[0]] if args[0] in self.env else self.destination.node('v',args[0])
            elif done:
                self.memo[j] = self.destination.node(tag, *(self.memo[x] for x in args))
            else:
                todo.append((j,True)); todo.extend((x,False) for x in args)
        return self.memo[root]


def replay_row(s, rows, row):
    assert type(row) is tuple and len(row) == 4
    formula, rule, refs, subs = row; term(s,formula)
    assert type(refs) is tuple and type(subs) is tuple
    if rule == 'mp':
        assert not subs and len(refs) == 2
        assert all(type(k) is int and 0 <= k < len(rows) for k in refs), 'relocation reference'
        left, right = (rows[k][0] for k in refs)
        assert s.nodes[right] == ('i',left,formula), 'MP conclusion'
    else:
        assert rule in ('ax1','ax2','ax3') and not refs
        assert all(type(pair) is tuple and len(pair) == 2 for pair in subs)
        assert len(dict(subs)) == len(subs), 'duplicate substitution'
        for k,v in subs: assert type(k) is str; term(s,v)
        assert s.ax_ids(rule,dict(subs)) == formula, 'axiom conclusion'


class Store:
    def __init__(self):
        self.syntax = h.Syntax(); self.rows = []; self.locations = []; self.segments = []
        A,B = self.syntax.parse('prefix'),self.syntax.parse('padding')
        row = (self.syntax.ax_ids('ax1',dict(A=A,B=B)), 'ax1', (), (('A',A),('B',B)))
        self.rows.append(row)

    def copy(self, package, env):
        assert package.rows and package.rows[-1][0] == package.goal
        translate = Translation(package.syntax,self.syntax,env)
        offset = len(self.rows); occurrence = len(self.segments)
        # Source MP references are checked against the source prefix, not the
        # destination's otherwise available records.
        source_prefix = []
        for local, row in enumerate(package.rows):
            replay_row(package.syntax,source_prefix,row); source_prefix.append(row)
            formula,rule,refs,subs = row
            moved = (translate(term(package.syntax,formula)),rule,
                tuple(offset+k for k in refs),
                tuple((k,translate(term(package.syntax,v))) for k,v in subs))
            replay_row(self.syntax,self.rows,moved)
            global_row = len(self.rows); self.rows.append(moved)
            self.locations.append((occurrence,package.paths,local,global_row))
        goal = translate(term(package.syntax,package.goal))
        assert self.rows[-1][0] == goal
        self.segments.append(dict(paths=package.paths,start=offset,count=len(package.rows),
            root=len(self.rows)-1,goal=goal,source_goal=package.syntax.text(package.goal),
            substitutions=tuple((k,owned(v,self.syntax)) for k,v in env.items()),checked=package.checked))
        # The translator and its memo have no store lifetime.
        return self.segments[-1]

    def snapshot(self):
        return dict(version=1,nodes=self.syntax.nodes,rows=self.rows,
            locations=self.locations,segments=self.segments)


def pool(nodes):
    assert type(nodes) is list
    s = h.Syntax()
    try:
        for i,node in enumerate(nodes):
            assert type(node) is tuple and node
            tag,*args = node
            if tag == 'v':
                assert len(args)==1 and type(args[0]) is str and re.fullmatch(r'[A-Za-z0-9_]+',args[0])
            else:
                assert tag in ('n','i') and len(args)==(1 if tag=='n' else 2)
                assert all(type(k) is int and 0<=k<i for k in args), 'non-topological syntax'
            assert s.node(*node)==i, 'duplicate/noncanonical syntax'
        return s
    except BaseException:
        s.close(); raise


def restore(snapshot, expected_segments):
    assert set(snapshot)=={'version','nodes','rows','locations','segments'} and type(snapshot['version']) is int and snapshot['version']==1
    assert exact(snapshot['segments'],expected_segments), 'checkpoint segment/provenance mismatch'
    s = pool(snapshot['nodes'])
    try:
        rows=snapshot['rows']; assert type(rows) is list and rows
        prefix=[]
        for row in rows: replay_row(s,prefix,row); prefix.append(row)
        A,B=s.parse('prefix'),s.parse('padding')
        assert rows[0]==(s.ax_ids('ax1',dict(A=A,B=B)),'ax1',(),(('A',A),('B',B))), 'prefix mismatch'
        locations=[]; start=1
        for occurrence,segment in enumerate(expected_segments):
            assert segment['start']==start and segment['count']>0
            assert segment['root']==start+segment['count']-1 < len(rows)
            assert rows[segment['root']][0]==segment['goal'], 'checkpoint endpoint'
            for local in range(segment['count']):
                row=rows[start+local]
                assert all(start<=r<start+local for r in row[2]), 'cross-occurrence relocation'
                locations.append((occurrence,segment['paths'],local,start+local))
            start+=segment['count']
        assert start==len(rows) and exact(locations,snapshot['locations']), 'checkpoint locations'
        out=object.__new__(Store); out.syntax=s; out.rows=rows
        out.locations=snapshot['locations']; out.segments=snapshot['segments']
        return out
    except BaseException:
        s.close(); raise


def compare(store, goals, saved):
    """ALL native/image fields, archive bytes/hashes/stats and source locations."""
    counts=[]; reports=[]; expanded=0
    p=h.Package(store.syntax,store.rows[-1][0],store.rows,(),{})
    location_index=0
    for occurrence,(seg,goal,old) in enumerate(zip(store.segments,goals,saved)):
        assert seg['source_goal']==goal and not seg['substitutions']
        assert seg['paths']==tuple(str((h.SOURCE/f'local-{occurrence}.{m}.jsonl.gz').relative_to(ROOT)) for m in h.MODES)
        assert store.syntax.text(seg['goal'])==goal and store.rows[seg['root']][0]==seg['goal']
        assert seg['checked']==old['checked']
        measurements={}; sums=dict.fromkeys(h.MODES,0); depths=dict.fromkeys(h.MODES,0); payload=1
        streams=[gzip.open(ROOT/x,'rb') for x in seg['paths']]
        hashes=[hashlib.sha256(),hashlib.sha256()]; relocated_bytes=dict.fromkeys(h.MODES,0); ref_delta=dict.fromkeys(h.MODES,0)
        try:
            for m,stream,digest in zip(h.MODES,streams,hashes):
                raw=stream.readline(); digest.update(raw); image=m=='not-or'; off=2 if image else 0
                assert h.replay.strict_read(raw)==dict(format=m,goal=store.syntax.text(seg['goal'],image))
                measurements[m]=dict(path=seg['paths'][len(measurements)],format=m,accepted=True,
                    lines=0,bytes=len(raw),formula_nodes=0,substitution_nodes=0,max_line_nodes=0,
                    max_record_nodes=0,max_line_depth=0,goal_nodes=store.syntax.stats[seg['goal']][off],
                    goal_depth=store.syntax.stats[seg['goal']][off+1])
                assert raw==h.enc(h.replay.strict_read(raw)), 'archive serialization convention'
                relocated_bytes[m]+=len(raw)
            sentinel=object(); row_indices=range(seg['start'],seg['root']+1)
            for local,(global_row,raw0,raw1) in enumerate(zip_longest(row_indices,*streams,fillvalue=sentinel)):
                assert all(x is not sentinel for x in (global_row,raw0,raw1)), 'simultaneous EOF'
                row=store.rows[global_row]; fields=[row[0]]+[v for k,v in row[3]]
                assert store.locations[location_index]==(occurrence,seg['paths'],local,global_row)
                location_index+=1; payload=max(payload,*(store.syntax.stats[t][4] for t in fields))
                for m,raw,digest in zip(h.MODES,(raw0,raw1),hashes):
                    image=m=='not-or'; off=2 if image else 0; source=h.replay.strict_read(raw)
                    output=p.record(row,image); want=copy.deepcopy(source)
                    if row[1]=='mp':
                        assert all(type(r) is int and 0<=r<local for r in source['refs'])
                        want['refs']=[r+seg['start'] for r in source['refs']]
                    else:
                        assert list(source['subs'])==[k for k,v in row[3]], 'substitution order'
                    assert output==want, 'complete relocated record'
                    assert raw==h.enc(source), 'archive serialization convention'
                    delta=sum(len(str(r))-len(str(r-seg['start'])) for r in row[2])
                    out_bytes=len(h.enc(output)); assert out_bytes-len(raw)==delta
                    relocated_bytes[m]+=out_bytes; ref_delta[m]+=delta
                    st=store.syntax.stats; count=st[fields[0]][off]; depth=st[fields[0]][off+1]
                    scount=sum(st[t][off] for t in fields[1:]); info=measurements[m]
                    info['lines']+=1; info['bytes']+=len(raw); digest.update(raw)
                    info['formula_nodes']+=count; info['substitution_nodes']+=scount
                    info['max_line_nodes']=max(info['max_line_nodes'],count)
                    info['max_record_nodes']=max(info['max_record_nodes'],count+scount)
                    info['max_line_depth']=max(info['max_line_depth'],depth)
                    sums[m]+=count+scount; depths[m]=max(depths[m],*(st[t][off+1] for t in fields))
            for m,digest in zip(h.MODES,hashes): measurements[m]['sha256']=digest.hexdigest()
            checked=dict(measurements=measurements,node_sums=sums,depths=depths,name_bytes=payload)
            assert checked==old['checked'], 'complete expanded measurements'
            assert measurements['native']['lines']==seg['count']
            for m in h.MODES: assert relocated_bytes[m]==measurements[m]['bytes']+ref_delta[m]
            counts.append(seg['count']); reports.append(dict(checked=checked,relocated_segment_bytes=relocated_bytes,reference_digit_delta=ref_delta))
            expanded+=sum(relocated_bytes.values()); assert expanded<MAX_EXPANDED
        finally:
            for stream in streams: stream.close()
    assert len(store.segments)==len(goals)==len(saved)==6 and location_index==len(store.locations)
    # One joined header per format, one prefix row, all relocated record lines.
    joined={}
    for m in h.MODES:
        image=m=='not-or'
        joined[m]=len(h.enc(dict(format=m,goal=store.syntax.text(store.rows[-1][0],image))))+len(h.enc(p.record(store.rows[0],image)))
        joined[m]+=sum(r['relocated_segment_bytes'][m]-len(h.enc(dict(format=m,goal=store.syntax.text(seg['goal'],image)))) for r,seg in zip(reports,store.segments))
    return dict(counts=counts,packages=reports,joined_stream_bytes=joined,joined_rows_per_format=len(store.rows),all_fields=True)


def small_tests():
    h.OUT=OUT
    reused=h.small_tests()
    regspec=importlib.util.spec_from_file_location('reg257',ROOT/'scripts/output-zero/regression_interned_255.py')
    reg=importlib.util.module_from_spec(regspec); regspec.loader.exec_module(reg); reg.main()
    agg=h.f.h.b.aggregate; primitive=agg.primitive
    packages=[]; trees=[]
    for number in range(2):
        s=h.Syntax()
        for text in (('q','A','B','C') if number==0 else ('C','B','A','q')): s.parse(text)
        rows=[]
        for env in (dict(A='(~'*120+'q'+')'*120,B='C'),dict(A='A',B='B'),dict(A='A',B='B')):
            ids={k:s.parse(v) for k,v in env.items()}; rows.append((s.ax_ids('ax1',ids),'ax1',(),tuple(ids.items())))
        ids=dict(A=rows[1][0],B=s.parse('q')); rows.append((s.ax_ids('ax1',ids),'ax1',(),tuple(ids.items())))
        rows.append((s.nodes[rows[3][0]][2],'mp',(1,3),()))
        paths=h.write_pair('cross'+str(number),rows,s)
        packages.append(h.Package(s,rows[-1][0],rows,tuple(str(x.relative_to(ROOT)) for x in paths),{}))
        trees.append(agg.load(paths[0],s.text(rows[-1][0])))
    assert packages[0].syntax.nodes[0]!=packages[1].syntax.nodes[0], 'required conflicting IDs'
    store=Store(); cases=[]
    envs=[{},dict(A='(B>C)',B='(~A)',C='q',q='(A>B)'),dict(A='q',B='C',C='A',q='B'),
        dict(A='(B>C)',B='(~A)',C='q',q='(A>B)')]
    try:
        for env in envs:
            for number,p in enumerate(packages):
                oracle=object.__new__(agg.Combination); oracle.p=agg.AppendProof()
                # Exact nonzero offset without materializing production input.
                for _ in store.rows: oracle.p.ax('ax1','prefix','padding')
                env_tree={k:agg.native(agg.checker.parse(v,'native')[0]) for k,v in env.items()}
                oracle.copy(trees[number]['rows'],env_tree)
                start=len(store.rows); seg=store.copy(p,{k:term(store.syntax,store.syntax.parse(v)) for k,v in env.items()})
                for actual,want in zip(store.rows[start:],oracle.p.rows[start:]):
                    wf,wr,wrefs,wsubs,deps=want
                    assert store.syntax.text(actual[0])==primitive.text(wf) and actual[1]==wr
                    assert list(actual[2])==list(wrefs) and not deps
                    assert {k:store.syntax.text(v) for k,v in actual[3]}=={k:primitive.text(v) for k,v in (wsubs or {}).items()}
                assert len(store.rows)-start==5 and store.rows[start+1][0]==store.rows[start+2][0]
                cases.append(dict(source_pool=number,start=start,count=5,environment=env))
        rejections=[]
        def reject(name,fn):
            try: value=fn()
            except (AssertionError,ValueError,TypeError,KeyError,IndexError): rejections.append(name)
            else:
                if isinstance(value,Store): value.syntax.close()
                raise AssertionError('accepted '+name)
        reject('wrong-pool-replacement',lambda:store.copy(packages[0],{'A':term(packages[0].syntax,0)}))
        reject('bare-id-replacement',lambda:store.copy(packages[0],{'A':0}))
        t=Translation(packages[0].syntax,store.syntax,{})
        reject('wrong-pool-source',lambda:t(term(packages[1].syntax,0)))
        reject('boolean-index',lambda:term(store.syntax,True))
        snap=store.snapshot(); expected=copy.deepcopy(store.segments)
        mutations={
            'offset':lambda z:z['segments'][0].__setitem__('start',0),
            'path':lambda z:z['segments'][0].__setitem__('paths',('wrong',)),
            'goal':lambda z:z['segments'][0].__setitem__('goal',0),
            'location':lambda z:z['locations'].__setitem__(0,(0,('wrong',),0,1)),
            'missing-row':lambda z:z['rows'].pop(),
            'forward-reference':lambda z:z['rows'].__setitem__(5,(z['rows'][5][0],'mp',(5,4),())),
            'cross-occurrence-reference':lambda z:z['rows'].__setitem__(5,(z['rows'][5][0],'mp',(0,4),())),
            'non-topological-node':lambda z:z['nodes'].__setitem__(0,('n',0)),
            'boolean-version':lambda z:z.__setitem__('version',True)}
        for name,mutate in mutations.items():
            z=copy.deepcopy(snap); mutate(z); reject(name,lambda z=z:restore(z,expected))
        # Full two-format serialization/reception of the complete bounded store.
        paths=h.write_pair('cross-joined',store.rows,store.syntax)
        q=h.load(paths,store.syntax.text(store.rows[-1][0])); assert h.compare_archives(q)==41; q.syntax.close()
        q=restore(copy.deepcopy(snap),expected)
        assert exact(q.syntax.nodes,store.syntax.nodes) and exact(q.syntax.stats,store.syntax.stats) and exact(q.snapshot(),snap)
        q.syntax.close()
        return dict(complete=True,cases=cases,all_tree_copier_fields=True,unused_native_depth=120,
            conflicting_ids=True,complete_two_format_rows=41,rejections=rejections,reused=reused,
            step253_rejections=json.loads((OUT/'supplement.json').read_text()))
    finally:
        store.syntax.close()
        for p in packages: p.syntax.close()


def save(cert):
    cert['worker_peak_rss_bytes']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*(1 if sys.platform=='darwin' else 1024)
    (OUT/'certificate.json').write_text(json.dumps(cert,indent=2)+'\n')


def main():
    started=time.monotonic(); cert=dict(complete=False,stage='small tests',failures=[])
    save(cert); packages=[]; store=None; reloaded=None
    try:
        cert['small']=small_tests(); save(cert)
        spec=importlib.util.spec_from_file_location('contract257',ROOT/'scripts/actual-tree/verify.py')
        v=importlib.util.module_from_spec(spec); spec.loader.exec_module(v)
        envelope=json.loads((h.SOURCE/'source-envelope.json').read_text())
        goals=v.contract(envelope['source'],envelope['edges'],envelope['request'])
        old=json.loads((h.SOURCE/'certificate.json').read_text())['certified_locals']
        cert['stage']='restore source pools'; save(cert)
        with gzip.open(h.OUT.parent/'interned-255/packages.pkl.gz','rb') as stream:
            snapshots=pickle.load(stream); assert stream.read()==b''
        assert len(snapshots)==len(goals)==len(old)==6
        for i,(snap,goal) in enumerate(zip(snapshots,goals)):
            s=pool(snap['nodes']); p=h.Package(s,snap['goal'],snap['rows'],snap['paths'],snap['checked'])
            packages.append(p)
            assert s.text(p.goal)==goal and old[i]['info']['expected']==goal and p.checked==old[i]['checked']
        del snapshots; gc.collect()
        cert['stage']='cross-pool full copying'; save(cert); store=Store()
        for i,p in enumerate(packages):
            seg=store.copy(p,{})
            cert['last_copied']=dict(occurrence=i,start=seg['start'],root=seg['root'],rows=seg['count']); save(cert)
            print('PASS copied pool',i,'offset',seg['start'],'rows',seg['count'],flush=True)
        cert['stage']='all original archive fields'; save(cert)
        cert['before_checkpoint']=compare(store,goals,old); save(cert)
        cert['stage']='checkpoint'; save(cert)
        path=OUT/'joined.pkl.gz'; assert not path.exists()
        with gzip.open(path,'wb',compresslevel=1) as stream: pickle.dump(store.snapshot(),stream,protocol=5)
        cert['stage']='reload and primitive replay'; save(cert)
        with gzip.open(path,'rb') as stream:
            snapshot=pickle.load(stream); assert stream.read()==b''
        reloaded=restore(snapshot,store.segments)
        assert exact(reloaded.snapshot(),store.snapshot()) and exact(reloaded.syntax.stats,store.syntax.stats)
        cert['checkpoint']=dict(path=str(path.relative_to(ROOT)),full_nodes_rows_provenance_equality=True,primitive_replay_rows=len(reloaded.rows))
        del snapshot; gc.collect()
        cert['stage']='all reloaded archive fields'; save(cert)
        cert['after_checkpoint']=compare(reloaded,goals,old)
        assert cert['before_checkpoint']==cert['after_checkpoint']
        cert['source_envelope_sha256']=hashlib.sha256((h.SOURCE/'source-envelope.json').read_bytes()).hexdigest()
        cert.update(complete=True,stage='complete',all_six_held_together=True,
            destination_unique_nodes=len(store.syntax.nodes),locations=len(store.locations),
            segments=store.segments,qualifications=['Trusted internal pickle, not an external input format.',
                'Parser depth limit 4096; no Closure, coordinates or joined receiver.',
                'Observed peak/heartbeat evidence is not a continuous hard-cap theorem.'])
    except BaseException as error:
        cert['failures'].append(type(error).__name__+': '+str(error)); raise
    finally:
        cert['elapsed_seconds']=time.monotonic()-started; save(cert)
        for p in packages: p.syntax.close()
        if store: store.syntax.close()
        if reloaded: reloaded.syntax.close()
    print('RESULT complete cross-pool copier; rows',len(store.rows),'certificate',str((OUT/'certificate.json').relative_to(ROOT)),flush=True)


if __name__=='__main__': main()
