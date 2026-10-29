"""Independent reception of step-473 operand/correction trace.

Imports no emitter, adapter, or correction constructor. Complete saved graphs
are checked, with the unchanged bounded receiver's backward word arithmetic.
Nested operand recipes are reconstructed directly from the Boolean input.
"""
from pathlib import Path
from parameterized_input import (CAPS, load, request, symbol_map, require,
                                exact_equal, write_json)
from receive_parameterized import Arithmetic, topo, serial

HERE = Path(__file__).resolve().parent
OUT = HERE / 'output-473'


def typed(g, transport):
    require(set(g) == {'vertices','source','sink','edges'}, 'graph fields')
    return dict(vertices=g['vertices'], source=g['source'], sink=g['sink'],
                edges=[[u,v,[transport[a] for a in lab]] for u,v,lab in g['edges']])


def normalized(g):
    edges = []
    for u,v,lab in g['edges']:
        if u == g['sink']:
            continue
        odd = set()
        for a in lab:
            odd.symmetric_difference_update({a})
        edges.extend([[u,v,[a]] for a in sorted(odd)])
    return dict(g,edges=edges)


def root(h, v):
    return dict(h,source=v)


def atom(a):
    return dict(vertices=2,source=0,sink=1,edges=[[0,1,[a]]])


def prefix(h, a, v):
    return dict(vertices=h['vertices']+1,source=h['vertices'],sink=h['sink'],
                edges=h['edges']+[[h['vertices'],v,[a]]])


def nested_schedule(h):
    jobs = []
    for u in range(h['vertices']):
        outgoing = [(v,lab[0]) for z,v,lab in h['edges'] if z == u]
        for v,a in outgoing:
            jobs.append((atom(a),root(h,v)))
        for j,(v,a) in enumerate(outgoing):
            for w,b in outgoing[j+1:]:
                jobs.append((prefix(h,a,v),prefix(h,b,w)))
    return jobs


def translation_calls(records):
    fs = [r['f'] for r in records]
    calls = []
    for r in records:
        tag,f,refs = r['rule'],r['f'],r['refs']
        if tag in ('axiom','contraction'):
            calls.append(f[2] if tag=='axiom' else f)
        elif tag=='expansion':
            calls.extend([fs[refs[0]],f[1]])
        elif tag=='cut':
            a,b,c = fs[refs[0]][1],fs[refs[0]][2],fs[refs[1]][2]
            calls.extend([b,c,['not',a]])
        factors = ([f[1]] if tag=='expansion' else
                   ['false'] if tag in ('contraction','association') else
                   [fs[refs[1]][2],fs[refs[0]][2]] if tag=='cut' else [])
        calls.extend(factors)
    return calls


def main():
    receipt = OUT / 'trace-verification.json'
    require(not receipt.exists(), 'existing trace receipt')
    req,raw,rows,checked = request(OUT/'inputs/proof.jsonl',OUT/'inputs/request.json')
    transport = symbol_map(req['alphabet'],req['dictionary'])
    ar = Arithmetic(req)
    index = load(OUT/'trace/index.json')
    evidence, operands, booleans, translations = [], {}, {}, []
    last_graphs = []
    current = None
    def evaluate(g, modes=('free',)):
        h = typed(g,transport)
        order = topo(h['vertices'],h['edges'],req)
        require(type(h['source']) is int and type(h['sink']) is int and
                0 <= h['source'] < h['vertices'] and 0 <= h['sink'] < h['vertices'],
                'designated graph endpoints')
        return {mode:ar.evaluate(h['vertices'],h['edges'],order,h['source'],h['sink'],mode)
                for mode in modes}
    try:
        for current,item in enumerate(index):
            require(item['index']==current and item['file']=='event-%05d.json'%current,
                    'contiguous trace index')
            event = load(OUT/'trace'/item['file'])
            kind = event['kind']
            require(kind==item['kind'], 'indexed kind')
            saved = dict(index=current,kind=kind)
            if kind=='translation':
                g = event['graph']
                require(all(a=='1' or a in {'x'+str(j+1) for j in range(len(req['alphabet']))}
                            for _,_,lab in g['edges'] for a in lab), 'original-only translation')
                got = evaluate(g)['free']
                target = ar.translation(event['formula'])
                require(got==target, 'formal ordered source translation')
                translations.append(event['formula'])
                last_graphs.append(g)
                saved.update(polynomial=serial(got),target=serial(target),
                             records=g['vertices']+len(g['edges']))
            elif kind=='boolean-input':
                require(last_graphs and exact_equal(event['graph'],last_graphs[-1]),
                        'Boolean input is actual translated operand')
                h = normalized(event['graph'])
                target = evaluate(event['graph'])['free']
                require(evaluate(h)['free']==target, 'all-path normalization preserves input')
                booleans[current] = dict(h=h, polynomial=target, jobs=nested_schedule(h),
                                         position=0, completed=False)
                saved.update(input=serial(target))
            elif kind=='commutator-input':
                f,g = event['f'],event['g']
                parent = event['parent']
                if parent is None:
                    require(len(last_graphs)>=2 and exact_equal(f,last_graphs[-2]) and
                            exact_equal(g,last_graphs[-1]), 'direct correction translation provenance')
                else:
                    state = booleans[parent]
                    k = state['position']
                    require(k<len(state['jobs']) and exact_equal([f,g],list(state['jobs'][k])),
                            'complete ordered nested suffix/prefix recipe')
                    state['position'] += 1
                require(all(a=='1' or a in {'x'+str(j+1) for j in range(len(req['alphabet']))}
                            for h in (f,g) for _,_,lab in h['edges'] for a in lab),
                        'every actual nested operand original-only')
                a,b = evaluate(f)['free'],evaluate(g)['free']
                target = ar.add(ar.mul(a,b),ar.mul(b,a))
                operands[current] = dict(target=target,completed=False)
                saved.update(parent=parent,operands=[serial(a),serial(b)],target=serial(target))
            elif kind=='commutator-output':
                state = operands[event['parent']]
                polys = evaluate(event['graph'],('free','zero','axioms'))
                require(not polys['zero'] and polys['axioms']==state['target'],
                        'individual commutator contracts')
                state['completed'] = True
                saved.update(parent=event['parent'],polynomials={m:serial(p) for m,p in polys.items()})
            elif kind=='boolean-output':
                state = booleans[event['parent']]
                require(exact_equal(event['normalized'],state['h']), 'normalized suffix graph retention')
                require(state['position']==len(state['jobs']), 'every nested call retained')
                polys = evaluate(event['graph'],('free','zero','axioms'))
                a = state['polynomial']
                target = ar.add(ar.mul(a,a),a)
                require(not polys['zero'] and polys['axioms']==target, 'individual Boolean contracts')
                state['completed'] = True
                saved.update(parent=event['parent'],polynomials={m:serial(p) for m,p in polys.items()},
                             target=serial(target),nested_calls=state['position'])
            else:
                raise AssertionError('unexpected trace event')
            evidence.append(saved)
            # Incremental evidence survives arithmetic caps or interruption.
            write_json(OUT/'trace-received-prefix.json',dict(events=evidence,arithmetic=ar.counts))
        expected = translation_calls(rows)
        failure = load(OUT/'failure.json') if (OUT/'failure.json').exists() else None
        if failure is None:
            require(translations==expected, 'all exact source translation call occurrences')
            require(all(v['completed'] for v in operands.values()) and
                    all(v['completed'] for v in booleans.values()), 'all correction outputs received')
        else:
            frame = load(OUT/'failure-frame-2.json')
            require(frame['i']==22 and frame['r']==rows[22] and frame['r']['rule']=='axiom',
                    'retained failed source record')
            require(translations==translation_calls(rows[:22])+[rows[22]['f'][2]],
                    'all translation occurrences up through interrupted axiom')
            require([k for k,v in operands.items() if not v['completed']]==[201] and
                    [k for k,v in booleans.items() if not v['completed']]==[196],
                    'exact pending correction outputs')
        result = dict(accepted=failure is None,verified_trace_prefix=True,
                      events=len(evidence),translations=len(translations),
                      commutators=len(operands),booleans=len(booleans),
                      arithmetic=ar.counts,caps=CAPS,failures=[],
                      pending_commutators=[k for k,v in operands.items() if not v['completed']],
                      pending_booleans=[k for k,v in booleans.items() if not v['completed']],
                      scope='Complete saved events only; no pending output, partial-K or full K/H acceptance.',
                      evidence='trace-received-prefix.json',source=checked)
        write_json(receipt,result)
        print(dict(accepted=result['accepted'],verified_trace_prefix=True,
                   events=len(evidence),translations=len(translations),
                   commutators=len(operands),booleans=len(booleans),
                   arithmetic=ar.counts,path=str(receipt)))
    except Exception as error:
        write_json(OUT/'trace-verification.failure.json',dict(
            accepted=False,event=current,completed_events=len(evidence),
            failure=repr(error),details=list(error.args),arithmetic=ar.counts,caps=CAPS))
        raise


if __name__=='__main__':
    main()
