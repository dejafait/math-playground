#!/usr/bin/env python3
"""Complete head-inverse defect payment, fixed mixed test562.

Outward binary64 intervals for explicit finite entries; Decimal constants.
The covered digamma remainder and complete series tails are retained.
No FFT accuracy assumption, inverse/eigenvalue oracle, or parameter search.
"""
import hashlib
import importlib.util
import json
import math
from decimal import Context, Decimal, ROUND_CEILING, ROUND_FLOOR, ROUND_HALF_EVEN
from pathlib import Path
import numpy as np

BASE = Path(__file__).resolve().parent
N, E, SHIFT, DIAG_CUTOFF = 512, 1020, 4096, 65536

def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, BASE/filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

iv = load('iv573', 'complete-schur-531.py')
iv.DOWN = Context(prec=80, rounding=ROUND_FLOOR)
iv.UP = Context(prec=80, rounding=ROUND_CEILING)
iv.NEAR = Context(prec=80, rounding=ROUND_HALF_EVEN)
I = iv.I
old = load('entries573', 'residual-certificate-532.py')
checks, failures, pins = [], [], {}

def check(ok, label):
    checks.append(dict(label=label, passed=bool(ok)))
    if not ok:
        failures.append(label)

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def down(x):
    return np.nextafter(x, -np.inf)

def up(x):
    return np.nextafter(x, np.inf)

class A:
    """Closed array intervals, each basic operation rounded outwards."""
    __array_priority__ = 1000
    def __init__(self, lo, hi=None):
        self.lo = np.asarray(lo, dtype=np.float64)
        self.hi = self.lo.copy() if hi is None else np.asarray(hi, dtype=np.float64)
    @staticmethod
    def cast(x):
        return x if isinstance(x, A) else A(x)
    def __add__(self, x):
        x = A.cast(x)
        return A(down(self.lo+x.lo), up(self.hi+x.hi))
    __radd__ = __add__
    def __neg__(self):
        return A(-self.hi, -self.lo)
    def __sub__(self, x):
        return self+-A.cast(x)
    def __rsub__(self, x):
        return A.cast(x)+-self
    def __mul__(self, x):
        x = A.cast(x)
        products = [a*b for a in (self.lo,self.hi) for b in (x.lo,x.hi)]
        return A(down(np.minimum.reduce(products)), up(np.maximum.reduce(products)))
    __rmul__ = __mul__
    def __truediv__(self, x):
        x = A.cast(x)
        assert np.all((x.lo > 0) | (x.hi < 0))
        return self*A(down(1/x.hi),up(1/x.lo))
    def __rtruediv__(self, x):
        return A.cast(x)/self
    def __getitem__(self, key):
        return A(self.lo[key], self.hi[key])
    def set(self, key, x):
        x = A.cast(x)
        self.lo[key],self.hi[key] = x.lo,x.hi

def ai(x):
    return A(down(float(x.lo)),up(float(x.hi)))

def atan(q):
    x=I(1)/q
    power,total=x,I(0)
    for j in range(80):
        total += (-1)**j*power/(2*j+1)
        power *= x*x
    return total+I(-power.hi,power.hi)/161

def fro_upper(x):
    # Positive summation, including multiplication and one final sqrt.
    x=np.asarray(x)
    gamma=(x.size+2)*2.0**-53/(1-(x.size+2)*2.0**-53)
    total=up(np.sum(up(x*x))/(1-gamma))
    return float(up(np.sqrt(total)))

def center_radius(a):
    center=a.lo+(a.hi-a.lo)/2
    radius=up(np.maximum(np.abs(center-a.lo),np.abs(a.hi-center)))
    return center,radius,fro_upper(radius)

def positive_sum(a, axis):
    assert np.all(a.lo >= 0)
    count=a.lo.shape[axis]
    gamma=(count+2)*2.0**-53/(1-(count+2)*2.0**-53)
    return A(down(np.sum(a.lo,axis=axis)/(1+gamma)),
             up(np.sum(a.hi,axis=axis)/(1-gamma)))

def sincos(x, pi):
    q=np.rint(((x.lo+x.hi)/2)/(float(pi.lo)/2)).astype(np.int64)
    r=x-A(q)*ai(pi/2)
    assert np.max(np.maximum(abs(r.lo),abs(r.hi))) < .786
    r2=r*r
    sn,cs,ts,tc=r,A(np.ones_like(q)),r,A(np.ones_like(q))
    for j in range(1,11):
        ts=-ts*r2/((2*j)*(2*j+1))
        tc=-tc*r2/((2*j-1)*(2*j))
        sn,cs=sn+ts,cs+tc
    # Taylor tails on |r|<.786 are both <1e-21.
    sn=sn+A(-1e-21,1e-21)
    cs=cs+A(-1e-21,1e-21)
    sine,cosine=A(np.zeros_like(q)),A(np.zeros_like(q))
    for quadrant,s,c in [(0,sn,cs),(1,cs,-sn),(2,-sn,-cs),(3,-cs,sn)]:
        mask=q%4==quadrant
        sine.set(mask,s[mask]);cosine.set(mask,c[mask])
    return sine,cosine

audit=json.loads((BASE/'neutral-head-covariance-audit-561.json').read_text())
check(not audit['failures'] and all(c['passed'] for c in audit['checks']),
      'inherited complete audit561 check list')
for name in ['neutral-head-covariance-559.npz','complete-schur-531.py',
             'complete-covariance-532.npz','residual-certificate-532.py']:
    pins[name]=sha(BASE/name)
    check(pins[name]==audit['original_hashes'][name], 'unchanged audited '+name)
with np.load(BASE/'neutral-head-covariance-559.npz') as data:
    z,y,xhat,mc=data['z'],data['predictor_free'],data['head_solution'],data['comparison_lower']
with np.load(BASE/'complete-covariance-532.npz') as data:
    m_old,cov=data['m0'],data['cov00']

pi,ell=16*atan(5)-4*atan(239),I(3).ln()/2
fourth=I(3).sqrt().sqrt()
ii=np.arange(N)
parity=np.where(ii%2==0,1.,-1.)
k=ai(pi/ell)*A(ii)
ks=k*k
nu=A(np.full(N,float((2/ell).sqrt().lo)))
nu.lo[:]=float(down(float((2/ell).sqrt().lo)))
nu.hi= np.full(N,float(up(float((2/ell).sqrt().hi))))
nu.set(0,ai((1/ell).sqrt()))

# Same cited recurrence/remainder, evaluated at a more distant point.
yy=k/2
a=SHIFT+.25
den=A(a*a)+yy*yy
t=yy/a
assert np.max(t.hi)<.36
power=t
arg=A(np.zeros(N))
for j in range(100):
    arg=arg+((-1)**j)*power/(2*j+1)
    power=power*t*t
arg=arg+A(-1e-88,1e-88)  # .36^201/201 <1e-88
imag=arg+yy/(2*den)
loglo,loghi=[],[]
for j in range(N):
    loginterval=I(float(den.lo[j]),float(den.hi[j])).ln()/2
    loglo.append(down(float(loginterval.lo)))
    loghi.append(up(float(loginterval.hi)))
real=A(loglo,loghi)-a/(2*den)-ai(pi.ln())
for j in range(SHIFT):
    dj=(j+.25)**2+yy*yy
    imag=imag+yy/dj
    real=real-(j+.25)/dj
remainder=ai(I(2).sqrt())/(6*den)
imag=imag+A(-remainder.hi,remainder.hi)
real=real+A(-remainder.hi,remainder.hi)
b=k*imag/2
b.set(0,A(0.))
print('Complete4096-step digamma enclosures for512 modes',flush=True)

# Response diagonal: full65536-term positive sum plus covered remainder.
diag=A(np.zeros(N))
for start in range(0,DIAG_CUTOFF,1024):
    c=A(2*np.arange(start,start+1024)+.5)
    c2=c*c
    dd=c2[None,:]+ks[:,None]
    diag=diag+positive_sum(c2[None,:]/(dd*dd),axis=1)
cj=2*DIAG_CUTOFF+.5
diag=diag+1/(2*A(cj))
diagerr=1/(A(cj)*cj)+2*ks*(1/(6*A(cj)*cj*cj)+1/(A(cj)*cj*cj*cj))
diag=diag+A(-diagerr.hi,diagerr.hi)

denom=ks[:,None]-ks[None,:]
diagidx=np.diag_indices(N)
denom.set(diagidx,A(np.ones(N)))
response=(b[:,None]-b[None,:])/denom
response.set(diagidx,diag)
for j in range(64):
    c=2*j+.5
    response=response-ai(I(1)/(I(3**j)*fourth))*parity[:,None]*c*c/((c*c+ks[:,None])*(c*c+ks[None,:]))
response=response*(2*nu[:,None]*nu[None,:])*A(parity[:,None]==parity[None,:])
# Exponential response tail is <1e-30 in every entry.
response=response+A(-1e-30,1e-30)
moments=[]
for c in [.5,-.5]:
    growth=ai(fourth if c>0 else 1/fourth)
    moments.append(nu*c*(parity*growth-1)/(c*c+ks))
mm=response+256*(moments[0][:,None]*moments[0][None,:]+moments[1][:,None]*moments[1][None,:])
mm.set(diagidx,mm[diagidx]+real)
print('Complete response/diagonal/penalty head intervals',flush=True)

tt=A(np.zeros((N,N)))
for number,prime in old.POWERS:
    delta=7*ell-I(number).ln()
    weight=I(prime).ln()/I(number).sqrt()
    sn,cs=sincos(k*ai(delta),pi)
    signs=parity[:,None]*parity[None,:]
    if delta.lo>0:
        numerator=-signs*k[:,None]*sn[:,None]+k[None,:]*sn[None,:]
        sign=1
    else:
        assert delta.hi<0
        numerator=k[:,None]*sn[:,None]-signs*k[None,:]*sn[None,:]
        sign=-1
    entry=numerator/denom
    length=ai(ell-sign*delta)
    values=A(np.zeros(N))
    values.set(0,length)
    values.set(slice(1,None),length*cs[1:]/2-sign*sn[1:]/(2*k[1:]))
    entry.set(diagidx,values)
    tt=tt+ai(weight)*entry*nu[:,None]*nu[None,:]
for j in range(1,8):
    c=2*j+.5
    decay=ai(I(1)/(I(3**j)*fourth))
    minus=nu*c*(1-parity*decay)/(c*c+ks)
    plus=nu*c*(parity-decay)/(c*c+ks)
    prefactor=ai(1/(I(3**(6*j+1))*I(3).sqrt()))
    tt=tt+prefactor*minus[:,None]*plus[None,:]
# Full continuous tail norm<1e-24 hence each entry obeys the same bound.
tt=tt+A(-1e-24,1e-24)
hh=A(m_old)-ai(I('.00024'))*np.eye(N)-ai(I(100)/307)*(A(cov)+ai(I('.0046'))*np.eye(N))
m,rm,em=center_radius(mm)
t,rt,et=center_radius(tt)
h,rh,eh=center_radius(hh)
check(all(np.all(np.isfinite(a)) for a in [m,t,h,rm,rt,rh]),'all complete head interval endpoints finite')
check(all(np.all(a.lo<=a.hi) for a in [mm,tt,hh]),'all complete head interval orders')

g=z@y
rho=np.hstack((t@z,t.T@z))-m@g
defect=rho-h@xhat
norms={name:fro_upper(value) for name,value in [('m',m),('t',t),('h',h),('z',z),('y',y),('xhat',xhat),('g',g),('rho',rho),('defect',defect)]}
check(norms['z']<23 and norms['y']<10 and norms['xhat']<10 and norms['g']<10,
      'complete saved-factor Frobenius magnitudes')
u=I(1)/2**53
gamma=lambda n:n*u/(1-n*u)
# Includes g formation, two T products, m*g, h*xhat, and additions.
arithmetic=gamma(4096)*(I(2).sqrt()*I(norms['t'])*I(norms['z'])+
    I(norms['m'])*I(norms['z'])*I(norms['y'])+I(norms['h'])*I(norms['xhat'])+I(1))
check(arithmetic.hi<Decimal('1e-7'),'whole defect matrix arithmetic below1e-7')
zerr=I('1e-14')
basis=(I(2).sqrt()*I('4.71')+(I(norms['m'])+I(em))*I('1.320001'))*zerr
defect_error=I(2).sqrt()*I(et)*I('1.008')+I(em)*I('1.008')*I('1.320001')+I(eh)*I(norms['xhat'])+basis+arithmetic

# The crude defect/.239999 attempt is retained as floor-failure573.
# Verify the actual proposed correction, with the SAME exact H and Xhat.
# This is another inverse error proof, not a predictor or budget change.
correction=np.linalg.solve(h,defect)
correction_residual=defect-h@correction
correction_norm=fro_upper(correction)
correction_residual_norm=fro_upper(correction_residual)
correction_arithmetic=gamma(2048)*(I(norms['h'])*I(correction_norm)+I(norms['defect'])+I(1))
correction_error=(I(correction_residual_norm)+I(eh)*I(correction_norm)+correction_arithmetic)/I('.239999')
q=I('.0005')
scaled=correction/float(q.lo)
gram=scaled.T@scaled
target=float(1)*mc-gram-1e-6*np.eye(E)
factor=np.empty((0,0))
factor_ledger=dict(proposed=False)
try:
    factor=np.linalg.cholesky(target)
    residual=fro_upper(target-factor@factor.T)
    fsq=fro_upper(factor)**2
    maximum=max(float(np.max(np.abs(a))) for a in [gram,mc,target,factor])
    factor_ledger=dict(proposed=True,residual_fro=residual,factor_squared_fro=fsq,maximum_entry=maximum,scaled_correction_fro=fro_upper(scaled))
    check(residual<1e-7 and fsq<100000 and maximum<400 and fro_upper(scaled)<10,
          'complete normalized-correction factor and magnitudes')
except np.linalg.LinAlgError:
    check(False,'complete normalized-correction factor and magnitudes')
factor_error=I('1e-7')+gamma(2048)*100000+I('2e-7')+gamma(2048)*100
check(factor_error.hi<I('1e-6').lo,'restored factor margin pays Gram/scaling/reconstruction')
inverse_error=q+(defect_error/I('.239999')+correction_error)/I('.000999').sqrt()
zeta=(1/I('6.14')+4/(3*I('6.14')*511**3)).sqrt()
mixed_head=zeta*I(2).sqrt()*I('4.71')*inverse_error
check(mixed_head.hi<Decimal('.002'),'complete head-inverse contribution below .002')

archive=BASE/'signed-mixed-head-defect-573.npz'
np.savez_compressed(archive,m_lower=mm.lo,m_upper=mm.hi,t_lower=tt.lo,t_upper=tt.hi,
    h_lower=hh.lo,h_upper=hh.hi,m_center=m,t_center=t,h_center=h,m_radius=rm,t_radius=rt,h_radius=rh,
    exact_proxy_head_residual_center=rho,head_solution=xhat,defect=defect,correction=correction,
    correction_residual=correction_residual,scaled_correction_gram=gram,
    comparison=mc,factor=factor)
scalars=dict(head_matrix_error=I(em),cross_matrix_error=I(et),reference_matrix_error=I(eh),
    complete_matrix_arithmetic=arithmetic,exact_basis_error=basis,complete_defect_error=defect_error,
    correction_residual_norm=I(correction_residual_norm),correction_arithmetic=correction_arithmetic,
    complete_correction_solve_error=correction_error,normalized_inverse_error=inverse_error,
    mixed_head_contribution=mixed_head,full_factor_error=factor_error)
record=dict(parameters=dict(N=N,K=65536,endpoint_dimension=E,recurrence_shift=SHIFT,diagonal_cutoff=DIAG_CUTOFF),
    scope='Complete head inverse error relative to unchanged dyadic Xhat, exact proxy ZYhat; both mixed T orientations and all free input modes',
    certified_head_contribution_under_inherited_contracts=not failures,exact_finite_covariance_certified=False,
    actual_quarter_decided=False,input_hashes=pins,script_sha256=sha(Path(__file__)),
    archive=dict(path=str(archive.relative_to(BASE.parent.parent)),sha256=sha(archive)),
    complete_interval_entry_counts=dict(m=N*N,t=N*N,h=N*N),complete_matrix_norms=norms,
    factor=factor_ledger,scalars={key:value.json() for key,value in scalars.items()},
    required_total_exact_map_error='.004204',sought_head_component_upper='.002',
    checks=checks,failures=failures,
    unresolved=['Other finite direct-entry/basis errors','Complementary inverse diagonal/entry errors',
                'FFT proposal connection','Section12/13 and new result audit','Complement sign and all global qualifications'])
path=BASE/'signed-mixed-head-defect-573.json'
path.write_text(json.dumps(record,indent=2)+'\n')
print('Checks:',len(checks),'failures:',failures,flush=True)
print('Head contribution candidate upper (valid only if all checks pass):',mixed_head.hi,'; sought <.002; total required <=.004204',flush=True)
print('Certificate:',path.relative_to(BASE.parent.parent),'arrays:',archive.relative_to(BASE.parent.parent),flush=True)
