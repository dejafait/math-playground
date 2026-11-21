"""One approved d=3 additive self-convolution test; no new quadrature.

All interval endpoints and operations are exact fractions.  L791's
audited transcendental/analytic input remains a premise, not rederived.
The complete evidence is written beside this script; stdout is bounded.
"""
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = Path(__file__).resolve().parent
OUT = BASE / 'cubic-free-square-root-certificate-622.json'


class I:
    def __init__(self, lo, hi=None):
        self.lo, self.hi = F(lo), F(lo if hi is None else hi)
        assert self.lo <= self.hi

    def __add__(self, other):
        other = interval(other)
        return I(self.lo + other.lo, self.hi + other.hi)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-interval(other))

    def __rsub__(self, other):
        return interval(other) + (-self)

    def __mul__(self, other):
        other = interval(other)
        products = [a*b for a in (self.lo, self.hi)
                    for b in (other.lo, other.hi)]
        return I(min(products), max(products))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = interval(other)
        assert other.lo > 0 or other.hi < 0, 'zero denominator'
        return self * I(1/other.hi, 1/other.lo)

    def square(self):
        return I(0 if self.lo <= 0 <= self.hi else
                 min(self.lo**2, self.hi**2),
                 max(self.lo**2, self.hi**2))

    def contains(self, other):
        return self.lo <= other.lo <= other.hi <= self.hi

    def pair(self):
        return [str(self.lo), str(self.hi)]

    def decimal_pair(self, places=6):
        scale = 10**places
        low = (self.lo*scale).__floor__()
        high = (self.hi*scale).__ceil__()

        def display(n):
            return ('-' if n < 0 else '') + str(abs(n)//scale) + '.' + \
                str(abs(n) % scale).zfill(places)

        return [display(low), display(high)]


def interval(x):
    return x if isinstance(x, I) else I(x)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


checks, failures = [], []


def check(name, passed):
    checks.append({'name': name, 'passed': bool(passed)})
    if not passed:
        failures.append(name)


def load(relative):
    return json.loads((ROOT / relative).read_text())


def run():
    data = load('scripts/central-jacobi/fixed-model-certificate-476.json')
    audit = load('scripts/central-jacobi/audit-478/audit-report.json')
    source_path = 'scripts/actual-fredholm/fixed-pair-certificate-431.json'
    source = load(source_path)['evaluation']
    audit433 = load('scripts/actual-fredholm/audit-433/audit-report.json')
    replay433 = load('scripts/actual-fredholm/audit-433/fixed-pair-certificate-431.json')
    check('step478 PASS, no failures', audit['status'] == 'PASS' and
          not audit['failures'] and all(v['passed'] for v in audit['checks']))
    current_hashes = {}
    for path, sha in audit['original_hashes'].items():
        current_hashes[path] = digest(ROOT / path)
        check('unchanged audited input: ' + path, current_hashes[path] == sha)
    check('source hash equals L791', current_hashes[source_path] == data['source_sha256'])
    check('source hash equals L778 audit', current_hashes[source_path] == audit433['original_sha256'])
    check('L778 audit PASS, no failures', audit433['status'] == 'PASS' and not audit433['failures'])
    check('complete evaluator equals audited L778 replay', source == replay433['evaluation'])
    check('uniform complex radius 1600', source['uniform_disk_radius'] == 1600)
    eg = I(*source['uniform_G_error'])
    check('uniform analytic error within stated bound', 0 < eg.lo <= eg.hi < F('3.141e-48'))
    check('uniform error unchanged', data['uniform_G_error'] == source['uniform_G_error'])
    input_evidence = []
    gamma = []
    for j in range(4):
        coefficient = I(*source['coefficients'][j])
        error = eg.hi / 1600**j
        recomputed = coefficient + I(-error, error)
        a = I(*data['actual_a'][j])
        g = I(*data['gamma'][j])
        check('actual_a enclosure ' + str(j), a.contains(recomputed))
        check('gamma normalization enclosure ' + str(j),
              g.contains(a * (8 * 4**j * math.factorial(j))))
        check('gamma positive ' + str(j), g.lo > 0)
        input_evidence.append(dict(j=j, polynomial_coefficient=coefficient.pair(),
                                   analytic_error=str(error),
                                   recomputed_actual_a=recomputed.pair(),
                                   actual_a=a.pair(), gamma=g.pair()))
        gamma.append(g)
    relevant_names = ('inherited', 'prior', 'complex', 'error', 'actual_a', 'gamma')
    prior_checks = [v for v in audit['checks']
                    if v['name'].startswith(relevant_names)]
    report = dict(scope='Centered monic actual-theta P_3; unique monic symmetric additive square root',
                  arithmetic='Exact Python integer/Fraction interval endpoints and operations; no floating point',
                  inherited_contract='L778 complex analytic error and trusted Decimal evaluator contracts; step478 coefficient audit',
                  prior_status=audit['status'], prior_input_checks=prior_checks,
                  audited_hashes=audit['original_hashes'], current_hashes=current_hashes,
                  input_evidence=input_evidence, checks=checks, failures=failures)
    if failures:
        report.update(status='INVALID_INPUT', result='INCONCLUSIVE')
    else:
        # Ratios cancel gamma(0) exactly; avoid needless interval widening.
        h = gamma[2] / gamma[3]
        a = 3 * gamma[1] / gamma[3]
        b = -gamma[0] / gamma[3]
        p = a - 3*h.square()
        q = -2*h*h.square() + a*h + b
        c, e = p/2, q/2
        delta = -4*c*c.square() - 27*e.square()
        check('monic leading divisor R3 nonzero', gamma[3].lo > 0)
        bounds = dict(h=h, monic_x_coefficient=a, monic_constant=b,
                      centered_p=p, centered_q=q, factor_c=c, factor_e=e,
                      discriminant=delta)
        # Separately check the printed coarse enclosures; no float conversion.
        displays = {key: value.decimal_pair() for key, value in bounds.items()}
        for key, value in bounds.items():
            check('outward display ' + key, I(*displays[key]).contains(value))
        result = ('THREE_DISTINCT_REAL_ROOTS' if delta.lo > 0 else
                  'ONE_REAL_TWO_NONREAL' if delta.hi < 0 else 'INCONCLUSIVE')
        report.update(status='PASS' if not failures else 'FAIL', result=result,
                      exact_bounds={k: v.pair() for k, v in bounds.items()},
                      outward_decimal_bounds=displays,
                      required_discriminant_threshold='0',
                      exact_identity='For C=y^3+p*y+q, Q=y^3+(p/2)*y+q/2 satisfies Q boxplus_3 Q=C; uniqueness proved in L823',
                      unresolved='No degree-uniform realization, shifted/mixed transfer or RH conclusion')
    report['script_sha256'] = digest(Path(__file__))
    OUT.write_text(json.dumps(report, indent=2) + '\n')
    print('status:', report['status'], 'result:', report['result'])
    if 'outward_decimal_bounds' in report:
        for key in ('centered_p', 'centered_q', 'factor_c', 'factor_e', 'discriminant'):
            print(key + ':', report['outward_decimal_bounds'][key])
    print('required discriminant threshold: 0; input/implementation failures:', failures)
    print('full certificate:', OUT.relative_to(ROOT))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    run()
