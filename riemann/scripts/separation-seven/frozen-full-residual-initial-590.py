#!/usr/bin/env python3
"""Frozen C999n/C999o full residual; unchanged C999k reference, step590.

No trial optimization, cutoff change or scalar replacement of the inverse.
The inherited C744v/w analytic and IEEE754/Decimal contracts are hypotheses.
All proposed floating factors/solves are checked by residuals. Full evidence
is saved; stdout contains only bounds, failures and paths.
"""
import hashlib
import importlib.util
import json
import platform
import sys
from decimal import Context, Decimal, ROUND_CEILING, ROUND_FLOOR, ROUND_HALF_EVEN
from pathlib import Path

import numpy as np

BASE = Path(__file__).resolve().parent
N, J, K = 512, 1024, 65536


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


iv = load('interval555', BASE/'complete-schur-531.py')
iv.DOWN = Context(prec=70, rounding=ROUND_FLOOR)
iv.UP = Context(prec=70, rounding=ROUND_CEILING)
iv.NEAR = Context(prec=70, rounding=ROUND_HALF_EVEN)
I = iv.I
old = load('entries555', BASE/'residual-certificate-532.py')
checks, failures = [], []


def check(ok, label):
    checks.append(dict(label=label, passed=bool(ok)))
    if not ok:
        failures.append(label)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def ab(x):
    return max(x.lo.copy_abs(), x.hi.copy_abs())


def sq(x):
    if x.lo <= 0 <= x.hi:
        return I(0, iv.UP.multiply(ab(x), ab(x)))
    return x*x


def powi(x, n):
    out = I(1)
    for _ in range(n):
        out *= x
    return out


def inflate(x, error):
    return x+I(error.hi.copy_negate(), error.hi)


def atan(q):
    x = I(1)/q
    center = sum(((-1)**j*powi(x, 2*j+1)/(2*j+1) for j in range(80)), I(0))
    return inflate(center, powi(x, 161)/161)


def as_i(x):
    return I(Decimal(float(x)))


def l1(vec):
    return sum((I(ab(x)) for x in vec), I(0))


def norm(vec):
    return sum((sq(x) for x in vec), I(0)).sqrt()


def dot(x, y):
    return sum((a*b for a, b in zip(x, y)), I(0))


pins = {}
original = json.loads((BASE/'original-galerkin-586.json').read_text())
manifest = json.loads((BASE/'endpoint-complement-locator-581.json').read_text())
for name in set(list(original['input_hashes']) + [
        'original-galerkin-586.py', 'original-galerkin-586.json',
        'original-galerkin-586.npz', 'original-minimum-audit-588.json',
        'fixed-block-metric-audit-557.json', 'certificate-audit-534.json']):
    pins[name] = sha(BASE/name)
for name, digest in original['input_hashes'].items():
    check(pins[name] == digest, 'original input hash '+name)
check(pins['original-galerkin-586.npz'] == original['archive']['sha256'], 'trial archive hash')
check(pins['original-galerkin-586.py'] == original['script_sha256'], 'trial generator hash')
check(sha(BASE/'endpoint-complement-locator-581.npz') == manifest['archive']['sha256'],
      'frozen endpoint manifest hash')
for name in ['original-galerkin-586.json', 'original-minimum-audit-588.json',
             'fixed-block-metric-audit-557.json', 'certificate-audit-534.json']:
    check(not json.loads((BASE/name).read_text())['failures'], name+' no failures')
audit = json.loads((BASE/'certificate-audit-534.json').read_text())
for name in ['complete-schur-531.py', 'residual-certificate-532.py', 'complete-covariance-532.npz']:
    check(sha(BASE/name) == audit['original_sha256'][name], 'audited reference pin '+name)
    pins[name] = sha(BASE/name)
with np.load(BASE/'original-galerkin-586.npz') as data:
    saved = {key: data[key].copy() for key in data.files}
with np.load(BASE/'endpoint-complement-locator-581.npz') as data:
    check(np.array_equal(data['free_numerators'], saved['free_numerators']),
          'all endpoint free integers unchanged')
check(np.max(np.abs(saved['free_numerators'])) < 2**53, 'endpoint integers exactly convertible')
pi, ell = 16*atan(5)-4*atan(239), I(3).ln()/2
k2 = [sq(n*pi/ell) for n in range(J)]
ratios = []
for n in range(2, J):
    ratio = (I('.25')+k2[n % 2])/(I('.25')+k2[n])
    if n % 2 == 0:
        ratio *= I(2).sqrt()
    ratios.append(ratio)


def complete(free):
    u = [I(0), I(0)]+[as_i(x) for x in free]
    for n in range(2, J):
        u[n % 2] -= ratios[n-2]*u[n]
    return u


endpoint_free = saved['free_numerators'].astype(float)/2**40
check(np.array_equal(endpoint_free*2**40, saved['free_numerators']), 'endpoint dyadics exact')
ff, hh = np.zeros(J-2), np.zeros(J-2)
ff[N-2:], hh[N-2:] = endpoint_free[:N], endpoint_free[N:]
exact = dict(f=complete(ff), h=complete(hh), g=complete(saved['middle_free_dyadic']))
vectors = dict(f=saved['endpoint_f_center'], h=saved['endpoint_h_center'], g=saved['middle_raw_center'])
ones = {name: l1(vec) for name, vec in exact.items()}
norms = {name: norm(vec) for name, vec in exact.items()}
conversion = {name: l1([x-as_i(y) for x, y in zip(vec, vectors[name])]) for name, vec in exact.items()}
for name in exact:
    check(conversion[name].hi < Decimal('1e-14'), name+' complete coordinate conversion<1e-14')
    check(ones[name].hi < 2, name+' coefficient L1<2')

# All exact vectors are finite and exactly neutral by the two parity ratios.
# Hence g is in Dom(A0), and Cg=0 removes the true moment penalty in rho.
# C999k Sections1/6 and C999l(5) apply to this trial, without orthogonality.
with np.load(BASE/'complete-covariance-532.npz') as data:
    m0, cov = data['m0'], data['cov00']
eta_m, eta_g = I('.00024'), I('.0046')
hf = m0-float(eta_m.lo)*np.eye(N)-(100/307)*(cov+float(eta_g.lo)*np.eye(N))
factor = np.linalg.cholesky(hf-.24*np.eye(N))
reconstruction = float(np.linalg.norm(hf-.24*np.eye(N)-factor@factor.T))
factor_normsq = float(np.sum(factor*factor))
check(reconstruction < 1e-7 and factor_normsq < 10000 and np.max(np.abs(factor)) < 20,
      'unchanged head factor full reconstruction/magnitudes')
check(np.max(np.abs(hf)) < 400, 'unchanged reference head entries<400')
floor = I('.239999')  # C999k full reconstruction rounding allowance<1e-6.

rho = np.zeros(K)
M, T, Ts = [saved[key] for key in ['local_matrix', 't_entries', 'ts_entries']]
check(all(x.shape == (J,J) and np.isfinite(x).all() and np.max(np.abs(x)) < 400
          for x in [M,T,Ts]), 'audited square shapes/magnitudes')
check(np.array_equal(T, Ts.T), 'square both orientations')
# M is D+S, not a comparison diagonal: Dg on512:1023 is retained here.
rho[:J] = T@vectors['f']+Ts@vectors['h']-M@vectors['g']

con = old.constants()
el, pif = con['ell'], con['pi']
indices = np.arange(K)
k = indices*pif/el
nu = np.full(K, np.sqrt(2/el)); nu[0] = 1/np.sqrt(el)
parity = np.where(indices % 2 == 0, 1., -1.)
imag, rem = old.psi_imag(k, pif)
b = k*imag/2

# C744w's scalar entry ledger extends: the same maximum output argument,
# denominator ratio<1024, frequency gap, and constant/shift cases apply.
# New accumulated vector error bounds below use all1024 input coefficients.
ratio_bound = I(J*J+(J-1)*(J-1))/(J*J-(J-1)*(J-1))
check(ratio_bound.hi < 1024, 'whole rectangular denominator cancellation ratio<1024')
rmax = I(2).sqrt()/(6*I('64.25')*I('64.25'))
offdiag_error = (2/ell)*rmax/(pi/ell)
diag_error = (1/I('131072.5')/I('131072.5')
              +2*k2[-1]*(1/(6*powi(I('131072.5'),3))+1/powi(I('131072.5'),4)))
local_entry_derived = rmax+offdiag_error+8*diag_error+I('1e-7')
epsM, epsT = I('.0001'), I('.000001')
check(local_entry_derived.hi < epsM.lo, 'all rectangular/local entry error<.0001')
# For n!=m: (kn rn+km rm)/(kn²-km²)<=rmax/|kn-km|.
# The normalized factor is nu_n nu_m, at most2/ell. This gives offdiag_error.
# Equal indices occur only in the audited square; their error is diag_error.
check((I(65535)*pi/ell*I('.549307')).hi < Decimal('207000'), 'all shift arguments within original ledger')


def translation(rows, delta):
    kn, km = k[rows,None], k[None,:J]
    sn, _ = old.sincos(k[rows]*delta, pif)
    sm, _ = old.sincos(k[:J]*delta, pif)
    signs = parity[rows,None]*parity[None,:J]
    numerator = (-signs*kn*sn[:,None]+km*sm[None,:] if delta > 0
                 else kn*sn[:,None]-signs*km*sm[None,:])
    return numerator/(kn*kn-km*km)*np.outer(nu[rows],nu[:J])


blocks = []
for start in range(J, K, N):
    rows = slice(start,start+N)
    kn, km = k[rows,None], k[None,:J]
    same = parity[rows,None] == parity[None,:J]
    response = (b[rows,None]-b[None,:J])/(kn*kn-km*km)
    for j in range(64):
        c = 2*j+.5
        response -= (3.**(-j)/con['fourth'])*parity[rows,None]*c*c/((c*c+kn*kn)*(c*c+km*km))
    response *= 2*np.outer(nu[rows],nu[:J])*same
    t, tt = np.zeros_like(response), np.zeros_like(response)
    for delta, weight in zip(con['deltas'],con['weights']):
        t += weight*translation(rows,delta)
        tt += weight*translation(rows,-delta)
    for j in range(1,8):
        c = 2*j+.5
        decay = 3.**(-j)/con['fourth']
        minus = nu*c*(1-parity*decay)/(c*c+k*k)
        plus = nu*c*(parity-decay)/(c*c+k*k)
        prefactor = 3.**(-6*j)/(3*np.sqrt(3.))
        t += prefactor*np.outer(minus[rows],plus[:J])
        tt += prefactor*np.outer(plus[rows],minus[:J])
    rho[rows] = t@vectors['f']+tt@vectors['h']-response@vectors['g']
    maximum = max(float(np.max(np.abs(x))) for x in [response,t,tt])
    check(maximum < 400, 'all generated entries<400 block '+str(start))
    blocks.append(dict(first=start,last=start+N-1,maximum_entry=maximum))
check(np.isfinite(rho).all(), 'every combined residual row finite')

# Per row, sum absolute products<400*(lf+lh+lg)<2400. gamma_2048<2.3e-13;
# all dot/addition and coordinate errors over256 rows in norm cost<1e-6.
delta_head = I(N).sqrt()*(epsM*ones['g']+epsT*(ones['f']+ones['h']))+I('1e-6')
delta_mid = I(K-N).sqrt()*(epsM*ones['g']+epsT*(ones['f']+ones['h']))+I('1e-6')
arith_row = I('2.3e-13')*2400+400*sum(conversion.values(),I(0))+I('1e-11')
check((256*arith_row).hi < Decimal('1e-6'), 'full matvec/coefficient arithmetic allowance')

solution = np.linalg.solve(hf,rho[:N])
yi, bi = [as_i(x) for x in solution], [as_i(x) for x in rho[:N]]
hyi = []
for i in range(N):
    value = I(0)
    for j in range(N):
        entry = as_i(m0[i,j])-I(100)/307*as_i(cov[i,j])
        if i == j:
            entry -= eta_m+I(100)/307*eta_g
        value += entry*yi[j]
    hyi.append(value)
solve_residual = norm([u-v for u,v in zip(bi,hyi)])
ynorm = norm(yi)
center_energy = 2*dot(yi,bi)-dot(yi,hyi)
head_upper = center_energy+2*ynorm*delta_head+sq(solve_residual+delta_head)/floor

d0 = I('6.14')
weighted_center, diagonal_lowers = I(0), []
for n in range(N,K):
    dn = (n/(2*ell)).ln()-2*ell*ell/(9*n*n)
    check(dn.lo > d0.hi, 'positive denominator row '+str(n))
    weighted_center += 2*sq(as_i(rho[n]))/dn
    diagonal_lowers.append(str(dn.lo))
middle_upper = sq(weighted_center.sqrt()+(2/d0).sqrt()*delta_mid)

# Entire n>=K: all inputs m<=1023, denominator sum<=1/(K-1024).
# Cg=0, Dg=0 on this tail. The square of the SUM pays every cross term.
weight_sum = sum((I(p).ln()/I(n).sqrt() for n,p in old.POWERS),I(0))
response_b = 4*ell*(1+I('1.5')/(I(3).sqrt().sqrt()))/(pi*pi)
prime_tail = 2*weight_sum/pi/I(K-J).sqrt()*(ones['f']+ones['h'])
response_tail = (1+response_b/K)/I(K-1).sqrt()*ones['g']
kappa = 1/(I(2187)*I(3).sqrt()*I('2.5')*(1-I(1)/729))
continuous_tail = kappa*(norms['f']+norms['h'])
rho_tail = prime_tail+response_tail+continuous_tail
dK = (K/(2*ell)).ln()-2*ell*ell/(9*K*K)
tail_upper = 2*sq(rho_tail)/dK
total_upper = head_upper+middle_upper+tail_upper
threshold = I('.42328427')
check(I(original['bounds']['trial_energy']['lo']).lo > threshold.hi, 'audited full original energy>threshold')
margin = threshold-total_upper
check(all(sha(BASE/name) == digest for name,digest in pins.items()), 'all pinned artifacts preserved')

art = BASE/'frozen-full-residual-590.npz'
np.savez_compressed(art,combined_residual=rho,reference_head_float=hf,
                    factor=factor,solution=solution,middle_free_dyadic=saved['middle_free_dyadic'])
out = BASE/'frozen-full-residual-590.json'
result = dict(target="Bound the complete reference-residual debt for C999n's frozen endpoints and C999o's fixed neutral trial using C999k's unchanged R, testing whether it is below .42328427.",
    parameters=dict(head=N,trial_support=J,K=K,reference='unchanged C999k'),
    input_hashes=pins,script_sha256=sha(Path(__file__)),
    coefficients={name:[x.json() for x in vec] for name,vec in exact.items()},
    coefficient_L1={name:x.json() for name,x in ones.items()},
    coefficient_L2={name:x.json() for name,x in norms.items()},
    coefficient_conversion={name:x.json() for name,x in conversion.items()},
    constants=dict(pi=pi.json(),ell=ell.json()),
    entry_ledger=dict(cancellation_ratio_upper=ratio_bound.json(),rmax=rmax.json(),
        offdiagonal_analytic_error=offdiag_error.json(),diagonal_error=diag_error.json(),
        local_derived=local_entry_derived.json(),epsM=epsM.json(),epsT=epsT.json(),arithmetic_row=arith_row.json()),
    reference=dict(reconstruction_float=reconstruction,factor_normsq_float=factor_normsq,
        exact_reconstruction_error_upper='1e-6',finite_inverse_error_floor=floor.json()),
    head=dict(rho_L2_error=delta_head.json(),solution_L2=ynorm.json(),
        exact_H_solution=[x.json() for x in hyi],solve_residual=solve_residual.json(),
        center_energy=center_energy.json(),upper=head_upper.json()),
    middle=dict(first=N,last=K-1,row_blocks=blocks,diagonal_lower_endpoints=diagonal_lowers,
        rho_L2_error=delta_mid.json(),complete_weighted_center=weighted_center.json(),upper=middle_upper.json()),
    tail=dict(first=K,max_input_index=J-1,weight_sum=weight_sum.json(),response_b=response_b.json(),
        prime_L2=prime_tail.json(),response_L2=response_tail.json(),continuous_L2=continuous_tail.json(),
        full_rho_L2=rho_tail.json(),diagonal_lower=dK.json(),upper=tail_upper.json()),
    summary=dict(head_upper=str(head_upper.hi),middle_upper=str(middle_upper.hi),
        infinite_tail_upper=str(tail_upper.hi),reference_action_upper=str(total_upper.hi),
        required_strict_upper=str(threshold.lo),minimized_energy_lower=str(margin.lo),
        passed=not failures and total_upper.hi < threshold.lo),
    checks=checks,failures=failures,binary_artifact=dict(path=art.name,sha256=sha(art)),
    qualifications=['Inherited analytic/IEEE754/Decimal contracts; whole-core and unreplayed c_* qualification.',
        'One fixed pair only; no uniform endpoint, H2, C744q or RH conclusion.',
        'New numerical enclosure awaits separate conceptual audit.'])
out.write_text(json.dumps(result,indent=2)+'\n')
print('Complete reference residual debt upper:',total_upper.hi,'; required <',threshold.lo)
print('Head/complement/infinite tail upper:',head_upper.hi,middle_upper.hi,tail_upper.hi)
print('Unrestricted neutral-middle energy lower:',margin.lo)
print('Checks:',len(checks),'; failures:',failures)
print('Certificate:',out.relative_to(BASE.parent.parent),'; full arrays:',art.relative_to(BASE.parent.parent))
assert not failures


