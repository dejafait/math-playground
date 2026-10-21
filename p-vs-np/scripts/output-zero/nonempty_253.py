"""One capped L068 fixture; unchanged proof operations, strict full replay.

The byte preflight is resource evidence only. A stopped internal pickle is
not a native proof archive and is never received as a checked package.
"""
import gc
import gzip
import hashlib
import importlib.util
import json
import pickle
import resource
import shutil
import signal
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT/'scripts/output-zero/output/nonempty-253'
sys.path.insert(0, str(ROOT/'scripts/left-closure'))
import replay_star as replay
import finish_exports as writers

def load(name, path):
    spec = importlib.util.spec_from_file_location(name, ROOT/path)
    obj = importlib.util.module_from_spec(spec); spec.loader.exec_module(obj)
    return obj

actual = load('nonempty253_actual', 'scripts/actual-tree/build.py')
verify = load('nonempty253_verify', 'scripts/actual-tree/verify.py')
tables = load('nonempty253_tables', 'scripts/coefficient-chain/construct.py')
sys.path.insert(0, str(ROOT/'scripts/coefficient-chain'))
table_check = load('nonempty253_table_check', 'scripts/coefficient-chain/check.py')
lc = replay.h.lc
b, p = actual.b, actual.p
MODES = ('native', 'not-or')
GiB = 2**30
CAP = dict(rss=2*GiB, storage=16*GiB, expanded=128*GiB, seconds=600)
SOURCE = dict(tree=['add', ['var', 0], ['var', 0]], letters=['x'], q='x', delete_zero=False)
cert = dict(step=253, target_complete=False, failures=[], certified_locals=[],
            certified_coordinates=[], pending=['coordinates', 'chain', 'bridge',
            'final composition', 'nested joined retention', 'original-source actual ledger'],
            caps=CAP, source=SOURCE, no_optional_proofs=True)
started = None
expanded = 0
active = None
stage = 'startup'

class Stop(Exception): pass

def enc(obj):
    return (json.dumps(obj, separators=(',', ':'), ensure_ascii=True)+'\n').encode('ascii')

def save():
    cert['stage'] = stage
    cert['elapsed_seconds'] = time.monotonic()-started
    cert['expanded_bytes_written'] = expanded
    cert['peak_rss_bytes'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * (1 if sys.platform == 'darwin' else 1024)
    (OUT/'certificate.json').write_text(json.dumps(cert, indent=2)+'\n')

def guard():
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * (1 if sys.platform == 'darwin' else 1024)
    if rss >= 7*GiB//4: raise Stop('conservative RSS checkpoint threshold: '+str(rss))
    if time.monotonic()-started >= 540: raise Stop('540-second checkpoint threshold')
    storage = sum(x.stat().st_size for x in OUT.iterdir() if x.is_file())
    if storage >= 15*GiB: raise Stop('conservative compressed-artifact threshold')
    if shutil.disk_usage(OUT).free < CAP['storage']-storage+GiB:
        raise Stop('free-space headroom unavailable')
    if expanded > CAP['expanded']: raise Stop('expanded output cap')

def scan(pair, goal):
    guard()
    # Original strict scanner, with a monitoring callback only at read boundaries.
    a = replay.a; a.syntax = replay.f.FastSyntax()
    count = 0
    def monitored(raw):
        nonlocal count
        count += 1
        if count % 1024 == 0: guard()
        return replay.strict_read(raw)
    a.read = monitored
    try:
        got = a.scan(pair[0], goal, pair[1])
        return {k:v for k,v in got.items() if k not in ('rows', 'references')}
    finally:
        a.syntax.close(); a.syntax = a.Syntax(); a.read = replay.original_read

def pair_write(o, stem):
    global expanded
    paths, result = [], {}
    for mode in MODES:
        path = OUT/(stem+'.'+mode+'.jsonl.gz'); assert not path.exists()
        paths.append(path); spelling = writers.Spelling(mode == 'not-or')
        size = 0; digest = hashlib.sha256()
        with gzip.open(path, 'wb', compresslevel=1) as stream:
            def put(row):
                nonlocal size
                global expanded
                raw = enc(row)
                if expanded+len(raw) > CAP['expanded']: raise Stop('expanded output cap before write')
                stream.write(raw); size += len(raw); expanded += len(raw); digest.update(raw)
            put(dict(format=mode, goal=spelling.text(o.p.rows[o.root][0])))
            for i, (f, rule, refs, subs, deps) in enumerate(o.p.rows):
                assert not deps
                row = dict(f=spelling.text(f), rule=rule)
                if rule == 'mp': row['refs'] = list(refs)
                else: row['subs'] = {k:spelling.text(v) for k,v in subs.items()}
                put(row)
                if i % 1024 == 0: guard()
        result[mode] = dict(lines=len(o.p.rows), bytes=size, sha256=digest.hexdigest())
    return paths, result

def majorants(F_lib, B):
    """L068 (4)-(11), from source and fixed libraries, before generation."""
    U,d = actual.validate_input(SOURCE, 4); N,n = 2*U,len(SOURCE['letters'])
    Q = len(enc(SOURCE))-1
    cl = lambda s: (s-1).bit_length()
    F = lambda s: 256+64*cl(s+2)
    t = 48*4**(2*d+2)
    H66=2*d+cl(n+2)+8; G66=2568*1000*(n+2); J66=G66; P66=48*4**(H66+1)
    h65=cl(2+N+n); V65=2**(3*h65+6); H65=9*h65+30
    G65=3471*10000*N*V65**2*(H65+1)**2; J65=N*J66+G65
    P65=8*4**(H65+1)*(t+1)
    h64=cl(2+2*N+n); V64=2**(3*h64+4); H64=9*h64+20
    G64=N*N*3471*10000*V64**2*(H64+1)**2; J64=N*J65+G64
    P64=8*4**(H64+1)*(t+1)
    Lloc=(N*N+2*N+3)*(512+128*cl(J64+N*N+N+3))
    R=1000*(B+4)*(n+2)*(U+2)**3*4**(2*d+3)
    T=2**30*(Q+2)**28+1; Jb=1634; Hb=d+1; Pb=48*4**(Hb+1)
    Mb=10000*(R+Jb+2)**2+(B+4)*(584+788)*Pb
    Js=Jb+J64+1449+2; ell=cl(Js+2)
    out=dict(Q_source=Q,Q_0=Q,U=U,depth=d,N=N,n=n,B=B,F_lib=F_lib,t=t,
             J66=J66,J65=J65,J64=J64,J_final=Js,Lloc=Lloc,R=R,T=T,Mb=Mb,formats={})
    for mode,c,S66,S65,Sb,St in [('native',3,2040,2456,584,792),('not-or',6,2712,3492,788,1100)]:
        dj=c*(2*d+1)+3
        U66=(B+4)*(G66+1)*S66*P66+(J66+2)*F(J66)
        U65=(B+4)*(N*U66+(G65+1)*S65*P65)+(J65+2)*F(J65)
        A64=max(N*U65,S65*P64)
        U64=(B+4)*(N*U65+G64*S65*P64+A64)+(J64+2)*F(J64)
        Vb=(Jb+2)*((B+4)*Sb*Pb+F(Jb))
        W=Vb+U64+2*(Jb+J64)*ell+(1449+4)*((B+4)*St*t+256+64*ell)
        out['formats'][mode]=dict(U66=U66,U65=U65,U64=U64,Vb=Vb,W=W,
            local_records=J66,coordinate_records=J65,local_bytes=U66,coordinate_bytes=U65)
    E=10000+Q+F_lib+R+T+Mb+Lloc+Js+sum(N*x['U66']+N*x['U65']+x['Vb']+x['U64']+x['W'] for x in out['formats'].values())
    out.update(E_star=E,M_star=10**8*(E+2)**5,aggregate_full_bit_bound=8*(4*E+10**8*(E+2)**5))
    return out

class ByteCount:
    """Exact serialized JSON length without expanded formula strings."""
    def __init__(self): self.cache={}
    def term(self,t,image):
        key=(id(t),image)
        if key in self.cache:
            held,value=self.cache[key]; assert held is t; return value
        if isinstance(t,str): value=len(t)
        elif t[0]=='n': value=3+self.term(t[1],image)
        else: value=(6 if image else 3)+self.term(t[1],image)+self.term(t[2],image)
        self.cache[key]=(t,value); return value
    def row(self,row,image):
        f,rule,refs,subs,deps=row
        shell=dict(f='',rule=rule)
        if rule=='mp': shell['refs']=list(refs)
        else: shell['subs']={k:'' for k in subs}
        return len(enc(shell))+self.term(f,image)+sum(self.term(v,image) for v in (subs or {}).values())

def main():
    global started, active, stage
    if OUT.exists(): raise RuntimeError('fresh destination required')
    OUT.mkdir(parents=True); started=time.monotonic(); save()
    signal.signal(signal.SIGALRM, lambda *_: (_ for _ in ()).throw(Stop('540-second alarm')))
    signal.alarm(540)
    try:
        guard(); (OUT/'source.json').write_bytes(enc(SOURCE))
        data=actual.construct(SOURCE,4); req=data['request']
        goals=verify.contract(SOURCE,data['edges'],req)
        assert table_check.words(SOURCE['tree']) == set()
        table=tables.construct(SOURCE,4); assert table_check.check(table)
        assert table['adjacency']==req
        (OUT/'source-envelope.json').write_bytes(enc(dict(source=SOURCE,edges=data['edges'],request=req)))
        (OUT/'tables.json').write_bytes(enc(table))
        cert['source_checks']=dict(independent_actual_contract=True,formal_word_zero=True,
            all_dimensioned_tables=True,dimensions=table['ledger']['dimensions'],source_row=table['chain']['levels'][0]['R'])
        stage='fixed-library reception'; save()
        source_lib={}; closure_lib={}; lib_checks={}; F_lib=0; B=1
        source_goals=dict((k,b.ep.fixed()[k]) for k in ('refl','symm','trans','congL','congR','zeroR','zeroL','prod_zero'))
        source_goals.update(actual.fixed())
        closure_goals=dict(lc.b.ep.fixed(),close_cancel=lc.ep.cancellation())
        for role, goals_dict, dest in [('source',source_goals,source_lib),('closure',closure_goals,closure_lib)]:
            lib_checks[role]={}
            for name,goal in goals_dict.items():
                if name in actual.fixed(): folder='actual-tree'
                elif name=='close_cancel': folder='left-closure'
                elif name in ('zeroR','zeroL','prod_zero'): folder='backward-zero'
                elif name in ('dist','prod_cong'): folder='balanced-distribution'
                else: folder='balanced-slot'
                pair=[ROOT/f'scripts/{folder}/output/{name}.{mode}.jsonl.gz' for mode in MODES]
                # source_goals mixes internal and endpoint syntax: normalize once.
                literal=p.text(goal) if name in actual.fixed() else lc.ep.e.c.serialize(goal)
                got=scan(pair,literal)
                lib_checks[role][name]=got
                F_lib+=sum(x['bytes'] for x in got['measurements'].values())
                B=max(B,got['name_bytes'])
                dest[name]=b.aggregate.load(pair[0],literal)
            cert['libraries']=lib_checks; save(); print('PASS fixed library',role,flush=True)
        # Pay the repeated bridge/chain/trans library roles as constants too.
        bound=majorants(4*F_lib,B); (OUT/'source-majorants.json').write_bytes(enc(bound))
        cert['source_majorants']='scripts/output-zero/output/nonempty-253/source-majorants.json'
        stage='small local packages'; paths=[]
        for v in range(req['N']):
            guard(); o=b.Store(source_lib,'x'); active=o
            info=actual.local(o,data,v)
            pair,written=pair_write(o,'local-'+str(v)); checked=scan(pair,info['expected'])
            for mode in MODES:
                assert all(written[mode][k]==checked['measurements'][mode][k] for k in ('bytes','lines','sha256'))
                assert written[mode]['bytes']<=bound['formats'][mode]['local_bytes']
                assert written[mode]['lines']<=bound['J66']
            cert['certified_locals'].append(dict(v=v,info=info,checked=checked))
            paths.append(pair[0]); save(); print('PASS local',v,'records',written['native']['lines'],flush=True)
            active=None; del o; gc.collect()
        stage='coordinate preflight'; obj=lc.Closure(req,paths,closure_lib); active=obj
        assert all(obj.tables[k]==table['chain'][k] for k in ('beta','G'))
        assert obj.tables['K']==table['K']
        counter=ByteCount(); counts=[0,0]
        # Test the counting specialization on all complete local records/fields.
        for row in obj.p.rows:
            for image in (False,True):
                f,rule,refs,subs,deps=row
                rendered=dict(f=p.text(f,image),rule=rule)
                if rule=='mp': rendered['refs']=list(refs)
                else: rendered['subs']={k:p.text(v,image) for k,v in subs.items()}
                assert counter.row(row,image)==len(enc(rendered))
                counts[image]+=counter.row(row,image)
        cert['counting_validation']=dict(complete_imported_records=len(obj.p.rows),both_formats=True)
        original_add=obj.p.add
        def counted_add(*args,**kwargs):
            j=original_add(*args,**kwargs)
            for image in (False,True): counts[image]+=counter.row(obj.p.rows[j],image)
            # Every required later export retains this whole current prefix.
            lower=(req['N']-len(obj.coordinate_roots))*sum(counts)+expanded
            if j % 1024 == 0:
                cert['preflight']=dict(coordinate=len(obj.coordinate_roots),records=len(obj.p.rows),
                    partial_record_bytes=dict(zip(MODES,counts)),minimum_expanded_outputs=lower,
                    required_cap=CAP['expanded'],proof_verified=False)
                save(); guard()
            if lower>CAP['expanded']:
                cert['preflight']=dict(coordinate=len(obj.coordinate_roots),records=len(obj.p.rows),
                    partial_record_bytes=dict(zip(MODES,counts)),minimum_expanded_outputs=lower,
                    required_cap=CAP['expanded'],proof_verified=False)
                raise Stop('complete-prefix output lower bound exceeds approved expanded cap')
            return j
        obj.p.add=counted_add
        for v in range(req['N']):
            cert['coordinate_started']=v; save(); obj.row(v)
            cert['completed_coordinate_roots']=obj.coordinate_roots[:]; save()
            # This bounded fixture may only advance after whole-pair replay.
            pair,written=pair_write(obj,'coordinate-'+str(v))
            goal=lc.ep.e.c.serialize(obj.tables['closed'][v]); checked=scan(pair,goal)
            cert['certified_coordinates'].append(dict(v=v,written=written,checked=checked)); save()
        raise Stop('coordinates completed; joined stage requires remaining-budget recheck')
    except Stop as error:
        cert['resource_stop']=str(error); cert['target_complete']=False
        print('STOP',error,flush=True)
    except BaseException as error:
        cert['failures'].append(type(error).__name__+': '+str(error))
        raise
    finally:
        signal.alarm(0)
        # Rows and coordinate/call/import metadata are losslessly saved; no
        # pickle of local functions, and no assertion of primitive validation.
        if active is not None:
            partial=dict(rows=active.p.rows,imports=active.imports,calls=active.calls,
                coordinate_roots=getattr(active,'coordinate_roots',[]),
                traces=getattr(active,'traces',[]),root=getattr(active,'root',None),
                source=SOURCE,stage=stage,verified=False)
            path=OUT/'unfinished-state.pickle.gz'
            with gzip.open(path,'wb',compresslevel=1) as stream: pickle.dump(partial,stream,protocol=5)
            cert['unfinished_internal_state']=str(path.relative_to(ROOT))
            cert['unfinished_records']=len(active.p.rows)
        save()
        print('RESULT target_complete',cert['target_complete'],'locals',len(cert['certified_locals']),
            'coordinates',len(cert['certified_coordinates']),'expanded written',expanded,
            '/',CAP['expanded'],'certificate',str((OUT/'certificate.json').relative_to(ROOT)),flush=True)

if __name__=='__main__': main()
