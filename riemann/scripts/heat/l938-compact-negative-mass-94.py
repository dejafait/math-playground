#!/usr/bin/env python3
"""One fixed full-density Bernstein/Jensen certificate; exact enclosures."""
import hashlib
import json
import sys
from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING
from fractions import Fraction as F
from math import factorial
from pathlib import Path

sys.set_int_max_str_digits(0)
BASE = Path(__file__).resolve().parent
OUT = BASE / 'l938-compact-negative-mass-94.json'
COEFF = BASE / 'l938-compact-bernstein-enclosures-94.json'
N, G = 3089, 10**120
report = dict(status='IN_PROGRESS', checks=[], failures=[], inputs_sha256={},
              python=sys.version, stage='input')


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


def shown(x):
    with localcontext() as ctx:
        ctx.prec = 16
        ctx.rounding = ROUND_FLOOR
        lo = str(Decimal(x.numerator)/Decimal(x.denominator))
        ctx.rounding = ROUND_CEILING
        hi = str(Decimal(x.numerator)/Decimal(x.denominator))
    check('outward display '+str(len(report['checks'])), F(lo) <= x <= F(hi))
    return dict(lower=lo, upper=hi)


save()
kernel = read('actual-h2-energy-cell-48.json')
poly = read('actual-h2-energy-cell-polynomial-48.json')
audit50 = read('actual-h2-energy-cell-audit-50.json')
old = read('l938-negative-tail-allowance-87.json')
audit92 = read('c948a-complete-budget-audit-92.json')
claim90 = read('l938-signed-response-complete-90.json')
for name, count, status, obj in [
    ('audit50', 5101, 'PASSED', audit50),
    ('audit92', None, 'PASSED_CONDITIONAL_FULL_AUDIT', audit92)]:
    check(name+' complete saved flags', obj['status'] == status and not obj['failures']
          and all(c['passed'] is True for c in obj['checks'])
          and (count is None or len(obj['checks']) == count))
for name in ('actual-h2-energy-cell-48.json', 'actual-h2-energy-cell-polynomial-48.json'):
    check('unchanged audited input '+name,
          report['inputs_sha256'][name] == audit50['inputs_sha256'][name])
check('unchanged replacement producer', report['inputs_sha256']['l938-signed-response-complete-90.json']
      == audit92['inputs_sha256']['l938-signed-response-complete-90.json'])
ap = kernel['approximation']
check('all fixed kernel settings', (ap['degree'], ap['nodes'], ap['theta_terms'], ap['precision'])
      == (256,257,8,200) and int(ap['chebyshev_denominator']) == G
      and int(ap['power_denominator']) == G*4**256)
R = list(map(int, poly['numerators']))
den = int(poly['denominator'])
C = 2*factorial(12)*int(ap['power_denominator'])*4**262
check('full polynomial and normalization', len(R) == 3073 and R[-1] != 0
      and den == C**12 and den > 0 and N == 17+len(R)-1)
check('replacement same kernel', report['inputs_sha256']['actual-h2-energy-cell-48.json']
      == audit92['inputs_sha256']['actual-h2-energy-cell-48.json'])
B = F(audit92['exact']['total_upper'])
m = F('8.935649629627030e-35')
check('exact audited B and margin', B == F(claim90['result']['total_upper'])
      and m == F(audit92['exact']['required_strict_upper']) and 0 < B < m)
pi_hi = F(old['exact']['pi_upper'])
exp_hi = F(old['exact']['exp_upper'])
check('same positive scalar enclosures', pi_hi == F(ap['pi']['upper'])
      and 3 < pi_hi < 4 and 2 < exp_hi < 3)
report['qualification'] = ('All original theta, polynomial-execution, derivative-prefix and '
    'arithmetic contracts inherited. New integer enclosures use the complete degree3089 density. '
    'Saved flags/hashes are consistency checks, not independent mathematical verification.')
report['stage'] = 'full power coefficients'
save()

# Ordinary coefficients of v_p(8x)/pi^6: t_s=R_(s-17)8^s/(den*s!).
fac = [factorial(s) for s in range(N+1)]
power = []
for s in range(N+1):
    num = 0 if s < 17 else R[s-17]*8**s*G
    divisor = den*fac[s]
    lo, hi = num//divisor, -((-num)//divisor)
    check('complete power inclusion '+str(s), lo*divisor <= num <= hi*divisor
          and 0 <= hi-lo <= 1)
    power.append((lo,hi))

# b_j=sum_s t_s binom(j,s)/binom(N,s). Backward nested contraction.
global_bounds = []
for j in range(N+1):
    lo, hi = power[j]
    for s in range(j-1,-1,-1):
        mul, divisor = j-s, N-s
        lo = power[s][0] + lo*mul//divisor
        hi = power[s][1] - ((-hi*mul)//divisor)
    check('full Bernstein interval '+str(j), 0 <= hi-lo <= 3*(j+1))
    global_bounds.append((lo,hi))
    if j % 512 == 0:
        print('Global full-degree conversion:', j+1, '/', N+1, flush=True)
report['stage'] = 'sixteen fixed cell restrictions'
save()

split_records = []
updates = 0


def split(bounds, a, b):
    """Midpoint de Casteljau; outward integer grid, including endpoints."""
    global updates
    work = list(bounds)
    left, right = [work[0]], [work[-1]]
    for r in range(1,N+1):
        work = [((x[0]+y[0])//2, -((-(x[1]+y[1]))//2))
                for x,y in zip(work,work[1:])]
        updates += len(work)
        left.append(work[0])
        right.append(work[-1])
    right.reverse()
    split_records.append(dict(interval=[str(a),str(b)],
        left=[[str(x),str(y)] for x,y in left],
        right=[[str(x),str(y)] for x,y in right]))
    print('Restricted interval', a, b, '; split', len(split_records), '/16', flush=True)
    return left,right


_, right = split(global_bounds,F(0),F(8))
leaves = [(F(4),F(8),right)]
for depth in range(4):
    refined = []
    for a,b,values in leaves:
        l,r = split(values,a,b)
        mid = (a+b)/2
        refined.extend([(a,mid,l),(mid,b,r)])
    leaves = refined
check('exact stipulated cells', len(leaves) == 16 and len(split_records) == 16
      and all(a == F(16+i,4) and b == F(17+i,4) for i,(a,b,_) in enumerate(leaves)))

cells = []
negative_total = 0
for i,(a,b,bounds) in enumerate(leaves):
    check('all full cell coefficients '+str(i), len(bounds) == N+1 and all(x<=y for x,y in bounds))
    neg = sum(max(-x,0) for x,y in bounds)
    mass_over_pi6 = F(neg,4*(N+1)*G)
    allowance = exp_hi*pi_hi**6*mass_over_pi6
    negative_total += neg
    cells.append(dict(cell=i+16, interval=[str(a),str(b)],
        negative_lower_coefficients=sum(x<0 for x,y in bounds),
        negative_coefficient_sum_numerator=str(neg),
        normalized_integral_upper=str(mass_over_pi6),
        weighted_actual_units_upper=str(allowance), enclosure=shown(allowance)))

COEFF.write_text(json.dumps(dict(degree=N,grid=str(G),
    normalized='v_p(8x)/pi^6', power=[[str(x),str(y)] for x,y in power],
    global_bernstein=[[str(x),str(y)] for x,y in global_bounds],
    subdivisions=split_records,
    cells=[dict(interval=[str(a),str(b)],coefficients=[[str(x),str(y)] for x,y in v])
           for a,b,v in leaves]),indent=2)+'\n')
A = exp_hi*pi_hi**6*F(negative_total,4*(N+1)*G)
total = A+B
report['cells'] = cells
report['coefficient_artifact'] = COEFF.name
report['coefficient_sha256'] = hashlib.sha256(COEFF.read_bytes()).hexdigest()
report['exact'] = dict(compact_polynomial_upper=str(A), replacement_B=str(B),
    combined_upper=str(total), required_strict_upper=str(m), unused_margin=str(m-total),
    ratio=str(total/m), pi_upper=str(pi_hi),exp_upper=str(exp_hi),
    negative_coefficient_sum_numerator=str(negative_total))
report['summary'] = dict(degree=N,cells=16,coefficients_per_cell=N+1,
    subdivisions=16,midpoint_updates=updates,compact_upper=shown(A),
    replacement_upper=shown(B),combined_upper=shown(total),ratio=shown(total/m),
    unused_margin=shown(m-total),required_strict_upper=str(m),
    pass_strict=total<m,omitted_coefficients='NONE',outer_tail='UNPAID')
report['status'] = 'COMPACT_FIXED_CERTIFICATE_PASSED' if total<m else 'COMPACT_FIXED_CERTIFICATE_STOP'
report['stage'] = 'complete; independent coefficient verification required'
report['producer_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
save()
print('Result:',report['status'],'; compact <=',report['summary']['compact_upper']['upper'])
print('Combined <=',report['summary']['combined_upper']['upper'],'; required <',m)
print('Ratio <=',report['summary']['ratio']['upper'],'; failures:',report['failures'])
print('Full certificate:',OUT,'; full coefficients:',COEFF)
