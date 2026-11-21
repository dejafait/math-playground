#!/usr/bin/env python3
"""Uncertified finite-column locator for the fixed assessment562 test.

The reference, predictor, head and final output cutoff K=65536 are fixed.
This locator initially omits complementary inverse-action outputs; that
omission has no sign and MUST be paid before any rejection or pass.
"""
import hashlib
import importlib.util
import json
from pathlib import Path
import numpy as np

BASE = Path(__file__).resolve().parent
N, K, J = 512, 65536, 1024
spec = importlib.util.spec_from_file_location('entries564', BASE/'residual-certificate-532.py')
old = importlib.util.module_from_spec(spec)
spec.loader.exec_module(old)
con = old.constants()
ell, pi = con['ell'], con['pi']
nn = np.arange(J)
k = nn*pi/ell
nu = np.full(J, np.sqrt(2/ell)); nu[0] /= np.sqrt(2)
parity = np.where(nn % 2 == 0, 1., -1.)
rows, cols = np.arange(N, J), np.arange(N)
kn, km = k[rows, None], k[None, cols]
signs = parity[rows, None]*parity[None, cols]
norm = np.outer(nu[rows], nu[cols])


def shift(delta):
    if delta == 0:
        return np.zeros((J-N, N))
    sn, _ = old.sincos(k[rows]*delta, pi)
    sm, _ = old.sincos(k[cols]*delta, pi)
    numerator = (-signs*kn*sn[:, None]+km*sm[None, :]
                 if delta > 0 else kn*sn[:, None]-signs*km*sm[None, :])
    return norm*numerator/(kn*kn-km*km)


def continuous(separation):
    tt, ts = np.zeros((J-N, N)), np.zeros((J-N, N))
    for j in range(1, 8):
        c = 2*j+.5
        decay = 3.**(-j)/con['fourth']
        minus = nu*c*(1-parity*decay)/(c*c+k*k)
        plus = nu*c*(parity-decay)/(c*c+k*k)
        scale = np.exp(-(separation-1)*ell*c)
        tt += scale*np.outer(minus[rows], plus[cols])
        ts += scale*np.outer(plus[rows], minus[cols])
    return tt, ts


tt, ts = continuous(7)
for delay, weight in zip(con['deltas'], con['weights']):
    tt += weight*shift(delay)
    ts += weight*shift(-delay)
uu, us = continuous(14)
source = json.loads((BASE/'response-prefix-stop-546.json').read_text())
prime_rows = source['remote']['primes']
for row in prime_rows:
    weight = float(row['weight']['lo'])
    delay = float(row['delta']['lo'])
    if row['n'] == 2187:
        delay = 0.
    uu += weight*shift(delay)
    us += weight*shift(-delay)

imag, _ = old.psi_imag(k, pi)
b = k*imag/2
ss = (b[rows, None]-b[None, cols])/(kn*kn-km*km)
for j in range(64):
    c = 2*j+.5
    ss -= (3.**(-j)/con['fourth'])*parity[rows, None]*c*c/((c*c+kn*kn)*(c*c+km*km))
ss *= 2*norm*(signs == 1)
mom = np.array([nu*c*(parity*(con['fourth'] if c > 0 else 1/con['fourth'])-1)/(c*c+k*k)
                for c in [.5, -.5]])
w0 = ss+256*mom[:, rows].T@mom[:, cols]
with np.load(BASE/'complete-covariance-532.npz') as z:
    m0, t0 = z['m0'], z['mc']+z['mg']
with np.load(BASE/'response-prefix-remote-546.npz') as z:
    u0 = z['remote_prime']
with np.load(BASE/'neutral-head-covariance-559.npz') as z:
    zh, g, solution, mc = z['z'], z['predictor_raw'], z['head_solution'], z['comparison_lower']
    output_finite, output_tail = z['finite_covariance'], z['tail_covariance_upper']
correction = np.zeros((N, J-N))
rp = (.25+k[rows % 2]**2)/(.25+k[rows]**2)*np.where(rows % 2 == 0, np.sqrt(2), 1.)
correction[rows % 2, np.arange(J-N)] = -rp
aa = zh.T@(w0.T+m0@correction)
ur = (uu@zh+correction.T@u0@zh).T
usr = (us@zh+correction.T@u0.T@zh).T
forcing_head = np.hstack((ts.T+t0@correction, tt.T+t0.T@correction))
mixed = np.block([[aa, -ur], [-usr, aa]])-(g+solution).T@forcing_head
dt = np.log(rows/(2*ell))-2*ell*ell/(9*rows*rows)
weights = np.concatenate((dt, dt))
chol = np.linalg.cholesky(mc)
white = np.linalg.solve(chol, mixed)/np.sqrt(weights)[None, :]
eigenvalues, eigenvectors = np.linalg.eigh(white@white.T)
v = eigenvectors[:, -1]
x = np.linalg.solve(chol.T, v)
x /= np.linalg.norm(x)
y = (x@mixed)/weights
y /= np.sqrt(np.dot(weights*y, y))
cross, head = float(x@mixed@y), float(x@mc@x)
out = BASE/'signed-mixed-diagnostic-564.npz'
np.savez_compressed(out, mixed_head_output_only=mixed, x=x, y=y,
                    weights=weights, moment_ratios=rp, comparison=mc,
                    t_tail_head=tt, ts_tail_head=ts, u_tail_head=uu,
                    us_tail_head=us, w_tail_head=w0)
report = dict(certified=False, scope='unchanged assessment562; finite input subset512:1023; inverse output head only',
              input_first=512, input_last=1023, required_final_output_K=K,
              diagnostic_generalized_ratio=float(eigenvalues[-1]), required_ratio_upper=.25,
              head_quarter=head/4, mixed_pairing=cross, mixed_pairing_square_diagnostic=cross*cross,
              failures=['Complementary inverse-action outputs512:infinity unpaid',
                        'All entry, predictor, solve and arithmetic enclosures unpaid',
                        'No full input covariance or quarter-budget conclusion'],
              archive=str(out.relative_to(BASE.parent.parent)),
              archive_sha256=hashlib.sha256(out.read_bytes()).hexdigest(),
              source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
path = BASE/'signed-mixed-diagnostic-564.json'
path.write_text(json.dumps(report, indent=2)+'\n')
print(f'UNCERTIFIED ratio={eigenvalues[-1]:.12g}; required<=.25; pairing={cross:.12g}; square={cross*cross:.12g}; head/4={head/4:.12g}')
print('Unpaid: complementary inverse output, arithmetic and input completion. No sign conclusion.')
print(f'Report={path.relative_to(BASE.parent.parent)}; arrays={out.relative_to(BASE.parent.parent)}')


def relative_output_center(covariance):
    value = np.linalg.solve(chol, covariance)
    value = np.linalg.solve(chol, value.T).T
    return float(np.linalg.eigvalsh((value+value.T)/2)[-1])


output_report = dict(certified=False,
    diagnostic_output_covariance_relative=relative_output_center(output_finite+output_tail),
    diagnostic_finite_output_covariance_relative=relative_output_center(output_finite),
    diagnostic_tail_output_covariance_relative=relative_output_center(output_tail),
    limitations=['Saved centers plus old tail upper only; changed weighted predictor/roundoff not paid',
                 'Not a mixed covariance or budget decision'],
    source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
output_path = BASE/'signed-mixed-output-diagnostic-564.json'
output_path.write_text(json.dumps(output_report, indent=2)+'\n')
print(f'Uncertified relative output covariance={output_report["diagnostic_output_covariance_relative"]:.12g}; no mixed bound; report={output_path.relative_to(BASE.parent.parent)}')
