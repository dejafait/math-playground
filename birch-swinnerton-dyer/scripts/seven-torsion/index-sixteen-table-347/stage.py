"""Complete V table: full fixed inputs, one production, independent original-H replay."""
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

def shape(a,h,w):
    need(type(a) is list and len(a)==h and all(type(r) is list and len(r)==w for r in a),'integer_matrix_shape')
    need(all(type(x) is int for r in a for x in r),'all_integer_entries')
def rat(a):
    need(all(type(x) in (str,int) for r in a for x in r),'no_float_rationals')
    return [[F(x) for x in r] for r in a]
def prepare_sources():
    # Source adaptation only; no historical producer, stage or wrapper executes.
    def replace(t,a,b):
        need(a in t,'source_adaptation_found_'+a[:60]);return t.replace(a,b)
    p=(S/'index-eight-table-339/produce.py').read_text()
    for a,b in [("read('basis.json')","read('u-basis.json')"),
        ('decision-335.json','decision-343.json'),('[1]*45+[2]*3','[1]*44+[2]*4'),
        ("'prior_scales':[31,62,124]","'prior_scales':[31,62,124,248]"),
        ("'input_scale':124","'input_scale':248"),("'index':8","'index':16"),
        ('248','496'),("'basis_in_s'","'basis_in_u'"),
        ("read('product-","read('u-product-"),('u-basis.json', 'v-basis.json'),
        ('u-product-','v-product-'),('index=8','index=16')]:
        p=replace(p,a,b)
    # Above filename replacements also touched the old-input reads: restore only those two.
    p=replace(p,"old=read('v-basis.json')", "old=read('u-basis.json')")
    p=replace(p,"source=read('v-product-", "source=read('u-product-")
    # A blanket scale substitution would change input metadata; enforce exact chain.
    p=replace(p,"'prior_scales':[31,62,124,496]", "'prior_scales':[31,62,124,248]")
    p=replace(p,"'input_scale':496", "'input_scale':248")
    v=(S/'index-eight-table-339/verify_u.py').read_text()
    for a,b in [("old=read('basis.json'); got=read('u-basis.json')", "old=read('u-basis.json'); got=read('v-basis.json')"),
        ('decision-335.json','decision-343.json'),('decision-337.json','decision-345.json'),
        ('fixed-independent-multiplier.json','V-independent-multiplier.json'),
        ('>=45','>=44'),("==8", "==16"),("d['kernel_dimension']==3", "d['kernel_dimension']==4"),
        ('[U:S] = absolute determinant of S basis in U','[V:U] = absolute determinant of U basis in V'),
        ("got['basis_in_s']", "got['basis_in_u']"),
        ("old['scale']==124 and old['original_scale']==31 and old['input_scale']==62\n        and got['scale']==248 and got['input_scale']==124", "old['scale']==248 and old['original_scale']==31 and old['input_scale']==124\n        and got['scale']==496 and got['input_scale']==248"),
        ("got['prior_scales']==[31,62,124]", "got['prior_scales']==[31,62,124,248]"),
        ("column=[F(248*", "column=[F(496*"),
        ("read('u-product-", "read('v-product-"),('poly[a]-=248*z*x','poly[a]-=496*z*x'),
        ("save('u-division-", "save('v-division-"),('scale=248','scale=496'),
        ('u-verification-report.json','v-verification-report.json')]:
        v=replace(v,a,b)
    # Human-facing labels have no mathematical role; make the instance explicit.
    v=v.replace('Independent U replay','Independent V replay').replace('audited_U','audited_V')
    for name,source in [('produce.py',p),('verify_v.py',v)]:
        compile(source,str(D/name),'exec')
        with (D/name).open('x') as f:f.write(source)

report={'status':'STOP','failures':[],'phase':'initial_inventory'}
try:
    OLD=S/'index-eight-order-two-343';PRIOR=S/'U-two-audit-345'
    previous=read(PRIOR/'canonical-input-hashes.json')
    need(len(previous)==2706,'entire_step345_input_inventory')
    names=set(previous)
    for folder in (OLD,PRIOR):
        names.update(str(p.relative_to(ROOT)) for p in folder.rglob('*') if p.is_file())
    names.update(['drafts/literature/2026-10-19-index-sixteen-multiplier-table.md',
        'drafts/2026-10-19-U-two-critical-audit-attempt.md',
        'drafts/2026-10-19-index-sixteen-table-attempt.md',
        'history/345-2026-10-19-U-two-critical-audit.md',
        'scripts/seven-torsion/index-eight-table-339/produce.py',
        'scripts/seven-torsion/index-eight-table-339/verify_u.py'])
    before={n:digest(ROOT/n) for n in sorted(names)}
    lemma='lemmas/L089-conductor389-index-eight-order-not-2-maximal.md'
    oldhash='cc34fd9b31bb86510b4e362dd91221b1119d081a4864eda3234239aa7c8fb40a'
    newhash='b65b37847b15c3fcb3f20495cf59ce3bb30ba4fe4bb57e9b70f04f60235edced'
    need(previous[lemma]==oldhash and before[lemma]==newhash,'exact_documented_L089_addendum_transition')
    need(all(before[n]==h for n,h in previous.items() if n!=lemma),'every_other_step345_input_unchanged')
    save('canonical-input-hashes.json',before)
    save('inventory-transition.json',{'only_permitted_post345_document_change':lemma,
        'prior':oldhash,'current':newhash,
        'reason':'Exact post-audit L089 addendum transition recorded in drafts/2026-10-19-U-two-critical-audit-attempt.md.',
        'retained_step345_transition':read(PRIOR/'inventory-transition.json')})
    for folder,count in [(OLD,248),(PRIOR,447)]:
        manifest=read(folder/'copy-manifest.json');need(len(manifest)==count,'complete_prior_manifest')
        for name,e in manifest.items():
            need(before[e['source']]==e['sha256']==before[str((folder/name).relative_to(ROOT))],
                'every_prior_copy_and_source_'+str(folder.name)+'_'+name)
    manifest={}
    def copyfrom(dest,src):
        key=str(src.relative_to(ROOT));raw=src.read_bytes()
        need(hashlib.sha256(raw).hexdigest()==before[key],'source_before_copy_'+dest)
        with (D/dest).open('xb') as f:f.write(raw)
        need(digest(D/dest)==before[key],'exact_copy_'+dest)
        manifest[dest]={'source':key,'sha256':before[key]}
    def copy(dest,name):copyfrom(dest,OLD/name)
    sfiles=['basis.json']+['product-%02d.json'%i for i in range(48)]
    ufiles=['u-basis.json']+['u-product-%02d.json'%i for i in range(48)]
    core=['radical-lattice.json','numerator-lattice.json','decision.json']+['action-%02d.json'%i for i in range(48)]
    for name in sfiles+ufiles+core+['input_verify.py','verify_u.py',
        'decision-335.json','decision-337.json','fixed-independent-multiplier.json','fixed-numerator-lattice.json']:
        copy(name,name)
    prefixes=['fixed-S-original-division-','fixed-S-fresh-division-','division-',
        'fixed-U-division-','u-division-','action-division-']
    for prefix in prefixes:
        for i in range(48):copy('original343-'+prefix+'%02d.json'%i,prefix+'%02d.json'%i)
    for name in sfiles:
        for dn in ['index-four-table-329','preserved-table-replay-331','preserved-table-audit-333',
            'index-four-order-two-335','index-eight-audit-337','index-eight-table-339','index-eight-table-audit-341']:
            need(digest(S/dn/name)==manifest[name]['sha256'],'entire_S_provenance_'+dn+'_'+name)
    for name in ufiles:
        for dn in ['index-eight-table-339','index-eight-table-audit-341','U-two-audit-345']:
            need(digest(S/dn/name)==manifest[name]['sha256'],'entire_U_provenance_'+dn+'_'+name)
    for dest,src in [('decision-343.json',OLD/'decision.json'),('decision-345.json',PRIOR/'decision.json'),
        ('V-numerator-343.json',OLD/'numerator-lattice.json'),('V-numerator-345.json',PRIOR/'numerator-lattice.json'),
        ('V-independent-multiplier.json',PRIOR/'independent-multiplier.json'),
        ('V-independent-preimage.json',PRIOR/'numerator-independent-preimage.json')]:copyfrom(dest,src)
    save('copy-manifest.json',manifest)
    prepare_sources()
    codes={p.name:digest(p) for p in D.glob('*.py')};save('code-hashes.json',codes)
    report['phase']='complete_S_U_input_validation'
    iv=run('input_verify.py','input-report.json')
    counts={'product_slots':110592,'product_identities':2304,'remainder_coefficients':218880,
        'transport_entries':18432,'inverse_products':8,'division_certificates':2304,'identity_actions':96}
    for k,x in counts.items():need(iv[k]==x,'full_S_'+k)
    need(iv['index']==4,'actual_S_index')
    sb=read(D/'basis.json');st=[read(D/('product-%02d.json'%i)) for i in range(48)]
    checked={p:divisions('original343-'+p,sb,st) for p in prefixes[:3]}
    fresh_s=divisions('division-',sb,st)
    uv=run('verify_u.py','u-verification-report.json')
    for k,x in counts.items():need(uv[k]==x,'full_U_'+k)
    need(uv['index']==8 and uv['scale']==248 and uv['basis_elements']==48,'actual_U_scale_index')
    ub=read(D/'u-basis.json');ut=[read(D/('u-product-%02d.json'%i)) for i in range(48)]
    for p in prefixes[3:5]:checked[p]=divisions('original343-'+p,ub,ut)
    fresh_u=divisions('u-division-',ub,ut)
    J=read(D/'radical-lattice.json')['basis']
    checked['action-division-']=divisions('original343-action-division-',ub,ut,J)
    need(set(checked)==set(prefixes) and sum(checked.values())==13824,'six_complete_original_division_sets')
    report['phase']='full_audited_V_lattice_interfaces'
    dc=read(D/'decision-343.json');ind=read(D/'V-independent-multiplier.json')
    nc=read(D/'V-numerator-343.json');pe=read(D/'V-independent-preimage.json')
    I=[[int(i==j) for j in range(48)] for i in range(48)]
    M=[[F(int(i==j),2 if j>=44 else 1) for j in range(48)] for i in range(48)]
    T=[[int(i==j)*(2 if i>=44 else 1) for j in range(48)] for i in range(48)]
    Q=[[int(2*x) for x in row] for row in M]
    need(dc==read(D/'decision-345.json') and nc==read(D/'V-numerator-345.json'), 'whole_original_audited_V_interfaces')
    need(rat(dc['M'])==M and dc['inverse']==T and dc['numerator']==Q
        and dc['index']==dc['determinant']==16 and dc['kernel_dimension']==4
        and dc['decision']=='NOT_2_MAXIMAL','complete_V_decision')
    need(rat(ind['basis'])==M and ind['numerator']==Q and ind['inclusion']==T
        and ind['determinant']==16 and ind['index_orientation']=='[V:U] = absolute determinant of U basis in V',
        'entire_independent_V_multiplier')
    need(mm(M,T)==I and mm(T,M)==I,'both_V_multiplier_inverse_products')
    G=tr(I[44:]+[[2*x for x in row] for row in I])
    for a,h,w in [(Q,48,48),(G,48,52),(nc['C'],52,48),(nc['D'],48,52),
        (pe['G_to_basis'],52,48),(pe['basis_to_G'],48,52)]:shape(a,h,w)
    QI=rat(nc['inverse']);PI=rat(pe['inverse'])
    need(nc['rank']==48 and nc['basis']==pe['basis']==Q and nc['S']==pe['generators']==G
        and pe['kernel_rows']==I[44:],'whole_global_numerator_preimage_inputs')
    need(mm(G,nc['C'])==Q and mm(Q,nc['D'])==G and mm(Q,QI)==I and mm(QI,Q)==I,
        'original_both_integer_preimage_generations_and_inverses')
    need(mm(G,pe['G_to_basis'])==Q and mm(Q,pe['basis_to_G'])==G
        and mm(Q,PI)==I and mm(PI,Q)==I,'independent_both_integer_preimage_generations_and_inverses')
    forward=rat(pe['saved_basis_in_displayed']);back=rat(pe['displayed_basis_in_saved'])
    need(all(F(x).denominator==1 for a in (forward,back) for row in a for x in row)
        and mm(Q,forward)==nc['basis'] and mm(nc['basis'],back)==Q
        and mm(forward,back)==I and mm(back,forward)==I,'both_integral_lattice_containments')
    need(ind['identity']==ub['identity'] and ind['identity_in_multiplier']==dc['identity_in_multiplier']
        and mm(M,tr([ind['identity_in_multiplier']]))==tr([ub['identity']]),'entire_actual_V_identity_interfaces')
    evidence={'status':'PASS','failures':[],'original_sets':checked,'original_divisions':13824,
        'fresh_S_divisions':fresh_s,'fresh_U_divisions':fresh_u,'all_actual_dividends_checked':True,
        'whole_V_lattice_and_both_global_preimages_checked':True,'all_inputs_before_production':True}
    save('input-validation.json',evidence)
    report['phase']='one_V_table_production'
    p=run('produce.py','producer-report.json')
    need(p['products']==2304 and p['product_slots']==110592 and p['index']==16 and p['scale']==496,'whole_V_production')
    report['phase']='independent_original_H_V_replay'
    v=run('verify_v.py','v-verification-report.json')
    for k,x in counts.items():need(v[k]==x,'full_V_'+k)
    need(v['index']==16 and v['scale']==496 and v['basis_elements']==48,'actual_V_scale_index')
    vb=read(D/'v-basis.json');vt=[read(D/('v-product-%02d.json'%i)) for i in range(48)]
    vd=divisions('v-division-',vb,vt)
    for name,obj in [('input-report.json',iv),('u-verification-report.json',uv),
        ('producer-report.json',p),('v-verification-report.json',v),('input-validation.json',evidence)]:
        need(read(D/name)==obj,'complete_report_reread_'+name)
    for bn,tn,b,t in [('basis.json','product-',sb,st),('u-basis.json','u-product-',ub,ut),('v-basis.json','v-product-',vb,vt)]:
        need(read(D/bn)==b and all(read(D/(tn+'%02d.json'%i))==t[i] for i in range(48)), 'whole_basis_table_reread_'+bn)
    report['phase']='final_preservation'
    after={n:digest(ROOT/n) for n in before};copies={n:digest(D/n) for n in manifest}
    code_after={p.name:digest(p) for p in D.glob('*.py')}
    need(before==after and codes==code_after and copies=={n:e['sha256'] for n,e in manifest.items()},'all_original_copy_source_preservation')
    preservation={'equal':True,'before':before,'after':after,'fixed_before':{n:e['sha256'] for n,e in manifest.items()},
        'fixed_after':copies,'code_before':codes,'code_after':code_after}
    save('preservation-stage.json',preservation)
    for name,obj in [('preservation-stage.json',preservation),('copy-manifest.json',manifest),
        ('canonical-input-hashes.json',before),('code-hashes.json',codes)]:need(read(D/name)==obj,'full_inventory_reread_'+name)
    report.update(status='PASS',phase='complete',index=16,scale=496,product_slots=110592,products=2304,
        transport_entries=18432,inverse_products=8,identity_actions=96,
        original_divisions=13824,fresh_S_U_divisions=fresh_s+fresh_u,V_divisions=vd,
        original_files=len(before),fixed_copies=len(manifest),code_files=len(codes),all_actual_dividends_checked=True)
except Exception as e:report.update(status='STOP',failures=[type(e).__name__+': '+str(e)])
report.update(seconds=time.monotonic()-START,required_seconds=180,required_bytes=134217728)
save('stage-report.json',report);print(json.dumps(report))
sys.exit(0 if report['status']=='PASS' else 1)
