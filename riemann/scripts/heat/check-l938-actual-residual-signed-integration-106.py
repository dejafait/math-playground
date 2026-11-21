#!/usr/bin/env python3
"""Exact replay of the complete new scalar ledger and all saved node contractions.

Does not independently produce transcendental values or derivative prefixes.
"""
import hashlib
import json
import sys
from fractions import Fraction as F
from pathlib import Path

sys.set_int_max_str_digits(0)
BASE=Path(__file__).resolve().parent
OUT=BASE/'l938-actual-residual-signed-integration-check-106.json'
checks, failures=[],[]


def check(name, condition):
    checks.append(dict(name=name,passed=bool(condition)))
    if not condition:
        failures.append(name)


def read(name):
    return json.loads((BASE/name).read_text())


def interval(obj):
    return F(obj['lower']),F(obj['upper'])


def mul(x,y):
    values=[a*b for a in x for b in y]
    return min(values),max(values)


def add(x,y):
    return x[0]+y[0],x[1]+y[1]


def power(x,n):
    # Only nonnegative factors are passed here.
    assert x[0]>=0
    return x[0]**n,x[1]**n


def contains(outer,inner):
    return outer[0]<=inner[0]<=inner[1]<=outer[1]


r=read('l938-actual-residual-signed-integration-106.json')
node_raw=(BASE/'l938-actual-residual-nodes-106.json').read_bytes()
nodes=json.loads(node_raw)
check('producer complete and all flags',r['status'].startswith('COMPLETED_CONDITIONAL_')
      and not r['failures'] and all(c['passed'] is True for c in r['checks']))
check('complete node artifact identity',hashlib.sha256(node_raw).hexdigest()==r['nodes_sha256']
      and nodes['status']=='COMPLETE' and len(nodes['nodes'])==4096)
for name,digest in r['inputs_sha256'].items():
    check('input identity '+name,hashlib.sha256((BASE/name).read_bytes()).hexdigest()==digest)
kernel=read('actual-h2-energy-cell-48.json')['approximation']
point=read('l938-pointwise-signed-response-104.json')['exact']
pi=interval(kernel['pi'])
a=r['analytic']
pmajor=sum((abs(F(int(c['chosen_numerator']),10**120))*F(3,2)**l
           for l,c in enumerate(kernel['chebyshev_coefficients'])),F(0))
check('full complex polynomial majorant',pmajor==F(a['polynomial_majorant']))
M=F(25,24)**17*(10**9+pmajor)*sum(map(F,a['response_absolute_sum_bounds']))
check('ellipse amplitude scalar normalization',M==F(a['amplitude_majorant']))
delta=4*M*F(2,3)**8191
err=2*pi[1]**6*8**17*delta
check('projection and both quadrature weight masses',delta==F(a['projection_error'])
      and err==F(a['quadrature_error']) and err>0)
complement=F(kernel['epsilon'])*pi[1]**6*F(point['complement_norm'])
second=F(point['second_order_upper'])
check('complete unchanged complement and Taylor remainder',complement==F(a['complement'])
      and second==F(a['second_order']) and complement>0 and second>0)
total=(F(0),F(0))
for j,node in enumerate(nodes['nodes']):
    check('ordered node '+str(j),node['j']==j)
    theta=mul(pi,(F(2*j+1,8192),)*2)
    check('node angle '+str(j),contains(interval(node['theta']),theta))
    z=interval(node['z'])
    y=interval(node['y'])
    check('affine y '+str(j),contains(y,((1+z[0])/2,(1+z[1])/2)) and 0<y[0]<=y[1]<1)
    omy=(1-y[1],1-y[0])
    x=interval(node['energy'])
    check('affine energy '+str(j),contains(x,(8*omy[0],8*omy[1])) and 0<x[0]<=x[1]<8)
    u=interval(node['sqrt_energy'])
    check('sqrt endpoint exact squares '+str(j),0<=u[0]**2<=x[0] and u[1]**2>=x[1])
    kval,pval,residual=map(interval,(node['kernel'],node['polynomial'],node['residual']))
    check('signed residual subtraction '+str(j),contains(residual,(kval[0]-pval[1],kval[1]-pval[0])))
    response=(F(0),F(0))
    for k,row in enumerate(node['response_rows']):
        term=mul(mul(power(y,6-k),power(omy,k)),interval(row))
        response=add(response,term)
    saved_response=interval(node['response'])
    check('all seven response row contraction '+str(j),contains(saved_response,response))
    amplitude=mul(mul(power(y,11),residual),saved_response)
    saved_amplitude=interval(node['amplitude'])
    check('amplitude normalization '+str(j),contains(saved_amplitude,amplitude))
    total=add(total,saved_amplitude)
    check('full exact partial sum '+str(j),contains(interval(node['running_sum']),total))
    if (j+1)%1024==0:
        print('Checked complete node contractions:',j+1,'/4096',flush=True)
saved_sum=interval(r['result']['signed_sum'])
check('final sum includes every saved amplitude',contains(saved_sum,total))
scale=(pi[0]**6*F(8**17,4096),pi[1]**6*F(8**17,4096))
quad=mul(scale,saved_sum)
saved_quad=interval(r['result']['signed_quadrature'])
check('pi6 energy17 quadrature normalization',contains(saved_quad,quad))
payment=err+complement+second
result=r['result']
lo=F(point['polynomial_endpoint_lower'])+saved_quad[0]-payment
hi=F(point['polynomial_endpoint_upper'])+saved_quad[1]+payment
check('all three external payments',payment==F(result['total_external_payment']))
check('full final exact enclosure',lo==F(result['actual_lower']) and hi==F(result['actual_upper']) and lo<=hi)
sign='POSITIVE' if lo>0 else 'NEGATIVE' if hi<0 else 'INCONCLUSIVE'
check('sign conclusion follows from full enclosure',sign==result['sign'] and (lo>0)==result['strict_positive_test'])
out=dict(status='PASSED' if not failures else 'FAILED',checks=checks,failures=failures,
    checked_node_count=len(nodes['nodes']),complete_signed_amplitude_sum=list(map(str,total)),
    sign=sign,actual_lower=str(lo),actual_upper=str(hi),
    scope='Exact scalar ledger and all saved node contractions; not independent '
          'theta/cosine/Clenshaw/response-Horner production or complex absolute-sum audit.')
OUT.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(dict(status=out['status'],checks=len(checks),failures=failures,sign=sign,
                     required_lower='>0',certificate=str(OUT)),indent=2))
if failures:
    sys.exit(1)
