"""Supplementary independent gate replay; no producer imports.

This is same-step verification, not a separate critical proof audit.
Run: python3 scripts/seven-coordinate/verify_residual_kernel_gates.py
"""
from collections import Counter
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json

P = 97
S = [1, 8, 12, 18, 22, 27, 33]
H = sorted({pow(8, n, P) for n in range(16)})
PAIRS = list(combinations(range(7), 2))
QUADS = list(combinations(range(7), 4))
HERE = Path(__file__).resolve().parent


def rank(rows):
    a = [row[:] for row in rows]
    n = 0
    for j in range(len(a[0])):
        k = next((k for k in range(n, len(a)) if a[k][j]), None)
        if k is None:
            continue
        a[n], a[k] = a[k], a[n]
        a[n] = [x*pow(a[n][j], -1, P) % P for x in a[n]]
        for k in range(n+1, len(a)):
            c = a[k][j]
            a[k] = [(x-c*y) % P for x, y in zip(a[k], a[n])]
        n += 1
    return n


def alternating(p):
    a = [[0]*7 for _ in range(7)]
    for (i, j), x in zip(PAIRS, p):
        a[i][j], a[j][i] = x, -x % P
    return a


def quadrics(p):
    a = alternating(p)
    return [(a[i][j]*a[k][l]-a[i][k]*a[j][l]+a[i][l]*a[j][k]) % P
            for i, j, k, l in QUADS]


def projective(v):
    inv = pow(next(x for x in v if x), -1, P)
    return [x*inv % P for x in v]


def convolution(a, b):
    result = [0]*(len(a)+len(b)-1) if a and b else []
    for n in range(len(result)):
        result[n] = sum(a[i]*b[n-i] for i in range(len(a)) if 0 <= n-i < len(b)) % P
    return result


def run():
    raw = (HERE/'third-row-variation.json').read_bytes()
    source = json.loads(raw)
    assert sha256(raw).hexdigest() == '34d6bb68537b8e5b153552801426c2f37266c96fa1446bb8ec89ae03885f85c2'
    data_bytes = (HERE/'residual-kernel-gates.json').read_bytes()
    data = json.loads(data_bytes)
    assert source['failures'] == data['failures'] == []
    assert data['source_sha256'] == sha256(raw).hexdigest()
    assert data['S'] == S and data['H'] == H
    expected = {(n, m) for n, seed in enumerate(source['seeds'])
                if not seed['reused_audited_L110'] for m, c in enumerate(seed['cases'])
                if c['pairwise_linear'] and c['rank'] < 21}
    assert len(expected) == 266
    assert [(r['seed_index'], r['case_index']) for r in data['records']] == sorted(expected)
    replays, failed, gate_counts = [], [], Counter()
    for rec in data['records']:
        n, m = rec['seed_index'], rec['case_index']
        seed = source['seeds'][n]
        case = seed['cases'][m]
        basis = case['kernel_basis']
        assert basis == rec['kernel_basis'] and rec['rank'] == case['rank']
        rows = source['first_two']+[{'I': seed['third_I'], 'K': seed['third_K']},
                                    {'I': case['I'], 'K': case['K']}]
        assert rows == rec['rows']
        assert all(len(set(a['I']+a['K']) & set(b['I']+b['K'])) <= 1
                   for a, b in combinations(rows, 2))
        q0 = quadrics(basis[0])
        q2 = quadrics(basis[1]) if len(basis) == 2 else [0]*35
        b1 = basis[1] if len(basis) == 2 else [0]*21
        at_one = quadrics([(a+b) % P for a, b in zip(basis[0], b1)])
        at_minus_one = quadrics([(a-b) % P for a, b in zip(basis[0], b1)])
        mixed = [(a-b)*pow(2, -1, P) % P for a, b in zip(at_one, at_minus_one)]
        coefficients = [list(x) for x in zip(q0, mixed, q2)]
        assert coefficients == rec['homogeneous_plucker_coefficients']
        assert q0 == q2 == [0]*35
        assert not any(mixed) if len(basis) == 1 else any(mixed)
        assert rec['affine_gcd'] == ([] if len(basis) == 1 else [0, 1])
        total = [0]*10
        for c, q in zip(rec['bezout_coefficients'], coefficients):
            for j, x in enumerate(convolution(c, q)):
                total[j] = (total[j]+x) % P
        while total and total[-1] == 0:
            total.pop()
        assert total == rec['affine_gcd']
        assert len(rec['decomposable_points']) == len(basis)
        point_records = []
        for p, saved in zip(basis, rec['decomposable_points']):
            assert p == saved['bivector']
            a = alternating(p)
            assert rank(a) == 2 and quadrics(p) == [0]*35
            # A different nonzero pivot and scaling reconstruct the same plane.
            i, j = PAIRS[max(n for n, x in enumerate(p) if x)]
            u, v = a[i][:], a[j][:]
            independent_wedge = [(u[x]*v[y]-u[y]*v[x]) % P for x, y in PAIRS]
            assert projective(independent_wedge) == projective(p)
            all_rows, failures = [], []
            for row_number, (row, old_gate) in enumerate(zip(rows, saved['row_gates'])):
                # Differentiate X^16-1 at S union K to obtain g, independently
                # of the producer's seven-factor direct product.
                g = {}
                for x in S+row['K']:
                    den = 1
                    for y in S+row['K']:
                        if x != y:
                            den = den*(x-y) % P
                    g[x] = 16*pow(x, 15, P)*pow(den, -1, P) % P
                    assert g[x]
                observed = sorted(set(S)-set(row['I']))
                z = observed[-1]
                quotient_u, quotient_v = [[(w[S.index(x)]*pow(g[x], -1, P)-
                                            w[S.index(z)]*pow(g[z], -1, P)) % P
                                           for x in observed[:-1]] for w in (u, v)]
                restricted_rank = rank([list(x) for x in zip(quotient_u, quotient_v)])
                assert restricted_rank == old_gate['projection_rank'] == 1
                j0 = max(j for j in range(4) if quotient_u[j] or quotient_v[j])
                alpha, beta = quotient_v[j0], -quotient_u[j0] % P
                h = [(alpha*x+beta*y) % P for x, y in zip(u, v)]
                assert projective(h) == projective(old_gate['intersection_vector'])
                lam = h[S.index(z)]*pow(g[z], -1, P) % P
                assert all(h[S.index(x)] == lam*g[x] % P for x in observed)
                weights = [(h[S.index(x)]-lam*g[x]) % P for x in row['I']]+[
                    -lam*g[x] % P for x in row['K']]
                assert (lam == 0) == (old_gate['lambda_value'] == 0)
                assert [x == 0 for x in weights] == [x == 0 for x in old_gate['error_weights']]
                errors = dict(zip(row['I']+row['K'], weights))
                moments = [sum(((h[S.index(x)] if x in S else 0)-errors.get(x, 0))*
                               pow(x, d, P) for x in H) % P for d in range(1, 9)]
                assert moments == [0]*8
                row_failures = (['lambda_zero'] if not lam else [])+[
                    f'overlap_weight_zero_at_{x}' for x, w in zip(row['I'], weights[:2]) if not w]
                assert row_failures == old_gate['failed_gates']
                failures.extend(row_failures)
                gate_counts.update(row_failures)
                # Check the stored original-chart inequality in its stated basis.
                old_alpha, old_beta = old_gate['direction_coefficients']
                assert old_gate['prescribed_finite_gate'] == {
                    'D_coefficient': old_alpha, 'C_coefficient': -old_beta % P}
                all_rows.append({'row': row_number, 'projected_rank': restricted_rank,
                                 'intersection_vector': h, 'lambda_value': lam,
                                 'error_weights': weights, 'moment_residuals': moments,
                                 'failed_gates': row_failures})
            assert failures and not saved['passes_intrinsic_gates']
            assert all_rows[3]['lambda_value'] == 0
            point_records.append({'bivector': p, 'alternate_u': u, 'alternate_v': v,
                                  'row_replay': all_rows, 'rejected': True})
        replays.append({'seed_index': n, 'case_index': m,
                        'reconstructed_plucker_coefficients': coefficients,
                        'verified_bezout_sum': total, 'points': point_records})
    points = sum(len(r['points']) for r in replays)
    summary = {'occurrences_replayed': len(replays), 'required_occurrences': 266,
               'all_projective_points_replayed': points, 'required_points': 275,
               'row_gates_replayed': 4*points, 'required_row_gates': 1100,
               'moment_residuals_checked': 32*points, 'failed_gate_counts': dict(gate_counts),
               'intrinsically_passing_points': 0, 'failures': len(failed)}
    assert summary['failed_gate_counts'] == data['summary']['failed_gate_counts']
    assert points == 275
    path = HERE/'residual-kernel-gates-replay.json'
    path.write_text(json.dumps({'source_sha256': sha256(raw).hexdigest(),
                                'gate_certificate_sha256': sha256(data_bytes).hexdigest(),
                                'scope': 'same-step independent reconstruction, not separate critical audit',
                                'summary': summary, 'records': replays, 'failures': failed}, indent=2)+'\n')
    print(json.dumps(summary, sort_keys=True))
    print(f'Certificate: {path}')


if __name__ == '__main__':
    run()
