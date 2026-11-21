#!/usr/bin/env python3
"""Exact N=6 boundary-metric obstruction; standard library only.

Run from riemann:
    python3 scripts/pollaczek/tilted_boundary_metric_2010.py
Every interval endpoint is a Fraction. No floating point input or result
is used. Polynomials are ascending in pi, with coefficients a+b*sqrt(2).
The common positive factor S=sin(pi/8)/sqrt(2) is removed from u and beta.
"""

from fractions import Fraction as F
from math import comb, factorial, isqrt
from pathlib import Path
import json


ZERO = (F(0), F(0))


def qadd(x, y):
    return (x[0] + y[0], x[1] + y[1])


def qmul(x, y):
    return (x[0] * y[0] + 2 * x[1] * y[1],
            x[0] * y[1] + x[1] * y[0])


def padd(x, y):
    return [qadd(x[k] if k < len(x) else ZERO,
                 y[k] if k < len(y) else ZERO)
            for k in range(max(len(x), len(y)))]


def pscale(x, c):
    return [(a * c, b * c) for a, b in x]


def pmul(x, y):
    out = [ZERO] * (len(x) + len(y) - 1)
    for i, xi in enumerate(x):
        for j, yj in enumerate(y):
            out[i+j] = qadd(out[i+j], qmul(xi, yj))
    return out


def iadd(x, y):
    return (x[0] + y[0], x[1] + y[1])


def iscale(x, c):
    return (x[0]*c, x[1]*c) if c >= 0 else (x[1]*c, x[0]*c)


def imul(x, y):
    vals = [a*b for a in x for b in y]
    return (min(vals), max(vals))


def peval(p, pi_interval, sqrt2_interval):
    out = (F(0), F(0))
    for a, b in reversed(p):
        coefficient = iadd((a, a), iscale(sqrt2_interval, b))
        out = iadd(imul(out, pi_interval), coefficient)
    return out


def floor_fraction(x):
    return x.numerator // x.denominator


def outward_grid(interval, digits):
    scale = 10**digits
    lo = floor_fraction(interval[0] * scale)
    hi = -floor_fraction(-interval[1] * scale)
    return (F(lo, scale), F(hi, scale))


def rational(x):
    return str(x.numerator) + '/' + str(x.denominator)


def interval_json(x):
    return {'lower': rational(x[0]), 'upper': rational(x[1])}


def poly_json(p):
    return [{'rational': rational(a), 'sqrt2': rational(b)} for a, b in p]


def arctan_bounds(denominator, count):
    assert count > 0 and count % 2 == 0
    x = F(1, denominator)
    terms = [(-1)**k * x**(2*k+1) / (2*k+1) for k in range(count)]
    partial = sum(terms, F(0))
    remainder_upper = x**(2*count+1) / (2*count+1)
    return (partial, partial + remainder_upper), {
        'argument': rational(x), 'term_count': count,
        'terms': [rational(t) for t in terms],
        'partial_sum': rational(partial),
        'positive_remainder_upper': rational(remainder_upper)}


def main():
    failures = []
    checks = {}

    def check(name, value):
        checks[name] = bool(value)
        if not value:
            failures.append(name)

    atan5, atan5_data = arctan_bounds(5, 48)
    atan239, atan239_data = arctan_bounds(239, 48)
    pi_machin = iadd(iscale(atan5, 16), iscale(atan239, -4))
    pi_interval = outward_grid(pi_machin, 60)
    sqrt_scale = 10**60
    sqrt_floor = isqrt(2 * sqrt_scale**2)
    sqrt2_interval = (F(sqrt_floor, sqrt_scale), F(sqrt_floor+1, sqrt_scale))
    check('pi_outward_rounding',
          pi_interval[0] <= pi_machin[0] <= pi_machin[1] <= pi_interval[1])
    check('sqrt2_squared_endpoints',
          0 < sqrt2_interval[0]**2 < 2 < sqrt2_interval[1]**2)
    check('machin_tangent_identity',
          (F(120,119)-F(1,239))/(1+F(120,119)*F(1,239)) == 1)
    check('machin_angle_positive_lower', 4*(F(1,5)-F(1,375))-F(1,239) > 0)

    bernoulli = [F(1)]
    for m in range(1, 19):
        bernoulli.append(-sum((comb(m+1,k)*bernoulli[k] for k in range(m)),
                             F(0)) / (m+1))
    expected_even = [F(1,6), F(-1,30), F(1,42), F(-1,30), F(5,66),
                     F(-691,2730), F(7,6), F(-3617,510), F(43867,798)]
    check('bernoulli_even_table', bernoulli[2:19:2] == expected_even)
    check('bernoulli_odd_table', bernoulli[1] == F(-1,2)
          and all(bernoulli[k] == 0 for k in range(3,19,2)))

    # sin(pi*m/2+pi/8)/sin(pi/8) = 1,1+sqrt(2),-1,-1-sqrt(2).
    phases = [(F(1),F(0)), (F(1),F(1)), (F(-1),F(0)), (F(-1),F(-1))]
    u = []
    for n in range(9):
        polynomial = [ZERO] * (n+2)
        for h in range(n+1):
            coefficient = (-F(factorial(n),1) * 4**h * (4**(h+1)-1)
                           * bernoulli[2*h+2] * 2**(h+1)
                           / (factorial(n-h)*factorial(2*h+2)))
            phase = phases[(n-h) % 4]
            polynomial[h+1] = (coefficient*phase[0], coefficient*phase[1])
        u.append(polynomial)

    beta = []
    for n in range(7):
        polynomial = padd(pscale(u[n], 8*n*n+12*n+7),
                          pscale(u[n+2], (2*n+3)*(2*n+5)))
        if n >= 2:
            polynomial = padd(polynomial, pscale(u[n-2], 4*n*(n-1)))
        beta.append(polynomial)
    weights = [F(factorial(6), factorial(6-k)*6**k) for k in range(7)]
    a = [pscale(beta[k], weights[k]) for k in range(7)]
    u_intervals = [peval(p, pi_interval, sqrt2_interval) for p in u]
    beta_intervals = [peval(p, pi_interval, sqrt2_interval) for p in beta]
    a_intervals = [peval(p, pi_interval, sqrt2_interval) for p in a]
    q = padd(padd(pscale(pmul(a[1],a[1]), F(3,2)),
                  pscale(pmul(a[0],a[0]), F(-1))),
             pscale(pmul(a[2],a[0]), F(-5,2)))
    q_beta = padd(padd(pscale(pmul(beta[1],beta[1]), F(3,2)),
                       pscale(pmul(beta[0],beta[0]), F(-1))),
                  pscale(pmul(beta[2],beta[0]), F(-25,12)))
    check('Q_normalization_identity', q == q_beta)
    q_interval = peval(q, pi_interval, sqrt2_interval)
    q_factored = iadd(iadd(iscale(imul(a_intervals[1],a_intervals[1]),F(3,2)),
                           iscale(imul(a_intervals[0],a_intervals[0]),F(-1))),
                      iscale(imul(a_intervals[2],a_intervals[0]),F(-5,2)))

    d_squared = [F(693,256),F(315,128),F(35,16),F(15,8),F(3,2),F(1)]
    j_off_squared = [F(55,2),F(18),F(21,2),F(5),F(3,2)]
    scaling_checks = []
    for i in range(5):
        k = 5-i
        upper = F(2*k+1,2)
        lower = F(k)
        identity = upper*d_squared[i+1] == lower*d_squared[i]
        scaling_checks.append({'basis_degree': k, 'upper': rational(upper),
                               'lower': rational(lower), 'identity': identity})
        check('scaling_edge_'+str(i+1), identity
              and upper*lower == j_off_squared[i])
    check('D_last_entry_one', d_squared[-1] == 1)
    check('D_all_positive', all(x>0 for x in d_squared))
    check('radical_elimination_ratio_squared',
          F(5)*d_squared[3]/F(3,2) == F(25,4))

    # Coarse rational targets are selected for readable proof output after
    # exact intervals have been computed. The exact endpoints are retained.
    check('beta6_nonzero', beta_intervals[6][0] > 0 or beta_intervals[6][1] < 0)
    check('a0_nonzero', a_intervals[0][0] > 0 or a_intervals[0][1] < 0)
    check('Q_nonzero_expanded', q_interval[0] > 0 or q_interval[1] < 0)
    check('Q_nonzero_factored', q_factored[0] > 0 or q_factored[1] < 0)
    check('Q_enclosures_overlap',
          max(q_interval[0],q_factored[0]) <= min(q_interval[1],q_factored[1]))

    small_enclosures = {
        'beta0_over_S': interval_json(outward_grid(beta_intervals[0], 12)),
        'beta6_over_S': interval_json(outward_grid(beta_intervals[6], 12)),
        'a6_over_S': interval_json(outward_grid(a_intervals[6], 12)),
        'Q_over_S_squared': interval_json(outward_grid(q_interval, 12)),
    }
    certificate = {
        'target': 'N=6, full Kuznetsov T_6; G=I+e1*z^T+z*e1^T, A^T*G=G*A',
        'method': 'Exact Q(sqrt(2))[pi] coefficients; rational interval Horner evaluation',
        'normalization': 'S=sin(pi/8)/sqrt(2)>0; all u,beta,a arrays divided by S; Q divided by S^2',
        'reproduction': 'python3 scripts/pollaczek/tilted_boundary_metric_2010.py',
        'atan5': atan5_data, 'atan239': atan239_data,
        'pi_machin_interval': interval_json(pi_machin),
        'pi_interval': interval_json(pi_interval),
        'sqrt2_interval': interval_json(sqrt2_interval),
        'bernoulli_0_through_18': [rational(x) for x in bernoulli],
        'u_over_S_polynomials': [poly_json(p) for p in u],
        'beta_over_S_polynomials': [poly_json(p) for p in beta],
        'weights': [rational(x) for x in weights],
        'a_over_S_polynomials': [poly_json(p) for p in a],
        'u_over_S_intervals': [interval_json(x) for x in u_intervals],
        'beta_over_S_intervals': [interval_json(x) for x in beta_intervals],
        'a_over_S_intervals': [interval_json(x) for x in a_intervals],
        'Q_over_S_squared_polynomial': poly_json(q),
        'Q_over_S_squared_interval_expanded': interval_json(q_interval),
        'Q_over_S_squared_interval_factored': interval_json(q_factored),
        'D_squared': [rational(x) for x in d_squared],
        'J_offdiagonal_squared': [rational(x) for x in j_off_squared],
        'scaling_checks': scaling_checks,
        'compatibility_system': {
            'variables': 'g=1+2*z1; y=(z2,z3,z4,z5,z6)',
            'blocks': 'alpha=-v1; c=sqrt(55/2)*f1; b=(sqrt(55/2)-v2,-v3,-v4,-v5,-v6); B=J[2:6,2:6]',
            'equations': ['(B-alpha*I)*y+g*b=c', 'y_i*b_j-b_i*y_j=0 for all 1<=i<j<=5'],
            'elimination': 'b5!=0 forces y=lambda*b; rows 4,5 imply lambda*K=0, then g=0, contrary to c!=0',
            'K': '36*sqrt(3/2)*Q/(a6^2*D1^2)',
            'Q': '(3/2)*a1^2-a0^2-(5/2)*a2*a0',
        },
        'readable_enclosures': small_enclosures,
        'required_bounds': 'beta6/S!=0, a0/S!=0, Q/S^2!=0; positive D entries',
        'checks': checks, 'failures': failures,
        'result': 'INCOMPATIBLE_BOUNDARY_METRIC' if not failures else 'INCOMPLETE',
        'scope': 'N=6 only; no other metric, degree, eventual uniformity, root count or RH conclusion',
    }
    out = Path(__file__).with_name('tilted-boundary-metric-2010.json')
    out.write_text(json.dumps(certificate, indent=2)+'\n')
    print('Result:', certificate['result'])
    print('Required:', certificate['required_bounds'])
    for name, enclosure in small_enclosures.items():
        print(name+': ['+enclosure['lower']+', '+enclosure['upper']+']')
    print('Checks:', len(checks), '; failures:', ', '.join(failures) if failures else 'none')
    print('Certificate:', out.relative_to(Path.cwd()))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
