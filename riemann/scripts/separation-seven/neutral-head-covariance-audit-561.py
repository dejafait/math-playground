#!/usr/bin/env python3
"""C999l audit: full replay comparison, integer outward scalar checks,
all saved factor reconstructions and complete finite arithmetic ledgers.
No retuning; inherited analytic/IEEE754/Decimal contracts remain explicit.
"""
import hashlib
import importlib.util
import json
import platform
import sys
from decimal import Decimal, localcontext
from fractions import Fraction as Fr
from pathlib import Path
import numpy as np

BASE = Path(__file__).resolve().parent
N, K, F, E = 512, 65536, 510, 1020

def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

arith = load('int552audit561', BASE/'fixed-trial-residual-audit-552.py')
Q, SCALE = arith.Q, arith.SCALE
checks, failures, evidence = [], [], {}

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def check(ok, label):
    checks.append({'label':label, 'passed':bool(ok)})
    if not ok:
        failures.append(label)

def sq(x):
    if x.lo <= 0 <= x.hi:
        return Q.ends(0, -(-max(x.lo*x.lo, x.hi*x.hi)//SCALE))
    return x*x

def ln(x):
    assert x.lo > 0
    with localcontext() as ctx:
        ctx.prec = 140
        lo = ctx.next_minus((Decimal(x.lo)/Decimal(SCALE)).ln())
        hi = ctx.next_plus((Decimal(x.hi)/Decimal(SCALE)).ln())
    return Q.ends(Q(Fr(lo)).lo, Q(Fr(hi)).hi)

def enclosed(x, saved, label):
    check(Fr(saved['lo']) <= Fr(x.lo,SCALE) <= Fr(x.hi,SCALE) <= Fr(saved['hi']), label)

def upper(x, saved, label):
    check(0 <= x.lo <= x.hi and Fr(x.hi,SCALE) <= Fr(saved['hi']), label)

def fro(a):
    return float(np.sqrt(np.sum(a*a)))

def gamma(n):
    t = Q(Fr(n, 2**53))
    return t/(1-t)

def short(x):
    with localcontext() as ctx:
        ctx.prec = 22
        ctx.rounding = 'ROUND_CEILING'
        return str(Decimal(x.hi)/Decimal(SCALE))

original = json.loads((BASE/'neutral-head-covariance-559.json').read_text())
replay = json.loads((BASE/'neutral-head-covariance-replay-561.json').read_text())
first = json.loads((BASE/'neutral-head-covariance-first-pass-559.json').read_text())
names = ['neutral-head-covariance-559.'+e for e in ('py','json','npz','log')]
names += ['neutral-head-covariance-first-pass-559.'+e for e in ('py','json','npz','log')]
names += list(original['input_hashes'])
pins = {n:sha(BASE/n) for n in names}
check(original['source_script_sha256']==pins['neutral-head-covariance-559.py'], 'original script hash')
check(original['binary_artifact']['sha256']==pins['neutral-head-covariance-559.npz'], 'original full binary hash')
for n, h in original['input_hashes'].items():
    check(pins[n]==h, 'input hash '+n)
check(not original['failures'] and all(q['passed'] for q in original['checks']), 'all original checks')
check(not replay['failures'] and all(q['passed'] for q in replay['checks']), 'all 100-digit replay checks')
check(original['parameters']==dict(N=N,K=K,endpoint_dimension=E,middle_dimension=F,d0='6.14',fraction='1/2',penalty=256), 'unchanged full family and reference')
with np.load(BASE/'neutral-head-covariance-559.npz') as a:
    arrays = {k:a[k] for k in a.files}
with np.load(BASE/'neutral-head-covariance-replay-561.npz') as a:
    check(set(a.files)==set(arrays), 'full matrix field coverage')
    for k,v in arrays.items():
        check(np.array_equal(v,a[k]), 'entire matrix replay '+k)
        check(np.isfinite(v).all(), 'finite matrix '+k)
check(original['finite']['regenerated_combined_residual_sha256']==replay['finite']['regenerated_combined_residual_sha256'], 'all 65024 residual row bytes')
blocks=original['finite']['row_blocks']
check([(x['first'],x['last']) for x in blocks]==[(n,n+N-1) for n in range(N,K,N)], '127 blocks exactly partition finite complement')
check(blocks==replay['finite']['row_blocks'], 'all finite row magnitude ledgers replay')
check(sum(x['raw_factor_fro_squared'] for x in blocks)<20, 'complete raw squared factor norm <20')
check(all(x['maximum_entry']<400 for x in blocks), 'all raw factor entries <400')

half=Q(Fr(1,2))
ell=sum((half**(2*j+1)/(2*j+1) for j in range(200)),Q())
ell+=Q.ends(0,(half**401/(401*(1-half*half))).hi)
pi=16*arith.atan(5)-4*arith.atan(239)
enclosed(ell,original['constants']['ell'],'independent atanh ell')
enclosed(pi,original['constants']['pi'],'independent Machin pi')
z=arrays['z']; y=arrays['predictor_free']; g=arrays['predictor_raw']
k2=[sq(n*pi/ell) for n in range(N)]
conv, rsq=Q(),[Q(),Q()]
for n in range(2,N):
    p=n%2
    r=(Q('.25')+k2[p])/(Q('.25')+k2[n])
    if p==0: r*=Q(2).sqrt()
    enclosed(r,original['neutral_ratios'][n-2],'exact neutral ratio '+str(n))
    conv+=(r-Q(Fr(float(-z[p,n-2])))).ab()
    rsq[p]+=sq(r)
    check(z[n,n-2]==1 and np.count_nonzero(z[:,n-2])==2, 'neutral column support '+str(n))
check(conv.hi<Q('1e-14').lo,'whole exact-to-dyadic basis error')
zn=Q('1.008'); yn=Q('1.320001'); mz=Q('6.190001')
check((1+Q.ends(max(q.lo for q in rsq),max(q.hi for q in rsq))).sqrt().hi<zn.lo,'operator basis norm')
evidence['basis_conversion']=conv.json()

# Fresh enumeration and every retained diagonal weight, not a sample.
primes=[]
for p in range(2,81):
    if all(p%d for d in range(2,__import__('math').isqrt(p)+1)):
        primes.append(p)
powers=[]
for p in primes:
    n=p
    while n<81:
        if n>27:powers.append((n,p))
        n*=p
powers.sort()
old=load('entries532audit561',BASE/'residual-certificate-532.py')
check(powers==old.POWERS,'complete separation7 prime enumeration')
ap,am=Q(),Q()
for n,p in powers:
    delay=7*ell-ln(Q(n)); w=ln(Q(p))/Q(n).sqrt()
    check(delay.lo>0 or delay.hi<0,'strict delay sign '+str(n))
    if delay.lo>0:ap+=w
    else:am+=w
fixed=json.loads((BASE/'fixed-block-metric-555.json').read_text())
lowers=fixed['middle']['diagonal_lower_endpoints']
check(len(lowers)==K-N,'complete lower weight count')
for n,s in enumerate(lowers,N):
    dn=ln(n/(2*ell))-2*sq(ell)/(9*n*n)
    check(Q(s).hi<=dn.lo and Q(s).lo>Q('6.14').hi, 'diagonal bound '+str(n))
    weight=np.nextafter(float(2/Decimal(s)),np.inf)
    check(Fr(float(weight))>=2/Fr(s),'upward finite weight '+str(n))

eta_a=Q('.00024')*sq(zn)+Q('1e-7')
eta_b=Q(2).sqrt()*sq(zn)*N*Q('2.1e-7')+Q('1e-7')
k14=1/(Q(3**16)*Q(3).sqrt().sqrt()*Q('2.5')*(1-Q(1)/3**13))
eta_u=sq(zn)*(N*Q('1e-7')+k14)+Q('1e-7')
rgal=eta_b+eta_a*yn+Q('1e-7'); dy=rgal/Q('.779')
e_trial=eta_a*(1+sq(yn))+2*eta_b*yn+eta_u+Q('1e-6')+sq(rgal)/Q('.779')
e0=Q('.000000181')+Q((K-N)*N).sqrt()*Q('1e-7')
dp=Q(2).sqrt()*N*Q('2.1e-7')*zn+Q('.00024')*zn*yn+Q('1e-7')
dm=Q(2).sqrt()*Q((K-N)*N).sqrt()*Q('2.1e-7')*zn+e0*zn*yn+Q('1e-7')
df=(sq(dp)/Q('.239999')+2*sq(dm)/Q('6.14')).sqrt()
tf=Q(str(float(np.trace(arrays['head_covariance']+arrays['finite_covariance']))))+Q('.00001')
check(tf.lo>0 and tf.hi<Q(3).lo,'complete finite trace including head error <3')
e_f=2*tf.sqrt()*df+sq(df)+Q('.00001')
values=dict(head_form_error=eta_a,forcing_error=eta_b,remote_error=eta_u,
    galerkin_equation_error=rgal,predictor_free_error=dy,full_trial_error=e_trial,
    residual_head_error=dp,residual_middle_error=dm,weighted_residual_error=df,finite_covariance_error=e_f)
for key,value in values.items():upper(value,original['finite'][key],'independent finite bound '+key)
wb=4*ell*(1+Q('1.5')/Q(3).sqrt().sqrt())/sq(pi)
weights=[2*ap/pi/Q(K-1).sqrt(),2*am/pi/Q(K-1).sqrt()]*2
weights += [Q(2).sqrt()*(1+wb/K)/Q(K-1).sqrt(),(1+wb/K)/Q(K-1).sqrt()]
pr=(2/pi)/(1-Q((N-1)**2)/(K*K))*(Q(sum(n**4 for n in range(1,N))).sqrt()/Q(5*(K-1)**5).sqrt()+Q(sum(n*n for n in range(1,N))).sqrt()/Q(3*(K-1)**3).sqrt())*(ap+am)
sr=sum((sq(4*n+16*ell/sq(pi)) for n in range(N)),Q()).sqrt()/Q(3*(K-1)**3).sqrt()
kap=1/(2187*Q(3).sqrt()*Q('2.5')*(1-Q(1)/729))
trem=Q(2).sqrt()*zn*(pr+kap)+sr*zn*yn
dk=ln(K/(2*ell))-2*sq(ell)/(9*K*K)
tvals=dict(prime_weight_positive=ap,prime_weight_negative=am,response_b=wb,prime_remainder=pr,response_remainder=sr,complete_continuous_norm=kap,remainder=trem,diagonal_lower=dk)
for key,value in tvals.items():enclosed(value,original['tail'][key],'independent tail bound '+key)
for j,w in enumerate(weights):enclosed(w,original['tail']['six_weights'][j],'boundary weight '+str(j))
lz=(sq(mz+Q('.00024')*zn+Q('1e-7'))/Q('.239999')+2*sq((Q('.586')+e0+Q('.062501906'))*zn)/Q('6.14')).sqrt()
dg=lz*dy; eg=2*Q('.951').sqrt()*dg+sq(dg)
for key,value in dict(reference_weighted_LZ_bound=lz,residual_change=dg,covariance_error=eg).items():upper(value,original['exact_predictor'][key],'independent predictor bound '+key)
evidence['integer_scalar_bounds']={k:v.json() for k,v in dict(**values,**tvals,weighted_LZ=lz,delta_G=dg,e_G=eg).items()}

# All entries of every original factor; gamma ledgers do not trust Cholesky.
with np.load(BASE/'complete-covariance-532.npz') as a:
    m0=a['m0']; t0=a['mc']+a['mg']; cov=a['cov00']
with np.load(BASE/'response-prefix-remote-546.npz') as a: remote=a['remote_prime']
aa,bb=arrays['a'],arrays['b']
targets=dict(galerkin_floor=aa-.7793*np.eye(F),predictor_norm=1.32**2*np.eye(F)-y@y.T,
    head_LZ_norm=6.19**2*np.eye(F)-(m0@z).T@(m0@z),comparison_margin=arrays['comparison_lower']-.001*np.eye(E))
fl={}
for name,mat in targets.items():
    fac=arrays['factor_'+name]; resid=fro(mat-fac@fac.T); f2=fro(fac)**2
    # 2e-7 covers operand assembly, subtraction and norm-evaluation;
    # product uses conservatively gamma_2048 rather than gamma_1024.
    err=Q(str(resid))+gamma(2048)*Q('100000')+Q('2e-7')
    check(resid<1e-7 and f2<100000 and np.max(np.abs(mat))<400, 'full proposed factor '+name)
    check(err.hi<Q('1e-6').lo,'certified reconstruction allowance '+name)
    fl[name]=dict(full_reconstruction_fro=resid,factor_squared_norm=f2,upper=err.json(),required='1e-6')
check((Q('.7793')-eta_a-Q('1e-6')).lo>Q('.779').hi,'finite Galerkin floor only')
check(sq(yn).lo>(Q('1.32')**2+Q('1e-6')).hi,'enlarged predictor norm')
check(sq(mz).lo>(Q('6.19')**2+Q('1e-6')).hi,'enlarged head LZ norm')
check(fro(aa@y-bb)<1e-9 and fro(y)<10 and fro(g)<10,'complete predictor residual and sizes')
check(fro(m0)<400 and fro(t0)<40 and fro(cov)<1 and fro(remote)<60 and fro(z)<23,'full transformation magnitudes')
check(sum(x['weighted_residual_fro']**2 for x in blocks)<3,'all finite weighted Gram squares <3')
hf=m0-.00024*np.eye(N)-(100/307)*(cov+.0046*np.eye(N))
rh=arrays['head_residual']; sol=arrays['head_solution']
hr=fro(rh-hf@sol)
check(fro(rh)<1 and fro(sol)<10,'head solve Frobenius magnitudes')
ha=(Q(str(fro(rh)))+Q('1e-7'))*(Q(str(hr))+Q('1e-8')*Q(str(fro(sol)))+Q('1e-7'))/Q('.239999')+Q('1e-7')
check(ha.hi<Q('1e-6').lo,'full head action operator and nuclear error')
# Frobenius conversions above have slack; avoid interpreting their last digit
# as an exact norm. Analytic transformations have a 1e-7/1e-6 error budget.
check((gamma(2048)*Q(400*23)*100).hi<Q('1e-6').lo,'100 coarse transformation roundoff charges fit trial budget')
check((gamma(K)*Q(3)+gamma(E*E)*Q(10)+Q('2e-6')).hi<Q('1e-5').lo,'Gram and trace error budget including head error')
cf=fro(arrays['full_covariance_upper'])
check(cf+1e-6<.951,'entire covariance Frobenius allowance <.951')
check(abs(cf-float(original['exact_predictor']['tilde_covariance_frobenius_upper']['hi'])+1e-6)<1e-12,'original whole covariance norm')
# Six-row squared-sum assembly: data and magnitudes are all read.
boundary=arrays['boundary_functionals']
check(boundary.shape==(6,E) and fro(boundary)<100,'complete six functionals and magnitude')
check(max(float(w.hi/SCALE) for w in weights)<.012 and sum(float(w.hi/SCALE) for w in weights)<.05,'six positive weight magnitudes')
check(trem.hi<Q('.002978927').lo and dk.lo>Q('10.9963070613268').hi,'uniform all-n tail bounds')
check(first['failures']==['factor reconstruction comparison_margin'],'preserved first pass has only failed comparison factor')
for n,h in pins.items():check(sha(BASE/n)==h,'original preserved '+n)
evidence.update(factor_reconstructions=fl,whole_covariance_frobenius=cf,
    head_action_error=ha.json(),finite_trace_expression=tf.json(),
    first_pass_failures=first['failures'],first_pass_interpretation='Inconclusive enclosure, not a negative actual reference direction.')
result=dict(scope='Conceptual audit of unchanged C999l N512/K65536 family',
    source_script_sha256=sha(Path(__file__)),original_hashes=pins,
    replay_artifacts=['neutral-head-covariance-replay-561.'+e for e in ('py','json','npz','log')],
    evidence=evidence,checks=checks,failures=failures,
    summary=dict(passed=not failures,required_lower='0',upheld_lower='.000999',
                 trial_error_upper=short(e_trial),finite_covariance_error_upper=short(e_f),
                 tail_remainder_upper=short(trem),exact_predictor_error_upper=short(eg)),
    runtime=dict(python=sys.version,numpy=np.__version__,platform=platform.platform()),
    qualifications=['Analytic response identity and IEEE754/Decimal contracts retained.',
       'Whole-core and unreplayed c_star qualifications retained.',
       'Finite endpoint family only; infinite endpoint complements, C744q, H2 and actual-Xi assembly open.'])
output=BASE/'neutral-head-covariance-audit-561.json'
output.write_text(json.dumps(result,indent=2)+'\n')
print('Checks:',len(checks),'failures:',failures)
print('Required >=0; upheld lower if analytic and arithmetic contracts hold: .000999')
print('Trial/finite/exact-predictor errors:',short(e_trial),short(e_f),short(eg))
print('Full covariance Frobenius:',cf,'required <.951')
print('Certificate:',output.relative_to(BASE.parent.parent))
assert not failures
