"""Independent rational audit of L819; preserve every step602 artifact.

Run from the riemann notebook. No old arithmetic implementation is imported.
The original program runs separately only for a complete byte-for-byte replay.
"""
from fractions import Fraction as F
from pathlib import Path
from math import comb
import hashlib
import json
import shutil
import subprocess
import sys


BASE = Path(__file__).resolve().parents[2]
DEST = BASE / 'scripts/central-jacobi/audit-604'
DEST.mkdir(exist_ok=True)
GRID = 10**70
checks = []
division_checks = []


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def closed(lo, hi):
    """Outward projection to integer multiples of 10^-70, using integers only."""
    lo, hi = F(lo), F(hi)
    assert lo <= hi
    a, b = lo * GRID, hi * GRID
    return (F(a.numerator // a.denominator, GRID),
            F(-((-b.numerator) // b.denominator), GRID))


def scalar(v):
    return (F(v), F(v))


def plus(a, b):
    return closed(a[0] + b[0], a[1] + b[1])


def minus(a, b):
    return closed(a[0] - b[1], a[1] - b[0])


def times(a, b):
    candidates = [a[0]*b[0], a[0]*b[1], a[1]*b[0], a[1]*b[1]]
    return closed(min(candidates), max(candidates))


def quotient(a, b):
    good = b[0] > 0 or b[1] < 0
    division_checks.append({'denominator': record(b), 'excludes_zero': good})
    assert good, 'division by interval containing zero'
    candidates = [x/y for x in a for y in b]
    return closed(min(candidates), max(candidates))


def scaled(a, v):
    return times(a, scalar(v))


def power(a, n):
    result = scalar(1)
    for _ in range(n):
        result = times(result, a)
    return result


def total(items):
    result = scalar(0)
    for item in items:
        result = plus(result, item)
    return result


def record(v):
    return [str(v[0]), str(v[1])]


def check_bool(name, passed, **evidence):
    checks.append({'name': name, 'pass': bool(passed), **evidence})


def bound(name, value, lower, upper):
    lower, upper = F(lower), F(upper)
    good = lower < value[0] <= value[1] < upper
    check_bool(name, good, actual_closed_interval=record(value),
               required_open_interval=[str(lower), str(upper)])


source = BASE / 'scripts/central-jacobi/discrete_pairing_602.py'
input_path = BASE / 'lemmas/L791-fixed-central-five-root-jacobi-model.md'
old_path = BASE / 'scripts/central-jacobi/discrete-pairing-certificate-602.json'
first_path = BASE / 'scripts/central-jacobi/discrete-pairing-first-pass-602.json'
old = json.loads(old_path.read_text())
first = json.loads(first_path.read_text())
original_hashes = {str(p.relative_to(BASE)): sha(p)
                   for p in (source, input_path, old_path, first_path)}
check_bool('saved program hash', old['program_sha256'] == sha(source))
check_bool('saved input hash', old['input_sha256'] == sha(input_path))

# An isolated working directory preserves both original output and its inputs.
replay = DEST / 'replay'
(replay / 'lemmas').mkdir(parents=True, exist_ok=True)
shutil.copyfile(source, replay / source.name)
shutil.copyfile(input_path, replay / 'lemmas' / input_path.name)
proc = subprocess.run([sys.executable, source.name], cwd=replay,
                      text=True, capture_output=True)
(DEST / 'replay.log').write_text(proc.stdout + proc.stderr)
replayed_path = replay / old_path.name
check_bool('original replay exit', proc.returncode == 0, returncode=proc.returncode)
check_bool('complete byte-identical original certificate replay',
           replayed_path.is_file() and replayed_path.read_bytes() == old_path.read_bytes())

# The inputs and proof thresholds below are transcribed from L819, not imported
# from the old generator. Compare the exact endpoints with the saved record.
q = [tuple(map(F, endpoints)) for endpoints in [
    ('1.07484394250019421126346157158', '1.07484394250019421126346157162'),
    ('1.06274366627144916855311401273', '1.06274366627144916855311401285'),
    ('1.05430333113463476927545484495', '1.05430333113463476927545484516')]]
check_bool('exact q endpoints', [record(v) for v in q] == old['q'])
Q, R, Z = q
S = times(R, Z)

# Solve all three affine equations for (p,s,t), with constant and r terms
# as simultaneous right-hand sides. This is independent of K/H and -J/H.
matrix = [
    [scalar(-1), Q, scaled(Q, -1), minus(Q, scalar(1)), scalar(-1)],
    [scaled(R, -1), scalar(1), scalar(1), minus(R, scalar(1)), R],
    [scaled(S, -2), scalar(2), scalar(4), minus(S, scalar(1)), scaled(S, 4)]]
pivots = []
for k in range(3):
    pivot = matrix[k][k]
    pivots.append(record(pivot))
    matrix[k] = [quotient(v, pivot) for v in matrix[k]]
    for i in range(3):
        if i == k:
            continue
        factor = matrix[i][k]
        matrix[i] = [minus(matrix[i][j], times(factor, matrix[k][j]))
                     for j in range(5)]
p0, p1 = matrix[0][3:]
s0, s1 = matrix[1][3:]
t0, t1 = matrix[2][3:]
H = minus(times(R, minus(scalar(3), scaled(Z, 2))), quotient(scalar(1), Q))
affine = dict(H=H, p0=p0, p1=p1, s0=s0, s1=s1, t0=t0, t1=t1)

first_bound_index = len(checks)
bound('H', H, '.01695', '.01696')
bound('p0', p0, '.10944', '.10945')
bound('p1', p1, '21.422', '21.423')
bound('p0*p1', times(p0, p1), '2.34', '2.35')
bound('t0', t0, '.003799', '.003800')

coefficient_bounds = {
    1: [('-0.002811', '-0.002810'), ('.0375', '.0376'), ('.723', '.724'),
        ('6.838', '6.839'), ('23.829', '23.830')],
    2: [('-0.000923', '-0.000922'), ('.0920', '.0921'), ('1.659', '1.660'),
        ('15.416', '15.417'), ('52.487', '52.488')],
    3: [('.001087', '.001088'), ('.1570', '.1571'), ('2.814', '2.815'),
        ('25.743', '25.744'), ('85.974', '85.975')]}

# Ns=s1*v^2+b*v-s0 and Nt=t1*v^2+h*v-t0. Expand P_m directly,
# without polynomial multiplication or the original Horner shift routine.
b = minus(times(s0, p1), times(s1, p0))
h = minus(times(t0, p1), times(t1, p0))
polynomials = {}
for m in (1, 2, 3):
    coefficients = [scaled(t0, -1),
        total([s0, h, scaled(t0, 2*m)]),
        total([scalar(-1), scaled(s0, -m), scaled(b, -1), t1,
               scaled(h, -2*m), scaled(t0, -m*m)]),
        total([p1, scaled(s1, -1), scaled(b, m), scaled(t1, -2*m), scaled(h, m*m)]),
        total([scaled(s1, m), scaled(t1, m*m)])]
    shifted = [total([scaled(times(coefficients[j], power(p0, j-i)), comb(j, i))
                      for j in range(i, 5)]) for i in range(5)]
    polynomials[str(m)] = {'c_coefficients': list(map(record, coefficients)),
                          'c_minus_p0_coefficients': list(map(record, shifted))}
    for i, (lo, hi) in enumerate(coefficient_bounds[m]):
        bound('P%d shifted coefficient %d' % (m, i), shifted[i], lo, hi)


def factored_endpoint(c, m):
    E = minus(times(p1, c), scalar(1))
    cr = times(c, minus(c, p0))
    Ns = plus(times(s0, E), times(s1, cr))
    Nt = plus(times(t0, E), times(t1, cr))
    w = minus(scalar(1), scaled(c, m))
    return total([times(power(c, 2), E), scaled(times(times(c, w), Ns), -1),
                  times(power(w, 2), Nt)])


cases = {}
for m, lo, hi, nlo, nhi in [
        (1, '.14677442', '.14677444', '40.17', '40.20'),
        (2, '.11802777', '.11802778', '149.38', '149.40')]:
    c = (F(lo), F(hi))
    left, right = factored_endpoint(scalar(lo), m), factored_endpoint(scalar(hi), m)
    bound('P%d left endpoint' % m, left, '-.0000001', '0')
    bound('P%d right endpoint' % m, right, '0', '.0000001')
    cp = minus(c, p0)
    E = minus(times(p1, c), scalar(1))
    w = minus(scalar(1), scaled(c, m))
    a = quotient(cp, E)
    Nt = plus(times(t0, E), times(t1, times(c, cp)))
    # Direct cleared-denominator formula, then a single difference quotient.
    x = quotient(times(Nt, w), times(c, E))
    other = quotient(minus(x, a), times(a, x))
    for name, value, lower, upper in [
            ('c-p0', cp, '.008', '.04'), ('p1*c-1', E, '1.5', '2.2'),
            ('1-m*c', w, '.7', '.9'), ('a', a, '.005', '.02'),
            ('x', x, '.03', '.07'), ('other gap', other, nlo, nhi)]:
        bound('m=%d %s' % (m, name), value, lower, upper)
    cases[str(m)] = {'c': record(c), 'a': record(a), 'x': record(x),
                     'other_gap': record(other), 'endpoint_values': [record(left), record(right)]}

independent_comparisons = checks[first_bound_index:]
check_bool('all 36 original comparison specifications accounted for',
           len(independent_comparisons) == 36 and
           [(c['name'], c['required_open_interval']) for c in independent_comparisons] ==
           [(c['name'], c['required_open_interval']) for c in old['checks']])

# Check the complete saved rational values, not only the saved passing flags.
def old_interval(pair):
    lo, hi = map(F, pair)
    assert lo <= hi
    return lo, hi


saved_values = {k: old_interval(old['affine'][k]) for k in ('H', 'p0', 'p1', 't0')}
saved_values['p0*p1'] = times(old_interval(old['affine']['p0']), old_interval(old['affine']['p1']))
for m in (1, 2, 3):
    values = old['polynomials'][str(m)]['c_minus_p0_coefficients']
    check_bool('saved P%d has no degree above four' % m,
               len(values) >= 5 and all(old_interval(v) == (0, 0) for v in values[5:]))
    for i in range(5):
        saved_values['P%d shifted coefficient %d' % (m, i)] = old_interval(values[i])
for m in (1, 2):
    saved = old['cases'][str(m)]
    c = old_interval(saved['c'])
    saved_values['P%d left endpoint' % m] = old_interval(saved['endpoint_values'][0])
    saved_values['P%d right endpoint' % m] = old_interval(saved['endpoint_values'][1])
    for name, v in [('c-p0', minus(c, old_interval(old['affine']['p0']))),
                    ('p1*c-1', minus(times(old_interval(old['affine']['p1']), c), scalar(1))),
                    ('1-m*c', minus(scalar(1), scaled(c, m))),
                    ('a', old_interval(saved['a'])), ('x', old_interval(saved['x'])),
                    ('other gap', old_interval(saved['other_gap']))]:
        saved_values['m=%d %s' % (m, name)] = v
saved_comparisons = []
for spec in old['checks']:
    value = saved_values[spec['name']]
    lower, upper = map(F, spec['required_open_interval'])
    passed = lower < value[0] <= value[1] < upper
    saved_comparisons.append({'name': spec['name'], 'actual_closed_interval': record(value),
                             'required_open_interval': spec['required_open_interval'], 'pass': passed})
check_bool('complete saved bounds independently compared',
           len(saved_comparisons) == 36 and all(v['pass'] for v in saved_comparisons))

# Preserve and explain the historical failure. No first-pass program is saved,
# so its different program hash is recorded, not claimed to have been replayed.
first_failed_specs = [v for v in first['checks'] if not v['pass']]
check_bool('first-pass failure is exactly the old x lower threshold',
           first['failures'] == ['m=2 x'] and len(first_failed_specs) == 1 and
           first_failed_specs[0]['name'] == 'm=2 x' and
           first_failed_specs[0]['required_open_interval'] == ['1/25', '7/100'])
check_bool('first-pass mathematical fields unchanged by threshold correction',
           all(first[k] == old[k] for k in ('q', 'affine', 'polynomials', 'cases', 'input_sha256')))
first_x = old_interval(first['cases']['2']['x'])
check_bool('first-pass x interval is strictly below 0.04 but above 0.03',
           F('.03') < first_x[0] <= first_x[1] < F('.04'), actual=record(first_x))
new_x = tuple(map(F, cases['2']['x']))
check_bool('independent x interval confirms the same threshold issue',
           F('.03') < new_x[0] <= new_x[1] < F('.04'), actual=record(new_x))

check_bool('all original artifacts preserved',
           all(sha(BASE / path) == value for path, value in original_hashes.items()))
failures = [c['name'] for c in checks if not c['pass']]
report = {
    'qualification': 'L819 finite arithmetic audit only; conceptual proof is in the canonical lemma. L791 contracts retained.',
    'result': 'FAIL' if failures else 'PASS', 'failures': failures,
    'program_sha256': sha(Path(__file__)), 'original_hashes': original_hashes,
    'first_pass_program_sha256_unreplayed': first['program_sha256'],
    'arithmetic': 'Python integers/Fraction; outward integer grid 10^-70; no original implementation import',
    'q': list(map(record, q)), 'gaussian_pivots': pivots,
    'affine': {k: record(v) for k, v in affine.items()},
    'polynomials': polynomials, 'cases': cases, 'division_checks': division_checks,
    'independent_comparison_count': len(independent_comparisons),
    'saved_comparisons': saved_comparisons, 'checks': checks,
    'threshold': 'For d>=5 the designated gap is an integer 1 or 2; other gap <149.40<150 and >d-2 imply d<=151.'}
path = DEST / 'audit-report.json'
path.write_text(json.dumps(report, indent=2) + '\n')
print(report['result'], len(checks), 'checks;', len(independent_comparisons),
      'independent proof comparisons;', len(saved_comparisons), 'complete saved comparisons')
print('Failures:', failures)
for m in (1, 2):
    gap = tuple(map(F, cases[str(m)]['other_gap']))
    # This is display only: every comparison above uses the full rationals.
    print('m=%d other-gap display:' % m, tuple(float(v) for v in gap),
          'required:', ('(40.17,40.20)' if m == 1 else '(149.38,149.40)'))
print('Required continuous gap > d-2; certified upper <150 implies d<=151.')
print('Full certificate:', path.relative_to(BASE))
if failures:
    raise SystemExit(1)
