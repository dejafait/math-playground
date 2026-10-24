"""Separate audit of exactly L137; replay original programs without modifying inputs.

Run from the notebook: python3 -E -B scripts/seven-coordinate/audit_l137.py
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
    report = dict(step_id='2026-10-23-mca-407-l137-critical-audit',
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

    copied = ['first_l136_mismatch_locus_gates.py',
              'verify_first_l136_mismatch_locus_gates.py',
              'zero_anchor_support_filter.py', 'residual_kernel_gates.py',
              'new-pair-filter/third-175.json', 'l135-literal-reuse.json',
              'first-l136-mismatch-locus-gates.json',
              'first-l136-mismatch-locus-gates-replay.json']
    provenance = ['l125-critical-audit.json', 'l136-critical-audit.json',
                  'new-pair-filter.json', 'l135-literal-reuse-replay.json',
                  'l132-critical-audit.json', 'l134-critical-audit.json',
                  'residual-locus-reuse.json', 'l133-literal-reuse.json',
                  '../../lemmas/L109-seven-coordinate-parameter-free-support-filter.md',
                  '../../lemmas/L125-new-pair-rank-factor-activity-partition.md']
    try:
        check('audit assertions enabled', __debug__)
        for name in copied + provenance:
            check('notebook-local input ' + name,
                  (HERE/name).resolve().is_relative_to(HERE.parent.parent))
            report['input_sha256'][name] = digest(name)
        cert = read(copied[-2])
        replay = read(copied[-1])
        old = read('l136-critical-audit.json')
        original = read('l125-critical-audit.json')
        check('complete prior L136 audit passed', old['failures'] == [] and
              len(old['checks']) == 503 and all(c['passes'] for c in old['checks']) and
              old['original_artifacts_byte_unchanged'])
        check('prior L125 audit passed', original['failures'] == [] and
              original['original_artifacts_byte_unchanged'] and original['full_saved_replay_identical'])
        for name in ['l125-critical-audit.json', 'new-pair-filter.json',
                     'new-pair-filter/third-175.json', 'l135-literal-reuse.json',
                     'l135-literal-reuse-replay.json', 'l132-critical-audit.json',
                     'l134-critical-audit.json', 'residual-locus-reuse.json',
                     'l133-literal-reuse.json'] + provenance[-2:]:
            check('L136 audited input binding ' + name, digest(name) == old['input_sha256'][name])
        for name in ['new-pair-filter.json', 'new-pair-filter/third-175.json',
                     'zero_anchor_support_filter.py']:
            check('L125 original binding ' + name, digest(name) == original['audited_input_hashes'][name])
        check('no original certificate failures', cert['failures'] == replay['failures'] == [])
        check('complete replay certificate binding', replay['certificate_sha256'] == digest(copied[-2]))
        with TemporaryDirectory(prefix='l137-audit-', dir=HERE) as temp:
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
                check(program + ' assertions-enabled isolated execution', result.returncode == 0)
            for name in copied:
                check('complete byte reproduction/preservation ' + name,
                      sha256((isolated/name).read_bytes()).hexdigest() == report['input_sha256'][name])

        master = read('new-pair-filter.json')
        overlay = read('l135-literal-reuse.json')
        prior118 = read('residual-locus-reuse.json')
        prior100 = read('l133-literal-reuse.json')
        check('complete historical lists preserved',
              overlay['historical_residual_occurrences'] == master['residual_occurrences'] and
              len(master['residual_occurrences']) == 154 and
              overlay['historical_l132_mismatches'] == prior118['unmatched_indices'] and
              len(prior118['unmatched_indices']) == 118 and
              overlay['historical_l134_mismatches'] == prior100['unmatched_indices'] and
              len(prior100['unmatched_indices']) == 100 and
              len(overlay['unmatched_indices']) == 82 and
              overlay['unmatched_indices'][0] == [175,238])
        shard = read('new-pair-filter/third-175.json')
        record = shard['cases'][24]
        binding = overlay['overlay'][8]
        check('exact original record and audited first mismatch',
              record['fourth_index'] == 238 and shard['third_index'] == 175 and
              [r for r in shard['cases'] if r['fourth_index'] == 238] == [record] and
              binding['indices'] == [175,238] and binding['complete_original_record'] == record and
              binding['disposition'] == 'unmatched' and
              cert['audited_mismatch_binding']['complete_overlay'] == binding)

        s = [1,8,12,18,22,27,33]
        h = [x for x in range(1,P) if pow(x,16,P) == 1]
        pairs = list(combinations(range(7),2))
        check('exact H and S', cert['H'] == h and len(h) == 16 and cert['S'] == s)
        universe = sorted([[sorted(set(a)&set(s)), sorted(set(a)-set(s))]
                           for a in combinations(h,4) if len(set(a)&set(s)) == 2])
        check('independent full-universe indices', len(universe) == 756 and
              universe[175] == [[1,27],[79,89]] and universe[238] == [[8,12],[70,79]])
        expected_basis = [[int(n == 1) for n in range(21)],
                          [dict(zip([0,6,7,8,9,10],[55,68,2,44,54,1])).get(n,0) for n in range(21)]]
        check('complete displayed ordered basis', cert['kernel_basis'] == expected_basis)
        check('complete minor and extension-rank witnesses',
              cert['rank_minor_rows'] == list(range(17))+[18,19] and
              cert['rank_minor_columns'] == [n for n in range(21) if n not in (1,10)] and
              cert['rank_minor_integer_determinant'] == -124989965239914621838197515939217408 and
              replay['rank_minor_integer_determinant'] == cert['rank_minor_integer_determinant'] and
              cert['rank_minor_residue'] == 86 and
              cert['kernel_residuals'] == [[0]*24]*2)
        check('full original matrix replay', replay['rebuilt_original_matrix'] == cert['original_matrix'] and
              len(cert['original_matrix']) == 24 and all(len(r) == 21 for r in cert['original_matrix']))
        mixed = {(1,8,12,18):95, (1,8,12,22):53, (1,8,12,27):43, (1,8,12,33):96}
        expected_q = [[0,mixed.get(q,0),0] for q in combinations(s,4)]
        check('all homogeneous coefficients and infinity',
              cert['plucker_coefficients_s2_st_t2'] == replay['plucker_coefficients_s2_st_t2'] == expected_q and
              cert['complete_projective_parameter_locus'] == [[1,0],[0,1]])
        check('all affine quotients and Bezout coefficients', cert['affine_gcd'] == [0,1] and
              cert['affine_quotients'] == [[q[1]] if q[1] else [] for q in expected_q] and
              cert['bezout_coefficients'] == [[96] if q == (1,8,12,33) else [] for q in combinations(s,4)])

        # Check the complete saved replay, not a preview or a summary counter.
        table = [[(81,0,0,[81,0,0,0]),(0,12,0,[12,0,0,0]),
                  (56,0,0,[56,0,0,0]),(0,70,0,[0,70,0,0])],
                 [(0,28,0,[0,85,0,0]),(46,12,42,[32,54,14,32]),
                  (94,71,29,[33,28,9,53]),(0,28,0,[85,0,0,0])]]
        expected_pivots = []
        expected_rows = []
        for pi, point in enumerate(cert['points_and_all_row_gates']):
            check(f'point {pi} exhaustive displayed plane',
                  (point['u'],point['v']) == [([1,0,0,0,0,0,0],[0,0,1,0,0,0,0]),
                                            ([1,0,94,37,38,29,67],[0,55,0,0,0,0,0])][pi])
            for j, (row, block, gate) in enumerate(zip(cert['rows'],cert['blocks'],point['row_gates'])):
                a,b,lam,weights = table[pi][j]
                check(f'complete displayed row {pi},{j}', gate['direction_coefficients'] == [a,b] and
                      gate['lambda_value'] == lam and gate['error_weights'] == weights and
                      gate['projection_rank'] == 1 and gate['projection_minors'] == [0]*6 and
                      gate['passes'] == all(weights) and gate['moment_residuals'] == [0]*8 and
                      gate['h_minus_error_minus_lambda_g_on_H'] == [0]*16 and
                      gate['prescribed_finite_gate'] == {'D_coefficient':a,'C_coefficient':-b%P})
                expected_rows.append(dict(point_index=pi,row_number=j+1,Q_u=gate['Q_u'],Q_v=gate['Q_v'],
                    h=gate['intersection_vector'],lambda_=lam))
                expected_rows[-1]['lambda'] = expected_rows[-1].pop('lambda_')
                expected_rows[-1].update(error={str(x):w for x,w in zip(row['I']+row['K'],weights)},
                    moments=[0]*8,finite_gate_coefficients_D_C=[a,-b%P])
                report['complete_row_checks'].append(dict(point=pi,row=j+1,
                    full_gate=gate,passed=True))
            p = point['bivector']
            skew = [[0]*7 for _ in range(7)]
            for (x,y),value in zip(pairs,p):
                skew[x][y],skew[y][x] = value,-value%P
            for (a,b),value in zip(pairs,p):
                if not value:
                    continue
                u = [skew[x][b]*pow(value,-1,P)%P for x in range(7)]
                v = skew[a]
                for j,(row,block,gate) in enumerate(zip(cert['rows'],cert['blocks'],point['row_gates'])):
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
        check('complete 91 ordered pivot records', len(expected_pivots) == 91 and replay['all_pivot_replay'] == expected_pivots)
        report['complete_pivot_checks'] = expected_pivots
        check('six lambda failures and exactly two full rows retained',
              sum(r['lambda'] == 0 for r in expected_rows) == 6 and
              [(r['point_index'],r['row_number']) for r in expected_rows if all(r['error'].values())] == [(1,2),(1,3)])
        check('both first-row rejection lines',
              expected_rows[0]['h'] == [81,0,0,0,0,0,0] and
              expected_rows[4]['h'] == [0,85,0,0,0,0,0])
        report['summary'] = dict(actual_loci=1,required_loci=1,rank=19,kernel_dimension=2,
            homogeneous_equations=35,complete_extension_points=2,row_gates=8,
            exterior_pivots=7,projection_pivots=len(expected_pivots),pointwise_entries=128,
            original_moments=64,passing_planes=0,full_rows=2,lambda_zero_rows=6,
            original_files=len(report['input_sha256']),isolated_files=len(copied))
    except Exception as error:
        report['failures'].append(f'{type(error).__name__}: {error}')
    finally:
        preserved = all(digest(name) == value for name,value in report['input_sha256'].items())
        report['original_artifacts_byte_unchanged'] = preserved
        if not preserved:
            report['failures'].append('An original input changed')
        report['audit_code_sha256'] = sha256(Path(__file__).read_bytes()).hexdigest()
        report['qualification'] = 'One indexed input; shared Python/residue arithmetic and inherited finite certificates; no new exclusion, assembly or global bound.'
        target = HERE/'l137-critical-audit.json'
        target.write_text(json.dumps(report,indent=2)+'\n')
        print(json.dumps(report.get('summary',{}),sort_keys=True))
        print(f"Checks {sum(c['passes'] for c in report['checks'])}/{len(report['checks'])}; "
              f"failures {report['failures']}; originals unchanged {preserved}; certificate {target}")
    if report['failures']:
        raise SystemExit(1)


if __name__ == '__main__':
    run()
