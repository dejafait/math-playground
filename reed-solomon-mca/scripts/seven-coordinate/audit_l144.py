"""Separate L144 audit: complete existing evidence and isolated whole-output replay.

Run: python3 -E -B scripts/seven-coordinate/audit_l144.py
No historical filter or other occurrence is executed.
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
    report = dict(step_id='2026-10-23-mca-435-l144-critical-audit', checks=[],
                  failures=[], input_sha256={}, runs=[], complete_rows=[], complete_pivots=[])

    def check(name, condition):
        report['checks'].append(dict(name=name, passes=bool(condition)))
        if not condition:
            raise ValueError(name)

    def digest(name):
        return sha256((HERE/name).read_bytes()).hexdigest()

    def read(name):
        return json.loads((HERE/name).read_bytes())

    copied = ['first_l143_mismatch_locus_gates.py',
              'verify_first_l143_mismatch_locus_gates.py',
              'zero_anchor_support_filter.py', 'residual_kernel_gates.py',
              'new-pair-filter/third-238.json', 'l141-l142-literal-reuse.json',
              'l143-critical-audit.json', 'first-l143-mismatch-locus-gates.json',
              'first-l143-mismatch-locus-gates-replay.json']
    provenance = ['l125-critical-audit.json', 'new-pair-filter.json',
                  '../../lemmas/L109-seven-coordinate-parameter-free-support-filter.md',
                  '../../lemmas/L125-new-pair-rank-factor-activity-partition.md',
                  '../../lemmas/L143-l141-l142-literal-exchange-only.md']
    try:
        check('assertions enabled', __debug__)
        for name in copied + provenance:
            check('notebook-local input ' + name,
                  (HERE/name).resolve().is_relative_to(HERE.parent.parent))
            report['input_sha256'][name] = digest(name)
        cert = read('first-l143-mismatch-locus-gates.json')
        replay = read('first-l143-mismatch-locus-gates-replay.json')
        prior = read('l143-critical-audit.json')
        original = read('l125-critical-audit.json')
        check('complete prior L143 verdict', prior['failures'] == [] and
              len(prior['checks']) == 6674 and all(c['passes'] for c in prior['checks']) and
              prior['original_artifacts_byte_unchanged'])
        check('prior L125 verdict', original['failures'] == [] and
              original['original_artifacts_byte_unchanged'] and original['full_saved_replay_identical'])
        for name in ['new-pair-filter/third-238.json', 'new-pair-filter.json',
                     'l141-l142-literal-reuse.json', 'l125-critical-audit.json',
                     'zero_anchor_support_filter.py', 'residual_kernel_gates.py'] + provenance[2:4]:
            check('L143 bound input ' + name, digest(name) == prior['input_sha256'][name])
        for name in ['new-pair-filter/third-238.json', 'new-pair-filter.json',
                     'zero_anchor_support_filter.py']:
            check('L125 bound input ' + name, digest(name) == original['audited_input_hashes'][name])
        check('producer and replay have no failures', cert['failures'] == replay['failures'] == [])
        check('replay bound to complete producer bytes',
              replay['certificate_sha256'] == digest('first-l143-mismatch-locus-gates.json'))
        with TemporaryDirectory(prefix='l144-audit-', dir=HERE) as temp:
            isolated = Path(temp)/'reed-solomon-mca'/'scripts'/'seven-coordinate'
            for name in copied:
                dst = isolated/name
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(HERE/name, dst)
            for program in copied[:2]:
                result = subprocess.run([sys.executable, '-E', '-B', str(isolated/program)],
                                        cwd=isolated.parent.parent, capture_output=True,
                                        text=True, check=False)
                report['runs'].append(dict(program=program, returncode=result.returncode,
                    stdout=result.stdout.replace(temp, '<isolated-copy>'),
                    stderr=result.stderr.replace(temp, '<isolated-copy>')))
                check(program + ' isolated execution', result.returncode == 0)
            for name in copied:
                check('whole-byte reproduction/preservation ' + name,
                      sha256((isolated/name).read_bytes()).hexdigest() == report['input_sha256'][name])

        master = read('new-pair-filter.json')
        overlay = read('l141-l142-literal-reuse.json')
        shard = read('new-pair-filter/third-238.json')
        record = shard['cases'][182]
        binding = overlay['overlay'][0]
        check('historical lists retained', len(master['residual_occurrences']) == 154 and
              overlay['historical_residual_occurrences'] == master['residual_occurrences'] and
              len(overlay['unmatched_indices']) == 44 and overlay['unmatched_indices'][0] == [238,647])
        check('exact original and overlay records', shard['third_index'] == 238 and
              [r for r in shard['cases'] if r['fourth_index'] == 647] == [record] and
              binding['indices'] == [238,647] and binding['complete_original_record'] == record and
              binding['case_pointer'] == '/cases/182' and binding['disposition'] == 'unmatched' and
              cert['audited_mismatch_binding']['complete_overlay'] == binding)
        s = [1,8,12,18,22,27,33]
        h = [x for x in range(1,P) if pow(x,16,P) == 1]
        pairs = list(combinations(range(7),2))
        universe = sorted([[sorted(set(a)&set(s)), sorted(set(a)-set(s))]
                           for a in combinations(h,4) if len(set(a)&set(s)) == 2])
        check('independent complete universe indices', len(universe) == 756 and
              universe[238] == [[8,12],[70,79]] and universe[647] == [[18,33],[89,96]])
        expected_basis = [[int(n == 7) for n in range(21)],
                          [dict(zip([1,6,11,12,13,14],[15,84,73,63,62,1])).get(n,0)
                           for n in range(21)]]
        check('displayed complete ordered basis', cert['kernel_basis'] == expected_basis)
        check('rank and extension-kernel witnesses',
              cert['rank_minor_rows'] == list(range(16))+[18,19,21] and
              cert['rank_minor_columns'] == [n for n in range(21) if n not in (7,14)] and
              cert['rank_minor_integer_determinant'] == 301994834048563991836699490827272192 and
              replay['rank_minor_integer_determinant'] == cert['rank_minor_integer_determinant'] and
              cert['rank_minor_residue'] == 84 and cert['kernel_residuals'] == [[0]*24]*2)
        check('all original entries replayed', replay['rebuilt_original_matrix'] == cert['original_matrix'] and
              len(cert['original_matrix']) == 24 and all(len(r) == 21 for r in cert['original_matrix']))
        mixed = {(1,8,12,18):82, (8,12,18,22):34, (8,12,18,27):35, (8,12,18,33):96}
        expected_q = [[0,mixed.get(q,0),0] for q in combinations(s,4)]
        check('all homogeneous coefficients and exhaustive projective roots',
              cert['plucker_coefficients_s2_st_t2'] == replay['plucker_coefficients_s2_st_t2'] == expected_q and
              cert['complete_projective_parameter_locus'] == [[1,0],[0,1]] and
              cert['infinity_is_decomposable'] and cert['affine_linear_factor_roots_with_multiplicity'] == [0])
        check('complete division and Bezout identities', cert['affine_gcd'] == [0,1] and
              cert['affine_quotients'] == [[q[1]] if q[1] else [] for q in expected_q] and
              cert['bezout_coefficients'] == [[96] if q == (8,12,18,33) else [] for q in combinations(s,4)])
        table = [[(53,0,0,[0,53,0,0]), (0,75,0,[0,75,0,0]),
                  (9,0,0,[9,0,0,0]), (0,25,0,[25,0,0,0])],
                 [(51,51,24,[58,32,57,90]), (0,44,0,[78,0,0,0]),
                  (0,75,0,[0,58,0,0]), (13,51,82,[35,48,75,23])]]
        expected_rows, expected_pivots = [], []
        for pi, point in enumerate(cert['points_and_all_row_gates']):
            check(f'displayed plane {pi}', (point['u'],point['v']) == [
                ([0,1,0,0,0,0,0],[0,0,0,1,0,0,0]),
                ([1,25,0,21,54,67,84],[0,0,15,0,0,0,0])][pi])
            for j, (row, gate) in enumerate(zip(cert['rows'],point['row_gates'])):
                a,b,lam,weights = table[pi][j]
                check(f'complete row {pi},{j}', gate['direction_coefficients'] == [a,b] and
                      gate['lambda_value'] == lam and gate['error_weights'] == weights and
                      gate['projection_rank'] == 1 and gate['projection_minors'] == [0]*6 and
                      gate['passes'] == all(weights) and gate['moment_residuals'] == [0]*8 and
                      gate['h_minus_error_minus_lambda_g_on_H'] == [0]*16 and
                      gate['prescribed_finite_gate'] == {'D_coefficient':a,'C_coefficient':-b%P})
                saved = dict(point_index=pi,row_number=j+1,Q_u=gate['Q_u'],Q_v=gate['Q_v'],
                             h=gate['intersection_vector'],error={str(x):w for x,w in zip(row['I']+row['K'],weights)},
                             moments=[0]*8,finite_gate_coefficients_D_C=[a,-b%P])
                saved['lambda'] = lam
                expected_rows.append(saved)
                report['complete_rows'].append(dict(point=pi,row=j+1,full_gate=gate))
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
                        check(f'pivot {pi},{a},{b},{j},{n}', scalar != 0 and
                              hh == [scalar*x%P for x in gate['intersection_vector']])
                        expected_pivots.append(dict(point=pi,exterior_pivot=[a,b],row=j+1,
                            projection_component=n,direction=[aa,bb],scalar=scalar,h=hh,
                            lambda_value=scalar*gate['lambda_value']%P,
                            error_weights=[scalar*x%P for x in gate['error_weights']]))
        check('all eight complete replay rows', len(expected_rows) == 8 and replay['all_row_replay'] == expected_rows)
        check('all 82 complete ordered pivot records', len(expected_pivots) == 82 and replay['all_pivot_replay'] == expected_pivots)
        report['complete_pivots'] = expected_pivots
        check('exact failures and retained full rows',
              sum(r['lambda'] == 0 for r in expected_rows) == 6 and
              [(r['point_index'],r['row_number']) for r in expected_rows if all(r['error'].values())] == [(1,1),(1,4)] and
              [p['passes_intrinsic_gates'] for p in cert['points_and_all_row_gates']] == [False,False])
        check('complete producer summary', cert['summary'] == dict(
            actual_loci=1,required_loci=1,rank=19,kernel_dimension=2,basis_residuals=48,
            plucker_equations=35,nonzero_plucker_equations=4,complete_projective_points=2,
            row_tests=8,rank_zero_rows=0,rank_one_rows=8,lambda_zero_rows=6,full_weight_rows=2,
            intrinsically_passing_points=0,required_intrinsically_passing_points_for_exclusion=0,unresolved_branches=0))
        check('complete replay summary', replay['summary'] == dict(
            matrix_entries_compared=504,rank=19,complete_kernel_vectors=2,plucker_equations=35,
            complete_points=2,row_gates_replayed=8,nonzero_exterior_pivots=7,all_projection_pivot_checks=82,
            lambda_zero_rows=6,full_weight_rows=2,intrinsic_survivors=0,required_survivors_for_exclusion=0,
            moment_residuals=64,pointwise_entries=128))
        report['summary'] = dict(actual_loci=1,required_loci=1,original_entries=504,rank=19,
            kernel_dimension=2,homogeneous_equations=35,complete_extension_points=2,row_gates=8,
            exterior_pivots=7,projection_pivots=82,pointwise_entries=128,original_moments=64,
            passing_planes=0,required_passing_planes_for_exclusion=0,full_rows=2,lambda_zero_rows=6,
            original_files=len(report['input_sha256']),isolated_files=len(copied))
    except Exception as error:
        report['failures'].append(f'{type(error).__name__}: {error}')
    finally:
        preserved = all(digest(name) == value for name,value in report['input_sha256'].items())
        report['original_artifacts_byte_unchanged'] = preserved
        if not preserved:
            report['failures'].append('An original input changed')
        report['audit_code_sha256'] = sha256(Path(__file__).read_bytes()).hexdigest()
        report['qualification'] = 'Separate scoped audit; shared Python/residue arithmetic and inherited finite certificates. No new locus, census, assembly or global bound.'
        target = HERE/'l144-critical-audit.json'
        target.write_text(json.dumps(report,indent=2)+'\n')
        print(json.dumps(report.get('summary',{}),sort_keys=True))
        print(f"Checks {sum(c['passes'] for c in report['checks'])}/{len(report['checks'])}; "
              f"failures {report['failures']}; originals unchanged {preserved}; certificate {target}")
    if report['failures']:
        raise SystemExit(1)


if __name__ == '__main__':
    run()
