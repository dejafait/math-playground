"""One index-64 table attempt; fixed verdict evidence is replayed, never produced."""
from pathlib import Path
import json,sys,textwrap,time,hashlib
D=Path(__file__).resolve().parent;S=D.parent

def change(t,a,b):
    if t.count(a)!=1:raise ValueError('unique_adaptation_'+a[:80])
    return t.replace(a,b)
# This preparation itself runs only inside the external watchdog.
src=(S/'W-two-audit-361/audit.py').read_text()
src=src.split('    # Adapt only the already assessed independent full rank/preimage instance.\n',1)[0]
extra='''
    fixed361=S/'W-two-audit-361'
    previous361=read(fixed361/'audit-input-hashes.json')
    need(len(previous361)==8040,'entire_8040_step361_inventory')
    audit_names.update(previous361)
    audit_names.update(str(p.relative_to(ROOT)) for p in fixed361.rglob('*') if p.is_file())
    audit_names.update(['drafts/literature/2026-10-20-index-sixty-four-multiplier-table.md',
        'drafts/2026-10-20-index-sixty-four-table-attempt.md',
        'history/361-2026-10-20-W-two-critical-audit.md',
        'history/362-2026-10-20-index64-table-scope.md'])
'''
src=change(src,'    audit_before={n:digest(ROOT/n) for n in sorted(audit_names)}',extra+'    audit_before={n:digest(ROOT/n) for n in sorted(audit_names)}')
transition='''
    post361={
        'lemmas/L093-conductor389-index-thirty-two-order-not-2-maximal.md':
        ('a23cf1537577dbb1bfbfd85efb8b5f4c1c7d9865a3d1763dd00cf8f9d24a4344','06775693da9f08d6a43b3aced0f97fc8b84ca68eda4d6f77799c58e84ca976b5'),
        'drafts/2026-10-20-W-two-critical-audit-attempt.md':
        ('a1772ff757b2cf9133778b96236aab4248c3c157baf780d16da7e71412a95367','f981d3e7c19c11161c5503046328e7dff1ad82f48bcc63dc9442b05a03d63a5b')}
    hist361='history/361-2026-10-20-W-two-critical-audit.md'
    h361='5f01bba525a8e7b0aa262c51ef00565ce2637fce631c6e45431c77f682da01f2'
    need(audit_before[hist361]==h361,'exact_history361_hash')
    history361=(ROOT/hist361).read_text()
    for n,(a,b) in post361.items():
        need(previous361[n]==a and audit_before[n]==b and a in history361 and b in history361,
            'exact_post361_bound_to_inventory_and_history_'+n)
    note361='drafts/2026-10-20-W-two-critical-audit-attempt.md'
    raw361=(ROOT/note361).read_bytes(); marker361=b'\\n## Completed execution\\n'
    need(raw361.count(marker361)==1 and hashlib.sha256(raw361.split(marker361)[0]).hexdigest()==post361[note361][0],
        'exact_step361_note_append')
    need(all(audit_before[n]==h for n,h in previous361.items() if n not in post361),'every_other_step361_original')
    mf361=read(fixed361/'audit-complete-copy-manifest.json')
    need(len(mf361)==377,'all_377_step361_copy_bindings')
    for n,e in mf361.items():
        need(audit_before[e['source']]==e['sha256']==audit_before[str((fixed361/n).relative_to(ROOT))],
            'whole_step361_copy_binding_'+n)
    cd361=read(fixed361/'code-hashes.json');need(len(cd361)==17,'all_17_step361_sources')
    need(all(digest(fixed361/n)==h for n,h in cd361.items()),'every_step361_source_hash')
    save('post361-transition.json',{'exact_changes':post361,'history':hist361,'history_sha256':h361,
        'every_other_original_unchanged':True,'no_pathname_exemptions':True})
'''
src=change(src,"    note359='drafts/2026-10-20-W-two-attempt.md'",transition+"    note359='drafts/2026-10-20-W-two-attempt.md'")
# Extend the saved independent direct systems through the entire audit copy.
src=change(src,"    with (D/'w_main.txt').open('x') as f:f.write(wmain)",'''
    wa="    for c in original359['systems'].values(): reread(c)\\n"
    need(wmain.count(wa)==1,'unique_step361_W_copy_comparison')
    wmain=wmain.replace(wa,wa+
        "    original361=load(S/'W-two-audit-361/W-exact-lattice-certificate.json')\\n"+
        "    need(original361==persisted,'entire_original361_W_certificate')\\n"+
        "    for c in original361['systems'].values(): reread(c)\\n")
    wmain=wmain.replace("['W-table-audit-357','W-two-359']", "['W-table-audit-357','W-two-359','W-two-audit-361']")
    with (D/'w_main.txt').open('x') as f:f.write(wmain)''')
# Append one input-only fixed verdict replay, fixed independent identities,
# entire new interface, then table production/replay and preservation.
src+='''
    report['phase']='fixed_W_eliminations_and_actual_actions'
    fixed_replay=run('W_verify.py','test-verification-report.json')
    need(fixed_replay['index']==64 and fixed_replay['action_rank']==42
        and fixed_replay['action_division_certificates']==2304,'complete_fixed_W_elimination_replay')
    fresh_actions=divisions('test-action-division-',wb,wt,WJ,action_prefix='test-')
    fixed361_inputs=sum([divisions('division-',sb,st,folder=fixed361),
        divisions('u-division-',ub,ut,folder=fixed361),divisions('v-division-',vb,vt,folder=fixed361),
        divisions('w-division-',wb,wt,folder=fixed361)])
    fixed361_actions=divisions('test-action-division-',wb,wt,WJ,folder=fixed361,action_prefix='test-')
    need(fixed361_inputs==9216 and fixed361_actions==fresh_actions==2304,'all_step361_and_fresh_actual_dividends')
    for n in core359:
        need(read(fixed361/n)==read(fixed359/n)==read(D/n),'whole_fixed359_361_fresh_'+n)
    report['phase']='fixed_independent_ranks_kernels_and_global_preimages'
    # Use binary-product definitions only: no rank search, elimination,
    # kernel discovery, inverse construction or new preimage production.
    defs=(fixed361/'independent.py').read_text().split('def preimage(',1)[0]
    ns={'__file__':str(D/'fixed_independent.py')}
    exec(compile(defs,str(D/'fixed_independent.py'),'exec'),ns)
    bm=ns['bm'];bits=ns['bits']
    def binary_shape(a,h,w):
        need(type(a) is list and len(a)==h and all(type(r) is list and len(r)==w for r in a),'full_binary_shape')
        for row in a:bits(row)
    def fixed_rank(label,A,r,kernel):
        c=read(fixed361/(label+'-full-rank.json'));height=len(A)
        shapes={'matrix':(height,48),'columns':(height,r),'factor':(r,48),'left_inverse':(r,height),
            'kernel':(48,48-r),'kernel_projection':(48-r,48),'kernel_rows':(48-r,48),'selected_inverse':(r,r)}
        for key,(h,w) in shapes.items():binary_shape(c[key],h,w)
        C,B,L,K,P=map(c.get,['columns','factor','left_inverse','kernel','kernel_projection'])
        RI=[[int(i==j) for j in range(r)] for i in range(r)]
        KI=[[int(i==j) for j in range(48-r)] for i in range(48-r)]
        need(c['matrix']==A and C==[row[:r] for row in A] and bm(C,B)==A and bm(L,C)==RI,
            'full_fixed_rank_factorization_'+label)
        need(B==I[:r] and c['rank']==r and bm(A,K)==[[0]*(48-r) for _ in A] and bm(P,K)==KI
            and K==tr(c['kernel_rows']) and c['kernel_rows']==I[r:]==kernel,'entire_fixed_kernel_'+label)
        rows=c['selected_rows'];inv=c['selected_inverse']
        need(len(rows)==r and len(set(rows))==r and all(type(x) is int and 0<=x<height for x in rows),
            'fixed_selected_rows_'+label)
        selected=[C[i] for i in rows]
        need(bm(selected,inv)==RI and bm(inv,selected)==RI,'both_fixed_selected_inverse_products_'+label)
    fc=read(D/'test-frobenius.json')
    first=tr([[x%2 for x in wt[i][i]] for i in range(48)]);terminal=first
    for k in range(6):
        if k:terminal=bm(first,terminal)
        need(terminal==fc['iterates'][k],'all_fixed_independent_frobenius_iterates')
    fixed_rank('frobenius',terminal,1,fc['elimination']['kernel'])
    actions=[read(D/('test-action-%02d.json'%i)) for i in range(48)]
    stack=[[actions[i][k][j]%2 for i in range(48)] for j in range(48) for k in range(48)]
    ak=read(D/'test-action-kernel.json')
    need(ak['matrix']==stack,'entire_actual_action_stack')
    fixed_rank('action',stack,42,ak['kernel'])
    def fixed_preimage(label,kernel):
        e=read(fixed361/(label+'-independent-preimage.json'));c=read(D/('test-'+label+'-lattice.json'))
        G=tr(kernel+[[2*x for x in row] for row in I]);L=e['basis'];LI=rat(e['inverse'])
        U=e['G_to_basis'];V=e['basis_to_G'];width=48+len(kernel)
        for a,h,w in [(G,48,width),(L,48,48),(U,width,48),(V,48,width)]:shape(a,h,w)
        need(e['kernel_rows']==kernel and e['generators']==c['S']==G and L==c['basis']
            and mm(G,U)==L and mm(L,V)==G and mm(L,LI)==I and mm(LI,L)==I,'whole_fixed_preimage_'+label)
        f=rat(e['saved_basis_in_displayed']);b=rat(e['displayed_basis_in_saved'])
        need(all(F(x).denominator==1 for a in (f,b) for row in a for x in row)
            and mm(L,f)==c['basis'] and mm(c['basis'],b)==L and mm(f,b)==I and mm(b,f)==I,
            'both_integral_fixed_preimage_comparisons_'+label)
        return e
    radical=fixed_preimage('radical',I[1:]);numerator=fixed_preimage('numerator',I[42:])
    need(radical['basis']==WJ,'entire_actual_W_radical_binding')
    for i,A in enumerate(actions):
        shape(A,48,48)
        need(mm(WJ,A)==mm(tr(wt[i]),WJ),'all_saved_full_radical_actions')
    # Distinct filenames protect the input V-to-W interface and its sources.
    for dest,path in [('decision-359.json',fixed359/'test-decision.json'),
        ('decision-361.json',fixed361/'test-decision.json'),
        ('Z-numerator-359.json',fixed359/'test-numerator-lattice.json'),
        ('Z-numerator-361.json',fixed361/'test-numerator-lattice.json'),
        ('Z-independent-multiplier.json',fixed361/'independent-multiplier.json'),
        ('Z-independent-preimage.json',fixed361/'numerator-independent-preimage.json')]:copy(dest,path)
    interface=(fixed361/'successor-interface-body.txt').read_text()
    interface=interface.replace('W-', 'Z-').replace('decision-351.json','decision-359.json').replace('decision-353.json','decision-361.json')
    interface=interface.replace('numerator-351.json','numerator-359.json').replace('numerator-353.json','numerator-361.json')
    interface=interface.replace('>=43','>=42').replace('I[43:]','I[42:]').replace('53','54').replace('==32','==64').replace('==5','==6')
    interface=interface.replace('[(I:I):V] = absolute determinant of V basis in (I:I)',
        '[(I:I):W] = absolute determinant of W basis in (I:I)').replace("vb['identity']","wb['identity']")
    with (D/'new-successor-interface-body.txt').open('x') as f:f.write(interface)
    exec(compile(interface,str(D/'new-successor-interface-body.txt'),'exec'),globals())
    dc=read(D/'decision-359.json');im=read(D/'Z-independent-multiplier.json')
    witness=dc['strict_witness'];strict=im['strict_action']
    shape(strict,48,48)
    need(im['strict_numerator']==I[42] and im['strict_denominator']==2 and witness['column']==42
        and witness['numerator']==I[42] and witness['radical_action']==strict
        and [[2*x for x in row] for row in strict]==actions[42],'full_actual_strict_action_interface')
    # All 377 step-361 fixed bindings agree; generated audit-only artifacts
    # remain read in place, with their original hashes and full equations.
    for n,e in mf361.items():
        if (D/n).is_file():need(digest(D/n)==e['sha256'],'fixed361_fresh_binding_'+n)
    save('new-successor-input-validation.json',{'status':'PASS','failures':[],
        'half_columns':[42,43,44,45,46,47],'index':64,'global_preimages':2,
        'full_fixed_rank_factorizations':2,'all_original_eliminations_replayed':True,
        'all_original_V_and_direct_W_solves_replayed':True,'all_before_production':True,
        'fixed_input_divisions':64512+fixed359_count+fixed361_inputs,
        'fixed_W_action_divisions':original_actions+fixed361_actions,'fresh_W_action_divisions':fresh_actions})
    report['phase']='successor_table_source_adaptation'
    p=(FIX/'produce.py').read_text()
    p=p.replace("old=read('v-basis.json'); d=read('decision-351.json')","old=read('w-basis.json'); d=read('decision-359.json')")
    p=p.replace('[1]*43+[2]*5','[1]*42+[2]*6').replace("'basis_in_v'","'basis_in_w'")
    p=p.replace("source=read('v-product-","source=read('w-product-").replace("save('w-","save('z-")
    p=p.replace("'scale':992","'scale':1984").replace("'input_scale':496","'input_scale':992")
    p=p.replace("'prior_scales':[31,62,124,248,496]","'prior_scales':[31,62,124,248,496,992]")
    p=p.replace("'index':32","'index':64").replace('992*power','1984*power').replace('scale_992','scale_1984')
    p=p.replace('index=32,scale=992','index=64,scale=1984')
    v=(FIX/'verify_w.py').read_text()
    v=v.replace("old=read('v-basis.json'); got=read('w-basis.json')","old=read('w-basis.json'); got=read('z-basis.json')")
    v=v.replace('decision-351.json','decision-359.json').replace('decision-353.json','decision-361.json')
    v=v.replace('W-independent-multiplier.json','Z-independent-multiplier.json').replace('>=43','>=42').replace('==32','==64')
    v=v.replace("d['kernel_dimension']==5","d['kernel_dimension']==6").replace("got['basis_in_v']","got['basis_in_w']")
    v=v.replace('[(I:I):V] = absolute determinant of V basis in (I:I)','[(I:I):W] = absolute determinant of W basis in (I:I)')
    v=change(v,"old['scale']==496 and old['original_scale']==31 and old['input_scale']==248\\n        and got['scale']==992 and got['input_scale']==496",
        "old['scale']==992 and old['original_scale']==31 and old['input_scale']==496\\n        and got['scale']==1984 and got['input_scale']==992")
    v=v.replace("got['prior_scales']==[31,62,124,248,496]","got['prior_scales']==[31,62,124,248,496,992]")
    v=v.replace('F(992*','F(1984*').replace('poly[a]-=992*z*x','poly[a]-=1984*z*x')
    v=v.replace("read('w-product-","read('z-product-").replace("save('w-division-","save('z-division-")
    v=v.replace('scale=992','scale=1984').replace('w-verification-report.json','z-verification-report.json')
    v=v.replace('exact_index_thirty_two_orientation','exact_index_sixty_four_orientation')
    # Derive the denominator from every actual rational power-map entry.
    # No scale value is accepted merely because it occurs in metadata.
    v=v.replace("V=[]\\n", "need(math.lcm(*(x.denominator for row in matrices['basis_to_power'] for x in row))==1984,'reconstructed_actual_scale')\\n    V=[]\\n")
    for n,t in [('produce_z.py',p),('verify_z.py',v)]:
        compile(t,str(D/n),'exec')
        with (D/n).open('x') as f:f.write(t)
    code={p.name:digest(p) for p in D.iterdir() if p.suffix in ('.py','.txt')}
    save('code-hashes.json',code);save('table-complete-copy-manifest.json',manifest)
    report['phase']='one_full_successor_table_production'
    prod=run('produce_z.py','producer-report.json')
    need(prod['products']==2304 and prod['product_slots']==110592 and prod['index']==64 and prod['scale']==1984,'entire_new_production')
    report['phase']='independent_successor_original_H_replay'
    zr=run('verify_z.py','z-verification-report.json')
    for k,x in counts.items():need(zr[k]==x,'full_successor_'+k)
    need(zr['index']==64 and zr['scale']==1984,'entire_successor_scale_and_index')
    zb=read(D/'z-basis.json');zt=[read(D/('z-product-%02d.json'%i)) for i in range(48)]
    zd=divisions('z-division-',zb,zt)
    save('table-persisted-input-checks.json',{'status':'PASS','failures':[],
        'fixed_input_divisions':64512+fixed359_count+fixed361_inputs,
        'fixed_W_action_divisions':original_actions+fixed361_actions,
        'fresh_input_divisions':fresh_s+fresh_u+fresh_v+fresh_w,'fresh_W_action_divisions':fresh_actions,
        'new_table_divisions':zd,'all_actual_dividends_checked':True,'all_original_systems_replayed':True})
    for bn,tn,b,t in [('basis.json','product-',sb,st),('u-basis.json','u-product-',ub,ut),
        ('v-basis.json','v-product-',vb,vt),('w-basis.json','w-product-',wb,wt),('z-basis.json','z-product-',zb,zt)]:
        need(read(D/bn)==b and all(read(D/(tn+'%02d.json'%i))==t[i] for i in range(48)),'entire_final_table_'+bn)
    for n,obj in [('producer-report.json',prod),('z-verification-report.json',zr),('test-verification-report.json',fixed_replay)]:
        need(read(D/n)==obj,'entire_final_report_'+n)
    report['phase']='final_preservation'
    audit_after={n:digest(ROOT/n) for n in audit_before}
    copies={n:digest(D/n) for n in manifest};code_after={n:digest(D/n) for n in code}
    need(audit_before==audit_after and code==code_after and all(code[n]==h for n,h in prepared.items())
        and copies=={n:e['sha256'] for n,e in manifest.items()},'entire_preservation')
    preservation={'equal':True,'before':audit_before,'after':audit_after,'code_before':code,'code_after':code_after,
        'fixed_before':{n:e['sha256'] for n,e in manifest.items()},'fixed_after':copies}
    save('preservation-table.json',preservation)
    for n,obj in [('audit-input-hashes.json',audit_before),('preservation-table.json',preservation),
        ('code-hashes.json',code),('table-complete-copy-manifest.json',manifest)]:need(read(D/n)==obj,'entire_final_inventory_'+n)
    for n in ['new-successor-input-validation.json','table-persisted-input-checks.json']:
        r=read(D/n);need(r['status']=='PASS' and not r['failures'],'full_final_evidence_'+n)
    report.update(status='PASS',phase='complete',products=2304,product_slots=110592,index=64,scale=1984,
        original_files=len(audit_before),fixed_copies=len(manifest),source_files=len(code),
        fixed_input_divisions=64512+fixed359_count+fixed361_inputs,fixed_W_action_divisions=original_actions+fixed361_actions,
        fresh_input_divisions=fresh_s+fresh_u+fresh_v+fresh_w,fresh_W_action_divisions=fresh_actions,
        successor_divisions=zd,all_actual_dividends_checked=True,all_original_V_and_W_systems_replayed=True)
except Exception as exc:
    report.update(status='STOP',failures=[type(exc).__name__+': '+str(exc)])
report.update(seconds=time.monotonic()-BEGAN,required_seconds=180,required_bytes=134217728)
save('stage-report.json',report);print(json.dumps(report));sys.exit(0 if report['status']=='PASS' else 1)
'''
# Make the exact fixed-rank checker definitions auditable as an executed source.
src=change(src,"    exec(compile(defs,str(D/'fixed_independent.py'),'exec'),ns)",
    "    with (D/'fixed_independent.py').open('x') as f:f.write(defs)\n    exec(compile(defs,str(D/'fixed_independent.py'),'exec'),ns)")
# Helper needed in the generated execution body after input helpers redefine replace.
src=src.replace('def read(p):return json.loads(p.read_text())','def change(t,a,b):\n    if t.count(a)!=1:raise ValueError("unique_adaptation_"+a[:80])\n    return t.replace(a,b)\ndef read(p):return json.loads(p.read_text())')
compile(src,str(D/'execution.py'),'exec')
with (D/'execution.py').open('x') as f:f.write(src)
exec(compile(src,str(D/'execution.py'),'exec'),globals())
