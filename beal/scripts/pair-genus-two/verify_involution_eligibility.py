"""Independent exact certificate replay, sharing the producer's cumulative caps."""
from fractions import Fraction as Q
from math import comb, gcd, isqrt, lcm
from pathlib import Path
import hashlib
import json

BASE = Path(__file__).resolve().parent
ROOT = BASE.parent.parent
LEDGER = BASE/'involution-eligibility-ledger.json'
CERT = BASE/'involution-eligibility-certificate.json'
OUT = BASE/'involution-eligibility-verification.json'
ledger = json.loads(LEDGER.read_text())
caps = ledger['caps']
assert caps == dict(divisor_trials=10000, work=200000, degree=64, bits=4096)
run = dict(status='REPLAY_IN_PROGRESS', start=ledger['used'].copy())
ledger['runs'].append(run)
checks = []
max_degree = 0
max_bits = 0


def charge(kind='work', n=1):
    if ledger['used'][kind]+n > caps[kind]:
        raise RuntimeError('CAP_STOP: '+kind)
    ledger['used'][kind] += n


def nodes(x):
    if isinstance(x, dict):
        return 1+sum(nodes(v) for v in x.values())
    if isinstance(x, list):
        return 1+sum(nodes(v) for v in x)
    return 1


def check(name, ok):
    charge()
    checks.append(dict(name=name, ok=bool(ok)))
    assert ok, name


def clean(p):
    global max_degree, max_bits
    p = {i: Q(a) for i, a in p.items() if a}
    degree = max(p, default=0)
    bits = max((max(abs(a.numerator).bit_length(), a.denominator.bit_length())
                for a in p.values()), default=0)
    assert degree <= caps['degree'] and bits <= caps['bits']
    max_degree, max_bits = max(max_degree, degree), max(max_bits, bits)
    return p


def dense(p):
    return clean(dict(enumerate(map(Q, p))))


def plus(p, q):
    charge()
    r = p.copy()
    for i, a in q.items():
        r[i] = r.get(i, Q(0))+a
    return clean(r)


def times(p, q):
    charge()
    r = {}
    for i, a in p.items():
        for j, b in q.items():
            r[i+j] = r.get(i+j, Q(0))+a*b
    return clean(r)


def value(p, x):
    charge()
    # Direct powers rather than the producer's Horner evaluation.
    r = sum((a*x**i for i, a in p.items()), Q(0))
    clean({0: r})
    return r


def replay_roots(record):
    coefficients = record['primitive_coefficients']
    all_divisors = []
    for idx, side in enumerate(['numerator_divisors', 'denominator_divisors']):
        entry = record[side]
        n = abs(coefficients[0 if idx == 0 else -1])
        check('divisor_input', entry['integer'] == n)
        expected, trials = set(), []
        for d in range(1, isqrt(n)+1):
            charge('divisor_trials')
            charge()
            residual = n % d
            trials.append([d, residual])
            if residual == 0:
                expected.update([d, n//d])
        check('entire_divisor_certificate', entry == dict(
            integer=n, trials=trials, divisors=sorted(expected)))
        all_divisors.append(expected)
    p = dense(coefficients)
    expected = {}
    for a in all_divisors[0]:
        for b in all_divisors[1]:
            for sign in [1, -1]:
                charge()
                if gcd(a, b) == 1:
                    r = Q(sign*a, b)
                    expected[r] = value(p, r)
    actual = {Q(row['candidate']): Q(row['residual']) for row in record['candidates']}
    check('all_reduced_candidates_and_residuals', len(actual) == len(record['candidates'])
          and actual == expected)
    roots = sorted(r for r, v in expected.items() if v == 0)
    check('complete_rational_root_list', roots == list(map(Q, record['roots'])))
    return roots


try:
    c = json.loads(CERT.read_text())
    charge(n=nodes(c))  # All input certificate nodes processed by this replay.
    # Account for the five full selected-pointer inspections already performed.
    prior = [c['affine_chart']['proportionality_equations'],
             c['affine_chart']['bezout_coefficients'],
             c['quartic_rational_root_certificate'],
             c['affine_chart']['rational_root_certificate'],
             c['projective_infinity_chart']]
    inspection_nodes = sum(nodes(v) for v in prior)
    charge(n=inspection_nodes)
    run['prior_selected_inspection_nodes'] = inspection_nodes
    check('complete_status', c['status'] == 'COMPLETE_NO_EXTRA_Q_INVOLUTION'
          and not c['failures'] and all(v['ok'] for v in c['checks']))
    for name, digest in c['source_hashes'].items():
        check('input_hash', hashlib.sha256((ROOT/name).read_bytes()).hexdigest() == digest)
    check('quartic_branch_prerequisite', replay_roots(c['quartic_rational_root_certificate']) == [])
    f = [-308, -2288, 341, 3388, 1034, -704, -275]
    check('full_exact_twist', times(dense([-4, 0, 1]), dense([77, 572, -66, -704, -275])) == dense(f))
    ac = c['affine_chart']
    g = list(map(dense, ac['transformed_sextic_coefficients']))
    check('seven_binary_coefficients_degree_at_most_six', len(g) == 7
          and all(max(p, default=0) <= 6 for p in g))
    # Seven independent parameter values certify every degree-at-most-six
    # coefficient polynomial. Direct integer binary expansion is used here.
    for r in range(7):
        expected = [0]*7
        for i, a in enumerate(f):
            for j in range(7):
                for p in range(max(0, j-(6-i)), min(i, j)+1):
                    charge()  # A binary coefficient term/check.
                    q = j-p
                    expected[j] += a*comb(i, p)*r**p*(-4)**(i-p) \
                        *comb(6-i, q)*(-r)**(6-i-q)
        check('binary_identity_parameter_'+str(r), [value(p, Q(r)) for p in g] == expected)
    eqs = list(map(dense, ac['proportionality_equations']))
    for j, e in enumerate(eqs, 1):
        check('full_coefficient_equation_'+str(j), e == plus(
            times(dense([f[0]]), g[j]), times(dense([-f[j]]), g[0])))
    h = dense(ac['monic_gcd'])
    check('gcd_is_singular_factor', h == dense([-4, 0, 1]))
    total = {}
    for e, w, quotient in zip(eqs, ac['bezout_coefficients'], ac['exact_quotients']):
        total = plus(total, times(e, dense(w)))
        check('gcd_divides_equation', times(h, dense(quotient)) == e)
    check('full_bezout_identity', total == h)
    check('root_exhaustion', replay_roots(ac['rational_root_certificate']) == [Q(-2), Q(2)])
    for r, exception in zip([-2, 2], c['singular_exceptions']):
        coefficients = [value(p, Q(r)) for p in g]
        lam = Q(exception['sextic_multiplier'])
        check('entire_singular_exception', Q(exception['r']) == r
              and Q(exception['determinant']) == 0
              and Q(exception['square_matrix_scalar']) == 0
              and list(map(Q, exception['full_coefficients'])) == coefficients
              and coefficients == [lam*a for a in f])
    check('exactly_two_singular_exceptions', len(c['singular_exceptions']) == 2)
    inf = c['projective_infinity_chart']
    expected = [a*(-1)**j for j, a in enumerate(f)]
    check('infinity_chart_full_failure', inf['matrix'] == [[1, 0], [0, -1]]
          and inf['full_coefficients'] == expected
          and Q(inf['forced_multiplier']) == 1
          and list(map(Q, inf['proportionality_residual'])) == [a-b for a, b in zip(expected, f)]
          and any(a != b for a, b in zip(expected, f)))
    check('no_survivors', c['nonsingular_survivors'] == [])
    weights = ac['bezout_coefficients']
    denom = lcm(*(Q(a).denominator for p in weights for a in p))
    integer_weights = [[int(Q(a)*denom) for a in p] for p in weights]
    charge(n=sum(len(p) for p in weights))
    report = dict(status='VERIFIED_EXACT_CERTIFICATE', checks=checks, failures=[],
        certificate_sha256=hashlib.sha256(CERT.read_bytes()).hexdigest(),
        producer_sha256=hashlib.sha256((BASE/'involution_eligibility.py').read_bytes()).hexdigest(),
        integer_bezout=dict(multiplier=denom, coefficients=integer_weights),
        max_degree=max_degree, max_bits=max_bits, caps=caps)
    charge(n=nodes(report))
    run.update(status=report['status'], end=ledger['used'].copy())
    report['cumulative_charged_usage'] = ledger['used'].copy()
    charge(n=nodes(report['cumulative_charged_usage']))
    report['cumulative_charged_usage'] = ledger['used'].copy()
    run['end'] = ledger['used'].copy()
    OUT.write_text(json.dumps(report, indent=2)+'\n')
except Exception as exc:
    run.update(status='REPLAY_INCOMPLETE', error=str(exc), end=ledger['used'].copy())
    OUT.write_text(json.dumps(dict(status=run['status'], error=str(exc), checks=checks), indent=2)+'\n')
    raise
finally:
    LEDGER.write_text(json.dumps(ledger, indent=2)+'\n')

print('Result:', report['status'], '; checks:', len(checks), '; failures: []')
print('Cumulative actual/required bounds:', ledger['used'], '/', caps)
print('Replay max degree/bits:', max_degree, max_bits)
print('Evidence:', OUT.relative_to(ROOT), '; ledger:', LEDGER.relative_to(ROOT))
