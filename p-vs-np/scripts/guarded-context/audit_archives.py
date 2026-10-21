"""Step 182: recover overwritten fixed archives; independently audit all records.

The original certificate and all original streams are read-only. Reconstruction
uses only checker syntax and context_endpoints, never the proof emitter. Import
lift only for the final malformed-input reception checks.
"""
import gzip
import itertools
import json
from pathlib import Path
import context_endpoints as e

checker = e.checker
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
OUT = HERE / 'output'
REPORT = OUT / 'audit-182.json'
result = {'complete': False, 'failures': [], 'findings': [], 'library': {},
          'cases': [], 'corruptions': []}


def save():
    REPORT.write_text(json.dumps(result, indent=2) + '\n')


def require(ok, message):
    if not ok:
        raise AssertionError(message)


def unique(pairs):
    out = {}
    for key, value in pairs:
        require(key not in out, 'duplicate JSON key')
        out[key] = value
    return out


def records(path):
    with gzip.open(path, 'rt', encoding='ascii') as stream:
        for raw in stream:
            yield json.loads(raw, object_pairs_hook=unique)


def read(path):
    it = records(path)
    return next(it), list(it)


def tree(s):
    return e.validate_term(s)


def text(t):
    return checker.serialize(t)


def subst(t, env):
    if isinstance(t, str):
        return env.get(t, t)
    return (t[0], *(subst(a, env) for a in t[1:]))


def image_row(row):
    out = dict(row, f=text(e.image(tree(row['f']))))
    if 'subs' in row:
        out['subs'] = {k: text(e.image(tree(v))) for k, v in row['subs'].items()}
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


def compare_measurement(actual, saved, relocated=False):
    for key, value in actual.items():
        if relocated and key == 'path':
            continue
        require(saved[key] == value, 'saved measurement differs: ' + key)


class Reconstruction:
    def __init__(self):
        self.rows = []

    def copy(self, source, env):
        start = len(self.rows)
        for k, row in enumerate(source):
            out = {'f': text(subst(tree(row['f']), env)), 'rule': row['rule']}
            if row['rule'] == 'mp':
                require(all(type(r) is int and 0 <= r < k for r in row['refs']), 'source refs')
                out['refs'] = [start + r for r in row['refs']]
            else:
                out['subs'] = {a: text(subst(tree(t), env)) for a, t in row['subs'].items()}
            self.rows.append(out)
        return len(self.rows) - 1

    def ax(self, rule, **env):
        # Independent primitive schemas, not compiler.Proof.ax.
        a, b = env['A'], env['B']
        if rule == 'ax1':
            f = e.im(a, e.im(b, a))
        elif rule == 'ax2':
            c = env['C']
            f = e.im(e.im(a, e.im(b, c)), e.im(e.im(a, b), e.im(a, c)))
        else:
            raise AssertionError('unexpected guarding axiom')
        self.rows.append({'f': text(f), 'rule': rule, 'subs': {k: text(v) for k, v in env.items()}})
        return len(self.rows) - 1

    def mp(self, a, b):
        conditional = tree(self.rows[b]['f'])
        require(isinstance(conditional, tuple) and conditional[0] == 'imp', 'MP shape')
        require(tree(self.rows[a]['f']) == conditional[1], 'MP antecedent')
        self.rows.append({'f': text(conditional[2]), 'rule': 'mp', 'refs': [a, b]})
        return len(self.rows) - 1


def write_fixed(path, goal, rows, mode):
    header = {'format': mode, 'goal': text(goal if mode == 'native' else e.image(goal))}
    expected = [header] + [r if mode == 'native' else image_row(r) for r in rows]
    # Never silently replace a prior recovery artifact with different content.
    if path.exists():
        require(list(records(path)) == expected, 'existing recovery differs')
        return
    with gzip.open(path, 'wt', encoding='ascii', compresslevel=6) as stream:
        for row in expected:
            stream.write(json.dumps(row, separators=(',', ':')) + '\n')


def reconstruct(case, source, library):
    o = Reconstruction()
    imported = o.copy(source, {})
    events = []
    guard = tree(case['guard'])

    def go(node):
        if node == {'mark': True}:
            return tree(case['U']), tree(case['V']), imported
        # Count marks independently at this cut, rather than trusting event data.
        left_marks = e.inspect(node['left'])[2]
        side = 'left' if left_marks else 'right'
        other = 'right' if left_marks else 'left'
        require(e.inspect(node[other])[2] == 0, 'marked sibling')
        a, b, prior = go(node[side])
        sibling = e.fill(node[other], 'UNUSED')
        name = node['op'] + '-' + side
        env = {'A': a, 'B': b, 'C': sibling, 'G': guard}
        law = o.copy(library[name], env)
        root = o.mp(prior, law)
        op = e.xx if node['op'] == 'xor' else e.aa
        u, v = (op(a, sibling), op(b, sibling)) if side == 'left' else (op(sibling, a), op(sibling, b))
        require(o.rows[root]['f'] == text(e.im(guard, e.ee(u, v))), 'ancestor endpoint')
        events.append({'template': name, 'prior': prior, 'law': law, 'root': root,
                       'arguments': {k: text(t) for k, t in env.items()}})
        return u, v, root

    _, _, root = go(case['context'])
    require(root == len(o.rows) - 1, 'last record')
    require(o.rows[root]['f'] == e.goal(case['guard'], case['U'], case['V'], case['context']), 'goal')
    require(events == case['events'], 'complete events/references/arguments')
    require(o.rows[:len(source)] == source, 'all unused/supplied records retained')
    return o.rows, events


def main():
    save()
    old = json.loads((OUT / 'certificate-180.json').read_text())
    require(old['complete'] and not old['failures'], 'old report incomplete')
    library = {}
    for op, side in itertools.product(['xor', 'and'], ['left', 'right']):
        name = op + '-' + side
        fn = e.xx if op == 'xor' else e.aa
        a, b, c, g = 'A', 'B', 'C', 'G'
        u, v = (fn(a, c), fn(b, c)) if side == 'left' else (fn(c, a), fn(c, b))
        h, k = e.ee(a, b), e.ee(u, v)
        law = e.im(h, k)
        base = (HERE.parent / 'balanced-slot' / 'output' / ('cong' + ('L' if side == 'left' else 'R') + '.native.jsonl.gz')
                if op == 'xor' else OUT / (name + '-unguarded.native.jsonl.gz'))
        base_check = checker.check(base, text(law))
        if op == 'and':
            compare_measurement(base_check, old['unguarded'][name])
        header, source = read(base)
        require(header == {'format': 'native', 'goal': text(law)}, 'unguarded header')
        o = Reconstruction()
        root = o.copy(source, {})
        first = o.mp(root, o.ax('ax1', A=law, B=g))
        o.mp(first, o.ax('ax2', A=g, B=h, C=k))
        goal = e.im(e.im(g, h), e.im(g, k))
        require(o.rows[-1]['f'] == text(goal), 'fixed endpoint')
        library[name] = o.rows
        for mode in ['native', 'not-or']:
            previous = old['library'][name + '-' + mode]
            overwritten = ROOT / previous['path']
            current = checker.check(overwritten)
            growing = next(c for c in old['cases'] if c['name'] == name)['proofs'][mode]['measurement']
            compare_measurement(current, growing)
            require(current['sha256'] != previous['sha256'], 'expected archive collision missing')
            path = OUT / ('fixed-' + name + '.' + mode + '.jsonl.gz')
            write_fixed(path, goal, o.rows, mode)
            expected = text(goal if mode == 'native' else e.image(goal))
            measured = checker.check(path, expected)
            compare_measurement(measured, previous, relocated=True)
            result['library'][name + '-' + mode] = measured
            result['findings'].append({'kind': 'overwritten-fixed-archive-recovered',
                'old_path': previous['path'], 'current_sha256': current['sha256'],
                'recovered_path': measured['path'], 'recovered_sha256': measured['sha256'],
                'exact_original_uncompressed_bytes_recovered': True})
        save()
        print('fixed', name, 'lines', len(o.rows), 'both formats recovered; original hashes match', flush=True)

    constants = {mode: {'D': max(result['library'][n+'-'+mode]['max_line_depth'] for n in library),
                        'S': max(result['library'][n+'-'+mode]['max_record_nodes'] for n in library),
                        'c': 3 if mode == 'native' else 6} for mode in ['native', 'not-or']}
    L = max(len(rows) for rows in library.values())
    result['constants'] = {'L': L, **constants}
    require(result['constants'] == old['constants'], 'library constants')

    for case in old['cases']:
        path = ROOT / case['input']['path']
        expected = e.coordinate(case['guard'], case['U'], case['V'])
        measurement = checker.check(path, expected)
        compare_measurement(measurement, case['input'])
        header, source = read(path)
        require(header == {'format': 'native', 'goal': expected}, 'input header')
        stats = {mode: fields_stats(source, mode) for mode in constants}
        for mode, (nodes, depth, _) in stats.items():
            require(nodes == case['input']['node_sums'][mode] and depth == case['input']['depths'][mode], 'input stats')
        s, h, terms = e.request(case['guard'], case['U'], case['V'], case['context'])
        rows, events = reconstruct(case, source, library)
        k, N = len(events), len(source)
        R, J = k * (L + 1), N + k * (L + 1)
        require((s, h, k, N, R, J) == tuple(case[x] for x in ['s', 'h', 'k', 'N', 'R', 'J']), 'case parameters')
        require(k <= h <= s.bit_length(), 'height promise a=1')
        require(len(rows) == N + sum(len(library[event['template']]) + 1 for event in events), 'exact lines')
        audited = {'name': case['name'], 'input': measurement, 'all_records_reconstructed': True,
                   'events': events, 'proofs': {}}
        for mode, con in constants.items():
            proof = case['proofs'][mode]
            path = ROOT / proof['measurement']['path']
            expected = e.goal(case['guard'], case['U'], case['V'], case['context'], mode)
            measured = checker.check(path, expected)
            compare_measurement(measured, proof['measurement'])
            stream = records(path)
            require(next(stream) == {'format': mode, 'goal': expected}, 'output header')
            for i, (want, got) in enumerate(itertools.zip_longest(rows, stream)):
                require(want is not None and got is not None, 'output length')
                if mode == 'not-or':
                    want = image_row(want)
                require(want == got, 'complete record mismatch ' + str(i))
            def fmt(t):
                return t if mode == 'native' else e.image(t)
            sizes = [e.stats(fmt(tree(t))) for t in [case['U'], case['V']] + terms]
            t, d = max(x[0] for x in sizes), max(x[1] for x in sizes)
            gn, gd, gb = e.stats(fmt(tree(case['guard'])))
            K, delta, payload = stats[mode]
            B = max([payload, gb] + [x[2] for x in sizes])
            P = max(gn, 8 * 4**(h+1) * (t+1))
            F = 256 + 64 * (J+1).bit_length()
            bounds = {'lines': J, 'depth': max(delta, con['D'] + max(gd, con['c']*h+d)),
                'record_nodes': max(K, con['S']*P),
                'bytes': (B+4)*(K+(R+1)*con['S']*P)+(J+2)*F}
            bounds['bits'] = 8*bounds['bytes']
            params = dict(t=t, d=d, guard_nodes=gn, guard_depth=gd, B=B, K=K, delta=delta, P=P)
            require(params == proof['parameters'] and bounds == proof['bounds'], 'canonical parameters/bounds')
            for label, field in [('lines', 'lines'), ('depth', 'max_line_depth'),
                                  ('record_nodes', 'max_record_nodes'), ('bytes', 'bytes')]:
                require(measured[field] <= bounds[label], 'failed bound ' + label)
            args = [e.stats(fmt(tree(v))) for event in events for key, v in event['arguments'].items() if key != 'G']
            argmax = {'nodes': max([t] + [x[0] for x in args]), 'depth': max([d] + [x[1] for x in args])}
            require(argmax == proof['context_arguments'], 'actual context arguments')
            require(argmax['nodes'] <= P and argmax['depth'] <= con['c']*h+d, 'argument bounds')
            require(all(event['arguments']['G'] == case['guard'] for event in events), 'separate exact guard')
            audited['proofs'][mode] = {'measurement': measured, 'parameters': params,
                'bounds': bounds, 'arguments': argmax, 'complete_record_match': True}
            print(case['name'], mode, 'lines', measured['lines'], '/', J,
                  'depth', measured['max_line_depth'], '/', bounds['depth'],
                  'bytes', measured['bytes'], '/', bounds['bytes'], flush=True)
        result['cases'].append(audited)
        save()

    # Only reception rejection uses the actual emitter/importer.
    import lift
    good = old['cases'][0]
    path = ROOT / good['input']['path']
    head, rows = read(path)
    for corruption in old['corruptions']:
        label = corruption['name']
        g, context, requested = good['guard'], good['context'], path
        differences = []
        if 'path' in corruption:
            requested = ROOT / corruption['path']
            bh, br = read(requested)
            if bh != head:
                differences.append({'header': {key: [head.get(key), bh.get(key)]
                    for key in set(head) | set(bh) if head.get(key) != bh.get(key)}})
            require(len(br) == len(rows), 'corruption length')
            for i, (a, b) in enumerate(zip(rows, br)):
                if a != b:
                    differences.append({'line': i, 'fields': [key for key in set(a) | set(b) if a.get(key) != b.get(key)]})
            require(len(differences) == 1, 'one changed record/header')
        elif label == 'changed-guard':
            g = 'CHANGED'
        elif label == 'missing-proof':
            requested = None
        elif label == 'missing-mark':
            context = {'term': 'A'}
        elif label == 'two-marks':
            context = {'op': 'xor', 'left': {'mark': True}, 'right': {'mark': True}}
        else:
            raise AssertionError('unexpected malformed request')
        try:
            lift.Lift(g, good['U'], good['V'], context, requested, {})
        except (checker.Invalid, ValueError) as err:
            require(str(err) == corruption['reason'], 'rejection reason differs')
            result['corruptions'].append({'name': label, 'rejected': True, 'reason': str(err), 'differences': differences})
        else:
            raise AssertionError('malformed input accepted')
        save()
    result['complete'] = True
    save()
    print('10 malformed receptions rejected; 8 archive collisions recovered; failures', len(result['failures']),
          'certificate', REPORT.relative_to(ROOT), flush=True)


if __name__ == '__main__':
    try:
        main()
    except Exception as err:
        result['failures'].append(repr(err))
        save()
        raise
