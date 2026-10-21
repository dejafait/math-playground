"""Exact-rule quadrature bound via an interval-certified rho polynomial.

Integer fixed-point outward arithmetic; NumPy only proposes coefficients.
This does NOT enclose the stored binary64 Gauss nodes or transforms.
"""
import json
from fractions import Fraction as F
from pathlib import Path
import numpy as np

S = 10**80
ORDER = 24


class I:
    __slots__ = ('lo', 'hi')

    def __init__(self, lo, hi=None):
        self.lo, self.hi = lo, lo if hi is None else hi

    @classmethod
    def rational(cls, q):
        q = F(q)
        return cls(q.numerator*S//q.denominator,
                   -((-q.numerator*S)//q.denominator))

    def __add__(self, b):
        return I(self.lo+b.lo, self.hi+b.hi)

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, b):
        return self+-b

    def __mul__(self, b):
        z = [self.lo*b.lo, self.lo*b.hi, self.hi*b.lo, self.hi*b.hi]
        return I(min(z)//S, -((-max(z))//S))

    def __truediv__(self, b):
        assert b.lo > 0 or b.hi < 0
        z = [F(a*S, c) for a in (self.lo, self.hi) for c in (b.lo, b.hi)]
        mn, mx = min(z), max(z)
        return I(mn.numerator//mn.denominator,
                 -((-mx.numerator)//mx.denominator))

    def absolute_upper(self):
        return F(max(abs(self.lo), abs(self.hi)), S)


ZERO, ONE = I(0), I(S)


def exp_negative(x):
    """e^-x: alternating bounds at x/2^k <=1/8, then square."""
    assert x.lo >= 0
    k = 0
    while x.hi > S//8:
        x = x/I.rational(2)
        k += 1
    term, total = ONE, ONE
    for j in range(1, 61):
        term = term*x/I.rational(j)
        total = total-term if j % 2 else total+term
    # Alternating-series upper S_60 and lower S_61.
    lower = total-term*x/I.rational(61)
    result = I(lower.lo, total.hi)
    assert result.lo > 0
    for _ in range(k):
        result = result*result
    return result


def reciprocal_jet(a):
    out = [ONE/a[0]]
    for n in range(1, ORDER+1):
        total = ZERO
        for k in range(1, min(n, len(a)-1)+1):
            total = total+a[k]*out[n-k]
        out.append(-total/a[0])
    return out


def exponential_jet(q):
    out = [exp_negative(-q[0])]
    for n in range(1, ORDER+1):
        total = ZERO
        for k in range(1, n+1):
            total = total+I.rational(k)*q[k]*out[n-k]
        out.append(total/I.rational(n))
    return out


def quotient_jet(a, b):
    out = [a[0]/b[0]]
    for n in range(1, ORDER+1):
        total = a[n]
        for k in range(1, n+1):
            total = total-b[k]*out[n-k]
        out.append(total/b[0])
    return out


def rho_jet(center, halfwidth):
    c, l = I.rational(center), I.rational(halfwidth)
    square = [c*c, I.rational(2)*c*l, l*l]
    u = [I.rational(9)-square[0], -square[1], -square[2]]
    v = [square[0]-I.rational(F(25, 4)), square[1], square[2]]
    b1 = exponential_jet([-z for z in reciprocal_jet(u)])
    b2 = exponential_jet([-z for z in reciprocal_jet(v)])
    return quotient_jet(b1, [a+b for a, b in zip(b1, b2)])


def polynomial_jet(coefficients, center, halfwidth):
    """Full scaled Taylor polynomial by exact Chebyshev recurrence."""
    degree = len(coefficients)-1
    y, z = I.rational(4*center-11), I.rational(4*halfwidth)
    t0 = [ONE]+[ZERO]*degree
    t1 = [y, z]+[ZERO]*(degree-1)
    out = [coefficients[0]*a+coefficients[1]*b for a, b in zip(t0, t1)]
    two_y, two_z = I.rational(2)*y, I.rational(2)*z
    for j in range(2, degree+1):
        t2 = [ZERO]*(degree+1)
        for k in range(j+1):
            value = two_y*t1[k]-t0[k]
            if k:
                value = value+two_z*t1[k-1]
            t2[k] = value
            out[k] = out[k]+coefficients[j]*value
        t0, t1 = t1, t2
    return out


def record(q):
    q = F(q)
    # Decimal presentation rounded upward at 24 fractional places.
    scaled = -((-q.numerator*10**24)//q.denominator)
    sign = '-' if scaled < 0 else ''
    absolute = abs(scaled)
    return dict(numerator=str(q.numerator), denominator=str(q.denominator),
                decimal_upper=f'{sign}{absolute//10**24}.{absolute%10**24:024d}')


def main():
    degree, nodes = 200, 2048
    theta = np.pi*(np.arange(nodes)+0.5)/nodes
    x = 2.75+0.25*np.cos(theta)
    u, v = 9-x*x, x*x-25/4
    b1, b2 = np.exp(-1/u), np.exp(-1/v)
    proposed = 2/nodes*np.cos(np.arange(degree+1)[:, None]*theta)@(b1/(b1+b2))
    proposed[0] /= 2
    # Each coefficient is the exact dyadic represented by its float.
    exact = [F(float(z)) for z in proposed]
    coefficients = [I.rational(z) for z in exact]
    delta = F(1, 256)
    rows = []
    # Flat endpoint collars; 16 cells avoid a large absolute Taylor bound.
    # min(1/(6 delta)-1/(11/4-6 delta)) > 41; ratio <=e^-41.
    collar_ratio = exp_negative(I.rational(41)).absolute_upper()
    collar_error = collar_ratio/(1-collar_ratio)
    for endpoint, baseline in ((F(5, 2), 1), (F(3), 0)):
        for j in range(16):
            l = delta/32
            c = endpoint+(2*j+1)*l if baseline else endpoint-(2*j+1)*l
            p = polynomial_jet(coefficients, c, l)
            p[0] = p[0]-I.rational(baseline)
            bound = sum(z.absolute_upper() for z in p)+collar_error
            rows.append(dict(case='endpoint_collar', center=str(c), halfwidth=str(l),
                             baseline=baseline, bound=record(bound)))
    # Rational geometric cells, covering the full remaining interval.
    left, end = F(5, 2)+delta, F(3)-delta
    while left < end:
        distance = min(left-F(5, 2), F(3)-left)
        width = min(distance/64, end-left)
        c, l = left+width/2, width/2
        r = min(c-F(5, 2), F(3)-c)/16
        assert l/r <= F(1, 4)
        a, p = rho_jet(c, l), polynomial_jet(coefficients, c, l)
        taylor = sum((a[j]-p[j]).absolute_upper() for j in range(ORDER+1))
        polynomial_tail = sum(z.absolute_upper() for z in p[ORDER+1:])
        remainder = F(I.rational(2*(l/r)**(ORDER+1)/(1-l/r)).hi, S)
        bound = taylor+polynomial_tail+remainder
        rows.append(dict(case='interior', center=str(c), halfwidth=str(l), radius=str(r),
                         taylor_residual=record(taylor), polynomial_tail=record(polynomial_tail),
                         analytic_remainder=record(remainder), bound=record(bound)))
        left += width
    maximum = max(F(int(z['bound']['numerator']), int(z['bound']['denominator'])) for z in rows)
    required = F(1, 10**12)
    failures = [dict(cell=j, bound=z['bound']) for j, z in enumerate(rows)
                if F(int(z['bound']['numerator']), int(z['bound']['denominator'])) > required]
    # exp bound on Bernstein ellipse R=4. pi<22/7 => |frequency|<=88.
    # Transition A<=22, sup phase <=e^(165/4)<e^42<3^42.
    phase_error = F(2*3**42, 3*4**86)
    # Core A<=110; ellipse phase bound <e^207<3^207.
    core_error = F(2*3**207, 3*4**286)
    error_bounds = [2*maximum+2*(1+maximum)*phase_error+10*core_error,
                    6*maximum+6*(1+maximum)*phase_error+25*core_error]
    thresholds = [F(6, 10**12), F(9, 10**12)]
    result = dict(scope='Exact degree-144 four-panel Gauss rule, h=0,1, |n|<=224.',
                  arithmetic='Outward integer fixed point at scale 10^80; exact dyadic proposed coefficients.',
                  rho_polynomial_degree=degree, taylor_order=ORDER,
                  rho_coefficients=[record(q) for q in exact], cells=rows,
                  cell_count=len(rows), rho_residual_upper=record(maximum),
                  required_rho_residual=record(required), rho_failures=failures,
                  phase_polynomial_degree=86, phase_residual_upper=record(phase_error),
                  core_phase_degree=286, core_residual_upper=record(core_error),
                  quadrature_error_upper=[record(q) for q in error_bounds],
                  required_quadrature_error=[record(q) for q in thresholds],
                  exact_quadrature_checks_passed=all(a <= b for a, b in zip(error_bounds, thresholds)),
                  stored_binary64_coefficient_error_certified=False,
                  retained_sign_certified=False,
                  unresolved=['Stored nodes/weights, rho and phase evaluations and transform summation',
                              'L035 sensitivity enclosure and tensor arithmetic',
                              'Other Ward terms and nonlinear forest compensation'])
    path = Path(__file__).with_name('exact-fourier-quadrature-certificate.json')
    path.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(dict(cell_count=len(rows), rho_residual_upper=record(maximum)['decimal_upper'],
                         rho_failure_count=len(failures),
                         actual_bounds=[record(q)['decimal_upper'] for q in error_bounds],
                         required_bounds=[str(q) for q in thresholds],
                         passed=result['exact_quadrature_checks_passed'], path=str(path))))


if __name__ == '__main__':
    main()
