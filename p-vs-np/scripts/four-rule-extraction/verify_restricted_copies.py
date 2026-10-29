"""Independent step-493 receiver. Imports no constructor or path filter.

Rebuilds all recipes and endpoint cuts by bitset transitive closure, receives
every graph occurrence, and evaluates the full L035/L036 free references.
"""
from collections import Counter
from pathlib import Path
import hashlib
from parameterized_input import (CAPS, load, request, require, exact_equal,
                                bound, symbol_map, Rejected)
from receive_parameterized import Arithmetic, topo, serial
from receive_selected_commutator import install_evidence_budget

HERE=Path(__file__).resolve().parent
OLD=HERE/'output-489'
OUT=HERE/'output-493'
MODES=('free','zero','axioms')
TARGET=('Test trimming each selected L035 copy to its designated entry-to-exit '
        'paths in the record-78 Boolean witness, preserving its complete free '
        'polynomial under the unchanged caps.')


class IncrementalArithmetic(Arithmetic):
    """Same ordered pair operations/caps/counters; no repeated set-length scan.

    Each new word's length is checked before concatenation. Deleting a word
    cannot increase size or length. Global maxima therefore need updates only
    on insertion. The final inherited check is retained, including empty sets.
    """
    def mul(self,a,b):
        self.counts['multiplication_pairs']+=len(a)*len(b)
        bound(self.counts['multiplication_pairs'],'multiplication_pairs','before multiplication')
        out=set()
        for u in a:
            for v in b:
                length=len(u)+len(v)
                bound(length,'word_length','before concatenation')
                w=u+v
                if w in out:
                    out.remove(w)
                else:
                    bound(len(out)+1,'polynomial_words','multiplication before insertion')
                    out.add(w)
                    self.counts['max_polynomial_words']=max(len(out),self.counts['max_polynomial_words'])
                    self.counts['max_word_length']=max(length,self.counts['max_word_length'])
        return self.check(out)


def main():
    require(not (OUT/'reception.json').exists() and not (OUT/'reception.failure.json').exists(),
            'refuse prior reception')
    write=install_evidence_budget(OUT)
    stage='input'
    ar=None
    try:
        cert=load(OUT/'restricted-boolean.json')
        inventory=load(OUT/'restricted-interior-bound.json')
        req,raw,rows,checked=request(OLD/'inputs/proof.jsonl',OLD/'inputs/request.json')
        event=load(OLD/'trace/event-02643.json')
        translation=load(OLD/'trace/event-02642.json')
        transport=symbol_map(req['alphabet'],req['dictionary'])
        ar=IncrementalArithmetic(req)
        # Diagnostic against the inherited engine; the invariant in the class
        # docstring, not this finite comparison, justifies the implementation.
        x=('original',0); y=('original',1)
        cases=[(set(),{()}),({()},{()}),({(),(x,)},{(),(x,)}),
               ({(x,),(y,),(x,y)},{(),(x,),(y,)}),
               ({tuple([x]*257)},{()}),({tuple([x]*257)},set())]
        checks=[]
        for i,(a,b) in enumerate(cases+[(set(),set())]):
            results=[]
            for cls in (Arithmetic,IncrementalArithmetic):
                test=cls(req)
                if i==len(cases): test.counts['multiplication_pairs']=CAPS['multiplication_pairs']+1
                try: result=dict(polynomial=serial(test.mul(a,b)),error=None)
                except Rejected as exc: result=dict(polynomial=None,error=str(exc))
                results.append(dict(result,counters=test.counts))
            require(exact_equal(results[0],results[1]),'incremental engine diagnostic equivalence')
            checks.append(dict(case=i,left=serial(a),right=serial(b),result=results[0]))
        write(OUT/'arithmetic-equivalence.json',dict(cases=checks,failures=[],
              unchanged_caps=CAPS,scope='Finite diagnostics; general invariant stated in receiver and L097.'))
        require(cert['target']==inventory['target']==TARGET
                and exact_equal(cert['caps'],CAPS) and exact_equal(inventory['caps'],CAPS)
                and exact_equal(cert['alphabet'],req['alphabet'])
                and exact_equal(cert['dictionary'],req['dictionary'])
                and exact_equal(cert['checked_source'],checked), 'unchanged target/framing/source')
        for name,digest in cert['input_hashes'].items():
            require(hashlib.sha256((HERE/name).read_bytes()).hexdigest()==digest,
                    'retained complete input bytes')
        require(cert['source_record']==78 and cert['boolean_event']==2643
                and checked['records']==212 and checked['sha256']==
                'f779fa52af4eb63805e45aa9940620be1cd3ce6c993ff4a903a996a0b539c74e'
                and rows[78]['rule']=='axiom' and translation['kind']=='translation'
                and event['kind']=='boolean-input'
                and exact_equal(translation['formula'],rows[78]['f'][2])
                and exact_equal(translation['graph'],event['graph']), 'source row/event binding')
        prior=load(HERE/'output-491/retained-interior-bound.json')
        prior_receipt=load(HERE/'output-491/bound-reception.json')
        require(prior_receipt['complete_recipe_and_occurrences_received'] is True,
                'prior complete bound receipt retained, not used as current oracle')
        g=event['graph']
        normalized_edges=[]
        for u,v,lab in g['edges']:
            if u!=g['sink']:
                normalized_edges.extend([u,v,[x]] for x,n in sorted(Counter(lab).items()) if n%2)
        h=dict(g,edges=normalized_edges)
        require(exact_equal(h,cert['normalized']) and exact_equal(h,inventory['normalized'])
                and (h['vertices'],h['source'],h['sink'],len(h['edges']))==(154,0,1,199),
                'complete independent normalization')

        def typed(z,original=False):
            require(set(z)=={'vertices','source','sink','edges'}, 'graph fields')
            n=z['vertices']
            require(type(n) is int and type(z['source']) is int and type(z['sink']) is int
                    and 0<=z['source']<n and 0<=z['sink']<n,'graph roots')
            edges=[]
            for u,v,lab in z['edges']:
                require(all(x in transport for x in lab),'declared full dictionary')
                symbols=[transport[x] for x in lab]
                require(not original or all(x[0] in ('one','original') for x in symbols),
                        'original labels including dead occurrences')
                edges.append([u,v,symbols])
            return edges,topo(n,edges,req)

        def evaluate(z,modes=MODES):
            edges,order=typed(z)
            return {m:ar.evaluate(z['vertices'],edges,order,z['source'],z['sink'],m) for m in modes}

        value=evaluate(g,('free',))['free']
        require(value==evaluate(h,('free',))['free']==ar.translation(rows[78]['f'][2]),
                'complete actual input translation polynomial')

        def closure(z):
            typed(z,original=True)
            n=z['vertices']; reach=[1<<i for i in range(n)]
            for u,v,_ in z['edges']: reach[u]|=1<<v
            for k in range(n):
                bit=1<<k
                for u in range(n):
                    if reach[u]&bit: reach[u]|=reach[k]
            return reach

        def cut(z,s,t,reach):
            n=z['vertices']; no_path=not bool(reach[s]&(1<<t))
            live=sorted({s,t}) if no_path else [v for v in range(n)
                    if reach[s]&(1<<v) and reach[v]&(1<<t)]
            ranks={v:i for i,v in enumerate(live)}
            mapping=[ranks.get(v) for v in range(n)]
            indices=[i for i,(u,v,_) in enumerate(z['edges']) if not no_path
                     and reach[s]&(1<<u) and reach[v]&(1<<t)]
            retained=set(indices)
            metadata=dict(entry=s,exit=t,old_to_new=mapping,new_to_old=live,
                          retained_edges=indices,deleted_vertices=[v for v in range(n) if v not in ranks],
                          deleted_edges=[i for i in range(len(z['edges'])) if i not in retained],
                          no_path=no_path,transported_entry=mapping[s],transported_exit=mapping[t])
            result=dict(vertices=len(live),source=mapping[s],sink=mapping[t],
                        edges=[[mapping[z['edges'][i][0]],mapping[z['edges'][i][1]],
                                z['edges'][i][2]] for i in indices])
            return metadata,result

        def whole(z,saved):
            metadata,out=cut(z,z['source'],z['sink'],closure(z))
            expected=dict(original=z,trimmed=out,old_to_new=metadata['old_to_new'],
                          new_to_old=metadata['new_to_old'],
                          retained_edge_indices=metadata['retained_edges'],no_path=metadata['no_path'])
            require(exact_equal(saved,expected),'complete original whole-operand restriction')
            typed(out,True)
            return out

        jobs=[]; attachments=[]
        for u in range(h['vertices']):
            outgoing=[(i,v,lab[0]) for i,(z,v,lab) in enumerate(h['edges']) if z==u]
            for i,v,x in outgoing:
                if x!='1': attachments.append((u,'edge_boolean',None,i,v,x))
                index=len(jobs)
                jobs.append((u,'product_commutator',[i],
                             dict(vertices=2,source=0,sink=1,edges=[[0,1,[x]]]),dict(h,source=v)))
                attachments.append((u,'product_commutator',index,i,v,x))
            for pos,(i,v,x) in enumerate(outgoing):
                for j,w,y in outgoing[pos+1:]:
                    index=len(jobs)
                    f=dict(h,vertices=h['vertices']+1,source=h['vertices'],
                           edges=h['edges']+[[h['vertices'],v,[x]]])
                    b=dict(h,vertices=h['vertices']+1,source=h['vertices'],
                           edges=h['edges']+[[h['vertices'],w,[y]]])
                    jobs.append((u,'sum_commutator',[i,j],f,b))
                    attachments.append((u,'sum_commutator',index,None,None,None))
        require(len(jobs)==245==len(cert['jobs'])==len(inventory['jobs'])==len(prior['jobs']),
                'all jobs including beyond the old stopping point')
        refs=OUT/'references-received'
        require(not refs.exists(),'preserve interrupted references and refuse new overwrite')
        refs.mkdir()
        totals=Counter(); kind_counts=Counter(); copy_cases=Counter(); details=[]
        polynomials=[]; all_pair_count=0; selected_count=0

        def tables(z):
            edges,order=typed(z,True); adj=[[] for _ in range(z['vertices'])]
            for u,v,lab in edges: adj[u].append((v,lab))
            p=[set() for _ in adj]; p[z['source']]={()}
            for u in order:
                for v,lab in adj[u]: p[v]=ar.add(p[v],ar.mul(p[u],ar.label(lab,'free')))
                bound(sum(map(len,p)),'stored_words','complete prefix reference table')
            q=[set() for _ in adj]
            for u in reversed(order):
                q[u]={()} if u==z['sink'] else set()
                for v,lab in adj[u]: q[u]=ar.add(q[u],ar.mul(ar.label(lab,'free'),q[v]))
                bound(sum(map(len,p))+sum(map(len,q)),'stored_words','complete suffix reference table')
            return p,q

        for index,((u,kind,occurrences,f,g),item,old,counted) in enumerate(
                zip(jobs,cert['jobs'],prior['jobs'],inventory['jobs'])):
            stage='job '+str(index)
            require((item['index'],item['vertex'],item['kind'],item['edge_occurrences'])==
                    (index,u,kind,occurrences),'complete ordered source occurrences')
            require(len(item['restrictions'])==2,'both original restrictions')
            a,b=[whole(z,r) for z,r in zip((f,g),item['restrictions'])]
            require(exact_equal(item['restrictions'],old['restrictions']) and
                    exact_equal(item['restrictions'],counted['restrictions']),'old operand interface fixed')
            reach=[closure(z) for z in (a,b)]
            expected_pairs=[]; pairs=0
            for i,(_,_,al) in enumerate(a['edges']):
                for j,(_,_,bl) in enumerate(b['edges']):
                    pairs+=1; labels=[]
                    for x in al:
                        for y in bl:
                            xx,yy=transport[x],transport[y]
                            if xx[0]==yy[0]=='original' and xx[1]!=yy[1]:
                                lo,hi=sorted((xx[1]+1,yy[1]+1)); labels.append('t:%d:%d'%(lo,hi))
                    if labels: expected_pairs.append(dict(f_edge=i,g_edge=j,central=labels))
            bound(pairs,'records','complete all-pair inventory')
            require(exact_equal(expected_pairs,old['selected']) and
                    len(expected_pairs)==len(item['selected'])==len(counted['selected']),
                    'all literal selections and central multiplicities unchanged')
            out=item['graph']; edges=out['edges']; vertex,cursor=2,0
            for pair,part,countpart in zip(expected_pairs,item['selected'],counted['selected']):
                require(exact_equal(pair,{k:part[k] for k in ('f_edge','g_edge','central')}),
                        'selected pair order and labels')
                i,j=pair['f_edge'],pair['g_edge']
                au,av,_=a['edges'][i]; bu,bv,_=b['edges'][j]
                require(len(part['copies'])==4,'four separate internal copies')
                roots=[]
                for ci,(z,s,t,r) in enumerate(((a,a['source'],au,reach[0]),
                         (b,b['source'],bu,reach[1]),(b,bv,b['sink'],reach[1]),
                         (a,av,a['sink'],reach[0]))):
                    expected,child=cut(z,s,t,r)
                    require(exact_equal(expected,countpart['copies'][ci]),'complete preallocation map')
                    expected.update(vertex_range=[vertex,vertex+child['vertices']],
                                    edge_range=[cursor,cursor+len(child['edges'])])
                    require(exact_equal(expected,part['copies'][ci]),'all retained/deleted occurrences and roots')
                    for cu,cv,lab in child['edges']:
                        require(cursor<len(edges) and exact_equal(edges[cursor],
                                [vertex+cu,vertex+cv,lab]),'every internal copied edge/label occurrence')
                        cursor+=1
                    roots.append((vertex+child['source'],vertex+child['sink']))
                    vertex+=child['vertices']
                    copy_cases['copies']+=1
                    copy_cases['coincident_roots' if s==t else 'distinct_roots']+=1
                    copy_cases['no_path' if expected['no_path'] else 'path_exists']+=1
                fp,gp,gs,fs=roots
                connectors=[[0,fp[0],['1']],[fp[1],gp[0],['1']],
                            [gs[1],fs[0],['1']],[fs[1],1,['1']]]
                end=cursor+4+len(pair['central'])
                require(part['connecting_edges']==[cursor,end] and
                        exact_equal(edges[cursor:cursor+4],connectors) and
                        exact_equal(edges[cursor+4:end],[[gp[1],gs[0],[x]] for x in pair['central']]),
                        'every exterior connector and central occurrence, no cross-copy additions')
                cursor=end
            require(vertex==out['vertices'] and cursor==len(edges)
                    and out['source']==0 and out['sink']==1,'entire W partition exhausted')
            actual=dict(vertices=vertex,edges=cursor,records=vertex+cursor,
                        label_entries=sum(len(l) for _,_,l in edges))
            require(all(item[k]==counted[k]==v for k,v in actual.items()),'independent exact interior ledger')
            totals.update(actual); kind_counts[kind]+=1
            # Complete reference (4), independent of the changed graph. Empty
            # central lists contribute exactly zero in every mode, without PIT.
            tab=[tables(z) for z in (a,b)]
            reference={m:set() for m in MODES}; terms=[]; retained=0
            table_words=sum(len(p) for t in tab for row in t for p in row)
            for pair in expected_pairs:
                au,av,_=a['edges'][pair['f_edge']]; bu,bv,_=b['edges'][pair['g_edge']]
                left=ar.mul(tab[0][0][au],tab[1][0][bu])
                term={}
                for mode in MODES:
                    p=ar.mul(left,ar.label([transport[x] for x in pair['central']],mode))
                    p=ar.mul(p,tab[1][1][bv]); p=ar.mul(p,tab[0][1][av])
                    reference[mode]=ar.add(reference[mode],p); term[mode]=p
                retained+=sum(map(len,term.values()))
                bound(table_words+retained+sum(map(len,reference.values())),
                      'stored_words','complete retained all-pair reference evidence')
                terms.append(dict(pair,polynomials={m:serial(p) for m,p in term.items()}))
            received=evaluate(out)
            require(all(received[m]==reference[m] for m in MODES),'full free/zero/substituted W equalities')
            fa,gb=tab[0][1][a['source']],tab[1][1][b['source']]
            require(not reference['zero'] and reference['axioms']==
                    ar.add(ar.mul(fa,gb),ar.mul(gb,fa)),'unchanged W substitution identity')
            polynomials.append(reference)
            all_pair_count+=pairs; selected_count+=len(expected_pairs)
            ref=dict(index=index,all_pair_count=pairs,empty_central_count=pairs-len(expected_pairs),
                     selected_terms=terms,polynomials={m:serial(p) for m,p in reference.items()},
                     operand_subpaths=[dict(prefix=[serial(p) for p in ps],suffix=[serial(p) for p in ss])
                                       for ps,ss in tab])
            write(refs/('job-%03d.json'%index),ref)
            details.append(dict(index=index,kind=kind,pairs=pairs,selected=len(expected_pairs),**actual))
        require(dict(totals)==cert['restricted_interiors']==inventory['restricted_interiors']
                and cert['fits_necessary_bound'] is True,'complete received interior counts')
        stage='outer occurrences'
        out=cert['graph']; edges=out['edges']; cursor=len(h['edges']); vertex=h['vertices']+1
        require(out['source']==h['source'] and out['sink']==h['vertices'] and
                exact_equal(edges[:cursor],h['edges']),'unchanged complete propagation graph')
        require(len(attachments)==len(cert['attachments']),'complete attachment schedule')

        def embedded(child,offset):
            nonlocal cursor
            for u,v,lab in child['edges']:
                require(cursor<len(edges) and exact_equal(edges[cursor],[offset+u,offset+v,lab]),
                        'every external L036 copied occurrence')
                cursor+=1
            return offset+child['source'],offset+child['sink']

        def atom(x): return dict(vertices=2,source=0,sink=1,edges=[[0,1,[x]]])

        for (u,kind,index,i,v,x),saved in zip(attachments,cert['attachments']):
            lo,first=vertex,cursor
            if kind=='sum_commutator':
                child=cert['jobs'][index]['graph']; s,t=embedded(child,vertex); vertex+=child['vertices']
            else:
                factors=([atom('b:'+x[1:]),dict(h,source=v),dict(h,source=v)] if kind=='edge_boolean'
                         else [atom(x),cert['jobs'][index]['graph'],dict(h,source=v)])
                s,t=vertex,vertex+1; vertex+=2; last=s
                for child in factors:
                    cs,ct=embedded(child,vertex)
                    require(exact_equal(edges[cursor],[last,cs,['1']]),'ordered external factor connector')
                    cursor+=1; last=ct; vertex+=child['vertices']
                require(exact_equal(edges[cursor],[last,t,['1']]),'external last connector'); cursor+=1
            require(exact_equal(edges[cursor:cursor+2],[[u,s,['1']],[t,out['sink'],['1']]]),
                    'external two attachment connectors'); cursor+=2
            require(exact_equal(saved,dict(vertex=u,kind=kind,job=index,vertex_range=[lo,vertex],
                                           edge_range=[first,cursor])),'all outer occurrence partitions')
        require(vertex==out['vertices'] and cursor==len(edges),'complete Boolean graph exhausted')
        ledger=dict(vertices=vertex,edges=cursor,records=vertex+cursor,
                    label_entries=sum(len(l) for _,_,l in edges),
                    required_records=CAPS['records'],required_label_entries=CAPS['label_entries'])
        require(exact_equal(ledger,cert['full_count']) and exact_equal(ledger,load(OUT/'full-count.json')),
                'complete independently reconstructed ledger')
        bound(ledger['records'],'records','received full Boolean records')
        bound(ledger['label_entries'],'label_entries','received full Boolean label entries')
        stage='complete L036 reference'
        ht=tables(h); suffix=ht[1]; local=[{m:set() for m in MODES} for _ in range(h['vertices'])]
        for u,kind,index,i,v,x in attachments:
            for mode in MODES:
                if kind=='sum_commutator': p=polynomials[index][mode]
                elif kind=='edge_boolean':
                    p=ar.mul(ar.label([transport['b:'+x[1:]]],mode),suffix[v]); p=ar.mul(p,suffix[v])
                else:
                    p=ar.mul(ar.label([transport[x]],mode),polynomials[index][mode]); p=ar.mul(p,suffix[v])
                local[u][mode]=ar.add(local[u][mode],p)
        hedges,order=typed(h,True); adjacency=[[] for _ in range(h['vertices'])]
        for u,v,lab in hedges: adjacency[u].append((v,lab))
        btable=[{m:set() for m in MODES} for _ in adjacency]
        for u in reversed(order):
            for mode in MODES:
                p=set(local[u][mode])
                for v,lab in adjacency[u]: p=ar.add(p,ar.mul(ar.label(lab,'free'),btable[v][mode]))
                btable[u][mode]=p
            bound(sum(len(p) for row in local+btable for p in row.values())+
                  sum(len(p) for row in polynomials for p in row.values()),
                  'stored_words','all complete retained Boolean references')
        reference=btable[h['source']]
        received=evaluate(out)
        require(all(received[m]==reference[m] for m in MODES),
                'complete unchanged L036 free/zero/substituted reference equality')
        target=ar.add(ar.mul(value,value),value)
        require(not received['zero'] and received['axioms']==target,'complete Boolean identities')
        stage='structural placeholder paths'
        typed_edges,order=typed(out)
        adj=[[] for _ in range(out['vertices'])]
        for u,v,lab in typed_edges: adj[u].append((v,lab))
        states=[set() for _ in adj]; states[out['source']]={0}
        for u in order:
            for v,lab in adj[u]:
                kinds={x[0]=='placeholder' for x in lab}
                require(len(kinds)<=1,'single-kind structural labels')
                increment=int(kinds=={True})
                states[v].update(k+increment for k in states[u])
                require(all(k<=1 for k in states[v]),'no reachable path takes two placeholders')
        require(states[out['sink']]<={1},'every accepting path takes one placeholder before cancellation')
        write(refs/'boolean.json',dict(local=[{m:serial(p) for m,p in r.items()} for r in local],
                    propagated=[{m:serial(p) for m,p in r.items()} for r in btable],
                    polynomials={m:serial(p) for m,p in reference.items()},target=serial(target)))
        receipt=dict(accepted_isolated_witness=True,failures=[],target=TARGET,caps=CAPS,
                     input_polynomial=serial(value),job_kinds=dict(kind_counts),jobs=details,
                     restricted_interiors=dict(totals),all_pairs=all_pair_count,
                     selected_pairs=selected_count,copy_cases=dict(copy_cases),attachments=len(attachments),
                     full_count=ledger,arithmetic=ar.counts,structural_counts=sorted(states[out['sink']]),
                     polynomials={m:serial(p) for m,p in received.items()},
                     complete_occurrence_maps_received=True,complete_free_reference_received=True,
                     complete_KH_received=False,nonzero_fJ_received=False,
                     independent_full_extraction_evidence_stop_repaired=False,
                     receiver_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
        write(OUT/'reception.json',receipt)
        used=sum(p.stat().st_size for p in OUT.rglob('*') if p.is_file())
        print(dict(accepted_isolated_witness=True,jobs=len(jobs),selected_pairs=selected_count,
                   copies=copy_cases['copies'],records=ledger['records'],required=CAPS['records'],
                   evidence_bytes=used,required_evidence_bytes=CAPS['certificate_bytes'],
                   arithmetic=ar.counts,failures=[],path=str(OUT/'reception.json')))
    except (Rejected,KeyError,IndexError,TypeError,ValueError) as exc:
        write(OUT/'reception.failure.json',dict(accepted_isolated_witness=False,stage=stage,
              error=str(exc),arithmetic=None if ar is None else ar.counts,complete_KH_received=False))
        print(dict(accepted_isolated_witness=False,stage=stage,error=str(exc),
                   path=str(OUT/'reception.failure.json')),flush=True)
        raise


if __name__=='__main__':
    main()
