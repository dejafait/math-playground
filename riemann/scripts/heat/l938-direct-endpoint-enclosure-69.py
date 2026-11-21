#!/usr/bin/env python3
"""Fixed degree256 actual v/v' endpoint preflight; exact rational arithmetic.

Proof and scope: L944. Reuses L938's separately audited input identities,
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
out = base / 'l938-direct-endpoint-enclosure-69.json'
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
A = 12*eps*8**11
D = delta*8**11+11*B*eps*8**10
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
check('density singleton unresolved', -radius < center < radius)
check('derivative singleton unresolved', -derivative_radius < derivative < derivative_radius)
check('density margin displayed bracket', F(338,10000) < center/radius < F(339,10000))
check('derivative margin displayed bracket', F(220,10**6) < -derivative/derivative_radius < F(221,10**6))
report.update({'status': 'SCOPED_ENCLOSURE_STOP', 'endpoint': '4',
    'normalization': 'v/pi^6 and vprime/pi^6; positive constant only',
    'bounds': {k: str(v) for k,v in {'epsilon':eps, 'delta':delta,
       'B':B, 'product_error':A, 'product_derivative_error':D, 'beta_constant':Z}.items()},
    'endpoint_enclosures': records,
    'verified_margin_brackets': {'v_center_over_radius':['0.0338','0.0339'],
       'negative_vprime_center_over_radius':['0.000220','0.000221']},
    'coverage': {'maximum_depth':12, 'maximum_intervals':8191,
       'intervals_examined':0, 'singleton_preflights':1,
       'unresolved_closed_domain':['1/4','4'],
       'reason':'Both endpoint singleton enclosures contain zero; fixed global-error inclusion cannot certify an interval containing 4.'}})
save()
print('SCOPED_ENCLOSURE_STOP: E=4, both inclusions contain zero; no subdivision run.')
for name, rec in records.items():
    print(name+': center='+rec['display_center']+', error='+rec['display_radius']+
          ', |center|/error='+display(abs(F(rec['center_over_radius'])))+'; required >1 for exclusion.')
print('Failures: '+str(report['failures'])+'; certificate: '+str(out))
