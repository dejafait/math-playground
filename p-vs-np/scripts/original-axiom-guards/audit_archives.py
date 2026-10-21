"""Step 186: complete archive audit, no emitter/planner imports or old writes."""
import gzip
import hashlib
import importlib.util
import itertools
import json
import math
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
OUT = HERE / 'output'
sys.path.insert(0, str(HERE.parent / 'balanced-slot'))
import checker
spec = importlib.util.spec_from_file_location('guard_receiver', HERE / 'endpoints.py')
receiver = importlib.util.module_from_spec(spec)
spec.loader.exec_module(receiver)

def N(a): return ('not', a)
def I(a, b): return ('imp', a, b)
def P(a, b): return N(I(a, N(b)))
def X(a, b): return I(I(a, b), N(I(b, a)))
def E(a, b): return N(X(a, b))
def OR(a, b): return I(N(a), b)
def image(t):
    if isinstance(t, str): return t
    if t[0] == 'not': return N(image(t[1]))
    return ('or', N(image(t[1])), image(t[2]))
def fold(xs, shape, op):
    if len(xs) == 1: return xs[0]
    if len(xs) == 2: return op(*xs)
    if shape == 'left': return op(op(xs[0], xs[1]), xs[2])
    return op(xs[0], op(xs[1], xs[2]))
def fixed_goals():
    a, b, c = 'A', 'B', 'C'
    t = I('q', 'q'); z = N(t)
    out = {'id': I(a, a), 'projection-left': I(P(a, b), a),
           'projection-right': I(P(a, b), b),
           'syl': I(I(a, b), I(I(b, c), I(a, c))),
           'boolean': E(X(P(a, a), a), z),
           'commutator': E(X(P(a, b), P(b, a)), z)}
    for arity in (1, 2, 3):
        for signs in itertools.product((False, True), repeat=arity):
            for shape in (('left', 'right') if arity == 3 else ('left',)):
                vs = [a, b, c][:arity]
                lits = [N(v) if neg else v for v, neg in zip(vs, signs)]
                factors = [v if neg else X(t, v) for v, neg in zip(vs, signs)]
                key = 'clause-' + ''.join('n' if neg else 'p' for neg in signs) + '-' + shape
                out[key] = I(fold(lits, shape, OR), E(fold(factors, shape, P), z))
    return out
def independent_request(data):
    t = I(data['q'], data['q']); z = N(t)
    def clause(c):
        if 'var' in c:
            a = c['var']
            return (N(a), a) if c['negative'] else (a, X(t, a))
        a, b = clause(c['left']), clause(c['right'])
        return OR(a[0], b[0]), P(a[1], b[1])
    cs = [clause(c) for c in data['clauses']]
    def guard(tree):
        if type(tree) is int: return cs[tree][0]
        return P(guard(tree['left']), guard(tree['right']))
    g = guard(data['conjunction'])
    vals = [c[1] for c in cs]
    vals += [X(P(a, a), a) for a in data['dictionary']]
    vals += [X(P(a, b), P(b, a)) for a, b in itertools.combinations(data['dictionary'], 2)]
    return g, vals, z
def stats(t):
    if isinstance(t, str): return (1, 0, len(t))
    ch = [stats(a) for a in t[1:]]
    return 1 + sum(a[0] for a in ch), 1 + max(a[1] for a in ch), max(a[2] for a in ch)
def translate_text(s): return checker.serialize(image(checker.parse(s, 'native')[0]))
def compare_images(native, translated):
    count = 0
    with gzip.open(native, 'rt') as ns, gzip.open(translated, 'rt') as ts:
        nh, th = json.loads(next(ns)), json.loads(next(ts))
        assert th == {'format': 'not-or', 'goal': translate_text(nh['goal'])}
        for nr, tr in itertools.zip_longest(ns, ts):
            assert nr is not None and tr is not None
            n, t = json.loads(nr), json.loads(tr)
            expected = dict(n, f=translate_text(n['f']))
            if 'subs' in n: expected['subs'] = {k: translate_text(v) for k, v in n['subs'].items()}
            assert t == expected
            count += 1
    return count

def main():
    old_path = OUT / 'certificate-184.json'
    old_raw = old_path.read_bytes(); old = json.loads(old_raw)
    cert = {'complete': False, 'failures': [], 'fixed': {}, 'growing': [], 'rejections': [],
            'prior_certificate_sha256': hashlib.sha256(old_raw).hexdigest()}
    dest = OUT / 'audit-186.json'
    def save(): dest.write_text(json.dumps(cert, indent=2) + '\n')
    def checked(path, expected, previous):
        measured = checker.check(path, checker.serialize(expected))
        assert measured == previous, ('saved measurement mismatch', str(path))
        return measured
    save()
    try:
        assert old['complete'] and not old['failures']
        assert old['strict_reception_supplement']['complete']
        goals = fixed_goals(); assert set(goals) == set(old['library']) and len(goals) == 28
        fixed_paths, growing_paths = set(), set()
        for name, goal in goals.items():
            result = {}
            for mode, target in [('native', goal), ('not-or', image(goal))]:
                path = OUT / ('fixed-' + name + '.' + mode + '.jsonl.gz')
                fixed_paths.add(path)
                result[mode] = checked(path, target, old['library'][name][mode])
            result['literal_image_records'] = compare_images(
                OUT / ('fixed-' + name + '.native.jsonl.gz'), OUT / ('fixed-' + name + '.not-or.jsonl.gz'))
            cert['fixed'][name] = result; save()
        constants = {'L': max(r['native']['lines'] for r in cert['fixed'].values())}
        for mode in ('native', 'not-or'):
            constants[mode] = {'D': max(r[mode]['max_line_depth'] for r in cert['fixed'].values()),
                               'S': max(r[mode]['max_record_nodes'] for r in cert['fixed'].values())}
        assert constants == old['constants']
        cert['constants'] = constants; save()
        print('PASS all 28 fixed schemas, both complete formats; maxima', constants, flush=True)
        supplements = []
        for case in old['cases']:
            data = json.loads((ROOT / case['request']).read_text())
            received = receiver.request(data)
            g, vals, z = independent_request(data)
            assert received[0] == g and received[2] == vals
            assert len(vals) == case['axiom_count'] == len(case['proofs'])
            m = len(data['clauses']); J0 = constants['L'] + m * (2 * constants['L'] + 2)
            assert (m, J0, len(vals) * J0) == (case['m'], case['J0'], case['total_line_bound'])
            for index, (value, saved) in enumerate(zip(vals, case['proofs'])):
                assert saved['position'] == index + 1
                goal = I(g, E(value, z)); result = {'case': case['name'], 'position': index + 1, 'formats': {}}
                for mode, tr in [('native', lambda t: t), ('not-or', image)]:
                    previous = saved['formats'][mode]
                    path = ROOT / previous['measurement']['path']; growing_paths.add(path)
                    assert path not in fixed_paths
                    measurement = checked(path, tr(goal), previous['measurement'])
                    gs, zs = stats(tr(g)), stats(tr(z)); es = [stats(tr(v)) for v in vals]
                    W = 2 * gs[0] + 2 * max(s[0] for s in es) + 2 * zs[0] + 16
                    d = max(gs[1], max(s[1] for s in es) + 6, zs[1] + 6)
                    B = max(1, gs[2], zs[2], *(s[2] for s in es))
                    S, D = constants[mode]['S'], constants[mode]['D']
                    bounds = {'lines': J0, 'depth': D + d, 'record_nodes': S * W,
                              'bytes': (J0 + 2) * ((B + 4) * S * W + 256 + 64 * math.ceil(math.log2(J0 + 2)))}
                    assert bounds == previous['bounds']
                    assert {'W': W, 'd': d, 'B': B} == previous['parameters']
                    tests = {k: measurement[v] <= bounds[k] for k, v in
                             [('lines', 'lines'), ('depth', 'max_line_depth'),
                              ('record_nodes', 'max_record_nodes'), ('bytes', 'bytes')]}
                    assert tests == previous['tests'] and all(tests.values())
                    result['formats'][mode] = {'measurement': measurement, 'bounds': bounds, 'tests': tests}
                    supplements.append({'position': index + 1, 'case': case['name'], 'format': mode,
                                        'current_exact_endpoint': True, 'records_retained': measurement['lines']})
                result['literal_image_records'] = compare_images(
                    ROOT / result['formats']['native']['measurement']['path'],
                    ROOT / result['formats']['not-or']['measurement']['path'])
                cert['growing'].append(result); save()
            print('PASS complete growing case', case['name'], len(vals), 'guards in both formats', flush=True)
        # Compare every old supplement entry, not its summary flag or a preview.
        key = lambda r: (r['case'], r['format'], r['position'])
        assert sorted(supplements, key=key) == sorted(old['strict_reception_supplement']['endpoint_checks'], key=key)
        assert not fixed_paths & growing_paths and len(fixed_paths) == len(growing_paths) == 56
        cert['strict_reception_reconciled'] = len(supplements)
        for rejected in old['rejections']:
            path = ROOT / rejected['path']
            try:
                if str(path).endswith('.gz'): checker.check(path)
                else: receiver.request(json.loads(path.read_text()))
            except checker.Invalid as err:
                cert['rejections'].append({'path': rejected['path'], 'reason': str(err)})
            else: raise AssertionError('invalid reception passed ' + str(path))
        assert len(cert['rejections']) == 16
        assert old_path.read_bytes() == old_raw
        cert['complete'] = True; save()
        print('PASS 112 full primitive streams; 56 literal-image pairs; 56 strict-reception entries; 16 rejections', flush=True)
        for mode in ('native', 'not-or'):
            worst = max((r['formats'][mode] for r in cert['growing']), key=lambda r: r['measurement']['bytes'])
            print(mode, 'largest actual/required:', {k: [worst['measurement'][v], worst['bounds'][k]]
                  for k, v in [('lines', 'lines'), ('depth', 'max_line_depth'), ('record_nodes', 'max_record_nodes'), ('bytes', 'bytes')]}, flush=True)
        print('failures:', cert['failures'], '; full certificate:', dest, flush=True)
    except Exception as err:
        cert['failures'].append(repr(err)); save(); raise

if __name__ == '__main__': main()
