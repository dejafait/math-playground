"""One approved d=4 additive self-convolution test; no new quadrature.

All interval endpoints and operations are exact fractions.  L791's
audited transcendental/analytic input remains a premise, not rederived.
The complete evidence is written beside this script; stdout is bounded.
"""
from fractions import Fraction as F
import hashlib
import json
import math
from itertools import combinations, permutations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = Path(__file__).resolve().parent
OUT = BASE / 'quartic-free-square-root-certificate-624.json'


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
    for j in range(5):
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
    report = dict(scope='Centered monic actual-theta P_4; unique monic symmetric additive square root',
                  arithmetic='Exact Python integer/Fraction interval endpoints and operations; no floating point',
                  inherited_contract='L778 complex analytic error and trusted Decimal evaluator contracts; step478 coefficient audit',
                  prior_status=audit['status'], prior_input_checks=prior_checks,
                  audited_hashes=audit['original_hashes'], current_hashes=current_hashes,
                  input_evidence=input_evidence, checks=checks, failures=failures)
    if failures:
        report.update(status='INVALID_INPUT', result='INCONCLUSIVE')
    else:
        # Actual coefficient equations and identity are proved in L824.
        # Cancel gamma(0) algebraically before interval evaluation.
        h = gamma[3] / gamma[4]
        a = 6 * gamma[2] / gamma[4]
        b = -4 * gamma[1] / gamma[4]
        d = gamma[0] / gamma[4]
        p = a - 6*h.square()
        q = b + 2*a*h - 8*h*h.square()
        r = d + b*h + a*h.square() - 3*h.square().square()
        c, e, f = p/2, q/2, r/2-p.square()/48
        check('monic leading divisor R4 nonzero', gamma[4].lo > 0)
        bounds = dict(h=h, monic_x2=a, monic_x=b, monic_constant=d,
                      centered_p=p, centered_q=q, centered_r=r,
                      factor_c=c, factor_e=e, factor_f=f)

        # One outward rational enlargement at this boundary prevents
        # denominator growth. Subsequent Newton/determinant arithmetic is
        # exact on these intervals, whose endpoints have power-of-ten
        # denominators. This never replaces the raw factor enclosures.
        scale = 10**80
        def grid(x):
            return I(F((x.lo*scale).__floor__(), scale),
                     F((x.hi*scale).__ceil__(), scale))
        raw_factor = dict(c=c, e=e, f=f)
        factor = {key: grid(value) for key, value in raw_factor.items()}
        for key in factor:
            check('factor outward grid ' + key,
                  factor[key].contains(raw_factor[key]))
        c, e, f = (factor[key] for key in ('c', 'e', 'f'))

        # Newton identities for x^4+cx^2+ex+f, with multiplicities.
        # First compute all sums using the generic coefficient recurrence.
        coef = [I(1), I(0), c, e, f]
        sums = [I(4)]
        for k in range(1, 7):
            total = I(0)
            if k <= 4:
                for j in range(1, k):
                    total = total + coef[j]*sums[k-j]
                total = total + k*coef[k]
            else:
                for j in range(1, 5):
                    total = total + coef[j]*sums[k-j]
            sums.append(-total)
        # Closed forms independently check the generic recurrence's
        # enclosure at the interval level, without assuming real roots.
        closed = [I(4), I(0), -2*c, -3*e,
                  2*c.square()-4*f, 5*c*e,
                  -2*c*c.square()+6*c*f+3*e.square()]
        for k, value in enumerate(closed):
            check('Newton recurrence encloses closed form ' + str(k),
                  sums[k].contains(value))
        hermite = [[closed[i+j] for j in range(4)] for i in range(4)]

        def determinant(matrix):
            n = len(matrix)
            result = I(0)
            for perm in permutations(range(n)):
                inversions = sum(perm[i] > perm[j]
                                 for i in range(n) for j in range(i+1, n))
                term = I(-1 if inversions % 2 else 1)
                for i in range(n):
                    term = term * matrix[i][perm[i]]
                result = result + term
            return result

        minors = {}
        for n in range(1, 5):
            for indices in combinations(range(4), n):
                minor = determinant([[hermite[i][j] for j in indices]
                                     for i in indices])
                name = ','.join(map(str, indices))
                minors[name] = dict(indices=list(indices),
                                    leading=indices == tuple(range(n)),
                                    exact_bounds=minor.pair(),
                                    outward_decimal_bounds=minor.decimal_pair(),
                                    strictly_positive=minor.lo > 0,
                                    nonnegative=minor.lo >= 0,
                                    strictly_negative=minor.hi < 0)
                check('outward minor display ' + name,
                      I(*minors[name]['outward_decimal_bounds']).contains(minor))
        leading_positive = all(v['strictly_positive'] for v in minors.values()
                               if v['leading'])
        all_nonnegative = all(v['nonnegative'] for v in minors.values())
        negative = [name for name, value in minors.items()
                    if value['strictly_negative']]
        result = ('FOUR_DISTINCT_REAL_ROOTS' if leading_positive else
                  'ALL_ROOTS_REAL_WITH_MULTIPLICITIES' if all_nonnegative else
                  'NOT_REAL_ROOTED' if negative else 'INCONCLUSIVE')
        displays = {key: value.decimal_pair() for key, value in bounds.items()}
        for key, value in bounds.items():
            check('outward coefficient display ' + key,
                  I(*displays[key]).contains(value))
        # Record the complete imported degree-four convolution weight table.
        weights = {str(k): [dict(i=i, j=k-i,
                     weight=str(F(math.factorial(4-i)*math.factorial(4-k+i),
                                  math.factorial(4)*math.factorial(4-k))))
                    for i in range(k+1)] for k in range(5)}
        check('degree-four k2 cross weight', weights['2'][1]['weight'] == '3/4')
        check('degree-four k3 cross weights',
              weights['3'][1]['weight'] == weights['3'][2]['weight'] == '1/2')
        check('degree-four k4 cross weights',
              weights['4'][1]['weight'] == weights['4'][3]['weight'] == '1/4'
              and weights['4'][2]['weight'] == '1/6')
        report.update(status='PASS' if not failures else 'FAIL', result=result,
                      exact_bounds={k: v.pair() for k, v in bounds.items()},
                      outward_decimal_bounds=displays,
                      factor_grid={k: v.pair() for k, v in factor.items()},
                      grid_denominator=str(scale),
                      newton_sums=[v.pair() for v in closed],
                      generic_newton_sums=[v.pair() for v in sums],
                      hermite_matrix=[[v.pair() for v in row] for row in hermite],
                      principal_minors=minors, convolution_weights=weights,
                      criteria=dict(positive_leading_minors=leading_positive,
                                    all_principal_minors_nonnegative=all_nonnegative,
                                    negative_principal_minors=negative),
                      required_hermite_threshold='0 for every principal minor; strict leading minors suffice',
                      exact_identity='C=y^4+p*y^2+q*y+r; Q=y^4+(p/2)*y^2+(q/2)*y+r/2-p^2/48; uniqueness and exact identity in L824',
                      unresolved='No degree-uniform realization, shifted/mixed transfer or RH conclusion; separate audit pending')
    report['script_sha256'] = digest(Path(__file__))
    OUT.write_text(json.dumps(report, indent=2) + '\n')
    print('status:', report['status'], 'result:', report['result'])
    if 'outward_decimal_bounds' in report:
        for key in ('centered_p', 'centered_q', 'centered_r',
                    'factor_c', 'factor_e', 'factor_f'):
            print(key + ':', report['outward_decimal_bounds'][key])
        for name, value in report['principal_minors'].items():
            if value['leading']:
                print('leading minor ' + name + ':', value['outward_decimal_bounds'])
        print('negative principal minors:', report['criteria']['negative_principal_minors'])
    print('required minor threshold: 0; failures:', failures)
    print('full certificate:', OUT.relative_to(ROOT))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    run()
