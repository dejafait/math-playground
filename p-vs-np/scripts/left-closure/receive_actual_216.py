"""One preserved actual-tree reception; complete exports and source-only ledgers."""
import hashlib
import json
import sys
import finish_exports as f
import replay_star as r

h, ROOT, OUT = f.h, f.ROOT, f.OUT
DEST = OUT / 'reception-216.json'
SOURCE = ROOT / 'scripts/actual-tree/output'


def compact(a):
    return {k: v for k, v in a.items() if k not in ('rows', 'references')}


def main():
    paths_out = [OUT / ('actual-216-coordinate-' + str(v) + '.' + m + '.jsonl.gz')
                 for v in range(2) for m in ('native', 'not-or')]
    assert not any(p.exists() for p in [DEST] + paths_out), 'preserve earlier artifacts'
    cert = dict(step=216, complete=False, failures=[], phase='source-reception', exports=[])
    save = lambda: r.save(DEST, cert)
    save()
    try:
        inp_path = SOURCE / 'empty-zero-repaired.input.json'
        inp = r.strict_read(inp_path.read_bytes()); d = inp['request']
        verify = h.module('reception216_contract', SOURCE.parent / 'verify.py')
        goals = verify.contract(inp['source'], inp['edges'], d)
        previous = r.strict_read((SOURCE / 'audit-214.json').read_bytes())
        assert previous['complete'] and previous['failures'] == []
        case = next(a for a in previous['cases'] if a['name'] == 'empty-zero-repaired')
        assert case['complete'] and case['input'] == str(inp_path.relative_to(ROOT))
        original = []
        for i in range(2):
            path = SOURCE / ('retained-' + str(i) + '.native.jsonl.gz')
            # Reconstruct the original optional-proof endpoints, not a header promise.
            term = 'unused'
            for _ in range(35 if i else 0): term = verify.e.neg(term)
            goal = verify.c.serialize(verify.e.imp(term, term))
            got = r.scan(r.f.FastSyntax, path, goal)
            assert compact(got) == previous['inputs'][i]
            original.append((path, len(got['rows'])))
        paths = [SOURCE / ('empty-zero-repaired-v' + str(v) + '.native.jsonl.gz') for v in range(2)]
        source_checks = []
        for v, path in enumerate(paths):
            image = path.with_name(path.name.replace('.native.', '.not-or.'))
            got = r.scan(r.f.FastSyntax, path, goals[v], image, imports=original)
            assert compact(got) == case['vertices'][v]['full']
            source_checks.append(compact(got))
        cert.update(original_input=str(inp_path.relative_to(ROOT)),
                    original_input_sha256=hashlib.sha256(inp_path.read_bytes()).hexdigest(),
                    original_received=[dict(path=str(p.relative_to(ROOT)), lines=n) for p, n in original],
                    source_packages=source_checks, phase='closure-reception')
        save()
        initial = r.strict_read((OUT / 'certificate-202.json').read_bytes())
        lib = f.library(initial)
        obj = h.lc.Closure(d, paths, lib)
        terms = {m: h.suite.measured_terms(d, m) for m in ('native', 'not-or')}
        bound = h.lc.thresholds(d, obj.packages, initial['constants'], terms,
                              max(a['name_bytes'] for a in lib.values()))
        # Independently replayed input measurements must be the paid inputs.
        assert bound['imported_records'] == sum(a['measurements']['native']['lines'] for a in source_checks)
        for m in terms:
            assert bound['formats'][m]['imported_nodes'] == sum(a['node_sums'][m] for a in source_checks)
            assert bound['formats'][m]['imported_depth'] == max(a['depths'][m] for a in source_checks)
        # Source-only majorant: L066's bound, not measured/generated exports.
        source_bound = case['bounds']
        source_payload = max([1,len(inp['source']['q'])]+[len(x) for x in inp['source']['letters']]+
            [a['name_bytes'] for a in previous['inputs']]+
            [a['name_bytes'] for a in previous['library'].values()]+
            [a['name_bytes'] for a in lib.values()])
        assert bound['formats']['native']['payload_bytes'] <= source_payload
        majorant_packages = [dict(rows=range(source_bound['formats']['native']['lines']),
            node_sums={m: source_bound['formats'][m]['bytes'] for m in terms},
            depths={m: source_bound['formats'][m]['depth'] for m in terms},
            name_bytes=source_payload) for _ in range(d['N'])]
        composed = h.lc.thresholds(d, majorant_packages, initial['constants'], terms,
                                  max(a['name_bytes'] for a in lib.values()))
        for m in terms:
            for key in ('lines', 'depth', 'record_nodes', 'bytes', 'aggregate_bytes'):
                assert bound['formats'][m][key] <= composed['formats'][m][key]
        cert.update(uniform_ledger=bound, source_bound=source_bound,
                    composed_source_majorant=composed, imports=obj.imports, phase='compile')
        save()
        chain = h.module('reception216_chain', ROOT / 'scripts/backward-zero/chain.py')
        receiving = {k: d[k] for k in ('N','n','q','suffixes','letters')}
        receiving.update(beta=obj.tables['beta'], G=obj.tables['G'], levels=[dict(k=0,R=[],T=[])])
        expected = chain.validate(receiving)
        assert expected == [h.ep.e.c.serialize(g) for g in obj.tables['closed']]
        cert['receiving'] = receiving
        for v in range(d['N']):
            print('compile actual coordinate', v, flush=True)
            obj.row(v)
            assert obj.root == len(obj.p.rows)-1
            cert.update(phase='write', active_coordinate=v, active_root=obj.root)
            save()
            writers = {}; streams = []
            for m, image in [('native', False), ('not-or', True)]:
                path = OUT / ('actual-216-coordinate-' + str(v) + '.' + m + '.jsonl.gz')
                writers[m] = f.write(obj, path, image); streams.append(path)
            cert['phase'] = 'replay'; save()
            checked = r.scan(r.f.FastSyntax, streams[0], expected[v], streams[1],
                roots={root: expected[w] for w, root in enumerate(obj.coordinate_roots)},
                imports=[(path, len(pkg['rows'])) for path, pkg in zip(paths,obj.packages)])
            export = dict(coordinate=v, root=obj.root, endpoint=expected[v],
                          complete_input_retention=True, literal_image=True, proofs={})
            for m in writers:
                measured = checked['measurements'][m]
                assert all(writers[m][k] == measured[k] for k in ('bytes','lines','sha256'))
                assert obj.root == measured['lines']-1
                checks = h.ledger.check(measured,bound['formats'][m])
                assert checked['depths'][m] <= bound['formats'][m]['depth']
                export['proofs'][m] = dict(measurement=measured, uniform_checks=checks,
                    full_field_depth=checked['depths'][m], writer_matches=True)
                print(v,m,'lines',measured['lines'],'/',bound['lines'],
                      'bytes',measured['bytes'],'/',bound['formats'][m]['bytes'],flush=True)
            cert['exports'].append(export); save()
        assert obj.max_argument_height <= bound['H']
        assert all(t['max_height'] <= bound['H'] for t in obj.traces)
        syntax = r.f.FastSyntax()
        try:
            cert['argument_checks'] = {}
            for m, offset in [('native',0),('not-or',2)]:
                stats = [syntax.stats[syntax.parse(s)] for call in obj.calls for s in call['arguments'].values()]
                nodes=max([s[offset] for s in stats]+[0]); depth=max([s[offset+1] for s in stats]+[0])
                assert nodes<=bound['formats'][m]['argument_nodes'] and depth<=bound['formats'][m]['argument_depth']
                cert['argument_checks'][m]=dict(nodes=nodes,depth=depth)
        finally: syntax.close()
        cert['aggregate'] = {}
        for m in terms:
            size=sum(e['proofs'][m]['measurement']['bytes'] for e in cert['exports'])
            lines=sum(e['proofs'][m]['measurement']['lines'] for e in cert['exports'])
            assert lines<=bound['aggregate_lines'] and size<=bound['formats'][m]['aggregate_bytes']
            cert['aggregate'][m]=dict(lines=lines,required_lines=bound['aggregate_lines'],bytes=size,
                required_bytes=bound['formats'][m]['aggregate_bytes'],
                composed_required_bytes=composed['formats'][m]['aggregate_bytes'])
            print(m,'aggregate bytes',size,'/',bound['formats'][m]['aggregate_bytes'],flush=True)
        cert.update(complete=True,phase='complete',max_argument_height=obj.max_argument_height)
        save(); print('PASS two full pairs;',DEST.relative_to(ROOT),flush=True)
    except BaseException as exc:
        cert['failures'].append(type(exc).__name__+': '+str(exc)); save(); raise


def check_completed_accounting():
    """Check the saved composition solely from original inputs; emit no proofs."""
    cert = r.strict_read(DEST.read_bytes())
    assert cert['complete'] and not cert['failures']
    inp_path = ROOT / cert['original_input']; inp = r.strict_read(inp_path.read_bytes())
    old = r.strict_read((SOURCE / 'audit-214.json').read_bytes())
    initial = r.strict_read((OUT / 'certificate-202.json').read_bytes())
    lib = f.library(initial); d = inp['request']
    assert inp['source']['tree'] == ['zero'] and inp['source']['letters'] == []
    assert hashlib.sha256(inp_path.read_bytes()).hexdigest() == cert['original_input_sha256']
    B = max([1,len(inp['source']['q'])]+[a['name_bytes'] for a in old['inputs']]+
            [a['name_bytes'] for a in old['library'].values()]+[a['name_bytes'] for a in lib.values()])
    assert B == 6 and all(a['name_bytes']<=B for a in cert['source_packages'])
    # Exact L066 equation (1) recomputation on U=1,d=0,n=0.
    J = 10+2568*2000; P = 48*4**10
    source_bound = dict(U=1,source_depth=0,N=2,n=0,H=9,operations=2000,
        generated_records=2568*2000,argument_nodes=P,formats={})
    for m,D,S,c in [('native',18,2040,3),('not-or',24,2712,6)]:
        K=sum(a['node_sums'][m] for a in old['inputs'])
        delta=max(a['depths'][m] for a in old['inputs'])
        size=(B+4)*(K+(2568*2000+1)*S*P)+(J+2)*(256+64*(J+1).bit_length())
        source_bound['formats'][m]=dict(lines=J,depth=max(delta,D+c*9+3),
            record_nodes=max(K,S*P),bytes=size,aggregate_bytes=2*size,aggregate_bits=16*size)
        for a in cert['source_packages']:
            assert a['measurements'][m]['lines']<=J and a['measurements'][m]['bytes']<=size
            assert a['node_sums'][m]<=a['measurements'][m]['bytes']
            assert a['depths'][m]<=source_bound['formats'][m]['depth']
    assert source_bound == cert['source_bound']
    terms={m:h.suite.measured_terms(d,m) for m in ('native','not-or')}
    packages=[dict(rows=range(J),node_sums={m:source_bound['formats'][m]['bytes'] for m in terms},
        depths={m:source_bound['formats'][m]['depth'] for m in terms},name_bytes=B) for _ in range(2)]
    composed=h.lc.thresholds(d,packages,initial['constants'],terms,max(a['name_bytes'] for a in lib.values()))
    assert composed == cert['composed_source_majorant']
    for m in terms:
        assert cert['aggregate'][m]['bytes']<=composed['formats'][m]['aggregate_bytes']
    original_bytes=len(inp_path.read_bytes())+sum(a['measurements']['native']['bytes'] for a in old['inputs'])
    cert['source_accounting_check']=dict(complete=True,source_payload_bytes=B,
        explicit_source_and_optional_native_bytes=original_bytes,
        optional_path_framing_bytes=len(json.dumps(cert['original_received']).encode('ascii')),
        original_optional_records=10,source_bound_recomputed=True,composition_recomputed=True,
        node_count_majorant='Every expanded syntax node contributes at least one uncompressed ASCII byte; header/framing only enlarge it.',
        library='Fixed finite source and closure libraries are paid constants, not generated output inputs.')
    r.save(DEST,cert)
    print('PASS source-only composition; source/optional bytes',original_bytes,'payload',B,';',DEST.relative_to(ROOT))


if __name__ == '__main__':
    if sys.argv[1:] == ['--check-accounting-only']: check_completed_accounting()
    else: main()
