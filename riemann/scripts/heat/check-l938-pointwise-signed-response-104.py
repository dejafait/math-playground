#!/usr/bin/env python3
"""Independent new-scalar and full endpoint replay; no producer execution."""
import hashlib
import json
import sys
from fractions import Fraction as F
from math import factorial, prod
from pathlib import Path

sys.set_int_max_str_digits(0)
BASE = Path(__file__).resolve().parent
OUT = BASE / 'l938-pointwise-signed-response-check-104.json'
report = dict(status='IN_PROGRESS', checks=[], failures=[], inputs_sha256={})


def check(name, ok):
    report['checks'].append(dict(name=name, passed=bool(ok)))
    if not ok:
        report['failures'].append(name)
        report['status'] = 'FAILED'
        OUT.write_text(json.dumps(report, indent=2)+'\n')
        raise AssertionError(name)


def read(name):
    raw = (BASE/name).read_bytes()
    report['inputs_sha256'][name] = hashlib.sha256(raw).hexdigest()
    return json.loads(raw)


data = read('l938-pointwise-signed-response-104.json')
claim = read('l938-signed-response-complete-90.json')
audit = read('c948a-complete-budget-audit-92.json')
poly = read('actual-h2-energy-cell-polynomial-48.json')
kernel = read('actual-h2-energy-cell-48.json')
x = {k: F(v) for k, v in data['exact'].items()}
for name in report['inputs_sha256']:
    if name != 'l938-pointwise-signed-response-104.json':
        check('same input '+name, report['inputs_sha256'][name] == data['inputs_sha256'][name])
M = [F(row['maximum']) for row in audit['replay_rows']]
beta = [F(prod(range(1, 34-2*k, 2))*prod(range(1, 2*k, 2)), 2**17*factorial(17))
        for k in range(7)]
prefix = 8**17*sum((m*b for m,b in zip(M,beta)), F(0))
check('pointwise prefix', prefix == x['prefix_norm'])
q = F(128, 715)
weights = sum((F(v)*F(1, 2*4**k*factorial(k))
               for k,v in enumerate(claim['tail']['derivative_majorants'])), F(0))
# Recurrence product for (L+17)!, separate from the producer factorial call.
denominator = prod(range(1, 1430))
tail = F(8**17*256**1412, denominator)*weights/(1-q)
check('pointwise complement', q == x['geometric_ratio'] and tail == x['complement_norm'])
# Check the pre-energy-integration beta/gamma cancellation independently,
# including both k endpoints at the first omitted l.
for k in range(7):
    l, h = 1412, 1429-k
    beta_over_pi = F(factorial(2*h)*factorial(2*k),
                    4**(h+k)*factorial(h)*factorial(k)*factorial(l+17))
    f_without_dC = F(4**h*factorial(h), 2*factorial(2*k)*factorial(2*h))
    check('uncancelled complement beta '+str(k), f_without_dC*beta_over_pi
          == F(1, 2*4**k*factorial(k)*factorial(l+17)))
epsilon = F(kernel['approximation']['epsilon'])
pi_hi = F(kernel['approximation']['pi']['upper'])
pi_lo = F(kernel['approximation']['pi']['lower'])
Z = F(293, 540*2**36*factorial(17))
linear = epsilon*pi_hi**6*(prefix+tail)
second = F(12*11, 2)*epsilon**2*8**10*pi_hi**6*Z*8**17
check('all higher replacement terms paid', second == x['second_order_upper'])
check('total pointwise error', linear == x['first_order_upper']
      and linear+second == x['total_error_upper'])

# Backwards exact rational Horner with unreduced integer numerator/denominator.
R = list(map(int, poly['numerators']))
u, d = R[-1], 1
for l in range(len(R)-2, -1, -1):
    d *= l+18
    u = 8*u + R[l]*d
center = F(u*8**17, d*factorial(17)*int(poly['denominator']))
check('all3073 terms independent nested endpoint', center == x['normalized_polynomial_endpoint'])
check('new exact density enclosures', center*pi_lo**6 == x['polynomial_endpoint_lower']
      and center*pi_hi**6 == x['polynomial_endpoint_upper'])
check('strict threshold fails', linear+second > center*pi_lo**6 > 0)
check('complete enclosure contains zero', x['actual_endpoint_lower']
      == center*pi_lo**6-linear-second < 0 < center*pi_hi**6+linear+second
      == x['actual_endpoint_upper'])
check('ratio', x['error_to_required_ratio'] == (linear+second)/(center*pi_lo**6))
for name, interval in data['summary'].items():
    check('complete outward display '+name,
          F(interval['lower']) <= x[name] <= F(interval['upper']))
report['status'] = 'PASSED_CONDITIONAL_NEW_ARITHMETIC_REPLAY'
report['qualification'] = ('Complete new scalar/endpoint replay, not a theta, '
    'signed-prefix or original full-polynomial production audit.')
OUT.write_text(json.dumps(report, indent=2)+'\n')
print(json.dumps(dict(status=report['status'], checks=len(report['checks']),
    failures=report['failures'], certificate=str(OUT)), indent=2))
