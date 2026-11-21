"""Independent bounded audit of L824; no new evaluator or degree sweep.

Replays step624 into a separate directory. Independently uses rational
intervals on a 10^-90 outward grid, companion-matrix traces, Laplace
determinants and symmetric elimination. Original evidence is read-only.
"""
from fractions import Fraction as F
import contextlib
import hashlib
import importlib.util
import io
from itertools import combinations
import json
import math
from pathlib import Path

BASE = Path(__file__).resolve().parent
ROOT = BASE.parent.parent
OUT = BASE / 'audit-626'
SCALE = 10**90
checks, failures = [], []


class B:
    def __init__(self, lo=0, hi=None):
        self.lo, self.hi = F(lo), F(lo if hi is None else hi)
        assert self.lo <= self.hi

    @staticmethod
    def rounded(lo, hi):
        return B(F(math.floor(lo*SCALE), SCALE),
                 F(math.ceil(hi*SCALE), SCALE))

    def __add__(self, other):
        other = box(other)
        return B.rounded(self.lo+other.lo, self.hi+other.hi)

    __radd__ = __add__

    def __neg__(self):
        return B(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-box(other))

    def __rsub__(self, other):
        return box(other) + (-self)

    def __mul__(self, other):
        other = box(other)
        # Midpoint/radius enclosure, independent of endpoint-product code.
        m, r = (self.lo+self.hi)/2, (self.hi-self.lo)/2
        n, s = (other.lo+other.hi)/2, (other.hi-other.lo)/2
        radius = abs(m)*s + abs(n)*r + r*s
        return B.rounded(m*n-radius, m*n+radius)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = box(other)
        assert other.lo > 0 or other.hi < 0
        return self * B.rounded(1/other.hi, 1/other.lo)

    def pair(self):
        return [str(self.lo), str(self.hi)]

    def display(self):
        def fmt(n):
            return ('-' if n < 0 else '') + str(abs(n)//10**6) + '.' + str(abs(n)%10**6).zfill(6)
        return [fmt(math.floor(self.lo*10**6)), fmt(math.ceil(self.hi*10**6))]

    def contains(self, other):
        return self.lo <= other.lo and other.hi <= self.hi


def box(x):
    return x if isinstance(x, B) else B(x)


def check(name, value):
    checks.append(dict(name=name, passed=bool(value)))
    if not value:
        failures.append(name)


def read(path):
    return json.loads((ROOT/path).read_text())


def sha(path):
    return hashlib.sha256((ROOT/path).read_bytes()).hexdigest()


def matmul(a, b):
    return [[sum((a[i][k]*b[k][j] for k in range(4)), B())
             for j in range(4)] for i in range(4)]


def laplace(a):
    if len(a) == 1:
        return a[0][0]
    return sum((((-1)**j)*a[0][j]*laplace(
        [[row[k] for k in range(len(a)) if k != j] for row in a[1:]])
        for j in reversed(range(len(a)))), B())


def run():
    OUT.mkdir(exist_ok=True)
    original_path = 'scripts/central-jacobi/quartic-free-square-root-certificate-624.json'
    script_path = 'scripts/central-jacobi/quartic_free_square_root_624.py'
    saved = read(original_path)
    source_path = 'scripts/actual-fredholm/fixed-pair-certificate-431.json'
    model_path = 'scripts/central-jacobi/fixed-model-certificate-476.json'
    audit478_path = 'scripts/central-jacobi/audit-478/audit-report.json'
    audit433_path = 'scripts/actual-fredholm/audit-433/audit-report.json'
    replay433_path = 'scripts/actual-fredholm/audit-433/fixed-pair-certificate-431.json'
    first_script = 'scripts/central-jacobi/quartic-624/first-pass.py'
    first_cert = 'scripts/central-jacobi/quartic-624/first-pass.json'
    paths = [original_path, script_path, source_path, model_path,
             audit478_path, audit433_path, replay433_path, first_script, first_cert]
    hashes = {p: sha(p) for p in paths}
    audit478, audit433 = read(audit478_path), read(audit433_path)
    source, model = read(source_path)['evaluation'], read(model_path)
    for label, record in [('step624', saved), ('step478', audit478), ('step433', audit433)]:
        outcomes = (all(isinstance(v, str) and v for v in record['checks'])
                    if label == 'step433' else all(v['passed'] for v in record['checks']))
        check(label+' status and all recorded checks', record['status'] == 'PASS'
              and not record['failures'] and bool(record['checks']) and outcomes)
    for path, value in audit478['original_hashes'].items():
        check('step478 original hash '+path, sha(path) == value)
    check('step624 script hash', hashes[script_path] == saved['script_sha256'])
    check('step624 source hash records', saved['audited_hashes'] == saved['current_hashes']
          == audit478['original_hashes'])
    check('source hash shared by L791 and step433',
          hashes[source_path] == model['source_sha256'] == audit433['original_sha256'])
    check('complete inherited evaluator replay equality', source == read(replay433_path)['evaluation'])
    check('uniform disk radius', source['uniform_disk_radius'] == 1600)
    eg = B(*source['uniform_G_error'])
    check('retained uniform error', source['uniform_G_error'] == model['uniform_G_error']
          and 0 < eg.lo <= eg.hi < F('3.141e-48'))
    input_rows, gamma = [], []
    for j in range(5):
        coeff = B(*source['coefficients'][j])
        error = eg.hi/F(1600**j)
        # Exact unrounded endpoint addition for the inherited input check.
        actual = B(coeff.lo-error, coeff.hi+error)
        aa, gg = B(*model['actual_a'][j]), B(*model['gamma'][j])
        scale = 8*4**j*math.factorial(j)
        normal = B(scale*aa.lo, scale*aa.hi)
        check('actual_a contains full analytic error '+str(j), aa.contains(actual))
        check('gamma normalization '+str(j), gg.contains(normal) and gg.lo > 0)
        row = saved['input_evidence'][j]
        check('saved input evidence '+str(j), row == dict(j=j,
              polynomial_coefficient=coeff.pair(), analytic_error=str(error),
              recomputed_actual_a=actual.pair(), actual_a=aa.pair(), gamma=gg.pair()))
        input_rows.append(dict(j=j, analytic_error=str(error), actual_a=aa.pair(),
                               gamma=gg.pair(), recomputed_actual_a=actual.pair()))
        gamma.append(gg)
    check('preserved first-pass status and single failure',
          read(first_cert)['status'] == 'FAIL' and read(first_cert)['failures']
          == ['Newton recurrence encloses closed form 6'])
    if failures:
        report = dict(status='INVALID_INPUT', checks=checks, failures=failures,
                      original_hashes=hashes, input_evidence=input_rows)
    else:
        # Full replay into a separate path, without overwriting source artifacts.
        spec = importlib.util.spec_from_file_location('quartic624_replay', ROOT/script_path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        mod.OUT = OUT/'quartic-free-square-root-replay-624.json'
        with contextlib.redirect_stdout(io.StringIO()):
            mod.run()
        check('entire step624 replay exact equality', json.loads(mod.OUT.read_text()) == saved)

        # Recompute using a different centering order: h*(A-3h^2) etc.
        h = gamma[3]/gamma[4]
        a, b, d = 6*gamma[2]/gamma[4], -4*gamma[1]/gamma[4], gamma[0]/gamma[4]
        p = a-6*h*h
        q = b+2*h*(a-4*h*h)
        r = d+h*(b+h*(a-3*h*h))
        c, e, f = p/2, q/2, (r-p*p/24)/2
        factor = dict(c=c, e=e, f=f)
        for key, value in factor.items():
            check('independent coefficient agrees with stated decimal '+key,
                  B(*saved['outward_decimal_bounds']['factor_'+key]).contains(value))

        # Companion matrix charpoly is t^4+c*t^2+e*t+f. No root inputs.
        companion = [[B(0), B(0), B(0), -f],
                     [B(1), B(0), B(0), -e],
                     [B(0), B(1), B(0), -c],
                     [B(0), B(0), B(1), B(0)]]
        power = [[B(int(i == j)) for j in range(4)] for i in range(4)]
        sums = []
        powers = []
        for k in range(7):
            sums.append(sum((power[i][i] for i in reversed(range(4))), B()))
            powers.append([[v.pair() for v in row] for row in power])
            if k < 6:
                power = matmul(power, companion)
        hermite = [[sums[i+j] for j in range(4)] for i in range(4)]
        minors = {}
        for order in range(1, 5):
            for ix in combinations(range(4), order):
                v = laplace([[hermite[i][j] for j in ix] for i in ix])
                name = ','.join(map(str, ix))
                minors[name] = dict(exact_bounds=v.pair(), outward_bounds=v.display(),
                                    leading=ix == tuple(range(order)), required='0',
                                    strictly_positive=v.lo > 0)
                check('independent positive principal minor '+name, v.lo > 0)
        # A second sufficient sign test: interval symmetric Schur elimination.
        remainder = hermite
        pivots, cumulative = [], B(1)
        for k in range(4):
            pivot = remainder[0][0]
            check('positive elimination pivot '+str(k), pivot.lo > 0)
            cumulative = cumulative*pivot
            pivots.append(dict(pivot=pivot.pair(), outward_pivot=pivot.display(),
                               cumulative_leading_bound=cumulative.pair(), required='0'))
            remainder = [[remainder[i][j]-remainder[i][0]*remainder[0][j]/pivot
                          for j in range(1, len(remainder))]
                         for i in range(1, len(remainder))]
        for path in paths:
            check('original artifact preserved '+path, sha(path) == hashes[path])
        report = dict(status='PASS' if not failures else 'FAIL',
                      classification='REPRODUCTION: independent finite audit only',
                      inherited_contract='L791/step478 and L778/step433; complex analytic and trusted backend contracts unchanged',
                      grid_denominator=str(SCALE), arithmetic='exact rational midpoint/radius with outward grid after operations',
                      original_hashes=hashes, input_evidence=input_rows,
                      factor={k:v.pair() for k,v in factor.items()},
                      companion_powers=powers, newton_sums=[v.pair() for v in sums],
                      hermite_matrix=[[v.pair() for v in row] for row in hermite],
                      principal_minors=minors, elimination_pivots=pivots,
                      required='all four leading lower bounds > 0; achieved all 15 principal lower bounds > 0 and all elimination pivots > 0',
                      checks=checks, failures=failures,
                      replay_path=str(mod.OUT.relative_to(ROOT)),
                      limitations='No independent backend attestation, degree-uniform realization, shifted/mixed signs or RH assertion')
    report['script_sha256'] = sha('scripts/central-jacobi/audit_626.py')
    path = OUT/'audit-report.json'
    path.write_text(json.dumps(report, indent=2)+'\n')
    print('status:', report['status'], 'checks:', len(checks), 'failures:', failures)
    for name, value in report.get('principal_minors', {}).items():
        if value['leading']:
            print('leading minor', name, value['outward_bounds'], 'required lower > 0')
    for k, value in enumerate(report.get('elimination_pivots', [])):
        print('elimination pivot', k, value['outward_pivot'], 'required lower > 0')
    print('complete evidence:', path.relative_to(ROOT))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    run()
