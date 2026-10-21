"""One external watchdog: copying through final reports; no retry."""
from pathlib import Path
import json, os, signal, subprocess, sys, time
D = Path(__file__).resolve().parent
CAP = 134217728
START = time.monotonic()
def save(name, value):
    with (D/name).open('x') as f:
        json.dump(value, f, separators=(',', ':')); f.write('\n')
def size():
    return sum(p.stat().st_size for p in D.rglob('*') if p.is_file())
save('run-start.json', {'required_seconds':180, 'required_bytes':CAP})
failures = []
with (D/'audit.log').open('x') as log:
    child = subprocess.Popen([sys.executable, '-B', str(D/'audit.py')],
        stdout=log, stderr=subprocess.STDOUT, start_new_session=True)
    while child.poll() is None:
        if time.monotonic()-START >= 180 or size() > CAP-65536:
            failures.append('combined_time_or_byte_cap')
            os.killpg(child.pid, signal.SIGKILL); child.wait(); break
        time.sleep(.01)
if child.returncode:
    failures.append('audit_exit_'+str(child.returncode))
if time.monotonic()-START >= 180 or size() > CAP-16384:
    failures.append('final_bound')
report = {'status':'STOP' if failures else 'PASS', 'failures':failures,
    'returncode':child.returncode, 'seconds':time.monotonic()-START,
    'bytes_before_watchdog':size(), 'required_seconds':180, 'required_bytes':CAP}
save('watchdog.json', report)
elapsed = time.monotonic()-START
final_bytes = size()
if elapsed >= 180 or final_bytes >= CAP:
    save('late-bound-failure.json', {'seconds':elapsed, 'bytes':final_bytes})
    sys.exit(1)
print(json.dumps({**report, 'seconds_through_watchdog_write':elapsed,
    'final_bytes':final_bytes, 'path':str(D)}))
sys.exit(0 if report['status']=='PASS' else 1)
