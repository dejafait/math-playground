#!/usr/bin/env python3
"""Outward Decimal/Simpson certificate for actual centered Theta coefficients.
Run from notebook root: python3 scripts/centered-hermite/residue-moment-382.py
Only Python standard library. Full evidence is written beside this script.
"""
from decimal import Decimal as D, localcontext, ROUND_FLOOR, ROUND_CEILING
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import json

PREC = 60
N = 65536  # even; Simpson mesh on [0,2]
OUT = Path(__file__).with_name('residue-moment-382.json')

def rd(fn, rounding):
    with localcontext() as ctx:
        ctx.prec = PREC
        ctx.rounding = rounding
        return +fn()

class I:
    def __init__(self, lo, hi=None):
        self.lo = D(lo)
        self.hi = D(lo if hi is None else hi)
        assert self.lo <= self.hi
    @staticmethod
    def rat(q):
        q=F(q)
        return I(rd(lambda:D(q.numerator)/D(q.denominator),ROUND_FLOOR),
                 rd(lambda:D(q.numerator)/D(q.denominator),ROUND_CEILING))
    def __add__(self, other):
        b=cv(other)
        return I(rd(lambda:self.lo+b.lo,ROUND_FLOOR),rd(lambda:self.hi+b.hi,ROUND_CEILING))
    __radd__=__add__
    def __neg__(self):
        return I(self.hi.copy_negate(),self.lo.copy_negate())
    def __sub__(self, other): return self+-cv(other)
    def __rsub__(self, other): return cv(other)+-self
    def __mul__(self, other):
        b=cv(other)
        lows=[rd(lambda:x*y,ROUND_FLOOR) for x in (self.lo,self.hi) for y in (b.lo,b.hi)]
        highs=[rd(lambda:x*y,ROUND_CEILING) for x in (self.lo,self.hi) for y in (b.lo,b.hi)]
        return I(min(lows),max(highs))
    __rmul__=__mul__
    def __truediv__(self,other):
        b=cv(other)
        assert b.lo>0 or b.hi<0
        inv=I(rd(lambda:D(1)/b.hi,ROUND_FLOOR),rd(lambda:D(1)/b.lo,ROUND_CEILING))
        return self*inv
    def __pow__(self,n):
        assert n>=0
        r=I(1)
        for _ in range(n): r=r*self
        return r
    def exp(self):
        # Decimal.exp is correctly rounded to nearest; adjacent representables
        # enclose its exact value, regardless of the enclosing context's mode.
        with localcontext() as ctx:
            ctx.prec=PREC
            return I(self.lo.exp().next_minus(),self.hi.exp().next_plus())
    def pair(self): return [str(self.lo),str(self.hi)]

def cv(x): return x if isinstance(x,I) else I(x)

def atan_bounds(q,terms):
    s=sum((F((-1)**k,(2*k+1)*q**(2*k+1)) for k in range(terms)),F(0))
    t=F((-1)**terms,(2*terms+1)*q**(2*terms+1))
    return min(s,s+t),max(s,s+t)

alo,ahi=atan_bounds(5,50)
blo,bhi=atan_bounds(239,15)
# Machin identity pi/4=4 atan(1/5)-atan(1/239).
pi=16*I(I.rat(alo).lo,I.rat(ahi).hi)-4*I(I.rat(blo).lo,I.rat(bhi).hi)
assert pi.lo>D(3) and pi.hi<D(4)

# K_n^(r)=exp(u/2-v) P_r(v), v=pi*n^2*exp(2u).
# P_(r+1)=(1/2-2v)P_r+2v P_r'. The global bound
# v^k exp(-v)<=k! follows from the exponential series.
polys=[]
p={1:F(-12),2:F(8)}
for r in range(5):
    polys.append(p)
    q={}
    for k,c in p.items():
        q[k]=q.get(k,F(0))+(F(1,2)+2*k)*c
        q[k+1]=q.get(k+1,F(0))-2*c
    p=q
norms=[sum((abs(c)*factorial(k) for k,c in p.items()),F(0)) for p in polys]
bounds=[]
errors=[]
for p in range(0,9,2):
    bound=12*sum((comb(4,s)*F(factorial(p),factorial(p-s))*2**(p-s)*norms[4-s]
                  for s in range(min(4,p)+1)),F(0))
    bounds.append(bound)
    errors.append(I.rat(F(2,180)*F(2,N)**4*bound))

# Uniform for p=0,2,...,8. See canonical proof for both estimates.
n_tail=2*256*8*pi**2*I(9).exp()*1250*(-25*pi).exp()
u_tail=384*pi*(-pi*I(4).exp()/2).exp()
assert n_tail.hi<D('1e-20') and u_tail.hi<D('1e-30')

sums=[I(0) for _ in range(5)]
for i in range(N+1):
    u=I.rat(F(2*i,N))
    e2=(2*u).exp()
    eh=(u/2).exp()
    k=I(0)
    for n in range(1,5):
        v=pi*(n*n)*e2
        # W(v)=8v^2-12v is increasing on v>=pi>3.
        w=8*v**2-12*v
        k=k+eh*w*(-v).exp()
    weight=1 if i in (0,N) else (4 if i%2 else 2)
    u2=u*u
    power=I(1)
    for j in range(5):
        sums[j]=sums[j]+weight*k*power
        power=power*u2
    if i and i%16384==0:
        print(f'validated quadrature nodes {i}/{N}',flush=True)

moments=[]
for j,s in enumerate(sums):
    quadrature=s*I.rat(F(2,3*N))
    # Simpson error is two-sided; omitted positive tails only enlarge upper.
    err=errors[j]
    moments.append(quadrature+I(err.hi.copy_negate(),err.hi)+I(0,n_tail.hi)+I(0,u_tail.hi))
assert moments[0].lo>0
rawgamma=[moments[j]*factorial(j)/factorial(2*j) for j in range(5)]
gamma=[v/moments[0] for v in rawgamma]
gamma[0]=I(1) # exact normalized constant
c=gamma[1]
b2=gamma[2]-c**2
b3=gamma[3]-3*c*gamma[2]+2*c**3
b4=gamma[4]-4*c*gamma[3]+6*c**2*gamma[2]-3*c**4
claims={'b2_lower_gt_minus_0.000038': b2.lo>D('-0.000038'),
        'b2_upper_lt_minus_0.000037': b2.hi<D('-0.000037'),
        'b4_lower_gt_0.00000000016': b4.lo>D('0.00000000016'),
        'b4_upper_lt_0.00000000018': b4.hi<D('0.00000000018')}
cert={'precision':PREC,'method':'composite Simpson with outward Decimal intervals',
      'mesh_intervals':N,'domain':['0','2'],'retained_n':[1,2,3,4],
      'pi_interval':pi.pair(),'machin_arctan_terms':[50,15],
      'derivative_polynomials':[{str(k):str(v) for k,v in p.items()} for p in polys],
      'derivative_bounds':[str(v) for v in bounds],
      'simpson_errors':[v.pair() for v in errors],
      'n_tail_bound':n_tail.pair(),'u_tail_bound':u_tail.pair(),
      'moments':[v.pair() for v in moments],
      'normalized_gamma':[v.pair() for v in gamma],
      'centered':{'b2':b2.pair(),'b3':b3.pair(),'b4':b4.pair()},
      'required':{'b2':['-0.000038','-0.000037'],'b4':['0.00000000016','0.00000000018']},
      'claims':claims,'failures':[k for k,v in claims.items() if not v]}
OUT.write_text(json.dumps(cert,indent=2)+'\n')
print('actual centered bounds:',json.dumps(cert['centered']))
print('required: -0.000038 < b2 < -0.000037; 1.6e-10 < b4 < 1.8e-10')
print('failures:',cert['failures'])
print('certificate:',OUT)
assert all(claims.values())
