"""Complete retained evidence/rejection audit; no original file writes."""
from pathlib import Path
from fractions import Fraction as Q
import copy, hashlib, importlib.util, json, signal, time
R=Path(__file__).resolve().parent; U=R.parent; D=U/'compressed-249'
start=time.monotonic(); signal.alarm(180)
checks=[]
def need(ok,label):
    if not ok:raise ValueError(label)
    checks.append(label)
def read(p):return json.loads(p.read_text())
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
spec=importlib.util.spec_from_file_location('direction_replay',D/'verify_direction.py')
V=importlib.util.module_from_spec(spec);spec.loader.exec_module(V)
c=read(D/'direction.json'); fresh=read(R/'direction.json')
for name in ['direction-replay.json','final-direction-replay.json']:
    old=read(D/name)
    need(old['passed'] is True and old['failures']==[],name+'_passed')
    need(old['checks']==fresh['checks'] and len(old['checks'])==93,name+'_all_checks')
    for key in ['dimension','required_dimension','mixed_rank','required_mixed_rank']:
        need(old[key]==fresh[key],name+'_'+key)
    need(old['seconds']<180,name+'_time')
retained=read(D/'direction-rejections.json')
need(retained['passed'] and not retained['upstream_changed'] and not retained['direction_changed'],
     'retained_rejection_result')
expected={'wrong_scalar':'all_2304_Reynolds_entries_six_scalars',
          'wrong_degree':'degree_eight_monic','wrong_inclusion':'entire_B_inclusion',
          'wrong_inverse':'B_inverse_on_full_image'}
need(len(retained['cases'])==4 and {r['case'] for r in retained['cases']}==set(expected),
     'complete_retained_case_list')
cases=[]
for name,label in expected.items():
    saved=read(D/'rejections'/(name+'.json')); target=copy.deepcopy(c); action=None
    if name=='wrong_scalar':
        original_action=read(U/'scalar-actions-243/actions.json')
        original_action['maps']['2']['B_action'][0][0]='2'
        action=D/'rejections/altered-actions.json'
        need(read(action)==original_action,'scalar_fixture_exact_one_entry_change')
        target['action_hash']=digest(action)
    elif name=='wrong_degree':target['h']=target['h'][:-1]
    elif name=='wrong_inclusion':target['E_B'][0][0]='2'
    else:
        target['K_B'][0][0]=str(Q(target['K_B'][0][0])+1)
        # Independent row/column rational product checks the deliberately
        # consistent altered projection; the crosscheck uses integer products.
        target['R_B']=[[str(sum(Q(a)*Q(b) for a,b in zip(row,col)))
                        for col in zip(*target['K_B'])] for row in target['E_B']]
    need(saved==target,name+'_entire_fixture_matches_intended_change')
    old=next(r for r in retained['cases'] if r['case']==name)
    need(old['passed'] and old['actual']==old['expected']==label,name+'_retained_label')
    try:
        V.run(D/'rejections'/(name+'.json'),action); actual='ACCEPTED'
    except ValueError as e:actual=str(e)
    signal.alarm(180)
    need(actual==label,name+'_fresh_mathematical_rejection')
    cases.append({'case':name,'actual':actual,'required':label,'passed':True})
for stage in ['build_direction','verify_direction','check_direction_rejections']:
    watchdog=read(D/(stage+'-watchdog.json'))
    need(watchdog['returncode']==0 and not watchdog['watchdog_fired']
         and watchdog['seconds']<181 and watchdog['child_limit']==180
         and watchdog['watchdog_limit']==181 and watchdog['certificate_bytes']<watchdog['byte_cap'],
         stage+'_retained_watchdog')
    # These logs are each one JSON summary, not truncated transcript previews.
    log=read(D/(stage+'.log'))
    if stage=='build_direction':
        need(log['status']=='PRODUCED_UNVERIFIED' and log['actual_dimension']==8
             and log['required_dimension']==8 and log['mixed_rank']==log['required_rank']==24,
             'producer_log_scope_and_dimensions')
    else:need(log['passed'] is True,stage+'_log_passed')
    need(log['seconds']<180,stage+'_log_time')
final=read(D/'final-preservation.json')
need(final['upstream_changed']==[] and final['direction_replay_passed'] and final['direction_rejections_passed'],
     'old_final_preservation_claim')
for name,entry in final['inventory'].items():
    path=D/name
    need(path.stat().st_size==entry['bytes'] and digest(path)==entry['sha256'],
         'old_inventory_'+name)
old_manifest=read(D/'original-manifest.json')
need(len(old_manifest)==final['upstream_files_checked']==retained['upstream_files'],
     'old_upstream_inventory_counts')
for name,sha in old_manifest.items():need(digest(U/name)==sha,'old_upstream_'+name)
# The earlier capped output is preserved, not mathematically imported.
need(final['target_completed'] is False and final['actual_relation_columns']==26
     and final['required_relation_columns']==336, 'unverified_relation_stop_retained')
manifest=read(R/'original-manifest.json')
changed=[name for name,sha in manifest.items() if not (U/name).is_file() or digest(U/name)!=sha]
need(not changed,'all_original_bytes_preserved')
up=read(R/'upstream.json');act=read(R/'actions.json');cross=read(R/'crosscheck.json')
need(up['status']=='PASS' and up['failures']==[],'fresh_upstream_report')
need(act['status']=='PASS' and act['failures']==[] and act['basis_images']==576
     and act['matrix_composition_entries_checked']==act['matrix_composition_entries_required']==165888,
     'fresh_complete_action_report')
need(len(act['scalar_compositions'])==36 and all(not r['failures'] and
     r['B_entries_checked']==r['T_entries_checked']==2304 for r in act['scalar_compositions']),
     'every_scalar_composition_report')
need(cross['passed'] and not cross['failures'] and len(cross['characteristic_evaluations'])==25
     and all(r['determinant']==r['h_cubed'] for r in cross['characteristic_evaluations']),
     'complete_distinct_check_report')
need(fresh['passed'] and fresh['failures']==[],'fresh_direction_report')
report={'passed':True,'failures':[],'checks':checks,'cases':cases,
        'original_files':len(manifest),'changed_originals':changed,
        'retained_inventory_files':len(final['inventory']),
        'retained_upstream_files':len(old_manifest),'fresh_direction_checks':len(fresh['checks']),
        'fresh_distinct_checks':len(cross['checks']),
        'seconds':time.monotonic()-start,'required_seconds':180,
        'actual_fixed_rank':8,'required_fixed_rank':8,
        'scope':'L070 only; no incidence or Selmer conclusion'}
need(report['seconds']<180,'evidence_inspection_time')
with (R/'audit-report.json').open('x') as out:json.dump(report,out,indent=2)
signal.alarm(0)
print(json.dumps({k:v for k,v in report.items() if k!='checks'}))
