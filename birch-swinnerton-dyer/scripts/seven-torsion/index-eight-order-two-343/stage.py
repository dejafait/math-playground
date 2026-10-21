"""Entire U: complete input replay, one modular test, independent replay."""
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
report={'status':'STOP','failures':[],'phase':'setup'}
try:
    prior=S/'index-eight-table-audit-341';table_source=S/'index-eight-table-339'
    old=S/'index-four-order-two-335';audit=S/'index-eight-audit-337'
    prior_hashes=read(prior/'canonical-input-hashes.json');names=set(prior_hashes)
    for folder in [prior,table_source,old,audit]:
        names.update(str(p.relative_to(ROOT)) for p in folder.rglob('*') if p.is_file())
    names.update(['lemmas/L088-conductor389-index-eight-multiplier-order-table.md',
        'drafts/literature/2026-10-19-index-eight-order-prime-two-test.md',
        'history/341-2026-10-19-index-eight-table-critical-audit.md',
        'history/342-2026-10-19-index-eight-order-two-scope-review.md'])
    before={n:digest(ROOT/n) for n in sorted(names)}
    lemma='lemmas/L088-conductor389-index-eight-multiplier-order-table.md'
    need(all(before[n]==h for n,h in prior_hashes.items() if n!=lemma),'all_other_post341_inputs_unchanged')
    save('canonical-input-hashes.json',before)
    save('inventory-transition.json',{'only_permitted_post341_document_change':lemma,
        'prior':prior_hashes[lemma],'current':before[lemma],
        'reason':'Step 341 appended its recorded separate critical audit after preservation.',
        'retained_post337_transition':read(table_source/'inventory-transition.json')})
    manifest={}
    def copy(dest,src):
        raw=src.read_bytes();expected=before[str(src.relative_to(ROOT))]
        need(hashlib.sha256(raw).hexdigest()==expected,'source_before_copy_'+dest)
        with (D/dest).open('xb') as f:f.write(raw)
        need(digest(D/dest)==expected,'fixed_copy_'+dest)
        manifest[dest]={'source':str(src.relative_to(ROOT)),'sha256':expected}
    fixed=['basis.json']+['product-%02d.json'%i for i in range(48)]
    for n in fixed:
        copy(n,table_source/n)
        for dn in ['index-four-table-329','preserved-table-replay-331','preserved-table-audit-333',
                   'index-four-order-two-335','index-eight-audit-337','index-eight-table-audit-341']:
            need(digest(S/dn/n)==manifest[n]['sha256'],'all_S_provenance_'+dn+'_'+n)
    for n in ['u-basis.json']+['u-product-%02d.json'%i for i in range(48)]:
        copy(n,table_source/n)
        need(digest(prior/n)==manifest[n]['sha256'],'all_49_U_fixed_bytes_'+n)
    for i in range(48):
        n='division-%02d.json'%i
        copy('fixed-S-original-'+n,table_source/('fixed-'+n))
        need(digest(old/n)==manifest['fixed-S-original-'+n]['sha256']
            and digest(audit/('fixed-'+n))==manifest['fixed-S-original-'+n]['sha256'],
            'retained_original_S_division_provenance')
        copy('fixed-S-fresh-'+n,table_source/n)
        copy('fixed-U-'+n,table_source/('u-'+n))
    for n in ['input_verify.py','verify_u.py','decision-335.json','decision-337.json',
              'fixed-independent-multiplier.json','fixed-numerator-lattice.json']:
        copy(n,table_source/n)
        need(digest(prior/n)==manifest[n]['sha256'],'required_341_copy_'+n)
    save('copy-manifest.json',manifest)
    code={p.name:digest(p) for p in D.glob('*.py')};save('code-hashes.json',code)
    report['phase']='full_S_replay'
    iv=run('input_verify.py','input-report.json')
    counts={'product_slots':110592,'product_identities':2304,'remainder_coefficients':218880,
        'transport_entries':18432,'inverse_products':8,'division_certificates':2304,'identity_actions':96}
    for k,x in counts.items():need(iv[k]==x,'S_complete_'+k)
    need(iv['index']==4,'S_index')
    sb=read(D/'basis.json');st=[read(D/('product-%02d.json'%i)) for i in range(48)]
    s_orig=divisions('fixed-S-original-division-',sb,st)
    s_339=divisions('fixed-S-fresh-division-',sb,st)
    s_fresh=divisions('division-',sb,st)
    report['phase']='full_U_replay'
    uv=run('verify_u.py','u-verification-report.json')
    for k,x in counts.items():need(uv[k]==x,'U_complete_'+k)
    need(uv['index']==8 and uv['scale']==248 and uv['basis_elements']==48,'entire_U_scale_and_index')
    ub=read(D/'u-basis.json');ut=[read(D/('u-product-%02d.json'%i)) for i in range(48)]
    u_orig=divisions('fixed-U-division-',ub,ut);u_fresh=divisions('u-division-',ub,ut)
    numerator=read(D/'fixed-numerator-lattice.json');dc=read(D/'decision-335.json')
    need(numerator['basis']==dc['numerator'],'whole_audited_U_numerator_lattice')
    validation={'status':'PASS','failures':[],'all_before_modular_production':True,
        'complete_S_replay':iv,'complete_U_replay':uv,'original_S_divisions':s_orig,
        'step339_S_divisions':s_339,'fresh_S_divisions':s_fresh,'original_U_divisions':u_orig,
        'fresh_U_divisions':u_fresh,'full_audited_U_lattice_checked':True}
    save('input-validation.json',validation)
    report['phase']='one_full_U_test'
    p=run('produce.py','producer-report.json')
    v=run('verify.py','verification-report.json')
    for r,label in [(p,'producer'),(v,'independent')]:
        for k,x in {'input_product_slots':110592,'action_slots':110592,'frobenius_slots':13824,
                    'frobenius_iterates':6,'exponent':64,'prime':2}.items():need(r[k]==x,label+'_complete_'+k)
    for k in ['decision','index','frobenius_rank','radical_dimension','action_rank','action_kernel_dimension']:
        need(p[k]==v[k],'independent_full_result_'+k)
    need(v['action_division_certificates']==2304,'all_action_divisions_persisted')
    actions=divisions('action-division-',ub,ut,read(D/'radical-lattice.json')['basis'])
    final=read(D/'decision.json')
    need(final['decision']==v['decision'] and final['index']==v['index'],'full_final_verdict')
    # Complete reports, table/basis bytes and all producer certificates were reread
    # by the independent verifier or actual-dividend checks above; bind reports here.
    for n,r in [('input-report.json',iv),('u-verification-report.json',uv),
                ('input-validation.json',validation),('producer-report.json',p),('verification-report.json',v)]:
        need(read(D/n)==r,'complete_report_reread_'+n)
    need(read(D/'u-basis.json')==ub and read(D/'basis.json')==sb
        and all(read(D/('u-product-%02d.json'%i))==ut[i] and read(D/('product-%02d.json'%i))==st[i]
                for i in range(48)),'full_input_roundtrips')
    report['phase']='preservation'
    after={n:digest(ROOT/n) for n in before};copies={n:digest(D/n) for n in manifest}
    code_after={p.name:digest(p) for p in D.glob('*.py')}
    need(before==after and code==code_after and copies=={n:x['sha256'] for n,x in manifest.items()},
        'all_original_fixed_copy_and_source_preservation')
    preservation={'equal':True,'before':before,'after':after,'code_before':code,'code_after':code_after,
        'fixed_before':{n:x['sha256'] for n,x in manifest.items()},'fixed_after':copies}
    save('preservation-stage.json',preservation)
    need(read(D/'preservation-stage.json')==preservation and read(D/'copy-manifest.json')==manifest
        and read(D/'canonical-input-hashes.json')==before and read(D/'code-hashes.json')==code,
        'complete_inventory_rereads')
    report.update(status='PASS',phase='complete',decision=final['decision'],index=final['index'],
        frobenius_rank=v['frobenius_rank'],radical_dimension=v['radical_dimension'],
        action_rank=v['action_rank'],action_kernel_dimension=v['action_kernel_dimension'],
        input_product_slots=110592,action_slots=110592,frobenius_slots=13824,scale=248,
        row_operations=v['row_operations'],original_S_divisions=s_orig,step339_S_divisions=s_339,
        fresh_S_divisions=s_fresh,original_U_divisions=u_orig,fresh_U_divisions=u_fresh,
        persisted_action_divisions=actions,all_actual_dividends_checked=True,
        original_files=len(before),fixed_copies=len(manifest),code_files=len(code))
except Exception as e:report.update(status='STOP',failures=[type(e).__name__+': '+str(e)])
report.update(seconds=time.monotonic()-START,required_seconds=180,required_bytes=134217728)
save('stage-report.json',report);print(json.dumps(report))
sys.exit(0 if report['status']=='PASS' else 1)
