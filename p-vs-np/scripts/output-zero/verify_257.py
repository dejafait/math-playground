"""Inspect full completed copier certificates and actual/required bounds."""
import gzip
import json
from pathlib import Path
import copier_257 as c

def read(name): return json.loads((c.OUT/name).read_text())

def main():
    cert=read('certificate.json'); monitor=read('monitor.json'); test=read('heartbeat-selftest.json')
    strict=read('strict-reload.json'); sm=read('strict-monitor.json')
    assert cert['complete'] and cert['stage']=='complete' and not cert['failures']
    assert strict['complete'] and strict['stage']=='complete' and not strict['failures']
    assert strict['strict_types'] and len(strict['rejections'])==8
    assert all(x['error'].startswith('AssertionError:') for x in strict['rejections'])
    assert c.exact(cert['before_checkpoint'],cert['after_checkpoint'])
    assert c.exact(strict['comparison'],cert['after_checkpoint'])
    small=cert['small']
    assert small['complete'] and small['all_tree_copier_fields'] and small['conflicting_ids']
    assert len(small['cases'])==8 and len(small['rejections'])==13
    assert [x['start'] for x in small['cases']]==list(range(1,41,5))
    assert small['complete_two_format_rows']==41 and small['unused_native_depth']==120
    assert small['reused']['complete'] and len(small['reused']['rejections'])==17
    assert small['reused']['parser_max_accepted_depth']==4096 and small['reused']['parser_rejected_depth']==4097
    assert small['step253_rejections']['complete'] and len(small['step253_rejections']['rejections'])==6 and not small['step253_rejections']['failures']
    assert cert['checkpoint']['full_nodes_rows_provenance_equality']
    assert cert['checkpoint']['primitive_replay_rows']==strict['complete_replayed_rows']==155589
    assert strict['complete_locations']==cert['locations']==155588
    assert test['complete'] and test['stopped'] and test['stop_reason']=='rss' and test['exit_code']!=0 and not test['failures']
    assert 'PASS child-process creation blocked' in (c.OUT/'heartbeat-selftest.log').read_text()
    for m in (monitor,sm):
        assert m['complete'] and m['exit_code']==0 and not m['stopped'] and not m['failures'] and m['samples']>0
        assert m['peak_process_tree_rss_bytes']==m['parent_peak_rss_bytes']+m['worker_peak_rss_bytes']
        assert m['peak_process_tree_rss_bytes']<m['stop_threshold_bytes']==3*2**29
    assert monitor['worker_peak_rss_bytes']>=cert['worker_peak_rss_bytes']
    comparison=cert['after_checkpoint']; start=1
    assert comparison['all_fields'] and comparison['counts']==[37000,16288,28654,16288,28654,28704]
    assert comparison['joined_rows_per_format']==155589 and len(cert['segments'])==6
    totals={m:dict(lines=0,bytes=0,formula_nodes=0,substitution_nodes=0) for m in c.h.MODES}
    deltas=dict.fromkeys(c.h.MODES,0)
    for i,(seg,n,report) in enumerate(zip(cert['segments'],comparison['counts'],comparison['packages'])):
        assert seg['start']==start and seg['count']==n and seg['root']==start+n-1
        assert seg['paths']==[str((c.h.SOURCE/f'local-{i}.{m}.jsonl.gz').relative_to(c.ROOT)) for m in c.h.MODES]
        assert c.exact(seg['checked'],report['checked']) and seg['substitutions']==[]
        for mode in c.h.MODES:
            for key in totals[mode]: totals[mode][key]+=report['checked']['measurements'][mode][key]
            delta=report['reference_digit_delta'][mode]; assert type(delta) is int and delta>=0
            assert report['relocated_segment_bytes'][mode]==report['checked']['measurements'][mode]['bytes']+delta
            deltas[mode]+=delta
        start+=n
    assert start==155589 and totals['native']['bytes']==256056258 and totals['not-or']['bytes']==376605480
    expanded=0
    for path in c.OUT.glob('*.gz'):
        with gzip.open(path,'rb') as stream:
            while True:
                block=stream.read(2**20)
                if not block: break
                expanded+=len(block)
    # Conservatively include all three virtual full joined-stream comparisons,
    # although no production joined proof stream is written to disk.
    accounted_expanded=expanded+3*sum(comparison['joined_stream_bytes'].values())
    storage=sum(p.stat().st_size for p in c.OUT.iterdir() if p.is_file())
    bounds=dict(rss=dict(actual=max(monitor['peak_process_tree_rss_bytes'],sm['peak_process_tree_rss_bytes']),required_max=2**31,watchdog_stop_threshold=3*2**29),
        seconds=dict(actual=monitor['elapsed_seconds']+sm['elapsed_seconds']+test['elapsed_seconds'],required_max=600),
        new_artifacts=dict(actual=storage,required_max=16*2**30),
        expanded_output=dict(actual=accounted_expanded,required_max=128*2**30))
    assert all(v['actual']<v['required_max'] for v in bounds.values())
    result=dict(complete=True,target_complete=True,failures=[],actual_required=bounds,
        source_all_record_totals=totals,reference_digit_delta=deltas,
        joined_rows_per_format=155589,source_occurrences=155588,valid_prefix_rows=1,
        joined_stream_bytes=comparison['joined_stream_bytes'],expanded_new_gzip_payload=expanded,
        numeric_type_checkpoint_rejections=8,total_rejection_tests=44,
        checkpoint_strict_types=True,complete_source_archive_comparison_passes=3,
        source_version_before_repair='copier-before-strict-metadata.py',
        qualification='Known-operation implementation reproduction only. Measured process lifetime maxima/heartbeat watchdog, not a continuous hard-cap theorem. Trusted internal pickle only; parser limit 4096; no Closure/coordinates/joined receiver or SAT consequence.')
    path=c.OUT/'verification-complete.json'; assert not path.exists()
    # Include this certificate itself in the final storage count. Preserve the
    # earlier inspection, whose storage observation preceded its own write.
    for _ in range(10):
        raw=json.dumps(result,indent=2)+'\n'
        total=storage+len(raw.encode('utf-8'))
        if bounds['new_artifacts']['actual']==total: break
        bounds['new_artifacts']['actual']=total
    else: raise AssertionError('storage fixed point did not stabilize')
    assert bounds['new_artifacts']['actual']<bounds['new_artifacts']['required_max']
    path.write_text(raw)
    assert sum(p.stat().st_size for p in c.OUT.iterdir() if p.is_file())==bounds['new_artifacts']['actual']
    print('RESULT complete cross-pool boundary; rows/format',155589,'retained source rows',155588,'rejection tests',44)
    for k,v in bounds.items(): print(k,v['actual'],'/',v['required_max'],'PASS')
    print('reference digit deltas',deltas,'joined expanded bytes',comparison['joined_stream_bytes'])
    print('evidence',path.relative_to(c.ROOT))

if __name__=='__main__': main()
