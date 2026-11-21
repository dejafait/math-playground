#!/usr/bin/env python3
"""Fixed full-residual band certificate; analytic ledger is in C998q.

No parameter search. Binary64 centers use C744w's retained arithmetic
contract. Final 3x3 sign checks use Fraction on exact stored dyadics.
The auxiliary smooth-kernel grid does not change the 286/14 reference.
"""
from decimal import Decimal as D, localcontext, ROUND_CEILING
from fractions import Fraction as F
from pathlib import Path
import hashlib
import importlib.util
import json
import numpy as np

B = Path(__file__).resolve().parent
OUT = B / 'shifted-finite-band-701.json'
TARGET = 'Test a 10^-6 X*X lower saving from modes512:1023 of the full frozen C998a residual under the fixed shifted reference R-2delta I, paying all coefficient and projection errors.'
checks, failures, pins = [], [], {}
report = dict(target=TARGET, result='INCOMPLETE', certified=False,
              checks=checks, failures=failures, input_sha256=pins,
              fixed=dict(band=[512,1023], delta='1/100', beta='219999/1000000',
                         reference_m=286, reference_J=14, quadrature_m=4096,
                         E_first=14, E_stop=80, column_error_limit='1/200',
                         new_arithmetic_reserve='1/100000',
                         center_singular_test='1/125', threshold='1/1000000'),
              qualification='Conditional on C744v/w and C999/C998a retained analytic, arithmetic, source, core and unreplayed c_star contracts. No full Gamma/E, S3 or RH conclusion.')

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def ck(ok, name):
    checks.append(dict(check=name, passed=bool(ok)))
    if not ok: raise ValueError(name)
def pin(name, expected=None):
    pins[name] = sha(B/name)
    if expected: ck(pins[name] == expected, 'pin '+name)
def enc(q): return str(q)
def upper(x, places=12):
    with localcontext() as c:
        c.prec=80
        return F(x.quantize(D(1).scaleb(-places), rounding=ROUND_CEILING))
def ff(x): return F.from_float(float(x))
def dec(q): return D(q.numerator)/D(q.denominator)
def sqrt_upper(q):
    with localcontext() as c:
        c.prec=80
        return upper(dec(q).sqrt()+D('1e-60'))
def norm_upper(a): return sqrt_upper(sum((ff(x)**2 for x in a), F(0)))+F(1,10**12)
def exact_gram(a, weights=None):
    w = [F(1)]*len(a) if weights is None else [ff(x) for x in weights]
    return [[sum((ff(row[i])*ff(row[j])*t for row,t in zip(a,w)),F(0))
             for j in range(3)] for i in range(3)]
def minors(a):
    return [a[0][0],a[0][0]*a[1][1]-a[0][1]*a[1][0],
            a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
            -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
            +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0])]
def matenc(a): return [[enc(x) for x in row] for row in a]

try:
    pin('frozen-reference-proposal-652.npz','2b770a8a689a972ae487b9dd718e2e6d47b6769a5530e7fec244a102c5c317c6')
    pin('neutral-reference-rank-obstruction-640.json')
    pin('neutral-reference-rank-audit-642.json')
    saved=json.loads((B/'neutral-reference-rank-obstruction-640.json').read_text())
    audited=json.loads((B/'neutral-reference-rank-audit-642.json').read_text())
    ck(saved['witness']==audited['witness'] and not audited['failures'], 'entire audited96-integer witness')
    w=saved['witness']
    ck(w['support_indices_zero_based']==list(range(16))+list(range(1022,1038))
       and w['denominator']==2**24 and w['ambient_dimension']==2044
       and w['omitted_coordinates']=='exactly zero','exact support and scale')
    X=np.zeros((2044,3)); X[w['support_indices_zero_based']]=np.array(w['integer_columns_by_row'])/2**24
    with np.load(B/'frozen-reference-proposal-652.npz',allow_pickle=False) as z:
        Y=z['free_middle_dyadics'].copy()
    ck(Y.shape==(254,3) and np.isfinite(Y).all(),'all762 frozen free dyadics')
    pin('residual-certificate-532.py')
    spec=importlib.util.spec_from_file_location('entries532',B/'residual-certificate-532.py')
    old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)
    con=old.constants(); ell,pi=con['ell'],con['pi']; a=ell/2
    n=np.arange(1024); k=n*pi/ell
    nu=np.full(1024,np.sqrt(2/ell));nu[0]=1/np.sqrt(ell)
    parity=np.where(n%2==0,1.,-1.)
    # Exact completion is defined by these formulas; centers are rounded once.
    def complete(y):
        N=len(y)+2
        with localcontext() as c:
            c.prec=80
            el=D(3).ln()/2; pp=D(old.PI_TEXT); rt=D(2).sqrt()
            rows=[[D.from_float(float(x)) for x in row] for row in y]
            lo=[]
            for p in [0,1]:
                rr=[]
                for j in range(3):
                    rr.append(-sum(((rt if p==0 else D(1))
                        *(D(1)/4+(D(p)*pp/el)**2)
                        /(D(1)/4+(D(q)*pp/el)**2)*rows[q-2][j]
                        for q in range(2,N) if q%2==p),D(0)))
                lo.append(rr)
            return np.array([[float(x) for x in row] for row in lo+rows])
    f=complete(X[:16]);h=complete(X[1022:1038]);q=complete(Y)
    l1=lambda z:[sum((abs(ff(x)) for x in z[:,j]),F(0))+F(1,10**12) for j in range(3)]
    sf,sh,sq=l1(f),l1(h),l1(q)
    nf,nh,nq=([norm_upper(z[:,j]) for j in range(3)] for z in [f,h,q])
    ck(max(sf+sh+sq)<20,'coefficient L1 norms below20')
    ck(max(nq)<1,'frozen exact-neutral middle norms below1')
    # C998q's explicit new arithmetic ledger. Per basis-cell integral
    # error1e-13, per smooth kernel value error1e-10, gamma_(2M)<1e-12.
    smooth_arithmetic=[]
    for M in [286,4096]:
        cell_error=21*F(1,10**13)+F(3,M*10**12)
        action_error=12*M*cell_error+F(1,10**10)+F(2,10**11)
        coefficient_error=2*action_error+12*M*F(1,10**13)+F(3,10**11)
        smooth_arithmetic.append(23*coefficient_error)
    E_arithmetic=23*66*F(5,10**10)
    assembly_arithmetic=F(1,10**8)
    new_arithmetic=sum(smooth_arithmetic,F(0))+E_arithmetic+assembly_arithmetic
    report['new_arithmetic_ledger']=dict(
        smooth_band_errors=[enc(x) for x in smooth_arithmetic],
        E_band_error=enc(E_arithmetic),assembly_band_error=enc(assembly_arithmetic),
        entire_bound=enc(new_arithmetic),reserved=enc(F(1,100000)))
    ck(new_arithmetic<F(1,100000),'entire new arithmetic fits fixed1e-5 allocation')
    report['coefficient_norm_upper']={key:[enc(v) for v in val]
          for key,val in [('sf',sf),('sh',sh),('sq',sq),('nf',nf),('nh',nh),('nq',nq)]}
    # Entire original response and both forcing orientations on every band row.
    kn=k[512:,None];km=k[None,:256]
    denom=kn*kn-km*km
    imag,rem=old.psi_imag(k,pi);bb=k*imag/2
    scale=2*np.outer(nu[512:],nu[:256])*(parity[512:,None]==parity[None,:256])
    S=(bb[512:,None]-bb[None,:256])/denom
    for j in range(64):
        c=2*j+.5
        S-=3.**(-j)/con['fourth']*parity[512:,None]*c*c/((c*c+kn*kn)*(c*c+km*km))
    S*=scale
    def trans(dl, width):
        kr=k[512:,None];kc=k[None,:width]
        sr,_=old.sincos(k[512:]*dl,pi);sc,_=old.sincos(k[:width]*dl,pi)
        signs=parity[512:,None]*parity[None,:width]
        num=(-signs*kr*sr[:,None]+kc*sc[None,:]) if dl>0 else (kr*sr[:,None]-signs*kc*sc[None,:])
        return num/(kr*kr-kc*kc)*np.outer(nu[512:],nu[:width])
    T=np.zeros((512,18));Ts=T.copy()
    for dl,wt in zip(con['deltas'],con['weights']):
        T+=wt*trans(dl,18);Ts+=wt*trans(-dl,18)
    for j in range(1,8):
        c=2*j+.5;dd=3.**(-j)/con['fourth']
        minus=nu*c*(1-parity*dd)/(c*c+k*k)
        plus=nu*c*(parity-dd)/(c*c+k*k)
        pre=3.**(-6*j)/(3*np.sqrt(3.))
        T+=pre*np.outer(minus[512:],plus[:18]);Ts+=pre*np.outer(plus[512:],minus[:18])
    ck(max(np.max(abs(S)),np.max(abs(T)),np.max(abs(Ts)))<400,'all original band entries below400')
    original=T@f+Ts@h-S@q
    # Exact parity basis: sqrt(2)(-1)^n e_n(t).
    def integrals(indices,M):
        edges=np.arange(M+1)*a/M
        sn,_=old.sincos(k[indices,None]*edges[None,:],pi)
        out=np.diff(sn,axis=1)/np.where(indices[:,None]==0,1,k[indices,None])
        if 0 in indices: out[indices==0]=a/M
        return out*(np.sqrt(2)*nu[indices]*parity[indices])[:,None]
    def smooth_action(M):
        # Only2M-1 distinct kernel values; Decimal avoids corner cancellation.
        with localcontext() as c:
            c.prec=80;aa=D(3).ln()/4
            hv=[]
            for j in range(1,2*M):
                u=D(j)*aa/D(M)
                hv.append(float((-u/2).exp()/(1-(-2*u).exp())-1/(2*u)))
        hv=np.array(hv)
        ck(np.max(abs(hv))<12,'smooth scalar bound grid'+str(M))
        inp=integrals(np.arange(256),M);out=integrals(np.arange(512,1024),M)
        result=np.zeros((512,3))
        for p in [0,1]:
            ii=np.arange(256)%2==p;oo=np.arange(512,1024)%2==p
            cell=inp[ii].T@q[ii]
            action=np.empty_like(cell)
            for first in range(0,M,128):
                rows=np.arange(first,min(first+128,M))
                hh=hv[rows[:,None]+np.arange(M)[None,:]]
                action[rows]=hh@cell
            result[oo]=out[oo]@action
        return result
    coarse=smooth_action(286);fine=smooth_action(4096)
    # E correction includes every one of its four products, in both parities.
    E=np.zeros((512,3))
    for j in range(14,80):
        c=2*j+.5
        with localcontext() as ctx:
            ctx.prec=80;ee=float((-D(str(c))*D(3).ln()/4).exp())
        b=ee*ee
        sn=np.choose(n%4,[0.,1.,0.,-1.]);cs=np.choose(n%4,[1.,0.,-1.,0.])
        norm=np.sqrt(2)*nu*parity
        ph=norm*(c+ee*(-c*cs+k*sn))/(c*c+k*k)
        ps=norm*(ee*(c*cs+k*sn)-b*c)/(c*c+k*k)
        for p,eps in [(0,1),(1,-1)]:
            ii=np.arange(256)%2==p;oo=np.arange(512,1024)%2==p
            ap=ph[:256][ii]@q[ii];az=ps[:256][ii]@q[ii]
            E[oo]+=(eps*b*ph[512:][oo,None]*ap+ps[512:][oo,None]*az
                       +eps*ph[512:][oo,None]*az+eps*ps[512:][oo,None]*ap)/(1-eps*b)
    center=original-coarse+fine+E
    ck(center.shape==(512,3) and np.isfinite(center).all(),'all1536 complete band centers formed')
    # Pay full projection, not a sampled or truncated moment vector.
    with localcontext() as c:
        c.prec=80;el=D(3).ln()/2;pp=D(old.PI_TEXT)
        ep=(el/2).exp();em=1/ep
        gp=(el.exp()-1);gm=1-(-el).exp();det=gp*gm-el*el
        projection_trace=D(0);pr=[];weights=[];wr=[]
        for index in range(512,1024):
            kk=D(index)*pp/el;nn=(2/el).sqrt();sg=D(1 if index%2==0 else -1)
            cp=nn*(sg*ep-1)/2/(D(1)/4+kk*kk)
            cm=-nn*(sg*em-1)/2/(D(1)/4+kk*kk)
            v=(gm*cp*cp-2*el*cp*cm+gp*cm*cm)/det
            ck(v>0,'positive moment projection norm row'+str(index))
            projection_trace+=v;pr.append(upper(v.sqrt()+D('1e-60')))
            yy=kk/2;aa=D('64.25')
            hv=(aa*aa+yy*yy).ln()/2-aa/(2*(aa*aa+yy*yy))-pp.ln()
            for z in range(64): hv-=(D(z)+D('.25'))/((D(z)+D('.25'))**2+yy*yy)
            er=D(2).sqrt()/(6*(aa*aa+yy*yy))+D('1e-50')
            wc=1/D('.219999')-1/(hv/2-D('.02'))
            wl=1/D('.219999')-1/((hv-er)/2-D('.02'))
            wu=1/D('.219999')-1/((hv+er)/2-D('.02'))
            wf=float(wc);weights.append(wf)
            we=max(abs(D.from_float(wf)-wl),abs(wu-D.from_float(wf)))+D('1e-50')
            wr.append(upper(we))
        pbound=upper((projection_trace+D('1e-50')).sqrt())
    ck(max(wr)<F(1,10**8),'all512 weight errors below1e-8')
    ck(min(weights)>4 and max(weights)<5,'all band weight centers inside(4,5)')
    eta=F(303,16)*F(3,10)**2/4096
    tail=18*F(2,3)**80
    errors=[];ledger=[]
    for j in range(3):
        eo=F(181,10**9)*nq[j]+23*(F(1,10**7)*sq[j]+F(21,10**8)*(sf[j]+sh[j]))+F(1001,10**9)
        eg=5*(nf[j]+nh[j])+45*nq[j]
        pe=pbound*eg
        ej=eo+(eta+tail)*nq[j]+pe+F(1,100000)
        errors.append(ej)
        ledger.append(dict(column=j,original_entry_and_action_error=enc(eo),
            smooth_quadrature_error=enc(eta*nq[j]),E_suffix_error=enc(tail*nq[j]),
            full_unprojected_norm_upper=enc(eg),full_projection_error=enc(pe),
            new_arithmetic_error=enc(F(1,100000)),complete_band_error=enc(ej)))
    report['projection']=dict(ambient_Pband_PW_norm_upper=enc(pbound),
                              each_basis_projection_norm_upper=[enc(x) for x in pr])
    report['error_ledger']=ledger
    ck(max(errors)<F(1,200),'fixed complete band column allocation1/200')
    eop=sqrt_upper(sum((x*x for x in errors),F(0)))
    gram=exact_gram(center);s0=F(1,125)
    sing=[[gram[i][j]-(s0*s0 if i==j else 0) for j in range(3)] for i in range(3)]
    sm=minors(sing)
    ck(all(x>0 for x in sm),'exact center singular lower bound1/125')
    ck(eop<s0,'complete coefficient operator error below singular lower bound')
    saving=4*(s0-eop)**2
    xgram=exact_gram(X)
    psd=[[saving*(i==j)-F(1,10**6)*xgram[i][j] for j in range(3)] for i in range(3)]
    pm=minors(psd)
    ck(all(x>0 for x in pm),'exact PSD certificate for saving minus1e-6 XstarX')
    kg=exact_gram(center,weights)
    cn=[norm_upper(center[:,j]) for j in range(3)]
    kr=[[F(1,10**8)*cn[i]*cn[j]+5*(cn[i]*errors[j]+cn[j]*errors[i]+errors[i]*errors[j])
          for j in range(3)] for i in range(3)]
    report['coefficients']=dict(first=512,last=1023,
        centers_as_exact_binary64=center.tolist(),
        column_L2_error_upper=[enc(x) for x in errors],
        individual_entry_radius=[enc(x) for x in errors],
        warning='Column L2 bounds are stronger than separate entry radii; all projection errors retained.')
    report['weights']=dict(centers_as_exact_binary64=weights,
                          individual_absolute_error=[enc(x) for x in wr],analytic_lower='4',analytic_upper='5')
    report['matrix']=dict(K_center=matenc(kg),K_entry_radius=matenc(kr),
                         coefficient_center_gram=matenc(gram),XstarX=matenc(xgram))
    report['exact_PSD_certificate']=dict(center_singular_lower=enc(s0),
        center_gram_shifted_leading_minors=[enc(x) for x in sm],
        complete_operator_error_upper=enc(eop),
        K_isotropic_lower=enc(saving),threshold_matrix=matenc(psd),
        threshold_leading_minors=[enc(x) for x in pm])
    ck(all(sha(B/name)==digest for name,digest in pins.items()),'all source artifacts preserved')
    report.update(result='CONDITIONAL_FIXED_BAND_SAVING_CERTIFIED',certified=True)
except Exception as exc:
    failures.append(type(exc).__name__+': '+str(exc))
    report['result']='FIXED_SERVICE_OR_THRESHOLD_FAILED'

report['script_sha256']=sha(Path(__file__))
OUT.write_text(json.dumps(report,indent=2)+'\n')
print('Result:',report['result'])
if 'error_ledger' in report:
    print('Complete column errors:',[float(F(x['complete_band_error'])) for x in report['error_ledger']],'; required <=.005')
if 'exact_PSD_certificate' in report:
    p=report['exact_PSD_certificate']
    print('Center singular lower:',float(F(p['center_singular_lower'])),
          '; complete operator error <=',float(F(p['complete_operator_error_upper'])))
    print('K lower >=',float(F(p['K_isotropic_lower'])),'I; required >=1e-6 X*X')
print('Checks:',sum(x['passed'] for x in checks),'/',len(checks),'Failures:',failures)
print('Complete certificate:',OUT.relative_to(B.parent.parent))
