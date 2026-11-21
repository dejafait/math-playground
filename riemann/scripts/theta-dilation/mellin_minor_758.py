"""One complete actual-theta Mellin minor, with outward fixed-point intervals.
All transcendental calls use correctly rounded Decimal.exp; no binary floats.
Analytic range/series/tail bounds are proved in C233d.
"""
from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import math
import platform

BASE = Path(__file__).resolve().parent
OUT = BASE / 'mellin-minor-certificate-758.json'
S = 10**40
N = 262144
X = 2

class I:
    def __init__(self, lo, hi=None, raw=False):
        if raw:
            self.lo, self.hi = lo, hi
        else:
            a, b = F(lo), F(lo if hi is None else hi)
            self.lo = (a.numerator*S)//a.denominator
            self.hi = -((-b.numerator*S)//b.denominator)
        assert self.lo <= self.hi
    def __add__(self, b):
        b = cv(b)
        return I(self.lo+b.lo, self.hi+b.hi, raw=True)
    __radd__ = __add__
    def __neg__(self):
        return I(-self.hi, -self.lo, raw=True)
    def __sub__(self, b):
        return self + -cv(b)
    def __mul__(self, b):
        b=cv(b)
        p=[self.lo*b.lo,self.lo*b.hi,self.hi*b.lo,self.hi*b.hi]
        return I(min(p)//S,-((-max(p))//S),raw=True)
    __rmul__=__mul__
    def __truediv__(self,b):
        b=cv(b)
        assert b.lo > 0
        return self*I(S*S//b.hi,-((-S*S)//b.lo),raw=True)
    def pair(self):
        return [fmt(self.lo),fmt(self.hi)]

def cv(a):
    return a if isinstance(a,I) else I(a)

def fmt(a):
    sg='-' if a<0 else ''
    q,r=divmod(abs(a),S)
    return f'{sg}{q}.{r:040d}'

def exp(a):
    a=cv(a)
    with localcontext() as c:
        c.prec=60
        lo=(Decimal(a.lo)/Decimal(S)).exp().next_minus()
        hi=(Decimal(a.hi)/Decimal(S)).exp().next_plus()
        l=int((lo*Decimal(S)).to_integral_value(rounding=ROUND_FLOOR))
        h=int((hi*Decimal(S)).to_integral_value(rounding=ROUND_CEILING))
    return I(l,h,raw=True)

def atan_inverse(q, terms):
    v=sum((F((-1)**j,(2*j+1)*q**(2*j+1)) for j in range(terms)),F(0))
    nxt=F((-1)**terms,(2*terms+1)*q**(2*terms+1))
    return min(v,v+nxt),max(v,v+nxt)

def pi_interval():
    a,b=atan_inverse(5,64)
    c,d=atan_inverse(239,20)
    return I(16*a-4*d,16*b-4*c)

def tail_poly(j):
    return sum(F(math.comb(j,l)*2**(j-l)*math.factorial(l)) for l in range(j+1))

def main():
    report={'step':758,'status':'INCOMPLETE','failures':[],
            'scope':'Exactly q1*q3-q2^2; no higher minor or representation claim',
            'arithmetic':'Integer outward fixed-point at 10^-40; correctly rounded Decimal.exp at precision 60, expanded by one ulp',
            'python':platform.python_version(),'N':N,'X':X,'theta_terms':4,
            'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    try:
        pi=pi_interval()
        checks={
            '3<pi<22/7':pi.lo>3*S and pi.hi<I(F(22,7)).lo,
            'exp(3)>216/11':exp(3).lo>I(F(216,11)).hi,
            'exp(4)>50':exp(4).lo>50*S,
            'geometric global prefactor below 90':(I(88)/(I(1)-exp(F(-9,2)))).hi<90*S,
            '75^3<exp(75/4)':I(75**3).hi<exp(F(75,4)).lo,
            'omitted n>=5 bound below 1e-22':(8*exp(F(-225,4))/(I(1)-exp(F(-99,4)))).hi<I('1e-22').lo,
            '90*exp(-75)<1e-29':(90*exp(-75)).hi<I('1e-29').lo,
        }
        report['analytic_checks']=checks
        assert all(checks.values()),'analytic bound check failed'
        eps=I(0,'1e-22')
        h=F(X,N)
        P={j:I(0) for j in (0,2,4)}
        norm={j:I(0) for j in (0,2)}
        F0,F2,BH2,BA2=I(0),I(0),I(0),I(0)
        cells=[]
        left2,left_half=exp(0),exp(0)
        for i in range(N):
            l,r=i*h,(i+1)*h
            right2,right_half=exp(2*r),exp(r/2)
            e2=I(left2.lo,right2.hi,raw=True)
            ehalf=I(left_half.lo,right_half.hi,raw=True)
            K=I(0)
            for n in range(1,5):
                v=pi*(n*n)*e2
                K=K+4*ehalf*v*(2*v-3)*exp(-v)
            K=K+eps
            assert K.lo>=0
            J={j:K*F(r**(j+1)-l**(j+1),j+1) for j in (0,1,2,3,4)}
            K2=K*K
            BH2=BH2+J[1]*F0+K2*(l*h*h/2+h**3/3)
            BA2=BA2+(J[3]*F0-J[1]*F2+K2*(l*l*h**3/3+5*l*h**4/12+2*h**5/15))/4
            F0,F2=F0+J[0],F2+J[2]
            for j in P:
                P[j]=P[j]+J[j]
            for j in norm:
                norm[j]=norm[j]+K2*F(r**(j+1)-l**(j+1),j+1)
            cells.append({'l':str(l),'r':str(r),'K':K.pair()})
            left2,left_half=right2,right_half
        for j in P:
            P[j]=P[j]+I(0,F('1e-29')*tail_poly(j))
        for j in norm:
            norm[j]=norm[j]+I(0,F('1e-58')*tail_poly(j))
        assert P[0].hi<181*S
        BH2=BH2+I(0,181*F('1e-29')*tail_poly(1))
        BA2=BA2+I(0,F(181,4)*F('1e-29')*tail_poly(3))
        M={j:2*P[j] for j in P}
        H0,A0=2*norm[0],2*norm[2]
        BH=[M[0]*M[0]/4,BH2,M[0]*M[2]/8]
        BA=[M[0]*M[2]/8,BA2,(M[0]*M[4]-M[2]*M[2])/32]
        assert all(x.lo>0 for x in [H0,A0]+BH+BA)
        q=[a/b*H0/A0 for a,b in zip(BA,BH)]
        D=q[0]*q[2]-q[1]*q[1]
        report.update(status='PASS' if D.lo>=0 else ('STOP' if D.hi<0 else 'UNRESOLVED'),
                      pi=pi.pair(),positive_half_moments={str(j):v.pair() for j,v in P.items()},
                      H0=H0.pair(),A0=A0.pair(),BH=[v.pair() for v in BH],BA=[v.pair() for v in BA],
                      q=[v.pair() for v in q],D=D.pair(),threshold='0',
                      spatial_tail_K_bound='1e-29 exp(-(x-2)), x>=2',
                      omitted_theta_uniform_bound='1e-22, x>=0',cells=cells)
    except Exception as e:
        report['failures'].append(repr(e))
        raise
    finally:
        OUT.write_text(json.dumps(report,indent=2)+'\n')
        print('status:',report['status'],'failures:',report['failures'])
        if 'D' in report:
            print('q intervals:',report['q'])
            print('D interval:',report['D'],'required threshold: 0')
        print('Full certificate:',OUT.relative_to(BASE.parent.parent))

if __name__=='__main__':
    main()
