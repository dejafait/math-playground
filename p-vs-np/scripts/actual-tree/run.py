"""One bounded actual-tree attempt; full certificates, no closure exports."""
import copy
import gzip
import hashlib
import json
from functools import lru_cache
from pathlib import Path
import build as h
import verify

b, p, c = h.b, h.p, h.c
HERE = Path(__file__).resolve().parent
OUT = HERE / 'output'; ROOT = HERE.parents[1]
audit = h.module('actual_archive_audit', HERE.parent / 'backward-zero' / 'audit_archives.py')
DEST = OUT / 'certificate-212-repaired.json'

def save(obj): DEST.write_text(json.dumps(obj, indent=2) + '\n')

def write(o, path, image=False):
    # Complete fresh-store serialization, including every received record.
    @lru_cache(4096)
    def spell(f):
        if isinstance(f, str): return f
        if f[0] == 'n': return '(~' + spell(f[1]) + ')'
        a, bb = spell(f[1]), spell(f[2])
        return '((~' + a + ')|' + bb + ')' if image else '(' + a + '>' + bb + ')'
    digest = hashlib.sha256(); size = 0
    with gzip.open(path, 'wb', compresslevel=1) as stream:
        def put(row):
            nonlocal size
            raw = (json.dumps(row, separators=(',', ':')) + '\n').encode('ascii')
            size += len(raw); digest.update(raw); stream.write(raw)
        put(dict(format='not-or' if image else 'native', goal=spell(o.p.rows[o.root][0])))
        for f, rule, refs, subs, deps in o.p.rows:
            assert not deps
            row = dict(f=spell(f), rule=rule)
            if rule == 'mp': row['refs'] = list(refs)
            else: row['subs'] = {k: spell(v) for k, v in subs.items()}
            put(row)
    return dict(lines=len(o.p.rows), bytes=size, sha256=digest.hexdigest())

def library(cert):
    result = {}
    for name in ('refl', 'symm', 'trans', 'congL', 'congR', 'zeroR', 'zeroL', 'prod_zero'):
        folder = HERE.parent / ('backward-zero' if name in ('zeroR', 'zeroL', 'prod_zero') else 'balanced-slot') / 'output'
        expected = b.ep.c.serialize(b.ep.fixed()[name])
        native, image = [folder / (name + '.' + mode + '.jsonl.gz') for mode in ('native', 'not-or')]
        audit.syntax = audit.Syntax()
        checks = audit.scan(native, expected, image)['measurements']
        result[name] = b.aggregate.load(native, expected)
        cert['library'][name] = checks; save(cert)
    for name, goal in h.fixed().items():
        paths = [OUT / (name + '.' + mode + '.jsonl.gz') for mode in ('native', 'not-or')]
        if not any(path.exists() for path in paths):
            synth = p.Proof(); synth.build_helpers(); root = synth.prove_fixed(goal)
            for image, path in enumerate(paths): synth.write(root, path, bool(image))
        elif not all(path.exists() for path in paths):
            raise RuntimeError('incomplete fixed pair; preserve and use a new path')
        # Two implementations check every new fixed record, not just its truth table.
        for image, path in enumerate(paths): c.check(path, p.text(goal, bool(image)))
        audit.syntax = audit.Syntax()
        checks = audit.scan(paths[0], p.text(goal), paths[1])['measurements']
        result[name] = b.aggregate.load(paths[0], p.text(goal))
        cert['library'][name] = checks; save(cert)
        print('fixed', name, 'complete native/image records', checks['native']['lines'], flush=True)
    cert['constants'] = dict(L=max(a['native']['lines'] for a in cert['library'].values()))
    for mode in ('native', 'not-or'):
        cert['constants'][mode] = dict(D=max(a[mode]['max_line_depth'] for a in cert['library'].values()),
                                      S=max(a[mode]['max_record_nodes'] for a in cert['library'].values()))
    save(cert)
    return result

def bounds(source, packages, constants):
    U, depth = h.validate_input(source)
    N, n = 2 * U, len(source['letters'])
    H = 2 * depth + (n + 1).bit_length() + 8
    T = 1000 * (n + 2); G = (constants['L'] + 1) * T
    I = sum(len(a['rows']) for a in packages); J = I + G
    B = max([1, len(source['q']), 1] + [len(x) for x in source['letters']] + [a['name_bytes'] for a in packages])
    F = 256 + 64 * (J + 1).bit_length()
    P = 8 * 4**(H + 1) * 6  # five-node Y/Z/letter atoms in either format
    answer = dict(U=U, source_depth=depth, N=N, n=n, H=H, operations=T, generated_records=G,
                  argument_nodes=P, formats={})
    for mode, coefficient in (('native', 3), ('not-or', 6)):
        K = sum(a['node_sums'][mode] for a in packages)
        delta = max([0] + [a['depths'][mode] for a in packages])
        S, D = constants[mode]['S'], constants[mode]['D']
        byte_bound = (B + 4) * (K + (G + 1) * S * P) + (J + 2) * F
        answer['formats'][mode] = dict(lines=J, depth=max(delta, D + coefficient * H + 3),
            record_nodes=max(K, S * P), bytes=byte_bound,
            aggregate_bytes=N * byte_bound, aggregate_bits=8 * N * byte_bound)
    return answer

def extras():
    # Complete received occurrences with genuine earlier MP references.
    packages, paths = [], []
    for index, depth in enumerate((0, 35)):
        f = 'unused'
        for _ in range(depth): f = p.N(f)
        proof = p.Proof(); root = proof.identity(f)
        path = OUT / ('retained-' + str(index) + '.native.jsonl.gz')
        if not path.exists(): proof.write(root, path)
        packages.append(b.aggregate.load(path, p.text(p.I(f, f)))); paths.append(path)
    return packages, paths

def test(name, source, lib, packages, input_paths, cert):
    data = h.construct(source); request = data['request']
    expected = verify.contract(source, data['edges'], request)
    input_path = OUT / (name + '.input.json')
    input_path.write_text(json.dumps(dict(source=source, edges=data['edges'], request=request), indent=2) + '\n')
    bound = bounds(source, packages, cert['constants'])
    record = dict(name=name, input=str(input_path.relative_to(ROOT)), bounds=bound,
                  vertices=[], aggregate={}, complete=False)
    cert['cases'].append(record); save(cert)
    for v in range(request['N']):
        o = b.Store(lib, source['q'])
        for i, package in enumerate(packages): o.retain(package, 'retained-' + str(i))
        info = h.local(o, data, v)
        assert info['expected'] == expected[v]
        paths = [OUT / (name + '-v' + str(v) + '.' + mode + '.jsonl.gz') for mode in ('native', 'not-or')]
        writers = [write(o, path, bool(image)) for image, path in enumerate(paths)]
        audit.syntax = audit.Syntax()
        replay = audit.scan(paths[0], expected[v], paths[1], imports=[(path, len(package['rows']))
            for path, package in zip(input_paths, packages)])
        measures = replay['measurements']
        for mode, writer in zip(('native', 'not-or'), writers):
            actual, required = measures[mode], bound['formats'][mode]
            for key in ('lines', 'bytes', 'sha256'): assert actual[key] == writer[key]
            assert actual['lines'] <= required['lines'] and actual['bytes'] <= required['bytes']
            assert actual['max_line_depth'] <= required['depth']
            assert actual['max_record_nodes'] <= required['record_nodes']
        args = []
        for call in o.calls:
            for argument in call['arguments'].values():
                node = audit.syntax.parse(argument); s = audit.syntax.stats[node]
                assert s[0] <= bound['argument_nodes'] and s[2] <= bound['argument_nodes']
                assert s[1] <= 3 * bound['H'] + 3 and s[3] <= 6 * bound['H'] + 3
                args.append(s)
        assert info['law_calls'] <= bound['operations']
        record['vertices'].append(dict(v=v, case=info['case'], measures=measures,
            retained=[dict(start=i['start'], lines=i['lines']) for i in o.imports],
            argument_actual_nodes=max(max(s[0], s[2]) for s in args),
            argument_required_nodes=bound['argument_nodes']))
        save(cert)
        print(name, v, info['case'], 'PASS all', measures['native']['lines'], 'records; bytes',
              measures['native']['bytes'], '/', bound['formats']['native']['bytes'], flush=True)
    for mode in ('native', 'not-or'):
        actual = sum(v['measures'][mode]['bytes'] for v in record['vertices'])
        required = bound['formats'][mode]['aggregate_bytes']
        assert actual <= required
        record['aggregate'][mode] = dict(actual_bytes=actual, required_bytes=required,
                                        actual_bits=8 * actual, required_bits=8 * required)
    record['complete'] = True; save(cert)
    return data

def rejections(source, data, cert):
    def reject(label, mutate):
        graph, request = copy.deepcopy(data['edges']), copy.deepcopy(data['request'])
        mutate(graph, request)
        try: verify.contract(source, graph, request)
        except verify.c.Invalid as error:
            cert['rejections'].append(dict(label=label, rejected=True, reason=str(error)))
        else: raise AssertionError('accepted corruption ' + label)
    reject('wrong-suffix', lambda g, d: d['suffixes'].__setitem__(0, 'wrong'))
    reject('wrong-constant', lambda g, d: d.__setitem__('q', 'wrong'))
    reject('wrong-connector', lambda g, d: g[0].__setitem__('w', 0))
    reject('duplicated-letter-position', lambda g, d: d['Eb'][1][1].__setitem__(2, 1))
    reject('selected-order', lambda g, d: d['suffixes'].reverse())
    save(cert)

def main():
    OUT.mkdir(exist_ok=True)
    if DEST.exists(): raise RuntimeError('preserve prior certificate; choose a new step path')
    cert = dict(step=212, complete=False, failures=[], library={}, cases=[], rejections=[],
                preserved_initial='scripts/actual-tree/output/certificate-212.json',
                repair='Final endpoint append now proves Y and detaches Y -> E; original append ended at Y -> E.')
    save(cert)
    try:
        lib = library(cert); packages, input_paths = extras()
        cases = [
            ('empty-zero', dict(tree=['zero'], letters=[], q='q', delete_zero=True)),
            ('retained-zero', dict(tree=['zero'], letters=['x'], q='q', delete_zero=False)),
            ('one', dict(tree=['one'], letters=[], q='q', delete_zero=False)),
            ('addition-final-one', dict(tree=['add', ['var', 1], ['one']], letters=['unused', 'q', 'q'], q='q', delete_zero=False)),
            ('product-repeat', dict(tree=['mul', ['var', 0], ['var', 1]], letters=['q', 'q', 'unused'], q='q', delete_zero=False)),
        ]
        for name, source in cases:
            data = test(name + '-repaired', source, lib, packages, input_paths, cert)
        rejections(cases[-1][1], data, cert)
        cert['complete'] = True; save(cert)
        print('PASS complete actual-tree local packages;', DEST.relative_to(ROOT), flush=True)
    except BaseException as error:
        cert['failures'].append(type(error).__name__ + ': ' + str(error)); save(cert)
        raise

if __name__ == '__main__': main()
