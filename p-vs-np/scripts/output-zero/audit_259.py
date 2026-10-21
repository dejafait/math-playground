"""Independent saved-checkpoint audit; never regenerate or materialize proofs."""
import copy, gzip, hashlib, json, pickle, sys, time
from pathlib import Path
import copier_257 as c
ROOT=c.ROOT
OUT=ROOT/'scripts/output-zero/output/audit-259'
OLD=c.OUT

def read(name): return json.loads((OLD/name).read_text())
def same(a,b):
    assert type(a) is type(b)
    if type(a) is dict:
        assert len(a)==len(b)
        for (k,v),(j,w) in zip(a.items(),b.items()): same(k,j); same(v,w)
    elif type(a) in (list,tuple):
        assert len(a)==len(b)
        for v,w in zip(a,b): same(v,w)
    else: assert a==b

def unpickle(path):
    with gzip.open(path,'rb') as f:
        x=pickle.load(f); assert f.read()==b''; return x

def main():
    started=time.monotonic(); OUT.mkdir(exist_ok=True)
    path=OUT/'certificate.json'; assert not path.exists()
    result=dict(complete=False,failures=[],runtime=sys.version,checks={},rejections=[])
    path.write_text(json.dumps(result,indent=2)+'\n')
    try:
        prior=read('certificate.json'); strict=read('strict-reload.json'); final=read('verification-complete.json')
        for v in (prior,strict,final): assert v['complete'] and not v['failures']
        same(prior['before_checkpoint'],prior['after_checkpoint']); same(strict['comparison'],prior['after_checkpoint'])
        snap=unpickle(OLD/'joined.pkl.gz')
        sources=unpickle(OLD.parent/'interned-255/packages.pkl.gz')
        assert type(snap) is dict and type(snap['version']) is int and snap['version']==1
        nodes=snap['nodes']; index={}
        for j,node in enumerate(nodes):
            assert type(node) is tuple and node not in index
            if node[0]=='v': assert len(node)==2 and type(node[1]) is str and node[1].isascii() and all(x.isalnum() or x=='_' for x in node[1]) and node[1]
            else:
                assert node[0] in ('n','i') and len(node)==(2 if node[0]=='n' else 3)
                assert all(type(k) is int and 0<=k<j for k in node[1:])
            index[node]=j
        def I(a,b): return index[('i',a,b)]
        def N(a): return index[('n',a)]
        rows=snap['rows']
        for j,row in enumerate(rows):
            assert type(row) is tuple and len(row)==4
            f,rule,refs,subs=row
            assert type(f) is int and 0<=f<len(nodes) and type(rule) is str and type(refs) is tuple and type(subs) is tuple
            if rule=='mp':
                assert not subs and len(refs)==2 and all(type(k) is int and 0<=k<j for k in refs)
                assert nodes[rows[refs[1]][0]]==('i',rows[refs[0]][0],f)
            else:
                assert not refs and rule in ('ax1','ax2','ax3')
                assert all(type(p) is tuple and len(p)==2 and type(p[0]) is str and type(p[1]) is int and 0<=p[1]<len(nodes) for p in subs)
                env=dict(subs); assert len(env)==len(subs) and set(env)==({'A','B','C'} if rule=='ax2' else {'A','B'})
                A,B=env['A'],env['B']
                want=I(A,I(B,A)) if rule=='ax1' else I(I(N(A),N(B)),I(B,A)) if rule=='ax3' else I(I(A,I(B,env['C'])),I(I(A,B),I(A,env['C'])))
                assert f==want
        assert len(rows)==155589 and len(snap['locations'])==155588 and len(sources)==len(snap['segments'])==6
        expected=copy.deepcopy(prior['segments'])
        for seg in expected: seg['paths']=tuple(seg['paths']); seg['substitutions']=tuple(tuple(p) for p in seg['substitutions'])
        same(snap['segments'],expected)
        start=1; loc=0; ref_delta=0; counts=[]
        for occurrence,(source,seg) in enumerate(zip(sources,snap['segments'])):
            mapping=[]
            for node in source['nodes']:
                key=node if node[0]=='v' else (node[0],*(mapping[x] for x in node[1:]))
                mapping.append(index[key])
            assert seg['start']==start and seg['count']==len(source['rows']) and not seg['substitutions']
            same(seg['paths'],source['paths']); same(seg['checked'],source['checked'])
            assert seg['goal']==mapping[source['goal']]
            for local,row in enumerate(source['rows']):
                f,rule,refs,subs=row
                assert all(type(r) is int and 0<=r<local for r in refs)
                want=(mapping[f],rule,tuple(start+r for r in refs),tuple((k,mapping[v]) for k,v in subs))
                same(rows[start+local],want)
                same(snap['locations'][loc],(occurrence,seg['paths'],local,start+local)); loc+=1
                ref_delta+=sum(len(str(start+r))-len(str(r)) for r in refs)
            assert seg['root']==start+len(source['rows'])-1 and rows[seg['root']][0]==seg['goal']
            counts.append(len(source['rows'])); start+=len(source['rows'])
        assert start==len(rows) and ref_delta==112718
        result['checks']['all_checkpoint_rows']=len(rows)
        result['checks']['complete_source_to_destination_mapping']=dict(counts=counts,locations=loc,reference_digit_delta_per_format=ref_delta)
        # Bind the saved three comparisons to unchanged full archive byte streams.
        archive_hashes=[]
        for report in prior['after_checkpoint']['packages']:
            for mode,info in report['checked']['measurements'].items():
                digest=hashlib.sha256(); length=0
                with gzip.open(ROOT/info['path'],'rb') as f:
                    while chunk:=f.read(2**20): digest.update(chunk); length+=len(chunk)
                assert length==info['bytes'] and digest.hexdigest()==info['sha256']
                archive_hashes.append(dict(path=info['path'],bytes=length,sha256=digest.hexdigest()))
        result['checks']['unchanged_archives']=archive_hashes
        assert hashlib.sha256((c.h.SOURCE/'source-envelope.json').read_bytes()).hexdigest()==prior['source_envelope_sha256']
        # Resource evidence, independently recomputed, includes all old artifacts.
        monitors=[read('monitor.json'),read('strict-monitor.json')]; test=read('heartbeat-selftest.json')
        for m in monitors:
            assert m['complete'] and not m['failures'] and not m['stopped'] and m['exit_code']==0 and m['samples']>0
            assert m['peak_process_tree_rss_bytes']==m['parent_peak_rss_bytes']+m['worker_peak_rss_bytes']<m['stop_threshold_bytes']==3*2**29
        assert test['complete'] and test['stopped'] and test['stop_reason']=='rss' and test['exit_code']!=0 and not test['failures']
        assert 'PASS child-process creation blocked' in (OLD/'heartbeat-selftest.log').read_text()
        expanded=0
        for p in OLD.glob('*.gz'):
            with gzip.open(p,'rb') as f:
                while chunk:=f.read(2**20): expanded+=len(chunk)
        actual=dict(rss=max(m['peak_process_tree_rss_bytes'] for m in monitors),seconds=sum(m['elapsed_seconds'] for m in monitors)+test['elapsed_seconds'],new_artifacts=sum(p.stat().st_size for p in OLD.iterdir() if p.is_file()),expanded_output=expanded+3*sum(prior['after_checkpoint']['joined_stream_bytes'].values()))
        for name,value in actual.items(): assert value==final['actual_required'][name]['actual']<final['actual_required'][name]['required_max']
        result['checks']['saved_run_actual_required']=final['actual_required']
        # Small independent discriminators; no production tree reconstruction.
        s=c.h.Syntax(); d=c.h.Syntax(); other=c.h.Syntax()
        try:
            root=s.parse('(A>B)'); d.parse('different_first_node')
            env={'A':c.term(d,d.parse('B')),'B':c.term(d,d.parse('(~A)'))}
            tr=c.Translation(s,d,env); env['A']=c.term(d,d.parse('changed'))
            assert d.text(tr(c.term(s,root)))=='(B>(~A))'
            assert d.text(c.Translation(s,d,{'A':c.term(d,d.parse('q'))})(c.term(s,root)))=='(q>B)'
            def reject(name,fn):
                try: fn()
                except (AssertionError,ValueError,TypeError,KeyError,IndexError) as e: result['rejections'].append(dict(name=name,error=type(e).__name__+': '+str(e)))
                else: raise AssertionError('accepted '+name)
            reject('wrong-source-pool',lambda:tr(c.term(other,other.parse('A'))))
            reject('wrong-destination-pool',lambda:c.Translation(s,d,{'A':c.term(s,root)}))
            reject('bare-index',lambda:c.Translation(s,d,{'A':0}))
            reject('boolean-index',lambda:c.term(d,True))
            # Restore tests use a tiny complete admitted package, without writes.
            ss=c.Store(); pp=c.h.Package(ss.syntax,ss.rows[-1][0],list(ss.rows),('native','image'),{})
            dest=c.Store(); dest.copy(pp,{})
            try:
                small=copy.deepcopy(dest.snapshot()); exp=copy.deepcopy(dest.segments)
                q=c.restore(small,exp); q.syntax.close()
                for name,mutate in [
                    ('float-count',lambda z:z['segments'][0].__setitem__('count',1.0)),
                    ('boolean-location',lambda z:z['locations'].__setitem__(0,(False,('native','image'),0,1))),
                    ('paths-list',lambda z:z['segments'][0].__setitem__('paths',['native','image'])),
                    ('segments-tuple',lambda z:z.__setitem__('segments',tuple(z['segments']))),
                    ('unexpected-string-key',lambda z:z['segments'][0].__setitem__('extra',0))]:
                    bad=copy.deepcopy(small); mutate(bad)
                    reject(name,lambda bad=bad:c.restore(bad,exp))
            finally: ss.syntax.close(); dest.syntax.close()
            assert c.exact({1:'x'},{True:'x'}) # Deliberate outside-schema limit, not claimed strict here.
            assert not c.exact({'start':1},{'start':True}) and not c.exact({'start':1},{'start':1.0})
            result['checks']['scope']=dict(environment_snapshot=True,simultaneous_replacement=True,fresh_environment=True,fixed_string_key_schema_required=True,historical_runtime_version_not_recorded=True)
        finally: s.close(); d.close(); other.close()
        result['complete']=True
    except BaseException as e:
        result['failures'].append(type(e).__name__+': '+str(e)); raise
    finally:
        result['elapsed_seconds']=time.monotonic()-started
        path.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS independent checkpoint rows',len(rows),'source occurrences',loc,'small rejections',len(result['rejections']))
    for name,v in result['checks']['saved_run_actual_required'].items(): print(name,v['actual'],'/',v['required_max'])
    print('Evidence',path.relative_to(ROOT),'historical runtime version not recorded; schema qualification retained')
if __name__=='__main__': main()
