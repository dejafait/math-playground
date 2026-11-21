#!/usr/bin/env python3
"""Certify the full saved dyadic mixed-row CENTER covariance only.

No FFT accuracy or exact-operator connection is assumed. Exact neutral
ratios, outward weights, every finite column, and full Gram/factor errors
are paid under the inherited IEEE754/Decimal contract.
"""
import hashlib
import importlib.util
import json
from decimal import Context, Decimal, ROUND_CEILING, ROUND_FLOOR, ROUND_HALF_EVEN
from pathlib import Path
import numpy as np

BASE = Path(__file__).resolve().parent
N, K, E = 512, 65536, 1020
spec = importlib.util.spec_from_file_location('iv572', BASE/'complete-schur-531.py')
iv = importlib.util.module_from_spec(spec)
spec.loader.exec_module(iv)
iv.DOWN = Context(prec=80, rounding=ROUND_FLOOR)
iv.UP = Context(prec=80, rounding=ROUND_CEILING)
iv.NEAR = Context(prec=80, rounding=ROUND_HALF_EVEN)
I = iv.I
checks, failures, pins = [], [], {}

def check(ok, label):
    checks.append(dict(label=label, passed=bool(ok)))
    if not ok:
        failures.append(label)

def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(8*1024*1024), b''):
            h.update(block)
    return h.hexdigest()

def atan(q):
    x = I(1)/q
    total, power = I(0), x
    for j in range(80):
        total += (-1)**j*power/(2*j+1)
        power *= x*x
    return total+I(-power.hi,power.hi)/161

def upper_float(x):
    return float(np.nextafter(float(x),np.inf))

def lower_float(x):
    return float(np.nextafter(float(x),-np.inf))

audit = json.loads((BASE/'neutral-head-covariance-audit-561.json').read_text())
check(not audit['failures'] and all(c['passed'] for c in audit['checks']),
      'complete inherited head audit check list')
for name in ['neutral-head-covariance-559.npz','complete-schur-531.py']:
    pins[name] = sha(BASE/name)
    check(pins[name] == audit['original_hashes'][name], 'unchanged audited input '+name)
with np.load(BASE/'neutral-head-covariance-559.npz') as data:
    mc = data['comparison_lower']
check(mc.shape == (E,E) and np.array_equal(mc,mc.T), 'exact comparison dimensions and symmetry')
raw_path = BASE/'signed-mixed-columns-565.npy'
pins[raw_path.name] = sha(raw_path)
raw = np.load(raw_path,mmap_mode='r')
check(raw.shape == (2,K,E) and raw.dtype == np.dtype('float64'), 'all saved dyadic raw rows present')

# All scalar coordinates are enclosed independently of library log/sine.
pi, ell = 16*atan(5)-4*atan(239), I(3).ln()/2
pi2ell2 = pi*pi/(ell*ell)
sqrt2 = I(2).sqrt()
rhat, weights = np.empty(K-N), np.empty(K-N)
dlo, dhi, rlo, rhi = [np.empty(K-N) for _ in range(4)]
max_r_error = Decimal(0)
scalar_ok = True
for n in range(N,K):
    j, parity = n-N,n % 2
    dn = (I(n)/(2*ell)).ln()-2*ell*ell/(9*n*n)
    rn = (sqrt2 if parity == 0 else I(1))*(I('.25')+pi2ell2*parity)/(I('.25')+pi2ell2*n*n)
    weight = 1/dn.sqrt()
    rhat[j] = float(rn.lo)
    weights[j] = upper_float(weight.hi)
    dlo[j], dhi[j] = lower_float(dn.lo),upper_float(dn.hi)
    rlo[j], rhi[j] = lower_float(rn.lo),upper_float(rn.hi)
    re = max((I(float(rhat[j]))-rn).lo.copy_abs(),(I(float(rhat[j]))-rn).hi.copy_abs())
    max_r_error = max(max_r_error,re)
    scalar_ok = scalar_ok and (dn.lo > Decimal('6.14') and weight.hi <= Decimal.from_float(weights[j]) < Decimal('.5')
        and re < Decimal('1e-20') and Decimal(0) < rn.lo <= rn.hi < Decimal('1e-5'))
check(scalar_ok,'every exact neutral ratio and upward inverse-square-root weight enclosed')
print('Directed coordinates complete:',K-N,flush=True)

# One signed column is formed before its outer product. Distinct input
# coordinates are the only ranges added as Grams.
gram = np.zeros((E,E))
blocks = []
raw_sq, row_sq = 0.,0.
low = np.array(raw[:,:2])
low_sq = float(np.sum(low*low))
digest = hashlib.sha256()
for start in range(N,K,N):
    j = slice(start-N,start)
    parity = np.arange(start,start+N) % 2
    ledger = dict(first=start,last=start+N-1,orientations=[])
    for side in range(2):
        block = np.array(raw[side,start:start+N])
        good = bool(np.all(np.isfinite(block)))
        weighted = (block-rhat[j,None]*low[side,parity])*weights[j,None]
        gram += weighted.T@weighted
        digest.update(weighted.tobytes())
        bf, wf = float(np.sum(block*block)),float(np.sum(weighted*weighted))
        raw_sq += bf
        row_sq += wf
        ledger['orientations'].append(dict(side=side,raw_squared_fro=bf,weighted_squared_fro=wf))
        check(good and np.all(np.isfinite(weighted)),'complete finite block '+str(start)+' side '+str(side))
    blocks.append(ledger)
    if start % 16384 == 0:
        print('Complete finite center Gram through',start+N-1,flush=True)
check(raw_sq+low_sq < 900000,'all raw and low rows have Frobenius norm below1000 with slack')
check(row_sq < 90,'all weighted dyadic rows have Frobenius norm below10 with slack')
check(np.all(np.isfinite(low)),'all low rows finite')
check(float(np.linalg.norm(mc)) < 400,'comparison Frobenius bound')
gram = (gram+gram.T)/2

# Exact error bridge for the center, not for the unknown mathematical B.
u = I(1)/2**53
gamma = lambda n: n*u/(1-n*u)
ratio_conversion = I('1e-20')*I(K-N).sqrt()*1000/2
row_rounding = gamma(8)*(1000+I(K-N).sqrt()*I('1e-5')*1000)/2
row_error = ratio_conversion+row_rounding+I('1e-12')
check(row_error.hi < Decimal('1e-9'),'exact-ratio and complete row-arithmetic error below1e-9')
gram_rounding = gamma(1024)*100+gamma(512)*100+I('1e-10')
check(gram_rounding.hi < Decimal('1e-8'),'all block Gram and accumulation arithmetic below1e-8')
center_gram_error = I(20)*I('1e-9')+I('1e-9')*I('1e-9')+I('1e-8')
target = .083*mc-gram-1e-6*np.eye(E)
factor = np.empty((0,0))
factor_ledger = dict(proposed=False)
try:
    factor = np.linalg.cholesky(target)
    residual = float(np.linalg.norm(target-factor@factor.T))
    factor_sq = float(np.sum(factor*factor))
    maximum = max(float(np.max(np.abs(a))) for a in [gram,mc,target,factor])
    factor_ledger = dict(proposed=True,residual_fro=residual,factor_squared_fro=factor_sq,maximum_entry=maximum)
    check(residual < 1e-7 and factor_sq < 100000 and maximum < 400,'full proposed factor reconstruction')
except np.linalg.LinAlgError:
    check(False,'full proposed factor reconstruction')
total_error = I('1e-7')+gamma(2048)*100000+I('2e-7')+center_gram_error
check(total_error.hi < Decimal('1e-6'),'restored margin pays full center Gram and factor error')
remaining_norm_budget = I('.085440').sqrt()-I('.083').sqrt()
check(remaining_norm_budget.lo > Decimal(0),'positive remaining exact-map perturbation budget')

archive = BASE/'signed-mixed-finite-center-572.npz'
np.savez_compressed(archive,comparison=mc,center_covariance=gram,factor=factor,
    neutral_ratio_center=rhat,upward_inverse_sqrt_weight=weights,
    d_lower=dlo,d_upper=dhi,r_lower=rlo,r_upper=rhi)
record = dict(parameters=dict(N=N,K=K,endpoint_dimension=E,input_first=N,input_last=K-1),
    scope='Exact dyadic raw proposal rows565 with exact neutral ratios and true d_n weights; no operator or FFT accuracy assertion',
    certified_center_under_inherited_contracts=not failures,exact_operator_finite_covariance_certified=False,
    actual_quarter_decided=False,input_hashes=pins,script_sha256=sha(Path(__file__)),
    archive=dict(path=str(archive.relative_to(BASE.parent.parent)),sha256=sha(archive)),
    scalar_rows=K-N,maximum_ratio_conversion_error=str(max_r_error),
    combined_weighted_rows_sha256=digest.hexdigest(),row_blocks=blocks,
    magnitude_ledger=dict(raw_and_low_squared_fro=raw_sq+low_sq,weighted_squared_fro=row_sq),
    factor=factor_ledger,center_covariance_upper='.083',required_exact_finite_upper='.085440',
    scalars=dict(row_error=row_error.json(),gram_rounding=gram_rounding.json(),center_gram_error=center_gram_error.json(),
        full_factor_error=total_error.json(),remaining_exact_map_norm_budget=remaining_norm_budget.json()),
    checks=checks,failures=failures,
    unresolved=['No accuracy claim for the FFT proposal','Complete finite exact-operator/entry/basis/inverse-solve error unpaid',
        'Section12 joint tail audit and independent complementary coercivity open',
        'Whole-core/c_star and global RH qualifications retained'])
out = BASE/'signed-mixed-finite-center-572.json'
out.write_text(json.dumps(record,indent=2)+'\n')
print('Center checks:',len(checks),'failures:',failures)
print('Certified CENTER covariance upper .083; required EXACT finite covariance upper .085440')
print('Remaining normalized exact-map error must be <=',remaining_norm_budget.lo)
print('Actual finite covariance and quarter test undecided')
print('Certificate:',out.relative_to(BASE.parent.parent),'factor:',archive.relative_to(BASE.parent.parent))
