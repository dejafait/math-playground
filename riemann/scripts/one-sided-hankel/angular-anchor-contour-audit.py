"""Replay all of L672's exact certificate and audit its full mesh record.

The analytic justification remains in L672. This writes a separate full
replay, preserves the original certificate, compares every stored value,
and checks a load-bearing sample by independent Fraction power summation.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json

directory = Path(__file__).resolve().parent
source = directory / 'angular-anchor-contour-certificate.py'
original_path = source.with_suffix('.json')
original_bytes = original_path.read_bytes()
original = json.loads(original_bytes)
replay_path = directory / 'angular-anchor-contour-audit-replay.json'
namespace = {'__file__': str(replay_path.with_suffix('.py')),
             '__name__': '__audit_replay__'}
exec(compile(source.read_text(), str(source), 'exec'), namespace)
replay = json.loads(replay_path.read_text())

failures = []
checks = []


def check(name, passed, actual, required):
    checks.append(dict(name=name, passed=bool(passed), actual=str(actual),
                       required=str(required)))
    if not passed:
        failures.append(name)


check('every replay field equals the preserved certificate',
      replay == original, replay == original, True)
check('original file is unchanged', original_path.read_bytes() == original_bytes,
      hashlib.sha256(original_path.read_bytes()).hexdigest(),
      hashlib.sha256(original_bytes).hexdigest())

# Enumerate the expected coordinates independently of the certificate loop.
expected = {(kind, s, y, sign)
            for kind, s, y in
            ([('vertical', s, Q(k, 50))
              for s in (Q(-9, 100), Q(9, 100)) for k in range(26)] +
             [('horizontal', Q(-9+3*k, 100), Q(1, 2)) for k in range(7)])
            for sign in (-1, 1)}
seen = set()
sample_count = 0
row_results = []
for index, row in enumerate(replay['rows']):
    key = (row['kind'], Q(row['s']), Q(row['y']), row['real_part_sign'])
    den = 120 if row['kind'] == 'vertical' else 10
    interp = (Q(13, 8)*Q(1, 50)**2 + Q(100, 8)*Q(1, 120)**2
              if den == 120 else
              Q(16, 8)*Q(3, 100)**2 + Q(100, 8)*Q(1, 10)**2)
    samples = row['sample_upper_numerators']
    sample_max = Q(max(samples), 10**12)
    upper = sample_max + interp
    passed = (key in expected and key not in seen and
              row['v_denominator'] == den and len(samples) == 2*den+1 and
              all(type(value) is int for value in samples) and
              row['sample_scale'] == 10**12 and
              Q(row['sampled_max_upper']) == sample_max and
              Q(row['interpolation_error']) == interp and
              Q(row['certified_upper']) == upper and upper < -Q(11, 1000))
    row_results.append(dict(index=index, passed=passed, actual=str(upper),
                            required='-11/1000'))
    if not passed:
        failures.append(f'complete row {index}')
    seen.add(key)
    sample_count += len(samples)
check('both full tensor meshes and circle charts', seen == expected,
      len(seen), len(expected))
check('all stored samples inspected', sample_count == 25358,
      sample_count, 25358)
check('all recorded auxiliary checks pass',
      all(item['passed'] for item in replay['checks']),
      all(item['passed'] for item in replay['checks']), True)
maximum = max(Q(row['certified_upper']) for row in replay['rows'])
check('global maximum independently aggregated',
      maximum == Q(replay['maximum_upper']), maximum, replay['maximum_upper'])
check('strict exponent gap', maximum < -Q(11, 1000), maximum, '-11/1000')

# Exact Fraction powers at the maximum witness, independent of fixed-point
# recurrence. This is an additional arithmetic check, not a mesh substitute.
witness = replay['maximum_witness']
v = Q(witness['v_numerator'], 120)
u = (witness['real_part_sign']*(1-v*v)/(1+v*v), 2*v/(1+v*v))
a = (-Q(5, 4)+Q(witness['s']), Q(witness['y']))
a2 = a[0]**2+a[1]**2
uc = (u[0], -u[1])


def cmul(a, b):
    return a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]


arguments = [cmul(u, (a[0]/a2, -a[1]/a2)),
             (-u[0]/Q(5, 4), -u[1]/Q(5, 4)),
             (-Q(5, 4)*uc[0]/Q(121, 64), -Q(5, 4)*uc[1]/Q(121, 64)),
             cmul(a, (uc[0]/Q(121, 64), uc[1]/Q(121, 64)))]
series_results = []
for index, z in enumerate(arguments):
    power, total = (Q(1), Q(0)), Q(0)
    for k in range(1, 101):
        power = cmul(power, z)
        total += power[0]/(k*(k+1))
    fixed = Q(namespace['series_fixed'](z), 10**40)
    error = abs(total-fixed)
    bound = namespace['round_error']
    passed = error <= bound
    series_results.append(dict(index=index, exact_partial_sum=str(total),
                               fixed_partial_sum=str(fixed),
                               absolute_error=str(error), required_bound=str(bound),
                               passed=passed))
    check(f'exact Fraction series {index} versus fixed-point', passed,
          'error <= recorded round_error' if passed else str(error), str(bound))

report = dict(kind='complete replay and conceptual-audit supporting arithmetic',
              source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
              preserved_certificate_sha256=hashlib.sha256(original_bytes).hexdigest(),
              replay_path=str(replay_path.relative_to(directory.parent.parent)),
              sample_count=sample_count, row_count=len(row_results),
              maximum_upper=str(maximum), required_upper='-11/1000',
              strict_margin=str(-Q(11, 1000)-maximum),
              checks=checks, rows=row_results, exact_series=series_results,
              failures=failures,
              scope='Complete finite arithmetic only; the analytic audit is in L672.')
output = Path(__file__).with_suffix('.json')
output.write_text(json.dumps(report, indent=2)+'\n')
print(f'Audit: {sample_count} samples, {len(row_results)} rows; full replay equality: {replay == original}')
print(f'Actual maximum: {maximum}; required < -11/1000; strict margin: {-Q(11, 1000)-maximum}')
print(f'Independent Fraction checks: {len(series_results)}; failures: {failures}')
print(f'Full audit: {output}; full replay: {replay_path}')
if failures:
    raise SystemExit(1)
