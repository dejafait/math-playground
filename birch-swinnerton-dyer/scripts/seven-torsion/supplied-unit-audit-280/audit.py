"""One aggregate audit: exact copied replay, complete comparison, Laplace records."""
from pathlib import Path
from fractions import Fraction as Q
import hashlib,json,runpy,signal,sys,time,traceback
import stage_io as io
R=Path(__file__).resolve().parent;U=R.parent;O=U/'supplied-unit-278'
t=time.monotonic();CAP=134217728
report={'passed':False,'failures':[],'checks':[],'excluded_verification_report_fields':['seconds','preserved_files','changed_or_missing']}
written=[]
def need(ok,label):
    if not ok:raise ValueError(label)
    report['checks'].append(label)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def preservation():
    inv=io.read(R/'originals.json')
    changed=[p for p,h in inv.items() if not (U/p).is_file() or sha(U/p)!=h]
    return {'preserved_files':len(inv),'changed_or_missing':changed}
def alarm(*_):raise TimeoutError('aggregate 180-second arithmetic-stage limit')
signal.signal(signal.SIGALRM,alarm);signal.setitimer(signal.ITIMER_REAL,180)
original_save=io.save
# These overrides affect I/O timing and reporting only. Arithmetic code is unchanged.
def replay_save(name,value):
    original_save(name,value);written.append(name)
def replay_finish(name,result,unused):
    result.update(seconds=time.monotonic()-t,required_seconds=180,**preservation())
    if result['changed_or_missing']:
        result['passed']=False;result['failures'].append('original bytes changed')
    io.save(name+'-report.json',result)
    need(result['passed'] and not result['failures'],'fresh_complete_verifier_passes')
def replay_exit(code=0):
    need(code==0,'fresh_verifier_exit_zero')
io.start=lambda:t;io.finish=replay_finish;io.save=replay_save
old_exit=sys.exit;sys.exit=replay_exit
try:
    inventory=io.read(R/'input-inventory.json')
    for name,row in inventory['copies'].items():
        need(sha(R/name)==row['sha256']==sha(U/row['source']),'byte_identical_input_'+name)
    need(io.read(R/'construction-report.json')['passed'],'copied_construction_provenance')
    prior=io.read(O/'originals.json');current=io.read(R/'originals.json')
    need(len(prior)==529 and all(current.get(p)==h for p,h in prior.items()),'complete_prior_529_inventory_retained')
    need(all(str(p.relative_to(U)) in current for p in O.rglob('*') if p.is_file() and '__pycache__' not in p.parts),'all_current_original_files_inventoried')
    for name,h in io.read(O/'source-hashes.json').items():
        need(sha(O/name)==h,'original_executed_source_hash_'+name)
    need(not preservation()['changed_or_missing'],'original_hashes_match_before_replay')
    g=runpy.run_path(str(R/'verify_norms.py'),run_name='__main__')
    sys.exit=old_exit
    report['fresh_replay_seconds']=time.monotonic()-t
    # Compare every entire fresh output object. Timing and inventory size are
    # the only execution-dependent report fields; mathematical payload is exact.
    comparisons=[]
    for name in written:
        fresh=io.read(R/name);saved=io.read(O/name)
        excluded=report['excluded_verification_report_fields'] if name=='verification-report.json' else []
        if excluded:
            fresh={k:v for k,v in fresh.items() if k not in excluded}
            saved={k:v for k,v in saved.items() if k not in excluded}
        need(fresh==saved,'complete_saved_fresh_'+name)
        comparisons.append({'path':name,'all_payload_equal':True,'excluded_fields':excluded,'fresh_sha256':sha(R/name),'original_sha256':sha(O/name)})
    need(len([x for x in written if x.startswith('faddeev-') and '-result' not in x])==35,'all_35_recurrence_records')
    need(len([x for x in written if x.startswith('faddeev-') and '-result' in x])==5,'all_five_characteristic_and_terminal_records')
    original_save('complete-output-comparisons.json',comparisons)
    # Full accepted incidence evidence and all transports, not previews/flags.
    a=io.read(U/'incidence-269/complete-replay-evidence.json')
    b=io.read(U/'incidence-audit-271/complete-replay-evidence.json')
    need(a==b,'complete_incidence_269_271_evidence_agreement')
    dense=io.read(U/'incidence-audit-271/dense-evidence.json')
    trans=io.read(R/'verification-transports.json')
    for key in ('point_standard_columns','point_power_columns','line_columns','point_original_x','point_original_y'):
        need(trans[key]==a[key]==dense[key],'full_upstream_transport_'+key)
    for key in ('F','y_V_factor'):
        convert=g['l'] if key=='F' else None
        if key=='F':need(tuple(map(g['l'],a[key]))==g['F'],'complete_upstream_F')
        else:need(g['e'](a[key])==g['yf'],'complete_upstream_y_factor')
    def allzero(x):
        if isinstance(x,dict):return all(allzero(v) for v in x.values())
        if isinstance(x,list):return all(allzero(v) for v in x)
        return Q(x)==0
    need(allzero(a['residuals']) and allzero(dense['residuals']),'complete_accepted_upstream_residuals_zero')
    # Independent bottom-up certificate check of the imported cofactor formula.
    # No producer code is imported. Reachability is derived from complete
    # matrices, so a missing or extra recorded minor cannot pass.
    bz,bo=g['bz'],g['bo'];ba,bn,bm,bf=g['ba'],g['bn'],g['bm'],g['bf']
    def flat(v):return tuple(map(Q,v))
    def key(cols):return ','.join(map(str,cols))
    labels=['a','b','a_prime','scalar2','zero'];minor_counts={}
    for label in labels:
        matrix=g['matrices'][label]
        saved=io.read(R/('laplace-'+label+'.json'))
        need(saved['row_rule']=='7 - len(columns)' and flat(saved['empty_minor'])==bf(bo),'laplace_conventions_'+label)
        reachable=set();pending=[tuple(range(7))]
        while pending:
            cols=pending.pop()
            if not cols or cols in reachable:continue
            reachable.add(cols);r=7-len(cols)
            for j,c in enumerate(cols):
                if matrix[r][c]!=bz:pending.append(cols[:j]+cols[j+1:])
        need(set(saved['ordered_remaining_column_minors'])=={key(c) for c in reachable},'exact_reachable_minor_key_set_'+label)
        values={():bo};records={}
        for cols in sorted(reachable,key=lambda x:(len(x),x)):
            row=7-len(cols);value=bz;terms=[]
            for j,c in enumerate(cols):
                child=cols[:j]+cols[j+1:]
                if matrix[row][c]==bz:
                    terms.append({'column':c,'position':j,'zero_entry_branch':True});continue
                term=bm(matrix[row][c],values[child]);signed=term if j%2==0 else bn(term)
                value=ba(value,signed)
                terms.append({'column':c,'position':j,'child':key(child),'sign':(-1)**j,'signed_term':bf(signed)})
            need(flat(saved['ordered_remaining_column_minors'][key(cols)])==bf(value),'entire_laplace_minor_'+label+'_'+key(cols))
            values[cols]=value;records[key(cols)]={'value':bf(value),'terms':terms}
        root=bf(values[tuple(range(7))]);fresh=io.read(R/('faddeev-'+label+'-result.json'))
        need(root==flat(saved['norm'])==flat(fresh['norm']),'full_laplace_faddeev_norm_'+label)
        final=g['savednorm']['norms'][label]
        need(root==flat(final)==flat(io.read(R/('norm-'+label+'.json'))['norm']),'full_stored_norm_'+label)
        original_save('checked-laplace-'+label+'.json',{'empty_minor':bf(bo),'minors':records,'norm':root,'exact_reachable_key_coverage':True})
        minor_counts[label]=len(records)
    expected={'a':127,'b':127,'a_prime':127,'scalar2':7,'zero':1}
    need(minor_counts==expected==io.read(O/'complete-evidence-inspection.json')['laplace_minor_counts'],'all_389_saved_minor_records')
    need(g['savednorm']['mixed_root_claim'] is False,'no_mixed_root_claim')
    rejection=io.read(R/'rejections.json')
    need(len(rejection)==5 and rejection==io.read(O/'producer-rejections.json'),'all_five_producer_and_verifier_rejection_conditions_agree')
    need(all(r['rejected'] and r['full_malformed_replay'] is False and r['scope']=='named full-data condition only' for r in rejection),'rejections_retain_condition_only_scope')
    need(io.read(O/'producer-input-rejections.json')==rejection[:3],'all_three_producer_input_rejections_retained')
    need(set(written)==set(['verification-transports.json','independent-inputs.json','independent-matrices.json','rejections.json','verification-summary.json','verification-report.json'] + ['mutant-'+r['case']+'.json' for r in rejection] + ['faddeev-'+label+'-'+str(k)+'.json' for label in labels for k in range(1,8)] + ['faddeev-'+label+'-result.json' for label in labels]),'exact_full_fresh_output_file_set')
    report.update(laplace_minor_counts=minor_counts,full_compared_output_files=len(comparisons),matrix_slots=11760,norm_slots=240,recurrence_records=35,passed=True)
except BaseException as exc:
    report['passed']=False;report['failures'].append(type(exc).__name__+': '+str(exc))
    traceback.print_exc()
finally:
    sys.exit=old_exit
    keep=preservation();original_save('audit-preservation.json',keep)
    if keep['changed_or_missing']:report['passed']=False;report['failures'].append('original preservation failure')
    report.update(seconds=time.monotonic()-t,required_seconds=180,required_bytes=CAP,**keep)
    if report['seconds']>180:report['passed']=False;report['failures'].append('aggregate internal cap exceeded')
    report['bytes_before_report']=sum(p.stat().st_size for p in R.rglob('*') if p.is_file())
    original_save('audit-report.json',report)
    signal.setitimer(signal.ITIMER_REAL,0)
    print(json.dumps({k:v for k,v in report.items() if k!='checks'}),flush=True)
sys.exit(0 if report['passed'] else 1)
