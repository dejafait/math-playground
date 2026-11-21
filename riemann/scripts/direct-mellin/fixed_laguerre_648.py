"""One real-box certified diagnostic; see L829 for all analytic bounds.

Run from the active notebook: python3 scripts/direct-mellin/fixed_laguerre_648.py
Only stdlib: Decimal directed arithmetic + correctly rounded exp, expanded
by one neighboring number on either side. No binary floating arithmetic.
"""
import decimal
from decimal import Decimal as D
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import platform
import sys

BASE = Path(__file__).resolve().parent
ROOT = BASE.parent.parent
OUT = BASE / 'fixed-laguerre-certificate-648.json'
STAGES = ((40, 8192), (60, 131072))
LOW = HIGH = NEAR = None


def contexts(precision):
    global LOW, HIGH, NEAR
    LOW = decimal.Context(prec=precision, rounding=decimal.ROUND_FLOOR)
    HIGH = decimal.Context(prec=precision, rounding=decimal.ROUND_CEILING)
    NEAR = decimal.Context(prec=precision, rounding=decimal.ROUND_HALF_EVEN)
    for c in (LOW, HIGH, NEAR):
        for flag in (decimal.InvalidOperation, decimal.DivisionByZero,
                     decimal.Overflow, decimal.Underflow, decimal.Subnormal,
                     decimal.Clamped, decimal.FloatOperation):
            c.traps[flag] = True


class I:
    def __init__(self, lo, hi=None):
        self.lo, self.hi = D(lo), D(lo if hi is None else hi)
        assert self.lo.is_finite() and self.hi.is_finite()
        assert self.lo <= self.hi

    @classmethod
    def rational(cls, x):
        x = F(x)
        a, b = D(x.numerator), D(x.denominator)
        return cls(LOW.divide(a, b), HIGH.divide(a, b))

    def __add__(self, other):
        other = interval(other)
        return I(LOW.add(self.lo, other.lo), HIGH.add(self.hi, other.hi))

    __radd__ = __add__

    def __neg__(self):
        return I(self.hi.copy_negate(), self.lo.copy_negate())

    def __sub__(self, other):
        return self + -interval(other)

    def __mul__(self, other):
        other = interval(other)
        pairs = [(a, b) for a in (self.lo, self.hi)
                 for b in (other.lo, other.hi)]
        return I(min(LOW.multiply(a, b) for a, b in pairs),
                 max(HIGH.multiply(a, b) for a, b in pairs))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = interval(other)
        assert other.lo > 0 or other.hi < 0, 'division across zero'
        return self * I(LOW.divide(D(1), other.hi),
                        HIGH.divide(D(1), other.lo))

    def square(self):
        vals = (self.lo, self.hi)
        lo = D(0) if self.lo <= 0 <= self.hi else min(LOW.multiply(v, v) for v in vals)
        return I(lo, max(HIGH.multiply(v, v) for v in vals))

    def exp(self):
        a, b = NEAR.exp(self.lo), NEAR.exp(self.hi)
        return I(NEAR.next_minus(a), NEAR.next_plus(b))

    def pair(self):
        return [str(self.lo), str(self.hi)]


def interval(x):
    return x if isinstance(x, I) else I(x)


def pi_interval():
    def atan(q, terms):
        s = sum((F((-1)**k, (2*k+1)*q**(2*k+1)) for k in range(terms)), F(0))
        r = F((-1)**terms, (2*terms+1)*q**(2*terms+1))
        return I.rational(min(s, s+r)) + I(0, I.rational(abs(r)).hi)
    # For even terms the partial sum is a lower bound, so the preceding
    # general enclosure is [s,s+r]. Both choices below are even.
    return 16*atan(5, 80) - 4*atan(239, 30)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run_stage(precision, boxes, report):
    contexts(precision)
    stage = dict(precision=precision, boxes=boxes, status='INCOMPLETE', checks=[])
    report['stages'].append(stage)

    def check(name, ok):
        stage['checks'].append(dict(name=name, passed=bool(ok)))
        if not ok:
            raise AssertionError(name)

    pi = pi_interval()
    check('3 < pi and pi^2 < 10', pi.lo > 3 and pi.square().hi < 10)
    check('e > 2 and exp(4) > 54', I(1).exp().lo > 2 and I(4).exp().lo > 54)
    check('n>=2 ratio below one half',
          (I.rational(F(81,16))*I(-15).exp()).hi < D('0.5'))
    check('n=2 initial envelope below one half', (16*I(-9).exp()).hi < D('0.5'))
    check('omitted theta ratio below one half',
          (I.rational(F(6,5)) .square().square()*I(-33).exp()).hi < D('0.5'))
    check('omitted theta envelope decreasing', I.rational(F(9,2)).hi < 2*3*25)
    a = I(-20).exp()
    endpoint_c = (80*(I.rational(F(9,2))*a-3).exp()).hi
    endpoint_m = [(I(endpoint_c)*a*k).hi for k in (1,21,442)]
    endpoint = [I(0, endpoint_m[0]), I(endpoint_m[1].copy_negate(),0), I(0,endpoint_m[2])]
    theta_eps = (50000*I(-75).exp()).hi
    theta_errors = [(I(theta_eps)*21*I(1).exp()*20**j).hi for j in range(3)]
    tail_eps = I(-140).exp().hi
    check('tail reduction 80 exp(-151)/318 < exp(-140)',
          (80*I(-151).exp()/318).hi < I(-140).exp().lo)
    step = I.rational(F(21, boxes))
    check('dyadic quadrature width exact', step.lo == step.hi)
    totals = [I(0), I(0), I(0)]
    cells_path = BASE/f'fixed-laguerre-boxes-648-p{precision}-n{boxes}.jsonl.gz'
    block_sums = []
    block = [I(0),I(0),I(0)]
    with gzip.open(cells_path, 'wt', encoding='utf-8') as out:
        for k in range(boxes):
            left = I.rational(F(-20*boxes+21*k, boxes))
            right = I.rational(F(-20*boxes+21*(k+1), boxes))
            assert left.lo == left.hi and right.lo == right.hi
            t = I(left.lo, right.hi)
            x = t.exp()
            y = (2*x).exp()
            p4 = I(0)
            for n in range(1,5):
                v = pi*(n*n)*y
                assert v.lo > D('1.5')
                p4 = p4+2*v*(2*v-3)*(-v).exp()
            p4 = (x/2).exp()*p4
            f0 = x*p4
            ranges = [f0, t*f0, t.square()*f0]
            cells = [step*v for v in ranges]
            for j in range(3):
                totals[j] = totals[j]+cells[j]
                block[j] = block[j]+cells[j]
            out.write(json.dumps(dict(k=k,t=t.pair(),ranges=[v.pair() for v in ranges],
                                      integrals=[v.pair() for v in cells]),separators=(',',':'))+'\n')
            if (k+1) % 256 == 0:
                block_sums.append(dict(first=k-255,last=k,integrals=[v.pair() for v in block]))
                block = [I(0),I(0),I(0)]
    check('all prescribed cells enclosed', len(block_sums)*256 == boxes)
    stage['quadrature'] = dict(interval=[-20,1],width=step.pair(),
                               integral_enclosures=[v.pair() for v in totals],
                               block_sums=block_sums,
                               cells_path=str(cells_path.relative_to(ROOT)),
                               cells_sha256=digest(cells_path))
    stage['bounds'] = dict(pi=pi.pair(),a=a.pair(),endpoint_P_upper=str(endpoint_c),
                          endpoint_enclosures=[v.pair() for v in endpoint],
                          theta_pointwise_upper=str(theta_eps),
                          theta_integrated_absolute_uppers=list(map(str,theta_errors)),
                          infinite_tail_absolute_upper=str(tail_eps),
                          roundoff='All operations outward; exp half-even bracketed by neighbors; no untracked additive roundoff.')
    js = [totals[j]+endpoint[j]
          + I(theta_errors[j].copy_negate(),theta_errors[j])
          + I(tail_eps.copy_negate(),tail_eps) for j in range(3)]
    check('J0 strictly positive', js[0].lo > 0)
    r1, r2 = js[1]/js[0], js[2]/js[0]
    variance = r2-r1.square()
    scalar = pi.square()/2-4*variance
    stage['evaluation'] = dict(J=[v.pair() for v in js],J1_over_J0=r1.pair(),
                               J2_over_J0=r2.pair(),log_variance=variance.pair(),
                               scalar=scalar.pair(),required_threshold='0',
                               decision=('NEGATIVE' if scalar.hi < 0 else
                                         'PASS_NECESSARY_ONLY' if scalar.lo >= 0 else 'INCONCLUSIVE'))
    stage['status'] = 'CERTIFIED_ENCLOSURE'
    return stage['evaluation']['decision']


def main():
    report = dict(step=648,status='INCOMPLETE',failures=[],stages=[],
                  scope='Only E prime(0)^2-E(0)E double-prime(0); no Xi sign conclusion',
                  declared_stages=[dict(precision=p,boxes=n) for p,n in STAGES],
                  python=sys.version,platform=platform.platform(),libmpdec=decimal.__libmpdec_version__,
                  arithmetic='Python Decimal Context directed arithmetic and expanded correctly rounded exp; exact Fraction Machin bounds',
                  backend_contract='https://docs.python.org/3/library/decimal.html#decimal.Decimal.exp',
                  program_sha256=digest(Path(__file__)),
                  input_sha256={p:digest(ROOT/p) for p in (
                      'lemmas/L828-abstract-fabry-complete-bernstein-obstruction.md',
                      'lemmas/C828a-actual-theta-complete-bernstein-exclusion.md',
                      'lemmas/L019-the-theta-boundary-derivative-and-a-positive-kernel.md',
                      'drafts/literature/2026-11-05-direct-mellin-fixed-laguerre-test.md')})
    try:
        for precision,boxes in STAGES:
            decision = run_stage(precision,boxes,report)
            OUT.write_text(json.dumps(report,indent=2)+'\n')
            print(json.dumps(dict(stage_precision=precision,boxes=boxes,
                                  **report['stages'][-1]['evaluation']),separators=(',',':')),flush=True)
            if decision != 'INCONCLUSIVE':
                break
        report['status'] = decision
    except Exception as exc:
        report['failures'].append(type(exc).__name__+': '+str(exc))
        raise
    finally:
        OUT.write_text(json.dumps(report,indent=2)+'\n')
        print('Certificate:',OUT.relative_to(ROOT),'status:',report['status'],
              'failures:',report['failures'],flush=True)


if __name__ == '__main__':
    main()
