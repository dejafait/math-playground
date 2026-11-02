#!/usr/bin/env python3
"""Independent complete rational consumer for C499c; no producer imports.

The analytic/conceptual proof is in canonical C499c. This file checks every
stored mathematical field, elementary evaluation and producer assertion
against a reconstruction using endpoint pairs, and records full evidence.
The accepted L499 scalar/mass inputs are reused, with current hash linkage.
"""
from fractions import Fraction as Q
from hashlib import sha256
from math import isqrt, factorial
from pathlib import Path
from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING
import json

BASE = Path(__file__).resolve().parent
OUTPUT = BASE / 'c499c-certificate-audit.json'
SCALE = 10**60
evidence, assertions, elementary = [], [], []
stats = dict(reciprocals=0, square_roots=0, decoded_rationals=0,
             decoded_intervals=0)
result = dict(scope='C499c fixed endpoint only; source manuscripts retained as qualified imports.',
              method='Independent rational endpoint-pair reconstruction; no producer execution or imports.')


def floor_grid(q):
    return Q((q.numerator*SCALE)//q.denominator, SCALE)


def ceil_grid(q):
    return -floor_grid(-q)


def iv(q, h=None):
    return (Q(q), Q(q if h is None else h))


def plus(a, b):
    return floor_grid(a[0]+b[0]), ceil_grid(a[1]+b[1])


def neg(a):
    return -a[1], -a[0]


def minus(a, b):
    return plus(a, neg(b))


def times(a, b):
    candidates = (a[0]*b[0], a[0]*b[1], a[1]*b[0], a[1]*b[1])
    return floor_grid(min(candidates)), ceil_grid(max(candidates))


def divide(a, b):
    if b[0] <= 0 <= b[1]:
        raise ArithmeticError('interval divisor contains zero')
    stats['reciprocals'] += 1
    return times(a, (floor_grid(1/b[1]), ceil_grid(1/b[0])))


def sq(a):
    low = 0 if a[0] <= 0 <= a[1] else min(a[0]*a[0], a[1]*a[1])
    return floor_grid(Q(low)), ceil_grid(max(a[0]*a[0], a[1]*a[1]))


def root(a):
    if a[0] < 0:
        raise ArithmeticError('negative square-root input')
    l = isqrt((a[0].numerator*SCALE**2)//a[0].denominator)
    h = isqrt((a[1].numerator*SCALE**2)//a[1].denominator)+1
    low, high = Q(l, SCALE), Q(h, SCALE)
    if not (low**2 <= a[0] <= a[1] <= high**2):
        raise ArithmeticError('square-root endpoints not enclosing')
    stats['square_roots'] += 1
    return low, high


ZERO, ONE = iv(0), iv(1)


def cx(a=ZERO, b=ZERO):
    return a, b


def cadd(a, b):
    return plus(a[0], b[0]), plus(a[1], b[1])


def cneg(a):
    return neg(a[0]), neg(a[1])


def csub(a, b):
    return cadd(a, cneg(b))


def cmul(a, b):
    return (minus(times(a[0], b[0]), times(a[1], b[1])),
            plus(times(a[0], b[1]), times(a[1], b[0])))


def conj(a):
    return a[0], neg(a[1])


def cdiv(a, b):
    den = plus(sq(b[0]), sq(b[1]))
    if den[0] <= 0:
        raise ArithmeticError('unproved nonzero complex divisor')
    num = cmul(a, conj(b))
    return divide(num[0], den), divide(num[1], den)


def norm(a):
    return root(plus(sq(a[0]), sq(a[1])))


def cfields(a):
    return dict(real=a[0], imaginary=a[1], modulus=norm(a))


def encode(x):
    if isinstance(x, Q):
        return dict(numerator=str(x.numerator), denominator=str(x.denominator))
    if isinstance(x, tuple):
        if len(x) != 2 or not all(isinstance(y, Q) for y in x):
            raise TypeError('only real endpoint pairs are serialized as intervals')
        return dict(lower=encode(x[0]), upper=encode(x[1]))
    if isinstance(x, dict):
        return {k: encode(v) for k, v in x.items()}
    if isinstance(x, list):
        return [encode(y) for y in x]
    return x


def decode(x):
    if isinstance(x, dict):
        if set(x) == {'numerator', 'denominator'}:
            d = int(x['denominator'])
            if d <= 0:
                raise ValueError('nonpositive stored rational denominator')
            stats['decoded_rationals'] += 1
            return Q(int(x['numerator']), d)
        if set(x) == {'lower', 'upper'}:
            a = decode(x['lower']), decode(x['upper'])
            if not (isinstance(a[0], Q) and isinstance(a[1], Q) and a[0] <= a[1]):
                raise ValueError('invalid stored interval')
            stats['decoded_intervals'] += 1
            return a
        return {k: decode(v) for k, v in x.items()}
    if isinstance(x, list):
        return [decode(v) for v in x]
    if isinstance(x, float):
        raise ValueError('floating point data in rational certificate')
    return x


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def load(name):
    path = BASE/name
    result.setdefault('inputs', []).append(dict(path=name, sha256=digest(path)))
    return decode(json.loads(path.read_text()))


def verify(name, passed, actual, required):
    evidence.append(dict(name=name, passed=bool(passed), actual=actual, required=required))
    if not passed:
        raise AssertionError(name)


def equal(name, actual, expected):
    verify(name, actual == expected, actual, expected)


def predicate(name, passed, actual, required):
    # Recompute truth before comparing the producer's stored assertion.
    assertions.append(dict(name=name, passed=bool(passed), actual=actual, required=required))
    verify('independent predicate: '+name, passed, actual, required)


def ln_reduced(v):
    if not 1 <= v <= 2:
        raise ArithmeticError('log reduced argument outside [1,2]')
    z = (v-1)/(v+1)
    power, acc = iv(z), ZERO
    for j in range(100):
        acc = plus(acc, divide(power, iv(2*j+1)))
        power = times(power, iv(z*z))
    tail = 2*power[1]/(201*(1-z*z))
    answer = floor_grid(2*acc[0]), ceil_grid(2*acc[1]+tail)
    elementary.append(dict(kind='log_unit', v=v, z=z, terms=100,
                           half_sum=acc, first_omitted_power=power,
                           tail_upper=tail, enclosure=answer))
    return answer


def logarithm(a):
    if a <= 0:
        raise ArithmeticError('nonpositive logarithm')
    # Determine the exact dyadic exponent independently from bit lengths.
    k = a.numerator.bit_length()-a.denominator.bit_length()
    v = a/(Q(2)**k)
    if v < 1:
        k, v = k-1, 2*v
    if v >= 2:
        k, v = k+1, v/2
    return plus(times(iv(k), LOG_TWO), ln_reduced(v))


def log_interval(a):
    left, right = logarithm(a[0]), logarithm(a[1])
    return left[0], right[1]


def exponential(a):
    u, acc, term = abs(a), ONE, ONE
    if not u < 182:
        raise ArithmeticError('exponential tail ratio is not below one')
    for j in range(1, 181):
        term = divide(times(term, iv(u)), iv(j))
        acc = plus(acc, term)
    ratio = u/182
    tail = term[1]*u/181/(1-ratio)
    pos = acc[0], ceil_grid(acc[1]+tail)
    answer = divide(ONE, pos) if a < 0 else pos
    elementary.append(dict(kind='exp', argument=a, degree=180, sum=acc,
                           last_term=term, subsequent_ratio_cap=ratio,
                           tail_upper=tail, positive_enclosure=pos, enclosure=answer))
    return answer


def exp_interval(a):
    low, high = exponential(a[0]), exponential(a[1])
    return low[0], high[1]


def phase_value(a, label):
    ratio = ((a[0]+a[1])/2)/(PI[0]+PI[1])+Q(1, 2)
    turns = ratio.numerator//ratio.denominator
    reduced = minus(a, times(iv(2*turns), PI))
    radius = max(abs(x) for x in reduced)
    if radius > 4:
        raise ArithmeticError('reduced phase outside [-4,4]')
    sine, cosine, term = ZERO, ZERO, ONE
    for degree in range(160):
        if degree % 2:
            sine = plus(sine, term) if degree % 4 == 1 else minus(sine, term)
        else:
            cosine = plus(cosine, term) if degree % 4 == 0 else minus(cosine, term)
        term = divide(times(term, reduced), iv(degree+1))
    remainder = ceil_grid(radius**160/factorial(160))
    sine, cosine = plus(sine, iv(-remainder, remainder)), plus(cosine, iv(-remainder, remainder))
    n2 = plus(sq(sine), sq(cosine))
    predicate('unit phase '+label, n2[0] <= 1 <= n2[1], n2, 1)
    elementary.append(dict(kind='cis', label=label, phase=a, turns=turns,
                           reduced=reduced, degree=159, tail_upper=remainder,
                           sine=sine, cosine=cosine))
    return cosine, sine


def run():
    global PI, LOG_TWO
    source = load('phase-sensitive-256-block-certificate.json')
    corner = load('fixed-corner-two-charge.json')
    audit = load('l499-certificate-audit.json')
    result['producer_sha256'] = digest(BASE/'phase-sensitive-256-block-certificate.py')
    equal('producer source hash', source['script_sha256'], result['producer_sha256'])
    equal('exact producer input identities', source['inputs'], result['inputs'][1:])
    # Prior audit is accepted mathematics; its status alone is not a new proof.
    equal('retained L499 audit status', [audit['result'], audit['failures']], ['PASS', []])
    corner_hash = digest(BASE/'fixed-corner-two-charge.json')
    recorded = [r['sha256'] for r in audit['inputs'] if r['path'] == 'fixed-corner-two-charge.json']
    predicate('corner retained by independent audit', recorded == [corner_hash], corner_hash, 'audited corner hash')
    for entry in audit['inputs']:
        current = digest(BASE/entry['path'])
        predicate('audited input unchanged '+entry['path'], current == entry['sha256'], current, entry['sha256'])
    t, X, n, N = Q('.16836'), Q('6000284561421.5'), 691004, 691260
    ell0, cap, eps = Q('24.18022820120389'), Q('.500000000001'), Q('.0000006')
    eps1 = (eps+Q('.0000013'))*Q('8.770232')/Q('.14142')
    reserve = Q(14176540015048665224252705167939023,33554432000000000000000000000000000000)
    PI = corner['elementary_inputs']['pi']
    lx, sigma_x = corner['elementary_inputs']['L'], corner['elementary_inputs']['sigma']
    LOG_TWO = ln_reduced(Q(2))
    bound = corner['bounds']
    R, Jcap, D = [bound[k] for k in ('R', 'Jplus', 'product_derivative_cap')]
    verify('positive accepted inputs', min(PI[0], lx[0], sigma_x[0], R[0], Jcap[0], D[0]) > 0,
           dict(pi=PI, L=lx, sigma=sigma_x, R=R, J=Jcap, D=D), '>0')
    predicate('exact reserve', bound['reserve_lower'] == reserve, bound['reserve_lower'], reserve)
    old_parameters = dict(x=X, t=t, N=n, ell0=ell0, cap=cap, epsilon=eps,
                          epsilon_1=eps1, grid_denominator=str(10**50))
    predicate('exact inherited parameters', corner['parameters'] == old_parameters,
              corner['parameters'], old_parameters)
    predicate('block length', N-n == 256, N-n, 256)
    coef = Q(N*N)-t/16
    Y = times(times(iv(4), PI), iv(coef))
    domain_log = plus(lx, divide(minus(Y, iv(X)), iv(X)))
    predicate('closed analytic domain', Y[0] > X and t*domain_log[1] < Q('5.17'),
              dict(Y=Y, tL=times(iv(t), domain_log)), 'Y>X; tL<5.17')
    predicate('symbolic canonical cutoff equality', coef+t/16 == N*N, coef+t/16, N*N)
    rebuilt = dict(parameters=dict(t=t, X=X, old_N=n, new_N=N, count=N-n,
                    ell0=ell0, cap=cap, epsilon=eps, epsilon_1=eps1, r0=reserve,
                    grid_denominator=str(SCALE), channels_per_primitive=2**63))
    u = divide(ONE, Y)
    verify('arctangent alternating series domain', 0 < u[0] <= u[1] < 1, u, '(0,1)')
    atan_lo = minus(u, divide(times(times(u, u), u), iv(3)))[0]
    argz = minus(divide(PI, iv(2)), (atan_lo, u[1]))
    yy1 = plus(ONE, times(Y, Y))
    lstar = minus(divide(log_interval(yy1), iv(2)), log_interval(times(iv(4), PI)))
    alpha = (minus(divide(lstar, iv(2)), divide(ONE, yy1)),
             minus(divide(argz, iv(2)), divide(times(iv(3), Y), yy1)))
    sigma = plus(iv(Q(1, 2)), divide(times(iv(t), alpha[0]), iv(2)))
    eta = plus(divide(Y, iv(2)), divide(times(iv(t), alpha[1]), iv(2)))
    qa = divide(times(Y, plus(times(Y, Y), iv(5))), times(yy1, yy1))
    ca = divide(minus(times(times(iv(7), Y), Y), iv(5)), times(yy1, yy1))
    aprime = ca, neg(qa)
    nuprime = (divide(times(iv(t), qa), iv(4)),
               plus(iv(Q(1, 2)), divide(times(iv(t), ca), iv(4))))
    theta = plus(plus(minus(PI, divide(argz, iv(4))),
                      divide(times(Y, minus(lstar, ONE)), iv(4))),
                 divide(times(times(iv(t), alpha[0]), alpha[1]), iv(2)))
    v = phase_value(theta, 'Theta')
    # Independent Eratosthenes sieve, not producer trial division.
    sieve = [True]*308
    sieve[0:2] = [False, False]
    for p in range(2, 18):
        if sieve[p]:
            for j in range(p*p, 308, p):
                sieve[j] = False
    primes = [p for p in range(308) if sieve[p]]
    predicate('complete prime set', len(primes) == 63 and [r['p'] for r in corner['prime_rows']] == primes,
              primes, 'all primes<=307')
    E, Elog, J, logsum = cx(ONE), cx(), cx(), ZERO
    prows = []
    for p, old in zip(primes, corner['prime_rows']):
        h = old['log_p']
        exponent = minus(divide(times(times(iv(t), h), h), iv(4)), times(sigma, h))
        w = exp_interval(exponent)
        a = cmul(phase_value(times(neg(eta), h), 'prime '+str(p)), cx(w))
        f = csub(cx(ONE), a)
        predicate('nonzero Euler factor '+str(p), w[1] < 1, w, '<1')
        Elog = csub(cmul(Elog, f), cmul(cmul(E, cx(h)), a))
        E = cmul(E, f)
        J = cadd(J, cdiv(cmul(cx(h), a), f))
        logsum = plus(logsum, h)
        prows.append(dict(p=p, log_p=h, radius=w, A=cfields(a), factor=cfields(f)))
    rho = norm(E)
    ell = minus(times(iv(2), cadd(alpha, cmul(cmul(cx(iv(t/2)), alpha), aprime))[0]),
                times(iv(4), cmul(nuprime, J)[1]))
    predicate('actual positive phase floor', ell[0] > ell0, ell, ell0)
    predicate('sigma increases', sigma[0] > sigma_x[1], sigma, sigma_x)
    ds, dl, weights, absolute, absolute_support = cx(), cx(), ZERO, ZERO, ZERO
    jrows = []
    for j in range(n+1, N+1):
        h = logarithm(Q(j))
        exponent = minus(divide(times(times(iv(t), h), h), iv(4)), times(sigma, h))
        w = exp_interval(exponent)
        a = cmul(phase_value(times(neg(eta), h), 'primitive '+str(j)), cx(w))
        ds, dl = cadd(ds, a), cadd(dl, cmul(cx(h), a))
        ab = times(times(w, R), plus(ONE, divide(times(iv(2), plus(h, Jcap)), iv(ell0))))
        ab_support = times(times(w, R), plus(ONE, divide(times(iv(2), plus(h, logsum)), iv(ell0))))
        weights, absolute, absolute_support = plus(weights, w), plus(absolute, ab), plus(absolute_support, ab_support)
        jrows.append(dict(j=j, log_j=h, radius=w, term=cfields(a),
                          absolute_channel_envelope=ab, maximum_support_envelope=ab_support))
    dz = cmul(cmul(cx(rho), v), ds)
    dw = cmul(cmul(cx(rho), v), csub(dl, cmul(J, ds)))
    dg = cadd(csub(dz, cdiv(dw, cx(ell))), cdiv(conj(dw), cx(ell)))
    phase_hat = cdiv(cmul(v, conj(E)), cx(rho))
    wd = cmul(phase_hat, cadd(cmul(E, dl), cmul(Elog, ds)))
    zd = cmul(cmul(phase_hat, E), ds)
    gd = cadd(csub(zd, cdiv(wd, cx(ell))), cdiv(conj(wd), cx(ell)))
    diff = csub(gd, dg)
    predicate('product-rule recurrence agrees', all(a[0] <= 0 <= a[1] for a in diff),
              cfields(diff), 'both coordinates contain zero')
    bg = norm(dg)
    support = plus(jrows[-1]['log_j'], logsum)
    primitive_cap = plus(iv(Q(53, 3)), weights)
    kcap = times(times(R, primitive_cap), support)
    qx, ccx = X*(X*X+5)/(1+X*X)**2, (7*X*X-5)/(1+X*X)**2
    us = divide(times(iv(t*(qx+ccx)), kcap), iv(ell0))
    ur = plus(divide(times(R, iv(eps)), iv(2)),
              divide(times(iv(2), plus(times(D, iv(eps)), times(R, iv(eps1)))), iv(ell0)))
    total = plus(plus(bg, us), ur)
    margin = minus(iv(reserve), total)
    rebuilt.update(domain=dict(Y=Y, L_upper=domain_log, symbolic_cutoff=N,
                               derivative_frozen_at=N, old_model_only_finite=True),
                   actual_phase=dict(Lstar=lstar, arg_z=argz, alpha=cfields(alpha), sigma=sigma,
                                     eta=eta, theta=theta, ell=ell, E=cfields(E), J=cfields(J),
                                     rho=rho, nu_prime=cfields(nuprime)),
                   prime_rows=prows, primitive_rows=jrows,
                   increment=dict(DeltaS=cfields(ds), DeltaL=cfields(dl), DeltaZ=cfields(dz),
                                  DeltaW=cfields(dw), DeltaG=cfields(dg), B_G=bg,
                                  product_rule_Elog=cfields(Elog), direct_recurrence_G=cfields(gd),
                                  recurrence_difference=cfields(diff)),
                   envelopes=dict(R0=R, J0=Jcap, D0=D, block_weight_sum=weights,
                                  new_primitive_sum_cap=primitive_cap, full_output_log_cap=support,
                                  new_Lhat_cap=kcap, Q_at_X=qx, C_at_X=ccx, charge_saddle_new=us,
                                  charge_remainder_new=ur, absolute_channel_block=absolute,
                                  maximum_support_absolute_block=absolute_support,
                                  absolute_to_actual_ratio=divide(absolute, bg), combined_cost=total,
                                  reserve_lower=reserve, margin=margin))
    predicate('phase-sensitive strict reserve', total[1] < reserve, total, reserve)
    predicate('phase-sensitive saving', bg[1] < absolute[0], bg, absolute)
    predicate('resolved budget width', total[1]-total[0] < Q(1, 10**30), total[1]-total[0], '<1e-30')
    result['reconstruction'] = rebuilt
    result['elementary_reconstruction'] = elementary
    # Compare every field, not just the producer's success labels or previews.
    for key in ('parameters', 'domain', 'actual_phase', 'increment', 'envelopes'):
        equal('complete reconstructed '+key, source[key], rebuilt[key])
    for key, idfield, wanted in (('prime_rows', 'p', primes), ('primitive_rows', 'j', list(range(n+1, N+1)))):
        equal('complete ordered '+key+' identifiers', [r[idfield] for r in source[key]], wanted)
        for row, expected in zip(source[key], rebuilt[key]):
            equal('complete '+key+' row '+str(expected[idfield]), row, expected)
    equal('elementary evaluation count', len(source['elementary_evaluations']), len(elementary))
    for k, (row, expected) in enumerate(zip(source['elementary_evaluations'], elementary)):
        equal('complete elementary evaluation '+str(k), row, expected)
    equal('producer assertion count', len(source['checks']), len(assertions))
    for k, (row, expected) in enumerate(zip(source['checks'], assertions)):
        equal('complete producer assertion '+str(k), row, expected)
    equal('producer failure list', source['failures'], [])
    equal('producer result after independent reconstruction', source['result'], 'PASS')
    equal('no hidden producer exception', source.get('exception'), None)
    counts = {kind: sum(r['kind'] == kind for r in elementary) for kind in ('cis', 'exp', 'log_unit')}
    equal('all phase labels exactly once', [r['label'] for r in elementary if r['kind'] == 'cis'],
          ['Theta']+['prime '+str(p) for p in primes]+['primitive '+str(j) for j in range(n+1, N+1)])
    equal('expected elementary record counts', counts, dict(cis=320, exp=638, log_unit=261))
    result['counts'] = dict(prime_rows=len(prows), primitive_rows=len(jrows),
                            elementary=counts, original_assertions=len(assertions))
    # Check every displayed strict conclusion using exact decimal rationals.
    for key, bound_value in [('B_G', Q('.000000050913372122')),
                              ('combined_cost', Q('.000020881403151711')),
                              ('charge_saddle_new', Q('1.254886140805040147918351e-11')),
                              ('charge_remainder_new', Q('.000020830477230728159125102344'))]:
        actual = bg if key == 'B_G' else rebuilt['envelopes'][key]
        verify('published upper bound '+key, actual[1] < bound_value, actual, bound_value)
    verify('published margin lower bound', margin[0] > Q('.000401612412718832'), margin, '>.000401612412718832')
    verify('published ell bracket', Q('27.7359997688') < ell[0] <= ell[1] < Q('27.7359997689'), ell, '(27.7359997688,27.7359997689)')
    verify('published absolute-channel bracket', Q('.000701363160671208') < absolute[0] <= absolute[1] < Q('.000701363160671209'), absolute, '(.000701363160671208,.000701363160671209)')
    verify('published ratio lower bound', rebuilt['envelopes']['absolute_to_actual_ratio'][0] > 13775,
           rebuilt['envelopes']['absolute_to_actual_ratio'], '>13775')
    verify('published maximum-support lower bound', absolute_support[0] > Q('.00804038'), absolute_support, '>.00804038')


try:
    run()
except Exception as exc:
    result['exception'] = f'{type(exc).__name__}: {exc}'
    if not evidence or evidence[-1]['passed']:
        evidence.append(dict(name='consumer completed', passed=False, actual=result['exception'], required='no exception'))
failures = [r['name'] for r in evidence if not r['passed']]
result.update(result='FAIL' if failures else 'PASS', failures=failures, checks=evidence,
              rebuilt_producer_assertions=assertions, arithmetic_stats=stats,
              script_sha256=digest(Path(__file__)))
OUTPUT.write_text(json.dumps(encode(result), indent=2)+'\n')


def decimal(q, upward):
    with localcontext() as ctx:
        ctx.prec = 27
        ctx.rounding = ROUND_CEILING if upward else ROUND_FLOOR
        return str(Decimal(q.numerator)/Decimal(q.denominator))


print(f"{result['result']}: {len(evidence)} independent checks; failures={failures}")
if 'counts' in result:
    print(f"complete consumption: {result['counts']}")
if 'reconstruction' in result:
    r = result['reconstruction']
    for key, pair in [('B_G', r['increment']['B_G']), ('ell', r['actual_phase']['ell'])]+[
            (key, r['envelopes'][key]) for key in ('charge_saddle_new', 'charge_remainder_new', 'combined_cost', 'margin')]:
        print(f"{key} in [{decimal(pair[0], False)}, {decimal(pair[1], True)}]")
    print('required combined_cost < '+decimal(r['envelopes']['reserve_lower'], False))
print('certificate='+str(OUTPUT.relative_to(BASE.parent.parent)))
raise SystemExit(bool(failures))
