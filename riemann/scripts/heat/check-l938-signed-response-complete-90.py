#!/usr/bin/env python3
"""Independent normalization/maximizer contractions, not a full producer audit."""
import hashlib
import json
import sys
from fractions import Fraction as Q
from math import comb, factorial
from pathlib import Path

sys.set_int_max_str_digits(0)
BASE = Path(__file__).resolve().parent
OUT = BASE / 'l938-signed-response-complete-check-90.json'
report = dict(status='IN_PROGRESS', checks=[], failures=[], inputs_sha256={})


def save():
    OUT.write_text(json.dumps(report, indent=2)+'\n')


def check(name, ok):
    report['checks'].append(dict(name=name, passed=bool(ok)))
    if not ok:
        report['failures'].append(name)
        report['status'] = 'FAILED'
        save()
        raise AssertionError(name)


def read(name):
    raw = (BASE/name).read_bytes()
    report['inputs_sha256'][name] = hashlib.sha256(raw).hexdigest()
    return json.loads(raw)


save()
source = read('l938-signed-response-complete-90.json')
bounds = read('l938-response-bernstein-enclosures-90.json')
prefix = read('l938-signed-response-coefficients-89.json')
kernel = read('actual-h2-energy-cell-48.json')
old = read('l938-negative-tail-allowance-87.json')
check('complete producer flags', len(source['checks']) == 29626 and not source['failures']
      and all(x['passed'] is True for x in source['checks']))
check('coefficient enclosure hash', report['inputs_sha256'][source['bernstein_artifact']]
      == source['bernstein_sha256'])
for name in ['l938-signed-response-coefficients-89.json', 'actual-h2-energy-cell-48.json',
             'l938-negative-tail-allowance-87.json']:
    check('unchanged input '+name, report['inputs_sha256'][name] == source['inputs_sha256'][name])
D, GRID = bounds['degree'], int(bounds['grid'])
C = int(prefix['C'])
check('full degree and grid', D == 2816 and GRID == 10**120 and bounds['cut'] == 1411)
exact_witnesses = []
for k, block in enumerate(bounds['rows']):
    j = block['maximum_index']
    maxima = int(block['maximum_numerator'])
    check('complete row dimension '+str(k), block['k'] == k and len(block['bernstein']) == D+1)
    for i, pair in enumerate(block['bernstein']):
        lo, hi = map(int, pair)
        check('full saved bound '+str(k)+','+str(i), lo <= hi and max(abs(lo), abs(hi)) <= maxima)
    check('maximum summary '+str(k), Q(maxima,GRID) == Q(source['prefix']['maxima'][k]))
    # Full factorial gamma normalization, independent of producer's odd
    # products, and direct binomial contraction rather than rounded Horner.
    F = factorial(2*(17+j))
    num = 0
    for l in range(j+1):
        d = int(prefix['gradients'][k][l])
        h = 17-k+l
        check('exact gamma division '+str(k)+','+str(l), F % factorial(2*h) == 0)
        num += (d*4**h*factorial(h)*(F//factorial(2*h))*8**l
                *comb(j,l)*factorial(l)*factorial(D-l))
    value = Q(num,2*C**11*factorial(2*k)*F*factorial(D))
    lo, hi = map(int, block['bernstein'][j])
    check('independent exact maximizing contraction '+str(k), Q(lo,GRID) <= value <= Q(hi,GRID))
    exact_witnesses.append(dict(k=k,j=j,value=str(value),grid_lower=str(Q(lo,GRID)),
                                grid_upper=str(Q(hi,GRID))))

beta = [Q(factorial(34-2*k)*factorial(2*k),
          4**17*factorial(17-k)*factorial(k)*factorial(17)) for k in range(7)]
check('all beta masses factorial normalization', list(map(str,beta)) == source['prefix']['beta_masses_over_pi'])
mass = sum((Q((16+i+1)**18-(16+i)**18,18*4**18) for i in range(16)),Q(0))
check('all sixteen cells included', mass == Q(source['prefix']['energy_mass']))
pref = mass*sum((Q(m)*b for m,b in zip(source['prefix']['maxima'],beta)),Q(0))
check('complete prefix budget recombination', pref == Q(source['prefix']['complete_coefficient_norm_upper']))

ap=kernel['approximation']
r=Q(source['tail']['r'])
for k in range(7):
    v=Q(0)
    for l in range(256,-1,-1):
        q = (abs(int(ap['power_numerators'][l]))
             *(factorial(2*(k+l))//factorial(k+l))*4**(262-k-l)
             *(factorial(12)//factorial(2*k)))
        v=v*r+q
    check('integer Q positive evaluation '+str(k), v/C == Q(source['tail']['qplus'][k]))
L=source['tail']['first_degree']
ratio=Q(source['tail']['geometric_ratio'])
tail=8**18*(8/r)**L/Q(factorial(L+18))/(1-ratio)*sum(
    (Q(t)/Q(2*4**k*factorial(k)) for k,t in enumerate(source['tail']['derivative_majorants'])),Q(0))
check('complete geometric tail recombination', L==1412 and ratio==8/r/(L+19)
      and 0<ratio<1 and tail==Q(source['tail']['complete_norm_upper'])
      and 0<tail<Q(source['tail']['rational_cap']))
first = (Q(old['exact']['exp_upper'])*Q(ap['epsilon'])*Q(old['exact']['pi_upper'])**6
         *(pref+Q(source['tail']['rational_cap'])))
total=first+Q(source['result']['second_order_upper'])
cap=Q('8.079e-50')
check('complete strict budget', first==Q(source['result']['first_order_upper'])
      and total==Q(source['result']['total_upper']) and 0<total<cap
      <Q(source['result']['required_strict_upper']))
check('total display exact', Q(source['result']['total_upper_enclosure']['lower'])
      <= total <= Q(source['result']['total_upper_enclosure']['upper']))
report['exact_maximizer_contractions']=exact_witnesses
report['witness']=dict(total_upper_cap=str(cap), required_strict_upper=source['result']['required_strict_upper'],
    tail_norm_cap=source['tail']['rational_cap'], maxima_indices=source['prefix']['maximum_indices'],
    full_saved_coefficients=7*(D+1), exact_independent_contractions=7,
    result='COMPLETE_REPLACEMENT_BUDGET_PASSED')
report['scope']=('Checks every saved interval against its reported row maximum, independently contracts '
    'seven maximizing coefficients with factorial normalization, checks beta/cell normalizations, '
    'positive Q evaluations and final rational budget. Does not independently replay every Horner '
    'enclosure or audit inherited derivatives/theta inputs; not a conceptual audit of the proof.')
report['status']='PASSED'
save()
print('Result:',report['status'],'; checks:',len(report['checks']),'; failures:',report['failures'])
print('Total upper <',cap,'; required <',source['result']['required_strict_upper'])
print('Full certificate:',OUT)
