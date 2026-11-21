#!/usr/bin/env python3
"""Fixed degree256 actual v/v' endpoint preflight; exact rational arithmetic.

Proof and scope: C944a; specialization of L944 with L945. Reuses L938's separately audited input identities,
checking hashes and every audit pass/fail entry; does not replay theta nodes.
"""
import hashlib
import json
import sys
from decimal import Decimal, localcontext
from fractions import Fraction as F
from math import factorial
from pathlib import Path

sys.set_int_max_str_digits(0)
base = Path(__file__).resolve().parent
out = base / 'l938-two-bound-endpoint-73.json'
report = {'status': 'IN_PROGRESS', 'checks': [], 'failures': []}

def save():
    out.write_text(json.dumps(report, indent=2) + '\n')

def check(name, result):
    report['checks'].append({'name': name, 'passed': bool(result)})
    if not result:
        report['failures'].append(name)
        report['status'] = 'FAILED'
        save()
        raise AssertionError(name)

def display(q):
    with localcontext() as c:
        c.prec = 12
        return str(Decimal(q.numerator)/Decimal(q.denominator))

save()
data = json.loads((base/'actual-h2-energy-cell-48.json').read_text())
poly = json.loads((base/'actual-h2-energy-cell-polynomial-48.json').read_text())
audit = json.loads((base/'actual-h2-energy-cell-audit-50.json').read_text())
report['input_hashes'] = {}
for name, expected in audit['inputs_sha256'].items():
    actual = hashlib.sha256((base/name).read_bytes()).hexdigest()
    report['input_hashes'][name] = actual
    check('audited input hash '+name, actual == expected)
check('prior audit completed', audit['status'] == 'PASSED' and not audit['failures'])
check('every prior audit check', len(audit['checks']) == 5101 and
      all(c['passed'] is True for c in audit['checks']))
check('prior exact polynomial residual', audit['integer_identity']['residual'] == '0' and
      audit['integer_identity']['difference_bound_lt_half_base'] is True)
ap = data['approximation']
N = ap['degree']
check('fixed original budget', (N, ap['nodes'], ap['theta_terms'], ap['precision']) ==
      (256, 257, 8, 200))
eps_coeff = F(0)
delta_coeff = F(0)
pnorm_deriv = F(0)
for ell, row in enumerate(ap['chebyshev_coefficients']):
    check('coefficient index '+str(ell), row['k'] == ell)
    chosen = F(int(row['chosen_numerator']), int(ap['chebyshev_denominator']))
    lo, hi = (F(row['enclosure'][key]) for key in ('lower', 'upper'))
    eta = max(abs(chosen-lo), abs(chosen-hi))
    check('complete coefficient radius '+str(ell), eta == F(row['absolute_error']))
    eps_coeff += eta
    delta_coeff += eta*ell**2/4
    pnorm_deriv += abs(chosen)*ell**2/4
check('all kernel coefficients', len(ap['chebyshev_coefficients']) == N+1)
r = F(2, 3)
n = N+1
S0 = r**n/(1-r)
S2 = r**n*(n*n/(1-r)+2*n*r/(1-r)**2+r*(1+r)/(1-r)**3)
eps = 4*10**9*S0 + eps_coeff
delta = F(10**9, 2)*(S2+N*N*S0) + delta_coeff
check('original complete epsilon', eps == F(ap['epsilon']))
B = pnorm_deriv + delta
weight = sum((F(abs(row['coefficient']),
                __import__('math').prod(factorial(k)**a for k, a in
                   enumerate(row['exponents_A0_to_A6']))) for row in data['algebra']['terms']), F(0))
check('all beta rows', len(data['algebra']['terms']) == 34 and weight == F(293,540))
H = 2+eps
check('full epsilon positive and less than one', 0 < eps < 1)
A = 12*eps*H**11
D = delta*H**11+11*B*eps*H**10
Z = weight/F(2**36*factorial(17))
rr = list(map(int, poly['numerators']))
den = int(poly['denominator'])
check('polynomial input dimensions', len(rr) == 3073 and den ==
      (2*factorial(12)*int(ap['power_denominator'])*4**262)**12)

def exact_endpoint(offset):
    # sum_l R_l 4^(offset+l)/(offset+l)! / C^12.
    top = factorial(offset+len(rr)-1)
    quotient = 1
    acc = 0
    for ell in range(len(rr)-1, -1, -1):
        acc = 4*acc + rr[ell]*quotient
        quotient *= offset+ell
    return F(acc*4**offset, den*top)

center = exact_endpoint(17)
derivative = exact_endpoint(16)
radius = Z*4**17*A
derivative_radius = Z*4**16*(17*A+4*D)
records = {}
for name, value, error in [('v_over_pi6', center, radius),
                           ('vprime_over_pi6', derivative, derivative_radius)]:
    records[name] = {'center': str(value), 'radius': str(error),
                     'lower': str(value-error), 'upper': str(value+error),
                     'center_over_radius': str(value/error),
                     'display_center': display(value), 'display_radius': display(error)}
prior_path = base/'l938-direct-endpoint-enclosure-69.json'
prior = json.loads(prior_path.read_text())
check('prior endpoint completed', prior['status'] == 'SCOPED_ENCLOSURE_STOP' and not prior['failures'])
check('every prior endpoint check', all(row['passed'] is True for row in prior['checks']))
for key, value in {'epsilon':eps, 'delta':delta, 'B':B, 'beta_constant':Z}.items():
    check('unchanged '+key, value == F(prior['bounds'][key]))
for key, value in [('v_over_pi6', center), ('vprime_over_pi6', derivative)]:
    check('unchanged exact center '+key, value == F(prior['endpoint_enclosures'][key]['center']))
check('value radius strictly improved', 0 < radius < F(prior['endpoint_enclosures']['v_over_pi6']['radius']))
check('derivative radius strictly improved', 0 < derivative_radius < F(prior['endpoint_enclosures']['vprime_over_pi6']['radius']))
check('density lower bound positive', center-radius > 0)
check('derivative upper bound negative', derivative+derivative_radius < 0)
value_ratio = center/radius
derivative_ratio = -derivative/derivative_radius
value_floor = value_ratio.numerator//value_ratio.denominator
derivative_floor = derivative_ratio.numerator//derivative_ratio.denominator
check('density exact ratio bracket', value_floor < value_ratio < value_floor+1)
check('negative derivative exact ratio bracket', derivative_floor < derivative_ratio < derivative_floor+1)
report['producer_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
report['prior_endpoint_sha256'] = hashlib.sha256(prior_path.read_bytes()).hexdigest()
report.update({'status': 'SCOPED_ENDPOINT_PASS', 'endpoint': '4',
    'normalization': 'v/pi^6 and vprime/pi^6; positive constant only',
    'bounds': {k: str(v) for k,v in {'epsilon':eps, 'delta':delta,
       'B':B, 'common_factor_bound':H, 'product_error':A, 'product_derivative_error':D, 'beta_constant':Z}.items()},
    'endpoint_enclosures': records,
    'verified_margin_brackets': {'v_center_over_radius':[str(value_floor),str(value_floor+1)],
       'negative_vprime_center_over_radius':[str(derivative_floor),str(derivative_floor+1)]},
    'coverage': {'maximum_depth':12, 'maximum_intervals':8191,
       'intervals_examined':0, 'singleton_preflights':1,
       'unresolved_closed_domain':['1/4','4'],
       'reason':'Only E=4 tested: value lower bound positive, derivative upper bound negative. Compact domain has not been covered.'}})
save()
print('SCOPED_ENDPOINT_PASS: E=4, v lower>0, vprime upper<0; no subdivision run.')
for name, rec in records.items():
    print(name+': center='+rec['display_center']+', error='+rec['display_radius']+
          ', |center|/error='+display(abs(F(rec['center_over_radius'])))+'; required >1 for exclusion.')
print('Failures: '+str(report['failures'])+'; certificate: '+str(out))
