"""Independent formula replay of the one approved L125 residual locus; imports no producer.

Run: python3 scripts/seven-coordinate/verify_second_unmatched_locus_gates.py
"""
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
P = 97
S = [1, 8, 12, 18, 22, 27, 33]
H = sorted({pow(8, j, P) for j in range(16)})
J = sorted(set(H)-set(S))
ROWS = [([1, 8], [47, 50]), ([12, 18], [64, 75]),
        ([1, 18], [70, 79]), ([12, 33], [89, 96])]
PAIRS = list(combinations(range(7), 2))


def dot(a, b):
    return sum(x*y for x, y in zip(a, b)) % P


def derivative_g(k, x):
    denom = 1
    for y in S+k:
        if x != y:
            denom = denom*(x-y) % P
    return 16*pow(x, 15, P)*pow(denom, -1, P) % P


def rational_det(matrix):
    a = [[Fraction(x) for x in row] for row in matrix]
    det = Fraction(1)
    for c in range(len(a)):
        n = next(n for n in range(c, len(a)) if a[n][c])
        if n != c:
            a[c], a[n] = a[n], a[c]
            det = -det
        pivot = a[c][c]
        det *= pivot
        for n in range(c+1, len(a)):
            scale = a[n][c]/pivot
            a[n] = [x-scale*y for x, y in zip(a[n], a[c])]
    assert det.denominator == 1
    return det.numerator


def column_kernel(matrix):
    """Eliminate columns, tracking exact relations among original columns."""
    echelon, pivots, basis = {}, [], []
    for c, column in enumerate(zip(*matrix)):
        v, relation = list(column), [int(i == c) for i in range(21)]
        for r in sorted(echelon):
            scale = v[r]
            if scale:
                saved, coefficients = echelon[r]
                v = [(a-scale*b) % P for a, b in zip(v, saved)]
                relation = [(a-scale*b) % P for a, b in zip(relation, coefficients)]
        r = next((i for i, x in enumerate(v) if x), None)
        if r is None:
            basis.append(relation)
        else:
            inverse = pow(v[r], -1, P)
            echelon[r] = ([inverse*x % P for x in v],
                          [inverse*x % P for x in relation])
            pivots.append(c)
    return pivots, basis


def run():
    path = HERE/'second-unmatched-locus-gates.json'
    raw = path.read_bytes()
    cert = json.loads(raw)
    assert cert['modulus'] == P and cert['H'] == H and cert['S'] == S and cert['J'] == J
    assert cert['rows'] == [{'I': i, 'K': k} for i, k in ROWS]
    assert cert['column_pairs'] == [[S[a], S[b]] for a, b in PAIRS]
    source_raw = (HERE/cert['source']['path']).read_bytes()
    assert sha256(source_raw).hexdigest() == cert['source']['sha256']
    shard = json.loads(source_raw)
    assert shard['third_index'] == 94 and 539 in shard['residual_indices']
    records = [r for r in shard['cases'] if r['fourth_index'] == 539]
    assert len(records) == 1 and records[0]['status'] == 'residual'
    assert records[0] == shard['cases'][155]
    assert cert['source']['pointer'] == '/cases/155'
    assert cert['source']['full_universe_indices'] == [94,539]
    source = records[0]
    universe = [(list(i), list(k)) for i in combinations(S, 2) for k in combinations(J, 2)]
    assert universe[94] == ROWS[2] and universe[539] == ROWS[3]
    supports = [set(i+k) for i,k in ROWS]
    assert len({tuple(sorted(x)) for x in supports}) == 4
    assert all(len(a & b) <= 1 for a,b in combinations(supports,2))
    assert len(cert['blocks']) == 4
    qs, matrix, gs = [], [], []
    for (i, k), saved in zip(ROWS, cert['blocks']):
        g = {x: derivative_g(k, x) for x in S+k}
        assert all(g.values())
        gs.append(g)
        o = sorted(set(S)-set(i))
        z = o[0]
        # Independent normalized ratio quotient; scale back to the
        # original c_x, then verify all original exterior entries.
        q = []
        for x in o[1:]:
            ratio = [(int(y == x)*pow(g[x], -1, P)
                      -int(y == z)*pow(g[z], -1, P)) % P for y in S]
            q.append([v*g[z]*g[x] % P for v in ratio])
        block = [[(r[a]*s[b]-r[b]*s[a]) % P for a, b in PAIRS]
                 for r, s in combinations(q, 2)]
        assert saved == {'I': i, 'K': k, 'pivot': z, 'covectors': q, 'matrix': block}
        qs.append(q)
        matrix += block
    assert matrix == cert['original_matrix']
    basis = [[0,1]+[0]*19, [0,0,15,0,0,0,0,84,0,0,0,31,0,0,0,63,62,1,0,0,0]]
    assert basis == cert['kernel_basis'] == source['kernel_basis']
    columns, rebuilt_basis = column_kernel(matrix)
    assert len(columns) == 19 and rebuilt_basis == basis
    assert [[b[c] for c in (1, 17)] for b in basis] == [[1, 0], [0, 1]]
    assert cert['free_columns'] == [1, 17]
    residuals = [[dot(v, row) for row in matrix] for v in basis]
    assert residuals == cert['kernel_residuals'] and not any(map(any, residuals))
    assert len(cert['rank_minor_rows']) == len(set(cert['rank_minor_rows'])) == 19
    assert cert['rank_minor_columns'] == [c for c in range(21) if c not in (1, 17)]
    assert cert['rank_minor_columns'] == source['pivot_columns']
    assert cert['rank_minor_rows'] == source['minor_rows']
    assert residuals == source['kernel_residuals']
    minor = [[matrix[r][c] for c in cert['rank_minor_columns']] for r in cert['rank_minor_rows']]
    integer_det = rational_det(minor)
    assert minor == cert['rank_minor'] and integer_det == cert['rank_minor_integer_determinant']
    assert integer_det % P == cert['rank_minor_residue'] == 23
    assert cert['rank_minor_residue'] == source['minor_residue']
    # Rank >=19 by the minor, <=19 by two independent null vectors;
    # these identities persist under any scalar extension.
    quadrics, quads = [], []
    for a, b, c, d in combinations(range(7), 4):
        q = [0, 0, 0]
        for sign, ij, kl in [(1, (a, b), (c, d)), (-1, (a, c), (b, d)), (1, (a, d), (b, c))]:
            n, m = PAIRS.index(ij), PAIRS.index(kl)
            for u in range(2):
                for v in range(2):
                    q[u+v] = (q[u+v]+sign*basis[u][n]*basis[v][m]) % P
        quadrics.append(q)
        quads.append([S[x] for x in [a, b, c, d]])
    assert quadrics == cert['plucker_coefficients_s2_st_t2']
    assert quads == cert['plucker_quadruples']
    nonzero = [n for n, q in enumerate(quadrics) if any(q)]
    assert nonzero == cert['nonzero_plucker_indices']
    expected = {(1,8,12,18):13, (1,12,18,22):63, (1,12,18,27):62, (1,12,18,33):1}
    assert {tuple(quads[n]):quadrics[n] for n in nonzero} == {k:[0,v,0] for k,v in expected.items()}
    assert all(q == [0,0,0] for n,q in enumerate(quadrics) if n not in nonzero)
    assert cert['affine_gcd'] == [0, 1]
    assert len(cert['affine_quotients']) == len(cert['bezout_coefficients']) == 35
    total = [0]*3
    for q, quotient, bezout in zip(quadrics, cert['affine_quotients'], cert['bezout_coefficients']):
        assert quotient == ([q[1]] if q[1] else [])
        assert len(bezout) <= 1
        if bezout:
            total = [(x+bezout[0]*y) % P for x, y in zip(total, q)]
    assert total == [0, 1, 0]
    assert all(q[0] == q[2] == 0 for q in quadrics)
    assert any(q[1] for q in quadrics)
    assert cert['complete_projective_parameter_locus'] == [[1, 0], [0, 1]]
    assert len(cert['points_and_all_row_gates']) == 2
    replay, pivot_replay = [], []
    for point_index, (bivector, point) in enumerate(zip(basis, cert['points_and_all_row_gates'])):
        a, b = [(0, 2), (0, 3)][point_index]
        u = ([1,0,0,0,0,0,0] if point_index == 0 else [1,25,15,0,54,67,84])
        v = ([0,0,1,0,0,0,0] if point_index == 0 else [0,0,0,15,0,0,0])
        assert point['u'] == u and point['v'] == v and point['pivot_indices'] == [a, b]
        assert point['bivector'] == bivector
        assert [(u[x]*v[y]-u[y]*v[x]) % P for x, y in PAIRS] == bivector
        assert len(point['row_gates']) == 4
        for j, ((i, k), q, g, gate) in enumerate(zip(ROWS, qs, gs, point['row_gates'])):
            qu, qv = [[dot(row, w) for row in q] for w in (u, v)]
            minors = [(qu[x]*qv[y]-qu[y]*qv[x]) % P for x, y in combinations(range(4), 2)]
            assert not any(minors) and any(qu+qv)
            assert gate['Q_u'] == qu and gate['Q_v'] == qv and gate['projection_minors'] == minors
            assert gate['projection_rank'] == 1
            n = next(n for n in range(4) if qu[n] or qv[n])
            alpha, beta = -qv[n] % P, qu[n]
            h = [(alpha*x+beta*y) % P for x, y in zip(u, v)]
            assert any(h) and all(dot(row, h) == 0 for row in q)
            assert [alpha, beta] == gate['direction_coefficients'] and h == gate['intersection_vector']
            z = min(set(S)-set(i))
            lam = h[S.index(z)]*pow(g[z], -1, P) % P
            error = {x: (h[S.index(x)]-lam*g[x]) % P for x in i}
            error.update({x: -lam*g[x] % P for x in k})
            assert lam == gate['lambda_value']
            # Every lambda and weight is independently reconstructed here;
            assert [error[x] for x in i] == gate['overlap_weights']
            assert [error[x] for x in i+k] == gate['error_weights']
            assert list(error.values()).count(0) == (3 if lam == 0 else 0)
            assert gate['g_values_on_S_union_K'] == {str(x): g[x] for x in S+k}
            values = [((h[S.index(x)] if x in S else 0)-error.get(x, 0)) % P for x in H]
            moments = [sum(y*pow(x, d, P) for x, y in zip(H, values)) % P for d in range(1, 9)]
            identity = [(y-lam*derivative_g(k, x)) % P if x in S+k else y
                        for x, y in zip(H, values)]
            assert identity == gate['h_minus_error_minus_lambda_g_on_H'] and not any(identity)
            assert moments == gate['moment_residuals'] and not any(moments)
            failed = (['lambda_zero'] if not lam else [])+[f'overlap_weight_zero_at_{x}' for x in i if not error[x]]
            assert gate['failed_gates'] == failed and gate['passes'] == (not failed)
            assert gate['prescribed_finite_gate'] == {'D_coefficient': alpha, 'C_coefficient': -beta % P}
            assert gate['original_basis_convention'] == 'u_original=A*u+B*v; v_original=C*u+D*v; AD-BC!=0'
            assert gate['original_first_coefficient'] == '(D*alpha-C*beta)/(AD-BC)'
            replay.append({'point_index': point_index, 'row_number': j+1, 'Q_u': qu, 'Q_v': qv,
                           'h': h, 'lambda': lam, 'error': error, 'moments': moments,
                           'finite_gate_coefficients_D_C': [alpha, -beta % P]})
        assert not point['passes_intrinsic_gates']
        # Exhaust every nonzero exterior pivot and every nonzero projection
        # component. Coefficient identities persist over scalar extensions.
        alternating = [[0]*7 for _ in range(7)]
        for (x, y), value in zip(PAIRS, bivector):
            alternating[x][y], alternating[y][x] = value, -value % P
        for (a, b), value in zip(PAIRS, bivector):
            if not value:
                continue
            uu = [alternating[x][b]*pow(value, -1, P) % P for x in range(7)]
            vv = alternating[a]
            assert [(uu[x]*vv[y]-uu[y]*vv[x]) % P for x, y in PAIRS] == bivector
            for j, ((i, k), q, g, gate) in enumerate(zip(ROWS, qs, gs, point['row_gates'])):
                qu, qv = [[dot(row, w) for row in q] for w in (uu, vv)]
                assert any(qu+qv)
                assert all((qu[x]*qv[y]-qu[y]*qv[x]) % P == 0
                           for x, y in combinations(range(4), 2))
                canonical_h = gate['intersection_vector']
                ix = next(x for x, value in enumerate(canonical_h) if value)
                for n in range(4):
                    if not (qu[n] or qv[n]):
                        continue
                    aa, bb = -qv[n] % P, qu[n]
                    hh = [(aa*x+bb*y) % P for x, y in zip(uu, vv)]
                    scalar = hh[ix]*pow(canonical_h[ix], -1, P) % P
                    assert scalar and hh == [scalar*x % P for x in canonical_h]
                    z = min(set(S)-set(i))
                    lam = hh[S.index(z)]*pow(g[z], -1, P) % P
                    weights = [(hh[S.index(x)]-lam*g[x]) % P for x in i]+[-lam*g[x] % P for x in k]
                    assert lam == scalar*gate['lambda_value'] % P
                    assert weights == [scalar*x % P for x in gate['error_weights']]
                    pivot_replay.append(dict(point=point_index, exterior_pivot=[a,b], row=j+1,
                                             projection_component=n, direction=[aa,bb],
                                             scalar=scalar, h=hh, lambda_value=lam, error_weights=weights))
    assert cert['failures'] == []
    out = {'certificate_sha256': sha256(raw).hexdigest(), 'rank_minor_integer_determinant': integer_det,
           'rebuilt_original_matrix': matrix, 'kernel_residuals': residuals,
           'plucker_coefficients_s2_st_t2': quadrics, 'all_row_replay': replay, 'all_pivot_replay': pivot_replay,
           'summary': {'matrix_entries_compared': 504, 'rank': 19, 'complete_kernel_vectors': 2,
                       'plucker_equations': 35, 'complete_points': 2, 'row_gates_replayed': 8,
                       'nonzero_exterior_pivots': sum(sum(bool(x) for x in b) for b in basis),
                       'all_projection_pivot_checks': len(pivot_replay),
                       'lambda_zero_rows': 6, 'full_weight_rows': 2, 'moment_residuals': 64, 'pointwise_entries': 128},
           'failures': [], 'limitations': 'Same-step replay shares Python and residue field; separate critical audit pending.'}
    target = HERE/'second-unmatched-locus-gates-replay.json'
    target.write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps(out['summary'], sort_keys=True))
    print(f'Excluded loci 1/1; all extension branches covered by st=0; failures 0; replay: {target}')


if __name__ == '__main__':
    run()
