#!/usr/bin/env python3
"""Fixed-J inverse-input bound, C999m Section10; no FFT premise.

Full direct residual replay, inverse centers, factors and directed scalars
are saved. This is one component of the unchanged quarter-budget test.
"""
import hashlib
import importlib.util
import json
from decimal import Context, Decimal, ROUND_CEILING, ROUND_FLOOR, ROUND_HALF_EVEN, localcontext
from pathlib import Path
import numpy as np

BASE=Path(__file__).resolve().parent
N,J,K,F,E=512,32768,65536,510,1020
def load(name,path):
    sp=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
iv=load('iv569',BASE/'complete-schur-531.py')
iv.DOWN=Context(prec=80,rounding=ROUND_FLOOR)
iv.UP=Context(prec=80,rounding=ROUND_CEILING)
iv.NEAR=Context(prec=80,rounding=ROUND_HALF_EVEN)
I=iv.I
old=load('entries569',BASE/'residual-certificate-532.py')
checks,failures,pins=[],[],{}
def check(ok,label):
    checks.append(dict(label=label,passed=bool(ok)))
    if not ok: failures.append(label)
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def fro(x): return float(np.linalg.norm(x))
def sq(x): return x*x
def atan(q):
    x=I(1)/q; total=I(0); power=x
    for n in range(80):
        total+=((-1)**n)*power/(2*n+1); power*=x*x
    return total+I(-power.hi,power.hi)/161

audit=json.loads((BASE/'neutral-head-covariance-audit-561.json').read_text())
head=json.loads((BASE/'neutral-head-covariance-559.json').read_text())
audit534=json.loads((BASE/'certificate-audit-534.json').read_text())
for name in ['neutral-head-covariance-559.npz','neutral-head-covariance-559.json','complete-schur-531.py']:
    pins[name]=sha(BASE/name)
    check(pins[name]==audit['original_hashes'][name],'audited input unchanged '+name)
for name in ['residual-certificate-532.py','complete-covariance-532.npz']:
    pins[name]=sha(BASE/name)
    check(pins[name]==audit534['original_sha256'][name],'entry input unchanged '+name)
for label,data in [('559',head),('561',audit)]:
    check(not data['failures'] and all(c['passed'] for c in data['checks']),
          'complete inherited check list '+label)
check(sha(BASE/'neutral-head-covariance-audit-561.py')==audit['source_script_sha256'],
      'audit561 source unchanged')
check(head['parameters']==dict(N=N,K=K,endpoint_dimension=E,middle_dimension=F,
      d0='6.14',fraction='1/2',penalty=256),'fixed target parameters')
with np.load(BASE/'neutral-head-covariance-559.npz') as a:
    z,y,gg,mc,sol=a['z'],a['predictor_free'],a['predictor_raw'],a['comparison_lower'],a['head_solution']
check(np.array_equal(mc,mc.T),'exact comparison symmetry')
check(z.shape==(N,F) and gg.shape==(N,E) and sol.shape==(N,E),'full head dimensions')

# The exact audited559 direct formulas, inserted below; no FFT is used.
con = old.constants()
el, pif = con['ell'], con['pi']
indices = np.arange(K)
k = indices*pif/el
nu = np.full(K, np.sqrt(2/el)); nu[0] = 1/np.sqrt(el)
parity = np.where(indices % 2 == 0, 1., -1.)
imag, _ = old.psi_imag(k, pif)
bpsi = k*imag/2
moments = np.array([nu*c*(parity*(con['fourth'] if c > 0 else 1/con['fourth'])-1)
                    /(c*c+k*k) for c in [.5, -.5]])

def translation(rows, delta):
    kn, km = k[rows, None], k[None, :N]
    sn, _ = old.sincos(k[rows]*delta, pif)
    sm, _ = old.sincos(k[:N]*delta, pif)
    signs = parity[rows, None]*parity[None, :N]
    if delta > 0:
        numerator = -signs*kn*sn[:, None]+km*sm[None, :]
    else:
        numerator = kn*sn[:, None]-signs*km*sm[None, :]
    return numerator/(kn*kn-km*km)*np.outer(nu[rows], nu[:N])


with localcontext() as ctx:
    ctx.prec=80
    logs=np.array([float((Decimal('64.25')**2+(Decimal(float(t))/2)**2).ln()/2) for t in k[N:]])
yy=k[N:]/2; aa=64.25
hcenter=logs-aa/(2*(aa*aa+yy*yy))-con['logpi']
for j in range(64): hcenter-=(j+.25)/((j+.25)**2+yy*yy)
check(float(hcenter.min())>6.14,'all inverse diagonal centers above6.14')
vpath=BASE/'signed-mixed-inverse-centers-569.npy'
v=np.lib.format.open_memmap(vpath,mode='w+',dtype='float64',shape=(K,E))
v[:N]=sol
residual_hash=hashlib.sha256(); raw_normsq=0.; residual_fro2=0.; blocks=[]
for start in range(N,K,N):
    rows=slice(start,start+N)
    kn, km = k[rows, None], k[None, :N]
    same = parity[rows, None] == parity[None, :N]
    response = (bpsi[rows, None]-bpsi[None, :N])/(kn*kn-km*km)
    for j in range(64):
        c = 2*j+.5
        response -= ((3.**(-j)/con['fourth'])*parity[rows, None]*c*c
                     /((c*c+kn*kn)*(c*c+km*km)))
    response *= 2*np.outer(nu[rows], nu[:N])*same
    tt, ts = np.zeros_like(response), np.zeros_like(response)
    for delta, weight in zip(con['deltas'], con['weights']):
        tt += weight*translation(rows, delta)
        ts += weight*translation(rows, -delta)
    for j in range(1, 8):
        c = 2*j+.5
        decay = 3.**(-j)/con['fourth']
        minus = nu*c*(1-parity*decay)/(c*c+k*k)
        plus = nu*c*(parity-decay)/(c*c+k*k)
        prefactor = 3.**(-6*j)/(3*np.sqrt(3.))
        tt += prefactor*np.outer(minus[rows], plus[:N])
        ts += prefactor*np.outer(plus[rows], minus[:N])
    w0 = response+256*moments[:, rows].T@moments[:, :N]
    rho = np.hstack((tt@z, ts@z))-w0@gg
    residual_hash.update(rho.tobytes())
    v[rows]=((2/hcenter[start-N:start])[:,None])*rho
    normsq=sum(fro(q)**2 for q in [w0,tt,ts]); raw_normsq+=normsq
    rf=fro(rho); residual_fro2+=rf*rf
    maximum=max(float(np.max(np.abs(q))) for q in [w0,tt,ts])
    check(maximum<400,'complete direct entry magnitude '+str(start))
    blocks.append(dict(first=start,last=start+N-1,raw_fro_squared=normsq,residual_fro=rf))
    if start%16384==0: print('Direct inverse rows through',start+N-1,flush=True)
v.flush()
check(residual_hash.hexdigest()==head['finite']['regenerated_combined_residual_sha256'],
      'all65024 direct residual rows agree with audited559 digest')
check(raw_normsq<20 and residual_fro2<4,'complete direct row magnitude ledger')

# Six full normalized Gram factors; finite rows only, on all complex heads.
qdef={'boundary_plus':3.,'boundary_minus':3.,'low_norm':.35,
      'moment1':.011,'moment2':.006,'band_norm':.007}
grams={key:np.zeros((E,E)) for key in qdef}
boundary=np.zeros((2,E)); normalized_fro2={key:0. for key in qdef}
for start in range(0,K,N):
    w=np.array(v[start:start+N]); ns=np.arange(start,start+N)
    if start<J:
        dd=np.ones(N); dd[ns==0]=1/np.sqrt(2)
        boundary[0]+=dd@w; boundary[1]+=(dd*((-1.)**ns))@w
        for key,power in [('low_norm',0),('moment1',1),('moment2',2)]:
            scaled=((ns/(J-1))**power)[:,None]*w/qdef[key]
            grams[key]+=scaled.T@scaled
            normalized_fro2[key]+=fro(scaled)**2
    else:
        scaled=w/qdef['band_norm']; grams['band_norm']+=scaled.T@scaled
        normalized_fro2['band_norm']+=fro(scaled)**2
for key,row in zip(['boundary_plus','boundary_minus'],boundary):
    scaled=row/qdef[key]; grams[key]=np.outer(scaled,scaled)
    normalized_fro2[key]=fro(scaled)**2
check(max(normalized_fro2.values())<10000,'every normalized Gram row Frobenius below100')
check(fro(v[:J])<1 and fro(v[J:])<.1 and fro(boundary)<100,
      'complete finite inverse and boundary magnitudes')
u=I(1)/2**53
gamma=lambda n:n*u/(1-n*u)
gram_error=gamma(2*K)*10000+I('1e-8')
factor_error=I('1e-7')+gamma(2048)*100000+I('2e-7')+gram_error
check(factor_error.hi<Decimal('1e-6'),'complete Gram/factor error below restored margin')
factors={}; ledgers={}
for key,gram in grams.items():
    target=mc-gram-1e-6*np.eye(E)
    try:
        factor=np.linalg.cholesky(target)
        residual=fro(target-factor@factor.T); ff=fro(factor)**2
        maximum=max(float(np.max(np.abs(a))) for a in [target,factor,gram,mc])
        check(residual<1e-7 and ff<100000 and maximum<400,'full factor '+key)
        factors[key]=factor
        ledgers[key]=dict(norm_proposal=qdef[key],residual_fro=residual,
                         factor_fro_squared=ff,maximum_entry=maximum)
    except np.linalg.LinAlgError:
        check(False,'full factor '+key); ledgers[key]=dict(norm_proposal=qdef[key],failed=True)

# Directed enclosure of exact center-to-inverse errors on separate ranges.
pi,ell=16*atan(5)-4*atan(239),I(3).ln()/2
mu,zn,yn=I('.000999'),I('1.008'),I('1.320001')
dK=I('10.9963070613268')
dJ=(I(J)/(2*ell)).ln()-2*ell*ell/(9*J*J)
rdiag=I(2).sqrt()/(6*(sq(I('64.25'))+sq(I(N)*pi/(2*ell))))
check((rdiag+I('1e-7')).hi<Decimal('1e-6'),'all inverse diagonal errors below1e-6')
deltaP=I(head['finite']['residual_head_error']['hi'])
solve=I(head['finite']['head_solve_error']['hi'])/I('.239999')
ehead=deltaP/I('.239999')+solve
def rect_error(count):
    count=I(count)
    e0=I('.000000181')+(count*N).sqrt()*I('1e-7')
    return I(2).sqrt()*(count*N).sqrt()*I('2.1e-7')*zn+e0*zn*yn+I('1e-7')
def inv_error(count,lower):
    # rho center Frobenius<2 on either range, true h>=lower,
    # and computed h>=lower-1e-6 by the exact diagonal error.
    return (2/lower)*rect_error(count)+4*I('1e-6')/(lower*(lower-I('1e-6')))+I('1e-7')
elo=inv_error(J-N,I('6.14')); eband=inv_error(K-J,dJ)
center_conversion=I('1e-7')
qb=3+(I(N).sqrt()*ehead+I(J-N).sqrt()*elo+center_conversion)/mu.sqrt()
q0=I('.35')+((ehead*ehead+elo*elo).sqrt()+center_conversion)/mu.sqrt()
q1=I('.011')+(I(N-1)/(J-1)*ehead+elo+center_conversion)/mu.sqrt()
q2=I('.006')+(I((N-1)**2)/(J-1)**2*ehead+elo+center_conversion)/mu.sqrt()
qband=I('.007')+(eband+center_conversion)/mu.sqrt()
input568=json.loads((BASE/'signed-mixed-local-trial-input-568.json').read_text())
pins['signed-mixed-local-trial-input-568.json']=sha(BASE/'signed-mixed-local-trial-input-568.json')
check(not input568['failures'] and all(c['passed'] for c in input568['checks']),
      'all inherited568 checks; unaudited quantitative input retained')
check(sha(BASE/'signed-mixed-local-trial-input-568.py')==input568['script_sha256'],
      '568 source unchanged')
vp=I(input568['sine_tails']['positive']['complete_sine_square_upper']['hi'])
vm=I(input568['sine_tails']['negative']['complete_sine_square_upper']['hi'])
weight=I(input568['scalars']['prime_total_weight']['hi'])
kappa=1/(I(2187)*I(3).sqrt()*I('2.5')*(1-I(1)/729))
theta=1-I((J-1)**2)/(K*K)
lead=(2/pi)*I(2).sqrt()*qb*(vp.sqrt()+vm.sqrt())
rem=(2/pi)*I(2).sqrt()*weight*I(J).sqrt()/theta*(
    (J-1)**2*q2/(I(5).sqrt()*sq(I(K-1))*I(K-1).sqrt())
    +(J-1)*q1/(I(3).sqrt()*I(K-1)*I(K-1).sqrt()))
continuous=I(2).sqrt()*kappa*q0
band=I(2).sqrt()*I('4.71')*qband
low=I(2).sqrt()*I('4.71')*(q0*q0+qband*qband).sqrt()
neutral=(4/(3*dK*(K-1)**3)).sqrt()*low
allowance=(lead+rem+continuous+band)/dK.sqrt()+neutral

# A fixed predeclared convenient component ceiling; failure is preserved.
check(allowance.hi<Decimal('.1'),'complete inverse-input component below .1')
archive=BASE/'signed-mixed-inverse-input-569.npz'
np.savez_compressed(archive,comparison=mc,boundary_rows=boundary,hcenter=hcenter,
                    **{k+'_factor':v for k,v in factors.items()},
                    **{k+'_normalized_gram':v for k,v in grams.items()})
scalars=dict(dJ=dJ,dK=dK,diagonal_error_bound=rdiag+I('1e-7'),head_inverse_error=ehead,
    low_complement_inverse_error=elo,band_inverse_error=eband,
    boundary_norm=qb,low_norm=q0,moment1_norm=q1,moment2_norm=q2,band_norm=qband,
    raw_leading=lead,raw_prime_remainder=rem,raw_continuous=continuous,
    raw_band=band,low_correction=neutral,inverse_input_tail=allowance,
    factor_error=factor_error,gram_error=gram_error)
record=dict(parameters=dict(N=N,J=J,K=K,endpoint_dimension=E),
    scope='A_R^K=(-T*P_<K R^-1 rho_tilde,-T P_<K R^-1 rho_tilde); exact Z and fixed Yhat',
    certified_under_inherited_contracts=not failures,input_hashes=pins,
    script_sha256=sha(Path(__file__)),
    full_residual_digest=residual_hash.hexdigest(),row_blocks=blocks,
    raw_factor_fro_squared=raw_normsq,residual_center_fro_squared=residual_fro2,
    normalized_gram_fro_squared=normalized_fro2,factors=ledgers,
    scalars={k:v.json() for k,v in scalars.items()},checks=checks,failures=failures,
    component_required_upper='.1',full_mixed_required_upper='.5',
    full_quarter_test_decided=False,
    artifacts={p.name:dict(path=str(p.relative_to(BASE.parent.parent)),sha256=sha(p))
               for p in [archive,vpath]},
    qualifications=['Unaudited specialization under inherited analytic/whole-core/c_star/IEEE754/Decimal contracts',
        'All within-column cross products must still be paid; scalar component norms are not covariance increments',
        'Finite mixed locator FFT and signed arithmetic remain uncertified; no quarter decision',
        'Predictor allowance is paid once for the whole map; complementary positivity and RH remain open'])
out=BASE/'signed-mixed-inverse-input-569.json'; out.write_text(json.dumps(record,indent=2)+'\n')
print('Inverse-input checks:',len(checks),'failures:',failures)
print('Actual normalized inverse-input upper:',allowance.hi,'; proposed component ceiling .1')
print('Full mixed norm requires <=.5; finite signed arithmetic remains unpaid; quarter undecided')
print('Certificate:',out.relative_to(BASE.parent.parent),'factors:',archive.relative_to(BASE.parent.parent))
