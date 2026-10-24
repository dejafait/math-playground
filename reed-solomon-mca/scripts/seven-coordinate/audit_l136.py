"""Separate bounded L136 audit; no new locus, row mechanism or filter.

Run from the notebook: python3 -E -B scripts/seven-coordinate/audit_l136.py
Replay full original programs in an isolated copy; preserve original inputs.
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
    report = dict(step_id='2026-10-22-mca-402-l136-critical-audit',
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
        saved = read('l135-literal-reuse.json')
        replay = read('l135-literal-reuse-replay.json')
        prior_map = read('l134-critical-audit.json')['input_sha256']
        names = sorted(set(saved['input_sha256']) | set(prior_map) | {
            'l135_literal_reuse.py', 'verify_l135_literal_reuse.py',
            'l135-literal-reuse.json', 'l135-literal-reuse-replay.json'})
        report['original_file_count'] = len(names)
        for name in names:
            check('notebook-local input ' + name,
                  (HERE/name).resolve().is_relative_to(ROOT))
            report['input_sha256'][name] = digest(name)
        check('all original recorded input hashes', all(
            digest(name) == value for name, value in saved['input_sha256'].items()))
        check('original output/code provenance',
              saved['code_sha256'] == digest('l135_literal_reuse.py') and
              replay['certificate_sha256'] == digest('l135-literal-reuse.json') and
              replay['verifier_sha256'] == digest('verify_l135_literal_reuse.py'))
        check('no saved failures', saved['failures'] == replay['failures'] == [])
        # Recreate the relative ../../lemmas layout. Only reviewed run() bodies
        # execute; imported derivative helper has no execution on import.
        with TemporaryDirectory(prefix='l136-audit-', dir=HERE) as temp:
            isolated = Path(temp)/'scripts'/'seven-coordinate'
            isolated.mkdir(parents=True)
            for name in names:
                destination = isolated/name
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(HERE/name, destination)
            environment = dict(os.environ)
            environment.pop('PYTHONOPTIMIZE', None)
            for program in ('l135_literal_reuse.py', 'verify_l135_literal_reuse.py'):
                completed = subprocess.run(
                    [sys.executable, '-E', '-B', str(isolated/program)],
                    env=environment, capture_output=True, text=True, check=False)
                report['runs'].append(dict(program=program, returncode=completed.returncode,
                    stdout=completed.stdout.replace(temp, '<isolated-copy>'),
                    stderr=completed.stderr.replace(temp, '<isolated-copy>')))
                check(program + ' assertions-enabled isolated run', completed.returncode == 0)
            for name in ('l135-literal-reuse.json', 'l135-literal-reuse-replay.json'):
                check(name + ' full byte reproduction',
                      (isolated/name).read_bytes() == (HERE/name).read_bytes())
            check('every isolated input and output remains byte identical', all(
                sha256((isolated/name).read_bytes()).hexdigest() == value
                for name, value in report['input_sha256'].items()))

        master = read('new-pair-filter.json')
        prior = read('l125-critical-audit.json')
        s = [1, 8, 12, 18, 22, 27, 33]
        h = [x for x in range(1, P) if pow(x, 16, P) == 1]
        j = sorted(set(h)-set(s))
        # Independent four-subset construction, then split and sort by (I,K).
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
        previous = read('l133-literal-reuse.json')
        previous_replay = read('l133-literal-reuse-replay.json')
        previous_audit = read('l134-critical-audit.json')
        check('L134 audit and complete input hash map',
              previous_audit['failures'] == [] and
              all(c['passes'] for c in previous_audit['checks']) and
              all(digest(name) == value for name, value in previous_audit['input_sha256'].items()))
        l132 = read('residual-locus-reuse.json')
        l132_replay = read('residual-locus-reuse-replay.json')
        check('full historical 118 list and L132 provenance retained',
              saved['historical_l132_mismatches'] == previous['historical_l132_mismatches'] ==
              l132['unmatched_indices'] == l132_replay['unmatched_indices'] and
              len(l132['unmatched_indices']) == len(set(map(tuple, l132['unmatched_indices']))) == 118 and
              l132_replay['certificate_sha256'] == digest('residual-locus-reuse.json') and
              l132['failures'] == l132_replay['failures'] == [])
        check('exact 100 historical mismatches and single removal',
              saved['historical_l134_mismatches'] == previous['unmatched_indices'] ==
              previous_replay['unmatched_indices'] and
              len(previous['unmatched_indices']) == len(set(map(tuple, previous['unmatched_indices']))) == 100 and
              previous['unmatched_indices'].count([94, 539]) == 1 and
              saved['removed_only'] == [[94, 539]])
        expected_scope = [x for x in previous['unmatched_indices'] if x != [94, 539]]
        check('exact complete ordered 99-case scope', len(expected_scope) == 99 and
              saved['required_scope_indices'] == expected_scope)
        metadata = {m['third_index']: m for m in master['thirds']}
        shard_cases = {}
        for n in sorted({n for n, u in historical}):
            meta = metadata[n]
            name = meta['certificate']
            shard = read(name)
            check(f'third {n} complete audited residual list',
                  digest(name) == meta['sha256'] == prior['audited_input_hashes'][name] and
                  shard['third_index'] == n and shard['failures'] == [] and
                  shard['residual_indices'] == [u for a, u in historical if a == n] ==
                  [c['fourth_index'] for c in shard['cases'] if c['status'] == 'residual'])
            shard_cases[n] = shard['cases']

        t = [95, 96, 97, 102, 103, 104, 105, 106]
        expected_sets = {'L135': sorted([[x, 539] for x in t] + [[539, x] for x in [94]+t])}
        expected_matched = expected_sets['L135']
        check('all 17 displayed indices and 82 complementary mismatches',
              saved['covered_indices'] == expected_matched and
              saved['unmatched_indices'] == [x for x in expected_scope if x not in expected_matched] and
              len(saved['unmatched_indices']) == 82)
        check('one old exchange and sixteen additional ordered bindings',
              [539, 94] in expected_matched and len(expected_matched) == 17 and
              [94, 539] not in expected_matched)
        imports = {x['lemma']: x for x in saved['source_imports']}
        check('exact one imported source', len(saved['source_imports']) == 1 and set(imports) == {'L135'})
        expected_mixed = {'L135': {0: 13, 10: 63, 11: 62, 12: 1}}
        tables = {'L135': [(12, 0, 0, 12, [12, 0, 0, 0]),
                          (44, 0, 0, 44, [0, 78, 0, 0])]}
        for lemma, imported in imports.items():
            source = read(imported['certificate'])
            source_replay = read(imported['replay'])
            audit = read(imported['audit'])
            checks = audit['checks']
            check(lemma + ' full separate audit and all bound inputs',
                  audit['failures'] == [] and
                  (all(v is True for v in checks.values()) if isinstance(checks, dict)
                   else all(c['passed'] is True for c in checks)) and
                  all(digest(name) == value['sha256'] for name, value in audit['inputs'].items()))
            locus = imported['imported_locus']
            check('exact full locus field set', set(locus) == {
                'plucker_quadruples', 'plucker_coefficients_s2_st_t2', 'affine_gcd',
                'bezout_coefficients', 'affine_quotients', 'complete_projective_parameter_locus'})
            coefficients = [[0, expected_mixed[lemma].get(k, 0), 0] for k in range(35)]
            check(lemma + ' full homogeneous, affine and infinity import',
                  locus == {key: source[key] for key in locus} and
                  locus['plucker_quadruples'] == list(map(list, combinations(s, 4))) and
                  locus['plucker_coefficients_s2_st_t2'] == coefficients ==
                  source_replay['plucker_coefficients_s2_st_t2'] and
                  locus['affine_gcd'] == [0, 1] and
                  locus['complete_projective_parameter_locus'] == [[1, 0], [0, 1]])
            # These imported affine certificates consist only of constants times T.
            check(lemma + ' every saved quotient and Bezout coefficient',
                  locus['affine_quotients'] == [[v[1]] if v[1] else [] for v in coefficients] and
                  len(locus['bezout_coefficients']) == 35 and
                  all(len(v) <= 1 for v in locus['bezout_coefficients']) and
                  sum((u[0] if u else 0)*v[1] for u, v in
                      zip(locus['bezout_coefficients'], coefficients)) % P == 1)
            check(lemma + ' both point bindings and correct fixed rows',
                  len(imported['point_bindings']) == 2 and
                  [v['source_row_number'] for v in imported['point_bindings']] ==
                  [2, 2])
            for pi, binding in enumerate(imported['point_bindings']):
                ri = binding['source_row_number']-1
                point = source['points_and_all_row_gates'][pi]
                gate = binding['unchanged_rejecting_gate']
                row = source['rows'][ri]
                q0, q1, alpha, beta, weights = tables[lemma][pi]
                label_order = row['I']+row['K']
                rows = [r for r in source_replay['all_row_replay']
                        if r['point_index'] == pi and r['row_number'] == ri+1]
                check(f'{lemma} point {pi} complete plane and rejecting gate',
                      binding['source_point_index'] == pi and
                      binding['plane_representative'] == {key: point[key] for key in
                          ('u', 'v', 'bivector', 'pivot_indices')} and
                      gate == point['row_gates'][ri] and
                      (gate['Q_u'][0], gate['Q_v'][0]) == (q0, q1) and
                      gate['direction_coefficients'] == [alpha, beta] and
                      gate['projection_rank'] == 1 and gate['lambda_value'] == 0 and
                      gate['error_weights'] == weights and len(set(label_order)) == 4 and
                      len(rows) == 1 and rows[0]['error'] == dict(zip(map(str, label_order), weights)) and
                      gate['moment_residuals'] == [0]*8 and
                      gate['h_minus_error_minus_lambda_g_on_H'] == [0]*16 and
                      gate['prescribed_finite_gate'] == dict(D_coefficient=alpha, C_coefficient=-beta % P) and
                      gate['original_first_coefficient'] == '(D*alpha-C*beta)/(AD-BC)')
                # Re-evaluate exactly the imported row, not any changed row.
                row_input = binding['row_input']
                check(f'point {pi} fixed row-two polynomial and original block',
                      row_input['I'] == [12, 18] and row_input['K'] == [64, 75] and
                      row_input['z'] == 1 and row_input['original_block'] == source['blocks'][1])
                q = row_input['original_block']['covectors']
                dot = lambda a, b: sum(x*y for x, y in zip(a, b)) % P
                qu, qv = [[dot(c, v) for c in q] for v in (point['u'], point['v'])]
                vector = [(alpha*x+beta*y) % P for x, y in zip(point['u'], point['v'])]
                values = {int(k): v for k, v in row_input['g_values_on_S_union_K'].items()}
                lam = vector[s.index(1)]*pow(values[1], -1, P) % P
                errors = {x: ((vector[s.index(x)] if x in s else 0)-lam*values[x]) % P
                          for x in label_order}
                moment = [sum(((vector[s.index(x)] if x in s else 0)-errors.get(x, 0))*
                              pow(x, power, P) for x in h) % P for power in range(1, 9)]
                pointwise = [((vector[s.index(x)] if x in s else 0)-errors.get(x, 0)-
                              lam*values.get(x, 0)) % P for x in h]
                check(f'point {pi} exact original moments and chart coefficients',
                      qu == gate['Q_u'] and qv == gate['Q_v'] and
                      vector == gate['intersection_vector'] and any(vector) and lam == 0 and
                      list(errors.values()) == weights and moment == gate['moment_residuals'] == [0]*8 and
                      pointwise == gate['h_minus_error_minus_lambda_g_on_H'] == [0]*16 and
                      binding['original_row_replay'] == rows[0])
                p = point['bivector']
                cols = list(combinations(range(7), 2))
                skew = [[0]*7 for _ in s]
                for (a, b), value in zip(cols, p):
                    skew[a][b], skew[b][a] = value, -value % P
                pivot_records = []
                for a, b in cols:
                    if not skew[a][b]:
                        continue
                    pu = [skew[x][b]*pow(skew[a][b], -1, P) % P for x in range(7)]
                    pv = skew[a][:]
                    pqu, pqv = [[dot(c, v) for c in q] for v in (pu, pv)]
                    for component, (x, y) in enumerate(zip(pqu, pqv)):
                        if not (x or y):
                            continue
                        direction = [-y % P, x]
                        ph = [(direction[0]*v+direction[1]*w) % P for v, w in zip(pu, pv)]
                        pivot = next(k for k, value in enumerate(vector) if value)
                        scalar = ph[pivot]*pow(vector[pivot], -1, P) % P
                        plam = ph[0]*pow(values[1], -1, P) % P
                        pe = [((ph[s.index(x)] if x in s else 0)-plam*values[x]) % P for x in label_order]
                        check(f'point {pi} pivot {a},{b} component {component} same failed line',
                              scalar != 0 and ph == [scalar*v % P for v in vector] and
                              plam == 0 and pe == [scalar*v % P for v in weights])
                        pivot_records.append(dict(point=pi, exterior_pivot=[a,b], row=2,
                            projection_component=component, direction=direction, scalar=scalar,
                            h=ph, lambda_value=plam, error_weights=pe))
                check(f'point {pi} every nonzero pivot record complete', pivot_records ==
                      binding['all_nonzero_pivot_replay'] ==
                      [r for r in source_replay['all_pivot_replay'] if r['point'] == pi and r['row'] == 2])
            second_row_pivots = [p for p in source_replay['all_pivot_replay'] if p['row'] == 2]
            check('complete source replay hash, matrix and null residual binding',
                  source_replay['certificate_sha256'] == digest(imported['certificate']) and
                  source_replay['rebuilt_original_matrix'] == source['original_matrix'] and
                  source_replay['kernel_residuals'] == source['kernel_residuals'] and
                  source_replay['failures'] == source['failures'] == [])
            report['source_second_row_pivot_evidence'] = second_row_pivots
            report['source_checks'].append(dict(lemma=lemma, complete_import=imported,
                complete_audit_checks=checks, replay_sha256=digest(imported['replay'])))

        check('exact 99 overlay order', [e['indices'] for e in saved['overlay']] == expected_scope)
        for entry in saved['overlay']:
            n, u = entry['indices']
            index = int(entry['case_pointer'].split('/')[-1])
            record = shard_cases[n][index]
            check(f'{n},{u} complete original record and single comparison',
                  record == entry['complete_original_record'] and record['fourth_index'] == u and
                  len([c for c in shard_cases[n] if c['fourth_index'] == u]) == 1 and
                  [c['source'] for c in entry['comparisons']] == ['L135'])
            prior_entry = next(e for e in previous['overlay'] if e['indices'] == [n, u])
            check(f'{n},{u} complete L134 mismatch provenance',
                  prior_entry['complete_original_record'] == record and
                  prior_entry['disposition'] == 'unmatched' and
                  prior_entry['shard'] == entry['shard'] and
                  prior_entry['case_pointer'] == entry['case_pointer'])
            for comparison in entry['comparisons']:
                lemma = comparison['source']
                check(f'{n},{u} {lemma} exact stated index set',
                      comparison['covered'] == comparison['literal_ordered_basis_equal'] ==
                      ([n, u] in expected_sets[lemma]))
            report['complete_occurrence_checks'].append(dict(indices=[n, u],
                shard=entry['shard'], case_pointer=entry['case_pointer'],
                record_sha256=sha256(json.dumps(record, sort_keys=True).encode()).hexdigest(),
                complete_comparisons=entry['comparisons']))
        check('full replay bounds and counts',
              replay['summary'] == saved['summary'] and
              replay['original_entries_rebuilt'] == 49896 and
              replay['null_residual_entries_replayed'] == 4560 and
              saved['summary']['actual_tested'] == saved['summary']['required_tested'] == 99 and
              saved['summary']['literal_basis_comparisons'] == 99 and
              saved['summary']['matched_point_row_bindings'] == 34)
        check('all original inputs and outputs unchanged', all(
            digest(name) == value for name, value in report['input_sha256'].items()))
        report['summary'] = saved['summary']
        report['original_artifacts_byte_unchanged'] = True
        report['qualification'] = ('Separate audit of restricted reproduced L136 input only; '
            'shared Python/residue arithmetic and inherited finite-certificate assumptions. '
            'No new locus, changed-row test, assembly, universal extraction or global bound.')
    except Exception as error:
        report['failures'].append(str(error))
    report['audit_code_sha256'] = sha256(Path(__file__).read_bytes()).hexdigest()
    out = HERE/'l136-critical-audit.json'
    out.write_text(json.dumps(report, indent=2)+'\n')
    print(f"Checks {sum(c['passes'] for c in report['checks'])}/{len(report['checks'])}; "
          f"occurrences {len(report['complete_occurrence_checks'])}/99; "
          f"failures {len(report['failures'])}; certificate: {out}")
    if report['failures']:
        print('Failures:', report['failures'])
        raise SystemExit(1)
    print('Complete fresh replay: 99/99 comparisons; 17 imports; '
          '34/34 point-row bindings; 82 mismatches preserved; original files unchanged.')


if __name__ == '__main__':
    run()
