"""Certify the actual degree-144 Fourier table against the exact rule.

All enclosures use outward scale-10^180 integer arithmetic. NumPy proposes
root centers and generates the compared table; neither is trusted as an
enclosure. Complete root/weight and all-frequency evidence is saved.
"""
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

import numpy as np

import check_exact_fourier_quadrature as arithmetic
from check_continuum_pure_sectors import Integrals

# Configure the reused arithmetic in this process only; no source is changed.
S = arithmetic.S = 10**180
I = arithmetic.I
ZERO = arithmetic.ZERO = I(0)
ONE = arithmetic.ONE = I(S)
exp_negative = arithmetic.exp_negative
DEGREE = 144
TWO = I.rational(2)


def record(z):
    return {'lo': str(z.lo), 'hi': str(z.hi)}


def upper_display(q):
    # Exact upward decimal formatting, not binary64 rounding.
    places = 24
    a = -((-q.numerator * 10**places)//q.denominator)
    return f'{a//10**places}.{a%10**places:0{places}d}'


def legendre(z):
    prev, cur = ONE, z
    for j in range(2, DEGREE+1):
        prev, cur = cur, (I.rational(2*j-1)*z*cur-I.rational(j-1)*prev)/I.rational(j)
    return cur, prev


def sign_at(t):
    p, _ = legendre(I(t))
    if p.lo > 0:
        return 1
    if p.hi < 0:
        return -1
    raise ArithmeticError('Endpoint polynomial sign is unresolved')


def roots_and_weights():
    proposals, _ = np.polynomial.legendre.leggauss(DEGREE)
    rows, roots, weights = [], [], []
    radius = I.rational(F(1, 10**12)).hi
    for index, proposed in enumerate(proposals):
        c = I.rational(F(float(proposed)))
        lo, hi = c.lo-radius, c.hi+radius
        sl, sh = sign_at(lo), sign_at(hi)
        assert -S < lo < hi < S and sl != sh
        initial = {'lo': str(lo), 'hi': str(hi), 'sign_lo': sl, 'sign_hi': sh}
        while hi-lo > S//10**90:
            mid = (lo+hi)//2
            sm = sign_at(mid)
            if sm == sl:
                lo, sl = mid, sm
            else:
                hi, sh = mid, sm
        assert sign_at(lo) == sl and sign_at(hi) == sh and sl != sh
        z = I(lo, hi)
        p, pm = legendre(z)
        derivative = I.rational(DEGREE)*(pm-z*p)/(ONE-z*z)
        w = TWO/((ONE-z*z)*derivative*derivative)
        assert w.lo > 0
        if roots:
            assert roots[-1].hi < z.lo
        roots.append(z)
        weights.append(w)
        rows.append({'index': index, 'initial': initial, 'root': record(z),
                     'sign_lo': sl, 'sign_hi': sh, 'weight': record(w)})
    assert len(roots) == DEGREE
    return roots, weights, rows


def arctan_enclosure(q, count=80):
    total = sum(((-1)**j*q**(2*j+1)/F(2*j+1) for j in range(count)), F(0))
    next_term = (-1)**count*q**(2*count+1)/F(2*count+1)
    a, b = sorted((total, total+next_term))
    return I(I.rational(a).lo, I.rational(b).hi)


def sin_cos(angle):
    assert angle.lo >= 0
    reductions = 0
    while angle.hi > S//8:
        angle = angle/TWO
        reductions += 1
    square = angle*angle
    ct, st = ONE, angle
    c, s = ONE, angle
    for j in range(1, 31):
        ct = ct*square/I.rational((2*j-1)*(2*j))
        st = st*square/I.rational((2*j)*(2*j+1))
        c = c-ct if j % 2 else c+ct
        s = s-st if j % 2 else s+st
    cnext = ct*square/I.rational(61*62)
    snext = st*square/I.rational(62*63)
    # Alternating sums through positive terms j=30 are upper bounds.
    c, s = I((c-cnext).lo, c.hi), I((s-snext).lo, s.hi)
    for _ in range(reductions):
        c, s = c*c-s*s, TWO*s*c
    return s, c


def rho(z, transition):
    if not transition:
        return ONE
    square = z*z
    u, v = I.rational(9)-square, square-I.rational(F(25, 4))
    assert u.lo > 0 and v.lo > 0
    b1, b2 = exp_negative(ONE/u), exp_negative(ONE/v)
    return b1/(b1+b2)


def compare_component(actual, expected):
    difference = I.rational(F(float(actual)))-expected
    return difference.absolute_upper()


def main():
    pi = I.rational(16)*arctan_enclosure(F(1, 5))-I.rational(4)*arctan_enclosure(F(1, 239))
    omega = pi/I.rational(8)
    roots, weights, root_rows = roots_and_weights()
    panels, values = [], []
    for a, b in [(F(0), F(5, 2)), (F(5, 2), F(3))]:
        panel_rows = []
        for z, w in zip(roots, weights):
            x = I.rational((a+b)/2)+I.rational((b-a)/2)*z
            weight = I.rational((b-a)/2)*w
            cutoff = rho(x, a == F(5, 2))
            values.append((x, weight*cutoff))
            panel_rows.append({'x': record(x), 'weight': record(weight), 'rho': record(cutoff)})
        panels.append({'a': str(a), 'b': str(b), 'nodes': panel_rows})
    actual = Integrals((0, 2), 112, DEGREE)
    bounds = [F(0), F(0)]
    worst = [None, None]
    rows, failures = [], []
    margins = [F(593, 10**14), F(879, 10**14)]
    for n in range(225):
        even, odd = ZERO, ZERO
        for x, wrho in values:
            sine, cosine = sin_cos(I.rational(n)*omega*x)
            even = even+TWO*wrho*cosine
            odd = odd+TWO*wrho*x*sine
        for h in (0, 1):
            real, imag = (even, ZERO) if h == 0 else (ZERO, odd)
            for signed_n in ((0,) if n == 0 else (n, -n)):
                signed_imag = imag if signed_n >= 0 else -imag
                stored = actual.transforms[h][signed_n]
                error = compare_component(stored.real, real)+compare_component(stored.imag, signed_imag)
                if error > bounds[h]:
                    bounds[h], worst[h] = error, signed_n
                if error >= margins[h]:
                    failures.append({'h': h, 'n': signed_n, 'upper': upper_display(error)})
                rows.append({'h': h, 'n': signed_n,
                             'stored_real_hex': float(stored.real).hex(),
                             'stored_imag_hex': float(stored.imag).hex(),
                             'exact_rule_real': record(real), 'exact_rule_imag': record(signed_imag),
                             'error_upper': {'num': str(error.numerator), 'den': str(error.denominator)}})
    exact_quadrature = [F(7, 10**14), F(21, 10**14)]
    required = [F(6, 10**12), F(9, 10**12)]
    totals = [bounds[h]+exact_quadrature[h] for h in (0, 1)]
    assert len(rows) == 898
    source = Path(__file__).with_name('check_continuum_pure_sectors.py')
    data = {'status': 'PASS' if not failures else 'FAIL', 'scale': str(S),
            'degree': DEGREE, 'cutoff': 112, 'numpy_version': np.__version__,
            'integrals_source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
            'pi': record(pi), 'roots_and_weights': root_rows, 'positive_panels': panels,
            'transforms': rows, 'failure_count': len(failures), 'failures': failures,
            'bounds': [{'h': h, 'worst_n': worst[h], 'stored_minus_rule_upper': upper_display(bounds[h]),
                        'stored_margin_required': upper_display(margins[h]),
                        'total_with_L036_upper': upper_display(totals[h]),
                        'total_required': upper_display(required[h]),
                        'margin_pass': bounds[h] < margins[h], 'total_pass': totals[h] < required[h]}
                       for h in (0, 1)],
            'qualifications': ['Certifies this saved actual table; reruns must match its dyadic values or be rechecked.',
                               'L036 exact quadrature is a separate essential input.',
                               'No tensor sensitivity, tensor arithmetic, response sign or full Ward coefficient is enclosed.']}
    path = Path(__file__).with_name('stored-fourier-enclosure-certificate.json')
    path.write_text(json.dumps(data, indent=2)+'\n')
    print(json.dumps({'status': data['status'], 'roots': len(root_rows), 'transforms': len(rows),
                      'bounds': data['bounds'], 'failure_count': len(failures), 'path': str(path)}, indent=2))
    if failures or not all(totals[h] < required[h] for h in (0, 1)):
        raise SystemExit(1)


if __name__ == '__main__':
    main()
