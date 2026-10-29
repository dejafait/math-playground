import time
START=time.monotonic()
import ast,copy,difflib,hashlib,json,math,signal,subprocess,sys,textwrap,traceback
from pathlib import Path
sys.dont_write_bytecode=True
ROOT=Path.cwd(); BASE=ROOT/'scripts/four-rational-kernels'; OLD=BASE/'step-461'; OUT=BASE/'step-463'
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
steps=(417,419,422,424,429,431,433,435,437,440,442,446,449,451,453,455,457,459,461)
roots=[ROOT/'scripts/first-rational-kernel',ROOT/'scripts/second-rational-kernel',ROOT/'scripts/finite-derivative-coefficients']+[BASE/('step-'+str(i)) for i in (417,419,422,424,426,429,431,433,435,437,440,442,444,446,449,451,453,455,457,459,461)]+[BASE/'step-429-postmortem']
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
'drafts/2026-10-24-l112-audit-document-transition.json',
'drafts/2026-10-24-kernels-thirty-five-through-thirty-eight-document-transition.json']
selected=[
'lemmas/L113-kernels-thirty-five-through-thirty-eight-certificates.md',
'drafts/literature/2026-10-24-kernels-thirty-five-through-thirty-eight-audit.md',
'drafts/source-notes/2026-10-24-kernels-thirty-five-through-thirty-eight-audit-coverage.md',
'drafts/2026-10-24-l113-critical-audit.md',
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
def read(name): return json.loads((OLD/name).read_text())
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
    (OUT/'coordinator-source-diff.txt').write_text(''.join(difflib.unified_diff((BASE/'step-459/coordinator.py').read_text().splitlines(True),COORDINATOR.splitlines(True),fromfile='step-459/coordinator.py',tofile='step-463/coordinator.py')))
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
        if step in (446,449,451,453,455,457,459,461):
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
            elif step in (446,449,451,453,455,457,459,461):
                expected.update(original_reports_at_original_boundaries=copy.deepcopy(original_reports),failed444_frozen_separately=True,postmortem_429_preserved_as_outside_historical_cap=True)
            assert actual==expected,('whole_historical_report',step)
            original_reports[str(step)]=actual
    for step in (417,419,422,424,431,433,435,437,440,442,446,449,451,453,455,457,459,461):
        f='source-hashes.json' if step in (417,424,431,435,440,449,453,457,461) else 'fresh-source-hashes.json'
        old=json.loads((BASE/('step-'+str(step))/f).read_text())
        assert inventory([ROOT/p for p in old])==old,('whole_source_map',step)
    failed=json.loads((BASE/'step-444/terminal-report.json').read_text())
    fp=json.loads((BASE/'step-444/preservation.json').read_text())
    assert failed['status']=='STOP' and failed['child_exits']==[] and failed['completed_indices']==[]
    assert failed['preserved_inputs']==0 and failed['preservation'] is False
    assert fp['all_match'] is False and fp['original_tree_file_sets_equal'] is False
    assert not (BASE/'step-444/initial-inventory.json').exists() and not (BASE/'step-444/finalization.json').exists()
    save('historical-reconciliation.json',{'status':'PASS','inventories':reconciliation,'original_reports_at_original_boundaries':original_reports,'no_path_exemptions':True,'failed444_frozen_separately':True,'postmortem_429_preserved_as_outside_historical_cap':True})
    phase='whole_source_reconstruction'
    original_coordinator=(OLD/'coordinator.py').read_text()
    original_worker=(OLD/'worker.py').read_text()
    compile(original_coordinator,str(OLD/'coordinator.py'),'exec',flags=0,dont_inherit=True,optimize=0)
    assert (OLD/'coordinator-source-diff.txt').read_text()==''.join(difflib.unified_diff((BASE/'step-457/coordinator.py').read_text().splitlines(True),original_coordinator.splitlines(True),fromfile='step-457/coordinator.py',tofile='step-461/coordinator.py'))
    before_worker=(BASE/'step-457/worker.py').read_text(); rebuilt=before_worker
    worker_changes=[("assert INDEX in (31,32,33,34)","assert INDEX in (35,36,37,38)"),("'kernel_457_'","'kernel_461_'")]
    for a,b in worker_changes: rebuilt=exact_replace(rebuilt,a,b)
    assert rebuilt==original_worker
    compile(rebuilt,str(OLD/'worker.py'),'exec',flags=0,dont_inherit=True,optimize=0)
    assert read('worker-source-review.json')=={'changes':[{'old':a,'new':b} for a,b in worker_changes],'compile_only_before_import':True}
    assert (OLD/'worker-source-diff.txt').read_text()==''.join(difflib.unified_diff(before_worker.splitlines(True),rebuilt.splitlines(True),fromfile='step-457/worker.py',tofile='step-461/worker.py'))
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
        repl={k:[(a,b.replace('step-417','step-461')) for a,b in pairs] for k,pairs in repl.items()}
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
        identity=[index,str(fixed.resolve()),'kernel_461_'+str(index),sha((fixed/'producer.py').read_bytes()),sha((fixed/'replay.py').read_bytes())]
        for name in ('identity-before.json','identity-after-production.json','identity-after-replay.json'):
            assert json.loads((fixed/name).read_text())=={'identity':identity}
        reviews.append({'source_review':review,'all_three_original_identities':identity})
    source_map=read('source-hashes.json')
    assert set(source_map)=={str((OLD/f).relative_to(ROOT)) for f in ('coordinator.py','worker.py')}|{str((OLD/('n-'+str(i))/f).relative_to(ROOT)) for i in INDICES for f in ('producer.py','replay.py')}
    assert inventory([ROOT/p for p in source_map])==source_map
    phase='older_report_contracts'
    manifest=read('manifest.json')
    expected_manifest={'step':'BSD-2026-10-24-461-kernels-thirty-five-through-thirty-eight','indices':list(INDICES),'optimize':0,'required_seconds':180,'work_deadline_seconds':174,'required_new_bytes':LIMIT,'report_and_diagnostic_reserve':RESERVE,'panels_per_kernel':1016,'pairs_per_pass':21264880,'factor_slots':[129,65,65],'product_slots':[193,257],'scalar_terms':128,'scalar_squares':16,'grid_fractional_bits':256,'analytic_enlargement_grid':2**72,'strict_radius_powers':[183,50],'midpoint':'unchanged complete L103 record','source_generation_in_cap':True,'isolated_modules_per_child':True,'old_entrypoints_executed':False,'no_retry_or_resumption':True,'extra_signed_control_block_reused':False,'L106_values_used':False,'direct_argument_retained_whole':True,'self_slicing':False}
    assert {k:v for k,v in manifest.items() if k!='python'}==expected_manifest
    assert manifest['python'].startswith('3.15.0')
    term=read('terminal-report.json'); fin=read('finalization.json'); he=read('observed-child-exits.json'); hc=read('completed-kernels.json')
    assert set(term)=={'status','completed_indices','failure','child_exits','preserved_inputs','capture_complete','preservation','elapsed_before_terminal_seconds','inclusive_seconds','inclusive_new_bytes','required_seconds','required_new_bytes','terminal_timer_retained','path'}
    assert term=={**term,'status':'PASS','completed_indices':list(INDICES),'failure':None,'child_exits':he,'preserved_inputs':1391,'capture_complete':True,'preservation':True,'inclusive_seconds':119,'inclusive_new_bytes':12393323,'required_seconds':180,'required_new_bytes':LIMIT,'terminal_timer_retained':True,'path':str((OLD/'terminal-report.json').relative_to(ROOT))}
    prev=0
    for index,ex,st in zip(INDICES,he,hc,strict=True):
        assert set(ex)=={'n','returncode','start_seconds','observed_exit_seconds'}
        assert ex['n']==index and ex['returncode']==0 and prev<ex['start_seconds']<ex['observed_exit_seconds']<term['elapsed_before_terminal_seconds']
        prev=ex['observed_exit_seconds']; fixed=OLD/('n-'+str(index))
        assert st==json.loads((fixed/'status.json').read_text())
        assert 0<st['elapsed_seconds']<ex['observed_exit_seconds']
        k=json.loads((fixed/'kernel.json').read_text())
        assert st=={'status':'PASS','n':index,'panels':1016,'pairs_per_pass':21264880,'parameter_complete_equal':True,'ledger_equal':True,'identity_unchanged':True,'full_returned_report_persisted':True,'strict_radius_tests':[183,50],'radius':k['radius'],'elapsed_seconds':st['elapsed_seconds']}
        working=json.loads((fixed/'working.json').read_text())
        assert working=={'n':index,'stage':'replay','panels':961,'elapsed_seconds':working['elapsed_seconds']}
        assert 0<working['elapsed_seconds']<st['elapsed_seconds']
        assert json.loads((fixed/'child-stdout.txt').read_text())=={'n':index,'status':'PASS','radius':st['radius']}
        assert (fixed/'child-stderr.txt').read_bytes()==b''
    before_bytes=sum(p.stat().st_size for p in OLD.rglob('*') if p.is_file() and p.name not in ('terminal-report.json','finalization.json'))
    assert before_bytes+131072==term['inclusive_new_bytes']==12393323
    assert math.ceil(term['elapsed_before_terminal_seconds'])+3==119
    assert fin=={'elapsed_after_terminal_seconds':fin['elapsed_after_terminal_seconds'],'new_bytes_after_terminal':before_bytes+(OLD/'terminal-report.json').stat().st_size,'inclusive_seconds':119,'inclusive_new_bytes':12393323,'all_children_observed_before_terminal':True,'preservation_rechecked_after_terminal':True,'capture_complete':True,'parent_exit_time_not_claimed':True,'terminal_timer_retained':True}
    assert term['elapsed_before_terminal_seconds']<fin['elapsed_after_terminal_seconds']<119
    assert sum(p.stat().st_size for p in OLD.rglob('*') if p.is_file())+8192<=12393323
    save('full-historical-review.json',{'manifest':manifest,'source_reviews':reviews,'whole_direct_coordinator_compiled_and_hashed':True,'whole_production_worker_reconstructed':True,'fresh_compile_optimize':0,'terminal':term,'finalization':fin,'observed_exits':he,'completed':hc,'before_terminal_bytes':before_bytes,'qualification':'Historical exact parent-exit timestamp and all earlier timing qualifications remain unverified; fresh audit does not repair them.'})
    assert read('preservation.json')=={'count':1391,'files':historical[461],'mismatches':[],'capture_complete':True,'all_match':True,'tree_sets_equal':True,'fresh_sources_equal':True}
    phase='lexical_adapter'
    INSTALLER=(BASE/'step-459/installer.py').read_text()
    assert INSTALLER==(BASE/'step-437/installer.py').read_text()==(BASE/'step-433/installer.py').read_text()==(BASE/'step-422/installer.py').read_text()
    adaptations=[]
    class Sites(ast.NodeTransformer):
        def __init__(self,fn): self.fn=fn; self.changes=[]
        def visit_Constant(self,node):
            values={'scripts/four-rational-kernels/step-457':'scripts/four-rational-kernels/step-461','fixed_replay_459_':'fixed_replay_463_'}
            if isinstance(node.value,str) and node.value in values:
                self.changes.append([self.fn,node.value,values[node.value]])
                return ast.copy_location(ast.Constant(values[node.value]),node)
            return node
        def visit_Tuple(self,node):
            if len(node.elts)==4 and all(isinstance(x,ast.Constant) for x in node.elts) and [x.value for x in node.elts]==[31,32,33,34]:
                self.changes.append([self.fn,[31,32,33,34],list(INDICES)])
                return ast.copy_location(ast.Tuple(elts=[ast.Constant(x) for x in INDICES],ctx=ast.Load()),node)
            return self.generic_visit(node)
    def adapt(name):
        before=(BASE/'step-459'/name).read_text()
        compile(before,str(BASE/'step-459'/name),'exec',flags=0,dont_inherit=True,optimize=0)
        tree=ast.parse(before); changes=[]
        for node in tree.body:
            if isinstance(node,ast.FunctionDef) and node.name in ('identity_for','check_identity','preflight'):
                visitor=Sites(node.name); visitor.visit(node); changes+=visitor.changes
        expected=[['identity_for','scripts/four-rational-kernels/step-457','scripts/four-rational-kernels/step-461'],['identity_for','fixed_replay_459_','fixed_replay_463_'],['check_identity',[31,32,33,34],list(INDICES)]]
        if name=='preflight.py': expected+=[['preflight',[31,32,33,34],list(INDICES)]]
        assert changes==expected,(name,changes)
        after=ast.unparse(ast.fix_missing_locations(tree))+'\n'
        assert ast.dump(ast.parse(after),include_attributes=False)==ast.dump(tree,include_attributes=False)
        adaptations.append({'file':name,'ast_sites':changes,'entire_ast_equal':True})
        return before,after
    worker_before,WORKER=adapt('worker.py'); preflight_before,PREFLIGHT=adapt('preflight.py')
    for filename,source in [('worker.py',WORKER),('installer.py',INSTALLER),('preflight.py',PREFLIGHT)]:
        compile(source,str(OUT/filename),'exec',flags=0,dont_inherit=True,optimize=0)
        (OUT/filename).write_text(source)
        sources.update(inventory([OUT/filename]))
    assert (OUT/'installer.py').read_bytes()==(BASE/'step-459/installer.py').read_bytes()
    save('adapter-review.json',{'status':'PASS','changes':adaptations,'compile':'flags=0,dont_inherit=True,optimize=0','sentinel_and_installer_label_retained':True})
    for filename,before,after in [('worker',worker_before,WORKER),('preflight',preflight_before,PREFLIGHT)]:
        (OUT/(filename+'-diff.txt')).write_text(''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile='step-459/'+filename+'.py',tofile='step-463/'+filename+'.py')))
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
    phase='inert_preflights'
    ns={}
    exec(compile(PREFLIGHT,str(OUT/'preflight.py'),'exec',flags=0,dont_inherit=True,optimize=0),ns)
    preflight=ns['preflight'](OUT,INSTALLER)
    assert [x['n'] for x in preflight]==list(INDICES)
    save('identity-preflight.json',{'status':'PASS','indices':INDICES,'results':preflight,'all_before_any_kernel':True,'elapsed_seconds':time.monotonic()-START})
    endpoints={}
    for line in (ROOT/selected[0]).read_text().splitlines():
        if line.startswith('| ') and line.split('|')[1].strip() in ('35','36','37','38'):
            values=[int(v.strip()) for v in line.split('|')[1:-1]]
            endpoints[str(values[0])]=values[1:]
    assert set(endpoints)==set(map(str,INDICES)) and all(len(x)==3 for x in endpoints.values())
    assert [endpoints[str(i)][2] for i in INDICES]==[1020,1020,1017,1017]
    save('expected-endpoints.json',endpoints)
    sources.update(inventory([OUT/'expected-endpoints.json']))
    save('fresh-source-hashes.json',sources)
    save('audit-manifest.json',{'python':sys.version,'optimize':sys.flags.optimize,'indices':INDICES,'required_seconds':180,'work_deadline_seconds':174,'required_new_bytes':LIMIT,'report_and_diagnostic_reserve':RESERVE,'source_generation_in_cap':True,'preflights_before_any_kernel':True,'producer_executed':False,'installer_unchanged':True,'historical_entrypoints_executed':False,'direct_argument_retained_whole':True,'self_slicing':False,'no_retry_or_resumption':True})
    print(json.dumps({'stage':'static-and-four-inert-preflights','status':'PASS','elapsed_seconds':time.monotonic()-START}),flush=True)
    phase='complete_signed_replays'
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
    if failure is None: failure={'type':type(exc).__name__,'message':str(exc),'n':current,'phase':phase,'traceback':traceback.format_exc()}
finally:
    # Incomplete initial capture never establishes preservation.
    final={}; mismatch=[]; tree_ok=False; fresh_ok=False; preserved=False
    try:
        final=inventory([ROOT/p for p in initial])
        mismatch=[p for p in initial if initial[p]!=final.get(p)]
        tree_ok=capture_complete and tree_names()==names
        fresh_ok=inventory([ROOT/p for p in sources])==sources and (OUT/'coordinator.py').read_text()==COORDINATOR
        preserved=capture_complete and bool(initial) and not mismatch and tree_ok and fresh_ok
    except BaseException as exc:
        if failure is None: failure={'type':type(exc).__name__,'message':str(exc),'phase':'preservation','traceback':traceback.format_exc()}
    save('preservation.json',{'count':len(initial),'files':final,'mismatches':mismatch,'capture_complete':capture_complete,'all_match':preserved,'tree_sets_equal':tree_ok,'fresh_sources_equal':fresh_ok})
    if not preserved and failure is None: failure={'type':'PreservationFailure','message':str(mismatch)}
    if failure is not None: save('first-failure.json',failure)
    elapsed=time.monotonic()-START; sec=math.ceil(elapsed)+3; size=disk()+RESERVE
    okay=failure is None and completed==list(INDICES) and sec<=180 and size<=LIMIT and preserved
    terminal={'status':'PASS' if okay else 'STOP','completed_indices':completed,'failure':failure,'child_exits':exits,'preserved_inputs':len(initial),'capture_complete':capture_complete,'preservation':preserved,'elapsed_before_terminal_seconds':elapsed,'inclusive_seconds':sec,'inclusive_new_bytes':size,'required_seconds':180,'required_new_bytes':LIMIT,'terminal_timer_retained':True,'path':str((OUT/'terminal-report.json').relative_to(ROOT))}
    save('terminal-report.json',terminal)
    postcheck=False
    if capture_complete:
        postcheck=inventory([ROOT/p for p in initial])==initial and tree_names()==names and inventory([ROOT/p for p in sources])==sources
        assert postcheck
    assert (OUT/'coordinator.py').read_text()==COORDINATOR
    save('finalization.json',{'elapsed_after_terminal_seconds':time.monotonic()-START,'new_bytes_after_terminal':disk(),'inclusive_seconds':sec,'inclusive_new_bytes':size,'all_children_observed_before_terminal':len(exits)==4 and all(e['returncode']==0 for e in exits),'preservation_rechecked_after_terminal':postcheck,'capture_complete':capture_complete,'parent_exit_time_not_claimed':True,'terminal_timer_retained':True})
    assert time.monotonic()-START<=sec<=180 and disk()+8192<=size<=LIMIT
    print(json.dumps({'status':terminal['status'],'completed_indices':completed,'preserved_inputs':len(initial),'preservation':preserved,'inclusive_seconds':sec,'required_seconds':180,'inclusive_new_bytes':size,'required_new_bytes':LIMIT,'failure':failure,'path':terminal['path']}),flush=True)
    assert time.monotonic()-START<=sec
    sys.exit(0 if okay else 1)
