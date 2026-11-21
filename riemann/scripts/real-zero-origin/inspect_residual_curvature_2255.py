#!/usr/bin/env python3
"""Consume every2255 cell/error record; no new sign pass or retuning."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent
OUT = ROOT/'residual_curvature_inspection_2255.json'
path = ROOT/'residual_curvature_2255.json'
c = json.loads(path.read_text())
p = json.loads((ROOT/c['preflight']).read_text())
checks, failures = 0, []


def check(ok, name):
    global checks
    checks += 1
    if not ok:
        failures.append(name)


def iv(z):
    return F(z['lower']), F(z['upper'])


check(c['preflight_sha256'] == hashlib.sha256((ROOT/c['preflight']).read_bytes()).hexdigest(), 'preflight hash')
check(c['script_sha256'] == hashlib.sha256((ROOT/'residual_curvature_2255.py').read_bytes()).hexdigest(), 'script hash')
for name, digest in p['input_hashes'].items():
    check(digest == hashlib.sha256((ROOT/name).read_bytes()).hexdigest(), 'input hash '+name)
check(len(c['cells']) == c['total_cells'] == p['total_cells'] == 131072, 'all cells')
check(len(c['parameter_jets']) == 4096, 'all parameter jets')
for k, z in enumerate(c['parameter_jets']):
    ci, xi = divmod(k, 256)
    check((z['center'], z['x_index']) == (ci, xi), 'jet indices '+str(k))
    check(list(map(F, z['x'])) == [F(14)+F(xi, 512), F(14)+F(xi+1, 512)], 'x coverage '+str(k))
    for family, count in [('G', 17), ('I', 17), ('W', 33)]:
        check(len(z[family]) == count and all(iv(a)[0] <= iv(a)[1] for a in z[family]), 'jet intervals '+str(k)+family)
observed, summary = [], []
uniform = [None, None]
for ci in range(16):
    rows = c['cells'][ci*8192:(ci+1)*8192]
    positive, crossing, nonpositive = 0, 0, 0
    failed_us, max_error = set(), F(0)
    region = [None, None]
    for k, z in enumerate(rows):
        xi, ui = divmod(k, 32)
        check((z['center'], z['x_index'], z['u_index']) == (ci, xi, ui), 'cell indices '+str(ci*8192+k))
        ul, ur = F(ci, 16)+F(ui, 512), F(ci, 16)+F(ui+1, 512)
        check(list(map(F, z['u'])) == [ul, ur], 'u coverage '+str(ci*8192+k))
        pl, pu = iv(z['polynomial'])
        wl, wu = iv(z['W'])
        e = F(z['error'])
        check(pl <= pu and wl <= wu and e >= 0, 'interval order '+str(ci*8192+k))
        check(wl <= pl-e and wu >= pu+e, 'full error inflation '+str(ci*8192+k))
        terms = list(map(F, z['error_terms']))
        check(len(terms) == 3 and min(terms) >= 0 and e >= sum(terms), 'all nonlinear errors '+str(ci*8192+k))
        bi, bg, bk = map(F, z['polynomial_magnitudes'])
        ei, eg, ek = (F(p['centers'][ci][v]) for v in ('error_I', 'error_G', 'error_K'))
        xr = F(14)+F(xi+1, 512)
        exact_terms = [xr**4*ei*(2*bi+ei), xr**2*(eg*bk+ek*bg+eg*ek), xr**2*eg*(2*bg+eg)]
        check(all(a >= b for a, b in zip(terms, exact_terms)), 'product error bounds '+str(ci*8192+k))
        region = [wl if region[0] is None else min(wl, region[0]), wu if region[1] is None else max(wu, region[1])]
        max_error = max(e, max_error)
        if wl > 0:
            positive += 1
        else:
            nonpositive += int(wu <= 0)
            crossing += int(wu > 0)
            failed_us.add(ui)
            observed.append((ci, xi, ui))
    check(iv(c['region_hulls'][ci]) == tuple(region), 'region hull '+str(ci))
    uniform = [region[0] if uniform[0] is None else min(uniform[0], region[0]),
               region[1] if uniform[1] is None else max(uniform[1], region[1])]
    summary.append(dict(region=ci, u=p['centers'][ci]['u'], positive=positive,
                        crossing=crossing, nonpositive=nonpositive,
                        failed_u_indices=sorted(failed_us), maximum_product_error=str(max_error)))
check(observed == [(z['center'], z['x_index'], z['u_index']) for z in c['failures']], 'complete failure list')
check(tuple(uniform) == iv(c['uniform_W']), 'global hull')
check(not c['runtime']['unexpected_signals'], 'exceptional signals')
worst = min(c['cells'], key=lambda z: F(z['W']['lower']))
result = dict(status='PASS' if not failures else 'FAIL', checks=checks, failures=failures,
              regions=summary, crossing_cells=len(observed), nonpositive_cells=sum(z['nonpositive'] for z in summary),
              worst_cell=worst, certificate=path.name,
              qualification='All records consumed and exact-rational coverage/error checks; no independent replay of signed polynomial formation or backend verification.')
OUT.write_text(json.dumps(result, indent=2)+'\n')
print('Inspection:', result['status'], 'checks=', checks, 'failures=', len(failures),
      'crossing=', result['crossing_cells'], 'nonpositive=', result['nonpositive_cells'])
print('Actual/required W lower:', c['uniform_W']['lower'], '>0; full inspection:', OUT)
for z in summary:
    if z['crossing'] or z['nonpositive']:
        print('Region', z['region'], 'failed u indices', z['failed_u_indices'],
              'crossing/nonpositive', z['crossing'], z['nonpositive'])
