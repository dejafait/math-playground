"""Step 190: complete independent archive audit; never writes old evidence."""
import gzip
import hashlib
import importlib.util
import itertools
import json
import math
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
OUT = HERE / 'output'

def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    obj = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(obj)
    return obj

a = module('factored_audit', HERE.parent / 'original-axiom-guards/audit_archives.py')
ep = module('expanded_reception', HERE / 'endpoints.py')
checker = a.checker
N, I, P, X, E = a.N, a.I, a.P, a.X, a.E

def expanded_values(fact):
    """Enumerate binary choice masks, independently of Cartesian-product emitter."""
    def occurrences(c):
        if 'var' in c: return [(c['var'], c['negative'])]
        return occurrences(c['left']) + occurrences(c['right'])
    lists = []
    for c in fact['clauses']:
        occ = occurrences(c)
        k = sum(not neg for _, neg in occ)
        words = []
        for mask in range(1 << k):
            remaining = k; word = []
            for var, neg in occ:
                if neg: word.append(var)
                else:
                    remaining -= 1
                    if mask & (1 << remaining): word.append(var)
            words.append(word)
        lists.append(words)
    ds = fact['dictionary']
    lists += [[[v, v], [v]] for v in ds]
    lists += [[[u, v], [v, u]] for u, v in itertools.combinations(ds, 2)]
    def word(w):
        if not w: return I(fact['q'], fact['q'])
        out = w[0]
        for v in w[1:]: out = P(out, v)
        return out
    def summation(ws):
        if len(ws) == 1: return word(ws[0])
        middle = len(ws) // 2
        return X(summation(ws[:middle]), summation(ws[middle:]))
    return lists, [summation(ws) for ws in lists]

def fixed_goals():
    out = {'refl': E('A', 'A'),
           'guard-compose': I(I('G', E('A', 'D')), I(E('A', 'B'), I('G', E('B', 'D'))))}
    for arity in (1, 2, 3):
        vs = ['A', 'B', 'C'][:arity]
        for signs in itertools.product((False, True), repeat=arity):
            for shape in (('left', 'right') if arity == 3 else ('left',)):
                leaves = [{'var': v, 'negative': s} for v, s in zip(vs, signs)]
                op = lambda u, v: {'op': 'or', 'left': u, 'right': v}
                c = a.fold(leaves, shape, op)
                fact = {'q': 'q', 'clauses': [c], 'dictionary': []}
                _, expanded = expanded_values(fact)
                factors = [v if s else X(I('q', 'q'), v) for v, s in zip(vs, signs)]
                key = 'bridge-' + ''.join('n' if s else 'p' for s in signs) + '-' + shape
                out[key] = E(a.fold(factors, shape, P), expanded[0])
    return out

def unique(pairs):
    result = {}
    for k, v in pairs:
        if k in result: raise checker.Invalid('duplicate field')
        result[k] = v
    return result

def records(path):
    with gzip.open(path, 'rt', encoding='ascii') as stream:
        for raw in stream: yield json.loads(raw, object_pairs_hook=unique)

def imported_stats(path, expected):
    measured = checker.check(path, expected)
    rows = records(path)
    assert next(rows) == {'format': 'native', 'goal': expected}
    sums = {'native': 0, 'not-or': 0}; depths = dict(sums); B = 1
    count = 0
    for row in rows:
        count += 1
        for field in [row['f']] + list(row.get('subs', {}).values()):
            tree = checker.parse(field, 'native')[0]
            for name in re.findall(r'[^()>~]+', field):
                assert re.fullmatch('[A-Za-z0-9_]+', name)
                B = max(B, len(name))
            for mode, t in [('native', tree), ('not-or', a.image(tree))]:
                size, depth, _ = a.stats(t)
                sums[mode] += size; depths[mode] = max(depths[mode], depth)
    assert count == measured['lines']
    return measured, sums, depths, B

def compare_copy(output_rows, source, env, offset):
    source_rows = records(source); next(source_rows)
    # Token replacement is simultaneous and does not rescan replacement strings.
    def sub(s): return re.sub('[A-Za-z0-9_]+', lambda m: env.get(m[0], m[0]), s)
    count = 0
    for row in source_rows:
        expected = dict(row, f=sub(row['f']))
        if 'subs' in row: expected['subs'] = {k: sub(v) for k, v in row['subs'].items()}
        if 'refs' in row: expected['refs'] = [k + offset for k in row['refs']]
        assert next(output_rows) == expected, ('complete copied-record mismatch', source, count)
        count += 1
    return count

def main():
    old_path = OUT / 'certificate-188.json'
    raw = old_path.read_bytes(); old = json.loads(raw)
    cert = {'complete': False, 'failures': [], 'fixed': {}, 'growing': [], 'rejections': [],
            'prior_certificate_sha256': hashlib.sha256(raw).hexdigest()}
    dest = OUT / 'audit-190.json'
    def save(): dest.write_text(json.dumps(cert, indent=2) + '\n')
    def checked(path, expected, previous):
        result = checker.check(path, checker.serialize(expected))
        assert result == previous, ('full measurement mismatch', path)
        return result
    save()
    try:
        assert old['complete'] and not old['failures']
        goals = fixed_goals(); assert set(goals) == set(old['library']) and len(goals) == 24
        fixed_paths = set(); growing_paths = set()
        for name, goal in goals.items():
            result = {}
            for mode, target in [('native', goal), ('not-or', a.image(goal))]:
                path = OUT / ('fixed-' + name + '.' + mode + '.jsonl.gz')
                fixed_paths.add(path)
                result[mode] = checked(path, target, old['library'][name][mode])
            result['image_records'] = a.compare_images(OUT / ('fixed-' + name + '.native.jsonl.gz'),
                                                     OUT / ('fixed-' + name + '.not-or.jsonl.gz'))
            cert['fixed'][name] = result; save()
        constants = {'L': max(r['native']['lines'] for r in cert['fixed'].values())}
        for mode in ('native', 'not-or'):
            constants[mode] = {'D': max(r[mode]['max_line_depth'] for r in cert['fixed'].values()),
                               'S': max(r[mode]['max_record_nodes'] for r in cert['fixed'].values())}
        assert constants == old['constants']
        cert['constants'] = constants; save()
        print('PASS 24 complete fixed pairs; maxima', constants, flush=True)
        for case in old['cases']:
            request = ROOT / case['request']; data = json.loads(request.read_text())
            fact = data['factored']; received = ep.request(data)
            g, fs, z = a.independent_request(fact)
            words, es = expanded_values(fact)
            assert received == (g, fs, es)
            assert data['expanded_words'] == [[{'coefficient': 1, 'word': w} for w in ws] for ws in words]
            assert len(es) == len(case['proofs'])
            for idx, saved in enumerate(case['proofs']):
                assert saved['position'] == idx + 1
                guard = ROOT / saved['import']
                imp, sums, depths, payload = imported_stats(guard, checker.serialize(I(g, E(fs[idx], z))))
                assert imp['sha256'] == saved['import_sha256'] and imp['lines'] == saved['import_lines']
                J = imp['lines'] + 2 * constants['L'] + 2
                result = {'case': case['name'], 'position': idx + 1, 'import': imp, 'formats': {}}
                for mode, tr in [('native', lambda t: t), ('not-or', a.image)]:
                    previous = saved['formats'][mode]; path = ROOT / previous['measurement']['path']
                    growing_paths.add(path)
                    measured = checked(path, tr(I(g, E(es[idx], z))), previous['measurement'])
                    sizes = [a.stats(tr(t)) for t in (g, fs[idx], es[idx], z)]
                    W = sum(t[0] for t in sizes) + 8; d = max(t[1] for t in sizes)
                    B = max(payload, 1, *(t[2] for t in sizes))
                    R = max(sums[mode], constants[mode]['S'] * W)
                    delta = max(depths[mode], constants[mode]['D'] + d)
                    H = 256 + 64 * math.ceil(math.log2(J + 2))
                    bounds = {'lines': J, 'depth': delta, 'record_nodes': R, 'bytes': (J + 2) * ((B + 4) * R + H)}
                    assert bounds == previous['bounds']
                    assert {'W': W, 'd': d, 'B': B, 'import_record_node_sum': sums[mode]} == previous['parameters']
                    tests = {k: measured[v] <= bounds[k] for k, v in [('lines', 'lines'), ('depth', 'max_line_depth'),
                             ('record_nodes', 'max_record_nodes'), ('bytes', 'bytes')]}
                    assert tests == previous['tests'] and all(tests.values())
                    result['formats'][mode] = {'measurement': measured, 'bounds': bounds, 'tests': tests,
                        'parameters': {'J': J, 'W': W, 'd': d, 'R': R, 'Delta': delta, 'H': H, 'B': B}}
                native = ROOT / saved['formats']['native']['measurement']['path']
                translated = ROOT / saved['formats']['not-or']['measurement']['path']
                result['image_records'] = a.compare_images(native, translated)
                rows = records(native); next(rows)
                count = compare_copy(rows, guard, {}, 0)
                if idx < len(fact['clauses']):
                    def occ(c): return [c] if 'var' in c else occ(c['left']) + occ(c['right'])
                    c = fact['clauses'][idx]; os = occ(c)
                    shape = 'right' if len(os) == 3 and 'var' in c['left'] else 'left'
                    key = 'bridge-' + ''.join('n' if o['negative'] else 'p' for o in os) + '-' + shape
                    env = dict(zip(['A', 'B', 'C'], [o['var'] for o in os])); env['q'] = fact['q']
                else:
                    assert fs[idx] == es[idx]
                    key = 'refl'; env = {'A': checker.serialize(fs[idx])}
                count += compare_copy(rows, OUT / ('fixed-' + key + '.native.jsonl.gz'), env, count)
                bridge_line = count - 1
                env = {k: checker.serialize(v) for k, v in zip(['G', 'A', 'B', 'D'], [g, fs[idx], es[idx], z])}
                count += compare_copy(rows, OUT / 'fixed-guard-compose.native.jsonl.gz', env, count)
                first = next(rows); last = next(rows)
                assert first == {'f': checker.serialize(I(E(fs[idx], es[idx]), I(g, E(es[idx], z)))),
                                 'rule': 'mp', 'refs': [imp['lines'] - 1, count - 1]}
                assert last == {'f': checker.serialize(I(g, E(es[idx], z))), 'rule': 'mp', 'refs': [bridge_line, count]}
                assert next(rows, None) is None and count + 2 == result['formats']['native']['measurement']['lines']
                result['complete_copy_records'] = count
                cert['growing'].append(result); save()
            for mode in ('native', 'not-or'):
                entries = [r['formats'][mode] for r in cert['growing'] if r['case'] == case['name']]
                total = {kind + '_' + unit: sum(r['measurement' if kind == 'actual' else 'bounds'][unit] for r in entries)
                         for kind in ('actual', 'required') for unit in ('lines', 'bytes')}
                assert total == case['whole_list'][mode]
            print('PASS full case', case['name'], len(es), 'imports/copies and both formats', flush=True)
        assert not fixed_paths & growing_paths and len(fixed_paths) == 48 and len(growing_paths) == 56
        for bad in old['rejections']:
            try:
                if 'path' not in bad:
                    assert bad['name'] == 'wrong-guard-endpoint'
                    data = json.loads((OUT / 'mixed-repeated-positions-request.json').read_text())
                    path = HERE.parent / 'original-axiom-guards/output/mixed-repeated-positions-a1.native.jsonl.gz'
                    checker.check(path, ep.f.goals(data['factored'])[1])
                elif bad['path'].endswith('.gz'): checker.check(ROOT / bad['path'])
                else: ep.request(json.loads((ROOT / bad['path']).read_text()))
            except checker.Invalid as err: cert['rejections'].append({'name': bad['name'], 'reason': str(err)})
            else: raise AssertionError('malformed input accepted: ' + bad['name'])
        assert len(cert['rejections']) == 15 and old_path.read_bytes() == raw
        cert['complete'] = True; save()
        print('PASS 104 new full streams + 28 imports; 52 image pairs; all copy records; 15 rejections', flush=True)
        for mode in ('native', 'not-or'):
            totals = {kind + '_' + unit: sum(r['formats'][mode]['measurement' if kind == 'actual' else 'bounds'][unit]
                       for r in cert['growing']) for kind in ('actual', 'required') for unit in ('lines', 'bytes')}
            print(mode, totals, flush=True)
        print('failures:', cert['failures'], '; full certificate:', dest, flush=True)
    except Exception as err:
        cert['failures'].append(repr(err)); save(); raise

if __name__ == '__main__': main()
