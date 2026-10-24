"""Bounded step-449 reproduction of L108 on the preserved exercise only."""
import hashlib
import importlib.util
import json
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
OUT = Path(__file__).with_name('output-449')
CAPS = dict(records=2_000_000, certificate_bytes=200_000_000,
            polynomial_words=1_000_000, word_length=256,
            multiplication_pairs=100_000_000, stored_words=20_000_000)
SOURCE = BASE / 'parity-four-rule/output-goal-directed-447/checker-exercise.jsonl'
SHA = '9265d9b95dac5d2c1dcb549722b412454380b21b11d7d116e93cde479b558d7c'


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


b = module('boolean_component', BASE / 'affine-abp-boolean/check_suffix_graph.py')
c = module('literal_checker', BASE / 'parity-four-rule/checker.py')
m = b.marked
CONSTRUCTION = {'max_intermediate_records': 0, 'commutator_calls': 0}


def bound(n, stage):
    CONSTRUCTION['max_intermediate_records'] = max(CONSTRUCTION['max_intermediate_records'], n)
    if n > CAPS['records']:
        raise RuntimeError(dict(stage=stage, actual=n, cap=CAPS['records']))


raw_witness = m.witness


def checked_witness(f, g, **kw):
    # Exact retained-copy count from L035, before invoking its copy loops.
    p = len(f['edges']) * len(g['edges'])
    q = sum(x != '1' and y != '1' and x != y
            for _, _, el in f['edges'] for _, _, dl in g['edges']
            for x in el for y in dl)
    nv = 2 + 2*p*(f['vertices'] + g['vertices'])
    ne = 2*p*(len(f['edges']) + len(g['edges'])) + 4*p + q
    bound(nv + ne, 'L035 preflight')
    CONSTRUCTION['commutator_calls'] += 1
    out, central = raw_witness(f, g, **kw)
    if out['vertices'] != nv or len(out['edges']) != ne or central != q:
        raise RuntimeError('L035 exact copy count')
    return out, central


m.witness = checked_witness
raw_copy = b.copy_into


def checked_copy(out, g):
    bound(out['vertices'] + len(out['edges']) + g['vertices'] + len(g['edges']) + 8,
          'serial/Boolean copy preflight including connectors')
    return raw_copy(out, g)


b.copy_into = checked_copy


def translation(t):
    if isinstance(t, str):
        return m.graph(2, [] if t == 'true' else [(0, 1, ['1' if t == 'false' else
                                                            'x' + str(['A', 'B'].index(t) + 1)])])
    if t[0] == 'or':
        return b.product([translation(t[1]), translation(t[2])])
    h = translation(t[1])
    out = m.graph(2, [(0, 1, ['1'])], sink=1)
    s, e = b.copy_into(out, h)
    out['edges'].extend([[0, s, ['1']], [e, 1, ['1']]])
    return out


def main():
    raw = SOURCE.read_bytes()
    if hashlib.sha256(raw).hexdigest() != SHA:
        raise RuntimeError('preserved source changed')
    header, *records = [json.loads(line) for line in raw.splitlines()]
    checked = c.check(SOURCE, header['goal'])
    fs = [r['f'] for r in records]
    dictionary = dict(alphabet=header['alphabet'], placeholders=[
        dict(name='sigma:A', kind='boolean', originals=['A'], polynomial=[['A','A'],['A']]),
        dict(name='sigma:B', kind='boolean', originals=['B'], polynomial=[['B','B'],['B']]),
        dict(name='tau:A:B', kind='commutator', originals=['A','B'],
             polynomial=[['A','B'],['B','A']])])
    transport = {'1':'1', 'x1':'A', 'x2':'B', 'b:1':'sigma:A',
                 'b:2':'sigma:B', 't:1:2':'tau:A:B'}
    out = m.graph(1 + len(records), [], sink=len(records))
    blocks = []

    def attach(i, role, kind, args, g, parent=None):
        bound(out['vertices'] + len(out['edges']) + g['vertices'] + len(g['edges']) + 2,
              'outer graph preflight')
        lo, first = out['vertices'], len(out['edges'])
        start, end = b.copy_into(out, g)
        for edge in out['edges'][first:]:
            edge[2][:] = [transport[a] for a in edge[2]]
        origin = 0 if parent is None else parent + 1
        out['edges'].extend([[origin, start, ['1']], [end, i + 1, ['1']]])
        blocks.append(dict(line=i, role=role, kind=kind, arguments=args, parent=parent,
                           vertex_range=[lo, out['vertices']], edge_range=[first, len(out['edges'])],
                           entry=start, exit=end))

    for i, r in enumerate(records):
        tag, f, refs = r['rule'], r['f'], r['refs']
        if tag in ('true', 'not-false'):
            seed, kind, args = m.graph(2, []), 'zero', []
        elif tag in ('axiom', 'contraction'):
            a = f[2] if tag == 'axiom' else f
            seed, _, _ = b.construct(translation(a))
            kind, args = 'boolean', [a]
        elif tag == 'expansion':
            a, bb = fs[refs[0]], f[1]
            seed, _ = m.witness(translation(a), translation(bb))
            kind, args = 'commutator', [a, bb]
        elif tag == 'association':
            seed, kind, args = m.graph(2, []), 'zero', []
        elif tag == 'cut':
            a, bb, cc = fs[refs[0]][1], fs[refs[0]][2], fs[refs[1]][2]
            w, _ = m.witness(translation(bb), translation(cc))
            seed = b.product([translation(['not', a]), w])
            kind, args = 'prefixed-commutator', [a, bb, cc]
        else:
            raise RuntimeError('unreceived rule')
        attach(i, 'seed', kind, args, seed)
        factors = ([f[1]] if tag == 'expansion' else
                   ['false'] if tag in ('contraction', 'association') else
                   [fs[refs[1]][2], fs[refs[0]][2]] if tag == 'cut' else [])
        for j, factor in zip(refs, factors):
            attach(i, 'transition', 'translation', [factor], translation(factor), j)
    cert = dict(format='L108-finite-exercise-v1', caps=CAPS, source_sha256=SHA,
                source_text=raw.decode(), source_check=checked, dictionary=dictionary,
                name_transport=transport, graph=out, line_roots=list(range(1, 10)),
                blocks=blocks, construction=CONSTRUCTION)
    encoded = json.dumps(cert, separators=(',', ':')).encode() + b'\n'
    if len(encoded) > CAPS['certificate_bytes']:
        raise RuntimeError(dict(stage='serialization', actual=len(encoded), cap=CAPS['certificate_bytes']))
    OUT.mkdir(exist_ok=True)
    (OUT / 'source.jsonl').write_bytes(raw)
    (OUT / 'certificate.json').write_bytes(encoded)
    print(json.dumps(dict(vertices=out['vertices'], edges=len(out['edges']), roots=9,
                          bytes=len(encoded), caps=CAPS, construction=CONSTRUCTION)))
    print('Certificate:', OUT / 'certificate.json')


if __name__ == '__main__':
    try:
        main()
    except Exception as err:
        OUT.mkdir(exist_ok=True)
        (OUT / 'construction-failure.json').write_text(json.dumps(
            dict(failure=repr(err), caps=CAPS, construction=CONSTRUCTION), indent=2)+'\n')
        raise
