"""Step 209: one fresh coordinate, original inputs, strict complete replay."""
import json
import finish_exports as f
import replay_star as r

h, OUT, ROOT = f.h, f.OUT, f.ROOT
DEST = OUT / 'construction-209-star-coordinate-2.json'
REPLAY = OUT / 'replay-209-star-coordinate-2.json'
PATHS = [OUT / ('star-209-coordinate-2.' + mode + '.jsonl.gz')
         for mode in ('native', 'not-or')]


def main():
    assert not any(path.exists() for path in [DEST, REPLAY] + PATHS), 'preserve earlier artifacts'
    cert = dict(step=209, complete=False, failures=[], phase='reception',
                coordinate=2, original_request='scripts/left-closure/output/star-205.request.json',
                replay=str(REPLAY.relative_to(ROOT)), aggregate_verified=False)
    r.save(DEST, cert)
    try:
        initial = json.loads((OUT / 'certificate-202.json').read_text())
        d = json.loads((OUT / 'star-205.request.json').read_text())
        paths = [OUT / ('star-205-local-' + str(v) + '.native.jsonl.gz') for v in range(d['N'])]
        lib = f.library(initial)
        obj = h.lc.Closure(d, paths, lib)
        terms = {mode: h.suite.measured_terms(d, mode) for mode in ('native', 'not-or')}
        bound = h.lc.thresholds(d, obj.packages, initial['constants'], terms,
                                max(a['name_bytes'] for a in lib.values()))
        cert.update(phase='compile', original_inputs=[str(path.relative_to(ROOT)) for path in paths],
                    uniform_ledger=bound, imported_records=obj.imported_end)
        r.save(DEST, cert)
        obj.row(2)
        cert.update(phase='arguments', root=obj.root, records=len(obj.p.rows),
                    exact_endpoint=h.ep.e.c.serialize(obj.tables['closed'][2]),
                    max_argument_height=obj.max_argument_height, imports=obj.imports,
                    traces=obj.traces, argument_checks={})
        assert obj.max_argument_height <= bound['H']
        assert all(t['max_height'] <= bound['H'] for t in obj.traces)
        syntax = r.f.FastSyntax()
        try:
            for mode, offset in [('native', 0), ('not-or', 2)]:
                stats = [syntax.stats[syntax.parse(s)] for call in obj.calls
                         for s in call['arguments'].values()]
                nodes = max([s[offset] for s in stats] + [0])
                depth = max([s[offset+1] for s in stats] + [0])
                required = bound['formats'][mode]
                assert nodes <= required['argument_nodes'] and depth <= required['argument_depth']
                cert['argument_checks'][mode] = dict(nodes=nodes, depth=depth,
                    required_nodes=required['argument_nodes'], required_depth=required['argument_depth'])
                print(mode, 'argument nodes actual/required', nodes, '/', required['argument_nodes'],
                      'depth actual/required', depth, '/', required['argument_depth'], flush=True)
        finally:
            syntax.close()
        cert['phase'] = 'write'; cert['writers'] = {}
        r.save(DEST, cert)
        for mode, image, path in zip(('native', 'not-or'), (False, True), PATHS):
            cert['writers'][mode] = f.write(obj, path, image)
            r.save(DEST, cert)
        # Free the construction store; replay reconstructs all records independently.
        del obj
        cert['phase'] = 'replay'; r.save(DEST, cert)
        r.replay(coordinate=2, dest=REPLAY, paths=PATHS, step=209)
        checked = json.loads(REPLAY.read_text())
        assert checked['complete'] and not checked['failures']
        assert checked['uniform_ledger'] == bound
        assert checked['verified_exports'][0]['root'] == cert['root']
        cert.update(phase='complete', complete=True, verified_pairs=1)
        r.save(DEST, cert)
        print('PASS one fresh star coordinate-2 pair;', DEST.relative_to(ROOT), flush=True)
    except BaseException as exc:
        cert['failures'].append(type(exc).__name__ + ': ' + str(exc))
        r.save(DEST, cert)
        raise


if __name__ == '__main__':
    main()
