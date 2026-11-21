#!/usr/bin/env python
"""Certified finite inversion using elementary interval arithmetic (Python 2.7).

Run with the existing Anaconda interpreter; uses sympy.mpmath.iv only for
outward-rounded elementary operations, not its gamma/zeta/quadrature code.
Full node enclosures and all error budgets are saved; no samples prove signs.
"""
from __future__ import print_function, division
from fractions import Fraction as F
import hashlib
import json
import os
import platform
import sys
import time
from sympy import mpmath as mp

iv = mp.iv
iv.dps = 40
DEST = os.path.join(os.path.dirname(__file__), 'density-937.json')


def real(q):
    if isinstance(q, F):
        return iv.mpf(q.numerator) / q.denominator
    return iv.mpf(q)


def complex_(a=0, b=0):
    return iv.mpc(real(a), real(b))


def clog(z):
    return iv.mpc(iv.ln(abs(z)), iv.atan2(z.imag, z.real))


def cexp(z):
    r = iv.exp(z.real)
    return iv.mpc(r * iv.cos(z.imag), r * iv.sin(z.imag))


def csqrt(z):
    # Used only with Re z>0, Im z>=0; no branch crossing.
    a = iv.sqrt((abs(z) + z.real) / 2)
    return iv.mpc(a, z.imag / (2*a))


def upper(x):
    return x.b


def lower(x):
    return x.a


def widen(z, eps):
    e = upper(eps)
    interval = iv.mpf([-e, e])
    return z + iv.mpc(interval, interval)


def bernoulli(n):
    a = []
    for m in range(n+1):
        a.append(F(1, m+1))
        for j in range(m, 0, -1):
            a[j-1] = j*(a[j-1]-a[j])
    return a[0]


def fact(n):
    v = 1
    for k in range(2, n+1):
        v *= k
    return v


B = dict((k, bernoulli(k)) for k in range(2, 33, 2))
G = [(2*k-1, real(B[2*k] / (2*k*(2*k-1)))) for k in range(1, 12)]
Z = [(k, real(B[2*k] / fact(2*k))) for k in range(1, 17)]
LN = [iv.ln(real(n)) for n in range(1, 65)]
LOGPI = iv.ln(iv.pi)


def loggamma(w):
    # Shift 32 times, then DLMF 5.11.1/5.11(ii), n=12.
    v = w + 32
    ans = (v-real(F(1,2)))*clog(v)-v+iv.ln(2*iv.pi)/2
    for power, coefficient in G:
        ans += coefficient / v**power
    eps = real(abs(B[24])/F(24*23))*2**12 / lower(abs(v))**23
    ans = widen(ans, eps)
    for j in range(32):
        ans -= clog(w+j)
    return ans


def zeta(s, derivative=False):
    # Euler--Maclaurin, endpoint N=64, M=16, a=1 in Johansson (2013).
    # R bounded by 4 |(s)_32| (2*pi)^-32 N^(1-sigma-32)/(sigma+31).
    ans = complex_()
    der = complex_()
    for ln in LN[:63]:
        term = cexp(-s*ln)
        ans += term
        if derivative:
            der -= ln*term
    ln = LN[63]
    nms = cexp(-s*ln)
    ans += 64*nms/(s-1) + nms/2
    if derivative:
        der += 64*nms*(-ln/(s-1)-1/(s-1)**2)-ln*nms/2
    rising = complex_(1)
    rising_der = complex_()
    j = 0
    for k, coefficient in Z:
        while j < 2*k-1:
            rising_der = rising_der*(s+j)+rising
            rising *= s+j
            j += 1
        scale = cexp((1-s-2*k)*ln)
        ans += coefficient*rising*scale
        if derivative:
            der += coefficient*(rising_der-ln*rising)*scale
    sigma = lower(s.real)
    product = real(1)
    for j in range(32):
        product *= abs(s+j)
    eps = 4*product/(2*iv.pi)**32 * iv.exp((1-sigma-32)*ln)/(sigma+31)
    ans = widen(ans, eps)
    if derivative:
        # Only called at s=3/2. Cauchy disk radius 1/4 for R(s).
        assert s.real == real(F(3,2)) and s.imag == real(0)
        product = real(1)
        for j in range(32):
            product *= real(F(7,4)+j)
        eps_disk = 4*product/(2*iv.pi)**32 * iv.exp((-real(F(1,4))-32)*ln)/real(F(129,4))
        return ans, widen(der, 4*eps_disk)
    return ans


def digamma_three_quarters():
    w = real(F(3,4))
    v = w+32
    ans = iv.ln(v)-1/(2*v)
    for k in range(1,12):
        ans -= real(B[2*k]/(2*k))/v**(2*k)
    for j in range(32):
        ans -= 1/(w+j)
    # Cauchy on radius 1/4 for the shifted log-Gamma remainder.
    eps = 4*real(abs(B[24])/F(24*23))*2**12 / real(F(65,2))**23
    e = upper(eps)
    return ans + iv.mpf([-e,e])


def xi(s):
    return s*(s-1)/2 * cexp(-s*LOGPI/2+loggamma(s/2))*zeta(s)


def dyadic(t):
    sign, mantissa, exponent, bits = t
    if bits < 0:
        raise ValueError('Nonfinite interval endpoint')
    return {'mantissa': str((-1 if sign else 1)*mantissa), 'exponent_2': exponent}


def record(x):
    return {'display': str(x), 'lower': dyadic(x._mpi_[0]), 'upper': dyadic(x._mpi_[1])}


def crec(z):
    return {'real': record(z.real), 'imag': record(z.imag)}


checks = []


def check(name, actual, relation, required):
    ok = bool(actual < required) if relation == '<' else bool(actual > required)
    checks.append({'name': name, 'actual': record(actual), 'relation': relation,
                   'required': record(real(required)), 'passed': ok})
    return ok


start = time.time()
report = {'scope': 'Finite actual-density inversion plus certified omitted tail; inherited C466a inputs remain qualified.',
          'python': sys.version, 'mpmath': mp.__version__, 'platform': platform.platform(),
          'precision_decimal': iv.dps, 'script_sha256': hashlib.sha256(open(__file__,'rb').read()).hexdigest(),
          'checks': checks, 'nodes': [], 'failures': []}

try:
    c0c = xi(complex_(F(1,2)))
    c0 = c0c.real
    check('c0_positive', c0, '>', 0)
    z, zp = zeta(complex_(F(3,2)), True)
    x = (real(F(4,3))-LOGPI/4+digamma_three_quarters()/4+(zp/z).real/2)
    S = 3*x
    check('S_positive', S, '>', 0)
    check('S_below_one', S, '<', 1)

    def reciprocal(z):
        value = xi(real(F(1,2))+csqrt(z))
        if not abs(value) > 0:
            raise ValueError('Completion denominator not separated from zero')
        return c0/value

    laps = [reciprocal(complex_(s)).real for s in [F(1,2),F(3,4),F(1),F(5,4),F(3,2)]]
    difference = laps[0]-4*laps[1]+6*laps[2]-4*laps[3]+laps[4]
    mu4 = 256*difference
    Q4 = 8*(S**4*laps[2]+mu4)
    check('finite_difference_positive', difference, '>', 0)
    check('fourth_derivative_budget', Q4, '<', F(1,1000))

    T, n = 4096, 8192
    step = real(F(T,n))
    kappa = 1/(4*iv.sqrt(real(2)))
    lam = -(iv.ln(2*iv.pi)+1+iv.pi/4)/(2*iv.sqrt(real(2)))
    a = real(F(3,16))
    check('tail_sqrt_coefficient', kappa*iv.ln(real(T))+lam, '>', a)
    check('tail_remainder_below_one', 4*iv.ln(real(T))/iv.sqrt(real(T)), '<', 1)
    tail = 2*iv.exp(real(3))*real(T)**(-real(F(3,8)))*iv.exp(-a*iv.sqrt(real(T)))/a
    quadrature_error = real(T)*step**4*Q4/180
    report['constants'] = {'c0_complex': crec(c0c), 'x': record(x), 'S': record(S),
        'laplace_values': [record(v) for v in laps], 'fourth_difference': record(difference),
        'mu4_upper': record(mu4), 'fourth_derivative_upper': record(Q4),
        'T': T, 'n': n, 'step': record(step), 'tail_coefficient': record(a),
        'one_sided_tail_upper': record(tail), 'simpson_error_upper': record(quadrature_error)}
    print('Constants: S=%s; |f^(4)|<=%s; Simpson error<=%s; tail<=%s' %
          (S,Q4,quadrature_error,tail), flush=False) if sys.version_info[0] >= 3 else print(
          'Constants: S=%s; |f^(4)|<=%s; Simpson error<=%s; tail<=%s' % (S,Q4,quadrature_error,tail))
    sys.stdout.flush()
    if any(not c['passed'] for c in checks):
        raise ValueError('A prerequisite inequality failed before inversion')
    total = real(0)
    for j in range(n+1):
        t = real(j)*step
        val = (cexp(complex_(0,1)*S*t)*reciprocal(iv.mpc(1,t))).real
        weight = 1 if j in (0,n) else (4 if j % 2 else 2)
        total += weight*val
        report['nodes'].append({'j':j, 'value':record(val)})
        if j % 1024 == 0:
            print('Enclosed nodes %d/%d; elapsed %.1fs' % (j,n,time.time()-start))
            sys.stdout.flush()
    integral = step*total/3
    eps = upper(quadrature_error+tail)
    pS = iv.exp(S)/iv.pi * (integral+iv.mpf([-eps,eps]))
    m = real(F(1,1000))
    check('density_lower_bound', pS, '>', m)
    report['result'] = {'finite_simpson_sum':record(integral), 'total_integral_error_upper':record(eps),
                        'density_enclosure':record(pS), 'requested_m':record(m),
                        'm_certified': bool(pS > m), 'R_formula': 'max(exp(exp(256)), pi/(2S), (exp(S)/(pi*m))^16)',
                        'whole_m_R_pair_independently_audited':False}
    print('p(S)=%s; required >%s; %s' % (pS,m,'PASS' if pS > m else 'FAIL'))
except Exception as exc:
    report['failures'].append('%s: %s' % (type(exc).__name__,str(exc)))
    print('Failure: %s' % report['failures'][-1])
finally:
    report['elapsed_seconds'] = time.time()-start
    report['failed_checks'] = [c['name'] for c in checks if not c['passed']]
    with open(DEST,'w') as handle:
        json.dump(report,handle,indent=2,sort_keys=True)
        handle.write('\n')
    print('Certificate: %s; failures=%s; failed checks=%s' % (DEST,report['failures'],report['failed_checks']))
sys.exit(bool(report['failures'] or report['failed_checks']))
