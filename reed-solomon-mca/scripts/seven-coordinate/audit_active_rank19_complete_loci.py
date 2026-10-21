"""Separate bounded L120 audit. Preserve all historical and target evidence."""
from collections import Counter
from hashlib import sha256
from pathlib import Path
import json
import subprocess
import sys
import traceback

import zero_anchor_support_filter as direct
import verify_fixed_three_row_extensions as derivative
from verify_inactive_coordinate_screen import nullspace

HERE = Path(__file__).resolve().parent


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def run():
    previous = json.loads((HERE/'inactive-coordinate-partition-critical-audit.json').read_bytes())
    historical = previous['artifact_hashes_after']
    names = list(historical) + ['active-rank19-complete-loci.json',
                              'active-rank19-complete-loci-replay.json']
    names = list(dict.fromkeys(names))
    before = {name: digest(HERE/name) for name in names}
    code_names = ['active_rank19_complete_loci.py', 'verify_active_rank19_complete_loci.py',
                  'residual_kernel_gates.py', 'zero_anchor_support_filter.py',
                  'verify_fixed_three_row_extensions.py', 'verify_inactive_coordinate_screen.py',
                  Path(__file__).name]
    codes = {name: digest(HERE/name) for name in code_names}
    out = {'step_id': '2026-10-19-mca-337-active-rank19-critical-audit',
           'scope': 'L120 exact 223 occurrences only; no new support tests',
           'artifact_hashes_before': before, 'code_hashes': codes,
           'checks': [], 'records': [], 'failures': []}

    def check(name, condition):
        out['checks'].append({'name': name, 'passed': bool(condition)})
        assert condition, name

    try:
        check('audited historical artifacts unchanged',
              all(before[n] == h for n, h in historical.items()))
        check('prior audit and audited helpers', not previous['failures']
              and previous['replay_returncode'] == 0
              and all(c['passed'] for c in previous['checks'])
              and previous['artifact_hashes_before'] == historical
              and all(digest(HERE/n) == h for n, h in previous['code_hashes'].items()))
        cert = json.loads((HERE/'active-rank19-complete-loci.json').read_bytes())
        source = json.loads((HERE/'inactive-coordinate-screen.json').read_bytes())
        check('frozen source and current producer binding',
              cert['source_sha256'] == digest(HERE/'inactive-coordinate-screen.json')
              == '90b6f145c7993d33a834f3498fb3bee60f08ca328bd8e710af216a70df6172c1'
              and cert['code_sha256'] == codes['active_rank19_complete_loci.py'])
        expected = [(pos, r) for pos, r in enumerate(source['records'])
                    if r['status'] == 'screen_failure' and r['rank'] == 19
                    and 'L112_exchanged_rows' not in r['prior_exclusions']
                    and (r['third_index'], r['fourth_index']) != (0, 320)]
        check('exact domain and historical partitions', len(source['records']) == 599
              and sum(r['status'] == 'screen_failure' for r in source['records']) == 239
              and len(expected) == len(cert['records']) == 223)
        manifest = [[r['third_index'], r['fourth_index']] for pos, r in expected]
        check('complete ordered indexed manifest', cert['selected_manifest']
              == cert['processed_manifest'] == manifest and len(set(map(tuple, manifest))) == 223)
        survivors, points, rows = [], [], []
        for ri, ((position, old), rec) in enumerate(zip(expected, cert['records'])):
            assert rec['source_record_position'] == position
            assert rec['historical_index'] == manifest[ri]
            assert len(rec['rows']) == 4
            assert [[r['I'], r['K']] for r in rec['rows']] == old['four_rows']
            blocks = [direct.block(r['I'], r['K']) for r in rec['rows']]
            matrix = [row for block in blocks for row in block['matrix']]
            assert len(matrix) == 24 and all(len(row) == 21 for row in matrix)
            assert matrix == rec['original_matrix']
            assert matrix == [row for r in rec['rows'] for row in derivative.block(r['I'], r['K'])]
            pivots, basis = nullspace(matrix)
            assert len(pivots) == 19 and len(basis) == 2
            assert basis == rec['kernel_basis'] == old['kernel_basis']
            assert sorted(set(range(21))-set(pivots)) == rec['free_columns'] == old['free_columns']
            assert len(set(rec['rank_minor_rows'])) == len(set(rec['rank_minor_columns'])) == 19
            assert all(0 <= n < 24 for n in rec['rank_minor_rows'])
            assert all(0 <= n < 21 for n in rec['rank_minor_columns'])
            minor = [[matrix[r][c] for c in rec['rank_minor_columns']] for r in rec['rank_minor_rows']]
            assert direct.determinant(minor) == rec['rank_minor_residue'] != 0
            assert len(rec['homogeneous_coefficients_s2_st_t2']) == 35
            assert all(len(q) == 3 for q in rec['homogeneous_coefficients_s2_st_t2'])
            assert len(rec['points_and_all_row_gates']) == 2
            for pi, point in enumerate(rec['points_and_all_row_gates']):
                assert len(point['bivector']) == 21 and any(point['bivector'])
                assert len(point['u']) == len(point['v']) == 7
                assert len(point['row_gates']) == 4
                for g in point['row_gates']:
                    assert len(g['Q_u']) == len(g['Q_v']) == len(g['error_weights']) == 4
                    assert len(g['projection_minors']) == 6 and len(g['intersection_vector']) == 7
                    assert len(g['moment_residuals']) == 8
                    assert len(g['h_minus_error_minus_lambda_g_on_H']) == 16
                if point['passes_intrinsic_gates']:
                    survivors.append({'historical_index': rec['historical_index'],
                        'record_position': ri, 'point_position': pi, 'rows': rec['rows'],
                        'homogeneous_parameter': point['homogeneous_parameter'],
                        'u': point['u'], 'v': point['v'],
                        'row_gates': [{key: gate[key] for key in
                            ['direction_coefficients', 'lambda_value', 'error_weights', 'prescribed_finite_gate']}
                            for gate in point['row_gates']]})
                points.append(point)
                rows.extend(point['row_gates'])
            out['records'].append({'historical_index': rec['historical_index'],
                                   'original_rank': 19, 'nullity': 2,
                                   'minor_residue': rec['rank_minor_residue'],
                                   'all_array_lengths_checked': True})
        check('complete matrix/kernel reconstruction and untruncated gate arrays', len(out['records']) == 223)
        check('survivor details exactly match complete point evidence', survivors == cert['survivor_details'])
        by_index = {tuple(s['historical_index']): s for s in survivors}
        for a, b in [((38, 496), (191, 143)), ((51, 467), (178, 172))]:
            x, y = by_index[a], by_index[b]
            assert x['u'] == y['u'] and x['v'] == y['v']
            assert y['rows'] == [x['rows'][n] for n in [0, 1, 3, 2]]
            assert y['row_gates'] == [x['row_gates'][n] for n in [0, 1, 3, 2]]
        table = [
            ((38, 496), [1,0,30,88,43,87,31], [0,5,1,83,30,15,89],
             [([18,84],23,[53,25,91,62]), ([28,38],92,[75,93,67,59]),
              ([90,29],53,[26,23,26,61]), ([6,55],92,[89,91,67,36])]),
            ((51, 467), [1,0,4,20,23,33,82], [0,12,1,55,41,59,55],
             [([86,71],91,[60,23,10,26]), ([9,38],85,[48,68,25,64]),
              ([15,71],48,[92,77,94,23]), ([88,54],85,[85,68,60,96])])]
        for index, u, v, entries in table:
            s = by_index[index]
            assert s['u'] == u and s['v'] == v
            assert [(g['direction_coefficients'], g['lambda_value'], g['error_weights'])
                    for g in s['row_gates']] == entries
        check('all canonical survivor table entries and exchanged-row claims', True)
        check('all homogeneous types and failed/successful counts',
              Counter(str(r['affine_gcd']) for r in cert['records'])
              == Counter({'[0, 1]': 219, '[0, 94, 1]': 2, '[0, 16, 1]': 2})
              and len(points) == 446 and len(rows) == 1784
              and sum(p['passes_intrinsic_gates'] for p in points) == 4
              and sum(any(g['lambda_value'] == 0 for g in p['row_gates']) for p in points) == 442
              and sum(g['lambda_value'] == 0 for g in rows) == 1322
              and all(g['projection_rank'] == 1 for g in rows))
        log_path = HERE/'active-rank19-critical-audit.log'
        with log_path.open('w') as log:
            result = subprocess.run([sys.executable, str(HERE/'verify_active_rank19_complete_loci.py')],
                                    stdout=log, stderr=subprocess.STDOUT, check=False)
        out['replay_returncode'] = result.returncode
        out['replay_log'] = log_path.name
        check('complete independent homogeneous/factor/all-pivot/moment replay', result.returncode == 0)
        replay = json.loads((HERE/'active-rank19-complete-loci-replay.json').read_bytes())
        check('replayed artifact and code bindings', replay['source_sha256']
              == before['active-rank19-complete-loci.json']
              and replay['code_sha256'] == codes['verify_active_rank19_complete_loci.py']
              and not replay['failures'])
        out['complete_replay_summary'] = replay['summary']
        out['bounds'] = {'occurrences_actual': len(out['records']), 'occurrences_required': 223,
                         'excluded': 219, 'intrinsic_survivors': 4,
                         'global_interval_unchanged': '11/q–16/q'}
    except Exception:
        out['failures'].append(traceback.format_exc())
    out['artifact_hashes_after'] = {name: digest(HERE/name) for name in names}
    if out['artifact_hashes_after'] != before:
        out['failures'].append('Historical or target artifact changed during audit')
    if any(digest(HERE/n) != h for n, h in codes.items()):
        out['failures'].append('Audited code changed during audit')
    target = HERE/'active-rank19-critical-audit.json'
    target.write_text(json.dumps(out, indent=2)+'\n')
    print(f"Audited {len(out['records'])}/223 occurrences; failures {len(out['failures'])}; "
          f"unchanged artifacts {len(names)}; certificate {target}")
    if not out['failures']:
        print('219 exclusions; 4 intrinsic survivors; global interval unchanged at 11/q–16/q.')
    return bool(out['failures'])


if __name__ == '__main__':
    sys.exit(run())
