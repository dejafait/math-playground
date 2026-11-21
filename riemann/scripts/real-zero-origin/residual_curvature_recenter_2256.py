#!/usr/bin/env python3
"""One fixed midpoint translation of saved2255 coefficient intervals."""
import decimal
from decimal import Decimal as D
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import platform
import sys
import time

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT/'residual_curvature_2255.json'
OLDPRE = ROOT/'residual_curvature_preflight_2255.json'
OUT = ROOT/'residual_curvature_recenter_2256.json'
PRE = ROOT/'residual_curvature_recenter_preflight_2256.json'
PREC = 80
START = time.monotonic()
dn, up = [decimal.Context(prec=PREC, rounding=r, Emin=-999999, Emax=999999)
          for r in (decimal.ROUND_FLOOR, decimal.ROUND_CEILING)]
for ctx in (dn, up):
    for signal in ctx.traps:
        ctx.traps[signal] = signal not in (decimal.Inexact, decimal.Rounded)
    ctx.clear_flags()


def saved(z):
    return D(z['lower']), D(z['upper'])


def pack(z):
    return dict(lower=str(z[0]), upper=str(z[1]))


def rat(q):
    q = F(q)
    lo = dn.divide(D(q.numerator), D(q.denominator))
    hi = up.divide(D(q.numerator), D(q.denominator))
    assert lo == hi  # all scalar shifts/radii here are short dyadics
    return lo


def add(a, b):
    return dn.add(a[0], b[0]), up.add(a[1], b[1])


def scale(a, h):
    if h >= 0:
        return dn.multiply(a[0], h), up.multiply(a[1], h)
    return dn.multiply(a[1], h), up.multiply(a[0], h)


def symmetric_mul(a, radius):
    # The exact product of interval a with [-radius,radius].
    b = up.multiply(max(a[0].copy_abs(), a[1].copy_abs()), radius)
    return b.copy_negate(), b


def translate(a, h):
    b = list(a)
    n = len(b)-1
    for i in range(n-1, -1, -1):
        for j in range(i, n):
            b[j] = add(b[j], scale(b[j+1], h))
    return b


def centered_horner(a, radius):
    tail = a[-1]
    for coeff in a[-2:0:-1]:
        tail = add(symmetric_mul(tail, radius), coeff)
    tail = symmetric_mul(tail, radius)
    return add(a[0], tail), tail


c = json.loads(SOURCE.read_text())
p = json.loads(OLDPRE.read_text())
assert c['status'] == 'INCONCLUSIVE'
assert c['preflight_sha256'] == hashlib.sha256(OLDPRE.read_bytes()).hexdigest()
assert c['script_sha256'] == hashlib.sha256((ROOT/'residual_curvature_2255.py').read_bytes()).hexdigest()
assert len(c['cells']) == c['total_cells'] == p['total_cells'] == 131072
assert len(c['parameter_jets']) == 4096
assert not c['runtime']['unexpected_signals']
for name, digest in p['input_hashes'].items():
    assert digest == hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
pre = dict(status='FIXED_SETUP_BEFORE_SIGN_PASS', precision=PREC, total_cells=131072,
           x_cells=256, u_subcells=32, threshold='0', variable_radius='1/1024',
           source=SOURCE.name, source_sha256=hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
           original_preflight=OLDPRE.name, original_preflight_sha256=hashlib.sha256(OLDPRE.read_bytes()).hexdigest(),
           representation='Outward interval triangular binomial translation to each closed-cell midpoint; symmetric Horner.',
           unchanged='All saved coefficient intervals, closed cells, polynomial degrees, and complete per-cell error bounds.',
           trust='Correct CPython integers/Fraction and libmpdec directed basic arithmetic; no new exp or trig.')
PRE.write_text(json.dumps(pre, indent=2)+'\n')
print('Saved fixed preflight:', PRE, 'cells=', pre['total_cells'], flush=True)
radius = rat(F(1, 1024))
cells, failures, hulls = [], [], []
minimum, maximum, worst = None, None, None
for ci in range(16):
    uc = F(p['centers'][ci]['center'])
    region = [None, None]
    for xi in range(256):
        jet = c['parameter_jets'][ci*256+xi]
        assert (jet['center'], jet['x_index']) == (ci, xi)
        wp = [saved(a) for a in jet['W']]
        assert len(wp) == 33 and all(a <= b for a, b in wp)
        for ui in range(32):
            idx = (ci*256+xi)*32+ui
            old = c['cells'][idx]
            assert (old['center'], old['x_index'], old['u_index']) == (ci, xi, ui)
            ul, ur = map(F, old['u'])
            assert (ul, ur) == (F(ci,16)+F(ui,512), F(ci,16)+F(ui+1,512))
            h = rat((ul+ur)/2-uc)
            coeff = translate(wp, h)
            polynomial, nonconstant = centered_horner(coeff, radius)
            error = D(old['error'])
            value = dn.subtract(polynomial[0], error), up.add(polynomial[1], error)
            row = dict(center=ci, x_index=xi, u_index=ui, u=old['u'], shift=str(h),
                       translated_constant=pack(coeff[0]), translated_nonconstant=pack(nonconstant),
                       polynomial=pack(polynomial), error=old['error'], W=pack(value),
                       polynomial_magnitudes=old['polynomial_magnitudes'], error_terms=old['error_terms'])
            cells.append(row)
            if minimum is None or value[0] < minimum:
                minimum, worst = value[0], dict(row, translated_coefficients=list(map(pack,coeff)))
            maximum = value[1] if maximum is None else max(maximum, value[1])
            region = [value[0] if region[0] is None else min(region[0], value[0]),
                      value[1] if region[1] is None else max(region[1], value[1])]
            if value[0] <= 0:
                failures.append(dict(center=ci, x_index=xi, u_index=ui, W=pack(value),
                                     conclusion='NONPOSITIVE_BOX' if value[1] <= 0 else 'INCONCLUSIVE'))
    hulls.append(pack(region))
    print('Region', ci, 'W lower=', region[0], 'failed cells so far=', len(failures), flush=True)
flags = {str(i): {s.__name__: bool(v) for s,v in ctx.flags.items()} for i,ctx in enumerate((dn,up))}
unexpected = [(i,k) for i,f in flags.items() for k,v in f.items() if v and k not in ('Inexact','Rounded')]
assert not unexpected
result = dict(status='PASS' if not failures else 'INCONCLUSIVE',
              preflight=PRE.name, preflight_sha256=hashlib.sha256(PRE.read_bytes()).hexdigest(),
              script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              total_cells=len(cells), uniform_W=pack((minimum,maximum)), region_hulls=hulls,
              cells=cells, failures=failures, worst_cell=worst,
              runtime=dict(python=sys.version,implementation=platform.python_implementation(),
                           libmpdec=decimal.__libmpdec_version__,flags=flags,
                           unexpected_signals=unexpected,elapsed_seconds=time.monotonic()-START),
              qualification='Conditional arithmetic specialization; coefficient translation not independently audited; no exterior/preservation/all-degree claim.')
OUT.write_text(json.dumps(result,indent=2)+'\n')
print('Result:',result['status'],'actual W lower=',minimum,'required >0;',
      'failures=',len(failures),'certificate=',OUT,flush=True)
