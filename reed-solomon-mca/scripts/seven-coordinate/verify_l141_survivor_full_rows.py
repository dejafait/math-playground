"""Independent replay via all eight original moments, without producer imports."""
from collections import Counter
from hashlib import sha256
from itertools import combinations, product
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
P = 97
S = [1, 8, 12, 18, 22, 27, 33]
H = sorted({pow(8, n, P) for n in range(16)})
J = [x for x in H if x not in S]


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def normalize(x):
    factor = pow(next(y for y in x if y), -1, P)
    return [y*factor % P for y in x]


def integer_det(matrix):
    """Exact Bareiss determinant, independent of modular row reduction."""
    a = [row[:] for row in matrix]
    n, sign, previous = len(a), 1, 1
    assert all(len(row) == n for row in a)
    for k in range(n-1):
        pivot = next((r for r in range(k, n) if a[r][k]), None)
        if pivot is None:
            return 0
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            sign = -sign
        current = a[k][k]
        for r in range(k+1, n):
            for c in range(k+1, n):
                numerator = a[r][c]*current-a[r][k]*a[k][c]
                assert numerator % previous == 0
                a[r][c] = numerator//previous
            a[r][k] = 0
        previous = current
    return sign*a[-1][-1]


def eliminate(matrix, witness=None):
    """Reverse column pivot order; return complete RREF and null basis."""
    a = [row[:] for row in matrix]
    m, n = len(a), len(a[0])
    transform = [[int(i == j) for j in range(m)] for i in range(m)]
    pivot_values = []
    pivots = []
    for c in reversed(range(n)):
        r = len(pivots)
        if r == m:
            break
        p = next((s for s in reversed(range(r, m)) if a[s][c]), None)
        if p is None:
            continue
        a[r], a[p] = a[p], a[r]
        transform[r], transform[p] = transform[p], transform[r]
        pivot_values.append(a[r][c])
        scale = pow(a[r][c], -1, P)
        a[r] = [v*scale % P for v in a[r]]
        transform[r] = [v*scale % P for v in transform[r]]
        for s in range(m):
            if s != r:
                scale = a[s][c]
                a[s] = [(v-scale*w) % P for v, w in zip(a[s], a[r])]
                transform[s] = [(v-scale*w) % P for v, w in zip(transform[s], transform[r])]
        pivots.append(c)
    free = [c for c in range(n) if c not in pivots]
    basis = []
    for c in free:
        vector = [0]*n
        vector[c] = 1
        for r, p in enumerate(pivots):
            vector[p] = -a[r][c] % P
        assert all(sum(x*y for x, y in zip(row, vector)) % P == 0 for row in matrix)
        basis.append(vector)
    assert all(not any(row) for row in a[len(pivots):])
    if witness is not None:
        assert all(pivot_values)
        assert [[sum(transform[i][j]*matrix[j][c] for j in range(m)) % P
                 for c in range(n)] for i in range(m)] == a
        assert [[a[r][c] for c in pivots] for r in range(len(pivots))] == [
            [int(i == j) for j in range(len(pivots))] for i in range(len(pivots))]
        assert [[b[c] for c in free] for b in basis] == [
            [int(i == j) for j in range(len(free))] for i in range(len(free))]
        witness.update(left_multiplier=transform, nonzero_pivot_values=pivot_values)
    return a, pivots, basis


def polynomial(k):
    out = [1]
    for root in J:
        if root in k:
            continue
        nxt = [0]*(len(out)+1)
        for d, value in enumerate(out):
            nxt[d] = (nxt[d]-root*value) % P
            nxt[d+1] = (nxt[d+1]+value) % P
        out = nxt
    assert len(out) == 8
    return out


def value(poly, x):
    v = 0
    for coefficient in reversed(poly):
        v = (v*x+coefficient) % P
    return v


def run():
    path = HERE/'l141-survivor-full-rows.json'
    target = HERE/'l141-survivor-full-rows-replay.json'
    out = {'method': 'All original eight-by-six moment matrices; independent reverse-pivot elimination',
           'planes': [], 'failures': [], 'unresolved': []}
    try:
        before = digest(path)
        cert = json.loads(path.read_bytes())
        assert not cert['failures'] and not cert['unresolved']
        assert cert['H'] == H and cert['S'] == S and cert['modulus'] == P
        assert cert['producer_sha256'] == digest(HERE/'l141_survivor_full_rows.py')
        assert cert['input_hashes_before'] == cert['input_hashes_after']
        for name, h in cert['input_hashes_before'].items():
            assert digest(HERE/name) == h
        out['input_hashes'] = cert['input_hashes_before']
        out['producer_certificate_sha256'] = before
        out['verifier_sha256'] = digest(Path(__file__))
        assert __debug__
        source = json.loads((HERE/'first-l140-mismatch-locus-gates.json').read_bytes())
        audit = json.loads((HERE/'l141-critical-audit.json').read_bytes())
        assert not source['failures'] and not audit['failures']
        assert len(audit['checks']) == 431 and all(c['passes'] for c in audit['checks'])
        assert all(r['returncode'] == 0 for r in audit['runs']) and len(audit['runs']) == 2
        assert audit['original_artifacts_byte_unchanged']
        assert digest(HERE/'audit_l141.py') == audit['audit_code_sha256']
        for name, h in audit['input_sha256'].items():
            assert digest(HERE/name) == h == cert['input_hashes_before'][name]
        assert source['source']['full_universe_indices'] == [199, 565]
        assert source['source']['pointer'] == '/cases/167'
        assert source['audited_mismatch_binding']['pointer'] == '/overlay/8'
        assert [s['passes_intrinsic_gates'] for s in source['points_and_all_row_gates']] == [False, True]
        old = source['points_and_all_row_gates'][1]
        assert old['u'] == [1, 0, 42, 90, 52, 62, 61]
        assert old['v'] == [0, 69, 60, 1, 72, 45, 80]
        assert len(cert['planes']) == 1 and cert['planes'][0]['historical_indices'] == [[199, 565]]
        universe = [(list(i), list(k)) for i, k in product(combinations(S, 2), combinations(J, 2))]
        assert len(universe) == 756 and len(set(tuple(i+k) for i, k in universe)) == 756
        for rec in cert['planes']:
            u, v = rec['u'], rec['v']
            assert len(u) == len(v) == 7
            assert any((u[a]*v[b]-u[b]*v[a]) % P for a, b in combinations(range(7), 2))
            assert old['u'] == u and old['v'] == v
            assert len(rec['rows']) == 756
            replay = {'historical_indices': rec['historical_indices'], 'rows': []}
            out['planes'].append(replay)
            groups = {}
            for n, (i, k) in enumerate(universe):
                row = rec['rows'][n]
                assert row['row_index'] == n and row['I'] == i and row['K'] == k
                support = i+k
                matrix = [[sum(u[j]*pow(x, d, P) for j, x in enumerate(S)) % P,
                           sum(v[j]*pow(x, d, P) for j, x in enumerate(S)) % P]
                          +[-pow(x, d, P) % P for x in support] for d in range(1, 9)]
                witness = {}
                rref, pivots, kernel = eliminate(matrix, witness)
                determinant = integer_det(witness['left_multiplier'])
                assert determinant % P
                witness['left_multiplier_integer_determinant'] = determinant
                witness['left_multiplier_determinant_residue'] = determinant % P
                rank = len(pivots)
                assert rank in [4, 5, 6]
                # Four error columns have rank four; no pure-error kernel is possible.
                assert len(eliminate([r[2:] for r in matrix])[1]) == 4
                error_minor = [r[2:] for r in matrix[:4]]
                assert integer_det(error_minor) % P
                witness['error_minor_first_four_moment_rows'] = error_minor
                witness['error_minor_integer_determinant'] = integer_det(error_minor)
                assert all(any(b[:2]) for b in kernel)
                poly = polynomial(k)
                g = [value(poly, x) for x in H]
                assert g == row['g_values_on_H'] and len(g) == 16
                assert all(value(poly, x) for x in S+k)
                observed = [x for x in S if x not in i]
                z = observed[0]
                q = [[((value(poly, z) if y == x else 0)-(value(poly, x) if y == z else 0)) % P
                      for y in S] for x in observed[1:]]
                qu = [sum(x*y for x, y in zip(c, u)) % P for c in q]
                qv = [sum(x*y for x, y in zip(c, v)) % P for c in q]
                minors = [(qu[a]*qv[b]-qu[b]*qv[a]) % P for a, b in combinations(range(4), 2)]
                qr = len(eliminate([[x, y] for x, y in zip(qu, qv)])[1])
                assert qr == rank-4 == row['projection_rank']
                assert row['Q'] == q and row['z'] == z
                assert row['Q_u'] == qu and row['Q_v'] == qv and row['projection_minors'] == minors
                evidence = {'row_index': n, 'I': i, 'K': k, 'moment_matrix': matrix,
                            'moment_rref': rref, 'pivot_columns': pivots,
                            'moment_rank': rank, 'complete_null_basis': kernel, **witness}
                replay['rows'].append(evidence)
                if rank == 6:
                    assert not kernel and any(minors) and row['status'] == 'rank_two_no_intersection'
                    continue
                # The actual census must retain any rank-zero branch as a separate obstruction.
                if rank == 4:
                    assert row['status'] == 'rank_zero_whole_plane_nonpersistent_obstruction'
                    out['unresolved'].append({'indices': rec['historical_indices'], 'row_index': n,
                                              'reason': 'Unexpected rank-zero branch needs full coefficient replay'})
                    continue
                assert len(kernel) == 1 and not any(minors)
                gate = row['recovery']
                alpha, beta = gate['direction_coefficients']
                assert len(gate['direction_coefficients']) == 2 and (alpha or beta)
                assert normalize(kernel[0][:2]) == gate['normalized_direction'] == normalize([alpha, beta])
                scale = next(kernel[0][j]*pow(gate['direction_coefficients'][j], -1, P) % P
                             for j in range(2) if gate['direction_coefficients'][j])
                assert scale and kernel[0] == [x*scale % P for x in [alpha, beta]+gate['error_weights']]
                assert len(gate['error_weights']) == 4
                h = [(alpha*x+beta*y) % P for x, y in zip(u, v)]
                lam = h[S.index(z)]*pow(value(poly, z), -1, P) % P
                e = dict(zip(support, gate['error_weights']))
                identity = [((h[S.index(x)] if x in S else 0)-e.get(x, 0)-lam*value(poly, x)) % P for x in H]
                moments = [sum(((h[S.index(x)] if x in S else 0)-e.get(x, 0))*pow(x, d, P)
                               for x in H) % P for d in range(1, 9)]
                assert len(gate['identity_residuals']) == 16 and len(gate['shifted_moment_residuals']) == 8
                assert not any(identity+moments)
                assert h == gate['h'] and lam == gate['lambda_value']
                assert identity == gate['identity_residuals'] and moments == gate['shifted_moment_residuals']
                failed = (['lambda_zero'] if lam == 0 else [])+[
                    f'overlap_weight_zero_at_{x}' for x in i if e[x] == 0]
                assert failed == gate['failed_gates'] and gate['passes_intrinsic'] == (not failed)
                assert gate['prescribed_finite_gate'] == {'D_coefficient': alpha, 'C_coefficient': -beta % P}
                piv = next(j for j in range(4) if qu[j] or qv[j])
                assert row['projection_pivot'] == piv and [alpha, beta] == [-qv[piv] % P, qu[piv]]
                all_pivots = []
                for j in range(4):
                    if qu[j] or qv[j]:
                        d = [-qv[j] % P, qu[j]]
                        assert normalize(d) == gate['normalized_direction']
                        factor = next(d[c]*pow(gate['direction_coefficients'][c], -1, P) % P
                                      for c in range(2) if gate['direction_coefficients'][c])
                        assert factor and d == [factor*x % P for x in [alpha, beta]]
                        hh = [(d[0]*x+d[1]*y) % P for x, y in zip(u, v)]
                        ll = hh[S.index(z)]*pow(value(poly, z), -1, P) % P
                        ee = [(hh[S.index(x)]-ll*value(poly, x)) % P if x in S
                              else -ll*value(poly, x) % P for x in support]
                        assert ll == factor*lam % P and ee == [factor*e[x] % P for x in support]
                        all_pivots.append({'component': j, 'scale': factor, 'direction': d,
                                           'lambda_value': ll, 'error_weights': ee})
                evidence['all_nonzero_projection_pivots'] = all_pivots
                # Reconstruct the same plane at every nonzero exterior pivot.
                exterior = [[(u[a]*v[b]-u[b]*v[a]) % P for b in range(7)] for a in range(7)]
                exterior_pivots = []
                for a, b in combinations(range(7), 2):
                    pivot_value = exterior[a][b]
                    if not pivot_value:
                        continue
                    uu = [exterior[x][b]*pow(pivot_value, -1, P) % P for x in range(7)]
                    vv = exterior[a][:]
                    assert [[(uu[x]*vv[y]-uu[y]*vv[x]) % P for y in range(7)]
                            for x in range(7)] == exterior
                    first = [sum(c*x for c, x in zip(rowq, uu)) % P for rowq in q]
                    second = [sum(c*x for c, x in zip(rowq, vv)) % P for rowq in q]
                    for component in range(4):
                        if not (first[component] or second[component]):
                            continue
                        direction = [-second[component] % P, first[component]]
                        hh = [(direction[0]*x+direction[1]*y) % P for x, y in zip(uu, vv)]
                        coordinate = next(x for x in range(7) if h[x])
                        factor = hh[coordinate]*pow(h[coordinate], -1, P) % P
                        assert factor and hh == [factor*x % P for x in h]
                        ll = hh[S.index(z)]*pow(value(poly, z), -1, P) % P
                        ee = [(hh[S.index(x)]-ll*value(poly, x)) % P if x in S
                              else -ll*value(poly, x) % P for x in support]
                        assert ll == factor*lam % P and ee == [factor*e[x] % P for x in support]
                        exterior_pivots.append({'pivot': [a, b], 'nonzero_value': pivot_value,
                            'u': uu, 'v': vv, 'projection_component': component,
                            'direction': direction, 'h': hh, 'scale': factor,
                            'lambda_value': ll, 'error_weights': ee})
                evidence['all_exterior_and_projection_pivot_recoveries'] = exterior_pivots
                evidence['normalized_full_solution'] = normalize(kernel[0])
                if failed:
                    assert row['status'] == 'rank_one_failed_weight_gates'
                else:
                    assert all(e.values()) and row['status'] == 'intrinsic_success'
                    groups.setdefault(tuple(gate['normalized_direction']), []).append(n)
            direction_groups = [{'direction': list(d), 'row_indices': rows} for d, rows in sorted(groups.items())]
            duplicates = [g for g in direction_groups if len(g['row_indices']) > 1]
            assert direction_groups == rec['direction_groups'] and duplicates == rec['duplicate_direction_groups']
            summary = {'covered_rows': len(rec['rows']), 'required_rows': 756,
                       'projection_rank_counts': dict(Counter(str(r['projection_rank']) for r in rec['rows'])),
                       'status_counts': dict(Counter(r['status'] for r in rec['rows'])),
                       'failed_gate_counts': dict(Counter(f for r in rec['rows'] if 'recovery' in r
                                                         for f in r['recovery']['failed_gates'])),
                       'full_rows': sum(len(g['row_indices']) for g in direction_groups),
                       'distinct_directions_before_chart': len(groups), 'required_distinct_directions': 12,
                       'duplicate_direction_groups': len(duplicates), 'shortfall': max(0, 12-len(groups)),
                       'rank_zero_obstruction': any(r['projection_rank'] == 0 for r in rec['rows'])}
            assert summary == rec['summary']
            assert rec['disposition'] == ('excluded_necessary_shortfall' if len(groups) < 12 else 'complete_residual_saved')
            replay['summary'] = summary
            replay['moment_rank_counts'] = dict(Counter(r['moment_rank'] for r in replay['rows']))
            replay['direction_groups'] = direction_groups
        assert not out['unresolved'] and digest(path) == before
        assert all(digest(HERE/name) == h for name, h in out['input_hashes'].items())
    except Exception as exc:
        out['failures'].append({'type': type(exc).__name__, 'message': str(exc)})
        raise
    finally:
        target.write_text(json.dumps(out, separators=(',', ':'))+'\n')
        for rec in out['planes']:
            print(json.dumps({'indices': rec['historical_indices'], 'moment_rank_counts': rec.get('moment_rank_counts'),
                              **rec.get('summary', {})}, sort_keys=True))
        print(f"Failures {len(out['failures'])}; unresolved {len(out['unresolved'])}; complete replay {target}")


if __name__ == '__main__':
    run()
