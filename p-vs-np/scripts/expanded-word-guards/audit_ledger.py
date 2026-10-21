"""Reproduce step 190's fixed-name, metadata and whole-list majorant checks."""
import gzip
import json
import re
from pathlib import Path

OUT = Path(__file__).resolve().parent / 'output'
ROOT = OUT.parents[2]

def main():
    old = json.loads((OUT / 'certificate-188.json').read_text())
    cert = {'complete': False, 'failures': [], 'fixed_names': {}, 'cases': []}
    dest = OUT / 'ledger-audit-190.json'
    def save(): dest.write_text(json.dumps(cert, indent=2) + '\n')
    save()
    try:
        for key in old['library']:
            names = set()
            with gzip.open(OUT / ('fixed-' + key + '.native.jsonl.gz'), 'rt') as stream:
                next(stream)
                for line in stream:
                    row = json.loads(line)
                    for field in [row['f']] + list(row.get('subs', {}).values()):
                        names.update(re.findall('[^()>~]+', field))
            assert all(len(s) == 1 and re.fullmatch('[A-Za-z0-9_]', s) for s in names)
            cert['fixed_names'][key] = sorted(names)
        L = 8179; S = 25956; C = 2 * L + 5
        K = C * (1500 * S + 128 + 64 * C)
        assert K == 654214993680
        cert['K_stream'] = K
        for case in old['cases']:
            input_bytes = (ROOT / case['request']).stat().st_size
            for item in case['proofs']:
                with gzip.open(ROOT / item['import'], 'rb') as stream:
                    while chunk := stream.read(1024 * 1024): input_bytes += len(chunk)
            Q = 2 + input_bytes
            result = {'case': case['name'], 'Q_lower_bound': Q, 'formats': {}}
            for mode in ['native', 'not-or']:
                required = case['whole_list'][mode]['required_bytes']
                actual = case['whole_list'][mode]['actual_bytes']
                assert actual <= required <= K * Q**4
                result['formats'][mode] = {'actual': actual, 'per_position_required_sum': required,
                                           'Q4_majorant': K * Q**4}
            cert['cases'].append(result)
        cert['metadata_bytes'] = (OUT / 'certificate-188.json').stat().st_size + sum(
            (ROOT / c['request']).stat().st_size for c in old['cases'])
        assert cert['metadata_bytes'] == 132161
        cert['complete'] = True; save()
        print('PASS 24 one-byte fixed-name sets; four whole-list Q^4 bounds; metadata bytes',
              cert['metadata_bytes'], 'K_stream', K, 'failures', cert['failures'], 'certificate', dest)
    except Exception as err:
        cert['failures'].append(repr(err)); save(); raise

if __name__ == '__main__': main()
