"""Separate single-record L145 audit; no sweep or historical main execution.

Run: python3 -E -B scripts/seven-coordinate/audit_l145.py
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


def run():
    report = dict(step_id='2026-10-24-mca-439-l145-critical-audit',
                  checks=[], failures=[], input_sha256={}, runs=[])

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
        cert = read('l144-single-record-reuse.json')
        replay = read('l144-single-record-reuse-replay.json')
        programs = ['l144_single_record_reuse.py', 'verify_l144_single_record_reuse.py']
        helpers = ['l139_literal_reuse.py', 'verify_l139_literal_reuse.py',
                   'verify_new_pair_filter.py', 'verify_fixed_three_row_extensions.py']
        outputs = ['l144-single-record-reuse.json', 'l144-single-record-reuse-replay.json']
        names = sorted(set(cert['input_sha256']) | set(programs+helpers+outputs) |
                       {'../../lemmas/L144-first-l143-mismatch-full-gate-exclusion.md'})
        for name in names:
            check('notebook-local input '+name,
                  (HERE/name).resolve().is_relative_to(HERE.parent.parent))
            report['input_sha256'][name] = digest(name)
        for name, value in cert['input_sha256'].items():
            check('complete producer input binding '+name, digest(name) == value)
        check('producer and replay bytes bound', cert['code_sha256'] == digest(programs[0]) and
              replay['verifier_sha256'] == digest(programs[1]) and
              replay['certificate_sha256'] == digest(outputs[0]))
        check('original outputs successful', cert['failures'] == replay['failures'] == [] and
              cert['original_inputs_unchanged'] and cert['disposition'] == 'excluded')

        # Inspect the complete top-level syntax, not a header-only import scan.
        # All mathematical calls occur inside the separately inspected functions.
        for name in programs+helpers:
            module = ast.parse((HERE/name).read_text())
            unexpected = []
            main_guards = 0
            for node in module.body:
                if isinstance(node, (ast.Import, ast.ImportFrom, ast.Assign, ast.FunctionDef)):
                    continue
                if isinstance(node, ast.Expr) and isinstance(node.value, ast.Constant) and isinstance(node.value.value, str):
                    continue
                if isinstance(node, ast.If) and ast.unparse(node.test) == "__name__ == '__main__'":
                    main_guards += 1
                    continue
                unexpected.append(ast.unparse(node))
            check('guarded module initialization '+name, not unexpected and main_guards == 1)

        original, prior, source_audit = [read(n) for n in
            ('l125-critical-audit.json','l143-critical-audit.json','l144-critical-audit.json')]
        check('L125 full replay verdict', original['failures'] == [] and
              original['original_artifacts_byte_unchanged'] and original['full_saved_replay_identical'])
        for tag, audit, count in [('L143',prior,6674),('L144',source_audit,146)]:
            check(tag+' complete prior verdict', audit['failures'] == [] and
                  audit['original_artifacts_byte_unchanged'] and len(audit['checks']) == count and
                  all(c['passes'] for c in audit['checks']))
        for name in ['new-pair-filter.json','new-pair-filter/third-239.json']+helpers[2:]:
            check('L125 original hash '+name, digest(name) == original['audited_input_hashes'][name])
        for name in ['new-pair-filter.json','new-pair-filter/third-239.json',
                     'l141-l142-literal-reuse.json','l125-critical-audit.json']:
            check('L143 provenance '+name, digest(name) == prior['input_sha256'][name])
        for name, value in source_audit['input_sha256'].items():
            check('entire L144 audit manifest '+name,
                  name in report['input_sha256'] and digest(name) == value)

        master, shard, old = [read(n) for n in
            ('new-pair-filter.json','new-pair-filter/third-239.json','l141-l142-literal-reuse.json')]
        record, overlay = shard['cases'][182], old['overlay'][1]
        check('complete original and overlay', shard['third_index'] == 239 and
              [r for r in shard['cases'] if r['fourth_index'] == 647] == [record] and
              overlay['indices'] == cert['indices'] == [239,647] and
              overlay['case_pointer'] == '/cases/182' and
              overlay['shard'] == 'new-pair-filter/third-239.json' and
              overlay['disposition'] == 'unmatched' and
              record == overlay['complete_original_record'] == cert['complete_original_record'] and
              overlay == cert['complete_prior_overlay'])
        check('complete historical lists preserved',
              len(master['residual_occurrences']) == 154 and len(old['unmatched_indices']) == 44 and
              cert['historical_residual_occurrences'] == old['historical_residual_occurrences'] == master['residual_occurrences'] and
              cert['historical_mismatches'] == old['unmatched_indices'])
        s = [1,8,12,18,22,27,33]
        h = [x for x in range(1,P) if pow(x,16,P) == 1]
        pairs = list(combinations(range(7),2))
        universe = sorted([[sorted(set(a)&set(s)),sorted(set(a)-set(s))]
                           for a in combinations(h,4) if len(set(a)&set(s)) == 2])
        check('independent full universe and exact four supports', universe == master['universe'] and
              [universe[n] for n in master['first_indices']+[239,647]] ==
              [[[1,8],[47,50]],[[12,18],[64,75]],[[8,12],[70,85]],[[18,33],[89,96]]])
        expected_basis = [[int(n == 7) for n in range(21)],
                          [dict(zip([1,6,11,12,13,14],[15,84,73,63,62,1])).get(n,0) for n in range(21)]]
        check('entire displayed ordered basis and identity free coordinates',
              cert['kernel_basis'] == record['kernel_basis'] == expected_basis and
              cert['free_columns'] == [7,14] and
              [[v[n] for n in [7,14]] for v in expected_basis] == [[1,0],[0,1]])
        matrix = cert['original_matrix']
        check('original stack dimensions and complete zero residuals', len(matrix) == 24 and
              all(len(row) == 21 for row in matrix) and
              [[sum(a*b for a,b in zip(v,row))%P for row in matrix] for v in expected_basis] ==
              cert['kernel_residuals'] == record['kernel_residuals'] == [[0]*24]*2)
        check('fresh original minor indices', cert['rank_minor_rows'] == list(range(16))+[18,19,21] and
              cert['rank_minor_columns'] == [n for n in range(21) if n not in (7,14)])
        # An exact rational determinant independently certifies the selected residue.
        a = [[Fraction(matrix[r][c]) for c in cert['rank_minor_columns']] for r in cert['rank_minor_rows']]
        determinant = Fraction(1)
        for c in range(19):
            r = next(r for r in range(c,19) if a[r][c])
            if r != c:
                a[r],a[c] = a[c],a[r]
                determinant = -determinant
            determinant *= a[c][c]
            for r in range(c+1,19):
                scale = a[r][c]/a[c][c]
                a[r] = [x-scale*y for x,y in zip(a[r],a[c])]
        check('exact determinant has new residue 73', determinant.denominator == 1 and
              int(determinant)%P == cert['rank_minor_residue'] == record['minor_residue'] == 73)
        report['rank_minor_integer_determinant'] = int(determinant)

        source = read('first-l143-mismatch-locus-gates.json')
        source_replay = read('first-l143-mismatch-locus-gates-replay.json')
        check('entire ordered extension kernel literally equals L144',
              cert['literal_complete_ordered_kernel_equal'] and
              expected_basis == cert['source']['kernel_basis'] == source['kernel_basis'])
        check('complete inherited homogeneous locus and infinity',
              all(value == source[key] for key,value in cert['source']['imported_locus'].items()) and
              source['plucker_coefficients_s2_st_t2'] == source_replay['plucker_coefficients_s2_st_t2'] and
              source['complete_projective_parameter_locus'] == [[1,0],[0,1]] and
              source['infinity_is_decomposable'])
        check('exact second-row polynomial and original block',
              cert['row_inputs'][1]['g_coefficients_ascending'] == [75,10,43,58,96,17,66,1] and
              cert['row_inputs'][1]['original_block'] == source['blocks'][1])
        check('two and only two exhaustive bindings', len(cert['point_row_bindings']) == 2 and
              cert['point_row_bindings'] == cert['source']['point_bindings'])
        pivot_count = 0
        for pi,binding in enumerate(cert['point_row_bindings']):
            point = source['points_and_all_row_gates'][pi]
            gate = point['row_gates'][1]
            check(f'full point and unchanged second-row binding {pi}',
                  binding['source_point_index'] == pi and binding['source_row_number'] == 2 and
                  binding['row_input'] == cert['row_inputs'][1] and
                  binding['plane_representative'] == {k:point[k] for k in ('u','v','bivector','pivot_indices')} and
                  binding['unchanged_rejecting_gate'] == gate and
                  binding['original_row_replay'] == next(r for r in source_replay['all_row_replay'] if r['point_index'] == pi and r['row_number'] == 2))
            check(f'displayed rejection, moments and chart {pi}',
                  gate['direction_coefficients'] == [[0,75],[0,44]][pi] and
                  gate['error_weights'] == [[0,75,0,0],[78,0,0,0]][pi] and
                  gate['projection_rank'] == 1 and gate['lambda_value'] == 0 and not gate['passes'] and
                  gate['moment_residuals'] == [0]*8 and gate['h_minus_error_minus_lambda_g_on_H'] == [0]*16 and
                  gate['original_first_coefficient'] == '(D*alpha-C*beta)/(AD-BC)')
            pivots = [r for r in source_replay['all_pivot_replay'] if r['point'] == pi and r['row'] == 2]
            check(f'every alternative pivot binding {pi}', pivots == binding['all_nonzero_pivot_replay'] and
                  all(r['scalar'] and r['lambda_value'] == 0 and r['error_weights'][2:] == [0,0] for r in pivots))
            pivot_count += len(pivots)
        check('complete producer summary', cert['summary'] == dict(actual_records=1,required_records=1,
              original_entries=504,rank=19,kernel_dimension=2,literal_matches=1,point_row_bindings=2,required_bindings=2))
        check('complete independent replay summary', replay['summary'] == dict(actual_records=1,
              required_records=1,matrix_entries=504,null_residuals=48,rank=19,minor_residue=73,
              complete_kernel_vectors=2,point_row_bindings=2,required_bindings=2,
              projection_pivot_bindings=25,original_moments=16,pointwise_entries=32) and pivot_count == 25)

        # Both complete, inspected programs recompute all 504 entries and every
        # bound row, moment and alternative pivot. Historical helpers only import.
        with TemporaryDirectory(prefix='l145-audit-', dir=HERE) as temp:
            isolated = Path(temp)/'reed-solomon-mca'/'scripts'/'seven-coordinate'
            for name in names:
                dst = isolated/name
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(HERE/name,dst)
            for program in programs:
                result = subprocess.run([sys.executable,'-E','-B',str(isolated/program)],
                    cwd=isolated.parent.parent,capture_output=True,text=True,check=False)
                report['runs'].append(dict(program=program,returncode=result.returncode,
                    stdout=result.stdout.replace(temp,'<isolated-copy>'),
                    stderr=result.stderr.replace(temp,'<isolated-copy>')))
                check('complete isolated execution '+program, result.returncode == 0)
            for name in names:
                check('whole-byte reproduction/preservation '+name,
                      sha256((isolated/name).read_bytes()).hexdigest() == report['input_sha256'][name])
        report['complete_original_record'] = record
        report['complete_point_bindings'] = cert['point_row_bindings']
        report['summary'] = dict(actual_records=1,required_records=1,original_entries=504,
            null_residuals=48,rank=19,minor_residue=73,complete_extension_points=2,
            rejecting_row_bindings=2,required_bindings=2,projection_pivots=25,
            original_moments=16,pointwise_entries=32,original_files=len(names),
            byte_identical_outputs=2,required_outputs=2)
    except Exception as error:
        report['failures'].append(f'{type(error).__name__}: {error}')
    finally:
        preserved = all(digest(name) == value for name,value in report['input_sha256'].items())
        report['original_artifacts_byte_unchanged'] = preserved
        if not preserved:
            report['failures'].append('An original input changed')
        report['audit_code_sha256'] = sha256(Path(__file__).read_bytes()).hexdigest()
        report['qualification'] = 'Separate single-record critical audit; shared Python/residue arithmetic and inherited finite certificates; no new locus, sweep, assembly or global bound.'
        path = HERE/'l145-critical-audit.json'
        path.write_text(json.dumps(report,indent=2)+'\n')
        print(json.dumps(report.get('summary',{}),sort_keys=True))
        print(f"Checks {sum(c['passes'] for c in report['checks'])}/{len(report['checks'])}; failures {report['failures']}; originals unchanged {preserved}; certificate {path}")
    if report['failures']:
        raise SystemExit(1)


if __name__ == '__main__':
    run()
