"""One table-only specialization; historical stages never execute."""
from pathlib import Path
import json,sys,textwrap,time,hashlib
sys.set_int_max_str_digits(0)
D=Path(__file__).resolve().parent; S=D.parent; ROOT=D.parents[2]; START=time.monotonic()
def need(x,s):
    if not x: raise ArithmeticError(s)
def replace(t,a,b):
    need(t.count(a)==1,'unique_source_adaptation_'+a[:75]); return t.replace(a,b)
def save(n,x):
    with (D/n).open('x') as f: json.dump(x,f,separators=(',',':')); f.write('\n')
report={'status':'STOP','phase':'source_preparation','failures':[]}
try:
    # Preserve every inherited comparison. Only remove the audit's new
    # rank-proof generation/execution, outside this table-only target.
    audit=(S/'V-two-audit-353/audit.py').read_text()
    body=audit.split("report={'status':'STOP','phase':'initial_inventory','failures':[]}\ntry:\n",1)[1]
    body=body.split("    report['phase']='complete_fixed_V_verdict_replay'",1)[0]
    body=replace(body,'    names=set(previous351)',
        "    previous353=read(S/'V-two-audit-353/canonical-input-hashes.json')\n"
        "    need(len(previous353)==5745,'entire_step353_inventory')\n"
        "    names=set(previous353)")
    body=replace(body,'    for folder in [OLD,prior,table_source]:',
        "    for folder in [OLD,prior,table_source,S/'V-two-audit-353']:")
    body=replace(body,'    before={n:digest(ROOT/n) for n in sorted(names)}',
        "    names.update(['drafts/literature/2026-10-20-index-thirty-two-multiplier-table.md',\n"
        "        'drafts/2026-10-20-index-thirty-two-table-attempt.md',\n"
        "        'history/353-2026-10-20-V-two-critical-audit.md'])\n"
        "    before={n:digest(ROOT/n) for n in sorted(names)}\n"
        "    post353={\n"
        "      'lemmas/L091-conductor389-index-sixteen-order-not-2-maximal.md':\n"
        "      ('6e76b71ee5fe4deb2b516d64ba62b9aa6e7d6b6e79432539ff34ef08452f2e9b','c9463a1dfe5df314bd7d8f222ef2dddeec51b0fb67d70363ea36d898cf97213d'),\n"
        "      'drafts/2026-10-20-V-two-critical-audit-attempt.md':\n"
        "      ('f7865e4ab26f04a2a7cc662e35cdadd1010bdd645aa792c1fbfc5afa10656b23','fecd54289924ea68c30d2c2456f11e8cb0b0dbf6b1c044b4c725fa268fd5c36f')}\n"
        "    for n,(a,b) in post353.items():\n"
        "        need(previous353[n]==a and before[n]==b,'exact_post353_document_transition_'+n)\n"
        "    need(all(before[n]==h for n,h in previous353.items() if n not in post353),\n"
        "         'every_other_step353_input_unchanged')")
    body=replace(body,"    save('inventory-transition.json',transition)",
        "    need(transition==read(S/'V-two-audit-353/inventory-transition.json'),'whole_step353_transition')\n"
        "    transition={'retained_step353_transition':transition,\n"
        "        'exact_post353':{n:{'prior':a,'current':b} for n,(a,b) in post353.items()},\n"
        "        'no_pathname_exemptions':True}\n"
        "    save('inventory-transition.json',transition)")
    body=replace(body,"(prior,643),(OLD,643)]:","(prior,643),(OLD,643),(S/'V-two-audit-353',266)]:")
    body=replace(body,"[(table_source,6),(prior,7),(OLD,8)]:",
        "[(table_source,6),(prior,7),(OLD,8),(S/'V-two-audit-353',9)]:")
    begin=body.index('    # Ready independent factorization, kernel and integral-preimage mechanism.')
    end=body.index('    code={p.name:digest(p)',begin)
    body=body[:begin]+"    with (D/'solve_replay.py').open('x') as f: f.write(solve)\n"+body[end:]
    # The saved 353 solve replay adds a complete comparison against 351.
    begin=body.index("    solve=(OLD/'independent.py').read_text()")
    end=body.index("    with (D/'solve_replay.py').open('x')",begin)
    body=body[:begin]+(
        "    solve=(S/'V-two-audit-353/solve_replay.py').read_text()\n"
        "    anchor=\"    for c in original351['systems'].values(): reread(c)\\n\"\n"
        "    solve=replace(solve,anchor,anchor+\n"
        "        \"    original353=load(S/'V-two-audit-353/exact-lattice-certificate.json')\\n\"+\n"
        "        \"    need(original353==reread_cert,'entire_original353_exact_certificate_agrees')\\n\"+\n"
        "        \"    for c in original353['systems'].values(): reread(c)\\n\")\n"
        "    compile(solve,str(D/'solve_replay.py'),'exec')\n")+body[end:]
    # The inherited input block saves a code inventory too early for the
    # later table sources; use a distinct inventory and bind both at end.
    body=replace(body,"save('code-hashes.json',code)","save('input-code-hashes.json',code)")
    header=audit.split("report={'status':'STOP','phase':'initial_inventory','failures':[]}",1)[0]
    with (D/'input-replay-body.txt').open('x') as f: f.write(header+'\n'+textwrap.dedent(body))
    exec(compile(header+'\n'+textwrap.dedent(body),str(D/'input-replay-body.txt'),'exec'),globals())
    report['phase']='fixed_step353_divisions_and_multiplier_interfaces'
    audit353=S/'V-two-audit-353'
    fixed353=sum([divisions('division-',sb,st,folder=audit353),
        divisions('u-division-',ub,ut,folder=audit353),divisions('v-division-',vb,vt,folder=audit353),
        divisions('action-division-',vb,vt,J,folder=audit353,action_prefix='')])
    need(fixed353==9216,'all_step353_persisted_actual_dividends')
    # Copy the complete fixed successor interface, without overwriting the
    # separate earlier V/U and old-U data.
    for dest,src in [('decision-351.json',OLD/'decision.json'),
        ('decision-353.json',audit353/'decision.json'),
        ('W-numerator-351.json',OLD/'numerator-lattice.json'),
        ('W-numerator-353.json',audit353/'numerator-lattice.json'),
        ('W-independent-multiplier.json',audit353/'independent-multiplier.json'),
        ('W-independent-preimage.json',audit353/'numerator-independent-preimage.json')]: copy(dest,src)
    # Reuse all entries of the inspected full global-preimage comparison;
    # specialize only its instance, exact index and five terminal columns.
    whole=(table_source/'stage.py').read_text()
    lattice=between(whole,"    report['phase']='full_audited_V_lattice_interfaces'\n",
        "    report['phase']='one_V_table_production'")
    lattice=lattice.split('    evidence=',1)[0]
    lattice=lattice.replace('V-', 'W-').replace('audited_V','audited_W').replace('V_multiplier','W_multiplier')
    lattice=lattice.replace('decision-343.json','decision-351.json').replace('decision-345.json','decision-353.json')
    lattice=lattice.replace('numerator-343.json','numerator-351.json').replace('numerator-345.json','numerator-353.json')
    lattice=lattice.replace('>=44','>=43').replace('I[44:]','I[43:]').replace('52','53')
    lattice=lattice.replace('==16','==32').replace('==4\n','==5\n')
    lattice=lattice.replace('[V:U] = absolute determinant of U basis in V',
        '[(I:I):V] = absolute determinant of V basis in (I:I)')
    lattice=lattice.replace("ub['identity']","vb['identity']")
    with (D/'successor-interface-body.txt').open('x') as f: f.write(textwrap.dedent(lattice))
    exec(compile(textwrap.dedent(lattice),str(D/'successor-interface-body.txt'),'exec'),globals())
    # Also bind the full independently certified radical preimage used for
    # all V action dividends; both integer generation directions are checked.
    rp=read(audit353/'radical-independent-preimage.json'); rc=read(D/'radical-lattice.json')
    RJ=rc['basis']; RG=rp['generators']; RI=rat(rp['inverse'])
    for a,h,w in [(RG,48,95),(rp['G_to_basis'],95,48),(rp['basis_to_G'],48,95), (RJ,48,48)]:shape(a,h,w)
    need(RJ==rp['basis'] and RG==rc['S'] and mm(RG,rp['G_to_basis'])==RJ
        and mm(RJ,rp['basis_to_G'])==RG and mm(RJ,RI)==I and mm(RI,RJ)==I,
        'whole_actual_V_radical_two_sided_preimage')
    save('successor-input-validation.json',{'status':'PASS','failures':[],
        'original349_divisions':27648,'original351_divisions':fixed351,'original353_divisions':fixed353,
        'fresh_input_divisions':fresh_s+fresh_u+fresh_v,'six_original349_351_353_solves_replayed':True,
        'complete_five_column_multiplier_and_both_global_preimages':True,
        'all_before_successor_products':True})
    report['phase']='table_source_specialization'
    p=(table_source/'produce.py').read_text()
    p=p.replace('u-basis.json','v-basis.json').replace('decision-343.json','decision-351.json')
    p=p.replace('[1]*44+[2]*4','[1]*43+[2]*5').replace("'basis_in_u'","'basis_in_v'")
    p=p.replace('u-product-','v-product-').replace("save('v-", "save('w-")
    p=p.replace("'scale':496", "'scale':992").replace("'input_scale':248", "'input_scale':496")
    p=p.replace("'prior_scales':[31,62,124,248]", "'prior_scales':[31,62,124,248,496]")
    p=p.replace("'index':16", "'index':32").replace('496*power','992*power').replace('scale_496','scale_992')
    p=p.replace('index=16,scale=496','index=32,scale=992')
    v=(table_source/'verify_v.py').read_text()
    # Simultaneous variable-name moves avoid rewriting the old basis path.
    v=v.replace("old=read('u-basis.json'); got=read('v-basis.json')",
        "old=read('v-basis.json'); got=read('w-basis.json')")
    v=v.replace('decision-343.json','decision-351.json').replace('decision-345.json','decision-353.json')
    v=v.replace('V-independent-multiplier.json','W-independent-multiplier.json')
    v=v.replace('>=44','>=43').replace('==16','==32').replace("d['kernel_dimension']==4","d['kernel_dimension']==5")
    v=v.replace('[V:U] = absolute determinant of U basis in V','[(I:I):V] = absolute determinant of V basis in (I:I)')
    v=v.replace("got['basis_in_u']","got['basis_in_v']")
    v=replace(v,"old['scale']==248 and old['original_scale']==31 and old['input_scale']==124\n        and got['scale']==496 and got['input_scale']==248",
        "old['scale']==496 and old['original_scale']==31 and old['input_scale']==248\n        and got['scale']==992 and got['input_scale']==496")
    v=v.replace("got['prior_scales']==[31,62,124,248]", "got['prior_scales']==[31,62,124,248,496]")
    v=v.replace('F(496*','F(992*').replace('poly[a]-=496*z*x','poly[a]-=992*z*x')
    v=v.replace("read('v-product-", "read('w-product-").replace("save('v-division-", "save('w-division-")
    v=v.replace('scale=496','scale=992').replace('v-verification-report.json','w-verification-report.json')
    v=v.replace('exact_index_eight_orientation','exact_index_thirty_two_orientation')
    v=v.replace('Independent V replay','Independent W replay').replace('audited_V','audited_W')
    for n,t in [('produce.py',p),('verify_w.py',v)]:
        compile(t,str(D/n),'exec')
        with (D/n).open('x') as f: f.write(t)
    code={p.name:digest(p) for p in D.iterdir() if p.suffix in ('.py','.txt')}
    save('code-hashes.json',code); save('complete-copy-manifest.json',manifest)
    report['phase']='one_successor_table_production'
    prod=run('produce.py','producer-report.json')
    need(prod['products']==2304 and prod['product_slots']==110592 and prod['index']==32 and prod['scale']==992,
        'entire_new_table_production')
    report['phase']='independent_original_H_successor_replay'
    wr=run('verify_w.py','w-verification-report.json')
    for k,x in counts.items():need(wr[k]==x,'full_successor_'+k)
    need(wr['index']==32 and wr['scale']==992 and wr['basis_elements']==48,'actual_successor_scale_index')
    wb=read(D/'w-basis.json'); wt=[read(D/('w-product-%02d.json'%i)) for i in range(48)]
    wd=divisions('w-division-',wb,wt)
    save('persisted-input-checks.json',{'status':'PASS','failures':[],
        'original349_divisions':27648,'original351_divisions':fixed351,'original353_divisions':fixed353,
        'fresh_S_U_V_divisions':fresh_s+fresh_u+fresh_v,'successor_divisions':wd,
        'all_actual_dividends_checked':True,'all_six_original349_351_353_solves_replayed':True})
    for bn,tn,b,t in [('basis.json','product-',sb,st),('u-basis.json','u-product-',ub,ut),
        ('v-basis.json','v-product-',vb,vt),('w-basis.json','w-product-',wb,wt)]:
        need(read(D/bn)==b and all(read(D/(tn+'%02d.json'%i))==t[i] for i in range(48)), 'entire_final_table_reread_'+bn)
    for n,obj in [('producer-report.json',prod),('w-verification-report.json',wr),('solve-report.json',independent),
        ('input-report.json',iv),('u-verification-report.json',uv),('v-verification-report.json',vr)]:
        need(read(D/n)==obj,'entire_final_report_'+n)
    report['phase']='final_preservation'
    after={n:digest(ROOT/n) for n in before}; copies={n:digest(D/n) for n in manifest}
    code_after={n:digest(D/n) for n in code}
    need(before==after and code==code_after and copies=={n:e['sha256'] for n,e in manifest.items()},
        'all_original_copy_source_preservation')
    preservation={'equal':True,'before':before,'after':after,'code_before':code,'code_after':code_after,
        'fixed_before':{n:e['sha256'] for n,e in manifest.items()},'fixed_after':copies}
    save('preservation-stage.json',preservation)
    for n,obj in [('preservation-stage.json',preservation),('canonical-input-hashes.json',before),
        ('complete-copy-manifest.json',manifest),('code-hashes.json',code),('inventory-transition.json',transition)]:
        need(read(D/n)==obj,'complete_final_inventory_reread_'+n)
    for n in ['persisted-input-checks.json','successor-input-validation.json']:
        r=read(D/n);need(r['status']=='PASS' and not r['failures'],'full_final_evidence_'+n)
    report.update(status='PASS',phase='complete',index=32,scale=992,products=2304,product_slots=110592,
        original349_divisions=27648,original351_divisions=fixed351,original353_divisions=fixed353,
        fresh_input_divisions=fresh_s+fresh_u+fresh_v,successor_divisions=wd,
        all_actual_dividends_checked=True,original_files=len(before),fixed_copies=len(manifest),
        source_files=len(code),six_original349_351_353_solves_replayed=True)
except Exception as exc:
    report.update(status='STOP',failures=[type(exc).__name__+': '+str(exc)])
report.update(seconds=time.monotonic()-START,required_seconds=180,required_bytes=134217728)
save('stage-report.json',report); print(json.dumps(report)); sys.exit(0 if report['status']=='PASS' else 1)
