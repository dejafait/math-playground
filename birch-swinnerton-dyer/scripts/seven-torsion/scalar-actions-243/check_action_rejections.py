#!/usr/bin/env python3
"""Bounded full-schema altered-evidence cases; preserve all original bytes."""
from pathlib import Path
from fractions import Fraction
import copy,hashlib,json,subprocess,sys
ROOT=Path(__file__).resolve().parent

def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    data=json.loads((ROOT/'actions.json').read_text());manifest=json.loads((ROOT/'upstream-manifest.json').read_text())
    originals=[ROOT/'actions.json',ROOT/'build_actions.py',ROOT/'verify_actions.py',ROOT/'verification.json',ROOT/'upstream-replay.json']
    before={str(p):digest(p) for p in originals};cases=[]
    def alter(v):return str(Fraction(v)+1)
    d=copy.deepcopy(data);d['maps']['2']['X'][0][0]=alter(d['maps']['2']['X'][0][0]);cases.append(('wrong-coordinate',d,'geometric_X_2'))
    d=copy.deepcopy(data);d['denominators']['psi3']['inverse'][0][0]=alter(d['denominators']['psi3']['inverse'][0][0]);cases.append(('wrong-inverse',d,'denominator_inverse_psi3'))
    d=copy.deepcopy(data);d['maps']['3']['T_action'][0][1]=alter(d['maps']['3']['T_action'][0][1]);cases.append(('wrong-t-action',d,'full_T_basis_3_1'))
    d=copy.deepcopy(data);d['maps']['4']['B_action'][0][1]=alter(d['maps']['4']['B_action'][0][1]);cases.append(('wrong-B-action',d,'full_B_even_4_1'))
    d=copy.deepcopy(data);del d['denominators']['2Y'];cases.append(('missing-denominator',d,'complete_required_denominators'))
    out=ROOT/'rejections';out.mkdir(exist_ok=True);results=[]
    for name,d,label in cases:
        fixture=out/(name+'.json');report=out/(name+'-report.json');log=out/(name+'.log')
        fixture.write_text(json.dumps(d,separators=(',',':'))+'\n')
        p=subprocess.run([sys.executable,str(ROOT/'verify_actions.py'),'--certificate',str(fixture),'--report',str(report)],capture_output=True,text=True)
        log.write_text(p.stdout+p.stderr);r=json.loads(report.read_text())
        ok=p.returncode==1 and r['status']=='FAIL' and r['failures']==[label]
        results.append({'case':name,'expected':label,'actual':r['failures'],'intended_rejection':ok,'fixture':str(fixture.relative_to(ROOT)),'report':str(report.relative_to(ROOT))})
    after={str(p):digest(p) for p in originals}
    upstream_after={p:digest(Path(p)) for p in manifest}
    result={'status':'PASS' if all(r['intended_rejection'] for r in results) and before==after and manifest==upstream_after else 'FAIL','cases':results,'upstream_original_files':len(manifest),'upstream_preserved':manifest==upstream_after,'new_production_files_preserved':before==after,'production_hashes_before':before,'production_hashes_after':after,'upstream_hashes_after':upstream_after,'failures':[]}
    if result['status']!='PASS':result['failures']=['one or more rejections or byte-preservation checks failed']
    path=ROOT/'rejection-verification.json';path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'intended_rejections':sum(r['intended_rejection'] for r in results),'required_rejections':len(cases),'upstream_original_files':len(manifest),'upstream_preserved':result['upstream_preserved'],'production_preserved':result['new_production_files_preserved'],'failures':result['failures'],'report':str(path)}))
    return 0 if result['status']=='PASS' else 1
if __name__=='__main__':raise SystemExit(main())
