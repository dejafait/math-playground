"""Separate bounded L132 audit; no new locus, row mechanism or filter.

Run from the notebook: python3 -B scripts/seven-coordinate/audit_l132.py
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
    report = dict(step_id='2026-10-20-mca-386-residual-literal-import-critical-audit',
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
        saved = read('residual-locus-reuse.json')
        replay = read('residual-locus-reuse-replay.json')
        names = sorted(set(saved['input_sha256']) | {
            'residual_locus_reuse.py', 'verify_residual_locus_reuse.py',
            'residual-locus-reuse.json', 'residual-locus-reuse-replay.json'})
        check('closed inventory has 79 inputs', len(names) == 79)
        for name in names:
            check('notebook-local input ' + name,
                  (HERE/name).resolve().is_relative_to(ROOT))
            report['input_sha256'][name] = digest(name)
        check('all original recorded input hashes', all(
            digest(name) == value for name, value in saved['input_sha256'].items()))
        check('original output/code provenance',
              saved['code_sha256'] == digest('residual_locus_reuse.py') and
              replay['certificate_sha256'] == digest('residual-locus-reuse.json') and
              replay['verifier_sha256'] == digest('verify_residual_locus_reuse.py'))
        check('no saved failures', saved['failures'] == replay['failures'] == [])
        # Recreate the relative ../../lemmas layout. Only reviewed run() bodies
        # execute; imported derivative helper has no execution on import.
        with TemporaryDirectory(prefix='l132-audit-', dir=HERE) as temp:
            isolated = Path(temp)/'scripts'/'seven-coordinate'
            isolated.mkdir(parents=True)
            for name in names:
                destination = isolated/name
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(HERE/name, destination)
            environment = dict(os.environ)
            environment.pop('PYTHONOPTIMIZE', None)
            for program in ('residual_locus_reuse.py', 'verify_residual_locus_reuse.py'):
                completed = subprocess.run(
                    [sys.executable, '-B', str(isolated/program)],
                    env=environment, capture_output=True, text=True, check=False)
                report['runs'].append(dict(program=program, returncode=completed.returncode,
                    stdout=completed.stdout.replace(temp, '<isolated-copy>'),
                    stderr=completed.stderr.replace(temp, '<isolated-copy>')))
                check(program + ' assertions-enabled isolated run', completed.returncode == 0)
            for name in ('residual-locus-reuse.json', 'residual-locus-reuse-replay.json'):
                check(name + ' full byte reproduction',
                      (isolated/name).read_bytes() == (HERE/name).read_bytes())

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
        check('exact scope deletion of four records',
              [x for x in historical if x[0] in (58, 59)] ==
              [[58, 355], [58, 647], [59, 355], [59, 647]])
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

        a = [60, 61, 66, 68, 69, 70, 71]
        b = [60, 61, 66, 67, 68, 69, 70]
        expected_sets = {
            'L126': sorted([[x, 355] for x in a] + [[355, x] for x in [58, 59]+a]),
            'L127': sorted([[x, 647] for x in b] + [[647, x] for x in [58, 59]+b])}
        expected_matched = sorted(expected_sets['L126'] + expected_sets['L127'])
        check('all 32 displayed indices and 118 complementary mismatches',
              saved['covered_indices'] == expected_matched and
              saved['unmatched_indices'] == [x for x in historical
                  if x[0] not in (58, 59) and x not in expected_matched] and
              len(saved['unmatched_indices']) == 118)
        check('all four historical exchanges retained',
              all(x in expected_matched for x in [[355, 58], [355, 59], [647, 58], [647, 59]]))

        imports = {x['lemma']: x for x in saved['source_imports']}
        check('exact two imported sources', set(imports) == {'L126', 'L127'})
        expected_mixed = {'L126': {0: 2, 1: 44, 2: 54, 3: 1},
                          'L127': {0: 84, 10: 34, 11: 35, 12: 96}}
        tables = {'L126': [(0, 12, 85, 0, [85, 0, 0, 0]),
                          (0, 16, 81, 0, [0, 81, 0, 0])],
                  'L127': [(0, 44, 53, 0, [53, 0, 0, 0]),
                          (44, 0, 0, 44, [78, 0, 0, 0])]}
        for lemma, imported in imports.items():
            source = read(imported['certificate'])
            source_replay = read(imported['replay'])
            audit = read(imported['audit'])
            checks = audit['checks']
            check(lemma + ' full separate audit and all bound inputs',
                  audit['failures'] == [] and
                  (all(v is True for v in checks.values()) if isinstance(checks, dict)
                   else all(c['passes'] is True for c in checks)) and
                  all(digest(name) == value for name, value in audit['input_sha256'].items()))
            locus = imported['imported_locus']
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
                  ([1, 1] if lemma == 'L126' else [1, 2]))
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
            report['source_checks'].append(dict(lemma=lemma, complete_import=imported,
                complete_audit_checks=checks, replay_sha256=digest(imported['replay'])))

        check('exact 150 overlay order', [e['indices'] for e in saved['overlay']] ==
              [x for x in historical if x[0] not in (58, 59)])
        for entry in saved['overlay']:
            n, u = entry['indices']
            index = int(entry['case_pointer'].split('/')[-1])
            record = shard_cases[n][index]
            check(f'{n},{u} complete original record and both comparisons',
                  record == entry['complete_original_record'] and record['fourth_index'] == u and
                  len([c for c in shard_cases[n] if c['fourth_index'] == u]) == 1 and
                  [c['source'] for c in entry['comparisons']] == ['L126', 'L127'])
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
              replay['original_entries_rebuilt'] == 75600 and
              replay['null_residual_entries_replayed'] == 7008 and
              saved['summary']['actual_tested'] == saved['summary']['required_tested'] == 150 and
              saved['summary']['literal_basis_comparisons'] == 300 and
              saved['summary']['matched_point_row_bindings'] == 64)
        check('all original inputs and outputs unchanged', all(
            digest(name) == value for name, value in report['input_sha256'].items()))
        report['summary'] = saved['summary']
        report['original_artifacts_byte_unchanged'] = True
        report['qualification'] = ('Separate audit of restricted reproduced L132 input only; '
            'shared Python/residue arithmetic and inherited finite-certificate assumptions. '
            'No new locus, changed-row test, assembly, universal extraction or global bound.')
    except Exception as error:
        report['failures'].append(str(error))
    report['audit_code_sha256'] = sha256(Path(__file__).read_bytes()).hexdigest()
    out = HERE/'l132-critical-audit.json'
    out.write_text(json.dumps(report, indent=2)+'\n')
    print(f"Checks {sum(c['passes'] for c in report['checks'])}/{len(report['checks'])}; "
          f"occurrences {len(report['complete_occurrence_checks'])}/150; "
          f"failures {len(report['failures'])}; certificate: {out}")
    if report['failures']:
        print('Failures:', report['failures'])
        raise SystemExit(1)
    print('Complete fresh replay: 300/300 comparisons; 32 imports; '
          '64/64 point-row bindings; 118 mismatches preserved; original files unchanged.')


if __name__ == '__main__':
    run()
