"""Rigorous first retained direction for the approved fixed Schur test.

Standard-library Decimal intervals; see C759d for the exact reduction
and analytic tail bounds. No covariance truncation certifies a sign.
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
G = 128
gamma = sum((I(1)/j for j in range(1,G+1)),I(0))
gamma -= I(G).ln()+I(1)/(2*G)
gamma += I(1)/(12*G**2)
gamma = pm(gamma,I(1)/(60*G**4))
e_minus_one = I(-1).exp()
partial = {key:I(0) for key in ('S','C','D','B')}
terms=[]
for k in range(K):
    b = I(2*k)+I(1)/2
    e = (-2*b).exp()
    den = b*b+PI*PI
    row = {'S':PI*(1-e)/den,
           'C':-PI*PI*(1-e)/(b*den),
           'D':(1-e)*(b*b-PI*PI)/(den*den)-2*e*b/den,
           'B':(1-e)/b-(1-e*e_minus_one)/(b+I(1)/2)}
    terms.append({'k':k,'b':b.save(),'E':e.save(),
                  **{key:v.save() for key,v in row.items()}})
    for key,v in row.items():
        partial[key] += v
b0=I(2*K)+I(1)/2
R2=b0**(-2)+1/(2*b0)
R3=b0**(-3)+1/(4*b0*b0)
exp_tail=(-2*b0).exp()/(1-I(-4).exp())
drad=R2+2*exp_tail/b0
tails={'S':I(0,(PI*R2).hi),
       'C':I((-PI*PI*R3).lo,0),
       'D':I(drad.hi.copy_negate(),drad.hi),
       'B':I(0,(R2/2).hi)}
integrals={key:partial[key]+tails[key] for key in partial}
S,C,DD,B=(integrals[key] for key in ('S','C','D','B'))
tanh1=(I(2).exp()-1)/(I(2).exp()+1)
arch=-gamma-(4*PI*tanh1).ln()-2*C+DD-2*B-S/PI
sinh_half=(I('0.5').exp()-I('-0.5').exp())/2
g1=2*PI*sinh_half/(PI*PI+I(1)/4)
pole=-2*g1*g1
prime=I(0)
prime_rows=[]
for n,p in [(2,2),(3,3),(4,2),(5,5),(7,7)]:
    delay=I(n).ln()
    weight=I(p).ln()/I(n).sqrt()
    sn,cs,x,shift=sincos_turns(delay/2)
    q=(2-delay)*cs+sn/PI
    term=-weight*q
    prime += term
    prime_rows.append({'n':n,'p':p,'delay':delay.save(),'weight':weight.save(),
                       'reduction_integer':shift,'reduced_argument':x.save(),
                       'sin':sn.save(),'cos':cs.save(),'q':q.save(),'term':term.save()})
Q=arch+pole+prime
tau=I(11)/200
A11=Q-tau
checks={
    'all_five_prime_powers': [r['n'] for r in prime_rows]==[2,3,4,5,7],
    'last_delay_below_2': I(7).ln().hi<2,
    'next_prime_power_above_2': I(8).ln().lo>2,
    'pi_between_3_and_4': 3<PI.lo and PI.hi<4,
    'Q_lower_above_0_001': Q.lo>D('0.001'),
    'Q_upper_below_0_004': Q.hi<D('0.004'),
    'A11_upper_below_minus_0_051': A11.hi<D('-0.051'),
    'positive_scalar_floor': D('0.2859')>0,
}
failures=[key for key,ok in checks.items() if not ok]
report={'kind':'rigorous full-Q retained-direction Schur stop',
        'parameters':{'N':120,'retained_direction':1,'K':K,'precision':60,
                      'tau':'11/200','d':'2859/10000'},
        'source_url':'https://arxiv.org/html/2511.22755v1',
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'constants':{'pi':PI.save(),'gamma':gamma.save(),'tanh1':tanh1.save(),
                     'sinh_half':sinh_half.save(),'g1':g1.save()},
        'series_terms':terms,'series_partial_sums':{key:v.save() for key,v in partial.items()},
        'tail_majorants':{'R2':R2.save(),'R3':R3.save(),'exponential_sum':exp_tail.save()},
        'tails':{key:v.save() for key,v in tails.items()},
        'integrals':{key:v.save() for key,v in integrals.items()},
        'prime_terms':prime_rows,
        'components':{'archimedean':arch.save(),'pole':pole.save(),'prime':prime.save()},
        'result':{'Q_s1':Q.save(),'shifted_A11':A11.save(),
                  'S_d_upper_bound':str(A11.hi),'required_for_positive_S_d':'>0 in every nonzero retained direction',
                  'covariance_used':'complete Gram K is positive semidefinite; no truncation or upper estimate used'},
        'checks':checks,'failures':failures,'outcome':'NEGATIVE' if not failures else 'INCONCLUSIVE'}
path=Path(__file__).with_suffix('.json')
path.write_text(json.dumps(report,indent=2)+'\n')
print('Q(s1) in',Q.save())
print('S_d(s1) <= A11 <=',A11.hi,'; positive-definiteness requires >0')
print('Checks:',len(checks),'Failures:',failures,'Certificate:',path)
if failures:
    raise SystemExit(1)
