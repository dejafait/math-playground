"""Fresh variable-leaf actual-tree production/reception; complete exports and source-only ledgers."""
import gzip
import hashlib
import audit_218 as independent
import json
import sys
import finish_exports as f
import replay_star as r

h, ROOT, OUT = f.h, f.ROOT, f.OUT
DEST = OUT / 'reception-224.json'
SOURCE = ROOT / 'scripts/actual-tree/output'
actual = h.module('variable224_actual', SOURCE.parent / 'build.py')
from audit_222 import ceil_log



def compact(a):
    return {k: v for k, v in a.items() if k not in ('rows', 'references')}



def exact_variable(inp):
    """Independent literal reconstruction for this fixed original fixture."""
    I, X, E, P, neg = independent.I, independent.X, independent.E, independent.P, independent.neg
    y = I('q','q'); z = neg(y); suffixes = [P('x',y),y]
    eb = [[[0,1],[0,0]]]
    assert inp == dict(source=dict(tree=['var',0],letters=['x'],q='q',delete_zero=False),
        edges=[dict(v=0,w=1,kind='var',position=0)],
        request=dict(N=2,n=1,t=1,q='q',suffixes=suffixes,letters=['x'],
                     E0=[[0,0],[0,0]],Eb=eb))
    return dict(local=[E(suffixes[0],X(z,X(z,P('x',y)))),
                       E(y,X(y,X(z,P('x',z))))],
        coordinates=[E(suffixes[0],X(z,P('x',y))),E(y,X(y,P('x',z)))],
        K=[[1,0],[0,1]], receiving=dict(N=2,n=1,q='q',suffixes=suffixes,letters=['x'],
            beta=[[0],[1]],G=eb,levels=[dict(k=0,R=[],T=[])]))



def replay_libraries(prior, initial):
    libraries = {}
    for name, goals in zip(('source','closure'),independent.fixed()):
        library = {}; libraries[name] = library
        for law, goal in goals.items():
            saved = prior['library'][law]['measurements'] if name == 'source' else initial['library'][law]
            got = r.scan(r.f.FastSyntax,ROOT/saved['native']['path'],goal,
                         ROOT/saved['not-or']['path'])
            for m in ('native','not-or'):
                for key,value in got['measurements'][m].items():
                    assert saved[m][key] == value, (name,law,m,key)
            library[law] = compact(got)
        print('PASS complete fixed library',name,len(library),'pairs',flush=True)
    assert independent.constants(libraries['source']) == dict(L=2567,native=dict(D=18,S=2040),
                                                              **{'not-or':dict(D=24,S=2712)})
    assert independent.constants(libraries['closure']) == dict(L=3470,native=dict(D=19,S=2456),
                                                               **{'not-or':dict(D=27,S=3492)})
    return libraries


def independent_ledgers(cert, inp, initial, local, libraries, bound, source_bound, composed):
    """Recompute audited (1)/(4) from source/optional data and both libraries."""
    modes = ('native','not-or'); d = inp['request']; optional = cert['optional']
    B=max(1,len(d['q']),*[len(x) for x in d['letters']],*[x['name_bytes'] for x in optional],
          *[x['name_bytes'] for lib in libraries.values() for x in lib.values()])
    assert all(x['name_bytes'] <= B for x in local)
    cs=independent.constants(libraries['source']); cc=independent.constants(libraries['closure'])
    I0=sum(x['measurements']['native']['lines'] for x in optional)
    U,depth=actual.validate_input(inp['source'],depth_factor=4)
    N,n=2*U,len(inp['source']['letters'])
    H=2*depth+(n+1).bit_length()+8; T=1000*(n+2)
    G=(cs['L']+1)*T; J=I0+G; pp=48*4**(H+1)
    sb=dict(U=U,source_depth=depth,N=N,n=n,H=H,operations=T,
            generated_records=G,argument_nodes=pp,formats={})
    for m,factor in zip(modes,(3,6)):
        K=sum(x['node_sums'][m] for x in optional); delta=max(x['depths'][m] for x in optional)
        S,D=cs[m]['S'],cs[m]['D']
        size=(B+4)*(K+(G+1)*S*pp)+(J+2)*(256+64*(J+1).bit_length())
        sb['formats'][m]=dict(lines=J,depth=max(delta,D+factor*H+3),
            record_nodes=max(K,S*pp),bytes=size,aggregate_bytes=N*size,aggregate_bits=8*N*size)
        for pkg in local:
            measured=pkg['measurements'][m]
            assert measured['lines']<=J and measured['bytes']<=size
            assert measured['max_record_nodes']<=sb['formats'][m]['record_nodes']
            assert pkg['node_sums'][m]<=measured['bytes'] and pkg['depths'][m]<=sb['formats'][m]['depth']
    assert sb == source_bound
    syntax=r.f.FastSyntax()
    try:
        y=independent.I('q','q'); z=independent.neg(y)
        stats=[syntax.stats[syntax.parse(s)] for s in d['suffixes']+d['letters']+[y,z]]
        terms={m:(max(s[off] for s in stats),max(s[off+1] for s in stats))
               for m,off in zip(modes,(0,2))}
    finally: syntax.close()
    direct=independent.ledger(N,n,sum(x['measurements']['native']['lines'] for x in local),
        {m:sum(x['node_sums'][m] for x in local) for m in modes},
        {m:max(x['depths'][m] for x in local) for m in modes},B,terms,cc)
    majorant=independent.ledger(N,n,N*J,{m:N*sb['formats'][m]['bytes'] for m in modes},
        {m:sb['formats'][m]['depth'] for m in modes},B,terms,cc)
    assert direct == bound and majorant == composed
    cert['source_accounting_check']=dict(complete=True,source_payload_bytes=B,
        original_optional_records=I0,source_bound_recomputed=True,composition_recomputed=True,
        node_count_majorant='Full formula and substitution nodes each occupy at least one uncompressed ASCII byte.',
        qualification='Fixed thirteen-law source and fifteen-law closure libraries are paid separately; no generated coordinate length defines a bound.')


def check_prefix_and_metadata(cert, inp_path, inp, paths):
    cert['earlier_prefix'] = {}
    for m in ('native','not-or'):
        exports=[ROOT/x['proofs'][m]['measurement']['path'] for x in cert['exports']]
        count=size=0; digest=hashlib.sha256()
        with gzip.open(exports[0],'rb') as first,gzip.open(exports[1],'rb') as second:
            first.readline(); second.readline()  # Distinct independently checked endpoint headers.
            for raw in first:
                assert raw == second.readline(), (m,count,'earlier generated prefix changed')
                count+=1; size+=len(raw); digest.update(raw)
            assert second.readline(), 'later coordinate must add records'
        required=cert['exports'][0]['proofs'][m]['measurement']['lines']
        assert count == required == cert['exports'][0]['root']+1
        cert['earlier_prefix'][m]=dict(records=count,required_records=required,
            record_bytes=size,record_sha256=digest.hexdigest(),byte_identical_prefix=True)
        print('PASS earlier full prefix',m,count,'/',required,'records',flush=True)
    metadata=dict(source=inp,original_received=cert['original_received'],imports=cert['imports'],
        receiving=cert['receiving'],exports=[dict(coordinate=x['coordinate'],root=x['root'],
            paths={m:x['proofs'][m]['measurement']['path'] for m in ('native','not-or')})
            for x in cert['exports']])
    cert['metadata']=dict(complete_interface=metadata,bytes=len(json.dumps(metadata).encode('ascii')),
        original_source_optional_bytes=len(inp_path.read_bytes())+
            sum(x['measurements']['native']['bytes'] for x in cert['optional']),
        optional_path_framing_bytes=len(json.dumps(cert['original_received']).encode('ascii')),
        separate_library_bytes={name:{m:sum(x['measurements'][m]['bytes'] for x in lib.values())
            for m in ('native','not-or')} for name,lib in cert['libraries'].items()},
        qualification='Source/import/receiving/export paths and roots are paid interface metadata; complete stream bounds already pay proof headers and references. Shared fixed laws counted twice.')


def source_thresholds(source, optional, libraries):
    """Equation (1), separate arithmetic from the comparison below."""
    assert source == dict(tree=['var',0],letters=['x'],q='q',delete_zero=False)
    U,depth=actual.validate_input(source,depth_factor=4)
    N,n=2*U,len(source['letters']); cs=independent.constants(libraries['source'])
    B=max(1,len(source['q']),*[len(x) for x in source['letters']],
          *[x['name_bytes'] for x in optional],
          *[x['name_bytes'] for lib in libraries.values() for x in lib.values()])
    H=2*depth+ceil_log(n+2)+8; T=1000*(n+2); G=(cs['L']+1)*T
    J=sum(x['measurements']['native']['lines'] for x in optional)+G
    P=48*4**(H+1); F=256+64*ceil_log(J+2)
    bound=dict(U=U,source_depth=depth,N=N,n=n,H=H,operations=T,
               generated_records=G,argument_nodes=P,formats={})
    for m,c in zip(('native','not-or'),(3,6)):
        K=sum(x['node_sums'][m] for x in optional)
        delta=max(x['depths'][m] for x in optional)
        D,S=cs[m]['D'],cs[m]['S']
        size=(B+4)*K+(B+4)*(G+1)*S*P+(J+2)*F
        bound['formats'][m]=dict(lines=J,depth=max(delta,D+c*H+3),
            record_nodes=max(K,S*P),bytes=size,aggregate_bytes=N*size,aggregate_bits=8*N*size)
    return bound


def main():
    paths_out = [OUT / ('actual-224-coordinate-' + str(v) + '.' + m + '.jsonl.gz')
                 for v in range(2) for m in ('native', 'not-or')]
    source_out=[SOURCE/'variable-leaf-224.input.json']+[SOURCE/('variable-leaf-224-v'+str(v)+'.'+m+'.jsonl.gz') for v in range(2) for m in ('native','not-or')]
    all_out=[DEST]+paths_out+source_out
    sidecars=[p.with_name(p.name+'.writer.json') for p in paths_out+source_out[1:]]
    assert not any(p.exists() for p in all_out+sidecars), 'preserve earlier artifacts'
    cert = dict(step=224, complete=False, failures=[], phase='source-reception', exports=[], optional=[])
    save = lambda: r.save(DEST, cert)
    save()
    try:
        inp_path = SOURCE / 'variable-leaf-224.input.json'
        source=dict(tree=['var',0],letters=['x'],q='q',delete_zero=False)
        data=actual.construct(source,depth_factor=4)
        inp=dict(source=source,edges=data['edges'],request=data['request'])
        inp_path.write_text(json.dumps(inp,indent=2)+'\n'); d=inp['request']
        verify=h.module('reception224_contract',SOURCE.parent/'verify.py')
        goals=verify.contract(source,inp['edges'],d); exact=exact_variable(inp)
        assert goals==exact['local']; cert['independent_endpoints']=exact
        previous=r.strict_read((SOURCE/'audit-214.json').read_bytes())
        assert previous['complete'] and previous['failures']==[]
        initial=r.strict_read((OUT/'certificate-202.json').read_bytes())
        libraries=replay_libraries(previous,initial); cert['libraries']=libraries
        source_constants=independent.constants(libraries['source'])
        closure_constants=independent.constants(libraries['closure'])
        assert closure_constants==initial['constants']
        cert['constants']=dict(source=source_constants,closure=closure_constants)
        original=[]; optional_packages=[]
        for i in range(2):
            path=SOURCE/('retained-'+str(i)+'.native.jsonl.gz')
            term='unused'
            for _ in range(35 if i else 0): term=independent.neg(term)
            goal=independent.I(term,term)
            got=r.scan(r.f.FastSyntax,path,goal)
            assert compact(got)==previous['inputs'][i]
            original.append((path,len(got['rows'])))
            cert['optional'].append(compact(got))
            optional_packages.append(actual.b.aggregate.load(path,goal))
        source_bound=source_thresholds(source,cert['optional'],libraries)
        cert.update(original_input=str(inp_path.relative_to(ROOT)),
            original_input_sha256=hashlib.sha256(inp_path.read_bytes()).hexdigest(),
            original_received=[dict(path=str(p.relative_to(ROOT)),lines=n) for p,n in original],
            source_bound=source_bound,phase='local-production')
        save()
        source_lib={law:actual.b.aggregate.load(ROOT/entry['measurements']['native']['path'],goal)
                    for law,goal in independent.fixed()[0].items()
                    for entry in [libraries['source'][law]]}
        paths=[SOURCE/('variable-leaf-224-v'+str(v)+'.native.jsonl.gz') for v in range(2)]
        source_checks=[]; cert['local_production']=[]
        for v,path in enumerate(paths):
            o=actual.b.Store(source_lib,source['q'])
            assert not o.law_cache, 'fresh source store/cache'
            for i,package in enumerate(optional_packages): o.retain(package,'retained-'+str(i))
            info=actual.local(o,data,v); assert info['expected']==goals[v]
            image=path.with_name(path.name.replace('.native.','.not-or.'))
            cert.update(phase='local-write',active_coordinate=v,active_root=o.root); save()
            writers={m:f.write(o,p,im) for m,p,im in [('native',path,False),('not-or',image,True)]}
            cert['phase']='local-replay'; save()
            got=r.scan(r.f.FastSyntax,path,goals[v],image,imports=original)
            for m in ('native','not-or'):
                measures=got['measurements'][m]; required=source_bound['formats'][m]
                assert all(writers[m][key]==measures[key] for key in ('lines','bytes','sha256'))
                assert o.root==measures['lines']-1
                for key,load in [('lines','lines'),('bytes','bytes'),('max_record_nodes','record_nodes')]:
                    assert measures[key]<=required[load],(v,m,key)
                assert got['depths'][m]<=required['depth']
            assert info['law_calls']<=source_bound['operations']
            syntax=r.f.FastSyntax()
            try:
                stats=[syntax.stats[syntax.parse(s)] for call in o.calls for s in call['arguments'].values()]
                args={}
                for m,off,c in [('native',0,3),('not-or',2,6)]:
                    nodes=max(x[off] for x in stats); depth=max(x[off+1] for x in stats)
                    assert nodes<=source_bound['argument_nodes'] and depth<=c*source_bound['H']+3
                    args[m]=dict(nodes=nodes,depth=depth)
            finally: syntax.close()
            source_checks.append(compact(got))
            cert['local_production'].append(dict(v=v,info=info,arguments=args,writers=writers))
            cert['source_packages']=source_checks; save()
            print('PASS fresh variable local pair',v,len(got['rows']),'records',
                  'bytes',got['measurements']['native']['bytes'],'/',source_bound['formats']['native']['bytes'],flush=True)
        cert['source_aggregate']={}
        for m in ('native','not-or'):
            size=sum(x['measurements'][m]['bytes'] for x in source_checks)
            assert size<=source_bound['formats'][m]['aggregate_bytes']
            cert['source_aggregate'][m]=dict(bytes=size,required_bytes=source_bound['formats'][m]['aggregate_bytes'])
        cert['phase']='closure-reception'; save()
        lib=f.library(initial)
        obj = h.lc.Closure(d, paths, lib)
        assert not obj.law_cache, 'fresh closure cache'
        terms = {m: h.suite.measured_terms(d, m) for m in ('native', 'not-or')}
        bound = h.lc.thresholds(d, obj.packages, initial['constants'], terms,
                              max(a['name_bytes'] for a in lib.values()))
        # Independently replayed input measurements must be the paid inputs.
        assert bound['imported_records'] == sum(a['measurements']['native']['lines'] for a in source_checks)
        for m in terms:
            assert bound['formats'][m]['imported_nodes'] == sum(a['node_sums'][m] for a in source_checks)
            assert bound['formats'][m]['imported_depth'] == max(a['depths'][m] for a in source_checks)
        # Source-only majorant: L066's bound, not measured/generated exports.
        source_payload = max([1,len(inp['source']['q'])]+[len(x) for x in inp['source']['letters']]+
            [a['name_bytes'] for a in previous['inputs']]+
            [a['name_bytes'] for a in previous['library'].values()]+
            [a['name_bytes'] for a in lib.values()])
        assert bound['formats']['native']['payload_bytes'] <= source_payload
        majorant_packages = [dict(rows=range(source_bound['formats']['native']['lines']),
            node_sums={m: source_bound['formats'][m]['bytes'] for m in terms},
            depths={m: source_bound['formats'][m]['depth'] for m in terms},
            name_bytes=source_payload) for _ in range(d['N'])]
        composed = h.lc.thresholds(d, majorant_packages, initial['constants'], terms,
                                  max(a['name_bytes'] for a in lib.values()))
        for m in terms:
            for key in ('lines', 'depth', 'record_nodes', 'bytes', 'aggregate_bytes'):
                assert bound['formats'][m][key] <= composed['formats'][m][key]
        independent_ledgers(cert, inp, initial, source_checks, libraries, bound, source_bound, composed)
        cert.update(uniform_ledger=bound, source_bound=source_bound,
                    composed_source_majorant=composed, imports=obj.imports, phase='compile')
        save()
        chain = h.module('reception224_chain', ROOT / 'scripts/backward-zero/chain.py')
        receiving = {k: d[k] for k in ('N','n','q','suffixes','letters')}
        receiving.update(beta=obj.tables['beta'], G=obj.tables['G'], levels=[dict(k=0,R=[],T=[])])
        expected = chain.validate(receiving)
        assert expected == [h.ep.e.c.serialize(g) for g in obj.tables['closed']]
        assert obj.tables['K'] == exact['K'] and obj.tables['beta'] == [[0],[1]]
        assert obj.tables['G'] == exact['receiving']['G'] and expected == exact['coordinates']
        assert receiving == exact['receiving']
        cert['receiving'] = receiving
        for v in range(d['N']):
            print('compile variable-leaf coordinate', v, flush=True)
            obj.row(v)
            assert obj.root == len(obj.p.rows)-1
            cert.update(phase='write', active_coordinate=v, active_root=obj.root)
            save()
            writers = {}; streams = []
            for m, image in [('native', False), ('not-or', True)]:
                path = OUT / ('actual-224-coordinate-' + str(v) + '.' + m + '.jsonl.gz')
                writers[m] = f.write(obj, path, image); streams.append(path)
            cert['phase'] = 'replay'; save()
            checked = r.scan(r.f.FastSyntax, streams[0], expected[v], streams[1],
                roots={root: expected[w] for w, root in enumerate(obj.coordinate_roots)},
                imports=[(path, len(pkg['rows'])) for path, pkg in zip(paths,obj.packages)])
            export = dict(coordinate=v, root=obj.root, endpoint=expected[v],
                          complete_input_retention=True, literal_image=True, proofs={})
            for m in writers:
                measured = checked['measurements'][m]
                assert all(writers[m][k] == measured[k] for k in ('bytes','lines','sha256'))
                assert obj.root == measured['lines']-1
                checks = h.ledger.check(measured,bound['formats'][m])
                assert checked['depths'][m] <= bound['formats'][m]['depth']
                export['proofs'][m] = dict(measurement=measured, uniform_checks=checks,
                    full_field_depth=checked['depths'][m], writer_matches=True)
                print(v,m,'lines',measured['lines'],'/',bound['lines'],
                      'bytes',measured['bytes'],'/',bound['formats'][m]['bytes'],flush=True)
            cert['exports'].append(export); save()
        assert obj.max_argument_height <= bound['H']
        assert all(t['max_height'] <= bound['H'] for t in obj.traces)
        syntax = r.f.FastSyntax()
        try:
            cert['argument_checks'] = {}
            for m, offset in [('native',0),('not-or',2)]:
                stats = [syntax.stats[syntax.parse(s)] for call in obj.calls for s in call['arguments'].values()]
                nodes=max([s[offset] for s in stats]+[0]); depth=max([s[offset+1] for s in stats]+[0])
                assert nodes<=bound['formats'][m]['argument_nodes'] and depth<=bound['formats'][m]['argument_depth']
                cert['argument_checks'][m]=dict(nodes=nodes,depth=depth)
        finally: syntax.close()
        cert['aggregate'] = {}
        for m in terms:
            size=sum(e['proofs'][m]['measurement']['bytes'] for e in cert['exports'])
            lines=sum(e['proofs'][m]['measurement']['lines'] for e in cert['exports'])
            assert lines<=bound['aggregate_lines'] and size<=bound['formats'][m]['aggregate_bytes']
            cert['aggregate'][m]=dict(lines=lines,required_lines=bound['aggregate_lines'],bytes=size,
                required_bytes=bound['formats'][m]['aggregate_bytes'],
                composed_required_bytes=composed['formats'][m]['aggregate_bytes'])
            print(m,'aggregate bytes',size,'/',bound['formats'][m]['aggregate_bytes'],flush=True)
        check_prefix_and_metadata(cert, inp_path, inp, paths)
        cert.update(complete=True,phase='complete',max_argument_height=obj.max_argument_height)
        save(); print('PASS two full pairs; failures',cert['failures'],'certificate',DEST.relative_to(ROOT),flush=True)
    except BaseException as exc:
        cert['failures'].append(type(exc).__name__+': '+str(exc)); save(); raise



if __name__ == '__main__':
    assert not sys.argv[1:], 'one bounded construction only'
    main()
