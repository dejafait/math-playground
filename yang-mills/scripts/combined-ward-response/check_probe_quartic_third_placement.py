#!/usr/bin/env python3
"""Exact signed Q3 and pinned product checks; no actual-probe growth test."""
import json
from fractions import Fraction as F
from itertools import product
from pathlib import Path

from check_probe_quartic_wick import M as size, mm, run


def tr(x):
    return [list(row) for row in zip(*x)]


def check(pinned):
    reference = run(pinned)
    p = [[F(int(i == j and (not pinned or i != 0)))
          for j in range(size)] for i in range(size)]
    s, b, a = [mm(mm(p, x), p) for x in (
        [[2, 1, 0, 1], [1, 3, 1, 0], [0, 1, 4, 1], [1, 0, 1, 3]],
        [[1, 2, -1, 0], [2, 1, 2, -1], [-1, 2, 0, 1], [0, -1, 1, 2]],
        [[2, 1, 0, 2], [1, 2, 1, 2], [0, 1, -1, 0], [2, 2, 0, 1]])]
    tilt = [[2*x for x in row] for row in mm(mm(s, a), s)]
    phi, q = [F(1), F(1), F(-1), F(2)], [F(1), F(2), F(-1), F(3)]
    v = [[q[e]*phi[r] for r in range(size)] for e in range(size)]
    h = [[F(int(e == r))-(phi[r]/2 if e == 0 else F(0))
          for r in range(size)] for e in range(size)]
    hp, vp = mm(h, p), mm(v, p)
    khh, khv, kvh, kvv = [mm(mm(x, tilt), tr(y))
                          for x, y in ((h, h), (h, v), (v, h), (v, v))]
    hn, vn = mm(h, s), mm(v, s)
    terms = [F(0)]*4
    traces = F(0)
    for k in range(size):
        # B=sum_k unit_k B[k,:]; n=S unit_k, y=B[k,:].
        y = b[k]
        jy = [[-(sum(h[e][r]*y[e]*v[e][t]-v[e][r]*y[e]*h[e][t]
                     for e in range(size)))/2
               for t in range(size)] for r in range(size)]
        un = [[vn[g][k]*h[g][u]-hn[g][k]*v[g][u]
               for u in range(size)] for g in range(size)]
        closed = mm(mm(mm(p, jy), tilt), tr(un))
        traces += -6*sum(closed[g][g] for g in range(size))
        for e, g in product(range(size), repeat=2):
            weights = (hp[e][g]*vn[g][k]*kvh[e][g],
                       -hp[e][g]*hn[g][k]*kvv[e][g],
                       -vp[e][g]*vn[g][k]*khh[e][g],
                       vp[e][g]*hn[g][k]*khv[e][g])
            for j, value in enumerate(weights):
                terms[j] += 3*y[e]*value
    expected = F(reference['three_placements'][2])
    assert sum(terms) == traces == expected
    return {'case': reference['case'], 'four_signed_terms': list(map(str, terms)),
            'row_sum': str(sum(terms)), 'projected_trace': str(traces),
            'polynomial_Q3': str(expected), 'exact_match': True}


def pinned_product():
    # Three normal edges, two interior vertices; both outside values are zero.
    d = [[F(1), F(0)], [F(-1), F(1)], [F(0), F(-1)]]
    q = [[F(1), F(0)], [F(1), F(1)], [F(0), F(1)]]
    phi = [[F(1), F(0), F(0)], [F(1), F(1), F(0)]]
    p = [[F(1, 3)]*3 for _ in range(3)]
    def mult(x, y):
        return [[sum(x[i][k]*y[k][j] for k in range(len(y)))
                 for j in range(len(y[0]))] for i in range(len(x))]
    v, f = mult(q, phi), mult(d, phi)
    h = [[F(int(i == j))-f[i][j]/2 for j in range(3)] for i in range(3)]
    n = [F(2), F(-3), F(5)]
    hn = [sum(h[i][j]*n[j] for j in range(3)) for i in range(3)]
    vn = [sum(v[i][j]*n[j] for j in range(3)) for i in range(3)]
    rn = [n[i]-sum(f[i][j]*n[j] for j in range(3)) for i in range(3)]
    un = [[vn[i]*h[i][j]-hn[i]*v[i][j] for j in range(3)] for i in range(3)]
    reduced = [[vn[i]*F(int(i == j))-rn[i]*v[i][j] for j in range(3)]
               for i in range(3)]
    left, right = mult(p, un), mult(p, reduced)
    assert left == right
    upper = [vn[2]*F(int(j == 2))-n[2]*v[2][j] for j in range(3)]
    assert un[2] == upper
    assert mult(p, d) == [[F(0)]*2 for _ in range(3)]
    return {'case': 'two_interior_vertices_all_normal_end_edges',
            'P_U': [[str(x) for x in row] for row in left],
            'P_reduced_U': [[str(x) for x in row] for row in right],
            'upper_U_row': list(map(str, upper)), 'exact_match': True,
            'P_D_zero': True, 'upper_two_prefix_cancellation': True}


if __name__ == '__main__':
    rows = [check(False), check(True)]
    boundary = pinned_product()
    certificate = {
        'scope': 'Synthetic rational algebra only; all-mesh bound is analytic in L187.',
        'checks': rows, 'pinned_product': boundary, 'failures': [],
        'actual_bound': 'O(N^(7/2)) analytically; no signed lower bound',
        'required_bound': 'O(N^3)', 'remaining_power_loss': '1/2',
        'actual_probe_limit': None,
        'analytic_reference': 'lemmas/L187-probe-quartic-third-placement-projected-trace.md'}
    out = Path(__file__).with_name('probe-quartic-third-placement-certificate.json')
    out.write_text(json.dumps(certificate, indent=2)+'\n')
    print('Signed Q3 row/trace checks: 2/2 PASS; pinned product/end-row: PASS; failures: 0')
    print('Analytic upper bound O(N^(7/2)); required O(N^3); remaining power loss 1/2; no limit')
    print(out)
