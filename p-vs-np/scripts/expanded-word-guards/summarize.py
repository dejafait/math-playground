"""Aggregate complete certificate bounds; this does not replace primitive checking."""
import json
from pathlib import Path
HERE=Path(__file__).resolve().parent; ROOT=HERE.parent.parent
path=HERE/'output'/'certificate-188.json'; c=json.loads(path.read_text())
assert c['complete'] and not c['failures']
assert len(c['library'])==24
assert all(m['accepted'] for v in c['library'].values() for m in v.values())
out={'complete':True,'failures':c['failures'],'fixed_templates':len(c['library']),
     'constants':c['constants'],'rejections':len(c['rejections']),'cases':[]}
for case in c['cases']:
    r={'name':case['name'],'positions':len(case['proofs']),'formats':{}}
    for mode in ['native','not-or']:
        ps=[v['formats'][mode] for v in case['proofs']]
        for v in ps:
            assert v['measurement']['accepted'] and all(v['tests'].values())
            for key,mkey in [('lines','lines'),('depth','max_line_depth'),('record_nodes','max_record_nodes'),('bytes','bytes')]:
                assert v['measurement'][mkey]<=v['bounds'][key]
        totals=case['whole_list'][mode]
        assert totals['actual_lines']==sum(v['measurement']['lines'] for v in ps)
        assert totals['actual_bytes']==sum(v['measurement']['bytes'] for v in ps)
        result=dict(totals)
        for key,mkey in [('depth','max_line_depth'),('record_nodes','max_record_nodes')]:
            worst=max(ps,key=lambda v:v['measurement'][mkey])
            result[key]={'actual':worst['measurement'][mkey],'required':worst['bounds'][key]}
        r['formats'][mode]=result
        print(case['name'],mode,'lines',result['actual_lines'],'/',result['required_lines'],
              'bytes',result['actual_bytes'],'/',result['required_bytes'],
              'max depth',result['depth']['actual'],'/',result['depth']['required'],
              'max record nodes',result['record_nodes']['actual'],'/',result['record_nodes']['required'])
    out['cases'].append(r)
out['positions']=sum(v['positions'] for v in out['cases'])
out['metadata_bytes']=sum((ROOT/v['request']).stat().st_size for v in c['cases'])+path.stat().st_size
outpath=HERE/'output'/'summary-188.json'; outpath.write_text(json.dumps(out,indent=2)+'\n')
print('PASS fixed',out['fixed_templates'],'positions',out['positions'],'rejections',out['rejections'],
      'failures',out['failures'],'metadata bytes',out['metadata_bytes'],'certificate',path,'summary',outpath)
