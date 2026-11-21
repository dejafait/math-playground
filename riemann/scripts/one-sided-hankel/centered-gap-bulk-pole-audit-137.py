"""Replay L701's complete rational certificate without changing step 135.

This checks the finite certificate, not the analytic asymptotics or onset.
The conceptual audit is recorded in the canonical L701 proof.
"""
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
from tempfile import TemporaryDirectory
import json
import subprocess
import sys


base = Path(__file__).resolve().parent
source = base / 'centered-gap-bulk-pole-certificate-135.py'
original = source.with_suffix('.json')
replay = base / 'centered-gap-bulk-pole-certificate-replay-137.json'
output = base / 'centered-gap-bulk-pole-audit-137.json'
source_bytes, original_bytes = source.read_bytes(), original.read_bytes()
old = json.loads(original_bytes)
checks = []


def check(name, actual, required, passed):
    checks.append({'name': name, 'actual': actual, 'required': required,
                   'passed': bool(passed)})


def interval(value):
    lo, hi = map(Q, value)
    assert lo <= hi
    return lo, hi


def abs_upper(value):
    return max(map(abs, interval(value)))


with TemporaryDirectory(prefix='.l701-audit-', dir=base) as temporary:
    copied = Path(temporary) / source.name
    copied.write_bytes(source_bytes)
    result = subprocess.run([sys.executable, str(copied)],
                            capture_output=True, text=True)
    check('generator exit', result.returncode, '0', result.returncode == 0)
    if result.returncode != 0:
        raise RuntimeError(result.stdout + result.stderr)
    replay_bytes = copied.with_suffix('.json').read_bytes()
    replay.write_bytes(replay_bytes)

data = json.loads(replay_bytes)
check('complete replay', sha256(replay_bytes).hexdigest(),
      sha256(original_bytes).hexdigest(), replay_bytes == original_bytes)
check('source hash', sha256(source_bytes).hexdigest(), old['source_sha256'],
      sha256(source_bytes).hexdigest() == old['source_sha256'])
check('original artifacts preserved', 'byte comparison', 'both unchanged',
      source.read_bytes() == source_bytes and original.read_bytes() == original_bytes)
check('generator failures', data['failures'], '[]', data['failures'] == [])

# Exact tangent addition: tan(4 atan(1/5)-atan(1/239))=1.
# L701's audit separately checks that the angle lies in (0, pi/2).
tan_twice = 2*Q(1, 5)/(1-Q(1, 5)**2)
tan_four = 2*tan_twice/(1-tan_twice**2)
tan_machin = (tan_four-Q(1, 239))/(1+tan_four*Q(1, 239))
check('Machin tangent', str(tan_machin), '1', tan_machin == 1)

expected_inputs = [('625/1412', '225/1412'), ('787/1412', '-225/1412'),
                   ('32713/42713', '-3600/42713'), ('89/121', '0')]
expected_norms = ['949/5949', '625/6921', '80000/4038273', '256/11025']
check('log record count', len(data['logs']), '4', len(data['logs']) == 4)
for entry, inputs, norm in zip(data['logs'], expected_inputs, expected_norms):
    a, b = map(Q, entry['input'])
    norm2 = ((a-1)**2+b*b)/((a+1)**2+b*b)
    q0, terms = Q(entry['transform_modulus_upper']), entry['terms']
    tail = 2*q0**(2*terms+1)/((2*terms+1)*(1-q0*q0))
    check(entry['name']+' exact transform/tail',
          {'input': entry['input'], 'norm2': str(norm2), 'tail': str(tail)},
          {'input': list(inputs), 'norm2': norm, 'terms': 60, 'q0': '2/3'},
          entry['input'] == list(inputs) and a > 0 and norm2 == Q(norm)
          and norm2 == Q(entry['transform_norm_squared']) and norm2 < q0*q0
          and q0 == Q(2, 3) and terms == 60
          and tail == Q(entry['absolute_tail_bound']))

for part, broad in [('real', 'declared_alpha'), ('imag', 'declared_beta')]:
    lo, hi = interval(data['b'][part])
    a, b = interval(data[broad])
    check('b '+part+' enclosure', data['b'][part], data[broad], a < lo <= hi < b)
lo, hi = interval(data['twelve_theta_over_pi'])
check('phase nonresonance', data['twelve_theta_over_pi'], '(-5.257,-5.255)',
      Q('-5.257') < lo <= hi < Q('-5.255'))

# Recombine the stored outward coefficient boxes, independently of their
# stored cost fields. Extra outward rounding can only increase this bound.
T, r = Q(21, 20), Q(1, 4)
coefficient_cost = sum((abs_upper(c['constant'])+T*abs_upper(c['tangent_coefficient']))
                       *r**c['degree'] for c in data['coefficients'])
check('coefficient degrees', [c['degree'] for c in data['coefficients']],
      '[2,3,4]', [c['degree'] for c in data['coefficients']] == [2, 3, 4])
numerator_tail = interval(data['numerator_tail_upper'])[1]
denominator_tail = interval(data['denominator_tail_upper'])[1]
sinc_lower = interval(data['sinc_boundary_lower'])[0]
recombined = (coefficient_cost+numerator_tail+denominator_tail)/sinc_lower
check('outward recombined Taylor bound', str(recombined), '<0.186627<1/5',
      0 < recombined < Q('0.186627') < Q(1, 5))
linear_lower = interval(data['linear_boundary_lower'])[0]
check('limiting linear boundary', str(linear_lower), '>7/25', linear_lower > Q(7, 25))
check('limiting margin', str(linear_lower-recombined), '>0.1004105',
      linear_lower-recombined > Q('0.1004105'))
check('positive exponential bound', data['exp_series_upper'], '<9/5',
      interval(data['exp_series_upper'])[1] < Q(9, 5))
check('sinc lower', str(sinc_lower), '>89/100', sinc_lower > Q(89, 100))

epsilon = Q(1, 100)
actual_linear_lower = Q(7, 25)-Q(3, 2)*epsilon
actual_remainder_upper = Q(1, 5)+Q(5, 2)*epsilon
root_exclusion = interval(data['linear_slope_upper'])[1]*r+Q(3, 2)*epsilon
check('eventual actual Taylor boundary',
      {'linear_lower': str(actual_linear_lower),
       'remainder_upper': str(actual_remainder_upper),
       'margin': str(actual_linear_lower-actual_remainder_upper)},
      '53/200 > 45/200; conditional on the proved uniform error <1/100',
      actual_linear_lower == Q(53, 200) and actual_remainder_upper == Q(45, 200))
check('actual polynomial root exclusion', str(root_exclusion), '<1', root_exclusion < 1)

failures = [c['name'] for c in checks if not c['passed']]
report = {
    'kind': 'L701 complete replay and rational margin audit',
    'audit_source_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
    'original_certificate': original.name,
    'replay_certificate': replay.name,
    'checks': checks,
    'failures': failures,
    'qualification': 'Finite arithmetic only; L701 supplies the conceptual proof of uniform asymptotics, phase selection and eventual error. No effective finite-n onset or formal verification.'
}
output.write_text(json.dumps(report, indent=2)+'\n')
print('L701 audit:', 'PASS' if not failures else 'FAIL')
print('Complete replay byte-identical:', replay_bytes == original_bytes)
print('Limiting Taylor bound: <0.186627; required <0.2')
print('Actual boundary after error transfer: 53/200 > 45/200; margin 1/25')
print('Failures:', failures)
print('Full audit:', output)
print('Full replay:', replay)
if failures:
    raise SystemExit(1)
