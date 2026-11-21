#!/usr/bin/env python3
"""Exact integer intervals for the fixed law; analytic justification in C466e.

Only the generic outward interval class is reused from certificate896.
No gamma-model evaluation or estimates are called.
"""
import importlib.util
import json
from fractions import Fraction as R
from functools import cache
from math import comb, factorial
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    'interval896', BASE/'gamma-geometric/contact-certificate-896.py')
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
I, S, BITS = mod.I, mod.S, mod.BITS
N, K = 128, 12
LEFT, PREFIX, END, RIGHT = R(1,4), R(177,32), R(178,32), R(179,32)
OUT = Path(__file__).with_suffix('.json')

def cmul(z,w):
    return z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0]

def cdiv(z,w):
    d=w[0]*w[0]+w[1]*w[1]
    a,b=cmul(z,(w[0],-w[1]))
    return a/d,b/d

def cpow(z,n):
    out=(R(1),R(0))
    for _ in range(n):
        out=cmul(out,z)
    return out

def coefficients(nmax):
    prod=[R(1)]
    whole=[1]
    for n in range(1,nmax+1):
        prod.append(prod[-1]*R(2**n-1,2**n))
        whole.append(whole[-1]*(2**n-1))
    real=[(1,2/prod[-1])]
    for n in range(1,nmax+1):
        r=2**n
        a=R(10*r, (1-r)*((3-r)**2+1)*(-1)**(n-1)*whole[n-1])
        real.append((r,a/prod[nmax-n]))
    z=(R(-1),R(-2))
    for n in range(1,nmax+1):
        z=cdiv(z,(1-R(3,2**n),-R(1,2**n)))
    return real,z

@cache
def expminus(t):
    """Enclose exp(-t), t>=0; alternating Taylor then squaring."""
    t=R(t)
    assert t>=0
    if t>=BITS:
        return I(0,1,True)  # exp(-t)<=2^-BITS since e>2
    shifts=0
    while t>1:
        t/=2
        shifts+=1
    term=total=I(1)
    for j in range(1,101):
        term=term.scale(-t/j)
        total=total+term
    rem=I(t**101/factorial(101))
    total=total+I(-rem.hi,0,True)
    # The exact value is nonnegative. Interval intersections are safe.
    total=I(max(0,total.lo),total.hi,True)
    for _ in range(shifts):
        total=total*total
    return total

@cache
def trigpoint(x):
    """Sine/cosine Taylor polynomials through degree100, Lagrange error."""
    x=R(x)
    term=I(1)
    si,co=I(0),I(1)
    for j in range(1,101):
        term=term.scale(x/j)
        if j%2:
            si=si+term.scale((-1)**((j-1)//2))
        else:
            co=co+term.scale((-1)**(j//2))
    rem=I(abs(x)**101/factorial(101))
    box=I(-rem.hi,rem.hi,True)
    return si+box,co+box

def det3(a,b,c):
    return (a[0]*(b[1]*c[2]-b[2]*c[1])
            -a[1]*(b[0]*c[2]-b[2]*c[0])
            +a[2]*(b[0]*c[1]-b[1]*c[0]))

REAL,Z=coefficients(N)
HEAD,HZ=coefficients(8)
# Uniform bounds for derivatives of f*Exp(2)*...*Exp(256).
M=[sum(abs(a)*r**j for r,a in HEAD)
   +2*(abs(HZ[0])+abs(HZ[1]))*4**j for j in range(1,9)]
# p=p_N*law(Z_N), E Z_N=2^-N. Leibniz gives Q=e^x*p errors.
ERROR=[I(R(3**6,2**N)*sum(comb(j,k)*M[k] for k in range(j+1)))
       for j in range(8)]
TAIL=[]
for j in range(8):
    b=I(0)
    for r,a in REAL[K+1:]:
        b=b+expminus((r-1)*LEFT).scale(abs(a)*(r-1)**j)
    TAIL.append(b)
COEFF=[tuple(I(v) for v in cmul(Z,cpow((R(-2),R(-1)),j))) for j in range(8)]
RCOEFF=[(r,[I(a*(-(r-1))**j) for j in range(8)]) for r,a in REAL[:K+1]]

def jets(left,right):
    center=(left+right)/2
    radius=(right-left)/2
    sn,cs=trigpoint(center)
    rad=I(radius)
    sn=sn+I(-rad.hi,rad.hi,True)
    cs=cs+I(-rad.hi,rad.hi,True)
    ez=I(expminus(2*right).lo,expminus(2*left).hi,True)
    q=[]
    for j in range(8):
        v=2*ez*(cs*COEFF[j][0]+sn*COEFF[j][1])
        for r,aa in RCOEFF:
            ee=I(expminus((r-1)*right).lo,
                 expminus((r-1)*left).hi,True)
            v=v+ee*aa[j]
        err=TAIL[j]+ERROR[j]
        q.append(v+I(-err.hi,err.hi,True))
    return q

def determinants(q):
    def a(i,j):
        return q[i]*q[j+1]-q[i+1]*q[j]
    def b(i,j,k):
        return det3(q[i:i+3],q[j:j+3],q[k:k+3])
    d2=[-a(0,1),-a(0,2),-a(1,2)-a(0,3),-2*a(1,3)-a(0,4)]
    d3=[-b(0,1,2),-b(0,1,3),-b(0,2,3)-b(0,1,4),
        -b(1,2,3)-2*b(0,2,4)-b(0,1,5)]
    return d2,d3

def enclose(left,right):
    c=(left+right)/2
    r=(right-left)/2
    point=jets(c,c)
    whole=jets(left,right)
    d2,d3=determinants(point)
    b2,b3=determinants(whole)
    z=I.box(-r,r)
    z2=I.box(0,r*r)
    z3=I.box(-r**3,r**3)
    p=point[0]+point[1]*z+(point[2]*z2).scale(R(1,2))+(whole[3]*z3).scale(R(1,6))
    def taylor(a,b):
        return a[0]+a[1]*z+(a[2]*z2).scale(R(1,2))+(b[3]*z3).scale(R(1,6))
    dp=d3[1]+d3[2]*z+(b3[3]*z2).scale(R(1,2))
    return p,taylor(d2,b2),taylor(d3,b3),dp

def summary_bound(value):
    # Outward decimal display, never used for acceptance.
    q=R(value,S)
    return str(q.numerator*10**20//q.denominator)+'/10^20'

def main():
    cells=[]
    failed=[]
    def cover(left,right,mode,depth=0):
        p,d2,d3,dp=enclose(left,right)
        okay=p.lo>0 and d2.lo>0
        if mode=='prefix':
            okay=okay and d3.lo>0
        if mode=='contact':
            okay=okay and dp.hi<0
        if okay or depth==24:
            row=dict(left=str(left),right=str(right),mode=mode,
                     Q=p.data(),D2_Q=d2.data(),D3_Q=d3.data(),
                     D3_Q_prime=dp.data(),accepted=okay,depth=depth)
            cells.append(row)
            if len(cells)%1000==0:
                print('Accepted/failed cells',len(cells),'last right',right,flush=True)
            if not okay:
                failed.append(row)
            return
        mid=(left+right)/2
        cover(left,mid,mode,depth+1)
        cover(mid,right,mode,depth+1)
    # Fixed coarse partition avoids a parameter search; refinements only pay enclosures.
    for left,right,mode in ((LEFT,PREFIX,'prefix'),(PREFIX,END,'contact'),
                            (END,RIGHT,'lower')):
        width=right-left
        n=max(1,(width.numerator*32+width.denominator-1)//width.denominator)
        for i in range(n):
            cover(left+width*R(i,n),left+width*R(i+1,n),mode)
        print('Completed',mode,'cells so far',len(cells),'failures',len(failed),flush=True)
    endpoints=[]
    for x in (PREFIX,END):
        p,d2,d3,dp=enclose(x,x)
        endpoints.append(dict(x=str(x),Q=p.data(),D2_Q=d2.data(),
                              D3_Q=d3.data(),D3_Q_prime=dp.data()))
    signs=int(endpoints[0]['D3_Q'][0])>0 and int(endpoints[1]['D3_Q'][1])<0
    prefix_min=min(int(c['D3_Q'][0]) for c in cells if c['mode']=='prefix')
    dpmax=max(int(c['D3_Q_prime'][1]) for c in cells if c['mode']=='contact')
    d2min=min(int(c['D2_Q'][0]) for c in cells)
    report=dict(status='PASS' if not failed and signs else 'FAIL',
        bits=BITS,N=N,K=K,interval=[str(LEFT),str(RIGHT)],
        prefix_end=str(PREFIX),contact_end=str(END),
        head_derivative_bounds=[str(v) for v in M],
        true_law_error=[v.data() for v in ERROR],
        omitted_finite_modes=[v.data() for v in TAIL],
        endpoints=endpoints,cells=cells,failures=failed,
        summary=dict(cell_count=len(cells),failure_count=len(failed),
            endpoint_signs_pass=signs,minimum_prefix_D3_Q=str(prefix_min),
            maximum_contact_D3_Q_prime=str(dpmax),minimum_D2_Q=str(d2min),
            required_prefix_D3_lower='>0',required_contact_D3prime_upper='<0',
            required_D2_lower='>0',
            qualification='Compact certificate; analytic endpoint join is in C466e; separate critical review pending.'))
    OUT.write_text(json.dumps(report,indent=2)+'\n')
    print(report['status'],'cells',len(cells),'failed',len(failed))
    print('Prefix D3 lower >=',summary_bound(prefix_min),'required >0')
    print('D2 lower >=',summary_bound(d2min),'required >0')
    print('Contact D3prime upper <',summary_bound(dpmax+1),'+ 1e-20; required <0')
    print('Full certificate:',OUT)

if __name__=='__main__':
    main()
