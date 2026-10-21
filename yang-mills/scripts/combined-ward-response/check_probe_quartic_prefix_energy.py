#!/usr/bin/env python3
"""Exact pinned-prefix trace checks supporting L186; no fitted exponents."""
import json
from fractions import Fraction as F
from itertools import product
from pathlib import Path


def mm(a, b):
    cols = list(zip(*b))
    return [[sum(x*y for x, y in zip(row, col)) for col in cols]
            for row in a]


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def trace_product(a, b):
    return sum(a[i][j]*b[j][i] for i in range(len(a))
               for j in range(len(a)))


def inverse(a):
    n = len(a)
    rows = [[F(x) for x in row]+[F(i == j) for j in range(n)]
            for i, row in enumerate(a)]
    for j in range(n):
        pivot = rows[j][j]
        assert pivot > 0
        rows[j] = [x/pivot for x in rows[j]]
        for i in range(n):
            if i != j and rows[i][j]:
                factor = rows[i][j]
                rows[i] = [x-factor*y for x, y in zip(rows[i], rows[j])]
    return [row[n:] for row in rows]


def axial(n):
    u = [[min(i+1, j+1) for j in range(n)] for i in range(n)]
    ld = [[2*int(i == j)-int(abs(i-j) == 1) for j in range(n)]
          for i in range(n)]
    lm = [row[:] for row in ld]
    lm[-1][-1] -= 1
    ident = [[int(i == j) for j in range(n)] for i in range(n)]
    assert mm(u, lm) == ident
    w = mm(u, ld)
    assert w == [[int(i == j)+(i+1)*int(j == n-1)
                  for j in range(n)] for i in range(n)]
    values = [trace_product(w, w), trace_product(w, u),
              trace_product(u, u)]
    expected = [n*n+3*n, n*(n+1)*(n+2)//3,
                n*(n+1)*(n*n+n+1)//6]
    assert values == expected
    return u, ld, {'N': n+1, 'n': n, 'upper_rank_one_retained': True,
                   'inverse_identity': True,
                   'tr_UL_UL': values[0], 'tr_UL_U': values[1],
                   'tr_U2': values[2], 'exact_expected': expected,
                   'all_equal': True}


def tensor(N):
    n = N-1
    u, ld, _ = axial(n)
    sites = list(product(range(n), repeat=3))
    delta = [[6*int(x == y)-int(sum(abs(s-t) for s, t in zip(x, y)) == 1)
              for y in sites] for x in sites]
    g = inverse(delta)
    size = len(g)
    rows = list(product(range(n), range(size)))
    k0 = [[u[s][t]*g[x][y] for t, y in rows] for s, x in rows]
    # The full four-dimensional scalar Dirichlet Laplacian is sparse.
    # Its diagonal is 8 even on rows next to physical faces.
    lap_cols = [[(j, ld[s][t]*int(x == y)+int(s == t)*delta[x][y])
                 for j, (t, y) in enumerate(rows)
                 if ld[s][t]*int(x == y)+int(s == t)*delta[x][y]]
                for s, x in rows]
    w = [[sum(row[j]*v for j, v in col) for col in lap_cols]
         for row in k0]
    actual = trace_product(w, w)
    t1 = trace_product(mm(u, ld), mm(u, ld))*trace_product(g, g)
    t2 = 2*trace_product(mm(u, ld), u)*trace(g)
    t3 = trace_product(u, u)*size
    assert actual == t1+t2+t3
    return {'N': N, 'vertex_count': len(rows), 'transverse_vertex_count': size,
            'all_physical_end_diagonals_retained': True,
            'full_scalar_trace': str(actual),
            'three_tensor_terms': list(map(str, [t1, t2, t3])),
            'tensor_sum': str(t1+t2+t3), 'exact_match': True}


if __name__ == '__main__':
    axial_records = [axial(N-1)[2] for N in (2, 4, 6, 8, 16, 32)]
    tensor_records = [tensor(N) for N in (2, 4)]
    certificate = {
        'scope': 'Exact endpoint/trace identities only; full-mesh estimates are analytic in L186.',
        'axial_records': axial_records, 'tensor_records': tensor_records,
        'failures': [], 'required': 'All exact identities pass with upper pinned correction retained.',
        'analytic_bound_reference': 'lemmas/L186-probe-quartic-first-placement-subcubic.md',
        'analytic_DKD_HS_bound': 'O(N^(7/2))',
        'analytic_Q1_bound': 'O(N^(5/2))', 'required_cubic_bound': 'O(N^3)',
        'actual_probe_values': None, 'full_quartic_limit': None,
        'joint_group_limit': None}
    out = Path(__file__).with_name('probe-quartic-prefix-energy-certificate.json')
    out.write_text(json.dumps(certificate, indent=2)+'\n')
    print('Pinned axial identities: 6/6 PASS; full tensor traces: 2/2 PASS; failures: 0')
    print('L186 analytic Q_1 bound O(N^(5/2)); required O(N^3); no full-group limit certified')
    print(out)
