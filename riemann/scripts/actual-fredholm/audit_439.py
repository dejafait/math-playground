"""Bounded replay of the repaired certificate after conceptual review.

Preserves all old evidence. Full fields go to audit-439; stdout is short.
This is reviewed-code replay plus exact-rational checks, not a second
implementation of the transcendental backend or formal verification.
"""
import contextlib
import hashlib
import io
import json
import platform
from fractions import Fraction as F
from pathlib import Path

import signed_pair_435 as m
import independent_phase_437 as repair

BASE = Path(__file__).resolve().parent
OUT = BASE / 'audit-439'
OUT.mkdir(exist_ok=True)
REPORT = OUT / 'audit-report.json'
assert not REPORT.exists(), 'Preserve an existing audit; no automatic repeat'
ORIGINAL = BASE / 'independent-phase-certificate-437.json'
OLD = BASE / 'signed-pair-certificate-435.json'
CHECKER = BASE / 'check_independent_phase_437.py'
old = json.loads(ORIGINAL.read_text())
report = dict(status='UNFINISHED', failures=[], checks=[],
              runtime=dict(python=platform.python_version(),
                           decimal=m.decimal.__version__,
                           libmpdec=m.decimal.__libmpdec_version__),
              input_sha256=hashlib.sha256(ORIGINAL.read_bytes()).hexdigest(),
              inherited_input_sha256=hashlib.sha256(OLD.read_bytes()).hexdigest(),
              required_det_lower='0', required_norm_lower='1',
              scope='Same-settings full replay and complete finite rational checks; analytic audit in L779; documented backend contracts remain trusted.')
report['source_sha256'] = {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                           for p in [BASE/'signed_pair_435.py',
                                     BASE/'independent_phase_437.py', CHECKER]}


def save():
    REPORT.write_text(json.dumps(report, indent=2)+'\n')


def compare(name, fresh):
    assert fresh == old[name], 'Complete field mismatch: '+name
    report['checks'].append('Exact equality of every field: '+name)
    save()


def pair(x):
    lo, hi = map(F, x)
    assert lo <= hi
    return lo, hi


def upper_square(box):
    return max(map(abs, pair(box)))**2


def exp_upper(x, terms=256):
    # Exact series sum through terms; subsequent ratios <=x/(terms+2).
    assert 0 <= x < terms+2
    term = total = F(1)
    for k in range(1, terms+1):
        term *= x/k
        total += term
    return total + term*x/(terms+1)/(1-x/(terms+2))


try:
    save()
    fresh = {k: old[k] for k in old if k not in
             ['evaluation', 'inner_contour', 'outer_contour', 'zeros', 'signed']}
    coeff, eg, fresh['evaluation'] = m.build()
    compare('evaluation', fresh['evaluation'])
    for key, radius in [('inner_contour',2048), ('outer_contour',2304)]:
        fresh[key] = m.contour(coeff, eg, radius)
        compare(key, fresh[key])
    alpha, residues, fresh['zeros'] = m.roots_and_residues(coeff, eg)
    compare('zeros', fresh['zeros'])
    repair.SAVED = json.loads(OLD.read_text())['signed']
    fresh['signed'] = repair.fourier(coeff, eg, alpha, residues,
                                     fresh['outer_contour'])
    compare('signed', fresh['signed'])
    (OUT / ORIGINAL.name).write_text(json.dumps(fresh,indent=2)+'\n')
    # Unchanged checker runs against fresh output and an exact inherited copy.
    (OUT / OLD.name).write_bytes(OLD.read_bytes())
    with (OUT/'finite-check-output.txt').open('w') as log:
        with contextlib.redirect_stdout(log):
            exec(compile(CHECKER.read_text(), str(CHECKER), 'exec'),
                 {'__file__':str(OUT/CHECKER.name),'__name__':'__main__'})
    finite = json.loads((OUT/'independent-phase-check-437.json').read_text())
    assert finite['status']=='PASS' and not finite['failures']
    report['checks'].append('Unchanged exact-integer/rational checker passes every fresh finite, DFT, alias and HS/trace record')

    # Exact rational domain checks, including all rectangular evaluation inputs.
    largest_delta_sq = F(0)
    for key in ['inner_contour','outer_contour']:
        assert fresh[key]['radius_w']+1024 < 4096
        assert len(fresh[key]['segments']) == 1024
        for rec in fresh[key]['segments']:
            for box in [rec['center_w'], rec['w_box']]:
                assert sum(upper_square(v) for v in box) < 4096**2
            delta_sq = F(0)
            for box, center in zip(rec['w_box'],rec['center_w']):
                lo,hi = pair(box); cl,ch = pair(center)
                delta_sq += max(abs(lo-ch),abs(hi-cl))**2
            assert delta_sq < 1024**2
            largest_delta_sq = max(largest_delta_sq,delta_sq)
    for root in fresh['zeros']:
        assert max(map(abs,pair(root['root_w'])))+100 < 4096
    n = fresh['signed']
    for sample in n['samples']:
        assert sum(upper_square(v) for v in sample['z'])*2048**2 < 4096**2
    # A concise rational bound for the full collection, not a preview.
    delta_upper = largest_delta_sq.numerator//largest_delta_sq.denominator+1
    report['contour_delta_squared_upper'] = str(delta_upper)
    report['required_contour_delta_squared_upper'] = str(1024**2)
    report['checks'].append(f'All 2048 contour box/Taylor domains, both root derivative disks and all 2048 sample boxes lie in the enlarged evaluator domain; delta^2<{delta_upper}<1024^2')

    # Independent rational upper bound on the load-bearing exp transfer.
    E = pair(n['trace_norm_error'])[1]
    hat_trace = pair(n['finite']['finite_trace_norm'])[1]
    needed_exp = exp_upper(1+hat_trace+E)
    det_error = pair(n['determinant_perturbation_error'])[1]
    assert det_error >= E*needed_exp
    assert pair(n['actual_trace_norm_upper'])[1] >= hat_trace+E
    assert E < F('3.609621e-11')
    assert det_error < F('4.823978e-10')
    assert pair(n['signed_determinant'])[0] > 0
    assert pair(n['original_norm'])[0] >= 1
    report['checks'].append('Exact-rational 256-term exp-series majorant verifies the complete Bornemann determinant-error upper bound; both actual thresholds survive')
    report['independent_exp_upper_rational'] = dict(
        numerator_hex=hex(needed_exp.numerator),
        denominator_hex=hex(needed_exp.denominator),terms=256)
    for name,ctx in [('DN',m.DN),('UP',m.UP),('RN',m.RN)]:
        flags=[k.__name__ for k,v in ctx.flags.items() if v]
        assert set(flags)<={'Inexact','Rounded'},(name,flags)
        report.setdefault('context_flags',{})[name]=flags
    assert hashlib.sha256(ORIGINAL.read_bytes()).hexdigest()==report['input_sha256']
    assert hashlib.sha256(OLD.read_bytes()).hexdigest()==report['inherited_input_sha256']
    assert report['source_sha256']['signed_pair_435.py']==old['reuse_provenance']['primitive_sha256']
    report['checks'].append('Original certificates and primitive source preserved; no exceptional Decimal flags beyond Inexact/Rounded')
    report.update(status='PASS',
                  signed_determinant=n['signed_determinant'],
                  original_norm=n['original_norm'],
                  trace_norm_error=n['trace_norm_error'],
                  determinant_perturbation_error=n['determinant_perturbation_error'],
                  actual_counts=[fresh[k]['count_with_multiplicity'] for k in ['inner_contour','outer_contour']],
                  required_counts=[2,2],
                  limitations='Reviewed code replay, not an independently implemented backend; installed executable unattested; no all-degree result.')
except Exception as exc:
    report['status']='FAIL'
    report['failures'].append(dict(type=type(exc).__name__,message=str(exc)))
    save()
    raise
save()
print(json.dumps({k:report[k] for k in ['status','signed_determinant',
    'original_norm','required_det_lower','required_norm_lower','actual_counts',
    'required_counts','failures']},indent=2))
print('Full audit report:',REPORT)
print('Full replay evidence:',OUT/ORIGINAL.name)
