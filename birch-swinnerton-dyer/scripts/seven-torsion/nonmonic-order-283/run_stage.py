"""External one-shot watchdog; no retries or resumed stages."""
from pathlib import Path
import json, subprocess, sys, time
R = Path(__file__).resolve().parent
stage = sys.argv[1]
assert stage in ('build_order','verify_order')
start = time.monotonic()
with (R/(stage+'.log')).open('x') as log:
    try:
        result = subprocess.run([sys.executable,'-B',str(R/(stage+'.py'))],
            stdout=log,stderr=subprocess.STDOUT,timeout=181)
        report = {'returncode':result.returncode,'watchdog_fired':False}
    except subprocess.TimeoutExpired:
        report = {'returncode':None,'watchdog_fired':True}
report.update(stage=stage,seconds=time.monotonic()-start,internal_cap=180,
              external_cap=181,required_bytes=134217728)
report['bytes_before_report'] = sum(p.stat().st_size for p in R.iterdir() if p.is_file())
with (R/(stage+'-watchdog.json')).open('x') as out: json.dump(report,out)
print(json.dumps(report))
sys.exit(0 if report['returncode']==0 and report['bytes_before_report']<=134217728 else 1)
