from pathlib import Path
import copy,hashlib,json,signal,time
import verify_direction as V
R=Path(__file__).resolve().parent;U=R.parent
t=time.monotonic();signal.alarm(180)
out=R/'rejections';out.mkdir(exist_ok=False)
original=json.loads((R/'original-manifest.json').read_text())
preserved={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest() for p in R.iterdir() if p.is_file() and p.name!='relation-feasibility.json' and not p.name.startswith('build_relation') and p.name!='relation-columns.jsonl'}
c=json.loads((R/'direction.json').read_text());cases=[]
for name,expected in [('wrong_scalar','all_2304_Reynolds_entries_six_scalars'),('wrong_degree','degree_eight_monic'),('wrong_inclusion','entire_B_inclusion'),('wrong_inverse','B_inverse_on_full_image')]:
    d=copy.deepcopy(c);action=None
    if name=='wrong_scalar':
        act=json.loads((U/'scalar-actions-243/actions.json').read_text());act['maps']['2']['B_action'][0][0]='2'
        action=out/'altered-actions.json';action.write_text(json.dumps(act))
        d['action_hash']=hashlib.sha256(action.read_bytes()).hexdigest()
    if name=='wrong_degree':d['h']=d['h'][:-1]
    if name=='wrong_inclusion':d['E_B'][0][0]='2'
    if name=='wrong_inverse':
        # Keep factorization consistent to force inverse-image rather than schema rejection.
        d['K_B'][0][0]=str(V.F(d['K_B'][0][0])+1)
        EB=V.matrix(d['E_B']);KB=V.matrix(d['K_B']);d['R_B']=[[str(z) for z in row] for row in V.mm(EB,KB)]
    path=out/(name+'.json');path.write_text(json.dumps(d))
    try:V.run(path,action);actual='ACCEPTED'
    except Exception as e:actual=str(e)
    signal.alarm(180)
    cases.append({'case':name,'expected':expected,'actual':actual,'passed':expected==actual})
changed=[p for p,h in original.items() if not (U/p).is_file() or hashlib.sha256((U/p).read_bytes()).hexdigest()!=h]
own_changed=[p for p,h in preserved.items() if hashlib.sha256((R/p).read_bytes()).hexdigest()!=h]
report={'passed':all(c['passed'] for c in cases) and not changed and not own_changed,'cases':cases,'upstream_files':len(original),'upstream_changed':changed,'direction_files_checked':len(preserved),'direction_changed':own_changed,'seconds':time.monotonic()-t}
(R/'direction-rejections.json').write_text(json.dumps(report,separators=(',',':'))+'\n')
print(json.dumps(report));signal.alarm(0)
