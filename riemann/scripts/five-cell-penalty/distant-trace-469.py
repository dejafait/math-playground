"""Complete fixed covariance: transformed trace prefix plus entire tail.

Uses the prior same-step q=4096 certificate for core T values. All sums
retain the full response, prime, pole and ten-moment mixed cross terms.
"""
import hashlib
import json
import runpy
from decimal import Decimal
from pathlib import Path

HERE=Path(__file__).resolve().parent
OUT=HERE/'distant-trace-469.json'
names=['certify-455.py','refined-464.json','compression-463.json',
       'certificate-455.json','distant-469.json']
snap={name:(HERE/name).read_bytes() for name in names}
lib=runpy.run_path(str(HERE/'certify-455.py'))
I,A,PI,ELL,UP=(lib[z] for z in ('I','A','PI','ELL','UP'))
sc=lib['sincos']
sv=lambda x:I(x['lo'],x['hi'])
mag=lambda x:max(x.lo.copy_abs(),x.hi.copy_abs())
jm=lambda x:[[v.json() for v in row] for row in x]
ji=lambda x:[v.json() for v in x]
err=lambda e:I(e.copy_negate(),e)
core=json.loads(snap['refined-464.json'])
old=json.loads(snap['compression-463.json'])
base=json.loads(snap['certificate-455.json'])
first=json.loads(snap['distant-469.json'])
D,Q,E,K=64,4096,16384,16
report={'status':'IN_PROGRESS','parameters':{'core':D,'distant_start':Q,
        'prefix_end':E,'penalty':256,'geometric_terms':K},
        'input_sha256':{n:hashlib.sha256(b).hexdigest() for n,b in snap.items()},
        'checks':[],'failures':[]}


def save(): OUT.write_text(json.dumps(report,indent=2)+'\n')


def check(name,truth):
    report['checks'].append({'name':name,'passed':bool(truth)})
    if not truth:
        report['failures'].append(name)
        save()
        raise AssertionError(name)


def pw(x,n):
    y=I(1)
    while n:
        if n%2:y*=x
        x=x.sq();n//=2
    return y


def norm_upper(v):
    return sum((I(mag(x)).sq() for x in v),I(0)).sqrt().hi


def transform(v):
    return [sum((B[r][s]*v[s] for s in range(D)),I(0)) for r in range(D)]


check('same accepted interval source',report['input_sha256']['certify-455.py']==first['input_sha256']['certify-455.py'])
check('same accepted complete core',report['input_sha256']['refined-464.json']==first['input_sha256']['refined-464.json'])
B=[[sv(x) for x in row] for row in core['congruence']['B']]
u=[(s*PI/A).sq() for s in range(D)]
k=[s*PI/A for s in range(D)]
n=[(1/A).sqrt()]+[(2/A).sqrt()]*(D-1)
nq=(2/A).sqrt()
U=u[-1]
Z=[]
E0=(-A).exp()/(1-(-4*A).exp())
exp_tail=(-2*A*(I(257)/2)).exp()/(1-(-4*A).exp())
for s in range(D):
    te=sum(((-2*A*(I(4*j+1)/2)).exp()*u[s]/((I(4*j+1)/2).sq()+u[s])
            for j in range(64)),I(0))+I(0,exp_tail.hi)
    ar=sum((I(p).ln()/I(nn).sqrt()*k[s]*sc(k[s]*I(nn).ln())[0]
             for nn,p,_ in lib['PRIMES']),I(0))
    Z.append(sv(first['T_values'][s]['T'])-te+ar)

# The geometric series is in u_s/v. Normalize powers by U to keep
# coefficients bounded, and combine core rows before absolute bounds.
w=[[B[r][s]*n[s]*((-1)**s) for s in range(D)] for r in range(D)]
am=[[I(0) for _ in range(K)] for _ in range(D)]
dm=[[I(0) for _ in range(K)] for _ in range(D)]
rat=[u[s]/U for s in range(D)]
power=[I(1) for _ in range(D)]
for m in range(K):
    for r in range(D):
        am[r][m]=sum((w[r][s]*power[s] for s in range(D)),I(0))
        dm[r][m]=sum((w[r][s]*Z[s]*power[s] for s in range(D)),I(0))
    power=[power[s]*rat[s] for s in range(D)]
wa=[sum((I(mag(x)) for x in row),I(0)).hi for row in w]
wd=[sum((I(mag(w[r][s]*Z[s])) for s in range(D)),I(0)).hi for r in range(D)]
vp=(Q*PI/A).sq()
R=U/vp
arerr=[(I(wa[r])*pw(R,K)/(vp-U)).hi for r in range(D)]
drerr=[(I(wd[r])*pw(R,K)/(vp-U)).hi for r in range(D)]

bp=transform([sv(x) for x in old['pole_row']])
pc=(A/2).exp()*(1-(-A).exp())/2
P=[x*pc for x in bp]
bmo=[transform([sv(x) for x in row['row']]) for row in old['all_ten_moment_rows']]
moment_sin=[];moment_cos=[]
for res in range(10):
    us=[I(0) for _ in range(D)];vs=[I(0) for _ in range(D)]
    for bvec,row in zip(bmo,old['all_ten_moment_rows']):
        cell,sigma=row['cell'],row['sigma']
        sl,cl=sc(res*(2*cell-5)*PI/5)
        sr,cr=sc(res*(2*cell-3)*PI/5)
        el,er=(-sigma*ELL/4).exp(),(sigma*ELL/4).exp()
        for r in range(D):
            us[r]+=256*bvec[r]*(er*sr-el*sl)
            vs[r]+=256*bvec[r]*I(sigma)/2*(er*cr-el*cl)
    moment_sin.append(us);moment_cos.append(vs)
report['combined_coefficients']={'core_Z':ji(Z),'a':jm(am),'d':jm(dm),
    'a_uniform_error':list(map(str,arerr)),'d_uniform_error':list(map(str,drerr)),
    'wa':list(map(str,wa)),'wd':list(map(str,wd)),'P':ji(P),
    'moment_sin':jm(moment_sin),'moment_cos':jm(moment_cos),'E0':E0.json()}

# Entire q>=E covariance trace. See canonical proof for the two powers.
ke=E*PI/A;ve=ke.sq();re=U/ve
ae=[];de=[]
for r in range(D):
    at=sum((I(mag(am[r][m]))*pw(re,m) for m in range(1,K)),I(0))
    dt=sum((I(mag(dm[r][m]))*pw(re,m) for m in range(K)),I(0))
    at+=I(wa[r])*pw(re,K)/(1-re)
    dt+=I(wd[r])*pw(re,K)/(1-re)
    ae.append(I(at.hi));de.append(I(dt.hi))
a0=[am[r][0] for r in range(D)]
alpha=sum((I(p).ln()/I(nn).sqrt() for nn,p,_ in lib['PRIMES']),I(0))
cmax=PI/4+alpha
na0=I(norm_upper(a0));nae=I(norm_upper(ae));nde=I(norm_upper(de));np=I(norm_upper(P))
nbound=I(norm_upper([I(mag(a0[r]))+ae[r] for r in range(D)]))
tail_res=[]
for res in range(10):
    lead=[((-1)**res)*PI/4*a0[r]+moment_sin[res][r]/I(2).sqrt() for r in range(D)]
    aa=nq*(I(norm_upper(lead))+alpha*na0+cmax*nae)
    bb=nq*((1+E0)*nbound+nde+np+(I(norm_upper(moment_cos[res]))+
         I(norm_upper(moment_sin[res]))/(4*ke))/I(2).sqrt())
    tail_res.append({'residue':res,'A':aa.json(),'B':bb.json()})
at=I(max(sv(x['A']).hi for x in tail_res))
bt=I(max(sv(x['B']).hi for x in tail_res))
rho=sv(base['complement_floors'][0]['rho'])
te=(I(E)/(2*A)).ln()-2/ve-rho
check('positive entire-tail weight',te.lo>0)
series={p:(I(E)**p if False else I(0)) for p in ()}  # populated below
for p in (2,3,4):
    series[p]=pw(I(E).reciprocal(),p)+pw(I(E).reciprocal(),p-1)/(p-1)
ak=at*A/PI;bk=bt*(A/PI).sq()
tail=(ak.sq()*series[2]+2*ak*bk*series[3]+bk.sq()*series[4])/I(te.lo)
report['entire_tail']={'residue_bounds':tail_res,'A_max':at.json(),'B_max':bt.json(),
    'weight_lower':str(te.lo),'series':{str(p):x.json() for p,x in series.items()},
    'trace_upper':str(tail.hi),'start':E}
print('Entire covariance tail trace upper',tail.hi,'; required with prefix < 1-epsilon',flush=True)
save()

# Finite prefix. Monotone integral encloses the complete T(v) to width<=1:
# int_0^infty f <= sum_(j>=0)f(j) <= int_0^infty f+f(0),
# int = k/2*(pi/2-atan(1/(2k))). The 5-term alternating arctan has
# error <= x^11/11. All exponential responses remain included.
expterms=[((I(4*j+1)/2).sq(),(-2*A*(I(4*j+1)/2)).exp()) for j in range(16)]
texperr=(-2*A*(I(65)/2)).exp()/(1-(-4*A).exp())
phases=[]
for nn,p,_ in lib['PRIMES']:
    omega=PI/A*I(nn).ln()
    so,co=sc(omega)
    phases.append({'omega':omega,'so':so,'co':co,'alpha':I(p).ln()/I(nn).sqrt()})
trace=I(0);rows=[]
eps=I(core['congruence']['norm_upper'])
for q in range(Q,E):
    kq=q*PI/A;v=kq.sq();z=U/v
    xx=1/(2*kq)
    atan=sum((((-1)**j)*pw(xx,2*j+1)/(2*j+1) for j in range(5)),I(0))
    atan+=err((pw(xx,11)/11).hi)
    integral=kq/2*(PI/2-atan)
    tq=I(integral.lo,(integral+v/(v+I(1)/4)).hi)
    eq=sum((e*v/(c2+v) for c2,e in expterms),I(0))+I(0,texperr.hi)
    ar=I(0)
    for phase in phases:
        if (q-Q)%32==0:phase['s'],phase['c']=sc(q*phase['omega'])
        ar+=phase['alpha']*kq*phase['s']
    zz=tq-eq+ar
    y=[]
    for r in range(D):
        ap,dp=am[r][-1],dm[r][-1]
        for m in range(K-2,-1,-1):
            ap=ap*z+am[r][m];dp=dp*z+dm[r][m]
        ap=ap/v+err(arerr[r]);dp=dp/v+err(drerr[r])
        yy=nq*((-1)**q)*(zz*ap-dp+P[r]/(v+I(1)/4))
        yy+=nq/I(2).sqrt()*(kq*moment_sin[q%10][r]+moment_cos[q%10][r])/(v+I(1)/4)
        y.append(yy)
    t=(I(q)/(2*A)).ln()-2/v-rho
    check('positive weight '+str(q),t.lo>0)
    yn=sum((yy.sq() for yy in y),I(0))
    contribution=yn/I(t.lo)
    trace+=contribution
    rows.append({'q':q,'Z':zz.json(),'T':tq.json(),'T_exp':eq.json(),
                  'B_column':ji(y),'norm_squared':yn.json(),
                  'weight_lower':str(t.lo),'trace_contribution':contribution.json()})
    if q==Q:
        check('all first column enclosures intersect direct complete evaluation',
          all(max(yy.lo,sv(saved).lo)<=min(yy.hi,sv(saved).hi)
              for yy,saved in zip(y,first['B_column'])))
    for phase in phases:
        sn=phase['s']*phase['co']+phase['c']*phase['so']
        cn=phase['c']*phase['co']-phase['s']*phase['so']
        phase['s'],phase['c']=sn,cn
    if (q+1-Q)%1024==0:
        report['prefix_completed_through']=q
        report['prefix_running_trace']=trace.json()
        print('Prefix through',q,'trace upper',trace.hi,flush=True)
        # Keep full unfinished evidence on disk as it is obtained.
        report['prefix']=rows;save()
total=trace+tail
report['prefix']=rows
report['prefix_trace']=trace.json()
report['total_trace_upper']=str(total.hi)
report['required_upper']=str((1-eps).lo)
positive=total.hi<(1-eps).lo
report['status']='CERTIFIED_POSITIVE_COMPLETE_DISTANT_COMPARISON' if positive else 'TRACE_BOUND_INCONCLUSIVE'
if not positive:report['failures'].append('trace upper does not pay complete covariance; no positive or negative sign follows')
check('old inputs preserved',all((HERE/n).read_bytes()==b for n,b in snap.items()))
report['script_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
save()
print('Result',report['status'],'; prefix',trace.hi,'; tail',tail.hi,'; total',total.hi,
      '; required <',(1-eps).lo,'; failures',report['failures'],'; full certificate',OUT,flush=True)
