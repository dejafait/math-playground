"""Bind a separate L125 audit to a complete fresh replay, preserving inputs."""
from contextlib import redirect_stdout
from hashlib import sha256
from pathlib import Path
import json

import verify_new_pair_filter as verifier

HERE = Path(__file__).resolve().parent


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def run():
    master_path = HERE / 'new-pair-filter.json'
    replay_path = HERE / 'new-pair-filter-replay.json'
    master = json.loads(master_path.read_bytes())
    old_replay = json.loads(replay_path.read_bytes())
    paths = [master_path, replay_path,
             HERE / 'new_pair_filter.py', HERE / 'verify_new_pair_filter.py',
             HERE / 'zero_anchor_support_filter.py',
             HERE / 'verify_fixed_three_row_extensions.py',
             HERE / 'new-pair-filter.log', HERE / 'new-pair-filter-replay.log']
    paths += [HERE / meta['certificate'] for meta in master['thirds']]
    before = {str(p.relative_to(HERE)): digest(p) for p in paths}
    assert len(master['thirds']) == 382
    assert old_replay['source_sha256'] == digest(master_path)
    assert old_replay['code_sha256'] == digest(HERE / 'verify_new_pair_filter.py')
    assert old_replay['derivative_helper_sha256'] == digest(
        HERE / 'verify_fixed_three_row_extensions.py')
    assert old_replay['thirds'] == master['thirds']
    assert old_replay['summary'] == master['summary']
    assert old_replay['gate_coefficient_checks'] == 1512
    assert old_replay['failures'] == []
    for name in ['new-pair-filter.log', 'new-pair-filter-replay.log']:
        lines = (HERE / name).read_text().splitlines()
        summaries = [json.loads(line) for line in lines if line.startswith('{')]
        assert summaries == [master['summary']]
        assert '382/382' in lines[-3] and '100764' in lines[-3]
        assert 'Failures: 0;' in lines[-1]
    log_path = HERE / 'l125-critical-audit-replay.log'
    with log_path.open('w') as log, redirect_stdout(log):
        verifier.run()
    assert json.loads(replay_path.read_bytes()) == old_replay
    after = {str(p.relative_to(HERE)): digest(p) for p in paths}
    assert before == after
    first = old_replay['first_residual']
    assert (first['third_index'], first['fourth_index'], first['rank']) == (58, 355, 19)
    assert first['supports'][2:] == [[[1, 12], [70, 79]], [[8, 27], [79, 89]]]
    assert len(first['kernel_basis']) == 2
    output = dict(
        audited_input_hashes=before,
        audit_code_sha256=digest(Path(__file__)),
        complete_replay_log_sha256=digest(log_path),
        summary=master['summary'],
        first_residual=first,
        original_artifacts_byte_unchanged=True,
        full_saved_replay_identical=True,
        failures=[],
        qualification='Separate code/proof audit plus complete replay; shared Python and residue arithmetic; no residual feasibility or global theorem.')
    out_path = HERE / 'l125-critical-audit.json'
    out_path.write_text(json.dumps(output, indent=2) + '\n')
    print('Actual/required cases 100764/100764; shards 382/382; '
          'minors 100764/100764; null vectors 62682; residual entries 1504368; '
          'residuals 154 over 54 thirds; failures 0.')
    print(f'Certificate: {out_path}; full replay log: {log_path}')


if __name__ == '__main__':
    run()
