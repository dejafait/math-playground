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

result='INCONCLUSIVE';stage='startup';proposal_path=BASE/'residual-stationary-fixed-trial-proposal-603.npz'
try:
    names=['original-galerkin-586.npz','original-galerkin-586.json',
           'original-minimum-audit-588.json','fixed-block-metric-audit-557.json',
           'certificate-audit-534.json','complete-covariance-532.npz',
           'fixed-block-metric-555.json','residual-certificate-532.py','complete-schur-531.py',
           'joint-galerkin-family-ledger-598.json',
           'joint-galerkin-family-certificate-598.json','joint-galerkin-family-certificate-598.npz']
    pins={name:sha(BASE/name) for name in names}
    orig=json.loads((BASE/'original-galerkin-586.json').read_text())
    aud=json.loads((BASE/'certificate-audit-534.json').read_text())
    require(pins['original-galerkin-586.npz']==orig['archive']['sha256'],'audited square archive pin')
    for name in ['original-galerkin-586.json','original-minimum-audit-588.json',
                 'fixed-block-metric-audit-557.json','certificate-audit-534.json','joint-galerkin-family-ledger-598.json']:
        require(not json.loads((BASE/name).read_text())['failures'],'inherited no failures '+name)
    for name in ['complete-covariance-532.npz','residual-certificate-532.py','complete-schur-531.py']:
        require(pins[name]==aud['original_sha256'][name],'audited formula/reference pin '+name)
    require(not proposal_path.exists(),'single proposal path unused at invocation')
    pi,ell=16*atan(5)-4*atan(239),I(3).ln()/2
    require((pi/ell).lo>Decimal('5.719') and (pi/ell).hi<Decimal('5.720') and pi.lo>Decimal('3.14159'),'rational response constants')
    with np.load(BASE/'original-galerkin-586.npz') as q:
        M,T,Ts,U,Z=[q[n].copy() for n in ['local_matrix','t_entries','ts_entries','u_entries','neutral_coordinate_center']]
    require(np.array_equal(T,Ts.T) and np.array_equal(M,M.T),'both forcing orientations and symmetric local center')
    require(all(np.isfinite(v).all() and np.abs(v).max()<400 for v in [M,T,Ts,U]),'audited square magnitudes')
    ratios=[];dz=I(0);rs=[I(0),I(0)]
    for n in range(2,J):
        r=(I('.25')+sq((n%2)*pi/ell))/(I('.25')+sq(n*pi/ell))
        if n%2==0:r*=I(2).sqrt()
        ratios.append(r.json());dz+=I(ab(r+I(Decimal(float(Z[n%2,n-2])))));rs[n%2]+=sq(r)
    template=np.eye(J)[:,2:];template[:2]=Z[:2]
    require(np.array_equal(template,Z),'all neutral coordinate positions')
    require(dz.hi<Decimal('1e-14'),'all exact neutral ratios enclosed')
    zn=I('1.008');require((1+max(rs,key=lambda v:v.hi)).sqrt().hi<zn.lo,'exact neutral basis norm')
    ledger['neutral_ratio_intervals']=ratios
    with np.load(BASE/'complete-covariance-532.npz') as q:
        H=q['m0']-.00024*np.eye(N)-(100/307)*(q['cov00']+.0046*np.eye(N))
    require(positive('reference_floor',H-.24*np.eye(N)),'reference head positive factor')
    wh=np.linalg.solve(H,np.eye(N));wh=(wh+wh.T)/2
    fixed=json.loads((BASE/'fixed-block-metric-555.json').read_text())
    lows=fixed['middle']['diagonal_lower_endpoints']
    require(len(lows)==K-N,'every reference diagonal lower endpoint')
    weights=np.array([np.nextafter(float(iv.UP.divide(Decimal(2),Decimal(s))),np.inf) for s in lows])
    # Candidate selection only: no equation solution/enclosure is used as a theorem.
    stage='one finite stationary proposal';aa=Z.T@M@Z
    bb=Z.T@np.hstack((T@Z,Ts@Z));vv=np.zeros((F,F));vp=np.zeros((F,E))
    raw_digest=hashlib.sha256();selection_blocks=[]
    for start,m,t,ts in raw_blocks(M,T,Ts):
        for a in [m,t,ts]:raw_digest.update(a.tobytes())
        v=m@Z;p=np.hstack((t@Z,ts@Z))
        if start==0:
            wv=np.vstack((wh@v[:N],weights[:N,None]*v[N:]))
            wp=np.vstack((wh@p[:N],weights[:N,None]*p[N:]))
        else:
            w=weights[start-N:start];wv=w[:,None]*v;wp=w[:,None]*p
        vv+=v.T@wv;vp+=v.T@wp
        selection_blocks.append([start,start+m.shape[0]-1])
        if start%8192==0:print('Selection rows through',start+m.shape[0]-1,flush=True)
    cc=aa-(vv+vv.T)/2;dd=bb-vp
    Y=np.linalg.solve(cc,dd)  # exactly one solve, no regularization/pseudoinverse
    require(np.isfinite(Y).all(),'finite stationary proposal returned')
    np.savez_compressed(proposal_path,Y=Y,Z_center=Z,head_weight_center=wh,
                        C_center=cc,D_center=dd,VWV_center=vv,VWP_center=vp,
                        weights=weights,selection_blocks=np.array(selection_blocks))
    ledger['proposal']=dict(path=str(proposal_path.relative_to(ROOT)),sha256=sha(proposal_path),
        raw_row_sha256=raw_digest.hexdigest(),stationary_residual_diagnostic=float(np.linalg.norm(cc@Y-dd)),
        rule='returned free binary64 entries are exact dyadics; one save; no equation accuracy assumed')
    print('Saved single dyadic proposal',proposal_path.name,'Fro norm',np.linalg.norm(Y),flush=True)
    # Independent fixed-witness verification; no unknown Galerkin correction.
    stage='fixed trial norms and energy';G=Z@Y
    require(nf(Y).hi<16 and nf(G).hi<16,'new free/raw predictor Frobenius norms <16')
    yfloat=float(np.ceil(np.sqrt(np.linalg.eigvalsh(Y@Y.T)[-1])*10000)/10000+.0001)
    require(positive('predictor_norm',yfloat*yfloat*np.eye(F)-Y@Y.T),'new predictor norm full factor')
    yn=I(Decimal(yfloat))+I('1e-6');gn=zn*yn
    require(nf(M).hi<1000 and nf(T).hi<100 and nf(Ts).hi<100 and nf(U).hi<100,'new matrix arithmetic magnitude ledger')
    ea_raw=nf(response_error(np.arange(J),np.arange(J)))+I('1e-8')
    eta_a=ea_raw*sq(zn)+I('1e-6')
    eta_b=I(2).sqrt()*sq(zn)*J*I('1e-6')+I('2e-6')
    eta_u=sq(zn)*J*I('1e-6')+I('1e-6')
    endpoint=np.block([[aa,-Z.T@U.T@Z],[-Z.T@U@Z,aa]])
    trial=endpoint-bb.T@Y-Y.T@bb+Y.T@aa@Y
    trial_error=eta_a*(1+sq(yn))+2*eta_b*yn+eta_u+I('4e-5')
    rho=np.hstack((T@Z,Ts@Z))-M@G
    sol=np.linalg.solve(H,rho[:N]);head=(rho[:N].T@sol+sol.T@rho[:N])/2
    head_solve=nf(rho[:N]-H@sol)+I('1e-8')*nf(sol)+I('1e-6')
    head_error=nf(rho[:N])*head_solve/I('.239999')+I('1e-6')
    require(head_error.hi<Decimal('1e-5'),'new rational head inverse matrix/nuclear error<1e-5')
    finite=rho[N:].T@(weights[:N,None]*rho[N:]);blocks=[]
    eM2=float(np.sum(response_error(np.arange(J),np.arange(J))**2))
    digest=hashlib.sha256();stage='all finite residual outputs'
    for start,m,t,ts in raw_blocks(M,T,Ts):
        for a in [m,t,ts]:digest.update(a.tobytes())
        if start==0:continue
        rr=np.hstack((t@Z,ts@Z))-m@G
        weighted=np.sqrt(weights[start-N:start,None])*rr
        finite+=weighted.T@weighted
        er=response_error(np.arange(start,start+N),np.arange(J));eM2+=float(np.sum(er**2))
        mx=max(float(np.abs(a).max()) for a in [m,t,ts])
        require(mx<400,'complete rectangular magnitude '+str(start))
        blocks.append(dict(first=start,last=start+N-1,max_entry=mx,
                           weighted_residual_fro_squared=float(np.sum(weighted**2))))
        if start%8192==0:print('Verification residual rows through',start+N-1,flush=True)
    require(digest.hexdigest()==raw_digest.hexdigest(),'both passes identical all raw finite outputs')
    ea_all=I(Decimal(float(np.sqrt(eM2))))*I('1.00000001')+I('1e-8')
    dp=I(2).sqrt()*I(N*J).sqrt()*I('1e-6')*zn+ea_raw*gn+I('1e-6')
    dm=I(2).sqrt()*I((K-N)*J).sqrt()*I('1e-6')*zn+ea_all*gn+I('1e-6')
    deltafinite=(sq(dp)/I('.239999')+2*sq(dm)/I('6.14')).sqrt()
    finite_trace=I(Decimal(float(np.trace(head+finite))))+I('1e-4')
    finite_error=2*finite_trace.sqrt()*deltafinite+sq(deltafinite)+I('1e-4')
    # Six maps and entire suffix; C999q Section5 with this saved Y and its norm.
    stage='entire infinite output';idx=np.arange(J);d=np.ones(J);d[0]=1/np.sqrt(2)
    vp0=d;va=d*np.where(idx%2==0,1.,-1.);ve=d*(idx%2==0);vo=d*(idx%2==1)
    boundary=np.zeros((6,E));boundary[0,:F]=va@Z;boundary[1,:F]=vp0@Z
    boundary[2,F:]=vp0@Z;boundary[3,F:]=va@Z;boundary[4]=ve@G;boundary[5]=vo@G
    require(nf(boundary).hi<100,'new complete boundary map magnitude ledger')
    ap,am=I(0),I(0)
    for n,p in old.POWERS:
        wt=I(p).ln()/I(n).sqrt();dl=7*ell-I(n).ln()
        require(dl.lo>0 or dl.hi<0,'all nonzero separation7 delay signs '+str(n))
        if dl.lo>0:ap+=wt
        else:am+=wt
    wb=4*ell*(1+I('1.5')/I(3).sqrt().sqrt())/sq(pi)
    tw=[2*ap/pi/I(K-1).sqrt(),2*am/pi/I(K-1).sqrt(),2*ap/pi/I(K-1).sqrt(),2*am/pi/I(K-1).sqrt(),
        I(2).sqrt()*(1+wb/K)/I(K-1).sqrt(),(1+wb/K)/I(K-1).sqrt()]
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
    comparison=(trial+trial.T)/2-cov-uf(trial_error+I('1e-5'))*np.eye(E)
    comparison=(comparison+comparison.T)/2
    stage='final full matrix factor';ok=positive('joint_comparison',comparison-.001*np.eye(E))
    result='PASS_PENDING_CRITICAL_AUDIT' if ok and not failures else 'SUFFICIENT_LOWER_CERTIFICATE_FAILED'
    # A diagnostic may guide a separately assessed continuation; it is not a sign proof.
    ev,vec=np.linalg.eigh(comparison-.000999*np.eye(E))
    direction=vec[:,0];ray=float(direction@((comparison-.000999*np.eye(E))@direction))
    ray_error=I('5e-13')*(nf(comparison)+1)*sq(nf(direction))+I('1e-7')
    lower_ray=I(Decimal(ray))+I(-ray_error.hi,ray_error.hi)
    arrays.update(Y=Y,Z_center=Z,G_center=G,trial_center=trial,head_residual=rho[:N],head_solution=sol,
                  head_covariance=head,finite_covariance=finite,tail_boundary=boundary,
                  tail_covariance_upper=tail,full_covariance_upper=cov,comparison_lower=comparison,
                  shifted_lower_direction=direction)
    bounds.update(neutral_basis_norm=zn.json(),neutral_basis_conversion_L1=dz.json(),
                  predictor_norm=yn.json(),free_predictor_fro=nf(Y).json(),raw_predictor_fro=nf(G).json(),
                  local_square_error_fro=ea_raw.json(),local_all_output_error_fro=ea_all.json(),
                  eta_A=eta_a.json(),eta_B=eta_b.json(),eta_U=eta_u.json(),trial_error=trial_error.json(),
                  head_inverse_matrix_error=head_error.json(),residual_head_error=dp.json(),
                  residual_complement_error=dm.json(),weighted_residual_error=deltafinite.json(),
                  finite_trace=finite_trace.json(),finite_covariance_error=finite_error.json(),
                  prime_remainder=jr.json(),response_remainder=sr.json(),complete_tail_remainder=trem.json(),
                  tail_diagonal_lower=dk.json(),lower_certificate_shifted_rayleigh=lower_ray.json())
    ledger.update(row_blocks=blocks,complete_raw_row_sha256=digest.hexdigest(),tail_weights=[w.json() for w in tw],
                  diagnostic_unpaid_center_minimum=float(np.linalg.eigvalsh((trial+trial.T)/2-head-finite)[0]),
                  diagnostic_comparison_minimum=float(ev[0]+.000999),
                  every_finite_and_infinite_output_in_lower_certificate=True)
except Exception as ex:
    failures.append(type(ex).__name__+': '+str(ex))
    ledger['exception_stage']=stage
archive=BASE/'residual-stationary-fixed-trial-603.npz';np.savez_compressed(archive,**arrays)
check(all(sha(BASE/name)==val for name,val in pins.items()),'all inherited inputs preserved')
out=BASE/'residual-stationary-fixed-trial-603.json'
report=dict(target=TARGET,result=result,actual_target_sign='UNDECIDED',independently_audited=False,
            bounds=bounds,ledger=ledger,checks=checks,failures=failures,input_hashes=pins,
            script_sha256=sha(Path(__file__)),archive=dict(path=str(archive.relative_to(ROOT)),sha256=sha(archive)),
            required='.000999 uniform free Euclidean floor for all2044 complex endpoints',
            qualifications=['Inherited analytic-response and IEEE754/Decimal contracts',
                            'Whole-neutral-core and original c_star not independently replayed',
                            'One fixed dyadic proposal only; no optimizer assertion',
                            'Failed sufficient lower certificate is not an actual violating direction'])
out.write_text(json.dumps(report,indent=2)+'\n')
print('Result',result,'actual target UNDECIDED; failures',failures,flush=True)
for n in ['predictor_norm','trial_error','finite_covariance_error','complete_tail_remainder','lower_certificate_shifted_rayleigh']:
    print(n,bounds.get(n),flush=True)
print('Required full joint floor .000999; full certificate',out.relative_to(ROOT),'arrays',archive.relative_to(ROOT),flush=True)
