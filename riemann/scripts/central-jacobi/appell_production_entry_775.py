"""One P_(2,0) test, using audited L778 coefficients, exact rational intervals.

No new transcendental evaluation, zero list, other entry or minor search.
The Q operations round outwards on the 10^-100 grid. All evidence is saved.
"""
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path
from audit_478 import Q

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'scripts/central-jacobi/appell-production-entry-775.json'
checks, failures = [], []
report = dict(scope='Only Appell P_(2,0); inherited L778 analytic/software contracts',
              rational_grid='1/10^100', checks=checks, failures=failures)


def check(name, passed):
    checks.append(dict(name=name, passed=bool(passed)))
    if not passed:
        failures.append(name)


def load(path):
    return json.loads((ROOT/path).read_text())


def digest(path):
    return hashlib.sha256((ROOT/path).read_bytes()).hexdigest()


def display(x, digits=24):
    scale = 10**digits
    def dec(n):
        return ('-' if n < 0 else '') + str(abs(n)//scale) + '.' + str(abs(n)%scale).zfill(digits)
    return [dec((x.lo*scale).__floor__()), dec((x.hi*scale).__ceil__())]


def run():
    source_path = 'scripts/actual-fredholm/fixed-pair-certificate-431.json'
    model_path = 'scripts/central-jacobi/fixed-model-certificate-476.json'
    a433_path = 'scripts/actual-fredholm/audit-433/audit-report.json'
    replay_path = 'scripts/actual-fredholm/audit-433/fixed-pair-certificate-431.json'
    a478_path = 'scripts/central-jacobi/audit-478/audit-report.json'
    paths = [source_path, model_path, a433_path, replay_path, a478_path,
             'scripts/central-jacobi/audit_478.py',
             'scripts/central-jacobi/appell_production_entry_775.py']
    report['input_hashes'] = {p: digest(p) for p in paths}
    ev = load(source_path)['evaluation']
    model, a433, replay, a478 = [load(p) for p in [model_path,a433_path,replay_path,a478_path]]
    for p in [source_path, model_path, 'scripts/central-jacobi/fixed_model_476.py']:
        check('current hash matches step478: '+p, digest(p) == a478['original_hashes'][p])
    check('source hash matches step433', digest(source_path) == a433['original_sha256'])
    check('source hash matches L791', digest(source_path) == model['source_sha256'])
    check('complete evaluator equals step433 replay', ev == replay['evaluation'])
    for label, a in [('433',a433),('478',a478)]:
        check('saved audit '+label+' PASS with empty failures', a['status']=='PASS' and a['failures']==[])
    check('all step478 saved checks passed', all(c['passed'] for c in a478['checks']))
    check('step433 evaluator replay check present', 'Exact equality of ALL recomputed fields: evaluation' in a433['checks'])
    check('step433 flags only expected inexact/rounded',
          all(set(v) <= {'Inexact','Rounded'} for v in a433['context_flags'].values()))
    check('complex uniform error radius exactly 1600', ev['uniform_disk_radius']==1600)
    check('at least six ordinary polynomial coefficients', len(ev['coefficients'])>=6)
    eg = Q(*ev['uniform_G_error'])
    check('positive uniform error below L778 bound', 0 < eg.lo <= eg.hi < F('3.141e-48'))
    report['uniform_G_error'] = eg.pair()
    report['coefficient_error_rule'] = 'E_G_upper / 1600^j, added to both sides at every j=0,...,5'
    if failures:
        return
    aa, inputs = [], []
    for j in range(6):
        raw = Q(*ev['coefficients'][j])
        error = eg.hi / 1600**j
        actual = raw + Q(-error,error)
        check('actual a_'+str(j)+' positive', actual.lo > 0)
        if j<5:
            saved = Q(*model['actual_a'][j])
            check('actual a_'+str(j)+' enclosed by audited L791 interval',
                  saved.lo <= actual.lo <= actual.hi <= saved.hi)
        aa.append(actual)
        inputs.append(dict(j=j, polynomial_coefficient=ev['coefficients'][j],
                           Cauchy_error_upper=str(error), actual_a=actual.pair()))
    report['coefficient_inputs'] = inputs
    if failures:
        return
    # L776: a_j=M_(2j)/(8*4^j*(2j)!), L040: e_j=M_(2j)/((2j)!*M_0).
    # Hence e_j=4^j*a_j/a_0. e_0 is EXACTLY 1, not interval a_0/a_0.
    ee = [Q(1)] + [(4**j)*aa[j]/aa[0] for j in range(1,6)]
    ss = [Q(0)]
    for k in range(1,6):
        value = Q(0)
        for j in range(1,k):
            value = value + ((-1)**(j-1))*ee[j]*ss[k-j]
        value = value + ((-1)**(k-1))*k*ee[k]
        ss.append(value)
    report['e'] = [v.pair() for v in ee]
    report['S'] = {str(k):ss[k].pair() for k in range(1,6)}
    check('S_2 normalization interval excludes zero positively', ss[2].lo > 0)
    if failures:
        return
    mm = [Q(1)] + [ss[j+2]/ss[2] for j in range(1,4)]
    # Theorem2.19: A=1, Z=M'/M. P_(2,0)=2![t^2]Z.
    entry = mm[3]-3*mm[1]*mm[2]+2*mm[1]*mm[1]*mm[1]
    # Check the same entry by finite triangular inversion, not an entry sweep.
    # Only row2 of R^-1 and column0 of Rbar are multiplied.
    rr = [[Q(1),Q(0),Q(0)], [mm[1],Q(1),Q(0)], [mm[2],2*mm[1],Q(1)]]
    inv = [[Q(0) for _ in range(3)] for _ in range(3)]
    for i in range(3):
        inv[i][i] = Q(1)
        for j in range(i):
            inv[i][j] = -sum((rr[i][k]*inv[k][j] for k in range(j,i)), Q(0))
    matrix_entry = sum((inv[2][j]*mm[j+1] for j in range(3)),Q(0))
    numerator = ss[5]*ss[2]*ss[2]-3*ss[3]*ss[4]*ss[2]+2*ss[3]*ss[3]*ss[3]
    quotient_entry = numerator/(ss[2]*ss[2]*ss[2])
    for label, other in [('triangular inversion',matrix_entry),('power-sum numerator',quotient_entry)]:
        check('entry enclosure overlaps '+label, max(entry.lo,other.lo) <= min(entry.hi,other.hi))
    sign = 'NEGATIVE' if entry.hi<0 else 'NONNEGATIVE' if entry.lo>=0 else 'INCONCLUSIVE'
    if sign=='NEGATIVE':
        check('triangular inversion strictly negative', matrix_entry.hi<0)
        check('power-sum numerator strictly negative', numerator.hi<0)
        check('quotient enclosure strictly negative', quotient_entry.hi<0)
    report['m'] = [v.pair() for v in mm]
    report['P20'] = entry.pair()
    report['inverse_row2'] = [v.pair() for v in inv[2]]
    report['P20_matrix'] = matrix_entry.pair()
    report['power_sum_numerator'] = numerator.pair()
    report['P20_quotient'] = quotient_entry.pair()
    report['summary'] = dict(P20_outward_24_places=display(entry), required_threshold='0', sign=sign,
        S2_outward_24_places=display(ss[2]),
        decision='Stop this Appell production-TP construction' if sign=='NEGATIVE' else
                 'Retire the single diagnostic; no propagation or sweep',
        qualification='Conditional on inherited L778 analytic/evaluator/backend contracts; no RH conclusion')


if __name__ == '__main__':
    try:
        run()
    except Exception as exc:
        failures.append(type(exc).__name__+': '+str(exc))
    report['status'] = 'PASS' if not failures else 'FAIL'
    OUT.write_text(json.dumps(report,indent=2)+'\n')
    print('status:',report['status'],'checks:',len(checks),'failures:',failures)
    print('actual/required:',report.get('summary',{}))
    print('full certificate:',OUT.relative_to(ROOT))
    raise SystemExit(bool(failures))
