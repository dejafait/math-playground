#!/usr/bin/env python3
"""Complete internal rational evidence inspection; not an independent node replay."""
from fractions import Fraction as Q
from math import factorial, comb
from pathlib import Path
import hashlib
import json

root = Path(__file__).resolve().parent
cpath, ppath = root/'origin_margin_2231.json', root/'origin_margin_preflight_2231.json'
c, p = json.loads(cpath.read_text()), json.loads(ppath.read_text())
checks, failures = [], []


def check(name, condition):
    checks.append(dict(name=name, passed=bool(condition)))
    if not condition:
        failures.append(name)


def interval(a):
    return Q(a['lower']), Q(a['upper'])


def add(a, b):
    return a[0]+b[0], a[1]+b[1]


def mul(a, b):
    v = [x*y for x in a for y in b]
    return min(v), max(v)


def contains(outer, inner):
    return outer[0] <= inner[0] <= inner[1] <= outer[1]


check('preflight hash', hashlib.sha256(ppath.read_bytes()).hexdigest() == c['preflight_sha256'])
check('source hash', hashlib.sha256((root/'origin_margin_2231.py').read_bytes()).hexdigest() == c['script_sha256'])
check('parameters', c['parameters'] == p['parameters'] == dict(U=4, N=4, panels=65536,
      spatial_cells=1024, parameter_cells=32, degree=8, digits=80, center='57/4', radius='1/4', bracket=['14','29/2']))
max4, compact9 = [Q(0)]*9, Q(0)
for k, row in enumerate(p['spatial_cells']):
    l, r = interval(row['interval'])
    check(f'spatial coverage{k}', row['index'] == k and (l,r) == (Q(k,256), Q(k+1,256)))
    eb = list(map(Q, row['kernel_derivative_bounds']))
    check(f'spatial finite nonnegative{k}', len(eb) == 5 and all(x >= 0 for x in eb))
    part = (r-l)*r**9*eb[0]
    check(f'ninth cell{k}', Q(row['ninth_moment_part']) >= part)
    compact9 += Q(row['ninth_moment_part'])
    for j in range(9):
        pp = [r**(j-s)/factorial(j-s) if s <= j else Q(0) for s in range(5)]
        db = [sum((comb(t,s)*pp[s]*eb[t-s] for s in range(t+1)), Q(0)) for t in range(5)]
        b4 = sum((comb(4,t)*db[t]*Q(57,4)**(4-t) for t in range(5)), Q(0))
        max4[j] = max(max4[j], b4)
check('all spatial cells', len(p['spatial_cells']) == 1024)
cn = c['complete_ninth']
check('ninth agreement', cn == p['complete_ninth'])
check('ninth compact sum', Q(cn['compact']) >= compact9)
check('complete ninth', Q(cn['bound']) >= Q(cn['compact'])+Q(cn['index'])+Q(cn['spatial']))
remainder = Q(cn['remainder'])
check('Taylor remainder', remainder >= Q(cn['bound'])*Q(1,4)**9/factorial(9))
coefficients = []
for j, row in enumerate(c['coefficients']):
    e = row['errors']
    check(f'coefficient record{j}', row['j'] == j and e == p['errors'][j] and e['j'] == j)
    check(f'fourth derivative{j}', Q(e['fourth_derivative']) >= max4[j])
    check(f'Simpson{j}', Q(e['simpson']) >= Q(4**5,180*65536**4)*Q(e['fourth_derivative']))
    total = Q(row['total_error'])
    check(f'coefficient errors{j}', total >= sum((Q(e[key]) for key in ('simpson','index','spatial')),Q(0)))
    q, a = interval(row['quadrature']), interval(row['enclosure'])
    check(f'coefficient enclosure{j}', contains(a, (q[0]-total,q[1]+total)))
    coefficients.append(a)
check('all coefficients', len(coefficients) == 9)
k0 = interval(c['k0']['enclosure'])
k0f = interval(c['k0']['finite'])
check('K0 index tail', c['k0']['index_tail'] == p['k0_index_tail'])
check('K0 enclosure', contains(k0,(k0f[0],k0f[1]+Q(c['k0']['index_tail']))))
margins = []
for k, row in enumerate(c['parameter_cells']):
    xx = tuple(map(Q,row['x']))
    check(f'parameter coverage{k}', row['index'] == k and xx == (Q(14)+Q(k,64),Q(14)+Q(k+1,64)))
    delta = interval(row['delta'])
    check(f'parameter shift{k}', contains(delta,(xx[0]-Q(57,4),xx[1]-Q(57,4))))
    polynomial = coefficients[8]
    for j in range(7,-1,-1):
        polynomial = add(mul(polynomial,delta),coefficients[j])
    pr = interval(row['polynomial'])
    check(f'Horner{k}', contains(pr,polynomial))
    sine = interval(row['complete_sine_integral'])
    check(f'complete sine{k}', contains(sine,(pr[0]-remainder,pr[1]+remainder)))
    product = mul(xx,sine)
    margin = interval(row['margin'])
    check(f'origin margin{k}', contains(margin,(product[0]-k0[1],product[1]-k0[0])))
    check(f'rational margin{k}', margin[0] > Q(1,5))
    margins.append(margin)
check('all parameter cells',len(margins)==32)
check('uniform hull', contains(interval(c['uniform_margin']), (min(m[0] for m in margins),max(m[1] for m in margins))))
for label, artifact in [('preflight',p),('certificate',c)]:
    rr=artifact['runtime']
    check(label+' no failures', artifact['failures']==[])
    check(label+' no exceptional signals', rr['unexpected_signals']==[] and
          all(not value or signal in ('Inexact','Rounded') for flags in rr['flags'].values() for signal,value in flags.items()))
check('node and rotation counts', c['runtime']['counts']['nodes']==65537 and c['runtime']['counts']['trig_rotations']==65536)
out = root/'origin_margin_inspection_2231.json'
result = dict(status='PASS' if not failures else 'FAIL', checks=checks, failures=failures,
              inspected=dict(spatial_cells=1024,coefficients=9,parameter_cells=32),
              rational_lower_bound='1/5', uniform_margin=c['uniform_margin'],
              scope='Every serialized cell/error/range consumed; rational reconstruction, not independent exp bounds or node replay.',
              certificate_sha256=hashlib.sha256(cpath.read_bytes()).hexdigest())
out.write_text(json.dumps(result,indent=2)+'\n')
print(result['status'],len(checks),'checks; failures:',failures)
print('Actual lower:',c['uniform_margin']['lower'],'required > 1/5 > 0; evidence:',out)
if failures:
    raise SystemExit(1)
