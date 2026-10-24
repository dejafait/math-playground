"""Independent full binding replay; does not import the overlay producer.

Run: python3 -B scripts/seven-coordinate/verify_l137_literal_reuse.py
"""
from collections import Counter
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json

P = 97
HERE = Path(__file__).resolve().parent


def load(name):
    return json.loads((HERE/name).read_bytes())


def rref(matrix):
    a = [r[:] for r in matrix]
    pivots = []
    for c in range(len(a[0])):
        r = len(pivots)
        if r == len(a):
            break
        pivot = next((j for j in range(r, len(a)) if a[j][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inverse = pow(a[r][c], -1, P)
        a[r] = [x*inverse % P for x in a[r]]
        for j in range(len(a)):
            if j != r:
                scale = a[j][c]
                a[j] = [(x-scale*y) % P for x, y in zip(a[j], a[r])]
        pivots.append(c)
    basis = []
    for c in range(len(a[0])):
        if c not in pivots:
            v = [int(j == c) for j in range(len(a[0]))]
            for j, pivot in enumerate(pivots):
                v[pivot] = -a[j][c] % P
            basis.append(v)
    return pivots, basis


def det(matrix):
    a = [r[:] for r in matrix]
    value = 1
    for c in range(len(a)):
        r = next((r for r in range(c, len(a)) if a[r][c]), None)
        if r is None:
            return 0
        if r != c:
            a[r], a[c] = a[c], a[r]
            value = -value
        pivot = a[c][c]
        value = value*pivot % P
        for r in range(c+1, len(a)):
            scale = a[r][c]*pow(pivot, -1, P) % P
            a[r] = [(x-scale*y) % P for x, y in zip(a[r], a[c])]
    return value % P


def run():
    if not __debug__:
        raise RuntimeError('Run with assertions enabled')
    path = HERE/'l137-literal-reuse.json'
    report = json.loads(path.read_bytes())
    assert report['failures'] == [] and report['original_inputs_unchanged']
    for name, expected in report['input_sha256'].items():
        assert sha256((HERE/name).read_bytes()).hexdigest() == expected, name
    assert report['code_sha256'] == sha256((HERE/'l137_literal_reuse.py').read_bytes()).hexdigest()
    master = load('new-pair-filter.json')
    s, j = master['S'], master['J']
    h = [x for x in range(1, P) if pow(x, 16, P) == 1]
    assert h == master['H']
    universe = [[list(i), list(k)] for i in combinations(s, 2) for k in combinations(j, 2)]
    assert universe == master['universe']
    columns = list(combinations(range(7), 2))
    assert master['column_pairs'] == [[s[a], s[b]] for a, b in columns]
    historical = master['residual_occurrences']
    assert report['historical_residual_occurrences'] == historical
    assert len(historical) == len(set(map(tuple, historical))) == 154
    prior = load('l135-literal-reuse.json')
    prior_audit = load('l136-critical-audit.json')
    assert prior_audit['failures'] == [] and all(c['passes'] for c in prior_audit['checks'])
    assert sha256((HERE/'l135-literal-reuse.json').read_bytes()).hexdigest() == prior_audit['input_sha256']['l135-literal-reuse.json']
    assert report['historical_l136_mismatches'] == prior['unmatched_indices']
    assert report['historical_l132_mismatches'] == prior['historical_l132_mismatches']
    assert report['historical_l134_mismatches'] == prior['historical_l134_mismatches']
    assert len(report['historical_l134_mismatches']) == 100
    assert len(report['historical_l132_mismatches']) == 118
    assert len(prior['unmatched_indices']) == 82 and prior['unmatched_indices'].count([175,238]) == 1
    expected = [x for x in prior['unmatched_indices'] if x != [175,238]]
    assert len(expected) == 81 and report['required_scope_indices'] == expected
    assert report['removed_only'] == [[175,238]]
    assert [r['indices'] for r in report['overlay']] == expected
    # Derivative identity reconstructs g on S union K without the producer's product path.
    def row_input(i, k):
        retained = s+k
        values = {}
        for x in retained:
            denominator = 1
            for y in retained:
                if y != x:
                    denominator = denominator*(x-y) % P
            values[x] = 16*pow(x, 15, P)*pow(denominator, -1, P) % P
            assert values[x]
        z = min(set(s)-set(i))
        observed = [x for x in s if x not in i and x != z]
        q = [[(values[z]*int(y == x)-values[x]*int(y == z)) % P for y in s]
             for x in observed]
        rows = [[(a[x]*b[y]-a[y]*b[x]) % P for x, y in columns]
                for a, b in combinations(q, 2)]
        roots = sorted(set(j)-set(k))
        # Coefficient expansion by elementary symmetric sums; no iterative multiplication.
        coefficients = [sum(((-1)**(len(roots)-degree)) *
                            product(t) for t in combinations(roots, len(roots)-degree)) % P
                        for degree in range(len(roots)+1)]
        return {'I': i, 'K': k, 'z': z, 'g_roots': roots,
                'g_coefficients_ascending': coefficients,
                'g_values_on_S_union_K': {str(x): values[x] for x in retained},
                'original_block': {'I': i, 'K': k, 'pivot': z, 'covectors': q, 'matrix': rows}}

    sources = {}
    for imported in report['source_imports']:
        source = load(imported['certificate'])
        audit_source = load(imported['audit'])
        assert audit_source['failures'] == [] and all(c['passes'] for c in audit_source['checks'])
        for name, expected_hash in audit_source['input_sha256'].items():
            assert sha256((HERE/name).read_bytes()).hexdigest() == expected_hash
        replay_source = load(imported['replay'])
        assert replay_source['certificate_sha256'] == sha256((HERE/imported['certificate']).read_bytes()).hexdigest()
        assert imported['kernel_basis'] == source['kernel_basis']
        assert imported['imported_locus'] == {key: source[key] for key in imported['imported_locus']}
        assert imported['imported_locus']['complete_projective_parameter_locus'] == [[1, 0], [0, 1]]
        assert len(imported['imported_locus']['plucker_coefficients_s2_st_t2']) == 35
        for pi, binding in enumerate(imported['point_bindings']):
            assert binding['source_point_index'] == pi
            ri = binding['source_row_number']-1
            row = source['rows'][ri]
            assert binding['row_input'] == row_input(row['I'], row['K'])
            point = source['points_and_all_row_gates'][pi]
            assert binding['plane_representative'] == {key: point[key] for key in binding['plane_representative']}
            assert binding['unchanged_rejecting_gate'] == point['row_gates'][ri]
            assert binding['all_nonzero_pivot_replay'] == [r for r in replay_source['all_pivot_replay']
                if r['point'] == pi and r['row'] == ri+1]
            assert binding['original_row_replay'] == next(r for r in replay_source['all_row_replay']
                if r['point_index'] == pi and r['row_number'] == ri+1)
            assert all(r['scalar'] and r['lambda_value'] == 0 for r in binding['all_nonzero_pivot_replay'])
            gate = binding['unchanged_rejecting_gate']
            assert gate['passes'] is False and 'lambda_zero' in gate['failed_gates']
            assert not any(gate['moment_residuals'])
            assert not any(gate['h_minus_error_minus_lambda_g_on_H'])
            alpha, beta = gate['direction_coefficients']
            assert gate['prescribed_finite_gate'] == {'D_coefficient': alpha, 'C_coefficient': -beta % P}
            assert gate['original_first_coefficient'] == '(D*alpha-C*beta)/(AD-BC)'
            assert gate['original_basis_convention'] == 'u_original=A*u+B*v; v_original=C*u+D*v; AD-BC!=0'
            assert gate['projection_rank'] == 1 and gate['lambda_value'] == 0
            assert gate['error_weights'][2:] == [0, 0]
        sources[imported['lemma']] = imported
    assert set(sources) == {'L137'}
    assert len(report['source_imports']) == 1
    assert all(b['source_row_number'] == 1 for b in report['source_imports'][0]['point_bindings'])
    shard_cache = {}
    matched, unmatched = [], []
    count_by_source = Counter({'L137': 0})
    original_entries, null_entries, point_bindings = 0, 0, 0
    for entry in report['overlay']:
        n, u = entry['indices']
        if n not in shard_cache:
            shard_cache[n] = load(entry['shard'])
        shard = shard_cache[n]
        position = int(entry['case_pointer'].split('/')[-1])
        record = shard['cases'][position]
        prior_entry = next(r for r in prior['overlay'] if r['indices'] == [n,u])
        assert prior_entry['disposition'] == 'unmatched'
        assert prior_entry['complete_original_record'] == record == entry['complete_original_record']
        assert prior_entry['shard'] == entry['shard'] and prior_entry['case_pointer'] == entry['case_pointer']
        assert record['fourth_index'] == u and record['status'] == 'residual'
        rows = [{'I': universe[v][0], 'K': universe[v][1]}
                for v in master['first_indices']+[n, u]]
        assert entry['rows'] == rows
        input_rows = [row_input(row['I'], row['K']) for row in rows]
        matrix = [r for row in input_rows for r in row['original_block']['matrix']]
        assert matrix == [r for v in master['first_indices']+[n, u] for r in master['blocks'][v]['matrix']]
        pivots, basis = rref(matrix)
        assert pivots == record['pivot_columns'] and basis == record['kernel_basis']
        assert len(pivots) == record['rank'] == entry['rank']
        minor = [[matrix[r][c] for c in pivots] for r in record['minor_rows']]
        assert det(minor) == record['minor_residue'] != 0
        assert [[sum(a*b for a, b in zip(v, r)) % P for r in matrix] for v in basis] == record['kernel_residuals']
        assert not any(map(any, record['kernel_residuals']))
        original_entries += 504
        null_entries += 24*len(basis)
        assert [c['source'] for c in entry['comparisons']] == ['L137']
        any_covered = False
        for comparison in entry['comparisons']:
            src = sources[comparison['source']]
            equal = basis == src['kernel_basis']
            assert comparison['literal_ordered_basis_equal'] == equal
            if equal:
                count_by_source[comparison['source']] += 1
                assert comparison['mismatch'] is None
                bindings = []
                for binding in src['point_bindings']:
                    row = binding['source_row_number']-1
                    identical = input_rows[row] == binding['row_input']
                    bindings.append({'source_point_index': binding['source_point_index'],
                                     'target_row_number': row+1, 'complete_row_input_equal': identical})
                assert bindings == comparison['point_row_bindings']
                covered = all(b['complete_row_input_equal'] for b in bindings)
                point_bindings += len(bindings) if covered else 0
            else:
                assert comparison['point_row_bindings'] == []
                mismatch = comparison['mismatch']
                if len(basis) != len(src['kernel_basis']):
                    assert mismatch == {'kind': 'basis_length', 'actual': len(basis), 'source': len(src['kernel_basis'])}
                else:
                    a, b = next((a, b) for a in range(len(basis)) for b in range(21)
                                if basis[a][b] != src['kernel_basis'][a][b])
                    assert mismatch == {'kind': 'basis_entry', 'basis_index': a, 'column': b,
                                        'actual': basis[a][b], 'source': src['kernel_basis'][a][b]}
                covered = False
            assert comparison['covered'] == covered
            any_covered |= covered
        assert entry['disposition'] == ('covered' if any_covered else 'unmatched')
        (matched if any_covered else unmatched).append([n, u])
    assert report['covered_indices'] == matched and report['unmatched_indices'] == unmatched
    summary = {'historical_residuals_preserved': 154, 'excluded_scope_indices': 154-81,
               'actual_tested': len(expected), 'required_tested': 81, 'literal_basis_comparisons': 81,
               'literal_matches_by_source': dict(count_by_source), 'covered_occurrences': len(matched),
               'unmatched_occurrences': len(unmatched), 'matched_point_row_bindings': point_bindings,
               'rank_histogram_in_scope': {str(k): v for k, v in sorted(Counter(r['rank'] for r in report['overlay']).items())}}
    assert summary == report['summary']
    assert len(matched)+len(unmatched) == 81 and point_bindings == 2*len(matched)
    result = {'certificate_sha256': sha256(path.read_bytes()).hexdigest(),
              'verifier_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
              'summary': summary, 'original_entries_rebuilt': original_entries,
              'null_residual_entries_replayed': null_entries,
              'covered_indices': matched, 'unmatched_indices': unmatched, 'failures': [],
              'limitations': 'Same-step independent binding replay; shared Python/residue arithmetic. Audited source loci/gates reused, no new loci or assembly.'}
    out = HERE/'l137-literal-reuse-replay.json'
    out.write_text(json.dumps(result, indent=2)+'\n')
    print(f'Replayed {len(expected)}/81 occurrences; {original_entries} original entries; '
          f'{null_entries} null residual entries; {len(matched)} matched, {len(unmatched)} unmatched; '
          f'{point_bindings}/{2*len(matched)} point-row bindings; failures 0; certificate: {out}')


def product(values):
    result = 1
    for value in values:
        result *= value
    return result


if __name__ == '__main__':
    run()
