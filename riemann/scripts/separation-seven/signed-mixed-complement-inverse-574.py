#!/usr/bin/env python3
"""Complete complementary inverse accuracy, fixed mixed test562/step574.

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
N, E, SHIFT, K = 512, 1020, 4096, 65536

def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, BASE/filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

iv = load('iv574', 'complete-schur-531.py')
iv.DOWN = Context(prec=80, rounding=ROUND_FLOOR)
iv.UP = Context(prec=80, rounding=ROUND_CEILING)
iv.NEAR = Context(prec=80, rounding=ROUND_HALF_EVEN)
I = iv.I
old = load('entries574', 'residual-certificate-532.py')
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

def sqrt_a(x):
    assert np.all(x.lo >= 0)
    return A(down(np.sqrt(x.lo)), up(np.sqrt(x.hi)))

def valid(a):
    return bool(np.all(np.isfinite(a.lo)) and np.all(np.isfinite(a.hi))
                and np.all(a.lo <= a.hi))

audit=json.loads((BASE/'neutral-head-covariance-audit-561.json').read_text())
check(not audit['failures'] and all(c['passed'] for c in audit['checks']),
      'complete inherited audit561 check list')
for name in ['neutral-head-covariance-559.npz','complete-schur-531.py',
             'residual-certificate-532.py']:
    pins[name]=sha(BASE/name)
    check(pins[name]==audit['original_hashes'][name], 'unchanged audited '+name)
with np.load(BASE/'neutral-head-covariance-559.npz') as data:
    z,y=data['z'],data['predictor_free']
g=z@y
norms={key:fro_upper(value) for key,value in [('z',z),('y',y),('g',g)]}
check(norms['z']<23 and norms['y']<10 and norms['g']<10,
      'full saved factor Frobenius magnitudes')
vpath=BASE/'signed-mixed-inverse-output-565.npy'
pins[vpath.name]=sha(vpath)
vhat=np.load(vpath,mmap_mode='r')
check(vhat.shape==(K,E) and np.all(vhat[:N]==0),'entire original565 inverse shape and zero head')

pi,ell=16*atan(5)-4*atan(239),I(3).ln()/2
fourth=I(3).sqrt().sqrt()
indices=np.arange(K)
parity=np.where(indices%2==0,1.,-1.)
k=ai(pi/ell)*A(indices)
ks=k*k
nu=A(np.full(K,down(float((2/ell).sqrt().lo))),
     np.full(K,up(float((2/ell).sqrt().hi))))
nu.set(0,ai((1/ell).sqrt()))
yy=k/2
aa=SHIFT+.25
den=A(aa*aa)+yy*yy
t=yy/aa
for j in range(5):
    t=t/(1+sqrt_a(1+t*t))
check(float(np.max(t.hi))<.05,'all half-angle arguments below .05')
power,arg=t,A(np.zeros(K))
for j in range(12):
    arg=arg+((-1)**j)*power/(2*j+1)
    power=power*t*t
# 32*.05**25/25 < 4e-33; valid also for tiny negative enclosures at zero.
imag=32*arg+A(-4e-33,4e-33)+yy/(2*den)
loglo,loghi=[],[]
for j in range(K):
    q=I(float(den.lo[j]),float(den.hi[j])).ln()/2
    loglo.append(down(float(q.lo)));loghi.append(up(float(q.hi)))
real=A(loglo,loghi)-aa/(2*den)-ai(pi.ln())
for j in range(SHIFT):
    dj=(j+.25)**2+yy*yy
    imag=imag+yy/dj
    real=real-(j+.25)/dj
remainder=ai(I(2).sqrt())/(6*den)
imag=imag+A(-remainder.hi,remainder.hi)
real=real+A(-remainder.hi,remainder.hi)
b=k*imag/2
b.set(0,A(0.))
check(valid(b) and valid(real) and np.min(real.lo[N:])>6.14,
      'all full digamma intervals finite and inverse diagonal positive')
print('Enclosed all65536 digamma values and diagonal reciprocals',flush=True)

moments=[]
for c in [.5,-.5]:
    growth=ai(fourth if c>0 else 1/fourth)
    moments.append(nu*c*(parity*growth-1)/(c*c+ks))
shifts=[]
for number,prime in old.POWERS:
    delta=7*ell-I(number).ln()
    weight=I(prime).ln()/I(number).sqrt()
    sn,cs=sincos(k*ai(delta),pi)
    check(valid(sn) and valid(cs),'complete prime trigonometric enclosures '+str(number))
    shifts.append((1 if delta.lo>0 else -1,ai(weight),sn))
continuous=[]
for j in range(1,8):
    c=2*j+.5
    decay=ai(1/(I(3**j)*fourth))
    minus=nu*c*(1-parity*decay)/(c*c+ks)
    plus=nu*c*(parity-decay)/(c*c+ks)
    prefactor=ai(1/(I(3**(6*j+1))*I(3).sqrt()))
    continuous.append((minus,plus,prefactor))
u=I(1)/2**53
gamma=lambda n:n*u/(1-n*u)
mu=I('.000999')
zeta=(1/I('6.14')+4/(3*I('6.14')*511**3)).sqrt()
archive=BASE/'signed-mixed-complement-inverse-574.npz'
diffpath=BASE/'signed-mixed-complement-inverse-difference-574.npy'
differences=np.lib.format.open_memmap(diffpath,mode='w+',dtype='float64',shape=(K-N,E))
blocks=[]
total_error_squared=I(0)
center_difference_squared=I(0)
rounding_squared=I(0)
entry_squared=I(0)
for start in range(N,K,N):
    rows=slice(start,start+N)
    kn,km=k[rows,None],k[None,:N]
    # Exact disjoint integer rectangle ensures this entire denominator positive.
    denominator=ks[rows,None]-ks[None,:N]
    ss=(b[rows,None]-b[None,:N])/denominator
    for j in range(64):
        c=2*j+.5
        ss=ss-ai(1/(I(3**j)*fourth))*parity[rows,None]*c*c/(
            (c*c+ks[rows,None])*(c*c+ks[None,:N]))
    ss=ss*(2*nu[rows,None]*nu[None,:N])*(parity[rows,None]==parity[None,:N])
    ss=ss+A(-1e-30,1e-30)
    ll=ss+256*(moments[0][rows,None]*moments[0][None,:N]
              +moments[1][rows,None]*moments[1][None,:N])
    tt,ts=A(np.zeros((N,N))),A(np.zeros((N,N)))
    signs=parity[rows,None]*parity[None,:N]
    for sign,weight,sn in shifts:
        if sign>0:
            direct=-signs*kn*sn[rows,None]+km*sn[None,:N]
            adjoint=-kn*sn[rows,None]+signs*km*sn[None,:N]
        else:
            direct=kn*sn[rows,None]-signs*km*sn[None,:N]
            adjoint=signs*kn*sn[rows,None]-km*sn[None,:N]
        tt=tt+weight*direct/denominator*nu[rows,None]*nu[None,:N]
        ts=ts+weight*adjoint/denominator*nu[rows,None]*nu[None,:N]
    for minus,plus,prefactor in continuous:
        tt=tt+prefactor*minus[rows,None]*plus[None,:N]
        ts=ts+prefactor*plus[rows,None]*minus[None,:N]
    tt=tt+A(-1e-24,1e-24);ts=ts+A(-1e-24,1e-24)
    check(all(valid(a) for a in [ll,tt,ts]),'all rectangular interval entries '+str(start))
    lc,lr,le=center_radius(ll)
    tc,tr,te=center_radius(tt)
    sc,sr,se=center_radius(ts)
    fl,ft,fs=map(fro_upper,[lc,tc,sc])
    rho=np.hstack((tc@z,sc@z))-lc@g
    fn=fro_upper(rho)
    # Exact Z,Yhat with dyadic rounded g. This bounds combined matrix products,
    # g formation, final subtraction, and their full Frobenius magnitudes.
    e_ar=gamma(4096)*((I(ft)+I(fs))*I(norms['z'])+
                    I(fl)*I(norms['z'])*I(norms['y'])+1)
    e_basis=((I(ft)+I(fs)+I(te)+I(se))+
             (I(fl)+I(le))*I('1.320001'))*I('1e-14')
    e_entry=(I(te)+I(se))*I('1.008')+I(le)*I('1.008')*I('1.320001')
    e_rho=e_entry+e_basis+e_ar
    reciprocal=2/real[rows]
    inv,inv_rad,_=center_radius(reciprocal)
    invmax=I(float(np.max(reciprocal.hi)))
    inv_error=I(float(np.max(inv_rad)))
    vc=inv[:,None]*rho
    diff=vc-np.array(vhat[rows])
    differences[start-N:start]=diff
    df=fro_upper(diff)
    vnorm=fro_upper(vhat[rows])
    # Two basic operations, subtraction included. gamma8 allows norm slack.
    e_scalar=gamma(8)*(invmax*I(fn)+I(vnorm)+1)
    e_complete=invmax*e_rho+inv_error*I(fn)+e_scalar
    block_bound=I(df)+e_complete
    total_error_squared+=block_bound*block_bound
    center_difference_squared+=I(df)*I(df)
    rounding_squared+=e_ar*e_ar
    entry_squared+=e_entry*e_entry
    check(bool(np.all(np.isfinite(diff))) and block_bound.hi<Decimal('.001'),
          'complete inverse difference bound '+str(start))
    blocks.append(dict(first=start,last=start+N-1,
        full_entry_count_each=N*N,
        matrix_radius_fro=dict(local=le,T=te,Tstar=se),
        matrix_center_fro=dict(local=fl,T=ft,Tstar=fs,residual=fn,old_inverse=vnorm),
        inverse_center_difference_fro=df,
        combined_difference_sha256=hashlib.sha256(diff.tobytes()).hexdigest(),
        exact_residual_entry_error=e_entry.json(),exact_basis_error=e_basis.json(),
        complete_product_rounding=e_ar.json(),inverse_max=invmax.json(),
        inverse_radius_max=inv_error.json(),complete_inverse_center_error=e_complete.json(),
        exact_block_difference_bound=block_bound.json()))
    if start%8192==0:
        print('Complete interval inverse rows through',start+N-1,flush=True)
differences.flush()
raw_error=total_error_squared.sqrt()
mixed=zeta*I(2).sqrt()*I('4.71')*raw_error/mu.sqrt()
check(len(blocks)==127 and blocks[0]['first']==512 and blocks[-1]['last']==65535,
      'all65024 complementary rows and1020 columns covered')
check(mixed.hi<Decimal('.0001'),'complete complementary inverse contribution below .0001')
np.savez_compressed(archive,b_lower=b.lo,b_upper=b.hi,h_lower=real.lo,h_upper=real.hi,
    frequencies_lower=k.lo,frequencies_upper=k.hi,
    prime_sines_lower=np.array([sn.lo for _,_,sn in shifts]),
    prime_sines_upper=np.array([sn.hi for _,_,sn in shifts]),
    comparison_input_hash=np.array(pins['neutral-head-covariance-559.npz']))
scalars=dict(raw_inverse_difference=raw_error,
    dyadic_center_difference_fro=center_difference_squared.sqrt(),
    combined_residual_arithmetic=rounding_squared.sqrt(),
    combined_residual_entry_error=entry_squared.sqrt(),
    neutral_tail_norm=zeta,normalized_mixed_contribution=mixed)
record=dict(parameters=dict(N=N,K=K,endpoint_dimension=E,recurrence_shift=SHIFT),
    certified_component_under_inherited_contracts=not failures,
    actual_quarter_decided=False,exact_finite_covariance_certified=False,
    required_component_upper='.0001',remaining_before_component='.002648',
    remaining_after_reserved_component='.002548',
    source_sha256=sha(Path(__file__)),input_hashes=pins,
    archives={p.name:dict(path=str(p.relative_to(BASE.parent.parent)),sha256=sha(p))
              for p in [archive,diffpath]},
    complete_factor_norms=norms,scalars={key:value.json() for key,value in scalars.items()},
    blocks=blocks,checks=checks,failures=failures,
    unresolved=['finite direct-map entries and basis','FFT-to-exact-operator connection',
      'Sections12-15 independent audits','complement coercivity and global gaps'])
path=BASE/'signed-mixed-complement-inverse-574.json'
path.write_text(json.dumps(record,indent=2)+'\n')
print('Checks:',len(checks),'failures:',failures,flush=True)
print('Mixed contribution upper (conditional on checks):',mixed.hi,
      '; required <.0001; prior remaining .002648',flush=True)
print('Certificate:',path.relative_to(BASE.parent.parent),'; arrays:',
      archive.relative_to(BASE.parent.parent),diffpath.relative_to(BASE.parent.parent),flush=True)

