#!/usr/bin/env python3
"""Fixed known-method L049 enclosure; every bound uses exact arithmetic."""
import json
from fractions import Fraction as F
from math import factorial, gcd, isqrt
from pathlib import Path
HERE=Path(__file__).resolve().parent

class I:
    def __init__(self,bits): self.D=1<<bits
    def out(self,lo,hi=None):
        if hi is None: hi=lo
        assert lo<=hi
        return [(F(lo)*self.D).__floor__(), -((-F(hi)*self.D).__floor__())]
    def add(self,x,y): return [x[0]+y[0],x[1]+y[1]]
    def neg(self,x): return [-x[1],-x[0]]
    def sub(self,x,y): return self.add(x,self.neg(y))
    def mul(self,x,y):
        t=[a*b for a in x for b in y]
        return [min(t)//self.D,-((-max(t))//self.D)]
    def scale(self,x,c):
        t=sorted(F(v,self.D)*c for v in x)
        return self.out(*t)
    def div(self,x,y):
        assert y[0]>0
        t=[F(a,b) for a in x for b in y]
        return self.out(min(t),max(t))
    def sqrt(self,x):
        assert x[0]>=0
        l,h=isqrt(x[0]*self.D),isqrt(x[1]*self.D)
        return [l,h+(h*h<x[1]*self.D)]
    def cmul(self,x,y):
        return [self.sub(self.mul(x[0],y[0]),self.mul(x[1],y[1])),
                self.add(self.mul(x[0],y[1]),self.mul(x[1],y[0]))]
    def cscale(self,x,t): return [self.scale(v,t) for v in x]
    def cadd(self,x,y): return [self.add(x[k],y[k]) for k in (0,1)]

def primes(n):
    sieve=bytearray(b'\1')*(n+1); sieve[:2]=b'\0\0'
    for p in range(2,isqrt(n)+1):
        if sieve[p]: sieve[p*p:n+1:p]=b'\0'*len(range(p*p,n+1,p))
    return [p for p in range(2,n+1) if sieve[p]]

def invariants(a):
    a1,a2,a3,a4,a6=a
    b2=a1*a1+4*a2; b4=a1*a3+2*a4; b6=a3*a3+4*a6
    b8=a1*a1*a6+4*a2*a6-a1*a3*a4+a2*a3*a3-a4*a4
    return [b2,b4,b6,b8,b2*b2-24*b4,-b2**3+36*b2*b4-216*b6,
            -b2*b2*b8-8*b4**3-27*b6*b6+9*b2*b4*b6]

def transforms():
    # Inspected Tate lines 5--28: p=2 uses r=0,t=1; p=3 uses r=-1,t=0.
    return {'model':[0,0,0,0,1],'invariants':invariants([0,0,0,0,1]),
            'tate':[{'p':2,'r':0,'s':0,'t':1,'transformed':[0,0,2,0,0],
                     'invariants':invariants([0,0,2,0,0]),'v_delta':4,
                     'exit':'IV','f':2,'quadratic_roots':[0,1],'c':3},
                    {'p':3,'r':-1,'s':0,'t':0,'transformed':[0,-3,0,3,0],
                     'invariants':invariants([0,-3,0,3,0]),'v_delta':3,
                     'exit':'III','f':2,'c':2}],
            'N':36,'components':1,'bad_a_p':{'2':0,'3':0}}

def transport(v):
    p,q=v.numerator,v.denominator
    # Both Bezout choices and the middle translation are explicitly retained.
    sv=pow(p,-1,q) if q>1 else 0; tv=(p*sv-1)//q
    sr,tr=1,0
    assert (q*sr-6*sv)%36==0 and 6*q%36==0
    tt=0
    A=p*sr-6*(p*tt+tv); B=-p*tr+(p*tt+tv)
    C=q*sr-6*(q*tt+sv); D=-q*tr+(q*tt+sv)
    # A change sv -> sv+kq is another Bezout choice; choose small |C|.
    choices=[]
    for k in range(-2,3):
        s=sv+k*q; t=tv+k*p
        mat=[p-6*t,t,q-6*s,s]
        choices.append((abs(mat[2]),abs(mat[3]),k,mat,s,t))
    _,_,k,mat,sv,tv=min(choices)
    A,B,C,D=mat
    assert A*D-B*C==1 and C%36==0
    assert F(A+6*B,C+6*D)==v
    if C:
        z=[F(-D,C),F(1,abs(C))]; image=[F(A,C),F(1,abs(C))]
    else:
        z=[F(0),F(1)]; image=[F(B,D),F(1)]
    return {'v':str(v),'bezout_r':[sr,tr],'bezout_v':[sv,tv],'t':tt,
            'matrix':mat,'tau':[str(x) for x in z],
            'image':[str(x) for x in image]}

def truncation(y):
    H=0
    while F(1,2**((6*H*y).__floor__()))/(6*y)>F(1,2**38): H+=1
    return H

def arithmetic(T):
    rows=[]; aps={2:0,3:0}
    for p in primes(T):
        if p in (2,3): continue
        chars=[]
        for x in range(p):
            r=(x*x*x+1)%p; c=pow(r,(p-1)//2,p)
            chars.append(-1 if c==p-1 else c)
        total=p+1+sum(chars); aps[p]=p+1-total
        rows.append({'p':p,'characters':chars,'total':total,'a_p':aps[p]})
    a=[0,1]; facts=[]
    for n in range(2,T+1):
        m=n; val=1; fs=[]
        for p in primes(isqrt(n)+1):
            if m%p: continue
            k=0
            while m%p==0: m//=p; k+=1
            seq=[1,aps[p]]
            for _ in range(2,k+1): seq.append(aps[p]*seq[-1]-(0 if p in (2,3) else p)*seq[-2])
            val*=seq[k]; fs.append([p,k,seq])
        if m>1: val*=aps[m]; fs.append([m,1,[1,aps[m]]])
        a.append(val); facts.append([n,fs])
    assert all(abs(a[n])<=n for n in range(1,T+1))
    return rows,a,facts

def atan(inv,J):
    s=sum((F((-1)**k,(2*k+1)*inv**(2*k+1)) for k in range(J)),F(0))
    t=s+F((-1)**J,(2*J+1)*inv**(2*J+1))
    return sorted([s,t])

def primitive(c,pi,x,y,H,a):
    x=x-(x+F(1,2)).__floor__()
    w=[c.scale(pi,-2*y),c.scale(pi,2*x)]
    L=12; J=160
    assert 8*(abs(x)+y)<=L
    remainder=F(3**L*L**(J+1),factorial(J+1))
    term=[c.out(1),c.out(0)]; partial=term
    for k in range(1,J+1):
        term=c.cscale(c.cmul(term,w),F(1,k)); partial=c.cadd(partial,term)
    radius=(-(-remainder*c.D).__floor__())
    q=[[v[0]-radius,v[1]+radius] for v in partial]
    power=[c.out(1),c.out(0)]; summ=[c.out(0),c.out(0)]
    for n in range(1,H+1):
        power=c.cmul(power,q); summ=c.cadd(summ,c.cscale(power,F(a[n],n)))
    tail=F(1,2**((6*H*y).__floor__()))/(6*y)
    t=(-(-tail*c.D).__floor__())
    enclosed=[[v[0]-t,v[1]+t] for v in summ]
    return {'x_reduced':str(x),'y':str(y),'H':H,'w':w,'L':L,'J':J,
            'Taylor_remainder':str(remainder),'Taylor_radius':radius,'q':q,
            'finite_sum':summ,'tail_exact':str(tail),'tail_radius':t,'enclosure':enclosed}

def build():
    bits=96; c=I(bits); J=40
    at=[atan(5,J),atan(239,J)]
    piex=[16*at[0][0]-4*at[1][1],16*at[0][1]-4*at[1][0]]
    pi=c.out(*piex); assert 3*c.D<pi[0]<=pi[1]<4*c.D
    ell=37; r=F(1,6)
    vs=[ell*r]+[(r+j)/ell for j in range(ell)]
    transports=[transport(v) for v in vs]
    points={}
    for row in transports:
        for key in ('tau','image'):
            x,y=map(F,row[key]); xr=x-(x+F(1,2)).__floor__()
            points[(xr,y)]=truncation(y)
    T=max(max(points.values()),ell)
    counts,a,facts=arithmetic(T)
    h=next(row['total'] for row in counts if row['p']==ell)
    values=[]; index={}
    for (x,y),H in sorted(points.items()):
        index[(x,y)]=len(values); values.append(primitive(c,pi,x,y,H,a))
    integ=c.out(0)
    for row in transports:
        ids=[]
        for key in ('tau','image'):
            x,y=map(F,row[key]); x=x-(x+F(1,2)).__floor__(); ids.append(index[(x,y)])
        row['primitive_ids']=ids
        # {r,infinity}: sum(P(image)-P(tau))/h.
        integ=c.add(integ,c.sub(values[ids[1]]['enclosure'][0],values[ids[0]]['enclosure'][0]))
    integ=c.scale(integ,F(1,h))
    # x^3+1=(x+1)(x^2-x+1): r=-1,u=1/2,v^2=3/4,d=-3/2.
    d=c.out(F(-3,2)); vsq=c.out(F(3,4))
    R=c.sqrt(c.add(c.mul(d,d),vsq)); A=c.sqrt(R)
    G=c.sqrt(c.scale(c.add(R,d),F(1,2))); steps=[[A,G]]
    for _ in range(12):
        A,G=c.scale(c.add(A,G),F(1,2)),c.sqrt(c.mul(A,G)); steps.append([A,G])
    agm=[G[0],A[1]]; assert agm[0]>0
    period=c.div(pi,agm)
    normalized=c.div(integ,period); width=F(normalized[1]-normalized[0],c.D)
    return {'schema':'nonunitary-36-v1','bits':bits,'scale':c.D,'arithmetic':transforms(),
            'pi':{'J':J,'atan':[[str(x) for x in v] for v in at],
                  'exact':[str(x) for x in piex],'interval':pi},
            'ell':ell,'r':str(r),'h':h,'T':T,'point_counts':counts,'coefficients':a,
            'factorizations':facts,'transports':transports,'primitives':values,
            'period':{'real_root':'-1','conjugate_real':'1/2','v_squared':vsq,'d':d,'R':R,
                      'agm_steps':steps,'agm_bracket':agm,'total':period,'components':1},
            'result':{'integral':integ,'normalized':normalized,'width':str(width),
                      'required_width':'1/1048576','passed':width<F(1,2**20)}}

if __name__=='__main__':
    data=build(); path=HERE/'certificate.json'; path.write_text(json.dumps(data,separators=(',',':'))+'\n')
    r=data['result']; print('production', 'PASS' if r['passed'] else 'FAIL',
        'T=',data['T'],'transports=',len(data['transports']),'primitive points=',len(data['primitives']),
        'width=',r['width'],'required <',r['required_width'],'path=',path)
    raise SystemExit(0 if r['passed'] else 1)
