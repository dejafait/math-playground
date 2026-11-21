#!/usr/bin/env python3
"""Certify only the complete inverse-output tail allowance, C999m Section6.

Reuses the audited C999l matrices and C744w tail, under their contracts.
Does not certify the FFT locator, input tail, or quarter budget.
"""
import hashlib
import importlib.util
import json
from decimal import Context, Decimal, ROUND_CEILING, ROUND_FLOOR, ROUND_HALF_EVEN
from pathlib import Path
import numpy as np

BASE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('interval565', BASE/'complete-schur-531.py')
iv = importlib.util.module_from_spec(spec)
spec.loader.exec_module(iv)
iv.DOWN = Context(prec=80, rounding=ROUND_FLOOR)
iv.UP = Context(prec=80, rounding=ROUND_CEILING)
iv.NEAR = Context(prec=80, rounding=ROUND_HALF_EVEN)
I = iv.I
checks, failures = [], []


def check(ok, label):
    checks.append(dict(label=label, passed=bool(ok)))
    if not ok: failures.append(label)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


audit = json.loads((BASE/'neutral-head-covariance-audit-561.json').read_text())
original = json.loads((BASE/'neutral-head-covariance-559.json').read_text())
pins = {name:sha(BASE/name) for name in ['neutral-head-covariance-559.npz',
        'neutral-head-covariance-559.json','neutral-head-covariance-audit-561.json',
        'neutral-head-covariance-audit-561.py','complete-schur-531.py']}
for name in ['neutral-head-covariance-559.npz','neutral-head-covariance-559.json']:
    check(pins[name]==audit['original_hashes'][name], 'audited full input hash '+name)
check(pins['neutral-head-covariance-audit-561.py']==audit['source_script_sha256'],
      'audited source script unchanged')
check(not audit['failures'] and all(c['passed'] for c in audit['checks']),
      'all inherited audit561 checks passed')
check(not original['failures'] and all(c['passed'] for c in original['checks']),
      'all original559 checks passed')
check(original['parameters']==dict(N=512,K=65536,endpoint_dimension=1020,
      middle_dimension=510,d0='6.14',fraction='1/2',penalty=256), 'unchanged reference and family')
check(Decimal(original['finite']['predictor_free_error']['hi'])<Decimal('.000612'),
      'audited exact-predictor free error <.000612')
check(Decimal(original['tail']['diagonal_lower']['lo'])>Decimal('10.9963070613268'),
      'audited complete output lower weight')
with np.load(BASE/'neutral-head-covariance-559.npz') as z:
    m,ct=z['comparison_lower'],z['tail_covariance_upper']
check(m.shape==ct.shape==(1020,1020),'complete matrices')
check(np.array_equal(m,m.T),'exact dyadic comparison symmetry')
# The exact Hermitian part defines the saved tail quadratic form.
# Its floating assembly is included in the2e-7 operand allowance.
ct_center=(ct+ct.T)/2
a=.02*m-ct_center-1e-6*np.eye(1020)
factor=np.linalg.cholesky(a)  # proposal; success alone is not a check
reconstruction=float(np.linalg.norm(a-factor@factor.T))
f2=float(np.sum(factor*factor))
maximum=max(float(np.max(np.abs(q))) for q in [m,ct,a,factor])
check(reconstruction<1e-7,'entire factor reconstruction below1e-7')
check(f2<100000 and maximum<400,'full inherited factor magnitude ledger')
u=I(1)/I(2**53)
gamma=2048*u/(1-2048*u)
factor_error=I('1e-7')+gamma*100000+I('2e-7')
check(factor_error.hi<Decimal('1e-6'),'exact factor error fits positive margin1e-6')

# C999m(7),(10),(11), with the exact-predictor output correction.
dk=I('10.9963070613268')
zeta=(1/I('6.14')+4/(3*I('6.14')*511**3)).sqrt()
predictor_tail=(2/dk).sqrt()*I('.062501906')*I('1.008')*I('.000612')/I('.000999').sqrt()
weighted_tail=I('.02').sqrt()+predictor_tail
allowance=zeta*I(2).sqrt()*I('4.71')*(2/dk).sqrt()*weighted_tail
check(allowance.hi<Decimal('.163'),'complete normalized inverse-output error <.163')
archive=BASE/'signed-mixed-output-tail-565.npz'
np.savez_compressed(archive,comparison=m,tail_covariance=ct,
                    factor_matrix_center=a,factor=factor)
result=dict(scope='Only inverse-output truncation at K65536 in C999m(10)',
            certified_under_inherited_contracts=not failures,
            input_hashes=pins,source_sha256=sha(Path(__file__)),
            factor=dict(target='.02 M_cert-C_tail',subtracted_margin='1e-6',
                        observed_reconstruction_fro=reconstruction,
                        factor_squared_fro=f2,maximum_entry=maximum,
                        exact_reconstruction_allowance=factor_error.json()),
            scalar=dict(zeta_upper=zeta.json(),exact_predictor_weighted_tail=predictor_tail.json(),
                        full_weighted_residual_tail=weighted_tail.json(),
                        normalized_output_error=allowance.json()),
            achieved_upper='.163',quarter_test_requires_total_mixed_norm_at_most='.5',
            checks=checks,failures=failures,
            remaining=['Complete input covariance beyond65535',
                       'Finite signed covariance arithmetic, exact predictor and finite inverse action',
                       'Independent complementary coercivity and global actual-Xi assembly'],
            archive=dict(path=str(archive.relative_to(BASE.parent.parent)),sha256=sha(archive)),
            qualifications=['Inherited analytic response and IEEE754/Decimal contracts',
                            'Whole-neutral-core and unreplayed c_star qualifications',
                            'New allowance has no separate independent conceptual audit'])
path=BASE/'signed-mixed-output-tail-565.json'
path.write_text(json.dumps(result,indent=2)+'\n')
print('Output-tail checks',len(checks),'failures',failures)
print('Actual normalized output error <=',allowance.hi,'; allocated bound .163')
print('Required total mixed norm <=.5; input and finite arithmetic obligations remain')
print('Certificate',path.relative_to(BASE.parent.parent),'factor',archive.relative_to(BASE.parent.parent))
assert not failures
