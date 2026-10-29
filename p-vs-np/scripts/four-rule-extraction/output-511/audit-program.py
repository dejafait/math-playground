"""Step 511: receive fixed checker default JSON interfaces; no C-cost bound."""
from collections import Counter
import hashlib
import json
from pathlib import Path
import sys
import time
import traceback

import parameterized_input as p
import preflight_job7_transport as original

HERE = Path(__file__).resolve().parent
OUT = HERE/'output-511'
LIMIT, SECONDS, RESERVE = 100_000_000, 900, 1_000_000


def main():
    p.require(not OUT.exists(), 'fresh audit output')
    OUT.mkdir()
    (OUT/'audit-program.py').write_bytes(Path(__file__).read_bytes())
    start = time.monotonic()
    units, budget = 0, Counter()
    report = dict(status='IN_PROGRESS', failures=[], total_work_bound=False,
                  c_encoder_decoder_cost='UNKNOWN', graph_regeneration=False,
                  coordinate_search=False, word_expansion=False)

    def tick(kind, n=1):
        nonlocal units
        p.require(units+n <= LIMIT, 'selected unit cap before work')
        units += n; budget[kind] += n
        if units % 4096 == 0:
            p.require(time.monotonic()-start <= SECONDS, 'periodic timer')

    def equal(a,b):
        tick('complete_value_comparisons')
        if type(a) is not type(b): return False
        if type(a) is dict:
            return a.keys()==b.keys() and all(equal(a[k],b[k]) for k in a)
        if type(a) in (list,tuple):
            return len(a)==len(b) and all(equal(x,y) for x,y in zip(a,b))
        return a==b

    def decode(raw):
        # Independent finite-domain parser: safe ASCII strings, unsigned
        # integers, arrays and objects only; reject all other lexical cases.
        text=raw.decode('ascii') if type(raw) is bytes else raw
        i=0
        def white():
            nonlocal i
            while i<len(text) and text[i] in ' \t\r\n':
                tick('independent_parse_characters'); i+=1
        def take():
            nonlocal i
            p.require(i<len(text), 'complete JSON token')
            tick('independent_parse_characters'); c=text[i]; i+=1; return c
        def value(depth=0):
            nonlocal i
            tick('independent_parse_values')
            p.require(depth<=p.CAPS['json_depth'], 'independent depth cap')
            white(); c=take()
            if c=='"':
                chars=[]
                while True:
                    c=take()
                    if c=='"': return ''.join(chars)
                    p.require(32<=ord(c)<=126 and c!='\\', 'actual unescaped safe ASCII string domain')
                    chars.append(c)
            if c in '[{':
                out=[] if c=='[' else {}; close=']' if c=='[' else '}'
                white()
                if i<len(text) and text[i]==close: take(); return out
                while True:
                    child=value(depth+1)
                    if c=='[': out.append(child)
                    else:
                        p.require(type(child) is str and child not in out, 'unique string object key')
                        white(); p.require(take()==':', 'object colon')
                        out[child]=value(depth+1)
                    white(); sep=take()
                    if sep==close: return out
                    p.require(sep==',', 'complete container separator')
            p.require(c in '0123456789', 'actual unsigned integer domain')
            digits=c
            while i<len(text) and text[i] in '0123456789': digits+=take()
            p.require(len(digits)==1 or digits[0]!='0', 'no leading zero')
            return int(digits)
        result=value(); white(); p.require(i==len(text), 'consume complete JSON input')
        return result

    def encode_goal(x):
        # Only the actual formula domain, with default JSON comma spacing.
        tick('independent_encoding_nodes')
        if type(x) is str:
            for c in x:
                tick('independent_encoding_characters')
                p.require(32<=ord(c)<=126 and c not in ('"','\\'), 'safe ASCII goal')
            return '"'+x+'"'
        p.require(type(x) is list, 'actual goal strings/lists only')
        return '['+', '.join(encode_goal(v) for v in x)+']'

    calls=[]; active={}; deliveries=[]
    try:
        p.require(p.CAPS==original.EXPECTED_CAPS and sys.version_info[:3]==(3,15,0)
                  and sys.gettrace() is None, 'fixed caps/runtime/trace boundary')
        source=HERE/'output-489/inputs/proof.jsonl'
        request=HERE/'output-489/inputs/request.json'
        raw, req_raw=source.read_bytes(),request.read_bytes()
        tick('independent_input_bytes',len(raw)+len(req_raw))
        req=decode(req_raw)
        lines=raw.splitlines(keepends=True)
        values=[decode(line) for line in lines]
        header,*rows=values
        p.require(len(rows)==212 and len(lines)==213, 'fixed complete record count')
        expected_string=encode_goal(req['goal'])
        expected_tree=req['goal']  # This fixed endpoint is a leaf.
        p.require(type(expected_tree) is str and expected_tree=='false', 'actual endpoint domain')
        paths=[HERE/'preflight_job7_transport.py',Path(p.__file__),HERE.parent/'parity-four-rule/checker.py']
        bodies={};report['source_snapshots']={}
        for path in paths:
            body=path.read_bytes();tick('source_snapshot_bytes',len(body))
            name='literal-checker.py' if path.name=='checker.py' else path.name
            p.require(body==(HERE/'output-510'/name).read_bytes(), 'full prior source snapshot binding')
            (OUT/name).write_bytes(body);bodies[path]=body
            report['source_snapshots'][name]=dict(bytes=len(body),sha256=hashlib.sha256(body).hexdigest())
        manifest=json.loads((HERE/'output-502/manifest.json').read_bytes())
        p.require(hashlib.sha256(bodies[paths[0]]).hexdigest()==manifest['script_sha256'], 'original manifest binding')
        cf=str(paths[2]);jf=json.dumps.__code__.co_filename
        r=original.Run(); original.R=r; r.stage='default JSON source audit only'
        charges=Counter(); roundtrip_input=None

        def observe(frame,event,arg):
            nonlocal roundtrip_input
            tick('trace_events')
            before=r.visits;original.observe_source(frame,event,arg);delta=r.visits-before
            filename,name=frame.f_code.co_filename,frame.f_code.co_name
            parent=frame.f_back
            if filename==cf and name=='check_bytes' and event=='call':
                p.require(frame.f_locals['raw']==raw and equal(frame.f_locals['expected'],req['goal'])
                          and frame.f_locals['byte_limit']==p.CAPS['input_bytes'], 'actual immutable checker caller binding')
                roundtrip_input=frame.f_locals['expected']
            selected=filename==jf and name in ('dumps','loads') and parent is not None and parent.f_code.co_filename==cf
            if selected:
                charges[name+'_'+event]+=delta
                if event=='exception': raise AssertionError('selected default JSON exception')
                if event=='call':
                    local=frame.f_locals
                    if name=='dumps':
                        p.require(len(calls)==0 and parent.f_code.co_name=='check_bytes' and parent.f_lineno==53,
                                  'only actual default roundtrip serializer')
                        p.require(equal(local['obj'],req['goal']), 'full roundtrip dump argument')
                        defaults={k:local[k] for k in ('skipkeys','ensure_ascii','check_circular','allow_nan','cls','indent','separators','default','sort_keys','kw')}
                        p.require(equal(defaults,dict(skipkeys=False,ensure_ascii=True,check_circular=True,allow_nan=True,
                                  cls=None,indent=None,separators=None,default=None,sort_keys=False,kw={})), 'all default encoder arguments')
                        entry=dict(index=0,function=name,caller='check_bytes',line=53,input=local['obj'],defaults=defaults)
                    else:
                        j=len(calls)-1
                        wanted=expected_string if j==0 else lines[j-1]
                        p.require(0<=j<=213 and equal(local['s'],wanted), 'complete default decoder byte/string input in order')
                        caller,line=('check_bytes',53) if j==0 else ('_check_stream',65 if j==1 else 78)
                        p.require(parent.f_code.co_name==caller and parent.f_lineno==line, 'exact decoder caller binding')
                        defaults={k:local[k] for k in ('cls','object_hook','parse_float','parse_int','parse_constant','object_pairs_hook','kw')}
                        p.require(all(v is None for k,v in defaults.items() if k!='kw') and defaults['kw']=={}, 'all default decoder arguments')
                        entry=dict(index=len(calls),function=name,caller=caller,line=line,
                                   input_kind=type(wanted).__name__,input=wanted.decode('ascii') if type(wanted) is bytes else wanted,
                                   defaults=defaults)
                    calls.append(entry);active[id(frame)]=entry['index']
                elif event=='return':
                    i=active.pop(id(frame));entry=calls[i]
                    wanted=expected_string if i==0 else req['goal'] if i==1 else values[i-2]
                    p.require(equal(arg,wanted), 'complete independent default JSON result')
                    entry.update(output=arg,returned=True)
            if filename==cf and name=='tree' and event=='call' and parent is not None and parent.f_code.co_name=='check_bytes':
                p.require(equal(frame.f_locals['x'],req['goal']), 'decoded roundtrip delivered to tree')
                deliveries.append('tree')
            if filename==cf and name=='_check_stream' and event=='call':
                p.require(frame.f_locals['expected']==expected_tree, 'normalized roundtrip delivered to stream')
                deliveries.append('_check_stream')
            return observe

        sys.settrace(observe)
        try:
            actual_req,actual_raw,actual_rows,checked=p.request(source,request)
            bounds=p.input_bounds(actual_req,actual_raw,actual_rows,request)
        finally: sys.settrace(None)
        p.require(len(calls)==215 and not active and all(z['returned'] for z in calls), 'all one dump and 214 decode returns')
        p.require(deliveries==['tree','_check_stream'] and equal(roundtrip_input,req['goal']), 'complete roundtrip delivery')
        p.require(equal(actual_req,req) and equal(actual_rows,rows) and actual_raw==raw, 'complete independent input correspondence')
        old=json.loads((HERE/'output-502/preflight.json').read_bytes())
        p.require(equal(dict(r.source_observer),old['source_observer']) and r.visits==167_322, 'original full observer totals')
        p.require(all(v==0 for v in charges.values()), 'zero direct selected JSON function observer charges')
        for path,body in bodies.items(): p.require(path.read_bytes()==body, 'sources unchanged after check')
        p.require(source.read_bytes()==raw and request.read_bytes()==req_raw, 'raw inputs unchanged after check')
        decoder_chars=sum(len(z['input']) for z in calls if z['function']=='loads')
        report.update(status='NARROW_DEFAULT_JSON_INTERFACES_RECEIVED',caps=p.CAPS,runtime=sys.version,
            calls=calls,default_dump_calls=1,default_load_calls=214,roundtrip_goal=req['goal'],roundtrip_string=expected_string,
            roundtrip_output_ascii_bytes=len(expected_string),decoder_input_ascii_bytes=decoder_chars,
            roundtrip_deliveries=deliveries,original_selected_event_charges=dict(charges),
            original_source_visits=r.visits,original_source_observer=dict(r.source_observer),literal_check=checked,input_bounds=bounds,
            partial_augmented_source_items=168_943,partial_augmented_original_three_run_items=75_868_982,
            logical_volumes_added_to_item_subtotal=False,
            remaining='Default finite JSON arguments/results received only; actual C encoder/decoder, allocation, comparisons, hashing, I/O and bit/index costs remain UNKNOWN. Other source container/equality work, full independent transport/schema/framing/live peaks and complete historical failed/supplement work remain unresolved.')
    except Exception as err:
        sys.settrace(None)
        report.update(status='FAILED',failures=[dict(type=type(err).__name__,message=str(err),traceback=traceback.format_exc())],
                      partial_calls=calls,partial_deliveries=deliveries)
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
    p.require(total<=RESERVE and time.monotonic()-start<=SECONDS, 'complete evidence/time reserve')
    path=OUT/'default-json.json'
    with path.open('xb') as stream: stream.write(data)
    print(json.dumps(dict(status=report['status'],actual_units=units,required_units=LIMIT,
        actual_evidence_bytes=total,required_reserve_bytes=RESERVE,
        dump_calls=report.get('default_dump_calls','UNKNOWN'),load_calls=report.get('default_load_calls','UNKNOWN'),
        failures=report['failures'],path=str(path))))


if __name__=='__main__': main()
