"""Inspection shares the original 600-second experimental budget."""
import json
import sys
import watch_255 as w

def main():
    w.OUT=w.ROOT/'scripts/output-zero/output/coordinate-261'
    prior=['monitor.json','heartbeat-selftest.json']
    if (w.OUT/'inspection-monitor.json').exists(): prior.append('inspection-monitor.json')
    used=sum(json.loads((w.OUT/name).read_text())['elapsed_seconds'] for name in prior)
    remaining=590-used
    assert remaining>0
    name='inspection-retry-monitor' if len(prior)==3 else 'inspection-monitor'
    result=w.monitor('scripts/output-zero/inspect_261.py',3*w.GiB//2,remaining,name)
    for key in ('complete','stopped','stop_reason','exit_code','peak_process_tree_rss_bytes','elapsed_seconds','failures'): print(key,result.get(key))
    if result.get('exit_code')!=0 or result['stopped'] or result['failures']: sys.exit(1)

if __name__=='__main__': main()
