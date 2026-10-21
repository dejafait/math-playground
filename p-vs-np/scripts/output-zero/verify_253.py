"""Inspect full preserved evidence and bounds; never certify missing streams."""
import gzip
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'scripts/output-zero/output/nonempty-253'

def main():
    cert=json.loads((OUT/'certificate.json').read_text())
    bound=json.loads((OUT/'source-majorants.json').read_text())
    regression=json.loads((OUT/'regression.json').read_text())
    monitor=json.loads((OUT/'external-monitor.json').read_text())
    assert cert['target_complete'] is False and cert['certified_coordinates']==[]
    assert [x['v'] for x in cert['certified_locals']]==list(range(6))
    assert cert['source_checks']['formal_word_zero'] is True
    assert cert['source_checks']['all_dimensioned_tables'] is True
    assert cert['source_checks']['dimensions']==[1,1,0,0,0,0,0]
    assert regression['complete'] and len(regression['rejections'])==6
    actual={mode:dict(lines=0,bytes=0) for mode in ('native','not-or')}
    comparisons=[]
    for local in cert['certified_locals']:
        for mode,m in local['checked']['measurements'].items():
            assert m['accepted'] is True
            assert m['lines']<=bound['J66']
            assert m['bytes']<=bound['formats'][mode]['U66']
            assert (ROOT/m['path']).is_file()
            actual[mode]['lines']+=m['lines']; actual[mode]['bytes']+=m['bytes']
            comparisons.append(dict(vertex=local['v'],format=mode,
                actual_lines=m['lines'],required_max_lines=bound['J66'],
                actual_bytes=m['bytes'],required_max_bytes=bound['formats'][mode]['U66']))
    rss=cert['peak_rss_bytes']; assert rss>cert['caps']['rss']
    assert monitor['resident_bytes']>cert['caps']['rss']
    assert cert['failures']==['KeyboardInterrupt: ']
    storage=sum(p.stat().st_size for p in OUT.iterdir() if p.is_file())
    regression_bytes=0
    for path in OUT.glob('regression-*.jsonl.gz'):
        with gzip.open(path,'rb') as stream:
            regression_bytes+=sum(len(raw) for raw in stream)
    result=dict(complete_evidence_inspection=True,target_complete=False,
        source_and_tables_checked=True,complete_local_pairs=6,
        complete_coordinate_pairs=0,actual_local_totals=actual,
        local_source_bound_comparisons=comparisons,
        cap_checks=dict(rss=dict(actual_peak_bytes=rss,required_max_bytes=cert['caps']['rss'],passed=False),
            compressed_artifacts=dict(actual_bytes=storage,required_max_bytes=cert['caps']['storage'],passed=storage<cert['caps']['storage']),
            expanded_proof_outputs=dict(actual_bytes=cert['expanded_bytes_written']+regression_bytes,required_max_bytes=cert['caps']['expanded'],passed=cert['expanded_bytes_written']+regression_bytes<cert['caps']['expanded']),
            elapsed=dict(actual_worker_seconds=cert['elapsed_seconds'],required_max_seconds=600,passed=cert['elapsed_seconds']<600)),
        regression=dict(complete_positive_pair=True,exact_byte_count=True,malformed_rejections=6),
        failure='Stage-boundary RSS guards did not cover aggregate.load native-tree expansion. External measurement detected excess; tool-session Ctrl-C stopped reception.',
        boundary='Interrupted in balanced-coordinate/aggregate.py load/native during local-package reception, before Closure initialization returned. No coordinate generation or byte preflight reached; no coordinate state archive exists.',
        preserved='Source/envelope/tables/source-only majorants, six complete local pairs, full checks, regressions, monitor and interruption log. No stopped coordinate is certified.',
        pending=cert['pending'],
        mathematical_conclusion='No counterexample to L068 or P versus NP. This default-loader execution fails the approved resource contract; joined execution remains unverified.')
    (OUT/'verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print('RESULT six complete local pairs; zero coordinate/joined pairs; peak RSS',rss,'/',cert['caps']['rss'],'FAIL')
    print('local native/image expanded bytes',*[actual[m]['bytes'] for m in actual],'; evidence', (OUT/'verification.json').relative_to(ROOT))

if __name__=='__main__': main()
