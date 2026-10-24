import time
START=time.monotonic()
import ast,copy,difflib,hashlib,json,math,signal,subprocess,sys,traceback
from pathlib import Path
sys.dont_write_bytecode=True
ROOT=Path.cwd(); BASE=ROOT/'scripts/four-rational-kernels'; OUT=BASE/'step-435'
LIMIT=134217728; RESERVE=131072; INDICES=(15,16,17,18)
initial={}; sources={}; completed=[]; exits=[]; failure=None; current=None; names={}; worker=None
def alarm(*args): raise TimeoutError('aggregate_180_second_deadline')
signal.signal(signal.SIGALRM,alarm)
signal.setitimer(signal.ITIMER_REAL,max(.001,180-(time.monotonic()-START)))
OUT.mkdir()
assert sys.orig_argv[-2]=='-c' and sys.flags.optimize==0
coordinator=sys.orig_argv[-1]
(OUT/'coordinator.py').write_text(coordinator)
roots=[ROOT/'scripts/first-rational-kernel',ROOT/'scripts/second-rational-kernel',
 ROOT/'scripts/finite-derivative-coefficients']+[BASE/('step-'+str(i)) for i in (417,419,422,424,426,429,431,433)]+[BASE/'step-429-postmortem']
transition_paths=[
'drafts/2026-10-23-four-kernel-document-transition.json',
'drafts/2026-10-23-four-kernel-audit-document-transition.json',
'drafts/2026-10-23-isolated-audit-document-transition.json',
'drafts/2026-10-23-kernels-seven-through-ten-document-transition.json',
'drafts/2026-10-23-file-launcher-stop-document-transition.json',
'drafts/2026-10-23-kernels-eleven-through-fourteen-document-transition.json',
'drafts/2026-10-23-l107-audit-document-transition.json']
selected=[
'lemmas/L031-independent-twist-five-ratio-certificate.md',
'lemmas/L101-conductor389-second-derivative-error-budget.md',
'lemmas/L102-capped-rational-taylor-kernel-enclosures.md',
'lemmas/L103-first-rational-kernel-certificate.md',
'lemmas/L104-second-rational-kernel-certificate.md',
'lemmas/L105-four-fixed-rational-kernel-certificates.md',
'lemmas/L106-kernels-seven-through-ten-certificates.md',
'lemmas/L107-kernels-eleven-through-fourteen-certificates.md',
'drafts/literature/2026-10-23-kernels-fifteen-through-eighteen.md',
'drafts/source-notes/2026-10-23-kernels-fifteen-through-eighteen-coverage.md',
'drafts/2026-10-23-kernels-fifteen-through-eighteen-attempt.md',
'ATTEMPTS/045-index-128-table-source-adaptation-stop.md',
'ATTEMPTS/046-fixed-derivative-backend-unavailable.md',
'ATTEMPTS/047-four-kernel-audit-control-index-collision.md',
'ATTEMPTS/048-kernel-audit-launcher-quotation-stop.md',
'ATTEMPTS/049-file-launcher-literal-count-stop.md']+transition_paths
def sha(raw): return hashlib.sha256(raw).hexdigest()
def inventory(paths):
    ans={}
    for p in sorted(set(paths)):
        raw=p.read_bytes(); ans[str(p.relative_to(ROOT))]={'sha256':sha(raw),'bytes':len(raw)}
    return ans
def tree_names():
    return {str(root.relative_to(ROOT)):sorted(str(p.relative_to(ROOT)) for p in root.rglob('*') if p.is_file()) for root in roots}
def disk(): return sum(p.stat().st_size for p in OUT.rglob('*') if p.is_file())
def save(name,obj):
    raw=(json.dumps(obj,sort_keys=True,separators=(',',':'))+'\n').encode()
    assert disk()+len(raw)+RESERVE<=LIMIT,'aggregate_new_byte_cap'
    (OUT/name).write_bytes(raw)
def workcheck():
    assert time.monotonic()-START<174,'aggregate_work_deadline'
    assert disk()+RESERVE<=LIMIT,'aggregate_new_byte_cap'
try:
    historical={i:json.loads((BASE/('step-'+str(i))/'initial-inventory.json').read_text()) for i in (417,419,422,424,429,431,433)}
    paths=[p for root in roots for p in root.rglob('*') if p.is_file()]+[ROOT/p for p in selected]
    paths += [ROOT/p for inv in historical.values() for p in inv]
    initial=inventory(paths); names=tree_names()
    save('initial-inventory.json',initial)
    transitions=[json.loads((ROOT/p).read_text()) for p in transition_paths]
    reconciliation={}
    for step,inv in historical.items():
        applicable=transitions[{417:0,419:1,422:2,424:3,429:4,431:5,433:6}[step]:]
        changed=[]
        for rel,value in inv.items():
            expected=value
            for transition in applicable:
                entry=transition['files'].get(rel)
                if entry is not None:
                    assert expected==entry['before'],('exact_editorial_before',step,rel)
                    expected=entry['after']
                    changed.append({'path':rel,'transition':transition['step'],'before':entry['before'],'after':entry['after']})
            assert initial[rel]==expected,('historical_input_identity',step,rel)
        preserved=json.loads((BASE/('step-'+str(step))/'preservation.json').read_text())
        assert preserved['all_match'] and preserved['files']==inv
        assert preserved['count']==len(inv) and preserved['mismatches']==[]
        reconciliation[str(step)]={'count':len(inv),'all_match':True,'exact_transitions':changed}
    for step in (417,419,422,424,431,433):
        source_file='source-hashes.json' if step in (417,424,431) else 'fresh-source-hashes.json'
        old_sources=json.loads((BASE/('step-'+str(step))/source_file).read_text())
        assert inventory([ROOT/p for p in old_sources])==old_sources
    save('historical-reconciliation.json',{'status':'PASS','inventories':reconciliation,'no_path_exemptions':True,
      'historical_timing_qualifications':'retained; no historical timer or exit claim repaired',
      'postmortem_429_preserved_as_outside_historical_cap':True})
    save('manifest.json',{'step':'BSD-2026-10-23-435-kernels-fifteen-through-eighteen','indices':INDICES,
      'python':sys.version,'optimize':sys.flags.optimize,'required_seconds':180,'work_deadline_seconds':174,
      'required_new_bytes':LIMIT,'report_and_diagnostic_reserve':RESERVE,'panels_per_kernel':1016,
      'pairs_per_pass':21264880,'factor_slots':[129,65,65],'product_slots':[193,257],
      'scalar_terms':128,'scalar_squares':16,'grid_fractional_bits':256,'analytic_enlargement_grid':2**72,
      'strict_radius_powers':[183,50],'midpoint':'unchanged complete L103 record','source_generation_in_cap':True,
      'isolated_modules_per_child':True,'old_entrypoints_executed':False,'no_retry_or_resumption':True,
      'extra_signed_control_block_reused':False,'L106_values_used':False})
    worker_before=(BASE/'step-431/worker.py').read_text()
    worker=worker_before
    worker_changes=[("assert INDEX in (11,12,13,14)","assert INDEX in (15,16,17,18)"),
      ("'kernel_431_'","'kernel_435_'")]
    for a,b in worker_changes:
        assert worker.count(a)==1,('unique_worker_adaptation',a)
        worker=worker.replace(a,b,1)
    compile(worker,str(OUT/'worker.py'),'exec',flags=0,dont_inherit=True,optimize=0)
    (OUT/'worker.py').write_text(worker)
    (OUT/'worker-source-diff.txt').write_text(''.join(difflib.unified_diff(worker_before.splitlines(True),worker.splitlines(True),fromfile='step-431/worker.py',tofile='step-435/worker.py')))
    save('worker-source-review.json',{'changes':[{'old':a,'new':b} for a,b in worker_changes],'compile_only_before_import':True})
    old_tree=ast.parse((BASE/'step-417/bootstrap.py').read_text())
    old_parent=next(ast.literal_eval(node.value) for node in old_tree.body if isinstance(node,ast.Assign)
      and any(isinstance(t,ast.Name) and t.id=='PARENT' for t in node.targets))
    nodes=[node for node in ast.walk(ast.parse(old_parent)) if isinstance(node,ast.Assign)
      and any(isinstance(t,ast.Name) and t.id=='replacements' for t in node.targets)]
    assert len(nodes)==1
    allowed=(ast.Dict,ast.List,ast.Tuple,ast.Constant,ast.JoinedStr,ast.FormattedValue,ast.Name,ast.Load,ast.BinOp,ast.Add,ast.Call)
    assert all(isinstance(x,allowed) for x in ast.walk(nodes[0].value))
    assert all(x.id in ('n','str') for x in ast.walk(nodes[0].value) if isinstance(x,ast.Name))
    assert all(isinstance(x.func,ast.Name) and x.func.id=='str' for x in ast.walk(nodes[0].value) if isinstance(x,ast.Call))
    expression=compile(ast.Expression(nodes[0].value),'retained-adaptation-data','eval',flags=0,dont_inherit=True,optimize=0)
    for index in INDICES:
        current=index; workcheck()
        dest=OUT/('n-'+str(index)); dest.mkdir()
        replacements=eval(expression,{'__builtins__':{},'str':str},{'n':index})
        replacements={name:[(a,b.replace('step-417','step-435')) for a,b in pairs] for name,pairs in replacements.items()}
        differences=[]; review={}
        for name,pairs in replacements.items():
            before=(ROOT/'scripts/second-rational-kernel/step-412'/name).read_text(); after=before
            for a,b in pairs:
                assert after.count(a)==1,('unique_exact_adaptation',index,name,a)
                after=after.replace(a,b,1)
            compile(after,str(dest/name),'exec',flags=0,dont_inherit=True,optimize=0)
            (dest/name).write_text(after)
            assert (dest/name).read_text()==after
            sources[str((dest/name).relative_to(ROOT))]={'sha256':sha(after.encode()),'bytes':len(after.encode())}
            review[name]=[{'old':a,'new':b} for a,b in pairs]
            differences.extend(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile='step-412/'+name,tofile='n-'+str(index)+'/'+name))
        (dest/'source-diff.txt').write_text(''.join(differences))
        save('n-'+str(index)+'/source-review.json',{'n':index,'unique_exact_changes':review,
          'both_scalar_and_beta_arguments_bound':True,'pre_clip_conditions_bound':True,'midpoint_not_scaled':True,
          'all_independent_arithmetic_and_full_loops_unchanged':True,'compile_optimize':0})
        workcheck(); child_start=time.monotonic()-START
        try:
            result=subprocess.run([sys.executable,'-B',str(OUT/'worker.py'),str(index),str(dest),repr(START)],
              capture_output=True,timeout=max(.001,174-(time.monotonic()-START)))
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
            failure={'type':'ChildFailure','n':index,'returncode':code,'evidence':str((dest/'first-failure.json').relative_to(ROOT))}
            break
        status=json.loads((dest/'status.json').read_text())
        returned=json.loads((dest/'returned-report.json').read_text())
        assert status['status']=='PASS' and status['n']==index and stderr==b''
        assert status['radius']==returned['radius'] and returned['status']=='PASS'
        assert json.loads(stdout)=={'n':index,'status':'PASS','radius':returned['radius']}
        completed.append(status); save('completed-kernels.json',completed)
        print(json.dumps({'n':index,'status':'PASS','observed_exit_seconds':exits[-1]['observed_exit_seconds']}),flush=True)
        workcheck()
except BaseException as exc:
    if failure is None: failure={'type':type(exc).__name__,'message':str(exc),'n':current,'traceback':traceback.format_exc()}
finally:
    final=inventory([ROOT/p for p in initial])
    mismatches=[p for p in initial if initial[p]!=final.get(p)]
    fresh_paths=[OUT/'coordinator.py']+([OUT/'worker.py'] if (OUT/'worker.py').exists() else [])+[ROOT/p for p in sources]
    fresh_ok=(OUT/'coordinator.py').read_text()==coordinator and inventory([ROOT/p for p in sources])==sources
    if (OUT/'worker.py').exists(): fresh_ok=fresh_ok and (OUT/'worker.py').read_text()==worker
    preserved=not mismatches and tree_names()==names and fresh_ok
    fresh_inventory=inventory(fresh_paths)
    save('source-hashes.json',fresh_inventory)
    save('preservation.json',{'count':len(initial),'files':final,'mismatches':mismatches,
      'original_tree_file_sets_equal':tree_names()==names,'fresh_sources_equal':fresh_ok,'all_match':preserved})
    if not preserved and failure is None: failure={'type':'PreservationFailure','message':str(mismatches)}
    if failure is not None: save('first-failure.json',failure)
    elapsed=time.monotonic()-START; sec=math.ceil(elapsed)+3; size=disk()+RESERVE
    okay=failure is None and [x['n'] for x in completed]==list(INDICES) and sec<=180 and size<=LIMIT
    terminal={'status':'PASS' if okay else 'STOP','completed_indices':[x['n'] for x in completed],
      'failure':failure,'child_exits':exits,'preserved_inputs':len(initial),'preservation':preserved,
      'elapsed_before_terminal_seconds':elapsed,'inclusive_seconds':sec,'inclusive_new_bytes':size,
      'required_seconds':180,'required_new_bytes':LIMIT,'terminal_timer_retained':True,
      'path':str((OUT/'terminal-report.json').relative_to(ROOT))}
    save('terminal-report.json',terminal)
    assert inventory([ROOT/p for p in initial])==initial and tree_names()==names
    assert inventory(fresh_paths)==fresh_inventory
    save('finalization.json',{'elapsed_after_terminal_seconds':time.monotonic()-START,
      'new_bytes_after_terminal':disk(),'inclusive_seconds':sec,'inclusive_new_bytes':size,
      'all_children_observed_before_terminal':True,'preservation_rechecked_after_terminal':True,
      'parent_exit_time_not_claimed':True,'terminal_timer_retained':True})
    assert time.monotonic()-START<=sec<=180 and disk()+8192<=size<=LIMIT
    print(json.dumps(terminal),flush=True)
    assert time.monotonic()-START<=sec
    sys.exit(0 if okay else 1)
