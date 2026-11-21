"""Independent L796 finite audit. Original programs/certificates are read-only.

No original interval or symbolic implementation is imported. Analytic evaluator
and backend guarantees remain inherited from L778/L791, not proved here.
"""
import hashlib
import json
import math
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = Path(__file__).resolve().parent
OUT = BASE / 'audit-506'
checks = []


def check(name, passed):
    checks.append({'name': name, 'passed': bool(passed)})


def read(path):
    return json.loads(path.read_text())


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


# Tuple intervals. Reciprocal endpoints and all operations are exact rationals.
def interval(v):
    if isinstance(v, tuple):
        return v
    return F(v), F(v)


def add(u, v):
    u, v = interval(u), interval(v)
    return u[0]+v[0], u[1]+v[1]


def neg(u):
    return -u[1], -u[0]


def mul(u, v):
    u, v = interval(u), interval(v)
    products = [p*q for p in u for q in v]
    return min(products), max(products)


def div(u, v):
    v = interval(v)
    if v[0] <= 0 <= v[1]:
        raise ArithmeticError('interval denominator meets zero')
    return mul(u, (1/v[1], 1/v[0]))


def parse(v):
    result = tuple(F(x) for x in v)
    if len(result) != 2 or result[0] > result[1]:
        raise ArithmeticError('malformed interval')
    return result


def contains(outer, inner):
    return outer[0] <= inner[0] <= inner[1] <= outer[1]


def pair(u):
    return [str(x) for x in u]


def outward(u):
    lo, hi = u[0]*10**6, u[1]*10**6
    return [str(F(lo.numerator//lo.denominator, 10**6)),
            str(F(-((-hi.numerator)//hi.denominator), 10**6))]


# Integer polynomials in (a,b,c,x), after clearing denominators. Unlike
# step504, no Laurent polynomial operations or formal division are used.
def const(n):
    return {(0, 0, 0, 0): n} if n else {}


def padd(p, q):
    terms = dict(p)
    for k, v in q.items():
        terms[k] = terms.get(k, 0)+v
    return {k: v for k, v in terms.items() if v}


def pneg(p):
    return {k: -v for k, v in p.items()}


def pmul(p, q):
    terms = {}
    for k, v in p.items():
        for l, w in q.items():
            key = tuple(k[i]+l[i] for i in range(4))
            terms[key] = terms.get(key, 0)+v*w
    return {k: v for k, v in terms.items() if v}


def product(*ps):
    p = const(1)
    for q in ps:
        p = pmul(p, const(q) if isinstance(q, int) else q)
    return p


def total(*ps):
    p = {}
    for q in ps:
        p = padd(p, const(q) if isinstance(q, int) else q)
    return p


def symbolic():
    a, b, c, x = [{tuple(int(k == j) for k in range(4)): 1} for j in range(4)]
    ax_minus_1 = total(product(a, x), -1)
    p2 = total(product(b, x, x), product(-2, a, x), 1)
    p3 = total(product(-1, c, x, x, x), product(3, b, x, x),
               product(-3, a, x), 1)
    # Cleared residuals for xQ0-Q1-alpha0, xQ1-Q2-alpha1 Q1-beta1,
    # and xQ2-Q3-alpha2 Q2-beta2 Q1-delta, respectively.
    r0 = total(product(a, x), pneg(ax_minus_1), -1)
    r1 = total(product(a, b, x, ax_minus_1), product(-1, a, a, p2),
               product(-1, total(product(2, a, a), pneg(b)), ax_minus_1),
               pneg(total(product(a, a), pneg(b))))
    r2 = total(product(a, b, c, x, p2), product(a, b, b, p3),
               product(-1, a, total(product(3, b, b), product(-2, a, c)), p2),
               product(-1, total(product(b, c), product(3, a, b, b),
                                 product(-4, a, a, c)), ax_minus_1),
               pneg(total(product(a, b, b), product(b, c), product(-2, a, a, c))))
    return [r0, r1, r2]


def audit():
    original_path = BASE/'favard-prefix-certificate-504.json'
    data_path = BASE/'fixed-model-certificate-476.json'
    prior_path = BASE/'audit-478/audit-report.json'
    old, data, prior = read(original_path), read(data_path), read(prior_path)
    paths = [original_path, data_path, prior_path, BASE/'favard_prefix_504.py']
    check('canonical gamma source hash', sha(data_path) ==
          '2b429e4029fd7f50b30ea61b43d1be5aa22155b4c680c69440a716ff26643b2e')
    for name, expected in old['provenance'].items():
        check('step504 provenance '+name, sha(ROOT/name) == expected)
    check('step478 status', prior['status'] == 'PASS' and prior['failures'] == [])
    check('complete inherited hash record', old['inherited_original_hashes'] == prior['original_hashes'])
    for name, expected in prior['original_hashes'].items():
        check('inherited hash '+name, sha(ROOT/name) == expected)

    source_path = ROOT/'scripts/actual-fredholm/fixed-pair-certificate-431.json'
    source = read(source_path)
    evaluation = source['evaluation']
    older_audit = read(ROOT/'scripts/actual-fredholm/audit-433/audit-report.json')
    older_replay = read(ROOT/'scripts/actual-fredholm/audit-433/fixed-pair-certificate-431.json')
    # Inspect/recheck precisely the inherited data used, not unrelated model fitting.
    check('source hash matches L791 and step433', sha(source_path) == data['source_sha256'] == older_audit['original_sha256'])
    check('step433 evaluator replay equality', evaluation == older_replay['evaluation'])
    check('step433 status', older_audit['status'] == 'PASS' and older_audit['failures'] == [])
    check('complex Cauchy radius', evaluation['uniform_disk_radius'] == 1600)
    error = parse(evaluation['uniform_G_error'])
    check('complex error bound retained', data['uniform_G_error'] == evaluation['uniform_G_error'] and
          0 < error[0] <= error[1] < F('3.141e-48'))
    gamma = [parse(v) for v in data['gamma'][:4]]
    coefficient_evidence = []
    for j in range(4):
        e = error[1]/1600**j
        actual = add(parse(evaluation['coefficients'][j]), (-e, e))
        saved_actual = parse(data['actual_a'][j])
        calculated_gamma = mul(saved_actual, 8*4**j*math.factorial(j))
        check('Cauchy-enlarged actual coefficient '+str(j), contains(saved_actual, actual))
        check('gamma normalization enclosure '+str(j), contains(gamma[j], calculated_gamma))
        check('gamma positivity '+str(j), gamma[j][0] > 0)
        coefficient_evidence.append({'index': j, 'coefficient_error': str(e),
                                     'actual_recomputed': pair(actual),
                                     'actual_saved': pair(saved_actual),
                                     'gamma_recomputed': pair(calculated_gamma),
                                     'gamma_saved': pair(gamma[j])})
    check('full selected gamma decimal inputs', old['input_gamma_decimal'] == data['gamma'][:4])
    check('full selected gamma rational inputs', old['input_gamma_rational'] == [pair(v) for v in gamma])
    names = ([f'actual_a {j}' for j in range(4)] + [f'gamma {j}' for j in range(4)] +
             [f'gamma positivity {j}' for j in range(4)] +
             ['inherited source hash matches L791', 'inherited source hash matches L778 audit',
              'inherited evaluator equals complete audited replay', 'prior L778 audit passed',
              'complex Cauchy radius', 'inherited error positive and below stated bound',
              'error interval retained unchanged'])
    selected = [v for v in prior['checks'] if v['name'] in names]
    check('nineteen selected provenance checks complete', len(set(names)) == len(names) == len(selected) == 19
          and {v['name'] for v in selected} == set(names) and all(v['passed'] for v in selected)
          and old['selected_audit_checks'] == selected)

    a, b, c = [div(g, gamma[0]) for g in gamma[1:]]
    aa, bb, ab = mul(a, a), mul(b, b), mul(a, b)
    alpha = [div(1, a), add(div(mul(2, a), b), neg(div(1, a))),
             add(div(mul(3, b), c), neg(div(mul(2, a), b)))]
    beta = [add(div(1, b), neg(div(1, aa))),
            add(add(div(1, b), div(mul(3, a), c)), neg(div(mul(4, aa), bb)))]
    delta = add(add(div(1, c), div(1, ab)), neg(div(mul(2, a), bb)))
    denominators = dict(gamma0=gamma[0], a=a, b=b, c=c, a_squared=aa, b_squared=bb, a_times_b=ab)
    check('all denominator lower endpoints positive', all(v[0] > 0 for v in denominators.values()))
    check('conservative lower bounds in proof', gamma[0][0] > F('.49') and a[0] > F('.02')
          and b[0] > F('.0004') and c[0] > F('.00001'))
    check('complete normalized R intervals', old['R1_R2_R3'] == [pair(v) for v in (a, b, c)])
    check('complete denominator intervals', old['denominators'] == {k: pair(v) for k, v in denominators.items()})
    check('monic leading divisors', old['monic_leading_divisors_P0_to_P3'] ==
          [pair(interval(1)), pair(neg(a)), pair(b), pair(neg(c))])
    check('complete alpha intervals', old['alpha'] == [pair(v) for v in alpha])
    check('complete beta intervals', old['beta'] == [pair(v) for v in beta])
    check('complete forbidden interval', old['forbidden_Q0_coefficient'] == pair(delta))
    display = dict(alpha=[outward(v) for v in alpha], beta=[outward(v) for v in beta], delta=outward(delta))
    check('outward rational display equality', old['outward_display'] == display)
    stated_beta = [parse(['140.199017', '140.199018']), parse(['256.660342', '256.660343'])]
    stated_delta = parse(['-645.225425', '-645.225424'])
    check('all printed bounds enclose exact intervals', all(contains(u, v) for u, v in zip(stated_beta, beta))
          and contains(stated_delta, delta))
    check('both beta strictly positive', all(v[0] > 0 for v in beta))
    check('delta strictly below required zero', delta[1] < 0)
    residuals = symbolic()
    check('independent denominator-cleared polynomial identities', all(not r for r in residuals))
    check('step504 symbolic formulas and residuals', old['symbolic'] == dict(
          variables=['a', 'b', 'c', 'x'], recurrence_residuals=[[], [], []],
          alpha=['1/a', '2*a/b-1/a', '3*b/c-2*a/b'],
          beta=['1/b-1/a^2', '1/b+3*a/c-4*a^2/b^2'],
          forbidden_Q0_coefficient='1/c+1/(a*b)-2*a/b^2'))
    check('criterion and verification records', old['requirements'] == dict(forbidden_Q0_coefficient='0', beta1='>0', beta2='>0')
          and old['tests'] == dict(symbolic_identities=True, positive_denominators=True,
                                  beta_proved_positive=[True, True], beta_proved_nonpositive=[False, False],
                                  forbidden_coefficient_excludes_zero=True)
          and old['criterion_failures'] == ['nonzero forbidden Q0 coefficient']
          and old['verification_failures'] == [] and old['outcome'] == 'ORTHOGONALITY_OBSTRUCTION')
    check('original artifacts unchanged', all(sha(ROOT/name) == digest for name, digest in original_hashes.items()))
    return dict(scope='L796 actual P0..P3 finite audit only; inherited L778/L791 analytic and software contracts',
                coefficient_evidence=coefficient_evidence, denominators={k: pair(v) for k, v in denominators.items()},
                alpha=[pair(v) for v in alpha], beta=[pair(v) for v in beta], delta=pair(delta),
                polynomial_checks=dict(variables=['a','b','c','x'], clearing_factors=['a','a^2*b','a*b^2*c'],
                                       residuals=residuals),
                outward_display=display, required_delta='0', required_beta='>0',
                criterion_failure='nonzero forbidden Q0 coefficient',
                audited_paths={str(p.relative_to(ROOT)): sha(p) for p in paths})


original_hashes = {str(p.relative_to(ROOT)): sha(p) for p in
                  (BASE/'favard-prefix-certificate-504.json', BASE/'favard_prefix_504.py',
                   BASE/'fixed-model-certificate-476.json', BASE/'audit-478/audit-report.json')}
evidence = {}
try:
    evidence = audit()
except Exception as exc:
    check('audit execution '+type(exc).__name__+': '+str(exc), False)
failures = [v['name'] for v in checks if not v['passed']]
report = dict(status='PASS' if not failures else 'FAIL', checks=checks, failures=failures,
              original_hashes=original_hashes, program_sha256=sha(Path(__file__)), evidence=evidence)
OUT.mkdir(exist_ok=True)
path = OUT/'audit-report.json'
path.write_text(json.dumps(report, indent=2)+'\n')
print('L796 audit:', report['status'], '; checks:', len(checks), '; verification failures:', failures)
if evidence:
    print('actual outward bounds:', evidence['outward_display'])
    print('required: delta=0; beta1,beta2>0; criterion failure:', evidence['criterion_failure'])
print('full certificate:', path.relative_to(ROOT))
raise SystemExit(bool(failures))
