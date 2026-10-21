#!/usr/bin/env python3
"""Exact constants for L050; analytic arguments remain in its proof."""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json

checks = []
def check(name, actual, relation, required):
    a, b = F(actual), F(required)
    passed = {'<': a < b, '>': a > b, '=': a == b}[relation]
    checks.append(dict(name=name, actual=str(a), relation=relation,
                       required=str(b), passed=passed))

def log_enclosure(t, m=48):
    x = (t-1)/(t+1)
    low = 2*sum((x**(2*j+1)/F(2*j+1) for j in range(m)), F(0))
    error = 2*x**(2*m+1)/((2*m+1)*(1-x*x))
    return dict(argument=str(t), x=str(x), terms=m, lower=str(low),
                remainder_upper=str(error), upper=str(low+error))

R = sum((F(48,25)**j for j in range(20)), F(0))
check('geometric identity', R, '=', (F(48,25)**20-1)/(F(48,25)-1))
check('twenty occurrence geometric upper bound', R, '<', 503775)
A, B, ceiling = F(399,5)*503775, 72*503775+2, 10**9
check('length constant', F(1380,1034), '<', 2)
e_lower = sum((F(1,factorial(k)) for k in range(6)), F(0))
check('e lower comparison', e_lower, '>', F(27,10))
check('log20 below 3', e_lower**3, '>', 20)
check('log ceiling below 21', F(27,10)**21, '>', ceiling)
check('monotonicity derivative guard', A, '<', ceiling)
check('ceiling contradiction upper bound', 21*A+B, '<', ceiling)

logs = {name: log_enclosure(F(t)) for name,t in [('log2',2),('log3',3)]}
l2,u2 = F(logs['log2']['lower']),F(logs['log2']['upper'])
l3,u3 = F(logs['log3']['lower']),F(logs['log3']['upper'])
p,q = 9809721694,6189245291
res_lo,res_hi = q*l3-p*u2,q*u3-p*l2
check('rational approximant is strictly below log ratio',res_lo,'>',0)
check('rational approximant residual upper bound',res_hi,'<',l2/(2*ceiling))
check('log2 exceeds 2/3',l2,'>',F(2,3))
height_upper = F(1380*q+23,11)
check('minimum log height below 28',F(27,10)**28,'>',height_upper)
odd_upper = F(15,4)*503775*29
check('represented odd count contradiction',odd_upper,'<',225640000)

failures = [c for c in checks if not c['passed']]
result = dict(lemma='L050',scope='Twenty-word subsystem only; exact constant checks support written all-parameter proof.',
              R=str(R),R_upper=503775,A=str(A),B=B,length_ceiling=ceiling,
              p=p,q=q,log_enclosures=logs,residual_lower=str(res_lo),residual_upper=str(res_hi),
              minimum_shifted_height_upper=str(height_upper),minimum_log_height_upper=28,
              represented_odd_count_upper=str(odd_upper),primitive_odd_count_required=225640000,
              checks=checks,failures=failures)
path=Path(__file__).with_name('twenty-cyclic-height-certificate.json')
path.write_text(json.dumps(result,indent=2)+'\n')
print(f'checks={len(checks)}, failures={len(failures)}')
print(f'R<503775; N ceiling test: {21*A+B} < {ceiling}; A={A} < {ceiling}')
print(f'0 < {q} log3 - {p} log2 < log2/{2*ceiling}: certified')
print(f's_0 < {height_upper}; h_0 < 28; K < {odd_upper}; required K > 225640000')
print(f'certificate: {path.relative_to(Path.cwd())}')
if failures:
    print('failed checks: '+', '.join(c['name'] for c in failures))
    raise SystemExit(1)
