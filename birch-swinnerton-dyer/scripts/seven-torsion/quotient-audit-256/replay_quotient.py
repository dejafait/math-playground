"""Fresh complete replay, original fixture replay, and full evidence inspection."""
from pathlib import Path
from fractions import Fraction
import hashlib,importlib.util,json,signal,time
R=Path(__file__).resolve().parent; U=R.parent; O=U/'quotient-254'
start=time.monotonic()
signal.signal(signal.SIGALRM,lambda *_: (_ for _ in ()).throw(TimeoutError('180-second bound')))
signal.alarm(180)
spec=importlib.util.spec_from_file_location('quotient_verifier',O/'verify_quotient.py')
v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)
def save(name,obj):
    with (R/name).open('x') as f:json.dump(obj,f,indent=2)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
cert=json.loads((O/'quotient.json').read_text())
report=v.verify(cert,[]);save('quotient.json',report)
old=json.loads((O/'complete-replay.json').read_text())
assert report==old,'fresh replay differs from complete retained replay'
stage=json.loads((O/'replay-stage-report.json').read_text())
assert all(stage[k]==val for k,val in report.items()),'stage report mismatch'
assert stage['seconds']<stage['required_seconds']==180
production=json.loads((O/'production-report.json').read_text())
assert production['passed'] and not production['failures'] and production['seconds']<production['required_seconds']==180
for name in ['build_quotient','verify_quotient']:
    wd=json.loads((O/(name+'-watchdog.json')).read_text())
    assert wd['returncode']==0 and not wd['watchdog_fired'] and wd['seconds']<181
    assert wd['bytes_before_report']<=wd['byte_cap']==134217728
    log=json.loads((O/(name+'.log')).read_text())
    ref=production if name=='build_quotient' else stage
    assert log=={k:val for k,val in ref.items() if k!='checks'},'retained log mismatch'
rejections=[]
for name,label,key in [('wrong-x','full_paired_Velu_x_sum','x_numerator'),('wrong-discriminant-inverse','target_discriminant_unit','target_discriminant_inverse')]:
    fixture=json.loads((O/(name+'.json')).read_text())
    intended=json.loads(json.dumps(cert))
    if key=='x_numerator':intended[key][0][0]=str(Fraction(intended[key][0][0])+1)
    else:intended[key][0]=str(Fraction(intended[key][0])+1)
    assert fixture==intended,'fixture contains additional changes'
    checks=[]
    try:v.verify(fixture,checks)
    except ValueError as e:
        assert str(e)==label,(name,str(e),label)
        rejection={'fixture':name+'.json','expected':label,'actual':str(e),'passed':True}
        save(name+'-report.json',dict(rejection,checks_before_failure=checks))
        rejections.append(rejection)
    else:raise AssertionError('altered fixture accepted')
old_pres=json.loads((O/'rejections-and-preservation.json').read_text())
assert old_pres['passed'] and old_pres['changed_or_missing']==[] and old_pres['rejections']==rejections
inventories=[]
for path in [O/'original-manifest.json',O/'production-input-manifest.json',R/'original-manifest.json']:
    data=json.loads(path.read_text());changed=[p for p,d in data.items() if not (U/p).is_file() or sha(U/p)!=d]
    assert not changed,(str(path),changed)
    inventories.append({'manifest':str(path.relative_to(U)),'count':len(data),'changed_or_missing':changed})
assert inventories[0]['count']==old_pres['original_file_count']==152
summary=json.loads((O/'summary.json').read_text())
assert summary['passed'] and summary['actual_degree']==summary['required_degree']==7
assert summary['production_seconds']==production['seconds'] and summary['replay_seconds']==stage['seconds']
assert summary['original_files_preserved']==152 and summary['final_directory_bytes']==sum(p.stat().st_size for p in O.rglob('*') if p.is_file() and '__pycache__' not in p.parts)
result={'passed':True,'failures':[],'complete_replay_checks':len(report['checks']),'original_report_identical':True,'rejections':rejections,'inventories':inventories,'seconds':time.monotonic()-start,'required_seconds':180}
save('evidence.json',result);signal.alarm(0)
print(json.dumps(result))
