"""Independent finite necessary-bound receiver; no emitter/filter imports.

Reconstructs every L036 job, restriction and literal central occurrence.
This receives a failed record discriminator, never a Boolean identity.
"""
from collections import Counter
from pathlib import Path
import hashlib
from parameterized_input import CAPS, load, request, require, exact_equal, bound, symbol_map
from receive_parameterized import Arithmetic, topo, serial
from receive_selected_commutator import install_evidence_budget

HERE = Path(__file__).resolve().parent
OLD = HERE/'output-489'
OUT = HERE/'output-491'


def main():
    require(not (OUT/'bound-reception.json').exists(), 'refuse existing reception')
    write = install_evidence_budget(OUT)
    cert = load(OUT/'retained-interior-bound.json')
    req,raw,rows,checked = request(OLD/'inputs/proof.jsonl',OLD/'inputs/request.json')
    require(exact_equal(cert['caps'],CAPS) and exact_equal(cert['alphabet'],req['alphabet'])
            and exact_equal(cert['dictionary'],req['dictionary'])
            and exact_equal(cert['checked_source'],checked), 'unchanged framing and checked source')
    for name,digest in cert['input_hashes'].items():
        require(hashlib.sha256((HERE/name).read_bytes()).hexdigest()==digest, 'retained input bytes')
    event = load(OLD/'trace/event-02643.json')
    translation = load(OLD/'trace/event-02642.json')
    require(cert['source_record']==78 and cert['boolean_event']==2643 and
            checked['records']==212 and checked['sha256']==
            'f779fa52af4eb63805e45aa9940620be1cd3ce6c993ff4a903a996a0b539c74e'
            and rows[78]['rule']=='axiom' and translation['kind']=='translation'
            and event['kind']=='boolean-input'
            and exact_equal(translation['formula'],rows[78]['f'][2])
            and exact_equal(translation['graph'],event['graph']), 'exact source/Boolean binding')
    g = event['graph']
    # Separate coefficient normalization, preserving edge occurrences.
    normalized_edges = []
    for u,v,lab in g['edges']:
        if u!=g['sink']:
            normalized_edges.extend([u,v,[x]] for x,n in sorted(Counter(lab).items()) if n%2)
    h = dict(g,edges=normalized_edges)
    require(exact_equal(h,cert['normalized']), 'entire normalized operand')
    transport = symbol_map(req['alphabet'],req['dictionary'])
    ar = Arithmetic(req)

    def typed(z):
        require(set(z)=={'vertices','source','sink','edges'}, 'graph fields')
        require(all(x=='1' or transport[x][0]=='original'
                    for _,_,lab in z['edges'] for x in lab), 'all original labels including dead edges')
        n=z['vertices']
        require(type(z['source']) is int and type(z['sink']) is int and
                0<=z['source']<n and 0<=z['sink']<n, 'root indices')
        edges = [[u,v,[transport[x] for x in lab]] for u,v,lab in z['edges']]
        return edges,topo(n,edges,req)

    def evaluate(z):
        edges,order=typed(z)
        return ar.evaluate(z['vertices'],edges,order,z['source'],z['sink'],'free')

    value=evaluate(g)
    require(value==evaluate(h)==ar.translation(rows[78]['f'][2]), 'complete original input polynomial')
    jobs=[]
    for u in range(h['vertices']):
        outgoing=[(i,v,lab[0]) for i,(z,v,lab) in enumerate(h['edges']) if z==u]
        for i,v,x in outgoing:
            jobs.append((u,'product_commutator',[i],
                         dict(vertices=2,source=0,sink=1,edges=[[0,1,[x]]]),
                         dict(h,source=v)))
        for pos,(i,v,x) in enumerate(outgoing):
            for j,w,y in outgoing[pos+1:]:
                f=dict(h,vertices=h['vertices']+1,source=h['vertices'],
                       edges=h['edges']+[[h['vertices'],v,[x]]])
                z=dict(h,vertices=h['vertices']+1,source=h['vertices'],
                       edges=h['edges']+[[h['vertices'],w,[y]]])
                jobs.append((u,'sum_commutator',[i,j],f,z))
    require(len(jobs)==len(cert['jobs']), 'complete L036 recipe including all unsaved jobs')

    def restricted(z,item):
        require(exact_equal(z,item['original']), 'complete original job graph')
        typed(z)
        n,s,t=z['vertices'],z['source'],z['sink']
        # Bitset transitive closure, independently of forward/backward filtering.
        reach=[1<<i for i in range(n)]
        for a,b,_ in z['edges']: reach[a] |= 1<<b
        for k in range(n):
            bit=1<<k
            for a in range(n):
                if reach[a]&bit: reach[a] |= reach[k]
        no_path=not bool(reach[s]&(1<<t))
        live=sorted({s,t}) if no_path else [v for v in range(n)
                    if reach[s]&(1<<v) and reach[v]&(1<<t)]
        mapping=[live.index(v) if v in live else None for v in range(n)]
        indices=[i for i,(a,b,_) in enumerate(z['edges'])
                 if not no_path and reach[s]&(1<<a) and reach[b]&(1<<t)]
        expected=dict(vertices=len(live),source=mapping[s],sink=mapping[t],
                      edges=[[mapping[z['edges'][i][0]],mapping[z['edges'][i][1]],z['edges'][i][2]]
                             for i in indices])
        require(exact_equal(item,dict(original=z,trimmed=expected,old_to_new=mapping,
                                      new_to_old=live,retained_edge_indices=indices,no_path=no_path)),
                'complete root/vertex/edge maps and ordered label occurrences')
        typed(expected)
        return expected

    totals=Counter(); kinds=Counter(); nonempty=Counter(); detail=[]
    for index,(recipe,item) in enumerate(zip(jobs,cert['jobs'])):
        u,kind,occurrences,f,g=recipe
        require((item['index'],item['vertex'],item['kind'],item['edge_occurrences'])==
                (index,u,kind,occurrences), 'every job and ordered source edge occurrence')
        a,b=[restricted(z,r) for z,r in zip((f,g),item['restrictions'])]
        require(len(item['restrictions'])==2, 'two complete restrictions')
        bound(len(a['edges'])*len(b['edges']),'records','all-pair finite inventory')
        central=[]
        for i,(_,_,al) in enumerate(a['edges']):
            for j,(_,_,bl) in enumerate(b['edges']):
                labels=[]
                for x in al:
                    for y in bl:
                        xx,yy=transport[x],transport[y]
                        if xx[0]==yy[0]=='original' and xx[1]!=yy[1]:
                            lo,hi=sorted((xx[1]+1,yy[1]+1))
                            labels.append('t:%d:%d'%(lo,hi))
                if labels: central.append(dict(f_edge=i,g_edge=j,central=labels))
        require(exact_equal(central,item['selected']), 'every literal central occurrence with multiplicity')
        # Count the actual four-copy inventory, with the two shared W endpoints.
        nv,ne,nl=2,0,0
        for pair in central:
            for z in (a,b,b,a):
                nv+=z['vertices']; ne+=len(z['edges'])
                nl+=sum(len(lab) for _,_,lab in z['edges'])
            ne+=4+len(pair['central']); nl+=4+len(pair['central'])
        actual=dict(vertices=nv,edges=ne,records=nv+ne,label_entries=nl)
        require(all(item[k]==v for k,v in actual.items()), 'independent every-copy ledger')
        totals.update(actual); kinds[kind]+=1
        if central: nonempty.update(actual)
        detail.append(dict(index=index,kind=kind,retained_pairs=len(central),**actual))
    require(dict(totals)==cert['retained_interiors'] and
            cert['required_records']==CAPS['records'] and
            cert['fits_necessary_bound'] is (totals['records']<=CAPS['records']),
            'full summed necessary bound')
    require(totals['records']>CAPS['records'], 'failed record discriminator established')
    require(nonempty['records']>CAPS['records'], 'failure persists even deleting every empty W block')
    require(not cert['complete_shared_graph'] and not cert['complete_free_polynomial_received']
            and not cert['complete_KH_received'], 'no unperformed identity or integration acceptance')
    receipt=dict(verified_failed_discriminator=True,accepted_shared_witness=False,failures=[],
                 retained_interiors=dict(totals),nonempty_interiors=dict(nonempty),
                 job_kinds=dict(kinds),jobs=detail,actual=totals['records'],required=CAPS['records'],
                 excess=totals['records']-CAPS['records'],caps=CAPS,
                 complete_input_polynomial=serial(value),input_arithmetic=ar.counts,
                 complete_recipe_and_occurrences_received=True,
                 complete_free_polynomial_received=False,complete_shared_graph=False,
                 complete_KH_received=False,
                 scope='Necessary retained-interior count only; final-suffix sharing cannot alter these records.')
    write(OUT/'bound-reception.json',receipt)
    used=sum(p.stat().st_size for p in OUT.rglob('*') if p.is_file())
    print(dict(verified_failed_discriminator=True,jobs=len(jobs),actual=totals['records'],
               nonempty_records=nonempty['records'],required=CAPS['records'],
               evidence_bytes=used,required_evidence_bytes=CAPS['certificate_bytes'],
               failures=[],path=str(OUT/'bound-reception.json')))


if __name__=='__main__':
    main()
