"""Literal L133 import overlay on exactly the other 117 L132 mismatches.

Run: python3 -B scripts/seven-coordinate/l133_literal_reuse.py
No basis conversion, new locus, changed-row gates, filter or assembly.
"""
from collections import Counter
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json

from verify_new_pair_filter import column_kernel, determinant

HERE = Path(__file__).resolve().parent
P = 97
S = [1, 8, 12, 18, 22, 27, 33]
H = [x for x in range(1, P) if pow(x, 16, P) == 1]
J = [x for x in H if x not in S]
PAIRS = list(combinations(range(7), 2))
HASHES = {}


def raw(name):
    value = (HERE / name).read_bytes()
    HASHES[name] = sha256(value).hexdigest()
    return value


def read(name):
    return json.loads(raw(name))


def bound(name, expected):
    value = read(name)
    assert HASHES[name] == expected, name
    return value


def polynomial(roots):
    coefficients = [1]
    for root in roots:
        out = [0] * (len(coefficients) + 1)
        for i, c in enumerate(coefficients):
            out[i] = (out[i] - root*c) % P
            out[i+1] = (out[i+1] + c) % P
        coefficients = out
    return coefficients


def inputs(row):
    i, k = row['I'], row['K']
    z = min(set(S) - set(i))
    roots = [y for y in J if y not in k]
    values = {}
    for x in S+k:
        value = 1
        for y in roots:
            value = value * (x-y) % P
        assert value
        values[x] = value
    q = [[(int(y == x)*values[z] - int(y == z)*values[x]) % P
          for y in S] for x in S if x not in i and x != z]
    matrix = [[(a[x]*b[y]-a[y]*b[x]) % P for x, y in PAIRS]
              for a, b in combinations(q, 2)]
    return {'I': i, 'K': k, 'z': z, 'g_roots': roots,
            'g_coefficients_ascending': polynomial(roots),
            'g_values_on_S_union_K': {str(x): values[x] for x in S+k},
            'original_block': {'I': i, 'K': k, 'pivot': z,
                               'covectors': q, 'matrix': matrix}}


def source(lemma, stem, audit_name, rejecting_rows):
    audit = read(audit_name)
    assert audit['failures'] == []
    checks = audit['checks']
    assert (all(checks.values()) if isinstance(checks, dict)
            else all(c.get('passes', c.get('passed', False)) for c in checks))
    source_hashes = {name: item['sha256'] for name, item in audit['inputs'].items()}
    for name, expected in source_hashes.items():
        assert sha256((HERE/name).read_bytes()).hexdigest() == expected, name
        HASHES[name] = expected
    cert_name, replay_name = stem+'.json', stem+'-replay.json'
    cert = bound(cert_name, source_hashes[cert_name])
    replay = bound(replay_name, source_hashes[replay_name])
    assert replay['certificate_sha256'] == HASHES[cert_name]
    assert cert['failures'] == replay['failures'] == []
    assert cert['S'] == S and cert['H'] == H and cert['J'] == J
    assert cert['column_pairs'] == [[S[a], S[b]] for a, b in PAIRS]
    assert replay['rebuilt_original_matrix'] == cert['original_matrix']
    assert replay['kernel_residuals'] == cert['kernel_residuals']
    assert replay['plucker_coefficients_s2_st_t2'] == cert['plucker_coefficients_s2_st_t2']
    assert len(cert['plucker_coefficients_s2_st_t2']) == 35
    assert cert['complete_projective_parameter_locus'] == [[1, 0], [0, 1]]
    assert len(cert['points_and_all_row_gates']) == 2
    bindings = []
    for point_index, row_index in enumerate(rejecting_rows):
        point = cert['points_and_all_row_gates'][point_index]
        gate = point['row_gates'][row_index]
        row_input = inputs(cert['rows'][row_index])
        assert point['bivector'] == cert['kernel_basis'][point_index]
        assert [((point['u'][a]*point['v'][b]-point['u'][b]*point['v'][a]) % P)
                for a, b in PAIRS] == point['bivector']
        assert row_input['original_block'] == cert['blocks'][row_index]
        assert row_input['g_values_on_S_union_K'] == gate['g_values_on_S_union_K']
        assert gate['projection_rank'] == 1 and gate['lambda_value'] == 0
        assert gate['passes'] is False and 'lambda_zero' in gate['failed_gates']
        assert not any(gate['moment_residuals'])
        assert not any(gate['h_minus_error_minus_lambda_g_on_H'])
        assert gate['error_weights'][2:] == [0, 0]
        alpha, beta = gate['direction_coefficients']
        assert gate['prescribed_finite_gate'] == {'D_coefficient': alpha,
                                                'C_coefficient': -beta % P}
        assert gate['original_first_coefficient'] == '(D*alpha-C*beta)/(AD-BC)'
        replay_row = [g for g in replay['all_row_replay']
                      if g['point_index'] == point_index and g['row_number'] == row_index+1]
        assert len(replay_row) == 1
        replay_row = replay_row[0]
        for key, old in [('Q_u', 'Q_u'), ('Q_v', 'Q_v'), ('h', 'intersection_vector'),
                         ('lambda', 'lambda_value'),
                         ('moments', 'moment_residuals')]:
            assert replay_row[key] == gate[old]
        assert replay_row['error'] == dict(zip(map(str, row_input['I']+row_input['K']),
                                              gate['error_weights']))
        assert replay_row['finite_gate_coefficients_D_C'] == [alpha, -beta % P]
        bindings.append({'source_point_index': point_index, 'source_row_number': row_index+1,
                         'row_input': row_input,
                         'plane_representative': {k: point[k] for k in ('u', 'v', 'bivector', 'pivot_indices')},
                         'unchanged_rejecting_gate': gate,
                         'certificate_point_pointer': f'/points_and_all_row_gates/{point_index}',
                         'canonical_proof': f'{lemma}: original-row gates and prescribed charts',
                         'audit': audit_name})
    return {'lemma': lemma, 'certificate': cert_name, 'replay': replay_name,
            'audit': audit_name, 'kernel_basis': cert['kernel_basis'],
            'imported_locus': {key: cert[key] for key in (
                'plucker_quadruples', 'plucker_coefficients_s2_st_t2', 'affine_gcd',
                'bezout_coefficients', 'affine_quotients', 'complete_projective_parameter_locus')},
            'point_bindings': bindings}


def run():
    prior_audit = read('l132-critical-audit.json')
    assert prior_audit['failures'] == [] and prior_audit['original_artifacts_byte_unchanged']
    assert all(c['passes'] for c in prior_audit['checks'])
    old = bound('residual-locus-reuse.json', prior_audit['input_sha256']['residual-locus-reuse.json'])
    old_replay = bound('residual-locus-reuse-replay.json', prior_audit['input_sha256']['residual-locus-reuse-replay.json'])
    assert old['failures'] == old_replay['failures'] == []
    assert old_replay['certificate_sha256'] == HASHES['residual-locus-reuse.json']
    assert old['unmatched_indices'] == old_replay['unmatched_indices']
    mismatch_domain = old['unmatched_indices']
    assert len(mismatch_domain) == len(set(map(tuple, mismatch_domain))) == 118
    assert mismatch_domain.count([94, 355]) == 1
    expected_scope = [x for x in mismatch_domain if x != [94, 355]]
    assert len(expected_scope) == 117
    scope_set = set(map(tuple, expected_scope))
    audit = read('l125-critical-audit.json')
    assert audit['failures'] == [] and audit['original_artifacts_byte_unchanged']
    assert audit['full_saved_replay_identical']
    for name in ('verify_new_pair_filter.py', 'verify_fixed_three_row_extensions.py'):
        assert sha256(raw(name)).hexdigest() == audit['audited_input_hashes'][name]
    for name in ('../../lemmas/L109-seven-coordinate-parameter-free-support-filter.md',
                 '../../lemmas/L125-new-pair-rank-factor-activity-partition.md',
                 '../../lemmas/L132-residual-literal-locus-row-imports.md',
                 '../../lemmas/L133-first-unmatched-residual-full-gate-exclusion.md'):
        raw(name)
    master = bound('new-pair-filter.json', audit['audited_input_hashes']['new-pair-filter.json'])
    replay = bound('new-pair-filter-replay.json', audit['audited_input_hashes']['new-pair-filter-replay.json'])
    assert replay['failures'] == master['failures'] == []
    assert replay['source_sha256'] == HASHES['new-pair-filter.json']
    assert replay['thirds'] == master['thirds'] and replay['summary'] == master['summary'] == audit['summary']
    universe = [[list(i), list(k)] for i in combinations(S, 2) for k in combinations(J, 2)]
    assert master['universe'] == universe and len(universe) == 756
    assert master['S'] == S and master['J'] == J and master['H'] == H
    assert master['column_pairs'] == [[S[a], S[b]] for a, b in PAIRS]
    assert master['first_two'] == [[[1, 8], [47, 50]], [[12, 18], [64, 75]]]
    historical = master['residual_occurrences']
    assert len(historical) == len({tuple(x) for x in historical}) == 154
    assert historical == sorted(historical)
    assert master['summary']['statuses']['residual'] == 154
    assert old['historical_residual_occurrences'] == historical
    assert mismatch_domain == [r['indices'] for r in old['overlay'] if r['disposition'] == 'unmatched']
    sources = [source('L133', 'first-unmatched-locus-gates', 'l133-critical-audit.json', [0, 0])]
    by_third = {}
    for n, u in historical:
        by_third.setdefault(n, []).append(u)
    assert len(by_third) == 54
    metas = {meta['third_index']: meta for meta in master['thirds']}
    overlay, frozen = [], []
    for n, expected_indices in by_third.items():
        meta = metas[n]
        shard_name = meta['certificate']
        shard = bound(shard_name, meta['sha256'])
        assert HASHES[shard_name] == audit['audited_input_hashes'][shard_name]
        assert shard['third_index'] == n and shard['failures'] == []
        assert shard['residual_indices'] == expected_indices
        residuals = [(pos, case) for pos, case in enumerate(shard['cases']) if case['status'] == 'residual']
        assert [case['fourth_index'] for pos, case in residuals] == expected_indices
        for pos, case in residuals:
            u = case['fourth_index']
            frozen.append([n, u])
            if (n, u) not in scope_set:
                continue
            prior_entry = next(r for r in old['overlay'] if r['indices'] == [n, u])
            assert prior_entry['disposition'] == 'unmatched'
            assert prior_entry['shard'] == shard_name and prior_entry['case_pointer'] == f'/cases/{pos}'
            assert prior_entry['complete_original_record'] == case
            row_indices = master['first_indices'] + [n, u]
            rows = [{'I': universe[v][0], 'K': universe[v][1]} for v in row_indices]
            supports = [set(r['I']+r['K']) for r in rows]
            assert len({tuple(sorted(a)) for a in supports}) == 4
            assert all(len(a & b) <= 1 for a, b in combinations(supports, 2))
            row_inputs = [inputs(row) for row in rows]
            blocks = [item['original_block'] for item in row_inputs]
            assert blocks == [master['blocks'][v] for v in row_indices]
            matrix = [r for block in blocks for r in block['matrix']]
            pivots, basis = column_kernel(matrix)
            assert pivots == case['pivot_columns'] and basis == case['kernel_basis']
            rank = case['rank']
            assert len(pivots) == rank and len(basis) == 21-rank
            minor = [[matrix[r][c] for c in pivots] for r in case['minor_rows']]
            assert len(minor) == rank and determinant(minor) == case['minor_residue'] != 0
            residuals_checked = [[sum(a*b for a, b in zip(v, r)) % P for r in matrix] for v in basis]
            assert residuals_checked == case['kernel_residuals'] and not any(map(any, residuals_checked))
            comparisons = []
            for src in sources:
                equal = basis == src['kernel_basis']
                mismatch = None
                if not equal:
                    if len(basis) != len(src['kernel_basis']):
                        mismatch = {'kind': 'basis_length', 'actual': len(basis), 'source': len(src['kernel_basis'])}
                    else:
                        a, b = next((a, b) for a in range(len(basis)) for b in range(21)
                                    if basis[a][b] != src['kernel_basis'][a][b])
                        mismatch = {'kind': 'basis_entry', 'basis_index': a, 'column': b,
                                    'actual': basis[a][b], 'source': src['kernel_basis'][a][b]}
                point_bindings = []
                if equal:
                    for binding in src['point_bindings']:
                        j = binding['source_row_number']-1
                        identical = row_inputs[j] == binding['row_input']
                        point_bindings.append({'source_point_index': binding['source_point_index'],
                                               'target_row_number': j+1, 'complete_row_input_equal': identical})
                comparisons.append({'source': src['lemma'], 'literal_ordered_basis_equal': equal,
                                    'mismatch': mismatch, 'point_row_bindings': point_bindings,
                                    'covered': equal and len(point_bindings) == 2
                                    and all(b['complete_row_input_equal'] for b in point_bindings)})
            overlay.append({'indices': [n, u], 'rows': rows, 'rank': rank,
                            'shard': shard_name, 'case_pointer': f'/cases/{pos}',
                            'complete_original_record': case,
                            'comparisons': comparisons,
                            'disposition': 'covered' if any(c['covered'] for c in comparisons) else 'unmatched'})
    assert frozen == historical
    assert [r['indices'] for r in overlay] == expected_scope
    matched = [r['indices'] for r in overlay if r['disposition'] == 'covered']
    unmatched = [r['indices'] for r in overlay if r['disposition'] == 'unmatched']
    summary = {'historical_residuals_preserved': 154, 'excluded_scope_indices': 154-len(overlay),
               'actual_tested': len(overlay), 'required_tested': len(expected_scope),
               'literal_basis_comparisons': len(overlay),
               'literal_matches_by_source': {s['lemma']: sum(c['literal_ordered_basis_equal']
                   for r in overlay for c in r['comparisons'] if c['source'] == s['lemma']) for s in sources},
               'covered_occurrences': len(matched), 'unmatched_occurrences': len(unmatched),
               'matched_point_row_bindings': sum(len(c['point_row_bindings']) for r in overlay
                                                for c in r['comparisons'] if c['covered']),
               'rank_histogram_in_scope': dict(sorted(Counter(r['rank'] for r in overlay).items()))}
    for name, expected in list(HASHES.items()):
        assert sha256((HERE/name).read_bytes()).hexdigest() == expected
    output = {'step_id': '2026-10-21-mca-392-l133-literal-reuse-test',
              'scope': 'Literal complete ordered-kernel and unchanged rejecting-row imports only; no assembly.',
              'input_sha256': HASHES, 'code_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
              'historical_residual_occurrences': historical,
              'historical_l132_mismatches': mismatch_domain, 'removed_only': [[94, 355]],
              'required_scope_indices': expected_scope, 'source_imports': sources,
              'overlay': overlay, 'covered_indices': matched, 'unmatched_indices': unmatched,
              'summary': summary, 'original_inputs_unchanged': True, 'failures': [],
              'limitations': 'L125/L132/L133 audited evidence reused; shared Python/residue arithmetic; separate audit pending. Unmatched does not imply feasible.'}
    path = HERE/'l133-literal-reuse.json'
    path.write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps(summary, sort_keys=True))
    print(f'Actual/required residuals {len(overlay)}/{len(expected_scope)}; '
          f'covered {len(matched)}; unmatched {len(unmatched)}; failures 0; certificate: {path}')


if __name__ == '__main__':
    run()
