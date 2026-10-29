"""Read complete saved evidence after execution; no arithmetic module imports.

Outputs are post-execution review and are outside the production cap.
"""
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import traceback

ROOT = Path.cwd()
BASE = ROOT/'scripts/four-rational-kernels'
RUN = BASE/'step-468'
OUT = BASE/'step-468-postcheck'
OUT.mkdir()

def read(name):
    return json.loads((RUN/name).read_text())

def identity(path):
    raw = path.read_bytes()
    return {'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw)}

summary = {'status':'INCOMPLETE','post_execution_outside_production_cap':True}
try:
    terminal = read('terminal-report.json')
    final = read('finalization.json')
    assert terminal['status']=='PASS' and terminal['failure'] is None
    assert terminal['completed_indices']==[39,40,41,42]
    assert terminal['inclusive_seconds']<=180 and terminal['inclusive_new_bytes']<=134217728
    assert final['elapsed_after_terminal_seconds']<=terminal['inclusive_seconds']
    assert final['new_bytes_after_terminal']<=terminal['inclusive_new_bytes']
    assert final['preservation_rechecked_after_terminal'] and final['all_children_observed_before_terminal']
    assert final['terminal_timer_retained'] and final['parent_exit_time_not_claimed']
    assert read('observed-child-exits.json')==terminal['child_exits']
    assert [e['n'] for e in terminal['child_exits']]==[39,40,41,42]
    assert all(e['returncode']==0 and e['observed_exit_seconds']<174 for e in terminal['child_exits'])
    initial=read('initial-inventory.json')
    assert len(initial)==terminal['preserved_inputs']
    preservation=read('preservation.json')
    assert preservation['files']==initial and preservation['count']==len(initial)
    assert preservation['mismatches']==[]
    assert all(preservation[k] for k in ('all_match','capture_complete','tree_sets_equal','fresh_sources_equal'))
    assert all(identity(ROOT/p)==entry for p,entry in initial.items())
    sources=read('source-hashes.json')
    assert len(sources)==10 and all(identity(ROOT/p)==v for p,v in sources.items())
    assert (RUN/'coordinator.py').read_bytes()==(BASE/'step-468-prelaunch/coordinator.py').read_bytes()
    assert (RUN/'worker.py').read_bytes()==(BASE/'step-468-prelaunch/worker-expected.py').read_bytes()
    reconciliation=read('historical-reconciliation.json')
    assert reconciliation['status']=='PASS' and reconciliation['no_path_exemptions']
    assert reconciliation['failed444_frozen_separately']
    assert list(sorted(map(int,reconciliation['inventories'])))==[417,419,422,424,429,431,433,435,437,440,442,446,449,451,453,455,457,459,461,463]
    assert all(row['all_match'] for row in reconciliation['inventories'].values())
    for step, report in reconciliation['original_reports_at_original_boundaries'].items():
        assert report==json.loads((BASE/f'step-{step}/historical-reconciliation.json').read_text())
    fixed=json.loads((ROOT/'scripts/first-rational-kernel/step-404/parameter.json').read_text())
    ledger={'add':21787232,'clip':24386,'coefficient_pairs':21264880,'convert':5083,
            'divide':716408,'enlarge':2034,'multiply':21801456,'negate':356616,'scale':2033}
    rows=[]
    for n in (39,40,41,42):
        prefix=f'n-{n}/'
        parameter=read(prefix+'parameter.json')
        assert parameter==fixed
        assert read(prefix+'parameter-identity.json')=={'n':n,'complete_record_equal':True,'midpoint_unchanged':True}
        status=read(prefix+'status.json')
        assert status['status']=='PASS' and status['n']==n and status['panels']==1016
        assert status['pairs_per_pass']==21264880
        assert status['strict_radius_tests']==[183,50]
        assert all(status[k] for k in ('parameter_complete_equal','ledger_equal','identity_unchanged','full_returned_report_persisted'))
        kernel=read(prefix+'kernel.json')
        returned=read(prefix+'returned-report.json')
        assert returned=={'status':'PASS','parameter':'complete exact reconstruction','panels':1016,
            'coefficient_pairs':21264880,'counts':ledger,'radius':kernel['radius'],
            'all_stage_comparisons':'PASS','signed_rounding_checks':'every conversion, multiplication and division',
            'originals_preserved':'checked by aggregate runner'}
        assert read(prefix+'replay.json')==dict(returned,n=n)
        assert kernel['counts']==ledger and kernel['n']==n and kernel['complete_panels']==1016
        for name in ('producer-ledger.json','replay-ledger.json'):
            assert read(prefix+name)=={'n':n,'counts':ledger}
        ident=read(prefix+'identity-before.json')
        assert ident==read(prefix+'identity-after-production.json')==read(prefix+'identity-after-replay.json')
        expected_identity=[n,str((RUN/f'n-{n}').resolve()),f'kernel_468_{n}',
                           identity(RUN/f'n-{n}/producer.py')['sha256'],identity(RUN/f'n-{n}/replay.py')['sha256']]
        assert ident=={'identity':expected_identity}
        review=read(prefix+'source-review.json')
        assert review['n']==n and review['compile_optimize']==0
        assert all(review[k] for k in ('both_scalar_and_beta_arguments_bound','pre_clip_conditions_bound','midpoint_not_scaled','all_independent_arithmetic_and_full_loops_unchanged'))
        for name,pairs in review['unique_exact_changes'].items():
            text=(ROOT/'scripts/second-rational-kernel/step-412'/name).read_text()
            for pair in pairs:
                a,b=pair['old'],pair['new']
                assert text.count(a)==1
                text=text.replace(a,b,1)
            assert text==(RUN/prefix/name).read_text()
        # Inspect every persisted panel and its exact additive running sum.
        running=[0,0]
        count=0
        with (RUN/prefix/'panels.jsonl').open() as handle:
            for j,line in enumerate(handle):
                panel=json.loads(line)
                assert panel['n']==n and panel['index']==j
                assert panel['endpoints']==[[8+j,8],[9+j,8]]
                lo,hi=panel['panel_integral']
                assert lo<=hi
                running=[running[0]+lo,running[1]+hi]
                assert panel['running_sum']==running
                count+=1
        assert count==1016 and running==kernel['polynomial_sum']
        lo,hi=kernel['final_grid']
        assert kernel['grid_denominator']==2**256
        assert [lo,hi]==[running[0]-2**72,running[1]+2**72]
        radius=Fraction(hi-lo,2**257)
        assert radius==Fraction(*kernel['radius'])==Fraction(*status['radius'])
        assert radius<Fraction(1,2**183) and radius<Fraction(1,2**50)
        assert Fraction(*kernel['midpoint'])==Fraction(lo+hi,2**257)
        assert kernel['required_radius']==[1,2**50] and kernel['stronger_radius']==[1,2**183]
        assert (RUN/prefix/'child-stderr.txt').read_bytes()==b''
        assert json.loads((RUN/prefix/'child-stdout.txt').read_text())=={'n':n,'status':'PASS','radius':kernel['radius']}
        rows.append({'n':n,'lower_grid':lo,'upper_grid':hi,'radius':kernel['radius'],
                     'polynomial_width_grid':hi-lo-2**73,'panels':count,'pairs_per_pass':21264880})
    assert read('completed-kernels.json')==[read(f'n-{n}/status.json') for n in (39,40,41,42)]
    summary.update(status='PASS',inputs=len(initial),sources=len(sources),rows=rows,
                   inclusive_seconds=terminal['inclusive_seconds'],required_seconds=180,
                   inclusive_new_bytes=terminal['inclusive_new_bytes'],required_new_bytes=134217728,
                   production_terminal=terminal,production_finalization=final,
                   full_saved_reports_maps_ledgers_panels_checked=True,
                   arithmetic_reexecuted=False,parent_exit_observed_by_tool_separately=True)
except BaseException as exc:
    summary.update(status='STOP',failure={'type':type(exc).__name__,'message':str(exc),'traceback':traceback.format_exc()})
    raise
finally:
    (OUT/'evidence.json').write_text(json.dumps(summary,sort_keys=True,indent=2)+'\n')
    print(json.dumps({k:summary.get(k) for k in ('status','inputs','inclusive_seconds','required_seconds','inclusive_new_bytes','required_new_bytes')},sort_keys=True))
    print('Full post-execution certificate: scripts/four-rational-kernels/step-468-postcheck/evidence.json')
