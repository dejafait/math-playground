"""Step-226 archive-only variable reception audit; fresh n=1 ledger arithmetic."""
import gzip
import hashlib
import json
import replay_star as r
from audit_218 import fixed  # Fixed theorem spellings only; no accounting helpers.

ROOT, OUT = r.ROOT, r.OUT
SRC = ROOT/'scripts/actual-tree/output'
DEST = OUT/'audit-226.json'
MODES = ('native','not-or')

def compact(x): return {k:v for k,v in x.items() if k not in ('rows','references')}
def I(a,b): return '('+a+'>'+b+')'
def neg(a): return '(~'+a+')'
def X(a,b): return I(I(a,b),neg(I(b,a)))
def E(a,b): return neg(X(a,b))
def P(a,b): return neg(I(a,neg(b)))
def ceil_log(x):
    power = 1; result = 0
    while power < x: power *= 2; result += 1
    return result

def maxima(lib):
    return dict(L=max(v['measurements']['native']['lines'] for v in lib.values()),
        **{m:dict(D=max(v['depths'][m] for v in lib.values()),
                  S=max(v['measurements'][m]['max_record_nodes'] for v in lib.values())) for m in MODES})

def source_ledger(optional, const, B):
    # L066 (1), with this source's n=1. No imported arithmetic helper.
    n, N, d = 1, 2, 0
    H = 2*d + ceil_log(n+2) + 8
    T = 1000*(n+2)
    G = (const['L']+1)*T
    J = sum(p['measurements']['native']['lines'] for p in optional) + G
    pp = 48*4**(H+1)
    ans = dict(U=1,source_depth=d,N=N,n=n,H=H,operations=T,
               generated_records=G,argument_nodes=pp,formats={})
    for mode,c in zip(MODES,(3,6)):
        K = sum(p['node_sums'][mode] for p in optional)
        delta = max(p['depths'][mode] for p in optional)
        D,S = const[mode]['D'],const[mode]['S']
        imported = (B+4)*K
        generated_and_header = (B+4)*(G+1)*S*pp
        framing = (J+2)*(256+64*ceil_log(J+2))
        bound = imported + generated_and_header + framing
        ans['formats'][mode] = dict(lines=J,depth=max(delta,D+c*H+3),
            record_nodes=max(K,S*pp),bytes=bound,aggregate_bytes=N*bound,
            aggregate_bits=8*N*bound)
    return ans


def closure_ledger(count,nodes,depths,B,terms,const):
    # L065 (4), independently expanded into three separately charged sums.
    N,n = 2,1
    h = ceil_log(2+N+n)
    V = 2**(3*h+6); H = 9*h+30
    T = 10000*N*V**2*(H+1)**2
    G = (const['L']+1)*T; J = count+G
    ans = dict(h=h,V=V,H=H,elementary_operations=T,generated_records=G,
               imported_records=count,lines=J,aggregate_lines=N*J,formats={})
    for mode,c in zip(MODES,(3,6)):
        t,d = terms[mode]; D,S = const[mode]['D'],const[mode]['S']
        pp = 8*4**(H+1)*(t+1)
        bound = ((B+4)*nodes[mode] + (B+4)*(G+1)*S*pp
                 + (J+2)*(256+64*ceil_log(J+2)))
        ans['formats'][mode] = dict(lines=J,depth=max(depths[mode],D+c*H+d),
            record_nodes=max(nodes[mode],S*pp),bytes=bound,bits=8*bound,
            aggregate_bytes=N*bound,aggregate_bits=8*N*bound,
            argument_nodes=pp,argument_depth=c*H+d,input_term_nodes=t,
            input_term_depth=d,imported_nodes=nodes[mode],imported_depth=depths[mode],payload_bytes=B)
    return ans


def main():
    assert not DEST.exists(), 'preserve existing evidence'
    cert=dict(step=226,complete=False,failures=[],phase='inputs',libraries={},optional=[],local=[],exports=[])
    def save(): r.save(DEST,cert)
    cert['driver_sha256']=hashlib.sha256((OUT.parent/'receive_actual_variable_224.py').read_bytes()).hexdigest()
    save()
    oldpath=OUT/'reception-224.json'; oldraw=oldpath.read_bytes(); old=r.strict_read(oldraw)
    cert['preserved_certificate_sha256']=hashlib.sha256(oldraw).hexdigest()
    try:
        assert old['step']==224 and old['complete'] and old['failures']==[] and old['phase']=='complete'
        prior=r.strict_read((SRC/'audit-214.json').read_bytes())
        initial=r.strict_read((OUT/'certificate-202.json').read_bytes())
        inp_path=SRC/'variable-leaf-224.input.json'; raw=inp_path.read_bytes(); inp=r.strict_read(raw)
        y=I('q','q'); z=neg(y); S=[P('x',y),y]
        Eb=[[[0,1],[0,0]]]
        expected_source=dict(source=dict(tree=['var',0],letters=['x'],q='q',delete_zero=False),
            edges=[dict(v=0,w=1,kind='var',position=0)],request=dict(N=2,n=1,t=1,q='q',
            suffixes=S,letters=['x'],E0=[[0,0],[0,0]],Eb=Eb))
        assert inp==expected_source
        assert old['original_input']==str(inp_path.relative_to(ROOT))
        assert hashlib.sha256(raw).hexdigest()==old['original_input_sha256']
        local_goals=[E(S[0],X(z,X(z,P('x',y)))),E(y,X(y,X(z,P('x',z))))]
        goals=[E(S[0],X(z,P('x',y))),E(y,X(y,P('x',z)))]
        receiving=dict(N=2,n=1,q='q',suffixes=S,letters=['x'],beta=[[0],[1]],G=Eb,
                       levels=[dict(k=0,R=[],T=[])])
        exact=dict(local=local_goals,coordinates=goals,K=[[1,0],[0,1]],receiving=receiving)
        assert old['independent_endpoints']==exact and old['receiving']==receiving
        chain=r.h.module('audit226_chain',ROOT/'scripts/backward-zero/chain.py')
        assert chain.validate(receiving)==goals  # Syntax only; no chain execution.
        cert['endpoints']=exact
        for name,goals_fixed in zip(('source','closure'),fixed()):
            lib={}; cert['libraries'][name]=lib
            for law,goal in goals_fixed.items():
                saved=prior['library'][law]['measurements'] if name=='source' else initial['library'][law]
                got=compact(r.scan(r.f.FastSyntax,ROOT/saved['native']['path'],goal,ROOT/saved['not-or']['path']))
                for m in MODES:
                    for key,value in got['measurements'][m].items(): assert saved[m][key]==value,(name,law,m,key)
                assert got==old['libraries'][name][law]
                lib[law]=got; save()
            print('PASS fixed library',name,len(lib),'complete pairs',flush=True)
        constants={name:maxima(lib) for name,lib in cert['libraries'].items()}
        assert constants==old['constants']; cert['constants']=constants
        optional_imports=[]
        for i,depth in enumerate((0,35)):
            term='unused'
            for _ in range(depth): term=neg(term)
            path=SRC/('retained-'+str(i)+'.native.jsonl.gz')
            got=r.scan(r.f.FastSyntax,path,I(term,term)); result=compact(got)
            assert result==old['optional'][i]==prior['inputs'][i]
            cert['optional'].append(result); optional_imports.append((path,len(got['rows'])))
        original_received=[dict(path=str(p.relative_to(ROOT)),lines=n) for p,n in optional_imports]
        assert original_received==old['original_received']
        imports=[]
        for v,goal in enumerate(local_goals):
            path=SRC/('variable-leaf-224-v'+str(v)+'.native.jsonl.gz')
            got=r.scan(r.f.FastSyntax,path,goal,path.with_name(path.name.replace('.native.','.not-or.')),imports=optional_imports)
            result=compact(got); assert result==old['source_packages'][v]
            for m in MODES:
                proofpath=ROOT/got['measurements'][m]['path']
                writer=r.strict_read(proofpath.with_name(proofpath.name+'.writer.json').read_bytes())
                saved_writer=old['local_production'][v]['writers'][m]
                for key in ('lines','bytes','sha256'):
                    assert writer[key]==saved_writer[key]==got['measurements'][m][key]
            imports.append((path,len(got['rows']))); cert['local'].append(result); save()
            print('PASS original local',v,len(got['rows']),'records and nested imports',flush=True)
        B=max([1,len('q'),len('x')]+[v['name_bytes'] for v in cert['optional']]+
            [v['name_bytes'] for lib in cert['libraries'].values() for v in lib.values()])
        assert all(v['name_bytes']<=B for v in cert['local'])
        # Small source terms use the Python parser, independent of compiled archive parsing.
        syntax=r.a.Syntax(); stats=[syntax.stats[syntax.parse(s)] for s in S+['x',y,z]]
        terms={m:(max(s[i] for s in stats),max(s[i+1] for s in stats)) for m,i in zip(MODES,(0,2))}
        sb=source_ledger(cert['optional'],constants['source'],B)
        assert sb==old['source_bound']
        for m in MODES:
            for x in cert['local']:
                a=x['measurements'][m]; lim=sb['formats'][m]
                assert x['node_sums'][m]<=a['bytes']<=lim['bytes']
                assert a['lines']<=lim['lines'] and a['max_record_nodes']<=lim['record_nodes'] and x['depths'][m]<=lim['depth']
        direct=closure_ledger(sum(n for _,n in imports),{m:sum(x['node_sums'][m] for x in cert['local']) for m in MODES},
            {m:max(x['depths'][m] for x in cert['local']) for m in MODES},B,terms,constants['closure'])
        composed=closure_ledger(2*sb['formats']['native']['lines'],{m:2*sb['formats'][m]['bytes'] for m in MODES},
            {m:sb['formats'][m]['depth'] for m in MODES},B,terms,constants['closure'])
        assert direct==old['uniform_ledger'] and composed==old['composed_source_majorant']
        cert.update(source_bound=sb,uniform_ledger=direct,composed_source_majorant=composed,
                    original_statistics=dict(payload_bytes=B,terms=terms),phase='exports')
        offsets=[]; offset=0
        for v,(path,n) in enumerate(imports):
            offsets.append(dict(label='local-'+str(v),start=offset,lines=n,root=offset+n-1)); offset+=n
        assert offsets==old['imports']; cert['imports']=offsets; save()
        roots={}
        for v,goal in enumerate(goals):
            paths=[OUT/('actual-224-coordinate-'+str(v)+'.'+m+'.jsonl.gz') for m in MODES]
            root=old['exports'][v]['root']; roots[root]=goal
            print('START complete coordinate',v,flush=True)
            got=r.scan(r.f.FastSyntax,paths[0],goal,paths[1],roots=roots,imports=imports)
            assert len(got['rows'])-1==root
            saved_export=old['exports'][v]
            assert saved_export['coordinate']==v and saved_export['endpoint']==goal
            for m in MODES:
                measured=got['measurements'][m]; saved=saved_export['proofs'][m]
                proofpath=ROOT/measured['path']
                writer=r.strict_read(proofpath.with_name(proofpath.name+'.writer.json').read_bytes())
                for key in ('lines','bytes','sha256'): assert writer[key]==measured[key]
                assert measured==saved['measurement'] and got['depths'][m]==saved['full_field_depth']
                assert got['depths'][m]<=direct['formats'][m]['depth']<=composed['formats'][m]['depth']
                for key in ('lines','bytes','record_nodes'):
                    actual=measured['max_record_nodes' if key=='record_nodes' else key]
                    assert actual<=direct['formats'][m][key]<=composed['formats'][m][key]
                print('PASS',v,m,'lines',measured['lines'],'/',composed['lines'],
                      'bytes',measured['bytes'],'/',composed['formats'][m]['bytes'],flush=True)
            cert['exports'].append(dict(coordinate=v,root=root,full=compact(got),earlier_roots=dict(roots)))
            save()
        assert old['active_coordinate']==1 and old['active_root']==cert['exports'][1]['root']
        cert['aggregate']={}; cert['earlier_prefix']={}; cert['phase']='prefix'; save()
        for m in MODES:
            size=sum(x['full']['measurements'][m]['bytes'] for x in cert['exports'])
            count=sum(x['full']['measurements'][m]['lines'] for x in cert['exports'])
            agg=dict(lines=count,required_lines=direct['aggregate_lines'],bytes=size,
                required_bytes=direct['formats'][m]['aggregate_bytes'],composed_required_bytes=composed['formats'][m]['aggregate_bytes'])
            assert agg==old['aggregate'][m]
            assert size<=agg['required_bytes']<=agg['composed_required_bytes'] and count<=agg['required_lines']<=composed['aggregate_lines']
            cert['aggregate'][m]=agg
            paths=[ROOT/x['full']['measurements'][m]['path'] for x in cert['exports']]
            n=nb=0; digest=hashlib.sha256()
            with gzip.open(paths[0],'rb') as a,gzip.open(paths[1],'rb') as b:
                a.readline(); b.readline()  # Both distinct headers were reconstructed above.
                for row in a:
                    assert row==b.readline(),(m,n,'earlier record changed')
                    n+=1; nb+=len(row); digest.update(row)
                assert b.readline(), 'later prefix must extend earlier prefix'
            required=cert['exports'][0]['full']['measurements'][m]['lines']
            assert n==required==cert['exports'][0]['root']+1
            prefix=dict(records=n,required_records=required,record_bytes=nb,record_sha256=digest.hexdigest(),byte_identical_prefix=True)
            assert prefix==old['earlier_prefix'][m]; cert['earlier_prefix'][m]=prefix; save()
            print('PASS every earlier record',m,n,'/',required,flush=True)
        metadata=dict(source=inp,original_received=original_received,imports=offsets,receiving=receiving,
            exports=[dict(coordinate=x['coordinate'],root=x['root'],paths={m:x['full']['measurements'][m]['path'] for m in MODES}) for x in cert['exports']])
        accounting=dict(complete_interface=metadata,bytes=len(json.dumps(metadata).encode('ascii')),
            original_source_optional_bytes=len(raw)+sum(x['measurements']['native']['bytes'] for x in cert['optional']),
            optional_path_framing_bytes=len(json.dumps(original_received).encode('ascii')),
            separate_library_bytes={name:{m:sum(x['measurements'][m]['bytes'] for x in lib.values()) for m in MODES} for name,lib in cert['libraries'].items()})
        for key,value in accounting.items(): assert value==old['metadata'][key],key
        cert['metadata']=accounting
        cert['historical_claims_not_replayed']={k:old[k] for k in ('argument_checks','max_argument_height','local_production')}
        cert['limitation']='Historical constructor calls are not recoverable from archives; all emitted substitutions and full depths are checked. No chain or whole-receiver verdict.'
        assert oldpath.read_bytes()==oldraw
        cert.update(complete=True,phase='complete',preserved_certificate_unchanged=True,
                    verdict='Complete variable-leaf archive reception and independently recomputed source ledger pass.')
        save()
        for m,a in cert['aggregate'].items(): print('PASS aggregate',m,a['bytes'],'/',a['composed_required_bytes'],flush=True)
        print('PASS failures',cert['failures'],'certificate',DEST.relative_to(ROOT),flush=True)
    except BaseException as exc:
        cert['failures'].append(type(exc).__name__+': '+str(exc)); save(); raise

if __name__=='__main__': main()
