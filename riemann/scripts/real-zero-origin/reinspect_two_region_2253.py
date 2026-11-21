#!/usr/bin/env python3
"""Replay unchanged2251 exact-rational checks to separate2253 output; same checker, not independent implementation."""
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent
PREF = ROOT / 'two_region_preflight_2251.json'
CERT = ROOT / 'two_region_2251.json'
OUT = ROOT / 'two_region_exact_cells_2253.json'
p, c = json.loads(PREF.read_text()), json.loads(CERT.read_text())
failures, checks = [], 0


def check(ok, label):
    global checks
    checks += 1
    if not ok:
        failures.append(label)


def iv(a):
    return F(a['lower']), F(a['upper'])


def add(a, b):
    return a[0]+b[0], a[1]+b[1]


def neg(a):
    return -a[1], -a[0]


def mul(a, b):
    q = [x*y for x in a for y in b]
    return min(q), max(q)


def scale(a, s):
    return mul(a, (s, s))


def inflate(a, e):
    return a[0]-e, a[1]+e


def contains(a, b):
    return a[0] <= b[0] <= b[1] <= a[1]


def horner(aa, x):
    r = aa[-1]
    for a in aa[-2::-1]:
        r = add(mul(r, x), a)
    return r


check(c['preflight_sha256'] == hashlib.sha256(PREF.read_bytes()).hexdigest(), 'preflight hash')
check(c['script_sha256'] == hashlib.sha256((ROOT/'two_region_2251.py').read_bytes()).hexdigest(), 'script hash')
check(p['parameters'] == c['parameters'], 'settings unchanged')
check(len(p['spatial_cells']) == 1280, 'all1280 spatial cells')
polys = [[F(a) for a in pp] for pp in p['derivative_polynomials']]
check(polys[0] == [0, -12, 8], 'P0')
for m in range(17):
    q = [F(0)]*(len(polys[m])+1)
    for k, a in enumerate(polys[m]):
        q[k] += (F(1, 2)+2*k)*a
        q[k+1] -= 2*a
    check(q == polys[m+1], f'P recurrence{m}')
for m, pp in enumerate(polys):
    a = sum((abs(v)*(4*k)**k for k, v in enumerate(pp)), F(0))
    check(a == F(p['derivative_A'][m]), f'A{m}')

compact9, compact17 = F(0), F(0)
for k, row in enumerate(p['spatial_cells']):
    check((F(row['left']), F(row['right'])) == (F(k, 256), F(k+1, 256)), f'spatial coverage{k}')
    bb = [F(x) for x in row['bounds']]
    check(len(bb) == 18 and all(x >= 0 for x in bb), f'finite derivative bounds{k}')
    a9 = F(1, 256)*F(k+1, 256)**9*bb[0] if k < 1024 else F(0)
    a17 = F(1, 256)*bb[17] if k < 1024 else F(0)
    check(F(row['moment9']) >= a9 and F(row['moment17']) >= a17, f'compact contributions{k}')
    compact9 += F(row['moment9'])
    compact17 += F(row['moment17'])
for name, total in [('moment9', compact9), ('derivative17', compact17)]:
    record = p[name]
    check(F(record['compact']) >= total, name+' summation')
    check(F(record['total']) >= sum((F(record[x]) for x in ['compact', 'index', 'spatial']), F(0)), name+' complete')
check(F(p['remainders']['x']) >= F(p['moment9']['total'])*F(1, 4)**9/factorial(9), 'x remainder')
check(F(p['remainders']['J']) >= F(p['derivative17']['total'])*F(1, 16)**16/factorial(17), 'J remainder')
check(F(p['remainders']['I']) >= F(p['derivative17']['total'])*F(1, 32)**17/factorial(17), 'I remainder')

coeffs = []
for ci, (bounds, result) in enumerate(zip(p['centers'], c['centers'])):
    uc = F(0) if ci == 0 else F(2*ci+1, 32)
    check(F(bounds['center']) == F(result['center']) == uc, f'center{ci}')
    fams = []
    for family in ['cosine', 'sine']:
        aa = []
        for j, a in enumerate(result[family]):
            e = bounds['errors'][j]
            check(F(e['simpson']) >= F(4**5, 180*16384**4)*F(e['fourth']), f'Simpson{ci}/{family}/{j}')
            check(F(e['total']) >= sum((F(e[k]) for k in ['simpson', 'index', 'spatial']), F(0)), f'error sum{ci}/{family}/{j}')
            check(F(a['error']) == F(e['total']), f'error used{ci}/{family}/{j}')
            check(contains(iv(a['enclosure']), inflate(iv(a['quadrature']), F(a['error']))), f'coefficient{ci}/{family}/{j}')
            aa.append(iv(a['enclosure']))
        check(len(aa) == 9, f'all coefficients{ci}/{family}')
        fams.append(aa)
    coeffs.append(fams)

check(len(c['parameter_jets']) == 512, 'all512 parameter jets')
for z, rec in enumerate(c['parameter_jets']):
    ci, xi = divmod(z, 32)
    check((rec['center_index'], rec['x_index']) == (ci, xi), f'jet index{z}')
    xl, xr = F(14)+F(xi, 64), F(14)+F(xi+1, 64)
    check(list(map(F, rec['x'])) == [xl, xr], f'x coverage{z}')
    dx = (xl-F(57, 4), xr-F(57, 4))
    ic, sc = iv(rec['I_center']), iv(rec['S_center'])
    check(contains(ic, inflate(horner(coeffs[ci][0], dx), F(p['remainders']['x']))), f'I x Taylor{z}')
    check(contains(sc, inflate(horner(coeffs[ci][1], dx), F(p['remainders']['x']))), f'S x Taylor{z}')
    aa = list(map(iv, rec['coefficients']))
    kj = list(map(iv, p['centers'][ci]['jets']))
    check(aa[0] == ic and contains(aa[1], add(mul((xl, xr), sc), neg(kj[0]))), f'initial jets{z}')
    x2 = (xl*xl, xr*xr)
    for k in range(15):
        rhs = add(neg(scale(kj[k+1], F(1, factorial(k)))), neg(mul(x2, aa[k])))
        want = scale(rhs, F(1, (k+1)*(k+2)))
        check(contains(aa[k+2], want), f'ODE coefficient{z}/{k}')

uniform = {'J': [None, None], 'I': [None, None]}
check(len(c['cells']) == 16384, 'all16384 closed box cells')
for z, row in enumerate(c['cells']):
    jetindex, ui = divmod(z, 32)
    ci, xi = divmod(jetindex, 32)
    name = 'J' if ci == 0 else 'I'
    uc = F(0) if ci == 0 else F(2*ci+1, 32)
    ul = F(ui, 512) if ci == 0 else F(ci, 16)+F(ui, 512)
    ur = ul+F(1, 512)
    check((row['observable'], row['center_index'], row['x_index'], row['u_index']) == (name, ci, xi, ui), f'cell index{z}')
    check(list(map(F, row['u'])) == [ul, ur], f'u coverage{z}')
    delta = ul-uc, ur-uc
    check(contains(iv(row['delta']), delta), f'delta{z}')
    aa = list(map(iv, c['parameter_jets'][jetindex]['coefficients']))
    want = inflate(horner(aa[1:] if name == 'J' else aa, delta), F(p['remainders'][name]))
    actual = iv(row['enclosure'])
    check(contains(actual, want), f'cell inclusion{z}')
    check(actual[0] > F(c['parameters']['required_'+name]), f'positive bound{z}')
    for side in (0, 1):
        old = uniform[name][side]
        uniform[name][side] = actual[side] if old is None else (min if side == 0 else max)(old, actual[side])
for name in uniform:
    check(tuple(uniform[name]) == iv(c['uniform'][name]), f'uniform hull{name}')
check(c['runtime']['counts']['nodes'] == 16*16385, 'all nodes')
check(c['runtime']['counts']['trig_rotations'] == 16384, 'all rotations')
check(c['failures'] == [] and c['runtime']['unexpected_signals'] == [], 'runtime failures')
check(c['status'] == 'PASS', 'recorded pass')
summary = dict(status='PASS' if not failures else 'FAIL', checks=checks, failures=failures,
    complete_records_consumed=dict(spatial_cells=1280, coefficient_intervals=288,
                                   parameter_jets=512, closed_cells=16384),
    uniform=c['uniform'], required={n: c['parameters']['required_'+n] for n in ['J', 'I']},
    hashes={f.name: hashlib.sha256(f.read_bytes()).hexdigest() for f in [PREF, CERT]},
    qualification='Internal exact-rational reconstruction consumes all relevant records; it does not independently recompute exp/node quadrature or verify the backend, and is not the separate conceptual audit.')
OUT.write_text(json.dumps(summary, indent=2)+'\n')
print('Inspection:', summary['status'], 'checks:', checks, 'failures:', len(failures))
print('Actual bounds:', c['uniform'], 'required:', summary['required'])
print('Full record:', OUT)
