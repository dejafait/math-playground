"""One capped arithmetic stage: complete replay, distinct check, preservation."""
from pathlib import Path
from fractions import Fraction
import hashlib,json,signal,subprocess,sys,time
import dense_check
R=Path(__file__).resolve().parent; U=R.parent
START=time.monotonic(); result={'passed':False,'failures':[],'required_seconds':180,'required_bytes':134217728}
def enc(v):
    if isinstance(v,Fraction):return str(v)
    if isinstance(v,(tuple,list)):return [enc(x) for x in v]
    if isinstance(v,dict):return {k:enc(x) for k,x in v.items()}
    return v
def save(name,value):
    s=json.dumps(enc(value),separators=(',',':'))+'\n'
    assert sum(p.stat().st_size for p in R.rglob('*') if p.is_file())+len(s.encode())<=134217728,'new-evidence byte cap'
    with (R/name).open('x') as f:f.write(s)
def alarm(*_):raise TimeoutError('aggregate 180-second arithmetic cap')
signal.signal(signal.SIGALRM,alarm);signal.alarm(180)
try:
    # The byte-identical verifier imports no producer arithmetic. Its outputs
    # go only to the fresh audit directory; the saved construction is read-only.
    with (R/'fresh-replay.log').open('x') as log:
        done=subprocess.run([sys.executable,'-B',str(R/'verify_incidence.py')],stdout=log,stderr=subprocess.STDOUT,check=True)
    replay=json.loads((R/'replay-report.json').read_text())
    assert replay['passed'] and not replay['failures'],'fresh replay failed'
    old=json.loads((U/'incidence-269/complete-replay-evidence.json').read_text())
    new=json.loads((R/'complete-replay-evidence.json').read_text())
    assert old==new,'complete replay evidence differs'
    assert len(new['residuals'])==6 and all(v==[] for v in new['residuals'].values()),'full replay residuals'
    for key in ('point_standard_columns','point_power_columns','line_columns'):
        assert len(new[key])==48 and all(len(v)==336 for v in new[key]),key
    result['fresh_replay_seconds']=replay['seconds']
    result['distinct']=dense_check.run(R,save)
    dense=json.loads((R/'dense-evidence.json').read_text())
    # Complete evidence, not previews: compare every entry after rational parsing.
    comparison={}
    def rationalize(v):
        if isinstance(v,list):return tuple(rationalize(x) for x in v)
        return Fraction(v)
    for key in ('point_standard_columns','point_power_columns','line_columns','point_original_x','point_original_y'):
        comparison[key]=rationalize(dense[key])==rationalize(new[key])
        assert comparison[key],key+' distinct evidence mismatch'
    def allzero(v):return all(allzero(x) for x in v) if isinstance(v,list) else Fraction(v)==0
    assert all(allzero(v) for v in dense['residuals'].values()),'dense residuals nonzero'
    save('complete-evidence-inspection.json',{'whole_original_fresh_evidence_equal':old==new,'all_map_entries_equal':comparison,'replay_residuals':new['residuals'],'dense_residuals_all_zero':{k:allzero(v) for k,v in dense['residuals'].items()},'all_replay_checks':replay['checks'],'original_rejections':json.loads((U/'incidence-269/rejections.json').read_text()),'fresh_rejections':json.loads((R/'rejections.json').read_text()),'dense_rejections':dense['rejections']})
    result['passed']=True
except Exception as e:
    result['failures'].append(type(e).__name__+': '+str(e))
finally:
    signal.alarm(0)
    manifest=json.loads((R/'originals.json').read_text())
    changed=[p for p,h in manifest.items() if not (U/p).is_file() or hashlib.sha256((U/p).read_bytes()).hexdigest()!=h]
    save('audit-preservation.json',{'count':len(manifest),'changed_or_missing':changed,'passed':not changed})
    if changed:result['passed']=False;result['failures'].append('original files changed or missing')
    result['preserved_files']=len(manifest); result['seconds']=time.monotonic()-START
    result['bytes_before_report']=sum(p.stat().st_size for p in R.rglob('*') if p.is_file())
    save('audit-report.json',result)
print(json.dumps(result));sys.exit(0 if result['passed'] else 1)
