"""Replay L681 without overwriting its certificate; audit all cells exactly.

This checks finite arithmetic and coverage. The analytic proof and audit
remain in L681; this is not a numerical proof of the residue identity.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json

directory = Path(__file__).resolve().parent
source = directory / 'discrete-robin-quadrature-certificate.py'
original_path = source.with_suffix('.json')
original_bytes = original_path.read_bytes()
original = json.loads(original_bytes)
replay_path = directory / 'discrete-robin-quadrature-audit-replay.json'
namespace = {'__name__': '__audit_replay__',
             '__file__': str(replay_path.with_suffix('.py'))}
source_text = source.read_text()
exec(compile(source_text, str(source), 'exec'), namespace)
replay = json.loads(replay_path.read_text())
helpers = namespace['ns']
checks, failures, cell_strips, exact_checks = [], [], [], []


def check(name, passed, actual, required):
    checks.append(dict(name=name, passed=bool(passed), actual=str(actual),
                       required=str(required)))
    if not passed:
        failures.append(name)


check('original certificate preserved', original_path.read_bytes() == original_bytes,
      hashlib.sha256(original_path.read_bytes()).hexdigest(),
      hashlib.sha256(original_bytes).hexdigest())
check('complete replay matches original', replay == original, replay == original, True)
check('replay failures empty', replay['failures'] == [], replay['failures'], [])
check('all original auxiliary checks pass', all(c['passed'] for c in replay['checks']),
      sum(c['passed'] for c in replay['checks']), len(replay['checks']))
helper_path = directory / replay['helper_source']
helper_text = helper_path.read_text()
check('helper source hash', hashlib.sha256(helper_text.encode()).hexdigest()
      == replay['helper_source_sha256'], hashlib.sha256(helper_text.encode()).hexdigest(),
      replay['helper_source_sha256'])
boundary = '\npoints = {240:'
prefix = helper_text.split(boundary)[0]
check('preserved helper boundary excludes mesh and output',
      helper_text.count(boundary) == 1 and '\npoints = ' not in prefix
      and 'write_text(' not in prefix, replay['helper_read_boundary'], boundary.strip())

required, scale = -Q(3, 500), 10**12
rows = replay['rows']
lookup = {(r['kind'], Q(r['s']), Q(r['y']), r['real_part_sign']): r for r in rows}
expected = {('right', Q(7, 100), Q(j, 200), sign)
            for j in range(91) for sign in (-1, 1)}
expected |= {('top', Q(j, 200), Q(9, 20), sign)
             for j in range(-25, 15) for sign in (-1, 1)}
check('independent complete row census', set(lookup) == expected and len(rows) == 262,
      f'{len(lookup)} distinct / {len(rows)} total', '262 distinct / 262 total')
row_failures = []
for key, row in lookup.items():
    den = 300 if row['kind'] == 'right' else 50
    error = Q(1, 200)**2 + Q(100, 8)*Q(1, den)**2
    values = row['sample_upper_numerators']
    sample_max = Q(max(values), scale)
    if not (len(values) == 2*den+1 and all(type(v) is int for v in values)
            and row['v_denominator'] == den and row['sample_scale'] == scale
            and Q(row['sampled_max_upper']) == sample_max
            and Q(row['interpolation_error']) == error
            and Q(row['certified_upper']) == sample_max+error
            and sample_max+error < required):
        row_failures.append(str(key))
check('every row shape and upper bound', not row_failures, row_failures, [])

# Independently cover every two-dimensional interpolation cell, retaining
# all four corners. The top mesh has s=0 as a vertex, never in a cell interior.
cell_count = 0
cell_maximum = None
cell_failures = []
for kind, den, indices in [('right', 300, range(90)), ('top', 50, range(-25, 14))]:
    error = Q(1, 200)**2 + Q(100, 8)*Q(1, den)**2
    for sign in (-1, 1):
        for j in indices:
            if kind == 'right':
                key0 = (kind, Q(7, 100), Q(j, 200), sign)
                key1 = (kind, Q(7, 100), Q(j+1, 200), sign)
            else:
                key0 = (kind, Q(j, 200), Q(9, 20), sign)
                key1 = (kind, Q(j+1, 200), Q(9, 20), sign)
                assert not (Q(j, 200) < 0 < Q(j+1, 200))
            lower = lookup[key0]['sample_upper_numerators']
            upper = lookup[key1]['sample_upper_numerators']
            maxima = [max(lower[k], lower[k+1], upper[k], upper[k+1])
                      for k in range(2*den)]
            bound = Q(max(maxima), scale)+error
            cell_count += len(maxima)
            cell_maximum = bound if cell_maximum is None else max(cell_maximum, bound)
            if bound >= required:
                cell_failures.append(f'{kind} sign={sign} j={j}')
            cell_strips.append(dict(kind=kind, sign=sign, interval_index=j,
                                    v_denominator=den, sample_scale=scale,
                                    four_corner_maximum_numerators=maxima,
                                    interpolation_error=str(error), upper=str(bound)))
check('all continuous cells including both sides of zero',
      cell_count == 115800 and not cell_failures, f'{cell_count}; failures={cell_failures}',
      '115800; failures=[]')
check('continuous maximum independently reconstructed',
      cell_maximum == Q(replay['maximum_upper']) and cell_maximum < required,
      cell_maximum, required)

# Selected evaluations using exact rational powers, without coordinate or
# summand flooring. These supplement the full fixed-point replay and its
# analytic rounding proof; they do not replace continuous coverage.
def product(a, b):
    return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])


def exact_series(z):
    power, total = (Q(1), Q(0)), Q(0)
    for k in range(1, 101):
        power = product(power, z)
        total += power[0]/(k*(k+1))
    return total


witness = replay['maximum_witness']
selected = [(witness['row_index'], witness['v_numerator'])]
for key, vn in [(('right', Q(7, 100), Q(0), -1), -300),
                (('right', Q(7, 100), Q(9, 20), 1), 300),
                (('top', Q(0), Q(9, 20), -1), 0),
                (('top', Q(0), Q(9, 20), 1), 0),
                (('top', -Q(1, 8), Q(9, 20), -1), -50),
                (('top', Q(7, 100), Q(9, 20), 1), 50)]:
    selected.append((rows.index(lookup[key]), vn))

d, U = Q(5, 4), Q(121, 64)
for row_index, vn in selected:
    row = rows[row_index]
    s, y = Q(row['s']), Q(row['y'])
    v = Q(vn, row['v_denominator'])
    u = (row['real_part_sign']*(1-v*v)/(1+v*v), 2*v/(1+v*v))
    a = (-d+s, y)
    a2 = a[0]**2+a[1]**2
    args = [product(u, (a[0]/a2, -a[1]/a2)), (-u[0]/d, -u[1]/d),
            (-d*u[0]/U, d*u[1]/U), product(a, (u[0]/U, -u[1]/U))]
    sums = [exact_series(z) for z in args]
    errors = [abs(exact-Q(helpers['series_fixed'](z), helpers['SCALE']))
              for z, exact in zip(args, sums)]
    finite = sums[0]-sums[1]+sums[2]-sums[3]
    logs = helpers['logq'](d*d/a2)
    pi = helpers['PI']
    coefficient = -Q(20, 27)*max(s, Q(0))
    tail = 4*helpers['tail_error']
    lower_bound = logs[0]/2 + coefficient*pi[1] + finite-tail
    upper_bound = logs[1]/2 + coefficient*pi[0] + finite+tail
    saved = Q(row['sample_upper_numerators'][vn+row['v_denominator']], scale)
    passed = (all(e <= helpers['round_error'] for e in errors)
              and lower_bound <= upper_bound <= saved)
    record = dict(row_index=row_index, v_numerator=vn, passed=passed,
                  exact_partial_sums=[str(v) for v in sums],
                  fixed_point_errors=[str(v) for v in errors],
                  required_round_error=str(helpers['round_error']),
                  full_exponent_interval=[str(lower_bound), str(upper_bound)],
                  saved_upper=str(saved))
    exact_checks.append(record)
check('exact rational power comparisons at witness and boundary cases',
      all(r['passed'] for r in exact_checks), sum(r['passed'] for r in exact_checks),
      len(exact_checks))

# Rational margins used in extending the analytic estimates to this rectangle.
check('compact modulus lower margin', Q(5, 4)-Q(7, 100) > Q(29, 25),
      Q(59, 50), '>29/25')
check('compact modulus squared upper margin', Q(11, 8)**2+Q(9, 20)**2 < Q(9, 4),
      Q(11, 8)**2+Q(9, 20)**2, '<9/4')
check('q=1 height and rho limits', Q(9, 20)-Q(27, 20*15) == Q(9, 25)
      and Q(27, 100*15) == Q(9, 500), 'Y=9/25; rho=9/500', 'same')
check('all four series arguments below 9/10',
      max(Q(25, 29), Q(4, 5), Q(80, 121), Q(96, 121)) < Q(9, 10),
      max(Q(25, 29), Q(4, 5), Q(80, 121), Q(96, 121)), '<9/10')
check('weight upper bound from pi>3', 1+Q(10, 3) == Q(13, 3),
      Q(13, 3), 'strict bound using pi>3')

audit_path = Path(__file__).with_suffix('.json')
report = dict(kind='L681 independent conceptual-audit arithmetic support',
              generator_sha256=hashlib.sha256(source_text.encode()).hexdigest(),
              original_certificate_sha256=hashlib.sha256(original_bytes).hexdigest(),
              replay_path=replay_path.name, checks=checks, failures=failures,
              sample_count=replay['sample_count'], row_count=len(rows),
              cell_count=cell_count, maximum_upper=str(cell_maximum),
              required_upper=str(required), margin=str(required-cell_maximum),
              cell_strips=cell_strips, exact_rational_checks=exact_checks,
              qualification='Analytic residues, derivatives and finite-n proof are in L681; '
              'rate 3/500 remains below 1/100 and original unit residues are unchanged.')
audit_path.write_text(json.dumps(report, indent=2)+'\n')
print(f'Audit: {len(checks)} checks; {cell_count} cells; '
      f'{len(exact_checks)} exact-rational points; failures={failures}')
print(f'Actual continuous upper: {cell_maximum}; required < {required}; '
      f'margin={required-cell_maximum}')
print(f'Audit certificate: {audit_path}')
print(f'Preserved-original replay: {replay_path}')
if failures:
    raise SystemExit(1)
