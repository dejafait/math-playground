"""Exact-rational evidence replay; does not independently verify Decimal.exp or jets."""
import hashlib
import json
import re
from fractions import Fraction as Q
from math import factorial
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = Path(__file__).with_name('normalized-row-energy-mean-109.json')
OUT = Path(__file__).with_suffix('.json')


class R:
    def __init__(self, a, b=None):
        self.lo, self.hi = Q(a), Q(a if b is None else b)
        assert self.lo <= self.hi

    @staticmethod
    def load(data):
        return R(data['lower'], data['upper'])

    def __add__(self, other):
        return R(self.lo+other.lo, self.hi+other.hi)

    def __neg__(self):
        return R(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        values = [a*b for a in (self.lo,self.hi) for b in (other.lo,other.hi)]
        return R(min(values),max(values))

    def __truediv__(self, other):
        assert not other.lo <= 0 <= other.hi
        return self * R(1/other.hi,1/other.lo)

    def data(self):
        return {'lower':str(self.lo),'upper':str(self.hi)}


def total(values):
    out = R(0)
    for value in values:
        out = out + value
    return out


def product(values):
    out = R(1)
    for value in values:
        out = out * value
    return out


def contained(exact, data):
    outer = R.load(data)
    assert outer.lo <= exact.lo <= exact.hi <= outer.hi


def negative_exp(x):
    partial, term = Q(1), Q(1)
    for n in range(1,1001):
        term *= x/n
        partial += term
    remainder = term*x/1001 / (1-x/1002)
    assert 0 <= x/1002 < 1
    return R(1/(partial+remainder),1/partial)


def main():
    d = json.loads(SOURCE.read_text())
    for path, expected in d['inputs'].items():
        assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest() == expected
    assert d['budget'] == {'precision':100,'spatial_panels':64,'cutoff':2,'theta_terms':4,'taylor_order':8}
    assert len(d['panels']) == 64
    coefficient = sum((Q(factorial(9),factorial(9-j))*Q(50**(9-j),3**(j+1))
                       for j in range(10)),Q(0))
    assert str(coefficient) == d['tails']['spatial_coefficient']
    spatial = R(128*coefficient) * negative_exp(Q(150))
    theta = R(29030400000) * negative_exp(Q(74))
    for key,value in [('spatial',spatial),('theta',theta),('total',spatial+theta)]:
        contained(value,d['tails'][key])
    tail = R.load(d['tails']['total'])
    assert 0 < tail.hi < Q('2.114e-22')
    moments = {}
    for k in range(0,15,2):
        finite, errors = R(0), R(0)
        for p, panel in enumerate(d['panels']):
            assert panel['index'] == p
            assert R.load(panel['center']).lo == R.load(panel['center']).hi == Q(2*p+1,64)
            assert R.load(panel['domain']).lo == Q(2*p,64)
            assert R.load(panel['domain']).hi == Q(2*p+2,64)
            row = panel['orders'][str(k)]
            coefficients = row['midpoint_even_coefficients']
            poly = total(R.load(coefficients[str(j)])*R(Q(2,(j+1)*64**(j+1)))
                         for j in (0,2,4,6))
            contained(poly,row['polynomial_integral'])
            eighth = R.load(row['eighth_coefficient'])
            error = R(max(abs(eighth.lo),abs(eighth.hi))*Q(2,9*64**9))
            contained(error,row['error'])
            # Match the producer's outward error before summation.
            stored_error = R.load(row['error'])
            integral = R.load(row['polynomial_integral'])+R(-stored_error.hi,stored_error.hi)
            contained(integral,row['integral'])
            finite = finite + R.load(row['integral'])
            errors = errors + stored_error
        contained(finite,d['finite_moments'][str(k)])
        contained(errors,d['quadrature_error_bounds'][str(k)])
        contained(R.load(d['finite_moments'][str(k)])+R(0,tail.hi),d['moments'][str(k)])
        moments[k] = R.load(d['moments'][str(k)])
        assert moments[k].lo > 0
    A = [moments[2*k]/R(factorial(2*k)) for k in range(7)]
    B = [moments[2*k+2]/R(factorial(2*k)) for k in range(7)]
    for k in range(7):
        contained(A[k],d['factor_masses'][str(k)])
        contained(B[k],d['factor_first_moments'][str(k)])
    canonical = [(int(c),tuple(map(int,a.split(',')))) for c,a in re.findall(
        r'^\| (-?\d+) \| \(([0-9,]+)\) \|$',
        (ROOT/'lemmas/L938-actual-h2-fixed-energy-density-and-cell-test.md').read_text(),re.M)]
    assert len(canonical) == len(d['rows']) == 34
    masses, firsts = {'plus':R(0),'minus':R(0)}, {'plus':R(0),'minus':R(0)}
    for (c,alpha),row in zip(canonical,d['rows']):
        assert c == row['coefficient'] and alpha == tuple(row['alpha'])
        labels = [k for k,a in enumerate(alpha) for _ in range(a)]
        assert len(labels) == 12 and sum(labels) == 12
        mass = product(A[k] for k in labels)
        # Independent labelled-factor replacement: twelve terms, not seven
        # grouped powers; this checks multiplicity and shifted factorials.
        first = total(product(B[k] if i==j else A[k]
                              for i,k in enumerate(labels)) for j in range(12))
        contained(mass,row['mass'])
        contained(first,row['first_moment'])
        side = 'plus' if c>0 else 'minus'
        assert side == row['side']
        masses[side] = masses[side] + R(abs(c))*mass
        firsts[side] = firsts[side] + R(abs(c))*first
    for side in masses:
        contained(masses[side],d['masses'][side])
        contained(firsts[side],d['first_moments'][side])
        assert R.load(d['masses'][side]).lo > Q('6.33069e-25')
        assert R.load(d['masses'][side]).hi < Q('6.33070e-25')
    # Use the actual stored endpoints for the final operation replay.
    m = {k:R.load(v) for k,v in d['masses'].items()}
    b = {k:R.load(v) for k,v in d['first_moments'].items()}
    means = {s:b[s]/m[s] for s in m}
    for side in m:
        contained(means[side],d['means'][side])
    delta = R.load(d['means']['plus'])-R.load(d['means']['minus'])
    contained(delta,d['delta'])
    cross = b['plus']*m['minus']-b['minus']*m['plus']
    contained(cross,d['cross_numerator'])
    contained(R.load(d['cross_numerator'])/(m['plus']*m['minus']),d['cross_delta'])
    final = R.load(d['delta'])
    assert Q('-8.574e-7') < final.lo < 0 < final.hi < Q('8.576e-7')
    assert final.hi-final.lo > Q('1.714e-6')
    assert d['decision'] == 'inconclusive_stop' and not d['failures']
    for name,rounding in [('DOWN','ROUND_FLOOR'),('UP','ROUND_CEILING'),('NEAR','ROUND_HALF_EVEN')]:
        arithmetic = d['arithmetic'][name]
        assert arithmetic['precision'] == 100 and arithmetic['rounding'] == rounding
        assert all(arithmetic['traps'].values()) and not any(arithmetic['exceptional_flags'].values())
    out = {'status':'passed','failures':[], 'panels_checked':64, 'moments_checked':8,
           'rows_checked':34, 'labelled_first_moment_terms_checked':408,
           'rational_tail_bounds':{'spatial':spatial.data(),'theta':theta.data(),
                                   'total':(spatial+theta).data()},
           'checked_delta':d['delta'], 'decision':d['decision'],
           'certificate_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
           'scope':'complete saved panel integration and row arithmetic replay; jets and exp library not independently reimplemented'}
    OUT.write_text(json.dumps(out,indent=2)+'\n')
    print('passed:64 panels,8 moments,34 rows,408 labelled first-moment terms; failures=[]')
    print('required delta>=0; achieved enclosure contains zero; fixed test stops')
    print(f'certificate={OUT.relative_to(ROOT)}')


if __name__ == '__main__':
    main()
