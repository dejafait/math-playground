#!/usr/bin/env python3
"""Complete exact-rational internal evidence inspection; not independent audit."""
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import hashlib
import json
import time

ROOT = Path(__file__).resolve().parent
CERT = ROOT/'joint_kernel_2236.json'
OUT = ROOT/'joint_kernel_inspection_2236.json'
c = json.loads(CERT.read_text())
p = json.loads((ROOT/c['preflight']).read_text())
n = json.loads((ROOT/c['nodes']).read_text())
counts, failures = {}, []
started = time.monotonic()


def check(category, condition, location):
    counts[category] = counts.get(category, 0)+1
    if not condition:
        failures.append(dict(category=category, location=location))


def I(a):
    if isinstance(a, dict):
        return F(a['lower']), F(a['upper'])
    return tuple(map(F, a))


def add(a, b): return a[0]+b[0], a[1]+b[1]
def neg(a): return -a[1], -a[0]
def sub(a, b): return add(a, neg(b))
def pt(a): return F(a), F(a)
def mul(a, b):
    v = [x*y for x in a for y in b]
    return min(v), max(v)
def div(a, b):
    assert b[0] > 0
    return mul(a, (1/b[1], 1/b[0]))
def square(a):
    assert a[0] >= 0
    return a[0]**2, a[1]**2
def inflate(a, r): return a[0]-r, a[1]+r
def phase(s, co, j): return [s, co, neg(s), neg(co)][j % 4]
def horner(a, d):
    v = a[-1]
    for z in reversed(a[:-1]): v = add(mul(v, d), z)
    return v
def includes(saved, exact):
    a = I(saved)
    return a[0] <= exact[0] <= exact[1] <= a[1]

for name, path, digest in [('preflight', ROOT/c['preflight'], c['preflight_sha256']),
                          ('nodes', ROOT/c['nodes'], c['nodes_sha256']),
                          ('evaluator', ROOT/'joint_kernel_2236.py', c['script_sha256'])]:
    check('hash', hashlib.sha256(path.read_bytes()).hexdigest() == digest, name)
check('coverage', c['complete_box'] and len(c['joint_cells']) == 256*16*32, 'joint cells')
check('coverage', len(p['space']) == 1024 and len(p['suffix']) == 256 and
      len(n['saved']) == 256 and len(c['u_records']) == 256, 'all input rows')
check('settings', c['parameters'] == p['parameters'] and c['parameters'] == dict(
    U=4, indices=4, panels=65536, derivative_cells=1024, u_cells=256,
    x_cells=16, y_cells=32, centers=['57/4', '43/2'], radii=['1/4', '1/2'],
    frequency_degree=8, spatial_degree=3, precision=80, required_margin='1E-10'), 'frozen')
for loc, obj in [('preflight', p), ('nodes', n), ('certificate', c)]:
    rt = obj['runtime']
    check('runtime', not rt['unexpected_signals'], loc)
    for context, flags in rt['flags'].items():
        check('runtime', all(not v for name, v in flags.items()
                            if name not in ('Inexact', 'Rounded')), loc+context)
check('runtime', c['runtime']['counts']['nodes'] == 65537 and
      c['runtime']['counts']['trig_rotations'] == 131072 and
      c['runtime']['counts']['joint_cells'] == 131072, 'complete counts')

centers, radii = [F(57,4), F(43,2)], [F(1,4), F(1,2)]
indexfactor, space = F(p['constants']['index_factor']), F(p['constants']['space_tail'])
def tail(j): return indexfactor*factorial(j)/145**(j+1)+space
for k, row in enumerate(p['space']):
    l, r = F(k,256), F(k+1,256)
    check('spatial_coverage', row['index'] == k and F(row['left']) == l and F(row['right']) == r, k)
    es = list(map(F, row['E']))
    check('positive_bounds', all(e > 0 for e in es), k)
    for q, center in enumerate(centers):
        for j in range(9):
            pp = [r**(j-s)/factorial(j-s) if s <= j else F(0) for s in range(5)]
            db = [sum((comb(t,s)*pp[s]*es[t-s] for s in range(t+1)), F(0)) for t in range(5)]
            b4 = sum((comb(4,t)*db[t]*center**(4-t) for t in range(5)), F(0))
            check('fourth_bound', F(row['fourth'][q][j]) >= b4, [k,q,j])
    check('moment_part', F(row['mass_part']) >= es[0]/256 and
          F(row['ninth_part']) >= r**9*es[0]/256, k)

maxima = [[F(0)]*9 for _ in range(2)]
mass, ninth = tail(0), tail(9)
for k in range(1023,-1,-1):
    row=p['space'][k]
    mass += F(row['mass_part']); ninth += F(row['ninth_part'])
    maxima = [[max(maxima[q][j], F(row['fourth'][q][j])) for j in range(9)] for q in range(2)]
    if k < 256:
        sr=p['suffix'][str(k)]
        check('suffix_moments', F(sr['mass']) >= mass and F(sr['ninth']) >= ninth, k)
        check('suffix_maxima', [[F(v) for v in a] for a in sr['maxima']] == maxima, k)

minimum, maximum, minwhere = None, None, None
for k, ur in enumerate(c['u_records']):
    u=F(k,256); sr=p['suffix'][str(k)]; nr=n['saved'][str(k)]
    check('u_coverage', ur['index'] == k and F(ur['u']) == u and
          ur['joint_rows'] == [k*512,(k+1)*512], k)
    for q in range(2):
        raw=[[I(v) for v in a] for a in ur['unshifted_integrals'][q]]
        for j in range(9):
            required=(4-u)*F(1,16384)**4*F(sr['maxima'][q][j])/180+tail(j)/factorial(j)
            err=F(ur['quadrature_errors'][q][j])
            check('quadrature_error', err >= required, [k,q,j])
            for ph in range(2):
                quad=sub(I(n['total'][q][ph][j]), I(nr['prefix'][q][ph][j]))
                check('integral_enlargement', includes(raw[ph][j], inflate(quad,err)), [k,q,ph,j])
        co, si=I(nr['trig'][q][0]), I(nr['trig'][q][1])
        for ph in range(2):
            for j in range(9):
                v=pt(0)
                for ell in range(j+1):
                    sn=phase(raw[0][ell],raw[1][ell],j-ell+ph)
                    cs=phase(raw[0][ell],raw[1][ell],j-ell+ph+1)
                    rot=sub(mul(sn,co),mul(cs,si))
                    v=add(v,mul(pt((-u)**(j-ell)/factorial(j-ell)),rot))
                check('shifted_moment', includes(ur['shifted_coefficients'][q][ph][j],v), [k,q,ph,j])
        rem=F(ur['frequency_remainders'][q])
        check('frequency_remainder', rem >= radii[q]**9*F(sr['ninth'])/factorial(9), [k,q])
        base, length, ncell=(F(14),F(1,2),16) if q == 0 else (F(21),F(1),32)
        coeffs=[[I(v) for v in arr] for arr in ur['shifted_coefficients'][q]]
        check('frequency_coverage', len(ur['families'][q]) == ncell, [k,q])
        for j, fam in enumerate(ur['families'][q]):
            a,b=base+length*j/ncell,base+length*(j+1)/ncell
            freq=(a,b); dd=(a-centers[q],b-centers[q])
            check('frequency_coverage', I(fam['frequency']) == freq,[k,q,j])
            sint=inflate(horner(coeffs[0],dd),rem)
            cost=inflate(horner(coeffs[1],dd),rem)
            check('family_value', includes(fam['G'],mul(freq,sint)) and
                  includes(fam['Gprime'],neg(mul(square(freq),cost))),[k,q,j])
    kup=F(ur['K_upper']); m=F(ur['mass_upper'])
    check('spatial_majorants', kup >= F(nr['kernel'][1])+indexfactor and m == F(sr['mass']),k)
    fourth=F(ur['fourth_upper']); remainder=F(ur['u_remainder'])
    check('u_remainder', fourth >= F(29,2)**2*22**2*(kup+(F(29,2)**3+22**3)/F(923,4)*m)
          and remainder >= fourth*F(1,256)**4/24,k)
    localmin=None
    for i, xx in enumerate(ur['families'][0]):
        for j, yy in enumerate(ur['families'][1]):
            row=c['joint_cells'][k*512+i*32+j]
            check('joint_coverage', row[:3] == [k,i,j],[k,i,j])
            xs,ys=square(I(xx['frequency'])),square(I(yy['frequency']))
            den=sub(ys,xs)
            a0=div(sub(mul(ys,I(xx['G'])),mul(xs,I(yy['G']))),den)
            a1=div(sub(mul(ys,I(xx['Gprime'])),mul(xs,I(yy['Gprime']))),den)
            fac=div(mul(xs,ys),den)
            a2=mul(pt(F(1,2)),mul(fac,sub(I(yy['G']),I(xx['G']))))
            a3=mul(pt(F(1,6)),mul(fac,sub(I(yy['Gprime']),I(xx['Gprime']))))
            exact=inflate(horner([a0,a1,a2,a3],(F(0),F(1,256))),remainder)
            value=I(row[3:])
            check('joint_enclosure', includes(value,exact),[k,i,j])
            check('joint_margin', value[0] > F(1,10**10),[k,i,j])
            if minimum is None or value[0] < minimum: minimum,minwhere=value[0],[k,i,j]
            maximum=value[1] if maximum is None else max(maximum,value[1])
            localmin=value[0] if localmin is None else min(localmin,value[0])
    check('local_minimum', F(ur['local_minimum']) == localmin,k)
    if (k+1)%64 == 0: print('Exact inspection u cells:',k+1,'/256; failures:',len(failures),flush=True)
check('global_minimum', I(c['uniform_margin']) == (minimum,maximum) and c['minimum_cell'] == minwhere,'global')
check('positive_claim', minimum > F(69,10**10),'margin > 6.9e-9')
check('status', c['status'] == 'PASS' and not c['failures'],'certificate')
result=dict(status='PASS' if not failures else 'FAIL', checks=sum(counts.values()),
    categories=counts, failures=failures, minimum=str(minimum), required='1/10000000000',
    displayed_rational_lower='69/10000000000', minimum_cell=minwhere,
    records_consumed=dict(spatial=1024,suffix=256,node_snapshots=256,u=256,joint=131072),
    certificate_sha256=hashlib.sha256(CERT.read_bytes()).hexdigest(),
    inspection_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    qualification='Internal exact rational reconstruction from all saved evidence; not independent exponential recomputation, node replay, backend verification or critical mathematical audit.',
    elapsed_seconds=time.monotonic()-started)
OUT.write_text(json.dumps(result,indent=2)+'\n')
print('Result:',result['status'],'checks:',result['checks'],'failures:',len(failures),flush=True)
print('Actual minimum:',c['uniform_margin']['lower'],'required > 1e-10; certificate:',OUT,flush=True)
