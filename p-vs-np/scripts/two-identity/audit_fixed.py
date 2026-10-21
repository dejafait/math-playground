"""Step 251: read-only replay of L069's six fixed pairs, not a receiver run."""
import gzip
import importlib.util
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'scripts/two-identity/output'
CERT = OUT / 'audit-251.json'
spec = importlib.util.spec_from_file_location(
    'primitive_checker', ROOT / 'scripts/balanced-slot/checker.py')
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


def goals():
    # Literal definitions from L069; no emitter or build_fixed import.
    def n(u): return '(~' + u + ')'
    def i(u, v): return '(' + u + '>' + v + ')'
    def x(u, v): return i(i(u, v), n(i(v, u)))
    def e(u, v): return n(x(u, v))
    def p(u, v): return n(i(u, n(v)))
    a, b, c, g = 'A', 'B', 'C', 'G'
    y = i('q', 'q')
    z = n(y)
    return {
        'product-assoc': e(p(p(a, b), c), p(a, p(b, c))),
        'guarded-trans': i(i(g, e(a, b)), i(i(g, e(b, c)), i(g, e(a, c)))),
        'zero-not': i(e(a, z), n(a)),
        'plus-one-positive': i(e(x(a, y), z), a),
        'final-reception': i(a, i(i(g, e(a, b)), i(n(b), n(g)))),
        'empty-reception': i(i(g, z), n(g)),
    }


def image(text):
    def walk(t):
        if isinstance(t, str): return t
        if t[0] == 'not': return '(~' + walk(t[1]) + ')'
        assert t[0] == 'imp'
        return '((~' + walk(t[1]) + ')|' + walk(t[2]) + ')'
    return walk(checker.parse(text, 'native')[0])


def unique(pairs):
    result = {}
    for key, value in pairs:
        if key in result: raise ValueError('duplicate JSON field: ' + key)
        result[key] = value
    return result


def compare(native, translated):
    count = 0
    with gzip.open(native, 'rt') as ns, gzip.open(translated, 'rt') as ims:
        for index, (nr, ir) in enumerate(itertools.zip_longest(ns, ims)):
            assert nr is not None and ir is not None, 'unequal stream lengths'
            n = json.loads(nr, object_pairs_hook=unique)
            im = json.loads(ir, object_pairs_hook=unique)
            if index == 0:
                assert set(n) == {'format', 'goal'} and n['format'] == 'native'
                assert n['goal'].isascii()
                want = {'format': 'not-or', 'goal': image(n['goal'])}
            else:
                assert n['f'].isascii()
                want = dict(n, f=image(n['f']))
                if 'subs' in n:
                    assert all(v.isascii() for v in n['subs'].values())
                    want['subs'] = {k: image(v) for k, v in n['subs'].items()}
                count += 1
            assert im == want, ('literal image mismatch', index)
    return count


def main():
    required = {'L': 2033, 'native': {'D': 18, 'S': 1104},
                'not-or': {'D': 25, 'S': 1490}}
    cert = {'complete': False, 'scope': 'six fixed pairs only; no joined receiver',
            'required': required, 'library': {}, 'failures': []}
    def save(): CERT.write_text(json.dumps(cert, indent=2) + '\n')
    save()
    try:
        for name, goal in goals().items():
            metrics = {}
            paths = {mode: OUT / ('fixed-' + name + '.' + mode + '.jsonl.gz')
                     for mode in ['native', 'not-or']}
            for mode, path in paths.items():
                endpoint = goal if mode == 'native' else image(goal)
                m = checker.check(path, endpoint)
                m['path'] = str(path.relative_to(ROOT))
                assert m['lines'] <= required['L']
                assert m['max_line_depth'] <= required[mode]['D']
                assert m['max_record_nodes'] <= required[mode]['S']
                metrics[mode] = m
            compared = compare(paths['native'], paths['not-or'])
            assert compared == metrics['native']['lines'] == metrics['not-or']['lines']
            cert['library'][name] = {'endpoint': goal, 'formats': metrics,
                                     'complete_compared_records': compared}
            save()
            print(name, 'PASS', 'lines actual/required', compared, required['L'],
                  'depths', [metrics[m]['max_line_depth'] for m in paths],
                  'required', [required[m]['D'] for m in paths],
                  'record nodes', [metrics[m]['max_record_nodes'] for m in paths],
                  'required', [required[m]['S'] for m in paths], flush=True)
        cert['complete'] = True
        save()
        print('PASS failures=[]; certificate', CERT.relative_to(ROOT), flush=True)
    except Exception as error:
        cert['failures'].append(repr(error))
        save()
        raise


if __name__ == '__main__':
    main()
