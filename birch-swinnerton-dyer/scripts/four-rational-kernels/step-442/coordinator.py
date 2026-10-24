import time
START=time.monotonic()
import ast,copy,difflib,hashlib,json,math,signal,subprocess,sys,textwrap,traceback
from pathlib import Path
sys.dont_write_bytecode=True
ROOT=Path.cwd(); BASE=ROOT/'scripts/four-rational-kernels'; OLD=BASE/'step-440'; OUT=BASE/'step-442'
INDICES=(19,20,21,22); LIMIT=134217728; RESERVE=131072
initial={}; sources={}; names={}; completed=[]; exits=[]; failure=None; current=None
def alarm(*args): raise TimeoutError('aggregate_180_second_deadline')
signal.signal(signal.SIGALRM,alarm)
signal.setitimer(signal.ITIMER_REAL,max(.001,180-(time.monotonic()-START)))
OUT.mkdir()
assert sys.orig_argv[-2]=='-c' and sys.flags.optimize==0
COORDINATOR=sys.orig_argv[-1]
(OUT/'coordinator.py').write_text(COORDINATOR)
roots=[ROOT/'scripts/first-rational-kernel',ROOT/'scripts/second-rational-kernel',ROOT/'scripts/finite-derivative-coefficients']+[BASE/('step-'+str(i)) for i in (417,419,422,424,426,429,431,433,435,437,440)]+[BASE/'step-429-postmortem']
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
'drafts/2026-10-24-kernels-nineteen-through-twenty-two-document-transition.json']
selected=[
'lemmas/L109-kernels-nineteen-through-twenty-two-certificates.md',
'drafts/literature/2026-10-24-kernels-nineteen-through-twenty-two-audit.md',
'drafts/source-notes/2026-10-24-kernels-nineteen-through-twenty-two-audit-coverage.md',
'drafts/2026-10-24-l109-critical-audit.md']+transition_paths
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
    assert disk()+len(raw)+RESERVE<=LIMIT
    (OUT/name).write_bytes(raw)
def read(name): return json.loads((OLD/name).read_text())
def workcheck(): assert time.monotonic()-START<174 and disk()+RESERVE<=LIMIT
def literal_assignment(source,name):
    nodes=[x for x in ast.walk(ast.parse(source)) if isinstance(x,ast.Assign) and any(isinstance(t,ast.Name) and t.id==name for t in x.targets)]
    assert len(nodes)==1,('assignment',name)
    return ast.literal_eval(nodes[0].value)
def exact_replace(source,old,new):
    assert source.count(old)==1,('unique_adapter',old)
    return source.replace(old,new,1)
try:
    steps=(417,419,422,424,429,431,433,435,437,440)
    historical={i:json.loads((BASE/('step-'+str(i))/'initial-inventory.json').read_text()) for i in steps}
    paths=[p for root in roots for p in root.rglob('*') if p.is_file()]+[ROOT/p for p in selected]+[ROOT/p for inv in historical.values() for p in inv]
    initial=inventory(paths); names=tree_names(); save('initial-inventory.json',initial)
    transitions=[json.loads((ROOT/p).read_text()) for p in transition_paths]
    reconciliation={}; old_reconciliation={}
    for step,inv in historical.items():
        changed=[]; old_changed=[]
        for rel,value in inv.items():
            expected=value
            for pos in range(steps.index(step),len(transitions)):
                if pos==len(transitions)-1 and step!=440:
                    assert historical[440][rel]==expected,('post_437_boundary',step,rel)
                transition=transitions[pos]
                entry=transition['files'].get(rel)
                if entry is not None:
                    assert expected==entry['before'],('editorial_before',step,rel)
                    expected=entry['after']
                    item={'path':rel,'transition':transition['step'],'before':entry['before'],'after':entry['after']}
                    changed.append(item)
                    if pos<len(transitions)-1: old_changed.append(item)
            assert initial[rel]==expected,('historical_identity',step,rel)
        preserved=json.loads((BASE/('step-'+str(step))/'preservation.json').read_text())
        assert preserved['all_match'] and preserved['files']==inv
        assert preserved['count']==len(inv) and preserved['mismatches']==[]
        reconciliation[str(step)]={'count':len(inv),'all_match':True,'exact_transitions':changed}
        if step!=440: old_reconciliation[str(step)]={'count':len(inv),'all_match':True,'exact_transitions':old_changed}
    assert len(historical[440])==683
    assert read('preservation.json')=={'count':683,'files':historical[440],'mismatches':[],'original_tree_file_sets_equal':True,'fresh_sources_equal':True,'all_match':True}
    assert read('historical-reconciliation.json')=={'status':'PASS','inventories':old_reconciliation,'no_path_exemptions':True,'historical_timing_qualifications':'retained; no historical timer or exit claim repaired','postmortem_429_preserved_as_outside_historical_cap':True}
    for step in (417,419,422,424,431,433,435,437,440):
        f='source-hashes.json' if step in (417,424,431,435,440) else 'fresh-source-hashes.json'
        h=json.loads((BASE/('step-'+str(step))/f).read_text())
        assert inventory([ROOT/p for p in h])==h
    save('historical-reconciliation.json',{'status':'PASS','inventories':reconciliation,'original_step440_boundary':old_reconciliation,'no_path_exemptions':True})
    # Historical entrypoints are data only; reconstruct complete worker sources.
    chain=[]
    before=(BASE/'step-424/worker.py').read_text()
    for prior_step,next_step,expected in [
        (424,431,None),
        (431,435,[("assert INDEX in (11,12,13,14)","assert INDEX in (15,16,17,18)"),("'kernel_431_'","'kernel_435_'")]),
        (435,440,[("assert INDEX in (15,16,17,18)","assert INDEX in (19,20,21,22)"),("'kernel_435_'","'kernel_440_'")])]:
        directory=BASE/('step-'+str(next_step))
        historic=(directory/'coordinator.py').read_text()
        compile(historic,str(directory/'coordinator.py'),'exec',flags=0,dont_inherit=True,optimize=0)
        changes=literal_assignment(historic,'worker_changes')
        if expected is None: assert len(changes)==5
        else: assert changes==expected
        after=before
        for a,b in changes: after=exact_replace(after,a,b)
        assert after==(directory/'worker.py').read_text()
        compile(after,str(directory/'worker.py'),'exec',flags=0,dont_inherit=True,optimize=0)
        assert json.loads((directory/'worker-source-review.json').read_text())=={'changes':[{'old':a,'new':b} for a,b in changes],'compile_only_before_import':True}
        assert (directory/'worker-source-diff.txt').read_text()==''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile='step-'+str(prior_step)+'/worker.py',tofile='step-'+str(next_step)+'/worker.py'))
        chain.append({'before':prior_step,'after':next_step,'changes':changes,'whole_source_equal':True})
        before=after
    parent417=literal_assignment((BASE/'step-417/bootstrap.py').read_text(),'PARENT')
    nodes=[x for x in ast.walk(ast.parse(parent417)) if isinstance(x,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='replacements' for t in x.targets)]
    assert len(nodes)==1
    allowed=(ast.Dict,ast.List,ast.Tuple,ast.Constant,ast.JoinedStr,ast.FormattedValue,ast.Name,ast.Load,ast.BinOp,ast.Add,ast.Call)
    assert all(isinstance(x,allowed) for x in ast.walk(nodes[0].value))
    assert all(x.id in ('n','str') for x in ast.walk(nodes[0].value) if isinstance(x,ast.Name))
    assert all(isinstance(x.func,ast.Name) and x.func.id=='str' for x in ast.walk(nodes[0].value) if isinstance(x,ast.Call))
    expression=compile(ast.Expression(nodes[0].value),'restricted-retained-adaptation','eval',flags=0,dont_inherit=True,optimize=0)
    reviews=[]
    for index in INDICES:
        fixed=OLD/('n-'+str(index))
        repl=eval(expression,{'__builtins__':{},'str':str},{'n':index})
        repl={k:[(a,b.replace('step-417','step-440')) for a,b in pairs] for k,pairs in repl.items()}
        assert set(repl)=={'producer.py','replay.py'}
        diffs=[]
        for name,pairs in repl.items():
            before=(ROOT/'scripts/second-rational-kernel/step-412'/name).read_text(); after=before
            for a,b in pairs: after=exact_replace(after,a,b)
            assert after==(fixed/name).read_text()
            compile(after,str(fixed/name),'exec',flags=0,dont_inherit=True,optimize=0)
            diffs.extend(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile='step-412/'+name,tofile='n-'+str(index)+'/'+name))
        review={'n':index,'unique_exact_changes':{k:[{'old':a,'new':b} for a,b in pairs] for k,pairs in repl.items()},'both_scalar_and_beta_arguments_bound':True,'pre_clip_conditions_bound':True,'midpoint_not_scaled':True,'all_independent_arithmetic_and_full_loops_unchanged':True,'compile_optimize':0}
        assert json.loads((fixed/'source-review.json').read_text())==review
        assert (fixed/'source-diff.txt').read_text()==''.join(diffs)
        identity=[index,str(fixed.resolve()),'kernel_440_'+str(index),sha((fixed/'producer.py').read_bytes()),sha((fixed/'replay.py').read_bytes())]
        for name in ('identity-before.json','identity-after-production.json','identity-after-replay.json'):
            assert json.loads((fixed/name).read_text())=={'identity':identity}
        reviews.append({'source_review':review,'all_three_original_identities':identity})
    source_map=read('source-hashes.json')
    assert set(source_map)=={str((OLD/f).relative_to(ROOT)) for f in ('coordinator.py','worker.py')}|{str((OLD/('n-'+str(i))/f).relative_to(ROOT)) for i in INDICES for f in ('producer.py','replay.py')}
    assert inventory([ROOT/p for p in source_map])==source_map
    manifest=read('manifest.json')
    expected_manifest={'step':'BSD-2026-10-24-440-kernels-nineteen-through-twenty-two','indices':list(INDICES),'optimize':0,'required_seconds':180,'work_deadline_seconds':174,'required_new_bytes':LIMIT,'report_and_diagnostic_reserve':RESERVE,'panels_per_kernel':1016,'pairs_per_pass':21264880,'factor_slots':[129,65,65],'product_slots':[193,257],'scalar_terms':128,'scalar_squares':16,'grid_fractional_bits':256,'analytic_enlargement_grid':2**72,'strict_radius_powers':[183,50],'midpoint':'unchanged complete L103 record','source_generation_in_cap':True,'isolated_modules_per_child':True,'old_entrypoints_executed':False,'no_retry_or_resumption':True,'extra_signed_control_block_reused':False,'L106_values_used':False}
    assert {k:v for k,v in manifest.items() if k!='python'}==expected_manifest
    assert manifest['python'].startswith('3.15.0')
    term=read('terminal-report.json'); fin=read('finalization.json'); he=read('observed-child-exits.json'); hc=read('completed-kernels.json')
    assert set(term)=={'status','completed_indices','failure','child_exits','preserved_inputs','preservation','elapsed_before_terminal_seconds','inclusive_seconds','inclusive_new_bytes','required_seconds','required_new_bytes','terminal_timer_retained','path'}
    assert term=={**term,'status':'PASS','completed_indices':list(INDICES),'failure':None,'child_exits':he,'preserved_inputs':683,'preservation':True,'inclusive_seconds':109,'inclusive_new_bytes':5779283,'required_seconds':180,'required_new_bytes':LIMIT,'terminal_timer_retained':True,'path':str((OLD/'terminal-report.json').relative_to(ROOT))}
    prev=0
    for index,ex,st in zip(INDICES,he,hc,strict=True):
        assert set(ex)=={'n','returncode','start_seconds','observed_exit_seconds'}
        assert ex['n']==index and ex['returncode']==0 and prev<ex['start_seconds']<ex['observed_exit_seconds']<term['elapsed_before_terminal_seconds']
        prev=ex['observed_exit_seconds']; fixed=OLD/('n-'+str(index))
        assert st==json.loads((fixed/'status.json').read_text())
        assert set(st)=={'status','n','panels','pairs_per_pass','parameter_complete_equal','ledger_equal','identity_unchanged','full_returned_report_persisted','strict_radius_tests','radius','elapsed_seconds'}
        assert 0<st['elapsed_seconds']<ex['observed_exit_seconds']
        k=json.loads((fixed/'kernel.json').read_text())
        assert st=={'status':'PASS','n':index,'panels':1016,'pairs_per_pass':21264880,'parameter_complete_equal':True,'ledger_equal':True,'identity_unchanged':True,'full_returned_report_persisted':True,'strict_radius_tests':[183,50],'radius':k['radius'],'elapsed_seconds':st['elapsed_seconds']}
        working=json.loads((fixed/'working.json').read_text())
        assert set(working)=={'n','stage','panels','elapsed_seconds'}
        assert working=={'n':index,'stage':'replay','panels':961,'elapsed_seconds':working['elapsed_seconds']}
        assert 0<working['elapsed_seconds']<st['elapsed_seconds']
        assert json.loads((fixed/'child-stdout.txt').read_text())=={'n':index,'status':'PASS','radius':st['radius']}
        assert (fixed/'child-stderr.txt').read_bytes()==b''
    before_bytes=sum(p.stat().st_size for p in OLD.rglob('*') if p.is_file() and p.name not in ('terminal-report.json','finalization.json'))
    assert before_bytes+RESERVE==term['inclusive_new_bytes']==5779283
    assert math.ceil(term['elapsed_before_terminal_seconds'])+3==109
    assert fin=={'elapsed_after_terminal_seconds':fin['elapsed_after_terminal_seconds'],'new_bytes_after_terminal':before_bytes+(OLD/'terminal-report.json').stat().st_size,'inclusive_seconds':109,'inclusive_new_bytes':5779283,'all_children_observed_before_terminal':True,'preservation_rechecked_after_terminal':True,'parent_exit_time_not_claimed':True,'terminal_timer_retained':True}
    assert term['elapsed_before_terminal_seconds']<fin['elapsed_after_terminal_seconds']<109
    assert sum(p.stat().st_size for p in OLD.rglob('*') if p.is_file())+8192<=5779283
    save('full-historical-review.json',{'manifest':manifest,'source_reviews':reviews,'worker_chain':chain,'terminal':term,'finalization':fin,'observed_exits':he,'completed':hc,'before_terminal_bytes':before_bytes,'qualification':'Historical exact parent-exit timestamp and all earlier timing qualifications remain unverified; fresh audit does not repair them.'})
    INSTALLER=(BASE/'step-437/installer.py').read_text()
    assert INSTALLER==(BASE/'step-433/installer.py').read_text()==(BASE/'step-422/installer.py').read_text()
    adaptations=[]
    class Sites(ast.NodeTransformer):
        def __init__(self,fn): self.fn=fn; self.changes=[]
        def visit_Constant(self,node):
            values={'scripts/four-rational-kernels/step-435':'scripts/four-rational-kernels/step-440','fixed_replay_437_':'fixed_replay_442_'}
            if isinstance(node.value,str) and node.value in values:
                self.changes.append([self.fn,node.value,values[node.value]])
                return ast.copy_location(ast.Constant(values[node.value]),node)
            return node
        def visit_Tuple(self,node):
            if len(node.elts)==4 and all(isinstance(x,ast.Constant) for x in node.elts) and [x.value for x in node.elts]==[15,16,17,18]:
                self.changes.append([self.fn,[15,16,17,18],list(INDICES)])
                return ast.copy_location(ast.Tuple(elts=[ast.Constant(x) for x in INDICES],ctx=ast.Load()),node)
            return self.generic_visit(node)
    def adapt(name):
        before=(BASE/'step-437'/name).read_text()
        compile(before,str(BASE/'step-437'/name),'exec',flags=0,dont_inherit=True,optimize=0)
        tree=ast.parse(before); changes=[]
        for node in tree.body:
            if isinstance(node,ast.FunctionDef) and node.name in ('identity_for','check_identity','preflight'):
                visitor=Sites(node.name); visitor.visit(node); changes+=visitor.changes
        expected=[['identity_for','scripts/four-rational-kernels/step-435','scripts/four-rational-kernels/step-440'],['identity_for','fixed_replay_437_','fixed_replay_442_'],['check_identity',[15,16,17,18],list(INDICES)]]
        if name=='preflight.py': expected+=[['preflight',[15,16,17,18],list(INDICES)]]
        assert changes==expected,(name,changes)
        after=ast.unparse(ast.fix_missing_locations(tree))+'\n'
        adaptations.append({'file':name,'ast_sites':changes})
        return before,after
    worker_before,WORKER=adapt('worker.py'); preflight_before,PREFLIGHT=adapt('preflight.py')
    for filename,source in [('worker.py',WORKER),('installer.py',INSTALLER),('preflight.py',PREFLIGHT)]:
        compile(source,str(OUT/filename),'exec',flags=0,dont_inherit=True,optimize=0)
        (OUT/filename).write_text(source)
    assert (OUT/'installer.py').read_bytes()==(BASE/'step-437/installer.py').read_bytes()==(BASE/'step-433/installer.py').read_bytes()==(BASE/'step-422/installer.py').read_bytes()
    save('adapter-review.json',{'status':'PASS','changes':adaptations,'compile':'flags=0,dont_inherit=True,optimize=0','sentinel_and_installer_label_retained':True})
    for filename,before,after in [('worker',worker_before,WORKER),('preflight',preflight_before,PREFLIGHT)]:
        (OUT/(filename+'-diff.txt')).write_text(''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile='step-437/'+filename+'.py',tofile='step-442/'+filename+'.py')))
    retained=(BASE/'step-419/signed-checks.py').read_text()
    comparison=(ROOT/'scripts/second-rational-kernel/step-415/audit-body.py').read_text()
    left='    old_floor,old_ceil=replay.floor_checked,replay.ceil_checked\n'; right="    parameter=read('parameter.json')\n"
    assert comparison.count(left)==comparison.count(right)==1
    assert textwrap.dedent(comparison[comparison.index(left):comparison.index(right)])==retained
    parsed=ast.parse(INSTALLER); assert len(parsed.body)==1 and isinstance(parsed.body[0],ast.FunctionDef)
    fn=parsed.body[0]
    assert fn.name=='install' and [x.arg for x in fn.args.args]==['replay','D','signed','save']
    assert not fn.args.defaults and not fn.decorator_list and fn.returns is None
    assert all(arg.annotation is None for arg in fn.args.args)
    assert ast.dump(ast.Module(body=fn.body[:-1],type_ignores=[]),include_attributes=False)==ast.dump(ast.parse(retained),include_attributes=False)
    assert isinstance(fn.body[-1],ast.Return)
    assert not any(isinstance(x,(ast.Global,ast.Nonlocal,ast.Import,ast.ImportFrom)) for x in ast.walk(fn))
    assert not {'OUT','OLD','START','IDENTITY','globals','locals','exec','eval','compile','__import__'} & {x.id for x in ast.walk(fn) if isinstance(x,ast.Name)}
    for node in ast.walk(fn):
        if isinstance(node,ast.FunctionDef):
            assert not node.decorator_list and node.returns is None and all(x.annotation is None for x in node.args.args)
            assert all(isinstance(x,ast.Constant) and x.value==1 for x in node.args.defaults)
    calls=sorted({ast.unparse(x.func) for x in ast.walk(fn) if isinstance(x,ast.Call)})
    assert set(calls)=={'old_floor','old_ceil','old_times','old_over','old_enc','old_plus','old_neg','old_clip','old_product','min','max','len','all','setattr','times','floor_checked','ceil_checked','save','replay.LEDGER.get','replay.LEDGER.clear'}
    worker_ast=ast.parse(WORKER)
    sites=[x for x in ast.walk(worker_ast) if isinstance(x,ast.Name) and x.id=='IDENTITY' and isinstance(x.ctx,ast.Store)]
    assert len(sites)==1
    assert not any(isinstance(x,ast.Subscript) and isinstance(x.ctx,ast.Store) and isinstance(x.value,ast.Name) and x.value.id=='IDENTITY' for x in ast.walk(worker_ast))
    assert not any(isinstance(x,ast.Name) and x.id=='n' for x in ast.walk(worker_ast))
    save('static-binding-review.json',{'status':'PASS','installer_body_exact':True,'identity_binding_sites':1,'calls':calls,'installer_sha256':sha(INSTALLER.encode()),'worker_sha256':sha(WORKER.encode()),'preflight_sha256':sha(PREFLIGHT.encode())})
    ns={}
    exec(compile(PREFLIGHT,str(OUT/'preflight.py'),'exec',flags=0,dont_inherit=True,optimize=0),ns)
    preflight=ns['preflight'](OUT,INSTALLER)
    assert [x['n'] for x in preflight]==list(INDICES)
    save('identity-preflight.json',{'status':'PASS','indices':INDICES,'results':preflight,'all_before_any_kernel':True,'elapsed_seconds':time.monotonic()-START})
    endpoints={}
    for line in (ROOT/selected[0]).read_text().splitlines():
        if line.startswith('| ') and line.split('|')[1].strip() in ('19','20','21','22'):
            values=[int(v.strip()) for v in line.split('|')[1:-1]]; endpoints[str(values[0])]=values[1:]
    assert set(endpoints)==set(map(str,INDICES)) and all(len(x)==2 for x in endpoints.values())
    for i,w in zip(INDICES,(1389,1270,1186,1130),strict=True): endpoints[str(i)].append(w)
    save('expected-endpoints.json',endpoints)
    sources=inventory([OUT/f for f in ('coordinator.py','worker.py','installer.py','preflight.py','expected-endpoints.json')])
    save('fresh-source-hashes.json',sources)
    save('audit-manifest.json',{'python':sys.version,'optimize':sys.flags.optimize,'indices':INDICES,'required_seconds':180,'required_new_bytes':LIMIT,'source_generation_in_cap':True,'preflights_before_any_kernel':True,'producer_executed':False,'L106_values_used':False,'installer_unchanged':True,'no_retry_or_resumption':True})
    print(json.dumps({'stage':'static-and-four-inert-preflights','status':'PASS','elapsed_seconds':time.monotonic()-START}),flush=True)
    for index in INDICES:
        current=index; workcheck(); dest=OUT/('n-'+str(index)); dest.mkdir(); t=time.monotonic()-START
        try:
            result=subprocess.run([sys.executable,'-B',str(OUT/'worker.py'),str(index),str(dest),repr(START)],capture_output=True,timeout=max(.001,174-(time.monotonic()-START)))
            stdout,stderr,code=result.stdout,result.stderr,result.returncode
        except subprocess.TimeoutExpired as exc:
            stdout,stderr,code=exc.stdout or b'',exc.stderr or b'',None
            failure={'type':'ChildTimeout','n':index,'message':'child killed and waited; no retry'}
        assert len(stdout)+len(stderr)<=8192
        (dest/'child-stdout.txt').write_bytes(stdout); (dest/'child-stderr.txt').write_bytes(stderr)
        exits.append({'n':index,'returncode':code,'start_seconds':t,'observed_exit_seconds':time.monotonic()-START})
        save('observed-child-exits.json',exits)
        if failure is not None: break
        if code!=0:
            failure={'type':'ChildFailure','n':index,'returncode':code,'evidence':str((dest/'first-failure.json').relative_to(ROOT))}; break
        status=json.loads((dest/'status.json').read_text())
        assert status=={'status':'PASS','state':{'n':index,'stage':'complete','panels':1016},'elapsed_seconds':status['elapsed_seconds']}
        assert stderr==b'' and status['elapsed_seconds']<exits[-1]['observed_exit_seconds']
        assert json.loads(stdout)=={'n':index,'status':'PASS','panels':1016,'coefficient_pairs':21264880,'strict_radius_powers':[183,50]}
        completed.append(index); save('completed-indices.json',completed)
        print(json.dumps({'n':index,'status':'PASS','observed_exit_seconds':exits[-1]['observed_exit_seconds']}),flush=True)
        workcheck()
except BaseException as exc:
    if failure is None: failure={'type':type(exc).__name__,'message':str(exc),'n':current,'traceback':traceback.format_exc()}
finally:
    final=inventory([ROOT/p for p in initial])
    mismatch=[p for p in initial if initial[p]!=final.get(p)]
    preserved=not mismatch and tree_names()==names and inventory([ROOT/p for p in sources])==sources
    save('preservation.json',{'count':len(initial),'files':final,'mismatches':mismatch,'all_match':preserved,'tree_sets_equal':tree_names()==names,'fresh_sources_equal':inventory([ROOT/p for p in sources])==sources})
    if not preserved and failure is None: failure={'type':'PreservationFailure','message':str(mismatch)}
    if failure is not None: save('first-failure.json',failure)
    elapsed=time.monotonic()-START; sec=math.ceil(elapsed)+3; size=disk()+RESERVE
    okay=failure is None and completed==list(INDICES) and sec<=180 and size<=LIMIT
    terminal={'status':'PASS' if okay else 'STOP','completed_indices':completed,'failure':failure,'child_exits':exits,'preserved_inputs':len(initial),'preservation':preserved,'elapsed_before_terminal_seconds':elapsed,'inclusive_seconds':sec,'inclusive_new_bytes':size,'required_seconds':180,'required_new_bytes':LIMIT,'terminal_timer_retained':True,'path':str((OUT/'terminal-report.json').relative_to(ROOT))}
    save('terminal-report.json',terminal)
    assert inventory([ROOT/p for p in initial])==initial and tree_names()==names and inventory([ROOT/p for p in sources])==sources
    assert (OUT/'coordinator.py').read_text()==COORDINATOR
    save('finalization.json',{'elapsed_after_terminal_seconds':time.monotonic()-START,'new_bytes_after_terminal':disk(),'inclusive_seconds':sec,'inclusive_new_bytes':size,'all_children_observed_before_terminal':True,'preservation_rechecked_after_terminal':True,'parent_exit_time_not_claimed':True,'terminal_timer_retained':True})
    assert time.monotonic()-START<=sec<=180 and disk()+8192<=size<=LIMIT
    print(json.dumps(terminal),flush=True)
    assert time.monotonic()-START<=sec
    sys.exit(0 if okay else 1)
