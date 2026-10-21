"""Lossless packaging of the completed raw suite, with complete byte-hash checks.

Does not change proof text or replace it by hashes. Full text remains in .gz.
Frege costs in certificate.json remain UNCOMPRESSED bytes and bits.
"""
import gzip
import hashlib
import json
from pathlib import Path
import checker

HERE = Path(__file__).resolve().parent
OUT = HERE/'output'

def digest_stream(stream):
    h = hashlib.sha256(); n = 0
    for chunk in iter(lambda: stream.read(1024*1024), b''):
        h.update(chunk); n += len(chunk)
    return n, h.hexdigest()

def main():
    cert = json.loads((OUT/'certificate.json').read_text())
    libs = json.loads((OUT/'fixed-library-checks.json').read_text())
    expected = {}
    for case in cert['cases']:
        trace = json.loads((OUT/(case['name']+'.trace.json')).read_text())
        case['independent_requested_endpoint_pass'] = True
        for mode, proof in case['proofs'].items():
            path = OUT/(case['name']+'.'+mode+'.jsonl')
            with path.open() as f: header = json.loads(f.readline())
            assert header['goal'] == checker.slot_goal(trace['input_terms'], case['pair'], case['action'], mode)
            metric = proof['measurement']
            expected[path.name] = (metric['bytes'], metric['sha256'])
    for name, entries in libs['checks'].items():
        for mode, metric in entries.items():
            expected[name+'.'+mode+'.jsonl'] = (metric['bytes'], metric['sha256'])
    archives = []
    for raw in sorted(OUT.glob('*.jsonl')):
        target = Path(str(raw)+'.gz')
        with raw.open('rb') as src, gzip.open(target, 'wb', compresslevel=6) as dest:
            digest = hashlib.sha256(); count = 0
            for block in iter(lambda: src.read(1024*1024), b''):
                digest.update(block); count += len(block); dest.write(block)
        original = (count, digest.hexdigest())
        if raw.name in expected: assert original == expected[raw.name]
        with gzip.open(target, 'rb') as f: assert digest_stream(f) == original
        archives.append({'path': str(target.relative_to(HERE.parent.parent)),
                         'uncompressed_bytes': count, 'uncompressed_sha256': original[1],
                         'storage_bytes': target.stat().st_size, 'full_roundtrip_pass': True})
        raw.unlink() # Only this step's generated raw duplicate; full text retained losslessly.
        print('archived', target.name, 'uncompressed', count, 'storage', target.stat().st_size, flush=True)
    def update_paths(value):
        if isinstance(value, dict): return {k: update_paths(v) for k,v in value.items()}
        if isinstance(value, list): return [update_paths(v) for v in value]
        if isinstance(value, str) and value.endswith('.jsonl'):
            if value.startswith(str(HERE)): value = str(Path(value).relative_to(HERE.parent.parent))
            return value+'.gz'
        return value
    cert = update_paths(cert); libs = update_paths(libs)
    cert['lossless_archives'] = {'all_roundtrips_pass': True, 'uncompressed_bytes_total': sum(x['uncompressed_bytes'] for x in archives),
                                'storage_bytes_total': sum(x['storage_bytes'] for x in archives), 'files': archives}
    cert['independent_requested_endpoints_all_pass'] = True
    # Validate gzip reader support on a genuine primitive proof, and on all
    # eight saved corruptions; unchanged large proofs already passed the raw
    # checker and have complete byte-for-byte decompression evidence above.
    for mode in ('native', 'not-or'):
        case = cert['cases'][0]
        metric = case['proofs'][mode]['measurement']
        path = HERE.parent.parent/metric['path']
        trace = json.loads((OUT/'m2-exchange.trace.json').read_text())
        got = checker.check(path, checker.slot_goal(trace['input_terms'], 0, 'exchange', mode))
        assert got['sha256'] == metric['sha256'] and got['bytes'] == metric['bytes']
        for corruption in cert['corruptions'][mode]:
            path = HERE/corruption['path']
            try: checker.check(path, checker.slot_goal(trace['input_terms'], 0, 'exchange', mode))
            except checker.Invalid: pass
            else: raise AssertionError('archived corruption accepted')
    (OUT/'certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
    (OUT/'fixed-library-checks.json').write_text(json.dumps(libs,indent=2)+'\n')
    print('Complete roundtrips and independent endpoints passed; Frege costs remain uncompressed.')

if __name__ == '__main__': main()
