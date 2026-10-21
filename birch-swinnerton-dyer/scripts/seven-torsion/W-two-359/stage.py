"""Adapt inspected fixed replay and known modular interfaces inside the watchdog."""
from pathlib import Path
import json,sys,textwrap
D=Path(__file__).resolve().parent; S=D.parent
src=(S/'W-table-audit-357/audit.py').read_text()
def change(t,a,b):
    if t.count(a)!=1:raise ValueError('unique_preparation_boundary_'+a[:90])
    return t.replace(a,b)
# Every executed mathematical source is adapted after the external start.
inventory_extension='''
    fixed357=S/'W-table-audit-357'
    previous357=read(fixed357/'audit-input-hashes.json')
    need(len(previous357)==6801,'entire_6801_step357_inventory')
    audit_names.update(previous357)
    audit_names.update(str(p.relative_to(ROOT)) for p in fixed357.rglob('*') if p.is_file())
    audit_names.update(['drafts/literature/2026-10-20-index-thirty-two-order-prime-two-test.md',
        'drafts/2026-10-20-W-two-attempt.md','history/357-2026-10-20-index-thirty-two-table-critical-audit.md',
        'history/358-2026-10-20-W-two-source-scope.md'])
'''
src=change(src,'    audit_before={n:digest(ROOT/n) for n in sorted(audit_names)}',inventory_extension+'    audit_before={n:digest(ROOT/n) for n in sorted(audit_names)}')
transition='''
    post357={
        'lemmas/L092-conductor389-index-thirty-two-multiplier-order-table.md':
        ('4be8ae3f18f2545688ca8ecc0839521c68e6810f8c6bb79f3455a2b7a79c1f85','193730fc345fc756aa50cd308ec557157fcae213500ddb93c5809920123be73a'),
        'drafts/2026-10-20-index-thirty-two-table-critical-audit-attempt.md':
        ('a4b2cfd0c575ee5b97ad9516e28c4ed220cdd7579598050ff275121e923fa0cc','d0acc4a9b1b3e5cdaed5ab8678d816d965535e162392d5ac306cc847bbf2b433')}
    for n,(a,b) in post357.items():need(previous357[n]==a and audit_before[n]==b,'exact_post357_'+n)
    need(all(audit_before[n]==h for n,h in previous357.items() if n not in post357),'all_other_step357_originals')
    note357='drafts/2026-10-20-index-thirty-two-table-critical-audit-attempt.md'
    raw357=(ROOT/note357).read_bytes();mark357=b'\\n## Completed execution\\n'
    need(raw357.count(mark357)==1 and hashlib.sha256(raw357.split(mark357)[0]).hexdigest()==post357[note357][0], 'exact_step357_note_append')
    mf357=read(fixed357/'complete-copy-manifest.json');need(len(mf357)==322,'all_322_step357_copies')
    for n,e in mf357.items():need(audit_before[e['source']]==e['sha256']==audit_before[str((fixed357/n).relative_to(ROOT))],'whole_step357_copy_binding_'+n)
    cd357=read(fixed357/'code-hashes.json');need(len(cd357)==14,'all_14_step357_sources')
    need(all(digest(fixed357/n)==h for n,h in cd357.items()),'all_step357_executed_source_hashes')
    save('post357-transition.json',{'exact_changes':post357,'all_other_inputs_unchanged':True,'no_pathname_exemptions':True})
    # Fresh direct W reconstruction also replays every original step-357 system.
    wmain=(fixed357/'w_main.txt').read_text()
    anchor="    for c in persisted['systems'].values(): reread(c)\\n"
    need(wmain.count(anchor)==1,'unique_W_original_solve_insertion')
    wmain=wmain.replace(anchor,anchor+"    original357=load(S/'W-table-audit-357/W-exact-lattice-certificate.json')\\n    need(original357==persisted,'entire_original357_W_certificate')\\n    for c in original357['systems'].values(): reread(c)\\n")
    with (D/'w_main.txt').open('x') as f:f.write(wmain)
'''
src=change(src,"    note='drafts/2026-10-20-index-thirty-two-table-attempt.md'",transition+"    note='drafts/2026-10-20-index-thirty-two-table-attempt.md'")
src=change(src,"save('code-hashes.json',code);save('complete-copy-manifest.json',manifest)","save('input-audit-code-hashes.json',code);save('complete-copy-manifest.json',manifest)")
modular='''
    report['phase']='all_fixed357_actual_divisions'
    fixed357_count=sum([divisions('division-',sb,st,folder=fixed357),
        divisions('u-division-',ub,ut,folder=fixed357),divisions('v-division-',vb,vt,folder=fixed357),
        divisions('w-division-',wb,wt,folder=fixed357)])
    need(fixed357_count==9216,'all_9216_fixed357_actual_dividends')
    report['phase']='new_W_modular_source_specialization'
    p=(S/'index-sixteen-order-two-351/produce.py').read_text()
    p=p.replace('496','992').replace('246016','984064')
    p=p.replace("nb['input_scale']==248","nb['input_scale']==496")
    p=p.replace("nb['prior_scales']==[31,62,124,248]","nb['prior_scales']==[31,62,124,248,496]")
    p=p.replace("nb['index']==16","nb['index']==32")
    p=p.replace('v-basis.json','w-basis.json').replace('v-product-','w-product-')
    v=(S/'index-sixteen-order-two-351/verify.py').read_text()
    v=v.replace('496','992').replace("validation['index']==16","validation['index']==32")
    v=v.replace('v-basis.json','w-basis.json').replace('v-product-','w-product-').replace('v-verification-report.json','w-verification-report.json')
    for name in ['input-basis.json','frobenius.json','radical-lattice','numerator-lattice','action-',
        'action-kernel.json','decision.json','preservation-producer.json','preservation-verifier.json',
        'input-hashes.json','producer-report.json','verification-report.json']:
        p=p.replace("'"+name,"'test-"+name);v=v.replace("'"+name,"'test-"+name)
    for name,t in [('W_produce.py',p),('W_verify.py',v)]:
        compile(t,str(D/name),'exec')
        with (D/name).open('x') as f:f.write(t)
    code={p.name:digest(p) for p in D.iterdir() if p.suffix in ('.py','.txt')}
    save('code-hashes.json',code)
    report['phase']='one_actual_W_radical_action_multiplier_test'
    producer=run('W_produce.py','test-producer-report.json')
    verifier=run('W_verify.py','test-verification-report.json')
    for r,label in [(producer,'producer'),(verifier,'independent')]:
        for k,x in {'input_product_slots':110592,'action_slots':110592,'frobenius_slots':13824,
            'frobenius_iterates':6,'exponent':64,'prime':2}.items():need(r[k]==x,label+'_complete_'+k)
    for k in ['decision','index','frobenius_rank','radical_dimension','action_rank','action_kernel_dimension']:
        need(producer[k]==verifier[k],'independent_actual_W_result_'+k)
    need(verifier['action_division_certificates']==2304,'all_W_action_divisions_persisted')
    WJ=read(D/'test-radical-lattice.json')['basis']
    action_count=divisions('test-action-division-',wb,wt,WJ,action_prefix='test-')
    need(action_count==2304,'all_W_action_actual_dividends_reread')
    for n,o in [('test-producer-report.json',producer),('test-verification-report.json',verifier),
        ('test-decision.json',read(D/'test-decision.json'))]:need(read(D/n)==o,'final_new_result_reread_'+n)
    report.update(W_decision=verifier['decision'],W_multiplier_index=verifier['index'],
        W_frobenius_rank=verifier['frobenius_rank'],W_radical_dimension=verifier['radical_dimension'],
        W_action_rank=verifier['action_rank'],W_action_kernel_dimension=verifier['action_kernel_dimension'],
        new_W_action_divisions=action_count,fixed357_divisions=fixed357_count)
'''
src=change(src,"    report['phase']='final_preservation'",modular+"    report['phase']='final_preservation'")
with (D/'execution.py').open('x') as f:f.write(src)
exec(compile(src,str(D/'execution.py'),'exec'),globals())
