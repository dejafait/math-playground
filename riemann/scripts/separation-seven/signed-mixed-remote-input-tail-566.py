#!/usr/bin/env python3
"""Complete remote-U component of the fixed K65536 input tail.

Standard geometric-series specialization under assessment562. This is
not a certificate for the full mixed map or its quarter budget.
"""
import hashlib
import importlib.util
import json
import math
from decimal import Context, Decimal, ROUND_CEILING, ROUND_FLOOR, ROUND_HALF_EVEN
from pathlib import Path
import numpy as np

BASE = Path(__file__).resolve().parent
N, K, E = 512, 65536, 1020
spec = importlib.util.spec_from_file_location('interval566', BASE/'complete-schur-531.py')
iv = importlib.util.module_from_spec(spec)
spec.loader.exec_module(iv)
iv.DOWN = Context(prec=80, rounding=ROUND_FLOOR)
iv.UP = Context(prec=80, rounding=ROUND_CEILING)
iv.NEAR = Context(prec=80, rounding=ROUND_HALF_EVEN)
I = iv.I
checks, failures, factors, ledgers = [], [], {}, {}


def check(ok, label):
    checks.append(dict(label=label, passed=bool(ok)))
    if not ok:
        failures.append(label)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def sq(q):
    return q*q


def atan(q):
    x, total = I(1)/q, I(0)
    power = x
    for j in range(80):
        total += ((-1)**j)*power/(2*j+1)
        power *= x*x
    return total+I(power.hi.copy_negate(), power.hi)/161


def positive_difference(q):
    if q.lo > 0:
        return q
    assert q.hi < 0
    return -q


audit = json.loads((BASE/'neutral-head-covariance-audit-561.json').read_text())
remote_audit = json.loads((BASE/'response-prefix-audit-548.json').read_text())
original = json.loads((BASE/'neutral-head-covariance-559.json').read_text())
remote = json.loads((BASE/'response-prefix-stop-546.json').read_text())
pins = {}
for name, expected in [
    ('neutral-head-covariance-559.npz', audit['original_hashes']['neutral-head-covariance-559.npz']),
    ('neutral-head-covariance-559.json', audit['original_hashes']['neutral-head-covariance-559.json']),
    ('response-prefix-stop-546.json', remote_audit['input_hashes']['response-prefix-stop-546.json']),
    ('complete-schur-531.py', audit['original_hashes']['complete-schur-531.py'])]:
    pins[name] = sha(BASE/name)
    check(pins[name] == expected, 'unchanged audited input '+name)
for label, data in [('561', audit), ('559', original)]:
    check(not data['failures'] and all(q['passed'] for q in data['checks']),
          'all complete inherited checks pass '+label)
check(not remote_audit['failures'] and remote_audit['originals_unchanged']
      and all(q['passed'] for q in remote_audit['exact_rational_products']),
      'inherited548 audit passed with unchanged originals')
check(original['parameters']['K'] == K and original['parameters']['N'] == N,
      'unchanged head and input cutoff')

pi, ell = 16*atan(5)-4*atan(239), I(3).ln()/2
enumeration = []
for p in range(2, 4000):
    if any(p % j == 0 for j in range(2, math.isqrt(p)+1)):
        continue
    n = p
    while n*n < 3**15:
        if n*n > 3**13:
            enumeration.append((n,p))
        n *= p
enumeration.sort()
check(enumeration == [(q['n'], q['prime']) for q in remote['remote']['primes']],
      'complete independently enumerated334 prime powers')
check(len(enumeration) == 334 and 4000**2 > 3**15, 'enumeration covers entire range')
groups = {'positive': [], 'negative': []}
prime_records, total_weight = [], I(0)
for n,p in enumeration:
    weight = I(p).ln()/I(n).sqrt()
    total_weight += weight
    if n == 2187:
        check(p == 3, 'only exact zero delay is the identity translation')
        prime_records.append(dict(n=n, prime=p, weight=weight.json(), sign='zero', beta={'lo':'0','hi':'0'}))
        continue
    delta = 14*ell-I(n).ln()
    sign = 'positive' if delta.lo > 0 else 'negative'
    beta = positive_difference(delta)/ell
    assert 0 < beta.lo <= beta.hi < 1
    groups[sign].append((n, weight, beta))
    prime_records.append(dict(n=n, prime=p, weight=weight.json(), sign=sign, beta=beta.json()))

sine_tails, pair_records = {}, {}
for sign, rows in groups.items():
    diagonal, oscillatory = I(0), I(0)
    records = []
    minimum_gap = Decimal(1)
    for j,(n,a,b) in enumerate(rows):
        diagonal += a*a
        for m,c,d in rows[j:]:
            plus = b+d
            gap_plus = min(plus.lo, (2-plus).lo)
            assert gap_plus > 0
            minimum_gap = min(minimum_gap, gap_plus)
            if n == m:
                term = a*a/I(gap_plus)
                gap_minus = None
            else:
                diff = positive_difference(b-d)
                gap_minus = diff.lo
                minimum_gap = min(minimum_gap, gap_minus)
                term = 2*a*c*(1/I(gap_minus)+1/I(gap_plus))
            oscillatory += term
            records.append(dict(n=n,m=m,gap_sum_lower=str(gap_plus),
                gap_difference_lower=None if gap_minus is None else str(gap_minus),
                oscillatory_numerator_upper=str(term.hi)))
    upper = diagonal/(2*(K-1))+oscillatory/(2*K*K)
    sine_tails[sign] = dict(count=len(rows), pair_count=len(records),
        minimum_resonance_distance_lower=str(minimum_gap),
        squared_weight_sum=diagonal.json(), oscillatory_sum=oscillatory.json(),
        complete_weighted_sine_square_upper=upper.json())
    pair_records[sign] = records
    check(minimum_gap > 0, 'all sum/difference resonance gaps paid '+sign)
check(sum(len(v) for v in groups.values()) == 333, 'all nonidentity shifts included')

with np.load(BASE/'neutral-head-covariance-559.npz') as a:
    m = a['comparison_lower']
    boundary = a['boundary_functionals'][:4]
check(m.shape == (E,E) and boundary.shape == (4,E), 'full comparison and four boundary rows')
check(np.array_equal(m,m.T), 'exact dyadic comparison symmetry')
check(float(np.linalg.norm(boundary)) < 100, 'boundary conversion magnitude ledger')
u = I(1)/2**53
gamma = 2048*u/(1-2048*u)
factor_error = I('1e-7')+gamma*100000+I('2e-7')
check(factor_error.hi < Decimal('1e-6'), 'full factor error fits restored margin')
for j,row in enumerate(boundary):
    target = m-np.outer(row,row)/144-1e-6*np.eye(E)
    factor = np.linalg.cholesky(target)
    residual = float(np.linalg.norm(target-factor@factor.T))
    f2 = float(np.sum(factor*factor))
    maximum = max(float(np.max(np.abs(q))) for q in [target,factor,m])
    check(residual < 1e-7 and f2 < 100000 and maximum < 400,
          'complete normalized boundary factor '+str(j))
    factors['boundary_factor_'+str(j)] = factor
    ledgers['boundary_'+str(j)] = dict(observed_residual_fro=residual,
        squared_factor_fro=f2,maximum_entry=maximum,dyadic_boundary_norm_upper='12',
        exact_factor_error=factor_error.json())

# C999l's full basis conversion and the <=512-term boundary sums:
# exact boundary row differs from the saved dyadic row by <1e-7.
# Divide by sqrt(.000999), then add to the verified dyadic norm12.
boundary_exact = I(12)+I('1e-7')/I('.000999').sqrt()
sp = I(sine_tails['positive']['complete_weighted_sine_square_upper']['hi'])
sm = I(sine_tails['negative']['complete_weighted_sine_square_upper']['hi'])
leading = (2/pi)*I(2).sqrt()*boundary_exact*(sp.sqrt()+sm.sqrt())
m2 = I(sum(j*j for j in range(1,N))).sqrt()
m4 = I(sum(j**4 for j in range(1,N))).sqrt()
jrem = (2/pi)/(1-I((N-1)**2)/(K*K))*(
    m4/(I(5).sqrt()*I(K-1)*I(K-1)*I(K-1).sqrt())
    +m2/(I(3).sqrt()*I(K-1)*I(K-1).sqrt()))
head = I('1.008')/I('.000999').sqrt()
remainder = total_weight*jrem*head
kappa14 = 1/(I(3**16)*I(3).sqrt().sqrt()*I('2.5')*(1-I(1)/3**13))
continuous = kappa14*head
dk = I('10.9963070613268')
neutral_low = (4/(3*dk*(K-1)**3)).sqrt()*I('29.813203120')*head
allowance = (leading+remainder+continuous)/dk.sqrt()+neutral_low
check(allowance.hi < Decimal('.12'), 'entire remote-U input tail norm below.12')

# Check the complete prior output factor rather than trusting a preview.
outrec = json.loads((BASE/'signed-mixed-output-tail-565.json').read_text())
check(not outrec['failures'] and all(q['passed'] for q in outrec['checks']),
      'all14 output565 checks retained')
for name, expected in outrec['input_hashes'].items():
    check(sha(BASE/name) == expected, 'output565 input pin '+name)
check(sha(BASE/'signed-mixed-output-tail-565.py') == outrec['source_sha256'], 'output565 source pin')
check(sha(BASE/'signed-mixed-output-tail-565.npz') == outrec['archive']['sha256'], 'output565 archive pin')
with np.load(BASE/'signed-mixed-output-tail-565.npz') as a:
    check(np.array_equal(a['comparison'],m), 'output565 uses identical M_cert')
    ct = (a['tail_covariance']+a['tail_covariance'].T)/2
    outtarget = .02*m-ct-1e-6*np.eye(E)
    outf = a['factor']
    outres = float(np.linalg.norm(outtarget-outf@outf.T))
    check(outres < 1e-7 and float(np.sum(outf*outf)) < 100000
          and float(np.max(np.abs(outtarget))) < 400, 'full output565 factor replay')
zeta = (1/I('6.14')+4/(3*I('6.14')*511**3)).sqrt()
pred = (2/dk).sqrt()*I('.062501906')*I('1.008')*I('.000612')/I('.000999').sqrt()
output_error = zeta*I(2).sqrt()*I('4.71')*(2/dk).sqrt()*(I('.02').sqrt()+pred)
check(output_error.hi < Decimal('.163'), 'directed output allowance replay below.163')

archive = BASE/'signed-mixed-remote-input-tail-566.npz'
np.savez_compressed(archive,comparison=m,boundary_rows=boundary,**factors)
record = dict(scope='Only the full-U component of input modes n>=65536 in C999m; both orientations and exact low-mode corrections',
    certified_under_inherited_contracts=not failures, parameters=dict(N=N,K=K),
    source_sha256=sha(Path(__file__)),input_hashes=pins,
    primes=prime_records,sine_tails=sine_tails,all_pair_resonance_bounds=pair_records,
    boundary_factors=ledgers, scalars=dict(pi=pi.json(),ell=ell.json(),
        exact_boundary_norm=boundary_exact.json(),prime_total_weight=total_weight.json(),
        normalized_unweighted_leading=leading.json(),single_shift_remainder=jrem.json(),
        normalized_unweighted_remainder=remainder.json(),continuous=continuous.json(),
        neutral_low_correction=neutral_low.json(),normalized_remote_input_tail=allowance.json()),
    output565_recheck=dict(factor_residual=outres,normalized_output_error=output_error.json()),
    achieved_component_upper='.12', required_total_mixed_norm_upper='.5',
    full_quarter_test_decided=False,checks=checks,failures=failures,
    remaining=['Input tails of L endpoint terms and both T/inverse-action terms, with cross products',
               'Certified complete finite signed map, predictor and solve arithmetic',
               'Independent complementary coercivity and all global qualifications'],
    archive=dict(path=str(archive.relative_to(BASE.parent.parent)),sha256=sha(archive)))
path = BASE/'signed-mixed-remote-input-tail-566.json'
path.write_text(json.dumps(record,indent=2)+'\n')
print('Remote input-tail checks:',len(checks),'failures:',failures)
print('Actual normalized remote input-tail upper:',allowance.hi,'; recorded bound .12')
print('Required TOTAL mixed norm <=.5; this component alone does not decide the quarter budget')
print('Certificate:',path.relative_to(BASE.parent.parent),'factors:',archive.relative_to(BASE.parent.parent))
assert not failures
