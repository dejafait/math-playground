"""Read-only audit of preserved step-232 streams; fresh certificates only.

--source replays the inspected step-218 source audit into a fresh destination.
Default audits the joined archive and changed importer, using that fresh replay.
No source/local/coordinate/chain proof archive is generated or changed.
"""
import gzip
import hashlib
import json
import sys
import actual_zero_232 as driver

r, ROOT, MODES = driver.r, driver.ROOT, driver.MODES
up = driver.independent  # inspected archive-only audit_218 implementation
OUT = ROOT/'scripts/backward-zero/output/audit-234'
OLD = ROOT/'scripts/backward-zero/output/actual-zero-232-r1'


def read(path): return r.strict_read(path.read_bytes())
def compact(value): return up.compact(value)
def size(value): return len(json.dumps(value, separators=(',', ':')).encode('ascii'))


def source():
    OUT.mkdir(exist_ok=True)
    up.DEST = OUT/'source-replay.json'
    up.main()


def term_statistics():
    """Check the numerical prose discrepancy against full literal syntax."""
    dest=OUT/'term-statistics.json'
    assert not dest.exists(), 'preserve evidence'
    cert=dict(complete=False,failures=[],terms={})
    try:
        I,N,P=up.I,up.neg,up.P
        y=I('q','q'); z=N(y); s=P(z,y)
        syntax=r.a.Syntax()
        for name,t in [('S0',s),('S1',y),('Y',y),('Z',z)]:
            node=syntax.parse(t); cert['terms'][name]={}
            for m,image in [('native',False),('not-or',True)]:
                literal=syntax.text(node,image)
                _,nodes,depth=driver.b.checker.parse(literal,m)
                cert['terms'][name][m]=dict(literal=literal,nodes=nodes,depth=depth)
        maxima={m:dict(nodes=max(x[m]['nodes'] for x in cert['terms'].values()),
                       depth=max(x[m]['depth'] for x in cert['terms'].values())) for m in MODES}
        assert maxima=={'native':dict(nodes=10,depth=4),'not-or':dict(nodes=13,depth=6)}
        old=read(OLD/'certificate.json')
        H=old['direct_chain_ledger']['H']
        for m,factor in zip(MODES,(3,6)):
            bound=old['direct_chain_ledger']['formats'][m]
            assert bound['argument_depth']==factor*H+maxima[m]['depth']
            assert bound['argument_nodes']==8*4**(H+1)*(maxima[m]['nodes']+1)
            closure=old['closure_source_bound']['formats'][m]
            assert closure['input_term_nodes']==maxima[m]['nodes']
            assert closure['input_term_depth']==maxima[m]['depth']
        cert.update(complete=True,maxima=maxima,old_prose_image=dict(nodes=14,depth=5),
                    effect='Numerical prose correction only: both preserved executable ledgers already use 13 nodes and depth 6; all bounds and streams unchanged.')
    except BaseException as exc:
        cert['failures'].append(dict(type=type(exc).__name__,message=str(exc))); raise
    finally:
        dest.write_text(json.dumps(cert,indent=2)+'\n')
    print('PASS native nodes/depth 10/4, image 13/6; preserved ledgers agree; failures',
          cert['failures'],'certificate',dest.relative_to(ROOT),flush=True)


def main():
    dest = OUT/'certificate.json'
    assert not dest.exists(), 'preserve audit evidence'
    cert = dict(step=234, complete=False, failures=[], phase='source-linkage')
    def save(): dest.write_text(json.dumps(cert, indent=2)+'\n')
    save()
    try:
        fresh = read(OUT/'source-replay.json')
        assert fresh['complete'] and fresh['failures'] == []
        oldraw = (OLD/'certificate.json').read_bytes()
        old = r.strict_read(oldraw)
        supraw = (OLD/'source-interface-ledger.json').read_bytes()
        supplement = r.strict_read(supraw)
        prov = old['provenance']
        for key in ('input', 'table', 'prior'):
            assert hashlib.sha256((ROOT/prov[key]).read_bytes()).hexdigest() == prov[key+'_sha256']
        inp, table, prior = [read(ROOT/prov[key]) for key in ('input', 'table', 'prior')]
        driver.tablecheck.check(table)
        I, N, X, E, P = up.I, up.neg, up.X, up.E, up.P
        y = I('q', 'q'); z = N(y); suffixes = [P(z,y), y]
        levels = [dict(k=1,R=[[1,0]],T=[[]]), dict(k=0,R=[],T=[]), dict(k=0,R=[],T=[])]
        data = dict(N=2,n=0,q='q',suffixes=suffixes,letters=[],beta=[[0],[1]],G=[],levels=levels)
        assert inp['source'] == dict(tree=['zero'],letters=[],q='q',delete_zero=True)
        assert table['source'] == inp['source'] and table['depth_factor'] == 4
        assert table['K'] == [[1,0],[0,1]] and table['chain'] == data == prov['receiving']
        assert read(OLD/'request.json') == data
        goals = [E(suffixes[0],X(z,z)), E(y,X(y,z))]
        final = E(suffixes[0],z)
        assert prov['exact_coordinate_endpoints'] == goals and prov['exact_source_row_endpoint'] == final
        assert driver.chain.validate(data) == goals
        assert old['source_bound'] == fresh['source_bound']
        assert old['closure_source_bound'] == fresh['composed_source_majorant']
        cert['source_replay'] = 'scripts/backward-zero/output/audit-234/source-replay.json'
        cert['source_replay_sha256'] = hashlib.sha256((OUT/'source-replay.json').read_bytes()).hexdigest()
        cert['endpoints'] = dict(coordinates=goals,row=[final,E(z,z),E(z,z),final],receiving=data)

        # Recover locations from complete fresh counts, not saved offsets.
        paths = [ROOT/x['full']['measurements']['native']['path'] for x in fresh['exports']]
        images = [ROOT/x['full']['measurements']['not-or']['path'] for x in fresh['exports']]
        assert [str(p.relative_to(ROOT)) for p in paths] == prov['coordinate_paths']
        imports=[]; offset=0
        for v,entry in enumerate(fresh['exports']):
            count=entry['full']['measurements']['native']['lines']
            imports.append(dict(label='coordinate-'+str(v),start=offset,lines=count,root=offset+count-1))
            offset+=count
        assert imports == old['imports'] and offset == 361432
        locations=read(OLD/'locations.json')
        assert locations['coordinate_imports'] == imports and locations['levels'] == [1,0,0]
        assert len(locations['rows']) == len(old['rows']) == 1
        loc=locations['rows'][0]; row=old['rows'][0]
        assert loc == {k:row[k] for k in ('level','row','start','end','required_roots')}
        assert (loc['level'],loc['row'],loc['start'],loc['end']) == (0,0,offset,377087)
        assert row['next_roots'] == []
        roots=loc['required_roots']
        assert roots == [375610,375631,375633,377086]
        assert all(loc['start'] <= j < loc['end'] for j in roots)
        assert roots[-1] == loc['end']-1 == old['root']
        requested=dict(zip(roots,cert['endpoints']['row']))
        for imp,goal in zip(imports,goals): requested[imp['root']]=goal
        requested[imports[1]['start']+imports[0]['root']]=goals[0]
        assert {int(k):v for k,v in old['requested_roots'].items()} == requested
        cert.update(imports=imports,locations=locations,requested_roots=requested)

        # Input-defined bounds are computed BEFORE opening the joined proof.
        cc=up.constants({k:v for k,v in fresh['libraries']['closure'].items() if k!='close_cancel'})
        assert cc == old['constants']
        names=max(1, len(data['q']), *[x['name_bytes'] for x in fresh['optional']],
                  *[x['name_bytes'] for lib in fresh['libraries'].values() for x in lib.values()])
        assert names == 6
        packages=[dict(rows=range(x['full']['measurements']['native']['lines']),
                       **{k:x['full'][k] for k in ('node_sums','depths','name_bytes')}) for x in fresh['exports']]
        cb=fresh['composed_source_majorant']
        majors=[dict(rows=range(cb['lines']),node_sums={m:cb['formats'][m]['bytes'] for m in MODES},
                     depths={m:cb['formats'][m]['depth'] for m in MODES},name_bytes=names) for _ in paths]
        direct,dl=driver.auditchain.bounds(data,packages,cc,names)
        composed,cl=driver.auditchain.bounds(data,majors,cc,names)
        for m in MODES:
            for k in composed[m]:
                assert composed[m][k] == old['original_source_chain_ledger']['formats'][m][k]
                assert direct[m][k] == old['direct_chain_ledger']['formats'][m][k]
                assert direct[m][k] <= composed[m][k]
        assert cl == old['original_source_chain_ledger']['metadata_bytes']
        assert dl == old['direct_chain_ledger']['metadata_bytes']
        cert.update(original_source_bounds=composed,locations_bound=cl,direct_bounds=direct,
                    phase='complete-joined-replay')
        save()
        print('Replay joined native/image pair; bounds fixed from original sources',flush=True)
        got=r.scan(r.f.FastSyntax,OLD/'chain.native.jsonl.gz',final,OLD/'chain.not-or.jsonl.gz',
                   roots=requested,imports=[(p,x['lines']) for p,x in zip(paths,imports)])
        assert len(got['rows']) == loc['end']
        ancestor=r.a.ancestors(got['references'],roots[-1])
        assert imports[0]['root'] in ancestor
        for m in MODES:
            measured=got['measurements'][m]
            assert measured == old['proofs'][m]['measurement']
            for k in ('lines','bytes','record_nodes'):
                v=measured['max_record_nodes' if k=='record_nodes' else k]
                assert v <= direct[m][k] <= composed[m][k]
            assert got['depths'][m] <= direct[m]['depth'] <= composed[m]['depth']
            print('PASS',m,'records',measured['lines'],'<=',composed[m]['lines'],
                  'bytes',measured['bytes'],'<=',composed[m]['bytes'],
                  'full depth',got['depths'][m],'<=',composed[m]['depth'],flush=True)
        cert.update(joined=compact(got),source_coordinate_in_final_ancestry=imports[0]['root'],
                    phase='immutable-import-and-prefix')
        save(); del got

        # Exercise changed parsing and empty-map copy in a fresh import-only
        # store. Compare EVERY converted formula/substitution/rule/reference
        # back to its complete original serialization before retaining it.
        store=object.__new__(driver.ExactImportChain)
        driver.b.Store.__init__(store,{})
        cert['immutable_imports']=[]
        for v,(path,goal) in enumerate(zip(paths,goals)):
            pkg=driver.fast_package(path,goal)
            spell=driver.spelling.Spelling(False)
            with gzip.open(path,'rb') as stream:
                assert r.strict_read(stream.readline()) == dict(format='native',goal=goal)
                for index,(f,rule,refs,subs) in enumerate(pkg['rows']):
                    wanted=dict(f=spell.text(f),rule=rule)
                    if rule=='mp': wanted['refs']=refs
                    else: wanted['subs']={k:spell.text(t) for k,t in subs.items()}
                    assert r.strict_read(stream.readline()) == wanted,(v,index)
                assert not stream.read(1)
            full=fresh['exports'][v]['full']
            for k in ('node_sums','depths','name_bytes'): assert pkg[k] == full[k]
            assert pkg['measurement'] == {k:full['measurements']['native'][k] for k in ('lines','bytes','sha256')}
            root=store.retain(pkg,'coordinate-'+str(v))
            assert root == imports[v]['root'] and store.imports[-1] == imports[v]
            cert['immutable_imports'].append(dict(coordinate=v,records=len(pkg['rows']),root=root,
                every_converted_field_equal=True,exact_empty_substitution_retention=True))
            save(); del pkg,spell
            print('PASS complete immutable import and empty-map retention',v,flush=True)
        assert len(store.p.rows) == offset; del store
        cert['prefix']={}
        for m,ps in zip(MODES,(paths,images)):
            count=total=0; digest=hashlib.sha256()
            with gzip.open(ps[0],'rb') as first,gzip.open(ps[1],'rb') as second:
                first.readline(); second.readline()
                for raw in first:
                    assert raw == second.readline(),(m,count)
                    count+=1; total+=len(raw); digest.update(raw)
                assert second.readline()
            assert count == imports[0]['lines']
            cert['prefix'][m]=dict(records=count,bytes=total,sha256=digest.hexdigest())
        cert['phase']='source-interface-ledger'; save()

        # Each interface component is compared with its charged original or
        # independently checked subobject. Finite measurements set no bound.
        ac=old['original_input_accounting']
        interface=ac['complete_interface']
        coordpaths=[dict(native=str(p.relative_to(ROOT)),image=str(im.relative_to(ROOT)))
                    for p,im in zip(paths,images)]
        assert interface == dict(source=inp,optional=prior['original_received'],receiving=table['chain'],
                                 coordinates=coordpaths,locations=locations)
        tablebound=2**30*(len(json.dumps(table['source'],separators=(',',':')).encode('ascii'))+2)**28
        assert tablebound == table['ledger']['original_source_byte_bound'] == ac['table_required_bytes']
        framing=len(json.dumps(prior['original_received']).encode('ascii'))
        charges=dict(original_source_bytes=(ROOT/prov['input']).stat().st_size,
                     optional_framing_bytes=framing,coefficient_certificate_bound=tablebound,
                     original_coordinate_path_bytes=size(coordpaths),source_bounded_locations_bytes=cl,
                     outer_framing_bytes=1024)
        assert charges == supplement['interface_input_charges']
        required=sum(charges.values()); actual=size(interface)
        assert actual == ac['interface_bytes'] == supplement['interface_actual_bytes'] <= required
        assert required == supplement['interface_required_bytes']
        assert size(table['chain']) <= (ROOT/prov['table']).stat().st_size <= tablebound
        assert size(inp) <= charges['original_source_bytes']
        assert size(prior['original_received']) <= framing
        assert size(locations) <= (OLD/'locations.json').stat().st_size <= cl
        # Native optional blocks have no separately supplied images. Literal
        # images of all nested copies were checked transitively in paired scans.
        nested=[]
        for v,ci in enumerate(imports):
            for u,li in enumerate(fresh['imports']):
                start=ci['start']+li['start']
                for opt,entry in enumerate(fresh['optional']):
                    n=entry['measurements']['native']['lines']
                    assert n == prior['original_received'][opt]['lines'] == 5
                    nested.append(dict(coordinate=v,local=u,optional=opt,start=start,lines=n,end=start+n))
                    start+=n
        assert nested == supplement['nested_optional_occurrences']
        assert len(nested)==8 and sum(x['lines'] for x in nested)==40
        libbytes={name:{m:sum(x['measurements'][m]['bytes'] for x in lib.values()) for m in MODES}
                  for name,lib in fresh['libraries'].items()}
        libbytes['chain']={m:sum(x['measurements'][m]['bytes'] for k,x in fresh['libraries']['closure'].items()
                               if k!='close_cancel') for m in MODES}
        assert libbytes == ac['fixed_library_bytes']
        libtotal=sum(sum(x.values()) for x in libbytes.values())
        totalbound=sum(composed[m]['bytes']+cl for m in MODES)+tablebound+required+libtotal
        totalactual=sum(cert['joined']['measurements'][m]['bytes']+(OLD/'locations.json').stat().st_size for m in MODES)
        totalactual+=(ROOT/prov['table']).stat().st_size+actual+libtotal
        assert totalactual == supplement['full_output_actual_bytes'] <= totalbound
        assert totalbound == supplement['full_output_source_required_bytes']
        assert supplement['replay_certificate_sha256'] == hashlib.sha256(oldraw).hexdigest()
        cert.update(interface_charges=charges,interface_actual=actual,interface_required=required,
                    nested_optional_occurrences=nested,library_bytes=libbytes,
                    total_actual=totalactual,total_required=totalbound)
        assert (OLD/'certificate.json').read_bytes() == oldraw
        assert (OLD/'source-interface-ledger.json').read_bytes() == supraw
        cert.update(complete=True,phase='complete',verdict='Exact conditional empty-zero joined interface passes.',
                    limitations='Finite fixture plus separately inspected polynomial composition; no historical call trace reconstruction, initial-output identification, nonzero reception, whole L055, ordinary-input completeness, certificate existence or SAT verdict.')
        save()
        print('PASS interface',actual,'<=',required,'bytes; total',totalactual,'<=',totalbound,
              'bytes; optional records',40,'failures',cert['failures'],'certificate',dest.relative_to(ROOT),flush=True)
    except BaseException as exc:
        cert['failures'].append(dict(type=type(exc).__name__,message=str(exc)))
        save(); raise


if __name__=='__main__':
    if sys.argv[1:]==['--source']: source()
    elif sys.argv[1:]==['--term-statistics']: term_statistics()
    else: main()
