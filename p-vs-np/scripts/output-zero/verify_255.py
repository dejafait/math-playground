"""Inspect complete bounded loader evidence; does not rerun missing downstream work."""
import gzip
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'scripts/output-zero/output/interned-255'
OLD=ROOT/'scripts/output-zero/output/nonempty-253'

def read(name): return json.loads((OUT/name).read_text())

def main():
    c=read('certificate.json'); m=read('monitor.json'); t=read('heartbeat-selftest.json')
    old=json.loads((OLD/'certificate.json').read_text())
    supplemental=read('supplement.json'); sm=read('supplement-monitor.json')
    assert supplemental['complete'] and len(supplemental['rejections'])==6 and supplemental['failures']==[]
    assert sm['complete'] and sm['exit_code']==0 and sm['failures']==[] and not sm['stopped']
    assert c['complete'] and c['failures']==[] and c['stage']=='complete'
    assert m['complete'] and m['exit_code']==0 and m['failures']==[] and not m['stopped']
    assert t['complete'] and t['stopped'] and t['stop_reason']=='rss' and t['exit_code']!=0
    assert 'PASS child-process creation blocked' in (OUT/'heartbeat-selftest.log').read_text()
    assert m['samples']>0 and m['worker_peak_rss_bytes']>=c['worker_peak_rss_bytes']
    assert m['peak_process_tree_rss_bytes']==m['parent_peak_rss_bytes']+m['worker_peak_rss_bytes']
    assert c['small']['complete'] and len(c['small']['rejections'])==17
    assert c['small']['tree_copier_all_fields'] and c['small']['offset']==1
    assert c['small']['parser_max_accepted_depth']==4096 and c['small']['parser_rejected_depth']==4097
    assert c['all_six_held_together'] and c['checkpoint']['full_pool_row_equality']
    assert len(c['packages'])==len(c['checkpoint']['all_record_archive_comparisons'])==6
    totals={mode:dict(lines=0,bytes=0,formula_nodes=0,substitution_nodes=0) for mode in ('native','not-or')}
    for i,(actual,saved,count) in enumerate(zip(c['packages'],old['certified_locals'],c['checkpoint']['all_record_archive_comparisons'])):
        assert actual['vertex']==saved['v']==i
        assert actual['checked']==saved['checked']
        assert count==actual['retained_rows']==actual['checked']['measurements']['native']['lines']
        for mode in totals:
            for key in totals[mode]: totals[mode][key]+=actual['checked']['measurements'][mode][key]
    # Count ALL new gzip content, including checkpoint payload, conservatively.
    expanded=0
    for path in OUT.glob('*.gz'):
        with gzip.open(path,'rb') as stream:
            while True:
                block=stream.read(2**20)
                if not block: break
                expanded+=len(block)
    storage=sum(p.stat().st_size for p in OUT.iterdir() if p.is_file())
    comparisons=dict(rss=dict(actual=max(m['peak_process_tree_rss_bytes'],sm['peak_process_tree_rss_bytes']),required_max=2**31,
        watchdog_stop_threshold=3*2**29),seconds=dict(actual=m['elapsed_seconds']+sm['elapsed_seconds'],required_max=600),
        new_artifacts=dict(actual=storage,required_max=16*2**30),
        expanded_new_gzip_payload=dict(actual=expanded,required_max=128*2**30))
    for values in comparisons.values(): assert values['actual']<values['required_max']
    assert m['peak_process_tree_rss_bytes']<m['stop_threshold_bytes']
    result=dict(complete=True,target_complete=True,failures=[],actual_required=comparisons,
        all_record_totals=totals,malformed_rejections=23,
        checkpoint_all_record_counts=c['checkpoint']['all_record_archive_comparisons'],
        initial_ps_failure_preserved=read('watchdog-selftest.json')['failures'],
        resource_qualification='Peak RSS observations and fail-closed watchdog; not an all-input or continuous hard-cap theorem.',
        mathematical_scope='Known-operation reproduction: standalone receiving boundary only; no coordinate or joined proof, certificate existence or SAT conclusion.')
    path=OUT/'verification-final.json'; assert not path.exists()
    path.write_text(json.dumps(result,indent=2)+'\n')
    print('RESULT complete six-package loader; rows/format',totals['native']['lines'],'rejections',23)
    for k,v in comparisons.items(): print(k,v['actual'],'/',v['required_max'],'PASS')
    print('evidence',path.relative_to(ROOT))
if __name__=='__main__': main()
