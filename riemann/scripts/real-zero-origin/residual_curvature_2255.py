#!/usr/bin/env python3
"""One fixed closed-box curvature test; reuses audited C919r inputs."""
import decimal
from decimal import Decimal as D
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import hashlib
import json
import platform
import sys
import time

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'residual_curvature_2255.json'
PREFLIGHT = ROOT / 'residual_curvature_preflight_2255.json'
PREC, XCELLS, UCELLS = 80, 256, 32
START = time.monotonic()
contexts = [decimal.Context(prec=PREC, rounding=r, Emin=-999999, Emax=999999)
            for r in (decimal.ROUND_FLOOR, decimal.ROUND_CEILING, decimal.ROUND_HALF_EVEN)]
for context in contexts:
    for signal in context.traps:
        context.traps[signal] = signal not in (decimal.Inexact, decimal.Rounded)
    context.clear_flags()
dn, up, near = contexts


def rat(q):
    q = F(q)
    return dn.divide(D(q.numerator), D(q.denominator)), up.divide(D(q.numerator), D(q.denominator))


def saved(q):
    return D(q['lower']), D(q['upper'])


def pack(q):
    return dict(lower=str(q[0]), upper=str(q[1]))


def add(a, b):
    return dn.add(a[0], b[0]), up.add(a[1], b[1])


def neg(a):
    return a[1].copy_negate(), a[0].copy_negate()


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    if a[0] >= 0 and b[0] >= 0:
        return dn.multiply(a[0], b[0]), up.multiply(a[1], b[1])
    return min(dn.multiply(x, y) for x in a for y in b), max(up.multiply(x, y) for x in a for y in b)


def inflate(a, e):
    return dn.subtract(a[0], e), up.add(a[1], e)


def horner(aa, t):
    z = aa[-1]
    for a in aa[-2::-1]:
        z = add(mul(z, t), a)
    return z


def bound(a):
    return max(a[0].copy_abs(), a[1].copy_abs())


def usum(values):
    z = D(0)
    for v in values:
        assert v >= 0
        z = up.add(z, v)
    return z


def umul(*values):
    z = D(1)
    for v in values:
        assert v >= 0
        z = up.multiply(z, v)
    return z


def expupper(q):
    return up.next_plus(near.exp(rat(q)[1]))


def convolution(a, b):
    z = [rat(0) for _ in range(len(a)+len(b)-1)]
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            z[i+j] = add(z[i+j], mul(ai, bj))
    return z


def flags():
    return {str(i): {s.__name__: bool(v) for s, v in c.flags.items()}
            for i, c in enumerate(contexts)}


paths = [ROOT / n for n in ('two_region_preflight_2251.json', 'two_region_2251.json',
                           'two_region_audit_2253.json', 'two_region_exact_cells_2253.json')]
p, c, audit, exact = [json.loads(path.read_text()) for path in paths]
assert audit['status'] == exact['status'] == c['status'] == 'PASS'
assert not audit['failures'] and not exact['failures'] and not c['failures']
assert c['preflight_sha256'] == hashlib.sha256(paths[0].read_bytes()).hexdigest()
assert c['script_sha256'] == hashlib.sha256((ROOT/'two_region_2251.py').read_bytes()).hexdigest()
assert len(p['centers']) == len(c['centers']) == 16
assert len(p['spatial_cells']) == 1280
assert len(p['index_prefactors']) == 18
assert not c['runtime']['unexpected_signals']
M17, XR = D(p['derivative17']['total']), D(p['remainders']['x'])
CENTERS = [F(0)] + [F(2*i+1, 32) for i in range(1, 16)]
setup = []
for ci, uc in enumerate(CENTERS):
    assert F(p['centers'][ci]['center']) == F(c['centers'][ci]['center']) == uc
    left, right = F(ci, 16), F(ci+1, 16)
    radius = F(1, 16) if ci == 0 else F(1, 32)
    ids = list(range(int(256*left), int(256*right)))
    for k in ids:
        row = p['spatial_cells'][k]
        assert F(row['left']) == F(k, 256) and F(row['right']) == F(k+1, 256)
        assert len(row['bounds']) == 18
    B16 = usum([max(D(p['spatial_cells'][k]['bounds'][16]) for k in ids),
                umul(D(p['index_prefactors'][16]), expupper(-112*left))])
    eI = umul(M17, rat(radius**17/factorial(17))[1])
    eG = umul(rat(F(29, 2))[1], eI)
    eK = umul(B16, rat(radius**16/factorial(16))[1])
    jets = p['centers'][ci]['jets']
    assert len(jets) == 16
    for fam in ('cosine', 'sine'):
        assert len(c['centers'][ci][fam]) == 9
        for j, a in enumerate(c['centers'][ci][fam]):
            err = p['centers'][ci]['errors'][j]
            assert a['j'] == j and F(a['error']) == F(err['total'])
            assert F(err['total']) >= sum((F(err[v]) for v in ('simpson', 'index', 'spatial')), F(0))
            assert F(a['enclosure']['lower']) <= F(a['quadrature']['lower'])-F(a['error'])
            assert F(a['enclosure']['upper']) >= F(a['quadrature']['upper'])+F(a['error'])
    setup.append(dict(center=str(uc), u=[str(left), str(right)], radius=str(radius),
                      B16=str(B16), error_I=str(eI), error_G=str(eG), error_K=str(eK)))
pre = dict(status='FIXED_SETUP_BEFORE_SIGN_PASS', precision=PREC,
           x_cells=XCELLS, u_subcells=UCELLS, total_cells=16*XCELLS*UCELLS,
           threshold='0', M17=str(M17), x_remainder=str(XR), centers=setup,
           input_hashes={q.name: hashlib.sha256(q.read_bytes()).hexdigest() for q in paths},
           source='C919r audited signed quadrature enclosures, complete bounds (5)-(14); C919m half-line identities',
           trust='Correct CPython integers/Fraction and libmpdec directed arithmetic, neighbors and HALF_EVEN exp.')
PREFLIGHT.write_text(json.dumps(pre, indent=2)+'\n')
print('Saved fixed preflight:', PREFLIGHT, 'cells=', pre['total_cells'], flush=True)

cells, jets_out, failures, hulls = [], [], [], []
for ci, uc in enumerate(CENTERS):
    cc = [saved(a['enclosure']) for a in c['centers'][ci]['cosine']]
    ss = [saved(a['enclosure']) for a in c['centers'][ci]['sine']]
    kj = [saved(a) for a in p['centers'][ci]['jets']]
    kp = [mul(kj[k], rat(F(1, factorial(k)))) for k in range(16)]
    eI, eG, eK = (D(setup[ci][k]) for k in ('error_I', 'error_G', 'error_K'))
    hull = [None, None]
    for xi in range(XCELLS):
        xl, xr = F(14)+F(xi, 512), F(14)+F(xi+1, 512)
        xx = rat(xl)[0], rat(xr)[1]
        dx = rat(xl-F(57, 4))[0], rat(xr-F(57, 4))[1]
        ic, sc = inflate(horner(cc, dx), XR), inflate(horner(ss, dx), XR)
        x2, x4 = mul(xx, xx), mul(mul(xx, xx), mul(xx, xx))
        ip = [ic, sub(mul(xx, sc), kj[0])]
        gp = [mul(xx, sc), neg(mul(x2, ic))]
        for k in range(15):
            fac = rat(F(1, (k+1)*(k+2)))
            ip.append(mul(fac, sub(neg(mul(kj[k+1], rat(F(1, factorial(k))))), mul(x2, ip[k]))))
            gp.append(mul(fac, mul(x2, sub(kp[k], gp[k]))))
        assert len(ip) == len(gp) == 17
        ii, gg, gk = convolution(ip, ip), convolution(gp, gp), convolution(gp, kp)
        gk.append(rat(0))
        wp = [add(mul(x4, a), mul(x2, sub(b, d))) for a, b, d in zip(ii, gg, gk)]
        jets_out.append(dict(center=ci, x_index=xi, x=[str(xl), str(xr)],
                             I=list(map(pack, ip)), G=list(map(pack, gp)), W=list(map(pack, wp))))
        for ui in range(UCELLS):
            ul, ur = F(ci, 16)+F(ui, 512), F(ci, 16)+F(ui+1, 512)
            dd = rat(ul-uc)[0], rat(ur-uc)[1]
            ir, gr, kr = (horner(a, dd) for a in (ip, gp, kp))
            bi, bg, bk = map(bound, (ir, gr, kr))
            ei2 = umul(x4[1], eI, usum([umul(D(2), bi), eI]))
            egk = umul(x2[1], usum([umul(eG, bk), umul(eK, bg), umul(eG, eK)]))
            eg2 = umul(x2[1], eG, usum([umul(D(2), bg), eG]))
            error = usum([ei2, egk, eg2])
            poly = horner(wp, dd)
            value = inflate(poly, error)
            hull = [value[0] if hull[0] is None else min(hull[0], value[0]),
                    value[1] if hull[1] is None else max(hull[1], value[1])]
            row = dict(center=ci, x_index=xi, u_index=ui, u=[str(ul), str(ur)],
                       polynomial=pack(poly), error=str(error), W=pack(value),
                       polynomial_magnitudes=list(map(str, (bi, bg, bk))),
                       error_terms=list(map(str, (ei2, egk, eg2))))
            cells.append(row)
            if value[0] <= 0:
                failures.append(dict(center=ci, x_index=xi, u_index=ui, W=pack(value),
                                     conclusion='NONPOSITIVE_BOX' if value[1] <= 0 else 'INCONCLUSIVE'))
    hulls.append(pack(hull))
    print('Region', ci, 'W hull=', list(map(str, hull)), 'failed cells so far=', len(failures), flush=True)
ff = flags()
unexpected = [(i, k) for i, f in ff.items() for k, v in f.items()
              if v and k not in ('Inexact', 'Rounded')]
assert not unexpected
assert len(cells) == 16*XCELLS*UCELLS and len(jets_out) == 16*XCELLS
minimum = min(D(a['W']['lower']) for a in cells)
maximum = max(D(a['W']['upper']) for a in cells)
result = dict(status='PASS' if not failures else 'INCONCLUSIVE',
              preflight=PREFLIGHT.name, preflight_sha256=hashlib.sha256(PREFLIGHT.read_bytes()).hexdigest(),
              script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              total_cells=len(cells), uniform_W=pack((minimum, maximum)), region_hulls=hulls,
              parameter_jets=jets_out, cells=cells, failures=failures,
              runtime=dict(python=sys.version, implementation=platform.python_implementation(),
                           libmpdec=decimal.__libmpdec_version__, flags=ff,
                           unexpected_signals=unexpected, elapsed_seconds=time.monotonic()-START),
              qualification='Conditional arithmetic specialization; no independent audit; no exterior/preservation/all-degree claim.')
OUT.write_text(json.dumps(result, indent=2)+'\n')
print('Result:', result['status'], 'actual W lower=', minimum, 'required >0;',
      'failures=', len(failures), 'certificate=', OUT, flush=True)
