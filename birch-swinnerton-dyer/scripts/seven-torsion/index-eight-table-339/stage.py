"""Inclusive setup, full S input validation, one U production/replay, preservation."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json,subprocess,sys,time
sys.set_int_max_str_digits(0)
D=Path(__file__).resolve().parent; ROOT=D.parents[2]; S=D.parent; START=time.monotonic()
def read(p):return json.loads(p.read_text())
def need(x,s):
    if not x:raise ArithmeticError(s)
def save(n,x):
    with (D/n).open('x') as f:json.dump(x,f,separators=(',',':'));f.write('\n')
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def run(name,report):
    with (D/(name+'.log')).open('x') as log:
        rc=subprocess.run([sys.executable,'-B',str(D/name)],stdout=log,stderr=subprocess.STDOUT).returncode
    need(rc==0,'first_failure_'+name+'_exit_'+str(rc))
    result=read(D/report);need(result['status']=='PASS' and not result['failures'],'full_'+report)
    return result
def divisions(prefix,basis,products):
    V=basis['scaled_polynomials'];H=basis['H'];scale=basis['scale'];count=0
    for i in range(48):
        cert=read(D/(prefix+'%02d.json'%i))
        need(type(cert['i']) is int and cert['i']==i and len(cert['products'])==48,'full_division_row')
        for j,e in enumerate(cert['products']):
            need(type(e['j']) is int and e['j']==j and len(e['dividend'])==95
                and all(type(x) is int for x in e['dividend']) and len(e['quotient'])==47
                and len(e['remainder'])==95 and all(type(x) is str for x in e['quotient']+e['remainder']),
                'complete_exact_division_types')
            actual=[0]*95
            # Independently expand from the actual basis and product row, not saved dividend labels.
            for a in range(48):
                for b in range(48):
                    if V[i][a] and V[j][b]:actual[a+b]+=V[i][a]*V[j][b]
            for k,c in enumerate(products[i][j]):
                if c:
                    for a,x in enumerate(V[k]):
                        if x:actual[a]-=scale*c*x
            need(actual==e['dividend'],'all_actual_dividend_positions_'+str((prefix,i,j)))
            q=list(map(F,e['quotient']));rem=list(map(F,e['remainder']))
            need(not any(rem),'all_remainder_positions_zero')
            reconstructed=rem[:]
            for a,x in enumerate(q):
                if x:
                    for b,h in enumerate(H):
                        if h:reconstructed[a+b]+=x*h
            need(actual==reconstructed,'whole_persisted_H_division_'+str((prefix,i,j)));count+=1
    need(count==2304,'all_persisted_divisions');return count
report={'status':'STOP','failures':[],'phase':'setup'}
try:
    prior=S/'index-eight-audit-337';old=S/'index-four-order-two-335'
    prior_hashes=read(prior/'canonical-input-hashes.json');names=set(prior_hashes)
    names.update(str(p.relative_to(ROOT)) for p in prior.rglob('*') if p.is_file())
    names.update(str(p.relative_to(ROOT)) for p in old.rglob('*') if p.is_file())
    names.update(['drafts/literature/2026-10-19-index-eight-multiplier-table.md',
        'history/337-2026-10-19-index-eight-critical-audit.md',
        'history/338-2026-10-19-index-eight-table-source-approval.md'])
    before={n:digest(ROOT/n) for n in sorted(names)}
    # L087's documented audit addendum followed step 337's pre-addendum inventory.
    lemma='lemmas/L087-conductor389-index-four-order-not-2-maximal.md'
    need(all(before[n]==h for n,h in prior_hashes.items() if n!=lemma),'all_other_prior_inputs_unchanged')
    save('canonical-input-hashes.json',before)
    save('inventory-transition.json',{'only_permitted_post337_document_change':lemma,
        'prior':prior_hashes[lemma],'current':before[lemma],
        'reason':'Step 337 appended its recorded separate critical audit after preservation.'})
    manifest={}
    def copy(dest,src):
        raw=src.read_bytes();expected=before[str(src.relative_to(ROOT))]
        need(hashlib.sha256(raw).hexdigest()==expected,'source_before_copy_'+dest)
        with (D/dest).open('xb') as f:f.write(raw)
        need(digest(D/dest)==expected,'full_copy_'+dest)
        manifest[dest]={'source':str(src.relative_to(ROOT)),'sha256':expected}
    fixed=['basis.json']+['product-%02d.json'%i for i in range(48)]
    for name in fixed:
        copy(name,old/name)
        for dn in ['index-four-table-329','preserved-table-replay-331','preserved-table-audit-333','index-eight-audit-337']:
            need(digest(S/dn/name)==manifest[name]['sha256'],'complete_fixed_provenance_'+dn+'_'+name)
    for i in range(48):
        name='division-%02d.json'%i;copy('fixed-'+name,old/name)
        need(digest(prior/('fixed-'+name))==manifest['fixed-'+name]['sha256'],'original_division_337_'+name)
    copy('input_verify.py',old/'input_verify.py')
    copy('decision-335.json',old/'decision.json');copy('decision-337.json',prior/'decision.json')
    copy('fixed-independent-multiplier.json',prior/'independent-multiplier.json')
    copy('fixed-numerator-lattice.json',prior/'numerator-lattice.json')
    save('copy-manifest.json',manifest)
    code={p.name:digest(p) for p in D.glob('*.py')};save('code-hashes.json',code)
    report['phase']='complete_S_validation'
    iv=run('input_verify.py','input-report.json')
    for k,x in {'product_slots':110592,'product_identities':2304,'remainder_coefficients':218880,
        'transport_entries':18432,'inverse_products':8,'division_certificates':2304,'identity_actions':96,'index':4}.items():
        need(iv[k]==x,'complete_input_count_'+k)
    basis=read(D/'basis.json');table=[read(D/('product-%02d.json'%i)) for i in range(48)]
    original=divisions('fixed-division-',basis,table);fresh=divisions('division-',basis,table)
    decision=read(D/'decision-335.json');ind=read(D/'fixed-independent-multiplier.json')
    numerator=read(D/'fixed-numerator-lattice.json')
    M=[[F(int(i==j),2 if j>=45 else 1) for j in range(48)] for i in range(48)]
    T=[[int(i==j)*(2 if j>=45 else 1) for j in range(48)] for i in range(48)]
    Q=[[2*x for x in r] for r in M]
    need(decision==read(D/'decision-337.json') and [[F(x) for x in r] for r in decision['M']]==M
        and decision['inverse']==T and decision['numerator']==Q and decision['index']==decision['determinant']==8,
        'entire_U_lattice_before_production')
    need(numerator['basis']==Q and [[F(x) for x in r] for r in ind['basis']]==M
        and ind['numerator']==Q and ind['inclusion']==T and ind['determinant']==8
        and ind['identity']==basis['identity'] and ind['identity_in_multiplier']==decision['identity_in_multiplier'],
        'full_audited_lattice_and_identity_before_production')
    save('input-validation.json',{'status':'PASS','failures':[],'original_actual_divisions':original,
        'fresh_actual_divisions':fresh,'complete_S_replay':iv,'full_U_lattice_checked':True,
        'all_input_obligations_before_production':True})
    report['phase']='one_production'
    p=run('produce.py','producer-report.json')
    need(p['product_slots']==110592 and p['products']==2304 and p['index']==8 and p['scale']==248,'full_production')
    report['phase']='independent_U_replay'
    v=run('verify_u.py','u-verification-report.json')
    for k,x in {'product_slots':110592,'product_identities':2304,'remainder_coefficients':218880,
        'transport_entries':18432,'inverse_products':8,'division_certificates':2304,
        'identity_actions':96,'index':8,'scale':248,'basis_elements':48}.items():need(v[k]==x,'complete_U_'+k)
    ub=read(D/'u-basis.json');ut=[read(D/('u-product-%02d.json'%i)) for i in range(48)]
    actual=divisions('u-division-',ub,ut)
    need(read(D/'u-verification-report.json')==v and read(D/'producer-report.json')==p
        and read(D/'input-report.json')==iv and read(D/'input-validation.json')['all_input_obligations_before_production'],
        'full_report_rereads')
    # Reread every produced basis/product byte and all exact transport strings.
    need(read(D/'u-basis.json')==ub and all(read(D/('u-product-%02d.json'%i))==ut[i] for i in range(48)),
        'all_output_roundtrips')
    report['phase']='final_preservation'
    after={n:digest(ROOT/n) for n in before};copies={n:digest(D/n) for n in manifest}
    code_after={p.name:digest(p) for p in D.glob('*.py')}
    need(before==after and code==code_after and copies=={n:x['sha256'] for n,x in manifest.items()},
        'all_original_copy_and_source_preservation')
    save('preservation-stage.json',{'equal':True,'before':before,'after':after,'code_before':code,'code_after':code_after,
        'fixed_before':{n:x['sha256'] for n,x in manifest.items()},'fixed_after':copies})
    report.update(status='PASS',phase='complete',original_files=len(before),fixed_copies=len(manifest),
        code_files=len(code),original_S_divisions=original,fresh_S_divisions=fresh,U_divisions=actual,
        product_slots=110592,product_identities=2304,transport_entries=18432,inverse_products=8,
        identity_actions=96,index=8,scale=248,all_actual_dividends_checked=True)
except Exception as e:report.update(status='STOP',failures=[type(e).__name__+': '+str(e)])
report.update(seconds=time.monotonic()-START,required_seconds=180,required_bytes=134217728)
save('stage-report.json',report);print(json.dumps(report))
sys.exit(0 if report['status']=='PASS' else 1)
