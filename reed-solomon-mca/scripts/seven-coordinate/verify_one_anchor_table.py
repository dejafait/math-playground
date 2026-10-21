"""Compile/run independent full certificate replay; compare and hash artifacts.

Run from the active notebook. Uses no producer code and never reruns it.
"""
from pathlib import Path
import hashlib
import json
import subprocess
import tempfile


def run():
    base = Path('scripts/seven-coordinate')
    with tempfile.TemporaryDirectory(prefix='mca-one-anchor-verify-') as tmp:
        exe = str(Path(tmp) / 'verify')
        subprocess.run(['c++', '-O3', '-std=c++17',
                        str(base / 'verify_one_anchor_table.cpp'), '-o', exe], check=True)
        subprocess.run([exe], check=True)
    producer = json.loads((base / 'one-anchor-table.json').read_text())
    replay = json.loads((base / 'one-anchor-table-verification-raw.json').read_text())
    fields = ('complete', 'seed_count', 'required_seed_count', 'candidate_count',
              'row_count', 'required_rows_per_candidate', 'full_successes',
              'maximum_distinct_scalars', 'required_threshold', 'seed_gate_counts',
              'row_gate_counts', 'histogram', 'maximizer_ids', 'failures')
    for field in fields:
        assert producer[field] == replay[field], field
    assert replay['complete'] and replay['failures'] == 0
    assert replay['seed_count'] == replay['required_seed_count'] == 14696640
    assert replay['row_count'] == replay['candidate_count'] * 540
    assert sum(replay['seed_gate_counts']) == replay['seed_count']
    assert sum(replay['row_gate_counts'].values()) == replay['row_count']
    assert sum(replay['histogram'].values()) == replay['candidate_count']
    assert (base / 'one-anchor-seeds.bin').stat().st_size == 4 * replay['seed_count']
    hashes = {}
    for name in ('one_anchor_table.cpp', 'verify_one_anchor_table.cpp',
                 'verify_one_anchor_table.py', 'one-anchor-table.json',
                 'one-anchor-table-verification-raw.json',
                 'one-anchor-seeds.bin', 'one-anchor-candidates.tsv'):
        digest = hashlib.sha256()
        with (base / name).open('rb') as stream:
            for chunk in iter(lambda: stream.read(1024 * 1024), b''):
                digest.update(chunk)
        hashes[name] = digest.hexdigest()
    replay['sha256'] = hashes
    replay['scope'] = dict(field='F_(97^20)', prime=97,
                           S=[1, 8, 12, 18, 22, 27, 33], P=[1, 8, 12],
                           profile='t=1; equality necessary filter; before original-point deletion')
    replay['producer_fields_compared'] = list(fields)
    replay['qualifications'] = ['Both programs use C++ and residue arithmetic.',
                                'No separate critical audit has yet been completed.',
                                'Audited L107 reduction and its finite inputs remain essential.']
    destination = base / 'one-anchor-table-verification.json'
    destination.write_text(json.dumps(replay, indent=2) + '\n')
    print(f"Certificate comparison and hashes passed; maximum "
          f"{replay['maximum_distinct_scalars']}/{replay['required_threshold']}; "
          f"failures 0; {destination}")


if __name__ == '__main__':
    run()
