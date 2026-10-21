"""Replay-only V audit. Source extraction and all work run inside the watchdog."""
from pathlib import Path
from fractions import Fraction as F
import hashlib, json, subprocess, sys, time, textwrap
sys.set_int_max_str_digits(0)
D=Path(__file__).resolve().parent; ROOT=D.parents[2]; S=D.parent; START=time.monotonic()
def save(n,x):
    with (D/n).open('x') as f: json.dump(x,f,separators=(',',':')); f.write('\n')
report={'status':'STOP','failures':[],'phase':'source_helpers'}
try:
    prior=S/'index-sixteen-table-347'
    source=(prior/'stage.py').read_text()
    # Only definitions/imports, never the historical stage, preparation or producer.
    helpers=source.split('def prepare_sources():')[0]
    exec(compile(helpers,str(prior/'stage.py')+':helpers','exec'),globals())
    report['phase']='initial_inventory'
    previous=read(prior/'canonical-input-hashes.json'); need(len(previous)==3330,'entire_step347_inventory')
    names=set(previous)
    names.update(str(p.relative_to(ROOT)) for p in prior.rglob('*') if p.is_file())
    names.update(['lemmas/L090-conductor389-index-sixteen-multiplier-order-table.md',
        'drafts/literature/2026-10-19-index-sixteen-table-critical-audit.md',
        'drafts/2026-10-19-index-sixteen-table-critical-audit-attempt.md',
        'history/347-2026-10-19-index-sixteen-table.md',
        'history/348-2026-10-19-index-sixteen-table-audit-scope.md',
        'scripts/seven-torsion/index-eight-table-audit-341/independent.py',
        'ATTEMPTS/041-first-overorder-integral-power-witness-cap.md',
        'ATTEMPTS/042-changed-order-audit-approval-repetition.md',
        'ATTEMPTS/044-index-four-table-verifier-integer-zero.md'])
    before={n:digest(ROOT/n) for n in sorted(names)}
    note='drafts/2026-10-19-index-sixteen-table-attempt.md'
    oldhash='d0917f59ac51e1bd824dc732f96b50bbbe4b5e84eb099a28e22b0da1f7e4cd79'
    newhash='ba7345d0f3cf539defa7231456dbedbcebd5f9d73bbfb1f61159dbf60fb970a5'
    raw=(ROOT/note).read_bytes(); marker=b'\n## Completed execution\n'
    need(raw.count(marker)==1,'one_documentation_outcome_append')
    prefix=raw.split(marker)[0]
    need(hashlib.sha256(prefix).hexdigest()==oldhash and previous[note]==oldhash and before[note]==newhash,
         'exact_documentation_only_append_bytes')
    need(all(before[n]==h for n,h in previous.items() if n!=note),'all_other_step347_inputs_unchanged')
    prior_transition=read(prior/'inventory-transition.json')
    # Validate each previously authorized historical transition against its actual inventory.
    transitions=[(prior_transition,'only_permitted_post345_document_change','U-two-audit-345'),
        (prior_transition['retained_step345_transition']['retained_step343_transition'],
         'only_permitted_post341_document_change','index-eight-table-audit-341'),
        (prior_transition['retained_step345_transition']['retained_step343_transition']['retained_post337_transition'],
         'only_permitted_post337_document_change','index-eight-audit-337')]
    changed={note}
    for t,key,folder in transitions:
        n=t[key]; historical=read(S/folder/'canonical-input-hashes.json')
        need(t['prior']==historical[n] and t['current']==before[n],'exact_retained_transition_'+folder)
        changed.add(n)
    for folder in ['U-two-audit-345','index-eight-table-audit-341','index-eight-audit-337']:
        historical=read(S/folder/'canonical-input-hashes.json')
        need(all(before[n]==h for n,h in historical.items() if n not in changed),'every_other_historical_input_'+folder)
    save('canonical-input-hashes.json',before)
    transition={'only_new_document_change':note,'prior':oldhash,'current':newhash,
        'prefix_reconstructed_and_hashed':True,'retained_step347_transition':prior_transition}
    save('inventory-transition.json',transition)
    for folder,count in [(S/'index-eight-order-two-343',248),(S/'U-two-audit-345',447),(prior,449)]:
        manifest_old=read(folder/'copy-manifest.json'); need(len(manifest_old)==count,'complete_manifest_'+folder.name)
        for n,e in manifest_old.items():
            need(before[e['source']]==e['sha256']==before[str((folder/n).relative_to(ROOT))],
                 'all_copy_source_bindings_'+folder.name+'_'+n)
    oldcodes=read(prior/'code-hashes.json'); need(len(oldcodes)==6,'all_six_step347_sources')
    need(all(digest(prior/n)==h for n,h in oldcodes.items()),'six_executed_sources_unchanged')
    manifest={}
    def copy(dest,src):
        key=str(src.relative_to(ROOT)); raw=src.read_bytes()
        need(hashlib.sha256(raw).hexdigest()==before[key],'source_before_copy_'+dest)
        with (D/dest).open('xb') as f: f.write(raw)
        need(digest(D/dest)==before[key],'full_copy_'+dest)
        manifest[dest]={'source':key,'sha256':before[key]}
    # The complete step-347 fixed set, retaining all original343 names and action matrices.
    for name in read(prior/'copy-manifest.json'): copy(name,prior/name)
    vfiles=['v-basis.json']+['v-product-%02d.json'%i for i in range(48)]
    for name in vfiles+['verify_v.py']: copy(name,prior/name)
    for pre in ['division-','u-division-','v-division-']:
        for i in range(48): copy('original347-'+pre+'%02d.json'%i,prior/(pre+'%02d.json'%i))
    sfiles=['basis.json']+['product-%02d.json'%i for i in range(48)]
    ufiles=['u-basis.json']+['u-product-%02d.json'%i for i in range(48)]
    for name in sfiles:
        for dn in ['index-four-table-329','preserved-table-replay-331','preserved-table-audit-333',
            'index-four-order-two-335','index-eight-audit-337','index-eight-table-339','index-eight-table-audit-341']:
            need(digest(S/dn/name)==manifest[name]['sha256'],'entire_S_provenance_'+dn+'_'+name)
    for name in ufiles:
        for dn in ['index-eight-table-339','index-eight-table-audit-341','index-eight-order-two-343','U-two-audit-345']:
            need(digest(S/dn/name)==manifest[name]['sha256'],'entire_U_provenance_'+dn+'_'+name)
    save('copy-manifest.json',manifest)
    independent_source=(S/'index-eight-table-audit-341/independent.py').read_text()
    head=independent_source.split("    got=load(D/'u-basis.json')")[0]
    need('def main():' in head and head.endswith('for r in s]\n'),'precise_independent_source_boundary')
    independent=head+(D/'independent-body.txt').read_text()
    compile(independent,str(D/'independent.py'),'exec')
    with (D/'independent.py').open('x') as f: f.write(independent)
    code={p.name:digest(p) for p in D.iterdir() if p.suffix=='.py' or p.name=='independent-body.txt'}
    save('code-hashes.json',code)
    report['phase']='complete_S_U_replay_and_original_dividends'
    counts={'product_slots':110592,'product_identities':2304,'remainder_coefficients':218880,
        'transport_entries':18432,'inverse_products':8,'division_certificates':2304,'identity_actions':96}
    iv=run('input_verify.py','input-report.json')
    for k,x in counts.items(): need(iv[k]==x,'full_S_'+k)
    need(iv['index']==4,'S_index')
    sb=read(D/'basis.json'); st=[read(D/('product-%02d.json'%i)) for i in range(48)]
    prefixes=['fixed-S-original-division-','fixed-S-fresh-division-','division-',
        'fixed-U-division-','u-division-','action-division-']
    checked={p:divisions('original343-'+p,sb,st) for p in prefixes[:3]}
    original347s=divisions('original347-division-',sb,st); fresh_s=divisions('division-',sb,st)
    uv=run('verify_u.py','u-verification-report.json')
    for k,x in counts.items(): need(uv[k]==x,'full_U_'+k)
    need(uv['index']==8 and uv['scale']==248 and uv['basis_elements']==48,'U_scale_index')
    ub=read(D/'u-basis.json'); ut=[read(D/('u-product-%02d.json'%i)) for i in range(48)]
    for p in prefixes[3:5]: checked[p]=divisions('original343-'+p,ub,ut)
    original347u=divisions('original347-u-division-',ub,ut); fresh_u=divisions('u-division-',ub,ut)
    J=read(D/'radical-lattice.json')['basis']
    checked['action-division-']=divisions('original343-action-division-',ub,ut,J)
    need(sum(checked.values())==13824 and set(checked)==set(prefixes),'all_six_original343_sets')
    report['phase']='full_audited_V_lattice_interfaces'
    # Exact inspected full-lattice comparison only; no radical/action kernel or production.
    block=source.split("    report['phase']='full_audited_V_lattice_interfaces'\n",1)[1]
    block=block.split("    report['phase']='one_V_table_production'",1)[0]
    exec(compile(textwrap.dedent(block),str(prior/'stage.py')+':lattice_interfaces','exec'),globals())
    report['phase']='full_V_original_H_replay'
    vr=run('verify_v.py','v-verification-report.json')
    for k,x in counts.items(): need(vr[k]==x,'full_V_'+k)
    need(vr['index']==16 and vr['scale']==496 and vr['basis_elements']==48,'V_scale_index')
    vb=read(D/'v-basis.json'); vt=[read(D/('v-product-%02d.json'%i)) for i in range(48)]
    original347v=divisions('original347-v-division-',vb,vt); fresh_v=divisions('v-division-',vb,vt)
    report['phase']='independent_complete_basis_systems'
    ind=run('independent.py','independent-report.json')
    for k,x in {'elimination_systems':6,'transport_entries':13824,'inclusion_entries':4608,
        'scaled_slots':11520,'index':16,'identity_entries':96,'solved_identity_actions':192,
        'complete_certificate_reread':True,'both_integral_V_containments':True}.items(): need(ind[k]==x,'independent_'+k)
    for name,obj in [('input-report.json',iv),('u-verification-report.json',uv),
        ('v-verification-report.json',vr),('independent-report.json',ind),('input-validation.json',evidence)]:
        need(read(D/name)==obj,'all_report_rereads_'+name)
    for bn,tn,b,t in [('basis.json','product-',sb,st),('u-basis.json','u-product-',ub,ut),('v-basis.json','v-product-',vb,vt)]:
        need(read(D/bn)==b and all(read(D/(tn+'%02d.json'%i))==t[i] for i in range(48)),'all_full_table_rereads_'+bn)
    report['phase']='final_preservation'
    after={n:digest(ROOT/n) for n in before}; copies={n:digest(D/n) for n in manifest}
    code_after={n:digest(D/n) for n in code}
    need(before==after and code==code_after and copies=={n:e['sha256'] for n,e in manifest.items()},'complete_preservation')
    preservation={'equal':True,'before':before,'after':after,'code_before':code,'code_after':code_after,
        'fixed_before':{n:e['sha256'] for n,e in manifest.items()},'fixed_after':copies}
    save('audit-preservation.json',preservation)
    for name,obj in [('audit-preservation.json',preservation),('copy-manifest.json',manifest),
        ('canonical-input-hashes.json',before),('code-hashes.json',code),('inventory-transition.json',transition)]:
        need(read(D/name)==obj,'all_inventory_rereads_'+name)
    report.update(status='PASS',phase='complete',original_files=len(before),fixed_copies=len(manifest),
        prepared_and_executed_source_files=len(code),original343_divisions=checked,
        original343_count=sum(checked.values()),original347_S_U_count=original347s+original347u,
        original347_V_count=original347v,fresh_count=fresh_s+fresh_u+fresh_v,
        product_slots_per_table=110592,products_per_table=2304,index=16,scale=496,
        independent=ind,all_actual_dividends_checked=True)
except Exception as e:
    report.update(status='STOP',failures=[type(e).__name__+': '+str(e)])
report.update(seconds=time.monotonic()-START,required_seconds=180,required_bytes=134217728)
save('audit-report.json',report)
print(json.dumps(report)); sys.exit(0 if report['status']=='PASS' else 1)
