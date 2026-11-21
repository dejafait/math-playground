"""Exact-rational constants for the L701 bulk-disk Taylor comparison.

No finite Picard array or numerical zero count is used. Logarithms use
the convergent complex atanh series with an absolute tail; pi uses
Machin's identity and alternating arctangent bounds. Every arithmetic
operation is rational. Decimal strings below are outward rational bounds.
The analytic asymptotic and its eventual quantifiers are proved in L701.
"""
from fractions import Fraction as Q
from math import factorial
from pathlib import Path
from hashlib import sha256
import json


class I:
    def __init__(self, lo, hi=None):
        self.lo, self.hi = Q(lo), Q(lo if hi is None else hi)
        assert self.lo <= self.hi

    def __add__(self, other):
        other = iv(other)
        return I(self.lo + other.lo, self.hi + other.hi)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-iv(other))

    def __rsub__(self, other):
        return iv(other) + (-self)

    def __mul__(self, other):
        other = iv(other)
        products = [a*b for a in (self.lo, self.hi)
                    for b in (other.lo, other.hi)]
        return I(min(products), max(products))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = iv(other)
        assert not other.lo <= 0 <= other.hi
        return self * I(1/other.hi, 1/other.lo)

    def abs_upper(self):
        return max(abs(self.lo), abs(self.hi))


def iv(x):
    return x if isinstance(x, I) else I(x)


def power(x, k):
    out = I(1)
    for _ in range(k):
        out = out*x
    return out


def cadd(a, b):
    return a[0]+b[0], a[1]+b[1]


def cmul(a, b):
    return a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]


def cscale(a, b):
    return a[0]*b, a[1]*b


def cinv_exact(z):
    norm = z[0]*z[0]+z[1]*z[1]
    return z[0]/norm, -z[1]/norm


def outward(x, digits=30):
    scale = 10**digits
    lo = (x.lo*scale).__floor__()
    hi = -(-x.hi*scale).__floor__()
    return I(Q(lo, scale), Q(hi, scale))


def decimal(q, digits=30):
    scaled = q*10**digits
    assert scaled.denominator == 1
    n = scaled.numerator
    sign = '-' if n < 0 else ''
    whole, part = divmod(abs(n), 10**digits)
    return f'{sign}{whole}.{part:0{digits}d}'


def record(x):
    x = outward(iv(x))
    return [decimal(x.lo), decimal(x.hi)]


def crecord(z):
    return {'real': record(z[0]), 'imag': record(z[1])}


log_records = []


def clog_exact(z, name, terms=60):
    # Re(z)>0 selects the principal logarithm and |(z-1)/(z+1)|<1.
    assert z[0] > 0
    t = cmul((z[0]-1, z[1]), cinv_exact((z[0]+1, z[1])))
    q = Q(2, 3)
    norm2 = t[0]*t[0]+t[1]*t[1]
    assert norm2 < q*q
    t2, term, total = cmul(t, t), t, (Q(0), Q(0))
    for k in range(terms):
        total = cadd(total, cscale(term, Q(2, 2*k+1)))
        term = cmul(term, t2)
    tail = 2*q**(2*terms+1)/((2*terms+1)*(1-q*q))
    result = tuple(outward(I(c-tail, c+tail)) for c in total)
    log_records.append({'name': name, 'input': [str(c) for c in z],
                        'terms': terms, 'transform_norm_squared': str(norm2),
                        'transform_modulus_upper': str(q),
                        'absolute_tail_bound': str(tail),
                        'log_enclosure': crecord(result)})
    return result


def atan_inv(q, terms=40):
    value = sum((Q((-1)**k, (2*k+1)*q**(2*k+1))
                 for k in range(terms)), Q(0))
    tail = Q(1, (2*terms+1)*q**(2*terms+1))
    return I(value-tail, value+tail)


pi = outward(16*atan_inv(5)-4*atan_inv(239))
U = Q(121, 64)
w = (Q(625, 706), Q(225, 706))
v = cscale(w, Q(1, 2))
one_minus_v = (1-v[0], -v[1])
c = cscale(v, 1/U)
one_minus_c = (1-c[0], -c[1])
log_v = clog_exact(v, 'log(v)')
log_one_minus_v = clog_exact(one_minus_v, 'log(1-v)')
log_one_minus_c = clog_exact(one_minus_c, 'log(1-v/U)')
v_inv = cinv_exact(v)
v_inv2 = cmul(v_inv, v_inv)
Jv = cadd(cscale(v_inv, -1),
           cscale(cmul(v_inv2, log_one_minus_c), -U))
phi_prime = cadd(cadd(log_v, cscale(log_one_minus_v, -1)),
                 cadd((I(0), -pi), Jv))
b0 = cmul(w, phi_prime)
log_real = clog_exact((1-Q(1, 2)/U, Q(0)), 'log(1-1/(2U))')[0]
Jhalf = -2-4*U*log_real
b = cadd(b0, (-Jhalf, I(0)))
g = cadd(cadd(cmul(one_minus_v, log_one_minus_v), cmul(v, log_v)),
         cmul(v, (I(0), -pi)))
g = cadd(g, cadd((I(1), I(0)),
                 cmul(cmul(one_minus_c, cinv_exact(c)), log_one_minus_c)))
phase_ratio = 12*g[1]/pi

failures = []


def check(name, condition):
    if not condition:
        failures.append(name)
    return bool(condition)


alpha = I(Q(564, 1000), Q(566, 1000))
beta = I(Q(-2177, 1000), Q(-2175, 1000))
check('alpha enclosure', alpha.lo < b[0].lo <= b[0].hi < alpha.hi)
check('beta enclosure', beta.lo < b[1].lo <= b[1].hi < beta.hi)
check('nonresonant phase', Q(-5257, 1000) < phase_ratio.lo
      <= phase_ratio.hi < Q(-5255, 1000))
T, radius, B, exp_bound = Q(21, 20), Q(1, 4), Q(9, 4), Q(9, 5)
check('tangent cap', Q(51, 49) < T*T)
check('complex coefficient cap', alpha.abs_upper()**2+beta.abs_upper()**2 < B*B)
check('phase amplitude cap', 1+T*T == Q(29, 20)**2)
L = alpha.abs_upper()+T*beta.abs_upper()
ell_lower = 1-L*radius
check('linear margin', ell_lower > Q(7, 25))

# An exact positive-series upper bound for exp(B*radius).
x = B*radius
exp_partial = sum((x**k/Q(factorial(k)) for k in range(21)), Q(0))
exp_tail = x**21/Q(factorial(21))/(1-x/22)
check('exponential tail bound', exp_partial+exp_tail < exp_bound)

bc = (alpha, beta)
b2, b3, b4 = cmul(bc, bc), None, None
b3 = cmul(b2, bc)
b4 = cmul(b3, bc)
pi2, pi4 = pi*pi, power(pi, 4)
coefficients = [
    (b2[0]/2+pi2/6, -b2[1]/2),
    (b3[0]/6+alpha*pi2/6, -b3[1]/6-beta*pi2/6),
    (b4[0]/24-pi4/120, -b4[1]/24),
]
coeff_records, polynomial_cost = [], Q(0)
for k, (constant, tangent) in enumerate(coefficients, 2):
    bound = constant.abs_upper()+T*tangent.abs_upper()
    cost = bound*radius**k
    polynomial_cost += cost
    coeff_records.append({'degree': k, 'constant': record(constant),
                          'tangent_coefficient': record(tangent),
                          'absolute_coefficient_upper': record(bound),
                          'boundary_cost_upper': record(cost)})

Q2 = pi.hi**2*radius**2
sinc_loss = Q2/(6*(1-Q2/20))
sinc_lower = 1-sinc_loss
numerator_tail = Q(29, 20)*exp_bound*x**5/factorial(5)
denominator_tail = (L*radius*Q2**2/120
                    +(1+L*radius)*Q2**3/(5040*(1-Q2/72)))
remainder_upper = (polynomial_cost+numerator_tail+denominator_tail)/sinc_lower
check('sinc margin', sinc_lower > Q(89, 100))
check('Taylor remainder margin', remainder_upper < Q(1, 5))

source = Path(__file__)
output = source.with_suffix('.json')
report = {
    'kind': 'Exact-rational constants and full-circle limiting Taylor certificate for L701',
    'source_sha256': sha256(source.read_bytes()).hexdigest(),
    'pi_method': '16 atan(1/5)-4 atan(1/239), 40 terms and absolute alternating tails',
    'pi': record(pi), 'logs': log_records,
    'g': crecord(g), 'b': crecord(b),
    'twelve_theta_over_pi': record(phase_ratio),
    'declared_alpha': record(alpha), 'declared_beta': record(beta),
    'phase_square_threshold': '49/100', 'tangent_cap': str(T),
    'radius': str(radius), 'coefficient_modulus_upper': str(B),
    'linear_slope_upper': record(L),
    'linear_boundary_lower': record(ell_lower), 'required_linear_lower': '7/25',
    'exp_series_upper': record(exp_partial+exp_tail), 'exp_bound': str(exp_bound),
    'coefficients': coeff_records,
    'sinc_boundary_lower': record(sinc_lower),
    'polynomial_cost_upper': record(polynomial_cost),
    'numerator_tail_upper': record(numerator_tail),
    'denominator_tail_upper': record(denominator_tail),
    'Taylor_remainder_upper': record(remainder_upper), 'required_remainder_upper': '1/5',
    'limiting_strict_margin_lower': record(ell_lower-remainder_upper),
    'failures': failures,
    'qualification': 'Constants only. Uniform exact-profile asymptotics, phase recurrence, holomorphy and Rouche application are in L701. No formal verification or finite-n onset.'
}
output.write_text(json.dumps(report, indent=2)+'\n')
print('Certificate:', 'PASS' if not failures else 'FAIL')
print('12 theta/pi:', record(phase_ratio), '; required strictly between -5.257 and -5.255')
print('Linear boundary lower:', record(ell_lower), '; required > 0.28')
print('Taylor remainder upper:', record(remainder_upper), '; required < 0.20')
print('Failures:', failures)
print('Full certificate:', output)
if failures:
    raise SystemExit(1)
