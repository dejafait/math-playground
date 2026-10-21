"""Complete independent replay of the approved residual coordinate-factor filter.

Run: python3 scripts/seven-coordinate/verify_residual_coordinate_factors.py
Derivative blocks and column elimination; no producer imports or point sampling.
"""
from collections import Counter
from hashlib import sha256
from itertools import combinations, product
from pathlib import Path
import json

import verify_fixed_three_row_extensions as independent

P = 97
HERE = Path(__file__).resolve().parent
S = [1, 8, 12, 18, 22, 27, 33]
H = [x for x in range(1, P) if pow(x, 16, P) == 1]
J = [x for x in H if x not in S]
PAIRS = list(combinations(range(7), 2))
FIRST = [((1, 8), (47, 50)), ((12, 18), (64, 70))]
NAMED = ((1, 22), (75, 79))


def g_derivative(k, x):
    denominator = 1
    for y in S+list(k):
        if y != x:
            denominator = denominator*(x-y) % P
    assert denominator
    return 16*pow(x, 15, P)*pow(denominator, -1, P) % P


def run():
    path = HERE/'residual-coordinate-factors.json'
    target_data = path.read_bytes()
    target = json.loads(target_data)
    source_path = HERE/'remaining-third-factor-filter.json'
    source_data = source_path.read_bytes()
    source = json.loads(source_data)
    assert target['source_sha256'] == sha256(source_data).hexdigest()
    assert target['source'] == source_path.name and target['failures'] == source['failures'] == []
    assert target['modulus'] == P and target['S'] == S and target['H'] == H
    assert target['first_two'] == [[list(i), list(k)] for i, k in FIRST]
    universe = list(product(combinations(S, 2), combinations(J, 2)))
    sets = {key: set(key[0]+key[1]) for key in universe}
    pair_union = sets[FIRST[0]] | sets[FIRST[1]]
    thirds = [key for key in universe if all(len(sets[key]&sets[a]) <= 1 for a in FIRST)
              and sets[key]&pair_union and key != NAMED]
    assert len(thirds) == len(source['thirds']) == 351
    assert [(tuple(m['third_I']), tuple(m['third_K'])) for m in source['thirds']] == thirds
    assert H == independent.H and S == independent.S and J == independent.J
    blocks = {key: independent.block(*key) for key in universe}
    stats, ranks, chosen, overlap = Counter(), Counter(), Counter(), Counter()
    disjoint = {key for key in universe if all(len(sets[key]&sets[a]) <= 1 for a in FIRST)
                and not sets[key]&pair_union}
    old_excluded = {thirds[n] for n in source['excluded_triple_indices']}
    old_thirds, remaining_thirds, excluded_thirds, audits = [], [], [], []
    regression = None
    target_by_third = {meta['third_index']: meta for meta in target['thirds']}
    assert len(target_by_third) == len(target['thirds']) == 230
    gate_checks = 0
    for n, (third, meta) in enumerate(zip(thirds, source['thirds'])):
        src_path = HERE/meta['certificate']
        assert src_path == HERE/'remaining-third-factor-filter'/f'third-{n:03d}.json'
        data = src_path.read_bytes()
        digest = sha256(data).hexdigest()
        assert digest == meta['sha256']
        src = json.loads(data)
        assert src['failures'] == [] and len(src['cases']) == 756
        assert [(tuple(c['I']), tuple(c['K'])) for c in src['cases']] == universe
        indices = [u for u, c in enumerate(src['cases']) if c['status'] == 'unresolved']
        assert indices == src['residual_case_indices'] and len(indices) == meta['residual_fourths']
        if not indices:
            assert n not in target_by_third
            continue
        old_thirds.append(n)
        new_meta = target_by_third[n]
        new_path = HERE/new_meta['certificate']
        assert new_path == HERE/'residual-coordinate-factors'/f'third-{n:03d}.json'
        new_data = new_path.read_bytes()
        assert sha256(new_data).hexdigest() == new_meta['sha256']
        saved = json.loads(new_data)
        assert saved['failures'] == [] and saved['third_index'] == n
        assert saved['source_sha256'] == digest and saved['source_shard'] == str(src_path.relative_to(HERE))
        assert saved['historical_residual_indices'] == indices
        assert [c['fourth_index'] for c in saved['cases']] == indices
        remaining = []
        for u, rec in zip(indices, saved['cases']):
            original = src['cases'][u]
            keys = FIRST+[third, universe[u]]
            assert rec['third_index'] == n and rec['four_rows'] == [[list(i), list(k)] for i, k in keys]
            assert len(set(keys)) == 4 and all(len(sets[a]&sets[b]) <= 1 for a, b in combinations(keys, 2))
            matrix = [row for key in keys for row in blocks[key]]
            rank, columns = independent.column_rank(matrix)
            assert rank == rec['rank'] == original['rank'] and rank < 21
            basis = rec['kernel_basis']
            assert basis == original['kernel_basis'] and len(basis) == 21-rank
            assert all(len(v) == 21 and all(type(x) is int and 0 <= x < P for x in v) for v in basis)
            free = [c for c in range(21) if c not in columns]
            assert free == rec['free_columns']
            assert [[v[c] for c in free] for v in basis] == [
                [int(a == b) for b in range(len(basis))] for a in range(len(basis))]
            residuals = [[sum(a*b for a, b in zip(v, row)) % P for row in matrix] for v in basis]
            assert residuals == rec['original_stack_residuals'] == original['kernel_residuals']
            assert not any(map(any, residuals))
            row_indices = rec['independent_original_rows']
            assert len(set(row_indices)) == len(row_indices) == rank and all(0 <= r < 24 for r in row_indices)
            assert independent.column_rank([matrix[r] for r in row_indices])[0] == rank
            factors = rec['factor_tests']
            expected_pairs = [(j+1, c) for j, (i, k) in enumerate(keys) for c in i]
            assert [(f['row'], f['coordinate']) for f in factors] == expected_pairs
            passes = []
            for f in factors:
                j, c = f['row']-1, f['coordinate']
                i, k = keys[j]
                forbidden = [t for t, (a, b) in enumerate(PAIRS) if S[a] != c and S[b] != c]
                coefficients = [[v[t] for t in forbidden] for v in basis]
                contained = all(x == 0 for v in coefficients for x in v)
                assert f['forbidden_columns'] == forbidden
                assert f['complete_off_factor_coefficients'] == coefficients and f['contained'] == contained
                if not contained:
                    assert 'gate' not in f
                    continue
                passes.append(f)
                gate = f['gate']
                z = min(set(S)-set(i))
                gz = g_derivative(k, z)
                assert gz and c in i and c != z
                h = [int(x == c) for x in S]
                observed = sorted(set(S)-set(i))
                # Rebuild the four covectors through normalized ratios, independently.
                qh = [(h[S.index(x)]*pow(g_derivative(k, x), -1, P)
                       -h[S.index(z)]*pow(gz, -1, P))*gz*g_derivative(k, x) % P
                      for x in observed[1:]]
                lam = h[S.index(z)]*pow(gz, -1, P) % P
                error = {str(x): ((h[S.index(x)]-lam*g_derivative(k, x)) if x in i
                                 else -lam*g_derivative(k, x)) % P for x in i+k}
                moments = [sum(((h[S.index(x)] if x in S else 0)-error.get(str(x), 0))
                               *pow(x, d, P) for x in H) % P for d in range(1, 9)]
                other = next(x for x in i if x != c)
                expected = {'pivot': z, 'g_pivot': gz, 'Q_Ec': qh, 'h': h,
                    'lambda': lam, 'error': error, 'other_overlap': other,
                    'original_moment_residuals': moments, 'rank_zero': 'rejected_by_L109_nonpersistence',
                    'rank_one': 'unique_recovery_line_Ec_fails_full_weights',
                    'prescribed_chart': 'intrinsic_failure_before_finite_gate'}
                assert gate == expected and not any(qh) and not any(moments)
                assert lam == error[str(other)] == 0 and all(error[str(x)] == 0 for x in k)
                assert error[str(c)] == 1
                gate_checks += 1
            status = 'excluded_coordinate_factor' if passes else 'unresolved'
            assert rec['status'] == status
            fourth = universe[u]
            prior_class = ('L112_disjoint' if fourth in disjoint else 'L113_named' if fourth == NAMED
                           else 'L114_excluded' if fourth in old_excluded else 'historical_residual')
            assert rec['fourth_historical_class'] == prior_class
            overlap[f'{prior_class}:{status}'] += 1
            assert rec['selected_factor'] == ({'row': passes[0]['row'], 'coordinate': passes[0]['coordinate']} if passes else None)
            known = (n, u) == (0, 249)
            assert rec['already_excluded_by_L115'] == known
            if known:
                assert passes and any(f['row'] == 2 and f['coordinate'] == 12 for f in passes)
                regression = {'third_index': n, 'fourth_index': u, 'status': status,
                              'passing_factors': [[f['row'], f['coordinate']] for f in passes]}
            if passes:
                chosen[f"row{passes[0]['row']}_label{passes[0]['coordinate']}"] += 1
            else:
                remaining.append(u)
            stats.update({'occurrences': 1, status: 1, 'basis_vectors': len(basis),
                          'original_residual_entries': 24*len(basis), 'factor_tests': 8,
                          'passing_factor_tests': len(passes)})
            ranks[rank] += 1
        assert remaining == saved['remaining_indices']
        assert new_meta == {'third_index': n, 'historical': len(indices), 'remaining': len(remaining),
                            'excluded': len(indices)-len(remaining), 'certificate': str(new_path.relative_to(HERE)),
                            'sha256': sha256(new_data).hexdigest()}
        (remaining_thirds if remaining else excluded_thirds).append(n)
        audits.append(new_meta)
        if len(audits) % 25 == 0:
            print(f"Replayed residual thirds {len(audits)}/230; occurrences {stats['occurrences']}/24866", flush=True)
    assert stats['occurrences'] == 24866 and len(old_thirds) == 230
    assert old_thirds == source['residual_triple_indices'] and regression == target['L115_regression']
    summary = dict(stats, required_occurrences=24866, historical_residual_thirds=230,
                   remaining_thirds=len(remaining_thirds), newly_excluded_thirds=len(excluded_thirds),
                   known_L115_occurrences=1, newly_excluded_occurrences=stats['excluded_coordinate_factor']-1,
                   rank_histogram={str(k): v for k, v in sorted(ranks.items())},
                   selected_factor_histogram=dict(sorted(chosen.items())),
                   fourth_historical_class_histogram=dict(sorted(overlap.items())))
    assert summary == target['summary'] and audits == target['thirds']
    assert excluded_thirds == target['newly_excluded_third_indices']
    assert remaining_thirds == target['remaining_third_indices']
    output = {'source_sha256': sha256(target_data).hexdigest(), 'summary': summary,
              'complete_gate_certificates_checked': gate_checks,
              'thirds': audits, 'L115_regression': regression, 'failures': [],
              'scope': 'same-step complete independent replay; separate critical audit remains required'}
    out = HERE/'residual-coordinate-factors-replay.json'
    out.write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps(summary, sort_keys=True))
    print(f'Failures: 0; gate certificates {gate_checks}; replay: {out}')


if __name__ == '__main__':
    run()
