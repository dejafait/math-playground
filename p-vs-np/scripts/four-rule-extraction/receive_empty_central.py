"""Independent complete receiver; no constructor, filter or selector imports.

The reference is L035 (4) over ALL received edge pairs, calculated from
original-only subpath sums. No allocated old witness graph is assumed.
"""
from pathlib import Path
from collections import Counter
import hashlib
from parameterized_input import (CAPS,load,write_json,require,bound,request,
                                symbol_map,exact_equal,read_bytes)
from receive_parameterized import Arithmetic,topo
from verify_constant_translation import typed,normalized,nested_schedule
from verify_path_trimming import serial

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
OLD,OUT = HERE/'output-477',HERE/'output-479'


def main():
    path = OUT/'reception.json'
    require(not path.exists(), 'refuse existing receipt')
    receipt = dict(accepted=False,failures=[],complete_KH_received=False,
                   scope='isolated event 219 only; no integrated constructor change')
    ar = None
    try:
        req,raw,rows,checked = request(OLD/'inputs/proof.jsonl',OLD/'inputs/request.json')
        cert,inventory,candidate = (load(OUT/p) for p in ('inputs.json','inventory.json','candidate.json'))
        transport = symbol_map(req['alphabet'],req['dictionary'])
        ar = Arithmetic(req)
        for obj in (cert,candidate):
            require(exact_equal(obj['caps'],CAPS) and
                    exact_equal(obj['alphabet'],req['alphabet']) and
                    exact_equal(obj['dictionary'],req['dictionary']), 'full names/dictionary/caps')
        event,parent = load(OLD/'trace/event-00219.json'),load(OLD/'trace/event-00196.json')
        frame = load(OLD/'failure-frame-9.json')
        require(exact_equal(cert['original_event'],event) and exact_equal(cert['parent'],parent)
                and exact_equal(cert['frame'],frame), 'complete saved inputs')
        jobs = nested_schedule(normalized(parent['graph']))
        require(event['parent']==196 and event['entry']=='m.witness' and
                exact_equal([event['f'],event['g']],list(jobs[11])), 'exact ordered original recipe')
        original_frame = load(OLD/'failure-frame-8.json')
        require(all(exact_equal(event[k],original_frame[k]) for k in ('f','g')),
                'original failure frame')
        stop = load(OLD/'stop-check.json')
        integration = load(OLD/'integration-reception.json')
        require(stop['verified_resource_stop'] is True and stop['failed_event']==219 and
                stop['boolean_parent']==196 and stop['rejected_ledger']['actual']==3586238 and
                not stop['failures'] and integration['complete_trace_prefix_received'] is True and
                integration['events']==220 and not integration['failures'], 'prior stop/receipt scope')
        manifest = load(OLD/'inputs/manifest.json')
        for k in ('source','annotations','pair','proof','request'):
            name = k+('.jsonl' if k=='proof' else '.json')
            origin = HERE/('output-470' if k in ('proof','request') else
                          'output-461/final/empty-clause')/name
            data = read_bytes(OLD/'inputs'/name,'input_bytes')
            require(data==read_bytes(origin,'input_bytes') and
                    hashlib.sha256(data).hexdigest()==manifest[k], 'exact retained caller bytes')
        for p,digest in cert['input_hashes'].items():
            require(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==digest, 'preserved input '+p)
        # Independent all-pairs Boolean closure, then literal occurrence-map reception.
        graphs,polys,restriction_evidence = [],[],{}
        for key in ('f','g'):
            item = event['restrictions'][key]
            h,z = item['original'],item['trimmed']
            require(exact_equal(h,event[key]) and exact_equal(z,frame[key]), 'exact operand provenance')
            n,s,t = h['vertices'],h['source'],h['sink']
            reach = [[u==v for v in range(n)] for u in range(n)]
            for u,v,_ in h['edges']:
                reach[u][v]=True
            for k in range(n):
                for u in range(n):
                    if reach[u][k]:
                        for v in range(n):
                            reach[u][v] = reach[u][v] or reach[k][v]
            kept = [u for u in range(n) if reach[s][u] and reach[u][t]] if reach[s][t] else sorted({s,t})
            indices = [i for i,(u,v,_) in enumerate(h['edges']) if reach[s][u] and reach[v][t]]
            mapping = [kept.index(u) if u in kept else None for u in range(n)]
            expected = dict(vertices=len(kept),source=mapping[s],sink=mapping[t],
                        edges=[[mapping[h['edges'][i][0]],mapping[h['edges'][i][1]],h['edges'][i][2]]
                               for i in indices])
            require(exact_equal(mapping,item['old_to_new']) and exact_equal(kept,item['new_to_old'])
                    and exact_equal(indices,item['retained_edge_indices']) and
                    item['no_path'] is (not reach[s][t]) and exact_equal(z,expected), 'complete restrictions')
            values=[]
            for hh in (h,z):
                require(all(x=='1' or x in {'x%d'%(i+1) for i in range(len(req['alphabet']))}
                            for _,_,lab in hh['edges'] for x in lab), 'original-only complete labels')
                zz=typed(hh,transport)
                order=topo(zz['vertices'],zz['edges'],req)
                values.append(ar.evaluate(zz['vertices'],zz['edges'],order,zz['source'],zz['sink'],'free'))
            require(values[0]==values[1], 'full operand polynomial equality')
            graphs.append(z); polys.append(values[1])
            restriction_evidence[key]=dict(original=serial(values[0]),trimmed=serial(values[1]))
        f,g=graphs
        # Build complete prefix/suffix subpath tables without any branch selection.
        tables=[]
        for h in graphs:
            z=typed(h,transport); order=topo(z['vertices'],z['edges'],req)
            prefix=[set() for _ in range(z['vertices'])]; prefix[z['source']]={()}
            outgoing=[[] for _ in prefix]
            for u,v,lab in z['edges']: outgoing[u].append((v,lab))
            for u in order:
                for v,lab in outgoing[u]:
                    prefix[v]=ar.add(prefix[v],ar.mul(prefix[u],ar.label(lab,'free')))
                bound(sum(map(len,prefix)),'stored_words','reference prefix tables')
            suffix=[set() for _ in prefix]
            for u in reversed(order):
                suffix[u]={()} if u==z['sink'] else set()
                for v,lab in outgoing[u]:
                    suffix[u]=ar.add(suffix[u],ar.mul(ar.label(lab,'free'),suffix[v]))
                bound(sum(map(len,prefix))+sum(map(len,suffix)),'stored_words','reference subpaths')
            tables.append((prefix,suffix))
        bound(sum(len(p) for tab in tables for direction in tab for p in direction),
              'stored_words','all retained reference subpaths')
        reference=set(); allpairs=[]
        # Receiver coefficient rule uses typed dictionary originals, not emitter token parsing.
        pair_id={tuple(req['alphabet'].index(x) for x in p['originals']):i
                 for i,p in enumerate(req['dictionary']['placeholders']) if p['kind']=='commutator'}
        for i,(u,v,elab) in enumerate(f['edges']):
            for j,(a,b,dlab) in enumerate(g['edges']):
                central=[]
                for x in elab:
                    for y in dlab:
                        xx,yy=transport[x],transport[y]
                        if xx[0]=='original' and yy[0]=='original' and xx[1]!=yy[1]:
                            central.append(['placeholder',pair_id[tuple(sorted((xx[1],yy[1])))]])
                term=ar.mul(tables[0][0][u],tables[1][0][a])
                term=ar.mul(term,ar.label(central,'free'))
                term=ar.mul(term,tables[1][1][b])
                term=ar.mul(term,tables[0][1][v])
                reference=ar.add(reference,term)
                allpairs.append(dict(f_edge=i,g_edge=j,central=central,polynomial=serial(term)))
        write_json(OUT/'reference.json',dict(all_pairs=allpairs,polynomial=serial(reference),
            operand_subpaths=[dict(prefix=[serial(p) for p in a],suffix=[serial(p) for p in b]) for a,b in tables]))
        require(len(inventory['pairs'])==len(allpairs), 'full all-pair inventory length')
        out=candidate['graph']; edges=out['edges']; cursor=0; vertex=2; branch=0; q=0
        for expected,listed in zip(allpairs,inventory['pairs']):
            i,j=expected['f_edge'],expected['g_edge']; central=expected['central']
            require((listed['f_edge'],listed['g_edge'])==(i,j) and
                    exact_equal([transport[x] for x in listed['central']],central), 'every literal central list')
            q+=len(central)
            if not central:
                continue
            p=candidate['branches'][branch]; branch+=1
            require((p['f_edge'],p['g_edge'])==(i,j) and len(p['copies'])==4, 'retained pair occurrence/order')
            u,v,_=f['edges'][i]; a,b,_=g['edges'][j]
            roots=[]
            for part,h,s,t in zip(p['copies'],(f,g,g,f),(f['source'],g['source'],b,v),
                                  (u,a,g['sink'],f['sink'])):
                end=cursor+len(h['edges']); hi=vertex+h['vertices']
                require(part==dict(vertex_range=[vertex,hi],edge_range=[cursor,end],
                                   entry=vertex+s,exit=vertex+t), 'exact complete four-copy partition')
                require(exact_equal(edges[cursor:end],[[vertex+x,vertex+y,lab] for x,y,lab in h['edges']]),
                        'every copied endpoint/label occurrence')
                roots.append((vertex+s,vertex+t)); cursor=end; vertex=hi
            fp,gp,gs,fs=roots
            connectors=[[0,fp[0],['1']],[fp[1],gp[0],['1']],[gs[1],fs[0],['1']],[fs[1],1,['1']]]
            end=cursor+4+len(central)
            require(p['connecting_edges']==[cursor,end] and exact_equal(edges[cursor:cursor+4],connectors)
                    and exact_equal([[x,y,[transport[t] for t in lab]] for x,y,lab in edges[cursor+4:end]],
                                    [[gp[1],gs[0],[c]] for c in central]), 'complete connector/central partition')
            cursor=end
        require(branch==len(candidate['branches']) and vertex==out['vertices'] and cursor==len(edges)
                and out['source']==0 and out['sink']==1, 'all records accounted for')
        # Independent count from input totals and independently received inventory.
        nv=2+2*branch*(f['vertices']+g['vertices'])
        ne=2*branch*(len(f['edges'])+len(g['edges']))+4*branch+q
        ledger=dict(retained=branch,omitted=len(allpairs)-branch,central=q,vertices=nv,edges=ne,records=nv+ne)
        require((nv,ne)==(out['vertices'],len(edges)) and
                all(inventory[k]==v for k,v in ledger.items() if k!='omitted') and
                inventory['required']==CAPS['records'], 'independent selected ledger')
        z=typed(out,transport); order=topo(nv,z['edges'],req)
        values={mode:ar.evaluate(nv,z['edges'],order,0,1,mode) for mode in ('free','zero','axioms')}
        target=ar.add(ar.mul(polys[0],polys[1]),ar.mul(polys[1],polys[0]))
        require(values['free']==reference and not values['zero'] and values['axioms']==target,
                'full free / zero / substituted equalities')
        prior=load(OLD/'trace-received-prefix.json')['events'][219]
        require(exact_equal(serial(target),prior['target']), 'nonzero original target binding')
        # Path-count sets disregard cancellation and zero polynomial values.
        states=[set() for _ in range(nv)]; states[0]={0}
        adj=[[] for _ in range(nv)]
        for u,v,lab in z['edges']: adj[u].append((v,lab))
        for u in order:
            for v,lab in adj[u]:
                kinds={x[0]=='placeholder' for x in lab}
                require(len(kinds)<=1, 'single-kind label')
                # Empty-labelled copied edges are still structural graph paths.
                increment=1 if kinds=={True} else 0
                states[v].update(k+increment for k in states[u])
                require(all(k<=1 for k in states[v]), 'no path uses two placeholders')
        require(states[1]=={1}, 'every accepting path uses exactly one placeholder')
        label_entries=sum(len(lab) for _,_,lab in edges)
        name_bytes=sum(len(x.encode()) for x in req['alphabet'])+sum(len(p['name'].encode()) for p in req['dictionary']['placeholders'])
        charges=dict(label_entries=label_entries,complete_name_bytes=name_bytes,
                     root_references=[0,1],dictionary_entries=len(req['dictionary']['placeholders']),
                     candidate_serialized_bytes=(OUT/'candidate.json').stat().st_size,
                     files={p.name:p.stat().st_size for p in sorted(OUT.iterdir()) if p.is_file()})
        bound(charges['candidate_serialized_bytes'],'certificate_bytes','complete candidate encoding')
        bound(sum(charges['files'].values()),'certificate_bytes','aggregate current evidence bytes')
        receipt.update(accepted=True,ledger=ledger,charges=charges,caps=CAPS,
            arithmetic=ar.counts,polynomials={k:serial(p) for k,p in values.items()},target=serial(target),
            operands=restriction_evidence,all_pairs_received=len(allpairs),
            full_free_reference_received=True,literal_copy_partitions_received=True,
            structural_placeholder_counts=sorted(states[1]),original_recipe_job=11,
            caller_bytes_preserved=True,input_hashes=cert['input_hashes'],source_check=checked)
    except Exception as exc:
        receipt['failures'].append(repr(exc))
        if ar is not None: receipt['arithmetic']=ar.counts
        write_json(path,receipt)
        raise
    write_json(path,receipt)
    total=sum(p.stat().st_size for p in OUT.iterdir() if p.is_file())
    bound(total,'certificate_bytes','aggregate final evidence including receipt')
    print(dict(accepted=True,actual=ledger['records'],required=CAPS['records'],retained=branch,
               free_words=len(reference),target_words=len(target),bytes=total,
               failures=[],path=str(path)))


if __name__=='__main__':
    main()
