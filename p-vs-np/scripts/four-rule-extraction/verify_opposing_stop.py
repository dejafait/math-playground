"""Full structural binding/count check of step 489's one saved resource stop.

Receives the entire retained K prefix and partial Boolean graph. No identities
are assigned to either unfinished graph; arithmetic is a separate receipt.
"""
from pathlib import Path
import hashlib
import traceback
import verify_trimmed_stop as old
import verify_opposing_occurrence as caller
from parameterized_input import (CAPS, load, require, exact_equal, write_json,
                                request, symbol_map)
from verify_positive_stop import graph
from verify_constant_translation import typed, normalized, root, atom, prefix
from receive_occurrence import copied_composition
from receive_selected_commutator import install_evidence_budget

HERE = Path(__file__).resolve().parent
OUT = HERE / 'output-489'


def main(persist=True):
    require(not (OUT / 'stop-check.json').exists(), 'refuse existing stop receipt')
    if persist:
        install_evidence_budget(OUT)
    old.OUT = OUT
    req, raw, rows, checked = request(OUT/'inputs/proof.jsonl', OUT/'inputs/request.json')
    require(checked['records']==212 and checked['sha256']==
            'f779fa52af4eb63805e45aa9940620be1cd3ce6c993ff4a903a996a0b539c74e',
            'exact independently audited endpoint transcript')
    failure = load(OUT/'failure.json')
    outer = load(OUT/'failure-frame-3.json')
    copy = load(OUT/'failure-frame-8.json')
    attach = load(OUT/'failure-frame-7.json')
    require(exact_equal(copy['out'], attach['out']) and attach['kind']=='sum_commutator',
            'complete pending attach/copy output binding')
    del attach
    boolean = load(OUT/'failure-frame-6.json')
    require(exact_equal(boolean['out'], copy['out']), 'complete Boolean/copy frame binding')
    del boolean
    failed = outer['i']
    require(failed==78 and exact_equal(outer['r'],rows[failed]) and
            rows[failed]['rule']=='axiom', 'exact pending source axiom')
    n, nd = len(req['alphabet']),len(req['dictionary']['placeholders'])
    kcounts = graph(outer['out'], True, n, nd)
    bcounts = graph(copy['out'], False, n, nd)
    pending = graph(copy['g'], False, n, nd)
    actual = bcounts['records']+pending['records']+8
    require(actual==2011597 and actual>CAPS['records'] and
            failure['detail']==[dict(stage='serial/Boolean copy preflight including connectors',
                                    actual=actual,required=CAPS['records'],resource='records')],
            'complete independently counted rejected allocation')
    index = load(OUT/'trace/index.json')
    binding = old.Binding(index, symbol_map(req['alphabet'],req['dictionary']))
    blocks = outer['blocks']
    cursor,vertex,edge = 0,len(rows)+1,0
    fs = [r['f'] for r in rows]

    def block(i,role,kind,args,parent,expected=None,factors=None):
        nonlocal cursor,vertex,edge
        item=blocks[cursor]; cursor+=1
        require(exact_equal([item[k] for k in ('line','role','kind','arguments','parent')],
                            [i,role,kind,args,parent]), 'complete source block metadata')
        lo,hi=item['vertex_range']; first,last=item['edge_range']; s,t=item['entry'],item['exit']
        require(lo==vertex and first==edge and lo<hi<=kcounts['vertices'] and
                first+2<=last<=kcounts['edges'] and lo<=s<hi and lo<=t<hi,
                'contiguous fresh K prefix partitions')
        interior=outer['out']['edges'][first:last-2]
        require(all(lo<=u<hi and lo<=v<hi for u,v,_ in interior),'every fresh K interior')
        require(exact_equal(outer['out']['edges'][last-2:last],
                            [[0 if parent is None else parent+1,s,[['one']]],
                             [t,i+1,[['one']]]]), 'all K attachment connectors')
        local=dict(vertices=hi-lo,source=s-lo,sink=t-lo,
                   edges=[[u-lo,v-lo,lab] for u,v,lab in interior])
        if factors is None:
            require(exact_equal(local,typed(expected,binding.transport)),
                    'complete trace output copied to K prefix')
        else:
            copied_composition(local,[typed(g,binding.transport) for g in factors],'product')
        vertex,edge=hi,last

    for i,r in enumerate(rows[:failed]):
        tag,f,refs=r['rule'],r['f'],r['refs']; factors=None
        if tag in ('axiom','contraction'):
            a=f[2] if tag=='axiom' else f
            seed=binding.boolean(binding.translation(a)); kind,args='boolean',[a]
        elif tag=='expansion':
            a,b=fs[refs[0]],f[1]
            aa,bb=binding.translation(a),binding.translation(b)
            seed=binding.commutator(aa,bb,None); kind,args='commutator',[a,b]
        elif tag=='cut':
            a,b,c=fs[refs[0]][1],fs[refs[0]][2],fs[refs[1]][2]
            bb,cc=binding.translation(b),binding.translation(c)
            w=binding.commutator(bb,cc,None); pre=binding.translation(['not',a])
            factors,seed=[pre,w],None; kind,args='prefixed-commutator',[a,b,c]
        else:
            require(tag in ('true','not-false','association'),'known zero seed')
            seed=dict(vertices=2,source=0,sink=1,edges=[]); kind,args='zero',[]
        block(i,'seed',kind,args,None,seed,factors)
        formulas=([f[1]] if tag=='expansion' else ['false'] if tag in ('contraction','association')
                  else [fs[refs[1]][2],fs[refs[0]][2]] if tag=='cut' else [])
        for j,formula in zip(refs,formulas):
            block(i,'transition','translation',[formula],j,binding.translation(formula))
    require(cursor==len(blocks) and vertex==kcounts['vertices'] and edge==kcounts['edges']
            and outer['out']['source']==0 and outer['out']['sink']==len(rows),
            'all retained K records and all 212 allocated source roots')
    g=binding.translation(rows[failed]['f'][2])
    parent,event=binding.take('boolean-input')
    require(exact_equal(event['graph'],g),'exact pending axiom Boolean operand')
    h=normalized(g); out=copy['out']; edges=out['edges']
    require(out['source']==h['source'] and out['sink']==h['vertices'] and
            exact_equal(edges[:len(h['edges'])],h['edges']), 'complete Boolean propagation prefix')
    vertex,cursor=h['vertices']+1,len(h['edges'])
    attachments,jobs=0,0

    def attach(u,kind,child):
        nonlocal vertex,cursor,attachments
        if binding.position==len(index) and kind=='sum_commutator':
            require(exact_equal(child,copy['g']) and vertex==out['vertices'] and
                    cursor==len(edges), 'entire partial Boolean and exact pending block')
            raise StopIteration
        if type(child) is list:
            # Independently receive the actual serial wrapper and copied factors.
            nv=2+sum(c['vertices'] for c in child)
            ne=sum(len(c['edges']) for c in child)+len(child)+1
            local=dict(vertices=nv,source=0,sink=1,
                       edges=[[a-vertex,b-vertex,lab] for a,b,lab in edges[cursor:cursor+ne]])
            # The existing typed composition checker receives all interiors/connectors.
            copied_composition(typed(local,binding.transport),
                               [typed(c,binding.transport) for c in child],'product')
            s,t=vertex,vertex+1
            vertex+=nv; cursor+=ne
        else:
            lo=vertex; s,t=lo+child['source'],lo+child['sink']
            for a,b,lab in child['edges']:
                require(exact_equal(edges[cursor],[lo+a,lo+b,lab]),'every Boolean copied edge')
                cursor+=1
            vertex+=child['vertices']
        require(exact_equal(edges[cursor:cursor+2],[[u,s,['1']],[t,out['sink'],['1']]]),
                'every completed Boolean attachment connector')
        cursor+=2; attachments+=1

    stopped=False
    try:
        for u in range(h['vertices']):
            outgoing=[(v,lab[0]) for a,v,lab in h['edges'] if a==u]
            for v,x in outgoing:
                suffix=root(h,v)
                if x!='1': attach(u,'edge_boolean',[atom('b:'+x[1:]),suffix,suffix])
                w=binding.commutator(atom(x),suffix,parent); jobs+=1
                attach(u,'product_commutator',[atom(x),w,suffix])
            for i,(v,x) in enumerate(outgoing):
                for z,y in outgoing[i+1:]:
                    w=binding.commutator(prefix(h,x,v),prefix(h,y,z),parent); jobs+=1
                    attach(u,'sum_commutator',w)
    except StopIteration:
        stopped=True
    require(stopped and binding.position==len(index),'exact complete saved trace boundary')
    require(not (OUT/'emitted/K.json').exists() and not (OUT/'emitted/H.json').exists(),
            'no complete K/H output')
    hashes=caller.preservation()
    result=dict(verified_resource_stop=True,failures=[],complete_KH_received=False,
                failed_source_line_zero_based=failed,failed_rule='axiom',events=len(index),
                boolean_parent=parent,pending_commutator_output=len(index)-1,
                retained_K_blocks=len(blocks),completed_source_lines=list(range(failed)),
                all_source_root_vertices=len(rows),K_prefix=kcounts,partial_boolean=bcounts,
                pending_block=pending,required_copy_records=actual,record_cap=CAPS['records'],
                excess_records=actual-CAPS['records'],pending_kind='sum_commutator',
                complete_partial_boolean_copy_binding=True,completed_boolean_attachments=attachments,
                attempted_parent_commutators=jobs,complete_K_prefix_trace_binding=True,
                unchanged_hashes=hashes,
                supplementary_script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                evidence_bytes_before_stop_receipt=sum(p.stat().st_size for p in OUT.rglob('*')
                                                     if p.is_file()),caps=CAPS,
                scope='Full structural/count evidence only; unfinished Boolean and K have no claimed identities.')
    if persist:
        write_json(OUT/'stop-check.json',result)
    print(dict(verified_resource_stop=True,actual=actual,required=CAPS['records'],
               failed_source_line=failed,events=len(index),K_blocks=len(blocks),
               partial_boolean=bcounts['records'],pending_block=pending['records'],
               evidence_bytes=sum(p.stat().st_size for p in OUT.rglob('*') if p.is_file()),
               required_evidence_bytes=CAPS['certificate_bytes'],failures=[],
               boolean_parent=parent,attempted_parent_commutators=jobs,
               completed_boolean_attachments=attachments,
               K_prefix=kcounts,partial_boolean_counts=bcounts,pending_counts=pending,
               receipt_persisted=persist,
               path=str(OUT/'stop-check.json') if persist else
               'existing output-489 frames/trace; no new artifact after evidence-cap failure'))


if __name__=='__main__':
    import sys
    readonly=sys.argv[1:]==['--read-only']
    require(not sys.argv[1:] or readonly,'only optional --read-only is admitted')
    try:
        main(persist=not readonly)
    except Exception as error:
        if not readonly:
            write_json(OUT/'stop-check.failure.json',dict(
                accepted=False,failure=repr(error),traceback=traceback.format_exc(),
                caps=CAPS,evidence='complete existing output-489 frames and trace'))
        print(dict(accepted=False,failure=repr(error),path=str(OUT/'stop-check.failure.json')))
        raise
