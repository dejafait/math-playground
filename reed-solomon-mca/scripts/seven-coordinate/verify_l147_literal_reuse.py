"""Full derivative/row-elimination replay; imports no comparison producer."""
from collections import Counter
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json
from verify_l139_literal_reuse import rref, det, product

HERE = Path(__file__).resolve().parent
P = 97
S = [1, 8, 12, 18, 22, 27, 33]
H = [x for x in range(1, P) if pow(x, 16, P) == 1]
J = sorted(set(H)-set(S))
PAIRS = list(combinations(range(7), 2))


def load(name):
    return json.loads((HERE/name).read_bytes())


def row_input(i, k):
    values = {}
    for x in S+k:
        denominator = product(x-y for y in S+k if y != x) % P
        assert denominator
        values[x] = 16*pow(x, 15, P)*pow(denominator, -1, P) % P
        assert values[x]
    z = min(set(S)-set(i))
    q = [[((int(y == x)*pow(values[x], -1, P)-int(y == z)*pow(values[z], -1, P))
           *values[x]*values[z]) % P for y in S] for x in S if x not in i and x != z]
    matrix = [[(a[x]*b[y]-a[y]*b[x]) % P for x, y in PAIRS] for a, b in combinations(q, 2)]
    roots = [y for y in J if y not in k]
    coefficients = [sum((-1)**(len(roots)-d)*product(t)
                        for t in combinations(roots, len(roots)-d)) % P for d in range(len(roots)+1)]
    return dict(I=i, K=k, z=z, g_roots=roots, g_coefficients_ascending=coefficients,
        g_values_on_S_union_K={str(x): v for x, v in values.items()},
        original_block=dict(I=i, K=k, pivot=z, covectors=q, matrix=matrix))


def verify_binding(binding, pi, inp, basis, source, replay):
    """Reconstruct the entire identical row at this exhaustive source point."""
    point = source['points_and_all_row_gates'][pi]
    gate = point['row_gates'][1]
    assert binding['source_point_index'] == pi and binding['source_row_number'] == 2
    assert binding['row_input'] == inp == row_input(source['rows'][1]['I'], source['rows'][1]['K'])
    assert binding['unchanged_rejecting_gate'] == gate
    assert binding['plane_representative'] == {key: point[key] for key in ('u', 'v', 'bivector', 'pivot_indices')}
    u, v = point['u'], point['v']
    assert [(u[a]*v[b]-u[b]*v[a]) % P for a, b in PAIRS] == basis[pi] == point['bivector']
    q = inp['original_block']['covectors']
    qu, qv = [[sum(a*b for a, b in zip(c, w)) % P for c in q] for w in (u, v)]
    assert qu == gate['Q_u'] and qv == gate['Q_v']
    assert [(qu[a]*qv[b]-qu[b]*qv[a]) % P for a, b in combinations(range(4), 2)] == gate['projection_minors'] == [0]*6
    n = next(n for n in range(4) if qu[n] or qv[n])
    alpha, beta = -qv[n] % P, qu[n]
    hh = [(alpha*a+beta*b) % P for a, b in zip(u, v)]
    vals = {int(x): value for x, value in inp['g_values_on_S_union_K'].items()}
    lam = hh[S.index(inp['z'])]*pow(vals[inp['z']], -1, P) % P
    error = [(hh[S.index(x)]-lam*vals[x]) % P for x in inp['I']]+[-lam*vals[x] % P for x in inp['K']]
    assert gate['projection_rank'] == 1 and gate['direction_coefficients'] == [alpha, beta]
    assert gate['intersection_vector'] == hh and gate['lambda_value'] == lam == 0
    assert gate['error_weights'] == error and gate['overlap_weights'] == error[:2]
    assert error[2:] == [0, 0] and gate['passes'] is False
    assert gate['failed_gates'] == ['lambda_zero']+['overlap_weight_zero_at_'+str(x) for x, e in zip(inp['I'], error) if not e]
    edict = dict(zip(inp['I']+inp['K'], error))
    moments = [(sum(hh[n]*pow(x, d, P) for n, x in enumerate(S))-
                sum(e*pow(x, d, P) for x, e in edict.items())) % P for d in range(1, 9)]
    pointwise = [((hh[S.index(x)] if x in S else 0)-edict.get(x, 0)-lam*product(x-y for y in inp['g_roots'])) % P for x in H]
    assert moments == gate['moment_residuals'] == [0]*8
    assert pointwise == gate['h_minus_error_minus_lambda_g_on_H'] == [0]*16
    assert gate['g_values_on_S_union_K'] == inp['g_values_on_S_union_K']
    assert gate['prescribed_finite_gate'] == dict(D_coefficient=alpha, C_coefficient=-beta % P)
    assert gate['original_first_coefficient'] == '(D*alpha-C*beta)/(AD-BC)'
    assert gate['original_basis_convention'] == 'u_original=A*u+B*v; v_original=C*u+D*v; AD-BC!=0'
    replay_row = dict(point_index=pi, row_number=2, Q_u=qu, Q_v=qv, h=hh,
        error={str(x): e for x, e in edict.items()}, moments=moments,
        finite_gate_coefficients_D_C=[alpha, -beta % P])
    replay_row['lambda'] = lam
    assert binding['original_row_replay'] == replay_row
    assert replay_row == next(r for r in replay['all_row_replay'] if r['point_index'] == pi and r['row_number'] == 2)
    skew = [[0]*7 for _ in range(7)]
    for (a, b), value in zip(PAIRS, basis[pi]):
        skew[a][b], skew[b][a] = value, -value % P
    pivots = []
    for (a, b), value in zip(PAIRS, basis[pi]):
        if not value:
            continue
        uu = [skew[x][b]*pow(value, -1, P) % P for x in range(7)]
        vv = skew[a]
        assert [(uu[x]*vv[y]-uu[y]*vv[x]) % P for x, y in PAIRS] == basis[pi]
        qa, qb = [[sum(x*y for x, y in zip(c, w)) % P for c in q] for w in (uu, vv)]
        for n in range(4):
            if not (qa[n] or qb[n]):
                continue
            aa, bb = -qb[n] % P, qa[n]
            hv = [(aa*x+bb*y) % P for x, y in zip(uu, vv)]
            ix = next(x for x, w in enumerate(hh) if w)
            scalar = hv[ix]*pow(hh[ix], -1, P) % P
            assert scalar and hv == [scalar*x % P for x in hh]
            alternative_lambda = hv[S.index(inp['z'])]*pow(vals[inp['z']], -1, P) % P
            alternative_error = [(hv[S.index(x)]-alternative_lambda*vals[x]) % P for x in inp['I']]+[-alternative_lambda*vals[x] % P for x in inp['K']]
            assert alternative_lambda == 0 and alternative_error == [scalar*x % P for x in error]
            pivots.append(dict(point=pi, exterior_pivot=[a, b], row=2, projection_component=n,
                direction=[aa, bb], scalar=scalar, h=hv, lambda_value=alternative_lambda, error_weights=alternative_error))
    assert pivots == binding['all_nonzero_pivot_replay'] == [r for r in replay['all_pivot_replay'] if r['point'] == pi and r['row'] == 2]
    return dict(source_point=pi, row=2, lambda_value=lam, weights=error, moments=moments,
                pointwise=pointwise, alternative_pivots=pivots)


def run():
    assert __debug__
    path = HERE/'l147-literal-reuse.json'
    report = json.loads(path.read_bytes())
    assert report['failures'] == [] and report['original_inputs_unchanged']
    for name, value in report['input_sha256'].items():
        assert sha256((HERE/name).read_bytes()).hexdigest() == value, name
    assert report['code_sha256'] == sha256((HERE/'l147_literal_reuse.py').read_bytes()).hexdigest()
    master, prior = load('new-pair-filter.json'), load('l144-remaining-literal-reuse.json')
    audits = {name: load(name) for name in ('l125-critical-audit.json', 'l146-critical-audit.json',
                                          'l147-critical-audit.json')}
    for name, audit in audits.items():
        assert audit['failures'] == [] and audit['original_artifacts_byte_unchanged']
        if name == 'l125-critical-audit.json':
            assert audit['full_saved_replay_identical']
            assert audit['summary']['actual_cases'] == audit['summary']['required_cases'] == 100764
        else:
            assert all(c['passes'] for c in audit['checks'])
    for name in ('l146-critical-audit.json', 'l147-critical-audit.json'):
        for artifact, value in audits[name]['input_sha256'].items():
            assert sha256((HERE/artifact).read_bytes()).hexdigest() == value
    for artifact in ('new-pair-filter.json', 'verify_new_pair_filter.py', 'verify_fixed_three_row_extensions.py'):
        assert sha256((HERE/artifact).read_bytes()).hexdigest() == audits['l125-critical-audit.json']['audited_input_hashes'][artifact]
    prior_audit = audits['l146-critical-audit.json']
    assert sha256((HERE/'l144-remaining-literal-reuse.json').read_bytes()).hexdigest() == prior_audit['input_sha256']['l144-remaining-literal-reuse.json']
    prior_replay = load('l144-remaining-literal-reuse-replay.json')
    assert prior_replay['certificate_sha256'] == sha256((HERE/'l144-remaining-literal-reuse.json').read_bytes()).hexdigest()
    assert prior_replay['unmatched_indices'] == prior['unmatched_indices']
    assert master['S'] == S and master['H'] == H and master['J'] == J
    universe = [[list(a), list(b)] for a in combinations(S, 2) for b in combinations(J, 2)]
    assert universe == master['universe']
    assert master['column_pairs'] == [[S[a], S[b]] for a, b in PAIRS]
    historical = prior['unmatched_indices']
    assert len(historical) == len(set(map(tuple, historical))) == 26
    removed = [[274, 539]]
    assert all(historical.count(x) == 1 for x in removed)
    scope = [r for r in historical if r not in removed]
    assert len(scope) == 25 and report['required_scope_indices'] == scope and report['removed_only'] == removed
    assert report['historical_l146_mismatches'] == historical
    assert report['historical_residual_occurrences'] == prior['historical_residual_occurrences'] == master['residual_occurrences']
    assert len(master['residual_occurrences']) == 154
    assert [r['indices'] for r in report['overlay']] == scope
    source, source_replay = load('first-l146-mismatch-locus-gates.json'), load('first-l146-mismatch-locus-gates-replay.json')
    imported = report['source']
    assert imported['lemma'] == 'L147' and imported['kernel_basis'] == source['kernel_basis']
    assert imported['imported_locus'] == {key: source[key] for key in imported['imported_locus']}
    assert source['complete_projective_parameter_locus'] == [[1, 0], [0, 1]] and source['infinity_is_decomposable']
    assert len(imported['imported_locus']['plucker_coefficients_s2_st_t2']) == 35
    assert source_replay['certificate_sha256'] == sha256((HERE/imported['certificate']).read_bytes()).hexdigest()
    assert source['failures'] == source_replay['failures'] == []
    assert source_replay['plucker_coefficients_s2_st_t2'] == source['plucker_coefficients_s2_st_t2']
    assert len(imported['point_bindings']) == 2
    # Validate both full reference bindings independently, then replay them per match below.
    for pi, binding in enumerate(imported['point_bindings']):
        verify_binding(binding, pi, row_input(source['rows'][1]['I'], source['rows'][1]['K']),
                       source['kernel_basis'], source, source_replay)
    replayed, covered, unmatched, exchanges, shards = [], [], [], [], {}
    for entry in report['overlay']:
        n, u = entry['indices']
        name = entry['shard']
        if name not in shards:
            shards[name] = load(name)
            digest = sha256((HERE/name).read_bytes()).hexdigest()
            assert digest == audits['l125-critical-audit.json']['audited_input_hashes'][name] == prior_audit['input_sha256'][name]
        shard = shards[name]
        pos = int(entry['case_pointer'].split('/')[-1])
        case = shard['cases'][pos]
        previous = next(r for r in prior['overlay'] if r['indices'] == [n, u])
        assert entry['complete_prior_overlay'] == previous
        assert previous['disposition'] == 'unmatched' and previous['shard'] == name and previous['case_pointer'] == entry['case_pointer']
        assert case == previous['complete_original_record'] == entry['complete_original_record']
        assert shard['third_index'] == n and case['fourth_index'] == u and case['status'] == 'residual'
        assert [r for r in shard['cases'] if r['fourth_index'] == u] == [case]
        rows = [dict(I=universe[v][0], K=universe[v][1]) for v in master['first_indices']+[n, u]]
        assert rows == entry['rows'] == previous['rows']
        supports = [set(r['I']+r['K']) for r in rows]
        assert len(set(map(tuple, map(sorted, supports)))) == 4 and all(len(a & b) <= 1 for a, b in combinations(supports, 2))
        inputs = [row_input(r['I'], r['K']) for r in rows]
        assert inputs == entry['row_inputs']
        assert [r['original_block'] for r in inputs] == [master['blocks'][v] for v in master['first_indices']+[n, u]]
        matrix = [v for r in inputs for v in r['original_block']['matrix']]
        assert matrix == entry['original_matrix']
        columns, basis = rref(matrix)
        assert columns == case['pivot_columns'] == entry['rank_minor_columns']
        assert basis == case['kernel_basis'] == entry['kernel_basis']
        rank = len(columns)
        assert rank == case['rank'] == entry['rank'] and len(basis) == 21-rank
        free = sorted(set(range(21))-set(columns))
        assert free == entry['free_columns']
        assert [[v[c] for c in free] for v in basis] == [[int(a == b) for b in range(len(free))] for a in range(len(free))]
        minor_rows = entry['rank_minor_rows']
        assert minor_rows == case['minor_rows'] and len(minor_rows) == len(set(minor_rows)) == rank
        assert all(0 <= r < 24 for r in minor_rows)
        residue = det([[matrix[r][c] for c in columns] for r in minor_rows])
        assert residue == case['minor_residue'] == entry['rank_minor_residue'] != 0
        residuals = [[sum(a*b for a, b in zip(v, r)) % P for r in matrix] for v in basis]
        assert residuals == case['kernel_residuals'] == entry['kernel_residuals'] and not any(map(any, residuals))
        equal = basis == source['kernel_basis']
        assert equal == entry['literal_complete_ordered_kernel_equal']
        bindings = []
        if equal:
            assert entry['mismatch'] is None and entry['point_row_bindings'] == imported['point_bindings']
            for pi, binding in enumerate(entry['point_row_bindings']):
                bindings.append(verify_binding(binding, pi, inputs[1], basis, source, source_replay))
            assert len(bindings) == 2
        else:
            assert entry['point_row_bindings'] == []
            if len(basis) != len(source['kernel_basis']):
                witness = dict(kind='basis_length', actual=len(basis), source=len(source['kernel_basis']))
            else:
                a, b = next((a, b) for a in range(len(basis)) for b in range(21) if basis[a][b] != source['kernel_basis'][a][b])
                witness = dict(kind='basis_entry', basis_index=a, column=b, actual=basis[a][b], source=source['kernel_basis'][a][b])
            assert witness == entry['mismatch']
        assert entry['disposition'] == ('covered' if equal else 'unmatched')
        (covered if equal else unmatched).append([n, u])
        is_exchange = [u, n] in removed
        assert is_exchange == entry['old_exchanged_family']
        if equal and is_exchange:
            exchanges.append([n, u])
        replayed.append(dict(indices=[n, u], rebuilt_original_matrix=matrix, rank=rank,
            minor_residue=residue, free_columns=free, independently_reconstructed_kernel=basis,
            null_residuals=residuals, equal=equal, mismatch=entry['mismatch'], full_binding_replay=bindings))
    additional = [r for r in covered if r not in exchanges]
    additional_families = sorted({tuple(sorted(r)) for r in additional})
    assert len(additional) == 2*len(additional_families)
    assert all(list(r) in additional and list(reversed(r)) in additional for r in additional_families)
    assert report['additional_unordered_families'] == [list(r) for r in additional_families]
    summary = dict(actual_records=len(replayed), required_records=25, original_entries=504*len(replayed),
        null_residuals=sum(24*len(r['independently_reconstructed_kernel']) for r in replayed),
        nonzero_original_minors=len(replayed), literal_matches=len(covered), mismatches=len(unmatched),
        old_exchanges=len(exchanges), additional_ordered_bindings=len(additional),
        additional_unordered_families=len(additional_families),
        mismatch_witness_kinds=dict(sorted(Counter(r['mismatch']['kind'] for r in replayed if r['mismatch']).items())),
        matched_point_row_bindings=sum(len(r['full_binding_replay']) for r in replayed),
        required_matched_point_row_bindings=2*len(covered),
        rank_histogram={str(k): v for k, v in sorted(Counter(r['rank'] for r in replayed).items())})
    assert summary == report['summary'] and len(covered)+len(unmatched) == 25
    assert report['covered_indices'] == covered and report['unmatched_indices'] == unmatched
    assert report['old_exchange_indices'] == exchanges and report['additional_ordered_indices'] == additional
    binding_replays = [b for r in replayed for b in r['full_binding_replay']]
    result = dict(certificate_sha256=sha256(path.read_bytes()).hexdigest(),
        verifier_sha256=sha256(Path(__file__).read_bytes()).hexdigest(), summary=summary,
        complete_record_replay=replayed, covered_indices=covered, unmatched_indices=unmatched,
        projection_pivot_bindings=sum(len(b['alternative_pivots']) for b in binding_replays),
        original_moments=8*len(binding_replays), pointwise_entries=16*len(binding_replays), failures=[],
        qualification='Complete same-step derivative/row-elimination replay; shared Python/residue arithmetic. Audited locus imported, no new locus; separate critical audit pending.')
    out = HERE/'l147-literal-reuse-replay.json'
    out.write_text(json.dumps(result, indent=2)+'\n')
    print(f'Replayed {len(replayed)}/25; entries {summary["original_entries"]}; null residuals {summary["null_residuals"]}; '
          f'minors {len(replayed)}/25; matches {len(covered)}; mismatches {len(unmatched)}; '
          f'bindings {len(binding_replays)}/{2*len(covered)}; pivots {result["projection_pivot_bindings"]}; '
          f'moments {result["original_moments"]}; failures 0; {out}')


if __name__ == '__main__':
    run()
