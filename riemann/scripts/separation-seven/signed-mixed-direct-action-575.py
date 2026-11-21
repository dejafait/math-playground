#!/usr/bin/env python3
"""Complete finite direct action, fixed mixed test562/step575.

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

iv = load('iv575', 'complete-schur-531.py')
iv.DOWN = Context(prec=80, rounding=ROUND_FLOOR)
iv.UP = Context(prec=80, rounding=ROUND_CEILING)
iv.NEAR = Context(prec=80, rounding=ROUND_HALF_EVEN)
I = iv.I
old = load('entries575', 'residual-certificate-532.py')
checks, failures, pins = [], [], {}

def check(ok, label):
    checks.append(dict(label=label, passed=bool(ok)))
    if not ok:
        failures.append(label)

def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(8*1024*1024), b''):
            h.update(chunk)
    return h.hexdigest()

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


# Reuse complete proved enclosures; inspect every prerequisite flag and pin.
audit=json.loads((BASE/'neutral-head-covariance-audit-561.json').read_text())
check(not audit['failures'] and all(c['passed'] for c in audit['checks']),
      'complete inherited audit561 check list')
for name in ['neutral-head-covariance-559.npz','complete-schur-531.py',
             'residual-certificate-532.py']:
    pins[name]=sha(BASE/name)
    check(pins[name]==audit['original_hashes'][name], 'unchanged audited '+name)
for number,stem in [(573,'signed-mixed-head-defect'),(574,'signed-mixed-complement-inverse')]:
    path=BASE/f'{stem}-{number}.json'
    rec=json.loads(path.read_text());pins[path.name]=sha(path)
    check(not rec['failures'] and all(c['passed'] for c in rec['checks']),
          f'complete prerequisite checks{number}')
    script_key='script_sha256' if number==573 else 'source_sha256'
    check(sha(BASE/f'{stem}-{number}.py')==rec[script_key],f'unchanged source{number}')
    name=f'{stem}-{number}.npz'
    target=rec['archive'] if number==573 else rec['archives'][name]
    pins[name]=sha(BASE/name)
    check(pins[name]==target['sha256'],f'complete interval archive pin{number}')
    for inherited in ['neutral-head-covariance-559.npz','complete-schur-531.py','residual-certificate-532.py']:
        check(rec['input_hashes'][inherited]==pins[inherited],
              f'same inherited input{number} '+inherited)
with np.load(BASE/'neutral-head-covariance-559.npz') as data:
    z,y,xhat=data['z'],data['predictor_free'],data['head_solution']
with np.load(BASE/'signed-mixed-head-defect-573.npz') as data:
    lhead=A(data['m_lower'],data['m_upper'])
with np.load(BASE/'signed-mixed-complement-inverse-574.npz') as data:
    b=A(data['b_lower'],data['b_upper'])
    k=A(data['frequencies_lower'],data['frequencies_upper'])
check(b.lo.shape==(K,) and k.lo.shape==(K,) and valid(b) and valid(k),
      'complete65536 scalar tables valid')
check(lhead.lo.shape==(N,N) and valid(lhead),'complete head L enclosure valid')
center_rec=json.loads((BASE/'signed-mixed-finite-center-572.json').read_text())
check(not center_rec['failures'] and all(c['passed'] for c in center_rec['checks']),
      'complete center572 check list')
wpath=BASE/'signed-mixed-columns-565.npy'
vpath=BASE/'signed-mixed-inverse-output-565.npy'
for path in [wpath,vpath]:pins[path.name]=sha(path)
check(pins[wpath.name]==center_rec['input_hashes'][wpath.name],
      'same entire W565 as the certified center572')
vrec=json.loads((BASE/'signed-mixed-complement-inverse-574.json').read_text())
check(pins[vpath.name]==vrec['input_hashes'][vpath.name],'same entire complementary inverse565')

pi,ell=16*atan(5)-4*atan(239),I(3).ln()/2
fourth=I(3).sqrt().sqrt()
indices=np.arange(K);parity=np.where(indices%2==0,1.,-1.)
# The pinned k table is an enclosure; explicitly verify the new constants fit it.
kfresh=ai(pi/ell)*A(indices)
check(np.all(kfresh.lo>=k.lo) and np.all(kfresh.hi<=k.hi),
      'same complete frequency enclosures')
ks=k*k
nu=A(np.full(K,down(float((2/ell).sqrt().lo))),
     np.full(K,up(float((2/ell).sqrt().hi))))
nu.set(0,ai((1/ell).sqrt()))
moments=[]
for c in [.5,-.5]:
    growth=ai(fourth if c>0 else 1/fourth)
    moments.append(nu*c*(parity*growth-1)/(c*c+ks))

remote=json.loads((BASE/'response-prefix-stop-546.json').read_text())
enumeration=[]
for prime in range(2,4000):
    if any(prime%j==0 for j in range(2,math.isqrt(prime)+1)):continue
    number=prime
    while number*number<3**15:
        if number*number>3**13:enumeration.append((number,prime))
        number*=prime
enumeration.sort()
check(len(enumeration)==334 and 4000**2>3**15 and
      enumeration==[(r['n'],r['prime']) for r in remote['remote']['primes']],
      'complete independent334 prime-power enumeration')
check(iv.prime_powers()==old.POWERS and len(old.POWERS)==16,
      'complete independent16 prime-power enumeration')

prime_records=[]
def aggregate(separation, powers):
    sp,sm=A(np.zeros(K)),A(np.zeros(K))
    dg=A(np.zeros(N))
    for number,prime in powers:
        weight=I(prime).ln()/I(number).sqrt()
        delta=separation*ell-I(number).ln()
        if separation==14 and number==2187:
            check(prime==3,'zero shift2187 retained as identity')
            dg=dg+ai(weight)
            prime_records.append(dict(separation=separation,n=number,prime=prime,
                                      sign=0,weight=weight.json(),delta={'lo':'0','hi':'0'}))
            continue
        sign=1 if delta.lo>0 else -1
        check((delta.lo>0 or delta.hi<0) and (sign*delta/ell).hi<1,
              f'nonzero interior delay{separation}/{number}')
        sn,cs=sincos(k*ai(delta),pi)
        check(valid(sn) and valid(cs),f'all trigonometric intervals{separation}/{number}')
        if sign>0:sp=sp+ai(weight)*sn
        else:sm=sm+ai(weight)*sn
        val=(1-ai(sign*delta/ell))*cs[:N]
        val.set(slice(1,None),val[1:]-sign*sn[1:N]/(ai(ell)*k[1:N]))
        dg=dg+ai(weight)*val
        prime_records.append(dict(separation=separation,n=number,prime=prime,
                                  sign=sign,weight=weight.json(),delta=delta.json()))
    return sp,sm,dg

agg7=aggregate(7,old.POWERS)
agg14=aggregate(14,enumeration)
print('Complete16/334 shift sums enclosed for all65536 modes',flush=True)

def pow_i(a,n):
    result=I(1)
    for _ in range(n):result*=a
    return result

continuous={}
for separation in [7,14]:
    terms=[]
    q=separation-1
    for j in range(1,8):
        c=2*j+.5
        decay=ai(1/(I(3**j)*fourth))
        minus=nu*c*(1-parity*decay)/(c*c+ks)
        plus=nu*c*(parity-decay)/(c*c+ks)
        prefactor=ai(1/(I(3**(q*j))*pow_i(fourth,q)))
        terms.append((minus,plus,prefactor))
    continuous[separation]=terms
    # C744z(23), exact complete operator remainder, starting j=8.
    tail=1/(I(3**(8*q))*pow_i(fourth,q)*I('16.5')*(1-I(1)/3**q))
    check(tail.hi<Decimal('1e-24'),f'complete continuous tail{separation}<1e-24')

def translation(rows, separation):
    sp,sm,dg=agg7 if separation==7 else agg14
    kn,km=k[rows,None],k[None,:N]
    den=ks[rows,None]-ks[None,:N]
    diagidx=np.diag_indices(N)
    if rows.start==0:den.set(diagidx,A(np.ones(N)))
    signs=parity[rows,None]*parity[None,:N]
    num=-signs*kn*sp[rows,None]+km*sp[None,:N]
    num=num+kn*sm[rows,None]-signs*km*sm[None,:N]
    adj=signs*kn*sm[rows,None]-km*sm[None,:N]
    adj=adj-kn*sp[rows,None]+signs*km*sp[None,:N]
    direct=num/den*nu[rows,None]*nu[None,:N]
    transpose=adj/den*nu[rows,None]*nu[None,:N]
    if rows.start==0:
        direct.set(diagidx,dg);transpose.set(diagidx,dg)
    for minus,plus,prefactor in continuous[separation]:
        direct=direct+prefactor*minus[rows,None]*plus[None,:N]
        transpose=transpose+prefactor*plus[rows,None]*minus[None,:N]
    return direct+A(-1e-24,1e-24),transpose+A(-1e-24,1e-24)

def local(rows):
    if rows.start==0:return lhead
    ss=(b[rows,None]-b[None,:N])/(ks[rows,None]-ks[None,:N])
    for j in range(64):
        c=2*j+.5
        ss=ss-ai(1/(I(3**j)*fourth))*parity[rows,None]*c*c/(
            (c*c+ks[rows,None])*(c*c+ks[None,:N]))
    ss=ss*(2*nu[rows,None]*nu[None,:N])*(parity[rows,None]==parity[None,:N])
    ss=ss+A(-1e-30,1e-30)
    return ss+256*(moments[0][rows,None]*moments[0][None,:N]
                 +moments[1][rows,None]*moments[1][None,:N])

u=I(1)/2**53
gamma=lambda n:n*u/(1-n*u)
zbound,ybound,mu=I('1.008'),I('1.320001'),I('.000999')
norms={name:fro_upper(a) for name,a in [('z',z),('y',y),('xhat',xhat)]}
vcenter=z@y+xhat
fv=fro_upper(vcenter)
# Full basis conversion, raw product, and addition to exact dyadic Xhat.
ev=I('1e-14')*ybound+gamma(1024)*(I(norms['z'])*I(norms['y'])+I(norms['xhat'])+1)
check(all(math.isfinite(f) for f in [*norms.values(),fv]) and norms['z']<23 and norms['y']<10,
      'complete head factor magnitudes')
outpath=BASE/'signed-mixed-direct-center-575.npy'
out=np.lib.format.open_memmap(outpath,mode='w+',dtype='float64',shape=(2,K,E))
blocks=[]
weighted_sq=I(0)
for start in range(0,K,N):
    rows=slice(start,start+N)
    ll=local(rows)
    tt,ts=translation(rows,7)
    uu,us=translation(rows,14)
    check(all(valid(a) for a in [ll,tt,ts,uu,us]),f'complete five rectangular enclosures{start}')
    matrices=[center_radius(a) for a in [ll,tt,ts,uu,us]]
    lc,tc,sc,uc,ac=[a[0] for a in matrices]
    el,et,es,eu,ea=[I(a[2]) for a in matrices]
    fl,ft,fs,fu,fa=[I(fro_upper(a[0])) for a in matrices]
    lz=lc@z
    df=np.hstack((lz,-ac@z))-sc@vcenter
    dh=np.hstack((-uc@z,lz))-tc@vcenter
    out[0,rows]=df;out[1,rows]=dh
    eentry=(2*el+eu+ea)*zbound+(et+es)*(I(fv)+ev)
    ebasis=(2*fl+fu+fa)*I('1e-14')+(ft+fs)*ev
    ear=gamma(4096)*((2*fl+fu+fa)*I(norms['z'])+(ft+fs)*I(fv)+1)
    q=eentry+ebasis+ear
    check(np.all(np.isfinite(df)) and np.all(np.isfinite(dh)),f'complete1020-column center rows{start}')
    ledger=dict(first=start,last=start+N-1,entries_per_operator=N*N,
        radius_fro={name:float(e.lo) for name,e in zip(['L','T','Tstar','U','Ustar'],[el,et,es,eu,ea])},
        center_fro={name:float(f.lo) for name,f in zip(['L','T','Tstar','U','Ustar'],[fl,ft,fs,fu,fa])},
        entry_error=eentry.json(),basis_and_raw_predictor_error=ebasis.json(),
        complete_product_rounding=ear.json(),combined_pair_error=q.json(),
        center_pair_sha256=hashlib.sha256(df.tobytes()+dh.tobytes()).hexdigest())
    if start==0:
        low_error=q
    else:
        dstart=(I(start)/(2*ell)).ln()-2*ell*ell/(9*start*start)
        check(dstart.lo>Decimal('6.14'),f'positive increasing weight{start}')
        weighted_sq+=q*q/dstart
        ledger['first_weight']=dstart.json()
    blocks.append(ledger)
    if start%8192==0:print('Complete direct interval rows through',start+N-1,flush=True)
out.flush()
alpha=(4/(3*I('6.14')*511**3)).sqrt()
raw_weighted=weighted_sq.sqrt()
low_weighted=alpha*low_error
mixed=(raw_weighted+low_weighted)/mu.sqrt()
check(len(blocks)==128 and [x['first'] for x in blocks]==list(range(0,K,N)),
      'all65536 raw rows and both1020-column orientations')
check(mixed.hi<Decimal('.00001'),'complete normalized direct-action error below .00001')
archive=BASE/'signed-mixed-direct-action-575.npz'
np.savez_compressed(archive,vcenter=vcenter,
    s7_lower=agg7[0].lo,s7_upper=agg7[0].hi,t7_lower=agg7[1].lo,t7_upper=agg7[1].hi,
    diag7_lower=agg7[2].lo,diag7_upper=agg7[2].hi,
    s14_lower=agg14[0].lo,s14_upper=agg14[0].hi,t14_lower=agg14[1].lo,t14_upper=agg14[1].hi,
    diag14_lower=agg14[2].lo,diag14_upper=agg14[2].hi)
record=dict(parameters=dict(N=N,K=K,endpoint_dimension=E),
    certified_direct_component_under_inherited_contracts=not failures,
    exact_finite_covariance_certified=False,quarter_decided=False,
    required_direct_component_upper='.00001',prior_direct_and_fft_allowance='.002646',
    remaining_after_reserving_direct_component='.002636',
    source_sha256=sha(Path(__file__)),input_hashes=pins,
    archives={p.name:dict(path=str(p.relative_to(BASE.parent.parent)),sha256=sha(p)) for p in [outpath,archive]},
    full_factor_norms={**norms,'vcenter':fv},
    scalars={name:a.json() for name,a in [('raw_predictor_center_error',ev),('low_pair_error',low_error),
        ('weighted_raw_tail_error',raw_weighted),('weighted_low_error',low_weighted),
        ('normalized_direct_error',mixed)]},
    complete_prime_records=prime_records,blocks=blocks,checks=checks,failures=failures,
    unresolved=['finite exact T/Tstar action on Vhat_c versus Dhat-W565',
                'Sections12-16 independent audits','complement coercivity and global gaps'])
path=BASE/'signed-mixed-direct-action-575.json'
path.write_text(json.dumps(record,indent=2)+'\n')
print('Checks:',len(checks),'failures:',failures,flush=True)
print('Normalized direct error upper:',mixed.hi,'; required <.00001; remainder .002636',flush=True)
print('Certificate:',path.relative_to(BASE.parent.parent),'arrays:',outpath.relative_to(BASE.parent.parent),
      archive.relative_to(BASE.parent.parent),flush=True)
