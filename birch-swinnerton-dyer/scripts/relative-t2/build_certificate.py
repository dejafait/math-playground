#!/usr/bin/env python3
"""Exact instance certificate. No external databases or numerical arithmetic.

Sources, hypotheses and proof interpretation are in L030 (if completed)
and drafts/2026-10-07-concrete-relative-t2-attempt.md. Run from notebook root.
"""
import json
from fractions import Fraction as Q
from math import gcd, isqrt, prod
from pathlib import Path

OUT = Path('scripts/relative-t2/certificate.json')


def identity(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def rowop(a, op):
    typ, i, j, *tail = op
    if typ == 'swap':
        a[i], a[j] = a[j], a[i]
    elif typ == 'add':
        t = tail[0]
        a[i] = [x + t*y for x, y in zip(a[i], a[j])]
    else:
        assert typ == 'neg' and i == j
        a[i] = [-x for x in a[i]]


def colop(a, op):
    typ, i, j, *tail = op
    for r in a:
        if typ == 'swap':
            r[i], r[j] = r[j], r[i]
        elif typ == 'add':
            r[i] += tail[0]*r[j]
        else:
            assert typ == 'neg' and i == j
            r[i] = -r[i]


def inverse_op(op):
    return op[:3] + [-op[3]] if op[0] == 'add' else op


def diagonalize(rels):
    """Integral equivalence, not necessarily divisibility-ordered Smith form."""
    a = [r[:] for r in rels]
    n, m = len(a), len(a[0])
    rops, cops = [], []

    def rr(op):
        rowop(a, op)
        rops.append(op)

    def cc(op):
        colop(a, op)
        cops.append(op)

    k = 0
    while k < min(n, m):
        chosen = None
        for i in range(k, n):
            for j in range(k, m):
                if a[i][j] and (chosen is None or abs(a[i][j]) < chosen[0]):
                    chosen = (abs(a[i][j]), i, j)
                    if chosen[0] == 1:
                        break
            if chosen and chosen[0] == 1:
                break
        if chosen is None:
            break
        _, i, j = chosen
        if i != k:
            rr(['swap', k, i])
        if j != k:
            cc(['swap', k, j])
        while True:
            restarted = False
            for i in range(k+1, n):
                if a[i][k]:
                    q = a[i][k] // a[k][k]
                    if q:
                        rr(['add', i, k, -q])
                    if a[i][k]:
                        rr(['swap', k, i])
                        restarted = True
                        break
            if restarted:
                continue
            for j in range(k+1, m):
                if a[k][j]:
                    q = a[k][j] // a[k][k]
                    if q:
                        cc(['add', j, k, -q])
                    if a[k][j]:
                        cc(['swap', k, j])
                        restarted = True
                        break
            if restarted:
                continue
            break
        if a[k][k] < 0:
            rr(['neg', k, k])
        k += 1
        if k % 100 == 0:
            print('integral pivots', k, flush=True)
    assert all(a[i][j] == (a[i][i] if i == j and i < k else 0)
               for i in range(n) for j in range(m))
    c = identity(m)
    for op in cops:
        colop(c, op)
    ci = identity(m)
    for op in reversed(cops):
        colop(ci, inverse_op(op))
    return k, [a[i][i] for i in range(k)], rops, cops, c, ci


def matmul(a, b):
    cols = list(zip(*b))
    return [[sum(x*y for x, y in zip(r, c) if x and y) for c in cols] for r in a]


def reduce_rational(a):
    """RREF with a complete reversible elementary-row-operation log."""
    a = [[Q(x) for x in r] for r in a]
    ops, pivots = [], []
    k = 0
    for j in range(len(a[0])):
        i = next((i for i in range(k, len(a)) if a[i][j]), None)
        if i is None:
            continue
        if i != k:
            a[i], a[k] = a[k], a[i]
            ops.append(['swap', k, i])
        t = 1/a[k][j]
        if t != 1:
            a[k] = [t*x for x in a[k]]
            ops.append(['scale', k, str(t)])
        for i in range(len(a)):
            t = -a[i][j]
            if i != k and t:
                a[i] = [x+t*y for x, y in zip(a[i], a[k])]
                ops.append(['add', i, k, str(t)])
        pivots.append(j)
        k += 1
        if k == len(a):
            break
    free = [j for j in range(len(a[0])) if j not in pivots]
    kernel = []
    for j in free:
        v = [Q(0)]*len(a[0])
        v[j] = Q(1)
        for i, p in enumerate(pivots):
            v[p] = -a[i][j]
        kernel.append(v)
    return a, pivots, kernel, ops


def qjson(x):
    if isinstance(x, Q):
        return str(x)
    if isinstance(x, list):
        return [qjson(y) for y in x]
    if isinstance(x, dict):
        return {k: qjson(v) for k, v in x.items()}
    return x


def build():
    # Generalized Weierstrass invariants, recomputed from the input.
    a1, a2, a3, a4, a6 = model = [0, 1, 1, -2, 0]
    b2 = a1*a1+4*a2
    b4 = 2*a4+a1*a3
    b6 = a3*a3+4*a6
    b8 = a1*a1*a6+4*a2*a6-a1*a3*a4+a2*a3*a3-a4*a4
    c4 = b2*b2-24*b4
    c6 = -b2**3+36*b2*b4-216*b6
    delta = -b2*b2*b8-8*b4**3-27*b6*b6+9*b2*b4*b6
    assert c4**3-c6*c6 == 1728*delta
    trial = [[d, delta % d] for d in range(2, isqrt(delta)+1)]
    assert delta > 1 and all(r for _, r in trial)
    # Delta is prime with valuation one, so model is minimal everywhere;
    # c4 is prime to Delta, so the sole bad prime is multiplicative.
    assert gcd(c4, delta) == 1
    n = delta
    points = [[x, y] for x in range(2) for y in range(2)
              if (y*y+a1*x*y+a3*y-x**3-a2*x*x-a4*x-a6) % 2 == 0]
    table = [[x, y, (y*y+a1*x*y+a3*y-x**3-a2*x*x-a4*x-a6) % 2]
             for x in range(2) for y in range(2)]
    eigenvalue = 3-(1+len(points))
    arithmetic = {'model': model, 'b': [b2, b4, b6, b8], 'c4': c4,
                  'c6': c6, 'discriminant': delta, 'primality_trial': trial,
                  'j': Q(c4**3, delta), 'conductor': n,
                  'F2_table': table, 'F2_affine_points': points,
                  'F2_infinity_count': 1, 'a2': eigenvalue}
    assert delta % 2 and Q(c4**3, delta).denominator > 1

    # Prime-level P^1: (1,t) and (0,1). Lift maps 0 -> -1/t,
    # infinity -> 0; identity is the last lift. All determinants are one.
    projective = [[1, t] for t in range(n)] + [[0, 1]]
    lifts = [[0, -1, 1, t] for t in range(n)] + [[1, 0, 0, 1]]
    s = len(projective)

    def index(c, d):
        c, d = c % n, d % n
        assert c or d
        return d*pow(c, -1, n) % n if c else n

    relations, permutations = [], []
    for c, d in projective:
        si = index(d, -c)
        ui = index(d, -c-d)
        uui = index(-c-d, c)
        permutations.append([si, ui, uui])
    for i, (si, ui, uui) in enumerate(permutations):
        r = [0]*s
        for j in [i, si]:
            r[j] += 1
        relations.append(r)
        r = [0]*s
        for j in [i, ui, uui]:
            r[j] += 1
        relations.append(r)
    rank, diagonal, rops, cops, c, ci = diagonalize(relations)
    d = s-rank
    coords = [r[rank:] for r in c]
    basis_lifts = ci[rank:]
    saturated_basis = ci[:rank]
    assert matmul(c, ci) == identity(s)
    assert matmul(relations, coords) == [[0]*d for _ in relations]
    assert matmul(basis_lifts, coords) == identity(d)
    print('relative dimension', d, 'relation rank', rank,
          'torsion diagonal', [x for x in diagonal if x != 1], flush=True)

    def cusp(p, q):
        if q == 0:
            assert p
            return [1, 0]
        g = gcd(p, q)
        p, q = p//g, q//g
        return [-p, -q] if q < 0 else [p, q]

    def chain(target):
        p, q = target
        if q == 0:
            return {'target': target, 'continued_fraction': [], 'segments': []}
        terms = []
        aa, bb = p, q
        while bb:
            a = aa//bb
            terms.append(a)
            aa, bb = bb, aa-a*bb
        pm2, qm2, pm1, qm1 = 0, 1, 1, 0
        segments = []
        for a in terms:
            pp, qq = a*pm1+pm2, a*qm1+qm2
            det = pp*qm1-pm1*qq
            assert abs(det) == 1
            # columns next, previous; negate next column if necessary.
            lift = [det*pp, pm1, det*qq, qm1]
            ii = index(lift[2], lift[3])
            ha, hb, hc, hd = lifts[ii]
            la, lb, lc, ld = lift
            gamma = [la*hd-lb*hc, -la*hb+lb*ha,
                     lc*hd-ld*hc, -lc*hb+ld*ha]
            assert gamma[2] % n == 0
            segments.append({'start': cusp(pm1, qm1), 'end': cusp(pp, qq),
                             'lift': lift, 'coset': ii,
                             'Gamma0_reduction': gamma})
            pm2, qm2, pm1, qm1 = pm1, qm1, pp, qq
        assert cusp(pm1, qm1) == target
        return {'target': target, 'continued_fraction': terms, 'segments': segments}

    def path(start, end):
        ca, cb = chain(start), chain(end)
        raw = [0]*s
        for sign, ch in [(-1, ca), (1, cb)]:
            for seg in ch['segments']:
                raw[seg['coset']] += sign
        quotient = [sum(raw[i]*coords[i][j] for i in range(s) if raw[i])
                    for j in range(d)]
        return {'start': start, 'end': end, 'start_chain': ca,
                'end_chain': cb, 'raw': raw, 'coordinates': quotient}

    def transform(pt, matrix):
        p, q = pt
        a, b, c, d = matrix
        return cusp(a*p+b*q, c*p+d*q)

    endpoints = [[cusp(b, dd), cusp(a, cc)] for a, b, cc, dd in lifts]
    op_matrices = {'J': [[-1, 0, 0, 1]],
                   'H2': [[2, 0, 0, 1], [1, 0, 0, 2], [1, 1, 0, 2]]}
    paths, images, matrices, relation_images = {}, {}, {}, {}
    # Check each generator's original endpoints as well as operator images.
    basepaths = [path(a, b) for a, b in endpoints]
    assert [p['coordinates'] for p in basepaths] == coords
    for name, mm in op_matrices.items():
        paths[name] = [[path(transform(a, m), transform(b, m)) for m in mm]
                       for a, b in endpoints]
        img = [[sum(p['coordinates'][j] for p in terms) for j in range(d)]
               for terms in paths[name]]
        images[name] = img
        relation_images[name] = matmul(relations, img)
        assert relation_images[name] == [[0]*d for _ in relations]
        # Rows describe images of the basis; transpose for column convention.
        basis_img = matmul(basis_lifts, img)
        matrices[name] = [list(x) for x in zip(*basis_img)]
        assert matmul(coords, basis_img) == img
    j, h = matrices['J'], matrices['H2']
    assert matmul(j, j) == identity(d)
    assert matmul(j, h) == matmul(h, j)
    dual = [[j[col][row]-int(row == col) for col in range(d)]
            for row in range(d)]
    dual += [[h[col][row]-eigenvalue*int(row == col) for col in range(d)]
             for row in range(d)]
    reduced, pivots, kernel, ops = reduce_rational(dual)
    assert all(all(sum(x*y for x, y in zip(r, v)) == 0 for r in dual)
               for v in kernel)
    dim = len(kernel)
    cert = {'arithmetic': arithmetic, 'projective_cosets': projective,
            'SL2_lifts': lifts, 'permutations_S_U_U2': permutations,
            'relations': relations,
            'presentation': {'rank': rank, 'dimension': d, 'diagonal': diagonal,
                             'row_operations': rops, 'column_operations': cops,
                             'column_transform': c, 'inverse_column_transform': ci,
                             'saturated_relation_basis': saturated_basis,
                             'saturation_index': prod(diagonal),
                             'integral_generator_coordinates': coords,
                             'integral_quotient_basis_lifts': basis_lifts,
                             'coordinate_denominator': 1},
            'basepaths': basepaths, 'operator_endpoint_matrices': op_matrices,
            'operator_paths': paths, 'operator_generator_images': images,
            'operator_relation_images': relation_images, 'matrices': matrices,
            'dual': {'B': dual, 'rref': reduced, 'pivots': pivots,
                     'kernel_basis': kernel, 'row_operations': ops,
                     'rank': len(pivots), 'dimension': dim,
                     'required_dimension': 1},
            'failures': [], 'result': 'THRESHOLD_MET' if dim == 1 else 'INCONCLUSIVE'}
    if dim == 1:
        cert['integration_line'] = {
            'basis_functional': kernel[0],
            'integral_generator_values':
                [sum(x*y for x, y in zip(row, kernel[0])) for row in coords],
            'scale_to_real_integration': 'NONZERO_REAL_UNCOMPUTED',
            'Neron_normalized_scale': 'NOT_CERTIFIED'}
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(qjson(cert), separators=(',', ':'))+'\n')
    print('B rank', len(pivots), 'actual kernel dimension', dim,
          'required', 1, 'failures', cert['failures'], 'certificate', OUT)


if __name__ == '__main__':
    build()
