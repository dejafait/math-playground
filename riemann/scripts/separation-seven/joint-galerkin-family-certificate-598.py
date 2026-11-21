#!/usr/bin/env python3
"""Approved fixed-family test598. Full evidence; inherited contracts explicit."""
import hashlib, importlib.util, json
from pathlib import Path
from decimal import Decimal, Context, ROUND_CEILING, ROUND_FLOOR, ROUND_HALF_EVEN, localcontext
import numpy as np
BASE=Path(__file__).resolve().parent
ROOT=BASE.parent.parent
N,J,K,E,F=512,1024,65536,2044,1022
TARGET="Test whether the exact neutral raw0:1023 Galerkin predictor gives an unchanged-R comparison at least .000999 times the free Euclidean norm squared for every independent complex endpoint pair with free support2:1023."
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

try:
    names=['original-galerkin-586.npz','original-galerkin-586.json','original-minimum-audit-588.json','fixed-block-metric-audit-557.json','certificate-audit-534.json','complete-covariance-532.npz','residual-certificate-532.py','complete-schur-531.py','joint-galerkin-family-locator-598.npz','joint-galerkin-family-locator-598.py','fixed-block-metric-555.json']
    pins={name:sha(BASE/name) for name in names}
    orig=json.loads((BASE/'original-galerkin-586.json').read_text());audit=json.loads((BASE/'certificate-audit-534.json').read_text())
    check(pins['original-galerkin-586.npz']==orig['archive']['sha256'],'audited1024 square archive pin')
    for name in ['original-galerkin-586.json','original-minimum-audit-588.json','fixed-block-metric-audit-557.json','certificate-audit-534.json']:
        check(not json.loads((BASE/name).read_text())['failures'],'inherited failures empty '+name)
    for name in ['complete-covariance-532.npz','residual-certificate-532.py','complete-schur-531.py']:
        check(pins[name]==audit['original_sha256'][name],'audited reference/formula pin '+name)
    pi,ell=16*atan(5)-4*atan(239),I(3).ln()/2
    check((pi/ell).lo>Decimal('5.719') and (pi/ell).hi<Decimal('5.720') and pi.lo>Decimal('3.14159'),'rational constants for analytic bound')
    with np.load(BASE/'original-galerkin-586.npz') as q:M,T,Ts,U=[q[x].copy() for x in ['local_matrix','t_entries','ts_entries','u_entries']]
    with np.load(BASE/'joint-galerkin-family-locator-598.npz') as q:Z,ZT,A,B,Y,G,trial=[q[x].copy() for x in ['Z','ZT','A','B','Y','G','E']]
    check(np.array_equal(T,Ts.T),'full T orientations')
    check(all(np.isfinite(x).all() and np.abs(x).max()<400 for x in [M,T,Ts,U]),'all audited square entry magnitudes')
    # Rebuild every matrix relation. The saved solve is only a dyadic proposal.
    check(np.array_equal(ZT,Z),'joint endpoint coordinates equal entire neutral basis')
    ratios=[];dz=I(0);ratiosq=[I(0),I(0)]
    for n in range(2,J):
        r=(I('.25')+sq((n%2)*pi/ell))/(I('.25')+sq(n*pi/ell))
        if n%2==0:r*=I(2).sqrt()
        ratios.append(r.json());dz+=I(ab(r+I(Decimal(float(Z[n%2,n-2])))));ratiosq[n%2]+=sq(r)
    template=np.eye(J)[:,2:];template[:2]=Z[:2]
    check(np.array_equal(template,Z),'full neutral coordinate sparsity')
    check(dz.hi<Decimal('1e-14'),'all exact neutral ratios enclosed')
    zn=I('1.008');check((1+max(ratiosq,key=lambda x:x.hi)).sqrt().hi<zn.lo,'exact neutral basis norm<1.008')
    k2=[sq(n*pi/ell) for n in range(N,J)]
    dd=[(I(n)/(2*ell)).ln()-2*sq(ell)/(9*n*n) for n in range(N,J)]
    quarter=np.zeros(E)
    arrays['quarter_metric_upper']=quarter
    ea_raw=nf(response_error(np.arange(J),np.arange(J)))+I('1e-8')
    eta_a=ea_raw*sq(zn)+I('1e-6')
    eta_b=I(2).sqrt()*zn*zn*I(J)*I('1e-6')+I('2e-6')
    eta_u=sq(zn)*J*I('1e-6')+I('1e-6')
    # All uniform cross entry errors include their complete continuous suffixes.
    positive('galerkin_floor',A-.77*np.eye(F))
    floor=I('.77')-eta_a-I('1e-6');check(floor.lo>0,'exact finite Galerkin coercivity positive')
    positive('predictor_norm',1.4**2*np.eye(F)-Y@Y.T)
    yn=I('1.400001');gn=zn*yn
    check(nf(Y).hi<16 and nf(G).hi<16,'predictor Frobenius ledger<16')
    # Rebuild all finite data and pay each product by a uniform1e-6 ledger.
    aa=Z.T@M@Z;bb=Z.T@np.hstack((T@ZT,Ts@ZT));gg=Z@Y
    endpoint=np.block([[ZT.T@M@ZT,-ZT.T@U.T@ZT],[-ZT.T@U@ZT,ZT.T@M@ZT]])
    rebuilt=endpoint-bb.T@Y-Y.T@bb+Y.T@aa@Y
    check(nf(A-aa).hi<Decimal('1e-10') and nf(B-bb).hi<Decimal('1e-10') and nf(G-gg).hi<Decimal('1e-10') and nf(trial-rebuilt).hi<Decimal('1e-9'),'all complete family data rebuilt')
    check(nf(M).hi<1000 and nf(T).hi<100 and nf(U).hi<100,'matrix magnitude Frobenius ledger')
    rgal=nf(A@Y-B)+I('2e-6')+eta_b+eta_a*yn
    dy=rgal/floor
    trial_error=eta_a*(1+sq(yn))+2*eta_b*yn+eta_u+I('4e-5')+sq(rgal)/floor
    with np.load(BASE/'complete-covariance-532.npz') as q:
        H=q['m0']-.00024*np.eye(N)-(100/307)*(q['cov00']+.0046*np.eye(N))
    positive('reference_floor',H-.24*np.eye(N))
    rho=np.hstack((T@ZT,Ts@ZT))-M@G
    # Actual Dg on512:1023 occurs in M@G.
    sol=np.linalg.solve(H,rho[:N]);head=(rho[:N].T@sol+sol.T@rho[:N])/2
    head_solve=nf(rho[:N]-H@sol)+I('1e-8')*nf(sol)+I('1e-6')
    head_error=nf(rho[:N])*head_solve/I('.239999')+I('1e-6')
    check(head_error.hi<Decimal('1e-5'),'full rational head inverse error<1e-5')
    fixed=json.loads((BASE/'fixed-block-metric-555.json').read_text())
    lowers=fixed['middle']['diagonal_lower_endpoints']
    check(len(lowers)==K-N,'all audited reference weights present')
    weights=np.array([float(np.nextafter(float(2/Decimal(s)),np.inf)) for s in lowers])
    finite=rho[N:].T@(weights[:N,None]*rho[N:])
    trace_float=float(np.trace(head+finite))
    con=old.constants();el,pif=con['ell'],con['pi']
    indices=np.arange(K);k=indices*pif/el;nu=np.full(K,np.sqrt(2/el));nu[0]=1/np.sqrt(el)
    parity=np.where(indices%2==0,1.,-1.);im,_=old.psi_imag(k,pif);bpsi=k*im/2
    with localcontext() as c:
        c.prec=80;fourth=Decimal(3).sqrt().sqrt()
        decays=[float(Decimal(1)/(Decimal(3)**j*fourth)) for j in range(64)]
        cc=[float(Decimal(1)/(Decimal(3)**(6*j+1)*Decimal(3).sqrt())) for j in range(1,8)]
    def translation(rows,delta):
        kn,km=k[rows,None],k[None,:J];sn,_=old.sincos(k[rows]*delta,pif);sm,_=old.sincos(k[:J]*delta,pif)
        sig=parity[rows,None]*parity[None,:J]
        num=(-sig*kn*sn[:,None]+km*sm[None,:] if delta>0 else kn*sn[:,None]-sig*km*sm[None,:])
        return num/(kn*kn-km*km)*np.outer(nu[rows],nu[:J])
    blocks=[];eM2=0.;rawL2=0.;rhosq=0.;digest=hashlib.sha256();raw_max=0.
    # Error of ALL rows0:K for local M columns0:J.
    err_square=response_error(np.arange(J),np.arange(J));eM2=float(np.sum(err_square**2))
    for start in range(J,K,N):
        rows=slice(start,start+N);kn,km=k[rows,None],k[None,:J]
        response=(bpsi[rows,None]-bpsi[None,:J])/(kn*kn-km*km)
        for j in range(64):
            c=2*j+.5;response-=decays[j]*parity[rows,None]*c*c/((c*c+kn*kn)*(c*c+km*km))
        response*=2*np.outer(nu[rows],nu[:J])*(parity[rows,None]==parity[None,:J])
        tt,ts=np.zeros_like(response),np.zeros_like(response)
        for delta,w in zip(con['deltas'],con['weights']):tt+=w*translation(rows,delta);ts+=w*translation(rows,-delta)
        for j in range(1,8):
            c=2*j+.5;minus=nu*c*(1-parity*decays[j])/(c*c+k*k);plus=nu*c*(parity-decays[j])/(c*c+k*k)
            tt+=cc[j-1]*np.outer(minus[rows],plus[:J]);ts+=cc[j-1]*np.outer(plus[rows],minus[:J])
        rr=np.hstack((tt@ZT,ts@ZT))-response@G
        digest.update(rr.tobytes());weighted=np.sqrt(weights[start-N:start,None])*rr
        finite+=weighted.T@weighted
        rawL2+=float(np.sum(response**2));rhosq+=float(np.sum(weighted**2))
        er=response_error(np.arange(start,start+N),np.arange(J));eM2+=float(np.sum(er**2))
        mx=max(float(np.abs(x).max()) for x in [response,tt,ts]);raw_max=max(raw_max,mx)
        check(mx<400,'full rectangular entry magnitudes '+str(start))
        blocks.append(dict(first=start,last=start+N-1,max_entry=mx,weighted_residual_fro_squared=float(np.sum(weighted**2)),local_error_fro_squared=float(np.sum(er**2))))
        if start%8192==0:print('Completed family residual rows through',start+N-1,flush=True)
    ea_all=I(Decimal(float(np.sqrt(eM2))))*I('1.00000001')+I('1e-8')
    # Same rows0:511 entry error as a subset; global norm safely bounds it.
    dp=I(2).sqrt()*I(N*J).sqrt()*I('1e-6')*zn+ea_raw*gn+I('1e-6')
    dm=I(2).sqrt()*I((K-N)*J).sqrt()*I('1e-6')*zn+ea_all*gn+I('1e-6')
    deltafinite=(sq(dp)/I('.239999')+2*sq(dm)/I('6.14')).sqrt()
    finite_trace=I(Decimal(float(np.trace(head+finite))))+I('1e-4')
    finite_error=2*finite_trace.sqrt()*deltafinite+sq(deltafinite)+I('1e-4')
    # Uniform analytic entire tail; C999l boundary formula specialized to J.
    d=np.ones(J);d[0]=1/np.sqrt(2);ve=d*(indices[:J]%2==0);vo=d*(indices[:J]%2==1);vp=d;va=d*parity[:J]
    boundary=np.zeros((6,E));boundary[0,:F]=va@ZT;boundary[1,:F]=vp@ZT;boundary[2,F:]=vp@ZT;boundary[3,F:]=va@ZT
    boundary[4]=ve@G;boundary[5]=vo@G
    ap,am=I(0),I(0)
    for n,p in old.POWERS:
        wt=I(p).ln()/I(n).sqrt();dl=7*ell-I(n).ln();check(dl.lo>0 or dl.hi<0,'nonzero separation7 delay '+str(n))
        if dl.lo>0:ap+=wt
        else:am+=wt
    wb=4*ell*(1+I('1.5')/I(3).sqrt().sqrt())/sq(pi)
    tw=[2*ap/pi/I(K-1).sqrt(),2*am/pi/I(K-1).sqrt(),2*ap/pi/I(K-1).sqrt(),2*am/pi/I(K-1).sqrt(),I(2).sqrt()*(1+wb/K)/I(K-1).sqrt(),(1+wb/K)/I(K-1).sqrt()]
    wj=np.array([uf(x) for x in tw]);sumw=uf(sum(tw,I(0)))
    leading=sumw*(boundary.T@(wj[:,None]*boundary))
    m2=I(sum(n*n for n in range(1,J))).sqrt();m4=I(sum(n**4 for n in range(1,J))).sqrt()
    jr=(2/pi)/(1-I((J-1)**2)/(K*K))*(m4/(I(5).sqrt()*sq(I(K-1))*I(K-1).sqrt())+m2/(I(3).sqrt()*I(K-1)*I(K-1).sqrt()))
    sc=16*ell/sq(pi);sr=sum((sq(4*n+sc) for n in range(J)),I(0)).sqrt()/(I(3).sqrt()*I(K-1)*I(K-1).sqrt())
    kappa=1/(I(2187)*I(3).sqrt()*I('2.5')*(1-I(1)/729))
    trem=I(2).sqrt()*zn*((ap+am)*jr+kappa)+sr*gn
    dk=(I(K)/(2*ell)).ln()-2*sq(ell)/(9*K*K)
    tail=uf(2/dk)*(1.1*leading+uf(11*sq(trem))*np.eye(E))+1e-5*np.eye(E)
    cov=(head+finite+tail);cov=(cov+cov.T)/2+uf(finite_error)*np.eye(E)
    cov_bound=nf(cov)+I('1e-5')
    # Complete weighted LZ: head square from M; on all outputs>=1024, D=0.
    positive('local_operator_norm',100*np.eye(F)-(M@Z).T@(M@Z))
    mz=I('10.000001')+ea_raw*zn+I('1e-6')
    far_lz=(I(Decimal(float(np.sqrt(rawL2))))*I('1.00000001')+ea_all)*zn+I('1e-5')
    # Tail S columns: C744w's bound generalizes with max input J-1.
    # A direct coefficient-L1 bound is sufficient for this ERROR operator.
    Btail=4*ell*(1+I('1.5')/I(3).sqrt().sqrt())/sq(pi)
    sfar=I(J).sqrt()*(1+Btail/K)/I(K-1).sqrt()*zn
    # The head0:1023 estimate is uniformly weighted by the worst head weight;
    # extending it over512:1023 only enlarges it (H^-1<=1/.239999).
    wlz=(sq(mz)/I('.239999')+2/I('6.14')*(sq(far_lz)+sq(sfar))).sqrt()
    dg=wlz*dy
    exact_error=2*cov_bound.sqrt()*dg+sq(dg)
    comparison=(trial+trial.T)/2-cov-np.diag(quarter)-uf(trial_error+exact_error+I('1e-5'))*np.eye(E)
    comparison=(comparison+comparison.T)/2
    positive('quarter_comparison',comparison-.001*np.eye(E))
    arrays.update(Z=Z,ZT=ZT,A=A,B=B,Y=Y,G=G,trial=trial,head_residual=rho[:N],head_solution=sol,head_covariance=head,finite_covariance=finite,tail_boundary=boundary,tail_covariance_upper=tail,full_covariance_upper=cov,comparison_lower=comparison,local_error_radius_square=err_square)
    bounds.update(neutral_basis_norm=zn.json(),neutral_basis_conversion_L1=dz.json(),local_square_error_fro=ea_raw.json(),local_all_output_error_fro=ea_all.json(),eta_A=eta_a.json(),eta_B=eta_b.json(),eta_U=eta_u.json(),galerkin_floor=floor.json(),predictor_norm=yn.json(),equation_residual=rgal.json(),predictor_error=dy.json(),trial_error=trial_error.json(),head_inverse_matrix_error=head_error.json(),residual_head_error=dp.json(),residual_complement_error=dm.json(),weighted_residual_error=deltafinite.json(),finite_trace=finite_trace.json(),finite_covariance_error=finite_error.json(),prime_remainder=jr.json(),response_remainder=sr.json(),complete_tail_remainder=trem.json(),tail_diagonal_lower=dk.json(),full_covariance_operator_bound=cov_bound.json(),weighted_LZ_bound=wlz.json(),weighted_predictor_error=dg.json(),exact_predictor_covariance_error=exact_error.json())
    ledger.update(row_blocks=blocks,complete_residual_sha256=digest.hexdigest(),neutral_ratio_intervals=ratios,tail_weights=[x.json() for x in tw],raw_far_S_fro_squared=rawL2,diagnostic_comparison_minimum=float(np.linalg.eigvalsh(comparison)[0]),diagnostic_unpaid_center_minimum=float(np.linalg.eigvalsh((trial+trial.T)/2-head-finite)[0]))
except Exception as ex:
    failures.append(type(ex).__name__+': '+str(ex))
art=BASE/'joint-galerkin-family-certificate-598.npz';np.savez_compressed(art,**arrays)
check(all(sha(BASE/name)==val for name,val in pins.items()),'all inherited artifacts preserved')
passed=not failures
out=BASE/'joint-galerkin-family-certificate-598.json'
report=dict(target=TARGET,passed_under_inherited_contracts=passed,independently_audited=False,required='complete exact-Galerkin comparison >= .000999 Euclidean identity for every complex direction',result='PASS' if passed else 'INCONCLUSIVE',certified_absolute_surplus_if_all_checks_pass='.000999',bounds=bounds,ledger=ledger,checks=checks,failures=failures,input_hashes=pins,script_sha256=sha(Path(__file__)),archive=dict(path=str(art.relative_to(ROOT)),sha256=sha(art)),qualifications=['Inherited analytic-response and IEEE754/Decimal contracts','Whole-core and original c_star not independently replayed','Joint finite family only; no high endpoints, H2 or Xi sign','No library solve/eigenvalue/Cholesky success trusted without residuals'])
out.write_text(json.dumps(report,indent=2)+'\n')
print('Result',report['result'],'required full joint .000999 comparison; failures=',failures)
for name in ['local_square_error_fro','galerkin_floor','trial_error','finite_covariance_error','complete_tail_remainder','weighted_predictor_error','exact_predictor_covariance_error']:print(name,bounds.get(name))
print('Diagnostic comparison minimum',ledger.get('diagnostic_comparison_minimum'))
print('Full certificate',out.relative_to(ROOT),'arrays',art.relative_to(ROOT))
