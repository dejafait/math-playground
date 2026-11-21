"""One exact stored vector, complete compact Weil form; see C759n.

Pure Python integers construct endpoint-jump convolutions exactly.
Directed Decimal intervals enclose every subsequent operation.
No matrix eigenvalue or sampled quadrature is used as evidence.
"""
from decimal import Decimal as D, Context, ROUND_FLOOR, ROUND_CEILING
from fractions import Fraction as F
from pathlib import Path
from math import comb, factorial
import hashlib
import json
import sys
import numpy as np

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).parent
PREC, ORDER, EXP_ORDER, POLE_ORDER = 900, 256, 128, 64
LO = Context(prec=PREC, rounding=ROUND_FLOOR)
HI = Context(prec=PREC, rounding=ROUND_CEILING)


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
            raise ArithmeticError('divisor contains zero')
        return a * I(LO.divide(D(1), b.hi), HI.divide(D(1), b.lo))

    def __rtruediv__(a, b):
        return I(b) / a

    def __pow__(a, n):
        if n < 0:
            return I(1) / a**(-n)
        ans = I(1)
        while n:
            if n & 1:
                ans *= a
            a *= a
            n //= 2
        return ans

    def ln(a):
        return I(LO.next_minus(LO.ln(a.lo)), HI.next_plus(HI.ln(a.hi)))

    def exp(a):
        return I(LO.next_minus(LO.exp(a.lo)), HI.next_plus(HI.exp(a.hi)))

    def sqrt(a):
        return I(LO.next_minus(LO.sqrt(a.lo)), HI.next_plus(HI.sqrt(a.hi)))

    def save(a):
        return [str(a.lo), str(a.hi)]


def rat(q):
    return I(q.numerator) / q.denominator


def symmetric(v, r):
    rr = I(r).hi
    return I(LO.subtract(v.lo, rr), HI.add(v.hi, rr))


def abs_upper(v):
    return max(v.lo.copy_abs(), v.hi.copy_abs())


def iconvolve(a, b):
    """Exact signed integer convolution by balanced Kronecker packing."""
    if not any(a) or not any(b):
        return [0] * (len(a)+len(b)-1)
    bound = min(len(a), len(b))*max(map(abs, a))*max(map(abs, b))
    bits = (2*bound).bit_length()+1
    base = 1 << bits
    mask = base-1
    def pack(v):
        z = 0
        for c in reversed(v):
            z = (z << bits)+c
        return z
    z = pack(a)*pack(b)
    out = []
    for _ in range(len(a)+len(b)-1):
        c = z & mask
        if c > base//2:
            c -= base
        out.append(c)
        z = (z-c) >> bits
    assert z == 0
    # Independent integer identity checks, not floating evaluations.
    for t in (-1, 0, 1, 2):
        def ev(v):
            ans = 0
            for c in reversed(v):
                ans = ans*t+c
            return ans
        assert ev(out) == ev(a)*ev(b)
    return out


source = ROOT/'even-time-one-pair-849.npz'
source_hash = hashlib.sha256(source.read_bytes()).hexdigest()
assert source_hash == 'f74832d1420ec849848f3392e740a87b1bf9ddd53cb39a7ec9d7662c265548fa'
data = np.load(source)['modal_coefficients'][:, 0]
assert data.shape == (256,) and np.isfinite(data).all()
coeff = [F.from_float(float(x)) for x in data]
den_exp = max(q.denominator.bit_length()-1 for q in coeff)+508
den = 1 << den_exp
assert all(den % q.denominator == 0 for q in coeff)

# p(x)=(1-x^2) sum c_{j+1} P_{2j}(x), integer coefficients / den.
p = [0]*511
for j, q in enumerate(coeff[1:]):
    n = 2*j
    scale = q.numerator * (den // (q.denominator*(1 << n)))
    for m in range(n//2+1):
        val = scale * (-1)**m * comb(n, m)*comb(2*n-2*m, n)
        k = n-2*m
        p[k] += val
        p[k+2] -= val
assert sum(p) == 0 and all(p[k] == 0 for k in range(1, 511, 2))
facts = [factorial(k) for k in range(ORDER+1024)]
# Taylor expansion p(-1+t); multiplying by k! gives endpoint derivatives.
left = [sum(p[i]*comb(i, k)*(-1)**(i-k) for i in range(k, 511))*facts[k]
        for k in range(511)]
assert left[0] == 0
right = [-(-1)**k*left[k] for k in range(511)]
c = coeff[0].numerator*(den//coeff[0].denominator)
bl = [0, 0, 12800*c, -1536000*c, 61440000*c]
br = [0, 0, -12800*c, -1536000*c, -61440000*c]
jumps = [(F(-1), left), (F(-33,40), bl), (F(-31,40), br),
         (F(31,40), bl), (F(33,40), br), (F(1), right)]

# C(y)=(f*f)(-y)=sum_{b>0,k>=1} B[b,k]*(b-y)_+^k/(den^2*k!).
splines = {}
for i, (a, wa) in enumerate(jumps):
    for j in range(i, len(jumps)):
        aa, wb = jumps[j]
        b = -(a+aa)
        if b <= 0:
            continue
        v = iconvolve(wa, wb)
        mul = 1 if i == j else 2
        row = splines.setdefault(b, [0]*1022)
        for k, x in enumerate(v, start=1):
            row[k] += mul*x
print('Exact dyadic vector and autocorrelation constructed;', len(splines), 'pieces', flush=True)

den2 = den*den
norm_exact = F(0)
deriv_exact = F(0)
for b, row in splines.items():
    bp = F(1)
    for k, v in enumerate(row):
        if v:
            a = F(v, den2*facts[k])*bp
            norm_exact += a
            if k >= 2:
                deriv_exact -= a*k*(k-1)/(b*b)
        bp *= b
assert norm_exact > 0 and deriv_exact > 0
norm, deriv = rat(norm_exact), rat(deriv_exact)
print('Exact norm positive; derivative norm positive; enclosing moments', flush=True)

moments = [I(0) for _ in range(ORDER+1)]  # moments[n] = int y^(n-1) C(y)dy
T0 = I(0)
harmonic = [I(0)]
for k in range(1, 1022):
    harmonic.append(harmonic[-1]+I(1)/k)
component_records = []
for b, row in sorted(splines.items()):
    bi = rat(b)
    logpart = (2/bi).ln()
    bp = I(1)
    subtotal = I(0)
    for k, v in enumerate(row):
        if v:
            a = (I(v)/den2/facts[k])*bp
            subtotal += a*(harmonic[k]+logpart)
            term = a*bi/(k+1)
            for n in range(1, ORDER+1):
                moments[n] += term
                term *= bi*n/(k+n+1)
        bp *= bi
    T0 += subtotal
    component_records.append({'boundary': str(b), 'T0': subtotal.save()})

# K(y)=y*exp(y/2)/sinh(y), analytic on |y|<pi.
kernel = []
for n in range(ORDER+1):
    val = I(1)/((1 << n)*facts[n])
    for j in range(2, n+1, 2):
        val -= kernel[n-j]/facts[j+1]
    kernel.append(val)

integral = I(0)
terms = []
exp_error = I(0)
for n, kn in enumerate(kernel):
    en = I(0)
    for j in range(1, EXP_ORDER+1):
        en += I((-1)**j)*(1 << n)/(facts[j]*(n+j))
    er = I(1 << n)/(facts[EXP_ORDER+1]*(n+EXP_ORDER+1))
    en = symmetric(en, er)
    tn = T0 if n == 0 else norm*(1 << n)/n-moments[n]
    term = kn*(tn+norm*en)
    integral += term
    exp_error += I(abs_upper(kn))*norm*er
    terms.append({'n': n, 'kernel': kn.save(), 'Tn': tn.save(),
                  'En': en.save(), 'term': term.save()})
kernel_remainder = 100*(I(4)/5)**(ORDER+1)*(deriv+norm)
integral = symmetric(integral, kernel_remainder)

def atan_recip(k):
    z, val = I(1)/k, I(0)
    power = z
    for j in range(60):
        val += (-1)**j*power/(2*j+1)
        power *= z*z
    return symmetric(val, power/121)

pi = 16*atan_recip(5)-4*atan_recip(239)
sin_lower = sum((F((-1)**j)*F(5,2)**(2*j+1)/facts[2*j+1]
                 for j in range(6)), F(0))
disk_checks = (pi.lo > D('2.5') and sin_lower > F(1,2)
               and I('1.25').exp().hi < 4)
assert disk_checks
gk = 1024
gamma = sum((I(1)/j for j in range(1, gk+1)), I(0))
gamma -= I(gk).ln()+I(1)/(2*gk)
gamma += I(1)/(12*gk*gk)
gamma_error = I(1)/(60*gk**4)
gamma = symmetric(gamma, gamma_error)
tanh1 = (I(2).exp()-1)/(I(2).exp()+1)
arch = -(gamma+(4*pi*tanh1).ln())*norm+integral

# Complete polar product: 4 int_0^2 C(y)cosh(y/2)dy.
pole = sum((4*moments[2*j+1]/((1 << (2*j))*facts[2*j])
            for j in range(POLE_ORDER+1)), I(0))
pole_error = 16*norm/facts[2*POLE_ORDER+2]
pole = symmetric(pole, pole_error)

def corr(y):
    total = I(0)
    for b, row in splines.items():
        bb = rat(b)
        if bb.hi < y.lo:
            continue
        assert bb.lo > y.hi, 'shift crosses an unpaid piece boundary'
        r = bb-y
        value = I(0)
        for k in range(len(row)-1, -1, -1):
            value = value*r+I(row[k])/den2/facts[k]
        total += value
    return total

prime = I(0)
prime_rows = []
for n, base in [(2,2), (3,3), (4,2), (5,5), (7,7)]:
    delay = I(n).ln()
    weight = I(base).ln()/I(n).sqrt()
    cy = corr(delay)
    term = -2*weight*cy
    prime += term
    prime_rows.append({'n': n, 'base': base, 'delay': delay.save(),
                       'correlation': cy.save(), 'weight': weight.save(),
                       'contribution': term.save()})

form = arch+pole+prime
quotient = form/norm
checks = {'exact_input_hash': True, 'even_polynomial_and_endpoint_zero': True,
          'norm_positive': norm.lo > 0, 'derivative_norm_positive': deriv.lo > 0,
          'all_five_shifts': len(prime_rows) == 5,
          'complete_pole_term': True, 'exterior_subtraction_retained': True,
          'no_matrix_premise': True, 'kernel_disk_sin_bound': disk_checks,
          'quotient_positive': quotient.lo > 0,
          'quotient_negative': quotient.hi < 0}
status = ('POSITIVE_FIXED_VECTOR' if quotient.lo > 0 else
          'UNVERIFIED_CANDIDATE' if quotient.hi < 0 else 'INCONCLUSIVE_ZERO_CROSSING')
result = {
    'status': status, 'scope': 'One stored dyadic column0; no sweep; REPRODUCTION',
    'input': {'path': source.name, 'sha256': source_hash,
              'coefficients': [str(q) for q in coeff],
              'basis': 'v,(1-x^2)P_0,(1-x^2)P_2,...,(1-x^2)P_508',
              'denominator_exponent': den_exp},
    'exact_geometry': {'jump_positions': [str(a) for a, _ in jumps],
                       'jump_derivatives_integer_numerators': [[str(v) for v in row] for _, row in jumps],
                       'autocorrelation_integer_numerators': {str(b): [str(v) for v in row] for b, row in sorted(splines.items())},
                       'autocorrelation_denominator': '2^(2*denominator_exponent) * k!',
                       'norm_squared_exact': str(norm_exact), 'derivative_norm_squared_exact': str(deriv_exact)},
    'bounds': {'norm_squared': norm.save(), 'derivative_norm_squared': deriv.save(),
               'archimedean': arch.save(), 'both_poles': pole.save(), 'prime_sum': prime.save(),
               'full_form': form.save(), 'quotient': quotient.save(),
               'required_sign': 'upper<0 for a negative candidate; lower>0 rejects this indication'},
    'integration': {'precision_decimal': PREC, 'kernel_order': ORDER,
                     'kernel_disk_radius': '5/2', 'kernel_disk_bound': '20',
                     'kernel_error': kernel_remainder.save(),
                     'exponential_order': EXP_ORDER, 'exponential_error_included': exp_error.save(),
                     'pole_order': POLE_ORDER, 'pole_error': pole_error.save(),
                     'gamma_error': gamma_error.save(), 'T0_components': component_records,
                     'moments': [x.save() for x in moments[1:]], 'terms': terms},
    'primes': prime_rows, 'checks': checks,
    'failures': [] if quotient.lo > 0 or quotient.hi < 0 else ['Final interval crosses zero; fixed test ends.'],
    'software': {'python': sys.version, 'numpy': np.__version__,
                  'trust': 'Python integer/Fraction/Decimal documented exact and correctly-rounded semantics; not formal verification'},
    'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
out = Path(__file__).with_suffix('.json')
out.write_text(json.dumps(result, indent=2)+'\n')
def short(v):
    return f'[{v.lo:.12E}, {v.hi:.12E}]'
print('Norm squared:', short(norm))
print('Archimedean:', short(arch), 'both poles:', short(pole), 'primes:', short(prime))
print('Complete Q:', short(form), 'quotient:', short(quotient))
print('Required: upper<0 or lower>0; outcome:', status)
print('Kernel error:', short(kernel_remainder), 'failures:', result['failures'])
print('Certificate:', out)
