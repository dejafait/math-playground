"""Prepare inspected replay definitions under the watchdog; never run a producer."""
from pathlib import Path
import re
D=Path(__file__).resolve().parent;S=D.parent
src=(S/'W-two-359/execution.py').read_text()
def change(t,a,b):
    if t.count(a)!=1:raise ValueError('unique_preparation_boundary_'+a[:90])
    return t.replace(a,b)

inventory_extension="""
    fixed359=S/'W-two-359'
    previous359=read(fixed359/'audit-input-hashes.json')
    need(len(previous359)==7363,'entire_7363_step359_inventory')
    audit_names.update(previous359)
    audit_names.update(str(p.relative_to(ROOT)) for p in fixed359.rglob('*') if p.is_file())
    audit_names.update([
        'lemmas/L093-conductor389-index-thirty-two-order-not-2-maximal.md',
        'drafts/literature/2026-10-20-W-two-critical-audit.md',
        'drafts/2026-10-20-W-two-critical-audit-attempt.md',
        'history/359-2026-10-20-W-two-index64.md',
        'history/360-2026-10-20-W-two-audit-scope.md',
        'scripts/seven-torsion/V-two-audit-353/independent.py'])
"""
src=change(src,'    audit_before={n:digest(ROOT/n) for n in sorted(audit_names)}',
    inventory_extension+'    audit_before={n:digest(ROOT/n) for n in sorted(audit_names)}')
transition="""
    note359='drafts/2026-10-20-W-two-attempt.md'
    a359='99c1e1ceea80f471d2b1ca1a1c8dbd8d8ab86a70070e05241e9df91a04d96beb'
    b359='3f0b22531c79a9e28e3c128e1cf2cc399b30fa5404fc5b26c7f1a40790c5f765'
    hist359='history/359-2026-10-20-W-two-index64.md'
    h359='5741a0f3a78cdddfa05f9945f2e6ed3ef2a748bbb6e8d5badb8592fe8f5ecf92'
    raw359=(ROOT/note359).read_bytes(); marker359=b'\\n## Completed execution\\n'
    need(previous359[note359]==a359 and audit_before[note359]==b359
        and audit_before[hist359]==h359 and a359 in (ROOT/hist359).read_text()
        and b359 in (ROOT/hist359).read_text() and raw359.count(marker359)==1
        and hashlib.sha256(raw359.split(marker359)[0]).hexdigest()==a359,
        'exact_step359_append_bound_to_old_inventory_and_history')
    need(all(audit_before[n]==h for n,h in previous359.items() if n!=note359),
        'all_other_step359_originals')
    mf359=read(fixed359/'complete-copy-manifest.json')
    need(len(mf359)==322,'all_322_step359_copy_bindings')
    for n,e in mf359.items():
        need(audit_before[e['source']]==e['sha256']
            ==audit_before[str((fixed359/n).relative_to(ROOT))],'entire_fixed359_copy_'+n)
    cd359=read(fixed359/'code-hashes.json');need(len(cd359)==17,'all_17_step359_sources')
    need(all(digest(fixed359/n)==h for n,h in cd359.items()),'all_fixed359_source_hashes')
    save('post359-transition.json',{'path':note359,'prior':a359,'current':b359,
        'history':hist359,'history_sha256':h359,'all_other_inputs_unchanged':True,
        'no_pathname_exemptions':True})
"""
src=change(src,'    post357={',transition+'    post357={')
# Keep fresh and original W solves, and all fixed V solve copies.
anchor="    with (D/'w_main.txt').open('x') as f:f.write(wmain)"
wsolve_extra="""
    wanchor="    for c in original357['systems'].values(): reread(c)\\n"
    need(wmain.count(wanchor)==1,'unique_step359_W_solve_insertion')
    wmain=wmain.replace(wanchor,wanchor+
        "    original359=load(S/'W-two-359/W-exact-lattice-certificate.json')\\n"+
        "    need(original359==persisted,'entire_original359_W_certificate')\\n"+
        "    for c in original359['systems'].values(): reread(c)\\n")
    vanchor="    for c in prod['systems'].values(): reread(c)\\n"
    need(wmain.count(vanchor)==1,'unique_all_V_solve_copies_insertion')
    wmain=wmain.replace(vanchor,vanchor+
        "    for folder in ['W-table-audit-357','W-two-359']:\\n"+
        "        vc=load(S/folder/'exact-lattice-certificate.json')\\n"+
        "        need(vc==fresh,'entire_original_V_copy_'+folder)\\n"+
        "        for c in vc['systems'].values(): reread(c)\\n")
"""
src=change(src,anchor,wsolve_extra+anchor)
start="    report['phase']='new_W_modular_source_specialization'\n"
end="    report['phase']='final_preservation'\n"
if src.count(start)!=1 or src.count(end)!=1:raise ValueError('unique_no_producer_boundaries')
replay="""
    report['phase']='complete_step359_input_dividends'
    fixed359_count=sum([divisions('division-',sb,st,folder=fixed359),
        divisions('u-division-',ub,ut,folder=fixed359),
        divisions('v-division-',vb,vt,folder=fixed359),
        divisions('w-division-',wb,wt,folder=fixed359)])
    need(fixed359_count==9216,'all_9216_step359_input_divisions')
    # Exact bindings of the entire 322 fixed files to this fresh replay.
    for n,e in mf359.items():
        need((D/n).is_file() and digest(D/n)==e['sha256'],'original_fixed_fresh_'+n)
    core359=['test-input-basis.json','test-frobenius.json','test-radical-lattice.json',
        'test-action-kernel.json','test-numerator-lattice.json','test-decision.json']
    core359+=['test-action-%02d.json'%i for i in range(48)]
    for n in core359+['W_verify.py']:copy(n,fixed359/n)
    WJ=read(D/'test-radical-lattice.json')['basis']
    original_actions=divisions('test-action-division-',wb,wt,WJ,
        folder=fixed359,action_prefix='test-')
    need(original_actions==2304,'every_original_W_actual_action_dividend')
    # Adapt only the already assessed independent full rank/preimage instance.
    ind=(S/'V-two-audit-353/independent.py').read_text()
    ind=ind.replace("OLD = D.parent/'index-sixteen-order-two-351'",
        "OLD = D.parent/'W-two-359'")
    ind=ind.replace('v-product-','w-product-')
    ind=re.sub(r'\\b43\\b','42',ind)
    ind=re.sub(r'\\b32\\b','64',ind)
    ind=re.sub(r'\\b496\\b','992',ind)
    ind=ind.replace('[2]*42+[1]*5','[2]*42+[1]*6')
    ind=ind.replace('action_kernel_dimension=5','action_kernel_dimension=6')
    ind=ind.replace('action_left_inverse_entries=99072','action_left_inverse_entries=96768')
    ind=ind.replace('selected_inverse_entries=1849','selected_inverse_entries=1764')
    ind=ind.replace('[(I:I):V] = absolute determinant of V basis in (I:I)',
        '[(I:I):W] = absolute determinant of W basis in (I:I)')
    oldread="def read(path):\\n    return json.loads(path.read_text())"
    newread=("def read(path):\\n    if path.parent==D and (path.name in "+repr(
        ['frobenius.json','radical-lattice.json','numerator-lattice.json',
        'action-kernel.json','decision.json','input-basis.json'])+
        " or __import__('re').fullmatch(r'action-[0-9]{2}\\\\.json',path.name)):\\n"+
        "        path=path.with_name('test-'+path.name)\\n"+
        "    return json.loads(path.read_text())")
    need(ind.count(oldread)==1,'unique_independent_storage_redirection')
    ind=ind.replace(oldread,newread)
    compile(ind,str(D/'independent.py'),'exec')
    with (D/'independent.py').open('x') as f:f.write(ind)
    code={p.name:digest(p) for p in D.iterdir() if p.suffix in ('.py','.txt')}
    save('code-hashes.json',code);save('audit-complete-copy-manifest.json',manifest)
    report['phase']='full_fixed_W_modular_replay'
    verifier=run('W_verify.py','test-verification-report.json')
    for k,x in {'input_product_slots':110592,'action_slots':110592,
        'frobenius_slots':13824,'frobenius_iterates':6,'exponent':64,'prime':2,
        'action_division_certificates':2304,'frobenius_rank':1,
        'action_rank':42,'index':64,'action_kernel_dimension':6}.items():
        need(verifier[k]==x,'complete_W_replay_'+k)
    for name in ['test-producer-report.json','test-verification-report.json']:
        prior_report=read(fixed359/name)
        need(prior_report['status']=='PASS' and not prior_report['failures'],'fixed_report_'+name)
        for key in ['decision','index','frobenius_rank','radical_dimension',
            'action_rank','action_kernel_dimension']:
            need(prior_report[key]==verifier[key],'whole_fixed_fresh_result_'+key)
    action_count=divisions('test-action-division-',wb,wt,WJ,action_prefix='test-')
    need(action_count==2304,'all_fresh_W_actual_action_dividends')
    report['phase']='independent_complete_W_rank_kernel_and_global_preimages'
    supplement=run('independent.py','independent-report.json')
    for k,x in {'frobenius_rank':1,'action_rank':42,'index':64,
        'radical_kernel_dimension':47,'action_kernel_dimension':6,
        'independent_preimages':2,'action_entries':110592,
        'action_factorization_entries':110592,'action_left_inverse_entries':96768,
        'full_strict_action_entries':2304,'all_load_bearing_certificates_reread':True}.items():
        need(supplement[k]==x,'entire_independent_supplement_'+k)
    for n in core359:
        need(read(D/n)==read(fixed359/n),'final_entire_fixed_W_certificate_'+n)
    for n,obj in [('independent-report.json',supplement),
        ('test-verification-report.json',verifier)]:
        need(read(D/n)==obj,'final_audit_report_reread_'+n)
    need(read(D/'audit-complete-copy-manifest.json')==manifest,'final_complete_copy_manifest')
    report.update(W_decision=verifier['decision'],W_multiplier_index=verifier['index'],
        W_frobenius_rank=verifier['frobenius_rank'],W_action_rank=verifier['action_rank'],
        W_action_kernel_dimension=verifier['action_kernel_dimension'],
        fixed357_divisions=fixed357_count,fixed359_input_divisions=fixed359_count,
        fixed359_action_divisions=original_actions,fresh_W_action_divisions=action_count,
        full_independent_supplement=supplement,all_original_V_and_W_systems_replayed=True)
"""
src=src.split(start)[0]+replay+end+src.split(end)[1]
# The original input-only manifest remains immutable; final manifest includes W.
src=change(src,"('complete-copy-manifest.json',manifest)]:need(read(D/n)==obj",
    "('audit-complete-copy-manifest.json',manifest)]:need(read(D/n)==obj")
# re is needed only for the constrained instance-source adaptations above.
src=src.replace('import hashlib,json,sys,textwrap,time','import hashlib,json,sys,textwrap,time,re')
compile(src,str(D/'audit.py'),'exec')
with (D/'audit.py').open('x') as f:f.write(src)
exec(compile(src,str(D/'audit.py'),'exec'),globals())
