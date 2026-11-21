#!/usr/bin/env python3
"""Fixed739 degree28 test. Candidates are not optimality certificates.

No734/735 data or code imported. Original moments through56 are rebuilt.
Basic Decimal directions are an explicit inherited assumption. Work counts
are LOWER subtotals only; never report a full cost/storage pass from them.
"""
from decimal import Decimal as D, Context, localcontext, ROUND_FLOOR, ROUND_CEILING
from fractions import Fraction as F
from math import comb
from pathlib import Path
from hashlib import sha256
import json
import sys
sys.set_int_max_str_digits(0)
HERE=Path(__file__).resolve()
OUT=HERE.with_suffix('.json')
PREC, DEG, DIM, NC=256,28,29,35
LABELS=[29,36,21,15,46,55,64,10,74,83,6,92,3,100,107,40,113,1,25,118,122,125,0,69,127,51,87,18,128,96,2,8,120,124,104]
DN=Context(prec=PREC,rounding=ROUND_FLOOR)
UP=Context(prec=PREC,rounding=ROUND_CEILING)
Z=D(0)
COUNT={'householder_dot_tail_terms':0,'householder_update_tail_terms':0,'gradient_terms':0,'triangular_terms':0,'rotation_columns':0,'gram_product_terms':0}

def q(x):
    x=F(x)
    return DN.divide(D(x.numerator),D(x.denominator)),UP.divide(D(x.numerator),D(x.denominator))
def add(a,b): return DN.add(a[0],b[0]),UP.add(a[1],b[1])
def sub(a,b): return DN.subtract(a[0],b[1]),UP.subtract(a[1],b[0])
def scale(a,c):
    c=D(c)
    return (DN.multiply(a[0],c),UP.multiply(a[1],c)) if c>=0 else (DN.multiply(a[1],c),UP.multiply(a[0],c))
def mid(a): return (a[0]+a[1])/2

def polynomials(n):
    ps=[[1],[0,1]]
    for k in range(2,n+1):
        p=[0]*(k+1)
        for i,c in enumerate(ps[-1]): p[i+1]+=2*c
        for i,c in enumerate(ps[-2]): p[i]-=c
        ps.append(p)
    return ps[:n+1]

def moments(J,bern,periodic):
    u,v=F(4*J+1,4),F(8*J+1,4)
    z=(v-u)/(v+u)
    assert 0<z<F(1,3)
    logpart,power=(Z,Z),z
    for i in range(256):
        logpart=add(logpart,q(2*power/(2*i+1)))
        power*=z*z
    logtail=F(2,513*3**513)*F(9,8)
    logpart=add(logpart,(Z,q(logtail)[1]))
    s1=(1/u-1/v)/2
    s2=1/u-1/v+(u**-2-v**-2)/2
    for r in range(1,64):
        s1+=bern[2*r]/(2*r)*(u**(-2*r)-v**(-2*r))
        s2+=bern[2*r]*(u**(-2*r-1)-v**(-2*r-1))
    err1=periodic*u**-128/128
    err2=periodic*u**-129
    e1,e2=q(err1)[1],q(J*err2)[1]
    xm=[add(q(J*s2),(-e2,e2)),add(add(logpart,q(s1)),(-e1,e1))]
    sums=[]
    for p in range(55):
        value=(v**(p+1)-u**(p+1)-sum((comb(p+1,l)*sums[l] for l in range(p)),F(0)))/(p+1)
        sums.append(value)
        xm.append(q(value/J**(p+1)))
    tm=[]
    for n in range(57):
        value=(Z,Z)
        for p in range(n+1): value=add(value,scale(xm[p],comb(n,p)*2**p*(-3)**(n-p)))
        tm.append(value)
    cm=[]
    for poly in polynomials(56):
        value=(Z,Z)
        for p,c in enumerate(poly): value=add(value,scale(tm[p],c))
        cm.append(value)
    return cm,{'exact_power_sums':list(map(str,sums)),'inverse_moment_remainders':list(map(str,[J*err2,err1])),'log_remainder':str(logtail)}

def data(J):
    indices=[J+i*(J-1)//128 for i in LABELS]
    assert len(set(indices))==NC and all(J<=j<2*J for j in indices)
    ts=[F(4*j+1,2*J)-3 for j in indices]
    cols=[]
    for t in ts:
        a=[F(1),t]
        for n in range(2,DIM): a.append(2*t*a[-1]-a[-2])
        cols.append(a)
    return indices,ts,cols

# Incremental Lawson--Hanson mechanism, retaining source rank/rejection,
# Householder/Givens and secondary-loop cases; finite Decimal adaptation.
# Column-major A. No correctness of this candidate code is a proof premise.
def nnls(cols,b):
    a=[[D(x.numerator)/D(x.denominator) for x in c] for c in cols]
    b=b[:]
    index=list(range(NC)); x=[Z]*NC; nset=0; main=secondary=0
    history=[]; state='not_started'
    def construct(j,p):
        if p+1>=DIM: return Z
        cl=max(abs(a[j][i]) for i in range(p,DIM))
        if not cl: return Z
        norm=cl*sum(((a[j][i]/cl)**2 for i in range(p,DIM)),Z).sqrt()
        if a[j][p]>0: norm=-norm
        up=a[j][p]-norm
        a[j][p]=norm
        return up
    def apply(j,p,up,c):
        if p+1>=DIM or up*a[j][p]>=0: return
        inverse=1/(up*a[j][p])
        sm=c[p]*up
        for i in range(p+1,DIM):
            sm+=c[i]*a[j][i]
            COUNT['householder_dot_tail_terms']+=1
        if sm:
            sm*=inverse
            c[p]+=sm*up
            for i in range(p+1,DIM):
                c[i]+=sm*a[j][i]
                COUNT['householder_update_tail_terms']+=1
    def triangular():
        zz=b[:]
        for i in range(nset-1,-1,-1):
            j=index[i]
            zz[i]/=a[j][i]
            for h in range(i):
                zz[h]-=a[j][h]*zz[i]
                COUNT['triangular_terms']+=1
        return zz
    def remove(pos):
        nonlocal nset
        removed=index[pos]; x[removed]=Z
        for r in range(pos+1,nset):
            col=index[r]; index[r-1]=col
            aa,bb=a[col][r-1],a[col][r]
            norm=(aa*aa+bb*bb).sqrt()
            cc,ss=(aa/norm,bb/norm) if norm else (Z,D(1))
            a[col][r-1],a[col][r]=norm,Z
            for j in range(NC):
                if j!=col:
                    temp=a[j][r-1]
                    a[j][r-1]=cc*temp+ss*a[j][r]
                    a[j][r]=-ss*temp+cc*a[j][r]
                    COUNT['rotation_columns']+=1
            temp=b[r-1]
            b[r-1]=cc*temp+ss*b[r]
            b[r]=-ss*temp+cc*b[r]
        nset-=1; index[nset]=removed
    while True:
        main+=1
        if main>210: state='MAIN_CAP'; break
        if nset>=DIM or nset==NC: state='RANK_LIMIT'; break
        w={}
        for j in index[nset:]:
            sm=Z
            for i in range(nset,DIM):
                sm+=a[j][i]*b[i]
                COUNT['gradient_terms']+=1
            w[j]=sm
        accepted=False
        while w:
            j=max(w,key=w.get)
            if w[j]<=0: break
            pos=index.index(j); p=nset; saved=a[j][p]
            up=construct(j,p)
            unorm=sum((a[j][i]**2 for i in range(p)),Z).sqrt()
            if unorm+abs(a[j][p])*D('.01')>unorm:
                zz=b[:]; apply(j,p,up,zz)
                if a[j][p] and zz[p]/a[j][p]>0:
                    accepted=True; break
            a[j][p]=saved; w[j]=Z
        if not accepted: state='STATIONARY'; break
        b=zz[:]
        index[pos],index[nset]=index[nset],j
        nset+=1
        for jj in index[nset:]: apply(j,p,up,a[jj])
        for i in range(nset,DIM): a[j][i]=Z
        zz=triangular()
        while True:
            secondary+=1
            if secondary>3*NC: state='SECONDARY_CAP'; break
            alpha=D(2); drop=None
            for ip in range(nset):
                l=index[ip]
                if zz[ip]<=0:
                    t=-x[l]/(zz[ip]-x[l])
                    if alpha>t: alpha=t; drop=ip
            if alpha==2:
                for ip in range(nset): x[index[ip]]=zz[ip]
                break
            for ip in range(nset):
                l=index[ip]; x[l]+=alpha*(zz[ip]-x[l])
            remove(drop)
            while True:
                bad=next((ip for ip in range(nset) if x[index[ip]]<=0),None)
                if bad is None: break
                remove(bad)
            zz=triangular()
        history.append({'main':main,'secondary':secondary,'active':[LABELS[i] for i in index[:nset]]})
        if state=='SECONDARY_CAP': break
    return x,{'state':state,'main_visits':main,'secondary_visits':secondary,'active_labels':[LABELS[i] for i in index[:nset]],'history':history}

def gram(cm): return [[scale(add(cm[i+j],cm[abs(i-j)]),D('.5')) for j in range(DIM)] for i in range(DIM)]
def inverse(h):
    a=[[mid(v) for v in row]+[D(int(i==j)) for j in range(DIM)] for i,row in enumerate(h)]
    for k in range(DIM):
        pivot=max(range(k,DIM),key=lambda i:abs(a[i][k]))
        if not a[pivot][k]: raise ArithmeticError('zero Gram candidate pivot')
        a[k],a[pivot]=a[pivot],a[k]
        for i in range(k+1,DIM):
            fac=a[i][k]/a[k][k]
            for j in range(k+1,2*DIM): a[i][j]-=fac*a[k][j]
            a[i][k]=Z
    r=[[Z]*DIM for _ in range(DIM)]
    for c in range(DIM):
        for i in range(DIM-1,-1,-1): r[i][c]=(a[i][DIM+c]-sum((a[i][j]*r[j][c] for j in range(i+1,DIM)),Z))/a[i][i]
    return r

def validate(R,H,cm,cols,x):
    E=[]; rowbounds=[]
    for i in range(DIM):
        row=[]; bound=Z
        for j in range(DIM):
            value=(Z,Z)
            for k in range(DIM):
                value=add(value,scale(H[k][j],R[i][k]))
                COUNT['gram_product_terms']+=1
            value=sub((D(int(i==j)),)*2,value)
            row.append(value); bound=UP.add(bound,max(abs(value[0]),abs(value[1])))
        E.append(row); rowbounds.append(bound)
    e=max(rowbounds)
    A=max(sum((F(abs(v)) for v in row),F(0)) for row in R)
    residual=[]
    for n in range(DIM):
        exact=sum((F(x[i])*cols[i][n] for i in range(NC)),F(0))
        residual.append(sub(q(exact),cm[n]))
    z=max(max(abs(v[0]),abs(v[1])) for v in residual)
    eps2=F(DIM)*F(z)**2*A/(1-F(e)) if e<1 else None
    return {'error_intervals':E,'error_row_upper':rowbounds,'contraction_upper':e,'inverse_preconditioner_norm_exact':str(A),'residual_intervals':residual,'raw_residual_upper':z,'epsilon_squared_upper_exact':str(eps2) if eps2 is not None else None,'nonnegative':all(v>=0 for v in x),'contraction_pass':e<1,'residual_pass':eps2 is not None and eps2<=F(5,10**19)**2}

def export(v):
    if isinstance(v,(D,F)): return str(v)
    if isinstance(v,dict): return {k:export(x) for k,x in v.items()}
    if isinstance(v,(list,tuple)): return [export(x) for x in v]
    return v

def save(report):
    report['counts_lower_subtotals']=COUNT.copy()
    OUT.write_text(json.dumps(export(report),indent=2)+'\n')

if __name__=='__main__':
    eps=F(5,10**19)
    early=F(2**46)*sum((F(1,4*2**k) for k in range(8,11)),F(0))*(F(1,5**34)+eps*(1+F(1,5**34)))
    later=F(2**46)*sum((F(1,4*2**k) for k in range(11,72)),F(0))*(F(1,5**28)+eps*(1+F(1,5**28)))
    tail=F(2**46,4*2**72-3)
    report={'script_sha256':sha256(HERE.read_bytes()).hexdigest(),'parameters':{'degree':28,'precision':256,'labels':LABELS,'k_first':11,'k_last':71,'epsilon':'5e-19','uniform_limit':'1e-7','work_limit':10**8},'analytic':{'early_exact':str(early),'later_exact':str(later),'tail_exact':str(tail),'total_exact':str(early+later+tail),'rounded_upper':'7.291e-8','pass':early+later+tail<F(7291,10**11)<F(1,10**7)},'blocks':[],'complete_work_upper_bound':None,'complete_byte_storage_upper_bound':None,'state':'IN_PROGRESS','failures':[]}
    save(report)
    assert report['analytic']['pass']
    with localcontext() as ctx:
        ctx.prec=PREC
        bern=[F(1)]
        for n in range(1,129): bern.append(-sum((comb(n+1,j)*bern[j] for j in range(n)),F(0))/(n+1))
        periodic=abs(bern[128])+sum((comb(128,j)*abs(bern[j]) for j in range(129)),F(0))
        R=None
        for k in range(11,72):
            J=2**k
            cm,evidence=moments(J,bern,periodic)
            indices,ts,cols=data(J)
            x,solver=nnls(cols,[mid(v) for v in cm[:DIM]])
            block={'k':k,'indices':indices,'nodes_exact':ts,'original_moments':cm,'moment_evidence':evidence,'weights_decimal':x,'solver':solver}
            report['blocks'].append(block)
            if solver['state'] in ('MAIN_CAP','SECONDARY_CAP'):
                report['failures'].append('candidate_'+solver['state']); report['state']='CANDIDATE_STOP'; save(report); break
            H=gram(cm)
            if R is None:
                R=inverse(H); report['anchor_preconditioner']=R
            block['validation']=validate(R,H,cm,cols,x)
            checks=block['validation']
            save(report)
            print('k',k,'state',solver['state'],'main',solver['main_visits'],'secondary',solver['secondary_visits'],'contraction',float(checks['contraction_upper']),'residual_pass',checks['residual_pass'],flush=True)
            if not (checks['nonnegative'] and checks['contraction_pass'] and checks['residual_pass']):
                report['state']='CERTIFICATE_STOP'; report['failures'].append('first_uncertified_block_'+str(k)); save(report); break
        else:
            report['state']='ALL_RESIDUALS_PASS_COST_UNCERTIFIED'; save(report)
    print('RESULT',report['state'],'required residual<=5e-19; B^2 error<=1e-7; work<=1e8; full work/bytes unproved; certificate',OUT)
