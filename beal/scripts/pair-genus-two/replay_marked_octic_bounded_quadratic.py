#!/usr/bin/env python3
"""Independent arithmetic replay; no producer import. Critical audit is later."""
from fractions import Fraction as Q
from math import isqrt
from pathlib import Path
import json
import marked_octic_two_adic_image as L

BASE=Path(__file__).parent
SRC=BASE/'marked-octic-bounded-quadratic-certificate.json'
OUT=BASE/'marked-octic-bounded-quadratic-replay.json'
F=list(map(Q,[243,0,-3564,0,6930,0,-2860,0,275]))

def multiply(x,y):
    r=[Q(0)]*15
    for i,c in enumerate(x):
        for j,d in enumerate(y):r[i+j]+=c*d
    for k in range(14,7,-1):
        z=r[k]/275
        for j,c in enumerate(F):r[k-8+j]-=z*c
    return r[:8]

def determinant(m):
    m=[r[:] for r in m];out=Q(1);trace=[]
    for j in range(8):
        i=next(i for i in range(j,8) if m[i][j])
        if i!=j:m[i],m[j]=m[j],m[i];out=-out
        p=m[j][j];out*=p;trace.append(dict(column=j,pivot_row=i,pivot=p))
        for i in range(j+1,8):
            z=m[i][j]/p
            m[i]=[x-z*y for x,y in zip(m[i],m[j])]
    return out,trace

def vp(x,p):
    x=Q(x)
    if not x:return 10**6
    n,d=abs(x.numerator),x.denominator;v=0
    while n%p==0:n//=p;v+=1
    while d%p==0:d//=p;v-=1
    return v

def ev(c,x):
    v=Q(0)
    for z in reversed(c):v=v*x+z
    return v

def main():
    cert=json.loads(SRC.read_text());old=json.loads((BASE/'marked-octic-two-adic-image-certificate.json').read_text())
    checks=[];norms=[];local_rows=[]
    def check(name,actual,required):
        checks.append(dict(name=name,actual=actual,required=required,passed=actual==required))
    check('exact complete box',[(r['a'],r['b']) for r in cert['rows']],[(a,b) for a in range(-8,9) for b in range(-8,9)])
    eligible=[];square=[]
    for k,row in enumerate(cert['rows']):
        a,b=row['a'],row['b'];v=list(map(Q,[b,a,1,0,0,0,0,0]))
        cols=[multiply(v,[Q(int(i==j)) for i in range(8)]) for j in range(8)]
        matrix=[list(r) for r in zip(*cols)];n,trace=determinant(matrix)
        check('determinant '+str(k),str(n),row['norm'])
        # Replay the entire exact division identity, including zero coefficients.
        q=list(map(Q,row['division_quotient']));product=[Q(0)]*9
        for i,c in enumerate(q):
            for j,d in enumerate((b,a,1)):product[i+j]+=c*d
        for i,c in enumerate(map(Q,row['remainder'])):product[i]+=c
        check('division identity '+str(k),product,F)
        p,d=abs(n.numerator),n.denominator;ex=[]
        for ell in (2,3,5,11):
            z=vp(n,ell);ex.append(z)
            while p%ell==0:p//=ell
            while d%ell==0:d//=ell
        allowed=p==d==1
        check('all support data '+str(k),[ex,p,d,allowed],[row['support'][x] for x in ('exponents','numerator_remainder','denominator_remainder','eligible')])
        ns=n>0 and isqrt(n.numerator)**2==n.numerator and isqrt(n.denominator)**2==n.denominator
        check('norm square '+str(k),ns,row['norm_square'])
        if allowed:eligible.append([a,b])
        if allowed and ns:square.append([a,b])
        if ns:check('exact norm root '+str(k),Q(row['norm_square_root'])**2,n)
        norms.append(dict(pair=[a,b],matrix=matrix,elimination=trace,norm=n))
    check('all eligible pairs',eligible,cert['eligible_pairs'])
    check('complete local row list',[r['pair'] for r in cert['tested']],square)
    alpha=tuple(map(Q,old['field']['alpha_approximation']))
    r=tuple(map(Q,[468,-1126,Q(2585,3),Q(-5500,27)]))
    target=L.add(L.ONE,L.scale(r,4))
    check('Hensel target',target,tuple(map(Q,old['field']['alpha_square_target'])))
    cosets={tuple(r['residue']):r['label'] for r in old['residue_ring']['complete_unit_cosets']}
    table=old['residue_ring']['unit_multiplication_table'];scalars=old['scalar_labels']
    def lm(x,y):return 32*((x//32)^(y//32))+table[x%32][y%32]
    def label(x):
        w=L.val(x);u=L.residue(L.mul(x,L.power(L.PI,-w)))
        return dict(valuation=w,normalized_residue=u,label=32*(w%2)+cosets[u])
    # Independent higher-precision Newton lift for the unramified component.
    H=[3025,-31460,76230,-39204,2673];Hp=[(i+1)*H[i+1] for i in range(4)]
    M=5**10;r0=3
    for _ in range(5):r0=(r0-int(ev(H,r0))*pow(int(ev(Hp,r0)),-1,M))%M
    check('independent Hensel root',int(ev(H,r0))%M,0)
    check('same actual root ball',r0%(5**8),cert['five_transport']['r0_approximation'])
    rad=3*pow(r0,-1,M)%M;s=1
    for _ in range(5):s=(s-(s*s-rad)*pow(2*s,-1,M))%M
    check('independent principal square root',(s*s-rad)%M,0)
    check('same principal square-root ball',s%(5**8),cert['five_transport']['s_approximation'])
    for row in cert['tested']:
        a,b=row['pair'];name=str((a,b));bits=0
        for j,root in enumerate(cert['roots']):
            lo,hi=map(Q,root['interval']);check('root sign change '+name+str(j),ev(F,lo)*ev(F,hi)<0,True)
            # Factor-form bounds for the six split polynomials; direct positive bound for t²+3.
            if (a,b)==(0,3):negative=False;check('positive theta-square plus three '+str(j),lo*hi>0,True)
            else:
                # Exact extrema independently recomputed on the closed interval.
                values=[ev([b,a,1],x) for x in (lo,hi)]
                if lo<Q(-a,2)<hi:values.append(Q(4*b-a*a,4))
                check('strict sign interval '+name+str(j),min(values)>0 or max(values)<0,True)
                negative=max(values)<0
            bits|=int(negative)<<j
        signs=''.join('-' if bits>>j&1 else '+' for j in range(8))
        check('all eight signs '+name,signs,row['real_signs'])
        code=bits^(255 if bits&1 else 0);check('actual real membership '+name,code in (0,252,240,192),row['passes_real'])
        components=[]
        for j,sign in enumerate((1,-1)):
            # Use exact alpha² here, unlike producer alpha0².
            x=L.add(L.add(target,L.scale(alpha,sign*a)),L.scalar(b));lab=label(x)
            check('independent local label '+name+str(j),lab['label'],row['dyadic_components'][j]['label'])
            margin=None if not a else 20+4*vp(a,2)-lab['valuation']
            check('replay local precision '+name+str(j),margin is None or margin>8,True)
            c=row['dyadic_components'][j]
            bound=20+min(4,4*vp(a,2))
            check('producer cancellation bound '+name+str(j),[c['absolute_error_lower_bound'],c['relative_error_lower_bound']],
                  [bound,bound-c['valuation']])
            check('producer strict margin '+name+str(j),c['relative_error_lower_bound']>8,True)
            components.append(dict(exact_square_approximation=x,**lab,relative_error_lower_bound=margin,error_zero=not a))
        orbit=sorted((lm(components[0]['label'],s0),lm(components[1]['label'],s0)) for s0 in scalars)
        check('complete scalar orbit '+name,orbit,[tuple(x) for x in row['dyadic_orbit']])
        check('actual dyadic image '+name,min(orbit) in {tuple(x) for x in old['point_image']},row['passes_two'])
        x=Q(1,r0)+b;y=Q(a*s,3);w=min(vp(x,5),vp(y,5))
        unit=[x/Q(5)**w,y/Q(5)**w];res=[z.numerator*pow(z.denominator,-1,5)%5 for z in unit]
        nr=(res[0]**2-3*res[1]**2)%5
        u=row['five_U']
        check('full U class '+name,[w,res,nr,w%2,int(nr in (2,3))],
              [u['valuation'],u['normalized_residue'],u['residue_norm'],*u['square_class_bits']])
        check('producer strict five bound '+name,8-w,u['relative_error_lower_bound'])
        check('strict five bound '+name,8-w>0,True)
        for j,e in enumerate((4,2)):
            vals=([e*vp(a,5)+1] if a else [])+([e*vp(b,5)+2] if b else [])
            bound=min(vals) if vals else None
            check('ramified principal error '+name+str(j),bound,row['five_ramified_components'][j]['principal_error_lower_bound'])
            check('ramified strict square neighborhood '+name+str(j),bound is None or bound>0,True)
        # In every row the entire three-factor class is already square, stronger than quotient membership.
        check('actual unramified square class '+name,[w%2,int(nr in (2,3))],[0,0])
        check('five raw square class '+name,row['five_raw'],[0]*6)
        check('five identity membership '+name,[row['five_canonical'],row['passes_five']],['000000',True])
        local_rows.append(dict(pair=[a,b],dyadic=components,U=dict(r0=r0,s=s,valuation=w,residue=res,residue_norm=nr)))
    counts=dict(total=len(norms),eligible=len(eligible),norm_square=len(square),
        real_survivors=sum(r['passes_real'] for r in cert['tested']),
        real_two_survivors=sum(r['passes_real'] and r['passes_two'] for r in cert['tested']),
        removed_at_five=sum(r['passes_real'] and r['passes_two'] and not r['passes_five'] for r in cert['tested']))
    check('all counts',counts,cert['counts'])
    failures=[r['name'] for r in checks if not r['passed']]
    result=dict(norms=norms,local_replay=local_rows,counts=counts,checks=checks,failures=failures)
    OUT.write_text(json.dumps(L.clean(result),indent=2)+'\n')
    print(json.dumps(dict(checks=len(checks),counts=counts,failures=failures,path=str(OUT))))
    if failures:raise SystemExit(1)

if __name__=='__main__':main()
