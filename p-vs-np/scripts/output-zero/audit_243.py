"""Archive-only audit of step 241; fresh evidence, no proof constructors run.

Reuses the inspected strict primitive/image scanner. The specialization,
provenance reconstruction, equations and byte accounting below are independent
of compose_241/verify_retention_241/final_accounting_241.
"""
import copy
import gzip
import hashlib
import json
import sys
from itertools import zip_longest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT/'scripts/left-closure'))
import replay_star as r

OLD = ROOT/'scripts/output-zero/output/composition-241'
BRIDGE = ROOT/'scripts/actual-tree/output/initial-236/zero-deleted'
CHAIN = ROOT/'scripts/backward-zero/output/actual-zero-232-r1'
OUT = ROOT/'scripts/output-zero/output/audit-243'
MODES = ('native', 'not-or')

def read(p): return r.strict_read(p.read_bytes())
def compact(x): return {k:v for k,v in x.items() if k not in ('rows','references')}
def pair(folder, name): return [folder/f'{name}.{m}.jsonl.gz' for m in MODES]
def rows(p):
    with gzip.open(p, 'rb') as f:
        read_header = r.strict_read(f.readline())
        assert set(read_header) == {'format','goal'}
        for raw in f: yield r.strict_read(raw)
def scan(ps, goal, **kw): return r.scan(r.f.FastSyntax, ps[0], goal, ps[1], **kw)
def rawcharge(p):
    h=hashlib.sha256(); size=0
    with (gzip.open(p,'rb') if p.suffix=='.gz' else p.open('rb')) as f:
        for block in iter(lambda:f.read(1048576), b''):
            h.update(block); size+=len(block)
    return dict(bytes=size, sha256=h.hexdigest())
def leaves(x):
    if isinstance(x,dict): return sum(leaves(v) for v in x.values())
    if isinstance(x,list): return sum(map(leaves,x))
    return 1
def ceilog(n): return (n-1).bit_length()
def I(a,b): return '('+a+'>'+b+')'
def N(a): return '(~'+a+')'
def P(a,b): return N(I(a,N(b)))
def E(a,b): return P(I(a,b),I(b,a))

def specialize(row, env):
    # Recursive tuple implementation, not the producer's interned substitution.
    def term(s):
        def visit(t):
            if isinstance(t,str): return env.get(t,t)
            return (t[0], *(visit(v) for v in t[1:]))
        return r.a.ep.c.serialize(visit(r.a.ep.c.parse(s,'native')[0]))
    out=dict(f=term(row['f']),rule=row['rule'])
    if row['rule']=='mp': out['refs']=row['refs']
    else: out['subs']={k:term(v) for k,v in row['subs'].items()}
    return out

def ledger(cert, chain, sup, fixed):
    # Equations L066(1), L065(4), L064(1)/(2), then L067(3)/(4).
    # Original optional measurements are audited inputs, not generated outputs.
    J66=10+2568*2000; H66=9; PP=48*4**(H66+1)
    J65=2*J66+3471*10000*2*(2**12)**2*49**2
    G65=J65-2*J66
    G64=3471*10000*(2**13)**2*48**2; Jc=2*J65+G64
    Jb=1634; Lt=1449; J=Jb+Jc+Lt+2; delta=(J+2).bit_length()
    Vb={}; Uc={}; W={}; inherited={}
    for m,K,S66,D66,t,d,S65,D65,S64,D64,c in [
        ('native',1224,2040,18,10,4,2456,19,2456,18,3),
        ('not-or',1264,2712,24,13,6,3492,27,3492,25,6)]:
        U66=10*(K+(J66-10+1)*S66*PP)+(J66+2)*(256+64*ceilog(J66+2))
        P65=8*4**49*(t+1)
        U65=10*(2*U66+(G65+1)*S65*P65)+(J65+2)*(256+64*ceilog(J65+2))
        dep65=max(max(39 if m=='native' else 42,D66+c*H66+3),D65+c*48+d)
        P64=8*4**48*(t+1); A=max(2*U65,S64*P64)
        Uc[m]=10*(2*U65+G64*S64*P64+A)+(Jc+2)*(256+64*ceilog(Jc+2))
        assert U66==chain['source_bound']['formats'][m]['bytes']
        assert U65==chain['closure_source_bound']['formats'][m]['bytes']
        cb=chain['original_source_chain_ledger']['formats'][m]
        assert (Uc[m],A,max(dep65,D64+c*47+d))==(cb['bytes'],cb['record_nodes'],cb['depth'])
        Sbridge=584 if m=='native' else 788
        St=792 if m=='native' else 1100
        Vb[m]=(Jb+2)*(5*Sbridge*768+256+64*ceilog(Jb+2))
        W[m]=Vb[m]+Uc[m]+2*(Jb+Jc)*delta+(Lt+4)*(10*St*t+256+64*delta)
        assert W[m]==cert['required']['formats'][m]['bytes']
        inherited[m]=dict(source=U66,closure=U65,chain=Uc[m],depth=cb['depth'])
    assert Jc==chain['original_source_chain_ledger']['lines']
    locations=8*(512+128*ceilog(Jc+6))
    assert locations==69632==chain['original_source_chain_ledger']['metadata_bytes']
    R=1000*5*2*27*4**3
    Mb=10000*(R+Jb+2)**2+5*(584+788)*768
    table=2**30*59**28
    charges=sup['interface_input_charges']
    assert charges['coefficient_certificate_bound']==table
    assert sum(charges.values())==sup['interface_required_bytes']
    O=rawcharge(ROOT/chain['provenance']['input'])['bytes']
    for p in read(OLD/'retained-inputs.json')['original_optional_paths']:
        O+=rawcharge(ROOT/p['path'])['bytes']
    assert O==4979
    Escale=R+Mb+table+sum(charges.values())+fixed+O+J+sum(W.values())+10000
    assert Escale==cert['required']['metadata_scale']
    assert 10000*Escale**2==cert['required']['metadata_bytes']
    total=sum(W.values())+10000*Escale**2+fixed
    assert total==cert['required']['full_output_bytes']
    return dict(inherited=inherited,bridge=Vb,joined=W,lines=J,reference_digits=delta,
                locations=locations,metadata_scale=Escale,metadata_bound=10000*Escale**2,total_bound=total)

def main():
    assert not OUT.exists(), 'preserve all prior evidence'
    OUT.mkdir(); dest=OUT/'certificate.json'
    result=dict(step=243,complete=False,failures=[],phase='inputs')
    def save(): dest.write_text(json.dumps(result,indent=2)+'\n')
    save()
    try:
        cert=read(OLD/'certificate.json'); chain=read(CHAIN/'certificate.json')
        sup=read(CHAIN/'source-interface-ledger.json'); oldloc=read(CHAIN/'locations.json')
        source=read(ROOT/'scripts/actual-tree/output/empty-zero-repaired.input.json')
        y=I('q','q'); z=N(y); s=P(z,y); goal=E(z,z); bg=E(z,s); cg=E(s,z)
        expected_source=dict(source=dict(tree=['zero'],letters=[],q='q',delete_zero=True),edges=[],
            request=dict(N=2,n=0,q='q',t=1,suffixes=[s,y],letters=[],E0=[[0,0],[0,0]],Eb=[]))
        assert source==expected_source==read(BRIDGE/'source.json')
        prior=read(ROOT/chain['provenance']['prior'])
        for key in ('input','prior','table'):
            assert hashlib.sha256((ROOT/chain['provenance'][key]).read_bytes()).hexdigest()==chain['provenance'][key+'_sha256']
        retained=dict(original=source,bridge_source=source,bridge_manifest=read(BRIDGE/'bridge.json'),
            chain_interface=chain['original_input_accounting']['complete_interface'],original_chain_locations=oldloc,
            original_source_interface_charges=sup['interface_input_charges'],original_optional_paths=prior['original_received'])
        assert retained==read(OLD/'retained-inputs.json')
        assert retained['bridge_manifest']['goal']==bg
        assert chain['root']==oldloc['rows'][0]['required_roots'][-1]==377086
        assert chain['provenance']['exact_source_row_endpoint']==cg
        libpair=pair(ROOT/'scripts/balanced-slot/output','trans')
        library=scan(libpair,I(E('A','B'),I(E('B','C'),E('A','C'))))
        assert len(library['rows'])==1449
        assert [(library['depths'][m],library['measurements'][m]['max_record_nodes']) for m in MODES]==[(14,792),(20,1100)]
        env={k:r.a.ep.c.parse(v,'native')[0] for k,v in dict(A=z,B=s,C=z,q='q').items()}
        count=0
        for old,new in zip_longest(rows(libpair[0]),rows(pair(OLD,'trans-substituted')[0])):
            assert old is not None and new is not None and specialize(old,env)==new
            count+=1
        assert count==1449
        trans=scan(pair(OLD,'trans-substituted'),I(bg,I(cg,goal)))
        bridge=scan(pair(BRIDGE,'bridge'),bg)
        assert len(bridge['rows'])==1634
        for m in MODES:
            for key in ('lines','bytes','sha256'):
                assert bridge['measurements'][m][key]==retained['bridge_manifest']['files'][m][key]
        result.update(original_trans_records=count,library=compact(library),bridge=compact(bridge),trans=compact(trans))
        # Pay the source/closure/chain fixed libraries as separately retained
        # charges, including repeated physical files, as in the theorem.
        fresh234=read(ROOT/'scripts/backward-zero/output/audit-234/source-replay.json')
        groups={k:fresh234['libraries'][k] for k in ('source','closure')}
        groups['chain']={k:v for k,v in groups['closure'].items() if k!='close_cancel'}
        fixedfiles=[]
        for group,items in groups.items():
            for entry in items.values():
                for m in MODES:
                    item=entry['measurements'][m] if 'measurements' in entry else entry[m]
                    p=ROOT/item['path']; val=rawcharge(p)
                    assert val['bytes']==item['bytes'] and val['sha256']==item['sha256']
                    fixedfiles.append(dict(group=group,path=str(p.relative_to(ROOT)),**val))
        earlier=read(ROOT/'scripts/actual-tree/output/certificate-236.json')
        for name,entry in earlier['library'].items():
            for m in MODES:
                item=entry['measurements'][m]; val=rawcharge(ROOT/item['path'])
                assert val['bytes']==item['bytes'] and val['sha256']==item['sha256']
                fixedfiles.append(dict(group='bridge',name=name,path=item['path'],**val))
        for m in MODES:
            item=library['measurements'][m]
            fixedfiles.append(dict(group='trans',path=item['path'],bytes=item['bytes'],sha256=item['sha256']))
        fixed=sum(x['bytes'] for x in fixedfiles)
        assert fixed==50370561
        result['fixed_libraries']=fixedfiles
        result['bounds']=ledger(cert,chain,sup,fixed)
        shifted=copy.deepcopy(oldloc)
        for imp in shifted['coordinate_imports']:
            for key in ('start','root'): imp[key]+=1634
        for row in shifted['rows']:
            for key in ('start','end'): row[key]+=1634
            row['required_roots']=[k+1634 for k in row['required_roots']]
        optional=[dict(v,start=v['start']+1634,end=v['end']+1634) for v in sup['nested_optional_occurrences']]
        locals_=[dict(coordinate=i,local=j,start=1634+co['start']+lo['start'],lines=lo['lines'],root=1634+co['start']+lo['root'])
                 for i,co in enumerate(chain['imports']) for j,lo in enumerate(prior['imports'])]
        locations=dict(bridge=dict(start=0,lines=1634,root=1633),chain=dict(start=1634,lines=377087,root=378720),
            trans=dict(start=378721,lines=1449,root=380169),mps=[380170,380171],transported_chain=shifted,
            local_occurrences=locals_,optional_occurrences=optional,nested_earlier_coordinate_root=247117)
        assert locations==read(OLD/'locations.json')==cert['locations']
        roots={int(k)+1634:v for k,v in chain['requested_roots'].items()}
        roots.update({1633:bg,378720:cg,380169:I(bg,I(cg,goal)),380170:I(cg,goal),380171:goal})
        assert roots=={int(k):v for k,v in cert['requested_roots'].items()}
        result.update(locations=locations,requested_roots=roots,phase='full-paired-replay'); save()
        print('Source bounds independently recomputed; replay 380172 full records per format',flush=True)
        joined=scan(pair(OLD,'output-zero'),goal,roots=roots,
            imports=[(pair(BRIDGE,'bridge')[0],1634),(pair(CHAIN,'chain')[0],377087),(pair(OLD,'trans-substituted')[0],1449)])
        assert len(joined['rows'])==380172
        assert joined['references'][-2:]==[[1633,380169],[378720,380170]]
        ancestry=r.a.ancestors(joined['references'],380171)
        assert 1633 in ancestry and 378720 in ancestry
        for m in MODES:
            assert joined['measurements'][m]==cert['output']['measurements'][m]
            actual=joined['measurements'][m]; bd=cert['required']['formats'][m]
            assert actual['lines']<=bd['lines'] and actual['bytes']<=bd['bytes']
            assert actual['max_record_nodes']<=bd['record_nodes'] and joined['depths'][m]<=bd['depth']
            print('PASS',m,'records',actual['lines'],'<=',bd['lines'],'bytes',actual['bytes'],'<=',bd['bytes'],flush=True)
        result.update(joined=compact(joined),both_roots_in_ancestry=True,phase='nested-retention-and-accounting'); save()
        wanted={}
        for occurrence in optional:
            package=prior['original_received'][occurrence['optional']]
            original=list(rows(ROOT/package['path'])); assert len(original)==occurrence['lines']==5
            for j,value in enumerate(original):
                v=copy.deepcopy(value)
                if 'refs' in v: v['refs']=[k+occurrence['start'] for k in v['refs']]
                wanted[occurrence['start']+j]=v
        found=0
        for i,row in enumerate(rows(pair(OLD,'output-zero')[0])):
            if i in wanted:
                assert row==wanted[i]; found+=1
            if i==max(wanted): break
        assert found==40
        result['original_optional_records_compared']=found
        # Account every artifact, through EOF for gzip streams, including the
        # old final report itself. New audit evidence is a separate artifact.
        inventory={p.name:rawcharge(p) for p in sorted(OLD.iterdir())}
        nleaves={p.name:leaves(read(p)) for p in OLD.iterdir() if p.suffix=='.json'}
        assert sum(nleaves.values())<1000
        ancillary=sum(v['bytes'] for k,v in inventory.items() if k not in ('output-zero.native.jsonl.gz','output-zero.not-or.jsonl.gz'))
        final=read(OLD/'final-accounting.json')
        proofs=sum(joined['measurements'][m]['bytes'] for m in MODES)
        assert ancillary==final['ancillary_uncompressed_bytes']
        assert proofs+fixed+ancillary==final['full_output_and_fixed_libraries_bytes']==2749679919
        # Exact serializer replay, including the already final numerical values.
        assert (json.dumps(final,indent=2)+'\n').encode('ascii')==(OLD/'final-accounting.json').read_bytes()
        assert ancillary<=result['bounds']['metadata_bound']
        assert proofs+fixed+ancillary<=result['bounds']['total_bound']
        result.update(inventory=inventory,metadata_leaves=nleaves,ancillary_bytes=ancillary,
            total_charged_bytes=proofs+fixed+ancillary,self_accounting_fixed_point=True,
            complete=True,phase='complete',qualification='Exact retained empty-zero interface only. Reuses audited source/closure/table contracts and strict scanner; no general receiver or SAT conclusion.')
        save()
        print('PASS ancillary',ancillary,'<=',result['bounds']['metadata_bound'],'metadata leaves',sum(nleaves.values()),'< 1000; failures []',str(dest.relative_to(ROOT)),flush=True)
    except BaseException as exc:
        result['failures'].append(dict(type=type(exc).__name__,message=str(exc))); save(); raise

def supplement():
    """Complete original image retention and ancillary framing inventory."""
    dest=OUT/'retention-accounting.json'
    assert not dest.exists(), 'preserve evidence'
    result=dict(complete=False,failures=[])
    try:
        cert=read(OLD/'certificate.json'); fresh=read(OUT/'certificate.json')
        assert fresh['complete'] and not fresh['failures']
        # Read the complete original paired inputs, including their image
        # records; compare every field through each input's own EOF.
        imports=[(BRIDGE,'bridge',1634),(CHAIN,'chain',377087),(OLD,'trans-substituted',1449)]
        counts={}
        for m in MODES:
            emitted=iter(rows(OLD/f'output-zero.{m}.jsonl.gz')); offset=0
            for folder,stem,n in imports:
                original=folder/f'{stem}.{m}.jsonl.gz'; count=0
                with gzip.open(original,'rb') as f:
                    header=r.strict_read(f.readline())
                expected_goal=(fresh['bridge'] if stem=='bridge' else fresh['trans'] if stem=='trans-substituted' else cert['inputs']['chain'])['measurements'][m]
                charge=rawcharge(original)
                assert charge['bytes']==expected_goal['bytes'] and charge['sha256']==expected_goal['sha256']
                assert header['format']==m
                for value in rows(original):
                    v=copy.deepcopy(value)
                    if 'refs' in v: v['refs']=[k+offset for k in v['refs']]
                    assert next(emitted)==v, (m,stem,count)
                    count+=1
                assert count==n; counts[m+'/'+stem]=count; offset+=count
            # Exactly the two already primitive-checked MPs, then true EOF.
            assert next(emitted)['refs']==[1633,380169]
            assert next(emitted)['refs']==[378720,380170]
            assert next(emitted,None) is None
        manifest=read(OLD/'manifest.json')
        y=I('q','q'); z=N(y)
        assert manifest['goal']==E(z,z) and manifest['root']==380171
        assert manifest['complete_records_retained']==380170
        assert manifest['locations']=='locations.json' and manifest['inputs']=='retained-inputs.json'
        for m in MODES:
            for k in ('lines','bytes','sha256'):
                assert manifest['files'][m][k]==fresh['joined']['measurements'][m][k]
        ancillary={}
        def groups(x):
            # Values, keys, braces, colons, commas, and a newline per record
            # are bounded separately; the scalar count is not a byte count.
            if isinstance(x,dict): return 2+len(x)+max(0,len(x)-1)+sum(1+groups(v) for v in x.values())
            if isinstance(x,list): return 2+max(0,len(x)-1)+sum(map(groups,x))
            return 1
        for p in sorted(OLD.glob('*.gz')):
            if p.name.startswith('output-zero.'): continue
            n=0; mxscalar=0; mxgroups=0; maxfield=0
            for row in rows(p):
                n+=1; mxscalar=max(mxscalar,leaves(row)); mxgroups=max(mxgroups,groups(row))
                terms=[row['f']]+list(row.get('subs',{}).values())
                maxfield=max(maxfield,*(len(t) for t in terms))
            limit=1449 if p.name.startswith('trans-substituted.') else 1656
            assert n<=limit and mxscalar<=5 and mxgroups<=32
            ancillary[p.name]=dict(records=n,required_records=limit,max_scalar_values=mxscalar,
                max_keys_values_punctuation_groups=mxgroups,max_formula_field_bytes=maxfield)
        assert len(ancillary)==8
        result.update(complete=True,entire_original_records=counts,manifest_checked=True,ancillary=ancillary,
            framing_qualification='At most five scalar values per record; at most 32 separately counted keys/values/punctuation groups. This refines the prose less-than-20 grouping convention. 651 metadata leaves plus 32*(2*1449+6*1656) record groups and fixed headers/framing remain below 1000E*. No bound or archive changes.')
    except BaseException as exc:
        result['failures'].append(dict(type=type(exc).__name__,message=str(exc))); raise
    finally:
        dest.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS complete both-format input retention; ancillary fields/framing; failures []',str(dest.relative_to(ROOT)),flush=True)

def metadata_framing():
    dest=OUT/'metadata-framing.json'
    assert not dest.exists(), 'preserve evidence'
    def groups(x):
        if isinstance(x,dict): return 2+len(x)+max(0,len(x)-1)+sum(1+groups(v) for v in x.values())
        if isinstance(x,list): return 2+max(0,len(x)-1)+sum(map(groups,x))
        return 1
    counts={p.name:groups(read(p)) for p in sorted(OLD.glob('*.json'))}
    assert sum(counts.values())<10000
    dest.write_text(json.dumps(dict(complete=True,failures=[],groups=counts,total_groups=sum(counts.values()),required_groups=10000,
        qualification='Same individual key/value/brace/colon/comma convention as audit_243.supplement; string spelling is a separate field payload.'),indent=2)+'\n')
    print('PASS metadata groups',sum(counts.values()),'< 10000; failures [];',dest.relative_to(ROOT),flush=True)

if __name__=='__main__':
    if '--metadata' in sys.argv: metadata_framing()
    elif '--supplement' in sys.argv: supplement()
    else: main()
