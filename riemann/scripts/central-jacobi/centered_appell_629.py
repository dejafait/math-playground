"""One approved degree-2/3 lowering test; inherited L778/L791 contracts.

No transcendental evaluation or new degree search. Integer/Fraction
intervals round outward on the step478 10^-100 grid. Full evidence on disk.
"""
import hashlib
import json
import math
from fractions import Fraction as F
from pathlib import Path
from audit_478 import Q

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'scripts/central-jacobi/centered-appell-629.json'
checks, failures = [], []
evidence = {}


def check(name, passed):
    checks.append({'name': name, 'passed': bool(passed)})
    if not passed:
        failures.append(name)


def load(path):
    return json.loads((ROOT / path).read_text())


def contains(a, b):
    return a.lo <= b.lo <= b.hi <= a.hi


def digest(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def display(x):
    scale = 10**6
    lo = (x.lo * scale).__floor__()
    hi = (x.hi * scale).__ceil__()
    def dec(n):
        return ('-' if n < 0 else '') + str(abs(n)//scale) + '.' + str(abs(n)%scale).zfill(6)
    return [dec(lo), dec(hi)]


def run():
    model_path = 'scripts/central-jacobi/fixed-model-certificate-476.json'
    source_path = 'scripts/actual-fredholm/fixed-pair-certificate-431.json'
    data = load(model_path)
    source = load(source_path)['evaluation']
    a478 = load('scripts/central-jacobi/audit-478/audit-report.json')
    a433 = load('scripts/actual-fredholm/audit-433/audit-report.json')
    replay = load('scripts/actual-fredholm/audit-433/fixed-pair-certificate-431.json')
    paths = [model_path, source_path, 'scripts/central-jacobi/audit-478/audit-report.json',
             'scripts/actual-fredholm/audit-433/audit-report.json',
             'scripts/central-jacobi/audit_478.py',
             'scripts/central-jacobi/centered_appell_629.py']
    evidence['input_hashes'] = {p: digest(p) for p in paths}
    for p in (model_path, source_path):
        check('matches step478 hash ' + p, digest(p) == a478['original_hashes'][p])
    check('source matches L791', digest(source_path) == data['source_sha256'])
    check('source matches step433', digest(source_path) == a433['original_sha256'])
    check('entire evaluator matches step433 replay', source == replay['evaluation'])
    for name, audit in [('478', a478), ('433', a433)]:
        check('saved audit PASS ' + name, audit['status'] == 'PASS' and not audit['failures'])
    check('every saved step478 check passes', all(c['passed'] for c in a478['checks']))
    check('complex disk radius', source['uniform_disk_radius'] == 1600)
    eg = Q(*source['uniform_G_error'])
    check('positive inherited error below 3.141e-48', 0 < eg.lo <= eg.hi < F('3.141e-48'))
    check('same analytic error', data['uniform_G_error'] == source['uniform_G_error'])
    evidence['uniform_G_error'] = eg.pair()
    inputs = []
    gamma = []
    for j in range(4):
        coefficient = Q(*source['coefficients'][j])
        error = eg.hi / 1600**j
        actual = coefficient + Q(-error, error)
        saved_a = Q(*data['actual_a'][j])
        saved_g = Q(*data['gamma'][j])
        computed_g = saved_a * (8 * 4**j * math.factorial(j))
        check('Cauchy enclosure ' + str(j), contains(saved_a, actual))
        check('gamma normalization enclosure ' + str(j), contains(saved_g, computed_g))
        check('gamma positive ' + str(j), saved_g.lo > 0)
        inputs.append(dict(j=j, evaluator=coefficient.pair(), coefficient_error=str(error),
                           recomputed_actual_a=actual.pair(), actual_a=saved_a.pair(),
                           recomputed_gamma=computed_g.pair(), gamma=saved_g.pair()))
        gamma.append(saved_g)
    evidence['coefficient_inputs'] = inputs
    if failures:
        return
    r1, r2, r3 = [g/gamma[0] for g in gamma[1:]]
    h2, h3 = r1/r2, r2/r3
    u2 = 1/r2 - h2.square()
    u3 = 3*r1/r3 - 3*h3.square()
    v3 = -1/r3 + 3*r1*h3/r3 - 2*h3.square()*h3
    b2, b3, c3 = u2/2, u3/2, v3/2
    defect = b3-3*b2
    # Independent rearrangement of the same exact expression, with all
    # correlations enlarged, not assumed independent in reality.
    alternative = (3*(r1/r3-h3.square()-1/r2+h2.square()))/2
    check('defect enclosure excludes zero', defect.hi < 0 or defect.lo > 0)
    check('stated strict defect bounds', F('9.582501') < defect.lo <= defect.hi < F('9.582502'))
    check('rearranged defect excludes zero on same side',
          (defect.hi < 0 and alternative.hi < 0) or
          (defect.lo > 0 and alternative.lo > 0))
    check('two enclosures overlap', max(defect.lo, alternative.lo) <= min(defect.hi, alternative.hi))
    vals = dict(R1=r1, R2=r2, R3=r3, h2=h2, h3=h3, u2=u2, u3=u3, v3=v3,
                Q2_constant=b2, Q3_linear=b3, Q3_constant=c3,
                derivative_defect=defect, rearranged_defect=alternative)
    evidence['intervals'] = {k: v.pair() for k,v in vals.items()}
    evidence['outward_decimal_displays'] = {k: display(v) for k,v in vals.items()}
    evidence['required_defect_for_compatibility'] = '0 exactly'
    evidence['full_derivative_defect_coefficients_descending'] = ['0', '0', defect.pair()]


if __name__ == '__main__':
    try:
        run()
    except Exception as exc:
        failures.append(type(exc).__name__ + ': ' + str(exc))
    report = dict(scope='Centered monic actual P2/P3 additive-factor lowering test only',
                  contracts='L778/step433 analytic and software contracts; L791/step478 coefficients',
                  rational_grid='1/10^100', status='FAIL' if failures else 'PASS',
                  checks=checks, failures=failures, evidence=evidence)
    OUT.write_text(json.dumps(report, indent=2) + '\n')
    print('status:', report['status'], 'checks:', len(checks), 'failures:', failures)
    print('actual defect:', evidence.get('outward_decimal_displays', {}).get('derivative_defect'),
          'required: 0 exactly')
    print('full certificate:', OUT.relative_to(ROOT))
    raise SystemExit(bool(failures))
