"""Step 178: complete archive audit; reconstruct without the proof emitter.

Only the final malformed-reception tests import aggregate. Existing archives,
checker, templates and certificate-176 are read-only inputs.
"""
import gzip
import itertools
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE.parent / 'balanced-slot'))
import checker
import endpoints as e

OUT = HERE / 'output' / 'audit-178.json'
result = {'complete': False, 'failures': [], 'library': {}, 'cases': [], 'corruptions': []}


def save():
    OUT.write_text(json.dumps(result, indent=2) + '\n')


def require(ok, message):
    if not ok:
        raise AssertionError(message)


def unique(pairs):
    out = {}
    for k, v in pairs:
        require(k not in out, 'duplicate JSON key')
        out[k] = v
    return out


def records(path):
    with gzip.open(path, 'rt', encoding='ascii') as stream:
        for line in stream:
            yield json.loads(line, object_pairs_hook=unique)


def read(path):
    it = records(path)
    return next(it), list(it)


def tree(s):
    return checker.parse(s, 'native')[0]


def subst(t, env):
    if isinstance(t, str):
        return env.get(t, t)  # simultaneous, never resubstitute the replacement
    return (t[0], *(subst(a, env) for a in t[1:]))


def image_row(row):
    out = dict(row, f=checker.serialize(e.image(tree(row['f']))))
    if 'subs' in row:
        out['subs'] = {k: checker.serialize(e.image(tree(v))) for k, v in row['subs'].items()}
    return out


def fields_stats(rows, mode):
    total, depth, payload = 0, 0, 1
    for row in rows:
        for s in [row['f'], *row.get('subs', {}).values()]:
            t = tree(s)
            if mode == 'not-or':
                t = e.image(t)
            n, d, b = e.stats(t)
            total += n
            depth = max(depth, d)
            payload = max(payload, b)
    return total, depth, payload


def compare_measurement(actual, saved):
    for key, value in actual.items():
        require(saved[key] == value, 'saved measurement differs: ' + key)


def reconstruct(case, packages, library):
    """Explicitly reconstruct all native records and provenance, without aggregate."""
    rows, imports, leaves, events = [], [], [], []

    def copy(source, env):
        start = len(rows)
        for k, row in enumerate(source):
            out = {'f': checker.serialize(subst(tree(row['f']), env)), 'rule': row['rule']}
            if row['rule'] == 'mp':
                require(all(0 <= r < k for r in row['refs']), 'source reference')
                out['refs'] = [start + r for r in row['refs']]
            else:
                out['subs'] = {a: checker.serialize(subst(tree(t), env)) for a, t in row['subs'].items()}
            rows.append(out)
        return len(rows) - 1

    def mp(a, b):
        conditional = tree(rows[b]['f'])
        require(isinstance(conditional, tuple) and conditional[0] == 'imp', 'reconstructed MP shape')
        require(tree(rows[a]['f']) == conditional[1], 'reconstructed MP antecedent')
        rows.append({'f': checker.serialize(conditional[2]), 'rule': 'mp', 'refs': [a, b]})
        return len(rows) - 1

    for source in packages:
        start = len(rows)
        root = copy(source, {})
        imports.append({'start': start, 'lines': len(source), 'root': root})
        leaves.append(root)

    def go(lo, hi):
        if hi - lo == 1:
            return tree(case['U'][lo]), tree(case['V'][lo]), leaves[lo]
        mid = (lo + hi) // 2
        a, b, left = go(lo, mid)
        c, d, right = go(mid, hi)
        first = mp(left, copy(library['congL'], {'A': a, 'B': b, 'C': c}))
        second = mp(right, copy(library['congR'], {'A': c, 'B': d, 'C': b}))
        u, v, w = e.xor(a, c), e.xor(b, c), e.xor(b, d)
        law = copy(library['trans'], {'A': u, 'B': v, 'C': w})
        root = mp(second, mp(first, law))
        events.append({'range': [lo, hi], 'left': left, 'right': right, 'root': root,
                       'arguments': [checker.serialize(t) for t in [a, b, c, d, u, v, w]]})
        return u, w, root

    _, _, root = go(0, case['M'])
    require(root == len(rows) - 1, 'last record')
    require(rows[root]['f'] == e.goal(case['U'], case['V']), 'final reconstructed endpoint')
    require(imports == case['imports'], 'all import offsets')
    require(events == case['events'], 'complete event sequence and arguments')
    return rows, events


def main():
    save()
    saved = json.loads((HERE / 'output' / 'certificate-176.json').read_text())
    require(saved['complete'] and not saved['failures'], 'prior report incomplete')
    a, b, c = 'A', 'B', 'C'
    laws = {'congL': e.imp(e.equiv(a, b), e.equiv(e.xor(a, c), e.xor(b, c))),
            'congR': e.imp(e.equiv(a, b), e.equiv(e.xor(c, a), e.xor(c, b))),
            'trans': e.imp(e.equiv(a, b), e.imp(e.equiv(b, c), e.equiv(a, c)))}
    library = {}
    constants = {'native': (18, 2456, 3), 'not-or': (25, 3492, 6)}
    for name, goal in laws.items():
        for mode in constants:
            path = HERE.parent / 'balanced-slot' / 'output' / (name + '.' + mode + '.jsonl.gz')
            expected = checker.serialize(goal if mode == 'native' else e.image(goal))
            measured = checker.check(path, expected)
            compare_measurement(measured, saved['library'][name if mode == 'native' else name + '-image'])
            require(measured['lines'] <= 3470 and measured['max_line_depth'] <= constants[mode][0]
                    and measured['max_record_nodes'] <= constants[mode][1], 'fixed-library bounds')
            result['library'][name + '-' + mode] = measured
            if mode == 'native':
                _, library[name] = read(path)
        native_rows = library[name]
        _, image_rows = read(HERE.parent / 'balanced-slot' / 'output' / (name + '.not-or.jsonl.gz'))
        require([image_row(r) for r in native_rows] == image_rows, 'fixed literal image')
    save()
    print('six complete fixed streams checked against independently written endpoints', flush=True)

    for case in saved['cases']:
        packages, input_results = [], []
        for k, rel in enumerate(case['input_paths']):
            expected = e.coordinate(case['U'][k], case['V'][k])
            measurement = checker.check(ROOT / rel, expected)
            compare_measurement(measurement, case['inputs'][k])
            header, rows = read(ROOT / rel)
            require(header == {'format': 'native', 'goal': expected}, 'input header')
            packages.append(rows)
            stats = {mode: fields_stats(rows, mode) for mode in constants}
            for mode, (nodes, depth, payload) in stats.items():
                require(nodes == case['inputs'][k]['node_sums'][mode], 'input node sum')
                require(depth == case['inputs'][k]['depths'][mode], 'input depth')
                require(payload == case['inputs'][k]['name_bytes'], 'input payload')
            input_results.append({'measurement': measurement, 'stats': stats})
        rows, events = reconstruct(case, packages, library)
        n = sum(len(p) for p in packages)
        m, h = len(packages), len(packages).bit_length() - 1
        g = (m - 1) * (3 * 3470 + 4)
        j = n + g
        require((m, h, n, g, j) == tuple(case[k] for k in ['M', 'h', 'N', 'G', 'J']), 'case count parameters')
        require(len(rows) == n + 5775 * (m - 1), 'exact unpruned line count')
        audited = {'name': case['name'], 'inputs': input_results, 'imports': case['imports'],
                   'events_checked': len(events), 'all_records_reconstructed': True, 'proofs': {}}
        for mode, (D, S, c) in constants.items():
            proof = case['proofs'][mode]
            path = ROOT / proof['measurement']['path']
            expected = e.goal(case['U'], case['V'], mode)
            measurement = checker.check(path, expected)
            compare_measurement(measurement, proof['measurement'])
            require(expected == proof['expected_goal'], 'saved goal')
            actual = records(path)
            require(next(actual) == {'format': mode, 'goal': expected}, 'output header')
            for k, (want, got) in enumerate(itertools.zip_longest(rows, actual)):
                require(want is not None and got is not None, 'output length mismatch')
                if mode == 'not-or':
                    want = image_row(want)
                require(want == got, 'complete output record differs: ' + str(k))
            ts = [tree(s) for s in case['U'] + case['V']]
            if mode == 'not-or':
                ts = [e.image(t) for t in ts]
            sizes = [e.stats(t) for t in ts]
            t, d = max(s[0] for s in sizes), max(s[1] for s in sizes)
            K = sum(p['stats'][mode][0] for p in input_results)
            delta = max(p['stats'][mode][1] for p in input_results)
            B = max([1] + [s[2] for s in sizes] + [p['stats'][mode][2] for p in input_results])
            P = 32 * m * m * (t + 1)
            F = 256 + 64 * (j + 1).bit_length()  # exact ceil(log2(j+2))
            bounds = {'lines': j, 'depth': max(delta, D + c * h + d),
                      'record_nodes': max(K, S * P), 'bytes': (B + 4) * (K + (g + 1) * S * P) + (j + 2) * F}
            bounds['bits'] = 8 * bounds['bytes']
            parameters = dict(t=t, d=d, B=B, K=K, delta=delta, P=P)
            require(parameters == proof['parameters'] and bounds == proof['bounds'], 'recomputed bound/parameter')
            for key, field in [('lines', 'lines'), ('depth', 'max_line_depth'),
                               ('record_nodes', 'max_record_nodes'), ('bytes', 'bytes')]:
                require(measurement[field] <= bounds[key], 'bound violated: ' + key)
            arg_stats = [e.stats(tree(s) if mode == 'native' else e.image(tree(s)))
                         for event in events for s in event['arguments']]
            argmax = {'nodes': max(s[0] for s in arg_stats), 'depth': max(s[1] for s in arg_stats)}
            require(argmax == proof['arguments'] and argmax['nodes'] <= P
                    and argmax['depth'] <= c * h + d, 'all argument bounds')
            audited['proofs'][mode] = {'measurement': measurement, 'parameters': parameters,
                                      'bounds': bounds, 'arguments': argmax, 'complete_record_match': True}
            print(case['name'], mode, 'lines', measurement['lines'], '/', j,
                  'depth', measurement['max_line_depth'], '/', bounds['depth'],
                  'bytes', measurement['bytes'], '/', bounds['bytes'], flush=True)
            save()
        result['cases'].append(audited)
        save()

    # Test the actual receiving boundary only after emitter-independent archive work.
    import aggregate
    case = saved['cases'][0]
    us, vs = case['U'], case['V']
    paths = [ROOT / p for p in case['input_paths']]
    good_header, good_rows = read(paths[1])
    for old in saved['corruptions']:
        label = old['case']
        request_v, request_paths = vs, paths
        differences = []
        if 'path' in old:
            bad = ROOT / old['path']
            bh, br = read(bad)
            if bh != good_header:
                differences.append({'header': {k: [good_header.get(k), bh.get(k)]
                                               for k in set(bh) | set(good_header) if bh.get(k) != good_header.get(k)}})
            require(len(br) == len(good_rows), 'corruption line count')
            for k, (x, y) in enumerate(zip(good_rows, br)):
                if x != y:
                    differences.append({'line': k, 'fields': [f for f in set(x) | set(y) if x.get(f) != y.get(f)]})
            require(len(differences) == 1, 'corruption must change one record/header')
            request_paths = [paths[0], bad]
        elif label == 'missing-proof':
            request_paths = paths[:1]
        elif label == 'different-request':
            request_v = ['q'] + vs[1:]
        else:
            raise AssertionError('unknown corruption')
        try:
            aggregate.Combination(us, request_v, request_paths, {})
        except (checker.Invalid, ValueError) as err:
            require(str(err) == old['reason'], 'changed rejection reason')
            result['corruptions'].append({'case': label, 'rejected': True, 'reason': str(err),
                                          'complete_archive_differences': differences})
        else:
            raise AssertionError('corruption accepted: ' + label)
        save()
    result['complete'] = True
    save()
    print('eight reception failures reproduced; complete certificate', OUT.relative_to(ROOT),
          'failures', len(result['failures']), flush=True)


if __name__ == '__main__':
    try:
        main()
    except Exception as err:
        result['failures'].append(repr(err))
        save()
        raise
