"""Isolated full replay for the separately reviewed L135 proof/program audit.

No support search: execute the inspected single-occurrence programs only.
All originals remain untouched; complete mathematical evidence is bound by
hash, regenerated in isolation, and compared byte for byte.
"""
from hashlib import sha256
from pathlib import Path
from tempfile import TemporaryDirectory
import json
import subprocess
import sys

HERE = Path(__file__).resolve().parent
FILES = [
    'second_unmatched_locus_gates.py',
    'verify_second_unmatched_locus_gates.py',
    'zero_anchor_support_filter.py',
    'residual_kernel_gates.py',
    'new-pair-filter/third-094.json',
    'second-unmatched-locus-gates.json',
    'second-unmatched-locus-gates-replay.json',
]


def run():
    if not __debug__:
        raise RuntimeError('Run audit with assertions enabled')
    before = {name: (HERE/name).read_bytes() for name in FILES}
    manifest = {name: {'sha256': sha256(raw).hexdigest(), 'bytes': len(raw)}
                for name, raw in before.items()}
    checks, failures, execution = [], [], []

    def check(name, condition):
        checks.append({'check': name, 'passed': bool(condition)})
        if not condition:
            failures.append(name)

    cert = json.loads(before['second-unmatched-locus-gates.json'])
    replay = json.loads(before['second-unmatched-locus-gates-replay.json'])
    shard = json.loads(before['new-pair-filter/third-094.json'])
    record = shard['cases'][155]
    try:
        with TemporaryDirectory(prefix='l135-audit-', dir=HERE) as tmp:
            isolated = Path(tmp)
            for name, raw in before.items():
                path = isolated/name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(raw)
            for program in FILES[:2]:
                result = subprocess.run([sys.executable, '-E', '-B', program],
                                        cwd=isolated, text=True, capture_output=True)
                execution.append({'program': program, 'returncode': result.returncode,
                                  'stdout': result.stdout, 'stderr': result.stderr})
                check(program+' completed', result.returncode == 0)
                if result.returncode:
                    raise RuntimeError(program+' failed; see complete execution record')
            for name, raw in before.items():
                check('isolated byte equality: '+name, (isolated/name).read_bytes() == raw)
        check('source SHA256', cert['source']['sha256'] ==
              manifest['new-pair-filter/third-094.json']['sha256'])
        check('complete source record binding', record['fourth_index'] == 539 and
              record['status'] == 'residual' and
              cert['kernel_basis'] == record['kernel_basis'] and
              cert['kernel_residuals'] == record['kernel_residuals'])
        check('replay certificate SHA256', replay['certificate_sha256'] ==
              manifest['second-unmatched-locus-gates.json']['sha256'])
        check('complete original matrix shape', len(cert['original_matrix']) == 24 and
              all(len(row) == 21 for row in cert['original_matrix']))
        check('complete matrix replay', cert['original_matrix'] == replay['rebuilt_original_matrix'])
        check('minor exact integer and nonzero residue',
              cert['rank_minor_integer_determinant'] ==
              replay['rank_minor_integer_determinant'] ==
              -945819218664996129435665357596016640 and
              cert['rank_minor_integer_determinant'] % 97 == cert['rank_minor_residue'] == 23)
        check('all homogeneous coefficients replayed',
              len(cert['plucker_coefficients_s2_st_t2']) == 35 and
              cert['plucker_coefficients_s2_st_t2'] == replay['plucker_coefficients_s2_st_t2'])
        gates = [g for point in cert['points_and_all_row_gates'] for g in point['row_gates']]
        check('eight necessary row gates', len(gates) == 8 and
              all(g['projection_rank'] == 1 for g in gates))
        check('six lambda-zero and two full rows',
              sum(g['lambda_value'] == 0 for g in gates) == 6 and
              sum(all(g['error_weights']) for g in gates) == 2)
        check('both second-row failures', all(
              p['row_gates'][1]['lambda_value'] == 0 and
              p['row_gates'][1]['error_weights'].count(0) == 3
              for p in cert['points_and_all_row_gates']))
        check('all 128 pointwise identities',
              sum(len(g['h_minus_error_minus_lambda_g_on_H']) for g in gates) == 128 and
              all(not any(g['h_minus_error_minus_lambda_g_on_H']) for g in gates))
        check('all 64 original moments', sum(len(g['moment_residuals']) for g in gates) == 64 and
              all(not any(g['moment_residuals']) for g in gates))
        check('complete seven exterior and 73 projection pivot replay',
              len(replay['all_pivot_replay']) == 73 and
              len({(r['point'], tuple(r['exterior_pivot'])) for r in replay['all_pivot_replay']}) == 7)
        check('original certificates have no failures', cert['failures'] == replay['failures'] == [])
    except Exception as error:
        failures.append(type(error).__name__+': '+str(error))
    for name, raw in before.items():
        check('original bytes preserved: '+name, (HERE/name).read_bytes() == raw)
    log = HERE/'l135-critical-audit-replay.log'
    log.write_text(''.join(
        item['program']+' (exit '+str(item['returncode'])+')\n'+item['stdout']+item['stderr']
        for item in execution))
    result = {
        'step_id': '2026-10-21-mca-398-second-unmatched-critical-audit',
        'scope': 'Only L135 original occurrence (94,539); proof audit is in the canonical lemma.',
        'inputs': manifest, 'source_record': record, 'execution': execution, 'checks': checks,
        'summary': {'actual_loci': 1, 'required_loci': 1, 'rank': 19,
                    'rank_minor_residue': 23, 'required_nonzero_minor': True,
                    'complete_points': 2, 'passing_planes': 0,
                    'checks_passed': sum(c['passed'] for c in checks), 'checks_required': len(checks),
                    'full_replay_counts': replay['summary']},
        'failures': failures,
        'limitations': 'Shared Python/residue arithmetic; no new exclusion, global bound or proof-assistant check.'}
    target = HERE/'l135-critical-audit.json'
    target.write_text(json.dumps(result, indent=2)+'\n')
    print('L135 loci 1/1; rank 19, nonzero minor 23; passing planes 0/2.')
    print(f"Checks {result['summary']['checks_passed']}/{len(checks)}; failures {len(failures)}.")
    print('Certificate:', target)
    print('Complete log:', log)
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    run()
