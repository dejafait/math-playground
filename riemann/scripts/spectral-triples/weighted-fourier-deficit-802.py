"""Full fixed-W positive-deficit trace upper certificate; see C759c.

Every sine mode j>120 is included by C759a(8). No digamma sampling or
numerical quadrature: unit rectangles use proved monotone majorants.
Directed interval convention reused from complement-budget-793.py.
"""
from decimal import Decimal as D, Context, ROUND_FLOOR, ROUND_CEILING
from pathlib import Path
import hashlib
import json

LO = Context(prec=60, rounding=ROUND_FLOOR)
HI = Context(prec=60, rounding=ROUND_CEILING)


class I:
    def __init__(self, lo=0, hi=None):
        if isinstance(lo, I):
            self.lo, self.hi = lo.lo, lo.hi
        else:
            self.lo = D(lo)
            self.hi = self.lo if hi is None else D(hi)

    def __add__(a, b):
        b = I(b)
        return I(LO.add(a.lo, b.lo), HI.add(a.hi, b.hi))

    __radd__ = __add__

    def __neg__(a):
        return I(a.hi.copy_negate(), a.lo.copy_negate())

    def __sub__(a, b):
        return a + (-I(b))

    def __rsub__(a, b):
        return I(b) - a

    def __mul__(a, b):
        b = I(b)
        pairs = [(x, y) for x in (a.lo, a.hi) for y in (b.lo, b.hi)]
        return I(min(LO.multiply(x, y) for x, y in pairs),
                 max(HI.multiply(x, y) for x, y in pairs))

    __rmul__ = __mul__

    def __truediv__(a, b):
        b = I(b)
        if b.lo <= 0 <= b.hi:
            raise ArithmeticError('division interval contains zero')
        return a * I(LO.divide(D(1), b.hi), HI.divide(D(1), b.lo))

    def __rtruediv__(a, b):
        return I(b) / a

    def __pow__(a, n):
        if n < 0:
            return I(1) / a**(-n)
        result = I(1)
        while n:
            if n & 1:
                result *= a
            a *= a
            n //= 2
        return result

    def ln(a):
        if a.lo <= 0:
            raise ArithmeticError('nonpositive logarithm argument')
        return I(LO.next_minus(LO.ln(a.lo)), HI.next_plus(HI.ln(a.hi)))

    def exp(a):
        return I(LO.next_minus(LO.exp(a.lo)), HI.next_plus(HI.exp(a.hi)))

    def sqrt(a):
        if a.lo < 0:
            raise ArithmeticError('negative square-root argument')
        return I(LO.next_minus(LO.sqrt(a.lo)), HI.next_plus(HI.sqrt(a.hi)))

    def positive_part(a):
        return I(max(D(0), a.lo), max(D(0), a.hi))

    def save(a):
        return [str(a.lo), str(a.hi)]


def atan_recip(k):
    z = I(1)/k
    value, power = I(0), z
    for j in range(60):
        value += (-1)**j * power/(2*j+1)
        power *= z*z
    radius = (power/121).hi
    return I(LO.subtract(value.lo, radius), HI.add(value.hi, radius))


N, cutoff = 120, 350
pi = 16*atan_recip(5)-4*atan_recip(239)
m_floor = -(4*pi).ln()-4
edge = 121*pi


def h(t):
    t = I(t)
    return (t/(2*pi)).ln()-2/t**2


def sine_tail_majorant(t):
    t = I(t)
    gap = 1-(t/edge)**2
    if gap.lo <= 0:
        raise ArithmeticError('majorant evaluated past its frequency range')
    return 4/(pi**2*N*gap**2)


# Evenness converts dt/(2*pi) over R to dt/pi over the positive half-line.
# [0,1]: global m_floor; [k,k+1]: h(k) lower and M(k+1) upper.
origin = (4-m_floor)*sine_tail_majorant(1)/pi
bound = origin
rows = []
for k in range(1, cutoff):
    deficit = (4-h(k)).positive_part()
    tail = sine_tail_majorant(k+1)
    contribution = deficit*tail/pi
    bound += contribution
    rows.append({'left': k, 'right': k+1,
                 'deficit_upper_function': deficit.save(),
                 'all_modes_tail_majorant': tail.save(),
                 'rectangle': contribution.save()})

prime_rows, C = [], I(0)
for n, p in [(2, 2), (3, 3), (4, 2), (5, 5), (7, 7)]:
    weight = I(p).ln()/I(n).sqrt()
    chain = I(2).sqrt() if n == 2 else I(1)
    C += weight*chain
    prime_rows.append({'n': n, 'p': p, 'weight': weight.save(),
                       'chain_norm': chain.save()})
sinh_half = (I('0.5').exp()-I('-0.5').exp())/2
P = 8*sinh_half**2/(pi**2*N)
tau = I(11)/200
threshold = 4-C-P-tau
shifted_floor = threshold-bound
unshifted_floor = 4-bound-C-P

checks = {
    'cutoff_below_first_omitted_frequency': D(cutoff) < edge.lo,
    'symbol_lower_at_cutoff_above_four': h(cutoff).lo > 4,
    'all_349_rectangles_present': len(rows) == 349 and
        all(r['left'] == k and r['right'] == k+1
            for k, r in enumerate(rows, 1)),
    'nonnegative_rectangle_enclosures': all(
        D(r['rectangle'][0]) >= 0 and D(r['rectangle'][1]) >= D(r['rectangle'][0])
        for r in rows),
    'bound_below_0_529': bound.hi < D('0.529'),
    'threshold_above_0_8139': threshold.lo > D('0.8139'),
    'bound_strictly_below_threshold': bound.hi < threshold.lo,
    'unshifted_floor_above_0_3409': unshifted_floor.lo > D('0.3409'),
    'shifted_floor_above_0_2859': shifted_floor.lo > D('0.2859'),
}
failures = [k for k, v in checks.items() if not v]
result = {
    'task': 'fixed level4 full positive Fourier-deficit trace; W sine120 complement',
    'classification': 'REPRODUCTION; unaudited local specialization',
    'precision': 60, 'N': N, 'cutoff': cutoff, 'rectangle_width': 1,
    'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'constants': {'pi': pi.save(), 'm_floor': m_floor.save(),
                  'first_omitted_frequency': edge.save(),
                  'h_cutoff': h(cutoff).save()},
    'origin_rectangle': origin.save(), 'rectangles': rows,
    'prime_rows': prime_rows,
    'bounds': {'upper_majorant_B': bound.save(), 'C': C.save(), 'P_120': P.save(),
               'tau': tau.save(), 'required_trace_threshold': threshold.save(),
               'unshifted_floor': unshifted_floor.save(),
               'shifted_floor': shifted_floor.save(),
               'trace_enclosure': ['0', str(bound.hi)]},
    'checks': checks, 'failures': failures,
    'limitations': ['B is an upper majorant, not the trace value.',
                   'No lower trace estimate or exact spectral value is computed.',
                   'Form-dual coupling, finite Schur sign, parity and Xi bridges remain open.',
                   'Decimal arithmetic is a software trust assumption.'],
}
output = Path(__file__).with_suffix('.json')
output.write_text(json.dumps(result, indent=2)+'\n')
for key in ('upper_majorant_B', 'required_trace_threshold', 'shifted_floor'):
    print(key, result['bounds'][key])
print('all omitted modes j>120; 349 unit rectangles; |t|>=350 deficit zero')
print('failures', failures, 'certificate', output.as_posix())
if failures:
    raise SystemExit(1)
