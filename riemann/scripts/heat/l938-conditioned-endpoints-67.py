#!/usr/bin/env python3
"""Exact column conditioning plus ONE simultaneous endpoint diagnostic.

No uniform or interval certificate is claimed. Decimal evaluations are
high-precision diagnostics, not directed full-kernel enclosures.
"""
from collections import Counter
from decimal import Decimal as D, localcontext
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import importlib.util
import json
from math import factorial, prod
import numpy as np

ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).with_suffix('.json')
ARR=Path(__file__).with_suffix('.npz')
spec=importlib.util.spec_from_file_location('old66', Path(__file__).with_name('l938-full-field-screen-66.py'))
old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)
R={'scope':'fixed full degree-13 class, simultaneous endpoint diagnostic only',
   'checks':[], 'failures':[], 'stage':'initial'}
def save(): OUT.write_text(json.dumps(R,indent=2,allow_nan=False)+'\n')
def check(name,passed,actual=None,required=None):
 row=dict(name=name,passed=bool(passed),actual=actual,required=required)
 R['checks'].append(row)
 if not passed:R['failures'].append(row)
def dec(x):
 x=F(x);return D(x.numerator)/D(x.denominator)
def add(p,k,v):
 p[k]=p.get(k,F(0))+v
 if p[k]==0:del p[k]
def exact_conditioning(basis):
 """Column echelon on exact polynomial divergence and score moments j=1..4.
 Each operation is rational, and the returned triangular map is invertible.
 """
 pivots={};polys=[];transforms=[];labels=[]
 for col,b in enumerate(basis):
  mu=tuple(b['mu']);counts=Counter(mu);p={};tr={col:F(1)}
  for r,sgn in ((b['r'],1),(b['s'],-1)):
   nu=old.remove(mu,r);nr=counts[r]
   if r==1: shape=nu; fac=12-len(nu)
   else:shape=tuple(sorted(nu+(r-1,),reverse=True));fac=shape.count(r-1)
   add(p,(0,shape),sgn*F(2*r-1,2)*fac/nr)
   for j in range(1,5):
    shape=tuple(sorted(nu+(r+j,),reverse=True))
    add(p,(j,shape),sgn*F(shape.count(r+j),nr))
  while p:
   lead=min(p)
   if lead not in pivots:break
   ix=pivots[lead];c=p[lead]
   for k,v in polys[ix].items():add(p,k,-c*v)
   for k,v in transforms[ix].items():add(tr,k,-c*v)
  if not p:raise ArithmeticError('insufficient exact score-moment maps')
  lead=min(p);pivot=p[lead]
  p={k:v/pivot for k,v in p.items()};tr={k:v/pivot for k,v in tr.items()}
  pivots[lead]=col;polys.append(p);transforms.append(tr);labels.append(lead)
 check('all 171 columns retained by exact invertible triangular operations',len(transforms)==171,len(transforms),171)
 check('triangular map has nonzero diagonal',all(tr.get(j,0)!=0 and max(tr)==j for j,tr in enumerate(transforms)))
 R['exact_conditioning']={'score_moments_used':[1,2,3,4],
   'pivot_levels':dict(Counter(str(k[0]) for k in labels)),
   'transforms':[{str(k):str(v) for k,v in tr.items()} for tr in transforms],
   'pivot_labels':[[j,list(p)] for j,p in labels],
   'meaning':'T0 plus exact polynomial maps sum X_i*t_i^j; these condition the basis but do not approximate theta'}
 return transforms

def sym(values,maxdegree,maxlength):
 shapes=[p for n in range(maxdegree+1) for p in old.partitions(n) if len(p)<=maxlength]
 shape=values.shape[:-1]
 out={p:np.full(shape,D(0),dtype=object) for p in shapes};out[()][:]=D(1)
 for i in range(values.shape[-1]):
  powers=[np.full(shape,D(1),dtype=object)]
  for r in range(1,maxdegree+1):powers.append(powers[-1]*values[...,i])
  for p in reversed(shapes[1:]):
   if len(p)>i+1:continue
   for r in set(p):out[p]+=powers[r]*out[old.remove(p,r)]
 return out

def score(x):
 pi=D('3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679')
 if x==0:
  k=D(0);k2=D(0)
  for n in range(1,9):
   z=pi*n*n;e=(-z).exp();k+=(8*z*z-12*z)*e
   k2+=(32*z**4-224*z**3+330*z*z-75*z)*e
  return k2/(2*k)
 u=x.sqrt();k=D(0);kp=D(0)
 for n in range(1,9):
  z=pi*n*n*(2*u).exp();c=(u/2-z).exp()
  k+=(8*z*z-12*z)*c;kp+=(-16*z**3+60*z*z-30*z)*c
 return kp/(2*u*k)

def build_matrix(t,rows,basis,transforms,energies=(F(1,4),F(4))):
 full=sym(t,12,12)
 leave=sym(np.stack([np.delete(t,i,axis=1) for i in range(12)],axis=1),12,11)
 p=np.full(len(t),D(0),dtype=object)
 for row in rows:
  p+=dec(F(row['coefficient_of_m_mu'])*10**24)*full[tuple(row['mu'])]
 out=[];rad=[]
 for energy in energies:
  E=dec(energy);h=np.array([[score(E*x) for x in point] for point in t],dtype=object)
  cov={}
  for mu in [p for p in old.partitions(13) if len(p)<=12]:
   cnt=Counter(mu)
   for r,nr in cnt.items():
    nu=old.remove(mu,r)
    if r==1:base=(12-len(nu))*full[nu]
    else:
     lower=tuple(sorted(nu+(r-1,),reverse=True));base=lower.count(r-1)*full[lower]
    theta=E*np.sum(t**r*leave[nu]*h,axis=1)
    cov[mu,r]=((D(r)-D('.5'))*base+theta)/D(nr)
  original=[cov[tuple(b['mu']),b['r']]-cov[tuple(b['mu']),b['s']] for b in basis]
  conditioned=[sum((dec(c)*original[k] for k,c in tr.items()),np.full(len(t),D(0),dtype=object)) for tr in transforms]
  out.append(np.column_stack(conditioned+[-p,-E*p]))
  rad.append((17+E*np.sum(t*h,axis=1))*p)
  print('Decimal endpoint matrix built:',str(energy),flush=True)
 return np.concatenate(out),np.concatenate(rad)

def screen(a,d):
 """Untruncated SVD change of coordinates; bounded barrier diagnostic."""
 scale=np.linalg.norm(a,axis=0);ascaled=a/scale
 u,s,vt=np.linalg.svd(ascaled,full_matrices=False)
 R['numerical_conditioning']={'columns':a.shape[1], 'singular_values':s.tolist(),
  'smallest_to_largest':float(s[-1]/s[0]),'discarded_directions':0}
 check('endpoint matrix numerical rank threshold',s[-1]/s[0]>1e-13,float(s[-1]/s[0]),'>1e-13; no truncation allowed')
 if s[-1]/s[0]<=1e-13:return None
 q=u;ds=d/max(1.,np.max(np.abs(d)));dscale=max(1.,np.max(np.abs(d)))
 mat=np.column_stack([q,-np.ones(len(d))]);obj=np.zeros(a.shape[1]+1);obj[-1]=-1
 z=np.zeros(a.shape[1]+1);z[-1]=float(ds.min())-1
 path=[];stop='fixed schedule completed'
 for mu in (1.,.1,.01,.001,.0001,.00001,.000001,.0000001):
  for it in range(45):
   slack=ds+mat@z;grad=obj-mu*mat.T@(1/slack);weighted=mat/slack[:,None]
   try:direction=np.linalg.solve(mu*weighted.T@weighted,-grad)
   except np.linalg.LinAlgError:stop='singular Newton matrix';break
   slope=float(grad@direction)
   if not np.isfinite(slope) or slope>=0:stop='non-descent Newton direction';break
   if -slope<1e-11:break
   move=mat@direction;negative=move<0
   step=min(1.,float(np.min(-.99*slack[negative]/move[negative])) if np.any(negative) else 1.)
   value=float(obj@z-mu*np.log(slack).sum())
   for _ in range(55):
    prop=z+step*direction;ss=ds+mat@prop
    if np.all(ss>0) and obj@prop-mu*np.log(ss).sum()<=value+.01*step*slope:break
    step/=2
   else:stop='line search exhausted';break
   z=prop
   if np.max(np.abs(z))>1e8:stop='coefficient magnitude stop';break
  slack=ds+mat@z
  path.append(dict(mu=mu,iterations=it+1,epsilon=float(z[-1]*dscale),minimum_slack=float(slack.min())))
  R['screen_path']=path;R['stage']='barrier';save()
  if stop!='fixed schedule completed':break
 coeff=(vt.T@(z[:-1]/s))/scale*dscale
 dual=mu/(ds+mat@z);dual/=dual.sum()
 residual=d+a@coeff
 R['screen']={'stop':stop,'coefficients':coeff.tolist(),'sample_minimum':float(residual.min()),
  'epsilon':float(z[-1]*dscale),'dual_weights':dual.tolist(),'dual_radial':float(dual@d),
  'dual_scaled_column_defect_inf':float(np.max(np.abs(ascaled.T@dual))),
  'required':'uniform epsilon>0, or exact full-column dual with nonpositive radial value'}
 check('barrier completed without coefficient or solver stop',stop=='fixed schedule completed',stop)
 return coeff

def main():
 previous=ROOT/'scripts/heat/l938-full-field-screen-66.json'
 oldreport=json.loads(previous.read_text());basis=oldreport['basis'];rows=oldreport['Pbar_rows']
 paths=[previous,ROOT/'lemmas/L943-full-degree-thirteen-simplex-field-coordinates.md',ROOT/'lemmas/L942-actual-simplex-two-field-divergence-obstruction.md',Path(__file__)]
 R['input_sha256']={str(p.relative_to(ROOT)):sha256(p.read_bytes()).hexdigest() for p in paths}
 transforms=exact_conditioning(basis);R['stage']='exact conditioning saved';save()
 print('Exact conditioning levels:',R['exact_conditioning']['pivot_levels'],flush=True)
 # All 86 structured points (including both algebraic root MIDPOINTS),
 # plus 128 deterministic diverse rational points from the previous screen.
 records=oldreport['samples'];chosen=list(range(86))
 for start in (86,214,342,470):chosen.extend(range(start,start+32))
 records=[records[i] for i in chosen]
 R['samples']=records;R['energies']=['1/4','4']
 R['qualifications']=['Root samples are rational midpoints ONLY; exact L942 zeros remain mandatory for any final proof.',
  '80-digit Decimal arithmetic and eight theta terms are diagnostic, without directed rounding/full tail bounds.',
  'Exact column operations retain all fields, but sampled endpoint feasibility gives no uniform positivity.',
  'E-independent field and affine scalar; no degree, interval or multiplier expansion.']
 R['stage']='Decimal endpoint matrices pending';save()
 with localcontext() as ctx:
  ctx.prec=80
  t=np.array([[dec(F(x)) for x in r['t']] for r in records],dtype=object)
  a,d=build_matrix(t,rows,basis,transforms)
  af=np.array(a,dtype=float);df=np.array(d,dtype=float)
  R['stage']='matrices built';save();np.savez_compressed(ARR,columns=af,radial=df)
  coeff=screen(af,df)
  if coeff is not None:
   exactcoeff=[F(float(x)) for x in coeff]
   original=[F(0)]*171
   for c,tr in zip(exactcoeff[:171],transforms):
    for k,v in tr.items():original[k]+=c*v/10**24
   R['candidate']={'field_basis_coefficients':list(map(str,original)),
     'a0':str(exactcoeff[-2]),'a1':str(exactcoeff[-1]),'qualification':'rationalized candidate, uncertified'}
   residual=d+sum((a[:,j]*dec(c) for j,c in enumerate(exactcoeff)),np.full(len(d),D(0),dtype=object))
   R['decimal_replay']={'minimum':str(min(residual)), 'negative_count':sum(x<0 for x in residual),
    'endpoint_minima':[str(min(residual[:len(t)])),str(min(residual[len(t):]))],
    'sample_minimum_required':'>0; necessary, still not sufficient',
    'rounding_tail_contract':'none; 80-digit diagnostic only'}
   np.savez_compressed(ARR,columns=af,radial=df,residual=np.array(residual,dtype=float))
 R['stage']='finished';R['result']='EXPLORATION: no uniform certificate or rigorous full-class dual';save()
 print(R['result'])
 print('Numerical conditioning ratio:',R['numerical_conditioning']['smallest_to_largest'],'required >1e-13')
 if 'screen'in R:print('Barrier stop:',R['screen']['stop'],'sample minimum:',R['screen']['sample_minimum'])
 if 'decimal_replay'in R:print('Decimal replay:',R['decimal_replay'])
 print('Failures:',len(R['failures']),'record:',OUT.relative_to(ROOT),'arrays:',ARR.relative_to(ROOT))
if __name__=='__main__':main()
