#!/usr/bin/env python3
"""Bounded diagnostic for the inherited head-inverse uncertainty ball.

No actual mixed-map bound is claimed. The saved FFT rows are treated as
arbitrary exact dyadic centers, not as accurate operator evaluations.
"""
import importlib.util
import json
from pathlib import Path
import numpy as np

BASE = Path(__file__).resolve().parent
N, K, E = 512, 65536, 1020
spec = importlib.util.spec_from_file_location('entry572', BASE/'residual-certificate-532.py')
old = importlib.util.module_from_spec(spec)
spec.loader.exec_module(old)
con = old.constants()
ell, pi = con['ell'], con['pi']
nn = np.arange(K)
k = nn*pi/ell
nu = np.full(K, np.sqrt(2/ell)); nu[0] = 1/np.sqrt(ell)
parity = np.where(nn % 2 == 0, 1., -1.)
with np.load(BASE/'signed-mixed-complete-locator-565.npz') as data:
    x = data['x']
with np.load(BASE/'neutral-head-covariance-559.npz') as data:
    mc = data['comparison_lower']
with np.load(BASE/'complete-covariance-532.npz') as data:
    t0 = data['mc']+data['mg']
raw = np.load(BASE/'signed-mixed-columns-565.npy', mmap_mode='r')
d = np.log(nn[N:]/(2*ell))-2*ell*ell/(9*nn[N:]**2)
r = (.25+k[nn[N:] % 2]**2)/(.25+k[N:]**2)*np.where(nn[N:] % 2 == 0,np.sqrt(2),1.)
a = np.empty((2,K-N))
low = np.array([raw[side,:2]@x for side in range(2)])
for start in range(N,K,N):
    for side in range(2):
        a[side,start-N:start] = raw[side,start:start+N]@x-r[start-N:start]*low[side,nn[start:start+N] % 2]

def rectangles(start):
    rows = slice(start,start+N)
    kn, km = k[rows,None], k[None,:N]
    signs = parity[rows,None]*parity[None,:N]
    tt, ts = np.zeros((N,N)), np.zeros((N,N))
    normalization = np.outer(nu[rows],nu[:N])
    for delta, weight in zip(con['deltas'],con['weights']):
        for delay, matrix in [(delta,tt),(-delta,ts)]:
            sn,_ = old.sincos(k[rows]*delay,pi)
            sm,_ = old.sincos(k[:N]*delay,pi)
            numerator = (-signs*kn*sn[:,None]+km*sm[None,:]) if delay>0 else (kn*sn[:,None]-signs*km*sm[None,:])
            matrix += weight*numerator/(kn*kn-km*km)*normalization
    for j in range(1,8):
        c = 2*j+.5
        decay = 3.**(-j)/con['fourth']
        minus = nu*c*(1-parity*decay)/(c*c+k*k)
        plus = nu*c*(parity-decay)/(c*c+k*k)
        prefactor = 3.**(-6*j)/(3*np.sqrt(3.))
        tt += prefactor*np.outer(minus[rows],plus[:N])
        ts += prefactor*np.outer(plus[rows],minus[:N])
    return tt, ts

gradient = np.zeros(N)
for start in range(N,K,N):
    tt,ts = rectangles(start)
    rr = r[start-N:start]
    pp = nn[start:start+N] % 2
    ts -= rr[:,None]*t0.T[pp]
    tt -= rr[:,None]*t0[pp]
    gradient += ts.T@(a[0,start-N:start]/d[start-N:start])+tt.T@(a[1,start-N:start]/d[start-N:start])
    if start % 16384 == 0:
        print('Head-error gradient through',start+N-1,flush=True)
q = gradient/np.linalg.norm(gradient)*.99999
tq = np.empty_like(a)
for start in range(N,K,N):
    tt,ts = rectangles(start)
    rr = r[start-N:start]
    pp = nn[start:start+N] % 2
    tq[0,start-N:start] = ts@q-rr*(t0.T@q)[pp]
    tq[1,start-N:start] = tt@q-rr*(t0@q)[pp]
rho = .00196
den = float(x@mc@x)
center = float(np.sum(a*a/d))/den
perturbed = float(np.sum((a+rho*tq)**2/d))/den
np.savez_compressed(BASE/'signed-mixed-head-error-locator-572.npz',x=x,q=q,center_action=a,shift_action=tq,comparison=mc)
record = dict(certified=False,scope='Unstructured head inverse error ball around the exact saved dyadic mixed rows',
    N=N,K=K,perturbation_rho=rho,x_norm=float(np.linalg.norm(x)),q_norm=float(np.linalg.norm(q)),
    head_denominator=den,center_ratio=center,perturbed_ratio=perturbed,required_finite_upper=.085440,
    shift_action_norm=float(np.sqrt(np.sum(tq*tq/d))),gradient_norm=float(np.linalg.norm(gradient)),
    quarter_decided=False,failures=['This locator has no directed scalar or operator-entry certificate'])
(BASE/'signed-mixed-head-error-locator-572.json').write_text(json.dumps(record,indent=2)+'\n')
print('UNCERTIFIED center and uncertainty-family ratios:',center,perturbed,'; sufficient finite threshold .085440')
print('Artifact: scripts/separation-seven/signed-mixed-head-error-locator-572.json')
