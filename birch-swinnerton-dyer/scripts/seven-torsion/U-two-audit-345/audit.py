"""Fixed U verdict audit: replay only, with independent complete certificates."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json,subprocess,sys,time
sys.set_int_max_str_digits(0)
D=Path(__file__).resolve().parent;ROOT=D.parents[2];S=D.parent;START=time.monotonic()
def read(p):return json.loads(p.read_text())
def need(x,s):
    if not x:raise ArithmeticError(s)
def save(n,x):
    with (D/n).open('x') as f:json.dump(x,f,separators=(',',':'));f.write('\n')
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def tr(a):return [list(r) for r in zip(*a)]
def mm(a,b):
    cols=list(zip(*b))
    return [[sum(x*y for x,y in zip(r,c) if x and y) for c in cols] for r in a]
def run(n,r):
    with (D/(n+'.log')).open('x') as log:
        rc=subprocess.run([sys.executable,'-B',str(D/n)],stdout=log,stderr=subprocess.STDOUT).returncode
    need(rc==0,'first_failure_'+n+'_exit_'+str(rc))
    report=read(D/r);need(report['status']=='PASS' and not report['failures'],'complete_'+r)
    return report
def divisions(prefix,basis,table,radical=None):
    V=basis['scaled_polynomials'];H=basis['H'];scale=basis['scale'];count=0
    if radical is not None:W=tr(mm(tr(V),radical))
    for i in range(48):
        cert=read(D/(prefix+'%02d.json'%i))
        need(type(cert['i']) is int and cert['i']==i and len(cert['products'])==48,'full_division_row')
        if radical is not None:
            A=read(D/('action-%02d.json'%i));JA=mm(radical,A)
            need(JA==mm(tr(table[i]),radical),'all_persisted_action_coordinate_slots')
            expansion=tr(mm(tr(V),JA))
        for j,e in enumerate(cert['products']):
            need(type(e['j']) is int and e['j']==j and len(e['dividend'])==95
                and all(type(x) is int for x in e['dividend']) and len(e['quotient'])==47
                and len(e['remainder'])==95 and all(type(x) is str for x in e['quotient']+e['remainder']),
                'all_exact_division_shapes_and_types')
            actual=[0]*95;right=V[j] if radical is None else W[j]
            for a,x in enumerate(V[i]):
                if x:
                    for b,y in enumerate(right):
                        if y:actual[a+b]+=x*y
            if radical is None:
                for k,c in enumerate(table[i][j]):
                    if c:
                        for a,x in enumerate(V[k]):
                            if x:actual[a]-=scale*c*x
            else:
                for a,x in enumerate(expansion[j]):actual[a]-=scale*x
            need(actual==e['dividend'],'actual_dividend_'+str((prefix,i,j)))
            q=list(map(F,e['quotient']));rem=list(map(F,e['remainder']))
            need(not any(rem),'all_95_remainder_positions_zero')
            reconstructed=rem[:]
            for a,x in enumerate(q):
                if x:
                    for b,h in enumerate(H):
                        if h:reconstructed[a+b]+=x*h
            need(actual==reconstructed,'full_H_division_'+str((prefix,i,j)));count+=1
    need(count==2304,'entire_division_set');return count
report={'status':'STOP','failures':[],'phase':'initial_inventory'}
try:
    OLD=S/'index-eight-order-two-343'
    previous=read(OLD/'canonical-input-hashes.json')
    need(len(previous)==2228,'entire_step343_input_inventory')
    names=set(previous)
    names.update(str(p.relative_to(ROOT)) for p in OLD.rglob('*') if p.is_file())
    names.update(['lemmas/L089-conductor389-index-eight-order-not-2-maximal.md',
        'drafts/literature/2026-10-19-index-eight-order-two-critical-audit.md',
        'scripts/seven-torsion/index-eight-audit-337/independent.py',
        'scripts/seven-torsion/index-eight-audit-337/run_once.py',
        'ATTEMPTS/041-first-overorder-integral-power-witness-cap.md',
        'ATTEMPTS/042-changed-order-audit-approval-repetition.md',
        'ATTEMPTS/044-index-four-table-verifier-integer-zero.md'])
    before={n:digest(ROOT/n) for n in sorted(names)}
    need(all(before[n]==h for n,h in previous.items()),'all_original343_inventory_inputs_unchanged')
    save('canonical-input-hashes.json',before)
    # No additional historical hash exception: retain only documented prior transitions.
    save('inventory-transition.json',{'new_input_exceptions':[],
        'retained_step343_transition':read(OLD/'inventory-transition.json'),
        'L089_before_audit_addendum':before['lemmas/L089-conductor389-index-eight-order-not-2-maximal.md']})
    old_manifest=read(OLD/'copy-manifest.json')
    need(len(old_manifest)==248,'full_step343_copy_manifest')
    for name,e in old_manifest.items():
        need(before[e['source']]==e['sha256']==before[str((OLD/name).relative_to(ROOT))],
            'every_step343_fixed_copy_and_source_'+name)
    manifest={}
    def copy(dest,srcname):
        src=OLD/srcname;key=str(src.relative_to(ROOT));raw=src.read_bytes()
        need(hashlib.sha256(raw).hexdigest()==before[key],'source_before_copy_'+dest)
        with (D/dest).open('xb') as f:f.write(raw)
        need(digest(D/dest)==before[key],'exact_fixed_copy_'+dest)
        manifest[dest]={'source':key,'sha256':before[key]}
    sfiles=['basis.json']+['product-%02d.json'%i for i in range(48)]
    ufiles=['u-basis.json']+['u-product-%02d.json'%i for i in range(48)]
    core=['input-basis.json','frobenius.json','radical-lattice.json','action-kernel.json',
        'numerator-lattice.json','decision.json']+['action-%02d.json'%i for i in range(48)]
    for name in sfiles+ufiles+core+['input_verify.py','verify_u.py','verify.py',
        'decision-335.json','decision-337.json','fixed-independent-multiplier.json',
        'fixed-numerator-lattice.json']:
        copy(name,name)
    original_prefixes=['fixed-S-original-division-','fixed-S-fresh-division-','division-',
        'fixed-U-division-','u-division-','action-division-']
    for prefix in original_prefixes:
        for i in range(48):copy('original343-'+prefix+'%02d.json'%i,prefix+'%02d.json'%i)
    for name in sfiles:
        for dn in ['index-four-table-329','preserved-table-replay-331','preserved-table-audit-333',
                   'index-four-order-two-335','index-eight-audit-337','index-eight-table-339',
                   'index-eight-table-audit-341']:
            need(digest(S/dn/name)==manifest[name]['sha256'],'full_S_provenance_'+dn+'_'+name)
    for name in ufiles:
        for dn in ['index-eight-table-339','index-eight-table-audit-341']:
            need(digest(S/dn/name)==manifest[name]['sha256'],'full_U_provenance_'+dn+'_'+name)
    for i in range(48):
        name='division-%02d.json'%i
        h=manifest['original343-fixed-S-original-'+name]['sha256']
        for dn,n in [('index-four-order-two-335',name),('index-eight-audit-337','fixed-'+name),
                     ('index-eight-table-339','fixed-'+name)]:
            need(digest(S/dn/n)==h,'original_S_division_fixed_provenance')
    save('copy-manifest.json',manifest)
    # Adapt only the separately assessed full-certificate mechanism; never execute a producer.
    source=(S/'index-eight-audit-337/independent.py').read_text()
    def replace_once(text,a,b):
        need(text.count(a)==1,'unique_independent_adaptation_'+a[:70])
        return text.replace(a,b)
    source=replace_once(source,"OLD = D.parent/'index-four-order-two-335'","OLD = D.parent/'index-eight-order-two-343'")
    source=replace_once(source,"table=[read(D/('product-%02d.json'%i)) for i in range(48)]", "table=[read(D/('u-product-%02d.json'%i)) for i in range(48)]")
    import re
    # Only the main fixed-instance specialization changes; general proof-certificate code is identical.
    common,main=source.split('def main():',1)
    main=re.sub(r'\b45\b','44',main)
    main=replace_once(main,'[2]*44+[1]*3','[2]*44+[1]*4')
    main=main.replace('det==8','det==16').replace('==8,','==16,').replace('index=8,','index=16,')
    main=replace_once(main,'action_kernel_dimension=3','action_kernel_dimension=4')
    main=replace_once(main,'124*int(i==0)','248*int(i==0)')
    main=replace_once(main,"'[U:S] = absolute determinant of S basis in U'","'[V:U] = absolute determinant of U basis in V'")
    main=replace_once(main,'independent_index_eight','independent_index_sixteen')
    main=replace_once(main,'action_left_inverse_entries=2025','action_left_inverse_entries=101376,selected_inverse_entries=1936')
    source=common+'def main():'+main
    compile(source,str(D/'independent.py'),'exec')
    with (D/'independent.py').open('x') as f:f.write(source)
    codes={p.name:digest(p) for p in D.glob('*.py')};save('code-hashes.json',codes)
    report['phase']='fresh_complete_S_input_replay'
    iv=run('input_verify.py','input-report.json')
    counts={'product_slots':110592,'product_identities':2304,'remainder_coefficients':218880,
        'transport_entries':18432,'inverse_products':8,'division_certificates':2304,'identity_actions':96}
    for k,x in counts.items():need(iv[k]==x,'entire_S_'+k)
    need(iv['index']==4,'S_index')
    sb=read(D/'basis.json');st=[read(D/('product-%02d.json'%i)) for i in range(48)]
    checked={}
    for prefix in original_prefixes[:3]:
        checked[prefix]=divisions('original343-'+prefix,sb,st)
    fresh_s=divisions('division-',sb,st)
    report['phase']='fresh_complete_U_input_replay'
    uv=run('verify_u.py','u-verification-report.json')
    for k,x in counts.items():need(uv[k]==x,'entire_U_'+k)
    need(uv['index']==8 and uv['scale']==248 and uv['basis_elements']==48,'actual_U_scale_index')
    ub=read(D/'u-basis.json');ut=[read(D/('u-product-%02d.json'%i)) for i in range(48)]
    for prefix in original_prefixes[3:5]:
        checked[prefix]=divisions('original343-'+prefix,ub,ut)
    fresh_u=divisions('u-division-',ub,ut)
    need(read(D/'fixed-numerator-lattice.json')['basis']==read(D/'decision-335.json')['numerator'],
        'full_U_multiplier_input_lattice_equality')
    J=read(D/'radical-lattice.json')['basis']
    checked['action-division-']=divisions('original343-action-division-',ub,ut,J)
    need(set(checked)==set(original_prefixes) and sum(checked.values())==13824,'all_six_original_sets')
    evidence={'status':'PASS','failures':[],'original_sets':checked,'original_divisions':13824,
        'fresh_S_divisions':fresh_s,'fresh_U_divisions':fresh_u,
        'all_actual_dividends_reconstructed':True,'original_evidence_checked_before_kernel_replay':True}
    save('persisted-input-checks.json',evidence)
    report['phase']='full_original_Frobenius_action_kernel_lattice_replay'
    v=run('verify.py','verification-report.json')
    expected={'input_product_slots':110592,'product_slots':110592,'product_identities':2304,
        'remainder_coefficients':218880,'action_slots':110592,'frobenius_slots':13824,
        'frobenius_iterates':6,'exponent':64,'prime':2,'frobenius_rank':1,'radical_dimension':47,
        'action_rank':44,'action_kernel_dimension':4,'index':16,'identity_actions':96,
        'transport_entries':18432,'inverse_products':8,'action_division_certificates':2304,'row_operations':1521}
    for k,x in expected.items():need(v[k]==x,'full_kernel_replay_'+k)
    need(v['decision']=='NOT_2_MAXIMAL','strict_verdict_replayed')
    fresh_action=divisions('action-division-',ub,ut,J)
    report['phase']='independent_full_rank_kernel_and_global_preimage_certificates'
    independent=run('independent.py','independent-report.json')
    for k,x in {'frobenius_rank':1,'action_rank':44,'index':16,'radical_kernel_dimension':47,
        'action_kernel_dimension':4,'independent_preimages':2,'action_entries':110592,
        'full_strict_action_entries':2304,'action_left_inverse_entries':101376}.items():
        need(independent[k]==x,'independent_complete_'+k)
    need(independent['all_load_bearing_certificates_reread'] is True,'persisted_supplement_rechecked')
    for name,obj in [('input-report.json',iv),('u-verification-report.json',uv),
        ('verification-report.json',v),('independent-report.json',independent),
        ('persisted-input-checks.json',evidence)]:need(read(D/name)==obj,'whole_report_roundtrip_'+name)
    need(read(D/'basis.json')==sb and read(D/'u-basis.json')==ub
        and all(read(D/('product-%02d.json'%i))==st[i] and read(D/('u-product-%02d.json'%i))==ut[i]
                for i in range(48)),'complete_fixed_tables_reread')
    report['phase']='final_preservation'
    after={n:digest(ROOT/n) for n in before}
    copies={n:digest(D/n) for n in manifest};code_after={p.name:digest(p) for p in D.glob('*.py')}
    need(before==after and codes==code_after and copies=={n:e['sha256'] for n,e in manifest.items()},
        'all_original_copy_source_hashes_preserved')
    preservation={'equal':True,'before':before,'after':after,
        'fixed_before':{n:e['sha256'] for n,e in manifest.items()},'fixed_after':copies,
        'code_before':codes,'code_after':code_after}
    save('audit-preservation.json',preservation)
    for name,obj in [('audit-preservation.json',preservation),('copy-manifest.json',manifest),
        ('canonical-input-hashes.json',before),('code-hashes.json',codes)]:
        need(read(D/name)==obj,'entire_final_inventory_reread_'+name)
    report.update(status='PASS',phase='complete',decision='NOT_2_MAXIMAL',scale=248,
        frobenius_rank=1,action_rank=44,index=16,radical_kernel_dimension=47,action_kernel_dimension=4,
        original_division_sets=checked,original_divisions=13824,fresh_divisions=fresh_s+fresh_u+fresh_action,
        original_files=len(before),fixed_copies=len(manifest),code_files=len(codes),replay_counts=expected,
        independent_preimages=2,all_load_bearing_certificates_reread=True)
except Exception as e:report.update(status='STOP',failures=[type(e).__name__+': '+str(e)])
report.update(seconds=time.monotonic()-START,required_seconds=180,required_bytes=134217728)
save('audit-report.json',report);print(json.dumps(report))
sys.exit(0 if report['status']=='PASS' else 1)
