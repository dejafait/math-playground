import importlib.util, json, sys, time, traceback
from pathlib import Path
from fractions import Fraction
sys.dont_write_bytecode = True
assert sys.flags.optimize == 0
import hashlib, copy
PRIMITIVES = ('floor_checked', 'ceil_checked', 'times', 'over', 'enclose', 'plus', 'opposite', 'intersect', 'product')

def fresh_counts():
    result = {k: 0 for k in ('floor', 'ceiling', 'multiply', 'divide', 'convert', 'plus', 'negate', 'clip', 'products', 'zero_operand_multiplications')}
    result['sign_cases'] = [0] * 9
    return result

def identity_for(index, output):
    fixed = (Path('scripts/four-rational-kernels/step-440') / ('n-' + str(index))).resolve()
    return (index, str(fixed), str(Path(output).resolve()), 'fixed_replay_442_' + str(index), hashlib.sha256((fixed / 'replay.py').read_bytes()).hexdigest())

def check_identity(identity, fixed, output, module, original_module):
    assert isinstance(identity, tuple) and len(identity) == 5
    assert type(identity[0]) is int and identity[0] in (19, 20, 21, 22)
    assert all((type(x) is str for x in identity[1:]))
    assert str(fixed.resolve()) == identity[1] and str(output.resolve()) == identity[2]
    assert fixed.name == output.name == 'n-' + str(identity[0])
    assert module is original_module and module.__name__ == identity[3]
    assert Path(module.__file__).resolve() == fixed / 'replay.py'
    assert hashlib.sha256((fixed / 'replay.py').read_bytes()).hexdigest() == identity[4]
    assert module.SCALE == 2 ** 256

def check_captures(module, wrappers, originals, signed, grid):
    assert len(wrappers) == 9 and len({id(f) for f in wrappers}) == 9
    old_names = ('old_floor', 'old_ceil', 'old_times', 'old_over', 'old_enc', 'old_plus', 'old_neg', 'old_clip', 'old_product')
    evidence = []
    for name, fn, old_name, old in zip(PRIMITIVES, wrappers, old_names, originals, strict=True):
        assert getattr(module, name) is fn and fn is not old
        closure = dict(zip(fn.__code__.co_freevars, (cell.cell_contents for cell in fn.__closure__), strict=True))
        assert closure[old_name] is old and closure['signed'] is signed
        if 'D' in closure:
            assert closure['D'] == grid
        if 'replay' in closure:
            assert closure['replay'] is module
        evidence.append({'primitive': name, 'closure_names': sorted(closure), 'original_captured': True, 'counter_captured': True})
    return evidence
IDENTITY = identity_for(int(sys.argv[1]), sys.argv[2])
OLD = Path(IDENTITY[1])
OUT = Path(IDENTITY[2])
START = float(sys.argv[3])
sentinel = -422
state = {'n': IDENTITY[0], 'stage': 'setup', 'panels': 0}

def read(name):
    return json.loads((OLD / name).read_text())

def save(name, obj):
    (OUT / name).write_text(json.dumps(obj, sort_keys=True, separators=(',', ':')) + '\n')

def progress(stage, panels):
    state.update(stage=stage, panels=panels)
    assert time.monotonic() - START < 174
    save('working.json', {**state, 'elapsed_seconds': time.monotonic() - START})
try:
    compile((OLD / 'replay.py').read_text(), str(OLD / 'replay.py'), 'exec', flags=0, dont_inherit=True, optimize=0)
    spec = importlib.util.spec_from_file_location(IDENTITY[3], OLD / 'replay.py')
    replay = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(replay)
    D = replay.SCALE
    assert D == 2 ** 256
    signed = {k: 0 for k in ('floor', 'ceiling', 'multiply', 'divide', 'convert', 'plus', 'negate', 'clip', 'products', 'zero_operand_multiplications')}
    signed['sign_cases'] = [0] * 9
    original_module = replay
    before_identity = IDENTITY
    before_paths = (OLD, OUT)
    original_primitives = tuple((getattr(replay, k) for k in PRIMITIVES))
    check_identity(IDENTITY, OLD, OUT, replay, original_module)
    installer_namespace = {}
    exec(compile((OUT.parent / 'installer.py').read_text(), 'installer-422', 'exec', flags=0, dont_inherit=True, optimize=0), installer_namespace)
    wrappers = installer_namespace['install'](replay, D, signed, save)
    assert IDENTITY == before_identity and (OLD, OUT) == before_paths and (sentinel == -422)
    check_identity(IDENTITY, OLD, OUT, replay, original_module)
    captures = check_captures(replay, wrappers, original_primitives, signed, D)
    assert signed == fresh_counts() and replay.LEDGER == {}
    save('identity-before-replay.json', {'identity': IDENTITY, 'captures': captures, 'sentinel': sentinel})
    parameter = read('parameter.json')
    assert parameter == json.loads(Path('scripts/first-rational-kernel/step-404/parameter.json').read_text())
    assert parameter['midpoint'] == [73775804382331484748893662180180200545104154546089041648426948815067512948607, 2 ** 257]
    final = read('kernel.json')
    progress('replay', 0)
    with (OLD / 'panels.jsonl').open() as handle:
        report = replay.run(parameter, (json.loads(line) for line in handle), final, progress)
    report = copy.deepcopy(report)
    save('returned-report.json', report)
    captured_signed = signed
    signed = copy.deepcopy(signed)
    counts = copy.deepcopy(replay.LEDGER)
    save('returned-ledger-and-signed.json', {'counts': counts, 'signed': signed})
    assert IDENTITY == before_identity and (OLD, OUT) == before_paths and (sentinel == -422)
    check_identity(IDENTITY, OLD, OUT, replay, original_module)
    save('identity-after-replay.json', {'identity': IDENTITY, 'sentinel': sentinel})
    check_captures(replay, wrappers, original_primitives, captured_signed, D)
    assert json.loads((OUT / 'returned-report.json').read_text()) == report
    assert json.loads((OUT / 'returned-ledger-and-signed.json').read_text()) == {'counts': counts, 'signed': signed}
    assert report == read('returned-report.json')
    expected_counts = {'add': 21787232, 'clip': 24386, 'coefficient_pairs': 21264880, 'convert': 5083, 'divide': 716408, 'enlarge': 2034, 'multiply': 21801456, 'negate': 356616, 'scale': 2033}
    assert report == {'status': 'PASS', 'parameter': 'complete exact reconstruction', 'panels': 1016, 'coefficient_pairs': 21264880, 'counts': expected_counts, 'radius': final['radius'], 'all_stage_comparisons': 'PASS', 'signed_rounding_checks': 'every conversion, multiplication and division', 'originals_preserved': 'checked by aggregate runner'}
    assert set(final) == {'grid_denominator', 'polynomial_sum', 'final_grid', 'midpoint', 'radius', 'required_radius', 'stronger_radius', 'counts', 'complete_panels', 'n'}
    assert 'n' not in report
    assert {**report, 'n': IDENTITY[0]} == read('replay.json')
    counts = dict(replay.LEDGER)
    assert report['counts'] == counts == final['counts']
    for name in ('producer-ledger.json', 'replay-ledger.json'):
        assert read(name) == {'n': IDENTITY[0], 'counts': counts}
    for key, expected in {'multiply': 21801456, 'divide': 716408, 'convert': 5083, 'negate': 356616, 'clip': 24386}.items():
        assert signed[key] == counts[key] == expected
    assert signed['products'] == 2032 and counts['coefficient_pairs'] == 21264880
    assert counts['add'] == 21787232 == signed['plus'] + 21264880 + 1016
    assert counts['scale'] == 2033 and counts['enlarge'] == 2034
    assert sum(signed['sign_cases']) == signed['multiply']
    assert signed['floor'] == signed['ceiling'] == signed['multiply'] + signed['divide'] + signed['convert'] + 1
    expected = json.loads((OUT.parent / 'expected-endpoints.json').read_text())[str(IDENTITY[0])]
    l, u, w = expected
    assert final['n'] == IDENTITY[0] and final['final_grid'] == [l, u]
    assert final['polynomial_sum'] == [l + 2 ** 72, u - 2 ** 72]
    assert u - l == 2 ** 73 + w
    assert Fraction(*final['midpoint']) == Fraction(l + u, 2 * D)
    assert Fraction(*final['radius']) == Fraction(2 ** 73 + w, 2 * D) < Fraction(1, 2 ** 183) < Fraction(1, 2 ** 50)
    assert final['required_radius'] == [1, 2 ** 50] and final['stronger_radius'] == [1, 2 ** 183]
    assert read('parameter-identity.json') == {'n': IDENTITY[0], 'complete_record_equal': True, 'midpoint_unchanged': True}
    status = read('status.json')
    for key, value in {'status': 'PASS', 'n': IDENTITY[0], 'panels': 1016, 'pairs_per_pass': 21264880, 'parameter_complete_equal': True, 'ledger_equal': True, 'strict_radius_tests': [183, 50], 'radius': final['radius']}.items():
        assert status[key] == value
    assert status == {'status': 'PASS', 'n': IDENTITY[0], 'panels': 1016, 'pairs_per_pass': 21264880, 'parameter_complete_equal': True, 'ledger_equal': True, 'identity_unchanged': True, 'full_returned_report_persisted': True, 'strict_radius_tests': [183, 50], 'radius': final['radius'], 'elapsed_seconds': status['elapsed_seconds']}
    save('complete-replay.json', {'status': 'PASS', 'n': IDENTITY[0], 'replay': report, 'immutable_ledger': counts, 'distinct_signed_checks': signed, 'parameter': parameter, 'kernel': final, 'sole_metadata_addition': 'n', 'producer_executed': False, 'strict_radius_powers': [183, 50]})
    state.update(stage='complete', panels=1016)
    save('status.json', {'status': 'PASS', 'state': state, 'elapsed_seconds': time.monotonic() - START})
    print(json.dumps({'n': IDENTITY[0], 'status': 'PASS', 'panels': 1016, 'coefficient_pairs': counts['coefficient_pairs'], 'strict_radius_powers': [183, 50]}), flush=True)
except BaseException as exc:
    save('first-failure.json', {'type': type(exc).__name__, 'message': str(exc), 'state': state, 'traceback': traceback.format_exc()})
    print(json.dumps({'n': IDENTITY[0], 'status': 'STOP', 'state': state, 'error': str(exc)}), flush=True)
    sys.exit(1)
