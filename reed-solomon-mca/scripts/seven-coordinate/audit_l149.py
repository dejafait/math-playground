"""Separate L149 critical audit: exactly eight originals and selected rows.

Run with python3 -E -B scripts/seven-coordinate/audit_l149.py.
Only the two L149 programs execute, in an isolated copy. No added-row test.
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
S = [1, 8, 12, 18, 22, 27, 33]
H = [x for x in range(1, P) if pow(x, 16, P) == 1]
PAIRS = list(combinations(range(7), 2))
MANIFEST = [[467,750],[499,668],[608,695],[668,499],
            [678,749],[695,608],[749,678],[750,467]]


def integer_determinant(matrix):
    a = [[Fraction(x) for x in row] for row in matrix]
    answer = Fraction(1)
    for c in range(len(a)):
        r = next((r for r in range(c, len(a)) if a[r][c]), None)
        if r is None:
            return 0
        if r != c:
            a[r], a[c] = a[c], a[r]
            answer = -answer
        answer *= a[c][c]
        for r in range(c+1, len(a)):
            scale = a[r][c]/a[c][c]
            a[r] = [x-scale*y for x, y in zip(a[r], a[c])]
    assert answer.denominator == 1
    return int(answer)


def run():
    report = dict(step_id='2026-10-24-mca-455-l149-critical-audit',
                  checks=[], failures=[], input_sha256={}, records=[], runs=[])

    def check(name, value):
        report['checks'].append(dict(name=name, passes=bool(value)))
        if not value:
            raise ValueError(name)

    def digest(name):
        return sha256((HERE/name).read_bytes()).hexdigest()

    def read(name):
        return json.loads((HERE/name).read_bytes())

    try:
        check('assertions enabled', __debug__)
        outputs = ['l148-rank20-gates.json', 'l148-rank20-gates-replay.json']
        programs = ['l148_rank20_gates.py', 'verify_l148_rank20_gates.py']
        helpers = ['l139_literal_reuse.py', 'verify_new_pair_filter.py',
                   'verify_fixed_three_row_extensions.py', 'residual_kernel_gates.py',
                   'zero_anchor_support_filter.py', 'verify_active_rank19_complete_loci.py',
                   'verify_rank20_selected_gates.py']
        cert, replay = map(read, outputs)
        audits = {tag: read(tag+'-critical-audit.json') for tag in ('l125', 'l148')}
        manifests = {tag: a['audited_input_hashes' if tag == 'l125' else 'input_sha256']
                     for tag, a in audits.items()}
        names = set(cert['input_sha256']) | set(outputs+programs+helpers)
        for manifest in manifests.values():
            names.update(manifest)
        names = sorted(names)
        for name in names:
            check('local input '+name, (HERE/name).resolve().is_relative_to(HERE.parent.parent))
            report['input_sha256'][name] = digest(name)
        for name, value in cert['input_sha256'].items():
            check('producer manifest '+name, digest(name) == value)
        for tag, audit in audits.items():
            check(tag+' successful original audit', audit['failures'] == [] and audit['original_artifacts_byte_unchanged'])
            if tag == 'l125':
                check('L125 complete old-schema verdict', audit['full_saved_replay_identical'] and
                      audit['summary']['actual_cases'] == audit['summary']['required_cases'] == 100764)
            else:
                check('L148 every prior check', bool(audit['checks']) and all(c['passes'] for c in audit['checks']))
            for name, value in manifests[tag].items():
                check(tag+' full manifest '+name, digest(name) == value)
        check('code and complete certificate bindings', cert['code_sha256'] == digest(programs[0]) and
              replay['code_sha256'] == digest(programs[1]) and replay['certificate_sha256'] == digest(outputs[0]) and
              cert['failures'] == replay['failures'] == [] and cert['original_inputs_unchanged'])
        for name, value in replay['helper_sha256'].items():
            check('verifier helper '+name, digest(name) == value)
        # All top-level assignments and all called helper bodies were manually read.
        # Confirm that no uninspected top-level execution or historical main runs.
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

        master, prior = read('new-pair-filter.json'), read('l147-literal-reuse.json')
        universe = sorted([[sorted(set(a)&set(S)), sorted(set(a)-set(S))]
                           for a in combinations(H,4) if len(set(a)&set(S)) == 2])
        check('complete support universe', len(universe) == 756 and universe == master['universe'] and
              cert['S'] == S and cert['H'] == H and cert['J'] == sorted(set(H)-set(S)) and cert['modulus'] == P)
        check('exact domain and historical list', cert['selected_manifest'] == prior['unmatched_indices'] == MANIFEST and
              [r['indices'] for r in cert['records']] == [r['indices'] for r in replay['records']] == MANIFEST and
              len(master['residual_occurrences']) == 154 and prior['historical_residual_occurrences'] == master['residual_occurrences'])
        check('actual fixed pair', [universe[n] for n in master['first_indices']] == [[[1,8],[47,50]],[[12,18],[64,75]]])
        lemma = (HERE.parent.parent/'lemmas/L149-l148-rank20-selected-row-classification.md').read_text()
        total_ext = total_proj = total_mom = total_pointwise = 0
        exclusions, survivors, plane_keys = [], [], set()
        expected_minors = [78,54,18,52,67,29,19,57]
        for index, rec, rebuilt, classified, expected_minor in zip(
                MANIFEST, cert['records'], replay['records'], replay['classification'], expected_minors, strict=True):
            tag = str(index)+' '
            old = next(r for r in prior['overlay'] if r['indices'] == index)
            shard = read(rec['shard'])
            case = shard['cases'][int(rec['case_pointer'].split('/')[-1])]
            check(tag+'complete original record', digest(rec['shard']) == manifests['l125'][rec['shard']] == manifests['l148'][rec['shard']] and
                  shard['third_index'] == index[0] and [r for r in shard['cases'] if r['fourth_index'] == index[1]] == [case] and
                  case == rec['complete_original_record'] == old['complete_original_record'] and case['status'] == 'residual' and
                  old['disposition'] == 'unmatched' and old['mismatch'] == dict(kind='basis_length',actual=1,source=2) and
                  rec['case_pointer'] == old['case_pointer'] and rec['shard'] == old['shard'])
            rows = [dict(I=universe[n][0],K=universe[n][1]) for n in master['first_indices']+index]
            check(tag+'complete original rows', rec['rows'] == old['rows'] == classified['rows'] == rows and
                  rec['row_inputs'] == old['row_inputs'] and rec['original_matrix'] == old['original_matrix'] and
                  rec['kernel_basis'] == old['kernel_basis'] == case['kernel_basis'])
            matrix, [p] = rec['original_matrix'], rec['kernel_basis']
            free = rec['free_columns']
            check(tag+'nonzero whole extension-kernel certificate', len(matrix) == 24 and all(len(r) == 21 for r in matrix) and
                  len(p) == 21 and len(free) == 1 and p[free[0]] == 1 and
                  free == sorted(set(range(21))-set(case['pivot_columns'])) and
                  [[sum(x*y for x,y in zip(row,p))%P for row in matrix]] == rec['kernel_residuals'] == case['kernel_residuals'] == [[0]*24])
            rr, cc = rec['rank_minor_rows'], rec['rank_minor_columns']
            check(tag+'original minor indices', rr == case['minor_rows'] and cc == case['pivot_columns'] and
                  len(rr) == len(set(rr)) == len(cc) == len(set(cc)) == case['rank'] == 20 and
                  all(0 <= r < 24 for r in rr) and all(0 <= c < 21 for c in cc))
            det = integer_determinant([[matrix[r][c] for c in cc] for r in rr])
            check(tag+'exact rational determinant', det%P == expected_minor == rec['rank_minor_residue'] == case['minor_residue'] == classified['minor'] != 0)
            point = rec['plane_and_all_row_gates']
            u, v = point['u'], point['v']
            check(tag+'canonical plane and all homogeneous identities',
                  [(u[a]*v[b]-u[b]*v[a])%P for a,b in PAIRS] == p == point['bivector'] and
                  rec['plucker_values'] == [0]*35 and rec['decomposable'] and
                  u[:2] == [1,0] and v[0] == 0 and v[1] != 0 and classified['u'] == u and classified['v'] == v)
            check(tag+'complete fresh kernel', len(rebuilt['independent_kernel']) == 1 and
                  any(rebuilt['independent_kernel'][0]) and all(sum(a*b for a,b in zip(row,rebuilt['independent_kernel'][0]))%P == 0 for row in matrix))
            plane_keys.add(tuple(u))
            plane_name = {(1,0,40,56,96,57,34):'P',(1,0,74,77,45,42,87):'Q',
                          (1,0,31,55,34,85,3):'R',(1,0,48,9,44,54,1):'T'}[tuple(u)]
            check(tag+'displayed plane table', f"| {plane_name} | ({','.join(map(str,u))}) | ({','.join(map(str,v))}) |" in lemma)
            for rn, (row, gate, restored, table) in enumerate(zip(rows,point['row_gates'],rebuilt['row_replay'],classified['row_gates'],strict=True)):
                alpha,beta = gate['direction_coefficients']
                lam, weights = gate['lambda_value'], gate['error_weights']
                h = [(alpha*x+beta*y)%P for x,y in zip(u,v)]
                check(tag+f'row {rn} complete gate and original moments', gate['projection_rank'] == 1 and
                      gate['projection_minors'] == [0]*6 and any(gate['Q_u']+gate['Q_v']) and any(h) and h == gate['intersection_vector'] and
                      restored['direction'] == table['direction'] == [alpha,beta] and restored['lambda_value'] == table['lambda_value'] == lam and
                      restored['weights'] == table['weights'] == weights and restored['failed_gates'] == table['failed_gates'] == gate['failed_gates'] and
                      gate['prescribed_finite_gate'] == {'D_coefficient':alpha,'C_coefficient':-beta%P} and
                      gate['moment_residuals'] == [0]*8 and gate['h_minus_error_minus_lambda_g_on_H'] == [0]*16)
                mm = [[sum(w[S.index(x)]*pow(x,d,P) for x in S)%P for w in (u,v)] + [-pow(x,d,P)%P for x in row['I']+row['K']] for d in range(1,9)]
                check(tag+f'row {rn} entire moment matrix and null line', mm == restored['moment_matrix'] and
                      restored['moment_rank'] == 5 and len(restored['moment_kernel']) == 6 and any(restored['moment_kernel']) and
                      all(sum(a*b for a,b in zip(r,restored['moment_kernel']))%P == 0 for r in mm))
                line = f"| {plane_name} | {','.join(map(str,row['I']))}; {','.join(map(str,row['K']))} | ({alpha},{beta}) | {lam} | ({','.join(map(str,weights))}) |"
                check(tag+f'row {rn} exact displayed table', line in lemma)
                total_mom += 8
                total_pointwise += 16
            pivots = [list(pair) for pair,value in zip(PAIRS,p) if value]
            expected_choices = []
            # Enumerate all nonzero exterior and projection pivots, without
            # trusting a count. Independently rebuild each alternative plane.
            skew = [[0]*7 for _ in S]
            for (a,b),value in zip(PAIRS,p):
                skew[a][b],skew[b][a] = value,-value%P
            for a,b in pivots:
                uu = [skew[x][b]*pow(skew[a][b],-1,P)%P for x in range(7)]
                vv = skew[a]
                for rn, inp in enumerate(rec['row_inputs']):
                    q = inp['original_block']['covectors']
                    aa,bb = [[sum(c*w for c,w in zip(cov,w))%P for cov in q] for w in (uu,vv)]
                    for m in range(4):
                        if aa[m] or bb[m]:
                            expected_choices.append(([a,b],rn+1,m))
            check(tag+'complete alternative-pivot domain', [(a['pivot'],a['row'],a['component']) for a in rebuilt['all_pivot_replay']] == expected_choices)
            for alt in rebuilt['all_pivot_replay']:
                gate = point['row_gates'][alt['row']-1]
                check(tag+'nonzero alternative scale '+str((alt['pivot'],alt['row'],alt['component'])), alt['scale']%P != 0 and
                      alt['lambda_value'] == alt['scale']*gate['lambda_value']%P and
                      alt['error_weights'] == [alt['scale']*x%P for x in gate['error_weights']])
            total_ext += len(pivots)
            total_proj += len(expected_choices)
            passes = all(g['passes'] for g in point['row_gates'])
            disposition = 'intrinsic_survivor' if passes else 'excluded_necessary_gates'
            check(tag+'complete disposition', rec['disposition'] == classified['disposition'] == disposition and point['passes_intrinsic_gates'] == passes)
            if passes:
                survivors.append(index)
                check(tag+'all full weights and distinct directions', all(g['lambda_value'] and all(g['error_weights']) for g in point['row_gates']) and all(rebuilt['direction_determinants']))
            else:
                exclusions.append(index)
                check(tag+'only first-row failure', point['row_gates'][0]['failed_gates'] == ['lambda_zero'] and
                      point['row_gates'][0]['error_weights'][2:] == [0,0] and all(point['row_gates'][0]['error_weights'][:2]) and
                      all(g['passes'] for g in point['row_gates'][1:]))
            report['records'].append(dict(indices=index,integer_determinant=det,residue=det%P,
                complete_kernel=p,plane=plane_name,disposition=disposition,
                exterior_pivots=len(pivots),projection_pivots=len(expected_choices)))
        check('exact exclusions and survivors', exclusions == [[499,668],[668,499],[678,749],[749,678]] and
              survivors == [[467,750],[608,695],[695,608],[750,467]] and len(plane_keys) == 4)
        groups = replay['plane_groups']
        check('four distinct planes and both orders', len(groups) == 4 and
              all(g['indices'] == [r['indices'] for r in replay['classification'] if r['u'] == g['u'] and r['v'] == g['v']] and
                  len(g['indices']) == 2 and g['indices'][0] == list(reversed(g['indices'][1])) for g in groups) and
              sum(g['disposition'] == 'intrinsic_survivor' for g in groups) == 2)
        summary = dict(actual_records=8,required_records=8,rank=20,kernel_dimension=1,nonzero_original_minors=8,
            original_entries=4032,plucker_values=280,decomposable_points=8,
            dispositions={'intrinsic_survivor':4,'excluded_necessary_gates':4},projection_ranks={'1':32},failed_gates={'lambda_zero':4})
        check('all reported counts', cert['summary'] == summary and replay['summary'] == dict(summary,
              all_nonzero_exterior_pivots=124,all_nonzero_projection_pivots=1882,original_moment_matrices_rank5=32,
              original_moment_residuals=256,pointwise_entries=512,distinct_planes=4,surviving_planes=2,source_files_unchanged=496) and
              (total_ext,total_proj,total_mom,total_pointwise) == (124,1882,256,512))
        with TemporaryDirectory(prefix='l149-audit-',dir=HERE) as temp:
            isolated = Path(temp)/'reed-solomon-mca'/'scripts'/'seven-coordinate'
            for name in names:
                target = isolated/name
                target.parent.mkdir(parents=True,exist_ok=True)
                shutil.copyfile(HERE/name,target)
            for program in programs:
                result = subprocess.run([sys.executable,'-E','-B',str(isolated/program)],
                    cwd=isolated.parent.parent,capture_output=True,text=True,check=False)
                report['runs'].append(dict(program=program,returncode=result.returncode,
                    stdout=result.stdout.replace(temp,'<isolated-copy>'),stderr=result.stderr.replace(temp,'<isolated-copy>')))
                check('complete isolated execution '+program,result.returncode == 0)
            for name in names:
                check('full-byte isolated reproduction/preservation '+name,
                      sha256((isolated/name).read_bytes()).hexdigest() == report['input_sha256'][name])
        report['summary'] = dict(summary,exterior_pivots=total_ext,projection_pivots=total_proj,
            original_moments=total_mom,pointwise_entries=total_pointwise,distinct_planes=4,surviving_planes=2,
            bound_original_files=len(names),byte_identical_outputs=2,required_outputs=2)
        report['exclusions'],report['survivors'] = exclusions,survivors
    except Exception as error:
        report['failures'].append(f'{type(error).__name__}: {error}')
    finally:
        preserved = all(digest(name) == value for name,value in report['input_sha256'].items())
        report['original_artifacts_byte_unchanged'] = preserved
        if not preserved:
            report['failures'].append('Original input changed')
        report['audit_code_sha256'] = sha256(Path(__file__).read_bytes()).hexdigest()
        report['qualification'] = 'Separate restricted audit; shared Python/residue arithmetic and inherited finite certificates; no added rows, assembly or global improvement.'
        target = HERE/'l149-critical-audit.json'
        target.write_text(json.dumps(report,indent=2)+'\n')
        print(json.dumps(report.get('summary',{}),sort_keys=True))
        print(f"Checks {sum(c['passes'] for c in report['checks'])}/{len(report['checks'])}; failures {report['failures']}; originals unchanged {preserved}; certificate {target}")
    if report['failures']:
        raise SystemExit(1)


if __name__ == '__main__':
    run()
