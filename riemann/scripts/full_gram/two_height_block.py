#!/usr/bin/env python3
"""Exact finite-displacement contraction; rational interval budget.

No finite Taylor approximation to the actual Hardy function is made.
The analytic hypotheses and infinite tail argument belong to L636.
"""
from fractions import Fraction as F
from itertools import combinations
from math import factorial
from pathlib import Path
import json

OUT = Path(__file__).with_name('two_height_block_certificate.json')
# Polynomials in u,v, truncated only after every operation at u^3,v^1.
def add(a,b):
    c=a.copy()
    for k,v in b.items(): c[k]=c.get(k,F(0))+v
    return {k:v for k,v in c.items() if v}
def scale(a,s): return {k:v*s for k,v in a.items() if v*s}
def mul(a,b):
    c={}
    for (i,j),x in a.items():
        for (k,l),y in b.items():
            if i+k<=3 and j+l<=1:
                key=(i+k,j+l); c[key]=c.get(key,F(0))+x*y
    return {k:v for k,v in c.items() if v}
def power(a,k):
    r={(0,0):F(1)}
    for _ in range(k): r=mul(r,a)
    return r
def mono(a,b,r,s):
    x=mul(power(a,r),power(b,s))
    return add(x,mul(power(a,s),power(b,r))) if r!=s else x
def parity(seq): return (-1)**sum(seq[i]>seq[j] for i in range(4) for j in range(i+1,4))

def weights(nu, same):
    # b=(u,-u,1+v,1-v) or (u,-u,1,-1).
    z=[{(1,0):F(1)},{(1,0):F(-1)},
       {(0,0):F(1),(0,1):F(1)} if same else {(0,0):F(1)},
       {(0,0):F(1),(0,1):F(-1)} if same else {(0,0):F(-1)}]
    delta={(0,0):F(1)}
    for i,j in combinations(range(4),2): delta=mul(delta,add(z[i],scale(z[j],-1)))
    # N/Delta after removing the forced u (and v at the double collision).
    shift=(1,1 if same else 0)
    den={(i-shift[0],j-shift[1]):x for (i,j),x in delta.items()
         if i>=shift[0] and j>=shift[1]}
    assert den.get((0,0))
    # Laurent Fourier coefficients in exp(i), each with i^power, power mod 4.
    num={}
    for I in combinations(range(4),2):
        J=tuple(j for j in range(4) if j not in I); i,j=I; k,l=J
        p=mul(add(z[i],scale(z[j],-1)),add(z[k],scale(z[l],-1)))
        p=mul(p,mono(z[i],z[j],nu[0],nu[1]))
        p=mul(p,mono(z[k],z[l],nu[2],nu[3]))
        p=scale(p,parity(I+J)*(-1)**(nu[2]+nu[3]))
        ell=scale(add(add(z[i],z[j]),scale(add(z[k],z[l]),-1)),F(1,2))
        e=ell.get((0,0),F(0)); assert e.denominator==1
        aa,bb=ell.get((1,0),F(0)),ell.get((0,1),F(0))
        for r in range(4):
            for s in range(2):
                coeff=aa**r*bb**s/F(factorial(r)*factorial(s))
                if not coeff: continue
                term=mul(p,{(r,s):coeff})
                ip=(sum(nu)+r+s)%4
                sign=1 if ip<2 else -1
                key=(int(e),ip%2)
                num[key]=add(num.get(key,{}),scale(term,sign))
    # Cancellation along both collision hyperplanes is checked at every retained order.
    for p in num.values():
        assert all(i>=shift[0] and j>=shift[1] for i,j in p)
    out={}
    for key,p in num.items():
        reduced={(i-shift[0],j-shift[1]):x for (i,j),x in p.items()}
        q={}
        for deg in range(3):
            # v=0 is sufficient after the division by v.
            val=reduced.get((deg,0),F(0))-sum(den.get((h,0),F(0))*q.get(deg-h,F(0)) for h in range(1,deg+1))
            q[deg]=val/den[(0,0)]
        assert all(sum(den.get((h,0),F(0))*q.get(deg-h,F(0)) for h in range(deg+1))
                   == reduced.get((deg,0),F(0)) for deg in range(3))
        out[key]=-q[2]  # Q_b=-1/2 d_u^2, hence minus the u^2 coefficient.
    # Convert exp(+/- i) into real 1,cos(1),sin(1) coefficients.
    real=[F(0)]*3; imag=[F(0)]*3
    for (e,ip),v in out.items():
        assert e in (-1,0,1)
        if e==0: (imag if ip else real)[0]+=v
        elif ip==0:
            real[1]+=v; imag[2]+=e*v
        else:
            imag[1]+=v; real[2]-=e*v
    return real,imag

def plus(a,b): return [x+y for x,y in zip(a,b)]
def minus(a,b): return [x-y for x,y in zip(a,b)]
def ivadd(a,b): return (a[0]+b[0],a[1]+b[1])
def ivscale(a,c): return (a[0]*c,a[1]*c) if c>=0 else (a[1]*c,a[0]*c)
def ivabs(a): return max(abs(a[0]),abs(a[1]))
def trig_interval(sine):
    # Alternating series: twenty terms and its next term enclose sin(1), cos(1).
    s=sum((F((-1)**j,factorial(2*j+(1 if sine else 0))) for j in range(20)),F(0))
    nxt=F(1,factorial(40+(1 if sine else 0)))
    return (s,s+nxt)
COS=trig_interval(False); SIN=trig_interval(True)
def evaluate(v): return ivadd((v[0],v[0]),ivadd(ivscale(COS,v[1]),ivscale(SIN,v[2])))
def strings(x):
    if isinstance(x,F): return str(x)
    if isinstance(x,dict): return {str(k):strings(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)): return [strings(v) for v in x]
    return x

def main():
    diag0,di0=weights((0,0,0,0),True)
    cross0,ci0=weights((0,0,0,0),False)
    assert not any(di0+ci0)
    even=evaluate(plus(diag0,cross0)); odd=evaluate(minus(diag0,cross0))
    assert even[0]>0 and odd[0]>0
    # Rational lower bounds, not floating eigenvalues.
    elo=F(1,100); olo=F(1,3000); geometric=F(1,550)
    assert elo<even[0] and olo<odd[0] and geometric**2<elo*olo
    maxima=[F(0)]*9; rows=[]; lookup={}
    for a in range(9):
        for b in range(a+1):
            for c in range(9-a-b):
                for d in range(min(c,8-a-b-c)+1):
                    nu=(a,b,c,d); k=sum(nu)
                    dr,di=weights(nu,True); cr,ci=weights(nu,False)
                    assert not any(ci)
                    orbit=(1 if a==b else 2)*(1 if c==d else 2)
                    ee=ivabs(evaluate(plus(dr,cr)))/elo/orbit
                    oo=ivabs(evaluate(minus(dr,cr)))/olo/orbit
                    mixed=ivabs(evaluate(di))/geometric/orbit
                    bound=max(ee,oo)+mixed
                    maxima[k]=max(maxima[k],bound)
                    lookup[nu]=(dr,di,cr)
                    rows.append({'nu':nu,'orbit':orbit,'diagonal_real':dr,'diagonal_imag':di,
                                 'cross_real':cr,'even_bound':ee,'odd_bound':oo,
                                 'mixed_bound':mixed,'bound':bound})
    exchange=all(lookup[nu[2:]+nu[:2]]==(dr,[-x for x in di],cr) for nu,(dr,di,cr) in lookup.items())
    # Rounded-up rational degree costs avoid unnecessarily enormous fractions in the proof.
    rounded=[F((x.numerator*1000+x.denominator-1)//x.denominator,1000) for x in maxima]
    expo=[F(0)]+[F(4,factorial(k))+(2 if k==1 else 0) for k in range(1,25)]
    A=[F(1)]
    for k in range(1,25): A.append(sum(j*expo[j]*A[k-j] for j in range(1,k+1))/k)
    costs=[rounded[k]*A[k]/100**k for k in range(1,9)]
    low=sum(costs,F(0))
    u=F(3,200)
    tail_series=sum((A[k]*u**k for k in range(9,25)),F(0))+19683*u**25
    # Six denominators >= (1/4)^4, exp <=6; Q and observer Cauchy cost 420.
    # Two observer channels give operator norm at most twice max entry, then divide by olo.
    tail_cost=2*F(420*6*256*6)*tail_series/olo
    total=low+tail_cost
    checks={'all_175_orbits':len(rows)==175,'all_495_indices':sum(x['orbit'] for x in rows)==495,
            'direct_kernel_diagonal':diag0==[F(13,6),F(-4),F(0)],
            'direct_kernel_cross':cross0==[F(-4),F(3),F(17,6)],
            'pair_exchange':exchange,'positive_even_reference':elo<even[0],
            'positive_odd_reference':olo<odd[0],'cross_normalization':geometric**2<elo*olo,
            'rounded_bounds_dominate':all(r>=x for r,x in zip(rounded,maxima)),
            'below_one':total<1,'below_seven_sixteenths':total<F(7,16)}
    data={'description':'Exact +/-1 displacement leading functional and full-Gram sufficient budget',
          'qualification':'Analytic row extension, normal-family tail and actual-Xi transfer are proved in L636; this certificate only proves the finite rational algebra and bounds.',
          'trig':{'cos':COS,'sin':SIN},'reference':{'diagonal':diag0,'cross':cross0,'even_interval':even,'odd_interval':odd,'even_lower':elo,'odd_lower':olo,'geometric_lower':geometric},
          'rows':rows,'rounded_degree_bounds':rounded,'majorant':A,
          'budget':{'low_degree_costs':costs,'low_total':low,'tail_series':tail_series,'tail_cost':tail_cost,'total':total,'required':F(1)},
          'checks':checks,'failures':[k for k,v in checks.items() if not v]}
    OUT.write_text(json.dumps(strings(data),indent=2)+'\n')
    print('Reference lower bounds (units 6/pi^2): even > 1/100, odd > 1/3000')
    print('Degree bounds:',list(map(str,rounded)))
    print('Sufficient limsup costs: low = %.12g, tail = %.12g, total = %.12g; required < 1'%(float(low),float(tail_cost),float(total)))
    print('Failures:',data['failures'])
    print('Certificate:',OUT.relative_to(OUT.parents[2]))
    if data['failures']: raise SystemExit(1)

if __name__=='__main__': main()
