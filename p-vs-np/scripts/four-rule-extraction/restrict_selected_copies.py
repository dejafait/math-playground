"""Step 493: isolated four-copy endpoint restriction, never integration.

The old complete job ledger is an input, not an acceptance oracle. A separate
receiver reconstructs its recipes, all restrictions and the full polynomial.
"""
from pathlib import Path
import hashlib
from parameterized_input import CAPS, load, request, require, exact_equal, bound
from receive_selected_commutator import install_evidence_budget
from trim_saved_operands import trim
from verify_constant_translation import normalized, atom, root

HERE = Path(__file__).resolve().parent
OLD = HERE/'output-489'
OUT = HERE/'output-493'
TARGET = ('Test trimming each selected L035 copy to its designated entry-to-exit '
          'paths in the record-78 Boolean witness, preserving its complete free '
          'polynomial under the unchanged caps.')


def restriction(g, s, t):
    r = trim(dict(g, source=s, sink=t))
    return dict(entry=s, exit=t, old_to_new=r['old_to_new'],
                new_to_old=r['new_to_old'], retained_edges=r['retained_edge_indices'],
                deleted_vertices=[i for i,v in enumerate(r['old_to_new']) if v is None],
                deleted_edges=[i for i in range(len(g['edges']))
                               if i not in set(r['retained_edge_indices'])],
                no_path=r['no_path'], transported_entry=r['trimmed']['source'],
                transported_exit=r['trimmed']['sink'])


def embedded(edges, g, offset):
    edges.extend([u+offset,v+offset,list(l)] for u,v,l in g['edges'])
    return offset+g['source'], offset+g['sink']


def main():
    require(not OUT.exists(), 'refuse existing output')
    OUT.mkdir()
    write = install_evidence_budget(OUT)
    req, raw, rows, checked = request(OLD/'inputs/proof.jsonl', OLD/'inputs/request.json')
    event = load(OLD/'trace/event-02643.json')
    translation = load(OLD/'trace/event-02642.json')
    require(checked['records']==212 and checked['sha256']==
            'f779fa52af4eb63805e45aa9940620be1cd3ce6c993ff4a903a996a0b539c74e'
            and event['kind']=='boolean-input' and translation['kind']=='translation'
            and rows[78]['rule']=='axiom'
            and exact_equal(translation['formula'],rows[78]['f'][2])
            and exact_equal(translation['graph'],event['graph']), 'fixed source binding')
    prior = load(HERE/'output-491/retained-interior-bound.json')
    h = normalized(event['graph'])
    require(exact_equal(h,prior['normalized']) and exact_equal(prior['caps'],CAPS)
            and exact_equal(prior['alphabet'],req['alphabet'])
            and exact_equal(prior['dictionary'],req['dictionary']), 'unchanged prior framing')
    files = [OLD/p for p in ('inputs/proof.jsonl','inputs/request.json',
                             'trace/event-02642.json','trace/event-02643.json')]
    files += [HERE/'output-491/retained-interior-bound.json',
              HERE/'output-491/bound-reception.json',Path(__file__)]
    cert = dict(target=TARGET,caps=CAPS,alphabet=req['alphabet'],dictionary=req['dictionary'],
                checked_source=checked,source_record=78,boolean_event=2643,normalized=h,
                jobs=[],input_hashes={str(p.relative_to(HERE)):
                    hashlib.sha256(p.read_bytes()).hexdigest() for p in files},
                scope='Isolated internal restriction only; external L036 recipe unchanged.')
    write(OUT/'checkpoint.json',cert)
    for old in prior['jobs']:
        a,b = [r['trimmed'] for r in old['restrictions']]
        job = dict(index=old['index'],vertex=old['vertex'],kind=old['kind'],
                   edge_occurrences=old['edge_occurrences'],restrictions=old['restrictions'],
                   selected=[],vertices=2,edges=0,label_entries=0)
        for p in old['selected']:
            u,v,_=a['edges'][p['f_edge']]; c,d,_=b['edges'][p['g_edge']]
            copies=[restriction(z,s,t) for z,s,t in
                    ((a,a['source'],u),(b,b['source'],c),
                     (b,d,b['sink']),(a,v,a['sink']))]
            job['selected'].append(dict(p,copies=copies))
            job['vertices'] += sum(len(x['new_to_old']) for x in copies)
            job['edges'] += sum(len(x['retained_edges']) for x in copies)+4+len(p['central'])
            job['label_entries'] += sum(sum(len(z['edges'][i][2]) for i in x['retained_edges'])
                                       for x,z in zip(copies,(a,b,b,a)))+4+len(p['central'])
        job['records']=job['vertices']+job['edges']
        cert['jobs'].append(job)
    totals = {k:sum(j[k] for j in cert['jobs'])
              for k in ('vertices','edges','records','label_entries')}
    cert['restricted_interiors']=totals
    cert['fits_necessary_bound']=totals['records']<=CAPS['records']
    write(OUT/'restricted-interior-bound.json',cert)
    print(dict(stage='complete interior inventory',jobs=len(cert['jobs']),
               actual=totals['records'],required=CAPS['records'],
               label_entries=totals['label_entries'],failures=[],
               path=str(OUT/'restricted-interior-bound.json')),flush=True)
    if not cert['fits_necessary_bound']:
        return
    # Exact full external recipe count, before allocating the Boolean graph.
    nv,ne,nl = h['vertices']+1,len(h['edges']),sum(len(l) for _,_,l in h['edges'])
    jobs_by_key={(j['kind'],tuple(j['edge_occurrences'])):j for j in cert['jobs']}
    recipe=[]
    for u in range(h['vertices']):
        outgoing=[(i,v,l[0]) for i,(z,v,l) in enumerate(h['edges']) if z==u]
        for i,v,x in outgoing:
            if x!='1':
                factors=[atom('b:'+x[1:]),root(h,v),root(h,v)]
                recipe.append((u,'edge_boolean',None,factors))
                nv+=2+sum(z['vertices'] for z in factors)
                ne+=6+sum(len(z['edges']) for z in factors)
                nl+=6+sum(len(l) for z in factors for _,_,l in z['edges'])
            job=jobs_by_key['product_commutator',(i,)]
            recipe.append((u,'product_commutator',job,[atom(x),None,root(h,v)]))
            nv+=2+2+job['vertices']+h['vertices']
            ne+=6+1+job['edges']+len(h['edges'])
            nl+=6+1+job['label_entries']+sum(len(l) for _,_,l in h['edges'])
        for pos,(i,v,x) in enumerate(outgoing):
            for j,w,y in outgoing[pos+1:]:
                job=jobs_by_key['sum_commutator',(i,j)]
                recipe.append((u,'sum_commutator',job,None))
                nv+=job['vertices']; ne+=job['edges']+2; nl+=job['label_entries']+2
    ledger=dict(vertices=nv,edges=ne,records=nv+ne,label_entries=nl,
                required_records=CAPS['records'],required_label_entries=CAPS['label_entries'])
    write(OUT/'full-count.json',ledger)
    bound(nv+ne,'records','complete isolated Boolean preflight')
    bound(nl,'label_entries','complete isolated Boolean label preflight')
    for job in cert['jobs']:
        a,b=[r['trimmed'] for r in job['restrictions']]
        edges=[]; vertex=2
        for p in job['selected']:
            roots=[]
            for x,z in zip(p['copies'],(a,b,b,a)):
                lo,cursor=vertex,len(edges)
                mapping=x['old_to_new']
                edges.extend([lo+mapping[z['edges'][i][0]],lo+mapping[z['edges'][i][1]],
                              list(z['edges'][i][2])] for i in x['retained_edges'])
                vertex+=len(x['new_to_old'])
                s,t=lo+x['transported_entry'],lo+x['transported_exit']
                x.update(vertex_range=[lo,vertex],edge_range=[cursor,len(edges)])
                roots.append((s,t))
            fp,gp,gs,fs=roots
            p['connecting_edges']=[len(edges),len(edges)+4+len(p['central'])]
            edges.extend([[0,fp[0],['1']],[fp[1],gp[0],['1']],
                          [gs[1],fs[0],['1']],[fs[1],1,['1']]])
            edges.extend([gp[1],gs[0],[x]] for x in p['central'])
        job['graph']=dict(vertices=vertex,source=0,sink=1,edges=edges)
        require(vertex==job['vertices'] and len(edges)==job['edges'], 'constructed interior ledger')
    edges=[[u,v,list(l)] for u,v,l in h['edges']]; vertex=h['vertices']+1
    attachments=[]
    for u,kind,job,factors in recipe:
        lo,cursor=vertex,len(edges)
        if kind=='sum_commutator':
            z=job['graph']; s,t=embedded(edges,z,vertex); vertex+=z['vertices']
        else:
            factors=[job['graph'] if z is None else z for z in factors]
            s,t=vertex,vertex+1; vertex+=2; last=s
            for z in factors:
                cs,ct=embedded(edges,z,vertex)
                edges.append([last,cs,['1']]); last=ct; vertex+=z['vertices']
            edges.append([last,t,['1']])
        edges.extend([[u,s,['1']],[t,h['vertices'],['1']]])
        attachments.append(dict(vertex=u,kind=kind,job=None if job is None else job['index'],
                                vertex_range=[lo,vertex],edge_range=[cursor,len(edges)]))
    cert.update(graph=dict(vertices=vertex,source=h['source'],sink=h['vertices'],edges=edges),
                attachments=attachments,full_count=ledger,complete_KH_received=False)
    require(vertex==nv and len(edges)==ne,'complete allocated ledger')
    write(OUT/'restricted-boolean.json',cert)
    print(dict(stage='constructed isolated Boolean',records=nv+ne,required=CAPS['records'],
               label_entries=nl,failures=[],path=str(OUT/'restricted-boolean.json')),flush=True)


if __name__=='__main__':
    main()
