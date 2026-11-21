"""Exact-integer products and outward Decimal interval phase certificate.

Every finite product is evaluated with Python integers. Only its direction
is needed, so a common positive power of two is removed with exact enclosing
integer endpoints. All subsequent arithmetic is directed at 70 digits.
The accompanying L700 proof supplies the infinite-tail and phase-grid costs.
"""
from decimal import Decimal as D, getcontext, ROUND_FLOOR, ROUND_CEILING, ROUND_HALF_EVEN
from hashlib import sha256
import json
from pathlib import Path

ctx = getcontext()
ctx.prec = 70
K, J, GRID = 32768, 64, 2048


def down(op):
    ctx.rounding = ROUND_FLOOR
    return op()


def up(op):
    ctx.rounding = ROUND_CEILING
    return op()


class I:
    def __init__(self, lo, hi=None):
        self.lo, self.hi = D(lo), D(lo if hi is None else hi)
        assert self.lo <= self.hi

    def __add__(self, b):
        b = as_i(b)
        return I(down(lambda: self.lo + b.lo), up(lambda: self.hi + b.hi))

    __radd__ = __add__

    def __neg__(self):
        # copy_negate is exact; unary minus would apply the current context.
        return I(self.hi.copy_negate(), self.lo.copy_negate())

    def __sub__(self, b):
        return self + (-as_i(b))

    def __rsub__(self, b):
        return as_i(b) + (-self)

    def __mul__(self, b):
        b = as_i(b)
        pairs = [(a, c) for a in (self.lo, self.hi) for c in (b.lo, b.hi)]
        return I(min(down(lambda a=a, c=c: a*c) for a, c in pairs),
                 max(up(lambda a=a, c=c: a*c) for a, c in pairs))

    __rmul__ = __mul__

    def __truediv__(self, b):
        b = as_i(b)
        assert not b.lo <= 0 <= b.hi
        recip = I(down(lambda: D(1)/b.hi), up(lambda: D(1)/b.lo))
        return self * recip

    def abs_upper(self):
        return max(self.lo.copy_abs(), self.hi.copy_abs())

    def record(self):
        return [str(self.lo), str(self.hi)]


def as_i(x):
    return x if isinstance(x, I) else I(x)


def square(x):
    if x.lo <= 0 <= x.hi:
        return I(0, up(lambda: x.abs_upper()**2))
    small = min(x.lo.copy_abs(), x.hi.copy_abs())
    large = x.abs_upper()
    return I(down(lambda: small*small), up(lambda: large*large))


def sqrt_i(x):
    assert x.lo >= 0
    lo = x.lo.sqrt().next_minus()
    hi = x.hi.sqrt().next_plus()
    assert lo >= 0
    assert up(lambda: lo*lo) <= x.lo
    assert down(lambda: hi*hi) >= x.hi
    return I(lo, hi)


def atan_inv(q, terms=120):
    x = I(1) / q
    x2, power, value = x*x, x, I(0)
    for k in range(terms):
        term = power/(2*k+1)
        value = value + (term if k % 2 == 0 else -term)
        power = power*x2
    tail = (power/(2*terms+1)).abs_upper()
    return value + I(-tail, tail)


PI = 16*atan_inv(5) - 4*atan_inv(239)
# Machin's identity; the alternating-series remainder is included above.
ln2, power, x2 = I(0), I(1)/3, I(1)/9
for k in range(100):
    ln2 = ln2 + 2*power/(2*k+1)
    power = power*x2
ln2 = ln2 + I(0, (2*power/((201)*(1-x2))).hi)
LOGK = 15*ln2


def cis(x):
    # Any integer gives an exact 2*pi reduction. This choice keeps |x|<4.
    q = int(((x.lo+x.hi)/(2*(PI.lo+PI.hi))).to_integral_value(rounding=ROUND_HALF_EVEN))
    x = x - q*(2*PI)
    assert x.abs_upper() < 4
    x2 = x*x
    cterm, sterm = I(1), x
    c, s = cterm, sterm
    for k in range(1, 81):
        cterm = -cterm*x2/((2*k-1)*(2*k))
        sterm = -sterm*x2/((2*k)*(2*k+1))
        c, s = c+cterm, s+sterm
    # Taylor through degree 161 for both; |remainder| <= 4^162/162!.
    import math
    tail = (I(4**162)/math.factorial(162)).hi
    return c+I(-tail, tail), s+I(-tail, tail)


def cmul(a, b):
    return a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]


def exact_product(j, first, last):
    if last-first == 1:
        return 706*first-625*j, -225*j
    mid = (first+last)//2
    ar, ai = exact_product(j, first, mid)
    br, bi = exact_product(j, mid, last)
    rr, ii = ar*br, ai*bi
    return rr-ii, (ar+ai)*(br+bi)-rr-ii


def digest_integer(x):
    data = abs(x).to_bytes((abs(x).bit_length()+7)//8, 'big')
    return sha256((b'-' if x < 0 else b'+')+data).hexdigest()


units, products = [], []
for j in range(1, J+1):
    ar, ai = exact_product(j, 1, K+1)
    rr, ii = 9*ar-25*ai, 25*ar+9*ai
    if j % 2 == 0:
        rr, ii = -rr, -ii
    shift = max(abs(rr).bit_length(), abs(ii).bit_length())-200
    assert shift > 0
    r0, i0 = rr >> shift, ii >> shift
    r, im = I(r0, r0+1), I(i0, i0+1)
    norm = sqrt_i(square(r)+square(im))
    unit = r/norm, im/norm
    phi = j*(I(225)/706)*(LOGK + I(32)/121)
    unit = cmul(unit, cis(phi))
    units.append(unit)
    products.append({'j': j, 'real_sha256': digest_integer(rr),
                     'imag_sha256': digest_integer(ii), 'binary_shift': shift,
                     'scaled_real': r.record(), 'scaled_imag': im.record(),
                     'unit_real': unit[0].record(), 'unit_imag': unit[1].record()})

delta = I(J)/K + I(J*J)/(2*K*(1-I(J)/(K+1)))
grid_cost = J*PI/GRID
rows, failures = [], []
worst_margin, worst_index = D('Infinity'), None
for k in range(GRID):
    theta = 2*PI*k/GRID
    base = cis(-theta)
    power = I(1), I(0)
    best_positive, best_negative = D('-Infinity'), D('-Infinity')
    positive_j, negative_j = None, None
    for j in range(1, J+1):
        power = cmul(power, base)
        real, _ = cmul(units[j-1], power)
        if real.lo > best_positive:
            best_positive, positive_j = real.lo, j
        if real.hi.copy_negate() > best_negative:
            best_negative, negative_j = real.hi.copy_negate(), j
    margin = min(best_positive, best_negative)
    paid = (I(margin)-delta-grid_cost).lo
    if paid < worst_margin:
        worst_margin, worst_index = paid, k
    if paid <= D('0.5'):
        failures.append(k)
    rows.append({'k': k, 'positive_j': positive_j, 'negative_j': negative_j,
                 'positive_lower': str(best_positive),
                 'negative_magnitude_lower': str(best_negative),
                 'paid_margin_lower': str(paid)})

out = {'kind': 'rigorous finite phase certificate; asymptotic transfer in L700',
       'precision': ctx.prec, 'K': K, 'J': J, 'grid': GRID,
       'pi': PI.record(), 'log_K': LOGK.record(),
       'infinite_product_phase_error_upper': str(delta.hi),
       'continuous_grid_cost_upper': str(grid_cost.hi),
       'required_paid_margin': '0.5', 'actual_paid_margin_lower': str(worst_margin),
       'worst_grid_index': worst_index, 'failures': failures,
       'products': products, 'grid_witnesses': rows}
path = Path(__file__).with_suffix('.json')
path.write_text(json.dumps(out, indent=2)+'\n')
print('Finite phase certificate:', 'PASS' if not failures else 'FAIL')
print('Actual paid lower margin:', worst_margin, '; required > 0.5')
print('Infinite-product cost <=', delta.hi)
print('Continuous-grid cost <=', grid_cost.hi)
print('Failed cells:', len(failures), '; full certificate:', path)
assert not failures
