#!/usr/bin/env python3
"""Nonrigorous fixed r=3,m=5 screen; full values saved, not a certificate."""
import json
import math
from pathlib import Path


def simpson(f, a, b, tol=1e-12):
    m = (a+b)/2
    fa, fm, fb = f(a), f(m), f(b)
    whole = (b-a)*(fa+4*fm+fb)/6
    def rec(a,b,fa,fm,fb,whole,tol,depth):
        m = (a+b)/2
        fl, fr = f((a+m)/2), f((m+b)/2)
        left, right = (m-a)*(fa+4*fl+fm)/6, (b-m)*(fm+4*fr+fb)/6
        delta = left+right-whole
        if depth == 0 or abs(delta) <= 15*tol:
            return left+right+delta/15
        return rec(a,m,fa,fl,fm,left,tol/2,depth-1)+rec(m,b,fm,fr,fb,right,tol/2,depth-1)
    return rec(a,b,fa,fm,fb,whole,tol,25)


def row(x,n):
    return [math.exp(-(n*n-1)*x)*simpson(
        lambda q: math.exp(-q)*(x*math.log1p(q/(n*n*x)))**p
        *(1+q/(n*n*x))**.25*(2*(n*n*x+q)-3)/(2*x-3)
        /math.factorial(p), 0, 80) for p in range(5)]


def signed(a):
    a1,a2,a3,a4,a5=a
    return a1*a4*a4+a3**3+a5*a2*a2-a1*a3*a5-2*a2*a3*a4


rows=[]
for x in [math.pi,4,6,10,20,40,80,160]:
    base=row(x,1)
    total=[sum(v) for v in zip(*(row(x,n) for n in range(1,5)))]
    sb,sk=signed(base),signed(total)
    rows.append(dict(x=x,u=.5*math.log(x/math.pi),base=base,total_n_le_4=total,
                     signed_base=sb,signed_total=sk,relative_difference=abs(sk-sb)/abs(sb),
                     rescaled_base=x**3*sb))
out=Path(__file__).with_suffix('.json')
out.write_text(json.dumps(dict(status='NONRIGOROUS_DIAGNOSTIC',
    required='positive base and relative error < 1/2 for every x >= pi',
    failures=['No quadrature, rounding, n>=5, or continuum certificate.'],rows=rows),indent=2)+'\n')
print('NONRIGOROUS diagnostic; required relative bound < 0.5 on entire domain.')
for r in rows:
    print(f"x={r['x']:.8g} base={r['signed_base']:.9g} rel={r['relative_difference']:.9g} x^3*base={r['rescaled_base']:.9g}")
print('Uncertified: quadrature, rounding, omitted n>=5, continuum. Full output:',out)
