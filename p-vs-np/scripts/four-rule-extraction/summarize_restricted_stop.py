"""Metadata/prefix preservation receipt after step-493's terminal cap failure.

Does not rerun a failed reference, evaluate a graph or allocate a new witness.
"""
from pathlib import Path
import ast
import hashlib
from parameterized_input import CAPS, load, require, exact_equal
from receive_selected_commutator import install_evidence_budget

HERE=Path(__file__).resolve().parent
OUT=HERE/'output-493'


def main():
    require(not (OUT/'stop-summary.json').exists(),'refuse existing summary')
    failure=load(OUT/'reception.failure.json')
    error=ast.literal_eval(failure['error'])
    require(failure['accepted_isolated_witness'] is False and failure['stage']=='job 7'
            and error==dict(stage='stored traversal words',actual=20_010_316,
                            required=CAPS['stored_words'],resource='stored_words')
            and failure['arithmetic']['max_stored_words']==error['actual'],
            'retained exact failed guard, not accepted resource bound')
    require(not (OUT/'reception.json').exists(),'no complete receiver acceptance')
    a=sorted((OUT/'references').glob('job-*.json'))
    b=sorted((OUT/'references-received').glob('job-*.json'))
    require([p.name for p in a]==[p.name for p in b]==['job-%03d.json'%i for i in range(7)],
            'exactly seven completed references in both preserved runs')
    for p,q in zip(a,b):
        require(exact_equal(load(p),load(q)),'complete old/incremental prefix reference equality')
    files=sorted(p for p in OUT.rglob('*') if p.is_file())
    manifest={str(p.relative_to(OUT)):dict(bytes=p.stat().st_size,
               sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for p in files}
    summary=dict(outcome='NEGATIVE',accepted_isolated_witness=False,failure=failure,
                 exact_failed_bound=error,completed_reference_jobs=list(range(7)),
                 old_and_incremental_prefix_references_identical=True,
                 failing_job=7,failing_kind='sum_commutator',failing_job_records=81_464,
                 constructor_full_count=load(OUT/'full-count.json'),
                 complete_boolean_polynomial_received=False,
                 complete_outer_occurrences_received=False,
                 complete_all_job_occurrences_received=False,
                 complete_KH_received=False,nonzero_fJ_received=False,
                 complete_reference_jobs_7_through_244=False,
                 interrupted_run_counters_available=False,
                 partial_files=[str(p.relative_to(OUT)) for p in files if p.suffix=='.partial'],
                 evidence_bytes_before_summary=sum(x['bytes'] for x in manifest.values()),
                 required_evidence_bytes=CAPS['certificate_bytes'],files=manifest,
                 scope='Read-only receipt/prefix comparison and inventory; no failed calculation retried.')
    write=install_evidence_budget(OUT)
    write(OUT/'stop-summary.json',summary)
    used=sum(p.stat().st_size for p in OUT.rglob('*') if p.is_file())
    print(dict(outcome='NEGATIVE',failed_resource=error['resource'],actual=error['actual'],
               required=error['required'],complete_reference_jobs=7,
               evidence_bytes=used,required_evidence_bytes=CAPS['certificate_bytes'],
               failures=[error],path=str(OUT/'stop-summary.json')))


if __name__=='__main__':
    main()
