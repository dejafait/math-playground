"""Floating design of a parameter-interpolation contour; not a certificate."""
import json
from pathlib import Path
import numpy as np

x, U, r = -1.25, 121 / 64, .45
nodes, weights = np.polynomial.legendre.leggauss(80)
t, weights = (nodes + 1) / 2, weights / 2
u = np.exp(2j * np.pi * np.arange(512) / 512)
base = np.log(np.abs(x - t[:, None] * u)) - np.log(np.abs(U * u - t[:, None] * x))


def envelope(s, y):
    a = x + s + 1j * y
    vals = np.sum(weights[:, None] *
                  (base - np.log(np.abs(a - t[:, None] * u))
                   + np.log(np.abs(U * u - t[:, None] * a))), axis=0)
    k = int(np.argmax(vals))
    return float(vals[k]), k


def primitive(s, v):
    if s == 0:
        return v * np.log(abs(v)) - v if v else 0.
    return .5 * v * np.log(s*s + v*v) - v + s * np.arctan(v/s)


def kernel(s, y):
    return (2*r*(np.log(r)-1) - primitive(abs(s), y+r)
            + primitive(abs(s), y-r)) / 2.7


rows = []
for width in (.03, .05, .07, .09, .11, .13):
    plus, minus = [], []
    for y in np.linspace(-.5, .5, 101):
        for s, dest in ((width, plus), (-width, minus)):
            val, arg = envelope(s, y)
            dest.append(dict(s=s, y=float(y), envelope=val,
                             maximizing_angle_index=arg, kernel=float(kernel(s,y))))
    p = max(v['envelope']+v['kernel'] for v in plus)
    m = max(v['envelope']+v['kernel'] for v in minus)
    center = (p-m)/(2*width)
    top = []
    for s in np.linspace(-width, width, 41):
        val, arg = envelope(s, .5)
        top.append(dict(s=float(s), y=.5, envelope=val,
                        maximizing_angle_index=arg, kernel=float(kernel(s,.5))))
    side_bound = (p+m)/2
    top_bound = max(v['envelope']-center*v['s']+v['kernel'] for v in top)
    rows.append(dict(width=width, center=center, side_exponent=side_bound,
                     top_exponent=top_bound, plus=plus, minus=minus, top=top))
    print(f'width={width}: center={center:.8g}, side exponent={side_bound:.8g}, '
          f'top exponent={top_bound:.8g}, required <= -.01', flush=True)
out = Path(__file__).with_suffix('.json')
out.write_text(json.dumps(dict(status='FLOATING_DESIGN_ONLY',
                              angular_points=512, legendre_nodes=80,
                              failures=[], rows=rows), indent=2)+'\n')
print('Full diagnostic:', out)
print('No uniform contour or asymptotic claim certified.')
