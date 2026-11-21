#!/usr/bin/env python3
"""One joint input-tail enclosure in C999m's fixed geometry.

Reuse audited finite maps/Grams; no FFT, new cutoff or predictor tuning.
An eigenvalue only proposes a factor, whose complete reconstruction is paid.
"""
import hashlib
import importlib.util
import json
import math
from decimal import Context, Decimal, ROUND_CEILING, ROUND_FLOOR, ROUND_HALF_EVEN
from pathlib import Path

import numpy as np

BASE = Path(__file__).resolve().parent
N, J, K, F, E = 512, 32768, 65536, 510, 1020
sp = importlib.util.spec_from_file_location('iv571', BASE/'complete-schur-531.py')
iv = importlib.util.module_from_spec(sp)
sp.loader.exec_module(iv)
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
    h = hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda: f.read(8*1024*1024), b''):
            h.update(block)
    return h.hexdigest()


def read(name):
    pins[name] = sha(BASE/name)
    return json.loads((BASE/name).read_text())


def fro(x):
    return float(np.linalg.norm(x))


def upper(rec, key):
    return I(rec['scalars'][key]['hi'])


def dyadic_upper(interval):
    value = float(np.nextafter(float(interval.hi), np.inf))
    check(Decimal.from_float(value) >= interval.hi, 'directed dyadic coefficient')
    return value


audit = read('signed-mixed-audit-570.json')
check(not audit['failures'] and all(c['passed'] for c in audit['checks']),
      'all conceptual-audit570 checks')
check(sha(BASE/'signed-mixed-audit-570.py') == audit['script_sha256'], 'audit570 source')
for name, digest in audit['input_hashes'].items():
    pins[name] = sha(BASE/name)
    check(pins[name] == digest, 'audited input '+name)
remote = read('signed-mixed-remote-input-tail-566.json')
local = read('signed-mixed-local-trial-input-568.json')
inverse = read('signed-mixed-inverse-input-569.json')
for rec in [remote, local, inverse]:
    check(not rec['failures'] and all(c['passed'] for c in rec['checks']),
          'complete inherited component checks')
    for name, digest in rec['input_hashes'].items():
        pins[name] = sha(BASE/name)
        check(pins[name] == digest, 'component input '+name)
for name, item in inverse['artifacts'].items():
    pins[name] = sha(BASE/name)
    check(pins[name] == item['sha256'], 'complete inverse artifact '+name)

with np.load(BASE/'neutral-head-covariance-559.npz') as a:
    z, y, mc = a['z'], a['predictor_free'], a['comparison_lower']
with np.load(BASE/'signed-mixed-remote-input-tail-566.npz') as a:
    ub = a['boundary_rows']
    check(np.array_equal(mc, a['comparison']), 'same566 comparison')
with np.load(BASE/'signed-mixed-local-trial-input-568.npz') as a:
    lb, gb, g = a['local_boundary_rows'], a['trial_boundary_rows'], a['raw_trial_center']
    check(np.array_equal(mc, a['comparison']), 'same568 comparison')
with np.load(BASE/'signed-mixed-inverse-input-569.npz') as a:
    vb = a['boundary_rows']
    igrams = {s: a[s+'_normalized_gram'] for s in ['low_norm', 'moment1', 'moment2', 'band_norm']}
    check(np.array_equal(mc, a['comparison']), 'same569 comparison')
check(np.array_equal(mc, mc.T) and mc.shape == (E,E), 'complete symmetric M_cert')
check(fro(mc) < 400, 'M_cert Frobenius below400')

# Exact coefficients are upward dyadic endpoints of inherited analytic bounds.
pi = I(local['scalars']['pi']['lo'], local['scalars']['pi']['hi'])
dk, mu, eta = I('10.9963070613268'), I('.000999'), I('1e-7')
sqrt2 = I(2).sqrt()
vp14, vm14 = [I(remote['sine_tails'][s]['complete_weighted_sine_square_upper']['hi']) for s in ['positive','negative']]
vp7, vm7 = [I(local['sine_tails'][s]['complete_sine_square_upper']['hi']) for s in ['positive','negative']]
a14, a7 = upper(remote,'prime_total_weight'), upper(local,'prime_total_weight')
jrem, srem = upper(local,'shift_remainder'), upper(local,'response_remainder')
k7 = upper(local,'complete_continuous_norm')
# This is the complete inherited continuous U norm, not a sampled kernel.
ell = I(local['scalars']['ell']['lo'], local['scalars']['ell']['hi'])
k14 = 1/(I(3**16)*I(3).sqrt().sqrt()*I('2.5')*(1-I(1)/3**13))
theta = 1-I((J-1)**2)/(K*K)
c_intervals = dict(
    local_leading=(1+upper(local,'response_b')/K)/(I(K-1)*dk).sqrt(),
    remote_positive=(2/pi)*(vp14/dk).sqrt(),
    remote_negative=(2/pi)*(vm14/dk).sqrt(),
    endpoint_remainders=(srem+a14*jrem+k14)/dk.sqrt(),
    combined_trial_inverse_boundary=(2/pi)*(vp7.sqrt()+vm7.sqrt())/dk.sqrt(),
    trial_remainder=sqrt2*(a7*jrem+k7)/dk.sqrt(),
    inverse_moment1=(2/pi)*sqrt2*a7*I(J).sqrt()/theta*(J-1)/(I(3*(K-1)**3)*dk).sqrt(),
    inverse_moment2=(2/pi)*sqrt2*a7*I(J).sqrt()/theta*(J-1)**2/(I(5*(K-1)**5)*dk).sqrt(),
    inverse_continuous=sqrt2*k7/dk.sqrt(),
    inverse_band=sqrt2*I('4.71')/dk.sqrt())
c = {key: dyadic_upper(value) for key, value in c_intervals.items()}
ci = {key:I(Decimal.from_float(value)) for key,value in c.items()}

# Fixed Cauchy weights from the previous scalar bounds; no optimization loop.
a_strings = ['12','17','17','32','16','43','.011','.006','.35','.007']
ast = dict(zip(c, a_strings))
S = sum((ci[key]*I(ast[key]) for key in c), I(0))

zb = np.zeros((2*N,E))
zb[:N,:F] = z
zb[N:,F:] = z
combined = gb+vb
maps = dict(local_leading=lb, remote_positive=ub[[0,2]], remote_negative=ub[[1,3]],
            endpoint_remainders=zb, combined_trial_inverse_boundary=combined, trial_remainder=g)
check(fro(z)<23 and fro(y)<11 and fro(g)<11 and fro(combined)<100,
      'complete basis/trial/combined row magnitudes')
check(fro(gb)<100 and fro(vb)<100, 'both full boundary operands below100')
check(all(fro(value)<100 for value in maps.values()), 'all new Gram row maps below100')
scales = {key:'1' for key in c}
scales.update(inverse_moment1='.011',inverse_moment2='.006',inverse_continuous='.35',inverse_band='.007')
grams = {key:value.T@value for key,value in maps.items()}
grams.update(inverse_moment1=igrams['moment1'],inverse_moment2=igrams['moment2'],
             inverse_continuous=igrams['low_norm'],inverse_band=igrams['band_norm'])

# The exact majorant is sum d_i * (C_i/q_i)^*(C_i/q_i).
# Each d_i is >= S*c_i*q_i^2/a_i. Stored inverse Grams use precisely q_i.
weights = {key:dyadic_upper(S*ci[key]*I(scales[key])*I(scales[key])/I(ast[key])) for key in c}
qhat = np.zeros((E,E))
for key, gram in grams.items():
    qhat += weights[key]*gram
qhat = (qhat+qhat.T)/2

# A diagnostic only proposes an upper endpoint. No changes to maps/weights follow.
proposal_root = np.linalg.cholesky(mc)
proposal_left = np.linalg.solve(proposal_root, qhat)
proposal_matrix = np.linalg.solve(proposal_root, proposal_left.T).T
eig = float(np.linalg.eigvalsh((proposal_matrix+proposal_matrix.T)/2)[-1])
q_string = str(Decimal(math.ceil(1000*math.sqrt(max(0.,eig)))+2)/1000)
q = I(q_string)
q2_float = float(Decimal(q_string)*Decimal(q_string))
target = q2_float*mc-qhat-1e-6*np.eye(E)
factor = np.empty((0,0))
reconstruction = None
try:
    factor = np.linalg.cholesky(target)
    residual, f2 = fro(target-factor@factor.T), fro(factor)**2
    reconstruction = dict(residual_fro=residual,factor_squared_fro=f2,
        maximum_entry=max(float(np.max(np.abs(v))) for v in [target,factor,qhat]))
    check(residual<1e-7 and f2<100000 and reconstruction['maximum_entry']<400,
          'entire joint factor reconstruction')
except np.linalg.LinAlgError:
    check(False, 'entire joint factor reconstruction')

u = I(1)/2**53
gamma = lambda n:n*u/(1-n*u)
old_gram_error = gamma(2*K)*10000+I('1e-8')
new_gram_error = gamma(2048)*10000+I('1e-8')
weighted_gram_error = sum((I(Decimal.from_float(weights[key]))*(
    new_gram_error if key in maps else old_gram_error) for key in c),I(0))
weighted_magnitude = sum(weights[key]*fro(gram) for key,gram in grams.items())
check(weighted_magnitude<10000, 'weighted Gram assembly magnitude below10000')
check(all(fro(gram)<10000 for gram in grams.values()), 'all full stored Grams below10000')
# 2e-7 pays weighted scalar assembly, q^2 conversion, symmetrization and norms.
factor_error = I('1e-7')+gamma(2048)*100000+I('2e-7')+weighted_gram_error
check(factor_error.hi<Decimal('1e-6'), 'full joint Gram/factor error below restored margin')

# Exact maps versus the dyadic maps whose full Grams were just enclosed.
eH = upper(inverse,'head_inverse_error')
e0 = upper(inverse,'low_complement_inverse_error')
eB = upper(inverse,'band_inverse_error')
alpha = I(N-1)/(J-1)
eb = I(N).sqrt()*eH+I(J-N).sqrt()*e0+eta
delta = dict(local_leading=eta,remote_positive=sqrt2*eta,remote_negative=sqrt2*eta,
    endpoint_remainders=I('1e-14'),
    combined_trial_inverse_boundary=sqrt2*(eb+eta)+eta,
    trial_remainder=eta,inverse_moment1=alpha*eH+e0+eta,
    inverse_moment2=alpha*alpha*eH+e0+eta,
    inverse_continuous=(eH*eH+e0*e0).sqrt()+eta,inverse_band=eB+eta)
conversion = sum((ci[key]*delta[key] for key in c),I(0))/mu.sqrt()
neutral = upper(remote,'neutral_low_correction')+upper(local,'neutral_low_correction')+upper(inverse,'low_correction')
tail = q+conversion+neutral
rounded_tail = (tail.hi*Decimal(1000)).to_integral_value(rounding=ROUND_CEILING)/Decimal(1000)
finite_threshold = (I('.5')-I('.163')-I('.008'))*(I('.5')-I('.163')-I('.008'))-I(rounded_tail)*I(rounded_tail)
check(tail.hi<Decimal('.25'), 'improves previous complete scalar input allowance .25')

archive = BASE/'signed-mixed-joint-input-571.npz'
np.savez_compressed(archive,comparison=mc,majorant_center=qhat,target=target,factor=factor,
    combined_boundary_rows=combined,**{key+'_gram':value for key,value in grams.items()})
record = dict(parameters=dict(N=N,J=J,K=K,endpoint_dimension=E),
    scope='Complete n>=65536 input tail of B_tilde^(K), fixed562 quarter test',
    certified_under_inherited_contracts=not failures,script_sha256=sha(Path(__file__)),input_hashes=pins,
    coefficient_enclosures={key:value.json() for key,value in c_intervals.items()},
    exact_dyadic_coefficients={key:str(Decimal.from_float(value)) for key,value in c.items()},
    cauchy_weights=ast,cauchy_sum=S.json(),gram_scales=scales,
    exact_dyadic_gram_weights={key:str(Decimal.from_float(value)) for key,value in weights.items()},
    diagnostic_only_largest_generalized_eigenvalue=eig,proposed_center_norm=q_string,
    reconstruction=reconstruction,weighted_gram_magnitude=weighted_magnitude,
    exact_map_errors={key:value.json() for key,value in delta.items()},
    scalars=dict(new_gram_error=new_gram_error.json(),inherited_gram_error=old_gram_error.json(),
        weighted_gram_error=weighted_gram_error.json(),factor_error=factor_error.json(),
        conversion_norm=conversion.json(),neutral_low_correction=neutral.json(),
        complete_input_tail=tail.json(),required_finite_covariance=finite_threshold.json()),
    rounded_input_bound=str(rounded_tail),previous_complete_input_bound='.25',
    full_mixed_required_norm='.5',full_quarter_test_decided=False,checks=checks,failures=failures,
    archive=dict(path=str(archive.relative_to(BASE.parent.parent)),sha256=sha(archive)),
    qualifications=['Audited analytic/whole-core/c_star/IEEE754/Decimal contracts retained',
        'New quantitative specialization not independently audited; no novelty claim',
        'Finite signed covariance and its arithmetic are still unpaid; locator is not a certificate',
        'Predictor and inverse-output allowances remain .008 and .163, paid once',
        'Complement coercivity, C744q, H2, non-neutral coverage and actual-Xi assembly remain open'])
out = BASE/'signed-mixed-joint-input-571.json'
out.write_text(json.dumps(record,indent=2)+'\n')
print('Joint input checks:',len(checks),'failures:',failures)
print('Center norm upper:',q_string,'; exact-map correction:',conversion.hi)
print('Complete input upper:',tail.hi,'; previous .25; rounded:',rounded_tail)
print('Required certified finite covariance <=',finite_threshold.lo,'; remains unpaid')
print('Full mixed required norm <=.5; quarter undecided')
print('Certificate:',out.relative_to(BASE.parent.parent),'arrays:',archive.relative_to(BASE.parent.parent))
assert not failures
