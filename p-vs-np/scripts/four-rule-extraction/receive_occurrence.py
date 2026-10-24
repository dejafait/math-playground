"""Independent bounded occurrence reception; imports no emitter/constructors.

Shares strict source/provenance parsing with the emitter, and reuses the audited
backward free-word evaluator. This new boundary still needs separate review.
"""
from pathlib import Path
from parameterized_input import (CAPS, require, fields, integer, exact_equal, load,
                                bound, read_bytes, parse, write_json)
from occurrence_input import context, sha, bind_K
from receive_parameterized import Arithmetic, topo, serial, receive as receive_K


def plan(ctx):
    """Only the fixed L097 recipe is admitted; no candidate-selected factor order."""
    result = [('one',dict(kind='constant',value=True))]
    def op(k,kind,inputs):
        result.append((k,dict(kind=kind,inputs=inputs)))
        return k
    for s,group in enumerate(ctx['groups']):
        p = 's'+str(s)+':'
        pos,neg = [],[]
        for j,x in enumerate(group):
            pos.append(p+'z'+str(j))
            result.append((pos[-1],dict(kind='literal',original=x,negative=False)))
            neg.append(p+'n'+str(j))
            result.append((neg[-1],dict(kind='literal',original=x,negative=True)))
        A = op(p+'A','product',neg[1:])
        B = op(p+'B','product',pos[1:])
        a = op(p+'a','product',neg)
        b = op(p+'b','product',pos)
        e = op(p+'e','sum',[a,b])
        ab = op(p+'ab','product',[a,b])
        op(p+'t','sum',[e,ab])
        W = op(p+'W','commutator',[A,pos[0]])
        first = op(p+'first','product',[neg[0],W,B])
        sigma = p+'sigma'
        result.append((sigma,dict(kind='boolean',original=group[0])))
        second = op(p+'second','product',[sigma,A,B])
        op(p+'R','sum',[first,second])
    for s in range(len(ctx['groups'])):
        op('term'+str(s),'product',['s'+str(h)+':t' for h in range(s)]+
           ['s'+str(s)+':R']+['s'+str(h)+':e' for h in range(s+1,len(ctx['groups']))])
    op('J','sum',['term'+str(s) for s in range(len(ctx['groups']))])
    result.extend([('f',dict(kind='tester',which='D')),('g',dict(kind='tester',which='E'))])
    op('fJ','product',['f','J'])
    return result


def graph_check(g,req):
    fields(g,'vertices edges source sink')
    order = topo(g['vertices'],g['edges'],req)
    require(integer(g['source']) and integer(g['sink']) and
            0<=g['source']<g['vertices'] and 0<=g['sink']<g['vertices'],'graph endpoints')
    return order


def copied_composition(g, children, kind):
    """Verify exact fresh partitions and connectors without constructing a graph."""
    require(g['source']==0 and g['sink']==1 and
            g['vertices']==2+sum(c['vertices'] for c in children),'composition vertices/endpoints')
    edges,idx,offset,last = g['edges'],0,2,0
    for child in children:
        for u,v,lab in child['edges']:
            require(idx<len(edges) and exact_equal(edges[idx],[u+offset,v+offset,lab]),
                    'complete fresh copied interior')
            idx += 1
        s,t = child['source']+offset,child['sink']+offset
        connectors = [[0,s,[['one']]],[t,1,[['one']]]] if kind=='sum' else [[last,s,[['one']]]]
        for edge in connectors:
            require(idx<len(edges) and exact_equal(edges[idx],edge),'ordered composition connector')
            idx += 1
        last = t
        offset += child['vertices']
    if kind=='product':
        require(idx<len(edges) and exact_equal(edges[idx],[last,1,[['one']]]),'product final connector')
        idx += 1
    require(idx==len(edges),'unaccounted composition edges')


def tester_check(g,t,alphabet):
    n = t['vertices']
    require(g['vertices']==n+2 and g['source']==n and g['sink']==n+1,'tester graph roots')
    require(len(g['edges'])==len(t['transitions'])+2,'all actual tester transitions')
    for edge,(u,bit,v) in zip(g['edges'],t['transitions']):
        lab = ([] if bit else [['one']])+[['original',alphabet.index(t['order'][u//3])]]
        require(exact_equal(edge,[u,v,lab]),'tester affine edge reception')
    require(exact_equal(g['edges'][-2:],[[n,t['root'],[['one']]],[t['one'],n+1,[['one']]]]),
            'tester entrance/accepting terminal connectors')


def truth(ar,t):
    if type(t) is str:
        return {()} if t=='true' else set() if t=='false' else {(('original',ar.alphabet.index(t)),)}
    a = truth(ar,t[1])
    if t[0]=='not':
        return ar.add({()},a)
    b = truth(ar,t[2])
    return ar.mul(a,b) if t[0]=='and' else ar.add({()},ar.mul(ar.add({()},a),ar.add({()},b)))


def correction_check(data,ctx):
    fields(data,'format graphs recipes input_metrics construction aggregate_records caps')
    require(data['format']=='L097-ordered-correction-v1' and exact_equal(data['caps'],CAPS),'correction format/caps')
    require(exact_equal(data['input_metrics'],ctx['input_metrics']),'original input metrics')
    fields(data['construction'],'max_intermediate_records commutator_calls')
    require(all(integer(x) and 0<=x<=CAPS['records'] for x in data['construction'].values()),
            'correction construction counters')
    expected = plan(ctx)
    graphs,specs = data['graphs'],data['recipes']
    require(type(graphs) is dict and type(specs) is dict and list(graphs)==[k for k,_ in expected] and
            list(specs)==list(graphs),'complete ordered correction graph inventory')
    req = ctx['request']
    # Aggregate preflight precedes any per-graph adjacency allocation.
    total = 0
    for g in graphs.values():
        fields(g,'vertices edges source sink')
        require(integer(g['vertices']) and g['vertices']>0 and type(g['edges']) is list,'graph preflight types')
        total += g['vertices']+len(g['edges'])
        bound(total,'records','retained correction graph aggregate')
    require(integer(data['aggregate_records']) and data['aggregate_records']==total,'aggregate record evidence')
    ar,values,evidence = Arithmetic(req),{},{}
    for key,spec in expected:
        require(exact_equal(specs[key],spec),'exact L097 recipe: '+key)
        g = graphs[key]
        order = graph_check(g,req)
        kind = spec['kind']
        if kind in ('sum','product'):
            copied_composition(g,[graphs[k] for k in spec['inputs']],kind)
        elif kind=='tester':
            tester_check(g,ctx['pair'][spec['which']],req['alphabet'])
        elif kind in ('literal','constant','boolean'):
            if kind=='constant':
                lab = [['one']] if spec['value'] else []
            elif kind=='literal':
                lab = ([['one']] if spec['negative'] else [])+[['original',req['alphabet'].index(spec['original'])]]
            else:
                j = next(i for i,p in enumerate(req['dictionary']['placeholders'])
                         if p['kind']=='boolean' and p['originals']==[spec['original']])
                lab = [['placeholder',j]]
            require(g['vertices']==2 and g['source']==0 and g['sink']==1 and
                    exact_equal(g['edges'],[[0,1,lab]]),'exact atomic graph')
        else:
            require(kind=='commutator','known correction kind')
            for child in spec['inputs']:
                require(all(z[0] in ('one','original') for _,_,lab in graphs[child]['edges'] for z in lab),
                        'L035 operands original-only')
        polys = {mode:ar.evaluate(g['vertices'],g['edges'],order,g['source'],g['sink'],mode)
                 for mode in ('free','zero','axioms')}
        if kind=='commutator':
            a,b = [values[k]['free'] for k in spec['inputs']]
            target = ar.add(ar.mul(a,b),ar.mul(b,a))
            require(not polys['zero'] and polys['axioms']==target,'commutator identities: '+key)
        elif kind in ('sum','product'):
            for mode in polys:
                value = set() if kind=='sum' else {()}
                for child in spec['inputs']:
                    value = (ar.add if kind=='sum' else ar.mul)(value,values[child][mode])
                require(polys[mode]==value,'complete composition polynomial: '+key)
        values[key] = polys
        evidence[key] = {mode:serial(poly) for mode,poly in polys.items()}
    # These are full free-ring comparisons, not Boolean evaluations.
    f,g = values['f']['free'],values['g']['free']
    tilde = truth(ar,ctx['U'])
    require(f==truth(ar,ctx['C']),'exact split-clause f')
    for s in range(len(ctx['groups'])):
        p = 's'+str(s)+':'
        require(not values[p+'R']['zero'] and values[p+'R']['axioms']==ar.add(
                values[p+'e']['free'],values[p+'t']['free']),'group R exact identity')
    require(not values['J']['zero'] and values['J']['axioms']==ar.add(g,tilde),'ordered J exact identity')
    evidence['targets'] = dict(f=serial(f),g=serial(g),tilde=serial(tilde),
                               J=serial(ar.add(g,tilde)),fg=serial(ar.mul(f,g)),
                               K=serial(ar.mul(f,tilde)))
    return dict(component_checked=True,graphs=evidence,arithmetic=ar.counts,
                aggregate_records=total,required_records=CAPS['records'],failures=[])


def receive(manifest,source,annotations,pair,proof,request,K,H):
    ctx = context(manifest,source,annotations,pair,proof,request)
    # Independently validate all generic proof roots/blocks using caller paths.
    kres = receive_K(K,proof,request)
    raw = read_bytes(H,'certificate_bytes')
    data = parse(raw)
    fields(data,'format manifest inputs dictionary K_sha256 correction H')
    require(data['format']=='L097-supplied-occurrence-v1','occurrence certificate format')
    require(exact_equal(data['manifest'],ctx['manifest']) and exact_equal(data['inputs'],ctx['raw']),
            'complete original caller input retention')
    require(exact_equal(data['dictionary'],ctx['request']['dictionary']),'unchanged original B dictionary')
    kraw = read_bytes(K,'certificate_bytes')
    require(sha(kraw)==kres['certificate_sha256']==data['K_sha256'],'checked K byte binding')
    kdata = parse(kraw)
    bind_K(kdata,ctx)
    kgraph = kdata['graph']
    corrections = correction_check(data['correction'],ctx)
    targetK = corrections['graphs']['targets']['K']
    require(exact_equal(kres['roots'][-1]['polynomials']['axioms'],targetK),'literal endpoint gives exact f tilde')
    req = ctx['request']
    h = data['H']
    order = graph_check(h,req)
    copied_composition(h,[kgraph,data['correction']['graphs']['fJ']],'sum')
    ar = Arithmetic(req)
    polys = {mode:ar.evaluate(h['vertices'],h['edges'],order,h['source'],h['sink'],mode)
             for mode in ('free','zero','axioms')}
    require(not polys['zero'] and exact_equal(serial(polys['axioms']),corrections['graphs']['targets']['fg']),
            'unchanged H zero/substituted fg identities')
    return dict(accepted=True,extractor=kres,correction=corrections,
                H={mode:serial(p) for mode,p in polys.items()},arithmetic=ar.counts,
                bounds=dict(certificate_bytes=len(raw),required_bytes=CAPS['certificate_bytes'],
                            H_records=h['vertices']+len(h['edges']),required_records=CAPS['records']),
                input_metrics=ctx['input_metrics'],H_sha256=sha(raw),caps=CAPS,failures=[])


if __name__=='__main__':
    import argparse
    ap = argparse.ArgumentParser()
    for key in ('manifest','source','annotations','pair','proof','request','K','H','output'):
        ap.add_argument(key,type=Path)
    args = vars(ap.parse_args())
    output = args.pop('output')
    try:
        result = receive(**args)
        write_json(output,result)
        print({'accepted':True,'bounds':result['bounds'],'evidence':str(output)})
    except Exception as error:
        write_json(output.with_suffix('.failure.json'),dict(accepted=False,failure=repr(error),caps=CAPS))
        raise
