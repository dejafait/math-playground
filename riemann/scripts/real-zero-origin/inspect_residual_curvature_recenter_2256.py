#!/usr/bin/env python3
"""Inspect all2256 records and exactly check the worst-cell translation."""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent
OUT = ROOT/'residual_curvature_recenter_inspection_2256.json'
path = ROOT/'residual_curvature_recenter_2256.json'
c = json.loads(path.read_text())
p = json.loads((ROOT/c['preflight']).read_text())
old = json.loads((ROOT/p['source']).read_text())
op = json.loads((ROOT/p['original_preflight']).read_text())
checks, failures = 0, []


def check(ok,name):
    global checks
    checks += 1
    if not ok:
        failures.append(name)


def iv(z):
    return F(z['lower']), F(z['upper'])


def add(a,b):
    return a[0]+b[0],a[1]+b[1]


def scale(a,h):
    return (a[0]*h,a[1]*h) if h >= 0 else (a[1]*h,a[0]*h)


def packf(a):
    return dict(lower=str(a[0]),upper=str(a[1]))


check(c['preflight_sha256'] == hashlib.sha256((ROOT/c['preflight']).read_bytes()).hexdigest(),'preflight hash')
check(c['script_sha256'] == hashlib.sha256((ROOT/'residual_curvature_recenter_2256.py').read_bytes()).hexdigest(),'script hash')
check(p['source_sha256'] == hashlib.sha256((ROOT/p['source']).read_bytes()).hexdigest(),'old full certificate hash')
check(p['original_preflight_sha256'] == hashlib.sha256((ROOT/p['original_preflight']).read_bytes()).hexdigest(),'old preflight hash')
check(old['preflight_sha256'] == p['original_preflight_sha256'],'original binding')
for name,digest in op['input_hashes'].items():
    check(digest == hashlib.sha256((ROOT/name).read_bytes()).hexdigest(),'prior input hash '+name)
check(len(c['cells']) == len(old['cells']) == c['total_cells'] == p['total_cells'] == 131072,'all closed cells')
check(p['precision'] == op['precision'] == 80 and p['x_cells'] == op['x_cells'] == 256 and p['u_subcells'] == op['u_subcells'] == 32,'unchanged settings')
observed, summary = [], []
uniform = [None,None]
for ci in range(16):
    rows = c['cells'][ci*8192:(ci+1)*8192]
    region = [None,None]
    positive = crossing = nonpositive = 0
    failed_us, max_error = set(),F(0)
    for k,z in enumerate(rows):
        xi,ui = divmod(k,32)
        idx = ci*8192+k
        prior = old['cells'][idx]
        check((z['center'],z['x_index'],z['u_index']) == (ci,xi,ui),'cell indices '+str(idx))
        ul,ur = F(ci,16)+F(ui,512),F(ci,16)+F(ui+1,512)
        check(list(map(F,z['u'])) == [ul,ur] and z['u'] == prior['u'],'closed u coverage '+str(idx))
        jet = old['parameter_jets'][ci*256+xi]
        check(list(map(F,jet['x'])) == [F(14)+F(xi,512),F(14)+F(xi+1,512)],'closed x coverage '+str(idx))
        check(F(z['shift']) == (ul+ur)/2-F(op['centers'][ci]['center']),'exact midpoint shift '+str(idx))
        check(F(p['variable_radius']) == (ur-ul)/2 == F(1,1024),'exact cell radius '+str(idx))
        a,b = iv(z['translated_constant']),iv(z['translated_nonconstant'])
        pl,pu = iv(z['polynomial'])
        wl,wu = iv(z['W'])
        e = F(z['error'])
        check(a[0] <= a[1] and b[0] == -b[1] and b[1] >= 0 and pl <= pu and wl <= wu and e >= 0,'interval order '+str(idx))
        check(pl <= a[0]+b[0] and pu >= a[1]+b[1],'translated sum enclosure '+str(idx))
        check(wl <= pl-e and wu >= pu+e,'full inflation '+str(idx))
        check(all(z[v] == prior[v] for v in ('error','polynomial_magnitudes','error_terms')),'unchanged full error '+str(idx))
        terms = list(map(F,z['error_terms']))
        check(len(terms) == 3 and min(terms) >= 0 and e >= sum(terms),'all nonlinear errors '+str(idx))
        bi,bg,bk = map(F,z['polynomial_magnitudes'])
        ei,eg,ek = (F(op['centers'][ci][v]) for v in ('error_I','error_G','error_K'))
        xr = F(14)+F(xi+1,512)
        exact_terms = [xr**4*ei*(2*bi+ei),xr**2*(eg*bk+ek*bg+eg*ek),xr**2*eg*(2*bg+eg)]
        check(all(a >= b for a,b in zip(terms,exact_terms)),'exact product error bounds '+str(idx))
        region = [wl if region[0] is None else min(wl,region[0]),wu if region[1] is None else max(wu,region[1])]
        max_error = max(e,max_error)
        if wl > 0:
            positive += 1
        else:
            crossing += int(wu > 0)
            nonpositive += int(wu <= 0)
            failed_us.add(ui)
            observed.append((ci,xi,ui))
    check(iv(c['region_hulls'][ci]) == tuple(region),'region hull '+str(ci))
    uniform = [region[0] if uniform[0] is None else min(uniform[0],region[0]),region[1] if uniform[1] is None else max(uniform[1],region[1])]
    summary.append(dict(region=ci,u=op['centers'][ci]['u'],positive=positive,crossing=crossing,
                        nonpositive=nonpositive,failed_u_indices=sorted(failed_us),maximum_product_error=str(max_error)))
check(observed == [(z['center'],z['x_index'],z['u_index']) for z in c['failures']],'complete failure list')
check(tuple(uniform) == iv(c['uniform_W']),'uniform hull')
check(not c['runtime']['unexpected_signals'],'exceptional signals')
check((c['status'] == 'PASS') == (len(observed) == 0),'status matches evidence')
w = c['worst_cell']
idx = (w['center']*256+w['x_index'])*32+w['u_index']
check(all(w[v] == c['cells'][idx][v] for v in c['cells'][idx]),'worst cell full match')
check(iv(w['W'])[0] == uniform[0],'actual worst lower')
aa = list(map(iv,old['parameter_jets'][w['center']*256+w['x_index']]['W']))
bb = list(map(iv,w['translated_coefficients']))
check(len(bb) == len(aa) == 33,'worst complete coefficients')
h = F(w['shift'])
exact_coeff = []
for j in range(33):
    exact = (F(0),F(0))
    for k in range(j,33):
        exact = add(exact,scale(aa[k],comb(k,j)*h**(k-j)))
    exact_coeff.append(packf(exact))
    check(bb[j][0] <= exact[0] <= exact[1] <= bb[j][1],'exact binomial coefficient '+str(j))
tail = bb[-1]
r = F(1,1024)
for coeff in bb[-2:0:-1]:
    mag = max(abs(tail[0]),abs(tail[1]))*r
    tail = add((-mag,mag),coeff)
mag = max(abs(tail[0]),abs(tail[1]))*r
stored_tail = iv(w['translated_nonconstant'])
check(stored_tail[0] <= -mag and stored_tail[1] >= mag,'worst exact symmetric Horner')
check(iv(w['translated_constant']) == bb[0],'worst constant coefficient')
result = dict(status='PASS' if not failures else 'FAIL',checks=checks,failures=failures,
              certificate=path.name,regions=summary,crossing_cells=len(observed),
              nonpositive_cells=sum(z['nonpositive'] for z in summary),worst_cell=w,
              worst_exact_binomial_intervals=exact_coeff,
              qualification='Every cell/coverage/error record consumed; full exact binomial and symmetric Horner check at the worst cell only. Not an independent replay of all translations, polynomial formation, quadrature or arithmetic backend.')
OUT.write_text(json.dumps(result,indent=2)+'\n')
print('Inspection:',result['status'],'checks=',checks,'failures=',len(failures),
      'crossing=',result['crossing_cells'],'nonpositive=',result['nonpositive_cells'])
print('Actual/required W lower:',c['uniform_W']['lower'],'>0; full inspection:',OUT)
for z in summary:
    if z['crossing'] or z['nonpositive']:
        print('Region',z['region'],'failed u indices',z['failed_u_indices'],'crossing/nonpositive',z['crossing'],z['nonpositive'])
