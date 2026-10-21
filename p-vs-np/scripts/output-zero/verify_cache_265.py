"""Verify saved partial evidence only; never loads the production checkpoint."""
import gzip
import hashlib
import json
import resource
import sys
import time
import zlib
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'scripts/output-zero/output/cache-265'


def main():
    summary=json.loads((OUT/'monitor-summary.json').read_text())
    cert=json.loads((OUT/'certificate.json').read_text())
    assert time.monotonic()<summary['deadline_monotonic']
    assert cert['status']=='STOPPED' and not cert['target_complete']
    assert cert['failures']==['AssertionError: conservative live-workspace admission']
    assert cert['restore']['all_primitive_rows']==1149478
    assert cert['restore']['external_source_occurrences']==155588
    assert cert['restore']['generated_tail_rows']==993889
    assert cert['restore']['exact_endpoint']
    assert cert['restore']['maxima']==[[596317,2370196],[596317,3534568]]
    assert cert['valid_prefix']['records']==64 and cert['valid_prefix']['complete_primitive_replay']
    assert len(cert['small']['rejections'])==20 and len(cert['record_rejections'])==16
    assert all(cert['small'][k] for k in ('depth4096','eviction_recomputation','mode_separation','double_negations'))
    assert len(summary['tests'])==6 and all(not x['failures'] for x in summary['tests'])
    assert [x['stop_reason'] for x in summary['tests']]==['rss','heartbeat','storage','rss','expired-start','expired-start']
    assert all(not x['launched'] for x in summary['tests'][-2:])
    assert summary['terminal_only_unit']['injected'] and summary['terminal_only_unit']['rejected']
    m=summary['main_repaired']
    assert m['complete'] and not m['stopped'] and not m['failures'] and m['exit_code']==1
    assert m['terminal_peak_rechecked'] and m['samples']>0
    assert m['peak_process_tree_rss_bytes']==m['worker_peak_rss_bytes']+m['parent_peak_rss_bytes']<1610612736
    comparisons=cert['comparisons']
    assert [(x['format'],x['window']) for x in comparisons]==[('native','begin'),('native','middle'),('native','end')]
    reinflated=0; verified=[]
    for item in comparisons:
        payloads=[]
        for suffix in ('baseline','adapted'):
            path=OUT/(item['window']+'.native.'+suffix+'.jsonl.gz')
            blob=path.read_bytes(); d=zlib.decompressobj(31); data=d.decompress(blob)+d.flush()
            assert d.eof and not d.unused_data and not d.unconsumed_tail
            assert len(data)==item['bytes']
            assert hashlib.sha256(data).hexdigest()==item['sha256']
            payloads.append(data); reinflated+=len(data)
        assert payloads[0]==payloads[1]
        records=[json.loads(raw) for raw in payloads[0].splitlines()]
        assert len(records)==1+len(item['indices']) and records[0]['format']=='native'
        assert all(set(r)==({'f','rule','refs'} if r['rule']=='mp' else {'f','rule','subs'}) for r in records[1:])
        verified.append(dict(window=item['window'],complete_reinflated_byte_equality=True,bytes=item['bytes'],
                             records=len(records)-1,global_indices=item['indices']))
    n=cert['restore']['maxima'][0][1]
    minimum_workspace=64*n+1024*2+33554432+512*32768+64*2**20
    diagnostic=cert['worker_peak_rss_bytes']+minimum_workspace
    # This diagnostic uses the recorded terminal watermark; the actual stop
    # is established by the saved failed runtime assertion, not a reconstructed
    # claim to know the missing admission depth or instantaneous current RSS.
    assert diagnostic>1610612736
    verifier_peak=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*(1 if sys.platform=='darwin' else 1024)
    parent_max=max(m['parent_peak_rss_bytes'],*(x['parent_peak_rss_bytes'] for x in summary['tests']),
        json.loads((OUT/'rss-selftest.json').read_text())['parent_peak_rss_bytes'])
    combined=m['worker_peak_rss_bytes']+parent_max+verifier_peak
    assert combined<1610612736
    # The first failed worker's entire 1 MiB small-data reserve and this
    # independent reinflation are additional to the final worker's counters.
    first=json.loads((OUT/'initial-worker-test-certificate.json').read_text())
    expanded=cert['expanded_actual']+first['expanded_actual']+summary['output_selftest_expanded_bytes']+reinflated
    differential=cert['differential_expanded']+first['differential_expanded']+reinflated
    assert expanded<=137438953472 and differential<=268435456 and cert['benchmark_expanded']<=1073741824
    storage=sum(x.stat().st_size for x in OUT.iterdir() if x.is_file())
    assert storage+2**20<17179869184
    result=dict(complete=True,target_complete=False,failures=[],verdict='PARK: workspace admission failed',
        verified_partial_windows=verified,production_pair=False,maximum_rows_rendered=False,
        image_benchmark_run=False,aggregate_factor_two_test_complete=False,
        primitive_checkpoint_rows=1149478,valid_prefix_records_per_format=64,
        native_max_record_bytes=n,image_max_record_bytes=3534568,
        minimum_workspace_diagnostic_bytes=minimum_workspace,
        worker_terminal_peak_plus_minimum_workspace=diagnostic,rss_stop=1610612736,rss_max=2147483648,
        observed_parent_plus_worker_peak=m['peak_process_tree_rss_bytes'],verifier_peak=verifier_peak,
        conservative_combined_peak_including_verifier=combined,
        expanded_accounted_including_reserves=expanded,differential_accounted_including_reserves=differential,
        benchmark_expanded=cert['benchmark_expanded'],artifact_bytes_before_report=storage,
        start_monotonic=summary['start_monotonic'],deadline_monotonic=summary['deadline_monotonic'],
        elapsed_through_verification=time.monotonic()-summary['start_monotonic'],
        qualifications=['lifetime watermark admission can overestimate current live memory',
            'sampled monitoring is not continuous hard-cap enforcement',
            'terminal-selftest high RSS was synthetic injection, not actual allocation',
            'oversized final-only pipe-drain case not executed; synthetic stop reached live branch',
            'gzip-error tests emitted an ignored finalizer warning; clean error cleanup is not established',
            'no full coordinate reception, all-window speed comparison or SAT consequence'])
    (OUT/'verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print('RESULT saved negative verified; maximum native row',n,'image',3534568)
    print('observed combined RSS',m['peak_process_tree_rss_bytes'],'stop/max',1610612736,2147483648)
    print('minimum workspace diagnostic',minimum_workspace,'worker watermark + workspace',diagnostic,'stop',1610612736)
    print('expanded/differential/benchmark',expanded,differential,cert['benchmark_expanded'])
    print('required bounds',137438953472,268435456,1073741824)
    print('complete windows',len(verified),'aggregate speed test incomplete; failures',result['failures'])
    print('evidence',str((OUT/'verification.json').relative_to(ROOT)))


if __name__=='__main__': main()
