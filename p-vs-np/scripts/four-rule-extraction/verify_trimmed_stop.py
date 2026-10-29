"""Full structural/count/trace binding of step 477's fixed-cap stop.

No emitter, filter or constructor imports. Does not assign an identity to an
unfinished Boolean output or a partial K. Full arithmetic is in the separate
two-stage trace receiver's retained evidence.
"""
from pathlib import Path
import hashlib
from parameterized_input import CAPS, load, require, exact_equal, write_json, symbol_map, request
from verify_positive_stop import graph
from verify_path_trimming import counts
from verify_constant_translation import typed, normalized, nested_schedule
from receive_occurrence import copied_composition

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
OUT = HERE / 'output-477'


class Binding:
    def __init__(self, index, transport):
        self.index, self.transport, self.position = index, transport, 0

    def take(self, kind):
        j = self.position
        item = self.index[j]
        require(item['index'] == j and item['file'] == 'event-%05d.json' % j,
                'complete index')
        e = load(OUT/'trace'/item['file'])
        require(item['kind'] == e['kind'] == kind, 'exact binding trace sequence')
        self.position += 1
        return j, e

    def translation(self, formula):
        _, e = self.take('translation')
        require(exact_equal(e['formula'], formula), 'binding exact formula occurrence')
        return e['graph']

    def commutator(self, f, g, parent):
        j, e = self.take('commutator-input')
        require(e['entry'] == 'm.witness' and e['parent'] == parent and
                exact_equal([e['f'],e['g']], [f,g]), 'binding original recipe pair')
        _, output = self.take('commutator-output')
        require(output['parent'] == j, 'binding actual correction output')
        return output['graph']

    def boolean(self, g):
        j, e = self.take('boolean-input')
        require(exact_equal(e['graph'], g), 'binding actual Boolean input')
        h = normalized(g)
        for f, gg in nested_schedule(h):
            self.commutator(f, gg, j)
        _, output = self.take('boolean-output')
        require(output['parent'] == j and exact_equal(output['normalized'], h),
                'binding actual Boolean output and normalized parent')
        return output['graph']


def main():
    path = OUT/'stop-check.json'
    require(not path.exists(), 'refuse existing stop receipt')
    req, raw, rows, checked = request(OUT/'inputs/proof.jsonl', OUT/'inputs/request.json')
    failure = load(OUT/'failure.json')
    outer = load(OUT/'failure-frame-3.json')
    boolean = load(OUT/'failure-frame-6.json')
    original = load(OUT/'failure-frame-8.json')
    call = load(OUT/'failure-frame-9.json')
    event = load(OUT/'trace/event-00219.json')
    parent = load(OUT/'trace/event-00196.json')
    index = load(OUT/'trace/index.json')
    arithmetic = load(OUT/'integration-reception.json')
    received = load(OUT/'trace-received-prefix.json')['events']
    require(failure['stage'] == 'emission' and outer['i'] == 22 and
            exact_equal(outer['r'], rows[22]) and rows[22]['rule'] == 'axiom',
            'exact failed source record')
    require(len(index) == len(received) == 220 and arithmetic['events'] == 220 and
            arithmetic['complete_trace_prefix_received'] is True and
            arithmetic['accepted'] is False and arithmetic['complete_KH_received'] is False and
            not arithmetic['failures'], 'complete independent arithmetic prefix receipt')
    for j, item in enumerate(index):
        require(item['index'] == received[j]['index'] == j and
                item['kind'] == received[j]['kind'], 'complete received event inventory')
    require([j for j,x in enumerate(index) if x['kind'] == 'commutator-input' and
             not any(y['kind']=='commutator-output' and y.get('parent')==j for y in received)] == [219],
            'exact absent commutator output')
    require([j for j,x in enumerate(index) if x['kind'] == 'boolean-input' and
             not any(y['kind']=='boolean-output' and y.get('parent')==j for y in received)] == [196],
            'exact absent Boolean output')
    require(event['parent'] == 196 and event['entry'] == 'm.witness' and
            exact_equal([event['f'],event['g']], [original['f'],original['g']]) and
            exact_equal(parent['graph'],boolean['g']), 'full original operand/parent frame bindings')
    jobs = nested_schedule(normalized(parent['graph']))
    attempted = [j for j,x in enumerate(received) if x['kind']=='commutator-input' and x['parent']==196]
    require(attempted == list(range(197,220,2)) and
            all(exact_equal([load(OUT/'trace'/('event-%05d.json'%j))[k] for k in ('f','g')],
                            list(jobs[i])) for i,j in enumerate(attempted)),
            'every attempted ordered normalized-parent nested pair')
    require(exact_equal([event['f'],event['g']], list(jobs[11])), 'twelfth nested recipe call')
    for k in ('f','g'):
        require(exact_equal(event['restrictions'][k]['trimmed'],call[k]),
                'complete actual restricted constructor operands')
    new = counts(call['f'],call['g'])
    old = counts(event['f'],event['g'])
    require(exact_equal(new,event['trimmed_ledger']) and
            exact_equal(old,event['original_ledger']) and
            all(new[k] == call[k] for k in ('p','q')) and
            (new['vertices'],new['edges']) == (call['nv'],call['ne']),
            'independent exact rejected ledger and complete failure operands')
    require(new['actual'] == 3_586_238 > CAPS['records'] and
            failure['detail'] == [dict(stage='L035 preflight',actual=new['actual'],
                                      required=CAPS['records'],resource='records')],
            'exact unchanged record-cap failure')
    n, nd = len(req['alphabet']),len(req['dictionary']['placeholders'])
    prefix = graph(outer['out'],True,n,nd)
    partial_boolean = graph(boolean['out'],False,n,nd)
    operands = {k:graph(call[k],False,n,nd) for k in ('f','g')}
    transport = symbol_map(req['alphabet'],req['dictionary'])
    binding = Binding(index,transport)
    blocks, cursor = outer['blocks'], 0
    vertex, edge = len(rows)+1, 0
    fs = [r['f'] for r in rows]

    def block(i, role, kind, args, parent_ref, expected=None, factors=None):
        nonlocal cursor, vertex, edge
        b = blocks[cursor]
        cursor += 1
        require((b['line'],b['role'],b['kind'],b['arguments'],b['parent']) ==
                (i,role,kind,args,parent_ref), 'exact complete source/block metadata')
        lo, hi = b['vertex_range']
        first, last = b['edge_range']
        s, t = b['entry'],b['exit']
        require(lo == vertex and first == edge and lo < hi <= prefix['vertices'] and
                first+2 <= last <= prefix['edges'] and lo <= s < hi and lo <= t < hi,
                'complete contiguous fresh prefix partitions/endpoints')
        interior = outer['out']['edges'][first:last-2]
        require(all(lo <= u < hi and lo <= v < hi for u,v,_ in interior), 'fresh interiors')
        require(exact_equal(outer['out']['edges'][last-2:last],
                            [[0 if parent_ref is None else parent_ref+1,s,[['one']]],
                             [t,i+1,[['one']]]]), 'exact retained connectors')
        local = dict(vertices=hi-lo,source=s-lo,sink=t-lo,
                     edges=[[u-lo,v-lo,lab] for u,v,lab in interior])
        if factors is None:
            require(exact_equal(local,typed(expected,transport)), 'complete trace output copied to K prefix')
        else:
            copied_composition(local,[typed(g,transport) for g in factors],'product')
        vertex, edge = hi,last

    for i,r in enumerate(rows[:22]):
        tag, f, refs = r['rule'],r['f'],r['refs']
        factors = None
        if tag in ('axiom','contraction'):
            a = f[2] if tag=='axiom' else f
            seed = binding.boolean(binding.translation(a))
            kind,args = 'boolean',[a]
        elif tag=='expansion':
            a,b = fs[refs[0]],f[1]
            aa,bb = binding.translation(a),binding.translation(b)
            seed = binding.commutator(aa,bb,None)
            kind,args = 'commutator',[a,b]
        elif tag=='cut':
            a,b,c = fs[refs[0]][1],fs[refs[0]][2],fs[refs[1]][2]
            bb,cc = binding.translation(b),binding.translation(c)
            w = binding.commutator(bb,cc,None)
            pre = binding.translation(['not',a])
            factors,seed = [pre,w],None
            kind,args = 'prefixed-commutator',[a,b,c]
        else:
            require(tag in ('true','not-false','association'),'known zero seed')
            seed = dict(vertices=2,source=0,sink=1,edges=[])
            kind,args = 'zero',[]
        block(i,'seed',kind,args,None,seed,factors)
        formulas = ([f[1]] if tag=='expansion' else ['false'] if tag in ('contraction','association') else
                    [fs[refs[1]][2],fs[refs[0]][2]] if tag=='cut' else [])
        for j,formula in zip(refs,formulas):
            block(i,'transition','translation',[formula],j,binding.translation(formula))
    require(cursor == len(blocks) and vertex == prefix['vertices'] and edge == prefix['edges'] and
            binding.position == 195 and outer['out']['source'] == 0 and outer['out']['sink'] == 31,
            'every complete source-prefix graph record and all source-root vertices')
    # Event 195 translates the pending source record; event 196 is its Boolean input.
    require(exact_equal(binding.translation(rows[22]['f'][2]),parent['graph']) and
            binding.position == 196, 'pending axiom exact translation binding')
    isolated = load(HERE/'output-475/trimmed-pair.json')
    earlier = load(OUT/'trace/event-00201.json')
    earlier_out = load(OUT/'trace/event-00202.json')
    require(exact_equal(earlier['restrictions'],isolated['operands']) and
            earlier_out['parent'] == 201 and earlier['trimmed_ledger']['actual'] == 45_474 and
            earlier_out['graph']['vertices']+len(earlier_out['graph']['edges']) == 45_474,
            'isolated passing pair is now actually constructed and received')
    require(not (OUT/'emitted/K.json').exists() and not (OUT/'emitted/H.json').exists(),
            'no complete K/H output')
    hashes = load(OUT/'preservation-before.json')
    hashes.update(load(OUT/'source-hashes.json'))
    hashes.update(load(OUT/'run-scope.json')['source_hashes'])
    for p,digest in hashes.items():
        require(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==digest,'unchanged recorded bytes')
    extra = {str(Path(__file__).resolve().relative_to(ROOT)):
             hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    result = dict(verified_resource_stop=True, complete_KH_received=False,
                  failed_source_line_zero_based=22, failed_event=219, boolean_parent=196,
                  nested_call_zero_based=11, completed_source_lines=list(range(22)),
                  all_source_root_vertices=31, retained_blocks=len(blocks),
                  complete_prefix_trace_bindings=True,prefix=prefix,partial_boolean=partial_boolean,
                  operands=operands,old_ledger=old,rejected_ledger=new,
                  excess_records=new['actual']-CAPS['records'],
                  pending_operand_words=[len(x['original_polynomial']) for x in received[219]['operands']],
                  pending_target_words=len(received[219]['target']),
                  received_commutator_outputs=sum(x['kind']=='commutator-output' for x in received),
                  received_boolean_outputs=sum(x['kind']=='boolean-output' for x in received),
                  unchanged_hashes=hashes,supplementary_source_hashes=extra,
                  scope='Complete saved structural/recipe/count evidence; no unfinished Boolean/partial-K or full K/H identities.',
                  caps=CAPS,failures=[])
    write_json(path,result)
    print(dict(verified_resource_stop=True,actual=new['actual'],required=CAPS['records'],
               retained_prefix_records=prefix['records'],retained_blocks=len(blocks),
               operand_records={k:v['records'] for k,v in operands.items()},
               failures=[],path=str(path)))


if __name__=='__main__':
    main()
