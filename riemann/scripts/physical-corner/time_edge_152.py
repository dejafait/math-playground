#!/usr/bin/env python3
"""One whole-time-edge derivative enclosure; no subdivision. Step152."""
from array import array
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import hashlib
import json
import time

from certify_148 import (IV, Q, BITS, log_point, log_iv, sqrt_iv, pi_iv,
                         atan_small, cmul, physical_prime, negative_exp,
                         enc_complex, approx, HELPER)

HERE = Path(__file__).resolve().parent
OUT = HERE/'time-edge-152.json'
ANCHOR = HERE/'independent-audit-150.json'
BLOCK = 2048
LIMIT_SECONDS = 600


def cadd(a, b):
    return a[0]+b[0], a[1]+b[1]


def cscale(a, r):
    return a[0]*r, a[1]*r


def dot(a, b):
    return a[0]*b[0]+a[1]*b[1]


def main():
    started = time.monotonic()
    data = {'status': 'IN_PROGRESS', 'bits': BITS,
            'target': 'Complete fixed-X whole-edge first time derivative enclosure',
            'inputs': {'t_lower': '98/625', 't_upper': '1/5', 'x': 6000000185827},
            'hashes': {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                       for p in [Path(__file__), HERE/'certify_148.py', HELPER, ANCHOR]},
            'blocks': [], 'gates': {}, 'failures': [], 'completed_through': 0,
            'deadline_seconds': LIMIT_SECONDS, 'block_size': BLOCK,
            'qualification': 'Inclusion test only; an unpaid lower bound is inconclusive.'}

    def save():
        data['elapsed_seconds'] = time.monotonic()-started
        OUT.write_text(json.dumps(data, separators=(',', ':'))+'\n')

    def gate(name, test, v=None):
        data['gates'][name] = {'passed': bool(test)}
        if v is not None:
            data['gates'][name]['evidence'] = v.enc()
        if not test:
            raise ArithmeticError(name)

    save()
    try:
        a, b = F(98, 625), F(1, 5)
        t = IV.raw(IV(a).l, IV(b).h)
        x, pi, N = IV(6000000185827), pi_iv(), 690988
        lower = x/(4*pi)+IV(a)/16-N*N
        upper = (N+1)**2-x/(4*pi)-IV(b)/16
        gate('whole_edge_floor_lower', lower.l > 0, lower)
        gate('whole_edge_floor_upper', upper.l > 0, upper)
        data['N'] = N
        d = 1+x*x
        arg = pi/2-atan_small(F(1, 6000000185827))
        au = log_iv(sqrt_iv(d)/(4*pi))/2-1/d
        av = arg/2-3*x/d
        inv_s, inv_sm = (2/d, -2*x/d), (-2/d, -2*x/d)
        ss, mm = cmul(inv_s, inv_s), cmul(inv_sm, inv_sm)
        ap = (-ss[0]/2-mm[0]+inv_s[0]/2,
              -ss[1]/2-mm[1]+inv_s[1]/2)
        ell_prime = cmul((au, av), ap)[0]
        sigma, tau = IV(F(1, 2))+t*au/2, x/2+t*av/2
        ell = 2*au+t*ell_prime
        logN, log32 = log_point(F(N)), log_point(F(32))
        shift = ell-2*log32
        gate('ell_logN_gt13', (ell-logN-13).l > 0, ell-logN-13)
        gate('shift_gt0', shift.l > 0, shift)
        gate('shift_lt25', shift.h < 25*Q, 25-shift)
        gate('all_nonconstant_exponents_negative', (sigma-t*logN/4).l > 0,
             sigma-t*logN/4)
        data['constants'] = {k: z.enc() for k, z in [
            ('t', t), ('pi', pi), ('alpha_re', au), ('alpha_im', av),
            ('alpha_prime_re', ap[0]), ('alpha_prime_im', ap[1]),
            ('sigma', sigma), ('tau', tau), ('ell', ell), ('ell_prime', ell_prime)]}
        anchor = json.loads(ANCHOR.read_text())
        gate('audited_anchor_passed', anchor['status'] == 'PASS' and
             not anchor['failures'] and anchor['N'] == N)
        z = anchor['result']['F']
        den = 1 << z['denominator_power_two']
        F0 = IV.raw(IV(F(int(z['lo']), den)).l, IV(F(int(z['hi']), den)).h)
        data['anchor_F'] = F0.enc()
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
        sums = {k: (IV(0), IV(0)) for k in ['A', 'L', 'At', 'Lt']}
        prime_count = 0
        for lo in range(1, N+1, BLOCK):
            hi = min(N, lo+BLOCK-1)
            bs = {k: (IV(0), IV(0)) for k in sums}
            min_amp, min_red, primes = None, 4*Q, 0
            for n in range(lo, hi+1):
                if n == 1:
                    u, chi = logs[1], characters[1]
                elif spf[n]:
                    p, m = spf[n], n//spf[n]
                    assert p*m == n and 2 <= p <= m <= keep
                    u, chi = logs[p]+logs[m], cmul(characters[p], characters[m])
                else:
                    u = log_point(F(n))
                    chi, margin, _, _ = physical_prime(u, tau, 2*pi)
                    min_red, primes = min(min_red, margin), primes+1
                if n <= keep:
                    logs[n], characters[n] = u, chi
                amplitude = negative_exp(u*(t*u/4-sigma))
                assert amplitude.l > 0
                term = cscale(chi, amplitude)
                beta = (u*u/4-au*u/2, -av*u/2)
                term_t = cmul(beta, term)
                for key, value in [('A', term), ('L', cscale(term, u)),
                                   ('At', term_t), ('Lt', cscale(term_t, u))]:
                    bs[key] = cadd(bs[key], value)
                min_amp = amplitude.l if min_amp is None else min(min_amp, amplitude.l)
            for k in sums:
                sums[k] = cadd(sums[k], bs[k])
            prime_count += primes
            data['blocks'].append({'lo': lo, 'hi': hi, 'count': hi-lo+1,
                'prime_count': primes, 'all_term_gates_passed': True,
                'min_amplitude_lower': str(min_amp), 'min_prime_reduction_margin': str(min_red),
                'sums': {k: enc_complex(v) for k, v in bs.items()}})
            data['completed_through'] = hi
            data['sums'] = {k: enc_complex(v) for k, v in sums.items()}
            save()
            if len(data['blocks']) % 32 == 0 or hi == N:
                print(json.dumps({'through': hi, 'required': N,
                      'seconds': round(time.monotonic()-started, 2)}), flush=True)
            if hi < N and time.monotonic()-started > LIMIT_SECONDS:
                data['status'] = 'COST_STOP'
                data['failures'].append('incomplete_support_at_cost_ceiling')
                save()
                print(json.dumps({'status': data['status'], 'path': str(OUT)}), flush=True)
                return
        gate('complete_support', data['blocks'][0]['lo'] == 1 and
             data['blocks'][-1]['hi'] == N and sum(z['count'] for z in data['blocks']) == N and
             all(c['hi']+1 == d['lo'] for c, d in zip(data['blocks'], data['blocks'][1:])))
        data['prime_count'] = prime_count
        A, L, At, Lt = [sums[k] for k in ['A', 'L', 'At', 'Lt']]
        S = cadd(cscale(A, ell), cscale(L, -2))
        St = cadd(cadd(cscale(A, ell_prime), cscale(At, ell)), cscale(Lt, -2))
        derivative = dot(At, S)+dot(A, St)
        elapsed = IV.raw(0, IV(b-a).h)
        propagated = F0+elapsed*derivative
        r2_upper = A[0].abs_upper()**2+A[1].abs_upper()**2
        radius = sqrt_iv(IV.raw(0, r2_upper.h))
        p, q = IV(F(101, 200000000)), IV(F(142, 10000000)+F(1, 250000000000))
        payment = p*(25*radius+F(81, 2))+q*radius+p*q
        paid = propagated-payment
        data['result'] = {k: z.enc() for k, z in [
            ('F_derivative', derivative), ('elapsed', elapsed), ('F_propagated', propagated),
            ('R_upper_enclosure', radius), ('R_squared_upper', r2_upper), ('E', payment),
            ('F_minus_E', paid), ('p', p), ('q', q)]}
        data['result']['S'] = enc_complex(S)
        data['result']['S_derivative'] = enc_complex(St)
        data['result']['required_positive_threshold'] = '0'
        data['status'] = 'POSITIVE_PAID' if paid.l > 0 else 'INCONCLUSIVE_WIDTH'
        if paid.l <= 0:
            data['failures'].append('whole_edge_derivative_enclosure_does_not_pay_zero_threshold')
        save()
        print(json.dumps({'status': data['status'], 'N': N, 'blocks': len(data['blocks']),
              'F_derivative': approx(derivative), 'F_propagated': approx(propagated),
              'R_upper_enclosure': approx(radius), 'E': approx(payment),
              'F_minus_E': approx(paid), 'required': 0,
              'failures': data['failures'], 'path': str(OUT)}), flush=True)
    except Exception as exc:
        data['status'] = 'FAILED'
        data['failures'].append(type(exc).__name__+': '+str(exc))
        save()
        print(json.dumps({'status': 'FAILED', 'failures': data['failures'], 'path': str(OUT)}), flush=True)
        raise


if __name__ == '__main__':
    main()
