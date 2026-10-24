import time
START=time.monotonic()
import ast,copy,difflib,hashlib,json,math,signal,subprocess,sys,traceback
from pathlib import Path
sys.dont_write_bytecode=True
ROOT=Path.cwd(); BASE=ROOT/'scripts/four-rational-kernels'; OUT=BASE/'step-461'
INDICES=(35,36,37,38); LIMIT=134217728; RESERVE=131072
initial={}; sources={}; names={}; completed=[]; exits=[]; failure=None; current=None
capture_complete=False; phase='setup'
def alarm(*args): raise TimeoutError('aggregate_180_second_deadline')
signal.signal(signal.SIGALRM,alarm)
signal.setitimer(signal.ITIMER_REAL,max(.001,180-(time.monotonic()-START)))
OUT.mkdir()
assert sys.orig_argv[-2]=='-c' and sys.flags.optimize==0
COORDINATOR=sys.orig_argv[-1]
(OUT/'coordinator.py').write_text(COORDINATOR)
steps=(417,419,422,424,429,431,433,435,437,440,442,446,449,451,453,455,457,459)
roots=[ROOT/'scripts/first-rational-kernel',ROOT/'scripts/second-rational-kernel',ROOT/'scripts/finite-derivative-coefficients']+[BASE/('step-'+str(i)) for i in (417,419,422,424,426,429,431,433,435,437,440,442,444,446,449,451,453,455,457,459)]+[BASE/'step-429-postmortem']
transition_paths=[
'drafts/2026-10-23-four-kernel-document-transition.json',
'drafts/2026-10-23-four-kernel-audit-document-transition.json',
'drafts/2026-10-23-isolated-audit-document-transition.json',
'drafts/2026-10-23-kernels-seven-through-ten-document-transition.json',
'drafts/2026-10-23-file-launcher-stop-document-transition.json',
'drafts/2026-10-23-kernels-eleven-through-fourteen-document-transition.json',
'drafts/2026-10-23-l107-audit-document-transition.json',
'drafts/2026-10-23-kernels-fifteen-through-eighteen-document-transition.json',
'drafts/2026-10-24-l108-audit-document-transition.json',
'drafts/2026-10-24-kernels-nineteen-through-twenty-two-document-transition.json',
'drafts/2026-10-24-l109-audit-document-transition.json',
'drafts/2026-10-24-l106-audit-document-transition.json',
'drafts/2026-10-24-direct-kernels-twenty-three-through-twenty-six-document-transition.json',
'drafts/2026-10-24-l110-audit-document-transition.json',
'drafts/2026-10-24-kernels-twenty-seven-through-thirty-document-transition.json',
'drafts/2026-10-24-l111-audit-document-transition.json',
'drafts/2026-10-24-kernels-thirty-one-through-thirty-four-document-transition.json',
'drafts/2026-10-24-l112-audit-document-transition.json']
selected=[
'lemmas/L112-kernels-thirty-one-through-thirty-four-certificates.md',
'lemmas/L031-independent-twist-five-ratio-certificate.md',
'lemmas/L101-conductor389-second-derivative-error-budget.md',
'lemmas/L102-capped-rational-taylor-kernel-enclosures.md',
'lemmas/L103-first-rational-kernel-certificate.md',
'drafts/literature/2026-10-24-kernels-thirty-five-through-thirty-eight.md',
'drafts/source-notes/2026-10-24-kernels-thirty-five-through-thirty-eight-coverage.md',
'drafts/2026-10-24-kernels-thirty-five-through-thirty-eight-attempt.md',
'ATTEMPTS/045-index-128-table-source-adaptation-stop.md',
'ATTEMPTS/046-fixed-derivative-backend-unavailable.md',
'ATTEMPTS/047-four-kernel-audit-control-index-collision.md',
'ATTEMPTS/048-kernel-audit-launcher-quotation-stop.md',
'ATTEMPTS/049-file-launcher-literal-count-stop.md',
'ATTEMPTS/050-kernel-coordinator-self-delimiter-stop.md']+transition_paths
def sha(raw): return hashlib.sha256(raw).hexdigest()
def inventory(paths):
    ans={}
    for p in sorted(set(paths)):
        raw=p.read_bytes(); ans[str(p.relative_to(ROOT))]={'sha256':sha(raw),'bytes':len(raw)}
    return ans
def tree_names(): return {str(r.relative_to(ROOT)):sorted(str(p.relative_to(ROOT)) for p in r.rglob('*') if p.is_file()) for r in roots}
def disk(): return sum(p.stat().st_size for p in OUT.rglob('*') if p.is_file())
def save(name,obj):
    raw=(json.dumps(obj,sort_keys=True,separators=(',',':'))+'\n').encode()
    assert disk()+len(raw)+RESERVE<=LIMIT,'aggregate_new_byte_cap'
    (OUT/name).write_bytes(raw)
def workcheck(): assert time.monotonic()-START<174 and disk()+RESERVE<=LIMIT
def literal_assignment(source,name):
    nodes=[x for x in ast.parse(source).body if isinstance(x,ast.Assign) and any(isinstance(t,ast.Name) and t.id==name for t in x.targets)]
    assert len(nodes)==1,('unique_top_level_assignment',name)
    return ast.literal_eval(nodes[0].value)
def exact_replace(source,old,new):
    assert source.count(old)==1,('unique_adapter',old)
    return source.replace(old,new,1)
sources=inventory([OUT/'coordinator.py'])
try:
    compile(COORDINATOR,str(OUT/'coordinator.py'),'exec',flags=0,dont_inherit=True,optimize=0)
    phase='initial_capture'
    historical={i:json.loads((BASE/('step-'+str(i))/'initial-inventory.json').read_text()) for i in steps}
    paths=[p for r in roots for p in r.rglob('*') if p.is_file()]+[ROOT/p for p in selected]+[ROOT/p for inv in historical.values() for p in inv]
    initial=inventory(paths); names=tree_names()
    save('initial-inventory.json',initial); capture_complete=True
    transitions=[json.loads((ROOT/p).read_text()) for p in transition_paths]
    assert len(transitions)==len(steps)
    def reconcile(stop):
        result={}
        for pos,step in enumerate(steps[:stop]):
            inv=historical[step]; changed=[]
            for rel,value in inv.items():
                expected=value
                for transition in transitions[pos:stop]:
                    entry=transition['files'].get(rel)
                    if entry is not None:
                        assert expected==entry['before'],('editorial_before',step,rel,transition['step'])
                        expected=entry['after']
                        changed.append({'path':rel,'transition':transition['step'],'before':entry['before'],'after':entry['after']})
                boundary=initial if stop==len(steps) else historical[steps[stop]]
                assert boundary[rel]==expected,('historical_boundary',step,stop,rel)
            result[str(step)]={'count':len(inv),'all_match':True,'exact_transitions':changed}
        return result
    phase='historical_boundaries'
    reconciliation=reconcile(len(steps))
    boundaries={str(step):reconcile(pos) for pos,step in enumerate(steps) if step>=424}
    original_reports={}
    for step in steps:
        inv=historical[step]
        preserved=json.loads((BASE/('step-'+str(step))/'preservation.json').read_text())
        assert preserved['all_match'] and preserved['files']==inv
        assert preserved['count']==len(inv) and preserved['mismatches']==[]
        if step in (446,449,451,453,455,457,459):
            assert preserved['capture_complete'] and preserved['tree_sets_equal'] and preserved['fresh_sources_equal']
        if step>=424:
            actual=json.loads((BASE/('step-'+str(step))/'historical-reconciliation.json').read_text())
            rows=copy.deepcopy(boundaries[str(step)])
            expected={'status':'PASS','inventories':rows,'no_path_exemptions':True}
            if step==424:
                expected['historical_timing_qualifications']='retained; no old timer or parent-exit claim repaired'
            elif step==429:
                for earlier,row in rows.items():
                    f='source-hashes.json' if int(earlier) in (417,424) else 'fresh-source-hashes.json'
                    row['source_hashes']=json.loads((BASE/('step-'+earlier)/f).read_text())
                    assert inventory([ROOT/p for p in row['source_hashes']])==row['source_hashes']
            elif step in (431,435,440):
                expected.update(historical_timing_qualifications='retained; no historical timer or exit claim repaired',postmortem_429_preserved_as_outside_historical_cap=True)
            elif step==442:
                expected['original_step440_boundary']=boundaries['440']
            elif step in (446,449,451,453,455,457,459):
                expected.update(original_reports_at_original_boundaries=copy.deepcopy(original_reports),failed444_frozen_separately=True,postmortem_429_preserved_as_outside_historical_cap=True)
            assert actual==expected,('whole_historical_report',step)
            original_reports[str(step)]=actual
    for step in (417,419,422,424,431,433,435,437,440,442,446,449,451,453,455,457,459):
        f='source-hashes.json' if step in (417,424,431,435,440,449,453,457) else 'fresh-source-hashes.json'
        old=json.loads((BASE/('step-'+str(step))/f).read_text())
        assert inventory([ROOT/p for p in old])==old,('whole_source_map',step)
    failed=json.loads((BASE/'step-444/terminal-report.json').read_text())
    fp=json.loads((BASE/'step-444/preservation.json').read_text())
    assert failed['status']=='STOP' and failed['child_exits']==[] and failed['completed_indices']==[]
    assert failed['preserved_inputs']==0 and failed['preservation'] is False
    assert fp['all_match'] is False and fp['original_tree_file_sets_equal'] is False
    assert not (BASE/'step-444/initial-inventory.json').exists() and not (BASE/'step-444/finalization.json').exists()
    save('historical-reconciliation.json',{'status':'PASS','inventories':reconciliation,'original_reports_at_original_boundaries':original_reports,'no_path_exemptions':True,'failed444_frozen_separately':True,'postmortem_429_preserved_as_outside_historical_cap':True})
    phase='production_source_construction'
    (OUT/'coordinator-source-diff.txt').write_text(''.join(difflib.unified_diff((BASE/'step-457/coordinator.py').read_text().splitlines(True),COORDINATOR.splitlines(True),fromfile='step-457/coordinator.py',tofile='step-461/coordinator.py')))
    save('manifest.json',{'step':'BSD-2026-10-24-461-kernels-thirty-five-through-thirty-eight','indices':INDICES,
      'python':sys.version,'optimize':sys.flags.optimize,'required_seconds':180,'work_deadline_seconds':174,
      'required_new_bytes':LIMIT,'report_and_diagnostic_reserve':RESERVE,'panels_per_kernel':1016,
      'pairs_per_pass':21264880,'factor_slots':[129,65,65],'product_slots':[193,257],
      'scalar_terms':128,'scalar_squares':16,'grid_fractional_bits':256,'analytic_enlargement_grid':2**72,
      'strict_radius_powers':[183,50],'midpoint':'unchanged complete L103 record','source_generation_in_cap':True,
      'isolated_modules_per_child':True,'old_entrypoints_executed':False,'no_retry_or_resumption':True,
      'extra_signed_control_block_reused':False,'L106_values_used':False,'direct_argument_retained_whole':True,'self_slicing':False})
    worker_before=(BASE/'step-457/worker.py').read_text(); worker=worker_before
    worker_changes=[("assert INDEX in (31,32,33,34)","assert INDEX in (35,36,37,38)"),("'kernel_457_'","'kernel_461_'")]
    for a,b in worker_changes: worker=exact_replace(worker,a,b)
    compile(worker,str(OUT/'worker.py'),'exec',flags=0,dont_inherit=True,optimize=0)
    (OUT/'worker.py').write_text(worker)
    sources.update(inventory([OUT/'worker.py']))
    (OUT/'worker-source-diff.txt').write_text(''.join(difflib.unified_diff(worker_before.splitlines(True),worker.splitlines(True),fromfile='step-457/worker.py',tofile='step-461/worker.py')))
    save('worker-source-review.json',{'changes':[{'old':a,'new':b} for a,b in worker_changes],'compile_only_before_import':True})
    parent417=literal_assignment((BASE/'step-417/bootstrap.py').read_text(),'PARENT')
    nodes=[x for x in ast.walk(ast.parse(parent417)) if isinstance(x,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='replacements' for t in x.targets)]
    assert len(nodes)==1
    allowed=(ast.Dict,ast.List,ast.Tuple,ast.Constant,ast.JoinedStr,ast.FormattedValue,ast.Name,ast.Load,ast.BinOp,ast.Add,ast.Call)
    assert all(isinstance(x,allowed) for x in ast.walk(nodes[0].value))
    assert all(x.id in ('n','str') for x in ast.walk(nodes[0].value) if isinstance(x,ast.Name))
    assert all(isinstance(x.func,ast.Name) and x.func.id=='str' for x in ast.walk(nodes[0].value) if isinstance(x,ast.Call))
    expression=compile(ast.Expression(nodes[0].value),'restricted-retained-adaptation','eval',flags=0,dont_inherit=True,optimize=0)
    for index in INDICES:
        current=index; phase='kernel_'+str(index); workcheck()
        dest=OUT/('n-'+str(index)); dest.mkdir()
        repl=eval(expression,{'__builtins__':{},'str':str},{'n':index})
        repl={k:[(a,b.replace('step-417','step-461')) for a,b in pairs] for k,pairs in repl.items()}
        assert set(repl)=={'producer.py','replay.py'}
        differences=[]; review={}
        for name,pairs in repl.items():
            before=(ROOT/'scripts/second-rational-kernel/step-412'/name).read_text(); after=before
            compile(before,'whole-step412-'+name,'exec',flags=0,dont_inherit=True,optimize=0)
            for a,b in pairs: after=exact_replace(after,a,b)
            compile(after,str(dest/name),'exec',flags=0,dont_inherit=True,optimize=0)
            (dest/name).write_text(after)
            assert (dest/name).read_text()==after
            sources.update(inventory([dest/name]))
            review[name]=[{'old':a,'new':b} for a,b in pairs]
            differences.extend(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile='step-412/'+name,tofile='n-'+str(index)+'/'+name))
        (dest/'source-diff.txt').write_text(''.join(differences))
        save('n-'+str(index)+'/source-review.json',{'n':index,'unique_exact_changes':review,'both_scalar_and_beta_arguments_bound':True,'pre_clip_conditions_bound':True,'midpoint_not_scaled':True,'all_independent_arithmetic_and_full_loops_unchanged':True,'compile_optimize':0})
        save('source-hashes.json',sources)
        workcheck(); child_start=time.monotonic()-START
        try:
            result=subprocess.run([sys.executable,'-B',str(OUT/'worker.py'),str(index),str(dest),repr(START)],capture_output=True,timeout=max(.001,174-(time.monotonic()-START)))
            stdout,stderr,code=result.stdout,result.stderr,result.returncode
        except subprocess.TimeoutExpired as exc:
            stdout,stderr,code=exc.stdout or b'',exc.stderr or b'',None
            failure={'type':'ChildTimeout','n':index,'message':'child killed and waited; no retry'}
        assert len(stdout)+len(stderr)<=8192
        (dest/'child-stdout.txt').write_bytes(stdout); (dest/'child-stderr.txt').write_bytes(stderr)
        exits.append({'n':index,'returncode':code,'start_seconds':child_start,'observed_exit_seconds':time.monotonic()-START})
        save('observed-child-exits.json',exits)
        if failure is not None: break
        if code!=0:
            failure={'type':'ChildFailure','n':index,'returncode':code,'evidence':str((dest/'first-failure.json').relative_to(ROOT))}; break
        status=json.loads((dest/'status.json').read_text()); returned=json.loads((dest/'returned-report.json').read_text())
        assert status['status']=='PASS' and status['n']==index and stderr==b''
        assert status['elapsed_seconds']<exits[-1]['observed_exit_seconds']
        assert status['radius']==returned['radius'] and returned['status']=='PASS'
        assert json.loads(stdout)=={'n':index,'status':'PASS','radius':returned['radius']}
        completed.append(status); save('completed-kernels.json',completed)
        print(json.dumps({'n':index,'status':'PASS','observed_exit_seconds':exits[-1]['observed_exit_seconds']}),flush=True)
        workcheck()
except BaseException as exc:
    if failure is None: failure={'type':type(exc).__name__,'message':str(exc),'n':current,'phase':phase,'traceback':traceback.format_exc()}
finally:
    final={}; mismatch=[]; tree_ok=False; fresh_ok=False; preserved=False
    try:
        final=inventory([ROOT/p for p in initial])
        mismatch=[p for p in initial if initial[p]!=final.get(p)]
        tree_ok=capture_complete and tree_names()==names
        fresh_ok=inventory([ROOT/p for p in sources])==sources and (OUT/'coordinator.py').read_text()==COORDINATOR
        preserved=capture_complete and bool(initial) and not mismatch and tree_ok and fresh_ok
    except BaseException as exc:
        if failure is None: failure={'type':type(exc).__name__,'message':str(exc),'phase':'preservation','traceback':traceback.format_exc()}
    save('source-hashes.json',sources)
    save('preservation.json',{'count':len(initial),'files':final,'mismatches':mismatch,'capture_complete':capture_complete,'all_match':preserved,'tree_sets_equal':tree_ok,'fresh_sources_equal':fresh_ok})
    if not preserved and failure is None: failure={'type':'PreservationFailure','message':str(mismatch)}
    if failure is not None: save('first-failure.json',failure)
    elapsed=time.monotonic()-START; sec=math.ceil(elapsed)+3; size=disk()+RESERVE
    done=[x['n'] for x in completed]
    okay=failure is None and done==list(INDICES) and len(exits)==4 and all(e['returncode']==0 for e in exits) and sec<=180 and size<=LIMIT and preserved
    terminal={'status':'PASS' if okay else 'STOP','completed_indices':done,'failure':failure,'child_exits':exits,'preserved_inputs':len(initial),'capture_complete':capture_complete,'preservation':preserved,'elapsed_before_terminal_seconds':elapsed,'inclusive_seconds':sec,'inclusive_new_bytes':size,'required_seconds':180,'required_new_bytes':LIMIT,'terminal_timer_retained':True,'path':str((OUT/'terminal-report.json').relative_to(ROOT))}
    save('terminal-report.json',terminal)
    postcheck=False
    if capture_complete:
        postcheck=inventory([ROOT/p for p in initial])==initial and tree_names()==names and inventory([ROOT/p for p in sources])==sources
        assert postcheck
    assert (OUT/'coordinator.py').read_text()==COORDINATOR
    save('finalization.json',{'elapsed_after_terminal_seconds':time.monotonic()-START,'new_bytes_after_terminal':disk(),'inclusive_seconds':sec,'inclusive_new_bytes':size,'all_children_observed_before_terminal':len(exits)==4 and all(e['returncode']==0 for e in exits),'preservation_rechecked_after_terminal':postcheck,'capture_complete':capture_complete,'parent_exit_time_not_claimed':True,'terminal_timer_retained':True})
    assert time.monotonic()-START<=sec<=180 and disk()+8192<=size<=LIMIT
    print(json.dumps({'status':terminal['status'],'completed_indices':done,'preserved_inputs':len(initial),'preservation':preserved,'inclusive_seconds':sec,'required_seconds':180,'inclusive_new_bytes':size,'required_new_bytes':LIMIT,'failure':failure,'path':terminal['path']}),flush=True)
    assert time.monotonic()-START<=sec
    sys.exit(0 if okay else 1)
