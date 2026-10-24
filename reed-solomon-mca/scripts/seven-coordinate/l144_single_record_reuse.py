"""One approved literal L144 binding; no sweep or new locus computation."""
import json
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import l139_literal_reuse as reuse

HERE = Path(__file__).resolve().parent


def run():
    assert __debug__
    audit = reuse.read('l125-critical-audit.json')
    prior = reuse.read('l143-critical-audit.json')
    assert audit['failures'] == prior['failures'] == []
    assert audit['original_artifacts_byte_unchanged'] and audit['full_saved_replay_identical']
    assert prior['original_artifacts_byte_unchanged'] and all(c['passes'] for c in prior['checks'])
    for name in ('verify_new_pair_filter.py','verify_fixed_three_row_extensions.py'):
        assert sha256(reuse.raw(name)).hexdigest()==audit['audited_input_hashes'][name]
    reuse.raw('l139_literal_reuse.py')
    master = reuse.bound('new-pair-filter.json', audit['audited_input_hashes']['new-pair-filter.json'])
    shard_name = 'new-pair-filter/third-239.json'
    shard = reuse.bound(shard_name, audit['audited_input_hashes'][shard_name])
    assert reuse.HASHES[shard_name] == prior['input_sha256'][shard_name]
    old = reuse.bound('l141-l142-literal-reuse.json', prior['input_sha256']['l141-l142-literal-reuse.json'])
    case, overlay = shard['cases'][182], old['overlay'][1]
    assert shard['third_index'] == 239 and case['fourth_index'] == 647
    assert [r for r in shard['cases'] if r['fourth_index'] == 647] == [case]
    assert overlay['indices'] == [239,647] and overlay['complete_original_record'] == case
    assert overlay['case_pointer'] == '/cases/182' and overlay['shard'] == shard_name
    assert overlay['disposition'] == 'unmatched'
    assert len(master['residual_occurrences']) == 154 and len(old['unmatched_indices']) == 44
    universe = [[list(i),list(k)] for i in combinations(reuse.S,2) for k in combinations(reuse.J,2)]
    assert universe == master['universe']
    indices = master['first_indices']+[239,647]
    rows = [dict(I=universe[n][0],K=universe[n][1]) for n in indices]
    assert rows == overlay['rows']
    supports = [set(r['I']+r['K']) for r in rows]
    assert len(set(map(tuple,map(sorted,supports)))) == 4
    assert all(len(a&b)<=1 for a,b in combinations(supports,2))
    row_inputs = [reuse.inputs(r) for r in rows]
    assert [r['original_block'] for r in row_inputs] == [master['blocks'][n] for n in indices]
    matrix = [v for r in row_inputs for v in r['original_block']['matrix']]
    columns,basis = reuse.column_kernel(matrix)
    assert columns == case['pivot_columns'] and basis == case['kernel_basis']
    assert len(columns) == case['rank'] == 19 and len(basis) == 2
    free = sorted(set(range(21))-set(columns))
    assert [[b[c] for c in free] for b in basis] == [[1,0],[0,1]]
    residuals = [[sum(a*b for a,b in zip(v,r))%97 for r in matrix] for v in basis]
    assert residuals == case['kernel_residuals'] == [[0]*24]*2
    minor = [[matrix[r][c] for c in columns] for r in case['minor_rows']]
    residue = reuse.determinant(minor)
    assert len(minor) == 19 and residue == case['minor_residue'] != 0
    source = reuse.source('L144','first-l143-mismatch-locus-gates','l144-critical-audit.json',[1,1])
    equal = basis == source['kernel_basis']
    bindings = []
    if equal:
        for binding in source['point_bindings']:
            assert row_inputs[1] == binding['row_input']
            bindings.append(binding)
    for name,value in reuse.HASHES.items():
        assert sha256((HERE/name).read_bytes()).hexdigest() == value
    report = dict(step_id='2026-10-24-mca-437-l144-single-record-reuse',indices=[239,647],
        complete_original_record=case,complete_prior_overlay=overlay,rows=rows,row_inputs=row_inputs,
        original_matrix=matrix,rank_minor_rows=case['minor_rows'],rank_minor_columns=columns,
        rank_minor_residue=residue,free_columns=free,kernel_basis=basis,kernel_residuals=residuals,
        source=source,literal_complete_ordered_kernel_equal=equal,point_row_bindings=bindings,
        historical_residual_occurrences=master['residual_occurrences'],historical_mismatches=old['unmatched_indices'],
        input_sha256=reuse.HASHES,original_inputs_unchanged=True,failures=[],
        summary=dict(actual_records=1,required_records=1,original_entries=504,rank=19,kernel_dimension=2,
                     literal_matches=int(equal),point_row_bindings=len(bindings),required_bindings=2),
        disposition='excluded' if equal and len(bindings)==2 else 'mismatch_stop',
        qualification='Same-step binding; audited locus and unchanged row imported. No new locus, sweep, changed-row gates, assembly or global improvement.')
    report['code_sha256']=sha256(Path(__file__).read_bytes()).hexdigest()
    out=HERE/'l144-single-record-reuse.json'
    out.write_text(json.dumps(report,indent=2)+'\n')
    print(f"Records 1/1; minor {residue} != 0; rank 19; literal match {equal}; bindings {len(bindings)}/2; failures 0; {out}")


if __name__ == '__main__':
    run()
