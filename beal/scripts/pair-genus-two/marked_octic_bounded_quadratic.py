#!/usr/bin/env python3
"""Exact approved 289-value test. Full proof and bounds: L125."""
from fractions import Fraction as Q
from hashlib import sha256
from math import isqrt
from pathlib import Path
import json
import marked_octic_two_adic_image as dy

BASE=Path(__file__).parent
OUT=BASE/'marked-octic-bounded-quadratic-certificate.json'
SOURCE=BASE/'marked-octic-two-adic-image-certificate.json'
F=[243,0,-3564,0,6930,0,-2860,0,275]
S=(2,3,5,11)

def vp(x,p):
    x=Q(x)
    if not x:return None
    n,d=abs(x.numerator),x.denominator
    z=0
    while n%p==0:n//=p;z+=1
    while d%p==0:d//=p;z-=1
    return z

def ev(c,x):
    y=Q(0)
    for z in reversed(c):y=y*x+z
    return y

def strip(n):
    p,q=abs(n.numerator),n.denominator
    ex=[]
    for ell in S:
        z=0
        while p%ell==0:p//=ell;z+=1
        while q%ell==0:q//=ell;z-=1
        ex.append(z)
    return dict(exponents=ex,numerator_remainder=p,denominator_remainder=q,eligible=p==q==1)

def qbounds(a,b,lo,hi):
    vals=[lo*lo+a*lo+b,hi*hi+a*hi+b]
    vertex=Q(-a,2)
    if lo<=vertex<=hi:vals.append(vertex*vertex+a*vertex+b)
    return min(vals),max(vals)

def main():
    rows=[]
    for a in range(-8,9):
        for b in range(-8,9):
            r=list(map(Q,F)); quotient=[Q(0)]*7
            for k in range(8,1,-1):
                z=r[k];quotient[k-2]=z
                r[k-1]-=a*z;r[k-2]-=b*z;r[k]=0
            d,c=r[:2]
            n=(d*d-a*c*d+b*c*c)/275**2
            assert n
            nd=strip(n)
            square=n>0 and isqrt(n.numerator)**2==n.numerator and isqrt(n.denominator)**2==n.denominator
            rows.append(dict(a=a,b=b,division_quotient=quotient,remainder=[d,c],norm=n,
                             support=nd,norm_square=square,
                             norm_square_root=Q(isqrt(n.numerator),isqrt(n.denominator)) if square else None))
    eligible=[r for r in rows if r['support']['eligible']]
    tested=[r for r in eligible if r['norm_square']]
    roots=[]
    for lo,hi in [(Q(5,2),Q(3)),(Q(3,2),Q(2)),(Q(3,4),Q(1)),(Q(1,4),Q(1,2)),
                  (Q(-1,2),Q(-1,4)),(Q(-1),Q(-3,4)),(Q(-2),Q(-3,2)),(Q(-3),Q(-5,2))]:
        initial=(lo,hi);trace=[]
        while any(qbounds(r['a'],r['b'],lo,hi)[0]<=0<=qbounds(r['a'],r['b'],lo,hi)[1] for r in tested):
            mid=(lo+hi)/2;z=ev(F,mid);assert z
            trace.append(dict(midpoint=mid,F_value=z))
            if ev(F,lo)*z<0:hi=mid
            else:lo=mid
        assert ev(F,lo)*ev(F,hi)<0
        roots.append(dict(initial=initial,bisections=trace,interval=(lo,hi),endpoint_values=[ev(F,lo),ev(F,hi)]))
    old=json.loads(SOURCE.read_text())
    alpha=tuple(map(Q,old['field']['alpha_approximation']))
    assert old['field']['alpha_error_lower_bound']==20
    cosets={tuple(r['residue']):r['label'] for r in old['residue_ring']['complete_unit_cosets']}
    table=old['residue_ring']['unit_multiplication_table'];scalars=old['scalar_labels']
    def lm(x,y):return 32*((x//32)^(y//32))+table[x%32][y%32]
    def label(x):
        w=dy.val(x);assert w is not None
        residue=dy.residue(dy.mul(x,dy.power(dy.PI,-w)))
        return dict(approximation=x,valuation=w,normalized_residue=residue,label=32*(w%2)+cosets[residue])
    H=[3025,-31460,76230,-39204,2673]
    precision=8;r0=3;hensel=[]
    for depth in range(1,precision):
        mod=5**depth
        choices=[r0+j*mod for j in range(5)]
        passing=[x for x in choices if ev(H,x)%(5*mod)==0];assert len(passing)==1
        r0=passing[0];hensel.append(dict(depth=depth+1,root=r0,residual=ev(H,r0)))
    # s=sqrt(3/r0), theta=omega*s/3; exact r0 is within 5^precision.
    mod=5**precision;rad=3*pow(r0,-1,mod)%mod;s=1;sqrt_trace=[]
    for depth in range(1,precision):
        m=5**depth
        passing=[s+j*m for j in range(5) if ((s+j*m)**2-rad)%(5*m)==0]
        assert len(passing)==1;s=passing[0];sqrt_trace.append(dict(depth=depth+1,root=s))
    point2={tuple(x) for x in old['point_image']};point5={'000000','101000'}
    scalar5=[(0,0,0,0,0,0),(0,1,0,1,0,0),(0,1,0,1,1,0),(0,0,0,0,1,0)]
    evidence=[]
    for row in tested:
        a,b=row['a'],row['b'];real=[];bits=0
        for j,root in enumerate(roots):
            lo,hi=root['interval'];bounds=qbounds(a,b,lo,hi)
            assert bounds[0]>0 or bounds[1]<0
            negative=bounds[1]<0;bits|=int(negative)<<j
            real.append(dict(value_bounds=bounds,negative=negative))
        real_code=bits^(255 if bits&1 else 0)
        comps=[]
        mult_bound=min(4,4*dy.v2(a)) if a else 4
        for sign in (1,-1):
            x=dy.add(dy.add(dy.mul(alpha,alpha),dy.scale(alpha,sign*a)),dy.scalar(b))
            c=label(x);c['absolute_error_lower_bound']=20+mult_bound
            c['relative_error_lower_bound']=20+mult_bound-c['valuation']
            assert c['relative_error_lower_bound']>8
            comps.append(c)
        orbit=sorted((lm(comps[0]['label'],s0),lm(comps[1]['label'],s0)) for s0 in scalars)
        ram=[]
        for e in (4,2):
            terms=([e*vp(a,5)+1] if a else [])+([e*vp(b,5)+2] if b else [])
            lower=min(terms) if terms else None
            assert lower is None or lower>0
            ram.append(dict(e=e,value_valuation=-2,principal_error_lower_bound=lower,
                            principal_error_identically_zero=not terms,square_class_bits=[0,0]))
        # Actual U value is (1/r0+b)+(a*s/3)omega; its error is >=precision.
        x=Q(1,r0)+b;y=Q(a*s,3)
        vals=[v for v in (vp(x,5),vp(y,5)) if v is not None];w=min(vals)
        unit=[x/Q(5)**w,y/Q(5)**w]
        residue=[z.numerator*pow(z.denominator,-1,5)%5 for z in unit]
        nr=(residue[0]**2-3*residue[1]**2)%5;assert nr
        f=int(nr in (2,3));raw=(0,0,0,0,w%2,f)
        assert precision-w>0
        five_orbit=sorted(tuple(x^y for x,y in zip(raw,t)) for t in scalar5)
        canonical=next(t for t in five_orbit if t[3]==t[4]==0)
        code=''.join(map(str,canonical))
        evidence.append(dict(pair=[a,b],norm=row['norm'],norm_square_root=row['norm_square_root'],
            real_signs=''.join('-' if bits>>j&1 else '+' for j in range(8)),real_evidence=real,
            real_code=real_code,passes_real=real_code in (0,252,240,192),
            dyadic_components=comps,dyadic_orbit=orbit,dyadic_quotient=min(orbit),passes_two=min(orbit) in point2,
            five_ramified_components=ram,five_U=dict(approximation=[x,y],valuation=w,
                normalized_residue=residue,residue_norm=nr,square_class_bits=[w%2,f],
                absolute_error_lower_bound=precision,relative_error_lower_bound=precision-w),
            five_raw=raw,five_orbit=five_orbit,five_canonical=code,passes_five=code in point5))
    removed=[r['pair'] for r in evidence if r['passes_real'] and r['passes_two'] and not r['passes_five']]
    counts=dict(total=len(rows),eligible=len(eligible),norm_square=len(tested),
        real_survivors=sum(r['passes_real'] for r in evidence),
        real_two_survivors=sum(r['passes_real'] and r['passes_two'] for r in evidence),removed_at_five=len(removed))
    cert=dict(input=dict(F=F,bounds=[-8,8],support=S,leading_coefficient=3025),
        local_input=dict(path=SOURCE.name,sha256=sha256(SOURCE.read_bytes()).hexdigest()),
        rows=rows,eligible_pairs=[[r['a'],r['b']] for r in eligible],roots=roots,
        five_transport=dict(H=H,precision=precision,r0_approximation=r0,r0_hensel=hensel,
                            sqrt_radicand=rad,s_approximation=s,s_hensel=sqrt_trace),
        tested=evidence,counts=counts,removed=removed,failures=[],
        precision=dict(two_minimum=min(c['relative_error_lower_bound'] for r in evidence for c in r['dyadic_components']),
            two_required_strictly_above=8,five_U_minimum=min(r['five_U']['relative_error_lower_bound'] for r in evidence),
            five_required_strictly_above=0),
        limitations=['Only 289 individual values','No supported-group completeness','No point or integer exclusion','Critical audit pending'])
    OUT.write_text(json.dumps(dy.clean(cert),indent=2)+'\n')
    print(json.dumps(dict(counts=counts,precision=cert['precision'],failures=[],path=str(OUT))))
    print(json.dumps([dict(pair=r['pair'],norm=str(r['norm']),signs=r['real_signs'],dyadic=r['dyadic_quotient'],
                          five=r['five_canonical'],passes=[r['passes_real'],r['passes_two'],r['passes_five']]) for r in evidence]))

if __name__=='__main__':main()
