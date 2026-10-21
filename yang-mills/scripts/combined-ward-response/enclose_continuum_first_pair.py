"""L081 K=96 continuum tensor: Fourier/IBP spatial enclosure and full time rule.

Uses L036/L037 certified input records and L039 IEEE midpoint-radius rules.
Full moments, matrices, heat intervals and signed term records are saved.
"""
import hashlib
import json
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations
from math import factorial, isqrt
from pathlib import Path
import numpy as np
import check_stored_fourier_enclosure as sw
import check_signed_retained_enclosure as sr

ar, I, S = sw.arithmetic, sw.I, sw.S
rat = I.rational
ROOT = Path(__file__).parent
K, DEGREE = 96, 28
ZERO, ONE = rat(0), rat(1)


def rec(z):
    return dict(lo=str(z.lo), hi=str(z.hi))


def read(z):
    return I(int(z['lo']), int(z['hi']))


def pair(z):
    return dict(center_hex=float(z[0]).hex(), radius_hex=float(z[1]).hex())


def rational(q):
    return dict(numerator=str(q.numerator), denominator=str(q.denominator))


def enclosed(rows):
    obj = np.asarray(rows, dtype=object)
    v = np.asarray([sr.midpoint_radius(z) for z in obj.ravel()])
    return v[:, 0].reshape(obj.shape), v[:, 1].reshape(obj.shape)


def exact(x):
    c = np.asarray(x, dtype=float)
    return c, np.zeros_like(c)


def trans(z):
    return z[0].T, z[1].T


def cmul(a, b):
    return a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]


def cadd(a, b):
    return a[0]+b[0], a[1]+b[1]


def main():
    source = ROOT/'stored-fourier-enclosure-certificate.json'
    saved = json.loads(source.read_text())
    assert int(saved['scale']) == S and saved['degree'] == 144
    pi = read(saved['pi']); omega = pi/rat(8)
    norm0 = I(isqrt(S*S//8), isqrt(S*S//8)+1)
    assert 8*norm0.lo**2 <= S*S < 8*norm0.hi**2
    moments, moment_rows = {}, []
    # Import precisely the saved dyadic table with L037's total error.
    errors = {0: F(1565, 10**16), 1: F(3333, 10**16)}
    for row in saved['transforms']:
        h, n = row['h'], row['n']
        if abs(n) > 2*K: continue
        eps = rat(errors[h]).hi
        vals = []
        for key in ('stored_real_hex', 'stored_imag_hex'):
            v = rat(F(float.fromhex(row[key])))
            vals.append(I(v.lo-eps, v.hi+eps))
        moments[h, n] = tuple(vals)
        moment_rows.append(dict(h=h, n=n, real=rec(vals[0]), imag=rec(vals[1]), origin='L037'))
    assert len(moments) == 2*(4*K+1)
    # Smaller frequency range permits degree 84/284 phase approximants;
    # h<=3 keeps the total polynomial degree <=287 in both panel types.
    epsrho = F(348, 10**16)
    dt, dc = F(2*3**36, 3*4**84), F(2*3**179, 3*4**284)
    qerr = {h: 2*3**h*(epsrho+(1+epsrho)*dt)+10*F(5, 2)**h*dc for h in (2, 3)}
    assert all(qerr[h] < F(7, 10**14)*3**h for h in (2, 3))
    # Reuse every certified exact-rule node, weight and cutoff from L037.
    nodes = [(read(z['x']), read(z['weight'])*read(z['rho']))
             for p in saved['positive_panels'] for z in p['nodes']]
    assert len(nodes) == 288
    for n in range(K+1):
        totals = {2: ZERO, 3: ZERO}
        for x, wr in nodes:
            sine, cosine = sw.sin_cos(rat(n)*omega*x)
            xx = x*x
            totals[2] = totals[2]+rat(2)*wr*xx*cosine
            totals[3] = totals[3]+rat(2)*wr*xx*x*sine
        for h in (2, 3):
            err = rat(qerr[h]).hi
            v = I(totals[h].lo-err, totals[h].hi+err)
            z = (v, ZERO) if h == 2 else (ZERO, v)
            for signed in ((0,) if n == 0 else (n, -n)):
                zz = z if signed >= 0 else (z[0], -z[1])
                moments[h, signed] = zz
                moment_rows.append(dict(h=h, n=signed, real=rec(zz[0]), imag=rec(zz[1]), origin='exact rule plus generalized L036'))
        if n % 24 == 0: print(f'Enclosed new moments through frequency {n}/{K}', flush=True)

    @lru_cache(None)
    def basis(t, kind, n):
        freq = omega*rat(n)
        if kind == 'top':
            amp = norm0 if n == 0 else rat(F((-1)**n, 2))
            if t == 'V': amp = amp*freq
            return {(0, 0): (amp, ZERO)}
        if n == 0:
            assert t == 'E'
            if kind == 'b': return {(0, 0): (norm0, ZERO)}
            if kind == 'd': return {(0, 0): (ZERO, ZERO)}
            assert kind == 'prefix'
            return {(0, 0): (rat(4)*norm0, ZERO), (0, 1): (norm0, ZERO)}
        use_sine = (t == 'V' and kind == 'b') or (t == 'E' and kind in ('d', 'prefix'))
        amp = rat(F(1, 2))
        if kind == 'd': amp = amp*freq*(rat(-1) if t == 'E' else ONE)
        if kind == 'prefix': amp = amp/freq
        ans = {}
        for sign in (-1, 1):
            phase = ((1,0),(0,1),(-1,0),(0,-1))[(sign*n) % 4]
            z = (ZERO, -rat(F(sign, 2))*amp) if use_sine else (amp/rat(2), ZERO)
            ans[sign*n, 0] = cmul(z, (rat(phase[0]), rat(phase[1])))
        return ans

    def product(a, b):
        out = {}
        for (n, h), z in a.items():
            for (m, j), w in b.items():
                key = n+m, h+j
                out[key] = cadd(out.get(key, (ZERO, ZERO)), cmul(z, w))
        return out

    def derivative(poly):
        out = {}
        for (n, h), z in poly.items():
            key = n, h
            out[key] = cadd(out.get(key, (ZERO, ZERO)), cmul(z, (ZERO, omega*rat(n))))
            if h:
                key = n, h-1
                out[key] = cadd(out.get(key, (ZERO, ZERO)), cmul(z, (rat(h), ZERO)))
        return out

    @lru_cache(None)
    def entry(t, kind, n, weight, tt, kk, m):
        poly = product(basis(t, kind, n), basis(tt, kk, m))
        if weight == 'hf':
            poly = product(poly, {(0, 1): (rat(4), ZERO), (0, 2): (ONE, ZERO)})
            base, count = 0, 0
        else:
            base, count = {'r': (0,0), 'f': (1,0), 'rp': (0,1), 'fp': (1,1), 'fpp': (1,2)}[weight]
        for _ in range(count): poly = derivative(poly)
        val = (ZERO, ZERO)
        for (freq, h), z in poly.items():
            val = cadd(val, cmul(z, moments[h+base, freq]))
        if count % 2: val = (-val[0], -val[1])
        assert val[1].lo <= 0 <= val[1].hi  # Real row products.
        return val[0]

    types = lambda a: tuple('E' if j == a else 'V' for j in range(4))
    ordinary = lambda a: [(t, 'b') for t in types(a)]
    indices = {'E': range(K+1), 'V': range(1, K+1)}
    cache, archive = {}, {}
    def integral(a, weight, b):
        key = a, weight, b
        if key not in cache:
            raw = [[entry(*a, n, weight, *b, m) for m in indices[b[0]]] for n in indices[a[0]]]
            cache[key] = enclosed(raw)
            ix = len(cache)-1
            archive[f'spatial_{ix}_c'], archive[f'spatial_{ix}_r'] = cache[key]
        return cache[key]
    u = {0: [(1, ['f', 'r', 'fp', 'r'])], 2: [(-1, ['fp', 'r', 'f', 'r'])], 1: [], 3: []}
    ds = {'r': 'rp', 'f': 'fp', 'fp': 'fpp'}
    def deriv(terms, axis):
        out = []
        for sign, vec in terms:
            v = list(vec); v[axis] = ds[v[axis]]; out.append((sign, v))
        return out
    w = {a: deriv(u[a], a) for a in range(4)}
    shear = {(a,b): deriv(u[b], a)+deriv(u[a], b) for a,b in combinations(range(4),2)}
    def circulation(a,b):
        if a > b: return [(c,-s,v) for c,s,v in circulation(b,a)]
        out = []
        for c,j,s in ((b,a,1),(a,b,-1)):
            v = ordinary(c); v[j] = (types(c)[j], 'd'); out.append((c,s,v))
        return out
    Q = {3: [], 6: []}
    def addq(i, left, right, coeff, scale):
        for s,v in coeff:
            for a,sl,ll in left:
                for b,sr_,rr in right:
                    Q[i].append((a,b,scale*s*sl*sr_,[integral(x,c,y) for x,c,y in zip(ll,v,rr)]))
    for a,b in combinations(range(4),2):
        row = circulation(a,b); addq(3,row,row,w[a]+w[b],F(1))
        for c in range(4):
            if c in (a,b): continue
            left,right = circulation(a,c),circulation(b,c)
            addq(6,left,right,shear[a,b],F(1,2)); addq(6,right,left,shear[a,b],F(1,2))
    M = []
    for mu in (1,2,3):
        upper,lifted = [],[]
        for a in (mu,0):
            uf,vf = ordinary(a),ordinary(a); uf[0] = (types(a)[0],'top')
            sign = 1
            if a == 0:
                sign = -1; vf[0] = ('E','prefix'); uf[mu] = vf[mu] = ('V','d')
            upper.append((a,sign,uf)); lifted.append((a,sign,vf))
        for a,sl,ll in upper:
            for b,sr_,rr in lifted:
                M.append((a,b,F(sl*sr_),[integral(x,c,y) for x,c,y in zip(ll,['hf','r','fp','r'],rr)]))
    assert (len(M),len(Q[3]),len(Q[6])) == (12,24,96)
    print(f'Enclosed {len(cache)} distinct spatial matrices; all 132 component terms built', flush=True)
    sw.DEGREE = DEGREE
    roots,weights,root_rows = sw.roots_and_weights()
    panels = [(F(0),F(1,2**14))]+[(F(2)**j,F(2)**(j+1)) for j in range(-14,8)]
    nodes,ww,mapped = [],[],[]
    for ip,(a,b) in enumerate(panels):
        for ix,(z,w_) in enumerate(zip(roots,weights)):
            t = rat(F(1,16)+(a+b)/2)+rat((b-a)/2)*z
            wt = rat((b-a)/2)*w_; nodes.append(t); ww.append(wt)
            mapped.append(dict(panel=ip,root=ix,time=rec(t),weight=rec(wt)))
    lam = [omega*omega*rat(n*n) for n in range(K+1)]
    rawheat = [[ar.exp_negative(t*l) for l in lam] for t in nodes]
    he = enclosed(rawheat); heat = {'E':he,'V':(he[0][:,1:],he[1][:,1:])}; weights_mr = enclosed(ww)
    archive['heat_c'],archive['heat_r'] = he
    archive['weights_c'],archive['weights_r'] = weights_mr
    print(f'Enclosed {len(nodes)} time nodes and {len(nodes)*(K+1)} heat entries', flush=True)
    # Relative inverse error, uniform over the complete retained spectrum.
    # lambda <= 4*(K*pi/8)^2 < K^2 and initial lambda*2^-14 < 1.
    assert K*K < 2**14
    cg = F(factorial(DEGREE)**4,(2*DEGREE+1)*factorial(2*DEGREE)**3)
    rq = cg*(1+22*factorial(2*DEGREE+1))
    rt = ar.exp_negative(rat(256*F(27,64))).absolute_upper()
    rel = rq+rt
    cp = F(1296*1155*3,32)
    norm = {3:3025,6:820368}
    timeerr = {i: cp*norm[i]*(4*12**4)**2*(2*rel+rel*rel) for i in (3,6)}
    coverage,results = [],[]; count = len(nodes)
    def integrate(z):
        total = exact(0.)
        for a in range(0,count,160):
            for b in range(0,count,160):
                aa,bb = min(a+160,count),min(b+160,count)
                block = z[0][a:aa,b:bb],z[1][a:aa,b:bb]
                wa = weights_mr[0][a:aa],weights_mr[1][a:aa]
                wb = weights_mr[0][b:bb],weights_mr[1][b:bb]
                total = sr.add(total,sr.dot(sr.dot(wa,block),wb))
        return total
    for i in (3,6):
        total = exact(0.); nt = 0
        for im,(a,b,cm,mm) in enumerate(M):
            for iq,(qa,qb,cq,qq) in enumerate(Q[i]):
                if (qa,qb) != (b,a): continue
                value = exact(np.ones((count,count)))
                for j,(m,q) in enumerate(zip(mm,qq)):
                    prod = sr.multiply(m,trans(q))
                    feature = sr.dot(sr.dot(heat[types(a)[j]],prod),trans(heat[types(b)[j]]))
                    value = sr.multiply(value,feature)
                term = integrate(sr.multiply(value,enclosed(rat(cm*cq))))
                total = sr.add(total,term); nt += 1
                coverage.append(dict(probe=i,M=im,Q=iq,coefficient=str(cm*cq),integral=pair(term)))
        c,r = F(float(total[0])),F(float(total[1])); error = r+timeerr[i]+F(4,10**15)
        results.append(dict(probe=i,retained=pair(total),terms=nt,time_error=rational(timeerr[i]),
                            total_error=rational(error),lower=rational(c-error),upper=rational(c+error),
                            error_below_one=error<1,sign='negative' if c+error<0 else 'unresolved'))
        print(f'Probe {i}: center {float(c):.12g}; spatial/arithmetic radius {float(r):.6g}; time error {float(timeerr[i]):.6g}; total {float(error):.6g}, required <1; sign {results[-1]["sign"]}', flush=True)
    assert [r['terms'] for r in results] == [28,72]
    archive_path = ROOT/'continuum-first-pair-enclosure-factors.npz'
    np.savez_compressed(archive_path,**archive)
    failures = [f'probe {r["probe"]}: total error >=1 or sign unresolved' for r in results if not r['error_below_one'] or r['sign'] == 'unresolved']
    out = dict(K=K,degree=DEGREE,scale=str(S),pi=rec(pi),zero_norm=rec(norm0),moments=moment_rows,
        spatial_keys=[str(k) for k in cache],roots=root_rows,mapped_rule=mapped,
        heat=[[rec(z) for z in row] for row in rawheat],
        component_terms={label:[[a,b,str(c)] for a,b,c,_ in rows] for label,rows in [('M',M),('Q3',Q[3]),('Q6',Q[6])]},
        tensor_terms=coverage,relative_quadrature_error=rational(rq),relative_time_tail=rational(rt),results=results,failures=failures,
        input_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
        factor_archive=archive_path.name,factor_archive_sha256=hashlib.sha256(archive_path.read_bytes()).hexdigest(),
        script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        arithmetic_model='L039 IEEE addition/product/FMA, no overflow; underflow allowance 1e-290',
        qualifications=['Conditional on canonical L036/L037 certified inputs and L039 arithmetic model.',
                        'Only L081 selected continuum diagnostic; no complete response or logarithm.'])
    path = ROOT/'continuum-first-pair-enclosure-certificate.json'; path.write_text(json.dumps(out,indent=2)+'\n')
    print(f'Failures: {failures}; full certificate: {path}; factors: {archive_path}', flush=True)
    if failures: raise SystemExit(1)


if __name__ == '__main__':
    main()
