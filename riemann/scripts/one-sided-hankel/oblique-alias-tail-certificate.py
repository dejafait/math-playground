"""Exact rational half-plane certificate for the complete higher-alias tail."""
from fractions import Fraction as F
from pathlib import Path
import json

class I:
    def __init__(self, lo, hi=None):
        self.lo=F(lo); self.hi=self.lo if hi is None else F(hi)
        assert self.lo<=self.hi
    def __add__(self, other):
        o=other if isinstance(other,I) else I(other)
        return I(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self,other): return self+-as_i(other)
    def __rsub__(self,other): return as_i(other)+-self
    def __mul__(self,other):
        o=as_i(other)
        v=[a*b for a in (self.lo,self.hi) for b in (o.lo,o.hi)]
        return I(min(v),max(v))
    __rmul__=__mul__

def as_i(a): return a if isinstance(a,I) else I(a)

failures=[]; checks=[]
def check(name,actual,required,relation='>'):
    ok=actual>required if relation=='>' else actual<required
    checks.append(dict(name=name,actual=str(actual),relation=relation,required=str(required),passed=ok))
    if not ok: failures.append(name)

# Nested half-angle radicals enclose cos(13*pi/16), sin(13*pi/16).
scale=10**12
rt2=I(F(1414213562373,scale),F(1414213562374,scale))
w=I(F(765366864729,scale),F(765366864732,scale))
ca=I(F(831469612301,scale),F(831469612304,scale))
sa=I(F(555570233018,scale),F(555570233022,scale))
check('sqrt2 lower',F(2),rt2.lo**2)
check('sqrt2 upper',rt2.hi**2,F(2))
check('nested radical lower',2-rt2.hi,w.lo**2)
check('nested radical upper',w.hi**2,2-rt2.lo)
check('central cosine lower',2+w.lo,4*ca.lo**2)
check('central cosine upper',4*ca.hi**2,2+w.hi)
check('central sine lower',2-w.hi,4*sa.lo**2)
check('central sine upper',4*sa.hi**2,2-w.lo)
eps=F(1,10**6)
c=I(F(-831471,10**6),F(-831468,10**6))
s=I(F(555569,10**6),F(555572,10**6))
check('sector cosine lower',-ca.hi-eps,c.lo)
check('sector cosine upper',c.hi,-ca.lo+eps)
check('sector sine lower',sa.lo-eps,s.lo)
check('sector sine upper',s.hi,sa.hi+eps)

d,U,h=F(5,4),F(121,64),F(136,125)
N=512
cells=[]
def margins(t,K):
    D1=d*d+2*d*c*t+t*t
    D2=U*U+2*U*d*c*t+d*d*t*t
    A=K*D2-t*t*D1
    D=K*D2-U*D1
    C=K*D2*(h*h+2*h*c*t+t*t)-D1*(U*U+2*U*h*c*t+h*h*t*t)
    B=2*t*s*D
    disc=4*A*C-B*B
    slope=h*A+t*c*D
    return D1.lo,D2.lo,A.lo,disc.lo,slope.lo

def valid(t,K): return min(margins(t,K))>0

previous=F(1)
for j in range(N):
    t=I(F(j,N),F(j+1,N))
    low,high=F(1),F(4)
    if not valid(t,high):
        failures.append(f'cell {j}: K=4 does not certify all margins')
        continue
    for unused in range(14):
        mid=(low+high)/2
        if valid(t,mid): high=mid
        else: low=mid
    K=max(previous,high)
    mm=margins(t,K)
    if min(mm)<=0: failures.append(f'cell {j}: monotone envelope failed')
    previous=K
    # (1/2)log K = atanh z; this positive remainder is an exact upper bound.
    z=(K-1)/(K+1)
    J=16
    log_upper=sum((z**(2*k+1)/F(2*k+1) for k in range(J)),F(0))
    log_upper+=z**(2*J+1)/(F(2*J+1)*(1-z*z))
    # A rational upward rounding keeps the final exact sum compact.
    precision=10**12
    scaled=log_upper*precision
    log_upper_rounded=F(-(-scaled.numerator//scaled.denominator),precision)
    cells.append(dict(j=j,t=[str(t.lo),str(t.hi)],K=str(K),
                      lower_margins=dict(zip(('D1','D2','A','discriminant','half_plane_slope'),map(str,mm))),
                      half_log_upper=str(log_upper_rounded)))

if len(cells)!=N: failures.append('missing cells')
rate=sum((F(v['half_log_upper']) for v in cells),F(0))/N
check('uniform product exponent',rate,F(31,100),'<')
check('rho logarithm lower margin',F(3,10)-F(3,10)**3/6,F(29,100))
tail_rate=F(4,3)*(F(3,10)-F(3,10)**3/6)-F(31,100)
check('higher-alias exponent versus required',tail_rate,F(1,32))
check('m=5 geometric denominator exponent',10*(F(3,10)-F(3,10)**3/6),F(1))

summary=dict(cells=N,product_exponent_upper=str(rate),product_exponent_required='31/100',
             maximum_K=str(max(F(v['K']) for v in cells)),
             minimum_margins={key:str(min(F(v['lower_margins'][key]) for v in cells))
                              for key in ('D1','D2','A','discriminant','half_plane_slope')},
             higher_alias_decay=str(tail_rate),required_decay='1/32',
             full_tail_bound='4*exp(-21*n/250)',passed=not failures)
out=Path(__file__).with_suffix('.json')
out.write_text(json.dumps(dict(status='EXACT_RATIONAL_CERTIFICATE',summary=summary,
                              checks=checks,failures=failures,cells=cells),indent=2)+'\n')
print('Exact rational certificate:', 'PASS' if not failures else 'FAIL')
print('Product exponent:',rate,'=',float(rate),'required < 31/100')
print('Full higher-alias tail <= 4 exp(-gamma*n); gamma:',tail_rate,'required > 1/32')
print('Complete rational cells:',len(cells),'failures:',failures)
print('Certificate:',out)
if failures: raise SystemExit(1)
