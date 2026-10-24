"""Complete L109 quotient test on exactly L149's two audited survivors."""
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
PLANES = [
    ('P', [1, 0, 40, 56, 96, 57, 34], [0, 45, 56, 59, 65, 18, 55], [[467, 750], [750, 467]]),
    ('R', [1, 0, 31, 55, 34, 85, 3], [0, 47, 67, 90, 86, 57, 18], [[608, 695], [695, 608]])]



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
    target = HERE/'l149-survivor-full-rows.json'
    out = {'scope': 'Exactly audited L149 P/R, all 756 two-overlap rows per plane; necessary test only',
           'modulus': P, 'H': H, 'S': S, 'planes': [], 'failures': [], 'unresolved': []}
    try:
        assert __debug__
        audit = json.loads((HERE/'l149-critical-audit.json').read_bytes())
        assert not audit['failures'] and len(audit['checks']) == 4476
        assert all(c['passes'] for c in audit['checks'])
        assert len(audit['runs']) == 2 and all(r['returncode'] == 0 for r in audit['runs'])
        assert audit['original_artifacts_byte_unchanged']
        assert digest(HERE/'audit_l149.py') == audit['audit_code_sha256']
        for name, value in audit['input_sha256'].items():
            assert digest(HERE/name) == value
        bound_names = list(audit['input_sha256'])+['l149-critical-audit.json', 'audit_l149.py']
        out['input_hashes_before'] = {name: digest(HERE/name) for name in bound_names}
        out['producer_sha256'] = digest(Path(__file__))
        source = json.loads((HERE/'l148-rank20-gates.json').read_bytes())
        assert source['failures'] == [] and source['original_inputs_unchanged']
        assert source['selected_manifest'] == [[467,750],[499,668],[608,695],[668,499],
                                               [678,749],[695,608],[749,678],[750,467]]
        assert [r['indices'] for r in source['records'] if r['disposition'] == 'intrinsic_survivor'] == [
            [467,750],[608,695],[695,608],[750,467]]
        assert source['code_sha256'] == digest(HERE/'l148_rank20_gates.py')
        universe = [(list(i), list(k)) for i in combinations(S, 2) for k in combinations(J, 2)]
        assert len(H) == 16 and len(J) == 9 and len(universe) == 756
        for label, u, v, indices in PLANES:
            originals = [r for r in source['records'] if r['indices'] in indices]
            assert len(originals) == 2 and [r['indices'] for r in originals] == indices
            for old in originals:
                assert old['disposition'] == 'intrinsic_survivor'
                assert old['plane_and_all_row_gates']['passes_intrinsic_gates']
                assert old['plane_and_all_row_gates']['u'] == u
                assert old['plane_and_all_row_gates']['v'] == v
            rec = {'label': label, 'historical_indices': indices, 'u': u, 'v': v, 'rows': [],
                   'source_bindings': [{'indices': r['indices'], 'shard': r['shard'],
                                        'case_pointer': r['case_pointer'],
                                        'rank_minor_residue': r['rank_minor_residue']} for r in originals]}
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
            for old in originals:
                for oldrow, gate in zip(old['rows'], old['plane_and_all_row_gates']['row_gates']):
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
            rec['disposition'] = ('rank_zero_nonpersistence_obstruction' if rec['summary']['rank_zero_obstruction'] else
                                  'excluded_necessary_shortfall' if len(groups) < 12 else 'complete_residual_saved')
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
