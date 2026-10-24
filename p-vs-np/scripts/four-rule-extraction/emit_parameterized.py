"""Bounded parameterized reproduction of audited L108; finite diagnostics only."""
import importlib.util
import json
from collections import Counter
from pathlib import Path
from parameterized_input import CAPS, bound as limit, request, symbol_map, write_json, input_bounds
BASE = Path(__file__).resolve().parents[1]
def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


b = module('boolean_component', BASE / 'affine-abp-boolean/check_suffix_graph.py')
m = b.marked
CONSTRUCTION = {'max_intermediate_records': 0, 'commutator_calls': 0}
ALPHABET = []


def bound(n, stage):
    CONSTRUCTION['max_intermediate_records'] = max(CONSTRUCTION['max_intermediate_records'], n)
    limit(n, 'records', stage)


def original_only(g):
    allowed = {'1'} | {'x'+str(i+1) for i in range(len(ALPHABET))}
    if any(type(a) is not str or a not in allowed for _,_,lab in g['edges'] for a in lab):
        raise RuntimeError('non-original correction operand')

raw_witness = m.witness


def checked_witness(f, g, **kw):
    original_only(f)
    original_only(g)
    # Exact retained-copy count from L035, before invoking its copy loops.
    p = len(f['edges']) * len(g['edges'])
    af = Counter(x for _,_,lab in f['edges'] for x in lab if x!='1')
    ag = Counter(x for _,_,lab in g['edges'] for x in lab if x!='1')
    q = sum(af.values())*sum(ag.values())-sum(v*ag[x] for x,v in af.items())
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
                                                            'x' + str(ALPHABET.index(t) + 1)])])
    if t[0] == 'or':
        return b.product([translation(t[1]), translation(t[2])])
    h = translation(t[1])
    out = m.graph(2, [(0, 1, ['1'])], sink=1)
    s, e = b.copy_into(out, h)
    out['edges'].extend([[0, s, ['1']], [e, 1, ['1']]])
    return out


raw_graph = m.graph
def checked_graph(nv, edges, source=0, sink=None):
    bound(nv+len(edges), 'graph allocation preflight')
    return raw_graph(nv, edges, source, sink)
m.graph = b.graph = checked_graph

raw_construct = b.construct
raw_prefixed = b.prefixed

def checked_construct(g):
    original_only(g)
    bound(g['vertices']+len(g['edges'])+1, 'Boolean initial propagation preflight')
    return raw_construct(g)

def checked_prefixed(g, a, v):
    bound(g['vertices']+len(g['edges'])+2, 'prefix list allocation preflight')
    return raw_prefixed(g,a,v)
b.construct = checked_construct
b.prefixed = checked_prefixed

def emit(source_path, request_path, output_path):
    global ALPHABET
    req, raw, records, checked = request(source_path, request_path)
    ALPHABET = req['alphabet']
    CONSTRUCTION.update(max_intermediate_records=0, commutator_calls=0)
    fs = [r['f'] for r in records]
    dictionary = req['dictionary']
    transport = symbol_map(ALPHABET, dictionary)
    out = m.graph(1 + len(records), [], sink=len(records))
    blocks = []

    def attach(i, role, kind, args, g, parent=None):
        bound(out['vertices'] + len(out['edges']) + g['vertices'] + len(g['edges']) + 2,
              'outer graph preflight')
        lo, first = out['vertices'], len(out['edges'])
        start, end = b.copy_into(out, g)
        for edge in out['edges'][first:]:
            edge[2][:] = [list(transport[a]) for a in edge[2]]
        origin = 0 if parent is None else parent + 1
        out['edges'].extend([[origin, start, [['one']]], [end, i + 1, [['one']]]])
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
    cert = dict(format='L108-parameterized-v1', caps=CAPS,
                source_sha256=req['source_sha256'], source_text=raw.decode(),
                source_check=checked, dictionary=dictionary, symbol_table=transport,
                graph=out, line_roots=list(range(1,len(records)+1)),
                blocks=blocks, construction=CONSTRUCTION.copy())
    size = write_json(output_path, cert)
    inputs = input_bounds(req,raw,records,request_path)
    return dict(certificate=str(output_path), vertices=out['vertices'],
                edges=len(out['edges']), roots=len(records), bytes=size,
                construction=CONSTRUCTION.copy(), input_bounds=inputs, caps=CAPS)

if __name__=='__main__':
    import argparse
    ap=argparse.ArgumentParser()
    ap.add_argument('source',type=Path)
    ap.add_argument('request',type=Path,help='independently selected caller authorization')
    ap.add_argument('output',type=Path)
    args=ap.parse_args()
    try:
        print(json.dumps(emit(args.source,args.request,args.output)))
    except Exception as e:
        write_json(args.output.with_suffix('.failure.json'),
                   dict(accepted=False, failure=repr(e), artifact=str(args.output), caps=CAPS))
        raise
