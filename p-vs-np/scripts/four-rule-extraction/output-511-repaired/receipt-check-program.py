"""Read every step-511 interface record and save a bounded reconciliation."""
import ast
from collections import Counter
import hashlib
import json
from pathlib import Path
import time

import parameterized_input as p

HERE=Path(__file__).resolve().parent
OUT=HERE/'output-511-repaired'


def main():
    dest=OUT/'receipt-check.json'
    p.require(not dest.exists(), 'preserve reconciliation evidence')
    start=time.monotonic(); units=0; budget=Counter(); failures=[]; passed=[]
    data=json.loads((OUT/'default-json.json').read_bytes())
    prior=data['audit_item_event_units']; prior_time=data['cumulative_elapsed_seconds']
    (OUT/'receipt-check-program.py').write_bytes(Path(__file__).read_bytes())

    def tick(kind,n=1):
        nonlocal units
        p.require(prior+units+n<=100_000_000, 'cumulative selected unit cap')
        units+=n;budget[kind]+=n
        if units%4096==0: p.require(prior_time+time.monotonic()-start<=900,'cumulative timer')

    def same(a,b):
        tick('complete_value_comparisons')
        if type(a) is not type(b): return False
        if type(a) is dict:
            return a.keys()==b.keys() and all(same(a[k],b[k]) for k in a)
        if type(a) is list:
            return len(a)==len(b) and all(same(x,y) for x,y in zip(a,b))
        return a==b

    def check(ok,name):
        p.require(ok,name);passed.append(name)

    try:
        check(data['status']=='NARROW_DEFAULT_JSON_INTERFACES_RECEIVED' and not data['failures'],'successful narrow probe')
        source=(HERE/'output-489/inputs/proof.jsonl').read_bytes()
        request=(HERE/'output-489/inputs/request.json').read_bytes()
        tick('literal_input_bytes',len(source)+len(request))
        # The probe has already established its restricted JSON lexical domain.
        # literal_eval supplies a separately implemented parser for these actual
        # strings/unsigned integers/containers, not a general JSON validator.
        lines=source.splitlines(keepends=True)
        req=ast.literal_eval(request.decode('ascii'))
        values=[ast.literal_eval(z.decode('ascii')) for z in lines]
        calls=data['calls']
        check(len(calls)==215 and len(values)==213,'complete interface cardinalities')
        encoded=calls[0]['output']
        check(same(ast.literal_eval(encoded),req['goal']) and len(encoded)==818,'complete roundtrip string interpretation')
        dump_defaults=dict(skipkeys=False,ensure_ascii=True,check_circular=True,allow_nan=True,cls=None,
                           indent=None,separators=None,default=None,sort_keys=False,kw={})
        load_defaults=dict(cls=None,object_hook=None,parse_float=None,parse_int=None,parse_constant=None,object_pairs_hook=None,kw={})
        for i,call in enumerate(calls):
            tick('interface_records')
            check(call['index']==i and call['returned'] is True,'ordered returned interface '+str(i))
            if i==0:
                check(call['function']=='dumps' and call['caller']=='check_bytes' and call['line']==53
                      and same(call['input'],req['goal']) and same(call['defaults'],dump_defaults),'full dump binding')
            else:
                wanted_input=encoded if i==1 else lines[i-2].decode('ascii')
                wanted_output=req['goal'] if i==1 else values[i-2]
                caller,line=('check_bytes',53) if i==1 else ('_check_stream',65 if i==2 else 78)
                tick('complete_decoder_input_characters',len(wanted_input))
                check(call['function']=='loads' and call['caller']==caller and call['line']==line
                      and call['input_kind']==('str' if i==1 else 'bytes') and call['input']==wanted_input
                      and same(call['output'],wanted_output) and same(call['defaults'],load_defaults),
                      'full decoder binding '+str(i-1))
        expected_charges={fn+'_'+event:0 for fn in ('dumps','loads') for event in ('call','line','return')}
        check(same(data['original_selected_event_charges'],expected_charges),'complete selected direct-charge dictionary')
        check(data['decoder_input_ascii_bytes']==101314+818==102132
              and data['roundtrip_output_ascii_bytes']==818,'all input/output byte lengths')
        old=json.loads((HERE/'output-502/preflight.json').read_bytes())
        check(same(data['original_source_observer'],old['source_observer']) and data['original_source_visits']==167322,
              'complete original source observer')
        check(data['roundtrip_deliveries']==['tree','_check_stream'] and same(data['roundtrip_goal'],req['goal']),
              'complete roundtrip deliveries and goal')
        check(data['literal_check']['accepted'] and data['literal_check']['records']==212
              and data['literal_check']['sha256']==hashlib.sha256(source).hexdigest()==req['source_sha256'],
              'literal immutable source binding')
        for name,path in [('preflight_job7_transport.py',HERE/'preflight_job7_transport.py'),
                          ('parameterized_input.py',Path(p.__file__)),('literal-checker.py',HERE.parent/'parity-four-rule/checker.py')]:
            body=path.read_bytes();tick('source_snapshot_bytes',len(body))
            check(body==(OUT/name).read_bytes()==(HERE/'output-510'/name).read_bytes()
                  and len(body)==data['source_snapshots'][name]['bytes']
                  and hashlib.sha256(body).hexdigest()==data['source_snapshots'][name]['sha256'],'full source binding '+name)
        check(same(data['caps'],p.CAPS) and data['partial_augmented_source_items']==168943
              and data['partial_augmented_original_three_run_items']==75868982
              and data['logical_volumes_added_to_item_subtotal'] is False,'unchanged caps and partial item subtotals')
        check(sum(data['audit_budget'].values())==prior and data['previous_attempt']['selected_units']==234432
              and data['previous_attempt']['charged_evidence_bytes']==28851,'full probe selected-unit and failed-prefix totals')
    except Exception as err:
        failures.append(dict(type=type(err).__name__,message=str(err)))
    result=dict(status='PASS' if not failures else 'FAILED',failures=failures,passed_checks=passed,
        reconciliation_selected_units=units,reconciliation_budget=dict(budget),
        cumulative_selected_units=prior+units,required_selected_units=100_000_000,
        cumulative_seconds=prior_time+time.monotonic()-start,required_seconds=900,
        charged_evidence_bytes=0,required_reserve_bytes=1_000_000,required_evidence_bytes=p.CAPS['certificate_bytes'],
        total_work_bound=False,qualification='Both probes and this selected reconciliation included. Python/C parser/encoder, hashing, I/O, allocation and bit/index work, tool reads and total interpreter costs remain unbounded here.')
    fixed=data['program_snapshots_and_receipt_bytes']+2*Path(__file__).stat().st_size
    while True:
        raw=json.dumps(result,separators=(',',':'),ensure_ascii=True).encode()
        total=fixed+len(raw)
        if result['charged_evidence_bytes']==total: break
        result['charged_evidence_bytes']=total
    p.require(total<=1_000_000 and result['cumulative_seconds']<=900,'complete selected reserve/time')
    with dest.open('xb') as stream: stream.write(raw)
    print(json.dumps({k:v for k,v in result.items() if k not in ('passed_checks','reconciliation_budget','qualification')},separators=(',',':')))
    print(str(dest))


if __name__=='__main__': main()
