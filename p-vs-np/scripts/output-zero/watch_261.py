"""One fail-closed budget for preflight and the complete vertex-0 experiment."""
import sys
import watch_255 as w

def main():
    w.OUT=w.ROOT/'scripts/output-zero/output/coordinate-261'
    w.OUT.mkdir(exist_ok=False)
    test=w.monitor('--selftest',48*2**20,5,'heartbeat-selftest')
    assert test['complete'] and test['stopped'] and test.get('stop_reason')=='rss'
    assert test['samples']>0 and test['exit_code']!=0 and not test['failures']
    assert 'PASS child-process creation blocked' in (w.OUT/'heartbeat-selftest.log').read_text()
    actual=w.monitor('scripts/output-zero/coordinate_261.py',3*w.GiB//2,540,'monitor')
    for key in ('complete','stopped','stop_reason','exit_code','samples','peak_process_tree_rss_bytes','elapsed_seconds','failures'):
        print(key,actual.get(key))
    print('required RSS',2*w.GiB,'stop',3*w.GiB//2,'seconds',600,'artifacts',16*w.GiB,'expanded',128*w.GiB)
    print('evidence',w.OUT.relative_to(w.ROOT))
    if actual.get('exit_code')!=0 or actual['stopped'] or actual['failures']: sys.exit(1)

if __name__=='__main__': main()
