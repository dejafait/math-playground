#!/usr/bin/env python3
"""Check the selected coefficient via odd-product gamma normalization.

This verifies the coefficient contraction, not the full response norm,
and does not independently reconstruct the saved derivative prefixes.
"""
import hashlib
import json
import sys
from fractions import Fraction as Q
from math import comb, factorial
from pathlib import Path

sys.set_int_max_str_digits(0)
BASE=Path(__file__).resolve().parent
OUT=BASE/'l938-signed-response-check-89.json'
report=dict(status='IN_PROGRESS',checks=[],failures=[],inputs_sha256={})


def save():
    OUT.write_text(json.dumps(report,indent=2)+'\n')


def check(name,ok):
    report['checks'].append(dict(name=name,passed=bool(ok)))
    if not ok:
        report['failures'].append(name)
        report['status']='FAILED'
        save()
        raise AssertionError(name)


def read(name):
    raw=(BASE/name).read_bytes()
    report['inputs_sha256'][name]=hashlib.sha256(raw).hexdigest()
    return json.loads(raw)


save()
source=read('l938-signed-response-89.json')
data=read('l938-signed-response-coefficients-89.json')
check('coefficient artifact hash',report['inputs_sha256']['l938-signed-response-coefficients-89.json']
      ==source['coefficient_sha256'])
check('all producer checks',len(source['checks'])==10270 and not source['failures']
      and all(c['passed'] is True for c in source['checks']))
C=int(data['C']); cut=data['cut']; H=17+cut
grad=[list(map(int,row)) for row in data['gradients']]
check('all seven complete prefixes',len(grad)==7 and all(len(row)==cut+1 for row in grad))
D,N,j=2816,2822,1411
check('fixed full degrees and selected index',data['full_degree']==D and cut==j
      and (source['selected']['energy_degree'],source['selected']['residual_degree'],
           source['selected']['i'],source['selected']['j'])==(D,N,D,j))
odd=[1]
for h in range(1,H+1): odd.append(odd[-1]*(2*h-1))
numerator=0
for k,row in enumerate(grad):
    for l,d in enumerate(row):
        a=l+6-k
        if a>j: continue
        h=17-k+l
        check('odd product exact division '+str(k)+','+str(l),odd[H]%odd[h]==0)
        # Degree elevation in the independent falling-factorial form.
        old=comb(N-l-6,j-a)*factorial(N)
        new=comb(N,j)*(factorial(j)//factorial(j-a))
        new*=factorial(N-j)//factorial(N-j-k)
        new*=factorial(N-l-6)
        check('degree elevation falling factorial '+str(k)+','+str(l),old==new)
        numerator+=(d*2**h*(factorial(12)//factorial(2*k))*(odd[H]//odd[h])
                    *8**l*comb(N-l-6,j-a))
denominator=2*C**11*factorial(12)*odd[H]*comb(N,j)
b=Q(numerator,denominator)
check('complete selected signed coefficient',b==Q(source['selected']['coefficient'])
      ==Q(int(data['selected_numerator']),int(data['selected_denominator'])))
nu=Q(comb(N,j)*odd[j+11]*odd[N-j],2**(N+11)*factorial(N+11))
check('beta weight via odd gamma products',nu==Q(source['selected']['beta_mass_over_pi']))
mass=Q(source['selected']['energy_mass'])
check('positive endpoint energy mass brackets',Q(31,4)**17/(4*(D+1))<mass<Q(8)**17/(4*(D+1)))
lo,hi=(Q(source['selected']['contribution_'+s]) for s in ('lower','upper'))
margin=Q(source['second_order']['margin'])
check('selected contribution positive but below margin',0<lo<=hi<margin)
check('displayed coefficient full enclosure',Q(source['selected']['coefficient_enclosure']['lower'])
      <=b<=Q(source['selected']['coefficient_enclosure']['upper']))
report['witness']=dict(selected_coefficient=str(b),beta_weight_over_pi=str(nu),
    selected_contribution=source['selected']['contribution_enclosure'],required_full_sum_below=str(margin),
    conclusion='Selected term does not stop the test; full norm is still uncomputed.')
report['scope']='Odd-product gamma and falling-factorial contraction replay; derivative prefixes and kernel enclosure inherited, full coefficient sum not checked.'
report['status']='PASSED'
save()
print('Result:',report['status'],'; checks:',len(report['checks']),'; failures:',report['failures'])
print('Selected allowance:',report['witness']['selected_contribution'],'; required full sum <',margin)
print('Full norm: UNCOMPUTED; certificate:',OUT)
