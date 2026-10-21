"""Account for the final report and retention supplement; no proof claim."""
import gzip
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'scripts/output-zero/output/composition-241'
DEST=OUT/'final-accounting.json'


def main():
    assert not DEST.exists(), 'preserve prior evidence'
    cert=json.loads((OUT/'certificate.json').read_text())
    retained=json.loads((OUT/'retention-check.json').read_text())
    assert cert['complete'] and retained['complete'] and cert['failures']==retained['failures']==[]
    pair={OUT/f'output-zero.{m}.jsonl.gz' for m in ('native','not-or')}
    ancillary=0
    for path in OUT.iterdir():
        if path in pair: continue
        if path.suffix=='.gz':
            with gzip.open(path,'rb') as stream:
                while True:
                    data=stream.read(1048576)
                    if not data: break
                    ancillary+=len(data)
        else: ancillary+=path.stat().st_size
    proofs=sum(x['bytes'] for x in cert['output']['measurements'].values())
    fixed=cert['required']['original_parameters']['fixed_library_bytes']
    result=dict(complete=True,failures=[],proof_uncompressed_bytes=proofs,
        fixed_library_uncompressed_bytes=fixed,ancillary_uncompressed_bytes=0,
        full_output_and_fixed_libraries_bytes=0,
        ancillary_required_bytes=cert['required']['metadata_bytes'],
        full_output_source_required_bytes=cert['required']['full_output_bytes'],
        qualification='Accounting only; full primitive/image/import checks remain in certificate.json and original-template/nested-occurrence checks in retention-check.json. Every ancillary artifact, including this final report and all rejection witnesses, is paid uncompressed.')
    for _ in range(10):
        raw=(json.dumps(result,indent=2)+'\n').encode('ascii')
        value=ancillary+len(raw)
        if result['ancillary_uncompressed_bytes']==value: break
        result['ancillary_uncompressed_bytes']=value
        result['full_output_and_fixed_libraries_bytes']=proofs+fixed+value
    else: raise AssertionError('accounting serialization did not stabilize')
    assert result['ancillary_uncompressed_bytes']<=result['ancillary_required_bytes']
    assert result['full_output_and_fixed_libraries_bytes']<=result['full_output_source_required_bytes']
    assert result['full_output_and_fixed_libraries_bytes']<=cert['actual_accounting']['full_output_and_fixed_libraries_bytes']
    DEST.write_bytes(raw)
    print('PASS final full uncompressed charge',result['full_output_and_fixed_libraries_bytes'],
          '<=',result['full_output_source_required_bytes'],'bytes; failures [] certificate',DEST.relative_to(ROOT))


if __name__=='__main__': main()
