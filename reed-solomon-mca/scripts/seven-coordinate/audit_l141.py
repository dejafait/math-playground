"""Audit only L141's existing (199,565) classification; preserve every input.

Run from the notebook: python3 -E -B scripts/seven-coordinate/audit_l141.py
"""
from hashlib import sha256
from itertools import combinations
from pathlib import Path
from tempfile import TemporaryDirectory
import json
import shutil
import subprocess
import sys

HERE = Path(__file__).resolve().parent
P = 97


def run():
    report = dict(step_id='2026-10-23-mca-423-l141-critical-audit',
                  checks=[], failures=[], input_sha256={}, runs=[],
                  complete_row_checks=[], complete_pivot_checks=[])

    def check(name, condition):
        report['checks'].append(dict(name=name, passes=bool(condition)))
        if not condition:
            raise ValueError(name)

    def read(name):
        return json.loads((HERE/name).read_bytes())

    def digest(name):
        return sha256((HERE/name).read_bytes()).hexdigest()

    copied = ['first_l140_mismatch_locus_gates.py',
              'verify_first_l140_mismatch_locus_gates.py',
              'zero_anchor_support_filter.py', 'residual_kernel_gates.py',
              'new-pair-filter/third-199.json', 'l139-literal-reuse.json',
              'l140-critical-audit.json', 'first-l140-mismatch-locus-gates.json',
              'first-l140-mismatch-locus-gates-replay.json']
    provenance = ['l125-critical-audit.json', 'l138-critical-audit.json',
                  'l136-critical-audit.json', 'new-pair-filter.json',
                  'residual-locus-reuse.json', 'l133-literal-reuse.json',
                  'l135-literal-reuse.json', 'l137-literal-reuse.json',
                  'l139-literal-reuse-replay.json',
                  'first-l140-mismatch-homogeneous-initial.json',
                  'first-l140-mismatch-development-diagnostic.json',
                  '../../lemmas/L109-seven-coordinate-parameter-free-support-filter.md',
                  '../../lemmas/L125-new-pair-rank-factor-activity-partition.md',
                  '../../lemmas/L140-l139-literal-first-row-imports.md']
    try:
        check('assertions enabled', __debug__)
        for name in copied + provenance:
            check('notebook-local input ' + name,
                  (HERE/name).resolve().is_relative_to(HERE.parent.parent))
            report['input_sha256'][name] = digest(name)
        cert = read('first-l140-mismatch-locus-gates.json')
        replay = read('first-l140-mismatch-locus-gates-replay.json')
        prior = read('l140-critical-audit.json')
        partition = read('l125-critical-audit.json')
        check('complete prior L140 audit passed', prior['failures'] == [] and
              len(prior['checks']) == 419 and all(c['passes'] for c in prior['checks']) and
              prior['original_artifacts_byte_unchanged'])
        check('complete prior L125 audit passed', partition['failures'] == [] and
              partition['original_artifacts_byte_unchanged'] and partition['full_saved_replay_identical'])
        for name in ['new-pair-filter/third-199.json', 'l139-literal-reuse.json',
                     'l139-literal-reuse-replay.json'] + provenance[:8] + provenance[-3:-1]:
            check('L140 audited binding ' + name, digest(name) == prior['input_sha256'][name])
        for name in ['new-pair-filter.json', 'new-pair-filter/third-199.json',
                     'zero_anchor_support_filter.py']:
            check('L125 original binding ' + name, digest(name) == partition['audited_input_hashes'][name])
        check('saved certificates have no failures', cert['failures'] == replay['failures'] == [])
        check('complete saved replay binding', replay['certificate_sha256'] == digest('first-l140-mismatch-locus-gates.json'))
        with TemporaryDirectory(prefix='l141-audit-', dir=HERE) as temp:
            isolated = Path(temp)
            for name in copied:
                destination = isolated/name
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(HERE/name, destination)
            for program in copied[:2]:
                result = subprocess.run([sys.executable, '-E', '-B', str(isolated/program)],
                                        capture_output=True, text=True, check=False)
                report['runs'].append(dict(program=program, returncode=result.returncode,
                    stdout=result.stdout.replace(temp, '<isolated-copy>'),
                    stderr=result.stderr.replace(temp, '<isolated-copy>')))
                check(program + ' complete isolated run', result.returncode == 0)
            for name in copied:
                check('complete byte reproduction/preservation ' + name,
                      sha256((isolated/name).read_bytes()).hexdigest() == report['input_sha256'][name])

        overlay = read('l139-literal-reuse.json')
        history = [('historical_residual_occurrences', 'new-pair-filter.json', 'residual_occurrences', 154),
                   ('historical_l132_mismatches', 'residual-locus-reuse.json', 'unmatched_indices', 118),
                   ('historical_l134_mismatches', 'l133-literal-reuse.json', 'unmatched_indices', 100),
                   ('historical_l136_mismatches', 'l135-literal-reuse.json', 'unmatched_indices', 82),
                   ('historical_l138_mismatches', 'l137-literal-reuse.json', 'unmatched_indices', 64)]
        for field, name, key, length in history:
            check('complete unchanged historical list ' + field,
                  overlay[field] == read(name)[key] and len(overlay[field]) == length)
        check('all 46 mismatches preserved and first is correct',
              len(overlay['unmatched_indices']) == 46 and overlay['unmatched_indices'][0] == [199,565])
        shard = read('new-pair-filter/third-199.json')
        record = shard['cases'][167]
        binding = overlay['overlay'][8]
        check('complete original record and overlay', shard['third_index'] == 199 and
              record['fourth_index'] == 565 and
              [r for r in shard['cases'] if r['fourth_index'] == 565] == [record] and
              binding['indices'] == [199,565] and binding['complete_original_record'] == record and
              binding['disposition'] == 'unmatched' and
              cert['audited_mismatch_binding']['complete_overlay'] == binding)
        s = [1,8,12,18,22,27,33]
        h = [x for x in range(1,P) if pow(x,16,P) == 1]
        pairs = list(combinations(range(7),2))
        quads = list(combinations(s,4))
        universe = sorted([[sorted(set(a)&set(s)), sorted(set(a)-set(s))]
                           for a in combinations(h,4) if len(set(a)&set(s)) == 2])
        check('independent full-universe indices and field', len(h) == 16 and cert['H'] == h and
              cert['S'] == s and len(universe) == 756 and
              universe[199] == [[1,33],[64,89]] and universe[565] == [[18,22],[70,96]])
        expected_basis = [[int(n == 2) for n in range(21)],
                          [26,69,0,44,76,92,72,85,6,37,63,56,6,78,43,59,66,57,60,63,1]]
        check('complete displayed ordered basis', cert['kernel_basis'] == expected_basis)
        check('complete extension-rank witnesses',
              cert['rank_minor_rows'] == list(range(17))+[18,19] and
              cert['rank_minor_columns'] == [n for n in range(21) if n not in (2,20)] and
              cert['rank_minor_integer_determinant'] == 22184838231552325148529662157127680 and
              replay['rank_minor_integer_determinant'] == cert['rank_minor_integer_determinant'] and
              cert['rank_minor_residue'] == 13 and cert['kernel_residuals'] == [[0]*24]*2)
        check('complete 504 original entries replay', replay['rebuilt_original_matrix'] == cert['original_matrix'] and
              len(cert['original_matrix']) == 24 and all(len(r) == 21 for r in cert['original_matrix']))
        multiples = {(1,8,12,18):53, (1,8,18,22):36, (1,8,18,27):28, (1,8,18,33):87,
                     (1,12,18,22):36, (1,12,18,27):80, (1,12,18,33):64,
                     (1,18,22,27):28, (1,18,22,33):10, (1,18,27,33):91}
        expected_q = [[0,16*multiples.get(q,0)%P,multiples.get(q,0)] for q in quads]
        check('all homogeneous coefficients and direct infinity failure',
              cert['plucker_coefficients_s2_st_t2'] == replay['plucker_coefficients_s2_st_t2'] == expected_q and
              cert['complete_projective_parameter_locus'] == [[1,0],[1,81]] and
              cert['infinity_is_decomposable'] is False and expected_q[quads.index((1,18,27,33))] == [0,1,91])
        check('all quotients and Bezout coefficients', cert['affine_gcd'] == [0,16,1] and
              cert['affine_quotients'] == [[q[2]] if q[2] else [] for q in expected_q] and
              cert['bezout_coefficients'] == [[16] if q == (1,18,27,33) else [] for q in quads])
        initial = read('first-l140-mismatch-homogeneous-initial.json')
        check('entire initial homogeneous extraction matches final evidence', initial == dict(
              indices=[199,565], quadrics=expected_q, affine_gcd=[0,16,1], infinity=False,
              nonzero_restrictions=[dict(quadruple=list(q),coefficients=c)
                                   for q,c in zip(quads,expected_q) if any(c)]))
        diagnostic = read('first-l140-mismatch-development-diagnostic.json')
        check('preserved failed expectation, not a suppressed mathematical gate',
              diagnostic['indices'] == [199,565] and diagnostic['exception'] == 'AssertionError' and
              diagnostic['failed_expectation'] == "assert not point['passes_intrinsic_gates']" and
              diagnostic['final_certificate'] == 'first-l140-mismatch-locus-gates.json' and
              diagnostic['final_replay'] == 'first-l140-mismatch-locus-gates-replay.json')
        report['development_diagnostic'] = diagnostic

        table = [[(53,0,0,[53,0,0,0]),(0,12,0,[0,12,0,0]),
                  (71,0,0,[71,0,0,0]),(0,33,0,[33,0,0,0])],
                 [(63,73,23,[1,83,91,62]),(63,12,28,[52,89,74,86]),
                  (23,25,85,[92,31,6,22]),(31,33,28,[53,65,27,74])]]
        planes = [([1,0,0,0,0,0,0],[0,0,0,1,0,0,0]),
                  ([1,0,42,90,52,62,61],[0,69,60,1,72,45,80])]
        expected_rows, expected_pivots = [], []
        for pi, point in enumerate(cert['points_and_all_row_gates']):
            check(f'complete displayed plane {pi}', (point['u'],point['v']) == planes[pi])
            for j,(row,gate) in enumerate(zip(cert['rows'],point['row_gates'])):
                a,b,lam,weights = table[pi][j]
                check(f'complete displayed row {pi},{j}', gate['direction_coefficients'] == [a,b] and
                      gate['lambda_value'] == lam and gate['error_weights'] == weights and
                      gate['projection_rank'] == 1 and gate['projection_minors'] == [0]*6 and
                      gate['passes'] == all(weights) and gate['moment_residuals'] == [0]*8 and
                      gate['h_minus_error_minus_lambda_g_on_H'] == [0]*16 and
                      gate['prescribed_finite_gate'] == {'D_coefficient':a,'C_coefficient':-b%P})
                expected_rows.append({'point_index':pi,'row_number':j+1,'Q_u':gate['Q_u'],'Q_v':gate['Q_v'],
                    'h':gate['intersection_vector'],'lambda':lam,
                    'error':{str(x):w for x,w in zip(row['I']+row['K'],weights)},
                    'moments':[0]*8,'finite_gate_coefficients_D_C':[a,-b%P]})
                report['complete_row_checks'].append(dict(point=pi,row=j+1,full_gate=gate,passed=True))
            skew = [[0]*7 for _ in range(7)]
            for (x,y),value in zip(pairs,point['bivector']):
                skew[x][y],skew[y][x] = value,-value%P
            for (a,b),value in zip(pairs,point['bivector']):
                if not value:
                    continue
                u = [skew[x][b]*pow(value,-1,P)%P for x in range(7)]
                v = skew[a]
                for j,(block,gate) in enumerate(zip(cert['blocks'],point['row_gates'])):
                    qu,qv = [[sum(x*y for x,y in zip(c,w))%P for c in block['covectors']] for w in (u,v)]
                    for n in range(4):
                        if not (qu[n] or qv[n]):
                            continue
                        aa,bb = -qv[n]%P,qu[n]
                        hh = [(aa*x+bb*y)%P for x,y in zip(u,v)]
                        ix = next(x for x,w in enumerate(gate['intersection_vector']) if w)
                        scalar = hh[ix]*pow(gate['intersection_vector'][ix],-1,P)%P
                        check(f'pivot {pi},{a},{b},{j},{n} same nonzero line', scalar != 0 and
                              hh == [scalar*x%P for x in gate['intersection_vector']])
                        expected_pivots.append(dict(point=pi,exterior_pivot=[a,b],row=j+1,
                            projection_component=n,direction=[aa,bb],scalar=scalar,h=hh,
                            lambda_value=scalar*gate['lambda_value']%P,
                            error_weights=[scalar*x%P for x in gate['error_weights']]))
        check('complete eight original replay rows', len(expected_rows) == 8 and replay['all_row_replay'] == expected_rows)
        check('complete 346 ordered pivot records', len(expected_pivots) == 346 and replay['all_pivot_replay'] == expected_pivots)
        report['complete_pivot_checks'] = expected_pivots
        check('exactly one intrinsic survivor; no forced exclusion',
              [p['passes_intrinsic_gates'] for p in cert['points_and_all_row_gates']] == [False,True] and
              [(r['point_index'],r['row_number']) for r in expected_rows if all(r['error'].values())]
              == [(1,1),(1,2),(1,3),(1,4)])
        check('complete producer summary', cert['summary'] == dict(actual_loci=1,required_loci=1,
              rank=19,kernel_dimension=2,basis_residuals=48,plucker_equations=35,nonzero_plucker_equations=10,
              complete_projective_points=2,row_tests=8,rank_zero_rows=0,rank_one_rows=8,
              lambda_zero_rows=4,full_weight_rows=4,intrinsically_passing_points=1,
              required_intrinsically_passing_points_for_exclusion=0,unresolved_branches=0))
        check('complete replay summary', replay['summary'] == dict(matrix_entries_compared=504,rank=19,
              complete_kernel_vectors=2,plucker_equations=35,complete_points=2,row_gates_replayed=8,
              nonzero_exterior_pivots=22,all_projection_pivot_checks=346,lambda_zero_rows=4,
              full_weight_rows=4,intrinsic_survivors=1,required_survivors_for_exclusion=0,
              moment_residuals=64,pointwise_entries=128))
        report['summary'] = dict(actual_loci=1,required_loci=1,rank=19,kernel_dimension=2,
              homogeneous_equations=35,complete_extension_points=2,row_gates=8,
              exterior_pivots=22,projection_pivots=346,pointwise_entries=128,original_moments=64,
              passing_planes=1,required_passing_planes_for_exclusion=0,full_rows=4,lambda_zero_rows=4,
              original_files=len(report['input_sha256']),isolated_files=len(copied))
    except Exception as error:
        report['failures'].append(f'{type(error).__name__}: {error}')
    finally:
        preserved = all(digest(name) == value for name,value in report['input_sha256'].items())
        report['original_artifacts_byte_unchanged'] = preserved
        if not preserved:
            report['failures'].append('An original input changed')
        report['audit_code_sha256'] = sha256(Path(__file__).read_bytes()).hexdigest()
        report['qualification'] = 'Existing necessary classification only; shared Python/residue arithmetic and inherited finite certificates; no census, actual-event inference or global bound.'
        target = HERE/'l141-critical-audit.json'
        target.write_text(json.dumps(report,indent=2)+'\n')
        print(json.dumps(report.get('summary',{}),sort_keys=True))
        print(f"Checks {sum(c['passes'] for c in report['checks'])}/{len(report['checks'])}; "
              f"failures {report['failures']}; originals unchanged {preserved}; certificate {target}")
    if report['failures']:
        raise SystemExit(1)


if __name__ == '__main__':
    run()
