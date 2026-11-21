#!/usr/bin/env python3
"""Integer interval certificate for the fixed model, not its endpoint join.

Every stored interval endpoint is an integer times 2**(-BITS).
No floating-point arithmetic enters an enclosure or acceptance decision.
See C466d, certified compact contact subsection, for all remainder proofs.
"""
import json
from fractions import Fraction as R
from functools import cache
from math import comb, factorial, isqrt
from pathlib import Path

BITS = 512
S = 1 << BITS
ORDER = 16
N = 48
ASYM = 160
OUT = Path(__file__).with_suffix('.json')


def ceildiv(a, b):
    return -((-a)//b)


class I:
    def __init__(self, lo, hi=None, raw=False):
        if raw:
            self.lo, self.hi = lo, hi
        else:
            v = R(lo)
            self.lo = v.numerator*S//v.denominator
            self.hi = ceildiv(v.numerator*S, v.denominator)
        assert self.lo <= self.hi

    @staticmethod
    def box(a, b):
        return I(I(a).lo, I(b).hi, True)

    def __add__(self, other):
        other = lift(other)
        return I(self.lo+other.lo, self.hi+other.hi, True)
    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo, True)

    def __sub__(self, other):
        return self+-lift(other)

    def __rsub__(self, other):
        return lift(other)+-self

    def __mul__(self, other):
        other = lift(other)
        p = [a*b for a in (self.lo, self.hi) for b in (other.lo, other.hi)]
        return I(min(p)//S, ceildiv(max(p), S), True)
    __rmul__ = __mul__

    def __truediv__(self, other):
        other = lift(other)
        assert other.lo > 0 or other.hi < 0
        pairs = [(a*S, b) for a in (self.lo, self.hi)
                 for b in (other.lo, other.hi)]
        return I(min(a//b for a, b in pairs),
                 max(ceildiv(a, b) for a, b in pairs), True)

    def __pow__(self, n):
        assert n >= 0
        out, base = I(1), self
        while n:
            if n & 1:
                out = out*base
            n //= 2
            if n:
                base = base*base
        return out

    def scale(self, r):
        """Scale by an exact rational without first rounding that rational."""
        r = R(r)
        v = [self.lo*r.numerator, self.hi*r.numerator]
        return I(min(v)//r.denominator, ceildiv(max(v), r.denominator), True)

    def sqrt(self):
        assert self.lo >= 0
        lo, hi = isqrt(self.lo*S), isqrt(self.hi*S)
        if hi*hi < self.hi*S:
            hi += 1
        return I(lo, hi, True)

    def data(self):
        return [str(self.lo), str(self.hi)]


def lift(x):
    return x if isinstance(x, I) else I(x)


def symmetric(bound):
    return I(-bound.hi, bound.hi, True)


@cache
def fall(k):
    v = R(1)
    for j in range(k):
        v *= R(1, 2)-j
    return v


def jbase(c, b):
    """Enclose J_b(c), including both finite-evaluation tails."""
    t = b*c
    root = I(c).sqrt()
    if t <= 1024:
        ti = I(t)
        term = total = weighted = I(1)
        k = 0
        while True:
            k += 1
            term = (term*ti).scale(R(1, k))
            total = total+term
            weighted = weighted+term.scale(R(1, 2*k+1))
            if k > 2*t and term.hi*(1 << 450) < total.lo:
                break
            assert k < 10000
        tail = (term*ti).scale(R(1, k+1))/(1-I(t/(k+2)))
        exp_t = total+I(0, tail.hi, True)
        series = weighted+I(0, tail.hi, True)
        return root.scale(R(1, b))*(1-series/exp_t)
    assert t >= 4*ASYM
    total = I(0)
    for k in range(ASYM-1, -1, -1):
        total = total.scale(1/t)+I((-1)**k*fall(k))
    remainder = (I(2*abs(fall(ASYM))/t**ASYM)
                 +I(5*factorial(256)*(R(2)/t)**256))
    return root.scale(R(1, b))*(total+symmetric(remainder))


def tail_bounds(c):
    """C466d(18)-(19), at the center, through derivative ORDER."""
    n = N+1
    b = 2**n-1
    d = R(2**n)
    for m in range(1, n):
        d /= 2**m-1
    root = I(c).sqrt()
    out = []
    for j in range(ORDER+1):
        bound = (root*I(c)).scale(R(2, 3)*b**j)
        for v in range(j):
            bound += root.scale(abs(fall(v))*b**(j-1-v)/c**v)
        rho = R(2*3**j, b)
        assert rho < 1
        out.append(bound.scale(d/(1-rho)))
    return out


def center_jets(c):
    q = [I(0) for _ in range(ORDER+1)]
    root = I(c).sqrt()
    powers = [root.scale(fall(j)/c**j) for j in range(ORDER)]
    d = R(2)
    for n in range(1, N+1):
        b = 2**n-1
        val = jbase(c, b)
        q[0] += val.scale(d)
        for j in range(1, ORDER+1):
            val = powers[j-1]-val.scale(b)
            q[j] += val.scale(d)
        d *= R(-2, 2**n-1)
    for j, e in enumerate(tail_bounds(c)):
        q[j] += symmetric(e)
    return q


def tilt_jets(q):
    assert q[0].lo > 0
    a = R(q[1].lo+q[1].hi, q[0].lo+q[0].hi)
    return a, [sum((q[k].scale(comb(j,k)*(-a)**(j-k))
                    for k in range(j+1)), I(0)) for j in range(ORDER+1)]


def cell_jets(c, delta, q, a):
    radius = c/2
    theta = delta/radius
    assert 0 <= theta < 1
    # |exp(-a*(z-c))*Q(z)| <= 3**ceil(|a|*radius)*13*c^(3/2).
    ar = abs(a)*radius
    exponent = ceildiv(ar.numerator, ar.denominator)
    majorant = (I(c)*I(c).sqrt()).scale(13*3**exponent)
    h = I.box(-delta, delta)
    out = []
    for j in range(6):
        v = I(0)
        for k in range(ORDER-j, -1, -1):
            v = v*h+q[j+k].scale(R(1, factorial(k)))
        ratio = theta*R(ORDER+2, ORDER+2-j)
        assert ratio < 1
        error = majorant.scale(R(factorial(ORDER+1), factorial(ORDER+1-j))
                               /radius**j*theta**(ORDER+1-j)/(1-ratio))
        out.append(v+symmetric(error))
    return out


def det3(a, b, c):
    return (a[0]*(b[1]*c[2]-b[2]*c[1])
            -a[1]*(b[0]*c[2]-b[2]*c[0])
            +a[2]*(b[0]*c[1]-b[1]*c[0]))


def evaluate(q):
    f = -det3(q[:3], q[1:4], q[2:5])
    fp = -det3(q[:3], q[1:4], q[3:6])
    if q[0].lo <= 0:
        return f, None, None
    z = f/q[0]**3
    zp = fp/q[0]**3-3*f*q[1]/q[0]**4
    return f, z, zp


def short(integer):
    # Reporting only: an outward grid of spacing 10^-15.
    lo = integer*10**15//S
    return str(R(lo, 10**15))


def certify_segment(left, right, mode):
    stack = [(left, right)]
    accepted, rejected = [], []
    evaluations = 0
    while stack:
        a, b = stack.pop()
        c, delta = (a+b)/2, (b-a)/2
        # Start with relative cell radius <= 1/256.
        if delta > c/256:
            stack.extend([(c, b), (a, c)])
            continue
        a_tilt, q = tilt_jets(center_jets(c))
        evaluations += 1
        enclosed = cell_jets(c, delta, q, a_tilt)
        fq, zq, zpq = evaluate(enclosed)
        ok = zq is not None and (zq.lo > 0 if mode == 'positive'
                                 else zpq.hi*5000 < -S)
        if ok:
            accepted.append({'left':str(a), 'right':str(b),
                             'tilt':str(a_tilt),
                             'Q_tilt':enclosed[0].data(),
                             'F':fq.data(), 'Z':zq.data(), 'Zprime':zpq.data()})
        elif b-a > R(1, 2**28) and evaluations < 20000:
            stack.extend([(c, b), (a, c)])
        else:
            rejected.append({'left':str(a), 'right':str(b),
                             'F':fq.data(), 'Z':None if zq is None else zq.data(),
                             'Zprime':None if zpq is None else zpq.data()})
            break
        if evaluations % 250 == 0:
            print(mode, 'evaluations', evaluations, 'accepted', len(accepted),
                  'through',str(b), 'remaining', len(stack), flush=True)
    accepted.sort(key=lambda v:R(v['left']))
    covered = not rejected and not stack and bool(accepted)
    if covered:
        assert R(accepted[0]['left']) == left and R(accepted[-1]['right']) == right
        assert all(R(a['right']) == R(b['left']) for a,b in zip(accepted,accepted[1:]))
    return {'interval':[str(left),str(right)], 'mode':mode,
            'complete':covered, 'evaluations':evaluations,
            'cells':accepted,'failures':rejected,
            'unprocessed':[[str(a),str(b)] for a,b in stack]}


def main():
    payload = {'status':'INCOMPLETE', 'bits':BITS,'order':ORDER,
               'exponential_terms':N,'large_argument_terms':ASYM,
               'normalization':'Q=Gamma(3/2)*exp(x)*p/K; Z=D3(Q)/Q^3',
               'endpoint_join_proved':False,
               'first_contact_proved':False,'segments':[], 'endpoints':[]}
    for x in (R(139,32), R(35,8)):
        f,z,zp = evaluate(center_jets(x)[:6])
        payload['endpoints'].append({'x':str(x),'F':f.data(),'Z':z.data(),'Zprime':zp.data()})
    for a,b,mode in [(R(139,32),R(35,8),'decreasing'),
                     (R(1,32),R(139,32),'positive')]:
        segment = certify_segment(a,b,mode)
        payload['segments'].append(segment)
        OUT.write_text(json.dumps(payload,indent=2)+'\n')
        print(mode,'complete',segment['complete'],'cells',len(segment['cells']),flush=True)
    compact_ok = all(s['complete'] for s in payload['segments'])
    endpoints_ok = (int(payload['endpoints'][0]['Z'][0]) > 0
                    and int(payload['endpoints'][1]['Z'][1]) < 0)
    payload['status'] = 'COMPACT_CERTIFIED_ENDPOINT_JOIN_OPEN' if compact_ok and endpoints_ok else 'FAILED'
    payload['summary'] = {
        'compact_coverage_passed':compact_ok, 'endpoint_signs_passed':endpoints_ok,
        'minimum_prefix_Z_lower':str(min(int(v['Z'][0]) for v in payload['segments'][1]['cells']))
            if payload['segments'][1]['cells'] else None,
        'maximum_contact_Zprime_upper':str(max(int(v['Zprime'][1]) for v in payload['segments'][0]['cells']))
            if payload['segments'][0]['cells'] else None,
        'required_contact_Zprime_upper':'-1/5000',
        'unresolved':['No effective positive interval covering (0,1/32).',
                      'An earlier zero below 1/32 is not excluded.',
                      'C466d admissibility and endpoint proof remain unaudited.']}
    OUT.write_text(json.dumps(payload,indent=2)+'\n')
    print(payload['status'])
    for row in payload['endpoints']:
        print('x',row['x'],'Z lower grid',short(int(row['Z'][0])),
              'Z upper below grid+1e-15',short(int(row['Z'][1])))
    summary=payload['summary']
    if summary['minimum_prefix_Z_lower']:
        print('Prefix Z lower >=',short(int(summary['minimum_prefix_Z_lower'])))
    if summary['maximum_contact_Zprime_upper']:
        print('Contact Zprime upper <',short(int(summary['maximum_contact_Zprime_upper'])),
              '+ 1e-15; required < -1/5000')
    print('Unresolved:', '; '.join(summary['unresolved']))
    print('Full certificate:', OUT)


if __name__ == '__main__':
    main()
