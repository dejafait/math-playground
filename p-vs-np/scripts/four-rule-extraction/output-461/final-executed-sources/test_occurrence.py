"""One bounded step-461 attempt. NO valid occurrence proof is manufactured.

Correction components are checked on caller-owned finite source/pair inputs.
Each diagnostic proof file is explicitly INVALID (its last line is true).
Passing front-end reception is not full occurrence-witness acceptance.
"""
import copy
import json
from pathlib import Path
import emit_occurrence as emitter
import receive_occurrence as receiver
from audit_parameterized import Forward
from occurrence_input import (context, pair_spec, fold, expand, complement, sha, bind_K)
from parameterized_input import (CAPS, write_json, load, Rejected, request as proof_request,
                                bound, read_bytes, exact_equal)

HERE = Path(__file__).resolve().parent
OUT = HERE/'output-461'


def dictionary(alphabet):
    ps = [dict(name=x,kind='boolean',originals=[x],polynomial=[[x,x],[x]]) for x in alphabet]
    for i,x in enumerate(alphabet):
        for j,y in enumerate(alphabet[i+1:],i+1):
            ps.append(dict(name='p'+str(i)+'_'+str(j),kind='commutator',originals=[x,y],
                           polynomial=[[x,y],[y,x]]))
    return dict(alphabet=alphabet,placeholders=list(reversed(ps)))


def fixture(name,clauses):
    folder = OUT/name
    folder.mkdir()
    def tree(n,tag,empty):
        return fold(list(range(n)),tag,empty)
    f = dict(format='ordered-width-three-v1',clauses=[
        dict(literals=[dict(variable=x,negative=n) for x,n in row],tree=tree(len(row),'or','false'))
        for row in clauses],tree=tree(len(clauses),'and','true'))
    full = clauses+[[('u',False),('v',False)],[('u',True),('v',True)]]
    names = []
    offset = 0
    for row in full:
        names.append(['y'+str(offset+j) for j in range(len(row))])
        offset += len(row)
    alphabet = list(reversed([x for row in names for x in row]))
    a = dict(format='L087-occurrences-v1',gadget=['u','v'],names=names,alphabet=alphabet)
    old = sorted({x for row in clauses for x,_ in row})+['u','v']
    groups = [[y for row,ls in zip(names,full) for y,(x,_) in zip(row,ls) if x==v] for v in old]
    full_literals = [[dict(variable=x,negative=n) for x,n in row] for row in full]
    p = dict(format='L087-canonical-pair-v1',**pair_spec(full_literals,names,groups))
    split = [fold([['not',y] if n else y for y,(_,n) in zip(row,ls)],'or','false')
             for row,ls in zip(names,full)]
    c = (['and',['and',fold(split[:-2],'and','true'),split[-2]],split[-1]] if clauses else
         ['and',split[-2],split[-1]])
    us = [['or',fold([['not',x] for x in g],'and','true'),fold(g,'and','true')] for g in groups]
    goal = complement(expand(['not',['and',c,fold(us,'and','true')]]))
    # This is a malformed diagnostic input, not a purported supplied proof.
    proof = (json.dumps(dict(format='literal-four-rule-v1',alphabet=alphabet,goal=goal),separators=(',',':'))+
             '\n'+json.dumps(dict(rule='true',f='true',refs=[]))+'\n').encode()
    (folder/'proof.jsonl').write_bytes(proof)
    req = dict(format='L108-request-v1',source_sha256=sha(proof),goal=goal,
               alphabet=alphabet,dictionary=dictionary(alphabet))
    for k,obj in [('source',f),('annotations',a),('pair',p),('request',req)]:
        write_json(folder/(k+'.json'),obj,'input_bytes')
    manifest = dict(format='L097-occurrence-caller-v1')
    for k in ('source','annotations','pair','proof','request'):
        file = folder/(k+('.jsonl' if k=='proof' else '.json'))
        manifest[k] = sha(file.read_bytes())
    write_json(folder/'manifest.json',manifest,'input_bytes')
    return folder


def paths(folder):
    return dict(manifest=folder/'manifest.json',source=folder/'source.json',
                annotations=folder/'annotations.json',pair=folder/'pair.json',
                proof=folder/'proof.jsonl',request=folder/'request.json')


def get_context(folder):
    return context(*[paths(folder)[k] for k in ('manifest','source','annotations','pair','proof','request')])


def main():
    OUT.mkdir(exist_ok=False)
    # Preserve exactly the two narrowly relevant fixed archives; no all-checkpoint scan.
    def archives():
        return {str(p.relative_to(HERE)):sha(p.read_bytes()) for n in (457,459)
                for p in sorted((HERE/('output-'+str(n))).rglob('*')) if p.is_file()}
    before = archives()
    write_json(OUT/'archives-before.json',before)
    results = []
    cases = [('opposing-units',[[('x',False)],[('x',True)]]),
             ('singleton-mixed',[[('x',False),('z',True)]]),
             ('repeated-mixed',[[('x',False),('x',False),('x',True)]]),
             ('empty-source',[]),('empty-clause',[[]])]
    base = None
    for name,clauses in cases:
        folder = fixture(name,clauses)
        ctx = get_context(folder)
        data = emitter.corrections(ctx)
        size = write_json(folder/'correction.json',data)
        # Receiver reads the serialized bytes, rather than the emitter object.
        checked = receiver.correction_check(load(folder/'correction.json'),ctx)
        write_json(folder/'component-check.json',checked)
        # Reuse step-459's independently implemented FORWARD integer-coefficient
        # arithmetic, comparing every complete graph/mode against backward words.
        forward = Forward(ctx['request'])
        comparisons = 0
        forward_words = {}
        for key,g in data['graphs'].items():
            forward_words[key] = {}
            for mode in ('free','zero','axioms'):
                table = forward.graph(g['vertices'],g['edges'],g['source'],mode)
                poly = table[g['sink']]
                forward.compare(poly,checked['graphs'][key][mode],key+'/'+mode)
                forward_words[key][mode] = forward.serial(poly)
                comparisons += 1
        write_json(folder/'forward-component-check.json',dict(
            graphs=forward_words,comparisons=comparisons,metrics=forward.metrics,failures=[]))
        try:
            proof_request(folder/'proof.jsonl',folder/'request.json')
        except Rejected as error:
            require_message = str(error)
            assert require_message=='caller exact final endpoint',require_message
        else:
            raise AssertionError('invalid diagnostic archive accepted')
        nonzero = bool(checked['graphs']['fJ']['axioms'])
        result = dict(name=name,front_end_checked=True,correction_checked=True,
                      proof_accepted=False,full_composition_accepted=False,
                      proof_rejection=require_message,nonzero_fJ=nonzero,
                      forward_comparisons=comparisons,forward_metrics=forward.metrics,
                      bytes=size,records=data['aggregate_records'],arithmetic=checked['arithmetic'],
                      input_metrics=ctx['input_metrics'],path=str(folder.relative_to(HERE)))
        write_json(folder/'case-result.json',result)
        results.append(result)
        if name=='opposing-units':
            base = (folder,ctx,data)
    folder,ctx,data = base
    bad = OUT/'mutations'
    bad.mkdir()
    mutations = []
    # Binding tests use actual old generic archives, with NO claim that they
    # supply an occurrence proof. The accepted call is only a byte/dict helper.
    old = load(HERE/'output-457/old-nonzero/certificate.json')
    helper_ctx = dict(raw=dict(proof=old['source_text']),manifest=dict(proof=old['source_sha256']),
                      request=dict(dictionary=old['dictionary']))
    bind_K(old,helper_ctx)
    binding = [dict(name='unchanged-generic-byte-binding-only',accepted=True,occurrence_acceptance=False)]
    for key,change in [('changed-proof-text',lambda d:d.__setitem__('source_text',d['source_text']+'\n')),
                       ('changed-proof-digest',lambda d:d.__setitem__('source_sha256','0'*64)),
                       ('changed-dictionary-order',lambda d:d['dictionary']['placeholders'].reverse())]:
        obj = copy.deepcopy(old)
        change(obj)
        try:
            bind_K(obj,helper_ctx)
        except Rejected as error:
            binding.append(dict(name=key,accepted=False,reason=str(error)))
            mutations.append(dict(name='K-binding-'+key,accepted=False,reason=str(error)))
        else:
            raise AssertionError('K binding failed '+key)
    try:
        bind_K(old,ctx)
    except Rejected as error:
        binding.append(dict(name='actual-other-caller-K',accepted=False,reason=str(error)))
        mutations.append(dict(name='K-binding-actual-other-caller',accepted=False,reason=str(error)))
    else:
        raise AssertionError('actual foreign K binding accepted')
    write_json(OUT/'K-binding-checks.json',binding)
    def correction_case(name,change):
        obj = copy.deepcopy(data)
        change(obj)
        obj['aggregate_records'] = sum(g['vertices']+len(g['edges']) for g in obj['graphs'].values())
        artifact = bad/(name+'.json')
        write_json(artifact,obj)
        try:
            receiver.correction_check(load(artifact),ctx)
        except Exception as error:
            mutations.append(dict(name=name,accepted=False,reason=repr(error),artifact=str(artifact.relative_to(HERE))))
        else:
            raise AssertionError('undetected correction mutation '+name)
    correction_case('wrong-R-order',lambda d:d['recipes']['s0:first']['inputs'].reverse())
    correction_case('wrong-J-context',lambda d:d['recipes']['term0']['inputs'].reverse())
    correction_case('erased-R',lambda d:d['graphs']['s0:R']['edges'].clear())
    correction_case('cycle',lambda d:d['graphs']['s0:W']['edges'].append([0,0,[]]))
    correction_case('boolean-vertex-alias',lambda d:d['graphs']['s0:W'].__setitem__('source',True))
    correction_case('float-label-alias',lambda d:d['graphs']['s0:sigma']['edges'][0][2][0].__setitem__(1,0.0))
    correction_case('dropped-group',lambda d:d['graphs'].pop('s0:R'))
    correction_case('wrong-target-input-metric',lambda d:d['input_metrics'].__setitem__('Q_bytes',0))
    correction_case('record-cap',lambda d:d['graphs']['s0:W'].__setitem__('vertices',CAPS['records']+1))
    # Repair aggregate to expose actual algebraic erasure, not an evidence mismatch.
    def erase_w(d):
        g = d['graphs']['s0:W']
        for _,_,lab in g['edges']:
            lab[:] = [x for x in lab if x[0]!='placeholder']
    correction_case('erased-W-placeholder',erase_w)
    def front_case(name,key,change,pin=True,raw_override=None):
        sub = bad/name
        sub.mkdir()
        for k,path in paths(folder).items():
            (sub/path.name).write_bytes(path.read_bytes())
        path = sub/(key+'.json')
        if raw_override is None:
            obj = load(path,'input_bytes')
            change(obj)
            write_json(path,obj,'input_bytes')
        else:
            path.write_bytes(raw_override)
        if pin:
            m = load(sub/'manifest.json','input_bytes')
            m[key] = sha(path.read_bytes())
            write_json(sub/'manifest.json',m,'input_bytes')
        try:
            get_context(sub)
        except Exception as error:
            mutations.append(dict(name=name,accepted=False,reason=repr(error),artifact=str(sub.relative_to(HERE))))
        else:
            raise AssertionError('undetected input mutation '+name)
    front_case('source-sign','source',lambda d:d['clauses'][0]['literals'][0].__setitem__('negative',True))
    front_case('bool-source-sign','source',lambda d:d['clauses'][0]['literals'][0].__setitem__('negative',0))
    front_case('positional-bool','source',lambda d:d['clauses'][0].__setitem__('tree',False))
    front_case('dropped-occurrence','annotations',lambda d:d['names'][0].clear())
    front_case('duplicate-occurrence','annotations',lambda d:d['names'][0].__setitem__(0,d['names'][1][0]))
    front_case('wrong-gadget-source','annotations',lambda d:d.__setitem__('gadget',['x','v']))
    front_case('alphabet-reordered','annotations',lambda d:d['alphabet'].reverse())
    front_case('pair-transition','pair',lambda d:d['D']['transitions'][0].__setitem__(2,1))
    front_case('pair-root-bool','pair',lambda d:d['D'].__setitem__('root',True))
    front_case('wrong-pair-order','pair',lambda d:d['E']['order'].reverse())
    front_case('dictionary-reordered','request',lambda d:d['dictionary']['placeholders'].reverse(),pin=False)
    front_case('equivalent-wrong-endpoint','request',lambda d:d.__setitem__('goal',['not',['not',d['goal']]]))
    front_case('dictionary-bad-polynomial','request',lambda d:d['dictionary']['placeholders'][0].__setitem__('polynomial',[]))
    front_case('duplicate-JSON-key','pair',lambda d:None,raw_override=b'{"format":1,"format":2}')
    front_case('input-byte-cap','pair',lambda d:None,raw_override=b' '*(CAPS['input_bytes']+1))
    # A valid old generic source/request is still not this occurrence endpoint.
    try:
        receiver.receive(**paths(folder),K=HERE/'output-457/old-nonzero/certificate.json',
                         H=bad/'no-H-will-be-read.json')
    except Rejected as error:
        assert str(error)=='caller exact final endpoint'
        mutations.append(dict(name='generic-certificate-cannot-substitute',accepted=False,reason=str(error),
                              limitation='fails earlier on missing valid occurrence proof; H branch unexercised'))
    else:
        raise AssertionError('invalid proof reached complete composition')
    # Exercise the final copying checker on bounded graphs without inventing K.
    fgraph,jgraph = data['graphs']['f'],data['graphs']['J']
    shell = emitter.compose('sum',[fgraph,jgraph])
    receiver.graph_check(shell,ctx['request'])
    receiver.copied_composition(shell,[fgraph,jgraph],'sum')
    corrupt = copy.deepcopy(shell)
    corrupt['edges'][-1][0] = 0
    try:
        receiver.copied_composition(corrupt,[fgraph,jgraph],'sum')
    except Rejected as error:
        mutations.append(dict(name='changed-outer-connector',accepted=False,reason=str(error),
                              limitation='structural component only; no proof/K/H acceptance'))
    else:
        raise AssertionError('changed connector accepted')
    write_json(OUT/'outer-copy-component.json',dict(graph=shell,corrupt=corrupt,proof_or_H=False))
    after = archives()
    assert exact_equal(before,after),'existing archives changed'
    write_json(OUT/'archives-after.json',after)
    write_json(OUT/'cases.json',results)
    write_json(OUT/'mutations.json',mutations)
    scripts = [HERE/x for x in ('occurrence_input.py','emit_occurrence.py','receive_occurrence.py','test_occurrence.py')]
    summary = dict(outcome='bounded attempt; complete positive composition UNVERIFIED',
                   front_end_cases=len(results),correction_component_cases=len(results),
                   valid_supplied_endpoint_proofs=0,complete_positive_compositions=0,
                   nonzero_fJ_cases=sum(x['nonzero_fJ'] for x in results),
                   independent_forward_comparisons=sum(x['forward_comparisons'] for x in results),
                   rejected_cases=len(mutations)+len(results),failures=[],
                   max_actual=dict(records=max(x['records'] for x in results),
                                   certificate_bytes=max(x['bytes'] for x in results),
                                   **{k:max(x['arithmetic'][k] for x in results) for k in results[0]['arithmetic']}),
                   required=CAPS,preserved_archive_files=len(before),
                   forward_max_actual={k:max(x['forward_metrics'][k] for x in results)
                                       for k in results[0]['forward_metrics']},
                   scripts={p.name:sha(p.read_bytes()) for p in scripts},
                   limitations=['no valid endpoint proof received; full emit/receive success branch unexecuted',
                                'shared provenance parser and new composition code await separate critical audit',
                                'trusted caller paths and SHA256 collision resistance',
                                'generic literal checker second read remains separately uncapped',
                                'caps/counters do not establish total interpreter work/memory or all-size guarantees'])
    write_json(OUT/'summary.json',summary)
    print(json.dumps({k:summary[k] for k in ('outcome','front_end_cases','correction_component_cases',
                     'valid_supplied_endpoint_proofs','complete_positive_compositions','nonzero_fJ_cases',
                     'rejected_cases','independent_forward_comparisons','max_actual',
                     'forward_max_actual','preserved_archive_files','failures')}))
    print('Required bounds and full evidence:',OUT/'summary.json')


if __name__=='__main__':
    try:
        main()
    except Exception as error:
        if OUT.exists():
            write_json(OUT/'failure.json',dict(completed=False,failure=repr(error),caps=CAPS))
        raise
