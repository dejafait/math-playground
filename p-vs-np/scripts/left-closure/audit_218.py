"""Archive-only independent reception/ledger audit; never constructs proofs."""
import gzip
import hashlib
import json
import sys
from pathlib import Path
import replay_star as r

h, ROOT, OUT = r.h, r.ROOT, r.OUT
SOURCE = ROOT / 'scripts/actual-tree/output'
DEST = OUT / 'audit-218.json'
MODES = ('native', 'not-or')


def compact(x):
    return {k: v for k, v in x.items() if k not in ('rows', 'references')}


def I(a, b): return '(' + a + '>' + b + ')'
def neg(a): return '(~' + a + ')'
def X(a, b): return I(I(a, b), neg(I(b, a)))
def E(a, b): return neg(X(a, b))
def P(a, b): return neg(I(a, neg(b)))


def fixed():
    a, b, c = 'A', 'B', 'C'
    y = I('q', 'q'); z = neg(y)
    common = dict(refl=E(a,a), symm=I(E(a,b),E(b,a)),
        trans=I(E(a,b),I(E(b,c),E(a,c))),
        congL=I(E(a,b),E(X(a,c),X(b,c))),
        congR=I(E(a,b),E(X(c,a),X(c,b))),
        zeroL=E(X(z,a),a), zeroR=E(X(a,z),a), prod_zero=E(P(a,z),z))
    source = dict(common, prod_assoc=E(P(P(a,b),c),P(a,P(b,c))),
        right_dist=E(P(X(a,b),c),X(P(a,c),P(b,c))),
        unitL=E(P(y,a),a), unitR=E(P(a,y),a), zero_prodL=E(P(z,a),z))
    closure = dict(common, assoc=E(X(X(a,b),c),X(a,X(b,c))),
        comm=E(X(a,b),X(b,a)), cancel=E(X(a,a),z), zero_slots=E(z,X(z,z)),
        dist=E(P(a,X(b,c)),X(P(a,b),P(a,c))),
        prod_cong=I(E(b,c),E(P(a,b),P(a,c))),
        close_cancel=I(E(a,X(a,X(b,c))),E(b,c)))
    return source, closure


def constants(lib):
    return dict(L=max(x['measurements']['native']['lines'] for x in lib.values()),
        **{m:dict(D=max(x['depths'][m] for x in lib.values()),
                  S=max(x['measurements'][m]['max_record_nodes'] for x in lib.values()))
           for m in MODES})


def ledger(N, n, I0, K, delta, B, terms, lib):
    # Equation (4), independently written; never calls constructor thresholds.
    hh = (N+n+1).bit_length(); V = 2**(3*hh+6); H = 9*hh+30
    T = 10000*N*V*V*(H+1)**2; G = (lib['L']+1)*T; J = I0+G
    ans = dict(h=hh,V=V,H=H,elementary_operations=T,generated_records=G,
        imported_records=I0,lines=J,aggregate_lines=N*J,formats={})
    for m, factor in zip(MODES,(3,6)):
        t,d = terms[m]; S,D = lib[m]['S'],lib[m]['D']
        pp = 8*4**(H+1)*(t+1)
        size = (B+4)*(K[m]+(G+1)*S*pp)+(J+2)*(256+64*(J+1).bit_length())
        ans['formats'][m] = dict(lines=J,depth=max(delta[m],D+factor*H+d),
            record_nodes=max(K[m],S*pp),bytes=size,bits=8*size,
            aggregate_bytes=N*size,aggregate_bits=8*N*size,
            argument_nodes=pp,argument_depth=factor*H+d,input_term_nodes=t,
            input_term_depth=d,imported_nodes=K[m],imported_depth=delta[m],payload_bytes=B)
    return ans


def main():
    assert not DEST.exists(), 'preserve previous audit evidence'
    cert = dict(step=218,complete=False,failures=[],libraries={},optional=[],local=[],exports=[])
    def save(): r.save(DEST,cert)
    save()
    preserved = OUT/'reception-216.json'
    original_bytes = preserved.read_bytes()
    cert['preserved_certificate_sha256'] = hashlib.sha256(original_bytes).hexdigest()
    try:
        old = r.strict_read(original_bytes)
        prior = r.strict_read((SOURCE/'audit-214.json').read_bytes())
        initial = r.strict_read((OUT/'certificate-202.json').read_bytes())
        inp_path = SOURCE/'empty-zero-repaired.input.json'
        raw = inp_path.read_bytes(); inp = r.strict_read(raw); d = inp['request']
        assert hashlib.sha256(raw).hexdigest() == old['original_input_sha256']
        y = I('q','q'); z = neg(y); suffixes = [P(z,y),y]
        assert inp == dict(source=dict(tree=['zero'],letters=[],q='q',delete_zero=True),
            edges=[],request=dict(N=2,n=0,t=1,q='q',suffixes=suffixes,
                letters=[],E0=[[0,0],[0,0]],Eb=[]))
        local_goals = [E(suffixes[v],X(z if v==0 else y,X(z,z))) for v in range(2)]
        goals = [E(suffixes[v],X(z if v==0 else y,z)) for v in range(2)]
        receiving = dict(N=2,n=0,q='q',suffixes=suffixes,letters=[],
            beta=[[0],[1]],G=[],levels=[dict(k=0,R=[],T=[])])
        assert old['receiving'] == receiving
        # Syntax validation only; no ChainStore or row/constructor execution.
        chain = h.module('audit218_chain', ROOT/'scripts/backward-zero/chain.py')
        assert chain.validate(receiving) == goals
        assert [h.ep.e.c.serialize(g) for g in h.ep.request(d)['local']] == local_goals
        cert['endpoints'] = dict(local=local_goals,coordinates=goals,receiving=receiving)
        for name, endpoint_map in zip(('source','closure'),fixed()):
            lib = {}; cert['libraries'][name] = lib
            for law,goal in endpoint_map.items():
                saved = prior['library'][law]['measurements'] if name=='source' else initial['library'][law]
                got = r.scan(r.f.FastSyntax,ROOT/saved['native']['path'],goal,
                             ROOT/saved['not-or']['path'])
                for m in MODES:
                    for k,v in got['measurements'][m].items(): assert saved[m][k]==v,(name,law,m,k)
                lib[law] = compact(got); save()
            print('PASS full fixed library',name,len(lib),'pairs',flush=True)
        cs,cc = [constants(cert['libraries'][k]) for k in ('source','closure')]
        assert cs == dict(L=2567,native=dict(D=18,S=2040),**{'not-or':dict(D=24,S=2712)})
        assert cc == dict(L=3470,native=dict(D=19,S=2456),**{'not-or':dict(D=27,S=3492)})
        cert['constants'] = dict(source=cs,closure=cc)
        optional_imports = []
        for i,depth in enumerate((0,35)):
            term='unused'
            for _ in range(depth): term=neg(term)
            path=SOURCE/('retained-'+str(i)+'.native.jsonl.gz')
            got=r.scan(r.f.FastSyntax,path,I(term,term))
            assert compact(got)==prior['inputs'][i]
            cert['optional'].append(compact(got)); optional_imports.append((path,len(got['rows'])))
        imports=[]
        for v,goal in enumerate(local_goals):
            path=SOURCE/('empty-zero-repaired-v'+str(v)+'.native.jsonl.gz')
            got=r.scan(r.f.FastSyntax,path,goal,path.with_name(path.name.replace('.native.','.not-or.')),
                       imports=optional_imports)
            assert compact(got)==old['source_packages'][v]
            cert['local'].append(compact(got)); imports.append((path,len(got['rows'])))
            save()
        B=max(1,len(d['q']),*[x['name_bytes'] for x in cert['optional']],
              *[x['name_bytes'] for lib in cert['libraries'].values() for x in lib.values()])
        assert B==6 and all(x['name_bytes']<=B for x in cert['local'])
        # Source equation (1), using optional inputs and separate source library.
        count=sum(x['measurements']['native']['lines'] for x in cert['optional'])
        H=9; T=2000; G=(cs['L']+1)*T; J=count+G; pp=48*4**(H+1)
        sb=dict(U=1,source_depth=0,N=2,n=0,H=H,operations=T,
                generated_records=G,argument_nodes=pp,formats={})
        for m,factor in zip(MODES,(3,6)):
            K=sum(x['node_sums'][m] for x in cert['optional'])
            delta=max(x['depths'][m] for x in cert['optional'])
            S,D=cs[m]['S'],cs[m]['D']
            size=(B+4)*(K+(G+1)*S*pp)+(J+2)*(256+64*(J+1).bit_length())
            sb['formats'][m]=dict(lines=J,depth=max(delta,D+factor*H+3),
                record_nodes=max(K,S*pp),bytes=size,aggregate_bytes=2*size,aggregate_bits=16*size)
            for x in cert['local']:
                assert x['node_sums'][m]<=x['measurements'][m]['bytes']<=size
                assert x['measurements'][m]['lines']<=J and x['depths'][m]<=sb['formats'][m]['depth']
        assert sb==old['source_bound']
        syntax=r.f.FastSyntax()
        try:
            stats=[syntax.stats[syntax.parse(s)] for s in suffixes+[y,z]]
            terms={m:(max(s[off] for s in stats),max(s[off+1] for s in stats))
                   for m,off in zip(MODES,(0,2))}
        finally: syntax.close()
        bound=ledger(2,0,sum(n for _,n in imports),
            {m:sum(x['node_sums'][m] for x in cert['local']) for m in MODES},
            {m:max(x['depths'][m] for x in cert['local']) for m in MODES},B,terms,cc)
        composed=ledger(2,0,2*J,{m:2*sb['formats'][m]['bytes'] for m in MODES},
            {m:sb['formats'][m]['depth'] for m in MODES},B,terms,cc)
        assert bound==old['uniform_ledger'] and composed==old['composed_source_majorant']
        cert.update(source_bound=sb,uniform_ledger=bound,composed_source_majorant=composed)
        actual_imports=[]; offset=0
        for v,(_,n) in enumerate(imports):
            actual_imports.append(dict(label='local-'+str(v),start=offset,lines=n,root=offset+n-1)); offset+=n
        assert actual_imports==old['imports']
        cert['imports']=actual_imports; save()
        roots={}
        for v,goal in enumerate(goals):
            paths=[OUT/('actual-216-coordinate-'+str(v)+'.'+m+'.jsonl.gz') for m in MODES]
            print('Replaying complete coordinate pair',v,flush=True)
            # Saved root is only a requested location, checked against fresh EOF/count below.
            roots[old['exports'][v]['root']]=goal
            got=r.scan(r.f.FastSyntax,paths[0],goal,paths[1],roots=roots,imports=imports)
            assert len(got['rows'])-1==old['exports'][v]['root']
            for m in MODES:
                measured=got['measurements'][m]; saved=old['exports'][v]['proofs'][m]['measurement']
                assert measured==saved
                assert got['depths'][m]<=bound['formats'][m]['depth']
                for key in ('lines','bytes','record_nodes'):
                    value=measured['max_record_nodes' if key=='record_nodes' else key]
                    assert value<=bound['formats'][m][key]<=composed['formats'][m][key]
                print(v,m,'lines',measured['lines'],'/',bound['lines'],
                    'bytes',measured['bytes'],'/',composed['formats'][m]['bytes'],flush=True)
            cert['exports'].append(dict(coordinate=v,root=len(got['rows'])-1,full=compact(got),
                complete_imports=True,literal_image=True,earlier_coordinate_roots=dict(roots)))
            save()
        cert['aggregate']={}
        for m in MODES:
            size=sum(x['full']['measurements'][m]['bytes'] for x in cert['exports'])
            lines=sum(x['full']['measurements'][m]['lines'] for x in cert['exports'])
            assert size==old['aggregate'][m]['bytes']<=composed['formats'][m]['aggregate_bytes']
            assert lines<=composed['aggregate_lines']
            cert['aggregate'][m]=dict(bytes=size,required_bytes=composed['formats'][m]['aggregate_bytes'],
                lines=lines,required_lines=composed['aggregate_lines'])
        native_input=len(raw)+sum(x['measurements']['native']['bytes'] for x in cert['optional'])
        framing=len(json.dumps(old['original_received']).encode('ascii'))
        assert (native_input,framing)==(4979,158)
        metadata=dict(source=inp,original_received=old['original_received'],imports=actual_imports,
            receiving=receiving,exports=[dict(coordinate=v,root=x['root'],
                paths={m:x['full']['measurements'][m]['path'] for m in MODES})
                for v,x in enumerate(cert['exports'])])
        cert['metadata']=dict(complete_interface=metadata,bytes=len(json.dumps(metadata).encode('ascii')),
            original_source_optional_bytes=native_input,optional_path_framing_bytes=framing,
            source_payload_bytes=B,
            separate_library_bytes={name:{m:sum(x['measurements'][m]['bytes'] for x in lib.values())
                for m in MODES} for name,lib in cert['libraries'].items()},
            qualification='Shared laws counted in both fixed libraries; paths, roots, tables and headers charged. Audit diagnostics are not additional Frege premises.')
        assert preserved.read_bytes()==original_bytes
        cert.update(complete=True,preserved_certificate_unchanged=True,
            verdict='Complete bounded reception and original-source composition pass; no chain or nonzero fixture executed.',
            limitation='Historical constructor call traces were not reconstructed; no whole-L055 or ordinary-input completeness verdict.')
        save()
        print('PASS; failures',cert['failures'],'certificate',DEST.relative_to(ROOT),flush=True)
    except BaseException as exc:
        cert['failures'].append(type(exc).__name__+': '+str(exc)); save(); raise


def prefix_audit():
    """Additional exact prefix check, preserving the completed main audit."""
    dest=OUT/'audit-218-prefix.json'
    assert not dest.exists(), 'preserve previous prefix evidence'
    main_bytes=DEST.read_bytes(); base=r.strict_read(main_bytes)
    assert base['complete'] and base['failures']==[]
    cert=dict(step=218,complete=False,failures=[],formats={},
              replay_certificate_sha256=hashlib.sha256(main_bytes).hexdigest())
    try:
        for m in MODES:
            paths=[ROOT/x['full']['measurements'][m]['path'] for x in base['exports']]
            count=size=0; digest=hashlib.sha256()
            with gzip.open(paths[0],'rb') as first, gzip.open(paths[1],'rb') as second:
                first.readline(); second.readline()  # Distinct audited endpoint headers.
                for raw in first:
                    assert raw==second.readline(), (m,count,'earlier prefix changed')
                    count+=1; size+=len(raw); digest.update(raw)
                assert second.readline(), 'later coordinate has no additional record'
            required=base['exports'][0]['full']['measurements'][m]['lines']
            assert count==required==base['exports'][0]['root']+1
            cert['formats'][m]=dict(records=count,required_records=required,
                record_bytes=size,record_sha256=digest.hexdigest(),byte_identical_prefix=True)
            print('PASS earlier complete prefix',m,count,'/',required,'records',flush=True)
        assert DEST.read_bytes()==main_bytes
        assert hashlib.sha256((OUT/'reception-216.json').read_bytes()).hexdigest()==base['preserved_certificate_sha256']
        cert['complete']=True
    except BaseException as exc:
        cert['failures'].append(type(exc).__name__+': '+str(exc)); raise
    finally: r.save(dest,cert)
    print('PASS; failures',cert['failures'],'certificate',dest.relative_to(ROOT),flush=True)


if __name__=='__main__':
    if sys.argv[1:]==['--prefix-only']: prefix_audit()
    else: main()
