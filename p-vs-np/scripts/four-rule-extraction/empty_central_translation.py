"""Step 481: both L035 entries, literal-empty central selection before copies.

Reuses scalar translation and whole-operand restriction, not semantic selection.
Every pending input/inventory is persisted before the selected preflight.
"""
from trimming_translation import Trimming, e
from trim_saved_operands import trim, ledger
from parameterized_input import CAPS, bound, require


class EmptyCentral(Trimming):
    def call(self, entry, f, g, **kw):
        require(not kw, 'no mutation or changed constructor parameters')
        e.original_only(f)
        e.original_only(g)
        restrictions = dict(f=trim(f), g=trim(g))
        a, b = (restrictions[k]['trimmed'] for k in ('f', 'g'))
        e.original_only(a)
        e.original_only(b)
        bound(len(a['edges'])*len(b['edges']), 'records', 'literal inventory entries')
        inventory = []
        for i, (_, _, al) in enumerate(a['edges']):
            for j, (_, _, bl) in enumerate(b['edges']):
                central = []
                for x in al:
                    for y in bl:
                        if x != '1' and y != '1' and x != y:
                            lo, hi = sorted((int(x[1:]), int(y[1:])))
                            central.append('t:%d:%d' % (lo, hi))
                inventory.append(dict(f_edge=i, g_edge=j, central=central))
        selected = [p for p in inventory if p['central']]
        r, q = len(selected), sum(len(p['central']) for p in inventory)
        nv = 2+2*r*(a['vertices']+b['vertices'])
        ne = 2*r*(len(a['edges'])+len(b['edges']))+4*r+q
        labels = 2*r*sum(len(l) for h in (a,b) for _,_,l in h['edges'])+4*r+q
        chosen = dict(retained=r, omitted=len(inventory)-r, central=q,
                      vertices=nv, edges=ne, actual=nv+ne, label_entries=labels,
                      required=CAPS['records'], fits=nv+ne <= CAPS['records'])
        index = self.save('commutator-input', parent=self.boolean, entry=entry,
                          f=f, g=g, restrictions=restrictions,
                          original_ledger=ledger(f,g), trimmed_ledger=ledger(a,b),
                          inventory=inventory, selected_ledger=chosen)
        e.bound(nv+ne, 'selected L035 preflight')
        bound(labels, 'label_entries', 'selected L035 label preflight')
        e.CONSTRUCTION['commutator_calls'] += 1
        out = e.m.graph(2, [], sink=1)
        parts = []

        def copy(h, s, t):
            lo, first = out['vertices'], len(out['edges'])
            out['vertices'] += h['vertices']
            out['edges'].extend([lo+u,lo+v,list(lab)] for u,v,lab in h['edges'])
            return dict(vertex_range=[lo,out['vertices']],
                        edge_range=[first,len(out['edges'])],entry=lo+s,exit=lo+t)

        for p in selected:
            u,v,_ = a['edges'][p['f_edge']]
            s,t,_ = b['edges'][p['g_edge']]
            copies = [copy(a,a['source'],u),copy(b,b['source'],s),
                      copy(b,t,b['sink']),copy(a,v,a['sink'])]
            fp,gp,gs,fs = copies
            first = len(out['edges'])
            out['edges'].extend([[0,fp['entry'],['1']], [fp['exit'],gp['entry'],['1']],
                                [gs['exit'],fs['entry'],['1']], [fs['exit'],1,['1']]])
            out['edges'].extend([gp['exit'],gs['entry'],[x]] for x in p['central'])
            parts.append(dict(f_edge=p['f_edge'],g_edge=p['g_edge'],copies=copies,
                              connecting_edges=[first,len(out['edges'])]))
        require(out['vertices']==nv and len(out['edges'])==ne and
                sum(len(l) for _,_,l in out['edges'])==labels, 'selected exact-copy count')
        self.save('commutator-output', parent=index, graph=out, central=q, branches=parts)
        return out, q


def install(folder):
    adapter = EmptyCentral(folder)
    e.translation = adapter.translation
    e.b.construct = adapter.construct
    e.m.witness = adapter.witness
    e.checked_witness = adapter.occurrence_witness
    return adapter
