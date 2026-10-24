import hashlib, importlib.util, json, math, sys, traceback, difflib, ast
from pathlib import Path
from fractions import Fraction
sys.dont_write_bytecode = True
ROOT = Path.cwd()
BASE = ROOT/'scripts/second-rational-kernel'
OUT = BASE/'step-412'
OLD = ROOT/'scripts/first-rational-kernel'
LIMIT = 134217728
RESERVE = 65536
STATE = {'stage': 'setup', 'panels': 0, 'n': 2}
initial = {}
original_paths = []
source_info = {}
report = None
failure = None
handle = None

def sha(raw):
    return hashlib.sha256(raw).hexdigest()
def disk():
    return sum(p.stat().st_size for p in BASE.rglob('*') if p.is_file())
def check_work():
    assert time.monotonic()-START < 174, 'work_deadline'
    assert disk()+RESERVE+8192 < LIMIT, 'byte_cap'
def save(name, value):
    raw = (json.dumps(value,sort_keys=True,separators=(',',':'))+'\n').encode()
    assert disk()+len(raw)+RESERVE+8192 <= LIMIT, 'new_byte_cap'
    (OUT/name).write_bytes(raw)
def inventory(paths):
    answer = {}
    for p in sorted(set(paths)):
        raw = p.read_bytes()
        answer[str(p.relative_to(ROOT))] = {'sha256':sha(raw), 'bytes':len(raw)}
    return answer
def progress(stage, panels):
    STATE.update(stage=stage,panels=panels)
    check_work()
    save('working.json',{**STATE,'elapsed_seconds':time.monotonic()-START})
def emit(record):
    raw = (json.dumps(record,separators=(',',':'))+'\n').encode()
    assert disk()+len(raw)+RESERVE+8192 <= LIMIT, 'panel_byte_cap'
    handle.write(raw)
    handle.flush()
    STATE.update(stage='production',panels=record['index']+1)
def load(name,path):
    spec = importlib.util.spec_from_file_location(name,path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
def json_form(x):
    return json.loads(json.dumps(x))
try:
    # Exclusive creation: a partial attempt is never overwritten or resumed.
    BASE.mkdir()
    OUT.mkdir()
    (OUT/'run.py').write_text(SOURCE)
    (OUT/'bootstrap.txt').write_text('Clock START precedes signal setup, SOURCE assignment, imports, directories, source writing and inventories. Work deadline 174 seconds; terminal deadline 180 remains armed through final writing and terminal report. No old entrypoint executes.\n')
    selected = [
        'lemmas/L031-independent-twist-five-ratio-certificate.md',
        'lemmas/L101-conductor389-second-derivative-error-budget.md',
        'lemmas/L102-capped-rational-taylor-kernel-enclosures.md',
        'lemmas/L103-first-rational-kernel-certificate.md',
        'drafts/literature/2026-10-23-second-rational-kernel-certificate.md',
        'drafts/source-notes/2026-10-23-second-rational-kernel-coverage.md',
        'ATTEMPTS/043-complex-order-two-quadratic-coefficient-import.md',
        'ATTEMPTS/045-index-128-table-source-adaptation-stop.md',
        'ATTEMPTS/046-fixed-derivative-backend-unavailable.md']
    roots = [OLD, ROOT/'scripts/finite-derivative-coefficients']
    original_paths = [p for root in roots for p in root.rglob('*') if p.is_file()]
    original_paths += [ROOT/rel for rel in selected]
    initial = inventory(original_paths)
    save('initial-inventory.json', initial)
    transformations = {
      'producer.py': [
       ('Static step-404 producer.', 'Isolated step-412 n=2 producer.'),
       ('scalar, scalar_hash = exponential(u*a8, v*8*(1 << 16))',
        'assert 0 < 2*u*a8 < v*8*(1 << 16)//8\n        scalar, scalar_hash = exponential(2*u*a8, v*8*(1 << 16))'),
       ('beta = clip(cv(u, 8*v), 0, 8*D)',
        'assert 0 < 2*u <= 64*v\n        beta = clip(cv(2*u, 8*v), 0, 8*D)'),
       ('assert radius <= Fraction(1, 1 << 50)', 'assert radius < Fraction(1, 1 << 50)'),
       ("'n': 1}", "'n': 2}")],
      'replay.py': [
       ('Independent step-404 replay;', 'Independent isolated step-412 n=2 replay;'),
       ('scalar, hs = exp_series(num*endpoint, den*524288)',
        'assert 0 < num*endpoint*2 < den*65536\n        scalar, hs = exp_series(num*endpoint*2, den*524288)'),
       ('beta = intersect(enclose(num, den*8), 0, SCALE*8)',
        'assert 0 < num*2 <= den*64\n        beta = intersect(enclose(num*2, den*8), 0, SCALE*8)'),
       ('rad <= Fraction(1, 2**50)', 'rad < Fraction(1, 2**50)'),
       ("'n': 1}", "'n': 2}")]
    }
    changes = {}
    differences = []
    for name, replacements in transformations.items():
        before = (OLD/name).read_text()
        after = before
        for old,new in replacements:
            assert after.count(old) == 1, ('unique_exact_adaptation',name,old)
            after = after.replace(old,new,1)
        ast.parse(after)
        (OUT/name).write_text(after)
        assert (OUT/name).read_text() == after
        source_info[name] = {'sha256':sha(after.encode()),'bytes':len(after.encode())}
        changes[name] = [{'old':o,'new':n} for o,n in replacements]
        differences.extend(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile='old/'+name,tofile='step-412/'+name))
    (OUT/'source-diff.txt').write_text(''.join(differences))
    save('source-review.json', {'n':2,'exact_unique_transformations':changes,
        'review':'Only two scalar arguments per implementation, strict acceptance and output labels change; added exact range checks precede containing exp/beta clips. All independent arithmetic, parameter rules and full loops remain copied separately.',
        'sources':source_info,'original_entrypoint_imported_or_executed':False})
    save('manifest.json', {'step':'BSD-2026-10-23-412-second-rational-kernel',
        'n':2,'parameter':'unchanged complete step-404 parameter.json; no doubling',
        'encoding':'grid endpoint integer / 2^256; rational [numerator,positive denominator]',
        'grid_fractional_bits':256,'panels':1016,'factor_degrees':[128,64,64],
        'product_slots':[193,257],'coefficient_pairs_per_panel':[8385,12545],
        'scalar_exp_terms':128,'log_terms':128,'scalar_squares':16,
        'final_enlargement_grid_units':2**72,'time_cap_seconds':180,
        'work_deadline_seconds':174,'byte_cap':LIMIT,'diagnostic_allowance':8192,
        'final_report_reserve':RESERVE,'python':sys.version,
        'source_hashes':source_info,'source_generation_in_cap':True,
        'independence':'producer four-product min/max; replay signed divmod, sign-case extrema, reversed convolution and primitive traversal; no producer arithmetic imported by replay'})
    producer = load('second_producer_412',OUT/'producer.py')
    replay = load('second_replay_412',OUT/'replay.py')
    STATE.update(stage='parameter')
    fixed = json.loads((OLD/'step-404/parameter.json').read_text())
    parameter = producer.parameter()
    assert json_form(parameter) == fixed, 'entire_parameter_record_identity'
    assert fixed['c_grid'] == [36887902191165742374446831090090100164633110307723623187031015736440321082816,36887902191165742374446831090090100380471044238365418461395933078627191865791]
    assert fixed['midpoint'] == [73775804382331484748893662180180200545104154546089041648426948815067512948607,2**257]
    assert replay.verify_parameter(fixed) == tuple(fixed['midpoint'])
    replay.LEDGER.clear()  # Preliminary checks only; full pass verifies parameter afresh.
    save('parameter.json',parameter)
    save('parameter-identity.json',{'complete_record_equal':True,'independent_reconstruction':True,'c_midpoint_unchanged':True,'doubled_midpoint':False,'preliminary_replay_ledger_reset':True})
    progress('production',0)
    handle = (OUT/'panels.jsonl').open('xb')
    kernel = producer.run(parameter,emit,progress)
    handle.close()
    handle = None
    assert kernel['n'] == 2
    assert Fraction(*kernel['radius']) < Fraction(1,2**50)
    assert Fraction(*kernel['radius']) < Fraction(1,2**183)
    save('kernel.json',kernel)
    progress('replay',0)
    with (OUT/'panels.jsonl').open() as f:
        report = replay.run(json.loads((OUT/'parameter.json').read_text()),
            (json.loads(line) for line in f),json.loads((OUT/'kernel.json').read_text()),progress)
    report['n'] = 2
    assert report['panels'] == 1016 and report['coefficient_pairs'] == 21264880
    assert report['counts'] == kernel['counts']
    save('replay.json',report)
    STATE.update(stage='complete',panels=1016)
    check_work()
except BaseException as exc:
    failure = {'type':type(exc).__name__,'message':str(exc),'state':dict(STATE),'traceback':traceback.format_exc()}
finally:
    # The terminal timer remains armed through all final writing and reporting.
    signal.setitimer(signal.ITIMER_REAL,max(0.001,180-(time.monotonic()-START)))
    if handle is not None:
        handle.close()
    preservation = inventory(original_paths)
    unchanged = preservation == initial
    current_old_paths = [p for root in (OLD,ROOT/'scripts/finite-derivative-coefficients') for p in root.rglob('*') if p.is_file()]
    old_initial_set = {p for p in initial if p.startswith('scripts/first-rational-kernel/') or p.startswith('scripts/finite-derivative-coefficients/')}
    names_unchanged = {str(p.relative_to(ROOT)) for p in current_old_paths} == old_initial_set
    sources_match = all(sha((OUT/n).read_bytes()) == info['sha256'] for n,info in source_info.items())
    if not (unchanged and names_unchanged and sources_match) and failure is None:
        failure = {'type':'PreservationFailure','message':'original inventory/names or fresh source mismatch','state':dict(STATE)}
    if OUT.exists():
        save('preservation.json',{'all_match':unchanged,'original_file_set_unchanged':names_unchanged,
            'count':len(initial),'complete_rehashed_inventory':preservation,'fresh_sources_unchanged':sources_match})
        if failure is not None:
            save('first-failure.json',failure)
        elapsed = time.monotonic()-START
        inclusive_seconds = math.ceil(elapsed)+2
        inclusive_bytes = disk()+RESERVE+8192
        ok = inclusive_seconds <= 180 and inclusive_bytes <= LIMIT
        status = {'status':'PASS' if failure is None and report is not None and ok else 'STOP',
            'n':2,'state':STATE,'complete_replay':report is not None,'first_failure':failure,
            'all_inputs_preserved':unchanged and names_unchanged,'preserved_inputs':len(initial),
            'source_preservation':sources_match,'elapsed_before_status_write_seconds':elapsed,
            'conservative_inclusive_seconds':inclusive_seconds,'conservative_inclusive_bytes':inclusive_bytes,
            'required_seconds':180,'required_bytes':LIMIT,'resource_checks':ok,
            'terminal_timer_retained':True,'new_disk_before_status_bytes':disk()}
        save('status.json',status)
        after_status = time.monotonic()-START
        save('finalization.json',{'elapsed_after_status_write_seconds':after_status,
            'terminal_timer_retained':True,'inclusive_seconds':inclusive_seconds,
            'inclusive_bytes':inclusive_bytes,'disk_after_status_bytes':disk()})
        after_finalization = time.monotonic()-START
        terminal = {'status':status['status'],'n':2,'elapsed_after_finalization_write_seconds':after_finalization,
            'inclusive_seconds':inclusive_seconds,'inclusive_bytes':inclusive_bytes,
            'required_seconds':180,'required_bytes':LIMIT,'preserved_inputs':len(initial),
            'failure':None if failure is None else failure['message'],
            'path':str((OUT/'status.json').relative_to(ROOT))}
        save('terminal-report.json',terminal)
        assert disk()+8192 <= inclusive_bytes <= LIMIT
        assert time.monotonic()-START <= inclusive_seconds <= 180
        print(json.dumps(terminal),flush=True)
        assert time.monotonic()-START <= inclusive_seconds
