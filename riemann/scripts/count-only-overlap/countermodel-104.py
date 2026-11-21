"""Exact-rational scalar certificate for L897; no zero enumeration needed."""
from fractions import Fraction as F
from decimal import Decimal, localcontext
from pathlib import Path
import json
import sys
sys.set_int_max_str_digits(0)
N = 50
class I:
    def __init__(self, lo, hi=None):
        self.lo = F(lo); self.hi = F(lo if hi is None else hi)
        assert self.lo <= self.hi
    def __add__(self, other):
        o = as_i(other); return I(self.lo+o.lo, self.hi+o.hi)
    __radd__ = __add__
    def __neg__(self): return I(-self.hi, -self.lo)
    def __sub__(self, other): return self + -as_i(other)
    def __rsub__(self, other): return as_i(other) + -self
    def __mul__(self, other):
        o = as_i(other)
        p = [x*y for x in (self.lo,self.hi) for y in (o.lo,o.hi)]
        return I(min(p),max(p))
    __rmul__ = __mul__
    def __truediv__(self, other):
        o = as_i(other); assert o.lo*o.hi>0
        return self*I(1/o.hi,1/o.lo)
    def __rtruediv__(self, other): return as_i(other)/self
    def ln(self):
        assert self.lo>0
        return I(log_bounds(self.lo)[0],log_bounds(self.hi)[1])
def as_i(x): return x if isinstance(x,I) else I(x)
def basic_log(x):
    assert 1<=x<=2
    z=(x-1)/(x+1)
    value=2*sum((z**(2*n+1)/F(2*n+1) for n in range(N)),F(0))
    error=2*z**(2*N+1)/(F(2*N+1)*(1-z*z))
    return I(value,value+error)
LOG2=basic_log(F(2))
def log_bounds(x):
    assert x>0
    shift=0
    while x>=2: x/=2; shift+=1
    while x<1: x*=2; shift-=1
    a=basic_log(x)+shift*LOG2
    return a.lo,a.hi
def atan_bounds(x):
    value=sum(((-1)**n*x**(2*n+1)/F(2*n+1) for n in range(N)),F(0))
    nxt=x**(2*N+1)/F(2*N+1)
    return I(value,value+nxt) if N%2==0 else I(value-nxt,value)
# Machin's identity pi=16 arctan(1/5)-4 arctan(1/239).
pi=16*atan_bounds(F(1,5))-4*atan_bounds(F(1,239))
k=6002; J=k+1; m=9000000000000
K=12363153437138; H=3000175332800
b=F('0.34536'); d=F('8.08344')
gk=F(10000); T=gk+F(1,10**12)
R=2*(gk*gk+T*T)
q=2*gk*gk/(gk*gk+T*T)
a=R/(4*T*T); s=(1+q)/2; eps=1-q

def U(t):
    return I(t)/(2*pi)*((I(t)/(2*pi)).ln()-1)+b*I(t).ln()+d
u0=U(9999); uh=U(H-1); uH=U(H)
# Omit b/t so this lower bound holds for EVERY t>=9999.
derivative_lower=(I(9999)/(2*pi)).ln()/(2*pi)
V=(I(T)/(2*pi)).ln()/(pi*T)+(b*(I(T).ln()+F(1,2))+d-J)/(T*T)
B=((1+s*a)/I(1-a)).ln()+(1+s)*R/(4*(1-a))*V
terms={
    'B':B,
    '2logk':2*I(k).ln(),
    '(2k-2)log(1+q)':(2*k-2)*I(1+q).ln(),
    'klog2':k*LOG2,
    '-2klog(1-q)':-2*k*I(1-q).ln(),
    '(m+k+2)logs':(m+k+2)*I(s).ln(),
}
Hm=sum(terms.values(),I(0))
simple_bounds={'U_9999_lower':F(10152), 'U_Hminus1_minus_K_lower':F(11),
 'derivative_all_t_ge_9999_lower':F(117,100), 'V_lower':F(17,100000),
 'Hm_lower':F(300099,100)}
checks={
    'simple_U_9999':u0.lo>simple_bounds['U_9999_lower'],
    'simple_U_Hminus1':uh.lo-K>simple_bounds['U_Hminus1_minus_K_lower'],
    'simple_derivative':derivative_lower.lo>simple_bounds['derivative_all_t_ge_9999_lower'],
    'simple_V':V.lo>simple_bounds['V_lower'],
    'simple_Hm':Hm.lo>simple_bounds['Hm_lower'],
    'U_9999_exceeds_J':u0.lo>J,
    'U_Hminus1_exceeds_K':uh.lo>K,
    'derivative_above_one':derivative_lower.lo>1,
    'all_scalar_domains':0<q<s<1 and 0<a<1 and T>4 and T<H-1,
    'V_positive':V.lo>0,
    'epsilon_below_1e_minus15':0<eps<F(1,10**15),
    'rank_factor_below_1e13':m+k+2<10**13,
    'log2_above_half':LOG2.lo>F(1,2),
    'complete_Hm_above_3000':Hm.lo>3000,
}
def pack(x):
    x=as_i(x)
    with localcontext() as c:
        c.prec=24
        dec=lambda y: str(Decimal(y.numerator)/Decimal(y.denominator))
        return {'lower':str(x.lo),'upper':str(x.hi),
                'decimal_preview':[dec(x.lo),dec(x.hi)]}
certificate={
 'method':{'arctan_terms':N,'log_terms':N,
 'pi_identity':'16 atan(1/5)-4 atan(1/239)',
 'log_identity':'log x=shift*log2+2 sum z^(2n+1)/(2n+1); 1<=reduced x<2',
 'log_remainder_bound':'2 z^(2N+1)/((2N+1)(1-z^2))'},
 'parameters':dict(k=k,J=J,m=m,K=K,H=H,delta='1/1000000000000'),
 'construction':{'first_packet':'gamma_j=10000-(k-j)/k, 1<=j<=k',
 'selected_omitted':'gamma_J=10000+delta',
 'finite_remainder':'gamma_(J+l)=H-1+l/(K-J), 1<=l<=K-J',
 'infinite_tail':'gamma_(K+n)=H+n, n>=1'},
 'bounds':{'pi':pack(pi),'U_9999':pack(u0),'U_Hminus1_minus_K':pack(uh-K),
 'U_H_minus_K':pack(uH-K),'derivative_9999':pack(derivative_lower),
 'epsilon':pack(eps),'V':pack(V),'B':pack(B),'Hm':pack(Hm),
 'analytic_Hm_lower_threshold':'300099/100'},
 'Hm_terms':{key:pack(value) for key,value in terms.items()},
 'certified_simple_lower_bounds':{key:str(value) for key,value in simple_bounds.items()},
 'checks':checks,'failures':[key for key,passed in checks.items() if not passed],
 'scope':'Exact scalar arithmetic only; L897 proves complete sequence/count/product obligations.'}
path=Path(__file__).with_suffix('.json')
path.write_text(json.dumps(certificate,indent=2)+'\n')
print('Checks:',len(checks),'passed:',sum(checks.values()),'failures:',certificate['failures'])
for name,value,required in [('U(9999)',u0,J),('U(H-1)-K',uh-K,0),
 ('derivative lower for t>=9999',derivative_lower,1),('V(T)',V,0),('exact H_m',Hm,0)]:
    print(name,'>',pack(value)['decimal_preview'][0],'; required >',required)
print('Analytic lower bound: H_m > 300099/100 > 3000; required H_m >= 0.')
print('Certificate:',path)
assert all(checks.values())
