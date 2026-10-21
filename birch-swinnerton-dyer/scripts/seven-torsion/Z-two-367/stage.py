"""Prepare the full fixed replay and one actual-Z test after watchdog start."""
from pathlib import Path
D=Path(__file__).resolve().parent; S=D.parent
def change(t,a,b):
    if t.count(a)!=1:raise ValueError('unique_adaptation_'+a[:100])
    return t.replace(a,b)

# Historical sources are read; no historical wrapper, stage or producer executes.
src=(S/'Z-table-audit-365/execution.py').read_text()
src=change(src,'    audit_before={n:digest(ROOT/n) for n in sorted(audit_names)}',r'''
    fixed365=S/'Z-table-audit-365'
    previous365=read(fixed365/'audit-input-hashes.json')
    need(len(previous365)==9509,'all_9509_step365_originals')
    audit_names.update(previous365)
    audit_names.update(str(p.relative_to(ROOT)) for p in fixed365.rglob('*') if p.is_file())
    audit_names.update(['drafts/literature/2026-10-20-Z-order-prime-two-test.md',
        'drafts/2026-10-20-Z-two-attempt.md',
        'history/365-2026-10-20-index64-table-critical-audit.md',
        'history/366-2026-10-20-Z-two-source-comparison.md'])
    audit_before={n:digest(ROOT/n) for n in sorted(audit_names)}''')

src=change(src,"    note363='drafts/2026-10-20-index-sixty-four-table-attempt.md'",r'''
    post365={
      'lemmas/L094-conductor389-index-sixty-four-multiplier-order-table.md':
      ('c655930bd14ab8e78b1fcab16569bb70745b39f6b908095d93dac2bfcce8f838','3cfb4cc851f4a5ec77c7948b887222518391d2e1505f6545595abdbcc9541842'),
      'drafts/2026-10-20-index-sixty-four-table-critical-audit-attempt.md':
      ('7ca93ee5fbbf3bb76c2180655ec1d20a5c290def76ca11d34da65d01d4704996','a6ef756f42300da834077eee3e8a2b3a67b00e3b995c34750b25ac4b453da87b')}
    hist365='history/365-2026-10-20-index64-table-critical-audit.md'
    history365=(ROOT/hist365).read_text()
    for n,(a,b) in post365.items():
        need(previous365[n]==a and audit_before[n]==b and a in history365 and b in history365,
            'exact_post365_bound_to_old_inventory_and_history_'+n)
    note365='drafts/2026-10-20-index-sixty-four-table-critical-audit-attempt.md'
    raw365=(ROOT/note365).read_bytes();marker365=b'\n## Completed execution\n'
    need(raw365.count(marker365)==1 and hashlib.sha256(raw365.split(marker365)[0]).hexdigest()==post365[note365][0],
        'exact_post365_unique_completion_append')
    need(all(audit_before[n]==h for n,h in previous365.items() if n not in post365),'every_other_step365_original')
    mf365=read(fixed365/'audit-complete-copy-manifest.json')
    need(len(mf365)==433,'all_433_step365_copy_bindings')
    for n,e in mf365.items():
        need(audit_before[e['source']]==e['sha256']==audit_before[str((fixed365/n).relative_to(ROOT))],
            'whole_step365_copy_binding_'+n)
    cd365=read(fixed365/'code-hashes.json');need(len(cd365)==20,'all_twenty_step365_sources')
    need(all(digest(fixed365/n)==h for n,h in cd365.items()),'all_step365_executed_source_hashes')
    save('post365-transition.json',{'exact_changes':post365,'history':hist365,
        'history_sha256':audit_before[hist365],'all_other_originals_unchanged':True,'no_pathname_exemptions':True})
    note363='drafts/2026-10-20-index-sixty-four-table-attempt.md' ''')

# Fresh W/V solves additionally compare and replay their entire step-365 copies.
src=change(src,"    with (D/'w_main.txt').open('x') as f:f.write(wmain)",r'''
    wa365="    for c in original363['systems'].values(): reread(c)\n"
    need(wmain.count(wa365)==1,'unique_W365_solve_insertion')
    wmain=wmain.replace(wa365,wa365+
        "    original365=load(S/'Z-table-audit-365/W-exact-lattice-certificate.json')\n"+
        "    need(original365==persisted,'entire_original365_W_certificate')\n"+
        "    for c in original365['systems'].values(): reread(c)\n")
    wmain=wmain.replace("['W-table-audit-357','W-two-359','W-two-audit-361','index-sixty-four-table-363']",
        "['W-table-audit-357','W-two-359','W-two-audit-361','index-sixty-four-table-363','Z-table-audit-365']")
    with (D/'w_main.txt').open('x') as f:f.write(wmain)''')

# This independent canonical reconstruction checks all six original Z systems too.
zsource=(S/'Z-table-audit-365/Z_reconstruct.py').read_text()
zsource=change(zsource,"    for c in persisted['systems'].values():reread(c)",
    "    for c in persisted['systems'].values():reread(c)\n"+
    "    original365=load(S/'Z-table-audit-365/Z-exact-lattice-certificate.json')\n"+
    "    need(original365==persisted,'entire_original365_Z_certificate')\n"+
    "    for c in original365['systems'].values():reread(c)")
compile(zsource,str(D/'Z_reconstruct.py'),'exec')
with (D/'Z_reconstruct.py').open('x') as f:f.write(zsource)

modular=r'''
    report['phase']='all_fixed365_copies_actual_dividends_and_direct_systems'
    for n,e in mf365.items():
        need((D/n).is_file() and digest(D/n)==e['sha256'],'every_step365_fresh_copy_binding_'+n)
    fixed365_inputs=sum([divisions('division-',sb,st,folder=fixed365),
        divisions('u-division-',ub,ut,folder=fixed365),divisions('v-division-',vb,vt,folder=fixed365),
        divisions('w-division-',wb,wt,folder=fixed365)])
    fixed365_actions=divisions('test-action-division-',wb,wt,WJ,folder=fixed365,action_prefix='test-')
    fixed365_z=divisions('z-division-',zb,zt,folder=fixed365)
    need(fixed365_inputs==9216 and fixed365_actions==fixed365_z==2304,'all_fixed365_actual_dividends')
    for n in core359:
        need(read(fixed365/n)==read(D/n),'entire_step365_fixed_W_evidence_'+n)
    old_zr=read(fixed365/'z-verification-report.json')
    need(set(old_zr)==set(zr) and type(old_zr['seconds']) in (int,float) and type(zr['seconds']) in (int,float)
        and {k:x for k,x in old_zr.items() if k!='seconds'}=={k:x for k,x in zr.items() if k!='seconds'}
        and read(fixed365/'Z-solve-report.json')==zi,'entire_fixed365_Z_report_arithmetic_fields')
    save('ztest-input-validation.json',{'status':'PASS','failures':[],
        'fixed_S_U_V_W_divisions':92160+fixed365_inputs,
        'fixed_W_action_divisions':6912+fixed365_actions,'fixed_Z_divisions':fixed_z+fixed365_z,
        'fresh_S_U_V_W_divisions':fresh_s+fresh_u+fresh_v+fresh_w,
        'fresh_W_action_divisions':fresh_actions,'fresh_Z_divisions':fresh_z,
        'actual_input_scale':1984,'input_table_index':64,'direct_Z_systems':6,
        'all_original_V_W_Z_systems_replayed':True,'all_before_new_Z_production':True})
    report['phase']='new_Z_source_specialization'
    p=(fixed359/'W_produce.py').read_text()
    p=change(p,"nb['input_scale']==496","nb['input_scale']==992")
    p=change(p,"nb['prior_scales']==[31,62,124,248,496]","nb['prior_scales']==[31,62,124,248,496,992]")
    p=change(p,"nb['index']==32","nb['index']==64")
    p=change(p,'984064','3936256')
    # Replace only the actual scale expressions, not old-input or prior-scale metadata.
    for a,b in [('Q=[[992*x','Q=[[1984*x'),("nb['scale']==992","nb['scale']==1984"),
        ("'scale':992","'scale':1984")]:p=change(p,a,b)
    p=p.replace('w-basis.json','z-basis.json').replace('w-product-','z-product-')
    p=p.replace('scale 992','scale 1984').replace('actual_scale_992_V','actual_scale_1984_Z')
    p=p.replace('L090 V producer','L094 Z producer').replace('integral_V_', 'integral_Z_')
    p=p.replace('scaled_V_', 'scaled_Z_').replace('V_basis_', 'Z_basis_').replace('V_two_', 'Z_two_')
    p=p.replace('test-','ztest-')
    v=(fixed359/'W_verify.py').read_text()
    for a,b in [("validation['index']==32","validation['index']==64"),
        ("validation['scale']==992","validation['scale']==1984"),("ib['scale']==992","ib['scale']==1984"),
        ('[992*x for x in expansion[j]]','[1984*x for x in expansion[j]]')]:v=change(v,a,b)
    v=v.replace('w-basis.json','z-basis.json').replace('w-product-','z-product-')
    v=v.replace('w-verification-report.json','z-verification-report.json').replace('test-','ztest-')
    v=v.replace('992 times','1984 times')
    # Prevent accidental stale scale arithmetic in this changed-instance implementation.
    need('984064' not in p and '992*x' not in p and '992*x' not in v,'no_stale_W_product_or_action_scale')
    for name,t in [('Z_produce.py',p),('Z_verify.py',v)]:
        compile(t,str(D/name),'exec')
        with (D/name).open('x') as f:f.write(t)
    report['phase']='one_actual_Z_radical_action_multiplier_test'
    producer=run('Z_produce.py','ztest-producer-report.json')
    verifier=run('Z_verify.py','ztest-verification-report.json')
    for r,label in [(producer,'producer'),(verifier,'independent')]:
        for k,x in {'input_product_slots':110592,'action_slots':110592,'frobenius_slots':13824,
            'frobenius_iterates':6,'exponent':64,'prime':2}.items():need(r[k]==x,label+'_complete_'+k)
    for k in ['decision','index','frobenius_rank','radical_dimension','action_rank','action_kernel_dimension']:
        need(producer[k]==verifier[k],'independent_actual_Z_result_'+k)
    need(verifier['action_division_certificates']==2304,'all_Z_action_divisions_persisted')
    ZJ=read(D/'ztest-radical-lattice.json')['basis']
    z_action_count=divisions('ztest-action-division-',zb,zt,ZJ,action_prefix='ztest-')
    need(z_action_count==2304,'all_Z_action_actual_dividends_reread')
    for n,o in [('ztest-producer-report.json',producer),('ztest-verification-report.json',verifier),
        ('ztest-decision.json',read(D/'ztest-decision.json'))]:need(read(D/n)==o,'final_new_Z_result_reread_'+n)
    report.update(Z_decision=verifier['decision'],Z_multiplier_index=verifier['index'],
        Z_frobenius_rank=verifier['frobenius_rank'],Z_radical_dimension=verifier['radical_dimension'],
        Z_action_rank=verifier['action_rank'],Z_action_kernel_dimension=verifier['action_kernel_dimension'],
        new_Z_action_divisions=z_action_count,fixed365_input_divisions=fixed365_inputs,
        fixed365_W_action_divisions=fixed365_actions,fixed365_Z_divisions=fixed365_z)
'''
src=change(src,"    code={p.name:digest(p) for p in D.iterdir() if p.suffix in ('.py','.txt')}\n    save('code-hashes.json',code);save('audit-complete-copy-manifest.json',manifest)",
    modular+"    code={p.name:digest(p) for p in D.iterdir() if p.suffix in ('.py','.txt')}\n    save('code-hashes.json',code);save('audit-complete-copy-manifest.json',manifest)")
compile(src,str(D/'execution.py'),'exec')
with (D/'execution.py').open('x') as f:f.write(src)
exec(compile(src,str(D/'execution.py'),'exec'),globals())
