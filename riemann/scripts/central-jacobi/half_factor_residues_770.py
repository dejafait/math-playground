"""Approved L825 two-pole test; exact rational arithmetic, inherited evaluator.

Run from the notebook: python3 scripts/central-jacobi/half_factor_residues_770.py
Only writes its new certificate. No quadrature, degree sweep or new backend.
"""
import hashlib
import json
import math
from fractions import Fraction as F
from pathlib import Path

from audit_631 import I, includes, var, const, add, mul, scale, power, serial_poly

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / 'scripts/central-jacobi/half-factor-residues-770.json'
checks, failures, evidence = [], [], {}


def check(name, passed):
    checks.append(dict(name=name, passed=bool(passed)))
    if not passed:
        failures.append(name)


def read(path):
    return json.loads((ROOT / path).read_text())


def digest(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def run():
    audit = read('scripts/central-jacobi/audit-631/audit-report.json')
    old = read('scripts/central-jacobi/centered-appell-629.json')
    data = read('scripts/central-jacobi/fixed-model-certificate-476.json')
    source_path = 'scripts/actual-fredholm/fixed-pair-certificate-431.json'
    source = read(source_path)['evaluation']
    for path, expected in audit['evidence']['original_hashes'].items():
        check('unchanged audited input '+path, digest(path) == expected)
    paths = [
        'scripts/central-jacobi/audit-631/audit-report.json',
        'scripts/central-jacobi/audit_631.py',
        'scripts/central-jacobi/centered-appell-629.json',
        'scripts/central-jacobi/fixed-model-certificate-476.json',
        source_path,
        'scripts/central-jacobi/audit-478/audit-report.json',
        'scripts/actual-fredholm/audit-433/audit-report.json',
        'lemmas/L825-centered-theta-additive-factors-appell-obstruction.md',
        'lemmas/L791-fixed-central-five-root-jacobi-model.md',
        'lemmas/L778-actual-fixed-pair-fredholm-norm-certificate.md',
        'drafts/literature/2026-11-13-half-factor-two-residue-test-768.md',
        'scripts/central-jacobi/half_factor_residues_770.py',
    ]
    evidence['input_hashes'] = {p: digest(p) for p in paths}
    for label, report in [('631', audit), ('629', old),
                          ('478', read(paths[5])), ('433', read(paths[6]))]:
        entries = report['checks']
        valid = (all(isinstance(x, str) and bool(x) for x in entries)
                 if label == '433' else all(x['passed'] is True for x in entries))
        check('saved audit PASS without failures '+label,
              report['status'] == 'PASS' and report['failures'] == [] and bool(entries) and valid)
    check('source hash in L791 data', digest(source_path) == data['source_sha256'])
    check('complete evaluator matches audited replay', source == read(
        'scripts/actual-fredholm/audit-433/fixed-pair-certificate-431.json')['evaluation'])
    eg = I(*source['uniform_G_error'])
    check('complex disk and analytic error bound', source['uniform_disk_radius'] == 1600
          and 0 < eg.lo <= eg.hi < F('3.141e-48'))
    gamma, records = [], []
    for j in range(4):
        co = I(*source['coefficients'][j])
        err = eg.hi/1600**j
        actual = co + I(-err, err)
        saved_a, g = I(*data['actual_a'][j]), I(*data['gamma'][j])
        prior = old['evidence']['coefficient_inputs'][j]
        check('complete saved coefficient matches '+str(j),
              I(*prior['evaluator']).pair() == co.pair()
              and I(*prior['actual_a']).pair() == saved_a.pair()
              and I(*prior['gamma']).pair() == g.pair()
              and F(prior['coefficient_error']) == err)
        check('Cauchy error and gamma normalization '+str(j),
              includes(saved_a, actual) and includes(g, saved_a*(8*4**j*math.factorial(j)))
              and g.lo > 0)
        gamma.append(g)
        records.append(dict(j=j, evaluator=co.pair(), coefficient_error=str(err),
                            actual_a_exact=actual.pair(), actual_a=saved_a.pair(), gamma=g.pair()))
    evidence['coefficient_inputs'] = records
    r1, r2, r3 = [g/gamma[0] for g in gamma[1:]]
    h2, h3 = r1/r2, r2/r3
    a = (1/r2-h2.sq())/2
    b = (3*r1/r3-3*h3.sq())/2
    c = (-1/r3+3*r1*h3/r3-2*h3.sq()*h3)/2
    exact = dict(Q2_constant=a, Q3_linear=b, Q3_constant=c)
    evidence['exact_recomputed_coefficients'] = {k: v.pair() for k, v in exact.items()}
    # Use a proven outward six-decimal hull, never decimal approximations.
    hulls = {k: I(*old['evidence']['outward_decimal_displays'][k]) for k in exact}
    for k, v in exact.items():
        check('complete original interval contains exact recomputation '+k,
              includes(I(*old['evidence']['intervals'][k]), v))
        check('rational display hull contains exact recomputation '+k, includes(hulls[k], v))
    a, b, c = [hulls[k] for k in ('Q2_constant', 'Q3_linear', 'Q3_constant')]
    evidence['coefficient_hulls_used'] = {k: v.pair() for k, v in hulls.items()}
    check('two simple real denominator roots', a.hi < 0)
    # Fixed six-place rational sqrt enclosure, certified by exact squares.
    radicand = -a
    grid = 10**6
    low = math.isqrt((radicand.lo*grid**2).numerator // (radicand.lo*grid**2).denominator)
    high = math.isqrt((radicand.hi*grid**2).numerator // (radicand.hi*grid**2).denominator)+1
    t = I(F(low, grid), F(high, grid))
    check('strict rational sqrt enclosure', 0 < t.lo and t.lo**2 < radicand.lo
          and radicand.hi < t.hi**2)
    roots = dict(negative=-t, positive=t)
    # Exact polynomial division: Q3 = y Q2 + (b-a)y+c.
    # Expanding y(y^2+a)+(b-a)y+c gives coefficients [c,b,0,1].
    symbolic = dict(Q2_ascending=['a','0','1'], Q3_ascending=['c','b','0','1'],
                    division='y*(y^2+a)+(b-a)*y+c = y^3+b*y+c',
                    root_relation='r^2=-a',
                    root_numerator='r^3+b*r+c=(b-a)*r+c',
                    derivative='Q2_prime(r)=2*r',
                    residue='((b-a)*r+c)/(2*r)=(b-a)/2+c/(2*r)',
                    partial_fractions='Q3/Q2=y+rho_minus/(y+t)+rho_plus/(y-t)',
                    residue_sum='rho_minus+rho_plus=b-a',
                    residue_difference='t*(rho_plus-rho_minus)=c')
    # Full multivariate identities, not numerical sample substitutions.
    av, bv, cv, yv, tv = [var(k) for k in ('a','b','c','y','t')]
    diff = add(bv, scale(-1,av))
    lhs = add(mul(yv,add(power(yv,2),av)),mul(diff,yv),cv)
    rhs = add(power(yv,3),mul(bv,yv),cv)
    check('full symbolic division identity', lhs == rhs)
    # Clear 2t from the two simple-pole terms. Their combined numerator
    # is ((b-a)t-c)(y-t)+((b-a)t+c)(y+t)=2t((b-a)y+c).
    combined = add(mul(add(mul(diff,tv),scale(-1,cv)),add(yv,scale(-1,tv))),
                   mul(add(mul(diff,tv),cv),add(yv,tv)))
    expected = scale(2,mul(tv,add(mul(diff,yv),cv)))
    check('full partial fraction numerator identity', combined == expected)
    symbolic['expanded_division'] = serial_poly(lhs)
    symbolic['cleared_partial_fraction_numerator'] = serial_poly(combined)
    evidence['symbolic_identities'] = symbolic
    residues = {label: (b-a)/2+c/(2*r) for label, r in roots.items()}
    direct = {label: ((b-a)*r+c)/(2*r) for label, r in roots.items()}
    for label, residue in residues.items():
        check('nonzero denominator '+label, not roots[label].lo <= 0 <= roots[label].hi)
        check('negative residue '+label, residue.hi < 0)
        check('direct expression also negative '+label, direct[label].hi < 0)
        check('two algebraically equal enclosures overlap '+label,
              max(residue.lo,direct[label].lo) <= min(residue.hi,direct[label].hi))
    evidence['roots'] = {k: v.pair() for k, v in roots.items()}
    evidence['sqrt_square_checks'] = dict(radicand=radicand.pair(),
        lower_square=str(t.lo**2), upper_square=str(t.hi**2))
    evidence['residues'] = {k: v.pair() for k, v in residues.items()}
    evidence['direct_residue_enclosures'] = {k: v.pair() for k, v in direct.items()}
    evidence['required_threshold'] = '0 exactly; both residues must be strictly negative'
    evidence['certified_simple_bounds'] = {}
    for label, residue in residues.items():
        # Outward integer floor/ceiling to a six-place rational grid.
        lower = residue.lo*grid
        upper = residue.hi*grid
        display = I(F(lower.numerator//lower.denominator,grid),
                    F(-((-upper.numerator)//upper.denominator),grid))
        check('strict six-place residue bound '+label,
              display.lo < residue.lo <= residue.hi < display.hi < 0)
        evidence['certified_simple_bounds'][label] = display.pair()
    for path, expected in evidence['input_hashes'].items():
        check('input preserved '+path, digest(path) == expected)


if __name__ == '__main__':
    try:
        run()
    except Exception as exc:
        failures.append(type(exc).__name__+': '+str(exc))
    result = dict(scope='L825 original-coordinate Q3/Q2 only; inherited L778/L791 contracts',
                  method='exact Fraction endpoints; fixed rational square brackets; imported interlacing criterion',
                  reproduction='python3 scripts/central-jacobi/half_factor_residues_770.py',
                  status='FAIL' if failures else 'PASS', checks=checks, failures=failures, evidence=evidence)
    OUTPUT.write_text(json.dumps(result, indent=2)+'\n')
    print('status:',result['status'],'checks:',len(checks),'failures:',failures)
    print('roots:',evidence.get('roots'))
    print('actual residue bounds:',evidence.get('certified_simple_bounds'))
    print('required: both < 0 exactly; certificate:',OUTPUT.relative_to(ROOT))
    raise SystemExit(bool(failures))
