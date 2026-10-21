"""One-shot audit stages; originals are read only, failures are retained."""
import hashlib, json, subprocess, sys, time
from pathlib import Path

sys.set_int_max_str_digits(0)
A = Path(__file__).resolve().parent
ROOT = A.parents[1]
OLD = ROOT / 'scripts/residual-prime-289'
LIMIT = 67108864

def read(p):
    return json.loads(p.read_bytes())

def save(p, obj):
    with p.open('x') as f:
        json.dump(obj, f, separators=(',', ':'))

def digest(p):
    h = hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda: f.read(1048576), b''):
            h.update(b)
    return h.hexdigest()

def snapshot():
    paths = list(OLD.rglob('*'))
    paths += [ROOT / p for p in read(OLD / 'selection.json')['inputs']]
    return {str(p.relative_to(ROOT)): digest(p) for p in paths if p.is_file()}

def prepare(dest):
    dest.mkdir()
    for name in ('selection.json', 'dedekind.json', 'producer-report.json'):
        (dest / name).write_bytes((OLD / name).read_bytes())
    source = (OLD / 'verify.py').read_text()
    assert source.count('ROOT=R.parents[1]') == 1
    adapted = source.replace('ROOT=R.parents[1]', 'ROOT=R.parents[2]')
    (dest / 'verify.py').write_text(adapted)
    assert adapted.replace('ROOT=R.parents[2]', 'ROOT=R.parents[1]') == source

def main():
    stage = sys.argv[1]
    assert stage in ('replay', 'independent')
    out = A / (stage + '-watchdog.json')
    assert not out.exists()
    if stage == 'replay':
        save(A / 'original-hashes-before.json', snapshot())
        prepare(A / 'replay')
        command = [sys.executable, '-B', str(A / 'replay/verify.py')]
    else:
        assert read(A / 'replay-watchdog.json')['status'] == 'PASS'
        command = [sys.executable, '-B', str(A / 'independent.py')]
    start = time.monotonic()
    report = dict(status='FAILED', failures=[], internal_limit=180,
                  external_limit=181, byte_limit=LIMIT)
    try:
        result = subprocess.run(command, capture_output=True, text=True, timeout=181)
        report.update(returncode=result.returncode, stdout=result.stdout,
                      stderr=result.stderr, timeout=False)
        assert result.returncode == 0, 'child_returncode'
        p = A / ('replay/verification-report.json' if stage == 'replay' else 'independent-report.json')
        evidence = read(p)
        assert evidence['failures'] == [], 'child_failure_list'
        assert evidence['seconds'] <= 180, 'internal_time'
        if stage == 'replay':
            assert evidence['status'] == 'VERIFIED_VERDICT', 'full_replay_status'
            assert evidence['original_divisions'] == 14077, 'division_count'
            assert (evidence['selected'], evidence['gcd_degree'], evidence['verdict']) == (31, 2, 'NOT_P_MAXIMAL'), 'replay_verdict'
        else:
            assert evidence['status'] == 'PASS', 'independent_status'
        assert snapshot() == read(A / 'original-hashes-before.json'), 'original_preservation'
        report['status'] = 'PASS'
    except subprocess.TimeoutExpired as e:
        report.update(timeout=True)
        report['failures'].append('external_timeout')
    except Exception as e:
        report['failures'].append(type(e).__name__ + ': ' + str(e))
    report['seconds'] = time.monotonic() - start
    report['aggregate_bytes_before_report'] = sum(p.stat().st_size for p in A.rglob('*') if p.is_file())
    if report['seconds'] > 181 or report['aggregate_bytes_before_report'] + len(json.dumps(report)) > LIMIT:
        report['status'] = 'FAILED'
        report['failures'].append('external_time_or_byte_cap')
    save(out, report)
    print(json.dumps({k: v for k, v in report.items() if k not in ('stdout', 'stderr')}))

if __name__ == '__main__':
    main()
