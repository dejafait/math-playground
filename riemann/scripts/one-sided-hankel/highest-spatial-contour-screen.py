#!/usr/bin/env python3
"""Floating diagnostic to select an exact-contour proof; not a certificate."""
import json
from pathlib import Path
import numpy as np

d, R, U, alpha = 1.25, 1.375, 121/64, 2.7
theta = np.arange(1024) * 2*np.pi/1024
u = np.exp(1j*theta)


def series(z):
    p = np.ones_like(z)
    ans = np.zeros_like(z)
    for j in range(1, 201):
        p *= z
        ans += p/(j*(j+1))
    return ans.real


base = -series(-u/d)+series(-d/(U*u))


def exponent(s, y):
    a = -d+s+1j*y
    F = np.log(d/abs(a))+series(u/a)+base-series(a/(U*u))
    return F+np.log(abs(a)/R)/3-2*np.pi*max(s, 0)/alpha


rows = []
for kind in ['left', 'right', 'horizontal']:
    for p in np.linspace(0, 1, 101):
        s, y = ((-.09, .45*p) if kind == 'left' else
                ((.09, .45*p) if kind == 'right' else (-.09+.18*p, .45)))
        values = exponent(s, y)
        idx = int(np.argmax(values))
        rows.append({'kind': kind, 's': s, 'y': y, 'sample_max': float(values[idx]),
                     'theta_at_sample_max': float(theta[idx]),
                     'all_exponents': [float(v) for v in values]})
    peak = max((z for z in rows if z['kind'] == kind), key=lambda z: z['sample_max'])
    print(f"{kind}: sampled exponent maximum {peak['sample_max']:.12g}, "
          f"s={peak['s']:.6g}, y={peak['y']:.6g}, theta={peak['theta_at_sample_max']:.6g}")
out = Path(__file__).with_suffix('.json')
out.write_text(json.dumps({'status': 'FLOATING DIAGNOSTIC ONLY', 'rows': rows,
                          'required': -.03125, 'failures': [],
                          'limitations': ['Uncertified samples and series tail.',
                                          'No finite-n product bound in this screen.']}, indent=2)+'\n')
print(f"required contour rate (sufficient using constant diagonal): {-1/32}; full output: {out}")
