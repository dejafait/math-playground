"""One absolute deadline, no compiler, child-free workers, terminal RSS checks."""
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
OUT=ROOT/'scripts/output-zero/output/cache-265'
STOP=1610612736


def peak():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*(1 if sys.platform=='darwin' else 1024)


def kill(p):
    if p.poll() is None:
        os.killpg(p.pid,signal.SIGTERM)
        try: p.wait(timeout=1)
        except subprocess.TimeoutExpired:
            os.killpg(p.pid,signal.SIGKILL); p.wait(timeout=2)


def monitor(name,deadline,*,mode='main',limit=STOP,storage_limit=16*2**30-2**20,
            target='scripts/output-zero/cache_265.py',heartbeat_timeout=1):
    result=dict(name=name,launched=False,complete=False,stopped=False,failures=[],
        samples=0,worker_peak_rss_bytes=0,parent_peak_rss_bytes=peak(),
        deadline_monotonic=deadline,terminal_peak_rechecked=False,
        qualification='parent plus child-free worker lifetime maxima; sampled heartbeat, not continuous enforcement')
    start=time.monotonic()
    def save():
        result['elapsed_seconds']=time.monotonic()-start
        result['finished_monotonic']=time.monotonic()
        (OUT/(name+'.json')).write_text(json.dumps(result,indent=2)+'\n')
    if start>=deadline:
        result.update(complete=True,stopped=True,stop_reason='expired-start'); save(); return result
    readfd,writefd=os.pipe(); os.set_blocking(readfd,False)
    env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',PYTHONUNBUFFERED='1',
             CACHE265_DEADLINE=str(deadline),CACHE265_TEST=mode,
             CACHE265_PARENT_PEAK=str(peak()),CACHE265_HEARTBEAT_FD=str(writefd))
    with (OUT/(name+'.log')).open('w') as log:
        p=subprocess.Popen([sys.executable,'scripts/output-zero/rss_worker_255.py',str(writefd),target],
            cwd=ROOT,stdout=log,stderr=subprocess.STDOUT,start_new_session=True,pass_fds=(writefd,),env=env)
        result['launched']=True; os.close(writefd)
        selector=selectors.DefaultSelector(); selector.register(readfd,selectors.EVENT_READ)
        last=start; pending=b''; eof=False
        def receive(chunk):
            nonlocal pending,last
            pending+=chunk
            while b'\n' in pending:
                line,pending=pending.split(b'\n',1)
                value=int(line); assert value>0
                result['samples']+=1; last=time.monotonic()
                result['worker_peak_rss_bytes']=max(result['worker_peak_rss_bytes'],value)
        def reason():
            result['parent_peak_rss_bytes']=peak()
            rss=peak()+result['worker_peak_rss_bytes']
            result['peak_process_tree_rss_bytes']=rss
            storage=sum(x.stat().st_size for x in OUT.iterdir() if x.is_file())
            result['artifact_bytes']=storage
            if rss>=limit: return 'rss'
            if time.monotonic()>=deadline: return 'time'
            if storage>=storage_limit: return 'storage'
            if time.monotonic()-last>heartbeat_timeout: return 'heartbeat'
            return None
        try:
            while True:
                if not eof:
                    for key,mask in selector.select(timeout=.02):
                        chunk=os.read(readfd,65536)
                        if chunk: receive(chunk)
                        else:
                            eof=True; selector.unregister(readfd)
                else: time.sleep(.005)
                why=reason()
                if why:
                    result.update(stopped=True,stop_reason=why); kill(p); break
                if p.poll() is not None:
                    # Drain the ENTIRE pipe after exit; terminal samples are load-bearing.
                    while True:
                        try: chunk=os.read(readfd,65536)
                        except BlockingIOError: break
                        if not chunk: break
                        receive(chunk)
                    assert not pending, 'incomplete final heartbeat'
                    result['terminal_peak_rechecked']=True
                    why=reason()
                    if why: result.update(stopped=True,stop_reason=why)
                    break
            result.update(exit_code=p.wait(timeout=2),complete=True)
            if not result['stopped']:
                assert result['samples']>0 and result['terminal_peak_rechecked']
                assert result['peak_process_tree_rss_bytes']<limit
        except BaseException as error:
            result['failures'].append(type(error).__name__+': '+str(error)); kill(p)
        finally:
            selector.close(); os.close(readfd); save()
    return result


def main():
    if sys.argv[1:] == ['--repair-worker-tests']:
        summary=json.loads((OUT/'monitor-summary.json').read_text())
        previous=json.loads((OUT/'certificate.json').read_text())
        assert len(summary['tests'])==6 and 'restore' not in previous and 'comparisons' not in previous
        assert previous['failures']==['AssertionError: accepted corruption: sink-write']
        (OUT/'initial-worker-test-summary.json').write_text(json.dumps(summary,indent=2)+'\n')
        (OUT/'initial-worker-test-certificate.json').write_text(json.dumps(previous,indent=2)+'\n')
        for source in ('cache_265.py','watch_cache_265.py'):
            (OUT/('worker-repaired-'+source)).write_bytes((ROOT/'scripts/output-zero'/source).read_bytes())
        summary['worker_test_repair']='Python 3.15 small gzip writes buffer; test write+flush propagation and preserve original failure; no benchmark repeated'
        summary['main_repaired']=monitor('main-repaired',summary['deadline_monotonic'])
        actual=summary['main_repaired']
        cert=json.loads((OUT/'certificate.json').read_text())
        okay=(actual['complete'] and not actual['failures'] and not actual['stopped'] and actual['exit_code']==0
              and cert['target_complete'] and cert['status']=='PASS' and not cert['failures'])
        summary.update(status='PASS' if okay else 'STOPPED',failures=[] if okay else ['worker test/experiment failed; inspect complete certificates'],
                       elapsed_seconds=time.monotonic()-summary['start_monotonic'],finished_monotonic=time.monotonic(),
                       artifact_bytes=sum(p.stat().st_size for p in OUT.iterdir() if p.is_file()))
        (OUT/'monitor-summary.json').write_text(json.dumps(summary,indent=2)+'\n')
        print('RESULT',summary['status'],'elapsed/required',summary['elapsed_seconds'],'/ 600')
        print('failures',summary['failures'],'evidence',OUT.relative_to(ROOT))
        return 0 if okay else 1
    repair = sys.argv[1:] == ['--repair-preflight']
    if repair:
        prior=json.loads((OUT/'monitor-summary.json').read_text())
        assert len(prior['tests'])==1 and not (OUT/'main.json').exists()
        assert (OUT/'rss-selftest.log').read_text()==''
        assert prior['tests'][0]['peak_process_tree_rss_bytes']==50724864
        (OUT/'initial-preflight-summary.json').write_text(json.dumps(prior,indent=2)+'\n')
        start=prior['start_monotonic']; deadline=prior['deadline_monotonic']
    else:
        start=time.monotonic(); deadline=start+600
        OUT.mkdir(exist_ok=False)
    summary=dict(step=265,start_monotonic=start,deadline_monotonic=deadline,status='INCOMPLETE',
                 tests=[],failures=[],production_pair_emitted=False,compiler_invoked=False,
                 preflight_repair=repair)
    if repair:
        summary['preserved_initial_failure']='initial-preflight-summary.json'
        summary['repair_reason']='48 MiB was below measured 50,724,864-byte combined startup peaks; no allocation or benchmark ran; test threshold 80 MiB, production caps unchanged'
    def save():
        summary.update(elapsed_seconds=time.monotonic()-start,finished_monotonic=time.monotonic(),
                       artifact_bytes=sum(p.stat().st_size for p in OUT.iterdir() if p.is_file()))
        (OUT/'monitor-summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    save()
    try:
        for source in ('cache_265.py','watch_cache_265.py','rss_worker_255.py'):
            (OUT/(('repaired-' if repair else 'executed-')+source)).write_bytes((ROOT/'scripts/output-zero'/source).read_bytes())
        assert (ROOT/'scripts/left-closure/output/native_parser-207.so').is_file()
        rss_name='rss-selftest-repaired' if repair else 'rss-selftest'
        rss=monitor(rss_name,deadline,target='--selftest',limit=80*2**20 if repair else 48*2**20)
        summary['tests'].append(rss); save()
        assert rss['stop_reason']=='rss' and rss['exit_code']!=0 and not rss['failures']
        assert 'PASS child-process creation blocked' in (OUT/(rss_name+'.log')).read_text()
        stall=monitor('stall-selftest',deadline,mode='stall')
        summary['tests'].append(stall); save()
        assert stall['stop_reason']=='heartbeat' and not stall['failures']
        storage=monitor('output-selftest',deadline,mode='output',storage_limit=2**20)
        summary['output_selftest_expanded_bytes']=2*2**20
        summary['tests'].append(storage); save()
        assert storage['stop_reason']=='storage' and not storage['failures']
        terminal=monitor('terminal-selftest',deadline,mode='terminal')
        summary['tests'].append(terminal); save()
        assert terminal['stop_reason']=='rss' and not terminal['failures']
        # The loop also checks live samples; exercise the final-only decision directly.
        summary['terminal_only_unit']=dict(parent_peak=peak(),terminal_worker_peak=STOP,
            summed=peak()+STOP,rejected=peak()+STOP>=STOP,injected=True)
        expired=monitor('expired-start-selftest',min(deadline,time.monotonic()-1))
        summary['tests'].append(expired)
        gap_deadline=min(deadline,time.monotonic()+.02)
        time.sleep(.03)
        gap=monitor('phase-gap-selftest',gap_deadline)
        summary['tests'].append(gap)
        assert all(not x['launched'] and x['stop_reason']=='expired-start' for x in (expired,gap))
        save()
        actual=monitor('main',deadline)
        summary['main']=actual; save()
        assert actual['complete'] and not actual['failures'] and not actual['stopped'] and actual['exit_code']==0
        cert=json.loads((OUT/'certificate.json').read_text())
        assert cert['target_complete'] and cert['status']=='PASS' and not cert['failures']
        assert actual['peak_process_tree_rss_bytes']<STOP and summary['artifact_bytes']<17179869184
        assert time.monotonic()<deadline
        summary['status']='PASS'
    except BaseException as e:
        summary.update(status='STOPPED',failures=[type(e).__name__+': '+str(e)])
    finally: save()
    print('RESULT',summary['status'],'elapsed/required',summary['elapsed_seconds'],'/ 600')
    print('RSS stop/max',STOP,'/ 2147483648; artifacts',summary['artifact_bytes'],'/ 17179869184')
    print('failures',summary['failures'],'evidence',str(OUT.relative_to(ROOT)))
    return 0 if summary['status']=='PASS' else 1


if __name__=='__main__': sys.exit(main())
