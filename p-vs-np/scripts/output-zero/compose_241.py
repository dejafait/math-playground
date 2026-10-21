"""One retained empty-zero composition; no synthesis or source regeneration.

Full expanded JSON fields are copied. Existing audited input-bound theorems
are applied before measuring exports. All destinations are fresh.
"""
import copy
import gzip
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT/'scripts/backward-zero'))
import actual_zero_232 as prior
sys.path.insert(0, str(ROOT/'scripts/actual-tree'))
import initial_verify as iv

r, MODES = prior.r, prior.MODES
OUT = ROOT/'scripts/output-zero/output/composition-241'
BRIDGE = ROOT/'scripts/actual-tree/output/initial-236/zero-deleted'
CHAIN = ROOT/'scripts/backward-zero/output/actual-zero-232-r1'
SLOT = ROOT/'scripts/balanced-slot/output'


def enc(obj):
    return (json.dumps(obj, separators=(',', ':'), ensure_ascii=True)+'\n').encode('ascii')


def read(path): return r.strict_read(path.read_bytes())
def compact(obj): return {k:v for k,v in obj.items() if k not in ('rows','references')}
def paths(folder, stem): return [folder/f'{stem}.{m}.jsonl.gz' for m in MODES]


def rows(path):
    with gzip.open(path, 'rb') as stream:
        r.strict_read(stream.readline())
        for raw in stream: yield r.strict_read(raw)


def moved(row, offset):
    value = copy.deepcopy(row)
    if value['rule'] == 'mp': value['refs'] = [x+offset for x in value['refs']]
    return value


def scan(pair, goal, **kwargs):
    return r.scan(r.f.FastSyntax, pair[0], goal, pair[1], **kwargs)


def receive(envelope, original, cert, loc, root):
    checked = iv.receive(envelope, 4)
    assert envelope == original, 'source/suffix/q mismatch'
    assert original['source'] == dict(tree=['zero'], letters=[], q='q', delete_zero=True)
    assert cert['provenance']['receiving']['suffixes'] == original['request']['suffixes']
    assert len(loc['rows']) == 1
    row = loc['rows'][0]
    assert (row['level'],row['row']) == (0,0)
    assert root == cert['root'] == row['required_roots'][-1] == row['end']-1 == 377086, 'indexed root'
    return checked


def substituted_library(native, env):
    """Simultaneous variable substitution, including every axiom subs field."""
    syntax = r.f.FastSyntax()
    try:
        replacements = {k:syntax.parse(v) for k,v in env.items()}
        cache = {}
        def visit(j):
            if j in cache: return cache[j]
            tag,*args = syntax.nodes[j]
            value = (replacements.get(args[0],j) if tag=='v' else
                     syntax.node(tag, *(visit(a) for a in args)))
            cache[j] = value
            return value
        def term(text): return syntax.text(visit(syntax.parse(text)))
        for row in rows(native):
            result = dict(f=term(row['f']),rule=row['rule'])
            if row['rule']=='mp': result['refs'] = row['refs']
            else: result['subs'] = {k:term(v) for k,v in row['subs'].items()}
            yield result
    finally: syntax.close()


def write_pair(pair, goal, native_rows):
    syntax = r.f.FastSyntax()
    streams = [gzip.open(path,'wb') for path in pair]
    digests = [hashlib.sha256(),hashlib.sha256()]; totals=[0,0]; count=0
    def put(i,obj):
        raw=enc(obj); streams[i].write(raw); digests[i].update(raw); totals[i]+=len(raw)
    try:
        target=syntax.parse(goal)
        for i,m in enumerate(MODES): put(i,dict(format=m,goal=syntax.text(target,bool(i))))
        for row in native_rows:
            put(0,row)
            image=dict(f=syntax.text(syntax.parse(row['f']),True),rule=row['rule'])
            if row['rule']=='mp': image['refs']=row['refs']
            else: image['subs']={k:syntax.text(syntax.parse(v),True) for k,v in row['subs'].items()}
            put(1,image); count+=1
        return {m:dict(lines=count,bytes=totals[i],sha256=digests[i].hexdigest()) for i,m in enumerate(MODES)}
    finally:
        for stream in streams: stream.close()
        syntax.close()


def bound(envelope, chain, supplement, library):
    """Apply L066(2)-(4) and the audited L067 source composition, then relocate.

    No generated stream length/size, compressed size or intern count is an input.
    Fixed-library measurements are checked constants, not generated parameters.
    """
    U,d,n,B=1,0,0,1
    Jb=1634; H=d+1; Pstar=48*4**(H+1)
    R=1000*(B+4)*(n+2)*(U+2)**3*4**(2*d+3)
    bridge={m:(Jb+2)*((B+4)*S*Pstar+256+64*(Jb+1).bit_length())
            for m,S in zip(MODES,(584,788))}
    Mb=10000*(R+Jb+2)**2+(B+4)*(584+788)*Pstar
    cb=chain['original_source_chain_ledger']
    # These are the separately audited all-original-source monotone compositions.
    audit=read(ROOT/'scripts/backward-zero/output/audit-234/certificate.json')
    assert audit['complete'] and audit['failures']==[]
    assert audit['locations_bound']==cb['metadata_bytes']
    for m in MODES:
        for k,v in audit['original_source_bounds'][m].items(): assert cb['formats'][m][k]==v
    assert cb['lines']==10959585489735744040
    assert chain['closure_source_bound']['lines']==2796383077672992020
    assert chain['source_accounting_check']['source_payload_bytes']==6
    Jc=cb['lines']; Lt=library['measurements']['native']['lines']; Bstar=6
    assert Lt==1449
    J=Jb+Jc+Lt+2; digits=(J+2).bit_length()
    formats={}
    for m,t in zip(MODES,(10,13)):
        St=library['measurements'][m]['max_record_nodes']
        Dt=library['depths'][m]
        relocation=2*(Jb+Jc)*digits
        generated=(Lt+4)*((Bstar+4)*St*t+256+64*digits)
        byte_bound=bridge[m]+cb['formats'][m]['bytes']+relocation+generated
        formats[m]=dict(lines=J,bytes=byte_bound,bits=8*byte_bound,
            import_reference_allowance=relocation,trans_mp_header_allowance=generated,
            record_nodes=max(584*Pstar if m=='native' else 788*Pstar,
                             cb['formats'][m]['record_nodes'],St*t),
            depth=max(22 if m=='native' else 31,cb['formats'][m]['depth'],Dt+(4 if m=='native' else 6)),
            trans_record_nodes=St*t,trans_field_depth=Dt+(4 if m=='native' else 6))
    # Fixed libraries are paid separately, including conservative repeated laws.
    fixed=sum(sum(x.values()) for x in chain['original_input_accounting']['fixed_library_bytes'].values())
    earlier=read(ROOT/'scripts/actual-tree/output/certificate-236.json')
    fixed+=sum(x['measurements'][m]['bytes'] for x in earlier['library'].values() for m in MODES)
    fixed+=sum(library['measurements'][m]['bytes'] for m in MODES)
    table=supplement['interface_input_charges']['coefficient_certificate_bound']
    original=chain['original_input_accounting']['source_optional_native_bytes']
    # Each original metadata object is paid by a displayed source bound.
    # Ancillary proof material comprises the substituted trans pair and three
    # malformed prefixes of at most Jb+22 records/format. Their scalar fields,
    # plus <1000 ordinary metadata fields, number <1000E, and each expanded
    # field/numeral/path/goal costs <10E bytes. Thus 10000E^2 pays all ancillary
    # material, including the digits of this bound. No measurement defines E.
    E=R+Mb+table+supplement['interface_required_bytes']+fixed+original+J+sum(x['bytes'] for x in formats.values())+10000
    metadata=10000*E**2
    return dict(original_parameters=dict(U=U,d=d,n=n,B=B,Bstar=Bstar,admission=4,
        bridge_envelope_bound=R,bridge_metadata_bound=Mb,bridge_record_bound=Jb,
        bridge_proof_bounds=bridge,chain_record_bound=Jc,chain_proof_bounds={m:cb['formats'][m]['bytes'] for m in MODES},
        chain_locations_bound=cb['metadata_bytes'],table_bound=table,
        chain_interface_bound=supplement['interface_required_bytes'],original_source_optional_bytes=original,
        fixed_library_bytes=fixed,trans_records=Lt),
        lines=J,reference_digits=digits,formats=formats,metadata_scale=E,metadata_bytes=metadata,
        full_output_bytes=sum(x['bytes'] for x in formats.values())+metadata+fixed,
        basis='L066(2)-(4), L067 steps232/234 source composition, full-record substitution and explicit reference relocation. delta <= J+2 yields a fixed polynomial; generated measurements define no parameter.')


def main():
    assert not OUT.exists(), 'preserve all earlier work; fresh destination required'
    OUT.mkdir(parents=True)
    cert=dict(step=241,complete=False,failures=[],phase='receive',rejections=[])
    def save(): (OUT/'certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
    save()
    try:
        source_path=ROOT/'scripts/actual-tree/output/empty-zero-repaired.input.json'
        original=read(source_path); envelope=read(BRIDGE/'source.json')
        old=read(CHAIN/'certificate.json'); sup=read(CHAIN/'source-interface-ledger.json')
        loc=read(CHAIN/'locations.json'); manifest=read(BRIDGE/'bridge.json')
        assert old['complete'] and sup['complete'] and old['failures']==sup['failures']==[]
        checked=receive(envelope,original,old,loc,old['root'])
        I,N,E=prior.independent.I,prior.independent.neg,prior.independent.E
        Y=I('q','q'); Z=N(Y); S=original['request']['suffixes'][0]
        goal=E(Z,Z); bg=E(Z,S); cg=E(S,Z)
        assert checked['goal']==bg==manifest['goal']
        assert old['provenance']['exact_source_row_endpoint']==cg
        assert old['provenance']['input']==str(source_path.relative_to(ROOT))
        assert hashlib.sha256(source_path.read_bytes()).hexdigest()==old['provenance']['input_sha256']
        fixed_goal=I(E('A','B'),I(E('B','C'),E('A','C')))
        libpair=paths(SLOT,'trans'); library=scan(libpair,fixed_goal)
        cert['library']=compact(library)
        cert['required']=bound(envelope,old,sup,compact(library)); save()
        print('Original-source bounds fixed; replay both complete input pairs',flush=True)
        bp,cp=paths(BRIDGE,'bridge'),paths(CHAIN,'chain')
        bridge=scan(bp,bg); chain=scan(cp,cg,roots={int(k):v for k,v in old['requested_roots'].items()})
        for m in MODES:
            assert chain['measurements'][m]==old['proofs'][m]['measurement']
            for key in ('lines','bytes','sha256'): assert bridge['measurements'][m][key]==manifest['files'][m][key]
        nb=len(bridge['rows']); nc=len(chain['rows']); nt=len(library['rows'])
        assert nb==1634 and nc==377087 and nt==1449
        trans_offset=nb+nc; first_mp=trans_offset+nt; final=first_mp+1
        env=dict(A=Z,B=S,C=Z,q='q')
        tp=paths(OUT,'trans-substituted')
        tg=I(bg,I(cg,goal))
        tw=write_pair(tp,tg,substituted_library(libpair[0],env))
        trans=scan(tp,tg)
        assert len(trans['rows'])==nt
        for m in MODES:
            bd=cert['required']['formats'][m]
            assert trans['measurements'][m]['max_record_nodes']<=bd['trans_record_nodes']
            assert trans['depths'][m]<=bd['trans_field_depth']
        pair=paths(OUT,'output-zero')
        def composed_rows():
            for path,off in [(bp[0],0),(cp[0],nb),(tp[0],trans_offset)]:
                for row in rows(path): yield moved(row,off)
            yield dict(f=I(cg,goal),rule='mp',refs=[nb-1,first_mp-1])
            yield dict(f=goal,rule='mp',refs=[nb+old['root'],first_mp])
        cert.update(phase='write-full-joined-pair',inputs=dict(bridge=compact(bridge),chain=compact(chain)),
            trans=dict(environment=env,checks=compact(trans)),root=final)
        # References are deliberately not retained in the diagnostic certificate.
        save(); print('Write full joined pair',final+1,'records/format',flush=True)
        written=write_pair(pair,goal,composed_rows())
        shifted=copy.deepcopy(loc)
        for imp in shifted['coordinate_imports']:
            for k in ('start','root'): imp[k]+=nb
        for row in shifted['rows']:
            for k in ('start','end'): row[k]+=nb
            row['required_roots']=[nb+x for x in row['required_roots']]
        locals_=[]; nested=[]
        prior_reception=read(ROOT/old['provenance']['prior'])
        for co,imp in enumerate(old['imports']):
            for lo,item in enumerate(prior_reception['imports']):
                locals_.append(dict(coordinate=co,local=lo,start=nb+imp['start']+item['start'],
                    lines=item['lines'],root=nb+imp['start']+item['root']))
        for item in sup['nested_optional_occurrences']:
            new=dict(item); new['start']+=nb; new['end']+=nb; nested.append(new)
        location=dict(bridge=dict(start=0,lines=nb,root=nb-1),chain=dict(start=nb,lines=nc,root=nb+old['root']),
            trans=dict(start=trans_offset,lines=nt,root=first_mp-1),mps=[first_mp,final],
            transported_chain=shifted,local_occurrences=locals_,optional_occurrences=nested,
            nested_earlier_coordinate_root=nb+old['imports'][1]['start']+old['imports'][0]['root'])
        assert len(nested)==8 and sum(x['lines'] for x in nested)==40
        assert shifted['rows'][0]['required_roots'][-1]==nb+377086
        (OUT/'locations.json').write_bytes(enc(location))
        retained=dict(original=original,bridge_source=envelope,bridge_manifest=manifest,
            chain_interface=old['original_input_accounting']['complete_interface'],
            original_chain_locations=loc,original_source_interface_charges=sup['interface_input_charges'],
            original_optional_paths=prior_reception['original_received'])
        (OUT/'retained-inputs.json').write_bytes(enc(retained))
        roots={int(k)+nb:v for k,v in old['requested_roots'].items()}
        roots.update({nb-1:bg,nb+old['root']:cg,first_mp-1:tg,first_mp:I(cg,goal),final:goal})
        cert.update(phase='full-output-replay',locations=location,requested_roots=roots); save()
        got=scan(pair,goal,roots=roots,imports=[(bp[0],nb),(cp[0],nc),(tp[0],nt)])
        assert len(got['rows'])==final+1
        ancestor=r.a.ancestors(got['references'],final)
        assert nb-1 in ancestor and nb+old['root'] in ancestor
        for m in MODES:
            measure=got['measurements'][m]; bd=cert['required']['formats'][m]
            for k in ('lines','bytes','sha256'): assert measure[k]==written[m][k]
            assert measure['lines']<=bd['lines'] and measure['bytes']<=bd['bytes']
            assert measure['max_record_nodes']<=bd['record_nodes'] and got['depths'][m]<=bd['depth']
            print('PASS',m,'records',measure['lines'],'<=',bd['lines'],'bytes',measure['bytes'],'<=',bd['bytes'],
                  'full depth',got['depths'][m],'<=',bd['depth'],flush=True)
        cert.update(output=compact(got),both_input_roots_in_final_ancestry=True,phase='negative-receptions')
        save()
        def reject(label,action):
            try: action()
            except (AssertionError,ValueError,iv.c.Invalid) as error:
                cert['rejections'].append(dict(label=label,rejected=True,reason=type(error).__name__+': '+str(error)))
            else: raise AssertionError('accepted '+label)
            save()
        for label,mutate in [('source',lambda d:d['source'].__setitem__('tree',['one'])),
                             ('suffix',lambda d:d['request']['suffixes'].__setitem__(0,'q')),
                             ('q',lambda d:d['request'].__setitem__('q','changed'))]:
            bad=copy.deepcopy(envelope); mutate(bad)
            (OUT/f'reject-{label}.json').write_bytes(enc(bad))
            reject(label,lambda bad=bad:receive(bad,original,old,loc,old['root']))
        badloc=copy.deepcopy(loc); badloc['rows'][0]['required_roots'][-1]-=1
        (OUT/'reject-indexed-root.json').write_bytes(enc(badloc))
        reject('indexed-root',lambda:receive(envelope,original,old,badloc,old['root']))
        # Small malformed prefixes fail before their intentional truncation.
        # They are rejection witnesses, never positive complete-proof evidence.
        prefix=[]
        for i,row in enumerate(rows(pair[0])):
            prefix.append(row)
            if i==nb+20: break
        bad=copy.deepcopy(prefix)
        firstmp=next(i for i,row in enumerate(bad) if row['rule']=='mp')
        bad[firstmp]['refs'][0]=firstmp
        badpair=paths(OUT,'reject-reference')
        write_pair(badpair,goal,iter(bad))
        reject('imported-reference',lambda:scan(badpair,goal,imports=[(bp[0],nb),(cp[0],nc)]))
        bad=copy.deepcopy(prefix); del bad[nb+9]
        badpair=paths(OUT,'reject-omitted-optional')
        write_pair(badpair,goal,iter(bad))
        reject('omitted-retained-optional-record',lambda:scan(badpair,goal,imports=[(bp[0],nb),(cp[0],nc)]))
        badpair=paths(OUT,'reject-image')
        write_pair(badpair,goal,iter(prefix))
        with gzip.open(badpair[1],'rb') as stream: badimage=[r.strict_read(x) for x in stream]
        badimage[1]['subs']['A']='changed'
        with gzip.open(badpair[1],'wb') as stream:
            for row in badimage: stream.write(enc(row))
        reject('imported-image',lambda:scan(badpair,goal))
        result_manifest=dict(goal=goal,files=written,locations='locations.json',inputs='retained-inputs.json',
                             root=final,complete_records_retained=nb+nc+nt)
        (OUT/'manifest.json').write_bytes(enc(result_manifest))
        cert.update(complete=True,phase='complete',limitations='Exact preserved empty-zero fixture; no nonzero integration, ordinary-input completeness, whole-L055 audit, certificate existence or SAT consequence; separate composition audit pending.')
        save()
        # Include all ancillary files, including substituted library and every
        # saved rejection witness, in addition to the full pair and fixed inputs.
        ancillary=0
        for path in OUT.iterdir():
            if path in pair: continue
            if path.suffix=='.gz':
                with gzip.open(path,'rb') as stream:
                    while True:
                        chunk=stream.read(1024*1024)
                        if not chunk: break
                        ancillary+=len(chunk)
            else: ancillary+=path.stat().st_size
        assert ancillary+10000<=cert['required']['metadata_bytes']
        actual=sum(x['bytes'] for x in written.values())+ancillary+cert['required']['original_parameters']['fixed_library_bytes']
        cert['actual_accounting']=dict(ancillary_before_final_accounting_bytes=ancillary,
            accounting_growth_allowance_bytes=10000,full_output_and_fixed_libraries_bytes=actual+10000,
            required_bytes=cert['required']['full_output_bytes'])
        assert actual+10000<=cert['required']['full_output_bytes']
        save()
        print('PASS complete; rejections',len(cert['rejections']),'failures',cert['failures'],
              'total bytes',actual+10000,'<=',cert['required']['full_output_bytes'],
              'certificate',str((OUT/'certificate.json').relative_to(ROOT)),flush=True)
    except BaseException as error:
        cert.update(complete=False)
        cert['failures'].append(dict(type=type(error).__name__,message=str(error))); save(); raise


if __name__=='__main__': main()
