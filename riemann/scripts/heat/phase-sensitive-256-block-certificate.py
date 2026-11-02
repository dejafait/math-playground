#!/usr/bin/env python3
"""One actual-phase 256-index block and both resultant charges.

Exact rational interval arithmetic; prior audited corner inputs are reused.
No source transport decimal, partial-cell fall or coefficient replay is used.
Analytic qualifications and the signed comparison are stated in C499c.
"""
from decimal import Decimal, localcontext, ROUND_CEILING, ROUND_FLOOR
from fractions import Fraction as F
from hashlib import sha256
from math import isqrt
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
OUT = HERE / 'phase-sensitive-256-block-certificate.json'
GRID, LOG_TERMS, EXP_DEGREE = 10**60, 100, 180
checks, evaluations = [], []
report = dict(scope='One actual-phase 256-index endpoint; no uniform transport.', method='Exact rational outward intervals; elementary series and complete finite product identities.')

def down(a):
    return F(a.numerator*GRID//a.denominator, GRID)


def up(a):
    return -down(-a)


class Box:
    def __init__(self, lo, hi=None):
        self.lo, self.hi = F(lo), F(lo if hi is None else hi)
        if self.lo > self.hi:
            raise ValueError('reversed interval')

    def __add__(self, other):
        other = box(other)
        return Box(down(self.lo+other.lo), up(self.hi+other.hi))

    __radd__ = __add__

    def __neg__(self):
        return Box(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + -box(other)

    def __rsub__(self, other):
        return box(other) + -self

    def __mul__(self, other):
        other = box(other)
        v = [a*b for a in (self.lo, self.hi) for b in (other.lo, other.hi)]
        return Box(down(min(v)), up(max(v)))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = box(other)
        if other.lo*other.hi <= 0:
            raise ValueError('zero in denominator interval')
        return self * Box(down(1/other.hi), up(1/other.lo))

    def __rtruediv__(self, other):
        return box(other)/self


def box(a):
    return a if isinstance(a, Box) else Box(a)


def encode(a):
    if isinstance(a, F):
        return dict(numerator=str(a.numerator), denominator=str(a.denominator))
    if isinstance(a, Box):
        return dict(lower=encode(a.lo), upper=encode(a.hi))
    if isinstance(a, (list, tuple)):
        return [encode(v) for v in a]
    if isinstance(a, dict):
        return {k: encode(v) for k, v in a.items()}
    return a


def rat(a):
    n, d = int(a['numerator']), int(a['denominator'])
    if d <= 0:
        raise ValueError('nonpositive rational denominator')
    return F(n, d)


def read(a):
    return Box(rat(a['lower']), rat(a['upper']))


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def check(name, passed, actual, required):
    checks.append(dict(name=name, passed=bool(passed), actual=encode(actual),
                       required=encode(required)))
    if not passed:
        raise ValueError(name)


def log_unit(v):
    if not 1 <= v <= 2:
        raise ValueError('logarithm range reduction failed')
    z = (v-1)/(v+1)
    z2, power, total = z*z, box(z), Box(0)
    for j in range(LOG_TERMS):
        total = total + power/(2*j+1)
        power = power*z2
    tail = 2*power.hi/((2*LOG_TERMS+1)*(1-z2))
    ans = Box(down(2*total.lo), up(2*total.hi+tail))
    evaluations.append(dict(kind='log_unit', v=v, z=z, terms=LOG_TERMS,
                            half_sum=total, first_omitted_power=power,
                            tail_upper=tail, enclosure=ans))
    return ans


def exp_exact(a):
    u, term, total = abs(a), Box(1), Box(1)
    if not u < EXP_DEGREE+2:
        raise ValueError('exponential tail ratio invalid')
    for j in range(1, EXP_DEGREE+1):
        term = term*u/j
        total = total + term
    ratio = u/(EXP_DEGREE+2)
    tail = term.hi*u/(EXP_DEGREE+1)/(1-ratio)
    positive = Box(total.lo, up(total.hi+tail))
    ans = positive
    if a < 0:
        ans = Box(1)/positive
    evaluations.append(dict(kind='exp', argument=a, degree=EXP_DEGREE,
                            sum=total, last_term=term, subsequent_ratio_cap=ratio,
                            tail_upper=tail, positive_enclosure=positive,
                            enclosure=ans))
    return ans


def contains(outer, inner):
    return outer.lo <= inner.lo <= inner.hi <= outer.hi


def log_exact(a):
    if a <= 0:
        raise ValueError('nonpositive log argument')
    k, v = 0, F(a)
    while v >= 2:
        v /= 2
        k += 1
    while v < 1:
        v *= 2
        k -= 1
    return k*LOG2+log_unit(v)


def log_box(a):
    return Box(log_exact(a.lo).lo, log_exact(a.hi).hi)


def exp_box(a):
    return Box(exp_exact(a.lo).lo, exp_exact(a.hi).hi)


def sqrt_box(a):
    if a.lo < 0:
        raise ValueError('negative square root argument')
    l = isqrt(a.lo.numerator*GRID*GRID//a.lo.denominator)
    h = isqrt(a.hi.numerator*GRID*GRID//a.hi.denominator)+1
    return Box(F(l, GRID), F(h, GRID))


class Complex:
    def __init__(self, re=0, im=0):
        self.re, self.im = box(re), box(im)

    def __add__(self, other):
        other = complex_box(other)
        return Complex(self.re+other.re, self.im+other.im)

    __radd__ = __add__

    def __neg__(self):
        return Complex(-self.re, -self.im)

    def __sub__(self, other):
        return self+-complex_box(other)

    def __rsub__(self, other):
        return complex_box(other)+-self

    def __mul__(self, other):
        other = complex_box(other)
        return Complex(self.re*other.re-self.im*other.im,
                       self.re*other.im+self.im*other.re)

    __rmul__ = __mul__

    def conj(self):
        return Complex(self.re, -self.im)

    def __truediv__(self, other):
        other = complex_box(other)
        den = square(other.re)+square(other.im)
        if den.lo <= 0:
            raise ValueError('complex denominator may vanish')
        num = self*other.conj()
        return Complex(num.re/den, num.im/den)

    def __rtruediv__(self, other):
        return complex_box(other)/self

    def modulus(self):
        return sqrt_box(square(self.re)+square(self.im))


def complex_box(a):
    return a if isinstance(a, Complex) else Complex(a)


def square(a):
    vals = [a.lo*a.lo, a.hi*a.hi]
    return Box(0 if a.lo <= 0 <= a.hi else down(min(vals)), up(max(vals)))


def cencode(a):
    return dict(real=a.re, imaginary=a.im, modulus=a.modulus())


def cis(phase, label):
    # Any integer is valid; certify a small reduced interval afterwards.
    mid, period_mid = (phase.lo+phase.hi)/2, PI.lo+PI.hi
    turns = (mid/period_mid+F(1, 2)).__floor__()
    r = phase-turns*2*PI
    radius = max(abs(r.lo), abs(r.hi))
    if radius > 4:
        raise ValueError('trig reduction failed')
    sn, cs = Box(0), Box(0)
    term = Box(1)
    for k in range(160):
        if k % 4 == 0:
            cs += term
        elif k % 4 == 1:
            sn += term
        elif k % 4 == 2:
            cs -= term
        else:
            sn -= term
        term = term*r/(k+1)
    # Both displayed polynomials are Taylor polynomials through degree 159.
    # Real derivative magnitudes <=1 give the Lagrange remainder below.
    from math import factorial
    tail = up(radius**160/factorial(160))
    sn, cs = sn+Box(-tail, tail), cs+Box(-tail, tail)
    norm2 = square(sn)+square(cs)
    check('unit phase '+label, norm2.lo <= 1 <= norm2.hi, norm2, 1)
    evaluations.append(dict(kind='cis', label=label, phase=phase,
                            turns=turns, reduced=r, degree=159,
                            tail_upper=tail, sine=sn, cosine=cs))
    return Complex(cs, sn)


def run():
    global LOG2, PI
    cp, ap = HERE/'fixed-corner-two-charge.json', HERE/'l499-certificate-audit.json'
    corner, audit = [json.loads(p.read_text()) for p in (cp, ap)]
    report['inputs'] = [dict(path=p.name, sha256=digest(p)) for p in (cp, ap)]
    check('corner retained by independent audit',
          [r['sha256'] for r in audit['inputs'] if r['path'] == cp.name] == [digest(cp)],
          digest(cp), 'audited corner hash')
    for row in audit['inputs']:
        check('audited input unchanged '+row['path'], digest(HERE/row['path']) == row['sha256'],
              digest(HERE/row['path']), row['sha256'])
    t, X, n, N = F('.16836'), F('6000284561421.5'), 691004, 691260
    ell0, cap = F('24.18022820120389'), F('.500000000001')
    eps = F('.0000006')
    eps1 = (eps+F('.0000013'))*F('8.770232')/F('.14142')
    r0 = F(14176540015048665224252705167939023,
           33554432000000000000000000000000000000)
    PI = read(corner['elementary_inputs']['pi'])
    LX = read(corner['elementary_inputs']['L'])
    sigmaX = read(corner['elementary_inputs']['sigma'])
    LOG2 = log_unit(F(2))
    b = corner['bounds']
    R0, J0, D0 = [read(b[k]) for k in ('R', 'Jplus', 'product_derivative_cap')]
    check('exact reserve', rat(b['reserve_lower']) == r0, rat(b['reserve_lower']), r0)
    expected = dict(x=X, t=t, N=n, ell0=ell0, cap=cap, epsilon=eps,
                    epsilon_1=eps1, grid_denominator=str(10**50))
    check('exact inherited parameters', corner['parameters'] == encode(expected),
          corner['parameters'], expected)
    check('block length', N-n == 256, N-n, 256)
    coeff = F(N*N)-t/16
    Y = 4*PI*coeff
    domain_L = LX+(Y-X)/X
    check('closed analytic domain', Y.lo > X and t*domain_L.hi < F('5.17'),
          dict(Y=Y, tL=t*domain_L), 'Y>X; tL<5.17')
    check('symbolic canonical cutoff equality', coeff+t/16 == N*N,
          coeff+t/16, N*N)
    report['parameters'] = dict(t=t, X=X, old_N=n, new_N=N, count=N-n,
                                ell0=ell0, cap=cap, epsilon=eps, epsilon_1=eps1,
                                r0=r0, grid_denominator=str(GRID),
                                channels_per_primitive=2**63)
    # atan(1/Y) alternating expansion: u-u^3/3 encloses below, u above.
    u = 1/Y
    atan_small = Box((u-u*u*u/3).lo, u.hi)
    argz = PI/2-atan_small
    y2plus = 1+Y*Y
    Lstar = log_box(y2plus)/2-log_box(4*PI)
    alpha = Complex(Lstar/2-1/y2plus, argz/2-3*Y/y2plus)
    sigma, eta = F(1, 2)+t*alpha.re/2, Y/2+t*alpha.im/2
    Q = Y*(Y*Y+5)/(y2plus*y2plus)
    C = (7*Y*Y-5)/(y2plus*y2plus)
    aprime = Complex(C, -Q)
    nuprime = Complex(t*Q/4, F(1, 2)+t*C/4)
    theta = PI-argz/4+Y*(Lstar-1)/4+t*alpha.re*alpha.im/2
    phase = cis(theta, 'Theta')
    E, Elog, J, sumlogs = Complex(1), Complex(), Complex(), Box(0)
    prime_rows = []
    primes = [p for p in range(2, 308) if all(p % d for d in range(2, isqrt(p)+1))]
    check('complete prime set', len(primes) == 63 and
          [r['p'] for r in corner['prime_rows']] == primes, primes, 'all primes<=307')
    for row in corner['prime_rows']:
        p, h = row['p'], read(row['log_p'])
        w = exp_box(t*h*h/4-sigma*h)
        A = cis(-eta*h, 'prime '+str(p))*Complex(w)
        factor = 1-A
        check('nonzero Euler factor '+str(p), w.hi < 1, w, '<1')
        Elog = Elog*factor-E*Complex(h)*A
        E = E*factor
        J += Complex(h)*A/factor
        sumlogs += h
        prime_rows.append(dict(p=p, log_p=h, radius=w, A=cencode(A),
                               factor=cencode(factor)))
    rho = E.modulus()
    ell = 2*(alpha+Complex(t/2)*alpha*aprime).re-4*(nuprime*J).im
    check('actual positive phase floor', ell.lo > ell0, ell, ell0)
    check('sigma increases', sigma.lo > sigmaX.hi, sigma, sigmaX)
    DeltaS, DeltaL = Complex(), Complex()
    abs_weights, abs_G, abs_G_support, rows = Box(0), Box(0), Box(0), []
    # Complete positive-channel bound using h(m)<=1+2 log(m)/ell0.
    for j in range(n+1, N+1):
        h = log_exact(F(j))
        w = exp_box(t*h*h/4-sigma*h)
        a = cis(-eta*h, 'primitive '+str(j))*Complex(w)
        DeltaS += a
        DeltaL += Complex(h)*a
        # sum_d r_d log d = product(1+r_p)*sum_p log(p)r_p/(1+r_p).
        # J0 uses the larger 1-r_p denominator, so bounds that mean.
        absolute = w*R0*(1+2*(h+J0)/ell0)
        support_absolute = w*R0*(1+2*(h+sumlogs)/ell0)
        abs_weights += w
        abs_G += absolute
        abs_G_support += support_absolute
        rows.append(dict(j=j, log_j=h, radius=w, term=cencode(a),
                         absolute_channel_envelope=absolute,
                         maximum_support_envelope=support_absolute))
    Dz = Complex(rho)*phase*DeltaS
    Dw = Complex(rho)*phase*(DeltaL-J*DeltaS)
    Dg = Dz-Dw/Complex(ell)+Dw.conj()/Complex(ell)
    # Independent finite product-rule recurrence, without dividing Elog by E.
    phase_hat = phase*E.conj()/Complex(rho)
    Wdirect = phase_hat*(E*DeltaL+Elog*DeltaS)
    Zdirect = phase_hat*E*DeltaS
    Gdirect = Zdirect-Wdirect/Complex(ell)+Wdirect.conj()/Complex(ell)
    difference = Gdirect-Dg
    check('product-rule recurrence agrees',
          difference.re.lo <= 0 <= difference.re.hi and
          difference.im.lo <= 0 <= difference.im.hi,
          cencode(difference), 'both coordinates contain zero')
    BG = Dg.modulus()
    logN = rows[-1]['log_j']
    support = logN+sumlogs
    Anew = F(53, 3)+abs_weights
    Knew = R0*Anew*support
    QX = X*(X*X+5)/(1+X*X)**2
    CX = (7*X*X-5)/(1+X*X)**2
    Us = t*(QX+CX)*Knew/ell0
    Ur = R0*eps/2+2*(D0*eps+R0*eps1)/ell0
    total = BG+Us+Ur
    margin = r0-total
    report['domain'] = dict(Y=Y, L_upper=domain_L, symbolic_cutoff=N,
                            derivative_frozen_at=N, old_model_only_finite=True)
    report['actual_phase'] = dict(Lstar=Lstar, arg_z=argz, alpha=cencode(alpha),
                                  sigma=sigma, eta=eta, theta=theta, ell=ell,
                                  E=cencode(E), J=cencode(J), rho=rho,
                                  nu_prime=cencode(nuprime))
    report['prime_rows'], report['primitive_rows'] = prime_rows, rows
    report['increment'] = dict(DeltaS=cencode(DeltaS), DeltaL=cencode(DeltaL),
                               DeltaZ=cencode(Dz), DeltaW=cencode(Dw),
                               DeltaG=cencode(Dg), B_G=BG,
                               product_rule_Elog=cencode(Elog),
                               direct_recurrence_G=cencode(Gdirect),
                               recurrence_difference=cencode(difference))
    report['envelopes'] = dict(R0=R0, J0=J0, D0=D0, block_weight_sum=abs_weights,
                              new_primitive_sum_cap=Anew, full_output_log_cap=support,
                              new_Lhat_cap=Knew, Q_at_X=QX, C_at_X=CX,
                              charge_saddle_new=Us, charge_remainder_new=Ur,
                              absolute_channel_block=abs_G,
                              maximum_support_absolute_block=abs_G_support,
                              absolute_to_actual_ratio=abs_G/BG,
                              combined_cost=total, reserve_lower=r0, margin=margin)
    # Store predicate failures without aborting: a failed budget is informative.
    for name, passed, actual, required in [
        ('phase-sensitive strict reserve', total.hi < r0, total, r0),
        ('phase-sensitive saving', BG.hi < abs_G.lo, BG, abs_G),
        ('resolved budget width', total.hi-total.lo < F(1, 10**30),
         total.hi-total.lo, '<1e-30')]:
        checks.append(dict(name=name, passed=passed, actual=encode(actual), required=encode(required)))


try:
    run()
except Exception as exc:
    report['exception'] = f'{type(exc).__name__}: {exc}'
    if not checks or checks[-1]['passed']:
        checks.append(dict(name='execution completed', passed=False,
                           actual=report['exception'], required='no exception'))
failures = [r['name'] for r in checks if not r['passed']]
report.update(result='FAIL' if failures else 'PASS', checks=checks, failures=failures,
              elementary_evaluations=evaluations, script_sha256=digest(Path(__file__)))
OUT.write_text(json.dumps(encode(report), indent=2)+'\n')


def dec(a, upper=True):
    with localcontext() as ctx:
        ctx.prec = 26
        ctx.rounding = ROUND_CEILING if upper else ROUND_FLOOR
        return str(Decimal(a.numerator)/Decimal(a.denominator))


print(f"{report['result']}: {len(checks)} checks; failures={failures}")
if 'envelopes' in report:
    for key in ('absolute_channel_block', 'absolute_to_actual_ratio',
                'charge_saddle_new', 'charge_remainder_new', 'combined_cost'):
        print(f"{key} in [{dec(report['envelopes'][key].lo, False)}, {dec(report['envelopes'][key].hi)}]")
    print(f"B_G in [{dec(report['increment']['B_G'].lo, False)}, {dec(report['increment']['B_G'].hi)}]")
    print(f"required combined_cost < {dec(report['envelopes']['reserve_lower'], False)}")
    print(f"margin >= {dec(report['envelopes']['margin'].lo, False)}")
print(f'certificate={OUT.relative_to(HERE.parent.parent)}')
raise SystemExit(bool(failures))


