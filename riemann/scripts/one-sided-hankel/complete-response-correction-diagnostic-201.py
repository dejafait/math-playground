"""Nonrigorous rate screen for step 201; no sampled value is a proof."""
import cmath
import json
import math
from pathlib import Path

d, U, A, c0 = 1.25, 121 / 64, 2.7, 0.125
u = 0.3 + 0.4j
N = 2000
ts = [(j + 0.5) / N for j in range(N)]

def q(t, y):
    return (d + t*u)*(U*u + (d - 1j*y)*t)/((U*u+d*t)*(d+t*u-1j*y))

def phi(y):
    return sum(math.log(abs(q(t, y))) for t in ts) / N

physical = [{"y": y, "rate": phi(y)} for y in [-10, -2, -1, -0.6, -0.45, -0.44, -0.425, -0.4, -0.3, -0.2, 0, 0.2, 0.4, 0.45, 1, 2, 10]]
moment = []
for j in range(901):
    y = -0.45 + j / 1000
    moment.append({"y": y, "rate": phi(y) + math.log((d*d+y*y)/U)/6})
tilts = []
for theta in [0, 0.025, 0.05, 0.075, 0.1, 0.125, 0.15, 0.2, 0.25]:
    total = 0.0
    for t in ts:
        lam = d+t*u
        r = t*lam/(U*u+d*t)
        total += math.log(abs(r)+abs(1-r)*abs(lam)/(lam.real-A*theta))
    z = total/N
    tilts.append({"theta":theta, "log_mass_rate":z, "tail_rate_at_9_over_4":z-2.25*theta})
result = {"status":"FLOATING_POINT_DIAGNOSTIC_ONLY", "method":"midpoint integration, 2000 cells", "required_correction_rate_strictly_below":0.005, "physical":physical, "moment":moment, "moment_max":max(moment,key=lambda x:x['rate']), "tilts":tilts, "resolvent_pole_rate":phi(1j*c0), "failures":[], "qualification":"No rigorous error bounds; no conclusion about an infinite domain from the samples."}
C = d*d-U/4
def global_square_excess(t):
    ell = abs(d+u*t)**2
    beta = abs(U*u+d*t)**2
    e = 2*d*u.real*t+(t*t+U)/4
    return (U-t*t)*(2*u.imag*C*t)**2/(4*e*beta*ell)
def tilted_mass(t):
    lam = d+t*u
    r = t*lam/(U*u+d*t)
    return abs(r)+abs(1-r)*abs(lam)/(lam.real-A/5)
result['elementary_majorants'] = {
    'half_integral_global_square_excess':sum(global_square_excess(t) for t in ts)/(2*N),
    'half_integral_tail_square_excess_at_2_over_5':sum(abs(q(t,-0.4))**2-1 for t in ts)/(2*N),
    'mean_tilted_mass_at_1_over_5':sum(tilted_mass(t) for t in ts)/N,
    'moment_norm_cost':math.log((d*d+0.45**2)/U)/6,
}
path = Path(__file__).with_suffix('.json')
path.write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps({"status":result['status'],"required_rate":0.005,"elementary_majorants":result['elementary_majorants'],"certificate":str(path)},indent=2))
