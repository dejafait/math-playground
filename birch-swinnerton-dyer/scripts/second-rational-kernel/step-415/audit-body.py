
import ast, difflib, hashlib, importlib.util, json, math, signal, sys, time, traceback
from pathlib import Path
from fractions import Fraction
sys.dont_write_bytecode = True
ROOT = Path.cwd()
OLD = ROOT/'scripts/second-rational-kernel/step-412'
OUT = ROOT/'scripts/second-rational-kernel/step-415'
LIMIT = 134217728
STATE = {'stage':'setup','panels':0,'n':2}
initial = {}
report = None
failure = None
signed = {k:0 for k in ('floor','ceiling','multiply','divide','convert','plus','negate','clip','products','zero_operand_multiplications')}
signed['sign_cases'] = [0]*9
def alarm(*args): raise TimeoutError('aggregate_deadline')
signal.signal(signal.SIGALRM,alarm)
signal.setitimer(signal.ITIMER_REAL,max(.001,174-(time.monotonic()-START)))
def digest(raw): return hashlib.sha256(raw).hexdigest()
def disk(): return sum(p.stat().st_size for p in OUT.rglob('*') if p.is_file())
def save(name,obj):
    raw = (json.dumps(obj,sort_keys=True,separators=(',',':'))+'\n').encode()
    assert disk()+len(raw)+73728 < LIMIT, 'byte_cap'
    (OUT/name).write_bytes(raw)
def inventory(paths):
    result = {}
    for p in sorted(set(paths)):
        raw = p.read_bytes()
        result[str(p.relative_to(ROOT))] = {'sha256':digest(raw),'bytes':len(raw)}
    return result
def read(name): return json.loads((OLD/name).read_text())
def progress(stage,panels):
    STATE.update(stage=stage,panels=panels)
    assert time.monotonic()-START < 174
    save('working.json',{**STATE,'elapsed_seconds':time.monotonic()-START})
    if panels % 256 == 1: print(json.dumps(STATE),flush=True)
try:
    original = read('initial-inventory.json')
    assert len(original) == 62
    fixed_paths = [p for p in OLD.rglob('*') if p.is_file()]
    fixed_names = {str(p.relative_to(ROOT)) for p in fixed_paths}
    extras = ['lemmas/L104-second-rational-kernel-certificate.md',
        'drafts/literature/2026-10-23-second-rational-kernel-audit.md',
        'drafts/source-notes/2026-10-23-second-rational-kernel-audit-coverage.md']
    initial = inventory(fixed_paths+[ROOT/p for p in original]+[ROOT/p for p in extras])
    save('initial-inventory.json',initial)
    for rel,info in original.items(): assert initial[rel] == info, ('original_input',rel)
    roots = [ROOT/'scripts/first-rational-kernel',ROOT/'scripts/finite-derivative-coefficients']
    old_names = {str(p.relative_to(ROOT)) for root in roots for p in root.rglob('*') if p.is_file()}
    assert old_names == {p for p in original if any(p.startswith(str(root.relative_to(ROOT))+'/') for root in roots)}
    preservation = read('preservation.json')
    assert preservation == {'all_match':True,'original_file_set_unchanged':True,'count':62,
        'complete_rehashed_inventory':original,'fresh_sources_unchanged':True}
    manifest = read('manifest.json')
    source_review = read('source-review.json')
    body = (OLD/'run.py').read_text()
    tree = ast.parse(body)
    assignments = [node for node in ast.walk(tree) if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='transformations' for t in node.targets)]
    assert len(assignments)==1
    transforms = ast.literal_eval(assignments[0].value)
    changes = source_review['exact_unique_transformations']
    assert set(transforms)==set(changes)=={'producer.py','replay.py'}
    differences = []
    for name,pairs in transforms.items():
        assert changes[name] == [{'old':a,'new':b} for a,b in pairs]
        before = (ROOT/'scripts/first-rational-kernel'/name).read_text()
        after = before
        for a,b in pairs:
            assert after.count(a)==1
            after = after.replace(a,b,1)
        assert after == (OLD/name).read_text(), ('complete_source',name)
        ast.parse(after)
        actual = {'sha256':digest(after.encode()),'bytes':len(after.encode())}
        assert actual == manifest['source_hashes'][name] == source_review['sources'][name]
        differences.extend(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile='old/'+name,tofile='step-412/'+name))
    assert ''.join(differences) == (OLD/'source-diff.txt').read_text()
    assert source_review['n']==2 and source_review['original_entrypoint_imported_or_executed'] is False
    expected_manifest = {'n':2,'panels':1016,'grid_fractional_bits':256,'factor_degrees':[128,64,64],
        'product_slots':[193,257],'coefficient_pairs_per_panel':[8385,12545],
        'scalar_exp_terms':128,'log_terms':128,'scalar_squares':16,
        'final_enlargement_grid_units':2**72,'time_cap_seconds':180,'work_deadline_seconds':174,
        'byte_cap':LIMIT,'diagnostic_allowance':8192,'final_report_reserve':65536,'source_generation_in_cap':True}
    for key,value in expected_manifest.items(): assert manifest[key]==value, ('manifest',key)
    assert manifest['step']=='BSD-2026-10-23-412-second-rational-kernel'
    assert manifest['python'].startswith('3.15.0')
    assert read('parameter-identity.json') == {'complete_record_equal':True,'independent_reconstruction':True,
        'c_midpoint_unchanged':True,'doubled_midpoint':False,'preliminary_replay_ledger_reset':True}
    status,fin,term = read('status.json'),read('finalization.json'),read('terminal-report.json')
    assert status['status']=='PASS' and status['first_failure'] is None and status['complete_replay']
    assert status['state']=={'stage':'complete','panels':1016,'n':2}
    for key in ('all_inputs_preserved','source_preservation','resource_checks','terminal_timer_retained'): assert status[key] is True
    assert status['n']==2 and status['preserved_inputs']==62
    excluded = {'status.json','finalization.json','terminal-report.json'}
    before_status = sum(p.stat().st_size for p in fixed_paths if p.name not in excluded)
    assert before_status == status['new_disk_before_status_bytes'] == 1587986
    byte_bound = before_status+73728
    second_bound = math.ceil(status['elapsed_before_status_write_seconds'])+2
    assert byte_bound==status['conservative_inclusive_bytes']==1661714 < LIMIT
    assert second_bound==status['conservative_inclusive_seconds']==28 < 180
    assert status['required_seconds']==180 and status['required_bytes']==LIMIT
    assert fin['disk_after_status_bytes']==before_status+(OLD/'status.json').stat().st_size
    assert fin['terminal_timer_retained'] is True
    for rec in (fin,term):
        assert rec['inclusive_seconds']==second_bound and rec['inclusive_bytes']==byte_bound
    assert status['elapsed_before_status_write_seconds'] < fin['elapsed_after_status_write_seconds'] < term['elapsed_after_finalization_write_seconds'] < second_bound
    assert term['status']=='PASS' and term['failure'] is None and term['n']==2 and term['preserved_inputs']==62
    assert term['required_seconds']==180 and term['required_bytes']==LIMIT
    assert term['path']=='scripts/second-rational-kernel/step-412/status.json'
    assert sum(p.stat().st_size for p in fixed_paths)+8192 <= byte_bound
    working=read('working.json')
    assert working['n']==2 and working['stage']=='replay' and working['panels']==961
    assert working['elapsed_seconds']<status['elapsed_before_status_write_seconds']
    save('historical-review.json',{'manifest':manifest,'source_review':source_review,'status':status,
        'finalization':fin,'terminal':term,'working':working,'original_count':len(original),
        'fixed_file_count':len(fixed_paths),'before_status_bytes':before_status,'source_and_diff_exact':True,
        'qualification':'Historical bootstrap is descriptive, not a retained executable bootstrap; terminal timestamp precedes its own write and process exit. Fresh timing cannot certify either historical completion. Original n=1 finalization qualification remains.'})
    spec=importlib.util.spec_from_file_location('fixed_second_replay_415',OLD/'replay.py')
    replay=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(replay)
    D=replay.SCALE
    assert D==2**256
    old_floor,old_ceil=replay.floor_checked,replay.ceil_checked
    old_times,old_over=replay.times,replay.over
    old_enc,old_plus=replay.enclose,replay.plus
    old_neg,old_clip,old_product=replay.opposite,replay.intersect,replay.product
    def floor_checked(n,d):
        actual=old_floor(n,d)
        assert d>0 and actual==n//d and actual*d<=n<(actual+1)*d
        signed['floor']+=1
        return actual
    def ceil_checked(n,d):
        actual=old_ceil(n,d)
        assert d>0 and actual==-((-n)//d) and (actual-1)*d<n<=actual*d
        signed['ceiling']+=1
        return actual
    def times(a,b):
        actual=old_times(a,b)
        al,au=a; bl,bu=b
        extrema=(al*bl,al*bu,au*bl,au*bu)
        assert actual==(min(extrema)//D,-((-max(extrema))//D))
        ai=0 if al>=0 else 1 if au<=0 else 2
        bi=0 if bl>=0 else 1 if bu<=0 else 2
        signed['sign_cases'][3*ai+bi]+=1
        signed['multiply']+=1
        if a==(0,0) or b==(0,0): signed['zero_operand_multiplications']+=1
        return actual
    def over(a,k):
        actual=old_over(a,k)
        assert k>0 and a[0]<=a[1] and actual==(a[0]//k,-((-a[1])//k))
        signed['divide']+=1
        return actual
    def enclose(n,d=1):
        actual=old_enc(n,d)
        assert d>0 and actual==((n*D)//d,-((-n*D)//d))
        signed['convert']+=1
        return actual
    def plus(a,b):
        actual=old_plus(a,b)
        assert actual==(a[0]+b[0],a[1]+b[1])
        signed['plus']+=1
        return actual
    def opposite(a):
        actual=old_neg(a)
        assert actual==(-a[1],-a[0])
        signed['negate']+=1
        return actual
    def intersect(a,l,u):
        actual=old_clip(a,l,u)
        assert l<=u and actual==(max(a[0],l),min(a[1],u)) and actual[0]<=actual[1]
        signed['clip']+=1
        return actual
    def product(a,b):
        before=replay.LEDGER.get('coefficient_pairs',0)
        actual=old_product(a,b)
        assert replay.LEDGER['coefficient_pairs']-before==len(a)*len(b)
        assert (len(a),len(b),len(actual)) in ((129,65,193),(193,65,257))
        assert all(l<=u for l,u in actual)
        signed['products']+=1
        return actual
    for name,fn in [('floor_checked',floor_checked),('ceil_checked',ceil_checked),('times',times),('over',over),
        ('enclose',enclose),('plus',plus),('opposite',opposite),('intersect',intersect),('product',product)]: setattr(replay,name,fn)
    intervals=[(-2*D,-D),(-D,0),(-D,D),(0,0),(0,D),(D,2*D)]
    for a in intervals:
        for b in intervals: times(a,b)
    for n in (-2*D-1,-D,-1,0,1,D,2*D+1):
        for d in (1,3,D): floor_checked(n,d); ceil_checked(n,d)
    assert all(signed['sign_cases'])
    save('primitive-controls.json',signed)
    for key in signed: signed[key]=[0]*9 if key=='sign_cases' else 0
    replay.LEDGER.clear()
    parameter=read('parameter.json')
    assert parameter==json.loads((ROOT/'scripts/first-rational-kernel/step-404/parameter.json').read_text())
    assert parameter['c_grid']==[36887902191165742374446831090090100164633110307723623187031015736440321082816,36887902191165742374446831090090100380471044238365418461395933078627191865791]
    assert parameter['midpoint']==[73775804382331484748893662180180200545104154546089041648426948815067512948607,2**257]
    final=read('kernel.json')
    progress('replay',0)
    with (OLD/'panels.jsonl').open() as handle:
        report=replay.run(parameter,(json.loads(line) for line in handle),final,progress)
    # The saved aggregate adds exactly this one metadata field after run returns.
    assert 'n' not in report
    assert {**report,'n':2} == read('replay.json'), 'complete_original_report'
    assert report['counts']==replay.LEDGER==final['counts']
    for key,expected in {'multiply':21801456,'divide':716408,'convert':5083,'negate':356616,'clip':24386}.items():
        assert signed[key]==replay.LEDGER[key]==expected
    assert signed['products']==2032 and replay.LEDGER['coefficient_pairs']==21264880
    assert replay.LEDGER['add']==21787232==signed['plus']+21264880+1016
    assert replay.LEDGER['scale']==2033 and replay.LEDGER['enlarge']==2034
    assert sum(signed['sign_cases'])==signed['multiply']
    assert signed['floor']==signed['ceiling']==signed['multiply']+signed['divide']+signed['convert']+1
    expected_ends=[27752108342762384198586753289291805502031167688405252130383566291743051605286,27752108342762384198586753289291805502031167688405252139828299257482344076057]
    assert final['final_grid']==expected_ends
    assert final['polynomial_sum']==[expected_ends[0]+2**72,expected_ends[1]-2**72]
    assert final['polynomial_sum'][1]-final['polynomial_sum'][0]==2043379
    assert Fraction(*final['midpoint'])==Fraction(55504216685524768397173506578583611004062335376810504270211865549225395681343,2*D)
    radius=Fraction(*final['radius'])
    assert radius==Fraction(2**73+2043379,2*D)
    assert radius<Fraction(1,2**50) and radius<Fraction(1,2**183)
    assert final['required_radius']==[1,2**50] and final['stronger_radius']==[1,2**183]
    save('complete-replay.json',{'replay':report,'aggregate_metadata':{'n':2},'independent_primitives':signed,
        'parameter':parameter,'final':final,'required_radius_strict':True,'stronger_radius_strict':True,
        'original_report_exact_match':True,'producer_executed':False,'old_entrypoints_executed':False,'kernels_replayed':[2]})
    STATE.update(stage='complete',panels=1016)
except BaseException as exc:
    failure={'type':type(exc).__name__,'message':str(exc),'state':dict(STATE),'traceback':traceback.format_exc()}
finally:
    signal.setitimer(signal.ITIMER_REAL,max(.001,180-(time.monotonic()-START)))
    if failure: save('first-failure.json',failure)
    after=inventory([ROOT/p for p in initial])
    mismatches=[p for p in initial if after.get(p)!=initial[p]]
    fixed_after={str(p.relative_to(ROOT)) for p in OLD.rglob('*') if p.is_file()}
    historical_after={str(p.relative_to(ROOT)) for root in roots for p in root.rglob('*') if p.is_file()}
    preserve=not mismatches and fixed_after==fixed_names and historical_after==old_names
    save('preservation.json',{'files':after,'count':len(initial),'original_inputs':62,
        'mismatches':mismatches,'fixed_file_set_unchanged':fixed_after==fixed_names,
        'original_directory_sets_unchanged':historical_after==old_names,'all_match':preserve})
    if not preserve and failure is None:
        failure={'type':'PreservationFailure','message':str(mismatches)}
        save('first-failure.json',failure)
    elapsed=time.monotonic()-START
    ok=failure is None and report is not None and elapsed<174 and disk()+73728<LIMIT
    save('status.json',{'status':'PASS' if ok else 'STOP','state':STATE,'failure':failure,
        'preserved_files':len(initial),'original_inputs':62,'elapsed_before_status_seconds':elapsed,
        'historical_finalization_qualification':True,'required_seconds':180,'required_bytes':LIMIT})
    print(json.dumps({'status':'PASS' if ok else 'STOP','failure':failure,'panels':STATE['panels']}),flush=True)
    assert time.monotonic()-START<180 and disk()+8192<LIMIT
    sys.exit(0 if ok else 1)
