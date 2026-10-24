"""Exactly 25 approved original records; literal L147/unchanged-row reuse only."""
from collections import Counter
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json
import l139_literal_reuse as reuse

HERE = Path(__file__).resolve().parent
REMOVED = [[274, 539]]


def checked_audit(name):
    audit = reuse.read(name)
    assert audit['failures'] == [] and audit['original_artifacts_byte_unchanged']
    if name == 'l125-critical-audit.json':
        assert audit['full_saved_replay_identical']
        assert audit['summary']['actual_cases'] == audit['summary']['required_cases'] == 100764
    else:
        checks = audit['checks']
        assert (all(checks.values()) if isinstance(checks, dict)
                else all(c.get('passes', c.get('passed', False)) for c in checks))
    return audit


def run():
    assert __debug__
    original_audit = checked_audit('l125-critical-audit.json')
    assert original_audit['full_saved_replay_identical']
    prior_audit = checked_audit('l146-critical-audit.json')
    for name, value in prior_audit['input_sha256'].items():
        assert sha256(reuse.raw(name)).hexdigest() == value, name
    for name in ('verify_new_pair_filter.py', 'verify_fixed_three_row_extensions.py'):
        assert sha256(reuse.raw(name)).hexdigest() == original_audit['audited_input_hashes'][name]
    reuse.raw('l139_literal_reuse.py')
    master = reuse.bound('new-pair-filter.json', original_audit['audited_input_hashes']['new-pair-filter.json'])
    prior = reuse.bound('l144-remaining-literal-reuse.json', prior_audit['input_sha256']['l144-remaining-literal-reuse.json'])
    prior_replay = reuse.bound('l144-remaining-literal-reuse-replay.json', prior_audit['input_sha256']['l144-remaining-literal-reuse-replay.json'])
    assert prior['failures'] == prior_replay['failures'] == master['failures'] == []
    assert prior_replay['certificate_sha256'] == reuse.HASHES['l144-remaining-literal-reuse.json']
    assert prior_replay['unmatched_indices'] == prior['unmatched_indices']
    historical = prior['unmatched_indices']
    assert len(historical) == len(set(map(tuple, historical))) == 26
    assert all(historical.count(x) == 1 for x in REMOVED)
    scope = [x for x in historical if x not in REMOVED]
    assert len(scope) == 25
    assert len(master['residual_occurrences']) == 154
    assert prior['historical_residual_occurrences'] == master['residual_occurrences']
    universe = [[list(i), list(k)] for i in combinations(reuse.S, 2) for k in combinations(reuse.J, 2)]
    assert universe == master['universe'] and len(universe) == 756
    assert master['column_pairs'] == [[reuse.S[a], reuse.S[b]] for a, b in reuse.PAIRS]
    source = reuse.source('L147', 'first-l146-mismatch-locus-gates', 'l147-critical-audit.json', [1, 1])
    assert all(b['source_row_number'] == 2 for b in source['point_bindings'])
    overlay, shards = [], {}
    for n, u in scope:
        previous = next(r for r in prior['overlay'] if r['indices'] == [n, u])
        assert previous['disposition'] == 'unmatched'
        name = previous['shard']
        if name not in shards:
            shards[name] = reuse.bound(name, original_audit['audited_input_hashes'][name])
            assert reuse.HASHES[name] == prior_audit['input_sha256'][name]
        shard = shards[name]
        pos = int(previous['case_pointer'].split('/')[-1])
        case = shard['cases'][pos]
        assert shard['third_index'] == n and case['fourth_index'] == u and case['status'] == 'residual'
        assert [r for r in shard['cases'] if r['fourth_index'] == u] == [case]
        assert previous['complete_original_record'] == case
        row_indices = master['first_indices'] + [n, u]
        rows = [dict(I=universe[v][0], K=universe[v][1]) for v in row_indices]
        assert rows == previous['rows']
        supports = [set(r['I']+r['K']) for r in rows]
        assert len(set(map(tuple, map(sorted, supports)))) == 4
        assert all(len(a & b) <= 1 for a, b in combinations(supports, 2))
        row_inputs = [reuse.inputs(row) for row in rows]
        assert [r['original_block'] for r in row_inputs] == [master['blocks'][v] for v in row_indices]
        matrix = [v for row in row_inputs for v in row['original_block']['matrix']]
        columns, basis = reuse.column_kernel(matrix)
        assert columns == case['pivot_columns'] and basis == case['kernel_basis']
        rank = len(columns)
        assert rank == case['rank'] and len(basis) == 21-rank
        free = sorted(set(range(21))-set(columns))
        assert [[v[c] for c in free] for v in basis] == [
            [int(a == b) for b in range(len(free))] for a in range(len(free))]
        residuals = [[sum(a*b for a, b in zip(v, r)) % 97 for r in matrix] for v in basis]
        assert residuals == case['kernel_residuals'] and not any(map(any, residuals))
        minor = [[matrix[r][c] for c in columns] for r in case['minor_rows']]
        assert len(case['minor_rows']) == len(set(case['minor_rows'])) == rank
        residue = reuse.determinant(minor)
        assert residue == case['minor_residue'] != 0
        equal = basis == source['kernel_basis']
        witness, bindings = None, []
        if equal:
            for binding in source['point_bindings']:
                assert row_inputs[1] == binding['row_input']
                bindings.append(binding)
        elif len(basis) != len(source['kernel_basis']):
            witness = dict(kind='basis_length', actual=len(basis), source=len(source['kernel_basis']))
        else:
            a, b = next((a, b) for a in range(len(basis)) for b in range(21)
                        if basis[a][b] != source['kernel_basis'][a][b])
            witness = dict(kind='basis_entry', basis_index=a, column=b,
                           actual=basis[a][b], source=source['kernel_basis'][a][b])
        overlay.append(dict(indices=[n, u], shard=name, case_pointer=previous['case_pointer'],
            complete_original_record=case, complete_prior_overlay=previous, rows=rows,
            row_inputs=row_inputs, original_matrix=matrix, rank=rank,
            rank_minor_rows=case['minor_rows'], rank_minor_columns=columns, rank_minor_residue=residue,
            free_columns=free, kernel_basis=basis, kernel_residuals=residuals,
            literal_complete_ordered_kernel_equal=equal, mismatch=witness, point_row_bindings=bindings,
            old_exchanged_family=[u, n] in REMOVED,
            disposition='covered' if equal and len(bindings) == 2 else 'unmatched'))
    assert [r['indices'] for r in overlay] == scope
    covered = [r['indices'] for r in overlay if r['disposition'] == 'covered']
    unmatched = [r['indices'] for r in overlay if r['disposition'] == 'unmatched']
    exchanges = [r['indices'] for r in overlay if r['disposition'] == 'covered' and r['old_exchanged_family']]
    additional = [r for r in covered if r not in exchanges]
    additional_families = sorted({tuple(sorted(r)) for r in additional})
    assert len(additional) == 2*len(additional_families)
    assert all(list(r) in additional and list(reversed(r)) in additional for r in additional_families)
    summary = dict(actual_records=len(overlay), required_records=25,
        original_entries=504*len(overlay), null_residuals=sum(24*len(r['kernel_basis']) for r in overlay),
        nonzero_original_minors=len(overlay), literal_matches=len(covered), mismatches=len(unmatched),
        old_exchanges=len(exchanges), additional_ordered_bindings=len(additional),
        additional_unordered_families=len(additional_families),
        mismatch_witness_kinds=dict(sorted(Counter(r['mismatch']['kind'] for r in overlay if r['mismatch']).items())),
        matched_point_row_bindings=sum(len(r['point_row_bindings']) for r in overlay),
        required_matched_point_row_bindings=2*len(covered),
        rank_histogram=dict(sorted(Counter(r['rank'] for r in overlay).items())))
    for name, value in reuse.HASHES.items():
        assert sha256((HERE/name).read_bytes()).hexdigest() == value, name
    report = dict(step_id='2026-10-24-mca-449-l147-literal-reuse',
        input_sha256=reuse.HASHES, code_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
        historical_residual_occurrences=master['residual_occurrences'], historical_l146_mismatches=historical,
        removed_only=REMOVED, required_scope_indices=scope, source=source, overlay=overlay,
        covered_indices=covered, unmatched_indices=unmatched, old_exchange_indices=exchanges,
        additional_ordered_indices=additional, additional_unordered_families=additional_families,
        summary=summary, original_inputs_unchanged=True, failures=[],
        qualification='Literal audited locus/unchanged second-row imports only. No new locus, changed-row algebra, assembly or global improvement. Separate critical audit pending.')
    out = HERE/'l147-literal-reuse.json'
    out.write_text(json.dumps(report, indent=2)+'\n')
    print(f'Records {len(overlay)}/25; nonzero minors {len(overlay)}/25; literal matches {len(covered)}; '
          f'old exchanges {len(exchanges)}; additional ordered {len(additional)}; mismatches {len(unmatched)}; '
          f'bindings {summary["matched_point_row_bindings"]}/{2*len(covered)}; failures 0; {out}')


if __name__ == '__main__':
    run()
