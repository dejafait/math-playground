#!/usr/bin/env python3
"""Separate finite replay, Fraction endpoints, square histograms and matrix products.
Does not import producer code or trust certificate summary/decimal values.
"""
import json
from fractions import Fraction as Q
from math import factorial,gcd,isqrt
from hashlib import sha256
from pathlib import Path
HERE=Path(__file__).resolve().parent


def replay(data):
    assert data['schema']=='nonunitary-36-v1' and data['bits']==96
    den=2**96; assert data['scale']==den
    checks=[]; metrics={}
    def decode(v):
        assert len(v)==2 and all(type(x)is int for x in v) and v[0]<=v[1]
        return [Q(x,den) for x in v]
    def enclosing(vals):
        return [(min(vals)*den).__floor__(),-((-max(vals)*den).__floor__())]
    def op(v,w,fn): return enclosing([fn(x,y) for x in decode(v) for y in decode(w)])
    def plus(v,w): return op(v,w,lambda x,y:x+y)
    def minus(v,w): return op(v,w,lambda x,y:x-y)
    def times(v,w): return op(v,w,lambda x,y:x*y)
    def scalar(v,s): return enclosing([x*s for x in decode(v)])
    def divide(v,w):
        assert w[0]>0
        return op(v,w,lambda x,y:x/y)
    def root(v):
        assert v[0]>=0
        l,h=isqrt(v[0]*den),isqrt(v[1]*den)
        if h*h<v[1]*den: h+=1
        assert l*l<=v[0]*den<(l+1)**2
        assert (h-1)**2<v[1]*den<=h*h or h==0
        return [l,h]
    def exact(x): return enclosing([Q(x)])
    def complex_product(v,w):
        # Independent endpoint arithmetic, real/imag bilinear expressions.
        re=minus(times(v[0],w[0]),times(v[1],w[1]))
        im=plus(times(v[0],w[1]),times(v[1],w[0]))
        return [re,im]
    def complex_add(v,w): return [plus(v[0],w[0]),plus(v[1],w[1])]
    def complex_scalar(v,s): return [scalar(t,s) for t in v]

    ar=data['arithmetic']; assert ar['model']==[0,0,0,0,1]
    a1,a2,a3,a4,a6=ar['model']
    b2=a1*a1+4*a2; b4=2*a4+a1*a3; b6=4*a6+a3*a3
    b8=(b2*b6-b4*b4)//4
    c4=b2*b2-24*b4; c6=36*b2*b4-b2**3-216*b6
    delta=(c4**3-c6**2)//1728
    assert ar['invariants']==[b2,b4,b6,b8,c4,c6,delta]==[0,0,4,0,0,-864,-432]
    def valuation(p,v):
        k=0
        while v%p==0: v//=p; k+=1
        return k
    assert delta==-2**4*3**3
    # Discriminant scaling lowers local valuation by a positive multiple of 12.
    assert all(0<=valuation(p,abs(delta))<12 for p in (2,3))
    assert len(ar['tate'])==2
    for row in ar['tate']:
        p=row['p']; r,s,t=row['r'],row['s'],row['t']
        if p==2:
            assert b2%2==0 and r==a4%2 and t==(r*(1+a2+a4)+a6)%2 and s==0
        else:
            assert p==3 and b2%3==0 and r==-1 and (r+b6)%3==0
            assert t==(a1*r+a3)%3 and s==0
        # Substitution x=X+r, y=Y+t independently expands this specific model.
        transformed=[0,3*r,2*t,3*r*r,r**3+1-t*t]
        assert transformed==row['transformed']
        assert all(transformed[i]%p==0 for i in (2,3,4))
        _,aa2,aa3,aa4,aa6=transformed
        bb2=4*aa2; bb4=2*aa4; bb6=aa3*aa3+4*aa6
        bb8=4*aa2*aa6+aa2*aa3*aa3-aa4*aa4
        cc4=bb2**2-24*bb4; cc6=-bb2**3+36*bb2*bb4-216*bb6
        assert row['invariants']==[bb2,bb4,bb6,bb8,cc4,cc6,delta]
        n=valuation(p,abs(delta)); assert row['v_delta']==n and cc4%p==0
        assert aa6%(p*p)==0 # no II exit
        if p==3:
            assert bb8%(p**3)!=0 and row['exit']=='III' and row['f']==n-1==2 and row['c']==2
        else:
            assert bb8%(p**3)==0 and bb6%(p**3)!=0
            assert row['exit']=='IV' and row['f']==n-2==2
            roots=[x for x in range(p) if (x*x+(aa3//p)*x-aa6//(p*p))%p==0]
            assert row['quadratic_roots']==roots==[0,1] and row['c']==3
    assert ar['N']==2**2*3**2==36 and ar['components']==1 and delta<0
    assert ar['bad_a_p']=={'2':0,'3':0}
    checks.append('minimal discriminant scaling, both transformed small-prime Tate exits, conductor and additive factors')

    T=data['T']; assert T>=37 and T<20000
    prime_list=[]
    for p in range(2,T+1):
        if all(p%k for k in range(2,isqrt(p)+1)): prime_list.append(p)
    rows=data['point_counts']; assert [r['p'] for r in rows]==[p for p in prime_list if p not in (2,3)]
    aps={2:0,3:0}; xchecks=0
    for row in rows:
        p=row['p']; histogram=[0]*p
        for y in range(p): histogram[y*y%p]+=1
        numbers=[histogram[(x**3+1)%p] for x in range(p)]
        assert row['characters']==[v-1 for v in numbers]
        total=1+sum(numbers)
        assert row['total']==total and row['a_p']==p+1-total
        aps[p]=p+1-total; xchecks+=p
    coeffs=[0,1]; fsall=[]
    for n in range(2,T+1):
        rem=n; factors=[]; d=2
        while d*d<=rem:
            e=0
            while rem%d==0: rem//=d; e+=1
            if e: factors.append((d,e))
            d+=1
        if rem>1: factors.append((rem,1))
        product=1; records=[]
        for p,e in factors:
            sequence=[1,aps[p]]
            for k in range(2,e+1):
                sequence.append(aps[p]*sequence[k-1]-(p if 36%p else 0)*sequence[k-2])
            records.append([p,e,sequence]); product*=sequence[e]
        fsall.append([n,records]); coeffs.append(product)
    assert coeffs==data['coefficients'] and fsall==data['factorizations']
    assert all(abs(coeffs[n])<=n for n in range(1,T+1))
    assert data['ell']==37 and 37%36==1 and gcd(37,6)==1
    assert data['h']==38-aps[37]>0
    checks.append('every good-prime count by independent square histograms, every factorization and newform coefficient')
    metrics.update(T=T,good_primes=len(rows),point_count_x_checks=xchecks)

    pirow=data['pi']; J=pirow['J']; assert J==40
    at=[]
    for inv in (5,239):
        terms=[Q((-1)**k,(2*k+1)*inv**(2*k+1)) for k in range(J+1)]
        lowhigh=sorted([sum(terms[:-1]),sum(terms)])
        at.append(lowhigh)
    assert pirow['atan']==[[str(x) for x in row] for row in at]
    piends=[16*at[0][0]-4*at[1][1],16*at[0][1]-4*at[1][0]]
    assert pirow['exact']==[str(x) for x in piends]
    pi=enclosing(piends); assert pi==pirow['interval'] and 3*den<pi[0]<=pi[1]<4*den
    tan2=2*Q(1,5)/(1-Q(1,25)); tan4=2*tan2/(1-tan2*tan2)
    assert (tan4-Q(1,239))/(1+tan4*Q(1,239))==1
    checks.append('complete Machin alternating brackets and exact algebra')

    def matrix_product(m,n):
        return [[sum(m[i][k]*n[k][j] for k in (0,1)) for j in (0,1)] for i in (0,1)]
    trans=data['transports']; r=Q(data['r']); assert r==Q(1,6)
    vs=[37*r]+[(r+j)/37 for j in range(37)]
    assert len(trans)==38 and [Q(row['v']) for row in trans]==vs
    for row,v in zip(trans,vs):
        p,q=v.numerator,v.denominator
        sr,tr=row['bezout_r']; sv,tv=row['bezout_v']; t=row['t']
        assert sr-6*tr==1 and p*sv-q*tv==1
        m=matrix_product(matrix_product([[p,tv],[q,sv]],[[1,t],[0,1]]),[[sr,-tr],[-6,1]])
        A,B=m[0]; C,D=m[1]
        assert row['matrix']==[A,B,C,D] and A*D-B*C==1 and C%36==0
        assert (A+6*B)*q==(C+6*D)*p and C+6*D!=0
        x,y=map(Q,row['tau']); u,vv=map(Q,row['image']); assert y>0 and vv>0
        denominator=(C*x+D)**2+(C*y)**2
        assert denominator>0
        real=((A*x+B)*(C*x+D)+A*C*y*y)/denominator
        imag=y/denominator
        assert [real,imag]==[u,vv]
    checks.append('all 38 reduced Hecke endpoints, Bezout/congruence witnesses, matrices and both interior points')
    metrics['transports']=38

    primitives=data['primitives']; keys=[]; fullterms=0
    for row in primitives:
        x,y=Q(row['x_reduced']),Q(row['y']); H=row['H']; keys.append((x,y))
        assert -Q(1,2)<=x<Q(1,2) and y>0 and 0<=H<=T
        assert row['L']==12 and row['J']==160 and 8*(abs(x)+y)<=12
        w=[scalar(pi,-2*y),scalar(pi,2*x)]; assert w==row['w']
        rem=Q(3**12*12**161,factorial(161)); assert str(rem)==row['Taylor_remainder']
        radius=-((-rem*den).__floor__()); assert radius==row['Taylor_radius']
        term=[exact(1),exact(0)]; subtotal=term
        # Replays all rectangle propagation; factorial error covers complex Taylor tail.
        for k in range(1,161):
            term=complex_scalar(complex_product(term,w),Q(1,k))
            subtotal=complex_add(subtotal,term)
        qrect=[[v[0]-radius,v[1]+radius] for v in subtotal]
        assert qrect==row['q']
        power=[exact(1),exact(0)]; finite=[exact(0),exact(0)]
        for n in range(1,H+1):
            power=complex_product(power,qrect)
            finite=complex_add(finite,complex_scalar(power,Q(coeffs[n],n)))
        assert finite==row['finite_sum']
        tail=Q(1,2**((6*H*y).__floor__()))/(6*y)
        assert tail<=Q(1,2**38) and str(tail)==row['tail_exact']
        if H>0: assert Q(1,2**((6*(H-1)*y).__floor__()))/(6*y)>Q(1,2**38)
        tailradius=-((-tail*den).__floor__()); assert row['tail_radius']==tailradius
        assert row['enclosure']==[[v[0]-tailradius,v[1]+tailradius] for v in finite]
        fullterms+=H
    assert len(keys)==len(set(keys))
    used=set(); integ=exact(0)
    for row in trans:
        indices=row['primitive_ids']; assert len(indices)==2
        for i,key in zip(indices,('tau','image')):
            assert type(i)is int and 0<=i<len(primitives)
            x,y=map(Q,row[key]); x-= (x+Q(1,2)).__floor__()
            assert keys[i]==(x,y); used.add(i)
        left=primitives[indices[0]]['enclosure'][0]; right=primitives[indices[1]]['enclosure'][0]
        integ=plus(integ,minus(right,left))
    assert used==set(range(len(primitives)))
    assert T==max(37,max(row['H'] for row in primitives))
    integ=scalar(integ,Q(1,data['h']))
    checks.append('every complex Taylor operation and remainder, Fourier term and tail; complete oriented closing sum')
    metrics.update(primitive_points=len(primitives),Fourier_terms=fullterms)

    period=data['period']; assert period['real_root']=='-1' and period['conjugate_real']=='1/2'
    # Exact factorization and Vieta: g=(x+1)(x^2-x+1), one real root.
    rr,u,vsq,d=Q(-1),Q(1,2),Q(3,4),Q(-3,2)
    assert rr**3+1==0 and 2*u+rr==0 and u*u+vsq+2*rr*u==0 and -rr*(u*u+vsq)==1
    assert d==rr-u and vsq>0 and period['v_squared']==exact(vsq) and period['d']==exact(d)
    R=root(plus(times(exact(d),exact(d)),exact(vsq))); assert R==period['R']
    assert R[0]>exact(abs(d))[1] # branch positivity even though d<0
    A=root(R); G=root(scalar(plus(R,exact(d)),Q(1,2)))
    assert period['agm_steps'][0]==[A,G] and G[0]>0
    assert len(period['agm_steps'])==13
    for saved in period['agm_steps'][1:]:
        avg=scalar(plus(A,G),Q(1,2)); geom=root(times(A,G))
        A,G=avg,geom; assert saved==[A,G]
    agm=[G[0],A[1]]; assert agm==period['agm_bracket'] and agm[0]>0
    omega=divide(pi,agm)
    assert period['components']==1 and period['total']==omega
    result=data['result']; normalized=divide(integ,omega)
    assert result['integral']==integ and result['normalized']==normalized
    width=Q(normalized[1]-normalized[0],den); threshold=Q(1,2**20)
    assert result['width']==str(width) and Q(result['required_width'])==threshold
    assert result['passed']==(width<threshold)
    checks.append('exact one-real-root factorization, positive AGM branches, all period iterates, component factor and signed division')
    return {'passed':True,'target_passed':width<threshold,'checks':checks,'metrics':metrics,'width':str(width),
            'required_width':str(threshold),'normalized_interval':[str(x) for x in decode(normalized)],
            'integral_interval':[str(x) for x in decode(integ)],'period_interval':[str(x) for x in decode(omega)]}

if __name__=='__main__':
    import sys,traceback
    path=Path(sys.argv[1]) if len(sys.argv)>1 else HERE/'certificate.json'
    destination=Path(sys.argv[2]) if len(sys.argv)>2 else HERE/'verification.json'
    try:
        report=replay(json.loads(path.read_text())); report['certificate_sha256']=sha256(path.read_bytes()).hexdigest()
    except Exception as exc:
        report={'passed':False,'failure':repr(exc),'traceback':traceback.format_exc()}
    destination.write_text(json.dumps(report,indent=2)+'\n')
    print('replay', 'PASS' if report['passed'] else 'FAIL',
          'target=', 'PASS' if report.get('target_passed') else 'FAIL',
          'width=',report.get('width'),'required <',report.get('required_width'),
          'metrics=',report.get('metrics'),'failure=',report.get('failure'),'report=',destination)
    raise SystemExit(0 if report['passed'] else 1)
