#!/usr/bin/env python3
"""One frozen direct-theta Simpson/Taylor attempt. Canonical proof: C919f."""
import decimal
from decimal import Decimal as D
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import hashlib
import json
import platform
import sys
import time

PREC, U, N, PANELS, SPACE_CELLS, TIME_CELLS = 80, 4, 4, 2**18, 1024, 128
XS = [F(14), F(29, 2), F(41, 2), F(43, 2), F(49, 2), F(51, 2)]
ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'six_endpoint_2167.json'
PREFLIGHT = ROOT / 'six_endpoint_preflight_2167.json'
started = time.monotonic()
contexts = {}
for key, rounding in [('lo', decimal.ROUND_FLOOR),
                      ('hi', decimal.ROUND_CEILING),
                      ('near', decimal.ROUND_HALF_EVEN)]:
    c = decimal.Context(prec=PREC, rounding=rounding,
                        Emin=-999999, Emax=999999)
    for sig in c.traps:
        c.traps[sig] = sig not in (decimal.Inexact, decimal.Rounded)
    c.clear_flags()
    contexts[key] = c
lo, hi, near = (contexts[k] for k in ('lo', 'hi', 'near'))
counts = dict(nodes=0, spatial_cells=0, time_cells=0,
              exp_endpoint_calls=0, trig_rotations=0)


def pt(x):
    return D(x), D(x)


def rat(x):
    x = F(x)
    return (lo.divide(D(x.numerator), D(x.denominator)),
            hi.divide(D(x.numerator), D(x.denominator)))


def add(a, b):
    return lo.add(a[0], b[0]), hi.add(a[1], b[1])


def neg(a):
    return a[1].copy_negate(), a[0].copy_negate()


def sub(a, b):
    return add(a, neg(b))


def mulpos(a, b):
    """a is nonnegative; b may have either sign."""
    assert a[0] >= 0
    return (lo.multiply(a[1] if b[0] < 0 else a[0], b[0]),
            hi.multiply(a[1] if b[1] > 0 else a[0], b[1]))


def mul(a, b):
    if a[0] >= 0:
        return mulpos(a, b)
    if b[0] >= 0:
        return mulpos(b, a)
    return (min(lo.multiply(x, y) for x in a for y in b),
            max(hi.multiply(x, y) for x in a for y in b))


def divpos(a, b):
    assert a[0] >= 0 and b[0] > 0
    return lo.divide(a[0], b[1]), hi.divide(a[1], b[0])


def power(a, n):
    assert n >= 0 and a[0] >= 0
    out = pt(1)
    for _ in range(n):
        out = mulpos(out, a)
    return out


def expi(a):
    counts['exp_endpoint_calls'] += 2
    return lo.next_minus(near.exp(a[0])), hi.next_plus(near.exp(a[1]))


def upow(a, n):
    assert a >= 0 and n >= 0
    q = D(1)
    for _ in range(n):
        q = hi.multiply(q, a)
    return q


def usum(xs):
    q = D(0)
    for x in xs:
        q = hi.add(q, x)
    return q


def umul(*xs):
    q = D(1)
    for x in xs:
        assert x >= 0
        q = hi.multiply(q, x)
    return q


def atan_bounds(q, terms):
    s = sum((F((-1)**k, (2*k+1)*q**(2*k+1))
             for k in range(terms)), F(0))
    t = F((-1)**terms, (2*terms+1)*q**(2*terms+1))
    return min(s, s+t), max(s, s+t)


def si(a):
    return dict(lower=str(a[0]), upper=str(a[1]))


def flags():
    return {key: {s.__name__: bool(v) for s, v in c.flags.items()}
            for key, c in contexts.items()}


def runtime():
    ff = flags()
    unexpected = [(k, n) for k, dd in ff.items() for n, v in dd.items()
                  if v and n not in ('Inexact', 'Rounded')]
    return dict(python=sys.version, implementation=platform.python_implementation(),
                decimal_module=decimal.__file__, libmpdec=decimal.__libmpdec_version__,
                contexts={k: str(c) for k, c in contexts.items()}, flags=ff,
                unexpected_signals=unexpected, counts=counts.copy(),
                elapsed_seconds=time.monotonic()-started,
                trust_assumption='Correct CPython integers/Fraction and libmpdec directed basic operations, neighbors and correctly-rounded exp; runtime checks do not prove the backend.')


a5, a239 = atan_bounds(5, 80), atan_bounds(239, 25)
piq = 16*a5[0]-4*a239[1], 16*a5[1]-4*a239[0]
assert F(3) < piq[0] < piq[1] < F(22, 7)
assert piq[1]**2 < 10
pi = rat(piq[0])[0], rat(piq[1])[1]
assert sum((F(3)**k/factorial(k) for k in range(9)), F(0)) > 20
assert expi(pt(0))[0] <= 1 <= expi(pt(0))[1]
assert 2 < expi(pt(1))[0] < expi(pt(1))[1] < 3
q = F(1, 20)
assert 80*(1+11*q+11*q*q+q**3)/(1-q)**5 < 200
assert (1+11*F(1, 2)+11*F(1, 2)**2+F(1, 2)**3)/(1-F(1, 2))**5 == 300
assert F(4, 20)+F(45, 2) < 2*4**2
rates = [mulpos(pi, pt(n*n)) for n in range(1, N+1)]
center, radius = pt('0.025'), D('0.025')
h, cell_width = rat(F(U, PANELS)), rat(F(U, SPACE_CELLS))
assert h[0] == h[1] and cell_width[0] == cell_width[1]
index_factor = mulpos(pt(15000000), expi(pt(-75)))
spatial = mulpos(rat(F(200, 768)), expi(pt(-384)))[1]


def index_bound(p):
    return hi.multiply(index_factor[1], rat(F(factorial(p), 145**(p+1)))[1])


def exponent_derivative_bounds(l, r, time_upper):
    """Positive sum of magnitude bounds for both kernel exponentials."""
    vl_base = expi(pt(lo.multiply(D(2), l)))[0]
    vr_base = expi(pt(hi.multiply(D(2), r)))[1]
    accum = [D(0)]*5
    for rate in rates:
        vl = lo.multiply(rate[0], vl_base)
        vr = hi.multiply(rate[1], vr_base)
        for b, pref in [(D('4.5'), umul(D(8), rate[1], rate[1])),
                        (D('2.5'), umul(D(12), rate[1]))]:
            upper_exponent = hi.subtract(usum([umul(time_upper, r, r),
                                               umul(b, r)]), vl)
            e0 = umul(pref, expi(pt(upper_exponent))[1])
            a1 = usum([umul(D(2), time_upper, r), b, umul(D(2), vr)])
            a2 = usum([umul(D(2), time_upper), umul(D(4), vr)])
            a3, a4 = umul(D(8), vr), umul(D(16), vr)
            bell = [D(1), a1, usum([upow(a1, 2), a2]),
                    usum([upow(a1, 3), umul(D(3), a1, a2), a3]),
                    usum([upow(a1, 4), umul(D(6), a1, a1, a2),
                          umul(D(3), a2, a2), umul(D(4), a1, a3), a4])]
            accum = [hi.add(s, umul(e0, bq)) for s, bq in zip(accum, bell)]
    return accum


max4 = [[D(0)]*9 for _ in XS]
max4_cells = [[None]*9 for _ in XS]
spatial_rows = []
compact9 = D(0)
for k in range(SPACE_CELLS):
    l = rat(F(U*k, SPACE_CELLS))[0]
    r = rat(F(U*(k+1), SPACE_CELLS))[1]
    eb = exponent_derivative_bounds(l, r, D('0.025'))
    eb_time = exponent_derivative_bounds(l, r, D('0.05'))[0]
    ninth_part = umul(cell_width[1], upow(r, 18), eb_time)
    compact9 = hi.add(compact9, ninth_part)
    for j in range(9):
        pp = [hi.divide(umul(D(factorial(2*j)//factorial(2*j-t)),
                               upow(r, 2*j-t)), D(factorial(j)))
              if t <= 2*j else D(0) for t in range(5)]
        db = [usum(umul(D(comb(t, s)), pp[s], eb[t-s])
                   for s in range(t+1)) for t in range(5)]
        for ix, x in enumerate(XS):
            xd = rat(x)[1]
            bound = usum(umul(D(comb(4, t)), db[t], upow(xd, 4-t))
                         for t in range(5))
            if bound > max4[ix][j]:
                max4[ix][j], max4_cells[ix][j] = bound, k
    spatial_rows.append(dict(index=k, interval=si((l, r)),
                             exponential_derivative_bounds=list(map(str, eb)),
                             time_envelope=str(eb_time), ninth_integral_upper=str(ninth_part)))
    counts['spatial_cells'] += 1

tail_rows = [dict(j=j, theta_index_error=str(hi.divide(index_bound(2*j), D(factorial(j)))),
                  spatial_error=str(hi.divide(spatial, D(factorial(j))))) for j in range(9)]
time9 = usum([compact9, index_bound(18), spatial])
time_error = hi.divide(umul(time9, upow(radius, 9)), D(factorial(9)))
simpson_factor = rat(F(U**5, 180*PANELS**4))[1]
simpson = [[umul(simpson_factor, m) for m in row] for row in max4]
totals = [usum(umul(upow(radius, j), usum([simpson[ix][j],
                         D(tail_rows[j]['theta_index_error']), D(tail_rows[j]['spatial_error'])]))
                 for j in range(9)) for ix in range(len(XS))]
preflight = dict(status='READY_FOR_FIXED_NODE_PASS',
                 parameters=dict(U=U, N=N, digits=PREC, degree=8, center='1/40',
                                 panels=PANELS, spatial_cells=SPACE_CELLS, time_cells=TIME_CELLS),
                 constants=dict(pi=si(pi), exact_pi_bounds=list(map(str, piq)),
                                atan_terms=dict(q5=80, q239=25)),
                 tails=tail_rows, spatial_error_all_p_le_18=str(spatial),
                 complete_ninth=dict(compact=str(compact9), theta_index=str(index_bound(18)),
                                     spatial=str(spatial), bound=str(time9), remainder=str(time_error)),
                 spatial_cells=spatial_rows,
                 endpoint_error_bounds=[dict(x=str(x), fourth_derivatives=list(map(str, max4[ix])),
                       maximum_cells=max4_cells[ix], simpson_errors=list(map(str, simpson[ix])),
                       polynomial_error=str(totals[ix]), total_with_time_error=str(hi.add(totals[ix], time_error)))
                       for ix, x in enumerate(XS)], runtime=runtime(), failures=[])
assert not preflight['runtime']['unexpected_signals']
PREFLIGHT.write_text(json.dumps(preflight, indent=2)+'\n')
print('Preflight complete; full bounds:', PREFLIGHT, flush=True)
print('Complete ninth derivative upper:', time9, 'time error:', time_error, flush=True)
for row in preflight['endpoint_error_bounds']:
    print('x='+row['x']+' analytic error <= '+row['total_with_time_error']+'; required final signed margin > 0', flush=True)


def trig_step(t):
    """Taylor degree31 at one positive mesh angle, with full remainder."""
    assert 0 < t[0] <= t[1] < D('0.001')
    cs, sn = pt(0), pt(0)
    for k in range(16):
        ct = mulpos(power(t, 2*k), rat(F(1, factorial(2*k))))
        st = mulpos(power(t, 2*k+1), rat(F(1, factorial(2*k+1))))
        cs = add(cs, ct) if k % 2 == 0 else sub(cs, ct)
        sn = add(sn, st) if k % 2 == 0 else sub(sn, st)
    rem = hi.divide(upow(t[1], 32), D(factorial(32)))
    cs = lo.subtract(cs[0], rem), hi.add(cs[1], rem)
    sn = lo.subtract(sn[0], rem), hi.add(sn[1], rem)
    assert cs[0] > 0 and sn[0] > 0
    return cs, sn, rem


steps = [trig_step(mulpos(rat(x), h)) for x in XS]
cosines, sines = [pt(1) for _ in XS], [pt(0) for _ in XS]
sums = [[pt(0) for _ in range(9)] for _ in XS]
node_unit = h[0]
assert F(node_unit) == F(U, PANELS)
for i in range(PANELS+1):
    # Dyadic node has at most 23 significant decimal digits: product exact.
    u = pt(near.multiply(D(i), node_unit))
    u2 = mulpos(u, u)
    exp2u = expi(mulpos(pt(2), u))
    common = mulpos(center, u2)
    halfu = mulpos(pt('0.5'), u)
    kernel = pt(0)
    for rate in rates:
        v = mulpos(rate, exp2u)
        poly = mulpos(mulpos(pt(4), v), sub(mulpos(pt(2), v), pt(3)))
        assert poly[0] > 0
        term = mulpos(poly, expi(sub(add(common, halfu), v)))
        kernel = add(kernel, term)
    moment = mulpos(pt(1 if i in (0, PANELS) else (4 if i % 2 else 2)), kernel)
    for j in range(9):
        for ix in range(len(XS)):
            sums[ix][j] = add(sums[ix][j], mulpos(moment, cosines[ix]))
        if j < 8:
            moment = divpos(mulpos(moment, u2), pt(j+1))
    counts['nodes'] += 1
    if i < PANELS:
        for ix, (cstep, sstep, _) in enumerate(steps):
            c, s = cosines[ix], sines[ix]
            cosines[ix] = sub(mulpos(cstep, c), mulpos(sstep, s))
            sines[ix] = add(mulpos(cstep, s), mulpos(sstep, c))
            counts['trig_rotations'] += 1
    if i and i % 32768 == 0:
        print(f'Fixed node pass: {i}/{PANELS} panels, elapsed {time.monotonic()-started:.1f}s.', flush=True)

coefficients = []
coeff_i = []
quadrature_factor = rat(F(U, 3*PANELS))
for ix, x in enumerate(XS):
    rows, intervals = [], []
    for j in range(9):
        quad = mulpos(quadrature_factor, sums[ix][j])
        err = usum([simpson[ix][j], D(tail_rows[j]['theta_index_error']),
                    D(tail_rows[j]['spatial_error'])])
        enclosed = lo.subtract(quad[0], err), hi.add(quad[1], err)
        intervals.append(enclosed)
        rows.append(dict(j=j, quadrature=si(quad),
                         arithmetic_trigonometric_constants_width=str(hi.subtract(quad[1], quad[0])),
                         fourth_derivative_bound=str(max4[ix][j]), maximum_cell=max4_cells[ix][j],
                         simpson_error=str(simpson[ix][j]),
                         theta_index_error=tail_rows[j]['theta_index_error'],
                         spatial_error=tail_rows[j]['spatial_error'],
                         enclosure=si(enclosed)))
    coefficients.append(dict(x=str(x), coefficients=rows))
    coeff_i.append(intervals)

cells = []
uniform = [[None, None] for _ in XS]
signs = [[] for _ in XS]
minimum_margins = [None]*len(XS)
failures = []
for k in range(TIME_CELLS):
    l, r = F(k, 20*TIME_CELLS), F(k+1, 20*TIME_CELLS)
    delta = rat(l-F(1, 40))[0], rat(r-F(1, 40))[1]
    rows = []
    for ix, x in enumerate(XS):
        pol = coeff_i[ix][8]
        for j in range(7, -1, -1):
            pol = add(mul(pol, delta), coeff_i[ix][j])
        val = lo.subtract(pol[0], time_error), hi.add(pol[1], time_error)
        sg = 1 if val[0] > 0 else (-1 if val[1] < 0 else 0)
        margin = val[0] if sg == 1 else (val[1].copy_negate() if sg == -1 else D(0))
        if sg == 0:
            failures.append(f'cell{k}, x={x}: zero-containing enclosure')
        signs[ix].append(sg)
        minimum_margins[ix] = margin if minimum_margins[ix] is None else min(minimum_margins[ix], margin)
        uniform[ix][0] = val[0] if uniform[ix][0] is None else min(uniform[ix][0], val[0])
        uniform[ix][1] = val[1] if uniform[ix][1] is None else max(uniform[ix][1], val[1])
        rows.append(dict(x=str(x), polynomial_range=si(pol), full_enclosure=si(val),
                         sign=sg, signed_margin=str(margin)))
    for p in range(3):
        if signs[2*p][-1]*signs[2*p+1][-1] != -1:
            failures.append(f'cell{k}, pair{p}: opposite signs not certified')
    cells.append(dict(index=k, time_interval=[str(l), str(r)], delta=si(delta), endpoints=rows))
    counts['time_cells'] += 1

rr = runtime()
if rr['unexpected_signals']:
    failures.append('Unexpected Decimal signals: '+str(rr['unexpected_signals']))
assert counts['nodes'] == PANELS+1 and counts['spatial_cells'] == SPACE_CELLS
assert counts['time_cells'] == TIME_CELLS
certificate = dict(status='PASS' if not failures else 'INCONCLUSIVE',
                   target='Uniform strict opposite endpoint signs in three fixed boxes on [0,1/20]',
                   parameters=preflight['parameters'], preflight=PREFLIGHT.name,
                   preflight_sha256=hashlib.sha256(PREFLIGHT.read_bytes()).hexdigest(),
                   constants=preflight['constants'], tails=tail_rows,
                   complete_ninth=preflight['complete_ninth'],
                   trig_steps=[dict(x=str(x), cosine=si(c), sine=si(s), taylor_remainder=str(e),
                                    final_cosine=si(cosines[ix]), final_sine=si(sines[ix]))
                               for ix, (x, (c, s, e)) in enumerate(zip(XS, steps))],
                   coefficients=coefficients, time_cells=cells,
                   uniform_endpoints=[dict(x=str(x), enclosure=si(uniform[ix]),
                                           signs=sorted(set(signs[ix])), minimum_signed_margin=str(minimum_margins[ix]))
                                      for ix, x in enumerate(XS)],
                   coverage=dict(spatial_cells=SPACE_CELLS, time_cells=TIME_CELLS,
                                 shared_endpoints_included=True, nodes=counts['nodes']),
                   runtime=rr, failures=failures,
                   source='L019/L058; DLMF3.5(ii)(3.5.6)-(3.5.8); OpenStax Calculus2 Section6.3 Theorem6.7; Python Decimal contracts from review2166',
                   script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
OUT.write_text(json.dumps(certificate, indent=2)+'\n')
print('Result:', certificate['status'], flush=True)
for row in certificate['uniform_endpoints']:
    print('x='+row['x']+' F in ['+row['enclosure']['lower']+', '+row['enclosure']['upper']+']; minimum signed margin='+row['minimum_signed_margin']+'; required > 0', flush=True)
print('Failures:', len(failures), failures[:6], flush=True)
print('Full certificate:', OUT, flush=True)
if failures:
    raise SystemExit(1)
