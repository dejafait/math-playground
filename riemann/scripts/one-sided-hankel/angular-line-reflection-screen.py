"""Exploratory product-rate screen; floating point is not a certificate."""
import json
from pathlib import Path
import numpy as np

d, R = 1.25, 1.375
U = R * R
t, w = np.polynomial.legendre.leggauss(120)
t = (t + 1) / 2
w = w / 2
phi = 2 * np.pi * np.arange(512) / 512
psi = 2 * np.pi * np.arange(1024) / 1024
z = R * np.exp(1j * psi)
reflected = -2 * d - np.conjugate(z)
rows = []
for angle in phi:
    u = np.exp(1j * angle)
    def logB(v):
        v = np.asarray(v)[..., None]
        return np.log(np.abs(R * (v - t * u) / (U - t * v / u))) @ w
    anchor = float(logB(-d))
    inverse_profile = -logB(reflected)
    j = int(np.argmax(inverse_profile))
    cost = anchor + float(inverse_profile[j])
    rows.append(dict(phi=float(angle), anchor_rate=anchor,
                     inverse_norm_rate=float(inverse_profile[j]),
                     cost=cost, maximizing_boundary_psi=float(psi[j])))
best = min(rows, key=lambda row: row['cost'])
record = dict(kind='UNVERIFIED_DIAGNOSTIC',
              method='120 point Gauss-Legendre, 512 angular, 1024 spatial grid',
              required_root_rate=1/32, best_sampled=best,
              failures=['No quadrature or discretization error enclosure.',
                        'No full-energy comparison or operator upper bound.'],
              rows=rows)
path = Path(__file__).with_suffix('.json')
path.write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(dict(kind=record['kind'], best_sampled=best,
                     required_root_rate=record['required_root_rate'],
                     failures=record['failures'], path=str(path)), indent=2))
