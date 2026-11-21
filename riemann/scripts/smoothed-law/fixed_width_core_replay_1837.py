"""Supplementary ordinary replay, distinct from independent audit1837.

Re-execute the preserved evaluator to check its exact temporary-size
instrumentation and complete original evidence. Never overwrite originals.
"""
from pathlib import Path
import gzip
import hashlib
import importlib.util
import json

BASE = Path(__file__).resolve().parent
REPORT = BASE/'fixed_width_core_replay_check_1837.json'


def main():
    if REPORT.exists():
        raise SystemExit('Preserve replay check1837: refuses overwrite')
    spec = importlib.util.spec_from_file_location('preserved_evaluator1835', BASE/'fixed_width_interval_core_1835.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.OUT = BASE/'fixed_width_core_replay_1837.json'
    module.TRACE = BASE/'fixed_width_core_replay_trace_1837.jsonl.gz'
    module.main()
    original = json.loads((BASE/'fixed_width_interval_core_1835.json').read_text())
    replay = json.loads(module.OUT.read_text())
    checked = []; failures = []
    for key in original:
        if key in ['elapsed_seconds','evidence']:
            continue
        if original[key] != replay[key]:
            failures.append('full evidence field mismatch: '+key)
        checked.append(key)
    for key in ['script_sha256','old_P12_sha256']:
        if original['evidence'][key] != replay['evidence'][key]:
            failures.append('source hash mismatch: '+key)
    old_trace = BASE/'fixed_width_interval_core_trace_1835.jsonl.gz'
    old_digest = hashlib.sha256(gzip.decompress(old_trace.read_bytes())).hexdigest()
    new_digest = hashlib.sha256(gzip.decompress(module.TRACE.read_bytes())).hexdigest()
    if old_digest != new_digest:
        failures.append('complete decompressed trace differs')
    result = {'status':'PASS_COMPLETE_ORDINARY_REPLAY' if not failures else 'STOP_REPLAY_MISMATCH',
              'failures':failures,'full_fields_compared':checked,
              'exact_temporary_sizes':replay['temporary_sizes'],
              'decompressed_trace_hash':new_digest,
              'certificate':str(module.OUT.relative_to(BASE.parent.parent)),
              'trace':str(module.TRACE.relative_to(BASE.parent.parent)),
              'scope':'ordinary original-evaluator replay only; independent audit is fixed_width_core_audit_1837.json',
              'excluded':['elapsed wall time','gzip metadata and artifact paths']}
    REPORT.write_text(json.dumps(result,indent=2)+'\n')
    print(result['status'],'failures:',failures,'; all mathematical fields and entire trace compared')
    print('Temporary maxima:',replay['temporary_sizes']['max_bits'])
    print('Replay check:',REPORT.relative_to(BASE.parent.parent))


if __name__ == '__main__':
    main()
