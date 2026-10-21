#!/usr/bin/env python3
"""Exact synthetic algebra checks; no actual-probe exponent certificate."""
import json
from fractions import Fraction as F
from itertools import product
from pathlib import Path

M = 4

def mm(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(M))
             for j in range(M)] for i in range(M)]

def add(a, b):
    c = dict(a)
    for k, v in b.items():
        c[k] = c.get(k, F(0)) + v
        if not c[k]:
            del c[k]
    return c

def scale(a, f):
    return {k: f*v for k, v in a.items() if f*v}

def mul(a, b):
    c = {}
    for k, v in a.items():
        for l, w in b.items():
            t = tuple(sorted(k+l))
            c[t] = c.get(t, F(0))+v*w
    return {k: v for k, v in c.items() if v}

def diff(a, j):
    c = {}
    for k, v in a.items():
        n = k.count(j)
        if n:
            t = list(k)
            t.remove(j)
            c[tuple(t)] = v*n
    return c

def eps(a, b, c):
    if len({a, b, c}) != 3:
        return 0
    return 1 if (a, b, c) in ((0,1,2),(1,2,0),(2,0,1)) else -1

def run(pinned):
    P = [[F(int(i == j and (not pinned or i != 0)))
          for j in range(M)] for i in range(M)]
    baseS = [[2,1,0,1],[1,3,1,0],[0,1,4,1],[1,0,1,3]]
    baseB = [[1,2,-1,0],[2,1,2,-1],[-1,2,0,1],[0,-1,1,2]]
    baseA = [[2,1,0,2],[1,2,1,2],[0,1,-1,0],[2,2,0,1]]
    S, B, A = [mm(mm(P, x), P) for x in (baseS,baseB,baseA)]
    T = [[2*x for x in row] for row in mm(S,A)]
    V = mm(T,S)
    phi = [F(1),F(1),F(-1),F(2)]
    q = [F(1),F(2),F(-1),F(3)]
    pref = [[q[e]*phi[r] for r in range(M)] for e in range(M)]
    dphi = [[phi[r] if e == 0 else F(0) for r in range(M)]
            for e in range(M)]
    gamma = [[[ -F(1,2)*(int(e==r)*pref[e][s]-int(e==s)*pref[e][r])
                +F(1,4)*(dphi[e][r]*pref[e][s]-dphi[e][s]*pref[e][r])
                for s in range(M)] for r in range(M)] for e in range(M)]
    z = [[{(3*r+c,): F(1)} for c in range(3)] for r in range(M)]
    b = [[{} for c in range(3)] for e in range(M)]
    for e,r,s,c,d,f in product(range(M),range(M),range(M),range(3),range(3),range(3)):
        v = gamma[e][r][s]*eps(c,d,f)/2
        if v:
            b[e][c] = add(b[e][c],scale(mul(z[r][d],z[s][f]),v))
    original_b = [[{} for c in range(3)] for e in range(M)]
    for e,r,s,c,d,f in product(range(M),range(M),range(M),range(3),range(3),range(3)):
        coef = (-F(1,2)*int(e==r)*pref[e][s]
                +F(1,4)*dphi[e][r]*pref[e][s])*eps(c,d,f)
        if coef:
            original_b[e][c] = add(original_b[e][c],scale(mul(z[r][d],z[s][f]),coef))
    assert b == original_b
    # Exact LDL pivots on the supported covariance space.
    ids = list(range(1,M)) if pinned else list(range(M))
    work = [[S[i][j] for j in ids] for i in ids]
    pivots = []
    for k in range(len(ids)):
        pivot = work[k][k]
        assert pivot > 0
        pivots.append(str(pivot))
        for i in range(k+1,len(ids)):
            for j in range(k+1,len(ids)):
                work[i][j] -= work[i][k]*work[k][j]/pivot
    tz = [[{} for c in range(3)] for r in range(M)]
    for r,s,c in product(range(M),range(M),range(3)):
        tz[r][c] = add(tz[r][c],scale(z[s][c],T[r][s]))
    W = [[{} for c in range(3)] for r in range(M)]
    for a,e,r,c,d in product(range(M),range(M),range(M),range(3),range(3)):
        if P[a][e]:
            W[a][c] = add(W[a][c],scale(mul(diff(b[e][c],3*r+d),tz[r][d]),P[a][e]))
    J = {}
    for e,r,c in product(range(M),range(M),range(3)):
        J = add(J,scale(mul(z[r][c],b[e][c]),2*B[e][r]))
    quartic = {}
    for r,c in product(range(M),range(3)):
        quartic = add(quartic,mul(diff(J,3*r+c),W[r][c]))
    def cov(i,j):
        return S[i//3][j//3] if i%3 == j%3 else F(0)
    direct = F(0)
    for k,v in quartic.items():
        assert len(k)==4
        a,b_,c,d=k
        direct += v*(cov(a,b_)*cov(c,d)+cov(a,c)*cov(b_,d)+cov(a,d)*cov(b_,c))
    h = [[[2*sum(B[e][a]*gamma[e][b_][c]+B[e][b_]*gamma[e][c][a]+B[e][c]*gamma[e][a][b_]
                  for e in range(M)) for c in range(M)] for b_ in range(M)] for a in range(M)]
    for a,b_,c in product(range(M),repeat=3):
        key = tuple(sorted((3*a,3*b_+1,3*c+2)))
        assert J.get(key,F(0)) == h[a][b_][c]
    contracted = F(0)
    placements = [F(0),F(0),F(0)]
    for a,b_,c,e,u,v in product(range(M),repeat=6):
        contracted += 6*h[a][b_][c]*P[a][e]*gamma[e][u][v]*V[u][b_]*S[v][c]
        for j,x in enumerate((B[e][a]*gamma[e][b_][c],B[e][b_]*gamma[e][c][a],B[e][c]*gamma[e][a][b_])):
            # g is the W output row, e the probe b output row.
            for g in range(M):
                placements[j] += 12*x*P[a][g]*gamma[g][u][v]*V[u][b_]*S[v][c]
    assert direct == contracted == sum(placements)
    H = [[F(int(e==r))-dphi[e][r]/2 for r in range(M)] for e in range(M)]
    def rowcov(X,Y,C,e,g):
        return sum(X[e][r]*C[r][s]*Y[g][s] for r,s in product(range(M),repeat=2))
    determinant = F(0)
    for e,g in product(range(M),repeat=2):
        determinant += 3*B[e][g]*(rowcov(H,H,V,e,g)*rowcov(pref,pref,S,e,g)
            -rowcov(H,pref,V,e,g)*rowcov(pref,H,S,e,g)
            -rowcov(pref,H,V,e,g)*rowcov(H,pref,S,e,g)
            +rowcov(pref,pref,V,e,g)*rowcov(H,H,S,e,g))
    assert determinant == placements[0]
    return {'case': 'singular_co_closed' if pinned else 'full_space',
            'direct_quartic': str(direct), 'tensor_contraction': str(contracted),
            'three_placements': [str(x) for x in placements],
            'first_placement_determinant': str(determinant),
            'all_equalities_exact': True, 'original_bracket_matches': True,
            'cubic_tensor_matches': True, 'covariance_positive_ldl_pivots': pivots,
            'quartic_monomials': len(quartic)}

if __name__ == '__main__':
    rows = [run(False), run(True)]
    cert = {'scope': 'Synthetic exact algebra only; maps are not actual box/probe data.',
            'method': 'Sparse polynomial derivative plus all three Gaussian fourth-moment pairings; rational arithmetic.',
            'checks': rows, 'failures': [], 'required': 'Exact equality in both cases',
            'actual_probe_bound': None, 'required_actual_probe_bound': 'O(N^3)',
            'actual_probe_limit': None}
    out = Path(__file__).with_name('probe-quartic-wick-certificate.json')
    out.write_text(json.dumps(cert,indent=2)+'\n')
    print('Exact quartic/tensor/three-placement/determinant checks: 2/2 PASS; failures: 0')
    print('Actual-probe bound: not obtained; required O(N^3); limit: not obtained')
    print(out)
