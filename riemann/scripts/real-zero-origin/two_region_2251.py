#!/usr/bin/env python3
"""Fixed two-region signed cosine test2251; proof C919r."""
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

PREC, U, N, PANELS, SPACE_CELLS, PARAM_CELLS = 80, 4, 4, 2**14, 1280, 32
XC, RADIUS, DEGREE = F(57, 4), F(1, 4), 8
ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'two_region_2251.json'
PREFLIGHT = ROOT / 'two_region_preflight_2251.json'
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


def trig_step(t):
    """Taylor degree31 at one positive mesh angle, with full remainder."""
    assert 0 < t[0] <= t[1] < D('0.004')
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


def inflate(a, e):
    return lo.subtract(a[0], e), hi.add(a[1], e)


def horner(coeffs, x):
    out = coeffs[-1]
    for a in reversed(coeffs[:-1]):
        out = add(mul(out, x), a)
    return out


a5, a239 = atan_bounds(5, 80), atan_bounds(239, 25)
piq = 16*a5[0]-4*a239[1], 16*a5[1]-4*a239[0]
assert F(3) < piq[0] < piq[1] < F(22, 7) and piq[1]**2 < 10
pi = rat(piq[0])[0], rat(piq[1])[1]
rates = [mulpos(pi, pt(n*n)) for n in range(1, N+1)]
CENTERS = [F(0)] + [F(2*i+1, 32) for i in range(1, 16)]
U_DEGREE, SUBCELLS = 16, 32
REQUIRED_J, REQUIRED_I = D('0.01'), D('1e-12')
FAILURES = []
h = rat(F(U, PANELS))
assert h[0] == h[1] and 0 < mulpos(rat(XC), h)[1] < D('0.004')
polys = [[F(0), F(-12), F(8)]]
for m in range(17):
    p = polys[-1]
    q = [F(0)]*(len(p)+1)
    for k, a in enumerate(p):
        q[k] += (F(1, 2)+2*k)*a
        q[k+1] -= 2*a
    polys.append(q)
assert polys[2] == [0, -75, 330, -224, 32]
AA = [sum((abs(a)*(4*k)**k for k, a in enumerate(p)), F(0)) for p in polys]
index_pref = [mulpos(rat(2*a), expi(rat(F(-225, 4))))[1] for a in AA]
space_pref = [mulpos(rat(2*a), expi(pt(-512)))[1] for a in AA]


def index_tail(m, j=0):
    return umul(index_pref[m], rat(F(factorial(j), 112**(j+1)))[1])


def space_tail(m, j=0):
    factor = sum((F(comb(j, k)*4**(j-k)*factorial(k), 1024**(k+1))
                  for k in range(j+1)), F(0))
    return umul(space_pref[m], rat(factor)[1])


def kernel_derivative_bounds(left, right):
    """Whole closed cell; all m=0,...,17 of finite n<=4 sum."""
    el = expi(rat(2*left))[0]
    er = expi(rat(2*right))[1]
    out = [D(0)]*18
    for alpha in rates:
        vl, vr = lo.multiply(alpha[0], el), hi.multiply(alpha[1], er)
        fac = expi(pt(hi.subtract(rat(right/2)[1], vl)))[1]
        powers = [upow(vr, k) for k in range(20)]
        for m, p in enumerate(polys):
            value = usum(umul(rat(abs(a))[1], powers[k]) for k, a in enumerate(p))
            out[m] = hi.add(out[m], umul(fac, value))
    return out


def kernel_jets(s):
    """Signed jets at a single exact center, plus ALL omitted indices."""
    vals = [pt(0) for _ in range(16)]
    for alpha in rates:
        v = mulpos(alpha, expi(rat(2*s)))
        fac = expi(sub(rat(s/2), v))
        for m in range(16):
            val = mulpos(fac, horner([rat(a) for a in polys[m]], v))
            vals[m] = add(vals[m], val)
    taildecay = expi(rat(-112*s))[1]
    return [inflate(v, umul(index_pref[m], taildecay)) for m, v in enumerate(vals)]


# All analytic error bounds are saved before any signed quadrature.
spatial_rows, ebounds = [], []
moment9, moment17 = D(0), D(0)
for cell in range(SPACE_CELLS):
    left, right = F(cell, 256), F(cell+1, 256)
    eb = kernel_derivative_bounds(left, right)
    ebounds.append(eb)
    part9 = umul(rat(F(1, 256))[1], upow(rat(right)[1], 9), eb[0]) if cell < 1024 else D(0)
    part17 = umul(rat(F(1, 256))[1], eb[17]) if cell < 1024 else D(0)
    moment9, moment17 = hi.add(moment9, part9), hi.add(moment17, part17)
    spatial_rows.append(dict(index=cell, left=str(left), right=str(right),
                             bounds=list(map(str, eb)), moment9=str(part9),
                             moment17=str(part17)))
    counts['spatial_cells'] += 1
M9 = usum([moment9, index_tail(0, 9), space_tail(0, 9)])
M17 = usum([moment17, index_tail(17), space_tail(17)])
xrem = umul(M9, rat(F(1, 4)**9/factorial(9))[1])
jrem = umul(M17, rat(F(1, 16)**16/factorial(17))[1])
irem = umul(M17, rat(F(1, 32)**17/factorial(17))[1])
simpson_factor = rat(F(U**5, 180*PANELS**4))[1]
center_bounds = []
for uc in CENTERS:
    max4, maxcells = [D(0)]*9, [None]*9
    first = int(256*uc)
    assert F(first, 256) == uc
    for cell in range(first, first+1024):
        tupper = rat(F(cell+1, 256)-uc)[1]
        eb = ebounds[cell]
        for j in range(9):
            pp = [hi.divide(upow(tupper, j-s), D(factorial(j-s))) if s <= j else D(0)
                  for s in range(5)]
            db = [usum(umul(D(comb(k, s)), pp[s], eb[k-s]) for s in range(k+1))
                  for k in range(5)]
            b4 = usum(umul(D(comb(4, k)), db[k], rat(XC**(4-k))[1]) for k in range(5))
            if b4 > max4[j]:
                max4[j], maxcells[j] = b4, cell
    errors = []
    for j in range(9):
        ss = umul(simpson_factor, max4[j])
        ii = umul(index_tail(0, j), rat(F(1, factorial(j)))[1])
        tt = umul(space_tail(0, j), rat(F(1, factorial(j)))[1])
        errors.append(dict(j=j, fourth=str(max4[j]), maximizer=maxcells[j],
                           simpson=str(ss), index=str(ii), spatial=str(tt),
                           total=str(usum([ss, ii, tt]))))
    center_bounds.append(dict(center=str(uc), errors=errors,
                               jets=list(map(si, kernel_jets(uc)))))
preflight = dict(status='FIXED_SETTINGS_BEFORE_SIGN_PASS',
    parameters=dict(U=U, N=N, panels=PANELS, precision=PREC, x_center=str(XC),
                    x_degree=8, x_cells=32, u_degree=16, u_subcells=32,
                    centers=list(map(str, CENTERS)), spatial_cells=SPACE_CELLS,
                    required_J=str(REQUIRED_J), required_I=str(REQUIRED_I)),
    constants=dict(pi=si(pi), exact_pi_bounds=list(map(str, piq))),
    derivative_polynomials=[list(map(str, p)) for p in polys],
    derivative_A=list(map(str, AA)), index_prefactors=list(map(str, index_pref)),
    spatial_prefactors=list(map(str, space_pref)), spatial_cells=spatial_rows,
    moment9=dict(compact=str(moment9), index=str(index_tail(0, 9)),
                 spatial=str(space_tail(0, 9)), total=str(M9)),
    derivative17=dict(compact=str(moment17), index=str(index_tail(17)),
                      spatial=str(space_tail(17)), total=str(M17)),
    remainders=dict(x=str(xrem), J=str(jrem), I=str(irem)),
    centers=center_bounds, runtime=runtime(), failures=[])
PREFLIGHT.write_text(json.dumps(preflight, indent=2)+'\n')
print('Preflight saved:', PREFLIGHT, 'M9=', M9, 'M17=', M17,
      'remainders x/J/I=', xrem, jrem, irem, flush=True)

cstep, sstep, tr = trig_step(mulpos(rat(XC), h))
trigs, c, s = [], pt(1), pt(0)
for i in range(PANELS+1):
    trigs.append((c, s))
    if i < PANELS:
        c, s = sub(mulpos(cstep, c), mulpos(sstep, s)), add(mulpos(cstep, s), mulpos(sstep, c))
        counts['trig_rotations'] += 1
center_results = []
for ci, uc in enumerate(CENTERS):
    csums, ssums = [pt(0) for _ in range(9)], [pt(0) for _ in range(9)]
    for i in range(PANELS+1):
        tq = F(i*U, PANELS)
        sq = uc+tq
        t, su = rat(tq), rat(sq)
        assert t[0] == t[1] and F(t[0]) == tq
        assert su[0] == su[1] and F(su[0]) == sq
        kernel = pt(0)
        e2s = expi(rat(2*sq))
        for alpha in rates:
            v = mulpos(alpha, e2s)
            poly = mulpos(mulpos(pt(4), v), sub(mulpos(pt(2), v), pt(3)))
            assert poly[0] > 0
            kernel = add(kernel, mulpos(poly, expi(sub(rat(sq/2), v))))
        moment = mulpos(pt(1 if i in (0, PANELS) else (4 if i % 2 else 2)), kernel)
        c, s = trigs[i]
        cp, sp = [c, neg(s), neg(c), s], [s, c, neg(s), neg(c)]
        for j in range(9):
            csums[j] = add(csums[j], mulpos(moment, cp[j % 4]))
            ssums[j] = add(ssums[j], mulpos(moment, sp[j % 4]))
            if j < 8:
                moment = divpos(mulpos(moment, t), pt(j+1))
        counts['nodes'] += 1
    families = []
    for sums in (csums, ssums):
        records = []
        for j in range(9):
            quad = mulpos(rat(F(U, 3*PANELS)), sums[j])
            err = D(center_bounds[ci]['errors'][j]['total'])
            records.append(dict(j=j, quadrature=si(quad), error=str(err),
                                enclosure=si(inflate(quad, err))))
        families.append(records)
    center_results.append(dict(center=str(uc), cosine=families[0], sine=families[1]))
    print('Integrated center', str(uc), flush=True)

cells, parameter_jets = [], []
uniform = {'J': [None, None], 'I': [None, None]}
for ci, uc in enumerate(CENTERS):
    cc = [(D(a['enclosure']['lower']), D(a['enclosure']['upper'])) for a in center_results[ci]['cosine']]
    sc = [(D(a['enclosure']['lower']), D(a['enclosure']['upper'])) for a in center_results[ci]['sine']]
    kj = [(D(a['lower']), D(a['upper'])) for a in center_bounds[ci]['jets']]
    for xi in range(PARAM_CELLS):
        xl, xr = F(14)+F(xi, 64), F(14)+F(xi+1, 64)
        xx, dx = (rat(xl)[0], rat(xr)[1]), (rat(xl-XC)[0], rat(xr-XC)[1])
        ic, scell = inflate(horner(cc, dx), xrem), inflate(horner(sc, dx), xrem)
        aa = [ic, sub(mulpos(xx, scell), kj[0])]
        x2 = power(xx, 2)
        for k in range(15):
            rhs = sub(neg(mulpos(rat(F(1, factorial(k))), kj[k+1])), mulpos(x2, aa[k]))
            aa.append(mulpos(rat(F(1, (k+1)*(k+2))), rhs))
        parameter_jets.append(dict(center_index=ci, x_index=xi, x=[str(xl), str(xr)],
                                    I_center=si(ic), S_center=si(scell), coefficients=list(map(si, aa))))
        for ui in range(SUBCELLS):
            if ci == 0:
                name, threshold, rem = 'J', REQUIRED_J, jrem
                ul, ur = F(ui, 512), F(ui+1, 512)
                delta = rat(ul)[0], rat(ur)[1]
                value = inflate(horner(aa[1:], delta), rem)
            else:
                name, threshold, rem = 'I', REQUIRED_I, irem
                ul, ur = F(ci, 16)+F(ui, 512), F(ci, 16)+F(ui+1, 512)
                delta = rat(ul-uc)[0], rat(ur-uc)[1]
                value = inflate(horner(aa, delta), rem)
            if value[0] <= threshold:
                FAILURES.append(dict(observable=name, center=ci, x_cell=xi, u_cell=ui,
                                     reason='Positive required margin not certified', enclosure=si(value)))
            for side in (0, 1):
                old = uniform[name][side]
                uniform[name][side] = value[side] if old is None else (min if side == 0 else max)(old, value[side])
            cells.append(dict(observable=name, center_index=ci, x_index=xi, u_index=ui,
                              u=[str(ul), str(ur)], delta=si(delta), enclosure=si(value)))
            counts['parameter_cells'] += 1
rr = runtime()
if rr['unexpected_signals']:
    FAILURES.append(dict(reason='Unexpected Decimal signals', signals=rr['unexpected_signals']))
assert counts['nodes'] == len(CENTERS)*(PANELS+1)
assert counts['parameter_cells'] == len(CENTERS)*PARAM_CELLS*SUBCELLS
certificate = dict(status='PASS' if not FAILURES else 'INCONCLUSIVE',
    parameters=preflight['parameters'], preflight=PREFLIGHT.name,
    preflight_sha256=hashlib.sha256(PREFLIGHT.read_bytes()).hexdigest(),
    script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    trigonometric=dict(step_cosine=si(cstep), step_sine=si(sstep), remainder=str(tr),
                       final_cosine=si(c), final_sine=si(s)),
    centers=center_results, parameter_jets=parameter_jets, cells=cells,
    uniform={k: si(v) for k, v in uniform.items()}, runtime=rr, failures=FAILURES,
    qualification='Source-covered specialization; CPython/Fraction/libmpdec contracts retained. No independent backend or conceptual audit.')
OUT.write_text(json.dumps(certificate, indent=2)+'\n')
print('Result:', certificate['status'], 'actual/required J:', uniform['J'], REQUIRED_J,
      'actual/required I:', uniform['I'], REQUIRED_I, flush=True)
print('Failures:', len(FAILURES), 'full certificate:', OUT, flush=True)


