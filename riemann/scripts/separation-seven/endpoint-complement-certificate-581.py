#!/usr/bin/env python3
"""Enclose one frozen variational obstruction under C999n's entry ledger.

No eigenvalue, inverse or FFT accuracy is used. Full arrays and vectors
are inspected; errors are one-sided in the correct variational direction.
"""
import hashlib
import importlib.util
import json
from decimal import Decimal
from pathlib import Path
import numpy as np
BASE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('interval581',BASE/'complete-schur-531.py')
a=importlib.util.module_from_spec(spec);spec.loader.exec_module(a)
I=a.I
checks=[]
def check(ok,label):
    checks.append(dict(label=label,passed=bool(ok)))
    if not ok: raise AssertionError(label)
def exact(x):return I(Decimal(float(x)))
def absmax(x):return max(x.lo.copy_abs(),x.hi.copy_abs())
def square(x):
    if x.lo<=0<=x.hi:return I(0,a.UP.multiply(absmax(x),absmax(x)))
    return x*x
def inflate(x,e):return x+I(absmax(e).copy_negate(),absmax(e))
def power(x,n):
    out=I(1)
    for _ in range(n):out*=x
    return out
def atan(q):
    x=I(1)/q
    return inflate(sum((((-1)**j)*power(x,2*j+1)/(2*j+1) for j in range(80)),I(0)),power(x,161)/161)
def l1(v):return sum((I(absmax(x)) for x in v),I(0))
def norm2(v):return sum((square(x) for x in v),I(0))
def dot_center(x,m,y):
    # Binary64 centers and standard dot contract; full signed product.
    value=exact(float(x@m@y))
    # C999n: ||m||_max<400 and each dimension<=1024. gamma_4096
    # times400 is <2e-10; 1e-8 safely covers both products.
    error=I('1e-8')*l1([exact(t) for t in x])*l1([exact(t) for t in y])
    return inflate(value,error)
archive=BASE/'endpoint-complement-locator-581.npz'
with np.load(archive) as z:
    data={key:z[key].copy() for key in z.files}
q=2**40
free=[I(int(v))/q for v in data['free_numerators']]
t=[I(int(v))/q for v in data['trial_numerators']]
tc=data['trial_numerators'].astype(float)/q
check(len(free)==1024 and len(t)==1024,'full frozen independent endpoints and trial')
check(any(v.lo!=0 for v in free),'nonzero frozen rational free vector')
pi=16*atan(5)-4*atan(239);ell=I(3).ln()/2
espec=importlib.util.spec_from_file_location('entriescheck581',BASE/'residual-certificate-532.py')
e=importlib.util.module_from_spec(espec);espec.loader.exec_module(e)
con=e.constants()
check(absmax(pi-I(e.PI_TEXT))<Decimal('1e-55'),'full stated pi decimal via Machin enclosure')
check(absmax(pi-exact(con['pi']))<Decimal('2e-16'),'binary64 pi bound')
check(absmax(ell-exact(con['ell']))<Decimal('1e-16'),'binary64 ell bound')
locator=json.loads((BASE/'endpoint-complement-locator-581.json').read_text())
check(locator['archive']['sha256']==hashlib.sha256(archive.read_bytes()).hexdigest(),'full locator archive pin')
check(locator['script_sha256']==hashlib.sha256((BASE/'endpoint-complement-locator-581.py').read_bytes()).hexdigest(),'locator source pin')
for name,digest in locator['input_hashes'].items():
    check(digest==hashlib.sha256((BASE/name).read_bytes()).hexdigest(),'input pin '+name)
with np.load(BASE/'complete-covariance-532.npz') as original:
    mh,ch=original['m0'],original['cov00']
    check(np.abs(mh).max()<400 and np.abs(ch).max()<400,'exact dyadic head input magnitudes')
    hproposal=mh-.00024*np.eye(512)-(100/307)*(ch+.0046*np.eye(512))
    check(np.array_equal(hproposal,data['reference_head']),'complete unchanged reference head assembly')
remote=json.loads((BASE/'response-prefix-stop-546.json').read_text())['remote']['primes']
check(len(remote)==334,'all334 remote weights')
wsum=I(0)
for row in remote:
    v,p=row['n'],row['prime']
    wi=I(p).ln()/I(v).sqrt()
    di=I(0) if v==2187 else 14*ell-I(v).ln()
    # Binary64 rounding of correctly evaluated80-digit constants.
    wc=exact(float(a.NEAR.divide(a.NEAR.add(wi.lo,wi.hi),Decimal(2))))
    dc=exact(float(a.NEAR.divide(a.NEAR.add(di.lo,di.hi),Decimal(2))))
    check(absmax(wi-wc)<Decimal('1e-16') and absmax(di-dc)<Decimal('1e-16'),'remote constant rounding '+str(v))
    wsum+=wi
check(wsum.hi<53,'remote full weight sum below53')
k=[n*pi/ell for n in range(1024)]
nu0=(1/ell).sqrt();nu=(2/ell).sqrt()
r=[(nu/(nu0 if n%2==0 else nu))*(I('.25')+square(k[n%2]))/(I('.25')+square(k[n])) for n in range(512,1024)]
raw=[]
for start in [0,512]:
    v=[I(0),I(0)]+free[start:start+512]
    for j,n in enumerate(range(512,1024)):
        v[n%2]-=r[j]*free[start+j]
    raw.append(v)
f,h=raw;fc,hc=data['raw_f_center'],data['raw_h_center']
df=sum((I(absmax(x-exact(y))) for x,y in zip(f,fc)),I(0))
dh=sum((I(absmax(x-exact(y))) for x,y in zip(h,hc)),I(0))
check(df.hi<Decimal('1e-12') and dh.hi<Decimal('1e-12'),'complete exact-neutral correction errors')
lf,lh,lt=l1(f),l1(h),l1(t)
# Every recorded approximate entry is finite and below400.
for key in ['local_matrix','t_entries','ts_entries','u_entries','reference_head','diagonal']:
    check(np.isfinite(data[key]).all() and np.abs(data[key]).max()<400,'full entry magnitude '+key)
L,T,Ts,U=data['local_matrix'],data['t_entries'],data['ts_entries'],data['u_entries']
H,D=data['reference_head'],data['diagonal']
endpoint_center=dot_center(fc,L,fc)+dot_center(hc,L,hc)-2*dot_center(hc,U,fc)
# Uniform full-entry errors: local .001, each cross operator .000001.
endpoint_error=I('.001')*(lf*lf+lh*lh)+2*I('.000001')*lf*lh
# Perturbation of low coordinates, including full matrix centers.
endpoint_error+=I(401)*(df*(2*lf+df)+dh*(2*lh+dh)+2*(df*lh+dh*lf+df*dh))
endpoint=inflate(endpoint_center,endpoint_error)
pair_center=dot_center(tc,T,fc)+dot_center(tc,Ts,hc)
pair_error=I('.000001')*lt*(lf+lh)+I(401)*lt*(df+dh)
pair=inflate(pair_center,pair_error)
head=dot_center(tc[:512],H,tc[:512])
# H exact rational assembly error1e-10, diagonal h/2 error<.0001/2.
ref_error=I('1e-10')*l1(t[:512])*l1(t[:512])+I('.00005')*norm2(t[512:])
tail=sum((exact(D[n])/2*square(t[n]) for n in range(512,1024)),I(0))
energy=inflate(head+tail,ref_error)
check(energy.lo>0,'strictly positive reference denominator')
quotient=square(pair)/energy
weights=[(n/(2*ell)).ln()-2*ell*ell/(9*n*n) for n in range(512,1024)]
wnorm=sum((weights[j%512]*square(free[j]) for j in range(1024)),I(0))
difference=endpoint-quotient-wnorm/4
check(difference.hi<Decimal('-.117'),'upper endpoint below-.117, required below0')
failures=[c['label'] for c in checks if not c['passed']]
result=dict(certified_under_inherited_contracts=True,independently_audited=False,
    checks=checks,failures=failures,
    scope='one exact rational-free neutral endpoint vector, full unchanged R inverse via finite variational trial',
    bounds={name:v.json() for name,v in dict(endpoint_energy=endpoint,
       trial_pairing=pair,reference_energy=energy,inverse_pairing_lower_quotient=quotient,
       weighted_free_norm_squared=wnorm,difference_upper_enclosure=difference,
       endpoint_entry_allowance=endpoint_error,forcing_pairing_allowance=pair_error,
       reference_allowance=ref_error,neutral_f_l1_error=df,neutral_h_l1_error=dh).items()},
    actual_upper=str(difference.hi),required_upper_strictly_below='0',
    enclosure_meaning='difference_upper_enclosure encloses the finite-trial upper expression, not F from below; only its upper endpoint bounds the original F-minus-quarter difference',
    limitation='Stops sufficient quarter comparison only; no actual triple negativity or RH conclusion; independent audit pending.',
    archive=dict(path=str(archive.relative_to(BASE.parent.parent)),sha256=hashlib.sha256(archive.read_bytes()).hexdigest()),
    script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
out=BASE/'endpoint-complement-certificate-581.json'
out.write_text(json.dumps(result,indent=2)+'\n')
print('Conditional certificate upper='+str(difference.hi)+'; required<0; failures='+str(failures))
print('Bounds: endpoint='+str(endpoint.hi)+'; inverse lower='+str(quotient.lo)+'; norm² lower='+str(wnorm.lo))
print('Full evidence='+str(out.relative_to(BASE.parent.parent))+'; arrays='+str(archive.relative_to(BASE.parent.parent)))
