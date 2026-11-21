#!/usr/bin/env python3
"""Fixed joint two-real-zero compact certificate2236; proof C919o."""
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
OUT = ROOT / 'joint_kernel_2236.json'
PREFLIGHT = ROOT / 'joint_kernel_preflight_2236.json'
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
    assert 0 < t[0] <= t[1] < D('0.002')
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


# Every setting fixed in work2236 before the first numerical pass.
CENTERS = [F(57, 4), F(43, 2)]
RADII = [F(1, 4), F(1, 2)]
UCELLS, XCELLS, YCELLS = 256, 16, 32
REQUIRED = D('1e-10')
FAILURES = []
counts.update(joint_cells=0)


def inflate(a, e):
    return lo.subtract(a[0], e), hi.add(a[1], e)


def divide(a, b):
    assert b[0] > 0
    return mul(a, (lo.divide(D(1), b[1]), hi.divide(D(1), b[0])))


def sintcos(a, b, phase):
    return [a, b, neg(a), neg(b)][phase % 4]


def horner(coeff, delta):
    v = coeff[-1]
    for a in reversed(coeff[:-1]):
        v = add(mul(v, delta), a)
    return v


# All closed spatial derivative cells: unshifted moment quadratures.
space = []
for k in range(SPACE_CELLS):
    l, r = rat(F(k, 256))[0], rat(F(k+1, 256))[1]
    eb = exponent_derivative_bounds(l, r, D(0))
    bounds = []
    for cc in CENTERS:
        row = []
        for j in range(9):
            pp = [hi.divide(upow(r, j-s), D(factorial(j-s))) if s <= j else D(0)
                  for s in range(5)]
            db = [usum(umul(D(comb(t, s)), pp[s], eb[t-s])
                       for s in range(t+1)) for t in range(5)]
            row.append(usum(umul(D(comb(4, t)), db[t], upow(rat(cc)[1], 4-t))
                            for t in range(5)))
        bounds.append(row)
    space.append(dict(index=k, left=str(l), right=str(r), E=list(map(str, eb)),
                      fourth=[list(map(str, b)) for b in bounds],
                      mass_part=str(umul(cell_width[1], eb[0])),
                      ninth_part=str(umul(cell_width[1], upow(r, 9), eb[0]))))
    counts['spatial_cells'] += 1

# Suffix majorants, including both infinite omitted regions.
suffix = {}
maxima = [[D(0)]*9 for _ in CENTERS]
mass, ninth = usum([index_bound(0), spatial]), usum([index_bound(9), spatial])
for k in range(SPACE_CELLS-1, -1, -1):
    row = space[k]
    mass, ninth = hi.add(mass, D(row['mass_part'])), hi.add(ninth, D(row['ninth_part']))
    maxima = [[max(maxima[q][j], D(row['fourth'][q][j])) for j in range(9)]
              for q in range(2)]
    if k < UCELLS:
        suffix[k] = dict(mass=str(mass), ninth=str(ninth),
                         maxima=[list(map(str, b)) for b in maxima])

settings = dict(U=4, indices=4, panels=PANELS, derivative_cells=SPACE_CELLS,
                u_cells=UCELLS, x_cells=XCELLS, y_cells=YCELLS,
                centers=list(map(str, CENTERS)), radii=list(map(str, RADII)),
                frequency_degree=8, spatial_degree=3, precision=PREC,
                required_margin=str(REQUIRED))
preflight = dict(status='FROZEN_BEFORE_QUADRATURE', parameters=settings,
    constants=dict(pi=si(pi), exact_pi_bounds=list(map(str, piq)),
                   index_factor=str(index_factor[1]), space_tail=str(spatial)),
    space=space, suffix=suffix, runtime=runtime(), failures=[])
PREFLIGHT.write_text(json.dumps(preflight, separators=(',', ':'))+'\n')
print('Preflight saved:', PREFLIGHT, 'cells=', len(space), flush=True)

steps = [trig_step(mulpos(rat(c), h)) for c in CENTERS]
trig = [(pt(1), pt(0)) for _ in CENTERS]
sums = [[[pt(0) for j in range(9)] for phase in range(2)] for q in range(2)]
saved = {}
simpson_scale = rat(F(U, 3*PANELS))
for i in range(PANELS+1):
    t = pt(near.multiply(D(i), h[0]))
    assert F(t[0]) == F(i*U, PANELS)
    e2t, kval = expi(mulpos(pt(2), t)), pt(0)
    for alpha in rates:
        v = mulpos(alpha, e2t)
        poly = mulpos(mulpos(pt(4), v), sub(mulpos(pt(2), v), pt(3)))
        assert poly[0] > 0
        kval = add(kval, mulpos(poly, expi(sub(mulpos(pt('0.5'), t), v))))
    moments, moment = [], kval
    for j in range(9):
        moments.append(moment)
        if j < 8:
            moment = divpos(mulpos(moment, t), pt(j+1))
    w = pt(1 if i in (0, PANELS) else 4 if i % 2 else 2)
    node = []
    for q, (c, s) in enumerate(trig):
        pair = []
        for phase in range(2):
            vals = [mulpos(moments[j], sintcos(s, c, j+phase)) for j in range(9)]
            sums[q][phase] = [add(old, mulpos(w, val))
                              for old, val in zip(sums[q][phase], vals)]
            pair.append(vals)
        node.append(pair)
    if i % 64 == 0 and i < 16384:
        k = i//64
        assert k < UCELLS and F(t[0]) == F(k, UCELLS)
        prefix = [[[pt(0) if i == 0 else mulpos(simpson_scale, sub(sums[q][p][j], node[q][p][j]))
                    for j in range(9)] for p in range(2)] for q in range(2)]
        saved[k] = dict(prefix=prefix, trig=trig.copy(), kernel=kval)
    counts['nodes'] += 1
    if i < PANELS:
        trig = [(sub(mulpos(steps[q][0], c), mulpos(steps[q][1], s)),
                 add(mulpos(steps[q][0], s), mulpos(steps[q][1], c)))
                for q, (c, s) in enumerate(trig)]
        counts['trig_rotations'] += 2
    if i and i % 16384 == 0:
        print('Quadrature nodes completed:', i+1, '/', PANELS+1, flush=True)

total = [[[mulpos(simpson_scale, a) for a in pair] for pair in qq] for qq in sums]

# Scalar/interval evidence is serialized recursively, never printed wholesale.
def serial(v):
    if isinstance(v, D):
        return str(v)
    if isinstance(v, (list, tuple)):
        return [serial(x) for x in v]
    if isinstance(v, dict):
        return {str(k): serial(x) for k, x in v.items()}
    return v

node_record = dict(total=total, saved=saved,
                   trig_steps=steps, final_trig=trig, runtime=runtime())
NODE = ROOT / 'joint_kernel_nodes_2236.json'
NODE.write_text(json.dumps(serial(node_record), separators=(',', ':'))+'\n')
print('Complete node evidence saved:', NODE, flush=True)

parameter_rows, urows = [], []
global_lo, global_hi, minwhere = None, None, None
uv = rat(F(1, UCELLS))
vrange = (D(0), uv[1])
universal_den = rat(F(923, 4))[0]
xymax = rat(F(29, 2)**2*22**2)[1]
ratio = hi.divide(rat(F(29, 2)**3+22**3)[1], universal_den)
for k in range(UCELLS):
    u = F(k, UCELLS)
    sr = suffix[k]
    raw, shifted, enlarged, qerrs, rems, families = [], [], [], [], [], []
    for q in range(2):
        sf = rat((F(4)-u)*F(U, PANELS)**4/F(180))[1]
        errs = [usum([umul(sf, D(sr['maxima'][q][j])),
                       hi.divide(usum([index_bound(j), spatial]), D(factorial(j)))])
                for j in range(9)]
        integrals = [[inflate(sub(total[q][p][j], saved[k]['prefix'][q][p][j]), errs[j])
                      for j in range(9)] for p in range(2)]
        raw.append(integrals)
        qerrs.append(errs)
        c, s = saved[k]['trig'][q]
        coeffs = []
        for phase in range(2):
            arr = []
            for j in range(9):
                val = pt(0)
                for ell in range(j+1):
                    # Phase j+phase, stored phase ell; then rotate by -c*u.
                    sn = sintcos(integrals[0][ell], integrals[1][ell], j-ell+phase)
                    cs = sintcos(integrals[0][ell], integrals[1][ell], j-ell+phase+1)
                    rot = sub(mul(sn, c), mul(cs, s))
                    weight = rat((-u)**(j-ell)/factorial(j-ell))
                    val = add(val, mul(weight, rot))
                arr.append(val)
            coeffs.append(arr)
        shifted.append(coeffs)
        rem = hi.divide(umul(upow(rat(RADII[q])[1], 9), D(sr['ninth'])), D(factorial(9)))
        rems.append(rem)
        ncell = XCELLS if q == 0 else YCELLS
        base, length = (F(14), F(1, 2)) if q == 0 else (F(21), F(1))
        fam = []
        for j in range(ncell):
            aa, bb = base+length*j/ncell, base+length*(j+1)/ncell
            freq = rat(aa)[0], rat(bb)[1]
            dd = rat(aa-CENTERS[q])[0], rat(bb-CENTERS[q])[1]
            sint = inflate(horner(coeffs[0], dd), rem)
            cost = inflate(horner(coeffs[1], dd), rem)
            g = mulpos(freq, sint)
            gp = neg(mulpos(power(freq, 2), cost))
            fam.append(dict(frequency=freq, G=g, Gprime=gp))
        families.append(fam)
    # K(u) index-tail bound (pointwise, distinct from the integrated tail).
    kupper = hi.add(saved[k]['kernel'][1], index_factor[1])
    fourth = umul(xymax, usum([kupper, umul(ratio, D(sr['mass']))]))
    urem = hi.divide(umul(fourth, upow(uv[1], 4)), D(24))
    rowstart, localmin = len(parameter_rows), None
    for i, xx in enumerate(families[0]):
        for j, yy in enumerate(families[1]):
            xs, ys = power(xx['frequency'], 2), power(yy['frequency'], 2)
            den = sub(ys, xs)
            a0 = divide(sub(mulpos(ys, xx['G']), mulpos(xs, yy['G'])), den)
            a1 = divide(sub(mulpos(ys, xx['Gprime']), mulpos(xs, yy['Gprime'])), den)
            factor = divide(mulpos(xs, ys), den)
            a2 = mulpos(rat(F(1, 2)), mulpos(factor, sub(yy['G'], xx['G'])))
            a3 = mulpos(rat(F(1, 6)), mulpos(factor, sub(yy['Gprime'], xx['Gprime'])))
            poly = horner([a0, a1, a2, a3], vrange)
            value = inflate(poly, urem)
            parameter_rows.append([k, i, j, str(value[0]), str(value[1])])
            counts['joint_cells'] += 1
            if global_lo is None or value[0] < global_lo:
                global_lo, minwhere = value[0], [k, i, j]
            global_hi = value[1] if global_hi is None else max(global_hi, value[1])
            localmin = value[0] if localmin is None else min(localmin, value[0])
            if value[0] <= REQUIRED:
                FAILURES.append(dict(reason='Fixed enclosure misses the preregistered positive margin; no negative value certified',
                    cell=[k, i, j], enclosure=si(value), required=str(REQUIRED)))
                break
        if FAILURES:
            break
    urows.append(dict(index=k, u=str(u), quadrature_errors=qerrs, unshifted_integrals=raw,
        shifted_coefficients=shifted, frequency_remainders=rems, families=families,
        K_upper=kupper, mass_upper=D(sr['mass']), fourth_upper=fourth, u_remainder=urem,
        joint_rows=[rowstart, len(parameter_rows)], local_minimum=localmin))
    if FAILURES:
        break
    if (k+1) % 64 == 0:
        print('Closed u cells completed:', k+1, '/', UCELLS, 'minimum so far:', global_lo, flush=True)

rr = runtime()
if rr['unexpected_signals']:
    FAILURES.append(dict(reason='Unexpected Decimal signal', signals=rr['unexpected_signals']))
cert = dict(status='PASS' if not FAILURES else 'INCONCLUSIVE', parameters=settings,
    uniform_margin=si((global_lo, global_hi)), minimum_cell=minwhere,
    complete_box=(len(parameter_rows) == UCELLS*XCELLS*YCELLS),
    preflight=PREFLIGHT.name, preflight_sha256=hashlib.sha256(PREFLIGHT.read_bytes()).hexdigest(),
    nodes=NODE.name, nodes_sha256=hashlib.sha256(NODE.read_bytes()).hexdigest(),
    u_records=urows, joint_cells=parameter_rows, runtime=rr, failures=FAILURES,
    script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    arithmetic_contract='CPython/Fraction exact arithmetic; libmpdec directed basic operations, neighbors and correctly rounded HALF_EVEN exp. Runtime checks do not verify backend correctness.',
    provenance='Arithmetic and Bell/trig routines copied from origin_margin_2231.py; trig-step permitted bound widened from .001 to .002 before first run, same proved degree31 Taylor remainder.')
OUT.write_text(json.dumps(serial(cert), separators=(',', ':'))+'\n')
print('Result:', cert['status'], 'actual lower:', global_lo, 'required >', REQUIRED,
      'covered cells:', len(parameter_rows), '/', UCELLS*XCELLS*YCELLS, flush=True)
print('Failures:', len(FAILURES), 'certificate:', OUT, flush=True)
