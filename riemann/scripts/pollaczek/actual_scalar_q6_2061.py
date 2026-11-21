#!/usr/bin/env python3
"""One fixed Q_6 distinct-real-root screen; exact rational interval Sturm.

Run from riemann: python3 scripts/pollaczek/actual_scalar_q6_2061.py
No floating point, root approximations, precision fallback or degree sweep.
"""
from fractions import Fraction as F
from math import comb, factorial, isqrt
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
OUT = HERE / 'actual-scalar-q6-2061.json'
TARGET = ('Certify whether the prescribed actual scalar Q_6 has at least '
          "four distinct real zeros, retaining all odd coefficients and N=6's own Jensen weights.")
DIGITS = 60
GRID = 10**DIGITS
ZERO = (F(0), F(0))
data = {'target': TARGET, 'status': 'STARTED', 'checks': {},
        'required_distinct_real_count': 4, 'arithmetic_grid_digits': DIGITS,
        'replay': 'python3 scripts/pollaczek/actual_scalar_q6_2061.py',
        'scope': 'Only prescribed scalar Q_6; no U_N output or analytic transfer'}


def check(name, ok):
    data['checks'][name] = bool(ok)
    if not ok:
        raise ArithmeticError(name)


def enc_iv(v):
    return {'lower': str(v[0]), 'upper': str(v[1])}


def save(stage):
    data['status'] = stage
    data['failures'] = [k for k, v in data['checks'].items() if not v]
    OUT.write_text(json.dumps(data, indent=2) + '\n')


def outward(v, digits=DIGITS):
    scale = 10**digits
    lo, hi = v[0]*scale, v[1]*scale
    return (F(lo.numerator//lo.denominator, scale),
            F(-((-hi.numerator)//hi.denominator), scale))


def add(a, b):
    return outward((a[0]+b[0], a[1]+b[1]))


def neg(a):
    return -a[1], -a[0]


def mul(a, b):
    products = [x*y for x in a for y in b]
    return outward((min(products), max(products)))


def scale(a, c):
    return mul(a, (c, c))


def div(a, b):
    if b[0] <= 0 <= b[1]:
        raise ArithmeticError('division denominator contains zero')
    return mul(a, (1/b[1], 1/b[0]))


def sign(a):
    if a[0] > 0:
        return 1
    if a[1] < 0:
        return -1
    raise ArithmeticError('unresolved sign: ' + str(enc_iv(a)))


def ep_add(a, b):
    return [
        ((a[k][0] if k < len(a) else F(0)) +
         (b[k][0] if k < len(b) else F(0)),
         (a[k][1] if k < len(a) else F(0)) +
         (b[k][1] if k < len(b) else F(0)))
        for k in range(max(len(a), len(b)))]


def ep_scale(p, c):
    return [(c*a, c*b) for a, b in p]


def ep_encode(p):
    return [{'rational': str(a), 'sqrt2': str(b)} for a, b in p]


def ep_decode(p):
    return [(F(v['rational']), F(v['sqrt2'])) for v in p]


def ep_eval(p, pi, sqrt2):
    v = ZERO
    for a, b in reversed(p):
        v = add(mul(v, pi), add((a, a), scale(sqrt2, b)))
    return v


def arctan(d):
    terms = [F((-1)**j, (2*j+1)*d**(2*j+1)) for j in range(48)]
    total = sum(terms, F(0))
    error = F(1, 97*d**97)
    return (total, total+error), {
        'argument': str(F(1, d)), 'term_count': 48,
        'terms': list(map(str, terms)), 'partial_sum': str(total),
        'positive_remainder_upper': str(error)}


def remainder(a, b, trace):
    """Enclose actual remainder, deleting only exact top cancellations.

    Actual top coefficient of r-(r_top/b_top)*x^shift*b is identically
    zero. Interval dependence can widen its enclosure; deletion follows
    this identity, never a numerical smallness test. Lower entries are
    always retained, even if their enclosures contain zero.
    """
    r = list(a)
    sign(b[-1])
    trace['dividend'] = list(map(enc_iv, a))
    trace['divisor'] = list(map(enc_iv, b))
    trace['steps'] = []
    while len(r) >= len(b):
        shift = len(r)-len(b)
        ratio = div(r[-1], b[-1])
        canceled = add(r[-1], neg(mul(ratio, b[-1])))
        check('top_cancellation_enclosed_'+str(len(data['division_trace']))+'_'+str(shift),
              canceled[0] <= 0 <= canceled[1])
        for j in range(len(b)-1):
            r[shift+j] = add(r[shift+j], neg(mul(ratio, b[j])))
        r.pop()
        trace['steps'].append({'shift': shift, 'quotient_coefficient': enc_iv(ratio),
                               'exact_zero_enclosure': enc_iv(canceled),
                               'remaining_coefficients': list(map(enc_iv, r))})
    trace['remainder'] = list(map(enc_iv, r))
    return r


def variations(signs):
    return sum(a != b for a, b in zip(signs, signs[1:]))


def main():
    data['script_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    # Repeat C029n's elementary input certificates at the same fixed grid.
    a5, cert5 = arctan(5)
    a239, cert239 = arctan(239)
    raw_pi = (16*a5[0]-4*a239[1], 16*a5[1]-4*a239[0])
    pi = outward(raw_pi)
    s = isqrt(2*GRID**2)
    sqrt2 = F(s, GRID), F(s+1, GRID)
    data.update({'arctan5': cert5, 'arctan239': cert239,
                 'pi_machin_interval': enc_iv(raw_pi), 'pi_interval': enc_iv(pi),
                 'sqrt2_interval': enc_iv(sqrt2)})
    check('machin_tangent_identity',
          (F(120,119)-F(1,239))/(1+F(120,119)*F(1,239)) == 1)
    check('machin_angle_range', 0 < 4*(F(1,5)-F(1,375))-F(1,239) < F(4,5))
    check('sqrt2_squared_endpoints', 0 < sqrt2[0]**2 < 2 < sqrt2[1]**2)
    check('pi_outward', pi[0] <= raw_pi[0] <= raw_pi[1] <= pi[1])

    prior_path = HERE / 'tilted-boundary-metric-2010.json'
    prior = json.loads(prior_path.read_text())
    data['comparison_input_sha256'] = hashlib.sha256(prior_path.read_bytes()).hexdigest()
    check('same_fixed_pi_interval', enc_iv(pi) == prior['pi_interval'])
    check('same_fixed_sqrt2_interval', enc_iv(sqrt2) == prior['sqrt2_interval'])

    bern = [F(1)]
    for m in range(1,19):
        bern.append(-sum((comb(m+1,k)*bern[k] for k in range(m)), F(0))/(m+1))
    check('bernoulli_table', bern == list(map(F, prior['bernoulli_0_through_18'])))
    phases = [(F(1),F(0)), (F(1),F(1)), (F(-1),F(0)), (F(-1),F(-1))]
    u = []
    for n in range(9):
        p = [ZERO]*(n+2)
        for h in range(n+1):
            c = -F(factorial(n)*4**h*(4**(h+1)-1)*2**(h+1),
                   factorial(n-h)*factorial(2*h+2))*bern[2*h+2]
            a,b = phases[(n-h)%4]
            p[h+1] = c*a, c*b
        u.append(p)
    beta = []
    for n in range(7):
        p = ep_add(ep_scale(u[n], 8*n*n+12*n+7),
                   ep_scale(u[n+2], (2*n+3)*(2*n+5)))
        if n >= 2:
            p = ep_add(p, ep_scale(u[n-2], 4*n*(n-1)))
        beta.append(p)
    jensen = [F(factorial(6),factorial(6-k)*6**k) for k in range(7)]
    weights = [F(1)]
    for k in range(1,7):
        weights.append(weights[-1]*F(2*k+1, 2*k))
    A = [ep_scale(beta[k], jensen[k]) for k in range(7)]
    Q = [ep_scale(A[k], weights[k]) for k in range(7)]
    check('all_prior_u_exact', u == list(map(ep_decode, prior['u_over_S_polynomials'])))
    check('all_prior_beta_exact', beta == list(map(ep_decode, prior['beta_over_S_polynomials'])))
    check('N6_Jensen_weights_exact', jensen == list(map(F, prior['weights'])))
    check('all_prior_A6_exact', A == list(map(ep_decode, prior['a_over_S_polynomials'])))
    check('scalar_weights_exact', weights == list(map(F, ['1','3/2','15/8','35/16','315/128','693/256','3003/1024'])))
    q = [ep_eval(p, pi, sqrt2) for p in Q]
    data.update({'bernoulli_0_to_18': list(map(str, bern)),
                 'u_over_S_polynomials': list(map(ep_encode, u)),
                 'beta_over_S_polynomials': list(map(ep_encode, beta)),
                 'N6_Jensen_weights': list(map(str, jensen)),
                 'scalar_weights': list(map(str, weights)),
                 'A6_exact_polynomials': list(map(ep_encode, A)),
                 'Q6_exact_coefficient_polynomials': list(map(ep_encode, Q)),
                 'Q6_coefficient_intervals': list(map(enc_iv, q)),
                 'Q6_coefficient_outer_12': [enc_iv(outward(v,12)) for v in q],
                 'division_trace': [], 'sturm_chain': []})
    check('degree_six', sign(q[6]) != 0)
    check('all_odd_coefficients_retained_and_nonzero', all(sign(q[k]) != 0 for k in (1,3,5)))
    chain = [q, [scale(q[k], F(k)) for k in range(1,7)]]
    data['sturm_chain'] = [list(map(enc_iv, p)) for p in chain]
    save('COEFFICIENTS_AND_DERIVATIVE')
    # Each expected degree 4,3,2,1,0 must have nonzero leading enclosure.
    for expected_degree in (4,3,2,1,0):
        trace = {'expected_remainder_degree': expected_degree}
        data['division_trace'].append(trace)
        r = [neg(v) for v in remainder(chain[-2], chain[-1], trace)]
        check('remainder_length_'+str(expected_degree), len(r) == expected_degree+1)
        check('nonzero_leading_remainder_'+str(expected_degree), sign(r[-1]) != 0)
        chain.append(r)
        data['sturm_chain'] = [list(map(enc_iv, p)) for p in chain]
        save('STURM_THROUGH_DEGREE_'+str(expected_degree))
    check('nonzero_terminal_constant', sign(chain[-1][0]) != 0)
    # Division by the final nonzero constant has identically zero remainder.
    # Thus gcd(Q,Q')=1. Every polynomial in the chain has its certified degree.
    degrees = [len(p)-1 for p in chain]
    positive = [sign(p[-1]) for p in chain]
    negative = [sgn*(-1)**degree for sgn,degree in zip(positive,degrees)]
    vm, vp = variations(negative), variations(positive)
    count = vm-vp
    data.update({'sturm_degrees': degrees,
                 'sturm_leading_outer_12': [enc_iv(outward(p[-1],12)) for p in chain],
                 'signs_at_negative_infinity': negative,
                 'signs_at_positive_infinity': positive,
                 'variations_at_negative_infinity': vm,
                 'variations_at_positive_infinity': vp,
                 'actual_distinct_real_count': count,
                 'square_free': True, 'threshold_passed': count >= 4})
    check('root_count_range_and_parity', 0 <= count <= 6 and count % 2 == 0)
    save('CERTIFIED')
    print(json.dumps({k:data[k] for k in ('status','actual_distinct_real_count',
          'required_distinct_real_count','threshold_passed','sturm_degrees',
          'signs_at_negative_infinity','signs_at_positive_infinity',
          'variations_at_negative_infinity','variations_at_positive_infinity','failures')}))
    print('Certificate: scripts/pollaczek/' + OUT.name)
    print('Replay: ' + data['replay'])


if __name__ == '__main__':
    try:
        main()
    except ArithmeticError as exc:
        data['unresolved_error'] = str(exc)
        save('INCONCLUSIVE')
        print(json.dumps({'status':data['status'], 'error':str(exc),
                          'failures':data['failures'], 'certificate': 'scripts/pollaczek/'+OUT.name}))
        raise SystemExit(1)
