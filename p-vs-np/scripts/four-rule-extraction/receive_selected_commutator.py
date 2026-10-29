"""Independent all-pair reference and literal-copy receiver; no emitters.

Subpath arithmetic, literal selection, partitions and count ledgers are rebuilt
from typed received inputs. Full reference terms are saved, not sampled.
"""
import json
import sys
from pathlib import Path
from parameterized_input import CAPS, bound, require, exact_equal, write_json
from receive_parameterized import topo
from verify_constant_translation import typed
from verify_trimmed_occurrence import serial


def install_evidence_budget(folder):
    """Same per-file caps plus streaming aggregate charge for every new artifact."""
    folder = Path(folder)
    original = write_json
    def writer(path, value, key='certificate_bytes'):
        path = Path(path)
        require(path.is_relative_to(folder), 'evidence write inside fresh output')
        old = path.stat().st_size if path.exists() else 0
        used = sum(p.stat().st_size for p in folder.rglob('*') if p.is_file())-old
        tmp = path.with_suffix(path.suffix+'.partial')
        size = 0
        with tmp.open('wb') as stream:
            for chunk in json.JSONEncoder(separators=(',',':')).iterencode(value):
                raw = chunk.encode()
                size += len(raw)
                bound(size,key,'streamed file bytes: '+str(path))
                bound(used+size,'certificate_bytes','aggregate evidence before write')
                stream.write(raw)
            bound(size+1,key,'streamed newline')
            bound(used+size+1,'certificate_bytes','aggregate evidence newline')
            stream.write(b'\n')
        tmp.replace(path)
        return size+1
    # Rebind aliases already imported by the driver/receiver, without editing
    # any production module on disk. The parser and accepting contracts stay put.
    for module in list(sys.modules.values()):
        if module is not None and getattr(module,'write_json',None) is original:
            module.write_json = writer
    return writer


def selected_input(receiver, event, f, g):
    transport, ar = receiver.transport, receiver.ar
    pair_id = {tuple(receiver.req['alphabet'].index(x) for x in p['originals']):i
               for i,p in enumerate(receiver.req['dictionary']['placeholders'])
               if p['kind']=='commutator'}
    allpairs = []
    for i,(_,_,a) in enumerate(f['edges']):
        for j,(_,_,b) in enumerate(g['edges']):
            central = []
            for x in a:
                for y in b:
                    xx,yy = transport[x],transport[y]
                    if xx[0]=='original' and yy[0]=='original' and xx[1]!=yy[1]:
                        central.append(['placeholder',pair_id[tuple(sorted((xx[1],yy[1])))]] )
            allpairs.append(dict(f_edge=i,g_edge=j,central=central))
    bound(len(allpairs),'records','received full literal inventory')
    require(len(allpairs)==len(event['inventory']), 'complete literal inventory length')
    for a,b in zip(allpairs,event['inventory']):
        require((a['f_edge'],a['g_edge'])==(b['f_edge'],b['g_edge']) and
                exact_equal(a['central'],[transport[x] for x in b['central']]),
                'independently reconstructed literal central entries and multiplicities')
    r = sum(bool(p['central']) for p in allpairs)
    q = sum(len(p['central']) for p in allpairs)
    nv = 2+2*r*(f['vertices']+g['vertices'])
    ne = 2*r*(len(f['edges'])+len(g['edges']))+4*r+q
    labels = 2*r*sum(len(l) for h in (f,g) for _,_,l in h['edges'])+4*r+q
    ledger = dict(retained=r,omitted=len(allpairs)-r,central=q,vertices=nv,edges=ne,
                  actual=nv+ne,label_entries=labels,required=CAPS['records'],
                  fits=nv+ne<=CAPS['records'])
    require(exact_equal(ledger,event['selected_ledger']), 'independent selected ledger')
    return allpairs,ledger


def receive_output(receiver, j, event, output, f, g, allpairs, ledger, target, folder):
    ar,transport = receiver.ar,receiver.transport
    bound(ledger['actual'],'records','completed selected allocation')
    bound(ledger['label_entries'],'label_entries','completed selected label entries')
    require(output['parent']==j and output['central']==ledger['central'], 'selected output binding')
    tables = []
    retained_words = 0
    for h in (f,g):
        z = typed(h,transport); order = topo(z['vertices'],z['edges'],receiver.req)
        prefix = [set() for _ in range(z['vertices'])]; prefix[z['source']]={()}
        adj = [[] for _ in prefix]
        for u,v,lab in z['edges']: adj[u].append((v,lab))
        for u in order:
            for v,lab in adj[u]:
                prefix[v] = ar.add(prefix[v],ar.mul(prefix[u],ar.label(lab,'free')))
            bound(retained_words+sum(map(len,prefix)),'stored_words','reference prefixes')
        suffix = [set() for _ in prefix]
        for u in reversed(order):
            suffix[u] = {()} if u==z['sink'] else set()
            for v,lab in adj[u]:
                suffix[u] = ar.add(suffix[u],ar.mul(ar.label(lab,'free'),suffix[v]))
            bound(retained_words+sum(map(len,prefix))+sum(map(len,suffix)),
                  'stored_words','retained reference subpaths')
        retained_words += sum(map(len,prefix))+sum(map(len,suffix))
        tables.append((prefix,suffix))
    reference = set(); terms = []; term_words = 0
    for p in allpairs:
        u,v,_ = f['edges'][p['f_edge']]; a,b,_ = g['edges'][p['g_edge']]
        term = ar.mul(tables[0][0][u],tables[1][0][a])
        term = ar.mul(term,ar.label(p['central'],'free'))
        term = ar.mul(term,tables[1][1][b])
        term = ar.mul(term,tables[0][1][v])
        reference = ar.add(reference,term)
        terms.append(dict(p,polynomial=serial(term)))
        term_words += len(term)
        bound(retained_words+term_words+len(reference),'stored_words','full retained reference evidence')
    path = Path(folder)/'references'/('event-%05d.json' % j)
    path.parent.mkdir(exist_ok=True)
    write_json(path,dict(all_pairs=terms,polynomial=serial(reference),
        operand_subpaths=[dict(prefix=[serial(p) for p in a],suffix=[serial(p) for p in b])
                          for a,b in tables]))
    out = output['graph']; edges = out['edges']; vertex,cursor,branch = 2,0,0
    for p in allpairs:
        if not p['central']: continue
        require(branch<len(output['branches']), 'retained branch present')
        part = output['branches'][branch]; branch += 1
        i,k = p['f_edge'],p['g_edge']; u,v,_ = f['edges'][i]; a,b,_ = g['edges'][k]
        require((part['f_edge'],part['g_edge'])==(i,k) and len(part['copies'])==4,
                'selected branches retain full pair occurrence order')
        roots = []
        for copy,h,s,t in zip(part['copies'],(f,g,g,f),(f['source'],g['source'],b,v),
                              (u,a,g['sink'],f['sink'])):
            end,hi = cursor+len(h['edges']),vertex+h['vertices']
            require(exact_equal(copy,dict(vertex_range=[vertex,hi],edge_range=[cursor,end],
                                         entry=vertex+s,exit=vertex+t)), 'complete four-copy partition')
            for index,(x,y,lab) in enumerate(h['edges'],cursor):
                require(exact_equal(edges[index],[vertex+x,vertex+y,lab]), 'every copied record')
            roots.append((vertex+s,vertex+t)); vertex,cursor = hi,end
        fp,gp,gs,fs = roots
        connectors = [[0,fp[0],['1']],[fp[1],gp[0],['1']],
                      [gs[1],fs[0],['1']],[fs[1],1,['1']]]
        end = cursor+4+len(p['central'])
        require(part['connecting_edges']==[cursor,end] and
                exact_equal(edges[cursor:cursor+4],connectors), 'all selected connectors')
        require(exact_equal([[u,v,[transport[x] for x in lab]] for u,v,lab in edges[cursor+4:end]],
                            [[gp[1],gs[0],[x]] for x in p['central']]), 'all central occurrences')
        cursor = end
    require(branch==ledger['retained']==len(output['branches']) and
            vertex==ledger['vertices']==out['vertices'] and
            cursor==ledger['edges']==len(edges) and out['source']==0 and out['sink']==1,
            'entire selected output record accounting')
    require(sum(len(l) for _,_,l in edges)==ledger['label_entries'], 'entire selected labels')
    z = typed(out,transport); order = topo(z['vertices'],z['edges'],receiver.req)
    polys = receiver.evaluate(out,('free','zero','axioms'))
    require(polys['free']==reference and not polys['zero'] and polys['axioms']==target,
            'full all-pair free / zero / substituted equalities')
    states = [set() for _ in range(z['vertices'])]; states[0]={0}
    adj = [[] for _ in states]
    for u,v,lab in z['edges']: adj[u].append((v,lab))
    for u in order:
        for v,lab in adj[u]:
            kinds = {x[0]=='placeholder' for x in lab}
            require(len(kinds)<=1,'single-kind structural label')
            increment = int(kinds=={True})
            states[v].update(k+increment for k in states[u])
            require(all(k<=1 for k in states[v]), 'no path takes two placeholders')
    require(states[1] <= {1}, 'all accepting paths take one placeholder, vacuously if none')
    return dict(polynomials={m:serial(p) for m,p in polys.items()},
                reference_path=str(path.relative_to(folder)),all_pairs=len(allpairs),
                selected_ledger=ledger,literal_partitions_received=True,
                full_free_reference_received=True,structural_counts=sorted(states[1]))
