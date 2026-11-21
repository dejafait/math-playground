#!/usr/bin/env python3
"""Pay the exact Galerkin predictor error in assessment562's mixed map.

The predictor/reference/quarter test are unchanged. This certificate
bounds an approximation error, not the full signed covariance.
See C999m Section8 for domains, the cancellation identity and ledgers.
"""
import hashlib
import importlib.util
import json
from decimal import Context, Decimal, ROUND_CEILING, ROUND_FLOOR, ROUND_HALF_EVEN
from pathlib import Path

import numpy as np

BASE = Path(__file__).resolve().parent
N, K, F = 512, 65536, 510
spec = importlib.util.spec_from_file_location('interval567', BASE/'complete-schur-531.py')
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


audit = json.loads((BASE/'neutral-head-covariance-audit-561.json').read_text())
head_record = json.loads((BASE/'neutral-head-covariance-559.json').read_text())
fixed_audit = json.loads((BASE/'fixed-block-metric-audit-557.json').read_text())
for name in ['neutral-head-covariance-559.npz', 'neutral-head-covariance-559.json',
             'complete-covariance-532.npz', 'complete-schur-531.py',
             'fixed-block-metric-audit-557.json']:
    pins[name] = sha(BASE/name)
    check(pins[name] == audit['original_hashes'][name], 'unchanged audited input '+name)
for label, data in [('559', head_record), ('561', audit), ('557', fixed_audit)]:
    check(not data['failures'] and all(c['passed'] for c in data['checks']),
          'complete inherited check list '+label)
check(head_record['parameters']['N'] == N and head_record['parameters']['K'] == K,
      'fixed head and cutoff unchanged')
check(Decimal(head_record['finite']['predictor_free_error']['hi']) < Decimal('.000612'),
      'audited exact free predictor error below .000612')
check(Decimal(head_record['neutral_basis_conversion_L1']['hi']) < Decimal('1e-14'),
      'audited exact neutral basis conversion below 1e-14')

with np.load(BASE/'complete-covariance-532.npz') as a:
    m0, covariance = a['m0'], a['cov00']
with np.load(BASE/'neutral-head-covariance-559.npz') as a:
    z = a['z']
check(m0.shape == (N,N) and covariance.shape == (N,N) and z.shape == (N,F),
      'all complete finite arrays have the specified dimensions')
check(np.array_equal(covariance, covariance.T), 'exact saved covariance symmetry')

# The exact reference is rational/dyadic; this is only its floating center.
h = m0-.00024*np.eye(N)-(100/307)*(covariance+.0046*np.eye(N))
rhs = (h-m0)@z
defect = np.linalg.solve(h, rhs)  # proposal; full equation check below
solve_residual = float(np.linalg.norm(rhs-h@defect))
defect_fro = float(np.linalg.norm(defect))
magnitudes = dict(reference_fro=float(np.linalg.norm(h)),
                  reference_difference_fro=float(np.linalg.norm(h-m0)),
                  basis_fro=float(np.linalg.norm(z)),
                  proposed_defect_fro=defect_fro,
                  maximum_entry=max(float(np.max(np.abs(q))) for q in [h,m0,z,defect]))
check(magnitudes['reference_fro'] < 400 and magnitudes['reference_difference_fro'] < 1
      and magnitudes['basis_fro'] < 23 and magnitudes['maximum_entry'] < 400,
      'full head solve magnitude ledger')
check(solve_residual < 1e-9, 'full proposed head-defect equation residual below 1e-9')
check(defect_fro < .01732, 'full proposed head-defect Frobenius norm below .01732')

# A checked factor supplies an operator-order upper bound, not a numerical eigenvalue.
target = .172*np.eye(N)-covariance-1e-6*np.eye(N)
factor = np.linalg.cholesky(target)
factor_residual = float(np.linalg.norm(target-factor@factor.T))
factor_squared_fro = float(np.sum(factor*factor))
factor_maximum = max(float(np.max(np.abs(q))) for q in [target,factor,covariance])
check(factor_residual < 1e-7 and factor_squared_fro < 100000 and factor_maximum < 400,
      'complete covariance upper-factor reconstruction and magnitude ledger')

u = I(1)/2**53
gamma = 2048*u/(1-2048*u)
factor_error = I('1e-7')+gamma*100000+I('2e-7')
check(factor_error.hi < Decimal('1e-6'), 'restored factor margin pays all reconstruction errors')

# Product/assembly/norm errors for (Hhat-Mhat)Zhat-Hhat Ehat, in Frobenius norm.
# C999l's inherited ledger gives H-Hhat <1e-8; the displayed checks and
# gamma bound independently make this equation's elementary allowance <1e-7.
solve_roundoff = gamma*(I(1)*23+I(400)*I('.0174'))+I('1e-8')
check(solve_roundoff.hi+Decimal('1e-9') < Decimal('1e-7'),
      'head-defect equation arithmetic fits 1e-7')
check(Decimal(str(defect_fro))+Decimal('1e-7') < Decimal('.0174'),
      'norm evaluation allowance proves exact dyadic Frobenius bound .0174')

z_bound, mu, floor = I('1.008'), I('.000999'), I('.239999')
head_defect_error = ((I('1e-8')+I('.00024'))*z_bound
                    +I('1e-14')+I('1e-7')+I('1e-8')*I('.0174'))/floor
head_defect = I('.0174')+head_defect_error
check(head_defect.hi < Decimal('.019'), 'exact head defect below .019')

# Complete Q covariance and every output n>=512 are covered by C999k(3).
tail_defect = (2/I('6.14'))*z_bound*(I('.172')+I('.0046')).sqrt()
whole_defect = (head_defect*head_defect+tail_defect*tail_defect).sqrt()
zeta = (1/I('6.14')+4/(3*I('6.14')*511**3)).sqrt()
predictor_error = zeta*I(2).sqrt()*I('4.71')*whole_defect*I('.000612')/mu.sqrt()
check(predictor_error.hi < Decimal('.008'), 'complete mixed-map predictor error below .008')
check(predictor_error.hi < Decimal('.01'), 'intermediate useful-error threshold .01 met')

archive = BASE/'signed-mixed-predictor-error-567.npz'
np.savez_compressed(archive, reference_center=h, head_form_center=m0, neutral_basis=z,
                    proposed_head_defect=defect, covariance_center=covariance,
                    covariance_upper_factor=factor)
record = dict(scope='Exact Y versus dyadic Yhat with the SAME exact neutral Z; all input n>=512; complete and K-output-truncated mixed maps',
    certified_under_inherited_contracts=not failures,
    parameters=dict(N=N,K=K,reference_d0='6.14',fraction='1/2',penalty=256),
    input_hashes=pins, inherited_audit_sha256=sha(BASE/'neutral-head-covariance-audit-561.json'),
    head_solve=dict(observed_residual_fro=solve_residual, magnitudes=magnitudes,
                    exact_equation_error_upper='1e-7', arithmetic_allowance=solve_roundoff.json(),
                    exact_dyadic_defect_fro_upper='.0174'),
    covariance_upper=dict(bound='.172', observed_reconstruction_fro=factor_residual,
        factor_squared_fro=factor_squared_fro, maximum_entry=factor_maximum,
        exact_reconstruction_error=factor_error.json(), restored_margin='1e-6'),
    bounds=dict(exact_head_defect_error=head_defect_error.json(), exact_head_defect=head_defect.json(),
        full_complement_defect=tail_defect.json(), full_defect=whole_defect.json(),
        neutral_coordinate_norm=zeta.json(), exact_predictor_error= '0.000612',
        normalized_mixed_predictor_error=predictor_error.json(), reported_upper='.008',
        intermediate_required_upper='.01', full_mixed_required_upper='.5'),
    checks=checks, failures=failures, full_quarter_test_decided=False,
    qualifications=['Exact predictor retained; Yhat is only a numerical proxy',
        'No error contract for the saved FFT locator is supplied',
        'Complete remaining input tail and finite signed arithmetic remain unpaid',
        'New specialization unaudited; retain whole-core, c_* and IEEE754/Decimal qualifications',
        'No complementary coercivity or RH conclusion'],
    archive=str(archive.relative_to(BASE.parent.parent)), archive_sha256=sha(archive),
    script_sha256=sha(Path(__file__)))
path = BASE/'signed-mixed-predictor-error-567.json'
path.write_text(json.dumps(record,indent=2)+'\n')
print('Predictor-error checks:',len(checks),'failures:',failures)
print('Complete normalized predictor error upper:',predictor_error.hi)
print('Required for this intermediate estimate: <.01; reported <.008; full map requires <=.5, undecided')
print('Certificate:',path.relative_to(BASE.parent.parent))
print('Complete factors:',archive.relative_to(BASE.parent.parent))
assert not failures
