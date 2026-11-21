#!/usr/bin/env python3
"""Replay L682 and independently enclose every rational boundary sample.

The independent calculation uses rectangular complex intervals at 10^60
and 120 powers, rather than the original scalar rounding-error estimate.
The analytic extension between samples is audited in the canonical lemma.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent
SOURCE = HERE / 'highest-spatial-contour-certificate.py'
ORIGINAL = SOURCE.with_suffix('.json')
OUTPUT = Path(__file__).with_suffix('.json')
SCALE = 10**60
DEGREE = 120
failures = []


def floorq(v):
    return v.numerator * SCALE // v.denominator


def ceilq(v):
    return -((-v.numerator * SCALE) // v.denominator)


def scalar(v):
    return floorq(v), ceilq(v)


def plus(a, b):
    return a[0] + b[0], a[1] + b[1]


def minus(a, b):
    return a[0] - b[1], a[1] - b[0]


def times(a, b):
    products = [x*y for x in a for y in b]
    return min(products) // SCALE, -((-max(products)) // SCALE)


def divide_positive(a, k):
    return a[0] // k, -((-a[1]) // k)


def complex_times(a, b):
    return (minus(times(a[0], b[0]), times(a[1], b[1])),
            plus(times(a[0], b[1]), times(a[1], b[0])))


TAIL = Q(9, 10)**(DEGREE+1) / ((DEGREE+1)*(DEGREE+2)*Q(1, 10))
TAIL_SCALED = ceilq(TAIL)


def series(z):
    if z[0]**2 + z[1]**2 > Q(81, 100):
        raise ValueError('series radius exceeds 9/10')
    iz = scalar(z[0]), scalar(z[1])
    power = ((SCALE, SCALE), (0, 0))
    result = (0, 0)
    for k in range(1, DEGREE+1):
        power = complex_times(power, iz)
        result = plus(result, divide_positive(power[0], k*(k+1)))
    return result[0]-TAIL_SCALED, result[1]+TAIL_SCALED


def log_unit(v):
    assert 1 <= v <= 2
    w = (v-1)/(v+1)
    lower = 2*sum((w**(2*j+1)/Q(2*j+1) for j in range(40)), Q(0))
    return lower, lower + 2*w**81/(81*(1-w*w))


def log_enclosure(v):
    assert v > 0
    shift = 0
    while v < 1:
        v *= 2
        shift -= 1
    while v > 2:
        v /= 2
        shift += 1
    lo, hi = log_unit(v)
    a, b = log_unit(Q(2))
    return lo+min(shift*a, shift*b), hi+max(shift*a, shift*b)


source_bytes = SOURCE.read_bytes()
old_bytes = ORIGINAL.read_bytes()
old = json.loads(old_bytes)
with tempfile.TemporaryDirectory(prefix='l682-audit-') as temp:
    copy = Path(temp) / SOURCE.name
    copy.write_bytes(source_bytes)
    run = subprocess.run([sys.executable, str(copy)], capture_output=True, text=True)
    replay_path = copy.with_suffix('.json')
    replay_bytes = replay_path.read_bytes() if replay_path.exists() else b''
    replay = json.loads(replay_bytes) if replay_bytes else None
    replay_matches = run.returncode == 0 and replay == old
    if not replay_matches:
        failures.append('complete original replay mismatch or nonzero exit')
    # Retain all changed replay evidence if a mismatch ever occurs.
    if not replay_matches:
        OUTPUT.with_name(OUTPUT.stem+'-failed-replay.json').write_bytes(replay_bytes)

# Independent coverage enumeration: spatial edges, halves, and both charts.
positions = ([('vertical', s, Q(j, 100))
              for s in (Q(-9, 100), Q(9, 100)) for j in range(0, 46, 3)]
             + [('horizontal', Q(j, 100), Q(9, 20)) for j in range(-9, 10, 3)])
expected_rows = [(kind, str(s), str(y), sign)
                 for kind, s, y in positions for sign in (-1, 1)]
actual_rows = [(r['kind'], r['s'], r['y'], r['real_part_sign']) for r in old['rows']]
if actual_rows != expected_rows or len(old['rows']) != 78:
    raise ValueError('original mesh does not equal independently enumerated cover')

d, U = Q(5, 4), Q(121, 64)
angles = {}
for sign in (-1, 1):
    for j in range(-80, 81):
        v = Q(j, 80)
        re, im = sign*(1-v*v)/(1+v*v), 2*v/(1+v*v)
        assert re*re+im*im == 1
        base = minus(series((-d*re/U, d*im/U)), series((-re/d, -im/d)))
        angles[sign, j] = re, im, base

rows = []
global_old_max = None
global_independent_max = None
min_dominance = None
sample_count = 0
interpolation = Q(8, 8)*Q(3, 100)**2 + Q(130, 8)*Q(1, 80)**2
for index, row in enumerate(old['rows']):
    s, y = Q(row['s']), Q(row['y'])
    a = -d+s
    a2 = a*a+y*y
    l1, h1 = log_enclosure(d*d/a2)
    l2, h2 = log_enclosure(a2/U)
    damping = Q(20, 9)*max(s, 0)
    const = floorq(l1/2+l2/6-damping), ceilq(h1/2+h2/6-damping)
    lows, highs = [], []
    if len(row['sample_upper_numerators']) != 161:
        raise ValueError('wrong sample count')
    for offset, j in enumerate(range(-80, 81)):
        re, im, base = angles[row['real_part_sign'], j]
        za = ((re*a+im*y)/a2, (im*a-re*y)/a2)
        zb = ((a*re+y*im)/U, (y*re-a*im)/U)
        enclosure = plus(const, minus(plus(series(za), base), series(zb)))
        lo, hi = enclosure
        assert lo <= hi
        lows.append(lo)
        highs.append(hi)
        stored = Q(row['sample_upper_numerators'][offset], row['sample_scale'])
        dominance = stored-Q(hi, SCALE)
        min_dominance = dominance if min_dominance is None else min(min_dominance, dominance)
        if dominance < 0:
            failures.append(f'original bound not independently certified: row={index}, j={j}')
        global_old_max = stored if global_old_max is None else max(global_old_max, stored)
        global_independent_max = hi if global_independent_max is None else max(global_independent_max, hi)
        sample_count += 1
    stored_max = max(Q(v, row['sample_scale']) for v in row['sample_upper_numerators'])
    if (Q(row['sampled_max_upper']) != stored_max
            or Q(row['interpolation_error']) != interpolation
            or Q(row['certified_upper']) != stored_max+interpolation):
        failures.append(f'row {index} summary or interpolation mismatch')
    rows.append({'original_row_index': index, 'kind': row['kind'],
                 's': row['s'], 'y': row['y'], 'real_part_sign': row['real_part_sign'],
                 'v_numerators': list(range(-80, 81)), 'v_denominator': 80,
                 'sample_lower_numerators': lows, 'sample_upper_numerators': highs})

actual = global_old_max + interpolation
independent_actual = Q(global_independent_max, SCALE) + interpolation
required = -Q(7, 200)
if actual != Q(old['actual_upper']) or actual >= required or independent_actual >= required:
    failures.append('full contour maximum comparison failed')
if sample_count != 12558:
    failures.append('sample census failed')
check_failures = []
for check in old['checks']:
    left, right = Q(check['lhs']), Q(check['rhs'])
    truth = {'<': left < right, '>': left > right, '=': left == right}[check['op']]
    if not truth or truth != check['passed']:
        check_failures.append(check['name'])
failures.extend(check_failures)
if old['failures'] or old['status'] != 'PASS':
    failures.append('original reports failure')

certificate = {
    'status': 'PASS' if not failures else 'FAIL', 'failures': failures,
    'source_sha256': hashlib.sha256(source_bytes).hexdigest(),
    'original_sha256': hashlib.sha256(old_bytes).hexdigest(),
    'replay_sha256': hashlib.sha256(replay_bytes).hexdigest(),
    'full_replay_matches': replay_matches, 'replay_exit_code': run.returncode,
    'sample_count': sample_count, 'row_count': len(rows),
    'scale': SCALE, 'degree': DEGREE, 'series_tail_per_sum': str(TAIL),
    'all_original_sample_upper_bounds_dominate_independent_enclosures': min_dominance >= 0,
    'minimum_dominance': str(min_dominance),
    'maximum_sample_upper': str(global_old_max),
    'interpolation_error': str(interpolation),
    'actual_upper': str(actual), 'required_upper': str(required),
    'strict_margin': str(required-actual),
    'independent_actual_upper': str(independent_actual),
    'arithmetic_check_count': len(old['checks']),
    'arithmetic_check_failures': check_failures,
    'rows': rows,
}
OUTPUT.write_text(json.dumps(certificate, indent=2)+'\n')
print(f"status={certificate['status']}; replay_matches={replay_matches}; "
      f"all {sample_count} sample enclosures and {len(old['checks'])} arithmetic checks inspected")
print(f'actual={actual}; required < {required}; margin={required-actual}')
print(f'minimum sample dominance > 0: {min_dominance > 0}; failures={failures}')
print(f'complete independent enclosures: {OUTPUT}')
raise SystemExit(1 if failures else 0)
