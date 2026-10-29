"""Independent step-481 trace, Boolean-copy and complete K/H reception.

No emitter, adapter, selector or correction constructor is imported. Existing
source/occurrence recipe and production acceptance checks are reused intact.
"""
from pathlib import Path
import verify_trimmed_occurrence as base
from parameterized_input import require, exact_equal
from verify_path_trimming import counts
from verify_constant_translation import normalized, root, atom
from receive_selected_commutator import (selected_input, receive_output,
                                         install_evidence_budget)

OUT = Path(__file__).resolve().parent/'output-481'


class Reception(base.Reception):
    def commutator(self, f, g, parent, entry):
        j,event = self.take('commutator-input')
        require(event['parent']==parent and event['entry']==entry and
                exact_equal([event['f'],event['g']],[f,g]), 'original ordered recipe provenance')
        values,details = [],[]
        for key,expected in zip(('f','g'),(f,g)):
            value,detail = self.restriction(event['restrictions'][key],expected)
            values.append(value); details.append(detail)
        a,b = (event['restrictions'][key]['trimmed'] for key in ('f','g'))
        old,new = counts(f,g),counts(a,b)
        require(exact_equal(old,event['original_ledger']) and
                exact_equal(new,event['trimmed_ledger']), 'baseline all-pair ledgers retained')
        inventory,ledger = selected_input(self,event,a,b)
        target = self.ar.add(self.ar.mul(values[0],values[1]),self.ar.mul(values[1],values[0]))
        self.statistics['commutators'] += 1
        self.statistics['max_old_ledger'] = max(old['actual'],self.statistics['max_old_ledger'])
        self.statistics['max_new_ledger'] = max(ledger['actual'],self.statistics['max_new_ledger'])
        key = ('nested_calls' if parent is not None else 'source_direct_calls'
               if entry=='m.witness' else 'occurrence_direct_calls')
        self.statistics[key] += 1
        self.save(j,'commutator-input',parent=parent,entry=entry,operands=details,
                  original_ledger=old,trimmed_ledger=new,selected_ledger=ledger,
                  target=base.serial(target))
        self.pending = dict(kind='commutator',event=j,ledger=ledger)
        k,output = self.take('commutator-output')
        evidence = receive_output(self,j,event,output,a,b,inventory,ledger,target,OUT)
        self.save(k,'commutator-output',parent=j,**evidence)
        self.pending = None
        return output['graph']

    def boolean(self, g):
        j,event = self.take('boolean-input')
        require(exact_equal(event['graph'],g), 'actual Boolean translation input')
        h = normalized(g)
        a = self.evaluate(g,original=True)['free']
        require(self.evaluate(h,original=True)['free']==a, 'complete normalization')
        self.statistics['booleans'] += 1
        self.save(j,'boolean-input',input=base.serial(a),
                  required_nested_calls=len(base.nested_schedule(h)))
        # Reconstruct all jobs and all attached factors in their original order.
        attachments = []; jobs = 0
        for u in range(h['vertices']):
            outgoing = [(v,lab[0]) for z,v,lab in h['edges'] if z==u]
            for v,x in outgoing:
                suffix = root(h,v)
                if x!='1':
                    attachments.append((u,'edge_boolean',[atom('b:'+x[1:]),suffix,suffix]))
                w = self.commutator(atom(x),suffix,j,'m.witness'); jobs += 1
                attachments.append((u,'product_commutator',[atom(x),w,suffix]))
            for i,(v,x) in enumerate(outgoing):
                for z,y in outgoing[i+1:]:
                    from verify_constant_translation import prefix
                    w = self.commutator(prefix(h,x,v),prefix(h,y,z),j,'m.witness'); jobs += 1
                    attachments.append((u,'sum_commutator',w))
        self.pending = dict(kind='boolean',event=j,completed_nested_calls=jobs)
        k,output = self.take('boolean-output')
        require(output['parent']==j and exact_equal(output['normalized'],h),
                'complete normalized parent/output binding')
        out = output['graph']; edges = out['edges']
        require(out['source']==h['source'] and out['sink']==h['vertices'] and
                exact_equal(edges[:len(h['edges'])],h['edges']), 'complete Boolean propagation')
        vertex,cursor = h['vertices']+1,len(h['edges'])

        def embedded(child,offset):
            nonlocal cursor
            for u,v,lab in child['edges']:
                require(cursor<len(edges) and exact_equal(edges[cursor],[u+offset,v+offset,lab]),
                        'every Boolean copied endpoint/label/edge occurrence')
                cursor += 1
            return offset+child['source'],offset+child['sink']

        ledger = []
        for u,kind,block in attachments:
            first,lo = cursor,vertex
            if kind=='sum_commutator':
                s,t = embedded(block,vertex)
                vertex += block['vertices']
            else:
                # Exact independent product partition, including wrapper endpoints.
                s,t = vertex,vertex+1
                vertex += 2; last = s
                for child in block:
                    cs,ct = embedded(child,vertex)
                    require(exact_equal(edges[cursor],[last,cs,['1']]), 'ordered factor connector')
                    cursor += 1; last = ct; vertex += child['vertices']
                require(exact_equal(edges[cursor],[last,t,['1']]), 'final factor connector')
                cursor += 1
            ledger.append(dict(vertex=u,kind=kind,vertices=vertex-lo,edges=cursor-first))
            require(exact_equal(edges[cursor:cursor+2],[[u,s,['1']],[t,out['sink'],['1']]]),
                    'Boolean attachment connectors')
            cursor += 2
        require(vertex==out['vertices'] and cursor==len(edges) and
                exact_equal(ledger,output['ledger']), 'all Boolean records and actual attach ledger')
        polys = self.evaluate(out,('free','zero','axioms'))
        target = self.ar.add(self.ar.mul(a,a),a)
        require(not polys['zero'] and polys['axioms']==target, 'complete Boolean identities')
        self.save(k,'boolean-output',parent=j,nested_calls=jobs,
                  polynomials={m:base.serial(p) for m,p in polys.items()},
                  target=base.serial(target),complete_propagation_and_copy_partitions=True,
                  attachments=len(ledger),records=vertex+cursor)
        self.pending = None
        return out


if __name__=='__main__':
    base.OUT = OUT
    base.Reception = Reception
    install_evidence_budget(OUT)
    base.main()
