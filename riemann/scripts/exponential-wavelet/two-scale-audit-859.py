"""Exact checks of the full fixed C998 certificate and an unchanged replay.

No pair selection or retuning. Use --replay to regenerate a separate copy;
otherwise inspect the already saved replay. All record checks are saved.
"""
from fractions import Fraction as F
from math import factorial, isqrt
from pathlib import Path
import argparse
import contextlib
import hashlib
import json
import sys

BASE = Path(__file__).resolve().parent
SOURCE = BASE / 'two-scale-certificate-857.py'
ORIGINAL = BASE / 'two-scale-certificate-857.json'
REPLAY = BASE / 'two-scale-replay-859.json'
WITNESS = BASE / 'witness-857.json'
OUT = BASE / 'two-scale-audit-859.json'
args = argparse.ArgumentParser()
args.add_argument('--replay', action='store_true')
args = args.parse_args()
runtime = {'python': sys.version, 'replay_requested': args.replay}
if args.replay:
    source = SOURCE.read_text()
    old = "OUT=BASE/'two-scale-certificate-857.json'"
    new = "OUT=BASE/'two-scale-replay-859.json'"
    assert source.count(old) == 1
    ns = {'__file__': str(SOURCE), '__name__': '__main__'}
    with (BASE / 'two-scale-replay-859.log').open('w') as log:
        with contextlib.redirect_stdout(log):
            exec(compile(source.replace(old, new), str(SOURCE), 'exec'), ns)
    runtime['decimal_contexts'] = {
        name: {'precision': ns[name].prec, 'Emin': ns[name].Emin,
               'Emax': ns[name].Emax,
               'signals': {s.__name__: v for s, v in ns[name].flags.items()}}
        for name in ('LO', 'HI')}


class R:
    """Rational interval arithmetic, independent of Decimal rounding."""
    def __init__(self, a, b=None):
        if isinstance(a, R):
            self.a, self.b = a.a, a.b
        elif isinstance(a, list):
            self.a, self.b = map(F, a)
        else:
            self.a, self.b = F(a), F(a if b is None else b)
        assert self.a <= self.b

    def __add__(x, y):
        y = R(y)
        return R(x.a+y.a, x.b+y.b)
    __radd__ = __add__

    def __neg__(x):
        return R(-x.b, -x.a)

    def __sub__(x, y):
        return x + -R(y)

    def __rsub__(x, y):
        return R(y) + -x

    def __mul__(x, y):
        y = R(y)
        p = [a*b for a in (x.a, x.b) for b in (y.a, y.b)]
        return R(min(p), max(p))
    __rmul__ = __mul__

    def __truediv__(x, y):
        y = R(y)
        assert not y.a <= 0 <= y.b
        return x * R(1/y.b, 1/y.a)

    def __rtruediv__(x, y):
        return R(y) / x

    def contains(x, y):
        y = R(y)
        return x.a <= y.a <= y.b <= x.b


original = json.loads(ORIGINAL.read_text())
replay = json.loads(REPLAY.read_text())
witness = json.loads(WITNESS.read_text())
checks, failures = [], []


def check(name, condition):
    checks.append({'name': name, 'passed': bool(condition)})
    if not condition:
        failures.append(name)
    return bool(condition)


check('entire original equals entire replay', original == replay)
check('source hash', original['script_sha256'] == hashlib.sha256(SOURCE.read_bytes()).hexdigest())
check('witness hash', original['witness_sha256'] == hashlib.sha256(WITNESS.read_bytes()).hexdigest())
check('original checks and no failures', all(x['passed'] for x in original['checks']) and not original['failures'])
expected_c = [274,-403,56,268,-373,559,-483,32,603,-1000,732,-180]
expected_d = [-3,-37,191,-489,833,-974,709,-151,-325,429,-221,-24,131,-217,461,-723,652,-228,-117,-10,476,-681,208,602,-1000,734,-258,27]
for name, first in [('coarse_integer_coefficients', expected_c), ('fine_integer_coefficients', expected_d)]:
    check('canonical witness ' + name, witness[name] == first + first[::-1])
check('witness denominator', witness['denominator'] == 1000)

# The explicit polynomial formula supplies signs independently of the
# Decimal program's three-term recurrence. Its degree is exactly24.
n = 24
coeff = {n-2*k: F((-1)**k * factorial(2*n-2*k),
                   2**n * factorial(k)*factorial(n-k)*factorial(n-2*k))
         for k in range(n//2+1)}


def polynomial(x):
    return sum((c*x**j for j, c in coeff.items()), F(0))


root_records = []
previous = F(-1)
for j, row in enumerate(original['quadrature_roots']):
    x = R(row['root'])
    p, q = polynomial(x.a), polynomial(x.b)
    signs = check('exact root signs ' + str(j), p*q < 0)
    stored = check('root endpoint value enclosures ' + str(j), R(row['P_lower']).contains(p) and R(row['P_upper']).contains(q))
    separate = check('ordered interior root ' + str(j), previous < x.a < x.b < 1)
    previous = x.b
    # Exact interval recurrence verifies every directed derivative/weight
    # enclosure; the polynomial sign test above does not use this recurrence.
    p0, p1 = R(1), x
    for k in range(2, n+1):
        p0, p1 = p1, ((2*k-1)*x*p1-(k-1)*p0)/k
    derivative = n*(x*p1-p0)/(x*x-1)
    exact_weight = 2/((1-x*x)*derivative*derivative)
    weights = check('rational weight enclosure ' + str(j), R(row['weight']).contains(exact_weight) and R(row['weight']).a > 0)
    root_records.append({'index': j, 'bracket': row['root'],
                         'sign_lower': 1 if p > 0 else -1,
                         'sign_upper': 1 if q > 0 else -1,
                         'checks': [signs, stored, separate, weights]})
check('all24 roots', len(root_records) == n)

# Enumerate prime powers by factoring each integer, not by the producer's
# prime-and-power loop. Check all saved delays/weights in the full replay.
expected = []
for integer in range(2, 81):
    factors = []
    remaining = integer
    for p in range(2, isqrt(integer)+1):
        while remaining % p == 0:
            factors.append(p)
            remaining //= p
    if remaining > 1:
        factors.append(remaining)
    if len(set(factors)) == 1:
        expected.append((integer, factors[0]))
actual = [(r['n'], r['p']) for r in original['prime_powers']]
check('complete31 von Mangoldt pairs', actual == expected and len(actual) == 31)
check('positive delays and weights', all(R(r['delay']).a > 0 and R(r['weight']).a > 0 for r in original['prime_powers']))
check('Cprime encloses exact sum of recorded weights', R(original['Cprime']).contains(2*sum((R(r['weight']) for r in original['prime_powers']), R(0))))

panel_records = []
total = [R(0), R(0), R(0)]
previous = F(0)
for j, row in enumerate(original['panels']):
    left, right = R(row['left']), R(row['right'])
    required_width = F(1, 8) if j < 16 else F(1)
    ok = check('exact panel tiling ' + str(j), left.a == left.b == previous and right.a == right.b and right.a-left.a == required_width)
    previous = right.b
    total = [a+R(b) for a, b in zip(total, row['quadrature'])]
    panel_records.append({'index': j, 'left': row['left'], 'right': row['right'], 'tiling': ok})
check('complete526 panels reach512', len(panel_records) == 526 and previous == 512)
for j in range(3):
    check('exact panel sum enclosure ' + str(j), R(original['quadrature_sums'][j]).contains(total[j]))

# Independent rational Machin bounds and final error ledger.
def atan_bounds(k):
    partial = sum((F((-1)**j, (2*j+1)*k**(2*j+1)) for j in range(60)), F(0))
    error = F(1, 121*k**121)
    return R(partial-error, partial+error)


pi = 16*atan_bounds(5)-4*atan_bounds(239)
cg = F(factorial(24)**4, 49*factorial(48)**2)
check('Gauss coefficient and length', R(original['gauss_error']).contains(512*R(original['holomorphic_integrand_bound'])*cg))
for j, key in enumerate(['Q_u', 'Q_v', 'H_uv']):
    err = (R(original['gauss_error']) + R(original['tails_before_pi'][j])).b
    raw = R(original['quadrature_sums'][j])+R(-err, err)
    check('complete error ledger ' + key, R(original[key]).contains(raw/pi))
u, v, h = [R(original[k]) for k in ('Q_u', 'Q_v', 'H_uv')]
delta = R(original['four_H_squared_minus_Q_product'])
check('exact discriminant enclosure', delta.contains(4*h*h-u*v))
check('both diagonals and H positive', min(u.a, v.a, h.a) > 0)
check('half threshold rejected', delta.a > 0)
ratio = R(original['ratio'])
check('ratio lower endpoint justified by exact squaring', ratio.a > 0 and ratio.a**2*u.b*v.b <= h.a**2)
check('ratio upper endpoint justified by exact squaring', ratio.b**2*u.a*v.a >= h.b**2)
check('displayed conservative bounds', u.a > F('0.04111') and u.b < F('0.04516') and v.a > F('10.3564') and v.b < F('10.3967') and h.a > F('0.66574') and h.b < F('0.66825') and ratio.a > F('0.97'))
if 'decimal_contexts' in runtime:
    forbidden = ['InvalidOperation', 'DivisionByZero', 'Overflow', 'Underflow', 'Subnormal', 'Clamped', 'FloatOperation']
    check('no exceptional Decimal signals', all(not c['signals'][s] for c in runtime['decimal_contexts'].values() for s in forbidden))

report = {'status': 'PASS' if not failures else 'FAIL',
          'scope': 'C998 fixed pair; no new estimate or full-metric sign',
          'runtime': runtime, 'checks': checks, 'failures': failures,
          'root_records': root_records, 'prime_power_pairs': actual,
          'panel_records': panel_records,
          'Q_u': original['Q_u'], 'Q_v': original['Q_v'], 'H_uv': original['H_uv'],
          'discriminant': original['four_H_squared_minus_Q_product'],
          'ratio': original['ratio'], 'required': 'Q_u>0, Q_v>0 and 4H^2-Q_u*Q_v>0',
          'inputs_sha256': {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                            for p in (SOURCE, ORIGINAL, REPLAY, WITNESS)},
          'audit_script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
OUT.write_text(json.dumps(report, indent=2)+'\n')
print(json.dumps({k: report[k] for k in ['status', 'scope', 'Q_u', 'Q_v', 'H_uv', 'discriminant', 'ratio', 'required', 'failures']}, indent=2))
print('Checked', len(checks), 'conditions; complete evidence:', OUT)
sys.exit(bool(failures))
