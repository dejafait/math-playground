"""Floating real-crossing design only; no continuous or finite-n bound."""
import json
import math
from pathlib import Path
import numpy as np

d, U, r = 1.25, 121/64, .45
c = 10*math.pi/27


def S(v):
    return 1+(1/v-1)*math.log1p(-v)


def F(s):
    a = d-s
    return math.log(d/a)+S(1/a)-S(1/d)+S(d/U)-S(a/U)


def K(s):
    return (10/27)*(r*math.log(r*r/(s*s+r*r))
                   -2*s*math.atan(r/s))


rows = []
for j in range(1, 25000):
    s = j/100000
    value = (F(s)-F(-s))/2-c*s+K(s)
    rows.append(dict(s=s, exponent=value))
best = min(rows, key=lambda row: row['exponent'])
report = dict(status='FLOATING DESIGN ONLY; NOT A BOUND',
              required_upper=-.01, sampled_minimum=best, samples=rows,
              derivative_at_zero=math.log(5)+1.21*math.log(121/41)-.8-2*c,
              failures=[],
              qualifications='No continuous enclosure, optimality, '
              'finite-n estimate, cone-distance or signed-integral bound.')

# A bounded horizontal-slice diagnostic, keeping both rational factors.
def complex_S(v):
    return (1+(1/v-1)*np.log(1-v)).real


def angular_F(z, u):
    a = -d+z
    return (np.log(d/np.abs(a))+complex_S(u/a)-complex_S(-u/d)
            +complex_S(-d/(U*u))-complex_S(a/(U*u)))


def primitive(s, v):
    return v*np.log(s*s+v*v)/2-v+s*np.arctan2(v, s)


def complex_K(z):
    s, y = abs(z.real), z.imag
    return (10/27)*(2*r*(np.log(r)-1)
                   -primitive(s, y+r)+primitive(s, y-r))


angles = np.arange(2048)*(2*np.pi/2048)
u = np.exp(1j*angles)
slice_rows = []
for y in [0, .01, .02, .04, .06, .08, .1, .15, .2, .3, .4, .44]:
    values = []
    for j in range(1, 500):
        s = j/2000
        z = s+1j*y
        vals = angular_F(z, u)
        ix = int(np.argmax(vals))
        value = float(vals[ix]-(angular_F(z, -1)+angular_F(-z, -1))/2
                      -c*s+complex_K(z))
        values.append(dict(s=s, exponent=value, angle_index=ix))
    slice_rows.append(dict(y=y, samples=values,
                          sampled_minimum=min(values, key=lambda v:v['exponent'])))
report['slices'] = slice_rows
report['angle_count'] = len(angles)
path = Path(__file__).with_suffix('.json')
path.write_text(json.dumps(report, indent=2)+'\n')
print('Sampled real-crossing minimum:', best, '; required upper < -0.01')
print('Slice minima:', [(row['y'], row['sampled_minimum']) for row in slice_rows])
print('Execution failures:', report['failures'], '; full diagnostic:', path)
