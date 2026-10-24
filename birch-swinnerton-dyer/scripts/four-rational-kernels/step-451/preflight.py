import ast, copy, json, sys
from pathlib import Path
from types import SimpleNamespace
sys.dont_write_bytecode = True
import hashlib, copy
PRIMITIVES = ('floor_checked', 'ceil_checked', 'times', 'over', 'enclose', 'plus', 'opposite', 'intersect', 'product')

def fresh_counts():
    result = {k: 0 for k in ('floor', 'ceiling', 'multiply', 'divide', 'convert', 'plus', 'negate', 'clip', 'products', 'zero_operand_multiplications')}
    result['sign_cases'] = [0] * 9
    return result

def identity_for(index, output):
    fixed = (Path('scripts/four-rational-kernels/step-449') / ('n-' + str(index))).resolve()
    return (index, str(fixed), str(Path(output).resolve()), 'fixed_replay_451_' + str(index), hashlib.sha256((fixed / 'replay.py').read_bytes()).hexdigest())

def check_identity(identity, fixed, output, module, original_module):
    assert isinstance(identity, tuple) and len(identity) == 5
    assert type(identity[0]) is int and identity[0] in (23, 24, 25, 26)
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

def inert_module(identity):
    mod = SimpleNamespace(__name__=identity[3], __file__=str(Path(identity[1]) / 'replay.py'), SCALE=2 ** 256, LEDGER={})
    d = mod.SCALE

    def floor(num, den):
        return num // den

    def ceil(num, den):
        return -(-num // den)

    def times(a, b):
        vals = [x * y for x in a for y in b]
        mod.LEDGER['multiply'] = mod.LEDGER.get('multiply', 0) + 1
        return (mod.floor_checked(min(vals), d), mod.ceil_checked(max(vals), d))

    def over(a, k):
        return (mod.floor_checked(a[0], k), mod.ceil_checked(a[1], k))

    def enclose(num, den=1):
        return (mod.floor_checked(num * d, den), mod.ceil_checked(num * d, den))

    def plus(a, b):
        return (a[0] + b[0], a[1] + b[1])

    def opposite(a):
        return (-a[1], -a[0])

    def intersect(a, l, u):
        return (max(a[0], l), min(a[1], u))

    def product(a, b):
        assert all((x == (0, 0) for x in a + b))
        mod.LEDGER['coefficient_pairs'] = mod.LEDGER.get('coefficient_pairs', 0) + len(a) * len(b)
        return [(0, 0)] * (len(a) + len(b) - 1)
    for name, fn in zip(PRIMITIVES, (floor, ceil, times, over, enclose, plus, opposite, intersect, product), strict=True):
        setattr(mod, name, fn)
    return mod

def one(index, base, install):
    IDENTITY = identity_for(index, base / ('n-' + str(index)))
    OLD = Path(IDENTITY[1])
    OUT = Path(IDENTITY[2])
    n = -422
    before = (IDENTITY, OLD, OUT, n)
    replay = inert_module(IDENTITY)
    original_module = replay
    original_primitives = tuple((getattr(replay, k) for k in PRIMITIVES))
    original_keys = set(vars(replay))
    original_other = {k: v for k, v in vars(replay).items() if k not in PRIMITIVES and k != 'LEDGER'}
    signed = fresh_counts()
    callbacks = []

    def save(name, value):
        callbacks.append((name, copy.deepcopy(value)))
    check_identity(IDENTITY, OLD, OUT, replay, original_module)
    wrappers = install(replay, replay.SCALE, signed, save)
    assert before == (IDENTITY, OLD, OUT, n) and n == -422
    check_identity(IDENTITY, OLD, OUT, replay, original_module)
    assert set(vars(replay)) == original_keys
    assert {k: v for k, v in vars(replay).items() if k not in PRIMITIVES and k != 'LEDGER'} == original_other
    captures = check_captures(replay, wrappers, original_primitives, signed, replay.SCALE)
    expected = fresh_counts()
    expected.update(floor=57, ceiling=57, multiply=36, zero_operand_multiplications=11)
    expected['sign_cases'] = [9, 6, 3, 6, 4, 2, 3, 2, 1]
    assert callbacks == [('primitive-controls.json', expected)]
    assert signed == fresh_counts() and replay.LEDGER == {}
    d = replay.SCALE
    assert replay.floor_checked(-4, 3) == -2 and replay.ceil_checked(-4, 3) == -1
    assert replay.times((-d, d), (0, d)) == (-d, d)
    assert replay.over((-4, 4), 3) == (-2, 2)
    assert replay.enclose(0) == (0, 0)
    assert replay.plus((-1, 0), (0, 1)) == (-1, 1)
    assert replay.opposite((-1, 2)) == (-2, 1)
    assert replay.intersect((-d, d), 0, d) == (0, d)
    assert replay.product([(0, 0)] * 129, [(0, 0)] * 65) == [(0, 0)] * 193
    assert signed['products'] == 1 and replay.LEDGER['coefficient_pairs'] == 8385
    assert before == (IDENTITY, OLD, OUT, n) and len(callbacks) == 1
    check_identity(IDENTITY, OLD, OUT, replay, original_module)
    return {'n': index, 'identity': IDENTITY, 'sentinel': n, 'status': 'PASS', 'all_nine_replacements': True, 'captures': captures, 'controls': expected, 'post_return_counts': copy.deepcopy(signed), 'post_return_ledger': copy.deepcopy(replay.LEDGER), 'kernel_executed': False, 'callbacks': len(callbacks)}

def preflight(base, installer_source):
    ns = {}
    exec(compile(installer_source, 'installer-preflight-422', 'exec', flags=0, dont_inherit=True, optimize=0), ns)
    results = []
    for index in (23, 24, 25, 26):
        results.append(one(index, base, ns['install']))
    assert len({row['identity'][3] for row in results}) == 4
    return results
