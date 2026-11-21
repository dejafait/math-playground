#!/usr/bin/env python3
"""Unchanged C999q conceptual audit: complete artifacts and independent bounds.

110-place integer outward scalars, all-entry directed binary64 radii,
full factor/assembly checks. Analytic/IEEE754/Decimal/core contracts remain.
"""
import hashlib
import importlib.util
import json
import math
from decimal import Decimal, localcontext
from fractions import Fraction as Fr
from pathlib import Path
import numpy as np
BASE=Path(__file__).resolve().parent
N,J,K,F,E=512,1024,65536,1022,1024

def load(name,path):
    s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
helper=load('helper557audit596',BASE/'fixed-block-metric-audit-557.py')
Q,SCALE=helper.Q,helper.SCALE
sq,ln=helper.sq,helper.ln
checks=[];failures=[];evidence={}
def check(ok,label):
    checks.append(dict(label=label,passed=bool(ok)))
    if not ok:failures.append(label)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def exact(x):return Q(Fr(float(x)))
def fro(x):return exact(np.linalg.norm(x))*Q('1.000000001')+Q('1e-100')
def gamma(n):
    t=Q(Fr(n,2**53));return t/(1-t)
def enclosed(x,s,label):
    check(Fr(s['lo'])<=Fr(x.lo,SCALE)<=Fr(x.hi,SCALE)<=Fr(s['hi']),label)
def cap(x,s,label):check(0<=x.lo<=x.hi<Q(s).lo,label)
def bound(name,x,threshold):
    cap(x,threshold,'independent bound '+name)
    evidence.setdefault('bounds',{})[name]=dict(value=x.json(),required_less_than=threshold)
def uf(x):
    v=np.nextafter(float(Fr(x.hi,SCALE)),np.inf)
    check(Fr(float(v))>=Fr(x.hi,SCALE),'upward scalar conversion')
    return v

def main():
    original=json.loads((BASE/'tail-galerkin-family-certificate-594.json').read_text())
    replay=json.loads((BASE/'tail-galerkin-family-replay-596.json').read_text())
    names=set(original['input_hashes'])|{'tail-galerkin-family-certificate-594.'+e for e in ('py','json','npz')}|{'fixed-trial-residual-audit-552.py','fixed-block-metric-audit-557.py'}
    pins={n:sha(BASE/n) for n in names}
    check(original['script_sha256']==pins['tail-galerkin-family-certificate-594.py'],'original generator hash')
    check(original['archive']['sha256']==pins['tail-galerkin-family-certificate-594.npz'],'original full archive hash')
    for n,h in original['input_hashes'].items():check(pins[n]==h,'original input pin '+n)
    for r,label in [(original,'original'),(replay,'100-digit replay')]:
        check(not r['failures'] and all(x['passed'] for x in r['checks']),label+' all checks and failures')
    with np.load(BASE/'tail-galerkin-family-certificate-594.npz') as f:ar={k:f[k].copy() for k in f.files}
    with np.load(BASE/'tail-galerkin-family-replay-596.npz') as f:
        check(set(f.files)==set(ar),'all replay arrays covered')
        for k,v in ar.items():check(np.isfinite(v).all() and np.array_equal(v,f[k]),'entire array replay '+k)
    check(original['ledger']['complete_residual_sha256']==replay['ledger']['complete_residual_sha256'],'all higher residual row bytes replay')
    blocks=original['ledger']['row_blocks']
    check([(x['first'],x['last']) for x in blocks]==[(n,n+N-1) for n in range(J,K,N)],'126 higher blocks partition1024:65535')
    check(blocks==replay['ledger']['row_blocks'],'all complete row ledgers replay')
    check(all(x['max_entry']<400 for x in blocks),'all higher entries within magnitude ledger')
    with np.load(BASE/'original-galerkin-586.npz') as f:M,T,Ts,U=[f[k].copy() for k in ('local_matrix','t_entries','ts_entries','u_entries')]
    with np.load(BASE/'complete-covariance-532.npz') as f:m0,cov00=[f[k].copy() for k in ('m0','cov00')]
    H=m0-.00024*np.eye(N)-(100/307)*(cov00+.0046*np.eye(N))
    Z,ZT,A,B,Y,G=[ar[k] for k in ('Z','ZT','A','B','Y','G')]
    check(Z.shape==(J,F) and ZT.shape==(J,N) and Y.shape==(F,E),'fixed dimensions')
    check(np.array_equal(T,Ts.T),'both full forcing orientations')
    check(np.array_equal(ZT,Z[:,510:]),'exact saved band coordinate subset')
    template=np.eye(J)[:,2:];template[:2]=Z[:2]
    check(np.array_equal(template,Z),'all neutral coordinate sparsity')

    half=Q(Fr(1,2));ell=sum((half**(2*j+1)/(2*j+1) for j in range(200)),Q())
    ell+=Q.ends(0,(half**401/(401*(1-half*half))).hi)
    pi=16*helper.arith.atan(5)-4*helper.arith.atan(239)
    check((pi/ell).lo>Q('5.719').hi and (pi/ell).hi<Q('5.720').lo and pi.lo>Q('3.14159').hi and Q(2).sqrt().hi<Q('1.415').lo,'independent rational constants')
    conv=Q();rsq=[Q(),Q()]
    for n in range(2,J):
        p=n%2;r=(Q('.25')+sq(p*pi/ell))/(Q('.25')+sq(n*pi/ell))
        if p==0:r*=Q(2).sqrt()
        enclosed(r,original['ledger']['neutral_ratio_intervals'][n-2],'neutral ratio '+str(n))
        conv+=(r+exact(Z[p,n-2])).ab();rsq[p]+=sq(r)
    bound('basis_conversion',conv,'1e-14')
    zn=Q('1.008');yn=Q('.610001')
    cap((1+Q.ends(max(x.lo for x in rsq),max(x.hi for x in rsq))).sqrt(),'1.008','full neutral basis operator norm')
    old=load('entries532audit596',BASE/'residual-certificate-532.py')
    powers=[]
    for p in range(2,81):
        if all(p%d for d in range(2,math.isqrt(p)+1)):
            n=p
            while n<81:
                if n>27:powers.append((n,p))
                n*=p
    powers.sort();check(powers==old.POWERS,'complete16 separation7 prime powers')
    ap,am=Q(),Q()
    for n,p in powers:
        dl=7*ell-ln(Q(n));w=ln(Q(p))/Q(n).sqrt()
        check(dl.lo>0 or dl.hi<0,'strict shift sign '+str(n))
        if dl.lo>0:ap+=w
        else:am+=w
    # Every denominator and upward inverse weight; quarter upper has 2 copies.
    fixed=json.loads((BASE/'fixed-block-metric-555.json').read_text())
    lowers=fixed['middle']['diagonal_lower_endpoints'];check(len(lowers)==K-N,'all65024 denominators')
    weights=[]
    for n,s in enumerate(lowers,N):
        dn=ln(n/(2*ell))-2*sq(ell)/(9*n*n)
        check(Q(s).hi<=dn.lo and Q(s).lo>Q('6.14').hi,'positive diagonal lower '+str(n))
        w=float(np.nextafter(float(2/Decimal(s)),np.inf));weights.append(w)
        check(Fr(w)>=2/Fr(s),'upward inverse weight '+str(n))
        if n<J:
            for idx in (n-N,n):check(Fr(float(ar['quarter_metric_upper'][idx]))>=Fr(dn.hi,4*SCALE),'quarter upper '+str(idx))
    weights=np.asarray(weights)

    # All-entry radius audit. Outward +/- nextafter implements directed
    # binary64 arithmetic for these positive rational expressions.
    up=lambda x:np.nextafter(x,np.inf)
    down=lambda x:np.nextafter(x,-np.inf)
    cols=np.arange(J,dtype=float)
    def q_up(ns):
        a=down(down(down(5.719)*ns)/2)
        denom=down(6*down(64.25**2+down(a*a)))
        return up(up(1.415)/denom)
    qm=q_up(cols)
    def radii(rows):
        nn=np.asarray(rows,dtype=float);den=np.abs(nn[:,None]**2-cols[None,:]**2)
        equal=den==0;den[equal]=1
        # Replica of exact source center radius (it includes1e-12 evaluation slack).
        rn=1.415/(6*(64.25**2+(5.719*nn/2)**2));rm=1.415/(6*(64.25**2+(5.719*cols/2)**2))
        rad=(2/3.14159)*(nn[:,None]*rn[:,None]+cols[None,:]*rm[None,:])/den
        parity=(nn[:,None]-cols[None,:])%2==0;rad*=parity
        # Independent outward upper on the rational analytic expression.
        numerator=up(up(nn[:,None]*q_up(nn)[:,None])+up(cols[None,:]*qm[None,:]))
        upper=up(up(up(2/down(3.14159))*numerator)/den);upper*=parity
        c=Q('131072.5')
        for r,k in zip(*np.where(equal)):
            n=int(nn[r]);cc=131072.5
            rad[r,k]=rn[r]+8*(cc**-2+2*(5.720*n)**2*(1/(6*cc**3)+cc**-4))
            qu=Q('1.415')/(6*(Q('64.25')**2+(Q('5.719')*n/2)**2))
            diag=qu+8*(1/c**2+2*(Q('5.720')*n)**2*(1/(6*c**3)+1/c**4))
            upper[r,k]=np.nextafter(float(Fr(diag.hi,SCALE)),np.inf)
        rad+=1e-7+1e-12
        required=up(upper+up(1e-7))
        check(np.all(rad>=required),'every rational radius encloses entry '+str(int(nn[0])))
        return rad,float(np.min(rad-required))
    sumsq=0.;minslack=math.inf;radiusrecords=[]
    for start in range(0,K,N):
        rad,slack=radii(np.arange(start,start+N));minslack=min(minslack,slack)
        ss=float(np.sum(rad*rad));sumsq+=ss
        if start<J:check(np.array_equal(rad,ar['local_error_radius_square'][start:start+N]),'all saved square radii '+str(start))
        else:check(ss==blocks[(start-J)//N]['local_error_fro_squared'],'entire rectangle radius sum '+str(start))
        radiusrecords.append(dict(first=start,last=start+N-1,squared_sum=ss,minimum_outward_slack=slack))
    # At most2^26 nonnegative summands; 1e-8 inflation covers sums/products/sqrt.
    check(gamma(K*J+10).hi<Q('1e-8').lo,'full radius norm inflation dominates sequential arithmetic')
    eall=exact(np.sqrt(sumsq))*Q('1.000000008')+Q('1e-10')
    esq=fro(ar['local_error_radius_square'])+Q('1e-10')
    check(eall.hi<=Q(original['bounds']['local_all_output_error_fro']['hi']).lo,'complete rectangle radius norm below reported bound')
    check(esq.hi<=Q(original['bounds']['local_square_error_fro']['hi']).lo,'complete square radius norm below reported bound')
    ea=Q(original['bounds']['local_square_error_fro']['hi']);eaall=Q(original['bounds']['local_all_output_error_fro']['hi'])
    evidence['radius_blocks']=radiusrecords
    evidence['radius_total']=dict(entries=K*J,minimum_outward_slack=minslack,square_upper=esq.json(),rectangle_upper=eall.json())
    print('All67108864 entry radii,1022 ratios and65024 weights checked.',flush=True)

    # Complete matrix rebuild and every original factor (no solver trust).
    aa=Z.T@M@Z;bb=Z.T@np.hstack((T@ZT,Ts@ZT));gg=Z@Y
    endpoint=np.block([[ZT.T@M@ZT,-ZT.T@U.T@ZT],[-ZT.T@U@ZT,ZT.T@M@ZT]])
    rebuilt=endpoint-bb.T@Y-Y.T@bb+Y.T@aa@Y
    for label,x in [('A',A-aa),('B',B-bb),('G',G-gg),('trial',ar['trial']-rebuilt)]:cap(fro(x),'1e-9','full rebuild '+label)
    rho=np.hstack((T@ZT,Ts@ZT))-M@G
    check(np.array_equal(rho[:N],ar['head_residual']),'complete head residual with actual Dg')
    firstgram=rho[N:].T@(weights[:N,None]*rho[N:])
    lowertrace=exact(np.trace(firstgram))+sum((exact(b['weighted_residual_fro_squared']) for b in blocks),Q())
    check(abs(float(np.trace(ar['finite_covariance']))-float(Fr(lowertrace.hi,SCALE)))<1e-10,'initial512:1023 plus126 blocks full trace')
    targets=dict(galerkin_floor=A-.77*np.eye(F),predictor_norm=.61**2*np.eye(F)-Y@Y.T,reference_floor=H-.24*np.eye(N),local_operator_norm=100*np.eye(F)-(M@Z).T@(M@Z),quarter_comparison=ar['comparison_lower']-.001*np.eye(E))
    factor_evidence={}
    for name,target in targets.items():
        fac=ar['factor_'+name];rr=fro(target-fac@fac.T);ff2=sq(fro(fac))
        cap(ff2,'100000','full factor magnitude '+name);check(np.max(np.abs(target))<1000,'matrix magnitude '+name)
        err=rr+gamma(2048)*Q(100000)+Q('2e-7')
        cap(err,'1e-6','independent full factor reconstruction '+name)
        factor_evidence[name]=dict(observed_upper=rr.json(),total_upper=err.json(),required='1e-6')
    evidence['factors']=factor_evidence
    eta_a=sq(zn)*ea+Q('1e-6');eta_b=Q(2).sqrt()*sq(zn)*J*Q('1e-6')+Q('1e-6');eta_u=sq(zn)*J*Q('1e-6')+Q('1e-6')
    floor=Q('.77')-eta_a-Q('1e-6');check(floor.lo>Q('.769697497').hi,'positive finite floor only')
    rgal=fro(A@Y-B)+Q('1e-6')+eta_b+eta_a*yn;dy=rgal/floor
    trialerr=eta_a*(1+sq(yn))+2*eta_b*yn+eta_u+Q('1e-5')+sq(rgal)/floor
    for name,x,c in [('eta_A',eta_a,'.000301503'),('eta_B',eta_b,'.001472418'),('eta_U',eta_u,'.001041450'),('equation_residual',rgal,'.001657335'),('predictor_error',dy,'.002153229'),('trial_error',trialerr,'.003265064')]:bound(name,x,c)
    sol=ar['head_solution'];rh=ar['head_residual'];hs=fro(rh-H@sol)+Q('1e-8')*fro(sol)+Q('1e-6')
    he=fro(rh)*hs/Q('.239999')+Q('1e-6');bound('head_action_nuclear_error',he,'1e-5')
    rebuilt_head=(rh.T@sol+sol.T@rh)/2
    check(np.array_equal(rebuilt_head,ar['head_covariance']),'entire symmetric head action')
    dp=Q(2*N*J).sqrt()*Q('1e-6')*zn+ea*zn*yn+Q('1e-6')
    dm=Q(2*(K-N)*J).sqrt()*Q('1e-6')*zn+eaall*zn*yn+Q('1e-6')
    df=(sq(dp)/Q('.239999')+2*sq(dm)/Q('6.14')).sqrt()
    trace=exact(np.trace(ar['head_covariance']+ar['finite_covariance']))+Q('1e-4')
    ef=2*trace.sqrt()*df+sq(df)+Q('1e-4')
    for name,x,c in [('head_residual_error',dp,'.001215045'),('complement_residual_error',dm,'.012165043'),('weighted_residual_error',df,'.007372656'),('finite_trace',trace,'2.711084442'),('finite_covariance_error',ef,'.024433060')]:bound(name,x,c)
    wb=4*ell*(1+Q('1.5')/Q(3).sqrt().sqrt())/sq(pi)
    jr=(2/pi)/(1-Q((J-1)**2)/(K*K))*(Q(sum(n**4 for n in range(1,J))).sqrt()/Q(5*(K-1)**5).sqrt()+Q(sum(n*n for n in range(1,J))).sqrt()/Q(3*(K-1)**3).sqrt())
    sr=sum((sq(4*n+16*ell/sq(pi)) for n in range(J)),Q()).sqrt()/Q(3*(K-1)**3).sqrt()
    kap=1/(2187*Q(3).sqrt()*Q('2.5')*(1-Q(1)/729))
    trem=Q(2).sqrt()*zn*((ap+am)*jr+kap)+sr*zn*yn
    dk=ln(K/(2*ell))-2*sq(ell)/(9*K*K)
    tw=[2*ap/pi/Q(K-1).sqrt(),2*am/pi/Q(K-1).sqrt()]*2+[Q(2).sqrt()*(1+wb/K)/Q(K-1).sqrt(),(1+wb/K)/Q(K-1).sqrt()]
    for k,x in enumerate(tw):enclosed(x,original['ledger']['tail_weights'][k],'entire tail weight '+str(k))
    d=np.ones(J);d[0]=1/np.sqrt(2);par=np.where(np.arange(J)%2==0,1.,-1.)
    boundary=np.zeros((6,E));boundary[0,:N]=(d*par)@ZT;boundary[1,:N]=d@ZT;boundary[2,N:]=d@ZT;boundary[3,N:]=(d*par)@ZT
    boundary[4]=(d*(np.arange(J)%2==0))@G;boundary[5]=(d*(np.arange(J)%2==1))@G
    check(np.array_equal(boundary,ar['tail_boundary']),'all six entire boundary functionals')
    wj=np.asarray([uf(w) for w in tw]);leading=uf(sum(tw,Q()))*(boundary.T@(wj[:,None]*boundary))
    tail=uf(2/dk)*(1.1*leading+uf(11*sq(trem))*np.eye(E))+1e-5*np.eye(E)
    cap(fro(tail-ar['tail_covariance_upper']),'1e-12','entire tail matrix rebuild')
    cov=ar['head_covariance']+ar['finite_covariance']+ar['tail_covariance_upper'];cov=(cov+cov.T)/2+uf(ef)*np.eye(E)
    cap(fro(cov-ar['full_covariance_upper']),'1e-12','entire covariance assembly')
    ctilde=fro(ar['full_covariance_upper'])+Q('1e-5')
    mz=Q('10.000001')+ea*zn+Q('1e-6')
    mid=Q(original['ledger']['raw_far_S_fro_squared']).sqrt()*Q('1.00000001')*zn+eaall*zn+Q('1e-5')
    sf=Q(J).sqrt()*(1+wb/K)/Q(K-1).sqrt()*zn
    lz=(sq(mz)/Q('.239999')+2*(sq(mid)+sq(sf))/Q('6.14')).sqrt()
    dg=lz*dy;eg=2*ctilde.sqrt()*dg+sq(dg)
    for name,x,c in [('prime_remainder',jr,'.000418155'),('response_remainder',sr,'.002603168'),('tail_remainder',trem,'.006313785'),('full_covariance_norm',ctilde,'1.670760971'),('weighted_LZ',lz,'20.415951150'),('weighted_predictor_error',dg,'.043960215'),('exact_predictor_covariance_error',eg,'.115576619')]:bound(name,x,c)
    check(dk.lo>Q('10.9963070613268').hi,'entire increasing tail diagonal')
    # Use the original (slightly larger) scalar endpoints to rebuild its exact
    # saved comparison. Independent values above satisfy the stated caps.
    ob=original['bounds']
    for name,x in [('trial_error',trialerr),('finite_covariance_error',ef),('exact_predictor_covariance_error',eg)]:
        check(Fr(x.hi,SCALE)<=Fr(ob[name]['hi'])+Fr('1e-14'),'scalar agreement within final assembly slack '+name)
    debt=Q(ob['trial_error']['hi'])+Q(ob['exact_predictor_covariance_error']['hi'])+Q('1e-5')
    comparison=(ar['trial']+ar['trial'].T)/2-ar['full_covariance_upper']-np.diag(ar['quarter_metric_upper'])-uf(debt)*np.eye(E)
    comparison=(comparison+comparison.T)/2
    cap(fro(comparison-ar['comparison_lower']),'1e-12','complete final quarter comparison rebuild')

    # Explicit arithmetic budgets independent of factor library correctness.
    for name,x,c in [('Z',Z,32),('ZT',ZT,23),('Y',Y,8),('G',G,8),('M',M,1000),('T',T,100),('Ts',Ts,100),('U',U,100),('A',A,200),('B',B,50),('head_rhs',rh,1),('head_solution',sol,1),('boundary',boundary,100),('m0',m0,400),('cov00',cov00,1)]:cap(fro(x),str(c),'full norm ledger '+name)
    scalarS=(2*ell+2*pi)/(1-Q(Fr(3,4))) # lower bound d_a>.24 verified below, use .24 instead
    # 3^(-1/4)<.76 => d_a>.24 and (2ell+2pi)/.24<31<60.
    check((1/Q(3).sqrt().sqrt()).hi<Q('.76').lo,'Carleman d_a>.24')
    cap((2*ell+2*pi)/Q('.24'),'60','complete response norm <60')
    cap(ap+am+kap,'8','complete both forcing norms <8')
    budgets={}
    budgets['two_product_A']=gamma(4096)*32**2*1000+Q('1e-9')
    budgets['two_product_B']=2*gamma(4096)*32*23*100+Q('1e-9')
    budgets['trial']=20*gamma(4096)*(23**2*1000+50*8+200*8**2)+Q('1e-7')
    budgets['all_row_maps']=gamma(2048)*(2*257*23+1921*8)+Q('1e-8')
    budgets['head_gram_nuclear']=Q(E).sqrt()*gamma(1024)+Q('1e-8')
    budgets['finite_gram_trace']=gamma(K)*3+gamma(E*E)*10+gamma(2048)*Q(E).sqrt()*3+he+Q('1e-6')
    budgets['boundary']=gamma(4096)*100**2+Q('1e-7')
    budgets['H_assembly']=gamma(16)*401+Q('1e-10')
    for k,x in budgets.items():cap(x, '1e-5' if k in ('trial','boundary') else ('1e-4' if k=='finite_gram_trace' else ('1e-8' if k=='H_assembly' else '1e-6')), 'paid arithmetic '+k)
    check((sq(yn)-Q('.61')**2-Q('1e-6')).lo>(gamma(4096)*64+Q('1e-10')).hi,'predictor norm inflation pays Gram')
    check((Q('10.000001')**2-100-Q('1e-6')).lo>(gamma(4096)*100000+Q('1e-8')).hi,'LZ norm inflation pays Gram')
    evidence['arithmetic_budgets']={k:v.json() for k,v in budgets.items()}
    evidence['full_array_count']=len(ar);evidence['residual_digest']=original['ledger']['complete_residual_sha256']
    evidence['initial_complement_gram_trace']=float(np.trace(firstgram))
    evidence['finite_reference_trace']=trace.json()
    for n,h in pins.items():check(sha(BASE/n)==h,'original preserved '+n)
    evidence['input_hashes']=pins

try:main()
except Exception as exc:failures.append(type(exc).__name__+': '+str(exc))
out=BASE/'tail-galerkin-family-audit-596.json'
report=dict(scope='C999q unchanged fixed-band quarter conceptual audit',script_sha256=sha(Path(__file__)),evidence=evidence,checks=checks,failures=failures,result='PASS_UNDER_RETAINED_CONTRACTS' if not failures else 'INCONCLUSIVE',required='quarter exact tail metric in every complex direction',upheld_absolute_surplus='.000999' if not failures else None,qualifications=['Inherited analytic-response and IEEE754/Decimal contracts','Whole-neutral-core and original c_star not independently audited/replayed','Fixed band only; no mixed/high/H2/non-neutral/Xi conclusion'])
out.write_text(json.dumps(report,indent=2)+'\n')
print('Result',report['result'],'checks',len(checks),'failures',failures)
print('Required full quarter comparison; upheld surplus',report['upheld_absolute_surplus'])
for name in ['trial_error','finite_covariance_error','tail_remainder','weighted_LZ','exact_predictor_covariance_error']:print(name,evidence.get('bounds',{}).get(name))
print('Full certificate',out.relative_to(BASE.parent.parent))
