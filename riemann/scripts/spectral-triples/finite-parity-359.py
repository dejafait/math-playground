"""One fixed CCM cell; Decimal intervals, integral series and LDL inertia.

No floating eigensolver is used for certification. See the canonical
write-up for the integral expansion and all analytic remainder bounds.
Run with python3 (stdlib only). Output contains every entry and LDL pivot.
"""
from decimal import Decimal as D, Context, ROUND_FLOOR, ROUND_CEILING
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import time

PREC = 170
LO = Context(prec=PREC, rounding=ROUND_FLOOR)
HI = Context(prec=PREC, rounding=ROUND_CEILING)


class I:
    __slots__ = ('lo', 'hi')

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
        lows = [LO.multiply(x, y) for x in (a.lo, a.hi) for y in (b.lo, b.hi)]
        highs = [HI.multiply(x, y) for x in (a.lo, a.hi) for y in (b.lo, b.hi)]
        return I(min(lows), max(highs))

    __rmul__ = __mul__

    def __truediv__(a, b):
        b = I(b)
        if b.lo <= 0 <= b.hi:
            raise ArithmeticError('interval divisor contains zero')
        return a * I(LO.divide(D(1), b.hi), HI.divide(D(1), b.lo))

    def __rtruediv__(a, b):
        return I(b) / a

    def __pow__(a, n):
        if n < 0:
            return I(1) / (a ** (-n))
        out = I(1)
        while n:
            if n & 1:
                out = out * a
            a = a * a
            n //= 2
        return out

    def ln(a):
        # Decimal ln/sqrt are correctly rounded to nearest independently of
        # the context rounding mode. One adjacent value encloses each end.
        return I(LO.next_minus(LO.ln(a.lo)), HI.next_plus(HI.ln(a.hi)))

    def sqrt(a):
        return I(LO.next_minus(LO.sqrt(a.lo)), HI.next_plus(HI.sqrt(a.hi)))

    def exp(a):
        return I(LO.next_minus(LO.exp(a.lo)), HI.next_plus(HI.exp(a.hi)))

    def save(a):
        return [str(a.lo), str(a.hi)]

    def absupper(a):
        return max(a.lo.copy_abs(), a.hi.copy_abs())


def rat(q):
    return I(q.numerator) / q.denominator


def pm(a, e):
    e = I(e).absupper()
    return I(LO.subtract(a.lo, e), HI.add(a.hi, e))


def atan_recip(k):
    z = I(1) / k
    z2 = z*z
    power = z
    val = I(0)
    for n in range(400):
        val += power * (1 if n % 2 == 0 else -1) / (2*n+1)
        power *= z2
    return pm(val, power / 801)


def bernoulli(n):
    a = [F(0)] * (n+1)
    out = []
    for m in range(n+1):
        a[m] = F(1, m+1)
        for j in range(m, 0, -1):
            a[j-1] = j*(a[j-1]-a[j])
        out.append(a[0])
    return out


def sincos_reduced(turns):
    # sin/cos(2*pi*turns), reduce using an exactly selected integer;
    # nearest-midpoint selection influences only performance, not validity.
    center = LO.divide(LO.add(turns.lo, turns.hi), D(2))
    shift = int(center.to_integral_value())
    x = 2*PI*(turns-shift)
    assert x.absupper() < 4
    x2 = x*x
    st, ct = x, I(1)
    ss, cc = st, ct
    for k in range(1, 260):
        st = -st*x2/((2*k)*(2*k+1))
        ct = -ct*x2/((2*k-1)*(2*k))
        ss += st
        cc += ct
    se = st*x2/(520*521)
    ce = ct*x2/(519*520)
    # Subsequent absolute ratios < 16/(520*519) < 1/2.
    return pm(ss, 2*se), pm(cc, 2*ce)


N, K, R, EM = 120, 512, 160, 80
started = time.monotonic()
PI = 16*atan_recip(5)-4*atan_recip(239)
L = I(13).ln()
BB = bernoulli(2*EM)
fac = [1]
for k in range(1, 2*EM+1):
    fac.append(fac[-1]*k)
coef = [None]+[rat(BB[2*r]/fac[2*r]) for r in range(1, EM+1)]
B0 = I(2*K) + I(1)/2


def tail(s):
    """Enclose sum_{k=K}^infty (2k+1/2)^(-s), integer s>=2."""
    val = B0**(1-s)/(2*(s-1)) + B0**(-s)/2
    rising = 1
    prev = 0
    for r in range(1, EM+1):
        for j in range(prev, 2*r-1):
            rising *= s+j
        prev = 2*r-1
        term = coef[r]*(2**(2*r-1))*rising*B0**(-(s+2*r-1))
        if r < EM:
            val += term
        else:
            # Include the mth EM term conceptually, bound its integral
            # remainder by its magnitude, then omit it: two term losses.
            val = pm(val, 2*term)
    return val


TAIL = {s: tail(s) for s in range(2, 2*R+4)}
print('constants and inverse-power tails enclosed', flush=True)
# Euler--Maclaurin expansion for gamma, remainder bounded by next term.
GAMMA = sum((I(1)/j for j in range(1, K+1)), I(0))-I(K).ln()-I(1)/(2*K)
for r in range(1, EM):
    GAMMA += rat(BB[2*r]/(2*r))*I(K)**(-2*r)
GAMMA = pm(GAMMA, 2*rat(BB[2*EM]/(2*EM))*I(K)**(-2*EM))

# Terms exp(-(2k+1/2)L) have exact ratio 13^-2.
e0 = I(1)/I(13).sqrt()
es = [e0*I(169)**(-k) for k in range(K)]
assert (B0*L*(-1)).exp().hi < D('1e-1100')
EERROR = I('1e-1090')  # covers all omitted exponential tails, see proof
BASE = I(0)
for k in range(K):
    b = I(2*k)+I(1)/2
    BASE += (1-es[k])/b-(1-es[k]/I(13).sqrt())/(b+I(1)/2)
for r in range(R):
    BASE += ((-1)**r)*I(1)/I(2)**(r+1)*TAIL[r+2]
BASE = pm(BASE, I(1)/I(2)**(R+1)*TAIL[R+2]+EERROR)

freqs = []
for n in range(N+1):
    a = 2*PI*n/L
    a2 = a*a
    ss, cc, dd = I(0), I(0), I(0)
    for k in range(K):
        b = I(2*k)+I(1)/2
        den = b*b+a2
        ss += a*(1-es[k])/den
        cc -= a2*(1-es[k])/(b*den)
        dd += (1-es[k])*(b*b-a2)/(den*den)-L*es[k]*b/den
    power = I(1)
    for r in range(R):
        ss += a*power*TAIL[2*r+2]
        cc -= a2*power*TAIL[2*r+3]
        dd += (2*r+1)*power*TAIL[2*r+2]
        power *= -a2
    zmax = a2/(B0*B0)
    assert zmax.hi < 1
    abs_power = I(1) if R == 0 else (a2**R)
    ss = pm(ss, a*abs_power*TAIL[2*R+2]+EERROR)
    cc = pm(cc, a2*abs_power*TAIL[2*R+3]+EERROR)
    drem = abs_power*TAIL[2*R+2]*((2*R+1)/(1-zmax)+2*zmax/(1-zmax)**2)
    dd = pm(dd, drem+EERROR)
    freqs.append((ss, cc, dd))
    if n % 30 == 0:
        print('integral frequencies enclosed through', n, flush=True)

POINT = 32*L*(((L/4).exp()-(-L/4).exp())/2)**2
DIAG = GAMMA+(4*PI*I(6)/7).ln()
primepowers = [(2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3),(11,11),(13,13)]
prime_data = []
for k,p in primepowers:
    t = I(k).ln()
    trig = [sincos_reduced(n*t/L) for n in range(-N,N+1)]
    prime_data.append((t, I(p).ln()/I(k).sqrt(), trig))


def sineint(n):
    return freqs[abs(n)][0]*(1 if n >= 0 else -1)


def entry(n,m):
    pn = L*L+16*PI*PI*n*n
    pm_ = L*L+16*PI*PI*m*m
    point = POINT*(L*L-16*PI*PI*n*m)/(pn*pm_)
    if n == m:
        _,c,d = freqs[abs(n)]
        arch = DIAG+2*(c-d/L+BASE)
    else:
        arch = (sineint(m)-sineint(n))/(PI*(n-m))
    val = point-arch
    for t,w,trig in prime_data:
        q = (trig[m+N][0]-trig[n+N][0])/(PI*(n-m)) if n != m else 2*(1-t/L)*trig[n+N][1]
        val -= w*q
    return val


# Build the full signed matrix, without relying on parity to drop terms.
A = [[None]*(2*N+1) for _ in range(2*N+1)]
for n in range(-N,N+1):
    for m in range(n,N+1):
        A[n+N][m+N] = A[m+N][n+N] = entry(n,m)
print('full signed matrix enclosed', flush=True)
root2 = I(2).sqrt()
EV = [[I(0) for _ in range(N+1)] for _ in range(N+1)]
OD = [[I(0) for _ in range(N)] for _ in range(N)]
EV[0][0] = A[N][N]
for j in range(1,N+1):
    EV[0][j] = EV[j][0] = (A[N][N+j]+A[N][N-j])/root2
    for k in range(1,N+1):
        EV[j][k] = (A[N+j][N+k]+A[N+j][N-k]+A[N-j][N+k]+A[N-j][N-k])/2
        OD[j-1][k-1] = (A[N+j][N+k]-A[N+j][N-k]-A[N-j][N+k]+A[N-j][N-k])/2

out = Path(__file__).with_suffix('.json')
report = dict(kind='rigorous fixed-cell interval inertia attempt', parameters=dict(N=N,K=K,R=R,EM=EM,precision=PREC),
              source_url='https://arxiv.org/html/2511.22755v1',
              script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              constants=dict(pi=PI.save(), L=L.save(), gamma=GAMMA.save(), base=BASE.save()),
              inverse_power_tails={str(s):x.save() for s,x in TAIL.items()},
              frequencies=[[v.save() for v in row] for row in freqs],
              full_matrix=[[v.save() for v in row] for row in A],
              even_matrix=[[v.save() for v in row] for row in EV],
              odd_matrix=[[v.save() for v in row] for row in OD],
              max_entry_width=str(max(HI.subtract(v.hi,v.lo) for row in A for v in row)),
              prime_powers=primepowers, inertia=[], failures=[], outcome='IN_PROGRESS')


def save():
    report['elapsed_seconds'] = time.monotonic()-started
    out.write_text(json.dumps(report,indent=2)+'\n')


save()
print('max entry width', report['max_entry_width'], 'saved', out, flush=True)


def inertia(mat, shift, name):
    M = [[I(x) for x in row] for row in mat]
    for j in range(len(M)):
        M[j][j] -= I(shift)
    pivots, neg = [], 0
    for k in range(len(M)):
        p = M[k][k]
        pivots.append(p.save())
        if p.lo <= 0 <= p.hi:
            result = dict(block=name,shift=shift,success=False,pivots=pivots,negative=neg,failed_pivot=k)
            report['inertia'].append(result)
            save()
            print(name, shift, 'INCONCLUSIVE at pivot',k,flush=True)
            return None
        neg += p.hi < 0
        for j in range(k+1,len(M)):
            mult = M[j][k]/p
            for i in range(j,len(M)):
                M[i][j] = M[j][i] = M[i][j]-mult*M[i][k]
    result = dict(block=name,shift=shift,success=True,pivots=pivots,negative=neg)
    report['inertia'].append(result)
    save()
    print(name,shift,'negative count',neg,flush=True)
    return neg


# Bounded logarithmic location of the first parity levels. No parameter sweep:
# every test is the same lambda,N and uses the same certified matrix.
found = None
for exponent in [55,51,52,53,54,56,57,58,59,50,60]:
    shift = f'1e-{exponent}'
    ev = inertia(EV,shift,'even')
    od = inertia(OD,shift,'odd')
    if ev is None or od is None:
        report['failures'].append('interval pivot overlap at shift '+shift)
        break
    if ev == 1 and od == 0:
        found = exponent
        break
if found is not None:
    # A separate lower shift must still have exactly one eigenvalue below it.
    a = f'5e-{found+1}'
    low = inertia(EV,a,'even')
    if low == 1:
        report['outcome'] = 'CERTIFIED_SIMPLE_EVEN'
        report['gap_lower'] = str(LO.subtract(D(f'1e-{found}'),D(a)))
        report['even_min_upper'] = a
        report['even_second_lower'] = f'1e-{found}'
        report['odd_min_lower'] = f'1e-{found}'
    else:
        report['failures'].append('second separating shift did not certify one even eigenvalue')
if report['outcome'] != 'CERTIFIED_SIMPLE_EVEN':
    report['outcome'] = 'INCONCLUSIVE'
    report['failures'].append('no strict even/odd spectral separation certified in bounded shift test')
save()
print('RESULT', report['outcome'], 'gap lower',report.get('gap_lower'), 'required >0', flush=True)
print('failures',report['failures'],'complete certificate',out,flush=True)
