"""Step 510: fixed source non-variable sets and typed JSON, not C costs."""
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
OUT = HERE/'output-510'
LIMIT, SECONDS, RESERVE = 100_000_000, 900, 1_000_000


def main():
    p.require(not OUT.exists(), 'fresh evidence directory')
    OUT.mkdir()
    (OUT/'audit-program.py').write_bytes(Path(__file__).read_bytes())
    start = time.monotonic()
    units, budget = 0, Counter()
    report = dict(status='IN_PROGRESS', failures=[], total_work_bound=False,
                  c_set_encoder_cost='UNKNOWN', graph_regeneration=False,
                  coordinate_search=False, word_expansion=False)

    def tick(kind, n=1):
        nonlocal units
        p.require(units+n <= LIMIT, 'selected audit unit limit before work')
        units += n; budget[kind] += n
        if units % 4096 == 0:
            p.require(time.monotonic()-start <= SECONDS, 'periodic audit timer')

    def equal(a, b):
        tick('complete_value_comparisons')
        if type(a) is not type(b): return False
        if type(a) is dict:
            return a.keys()==b.keys() and all(equal(a[k], b[k]) for k in a)
        if type(a) in (list, tuple):
            return len(a)==len(b) and all(equal(x,y) for x,y in zip(a,b))
        return a==b

    def encode(x):
        # Independent encoder for the complete observed typed domain only.
        tick('independent_encoding_nodes')
        if type(x) is str:
            for ch in x:
                tick('independent_encoding_characters')
                p.require(32 <= ord(ch) <= 126 and ch not in ('"','\\'),
                          'exact safe ASCII domain, no omitted escaping')
            return '"'+x+'"'
        p.require(type(x) is list, 'observed typed domain is lists/strings')
        return '['+','.join(encode(v) for v in x)+']'

    try:
        p.require(p.CAPS==original.EXPECTED_CAPS, 'unchanged original CAPS')
        p.require(sys.version_info[:3]==(3,15,0) and sys.gettrace() is None,
                  'pinned runtime and no existing observer')
        source, request = HERE/'output-489/inputs/proof.jsonl', HERE/'output-489/inputs/request.json'
        raw, req_raw = source.read_bytes(), request.read_bytes()
        tick('independent_input_bytes',len(raw)+len(req_raw))
        def pairs(xs):
            result = {}
            for k,v in xs:
                tick('independent_decode_pairs')
                p.require(k not in result, 'independent duplicate rejection')
                result[k]=v
            return result
        req = json.loads(req_raw,object_pairs_hook=pairs)
        header, *rows = [json.loads(line,object_pairs_hook=pairs) for line in raw.splitlines()]
        alphabet, ps = req['alphabet'], req['dictionary']['placeholders']
        p.require(len(rows)==212 and len(alphabet)==6 and len(ps)==21, 'fixed input cardinalities')
        paths = [HERE/'preflight_job7_transport.py', Path(p.__file__), HERE.parent/'parity-four-rule/checker.py']
        texts = {}; report['source_snapshots'] = {}
        for path in paths:
            body = path.read_bytes(); tick('source_snapshot_bytes',len(body))
            name = 'literal-checker.py' if path.name=='checker.py' else path.name
            p.require(body==(HERE/'output-509'/name).read_bytes(), 'complete previous source snapshot equality')
            (OUT/name).write_bytes(body); texts[str(path)] = body.decode()
            report['source_snapshots'][name] = dict(bytes=len(body),sha256=hashlib.sha256(body).hexdigest())
        manifest = json.loads((HERE/'output-502/manifest.json').read_bytes())
        p.require(hashlib.sha256(paths[0].read_bytes()).hexdigest()==manifest['script_sha256'],
                  'original manifest source binding')
        pf, cf = str(paths[1]), str(paths[2])
        # Positions identify each actual CALL, without patching set, typed or fields.
        sites, census = {}, []
        for filename, names in ((pf,('fields','request')),(cf,('_check_stream',))):
            module = ast.parse(texts[filename])
            for node in ast.walk(module): tick('source_ast_nodes')
            for fn in module.body:
                if not isinstance(fn,ast.FunctionDef) or fn.name not in names: continue
                for node in ast.walk(fn):
                    if isinstance(node,ast.Call) and isinstance(node.func,ast.Name) and node.func.id=='set':
                        position = (node.lineno,node.end_lineno,node.col_offset,node.end_col_offset)
                        sites[(filename,fn.name,position)] = node
                        census.append(dict(file=Path(filename).name,function=fn.name,line=node.lineno,
                                           expression=ast.unparse(node)))
        report['set_call_ast_census'] = sorted(census,key=lambda z:(z['file'],z['line'],z['expression']))
        expected_fields = [(req,'format source_sha256 goal alphabet dictionary'),
            (req['dictionary'],'alphabet placeholders')]+[(z,'name kind originals polynomial') for z in ps]+[
            (header,'format alphabet goal')]+[(z,'rule f refs') for z in rows]
        expected_typed = [req['dictionary']['alphabet'],alphabet]
        for z in ps:
            a=z['originals']
            poly=[[a[0],a[0]],[a[0]]] if z['kind']=='boolean' else [[a[0],a[1]],[a[1],a[0]]]
            expected_typed.extend([z['polynomial'],poly])
        expected_typed.extend([header['alphabet'],alphabet,header['goal'],req['goal'],rows[-1]['f'],req['goal']])
        expected_json = [encode(v) for v in expected_typed]
        # Full expected dictionary associations use independent index pairs.
        associations = [('boolean',(x,)) for x in alphabet]
        for i in range(len(alphabet)):
            for j in range(i+1,len(alphabet)):
                tick('independent_dictionary_pairs'); associations.append(('commutator',(alphabet[i],alphabet[j])))
        def normalized(values):
            return sorted([[k,list(a)] for k,a in values])
        wanted_associations = normalized(associations)
        schema, typed, trees, states, calls = [], [], [], [], []
        code_maps = {}; field_active = {}; typed_active = {}
        r=original.Run(); original.R=r; r.stage='source set/serialization audit only'
        selected_events=Counter()

        def observe(frame,event,arg):
            tick('trace_events')
            before=r.visits; original.observe_source(frame,event,arg); delta=r.visits-before
            filename,name = frame.f_code.co_filename,frame.f_code.co_name
            local=frame.f_locals
            if filename==pf and name in ('fields','typed'):
                selected_events[name+'_'+event+'_original_charges'] += delta
                if event=='exception': raise AssertionError('source schema/typed exception')
                if name=='fields':
                    if event=='call':
                        i=len(schema); p.require(i<len(expected_fields),'no extra schema call')
                        x,keys=expected_fields[i]
                        p.require(equal(local['x'],x) and local['keys']==keys, 'complete schema operands and order')
                        p.require(sorted(x)==sorted(keys.split()), 'independent exact schema key set')
                        field_active[id(frame)]=i
                        schema.append(dict(index=i,keys=list(x),required=keys.split(),returned=False))
                    elif event=='return':
                        i=field_active.pop(id(frame));p.require(arg is None,'schema return')
                        schema[i]['returned']=True
                else:
                    if event=='call':
                        i=len(typed);p.require(i<len(expected_typed),'no extra typed call')
                        p.require(equal(local['x'],expected_typed[i]),'complete ordered typed argument')
                        typed_active[id(frame)]=i
                        typed.append(dict(index=i,argument=expected_typed[i],output=None,output_bytes=None))
                    elif event=='return':
                        i=typed_active.pop(id(frame))
                        p.require(type(arg) is str and arg==expected_json[i], 'complete independent JSON result')
                        tick('complete_encoded_character_comparisons',len(arg))
                        typed[i].update(output=arg,output_bytes=len(arg.encode('ascii')))
            if filename==pf and name=='check_tree' and event=='call':
                i=len(trees); wanted=([req['goal']]+[z['f'] for z in rows])[i]
                p.require(equal(local['t'],wanted) and type(local['alphabet']) is set and
                          sorted(local['alphabet'])==sorted(alphabet),'every actual tree alphabet set')
                tick('alphabet_set_members',len(alphabet)); trees.append(i)
            if filename==pf and name=='request' and event=='line':
                line=frame.f_lineno
                if line==153:
                    p.require(normalized(local['expected'])==normalized(associations[:6]),'initial Boolean expected set')
                if line in (155,159,164,165,168):
                    # Iteration-entry line 155 has 22 hits including exhaustion.
                    if line==155: i=sum(1 for z in states if z['line']==155)
                    elif line==168: i=len(ps)
                    else: i=next(j for j,z in enumerate(ps) if equal(local['p'],z))
                    names_end=i+(line in (164,165))
                    seen_end=i+(line==165)
                    if line in (155,168): names_end=seen_end=i
                    actual_names=sorted(local['names']); actual_seen=normalized(local['seen'])
                    want_names=sorted(z['name'] for z in ps[:names_end])
                    want_seen=normalized((z['kind'],tuple(z['originals'])) for z in ps[:seen_end])
                    p.require(actual_names==want_names and actual_seen==want_seen and
                              normalized(local['expected'])==wanted_associations,'all complete dictionary set states')
                    states.append(dict(line=line,index=i,names=actual_names,seen=actual_seen))
            if (filename==pf and name in ('fields','request')) or (filename==cf and name=='_check_stream'):
                frame.f_trace_opcodes=True
                if event=='opcode':
                    if frame.f_code not in code_maps:
                        code_maps[frame.f_code]={z.offset:z for z in dis.get_instructions(frame.f_code)}
                    ins=code_maps[frame.f_code][frame.f_lasti]
                    pos=ins.positions
                    key=(filename,name,(pos.lineno,pos.end_lineno,pos.col_offset,pos.end_col_offset))
                    if ins.opname=='CALL' and key in sites:
                        node=sites[key]; expression=ast.unparse(node)
                        if not node.args: operand=[]
                        elif isinstance(node.args[0],ast.Name):
                            value=local[node.args[0].id]; operand=list(value)
                            if type(value) is dict:
                                wanted=header if node.args[0].id=='h' else rows[local['i']] if name=='_check_stream' else local['x']
                                p.require(equal(value,wanted),'complete schema source object')
                            elif node.args[0].id=='alphabet': p.require(equal(value,alphabet),'complete repeated alphabet operand')
                        else:
                            p.require(expression=='set(keys.split())','only pinned split operand')
                            operand=local['keys'].split()
                        tick('logical_constructor_input_members',len(operand))
                        calls.append(dict(function=name,line=node.lineno,expression=expression,
                                          operand=operand,original_opcode_charge=delta))
                        p.require(delta==0,'no original constructor opcode charge')
            return observe

        sys.settrace(observe)
        try:
            actual_req,actual_raw,actual_rows,checked=p.request(source,request)
            bounds=p.input_bounds(actual_req,actual_raw,actual_rows,request)
        finally: sys.settrace(None)
        p.require(len(schema)==len(expected_fields)==236 and not field_active and
                  all(z['returned'] for z in schema),'all schema returns')
        p.require(len(typed)==len(expected_typed)==50 and not typed_active and
                  all(z['output'] is not None for z in typed),'all typed returns')
        p.require(len(trees)==213 and len(states)==86,'all tree and dictionary state checkpoints')
        p.require(equal(actual_req,req) and equal(actual_rows,rows) and actual_raw==raw,'full immutable correspondence')
        old=json.loads((HERE/'output-502/preflight.json').read_bytes())
        p.require(equal(dict(r.source_observer),old['source_observer']) and r.visits==167_322,'unchanged complete original observer')
        for path in paths: p.require(path.read_text()==texts[str(path)],'source snapshots unchanged')
        p.require(source.read_bytes()==raw and request.read_bytes()==req_raw,'input bytes unchanged')
        grouped={}
        for z in calls:
            key=str((z['function'],z['line'],z['expression']))
            if key not in grouped: grouped[key]=dict(calls=0,logical_input_members=0)
            grouped[key]['calls']+=1;grouped[key]['logical_input_members']+=len(z['operand'])
        p.require(len(calls)==1114, 'complete non-variable constructor call count')
        report.update(status='NARROW_SOURCE_SET_TYPED_CLASSES_RECEIVED',caps=p.CAPS,runtime=sys.version,
            schema_calls=schema,typed_calls=typed,tree_alphabet_sets_received=len(trees),
            dictionary_states=states,set_calls=calls,set_call_groups=grouped,
            total_builtin_set_calls=len(calls),logical_constructor_input_members=sum(len(z['operand']) for z in calls),
            typed_output_ascii_bytes=sum(z['output_bytes'] for z in typed),original_selected_event_charges=dict(selected_events),
            original_source_visits=r.visits,original_source_observer=dict(r.source_observer),literal_check=checked,input_bounds=bounds,
            partial_augmented_source_items=168_943,partial_augmented_original_three_run_items=75_868_982,
            logical_volumes_added_to_item_subtotal=False,
            remaining='Temporary set outputs are not stack-inspected; inputs and program conditions/stored states are checked. Actual C set/split/hash/sort/encoder costs, checker default JSON roundtrip, other container/equality work, full transport/schema/framing/live peaks and complete historical failed/supplement work remain UNKNOWN/unresolved.')
    except Exception as err:
        sys.settrace(None)
        report.update(status='FAILED',failures=[dict(type=type(err).__name__,message=str(err),traceback=traceback.format_exc())])
        for name in ('schema','typed','trees','states','calls'):
            if name in locals(): report['partial_'+name]=locals()[name]
    report.update(audit_item_event_units=units,audit_budget=dict(budget),required_item_event_units=LIMIT,
                  elapsed_seconds=time.monotonic()-start,required_seconds=SECONDS,
                  required_evidence_bytes=p.CAPS['certificate_bytes'],reserve_bytes=RESERVE,
                  program_snapshots_and_receipt_bytes=0)
    fixed=Path(__file__).stat().st_size+sum(z.stat().st_size for z in OUT.iterdir() if z.is_file())
    while True:
        data=json.dumps(report,ensure_ascii=True,separators=(',',':')).encode()
        total=fixed+len(data)
        if report['program_snapshots_and_receipt_bytes']==total: break
        report['program_snapshots_and_receipt_bytes']=total
    p.require(total<=RESERVE and time.monotonic()-start<=SECONDS,'complete evidence/time reserve')
    path=OUT/'source-sets-typed.json'
    with path.open('xb') as stream: stream.write(data)
    print(json.dumps(dict(status=report['status'],actual_units=units,required_units=LIMIT,
        actual_evidence_bytes=total,required_reserve_bytes=RESERVE,
        set_calls=report.get('total_builtin_set_calls','UNKNOWN'),typed_bytes=report.get('typed_output_ascii_bytes','UNKNOWN'),
        failures=report['failures'],path=str(path))))


if __name__=='__main__': main()
