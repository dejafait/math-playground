"""One fixed exact-rational interval inertia test; no evaluator replay or sweep."""
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

BASE = Path(__file__).resolve().parent
SOURCE = BASE / 'audit-439/independent-phase-certificate-437.json'
OUTPUT = BASE / 'taylor-index-certificate-444.json'


class Interval:
    def __init__(self, lo, hi=None):
        self.lo, self.hi = F(lo), F(lo if hi is None else hi)
        assert self.lo <= self.hi

    def __neg__(self):
        return Interval(-self.hi, -self.lo)

    def __add__(self, other):
        return Interval(self.lo + other.lo, self.hi + other.hi)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        ends = [x*y for x in (self.lo, self.hi) for y in (other.lo, other.hi)]
        return Interval(min(ends), max(ends))

    def __truediv__(self, other):
        assert other.lo > 0 or other.hi < 0, 'unpaid pivot denominator'
        return self * Interval(1/other.hi, 1/other.lo)

    def square(self):
        return Interval(0 if self.lo <= 0 <= self.hi else min(self.lo**2, self.hi**2),
                        max(self.lo**2, self.hi**2))

    def sign(self):
        return 1 if self.lo > 0 else -1 if self.hi < 0 else 0


def rational(x):
    return {'numerator': str(x.numerator), 'denominator': str(x.denominator)}


def outward(x, places=10):
    scale = 10**places
    low = (x.lo.numerator * scale) // x.lo.denominator
    high = -((-x.hi.numerator * scale) // x.hi.denominator)
    def fixed(n):
        sign = '-' if n < 0 else ''
        a = abs(n)
        return f'{sign}{a//scale}.{a%scale:0{places}d}'
    return [fixed(low), fixed(high)]


def record(x):
    return {'exact': [rational(x.lo), rational(x.hi)], 'outward_decimal': outward(x)}


def main():
    assert not OUTPUT.exists(), 'preserve prior certificate'
    report = {'step': 444, 'target': 'H_ij=-beta_(4+i+j), i,j=0..2',
              'source': str(SOURCE.relative_to(BASE.parent.parent)),
              'source_sha256': hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
              'scope': 'Fixed repaired coefficients only; no full certificate replay; inherited L779 contracts',
              'required_negative_index': 2, 'checks': [], 'failures': []}
    try:
        data = json.loads(SOURCE.read_text())
        s = data['signed']
        assert data['pair'] == [3, 2048] and data['failures'] == []
        assert s['N'] == 512 and s['L'] == 2048 and s['phase_index_rule'] == '(-j*n)%2048'
        assert s['sigma'] == ['1.125', '1.125']
        selected, beta = [], []
        for n in range(4, 9):
            j = n-1
            enc = Interval(*s['beta_enclosures'][j])
            re, im = [Interval(*p) for p in s['DFT_enclosures'][j]]
            alias = Interval(*s['DFT_alias_errors'][j])
            hat, eps = F(s['beta_hat'][j]), F(s['epsilon'][j])
            assert alias.lo >= 0 and eps >= 0
            # Recorded enclosures must include both directed DFT endpoints
            # widened by the COMPLETE alias upper bound, also in the imaginary part.
            assert enc.lo <= re.lo-alias.hi and enc.hi >= re.hi+alias.hi
            assert im.lo-alias.hi <= 0 <= im.hi+alias.hi
            assert enc.lo <= hat <= enc.hi
            assert eps >= max(hat-enc.lo, enc.hi-hat)
            # Widen to midpoint +/- saved epsilon: pay every saved entry error.
            complete = Interval(hat-eps, hat+eps)
            assert complete.lo <= enc.lo <= enc.hi <= complete.hi
            beta.append(complete)
            selected.append({'n': n, **{k: s[k][j] for k in
                            ('beta_enclosures', 'beta_hat', 'epsilon',
                             'DFT_enclosures', 'DFT_alias_errors')},
                             'used_interval': record(complete)})
        report['selected_inputs'] = selected
        report['checks'].append('All five complete rectangles, errors, alias transfers and real symmetry checked exactly')
        H = [[-beta[i+j] for j in range(3)] for i in range(3)]
        report['H'] = [[record(x) for x in row] for row in H]
        # Unpivoted congruence: eliminate row/column0, then row/column1.
        p0 = H[0][0]
        assert p0.sign() != 0
        q11 = H[1][1] - H[0][1].square()/p0
        q12 = H[1][2] - H[0][1]*H[0][2]/p0
        q22 = H[2][2] - H[0][2].square()/p0
        assert q11.sign() != 0
        p2 = q22 - q12.square()/q11
        pivots = [p0, q11, p2]
        assert all(x.sign() != 0 for x in pivots), 'unresolved pivot sign'
        report['first_schur_block'] = [[record(q11), record(q12)], [record(q12), record(q22)]]
        report['pivots'] = [record(x) for x in pivots]
        report['pivot_signs'] = [x.sign() for x in pivots]
        margins = [x.lo if x.sign() > 0 else -x.hi for x in pivots]
        report['pivot_distance_from_zero_lower'] = [rational(x) for x in margins]
        report['required_pivot_distance_from_zero'] = '0'
        inertia = {'positive': sum(x.sign() > 0 for x in pivots),
                   'negative': sum(x.sign() < 0 for x in pivots), 'zero': 0}
        report['inertia'] = inertia
        report['threshold_met'] = inertia['negative'] >= 2
        report['checks'].append('All pivot denominators avoid zero; interval Schur elimination and Sylvester inertia')
        report['status'] = 'EXCESS_INDEX' if report['threshold_met'] else 'NONDISCRIMINATING'
    except Exception as exc:
        report['status'] = 'UNRESOLVED'
        report['failures'].append({'type': type(exc).__name__, 'message': str(exc)})
    OUTPUT.write_text(json.dumps(report, indent=2) + '\n')
    print('status:', report['status'], 'inertia:', report.get('inertia'),
          'required n_- >=', report['required_negative_index'])
    for j, p in enumerate(report.get('pivots', [])):
        print('pivot', j, 'outward bounds:', p['outward_decimal'], 'required distance > 0')
    print('failures:', report['failures'])
    print('certificate:', OUTPUT.relative_to(BASE.parent.parent))
    if report['failures']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
