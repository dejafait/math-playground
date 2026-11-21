"""One bounded directed-interval implementation of the approved fixed pair.

No floating-point special functions, FFT/SVD, assumed zero list or RH input.
The accompanying canonical calculation note documents all analytic errors.
Full coefficients, quadrature cells, contour boxes and norm data go to JSON.
"""
import argparse
import decimal
import json
import math
import platform
from decimal import Decimal as D, Context, ROUND_FLOOR, ROUND_CEILING, ROUND_HALF_EVEN
from fractions import Fraction
from pathlib import Path

PREC = 75
DN = Context(prec=PREC, rounding=ROUND_FLOOR, Emin=-999999999, Emax=999999999)
UP = Context(prec=PREC, rounding=ROUND_CEILING, Emin=-999999999, Emax=999999999)
RN = Context(prec=PREC, rounding=ROUND_HALF_EVEN, Emin=-999999999, Emax=999999999)
decimal.setcontext(RN.copy())
BASE = Path(__file__).resolve().parent
CERT = BASE / 'fixed-pair-certificate-431.json'


class I:
    def __init__(self, lo=0, hi=None):
        self.lo, self.hi = D(lo), D(lo if hi is None else hi)
        assert self.lo.is_finite() and self.hi.is_finite() and self.lo <= self.hi
    def __add__(self, x):
        x = iv(x)
        return I(DN.add(self.lo, x.lo), UP.add(self.hi, x.hi))
    __radd__ = __add__
    def __neg__(self):
        return I(self.hi.copy_negate(), self.lo.copy_negate())
    def __sub__(self, x):
        return self + (-iv(x))
    def __rsub__(self, x):
        return iv(x) - self
    def __mul__(self, x):
        x = iv(x)
        pairs = [(a, b) for a in (self.lo, self.hi) for b in (x.lo, x.hi)]
        return I(min(DN.multiply(a, b) for a, b in pairs),
                 max(UP.multiply(a, b) for a, b in pairs))
    __rmul__ = __mul__
    def __truediv__(self, x):
        x = iv(x)
        assert x.lo > 0 or x.hi < 0, 'division by zero interval'
        return self * I(DN.divide(D(1), x.hi), UP.divide(D(1), x.lo))
    def __rtruediv__(self, x):
        return iv(x) / self
    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        out, x = I(1), self
        while n:
            if n & 1:
                out = out*x
            n //= 2
            if n:
                x = x.square()
        return out
    def square(self):
        if self.lo >= 0:
            return I(DN.multiply(self.lo, self.lo), UP.multiply(self.hi, self.hi))
        if self.hi <= 0:
            return (-self).square()
        return I(0, max(UP.multiply(self.lo, self.lo), UP.multiply(self.hi, self.hi)))
    def exp(self):
        return I(RN.next_minus(RN.exp(self.lo)), RN.next_plus(RN.exp(self.hi)))
    def sqrt(self):
        assert self.lo >= 0
        return I(max(D(0), RN.next_minus(RN.sqrt(self.lo))), RN.next_plus(RN.sqrt(self.hi)))
    def mag(self):
        return max(self.lo.copy_abs(), self.hi.copy_abs())
    def lowabs(self):
        return max(D(0), self.lo, self.hi.copy_negate())
    def mid(self):
        return RN.divide(RN.add(self.lo, self.hi), D(2))
    def err(self, x):
        return max(UP.subtract(D(x), self.lo), UP.subtract(self.hi, D(x)))
    def pair(self):
        return [str(self.lo), str(self.hi)]


def iv(x):
    return x if isinstance(x, I) else I(x)


def sym(e):
    e = iv(e).mag()
    return I(e.copy_negate(), e)


class C:
    def __init__(self, re=0, im=0):
        self.re, self.im = iv(re), iv(im)
    def __add__(self, x):
        x = cv(x)
        return C(self.re+x.re, self.im+x.im)
    __radd__ = __add__
    def __neg__(self):
        return C(-self.re, -self.im)
    def __sub__(self, x):
        return self + (-cv(x))
    def __rsub__(self, x):
        return cv(x) - self
    def __mul__(self, x):
        x = cv(x)
        return C(self.re*x.re-self.im*x.im, self.re*x.im+self.im*x.re)
    __rmul__ = __mul__
    def conj(self):
        return C(self.re, -self.im)
    def __truediv__(self, x):
        x = cv(x)
        z = self*x.conj()
        den = x.re.square()+x.im.square()
        return C(z.re/den, z.im/den)
    def mag(self):
        return (self.re.square()+self.im.square()).sqrt().hi
    def pair(self):
        return [self.re.pair(), self.im.pair()]
    def point(self):
        return [str(self.re.mid()), str(self.im.mid())]


def cv(x):
    return x if isinstance(x, C) else C(x)


def atan_recip(q):
    t, total = I(1)/q, I(0)
    power = t
    for n in range(180):
        total += ((-1)**n)*power/(2*n+1)
        power *= t.square()
    return total+sym(power/361)


PI = 16*atan_recip(5)-4*atan_recip(239)
assert PI.lo > 3 and PI.hi < 4


def expjet(q):
    f = [q[0].exp()]
    for j in range(1, len(q)):
        f.append(sum((k*q[k]*f[j-k] for k in range(1, j+1)), I(0))/j)
    return f


def build():
    # 128 cells on [0,2], halfwidth 1/128; Cauchy disk radius 1/8.
    cells, order, nj = 128, 24, 96
    h, d = I(1)/128, I(1)/8
    moments = [I(0) for _ in range(nj)]
    records = []
    for cell in range(cells):
        c = I(2*cell+1)/128
        e2 = [(2*c).exp()]
        for j in range(1, order+1):
            e2.append(e2[-1]*2/j)
        aa = [I(0) for _ in range(order+1)]
        for theta_n in range(1, 9):
            jet = [-PI*(theta_n**2)*v for v in e2]
            jet[0] += c/2
            jet[1] += I(1)/2
            aa = [x+y for x, y in zip(aa, expjet(jet))]
        v = (2*(c-d)).exp()*(1-2*d.square())
        ma = ((c+d)/2).exp()*(-3*v).exp()/(1-(-9*v).exp())
        # Normalized monomial u^(2n)/(4^n(2n)!), including its Taylor jet.
        mono = [I(1)]+[I(0) for _ in range(order)]
        mn = ma
        errs = []
        for n in range(nj):
            integ = I(0)
            for j in range(0, order+1, 2):
                coeff = sum((aa[l]*mono[j-l] for l in range(j+1)), I(0))
                integ += coeff*(h**j)/(j+1)
            err = 2*h*mn*((h/d)**(order+1))/(1-h/d)
            moments[n] += 2*h*integ+sym(err)
            errs.append(str(err.hi))
            den = 4*(2*n+2)*(2*n+1)
            mono = [(c.square()*mono[j]
                     +(2*c*mono[j-1] if j >= 1 else I(0))
                     +(mono[j-2] if j >= 2 else I(0)))/den
                    for j in range(order+1)]
            mn = mn*(c+d).square()/den
        records.append({'cell': cell, 'center': c.pair(), 'M_A': ma.pair(),
                        'moment_integral_error_upper': errs,
                        'A_Taylor_coefficients': [x.pair() for x in aa]})
        if cell % 32 == 31:
            print('coefficient cells', cell+1, '/', cells, flush=True)
    coeff = [(1-moments[0])/16]
    coeff += [(moments[n-1]-moments[n])/16 for n in range(1, nj)]
    coeff.append(moments[-1]/16)
    # Uniform |w|<=1600 errors NOT already contained in moment intervals.
    theta_tail = 2*I(1).exp()*I(-243).exp()*I(40).exp()/(1-I(-57).exp())
    # e^(2u)>=54(1+2(u-2)); u>=2, sqrt(|w|)/2<=20.
    assert I(4).exp().lo > 54
    u_tail = 2*I(-121).exp()/I('303.5')
    cosh_tail = (2*I(1).exp()*I(-3).exp()/(1-I(-9).exp())
                 *(I(40)**(2*nj))/math.factorial(2*nj)
                 /(1-I(1600)/((2*nj+1)*(2*nj+2))))
    eg = I(1601)/16*(theta_tail+u_tail+cosh_tail)
    data = {'precision': PREC, 'moment_count': nj, 'cells': cells, 'Taylor_order': order,
            'h': h.pair(), 'Cauchy_radius': d.pair(), 'pi': PI.pair(),
            'moments': [x.pair() for x in moments],
            'coefficients': [x.pair() for x in coeff], 'quadrature_cells': records,
            'uniform_disk_radius': 1600, 'theta_tail_J': theta_tail.pair(),
            'u_tail_J': u_tail.pair(), 'cosh_tail_J': cosh_tail.pair(),
            'uniform_G_error': eg.pair()}
    return coeff, eg, data


def load_coeff(data):
    return [I(*x) for x in data['coefficients']], I(*data['uniform_G_error'])


def peval(coeff, z):
    out = C()
    for a in reversed(coeff):
        out = out*z+a
    return out


def geval(coeff, eg, z):
    val = peval(coeff, z)
    return C(val.re+sym(eg), val.im+sym(eg))


def circle(rad, quadrant, t):
    out = C(1, t)/C(1, -t)*rad
    for _ in range(quadrant):
        out = C(-out.im, out.re)
    return out


def contour(coeff, eg, rad):
    # Polynomial Taylor jets at the center; tail via a disk of radius256.
    # Every center has modulus<=1280, so the disk is in |w|<=1536<1600.
    degree, base, maxdepth = 8, 128, 8
    mp = sum((I(a.mag())*(I(1600)**n) for n, a in enumerate(coeff)), I(0))
    records, vertices = [], []
    def segment(quadrant, left, right, depth):
        tl, tr = I(left.numerator)/left.denominator, I(right.numerator)/right.denominator
        tm = (tl+tr)/2
        z0 = circle(rad, quadrant, tm)
        zb = circle(rad, quadrant, I(tl.lo, tr.hi))
        delta = zb-z0
        ratio = I(delta.mag())/256
        assert ratio.hi < 1
        jet = [C() for _ in range(degree+1)]
        for a in reversed(coeff):
            for j in range(degree, 0, -1):
                jet[j] = jet[j]*z0+jet[j-1]
            jet[0] = jet[0]*z0+a
        val = jet[-1]
        for a in reversed(jet[:-1]):
            val = val*delta+a
        error = eg+mp*(ratio**(degree+1))/(1-ratio)
        val = C(val.re+sym(error), val.im+sym(error))
        ends = [geval(coeff, eg, circle(rad, quadrant, t)) for t in (tl, tr)]
        pts = [v.point() for v in ends]
        # Hull in the chosen exact decimal vertices as well as the curve.
        val = C(I(min(val.re.lo, *(D(p[0]) for p in pts)),
                  max(val.re.hi, *(D(p[0]) for p in pts))),
                I(min(val.im.lo, *(D(p[1]) for p in pts)),
                  max(val.im.hi, *(D(p[1]) for p in pts))))
        lower = max(val.re.lowabs(), val.im.lowabs())
        if lower <= 0:
            if depth == maxdepth:
                raise RuntimeError('contour enclosure failed at fixed depth cap')
            mid = (left+right)/2
            segment(quadrant, left, mid, depth+1)
            segment(quadrant, mid, right, depth+1)
            return
        vertices.append(pts[0])
        records.append({'quadrant': quadrant,
                        't': [str(left), str(right)], 'center_w': z0.pair(),
                        'w_box': zb.pair(), 'G_box': val.pair(),
                        'point_enclosures': [v.pair() for v in ends],
                        'vertices': pts, 'G_lower': str(lower),
                        'Taylor_tail_plus_G_error': error.pair(), 'depth': depth})
    for quadrant in range(4):
        for index in range(base):
            segment(quadrant, Fraction(index, base), Fraction(index+1, base), 0)
        print('contour radius', rad, 'quadrants', quadrant+1, '/4', flush=True)
    # Shared endpoint values must agree; otherwise hull both at junctions.
    for i, rec in enumerate(records):
        assert rec['vertices'][1] == records[(i+1) % len(records)]['vertices'][0]
    winding = 0
    crossings = []
    for i, rec in enumerate(records):
        (x, y), (xx, yy) = [[Fraction(v) for v in p] for p in rec['vertices']]
        cross = x*yy-y*xx
        inc = int(y <= 0 < yy and cross > 0)-int(yy <= 0 < y and cross < 0)
        if (y <= 0 < yy or yy <= 0 < y) and cross == 0:
            raise RuntimeError('polygon hits origin')
        winding += inc
        if inc:
            crossings.append({'segment': i, 'increment': inc})
    return {'radius_w': rad, 'segments': records, 'count_with_multiplicity': winding,
            'nonvanishing': True, 'G_boundary_lower': str(min(D(x['G_lower']) for x in records)),
            'crossings': crossings, 'polynomial_global_magnitude_upper': str(mp.hi)}


def root_and_residue(coeff, eg):
    lo, hi = D(-800), D(-799)
    trials = []
    for _ in range(70):
        lv, hv = geval(coeff, eg, C(lo)).re, geval(coeff, eg, C(hi)).re
        assert lv.lo*hv.lo < 0 and (lv.lo > 0 or lv.hi < 0) and (hv.lo > 0 or hv.hi < 0)
        if UP.subtract(hi, lo) < D('1e-18'):
            break
        mid = RN.divide(RN.add(lo, hi), D(2))
        mv = geval(coeff, eg, C(mid)).re
        trials.append({'w': str(mid), 'G': mv.pair()})
        if mv.lo <= 0 <= mv.hi:
            break
        if (mv.lo > 0) == (lv.lo > 0):
            lo = mid
        else:
            hi = mid
    root = I(lo, hi)
    assert UP.subtract(hi, lo) < D('1e-17')
    deriv_coeff = [n*a for n, a in enumerate(coeff) if n]
    deriv = peval(deriv_coeff, C(root)).re+sym(eg/100)
    # k=1, F(alpha)=R G'(R alpha), d=alpha F(alpha).
    alpha = root/1024
    residue = alpha*1024*deriv
    return alpha, residue, {'root_w': root.pair(), 'endpoint_G': [lv.pair(), hv.pair()],
                            'alpha': alpha.pair(), 'G_prime': deriv.pair(),
                            'derivative_Cauchy_error': (eg/100).pair(),
                            'residue': residue.pair(), 'bisection': trials}


def sincos(x):
    # x in [0,pi/2]; factorial Taylor with a common absolute remainder.
    assert x.lo >= 0 and x.hi < 2
    xx = x.square()
    cs, sn, ct, st = I(1), x, I(1), x
    for k in range(1, 65):
        ct = -ct*xx/((2*k)*(2*k-1))
        st = -st*xx/((2*k)*(2*k+1))
        cs += ct
        sn += st
    err = (I(2)**130)/math.factorial(130)
    return sn+sym(err), cs+sym(err)


def fourier(coeff, eg, alpha, residue, outer):
    N, L = 192, 1024
    sigma, a, rho = I(5)/4, I(4)/5, I(9)/10
    assert alpha.mag() < a.lo
    m_sigma = I(outer['G_boundary_lower'])/(sigma+a)
    mb = (1+a/sigma)/m_sigma
    ah, dh = alpha.mid(), residue.mid()
    ej, ed = alpha.err(ah), residue.err(dh)
    sums = [C() for _ in range(N+1)]
    samples = []
    for j in range(L):
        quadrant, rem = divmod(j, L//4)
        sn, cs = sincos(2*PI*rem/L)
        z = C(cs, sn)
        for _ in range(quadrant):
            z = C(-z.im, z.re)
        val = geval(coeff, eg, z*1024)
        bv = (z-C(alpha))*(z-C(alpha))/(z*val)
        power = C(1)
        for n in range(N+1):
            sums[n] += bv*power
            power *= z.conj()
        samples.append({'j': j, 'z': z.pair(), 'G': val.pair(), 'b': bv.pair()})
        if j % 256 == 255:
            print('DFT samples', j+1, '/', L, flush=True)
    beta, epsilon, enclosures, aliases = [], [], [], []
    for n in range(1, N+1):
        # b has only the one negative power -1. n<=N<L-1 excludes that alias.
        alias = mb*(sigma**0)/(sigma**(n+L))/(1-I(1)/(sigma**L))
        val = sums[n]/L
        assert (val.im+sym(alias)).lo <= 0 <= (val.im+sym(alias)).hi
        enc = val.re+sym(alias)
        bh = enc.mid()
        beta.append(bh)
        epsilon.append(enc.err(bh))
        enclosures.append(enc.pair())
        aliases.append(alias.pair())
    h_b = sum((n*I(b).square() for n, b in enumerate(beta, 1)), I(0)).sqrt()
    q = I(1)/sigma.square()
    tn = (q**(N+1))*((N+1)-N*q)/(1-q).square()
    delta_b = (sum((n*I(e).square() for n, e in enumerate(epsilon, 1)), I(0))
               +mb.square()*tn).sqrt()
    t = rho-a
    ms = I(dh.copy_abs())/t
    es = I(ed)/t+I(dh.copy_abs())*ej/t.square()
    hb = ms*rho/(1-rho.square())
    db = es*rho/(1-rho.square())
    # Hatted rank-one U rows i=3,...,N; all hatted data are exact decimals.
    urows = []
    for i in range(3, N+1):
        row = I(0)
        for b in reversed(beta[i-1:]):
            row = row*I(ah)+b
        urows.append(row)
    gram_u = sum((u.square() for u in urows), I(0))
    gram_y = (I(ah)**4)/(1-I(ah).square())
    k_norm = I(dh.copy_abs())*(gram_u*gram_y).sqrt()
    error = delta_b*hb+h_b*db+delta_b*db
    norm = I(max(D(0), DN.subtract(k_norm.lo, error.hi)), UP.add(k_norm.hi, error.hi))
    return {'N': N, 'L': L, 'sigma': sigma.pair(), 'a': a.pair(), 'rho': rho.pair(),
            'm_sigma': m_sigma.pair(), 'M_b': mb.pair(), 'alpha_hat': str(ah),
            'residue_hat': str(dh), 'alpha_error': str(ej), 'residue_error': str(ed),
            'samples': samples, 'beta_enclosures': enclosures,
            'beta_hat': [str(x) for x in beta], 'epsilon': [str(x) for x in epsilon],
            'DFT_alias_errors': aliases, 'h_b': h_b.pair(), 'delta_b': delta_b.pair(),
            'M_S': ms.pair(), 'E_S': es.pair(), 'h_B': hb.pair(), 'delta_B': db.pair(),
            'T_N': tn.pair(), 'U_rows': [x.pair() for x in urows],
            'Gram_U': gram_u.pair(), 'Gram_Y': gram_y.pair(),
            'finite_norm': k_norm.pair(), 'full_product_error': error.pair(),
            'original_norm': norm.pair(), 'required_upper': '1',
            'decision': 'BELOW_ONE' if norm.hi < 1 else ('AT_LEAST_ONE' if norm.lo >= 1 else 'INCONCLUSIVE')}


def save(data):
    CERT.write_text(json.dumps(data, indent=2)+'\n')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--phase', choices=['coeff', 'count', 'norm'], required=True)
    args = parser.parse_args()
    data = json.loads(CERT.read_text()) if CERT.exists() else {
        'step': 431, 'pair': [2, 1024], 'status': 'UNFINISHED', 'failures': [],
        'runtime': {'python': platform.python_version(), 'decimal': decimal.__version__,
                    'libmpdec': decimal.__libmpdec_version__, 'ball_library': 'directed Decimal endpoints; no FLINT'},
        'scope': 'known-method specialization; not independent proof audit or RH result'}
    try:
        if args.phase == 'coeff':
            assert 'evaluation' not in data, 'coefficient build already exists'
            _, _, data['evaluation'] = build()
        elif args.phase == 'count':
            coeff, eg = load_coeff(data['evaluation'])
            data['inner_contour'] = contour(coeff, eg, 1024)
            save(data)
            if data['inner_contour']['count_with_multiplicity'] != 1:
                data['status'] = 'ADMISSIBILITY_FAILURE'
            else:
                data['outer_contour'] = contour(coeff, eg, 1280)
                assert data['outer_contour']['count_with_multiplicity'] == 1
                _, _, data['zero'] = root_and_residue(coeff, eg)
                data['status'] = 'ADMISSIBILITY_AND_ROOT_CERTIFIED_PENDING_AUDIT'
        else:
            assert data['inner_contour']['count_with_multiplicity'] == 1
            assert data['outer_contour']['count_with_multiplicity'] == 1
            coeff, eg = load_coeff(data['evaluation'])
            alpha, residue = I(*data['zero']['alpha']), I(*data['zero']['residue'])
            data['norm'] = fourier(coeff, eg, alpha, residue, data['outer_contour'])
            data['status'] = data['norm']['decision']+'_PENDING_AUDIT'
    except Exception as exc:
        data['failures'].append({'phase': args.phase, 'type': type(exc).__name__, 'message': str(exc)})
        data['status'] = 'UNFINISHED_WITH_FAILURE'
        save(data)
        raise
    save(data)
    summary = {'status': data['status'], 'phase': args.phase, 'certificate': str(CERT),
               'failures': data['failures']}
    if 'norm' in data:
        summary.update(actual_norm=data['norm']['original_norm'], required_upper='1')
    if 'inner_contour' in data:
        summary['actual_count'] = data['inner_contour']['count_with_multiplicity']
        summary['required_count'] = 1
    if 'evaluation' in data:
        summary['uniform_G_error'] = data['evaluation']['uniform_G_error']
    print(json.dumps(summary, indent=2), flush=True)


if __name__ == '__main__':
    main()
