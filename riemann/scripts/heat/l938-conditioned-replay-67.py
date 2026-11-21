#!/usr/bin/env python3
"""Necessary checks of the fixed candidate, at EXACT roots and vertex limits.

Rational interval arithmetic, with full theta-tail bounds for 0<u<=2.
This is not a uniform certificate and tests no other candidate.
"""
from collections import Counter
from fractions import Fraction as F
from hashlib import sha256
from math import factorial
from pathlib import Path
import importlib.util
import json
ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).with_suffix('.json')
def loadmod(name,path):
 s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
m=loadmod('exact65',Path(__file__).with_name('l938-simplex-gradient-obstruction-65.py'))
m.DEN=2**400
I=m.I
R={'scope':'one fixed rational candidate from step67; exact L942 zeros and vertex limits only','checks':[],'failures':[]}
def check(name,passed,actual=None,required=None):
 r=dict(name=name,passed=bool(passed),actual=actual,required=required);R['checks'].append(r)
 if not passed:R['failures'].append(r)
def poly_add(p,q,c=F(1)):
 if len(p)<len(q):p.extend([F(0)]*(len(q)-len(p)))
 for j,v in enumerate(q):p[j]+=c*v
 return p
def multiply(p,q):
 z=[F(0)]*(len(p)+len(q)-1)
 for i,a in enumerate(p):
  for j,b in enumerate(q):z[i+j]+=a*b
 return z
def monomial_two_block(shape,a,b):
 """m_shape(q^a,1^b) by exact allocation of equal-exponent multiplicities."""
 counts=sorted(Counter(shape).items());out=[F(0)]*(sum(shape)+1)
 def walk(j,k,l,power,den):
  if j==len(counts):
   if k<=a and l<=b:out[power]+=F(factorial(a)*factorial(b),factorial(a-k)*factorial(b-l)*den)
   return
  exponent,nr=counts[j]
  for n in range(nr+1):
   if k+n<=a and l+nr-n<=b:walk(j+1,k+n,l+nr-n,power+exponent*n,den*factorial(n)*factorial(nr-n))
 walk(0,0,0,0,1)
 return out

def score(x,pi):
 u=m.sqrt_interval(x);assert 0<u.lo<=u.hi<=2
 e2=m.exp_interval(2*u);half=m.exp_interval(u/2);k=I(0);kp=I(0)
 for n in range(1,13):
  z=pi*n*n*e2;c=half*m.exp_interval(-z)
  k+=c*(8*z**2-12*z);kp+=c*(-16*z**3+60*z*z-30*z)
 # 3 n^2 <= z_n <= 220 n^2, exp(u/2)<3, exp(3)>20.
 # For n>=13 successive n^6*20^(-n^2) majorants have ratio <2/20^27.
 rho=F(2,20**27)
 ck=3*(8*220**2+12*220);cp=3*(16*220**3+60*220**2+30*220)
 tk=F(ck*13**4,20**169)/(1-rho);tp=F(cp*13**6,20**169)/(1-rho)
 k+=I(0,tk);kp+=I(-tp,tp);assert k.lo>0
 h=kp/(2*u*k)
 return h,dict(x=x.data(),u=u.data(),K=k.data(),K_prime=kp.data(),K_tail=str(tk),K_prime_tail=str(tp),h=h.data())

def main():
 source=Path(__file__).with_name('l938-conditioned-endpoints-67.json')
 prev=Path(__file__).with_name('l938-full-field-screen-66.json')
 data=json.loads(source.read_text());old=json.loads(prev.read_text())
 coeff=list(map(F,data['candidate']['field_basis_coefficients']));basis=old['basis']
 R['input_sha256']={str(p.relative_to(ROOT)):sha256(p.read_bytes()).hexdigest() for p in (source,prev,Path(__file__),Path(m.__file__))}
 pi=16*m.atan_reciprocal(5)-4*m.atan_reciprocal(239)
 check('global exponential bounds for theta tail',m.exp_point(F(3)).lo>20 and m.exp_point(F(4)).hi<55 and m.exp_point(F(1)).hi<3)
 check('successive omitted-majorant ratio',F(14,13)**6<2)
 rootdata=json.loads(Path(__file__).with_name('l938-simplex-gradient-obstruction-65.json').read_text())
 R['witnesses']=[]
 for w in rootdata['witnesses']:
  count=w['m'];n=12-count;lo,hi=map(F,w['root_bracket'])
  num=[1485,-2562,9415,-9996,6795,-2002,-63] if count==1 else [-3717,287497,-3221575,10631299,-5542978,-29318198,69213634,-63981834,29038487,-6214019,451605,13111,-1632]
  for _ in range(100):
   mid=(lo+hi)/2
   if m.polynomial_eval(num,mid)>0:lo=mid
   else:hi=mid
  check(f'm={count} refined exact root endpoint signs',m.polynomial_eval(num,lo)>0>m.polynomial_eval(num,hi))
  # Existing L942 derivative certificate applies on the containing interval.
  g=[F(0)];jpoly=[F(0)]
  for c,b in zip(coeff,basis):
   mu=tuple(b['mu']);cnt=Counter(mu)
   for r,sign in ((b['r'],1),(b['s'],-1)):
    nu=list(mu);nu.remove(r);nu=tuple(nu);nr=cnt[r]
    if r==1:lower=nu;fac=12-len(nu)
    else:lower=tuple(sorted(nu+(r-1,),reverse=True));fac=lower.count(r-1)
    poly_add(g,monomial_two_block(lower,count,n),c*sign*F(2*r-1,2)*fac/nr)
    qterm=[F(0)]*r+monomial_two_block(nu,count-1,n)
    poly_add(jpoly,qterm,c*sign*F(count,nr))
  root=I(lo,hi);ss=count*root+n;gvalue=m.polynomial_eval(g,root)/ss**12;jvalue=m.polynomial_eval(jpoly,root)/ss**13
  entry=dict(m=count,root_bracket=[str(lo),str(hi)],polynomial_divergence=list(map(str,g)),first_block_field_sum=list(map(str,jpoly)),energies=[])
  for energy in (F(1,4),F(4)):
   hq,qcert=score(energy*root/ss,pi);h1,onecert=score(I(energy)/ss,pi)
   residual=gvalue+energy*jvalue*(hq-h1)
   label='positive' if residual.lo>0 else 'negative' if residual.hi<0 else 'undecided'
   entry['energies'].append(dict(E=str(energy),score_q=qcert,score_one=onecert,residual=residual.data(),coarse_residual=m.coarse_bounds(residual,10**12),sign=label))
   check(f'candidate strictly positive at exact m={count} root E={energy}',residual.lo>0,label,'positive; necessary only')
  R['witnesses'].append(entry)
 # Every basis field vanishes at a vertex; only its polynomial divergence remains.
 vertex=F(0)
 for c,b in zip(coeff,basis):
  mu=tuple(b['mu']);cnt=Counter(mu)
  for r,sgn in ((b['r'],1),(b['s'],-1)):
   nu=list(mu);nu.remove(r);nu=tuple(nu)
   if r==1:lower=nu;fac=12-len(nu)
   else:lower=tuple(sorted(nu+(r-1,),reverse=True));fac=lower.count(r-1)
   if lower==(12,):vertex+=c*sgn*F(2*r-1,2)*fac/cnt[r]
 R['vertex']={'residual':str(vertex),'all_energies':'same exact value; X=0 and Pbar=0','required':'>0'}
 check('candidate positive vertex limits',vertex>0,'positive' if vertex>0 else 'nonpositive','>0')
 R['result']='necessary checks only; no uniform certificate or full-class dual'
 OUT.write_text(json.dumps(R,indent=2)+'\n')
 print(R['result'])
 for w in R['witnesses']:
  for e in w['energies']:print('m=',w['m'],'E=',e['E'],'sign=',e['sign'],'residual enclosure=',e['coarse_residual'])
 print('Vertex sign:','positive' if vertex>0 else 'nonpositive','checks:',len(R['checks']),'failures:',len(R['failures']),'full record:',OUT.relative_to(ROOT))
if __name__=='__main__':main()
