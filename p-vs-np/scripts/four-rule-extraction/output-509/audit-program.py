"""Step 509: nested outer selections and complete variable-union operands.

Read-only original source phase; no graph, word or coordinate experiment.
Logical set member volumes are NOT implementation-level set scan counts.
"""
import ast
from collections import Counter
import dis
import hashlib
import json
from pathlib import Path
import sys
import time
import traceback

import parameterized_input as p
import preflight_job7_transport as original

HERE = Path(__file__).resolve().parent
OUT = HERE/'output-509'
LIMIT, SECONDS, RESERVE = 100_000_000, 900, 1_000_000


def main():
    p.require(not OUT.exists(), 'fresh output only')
    OUT.mkdir()
    with (OUT/'audit-program.py').open('xb') as stream:
        stream.write(Path(__file__).read_bytes())
    start = time.monotonic()
    budget, units = Counter(), 0
    report = dict(status='IN_PROGRESS', failures=[], total_work_bound=False,
                  set_table_scan_count='UNKNOWN', graph_regeneration=False,
                  coordinate_search=False, word_expansion=False)

    def tick(kind, n=1):
        nonlocal units
        p.require(units+n <= LIMIT, 'audit item/event ceiling before next work')
        units += n; budget[kind] += n
        if units % 4096 == 0:
            p.require(time.monotonic()-start <= SECONDS, 'audit timer')

    def equal(a, b):
        tick('complete_value_comparisons')
        if type(a) is not type(b): return False
        if type(a) is dict:
            return a.keys() == b.keys() and all(equal(a[k], b[k]) for k in a)
        if type(a) in (list, tuple):
            return len(a) == len(b) and all(equal(x,y) for x,y in zip(a,b))
        return a == b

    try:
        p.require(p.CAPS == original.EXPECTED_CAPS, 'all original CAPS unchanged')
        p.require(sys.gettrace() is None, 'no preexisting trace')
        p.require(sys.version_info[:3] == (3,15,0), 'checked runtime version')
        source, request = HERE/'output-489/inputs/proof.jsonl', HERE/'output-489/inputs/request.json'
        raw, req_raw = p.read_bytes(source,'input_bytes'), p.read_bytes(request,'input_bytes')
        tick('independent_input_bytes',len(raw)+len(req_raw))
        def pairs(xs):
            out = {}
            for k,v in xs:
                tick('independent_decode_pairs')
                p.require(k not in out, 'independent duplicate rejection')
                out[k] = v
            return out
        req = json.loads(req_raw,object_pairs_hook=pairs)
        rows = [json.loads(line,object_pairs_hook=pairs) for line in raw.splitlines()]
        records, alphabet = rows[1:], req['alphabet']
        p.require(len(alphabet) == len(set(alphabet)) == 6, 'six distinct bound names')
        paths = [Path(p.__file__), HERE/'preflight_job7_transport.py', HERE.parent/'parity-four-rule/checker.py']
        texts = {}
        report['source_snapshots'] = {}
        for path in paths:
            body = path.read_bytes(); tick('source_snapshot_bytes',len(body))
            texts[str(path)] = body.decode()
            name = 'literal-checker.py' if path.name == 'checker.py' else path.name
            with (OUT/name).open('xb') as stream: stream.write(body)
            report['source_snapshots'][str(path.relative_to(HERE.parent))] = dict(
                bytes=len(body),sha256=hashlib.sha256(body).hexdigest(),snapshot=name)
        p.require(Path(p.__file__).read_bytes() == (HERE/'output-508/parameterized_input.py').read_bytes(),
                  'parameterized source matches prior parser audit')
        manifest = json.loads((HERE/'output-502/manifest.json').read_bytes())
        p.require(hashlib.sha256(paths[1].read_bytes()).hexdigest() == manifest['script_sha256'],
                  'primary source matches original manifest')
        pf, cf = str(paths[0]), str(paths[2])
        pm, cm = ast.parse(texts[pf]), ast.parse(texts[cf])
        for node in list(ast.walk(pm))+list(ast.walk(cm)): tick('source_ast_nodes')
        vg = next(z for z in cm.body if isinstance(z,ast.FunctionDef) and z.name == 'variables')
        p.require(ast.unparse(vg) == "def variables(t):\n    if isinstance(t, str):\n        return set() if t in ('true', 'false') else {t}\n    return set().union(*(variables(c) for c in t[1:]))", 'full variables body pin')
        nested = [z for z in ast.walk(pm) if isinstance(z,ast.GeneratorExp) and len(z.generators) == 2]
        p.require(len(nested) == 1 and nested[0].lineno == 153 and ast.unparse(nested[0]) ==
                  "(('commutator', (x, y)) for i, x in enumerate(alphabet) for y in alphabet[i + 1:])",
                  'unique full nested generator pin')

        # Independent occurrence tree: tuple syntax, integer bit masks, no
        # original variables(), child-set union, or identity-based node merge.
        def oracle(t):
            tick('independent_tree_occurrences')
            if type(t) is str:
                p.require(t in ('true','false') or t in alphabet,'independent names')
                return dict(tree=t,mask=0 if t in ('true','false') else 1<<alphabet.index(t),children=[],depth=1)
            p.require(type(t) is list and ((t[0]=='not' and len(t)==2) or
                       (t[0]=='or' and len(t)==3)), 'independent ordered syntax')
            children, mask = [], 0
            for child in t[1:]:
                tick('independent_tree_links')
                z = oracle(child); children.append(z); mask |= z['mask']
            return dict(tree=tuple([t[0]]+[z['tree'] for z in children]),mask=mask,
                        children=children,depth=1+max(z['depth'] for z in children))
        goal = oracle(req['goal'])
        roots = [oracle(row['f']) for row in records]
        expected, row_oracles, census = [], [], Counter()
        def names(mask):
            tick('mask_name_slots',len(alphabet))
            return sorted(x for i,x in enumerate(alphabet) if mask & (1<<i))
        for i,root in enumerate(roots):
            stack = [root]; metrics = Counter()
            while stack:
                tick('oracle_preorder_nodes')
                z = stack.pop(); z['record'] = i
                expected.append(z)
                arity = len(z['children']); mask = z['mask']
                cmasks = tuple(c['mask'] for c in z['children'])
                census[(arity,mask,cmasks)] += 1
                metrics['nodes'] += 1
                if arity:
                    metrics['union_calls'] += 1
                    metrics['union_arguments'] += arity
                    metrics['union_logical_input_members'] += sum(m.bit_count() for m in cmasks)
                    metrics['union_logical_output_members'] += mask.bit_count()
                else:
                    metrics['nonconstant_singletons' if mask else 'empty_constant_sets'] += 1
                stack.extend(reversed(z['children']))
            row_oracles.append(dict(record=i,root_mask=root['mask'],**metrics))
        expected_names = [names(z['mask']) for z in expected]
        active, next_node, completed = [], 0, 0
        actual_rows = [Counter() for _ in records]
        outer, yielded, gcounters, var_counts = [], [], Counter(), Counter()
        generator_code, opcode_map = None, None
        r = original.Run(); original.R = r; r.stage = 'fixed implicit-source audit only'

        def observer(frame,event,arg):
            nonlocal next_node,completed,generator_code,opcode_map
            tick('trace_events')
            before = r.visits
            original.observe_source(frame,event,arg)
            delta = r.visits-before
            code = frame.f_code
            if code.co_filename == cf and code.co_name == 'variables':
                var_counts[event+'_original_charges'] += delta
                if event == 'call':
                    p.require(next_node < len(expected),'no extra variable invocation')
                    j = next_node; next_node += 1; z = expected[j]
                    p.require(equal(frame.f_locals['t'],z['tree']),'entire ordered variables input')
                    p.require(delta == 1,'one original tree-node call charge')
                    active.append([id(frame),j,[]]); var_counts['calls'] += 1
                elif event == 'return':
                    p.require(active and active[-1][0] == id(frame),'complete LIFO variable return')
                    _,j,children = active.pop(); z = expected[j]
                    p.require(type(arg) is set and all(type(x) is str for x in arg),'exact returned set type')
                    tick('returned_set_member_comparisons',len(arg))
                    value = sorted(arg)
                    p.require(equal(value,expected_names[j]),'all returned names, no extras')
                    wanted = [names(c['mask']) for c in z['children']]
                    p.require(equal(children,wanted),'all child operands in order, no missing child')
                    metrics = actual_rows[z['record']]; metrics['nodes'] += 1
                    if z['children']:
                        metrics['union_calls'] += 1; metrics['union_arguments'] += len(children)
                        metrics['union_logical_input_members'] += sum(map(len,children))
                        metrics['union_logical_output_members'] += len(value)
                    else:
                        metrics['nonconstant_singletons' if value else 'empty_constant_sets'] += 1
                    if active: active[-1][2].append(value)
                    completed += 1; var_counts['returns'] += 1
                elif event == 'exception':
                    raise AssertionError('unexpected variables exception')
            if code.co_filename == pf and code.co_name == '<genexpr>' and code.co_firstlineno == 153:
                if generator_code is None:
                    generator_code = code
                    instructions = list(dis.get_instructions(code))
                    opcode_map = {x.offset:x for x in instructions}
                    loops = [x for x in instructions if x.opname == 'FOR_ITER']
                    p.require([x.offset for x in loops] == [20,56], 'two exact runtime iterator sites')
                    p.require(opcode_map[30].opname == 'LOAD_DEREF' and
                              opcode_map[30].argval == 'alphabet','post-outer-unpack evidence site')
                    report['nested_instructions'] = [dict(offset=x.offset,opname=x.opname,argrepr=x.argrepr)
                                                     for x in instructions]
                p.require(code is generator_code,'single nested generator code')
                frame.f_trace_opcodes = True
                gcounters[event+'_original_charges'] += delta
                if event == 'call':
                    gcounters['resumptions'] += 1
                    p.require(delta == 1,'original nested resumption charge')
                elif event == 'opcode':
                    p.require(delta == 0,'no original opcode charge')
                    if frame.f_lasti == 20: gcounters['outer_next_attempts'] += 1
                    if frame.f_lasti == 56: gcounters['inner_next_attempts'] += 1
                    if frame.f_lasti == 30:
                        i,x = frame.f_locals['i'],frame.f_locals['x']
                        p.require(type(i) is int and i == len(outer) and x == alphabet[i],
                                  'all outer selections in original order')
                        suffix = alphabet[i+1:]
                        outer.append(dict(index=i,name=x,suffix=suffix,original_opcode_charge=delta))
                        tick('outer_selection_checks')
                elif event == 'return':
                    if opcode_map[frame.f_lasti].opname == 'YIELD_VALUE':
                        yielded.append(arg); gcounters['yields'] += 1
                    else:
                        p.require(opcode_map[frame.f_lasti].opname == 'RETURN_VALUE' and arg is None,
                                  'normal final exhaustion')
                        gcounters['exhaustions'] += 1
                elif event == 'exception': raise AssertionError('unexpected nested generator exception')
            return observer

        sys.settrace(observer)
        try:
            actual_req,actual_raw,actual_records,checked = p.request(source,request)
            bounds = p.input_bounds(actual_req,actual_raw,actual_records,request)
        finally: sys.settrace(None)
        p.require(not active and next_node == completed == len(expected),'every occurrence fully received')
        for i,(metrics,wanted) in enumerate(zip(actual_rows,row_oracles)):
            p.require(equal(dict(metrics),{k:v for k,v in wanted.items() if k not in ('record','root_mask')}),
                      'entire per-record operand ledger')
        all_pairs = [('commutator',(x,y)) for i,x in enumerate(alphabet) for y in alphabet[i+1:]]
        p.require(equal(yielded,all_pairs) and len(outer)==6 and outer[-1]['suffix']==[],
                  'all nested pairs plus final zero-yield outer selection')
        p.require(gcounters['resumptions']==16 and gcounters['yields']==15 and
                  gcounters['exhaustions']==1 and gcounters['outer_next_attempts']==7 and
                  gcounters['inner_next_attempts']==21,'complete outer/inner iteration accounting')
        old = json.loads((HERE/'output-502/preflight.json').read_bytes())
        p.require(equal(dict(r.source_observer),old['source_observer']) and r.visits==167_322,
                  'entire original source observer unchanged by extra tracing')
        p.require(equal(actual_req,req) and equal(actual_records,records) and actual_raw==raw,
                  'complete immutable input correspondence')
        expected_checked = dict(accepted=True,records=len(records),rule_counts=dict(Counter(x['rule'] for x in records)),
            formula_nodes=len(expected),bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
        p.require(equal(checked,expected_checked),'all literal receipt fields')
        actual_bounds = dict(source_bytes=len(raw),request_bytes=len(req_raw),
            tree_depth=max([goal['depth']]+[z['depth'] for z in roots]),
            tree_nodes='PENDING',source_lines=len(records),alphabet=len(alphabet),
            dictionary_entries=len(req['dictionary']['placeholders']),
            name_bytes=max(len(x.encode()) for x in alphabet+[z['name'] for z in req['dictionary']['placeholders']]))
        # Goal size is independently traversed; do not trust a receipt or pin.
        stack,goal_nodes = [goal],0
        while stack:
            tick('independent_goal_size_nodes'); z=stack.pop();goal_nodes+=1;stack.extend(z['children'])
        actual_bounds['tree_nodes'] = len(expected)+goal_nodes
        expected_bounds = dict(actual=actual_bounds,required={k:p.CAPS['input_bytes'] if k in
            ('source_bytes','request_bytes') else p.CAPS[k] for k in actual_bounds})
        p.require(equal(bounds,expected_bounds),'all independent input bounds')
        for path in paths:
            p.require(path.read_text()==texts[str(path)],'original module bytes unchanged')
        p.require(source.read_bytes()==raw and request.read_bytes()==req_raw,'original input bytes unchanged')
        totals = Counter()
        for metrics in actual_rows: totals.update(metrics)
        report.update(status='NARROW_IMPLICIT_SOURCE_CLASSES_RECEIVED',caps=p.CAPS,
            runtime=sys.version,outer_selections=outer,nested_yields=yielded,
            nested_counters=dict(gcounters),variable_counters=dict(var_counts),
            variable_totals=dict(totals),per_record_oracle=row_oracles,
            complete_occurrence_type_census=[dict(arity=a,mask=m,child_masks=list(cs),occurrences=n)
                for (a,m,cs),n in sorted(census.items())],
            checked_variable_inputs=next_node,checked_variable_outputs=completed,
            original_source_visits=r.visits,original_source_observer=dict(r.source_observer),
            new_disjoint_outer_selections=6,partial_augmented_source_items=168_937+6,
            partial_augmented_original_three_run_items=75_868_976+6,
            union_member_volumes_added_to_item_subtotal=False,literal_check=checked,input_bounds=bounds,
            remaining='All other implicit operations, actual set table scans/copies/hashes/allocations, parser/read/bit/index costs, complete historical failed/supplement work, transport/schema/byte/live peaks and all coordinates/equalities remain unresolved. No complete ledger, format rejection, cap overflow or unrestricted complexity conclusion.')
    except Exception as err:
        sys.settrace(None)
        report.update(status='FAILED',failures=[dict(type=type(err).__name__,message=str(err),
                      traceback=traceback.format_exc())])
    report.update(audit_item_event_units=units,audit_budget=dict(budget),required_item_event_units=LIMIT,
                  elapsed_seconds=time.monotonic()-start,required_seconds=SECONDS,
                  required_evidence_bytes=p.CAPS['certificate_bytes'],reserve_bytes=RESERVE,
                  program_snapshots_and_receipt_bytes=0)
    fixed = Path(__file__).stat().st_size+sum(z.stat().st_size for z in OUT.iterdir() if z.is_file())
    while True:
        encoded = json.dumps(report,ensure_ascii=True,separators=(',',':')).encode()
        total = fixed+len(encoded)
        if report['program_snapshots_and_receipt_bytes']==total: break
        report['program_snapshots_and_receipt_bytes']=total
    p.require(total <= RESERVE and time.monotonic()-start <= SECONDS,'complete evidence reserve/time')
    path = OUT/'implicit-source.json'
    with path.open('xb') as stream: stream.write(encoded)
    print(json.dumps(dict(status=report['status'],actual_units=units,required_units=LIMIT,
        actual_evidence_bytes=total,required_reserve_bytes=RESERVE,
        new_outer_selections=report.get('new_disjoint_outer_selections','UNKNOWN'),
        variable_totals=report.get('variable_totals','UNKNOWN'),failures=report['failures'],path=str(path))))


if __name__ == '__main__': main()
