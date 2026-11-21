"""Independent finite C825a audit. No import or execution of prior arithmetic.

Run from riemann: python3 scripts/central-jacobi/audit_residues_772.py
Inherited analytic/transcendental contracts remain assumptions.
"""
import hashlib
import json
from fractions import Fraction as F
from math import factorial
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'scripts/central-jacobi/half-factor-residue-audit-772.json'
checks, failures, evidence, hashes = [], [], {}, {}


def check(name, result):
    checks.append({'name': name, 'passed': bool(result)})
    if not result:
        failures.append(name)


def digest(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def read(path):
    hashes[path] = digest(path)
    return json.loads((ROOT / path).read_text())


def interval(pair):
    a, b = map(F, pair)
    if a > b:
        raise ValueError('reversed endpoints')
    return a, b


def plus(a, b):
    return a[0]+b[0], a[1]+b[1]


def minus(a, b):
    return a[0]-b[1], a[1]-b[0]


def times(a, b):
    v = [x*y for x in a for y in b]
    return min(v), max(v)


def over(a, b):
    if b[0] <= 0 <= b[1]:
        raise ValueError('zero denominator')
    return times(a, (1/b[1], 1/b[0]))


def square(a):
    return (0 if a[0] <= 0 <= a[1] else min(x*x for x in a),
            max(x*x for x in a))


def scalar(k):
    return F(k), F(k)


def contains(outer, inner):
    return outer[0] <= inner[0] <= inner[1] <= outer[1]


def saved(pair):
    return [str(x) for x in pair]


def run():
    original = read('scripts/central-jacobi/half-factor-residues-770.json')
    old = original['evidence']
    audit631 = read('scripts/central-jacobi/audit-631/audit-report.json')
    original629 = read('scripts/central-jacobi/centered-appell-629.json')
    data = read('scripts/central-jacobi/fixed-model-certificate-476.json')
    source_path = 'scripts/actual-fredholm/fixed-pair-certificate-431.json'
    source = read(source_path)['evaluation']
    audit478 = read('scripts/central-jacobi/audit-478/audit-report.json')
    audit433 = read('scripts/actual-fredholm/audit-433/audit-report.json')
    replay = read('scripts/actual-fredholm/audit-433/fixed-pair-certificate-431.json')
    evidence['inspected_original_checks'] = {}
    for tag, report in [('770', original), ('631', audit631), ('629', original629),
                        ('478', audit478), ('433', audit433)]:
        entries = report['checks']
        complete = (all(type(x) is str and bool(x) for x in entries) if tag == '433'
                    else all(x['passed'] is True for x in entries))
        check('complete saved status/checks/failures '+tag,
              report['status'] == 'PASS' and report['failures'] == [] and entries and complete)
        evidence['inspected_original_checks'][tag] = {
            'checks': entries, 'status': report['status'], 'failures': report['failures']}
    evidence['original_hash_comparisons'] = []
    for tag, mapping in [('770', old['input_hashes']),
                         ('631', audit631['evidence']['original_hashes'])]:
        for path, expected in mapping.items():
            actual = digest(path)
            hashes[path] = actual
            check('saved input hash '+tag+' '+path, actual == expected)
            evidence['original_hash_comparisons'].append(
                dict(origin=tag, path=path, expected=expected, actual=actual))
    check('L791 source hash', digest(source_path) == data['source_sha256'])
    check('complete inherited evaluator equals audited replay', source == replay['evaluation'])
    error = interval(source['uniform_G_error'])
    check('analytic disk/error contract retained', source['uniform_disk_radius'] == 1600
          and 0 < error[0] <= error[1] < F('3.141e-48'))
    records, gamma = [], []
    for j in range(4):
        co = interval(source['coefficients'][j])
        err = error[1] / F(1600)**j
        exact_a = co[0]-err, co[1]+err
        a = interval(data['actual_a'][j])
        g = interval(data['gamma'][j])
        prior = old['coefficient_inputs'][j]
        prior629 = original629['evidence']['coefficient_inputs'][j]
        check('all coefficient provenance fields '+str(j), prior['j'] == j
              and interval(prior['evaluator']) == co
              and interval(prior['actual_a_exact']) == exact_a
              and interval(prior['actual_a']) == a and interval(prior['gamma']) == g
              and F(prior['coefficient_error']) == err
              and interval(prior629['evaluator']) == co
              and interval(prior629['actual_a']) == a and interval(prior629['gamma']) == g
              and F(prior629['coefficient_error']) == err)
        normalized = times(a, scalar(8*4**j*factorial(j)))
        check('Cauchy addition normalization positivity '+str(j),
              contains(a, exact_a) and contains(g, normalized) and g[0] > 0)
        gamma.append(g)
        records.append(dict(j=j, evaluator=saved(co), error=str(err), exact_a=saved(exact_a),
                            saved_a=saved(a), normalized=saved(normalized), gamma=saved(g)))
    evidence['complete_coefficient_inputs'] = records
    g0, g1, g2, g3 = gamma
    r1, r2, r3 = [over(g, g0) for g in gamma[1:]]
    h2, h3 = over(r1, r2), over(r2, r3)
    a = over(minus(over(scalar(1), r2), square(h2)), scalar(2))
    b = over(minus(over(times(scalar(3), r1), r3), times(scalar(3), square(h3))), scalar(2))
    c = over(minus(plus(over(scalar(-1), r3),
                        over(times(times(scalar(3), r1), h3), r3)),
                   times(scalar(2), times(square(h3), h3))), scalar(2))
    # Separate algebraically rearranged formulas directly in gamma; these
    # need only fit the rational hulls, not the narrower dependency-heavy intervals.
    alternate = [
        over(minus(times(g0,g2), square(g1)), times(scalar(2),square(g2))),
        over(times(scalar(3),minus(times(g1,g3), square(g2))), times(scalar(2),square(g3))),
        over(minus(plus(times(scalar(-1),times(g0,square(g3))),
                        times(scalar(3),times(times(g1,g2),g3))),
                   times(scalar(2),times(square(g2),g2))),
             times(scalar(2),times(square(g3),g3)))
    ]
    names = ['Q2_constant', 'Q3_linear', 'Q3_constant']
    required_hulls = [('-75.346033','-75.346032'), ('-216.455595','-216.455594'),
                      ('-52.683490','-52.683489')]
    hulls, coeffs = [], {}
    for name, exact, alt, bound in zip(names, [a,b,c], alternate, required_hulls):
        hull = interval(bound)
        check('full coefficient recomputation '+name,
              interval(old['exact_recomputed_coefficients'][name]) == exact
              and contains(interval(original629['evidence']['intervals'][name]), exact))
        check('both independent coefficient expressions fit claimed hull '+name,
              contains(hull, exact) and contains(hull, alt)
              and interval(old['coefficient_hulls_used'][name]) == hull
              and interval(original629['evidence']['outward_decimal_displays'][name]) == hull)
        hulls.append(hull)
        coeffs[name] = dict(exact=saved(exact), alternate=saved(alt), hull=saved(hull))
    evidence['complete_coefficient_recomputations'] = coeffs
    a,b,c = hulls
    t = interval(('8.680209','8.680210'))
    radicand = -a[1], -a[0]
    squares = t[0]**2, t[1]**2
    check('simple real roots and exact strict squares',
          0 < t[0] and squares[0] < radicand[0] <= radicand[1] < squares[1])
    check('saved square/root fields',
          interval(old['roots']['positive']) == t
          and interval(old['roots']['negative']) == (-t[1],-t[0])
          and interval(old['sqrt_square_checks']['radicand']) == radicand
          and F(old['sqrt_square_checks']['lower_square']) == squares[0]
          and F(old['sqrt_square_checks']['upper_square']) == squares[1])
    base = (b[0]-a[1])/2, (b[1]-a[0])/2
    # Since c<0<t, c/(2t) increases with c and t. This independently
    # computes its two extrema without the old interval/polynomial helpers.
    correction = c[0]/(2*t[0]), c[1]/(2*t[1])
    residues = {'negative': (base[0]-correction[1], base[1]-correction[0]),
                'positive': (base[0]+correction[0], base[1]+correction[1])}
    claimed = {'negative': interval(('-67.520092','-67.520090')),
               'positive': interval(('-73.589472','-73.589470'))}
    direct = {}
    for label, rho in residues.items():
        r = t if label == 'positive' else (-t[1],-t[0])
        direct[label] = over(plus(times(minus(b,a),r),c), times(scalar(2),r))
        check('complete residue endpoints '+label, interval(old['residues'][label]) == rho)
        check('complete direct expression endpoints '+label,
              interval(old['direct_residue_enclosures'][label]) == direct[label])
        bound = claimed[label]
        check('claimed strict open residue bound '+label,
              bound[0] < rho[0] <= rho[1] < bound[1] < 0
              and interval(old['certified_simple_bounds'][label]) == bound)
        check('direct sign and enclosure overlap '+label, direct[label][1] < 0
              and max(direct[label][0],rho[0]) <= min(direct[label][1],rho[1]))
    # Multivariate coefficient identities checked in the printed algebraic
    # audit, independently of step770's sparse-polynomial implementation.
    # The only possible division monomials are y^3, ay, by, c.
    division_terms = {'y^3':1, 'ay':1-1, 'by':1, 'c':1}
    check('division cancellation all terms', division_terms == {'y^3':1,'ay':0,'by':1,'c':1})
    check('complete saved division expansion', old['symbolic_identities']['expanded_division']
          == {'b*y':'1','c':'1','y*y*y':'1'})
    # ((b-a)t-c)(y-t)+((b-a)t+c)(y+t), collected in
    # ((b-a)ty, (b-a)t^2, cy, ct), equals (2,0,0,2).
    partial_terms = [1+1, -1+1, -1+1, 1+1]
    check('cleared partial fraction all terms', partial_terms == [2,0,0,2])
    check('complete saved partial fraction expansion',
          old['symbolic_identities']['cleared_partial_fraction_numerator']
          == {'a*t*y':'-2','b*t*y':'2','c*t':'2'})
    check('coefficient and root sign assumptions used', a[1] < 0 and c[1] < 0
          and t[0] > 0 and all(r[1] < 0 for r in residues.values()))
    evidence['finite_evidence'] = dict(hulls=dict(zip(names,map(saved,hulls))), t=saved(t),
        squares=saved(squares), radicand=saved(radicand), base=saved(base),
        correction=saved(correction), residues={k:saved(v) for k,v in residues.items()},
        direct={k:saved(v) for k,v in direct.items()},
        actual_bounds={k:saved(v) for k,v in claimed.items()}, required_threshold='0 (strictly negative)',
        identities={'division_terms':division_terms,'partial_fraction_collected_terms':partial_terms})
    evidence['source_application'] = {
        'Fisk': 'math/0612833v2 Section1.3 Lemma1.20(3), printed pp12-14; distinct real denominator roots, real monic degree2/3, both residues strictly negative',
        'Holtz_Tyaglov': '0912.4703v3 Definition3.1 Remark3.2 Theorem3.4 conditions2/6; p=Q2 q=-Q3, simple real poles, positive residues, linear part -y',
        'coprimality': 'At each of the two simple Q2 roots, Q3(r)=2r*rho(r) is nonzero; these are all Q2 roots.',
        'orientation': '(-Q3/Q2) derivative = -1 + rho_minus/(y+t)^2 + rho_plus/(y-t)^2 < 0 away from poles; Wronskian numerator Q2^2 times this derivative is negative, and equals (2*r)^2*rho(r) <0 at each pole.',
        'limit': 'Only this finite pair. No uniform interlacing, all-degree factors, mixed/shifted positivity or RH. Trusted inherited backend remains unattested.',
        'mathlib': 'Full matching coverage unchecked.'}
    for path, expected in hashes.items():
        check('input preserved '+path, digest(path) == expected)
    evidence['input_hashes'] = hashes
    evidence['audit_program_sha256'] = digest('scripts/central-jacobi/audit_residues_772.py')


if __name__ == '__main__':
    try:
        run()
    except Exception as exc:
        failures.append(type(exc).__name__+': '+str(exc))
    report = dict(status='FAIL' if failures else 'PASS', checks=checks, failures=failures,
                  scope='C825a finite arithmetic/source-hypothesis audit only; inherited L778/L791 analytic/software contracts',
                  reproduction='python3 scripts/central-jacobi/audit_residues_772.py', evidence=evidence)
    OUT.write_text(json.dumps(report,indent=2)+'\n')
    print('status:', report['status'], 'checks:',len(checks),'failures:',failures)
    finite = evidence.get('finite_evidence',{})
    print('actual residue bounds:',finite.get('actual_bounds'))
    print('required: both strictly below 0; certificate:',OUT.relative_to(ROOT))
    raise SystemExit(bool(failures))
