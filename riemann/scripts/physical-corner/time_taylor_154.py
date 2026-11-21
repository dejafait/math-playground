#!/usr/bin/env python3
"""One complete-support degree12 common-time model; exact dyadic inclusion.

No subdivision, degree retry, floating mathematical input or new payment.
See the step154 working note and canonical result for the inclusion proof.
"""
from array import array
from fractions import Fraction as F
from math import factorial, isqrt, comb
from pathlib import Path
import hashlib
import json
import time

from certify_148 import (IV, Q, BITS, log_point, log_iv, sqrt_iv, pi_iv,
                         atan_small, cmul, physical_prime, negative_exp,
                         enc_complex, approx, HELPER)

HERE = Path(__file__).resolve().parent
OUT = HERE/'time-taylor-154.json'
DEGREE, BLOCK, LIMIT_SECONDS = 12, 2048, 600


def addc(a, b):
    return a[0]+b[0], a[1]+b[1]


def scalec(a, b):
    return a[0]*b, a[1]*b


def zeros():
    return [IV(0) for _ in range(DEGREE+1)]


def encmodel(m):
    return {'coefficients': [x.enc() for x in m[0]],
            'component_remainder_radius': str(m[1])}


def polybound(c):
    # u in [0,1], coefficient uncertainties included.
    return IV.raw(sum(max(abs(x.l), abs(x.h)) for x in c),
                  sum(max(abs(x.l), abs(x.h)) for x in c))


def mscale(m, k):
    v = IV(k)
    radius = (IV.raw(m[1], m[1])*v.abs_upper()).h
    return [x*v for x in m[0]], radius


def madd(a, b):
    return [x+y for x, y in zip(a[0], b[0])], a[1]+b[1]


def mmul(a, b, name, trace):
    full = [IV(0) for _ in range(2*DEGREE+1)]
    for i, x in enumerate(a[0]):
        for j, y in enumerate(b[0]):
            full[i+j] += x*y
    discarded = polybound(full[DEGREE+1:])
    pa, pb = polybound(a[0]), polybound(b[0])
    ra, rb = IV.raw(a[1], a[1]), IV.raw(b[1], b[1])
    cross_a, cross_b, cross_ab = pa*rb, pb*ra, ra*rb
    radius = (discarded+cross_a+cross_b+cross_ab).h
    result = full[:DEGREE+1], radius
    trace[name] = {'a': encmodel(a), 'b': encmodel(b),
                   'discarded_coefficients': [z.enc() for z in full[DEGREE+1:]],
                   'discarded_bound': discarded.enc(), 'P_a_bound': pa.enc(),
                   'P_b_bound': pb.enc(), 'P_a_R_b': cross_a.enc(),
                   'P_b_R_a': cross_b.enc(), 'R_a_R_b': cross_ab.enc(),
                   'result': encmodel(result)}
    return result


def main():
    started = time.monotonic()
    data = {'status': 'IN_PROGRESS', 'bits': BITS, 'degree': DEGREE,
            'target': 'One complete fixed-X degree12 paid physical time edge',
            'inputs': {'a': '98/625', 'h': '27/625', 'x': 6000000185827,
                       'u_domain': ['0', '1']},
            'deadline_seconds': LIMIT_SECONDS, 'block_size': BLOCK,
            'hashes': {str(p.relative_to(HERE.parent)): hashlib.sha256(p.read_bytes()).hexdigest()
                       for p in [Path(__file__), HERE/'certify_148.py', HELPER,
                                 HERE/'time-edge-152.json']},
            'blocks': [], 'gates': {}, 'failures': [], 'completed_through': 0,
            'qualification': 'Informal interval certificate; actual analytic transfer remains conditional.'}

    def save():
        data['elapsed_seconds'] = time.monotonic()-started
        OUT.write_text(json.dumps(data, separators=(',', ':'))+'\n')

    def gate(name, test, value=None):
        data['gates'][name] = {'passed': bool(test)}
        if value is not None:
            data['gates'][name]['evidence'] = value.enc()
        if not test:
            raise ArithmeticError(name)

    save()
    try:
        a, h, b = IV(F(98, 625)), IV(F(27, 625)), IV(F(1, 5))
        x, N, pi = IV(6000000185827), 690988, pi_iv()
        data['N'] = N
        lower = x/(4*pi)+a/16-N*N
        upper = (N+1)**2-x/(4*pi)-b/16
        gate('floor_lower', lower.l > 0, lower)
        gate('floor_upper', upper.l > 0, upper)
        d = 1+x*x
        arg = pi/2-atan_small(F(1, 6000000185827))
        au = log_iv(sqrt_iv(d)/(4*pi))/2-1/d
        av = arg/2-3*x/d
        inv_s, inv_sm = (2/d, -2*x/d), (-2/d, -2*x/d)
        ss, mm = cmul(inv_s, inv_s), cmul(inv_sm, inv_sm)
        ap = (-ss[0]/2-mm[0]+inv_s[0]/2,
              -ss[1]/2-mm[1]+inv_s[1]/2)
        ellt = cmul((au, av), ap)[0]
        sigma0, tau0 = IV(F(1, 2))+a*au/2, x/2+a*av/2
        ell0, ell1 = 2*au+a*ellt, h*ellt
        whole_t = IV.raw(a.l, b.h)
        ell = 2*au+whole_t*ellt
        logN, log32 = log_point(F(N)), log_point(F(32))
        gate('ell_logN_gt13', (ell-logN-13).l > 0, ell-logN-13)
        gate('shift_positive', (ell-2*log32).l > 0, ell-2*log32)
        gate('shift_lt25', (25-ell+2*log32).l > 0, 25-ell+2*log32)
        gate('corner_amplitude_exponents_negative', (sigma0-a*logN/4).l > 0,
             sigma0-a*logN/4)
        exp2 = negative_exp(IV(-2)).reciprocal()
        gate('exp2_lt8', exp2.h < 8*Q, 8-exp2)
        # Reuse only the established uniform payment, no tighter derivation.
        payment_source = json.loads((HERE/'time-edge-152.json').read_text())
        oldE = payment_source['result']['E']
        oldEupper = F(int(oldE['hi']), 1 << oldE['denominator_power_two'])
        gate('established_payment_lt203e_6', payment_source['status'] == 'INCONCLUSIVE_WIDTH'
             and oldEupper < F(203, 1000000))
        data['constants'] = {k: z.enc() for k, z in [
            ('a', a), ('h', h), ('pi', pi), ('alpha_re', au), ('alpha_im', av),
            ('sigma0', sigma0), ('tau0', tau0), ('ell0', ell0), ('ell1', ell1),
            ('ell_prime', ellt), ('exp2', exp2)]}
        inverse_j = [IV(0)]+[IV(F(1, j)) for j in range(1, DEGREE+1)]
        tail_factor = IV(F(16, factorial(13)))
        data['tail_rule'] = {'v_upper_required': '2', 'exp_v_upper': '8',
                             'two_real_coordinates_factor': '2',
                             'factor': tail_factor.enc()}
        save()
        spf = array('I', [0])*(N+1)
        for p in range(2, isqrt(N)+1):
            if not spf[p]:
                for n in range(p*p, N+1, p):
                    if not spf[n]:
                        spf[n] = p
        keep = N//2
        logs, characters = [None]*(keep+1), [None]*(keep+1)
        logs[1], characters[1] = IV(0), (IV(1), IV(0))
        totals = {k: [(IV(0), IV(0)) for _ in range(DEGREE+1)] for k in ['A', 'L']}
        rhoA = rhoL = IV(0)
        prime_count = 0
        for lo in range(1, N+1, BLOCK):
            hi = min(N, lo+BLOCK-1)
            sums = {k: [(IV(0), IV(0)) for _ in range(DEGREE+1)] for k in totals}
            rA = rL = IV(0)
            min_amp, min_red, max_v, primes = None, 4*Q, 0, 0
            for n in range(lo, hi+1):
                if n == 1:
                    k, chi = logs[1], characters[1]
                elif spf[n]:
                    p, m = spf[n], n//spf[n]
                    assert p*m == n and 2 <= p <= m <= keep
                    k, chi = logs[p]+logs[m], cmul(characters[p], characters[m])
                else:
                    k = log_point(F(n))
                    chi, margin, _, _ = physical_prime(k, tau0, 2*pi)
                    min_red, primes = min(min_red, margin), primes+1
                if n <= keep:
                    logs[n], characters[n] = k, chi
                amplitude = negative_exp(k*(a*k/4-sigma0))
                assert amplitude.l > 0
                z = scalec(chi, amplitude)
                beta = (h*(k*k/4-au*k/2), -h*av*k/2)
                v = beta[0].abs_upper()+beta[1].abs_upper()
                assert 0 <= v.h <= 2*Q
                max_v = max(max_v, v.h)
                rem = tail_factor*amplitude*v**13
                rA, rL = rA+rem, rL+k*rem
                for j in range(DEGREE+1):
                    if j:
                        z = scalec(cmul(z, beta), inverse_j[j])
                    sums['A'][j] = addc(sums['A'][j], z)
                    sums['L'][j] = addc(sums['L'][j], scalec(z, k))
                min_amp = amplitude.l if min_amp is None else min(min_amp, amplitude.l)
            for key in totals:
                totals[key] = [addc(c, z) for c, z in zip(totals[key], sums[key])]
            rhoA, rhoL = rhoA+rA, rhoL+rL
            prime_count += primes
            data['blocks'].append({'lo': lo, 'hi': hi, 'count': hi-lo+1,
                'prime_count': primes, 'all_term_gates_passed': True,
                'min_amplitude_lower': str(min_amp), 'min_prime_reduction_margin': str(min_red),
                'max_v_upper': str(max_v), 'rhoA': rA.enc(), 'rhoL': rL.enc(),
                'coefficients': {key: [enc_complex(z) for z in seq] for key, seq in sums.items()}})
            data['completed_through'] = hi
            data['totals'] = {key: [enc_complex(z) for z in seq] for key, seq in totals.items()}
            data['remainders'] = {'rhoA': rhoA.enc(), 'rhoL': rhoL.enc()}
            save()
            if len(data['blocks']) % 32 == 0 or hi == N:
                print(json.dumps({'through': hi, 'required': N,
                                  'seconds': round(time.monotonic()-started, 2)}), flush=True)
            if hi < N and time.monotonic()-started > LIMIT_SECONDS:
                data['status'] = 'COST_STOP'
                data['failures'].append('complete_support_not_finished_within_cost_cap')
                save()
                print(json.dumps({'status': data['status'], 'path': str(OUT)}), flush=True)
                return
        gate('complete_support', data['blocks'][0]['lo'] == 1 and data['completed_through'] == N
             and sum(z['count'] for z in data['blocks']) == N
             and all(c['hi']+1 == d['lo'] for c, d in zip(data['blocks'], data['blocks'][1:])))
        data['prime_count'] = prime_count
        trace = {}
        em = zeros()
        em[0], em[1] = ell0, ell1
        ellmodel = em, 0
        components = {}
        result = zeros(), 0
        for c, name in enumerate(['re', 'im']):
            A = [z[c] for z in totals['A']], rhoA.h
            L = [z[c] for z in totals['L']], rhoL.h
            S = madd(mmul(ellmodel, A, 'ell_A_'+name, trace), mscale(L, -2))
            AS = mmul(A, S, 'A_S_'+name, trace)
            components[name] = {'A': encmodel(A), 'L': encmodel(L), 'S': encmodel(S)}
            result = madd(result, AS)
        bernstein = []
        for i in range(DEGREE+1):
            value = IV(0)
            for j in range(i+1):
                value += result[0][j]*F(comb(i, j), comb(DEGREE, j))
            bernstein.append(value)
        payment = IV(F(203, 1000000))
        rho = result[1]
        paid = IV.raw(min(z.l for z in bernstein)-rho-payment.h,
                      max(z.h for z in bernstein)+rho)
        data['product_trace'] = trace
        data['components'] = components
        data['result'] = {'F_model': encmodel(result),
            'bernstein': [z.enc() for z in bernstein], 'E_upper': payment.enc(),
            'F_minus_E_enclosure': paid.enc(), 'required_positive_threshold': '0'}
        data['status'] = 'POSITIVE_PAID' if paid.l > 0 else 'INCONCLUSIVE_WIDTH'
        if paid.l <= 0:
            data['failures'].append('degree12_Bernstein_lower_bound_unpaid')
        save()
        print(json.dumps({'status': data['status'], 'N': N, 'blocks': len(data['blocks']),
            'F_minus_E': approx(paid), 'required_lower': 0,
            'min_Bernstein_lower': float(F(min(z.l for z in bernstein), Q)),
            'full_remainder_radius': float(F(rho, Q)),
            'rhoA': approx(rhoA), 'rhoL': approx(rhoL), 'failures': data['failures'],
            'path': str(OUT)}), flush=True)
    except Exception as exc:
        data['status'] = 'FAILED'
        data['failures'].append(type(exc).__name__+': '+str(exc))
        save()
        print(json.dumps({'status': 'FAILED', 'failures': data['failures'], 'path': str(OUT)}), flush=True)
        raise


if __name__ == '__main__':
    main()
