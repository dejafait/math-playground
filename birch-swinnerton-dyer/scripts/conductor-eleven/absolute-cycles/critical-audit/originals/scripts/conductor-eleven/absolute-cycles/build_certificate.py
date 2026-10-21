#!/usr/bin/env python3
"""Fixed full absolute lattice and independently signed period certificate.

Recovery inputs are L039 structural/dual evidence only. No twist value,
calibrated symbols, BSD, rank or Sha data is loaded. Source contract: L043.
"""
import json
from fractions import Fraction as F
from hashlib import sha256
from math import factorial, gcd, isqrt
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE.parent


def ceilq(x):
    return -((-x.numerator)//x.denominator)


class Interval:
    def __init__(self, bits):
        self.D = 1 << bits

    def out(self, lo, hi=None):
        if hi is None:
            hi = lo
        assert lo <= hi
        return [(lo*self.D).__floor__(), ceilq(hi*self.D)]

    def add(self, x, y):
        return [x[0]+y[0], x[1]+y[1]]

    def sub(self, x, y):
        return [x[0]-y[1], x[1]-y[0]]

    def mul(self, x, y):
        v = [a*b for a in x for b in y]
        return [min(v)//self.D, -((-max(v))//self.D)]

    def scale(self, x, a):
        return self.out(*sorted(F(a)*F(t, self.D) for t in x))

    def div(self, x, y):
        assert y[0] > 0
        v = [F(a, b) for a in x for b in y]
        return self.out(min(v), max(v))


def matmul(a, b):
    return [[sum(x*y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def prime(p):
    return p >= 2 and all(p % k for k in range(2, isqrt(p)+1))


def atan(inv, count):
    s = sum((F((-1)**k, (2*k+1)*inv**(2*k+1)) for k in range(count)), F(0))
    t = s+F((-1)**count, (2*count+1)*inv**(2*count+1))
    return sorted([s, t])


def exponential(x, count):
    assert 0 < x < 1
    s = sum(((-x)**k/F(factorial(k)) for k in range(count+1)), F(0))
    return sorted([s, s+(-x)**(count+1)/factorial(count+1)])


def cosine(c, j, pi, degree):
    if j == 0:
        return {'j': 0, 'interval': [c.D, c.D]}
    theta = sorted(2*F(j, 11)*F(t, c.D) for t in pi)
    mid = sum(theta)/2
    radius = (theta[1]-theta[0])/2
    s = sum((F((-1)**k)*mid**(2*k)/factorial(2*k)
             for k in range(degree+1)), F(0))
    # Taylor remainder of degree 2*degree+1 (odd coefficient is zero),
    # plus Lipschitz error |cos(theta)-cos(mid)| <= |theta-mid|.
    err = abs(mid)**(2*degree+2)/factorial(2*degree+2)+radius
    return {'j': j, 'theta': [str(t) for t in theta], 'midpoint': str(mid),
            'radius': str(radius), 'polynomial': str(s), 'error': str(err),
            'interval': c.out(s-err, s+err)}


def make():
    paths = [BASE/'structural-certificate.json', BASE/'dual-certificate.json',
             BASE/'arithmetic-input.json']
    structural, dual, arithmetic = [json.loads(p.read_text()) for p in paths]
    assert structural['inputs'] == {'N': 11, 'P': [2]}
    assert arithmetic['model'] == [0, -1, 1, -10, -20]
    p = structural['presentation']
    Pi, Q, K = [p[k]['entries'] for k in ('Pi', 'Q', 'K')]
    coords = p['generator_coordinates']
    # Full cusp-equivalence witnesses for every endpoint, Proposition 2.2.3(2).
    witnesses, boundary = [], []
    for pair in structural['endpoints']:
        saved, flags = [], []
        for numerator, denominator in pair:
            flag = int(denominator % 11 == 0)
            target_p, target_q = (1, 0) if flag else (0, 1)
            u = next(u for u in range(1, 11)
                     if (target_q-u*denominator) % 11 == 0
                     and (u*target_p-numerator) % gcd(denominator, 11) == 0)
            saved.append({'cusp': [numerator, denominator], 'class': flag, 'unit': u})
            flags.append(flag)
        witnesses.append(saved)
        boundary.append(flags[1]-flags[0])
    B = matmul([boundary], Q)[0]
    assert B == [0, 0, -1]
    T = [[0, 1, 0], [0, 0, 1], [-1, 0, 0]]
    Ti = [[0, 0, -1], [1, 0, 0], [0, 1, 0]]
    phi = list(map(F, dual['line']['v']))
    assert phi == [F(5, 2), F(5), F(1)]
    image = [phi[0], phi[1]]
    gen = F(gcd(5, 10), 2)
    raw = [0]*12
    raw[3] = -1
    cycle = [sum(row[i]*raw[i] for i in range(12)) for row in Pi]
    cycle_phi = sum(x*y for x, y in zip(phi, cycle))
    assert cycle == [0, -1, 0] and cycle_phi == -5
    bits, truncation, atan_count, exp_count, cos_degree = 48, 64, 32, 40, 24
    c = Interval(bits)
    ab = [atan(inv, atan_count) for inv in (5, 239)]
    pi_exact = [16*ab[0][0]-4*ab[1][1], 16*ab[0][1]-4*ab[1][0]]
    pi = c.out(*pi_exact)
    h = c.scale(pi, F(2, 11))
    ex = [exponential(F(t, c.D), exp_count) for t in h]
    rex = [ex[1][0], ex[0][1]]
    r = c.out(*rex)
    counts, aps = [], {}
    for ell in range(2, truncation+1):
        if not prime(ell):
            continue
        if ell == 2:
            row = {'p': ell, 'pairs': [[x, y] for x in range(ell) for y in range(ell)
                    if (y*y+y-x*x*x+x*x+10*x+20) % ell == 0]}
            count = len(row['pairs'])
        else:
            chars = []
            for x in range(ell):
                disc = (1+4*(x*x*x-x*x-10*x-20)) % ell
                t = pow(disc, (ell-1)//2, ell)
                chars.append(-1 if t == ell-1 else t)
            row = {'p': ell, 'characters': chars}
            count = ell+sum(chars)
        row.update({'affine': count, 'a_p': ell-count})
        counts.append(row)
        aps[ell] = ell-count
    assert aps[11] == 1
    coeffs, factors = [0, 1], []
    for n in range(2, truncation+1):
        rem, value, fs = n, 1, []
        for ell in aps:
            if rem % ell:
                continue
            k = 0
            while rem % ell == 0:
                rem //= ell
                k += 1
            powers = [1, aps[ell]]
            for _ in range(2, k+1):
                powers.append(aps[ell]*powers[-1]-(0 if ell == 11 else ell)*powers[-2])
            value *= powers[k]
            fs.append([ell, k, powers])
        assert rem == 1
        coeffs.append(value)
        factors.append([n, fs])
    cosines = [cosine(c, j, pi, cos_degree) for j in range(6)]

    def cos_residue(k):
        k %= 11
        return cosines[min(k, 11-k)]['interval']

    power, total, terms = [c.D, c.D], [0, 0], []
    for n in range(1, truncation+1):
        power = c.mul(power, r)
        # M=(-5,-1;11,2): cos(2pi*n*a/11)-cos(-2pi*n*d/11).
        diff = c.sub(cos_residue(-5*n), cos_residue(-2*n))
        term = c.scale(c.mul(power, diff), F(coeffs[n], n))
        total = c.add(total, term)
        terms.append({'n': n, 'power': power, 'difference': diff, 'term': term, 'partial': total})
    nxt = c.mul(power, r)
    tail = c.div(c.scale(nxt, 2), [c.D-r[1], c.D-r[0]])[1]
    period = [total[0]-tail, total[1]+tail]
    assert period[1] < 0  # actual orientation threshold; no guessed sign
    beta_sign = (-1 if period[1] < 0 else 1)*(-1 if cycle_phi < 0 else 1)
    assert beta_sign == 1 and cycle_phi < 0
    scale = F(beta_sign, 1)/(2*gen)
    values = [scale*sum(a*b for a, b in zip(phi, col)) for col in coords]
    common = 1
    for value in values:
        common = common*value.denominator//gcd(common, value.denominator)
    return {
        'schema': 'conductor-eleven-full-absolute-v1',
        'inputs': {p.name: sha256(p.read_bytes()).hexdigest() for p in paths},
        'source_scope': {'model': arithmetic['model'], 'N': 11, 'optimal_label': '11a1',
                         'absolute_Manin_constant': 1, 'components': 1,
                         'published_optimality_qualification': 'L040; complete isogeny class and two-period comparison'},
        'boundary': {'cusp_order': ['zero', 'infinity'], 'endpoint_witnesses': witnesses,
                     'raw_reduced': boundary, 'raw_full': [[-v for v in boundary], boundary],
                     'quotient_reduced': B, 'quotient_full': [[-v for v in B], B],
                     'source_images': matmul([boundary], list(map(list, zip(*structural['A']['entries'])))),
                     'saturated_images': matmul([boundary], K)},
        'kernel': {'unimodular_transform': T, 'inverse': Ti,
                   'boundary_after_transform': matmul([B], T),
                   'basis_columns': [[1, 0, 0], [0, 1, 0]],
                   'raw_basis_columns': [[row[0] for row in Q], [row[1] for row in Q]],
                   'functional_values': list(map(str, image)), 'common_denominator': 2,
                   'integer_values': [5, 10], 'gcd': 5, 'bezout': [1, 0],
                   'positive_image_generator': str(gen), 'primitive_values': ['1', '2']},
        'cycle': {'raw': raw, 'coordinates': cycle, 'phi': str(cycle_phi),
                  'path': [[0, 1], [-1, 2]], 'matrix': [-5, -1, 11, 2],
                  'alpha': ['-2/11', '1/11'], 'M_alpha': ['-5/11', '1/11']},
        'fourier': {'bits': bits, 'scale': c.D, 'T': truncation,
                    'atan_count': atan_count, 'atan_brackets': [[str(t) for t in row] for row in ab],
                    'pi_exact': list(map(str, pi_exact)), 'pi': pi, 'height': '1/11', 'h': h,
                    'exp_count': exp_count, 'exp_exact': list(map(str, rex)), 'r': r,
                    'cos_degree': cos_degree, 'cosines': cosines,
                    'point_counts': counts, 'coefficients': coeffs, 'factorizations': factors,
                    'terms': terms, 'next_power': nxt, 'tail_upper': tail, 'period_interval': period},
        'normalization': {'beta_sign': beta_sign, 'beta_over_total_period': str(scale),
                          'generator_values': list(map(str, values)), 'common_denominator': common,
                          'denominator_primes': [2, 5], 'C_for_p_ge_5_not_5': 0},
        'failures': []}


if __name__ == '__main__':
    data = make()
    out = HERE/'certificate.json'
    out.write_text(json.dumps(data, indent=2)+'\n')
    f, n = data['fourier'], data['normalization']
    print('Full boundary kernel rank 2/required 2; primitive image 5/2 Z')
    print('Oriented period interval:', f['period_interval'], '/', f['scale'], '; required upper < 0')
    print('Normalized scalar:', n['beta_over_total_period'], '; all 12 values denominator', n['common_denominator'])
    print('Failures:', data['failures'], '; certificate:', out)
