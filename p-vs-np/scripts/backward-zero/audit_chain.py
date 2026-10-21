"""Step 200: replay complete chain archives; never synthesize proof strings."""
import gzip
import json
from pathlib import Path
import audit_archives as a

ROOT, OUT = a.ROOT, a.OUT
DEST = OUT / 'audit-200.json'


def row_request(data, i, j):
    base = {k: data[k] for k in ('N', 'n', 'q', 'suffixes', 'letters', 'beta', 'G')}
    current, nxt = data['levels'][i:i+2]
    return dict(base, k=nxt['k'], r=[current['R'][j]], R_next=nxt['R'], T=current['T'][j])


def bounds(data, inputs, constants, names):
    """Equations (1)/(2), independent of chain.thresholds and saved ledgers."""
    m = sum(x['k'] for x in data['levels'][:-1])
    D = 2 + data['N'] + data['n'] + max(x['k'] for x in data['levels'])
    h = (D-1).bit_length()
    V, H = 2**(3*h+4), 9*h+20
    G = m*(constants['L']+1)*10000*V**2*(H+1)**2
    I = sum(len(x['rows']) for x in inputs)
    J = I+G
    locations = (m+len(data['levels'])+data['N']+2)*(512+128*(J+len(data['levels'])+m+2).bit_length())
    out = {}
    for mode, c in [('native', 3), ('not-or', 6)]:
        t, depth, termnames = a.term_stats(data, mode)
        K = sum(x['node_sums'][mode] for x in inputs)
        delta = max(x['depths'][mode] for x in inputs)
        B = max(1, names, termnames, *(x['name_bytes'] for x in inputs))
        S, Dlib = constants[mode]['S'], constants[mode]['D']
        P = 8*4**(H+1)*(t+1)
        A = max(K, S*P)
        size = (B+4)*(K+G*S*P+A)+(J+2)*(256+64*(J+1).bit_length())
        out[mode] = dict(lines=J, depth=max(delta, Dlib+c*H+depth),
                         record_nodes=A, bytes=size, imported_nodes=K,
                         argument_nodes=P, argument_depth=c*H+depth)
    return out, locations


def main():
    cert = {'complete': False, 'failures': [], 'library': {}, 'cases': []}
    def save(): DEST.write_text(json.dumps(cert, indent=2)+'\n')
    save()
    try:
        saved = json.loads((OUT/'chain-198-certificate.json').read_text())
        assert saved['complete'] and not saved['failures'] and len(saved['cases']) == 3
        constants = {'L': 0, 'native': {'D': 0, 'S': 0}, 'not-or': {'D': 0, 'S': 0}}
        names = 1
        for name, goal in a.ep.fixed().items():
            records = saved['library'][name]
            checked = a.scan(ROOT/records['native']['path'], a.ep.c.serialize(goal),
                             ROOT/records['not-or']['path'])
            for mode, measured in checked['measurements'].items():
                a.same_measurement(measured, records[mode])
                constants[mode]['D'] = max(constants[mode]['D'], measured['max_line_depth'])
                constants[mode]['S'] = max(constants[mode]['S'], measured['max_record_nodes'])
            constants['L'] = max(constants['L'], len(checked['rows']))
            names = max(names, checked['name_bytes'])
            cert['library'][name] = checked['measurements']
        assert constants == saved['constants']
        cert['constants'] = constants
        save()
        print('28 fixed-law streams replayed; constants agree', flush=True)
        for case in saved['cases']:
            data = json.loads((ROOT/case['request']).read_text())
            fixed = {k: data[k] for k in ('N','n','q','suffixes','letters','beta','G')}
            fixed.update(k=0, r=[[0]*data['N']], R_next=[], T=[[[]] for _ in range(data['n'])])
            goals = a.ep.strings(fixed)['coordinates']
            assert len(case['coordinate_paths']) == data['N']
            inputs, imports, import_metadata = [], [], []
            offset = 0
            for v, (path, goal) in enumerate(zip(case['coordinate_paths'], goals)):
                checked = a.scan(ROOT/path, goal)
                count = len(checked['rows'])
                inputs.append(checked); imports.append((ROOT/path, count))
                import_metadata.append(dict(label='coordinate-'+str(v), start=offset, lines=count, root=offset+count-1))
                offset += count
            assert import_metadata == case['imports']
            location_path = ROOT/case['locations']['path']
            locations = json.loads(location_path.read_text())
            assert set(locations) == {'coordinate_imports','levels','rows'}
            assert locations['coordinate_imports'] == import_metadata
            assert locations['levels'] == [x['k'] for x in data['levels']]
            indexed = [(i,j) for i in range(len(data['levels'])-2,-1,-1)
                       for j in range(data['levels'][i]['k'])]
            assert data['levels'][-1] == dict(k=0, R=[], T=[])
            assert len(indexed) == len(locations['rows']) == len(case['rows'])
            roots, registered, uses = {}, {}, []
            final = goals[-1]
            for (i,j), loc, row in zip(indexed, locations['rows'], case['rows']):
                assert loc == {k:row[k] for k in ('level','row','start','end','required_roots')}
                assert (loc['level'],loc['row']) == (i,j) and loc['start'] == offset
                assert loc['start'] < loc['end']
                request = row_request(data,i,j)
                ends = a.ep.strings(request)['goals']
                rr = loc['required_roots']
                assert len(rr) == 4 and all(type(k) is int and 0 <= k < loc['end'] for k in rr)
                assert rr[-1] == loc['end']-1
                for k, goal in zip(rr,ends):
                    assert k not in roots or roots[k] == goal
                    roots[k] = goal
                nxt = [registered[(i+1,k)] for k in range(request['k'])]
                assert nxt == row['next_roots'] and all(k < loc['start'] for k in nxt)
                selected = sorted({k for table in request['T'] for k,bit in enumerate(table[0]) if bit})
                uses.extend(dict(level=i,row=j,selected_index=k,actual_root=nxt[k],
                                 before=loc['start'],in_Q8_zero_ancestry=True) for k in selected)
                registered[(i,j)] = rr[-1]
                offset, final = loc['end'], ends[-1]
            checked = a.scan(ROOT/case['proofs']['native']['path'], final,
                             ROOT/case['proofs']['not-or']['path'], roots, imports)
            assert len(checked['rows']) == offset
            for use in uses:
                row = next(r for r in locations['rows'] if (r['level'],r['row']) == (use['level'],use['row']))
                assert use['actual_root'] in a.ancestors(checked['references'],row['required_roots'][2])
            assert uses == case['used_next_row_ancestry']
            limits, metadata_limit = bounds(data, inputs, constants, names)
            assert metadata_limit == case['uniform_ledger']['metadata_bytes'] == case['locations']['required']
            assert location_path.stat().st_size == case['locations']['bytes'] <= metadata_limit
            checks = {}
            for mode, measured in checked['measurements'].items():
                a.same_measurement(measured, case['proofs'][mode]['measurement'])
                assert all(case['uniform_ledger']['formats'][mode][k] == v for k,v in limits[mode].items())
                checks[mode] = a.ledger.check(measured, limits[mode])
                assert checked['depths'][mode] <= limits[mode]['depth']
                print(case['name'], mode, 'lines', measured['lines'], '/', limits[mode]['lines'],
                      'depth', checked['depths'][mode], '/', limits[mode]['depth'],
                      'bytes', measured['bytes'], '/', limits[mode]['bytes'], flush=True)
            cert['cases'].append(dict(name=case['name'], measurements=checked['measurements'],
                input_measurements=[x['measurements']['native'] for x in inputs],
                uniform_limits=limits, checks=checks, metadata_bytes=location_path.stat().st_size,
                metadata_limit=metadata_limit, complete_imports=import_metadata,
                indexed_locations=locations['rows'], selected_ancestry=uses,
                full_formula_and_substitution_depths=checked['depths']))
            save()
        regression = json.loads((OUT/'chain-198-extraction-regression.json').read_text())
        assert regression['complete'] and not regression['failures']
        assert regression['records_compared'] == sum(regression[m]['lines'] for m in ('native','not-or'))
        # This reads the complete preservation report, not a new extraction run.
        cert['prior_extraction_report'] = regression
        cert['prior_rejections'] = saved['rejections']
        assert len(cert['prior_rejections']) == 13 and all(x['rejected'] for x in cert['prior_rejections'])
        cert['scope'] = 'Archive replay, all imports/indexed roots and input-only ledger; prior rejection/extraction reports inspected, not rerun.'
        cert['complete'] = True; save()
        print('complete: six chain streams, 28 fixed-law streams; failures', len(cert['failures']),
              'certificate', DEST.relative_to(ROOT), flush=True)
    except Exception as exc:
        cert['failures'].append(dict(type=type(exc).__name__, message=str(exc)))
        save()
        raise


if __name__ == '__main__':
    main()
