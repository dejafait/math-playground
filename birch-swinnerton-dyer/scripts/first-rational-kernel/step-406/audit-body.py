import hashlib, importlib.util, json, math, sys, traceback
from pathlib import Path
from fractions import Fraction
sys.dont_write_bytecode = True
ROOT = Path.cwd()
BASE = ROOT/'scripts/first-rational-kernel'
OLD = BASE/'step-404'
OUT = BASE/'step-406'
LIMIT = 134217728
STATE = {'stage': 'setup', 'panels': 0}
failure = None
report = None
initial = {}
checks = {}
signed = {'floor': 0, 'ceiling': 0, 'multiply': 0, 'divide': 0,
          'convert': 0, 'plus': 0, 'negate': 0, 'clip': 0, 'products': 0,
          'zero_operand_multiplications': 0, 'sign_cases': [0]*9}
def digest(raw):
    return hashlib.sha256(raw).hexdigest()
def inventory(paths):
    return {str(p.relative_to(ROOT)): {'sha256': digest(p.read_bytes()),
            'bytes': p.stat().st_size} for p in sorted(set(paths))}
def disk():
    return sum(p.stat().st_size for p in OUT.rglob('*') if p.is_file())
def save(name, obj):
    raw = (json.dumps(obj, sort_keys=True, separators=(',', ':'))+'\n').encode()
    assert disk()+len(raw)+65536 <= LIMIT, 'fresh_output_cap'
    (OUT/name).write_bytes(raw)
def progress(stage, panels):
    STATE.update(stage=stage, panels=panels)
    save('working.json', {**STATE, 'elapsed_seconds': time.monotonic()-START})
    if panels % 256 == 1:
        print(json.dumps({'stage': stage, 'panels': panels,
                          'elapsed_seconds': round(time.monotonic()-START, 3)}), flush=True)
try:
    OUT.mkdir()
    (OUT/'audit-body.py').write_text(SOURCE)
    (OUT/'bootstrap.txt').write_text(
        "Clock started before signal/path imports, directory creation, source writing and inventories.\n"
        "The command sets SOURCE to audit-body.py bytes and exec(compile(SOURCE,...), globals()).\n"
        "Work alarm at 174 seconds; finalization alarm remains armed through final report at 180 seconds.\n"
        "SOURCE and START are supplied by the bootstrap; no source/module was imported before START.\n")
    selected = json.loads((OLD/'input-inventory.json').read_text())
    assert len(selected) == 11
    paths = list(p for p in OLD.rglob('*') if p.is_file())
    paths += [ROOT/p for p in selected]
    initial = inventory(paths)
    save('initial-inventory.json', initial)
    pairs = []
    for rel, info in selected.items():
        original, fixed = ROOT/rel, OLD/'originals'/rel
        assert original.read_bytes() == fixed.read_bytes(), ('source_copy_mismatch', rel)
        assert initial[rel] == info, ('selected_input_mismatch', rel)
        assert initial[str(fixed.relative_to(ROOT))] == info, ('fixed_input_mismatch', rel)
        pairs.append({'path': rel, 'original_matches': True, 'fixed_matches': True})
    checks['input_pairs'] = len(pairs)
    # Parse every small historical record and check exact resource boundaries.
    status = json.loads((OLD/'status.json').read_text())
    manifest = json.loads((OLD/'manifest.json').read_text())
    preservation = json.loads((OLD/'preservation.json').read_text())
    historical_replay = json.loads((OLD/'replay.json').read_text())
    assert preservation['count'] == 11 and preservation['all_match']
    assert sorted(preservation['files'], key=lambda r:r['path']) == sorted(pairs,key=lambda r:r['path'])
    assert status['status'] == 'PASS' and status['first_failure'] is None
    assert status['state'] == {'stage':'complete','panels':1016} and status['complete_replay']
    assert status['preserved_inputs'] == 11 and status['all_inputs_preserved']
    assert manifest['n'] == 1 and manifest['panels'] == 1016
    for key, expected in {'grid_fractional_bits':256,'factor_degrees':[128,64,64],
        'product_slots':[193,257],'coefficient_pairs_per_panel':[8385,12545],
        'log_terms':128,'scalar_exp_terms':128,'scalar_squares':16,
        'final_enlargement_grid_units':2**72,'arctangent_terms':[24,25],
        'time_cap_seconds':180,'work_deadline_seconds':174,'byte_cap':LIMIT,
        'diagnostic_stdout_allowance':8192}.items():
        assert manifest[key] == expected, ('manifest', key)
    originals = [OLD/'originals'/p for p in selected]
    historical_names = ['input-inventory.json','manifest.json','parameter.json',
                        'panels.jsonl','kernel.json','replay.json','working-status.json','preservation.json']
    historic_disk = sum(p.stat().st_size for p in originals)
    historic_disk += sum((OLD/p).stat().st_size for p in historical_names)
    static_bytes = sum((ROOT/p).stat().st_size for p in manifest['source_paths'])
    assert historic_disk == status['actual_disk_before_status_bytes']
    assert historic_disk+static_bytes+16384 == status['conservative_inclusive_bytes']
    assert math.ceil(status['elapsed_before_final_write_seconds'])+2 == status['conservative_inclusive_seconds']
    assert status['conservative_inclusive_seconds'] <= 180
    assert status['conservative_inclusive_bytes'] <= LIMIT and status['resource_checks']
    assert (OLD/'status.json').stat().st_size < 8192
    all_current_bytes = sum(p.stat().st_size for p in OLD.rglob('*') if p.is_file())+static_bytes
    assert all_current_bytes+8192 <= status['conservative_inclusive_bytes']
    historical = {
        'status': status, 'manifest': manifest, 'preservation': preservation,
        'reconstructed_disk_before_status_bytes': historic_disk,
        'static_source_bytes': static_bytes,
        'current_all_artifacts_plus_static_bytes': all_current_bytes,
        'original_output_bound_including_reserves': status['conservative_inclusive_bytes'],
        'time_verdict': 'Recorded pre-final-write measurement only; historical post-write duration not independently recoverable.',
        'postwrite_time_in_L103_narrative': 25.268027415964752,
        'retained_terminal_log_found': False,
        'hard_final_report_watchdog': False,
        'qualification': 'Original runner clears timer before finalization. Source asserts post-write elapsed bound, but terminal output is not retained as a separate artifact. No fresh timing substitutes for it.'
    }
    save('historical-resources.json', historical)
    # Import only the unchanged replay. Producer and original runner are never imported or executed.
    spec = importlib.util.spec_from_file_location('fixed_replay_406', BASE/'replay.py')
    replay = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(replay)
    D = replay.SCALE
    assert D == 2**256
    old_floor, old_ceil = replay.floor_checked, replay.ceil_checked
    old_times, old_over = replay.times, replay.over
    old_enc, old_plus = replay.enclose, replay.plus
    old_neg, old_clip, old_product = replay.opposite, replay.intersect, replay.product
    def floor_checked(num, den):
        actual = old_floor(num, den)
        assert actual == num//den
        signed['floor'] += 1
        return actual
    def ceil_checked(num, den):
        actual = old_ceil(num, den)
        assert actual == -((-num)//den)
        signed['ceiling'] += 1
        return actual
    def times(a,b):
        actual = old_times(a,b)
        al,au = a
        bl,bu = b
        extrema = (al*bl,al*bu,au*bl,au*bu)
        assert actual == (min(extrema)//D, -((-max(extrema))//D)), ('multiply',a,b,actual)
        ai = 0 if al >= 0 else 1 if au <= 0 else 2
        bi = 0 if bl >= 0 else 1 if bu <= 0 else 2
        signed['sign_cases'][3*ai+bi] += 1
        signed['multiply'] += 1
        if a == (0,0) or b == (0,0):
            signed['zero_operand_multiplications'] += 1
        return actual
    def over(a,k):
        actual = old_over(a,k)
        assert k > 0 and a[0] <= a[1]
        assert actual == (a[0]//k,-((-a[1])//k))
        signed['divide'] += 1
        return actual
    def enclose(n,d=1):
        actual = old_enc(n,d)
        assert d > 0 and actual == ((n*D)//d,-((-n*D)//d))
        signed['convert'] += 1
        return actual
    def plus(a,b):
        actual = old_plus(a,b)
        assert actual == (a[0]+b[0],a[1]+b[1])
        signed['plus'] += 1
        return actual
    def opposite(a):
        actual = old_neg(a)
        assert actual == (-a[1],-a[0])
        signed['negate'] += 1
        return actual
    def intersect(a,l,u):
        actual = old_clip(a,l,u)
        assert l <= u and actual == (max(a[0],l),min(a[1],u))
        assert actual[0] <= actual[1]
        signed['clip'] += 1
        return actual
    def product(a,b):
        before = replay.LEDGER.get('coefficient_pairs',0)
        actual = old_product(a,b)
        assert replay.LEDGER['coefficient_pairs']-before == len(a)*len(b)
        assert len(actual) == len(a)+len(b)-1
        assert (len(a),len(b),len(actual)) in ((129,65,193),(193,65,257))
        assert all(x<=y for x,y in actual)
        signed['products'] += 1
        return actual
    for name, function in [('floor_checked',floor_checked),('ceil_checked',ceil_checked),
        ('times',times),('over',over),('enclose',enclose),('plus',plus),
        ('opposite',opposite),('intersect',intersect),('product',product)]:
        setattr(replay,name,function)
    # Full deterministic controls include all sign branches, exact zeros, crossing
    # zero and endpoint-zero intervals. They precede the sole kernel replay.
    intervals = [(-2*D,-D),(-D,0),(-D,D),(0,0),(0,D),(D,2*D)]
    for a in intervals:
        for b in intervals:
            times(a,b)
    for n in (-2*D-1,-D,-1,0,1,D,2*D+1):
        for d in (1,3,D):
            floor_checked(n,d)
            ceil_checked(n,d)
    controls = json.loads(json.dumps(signed))
    save('primitive-controls.json', controls)
    for key in signed:
        signed[key] = [0]*9 if key == 'sign_cases' else 0
    replay.LEDGER.clear()
    parameter = json.loads((OLD/'parameter.json').read_text())
    final = json.loads((OLD/'kernel.json').read_text())
    STATE.update(stage='replay',panels=0)
    with (OLD/'panels.jsonl').open() as handle:
        report = replay.run(parameter,(json.loads(line) for line in handle),final,progress)
    assert report == historical_replay, 'historical_full_replay_report'
    assert signed['multiply'] == replay.LEDGER['multiply'] == 21801456
    assert signed['divide'] == replay.LEDGER['divide'] == 716408
    assert signed['convert'] == replay.LEDGER['convert']
    assert signed['negate'] == replay.LEDGER['negate']
    assert signed['clip'] == replay.LEDGER['clip']
    assert signed['products'] == 2032
    assert replay.LEDGER['coefficient_pairs'] == 21264880
    assert replay.LEDGER['add'] == 21787232
    assert signed['plus']+21264880+1016 == replay.LEDGER['add']
    assert sum(signed['sign_cases']) == signed['multiply']
    assert signed['floor'] == signed['ceiling'] == signed['multiply']+signed['divide']+signed['convert']+1
    radius = Fraction(*final['radius'])
    assert radius == Fraction(2**72+2883372,D)
    assert radius <= Fraction(1,2**50) and radius < Fraction(1,2**183)
    assert final['polynomial_sum'][1]-final['polynomial_sum'][0] == 2*2883372
    save('complete-replay.json', {'replay':report,'independent_primitives':signed,
        'parameter':parameter, 'final':final,
        'required_radius_pass': True, 'stronger_radius_pass': True,
        'original_report_exact_match':True,'producer_executed':False,
        'original_runner_executed':False,'kernels_replayed':[1]})
    STATE.update(stage='complete',panels=1016)
except BaseException as exc:
    failure = {'type':type(exc).__name__,'message':str(exc),'state':dict(STATE),
               'traceback':traceback.format_exc()}
finally:
    # Keep a final deadline armed; timer dispatch is still an interface limitation.
    signal.setitimer(signal.ITIMER_REAL,max(0.001,180-(time.monotonic()-START)))
    if OUT.exists():
        if failure:
            save('first-failure.json', failure)
        after = inventory([ROOT/p for p in initial])
        mismatches = [p for p in initial if after.get(p) != initial[p]]
        save('preservation.json', {'files':after,'count':len(initial),
             'inventoried_pairs':len(selected) if 'selected' in globals() else 0,
             'mismatches':mismatches,'all_match':not mismatches})
        if mismatches and failure is None:
            failure = {'type':'PreservationFailure','message':str(mismatches)}
            save('first-failure.json',failure)
        elapsed = time.monotonic()-START
        inclusive_seconds = math.ceil(elapsed)+2
        inclusive_bytes = disk()+65536+8192
        ok = failure is None and report is not None and inclusive_seconds<=180 and inclusive_bytes<=LIMIT
        save('status.json', {'status':'PASS' if ok else 'STOP','state':STATE,
            'failure':failure,'historical_timing_qualification':True,
            'elapsed_before_status_seconds':elapsed,'inclusive_seconds':inclusive_seconds,
            'inclusive_bytes':inclusive_bytes,'required_seconds':180,'required_bytes':LIMIT,
            'preserved_files':len(initial),'input_pairs':checks.get('input_pairs',0)})
        measured_after_status = time.monotonic()-START
        save('finalization.json',{'elapsed_after_status_write_seconds':measured_after_status,
             'all_sources_copies_replay_preservation_status_included':True,
             'inclusive_seconds':inclusive_seconds,'inclusive_bytes':inclusive_bytes})
        # This read/write/verification and terminal report also have reserved headroom.
        assert disk()+8192 <= inclusive_bytes
        measured_after_finalization = time.monotonic()-START
        assert measured_after_finalization <= inclusive_seconds <= 180
        print(json.dumps({'status':'PASS' if ok else 'STOP','actual_seconds_after_finalization':measured_after_finalization,
            'inclusive_seconds':inclusive_seconds,'inclusive_bytes':inclusive_bytes,
            'required_seconds':180,'required_bytes':LIMIT,'failure':failure,
            'certificate':'scripts/first-rational-kernel/step-406/status.json'}),flush=True)
        assert time.monotonic()-START <= inclusive_seconds
    signal.setitimer(signal.ITIMER_REAL,0)
