"""Step 491: necessary retained-interior bound, before shared-graph allocation.

No extraction or commutator constructor is invoked. All L036 jobs are counted,
including those beyond the stopped trace; the complete finite ledger is saved.
"""
from pathlib import Path
import hashlib
from parameterized_input import CAPS, load, request, require, exact_equal, bound
from receive_selected_commutator import install_evidence_budget
from verify_constant_translation import normalized, root, atom, prefix
from trim_saved_operands import trim

HERE = Path(__file__).resolve().parent
OLD = HERE / 'output-489'
OUT = HERE / 'output-491'
TARGET = ('Test sharing one final original-only suffix graph across the stopped '
          'record-78 Boolean branches, preserving the complete free polynomial '
          'under the unchanged caps.')


def main():
    require(not OUT.exists(), 'refuse existing isolated output')
    OUT.mkdir()
    write = install_evidence_budget(OUT)
    req, raw, rows, checked = request(OLD/'inputs/proof.jsonl', OLD/'inputs/request.json')
    require(checked['records'] == 212 and checked['sha256'] ==
            'f779fa52af4eb63805e45aa9940620be1cd3ce6c993ff4a903a996a0b539c74e',
            'audited supplied endpoint bytes')
    event = load(OLD/'trace/event-02643.json')
    translated = load(OLD/'trace/event-02642.json')
    require(event['kind'] == 'boolean-input' and translated['kind'] == 'translation'
            and rows[78]['rule'] == 'axiom'
            and exact_equal(translated['formula'], rows[78]['f'][2])
            and exact_equal(translated['graph'], event['graph']), 'source row/input binding')
    h = normalized(event['graph'])
    require((h['vertices'], h['source'], h['sink'], len(h['edges'])) == (154,0,1,199),
            'exact isolated normalized operand')
    originals = {'1'} | {'x'+str(i+1) for i in range(len(req['alphabet']))}
    require(all(len(lab)==1 and lab[0] in originals for _,_,lab in h['edges']),
            'original-only normalized singleton labels')
    files = [OLD/p for p in ('inputs/proof.jsonl','inputs/request.json',
                             'trace/event-02642.json','trace/event-02643.json')]
    cert = dict(target=TARGET, caps=CAPS, alphabet=req['alphabet'], dictionary=req['dictionary'],
                checked_source=checked, source_record=78, boolean_event=2643,
                normalized=h, jobs=[],
                input_hashes={str(p.relative_to(HERE)): hashlib.sha256(p.read_bytes()).hexdigest()
                              for p in files},
                scope='Necessary disjoint selected-interior bound only; no changed graph or polynomial reception.')
    write(OUT/'checkpoint.json', cert)
    for u in range(h['vertices']):
        outgoing = [(i,v,lab[0]) for i,(z,v,lab) in enumerate(h['edges']) if z==u]
        recipes = [('product_commutator',[i], atom(x),root(h,v)) for i,v,x in outgoing]
        recipes += [('sum_commutator',[i,j],prefix(h,x,v),prefix(h,y,w))
                    for pos,(i,v,x) in enumerate(outgoing) for j,w,y in outgoing[pos+1:]]
        for kind, occurrences, f, g in recipes:
            restricted = [trim(a) for a in (f,g)]
            a,b = [r['trimmed'] for r in restricted]
            bound(len(a['edges'])*len(b['edges']), 'records', 'one literal inventory')
            selected = []
            for i,(_,_,al) in enumerate(a['edges']):
                for j,(_,_,bl) in enumerate(b['edges']):
                    central = []
                    for x in al:
                        for y in bl:
                            if x != '1' and y != '1' and x != y:
                                lo,hi = sorted((int(x[1:]),int(y[1:])))
                                central.append('t:%d:%d' % (lo,hi))
                    if central:
                        selected.append(dict(f_edge=i,g_edge=j,central=central))
            r,q = len(selected),sum(len(p['central']) for p in selected)
            nv = 2+2*r*(a['vertices']+b['vertices'])
            ne = 2*r*(len(a['edges'])+len(b['edges']))+4*r+q
            labels = 2*r*sum(len(l) for z in (a,b) for _,_,l in z['edges'])+4*r+q
            cert['jobs'].append(dict(index=len(cert['jobs']),vertex=u,kind=kind,
                                     edge_occurrences=occurrences,restrictions=restricted,
                                     selected=selected,vertices=nv,edges=ne,records=nv+ne,
                                     label_entries=labels))
    total = {key:sum(j[key] for j in cert['jobs'])
             for key in ('vertices','edges','records','label_entries')}
    cert.update(retained_interiors=total, required_records=CAPS['records'],
                fits_necessary_bound=total['records']<=CAPS['records'],
                complete_shared_graph=False, complete_free_polynomial_received=False,
                complete_KH_received=False)
    write(OUT/'retained-interior-bound.json',cert)
    print(dict(necessary_bound_fits=cert['fits_necessary_bound'],jobs=len(cert['jobs']),
               actual=total['records'],required=CAPS['records'],
               label_entries=total['label_entries'],failures=[],
               path=str(OUT/'retained-interior-bound.json')))


if __name__ == '__main__':
    main()
