#!/usr/bin/env python3
"""One exact neutral residual coefficient; no inverse or response truncation.

Full entry-error contracts: C744w(12)-(15), C744z(27)-(28).
All scalar operations are directed Decimal; stored binary64 entries are
converted exactly. The source/runtime qualifications remain hypotheses.
"""
import hashlib
import importlib.util
import json
import sys
from decimal import Context, Decimal, ROUND_CEILING, ROUND_FLOOR, ROUND_HALF_EVEN
from pathlib import Path

import numpy as np

BASE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('interval550', BASE/'complete-schur-531.py')
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
precision = int(sys.argv[1]) if len(sys.argv) > 1 else 80
mod.DOWN = Context(prec=precision, rounding=ROUND_FLOOR)
mod.UP = Context(prec=precision, rounding=ROUND_CEILING)
mod.NEAR = Context(prec=precision, rounding=ROUND_HALF_EVEN)
I = mod.I


def ab(x):
    return max(x.lo.copy_abs(), x.hi.copy_abs())


def sq(x):
    if x.lo <= 0 <= x.hi:
        return I(0, mod.UP.multiply(ab(x), ab(x)))
    return x*x


def inflate(x, error):
    return x+I(error.hi.copy_negate(), error.hi)


def l1(x):
    return sum((I(ab(v)) for v in x), I(0))


def power(x, n):
    out = I(1)
    for _ in range(n):
        out *= x
    return out


def atan(q):
    x = I(1)/q
    return inflate(sum((((-1)**j)*power(x, 2*j+1)/(2*j+1)
                        for j in range(80)), I(0)), power(x, 161)/161)


def bilinear(matrix, x, y):
    total = I(0)
    for i, yi in enumerate(y):
        if ab(yi) == 0:
            continue
        row = sum((I(Decimal(float(matrix[i, j])))*xj
                   for j, xj in enumerate(x) if ab(xj) != 0), I(0))
        total += yi*row
    return total


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


failures, hashes = [], []


def check(ok, label):
    if not ok:
        failures.append(label)


prior = json.loads((BASE/'response-prefix-stop-546.json').read_text())
audit = json.loads((BASE/'response-prefix-audit-548.json').read_text())
check(not prior['failures'] and not audit['failures'], 'inherited failures empty')
for record in prior['input_hashes']:
    name = record['path']
    actual = digest(BASE/name)
    expected = record['expected']
    check(actual == expected == audit['input_hashes'][name], 'hash '+name)
    hashes.append(dict(path=name, actual=actual, expected=expected))
direction_file = BASE/'response-prefix-direction-546.json'
direction_hash = digest(direction_file)
check(direction_hash == 'f39d45d9754d0415f5180e2cb5803d8152bfbaba3eb34130b4bf4b91b81da013',
      'exact546 direction hash')
direction = json.loads(direction_file.read_text())
N = direction['modes']
check(N == 512 and direction['denominator'] == 2**40, 'fixed data size/denominator')
pi, ell = 16*atan(5)-4*atan(239), I(3).ln()/2
k = [n*pi/ell for n in range(N)]
k2 = [sq(x) for x in k]
nu = [(I(1 if n == 0 else 2)/ell).sqrt() for n in range(N)]


def neutral(integers):
    check(len(integers) == N-2, 'free coefficient count')
    u = [I(0), I(0)]+[I(x)/direction['denominator'] for x in integers]
    for n in range(2, N):
        p = n % 2
        ratio = (I('.25')+k2[p])/(I('.25')+k2[n])
        if p == 0:
            ratio *= I(2).sqrt()
        u[p] -= ratio*u[n]
    return u


f, g = [neutral(direction[name]) for name in ['f_free_numerators', 'g_free_numerators']]
h = [((-1)**n)*v for n, v in enumerate(f)]
w = [I(0) for _ in range(N)]
w[2] = I(1)
w[0] = -I(2).sqrt()*I('.25')/(I('.25')+k2[2])
check(all(ab(g[n]) == 0 for n in range(1, N, 2)), 'middle even exactly')

with np.load(BASE/'complete-covariance-532.npz') as archive:
    head = archive['m0']
    seven = archive['mc']+archive['mg']

# Entrywise bound for the full D+S+256C*C matrix, used bilinearly.
r64 = [I(2).sqrt()/(6*(I('64.25')*I('64.25')+z/4)) for z in k2]
C = I('131072.5')
t = [1/(C*C)+2*z*(1/(6*power(C, 3))+1/power(C, 4)) for z in k2]
head_error = I('1e-7')*l1(g)*l1(w)
entries = []
for i in [0, 2]:
    for j in range(N):
        if j % 2 or ab(g[j]) == 0:
            continue
        if i == j:
            error = r64[i]+2*sq(nu[i])*t[i]
        else:
            gap = k2[max(i, j)]-k2[min(i, j)]
            error = nu[i]*nu[j]*(k[i]*r64[i]+k[j]*r64[j])/gap
        contribution = error*I(ab(w[i]))*I(ab(g[j]))
        head_error += contribution
        entries.append(dict(row=i, column=j, analytic_error=error.json(),
                            weighted_allowance=contribution.json()))

head_center = bilinear(head, g, w)
head_pair = inflate(head_center, head_error)
t1_center, t2_center = bilinear(seven, f, w), bilinear(seven, w, h)
t1_error, t2_error = [I('2.1e-7')*l1(x)*l1(y) for x, y in [(f, w), (w, h)]]
t1, t2 = inflate(t1_center, t1_error), inflate(t2_center, t2_error)
pair = t1+t2-head_pair
norm_w2 = 1+sq(w[0])
pair_abs_lower = (pair.lo if pair.lo > 0 else pair.hi.copy_negate()
                  if pair.hi < 0 else Decimal(0))
residual_lower = I(pair_abs_lower)*I(pair_abs_lower)/norm_w2
c_star = I('8.9e-18')
quotient_lower = residual_lower/c_star
energy_upper = I('.094207')
pair_required = (c_star*energy_upper*norm_w2).sqrt()
check(pair_abs_lower > pair_required.hi, 'one coefficient rejects majorant')
check(quotient_lower.lo > energy_upper.hi, 'quotient exceeds actual upper energy')
result = dict(scope='fixed546 trial; one full neutral residual coefficient only',
    precision=precision, source_script_sha256=digest(Path(__file__)),
    input_hashes=hashes, direction_sha256=direction_hash,
    coefficients={name: [v.json() for v in values] for name, values in
                  [('f', f), ('g', g), ('h', h), ('w', w)]},
    constants=dict(pi=pi.json(), ell=ell.json(), c_star=c_star.json()),
    analytic_entry_allowances=entries,
    pairings=dict(head_center=head_center.json(), head_error=head_error.json(),
                  head_full=head_pair.json(), Tf_w_center=t1_center.json(),
                  Tw_h_center=t2_center.json(), Tf_w_error=t1_error.json(),
                  Tw_h_error=t2_error.json(), Tf_w=t1.json(), Tw_h=t2.json()),
    summary=dict(residual_pairing=pair.json(), norm_w_squared=norm_w2.json(),
                 residual_norm_squared_lower=residual_lower.json(),
                 residual_majorant_lower=quotient_lower.json(),
                 required_pairing_upper=pair_required.json(),
                 actual_trial_energy_upper=energy_upper.json(),
                 rejects_fixed_majorant=quotient_lower.lo > energy_upper.hi),
    failures=failures,
    qualifications=['Full analytic/IEEE754/Decimal entry contracts inherited.',
                    'c_star source computation unreplayed; neutral construction not wholly audited.',
                    'No sign for exact minimized energy, uniform endpoints, H2, or RH.'])
path = BASE/f'fixed-trial-residual-550-{precision}.json'
path.write_text(json.dumps(result, indent=2)+'\n')
print('Full residual pairing:', pair.lo, pair.hi)
print('Required |pairing| for rejection >', pair_required.hi)
print('Residual majorant >=', quotient_lower.lo, '; required for pass < .093538')
print('Reject if > .094207; failures:', failures)
print('Certificate:', path.relative_to(BASE.parent.parent))
assert not failures
