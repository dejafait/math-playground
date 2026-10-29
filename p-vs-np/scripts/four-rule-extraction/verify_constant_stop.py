"""Independent full-graph/count/preservation check of the step-473 stop.

No emitter, scalar adapter, correction constructor or arithmetic is imported.
The step-471 structural graph checker is reused on complete saved graphs.
"""
from collections import Counter
import hashlib
from pathlib import Path
from parameterized_input import load, require, write_json, CAPS, exact_equal
from verify_positive_stop import graph

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
OUT = HERE / 'output-473'


def main():
    path = OUT/'stop-check.json'
    require(not path.exists(), 'existing stop receipt')
    failure = load(OUT/'failure.json')
    frame = load(OUT/'failure-frame-2.json')
    call = load(OUT/'failure-frame-7.json')
    event = load(OUT/'trace/event-00201.json')
    req = load(OUT/'inputs/request.json')
    rows = [__import__('json').loads(s) for s in (OUT/'inputs/proof.jsonl').read_bytes().splitlines()][1:]
    n,nd = len(req['alphabet']),len(req['dictionary']['placeholders'])
    require(frame['i']==22 and frame['r']==rows[22] and rows[22]['rule']=='axiom', 'exact failure location')
    require(exact_equal(event['f'],call['f']) and exact_equal(event['g'],call['g']) and
            event['parent']==196, 'complete pending operands')
    prefix = graph(frame['out'],True,n,nd)
    operands = [graph(call[k],False,n,nd) for k in ('f','g')]
    f,g = call['f'],call['g']
    p = len(f['edges'])*len(g['edges'])
    af,ag = [Counter(a for _,_,lab in h['edges'] for a in lab if a!='1') for h in (f,g)]
    q = sum(af.values())*sum(ag.values())-sum(v*ag[a] for a,v in af.items())
    nv = 2+2*p*(f['vertices']+g['vertices'])
    ne = 2*p*(len(f['edges'])+len(g['edges']))+4*p+q
    require((p,q,nv,ne)==(call['p'],call['q'],call['nv'],call['ne']), 'independent L035 ledger')
    require(nv+ne==10_500_818 and failure['detail']==[
        dict(stage='L035 preflight',actual=nv+ne,required=2_000_000,resource='records')],
        'exact rejected resource sum')
    blocks = frame['blocks']
    vertex,edge = len(rows)+1,0
    lines = set()
    for block in blocks:
        lo,hi = block['vertex_range']
        first,last = block['edge_range']
        require(lo==vertex and first==edge and lo<hi<=prefix['vertices'] and
                first+2<=last<=prefix['edges'], 'complete fresh partition')
        s,t = block['entry'],block['exit']
        require(lo<=s<hi and lo<=t<hi, 'block endpoints')
        require(all(lo<=u<hi and lo<=v<hi for u,v,_ in frame['out']['edges'][first:last-2]),
                'fresh block interior')
        parent = block['parent']
        require(frame['out']['edges'][last-2:last]==[
            [0 if parent is None else parent+1,s,[['one']]],
            [t,block['line']+1,[['one']]]], 'exact connectors')
        require(0<=block['line']<22, 'retained line range')
        lines.add(block['line'])
        vertex,edge = hi,last
    require(vertex==prefix['vertices'] and edge==prefix['edges'] and lines==set(range(22)),
            'every completed source line/graph record')
    expected_blocks = sum(1+len(r['refs']) for r in rows[:22])
    require(len(blocks)==expected_blocks and not (OUT/'emitted/K.json').exists() and
            not (OUT/'emitted/H.json').exists(), 'complete block count and absent K/H')
    hashes = load(OUT/'preservation-before.json')
    hashes.update(load(OUT/'source-hashes.json'))
    hashes.update(load(OUT/'run-scope.json')['source_hashes'])
    for name,h in hashes.items():
        require(hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==h, 'retained source/input bytes')
    manifest = load(OUT/'inputs/manifest.json')
    for key in ('source','annotations','pair','proof','request'):
        filename = key+('.jsonl' if key=='proof' else '.json')
        copied = OUT/'inputs'/filename
        origin = HERE/('output-470' if key in ('proof','request') else 'output-461/final/empty-clause')/filename
        require(copied.read_bytes()==origin.read_bytes() and
                hashlib.sha256(copied.read_bytes()).hexdigest()==manifest[key], 'exact original caller bytes')
    result = dict(verified_resource_stop=True,failed_source_line_zero_based=22,
                  completed_source_lines=list(range(22)),retained_blocks=len(blocks),
                  all_source_root_vertices=31,prefix=prefix,operands=operands,
                  ledger=dict(p=p,q=q,vertices=nv,edges=ne,actual=nv+ne,
                              required=CAPS['records'],excess=nv+ne-CAPS['records']),
                  unchanged_hashes=hashes,caps=CAPS,failures=[],
                  scope='Full saved topology/count/operand/byte checks; no partial-K or complete K/H polynomial acceptance.')
    write_json(path,result)
    print(dict(verified_resource_stop=True,failed_source_line_zero_based=22,
               completed_lines=22,prefix_records=prefix['records'],
               actual=nv+ne,required=CAPS['records'],path=str(path)))


if __name__=='__main__':
    main()
