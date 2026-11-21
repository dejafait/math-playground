"""Independent L823 audit; inherited analytic/backend contracts stay premises.

Uses functional rational intervals rounded outward on a 10^-100 grid,
and a different association of q and the discriminant from step622.
Original artifacts are read only. Full evidence is saved, stdout bounded.
"""
from fractions import Fraction as F
import hashlib
import json
from math import factorial
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).with_name('cubic-factor-audit-763.json')
SCALE = 10**100


def load(path):
    return json.loads((ROOT / path).read_text())


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def pair(values):
    lo, hi = map(F, values)
    assert lo <= hi
    return lo, hi


def point(value):
    return F(value), F(value)


def rounded(lo, hi):
    return F((lo*SCALE).__floor__(), SCALE), F((hi*SCALE).__ceil__(), SCALE)


def add(a, b):
    return rounded(a[0]+b[0], a[1]+b[1])


def neg(a):
    return -a[1], -a[0]


def mul(a, b):
    corners = [x*y for x in a for y in b]
    return rounded(min(corners), max(corners))


def div(a, b):
    assert b[0] > 0 or b[1] < 0
    return mul(a, rounded(1/b[1], 1/b[0]))


def power(a, n):
    assert n in (2, 3)
    if n == 3:
        return rounded(a[0]**3, a[1]**3)
    low = 0 if a[0] <= 0 <= a[1] else min(x*x for x in a)
    return rounded(low, max(x*x for x in a))


def contains(a, b):
    return a[0] <= b[0] <= b[1] <= a[1]


def encoded(a):
    return list(map(str, a))


def decimal_bound(a, places=6):
    scale = 10**places
    def text(n):
        return ('-' if n < 0 else '') + str(abs(n)//scale) + '.' + str(abs(n)%scale).zfill(places)
    return [text((a[0]*scale).__floor__()), text((a[1]*scale).__ceil__())]


def main():
    checks, failures = [], []
    def check(name, passed):
        checks.append(dict(name=name, passed=bool(passed)))
        if not passed:
            failures.append(name)

    source_path = 'scripts/actual-fredholm/fixed-pair-certificate-431.json'
    model_path = 'scripts/central-jacobi/fixed-model-certificate-476.json'
    cubic_path = 'scripts/central-jacobi/cubic-free-square-root-certificate-622.json'
    cubic_script = 'scripts/central-jacobi/cubic_free_square_root_622.py'
    audit478_path = 'scripts/central-jacobi/audit-478/audit-report.json'
    audit433_path = 'scripts/actual-fredholm/audit-433/audit-report.json'
    replay433_path = 'scripts/actual-fredholm/audit-433/fixed-pair-certificate-431.json'
    tracked = [source_path, model_path, cubic_path, cubic_script,
               audit478_path, audit433_path, replay433_path]
    before = {p: sha(p) for p in tracked}
    source = load(source_path)['evaluation']
    model, cubic = load(model_path), load(cubic_path)
    a478, a433 = load(audit478_path), load(audit433_path)
    for label, report in [('478', a478), ('433', a433), ('622', cubic)]:
        check('prior status/failures '+label, report['status'] == 'PASS' and not report['failures'])
    check('all step478 checks pass', all(c['passed'] for c in a478['checks']))
    check('all step622 checks pass', all(c['passed'] for c in cubic['checks']))
    for p, expected in a478['original_hashes'].items():
        check('step478 hash '+p, sha(p) == expected)
    check('source hash matches model and step433',
          before[source_path] == model['source_sha256'] == a433['original_sha256'])
    check('complete inherited evaluator equals audited replay',
          source == load(replay433_path)['evaluation'])
    check('step622 script hash', before[cubic_script] == cubic['script_sha256'])
    check('step622 current and audited hashes', cubic['current_hashes'] == cubic['audited_hashes'] == a478['original_hashes'])
    check('complex Cauchy radius exactly 1600', source['uniform_disk_radius'] == 1600)
    error = pair(source['uniform_G_error'])
    check('positive analytic error below 3.141e-48', 0 < error[0] <= error[1] < F('3.141e-48'))
    check('model retains analytic error', model['uniform_G_error'] == source['uniform_G_error'])

    inputs, gamma = [], []
    check('four complete step622 input records', len(cubic['input_evidence']) == 4)
    for j in range(4):
        coeff = pair(source['coefficients'][j])
        eps = error[1] / 1600**j
        # Exact operations for the inherited interval inclusion, no grid rounding.
        actual = coeff[0]-eps, coeff[1]+eps
        a, g = pair(model['actual_a'][j]), pair(model['gamma'][j])
        factor = 8*4**j*factorial(j)
        normalized = a[0]*factor, a[1]*factor
        check('coefficient plus complete analytic error '+str(j), contains(a, actual))
        check('factorial/radius normalization '+str(j), contains(g, normalized))
        check('strict gamma positivity '+str(j), g[0] > 0)
        record = dict(j=j, polynomial_coefficient=encoded(coeff), analytic_error=str(eps),
                      recomputed_actual_a=encoded(actual), actual_a=encoded(a), gamma=encoded(g))
        check('complete step622 evidence '+str(j), record == cubic['input_evidence'][j])
        inputs.append(record)
        gamma.append(g)

    bounds, displays = {}, {}
    if not failures:
        h = div(gamma[2], gamma[3])
        A = div(mul(point(3), gamma[1]), gamma[3])
        B = div(neg(gamma[0]), gamma[3])
        p = add(A, neg(mul(point(3), power(h, 2))))
        # Different association from the original -2h^3+A*h+B.
        q = add(B, mul(h, add(A, neg(mul(point(2), power(h, 2))))))
        c, e = div(p, point(2)), div(q, point(2))
        # Delta(Q)=-(2p^3+27q^2)/4. Cube is monotone, including negatives.
        delta = div(neg(add(mul(point(2), power(p, 3)), mul(point(27), power(q, 2)))), point(4))
        bounds = dict(h=h, monic_x_coefficient=A, monic_constant=B,
                      centered_p=p, centered_q=q, factor_c=c, factor_e=e,
                      discriminant=delta)
        displays = {k: decimal_bound(v) for k, v in bounds.items()}
        for k, value in bounds.items():
            check('original printed enclosure '+k, contains(pair(cubic['outward_decimal_bounds'][k]), value))
        check('original exact discriminant inside claimed decimal bound',
              contains(pair(['40491457.417703', '40491457.417704']), pair(cubic['exact_bounds']['discriminant'])))
        check('independent discriminant inside claimed decimal bound',
              contains(pair(['40491457.417703', '40491457.417704']), delta))
        check('strict discriminant lower bound', delta[0] > 0)
        check('coarse sign premises', c[1] < -216 and -53 < e[0] <= e[1] < 53)
        check('coarse discriminant arithmetic', 4*216**3-27*53**2 == 40234941 > 0)
    check('all original evidence preserved', before == {p: sha(p) for p in tracked})
    report = dict(status='PASS' if not failures else 'FAIL',
                  scope='Only L823 d=3 identity/normalization and finite discriminant audit',
                  arithmetic='Independent functional Fraction intervals; outward rounding on 10^-100 grid',
                  inherited_contract='L778 complex disk estimate and audited evaluator/software contracts; no binary attestation',
                  input_hashes=before, checks=checks, failures=failures,
                  input_evidence=inputs, exact_bounds={k: encoded(v) for k, v in bounds.items()},
                  outward_decimal_bounds=displays, required_discriminant_lower_bound='0',
                  coarse_certified_lower_bound='40234941',
                  alternative_formulas='q=B+h*(A-2*h^2); Delta=-(2*p^3+27*q^2)/4',
                  mathematical_review='Exact convolution identity and uniqueness checked in canonical L823 proof',
                  unresolved='Uniform factors, shifted/mixed signs and RH remain open')
    OUT.write_text(json.dumps(report, indent=2)+'\n')
    print('status:', report['status'], 'checks:', len(checks), 'failures:', failures)
    if displays:
        print('discriminant:', displays['discriminant'], '; required lower bound > 0')
        print('coarse certified lower bound: 40234941 > 0')
    print('full certificate:', OUT.relative_to(ROOT))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
