#!/usr/bin/env python3
"""One fixed N=512,K=65536 half-complement reference test; C999k.

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
N, K = 512, 65536


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


audit = json.loads((BASE/'certificate-audit-534.json').read_text())
check(not audit['failures'], 'inherited534 failures empty')
pins = {}
for name in ['complete-schur-531.py', 'residual-certificate-532.py',
             'complete-covariance-532.npz']:
    pins[name] = sha(BASE/name)
    check(pins[name] == audit['original_sha256'][name], 'audited input hash '+name)
for name in ['response-prefix-audit-548.json', 'fixed-trial-residual-audit-552.json']:
    pins[name] = sha(BASE/name)
    check(not json.loads((BASE/name).read_text())['failures'], name+' failures empty')
direction_path = BASE/'response-prefix-direction-546.json'
pins[direction_path.name] = sha(direction_path)
check(pins[direction_path.name] ==
      'f39d45d9754d0415f5180e2cb5803d8152bfbaba3eb34130b4bf4b91b81da013',
      'fixed546 exact direction hash')
direction = json.loads(direction_path.read_text())
check(direction['modes'] == N and direction['denominator'] == 2**40, 'fixed trial parameters')
pi, ell = 16*atan(5)-4*atan(239), I(3).ln()/2
k2 = [sq(n*pi/ell) for n in range(N)]


def neutral(integers):
    check(len(integers) == N-2, 'complete free coefficients')
    u = [I(0), I(0)]+[I(x)/(2**40) for x in integers]
    for n in range(2, N):
        p = n % 2
        ratio = (I('.25')+k2[p])/(I('.25')+k2[n])
        if p == 0:
            ratio *= I(2).sqrt()
        u[p] -= ratio*u[n]
    return u


f = neutral(direction['f_free_numerators'])
g = neutral(direction['g_free_numerators'])
h = [(-1)**n*x for n, x in enumerate(f)]
check(all(ab(g[n]) == 0 for n in range(1, N, 2)), 'middle exactly even')
exact = dict(f=f, g=g, h=h)
vectors = {name: np.array([float(iv.NEAR.divide(iv.NEAR.add(x.lo, x.hi), Decimal(2)))
                         for x in vec]) for name, vec in exact.items()}
conversion = {name: l1([x-as_i(y) for x, y in zip(vec, vectors[name])])
              for name, vec in exact.items()}
norms = {name: norm(vec) for name, vec in exact.items()}
ones = {name: l1(vec) for name, vec in exact.items()}
for name in exact:
    check(conversion[name].hi < Decimal('1e-14'), name+' coefficient L1 conversion <1e-14')
check(all(x.hi < 10 for x in ones.values()), 'all coefficient L1 norms <10')

with np.load(BASE/'complete-covariance-532.npz') as data:
    m0, mc, mg, cov = [data[key] for key in ['m0', 'mc', 'mg', 'cov00']]
check(np.array_equal(m0, m0.T), 'stored head exactly symmetric')
check(np.array_equal(cov, cov.T), 'stored full covariance exactly symmetric')
check(max(np.max(np.abs(x)) for x in [m0, mc, mg, cov]) < 400, 'stored entries <400')

# Operator-order enclosures, with all response/penalty covariance retained.
d0, eta_m, eta_g = I('6.14'), I('.00024'), I('.0046')
e0 = I('.000000181')+I((K-N)*N).sqrt()*I('1e-7')
tail_w = I('.062501')+I('.000000906')
debt_g = (2*I('.586')+e0)*e0+I('1e-6')+sq(tail_w)
check((I('.000184')+N*I('1e-7')).hi < eta_m.lo, 'head operator-order allowance')
check(debt_g.hi < eta_g.lo, 'complete covariance operator-order allowance')

# The exact reference head is H=m0-eta_m I-(100/307)(cov+eta_g I).
# This float matrix is only a proposed representation of that exact rational H.
hf = m0-float(eta_m.lo)*np.eye(N)-(100/307)*(cov+float(eta_g.lo)*np.eye(N))
factor = np.linalg.cholesky(hf-.24*np.eye(N))
reconstruction = float(np.linalg.norm(hf-.24*np.eye(N)-factor@factor.T))
factor_normsq = float(np.sum(factor*factor))
check(reconstruction < 1e-7, 'head factor reconstruction residual <1e-7')
check(factor_normsq < 10000 and np.max(np.abs(factor)) < 20, 'head factor magnitude ledger')
check(np.max(np.abs(hf)) < 400, 'reference head magnitude ledger')
# C999k gives the gamma bound including H assembly: true residual <1e-6.
finite_inverse_error_floor = I('.239999')

rho = np.zeros(K)
seven = mc+mg
rho[:N] = seven@vectors['f']+seven.T@vectors['h']-m0@vectors['g']

# Regenerate every complementary row with precisely C744w's formulas.
con = old.constants()
el, pif = con['ell'], con['pi']
indices = np.arange(K)
k = indices*pif/el
nu = np.full(K, np.sqrt(2/el)); nu[0] = 1/np.sqrt(el)
parity = np.where(indices % 2 == 0, 1., -1.)
imag, rem = old.psi_imag(k, pif)
b = k*imag/2
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


blocks = []
for start in range(N, K, N):
    rows = slice(start, start+N)
    kn, km = k[rows, None], k[None, :N]
    same = parity[rows, None] == parity[None, :N]
    response = (b[rows, None]-b[None, :N])/(kn*kn-km*km)
    for j in range(64):
        c = 2*j+.5
        response -= ((3.**(-j)/con['fourth'])*parity[rows, None]*c*c
                     /((c*c+kn*kn)*(c*c+km*km)))
    response *= 2*np.outer(nu[rows], nu[:N])*same
    t, tt = np.zeros_like(response), np.zeros_like(response)
    for delta, weight in zip(con['deltas'], con['weights']):
        t += weight*translation(rows, delta)
        tt += weight*translation(rows, -delta)
    for j in range(1, 8):
        c = 2*j+.5
        decay = 3.**(-j)/con['fourth']
        minus = nu*c*(1-parity*decay)/(c*c+k*k)
        plus = nu*c*(parity-decay)/(c*c+k*k)
        prefactor = 3.**(-6*j)/(3*np.sqrt(3.))
        t += prefactor*np.outer(minus[rows], plus[:N])
        tt += prefactor*np.outer(plus[rows], minus[:N])
    w0 = response+256*moments[:, rows].T@moments[:, :N]
    wc, wg = (t+tt)/2, (t-tt)/2
    # Keep both T orientations and every mixed term in the combined row.
    rho[rows] = ((wc+wg)@vectors['f']+(wc-wg)@vectors['h']-w0@vectors['g'])
    maximum = max(float(np.max(np.abs(x))) for x in [w0, wc, wg])
    check(maximum < 400, 'entry ledger rows '+str(start)+':'+str(start+N))
    blocks.append(dict(first=start, last=start+N-1, maximum_entry=maximum))

check(np.isfinite(rho).all(), 'all combined residual rows finite')
# Per-entry allowances, plus the already audited analytic response operator
# error; 1e-6 covers all vector conversions and floating matrix/vector sums.
delta_head = (eta_m*norms['g']+I(N).sqrt()*I('2.1e-7')*(ones['f']+ones['h'])+I('1e-6'))
delta_mid = (I('.000000181')*norms['g']+I(K-N).sqrt()
             *(I('1e-7')*ones['g']+I('2.1e-7')*(ones['f']+ones['h']))+I('1e-6'))

solution = np.linalg.solve(hf, rho[:N])
yi = [as_i(x) for x in solution]
bi = [as_i(x) for x in rho[:N]]
# Exact rational H entry action, accumulated with directed Decimal bounds.
hyi = []
for i in range(N):
    value = I(0)
    for j in range(N):
        entry = as_i(m0[i, j])-I(100)/307*as_i(cov[i, j])
        if i == j:
            entry -= eta_m+I(100)/307*eta_g
        value += entry*yi[j]
    hyi.append(value)
solve_residual = norm([u-v for u, v in zip(bi, hyi)])
y_norm = norm(yi)
center_energy = 2*dot(yi, bi)-dot(yi, hyi)
head_upper = (center_energy+2*y_norm*delta_head
              +sq(solve_residual+delta_head)/finite_inverse_error_floor)

# The exact reference inverse has complement weight 2/h(k_n). Lower bounds
# on each positive h(k_n) upper-bound its weighted action on the full row.
weighted_center = I(0)
diagonal_lowers = []
for n in range(N, K):
    lower = (n/(2*ell)).ln()-2*ell*ell/(9*n*n)
    check(lower.lo > d0.hi, 'positive diagonal row '+str(n))
    weighted_center += 2*sq(as_i(rho[n]))/lower
    diagonal_lowers.append(str(lower.lo))
middle_upper = sq(weighted_center.sqrt()+(2/d0).sqrt()*delta_mid)

# Entire n>=K tail. The square of the SUM pays all mixed covariance.
# The exact moment penalty is zero on g, and Dg has no such coefficients.
weight_sum = sum((I(p).ln()/I(n).sqrt() for n, p in old.POWERS), I(0))
response_b = 4*ell*(1+I('1.5')/(I(3).sqrt().sqrt()))/(pi*pi)
prime_tail = 2*weight_sum/pi/(I(K-N).sqrt())*(ones['f']+ones['h'])
response_tail = (1+response_b/K)/(I(K-1).sqrt())*ones['g']
kappa = 1/(I(2187)*I(3).sqrt()*I('2.5')*(1-I(1)/729))
continuous_tail = kappa*(norms['f']+norms['h'])
rho_tail = prime_tail+response_tail+continuous_tail
dK = (K/(2*ell)).ln()-2*ell*ell/(9*K*K)
tail_upper = 2*sq(rho_tail)/dK
total_upper = head_upper+middle_upper+tail_upper
margin_lower = I('.093538')-total_upper

art = BASE/'fixed-block-metric-555.npz'
np.savez_compressed(art, reference_head_float=hf, factor=factor,
                    solution=solution, combined_residual=rho)
result = dict(scope='One fixed546 N512 K65536 half-complement reference majorant',
    parameters=dict(N=N, K=K, complement_fraction='1/2', penalty=256, d0='6.14'),
    source_script_sha256=sha(Path(__file__)), input_hashes=pins,
    runtime=dict(python=sys.version, numpy=np.__version__, machine=platform.machine()),
    coefficients={name: [x.json() for x in vec] for name, vec in exact.items()},
    coefficient_L1={name: x.json() for name, x in ones.items()},
    coefficient_L2={name: x.json() for name, x in norms.items()},
    coefficient_conversion={name: x.json() for name, x in conversion.items()},
    constants=dict(pi=pi.json(), ell=ell.json()),
    reference=dict(head_allowance=eta_m.json(), covariance_allowance=eta_g.json(),
        finite_covariance_factor_error=e0.json(), full_W0_tail=tail_w.json(),
        total_covariance_error=debt_g.json(), reconstruction_float=reconstruction,
        exact_reconstruction_error_upper='1e-6', factor_norm_squared_float=factor_normsq,
        finite_solve_error_floor=finite_inverse_error_floor.json()),
    head=dict(rho_L2_error=delta_head.json(), solution_L2=y_norm.json(),
        exact_H_solution=[x.json() for x in hyi], solve_residual=solve_residual.json(),
        center_energy=center_energy.json(), upper=head_upper.json()),
    middle=dict(first=N, last=K-1, row_blocks=blocks,
        diagonal_lower_endpoints=diagonal_lowers, rho_L2_error=delta_mid.json(),
        complete_weighted_center=weighted_center.json(), upper=middle_upper.json()),
    tail=dict(first=K, prime_weight_sum=weight_sum.json(), response_b=response_b.json(),
        prime_L2=prime_tail.json(), response_L2=response_tail.json(),
        continuous_L2=continuous_tail.json(), full_rho_L2=rho_tail.json(),
        diagonal_lower=dK.json(), upper=tail_upper.json()),
    summary=dict(head_upper=str(head_upper.hi), middle_upper=str(middle_upper.hi),
        infinite_tail_upper=str(tail_upper.hi), reference_action_upper=str(total_upper.hi),
        required_strict_upper='.093538', rejection_lower_threshold='.094207',
        minimized_energy_lower=str(margin_lower.lo), passed=total_upper.hi < Decimal('.093538')),
    checks=checks, failures=failures,
    binary_artifact=dict(path=art.name, sha256=sha(art)),
    qualifications=['Full inherited analytic/IEEE754/Decimal contracts.',
        'Restricted-core construction and source c_star retain prior qualifications.',
        'Only fixed endpoints; no uniform triple sign, H2 witness or RH conclusion.',
        'An interval for an upper-bound expression is not a two-sided inverse enclosure.'])
out = BASE/'fixed-block-metric-555.json'
out.write_text(json.dumps(result, indent=2)+'\n')
print('Head inverse-action upper:', head_upper.hi)
print('Modes512:65535 weighted upper:', middle_upper.hi)
print('Entire n>=65536 weighted upper:', tail_upper.hi)
print('Reference upper:', total_upper.hi, '; required < .093538')
print('Fixed minimized energy lower:', margin_lower.lo)
print('Checks:', len(checks), '; failures:', failures)
print('Certificate:', out.relative_to(BASE.parent.parent))
print('Binary evidence:', art.relative_to(BASE.parent.parent))
assert not failures
