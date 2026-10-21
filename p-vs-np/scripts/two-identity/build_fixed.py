"""Step 249: fixed primitive receiving laws, not a whole IPS receiver."""
import gzip
import itertools
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(HERE.parent / 'balanced-coordinate'))
import aggregate

p, checker = aggregate.primitive, aggregate.checker
OUT = HERE / 'output'
CERT = OUT / 'certificate-249.json'


def schemas():
    a, b, c, g = 'A', 'B', 'C', 'G'
    y = p.I('q', 'q')
    z = p.N(y)
    def product(u, v): return p.N(p.I(u, p.N(v)))
    return {
        'product-assoc': p.E(product(product(a, b), c), product(a, product(b, c))),
        'guarded-trans': p.I(p.I(g, p.E(a, b)), p.I(p.I(g, p.E(b, c)), p.I(g, p.E(a, c)))),
        'zero-not': p.I(p.E(a, z), p.N(a)),
        'plus-one-positive': p.I(p.E(p.X(a, y), z), a),
        'final-reception': p.I(a, p.I(p.I(g, p.E(a, b)), p.I(p.N(b), p.N(g)))),
        'empty-reception': p.I(p.I(g, z), p.N(g)),
    }


def expected():
    # Independent literal endpoint construction; no emitter expressions used.
    def n(a): return '(~' + a + ')'
    def i(a, b): return '(' + a + '>' + b + ')'
    def x(a, b): return i(i(a, b), n(i(b, a)))
    def e(a, b): return n(x(a, b))
    def mul(a, b): return n(i(a, n(b)))
    a, b, c, g = 'A', 'B', 'C', 'G'
    y, z = i('q', 'q'), n(i('q', 'q'))
    return {
        'product-assoc': e(mul(mul(a, b), c), mul(a, mul(b, c))),
        'guarded-trans': i(i(g, e(a, b)), i(i(g, e(b, c)), i(g, e(a, c)))),
        'zero-not': i(e(a, z), n(a)),
        'plus-one-positive': i(e(x(a, y), z), a),
        'final-reception': i(a, i(i(g, e(a, b)), i(n(b), n(g)))),
        'empty-reception': i(i(g, z), n(g)),
    }


def translate(text):
    tree = checker.parse(text, 'native')[0]
    return checker.serialize(aggregate.endpoints.image(tree))


def compare_images(native, image):
    with gzip.open(native, 'rt') as ns, gzip.open(image, 'rt') as ims:
        nh, ih = json.loads(next(ns)), json.loads(next(ims))
        assert ih == {'format': 'not-or', 'goal': translate(nh['goal'])}
        for nr, ir in itertools.zip_longest(ns, ims):
            assert nr is not None and ir is not None
            n, im = json.loads(nr), json.loads(ir)
            want = dict(n, f=translate(n['f']))
            if 'subs' in n:
                want['subs'] = {k: translate(v) for k, v in n['subs'].items()}
            assert im == want


def main():
    OUT.mkdir(exist_ok=True)
    cert = {'complete': False, 'scope': 'six fixed laws only; no whole receiver',
            'library': {}, 'failures': []}
    def save(): CERT.write_text(json.dumps(cert, indent=2) + '\n')
    save()
    try:
        goals = expected()
        for name, goal in schemas().items():
            assert p.text(goal) == goals[name]
            obj = p.Proof()
            obj.build_helpers()
            root = obj.prove_fixed(goal)
            paths, metrics = {}, {}
            for image, mode in [(False, 'native'), (True, 'not-or')]:
                path = OUT / ('fixed-' + name + '.' + mode + '.jsonl.gz')
                obj.write(root, path, image)
                endpoint = translate(goals[name]) if image else goals[name]
                metrics[mode] = checker.check(path, endpoint)
                paths[mode] = path
            compare_images(paths['native'], paths['not-or'])
            cert['library'][name] = {'endpoint': goals[name], 'formats': metrics,
                'paths': {k: str(v.relative_to(ROOT)) for k, v in paths.items()},
                'complete_literal_image_comparison': True}
            save()
            print(name, 'PASS complete native/image; lines', metrics['native']['lines'],
                  'bytes', metrics['native']['bytes'], metrics['not-or']['bytes'], flush=True)
        cert['constants'] = {
            'L': max(v['formats']['native']['lines'] for v in cert['library'].values()),
            **{mode: {
                'D': max(v['formats'][mode]['max_line_depth'] for v in cert['library'].values()),
                'S': max(v['formats'][mode]['max_record_nodes'] for v in cert['library'].values())
            } for mode in ['native', 'not-or']}}
        # The measured constants are the fixed-library bounds, checked for every record.
        for value in cert['library'].values():
            for mode, m in value['formats'].items():
                b = cert['constants']
                assert m['lines'] <= b['L']
                assert m['max_line_depth'] <= b[mode]['D']
                assert m['max_record_nodes'] <= b[mode]['S']
        cert['complete'] = True
        save()
        print('PASS required fixed-library maxima', cert['constants'],
              'failures', cert['failures'], 'certificate', CERT, flush=True)
    except Exception as error:
        cert['failures'].append(repr(error))
        save()
        raise


if __name__ == '__main__':
    main()
