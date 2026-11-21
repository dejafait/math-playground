"""One approved six-moment Stieltjes test, with exact rational enclosures.

No new theta evaluator: consume L778's audited P_0 coefficients and retain
its analytic error. All new arithmetic uses Python integers/Fraction.
"""
import hashlib
import itertools
import json
import math
import platform
from fractions import Fraction as F
from pathlib import Path

BASE = Path(__file__).resolve().parent
ROOT = BASE.parent.parent
OUT = BASE / 'six-moment-certificate-639.json'
SCALE = 10**90


def floor_grid(x):
    return F((x.numerator*SCALE)//x.denominator, SCALE)


def ceil_grid(x):
    return -floor_grid(-x)


def dec(x):
    """Exact finite-decimal rendering of a grid endpoint, no rounding."""
    n = x*SCALE
    assert n.denominator == 1
    n = n.numerator
    sign = '-' if n < 0 else ''
    whole, frac = divmod(abs(n), SCALE)
    return sign+str(whole)+'.'+str(frac).zfill(90)


class Q:
    def __init__(self, lo=0, hi=None):
        lo, hi = F(lo), F(lo if hi is None else hi)
        assert lo <= hi
        self.lo, self.hi = floor_grid(lo), ceil_grid(hi)

    def __add__(self, other):
        other = q(other)
        return Q(self.lo+other.lo, self.hi+other.hi)

    __radd__ = __add__

    def __neg__(self):
        return Q(-self.hi, -self.lo)

    def __sub__(self, other):
        return self+-q(other)

    def __mul__(self, other):
        other = q(other)
        vals = [a*b for a in (self.lo, self.hi)
                for b in (other.lo, other.hi)]
        return Q(min(vals), max(vals))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = q(other)
        assert other.lo > 0 or other.hi < 0, 'denominator includes zero'
        return self*Q(1/other.hi, 1/other.lo)

    def pair(self):
        return [dec(self.lo), dec(self.hi)]


def q(x):
    return x if isinstance(x, Q) else Q(x)


def determinant(a):
    """Full Leibniz expansion for size at most three, no divisions."""
    n = len(a)
    total = Q(0)
    for p in itertools.permutations(range(n)):
        inversions = sum(p[i] > p[j] for i in range(n) for j in range(i+1, n))
        term = Q((-1)**inversions)
        for i in range(n):
            term = term*a[i][p[i]]
        total = total+term
    return total


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    source = ROOT/'scripts/actual-fredholm/fixed-pair-certificate-431.json'
    audit = ROOT/'scripts/actual-fredholm/audit-433/audit-report.json'
    replay = ROOT/'scripts/actual-fredholm/audit-433/fixed-pair-certificate-431.json'
    model = ROOT/'scripts/central-jacobi/fixed-model-certificate-476.json'
    files = (source, audit, replay, model)
    hashes = {str(p.relative_to(ROOT)): digest(p) for p in files}
    report = dict(step=639, status='INCOMPLETE', failures=[], checks=[],
                  scope='Only s_0,...,s_5; no all-degree or Xi-sign conclusion',
                  arithmetic='Exact Fraction; outward rounding to 10^-90 after each operation',
                  python=platform.python_version(), input_hashes=hashes,
                  program_sha256=digest(Path(__file__)))

    def check(name, passed):
        report['checks'].append(dict(name=name, passed=bool(passed)))
        if not passed:
            report['failures'].append(name)
            raise AssertionError(name)

    try:
        ev = json.loads(source.read_text())['evaluation']
        old_audit = json.loads(audit.read_text())
        check('source matches recorded L778 audit hash', digest(source) == old_audit['original_sha256'])
        check('source matches recorded L791 hash', digest(source) == json.loads(model.read_text())['source_sha256'])
        check('prior L778 audit passed', old_audit['status'] == 'PASS' and not old_audit['failures'])
        check('full evaluator matches audited replay', ev == json.loads(replay.read_text())['evaluation'])
        check('complex disk radius is 1600', ev['uniform_disk_radius'] == 1600)
        e_lo, e_hi = map(F, ev['uniform_G_error'])
        check('analytic error positive and below 3.141e-48', 0 < e_lo <= e_hi < F('3.141e-48'))
        check('at least six polynomial coefficients', len(ev['coefficients']) >= 6)
        report['source_P0_coefficients'] = ev['coefficients'][:6]
        report['source_uniform_G_error'] = ev['uniform_G_error']
        report['coefficient_rule'] = 'P0[j] + [-E_G_upper/1600^j, E_G_upper/1600^j]'
        cauchy, aa, gg = [], [], []
        for j, pair in enumerate(ev['coefficients'][:6]):
            eps = e_hi/F(1600**j)
            cauchy.append(Q(0, eps).pair())
            a = Q(*pair)+Q(-eps, eps)
            check('actual a_'+str(j)+' strictly positive', a.lo > 0)
            aa.append(a)
            gg.append(a*(8*4**j*math.factorial(j)))
        ss = [Q(1)]+[gg[0]/gg[j] for j in range(1, 6)]
        report['cauchy_error_upper_enclosures'] = cauchy
        report['actual_a'] = [a.pair() for a in aa]
        report['gamma'] = [g.pair() for g in gg]
        report['s'] = [s.pair() for s in ss]
        matrices, minors, pd = {}, {}, {}
        for shift in (0, 1):
            name = 'H'+str(shift)
            h = [[ss[i+j+shift] for j in range(3)] for i in range(3)]
            matrices[name] = [[v.pair() for v in row] for row in h]
            leading = [determinant([row[:k] for row in h[:k]]) for k in (1, 2, 3)]
            minors[name] = [v.pair() for v in leading]
            pd[name] = all(v.lo > 0 for v in leading)
        report['matrices'] = matrices
        report['leading_principal_minors'] = minors
        report['positive_definite'] = pd
        if all(pd.values()):
            report['status'] = 'FINITE_STIELTJES_FEASIBLE'
            report['range_condition'] = dict(verified=True, reason='H0 positive definite, hence invertible; range is R^3', vector=[ss[j].pair() for j in (3, 4, 5)])
        elif any(F(pair[1]) < 0 for vals in minors.values() for pair in vals):
            report['status'] = 'NEGATIVE_PRINCIPAL_MINOR'
        else:
            report['status'] = 'INCONCLUSIVE_NO_SINGULARITY_INFERRED'
        for path in files:
            check('input unchanged: '+str(path.relative_to(ROOT)), digest(path) == hashes[str(path.relative_to(ROOT))])
    except Exception as exc:
        report['status'] = 'FAILED'
        report['failures'].append(type(exc).__name__+': '+str(exc))
    OUT.write_text(json.dumps(report, indent=2)+'\n')
    print('Result:', report['status'])
    print('Required: all three leading minors of each symmetric matrix strictly > 0 for the PD branch')
    for name, vals in report.get('leading_principal_minors', {}).items():
        for k, pair in enumerate(vals, 1):
            # Coarse exact-decimal display; the complete 90-place intervals are on disk.
            lo, hi = map(F, pair)
            unit = 10**6
            a = F((lo*unit).__floor__(), unit)
            b = F((hi*unit).__ceil__(), unit)
            print(name, 'leading minor', k, ':', str(a), '<= actual <=', str(b), '; required > 0')
    print('Failures:', report['failures'])
    print('Certificate:', OUT.relative_to(ROOT))
    if report['status'] == 'FAILED':
        raise SystemExit(1)


if __name__ == '__main__':
    main()
