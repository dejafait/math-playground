from pathlib import Path
import json,os,signal,subprocess,sys,time
R=Path(__file__).resolve().parent
start=time.monotonic()
with (R/'audit.log').open('x') as log:
    child=subprocess.Popen([sys.executable,'-B',str(R/'audit.py')],stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
    try:
        rc=child.wait(timeout=181);fired=False
    except subprocess.TimeoutExpired:
        os.killpg(child.pid,signal.SIGKILL);child.wait();rc=None;fired=True
record={'returncode':rc,'watchdog_fired':fired,'seconds':time.monotonic()-start,'required_seconds':181,'arithmetic_seconds':180,'bytes_before_report':sum(p.stat().st_size for p in R.rglob('*') if p.is_file()),'required_bytes':134217728}
with (R/'watchdog.json').open('x') as f:json.dump(record,f)
print(json.dumps(record));sys.exit(0 if rc==0 and record['bytes_before_report']<=134217728 else 1)
