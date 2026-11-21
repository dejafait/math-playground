#!/usr/bin/env python3
"""One fixed-band, UNCERTIFIED locator, assessment579.

All analytic formulas represent full operators. No floating result is a
sign certificate; elementary/response and arithmetic errors remain unpaid.
A finite variational trial is used, never a replaced inverse.
"""
import hashlib
import importlib.util
import json
from decimal import Decimal, localcontext
from pathlib import Path
import numpy as np

BASE = Path(__file__).resolve().parent
ROOT = BASE.parent.parent
spec = importlib.util.spec_from_file_location('entries581', BASE/'residual-certificate-532.py')
e = importlib.util.module_from_spec(spec)
spec.loader.exec_module(e)
con = e.constants()
ell, pi = con['ell'], con['pi']
with localcontext() as ctx:
    ctx.prec = 80
    fourth_decimal = Decimal(3).sqrt().sqrt()
    decay_constants = [float(Decimal(1)/(Decimal(3)**j*fourth_decimal)) for j in range(64)]
    cross_constants = {sep:[float(Decimal(1)/fourth_decimal**((sep-1)*(4*j+1))) for j in range(1,8)] for sep in [7,14]}
J, N = 1024, 512
idx = np.r_[0, 1, np.arange(N, J)]
n = np.arange(J)
k = n*pi/ell
nu = np.full(J, np.sqrt(2/ell)); nu[0] /= np.sqrt(2)
par = np.where(n % 2 == 0, 1., -1.)
kn, km = k[:, None], k[None, idx]
den = kn*kn-km*km
rr, cc = idx, np.arange(len(idx))
den[rr, cc] = 1
scale = np.outer(nu, nu[idx])
signs = par[:, None]*par[None, idx]

def shift(delta):
    if delta == 0:
        a = np.zeros_like(den)
        a[rr, cc] = 1
        return a
    sn, cs = e.sincos(k*delta, pi)
    num = (-signs*kn*sn[:, None]+km*sn[None, idx] if delta > 0
           else kn*sn[:, None]-signs*km*sn[None, idx])
    a = num/den
    diag = np.empty(len(idx)); diag[0] = ell-abs(delta)
    ii = idx[1:]
    diag[1:] = (ell-abs(delta))*cs[ii]/2-np.sign(delta)*sn[ii]/(2*k[ii])
    a[rr, cc] = diag
    return a*scale

def continuous(sep):
    a, b = np.zeros_like(den), np.zeros_like(den)
    for j in range(1, 8):
        c = 2*j+.5
        decay = decay_constants[j]
        minus = nu*c*(1-par*decay)/(c*c+k*k)
        plus = nu*c*(par-decay)/(c*c+k*k)
        prefactor = cross_constants[sep][j-1]
        a += prefactor*np.outer(minus, plus[idx])
        b += prefactor*np.outer(plus, minus[idx])
    return a, b

# Regenerate the complete prime-power list by integer inequalities.
powers = []
for v in range(2, 4000):
    if not 3**13 < v*v < 3**15:
        continue
    p = next((p for p in range(2, int(np.sqrt(v))+1) if v % p == 0), v)
    rem = v
    while rem % p == 0:
        rem //= p
    if rem == 1:
        powers.append((v, p))
source_path = BASE/'response-prefix-stop-546.json'
source = json.loads(source_path.read_text())
assert powers == [(r['n'], r['prime']) for r in source['remote']['primes']]
assert len(powers) == 334 and (2187, 3) in powers
with localcontext() as ctx:
    ctx.prec = 80
    de = Decimal(3).ln()/2
    delays = [0. if v == 2187 else float(14*de-Decimal(v).ln()) for v,p in powers]
    weights = [float(Decimal(p).ln()/Decimal(v).sqrt()) for v,p in powers]

T, Ts = continuous(7)
for delta, weight in zip(con['deltas'], con['weights']):
    T += weight*shift(delta)
    Ts += weight*shift(-delta)
U, Us = continuous(14)
for delta, weight in zip(delays, weights):
    U += weight*shift(delta)
    Us += weight*shift(-delta)
print('Built full T/T* and U/U* entry centers; all334 remote powers, exact zero shift.', flush=True)

im, rem = e.psi_imag(k, pi)
b = k*im/2
S = (b[:, None]-b[None, idx])/den
sdiag = np.zeros(len(idx))
for start in range(0, 65536, 1024):
    c = 2*np.arange(start, start+1024)+.5
    sdiag += np.sum(c[None, :]**2/(c[None, :]**2+k[idx, None]**2)**2, axis=1)
sdiag += 1/(2*131072.5)
S[rr, cc] = sdiag
for j in range(64):
    c = 2*j+.5
    S -= decay_constants[j]*par[:, None]*c*c/((c*c+kn*kn)*(c*c+km*km))
S *= 2*scale*(signs == 1)
with localcontext() as ctx:
    ctx.prec = 80
    logs = np.array([float((Decimal('64.25')**2+(Decimal(float(t))/2)**2).ln()/2) for t in k])
y = k/2
D = logs-64.25/(2*(64.25**2+y*y))-con['logpi']
for j in range(64):
    D -= (j+.25)/((j+.25)**2+y*y)
L = S[idx, :].copy()
L[np.arange(len(idx)), np.arange(len(idx))] += D[idx]
L = (L+L.T)/2

# Exact object Z is C999m(1); this is only its floating locator center.
r = (.25+k[n[N:] % 2]**2)/(.25+k[N:]**2)*np.where(n[N:] % 2 == 0, np.sqrt(2), 1.)
Z = np.zeros((len(idx), N)); Z[2:] = np.eye(N)
Z[n[N:] % 2, np.arange(N)] = -r
A = Z.T@L@Z
V = Z.T@U[idx, :]@Z
E = np.block([[A, -V.T], [-V, A]])
forcing = np.hstack((T@Z, Ts@Z))
with np.load(BASE/'complete-covariance-532.npz') as data:
    H = data['m0']-.00024*np.eye(N)-(100/307)*(data['cov00']+.0046*np.eye(N))
X = np.empty_like(forcing)
X[:N] = np.linalg.solve(H, forcing[:N])
X[N:] = 2*forcing[N:]/D[N:, None]
# This center uses the best trial in0:1023. Omitted inverse directions
# would only lower the exact F, so a positive locator proves no floor.
d = np.log(n[N:]/(2*ell))-2*ell*ell/(9*n[N:]**2)
w = np.r_[d, d]
M = E-forcing.T@X-np.diag(w/4)
M = (M+M.T)/2
white = M/np.sqrt(w[:, None]*w[None, :])
vals, vecs = np.linalg.eigh(white)
free_center = vecs[:, 0]/np.sqrt(w)
# Freeze dyadic FREE coordinates; exact lows must be reconstructed from r.
q = 2**40
numerators = np.rint(free_center*q).astype(np.int64)
free = numerators.astype(float)/q
trial = X@free
trial_numerators = np.rint(trial*q).astype(np.int64)
trial = trial_numerators.astype(float)/q
rho = forcing@free
norm = float(np.dot(w*free, free))
raw = Z@free[:N], Z@free[N:]
endpoint = float(free@E@free)
energy = float(trial[:N]@H@trial[:N]+np.dot(D[N:]*trial[N:], trial[N:])/2)
pairing = float(trial@rho)
quotient = pairing*pairing/energy
value = endpoint-quotient-norm/4
sym = float(max(np.max(np.abs(U[idx, :]-Us[idx, :].T)),
                np.max(np.abs(T[idx, :]-Ts[idx, :].T))))
archive = BASE/'endpoint-complement-locator-581.npz'
np.savez_compressed(archive, local_matrix=L, t_entries=T, ts_entries=Ts,
    u_entries=U[idx, :], diagonal=D, raw_f_center=raw[0], raw_h_center=raw[1],
    endpoint_matrix=E, finite_forcing=forcing,
    reference_head=H, reference_tail_diagonal=D[N:]/2,
    free_numerators=numerators, trial_numerators=trial_numerators,
    neutral_ratio_centers=r, tail_weights=d, variational_comparison_center=M,
    eigenvalues=vals, physical_index_set=idx)
failures = ['All changed-range entry and arithmetic enclosures unpaid',
    'Exact moment ratios are defined algebraically; saved centers are not exact neutral coefficients',
    'Finite variational directions give no upper bound for the inverse; positive samples cannot prove F>=tail/4',
    'Library eigenvalue/solve results are locators, not certified spectral or sign evidence']
if value >= 0:
    failures.append('Frozen locator direction has nonnegative comparison center; no candidate negative upper certificate')
report = dict(certified=False, outcome='EXPLORATION',
    target='Test whether F(0,y)>=||y||_tail^2/4 fails on exactly neutral endpoint free modes512:1023, retaining signed U and the complete unchanged reference-inverse correction.',
    free_support=[512, 1023], physical_support=[0, 1, '512:1023'],
    trial_support=[0, 1023], denominator=q, remote_powers=len(powers),
    imaginary_free_and_trial_coordinates='exactly zero; independent real endpoints, no reflection constraint',
    diagnostic=dict(weighted_minimum=float(vals[0]), weighted_maximum=float(vals[-1]),
        tail_norm_squared=norm, endpoint_energy=endpoint,
        finite_trial_reference_energy=energy, finite_trial_pairing=pairing,
        inverse_pairing_lower_quotient_center=quotient,
        difference_upper_expression_center=value,
        difference_required_certified_upper_strictly_below=0,
        entry_adjoint_discrepancy=sym,
        free_nonzero_count=int(np.count_nonzero(numerators)),
        trial_nonzero_count=int(np.count_nonzero(trial_numerators))),
    failures=failures,
    input_hashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in
        [BASE/'residual-certificate-532.py', BASE/'complete-covariance-532.npz', source_path]},
    archive=dict(path=str(archive.relative_to(ROOT)),sha256=hashlib.sha256(archive.read_bytes()).hexdigest()),
    script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
path = BASE/'endpoint-complement-locator-581.json'
path.write_text(json.dumps(report,indent=2)+'\n')
print(f'UNCERTIFIED weighted comparison minimum={vals[0]:.12g}; required certified sign<0')
print(f'Frozen dyadic direction: upper-expression CENTER={value:.12g}; denominator CENTER={energy:.12g}; norm² CENTER={norm:.12g}')
print('Failures: '+ '; '.join(failures))
print(f'Certificate record={path.relative_to(ROOT)}; full arrays={archive.relative_to(ROOT)}')
