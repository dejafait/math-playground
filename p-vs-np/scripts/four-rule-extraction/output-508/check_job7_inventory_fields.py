"""Complete unused inventory-field/count checks omitted from the primary table.

Same step 502, no primary rerun and no coordinate or word calculation.
"""
from pathlib import Path
import json
import time
import parameterized_input as p
from preflight_job7_transport import Run

HERE=Path(__file__).resolve().parent
OUT=HERE/'output-502'


def main():
    path=OUT/'inventory-fields.json';p.require(not path.exists(),'preserve evidence')
    start=time.monotonic()
    receipt=json.loads((OUT/'accounting-check.json').read_bytes(),object_pairs_hook=p.no_duplicates)
    r=Run();r.stage='supplemental complete inventory fields'
    prior_visits=receipt['cumulative_reported_item_visits'];r.visits=prior_visits
    cert=p.load(HERE/'output-493/restricted-boolean.json');r.walk(cert)
    inv=p.load(HERE/'output-493/restricted-interior-bound.json');r.walk(inv)
    old=p.load(HERE/'output-491/retained-interior-bound.json');r.walk(old)
    a,b,c=[z['jobs'][7] for z in (cert,inv,old)]
    for z in (cert,inv):
        p.require(type(z['source_record']) is int and z['source_record']==78 and
                  type(z['boolean_event']) is int and z['boolean_event']==2643,'exact inventory source/event fields')
        p.require(r.eq(z['checked_source'],cert['checked_source']) and z['target']==cert['target'],
                  'complete repeated source and target binding')
    for z in (a,b,c):
        p.require(len(z['restrictions'])==2,'exactly both whole operands')
        p.require(r.eq(z['restrictions'],a['restrictions']),'entire whole-operand interface')
        p.require(len(z['selected'])==120,'entire selected list count')
        p.require(r.eq({k:z[k] for k in ('index','vertex','kind','edge_occurrences')},
                      {k:a[k] for k in ('index','vertex','kind','edge_occurrences')}),'every job identity field')
    p.fields(b,'index vertex kind edge_occurrences restrictions selected vertices edges label_entries records')
    for left,right,previous in r.items(zip(a['selected'],b['selected'],c['selected'])):
        p.fields(right,'f_edge g_edge central copies')
        p.require(len(left['copies'])==len(right['copies'])==4,'exactly four copies per selection')
        p.require(r.eq({k:left[k] for k in ('f_edge','g_edge','central')},previous) and
                  r.eq({k:right[k] for k in ('f_edge','g_edge','central')},previous),
                  'complete selected identity/central metadata in both inventories')
    for key in ('vertices','edges','records','label_entries'):
        p.require(type(a[key]) is int and type(b[key]) is int and a[key]==b[key],
                  'type-sensitive measured metrics')
    result=dict(result='PASS',separate_critical_audit=False,
        checks='all repeated job-7 identity/source/target fields, both whole-operand maps, all selected central metadata, exact list lengths and count-field types',
        primary_run_overwritten=False,word_or_coordinate_work=False,
        supplementary_item_visits=r.visits-prior_visits,cumulative_reported_item_visits=r.visits,
        required_item_visits=100_000_000,supplement_seconds=time.monotonic()-start,
        artifact_bytes_including_this_receipt=0,wire_baseline_plus_all_artifacts=0,
        conservative_coordinate_ceiling_after_all_artifacts_and_extra_reserve=0,
        required_evidence_bytes=200_000_000,reserve_bytes=1_000_000)
    programs=[HERE/'preflight_job7_transport.py',HERE/'check_job7_preflight_accounting.py',Path(__file__)]
    programs+=sorted((HERE/'__pycache__').glob('preflight_job7_transport.*.pyc'))
    used=sum(z.stat().st_size for z in OUT.iterdir() if z.is_file())+sum(z.stat().st_size for z in programs)
    while True:
        raw=json.dumps(result,ensure_ascii=True,separators=(',',':')).encode()
        total=used+len(raw)
        if result['artifact_bytes_including_this_receipt']==total:break
        result['artifact_bytes_including_this_receipt']=total
        result['wire_baseline_plus_all_artifacts']=receipt['baseline_wire_bytes']+total
        result['conservative_coordinate_ceiling_after_all_artifacts_and_extra_reserve']=200_000_000-1_000_000-receipt['baseline_wire_bytes']-total
    p.require(total<1_000_000 and r.visits<100_000_000,'same unchanged reserve and cumulative visit ceiling')
    p.require(time.monotonic()-start<900,'supplement timer ceiling')
    with path.open('xb') as stream:stream.write(raw)
    print(json.dumps(dict(result='PASS',cumulative_item_visits=r.visits,required_item_visits=100_000_000,
        artifact_bytes=total,required_evidence_bytes=200_000_000,failures=[],path=str(path))))


if __name__=='__main__':main()
