#!/usr/bin/env python3
"""Frozen complete signed origin-margin test2231; proof C919n."""
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

PREC, U, N, PANELS, SPACE_CELLS, PARAM_CELLS = 80, 4, 4, 2**16, 1024, 32
XC, RADIUS, DEGREE = F(57, 4), F(1, 4), 8
ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'origin_margin_2231.json'
PREFLIGHT = ROOT / 'origin_margin_preflight_2231.json'
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
counts = dict(nodes=0, spatial_cells=0, parameter_cells=0,
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
radius = rat(RADIUS)[1]
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


# A_j = (1/j!) integral t^j K(t) sin(XC*t+j*pi/2)dt.
# Taylor remainder is bounded by the complete ninth moment.
max4, maxcells = [D(0)]*9, [None]*9
compact9, spatial_rows = D(0), []
for k in range(SPACE_CELLS):
    l, r = rat(F(U*k, SPACE_CELLS))[0], rat(F(U*(k+1), SPACE_CELLS))[1]
    eb = exponent_derivative_bounds(l, r, D(0))
    part9 = umul(cell_width[1], upow(r, 9), eb[0])
    compact9 = hi.add(compact9, part9)
    for j in range(9):
        pp = [hi.divide(umul(D(factorial(j)//factorial(j-s)), upow(r, j-s)),
                        D(factorial(j))) if s <= j else D(0) for s in range(5)]
        db = [usum(umul(D(comb(t, s)), pp[s], eb[t-s])
                   for s in range(t+1)) for t in range(5)]
        b4 = usum(umul(D(comb(4, t)), db[t], upow(rat(XC)[1], 4-t))
                   for t in range(5))
        if b4 > max4[j]:
            max4[j], maxcells[j] = b4, k
    spatial_rows.append(dict(index=k, interval=si((l, r)),
                             kernel_derivative_bounds=list(map(str, eb)),
                             ninth_moment_part=str(part9)))
    counts['spatial_cells'] += 1

complete9 = usum([compact9, index_bound(9), spatial])
remainder = hi.divide(umul(complete9, upow(radius, 9)), D(factorial(9)))
simpson_factor = rat(F(U**5, 180*PANELS**4))[1]
errors = [dict(j=j, fourth_derivative=str(max4[j]), maximum_cell=maxcells[j],
               simpson=str(umul(simpson_factor, max4[j])),
               index=str(hi.divide(index_bound(j), D(factorial(j)))),
               spatial=str(hi.divide(spatial, D(factorial(j))))) for j in range(9)]
k0_tail = index_factor[1]
preflight = dict(status='FIXED_SETTINGS_BEFORE_NODE_PASS',
    parameters=dict(U=U, N=N, panels=PANELS, spatial_cells=SPACE_CELLS,
                    parameter_cells=PARAM_CELLS, degree=DEGREE, digits=PREC,
                    center=str(XC), radius=str(RADIUS), bracket=['14', '29/2']),
    constants=dict(pi=si(pi), exact_pi_bounds=list(map(str, piq)),
                   atan_terms=dict(q5=80, q239=25)),
    errors=errors, spatial_cells=spatial_rows,
    complete_ninth=dict(compact=str(compact9), index=str(index_bound(9)),
                       spatial=str(spatial), bound=str(complete9), remainder=str(remainder)),
    k0_index_tail=str(k0_tail), runtime=runtime(), failures=[])
PREFLIGHT.write_text(json.dumps(preflight, indent=2)+'\n')
print('Preflight:', PREFLIGHT, 'complete Taylor error <=', remainder, flush=True)

cstep, sstep, tr = trig_step(mulpos(rat(XC), h))
c, s, sums = pt(1), pt(0), [pt(0) for _ in range(9)]
k0_finite = None
for i in range(PANELS+1):
    u = pt(near.multiply(D(i), h[0]))
    assert F(u[0]) == F(i*U, PANELS)
    exp2u = expi(mulpos(pt(2), u))
    kernel = pt(0)
    for rate in rates:
        v = mulpos(rate, exp2u)
        poly = mulpos(mulpos(pt(4), v), sub(mulpos(pt(2), v), pt(3)))
        assert poly[0] > 0
        kernel = add(kernel, mulpos(poly, expi(sub(mulpos(pt('0.5'), u), v))))
    if i == 0:
        k0_finite = kernel
    moment = mulpos(pt(1 if i in (0, PANELS) else (4 if i % 2 else 2)), kernel)
    phases = [s, c, neg(s), neg(c)]
    for j in range(9):
        sums[j] = add(sums[j], mulpos(moment, phases[j % 4]))
        if j < 8:
            moment = divpos(mulpos(moment, u), pt(j+1))
    counts['nodes'] += 1
    if i < PANELS:
        c, s = sub(mulpos(cstep, c), mulpos(sstep, s)), add(mulpos(cstep, s), mulpos(sstep, c))
        counts['trig_rotations'] += 1

coefficients, ai = [], []
for j in range(9):
    quad = mulpos(rat(F(U, 3*PANELS)), sums[j])
    err = usum(D(errors[j][key]) for key in ('simpson', 'index', 'spatial'))
    enclosure = lo.subtract(quad[0], err), hi.add(quad[1], err)
    ai.append(enclosure)
    coefficients.append(dict(j=j, quadrature=si(quad), errors=errors[j],
                             total_error=str(err), enclosure=si(enclosure)))
k0 = k0_finite[0], hi.add(k0_finite[1], k0_tail)
cells, failures, uniform = [], [], [None, None]
for k in range(PARAM_CELLS):
    left, right = F(14)+F(k, 2*PARAM_CELLS), F(14)+F(k+1, 2*PARAM_CELLS)
    xx = rat(left)[0], rat(right)[1]
    delta = rat(left-XC)[0], rat(right-XC)[1]
    polynomial = ai[8]
    for j in range(7, -1, -1):
        polynomial = add(mul(polynomial, delta), ai[j])
    sine_integral = lo.subtract(polynomial[0], remainder), hi.add(polynomial[1], remainder)
    margin = sub(mulpos(xx, sine_integral), k0)
    if margin[0] <= 0:
        failures.append(dict(cell=k, reason='Uniform positive margin not certified', enclosure=si(margin)))
    uniform[0] = margin[0] if uniform[0] is None else min(uniform[0], margin[0])
    uniform[1] = margin[1] if uniform[1] is None else max(uniform[1], margin[1])
    cells.append(dict(index=k, x=[str(left), str(right)], delta=si(delta),
                      polynomial=si(polynomial), complete_sine_integral=si(sine_integral), margin=si(margin)))
    counts['parameter_cells'] += 1
rr = runtime()
if rr['unexpected_signals']:
    failures.append(dict(reason='Unexpected Decimal signals', signals=rr['unexpected_signals']))
assert counts['nodes'] == PANELS+1 and counts['spatial_cells'] == SPACE_CELLS
assert counts['parameter_cells'] == PARAM_CELLS and counts['trig_rotations'] == PANELS
certificate = dict(status='PASS' if not failures else 'INCONCLUSIVE',
    target='Uniform positive G_x(0)-K(0) for all x in [14,29/2]',
    parameters=preflight['parameters'], constants=preflight['constants'],
    preflight=PREFLIGHT.name, preflight_sha256=hashlib.sha256(PREFLIGHT.read_bytes()).hexdigest(),
    complete_ninth=preflight['complete_ninth'],
    trig=dict(step_cosine=si(cstep), step_sine=si(sstep), remainder=str(tr),
              final_cosine=si(c), final_sine=si(s)),
    coefficients=coefficients,
    k0=dict(finite=si(k0_finite), index_tail=str(k0_tail), enclosure=si(k0)),
    parameter_cells=cells, uniform_margin=si(uniform), required_threshold='0',
    rational_claim='1/10' if uniform[0] > D('0.1') else None,
    runtime=rr, failures=failures,
    arithmetic_provenance='Arithmetic, Machin bounds, exp enclosure, Bell bounds and mesh trig routine copied from accepted C919f evaluator2167; no original artifact modified.',
    script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
OUT.write_text(json.dumps(certificate, indent=2)+'\n')
print('Result:', certificate['status'], 'actual uniform margin:', uniform, 'required > 0', flush=True)
print('Failures:', len(failures), 'certificate:', OUT, flush=True)

