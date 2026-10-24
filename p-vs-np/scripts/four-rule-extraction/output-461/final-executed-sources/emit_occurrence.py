"""Bounded reproduction of L097 §2/6.5. Consumes a proof; never finds one."""
import copy
from pathlib import Path
import emit_parameterized as extraction
from parameterized_input import (CAPS, bound, require, symbol_map, write_json, load)
from occurrence_input import context, sha, bind_K


def compose(kind, graphs):
    require(kind in ('sum','product'),'composition tag')
    nv = 2+sum(g['vertices'] for g in graphs)
    ne = sum(len(g['edges']) for g in graphs)+(2*len(graphs) if kind=='sum' else len(graphs)+1)
    bound(nv+ne,'records','occurrence composition before copies')
    out = dict(vertices=nv,source=0,sink=1,edges=[])
    offset,last = 2,0
    for g in graphs:
        out['edges'].extend([[u+offset,v+offset,copy.deepcopy(l)] for u,v,l in g['edges']])
        s,t = offset+g['source'],offset+g['sink']
        if kind=='sum':
            out['edges'].extend([[0,s,[['one']]],[t,1,[['one']]]])
        else:
            out['edges'].append([last,s,[['one']]])
            last = t
        offset += g['vertices']
    if kind=='product':
        out['edges'].append([last,1,[['one']]])
    return out


def atom(label):
    return dict(vertices=2,source=0,sink=1,edges=[[0,1,label]])


def tester_graph(t, alphabet):
    nv = t['vertices']
    bound(nv+len(t['transitions'])+4,'records','tester graph preflight')
    edges = []
    for u,b,v in t['transitions']:
        label = [['original',alphabet.index(t['order'][u//3])]]
        if b==0:
            label = [['one']]+label
        edges.append([u,v,label])
    edges += [[nv,t['root'],[['one']]],[t['one'],nv+1,[['one']]]]
    return dict(vertices=nv+2,source=nv,sink=nv+1,edges=edges)


def corrections(ctx):
    """Named exact recipe, plus all independently copied graph occurrences."""
    req = ctx['request']
    alphabet = req['alphabet']
    extraction.ALPHABET = alphabet
    extraction.CONSTRUCTION.update(max_intermediate_records=0,commutator_calls=0)
    transport = symbol_map(alphabet,req['dictionary'])
    graphs, specs, groups = {}, {}, ctx['groups']
    aggregate = 0

    def put(key,g,spec):
        nonlocal aggregate
        aggregate += g['vertices']+len(g['edges'])
        bound(aggregate,'records','retained occurrence graph aggregate')
        graphs[key],specs[key] = g,spec
        return key

    def op(key,kind,keys):
        return put(key,compose(kind,[graphs[k] for k in keys]),dict(kind=kind,inputs=keys))

    def constant(key,one):
        return put(key,atom([['one']] if one else []),dict(kind='constant',value=one))

    def literal(key,x,neg=False):
        return put(key,atom(([['one']] if neg else [])+[['original',alphabet.index(x)]]),
                   dict(kind='literal',original=x,negative=neg))

    one = constant('one',True)
    # W inputs are exactly the original-only A,z formula graphs in L097 (1).
    for s,group in enumerate(groups):
        prefix = 's'+str(s)+':'
        positive,negative = [],[]
        for j,x in enumerate(group):
            positive.append(literal(prefix+'z'+str(j),x))
            negative.append(literal(prefix+'n'+str(j),x,True))
        A = op(prefix+'A','product',negative[1:])
        B = op(prefix+'B','product',positive[1:])
        a = op(prefix+'a','product',negative)
        b = op(prefix+'b','product',positive)
        e = op(prefix+'e','sum',[a,b])
        ab = op(prefix+'ab','product',[a,b])
        op(prefix+'t','sum',[e,ab])
        # Convert ONLY original-only operands to the private audited L035 module.
        def untyped(g):
            return dict(vertices=g['vertices'],source=g['source'],sink=g['sink'],
                        edges=[[u,v,['1' if z[0]=='one' else 'x'+str(z[1]+1) for z in lab]]
                               for u,v,lab in g['edges']])
        w,_ = extraction.checked_witness(untyped(graphs[A]),untyped(graphs[positive[0]]))
        w['edges'] = [[u,v,[list(transport[z]) for z in lab]] for u,v,lab in w['edges']]
        W = put(prefix+'W',w,dict(kind='commutator',inputs=[A,positive[0]]))
        first = op(prefix+'first','product',[negative[0],W,B])
        j = next(i for i,p in enumerate(req['dictionary']['placeholders'])
                 if p['kind']=='boolean' and p['originals']==[group[0]])
        sigma = put(prefix+'sigma',atom([['placeholder',j]]),dict(kind='boolean',original=group[0]))
        second = op(prefix+'second','product',[sigma,A,B])
        op(prefix+'R','sum',[first,second])
    terms = []
    for s in range(len(groups)):
        keys = ['s'+str(h)+':t' for h in range(s)]+['s'+str(s)+':R']+[
                's'+str(h)+':e' for h in range(s+1,len(groups))]
        terms.append(op('term'+str(s),'product',keys))
    op('J','sum',terms)
    put('f',tester_graph(ctx['pair']['D'],alphabet),dict(kind='tester',which='D'))
    put('g',tester_graph(ctx['pair']['E'],alphabet),dict(kind='tester',which='E'))
    op('fJ','product',['f','J'])
    return dict(format='L097-ordered-correction-v1',graphs=graphs,recipes=specs,
                input_metrics=ctx['input_metrics'],construction=extraction.CONSTRUCTION.copy(),
                aggregate_records=aggregate,caps=CAPS)


def emit(manifest, source, annotations, pair, proof, request, output):
    ctx = context(manifest,source,annotations,pair,proof,request)
    output = Path(output)
    output.mkdir(exist_ok=False)
    # The audited generic emitter validates the COMPLETE supplied proof first.
    construction = extraction.emit(proof,request,output/'K.json')
    correction = corrections(ctx)
    kdata = load(output/'K.json')
    bind_K(kdata,ctx)
    k = kdata['graph']
    h = compose('sum',[k,correction['graphs']['fJ']])
    cert = dict(format='L097-supplied-occurrence-v1',manifest=ctx['manifest'],
                inputs=ctx['raw'],dictionary=ctx['request']['dictionary'],
                K_sha256=sha((output/'K.json').read_bytes()),correction=correction,H=h)
    size = write_json(output/'H.json',cert)
    result = dict(completed=True,certificate_bytes=size,extractor=construction,
                  input_metrics=ctx['input_metrics'],caps=CAPS,
                  acceptance='unverified until receive_occurrence.receive checks both archives')
    write_json(output/'construction.json',result)
    return result


if __name__=='__main__':
    import argparse
    ap = argparse.ArgumentParser()
    for key in ('manifest','source','annotations','pair','proof','request','output'):
        ap.add_argument(key,type=Path)
    args = ap.parse_args()
    try:
        result = emit(**vars(args))
        print({'completed':result['completed'],'bytes':result['certificate_bytes'],'path':str(args.output)})
    except Exception as error:
        write_json(args.output.with_suffix('.failure.json'),dict(completed=False,failure=repr(error),caps=CAPS))
        raise
