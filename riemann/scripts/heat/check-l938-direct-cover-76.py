#!/usr/bin/env python3
"""Exact certificate consistency plus independently accumulated point checks.

This checks range assembly, cover topology and selected exact point centers;
it does not independently implement the Taylor interval range algorithm.
"""
import hashlib,json,sys
from fractions import Fraction as F
from math import factorial
from pathlib import Path
sys.set_int_max_str_digits(0)
BASE=Path(__file__).resolve().parent
OUT=BASE/'l938-direct-cover-check-76.json'
r=json.loads((BASE/'l938-direct-cover-76.json').read_text())
p=json.loads((BASE/'actual-h2-energy-cell-polynomial-48.json').read_text())
S=int(r['arithmetic']['scale']); rr=list(map(int,p['numerators'])); den=int(p['denominator'])
result={'status':'IN_PROGRESS','checks':[],'failures':[],'exact_point_checks':[]}

def save():OUT.write_text(json.dumps(result,indent=2)+'\n')
def check(name,truth):
 result['checks'].append({'name':name,'passed':bool(truth)})
 if not truth:
  result['status']='FAILED';result['failures'].append(name);save();raise AssertionError(name)

check('producer complete',r['status']=='CERTIFIED_COMPACT_COVER' and not r['failures'] and
      all(x['passed'] is True for x in r['checks']))
check('producer code hash',r['producer_sha256']==hashlib.sha256((BASE/'l938-direct-cover-76.py').read_bytes()).hexdigest())
for name,h in r['input_hashes'].items():check('full input hash '+name,h==hashlib.sha256((BASE/name).read_bytes()).hexdigest())
nodes={(x['depth'],x['index']):x for x in r['nodes']}
check('unique nodes',len(nodes)==len(r['nodes']))
leaves=[]
Z=F(r['bounds']['beta_constant']);A=F(r['bounds']['product_error']);D=F(r['bounds']['product_derivative_error'])
for (d,i),x in nodes.items():
 a,b=map(F,x['E']);n=2**d
 check('exact dyadic interval '+str((d,i)),a==F(n+15*i,4*n) and b==F(n+15*(i+1),4*n))
 if x['decision']=='BISECT':
  check('two children '+str((d,i)),(d+1,2*i) in nodes and (d+1,2*i+1) in nodes)
 else:leaves.append(x)
 if d:check('parent '+str((d,i)),nodes[(d-1,i//2)]['decision']=='BISECT')
 for key in ['value','derivative']:
  if key not in x:continue
  obj=x[key];ev=obj['evidence'];cl,ch=map(int,ev['center_coefficient'])
  var=int(ev['variation_scaled']);rem=int(ev['taylor_remainder_scaled']);tail=int(ev['discarded_tail_scaled'])
  check('nonnegative errors '+key+str((d,i)),min(var,rem,tail)>=0 and cl<=ch)
  check('assembled polynomial range '+key+str((d,i)),list(map(int,obj['polynomial_scaled']))==[cl-var-rem-tail,ch+var+rem+tail])
  expected=Z*b**17*A if key=='value' else Z*b**16*(17*A+b*D)
  radius=int(obj['actual_radius_scaled'])
  check('outward actual error '+key+str((d,i)),F(radius-1,S)<expected<=F(radius,S))
  lo,hi=map(int,obj['polynomial_scaled'])
  check('assembled actual range '+key+str((d,i)),list(map(int,obj['actual_scaled']))==[lo-radius,hi+radius])
 decision=x['decision'];v=list(map(int,x['value']['actual_scaled']))
 if decision=='VALUE_POSITIVE':check('positive value '+str((d,i)),v[0]>0)
 elif decision=='VALUE_NEGATIVE':check('negative value '+str((d,i)),v[1]<0)
 elif decision=='DERIVATIVE_POSITIVE':check('positive derivative '+str((d,i)),int(x['derivative']['actual_scaled'][0])>0)
 else:check('only internal undecided nodes '+str((d,i)),decision=='BISECT' and d<12)
leaves.sort(key=lambda x:F(x['E'][0]))
check('closed outer endpoints',leaves[0]['E'][0]=='1/4' and leaves[-1]['E'][1]=='4')
check('complete closed cover',all(F(x['E'][1])==F(y['E'][0]) for x,y in zip(leaves,leaves[1:])))
check('budgets',len(nodes)==99<=8191 and len(leaves)==50 and max(d for d,i in nodes)==9<=12)

ratios=[]
for x in leaves:
 obj=x['derivative'] if x['decision']=='DERIVATIVE_POSITIVE' else x['value']
 lo,hi=map(int,obj['polynomial_scaled']);radius=int(obj['actual_radius_scaled'])
 ratios.append((F(-hi if x['decision']=='VALUE_NEGATIVE' else lo,radius),x['depth'],x['index']))
minimum=min(ratios)
check('complete minimum margin and strict bracket',minimum==(F(r['summary']['minimum_clearance_over_radius']['exact_ratio']),5,31) and 78557<minimum[0]<78558)

# Independent exact summation: direct ascending powers, distinct from the
# fixed-point Taylor/Horner algorithm used for interval ranges.
def exact_point(s,E):
 top=factorial(s+len(rr)-1); fact=factorial(s)
 # Common denominator den*top*E.denominator^(s+d).
 a,b=E.numerator,E.denominator;d=len(rr)-1
 acc=0;apow=a**s;bpow=b**d
 for ell,R in enumerate(rr):
  quotient,remainder=divmod(top,fact)
  if remainder:raise AssertionError('factorial quotient')
  acc+=R*quotient*apow*bpow
  apow*=a
  if ell<d:bpow//=b
  fact*=s+ell+1
 return F(acc,den*top*b**(s+d))

points=[]
for x in leaves:
 if x['decision']=='DERIVATIVE_POSITIVE':
  points.append((x,(F(x['E'][0])+F(x['E'][1]))/2,'crossing-leaf midpoint'))
points.extend([(leaves[0],F(1,4),'outer endpoint'),(leaves[-1],F(4),'outer endpoint')])
for x,E,kind in points:
 row={'E':str(E),'kind':kind,'node':[x['depth'],x['index']],'values':{}}
 for s,key in [(17,'value'),(16,'derivative')]:
  q=exact_point(s,E)
  # Use the matching node's derivative range only when it was needed.
  if key not in x:continue
  lo,hi=map(int,x[key]['polynomial_scaled'])
  check('independent full polynomial point '+key+' '+str(E),F(lo,S)<=q<=F(hi,S))
  if kind=='crossing-leaf midpoint':
   # At the center, only t_0 plus the discarded tail is needed.
   ev=x[key]['evidence'];cl,ch=map(int,ev['center_coefficient']);tail=int(ev['discarded_tail_scaled'])
   check('independent Taylor constant '+key+' '+str(E),F(cl-tail,S)<=q<=F(ch+tail,S))
  row['values'][key]=str(q)
 result['exact_point_checks'].append(row);save()
result['status']='PASSED';result['checked_nodes']=len(nodes);result['checked_closed_leaves']=len(leaves)
result['scope']='Every recorded range assembly, error radius, tree edge, decision and endpoint; independent exact full-polynomial point checks on all four crossing leaves and the two outer endpoints. Taylor range proof remains in L946.'
save()
print('PASSED:',len(result['checks']),'checks;',len(nodes),'nodes;',len(leaves),'closed leaves; failures:',result['failures'])
print('Certificate:',OUT)
