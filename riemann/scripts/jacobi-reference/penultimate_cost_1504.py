"""One finite actual-coefficient test; no degree/parameter sweep.

Reuse only L778's audited entire evaluator and its complete complex error.
All new arithmetic is exact integer/Fraction interval arithmetic, rounded
outwards to a fixed decimal grid. No transcendental call is made here.
"""
import hashlib
import json
import math
import platform
from fractions import Fraction as F
from pathlib import Path

BASE = Path(__file__).resolve().parent
ROOT = BASE.parent.parent
OUT = BASE / 'penultimate-cost-1504.json'
GRID = 10**100


def down(x):
    return F((x.numerator * GRID) // x.denominator, GRID)


def up(x):
    return -down(-x)


def decimal(x):
    n = x * GRID
    assert n.denominator == 1
    sign = '-' if n < 0 else ''
    a, b = divmod(abs(n.numerator), GRID)
    return sign + str(a) + '.' + str(b).zfill(100)


class I:
    def __init__(self, lo=0, hi=None):
        lo = F(lo)
        hi = lo if hi is None else F(hi)
        assert lo <= hi
        self.lo, self.hi = down(lo), up(hi)

    def __add__(self, y):
        y = interval(y)
        return I(self.lo + y.lo, self.hi + y.hi)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, y):
        return self + -interval(y)

    def __rsub__(self, y):
        return interval(y) + -self

    def __mul__(self, y):
        y = interval(y)
        products = [a*b for a in (self.lo, self.hi)
                    for b in (y.lo, y.hi)]
        return I(min(products), max(products))

    __rmul__ = __mul__

    def __truediv__(self, y):
        y = interval(y)
        assert y.lo > 0 or y.hi < 0, 'division interval contains zero'
        return self * I(1/y.hi, 1/y.lo)

    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        out = I(1)
        for _ in range(n):
            out = out * self
        return out

    def pair(self):
        return [decimal(self.lo), decimal(self.hi)]


def interval(x):
    return x if isinstance(x, I) else I(x)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def determinant(matrix):
    """Complete signed Leibniz sum by subset dynamic programming.

    A state sums all assignments of its selected columns to the first
    len(mask) rows. Appending column j adds one inversion for each
    previously selected column greater than j. No pivot/division occurs.
    """
    n = len(matrix)
    dp = {0: I(1)}
    for mask in range(1 << n):
        row = mask.bit_count()
        if row == n:
            continue
        for j in range(n):
            if mask & (1 << j):
                continue
            sign = (-1) ** (mask >> (j + 1)).bit_count()
            nxt = mask | (1 << j)
            dp[nxt] = dp.get(nxt, I(0)) + sign * dp[mask] * matrix[row][j]
    return dp[(1 << n)-1], {str(k): v.pair() for k, v in dp.items()}


def main():
    source = ROOT / 'scripts/actual-fredholm/fixed-pair-certificate-431.json'
    audit = ROOT / 'scripts/actual-fredholm/audit-433/audit-report.json'
    replay = ROOT / 'scripts/actual-fredholm/audit-433/fixed-pair-certificate-431.json'
    files = (source, audit, replay)
    hashes = {str(p.relative_to(ROOT)): sha(p) for p in files}
    report = dict(step=1504, status='INCOMPLETE', failures=[], checks=[],
                  arithmetic='Exact Fraction with outward rounding to 10^-100',
                  python=platform.python_version(), program_sha256=sha(Path(__file__)),
                  input_hashes=hashes,
                  scope='Actual first six coefficients and one Sylvester determinant; no degree sweep; inherited L778 contracts apply')

    def check(name, passed):
        report['checks'].append(dict(name=name, passed=bool(passed)))
        if not passed:
            raise AssertionError(name)

    try:
        ev = json.loads(source.read_text())['evaluation']
        prior = json.loads(audit.read_text())
        check('L778 audited source hash unchanged', sha(source) == prior['original_sha256'])
        check('L778 audit passed', prior['status'] == 'PASS' and not prior['failures'])
        check('entire evaluator equals audited replay', ev == json.loads(replay.read_text())['evaluation'])
        check('complex disk radius 1600', ev['uniform_disk_radius'] == 1600)
        elo, ehi = map(F, ev['uniform_G_error'])
        check('complete analytic error less than 3.141e-48', 0 < elo <= ehi < F('3.141e-48'))
        coeff = ev['coefficients'][:6]
        check('six actual coefficient enclosures available', len(coeff) == 6)
        aa, errors = [], []
        for j, pair in enumerate(coeff):
            eps = ehi / 1600**j
            errors.append(I(0, eps))
            aa.append(I(*pair) + I(-eps, eps))
            check('actual G coefficient positive ' + str(j), aa[-1].lo > 0)
        ff = [I(1)] + [(4**j)*aa[j]/aa[0] for j in range(1, 6)]
        logs = [I(0)]
        for n in range(1, 6):
            logs.append(ff[n] - sum((k*logs[k]*ff[n-k] for k in range(1, n)), I(0))/n)
        sums = [I(0)] + [((-1)**(n+1))*n*logs[n] for n in range(1, 6)]
        v, t, q, h = sums[2:6]
        for n in range(2, 6):
            check('actual S_' + str(n) + ' positive', sums[n].lo > 0)
        feasibility = (F(9, 10)*v)**3 - t**2
        check('explicit matching feasibility margin positive', feasibility.lo > 0)
        sigma = F(1, 200)
        T, Q, H = t/(sigma**3), q/(sigma**4), h/(sigma**5)
        # Descending coefficients. Rows represent X^2 E, X E, E,
        # X^5 J, ..., J, in the basis X^8, ..., 1.
        E = [I(1), I(0), I(0), -8*T, 9*Q, I(0), -2*T**2]
        J = [T, -3*Q, 3*H, -T**2]
        matrix = []
        for offset in range(3):
            matrix.append([I(0)]*offset + E + [I(0)]*(2-offset))
        for offset in range(6):
            matrix.append([I(0)]*offset + J + [I(0)]*(5-offset))
        det, states = determinant(matrix)
        report.update(source_P0_coefficients=coeff,
                      uniform_G_error=ev['uniform_G_error'],
                      cauchy_error_bounds=[a.pair() for a in errors],
                      actual_G_coefficients=[a.pair() for a in aa],
                      F_ordinary_coefficients=[f.pair() for f in ff],
                      actual_b=[(math.factorial(j)*ff[j]).pair() for j in range(6)],
                      logarithm_coefficients=[a.pair() for a in logs[1:]],
                      reciprocal_sums={str(n): sums[n].pair() for n in range(1, 6)},
                      feasibility_margin=feasibility.pair(),
                      scale='1/200', normalized_sums=dict(T=T.pair(), Q=Q.pair(), H=H.pair()),
                      E_descending=[a.pair() for a in E], J_descending=[a.pair() for a in J],
                      sylvester_matrix=[[a.pair() for a in row] for row in matrix],
                      determinant_states=states, determinant=det.pair())
        check('Sylvester determinant excludes zero', det.lo > 0 or det.hi < 0)
        for path in files:
            check('input unchanged: ' + str(path.relative_to(ROOT)), sha(path) == hashes[str(path.relative_to(ROOT))])
        report['status'] = 'MATCHING_FEASIBLE_AND_RETAINED_COST_OBSTRUCTED'
    except Exception as exc:
        report['status'] = 'FAILED'
        report['failures'].append(type(exc).__name__ + ': ' + str(exc))
    OUT.write_text(json.dumps(report, indent=2) + '\n')
    print('Result:', report['status'])
    for label in ('feasibility_margin', 'determinant'):
        if label in report:
            lo, hi = map(F, report[label])
            print(label + ' (display only):', f'[{float(lo):.12g}, {float(hi):.12g}]')
    print('Required: feasibility margin > 0; determinant excludes 0; uniform compactness argument is in C028c.')
    print('Failures:', report['failures'])
    print('Full certificate:', OUT.relative_to(ROOT))
    return 0 if report['status'] != 'FAILED' else 1


if __name__ == '__main__':
    raise SystemExit(main())
