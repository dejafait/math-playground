#!/usr/bin/env python3
"""Nonrigorous midpoint screen for the exact step-299 quadratic forms.

Full matrices and vectors are stored; no matrix eigenvalue is a proof
about the smooth class. Exterior pairs are included analytically.
"""
import json
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
a = np.log(2.0)
b = 2 * np.log(3.0)
c = np.sqrt(2.0) * np.log(2.0)
records = []
for n in (128, 256, 512):
    d = b / n
    r = (np.arange(n) + 0.5) * d
    distance = np.abs(r[:, None] - r[None, :])
    np.fill_diagonal(distance, np.inf)
    kernel = (1 / distance + 1 / (r[:, None] + r[None, :])) / np.sqrt(r[:, None] * r[None, :])
    root = np.sqrt(r)
    W = np.arctanh(np.sqrt(r / b)) + np.arctan(np.sqrt(r / b))
    RB = d*d * root[:, None] * (np.diag(kernel.sum(axis=1)) - kernel) * root[None, :] + 2*d*np.diag(W)
    # Full symmetric midpoint grid and linear interpolation of the shift.
    y = (np.arange(2*n) + 0.5) * d - b
    fold = np.concatenate((np.arange(n)[::-1], np.arange(n)))
    sample = np.zeros((2*n, n))
    sample[np.arange(2*n), fold] = 1
    shift = np.zeros_like(sample)
    for j, yy in enumerate(y-a):
        p = (yy+b)/d - 0.5
        lo = int(np.floor(p))
        for k, w in ((lo, 1-(p-lo)), (lo+1, p-lo)):
            if 0 <= k < 2*n:
                shift[j, fold[k]] += w
    Q = c*d*(sample.T @ shift + shift.T @ sample)/2
    moment = np.cosh(r/2)
    moment /= np.linalg.norm(moment)
    # Householder basis for the exact discrete moment nullspace.
    v = moment.copy()
    v[0] += 1
    v /= np.linalg.norm(v)
    U = (np.eye(n) - 2*np.outer(v,v))[:, 1:]
    R = U.T @ RB @ U
    S = U.T @ Q @ U
    C = np.linalg.cholesky(R)
    A = np.linalg.solve(C, S)
    A = np.linalg.solve(C, A.T).T
    eig, vec = np.linalg.eigh(A)
    coeff = np.linalg.solve(C.T, vec[:, -1])
    h = U @ coeff
    h /= np.sqrt(2*d*np.dot(h,h))
    value_R = float(h @ RB @ h)
    value_Q = float(h @ Q @ h)
    entry = dict(n=n, ratio=float(eig[-1]), required_upper=0.5,
                 RB=value_R, Q2=value_Q, Q2_minus_half_RB=value_Q-value_R/2,
                 discrete_moment=float(2*d*np.dot(np.cosh(r/2),h)),
                 radius=r.tolist(), h=h.tolist())
    records.append(entry)
    np.savez_compressed(HERE / f'neutral-even-preview-299-n{n}.npz',
                        r=r, RB=RB, Q2=Q, h=h, moment=moment)
    print(f'n={n}: preview max Q2/RB={eig[-1]:.10f}; required <=0.5; '
          f'Q2={value_Q:.10f}; RB={value_R:.10f}; NOT CERTIFIED', flush=True)

result = dict(status='NONRIGOROUS_PREVIEW', target='Q2 <= RB/2',
              limitations=['midpoint quadrature', 'linear shift interpolation',
                           'discrete moments', 'no smoothness or continuum error bound'],
              records=records)
path = HERE / 'neutral-even-preview-299.json'
path.write_text(json.dumps(result, indent=2)+'\n')
print(f'Full preview: {path.relative_to(HERE.parent.parent)}')
