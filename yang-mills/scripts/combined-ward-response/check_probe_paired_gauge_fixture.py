#!/usr/bin/env python3
"""Exact two-vertex gauge-jet test, not actual lattice/probe asymptotics."""
import argparse
import json
from fractions import Fraction as F
from itertools import product
from pathlib import Path
from check_probe_quartic_skew_split import (
    transpose, multiply as mm, vector, diagonal, chain, encode)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--case', choices=('isotropic', 'anisotropic-prefix', 'anisotropic-cross'),
                        default='anisotropic-cross')
    case = parser.parse_args().case
    d = [[F(1), F(0)], [F(-1), F(1)]]
    d += [[F((-1)**j), F(0)] for j in range(6)]
    d += [[F(0), F(-1)]]
    d += [[F(0), F((-1)**j)] for j in range(6)]
    m = len(d)
    ids = range(m)
    eye = diagonal([F(1)]*m)
    dt = transpose(d)
    chi = mm([[F(8,63), F(1,63)], [F(1,63), F(8,63)]], dt)
    p = [[eye[i][j]-chain(d, chi)[i][j] for j in ids] for i in ids]
    phi = [[F(j == 0) for j in ids], [F(j in (0,1)) for j in ids]]
    q = [[abs(v) for v in row] for row in d]
    v, f = mm(q, phi), mm(d, phi)
    hmap = [[eye[i][j]-f[i][j]/2 for j in ids] for i in ids]
    gamma = [[[-(hmap[e][r]*v[e][s]-hmap[e][s]*v[e][r])/2
               for s in ids] for r in ids] for e in ids]
    t0 = [p[i][2] for i in ids]
    u0 = [p[i][1] if case != 'isotropic' else F(0) for i in ids]
    u2 = sum(x*x for x in u0)
    cov = [[p[i][j]+u0[i]*u0[j] for j in ids] for i in ids]
    l = [[p[i][j]-u0[i]*u0[j]/(1+u2) for j in ids] for i in ids]
    t = vector(cov, t0)
    bi, bj = (2,9) if case == 'anisotropic-cross' else (0,1)
    b = [[p[i][bi]*p[j][bj]+p[i][bj]*p[j][bi] for j in ids] for i in ids]
    tilt = [[x*y for y in t] for x in t]
    a = [[x*y/2 for y in t0] for x in t0]
    gt = [[sum(t[u]*gamma[g][u][s] for u in ids) for s in ids] for g in ids]
    pg = mm(p, gt)
    pgs = mm(pg, cov)
    h = [[[2*sum(b[e][r]*gamma[e][s][u]+b[e][s]*gamma[e][u][r]
                    +b[e][u]*gamma[e][r][s] for e in ids)
           for u in ids] for s in ids] for r in ids]
    quartic = 6*sum(h[r][s][u]*t[s]*pgs[r][u] for r,s,u in product(ids, repeat=3))
    placements = [F(0)]*3
    for r,s,u,e in product(ids, repeat=4):
        for j, value in enumerate((b[e][r]*gamma[e][s][u],
                                    b[e][s]*gamma[e][u][r],
                                    b[e][u]*gamma[e][r][s])):
            placements[j] += 12*value*t[s]*pgs[r][u]
    # Independently form the cubic <Lz,W> and use all three covariance lines.
    w = [[[pg[r][u]*t0[s]-pg[r][s]*t0[u] for u in ids] for s in ids] for r in ids]
    lw = [[[sum(l[e][r]*w[e][s][u] for e in ids) for u in ids]
           for s in ids] for r in ids]
    k = [[[lw[r][s][u]+lw[s][u][r]+lw[u][r][s] for u in ids]
          for s in ids] for r in ids]
    hs1 = [[[sum(cov[r][e]*h[e][j][u] for e in ids) for u in ids]
            for j in ids] for r in ids]
    hs2 = [[[sum(cov[j][e]*hs1[r][e][u] for e in ids) for u in ids]
            for j in ids] for r in ids]
    hs3 = [[[sum(cov[u][e]*hs2[r][j][e] for e in ids) for u in ids]
            for j in ids] for r in ids]
    sextic_lw = sum(hs3[r][s][u]*k[r][s][u] for r,s,u in product(ids, repeat=3))
    assert mm(chi,d) == [[F(1),F(0)],[F(0),F(1)]]
    assert mm(phi,d) == [[F(1),F(0)],[F(0),F(1)]]
    assert mm(p,p) == p and chain(p,b,p) == b and chain(p,a,p) == a
    assert mm(p,d) == [[F(0),F(0)] for _ in ids]
    assert chain(p,tilt,p) == tilt
    assert mm(l,cov) == p and [[2*x for x in row] for row in chain(cov,a,cov)] == tilt
    assert quartic == sum(placements) == sextic_lw
    checks = {
        'projector_and_both_right_inverses': True,
        'full_symmetric_supported_B_and_A': True,
        'quartic_equals_three_placements': str(quartic) == str(sum(placements)),
        'quartic_equals_independent_sextic_LW_tensor': quartic == sextic_lw,
    }
    filename = {'isotropic': 'probe-paired-gauge-fixture-isotropic-zero.json',
                'anisotropic-prefix': 'probe-paired-gauge-fixture-anisotropic-zero.json',
                'anisotropic-cross': 'probe-paired-gauge-fixture-certificate.json'}[case]
    path = Path(__file__).with_name(filename)
    path.write_text(json.dumps({
        'scope': 'Two-interior-vertex pinned graph; synthetic S=P+uu^T, L=inverse on im P, A and B. Not actual box probes.',
        'case': case,
        'method': 'Exact Fraction tensor contraction; full three-line Isserlis and quartic derivative orders compared.',
        'checks': checks, 'failures': [key for key,val in checks.items() if not val],
        'discriminating_test': {'required': 'Q nonzero to refute universal paired cancellation',
                                'actual_Q': str(quartic), 'met': quartic != 0,
                                'conclusion': 'Inconclusive: zero does not establish a universal identity'},
        'values': {'quartic_Q': str(quartic), 'placements': list(map(str, placements)),
                   'sextic_J_LW': str(sextic_lw), 'sextic_J_rho_H': '0',
                   'paired_gradient_response': str(-quartic)},
        'fixture': {'D': encode(d), 'q': encode(q), 'Phi': encode(phi),
                    'chi': encode(chi), 'P': encode(p), 'S': encode(cov), 'L': encode(l),
                    'A': encode(a), 'B': encode(b)},
        'actual_bound': 'Unchanged O(N^(7/2)) for Q only; no bound for the paired actual response.',
        'required_bound': 'O(N^3) and a controlled scaled limit',
        'actual_probe_limit': None,
    }, indent=2)+'\n')
    print(f'Exact paired gauge fixture: {sum(checks.values())}/{len(checks)} PASS; failures {len(checks)-sum(checks.values())}')
    print(f'Discriminating nonzero test: {"PASS" if quartic else "NOT MET"}; case={case}')
    print(f'Q={quartic}; paired response={-quartic}; placements={placements}')
    print('Actual paired bound/limit not obtained; required O(N^3) and convergence')
    print(path)


if __name__ == '__main__':
    main()
