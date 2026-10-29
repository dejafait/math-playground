"""Small arithmetic/omitted-input-graph ledger check for the same step 502.

This is not the separately scheduled critical audit and does not regenerate
the large transport or claim coefficient equalities. Preserve the first run.
"""
from pathlib import Path
import hashlib
import json
import time
import parameterized_input as p

HERE=Path(__file__).resolve().parent
OUT=HERE/'output-502'


def main():
    start=time.monotonic(); visits=0
    def walk(value):
        nonlocal visits
        visits+=1
        if type(value) is list:
            for v in value: walk(v)
        elif type(value) is dict:
            for k,v in value.items(): walk(k); walk(v)
    def encoded(value):
        # Only the small selected input graphs/receipts use this independent
        # serializer. No second large transport or binding object is formed.
        walk(value)
        return len(json.dumps(value,ensure_ascii=True,separators=(',',':')).encode())
    # Administrative receipts contain measured floating-point seconds and
    # large exact integer totals. They are not the strict transport schema.
    def metadata(path):
        return json.loads(p.read_bytes(path,'certificate_bytes'),
            object_pairs_hook=p.no_duplicates,parse_constant=p.reject_number)
    report=metadata(OUT/'preflight.json'); manifest=metadata(OUT/'manifest.json')
    walk(report);walk(manifest)
    p.require(report['status']=='MANDATORY_TRANSPORT_FITS','completed measured preflight')
    p.require(hashlib.sha256((HERE/'preflight_job7_transport.py').read_bytes()).hexdigest()==
              manifest['script_sha256'],'run source unchanged after measurement')
    dims=report['dimensions']; frames=report['framing']
    baseline=32+128+frames['B_bind']+frames['B_trans']
    p.require(baseline==report['zero_rank_size_baseline']['wire_bytes'],'all framing and empty coordinate arrays')
    full=baseline;bits=0;ops=0
    for d,row in zip(dims,report['full_rank_size_endpoint']['rows']):
        n,q=d['N'],d['q'];r=n
        a=(r*n+7)//8;b=(r+7)//8;c=(q*r*r+7)//8
        p.require((row['B_bytes'],row['c_bytes'],row['T_bytes'])==(a,b,c),'separate packing ceilings')
        full+=a+b+c;bits+=r*n+r+q*r*r
        ops+=16*(q+1)*(r+1)**2*(n+d['m0']+d['mL']+1)
    p.require((full,bits,ops)==tuple(report['full_rank_size_endpoint'][k] for k in
        ('wire_bytes','logical_coordinate_bits','algebraic_bit_operation_bound')),'full endpoint independent arithmetic')
    extra=[]
    # Four small source/operand graphs are embedded in the counted binding /
    # transport sections, but omitted from the first report's standalone table.
    event=p.load(HERE/'output-489/trace/event-02642.json');walk(event)
    prior=p.load(HERE/'output-491/retained-interior-bound.json');walk(prior)
    for name,g in [('source_translation',event['graph']),('normalized',prior['normalized'])]+[
            ('whole_original_'+str(i),m['original']) for i,m in enumerate(prior['jobs'][7]['restrictions'])]:
        walk(g)
        extra.append(dict(name=name,vertices=g['vertices'],edges=len(g['edges']),
            records=g['vertices']+len(g['edges']),label_entries=sum(len(e[2]) for e in g['edges']),
            graph_encoded_bytes=encoded(g),root_encoding_bytes=encoded([g['source'],g['sink']]),
            note='already included in exact section totals; this ledger adds no transport copy'))
    totals={k:sum(g[k] for g in report['graphs']) for k in ('vertices','edges','records','label_entries','graph_encoded_bytes')}
    p.require(max(g['records'] for g in report['graphs']+extra)<=p.CAPS['records'] and
              max(g['label_entries'] for g in report['graphs']+extra)<=p.CAPS['label_entries'],'all measured per graph caps')
    output=OUT/'accounting-check.json';p.require(not output.exists(),'preserve old check')
    used=sum(f.stat().st_size for f in OUT.iterdir() if f.is_file())
    code_paths=[HERE/'preflight_job7_transport.py',Path(__file__)]
    code_paths+=sorted((HERE/'__pycache__').glob('preflight_job7_transport.*.pyc'))
    code_bytes=sum(f.stat().st_size for f in code_paths)
    receipt=dict(result='arithmetic and supplemental input-graph ledger PASS',separate_critical_audit=False,
        input_graphs=extra,explicit_output_graph_totals=totals,
        maxima=dict(records=max(g['records'] for g in report['graphs']+extra),
                    label_entries=max(g['label_entries'] for g in report['graphs']+extra)),
        baseline_wire_bytes=baseline,full_rank_wire_bytes=full,required_evidence_bytes=p.CAPS['certificate_bytes'],
        output_bytes_before_this_receipt=used,retained_program_and_bytecode_bytes=code_bytes,
        code_paths=[str(f.relative_to(HERE)) for f in code_paths],reserve_bytes=1_000_000,
        conservative_coordinate_byte_ceiling_with_reserve=p.CAPS['certificate_bytes']-baseline-used-code_bytes-1_000_000,
        receipt_write_peak='existing outputs + retained programs + this newly sized receipt; no overwritten files',
        supplementary_item_visits=visits,cumulative_reported_item_visits=report['item_visits']+visits,
        required_item_visits=100_000_000,supplement_seconds=time.monotonic()-start,
        limitations='No independent regeneration of the full B_trans, no coordinate construction, no total interpreter-memory bound. First report preserved.')
    receipt['preserved_helper_failure']='helper-first-read.failure.json: strict mathematical-input parser rejected an administrative timing float before any graph check; corrected only metadata loading, no main preflight rerun.'
    raw=json.dumps(receipt,ensure_ascii=True,separators=(',',':')).encode()
    p.require(len(raw)<1_000_000 and used+code_bytes+len(raw)<1_000_000,'complete run artifacts fit receipt reserve')
    p.require(report['item_visits']+visits<100_000_000,'cumulative administrative visits')
    with output.open('xb') as stream:stream.write(raw)
    print(json.dumps(dict(result='PASS',baseline_wire_bytes=baseline,full_rank_wire_bytes=full,
        actual_run_artifact_bytes=used+code_bytes+len(raw),required_evidence_bytes=200_000_000,
        cumulative_item_visits=report['item_visits']+visits,required_item_visits=100_000_000,
        failures=[],path=str(output))))


if __name__=='__main__':main()
