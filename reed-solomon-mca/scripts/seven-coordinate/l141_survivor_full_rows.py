"""Complete L109 quotient test on exactly L141's audited survivor."""
from collections import Counter
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
P = 97
S = [1, 8, 12, 18, 22, 27, 33]
H = [x for x in range(1, P) if pow(x, 16, P) == 1]
J = sorted(set(H)-set(S))
EXPECTED_U = [1, 0, 42, 90, 52, 62, 61]
EXPECTED_V = [0, 69, 60, 1, 72, 45, 80]



def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def dot(x, y):
    assert len(x) == len(y)
    return sum(a*b for a, b in zip(x, y)) % P


def normalize(values):
    a = next(x for x in values if x)
    return [x*pow(a, -1, P) % P for x in values]


def evaluate_g(k, x):
    value = 1
    for y in J:
        if y not in k:
            value = value*(x-y) % P
    return value


def recovery(u, v, i, k, g, z, direction):
    alpha, beta = direction
    h = [(alpha*a+beta*b) % P for a, b in zip(u, v)]
    assert any(h)
    lam = h[S.index(z)]*pow(g[H.index(z)], -1, P) % P
    error = {x: (h[S.index(x)]-lam*g[H.index(x)]) % P for x in i}
    error.update({x: -lam*g[H.index(x)] % P for x in k})
    identity = [((h[S.index(x)] if x in S else 0)-error.get(x, 0)-lam*gx) % P
                for x, gx in zip(H, g)]
    moments = [sum(((h[S.index(x)] if x in S else 0)-error.get(x, 0))*pow(x, d, P)
                   for x in H) % P for d in range(1, 9)]
    assert len(identity) == 16 and len(moments) == 8 and not any(identity+moments)
    failed = (['lambda_zero'] if not lam else [])+[
        f'overlap_weight_zero_at_{x}' for x in i if not error[x]]
    return {'direction_coefficients': direction, 'normalized_direction': normalize(direction),
            'h': h, 'lambda_value': lam, 'error_weights': [error[x] for x in i+k],
            'identity_residuals': identity, 'shifted_moment_residuals': moments,
            'failed_gates': failed, 'passes_intrinsic': not failed,
            'prescribed_finite_gate': {'D_coefficient': alpha, 'C_coefficient': -beta % P}}


def run():
    target = HERE/'l141-survivor-full-rows.json'
    out = {'scope': 'Exactly L141 L_* at (199,565), all 756 two-overlap rows; necessary test only',
           'modulus': P, 'H': H, 'S': S, 'planes': [], 'failures': [], 'unresolved': []}
    try:
        assert __debug__
        audit = json.loads((HERE/'l141-critical-audit.json').read_bytes())
        assert not audit['failures'] and len(audit['checks']) == 431
        assert all(c['passes'] for c in audit['checks'])
        assert len(audit['runs']) == 2 and all(r['returncode'] == 0 for r in audit['runs'])
        assert audit['original_artifacts_byte_unchanged']
        assert digest(HERE/'audit_l141.py') == audit['audit_code_sha256']
        for name, value in audit['input_sha256'].items():
            assert digest(HERE/name) == value
        bound_names = list(audit['input_sha256'])+['l141-critical-audit.json', 'audit_l141.py']
        out['input_hashes_before'] = {name: digest(HERE/name) for name in bound_names}
        out['producer_sha256'] = digest(Path(__file__))
        source = json.loads((HERE/'first-l140-mismatch-locus-gates.json').read_bytes())
        assert not source['failures'] and source['source']['full_universe_indices'] == [199, 565]
        assert source['source']['pointer'] == '/cases/167'
        assert source['audited_mismatch_binding']['pointer'] == '/overlay/8'
        assert [x['passes_intrinsic_gates'] for x in source['points_and_all_row_gates']] == [False, True]
        survivor = source['points_and_all_row_gates'][1]
        assert survivor['u'] == EXPECTED_U and survivor['v'] == EXPECTED_V
        universe = [(list(i), list(k)) for i in combinations(S, 2) for k in combinations(J, 2)]
        assert len(H) == 16 and len(J) == 9 and len(universe) == 756
        for u, v in [(EXPECTED_U, EXPECTED_V)]:
            rec = {'historical_indices': [[199, 565]], 'u': u, 'v': v, 'rows': []}
            out['planes'].append(rec)
            for row_index, (i, k) in enumerate(universe):
                g = [evaluate_g(k, x) for x in H]
                assert all(g[H.index(x)] for x in S+k)
                observed = sorted(set(S)-set(i))
                z = observed[0]
                q = [[(int(y == x)*g[H.index(z)]-int(y == z)*g[H.index(x)]) % P
                      for y in S] for x in observed[1:]]
                qu, qv = [dot(c, u) for c in q], [dot(c, v) for c in q]
                minors = [(qu[x]*qv[y]-qu[y]*qv[x]) % P for x, y in combinations(range(4), 2)]
                rank = 2 if any(minors) else int(any(qu+qv))
                row = {'row_index': row_index, 'I': i, 'K': k, 'z': z, 'g_values_on_H': g,
                       'Q': q, 'Q_u': qu, 'Q_v': qv, 'projection_minors': minors,
                       'projection_rank': rank}
                rec['rows'].append(row)
                if rank == 2:
                    row['status'] = 'rank_two_no_intersection'
                elif rank == 0:
                    row['status'] = 'rank_zero_whole_plane_nonpersistent_obstruction'
                    row['coefficient_recoveries'] = [recovery(u, v, i, k, g, z, d)
                                                    for d in [[1, 0], [0, 1]]]
                else:
                    pivot = next(n for n in range(4) if qu[n] or qv[n])
                    direction = [-qv[pivot] % P, qu[pivot]]
                    row['projection_pivot'] = pivot
                    row['recovery'] = recovery(u, v, i, k, g, z, direction)
                    row['status'] = ('intrinsic_success' if row['recovery']['passes_intrinsic']
                                     else 'rank_one_failed_weight_gates')
            successes = [r for r in rec['rows'] if r['status'] == 'intrinsic_success']
            groups = {}
            for row in successes:
                groups.setdefault(tuple(row['recovery']['normalized_direction']), []).append(row['row_index'])
            rec['direction_groups'] = [{'direction': list(d), 'row_indices': indices}
                                       for d, indices in sorted(groups.items())]
            rec['duplicate_direction_groups'] = [x for x in rec['direction_groups'] if len(x['row_indices']) > 1]
            for oldrow, gate in zip(source['rows'], survivor['row_gates']):
                new = next(r for r in rec['rows'] if r['I'] == oldrow['I'] and r['K'] == oldrow['K'])
                assert new['status'] == 'intrinsic_success'
                for key in ['direction_coefficients', 'lambda_value', 'error_weights', 'prescribed_finite_gate']:
                    assert new['recovery'][key] == gate[key]
            rec['summary'] = {'covered_rows': len(rec['rows']), 'required_rows': 756,
                              'projection_rank_counts': dict(Counter(r['projection_rank'] for r in rec['rows'])),
                              'status_counts': dict(Counter(r['status'] for r in rec['rows'])),
                              'failed_gate_counts': dict(Counter(f for r in rec['rows'] if 'recovery' in r
                                                                for f in r['recovery']['failed_gates'])),
                              'full_rows': len(successes), 'distinct_directions_before_chart': len(groups),
                              'required_distinct_directions': 12,
                              'duplicate_direction_groups': len(rec['duplicate_direction_groups']),
                              'shortfall': max(0, 12-len(groups)),
                              'rank_zero_obstruction': any(r['projection_rank'] == 0 for r in rec['rows'])}
            rec['disposition'] = ('excluded_necessary_shortfall' if len(groups) < 12 else 'complete_residual_saved')
        out['input_hashes_after'] = {name: digest(HERE/name) for name in bound_names}
        assert out['input_hashes_before'] == out['input_hashes_after']
    except Exception as exc:
        out['failures'].append({'type': type(exc).__name__, 'message': str(exc)})
        raise
    finally:
        target.write_text(json.dumps(out, separators=(',', ':'))+'\n')
        for rec in out['planes']:
            print(json.dumps({'indices': rec['historical_indices'], **rec.get('summary', {})}, sort_keys=True))
        print(f"Failures {len(out['failures'])}; unresolved {len(out['unresolved'])}; full certificate {target}")


if __name__ == '__main__':
    run()
