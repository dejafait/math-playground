"""Focused adversarial checks for step 483; no production files modified."""
import copy
import json
import sys
from pathlib import Path
import parameterized_input as p
import receive_selected_commutator as s
import empty_central_translation as emitter
from verify_empty_central_occurrence import Reception
from receive_parameterized import Arithmetic
from verify_constant_translation import typed

HERE=Path(__file__).resolve().parent
OUT=HERE/'output-483/units'


def save(path,value):
    path.write_text(json.dumps(value,separators=(',',':'))+'\n')


def rejects(call,fragment):
    try: call()
    except (p.Rejected,RuntimeError) as error:
        assert fragment in str(error),(fragment,str(error))
        return dict(rejected=True,reason=str(error))
    raise AssertionError('missing rejection: '+fragment)


def main():
    OUT.mkdir(exist_ok=False)
    req=p.load(HERE/'output-481/inputs/request.json')
    emitter.e.ALPHABET=req['alphabet']
    receiver=object.__new__(Reception)
    receiver.req=req; receiver.transport=p.symbol_map(req['alphabet'],req['dictionary'])
    receiver.ar=Arithmetic(req)
    adapter=emitter.EmptyCentral(OUT)
    events=[]
    def capture(kind,**values):
        index=len(events)
        events.append(copy.deepcopy(dict(kind=kind,**values)))
        return index
    adapter.save=capture
    def atom(label):
        return dict(vertices=2,source=0,sink=1,edges=[[0,1,label]])
    def word(a,b):
        return dict(vertices=3,source=0,sink=2,edges=[[0,1,[a]],[1,2,[b]]])
    pairs=[('duplicate-cancelling-central',atom(['x1','x1']),atom(['x2'])),
           ('same-original-empty',atom(['x1']),atom(['x1'])),
           ('constant-empty',atom(['1']),atom(['x2'])),
           ('no-path',dict(vertices=2,source=0,sink=1,edges=[]),atom(['x2'])),
           ('coincident-empty-path',dict(vertices=1,source=0,sink=0,edges=[]),atom(['x2'])),
           ('ordered-four-factors',word('x1','x2'),word('x3','x4'))]
    results=[]
    for case,f,g in pairs:
        start=len(events)
        graph,q=adapter.call('m.witness',f,g)
        event,output=events[start:start+2]
        a,b=[event['restrictions'][k]['trimmed'] for k in ('f','g')]
        inventory,ledger=s.selected_input(receiver,event,a,b)
        x,y=[receiver.evaluate(h,original=True)['free'] for h in (f,g)]
        target=receiver.ar.add(receiver.ar.mul(x,y),receiver.ar.mul(y,x))
        evidence=s.receive_output(receiver,start,event,output,a,b,inventory,ledger,target,OUT)
        if case=='duplicate-cancelling-central':
            assert ledger['retained']==1 and ledger['central']==2
            assert not evidence['polynomials']['free'] and evidence['structural_counts']==[1]
        if case in ('same-original-empty','constant-empty','no-path','coincident-empty-path'):
            assert graph==dict(vertices=2,source=0,sink=1,edges=[]) and q==0
        results.append(dict(case=case,input=event,output=output,evidence=evidence))
    save(OUT/'selector-cases.json',results)

    # Reject changed complete-copy evidence even if aggregate identities could cancel.
    event,output=copy.deepcopy(events[-2:]); j=len(events)-2
    a,b=[event['restrictions'][k]['trimmed'] for k in ('f','g')]
    inv,ledger=s.selected_input(receiver,event,a,b)
    x,y=[receiver.evaluate(h,original=True)['free'] for h in (a,b)]
    target=receiver.ar.add(receiver.ar.mul(x,y),receiver.ar.mul(y,x))
    mutations=[]
    for kind in ('copy-label','connector','parent','extra-record','central-multiplicity','branch-order'):
        bad=copy.deepcopy(output)
        part=bad['branches'][0]
        if kind=='copy-label': bad['graph']['edges'][0][2]=['1']
        elif kind=='connector': bad['graph']['edges'][part['connecting_edges'][0]][1]+=1
        elif kind=='parent': bad['parent']+=1
        elif kind=='extra-record': bad['graph']['vertices']+=1
        elif kind=='central-multiplicity': bad['central']+=1
        else: bad['branches'].reverse()
        outcome=rejects(lambda:s.receive_output(receiver,j,event,bad,a,b,inv,ledger,target,OUT),'')
        mutations.append(dict(case=kind,mutation=bad,result=outcome))
    save(OUT/'mutations.json',mutations)

    guards=[]
    dead=atom(['x1']);dead['vertices']=4;dead['edges'].append([2,3,['b:1']])
    n=len(events)
    guards.append(dict(case='original-before-restriction',result=rejects(
        lambda:adapter.call('m.witness',dead,atom(['x2'])),'non-original')))
    assert len(events)==n
    rawtrim=emitter.trim
    def corrupted(g):
        value=rawtrim(g);value['trimmed']['edges'][0][2]=['b:1'];return value
    emitter.trim=corrupted
    guards.append(dict(case='original-after-restriction',result=rejects(
        lambda:adapter.call('m.witness',atom(['x1']),atom(['x2'])),'non-original')))
    emitter.trim=rawtrim
    assert len(events)==n
    # Lower isolated test caps only; output graph allocation must not be reached.
    rawgraph=emitter.e.m.graph
    def forbidden(*args,**kw): raise AssertionError('copy allocation reached before rejection')
    emitter.e.m.graph=forbidden
    for cap in ('records','label_entries'):
        old=p.CAPS[cap];p.CAPS[cap]=3 if cap=='records' else 1
        try:
            guards.append(dict(case=cap+'-before-copy',result=rejects(
                lambda:adapter.call('m.witness',atom(['x1']),atom(['x2'])),'preflight')))
        finally:p.CAPS[cap]=old
        assert events[-1]['kind']=='commutator-input'
    emitter.e.m.graph=rawgraph
    save(OUT/'guards.json',dict(cases=guards,pending_input_events=events[n:]))

    # Actual runner import order: every preexisting write_json global alias is rebound.
    import run_empty_central_occurrence as runner
    folder=OUT/'writer';folder.mkdir()
    original=p.write_json
    aliases=[name for name,m in list(sys.modules.items())
             if m is not None and getattr(m,'write_json',None) is original]
    writer=s.install_evidence_budget(folder)
    assert runner.write_json is writer
    assert all(sys.modules[name].write_json is writer for name in aliases)
    # A later normal import reads the patched parameterized_input global.
    namespace={};exec('from parameterized_input import write_json',namespace)
    assert namespace['write_json'] is writer
    # Test with a separate bound function; production CAPS never change here.
    original_bound=s.bound
    limits=dict(certificate_bytes=40,input_bytes=24)
    def testbound(actual,key,stage):
        p.require(actual<=limits[key],dict(stage=stage,actual=actual,required=limits[key]))
    s.bound=testbound
    records=[]
    path=folder/'a.json'
    size=writer(path,{'a':1},'input_bytes');assert size==8
    records.append(dict(case='initial-newline',bytes=size))
    size=writer(path,{'a':'1234567890'},'input_bytes');assert size==19
    records.append(dict(case='replacement-subtracts-old',bytes=size))
    other=folder/'b.json';assert writer(other,{'b':1},'input_bytes')==8
    before=path.read_bytes()
    records.append(dict(case='per-file-failure',result=rejects(
        lambda:writer(path,{'a':'x'*30},'input_bytes'),'streamed file bytes')))
    assert path.read_bytes()==before and path.with_suffix('.json.partial').exists()
    # A second fresh output, with each file in-cap, reaches the aggregate guard.
    records.append(dict(case='aggregate-failure',result=rejects(
        lambda:writer(folder/'c.json',{'a':'x'*20},'certificate_bytes'),'aggregate evidence')))
    assert not (folder/'c.json').exists()
    records.append(dict(case='outside-lexical-path',result=rejects(
        lambda:writer(OUT/'outside.json',{}),'inside fresh output')))
    # Equality at the content cap must still reject the final newline.
    limits['input_bytes']=7;limits['certificate_bytes']=100
    records.append(dict(case='newline-failure',result=rejects(
        lambda:writer(folder/'newline.json',{'a':1},'input_bytes'),'streamed newline')))
    assert not (folder/'newline.json').exists()
    s.bound=original_bound
    save(OUT/'writer-tests.json',dict(aliases=aliases,later_import_rebound=True,
        runner_alias_rebound=True,cases=records,
        artifacts={p.name:dict(bytes=p.stat().st_size,content=p.read_text()) for p in folder.iterdir()},
        scope='trusted generated paths; lexical check is not filesystem confinement; final aggregate is not peak old-plus-temporary disk'))
    save(OUT/'verification.json',dict(accepted=True,selector_cases=len(results),
        mutations=len(mutations),guards=len(guards),writer_cases=len(records),failures=[],
        arithmetic=receiver.ar.counts,caps=p.CAPS))
    print(dict(accepted=True,cases=len(results),mutations=len(mutations),guards=len(guards),
               writer_cases=len(records),failures=[],path=str(OUT/'verification.json')))


if __name__=='__main__':main()
