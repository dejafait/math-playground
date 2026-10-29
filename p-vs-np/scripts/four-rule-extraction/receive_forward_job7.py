"""Step 495: isolated forward reception of the unchanged restricted job 7.

No emitter, constructor, path filter or backward W traversal is invoked.
Reference subpaths use the separate typed set engine. Changed-W arithmetic
reuses the audited integer-word Forward engine. One budget charges both.
All completed reference/forward tables, marked terms and results stay retained.
"""
from collections import Counter, deque
from pathlib import Path
import hashlib
import json
from parameterized_input import (CAPS, load, request, require, exact_equal,
                                bound, symbol_map, Rejected)
from receive_parameterized import topo
from verify_restricted_copies import IncrementalArithmetic, TARGET as OLD_TARGET
from audit_parameterized import Forward, LIMITS

HERE=Path(__file__).resolve().parent
OLD=HERE/'output-489'
ARCHIVE=HERE/'output-493'
OUT=HERE/'output-495'
MODES=('free','zero','axioms')
TARGET=('Test forward free, zero-placeholder and substituted evaluation of the '
        'unchanged restricted job-7 commutator against complete L035 references '
        'under the original caps.')


class Budget:
    def __init__(self):
        self.pairs=0
        self.slots={}
        self.peak=0
        self.last=None

    def multiply(self,a,b):
        self.pairs+=len(a)*len(b)
        bound(self.pairs,'multiplication_pairs','joint cumulative multiplication work')

    def retain(self,name,words):
        # Replacing a destination is the original accounting convention.
        # No completed table, term, reference or mode is removed from slots.
        self.slots[name]=words
        total=sum(self.slots.values())
        self.peak=max(self.peak,total)
        self.last=dict(slot=name,actual=total,required=CAPS['stored_words'])
        bound(total,'stored_words','joint retained tables/terms/references/results: '+name)

    def report(self):
        return dict(multiplication_pairs=self.pairs,required_pairs=CAPS['multiplication_pairs'],
                    stored_words=sum(self.slots.values()),max_stored_words=self.peak,
                    required_stored_words=CAPS['stored_words'],slots=self.slots,last=self.last)


class ReferenceArithmetic(IncrementalArithmetic):
    def __init__(self,req,budget):
        super().__init__(req)
        self.budget=budget

    def mul(self,a,b):
        self.budget.multiply(a,b)
        return super().mul(a,b)


class RetainedForward(Forward):
    def __init__(self,req,budget):
        super().__init__(req)
        self.budget=budget
        self.tables={}
        self.position=None

    def mul(self,a,b):
        self.budget.multiply(a,b)
        return super().mul(a,b)

    def graph(self,nv,edges,source,mode):
        # Forward.graph's edge sweep, with the additional caller-wide guard.
        # Retain the partial table too if a guard raises.
        bound(nv+len(edges),'records','forward graph')
        adj,ind=[[] for _ in range(nv)],[0]*nv
        for u,v,label in edges:
            require(type(u) is int and type(v) is int and 0<=u<nv and 0<=v<nv,
                    'forward endpoints')
            adj[u].append((v,label)); ind[v]+=1
        queue=deque(i for i in range(nv) if not ind[i])
        table=[{} for _ in range(nv)]; table[source]={():1}
        self.tables[mode]=table
        visits,storage=0,1
        self.budget.retain('forward '+mode,storage)
        while queue:
            u=queue.popleft(); visits+=1
            for v,label in adj[u]:
                self.position=dict(mode=mode,tail=u,head=v,visited=visits)
                storage-=len(table[v])
                table[v]=self.add(table[v],self.mul(table[u],self.label(label,mode)))
                storage+=len(table[v])
                self.metrics['stored_words']=max(self.metrics['stored_words'],storage)
                self.budget.retain('forward '+mode,storage)
                ind[v]-=1
                if not ind[v]: queue.append(v)
        require(visits==nv,'forward cycle')
        return table


def chunks(value):
    """Raw complete JSON without retaining a second serialized polynomial.

    Set order is immaterial; every word is emitted once. No preview/hash
    replaces a polynomial. Two passes count exact bytes before any file write.
    """
    if isinstance(value,dict):
        yield '{'
        for i,(k,v) in enumerate(value.items()):
            if i: yield ','
            yield json.dumps(str(k)); yield ':'
            yield from chunks(v)
        yield '}'
    elif isinstance(value,(list,tuple,set)):
        yield '['
        for i,v in enumerate(value):
            if i: yield ','
            yield from chunks(v)
        yield ']'
    else:
        yield json.dumps(value,separators=(',',':'))


def evidence(name,value):
    path=OUT/name
    require(not path.exists(),'preserve prior evidence')
    used=sum(p.stat().st_size for p in OUT.rglob('*') if p.is_file())
    size=1
    for c in chunks(value):
        size+=len(c.encode())
        # A rejected proposed file is not written; its exact first failed
        # count is recorded separately. Existing evidence is never truncated.
        bound(size,'certificate_bytes','proposed evidence file: '+name)
        bound(used+size,'certificate_bytes','aggregate proposed evidence: '+name)
    with path.open('wb') as stream:
        for c in chunks(value): stream.write(c.encode())
        stream.write(b'\n')
    require(path.stat().st_size==size,'exact emitted evidence byte count')
    return size


def main():
    require(not OUT.exists(),'fresh output required; no failed retry')
    OUT.mkdir()
    require(all(CAPS[k]==v for k,v in LIMITS.items()),'unchanged forward CAPS')
    budget=Budget(); ar=None; forward=None; stage='input'; copy_cases=Counter()
    completed_modes=[]; structure_received=False; reference_received=False
    evidence('checkpoint.json',dict(target=TARGET,caps=CAPS,status='IN_PROGRESS',
             assessment='drafts/literature/2026-10-25-forward-selected-job-reception.md',
             scope='Only job 7. No backward W, integration, table release or cap change.'))
    try:
        cert=load(ARCHIVE/'restricted-boolean.json')
        inventory=load(ARCHIVE/'restricted-interior-bound.json')
        req,raw,rows,checked=request(OLD/'inputs/proof.jsonl',OLD/'inputs/request.json')
        event=load(OLD/'trace/event-02643.json')
        translation=load(OLD/'trace/event-02642.json')
        transport=symbol_map(req['alphabet'],req['dictionary'])
        ar=ReferenceArithmetic(req,budget)
        forward=RetainedForward(req,budget)
        require(cert['target']==inventory['target']==OLD_TARGET
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
        for index,((u,kind,occurrences,f,g),item,old,counted) in enumerate(
                zip(jobs,cert['jobs'],prior['jobs'],inventory['jobs'])):
            if index!=7: continue
            stage='job 7 structural reception'
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

            require(index==7 and kind=='sum_commutator' and actual['records']==81_464,
                    'exact approved fixed component')
            bound(actual['records'],'records','job 7 received records')
            bound(actual['label_entries'],'label_entries','job 7 received labels')
            typed_edges,order=typed(out)
            # Structural occurrence counts precede coefficient cancellation.
            states=[set() for _ in range(out['vertices'])]; states[out['source']]={0}
            adj=[[] for _ in states]
            for cu,cv,lab in typed_edges: adj[cu].append((cv,lab))
            for cu in order:
                for cv,lab in adj[cu]:
                    kinds={x[0]=='placeholder' for x in lab}
                    require(len(kinds)<=1,'single-kind structural label')
                    inc=int(kinds=={True})
                    states[cv].update(k+inc for k in states[cu])
                    require(all(k<=1 for k in states[cv]),'no path uses two placeholders')
            require(states[out['sink']]<={1},'every accepting path uses exactly one placeholder')
            structure_received=True
            # Fully load the old failure and metadata, without accepting them
            # as current occurrence/arithmetic evidence.
            failed=load(ARCHIVE/'reception.failure.json')
            stopped=load(ARCHIVE/'stop-summary.json')
            require(failed==stopped['failure'] and failed['stage']=='job 7'
                    and stopped['completed_reference_jobs']==list(range(7))
                    and stopped['complete_reference_jobs_7_through_244'] is False,
                    'preserved exact backward stop and missing references')
            evidence('structure.json',dict(index=index,kind=kind,source_record=78,
                     source_check=checked,source_row=rows[78],caps=CAPS,
                     alphabet=req['alphabet'],dictionary=req['dictionary'],
                     original_operands=[f,g],restricted_operands=[a,b],
                     whole_operand_maps=item['restrictions'],selected_occurrences=item['selected'],
                     all_pairs=pairs,selected_pairs=len(expected_pairs),copy_cases=dict(copy_cases),
                     actual=actual,structural_counts=sorted(states[out['sink']]),
                     complete_partitions_received=True,graph=out,
                     preserved_failure=failed,receiver_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()))

            stage='complete original operand references'
            tables=[]
            for operand,z in enumerate((a,b)):
                ze,zo=typed(z,True); za=[[] for _ in range(z['vertices'])]
                for cu,cv,lab in ze: za[cu].append((cv,lab))
                prefix=[set() for _ in za]; prefix[z['source']]={()}
                tables.append([prefix,None])
                pw=1; slot='operand %d prefix'%operand; budget.retain(slot,pw)
                for cu in zo:
                    for cv,lab in za[cu]:
                        pw-=len(prefix[cv])
                        prefix[cv]=ar.add(prefix[cv],ar.mul(prefix[cu],ar.label(lab,'free')))
                        pw+=len(prefix[cv]); budget.retain(slot,pw)
                suffix=[set() for _ in za]; tables[-1][1]=suffix
                sw=0; slot='operand %d suffix'%operand
                for cu in reversed(zo):
                    suffix[cu]={()} if cu==z['sink'] else set()
                    for cv,lab in za[cu]:
                        suffix[cu]=ar.add(suffix[cu],ar.mul(ar.label(lab,'free'),suffix[cv]))
                    sw+=len(suffix[cu]); budget.retain(slot,sw)

            reference={m:set() for m in MODES}; terms=[]; retained_terms=0
            # All literal edge pairs were examined above. Empty central lists
            # are identically zero in all modes; save their exact indices too.
            selected_indices={(p['f_edge'],p['g_edge']) for p in expected_pairs}
            empty_pairs=[[i,j] for i in range(len(a['edges'])) for j in range(len(b['edges']))
                         if (i,j) not in selected_indices]
            require(len(empty_pairs)+len(expected_pairs)==pairs,'exhausted all-pair reference')
            for pair in expected_pairs:
                au,av,_=a['edges'][pair['f_edge']]; bu,bv,_=b['edges'][pair['g_edge']]
                left=ar.mul(tables[0][0][au],tables[1][0][bu])
                budget.retain('reference left intermediate',len(left))
                term={}
                for mode in MODES:
                    p=ar.mul(left,ar.label([transport[x] for x in pair['central']],mode))
                    p=ar.mul(p,tables[1][1][bv]); p=ar.mul(p,tables[0][1][av])
                    term[mode]=p
                    retained_terms+=len(p); budget.retain('all retained marked terms',retained_terms)
                    reference[mode]=ar.add(reference[mode],p)
                    budget.retain('complete reference '+mode,len(reference[mode]))
                terms.append(dict(pair,polynomials=term))
            fa,gb=tables[0][1][a['source']],tables[1][1][b['source']]
            fg=ar.mul(fa,gb); budget.retain('ordered operand product fg',len(fg))
            gf=ar.mul(gb,fa); budget.retain('ordered operand product gf',len(gf))
            target=ar.add(fg,gf); budget.retain('ordered operand commutator',len(target))
            require(not reference['zero'] and reference['axioms']==target,
                    'complete reference substitution and zero identity')
            evidence('reference.json',dict(index=7,all_pairs=pairs,empty_pairs=empty_pairs,
                     selected_terms=terms,polynomials=reference,target=target,
                     ordered_products=dict(fg=fg,gf=gf),
                     operand_subpaths=[dict(prefix=p,suffix=q) for p,q in tables],
                     budget=budget.report(),arithmetic=ar.counts))
            reference_received=True
            print(dict(stage='complete independent reference saved',job=7,
                       polynomial_words={m:len(p) for m,p in reference.items()},
                       budget=budget.report(),path=str(OUT/'reference.json')),flush=True)

            for mode in MODES:
                stage='forward '+mode
                table=forward.graph(out['vertices'],typed_edges,out['source'],mode)
                result=table[out['sink']]
                # Result aliases the retained table entry; converting to a
                # separate typed set for equality needs its own retained slot.
                decoded={tuple(('original',x) if x<forward.n else
                               ('placeholder',x-forward.n) for x in w) for w in result}
                budget.retain('decoded result '+mode,len(decoded))
                require(decoded==reference[mode],'complete forward/reference equality '+mode)
                if mode=='axioms': require(decoded==target,'ordered operand commutator')
                completed_modes.append(mode)
                # Keep all decoded results as well as all completed tables.
                if mode=='free': decoded_results={}
                decoded_results[mode]=decoded
                evidence('mode-'+mode+'.json',dict(mode=mode,polynomial=decoded,
                         all_vertex_word_counts=[len(p) for p in table],
                         complete_equality=True,budget=budget.report(),
                         forward_metrics=forward.metrics))
                print(dict(stage=stage,complete_equality=True,budget=budget.report()),flush=True)
            evidence('reception.json',dict(accepted_fixed_job=True,target=TARGET,caps=CAPS,
                     completed_modes=completed_modes,structure_received=structure_received,
                     complete_reference_received=reference_received,budget=budget.report(),
                     forward_metrics=forward.metrics,reference_metrics=ar.counts,
                     complete_boolean_received=False,complete_KH_received=False,nonzero_fJ_received=False))
            print(dict(accepted_fixed_job=True,failures=[],path=str(OUT/'reception.json')),flush=True)
    except (Rejected,AssertionError,KeyError,IndexError,TypeError,ValueError) as exc:
        failure=dict(accepted_fixed_job=False,target=TARGET,stage=stage,error=str(exc),
                     completed_modes=completed_modes,structure_received=structure_received,
                     complete_reference_received=reference_received,budget=budget.report(),
                     forward_position=None if forward is None else forward.position,
                     forward_metrics=None if forward is None else forward.metrics,
                     reference_metrics=None if ar is None else ar.counts,
                     complete_boolean_received=False,complete_KH_received=False,nonzero_fJ_received=False)
        evidence('reception.failure.json',failure)
        used=sum(p.stat().st_size for p in OUT.rglob('*') if p.is_file())
        print(dict(accepted_fixed_job=False,stage=stage,error=str(exc),
                   actual_retained_words=budget.peak,required_retained_words=CAPS['stored_words'],
                   multiplication_pairs=budget.pairs,required_pairs=CAPS['multiplication_pairs'],
                   evidence_bytes=used,required_evidence_bytes=CAPS['certificate_bytes'],
                   path=str(OUT/'reception.failure.json')),flush=True)
        raise


if __name__=='__main__':
    main()

