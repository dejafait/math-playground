#!/usr/bin/env python3
"""Fixed finite point prescription and exact planning certificate for C998c.

Default invocation runs setup and the error/work ledger, NOT the point oracle
or a norm batch. --point-code T optionally evaluates a single input code:
|t-T*2^-1024|<=2^-1024, with the true t in [a*2^-80,a].
All old artifacts are read without mutation. No arbitrary-precision API oracle.
"""
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as Q
from math import factorial
import argparse
import json
import numpy as np

B = Path(__file__).resolve().parent
SP, P, N, LOG_N = 1024, 4096, 2048, 512
SS, S = 1 << SP, 1 << P
setup_charge = 0
checks, snapshots = [], {}


def check(name, value):
    checks.append({'name': name, 'pass': bool(value)})


def ceildiv(x, y):
    return -((-x)//y)


def floor_sqrt(x):
    # Explicit finite bisection, not a free square-root oracle.
    assert 0 <= x < 1 << 2052
    lo, hi = 0, 1 << ((x.bit_length()+1)//2)
    while hi-lo > 1:
        mid = (lo+hi)//2
        if mid*mid <= x:
            lo = mid
        else:
            hi = mid
    return lo


class I:
    """Directed dyadic intervals. Charge64 bounded integer operations/call."""
    def __init__(self, lo, hi=None):
        self.lo, self.hi = lo, lo if hi is None else hi
        assert self.lo <= self.hi

    @staticmethod
    def rational(x):
        global setup_charge
        setup_charge += 64
        x = Q(x)
        return I(x.numerator*SS//x.denominator,
                 ceildiv(x.numerator*SS, x.denominator))

    def __add__(self, o):
        global setup_charge
        setup_charge += 64
        return I(self.lo+o.lo, self.hi+o.hi)

    def __neg__(self):
        global setup_charge
        setup_charge += 64
        return I(-self.hi, -self.lo)

    def __sub__(self, o):
        return self + (-o)

    def __mul__(self, o):
        global setup_charge
        setup_charge += 64
        t = [x*y for x in (self.lo, self.hi) for y in (o.lo, o.hi)]
        return I(min(t)//SS, ceildiv(max(t), SS))

    def __truediv__(self, o):
        global setup_charge
        setup_charge += 64
        assert o.lo > 0
        t = [(x*SS, y) for x in (self.lo, self.hi) for y in (o.lo, o.hi)]
        return I(min(x//y for x,y in t), max(ceildiv(x,y) for x,y in t))

    def sqrt(self):
        global setup_charge
        # <=1026 bisections per endpoint, <=8 primitive ops/iteration.
        setup_charge += 20000
        assert self.lo >= 0
        lo, hi = floor_sqrt(self.lo*SS), floor_sqrt(self.hi*SS)
        if hi*hi < self.hi*SS:
            hi += 1
        return I(lo, hi)

    def middle(self):
        return (self.lo+self.hi)//2


def series_atan(x, count):
    # Alternating series: enclose the finite sum and the next-term tail.
    xx, power, out = x*x, x, I(0)
    for j in range(count):
        term = power/I.rational(2*j+1)
        out = out + (term if j % 2 == 0 else -term)
        power = power*xx
    tail = power/I.rational(2*count+1)
    return I(out.lo-tail.hi, out.hi+tail.hi)


def series_log_rational(r):
    # r in [1,3]; z<=1/2. Whole positive tail, including input rounding.
    z = I.rational((r-1)/(r+1))
    zz, power, out = z*z, z, I(0)
    for j in range(LOG_N):
        out = out + power/I.rational(2*j+1)
        power = power*zz
    tail = (power/I.rational(2*LOG_N+1))/(I.rational(1)-zz)
    return I(2*out.lo, 2*out.hi+2*tail.hi)


def read(name):
    raw = (B/name).read_bytes()
    snapshots[name] = raw
    return json.loads(raw)


def fixed_series(Z):
    """Si, C=Ci-gamma-log, sin, cos at the exact dyadic Z/2^4096.

    Every division is floor rounding to the fixed dyadic lattice. Factorial
    terms use exact Z^2 and a SINGLE final division; no rounded z^2 is used.
    """
    assert 0 < Z < 1024*S
    zz, aa, bb = Z*Z, Z, S
    si = cc = sn = cs = 0
    for j in range(N):
        si += aa//(2*j+1)
        if j:
            cc += bb//(2*j)
        sn += aa
        cs += bb
        if j+1 < N:
            aa = (-aa*zz)//(((2*j+2)*(2*j+3)) << (2*P))
            bb = (-bb*zz)//(((2*j+1)*(2*j+2)) << (2*P))
    return si, cc, sn, cs


def fixed_log_unit(num, den):
    # exact rational1<=num/den<=2; perturbation and tail paid in C998c.
    assert den <= num <= 2*den
    zz = ((num-den)*S)//(num+den)
    z2, power, out = zz*zz, zz, 0
    for j in range(LOG_N):
        out += (2*power)//(2*j+1)
        if j+1 < LOG_N:
            power = (power*z2) >> (2*P)
    return out


def point(T, a, pi, log2, coefficients):
    """Return six dyadic centers, each with the PROVED radius2^-400.

    The caller supplies the input enclosure contract in the module docstring.
    No claim here certifies that an arbitrary caller supplied a valid code.
    """
    assert 0 < T < SS
    # t0=T/2^1024; a0=a.middle()/2^1024. Division and quantization
    # are performed together; clamp to the known normalized domain.
    snum = (T << 512)//a.middle()
    snum = max(1 << (512-80), min(1 << 512, snum))
    num, den = (1 << 512)+snum, snum
    exponent = num.bit_length()-den.bit_length()
    if num < den << exponent:
        exponent -= 1
    assert 1 <= exponent <= 81
    ll = exponent*(log2.middle() << (P-SP)) + fixed_log_unit(num, den << exponent)
    pv = pi.middle() << (P-SP)
    # n=0 is integrated explicitly. Constants gamma and log(k_n) cancel.
    integrals = [ll]
    for n in range(1, 256):
        z0 = (n*pv*snum) >> 513
        z1 = (n*pv*((1 << 512)+snum)) >> 513
        s0, c0, sn, cs = fixed_series(z0)
        s1, c1, _, _ = fixed_series(z1)
        integrals.append((cs*(ll+c1-c0)+sn*(s1-s0)) >> P)
    values = []
    for column in coefficients:
        for parity in (0, 1):
            out = 0
            for n in range(parity, 256, 2):
                out += (column[n].middle()*integrals[n]) >> SP
            values.append(out)
    return values


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--point-code', type=int)
    args = parser.parse_args()
    old = read('jump-log-h1-bounds-654.json')
    audit = read('jump-log-h1-audit-655.json')
    raw = (B/'frozen-reference-proposal-652.npz').read_bytes()
    snapshots['frozen-reference-proposal-652.npz'] = raw
    check('frozen archive SHA256', sha256(raw).hexdigest() ==
          '2b770a8a689a972ae487b9dd718e2e6d47b6769a5530e7fec244a102c5c317c6')
    check('complete654 certificate pinned by655', sha256(snapshots[
        'jump-log-h1-bounds-654.json']).hexdigest() == audit['input_sha256'][
        'jump-log-h1-bounds-654.json'])
    check('audit655 all41 checks pass', len(audit['checks']) == 41 and
          all(c['pass'] for c in audit['checks']) and audit['failures'] == [])
    with np.load(B/'frozen-reference-proposal-652.npz', allow_pickle=False) as data:
        free = data['free_middle_dyadics'].copy()
    check('entire frozen trial shape', free.shape == (254, 3) and np.isfinite(free).all())
    aq = [[Q(*float(free[i,j]).as_integer_ratio()) for i in range(254)] for j in range(3)]
    for j in range(3):
        stored = old['exact_free_middle_columns'][j]
        check(f'column{j} all254 dyadics match654', aq[j] == [
            Q(int(x['numerator']), int(x['denominator'])) for x in stored])
        mass = sum(map(abs, aq[j]), Q())
        check(f'column{j} coefficient envelope6mass<16', 6*mass < 16)
        check(f'column{j} all127 free coefficients per parity nonzero',
              all(sum(x != 0 for x in aq[j][p::2]) == 127 for p in (0,1)))
        check(f'column{j} all exact free dyadics lie on setup lattice',
              all(SS % x.denominator == 0 for x in aq[j]))

    one = I.rational(1)
    log2, log3 = series_log_rational(Q(2)), series_log_rational(Q(3))
    a = log3/I.rational(4)
    pi = I.rational(16)*series_atan(I.rational(Q(1,5)), 256) - \
         I.rational(4)*series_atan(I.rational(Q(1,239)), 256)
    constants = {'a': a, 'pi': pi, 'log2': log2}
    for name, val in constants.items():
        check(name+' complete enclosure width plus midpoint rounding<2^-980',
              val.hi-val.lo+1 < 1 << (SP-980))
    check('a in(1/4,3/10) and pi in(3,4)', a.lo > SS//4 and
          10*a.hi < 3*SS and 3*SS < pi.lo < pi.hi < 4*SS)

    sqrt2 = I.rational(2).sqrt()
    norm0, norm1 = (one/a).sqrt(), (I.rational(2)/a).sqrt()
    a2, pi2 = a*a, pi*pi
    coeffs, encoded = [], []
    for j in range(3):
        q = [I(0), I(0)] + [I.rational(x) for x in aq[j]]
        for n in range(2,256):
            den = a2 + I.rational(n*n)*pi2
            ratio = (sqrt2*a2 if n%2 == 0 else a2+pi2)/den
            q[n%2] = q[n%2] - ratio*q[n]
        b = [q[0]*norm0] + [(-q[n] if n%2 else q[n])*norm1 for n in range(1,256)]
        coeffs.append(b)
        encoded.append([{'lo': str(x.lo), 'hi': str(x.hi)} for x in b])
        for n,x in enumerate(b):
            check(f'column{j} mode{n} midpoint coefficient error<2^-900',
                  x.hi-x.lo+1 < 1 << (SP-900))
        check(f'column{j} enclosed total absolute coefficient mass<16',
              sum(max(abs(x.lo), abs(x.hi)) for x in b) < 16*SS)

    # Exact, complete selected load-bearing numbers; no floating estimates.
    tail_num, tail_den = 2*1024**(2*N), factorial(2*N)
    check('all four series tails<2^-1023', tail_num*(1 << 1023) < tail_den)
    check('all series rounding<2^-2025',
          (N*N*(1 << 2048)+N)*(1 << 2025) < 1 << P)
    check('normalized log whole tail<2^-1600',
          Q(2, 3**(2*LOG_N+1)*(2*LOG_N+1))*Q(9,8) < Q(1,1 << 1600))
    errors = {'normalized_input': Q(1,1 << 426),
              'coefficient_sum': Q(256*81,1 << 900),
              'mode_and_final_arithmetic': Q(1,1 << 930)}
    error = sum(errors.values(), Q())
    check('whole density error<2^-425', error < Q(1,1 << 425))
    check('advertised radius2^-400<=required2^-53', Q(1,1 << 400) < Q(1,1 << 53))
    check('setup charged scalar operations<=10000000', setup_charge <= 10_000_000)
    per_point_upper = 2*255*(64*N+64)+64*(LOG_N+256+16)+64*6*256
    check('complete per point bound<=70000000', per_point_upper <= 70_000_000)
    query_count = 302*37
    updates = 2*255*2*(N-1)
    per_point_lower = 2*updates  # each specified update: multiplication AND division
    lower = query_count*per_point_lower
    upper = 10_000_000+query_count*70_000_000
    ceiling = 100_000_000
    check('prescribed batch exceeds ceiling even before setup/remaining work', lower > ceiling)
    report = {'result': 'POINT_CERTIFICATE_WITH_PRESCRIPTION_COST_STOP',
        'checks': checks, 'failures': [c['name'] for c in checks if not c['pass']],
        'parameters': {'series_terms': N, 'fraction_bits': P, 'setup_bits': SP,
                       'log_terms': LOG_N, 'integer_register_bits_bound': 16384},
        'input_contract': '|t-T*2^-1024|<=2^-1024; true a*2^-80<=t<=a; caller certifies code',
        'constant_intervals_scale2^-1024': {k:{'lo':str(x.lo),'hi':str(x.hi)} for k,x in constants.items()},
        'all768_coefficient_intervals_scale2^-1024': encoded,
        'full_series_tail_majorant': {'numerator':str(tail_num), 'denominator':str(tail_den)},
        'error_terms': {k:{'numerator':str(x.numerator),'denominator':str(x.denominator)} for k,x in errors.items()},
        'whole_error_upper': {'numerator':str(error.numerator),'denominator':str(error.denominator)},
        'advertised_radius': '2^-400', 'required_error': '2^-53',
        'work': {'unit': 'bounded integer arithmetic/comparison/shift operation, <=16384-bit registers; roots expanded into bisection',
                 'setup_charge_executed': setup_charge, 'setup_prescription_upper': 10_000_000,
                 'per_point_lower': per_point_lower, 'per_point_upper': 70_000_000,
                 'query_count': query_count, 'batch_lower': lower, 'batch_upper': upper,
                 'declared_ceiling': ceiling, 'decision': 'STOP_THIS_PRESCRIPTION_BEFORE_BATCH'},
        'not_computed': ['point values in default ledger invocation', 'full residual norms',
                        'outer error or node generation', 'projection moments', 'inverse pairings', 'signs'],
        'input_sha256': {k:sha256(v).hexdigest() for k,v in snapshots.items()},
        'script_sha256': sha256(Path(__file__).read_bytes()).hexdigest()}
    if args.point_code is not None:
        # A single requested point only; never a batch. No such run is needed
        # to establish the uniform analytic certificate or planning decision.
        report['single_point'] = {'input_code': str(args.point_code),
            'dyadic_centers_scale2^-4096': [str(v) for v in point(args.point_code,a,pi,log2,coeffs)],
            'radius': '2^-400', 'input_enclosure_validated_by_this_script': False}
    dest = B/'finite-cosine-point-660.json'
    dest.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({'result':report['result'], 'checks':len(checks),
        'failures':report['failures'], 'error_upper':'<2^-425',
        'advertised_radius':'2^-400', 'required':'2^-53',
        'batch_work_lower':lower, 'batch_work_upper':upper, 'ceiling':ceiling,
        'point_or_norm_batch_executed':False if args.point_code is None else 'single point only',
        'certificate':str(dest.relative_to(B.parent.parent))}, indent=2))
    if report['failures']:
        raise SystemExit(1)


if __name__ == '__main__':
    # A selected exact factorial ratio is load bearing and exceeds Python's
    # conservative decimal-display limit. No entire old certificate is printed.
    import sys
    sys.set_int_max_str_digits(0)
    main()
