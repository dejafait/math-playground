"""Archive-only audit of step 236; no proof emitter or constructor imports."""
import gzip
import importlib.util
import json
import sys
from pathlib import Path
import initial_verify as iv

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE.parent / 'backward-zero'))
spec = importlib.util.spec_from_file_location('audit239_scanner', HERE.parent / 'backward-zero' / 'audit_archives.py')
a = importlib.util.module_from_spec(spec); spec.loader.exec_module(a)
DEST = HERE / 'output' / 'audit-239.json'


def encoded(d):
    return (json.dumps(d, separators=(',', ':'), ensure_ascii=True)+'\n').encode('ascii')


def scan(native, goal, image):
    a.syntax = a.Syntax()
    r = a.scan(native, goal, image)
    return {k: v for k, v in r.items() if k not in ('rows', 'references')}


def rows(path):
    with gzip.open(path, 'rb') as stream:
        return [a.read(raw) for raw in stream]


def subst(text, env):
    def visit(t):
        if isinstance(t, str):
            return env.get(t, t)  # Never recurse into the replacement.
        return tuple([t[0]] + [visit(x) for x in t[1:]])
    return iv.c.serialize(visit(iv.c.parse(text, 'native')[0]))


def canonical_edges(source):
    edges = []; count = 0
    def visit(t):
        nonlocal count
        entry = count; count += 1
        if t[0] in ('add', 'mul'):
            le, lx = visit(t[1]); re, rx = visit(t[2])
        end = count; count += 1
        if t[0] == 'add':
            pairs = [(entry, le), (lx, end), (entry, re), (rx, end)]
        elif t[0] == 'mul':
            pairs = [(entry, le), (lx, re), (rx, end)]
        else:
            pairs = []
            if t[0] != 'zero' or not source['delete_zero']:
                edge = dict(v=entry, w=end, kind=t[0])
                if t[0] == 'var': edge['position'] = t[1]
                edges.append(edge)
        edges.extend(dict(v=v, w=w, kind='one') for v, w in pairs)
        return entry, end
    visit(source['tree'])
    return edges


def main():
    assert not DEST.exists(), 'preserve earlier audit evidence'
    cert = dict(step=239, complete=False, failures=[], library={}, cases=[], rejections=[])
    def save(): DEST.write_text(json.dumps(cert, indent=2)+'\n')
    save()
    try:
        old = a.read((HERE/'output/certificate-236.json').read_bytes())
        oldledger = a.read((HERE/'output/source-ledger-236.json').read_bytes())
        assert old['complete'] and oldledger['complete']
        assert old['failures'] == oldledger['failures'] == []
        e, c = iv.e, iv.c
        fixed = dict(unitR=e.eq(e.prod('A', e.imp('q', 'q')), 'A'),
                     symm=e.imp(e.eq('A', 'B'), e.eq('B', 'A')))
        libraries = {}
        for name, term in fixed.items():
            folder = HERE if name == 'unitR' else HERE.parent/'balanced-slot'
            paths = [folder/'output'/f'{name}.{mode}.jsonl.gz' for mode in ('native', 'not-or')]
            got = scan(paths[0], c.serialize(term), paths[1])
            assert got == old['library'][name]
            libraries[name] = rows(paths[0])[1:]
            cert['library'][name] = got
            save()
        J = sum(len(r) for r in libraries.values())+1
        constants = dict(lines={k:len(v) for k,v in libraries.items()}, formats={})
        for mode in ('native', 'not-or'):
            constants['formats'][mode] = dict(
                D=max(x['depths'][mode] for x in cert['library'].values()),
                S=max(x['measurements'][mode]['max_record_nodes'] for x in cert['library'].values()))
        assert constants == old['constants']
        assert constants == dict(lines=dict(unitR=761, symm=872),
            formats={'native':dict(D=16,S=584),'not-or':dict(D=22,S=788)})
        cert['constants'] = constants
        for prior in old['cases']:
            raw = (ROOT/prior['input']).read_bytes(); envelope = a.read(raw)
            assert raw == encoded(envelope)
            checked = iv.receive(envelope)
            source = envelope['source']
            assert envelope['edges'] == canonical_edges(source)
            assert checked == prior['expected']
            manifest_raw = (ROOT/prior['manifest']).read_bytes(); manifest = a.read(manifest_raw)
            folder = (ROOT/prior['manifest']).parent
            assert set(manifest) == {'input','goal','image_goal','files'}
            assert manifest['input'] == 'source.json' and manifest_raw == encoded(manifest)
            assert manifest['goal'] == checked['goal']
            paths = [folder/f'bridge.{mode}.jsonl.gz' for mode in ('native','not-or')]
            got = scan(paths[0], checked['goal'], paths[1])
            assert got == prior['checks']
            assert manifest['image_goal'] == a.syntax.text(a.syntax.parse(checked['goal']), True)
            # Compare every retained fixed record, not only its root or ancestry.
            actual = rows(paths[0])[1:]; offset = 0; retained = []
            F = c.parse(checked['formula'],'native')[0]
            S = c.parse(checked['suffix'],'native')[0]
            for name, env in [('unitR', {'A':F,'q':source['q']}),
                              ('symm', {'A':S,'B':F,'q':source['q']})]:
                for i, row in enumerate(libraries[name]):
                    wanted = dict(f=subst(row['f'],env),rule=row['rule'])
                    if row['rule'] == 'mp': wanted['refs'] = [offset+k for k in row['refs']]
                    else: wanted['subs'] = {k:subst(v,env) for k,v in row['subs'].items()}
                    assert actual[offset+i] == wanted, (name, i, 'full substituted occurrence')
                retained.append(dict(law=name,start=offset,records=len(libraries[name])))
                offset += len(libraries[name])
            assert len(actual) == J == 1634
            assert actual[-1] == dict(f=checked['goal'],rule='mp',refs=[760,1632])
            U,d,n,B = checked['U'],checked['depth'],len(source['letters']),max([1,len(source['q'])]+list(map(len,source['letters'])))
            Q = len(raw); Q0 = 2+len(encoded(source)); H = d+1
            Pstar = 48*4**(H+1); framing = 256+64*(J+1).bit_length()
            R = 1000*(B+4)*(n+2)*(U+2)**3*4**(2*d+3)
            assert Q <= R and U <= Q0 and n <= Q0 and B <= Q0
            required = {}
            for mode, coefficient in [('native',3),('not-or',6)]:
                cc = constants['formats'][mode]
                required[mode] = dict(lines=J,record_nodes=cc['S']*Pstar,
                    full_field_depth=cc['D']+coefficient*H+3,
                    bytes=(J+2)*((B+4)*cc['S']*Pstar+framing))
                assert required[mode] == prior['required']['formats'][mode]
                m = got['measurements'][mode]; bound = required[mode]
                assert m['lines'] == bound['lines']
                assert m['max_record_nodes'] <= bound['record_nodes']
                assert got['depths'][mode] <= bound['full_field_depth']
                assert m['bytes'] <= bound['bytes']
                entry = manifest['files'][mode]
                assert set(entry) == {'path','lines','bytes','sha256','storage_bytes'}
                assert entry['path'] == f'bridge.{mode}.jsonl.gz'
                for key in ('lines','bytes','sha256'): assert entry[key] == m[key]
                assert entry['storage_bytes'] == (folder/entry['path']).stat().st_size
                assert entry['storage_bytes'] <= 2*m['bytes']+100
            def metadata(q): return 10000*(q+J+2)**2+(B+4)*1372*Pstar
            total = Q+len(manifest_raw)+sum(x['bytes'] for x in got['measurements'].values())
            bound = Q+metadata(Q)+sum(x['bytes'] for x in required.values())
            source_bound = R+metadata(R)+sum(x['bytes'] for x in required.values())
            assert len(manifest_raw) <= metadata(Q) and total <= bound <= source_bound
            assert total == prior['total_actual_bytes'] and len(manifest_raw) == prior['metadata_actual_bytes']
            earlier = next(x for x in oldledger['cases'] if x['name']==prior['name'])
            assert earlier['envelope_required_bytes'] == R and earlier['total_required_bytes'] == source_bound
            assert earlier['total_actual_bytes'] == total
            cert['cases'].append(dict(name=prior['name'],input=prior['input'],manifest=prior['manifest'],
                checked=checked, measurements=got, retained=retained,final_refs=[760,1632],
                required=required,source=dict(Q0=Q0,U=U,d=d,n=n,B=B,envelope_actual=Q,envelope_required=R),
                metadata_actual=len(manifest_raw),metadata_required=metadata(Q),
                total_actual=total,total_required=bound,source_total_required=source_bound))
            save()
            print(prior['name'], 'PASS', J, 'records/format;', total, '/', bound,
                  'bytes; source-only', source_bound, flush=True)
        good = next(x for x in old['cases'] if x['name']=='variable-q')
        base = (ROOT/good['manifest']).parent
        for item in old['rejections']:
            label = item['label']
            try:
                if label.startswith(('native-', 'image-')):
                    native = ROOT/item['path'] if label.startswith('native-') else base/'bridge.native.jsonl.gz'
                    image = ROOT/item['path'] if label.startswith('image-') else base/'bridge.not-or.jsonl.gz'
                    scan(native, good['expected']['goal'], image)
                else:
                    iv.receive(a.read((HERE/'output/initial-236'/f'reject-{label}.json').read_bytes()))
            except (AssertionError, ValueError) as error:
                reason = str(error)
                expected = item['reason'].removeprefix('AssertionError: ')
                assert reason == expected, (label,reason,expected)
                cert['rejections'].append(dict(label=label,rejected=True,exception=type(error).__name__,reason=reason))
            else: raise AssertionError('accepted corruption '+label)
            save()
        assert len(cert['cases']) == 9 and len(cert['rejections']) == 13
        cert['complete'] = True; save()
        print('PASS: 2 fixed pairs, 9 bridge pairs, all fixed occurrences, 13 rejections; failures',
              cert['failures'], '; certificate', DEST.relative_to(ROOT), flush=True)
    except BaseException as error:
        cert['failures'].append(type(error).__name__+': '+str(error)); save(); raise


if __name__ == '__main__': main()
