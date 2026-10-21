"""Step 202 bounded genuine local fixtures and complete export replay."""
import copy
import gzip
import json
import importlib.util
from pathlib import Path

HERE=Path(__file__).resolve().parent; OUT=HERE/'output'; ROOT=HERE.parents[1]
def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
lc=module('left_closure_build',HERE/'build.py')
b,p,c,ep=lc.b,lc.p,lc.c,lc.ep
suite=module('closure_zero_suite',HERE.parent/'backward-zero'/'run_suite.py')
audit=module('closure_archive_audit',HERE.parent/'backward-zero'/'audit_archives.py')
ledger=module('closure_check_ledger',HERE.parent/'backward-zero'/'ledger.py')
DEST=OUT/'certificate-202.json'
def save(obj): DEST.write_text(json.dumps(obj,indent=2)+'\n')


def library(cert):
    lib=suite.library(cert)
    goal=ep.cancellation(); synth=p.Proof(); synth.build_helpers()
    root=synth.prove_fixed(b.aggregate.native(goal))
    checks={}
    for mode,image in [('native',False),('not-or',True)]:
        path=OUT/('close_cancel.'+mode+'.jsonl.gz')
        synth.write(root,path,image)
        checks[mode]=c.check(path,ep.e.c.serialize(ep.e.image(goal) if image else goal))
    # Complete native/image correspondence beyond separate primitive checks.
    audit.scan(OUT/'close_cancel.native.jsonl.gz',ep.e.c.serialize(goal),
               OUT/'close_cancel.not-or.jsonl.gz')
    cert['library']['close_cancel']=checks
    lib['close_cancel']=b.aggregate.load(OUT/'close_cancel.native.jsonl.gz',ep.e.c.serialize(goal))
    cert['constants']['L']=max(a['native']['lines'] for a in cert['library'].values())
    for mode in ('native','not-or'):
        cert['constants'][mode]=dict(D=max(a[mode]['max_line_depth'] for a in cert['library'].values()),
            S=max(a[mode]['max_record_nodes'] for a in cert['library'].values()))
    print('fixed common-expression cancellation both formats',checks['native']['lines'],'lines',flush=True)
    save(cert); return lib


def fixture(name,lib):
    q='A'; y=b.atom((0,),p.I(q,q)); z=b.atom((9,),p.N(p.I(q,q)))
    x=b.atom((3,0),q)
    if name=='diamond':
        # Exactly two constant 0-to-3 paths; variable edge 1-to-3.
        N=4;n=1;t=3
        E0=[[0,1,1,0],[0,0,0,1],[0,0,0,1],[0,0,0,0]]
        Eb=[[[0,0,0,0],[0,0,0,1],[0,0,0,0],[0,0,0,0]]]
        a=b.atom((2,0,3),b.P(q,b.nt(y)))
        views=[a,b.X(y,a),y,y]
    else:
        N=2;n=0;t=0;E0=[[0,0],[0,0]];Eb=[];views=[y,z]
    d=dict(N=N,n=n,q=q,t=t,suffixes=[p.text(b.nt(s)) for s in views],
           letters=[q]*n,E0=E0,Eb=Eb)
    tables=ep.request(d); paths=[]
    opaque=[b.atom((1,v),b.nt(s)) for v,s in enumerate(views)]
    for v in range(N):
        # Test-only decompositions have literally identical native formulas.
        o=b.Store(lib,q)
        extra=[]
        if v==0:
            deep='unused';
            for _ in range(35): deep=p.N(deep)
            extra=[o.p.ax('ax1',deep,'A')]
        rhs=b.X(y if v==t else z,b.X(b.W(E0[v],views,z),
            b.Bal([b.product(x,b.W(Eb[j][v],opaque,z)) for j in range(n)],z)))
        root,traces=b.compare(o,views[v],rhs,z)
        assert p.text(o.p.rows[root][0])==ep.e.c.serialize(tables['local'][v])
        path=OUT/(name+'-local-'+str(v)+'.native.jsonl.gz')
        suite.fixture_write(o,root,path,extra)
        c.check(path,ep.e.c.serialize(tables['local'][v])); paths.append(path)
    (OUT/(name+'.request.json')).write_text(json.dumps(d,indent=2)+'\n')
    return d,paths


def test_case(name,lib,cert):
    d,paths=fixture(name,lib)
    obj=lc.Closure(d,paths,lib)
    terms={mode:suite.measured_terms(d,mode) for mode in ('native','not-or')}
    bound=lc.thresholds(d,obj.packages,cert['constants'],terms,max(a['name_bytes'] for a in lib.values()))
    record=dict(name=name,request=str((OUT/(name+'.request.json')).relative_to(ROOT)),
        inputs=[str(path.relative_to(ROOT)) for path in paths],tables=obj.tables,
        uniform_ledger=bound,exports=[],complete=False)
    # Tables' formula trees are explicit evidence, not output proof axioms.
    cert['cases'].append(record); save(cert)
    for v in range(d['N']):
        print('compile',name,'coordinate',v,flush=True)
        obj.row(v); streams=[]; writers=[]
        for mode,image in [('native',False),('not-or',True)]:
            path=OUT/(name+'-coordinate-'+str(v)+'.'+mode+'.jsonl.gz')
            print('write',name,v,mode,len(obj.p.rows),'records',flush=True)
            writers.append(obj.write(path,image)); streams.append(path)
        expected=ep.e.c.serialize(obj.tables['closed'][v])
        checked=audit.scan(streams[0],expected,streams[1],
            {root:ep.e.c.serialize(obj.tables['closed'][w])
             for w,root in enumerate(obj.coordinate_roots)},
            [(path,len(pkg['rows'])) for path,pkg in zip(paths,obj.packages)])
        out=dict(coordinate=v,proofs={},root=obj.root,complete_input_retention=True,
            exact_endpoint=True,literal_image=True)
        for mode,writer,path in zip(('native','not-or'),writers,streams):
            measured=checked['measurements'][mode]
            assert all(writer[k]==measured[k] for k in ('bytes','lines','sha256'))
            checks=ledger.check(measured,bound['formats'][mode])
            out['proofs'][mode]=dict(path=str(path.relative_to(ROOT)),measurement=measured,
                uniform_checks=checks,writer_matches=True)
            print(name,v,mode,'lines actual/required',measured['lines'],'/',bound['lines'],
                'bytes actual/required',measured['bytes'],'/',bound['formats'][mode]['bytes'],flush=True)
        record['exports'].append(out);save(cert)
    assert obj.max_argument_height<=bound['H']
    assert all(a['max_height']<=bound['H'] for a in obj.traces)
    record['max_argument_height']=obj.max_argument_height
    record['imports']=obj.imports
    record['argument_checks']={}
    for mode,offset in [('native',0),('not-or',2)]:
        stats=[audit.syntax.stats[audit.syntax.parse(s)] for call in obj.calls
            for s in call['arguments'].values()]
        nodes=max([s[offset] for s in stats]+[0]);depth=max([s[offset+1] for s in stats]+[0])
        assert nodes<=bound['formats'][mode]['argument_nodes']
        assert depth<=bound['formats'][mode]['argument_depth']
        count=sum(e['proofs'][mode]['measurement']['bytes'] for e in record['exports'])
        assert count<=bound['formats'][mode]['aggregate_bytes']
        record['argument_checks'][mode]=dict(nodes=nodes,depth=depth,aggregate_bytes=count,
            aggregate_required=bound['formats'][mode]['aggregate_bytes'])
    record['complete']=True;save(cert)
    return d,paths,obj,record


def rejections(d,paths,lib,record,cert):
    def reject(name,op):
        try: op()
        except (c.Invalid,ep.c.Invalid,AssertionError) as exc:
            cert['rejections'].append(dict(name=name,rejected=True,reason=str(exc)))
        else: raise AssertionError('malformed input accepted: '+name)
    for name,change in [('dimension',lambda a:a['E0'][0].append(0)),
        ('triangularity',lambda a:a['E0'][0].__setitem__(0,1))]:
        changed=copy.deepcopy(d);change(changed)
        reject(name,lambda:ep.request(changed))
    def corrupt(source,name,mutation):
        path=OUT/(name+'.native.jsonl.gz')
        with gzip.open(source,'rt') as src,gzip.open(path,'wt') as dst:
            done=False
            for index,raw in enumerate(src):
                row=json.loads(raw)
                if not done: done=mutation(index,row)
                dst.write(json.dumps(row,separators=(',',':'))+'\n')
                if done: # Retain the complete suffix after the one corruption.
                    for rest in src: dst.write(rest)
                    break
            assert done
        return path
    def header(index,row):
        if index==0: row['goal']='A';return True
        return False
    bad=corrupt(paths[0],'wrong-local-endpoint',header)
    reject('local-endpoint',lambda:lc.Closure(d,[bad]+paths[1:],lib))
    exported=ROOT/record['exports'][0]['proofs']['native']['path']
    bad=corrupt(exported,'wrong-export-header',header)
    reject('exported-header',lambda:c.check(bad,ep.e.c.serialize(ep.request(d)['closed'][0])))
    def reference(index,row):
        if row.get('rule')=='mp': row['refs'][0]=index+100;return True
        return False
    bad=corrupt(exported,'wrong-mp-reference',reference)
    reject('MP-reference',lambda:c.check(bad))
    save(cert)


def main():
    cert=dict(step=202,library={},cases=[],rejections=[],failures=[],complete=False)
    save(cert)
    try:
        lib=library(cert)
        test_case('empty',lib,cert)
        d,paths,obj,record=test_case('diamond',lib,cert)
        assert obj.tables['beta']==[[0],[1],[1],[1]]
        assert obj.tables['G'][0][0][3]==1 and sum(obj.tables['K'][0])==3
        rejections(d,paths,lib,record,cert)
        cert['complete']=True;save(cert)
        print('PASS six complete native/image export pairs; five rejections;',DEST.relative_to(ROOT),flush=True)
    except Exception as exc:
        cert['failures'].append(type(exc).__name__+': '+str(exc));save(cert);raise

if __name__=='__main__':main()
