#!/usr/bin/env python3
"""Independent complete rational replay of L962. No generating imports.

224-bit outward integer endpoints; direct physical phases for ALL n.
Only stdout display uses floats. See L962 for all qualifications.
"""
from fractions import Fraction
from math import factorial, isqrt
from array import array
from pathlib import Path
import hashlib
import json
import time

HERE = Path(__file__).resolve().parent
OUT = HERE / 'independent-audit-150.json'
B = 224
D = 1 << B
BLOCK = 2048


class Box:
    __slots__ = ('a', 'b')

    def __init__(self, v=0):
        if isinstance(v, Box):
            self.a, self.b = v.a, v.b
        else:
            if not isinstance(v, (int, Fraction)):
                raise TypeError('exact inputs only')
            v = Fraction(v)
            self.a = v.numerator*D // v.denominator
            self.b = -((-v.numerator*D) // v.denominator)

    @staticmethod
    def endpoints(a, b):
        assert a <= b
        z = object.__new__(Box)
        z.a, z.b = a, b
        return z

    def __add__(self, other):
        if isinstance(other, int):
            return Box.endpoints(self.a+other*D, self.b+other*D)
        other = Box(other)
        return Box.endpoints(self.a+other.a, self.b+other.b)
    __radd__ = __add__

    def __neg__(self):
        return Box.endpoints(-self.b, -self.a)

    def __sub__(self, other):
        return self + (-Box(other))

    def __rsub__(self, other):
        return Box(other) + (-self)

    def __mul__(self, other):
        if isinstance(other, int):
            v = (self.a*other, self.b*other)
            return Box.endpoints(min(v), max(v))
        other = Box(other)
        v = (self.a*other.a, self.a*other.b,
             self.b*other.a, self.b*other.b)
        return Box.endpoints(min(v)//D, -((-max(v))//D))
    __rmul__ = __mul__

    def __truediv__(self, other):
        if isinstance(other, int) and other > 0:
            return Box.endpoints(self.a//other, -((-self.b)//other))
        other = Box(other)
        assert not other.a <= 0 <= other.b
        a, b = Fraction(D, other.b), Fraction(D, other.a)
        return self * Box.endpoints(Box(a).a, Box(b).b)

    def __rtruediv__(self, other):
        return Box(other)/self

    def widened(self, error):
        assert error >= 0
        return Box.endpoints(self.a-error, self.b+error)

    def record(self):
        return {'lo': str(self.a), 'hi': str(self.b), 'denominator_power_two': B}


def root(z):
    assert z.a >= 0
    lo, hi = isqrt(z.a*D), isqrt(z.b*D)
    return Box.endpoints(lo, hi+int(hi*hi < z.b*D))


def atan_rational(v, terms):
    assert 0 <= v <= Fraction(1, 2)
    # Exact alternating rational sum, not dyadic accumulation.
    power, total, vv = v, Fraction(0), v*v
    for j in range(terms):
        total += (-1 if j % 2 else 1)*power/(2*j+1)
        power *= vv
    nxt = (-1 if terms % 2 else 1)*power/(2*terms+1)
    return Box.endpoints(Box(min(total, total+nxt)).a,
                         Box(max(total, total+nxt)).b)


def unit_log(v):
    assert 1 <= v <= 2
    z = Box((v-1)/(v+1))
    zz, term, ans = z*z, z, Box(0)
    for j in range(64):
        ans += (2*term)/(2*j+1)
        term = term*zz
    # After64 terms, term encloses z^129; denominator >=129.
    tail = (2*term)/(129*(1-zz))
    return Box.endpoints(ans.a, (ans+tail).b)


LN2 = unit_log(Fraction(2))


def logarithm(v):
    v = Fraction(v)
    assert v > 0
    k = v.numerator.bit_length()-v.denominator.bit_length()
    m = v / (Fraction(2)**k)
    while m < 1:
        k -= 1
        m *= 2
    while m >= 2:
        k += 1
        m /= 2
    return unit_log(m)+k*LN2


def log_box(v):
    assert v.a > 0
    return Box.endpoints(logarithm(Fraction(v.a, D)).a,
                         logarithm(Fraction(v.b, D)).b)


def horner(coeff, v):
    ans = coeff[-1]
    for c in coeff[-2::-1]:
        ans = ans*v+c
    return ans


EXP = [Box(Fraction(1, factorial(j))) for j in range(29)]
EXP_ERR = Box(Fraction(1, 8**29*factorial(29))).b
COS = [Box(Fraction((-1)**j, factorial(2*j))) for j in range(24)]
SIN = [Box(Fraction((-1)**j, factorial(2*j+1))) for j in range(24)]
COS_ERR = Box(Fraction(1, 4**48*factorial(48))).b
SIN_ERR = Box(Fraction(1, 4**49*factorial(49))).b


def amplitude(v):
    # Taylor directly at a NEGATIVE argument; derivative <=1.
    assert -32*D <= v.a <= v.b <= 0
    z = v/256
    assert -D//8 <= z.a <= z.b <= 0
    ans = horner(EXP, z).widened(EXP_ERR)
    assert ans.a > 0
    for _ in range(8):
        ans = ans*ans
    return ans


def direct_phase(theta, pi):
    period = 2*pi
    # An arbitrary integer reduction is exact by periodicity. Check full box.
    k = (theta.a+theta.b+period.a)//(2*period.a)
    reduced = theta-k*period
    margin = 4*D-max(abs(reduced.a), abs(reduced.b))
    assert margin > 0
    z = reduced/16
    assert max(abs(z.a), abs(z.b)) < D//4
    zz = z*z
    c = horner(COS, zz).widened(COS_ERR)
    s = (z*horner(SIN, zz)).widened(SIN_ERR)
    # Four angle doublings, avoiding composite character multiplication.
    for _ in range(4):
        c, s = 2*c*c-1, 2*s*c
    return c, s, margin, abs(k)


def cmul(z, w):
    return z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0]


def complex_record(z):
    return {'re': z[0].record(), 'im': z[1].record()}


def main():
    start = time.monotonic()
    data = {'status': 'IN_PROGRESS', 'bits': B,
            'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'inputs': {'t': '98/625', 'x': 6000000185827},
            'blocks': [], 'gates': {}, 'failures': [], 'completed_through': 0,
            'method': 'independent dyadic operations; direct phase at EVERY integer; negative exp Taylor; trig angle doubling',
            'series': {'log_terms': 64, 'exp_degree': 28, 'cos_degree': 46,
                       'sin_degree': 47, 'angle_doublings': 4, 'exp_squarings': 8},
            'qualification': 'Informal implementation proof; L962 conditional analytic hypotheses retained.'}

    def save():
        data['elapsed_seconds'] = time.monotonic()-start
        OUT.write_text(json.dumps(data, separators=(',', ':'))+'\n')

    def require(name, test, evidence=None):
        data['gates'][name] = {'passed': bool(test)}
        if evidence is not None:
            data['gates'][name]['evidence'] = evidence
        if not test:
            raise ArithmeticError(name)

    save()
    try:
        # Basic exact operation checks precede every numerical premise.
        for a in [Fraction(-7, 3), Fraction(0), Fraction(2, 7)]:
            for b in [Fraction(-5, 9), Fraction(3, 2)]:
                for name, actual, box in [('add', a+b, Box(a)+Box(b)),
                                         ('mul', a*b, Box(a)*Box(b)),
                                         ('div', a/b, Box(a)/Box(b))]:
                    require(f'{name}:{a}:{b}', Fraction(box.a, D) <= actual <= Fraction(box.b, D))
        x, t = 6000000185827, Box(Fraction(98, 625))
        # atan(1/2)+atan(1/3)=pi/4: tangent addition and range(0,pi/2).
        pi = 4*(atan_rational(Fraction(1, 2), 128)+atan_rational(Fraction(1, 3), 128))
        rad = x/(4*pi)+t/16
        N = isqrt(rad.a//D)
        lower, upper = rad-N*N, (N+1)**2-rad
        require('floor_lower', lower.a > 0, lower.record())
        require('floor_upper', upper.a > 0, upper.record())
        require('N_equals690988', N == 690988)
        data['N'] = N
        d = 1+x*x
        arg = pi/2-atan_rational(Fraction(1, x), 4)
        ar = logarithm(d)/4-log_box(4*pi)/2-Box(Fraction(1, d))
        ai = arg/2-Box(Fraction(3*x, d))
        # Explicit rational alpha' from the two complex reciprocals.
        di = Fraction(4*x, d*d)-Fraction(8*x, d*d)-Fraction(x, d)
        # Equivalently Re(-1/(2s²)-1/(s-1)²+1/(2s)).
        # The first two real terms are (2+4)*(x²-1)/d².
        dr = Fraction(6*(x*x-1), d*d)+Fraction(1, d)
        aprime = Box(dr), Box(di)
        sigma, tau = Box(Fraction(1, 2))+t*ar/2, Box(Fraction(x, 2))+t*ai/2
        ell = 2*ar+t*(ar*aprime[0]-ai*aprime[1])
        lnN, ln32 = logarithm(N), logarithm(32)
        require('ell_logN_gt13', (ell-lnN-13).a > 0, (ell-lnN-13).record())
        require('shift_gt0', (ell-2*ln32).a > 0, (ell-2*ln32).record())
        require('shift_lt25', (25-ell+2*ln32).a > 0, (25-ell+2*ln32).record())
        require('amplitudes_nonpositive_exponents', (sigma-t*lnN/4).a > 0)
        data['constants'] = {k: v.record() for k, v in [
            ('pi', pi), ('radicand', rad), ('arg_s', arg), ('alpha_re', ar),
            ('alpha_im', ai), ('alpha_prime_re', aprime[0]), ('alpha_prime_im', aprime[1]),
            ('sigma', sigma), ('tau', tau), ('ell', ell), ('logN', lnN), ('log32', ln32)]}
        data['remainders'] = {'exp': str(EXP_ERR), 'cos': str(COS_ERR), 'sin': str(SIN_ERR), 'denominator_power_two': B}
        # Largest-prime-factor sieve, unlike the generator's smallest factor.
        factor = array('I', [0])*(N+1)
        for p in range(2, N+1):
            if factor[p] == 0:
                for n in range(p, N+1, p):
                    factor[n] = p
        logs = [None]*(N+1)
        logs[1] = Box(0)
        A, L = (Box(0), Box(0)), (Box(0), Box(0))
        save()
        for lo in range(1, N+1, BLOCK):
            hi = min(N, lo+BLOCK-1)
            a, l = (Box(0), Box(0)), (Box(0), Box(0))
            min_margin, min_amp, max_k, max_width, primes = 4*D, D, 0, 0, 0
            for n in range(lo, hi+1):
                if n == 1:
                    u, c, s, amp, margin, k = Box(0), Box(1), Box(0), Box(1), 4*D, 0
                else:
                    p = factor[n]
                    assert p >= 2 and n % p == 0
                    if p == n:
                        u = logarithm(n)
                        primes += 1
                    else:
                        m = n//p
                        assert 1 < m < n and logs[p] is not None and logs[m] is not None
                        u = logs[p]+logs[m]
                    assert u.a > 0
                    c, s, margin, k = direct_phase(-tau*u, pi)
                    amp = amplitude(t*u*u/4-sigma*u)
                logs[n] = u
                assert amp.a > 0
                tr, ti = amp*c, amp*s
                a = a[0]+tr, a[1]+ti
                l = l[0]+u*tr, l[1]+u*ti
                min_margin, min_amp = min(min_margin, margin), min(min_amp, amp.a)
                max_k = max(max_k, k)
                max_width = max(max_width, u.b-u.a, c.b-c.a, s.b-s.a, amp.b-amp.a)
            A, L = (A[0]+a[0], A[1]+a[1]), (L[0]+l[0], L[1]+l[1])
            data['blocks'].append({'lo': lo, 'hi': hi, 'count': hi-lo+1,
                'prime_count': primes, 'all_term_gates_passed': True,
                'direct_phases': hi-lo+1-int(lo == 1), 'min_reduction_margin': str(min_margin),
                'min_amplitude': str(min_amp), 'max_reduction_integer': str(max_k),
                'max_elementary_width': str(max_width),
                'A_block': complex_record(a), 'L_block': complex_record(l)})
            data['completed_through'] = hi
            data['sums'] = {'A': complex_record(A), 'L': complex_record(L)}
            save()
            if len(data['blocks']) % 32 == 0 or hi == N:
                print(json.dumps({'through': hi, 'required': N,
                    'elapsed_seconds': round(time.monotonic()-start, 2)}), flush=True)
            if hi < N and time.monotonic()-start > 900:
                data['status'] = 'COST_STOP'
                data['failures'].append('one_replay_900_second_ceiling')
                save()
                return
        require('complete_support', sum(b['count'] for b in data['blocks']) == N
                and data['blocks'][0]['lo'] == 1 and data['blocks'][-1]['hi'] == N
                and all(a['hi']+1 == b['lo'] for a, b in zip(data['blocks'], data['blocks'][1:])))
        require('direct_phase_count', sum(b['direct_phases'] for b in data['blocks']) == N-1)
        S = ell*A[0]-2*L[0], ell*A[1]-2*L[1]
        value = A[0]*S[0]+A[1]*S[1]
        R = root(A[0]*A[0]+A[1]*A[1])
        p, q = Box(Fraction(101, 200000000)), Box(Fraction(142, 10000000)+Fraction(1, 250000000000))
        error = (25*R+Box(Fraction(81, 2)))*p+R*q+p*q
        paid, ceiling = value-error, value+error
        for name, z, low, high in [
                ('F', value, Fraction('150.30628'), Fraction('150.30629')),
                ('R', R, Fraction('2.49096'), Fraction('2.49097')),
                ('E', error, Fraction('0.00008727'), Fraction('0.00008728'))]:
            require(name+'_bounds', z.a > low*D and z.b < high*D, z.record())
        require('paid_gt150.30619', paid.a > Fraction('150.30619')*D, paid.record())
        data['result'] = {k: z.record() for k, z in [
            ('F', value), ('R', R), ('E', error), ('F_minus_E', paid), ('F_plus_E', ceiling), ('p', p), ('q', q)]}
        data['result']['S'] = complex_record(S)
        data['required_bound'] = 'F-E>150.30619'
        data['status'] = 'PASS'
        save()
        print(json.dumps({'status': data['status'], 'through': N, 'blocks': len(data['blocks']),
              'F_minus_E': [float(Fraction(paid.a, D)), float(Fraction(paid.b, D))],
              'required': '>150.30619', 'failures': data['failures'], 'path': str(OUT)}), flush=True)
    except Exception as exc:
        data['status'] = 'FAIL'
        data['failures'].append(type(exc).__name__+': '+str(exc))
        save()
        raise


if __name__ == '__main__':
    main()
