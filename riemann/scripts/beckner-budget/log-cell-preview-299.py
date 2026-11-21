#!/usr/bin/env python3
"""Diagnostic only: exact elementary shift integrals on logarithmic cells.

The resource exponential series, moments, and eigensystem use floating
arithmetic. Piecewise profiles are not the target smooth functions.
"""
import json
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
a = np.log(2.)
b = 2*np.log(3.)
c = np.sqrt(2.)*np.log(2.)
records = []
for length, delta in ((6., .05), (12., .05), (24., .05), (24., .025)):
    n = round(length/delta)
    t = np.log(b) - np.arange(n, -1, -1)*delta
    r = np.exp(t)
    # RB= sum_m [(4d/beta)I-2K_beta], beta=2m+1/2.
    beta = 2*np.arange(20000)+.5
    eb = np.exp(-beta*delta)
    diag = float(np.sum(4*(1-eb)/beta**2))
    row = np.zeros(n)
    row[0] = diag
    weights = -2*(1-eb)**2/beta**2
    for j in range(1,n):
        row[j] = np.sum(weights*np.exp(-beta*delta*(j-1)))
    # Analytic leading tail; the omitted exponentially small remainder
    # and quadrature/rounding have NOT been interval certified.
    tail = 1/(4*(20000-.25))
    row[0] += 4*tail
    row[1] -= 2*tail
    idx = np.abs(np.arange(n)[:,None]-np.arange(n)[None,:])
    RB = row[idx]
    lo = np.maximum(r[:-1,None], r[None,:-1]-a)
    hi = np.minimum(r[1:,None], r[None,1:]-a)
    same = np.where(hi>lo, 2*(np.arcsinh(np.sqrt(np.maximum(hi,0)/a))-
                             np.arcsinh(np.sqrt(np.maximum(lo,0)/a))),0)
    lo = np.maximum(r[:-1,None], a-r[None,1:])
    hi = np.minimum(r[1:,None], a-r[None,:-1])
    opposite = np.where(hi>lo,2*(np.arcsin(np.sqrt(np.clip(hi/a,0,1)))-
                                np.arcsin(np.sqrt(np.clip(lo/a,0,1)))),0)
    Q = c*(same+same.T+opposite)
    nodes, weights = np.polynomial.legendre.leggauss(16)
    left, right = np.sqrt(r[:-1]),np.sqrt(r[1:])
    ss = (left[:,None]+right[:,None])/2+(right-left)[:,None]*nodes/2
    moment = 2*(right-left)*(np.cosh(ss**2/2)@weights)
    moment /= np.linalg.norm(moment)
    v = moment.copy()
    v[0] += 1
    v /= np.linalg.norm(v)
    U = (np.eye(n)-2*np.outer(v,v))[:,1:]
    R = U.T@RB@U
    S = U.T@Q@U
    C = np.linalg.cholesky(R)
    A = np.linalg.solve(C,S)
    A = np.linalg.solve(C,A.T).T
    eig, vec = np.linalg.eigh(A)
    profile = U@np.linalg.solve(C.T,vec[:,-1])
    Rval = float(profile@RB@profile)
    Qval = float(profile@Q@profile)
    beta0 = .5
    exp0 = np.exp(-beta0*delta)
    row0 = -2*(1-exp0)**2/beta0**2*np.exp(-beta0*delta*(np.arange(n)-1))
    row0[0] = 4*(1-exp0)/beta0**2
    R0 = U.T@row0[idx]@U
    C0 = np.linalg.cholesky(R0)
    A0 = np.linalg.solve(C0,S)
    A0 = np.linalg.solve(C0,A0.T).T
    top0 = float(np.linalg.eigvalsh(A0)[-1])
    records.append(dict(length=length,delta=delta,n=n,ratio=float(eig[-1]),
                        first_exponential_ratio=top0,
                        required_upper=.5,RB=Rval,Q2=Qval,
                        t=t.tolist(),profile=profile.tolist()))
    np.savez_compressed(HERE/f'log-cell-preview-299-n{n}-d{delta}.npz',
                        t=t,RB=RB,Q2=Q,profile=profile,moment=moment)
    print(f'length={length:g}, d={delta:g}, n={n}: preview max Q2/RB={eig[-1]:.10f}; '
          f'Q2/R0={top0:.10f}; required <=0.5; NOT CERTIFIED',flush=True)

path = HERE/'log-cell-preview-299.json'
path.write_text(json.dumps(dict(status='NONRIGOROUS_PREVIEW',records=records,
                               limitations=['floating arithmetic','truncated resource series',
                                             'quadrature moments','finite nonsmooth trial space',
                                             'no continuum upper bound']),indent=2)+'\n')
print(f'Full preview: {path.relative_to(HERE.parent.parent)}')
