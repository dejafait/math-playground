"""Build-accounting admission only; never invokes a compiler or loads a pool.

Run once after creating the incomplete certificate with its absolute deadline.
This attempt stops if its process-tree sampler cannot be started. A child's
terminal ru_maxrss alone does not account for overlapping compiler descendants.
"""
import json
import pathlib
import resource
import shutil
import subprocess
import sys
import time

OUT = pathlib.Path(__file__).resolve().parent / 'output/serializer-263'


def main():
    path = OUT / 'certificate.json'
    cert = json.loads(path.read_text())
    assert cert['status'] == 'INCOMPLETE'
    evidence = OUT / 'build-accounting-preflight.json'
    assert not evidence.exists()
    command = ['/bin/ps', '-axo', 'pid=,ppid=,rss=']
    result = dict(command=command, launched=False, available=False,
                  compiler_path=shutil.which('clang++'),
                  compiler_invoked=False, checkpoint_loaded=False,
                  deadline_monotonic=cert['deadline_monotonic'])
    if time.monotonic() >= cert['deadline_monotonic'] - 30:
        result['failure'] = 'absolute deadline: no subsequent work launched'
    else:
        try:
            proc = subprocess.run(command, capture_output=True, text=True,
                                  timeout=min(3, cert['deadline_monotonic'] - time.monotonic()))
            result.update(launched=True, exit_code=proc.returncode,
                          stderr=proc.stderr, sampled_processes=len(proc.stdout.splitlines()),
                          available=proc.returncode == 0 and bool(proc.stdout.strip()))
            if not result['available']:
                result['failure'] = 'process-tree sampling unavailable'
        except (OSError, subprocess.TimeoutExpired) as error:
            result.update(failure=type(error).__name__ + ': ' + str(error),
                          errno=getattr(error, 'errno', None))
    result['elapsed_seconds'] = time.monotonic() - cert['start_monotonic']
    result['preflight_terminal_peak_rss_bytes'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * (1 if sys.platform == 'darwin' else 1024)
    result['qualification'] = 'Preflight parent terminal peak only; no build/worker resource certification.'
    evidence.write_text(json.dumps(result, indent=2) + '\n')
    cert.update(status='ADMITTED' if result['available'] else 'STOPPED_BEFORE_BUILD',
                target_complete=False, compiler_invoked=False, checkpoint_loaded=False,
                native_exporter_implemented=False, new_proof_payload_bytes=0,
                evidence=str(evidence.relative_to(OUT.parents[3])),
                failures=[] if result['available'] else [result['failure']],
                not_run=['compiler/ABI/zlib checks', 'owned checkpoint validation',
                         'serializer implementation', 'full-byte differentials',
                         'gzip/error tests', 'worker monitoring/deadline self-tests',
                         'valid-prefix replay', 'factor-two performance comparison'])
    cert['elapsed_seconds'] = time.monotonic() - cert['start_monotonic']
    path.write_text(json.dumps(cert, indent=2) + '\n')
    print('build accounting available:', result['available'])
    print('failure:', result.get('failure'))
    print('elapsed/required seconds:', cert['elapsed_seconds'], '/', 600)
    print('compiler invoked:', cert['compiler_invoked'], '; expanded proof payload: 0')
    print('evidence:', evidence)
    return 0 if result['available'] else 1


if __name__ == '__main__':
    sys.exit(main())
