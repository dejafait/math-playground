"""Full continuous L2 certificate for L681 weights, q=1,2,4,8.

Outward binary64 interval operations; rational root isolation and a
Cauchy/Laurent alias bound. No libm trigonometry or sampled-norm inference.
Analytic justification is canonical in C681b. All sample bounds are saved.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
import numpy as np

N = 16384
NEG, POS = -np.inf, np.inf
checks, failures = [], []


def down(x):
    return np.nextafter(x, NEG)


def up(x):
    return np.nextafter(x, POS)


class I:
    def __init__(self, lo, hi=None):
        self.lo = np.asarray(lo, dtype=np.float64)
        self.hi = self.lo if hi is None else np.asarray(hi, dtype=np.float64)

    @staticmethod
    def rational(v):
        v = Q(v)
        f = float(v)
        return I(down(f), up(f))

    def __add__(a, b):
        b = ri(b)
        return I(down(a.lo+b.lo), up(a.hi+b.hi))

    __radd__ = __add__

    def __neg__(a):
        return I(-a.hi, -a.lo)

    def __sub__(a, b):
        return a+-ri(b)

    def __rsub__(a, b):
        return ri(b)+-a

    def __mul__(a, b):
        b = ri(b)
        terms = [a.lo*b.lo, a.lo*b.hi, a.hi*b.lo, a.hi*b.hi]
        return I(down(np.minimum.reduce(terms)), up(np.maximum.reduce(terms)))

    __rmul__ = __mul__

    def __truediv__(a, b):
        b = ri(b)
        if not np.all((b.lo > 0) | (b.hi < 0)):
            raise ArithmeticError('interval denominator contains zero')
        return a*I(down(1/b.hi), up(1/b.lo))

    def square(a):
        high = up(np.maximum(a.lo*a.lo, a.hi*a.hi))
        low = down(np.minimum(a.lo*a.lo, a.hi*a.hi))
        low = np.where((a.lo <= 0) & (a.hi >= 0), 0, low)
        return I(np.maximum(low, 0), high)


def ri(v):
    return v if isinstance(v, I) else I(v)


class C:
    def __init__(self, re, im=0):
        self.re, self.im = ri(re), ri(im)

    def __add__(a, b):
        b = ci(b)
        return C(a.re+b.re, a.im+b.im)

    __radd__ = __add__

    def __neg__(a):
        return C(-a.re, -a.im)

    def __sub__(a, b):
        return a+-ci(b)

    def __rsub__(a, b):
        return ci(b)+-a

    def __mul__(a, b):
        b = ci(b)
        return C(a.re*b.re-a.im*b.im, a.re*b.im+a.im*b.re)

    __rmul__ = __mul__

    def __truediv__(a, b):
        b = ci(b)
        den = b.re.square()+b.im.square()
        if not np.all(den.lo > 0):
            raise ArithmeticError('complex denominator not separated from zero')
        return C((a.re*b.re+a.im*b.im)/den,
                 (a.im*b.re-a.re*b.im)/den)

    def abs2(a):
        return a.re.square()+a.im.square()


def ci(v):
    return v if isinstance(v, C) else C(v)


def check(name, passed, actual, required):
    checks.append(dict(name=name, passed=bool(passed), actual=str(actual), required=str(required)))
    if not passed:
        failures.append(name)


def atan_bounds(v, count=60):
    value = sum((-1)**j*v**(2*j+1)/Q(2*j+1) for j in range(count))
    nxt = (-1)**count*v**(2*count+1)/Q(2*count+1)
    return min(value, value+nxt), max(value, value+nxt)


a5, a239 = atan_bounds(Q(1, 5)), atan_bounds(Q(1, 239))
PI = (16*a5[0]-4*a239[1], 16*a5[1]-4*a239[0])
pi = I(I.rational(PI[0]).lo, I.rational(PI[1]).hi)


def isolate(k):
    lo, hi = Q(2*k+1, 2), Q(8*k+5, 8)
    for _ in range(48):
        mid = (lo+hi)/2
        al, ah = atan_bounds(1/(10*mid), 30)
        fl = mid-Q(2*k+1, 2)-ah/PI[0]
        fh = mid-Q(2*k+1, 2)-al/PI[1]
        if fl > 0:
            hi = mid
        elif fh < 0:
            lo = mid
        else:
            raise ArithmeticError('undecided exact root sign')
    al, ah = atan_bounds(1/(10*lo), 30)
    left = lo-Q(2*k+1, 2)-al/PI[1]
    al, ah = atan_bounds(1/(10*hi), 30)
    right = hi-Q(2*k+1, 2)-ah/PI[0]
    check(f'root {k} endpoint signs', left < 0 < right,
          f'left upper={left}; right lower={right}', 'left upper<0<right lower')
    return lo, hi


# A primitive roots-of-unity enclosure by Taylor, then binary powers.
# sin/cos Taylor remainders are bounded by theta^(2m+1)/(2m+1)!
# and theta^(2m)/(2m)! respectively, since 0<theta<1.
theta = pi*2/N
t2 = theta*theta
sn, cs = I(0), I(0)
sp, cp = theta, I(1)
for j in range(16):
    sn = sn+sp
    cs = cs+cp
    sp = -sp*t2/((2*j+2)*(2*j+3))
    cp = -cp*t2/((2*j+1)*(2*j+2))
sn = sn+I(-max(abs(float(sp.lo)), abs(float(sp.hi))),
           max(abs(float(sp.lo)), abs(float(sp.hi))))
cs = cs+I(-max(abs(float(cp.lo)), abs(float(cp.hi))),
           max(abs(float(cp.lo)), abs(float(cp.hi))))
u = C(np.ones(N), np.zeros(N))
power = C(cs, sn)
indices = np.arange(N)
for bit in range(14):
    candidate = u*power
    mask = ((indices >> bit) & 1).astype(bool)
    u = C(I(np.where(mask, candidate.re.lo, u.re.lo), np.where(mask, candidate.re.hi, u.re.hi)),
          I(np.where(mask, candidate.im.lo, u.im.lo), np.where(mask, candidate.im.hi, u.im.hi)))
    power = power*power
check('all root-of-unity boxes finite and narrow',
      all(np.all(np.isfinite(v)) for v in [u.re.lo,u.re.hi,u.im.lo,u.im.hi])
      and np.max(u.re.hi-u.re.lo) < 1e-8 and np.max(u.im.hi-u.im.lo) < 1e-8,
      max(np.max(u.re.hi-u.re.lo),np.max(u.im.hi-u.im.lo)), '<1e-8')

root_boxes = [isolate(k) for k in range(16)]
x, R, U = I.rational(Q(-5,4)), I.rational(Q(11,8)), I.rational(Q(121,64))
rows = []
for q in [1,2,4,8]:
    n = 12*q+3
    h, rho = I.rational(Q(27,10*n)), I.rational(Q(27,100*n))
    lam = pi/h

    def W(a):
        val = ci(x)/a
        for j in range(1,n):
            t = I.rational(Q(j,n))
            val = val*((ci(x)-u*ci(t))/(a-u*ci(t))) * ((u*ci(U)-a*ci(t))/(u*ci(U)-ci(x*t)))
        return val

    f = W(ci(-R))-1
    weights = []
    for k in range(2*q):
        lo, hi = root_boxes[k]
        s = I(I.rational(lo).lo,I.rational(hi).hi)
        y = h*s
        v = rho.square()+y.square()
        weight = ((1+rho*lam)/rho)*v/(rho+lam*v)
        check(f'q={q} k={k} positive weight', float(weight.lo)>1 and float(weight.hi)<13/3,
              [float(weight.lo),float(weight.hi)], '(1,13/3)')
        weights.append(dict(k=k, lower=float(weight.lo),upper=float(weight.hi)))
        f = f-ci(weight)*(W(C(x,y))+W(C(x,-y)))
    sq = f.abs2()
    # Sums of positive binary64 terms: pairwise/tree ordering is immaterial
    # for the conservative sequential gamma_(N-1) relative-error bound.
    gamma = Q(N,2**52-N)
    sl, sh = float(np.sum(sq.lo)),float(np.sum(sq.hi))
    meanlo = Q.from_float(sl)/(1+gamma)/N
    meanhi = Q.from_float(sh)/(1-gamma)/N
    # Rational annulus bound: |g|<=4*n^2*175^(2n).
    M = 4*n*n*175**(2*n)
    rn = Q(9,10)**N
    alias = 2*M*rn/(1-rn)
    check(f'q={q} continuous alias bound', alias<Q(1,10**250),
          '2*(4*n^2*175^(2*n))*(9/10)^N/(1-(9/10)^N)', '<10^-250')
    lower, upper = meanlo-Q(1,10**250),meanhi+Q(1,10**250)
    # Decimal endpoints below are enclosing rational claims, checked exactly.
    candidates={1:(Q(3456,1000),Q(3458,1000)),2:(Q(3037,1000),Q(3040,1000)),
                4:(Q(2144,1000),Q(2148,1000)),8:(Q(1985,1000),Q(1990,1000))}
    nl,nh=candidates[q]
    check(f'q={q} full norm enclosure',nl*nl<lower<=upper<nh*nh,
          f'squared mean in [{float(lower):.17g},{float(upper):.17g}]',f'({nl},{nh}) squared')
    check(f'q={q} finite threshold fails',nl>1,nl,'>1>exp(-n/100)')
    rows.append(dict(q=q,n=n,grid_size=N,weights=weights,
                     sample_squared_lower=sq.lo.tolist(),sample_squared_upper=sq.hi.tolist(),
                     squared_mean_lower_exact=str(lower),squared_mean_upper_exact=str(upper),
                     alias_bound_formula='2*(4*n^2*175^(2*n))*(9/10)^N/(1-(9/10)^N)',
                     alias_upper='1/10^250',norm_interval=[str(nl),str(nh)],
                     exponent_interval=['-log('+str(nh)+')/'+str(n),'-log('+str(nl)+')/'+str(n)],
                     mean_width=float(upper-lower)))
    print(f'q={q}, n={n}: norm in ({float(nl)}, {float(nh)}); required exponent>0.01; '
          f'squared-mean width={float(upper-lower):.3g}',flush=True)

path=Path(__file__).with_suffix('.json')
report=dict(kind='outward interval full continuous Robin residual certificate',
            source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            numpy_version=np.__version__,binary64=np.finfo(np.float64).bits,
            pi_interval=[str(v) for v in PI],
            exact_root_intervals=[[str(v) for v in box] for box in root_boxes],
            angular_grid_size=N,checks=checks,failures=failures,rows=rows,
            qualification='Finite q only; neither an asymptotic-rate obstruction nor arbitrary-weight lower bound.')
path.write_text(json.dumps(report,indent=2)+'\n')
print(f'{len(checks)} checks; failures={failures}; full certificate: {path}')
if failures:
    raise SystemExit(1)
