"""Complete independent arithmetic audit of C759c, with originals read-only.

Basic arithmetic uses exact Fraction endpoints, rounded OUTWARD to the
rational grid 10^-90 after each operation. Transcendentals alone use
110-digit outward-expanded Decimal evaluations. All 349 saved rows are
checked, not sampled. Analytic justification is canonical in C759c.
"""
from contextlib import redirect_stdout
from decimal import Decimal, Context, ROUND_FLOOR, ROUND_CEILING, localcontext
from fractions import Fraction as F
from pathlib import Path
import hashlib
import io
import json
import runpy

BASE = Path(__file__).resolve().parent
SOURCE = BASE / 'weighted-fourier-deficit-802.py'
SAVED = BASE / 'weighted-fourier-deficit-802.json'
OUT = BASE / 'audit-804'
OUT.mkdir(exist_ok=True)
saved_bytes = SAVED.read_bytes()
source_bytes = SOURCE.read_bytes()
saved = json.loads(saved_bytes)
GRID = 10**90
DOWN = Context(prec=110, rounding=ROUND_FLOOR)
UP = Context(prec=110, rounding=ROUND_CEILING)
checks, failures = [], []


def down(q):
    q = F(q)*GRID
    return F(q.numerator//q.denominator, GRID)


def up(q):
    q = F(q)*GRID
    return F(-((-q.numerator)//q.denominator), GRID)


class R:
    def __init__(self, a=0, b=None):
        if isinstance(a, R):
            self.lo, self.hi = a.lo, a.hi
        else:
            self.lo, self.hi = down(a), up(a if b is None else b)
        assert self.lo <= self.hi

    def __add__(a, b):
        b = R(b)
        return R(a.lo+b.lo, a.hi+b.hi)

    __radd__ = __add__

    def __neg__(a):
        return R(-a.hi, -a.lo)

    def __sub__(a, b):
        return a + -R(b)

    def __rsub__(a, b):
        return R(b) + -a

    def __mul__(a, b):
        b = R(b)
        ends = [x*y for x in (a.lo, a.hi) for y in (b.lo, b.hi)]
        return R(min(ends), max(ends))

    __rmul__ = __mul__

    def __truediv__(a, b):
        b = R(b)
        assert not b.lo <= 0 <= b.hi
        return a * R(1/b.hi, 1/b.lo)

    def __rtruediv__(a, b):
        return R(b)/a

    def __pow__(a, n):
        assert isinstance(n, int) and n >= 0
        value = R(1)
        for _ in range(n):
            value *= a
        return value

    def positive_part(a):
        return R(max(F(0), a.lo), max(F(0), a.hi))


def decimal_endpoint(q, context):
    return context.divide(Decimal(q.numerator), Decimal(q.denominator))


def transc(x, operation):
    x = R(x)
    lo = decimal_endpoint(x.lo, DOWN)
    hi = decimal_endpoint(x.hi, UP)
    if operation in ('ln', 'sqrt'):
        assert lo > 0
    a = DOWN.next_minus(getattr(DOWN, operation)(lo))
    b = UP.next_plus(getattr(UP, operation)(hi))
    return R(F(a), F(b))


def exact_decimal(q):
    # Every endpoint lies on the fixed rational grid; no decimal rounding.
    v = q*GRID
    assert v.denominator == 1
    n = v.numerator
    s = str(abs(n)).rjust(91, '0')
    return ('-' if n < 0 else '') + s[:-90] + '.' + s[-90:]


def interval(x):
    x = R(x)
    return [exact_decimal(x.lo), exact_decimal(x.hi)]


def check(name, condition, detail=None):
    passed = bool(condition)
    checks.append({'name': name, 'passed': passed, 'detail': detail})
    if not passed:
        failures.append(name)


def enclosure(pointer, value):
    node = saved
    for key in pointer.split('/'):
        node = node[int(key)] if isinstance(node, list) else node[key]
    lo, hi = map(F, node)
    value = R(value)
    check(pointer, lo <= value.lo <= value.hi <= hi,
          {'independent_interval': interval(value), 'saved_interval': node})


def atan(k):
    center = sum((F((-1)**j, (2*j+1)*k**(2*j+1))
                  for j in range(60)), F(0))
    radius = F(1, 121*k**121)
    return R(center-radius, center+radius)


# Replay the original in an isolated output directory at hostile precision.
copy = OUT / SOURCE.name
copy.write_bytes(source_bytes)
with localcontext() as ambient, redirect_stdout(io.StringIO()) as replay_log:
    ambient.prec = 7
    runpy.run_path(str(copy), run_name='__main__')
(OUT/'replay.txt').write_text(replay_log.getvalue())
check('unchanged_replay_bytes', copy.with_suffix('.json').read_bytes() == saved_bytes)
check('source_hash', hashlib.sha256(source_bytes).hexdigest() == saved['script_sha256'])
check('saved_failures_empty', saved['failures'] == [])
check('saved_checks_all_true', all(saved['checks'].values()))
check('fixed_parameters', saved['N'] == 120 and saved['cutoff'] == 350
      and saved['rectangle_width'] == 1 and saved['precision'] == 60)

pi = 16*atan(5)-4*atan(239)
edge = 121*pi
m_floor = -transc(4*pi, 'ln')-4


def h(t):
    return transc(R(t)/(2*pi), 'ln')-F(2, t*t)


def tail(t):
    gap = 1-(R(t)/edge)**2
    check(f'domain/tail/{t}', gap.lo > 0, {'gap': interval(gap)})
    return 4/(120*pi**2*gap**2)


for key, value in [('pi', pi), ('m_floor', m_floor),
                   ('first_omitted_frequency', edge), ('h_cutoff', h(350))]:
    enclosure('constants/'+key, value)
check('support/h350_above4', h(350).lo > 4)
check('support/350_below121pi', 350 < edge.lo)
check('support/nonnegative_global_deficit_bound', (4-m_floor).lo > 0)

origin = (4-m_floor)*tail(1)/pi
enclosure('origin_rectangle', origin)
total = origin
check('complete_rectangle_count', len(saved['rectangles']) == 349)
positive_rows, zero_rows, unresolved_rows = [], [], []
for k in range(1, 350):
    row = saved['rectangles'][k-1]
    check(f'rectangles/{k-1}/index', row['left'] == k and row['right'] == k+1)
    raw_deficit = 4-h(k)
    if raw_deficit.lo > 0:
        positive_rows.append(k)
    elif raw_deficit.hi < 0:
        zero_rows.append(k)
    else:
        unresolved_rows.append(k)
    deficit = raw_deficit.positive_part()
    all_modes = tail(k+1)
    rectangle = deficit*all_modes/pi
    for key, value in [('deficit_upper_function', deficit),
                       ('all_modes_tail_majorant', all_modes),
                       ('rectangle', rectangle)]:
        enclosure(f'rectangles/{k-1}/{key}', value)
    check(f'rectangles/{k-1}/nonnegative', rectangle.lo >= 0)
    total += rectangle
check('all_positive_part_branches_resolved', unresolved_rows == [])

C = R(0)
check('complete_prime_count', len(saved['prime_rows']) == 5)
for i, (n, p) in enumerate([(2, 2), (3, 3), (4, 2), (5, 5), (7, 7)]):
    row = saved['prime_rows'][i]
    check(f'prime_rows/{i}/integers', row['n'] == n and row['p'] == p)
    weight = transc(p, 'ln')/transc(n, 'sqrt')
    chain = transc(2, 'sqrt') if n == 2 else R(1)
    enclosure(f'prime_rows/{i}/weight', weight)
    enclosure(f'prime_rows/{i}/chain_norm', chain)
    check(f'prime_rows/{i}/positive', weight.lo > 0 and chain.lo > 0)
    C += weight*chain
check('prime_support_and_chains', transc(7, 'ln').hi < 2 < transc(8, 'ln').lo
      and (2*transc(2, 'ln')).hi < 2 < (3*transc(2, 'ln')).lo
      and transc(3, 'ln').lo > 1)

sinh_half = (transc(F(1, 2), 'exp')-transc(F(-1, 2), 'exp'))/2
P = 8*sinh_half**2/(120*pi**2)
tau = R(F(11, 200))
threshold = 4-C-P-tau
shifted = threshold-total
unshifted = 4-total-C-P
values = {'upper_majorant_B': total, 'C': C, 'P_120': P, 'tau': tau,
          'required_trace_threshold': threshold,
          'unshifted_floor': unshifted, 'shifted_floor': shifted}
for key, value in values.items():
    enclosure('bounds/'+key, value)
check('trace_enclosure_normalization', saved['bounds']['trace_enclosure'] ==
      ['0', saved['bounds']['upper_majorant_B'][1]])
for key, lo, hi in [
    ('upper_majorant_B', '0.52800039426954205', '0.52800039426954207'),
    ('required_trace_threshold', '0.81391352324016218', '0.81391352324016219'),
    ('shifted_floor', '0.28591312897062012', '0.28591312897062013')]:
    a, b = map(F, saved['bounds'][key])
    check('published/'+key, F(lo) < a <= b < F(hi))
check('published/strict_comparison', 0 <= total.lo <= total.hi < F('0.529')
      < F('0.8139') < threshold.lo)
check('published/unshifted_floor', unshifted.lo > F('0.3409'))
check('published/shifted_floor', shifted.lo > F('0.2859'))
check('original_artifacts_unchanged', SAVED.read_bytes() == saved_bytes
      and SOURCE.read_bytes() == source_bytes)

result = {
    'task': 'C759c complete arithmetic audit; analytic audit in its canonical proof',
    'classification': 'REPRODUCTION',
    'audit_script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'source_sha256': hashlib.sha256(source_bytes).hexdigest(),
    'saved_certificate_sha256': hashlib.sha256(saved_bytes).hexdigest(),
    'method': 'Exact Fraction interval operations, outward rational grid 10^-90; '
              '110-digit outward Decimal transcendental endpoints; exact Machin series',
    'replay': 'scripts/spectral-triples/audit-804/weighted-fourier-deficit-802.json',
    'complete_rectangle_count': 349,
    'positive_part_branches': {'positive_left_endpoints': positive_rows,
                               'zero_left_endpoints': zero_rows,
                               'unresolved': unresolved_rows},
    'bounds': {key: interval(value) for key, value in values.items()},
    'check_count': len(checks), 'checks': checks, 'failures': failures,
    'conclusion': 'C759c arithmetic claims retained' if not failures else 'audit failed',
    'limitations': ['Trace itself is only bounded by B, not evaluated.',
                   'The analytic proof is not established by generator replay.',
                   'Python integers/Fraction and Decimal correctness are trust assumptions.',
                   'Coupling, Schur sign, parity and Xi bridges remain unresolved.'],
}
output = BASE/'weighted-fourier-deficit-audit-804.json'
output.write_text(json.dumps(result, indent=2)+'\n')
print('349 complete rectangles; checks:', len(checks), '; failures:', failures)
for key in ('upper_majorant_B', 'required_trace_threshold', 'shifted_floor'):
    print(key, result['bounds'][key])
print('Full certificate:', output.as_posix())
if failures:
    raise SystemExit(1)
