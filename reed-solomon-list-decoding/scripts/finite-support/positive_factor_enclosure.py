"""Single predeclared Newton trajectory and exact outward Krawczyk attempt."""
import gzip
import json
import time
from collections import defaultdict
from decimal import Decimal as D, getcontext
from fractions import Fraction as F
from math import comb
from pathlib import Path

B=Path(__file__).resolve().parent
OUT=B/'positive-factor-enclosure.json.gz'
getcontext().prec=90
Q=10**70
RAD=10**25  # 10^-45 in units 10^-70

def enc(x):
    x=F(x); return [x.numerator,x.denominator]
def dec(x):
    x=F(x); return D(x.numerator)/D(x.denominator)
def save(z):
    with gzip.open(OUT,'wt') as f: json.dump(z,f)
def cube_floor(n):
    lo,hi=0,1
    while hi**3<=n: hi*=2
    while hi-lo>1:
        m=(lo+hi)//2
        if m**3<=n: lo=m
        else: hi=m
    return lo

def solve(A,b):
    a=[list(r)+[v] for r,v in zip(A,b)]
    n=len(a)
    for k in range(n):
        p=max(range(k,n),key=lambda i:abs(a[i][k]))
        if not a[p][k]: raise ArithmeticError('zero candidate pivot')
        a[k],a[p]=a[p],a[k]
        pivot=a[k][k]
        a[k][k:]=[z/pivot for z in a[k][k:]]
        for i in range(k+1,n):
            m=a[i][k]
            if m:
                for j in range(k+1,n+1): a[i][j]-=m*a[k][j]
                a[i][k]=D(0)
    ans=[D(0)]*n
    for i in range(n-1,-1,-1):
        ans[i]=a[i][-1]-sum(a[i][j]*ans[j] for j in range(i+1,n))
    return ans

def inverse(A):
    n=len(A); a=[list(r)+[D(i==j) for j in range(n)] for i,r in enumerate(A)]
    for k in range(n):
        p=max(range(k,n),key=lambda i:abs(a[i][k]))
        if not a[p][k]: raise ArithmeticError('zero inverse pivot')
        a[k],a[p]=a[p],a[k]
        pivot=a[k][k]; a[k]=[z/pivot for z in a[k]]
        for i in range(n):
            if i!=k:
                m=a[i][k]
                if m:
                    a[i]=[x-m*y for x,y in zip(a[i],a[k])]
    return [r[n:] for r in a]

def main():
    start=time.monotonic()
    lp=json.loads((B/'delsarte-lp-results.json').read_text())
    a=[F(z['numerator'],z['denominator']) for z in lp['exact']['primal']]
    N=65537**28//2**128+1; H=comb(1024,68)
    U=F(comb(1024,64),comb(68,64)); g=[comb(68,i)*comb(956,i) for i in range(69)]
    c=[F(1)]+[F(0)]*4+[(N-1)*a[i-5]/((U-1)*g[i]) for i in range(5,69)]
    assert len(a)==64 and min(a)>0 and sum(a)==U-1
    assert sum(g[i]*c[i] for i in range(69))==N
    K=cube_floor(H//(N-1)); assert K**3*(N-1)<=H<(K+1)**3*(N-1)
    initial=[z*K for z in c[5:]]
    powers=[dec(x).adjusted() for x in initial]
    scales=[F(10)**e for e in powers]
    demands=[(N-2)*z for z in c[5:]]
    terms=[defaultdict(int) for _ in range(64)]
    count=dict(original=0,repeated=0,null=0,permitted=0)
    for i in range(69):
        for j in range(69):
            for t in range(max(0,i+j-68),min(i,j)+1):
                left=comb(i,t)*comb(68-i,j-t)
                for s in range(max(0,i+j-956),min(i,j)+1):
                    h=i+j-t-s; count['original']+=1
                    coef=left*comb(i,s)*comb(956-i,j-s)
                    if min(i,j,h)==0: count['repeated']+=1
                    elif min(i,j,h)<5: count['null']+=1
                    else:
                        count['permitted']+=1
                        terms[i-5][tuple(sorted((j-5,h-5)))]+=coef
    rows=[[[j,h,v] for (j,h),v in sorted(row.items())] for row in terms]
    report=dict(stage='coefficients',N=N,H=H,K=K,c=[enc(x) for x in c],
                scale_powers=powers,demands=[enc(x) for x in demands],
                coefficients=rows,counts=count,Q=Q,radius=RAD,
                initial=[enc(x/s) for x,s in zip(initial,scales)],trajectory=[])
    save(report)
    co=[]
    for i,row in enumerate(rows):
        co.append([(j,h,dec(F(v)*scales[i]*scales[j]*scales[h]/demands[i])) for j,h,v in row])
    u=[dec(x/s) for x,s in zip(initial,scales)]
    def evaluate(u,jac=False):
        values=[]; J=[]
        for i,row in enumerate(co):
            v=D(-1); r=[D(0)]*64
            for j,h,b in row:
                bjh=b*u[j]*u[h]; v+=u[i]*bjh
                if jac:
                    r[i]+=bjh
                    r[j]+=b*u[i]*u[h]
                    r[h]+=b*u[i]*u[j]
            values.append(v); J.append(r)
        return values,J
    success=False
    try:
        for it in range(101):
            if time.monotonic()-start>300: raise TimeoutError('candidate budget')
            f,J=evaluate(u,True); norm=max(map(abs,f))
            report['trajectory'].append(dict(iteration=it,max_residual=str(norm)))
            if norm<D('1e-65'): success=True; break
            if it==100: break
            delta=solve(J,[-x for x in f]); accepted=False
            for half in range(21):
                step=D(2)**(-half); trial=[x+step*z for x,z in zip(u,delta)]
                if min(trial)<=0: continue
                tf,_=evaluate(trial)
                if max(map(abs,tf))<norm:
                    u=trial; report['trajectory'][-1]['halvings']=half
                    accepted=True; break
            if not accepted: raise ArithmeticError('no accepted damped step')
    except (ArithmeticError,TimeoutError) as e:
        report['candidate_error']=str(e)
    report['candidate_success']=success
    report['candidate_decimal']=[str(x) for x in u]
    report['stage']='candidate_complete' if success else 'candidate_failed'
    save(report)
    if not success:
        print(json.dumps(dict(stage=report['stage'],iterations=len(report['trajectory'])-1,
          residual=report['trajectory'][-1]['max_residual'],required='1e-65',path=str(OUT))))
        return
    point=[int(x*D(Q)) for x in u]
    R=[[int(x*D(Q)) for x in row] for row in inverse(J)]
    report.update(point=point,preconditioner=R,stage='exact_started'); save(report)
    exact_start=time.monotonic()
    def mul(x,y):
        vals=[a*b for a in x for b in y]
        return (min(vals)//Q,-((-max(vals))//Q))
    def add(x,y): return (x[0]+y[0],x[1]+y[1])
    boxes=[(x-RAD,x+RAD) for x in point]
    assert min(x[0] for x in boxes)>0
    residual=[]; jacobian=[]; coeff_bounds=[]
    for i,row in enumerate(rows):
        if time.monotonic()-exact_start>180:
            report['stage']='exact_incomplete'; save(report); print('exact budget exceeded',OUT); return
        rv=(-Q,-Q); jr=[(0,0) for _ in range(64)]; cb=[]
        for j,h,v in row:
            b=F(v)*scales[i]*scales[j]*scales[h]/demands[i]
            low=b.numerator*Q//b.denominator
            high=-((-b.numerator*Q)//b.denominator)
            bi=(low,high); cb.append([j,h,low,high])
            rv=add(rv,mul(mul(mul(bi,(point[i],)*2),(point[j],)*2),(point[h],)*2))
            for k,p,q in ((i,j,h),(j,i,h),(h,i,j)):
                jr[k]=add(jr[k],mul(mul(bi,boxes[p]),boxes[q]))
        residual.append(rv); jacobian.append(jr); coeff_bounds.append(cb)
    rf=[]; defect=[]; image=[]; margins=[]
    for i in range(64):
        rf_i=(0,0)
        for k in range(64): rf_i=add(rf_i,mul((-R[i][k],)*2,residual[k]))
        rr=[]
        for j in range(64):
            v=(Q if i==j else 0,)*2
            for k in range(64): v=add(v,mul((-R[i][k],)*2,jacobian[k][j]))
            rr.append(v)
        si=rf_i
        for v in rr: si=add(si,mul(v,(-RAD,RAD)))
        rf.append(rf_i); defect.append(rr); image.append(si)
        margins.append(min(si[0]+RAD,RAD-si[1]))
    inclusion=min(margins)>0
    lo=F(point[0]-RAD,Q)*scales[0]; hi=F(point[0]+RAD,Q)*scales[0]
    verdict='pass' if hi**3<=c[5] else 'reject_enclosed_root' if lo**3>c[5] else 'straddles'
    report.update(stage='exact_complete',coefficient_bounds=coeff_bounds,
       box=boxes,residual=residual,jacobian=jacobian,negative_R_residual=rf,
       defect=defect,krawczyk_image=image,inclusion_margins=margins,
       inclusion=inclusion,capacity=dict(lower_cube_ratio=enc(lo**3/c[5]),
       upper_cube_ratio=enc(hi**3/c[5]),verdict=verdict),
       exact_seconds=time.monotonic()-exact_start)
    save(report)
    print(json.dumps(dict(stage=report['stage'],iterations=len(report['trajectory'])-1,
       residual=report['trajectory'][-1]['max_residual'],required='1e-65',
       inclusion=inclusion,min_margin_units=min(margins),required_margin='>0',
       capacity=verdict,ratio_lower=str(dec(lo**3/c[5])),
       ratio_upper=str(dec(hi**3/c[5])),path=str(OUT))))

if __name__=='__main__': main()
