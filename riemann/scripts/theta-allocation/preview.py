"""Nonrigorous selection only; exactly the approved 4096-point grid."""
import json
from pathlib import Path
import numpy as np

ROOT = Path(__file__).parent
nodes, weights = np.polynomial.legendre.leggauss(128)

def kernel(u, derivative=False):
    u = np.asarray(u)
    out = np.zeros_like(u)
    for n in range(1, 6):
        v = np.pi*n*n*np.exp(2*u)
        poly = -16*v**3+60*v**2-30*v if derivative else 8*v**2-12*v
        out += np.exp(u/2-v)*poly
    return out

def tail(u):
    u = np.asarray(u)
    t = (5-u[..., None])*(nodes+1)/2+u[..., None]
    return (5-u)/2*np.sum(weights*t*kernel(t), axis=-1)

rows = []
for j in range(1, 65):
    a = j/16
    b = a*(nodes+1)/2
    kb, hb = kernel(b), tail(b)
    ka, ha, da = float(kernel(a)), float(tail(a)), float(kernel(a, True))
    for x in range(1, 65):
        if ka == 0:
            continue
        q = a+(ha/ka)*(da/ka)
        s = a/2*np.sum(weights*kb*np.cos(x*b))
        bigk = (np.cos(x*(a+b))+np.cos(x*(a-b))
                +x*(a-b)*np.sin(x*(a+b))+x*(a+b)*np.sin(x*(a-b)))
        r = a*np.sum(weights*(ka*hb-ha*kb)*bigk)
        val = 4*q*s*s+r
        if np.isfinite(val):
            rows.append(dict(x=x, a_numerator=j, a_denominator=16,
                             unnormalized_preview=float(val), layer=float(4*q*s*s),
                             remainder=float(r)))
rows.sort(key=lambda z: z['unnormalized_preview'])
data = dict(status='NONRIGOROUS_PREVIEW_ONLY', grid='x=1..64, a=j/16 j=1..64',
            grid_size=4096, finite_evaluations=len(rows),
            skipped_underflow_points=4096-len(rows),
            implementation_correction='Initial preview derivative used 56*v^2; corrected to 60*v^2 by exact differentiation before candidate certification. Initial negative layer was invalid.',
            selection='least finite unnormalized value; stop on first certified negative; at most three',
            candidates=rows[:3], rows=rows)
(ROOT/'preview.json').write_text(json.dumps(data, indent=2)+'\n')
print(json.dumps({k:v for k,v in data.items() if k!='rows'}, indent=2))
