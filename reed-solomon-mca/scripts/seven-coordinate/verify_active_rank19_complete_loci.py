"""Independent full-entry, homogeneous-factor and all-pivot replay.

Imports no producer or producer helpers. Uses polynomial/Horner quotient
construction, column elimination, and direct certificate identities.
"""
from collections import Counter
from hashlib import sha256
from itertools import combinations, product
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
P = 97
S = [1, 8, 12, 18, 22, 27, 33]
H = sorted({pow(8, n, P) for n in range(16)})
J = sorted(set(H)-set(S))
PAIRS = list(combinations(range(7), 2))
QUADS = list(combinations(range(7), 4))


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def add(a, b):
    out = [(a[n] if n < len(a) else 0)+(b[n] if n < len(b) else 0)
           for n in range(max(len(a), len(b)))]
    out = [x % P for x in out]
    while out and not out[-1]:
        out.pop()
    return out


def multiply(a, b):
    out = []
    for n, x in enumerate(a):
        out = add(out, [0]*n+[x*y % P for y in b])
    return out


def evaluate(poly, x):
    out = 0
    for a in reversed(poly):
        out = (x*out+a) % P
    return out


def dot(a, b):
    return sum(x*y for x, y in zip(a, b)) % P


def rank(matrix):
    # Eliminate column vectors with reverse coordinate pivots.
    basis = {}
    for v in zip(*matrix):
        v = list(v)
        for r in sorted(basis, reverse=True):
            multiple = v[r]
            v = [(x-multiple*y) % P for x, y in zip(v, basis[r])]
        r = next((r for r in reversed(range(len(v))) if v[r]), None)
        if r is not None:
            basis[r] = [x*pow(v[r], -1, P) % P for x in v]
    return len(basis)


def determinant(a):
    # Column operations with reverse column pivot search.
    a = [r[:] for r in a]
    answer = 1
    for r in range(len(a)):
        c = next(c for c in reversed(range(r, len(a))) if a[r][c])
        if c != r:
            for row in a:
                row[r], row[c] = row[c], row[r]
            answer = -answer
        value = a[r][r]
        answer = answer*value % P
        for c in range(r+1, len(a)):
            factor = a[r][c]*pow(value, -1, P) % P
            for k in range(r, len(a)):
                a[k][c] = (a[k][c]-factor*a[k][r]) % P
    return answer


def block(i, k):
    poly = [1]
    for y in J:
        if y not in k:
            poly = multiply(poly, [-y % P, 1])
    values = {x: evaluate(poly, x) for x in H}
    assert all(values[x] for x in S+k)
    observed = sorted(set(S)-set(i))
    z = observed[0]
    q = [[(int(y == x)*values[z]-int(y == z)*values[x]) % P for y in S]
         for x in observed[1:]]
    exterior = [[(a[x]*b[y]-a[y]*b[x]) % P for x, y in PAIRS]
                for a, b in combinations(q, 2)]
    return q, values, z, exterior


def plane(p, pivot):
    a, b = pivot
    skew = [[0]*7 for _ in S]
    for (x, y), value in zip(PAIRS, p):
        skew[x][y], skew[y][x] = value, -value % P
    u = [skew[x][b]*pow(skew[a][b], -1, P) % P for x in range(7)]
    v = skew[a][:]
    assert [(u[x]*v[y]-u[y]*v[x]) % P for x, y in PAIRS] == p
    return u, v


def run():
    path = HERE/'active-rank19-complete-loci.json'
    before = digest(path)
    cert = json.loads(path.read_bytes())
    assert cert['H'] == H and cert['S'] == S and cert['modulus'] == P
    audit = json.loads((HERE/cert['audit_path']).read_bytes())
    assert digest(HERE/cert['audit_path']) == cert['audit_sha256']
    assert not audit['failures'] and all(c['passed'] for c in audit['checks'])
    assert audit['artifact_hashes_before'] == audit['artifact_hashes_after']
    for name, value in audit['artifact_hashes_after'].items():
        assert digest(HERE/name) == value
    source = json.loads((HERE/cert['source_path']).read_bytes())
    assert digest(HERE/cert['source_path']) == cert['source_sha256']
    assert cert['source_sha256'] == audit['artifact_hashes_after'][cert['source_path']]
    assert len(source['records']) == 599
    expected = [r for r in source['records'] if r['status'] == 'screen_failure' and r['rank'] == 19
                and 'L112_exchanged_rows' not in r['prior_exclusions']
                and (r['third_index'], r['fourth_index']) != (0, 320)]
    indices = [[r['third_index'], r['fourth_index']] for r in expected]
    assert len(indices) == len(set(map(tuple, indices))) == 223
    assert cert['selected_manifest'] == cert['processed_manifest'] == indices
    assert len(cert['records']) == len(expected)
    universe = list(product(combinations(S, 2), combinations(J, 2)))
    first = [((1, 8), (47, 50)), ((12, 18), (64, 70))]
    initial = set(sum((list(i+k) for i, k in first), []))
    eligible = [r for r in universe if all(len(set(r[0]+r[1]) & set(i+k)) <= 1 for i, k in first)]
    disjoint = [r for r in eligible if not set(r[0]+r[1]) & initial]
    thirds = [r for r in eligible if r not in disjoint and r != ((1, 22), (75, 79))]
    assert len(thirds) == 351
    records, survivors, failed_counts = [], [], Counter()
    gcd_counts, failing_with_lambda_zero = Counter(), 0
    projection_pivots = plucker_pivots = 0
    points_count = 0
    for old, rec in zip(expected, cert['records']):
        n, f = index = rec['historical_index']
        rows = [{'I': list(i), 'K': list(k)} for i, k in first+[thirds[n], universe[f]]]
        assert rec['rows'] == rows and old['four_rows'] == [[r['I'], r['K']] for r in rows]
        assert source['records'][rec['source_record_position']] == old
        blocks = [block(row['I'], row['K']) for row in rows]
        matrix = [r for q, g, z, ext in blocks for r in ext]
        assert matrix == rec['original_matrix'] and rank(matrix) == 19
        b0, b1 = basis = rec['kernel_basis']
        assert basis == old['kernel_basis']
        residuals = [[dot(r, v) for r in matrix] for v in basis]
        assert residuals == rec['kernel_residuals'] and not any(map(any, residuals))
        assert [[v[c] for c in rec['free_columns']] for v in basis] == [[1, 0], [0, 1]]
        assert len(rec['rank_minor_rows']) == len(rec['rank_minor_columns']) == 19
        minor = [[matrix[r][c] for c in rec['rank_minor_columns']] for r in rec['rank_minor_rows']]
        assert determinant(minor) == rec['rank_minor_residue'] != 0
        # Full coefficient multiplication, without the producer's polynomial code.
        quadrics = []
        for a, b, c, d in QUADS:
            q = [0, 0, 0]
            for sign, ij, kl in [(1, (a, b), (c, d)), (-1, (a, c), (b, d)), (1, (a, d), (b, c))]:
                i, k = PAIRS.index(ij), PAIRS.index(kl)
                q[0] += sign*b0[i]*b0[k]
                q[1] += sign*(b0[i]*b1[k]+b1[i]*b0[k])
                q[2] += sign*b1[i]*b1[k]
            quadrics.append([x % P for x in q])
        assert quadrics == rec['homogeneous_coefficients_s2_st_t2']
        gcd = rec['affine_gcd']
        gcd_counts[str(gcd)] += 1
        assert gcd and gcd[-1] == 1
        assert len(rec['bezout_coefficients']) == len(rec['gcd_quotients']) == 35
        total = []
        for q, quotient, coefficient in zip(quadrics, rec['gcd_quotients'], rec['bezout_coefficients']):
            assert multiply(gcd, quotient) == add(q, [])
            total = add(total, multiply(coefficient, q))
        assert total == gcd
        factorization = [1]
        roots = []
        for factor in rec['affine_linear_factors']:
            t, multiplicity = factor['root'], factor['multiplicity']
            assert multiplicity == 1 and t not in roots
            roots.append(t)
            factorization = multiply(factorization, [-t % P, 1])
        assert rec['remaining_affine_factor'] == [1] and factorization == gcd
        infinity = all(q[2] == 0 for q in quadrics)
        assert infinity == rec['infinity_is_decomposable']
        parameters = [[1, t] for t in roots]+([[0, 1]] if infinity else [])
        assert len(parameters) == 2 and rec['locus_type'] == 'finite_split'
        assert [p['homogeneous_parameter'] for p in rec['points_and_all_row_gates']] == parameters
        point_records, intrinsic = [], []
        for (s, t), point in zip(parameters, rec['points_and_all_row_gates']):
            p = [(s*x+t*y) % P for x, y in zip(*basis)]
            assert p == point['bivector']
            nonzero_pivots = [pair for pair, value in zip(PAIRS, p) if value]
            assert point['pivot_indices'] == list(nonzero_pivots[0])
            u, v = plane(p, nonzero_pivots[0])
            assert u == point['u'] and v == point['v']
            canonical_h = []
            row_passes = []
            for row, (q, g, z, ext), gate in zip(rows, blocks, point['row_gates']):
                qu, qv = [dot(c, u) for c in q], [dot(c, v) for c in q]
                minors = [(qu[x]*qv[y]-qu[y]*qv[x]) % P for x, y in combinations(range(4), 2)]
                assert qu == gate['Q_u'] and qv == gate['Q_v']
                assert not any(minors) and minors == gate['projection_minors']
                assert any(qu+qv) and gate['projection_rank'] == 1
                k = next(k for k in range(4) if qu[k] or qv[k])
                alpha, beta = -qv[k] % P, qu[k]
                h = [(alpha*x+beta*y) % P for x, y in zip(u, v)]
                assert [alpha, beta] == gate['direction_coefficients']
                assert h == gate['intersection_vector'] and any(h) and all(dot(c, h) == 0 for c in q)
                lam = h[S.index(z)]*pow(g[z], -1, P) % P
                error = {x: (h[S.index(x)]-lam*g[x]) % P for x in row['I']}
                error.update({x: -lam*g[x] % P for x in row['K']})
                weights = [error[x] for x in row['I']+row['K']]
                identity = [((h[S.index(x)] if x in S else 0)-error.get(x, 0)-lam*g[x]) % P for x in H]
                moments = [sum(((h[S.index(x)] if x in S else 0)-error.get(x, 0))*pow(x, d, P) for x in H) % P for d in range(1, 9)]
                assert not any(identity+moments)
                assert identity == gate['h_minus_error_minus_lambda_g_on_H'] and moments == gate['moment_residuals']
                assert lam == gate['lambda_value'] and weights == gate['error_weights']
                assert weights[:2] == gate['overlap_weights']
                failed = (['lambda_zero'] if not lam else [])+[
                    f'overlap_weight_zero_at_{x}' for x in row['I'] if not error[x]]
                assert failed == gate['failed_gates'] and gate['passes'] == (not failed)
                assert gate['prescribed_finite_gate'] == {'D_coefficient': alpha, 'C_coefficient': -beta % P}
                canonical_h.append(h)
                row_passes.append(not failed)
                failed_counts.update(failed)
            assert point['passes_intrinsic_gates'] == all(row_passes)
            if not all(row_passes):
                assert any(g['lambda_value'] == 0 for g in point['row_gates'])
                failing_with_lambda_zero += 1
            intrinsic.append(all(row_passes))
            # Every nonzero Plucker chart and every nonzero projection-row
            # pivot is covered; their unique h must be a nonzero multiple.
            pivot_records = []
            for pivot in nonzero_pivots:
                uu, vv = plane(p, pivot)
                pr = []
                for row_number, (row, (q, g, z, ext), h0) in enumerate(zip(rows, blocks, canonical_h)):
                    qu, qv = [dot(c, uu) for c in q], [dot(c, vv) for c in q]
                    assert any(qu+qv)
                    alternatives = []
                    for k in range(4):
                        if not (qu[k] or qv[k]):
                            continue
                        alpha, beta = -qv[k] % P, qu[k]
                        h = [(alpha*x+beta*y) % P for x, y in zip(uu, vv)]
                        anchor = next(i for i, x in enumerate(h0) if x)
                        multiple = h[anchor]*pow(h0[anchor], -1, P) % P
                        assert multiple and h == [multiple*x % P for x in h0]
                        assert all(dot(c, h) == 0 for c in q)
                        lam = h[S.index(z)]*pow(g[z], -1, P) % P
                        canonical = point['row_gates'][row_number]
                        assert lam == multiple*canonical['lambda_value'] % P
                        weights = [(h[S.index(x)]-lam*g[x]) % P for x in row['I']]+[-lam*g[x] % P for x in row['K']]
                        assert weights == [multiple*x % P for x in canonical['error_weights']]
                        alternatives.append({'projection_pivot': k, 'direction': [alpha, beta],
                                             'nonzero_scale_to_canonical': multiple})
                        projection_pivots += 1
                    pr.append(alternatives)
                pivot_records.append({'plucker_pivot': list(pivot), 'u': uu, 'v': vv, 'row_pivot_certificates': pr})
                plucker_pivots += 1
            point_records.append({'parameter': [s, t], 'all_pivot_replay': pivot_records})
            points_count += 1
        expected_disposition = 'intrinsic_survivor' if any(intrinsic) else 'excluded_necessary_gates'
        assert rec['disposition'] == expected_disposition
        assert (gcd == [0, 1]) == (expected_disposition == 'excluded_necessary_gates')
        if any(intrinsic):
            survivors.append(index)
        records.append({'historical_index': index, 'rank_minor_residue': rec['rank_minor_residue'],
                        'complete_parameters': parameters, 'intrinsic_point_passes': intrinsic,
                        'points': point_records})
    summary = {'required_occurrences': 223, 'replayed_occurrences': len(records),
               'matrix_entries_compared': 504*len(records), 'homogeneous_equations': 35*len(records),
               'gcd_identities': 36*len(records), 'complete_points': points_count,
               'row_gates_replayed': 4*points_count, 'all_nonzero_plucker_pivots': plucker_pivots,
               'all_nonzero_row_projection_pivots': projection_pivots,
               'excluded_occurrences': len(records)-len(survivors),
               'surviving_occurrence_indices': survivors,
               'failed_gate_histogram': dict(failed_counts), 'unresolved_branches': 0}
    summary['failing_points_with_lambda_zero'] = failing_with_lambda_zero
    assert failing_with_lambda_zero == cert['summary']['failing_points_with_lambda_zero'] == 442
    assert dict(gcd_counts) == cert['summary']['affine_gcd_histogram']
    assert len(survivors) == 4 and survivors == cert['summary']['surviving_occurrence_indices']
    assert failed_counts == Counter(cert['summary']['failed_gate_histogram'])
    assert not cert['failures'] and not cert['unresolved'] and digest(path) == before
    assert all(digest(HERE/name) == value for name, value in audit['artifact_hashes_after'].items())
    output = {'source_sha256': before, 'code_sha256': digest(Path(__file__)),
              'summary': summary, 'records': records, 'failures': []}
    target = HERE/'active-rank19-complete-loci-replay.json'
    target.write_text(json.dumps(output, separators=(',', ':'))+'\n')
    print(json.dumps(summary, sort_keys=True))
    print(f'Failures 0; unchanged historical inputs; certificate {target}')


if __name__ == '__main__':
    run()
