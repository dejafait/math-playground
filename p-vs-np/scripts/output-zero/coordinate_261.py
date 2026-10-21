"""One capped, pool-aware reproduction of the existing L065 vertex-0 plan.

No new rewrite or inference rule. Trusted local checkpoints only. Partial
checkpoints and exact byte counts are explicitly not complete proof packages.
"""
import copy
import gc
import gzip
import hashlib
import importlib.util
import json
import pickle
import platform
import resource
import sys
import time
from pathlib import Path
import copier_257 as c

h=c.h
ROOT=h.ROOT
OUT=ROOT/'scripts/output-zero/output/coordinate-261'
CAP=dict(rss=2**31,rss_stop=3*2**29,seconds=600,artifacts=16*2**30,expanded=128*2**30)

def module(name,path):
    spec=importlib.util.spec_from_file_location(name,ROOT/path)
    obj=importlib.util.module_from_spec(spec); spec.loader.exec_module(obj); return obj

# A separate module keeps the legacy tuple implementation available as a small
# differential oracle. Only syntax operations are adapted in this copy.
b=module('coordinate261_plan','scripts/backward-zero/build.py')
lc=h.f.h.lc

class Stop(Exception): pass

class ByteCount:
    """Exact ASCII/JSON field lengths; no formula string expansion."""
    def __init__(self,s): self.s=s; self.lengths=[]
    def sync(self):
        for node in self.s.nodes[len(self.lengths):]:
            tag,*args=node
            if tag=='v': value=(len(args[0]),len(args[0]))
            elif tag=='n': value=tuple(3+self.lengths[args[0]][m] for m in (0,1))
            else: value=tuple((3 if m==0 else 6)+sum(self.lengths[x][m] for x in args) for m in (0,1))
            self.lengths.append(value)
    def row(self,row,image):
        self.sync(); f,rule,refs,subs=row
        shell=dict(f='',rule=rule)
        if rule=='mp': shell['refs']=list(refs)
        else: shell['subs']={k:'' for k,v in subs}
        return len(h.enc(shell))+sum(self.lengths[j][int(image)] for j in [f]+[v for k,v in subs])

class CountRows(list):
    def __init__(self,s,header):
        super().__init__(); self.counter=ByteCount(s)
        self.bytes=list(header); self.max_row_bytes=[0,0]
    def append(self,row):
        sizes=[self.counter.row(row,m) for m in (False,True)]
        prospective=[a+b for a,b in zip(self.bytes,sizes)]
        if sum(prospective)>CAP['expanded']:
            raise Stop('complete two-format prefix would exceed expanded output cap: '+str(prospective))
        # The unchanged full-field receiver allocates one whole line. Refuse a
        # workspace whose conservative twelve simultaneous line buffers alone
        # exhaust the RSS stop threshold, before allocating any expanded text.
        if 12*max(sizes)>=CAP['rss_stop']:
            raise Stop('single-record full-field workspace admission: '+str(sizes))
        super().append(row); self.bytes=prospective
        self.max_row_bytes=[max(a,z) for a,z in zip(self.max_row_bytes,sizes)]

class Ops:
    def __init__(self,s): self.s=s
    def N(self,a): return c.term(self.s,self.s.node('n',c.owned(a,self.s)))
    def I(self,a,z): return c.term(self.s,self.s.node('i',c.owned(a,self.s),c.owned(z,self.s)))
    def X(self,a,z): return self.I(self.I(a,z),self.N(self.I(z,a)))
    def E(self,a,z): return self.N(self.X(a,z))
    def P(self,a,z): return self.N(self.I(a,self.N(z)))
    def text(self,t): return self.s.text(c.owned(t,self.s))

class RowsView:
    def __init__(self,store): self.store=store
    def __len__(self): return len(self.store.rows)
    def __getitem__(self,j):
        row=self.store.rows[j]
        return (c.term(self.store.syntax,row[0]),)+row[1:]

class Primitive:
    def __init__(self,store): self.store=store; self.rows=RowsView(store)
    def mp(self,a,z):
        rows=self.store.rows; s=self.store.syntax
        assert type(a) is int and type(z) is int and 0<=a<len(rows) and 0<=z<len(rows)
        node=s.nodes[rows[z][0]]
        assert node[0]=='i' and node[1]==rows[a][0], 'generated MP antecedent'
        row=(node[2],'mp',(a,z),()); c.replay_row(s,rows,row); rows.append(row)
        return len(rows)-1

class Compiler(b.Store):
    def __init__(self,store,library,q):
        self.store=store; self.p=Primitive(store); self.library=library; self.q=q
        self.calls=[]; self.max_argument_height=0; self.law_cache={}
        self.traces=[]; self.coordinate_roots=[]
        self.ops=Ops(store.syntax)
        b.p=self.ops; b.P=self.ops.P
        def native(t):
            if t[0]=='a':
                c.owned(t[2],store.syntax); return t[2]
            return (self.ops.X if t[0]=='x' else self.ops.P)(native(t[1]),native(t[2]))
        b.nt=native
    def law(self,name,env):
        self.max_argument_height=max(self.max_argument_height,max([b.height(t) for t in env.values()]+[0]))
        return self.use(name,{k:b.nt(v) for k,v in env.items()})
    def use(self,name,env):
        env=dict(env); env.setdefault('q',c.term(self.store.syntax,self.store.syntax.parse(self.q)))
        key=(name,tuple(sorted((k,c.owned(v,self.store.syntax)) for k,v in env.items())))
        if key in self.law_cache: return self.law_cache[key]
        package=self.library[name]; translate=c.Translation(package.syntax,self.store.syntax,env)
        begin=len(self.store.rows)
        for formula,rule,refs,subs in package.rows:
            row=(translate(c.term(package.syntax,formula)),rule,tuple(begin+r for r in refs),
                tuple((k,translate(c.term(package.syntax,v))) for k,v in subs))
            c.replay_row(self.store.syntax,self.store.rows,row); self.store.rows.append(row)
        j=len(self.store.rows)-1
        assert self.store.rows[j][0]==translate(c.term(package.syntax,package.goal))
        self.calls.append(dict(name=name,start=begin,root=j,env=key[1]))
        self.law_cache[key]=j; return j
    def row(self,d,roots):
        tables=lc.ep.request(d); op=self.ops; s=self.store.syntax
        parse=lambda t:c.term(s,s.parse(t))
        y=b.atom((0,),op.I(parse(d['q']),parse(d['q'])))
        z=b.atom((9,),op.N(y[2]))
        S=[b.atom((1,w),parse(text)) for w,text in enumerate(d['suffixes'])]
        xs=[b.atom((3,j),parse(text)) for j,text in enumerate(d['letters'])]
        rhs=[b.X(y if w==d['t'] else z,b.X(b.W(d['E0'][w],S,z),
             b.Bal([b.product(xs[j],b.W(d['Eb'][j][w],S,z)) for j in range(d['n'])],z))) for w in range(d['N'])]
        selected=[w for w,bit in enumerate(tables['K'][0]) if bit]
        a,r,proof=b.combine(self,[S[w] for w in selected],[rhs[w] for w in selected],[roots[w] for w in selected],z)
        closed=b.X(y if tables['beta'][0][0] else z,b.Bal([
            b.product(xs[j],b.W(tables['G'][j][0],S,z)) for j in range(d['n'])],z))
        target=b.X(a,b.X(S[0],closed)); comparison,traces=b.compare(self,r,target,z)
        premise=self.trans(a,r,target,proof,comparison)
        self.root=self.p.mp(premise,self.law('close_cancel',dict(A=a,B=S[0],C=closed)))
        expected=lc.ep.e.c.serialize(tables['closed'][0])
        assert s.text(self.store.rows[self.root][0])==expected
        assert self.root==len(self.store.rows)-1
        self.traces=traces; return self.root

def library():
    result={}
    for name,goal in dict(lc.b.ep.fixed(),close_cancel=lc.ep.cancellation()).items():
        folder=('left-closure' if name=='close_cancel' else 'backward-zero' if name in ('zeroR','zeroL','prod_zero')
                else 'balanced-distribution' if name in ('dist','prod_cong') else 'balanced-slot')
        paths=[ROOT/f'scripts/{folder}/output/{name}.{mode}.jsonl.gz' for mode in h.MODES]
        result[name]=h.load(paths,lc.ep.e.c.serialize(goal))
    assert len(result)==15
    return result

def small_tests(lib):
    """Complete fixed-field counting, owned syntax, and tuple-plan differential."""
    tests=[]
    for name,pkg in lib.items():
        counter=ByteCount(pkg.syntax)
        for row in pkg.rows:
            for image in (False,True): assert counter.row(row,image)==len(h.enc(pkg.record(row,image)))
        tests.append(dict(law=name,rows=len(pkg.rows),all_fields_both_formats=True))
    legacy=lc.b
    oldlib={name:legacy.aggregate.load(ROOT/pkg.paths[0],pkg.syntax.text(pkg.goal)) for name,pkg in lib.items()}
    # More than one positional tag may deliberately have equal syntax.
    differentials=[]; rejections=[]
    for q in ('q','x'):
        st=c.Store(); st.rows=CountRows(st.syntax,[0,0]); compiler=Compiler(st,lib,q)
        old=legacy.Store(oldlib,q); op=compiler.ops; s=st.syntax
        P=lambda text:c.term(s,s.parse(text))
        z=b.atom((9,),op.N(op.I(P(q),P(q))))
        oz=legacy.atom((9,),legacy.p.N(legacy.p.I(q,q)))
        atoms=[b.atom((1,j),P('A')) for j in range(2)]
        oats=[legacy.atom((1,j),'A') for j in range(2)]
        tree=b.X(b.X(atoms[1],z),b.X(atoms[0],atoms[1]))
        otree=legacy.X(legacy.X(oats[1],oz),legacy.X(oats[0],oats[1]))
        new,root,_=b.normalize(compiler,tree,z); oldnew,oldroot,_=legacy.normalize(old,otree,oz)
        assert op.text(b.nt(new))==legacy.p.text(legacy.nt(oldnew))
        assert len(st.rows)==len(old.p.rows)
        pp=h.Package(s,st.rows[-1][0],st.rows,(),{})
        for i,(f,rule,refs,subs,deps) in enumerate(old.p.rows):
            assert not deps
            for image in (False,True):
                want=dict(f=legacy.p.text(f,image),rule=rule)
                if rule=='mp': want['refs']=list(refs)
                else: want['subs']={k:legacy.p.text(v,image) for k,v in subs.items()}
                assert pp.record(st.rows[i],image)==want
        assert op.text(compiler.p.rows[root][0])==legacy.p.text(old.p.rows[oldroot][0])
        differentials.append(dict(q=q,rows=len(st.rows),all_fields_both_formats=True))
        other=h.Syntax()
        try:
            for label,call in [('wrong-pool',lambda:op.N(c.term(other,other.parse('A')))),
                ('bare-index',lambda:op.N(0)),('boolean-index',lambda:c.term(s,True))]:
                try: call()
                except AssertionError as error: rejections.append(dict(case=q+'-'+label,error=str(error)))
                else: raise AssertionError('accepted '+label)
        finally: other.close(); s.close()
    # Reuse the audited simultaneous-substitution boundary, now on a library
    # formula, with conflicting source/destination IDs and schematic collisions.
    st=c.Store(); s=st.syntax; src=lib['refl']; env={k:c.term(s,s.parse(v)) for k,v in dict(A='(B>C)',B='(~A)',C='q',q='x').items()}
    trans=c.Translation(src.syntax,s,env)
    tree=legacy.aggregate.native(legacy.checker.parse(src.syntax.text(src.goal),'native')[0])
    tenv={k:legacy.aggregate.native(legacy.checker.parse(s.text(v.index),'native')[0]) for k,v in env.items()}
    assert s.text(trans(c.term(src.syntax,src.goal)))==legacy.p.text(legacy.p.sub(tree,tenv))
    s.close()
    return dict(complete=True,counted_fixed_fields=tests,normalizer_differentials=differentials,
                rejections=rejections,simultaneous_substitution=True)

def checkpoint(path,store,compiler=None):
    assert not path.exists()
    extra={} if compiler is None else dict(calls=compiler.calls,traces=compiler.traces,
        max_argument_height=compiler.max_argument_height,law_cache=list(compiler.law_cache.items()))
    snapshot=store.snapshot()
    # Serialize plain rows, never the live counting adapter or its owned pool.
    snapshot['rows']=list(store.rows)
    with gzip.open(path,'wb',compresslevel=1) as stream:
        pickle.dump(dict(store=snapshot,adapter=extra),stream,protocol=5)

def write_pair(store,expected,counts):
    paths=[]; writers={}; pkg=h.Package(store.syntax,store.rows[-1][0],store.rows,(),{})
    assert store.syntax.text(pkg.goal)==expected
    for m,image in zip(h.MODES,(False,True)):
        path=OUT/f'coordinate-0.{m}.jsonl.gz'; assert not path.exists(); paths.append(path)
        size=0; digest=hashlib.sha256()
        with gzip.open(path,'wb',compresslevel=1) as stream:
            def put(obj):
                nonlocal size
                raw=h.enc(obj); stream.write(raw); size+=len(raw); digest.update(raw)
            put(dict(format=m,goal=store.syntax.text(pkg.goal,image)))
            for i,row in enumerate(store.rows):
                put(pkg.record(row,image))
                if (i+1)%100000==0: print('WRITE',m,i+1,'bytes',size,flush=True)
        assert size==counts[int(image)]
        writers[m]=dict(bytes=size,lines=len(store.rows),sha256=digest.hexdigest(),storage=path.stat().st_size)
    return paths,writers

def ledger(d,packages,lib,store):
    constants=json.loads((ROOT/'scripts/left-closure/output/certificate-202.json').read_text())['constants']
    stats={}
    for mode,off in zip(h.MODES,(0,2)):
        s=store.syntax; terms=[s.parse(t) for t in d['suffixes']+d['letters']+[f"({d['q']}>{d['q']})",f"(~({d['q']}>{d['q']}))"]]
        stats[mode]=(max(s.stats[j][off] for j in terms),max(s.stats[j][off+1] for j in terms),max(s.stats[j][4] for j in terms))
    return lc.thresholds(d,[pkg.checked|dict(rows=pkg.rows) for pkg in packages],constants,stats,max(pkg.checked['name_bytes'] for pkg in lib.values()))

def main():
    assert __debug__, 'assertions required'
    started=time.monotonic(); assert OUT.exists()
    cert=dict(step=261,complete=False,target_complete=False,stage='preparation',failures=[],caps=CAP,
        runtime=dict(python=sys.version,implementation=platform.python_implementation(),assertions=__debug__),
        assessment='drafts/literature/2026-10-16-interned-first-closed-coordinate.md',
        qualification='Known-operation bounded reproduction; trusted local pickle, fixed string keys, parser depth 4096; sampled/heartbeat monitor is not a continuous hard-cap theorem.')
    packages=[]; lib={}; store=None; compiler=None; received=None
    def save():
        cert['elapsed_seconds']=time.monotonic()-started
        cert['worker_peak_rss_bytes']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*(1 if sys.platform=='darwin' else 1024)
        if store:
            cert['rows_so_far']=len(store.rows)
            if isinstance(store.rows,CountRows):
                cert['complete_prefix_byte_counts']=dict(zip(h.MODES,store.rows.bytes))
                cert['max_serialized_row_bytes']=dict(zip(h.MODES,store.rows.max_row_bytes))
        (OUT/'certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
    save()
    try:
        lib=library(); cert['stage']='small differentials'; save()
        cert['small']=small_tests(lib); save()
        envelope=json.loads((h.SOURCE/'source-envelope.json').read_text()); d=envelope['request']
        verify=module('coordinate261_contract','scripts/actual-tree/verify.py')
        goals=verify.contract(envelope['source'],envelope['edges'],d)
        old=json.loads((h.SOURCE/'certificate.json').read_text())['certified_locals']
        expected=lc.ep.e.c.serialize(lc.ep.request(d)['closed'][0])
        cert['source_envelope_sha256']=hashlib.sha256((h.SOURCE/'source-envelope.json').read_bytes()).hexdigest()
        cert['expected']=expected; cert['stage']='restore source'; save()
        with gzip.open(ROOT/'scripts/output-zero/output/interned-255/packages.pkl.gz','rb') as stream:
            snapshots=pickle.load(stream); assert stream.read()==b''
        assert len(snapshots)==len(goals)==len(old)==6
        for i,(snap,goal) in enumerate(zip(snapshots,goals)):
            s=c.pool(snap['nodes']); pkg=h.Package(s,snap['goal'],snap['rows'],snap['paths'],snap['checked']); packages.append(pkg)
            assert s.text(pkg.goal)==goal==old[i]['info']['expected'] and c.exact(pkg.checked,old[i]['checked'])
        del snapshots; gc.collect()
        store=c.Store(); prefix=store.rows[0]
        headers=[len(h.enc(dict(format=m,goal=store.syntax.text(store.syntax.parse(expected),image)))) for m,image in zip(h.MODES,(False,True))]
        store.rows=CountRows(store.syntax,headers); store.rows.append(prefix)
        for pkg in packages: store.copy(pkg,{})
        cert['stage']='complete local-field comparison'; save()
        cert['local_comparison']=c.compare(store,goals,old); save()
        cert['original_input_ledger']=ledger(d,packages,lib,store)
        cert['imports']=copy.deepcopy(store.segments)
        checkpoint(OUT/'before-construction.pkl.gz',store)
        compiler=Compiler(store,lib,d['q']); cert['stage']='construct coordinate 0'; save()
        print('CONSTRUCT source rows',len(store.rows),'expected',expected,flush=True)
        # Save bounded progress at law boundaries, without expanded arguments.
        use=compiler.use; last=[len(store.rows)]
        def monitored_use(name,env):
            if len(store.rows)-last[0]>=20000:
                save(); last[0]=len(store.rows)
                print('PREFIX rows',len(store.rows),'expanded',sum(store.rows.bytes),flush=True)
            return use(name,env)
        compiler.use=monitored_use
        compiler.row(d,[segment['root'] for segment in store.segments])
        cert['stage']='complete preflight'; cert['max_argument_height']=compiler.max_argument_height
        cert['normalizations']=compiler.traces; save()
        bound=cert['original_input_ledger']; assert len(store.rows)<=bound['lines'] and compiler.max_argument_height<=bound['H']
        assert all(t['max_height']<=bound['H'] for t in compiler.traces)
        for mode,image in zip(h.MODES,(False,True)):
            assert store.rows.bytes[int(image)]<=bound['formats'][mode]['bytes']
        checkpoint(OUT/'constructed.pkl.gz',store,compiler)
        cert['stage']='write complete pair'; save()
        paths,writers=write_pair(store,expected,store.rows.bytes)
        cert['writers']=writers; cert['stage']='complete pair reception'; save()
        received=h.load(paths,expected)
        assert len(received.rows)==len(store.rows)
        # Cross-pool field mapping for ALL rows; receiver has checked all native
        # inferences and all native/image fields with simultaneous EOF.
        trans=c.Translation(store.syntax,received.syntax,{})
        for row,got in zip(store.rows,received.rows):
            f,r,refs,subs=row
            want=(trans(c.term(store.syntax,f)),r,refs,tuple((k,trans(c.term(store.syntax,v))) for k,v in subs))
            assert c.exact(want,got)
        for mode in h.MODES:
            got=received.checked['measurements'][mode]
            assert all(got[k]==writers[mode][k] for k in ('bytes','lines','sha256'))
            assert received.checked['node_sums'][mode]<=bound['formats'][mode]['record_nodes']*bound['lines']
            assert received.checked['depths'][mode]<=bound['formats'][mode]['depth']
            assert got['max_record_nodes']<=bound['formats'][mode]['record_nodes']
        cert.update(complete=True,target_complete=True,stage='complete',checked=received.checked,
            retained_local_rows=sum(seg['count'] for seg in store.segments),generated_rows=len(store.rows)-1-sum(seg['count'] for seg in store.segments))
    except BaseException as error:
        cert['failures'].append(type(error).__name__+': '+str(error))
        cert['stopped_at']=cert['stage']
        if store and not (OUT/'unfinished.pkl.gz').exists():
            checkpoint(OUT/'unfinished.pkl.gz',store,compiler)
        cert['stage']='parked incomplete'
        raise
    finally:
        save()
        if received: received.syntax.close()
        if store: store.syntax.close()
        for pkg in packages: pkg.syntax.close()
        for pkg in lib.values(): pkg.syntax.close()
    print('RESULT vertex-0 complete',cert['target_complete'],'rows',len(store.rows),'certificate',str((OUT/'certificate.json').relative_to(ROOT)),flush=True)

if __name__=='__main__': main()
