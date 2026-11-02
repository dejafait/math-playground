"""Full L673 arithmetic replay; analytic audit is canonical in L673.

Preserve the original certificate, recompute every enclosure, independently
enumerate the mesh, and check the decisive point with exact Fraction powers.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json

directory = Path(__file__).resolve().parent
source = directory / 'positive-cone-contour-certificate.py'
original_path = source.with_suffix('.json')
original_bytes = original_path.read_bytes()
original = json.loads(original_bytes)
replay_path = directory / 'positive-cone-contour-audit-replay.json'
namespace = {'__file__': str(replay_path.with_suffix('.py')),
             '__name__': '__audit_replay__'}
exec(compile(source.read_text(), str(source), 'exec'), namespace)
replay = json.loads(replay_path.read_text())
failures, checks = [], []


def check(name, passed, actual, required):
    checks.append(dict(name=name, passed=bool(passed), actual=str(actual),
                       required=str(required)))
    if not passed:
        failures.append(name)


check('every replay field equals the preserved certificate',
      replay == original, replay == original, True)
check('original certificate preserved', original_path.read_bytes() == original_bytes,
      hashlib.sha256(original_path.read_bytes()).hexdigest(),
      hashlib.sha256(original_bytes).hexdigest())

expected = {(kind, s, y, sign)
            for kind, s, y in
            ([('vertical', s, Q(k, 100))
              for s in (Q(-3, 50), Q(3, 50)) for k in range(51)] +
             [('horizontal', Q(k-3, 50), Q(1, 2)) for k in range(7)])
            for sign in (-1, 1)}
seen, sample_count, row_results = set(), 0, []
for index, row in enumerate(replay['rows']):
    key = (row['kind'], Q(row['s']), Q(row['y']), row['real_part_sign'])
    den = 240 if row['kind'] == 'vertical' else 30
    interp = (Q(17, 8)*Q(1, 100)**2 + Q(100, 8)*Q(1, 240)**2
              if den == 240 else
              Q(18, 8)*Q(1, 50)**2 + Q(100, 8)*Q(1, 30)**2)
    samples = row['sample_upper_numerators']
    sample_max = Q(max(samples), 10**12)
    upper = sample_max + interp
    passed = (key in expected and key not in seen and
              row['v_denominator'] == den and len(samples) == 2*den+1 and
              all(type(value) is int for value in samples) and
              row['sample_scale'] == 10**12 and
              Q(row['sampled_max_upper']) == sample_max and
              Q(row['interpolation_error']) == interp and
              Q(row['certified_upper']) == upper and upper < -Q(1, 200))
    row_results.append(dict(index=index, passed=passed, actual=str(upper),
                            required='-1/200'))
    if not passed:
        failures.append(f'complete row {index}')
    seen.add(key)
    sample_count += len(samples)
check('both full tensor meshes and circle charts', seen == expected,
      len(seen), len(expected))
check('all stored samples inspected', sample_count == 98978,
      sample_count, 98978)
check('all auxiliary rational checks pass',
      all(Q(item['actual']) < Q(item['required']) and item['passed']
          for item in replay['checks']), 'all actual < required', True)
check('replay failure list empty', not replay['failures'], replay['failures'], [])
maximum = max(Q(row['certified_upper']) for row in replay['rows'])
check('global maximum independently aggregated',
      maximum == Q(replay['maximum_upper']), maximum, replay['maximum_upper'])
check('strict exponent margin', maximum < -Q(1, 200), maximum, '-1/200')

# Independent exact powers at the maximum, also the rate-1/100 obstruction.
witness = replay['maximum_witness']
row = replay['rows'][witness['row_index']]
v = Q(witness['v_numerator'], row['v_denominator'])
u = (witness['real_part_sign']*(1-v*v)/(1+v*v), 2*v/(1+v*v))
s, y = Q(witness['s']), Q(witness['y'])
a = (-Q(5, 4)+s, y)
a2 = a[0]**2+a[1]**2
uc = (u[0], -u[1])


def cmul(a, b):
    return a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]


arguments = [cmul(u, (a[0]/a2, -a[1]/a2)),
             (-u[0]/Q(5, 4), -u[1]/Q(5, 4)),
             (-Q(5, 4)*uc[0]/Q(121, 64), -Q(5, 4)*uc[1]/Q(121, 64)),
             cmul(a, (uc[0]/Q(121, 64), uc[1]/Q(121, 64)))]
series_results, exact_values = [], []
for index, z in enumerate(arguments):
    power, total = (Q(1), Q(0)), Q(0)
    for k in range(1, 101):
        power = cmul(power, z)
        total += power[0]/(k*(k+1))
    fixed = Q(namespace['series_fixed'](z), 10**40)
    error, bound = abs(total-fixed), namespace['round_error']
    exact_values.append(total)
    series_results.append(dict(index=index, exact_partial_sum=str(total),
                               fixed_partial_sum=str(fixed),
                               absolute_error=str(error), required_bound=str(bound),
                               passed=error <= bound))
    check(f'exact Fraction series {index} versus fixed-point', error <= bound,
          'error <= round_error' if error <= bound else str(error), str(bound))

add, mul = namespace['add'], namespace['mul']
constant = add(mul(namespace['logq'](Q(25, 16)/a2), Q(1, 2)),
               namespace['kernel'](s, y))
constant = add(constant, mul(namespace['C_INTERVAL'], -s))
quadratic = -Q(3, 5)*(s*s-y*y)
constant = add(constant, (quadratic, quadratic))
signed_sum = exact_values[0]-exact_values[1]+exact_values[2]-exact_values[3]
lower = constant[0]+signed_sum-4*namespace['tail_error']
upper = constant[1]+signed_sum+4*namespace['tail_error']
point_lower = Q(namespace['floor_scaled'](lower, 10**12), 10**12)
point_upper = Q(namespace['ceil_scaled'](upper, 10**12), 10**12)
check('decisive point is on the contour and circle',
      s == Q(3, 50) and y == Q(1, 25) and v == Q(3, 80) and
      u[0]**2+u[1]**2 == 1, (str(s), str(y), str(v)), '(3/50, 1/25, 3/80)')
check('fixed-contour rate-1/100 obstruction', point_lower > -Q(1, 100),
      point_lower, '> -1/100')

report = dict(kind='complete replay and conceptual-audit supporting arithmetic',
              source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
              preserved_certificate_sha256=hashlib.sha256(original_bytes).hexdigest(),
              replay_path=str(replay_path.relative_to(directory.parent.parent)),
              sample_count=sample_count, row_count=len(row_results),
              maximum_upper=str(maximum), required_upper='-1/200',
              strict_margin=str(-Q(1, 200)-maximum), checks=checks,
              rows=row_results, exact_series=series_results,
              fixed_contour_point=dict(s=str(s), y=str(y), v=str(v),
                                       u_real=str(u[0]), u_imag=str(u[1]),
                                       lower=str(point_lower), upper=str(point_upper),
                                       excluded_upper='-1/100'), failures=failures,
              scope='Complete finite arithmetic; analytic proof and audit are in L673.')
output = Path(__file__).with_suffix('.json')
output.write_text(json.dumps(report, indent=2)+'\n')
print(f'Audit: {sample_count} samples, {len(row_results)} rows; replay equality: {replay == original}')
print(f'Actual maximum: {maximum}; required < -1/200; margin: {-Q(1, 200)-maximum}')
print(f'Fixed-contour point: [{point_lower}, {point_upper}]; required for obstruction > -1/100')
print(f'Independent Fraction checks: {len(series_results)}; failures: {failures}')
print(f'Full audit: {output}; full replay: {replay_path}')
if failures:
    raise SystemExit(1)
