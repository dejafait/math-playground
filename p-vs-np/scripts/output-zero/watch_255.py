"""Fail-closed parent watchdog; worker peak heartbeat replaces unavailable ps.

RSS accounting conservatively sums parent and worker lifetime maxima. A missing
heartbeat terminates the worker. No proof data are accepted from the heartbeat.
"""
import json
import os
import resource
import selectors
import signal
import subprocess
import sys
import time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'scripts/output-zero/output/interned-255'
GiB=2**30

def kill(p):
    if p.poll() is None:
        os.killpg(p.pid,signal.SIGTERM)
        try: p.wait(timeout=1)
        except subprocess.TimeoutExpired:
            os.killpg(p.pid,signal.SIGKILL); p.wait(timeout=2)

def monitor(target,limit,seconds,name):
    result=dict(complete=False,stop_threshold_bytes=limit,required_max_rss_bytes=2*GiB,
        required_max_seconds=seconds,interval_seconds=0.02,heartbeat_timeout_seconds=1,
        samples=0,peak_process_tree_rss_bytes=0,worker_peak_rss_bytes=0,
        failures=[],stopped=False,process_tree='parent + worker; worker creation/exec events denied',
        accounting='sum of parent and worker lifetime RSS maxima; conservative')
    path=OUT/(name+'.json'); assert not path.exists(); start=time.monotonic()
    readfd,writefd=os.pipe(); os.set_blocking(readfd,False)
    command=[sys.executable,'scripts/output-zero/rss_worker_255.py',str(writefd),target]
    with (OUT/(name+'.log')).open('w') as log:
        p=subprocess.Popen(command,cwd=ROOT,stdout=log,stderr=subprocess.STDOUT,start_new_session=True,
            pass_fds=(writefd,),env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',PYTHONUNBUFFERED='1'))
        os.close(writefd); selector=selectors.DefaultSelector(); selector.register(readfd,selectors.EVENT_READ)
        last=start; pending=b''
        try:
            while True:
                for key,mask in selector.select(timeout=0.02):
                    chunk=os.read(readfd,65536)
                    pending+=chunk
                    while b'\n' in pending:
                        line,pending=pending.split(b'\n',1); peak=int(line)
                        assert peak>0; result['samples']+=1; last=time.monotonic()
                        result['worker_peak_rss_bytes']=max(result['worker_peak_rss_bytes'],peak)
                parent=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*(1 if sys.platform=='darwin' else 1024)
                rss=parent+result['worker_peak_rss_bytes']
                result['parent_peak_rss_bytes']=parent
                result['peak_process_tree_rss_bytes']=max(result['peak_process_tree_rss_bytes'],rss)
                storage=sum(x.stat().st_size for x in OUT.iterdir() if x.is_file())
                reason='rss' if rss>=limit else 'time' if time.monotonic()-start>=seconds else 'storage' if storage>=15*GiB else 'heartbeat' if time.monotonic()-last>1 else None
                if reason:
                    result.update(stopped=True,stop_reason=reason); kill(p); break
                if p.poll() is not None:
                    # One more pass drains the final report written before exit.
                    chunk=os.read(readfd,65536); pending+=chunk
                    for line in pending.splitlines():
                        result['samples']+=1
                        result['worker_peak_rss_bytes']=max(result['worker_peak_rss_bytes'],int(line))
                    result['peak_process_tree_rss_bytes']=max(result['peak_process_tree_rss_bytes'],parent+result['worker_peak_rss_bytes'])
                    break
            result['exit_code']=p.wait(timeout=2); result['complete']=True
        except BaseException as error:
            result['failures'].append(type(error).__name__+': '+str(error)); kill(p)
        finally:
            selector.close(); os.close(readfd)
            result['elapsed_seconds']=time.monotonic()-start
            result['new_artifact_bytes']=sum(x.stat().st_size for x in OUT.iterdir() if x.is_file())
            path.write_text(json.dumps(result,indent=2)+'\n')
    return result

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    # Prior failed ps preflight is retained. No production was run under it.
    test=monitor('--selftest',48*2**20,5,'heartbeat-selftest')
    assert test['complete'] and test['stopped'] and test.get('stop_reason')=='rss'
    assert test['samples']>0 and test['exit_code']!=0 and not test['failures']
    assert 'PASS child-process creation blocked' in (OUT/'heartbeat-selftest.log').read_text()
    actual=monitor('scripts/output-zero/interned_255.py',3*GiB//2,540,'monitor')
    print('MONITOR',json.dumps({k:actual.get(k) for k in ['complete','stopped','exit_code','samples','peak_process_tree_rss_bytes','elapsed_seconds','failures']}))
    print('required RSS <',2*GiB,'stop threshold',3*GiB//2,'seconds <=600; output',OUT.relative_to(ROOT))
    if actual.get('exit_code')!=0 or actual['stopped'] or actual['failures']: sys.exit(1)
if __name__=='__main__': main()
