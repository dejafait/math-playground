"""Find and exactly check a violating point for a rounded probe candidate.

This checks one explicitly rounded candidate, never the whole family.
Run after rational_sos_probe.py --suffix _refined.
"""
from fractions import Fraction as F
from pathlib import Path
import json
import numpy as np

ROOT = Path(__file__).resolve().parent
source = ROOT / 'rational_sos_probe_refined.json'
data = json.loads(source.read_text())
den = 10**9
h = [[F(round(x * den), den) for x in row] for row in data['H']]
p = [F(round(x * den), den) for x in data['P_coefficients']]
si, ai = [0, 1, 3, 4], [2, 5]
exponents = [tuple(m[i] for i in si) for m in data['polynomial_basis']]
hf = np.array([[float(x) for x in row] for row in h])
pf = np.array([float(x) for x in p])
haa = hf[np.ix_(ai, ai)]
has = hf[np.ix_(ai, si)]
hss = hf[np.ix_(si, si)]
eig = np.linalg.eigvalsh(haa)
if eig[0] <= 0:
    raise RuntimeError('Acceleration block is not numerically positive; use another witness search.')
inv = np.linalg.inv(haa)
rng = np.random.default_rng(594)
w = rng.standard_normal((60000, 4))
w /= np.linalg.norm(w, axis=1)[:, None]
qf = np.array([.5, .375, .5, .375])
q = (w*w) @ qf
pv = np.zeros(len(w))
dp = np.zeros_like(w)
for coeff, m in zip(pf, exponents):
    pv += coeff * np.prod(w ** np.array(m), axis=1)
    for j in range(4):
        if m[j]:
            n = list(m)
            n[j] -= 1
            dp[:, j] += coeff * m[j] * np.prod(w ** np.array(n), axis=1)
grad = dp/q[:, None] - pv[:, None] * (2*w*qf)/(q*q)[:, None]
best = None
for branch in (0, 1):
    c = w @ has.T - grad[:, [1, 3]]/4
    c[:, 0] -= branch * w[:, 0]/16
    acc = -c @ inv
    constant = np.sum((w @ hss)*w, axis=1) - grad[:, 0]*w[:, 1]/4 - grad[:, 2]*w[:, 3]/4 + branch*w[:, 1]**2/16
    values = constant + np.sum(c*acc, axis=1)
    k = int(np.argmin(values))
    if best is None or values[k] < best[0]:
        point = np.zeros(6)
        point[si], point[ai] = w[k], acc[k]
        best = (float(values[k]), branch, point)
value, branch, point = best
v = [F(round(x*10**6), 10**6) for x in point]
state = [v[i] for i in si]
def mono(a, m):
    out = F(1)
    for x, n in zip(a, m):
        out *= x**n
    return out
pv = sum((c*mono(state, m) for c, m in zip(p, exponents)), F(0))
dp = []
for j in range(4):
    val = F(0)
    for c, m in zip(p, exponents):
        if m[j]:
            n = list(m)
            n[j] -= 1
            val += c*m[j]*mono(state, n)
    dp.append(val)
qcoeff = [F(1,2), F(3,8), F(1,2), F(3,8)]
q = sum((c*x*x for c, x in zip(qcoeff, state)), F(0))
dq = [2*c*x for c, x in zip(qcoeff, state)]
grad = [(q*a-pv*b)/(q*q) for a,b in zip(dp,dq)]
velocity = [v[1]/4,v[2]/2,v[4]/4,v[5]/2]
dv = sum((a*b for a,b in zip(grad,velocity)), F(0))
quad = sum((h[i][j]*v[i]*v[j] for i in range(6) for j in range(6)), F(0))
obs = v[0]*v[2]/8-v[1]*v[1]/16
residual = quad-dv-branch*obs
cleared = q*q*(quad-branch*obs)-q*sum((a*b for a,b in zip(dp,velocity)),F(0))+pv*sum((a*b for a,b in zip(dq,velocity)),F(0))
k = [[F(x) for x in row] for row in data['spectral_matrix']]
error = [[F(x) for x in row] for row in data['spectral_entry_error']]
cost = sum((h[i][j]*k[i][j] for i in range(6) for j in range(6)), F(0))
costerr = sum((abs(h[i][j])*error[i][j] for i in range(6) for j in range(6)), F(0))
out = dict(
    kind='exact_violation_of_one_rounded_candidate_not_a_family_obstruction',
    source=str(source.relative_to(ROOT.parent.parent)),
    candidate=dict(coefficient_denominator=den, H=[[str(x) for x in row] for row in h],
                   P_coefficients=[str(x) for x in p], state_monomials=exponents),
    witness=dict(coordinates='t=(x,4y,8z,X,4Y,8Z)',point=[str(x) for x in v],branch=branch),
    exact_evaluation=dict(q=str(q), P=str(pv), quadratic=str(quad), DV=str(dv),
                          B=str(obs), branch_residual=str(residual),
                          cleared_residual=str(q*q*residual)),
    exact_cost_interval=[str(cost-costerr),str(cost+costerr)],
    checks=dict(q_positive=q>0, branch_violated=residual<0,
                residual_below_minus_one_over_200=residual<-F(1,200),
                cleared_identity_exact=cleared==q*q*residual,
                cost_in_reported_rational_interval=F(3440040029,10**12)<cost-costerr and cost+costerr<F(3440040031,10**12),
                cost_below_required=cost+costerr<F(1,288)),
    numerical_summary=dict(min_sampled_residual=value, rational_point_residual=float(residual),
                           cost_lower=float(cost-costerr),cost_upper=float(cost+costerr),
                           required_cost=float(F(1,288)),sample_size=60000),
    limitations=['Only this explicitly rounded candidate is refuted.',
                 'The finite random search is a witness finder, not a global positivity or infeasibility test.',
                 'The original floating iterate and entire family remain undecided.'])
path = ROOT / 'rational_probe_candidate_violation.json'
path.write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps(dict(kind=out['kind'],checks=out['checks'],
                     actual_and_required=out['numerical_summary'],limitations=out['limitations']),indent=2))
print('Full exact certificate:',path.relative_to(ROOT.parent.parent))
