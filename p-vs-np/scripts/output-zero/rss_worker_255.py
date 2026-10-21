"""Worker-side peak-RSS heartbeat. Parent enforces limit and heartbeat timeout.

The worker has no children: Python process-creation events are forbidden before
any research modules are imported. The inspected native parser creates no child.
"""
import json
import os
import resource
import runpy
import sys
import threading
import time

fd=int(sys.argv[1]); target=sys.argv[2]
def forbid(event,args):
    if event in ('subprocess.Popen','os.system','os.fork','os.forkpty','os.posix_spawn','os.exec'):
        raise RuntimeError('RSS envelope forbids worker child processes and exec')
sys.addaudithook(forbid)
def heartbeat():
    while True:
        peak=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*(1 if sys.platform=='darwin' else 1024)
        os.write(fd,(str(peak)+'\n').encode('ascii'))
        time.sleep(0.02)
threading.Thread(target=heartbeat,daemon=True).start()
if target=='--selftest':
    import subprocess
    try: subprocess.run([sys.executable,'-c','pass'])
    except RuntimeError: print('PASS child-process creation blocked',flush=True)
    else: raise AssertionError('process guard failed')
    block=bytearray(64*2**20); print('allocated self-test memory',flush=True); time.sleep(20)
else:
    sys.argv=sys.argv[2:]
    runpy.run_path(target,run_name='__main__')
# Terminal max-RSS report before normal exit, including short final allocations.
os.write(fd,(str(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*(1 if sys.platform=='darwin' else 1024))+'\n').encode('ascii'))
