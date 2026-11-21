#!/usr/bin/env python3
"""Independent complete L961 audit; imports no original arithmetic code.

448-bit endpoint operations, longer series, interval-wide integer sieve,
literal triangular-matrix products and trailing Schur elimination.
Full evidence is saved; stdout is a compact summary. See L961 step146.
"""
from fractions import Fraction as F
from functools import lru_cache
from math import isqrt
from pathlib import Path
import hashlib
import json
import time

B = 448
UNIT = 1 << B
HERE = Path(__file__).resolve().parent
OLD = HERE / 'certificate-144.json'
OUT = HERE / 'audit-146.json'


def floor(q):
    return q.numerator // q.denominator


def ceil(q):
    return -floor(-q)


class I:
    def __init__(self, a=0, b=None):
        if isinstance(a, I) and b is None:
            self.a, self.b = a.a, a.b
        else:
            a = F(a)
            b = a if b is None else F(b)
            self.a, self.b = floor(a*UNIT), ceil(b*UNIT)
        assert self.a <= self.b

    @classmethod
    def raw(cls, a, b):
        return cls(F(a, UNIT), F(b, UNIT))

    def __add__(self, other):
        other = I(other)
        return I.raw(self.a+other.a, self.b+other.b)

    __radd__ = __add__

    def __neg__(self):
        return I.raw(-self.b, -self.a)

    def __sub__(self, other):
        return self + -I(other)

    def __rsub__(self, other):
        return I(other) + -self

    def __mul__(self, other):
        other = I(other)
        v = [F(x*y, UNIT) for x in (self.a, self.b)
             for y in (other.a, other.b)]
        return I.raw(floor(min(v)), ceil(max(v)))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = I(other)
        assert not other.a <= 0 <= other.b, 'zero-containing divisor'
        v = [F(x, y) for x in (self.a, self.b)
             for y in (other.a, other.b)]
        return I(min(v), max(v))

    def __rtruediv__(self, other):
        return I(other) / self

    def record(self):
        return {'lo': str(self.a), 'hi': str(self.b), 'bits': B}


@lru_cache(None)
def unitlog(q):
    q = F(q)
    assert 1 <= q <= 2
    z = I((q-1)/(q+1))
    square = z*z
    power, total = z, I(0)
    for j in range(190):
        total = total + power/(2*j+1)
        power = power*square
    tail = 2*power/(381*(1-square))
    return I.raw((2*total).a, (2*total+tail).b)


@lru_cache(None)
def logpoint(q):
    q = F(q)
    assert q > 0
    k = q.numerator.bit_length()-q.denominator.bit_length()
    m = q/F(2)**k
    if m < 1:
        k, m = k-1, 2*m
    assert 1 <= m < 2
    return unitlog(m)+k*unitlog(F(2))


def loginterval(v):
    v = I(v)
    assert v.a > 0
    return I.raw(logpoint(F(v.a, UNIT)).a, logpoint(F(v.b, UNIT)).b)


def exppoint(q):
    q = F(q)
    if q < 0:
        return 1/exppoint(-q)
    count = 0
    while q > F(1, 4):
        q /= 2
        count += 1
    z, term, total = I(q), I(1), I(1)
    for j in range(1, 128):
        term = term*z/j
        total = total+term
    omitted = term*z/128
    upper = total+omitted/(1-z/129)
    result = I.raw(total.a, upper.b)
    assert result.a > 0
    for _ in range(count):
        result = result*result
    return result


def expinterval(v):
    return I.raw(exppoint(F(v.a, UNIT)).a, exppoint(F(v.b, UNIT)).b)


def sqrtinterval(v):
    assert v.a >= 0
    a, b = isqrt(v.a*UNIT), isqrt(v.b*UNIT)
    return I.raw(a, b+int(b*b < v.b*UNIT))


def piinterval():
    def atan(q, length):
        partial = sum(((-1)**j*q**(2*j+1)/(2*j+1)
                       for j in range(length)), F(0))
        adjacent = partial+(-1)**length*q**(2*length+1)/(2*length+1)
        return I(min(partial, adjacent), max(partial, adjacent))
    return 16*atan(F(1, 5), 220)-4*atan(F(1, 239), 70)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    started = time.monotonic()
    old = json.loads(OLD.read_text())
    data = {'status': 'IN_PROGRESS', 'bits': B, 'failures': [], 'checks': [],
            'source_certificate_sha256': digest(OLD),
            'audit_script_sha256': digest(Path(__file__)),
            'series': {'log': 190, 'exp': 128, 'atan5': 220, 'atan239': 70},
            'required_pivot_lower': '0', 'stronger_pivot_lower': '67/100',
            'terms': [], 'pivots': [],
            'qualification': 'Independent arithmetic plus informal proof/code audit; not formal verification.'}

    def save():
        data['elapsed_seconds'] = time.monotonic()-started
        OUT.write_text(json.dumps(data, indent=2)+'\n')

    def need(test, name):
        data['checks'].append({'name': name, 'passed': bool(test)})
        if not test:
            data['failures'].append(name)

    def compare(v, stored, name):
        need(stored['bits'] == 320, name+' stored precision')
        lo, hi = int(stored['lo']), int(stored['hi'])
        need(lo <= hi and (lo << 128) <= v.a <= v.b <= (hi << 128),
             name+' fresh enclosure contained in stored enclosure')

    save()
    try:
        need(old['status'] == 'CLOSED_DISK_ZERO_FREE' and not old['failures'], 'original status')
        need(old['bits'] == 320, 'original precision')
        need(old['source_sha256'] == digest(HERE/'certify_144.py'), 'original source hash')
        need(old['helper_sha256'] == digest(HERE.parent/'centred-moment'/'audit_certificate_142.py'), 'original helper hash')
        need(old['inputs'] == {'t': '98/625', 'x': 6000000185827, 'primes': [2, 3, 5, 7]}, 'exact original inputs')
        t, x, pi = I(F(98, 625)), I(6000000185827), piinterval()
        r = x/(4*pi)+t/16
        nmax = 690988
        margins = [r-nmax*nmax, (nmax+1)*(nmax+1)-r]
        sigma_c = loginterval(sqrtinterval(1+x*x)/(4*pi))/4-1/(2*(1+x*x))
        sigma = F(1, 2)+t*sigma_c
        constants = {'pi': pi, 'radicand': r, 'c_pol': sigma_c, 'sigma': sigma}
        data['constants'] = {k: v.record() for k, v in constants.items()}
        for k, v in constants.items():
            compare(v, old['constants'][k], k)
        for name, v in zip(('natural_index_lower_strict', 'natural_index_upper_strict'), margins):
            need(v.a > 0, name)
            compare(v, old['gates'][name]['evidence'], name)
        data['natural_index_margins'] = [v.record() for v in margins]
        need(old['natural_index'] == nmax, 'original natural index')
        primes = (2, 3, 5, 7)
        support = []
        # Enumerate the integer interval, not the original recursive product tree.
        for n in range(1, nmax+1):
            residual, exponents = n, []
            for p in primes:
                e = 0
                while residual % p == 0:
                    residual //= p
                    e += 1
                exponents.append(e)
            if residual == 1:
                support.append((n, exponents))
        need(len(support) == len(old['terms']) == old['support_count'] == 1160, 'complete support count')
        need([(n, e, sum(e)) for n, e in support] ==
             [(v['n'], v['exponents'], v['omega']) for v in old['terms']], 'all support vectors and multiplicities')
        need(len({n for n, _ in support}) == 1160, 'unique support')
        need(2**19 <= nmax < 2**20, 'degree maximum and leading witness')
        need(old['degree'] == 19 and max(sum(e) for _, e in support) == 19, 'exact degree')
        logs = [logpoint(F(p)) for p in primes]
        data['prime_logs'] = [v.record() for v in logs]
        need(len(old['prime_logs']) == 4, 'all prime logarithms present')
        for j, v in enumerate(logs):
            compare(v, old['prime_logs'][j], f'log prime {j}')
        c = [I(0) for _ in range(20)]
        for j, (n, e) in enumerate(support):
            u = sum((e[k]*logs[k] for k in range(4)), I(0))
            weight = expinterval(t*u*u/4-sigma*u)
            need(weight.a > 0, f'positive weight {n}')
            compare(u, old['terms'][j]['log_n'], f'log n {n}')
            compare(weight, old['terms'][j]['a_n'], f'weight {n}')
            c[sum(e)] = c[sum(e)]+weight
            data['terms'].append({'n': n, 'exponents': e, 'omega': sum(e),
                                  'log_n': u.record(), 'a_n': weight.record()})
        need(len(old['coefficients']) == 20, 'all collected coefficients present')
        for j, v in enumerate(c):
            compare(v, old['coefficients'][j], f'coefficient {j}')
        need(c[0].a == c[0].b == UNIT and c[19].a > 0, 'nonzero constants and leading coefficients')
        data['coefficients'] = [v.record() for v in c]
        save()
        d = 19
        # Construct Q(S), Q#(S), then multiply transpose by matrix literally.
        forward = [[c[j-i] if j >= i else I(0) for j in range(d)] for i in range(d)]
        reverse = [[c[d-j+i] if j >= i else I(0) for j in range(d)] for i in range(d)]
        h = [[sum((forward[k][i]*forward[k][j]-reverse[k][i]*reverse[k][j]
                   for k in range(d)), I(0)) for j in range(d)] for i in range(d)]
        need(len(old['exterior_form']) == d and all(len(row) == d for row in old['exterior_form']), 'complete stored H dimensions')
        for i in range(d):
            for j in range(d):
                compare(h[i][j], old['exterior_form'][i][j], f'H {i} {j}')
                need(h[i][j].record() == h[j][i].record(), f'H symmetry {i} {j}')
        data['exterior_form'] = [[v.record() for v in row] for row in h]
        work = [row[:] for row in h]
        lower = [[I(int(i == j)) for j in range(d)] for i in range(d)]
        need(len(old['pivots']) == d, 'all stored pivots present')
        need(len(old['lower_factor']) == d and all(len(row) == d for row in old['lower_factor']), 'complete stored L dimensions')
        for j in range(d):
            pivot = work[j][j]
            need(pivot.a > 0, f'pivot {j} strictly positive')
            need(100*pivot.a > 67*UNIT, f'pivot {j} exceeds 67/100')
            need(100*int(old['pivots'][j]['lo']) > 67*(1 << 320), f'original pivot {j} exceeds 67/100')
            compare(pivot, old['pivots'][j], f'pivot {j}')
            data['pivots'].append(pivot.record())
            assert pivot.a > 0
            for i in range(j+1, d):
                lower[i][j] = work[i][j]/pivot
            for i in range(j+1, d):
                for k in range(j+1, d):
                    work[i][k] = work[i][k]-work[i][j]*work[j][k]/pivot
        for i in range(d):
            for j in range(d):
                compare(lower[i][j], old['lower_factor'][i][j], f'L {i} {j}')
        data['lower_factor'] = [[v.record() for v in row] for row in lower]
        # Every stored gate must be one of the complete expected predicates.
        expected = {'natural_index_lower_strict', 'natural_index_upper_strict',
                    'support_matches_independent_integer_sieve', 'support_no_duplicates',
                    'support_factorization', 'constant_exactly_one',
                    'nonconstant_degree_and_positive_leading',
                    'all_19_pivot_lower_bounds_above_67_over_100'}
        expected.update('positive_term_'+str(n) for n, _ in support)
        need(set(old['gates']) == expected, 'complete gate names')
        need(all(v['passed'] is True for v in old['gates'].values()), 'all original gates true')
        minimum = min(int(p['lo']) for p in data['pivots'])
        oldmin = min(int(p['lo']) for p in old['pivots'])
        need(old['minimum_pivot_lower_dyadic'] == str(oldmin), 'original minimum integer')
        need(F(old['minimum_pivot_lower_exact']) == F(oldmin, 1 << 320), 'original minimum rational')
        need(F(oldmin, 1 << 320) == F(359937399490813010351368583714034366515739341729221205346676966198400136077037846113184278859069,
             533996758980227520598755426542388028650676130589163192486760401955554931445160137505740521734144), 'canonical exact minimum rational')
        data['minimum_pivot_lower_exact'] = str(F(minimum, UNIT))
        data['minimum_pivot_index'] = min(range(d), key=lambda j: int(data['pivots'][j]['lo']))
        data['support_count'], data['degree'], data['natural_index'] = len(support), d, nmax
        data['status'] = 'AUDIT_PASS' if not data['failures'] else 'AUDIT_FAIL'
        save()
    except Exception as exc:
        data['exception'] = repr(exc)
        data['status'] = 'INCONCLUSIVE'
        save()
        raise
    print(json.dumps({'status': data['status'], 'checks': len(data['checks']),
                      'N': nmax, 'terms': len(support), 'degree': d,
                      'pivots_checked': len(data['pivots']),
                      'minimum_pivot_lower_display': float(F(minimum, UNIT)),
                      'actual_common_bound': '>67/100', 'required_common_bound': '>0',
                      'failures': data['failures'], 'certificate': str(OUT),
                      'seconds': data['elapsed_seconds']}, indent=2))
    if data['failures']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
