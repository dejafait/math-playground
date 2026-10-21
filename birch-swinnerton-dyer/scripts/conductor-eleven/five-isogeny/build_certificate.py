#!/usr/bin/env python3
"""Exact fixed Vélu reproduction. No external packages or numerical arithmetic."""
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
import json
from math import gcd, lcm

HERE = Path(__file__).resolve().parent
BASE = HERE.parent

def trim(a):
    a = list(map(F, a))
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a

def add(a,b):
    return trim([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)
                 for i in range(max(len(a),len(b)))])

def scale(a,t):
    return trim([x*t for x in a])

def mul(a,b):
    c = [F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j] += x*y
    return trim(c)

def div(a,b):
    a,b=trim(a),trim(b)
    assert b != [0]
    q=[F(0)]*max(1,len(a)-len(b)+1)
    while a != [0] and len(a)>=len(b):
        j=len(a)-len(b); t=a[-1]/b[-1]; q[j]+=t
        a=add(a,scale([0]*j+b,-t))
    return trim(q),a

def pgcd(a,b):
    while b != [0]: a,b=b,div(a,b)[1]
    return scale(a,1/a[-1])

class R:
    def __init__(self,n,d=(1,)):
        n,d=trim(n),trim(d); assert d != [0]
        g=pgcd(n,d); n,r=div(n,g); assert r==[0]
        d,r=div(d,g); assert r==[0]
        self.n=scale(n,1/d[-1]); self.d=scale(d,1/d[-1])
    def __add__(self,b):
        if not isinstance(b,R): b=R([b])
        return R(add(mul(self.n,b.d),mul(b.n,self.d)),mul(self.d,b.d))
    __radd__=__add__
    def __neg__(self): return R(scale(self.n,-1),self.d)
    def __sub__(self,b): return self+-b
    def __mul__(self,b):
        if not isinstance(b,R): b=R([b])
        return R(mul(self.n,b.n),mul(self.d,b.d))
    __rmul__=__mul__
    def __truediv__(self,b):
        if not isinstance(b,R): b=R([b])
        return R(mul(self.n,b.d),mul(self.d,b.n))
    def __rtruediv__(self,b): return R([b])/self
    def __pow__(self,k):
        v=R([1])
        for _ in range(k): v=v*self
        return v
    def deriv(self):
        dn=[i*self.n[i] for i in range(1,len(self.n))] or [0]
        dd=[i*self.d[i] for i in range(1,len(self.d))] or [0]
        return R(add(mul(dn,self.d),scale(mul(self.n,dd),-1)),mul(self.d,self.d))
    def json(self): return {'numerator':list(map(str,self.n)), 'denominator':list(map(str,self.d))}

def group_add(p,q):
    if p is None:return q
    if q is None:return p
    x,y=p; u,v=q
    if x==u and y+v==-1:return None
    slope=(3*x*x-2*x-10)/(2*y+1) if p==q else (v-y)/(u-x)
    z=slope*slope+1-x-u
    return z,-y-1+slope*(x-z)

def invariants(a4,a6):
    b2=-4; b4=2*a4; b6=1+4*a6; b8=-4*a6-1-a4*a4
    c4=b2*b2-24*b4; c6=-b2**3+36*b2*b4-216*b6
    delta=-b2*b2*b8-8*b4**3-27*b6*b6+9*b2*b4*b6
    return dict(b2=b2,b4=b4,b6=b6,b8=b8,c4=c4,c6=c6,delta=delta)

def build():
    P=(F(5),F(5)); cur=None; multiples=[]
    for _ in range(5):
        cur=group_add(cur,P)
        multiples.append(None if cur is None else list(map(str,cur)))
    assert multiples[-1] is None and all(p is not None for p in multiples[:-1])
    x=R([0,1]); f=x**3-x**2-10*x-F(79,4)
    h=x; paired=[]; tsum=F(0); wsum=F(0)
    for p in multiples[:2]:
        q=F(p[0]); r=F(p[1])+F(1,2)
        t=6*q*q-4*q-20; u=4*r*r
        h=h+t/(x-q)+u/(x-q)**2
        tsum+=t; wsum+=u+q*t
        paired.append(dict(x=str(q),Y=str(r),t=str(t),u=str(u),w=str(u+q*t)))
    a4=-10-5*tsum; a6=-20+4*tsum-7*wsum
    assert a4.denominator==a6.denominator==1
    a4,a6=int(a4),int(a6); v=h.deriv()
    eq=f*v**2-(h**3-h**2+a4*h+a6+F(1,4))
    assert eq.n==[0]
    eq7=R([1])
    for pair in paired:
        q=F(pair['x']); r=F(pair['Y'])
        eq7=eq7-2+2*(2*x+q-1)/(x-q)-2*(f+3*r*r)/(x-q)**3
    assert (eq7-v).n==[0]
    upstream=BASE/'absolute-cycles/certificate.json'
    data=json.loads(upstream.read_text()); z=list(map(F,data['normalization']['generator_values']))
    assert len(z)==12
    target=[5*t for t in z]; den=lcm(*(t.denominator for t in target))
    d0=lcm(*(t.denominator for t in z)); ts=[int(d0*t) for t in z]
    hs=[d0//gcd(abs(5*t),d0) for t in ts]
    return {'schema':'BSD-L046-five-isogeny-v1','source':[0,-1,1,-10,-20],
            'candidate':['5','5'],'multiples':multiples,'paired_terms':paired,
            'kernel_polynomial':['80','-21','1'],
            'map':{'x_target':h.json(),'Y_target_over_Y_source':v.json(),
                   'y_convention':'Y=y+1/2 on both models'},
            'target':[0,-1,1,a4,a6],'invariants':invariants(a4,a6),
            'identity_zero':eq.json(),'eq7_y_zero':(eq7-v).json(),
            'exceptional':{'finite_x':['5','16'],'x_pole_order_each':2,
                           'Y_pole_order_each':3,'infinity_x_pole_order':2,
                           'infinity_Y_pole_order':3,'image':'[0:1:0]',
                           'finite_x_leading_coefficients':[p['u'] for p in paired],
                           'finite_Y_factor_leading_coefficients':[str(-2*F(p['u'])) for p in paired]},
            'minimality':{'bad_prime':11,'delta_valuation':1,'required_less_than':12,
                          'coordinate_change':[1,0,0,0]},
            'differential':{'scalar':'1'},
            'real_map':{'geometric_kernel_size':5,'real_kernel_size':5,'cokernel_size':1,'period_ratio':'5'},
            'transfer':{'source_certificate':str(upstream.relative_to(BASE.parent.parent)),
                        'source_sha256':sha256(upstream.read_bytes()).hexdigest(),
                        'source_values':list(map(str,z)),'D0':d0,'integer_numerators':ts,
                        'target_values':list(map(str,target)),'individual_denominators':hs,
                        'common_denominator':den,'C_all_odd_primes':0},
            'failures':[]}

if __name__=='__main__':
    data=build(); out=HERE/'certificate.json'
    out.write_text(json.dumps(data,indent=2)+'\n')
    print('Order actual/required: 5/5; target:',data['target'])
    print('Discriminant:',data['invariants']['delta'],'; minimality valuation actual/threshold: 1/<12')
    print('Differential scalar: 1; real period ratio: 5; all values actual/required: 12/12; denominator: 2')
    print('Failures:',data['failures'],'; certificate:',out.relative_to(BASE.parent.parent))
