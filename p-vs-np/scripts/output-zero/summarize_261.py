"""Final, honest resource report for the stopped coordinate attempt."""
import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'scripts/output-zero/output/coordinate-261'

def main():
    evidence=json.loads((OUT/'inspection.json').read_text())
    names=('heartbeat-selftest','monitor','inspection-monitor','inspection-retry-monitor')
    monitors={name:json.loads((OUT/(name+'.json')).read_text()) for name in names}
    base=(OUT/'heartbeat-selftest.log').stat().st_birthtime
    intervals={name:dict(start=(OUT/(name+'.log')).stat().st_birthtime-base,
        duration=monitors[name]['elapsed_seconds']) for name in names}
    wall=max(a['start']+a['duration'] for a in intervals.values())
    active=sum(a['duration'] for a in intervals.values())
    assert wall>600 and active<600
    assert monitors['monitor']['stopped'] and monitors['monitor']['stop_reason']=='time'
    assert monitors['inspection-monitor']['exit_code']==1
    assert monitors['inspection-retry-monitor']['exit_code']==0
    assert evidence['complete'] and not evidence['target_complete'] and not evidence['failures']
    assert not evidence['expanded_new_gzip']['coordinate-0.native.jsonl.gz']['complete_gzip']
    paths=[
        'scripts/output-zero/coordinate_261.py','scripts/output-zero/watch_261.py',
        'scripts/output-zero/inspect_261.py','scripts/output-zero/watch_inspect_261.py',
        'scripts/output-zero/summarize_261.py',
        'drafts/2026-10-16-interned-coordinate-work.md',
        'drafts/literature/2026-10-16-compiled-coordinate-serializer.md',
        'lemmas/L068-general-actual-tree-output-zero-receiver.md',
        'history/261-2026-10-16-interned-coordinate-output-stop.md',
        'ATTEMPTS/025-interned-coordinate-python-writer-time-stop.md','PROGRESS.md']
    artifacts=sum(p.stat().st_size for p in OUT.iterdir() if p.is_file())
    extra=sum((ROOT/p).stat().st_size for p in paths)
    limits=dict(rss=dict(actual=max(monitors[n]['peak_process_tree_rss_bytes'] for n in names),required_max=2**31,stop_threshold=3*2**29),
        wall_seconds=dict(actual=wall,required_max=600,passed=False),
        active_monitor_seconds=dict(actual=active,required_max=600,qualification='Does not include inter-run gaps; insufficient for shared wall-time compliance.'),
        artifacts=dict(actual=artifacts+extra,required_max=16*2**30,qualification='Conservative: includes full modified documentation and all new implementation/report files.'),
        expanded_output=dict(actual=evidence['expanded_actual'],required_max=128*2**30))
    result=dict(complete=True,target_complete=False,outcome='NEGATIVE',
        resource_contract_met=False,actual_required=limits,intervals=intervals,
        failures=['Production writer exhausted its 540-second reserved window before completing the native stream.',
                  'Inspection launcher omitted inter-run gaps: full experimental interval exceeds 600 seconds.'],
        preserved_inspector_failure='inspection-before-json-path-adapter.py and inspection-monitor.log',
        internal_checkpoint_rows=1149478,retained_local_rows=155588,
        complete_proposed_bytes=evidence['counts_both_complete_proposed_formats'],
        corrected_ledger='inspection.json /corrected_original_input_ledger',
        source_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths[:5]},
        wall_qualification='Filesystem log birth timestamps plus monitor monotonic durations; interval estimate, not continuous hard-cap enforcement.',
        limitation='No complete coordinate archive pair/replay; internal primitive checks and byte counts are partial implementation evidence only.')
    path=OUT/'verification.json'; assert not path.exists()
    for _ in range(10):
        raw=json.dumps(result,indent=2)+'\n'; total=artifacts+extra+len(raw.encode())
        if limits['artifacts']['actual']==total: break
        limits['artifacts']['actual']=total
    else: raise AssertionError('artifact fixed point')
    path.write_text(raw)
    assert sum(p.stat().st_size for p in OUT.iterdir() if p.is_file())+extra==limits['artifacts']['actual']
    for key,bound in limits.items():
        print(key,bound['actual'],'/',bound['required_max'],'FAIL' if bound['actual']>=bound['required_max'] else 'PASS')
    print('RESULT NEGATIVE; complete target False; resource contract False; failures',len(result['failures']))
    print('evidence',path.relative_to(ROOT))

if __name__=='__main__': main()
