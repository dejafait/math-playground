"""Exact three-point obstruction for L681's fixed right contour edge.

The canonical corollary supplies the analytic interpretation. All bound
decisions are rational; this is not a screen over multiplier coefficients.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json

directory = Path(__file__).resolve().parent
helper_path = directory / 'positive-cone-contour-certificate.py'
source = helper_path.read_text()
boundary = '\npoints = {240:'
assert source.count(boundary) == 1
prefix = source.split(boundary)[0]
assert 'write_text(' not in prefix
ns = {'__name__': '__series_helpers__'}
exec(compile(prefix, str(helper_path), 'exec'), ns)
cmul, series = ns['complex_mul'], ns['series_fixed']
logq, PI = ns['logq'], ns['PI']
scale = 10**12
d, U, w = Q(5, 4), Q(121, 64), Q(7, 100)
weights = [Q(7, 9), Q(1, 5), Q(1, 45)]
specs = [(Q(0), Q(0)), (2*w, Q(1, 9)), (3*w, Q(1, 6))]
rows, checks, failures = [], [], []


def check(name, passed, actual, required):
    checks.append(dict(name=name, passed=bool(passed), actual=str(actual),
                       required=str(required)))
    if not passed:
        failures.append(name)


def floor_save(v):
    return Q((v.numerator*scale)//v.denominator, scale)


def ceil_save(v):
    return Q(-((-v.numerator*scale)//v.denominator), scale)


def exact_series(z):
    pr, pi, total = Q(1), Q(0), Q(0)
    for k in range(1, 101):
        pr, pi = pr*z[0]-pi*z[1], pr*z[1]+pi*z[0]
        total += pr/Q(k*(k+1))
    return total


for weight, (y, v) in zip(weights, specs):
    u = (-(1-v*v)/(1+v*v), 2*v/(1+v*v))
    a = (-d+w, y)
    a2 = a[0]**2+a[1]**2
    args = [cmul(u, (a[0]/a2, -a[1]/a2)), (-u[0]/d, -u[1]/d),
            (-d*u[0]/U, d*u[1]/U), cmul(a, (u[0]/U, -u[1]/U))]
    sums = [series(z) for z in args]
    finite = Q(sums[0]-sums[1]+sums[2]-sums[3], ns['SCALE'])
    logs = logq(d*d/a2)
    error = ns['four_series_error']
    coefficient = -Q(20, 27)*w
    lower = logs[0]/2 + coefficient*PI[1] + finite-error
    upper = logs[1]/2 + coefficient*PI[0] + finite+error
    exact_sums = [exact_series(z) for z in args]
    rounding_errors = [abs(s-Q(t, ns['SCALE'])) for s, t in zip(exact_sums, sums)]
    exact_finite = exact_sums[0]-exact_sums[1]+exact_sums[2]-exact_sums[3]
    exact_lower = logs[0]/2 + coefficient*PI[1] + exact_finite-4*ns['tail_error']
    exact_upper = logs[1]/2 + coefficient*PI[0] + exact_finite+4*ns['tail_error']
    basis2, basis4 = w*w-y*y, w**4-6*w*w*y*y+y**4
    check(f'point {y}: parameter/series/circle margins',
          Q(29, 25)**2 < a2 < Q(3, 2)**2
          and all(z[0]**2+z[1]**2 < Q(81, 100) for z in args)
          and u[0]**2+u[1]**2 == 1 and y < Q(9, 25),
          f'a^2={a2}, y={y}', '29/25<|a|<3/2; |args|<9/10; |u|=1; y<9/25')
    check(f'point {y}: outward rounding',
          floor_save(lower) <= lower <= upper <= ceil_save(upper),
          f'[{floor_save(lower)}, {ceil_save(upper)}]', 'contains full enclosure')
    check(f'point {y}: exact rational powers cross-check',
          all(e <= ns['round_error'] for e in rounding_errors)
          and lower <= exact_lower <= exact_upper <= upper,
          f'max series discrepancy < 10^-20: {max(rounding_errors) < Q(1, 10**20)}',
          'all 4 finite-sum errors within bound; exact enclosure nested')
    rows.append(dict(weight=str(weight), s=str(w), y=str(y), v=str(v),
                     u=[str(t) for t in u], a_squared=str(a2),
                     arguments=[[str(t) for t in z] for z in args],
                     fixed_partial_sums=sums, fixed_scale=ns['SCALE'],
                     exact_partial_sums=[str(t) for t in exact_sums],
                     fixed_rounding_errors=[str(t) for t in rounding_errors],
                     exact_power_enclosure=[str(exact_lower), str(exact_upper)],
                     log_interval=[str(t) for t in logs],
                     four_series_error=str(error),
                     full_lower=str(lower), full_upper=str(upper),
                     saved_lower=str(floor_save(lower)), saved_upper=str(ceil_save(upper)),
                     basis2=str(basis2), basis4=str(basis4)))

mass = sum(weights)
moment2 = sum(Q(row['weight'])*Q(row['basis2']) for row in rows)
moment4 = sum(Q(row['weight'])*Q(row['basis4']) for row in rows)
weighted_lower = sum(Q(row['weight'])*Q(row['saved_lower']) for row in rows)
weighted_upper = sum(Q(row['weight'])*Q(row['saved_upper']) for row in rows)
barrier = -Q(1, 125)
check('positive probability weights', all(t > 0 for t in weights) and mass == 1, mass, 1)
check('quadratic coefficient cancels exactly', moment2 == 0, moment2, 0)
check('quartic coefficient cancels exactly', moment4 == 0, moment4, 0)
check('coefficient-independent exponent obstruction', weighted_lower > barrier,
      weighted_lower, f'> {barrier} > -1/100')
report = dict(kind='exact rational lower certificate for fixed-contour exponent obstruction',
              helper_source=helper_path.name,
              helper_sha256=hashlib.sha256(source.encode()).hexdigest(),
              helper_boundary=boundary.strip(),
              pi_interval=[str(t) for t in PI], rows=rows, checks=checks,
              weighted_lower=str(weighted_lower), weighted_upper=str(weighted_upper),
              proved_barrier=str(barrier), required_strict_target='-1/100',
              initial_stronger_test=dict(requested_lower='-7/1000', passed=False,
                                         actual_lower=str(weighted_lower),
                                         qualification='The selected witness did not certify '
                                         'this stronger bound; it does certify > -1/125.'),
              quadratic_moment=str(moment2), quartic_moment=str(moment4),
              failures=failures,
              qualification='Obstructs a uniform absolute integrand bound on L681 fixed '
              'rectangle for even quartic Robin multipliers; no residual lower bound, '
              'other-contour obstruction, or arbitrary-weight conclusion.')
out = Path(__file__).with_suffix('.json')
out.write_text(json.dumps(report, indent=2)+'\n')
print('Three exact boundary values:', [(r['saved_lower'], r['saved_upper']) for r in rows])
print(f'Weighted exponent >= {weighted_lower} ({float(weighted_lower):.12f}); '
      f'required for obstruction > {barrier}; target requires < -1/100')
print('Initial stronger -7/1000 check failed and is retained in the certificate.')
print(f'Quadratic/quartic moments: {moment2}, {moment4}; failures: {failures}')
print(f'Complete certificate: {out}')
if failures:
    raise SystemExit(1)
