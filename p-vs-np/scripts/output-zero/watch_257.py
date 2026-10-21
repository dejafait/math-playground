"""Reuse the tested fail-closed watchdog with fresh output artifacts."""
import json
import sys
import watch_255 as w

def main():
    w.OUT=w.ROOT/'scripts/output-zero/output/copier-257'
    w.OUT.mkdir(parents=True,exist_ok=True)
    if sys.argv[1:]==['--strict']:
        prior=json.loads((w.OUT/'monitor.json').read_text())
        assert prior['complete'] and prior['exit_code']==0 and not prior['stopped'] and not prior['failures']
        used=prior['elapsed_seconds']+json.loads((w.OUT/'heartbeat-selftest.json').read_text())['elapsed_seconds']
        remaining=590-used
        assert remaining>0
        actual=w.monitor('scripts/output-zero/strict_reload_257.py',3*w.GiB//2,remaining,'strict-monitor')
        for k in ('complete','stopped','exit_code','samples','peak_process_tree_rss_bytes','elapsed_seconds','failures'):
            print(k,actual.get(k))
        if actual.get('exit_code')!=0 or actual['stopped'] or actual['failures']: sys.exit(1)
        return
    test=w.monitor('--selftest',48*2**20,5,'heartbeat-selftest')
    assert test['complete'] and test['stopped'] and test.get('stop_reason')=='rss'
    assert test['samples']>0 and test['exit_code']!=0 and not test['failures']
    assert 'PASS child-process creation blocked' in (w.OUT/'heartbeat-selftest.log').read_text()
    actual=w.monitor('scripts/output-zero/copier_257.py',3*w.GiB//2,540,'monitor')
    for k in ('complete','stopped','exit_code','samples','peak_process_tree_rss_bytes','elapsed_seconds','failures'):
        print(k,actual.get(k))
    print('required RSS <',2*w.GiB,'watchdog stop',3*w.GiB//2,'seconds <600; evidence',w.OUT.relative_to(w.ROOT))
    if actual.get('exit_code')!=0 or actual['stopped'] or actual['failures']: sys.exit(1)

if __name__=='__main__': main()
