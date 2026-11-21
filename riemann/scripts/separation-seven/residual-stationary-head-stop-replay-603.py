#!/usr/bin/env python3
"""Single stationary-surrogate fixed trial603. No optimizer or exact-map solve claim."""
import hashlib, importlib.util, json
from pathlib import Path
from decimal import Decimal, Context, ROUND_CEILING, ROUND_FLOOR, ROUND_HALF_EVEN, localcontext
import numpy as np
BASE=Path(__file__).resolve().parent
ROOT=BASE.parent.parent
N,J,K,E,F=512,1024,65536,2044,1022
TARGET="Test one dyadic neutral middle map proposed by stationary equations for the finite-output residual-corrected functional, verifying the unchanged joint2044 .000999 comparison with every finite and infinite output."
def load(name,path):
    s=importlib.util.spec_from_file_location(name,path); m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
iv=load('iv594',BASE/'complete-schur-531.py')
iv.DOWN=Context(prec=80,rounding=ROUND_FLOOR);iv.UP=Context(prec=80,rounding=ROUND_CEILING);iv.NEAR=Context(prec=80,rounding=ROUND_HALF_EVEN)
I=iv.I
old=load('entries594',BASE/'residual-certificate-532.py')
checks=[];failures=[];ledger={};bounds={};arrays={};pins={}
def check(ok,label):
    checks.append(dict(label=label,passed=bool(ok)))
    if not ok: failures.append(label)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def ab(x):return max(x.lo.copy_abs(),x.hi.copy_abs())
def sq(x):return I(0,iv.UP.multiply(ab(x),ab(x))) if x.lo<=0<=x.hi else x*x
def powi(x,n):
    y=I(1)
    for _ in range(n):y*=x
    return y
def atan(q):
    x=I(1)/q;s=sum(((-1)**j*powi(x,2*j+1)/(2*j+1) for j in range(80)),I(0));r=powi(x,161)/161
    return s+I(-r.hi,r.hi)
def uf(x):return float(np.nextafter(float(x.hi),np.inf))
def nf(x):return I(Decimal(float(np.linalg.norm(x))))*I('1.00000001')+I('1e-290')
def positive(name,matrix):
    try:
        ff=np.linalg.cholesky(matrix); rr=nf(matrix-ff@ff.T);ff2=sq(nf(ff))
        # All factor dimensions <=2044: gamma_4096<5e-13.
        allowance=I('5e-13')*(ff2+nf(matrix)+1)+I('1e-8')
        err=rr+allowance
        check(err.hi<Decimal('1e-6'),name+' reconstruction<1e-6')
        check(np.abs(matrix).max()<1000 and ff2.hi<100000,name+' magnitude ledger')
        arrays['factor_'+name]=ff
        ledger[name]=dict(observed_residual=rr.json(),rounding=allowance.json(),total=err.json(),factor_norm_squared=ff2.json())
        return not(err.hi>=Decimal('1e-6'))
    except np.linalg.LinAlgError:
        ledger[name]=dict(factor_proposed=False);check(False,name+' factor unavailable');return False

def response_error(rows,cols):
    # Bounds use exact rational 5.719<pi/ell<5.720 and sqrt2<1.415.
    nn=np.asarray(rows,dtype=float);mm=np.asarray(cols,dtype=float)
    rn=1.415/(6*(64.25**2+(5.719*nn/2)**2));rm=1.415/(6*(64.25**2+(5.719*mm/2)**2))
    den=np.abs(nn[:,None]**2-mm[None,:]**2);same=den==0;den[same]=1
    out=(2/3.14159)*(nn[:,None]*rn[:,None]+mm[None,:]*rm[None,:])/den
    # Opposite parity entries of S vanish algebraically, but their scalar
    # elementary error stays covered even if their centers are exactly0.
    out*=((nn[:,None]-mm[None,:])%2==0)
    for row,col in zip(*np.where(same)):
        c=131072.5
        out[row,col]=rn[row]+8*(c**-2+2*(5.720*nn[row])**2*(1/(6*c**3)+c**-4))
    # Entire elementary entry ledger + formula-rounding overestimate.
    return out+1e-7+1e-12

def require(ok,label):
    check(ok,label)
    if not ok: raise RuntimeError(label)

def raw_blocks(M,T,Ts):
    """All dyadic row centers; formulas from598, complete ranges unchanged."""
    yield 0,M,T,Ts
    con=old.constants();el,pif=con['ell'],con['pi']
    indices=np.arange(K);k=indices*pif/el
    nu=np.full(K,np.sqrt(2/el));nu[0]=1/np.sqrt(el)
    parity=np.where(indices%2==0,1.,-1.)
    im,_=old.psi_imag(k,pif);bpsi=k*im/2
    with localcontext() as c:
        c.prec=80;fourth=Decimal(3).sqrt().sqrt()
        decays=[float(Decimal(1)/(Decimal(3)**j*fourth)) for j in range(64)]
        cc=[float(Decimal(1)/(Decimal(3)**(6*j+1)*Decimal(3).sqrt())) for j in range(1,8)]
    def translation(rows,delta):
        kn,km=k[rows,None],k[None,:J]
        sn,_=old.sincos(k[rows]*delta,pif);sm,_=old.sincos(k[:J]*delta,pif)
        sig=parity[rows,None]*parity[None,:J]
        num=(-sig*kn*sn[:,None]+km*sm[None,:] if delta>0 else kn*sn[:,None]-sig*km*sm[None,:])
        return num/(kn*kn-km*km)*np.outer(nu[rows],nu[:J])
    for start in range(J,K,N):
        rows=slice(start,start+N);kn,km=k[rows,None],k[None,:J]
        response=(bpsi[rows,None]-bpsi[None,:J])/(kn*kn-km*km)
        for j in range(64):
            c=2*j+.5
            response-=decays[j]*parity[rows,None]*c*c/((c*c+kn*kn)*(c*c+km*km))
        response*=2*np.outer(nu[rows],nu[:J])*(parity[rows,None]==parity[None,:J])
        tt,ts=np.zeros_like(response),np.zeros_like(response)
        for delta,w in zip(con['deltas'],con['weights']):
            tt+=w*translation(rows,delta);ts+=w*translation(rows,-delta)
        for j in range(1,8):
            c=2*j+.5
            minus=nu*c*(1-parity*decays[j])/(c*c+k*k)
            plus=nu*c*(parity-decays[j])/(c*c+k*k)
            tt+=cc[j-1]*np.outer(minus[rows],plus[:J])
            ts+=cc[j-1]*np.outer(plus[rows],minus[:J])
        yield start,response,tt,ts

# This replay records the first failing gate only. No new proposal/tuning.
stop=json.loads((BASE/'residual-stationary-fixed-trial-603.json').read_text())
require(stop['script_sha256']==sha(BASE/'residual-stationary-fixed-trial-603.py'),'executed603 source pin')
require(stop['archive']['sha256']==sha(BASE/'residual-stationary-fixed-trial-603.npz'),'603 factor archive pin')
prop=stop['ledger']['proposal']
require(prop['sha256']==sha(ROOT/prop['path']),'single saved proposal pin')
for n,h in stop['input_hashes'].items():require(sha(BASE/n)==h,'inherited input preserved '+n)
with np.load(ROOT/prop['path']) as q:Y,Z=q['Y'].copy(),q['Z_center'].copy()
with np.load(BASE/'original-galerkin-586.npz') as q:
    M,T,Ts,U=[q[n].copy() for n in ['local_matrix','t_entries','ts_entries','u_entries']]
with np.load(BASE/'complete-covariance-532.npz') as q:
    H=q['m0']-.00024*np.eye(N)-(100/307)*(q['cov00']+.0046*np.eye(N))
with np.load(BASE/'residual-stationary-fixed-trial-603.npz') as q:
    ff=q['factor_predictor_norm'].copy();hf=q['factor_reference_floor'].copy()
# Reconstruct the complete norm and reference factors saved by the original run.
yfloat=float(np.ceil(np.sqrt(np.linalg.eigvalsh(Y@Y.T)[-1])*10000)/10000+.0001)
yfloatI=I(Decimal(yfloat));yn=yfloatI+I('1e-6');zn=I('1.008')
gamma=lambda n:I(n)/(I(2**53)-I(n))
req=I('1e-6')+gamma(4096)*sq(nf(Y))+I('1e-9')
require((sq(yn)-sq(yfloatI)).lo>req.hi,'predictor inflation pays factor and Gram error')
for name,target,f in [('new predictor factor',yfloat*yfloat*np.eye(F)-Y@Y.T,ff),
                      ('unchanged reference factor',H-.24*np.eye(N),hf)]:
    err=nf(target-f@f.T)+I('5e-13')*(sq(nf(f))+nf(target)+1)+I('1e-8')
    require(err.hi<Decimal('1e-6'),name+' full reconstruction')
    ledger[name]=dict(full_reconstruction_error=err.json(),required='1e-6')
G=Z@Y;rho=np.hstack((T@Z,Ts@Z))-M@G
sol=np.linalg.solve(H,rho[:N])
equation=nf(rho[:N]-H@sol)
head_solve=equation+I('1e-8')*nf(sol)+I('1e-6')
head_error=nf(rho[:N])*head_solve/I('.239999')+I('1e-6')
# Full arithmetic budgets, using the new actual Frobenius magnitudes.
arithmetic={
 'H_assembly':gamma(16)*401+I('1e-10'),
 'G_product':gamma(4096)*nf(Z)*nf(Y)+I('1e-10'),
 'row_map':gamma(4096)*(2*nf(T)*nf(Z)+nf(M)*nf(G))+I('1e-8'),
 'head_equation':gamma(4096)*(nf(H)*nf(sol)+nf(rho[:N]))+I('1e-8'),
 'head_product_matrix_and_nuclear':I(E).sqrt()*gamma(4096)*nf(rho[:N])*nf(sol)+I('1e-8')}
limits={'H_assembly':'1e-8','G_product':'1e-6','row_map':'1e-6',
        'head_equation':'1e-6','head_product_matrix_and_nuclear':'1e-6'}
for n,v in arithmetic.items():check(v.hi<Decimal(limits[n]),'replay arithmetic budget '+n)
bounds.update(predictor_norm=yn.json(),free_predictor_fro=nf(Y).json(),raw_predictor_fro=nf(G).json(),
              head_rhs_fro=nf(rho[:N]).json(),head_solution_fro=nf(sol).json(),
              head_equation_observed=equation.json(),head_inverse_solution_error=(head_solve/I('.239999')).json(),
              head_inverse_matrix_nuclear_error=head_error.json())
# The upper error estimate exceeds this prescribed allowance. This is NOT
# a lower bound on actual rounding or an actual target-sign calculation.
check(head_error.hi>=Decimal('1e-5'),'original preset head allowance is insufficient')
arrays.update(Y=Y,G_center=G,head_rhs_center=rho[:N],head_solution=sol,
              head_covariance_center=(rho[:N].T@sol+sol.T@rho[:N])/2)
a=BASE/'residual-stationary-head-stop-replay-603.npz';np.savez_compressed(a,**arrays)
out=BASE/'residual-stationary-head-stop-replay-603.json'
r=dict(result='PRESET_HEAD_ERROR_ALLOWANCE_EXCEEDED',actual_target_sign='UNDECIDED',
       required_gate='computed head matrix/nuclear error upper <1e-5',bounds=bounds,ledger=ledger,
       arithmetic={n:dict(actual=v.json(),required=limits[n]) for n,v in arithmetic.items()},
       checks=checks,failures=failures,script_sha256=sha(Path(__file__)),
       first_pass_sha256=sha(BASE/'residual-stationary-fixed-trial-603.json'),
       proposal_sha256=prop['sha256'],archive=dict(path=str(a.relative_to(ROOT)),sha256=sha(a)),
       uncomputed_outputs='1024:65535 and all n>=65536',
       qualification='An upper estimate exceeding a chosen allowance is inconclusive; no new solve proposal, no actual sign, no full comparison.')
out.write_text(json.dumps(r,indent=2)+'\n')
print('Result',r['result'],'actual target UNDECIDED; replay failures',failures)
print('Head matrix/nuclear error upper',head_error.hi,'preset required <1e-5')
for n,v in arithmetic.items():print(n,'actual upper',v.hi,'required <',limits[n])
print('Predictor norm upper',yn.hi,'head RHS Fro upper',nf(rho[:N]).hi)
print('Full certificate',out.relative_to(ROOT),'arrays',a.relative_to(ROOT))
