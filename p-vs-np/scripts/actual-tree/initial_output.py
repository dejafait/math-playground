"""Step 236: exact initial-output unit/symmetry specialization, no zero receiver.

No optional proof inputs, source normalization, synthesis or earlier generated
packages. The two existing fixed strings are checked in full before copying.
"""
import copy
import gzip
import hashlib
import json
from pathlib import Path
import build as h
import initial_verify as iv

b, p = h.b, h.p
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
OUT = HERE / 'output' / 'initial-236'
DEST = HERE / 'output' / 'certificate-236.json'
a = h.module('initial_236_archive_check', HERE.parent / 'backward-zero' / 'audit_archives.py')


def encoded(obj):
    return (json.dumps(obj, separators=(',', ':'), ensure_ascii=True)+'\n').encode('ascii')


def save(cert):
    DEST.write_text(json.dumps(cert, indent=2)+'\n')


def scan(native, goal, image=None):
    a.syntax = a.Syntax()
    return a.scan(native, goal, image)


def compact(result):
    return {k: v for k, v in result.items() if k not in ('rows', 'references')}


def libraries(cert):
    E, P, I = iv.e.eq, iv.e.prod, iv.e.imp
    expected = dict(unitR=E(P('A', I('q', 'q')), 'A'),
                    symm=I(E('A', 'B'), E('B', 'A')))
    lib = {}
    for name, goal in expected.items():
        folder = HERE if name == 'unitR' else HERE.parent / 'balanced-slot'
        paths = [folder / 'output' / (name+'.'+mode+'.jsonl.gz') for mode in ('native', 'not-or')]
        literal = iv.c.serialize(goal)
        checked = scan(paths[0], literal, paths[1])
        lib[name] = b.aggregate.load(paths[0], literal)
        cert['library'][name] = compact(checked)
        save(cert)
    constants = dict(lines={name: len(lib[name]['rows']) for name in lib}, formats={})
    for mode in ('native', 'not-or'):
        constants['formats'][mode] = dict(
            D=max(v['depths'][mode] for v in cert['library'].values()),
            S=max(v['measurements'][mode]['max_record_nodes'] for v in cert['library'].values()))
    cert['constants'] = constants
    save(cert)
    return lib


def construct(envelope, lib, depth_factor=4):
    expected = iv.receive(envelope, depth_factor)
    data = h.construct(envelope['source'], depth_factor)
    if data['edges'] != envelope['edges'] or data['request'] != envelope['request']:
        raise iv.c.Invalid('emitter source reconstruction mismatch')
    f = data['occurrences'][0]['value']
    s = data['suffix'][0]
    o = b.Store(lib, envelope['source']['q'])
    unit = o.law('unitR', {'A': f})
    o.root = o.symm(s, f, unit)
    if p.text(o.p.rows[o.root][0]) != expected['goal'] or o.root != len(o.p.rows)-1:
        raise iv.c.Invalid('actual final bridge record')
    return o, expected


def ledger(envelope, constants, admission=4):
    expected = iv.receive(envelope, admission)
    Q = len(encoded(envelope))
    H = expected['depth']+1
    Pstar = 48 * 4**(H+1)
    J = sum(constants['lines'].values())+1
    B = max([1, len(envelope['source']['q'])]+[len(x) for x in envelope['source']['letters']])
    F = 256+64*(J+1).bit_length()
    ans = dict(Q=Q, U=expected['U'], source_depth=expected['depth'], admission=admission,
               B=B, H=H, argument_nodes=Pstar, records=J, formats={})
    for mode, coefficient in (('native', 3), ('not-or', 6)):
        D, S = [constants['formats'][mode][k] for k in ('D', 'S')]
        ans['formats'][mode] = dict(lines=J, record_nodes=S*Pstar,
            full_field_depth=D+coefficient*H+3,
            bytes=(J+2)*((B+4)*S*Pstar+F))
    ans['metadata_bytes'] = 10000*(Q+J+2)**2+(B+4)*sum(
        c['S'] for c in constants['formats'].values())*Pstar
    ans['total_bytes'] = Q+ans['metadata_bytes']+sum(f['bytes'] for f in ans['formats'].values())
    ans['total_bits'] = 8*ans['total_bytes']
    return ans


def write(o, path, image=False):
    # AppendProof serialization retains both complete fixed occurrences, unused
    # lines included, and uses literal images only. No reachability pruning.
    return o.write(path, image)


def case(name, source, lib, cert):
    folder = OUT / name
    folder.mkdir()
    data = h.construct(source)
    envelope = dict(source=source, edges=data['edges'], request=data['request'])
    input_path = folder / 'source.json'
    input_path.write_bytes(encoded(envelope))
    required = ledger(envelope, cert['constants'])
    o, expected = construct(envelope, lib)
    record = dict(name=name, input=str(input_path.relative_to(ROOT)), complete=False,
                  required=required, calls=o.calls)
    cert['cases'].append(record); save(cert)
    paths = [folder / ('bridge.'+mode+'.jsonl.gz') for mode in ('native', 'not-or')]
    written = [write(o, path, bool(i)) for i, path in enumerate(paths)]
    got = scan(paths[0], expected['goal'], paths[1])
    for mode, writer in zip(('native', 'not-or'), written):
        actual, bound = got['measurements'][mode], required['formats'][mode]
        for key in ('lines', 'bytes', 'sha256'):
            assert actual[key] == writer[key]
        assert actual['lines'] <= bound['lines']
        assert actual['bytes'] <= bound['bytes']
        assert actual['max_record_nodes'] <= bound['record_nodes']
        assert got['depths'][mode] <= bound['full_field_depth']
    assert len(o.calls) == 2
    argument_checks = []
    for call in o.calls:
        for key, text in call['arguments'].items():
            node = a.syntax.parse(text); stats = a.syntax.stats[node]
            assert max(stats[0], stats[2]) <= required['argument_nodes']
            assert stats[1] <= 3*required['H']+3 and stats[3] <= 6*required['H']+3
            argument_checks.append(dict(law=call['name'], argument=key, stats=stats))
    manifest = dict(input='source.json', goal=expected['goal'],
        image_goal=a.syntax.text(a.syntax.parse(expected['goal']), True),
        files={mode: dict(path=path.name, **writer) for mode, path, writer in
               zip(('native', 'not-or'), paths, written)})
    raw = encoded(manifest)
    (folder / 'bridge.json').write_bytes(raw)
    assert len(raw) <= required['metadata_bytes']
    actual_total = input_path.stat().st_size+len(raw)+sum(w['bytes'] for w in written)
    assert actual_total <= required['total_bytes']
    record.update(complete=True, expected=expected, checks=compact(got), argument_checks=argument_checks,
                  manifest=str((folder/'bridge.json').relative_to(ROOT)), metadata_actual_bytes=len(raw),
                  total_actual_bytes=actual_total)
    save(cert)
    print(name, 'PASS', got['measurements']['native']['lines'], 'records/format;',
          actual_total, '/', required['total_bytes'], 'total bytes', flush=True)
    return envelope, paths, expected['goal']


def reject_sources(envelope, cert):
    def reject(label, mutate):
        value = copy.deepcopy(envelope); mutate(value)
        try:
            iv.receive(value)
        except iv.c.Invalid as error:
            cert['rejections'].append(dict(label=label, rejected=True, reason=str(error)))
        else:
            raise AssertionError('accepted '+label)
        (OUT / ('reject-'+label+'.json')).write_bytes(encoded(value))
        save(cert)
    reject('source-suffix', lambda d: d['request']['suffixes'].__setitem__(0, 'q'))
    reject('source-constant', lambda d: d['source'].__setitem__('tree', ['zero']))
    reject('request-q', lambda d: d['request'].__setitem__('q', 'changed'))
    reject('dictionary-duplicate', lambda d: d['source']['letters'].append(d['source']['letters'][0]))
    reject('optional-proof', lambda d: d.__setitem__('proofs', []))
    reject('source-position', lambda d: d['source'].__setitem__('tree', ['var', True]))
    reject('source-connector', lambda d: d['edges'][0].__setitem__('w', 0))


def reject_streams(paths, goal, cert):
    def reject(label, image, mutate):
        with gzip.open(paths[image], 'rb') as stream:
            rows = [json.loads(raw) for raw in stream]
        mutate(rows)
        path = OUT / ('reject-'+label+'.jsonl.gz')
        with gzip.open(path, 'wb') as stream:
            for row in rows:
                stream.write(encoded(row))
        try:
            scan(paths[0] if image else path, goal, path if image else paths[1])
        except (AssertionError, iv.c.Invalid, a.ep.c.Invalid) as error:
            cert['rejections'].append(dict(label=label, rejected=True, reason=type(error).__name__+': '+str(error),
                                           path=str(path.relative_to(ROOT))))
        else:
            raise AssertionError('accepted '+label)
        save(cert)
    reject('native-substitution', False, lambda rows: rows[1]['subs'].__setitem__('A', 'changed'))
    reject('native-forward-reference', False, lambda rows: rows[-1]['refs'].__setitem__(0, len(rows)-1))
    reject('native-final-record', False, lambda rows: rows.pop())
    reject('native-extra-field', False, lambda rows: rows[1].__setitem__('unused', 0))
    reject('image-substitution', True, lambda rows: rows[1]['subs'].__setitem__('A', 'changed'))
    reject('image-endpoint', True, lambda rows: rows[0].__setitem__('goal', 'changed'))


def main():
    if DEST.exists() or OUT.exists():
        raise RuntimeError('preserve earlier evidence; choose fresh step paths')
    OUT.mkdir()
    cert = dict(step=236, complete=False, failures=[], library={}, cases=[], rejections=[],
                contract='No optional proof occurrences; distinct dictionary names; no formal-zero premise.')
    save(cert)
    try:
        lib = libraries(cert)
        cases = [
            ('zero-deleted', ['zero'], [], 'q', True),
            ('zero-retained', ['zero'], [], 'q', False),
            ('one', ['one'], [], 'q', False),
            ('variable-q', ['var', 0], ['q'], 'q', True),
            ('variable-schematic', ['var', 1], ['q', 'A', 'B', 'C'], 'A', False),
            ('final-plus-one', ['add', ['var', 0], ['one']], ['q', 'A', 'B'], 'q', False),
            ('product-repeat', ['mul', ['var', 0], ['var', 0]], ['q', 'unused'], 'q', True),
            ('repeated-subtrees', ['mul', ['add', ['var', 0], ['var', 1]],
                                         ['add', ['var', 0], ['var', 1]]], ['A', 'B', 'q'], 'A', False),
            ('mixed-constant', ['add', ['zero'], ['mul', ['var', 0], ['one']]], ['C'], 'q', True),
        ]
        for name, tree, letters, q, delete_zero in cases:
            result = case(name, dict(tree=tree, letters=letters, q=q, delete_zero=delete_zero), lib, cert)
            if name == 'variable-schematic':
                reject_sources(result[0], cert)
            if name == 'variable-q':
                reject_streams(result[1], result[2], cert)
        cert['complete'] = True; save(cert)
        print('PASS', len(cert['cases']), 'complete pairs;', len(cert['rejections']),
              'rejections; failures', cert['failures'], '; certificate', DEST.relative_to(ROOT), flush=True)
    except BaseException as error:
        cert['failures'].append(type(error).__name__+': '+str(error)); save(cert)
        raise


if __name__ == '__main__':
    main()
