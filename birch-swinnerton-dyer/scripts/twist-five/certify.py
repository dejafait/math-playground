#!/usr/bin/env python3
"""Fixed E/5 certificate. All load-bearing arithmetic is integer/Fraction.

The proof and imported arithmetic inputs are in L031. No L030 functional,
analytic/rational rank, BSD data, or external numerical package is read.
"""
import json
from fractions import Fraction as F
from hashlib import sha256
from math import gcd, isqrt
from pathlib import Path

HERE = Path(__file__).resolve().parent


def ceilq(x):
    return -((-x.numerator) // x.denominator)


class Dyadic:
    def __init__(self, bits):
        self.bits = bits
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
        products = [a*b for a in x for b in y]
        return [min(products)//self.D, -((-max(products))//self.D)]

    def scale(self, x, c):
        c = F(c)
        ends = sorted([F(x[0], self.D)*c, F(x[1], self.D)*c])
        return self.out(*ends)

    def div(self, x, y):
        assert y[0] > 0
        ends = [F(a, b) for a in x for b in y]
        return self.out(min(ends), max(ends))

    def sqrt(self, x):
        assert 0 <= x[0] <= x[1]
        low = isqrt(x[0]*self.D)
        high = isqrt(x[1]*self.D)
        if high*high < x[1]*self.D:
            high += 1
        assert low*low <= x[0]*self.D
        assert high*high >= x[1]*self.D
        return [low, high]


def atan_bracket(inv, count):
    # Adjacent alternating partial sums enclose atan(1/inv).
    s = sum((F((-1)**k, (2*k+1)*inv**(2*k+1))
             for k in range(count)), F(0))
    t = s + F((-1)**count, (2*count+1)*inv**(2*count+1))
    return [min(s, t), max(s, t)]


def exp_bracket(x, count):
    # Adjacent alternating sums enclose exp(-x), for 0 < x < 1.
    assert 0 < x < 1
    term, s = F(1), F(1)
    for k in range(1, count+1):
        term *= -x/k
        s += term
    t = s + term*(-x)/(count+1)
    return [min(s, t), max(s, t)]


def polynomial(x):
    return 4*x*x*x + 4*x*x - 8*x + 1


def root_bracket(c, lo, hi):
    lo, hi = int(lo*c.D), int(hi*c.D)
    steps = []
    # The three disjoint sign-changing brackets contain all three roots.
    assert polynomial(F(lo, c.D))*polynomial(F(hi, c.D)) < 0
    while hi-lo > 1:
        mid = (lo+hi)//2
        sign = polynomial(F(mid, c.D))
        steps.append([mid, 1 if sign > 0 else -1 if sign < 0 else 0])
        if not sign:
            lo = hi = mid
            break
        if polynomial(F(lo, c.D))*sign < 0:
            hi = mid
        else:
            lo = mid
    assert lo == hi or polynomial(F(lo, c.D))*polynomial(F(hi, c.D)) < 0
    return [lo, hi], steps


def primes_to(n):
    return [p for p in range(2, n+1)
            if all(p % k for k in range(2, isqrt(p)+1))]


def point_count(p):
    if p == 2:
        pairs = [[x, y] for x in range(p) for y in range(p)
                 if (y*y+y-x*x*x-x*x+2*x) % p == 0]
        return {'p': p, 'pairs': pairs, 'affine': len(pairs),
                'total': len(pairs)+1, 'a_p': p-len(pairs)}
    chars = []
    for x in range(p):
        d = (1 + 4*(x*x*x+x*x-2*x)) % p
        t = pow(d, (p-1)//2, p)
        assert t in (0, 1, p-1)
        chars.append(-1 if t == p-1 else t)
    affine = p+sum(chars)
    return {'p': p, 'discriminant_characters': chars, 'affine': affine,
            'total': affine+1, 'a_p': p-affine}


def coefficients(T, counts):
    ap = {row['p']: row['a_p'] for row in counts}
    a = [0, 1]
    factor_data = []
    for n in range(2, T+1):
        value, rem, factors = 1, n, []
        for p in primes_to(n):
            if rem % p:
                continue
            exponent = 0
            while rem % p == 0:
                rem //= p
                exponent += 1
            prev, curr = 1, ap[p]
            powers = [prev, curr]
            for k in range(2, exponent+1):
                prev, curr = curr, ap[p]*curr-p*prev
                powers.append(curr)
            value *= curr
            factors.append([p, exponent, powers])
            if rem == 1:
                break
        assert rem == 1
        a.append(value)
        factor_data.append([n, factors])
    assert all(abs(a[n]) <= n for n in range(1, T+1))
    return a, factor_data


def chi5(n):
    return [0, 1, -1, -1, 1][n % 5]


def attempt(bits, T):
    c = Dyadic(bits)
    # pi from Machin's identity, with rational alternating-series errors.
    J = bits//3+8
    u, v = atan_bracket(5, J), atan_bracket(239, J)
    pi_exact = [16*u[0]-4*v[1], 16*u[1]-4*v[0]]
    pi = c.out(*pi_exact)
    sqrt389 = c.sqrt(c.out(F(389)))
    h = c.div(c.scale(pi, 2), c.scale(sqrt389, 5))
    K = bits//2+8
    elo = exp_bracket(F(h[1], c.D), K)[0]
    ehi = exp_bracket(F(h[0], c.D), K)[1]
    r = c.out(elo, ehi)
    assert 0 < r[0] <= r[1] < c.D
    counts = [point_count(p) for p in primes_to(T)]
    nodal = point_count(389)
    assert nodal['a_p'] == 1 and 95*95 % 389 == 856 % 389
    epsilon = -nodal['a_p']
    assert chi5(-389) == -epsilon
    a, factors = coefficients(T, counts)
    powers, partials = [], []
    power, partial = c.out(F(1)), c.out(F(0))
    for n in range(1, T+1):
        power = c.mul(power, r)
        partial = c.add(partial, c.scale(power, F(2*chi5(n)*a[n], n)))
        powers.append(power)
        partials.append(partial)
    next_power = c.mul(power, r)
    tail = c.div(c.scale(next_power, 2), [c.D-r[1], c.D-r[0]])[1]
    L = [partial[0]-tail, partial[1]+tail]
    roots, root_steps = [], []
    for lo, hi in [(F(-3), F(-2)), (F(0), F(1, 4)), (F(1, 4), F(1))]:
        root, steps = root_bracket(c, lo, hi)
        roots.append(root)
        root_steps.append(steps)
    e1, e2, e3 = roots
    A = c.sqrt(c.sub(e3, e1))
    G = c.sqrt(c.sub(e3, e2))
    agm_steps = [[A, G]]
    for _ in range(12):
        A, G = c.scale(c.add(A, G), F(1, 2)), c.sqrt(c.mul(A, G))
        agm_steps.append([A, G])
    # Exact arithmetic AGM has min <= limit <= max at every stage.
    agm = [min(A[0], G[0]), max(A[1], G[1])]
    omega_plus = c.div(pi, agm)
    omega_total = c.scale(omega_plus, 2)
    omega_twist = c.div(omega_total, c.sqrt(c.out(F(5))))
    ratio = c.div(L, omega_twist)
    B = 2  # proved before isolation in L031; does not come from decimals
    candidates = set()
    denominator_ranges = []
    for den in range(1, B+1):
        low = ceilq(F(ratio[0]*den, c.D))
        high = (ratio[1]*den)//c.D
        denominator_ranges.append([den, low, high])
        for num in range(low, high+1):
            if gcd(num, den) == 1:
                candidates.add(F(num, den))
    width = F(ratio[1]-ratio[0], c.D)
    isolated = len(candidates) == 1 and width < F(1, B*B)
    return {
        'bits': bits, 'scale': c.D, 'T': T,
        'source_inputs': {'model': [0, 1, 1, -2, 0], 'N': 389, 'Delta': 389,
                          'optimal_table_label': '389a1', 'torsion_order': 1,
                          'components': 2, 'Manin_constant': 1,
                          'twist': 5, 'Pal_minimalization_factor': 1, 'B': B},
        'pi': {'atan_terms': J, 'atan_brackets': [[str(t) for t in u], [str(t) for t in v]],
               'exact_bracket': [str(t) for t in pi_exact], 'interval': pi},
        'sqrt389': sqrt389, 'h': h,
        'exponential': {'Taylor_degree': K, 'exact_bracket': [str(elo), str(ehi)], 'r': r},
        'point_counts': counts, 'nodal_count': nodal, 'epsilon_N': epsilon,
        'chi_minus_N': chi5(-389), 'twist_root_number': -chi5(-389)*epsilon,
        'coefficients': a, 'factorizations_and_prime_powers': factors,
        'series': {'powers': powers, 'partials': partials, 'next_power': next_power,
                   'tail_upper': tail, 'L_interval': L},
        'period': {'roots': roots, 'root_bisections': root_steps, 'agm_steps': agm_steps,
                   'agm_bracket': agm, 'omega_plus': omega_plus,
                   'omega_total': omega_total, 'omega_twist': omega_twist},
        'isolation': {'ratio': ratio, 'width': str(width), 'required_width': '1/4',
                      'denominator_ranges': denominator_ranges,
                      'candidates': [str(t) for t in sorted(candidates)], 'isolated': isolated},
        'failures': [] if isolated else ['rational isolation not certified'],
    }


def main():
    attempts = []
    for bits, T in [(48, 256), (64, 384), (80, 512)]:
        # This fixed schedule permits at most three evaluations total.
        data = attempt(bits, T)
        attempts.append(data)
        iso = data['isolation']
        print(f"bits={bits} T={T} B=2 ratio_width={iso['width']} required<1/4 "
              f"candidates={iso['candidates']} failures={data['failures']}")
        if iso['isolated']:
            break
    cert = {'attempts': attempts, 'selected_attempt': len(attempts)-1}
    path = HERE/'certificate.json'
    path.write_text(json.dumps(cert, indent=2)+'\n')
    print('certificate:', path.relative_to(HERE.parents[1]),
          'sha256:', sha256(path.read_bytes()).hexdigest())


if __name__ == '__main__':
    main()
