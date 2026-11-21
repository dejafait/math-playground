#!/usr/bin/env python3
"""Exact rational interval certificate for the one approved actual-kernel J5."""
from fractions import Fraction as F
from math import comb, factorial
from decimal import Decimal, localcontext
from pathlib import Path
import json
P=256
S=1<<P
N=8
OUT=Path(__file__).with_suffix('.json')
def floor(q): return q.numerator//q.denominator
def ceil(q): return -floor(-q)
class I:
    def __init__(self,lo,hi=None):
        self.lo,self.hi=lo,lo if hi is None else hi
        assert self.lo<=self.hi
    @classmethod
    def q(cls,a,b=None):
        a=F(a); b=a if b is None else F(b)
        return cls(floor(a*S),ceil(b*S))
    def __add__(a,b):
        b=asI(b); return I(a.lo+b.lo,a.hi+b.hi)
    __radd__=__add__
    def __neg__(a): return I(-a.hi,-a.lo)
    def __sub__(a,b): return a+-asI(b)
    def __rsub__(a,b): return asI(b)+-a
    def __mul__(a,b):
        b=asI(b); c=[x*y for x in (a.lo,a.hi) for y in (b.lo,b.hi)]
        return I(min(c)//S,-((-max(c))//S))
    __rmul__=__mul__
    def __truediv__(a,b):
        b=asI(b); assert not b.lo<=0<=b.hi
        c=[F(x*S,y) for x in (a.lo,a.hi) for y in (b.lo,b.hi)]
        return I(floor(min(c)),ceil(max(c)))
    def __pow__(a,n):
        assert n>=0
        r=I.q(1)
        while n:
            if n&1:r=r*a
            a=a*a;n//=2
        return r
    def record(a):
        with localcontext() as c:
            c.prec=18
            view=[str(Decimal(x)/Decimal(S)) for x in (a.lo,a.hi)]
        return {'lo_integer':str(a.lo),'hi_integer':str(a.hi),'denominator_power_of_two':P,'decimal_preview':view}
def asI(a):return a if isinstance(a,I) else I.q(a)
def atan_bounds(q,M):
    v=sum((F((-1)**k,(2*k+1)*q**(2*k+1)) for k in range(M)),F(0))
    w=v+F((-1)**M,(2*M+1)*q**(2*M+1))
    return I.q(min(v,w),max(v,w))
pi=16*atan_bounds(5,120)-4*atan_bounds(239,40)
assert 3*S<pi.lo<pi.hi<4*S
# Taylor alternating enclosure at rational endpoints; t=x/1024 is in [0,1].
def exp_minus_endpoint(x):
    t=x/1024
    assert 0<=t<=1
    s=sum(((-t)**k/F(factorial(k)) for k in range(61)),F(0))
    low=s+(-t)**61/F(factorial(61))
    return I.q(low,s)**1024
def exp_minus(x):
    low=exp_minus_endpoint(F(x.hi,S))
    high=exp_minus_endpoint(F(x.lo,S))
    return I(low.lo,high.hi)
def poly_value(q,x):
    r=I.q(0)
    for a in reversed(q):r=r*x+a
    return r
polys=[[F(0),F(-12),F(8)]]
for j in range(6):
    q=polys[-1]; r=[F(0)]*(len(q)+1)
    for d,c in enumerate(q):
        r[d]+=(F(1,2)+2*d)*c;r[d+1]-=2*c
    polys.append(r)
rows=[]; ds=[I.q(0) for j in range(7)]
for n in range(1,N+1):
    v=pi*n*n;e=exp_minus(v)
    terms=[poly_value(q,v)*e for q in polys]
    ds=[d+t for d,t in zip(ds,terms)]
    rows.append({'n':n,'v':v.record(),'exp_minus_v':e.record(),'derivative_terms':[t.record() for t in terms]})
tails=[]
for j,q in enumerate(polys):
    # deg Q_j<=8; v<=4n² and n>=1 imply |Q_j(v)|<=B_j n^16.
    B=sum((abs(c)*4**d for d,c in enumerate(q)),F(0))
    m=N+1
    tail=2*B*m**16/F(2**(4*m*m))
    tails.append({'j':j,'B':str(B),'bound':str(tail)})
    ds[j]=ds[j]+I.q(-tail,tail)
assert ds[0].lo>0
# Exact theta parity, independently justified in the canonical proof, sets odd jets to zero.
r2,r4,r6=(ds[j]/ds[0] for j in (2,4,6))
k2=r2;k4=r4-3*r2**2;k6=r6-15*r4*r2+30*r2**3
a1,a3,a5=-k2,k4,-k6
A,B,C=a5,10*a3,5*a1
D=B**2-4*A*C
checks={'K0_positive':ds[0].lo>0,'a1_positive':a1.lo>0,'a5_nonzero':a5.hi<0 or a5.lo>0,'discriminant_positive':D.lo>0,'opposite_y_root_signs':(A*C).hi<0}
# If AC<0 and D>0, the y quadratic has one strictly negative and one positive root.
# Thus J5 has exactly three real zeros and one nonreal conjugate pair, all simple.
published={'K0':(ds[0],'1.78678','1.78680'),'a1':(a1,'18.72690','18.72691'),'a3':(a3,'-143.01494','-143.01493'),'a5':(a5,'-1548.74555','-1548.74554'),'D':(D,'2625391.45','2625391.46'),'AC':(A*C,'-145016.06','-145016.05')}
for name,(v,low,high) in published.items():
    checks['published_enclosure_'+name]=F(low)<F(v.lo,S)<=F(v.hi,S)<F(high)
for j in (1,3,5):checks['odd_derivative_encloses_zero_'+str(j)]=ds[j].lo<=0<=ds[j].hi
checks['all_tail_bounds_below_1e_60']=all(F(t['bound'])<F(1,10**60) for t in tails)
passed=all(checks.values())
cert={'target':'Fixed n=5 origin Jensen polynomial of h=(log(K(-iz)/K(0)))prime','precision_bits':P,'N':N,'pi_method':'Machin 16 atan(1/5)-4 atan(1/239); alternating sums M=120,40','pi':pi.record(),'exp_method':'alternating terms 0..60 and 61 bracket exp(-x/1024), monotone endpoints, repeated squaring to power1024','polynomials_Q':[[str(c) for c in q] for q in polys],'term_intervals':rows,'tail_method':'e^3>16; n^16 2^(-4n^2) ratio <=2^16 2^(-4(2n+1))<1/2 for n>=9','tail_bounds':tails,'kernel_derivatives':[d.record() for d in ds],'score_derivatives':{'a1':a1.record(),'a3':a3.record(),'a5':a5.record(),'a0_a2_a4':'exactly zero by proved theta parity'},'quadratic_in_y':{'A':A.record(),'B':B.record(),'C':C.record(),'D':D.record(),'AC':(A*C).record()},'published_enclosures':{k:[lo,hi] for k,(v,lo,hi) in published.items()},'checks':checks,'failures':[k for k,v in checks.items() if not v],'outcome':'NONREAL_PAIR_CERTIFIED' if passed else 'INCONCLUSIVE'}
OUT.write_text(json.dumps(cert,indent=2)+'\n')
print('Outcome:',cert['outcome'])
for name,v in [('K0',ds[0]),('a1',a1),('a3',a3),('a5',a5),('D',D),('AC',A*C)]:
    print(name, v.record()['decimal_preview'])
print('Required: K0>0, a1>0, a5!=0, D>0, AC<0; failures:',cert['failures'])
print('Certificate:',OUT.relative_to(Path.cwd()))
if not passed:raise SystemExit(1)
