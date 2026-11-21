#!/usr/bin/env python3
"""Exact rational arithmetic for the analytic tail argument in L767.

The derivative majorants and change of variables require the written proof.
This checks their polynomial arithmetic and the resulting interval bounds.
"""
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import json


def pmul(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,ai in enumerate(a):
        for j,bj in enumerate(b):
            c[i+j]+=ai*bj
    return c


def padd(a,b):
    c=[F(0)]*max(len(a),len(b))
    for i,v in enumerate(a): c[i]+=v
    for i,v in enumerate(b): c[i]+=v
    return c


class I:
    def __init__(self,a,b=None):
        self.lo,self.hi=F(a),F(a if b is None else b)
        assert self.lo<=self.hi
    def __add__(self,b):
        if not isinstance(b,I): b=I(b)
        return I(self.lo+b.lo,self.hi+b.hi)
    __radd__=__add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self,b): return self+-b
    def __mul__(self,b):
        if not isinstance(b,I): b=I(b)
        v=[self.lo*b.lo,self.lo*b.hi,self.hi*b.lo,self.hi*b.hi]
        return I(min(v),max(v))
    __rmul__=__mul__
    def __pow__(self,n):
        assert n>=0
        out=I(1)
        for _ in range(n): out=out*self
        return out
    def encode(self): return {'lower':str(self.lo),'upper':str(self.hi)}


def diff(vals,k):
    return sum(F((-1)**(k-j)*comb(k,j))*vals[j] for j in range(k+1))


# Coefficients of z^k majorize |(d/d epsilon)^k factor|/k!, k<=3.
A=[[F(1),F(1,16)], [F(0),F(1,4)],
   [F(0),F(0),F(3,32)], [F(0),F(0),F(0),F(7,128)]]
B=[[F(1),F(2,5)], [F(0),F(64,25)],
   [F(0),F(768,125)], [F(0),F(9216,625)]]
remainders=[]
majorants=[]
for p in range(5):
    T=[]
    for k in range(4):
        coeff=F(comb(p+k-1,k)) if p else F(k==0)
        T.append([F(0)]*(p+k)+[coeff])
    poly=[F(0)]
    for i in range(4):
        for j in range(4-i):
            k=3-i-j
            poly=padd(poly,pmul(pmul(A[i],B[j]),T[k]))
    majorants.append([str(v) for v in poly])
    remainders.append(sum(v*factorial(k) for k,v in enumerate(poly))/factorial(p))

a=[(p+1)*(F(5,4)-F(p,2)) for p in range(5)]
b=[F((p+1)*(p+2)*(12*p*p-40*p+15),96)+F(3*(p+1),2) for p in range(5)]
ad=[diff(a,k) for k in range(5)]
bd=[diff(b,k) for k in range(5)]
rd=[sum(comb(k,j)*remainders[j] for j in range(k+1)) for k in range(5)]
assert ad[2:]==[F(-1),F(0),F(0)] and bd[4]==3


def enclose(X):
    e=I(0,F(1,X))
    v0=I(1)+a[0]*e+b[0]*e**2+I(-rd[0],rd[0])*e**3
    v1=I(ad[1])+bd[1]*e+I(-rd[1],rd[1])*e**2
    v2=I(-1)+bd[2]*e+I(-rd[2],rd[2])*e**2
    v3=I(bd[3])+I(-rd[3],rd[3])*e
    v4=I(3)+I(-rd[4],rd[4])*e
    signed=-v0*v2*v4+e*v0*v3**2+e*v1**2*v4-2*e*v1*v2*v3+v2**3
    return signed,[v0,v1,v2,v3,v4]


screen=[]
for power in range(4,25):
    X=2**power
    signed,vs=enclose(X)
    screen.append({'X':X,'normalized_signed_lower':str(signed.lo),
                   'passes_lower_1':signed.lo>1})
    if signed.lo>1: break
else: raise AssertionError('No certified tail cutoff in bounded search')

constant=18*67**2*330
assert constant==26664660
coarse=[I(F(999,1000),F(1001,1000)),I(F(249,1000),F(251,1000)),
        I(F(-1001,1000),F(-999,1000)),I(4,F(9,2)),I(F(11,5),F(19,5))]
assert all(c.lo<=v.lo<=v.hi<=c.hi for c,v in zip(coarse,vs))
# All epsilon-weighted terms in the signed expression are nonnegative.
coarse_lower=F(999,1000)**2*F(11,5)-F(1001,1000)**3
assert coarse_lower>F(119,100)>1
# exp(3x)>=(3x)^10/10!, and x>=X: avoids giant exp certificates.
relative_upper=F(constant*factorial(10),3**10*X**7)
assert relative_upper<F(3,10**27)<F(1,2)
result={
    'status':'EXACT_RATIONAL_TAIL_CERTIFICATE',
    'domain':{'x_min':X,'x_definition':'pi*exp(2u)','epsilon_range':[0,str(F(1,X))]},
    'required':{'base_normalized_lower':'1/x^3','relative_error_upper':'1/2'},
    'entry_expansions':{'a':[str(v) for v in a],'b':[str(v) for v in b],
        'third_derivative_divided_by_6_majorant_polynomials':majorants,
        'integrated_remainders':[str(v) for v in remainders]},
    'finite_differences':{'a':[str(v) for v in ad],'b':[str(v) for v in bd],
        'remainder_bounds':[str(v) for v in rd]},
    'scaled_matrix_enclosures':[v.encode() for v in vs],
    'coarse_proof_enclosures':[v.encode() for v in coarse],
    'coarse_signed_lower':str(coarse_lower),
    'signed_determinant_times_x_cubed':signed.encode(),
    'tail':{'entry_error_upper':'330*exp(-3x)',
        'determinant_error_constant':constant,'relative_upper':str(relative_upper),
        'relative_upper_decimal_diagnostic':float(relative_upper)},
    'cutoff_search':screen,
    'checks':{'base_strictly_above_required':signed.lo>1,
        'coarse_enclosures_hold':True,'coarse_lower_above_119_over_100':coarse_lower>F(119,100),
        'relative_strictly_below_half':relative_upper<F(1,2)},
    'unresolved':['0 <= u < log(X/pi)/2; including u=0',
        'independent audit of analytic derivative bounds and certificate',
        'higher orders, effective all-order smoothing, exceptional coefficient transfer, RH']}
out=Path(__file__).with_suffix('.json')
out.write_text(json.dumps(result,indent=2)+'\n')
print(f'Exact tail cutoff x >= {X}; signed determinant*x^3 > {float(signed.lo):.9g}, required > 1.')
print(f'Relative error <= {float(relative_upper):.9g}, required < 0.5.')
print('Earlier dyadic cutoffs failed this enclosure; not counterexamples. See cutoff_search.')
print('NOT covered: pi <= x < cutoff, including u=0. Certificate:',out)
