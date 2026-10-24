"""Complete bounded integration/mutation evidence for step 457, not an audit."""
import copy
import hashlib
import json
from pathlib import Path
import emit_parameterized as e
import receive_parameterized as r
from parameterized_input import CAPS, request, load, parse, typed, write_json

HERE=Path(__file__).resolve().parent
OUT=HERE/'output-457'
OUT.mkdir(exist_ok=True)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def archives():
    return {str(p.relative_to(HERE)):sha(p) for n in (449,451,453,455)
            for p in sorted((HERE/('output-'+str(n))).rglob('*')) if p.is_file()}


def dictionary(alphabet):
    ps=[]
    for i,x in enumerate(alphabet):
        ps.append(dict(name=x,kind='boolean',originals=[x],polynomial=[[x,x],[x]]))
    for i,x in enumerate(alphabet):
        for j in range(i+1,len(alphabet)):
            y=alphabet[j]
            ps.append(dict(name='pair:'+str(i)+':'+str(j),kind='commutator',
                           originals=[x,y],polynomial=[[x,y],[y,x]]))
    # Caller positions deliberately differ from Boolean-first constructor tokens.
    return dict(alphabet=alphabet,placeholders=list(reversed(ps)))


def fixture(name,alphabet,rows,goal,raw=None):
    d=OUT/name
    d.mkdir(exist_ok=True)
    source=d/'source.jsonl'
    if raw is None:
        h=dict(format='literal-four-rule-v1',alphabet=alphabet,goal=goal)
        raw=('\n'.join(json.dumps(x,separators=(',',':')) for x in [h]+rows)+'\n').encode()
    source.write_bytes(raw)
    req=dict(format='L108-request-v1',source_sha256=sha(source),goal=goal,
             alphabet=alphabet,dictionary=dictionary(alphabet))
    write_json(d/'request.json',req,'input_bytes')
    construction=e.emit(source,d/'request.json',d/'certificate.json')
    reception=r.receive(d/'certificate.json',source,d/'request.json')
    assert reception['accepted'] and len(reception['roots'])==len(rows)
    write_json(d/'construction.json',construction)
    write_json(d/'reception.json',reception)
    return dict(name=name,roots=len(rows),blocks=len(reception['blocks']),
                records=construction['vertices']+construction['edges'],bytes=construction['bytes'],
                arithmetic=reception['arithmetic'],input_bounds=reception['input_bounds'],path=str(d.relative_to(HERE)))


def row(rule,f,refs=None):
    return dict(rule=rule,f=f,refs=[] if refs is None else refs)


def rename(t,mapping):
    return mapping.get(t,t) if type(t) is str else [t[0]]+[rename(x,mapping) for x in t[1:]]


def main():
    before=archives()
    write_json(OUT/'archives-before.json',before)
    cases=[]
    for name,path in [('old-exercise',HERE.parent/'parity-four-rule/output-goal-directed-447/checker-exercise.jsonl'),
                      ('old-nonzero',HERE/'nonzero-source.jsonl')]:
        raw=path.read_bytes()
        h,*rows=[parse(x) for x in raw.splitlines()]
        cases.append(fixture(name,h['alphabet'],rows,h['goal'],raw))
    h,*rows=[parse(x) for x in (HERE/'nonzero-source.jsonl').read_bytes().splitlines()]
    mapped=[dict(rule=x['rule'],f=rename(x['f'],{'A':'1','B':'x1'}),refs=x['refs']) for x in rows]
    # Add legal original atoms that coincide with connective tag strings; they are
    # strings rather than prefix arrays. Earlier final endpoint becomes unused.
    mapped += [row('axiom',['or',['not','or'],'or']),row('axiom',['or',['not','not'],'not'])]
    cases.append(fixture('collision-reordered',['or','1','x1','not','unused'],mapped,mapped[-1]['f']))
    cases.append(fixture('empty',[],[row('true','true'),row('not-false',['not','false'])],['not','false']))
    f=['or',['not','1'],'1']
    cases.append(fixture('singleton',['1'],[row('axiom',f)],f))
    # Constants in every cut argument, with an unused complete original entry.
    p=['or',['not','true'],'true']
    rows2=[row('axiom',p),row('expansion',['or',['not',['not','true']],p],[0]),
           row('cut',['or','true',p],[0,1])]
    cases.append(fixture('constant-cut-unused-alphabet',['spare'],rows2,rows2[-1]['f']))
    # Compare every complete old block/root polynomial after typed dictionary
    # transport. New caller placeholder display names/positions are different.
    regressions=[]
    for new_name,old_dir in [('old-exercise','output-449'),('old-nonzero','output-453')]:
        new=OUT/new_name
        nr=load(new/'reception.json')
        nq=load(new/'request.json','input_bytes')
        old=load(HERE/old_dir/'reception.json')
        oc=load(HERE/old_dir/'certificate.json')
        amap={x:('original',i) for i,x in enumerate(nq['alphabet'])}
        for p in oc['dictionary']['placeholders']:
            j=next(i for i,q in enumerate(nq['dictionary']['placeholders'])
                   if (p['kind'],p['originals'])==(q['kind'],q['originals']))
            amap[p['name']]=('placeholder',j)
        comparisons=0
        for group in ('roots','blocks'):
            assert len(old[group])==len(nr[group])
            for a,b in zip(old[group],nr[group]):
                for mode in ('free','zero','axioms'):
                    lhs={tuple(amap[x] for x in w) for w in a['polynomials'][mode]}
                    rhs={tuple(tuple(x) for x in w) for w in b['polynomials'][mode]}
                    assert lhs==rhs,(new_name,group,mode)
                    comparisons+=1
                assert {tuple(amap[x] for x in w) for w in a['target']}=={
                       tuple(tuple(x) for x in w) for w in b['target']}
                comparisons+=1
        regressions.append(dict(name=new_name,complete_polynomial_comparisons=comparisons,
                                old_reception_sha256=sha(HERE/old_dir/'reception.json')))
    write_json(OUT/'regressions.json',regressions)
    write_json(OUT/'accepted-cases.json',cases)

    base=OUT/'old-nonzero'
    cert=load(base/'certificate.json')
    mutations=[]
    bad=OUT/'mutations'
    bad.mkdir(exist_ok=True)
    def cert_case(name,change,accepted=False):
        obj=copy.deepcopy(cert)
        change(obj)
        path=bad/(name+'.json')
        write_json(path,obj)
        try:
            result=r.receive(path,base/'source.jsonl',base/'request.json')
        except Exception as ex:
            assert not accepted,(name,repr(ex))
            mutations.append(dict(name=name,accepted=False,reason=repr(ex),artifact=str(path.relative_to(HERE))))
        else:
            assert accepted,name
            write_json(bad/(name+'-reception.json'),result)
            mutations.append(dict(name=name,accepted=True,artifact=str(path.relative_to(HERE))))
    cert_case('sink-bool',lambda d:d['graph'].__setitem__('sink',True))
    cert_case('edge-index-bool',lambda d:d['graph']['edges'][0].__setitem__(0,True))
    cert_case('symbol-index-bool',lambda d:next(lab for _,_,lab in d['graph']['edges'] if lab and lab[0][0]=='placeholder')[0].__setitem__(1,True))
    cert_case('symbol-index-float',lambda d:next(lab for _,_,lab in d['graph']['edges'] if lab and lab[0][0]=='placeholder')[0].__setitem__(1,0.0))
    cert_case('wrong-namespace',lambda d:next(lab for _,_,lab in d['graph']['edges'] if lab and lab[0][0]=='placeholder')[0].__setitem__(0,'original'))
    cert_case('dictionary-swap',lambda d:d['dictionary']['placeholders'].reverse())
    cert_case('source-retention',lambda d:d.__setitem__('source_text',d['source_text']+'\n'))
    cert_case('digest',lambda d:d.__setitem__('source_sha256','0'*64))
    cert_case('symbol-table',lambda d:d['symbol_table'].__setitem__('1',['original',0]))
    cert_case('missing-unused-root',lambda d:d['line_roots'].pop(2))
    cert_case('missing-unused-block',lambda d:d['blocks'].pop(2))
    cert_case('provenance',lambda d:d['blocks'][0].__setitem__('line',1))
    cert_case('construction-bool',lambda d:d['construction'].__setitem__('commutator_calls',True))
    cert_case('evidence-bool',lambda d:d['source_check'].__setitem__('records',True))
    cert_case('evidence-float',lambda d:d['source_check'].__setitem__('records',9.0))
    cert_case('caps-changed',lambda d:d['caps'].__setitem__('records',3_000_000))
    cert_case('record-cap',lambda d:d['graph'].__setitem__('vertices',CAPS['records']+1))
    cert_case('label-cap',lambda d:d['graph']['edges'][0].__setitem__(2,[['one']]*(CAPS['label_width']+1)))
    cert_case('cycle',lambda d:d['graph']['edges'][0].__setitem__(1,d['graph']['edges'][0][0]))
    def erase(d,block,tag):
        first,last=d['blocks'][block]['edge_range']
        for _,_,lab in d['graph']['edges'][first:last-2]:
            lab[:]=[x for x in lab if x[0]!=tag]
    cert_case('nonzero-cut-erased',lambda d:erase(d,12,'placeholder'))
    cert_case('used-boolean-erased',lambda d:erase(d,1,'placeholder'))
    cert_case('neutral-label',lambda d:d['graph']['edges'][0][2].extend([['original',0],['original',0]]),True)

    # Source/request mutations are externally authorized for syntax tests. A
    # different well-formed source still cannot replace the pinned caller input.
    req=load(base/'request.json','input_bytes')
    raw=(base/'source.jsonl').read_bytes()
    def input_case(name,new_raw=None,change_req=None,raw_req=None):
        folder=bad/name
        folder.mkdir(exist_ok=True)
        source=folder/'source.jsonl'
        source.write_bytes(raw if new_raw is None else new_raw)
        q=copy.deepcopy(req)
        q['source_sha256']=sha(source)
        if change_req:
            change_req(q)
        if raw_req is None:
            write_json(folder/'request.json',q,'input_bytes')
        else:
            (folder/'request.json').write_bytes(raw_req)
        try:
            request(source,folder/'request.json')
        except Exception as ex:
            mutations.append(dict(name=name,accepted=False,reason=repr(ex),artifact=str(folder.relative_to(HERE))))
        else:
            raise AssertionError('accepted bad input '+name)
    input_case('source-duplicate-key',raw.replace(b'"rule":"axiom"',b'"rule":"true","rule":"axiom"',1))
    input_case('source-float-ref',raw.replace(b'"refs":[1]',b'"refs":[1.0]',1))
    input_case('source-bool-ref',raw.replace(b'"refs":[1]',b'"refs":[true]',1))
    input_case('source-same-cut-ref',raw.replace(b'"refs":[0,4]',b'"refs":[0,0]',1))
    input_case('source-substituted',raw+b'\n',change_req=lambda q:q.__setitem__('source_sha256',req['source_sha256']))
    for tag in ('axiom','true','not-false','expansion','contraction','association','cut'):
        all_rows=[parse(x) for x in raw.splitlines()]
        index=next(i for i,x in enumerate(all_rows[1:],1) if x['rule']==tag)
        all_rows[index]['f']='false'
        damaged=('\n'.join(json.dumps(x,separators=(',',':')) for x in all_rows)+'\n').encode()
        input_case('literal-'+tag,damaged)
    input_case('goal-mismatch',change_req=lambda q:q.__setitem__('goal','true'))
    input_case('alphabet-order',change_req=lambda q:q['alphabet'].reverse())
    input_case('dictionary-missing',change_req=lambda q:q['dictionary']['placeholders'].pop())
    input_case('dictionary-names',change_req=lambda q:q['dictionary']['placeholders'][0].__setitem__('name',q['dictionary']['placeholders'][1]['name']))
    input_case('dictionary-polynomial',change_req=lambda q:q['dictionary']['placeholders'][0].__setitem__('polynomial',[]))
    input_case('caller-sha-mismatch',change_req=lambda q:q.__setitem__('source_sha256','0'*64))
    input_case('request-duplicate-key',raw_req=b'{"format":"bad","format":"L108-request-v1"}')
    input_case('input-byte-cap',new_raw=b' '*(CAPS['input_bytes']+1))
    input_case('json-depth-cap',new_raw=(b'['*(CAPS['json_depth']+1)+b']'*(CAPS['json_depth']+1)))
    deep='A'
    for _ in range(CAPS['tree_depth']):
        deep=['not',deep]
    input_case('tree-depth-cap',change_req=lambda q:q.__setitem__('goal',deep))
    # A duplicate key in a candidate must be caught before its graph is used.
    duplicate=bad/'certificate-duplicate.json'
    duplicate.write_bytes((base/'certificate.json').read_bytes().replace(b'"format":',b'"format":"bad","format":',1))
    try:
        r.receive(duplicate,base/'source.jsonl',base/'request.json')
    except Exception as ex:
        mutations.append(dict(name='certificate-duplicate',accepted=False,reason=repr(ex),artifact=str(duplicate.relative_to(HERE))))
    else:
        raise AssertionError('accepted duplicate candidate')
    # Diagnostic arithmetic stops are direct small calls with original caps.
    arithmetic=r.Arithmetic(req)
    for name,call in [('word-length-cap',lambda:arithmetic.mul({(('original',0),)*CAPS['word_length']},{(('original',0),)})),
                      ('multiplication-cap',lambda:arithmetic.mul({()}, {()}))]:
        if name=='multiplication-cap':
            arithmetic.counts['multiplication_pairs']=CAPS['multiplication_pairs']
        try:
            call()
        except Exception as ex:
            mutations.append(dict(name=name,accepted=False,reason=repr(ex),artifact='direct bounded arithmetic call'))
        else:
            raise AssertionError(name)
    # Exact L035 copy preflight must fail before its internal copy loops.
    try:
        e.checked_witness(dict(vertices=1_000_000,edges=[[0,1,['x1']]]),
                          dict(vertices=1_000_000,edges=[[0,1,['x1']]]))
    except Exception as ex:
        mutations.append(dict(name='construction-copy-cap',accepted=False,reason=repr(ex),
                              artifact='direct L035 preflight, before copying'))
    else:
        raise AssertionError('construction copy cap')
    after=archives()
    assert before==after,'fixed archives changed'
    write_json(OUT/'archives-after.json',after)
    write_json(OUT/'mutation-results.json',mutations)
    summary=dict(accepted_cases=len(cases),accepted_roots=sum(x['roots'] for x in cases),
                 rejected=sum(not x['accepted'] for x in mutations),neutral_accepted=1,
                 preserved_archive_files=len(before),regression_polynomial_comparisons=sum(x['complete_polynomial_comparisons'] for x in regressions),failures=[],actual_max=dict(
                 records=max(x['records'] for x in cases),certificate_bytes=max(x['bytes'] for x in cases),
                 **{k:max(x['arithmetic'][k] for x in cases) for k in cases[0]['arithmetic']}),required=CAPS, input_actual_max={k:max(x['input_bounds']['actual'][k] for x in cases) for k in cases[0]['input_bounds']['actual']},
                 scripts={p.name:sha(p) for p in [Path(__file__),HERE/'parameterized_input.py',HERE/'emit_parameterized.py',HERE/'receive_parameterized.py']})
    write_json(OUT/'summary.json',summary)
    print(json.dumps(summary))
    print('Full certificates, all-root/block words, rejections and archive hashes:',OUT)

if __name__=='__main__':
    try:
        main()
    except Exception as ex:
        write_json(OUT/'failure.json',dict(accepted=False,failure=repr(ex),artifact=str(OUT),caps=CAPS))
        raise
