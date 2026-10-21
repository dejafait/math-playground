"""Step 198: complete small chain discriminator and paid boundary evidence."""
import copy
import gzip
import json
from pathlib import Path
import chain

b=chain.b; ep,p,c=b.ep,b.p,b.checker
HERE=Path(__file__).resolve().parent
# build's component imports alter sys.path; keep each notebook-local harness
# under its own name instead of resolving sibling run_suite/audit_archives.
suite=b.module('chain_suite_198',HERE/'run_suite.py')
audit=b.module('chain_archive_checker_198',HERE/'audit_archives.py')
ledger=b.module('chain_row_ledger_198',HERE/'ledger.py')
OUT=suite.OUT; DEST=OUT/'chain-198-certificate.json'


def save(obj): suite.save(DEST,obj)


def locations(obj):
    return {'coordinate_imports':obj.imports,
            'levels':[level['k'] for level in obj.data['levels']],
            'rows':[{key:row[key] for key in ('level','row','start','end','required_roots')}
                    for row in obj.rows]}


def run_case(name,data,lib,cert,deep=False,repeat_paths=False):
    chain.validate(data)
    fixed=dict(chain.base_request(data),k=0,r=[[0]*data['N']],R_next=[],
               T=[[[]] for _ in range(data['n'])])
    paths,_=suite.fixtures(fixed,name,lib,deep)
    if repeat_paths:
        assert len(set(ep.strings(fixed)['coordinates']))==1
        paths=[paths[0]]*data['N']
    request=OUT/(name+'.request.json'); suite.save(request,data)
    print('compile',name,flush=True)
    obj=chain.compile_chain(data,paths,lib)
    bound=chain.thresholds(data,obj.packages,cert['constants'],
        {mode:suite.measured_terms(fixed,mode) for mode in ('native','not-or')},
        max(a['name_bytes'] for a in lib.values()))
    record={'name':name,'request':str(request.relative_to(suite.ROOT)),
            'coordinate_paths':[str(path.relative_to(suite.ROOT)) for path in paths],
            'uniform_ledger':bound,'proofs':{},'rows':obj.rows,'imports':obj.imports,
            'input_uncompressed_bytes':sum(a['measurement']['bytes'] for a in obj.packages)
                                       +request.stat().st_size,
            'complete':False}
    cert['cases'].append(record); save(cert)
    root_goals={}
    for row in obj.rows:
        goals=ep.strings(chain.row_request(data,row['level'],row['row']))['goals']
        for root,goal in zip(row['required_roots'],goals):
            if root in root_goals: assert root_goals[root]==goal
            root_goals[root]=goal
    final=p.text(obj.p.rows[obj.root][0])
    loc=OUT/(name+'.locations.json'); suite.save(loc,locations(obj))
    assert loc.stat().st_size<=bound['metadata_bytes']
    record['locations']={'path':str(loc.relative_to(suite.ROOT)),
                         'bytes':loc.stat().st_size,'required':bound['metadata_bytes']}
    streams=[]; writers=[]
    for mode,image in [('native',False),('not-or',True)]:
        path=OUT/(name+'.'+mode+'.jsonl.gz'); streams.append(path)
        print('write',name,mode,len(obj.p.rows),'records',flush=True)
        writers.append(obj.write(path,image))
    print('reconstruct every native/image record and complete imports',name,flush=True)
    checked=audit.scan(streams[0],final,streams[1],root_goals,
                       [(path,len(pkg['rows'])) for path,pkg in zip(paths,obj.packages)])
    for (mode,writer),path in zip(zip(('native','not-or'),writers),streams):
        measured=checked['measurements'][mode]
        assert all(writer[key]==measured[key] for key in ('bytes','lines','sha256'))
        checks=ledger.check(measured,bound['formats'][mode])
        record['proofs'][mode]={'path':str(path.relative_to(suite.ROOT)),
            'measurement':measured,'uniform_checks':checks,'writer_matches':True}
        print(name,mode,'actual/required lines',measured['lines'],'/',bound['lines'],
              'bytes',measured['bytes'],'/',bound['formats'][mode]['bytes'],
              'depth',measured['max_line_depth'],'/',bound['formats'][mode]['depth'],flush=True)
    ancestry=[]
    for row in obj.rows:
        i,j=row['level'],row['row']; r=chain.row_request(data,i,j)
        used=sorted({k for table in r['T'] for k,bit in enumerate(table[0]) if bit})
        ancestors=audit.ancestors(checked['references'],row['required_roots'][2])
        for k in used:
            root=row['next_roots'][k]
            assert root<row['start'] and root in ancestors
            ancestry.append({'level':i,'row':j,'selected_index':k,'actual_root':root,
                             'before':row['start'],'in_Q8_zero_ancestry':True})
    record['used_next_row_ancestry']=ancestry
    record['all_requested_endpoints_checked']=True
    record['all_references_strictly_earlier']=True
    record['one_time_complete_coordinate_retention']=True
    record['max_argument_height']=obj.max_argument_height
    assert obj.max_argument_height<=bound['H']
    assert all(trace['max_height']<=bound['H'] for row in obj.rows for trace in row['traces'])
    # Bound every ACTUAL argument independently; these measurements are never
    # used to choose the uniform ledger.
    for mode in ('native','not-or'):
        a=2 if mode=='not-or' else 0
        stats=[audit.syntax.stats[audit.syntax.parse(text)]
               for call in obj.calls for text in call['arguments'].values()]
        nodes=max([t[a] for t in stats]+[0]); depth=max([t[a+1] for t in stats]+[0])
        assert nodes<=bound['formats'][mode]['argument_nodes']
        assert depth<=bound['formats'][mode]['argument_depth']
        record['proofs'][mode]['actual_argument_nodes']=nodes
        record['proofs'][mode]['actual_argument_depth']=depth
    record['complete']=True; save(cert)
    return obj,paths,streams


def negative_tests(data,paths,lib,obj,streams,cert):
    def reject(name,operation):
        try: operation()
        except (c.Invalid,ep.c.Invalid,AssertionError) as exc:
            cert['rejections'].append({'name':name,'rejected':True,
                                       'reason':str(exc) or type(exc).__name__})
        else: raise AssertionError('malformed input accepted: '+name)
    for name,change in [
        ('row-width',lambda d:d['levels'][0]['R'][0].append(0)),
        ('matrix-identity',lambda d:d['levels'][0]['T'][0][0][0].__setitem__(1,0)),
        ('non-bit',lambda d:d['G'][0][0].__setitem__(0,2)),
        ('terminal-not-empty',lambda d:d['levels'][-1].update(k=1,R=[[0]*d['N']],T=[[[[]]]])),
        ('missing-indexed-T',lambda d:d['levels'][1]['T'].pop()),
        ('r-beta',lambda d:d['beta'].__setitem__(0,[1]))]:
        changed=copy.deepcopy(data); change(changed)
        reject(name,lambda d=changed:chain.validate(d))
    reject('missing-coordinate',lambda:chain.compile_chain(data,paths[:-1],lib))
    h=obj.handles[(1,0)]
    reject('wrong-state-handle',lambda:obj.resolve(1,0,chain.RowHandle(object(),1,0,h.root)))
    reject('wrong-index-coincident-endpoint',lambda:obj.resolve(1,1,h))
    old=h.root
    h.root=len(obj.p.rows)
    reject('later-row-root',lambda:obj.resolve(1,0,h))
    h.root=0
    reject('wrong-row-endpoint',lambda:obj.resolve(1,0,h))
    h.root=old
    # Preserve complete corrupted archives; rejection is allowed at header.
    for name,path in [('wrong-coordinate-endpoint',paths[0]),('wrong-literal-endpoint',streams[1])]:
        corrupt=OUT/(name+'-chain-198.jsonl.gz')
        with gzip.open(path,'rb') as src,gzip.open(corrupt,'wb') as dst:
            header=json.loads(src.readline()); header['goal']='BAD_ENDPOINT'
            dst.write((json.dumps(header,separators=(',',':'))+'\n').encode('ascii'))
            for raw in src: dst.write(raw)
        if name=='wrong-coordinate-endpoint':
            reject(name,lambda:chain.compile_chain(data,[corrupt]+paths[1:],lib))
        else:
            reject(name,lambda:audit.scan(streams[0],p.text(obj.p.rows[obj.root][0]),corrupt))
        cert['rejections'][-1]['path']=str(corrupt.relative_to(suite.ROOT))
    save(cert)


def main():
    cert={'complete':False,'failures':[],'library':{},'cases':[], 'rejections':[],
          'harness_incidents':[{'type':'AttributeError','resolved':True,
                               'reason':'generic run_suite resolved a sibling after component sys.path insertion',
                               'log':'scripts/backward-zero/output/chain-198-initial.log'}],
          'all_size_bound':'L064_INFORMAL_PROOF_PENDING_SEPARATE_CRITICAL_AUDIT'}
    save(cert)
    try:
        lib=suite.library(cert); save(cert)
        q='A'; z=p.text(p.N(p.I(q,q)))
        data={'N':3,'n':1,'q':q,'suffixes':[z]*3,'letters':[q],
              'beta':[[0],[0],[0]],'G':[[[0,1,0],[0,0,1],[0,0,0]]],
              'levels':[{'k':1,'R':[[1,0,0]],'T':[[[[0,1]]]]},
                        {'k':2,'R':[[0,1,0],[0,1,0]],'T':[[[[1]]],[[[1]]]]},
                        {'k':1,'R':[[0,0,1]],'T':[[[[]]]]},
                        {'k':0,'R':[],'T':[]}]}
        obj,paths,streams=run_case('chain-198-used',data,lib,cert,deep=True)
        negative_tests(data,paths,lib,obj,streams,cert)
        empty={'k':0,'R':[],'T':[]}
        # Same complete coordinate path supplied twice is two occurrences.
        boundary={'N':2,'n':0,'q':q,'suffixes':[z]*2,'letters':[],
                  'beta':[[0],[0]],'G':[],'levels':[empty]}
        run_case('chain-198-depth-zero',boundary,lib,cert,deep=True,repeat_paths=True)
        boundary=copy.deepcopy(boundary)
        boundary['levels']=[{'k':1,'R':[[0,0]],'T':[[]]},copy.deepcopy(empty),
                            {'k':1,'R':[[1,0]],'T':[[]]},copy.deepcopy(empty)]
        run_case('chain-198-empty-level',boundary,lib,cert,deep=True,repeat_paths=True)
        cert['complete']=True; save(cert)
        print('complete; failures',len(cert['failures']),'rejections',len(cert['rejections']),
              'certificate',str(DEST.relative_to(suite.ROOT)),flush=True)
    except Exception as exc:
        cert['failures'].append({'type':type(exc).__name__,'message':str(exc)})
        save(cert); raise


if __name__=='__main__': main()
