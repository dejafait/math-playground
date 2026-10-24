"""Separate bounded L138 audit; replay literal imports, never enlarge the target.

Run from the notebook: python3 -E -B scripts/seven-coordinate/audit_l138.py
Both original programs execute in isolation; original artifacts stay unchanged.
"""
from hashlib import sha256
from itertools import combinations
from pathlib import Path
from tempfile import TemporaryDirectory
import json
import os
import shutil
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
P = 97


def run():
    report = dict(step_id='2026-10-23-mca-411-l138-critical-audit',
                  checks=[], failures=[], input_sha256={}, runs=[],
                  complete_occurrence_checks=[], source_checks=[])

    def check(name, condition):
        report['checks'].append(dict(name=name, passes=bool(condition)))
        if not condition:
            raise ValueError(name)

    def read(name):
        return json.loads((HERE/name).read_bytes())

    def digest(name):
        return sha256((HERE/name).read_bytes()).hexdigest()

    try:
        check('audit assertions enabled', __debug__)
        saved = read('l137-literal-reuse.json')
        replay = read('l137-literal-reuse-replay.json')
        prior_audit = read('l136-critical-audit.json')
        names = sorted(set(saved['input_sha256']) | set(prior_audit['input_sha256']) | {
            'l137_literal_reuse.py', 'verify_l137_literal_reuse.py',
            'l137-literal-reuse.json', 'l137-literal-reuse-replay.json'})
        report['original_file_count'] = len(names)
        for name in names:
            check('notebook-local input ' + name, (HERE/name).resolve().is_relative_to(ROOT))
            report['input_sha256'][name] = digest(name)
        check('all original recorded input hashes', all(
            digest(name) == value for name, value in saved['input_sha256'].items()))
        check('original output/code provenance',
              saved['code_sha256'] == digest('l137_literal_reuse.py') and
              replay['certificate_sha256'] == digest('l137-literal-reuse.json') and
              replay['verifier_sha256'] == digest('verify_l137_literal_reuse.py'))
        check('no saved failures', saved['failures'] == replay['failures'] == [])
        with TemporaryDirectory(prefix='l138-audit-', dir=HERE) as temp:
            isolated = Path(temp)/'scripts'/'seven-coordinate'
            isolated.mkdir(parents=True)
            for name in names:
                destination = isolated/name
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(HERE/name, destination)
            environment = dict(os.environ)
            environment.pop('PYTHONOPTIMIZE', None)
            for program in ('l137_literal_reuse.py', 'verify_l137_literal_reuse.py'):
                completed = subprocess.run(
                    [sys.executable, '-E', '-B', str(isolated/program)],
                    env=environment, capture_output=True, text=True, check=False)
                report['runs'].append(dict(program=program, returncode=completed.returncode,
                    stdout=completed.stdout.replace(temp, '<isolated-copy>'),
                    stderr=completed.stderr.replace(temp, '<isolated-copy>')))
                check(program + ' assertions-enabled isolated run', completed.returncode == 0)
            for name in ('l137-literal-reuse.json', 'l137-literal-reuse-replay.json'):
                check(name + ' full byte reproduction',
                      (isolated/name).read_bytes() == (HERE/name).read_bytes())
            check('every isolated input and output remains byte identical', all(
                sha256((isolated/name).read_bytes()).hexdigest() == value
                for name, value in report['input_sha256'].items()))

        master = read('new-pair-filter.json')
        partition_audit = read('l125-critical-audit.json')
        s = [1, 8, 12, 18, 22, 27, 33]
        h = [x for x in range(1, P) if pow(x, 16, P) == 1]
        j = sorted(set(h)-set(s))
        universe = sorted([[sorted(set(a)&set(s)), sorted(set(a)-set(s))]
                           for a in combinations(h, 4) if len(set(a)&set(s)) == 2])
        check('full universe, field, seven-set and actual pair',
              len(universe) == 756 and universe == master['universe'] and
              (master['S'], master['H'], master['J']) == (s, h, j) and
              [universe[k] for k in master['first_indices']] ==
              [[[1, 8], [47, 50]], [[12, 18], [64, 75]]])
        historical = master['residual_occurrences']
        check('full 154 list preserved', historical == saved['historical_residual_occurrences']
              and len(historical) == len(set(map(tuple, historical))) == 154)
        previous = read('l135-literal-reuse.json')
        previous_replay = read('l135-literal-reuse-replay.json')
        check('L136 audit and complete input hash map', prior_audit['failures'] == [] and
              all(c['passes'] for c in prior_audit['checks']) and
              prior_audit['original_artifacts_byte_unchanged'] and
              all(digest(name) == value for name, value in prior_audit['input_sha256'].items()))
        l132 = read('residual-locus-reuse.json')
        l132_replay = read('residual-locus-reuse-replay.json')
        l134 = read('l133-literal-reuse.json')
        l134_replay = read('l133-literal-reuse-replay.json')
        for identifier, size, earlier, earlier_replay in (
                ('l132', 118, l132, l132_replay), ('l134', 100, l134, l134_replay)):
            values = earlier['unmatched_indices']
            check(identifier + ' complete historical list and replay retained',
                  saved['historical_'+identifier+'_mismatches'] ==
                  previous['historical_'+identifier+'_mismatches'] == values ==
                  earlier_replay['unmatched_indices'] and
                  len(values) == len(set(map(tuple, values))) == size and
                  earlier['failures'] == earlier_replay['failures'] == [])
        check('exact 82 historical mismatches and single removal',
              saved['historical_l136_mismatches'] == previous['unmatched_indices'] ==
              previous_replay['unmatched_indices'] and
              len(previous['unmatched_indices']) == len(set(map(tuple, previous['unmatched_indices']))) == 82 and
              previous['unmatched_indices'].count([175, 238]) == 1 and
              saved['removed_only'] == [[175, 238]])
        expected_scope = [x for x in previous['unmatched_indices'] if x != [175, 238]]
        check('exact complete ordered 81-case scope', len(expected_scope) == 81 and
              saved['required_scope_indices'] == expected_scope)
        metadata = {m['third_index']: m for m in master['thirds']}
        shard_cases = {}
        for n in sorted({n for n, u in historical}):
            meta = metadata[n]
            name = meta['certificate']
            shard = read(name)
            check(f'third {n} complete audited residual list',
                  digest(name) == meta['sha256'] == partition_audit['audited_input_hashes'][name] and
                  shard['third_index'] == n and shard['failures'] == [] and
                  shard['residual_indices'] == [u for a, u in historical if a == n] ==
                  [c['fourth_index'] for c in shard['cases'] if c['status'] == 'residual'])
            shard_cases[n] = shard['cases']
        t = [239, 240, 241, 246, 248, 249, 250, 251]
        expected_matched = sorted([[175, x] for x in t] + [[x, 175] for x in [238]+t])
        check('all 17 displayed indices and 64 complementary mismatches',
              saved['covered_indices'] == expected_matched and
              saved['unmatched_indices'] == [x for x in expected_scope if x not in expected_matched] and
              len(saved['unmatched_indices']) == 64)
        check('one old exchange and sixteen additional ordered bindings',
              [238, 175] in expected_matched and len(expected_matched) == 17 and
              [175, 238] not in expected_matched)
        check('one complete source import', len(saved['source_imports']) == 1 and
              saved['source_imports'][0]['lemma'] == 'L137')
        imported = saved['source_imports'][0]
        source = read(imported['certificate'])
        source_replay = read(imported['replay'])
        audit = read(imported['audit'])
        check('L137 full separate audit and all bound inputs', audit['failures'] == [] and
              all(c['passes'] for c in audit['checks']) and
              all(digest(name) == value for name, value in audit['input_sha256'].items()))
        cols = list(combinations(range(7), 2))
        expected_basis = [[int(k == 1) for k in range(21)],
                          [{0:55, 6:68, 7:2, 8:44, 9:54, 10:1}.get(k, 0) for k in range(21)]]
        check('entire displayed ordered source basis',
              imported['kernel_basis'] == source['kernel_basis'] == expected_basis)
        locus = imported['imported_locus']
        check('exact full locus field set', set(locus) == {
            'plucker_quadruples', 'plucker_coefficients_s2_st_t2', 'affine_gcd',
            'bezout_coefficients', 'affine_quotients', 'complete_projective_parameter_locus'})
        coefficients = [[0, {0:95, 1:53, 2:43, 3:96}.get(k, 0), 0] for k in range(35)]
        check('full homogeneous, affine and infinity import',
              locus == {key: source[key] for key in locus} and
              locus['plucker_quadruples'] == list(map(list, combinations(s, 4))) and
              locus['plucker_coefficients_s2_st_t2'] == coefficients ==
              source_replay['plucker_coefficients_s2_st_t2'] and
              locus['affine_gcd'] == [0, 1] and
              locus['complete_projective_parameter_locus'] == [[1, 0], [0, 1]])
        check('every saved quotient and exact Bezout coefficient',
              locus['affine_quotients'] == [[v[1]] if v[1] else [] for v in coefficients] and
              locus['bezout_coefficients'] == [[96] if k == 3 else [] for k in range(35)] and
              96*96 % P == 1)
        check('both point bindings use the first row', len(imported['point_bindings']) == 2 and
              [v['source_row_number'] for v in imported['point_bindings']] == [1, 1])
        tables = [(81, 0, [81, 0, 0, 0]), (0, 28, [0, 85, 0, 0])]
        expected_planes = [([1,0,0,0,0,0,0], [0,0,1,0,0,0,0]),
                           ([1,0,94,37,38,29,67], [0,55,0,0,0,0,0])]
        for pi, binding in enumerate(imported['point_bindings']):
            point = source['points_and_all_row_gates'][pi]
            gate = binding['unchanged_rejecting_gate']
            alpha, beta, weights = tables[pi]
            row_input = binding['row_input']
            label_order = row_input['I']+row_input['K']
            rows = [r for r in source_replay['all_row_replay']
                    if r['point_index'] == pi and r['row_number'] == 1]
            check(f'point {pi} complete plane and rejecting gate',
                  binding['source_point_index'] == pi and
                  binding['plane_representative'] == {key: point[key] for key in
                      ('u', 'v', 'bivector', 'pivot_indices')} and
                  (point['u'], point['v']) == expected_planes[pi] and
                  [(point['u'][a]*point['v'][b]-point['u'][b]*point['v'][a]) % P
                   for a,b in cols] == point['bivector'] == expected_basis[pi] and
                  gate == point['row_gates'][0] and gate['projection_rank'] == 1 and
                  gate['lambda_value'] == 0 and gate['passes'] is False and
                  'lambda_zero' in gate['failed_gates'] and gate['error_weights'] == weights and
                  gate['direction_coefficients'] == [alpha, beta] and
                  len(rows) == 1 and rows[0]['error'] == dict(zip(map(str, label_order), weights)))
            check(f'point {pi} complete fixed first-row polynomial and original block',
                  row_input['I'] == [1,8] and row_input['K'] == [47,50] and
                  row_input['z'] == 12 and row_input['original_block'] == source['blocks'][0] and
                  row_input['g_roots'] == [64,70,75,79,85,89,96] and
                  row_input['g_coefficients_ascending'] == [50,81,21,43,16,83,24,1] and
                  row_input['g_values_on_S_union_K']['12'] == 44)
            q = row_input['original_block']['covectors']
            dot = lambda a,b: sum(x*y for x,y in zip(a,b)) % P
            qu, qv = [[dot(c,v) for c in q] for v in (point['u'], point['v'])]
            vector = [(alpha*x+beta*y) % P for x,y in zip(point['u'],point['v'])]
            values = {int(k): v for k,v in row_input['g_values_on_S_union_K'].items()}
            lam = vector[s.index(12)]*pow(values[12], -1, P) % P
            errors = {x: ((vector[s.index(x)] if x in s else 0)-lam*values[x]) % P
                      for x in label_order}
            moments = [sum(((vector[s.index(x)] if x in s else 0)-errors.get(x,0))*
                           pow(x,d,P) for x in h) % P for d in range(1,9)]
            pointwise = [((vector[s.index(x)] if x in s else 0)-errors.get(x,0)-
                          lam*values.get(x,0)) % P for x in h]
            check(f'point {pi} exact projection rank, original moments and chart coefficients',
                  qu == gate['Q_u'] and qv == gate['Q_v'] and any(qu+qv) and
                  all((qu[a]*qv[b]-qu[b]*qv[a]) % P == 0 for a,b in combinations(range(4),2)) and
                  vector == gate['intersection_vector'] and any(vector) and lam == 0 and
                  list(errors.values()) == weights and moments == gate['moment_residuals'] == [0]*8 and
                  pointwise == gate['h_minus_error_minus_lambda_g_on_H'] == [0]*16 and
                  gate['prescribed_finite_gate'] == dict(D_coefficient=alpha,C_coefficient=-beta % P) and
                  gate['original_first_coefficient'] == '(D*alpha-C*beta)/(AD-BC)' and
                  gate['original_basis_convention'] == 'u_original=A*u+B*v; v_original=C*u+D*v; AD-BC!=0' and
                  binding['original_row_replay'] == rows[0])
            skew = [[0]*7 for _ in s]
            for (a,b), value in zip(cols,point['bivector']):
                skew[a][b], skew[b][a] = value, -value % P
            pivots = []
            for a,b in cols:
                if not skew[a][b]:
                    continue
                pu = [skew[x][b]*pow(skew[a][b],-1,P) % P for x in range(7)]
                pv = skew[a][:]
                pqu,pqv = [[dot(c,v) for c in q] for v in (pu,pv)]
                for component,(x,y) in enumerate(zip(pqu,pqv)):
                    if not (x or y):
                        continue
                    direction = [-y % P,x]
                    ph = [(direction[0]*v+direction[1]*w) % P for v,w in zip(pu,pv)]
                    pivot = next(k for k,value in enumerate(vector) if value)
                    scalar = ph[pivot]*pow(vector[pivot],-1,P) % P
                    plam = ph[s.index(12)]*pow(values[12],-1,P) % P
                    pe = [((ph[s.index(x)] if x in s else 0)-plam*values[x]) % P for x in label_order]
                    check(f'point {pi} pivot {a},{b} component {component} same failed line',
                          scalar != 0 and ph == [scalar*v % P for v in vector] and
                          plam == 0 and pe == [scalar*v % P for v in weights])
                    pivots.append(dict(point=pi,exterior_pivot=[a,b],row=1,
                        projection_component=component,direction=direction,scalar=scalar,
                        h=ph,lambda_value=plam,error_weights=pe))
            check(f'point {pi} every nonzero pivot record complete',
                  len(pivots) == [4,24][pi] and pivots == binding['all_nonzero_pivot_replay'] ==
                  [r for r in source_replay['all_pivot_replay'] if r['point'] == pi and r['row'] == 1])
        check('complete source replay hash, matrix and null residual binding',
              source_replay['certificate_sha256'] == digest(imported['certificate']) and
              source_replay['rebuilt_original_matrix'] == source['original_matrix'] and
              source_replay['kernel_residuals'] == source['kernel_residuals'] and
              source_replay['failures'] == source['failures'] == [])
        report['source_checks'].append(dict(lemma='L137',complete_import=imported,
            complete_audit_checks=audit['checks'],replay_sha256=digest(imported['replay'])))
        check('exact 81 overlay order', [e['indices'] for e in saved['overlay']] == expected_scope)
        for entry in saved['overlay']:
            n,u = entry['indices']
            index = int(entry['case_pointer'].split('/')[-1])
            record = shard_cases[n][index]
            check(f'{n},{u} complete original record and single comparison',
                  record == entry['complete_original_record'] and record['fourth_index'] == u and
                  len([c for c in shard_cases[n] if c['fourth_index'] == u]) == 1 and
                  [c['source'] for c in entry['comparisons']] == ['L137'])
            prior_entry = next(e for e in previous['overlay'] if e['indices'] == [n,u])
            check(f'{n},{u} complete L136 mismatch provenance',
                  prior_entry['complete_original_record'] == record and prior_entry['disposition'] == 'unmatched' and
                  prior_entry['shard'] == entry['shard'] and prior_entry['case_pointer'] == entry['case_pointer'])
            check(f'{n},{u} exact stated index set',
                  entry['comparisons'][0]['covered'] == entry['comparisons'][0]['literal_ordered_basis_equal'] ==
                  ([n,u] in expected_matched))
            report['complete_occurrence_checks'].append(dict(indices=[n,u],shard=entry['shard'],
                case_pointer=entry['case_pointer'],
                record_sha256=sha256(json.dumps(record,sort_keys=True).encode()).hexdigest(),
                complete_comparisons=entry['comparisons']))
        check('full replay bounds and counts', replay['summary'] == saved['summary'] and
              replay['original_entries_rebuilt'] == 40824 and replay['null_residual_entries_replayed'] == 3696 and
              saved['summary']['actual_tested'] == saved['summary']['required_tested'] == 81 and
              saved['summary']['literal_basis_comparisons'] == 81 and
              saved['summary']['matched_point_row_bindings'] == 34 and
              saved['summary']['rank_histogram_in_scope'] == {'19':73,'20':8})
        check('all original inputs and outputs unchanged', all(
            digest(name) == value for name,value in report['input_sha256'].items()))
        report['summary'] = saved['summary']
        report['original_artifacts_byte_unchanged'] = True
        report['qualification'] = ('Separate audit of restricted reproduced L138 input only; '
            'shared Python/residue arithmetic and inherited finite-certificate assumptions. '
            'No new locus, changed-row test, assembly, universal extraction or global bound.')
    except Exception as error:
        report['failures'].append(str(error))
    report['audit_code_sha256'] = sha256(Path(__file__).read_bytes()).hexdigest()
    out = HERE/'l138-critical-audit.json'
    out.write_text(json.dumps(report,indent=2)+'\n')
    print(f"Checks {sum(c['passes'] for c in report['checks'])}/{len(report['checks'])}; "
          f"occurrences {len(report['complete_occurrence_checks'])}/81; "
          f"failures {len(report['failures'])}; certificate: {out}")
    if report['failures']:
        print('Failures:',report['failures'])
        raise SystemExit(1)
    print('Complete fresh replay: 81/81 comparisons; 17 imports; '
          '34/34 point-row bindings; 64 mismatches preserved; original files unchanged.')


if __name__ == '__main__':
    run()
