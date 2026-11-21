#!/usr/bin/env python3
"""Complete local/direct-trial input-tail component of the fixed562 test.

Exact neutral Z and fixed dyadic Yhat, both complex endpoint orientations.
No FFT, inverse-input certificate, quarter decision or complementary sign.
See C999m Section9 for the proof and inherited arithmetic qualifications.
"""
import hashlib
import importlib.util
import json
import math
from decimal import Context, Decimal, ROUND_CEILING, ROUND_FLOOR, ROUND_HALF_EVEN
from pathlib import Path

import numpy as np

BASE = Path(__file__).resolve().parent
N, K, F, E = 512, 65536, 510, 1020
spec = importlib.util.spec_from_file_location('interval568', BASE/'complete-schur-531.py')
iv = importlib.util.module_from_spec(spec)
spec.loader.exec_module(iv)
iv.DOWN = Context(prec=80, rounding=ROUND_FLOOR)
iv.UP = Context(prec=80, rounding=ROUND_CEILING)
iv.NEAR = Context(prec=80, rounding=ROUND_HALF_EVEN)
I = iv.I
checks, failures, pins = [], [], {}


def check(ok, label):
    checks.append(dict(label=label, passed=bool(ok)))
    if not ok:
        failures.append(label)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def atan(q):
    x, total = I(1)/q, I(0)
    power = x
    for j in range(80):
        total += ((-1)**j)*power/(2*j+1)
        power *= x*x
    return total+I(power.hi.copy_negate(), power.hi)/161


def abs_interval(x):
    if x.lo > 0:
        return x
    assert x.hi < 0
    return -x


audit = json.loads((BASE/'neutral-head-covariance-audit-561.json').read_text())
head = json.loads((BASE/'neutral-head-covariance-559.json').read_text())
for name in ['neutral-head-covariance-559.npz', 'neutral-head-covariance-559.json',
             'complete-schur-531.py']:
    pins[name] = sha(BASE/name)
    check(pins[name] == audit['original_hashes'][name], 'unchanged audited input '+name)
pins['neutral-head-covariance-audit-561.json'] = sha(BASE/'neutral-head-covariance-audit-561.json')
for label, data in [('559', head), ('561', audit)]:
    check(not data['failures'] and all(c['passed'] for c in data['checks']),
          'complete inherited check list '+label)
check(sha(BASE/'neutral-head-covariance-audit-561.py') == audit['source_script_sha256'],
      'inherited audit source unchanged')
check(head['parameters'] == dict(N=N,K=K,endpoint_dimension=E,middle_dimension=F,
                               d0='6.14',fraction='1/2',penalty=256),
      'fixed target parameters unchanged')
check(Decimal(head['neutral_basis_conversion_L1']['hi']) < Decimal('1e-14'),
      'inherited exact neutral basis error below 1e-14')

with np.load(BASE/'neutral-head-covariance-559.npz') as a:
    z, y, m = a['z'], a['predictor_free'], a['comparison_lower']
check(z.shape == (N,F) and y.shape == (F,E) and m.shape == (E,E),
      'complete head arrays have the required dimensions')
check(np.array_equal(m,m.T), 'exact dyadic comparison symmetry')
d = np.ones(N); d[0] = 1/np.sqrt(2)
even = d*(np.arange(N) % 2 == 0)
odd = d*(np.arange(N) % 2 == 1)
local = np.zeros((4,E))
local[:2,:F] = np.vstack((np.sqrt(2)*(even@z), odd@z))
local[2:,F:] = local[:2,:F]
g_center = z@y
trial = np.vstack((d@g_center,(d*((-1.)**np.arange(N)))@g_center))

magnitudes = dict(basis_fro=float(np.linalg.norm(z)),
    free_predictor_fro=float(np.linalg.norm(y)), raw_trial_fro=float(np.linalg.norm(g_center)),
    local_rows_fro=float(np.linalg.norm(local)), trial_rows_fro=float(np.linalg.norm(trial)),
    comparison_fro=float(np.linalg.norm(m)))
check(magnitudes['basis_fro'] < 23 and magnitudes['free_predictor_fro'] < 11
      and magnitudes['raw_trial_fro'] < 11 and magnitudes['local_rows_fro'] < 100
      and magnitudes['trial_rows_fro'] < 100 and magnitudes['comparison_fro'] < 400,
      'complete boundary arithmetic magnitude ledger')

u = I(1)/2**53
gamma = 2048*u/(1-2048*u)
factor_error = I('1e-7')+gamma*100000+I('2e-7')
check(factor_error.hi < Decimal('1e-6'), 'factor ledger fits restored positive margin')
# The following deliberately enlarged bound covers raw-trial product,
# all row products/sqrt conversions, and exact-Z conversion in Frobenius norm.
row_arithmetic = gamma*(I(23)*11*23+I(100)*23+I(100)) + I('1e-8')
check(row_arithmetic.hi < Decimal('1e-7'), 'all exact boundary row conversions fit 1e-7')

factors, factor_ledgers = {}, {}
for name, rows, bound in [('local',local,12), ('trial_plus',trial[:1],6),
                         ('trial_minus',trial[1:],6)]:
    gram = rows.T@rows
    target = m-gram/(bound*bound)-1e-6*np.eye(E)
    factor = np.linalg.cholesky(target)  # proposal; checked in full
    residual = float(np.linalg.norm(target-factor@factor.T))
    f2 = float(np.sum(factor*factor))
    maximum = max(float(np.max(np.abs(q))) for q in [rows,gram,target,factor,m])
    # gram may exceed400; its bound here is10000 and assembly division is paid.
    check(residual < 1e-7 and f2 < 100000 and maximum < 10000
          and float(np.max(np.abs(target))) < 400 and float(np.max(np.abs(factor))) < 400,
          'full boundary factor reconstruction '+name)
    factors[name+'_factor'] = factor
    factor_ledgers[name] = dict(proposed_norm_bound=bound, observed_residual_fro=residual,
        squared_factor_fro=f2, maximum_intermediate_entry=maximum,
        exact_reconstruction_error=factor_error.json(), restored_margin='1e-6')

pi, ell = 16*atan(5)-4*atan(239), I(3).ln()/2
enumeration = []
for p in range(2,82):
    if any(p % j == 0 for j in range(2,math.isqrt(p)+1)):
        continue
    q = p
    while q < 81:
        if q > 27:
            enumeration.append((q,p))
        q *= p
enumeration.sort()
check(enumeration == iv.prime_powers() and len(enumeration) == 16,
      'all sixteen active separation7 prime powers independently enumerated')
groups = {'positive': [], 'negative': []}
prime_records, total_weight = [], I(0)
for q,p in enumeration:
    delta, weight = 7*ell-I(q).ln(), I(p).ln()/I(q).sqrt()
    sign = 'positive' if delta.lo > 0 else 'negative'
    beta = abs_interval(delta)/ell
    check(0 < beta.lo <= beta.hi < 1, 'nonzero delay strictly inside cell '+str(q))
    groups[sign].append((q,weight,beta))
    total_weight += weight
    prime_records.append(dict(q=q,prime=p,weight=weight.json(),sign=sign,beta=beta.json()))

sine_tails, pair_records = {}, {}
for sign, rows in groups.items():
    diagonal, oscillatory = I(0), I(0)
    records, minimum_gap = [], Decimal(1)
    for j,(q,a,b) in enumerate(rows):
        diagonal += a*a
        for t,c,dv in rows[j:]:
            plus = b+dv
            gap_plus = min(plus.lo,(2-plus).lo)
            assert gap_plus > 0
            minimum_gap = min(minimum_gap,gap_plus)
            if q == t:
                gap_minus = None
                term = a*a/I(gap_plus)
            else:
                gap_minus = abs_interval(b-dv).lo
                minimum_gap = min(minimum_gap,gap_minus)
                term = 2*a*c*(1/I(gap_minus)+1/I(gap_plus))
            oscillatory += term
            records.append(dict(q=q,t=t,gap_sum_lower=str(gap_plus),
                gap_difference_lower=None if gap_minus is None else str(gap_minus),
                oscillatory_numerator_upper=str(term.hi)))
    upper = diagonal/(2*(K-1))+oscillatory/(2*K*K)
    sine_tails[sign] = dict(count=len(rows),pair_count=len(records),
        minimum_resonance_distance_lower=str(minimum_gap),
        squared_weight_sum=diagonal.json(),oscillatory_numerator=oscillatory.json(),
        complete_sine_square_upper=upper.json())
    pair_records[sign] = records
    check(minimum_gap > 0, 'complete resonance denominators paid '+sign)

mu, dk, zn, yn = I('.000999'), I('10.9963070613268'), I('1.008'), I('1.320001')
q_local, q_trial = 12+I('1e-7')/mu.sqrt(), 6+I('1e-7')/mu.sqrt()
b_response = 4*ell*(1+I('1.5')/I(3).sqrt().sqrt())/(pi*pi)
sumsq = I(0)
for j in range(N):
    vj = 4*j+16*ell/(pi*pi)
    sumsq += vj*vj
srem = sumsq.sqrt()/(I(3).sqrt()*I(K-1)*I(K-1).sqrt())
jrem = (2/pi)/(1-I((N-1)**2)/(K*K))*(
    I(sum(j**4 for j in range(1,N))).sqrt()/(I(5).sqrt()*I(K-1)*I(K-1)*I(K-1).sqrt())
    + I(sum(j*j for j in range(1,N))).sqrt()/(I(3).sqrt()*I(K-1)*I(K-1).sqrt()))
kappa = 1/(I(2187)*I(3).sqrt()*I('2.5')*(1-I(1)/729))
local_leading = (1+b_response/K)*q_local/I(K-1).sqrt()
local_remainder = srem*zn/mu.sqrt()
vp = I(sine_tails['positive']['complete_sine_square_upper']['hi'])
vm = I(sine_tails['negative']['complete_sine_square_upper']['hi'])
trial_leading = (2/pi)*I(2).sqrt()*q_trial*(vp.sqrt()+vm.sqrt())
trial_prime_remainder = I(2).sqrt()*total_weight*jrem*zn*yn/mu.sqrt()
trial_continuous = I(2).sqrt()*kappa*zn*yn/mu.sqrt()
raw = local_leading+local_remainder+trial_leading+trial_prime_remainder+trial_continuous
# P_low LZ is controlled by the audited full finite PLZ bound6.191.
low_map = (I('6.191')+I(2).sqrt()*I('4.71')*zn*yn)/mu.sqrt()
neutral_low = (4/(3*dk*(K-1)**3)).sqrt()*low_map
allowance = raw/dk.sqrt()+neutral_low
check(allowance.hi < Decimal('.06'), 'complete local/direct-trial input component below .06')

archive = BASE/'signed-mixed-local-trial-input-568.npz'
np.savez_compressed(archive,comparison=m,local_boundary_rows=local,
                    trial_boundary_rows=trial,raw_trial_center=g_center,**factors)
record = dict(scope='A_LT=(Lf_H-T*ZYhat x,Lh_H-TZYhat x); all free input n>=65536; exact Z and same Yhat',
    certified_under_inherited_contracts=not failures,
    parameters=dict(N=N,K=K,reference_d0='6.14',fraction='1/2',penalty=256),
    input_hashes=pins,script_sha256=sha(Path(__file__)),
    finite=dict(magnitudes=magnitudes,row_conversion_allowance=row_arithmetic.json(),
        exact_row_error_upper='1e-7',factor_ledgers=factor_ledgers),
    primes=prime_records,sine_tails=sine_tails,all_pair_resonance_bounds=pair_records,
    scalars=dict(pi=pi.json(),ell=ell.json(),local_boundary_norm=q_local.json(),
        trial_boundary_norm=q_trial.json(),prime_total_weight=total_weight.json(),
        response_b=b_response.json(),response_remainder=srem.json(),shift_remainder=jrem.json(),
        complete_continuous_norm=kappa.json(),normalized_raw_local_leading=local_leading.json(),
        normalized_raw_local_remainder=local_remainder.json(),normalized_raw_trial_leading=trial_leading.json(),
        normalized_raw_trial_prime_remainder=trial_prime_remainder.json(),
        normalized_raw_trial_continuous=trial_continuous.json(),normalized_raw_total=raw.json(),
        normalized_low_output=low_map.json(),neutral_low_correction=neutral_low.json(),
        normalized_local_trial_input_tail=allowance.json()),
    component_required_upper='.06',full_mixed_required_upper='.5',
    full_quarter_test_decided=False,checks=checks,failures=failures,
    qualifications=['Proxy only: exact predictor change is paid once in full map by C999m Section8',
        'Inverse-action input component and all cross products remain obligations',
        'Finite signed entry/basis/head-solve/FFT arithmetic remains unpaid',
        'Unaudited specialization; inherited analytic, whole-core, c_star and IEEE754/Decimal contracts',
        'No complementary coercivity or RH conclusion'],
    archive=dict(path=str(archive.relative_to(BASE.parent.parent)),sha256=sha(archive)))
path = BASE/'signed-mixed-local-trial-input-568.json'
path.write_text(json.dumps(record,indent=2)+'\n')
print('Local/direct-trial input checks:',len(checks),'failures:',failures)
print('Actual normalized component upper:',allowance.hi,'; component threshold <.06')
print('Full mixed-map norm requires <=.5; inverse-input and finite arithmetic unpaid; quarter undecided')
print('Certificate:',path.relative_to(BASE.parent.parent),'factors:',archive.relative_to(BASE.parent.parent))
assert not failures
