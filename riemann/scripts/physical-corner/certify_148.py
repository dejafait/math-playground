#!/usr/bin/env python3
"""One complete physical corner, exact dyadic inclusion. See L962.

Exhaustive consecutive block records, no omitted natural-support terms.
Only stdout approximations use float; no float is a mathematical input.
"""
from array import array
from fractions import Fraction as F
from math import factorial, isqrt
from pathlib import Path
import hashlib
import json
import sys
import time

HERE = Path(__file__).resolve().parent
HELPER = HERE.parent / 'centred-moment' / 'rational_replay_140.py'
sys.path.insert(0, str(HELPER.parent))
from rational_replay_140 import IV, Q, BITS, log_point, log_iv, sqrt_iv, pi_iv, ceildiv

OUT = HERE / 'certificate-148.json'
LIMIT_SECONDS = 600
BLOCK = 2048


def cmul(a, b):
    return a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]


def atan_small(x):
    # Exact alternating rational bounds, 0<=x<=1/2.
    assert F(0) <= x <= F(1, 2)
    s = sum(((-1)**j*x**(2*j+1)/F(2*j+1) for j in range(8)), F(0))
    term = x**17/17
    return IV.raw(IV(s).l, IV(s+term).h)


EXP_COEFF = [IV(F(1, factorial(j))) for j in range(40)]
EXP_REMAINDER = IV(F(1, 8)**40 / factorial(40) / (1-F(1, 8*41)))
COS_COEFF = [IV(F((-1)**j, factorial(2*j))) for j in range(48)]
SIN_COEFF = [IV(F((-1)**j, factorial(2*j+1))) for j in range(48)]
COS_REMAINDER = IV(F(4**96, factorial(96))).h
SIN_REMAINDER = IV(F(4**97, factorial(97))).h


def polynomial(coeff, x):
    y = coeff[-1]
    for c in reversed(coeff[:-1]):
        y = y*x+c
    return y


def negative_exp(v):
    # v encloses a nonpositive exact argument.
    assert v.h <= 0
    if v.l == v.h == 0:
        return IV(1)
    y = -v
    k = max(0, (8*y.h).bit_length()-Q.bit_length())
    while y.h > (Q << k)//8:
        k += 1
    den = 1 << k
    z = IV.raw(y.l//den, ceildiv(y.h, den))
    assert 0 <= z.l <= z.h <= Q//8
    p = polynomial(EXP_COEFF, z)
    p = IV.raw(p.l, p.h+EXP_REMAINDER.h)
    assert p.l > 0
    for _ in range(k):
        p = p*p
    return p.reciprocal()


def physical_prime(logp, tau, twopi):
    theta = -tau*logp
    a, b = theta.l+theta.h, twopi.l+twopi.h
    k = (2*a+b)//(2*b)
    reduced = theta-k*twopi
    reduction_margin = 4*Q-max(abs(reduced.l), abs(reduced.h))
    assert reduction_margin > 0
    square = reduced*reduced
    c = polynomial(COS_COEFF, square)
    s = reduced*polynomial(SIN_COEFF, square)
    c = IV.raw(c.l-COS_REMAINDER, c.h+COS_REMAINDER)
    s = IV.raw(s.l-SIN_REMAINDER, s.h+SIN_REMAINDER)
    return (c, s), reduction_margin, theta.h-theta.l, abs(k)


def enc_complex(z):
    return {'re': z[0].enc(), 'im': z[1].enc()}


def approx(z):
    return [float(F(z.l, Q)), float(F(z.h, Q))]


def main():
    started = time.monotonic()
    data = {'status': 'IN_PROGRESS', 'bits': BITS,
            'target': 'Complete physical lower corner scalar reserve',
            'inputs': {'t': '98/625', 'x': 6000000185827},
            'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'helper_sha256': hashlib.sha256(HELPER.read_bytes()).hexdigest(),
            'deadline_seconds': LIMIT_SECONDS, 'block_size': BLOCK,
            'blocks': [], 'failures': [], 'gates': {}, 'completed_through': 0,
            'series': {'log_terms': 100, 'exp_terms': 40,
                       'sin_cos_terms_each': 48, 'atan_inverse_x_terms': 8},
            'qualification': 'Informal exact interval calculation, conditional transfer; no RH claim.'}

    def save():
        data['elapsed_seconds'] = time.monotonic()-started
        OUT.write_text(json.dumps(data, separators=(',', ':'))+'\n')

    def gate(name, test, value=None):
        data['gates'][name] = {'passed': bool(test)}
        if value is not None:
            data['gates'][name]['evidence'] = value
        if not test:
            raise ArithmeticError(name)

    save()
    try:
        t, x, one = IV(F(98, 625)), IV(6000000185827), IV(1)
        pi = pi_iv()
        rad = x/(4*pi)+t/16
        N = isqrt(rad.l//Q)
        lower, upper = rad-N*N, (N+1)**2-rad
        gate('floor_lower', lower.l > 0, lower.enc())
        gate('floor_upper', upper.l > 0, upper.enc())
        gate('agrees_with_audited_N', N == 690988)
        data['N'] = N
        d = 1+x*x
        # Principal logarithm, Re(s)>0, arg(s)=atan(x).
        arg = pi/2-atan_small(F(1, 6000000185827))
        au = log_iv(sqrt_iv(d)/(4*pi))/2-1/d
        av = arg/2-3*x/d
        inv_s, inv_sm = (2/d, -2*x/d), (-2/d, -2*x/d)
        ss, mm = cmul(inv_s, inv_s), cmul(inv_sm, inv_sm)
        aprime = (-ss[0]/2-mm[0]+inv_s[0]/2,
                  -ss[1]/2-mm[1]+inv_s[1]/2)
        sigma, tau = IV(F(1, 2))+t*au/2, x/2+t*av/2
        ell = 2*au+t*cmul((au, av), aprime)[0]
        logN, log32 = log_point(F(N)), log_point(F(32))
        g1, g2 = ell-logN-13, ell-2*log32
        gate('retained_ell_minus_logN_gt13', g1.l > 0, g1.enc())
        gate('retained_shift_positive', g2.l > 0, g2.enc())
        gate('retained_shift_lt25', g2.h < 25*Q, (25-g2).enc())
        # Amplitude exponents = u*(t*u/4-sigma), u>=0.
        gate('all_nonconstant_amplitude_exponents_negative',
             (sigma-t*logN/4).l > 0, (sigma-t*logN/4).enc())
        data['constants'] = {name: z.enc() for name, z in [
            ('pi', pi), ('radicand', rad), ('arg_s', arg), ('alpha_re', au),
            ('alpha_im', av), ('alpha_prime_re', aprime[0]),
            ('alpha_prime_im', aprime[1]), ('sigma', sigma), ('tau', tau),
            ('ell', ell), ('logN', logN), ('log32', log32)]}
        data['finite_remainders'] = {'exp_reduced': EXP_REMAINDER.enc(),
            'cos_absolute': str(COS_REMAINDER), 'sin_absolute': str(SIN_REMAINDER)}
        gate('exp_zero_exact', negative_exp(IV(0)).l == negative_exp(IV(0)).h == Q)
        chi0, rm, _, _ = physical_prime(IV(0), tau, 2*pi)
        gate('phase_zero_encloses_one', chi0[0].l <= Q <= chi0[0].h and chi0[1].l <= 0 <= chi0[1].h)
        save()
        # Complete smallest-prime-factor sieve; zero marks primes (and1).
        spf = array('I', [0])*(N+1)
        for p in range(2, isqrt(N)+1):
            if not spf[p]:
                for n in range(p*p, N+1, p):
                    if not spf[n]:
                        spf[n] = p
        keep = N//2
        logs, characters = [None]*(keep+1), [None]*(keep+1)
        logs[1], characters[1] = IV(0), (IV(1), IV(0))
        A, L = (IV(0), IV(0)), (IV(0), IV(0))
        twopi = 2*pi
        prime_count = 0
        for lo in range(1, N+1, BLOCK):
            hi = min(N, lo+BLOCK-1)
            ba, bl = (IV(0), IV(0)), (IV(0), IV(0))
            minimum_amplitude = None
            minimum_reduction = 4*Q
            maximum_phase_width = maximum_reduction_integer = 0
            max_log_width = max_chi_width = max_amp_width = 0
            primes_in_block = 0
            for n in range(lo, hi+1):
                if n == 1:
                    u, chi = logs[1], characters[1]
                elif spf[n]:
                    p, m = spf[n], n//spf[n]
                    assert p*m == n and 2 <= p <= m <= keep
                    u = logs[p]+logs[m]
                    chi = cmul(characters[p], characters[m])
                else:
                    u = log_point(F(n))
                    chi, margin, width, ki = physical_prime(u, tau, twopi)
                    minimum_reduction = min(minimum_reduction, margin)
                    maximum_phase_width = max(maximum_phase_width, width)
                    maximum_reduction_integer = max(maximum_reduction_integer, ki)
                    primes_in_block += 1
                if n <= keep:
                    logs[n], characters[n] = u, chi
                # u=log(n), chi=exp(-i*tau*u), every integer included.
                exponent = u*(t*u/4-sigma)
                amplitude = negative_exp(exponent)
                assert amplitude.l > 0
                term = amplitude*chi[0], amplitude*chi[1]
                weighted = u*term[0], u*term[1]
                ba = ba[0]+term[0], ba[1]+term[1]
                bl = bl[0]+weighted[0], bl[1]+weighted[1]
                minimum_amplitude = amplitude.l if minimum_amplitude is None else min(minimum_amplitude, amplitude.l)
                max_log_width = max(max_log_width, u.h-u.l)
                max_chi_width = max(max_chi_width, chi[0].h-chi[0].l, chi[1].h-chi[1].l)
                max_amp_width = max(max_amp_width, amplitude.h-amplitude.l)
            A = A[0]+ba[0], A[1]+ba[1]
            L = L[0]+bl[0], L[1]+bl[1]
            prime_count += primes_in_block
            data['blocks'].append({'lo': lo, 'hi': hi, 'count': hi-lo+1,
                'prime_count': primes_in_block, 'all_term_and_factorization_gates_passed': True,
                'min_amplitude_lower': str(minimum_amplitude),
                'min_prime_reduction_margin': str(minimum_reduction),
                'max_prime_theta_width': str(maximum_phase_width),
                'max_reduction_integer_abs': str(maximum_reduction_integer),
                'max_log_width': str(max_log_width), 'max_chi_component_width': str(max_chi_width),
                'max_amplitude_width': str(max_amp_width),
                'A_block': enc_complex(ba), 'L_block': enc_complex(bl)})
            data['completed_through'] = hi
            data['sums'] = {'A': enc_complex(A), 'L': enc_complex(L)}
            save()
            if len(data['blocks']) % 8 == 0 or hi == N:
                print(json.dumps({'through': hi, 'required': N,
                                  'elapsed_seconds': round(time.monotonic()-started, 2)}), flush=True)
            if hi < N and time.monotonic()-started > LIMIT_SECONDS:
                data['status'] = 'COST_STOP'
                data['failures'].append('complete_support_not_finished_within_deadline')
                save()
                print(json.dumps({'status': data['status'], 'through': hi, 'required': N, 'path': str(OUT)}), flush=True)
                return
        gate('complete_natural_support', data['blocks'][0]['lo'] == 1 and data['blocks'][-1]['hi'] == N
             and sum(v['count'] for v in data['blocks']) == N
             and all(a['hi']+1 == b['lo'] for a, b in zip(data['blocks'], data['blocks'][1:])))
        data['prime_count'] = prime_count
        S = ell*A[0]-2*L[0], ell*A[1]-2*L[1]
        value = A[0]*S[0]+A[1]*S[1]
        squared = A[0]*A[0]+A[1]*A[1]
        gate('positive_norm_squared', squared.l > 0, squared.enc())
        radius = sqrt_iv(squared)
        p, q = IV(F(101, 200000000)), IV(F(142, 10000000)+F(1, 250000000000))
        budget = p*(25*radius+F(81, 2))+q*radius+p*q
        paid, ceiling = value-budget, value+budget
        data['result'] = {'S': enc_complex(S), 'F': value.enc(), 'R': radius.enc(),
            'E': budget.enc(), 'F_minus_E': paid.enc(), 'F_plus_E': ceiling.enc(),
            'p': p.enc(), 'q': q.enc(), 'required_positive_threshold': '0',
            'required_negative_threshold': '0'}
        data['status'] = 'POSITIVE_PAID' if paid.l > 0 else 'NEGATIVE_PAID' if ceiling.h < 0 else 'INCONCLUSIVE'
        save()
        print(json.dumps({'status': data['status'], 'N': N, 'blocks': len(data['blocks']),
            'F': approx(value), 'R': approx(radius), 'E': approx(budget),
            'F_minus_E': approx(paid), 'F_plus_E': approx(ceiling),
            'failed_gates': data['failures'], 'path': str(OUT)}), flush=True)
    except Exception as exc:
        data['status'] = 'FAILED'
        data['failures'].append(type(exc).__name__+': '+str(exc))
        save()
        print(json.dumps({'status': 'FAILED', 'failures': data['failures'], 'path': str(OUT)}), flush=True)
        raise


if __name__ == '__main__':
    main()
