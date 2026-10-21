"""Post-repair exact request/endpoint check, preserving complete prior evidence."""
import copy
import gzip
import json
import build
ep,checker=build.ep,build.checker
OUT=build.HERE/'output'; path=OUT/'certificate-184.json'
cert=json.loads(path.read_text())
assert cert['complete'] and not cert['failures']
assert len(cert['library'])==28 and len(cert['cases'])==4
for fixed in cert['library'].values():
    assert all(v['accepted'] for v in fixed.values())
checks=[]
for case in cert['cases']:
    data=json.loads((build.HERE.parent.parent/case['request']).read_text())
    for mode in ['native','not-or']:
        goals=ep.goals(data,mode)
        assert len(goals)==case['axiom_count']==len(case['proofs'])
        for item,goal in zip(case['proofs'],goals):
            result=item['formats'][mode]; assert result['measurement']['accepted']
            assert all(result['tests'].values())
            stream_path=build.HERE.parent.parent/result['measurement']['path']
            with gzip.open(stream_path,'rt') as stream:
                header=json.loads(next(stream)); last=None; count=0
                for raw in stream: last=json.loads(raw); count+=1
            assert header=={'format':mode,'goal':goal} and last['f']==goal
            assert count==result['measurement']['lines']
            checks.append({'position':item['position'],'case':case['name'],'format':mode,
                           'current_exact_endpoint':True,'records_retained':count})
good=json.loads((OUT/'mixed-repeated-positions-request.json').read_text())
for tag,mutate in [
    ('boolean-constant',lambda d:d['axioms'][0]['left'].__setitem__('left',True)),
    ('nonboolean-sign',lambda d:d['clauses'][0]['left'].__setitem__('negative',0)),
    ('wrong-product-bracketing',lambda d:d['axioms'].__setitem__(1,
      ep.binop('product',d['axioms'][1]['left']['left'],
               ep.binop('product',d['axioms'][1]['left']['right'],d['axioms'][1]['right']))))]:
    data=copy.deepcopy(good); mutate(data)
    reject=OUT/('rejected-'+tag+'.json'); reject.write_text(json.dumps(data,indent=2)+'\n')
    try: ep.request(data)
    except checker.Invalid as err:
        entry={'name':tag,'reason':str(err),'path':str(reject.relative_to(build.HERE.parent.parent))}
        if not any(r['name']==tag for r in cert['rejections']): cert['rejections'].append(entry)
    else: raise AssertionError('malformed exact request accepted '+tag)
cert['strict_reception_supplement']={'complete':True,'endpoint_checks':checks,
    'qualification':'Every request revalidated after typed-tree repair; full primitive checks are the preceding suite, unchanged checker.'}
path.write_text(json.dumps(cert,indent=2)+'\n')
print('PASS current exact requests/endpoints:',len(checks),'; total rejected cases:',len(cert['rejections']))
print('certificate:',path)
for mode in ['native','not-or']:
    measured=[r['formats'][mode] for c in cert['cases'] for r in c['proofs']]
    worst=max(measured,key=lambda r:r['measurement']['bytes'])
    print(mode,'largest bytes actual/required:',worst['measurement']['bytes'],'/',worst['bounds']['bytes'],
          '; lines:',worst['measurement']['lines'],'/',worst['bounds']['lines'],
          '; depth:',worst['measurement']['max_line_depth'],'/',worst['bounds']['depth'])
