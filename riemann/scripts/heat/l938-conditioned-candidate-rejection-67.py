#!/usr/bin/env python3
"""Rigorous full-kernel counterexample to ONE fixed rational candidate.
No obstruction to the degree-13 field class is asserted.
"""
from collections import Counter
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import importlib.util
import json

def load(name,p):
 s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
here=Path(__file__).resolve().parent
m=load('replay67',here/'l938-conditioned-replay-67.py')
I=m.I
OUT=Path(__file__).with_suffix('.json')

def monomials(t):
 shapes=[p for n in range(13) for p in partitions(n)]
 result={p:F(0) for p in shapes};result[()]=F(1)
 for i,x in enumerate(t):
  power=[x**j for j in range(13)]
  for p in reversed(shapes[1:]):
   if len(p)>i+1:continue
   for r in set(p):
    q=list(p);q.remove(r);result[p]+=power[r]*result[tuple(q)]
 return result

def partitions(n,top=None):
 if n==0:yield ();return
 for j in range(min(n,n if top is None else top),0,-1):
  for rest in partitions(n-j,j):yield (j,)+rest

def main():
 fit=here/'l938-conditioned-endpoints-67.json';held=here/'l938-conditioned-heldout-67.json';old=here/'l938-full-field-screen-66.json'
 data=json.loads(fit.read_text());hd=json.loads(held.read_text());baseline=json.loads(old.read_text())
 rec=hd['endpoint_and_midpoint'][-1];t=list(map(F,rec['minimum_sample']['t']));E=F(rec['E'])
 full=monomials(t);leave=[monomials(t[:i]+t[i+1:]) for i in range(12)]
 field=[F(0)]*12;poly=F(0)
 for c,b in zip(map(F,data['candidate']['field_basis_coefficients']),baseline['basis']):
  mu=tuple(b['mu']);cnt=Counter(mu)
  for r,sgn in ((b['r'],1),(b['s'],-1)):
   nu=list(mu);nu.remove(r);nu=tuple(nu);nr=cnt[r]
   for i in range(12):field[i]+=c*sgn*t[i]**r*leave[i][nu]/nr
   if r==1:shape=nu;fac=12-len(nu)
   else:shape=tuple(sorted(nu+(r-1,),reverse=True));fac=shape.count(r-1)
   poly+=c*sgn*F(2*r-1,2)*fac*full[shape]/nr
 assert sum(field)==0
 p=sum((F(row['coefficient_of_m_mu'])*full[tuple(row['mu'])] for row in baseline['Pbar_rows']),F(0))
 pi=16*m.m.atan_reciprocal(5)-4*m.m.atan_reciprocal(239)
 hs=[];cert=[]
 for x in t:
  h,c=m.score(I(E*x),pi);hs.append(h);cert.append(c)
 a=F(data['candidate']['a0'])+E*F(data['candidate']['a1'])
 radial=(17+E*sum((x*h for x,h in zip(t,hs)),I(0)))*p
 divergence=I(poly)+E*sum((x*h for x,h in zip(field,hs)),I(0))
 residual=radial+divergence-a*p
 report={'scope':'one fixed candidate only; not a full-class dual or a crossing counterexample',
  'input_sha256':{str(q.relative_to(m.ROOT)):sha256(q.read_bytes()).hexdigest() for q in (fit,held,old,Path(__file__),Path(m.__file__),Path(m.m.__file__))},
  'E':str(E),'t':list(map(str,t)),'sample_label':rec['minimum_sample']['label'],
  'field_values':list(map(str,field)),'exact_field_sum':str(sum(field)),
  'Pbar':str(p),'polynomial_divergence':str(poly),'a_E':str(a),
  'theta':cert,'radial':radial.data(),'divergence':divergence.data(),'residual':residual.data(),
  'coarse_residual':m.m.coarse_bounds(residual,10**9),
  'arithmetic':'exact integers/Fractions; 2^-400 outward intervals; rational exp/sqrt/pi and full tails of replay67',
  'checks':[{'name':'positive rational simplex point','passed':all(x>0 for x in t) and sum(t)==1},
   {'name':'field exactly tangent','passed':sum(field)==0},
   {'name':'strict candidate rejection','passed':residual.hi<0,'actual':m.m.coarse_bounds(residual,10**9),'required':'upper bound <0'}]}
 report['failures']=[r for r in report['checks'] if not r['passed']]
 report['result']='fixed rational candidate rigorously rejected' if residual.hi<0 else 'necessary witness inconclusive'
 OUT.write_text(json.dumps(report,indent=2)+'\n')
 print(report['result'],'E=',E,'residual enclosure=',report['coarse_residual'],'required >=epsilon>0')
 print('Checks=',len(report['checks']),'failures=',len(report['failures']),'record=',OUT.relative_to(m.ROOT))
if __name__=='__main__':main()
