"""Fixed first-sine full-Q modulus defect. See C759e for proof and tails.
Interval primitives reused verbatim from the audited step806 generator.
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

    def absupper(a):
        return max(a.lo.copy_abs(), a.hi.copy_abs())

    def save(a):
        return [str(a.lo), str(a.hi)]


def pm(a, e):
    r = I(e).absupper()
    return I(LO.subtract(a.lo, r), HI.add(a.hi, r))


def atan_recip(k):
    z = I(1) / k
    val, power = I(0), z
    for j in range(60):
        val += (-1)**j * power / (2*j+1)
        power *= z*z
    return pm(val, power/121)


PI = 16*atan_recip(5)-4*atan_recip(239)


def sincos_turns(turns):
    center = LO.divide(LO.add(turns.lo, turns.hi), D(2))
    shift = int(center.to_integral_value())
    x = 2*PI*(turns-shift)
    if x.absupper() >= 4:
        raise ArithmeticError('argument reduction bound failed')
    x2 = x*x
    st, ct = x, I(1)
    ss, cc = st, ct
    for k in range(1,60):
        st = -st*x2/((2*k)*(2*k+1))
        ct = -ct*x2/((2*k-1)*(2*k))
        ss += st
        cc += ct
    se, ce = st*x2/(120*121), ct*x2/(119*120)
    return pm(ss,2*se), pm(cc,2*ce), x, shift


K = 512
partial = I(0)
series = []
for j in range(K):
    b = I(2*j)+I(1)/2
    exponential = (-b).exp()
    laplace = PI*(1+exponential)/(b*b+PI*PI)
    term = laplace*laplace
    partial += term
    series.append({'j':j, 'b':b.save(), 'exp_minus_b':exponential.save(),
                   'laplace_u':laplace.save(), 'term':term.save()})
B = I(2*K)+I(1)/2
R4 = B**(-4)+B**(-3)/6
tail_bound = 4*PI*PI*R4
series_full = partial+I(0,tail_bound.hi)
arch = -4*series_full
den = PI*PI+I(1)/4
iplus = PI*(1+I('0.5').exp())/den
iminus = PI*(1+I('-0.5').exp())/den
pole = 4*(iplus*iplus+iminus*iminus)
prime = I(0)
prime_rows = []
for n,p in [(2,2),(3,3),(4,2),(5,5),(7,7)]:
    d = I(n).ln()
    assert 0 < d.lo and d.hi < 2
    if d.hi < 1:
        h = d
        branch = 'd<1'
    elif d.lo > 1:
        h = 2-d
        branch = 'd>1'
    else:
        raise ArithmeticError('correlation branch undecided')
    sn,cs,arg,shift = sincos_turns(h/2)
    H = (sn/PI-h*cs)/2
    weight = I(p).ln()/I(n).sqrt()
    term = -4*weight*H
    prime += term
    prime_rows.append({'n':n, 'p':p, 'delay':d.save(), 'branch':branch,
                       'h':h.save(), 'reduced_argument':arg.save(),
                       'reduction_integer':shift, 'sin':sn.save(),
                       'cos':cs.save(), 'H':H.save(),
                       'weight':weight.save(), 'term':term.save()})
delta = arch+pole+prime
# This imported audited enclosure is not recomputed by this defect script.
q_sine = I('0.00168053281301474','0.00364123566126519')
q_modulus = q_sine+delta
checks = {
    'pi_between_3_and_4': 3 < PI.lo and PI.hi < 4,
    'complete_prime_powers': [r['n'] for r in prime_rows] == [2,3,4,5,7],
    'next_prime_power_outside_support': I(8).ln().lo > 2,
    'all_H_positive': all(D(r['H'][0]) > 0 for r in prime_rows),
    'full_gamma_tail_paid': 0 < tail_bound.lo and tail_bound.hi < D('0.00000001'),
    'input_cap_paid': q_sine.hi < (I(1)/250).lo,
    'defect_sign_decided': delta.lo > 0 or delta.hi < 0,
}
failures = [k for k,v in checks.items() if not v]
certificate = {
    'kind':'fixed first-sine complete-Q modulus defect, REPRODUCTION',
    'parameters':{'K':K,'precision':60,'half_width':1,'sign_threshold':0},
    'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'arithmetic_basis':'step806 interval primitives, 60 digits, outward rounding; analytic tails in C759e',
    'constants':{'pi':PI.save(),'I_plus':iplus.save(),'I_minus':iminus.save()},
    'series_terms':series,'series_partial_sum':partial.save(),
    'tail':{'B':B.save(),'R4':R4.save(),'unsigned_tail_upper':tail_bound.save(),
            'gamma_defect_tail':(-4*I(0,tail_bound.hi)).save()},
    'prime_terms':prime_rows,
    'components':{'archimedean':arch.save(),'pole':pole.save(),'prime':prime.save()},
    'input':{'C759d_Q_sine':q_sine.save(),'required_energy_cap':'1/250'},
    'result':{'Delta_1':delta.save(),'Q_modulus_from_imported_Q_sine':q_modulus.save(),
              'required_for_strict_modulus_lowering':'Delta_1<0',
              'sign':'positive' if delta.lo>0 else 'negative' if delta.hi<0 else 'undecided'},
    'checks':checks,'failures':failures,
}
out=Path(__file__).with_suffix('.json')
out.write_text(json.dumps(certificate,indent=2)+'\n')
print('Delta_1 in',delta.save(),'; required threshold: 0')
print('Gamma-defect tail in',(-4*I(0,tail_bound.hi)).save())
print('Checks:',len(checks),'Failures:',failures,'Certificate:',out)
if failures:
    raise SystemExit(1)


