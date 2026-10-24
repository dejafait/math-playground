"""Separate complete L146 audit; no historical main or new reference test.

Run: python3 -E -B scripts/seven-coordinate/audit_l146.py
"""
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
from pathlib import Path
from tempfile import TemporaryDirectory
import ast
import json
import shutil
import subprocess
import sys

HERE = Path(__file__).resolve().parent
P = 97


def integer_determinant(matrix):
    a = [[Fraction(x) for x in row] for row in matrix]
    result = Fraction(1)
    for c in range(len(a)):
        r = next((r for r in range(c, len(a)) if a[r][c]), None)
        if r is None:
            return 0
        if r != c:
            a[r], a[c] = a[c], a[r]
            result = -result
        result *= a[c][c]
        for r in range(c+1, len(a)):
            scale = a[r][c]/a[c][c]
            a[r] = [x-scale*y for x, y in zip(a[r], a[c])]
    assert result.denominator == 1
    return int(result)


def run():
    report = dict(step_id='2026-10-24-mca-443-l146-critical-audit',
                  checks=[], failures=[], input_sha256={}, runs=[], records=[])

    def check(name, condition):
        report['checks'].append(dict(name=name, passes=bool(condition)))
        if not condition:
            raise ValueError(name)

    def digest(name):
        return sha256((HERE/name).read_bytes()).hexdigest()

    def read(name):
        return json.loads((HERE/name).read_bytes())

    try:
        check('assertions enabled', __debug__)
        outputs = ['l144-remaining-literal-reuse.json', 'l144-remaining-literal-reuse-replay.json']
        programs = ['l144_remaining_literal_reuse.py', 'verify_l144_remaining_literal_reuse.py']
        helpers = ['l139_literal_reuse.py', 'verify_l139_literal_reuse.py',
                   'verify_new_pair_filter.py', 'verify_fixed_three_row_extensions.py']
        cert, replay = map(read, outputs)
        audits = {tag: read(tag+'-critical-audit.json') for tag in ('l125','l143','l144','l145')}
        manifests = {tag: a['audited_input_hashes' if tag == 'l125' else 'input_sha256']
                     for tag, a in audits.items()}
        names = set(cert['input_sha256']) | set(outputs+programs+helpers)
        for manifest in manifests.values():
            names.update(manifest)
        names = sorted(names)
        for name in names:
            check('notebook-local input '+name,
                  (HERE/name).resolve().is_relative_to(HERE.parent.parent))
            report['input_sha256'][name] = digest(name)
        for name, value in cert['input_sha256'].items():
            check('producer binding '+name, digest(name) == value)
        for tag, audit in audits.items():
            check(tag+' successful prior verdict', audit['failures'] == [] and
                  audit['original_artifacts_byte_unchanged'])
            if tag == 'l125':
                check('L125 distinct older schema', audit['full_saved_replay_identical'] and
                      audit['summary']['actual_cases'] == audit['summary']['required_cases'] == 100764)
            else:
                check(tag+' entire prior checks', bool(audit['checks']) and all(c['passes'] for c in audit['checks']))
            for name, value in manifests[tag].items():
                check(tag+' complete manifest '+name, digest(name) == value)
        check('producer and verifier output binding', cert['code_sha256'] == digest(programs[0]) and
              replay['verifier_sha256'] == digest(programs[1]) and replay['certificate_sha256'] == digest(outputs[0]))
        check('successful original outputs', cert['failures'] == replay['failures'] == [] and cert['original_inputs_unchanged'])

        # Assignments and all imported helper initialization have been read.
        # Parse the whole modules to reject additional top-level execution.
        for name in programs+helpers:
            unexpected, guards = [], 0
            for node in ast.parse((HERE/name).read_text()).body:
                if isinstance(node, (ast.Import, ast.ImportFrom, ast.Assign, ast.FunctionDef)):
                    continue
                if isinstance(node, ast.Expr) and isinstance(node.value, ast.Constant) and isinstance(node.value.value, str):
                    continue
                if isinstance(node, ast.If) and ast.unparse(node.test) == "__name__ == '__main__'":
                    guards += 1
                    continue
                unexpected.append(ast.unparse(node))
            check('guarded initialization '+name, not unexpected and guards == 1)

        master, prior = read('new-pair-filter.json'), read('l141-l142-literal-reuse.json')
        source, source_replay = read('first-l143-mismatch-locus-gates.json'), read('first-l143-mismatch-locus-gates-replay.json')
        s = [1,8,12,18,22,27,33]
        h = [x for x in range(1,P) if pow(x,16,P) == 1]
        pairs = list(combinations(range(7),2))
        # Enumerate four-subsets directly, independently of the producer's Cartesian product.
        universe = sorted([[sorted(set(a)&set(s)), sorted(set(a)-set(s))]
                           for a in combinations(h,4) if len(set(a)&set(s)) == 2])
        check('full universe and original first pair', len(universe) == 756 and universe == master['universe'] and
              master['S'] == s and master['H'] == h and
              [universe[n] for n in master['first_indices']] == [[[1,8],[47,50]],[[12,18],[64,75]]])
        historical = prior['unmatched_indices']
        removed = [[238,647],[239,647]]
        scope = [x for x in historical if x not in removed]
        check('exact ordered 44-minus-two domain', len(historical) == len(set(map(tuple,historical))) == 44 and
              all(historical.count(x) == 1 for x in removed) and len(scope) == 42 and
              cert['required_scope_indices'] == scope == [r['indices'] for r in cert['overlay']] and
              cert['removed_only'] == removed)
        check('historical lists preserved', len(master['residual_occurrences']) == 154 and
              cert['historical_residual_occurrences'] == prior['historical_residual_occurrences'] == master['residual_occurrences'] and
              cert['historical_l143_mismatches'] == historical)
        expected_basis = [[int(n == 7) for n in range(21)],
                          [dict(zip([1,6,11,12,13,14],[15,84,73,63,62,1])).get(n,0) for n in range(21)]]
        imported = cert['source']
        check('entire reference basis and source import', expected_basis == imported['kernel_basis'] == source['kernel_basis'] and
              imported == read('l144-single-record-reuse.json')['source'] and imported['lemma'] == 'L144')
        locus_keys = ('plucker_quadruples','plucker_coefficients_s2_st_t2','affine_gcd',
                      'bezout_coefficients','affine_quotients','complete_projective_parameter_locus')
        check('complete audited extension locus including infinity', imported['imported_locus'] == {k:source[k] for k in locus_keys} and
              len(source['plucker_coefficients_s2_st_t2']) == 35 and source['infinity_is_decomposable'] and
              source['complete_projective_parameter_locus'] == [[1,0],[0,1]] and
              source_replay['plucker_coefficients_s2_st_t2'] == source['plucker_coefficients_s2_st_t2'])

        covered, unmatched, witnesses, total_pivots = [], [], [], 0
        shards = {}
        for entry, reconstructed in zip(cert['overlay'], replay['complete_record_replay'], strict=True):
            n, u = entry['indices']
            tag = f'({n},{u}) '
            name = entry['shard']
            if name not in shards:
                shards[name] = read(name)
            shard = shards[name]
            record = shard['cases'][int(entry['case_pointer'].split('/')[-1])]
            old = next(r for r in prior['overlay'] if r['indices'] == [n,u])
            check(tag+'full original provenance', digest(name) == manifests['l125'][name] == manifests['l143'][name] and
                  shard['third_index'] == n and [r for r in shard['cases'] if r['fourth_index'] == u] == [record] and
                  record['status'] == 'residual' and record == old['complete_original_record'] == entry['complete_original_record'] and
                  old == entry['complete_prior_overlay'] and old['disposition'] == 'unmatched' and
                  old['case_pointer'] == entry['case_pointer'] and old['shard'] == name)
            check(tag+'exact original rows', entry['rows'] == [dict(I=universe[v][0],K=universe[v][1])
                  for v in master['first_indices']+[n,u]] and entry['rows'] == old['rows'])
            matrix, basis, rank = entry['original_matrix'], entry['kernel_basis'], entry['rank']
            free = entry['free_columns']
            check(tag+'complete matrices and independent kernels', len(matrix) == 24 and all(len(r) == 21 for r in matrix) and
                  matrix == reconstructed['rebuilt_original_matrix'] == [row for item in entry['row_inputs'] for row in item['original_block']['matrix']] and
                  basis == reconstructed['independently_reconstructed_kernel'] == record['kernel_basis'] and
                  reconstructed['indices'] == [n,u] and rank == reconstructed['rank'] == record['rank'] and len(basis) == 21-rank and
                  free == reconstructed['free_columns'] == sorted(set(range(21))-set(record['pivot_columns'])) and
                  [[v[c] for c in free] for v in basis] == [[int(a == b) for b in range(len(free))] for a in range(len(free))])
            residuals = [[sum(a*b for a,b in zip(v,row))%P for row in matrix] for v in basis]
            check(tag+'every original null residual', residuals == [[0]*24 for _ in basis] ==
                  entry['kernel_residuals'] == record['kernel_residuals'] == reconstructed['null_residuals'])
            rows, cols = entry['rank_minor_rows'], entry['rank_minor_columns']
            check(tag+'original minor indices', rows == record['minor_rows'] and cols == record['pivot_columns'] and
                  len(rows) == len(set(rows)) == len(cols) == len(set(cols)) == rank and
                  all(0 <= r < 24 for r in rows) and all(0 <= c < 21 for c in cols))
            determinant = integer_determinant([[matrix[r][c] for c in cols] for r in rows])
            check(tag+'independent rational determinant', determinant%P == entry['rank_minor_residue'] ==
                  record['minor_residue'] == reconstructed['minor_residue'] != 0)
            equal = basis == expected_basis
            check(tag+'literal entire basis disposition', equal == entry['literal_complete_ordered_kernel_equal'] == reconstructed['equal'] and
                  entry['disposition'] == ('covered' if equal else 'unmatched'))
            if not equal:
                if len(basis) != len(expected_basis):
                    witness = dict(kind='basis_length',actual=len(basis),source=len(expected_basis))
                else:
                    a,b = next((a,b) for a in range(2) for b in range(21) if basis[a][b] != expected_basis[a][b])
                    witness = dict(kind='basis_entry',basis_index=a,column=b,actual=basis[a][b],source=expected_basis[a][b])
                check(tag+'explicit full mismatch witness', witness == entry['mismatch'] == reconstructed['mismatch'] and
                      entry['point_row_bindings'] == reconstructed['full_binding_replay'] == [])
                witnesses.append(dict(indices=[n,u],witness=witness))
                unmatched.append([n,u])
            else:
                covered.append([n,u])
                check(tag+'exactly both exhaustive bindings', entry['point_row_bindings'] == imported['point_bindings'] and
                      len(entry['point_row_bindings']) == len(reconstructed['full_binding_replay']) == 2 and entry['mismatch'] is None)
                for pi,binding in enumerate(entry['point_row_bindings']):
                    point = source['points_and_all_row_gates'][pi]
                    gate = point['row_gates'][1]
                    inp = entry['row_inputs'][1]
                    b = reconstructed['full_binding_replay'][pi]
                    check(tag+f'point {pi} complete unchanged row and representative', binding['source_point_index'] == pi and
                          binding['source_row_number'] == 2 and binding['row_input'] == inp and
                          inp['original_block'] == source['blocks'][1] and inp['I'] == [12,18] and inp['K'] == [64,75] and inp['z'] == 1 and
                          inp['g_coefficients_ascending'] == [75,10,43,58,96,17,66,1] and
                          binding['plane_representative'] == {k:point[k] for k in ('u','v','bivector','pivot_indices')} and
                          [(point['u'][a]*point['v'][b]-point['u'][b]*point['v'][a])%P for a,b in pairs] == basis[pi] and
                          binding['unchanged_rejecting_gate'] == gate)
                    pivots = [p for p in source_replay['all_pivot_replay'] if p['point'] == pi and p['row'] == 2]
                    check(tag+f'point {pi} entire gates moments pivots and chart', gate['projection_rank'] == 1 and
                          gate['direction_coefficients'] == [[0,75],[0,44]][pi] and
                          gate['error_weights'] == b['weights'] == [[0,75,0,0],[78,0,0,0]][pi] and
                          gate['lambda_value'] == b['lambda_value'] == 0 and not gate['passes'] and
                          gate['moment_residuals'] == b['moments'] == [0]*8 and
                          gate['h_minus_error_minus_lambda_g_on_H'] == b['pointwise'] == [0]*16 and
                          gate['original_first_coefficient'] == '(D*alpha-C*beta)/(AD-BC)' and
                          gate['original_basis_convention'] == 'u_original=A*u+B*v; v_original=C*u+D*v; AD-BC!=0' and
                          binding['original_row_replay'] == next(r for r in source_replay['all_row_replay'] if r['point_index'] == pi and r['row_number'] == 2) and
                          pivots == binding['all_nonzero_pivot_replay'] == b['alternative_pivots'] and
                          all(p['scalar'] and p['lambda_value'] == 0 and p['error_weights'][2:] == [0,0] for p in pivots))
                    total_pivots += len(pivots)
            report['records'].append(dict(indices=[n,u],rank=rank,integer_determinant=determinant,
                residue=determinant%P,complete_kernel=basis,mismatch=entry['mismatch'],covered=equal))

        expected_additional = sorted([[n,647] for n in (240,241,246,247,248,249,250)]+
                                     [[647,n] for n in (240,241,246,247,248,249,250)])
        old_exchanges = [[647,238],[647,239]]
        check('covered list and two old exchanges versus seven new families', covered == cert['covered_indices'] == replay['covered_indices'] ==
              sorted(expected_additional+old_exchanges) and cert['old_exchange_indices'] == old_exchanges and
              cert['additional_ordered_indices'] == expected_additional and
              cert['additional_unordered_families'] == [[n,647] for n in (240,241,246,247,248,249,250)])
        check('all 26 explicit mismatches preserved', unmatched == cert['unmatched_indices'] == replay['unmatched_indices'] and
              len(witnesses) == 26 and sum(w['witness']['kind'] == 'basis_length' for w in witnesses) == 8)
        expected_summary = dict(actual_records=42,required_records=42,original_entries=21168,null_residuals=1824,
            nonzero_original_minors=42,literal_matches=16,mismatches=26,old_exchanges=2,additional_ordered_bindings=14,
            additional_unordered_families=7,mismatch_witness_kinds=dict(basis_entry=18,basis_length=8),
            matched_point_row_bindings=32,required_matched_point_row_bindings=32,rank_histogram={'19':34,'20':8})
        check('exact complete summaries and pivot totals', cert['summary'] == replay['summary'] == expected_summary and
              total_pivots == replay['projection_pivot_bindings'] == 400 and replay['original_moments'] == 256 and replay['pointwise_entries'] == 512)

        # The inspected full producer and independent verifier reconstruct every
        # entry, nullspace, mismatch and gate. Originals are only read/copied.
        with TemporaryDirectory(prefix='l146-audit-', dir=HERE) as temp:
            isolated = Path(temp)/'reed-solomon-mca'/'scripts'/'seven-coordinate'
            for name in names:
                dst = isolated/name
                dst.parent.mkdir(parents=True,exist_ok=True)
                shutil.copyfile(HERE/name,dst)
            for program in programs:
                result = subprocess.run([sys.executable,'-E','-B',str(isolated/program)],
                    cwd=isolated.parent.parent,capture_output=True,text=True,check=False)
                report['runs'].append(dict(program=program,returncode=result.returncode,
                    stdout=result.stdout.replace(temp,'<isolated-copy>'),stderr=result.stderr.replace(temp,'<isolated-copy>')))
                check('complete isolated execution '+program,result.returncode == 0)
            for name in names:
                check('whole-byte isolated reproduction/preservation '+name,
                      sha256((isolated/name).read_bytes()).hexdigest() == report['input_sha256'][name])
        report['summary'] = dict(expected_summary,projection_pivots=total_pivots,original_moments=256,pointwise_entries=512,
            bound_original_files=len(names),byte_identical_outputs=2,required_outputs=2)
        report['complete_mismatch_witnesses'] = witnesses
        report['complete_source_bindings'] = imported
    except Exception as error:
        report['failures'].append(f'{type(error).__name__}: {error}')
    finally:
        preserved = all(digest(name) == value for name,value in report['input_sha256'].items())
        report['original_artifacts_byte_unchanged'] = preserved
        if not preserved:
            report['failures'].append('Original input changed')
        report['audit_code_sha256'] = sha256(Path(__file__).read_bytes()).hexdigest()
        report['qualification'] = 'Separate restricted critical audit; shared Python/residue arithmetic and inherited finite certificates; no new locus, changed-row algebra, assembly or global bound.'
        path = HERE/'l146-critical-audit.json'
        path.write_text(json.dumps(report,indent=2)+'\n')
        print(json.dumps(report.get('summary',{}),sort_keys=True))
        print(f"Checks {sum(c['passes'] for c in report['checks'])}/{len(report['checks'])}; failures {report['failures']}; originals unchanged {preserved}; certificate {path}")
    if report['failures']:
        raise SystemExit(1)


if __name__ == '__main__':
    run()
