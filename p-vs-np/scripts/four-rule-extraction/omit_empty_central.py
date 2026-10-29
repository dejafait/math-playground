"""Step 479: one saved pair, literal-empty branch selection only; no integration."""
from pathlib import Path
import hashlib
from parameterized_input import CAPS, load, write_json, require, bound

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
OLD = HERE / 'output-477'
OUT = HERE / 'output-479'


def main():
    require(not OUT.exists(), 'refuse existing output-479')
    OUT.mkdir()
    event = load(OLD/'trace/event-00219.json')
    req = load(OLD/'inputs/request.json')
    files = [OLD/p for p in ('trace/event-00219.json', 'trace/event-00196.json',
             'failure-frame-9.json', 'failure-frame-8.json', 'integration-reception.json',
             'trace-received-prefix.json', 'stop-check.json', 'inputs/proof.jsonl',
             'inputs/request.json', 'inputs/source.json', 'inputs/annotations.json',
             'inputs/pair.json', 'inputs/manifest.json')]
    files += [HERE/'omit_empty_central.py', HERE/'receive_empty_central.py']
    cert = dict(alphabet=req['alphabet'], dictionary=req['dictionary'], caps=CAPS,
                original_event=event, parent=load(OLD/'trace/event-00196.json'),
                frame=load(OLD/'failure-frame-9.json'),
                input_hashes={str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                              for p in files})
    # Save complete supplied provenance before construction.
    write_json(OUT/'inputs.json', cert)
    f, g = (event['restrictions'][k]['trimmed'] for k in ('f', 'g'))
    inventory = []
    for i, (_, _, a) in enumerate(f['edges']):
        for j, (_, _, b) in enumerate(g['edges']):
            central = []
            for x in a:
                for y in b:
                    if x != '1' and y != '1' and x != y:
                        lo, hi = sorted((int(x[1:]), int(y[1:])))
                        central.append('t:%d:%d' % (lo, hi))
            inventory.append(dict(f_edge=i, g_edge=j, central=central))
    selected = [p for p in inventory if p['central']]
    r, q = len(selected), sum(len(p['central']) for p in inventory)
    nv = 2+2*r*(f['vertices']+g['vertices'])
    ne = 2*r*(len(f['edges'])+len(g['edges']))+4*r+q
    write_json(OUT/'inventory.json', dict(pairs=inventory, retained=r, central=q,
               vertices=nv, edges=ne, records=nv+ne, required=CAPS['records']))
    bound(nv+ne, 'records', 'selected branch preflight')
    out = dict(vertices=2, source=0, sink=1, edges=[])
    parts = []

    def copy(h, entry, exit):
        lo, first = out['vertices'], len(out['edges'])
        out['vertices'] += h['vertices']
        out['edges'].extend([lo+u, lo+v, list(lab)] for u,v,lab in h['edges'])
        return dict(vertex_range=[lo,out['vertices']], edge_range=[first,len(out['edges'])],
                    entry=lo+entry, exit=lo+exit)

    for p in selected:
        u,v,_ = f['edges'][p['f_edge']]
        a,b,_ = g['edges'][p['g_edge']]
        copies = [copy(f,f['source'],u), copy(g,g['source'],a),
                  copy(g,b,g['sink']), copy(f,v,f['sink'])]
        fp,gp,gs,fs = copies
        first = len(out['edges'])
        out['edges'].extend([[0,fp['entry'],['1']], [fp['exit'],gp['entry'],['1']],
                             [gs['exit'],fs['entry'],['1']], [fs['exit'],1,['1']]])
        out['edges'].extend([gp['exit'],gs['entry'],[x]] for x in p['central'])
        parts.append(dict(f_edge=p['f_edge'],g_edge=p['g_edge'], copies=copies,
                          connecting_edges=[first,len(out['edges'])]))
    require((out['vertices'],len(out['edges'])) == (nv,ne), 'emitter ledger')
    write_json(OUT/'candidate.json', dict(graph=out, branches=parts,
               alphabet=req['alphabet'],dictionary=req['dictionary'],caps=CAPS))
    print(dict(constructed=True,retained=r,omitted=len(inventory)-r,
               actual=nv+ne,required=CAPS['records'],path=str(OUT/'candidate.json')))


if __name__ == '__main__':
    main()
