#!/usr/bin/env python3
"""Complete direct finite T/T* products for C999m(71), fixed test562.

Reuse pinned575 interval helpers and complete prime aggregates. No FFT
accuracy assertion. All finite rows, both orientations and1020 columns.
"""
import hashlib
import json
import time
from decimal import Decimal
from pathlib import Path
import numpy as np

BASE = Path(__file__).resolve().parent
K, N, E, BLOCK = 65536, 512, 1020, 128
helper_path = BASE/'signed-mixed-direct-action-575.py'
helper_source = helper_path.read_text()
ns = {'__file__': str(helper_path), '__name__': 'helpers576'}
# Definitions and interval-context initialization only; no575 production run.
exec(compile(helper_source.split('# Reuse complete proved enclosures;')[0],
             str(helper_path), 'exec'), ns)
I, A, ai, atan = [ns[n] for n in ['I','A','ai','atan']]
fro_upper, center_radius, valid, sincos = [ns[n] for n in
    ['fro_upper','center_radius','valid','sincos']]
checks, failures, pins = [], [], {}

def check(ok, label):
    checks.append(dict(label=label, passed=bool(ok)))
    if not ok:
        failures.append(label)

def sha(path):
    h=hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda:stream.read(8*1024*1024),b''):
            h.update(chunk)
    return h.hexdigest()

def pin(name, expected=None):
    digest=sha(BASE/name)
    pins[name]=digest
    if expected is not None:
        check(digest==expected,'complete input pin '+name)
    return digest

records={}
for number, stem in [(572,'signed-mixed-finite-center'),
                     (574,'signed-mixed-complement-inverse'),
                     (575,'signed-mixed-direct-action')]:
    filename=f'{stem}-{number}.json'
    record=json.loads((BASE/filename).read_text())
    records[number]=record
    pin(filename)
    check(not record['failures'] and all(c['passed'] for c in record['checks']),
          f'all prerequisite{number} production flags')
    key='script_sha256' if number==572 else 'source_sha256'
    pin(f'{stem}-{number}.py',record[key])
    name=f'{stem}-{number}.npz'
    archive=record['archive'] if number==572 else record['archives'][name]
    pin(name,archive['sha256'])
for name in ['complete-schur-531.py','residual-certificate-532.py']:
    pin(name,records[575]['input_hashes'][name])
for name,expected in [
    ('signed-mixed-columns-565.npy',records[572]['input_hashes']['signed-mixed-columns-565.npy']),
    ('signed-mixed-inverse-output-565.npy',records[574]['input_hashes']['signed-mixed-inverse-output-565.npy']),
    ('signed-mixed-direct-center-575.npy',records[575]['archives']['signed-mixed-direct-center-575.npy']['sha256'])]:
    pin(name,expected)
check(records[575]['input_hashes']['signed-mixed-columns-565.npy']==pins['signed-mixed-columns-565.npy']
      and records[575]['input_hashes']['signed-mixed-inverse-output-565.npy']==pins['signed-mixed-inverse-output-565.npy'],
      'all unchanged dyadic references agree')
assert not failures, failures

v=np.array(np.load(BASE/'signed-mixed-inverse-output-565.npy',mmap_mode='r'))
dhat=np.load(BASE/'signed-mixed-direct-center-575.npy',mmap_mode='r')
what=np.load(BASE/'signed-mixed-columns-565.npy',mmap_mode='r')
check(v.shape==(K,E) and np.all(np.isfinite(v)) and np.all(v[:N]==0),
      'all inverse-center rows and zero head')
check(dhat.shape==what.shape==(2,K,E),'both full raw dyadic pair dimensions')
fv=I(fro_upper(v))
with np.load(BASE/'signed-mixed-direct-action-575.npz') as data:
    sp=A(data['s7_lower'],data['s7_upper'])
    sm=A(data['t7_lower'],data['t7_upper'])
with np.load(BASE/'signed-mixed-complement-inverse-574.npz') as data:
    k=A(data['frequencies_lower'],data['frequencies_upper'])
with np.load(BASE/'signed-mixed-finite-center-572.npz') as data:
    rhat=data['neutral_ratio_center']
    weights=data['upward_inverse_sqrt_weight']
check(all(valid(a) and a.lo.shape==(K,) for a in [sp,sm,k]),
      'all complete scalar aggregate enclosures')
check(rhat.shape==weights.shape==(K-N,) and np.all(np.isfinite(rhat))
      and np.all(np.isfinite(weights)) and np.all((weights>0)&(weights<.5)),
      'all pinned weighted neutral coordinates')

pi,ell=16*atan(5)-4*atan(239),I(3).ln()/2
fourth=I(3).sqrt().sqrt()
indices=np.arange(K,dtype=np.int64)
parity=np.where(indices%2==0,1.,-1.)
ks=k*k
nu=A(np.full(K,ns['down'](float((2/ell).sqrt().lo))),
     np.full(K,ns['up'](float((2/ell).sqrt().hi))))
nu.set(0,ai((1/ell).sqrt()))
kap2=ai((pi/ell)*(pi/ell))
diagonal=A(np.zeros(K))
for number,prime in ns['old'].POWERS:
    weight=I(prime).ln()/I(number).sqrt()
    delta=7*ell-I(number).ln()
    sign=1 if delta.lo>0 else -1
    check((delta.lo>0 or delta.hi<0) and (sign*delta/ell).hi<1,
          f'interior nonzero T delay{number}')
    sn,cs=sincos(k*ai(delta),pi)
    val=(1-ai(sign*delta/ell))*cs
    val.set(slice(1,None),val[1:]-sign*sn[1:]/(ai(ell)*k[1:]))
    diagonal=diagonal+ai(weight)*val
check(valid(diagonal),'all exact prime-translation diagonal cases')

# Continuous terms remain in factored form for direct complete dot products.
continuous=[]
for j in range(1,8):
    c=2*j+.5
    decay=ai(1/(I(3**j)*fourth))
    minus=nu*c*(1-parity*decay)/(c*c+ks)
    plus=nu*c*(parity-decay)/(c*c+ks)
    prefactor=ai(1/(I(3**(6*j+1))*I(3).sqrt()))
    continuous.append((prefactor*minus,plus))
continuous_tail=1/(I(3**49)*I(3).sqrt()*I('16.5')*(1-I(1)/3**6))
check(continuous_tail.hi<Decimal('1e-24'),'complete continuous operator tail')

u=I(1)/2**53
gamma=lambda n:n*u/(1-n*u)
start_time=time.monotonic()
apath=BASE/'signed-mixed-inverse-action-center-576.npy'
action=np.lib.format.open_memmap(apath,mode='w+',dtype='float64',shape=(2,K,E))
action[:]=0.
blocks=[]
radius_sq,center_sq=I(0),I(0)
for first in range(0,K,BLOCK):
    last=first+BLOCK
    rows=slice(first,last)
    nr=indices[rows,None]
    integer_den=(nr-indices[None,:])*(nr+indices[None,:])
    ii=np.arange(BLOCK); jj=indices[rows]
    integer_den[ii,jj]=1  # diagonal overwritten by its exact separate case
    den=kap2*A(integer_den)
    signs=parity[rows,None]*parity[None,:]
    kn,km=k[rows,None],k[None,:]
    num=-signs*kn*sp[rows,None]+km*sp[None,:]
    num=num+kn*sm[rows,None]-signs*km*sm[None,:]
    matrix=num/den*nu[rows,None]*nu[None,:]
    matrix.set((ii,jj),diagonal[rows])
    check(valid(matrix),f'every finite T entry{first}:{last-1}')
    center,radius,er=center_radius(matrix)
    fc=fro_upper(center)
    radius_sq+=I(er)*I(er)
    center_sq+=I(fc)*I(fc)
    # side0 is T*V, side1 is TV. Every dot uses all K entries;
    # transpose block contributions cover the full K-term dot in order.
    action[1,rows]=center@v
    if first>=N:
        action[0]+=center.T@v[rows]
    blocks.append(dict(first=first,last=last-1,entry_count=BLOCK*K,
        radius_fro=er,center_fro=fc,
        matrix_center_sha256=hashlib.sha256(center.tobytes()).hexdigest(),
        direct_action_block_sha256=hashlib.sha256(np.asarray(action[1,rows]).tobytes()).hexdigest()))
    if first%2048==0:
        print('Complete direct matrix/products through',last-1,
              'seconds',round(time.monotonic()-start_time,1),flush=True)
    del matrix,num,den,center,radius,signs,kn,km,integer_den

# Treat seven exact finite continuous rank-one products. Enclose factor
# conversion and all K-term dot products, scalar multiplications/additions.
continuous_error=I(0)
continuous_magnitude=I(0)
continuous_records=[]
for j,(a,b) in enumerate(continuous,1):
    ac,ar,ea=center_radius(a)
    bc,br,eb=center_radius(b)
    fa,fb=I(fro_upper(ac)),I(fro_upper(bc))
    ea,eb=I(ea),I(eb)
    entry=ea*(fb+eb)+fa*eb
    rounding=gamma(2*K+32)*(fa*fb*fv+1)
    q=entry*fv+rounding
    direct=bc@v
    adjoint=ac@v
    action[1]+=ac[:,None]*direct[None,:]
    action[0]+=bc[:,None]*adjoint[None,:]
    continuous_error+=q
    continuous_magnitude+=fa*fb
    continuous_records.append(dict(j=j,a_center_fro=fa.json(),b_center_fro=fb.json(),
        a_radius_fro=ea.json(),b_radius_fro=eb.json(),operator_entry_error=entry.json(),
        product_rounding=rounding.json(),one_orientation_error=q.json()))
    print('Complete continuous rank-one action',j,flush=True)

fc_total=center_sq.sqrt()
entry_error=radius_sq.sqrt()*fv
# Covers full K-term direct dots, all transpose block dots and additions,
# as well as subsequent addition of all seven continuous products.
product_rounding=gamma(2*K+32)*(fc_total*fv+1)
continuous_addition=gamma(32)*((fc_total+continuous_magnitude)*fv+1)
one_action_error=entry_error+product_rounding+continuous_error+continuous_addition+continuous_tail*fv
pair_action_error=I(2).sqrt()*one_action_error
action.flush()
check(len(blocks)==K//BLOCK and sum(b['entry_count'] for b in blocks)==K*K,
      'entire65536-square T matrix and both full products')

# Exact dyadic target is Dhat-What. Pay both subtraction roundings.
# Use the audited upward weights572; this dominates the true weighted norm.
weighted_sq=I(0)
subtraction_sq=I(0)
coordinate_sq=I(0)
diffpath=BASE/'signed-mixed-inverse-action-difference-576.npy'
differences=np.lib.format.open_memmap(diffpath,mode='w+',dtype='float64',shape=(2,K,E))
diffblocks=[]
low=[]
lowerror=[]
for side in range(2):
    aa=np.array(action[side,:2]); dd=np.array(dhat[side,:2]); ww=np.array(what[side,:2])
    delta=aa-(dd-ww)
    differences[side,:2]=delta
    low.append(delta)
    lowerror.append(gamma(8)*(I(fro_upper(aa))+I(fro_upper(dd))+I(fro_upper(ww))+1))
for first in range(N,K,BLOCK):
    rows=slice(first,first+BLOCK)
    pos=slice(first-N,first+BLOCK-N)
    pp=indices[rows]%2
    for side in range(2):
        aa=np.array(action[side,rows]);dd=np.array(dhat[side,rows]);ww=np.array(what[side,rows])
        delta=aa-(dd-ww)
        differences[side,rows]=delta
        qsub=gamma(8)*(I(fro_upper(aa))+I(fro_upper(dd))+I(fro_upper(ww))+1)
        subtraction_sq+=qsub*qsub
        repeated=low[side][pp]
        weighted=(delta-rhat[pos,None]*repeated)*weights[pos,None]
        fw=I(fro_upper(weighted));fd=I(fro_upper(delta));fl=I(fro_upper(repeated))
        qcoord=I('.5')*(I('1e-20')*fl+gamma(16)*(fd+I('1e-5')*fl+1))
        weighted_sq+=fw*fw
        coordinate_sq+=qcoord*qcoord
        check(np.all(np.isfinite(delta)) and np.all(np.isfinite(weighted)),
              f'complete neutral difference{side}/{first}')
        diffblocks.append(dict(side=side,first=first,last=first+BLOCK-1,
            difference_fro=fd.json(),repeated_low_fro=fl.json(),
            weighted_center_fro=fw.json(),subtraction_error=qsub.json(),
            coordinate_error=qcoord.json(),
            difference_sha256=hashlib.sha256(delta.tobytes()).hexdigest()))
# Nonused head rows are stored too for a complete raw difference array.
for side in range(2):
    differences[side,2:N]=action[side,2:N]-(dhat[side,2:N]-what[side,2:N])
differences.flush()

mu=I('.000999')
zeta=(1/I('6.14')+4/(3*I('6.14')*511**3)).sqrt()
alpha=(4/(3*I('6.14')*511**3)).sqrt()
low_sub_error=(lowerror[0]*lowerror[0]+lowerror[1]*lowerror[1]).sqrt()
subtraction_error=I('.5')*subtraction_sq.sqrt()+alpha*low_sub_error
coordinate_error=coordinate_sq.sqrt()
weighted_center=weighted_sq.sqrt()
eta=(weighted_center+subtraction_error+coordinate_error+zeta*pair_action_error)/mu.sqrt()
check(eta.hi<=Decimal('.002645'),'complete normalized inverse-action error <=.002645')
rawerror=entry_error+product_rounding+continuous_error+continuous_addition+continuous_tail*fv
scalars=dict(inverse_center_fro=fv,finite_translation_radius=radius_sq.sqrt(),
    finite_translation_center_fro=fc_total,one_action_entry_error=entry_error,
    one_action_product_rounding=product_rounding,one_action_continuous_error=continuous_error,
    one_action_continuous_addition=continuous_addition,
    continuous_tail_operator=continuous_tail,pair_action_error=pair_action_error,
    weighted_difference_center_fro=weighted_center,weighted_subtraction_error=subtraction_error,
    weighted_coordinate_error=coordinate_error,neutral_norm=zeta,
    normalized_inverse_action_error=eta)
output=dict(parameters=dict(K=K,N=N,E=E,block=BLOCK),
    component_certified_under_inherited_contracts=not failures,
    exact_finite_covariance_certified=False,quarter_decided=False,
    required_component_upper='.002645',source_sha256=sha(Path(__file__)),input_hashes=pins,
    scalars={name:x.json() for name,x in scalars.items()},matrix_blocks=blocks,
    continuous_terms=continuous_records,difference_blocks=diffblocks,
    archives={p.name:dict(path=str(p.relative_to(BASE.parent.parent)),sha256=sha(p))
              for p in [apath,diffpath]},checks=checks,failures=failures,
    elapsed_seconds=time.monotonic()-start_time,
    unresolved=['independent audits Sections12-17','complement coercivity',
                'whole-core/c_* and global actual-Xi obligations'])
path=BASE/'signed-mixed-inverse-action-576.json'
path.write_text(json.dumps(output,indent=2)+'\n')
print('Checks:',len(checks),'failures:',failures,flush=True)
print('Complete normalized inverse-action error upper:',eta.hi,'; required <=.002645',flush=True)
print('Certificate:',path.relative_to(BASE.parent.parent),'arrays:',
      apath.relative_to(BASE.parent.parent),diffpath.relative_to(BASE.parent.parent),flush=True)
