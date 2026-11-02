#!/usr/bin/env python3
"""Exact rational certificate for one nonnegative L586 entry function."""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json

def add(a,b):
 c=a.copy()
 for n,v in b.items():c[n]=c.get(n,F(0))+v
 return c
def scale(a,s):return {n:v*s for n,v in a.items()}
def mul(a,b):
 c={}
 for n,v in a.items():
  for k,w in b.items():c[n+k]=c.get(n+k,F(0))+v*w
 return c
P={0:{0:F(1)},2:{0:F(-1,2),2:F(3,2)},4:{0:F(3,8),2:F(-30,8),4:F(35,8)},6:{0:F(-5,16),2:F(105,16),4:F(-315,16),6:F(231,16)}}
q={};norm=sum(F(2*k+1)*p[0]**2 for k,p in P.items())
for k,p in P.items():q=add(q,{n:v*2**n*(2*k+1)*p[0]/norm for n,v in p.items()})
p=mul(q,q)
# basis: 1,u^2,u^4,cos u,u^2 cos u,u^4 cos u,u sin u,u^3 sin u
spec=[('poly',0),('poly',2),('poly',4),('cos',0),('cos',2),('cos',4),('sin',1),('sin',3)]
def coeff(kind,shift,n):
 k=n-shift
 if kind=='poly':return F(k==0)
 if k<0 or k%2!=(kind=='sin'):return F(0)
 return F((-1)**(k//2),factorial(k))
mat=[[coeff(t,s,n) for t,s in spec]+[p.get(n,F(0))] for n in range(0,16,2)]
for i in range(8):
 j=next(j for j in range(i,8) if mat[j][i]);mat[i],mat[j]=mat[j],mat[i]
 v=mat[i][i];mat[i]=[a/v for a in mat[i]]
 for j in range(8):
  if j!=i:
   v=mat[j][i];mat[j]=[a-v*b for a,b in zip(mat[j],mat[i])]
c=[mat[i][-1] for i in range(8)]
N=50
err=sum(abs(sum(cj*coeff(t,s,n) for cj,(t,s) in zip(c,spec))-p.get(n,F(0)))/2**n for n in range(16,N+1,2))
# For each trig series, all omitted terms after exponent N; consecutive
# absolute terms on |u|<=1/2 have ratio <=1/4, so geometric factor 4/3.
tail=F(0)
for cj,(t,s) in zip(c,spec):
 if t=='poly':continue
 n=N+2
 tail+=abs(cj*coeff(t,s,n))*F(1,2**n)*F(4,3)
err+=tail
integral_p=sum(v/F((n+1)*2**n) for n,v in p.items())
delta=F(1,400)
ratio=(integral_p+2*delta)/(1+delta)
assert q[0]==1 and integral_p==F(256,1225)
assert all(sum(cj*coeff(t,s,n) for cj,(t,s) in zip(c,spec))==p.get(n,F(0)) for n in range(0,16,2))
assert err<F(11,5000)<delta
assert ratio<F(2,9)
assert ratio/64<F(1,288)
def exact(x):return str(x)
cert={
 "status":"PASS",
 "basis":[t+":"+str(s) for t,s in spec],
 "basis_coefficients":[exact(x) for x in c],
 "q_coefficients":{str(n):exact(v) for n,v in q.items()},
 "matched_even_degrees":list(range(0,16,2)),
 "tail_start_degree":N+2,
 "uniform_error_exact":exact(err),
 "uniform_error_proved_upper":"11/5000",
 "uniform_error_required_upper":exact(delta),
 "square_integral":exact(integral_p),
 "zero_atom_upper":exact(ratio),
 "zero_atom_required_upper":"2/9",
 "clipped_mean_upper":exact(ratio/64),
 "clipped_mean_required":"1/288",
 "strict_gap":exact(F(1,288)-ratio/64),
 "failures":[]}
out=Path(__file__).with_name('zero_atom_certificate.json')
out.write_text(json.dumps(cert,indent=2)+"\n")
print('PASS: uniform Taylor error < 11/5000 < 1/400; zero atom <=',ratio,'< 2/9')
print('Clipped mean <=',ratio/64,'< 1/288; strict gap =',F(1,288)-ratio/64)
print('Failures: 0; full exact certificate:',out)
