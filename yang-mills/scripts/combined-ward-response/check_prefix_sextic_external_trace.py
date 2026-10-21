#!/usr/bin/env python3
"""Exact signed trace algebra only; no actual box/probe asymptotics."""
import json
from fractions import Fraction as F
from functools import lru_cache
from itertools import permutations, product
from pathlib import Path

from check_probe_quartic_wick import add, scale, mul, diff, eps, mm

NVAR = 4
IDS = range(NVAR)


def tr(a):
    return sum(a[i][i] for i in IDS)


def transpose(a):
    return list(map(list, zip(*a)))


def madd(a, b, factor=1):
    return [[a[i][j] + factor*b[i][j] for j in IDS] for i in IDS]


def alt_tensor(values):
    out = [[[F(0) for _ in IDS] for _ in IDS] for _ in IDS]
    for triple, val in zip(((0,1,2),(0,1,3),(0,2,3),(1,2,3)), values):
        for order in permutations(range(3)):
            sign = (-1)**sum(order[i] > order[j] for i in range(3) for j in range(i+1,3))
            i,j,k = [triple[x] for x in order]
            out[i][j][k] = F(sign*val)
    return out


def cubic(c):
    return {(3*a,3*b+1,3*d+2): c[a][b][d]
            for a,b,d in product(IDS, repeat=3) if c[a][b][d]}


def run(singular):
    p = [[F(i == j and (not singular or i != 0)) for j in IDS] for i in IDS]
    bases = (
        [[2,1,0,1],[1,3,1,0],[0,1,4,1],[1,0,1,3]],
        [[2,1,0,2],[1,2,1,2],[0,1,-1,0],[2,2,0,1]],
        [[1,2,-1,0],[2,1,2,-1],[-1,2,0,1],[0,-1,1,2]],
    )
    cov, a, bmat = [mm(mm(p,x),p) for x in bases]
    tilt = [[2*x for x in row] for row in mm(cov,a)]
    m = mm(tilt,cov)
    pref = [[F(q*v) for v in (1,1,-1,2)] for q in (1,2,-1,3)]
    f = [[F(v if e == 0 else 0) for v in (1,1,-1,2)] for e in IDS]
    hmap = [[F(e == r)-f[e][r]/2 for r in IDS] for e in IDS]
    gamma = [[[-(hmap[e][r]*pref[e][s]-hmap[e][s]*pref[e][r])/2
               for s in IDS] for r in IDS] for e in IDS]
    z = [[{(3*r+c,): F(1)} for c in range(3)] for r in IDS]
    bz = [[{} for _ in range(3)] for _ in IDS]
    for e,r,s,c,d,g in product(IDS,IDS,IDS,range(3),range(3),range(3)):
        coef = gamma[e][r][s]*eps(c,d,g)/2
        if coef:
            bz[e][c] = add(bz[e][c],scale(mul(z[r][d],z[s][g]),coef))
    tz = [[{} for _ in range(3)] for _ in IDS]
    for r,s,c in product(IDS,IDS,range(3)):
        tz[r][c] = add(tz[r][c],scale(z[s][c],tilt[r][s]))
    j = {}
    for e,r,c in product(IDS,IDS,range(3)):
        j = add(j,scale(mul(z[r][c],bz[e][c]),2*bmat[e][r]))
    action_tensor, residual_tensor = alt_tensor((2,-1,3,1)), alt_tensor((-3,4,1,-2))
    action, residual = cubic(action_tensor), cubic(residual_tensor)
    # Canonical monomial ordering is enforced before differentiation/moments.
    action = {tuple(sorted(k)): v for k,v in action.items()}
    residual = {tuple(sorted(k)): v for k,v in residual.items()}
    ds = {}
    for r,c in product(IDS,range(3)):
        ds = add(ds,mul(diff(action,3*r+c),tz[r][c]))
    rho = add(residual,scale(ds,-1))
    w = [[{} for _ in range(3)] for _ in IDS]
    for out,e,r,c,d in product(IDS,IDS,IDS,range(3),range(3)):
        if p[out][e]:
            w[out][c] = add(w[out][c],scale(mul(diff(bz[e][c],3*r+d),tz[r][d]),p[out][e]))
    quartic = {}
    for r,c in product(IDS,range(3)):
        quartic = add(quartic,mul(diff(j,3*r+c),w[r][c]))

    @lru_cache(None)
    def moment(key):
        if not key:
            return F(1)
        i, rest = key[0], key[1:]
        return sum((cov[i//3][k//3]*moment(rest[:pos]+rest[pos+1:])
                    for pos,k in enumerate(rest) if i%3 == k%3), F(0))

    def expectation(poly):
        return sum((val*moment(key) for key,val in poly.items()), F(0))

    direct_sextic = expectation(mul(j,rho))
    direct_quartic = expectation(quartic)
    sb = mm(cov,bmat)
    trace_parts = [F(0)]*4
    for e in IDS:
        n = [sb[r][e] for r in IDS]
        tn = [sum(tilt[r][s]*n[s] for s in IDS) for r in IDS]
        def sliced(tensor, vec):
            return [[sum(vec[r]*tensor[r][u][v] for r in IDS) for v in IDS] for u in IDS]
        rn, sn, stn = sliced(residual_tensor,n), sliced(action_tensor,n), sliced(action_tensor,tn)
        jj = mm(mm(p,gamma[e]),p)
        # U_n is defined directly by its two row wedges, without a product-rule assumption.
        vn = [sum(pref[g][r]*n[r] for r in IDS) for g in IDS]
        hn = [sum(hmap[g][r]*n[r] for r in IDS) for g in IDS]
        un = [[vn[g]*hmap[g][r]-hn[g]*pref[g][r] for r in IDS] for g in IDS]
        blocks = (mm(mm(cov,rn),cov), mm(mm(cov,stn),cov), mm(mm(m,sn),cov), mm(m,transpose(un)))
        for idx,(factor,block) in enumerate(zip((-6,6,12,6),blocks)):
            trace_parts[idx] += factor*tr(mm(jj,block))

    placements = [F(0)]*3
    for e,g,r,s,u,v in product(IDS, repeat=6):
        placements[0] += 12*bmat[e][g]*gamma[e][r][s]*gamma[g][u][v]*m[u][r]*cov[v][s]
        placements[1] += 12*mm(m,bmat)[u][e]*gamma[e][s][r]*p[r][g]*gamma[g][u][v]*cov[v][s]
        placements[2] += 12*sb[v][e]*gamma[e][r][s]*p[r][g]*gamma[g][u][v]*m[u][s]
    checks = {
        'supported_symmetric_covariance_and_tilt': mm(p,cov) == cov and transpose(m) == m,
        'sextic_equals_external_trace': direct_sextic == sum(trace_parts[:3]),
        'quartic_equals_three_placements': direct_quartic == sum(placements),
        'third_placement_sign': trace_parts[3] == -placements[2],
        'complete_pair_equals_common_trace_minus_Q1_Q2': direct_sextic-direct_quartic == sum(trace_parts)-placements[0]-placements[1],
    }
    return {'case': 'singular_supported' if singular else 'full_space',
            'checks': checks, 'direct_sextic': str(direct_sextic),
            'external_trace_parts': list(map(str,trace_parts)),
            'direct_quartic': str(direct_quartic),
            'quartic_placements': list(map(str,placements)),
            'complete_pair': str(direct_sextic-direct_quartic)}


if __name__ == '__main__':
    rows = [run(False),run(True)]
    failures = [row['case']+':'+key for row in rows for key,val in row['checks'].items() if not val]
    out = Path(__file__).with_name('prefix-sextic-external-trace-certificate.json')
    out.write_text(json.dumps({'scope': 'Synthetic rational algebra; neither actual Wilson cubics nor actual probes.',
        'method': 'Direct sparse polynomial differentiation and complete Gaussian moments versus signed matrix traces.',
        'records': rows, 'failures': failures,
        'actual_analytic_bound': 'O(N^3 sqrt(log(eN))) for sextic; smooth-tilt placement O(sqrt(log(eN)))',
        'required': 'O(N^3) for complete paired response, then controlled convergence',
        'actual_probe_limit': None},indent=2)+'\n')
    print(f'Exact trace checks: {sum(sum(row["checks"].values()) for row in rows)}/10; failures: {len(failures)}')
    print('Analytic sextic bound N^3 sqrt(log(eN)); required paired bound N^3 and convergence; not certified by fixtures')
    print(out)
    if failures:
        raise SystemExit(1)
