#!/usr/bin/env python3
"""Certify one exact-neutral D+S_32 middle-comparison obstruction.

Directed Decimal scalar products; audited C744w head entry bounds;
new remote matrix with the explicit binary64 ledger in C744z Section8.
No eigenvalue or finite inverse enters the verification.
"""
import hashlib
import importlib.util
import json
import math
from decimal import Decimal
from pathlib import Path

import numpy as np

BASE = Path(__file__).resolve().parent


def module(name, filename):
    spec = importlib.util.spec_from_file_location(name, BASE / filename)
    out = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(out)
    return out


mod = module('interval546', 'complete-schur-531.py')
entries = module('entries546', 'residual-certificate-532.py')
I = mod.I


def ab(x):
    return max(x.lo.copy_abs(), x.hi.copy_abs())


def square(x):
    if x.lo <= 0 <= x.hi:
        return I(0, mod.UP.multiply(ab(x), ab(x)))
    return x*x


def inflate(x, error):
    return x+I(error.hi.copy_negate(), error.hi)


def power(x, n):
    out = I(1)
    for _ in range(n):
        out *= x
    return out


def atan_reciprocal(q):
    x = I(1)/q
    total = sum((((-1)**j)*power(x, 2*j+1)/(2*j+1)
                 for j in range(80)), I(0))
    return inflate(total, power(x, 161)/161)


def norm2(x):
    return sum((square(v) for v in x), I(0))


def l1(x):
    return sum((I(ab(v)) for v in x), I(0))


def bilinear(matrix, x, y):
    # All saved binary64 entries are converted exactly, then summed outward.
    out = I(0)
    for i, yi in enumerate(y):
        if yi.lo == yi.hi == 0:
            continue
        row = I(0)
        for j, xj in enumerate(x):
            if xj.lo == xj.hi == 0:
                continue
            row += I(Decimal(float(matrix[i, j])))*xj
        out += yi*row
    return out


direction_path = BASE/'response-prefix-direction-546.json'
direction = json.loads(direction_path.read_text())
N = direction['modes']
assert N == 512 and direction['response_prefix'] == 32
pi = 16*atan_reciprocal(5)-4*atan_reciprocal(239)
ell = I(3).ln()/2
fourth = I(3).sqrt().sqrt()
k = [n*pi/ell for n in range(N)]
k2 = [square(x) for x in k]
nu = [(I(1 if n == 0 else 2)/ell).sqrt() for n in range(N)]
alpha = [I(2).sqrt()*x for x in nu]
eta = [(-1)**n for n in range(N)]


def neutral(numerators):
    assert len(numerators) == N-2
    out = [I(0), I(0)]+[I(x)/direction['denominator'] for x in numerators]
    for n in range(2, N):
        p = n % 2
        ratio = (I('.25')+k2[p])/(I('.25')+k2[n])
        if p == 0:
            ratio *= I(2).sqrt()
        out[p] -= ratio*out[n]
    return out


f = neutral(direction['f_free_numerators'])
g = neutral(direction['g_free_numerators'])
h = [eta[n]*f[n] for n in range(N)]
assert all(g[n].lo == g[n].hi == 0 for n in range(1, N, 2))

# Pin the already-audited inputs; do not regenerate or mutate them.
audit = json.loads((BASE/'matrix-tail-audit-541.json').read_text())
input_hashes = []
for name in ['complete-covariance-532.npz', 'complete-schur-531.py',
             'residual-certificate-532.py']:
    expected = next(x['expected'] for x in audit['input_hashes'] if x['path'] == name)
    actual = hashlib.sha256((BASE/name).read_bytes()).hexdigest()
    assert actual == expected
    input_hashes.append(dict(path=name, actual=actual, expected=expected))
with np.load(BASE/'complete-covariance-532.npz') as saved:
    a = saved['m0'].copy()
    # This addition's roundoff is charged in the 2.1e-7 T entry allowance.
    t = saved['mc']+saved['mg']

# C744w(12)-(15): directional, complete analytic head error plus 1e-7.
r64 = [I(2).sqrt()/(6*(I('64.25')*I('64.25')+x/4)) for x in k2]
cj = I('131072.5')
diag_response_error = [1/(cj*cj)+2*x*(1/(6*power(cj, 3))+1/power(cj, 4))
                       for x in k2]


def head_error(x):
    total = I('1e-7')*square(l1(x))
    for n in range(N):
        total += square(x[n])*(r64[n]+2*square(nu[n])*diag_response_error[n])
        for m in range(n % 2, n, 2):
            entry = nu[n]*nu[m]*(k[n]*r64[n]+k[m]*r64[m])/(k2[n]-k2[m])
            total += 2*entry*I(ab(x[n]))*I(ab(x[m]))
    return total


ef = head_error(f)
eg = head_error(g)
af_center = bilinear(a, f, f)
ag_center = bilinear(a, g, g)
af = inflate(af_center, ef)
ag = inflate(ag_center, eg)
print('Complete endpoint and original middle heads enclosed.', flush=True)

# The same assessed recurrence, with shift256 instead of64, narrows Dg.
diagonal = []
for n in range(N):
    y2 = k2[n]/4
    base = I('256.25')
    den = base*base+y2
    value = den.ln()/2-base/(2*den)-pi.ln()
    for j in range(256):
        aj = I(j)+I('.25')
        value -= aj/(aj*aj+y2)
    diagonal.append(inflate(value, I(2).sqrt()/(6*den)))
dg = sum((diagonal[n]*square(g[n]) for n in range(N)), I(0))

prefix = I(0)
response_rows = []
q = 1/fourth
for j in range(32):
    c = I(2*j)+I('.5')
    for p in [0, 1]:
        projection = sum((alpha[n]*c*g[n]/(c*c+k2[n])
                          for n in range(p, N, 2)), I(0))
        term = (1-((-1)**p)*q)*square(projection)
        prefix += term
        response_rows.append(dict(j=j, parity=p, projection=projection.json(),
                                  square_contribution=term.json()))
    q /= 3

seven_centers = [bilinear(t, f, g), bilinear(t, g, h)]
seven_errors = [I('2.1e-7')*l1(f)*l1(g), I('2.1e-7')*l1(g)*l1(h)]
seven = [inflate(x, e) for x, e in zip(seven_centers, seven_errors)]
print('Both actual separation-seven pairings and 64 middle squares enclosed.', flush=True)

# Complete remote prime matrix, using the same shift antiderivatives and
# Taylor sincos as the audited C744w code. Section8 proves 1e-7 per entry.
def rounded(x, absolute):
    value = float(mod.NEAR.divide(mod.NEAR.add(x.lo, x.hi), Decimal(2)))
    error = ab(x-I(Decimal(value)))
    assert error < Decimal(absolute)
    return value, str(error)


ellf, _ = rounded(ell, '1e-16')
pif, _ = rounded(pi, '3e-16')
ns = np.arange(N)
kf = ns*pif/ellf
nuf = np.full(N, np.sqrt(2/ellf)); nuf[0] = 1/np.sqrt(ellf)
etaf = np.where(ns % 2 == 0, 1., -1.)
kn, km = kf[:, None], kf[None, :]
denf = kn*kn-km*km
denf[ns, ns] = 1
signs = np.outer(etaf, etaf)
remote_matrix = np.zeros((N, N))
prime_rows = []
weight_sum = I(0)
max_reduced = 0.
for number in range(2, 4000):
    if not 3**13 < number*number < 3**15:
        continue
    rem = number
    factors = []
    for prime in range(2, math.isqrt(number)+1):
        if rem % prime == 0:
            factors.append(prime)
            while rem % prime == 0:
                rem //= prime
    if rem > 1:
        factors.append(rem)
    if len(factors) != 1:
        continue
    weight = I(factors[0]).ln()/I(number).sqrt()
    delta = I(0) if number == 2187 else 14*ell-I(number).ln()
    assert -ell.lo < delta.lo <= delta.hi < ell.lo
    wf, we = rounded(weight, '1e-16')
    df, de = rounded(delta, '1e-16')
    weight_sum += weight
    if number == 2187:
        remote_matrix += wf*np.eye(N)
    else:
        assert delta.lo > 0 or delta.hi < 0
        arguments = kf*df
        reduced = arguments-np.rint(arguments/(pif/2))*(pif/2)
        max_reduced = max(max_reduced, float(np.max(np.abs(reduced))))
        sn, cs = entries.sincos(arguments, pif)
        if df > 0:
            out = (-signs*kn*sn[:, None]+km*sn[None, :])/denf
        else:
            out = (kn*sn[:, None]-signs*km*sn[None, :])/denf
        diagonal_f = np.empty(N)
        diagonal_f[0] = ellf-abs(df)
        diagonal_f[1:] = ((ellf-abs(df))*cs[1:]/2
                          -np.sign(df)*sn[1:]/(2*kf[1:]))
        out[ns, ns] = diagonal_f
        remote_matrix += wf*out*np.outer(nuf, nuf)
    prime_rows.append(dict(n=number, prime=factors[0], weight=weight.json(),
                           delta=delta.json(), weight_float_error=we,
                           delay_float_error=de))
assert len(prime_rows) == 334 and weight_sum.hi < Decimal(60)
assert max_reduced < .786
remote_center = bilinear(remote_matrix, f, h)
remote_prime_error = I('1e-7')*l1(f)*l1(h)
# Pay the whole continuous operator, not just its truncation.
kappa14 = 1/(I(3**16)*fourth*I('2.5')*(1-I(1)/3**13))
remote_continuous_error = kappa14*(norm2(f)*norm2(h)).sqrt()
remote = inflate(remote_center, remote_prime_error+remote_continuous_error)

endpoint = 2*af-2*remote
middle = dg+prefix-2*sum(seven, I(0))
comparison = endpoint+middle
original = endpoint+ag-2*sum(seven, I(0))
omitted_middle_response = ag-dg-prefix
checks = dict(exact_even_middle=all(g[n].lo == g[n].hi == 0 for n in range(1, N, 2)),
              complete_remote_count=len(prime_rows) == 334,
              zero_delay_present=sum(x['n'] == 2187 for x in prime_rows) == 1,
              all_input_hashes_match=True,
              remote_weight_sum_below60=weight_sum.hi < Decimal(60),
              all_reduced_arguments_below_point786=max_reduced < .786,
              comparison_negative=comparison.hi < Decimal(0),
              original_positive=original.lo > Decimal(0),
              discarded_response_positive=omitted_middle_response.lo > Decimal(0))
failures = [name for name, passed in checks.items() if not passed]
matrix_path = BASE/'response-prefix-remote-546.npz'
np.savez_compressed(matrix_path, remote_prime=remote_matrix)
result = dict(scope='Fixed 32-response middle comparison obstruction only',
    parameters=dict(modes=N, prefix_per_parity=32, diagonal_recurrence_shift=256),
    direction=dict(path=direction_path.name,
                   sha256=hashlib.sha256(direction_path.read_bytes()).hexdigest(), **direction),
    input_hashes=input_hashes, constants=dict(ell=ell.json(), pi=pi.json()),
    coefficients=dict(f=[x.json() for x in f], g=[x.json() for x in g], h=[x.json() for x in h]),
    diagonal_entries=[x.json() for x in diagonal],
    heads=dict(f_center=af_center.json(), f_error=ef.json(), f=af.json(),
               g_center=ag_center.json(), g_error=eg.json(), g=ag.json()),
    retained_middle_response=dict(rows=response_rows, total=prefix.json(), diagonal=dg.json()),
    seven=dict(centers=[x.json() for x in seven_centers],
               errors=[x.json() for x in seven_errors], pairings=[x.json() for x in seven]),
    remote=dict(primes=prime_rows, weight_sum=weight_sum.json(),
        max_reduced_argument=max_reduced, center=remote_center.json(),
        prime_entry_error='1e-7', prime_pairing_error=remote_prime_error.json(),
        entire_continuous_norm_bound=kappa14.json(), continuous_error=remote_continuous_error.json(),
        complete_pairing=remote.json(), matrices=dict(path=matrix_path.name,
        sha256=hashlib.sha256(matrix_path.read_bytes()).hexdigest())),
    summary=dict(endpoint_energy_minus_remote=endpoint.json(),
        middle_comparison_contribution=middle.json(), comparison_value=comparison.json(),
        required_comparison='>=0 on every exact-neutral triple',
        discarded_middle_response=omitted_middle_response.json(),
        original_form_value=original.json(), comparison_rejected=not failures),
    checks=checks, failures=failures,
    limitations=['C744w analytic and IEEE754/Decimal contracts inherited.',
        '512-mode vectors belong to the closed form domain; smooth transfer uses C744z Section1.',
        'Only the fixed prefix32 comparison fails, not every larger prefix.',
        'No negative original triple, infinite residual sign, H2 witness, or RH conclusion.'])
path = BASE/'response-prefix-stop-546.json'
path.write_text(json.dumps(result, indent=2)+'\n')
print('Comparison:', comparison.lo, comparison.hi, 'required >=0')
print('Original triple:', original.lo, original.hi)
print('Checks:', len(checks), 'failures:', failures)
print('Certificate:', path.relative_to(BASE.parent.parent))
assert not failures
