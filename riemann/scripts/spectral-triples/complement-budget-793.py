"""Fixed N=120 full-complement lower-envelope test; see C759a.

Decimal directed intervals, including transcendental outward expansion.
No finite matrix eigenvalues or sampled tail stand in for the complement.
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
        ends = [(x, y) for x in (a.lo, a.hi) for y in (b.lo, b.hi)]
        return I(min(LO.multiply(x, y) for x, y in ends),
                 max(HI.multiply(x, y) for x, y in ends))

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
        return I(LO.next_minus(LO.ln(a.lo)), HI.next_plus(HI.ln(a.hi)))

    def exp(a):
        return I(LO.next_minus(LO.exp(a.lo)), HI.next_plus(HI.exp(a.hi)))

    def sqrt(a):
        return I(LO.next_minus(LO.sqrt(a.lo)), HI.next_plus(HI.sqrt(a.hi)))

    def save(a):
        return [str(a.lo), str(a.hi)]


def symmetric(a, radius):
    r = I(radius).hi
    return I(LO.subtract(a.lo, r), HI.add(a.hi, r))


def atan_recip(k):
    z = I(1) / k
    val, power = I(0), z
    for j in range(60):
        val += (-1)**j * power / (2*j+1)
        power *= z*z
    return symmetric(val, power / 121)


N, K = 120, 512
pi = 16*atan_recip(5) - 4*atan_recip(239)
gamma_k = 128
gamma = sum((I(1)/j for j in range(1, gamma_k+1)), I(0))
gamma -= I(gamma_k).ln() + I(1)/(2*gamma_k)
gamma += I(1)/(12*gamma_k**2)
gamma = symmetric(gamma, I(1)/(60*gamma_k**4))

prime_rows = []
prime_norm = I(0)
prime_trial = I(0)
for n, p in [(2, 2), (3, 3), (4, 2), (5, 5), (7, 7)]:
    delay = I(n).ln()
    weight = I(p).ln()/I(n).sqrt()
    chain_norm = I(2).sqrt() if n == 2 else I(1)
    prime_norm += weight*chain_norm
    prime_trial += weight*(2-delay)
    prime_rows.append({'n': n, 'p': p, 'delay': delay.save(),
                       'weight': weight.save(), 'chain_norm': chain_norm.save()})

sinh_half = (I('0.5').exp()-I('-0.5').exp())/2
pole_tail = 8*sinh_half**2/(pi*pi*N)
m_floor = -(4*pi).ln()-4
frequency_edge = 121*pi


def h(t):
    t = I(t)
    return (t/(2*pi)).ln()-2/t**2


def leakage(t):
    t = I(t)
    return 4*t/(pi**3*N*(1-(t/frequency_edge)**2)**2)


p100 = leakage(100)
arch100 = h(100)*(1-p100)+m_floor*p100
lower100 = arch100-prime_norm-pole_tail
# All T<=100: h(T)<=log(100/(2*pi)), and the mixture is <=h(T).
case_low = (I(100)/(2*pi)).ln()-prime_norm
# All 100<=T<121*pi: p(T)>=p100; m_floor<-5, h(T)<log(121/2).
# Discard the negative pole budget to make this an UPPER bound on
# every generated lower estimate, not a lower bound on the spectrum.
h_max = (I(121)/2).ln()
case_high = h_max*(1-p100)-5*p100-prime_norm
uniform_ceiling = max(case_low.hi, case_high.hi)

# Constant even Ritz vector 1/sqrt(2), using the source defining entries.
# rho(y)=sum exp(-(2k+1/2)y), B=int rho(1-exp(-y/2)), D0=int y*rho.
terms = []
b_sum, d_sum = I(0), I(0)
for k in range(K):
    b = I(2*k)+I('0.5')
    e = (-2*b).exp()
    bt = (1-e)/b - (1-(-2*(b+I('0.5'))).exp())/(b+I('0.5'))
    dt = (1-e)/b**2-2*e/b
    b_sum += bt
    d_sum += dt
    terms.append({'k': k, 'B': bt.save(), 'D0': dt.save()})
b_edge = I(2*K)+I('0.5')
tail2 = b_edge**(-2)+1/(2*b_edge)
B = b_sum + I(0, (tail2/2).hi)
D0 = d_sum + I(0, tail2.hi)
tanh1 = (I(2).exp()-1)/(I(2).exp()+1)
arch_trial = -(gamma+(4*pi*tanh1).ln()+2*B-D0)
pole_trial = 16*sinh_half**2
trial = arch_trial+pole_trial-prime_trial
U, tau = D('0.054'), D('0.055')

checks = {
    'complete_prime_range': I(7).ln().hi < 2 < I(8).ln().lo,
    'two_chain_length_three': (2*I(2).ln()).hi < 2 < (3*I(2).ln()).lo,
    'other_chains_length_two': I(3).ln().lo > 1,
    'm_floor_below_minus_five': m_floor.hi < -5,
    'h_one_above_floor': h(1).lo > m_floor.hi,
    'p100_between_zero_and_one': 0 < p100.lo < p100.hi < 1,
    'prime_norm_above_3_129': prime_norm.lo > D('3.129'),
    'uniform_ceiling_below_minus_0_14': uniform_ceiling < D('-0.14'),
    'trial_positive': trial.lo > 0,
    'trial_below_U': trial.hi < U,
    'tau_above_U': tau > U,
}
failures = [key for key, value in checks.items() if not value]
result = {
    'task': 'full parity comparison; fixed 120 odd modes; analytic prerequisite test',
    'precision': 60, 'N': N, 'series_K': K,
    'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'constants': {'pi': pi.save(), 'gamma': gamma.save(), 'm_floor': m_floor.save(),
                  'first_omitted_frequency': frequency_edge.save()},
    'prime_rows': prime_rows,
    'bounds': {'prime_norm': prime_norm.save(), 'pole_tail': pole_tail.save(),
               'p100': p100.save(), 'arch100': arch100.save(),
               'lower100_unshifted': lower100.save(),
               'case_low_upper': case_low.save(), 'case_high_upper': case_high.save(),
               'all_thresholds_upper': str(uniform_ceiling),
               'required_shifted_lower': '>0', 'trial': trial.save(),
               'U': str(U), 'tau': str(tau)},
    'trial_details': {'B_partial': b_sum.save(), 'D0_partial': d_sum.save(),
                      'tail_sum_inverse_square_upper': tail2.save(),
                      'B': B.save(), 'D0': D0.save(),
                      'arch': arch_trial.save(), 'pole': pole_trial.save(),
                      'prime': prime_trial.save(), 'terms': terms},
    'checks': checks, 'failures': failures,
    'conclusion': 'insufficient_lower_envelope' if not failures else 'certificate_check_failed',
    'limitations': ['No full odd lower floor above U was certified.',
                    'No coupling or finite Schur sign was computed.',
                    'An upper bound on a lower estimate is not an upper spectral bound.',
                    'The actual parity inequality remains unresolved.'],
}
output = Path(__file__).with_suffix('.json')
output.write_text(json.dumps(result, indent=2)+'\n')
print('N=120; complete complement, no omitted-mode truncation')
for key in ('prime_norm', 'pole_tail', 'lower100_unshifted', 'all_thresholds_upper', 'trial'):
    print(key, result['bounds'][key])
print('U', U, 'tau', tau, 'required shifted complement lower bound > 0')
print('failures', failures, 'certificate', output.as_posix())
if failures:
    raise SystemExit(1)
