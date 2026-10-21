"""Step 210: compose existing complete replay evidence; never emit/replay streams."""
import copy
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import replay_star as r

h, ROOT, OUT = r.h, r.ROOT, r.OUT
DEST = OUT / 'aggregate-210-star.json'
MANIFEST = OUT / 'interface-210-star.json'
REPLAYS = [OUT / 'replay-207-strict-star-coordinate-0.json',
           OUT / 'replay-208-star-coordinate-1.json',
           OUT / 'replay-209-star-coordinate-2.json']


def read(path):
    return r.strict_read(path.read_bytes())


def validate(entries, expected):
    assert len(entries) == len(expected), 'all coordinate occurrences required'
    for v, (entry, goal) in enumerate(zip(entries, expected)):
        assert type(entry['coordinate']) is int and entry['coordinate'] == v, 'coordinate order'
        assert entry['endpoint'] == goal, 'exact receiving endpoint'
        assert entry['root'] == entry['lines'] - 1, 'last-record root'
        assert set(entry['proofs']) == {'native', 'not-or'}, 'both literal formats'


def main():
    assert not DEST.exists() and not MANIFEST.exists(), 'preserve evidence'
    cert = dict(step=210, complete=False, failures=[], phase='reception',
                scope='Certificate composition and exact receiving interface; no new primitive replay or chain import',
                limitations=['coordinate-0 historical cache-hit/call traces unavailable',
                             'whole L064 receiver import and row-chain invocation not performed'])
    r.save(DEST, cert)
    try:
        d = read(OUT / 'star-205.request.json'); tables = h.ep.request(d)
        source = read(OUT / 'certificate-205-star.json')['cases'][0]
        replays = [read(path) for path in REPLAYS]
        assert all(c['complete'] is True and c['failures'] == [] for c in replays)
        bound = replays[0]['uniform_ledger']
        assert bound == source['uniform_ledger']
        assert all(c['uniform_ledger'] == bound for c in replays)
        assert all(c['local_inputs'] == replays[0]['local_inputs'] for c in replays)
        assert all(c['finite_tables'] == {k: tables[k] for k in ('K', 'beta', 'G')} for c in replays)
        locals_ = replays[0]['local_inputs']
        assert [a['native']['path'] for a in locals_] == source['inputs']
        assert sum(a['native']['lines'] for a in locals_) == bound['imported_records']
        assert all(a['native']['accepted'] is True for a in locals_)
        # Directly exercise L064's receiving syntax, without invoking its compiler.
        spec = importlib.util.spec_from_file_location('aggregate_chain', ROOT / 'scripts/backward-zero/chain.py')
        chain = importlib.util.module_from_spec(spec); spec.loader.exec_module(chain)
        receiving = {k: d[k] for k in ('N', 'n', 'q', 'suffixes', 'letters')}
        receiving.update(beta=tables['beta'], G=tables['G'], levels=[dict(k=0, R=[], T=[])])
        expected = chain.validate(receiving)
        assert expected == [h.ep.e.c.serialize(g) for g in tables['closed']]
        entries = []
        for v, (path, replay) in enumerate(zip(REPLAYS, replays)):
            assert len(replay['verified_exports']) == 1
            export = replay['verified_exports'][0]
            assert export['coordinate'] == v
            assert all(export[k] is True for k in ('complete_input_retention', 'exact_endpoint', 'literal_image'))
            entry = dict(coordinate=v, endpoint=expected[v], root=export['root'],
                         lines=export['proofs']['native']['measurement']['lines'], proofs={},
                         replay=str(path.relative_to(ROOT)), replay_sha256=hashlib.sha256(path.read_bytes()).hexdigest())
            for mode in ('native', 'not-or'):
                proof = export['proofs'][mode]; m = proof['measurement']; req = bound['formats'][mode]
                assert export['root'] == m['lines'] - 1
                assert m['accepted'] is True and proof['writer_matches'] is True
                assert all(proof['uniform_checks'].values())
                assert all(h.ledger.check(m, req).values())
                assert proof['full_field_depth'] <= req['depth']
                # Each serialized substitution is a subfield of this full record.
                assert m['max_record_nodes'] <= req['argument_nodes']
                assert proof['full_field_depth'] <= req['argument_depth']
                archive = ROOT / m['path']; writer = read(archive.with_name(archive.name + '.writer.json'))
                assert all(writer[k] == m[k] for k in ('lines', 'bytes', 'sha256'))
                with gzip.open(archive, 'rb') as stream:
                    header = r.strict_read(stream.readline())
                goal = h.ep.e.c.serialize(h.ep.e.image(tables['closed'][v]) if mode == 'not-or' else tables['closed'][v])
                assert header['goal'] == goal
                entry['proofs'][mode] = m
            entries.append(entry)
        validate(entries, expected)
        rejected = []
        for name in ('missing', 'swapped', 'endpoint', 'root', 'image'):
            bad = copy.deepcopy(entries)
            if name == 'missing': bad.pop()
            elif name == 'swapped': bad[0], bad[1] = bad[1], bad[0]
            elif name == 'endpoint': bad[0]['endpoint'] = '(A>A)'
            elif name == 'root': bad[0]['root'] -= 1
            else: del bad[0]['proofs']['not-or']
            try: validate(bad, expected)
            except AssertionError: rejected.append(name)
            else: raise AssertionError('malformed manifest accepted: ' + name)
        totals = {}
        for mode in ('native', 'not-or'):
            measurements = [e['proofs'][mode] for e in entries]
            lines = sum(m['lines'] for m in measurements)
            size = sum(m['bytes'] for m in measurements)
            req = bound['formats'][mode]
            assert lines <= bound['aggregate_lines'] and size <= req['aggregate_bytes']
            assert 8*size <= req['aggregate_bits']
            totals[mode] = dict(lines=lines, required_lines=bound['aggregate_lines'], bytes=size,
                                required_bytes=req['aggregate_bytes'], bits=8*size, required_bits=req['aggregate_bits'])
            print(mode, 'aggregate lines', lines, '/', bound['aggregate_lines'],
                  'bytes', size, '/', req['aggregate_bytes'], 'bits', 8*size, '/', req['aggregate_bits'], flush=True)
        offset = 0; imports = []
        for entry in entries:
            imports.append(dict(coordinate=entry['coordinate'], start=offset, lines=entry['lines'],
                                root=offset+entry['root']))
            offset += entry['lines']
        manifest = dict(original_request=source['request'], receiving=receiving, coordinates=entries,
                        planned_receiver_imports=imports,
                        qualification='Offsets describe L064 relocation, not an executed import. Replay hashes bind prior certificates; archives were not rehashed or replayed this turn.')
        r.save(MANIFEST, manifest)
        cert.update(phase='complete', complete=True, uniform_ledger=bound, totals=totals,
                    manifest=str(MANIFEST.relative_to(ROOT)), manifest_bytes=MANIFEST.stat().st_size,
                    local_inputs=locals_, retained_local_records_per_coordinate=bound['imported_records'],
                    retained_local_records_aggregate=d['N']*bound['imported_records'],
                    planned_receiver_imports=imports, rejections=rejected, exact_receiving_endpoints=expected,
                    serialized_substitution_argument_checks=True,
                    evidence_basis='Complete 207-strict/208/209 primitive replay reused unchanged; all certificate fields consumed in full.')
        r.save(DEST, cert)
        print('PASS three certified pairs / five malformed manifests; manifest bytes', cert['manifest_bytes'],
              '; failures=[];', DEST.relative_to(ROOT), flush=True)
    except BaseException as exc:
        cert['failures'].append(type(exc).__name__ + ': ' + str(exc)); r.save(DEST, cert); raise


if __name__ == '__main__':
    main()
